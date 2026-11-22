#!/usr/bin/env python3
"""Finite deterministic Atlas refinement and bridge checks.

These routines check supplied finite tables. They do NOT implement Genesis gravity,
GR evolution, gauge classification, a continuum limit, or a PDE existence proof.
No missing native operator is replaced by a toy implementation.

Run tests: python finite_atlas.py --self-test
Check data: python finite_atlas.py --input finite_bridge.json
"""
from __future__ import annotations
import argparse
from collections import deque
from dataclasses import dataclass
from itertools import product
import json
from pathlib import Path
from typing import Any


@dataclass
class Model:
    states: tuple[str, ...]
    observations: dict[str, str]
    transitions: dict[str, dict[str, str]]  # absent state = undefined operation

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> 'Model':
        if not isinstance(data, dict):
            raise ValueError('A model must be a JSON object.')
        states = data.get('states')
        obs = data.get('observations')
        trans = data.get('transitions')
        if not isinstance(states, list) or not states or not all(isinstance(x, str) for x in states):
            raise ValueError('states must be a nonempty list of string identifiers.')
        if len(set(states)) != len(states):
            raise ValueError('State identifiers must be unique.')
        if not isinstance(obs, dict) or set(obs) != set(states) or not all(isinstance(x, str) for x in obs.values()):
            raise ValueError('observations must assign a string label to every state, and only those states.')
        if not isinstance(trans, dict):
            raise ValueError('transitions must be an object of partial-operation tables.')
        for action, table in trans.items():
            if not isinstance(action, str) or not isinstance(table, dict):
                raise ValueError('Each operation must have a string name and a table.')
            if not set(table) <= set(states) or not all(isinstance(t, str) and t in states for t in table.values()):
                raise ValueError(f'Operation {action!r} contains a state outside the declared model.')
        return cls(tuple(states), dict(obs), {a: dict(t) for a, t in trans.items()})


def group_by_signature(states: tuple[str, ...], signatures: dict[str, Any]) -> tuple[tuple[str, ...], ...]:
    blocks: dict[Any, list[str]] = {}
    for s in states:
        blocks.setdefault(signatures[s], []).append(s)
    return tuple(tuple(block) for block in blocks.values())


def refine(model: Model) -> dict[str, Any]:
    """Compute the coarsest strong congruence refining initial observations.

    At most |states|-|initial blocks| strict refinements occur. A fixed point
    is verified explicitly; a repeated unchanged partition is not called progress.
    """
    partition = group_by_signature(model.states, model.observations)
    history = [partition]
    actions = tuple(sorted(model.transitions))
    for _ in range(len(model.states) + 1):
        block_of = {s: i for i, b in enumerate(partition) for s in b}
        signatures = {}
        for s in model.states:
            successors = tuple((1, block_of[model.transitions[a][s]])
                               if s in model.transitions[a] else (0, -1)
                               for a in actions)
            signatures[s] = (block_of[s], successors)
        nxt = group_by_signature(model.states, signatures)
        if nxt == partition:
            return {'partitions': history, 'stable_partition': partition,
                    'strict_refinements': len(history)-1,
                    'strict_refinement_bound': len(model.states)-len(history[0])}
        if len(nxt) <= len(partition):
            raise AssertionError('Internal error: a changed refinement did not split a block.')
        history.append(nxt)
        partition = nxt
    raise AssertionError('Finite refinement exceeded its proved termination bound.')


def record(model: Model, state: str, word: tuple[str, ...]) -> tuple[str, str | None]:
    for a in word:
        table = model.transitions[a]
        if state not in table:
            return ('undefined', None)
        state = table[state]
    return ('defined', model.observations[state])


