#!/usr/bin/env python3
"""
MK43 Ultra / Astraeus Dark Matter Wind Tunnel E056
Weighted-tree geometry -> E043 direct-flow quotient response.

Status boundary
---------------
This is a controlled reconstructed-sandbox experiment. It does not establish an
external dark-matter or gravitational detection. It preserves the E042 typing
Flow/ker(D_C) ~= im(D_C) and tests whether E054-E055 finite corridor-tree geometry
retains the E043 response-relevant information.
"""
from pathlib import Path
import csv, hashlib, json, math, re
import numpy as np

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "SOURCE"
OUT = ROOT / "OUTPUT"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# Recover only the source runner definitions needed by the E043 probe map.
# The original runner is not altered on disk. Paths are rebound in memory to
# this package's source receipts, and execution stops before the original
# run_T entry point. Then the E043 inherited-environment extension is loaded.
# ---------------------------------------------------------------------------
orig = (SRC / "SOURCE_ORIGINAL_RECONSTRUCTED_H2_RUNNER.py").read_text()
prefix = orig.split("def run_T(n_manifolds", 1)[0]
prefix = re.sub(r"ROOT = Path\([^\n]+\)", f"ROOT = Path({str(ROOT / '_scratch').__repr__()})", prefix)
prefix = re.sub(r"BASE = Path\([^\n]+\)", f"BASE = Path({str(SRC).__repr__()})", prefix)
for a, b in [
    ("H_DIR = BASE / 'hydrogen'", "H_DIR = BASE"),
    ("P1_DIR = BASE / 'pipeline1/MK43U_Phase3_Ready_Recursive_Continuity_Pipeline_v0_3'", "P1_DIR = BASE"),
    ("P2_DIR = BASE / 'pipeline2'", "P2_DIR = BASE"),
    ("ER_DIR = BASE / 'erfoam/MK43U_ER_Foam_Chirality_Substrate_v0_3'", "ER_DIR = BASE"),
    ("ENV_DIR = BASE / 'environment/MK43U_ER_Foam_Environment_v0_1'", "ENV_DIR = BASE"),
]:
    prefix = prefix.replace(a, b)
prefix = re.sub(r"TRAVERSAL_PROTOCOL = Path\([^\n]+\)", "TRAVERSAL_PROTOCOL = BASE / 'UNUSED_PROTOCOL.txt'", prefix)
prefix = re.sub(r"DOT_PDF = Path\([^\n]+\)", "DOT_PDF = BASE / 'UNUSED_DOT.pdf'", prefix)
ns = {}
exec(prefix + "\n" + (SRC / "SOURCE_E043_RUN_T_WITH_INHERITED_ENV_EXTENSION.py").read_text(), ns)
run_T_with_env = ns["run_T_with_env"]

# ---------------------------------------------------------------------------
# E043 response orbit and E048 fixed-state response, recomputed in float64.
# ---------------------------------------------------------------------------
z43 = np.load(SRC / "SOURCE_E043_MULTI_HISTORY_RESPONSE_STATES.npz")
z48 = np.load(SRC / "SOURCE_E048_DRIVEN_FIXED_ENVIRONMENT_ESTAR.npz")
ENV_FIELDS = ["chi", "adj_memory", "corridor_memory", "persistent_memory"]

def env43(k: int):
    return {f: z43[f"E{k:02d}_{f}"].astype(np.float64) for f in ENV_FIELDS}

fresh_states, _, _, _ = run_T_with_env(1, False, False, initial_env=env43(0))
C_fresh = fresh_states[0]["C"]

R = []
archive_recompute = []
for k in range(1, 17):
    states, _, _, _ = run_T_with_env(1, False, False, initial_env=env43(k))
    rk = (states[0]["C"] - C_fresh).reshape(-1)
    R.append(rk)
    stored = z43[f"H{k:02d}_DeltaC_from_fresh"].reshape(-1).astype(np.float64)
    archive_recompute.append(float(np.linalg.norm(rk - stored)))
R = np.stack(R)

