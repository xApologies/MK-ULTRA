"""Exact algebra checks for the source-grounded chirality/energy/mass bridge.
These test identities and illustrative boundary cases, not native dynamics,
a Time-Shell implementation, physical calibration, or empirical predictions.
Run: python code/checks.py
"""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = []

def check(name, condition, scope):
    ok = bool(condition)
    RESULTS.append({'name': name, 'passed': ok, 'scope': scope})
    if not ok:
        raise AssertionError(name)

def zero(x):
    return sp.simplify(x) == 0

def main():
    p0,p1,p2,l0,l1,v = sp.symbols('p0 p1 p2 l0 l1 v', real=True)
    eps = sp.symbols('epsilon_P', positive=True)
    m0,m1 = l0-v,l1-v
    e=(p1-p0)/eps
    el=(l1-l0)/eps
    check('lock_filtered_mass_difference',zero(eps*el-(m1-m0)),
          'Common lock selector and fixed vacuum/unit; both endpoints mass-admissible.')
    check('lock_formation_equals_mass_number',zero((l1-v)/eps-m1/eps),
          'Conditional on an admissible vacuum-to-lock formation history.')
    check('history_composition',zero((p2-p0)/eps-((p1-p0)+(p2-p1))/eps),
          'Algebraic telescoping, not physical dynamics.')
    check('history_reverse_sign',zero((p0-p1)/eps+(p1-p0)/eps),
          'A reversed physical history is usable only if independently admissible.')
    check('closed_history_zero_net_change',zero((p0-p0)/eps),
          'Zero net change does not imply zero state inventory.')
    r0,r1=p0-l0,p1-l1
    check('full_change_lock_plus_remainder',zero(eps*e-(m1-m0)-(r1-r0)),
          'Remainder is bookkeeping; no nonnegativity or physical kinetic-energy claim.')
    check('full_history_energy_not_all_mass',
          sp.Rational(8-5,1)==3 and sp.Rational(2-2,1)==0,
          'Illustrative values: total persistence changes with fixed locked persistence.')
    k,y=sp.symbols('core_persistence total_shell_state_persistence',nonnegative=True)
    mass5=y-v; coremass=k-v; corr=mass5-coremass
    check('T4_to_T5_shell_correction',zero(eps*((y-k)/eps)-corr),
          'Requires Core5(Form5(K))~K and actual admissible K-to-Y history.')
    check('negative_shell_correction_allowed', (sp.Integer(3)-sp.Integer(5))==-2,
          'Illustrates the explicitly signed shell correction, not a physical solution.')
    old=sp.symbols('i b r o c'); new=sp.symbols('I B R O C')
    expanded=sum(sp.prod(new[:j])*(new[j]-old[j])*sp.prod(old[j+1:]) for j in range(5))
    check('five_factor_exact_difference',zero(sp.prod(new)-sp.prod(old)-expanded),
          'Exact finite product identity, order-dependent attribution; no differential approximation.')
    Eunit,munit,c=sp.symbols('Eunit munit c',positive=True)
    mu=sp.symbols('mu',nonnegative=True)
    rest_defect=Eunit*mu-c**2*munit*mu
    check('linear_rest_calibration',zero(rest_defect.subs(Eunit,c**2*munit)),
          'Checks a matching condition, does not derive its physical value.')
    check('monotone_mass_map_not_enough',sp.Integer(2)!=sp.Integer(2)**2,
          'Tm(M)=M^2 is zero-reflecting/strictly increasing on nonnegative inputs; Te(e)=e does not match c=1, eps=1.')
    # Independent 2x2 transport with zero net scalar energy: it is not an MK43 trajectory.
    A=sp.Matrix([[1,1],[0,1]]); B=sp.Matrix([[1,0],[1,1]])
    comm=A*B*A.inv()*B.inv()
    check('scalar_cycle_does_not_fix_transport',comm!=sp.eye(2),
          'Noncommuting transport can retain path information even when the endpoint scalar change is zero.')
    rho,p=sp.symbols('rho p',real=True)
    Ta=sp.diag(rho,0,0,0); Tb=sp.diag(rho,p,p,p)
    check('rest_density_does_not_determine_stress',Ta[0,0]==Tb[0,0] and Ta!=Tb,
          'Algebraic underdetermination: one scalar does not determine a symmetric tensor.')
    # Source v1.1 mode interface, kept separate from v3 history energy.
    mu_val=sp.Rational(1,2); cA=sp.Rational(1,2); lam=sp.Integer(1)
    espec=sp.sqrt(cA**2*lam+mu_val**2)
    check('mode_spectral_mass_shell_identity',zero(espec**2-cA**2*lam-mu_val**2),
          'Spectral interface identity only; no identification with history energy or a physical clock.')
    (ROOT/'results').mkdir(exist_ok=True)
    report={'passed':all(r['passed'] for r in RESULTS),'check_count':len(RESULTS),
            'sympy_version':sp.__version__,
            'scope':'Exact algebra and explicitly labeled examples only; no empirical or full native-interface validation.',
            'checks':RESULTS}
    (ROOT/'results'/'CHECK_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'passed':report['passed'],'check_count':len(RESULTS)}))

if __name__=='__main__':
    main()
