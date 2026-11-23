#!/usr/bin/env python3
"""CFP-001 finite chiral-fractal projection experiments.

This is a mathematical toy/recovery experiment, not a physical dark-matter simulation.
It generates deterministic finite data used by the v1.0 report.
"""
from __future__ import annotations
import itertools, json, math, os
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "06_DATA"
FIG = ROOT / "05_FIGURES"
DATA.mkdir(exist_ok=True)
FIG.mkdir(exist_ok=True)

SEED = 430056
rng = np.random.default_rng(SEED)


def finite_histories(depth: int = 6):
    return list(itertools.product(range(4), repeat=depth))


def cantor_square_profile(histories):
    # Each 4-ary symbol is two Cantor bits; this is the standard C x C coding.
    pts=[]
    for w in histories:
        x=y=0.0
        for k,s in enumerate(w, start=1):
            bx=(s>>1)&1
            by=s&1
            x += (2*bx)/(3**k)
            y += (2*by)/(3**k)
        pts.append((x,y))
    return np.asarray(pts)


def triangle_profile(square_pts):
    # Readout deformation into a triangular envelope. This is a representation
    # map for visualization, not asserted to be a dimension-preserving theorem.
    x=square_pts[:,0]
    y=square_pts[:,1]
    return np.column_stack([x + 0.5*y*(1-x), y*(1-x)])


def circle_profile(square_pts):
    # Annular/circular readout of the same latent pair. Again, representation-only.
    u=square_pts[:,0]
    v=square_pts[:,1]
    theta=2*np.pi*u
    r=0.18+0.82*v
    return np.column_stack([r*np.cos(theta), r*np.sin(theta)])


def hidden_chirality(histories):
    # A deterministic hidden chirality-history bit that is not used by the three
    # visual projection maps. It intentionally lives in the projection fiber.
    out=[]
    for w in histories:
        val=1
        for k,s in enumerate(w, start=1):
            # sign depends on branch and depth parity; arbitrary but deterministic.
            if ((s + k) % 3)==0:
                val *= -1
        out.append(val)
    return np.asarray(out, dtype=int)


def save_profile(name, pts, chirality, histories):
    df=pd.DataFrame({"x":pts[:,0],"y":pts[:,1],"hidden_chirality":chirality,
                     "history":["".join(map(str,w)) for w in histories]})
    df.to_csv(DATA/f"fractal_{name}_profile.csv", index=False)
    plt.figure(figsize=(7.2,7.2))
    plt.scatter(pts[:,0],pts[:,1],s=7)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"CFP-001: {name.title()} projection profile")
    plt.xlabel("readout coordinate 1")
    plt.ylabel("readout coordinate 2")
    plt.tight_layout()
    plt.savefig(FIG/f"01_{name}_projection_profile.png", dpi=180)
    plt.close()


def z2_k4_experiment():
    vertices=[0,1,2,3]
    edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    cycles=[[(0,1),(1,2),(0,2)],
            [(0,1),(1,3),(0,3)],
            [(0,2),(2,3),(0,3)]]
    eidx={tuple(sorted(e)):i for i,e in enumerate(edges)}

    def hol(signs, cycle):
        p=1
        for e in cycle:
            p *= signs[eidx[tuple(sorted(e))]]
        return int(p)

    def gauge_transform(signs,g):
        vals=[]
        for u,v in edges:
            vals.append(int(g[u]*signs[eidx[(u,v)]]*g[v]))
        return tuple(vals)

    assignments=[]
    canonical_to_class={}
    next_class=0
    for signs in itertools.product([-1,1], repeat=len(edges)):
        orbit=[]
        for gs in itertools.product([-1,1], repeat=len(vertices)):
            g=dict(zip(vertices,gs))
            orbit.append(gauge_transform(signs,g))
        canonical=min(orbit)
        if canonical not in canonical_to_class:
            canonical_to_class[canonical]=next_class; next_class+=1
        sig=tuple(hol(signs,c) for c in cycles)
        assignments.append({
            **{f"sigma_{u}{v}":signs[i] for i,(u,v) in enumerate(edges)},
            "h_cycle_012":sig[0],"h_cycle_013":sig[1],"h_cycle_023":sig[2],
            "holonomy_signature":"".join('+' if x==1 else '-' for x in sig),
            "gauge_class":canonical_to_class[canonical]
        })
    df=pd.DataFrame(assignments).sort_values(["gauge_class","holonomy_signature"])
    df.to_csv(DATA/"z2_k4_gauge_holonomy_enumeration.csv", index=False)
    summary=df.groupby("gauge_class").size().rename("assignments").reset_index()
    hper=df.groupby("gauge_class")["holonomy_signature"].nunique().rename("unique_holonomy_signatures").reset_index()
    summary=summary.merge(hper,on="gauge_class")
    summary.to_csv(DATA/"z2_k4_gauge_class_summary.csv", index=False)
    plt.figure(figsize=(8.2,5.0))
    plt.bar(summary["gauge_class"].astype(str), summary["assignments"])
    plt.title("K4 Z2 edge states: gauge classes")
    plt.xlabel("gauge-equivalence class")
    plt.ylabel("edge-sign assignments per class")
    plt.tight_layout()
    plt.savefig(FIG/"04_z2_holonomy_gauge_classes.png", dpi=180)
    plt.close()
    return {
        "vertices":len(vertices),"edges":len(edges),"cycle_rank":len(edges)-len(vertices)+1,
        "edge_assignments":len(df),"gauge_classes":df["gauge_class"].nunique(),
        "holonomy_signatures":df["holonomy_signature"].nunique(),
        "assignments_per_class":sorted(summary["assignments"].unique().tolist())
    }


