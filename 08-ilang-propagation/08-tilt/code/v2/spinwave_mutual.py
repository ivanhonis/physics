"""Check (item 3, leading order in 1/S): mutual cost of two held sources on the cubic torus.

Units J S = 1.  Quadratic form C_2 = 1/2 P^T T P + 1/2 Q^T V Q, T_k = z(1+gamma_k), V_k = z(1-gamma_k).
(1) Transverse direction sources (linear in Q): E_12 = -S eps1 eps2 g1 g2 G_a(x1,x2); the separation part is
    J E_r/(g1 g2) = -eps1 eps2 ghat(r), ghat = Lap^+ (single objects); -eps1 eps2 sum_{a,b} ghat(a-b) (two-object cells).
(2) Quadratic sources dH_i = 1/2 Q^T A_i Q + 1/2 P^T B_i P (along-n sources, bound held spin as a spin-length defect,
    changed link): E_12 = -2 int_0^inf dtau <dH_1(tau) dH_2(0)>_c, Wick with G_QQ, G_PP and G_QP = (i/2) F (tau > 0);
    far-from-push limit: the two zero modes (k = 0, k = Q) are left out.
Output: output/spinwave_mutual.txt
"""
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import ive

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
Z = 6


def kgrid(L):
    k = 2 * np.pi * np.arange(L) / L
    c = np.cos(k)
    g = (c[:, None, None] + c[None, :, None] + c[None, None, :]) / 3.0
    return g


def ghat(L):
    k = 2 * np.pi * np.arange(L) / L
    lap = 2 * ((1 - np.cos(k))[:, None, None] + (1 - np.cos(k))[None, :, None] + (1 - np.cos(k))[None, None, :])
    inv = np.zeros_like(lap)
    inv[lap > 1e-12] = 1.0 / lap[lap > 1e-12]
    return np.real(np.fft.ifftn(inv))


def ghat_inf(x):
    """Infinite cubic lattice: (Lap^{-1})(x) = int_0^inf prod_i e^{-2t} I_{x_i}(2t) dt."""
    f = lambda t: np.prod([ive(abs(int(c)), 2 * t) for c in x])
    return quad(f, 0, np.inf, limit=400, epsabs=1e-13, epsrel=1e-11)[0]


def eps(x):
    return (-1) ** (int(sum(x)) % 2)


def check_58(L=6, eta=0.7):
    n = L ** 3
    co = np.array(np.unravel_index(np.arange(n), (L,) * 3)).T
    adj = np.zeros((n, n))
    for d in range(3):
        sh = co.copy(); sh[:, d] = (sh[:, d] + 1) % L
        j = np.ravel_multi_index(sh.T, (L,) * 3)
        adj[np.arange(n), j] += 1; adj[j, np.arange(n)] += 1
    V = Z * np.eye(n) - adj
    V[0, 0] += eta
    Ga = np.linalg.inv(V)
    g = ghat(L).ravel()
    dif = lambda a, b: np.ravel_multi_index(tuple((co[a] - co[b]) % L), (L,) * 3)
    err = 0.0
    for a, b in [(5, 17), (40, 101), (3, 3), (0, 77)]:
        f = 1 / eta + g[dif(a, b)] - g[dif(a, 0)] - g[dif(b, 0)] + g[0]
        err = max(err, abs(f - Ga[a, b]))
    return err


def pert(kind, x, e=None):
    """Return (A, B) as lists of (site, site, value); per unit strength (see header of output)."""
    x = tuple(x)
    if kind == "along":
        A = [(x, x, -eps(x))]
        return A, A
    if kind == "along_cell":
        x2 = (x[0], x[1] + 1, x[2])
        A = [(x, x, -eps(x)), (x2, x2, -eps(x))]
        return A, A
    if kind == "defect":
        nb = []
        for d in range(3):
            for s in (1, -1):
                y = list(x); y[d] += s; nb.append(tuple(y))
        A = [(x, x, -Z)] + [(x, y, 0.5) for y in nb] + [(y, x, 0.5) for y in nb]
        B = [(x, x, -Z)] + [(x, y, -0.5) for y in nb] + [(y, x, -0.5) for y in nb]
        return A, B
    if kind == "link":
        y = tuple(np.array(x) - np.array(e))
        A = [(x, x, 1), (y, y, 1), (x, y, -1), (y, x, -1)]
        B = [(x, x, 1), (y, y, 1), (x, y, 1), (y, x, 1)]
        return A, B
    raise ValueError(kind)