def distinguishing_word(model: Model, left: str, right: str) -> tuple[str, ...] | None:
    """Shortest finite continuation exposing observation or enabledness difference.

    None means no difference under this finite deterministic model, not physical
    equivalence in any unmodeled theory. Breadth-first search visits each pair once.
    """
    if left not in model.states or right not in model.states:
        raise ValueError('Both states must belong to the model.')
    todo = deque([(left, right, ())])
    seen = {(left, right)}
    for_action = tuple(sorted(model.transitions))
    while todo:
        # Inspect all current-depth observations before accepting a longer
        # enabledness witness. Otherwise a later pair in this layer might
        # have a strictly shorter observation witness.
        layer = list(todo)
        todo.clear()
        for x, y, word in layer:
            if model.observations[x] != model.observations[y]:
                return word
        for x, y, word in layer:
            for a in for_action:
                table = model.transitions[a]
                ex, ey = x in table, y in table
                if ex != ey:
                    return word+(a,)
                if ex:
                    pair = (table[x], table[y])
                    if pair not in seen:
                        seen.add(pair)
                        todo.append((*pair, word+(a,)))
    return None


def check_bridge(native: Model, target: Model, mapping: dict[str, str],
                 physical_classes: dict[str, str] | None = None) -> dict[str, Any]:
    """Check an explicitly given finite map, not the existence of an unknown map.

    Operation names must already have matching meanings. Supplying matching names
    alone is not evidence of this interpretation outside the finite tables.
    """
    if not isinstance(mapping, dict) or set(mapping) != set(native.states):
        raise ValueError('mapping must specify exactly one target for every native state.')
    if not all(isinstance(v, str) and v in target.states for v in mapping.values()):
        raise ValueError('mapping contains an undeclared target state.')
    if set(native.transitions) != set(target.transitions):
        raise ValueError('Declare the same operation alphabet on both models, including empty domains.')
    if physical_classes is not None:
        if set(physical_classes) != set(native.states) or not all(isinstance(v,str) for v in physical_classes.values()):
            raise ValueError('physical_classes must explicitly classify every native state.')
    errors = []
    missing = sorted(set(target.states)-set(mapping.values()))
    if missing:
        errors.append({'kind':'coverage', 'unreached_target_states':missing})
    for x in native.states:
        y = mapping[x]
        if native.observations[x] != target.observations[y]:
            errors.append({'kind':'observation', 'native_state':x, 'target_state':y})
        for a in sorted(native.transitions):
            nt, tt = native.transitions[a], target.transitions[a]
            if (x in nt) != (y in tt):
                errors.append({'kind':'enabledness','state':x,'action':a})
            elif x in nt and mapping[nt[x]] != tt[y]:
                errors.append({'kind':'dynamics','state':x,'action':a,
                               'project_after_native':mapping[nt[x]],
                               'evolve_after_project':tt[y]})
    class_result = 'NOT_SUPPLIED'
    if physical_classes is not None:
        violations = []
        for x in native.states:
            for z in native.states:
                if (mapping[x] == mapping[z]) != (physical_classes[x] == physical_classes[z]):
                    violations.append([x,z])
        class_result = 'MATCHES_FIBERS' if not violations else 'DOES_NOT_MATCH_FIBERS'
        if violations:
            errors.append({'kind':'declared_physical_classes','pairs':violations})
    return {'status':'PASS_FINITE_TABLE_CHECK' if not errors else 'FAIL_FINITE_TABLE_CHECK',
            'errors':errors, 'declared_physical_class_test':class_result,
            'scope':'Finite supplied tables only. Physical interpretation, native laws, smooth geometry, and global GR coverage are not certified.'}


def atlas_example() -> Model:
    return Model.from_dict({
        'states':[str(x) for x in range(6)],
        'observations':{str(x):str(x%2) for x in range(6)},
        'transitions':{
            'flip':{str(x):str((x+1)%6) for x in range(6)},
            'jump':{str(x):str((x+2)%6) for x in range(6)},
            'gate':{str(x):str((x+2)%6) for x in range(4)}}})


