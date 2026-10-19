"""Check (i) of 06-ilang-source/04-profile.

Second-order mutual cost M2 computed numerically from the single-object contract
C1 = -t_f * (adjacency of the graph) via (4.3):
    M2 = -2 N_f g1 g2 phi(x1) phi(x2) R(x1, x2),   R = reduced resolvent of C1 at the eigenvalue of phi,
compared with the ring closed form (4.5) and the leading torus forms (4.6), (4.7).
Also: lowest + highest state on even rings (sum over the two ends, (4.13)).
"""
from pathlib import Path
from math import lgamma, log, pi
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import cg, LinearOperator

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
LOG = []


def out(s=""):
    print(s)
    LOG.append(s)


def torus_contract(L, D, t=1.0):
    """C1 = -t * sum over nearest-neighbour edges of the L^D torus (L >= 3)."""
    n = L**D
    idx = np.arange(n).reshape((L,) * D)
    r = np.concatenate([idx.ravel()] * D)
    c = np.concatenate([np.roll(idx, -1, axis=ax).ravel() for ax in range(D)])
    A = sp.coo_matrix((np.ones(len(r)), (r, c)), shape=(n, n)).tocsr()
    return -t * (A + A.T), idx


def phi_and_R(C1, which):
    """Eigenvector phi (which = 0: lowest, -1: highest) and reduced resolvent R of C1 at its eigenvalue."""
    e, v = np.linalg.eigh(C1)
    j = which % len(e)
    w = np.array([0.0 if k == j else 1.0 / (e[k] - e[j]) for k in range(len(e))])
    return v[:, j], (v * w) @ v.T


def m2_dense(C1, x1, x2, which, Nf=1, g1=1.0, g2=1.0, pr=None):
    """(4.3): M2 = -2 N_f g1 g2 phi(x1) phi(x2) R(x1, x2)."""
    phi, R = pr if pr is not None else phi_and_R(C1, which)
    return -2 * Nf * g1 * g2 * phi[x1] * phi[x2] * R[x1, x2]


def resolvent_column_cg(C1, phi, eps, x2, t=1.0):
    """R(., x2) from (C1 - eps + t |phi><phi|) y = e_x2 - phi phi(x2) by conjugate gradients."""
    n = C1.shape[0]
    op = LinearOperator((n, n), matvec=lambda u: C1 @ u - eps * u + t * phi * (phi @ u))
    b = -phi * phi[x2]
    b[x2] += 1.0
    y, info = cg(op, b, rtol=1e-13, atol=0.0, maxiter=20000)
    assert info == 0
    return y


# ---------------- ring: closed form (4.5) ----------------
out("== Ring: numerical (4.3) vs closed form (4.5); M2 * t_f * L^2 / (N_f g1 g2) vs d(L-d) - (L^2-1)/6 ==")
for L in [3, 4, 16, 101, 400]:
    for t in [1.0, 2.0]:
        C1 = -t * (np.eye(L, k=1) + np.eye(L, k=-1) + np.eye(L, k=L - 1) + np.eye(L, k=-(L - 1)))
        if L == 3:
            C1 = -t * (np.ones((3, 3)) - np.eye(3))
        dev = 0.0
        pr = phi_and_R(C1, 0)
        for d in range(1, L):
            M2 = m2_dense(C1, 0, d, 0, pr=pr)
            closed = (d * (L - d) - (L * L - 1) / 6) / (t * L * L)
            dev = max(dev, abs(M2 - closed) / ((L * L - 1) / (6 * t * L * L)))
        out(f"L={L:4d} t_f={t}: max_d |M2 - (4.5)| / max|(4.5)| = {dev:.2e}")
out("Ring L=3, d=1, t_f=1: M2 = %.12f, 2/27 = %.12f" % (m2_dense(-(np.ones((3, 3)) - np.eye(3)), 0, 1, 0), 2 / 27))

out("")
out("== Even rings: lowest + highest state (sum over the two ends, (4.13)); odd ring: top degeneracy ==")
for L in [4, 16, 64, 15]:
    C1 = -(np.eye(L, k=1) + np.eye(L, k=-1) + np.eye(L, k=L - 1) + np.eye(L, k=-(L - 1)))
    if L % 2 == 0:
        p0, p1 = phi_and_R(C1, 0), phi_and_R(C1, -1)
        s = max(abs(m2_dense(C1, 0, d, 0, pr=p0) + m2_dense(C1, 0, d, -1, pr=p1)) for d in range(1, L))
        out(f"L={L}: max_d |M2_lowest + M2_highest| = {s:.2e}")
    else:
        e = np.linalg.eigvalsh(C1)
        out(f"L={L} (odd): two highest eigenvalues of C1 = {e[-1]:.12f}, {e[-2]:.12f} (degenerate)")

# ---------------- square and cubic tori ----------------
kappa2 = 2 * lgamma(0.25) - log(2) - 0.5 * log(pi)  # ln(Gamma(1/4)^2 / (2 sqrt(pi)))
xi3 = -2.837297 / (4 * pi)
out("")
out(f"kappa_2 = {kappa2:.6f}, xi_3 = {xi3:.6f}")


def torus_table(D, Ls, rs, dirs, lead):
    for L in Ls:
        C1, idx = torus_contract(L, D)
        n = L**D
        phi = np.full(n, n**-0.5)
        eps = phi @ (C1 @ phi)
        res = np.linalg.norm(C1 @ phi - eps * phi)
        x2 = 0
        y = resolvent_column_cg(C1, phi, eps, x2)
        out(f"-- D={D}, L={L}: |X|={n}, eps0={eps:.6f}, ||C1 phi - eps0 phi|| = {res:.1e}, phi>0 (Perron)")
        out("   d vector        |d|     m_num        m_lead       m_num-m_lead")
        maxdev = 0.0
        for dv in dirs:
            for r in rs:
                d = tuple(r * a for a in dv)
                if max(d) > L // 4:
                    continue
                x1 = idx[d]
                M2 = -2 * phi[x1] * phi[x2] * y[x1]           # N_f = g1 = g2 = t_f = 1
                m_num = M2 * n                                  # M2 * t_f / (n g1 g2)
                dist = float(np.linalg.norm(d))
                m_lead = lead(dist, L)
                out(f"   {str(d):15s} {dist:6.2f} {m_num: .6f} {m_lead: .6f} {m_num - m_lead: .2e}")
                if 4 <= dist <= L / 8:
                    maxdev = max(maxdev, abs(m_num - m_lead))
        out(f"   max |m_num - m_lead| over 4 <= |d| <= L/8: {maxdev:.2e}")


out("")
out("== Square torus: m = M2 t_f/(n g1 g2) vs leading form (4.6): m_lead = -(1/pi)[ln(L/|d|) - kappa_2] ==")
torus_table(2, [64, 128, 256], [2, 4, 8, 16, 32], [(1, 0), (1, 1), (2, 1)],
            lambda r, L: -(log(L / r) - kappa2) / pi)
out("")
out("== Cubic torus: m vs leading form (4.7): m_lead = -2[1/(4 pi |d|) + xi_3/L] ==")
torus_table(3, [32, 48, 64], [2, 3, 4, 6, 8], [(1, 0, 0), (1, 1, 0), (1, 1, 1)],
            lambda r, L: -2 * (1 / (4 * pi * r) + xi3 / L))

(OUT / "second_order.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