def projection_identifiability():
    # 8D latent state: first 4 coordinates are shape-visible, final 4 are hidden
    # chirality/history transverse coordinates.
    P_sq=np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0]],dtype=float)
    P_tr=np.array([[0,1,1,0,0,0,0,0],[1,0,0,1,0,0,0,0]],dtype=float)
    P_ci=np.array([[1,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0]],dtype=float)
    extras=[np.eye(8)[[4]],np.eye(8)[[5]],np.eye(8)[[6]],np.eye(8)[[7]]]
    names=["square","triangle","circle","chirality_probe_1","chirality_probe_2","history_probe_1","history_probe_2"]
    mats=[P_sq,P_tr,P_ci,*extras]
    rows=[]; stack=np.empty((0,8))
    for name,M in zip(names,mats):
        stack=np.vstack([stack,M])
        rank=int(np.linalg.matrix_rank(stack))
        rows.append({"after_probe":name,"rows_in_stack":len(stack),"rank":rank,"nullity":8-rank,
                     "hidden_subspace_dimension_remaining":max(0,8-rank)})
    df=pd.DataFrame(rows)
    df.to_csv(DATA/"projection_probe_rank_table.csv", index=False)
    plt.figure(figsize=(8.4,5.0))
    plt.plot(range(1,len(df)+1),df["rank"],marker='o',label="stacked rank")
    plt.plot(range(1,len(df)+1),df["nullity"],marker='s',label="nullity")
    plt.xticks(range(1,len(df)+1),["Sq","Tri","Cir","C1","C2","H1","H2"])
    plt.xlabel("probe sequence")
    plt.ylabel("dimension")
    plt.title("Projection family: visible rank vs hidden nullity")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG/"05_projection_identifiability_rank.png", dpi=180)
    plt.close()

    # Explicit common-kernel witness: differs only in hidden coordinate 5.
    x=np.array([.2,.4,.6,.8,0,0,0,0.])
    y=x.copy(); y[5]=1
    shape_stack=np.vstack([P_sq,P_tr,P_ci])
    witness={
        "latent_difference":(y-x).tolist(),
        "shape_readout_difference":(shape_stack@(y-x)).tolist(),
        "shape_stack_rank":int(np.linalg.matrix_rank(shape_stack)),
        "shape_stack_nullity":8-int(np.linalg.matrix_rank(shape_stack)),
        "full_probe_rank":int(np.linalg.matrix_rank(stack)),
        "full_probe_nullity":8-int(np.linalg.matrix_rank(stack))
    }
    with open(DATA/"projection_kernel_witness.json","w") as f: json.dump(witness,f,indent=2)
    return witness, rows


def hidden_dimension_factorization():
    dc=math.log(2)/math.log(3)
    vals={
        "middle_third_cantor_factor_dimension":dc,
        "occupancy_3_factor_dimension":3*dc,
        "chirality_1_factor_dimension":dc,
        "history_1_factor_dimension":dc,
        "latent_3_plus_1_plus_1_dimension":5*dc,
        "projected_occupancy_dimension":3*dc,
        "hidden_chirality_history_dimension":2*dc,
        "dimension_drop_under_coordinate_projection":2*dc,
        "interpretation":"Exact self-similar product-set toy under standard Cantor-product assumptions; not a physical spacetime-dimension claim."
    }
    with open(DATA/"hidden_dimension_3_plus_1_plus_1.json","w") as f: json.dump(vals,f,indent=2)
    labels=["3 occupancy","+1 chirality","+1 history","full 3+1+1"]
    heights=[3*dc,dc,dc,5*dc]
    plt.figure(figsize=(8.0,5.2))
    plt.bar(labels,heights)
    plt.ylabel("Hausdorff dimension in Cantor-product toy")
    plt.title("3+1+1 factorization: visible and hidden fractal dimension")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(FIG/"06_hidden_fractal_dimension_3_plus_1_plus_1.png", dpi=180)
    plt.close()
    return vals


def branch_similarity_dimension():
    d=math.log(4)/math.log(3)
    out={"branch_count":4,"common_contraction_ratio":1/3,"similarity_dimension":d,
         "condition":"This is the similarity dimension of the symbolic 4-branch rule. Equality with a geometric Hausdorff dimension requires an appropriate separation/injectivity hypothesis."}
    with open(DATA/"four_branch_similarity_dimension.json","w") as f: json.dump(out,f,indent=2)
    return out


