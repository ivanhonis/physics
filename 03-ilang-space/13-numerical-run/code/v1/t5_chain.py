"""T5 (computation and check): local records and a chain at finite lambda, 16 qubit cells (dim 65536).
Computation: W, points, N_V, path analysis for local g=0, local g=0.5 and the nonlocal control.
Check: closed form W = prod_k cos^2(lambda (F_hk - F_h'k)) for g = 0 (local records and control)."""
import itertools

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply

from common import view, wmat, points, neighbour_graph, path_analysis, save

L, n = 16, 10
D = 2 ** L
grid = [0.05, 0.3, 1.0]
sx = sp.csr_matrix(np.array([[0, 1], [1, 0]], complex))
sy = sp.csr_matrix(np.array([[0, -1j], [1j, 0]], complex))


def emb(op, k, ncell):
    """Operator on cells k..k+ncell-1 (1-indexed), cell 1 = leftmost tensor factor."""
    return sp.kron(sp.kron(sp.identity(2 ** (k - 1), format="csr"), op),
                   sp.identity(2 ** (L - k - ncell + 1), format="csr"), format="csr")


SX = [emb(sx, k, 1) for k in range(1, L + 1)]
XXYY = sum(emb(sp.kron(sx, sx) + sp.kron(sy, sy), k, 2) for k in range(1, L))   # k = 1..15
omega = np.zeros(D, complex); omega[0] = 1.0                                       # |0>^{(x)16}
phi = np.full(n, 1 / np.sqrt(n))

f = np.array([[np.exp(-(i + 3 - k) ** 2 / (2 * 1.5 ** 2)) for k in range(1, L + 1)] for i in range(1, n + 1)])
R = np.random.default_rng(1340).standard_normal((n, L))
R = R * np.sqrt((f ** 2).sum(1) / (R ** 2).sum(1))[:, None]       # row-wise rescaling


def records(F):
    return [sum(F[i, k] * SX[k] for k in range(L)) for i in range(n)]


def closed_form_W(F, lam):
    return np.array([[np.prod(np.cos(lam * (F[i] - F[j])) ** 2) for j in range(n)] for i in range(n)])


cases = {"local_g0": (f, 0.0), "local_g0.5": (f, 0.5), "control_g0": (R, 0.0)}
out = {"part": "T5", "L": L, "n_places": n, "grid": grid, "f": f.tolist(), "R_rescaled": R.tolist(),
       "seed_R": 1340, "cases": {}}
for name, (F, g) in cases.items():
    Ks = records(F)
    Ms = [K + g * XXYY for K in Ks]
    rows = []
    for lam in grid:
        vecs = [expm_multiply(-1j * lam * M, omega) for M in Ms]                    # (12.8)
        psis = np.array([phi[i] * vecs[i] for i in range(n)])
        W = wmat(view(psis))                                                         # (2.11)
        pts = points(W)
        rep = [c[0] for c in pts]
        Wp = W[np.ix_(rep, rep)]
        edges, A, margin = neighbour_graph(Wp)                                      # (4.3)
        pa = path_analysis(len(pts), edges, A)                                       # (4.6) for ell
        row = {"lambda": lam, "W": W.tolist(), "points": [[h + 1 for h in c] for c in pts],
               "N_V_edges": [[[h + 1 for h in pts[i]], [h + 1 for h in pts[j]]] for i, j in edges],
               "alpha_points": A.tolist(), "min_W": float(W.min()), **pa,
               "diag_min_margin_in_(4.3)": margin,
               "diag_max_norm_dev": float(max(abs(np.linalg.norm(v) - 1) for v in vecs))}
        if pa["is_path"]:
            row["order_places"] = [[h + 1 for h in pts[v]] for v in pa["order"]]
        if g == 0.0:
            row["check_max_abs_dev_from_closed_form"] = float(np.max(np.abs(W - closed_form_W(F, lam))))
        if g == 0.5 and lam == 1.0:   # diagnostic: independent Taylor propagation (40 substeps)
            tay = []
            for M in Ms:
                v = omega.copy()
                for _ in range(40):
                    acc, term, m = v.copy(), v.copy(), 0
                    while np.linalg.norm(term) > 1e-18:
                        m += 1
                        term = (-1j * lam / 40 / m) * (M @ term)
                        acc = acc + term
                    v = acc
                tay.append(v)
            Wt = wmat(view(np.array([phi[i] * tay[i] for i in range(n)])))
            row["diag_taylor_max_abs_dev_vectors"] = float(max(np.max(np.abs(a - b)) for a, b in zip(vecs, tay)))
            row["diag_taylor_max_abs_dev_W"] = float(np.max(np.abs(W - Wt)))
        rows.append(row)
        print(f"{name} lambda={lam}: points={len(pts)} edges={len(edges)} degrees={pa['degrees']} "
              f"path={pa['is_path']} order={row.get('order_places')} ell={pa.get('ell_ends')} "
              f"check={row.get('check_max_abs_dev_from_closed_form')} margin={margin:.3e} minW={W.min():.3e}")
    out["cases"][name] = {"g": g, "per_lambda": rows}

c1 = all(r["is_path"] for r in out["cases"]["local_g0"]["per_lambda"])
c2 = not [r for r in out["cases"]["control_g0"]["per_lambda"] if r["lambda"] == 0.3][0]["is_path"]
out.update({"condition_local_g0_path_at_all_lambda": c1, "condition_control_not_path_at_0.3": c2,
            "rule": "supported iff local g=0 path at all three lambda and control not path at lambda=0.3",
            "decision": "pass" if (c1 and c2) else "fail"})
print("conditions:", c1, c2, "decision:", out["decision"])
save("t5_chain.json", out)
