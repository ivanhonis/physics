"""Check (i) of 07-bond-inertia: the mutual term (7.3)-(7.4) against second-order
perturbation theory in the total contract, restricted to at most two field quanta.

Ring of L = 16 cells, two Model D bodies (clock level fixed, so S_i -> M_i sigma_3),
grip F(q) = F0 + F1 q + F2 q^2.  The unperturbed contract H0 contains the motion terms,
the first-order grip abar*M_i*sigma_3 (abar = F0 + F2 w0) and the field; the
perturbation is V = sum_i sum_x |x><x| M_i sigma_3 (dF(q_x) - F2 w0).  The mutual
term is the part of the symmetric (des Cloizeaux) second-order effective contract with
one vertex on each body.  Everything is built numerically in the position basis of the
bodies and the occupation basis of the field modes (<= 2 quanta).
"""
import json
from itertools import combinations_with_replacement
from pathlib import Path

import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)


def fock(L):
    states = [()] + [(j,) for j in range(L)] + list(combinations_with_replacement(range(L), 2))
    index = {s: i for i, s in enumerate(states)}
    B = np.zeros((L, len(states), len(states)))
    for i, s in enumerate(states):
        for j in set(s):
            t = list(s); t.remove(j)
            B[j, index[tuple(sorted(t))], i] = np.sqrt(s.count(j))
    return states, B


def body(L, tau, Mbar):
    """Position-basis contract (index 2x+s) and its plane-wave eigenvectors."""
    s1 = np.array([[0, 1], [1, 0]], complex); s3 = np.diag([1.0, -1.0]).astype(complex)
    h = np.zeros((2 * L, 2 * L), complex)
    for x in range(L):
        y = (x + 1) % L
        h[2*y:2*y+2, 2*x:2*x+2] += 0.5 * tau * (-1j * s1)
        h[2*x:2*x+2, 2*y:2*y+2] += 0.5 * tau * (1j * s1)
        h[2*x:2*x+2, 2*x:2*x+2] += Mbar * s3
    W = np.zeros((2 * L, 2 * L), complex); e = np.zeros(2 * L); lab = []
    xs = np.arange(L)
    for n in range(L):
        p = 2 * np.pi * n / L
        pw = np.exp(1j * p * xs) / np.sqrt(L)
        blk = np.array([[np.vdot(np.kron(pw, np.eye(2)[a]), h @ np.kron(pw, np.eye(2)[b]))
                         for b in range(2)] for a in range(2)])
        ev, U = np.linalg.eigh(blk)
        for col, band in ((1, +1), (0, -1)):
            u = U[:, col]
            ref = u[0] if band == +1 else u[1]          # phase convention of Step 1
            u = u * abs(ref) / ref if abs(ref) > 1e-12 else u
            v = np.kron(pw, u); k = len(lab)
            W[:, k] = v; e[k] = ev[col]; lab.append((n, band))
    resid = np.max(np.abs(h @ W - W * e))
    return W, e, lab, resid


