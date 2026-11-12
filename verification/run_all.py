"""Recompute the finite scientific diagnostics and compare the committed record.

Run `python verification/run_all.py --write` only when intentionally refreshing
the deterministic reference output after reviewing a scientific change.
"""
from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm, null_space
from scipy.optimize import minimize_scalar

from weighted_capacity import amplitude_damping, entropy, h2, instance, lowering
from pair_lindblad import ds, run


ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def relative_entropy_diagonal(rho, probabilities):
    return -entropy(rho) - float(np.dot(np.diag(rho).real, np.log2(probabilities)))


def thermal_probabilities(n, p):
    return np.array([p**k.bit_count() * (1-p)**(n-k.bit_count()) for k in range(1 << n)])


def entropy_identity(n, eta, p, seed):
    """Check the identity independently on a general, ungraded mixed input."""
    rng = np.random.default_rng(seed)
    a = rng.normal(size=(1 << n, 1 << n)) + 1j*rng.normal(size=(1 << n, 1 << n))
    rho = a @ a.conj().T
    rho /= np.trace(rho)
    out = amplitude_damping(rho, n, eta)
    env = amplitude_damping(rho, n, 1-eta)
    db = relative_entropy_diagonal(out, thermal_probabilities(n, eta*p))
    de = relative_entropy_diagonal(env, thermal_probabilities(n, (1-eta)*p))
    derivative = eta*np.log2((1-eta*p)/(eta*p)) - (1-eta)*np.log2((1-(1-eta)*p)/((1-eta)*p))
    mean_n = float(sum(k.bit_count()*rho[k, k].real for k in range(1 << n)))
    rhs = n*(h2(eta*p)-h2((1-eta)*p)) + derivative*(mean_n-n*p) - db + de
    residual = abs(entropy(out)-entropy(env)-rhs)
    require(residual < 2e-11, 'coherent-information identity')
    return dict(B=n, eta=eta, reference_population=p, residual=residual)


def single_excitation_erasure(n, r, eta, seed):
    """Compare the entire restricted channel with direct Lindblad evolution."""
    rng = np.random.default_rng(seed)
    g = rng.normal(size=(r, n)) + 1j*rng.normal(size=(r, n))
    k = null_space(g)
    d = k.shape[1]
    v = np.zeros((1 << n, d), complex)
    for j in range(n):
        v[1 << j, :] = k[j, :]
    singles = [lowering(n, j) for j in range(n)]
    ls = [sum(c*s for c, s in zip(row, singles)) for row in g]
    generator = sum(ds(l) for l in ls) - np.log(eta)*sum(ds(s) for s in singles)
    # A collective Lamb term is nonzero outside the code but vanishes on it.
    ham = .37 * sum(l.conj().T @ l for l in ls)
    physical_d = 1 << n
    generator += -1j*(np.kron(np.eye(physical_d), ham)-np.kron(ham.T, np.eye(physical_d)))
    channel = expm(generator)
    vacuum = np.zeros((physical_d, physical_d), complex)
    vacuum[0, 0] = 1
    residuals = []
    for a in range(d):
        for b in range(d):
            unit = np.zeros((d, d), complex)
            unit[a, b] = 1
            encoded = v @ unit @ v.conj().T
            actual = (channel @ encoded.reshape(-1, order='F')).reshape((physical_d, physical_d), order='F')
            expected = eta*encoded + (1-eta)*np.trace(unit)*vacuum
            residuals.append(float(np.linalg.norm(actual-expected)))
    residual = max(residuals)
    require(residual < 1e-10, 'single-excitation erasure identity')
    return dict(B=n, r=r, logical_dimension=d, eta=eta, channel_basis_checks=d*d, max_residual=residual)


def calibration_geometry(delta, samples, seed):
    """Test complex disk errors and the extremal point of b<=delta^2."""
    rng = np.random.default_rng(seed)
    e = delta*np.sqrt(rng.random((samples, 2)))*np.exp(2j*np.pi*rng.random((samples, 2)))
    g = 1+e
    b = abs(g[:, 0]-g[:, 1])**2/(2*np.sum(abs(g)**2, axis=1))
    extremal = np.array([1-delta*delta+1j*delta*np.sqrt(1-delta*delta),
                         1-delta*delta-1j*delta*np.sqrt(1-delta*delta)])
    b_extreme = abs(extremal[0]-extremal[1])**2/(2*np.sum(abs(extremal)**2))
    require(float(max(b)) <= delta*delta+1e-12, 'calibration angle bound')
    require(abs(b_extreme-delta*delta) < 1e-12, 'calibration extremizer')
    return dict(delta=delta, random_samples=samples, max_random_b=float(max(b)), extremal_b=float(b_extreme))