def contraction(M1, M2, L):
    w, i1, i2 = [], [], []
    for a, b, u in M1:
        for c, d, v in M2:
            w.append(u * v)
            i1.append(np.ravel_multi_index(tuple(np.mod(np.array(a) - np.array(c), L)), (L,) * 3))
            i2.append(np.ravel_multi_index(tuple(np.mod(np.array(b) - np.array(d), L)), (L,) * 3))
    return np.array(w), np.array(i1), np.array(i2)


def mutual_quadratic(L, configs, nodes=400):
    g = kgrid(L)
    om = Z * np.sqrt(np.clip(1 - g ** 2, 0, None))
    mask = om > 1e-9
    Tk = np.where(mask, Z * (1 + g), 0.0)
    Vk = np.where(mask, Z * (1 - g), 0.0)
    omm = np.where(mask, om, 1.0)
    pre = []
    for (A1, B1), (A2, B2) in configs:
        pre.append((contraction(A1, A2, L), contraction(B1, B2, L),
                    contraction(A1, B2, L), contraction(B1, A2, L)))
    s, ws = np.polynomial.legendre.leggauss(nodes)
    lo, hi = np.log(1e-7), np.log(200.0)
    sv = 0.5 * (hi - lo) * s + 0.5 * (hi + lo)
    wv = 0.5 * (hi - lo) * ws
    acc = np.zeros(len(configs))
    for sj, wj in zip(sv, wv):
        tau = np.exp(sj)
        ex = np.where(mask, np.exp(-omm * tau), 0.0)
        GQ = np.real(np.fft.ifftn(Tk / (2 * omm) * ex)).ravel()
        GP = np.real(np.fft.ifftn(Vk / (2 * omm) * ex)).ravel()
        F = np.real(np.fft.ifftn(ex)).ravel()
        for n, (qq, pp, qp, pq) in enumerate(pre):
            val = 0.5 * np.sum(qq[0] * GQ[qq[1]] * GQ[qq[2]]) + 0.5 * np.sum(pp[0] * GP[pp[1]] * GP[pp[2]]) \
                - 0.125 * (np.sum(qp[0] * F[qp[1]] * F[qp[2]]) + np.sum(pq[0] * F[pq[1]] * F[pq[2]]))
            acc[n] += wj * tau * val
    return -2 * acc


def cont_link(e1, e2, e12):
    """Continuum: J E/(delta1 delta2 S) * r^7 for two changed links (unit vectors e1, e2), r along axis 1."""
    def C(t):
        X = np.array([t, 1.0, 0, 0]); rho = np.linalg.norm(X); n = X / rho
        I = np.eye(4) - 4 * np.outer(n, n)
        E1 = np.r_[0, e1]; E2 = np.r_[0, e2]; t0 = np.r_[1.0, 0, 0, 0]
        M1 = np.outer(E1, E1) - (2 / Z) * np.outer(t0, t0)
        M2 = np.outer(E2, E2) - (2 / Z) * np.outer(t0, t0)
        cross = I[0, 0] * (E1 @ I @ E2) - (I @ E1)[0] * (I @ E2)[0]
        return (4 * np.trace(M1 @ I @ M2 @ I) - (16 / Z) * e12 * cross) / rho ** 8
    val = quad(C, -np.inf, np.inf, epsabs=1e-13, epsrel=1e-12)[0]
    return -np.sqrt(2 * Z) / (16 * np.pi ** 4) * val