def run(case):
    L, kap, mh, tau = case["L"], case["kappa_h"], case["m_h"], case["tau"]
    M1, M2, sg1, sg2 = case["M1"], case["M2"], case["sigma1"], case["sigma2"]
    F0, F1, F2 = case["F0"], case["F1"], case["F2"]
    qs = 2 * np.pi * np.arange(L) / L
    om = np.sqrt(mh**2 + 4 * kap * np.sin(qs / 2)**2)
    w0 = np.sum(1 / (2 * L * om))
    abar = F0 + F2 * w0
    states, B = fock(L)
    EF = np.array([sum(om[j] for j in s) for s in states])
    vac = np.zeros(len(states)); vac[0] = 1
    X = []
    for x in range(L):
        qx = sum((B[j] * np.exp(1j * qs[j] * x) + B[j].T * np.exp(-1j * qs[j] * x))
                 / np.sqrt(2 * L * om[j]) for j in range(L))
        chi = F1 * (qx @ vac) + F2 * (qx @ (qx @ vac) - w0 * vac)
        X.append(chi)
    X = np.array(X)                                   # (x, fock)
    assert abs(X[:, 0]).max() < 1e-12                 # no vacuum component
    W1, e1, lab1, r1 = body(L, tau, abar * M1)
    W2, e2, lab2, r2 = body(L, tau, abar * M2)
    s3 = np.diag([1.0, -1.0])

    def Y(psi1, psi2):
        B1 = np.zeros((2 * L, L), complex); B2 = np.zeros((2 * L, L), complex)
        for x in range(L):
            B1[2*x:2*x+2, x] = M1 * s3 @ psi1[2*x:2*x+2]
            B2[2*x:2*x+2, x] = M2 * s3 @ psi2[2*x:2*x+2]
        V1 = np.einsum('ax,b,xc->abc', B1, psi2, X)
        V2 = np.einsum('a,bx,xc->abc', psi1, B2, X)
        tr = lambda T: np.einsum('ap,bq,abc->pqc', W1.conj(), W2.conj(), T)
        return tr(V1), tr(V2)

    En = e1[:, None, None] + e2[None, :, None] + EF[None, None, :]
    idx1 = {l: i for i, l in enumerate(lab1)}; idx2 = {l: i for i, l in enumerate(lab2)}

    def eps(M, sg, p):
        return sg * np.sqrt((abar * M)**2 + tau**2 * np.sin(p)**2)

    def th(M, p):
        return np.arctan2(tau * np.sin(p), abar * M)

    rows = []
    for (n1, n2, m) in case["labels"]:
        i1, i2 = idx1[(n1 % L, sg1)], idx2[(n2 % L, sg2)]
        f1, f2 = idx1[((n1 - m) % L, sg1)], idx2[((n2 + m) % L, sg2)]
        Yi = Y(W1[:, i1], W2[:, i2]); Yf = Y(W1[:, f1], W2[:, f2])
        Ei, Ef = e1[i1] + e2[i2], e1[f1] + e2[f2]
        cross = (Yf[0].conj() * Yi[1] + Yf[1].conj() * Yi[0])[:, :, 1:]   # Q: >= 1 quantum
        num = 0.5 * np.sum(cross * (1 / (Ei - En[:, :, 1:]) + 1 / (Ef - En[:, :, 1:])))
        # closed form (7.3)-(7.4)
        p1, p2, q = qs[n1 % L], qs[n2 % L], qs[m % L]
        p1f, p2f = p1 - q, p2 + q
        D1 = eps(M1, sg1, p1) - eps(M1, sg1, p1f); D2 = eps(M2, sg2, p2f) - eps(M2, sg2, p2)
        c1 = np.cos((th(M1, p1) + th(M1, p1f)) / 2); c2 = np.cos((th(M2, p2) + th(M2, p2f)) / 2)
        mu12 = sg1 * M1 * sg2 * M2
        wq = om[m % L]
        U1 = -mu12 * F1**2 * c1 * c2 / (2 * L) * (1 / (wq**2 - D1**2) + 1 / (wq**2 - D2**2))
        ob = om[(m - np.arange(L)) % L]; Om = om + ob
        U2 = -mu12 * F2**2 * c1 * c2 / (2 * L**2) * np.sum(Om / (om * ob) * (
            1 / (Om**2 - D1**2) + 1 / (Om**2 - D2**2)))
        form = U1 + U2
        rows.append({"labels_n1_n2_m": [n1, n2, m], "numerical": [num.real, num.imag],
                     "formula": form, "rel_dev": abs(num - form) / abs(form)})
    return {"case": {k: v for k, v in case.items() if k != "labels"}, "abar": abar,
            "eigvec_residual": max(r1, r2), "rows": rows,
            "max_rel_dev": max(r["rel_dev"] for r in rows)}


labels = [(0, 0, 1), (1, -2, 3), (3, -5, 2), (-2, 4, -1), (5, 2, 7), (2, 2, 0), (-3, 1, 0), (6, -6, 8)]
base = dict(L=16, kappa_h=1.0, m_h=0.3, tau=0.8, M1=0.7, M2=0.5, F0=1.0, F1=0.3, F2=0.2,
            sigma1=1, sigma2=1, labels=labels)
cases = [base,
         dict(base, F2=base["F1"]**2 / (4 * base["F0"])),          # square grip
         dict(base, sigma2=-1),                                     # mixed branches
         dict(base, tau=1.3)]                                       # r > 1
res = [run(c) for c in cases]
summary = {"max_rel_dev_all": max(r["max_rel_dev"] for r in res), "cases": res}
(OUT / "mutual_term_check.json").write_text(json.dumps(summary, indent=1))
for r in res:
    print(r["case"]["tau"], r["case"]["F2"], r["case"]["sigma2"], "max rel dev", r["max_rel_dev"],
          "resid", r["eigvec_residual"])
print("overall", summary["max_rel_dev_all"])