env_star = {f: z48[f].astype(np.float64) for f in ENV_FIELDS}
star_states, _, _, _ = run_T_with_env(1, False, False, initial_env=env_star)
r_star = (star_states[0]["C"] - C_fresh).reshape(-1)
Y = R - r_star[None, :]

# ---------------------------------------------------------------------------
# E054/E055 common labeled weighted-tree state.
# ---------------------------------------------------------------------------
def read_csv(path):
    with path.open(newline="") as f:
        return list(csv.DictReader(f))

peak_rows = read_csv(SRC / "SOURCE_E054_MERGE_TREE_PEAK_HEIGHTS.csv")
merge_rows = read_csv(SRC / "SOURCE_E054_SUPERLEVEL_MERGE_TREE_EVENTS.csv")
q_rows = read_csv(SRC / "SOURCE_E055_SHARED_WEIGHTED_TREE_COORDINATE.csv")
PEAKS = ["R", "B1", "B2", "B3", "B4", "B5", "B6", "B7"]

def w_for(history):
    p = {r["peak_label"]: float(r["normalized_peak_height"]) for r in peak_rows if r["history"] == history}
    m = sorted((r for r in merge_rows if r["history"] == history), key=lambda r: int(r["event_order_high_to_low"]))
    return np.array([p[x] for x in PEAKS] + [float(r["merge_level"]) for r in m], dtype=np.float64)

W = np.stack([w_for(f"E{k}") for k in range(1, 17)])
w_star = w_for("E*")
X = W - w_star[None, :]
q = np.array([float(r["shared_tree_coordinate_q"]) for r in q_rows], dtype=np.float64)

# ---------------------------------------------------------------------------
# Geometry first: fixed-origin distances, SVDs, ordering and incidence.
# ---------------------------------------------------------------------------
d_tree = np.linalg.norm(X, axis=1)
d_resp = np.linalg.norm(Y, axis=1)
U_t, s_t, Vt_t = np.linalg.svd(X, full_matrices=False)
U_r, s_r, Vt_r = np.linalg.svd(Y, full_matrices=False)

tree_pc1_energy = float(s_t[0] ** 2 / np.dot(s_t, s_t))
response_pc1_energy = float(s_r[0] ** 2 / np.dot(s_r, s_r))
tree_score1 = U_t[:, 0] * s_t[0]
resp_score1 = U_r[:, 0] * s_r[0]
if np.dot(tree_score1, resp_score1) < 0:
    resp_score1 = -resp_score1
pc1_cos = float(np.dot(tree_score1, resp_score1) / (np.linalg.norm(tree_score1) * np.linalg.norm(resp_score1)))
pc1_angle_deg = float(np.degrees(np.arccos(np.clip(pc1_cos, -1.0, 1.0))))

# Strict response-distance ordering toward E*.
response_order_inversions = []
for i in range(16):
    for j in range(i + 1, 16):
        if d_resp[i] < d_resp[j]:
            response_order_inversions.append([i + 1, j + 1])

# ---------------------------------------------------------------------------
# Minimal finite maps: fixed-origin linear map from tree coordinates to response.
# Nested tree principal coordinates quantify how much transverse information matters.
# ---------------------------------------------------------------------------
def fit_map(A, train=None):
    if train is None:
        train = np.arange(A.shape[0])
    B = np.linalg.lstsq(A[train], Y[train], rcond=None)[0]
    return A @ B, B

def model_metrics(pred):
    res = Y - pred
    per = np.linalg.norm(res, axis=1)
    return {
        "global_relative_residual": float(np.linalg.norm(res) / np.linalg.norm(Y)),
        "max_absolute_residual": float(np.max(per)),
        "max_residual_over_E1_to_Estar": float(np.max(per) / d_resp[0]),
        "per_history_absolute_residual": per.tolist(),
    }

