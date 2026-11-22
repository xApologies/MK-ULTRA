# Reconstructed runner excerpt around T7/R7 relaxation

351:     record('T6', 'temporally meaningful interaction regime', 1)
352: 
353:     # T7 — closure equilibrium/writeout; environment begins relaxing.
354:     target_sum = float(np.sum(CH['occupancy_load_1e']))
355:     for s in states:
356:         cr = P1['regions']['T7']['environmental_effects']['closure_recompression']
357:         s['closure'] = (1-cr) * s['closure'] + cr * CH['closure_topology']
358:         s['C'] *= target_sum / max(float(np.sum(s['C'])), 1e-15)
359:     # Interpret dynamic_history_retention=0.10 as a 10% relaxation step,
360:     # consistent with the supplied runtime report's slow environmental decay.
361:     for k in ('chi', 'adj_memory', 'corridor_memory', 'persistent_memory'):
362:         env[k] *= 0.90
363:     record('T7', 'stable recursive identity / temporal history readable', 1)
364:     return states, env, ledger, snap
365: 
366: # ---------------------------------------------------------------------------
501:             {'cycle':cycle,'stage':'R6','metric':'survival_score','value':survival_score},
502:             {'cycle':cycle,'stage':'R6','metric':'pair_corridor_survives','value':float(final_edge)},
503:         ]
504:         for name, passed in gates.items():
505:             ledger.append({'cycle':cycle,'stage':'R6','metric':f'gate_{name}','value':float(passed)})
506: 
507:         # Only a corridor that actually survived can imprint persistent ecology.
508:         if final_edge:
509:             env['corridor_memory'] = 0.67*env['corridor_memory'] + 0.33*normalize01(candidate)
510:             env['persistent_memory'] = 0.67*env['persistent_memory'] + 0.33*normalize01(candidate)*recover
511:         else:
512:             env['corridor_memory'] *= 0.90
513:             env['persistent_memory'] *= 0.90
514: 
515:         # R7 — closure/persistence verification and slow environmental relaxation.
516:         for k in ('chi','adj_memory','corridor_memory','persistent_memory'):
517:             env[k] *= 0.90
518:         ledger += [
519:             {'cycle':cycle,'stage':'R7','metric':'environment_chirality_abs_mean','value':float(np.mean(np.abs(env['chi'])))},
520:             {'cycle':cycle,'stage':'R7','metric':'environment_corridor_memory_mean','value':float(np.mean(env['corridor_memory']))},
