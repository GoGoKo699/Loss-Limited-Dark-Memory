"""Finite weighted-kernel/capacity diagnostics; not a general proof."""
import numpy as np
from scipy.linalg import null_space, eigvalsh
from scipy.optimize import minimize_scalar


def h2(x):
    if x <= 0 or x >= 1:
        return 0.0
    return float(-x*np.log2(x)-(1-x)*np.log2(1-x))


def entropy(rho):
    vals = eigvalsh((rho+rho.conj().T)/2)
    vals = vals[vals > 1e-13]
    return float(-np.sum(vals*np.log2(vals)))


def lowering(n, j):
    d = 1 << n
    out = np.zeros((d, d), complex)
    for k in range(d):
        if (k >> j) & 1:
            out[k ^ (1 << j), k] = 1
    return out


def amplitude_damping(rho, n, eta):
    out = rho.copy()
    for j in range(n):
        i0 = np.array([k for k in range(1 << n) if not ((k >> j) & 1)])
        i1 = i0 | (1 << j)
        old = out.copy()
        out[np.ix_(i0, i0)] = old[np.ix_(i0, i0)] + (1-eta)*old[np.ix_(i1, i1)]
        out[np.ix_(i1, i1)] = eta*old[np.ix_(i1, i1)]
        out[np.ix_(i0, i1)] = np.sqrt(eta)*old[np.ix_(i0, i1)]
        out[np.ix_(i1, i0)] = np.sqrt(eta)*old[np.ix_(i1, i0)]
    return out


def dissipator(op, rho):
    a = op.conj().T @ op
    return op @ rho @ op.conj().T - (a @ rho + rho @ a)/2


def instance(n, r, eta, seed):
    rng = np.random.default_rng(seed)
    gs = rng.normal(size=(r,n)) + 1j*rng.normal(size=(r,n))
    singles = [lowering(n,j) for j in range(n)]
    ls = [sum(gj*sj for gj,sj in zip(g,singles)) for g in gs]
    k = null_space(np.vstack(ls), rcond=1e-11)
    proj = k @ k.conj().T
    excitation = np.array([j.bit_count() for j in range(1 << n)])
    opt = minimize_scalar(lambda p: -(h2(eta*p)-h2((1-eta)*p)),
                          bounds=(1e-8,.5), method='bounded', options={'xatol':1e-14})
    p = float(opt.x)
    z = p/(1-p)
    weighted = proj * (z**excitation)[None,:]
    zk = float(np.trace(weighted).real)
    rho = weighted/zk
    out = amplitude_damping(rho,n,eta)
    env = amplitude_damping(rho,n,1-eta)
    ic = entropy(out)-entropy(env)
    q = -float(opt.fun)
    c = -np.log2(1-z)
    random_v = k @ (rng.normal(size=k.shape[1])+1j*rng.normal(size=k.shape[1]))
    random_v /= np.linalg.norm(random_v)
    random_out = amplitude_damping(np.outer(random_v,random_v.conj()),n,eta)
    invariant_residual = max(np.linalg.norm(dissipator(l,random_out)) for l in ls)
    return dict(n=n,r=r,eta=eta,dark_dimension=k.shape[1],p_star=p,q_ad=q,
                c_eta=float(c),partition=zk,partition_lower=(1+z)**n*(1-z)**r,
                coherent_information=ic,ci_lower=n*q-r*c,
                ci_margin=ic-(n*q-r*c),collective_residual=float(invariant_residual))
