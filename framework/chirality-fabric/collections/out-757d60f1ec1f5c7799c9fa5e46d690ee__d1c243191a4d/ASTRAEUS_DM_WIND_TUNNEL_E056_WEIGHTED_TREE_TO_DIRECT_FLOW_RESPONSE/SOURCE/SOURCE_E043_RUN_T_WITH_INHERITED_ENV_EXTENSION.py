# E043 transparent runner extension
# Original source:
# provenance://unavailable/path-sha256/0d7133249aa7a05dbfb9fdcd0b590d1094b0d1573b5987b3c6f830fb5f5ea241/MK43U_H2_concurrent_traversal_reconstructed.py
#
# The only semantic change to run_T is:
#   env = new_env()
# becomes:
#   env = new_env() if initial_env is None else copy(initial_env)
#
# Everything else is the original reconstructed T0->T7 function.
#
# This file records the exact patched function used in E043.

def run_T_with_env(n_manifolds: int = 2, pair_enabled: bool = True, snapshots: bool = True, initial_env=None):
    states = [new_h(f'H_{chr(65+i)}') for i in range(n_manifolds)]
    env = new_env() if initial_env is None else {k: v.copy() for k,v in initial_env.items()}
    ledger: List[Dict[str, object]] = []
    snap: Dict[str, Dict[str, np.ndarray]] = {}
    pair_src = CH['pair_closure_topology_H2'] if pair_enabled else np.zeros(SHAPE)
    pbase = geomean_fields(
        CH['core_persistence_protium'], CH['closure_topology'],
        CH['redistribution_resistance'], CH['environment_admissibility'])
    chi_norm = normalize01(np.abs(CHI))

    def env_source() -> np.ndarray:
        occ = sum(s['C'] for s in states)
        num = sum(s['chi'] * s['C'] for s in states)
        # The environment has its own baseline degree (=1), so manifold input
        # perturbs the environmental chirality field instead of replacing it.
        return num / (1.0 + occ)

    def shared_chi() -> np.ndarray:
        occ = sum(s['C'] for s in states)
        num = env['chi'] + sum(s['chi'] * s['C'] for s in states)
        return num / (1.0 + occ)

    def conductivity() -> np.ndarray:
        # Environment-admissibility gates local continuity movement; inherited
        # adjacency memory thickens conductivity by at most 10%.
        return np.clip(CH['environment_admissibility'] * (1.0 + 0.10 * env['adj_memory']), 0.0, 1.1)

    def record(stage: str, temporal_category: str, er_p: int):
        s = states[0]
        b = boundary_strength(s['P'])
        ledger.append({
            'stage': stage,
            'temporal_category': temporal_category,
            'er_p_index': int(er_p),
            'continuity_inventory_each': float(np.sum(s['C'])),
            'persistence_mean': float(np.mean(s['P'])),
            'closure_mean': float(np.mean(s['closure'])),
            'shell_mean': float(np.mean(s['shell'])),
            'environment_chirality_abs_mean': float(np.mean(np.abs(env['chi']))),
            'environment_chirality_max_abs': float(np.max(np.abs(env['chi']))),
            'shared_chirality_abs_mean': float(np.mean(np.abs(shared_chi()))),
            'environment_adjacency_memory_mean': float(np.mean(env['adj_memory'])),
            'environment_corridor_memory_mean': float(np.mean(env['corridor_memory'])),
            'environment_persistent_memory_mean': float(np.mean(env['persistent_memory'])),
            'timeshell_interface_strength_mean': float(np.mean(b)),
            'timeshell_interface_strength_max': float(np.max(b)),
        })
        if snapshots:
            snap[stage] = {
                'P': s['P'].copy(), 'C': s['C'].copy(), 'shell': s['shell'].copy(),
                'env_chi': env['chi'].copy(), 'env_adj_memory': env['adj_memory'].copy(),
                'env_corridor_memory': env['corridor_memory'].copy(),
                'env_persistent_memory': env['persistent_memory'].copy(),
                'timeshell_interface_strength': b.copy(), 'shared_chi': shared_chi().copy(),
            }

    # T0 — unresolved, time-independent chirality substrate.
    record('T0', 'time-independent', 0)

    # T1 — chirality admissibility amplification.
    g = P1['regions']['T1']['environmental_effects']['admissibility_amplification']
    env['chi'] = (1-g) * env['chi'] + g * env_source()
    for s in states:
        s['adj'] = clip01(s['adj'] + g * chi_norm * er_gain(0, 0) * (1-s['adj']))
    env['adj_memory'] = (1-g) * env['adj_memory'] + g * normalize01(np.abs(env['chi']))
    record('T1', 'time-independent', 0)

    # T2 — local adjacency routing by conservative N6 redistribution.
    g = P1['regions']['T2']['environmental_effects']['local_adjacency_weight']
    for s in states:
        s['C'] = conservative_redistribute(s['C'], g, conductivity() * s['adj'])
    env['chi'] = (1-g) * env['chi'] + g * env_source()
    grad = normalize01(boundary_strength(sum(s['C'] for s in states)))
    env['adj_memory'] = (1-g) * env['adj_memory'] + g * grad
    record('T2', 'time-independent', 0)

    # T3 — propagation reinforcement and pre-persistence corridor memory.
    g = P1['regions']['T3']['environmental_effects']['propagation_reinforcement']
    for s in states:
        s['C'] = conservative_redistribute(s['C'], g, conductivity() * s['adj'])
    env['chi'] = (1-g) * env['chi'] + g * env_source()
    if n_manifolds >= 2:
        proto = normalize01(geomean_fields(
            pair_src, CH['environment_admissibility'],
            geomean_fields(states[0]['shell'], states[1]['shell'])))
    else:
        proto = np.zeros(SHAPE)
    m = P1['regions']['T3']['environmental_effects']['corridor_memory']
    env['corridor_memory'] = (1-m) * env['corridor_memory'] + m * proto
    env['adj_memory'] = (1-g) * env['adj_memory'] + g * normalize01(grad + env['corridor_memory'])
    record('T3', 'time-independent', 0)

    # T4 — exact source dot signature: inherit -> stabilize -> close.
    pb = P1['regions']['T4']['environmental_effects']['persistence_bias_strength']
    kg = P1['regions']['T4']['environmental_effects']['knot_admissibility_gain']
    ca = P1['regions']['T4']['environmental_effects']['closure_asymmetry_strength']
    ptarget0 = clip01(pbase * (er_gain(2, 0) / np.mean(er_gain(2, 0))))
    for s in states:
        s['P'] = (1-pb) * s['P'] + pb * ptarget0
        s['P'] = (1-kg) * s['P'] + kg * ptarget0
        s['closure'] = (1-ca) * s['closure'] + ca * CH['closure_topology']
    e = P1['regions']['T4']['environmental_effects']['chirality_gradient_strength']
    env['chi'] = (1-e) * env['chi'] + e * env_source()
    env['adj_memory'] = (1-pb) * env['adj_memory'] + pb * normalize01(boundary_strength(sum(s['P'] for s in states)))
    record('T4', 'time-independent', 0)

    # T5 — NOT(time-independent): persistence closes enough for Time-Shell
    # boundary negotiation; use ER persistence/inheritance branch p=1.
    ptarget1 = clip01(pbase * (er_gain(2, 1) / np.mean(er_gain(2, 1))))
    for s in states:
        s['C'] = conservative_redistribute(
            s['C'], P1['regions']['T5']['environmental_effects']['occupancy_drift_strength'],
            conductivity() * CH['redistribution_resistance'])
        s['shell'] = conservative_redistribute(
            s['shell'], P1['regions']['T5']['environmental_effects']['shell_mobility_strength'],
            conductivity() * CH['environment_admissibility'])
        eq = P1['regions']['T5']['environmental_effects']['dynamic_equilibrium_gain']
        s['P'] = (1-eq) * s['P'] + eq * ptarget1
        s['closure'] = (1-eq) * s['closure'] + eq * CH['closure_topology']
    cg = P1['regions']['T5']['environmental_effects']['continuity_gradient_strength']
    env['chi'] = (1-cg) * env['chi'] + cg * env_source()
    bsum = normalize01(sum(boundary_strength(s['P']) for s in states))
    eq = P1['regions']['T5']['environmental_effects']['dynamic_equilibrium_gain']
    env['persistent_memory'] = (1-eq) * env['persistent_memory'] + eq * bsum * normalize01(np.abs(env['chi']))
    env['adj_memory'] = (1-cg) * env['adj_memory'] + cg * normalize01(env['corridor_memory'] + bsum)
    record('T5', 'NOT(time-independent); persistence/Time-Shell admissible', 1)

    # T6 — dynamic persistent interaction / coupling-preparation.
    for s in states:
        s['C'] = conservative_redistribute(
            s['C'], P1['regions']['T6']['environmental_effects']['continuity_current_strength'],
            conductivity() * CH['redistribution_resistance'])
        s['shell'] = conservative_redistribute(
            s['shell'], P1['regions']['T6']['environmental_effects']['shell_circulation_strength'],
            conductivity() * CH['environment_admissibility'])
        st = P1['regions']['T6']['environmental_effects']['dynamic_equilibrium_stabilizer']
        cf = P1['regions']['T6']['environmental_effects']['closure_feedback_strength']
        s['P'] = (1-st) * s['P'] + st * ptarget1
        s['closure'] = (1-cf) * s['closure'] + cf * CH['closure_topology']
    tg = P1['regions']['T6']['environmental_effects']['chirality_tension_strength']
    env['chi'] = (1-tg) * env['chi'] + tg * env_source()
    bsum = normalize01(sum(boundary_strength(s['P']) for s in states))
    if n_manifolds >= 2:
        coupling = normalize01(geomean_fields(pair_src, CH['environment_admissibility'], 0.1 + 0.9*bsum))
    else:
        coupling = np.zeros(SHAPE)
    ce = P1['regions']['T6']['environmental_effects']['coupling_interface_exposure']
    st = P1['regions']['T6']['environmental_effects']['dynamic_equilibrium_stabilizer']
    env['corridor_memory'] = (1-ce) * env['corridor_memory'] + ce * coupling
    env['persistent_memory'] = (1-st) * env['persistent_memory'] + st * coupling * normalize01(np.abs(env['chi']))
    env['adj_memory'] = (1-st) * env['adj_memory'] + st * normalize01(env['corridor_memory'] + bsum)
    record('T6', 'temporally meaningful interaction regime', 1)

    # T7 — closure equilibrium/writeout; environment begins relaxing.
    target_sum = float(np.sum(CH['occupancy_load_1e']))
    for s in states:
        cr = P1['regions']['T7']['environmental_effects']['closure_recompression']
        s['closure'] = (1-cr) * s['closure'] + cr * CH['closure_topology']
        s['C'] *= target_sum / max(float(np.sum(s['C'])), 1e-15)
    # Interpret dynamic_history_retention=0.10 as a 10% relaxation step,
    # consistent with the supplied runtime report's slow environmental decay.
    for k in ('chi', 'adj_memory', 'corridor_memory', 'persistent_memory'):
        env[k] *= 0.90
    record('T7', 'stable recursive identity / temporal history readable', 1)
    return states, env, ledger, snap

