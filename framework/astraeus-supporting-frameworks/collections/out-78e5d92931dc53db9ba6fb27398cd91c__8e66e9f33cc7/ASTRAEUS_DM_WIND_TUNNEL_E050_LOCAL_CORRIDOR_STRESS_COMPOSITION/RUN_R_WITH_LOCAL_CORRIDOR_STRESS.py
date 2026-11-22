def run_R_with_corridor_stress(states, env, cycles: int = 3, pair_enabled: bool = True, snapshots: bool = True, stress_mask=None, stress_amplitude: float = 0.0, stress_cycle: int = 1):
    states = [{k: (v.copy() if isinstance(v, np.ndarray) else v) for k,v in s.items()} for s in states]
    env = {k: v.copy() for k,v in env.items()}
    pair_src = CH['pair_closure_topology_H2'] if pair_enabled else np.zeros(SHAPE)
    init_sum = float(np.sum(CH['occupancy_load_1e']))
    ledger: List[Dict[str, object]] = []
    snap = {}
    final_edge = False

    for cycle in range(1, cycles+1):
        A, B = states[0], states[1]
        # R0 identity registration.
        ledger += [
            {'cycle': cycle, 'stage':'R0', 'metric':'identity_lock_A', 'value':1.0},
            {'cycle': cycle, 'stage':'R0', 'metric':'identity_lock_B', 'value':1.0},
        ]

        # R1 interaction-surface mapping. No interaction is forced.
        bA = normalize01(boundary_strength(A['P'])); bB = normalize01(boundary_strength(B['P']))
        shell_overlap = geomean_fields(A['shell'], B['shell'])
        boundary_context = normalize01(bA + bB)
        surface = normalize01(geomean_fields(
            np.clip(shell_overlap, 1e-12, 1),
            np.clip(CH['environment_admissibility'], 1e-12, 1),
            np.clip(0.05 + 0.95*boundary_context, 1e-12, 1)))
        align_field = 1.0 - np.abs(A['chi']-B['chi'])/(2*np.max(np.abs(CHI))+1e-12)
        alignment = float(np.mean(align_field))
        ledger += [
            {'cycle':cycle,'stage':'R1','metric':'surface_map_mean','value':float(np.mean(surface))},
            {'cycle':cycle,'stage':'R1','metric':'chirality_alignment_mean','value':alignment},
        ]

        # R2 controlled continuity exchange. For identical H states this can
        # have nonzero gross bidirectional shell sharing with zero net transfer.
        kx = P1['regions']['T6']['environmental_effects']['coupling_interface_exposure']
        F_AB = kx * surface * A['C']
        F_BA = kx * surface * B['C']
        A['C'] = A['C'] - F_AB + F_BA
        B['C'] = B['C'] - F_BA + F_AB
        gross_ab = float(np.sum(F_AB)/init_sum)
        gross_ba = float(np.sum(F_BA)/init_sum)
        ledger += [
            {'cycle':cycle,'stage':'R2','metric':'gross_exchange_A_to_B_fraction','value':gross_ab},
            {'cycle':cycle,'stage':'R2','metric':'gross_exchange_B_to_A_fraction','value':gross_ba},
            {'cycle':cycle,'stage':'R2','metric':'net_inventory_change_A_fraction','value':float((np.sum(A['C'])-init_sum)/init_sum)},
            {'cycle':cycle,'stage':'R2','metric':'net_inventory_change_B_fraction','value':float((np.sum(B['C'])-init_sum)/init_sum)},
            {'cycle':cycle,'stage':'R2','metric':'closure_integrity_A_corr','value':corr(A['closure'],CH['closure_topology'])},
            {'cycle':cycle,'stage':'R2','metric':'closure_integrity_B_corr','value':corr(B['closure'],CH['closure_topology'])},
        ]
        exchange_map = normalize01(F_AB + F_BA)
        env['chi'] = 0.90*env['chi'] + 0.10*((A['chi']+B['chi'])/2.0)*exchange_map
        env['adj_memory'] = 0.90*env['adj_memory'] + 0.10*exchange_map

        # R3 persistent coupling memory.
        m = P1['regions']['T3']['environmental_effects']['corridor_memory']
        env['corridor_memory'] = (1-m)*env['corridor_memory'] + m*surface
        coupling_memory = float(np.mean(env['corridor_memory']))
        ledger.append({'cycle':cycle,'stage':'R3','metric':'persistent_coupling_memory_mean','value':coupling_memory})

        # R4 — forms possibility. H-specific pair closure lives only in the
        # manifold; the environment only supplies common surface/context.
        env_context = clip01(0.5*CH['environment_admissibility'] +
                             0.5*normalize01(env['adj_memory']+env['corridor_memory']))
        candidate = pair_src * surface * env_context
        # E050 controlled Pipeline-2 Corridor Stress:
        # one bounded, localized suppression of the already-emitted R4 candidate.
        # It creates no new domain, writes no chirality, and leaves ancestry untouched.
        if stress_mask is not None and cycle == int(stress_cycle):
            candidate = np.clip(candidate * (1.0 - float(stress_amplitude) * stress_mask), 0.0, 1.0)
        if not pair_enabled:
            candidate[:] = 0.0
        w = candidate
        wsum = float(np.sum(w))
        if wsum > 1e-15:
            candidate_strength = weighted_mean(candidate, w)
            strain_map = candidate * (1.0-CH['redistribution_resistance'])
            overload_map = np.maximum(candidate-CH['open_shell_vacancy_1s1'], 0.0)
            recoverability_map = geomean_fields(
                CH['closure_topology'], CH['redistribution_resistance'], CH['environment_admissibility'])
            strain = weighted_mean(strain_map, w)
            overload = weighted_mean(overload_map, w)
            recover = weighted_mean(recoverability_map, w)
            chiover = weighted_mean(1.0-align_field, w)
        else:
            candidate_strength = strain = overload = recover = chiover = 0.0
            recoverability_map = np.zeros(SHAPE)
        ledger += [
            {'cycle':cycle,'stage':'R4','metric':'corridor_candidate_mean','value':float(np.mean(candidate))},
            {'cycle':cycle,'stage':'R4','metric':'corridor_candidate_weighted_strength','value':candidate_strength},
            {'cycle':cycle,'stage':'R4','metric':'elastic_strain_weighted','value':strain},
            {'cycle':cycle,'stage':'R4','metric':'bandwidth_overload_weighted','value':overload},
            {'cycle':cycle,'stage':'R4','metric':'recoverability_weighted','value':recover},
            {'cycle':cycle,'stage':'R4','metric':'chirality_overconstraint_weighted','value':chiover},
        ]

        # R5 — ordered topology resolution. For two distinct identity nodes the
        # graph alternatives are {} and {AB}. The reconstruction does not ask
        # which molecule should form. It asks whether the R4 edge is recoverable.
        burden = strain + overload + chiover
        margin = recover - burden
        pair_recoverable = bool(wsum > 1e-15 and margin > 0.0)
        selected_pair = pair_recoverable
        ledger += [
            {'cycle':cycle,'stage':'R5','metric':'recoverability_margin','value':margin},
            {'cycle':cycle,'stage':'R5','metric':'pair_recoverable','value':float(pair_recoverable)},
            {'cycle':cycle,'stage':'R5','metric':'selected_pair_corridor','value':float(selected_pair)},
        ]

        # R6 — every source-stated survivability condition must pass.
        if selected_pair:
            damp = P1['regions']['T6']['environmental_effects']['dynamic_equilibrium_stabilizer']
            strain_after = strain * (1.0-damp*recover)
            gates = {
                'ancestry': True,
                'strain_bounded': strain < recover,
                'chirality_capacity': chiover < recover,
                'bandwidth_capacity': overload < recover,
                'damping_reduces_instability': strain_after <= strain + 1e-15,
                'coherent_recoverability': recover > 0.0,
            }
            survives = all(gates.values())
            survival_score = float(np.mean([
                1.0,
                np.clip(1-strain/max(recover,1e-12),0,1),
                np.clip(1-chiover/max(recover,1e-12),0,1),
                np.clip(1-overload/max(recover,1e-12),0,1),
                np.clip((strain-strain_after)/max(strain,1e-12),0,1) if strain>0 else 1.0,
                recover]))
        else:
            strain_after = 0.0; survives = False; survival_score = 0.0
            gates = {k:False for k in (
                'ancestry','strain_bounded','chirality_capacity','bandwidth_capacity',
                'damping_reduces_instability','coherent_recoverability')}
        final_edge = bool(selected_pair and survives)
        ledger += [
            {'cycle':cycle,'stage':'R6','metric':'damped_strain','value':strain_after},
            {'cycle':cycle,'stage':'R6','metric':'survival_score','value':survival_score},
            {'cycle':cycle,'stage':'R6','metric':'pair_corridor_survives','value':float(final_edge)},
        ]
        for name, passed in gates.items():
            ledger.append({'cycle':cycle,'stage':'R6','metric':f'gate_{name}','value':float(passed)})

        # Only a corridor that actually survived can imprint persistent ecology.
        if final_edge:
            env['corridor_memory'] = 0.67*env['corridor_memory'] + 0.33*normalize01(candidate)
            env['persistent_memory'] = 0.67*env['persistent_memory'] + 0.33*normalize01(candidate)*recover
        else:
            env['corridor_memory'] *= 0.90
            env['persistent_memory'] *= 0.90

        # R7 — closure/persistence verification and slow environmental relaxation.
        for k in ('chi','adj_memory','corridor_memory','persistent_memory'):
            env[k] *= 0.90
        ledger += [
            {'cycle':cycle,'stage':'R7','metric':'environment_chirality_abs_mean','value':float(np.mean(np.abs(env['chi'])))},
            {'cycle':cycle,'stage':'R7','metric':'environment_corridor_memory_mean','value':float(np.mean(env['corridor_memory']))},
            {'cycle':cycle,'stage':'R7','metric':'environment_persistent_memory_mean','value':float(np.mean(env['persistent_memory']))},
            {'cycle':cycle,'stage':'R7','metric':'ancestry_identity_A_preserved','value':1.0},
            {'cycle':cycle,'stage':'R7','metric':'ancestry_identity_B_preserved','value':1.0},
            {'cycle':cycle,'stage':'R7','metric':'chirality_rewrite_max_abs','value':0.0},
            {'cycle':cycle,'stage':'R7','metric':'stable_pair_edge','value':float(final_edge)},
        ]
        if snapshots:
            snap[str(cycle)] = {
                'surface':surface.copy(), 'candidate':candidate.copy(),
                'env_chi':env['chi'].copy(), 'env_corridor':env['corridor_memory'].copy(),
                'env_persistent':env['persistent_memory'].copy(),
            }
    return states, env, ledger, final_edge, snap
