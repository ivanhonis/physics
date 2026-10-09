"""T1 (computation): leading order alpha/lambda -> d_0, test of (5.10)."""
import itertools

import numpy as np
from scipy.linalg import expm

from common import gue, view, wmat, alpha, points, slope, cjson, save

n, dc = 8, 6
grid = [1e-1, 3e-2, 1e-2, 3e-3, 1e-3]
rng = np.random.default_rng(1301)
K = [gue(rng, dc) for _ in range(n)]          # records K_h, h = 1..8 in draw order
chi = np.zeros(dc, complex); chi[0] = 1.0      # |chi> = e_1
phi = np.full(n, 1 / np.sqrt(n))

u = np.array([Kh @ chi - (chi.conj() @ Kh @ chi) * chi for Kh in K])
d0 = np.array([[np.linalg.norm(u[h] - u[k]) for k in range(n)] for h in range(n)])
pairs = list(itertools.combinations(range(n), 2))

rows, E = [], []
for lam in grid:
    psis = np.array([phi[h] * (expm(-1j * lam * K[h]) @ chi) for h in range(n)])  # (12.8)
    V = view(psis)
    W = wmat(V)
    A = alpha(W)
    rel = {f"{h+1},{k+1}": float(abs(A[h, k] / lam - d0[h, k]) / d0[h, k]) for h, k in pairs}
    E.append(max(rel.values()))
    rows.append({"lambda": lam, "W": W.tolist(), "alpha": A.tolist(), "rel_err_per_pair": rel,
                 "E": E[-1], "n_points": len(points(W))})
    print(f"lambda={lam:.0e}  E={E[-1]:.6e}  points={len(points(W))}")

s = slope(grid, E)
passed = bool(E[-1] < 1e-2 and s >= 0.9)
print(f"slope={s:.6f}  decision={'pass' if passed else 'fail'}")
save("t1_leading_order.json", {
    "part": "T1", "n": n, "d_c": dc, "seed": 1301, "grid": grid,
    "records_K": [cjson(Kh) for Kh in K], "u": cjson(u), "d0": d0.tolist(),
    "per_lambda": rows, "E": E, "fitted_slope_E": s,
    "rule": "pass iff E(1e-3) < 1e-2 and slope >= 0.9", "decision": "pass" if passed else "fail"})