def main():
    out = ["# Mutual cost of two held sources, leading order in 1/S, cubic torus (units as stated per block)"]
    out.append(f"\n(5.8) with kappa_h = J S, kappa_a = h_p against direct inverse (L=6): max error {check_58():.2e}")
    out.append("\n## (1) Transverse sources: separation part J E_r/(g1 g2 (m1perp.m2perp))")
    out.append("single objects: -eps1 eps2 ghat(r); cells (x, x+e2), + on the first object: -eps1 eps2 sum ghat")
    out.append(f"ghat_inf(0) = {ghat_inf((0, 0, 0)):.7f} (gamma_3 = 0.2527310)")
    out.append("r   eps1eps2   single: J E_r/(g1g2)  4 pi r ghat_inf(r)   cells: J E_r/(g1g2)  pi r sum ghat_inf"
               "   torus check: ghat_L(r)-ghat_L(8) for L=16, 32, 64 vs ghat_inf(r)-ghat_inf(8)")
    gl = {L: ghat(L) for L in (16, 32, 64)}
    g8 = ghat_inf((8, 0, 0))
    for r in range(2, 9):
        e12 = (-1) ** r
        gs = ghat_inf((r, 0, 0))
        gc = 2 * gs + ghat_inf((r, 1, 0)) + ghat_inf((r, -1, 0))
        tor = "  ".join(f"{gl[L][r, 0, 0] - gl[L][8, 0, 0]:.6f}" for L in (16, 32, 64))
        out.append(f"{r:2d}   {e12:+d}        {-e12 * gs: .6f}            {4 * np.pi * r * gs:.4f}"
                   f"             {-e12 * gc: .6f}         {np.pi * r * gc:.4f}            {tor}   {gs - g8:.6f}")
    kap = np.sqrt(2 * Z) / (32 * np.pi ** 3)
    lam = Z ** 1.5 / (16 * np.sqrt(2) * np.pi ** 3)
    cA = {1: cont_link([1, 0, 0], [1, 0, 0], 1), -1: cont_link([1, 0, 0], [1, 0, 0], -1)}
    cB = {1: cont_link([0, 1, 0], [0, 1, 0], 1), -1: cont_link([0, 1, 0], [0, 1, 0], -1)}
    pre = np.sqrt(3) / (8 * np.pi ** 3)
    out.append("\n## Continuum coefficients")
    out.append(f"along n, single:  J S E/(g1 g2) = -eps1 eps2 kappa_par / r^3, kappa_par = sqrt(2z)/(32 pi^3) = {kap:.7f}")
    out.append(f"held spin (defect), r >> l_b: S E/(J sig1 sig2) = +eps1 eps2 lambda / r^5, lambda = {lam:.7f}")
    out.append(f"changed links, J E/(d1 d2 S) * r^7: parallel to r: eps=+1 {cA[1]:.7f} (formula {-pre * (43/6 + 2.5):.7f}),"
               f" eps=-1 {cA[-1]:.7f} (formula {-pre * (43/6 - 2.5):.7f})")
    out.append(f"                                     perpendicular: eps=+1 {cB[1]:.7f} (formula {-pre * (4/3 - 5/12):.7f}),"
               f" eps=-1 {cB[-1]:.7f} (formula {-pre * (4/3 + 5/12):.7f})")
    out.append("\n## (2) Quadratic sources, lattice (zero modes left out); ratio = lattice / continuum")
    out.append("columns: r, eps1eps2, along single [J S E/(g1g2), ratio], along cell [.., ratio vs 4x], "
               "defect [S E/(J s1 s2), ratio], link par [J E/(d1d2S), ratio], link perp [.., ratio]")
    rs = list(range(2, 13))
    ratios = {}
    for L in (32, 64, 128):
        configs = []
        for r in rs:
            x2 = (r, 0, 0)
            configs += [(pert("along", (0, 0, 0)), pert("along", x2)),
                        (pert("along_cell", (0, 0, 0)), pert("along_cell", x2)),
                        (pert("defect", (0, 0, 0)), pert("defect", x2)),
                        (pert("link", (0, 0, 0), (1, 0, 0)), pert("link", x2, (1, 0, 0))),
                        (pert("link", (0, 0, 0), (0, 1, 0)), pert("link", x2, (0, 1, 0)))]
        res = mutual_quadratic(L, configs, nodes=300).reshape(len(rs), 5)
        out.append(f"L = {L}")
        ratios[L] = np.zeros_like(res)
        for i, r in enumerate(rs):
            e = (-1) ** r
            p = [-e * kap / r ** 3, -4 * e * kap / r ** 3, e * lam / r ** 5, cA[e] / r ** 7, cB[e] / r ** 7]
            ratios[L][i] = res[i] / np.array(p)
            row = "  ".join(f"{res[i, j]: .3e} {res[i, j] / p[j]:6.3f}" for j in range(5))
            out.append(f"{r:2d} {e:+d}  {row}")
    out.append("ratio extrapolated to L -> infinity: Aitken from L = 32, 64, 128 (geometric finite-size error);"
               " the L = 128 value where the change from 64 to 128 is below 1e-3 or not geometric")
    for i, r in enumerate(rs):
        x1, x2, x3 = ratios[32][i], ratios[64][i], ratios[128][i]
        d1, d2 = x2 - x1, x3 - x2
        geo = (np.abs(d2) > 1e-3) & (d1 * d2 > 0) & (np.abs(d2) < np.abs(d1))
        ex = np.where(geo, x3 + d2 / np.where(geo, d1 / np.where(geo, d2, 1.0) - 1, 1.0), x3)
        out.append(f"{r:2d}  " + "  ".join(f"{v:6.3f}" for v in ex))
    (OUT / "spinwave_mutual.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
