"""Check of (4.18) and (4.19) of 06-ilang-source/04-profile (item 2: range of the second-order form).

One field object, t_f = 1, on a ring (L = 64), a square torus (16 x 16) and a cubic torus (8^3).
delta(g) := lowest eigenvalue of C1 + V minus eps0 = lowest eigenvalue of Lambda + V (exact diagonalization).
(a) residual of the pole-free secular equation (4.18),
        |X| delta (c1 c2 - b^2 g1 g2) - (g1 c2 + g2 c1 - 2 b g1 g2),  c_i = 1 + g_i s0,  b = s_d,
        s(delta) = [(Lambda - delta)^{-1} Q] entries,
    at the exact delta, for couplings inside and far outside the regime of (4.19);
(b) the remainders r2 = max_x2 |M - M2| / calM and r3 = max_x2 |M - M2 - M3| / calM (x2 = x1 included),
    calM = 2 |g1 g2| l0 / |X|, against the bounds 4 eta/(1 - eta) and 4 eta^2/(1 - eta), eta = 16 l0 max|g_i|.
x2 runs over one representative of every class of separations under the symmetry of the graph.
"""
from itertools import product
from pathlib import Path
import numpy as np
from scipy.linalg import eigh

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
LOG = []


def out(s=""):
    print(s)
    LOG.append(s)


def laplacian(L, D):
    n = L**D
    idx = np.arange(n).reshape((L,) * D)
    A = np.zeros((n, n))
    for ax in range(D):
        nb = np.roll(idx, -1, axis=ax).ravel()
        A[idx.ravel(), nb] += 1
        A[nb, idx.ravel()] += 1
    return 2 * D * np.eye(n) - A, idx


def lowest(Lam, V):
    h = Lam.copy()
    for x, g in V:
        h[x, x] += g
    return eigh(h, eigvals_only=True, subset_by_index=[0, 0])[0]


graphs = [("ring L=64", 64, 1), ("square torus L=16", 16, 2), ("cubic torus L=8", 8, 3)]
for name, L, D in graphs:
    Lam, idx = laplacian(L, D)
    n = L**D
    w, U = eigh(Lam)
    assert abs(w[0]) < 1e-10 and w[1] > 1e-6
    Lp = (U[:, 1:] / w[1:]) @ U[:, 1:].T
    Lp2 = (U[:, 1:] / w[1:] ** 2) @ U[:, 1:].T
    l0, om1 = Lp[0, 0], w[1]
    reps = [idx[tuple(c)] for c in product(range(L // 2 + 1), repeat=D) if list(c) == sorted(c)]
    out(f"== {name}: |X| = {n}, l0 = Lambda^+(x,x) = {l0:.6f}, omega_1 = {om1:.6f}, l0 |X| omega_1 = {l0*n*om1:.3f}, "
        f"{len(reps)} separations")

    def S(delta, x2):
        r = 1.0 / (w[1:] - delta)
        return (U[0, 1:] * r) @ U[0, 1:], (U[0, 1:] * r) @ U[x2, 1:]

    # (a) residual of (4.18) at the exact lowest eigenvalue
    worst = 0.0
    for g1, g2 in [(0.01, 0.02), (0.3, -0.2), (3.0, 5.0), (-4.0, 1.5), (-10.0, -10.0)]:
        for x2 in reps[1:]:
            dl = lowest(Lam, [(0, g1), (x2, g2)])
            s0, sd = S(dl, x2)
            c1, c2 = 1 + g1 * s0, 1 + g2 * s0
            lhs, rhs = n * dl * (c1 * c2 - sd**2 * g1 * g2), g1 * c2 + g2 * c1 - 2 * sd * g1 * g2
            scale = abs(n * dl) * (abs(c1 * c2) + abs(sd**2 * g1 * g2)) + abs(g1 * c2) + abs(g2 * c1) + abs(2 * sd * g1 * g2)
            worst = max(worst, abs(lhs - rhs) / scale)
    out(f"   (4.18): max relative residual (|lhs - rhs| / sum of |terms|) at the exact lowest eigenvalue = {worst:.1e} "
        f"(couplings from (0.01,0.02) to (-10,-10))")

    # (b) remainders against the bound (4.19)
    out("   eta     g1         g2        r2        4eta/(1-eta)   r3        4eta^2/(1-eta)")
    for eta in [0.05, 0.25, 0.5, 0.9]:
        gm = eta / (16 * l0)
        for g1, g2 in [(gm, gm), (gm, -gm / 2), (-gm, -gm / 3)]:
            d1 = lowest(Lam, [(0, g1)])
            d2 = lowest(Lam, [(0, g2)])
            calM = 2 * abs(g1 * g2) * l0 / n
            r2 = r3 = 0.0
            for x2 in reps:
                V = [(0, g1 + g2)] if x2 == 0 else [(0, g1), (x2, g2)]
                M = lowest(Lam, V) - d1 - d2
                ld = Lp[0, x2]
                M2 = -2 * g1 * g2 * ld / n
                M3 = g1 * g2 * (g1 + g2) / n * (2 * l0 * ld + ld**2 - (Lp2[0, 0] + 2 * Lp2[0, x2]) / n)
                r2 = max(r2, abs(M - M2) / calM)
                r3 = max(r3, abs(M - M2 - M3) / calM)
            out(f"   {eta:4.2f}  {g1: .3e} {g2: .3e}  {r2:.2e}  {4*eta/(1-eta):.2e}       {r3:.2e}  "
                f"{4*eta**2/(1-eta):.2e}  {'ok' if (r2 <= 4*eta/(1-eta) and r3 <= 4*eta**2/(1-eta)) else 'VIOLATED'}")

# the pole case of Step 6: ring L = 4, g = (1, -1/2), d = 2 -> delta = 0 is a root of (4.18)
Lam, idx = laplacian(4, 1)
w, U = eigh(Lam)
Lp = (U[:, 1:] / w[1:]) @ U[:, 1:].T
dl = lowest(Lam, [(0, 1.0), (2, -0.5)])
c1, c2, b = 1 + 1.0 * Lp[0, 0], 1 - 0.5 * Lp[0, 0], Lp[0, 2]
out("")
out(f"Ring L=4, g=(1,-1/2), d=2: exact delta = {dl:.2e}; right side of (4.18) at delta=0: "
    f"{1.0*c2 - 0.5*c1 - 2*b*1.0*(-0.5):.2e}")

(OUT / "remainder_bound.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