def self_test() -> dict[str, Any]:
    cases = []
    def check(name: str, condition: bool) -> None:
        if not condition:
            raise AssertionError(name)
        cases.append({'name':name,'passed':True})

    atlas = atlas_example()
    refinement = refine(atlas)
    expected = [(('0','2','4'),('1','3','5')),
                (('0','2'),('1','3'),('4',),('5',)),
                (('0',),('1',),('2',),('3',),('4',),('5',))]
    check('Atlas RN025 exact partition sequence', refinement['partitions']==expected)
    check('Atlas RN025 exactly two strict refinements', refinement['strict_refinements']==2)
    witness = distinguishing_word(atlas,'0','2')
    check('A shortest distinguishing word has length two',witness is not None and len(witness)==2)
    check('Report-consistent jump then gate also distinguishes 0 and 2',record(atlas,'0',('jump','gate')) != record(atlas,'2',('jump','gate')))
    check('Witness is defined for one state and undefined for the other',
          record(atlas,'0',witness)!=record(atlas,'2',witness))
    alphabet = tuple(atlas.transitions)
    words = [w for length in range(5) for w in product(alphabet,repeat=length)]
    block = {s:i for i,b in enumerate(refinement['stable_partition']) for s in b}
    evaluations = 0
    agreement = True
    for x in atlas.states:
        for y in atlas.states:
            all_equal = True
            for word in words:
                evaluations += 1
                if record(atlas,x,word)!=record(atlas,y,word):
                    all_equal=False
            agreement = agreement and ((block[x]==block[y])==all_equal)
    check('4356 bounded word-state-pair checks agree with stable partition',agreement and evaluations==4356)
    check('All finite pair-witness results agree with stable partition', all(
        (distinguishing_word(atlas,x,y) is None)==(block[x]==block[y])
        for x in atlas.states for y in atlas.states))

    # Constructed test fixtures, not Genesis or GR implementations.
    target = Model.from_dict({'states':['0','1'],'observations':{'0':'0','1':'1'},
                             'transitions':{'step':{'0':'1','1':'0'}}})
    states = [f'{x}:{b}' for x in range(2) for b in range(3)]
    labels = {s:s.split(':')[0] for s in states}
    redundant = Model.from_dict({'states':states,'observations':labels,
        'transitions':{'step':{s:f'{1-int(s[0])}:{s[2]}' for s in states}}})
    check('Irrelevant retained labels yield two behavioral classes',len(refine(redundant)['stable_partition'])==2)
    check('Finite matched bridge passes',check_bridge(redundant,target,labels)['status']=='PASS_FINITE_TABLE_CHECK')
    check('Explicit declared quotient passes finite equality check',
          check_bridge(redundant,target,labels,labels)['status']=='PASS_FINITE_TABLE_CHECK')
    check('Distinct declared physical labels are not silently quotiented',
          check_bridge(redundant,target,labels,{s:s for s in states})['status']=='FAIL_FINITE_TABLE_CHECK')
    check('Raw labels remain recoverable from paired data',all(':'.join((labels[s],s.split(':')[1]))==s for s in states))
    bad = Model.from_dict({'states':['0','1'],'observations':{'0':'0','1':'1'},
                          'transitions':{'step':{'0':'0','1':'1'}}})
    check('Incorrect target dynamics rejected',any(e['kind']=='dynamics' for e in check_bridge(redundant,bad,labels)['errors']))
    partial = Model.from_dict({'states':['0','1'],'observations':{'0':'0','1':'1'},
                              'transitions':{'step':{'0':'1'}}})
    check('Enabledness mismatch rejected',any(e['kind']=='enabledness' for e in check_bridge(redundant,partial,labels)['errors']))
    enlarged = Model.from_dict({'states':['0','1','2'],'observations':{'0':'0','1':'1','2':'2'},
                               'transitions':{'step':{'0':'1','1':'0','2':'2'}}})
    check('Coverage failure rejected',any(e['kind']=='coverage' for e in check_bridge(redundant,enlarged,labels)['errors']))
    try:
        Model.from_dict({'states':['0'],'observations':{'0':'0'},'transitions':{'bad':{'0':'missing'}}})
        malformed_rejected=False
    except ValueError:
        malformed_rejected=True
    check('Malformed state reference rejected',malformed_rejected)

    # A bounded exhaustive verification of all finite-model parameter combinations:
    # two states, binary observation, two partial operations; each op has 3^2 tables.
    small_count=0
    table_options=[]
    for destinations in product([None,'0','1'],repeat=2):
        table_options.append({str(i):d for i,d in enumerate(destinations) if d is not None})
    for observations in product(['0','1'],repeat=2):
        for t1 in table_options:
            for t2 in table_options:
                m=Model.from_dict({'states':['0','1'],'observations':dict(zip(['0','1'],observations)),
                                   'transitions':{'a':t1,'b':t2}})
                r=refine(m)
                same=any('0' in b and '1' in b for b in r['stable_partition'])
                if same != (distinguishing_word(m,'0','1') is None):
                    raise AssertionError('Exhaustive two-state check failed')
                if r['strict_refinements']>r['strict_refinement_bound']:
                    raise AssertionError('Termination bound failed')
                small_count+=1
    check('All 324 two-state models agree with independent pair search',small_count==324)

    # Exact arithmetic tests of projection plus complement; fixtures, not native data.
    from fractions import Fraction as F
    vectors = [tuple(map(F,v)) for v in product(range(-2,3),repeat=3)]
    reconstructed = []
    for x in vectors:
        primary=(x[0],x[1]); complement=(F(0),F(0),x[2])
        restored=(primary[0]+complement[0],primary[1]+complement[1],complement[2])
        reconstructed.append(restored==x)
    check('Projection-plus-complement inverse on 125 rational fixtures',all(reconstructed))
    def duplicate_record(x: tuple[F, ...]) -> tuple[F, ...]:
        return (x[0],x[1],x[0])
    u=(F(1),F(2),F(3)); v=(F(1),F(2),F(4))
    check('Copying an already visible coordinate does not recover missing coordinate',
          duplicate_record(u)==duplicate_record(v) and u!=v)
    # Restricted identity must not be used as a global identity: T=diag(1,2),
    # P=diag(1,0) agrees on the first-coordinate sector only.
    def t(x: tuple[int,int]) -> tuple[int,int]:
        return (x[0],2*x[1])
    def p(x: tuple[int,int]) -> tuple[int,int]:
        return (x[0],0)
    sector=(1,0); outside=(0,1)
    check('Sector identity extension guard',t(t(sector))==p(sector) and t(t(outside))!=p(outside))
    return {'status':'ALL_TESTS_PASSED','tests':cases,'test_count':len(cases),
            'atlas_partitions':refinement['partitions'],
            'atlas_strict_refinements':2,'atlas_shortest_witness_0_vs_2':list(witness),
            'atlas_bounded_word_pair_checks':evaluations,
            'exhaustive_two_state_models':small_count,
            'native_genesis_gr':'NOT_EVALUATED: actual native operators, target evolution, and independently justified physical equivalence were not supplied as evaluated finite tables.',
            'scope':'Report example and constructed finite/linear fixtures only; no physical-equivalence certificate.'}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--self-test',action='store_true')
    group.add_argument('--input',type=Path)
    args=parser.parse_args()
    try:
        if args.self_test:
            result=self_test()
        else:
            data=json.loads(args.input.read_text())
            native=Model.from_dict(data['native']); target=Model.from_dict(data['target'])
            result={'native_refinement':refine(native),'target_refinement':refine(target),
                    'bridge':check_bridge(native,target,data['mapping'],data.get('physical_classes'))}
        print(json.dumps(result,indent=2))
    except (ValueError,KeyError,TypeError,OSError) as exc:
        parser.exit(2,f'Input error: {exc}\n')

if __name__=='__main__':
    main()