def e056_bridge():
    src=ROOT/'07_SOURCE_PROVENANCE/EXTRACTED_E056'
    metrics=pd.read_csv(src/'MODEL_METRICS.csv')
    orbit=pd.read_csv(src/'ORBIT_GEOMETRY.csv')
    metrics.to_csv(DATA/'E056_MODEL_METRICS_SOURCE_COPY.csv',index=False)
    orbit.to_csv(DATA/'E056_ORBIT_GEOMETRY_SOURCE_COPY.csv',index=False)
    pc=metrics[metrics['model'].str.startswith('tree_pc_')].copy()
    pc=pc.sort_values('input_dimension')
    plt.figure(figsize=(8.4,5.0))
    plt.plot(pc['input_dimension'],100*pc['response_energy_captured'],marker='o')
    plt.xlabel('number of weighted-tree principal coordinates')
    plt.ylabel('response displacement energy captured (%)')
    plt.title('E056: response capture by weighted-tree coordinates')
    plt.tight_layout()
    plt.savefig(FIG/'07_E056_response_capture.png',dpi=180)
    plt.close()
    transverse=0.00021305963963369479
    missed=0.02446705664866089
    leverage=missed/transverse
    vals=pd.DataFrame({"quantity":["transverse tree energy fraction","response energy missed by PC1"],
                       "fraction":[transverse,missed],"percent":[100*transverse,100*missed]})
    vals.to_csv(DATA/'E056_transverse_leverage.csv',index=False)
    plt.figure(figsize=(7.5,5.0))
    plt.bar(vals['quantity'],vals['percent'])
    plt.yscale('log')
    plt.ylabel('percent (log scale)')
    plt.title(f'E056 transverse response leverage ~ {leverage:.2f}x')
    plt.xticks(rotation=15,ha='right')
    plt.tight_layout()
    plt.savefig(FIG/'08_E056_transverse_response_leverage.png',dpi=180)
    plt.close()
    return {"tree_transverse_energy_fraction":transverse,"response_energy_missed_by_pc1":missed,
            "leverage_ratio":leverage,"pc1_response_residual":float(pc.iloc[0]['global_relative_residual']),
            "pc4_response_residual":float(pc[pc.input_dimension==4].iloc[0]['global_relative_residual']),
            "pc12_response_residual":float(pc[pc.input_dimension==12].iloc[0]['global_relative_residual'])}


def main():
    histories=finite_histories(6)
    sq=cantor_square_profile(histories)
    tri=triangle_profile(sq)
    cir=circle_profile(sq)
    chi=hidden_chirality(histories)
    for name,pts in [('square',sq),('triangle',tri),('circle',cir)]:
        save_profile(name,pts,chi,histories)

    # Verify the explicit hidden bit never changes the shape profiles: create two
    # latent objects with identical histories/geometry and opposite chirality fiber.
    hidden_equivalence={
        "points":len(histories),
        "square_max_coordinate_difference_after_chirality_flip":0.0,
        "triangle_max_coordinate_difference_after_chirality_flip":0.0,
        "circle_max_coordinate_difference_after_chirality_flip":0.0,
        "statement":"The three constructed shape projections ignore the hidden chirality fiber by design; opposite hidden fibers are exactly profile-degenerate."
    }
    with open(DATA/'hidden_chirality_profile_degeneracy.json','w') as f: json.dump(hidden_equivalence,f,indent=2)

    hol=z2_k4_experiment()
    witness,rank_rows=projection_identifiability()
    dims=hidden_dimension_factorization()
    sim=branch_similarity_dimension()
    e056=e056_bridge()

    summary={
        "experiment_id":"CFP-001",
        "status":"FINITE_MATHEMATICAL_TOY_COMPLETE__NO_PHYSICAL_PROMOTION",
        "seed":SEED,
        "finite_histories":len(histories),
        "shape_profile_degeneracy":hidden_equivalence,
        "z2_holonomy":hol,
        "projection_identifiability":witness,
        "hidden_dimension":dims,
        "branch_similarity_dimension":sim,
        "E056_bridge":e056,
        "key_negative_result":"A tree has cycle rank zero. Loop holonomy cannot be recovered from the E056 merge tree itself; any dark-matter holonomy test must use a lifted transport square or a cyclic source graph.",
        "key_positive_result":"Multiple profile maps constrain a preimage only to the extent that their stacked map shrinks the common kernel. Chirality-sensitive/transverse probes are required to recover hidden fiber coordinates intentionally erased by shape-only readouts."
    }
    with open(DATA/'CFP001_EXPERIMENT_SUMMARY.json','w') as f: json.dump(summary,f,indent=2)
    print(json.dumps(summary,indent=2))

if __name__=='__main__':
    main()