def divergence_nats(p, q):
    return float(p*np.log(p/q)+(1-p)*np.log((1-p)/(1-q)))


def all_checks():
    weighted = []
    for n, r in [(2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 3)]:
        for eta in [.6, .8, .95]:
            v = instance(n, r, eta, 1000+10*n+r)
            require(v['partition']+1e-8 >= v['partition_lower'], 'weighted partition bound')
            require(v['ci_margin'] >= -1e-8, 'capacity lower bound')
            require(v['collective_residual'] < 1e-7, 'dark invariance')
            weighted.append(v)
    pair = [run(np.deg2rad(angle), .9, gamma, 0., shift)
            for gamma in [.1, 1, 10, 1000] for angle in [0, 10, 20] for shift in [0, np.pi]]
    for v in pair:
        require(abs(v['bb84_error']-v['nominal_formula']) < 1e-10, 'pair Lindblad formula')
    dephasing = [run(np.deg2rad(10), .9, gamma, .01) for gamma in [.1, 1, 10, 1000]]
    for v in dephasing:
        require(abs(v['bb84_error']-v['nominal_formula']) <= .02+1e-10, 'dephasing task-error budget')
    identity = [entropy_identity(3, eta, p, 1234) for eta in [.6, .8, .95] for p in [.2, .4]]
    erasure = [single_excitation_erasure(n, r, eta, 100+n+r)
               for n, r in [(3, 1), (4, 2)] for eta in [.6, .9]]
    geometry = [calibration_geometry(delta, 10000, 214) for delta in [.1, .3, .6]]
    eta, delta, alpha = .9, .1, .1
    amplitude = np.sqrt(eta)*(1-2*delta**2)
    bare = (2-amplitude**2-amplitude)/4
    task_error = bare+.02+.01
    qclassical = (1-1/np.sqrt(2))/2
    require(task_error < alpha < qclassical, 'finite quantum/classical separation')
    p = minimize_scalar(lambda x: -(h2(.8*x)-h2(.2*x)), bounds=(1e-8, .5), method='bounded').x
    q = h2(.8*p)-h2(.2*p)
    c = -np.log2(1-p/(1-p))
    rate = q-c/32-.02-1.01*h2(.01/1.01)/32
    return dict(
        scope='Finite diagnostics only; universal and asymptotic statements require the written proofs and cited coding theorems.',
        weighted_profiles=weighted, entropy_identity=identity,
        pair_lindblad=pair, added_dephasing=dephasing,
        single_excitation_erasure=erasure, calibration_geometry=geometry,
        working_point=dict(eta=eta, relative_coupling_error=delta, bare_error_upper=float(bare),
                           storage_dephasing_error_budget=.02, endpoint_error_budget=.01,
                           total_error_upper=float(task_error), acceptance_fraction=alpha,
                           classical_error_threshold=float(qclassical),
                           quantum_failure_exponent_nats=divergence_nats(alpha, task_error),
                           classical_acceptance_exponent_nats=divergence_nats(alpha, qclassical)),
        capacity_example=dict(B=32, r=1, eta=.8, epsilon=.01, q_ad=float(q), c_eta=float(c), rate_lower=float(rate)))


def compare(actual, expected, where='results'):
    if isinstance(expected, dict):
        require(set(actual) == set(expected), where+' keys')
        for k in expected:
            compare(actual[k], expected[k], where+'.'+k)
    elif isinstance(expected, list):
        require(len(actual) == len(expected), where+' length')
        for i, (a, e) in enumerate(zip(actual, expected)):
            compare(a, e, where+f'[{i}]')
    elif isinstance(expected, float):
        require(np.isclose(actual, expected, rtol=2e-6, atol=2e-9), where+' numeric mismatch')
    else:
        require(actual == expected, where+' mismatch')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    actual = all_checks()
    output = ROOT/'results.json'
    if args.write:
        output.write_text(json.dumps(actual, indent=2)+'\n')
    else:
        compare(actual, json.loads(output.read_text()))
    print(json.dumps(dict(status='PASS', python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
                          weighted_instances=len(actual['weighted_profiles']),
                          max_dark_residual=max(x['collective_residual'] for x in actual['weighted_profiles']),
                          max_pair_residual=max(abs(x['bb84_error']-x['nominal_formula']) for x in actual['pair_lindblad']),
                          max_erasure_residual=max(x['max_residual'] for x in actual['single_excitation_erasure']),
                          working_point=actual['working_point'], capacity_example=actual['capacity_example']), indent=2))


if __name__ == '__main__':
    main()
