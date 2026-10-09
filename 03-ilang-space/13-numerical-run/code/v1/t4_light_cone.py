"""T4 (computation): light cone, test of (8.16), with negative control.
Diagnostic (labelled): mpmath (40 digits) recomputation of Delta W to bound double-precision rounding."""
import itertools

import mpmath as mp
import numpy as np
from scipy.linalg import expm

from common import gue, haar_state, view, wmat, slope, cjson, save

L = 5
grid = [0.1, 0.05, 0.025, 0.0125]
rng = np.random.default_rng(1309)
cells = [haar_state(rng, 2) for _ in range(L)]        # c_1..c_5, in this order
omega = cells[0]
for c in cells[1:]:
    omega = np.kron(omega, c)                          # c_1 is the leftmost tensor factor
Jk = {k: gue(np.random.default_rng(1310 + k), 4) for k in range(1, L)}
rng = np.random.default_rng(1320); Kh = [gue(rng, 2) for _ in range(3)]
rng = np.random.default_rng(1330); Bb = [gue(rng, 2) for _ in range(2)]   # B_beta1, B_beta2
phi = np.full(3, 1 / np.sqrt(3))
pairs = list(itertools.combinations(range(3), 2))


def on(op, first):
    """Embed an operator acting on cells first, first+1, ... (1-indexed) into the 2^L medium."""
    nc = int(round(np.log2(op.shape[0])))
    return np.kron(np.kron(np.eye(2 ** (first - 1)), op), np.eye(2 ** (L - first - nc + 1)))


Jsum = sum(on(Jk[k], k) for k in range(1, L))


def W_of(B_cell_op, lam):
    psis = np.array([phi[h] * (expm(-1j * lam * (on(Kh[h], 1) + B_cell_op + Jsum)) @ omega) for h in range(3)])
    return wmat(view(psis))                            # (12.8), (2.11)


def mp_W(B_cell_op, lam):
    mp.mp.dps = 40
    lam = mp.mpf(lam)
    out = []
    for h in range(3):
        M = on(Kh[h], 1) + B_cell_op + Jsum
        Mm = [[mp.mpc(complex(M[i, j])) for j in range(32)] for i in range(32)]
        v = [mp.mpc(complex(z)) for z in omega]
        acc, term, n = list(v), list(v), 0
        while True:                                    # Taylor series of exp(-i lam M) v
            n += 1
            term = [(-1j * lam / n) * mp.fsum(Mm[i][j] * term[j] for j in range(32)) for i in range(32)]
            acc = [acc[i] + term[i] for i in range(32)]
            if max(abs(t) for t in term) < mp.mpf("1e-45"):
                break
        out.append(acc)
    G = lambda a, b: mp.fsum(mp.conj(b[i]) * a[i] for i in range(32))   # <b|a>
    nrm = [G(out[h], out[h]).real for h in range(3)]
    return {(h, k): abs(G(out[h], out[k])) ** 2 / (nrm[h] * nrm[k]) for h, k in pairs}


res, ok_all, control_ok = {}, True, True
W0 = {lam: W_of(0.0, lam) for lam in grid}
mpW0 = {lam: mp_W(0.0, lam) for lam in grid}
for r in range(4):
    Bop = on(Bb[0], r + 1)
    rows, mx, mx_mp, ctrl = [], [], [], []
    for lam in grid:
        dW = W_of(Bop, lam) - W0[lam]
        per = {f"{h+1},{k+1}": float(dW[h, k]) for h, k in pairs}
        mx.append(max(abs(v) for v in per.values()))
        mW = mp_W(Bop, lam)
        dmp = {p: mW[p] - mpW0[lam][p] for p in pairs}
        mx_mp.append(float(max(abs(v) for v in dmp.values())))
        dWc = W_of(on(0.7 * np.eye(2), r + 1), lam) - W0[lam]
        ctrl.append(float(np.max(np.abs(dWc[np.triu_indices(3, 1)]))))
        rows.append({"lambda": lam, "Delta_W_per_pair": per, "max_abs_Delta_W": mx[-1],
                     "diag_mpmath_max_abs_Delta_W": mx_mp[-1],
                     "diag_rel_dev_double_vs_mpmath": abs(mx[-1] - mx_mp[-1]) / mx_mp[-1],
                     "control_max_abs_Delta_W": ctrl[-1]})
    s, s_mp = slope(grid, mx), slope(grid, mx_mp)
    ok = s >= 3 + r - 0.2
    ok_all &= ok
    c_ok = all(c <= 1e-12 for c in ctrl)
    control_ok &= c_ok
    res[f"r={r}"] = {"per_lambda": rows, "fitted_slope": s, "threshold": 3 + r - 0.2, "slope_ok": ok,
                     "exploratory_within_0.2_of_3+r": abs(s - (3 + r)) <= 0.2,
                     "diag_mpmath_fitted_slope": s_mp, "control_ok": c_ok}
    print(f"r={r}: max|dW|={['%.3e' % v for v in mx]} slope={s:.4f} (thr {3+r-0.2}) mp-slope={s_mp:.4f} "
          f"control max={max(ctrl):.2e}")
dec, dec_c = ("pass" if ok_all else "fail"), ("pass" if control_ok else "fail")
print("decision:", dec, " control:", dec_c)
save("t4_light_cone.json", {
    "part": "T4", "L": L, "grid": grid, "seeds": {"cells": 1309, "J_k": "1310+k", "K_h": 1320, "B_beta": 1330},
    "cell_states": [cjson(c) for c in cells], "J": {k: cjson(Jk[k]) for k in Jk},
    "K": [cjson(K) for K in Kh], "B": [cjson(B) for B in Bb], "results": res,
    "rule": "pass iff slope >= 3+r-0.2 for every r", "decision": dec,
    "control_rule": "B_beta1 = 0.7*1: pass iff max|Delta W| <= 1e-12 at every lambda", "control_decision": dec_c})
