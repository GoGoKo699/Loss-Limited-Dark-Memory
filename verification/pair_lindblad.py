"""Direct Lindblad check of a two-emitter passive delayed-basis memory."""
import numpy as np
from scipy.linalg import expm
from weighted_capacity import lowering


def ds(l):
    a=l.conj().T@l
    d=l.shape[0]
    return np.kron(l.conj(),l)-.5*(np.kron(np.eye(d),a)+np.kron(a.T,np.eye(d)))


def run(theta,eta,gamma,nu=0.,bright_shift=0.):
    s0,s1=lowering(2,0),lowering(2,1)
    e=np.eye(4,dtype=complex)
    d0=(e[:,1]-e[:,2])/np.sqrt(2)
    b0=(e[:,1]+e[:,2])/np.sqrt(2)
    ba=np.cos(theta)*b0+np.sin(theta)*d0
    l=np.sqrt(gamma)*(np.conj(ba[1])*s0+np.conj(ba[2])*s1)
    kappa=-np.log(eta)
    gen=ds(l)+kappa*(ds(s0)+ds(s1))
    ham=bright_shift*np.outer(ba,ba.conj())
    gen+=-1j*(np.kron(np.eye(4),ham)-np.kron(ham.T,np.eye(4)))
    for j in range(2):
        z=np.diag([1 if not ((k>>j)&1) else -1 for k in range(4)])
        gen+=nu*ds(z)
    evol=expm(gen)
    v=np.column_stack([e[:,0],d0])
    def channel(rho):
        big=v@rho@v.conj().T
        out=(evol@big.reshape(-1,order='F')).reshape((4,4),order='F')
        small=v.conj().T@out@v
        small[0,0]+=np.vdot(b0,out@b0)
        small[1,1]+=out[3,3]
        return small
    a=np.sqrt(eta)*(np.cos(theta)**2+np.exp(-gamma/2-1j*bright_shift)*np.sin(theta)**2)
    rho0=np.array([[1,0],[0,0]],complex)
    rho1=np.array([[0,0],[0,1]],complex)
    rhop=np.array([[1,1],[1,1]],complex)/2
    rhom=np.array([[1,-1],[-1,1]],complex)/2
    err=1-sum(np.trace(rho@channel(rho)).real for rho in [rho0,rho1,rhop,rhom])/4
    expected=(2-abs(a)**2-a.real)/4
    if nu==0:
        assert abs(err-expected)<1e-10
    return dict(theta_degrees=float(np.rad2deg(theta)),local_survival=eta,
                collective_rate=gamma,local_dephasing_each=nu,bright_shift=bright_shift,
                bb84_error=float(err),nominal_formula=float(expected))