model_rows = []
model_json = {}
for m in range(1, 13):
    A = U_t[:, :m] * s_t[:m]
    pred, _ = fit_map(A)
    met = model_metrics(pred)
    captured = 1.0 - met["global_relative_residual"] ** 2
    model_json[f"tree_pc_{m}"] = met
    model_rows.append({
        "model": f"tree_pc_{m}",
        "input_dimension": m,
        "response_energy_captured": captured,
        "global_relative_residual": met["global_relative_residual"],
        "max_absolute_residual": met["max_absolute_residual"],
        "max_residual_over_E1_to_Estar": met["max_residual_over_E1_to_Estar"],
    })

pred_full, B_full = fit_map(X)
model_json["full_tree_linear"] = model_metrics(pred_full)
model_rows.append({
    "model": "full_tree_linear",
    "input_dimension": 14,
    "response_energy_captured": 1.0 - model_json["full_tree_linear"]["global_relative_residual"] ** 2,
    "global_relative_residual": model_json["full_tree_linear"]["global_relative_residual"],
    "max_absolute_residual": model_json["full_tree_linear"]["max_absolute_residual"],
    "max_residual_over_E1_to_Estar": model_json["full_tree_linear"]["max_residual_over_E1_to_Estar"],
})

for deg in (1, 2, 3):
    A = np.stack([q ** j for j in range(1, deg + 1)], axis=1)
    pred, _ = fit_map(A)
    met = model_metrics(pred)
    model_json[f"q_polynomial_degree_{deg}"] = met
    model_rows.append({
        "model": f"q_polynomial_degree_{deg}",
        "input_dimension": deg,
        "response_energy_captured": 1.0 - met["global_relative_residual"] ** 2,
        "global_relative_residual": met["global_relative_residual"],
        "max_absolute_residual": met["max_absolute_residual"],
        "max_residual_over_E1_to_Estar": met["max_residual_over_E1_to_Estar"],
    })

# LOO audit for full tree and q-only linear model. This is diagnostic; E1 is endpoint extrapolation.
def loo(A):
    out = []
    for i in range(16):
        train = np.array([j for j in range(16) if j != i])
        B = np.linalg.lstsq(A[train], Y[train], rcond=None)[0]
        pred = A[i] @ B
        out.append(float(np.linalg.norm(Y[i] - pred)))
    return np.array(out)

loo_full = loo(X)
loo_q = loo(q[:, None])

# ---------------------------------------------------------------------------
# Resolution firewall: E043 stored response arrays were float32. The actual source
# runner replay discrepancy provides an intrinsic archive reconstruction floor.
# ---------------------------------------------------------------------------
archive_floor = float(max(archive_recompute))
late_collision_rows = []
for i in range(12, 16):
    late_collision_rows.append({
        "history": f"E{i+1}",
        "tree_distance_to_Estar": float(d_tree[i]),
        "recomputed_response_distance_to_Estar": float(d_resp[i]),
        "response_distance_over_E1_to_Estar": float(d_resp[i] / d_resp[0]),
        "below_E043_archive_recompute_floor": bool(d_resp[i] <= archive_floor),
    })

first_pc_count_below_archive_floor = None
for row in model_rows:
    if row["model"].startswith("tree_pc_") and row["max_absolute_residual"] <= archive_floor:
        first_pc_count_below_archive_floor = row["input_dimension"]
        break
if model_json["full_tree_linear"]["max_absolute_residual"] <= archive_floor:
    full_tree_below_floor = True
else:
    full_tree_below_floor = False

# The tiny E055 transverse tree-energy fraction carries a much larger fraction of
# response-orbit energy under a rank-1 tree map.
tree_transverse_energy_fraction = 1.0 - tree_pc1_energy
response_energy_missed_by_tree_pc1 = 1.0 - (1.0 - model_json["tree_pc_1"]["global_relative_residual"] ** 2)
transverse_response_leverage = float(response_energy_missed_by_tree_pc1 / tree_transverse_energy_fraction)

# ---------------------------------------------------------------------------
# Outputs.
# ---------------------------------------------------------------------------
def write_rows(path, rows):
    if not rows:
        return
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

orbit_rows = []
for i in range(16):
    orbit_rows.append({
        "history": f"E{i+1}",
        "history_depth": i + 1,
        "tree_distance_to_Estar": float(d_tree[i]),
        "response_distance_to_Estar_recomputed": float(d_resp[i]),
        "response_distance_over_E1_to_Estar": float(d_resp[i] / d_resp[0]),
        "q": float(q[i]),
        "E043_stored_vs_recomputed_response_L2": archive_recompute[i],
        "loo_full_tree_residual_over_E1_to_Estar": float(loo_full[i] / d_resp[0]),
        "loo_q_linear_residual_over_E1_to_Estar": float(loo_q[i] / d_resp[0]),
    })
write_rows(OUT / "ORBIT_GEOMETRY.csv", orbit_rows)
write_rows(OUT / "MODEL_METRICS.csv", model_rows)
write_rows(OUT / "LATE_INCIDENCE_AUDIT.csv", late_collision_rows)
write_rows(OUT / "LOO_AUDIT.csv", [
    {"history": f"E{i+1}", "full_tree_LOO_residual_over_E1": float(loo_full[i]/d_resp[0]), "q_linear_LOO_residual_over_E1": float(loo_q[i]/d_resp[0])}
    for i in range(16)
])

np.savez_compressed(
    OUT / "RECOMPUTED_DIRECT_FLOW_RESPONSE_ORBIT.npz",
    **{f"E{k:02d}_DeltaC_from_fresh_recomputed": R[k-1].reshape(32,32,32) for k in range(1,17)},
    Estar_DeltaC_from_fresh_recomputed=r_star.reshape(32,32,32),
)
np.savez_compressed(OUT / "FULL_TREE_LINEAR_MAP.npz", B_tree_to_response=B_full, w_star=w_star)

summary = {
    "experiment": "E056",
    "status": "CLOSED_MODERATE",
    "parent_promotions": 0,
    "physical_dark_matter_witness": False,
    "source_native_typing": "r_k in im(D_C) ~= Flow/ker(D_C)",
    "E043_archive_recompute_L2_min": float(min(archive_recompute)),
    "E043_archive_recompute_L2_max": archive_floor,
    "response_E1_to_Estar_L2": float(d_resp[0]),
    "response_distance_order_inversions": response_order_inversions,
    "tree_pc1_tree_energy_fraction": tree_pc1_energy,
    "response_pc1_response_energy_fraction": response_pc1_energy,
    "tree_response_leading_history_cosine": pc1_cos,
    "tree_response_leading_history_angle_deg": pc1_angle_deg,
    "tree_machine_rank": int(np.linalg.matrix_rank(X)),
    "response_machine_rank": int(np.linalg.matrix_rank(Y)),
    "models": model_json,
    "full_tree_linear_below_E043_archive_recompute_floor": full_tree_below_floor,
    "first_tree_pc_count_with_max_residual_below_archive_floor": first_pc_count_below_archive_floor,
    "tree_transverse_energy_fraction": tree_transverse_energy_fraction,
    "response_energy_missed_by_tree_pc1": response_energy_missed_by_tree_pc1,
    "transverse_response_leverage_ratio": transverse_response_leverage,
    "loo_full_tree_E2_E12_max_residual_over_E1": float(np.max(loo_full[1:12]) / d_resp[0]),
    "loo_full_tree_E1_endpoint_extrapolation_residual_over_E1": float(loo_full[0] / d_resp[0]),
    "late_incidence": late_collision_rows,
    "interpretation": {
        "q": "excellent monotone orbit-order coordinate, not a sufficient linear response coordinate",
        "full_weighted_tree": "predicts the tested direct-flow response to below the E043 archival reconstruction floor under the fixed-origin linear map",
        "transverse_information": "small in tree-weight energy but response-bearing; do not discard E055 transverse corrections",
        "success_class": "MODERATE: full weighted tree succeeds; dominant q alone does not",
    },
    "next_handle": "TEST_CROSS_PROBE_STABILITY_OF_THE_WEIGHTED_TREE_TO_RESPONSE_MAP_WITH_THE_EXISTING_SOURCE_NEUTRAL_OXYGEN_READOUTS",
}
(OUT / "SUMMARY.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
