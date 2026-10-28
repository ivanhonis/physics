"""Check (i) of 08-ilang-propagation/02-grip-weight (v3).

For (G2) grips F(q) = F0 + F1 q + F2 q^2 on rings and cubic tori, compute the
weighing ratios rho_mark and rho_bond,i (one per body, reference: a single body with
the grip of body i at the midpoint) from the exact lowest eigenvalue of the
uncompressed quadratic total contract
    E = sum_i s mu_i F0_i + 1/2 Tr sqrt(K') - 1/2 J^T K'^{-1} J ,
obtained by numerical linear algebra (eigvalsh, solve) with finite differences in
s (grip scaling) and g_s (source strength), and compare them with the formulas
of the derivation: (2.15) exact mark ratio, (2.16) exact bond ratio for two grips
(unfactored form, valid whenever U != 0), (2.14) order-mu^2 ratios, (2.18) leading order,
(2.19) square-grip deviation. On every graph one pair of different grips is tuned to
U_cl = 0 (v^T M v = 0), where only the unfactored (2.16) applies.
A second block follows the ratios as m_h -> 0 on a ring of fixed size, (2.24).
Outputs: output/g2_mark.csv, output/g2_bond.csv, output/g2_mh_limit.csv,
output/g2_summary.json.
"""
import csv
import itertools
import json
import os
import threading
import time
from pathlib import Path

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")  # small dense matrices: one thread is fastest
import numpy as np
from scipy import integrate

WALL_LIMIT_S = 1500
threading.Timer(WALL_LIMIT_S, lambda: os._exit(3)).start()
T0 = time.time()

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

KAPPA, MH = 1.0, 0.3
# Model D levels: M_k = m + 2 pi k/(N lambda0) with m = 0.5, N = 4, lambda0 = 2 pi
M_LEVEL = {0: 0.5, 1: 0.75}
GRIPS = {
    "square": (1.0, 0.6, 0.09),      # F0 (1 + 0.3 q)^2 : 4 F0 F2 = F1^2
    "generic": (1.0, 0.6, 0.15),     # 4 F0 F2 / F1^2 = 1.667
    "linear": (1.0, 0.6, 0.0),       # control
    "square_b02": (1.0, 0.4, 0.04),  # F0 (1 + 0.2 q)^2, used only in pairs
}
MARK_GRIPS = ["square", "generic", "linear"]
GRIP_PAIRS = [("square", "square"), ("generic", "generic"), ("linear", "linear"),
              ("square", "square_b02"), ("square", "generic")]
GRAPHS = [("ring", 1, 40), ("ring", 1, 80), ("cubic", 3, 8), ("cubic", 3, 12)]
LEVELS = [(0, +1), (0, -1), (1, +1), (1, -1)]
PAIRS = [((0, +1), (0, +1)), ((1, -1), (1, -1)), ((0, +1), (1, +1)), ((0, +1), (0, -1))]
MH_LIST = [0.3, 0.1, 0.03, 0.01, 0.003, 0.001]


class Graph:
    def __init__(self, D, L, mh=MH):
        self.D, self.L, self.mh = D, L, mh
        self.coords = np.array(list(itertools.product(range(L), repeat=D)))
        self.N = len(self.coords)
        idx = {tuple(c): i for i, c in enumerate(self.coords)}
        self.idx = idx
        K = np.eye(self.N) * (mh**2 + 2 * D * KAPPA)
        for i, c in enumerate(self.coords):
            for d in range(D):
                for sgn in (+1, -1):
                    c2 = c.copy()
                    c2[d] = (c2[d] + sgn) % L
                    K[i, idx[tuple(c2)]] -= KAPPA
        self.K = K
        ks = 2 * np.pi * self.coords / L  # momenta
        self.ks = ks
        self.w2 = mh**2 + KAPPA * np.sum(4 * np.sin(ks / 2) ** 2, axis=1)
        self.w = np.sqrt(self.w2)
        self.trK = 0.5 * np.sum(self.w)

    def site(self, c):
        return self.idx[tuple(np.mod(c, self.L))]

    def G(self, r):  # Green function K^{-1} at separation r (Fourier sum)
        return np.mean(np.cos(self.ks @ np.asarray(r, float)) / self.w2)

    def w0(self):
        return np.mean(1 / (2 * self.w))

    def J2(self, r):  # int_0^inf c_r(tau)^2 dtau, c_r(tau) = (1/2N) sum_k cos(k.r) e^{-w_k tau}/w_k
        a = np.cos(self.ks @ np.asarray(r, float)) / self.w
        W = self.w[:, None] + self.w[None, :]
        return float(np.sum((a[:, None] * a[None, :]) / W) / (4 * self.N**2))

    def g(self, nu, r=None):
        if r is None:
            return np.mean(1 / (self.w2 + nu**2))
        return np.mean(np.cos(self.ks @ np.asarray(r, float)) / (self.w2 + nu**2))


def energy(gr, bodies, s, gsrc, src):
    """Exact lowest eigenvalue of 1/2 p^2 + 1/2 q K q + sum_i s mu_i F_i(q_{x_i}) + g q_src."""
    Kp = gr.K.copy()
    J = np.zeros(gr.N)
    c = 0.0
    for (x, mu, F) in bodies:
        F0, F1, F2 = F
        Kp[x, x] += 2 * s * mu * F2
        J[x] += s * mu * F1
        c += s * mu * F0
    J[src] += gsrc
    ev = np.linalg.eigvalsh(Kp)
    if ev.min() <= 0:
        raise ValueError("no lowest eigenvector: K' not positive")
    return c + 0.5 * np.sum(np.sqrt(ev)) - 0.5 * J @ np.linalg.solve(Kp, J)


def dweight(gr, bodies, s, src):
    # linear coefficient in g of the exact eigenvalue: E is exactly quadratic in g and the
    # trace term is g-independent (same K'), so [E(g) - E(-g)]/(2g) = -J_b^T K'^{-1} e_src exactly
    Kp = gr.K.copy()
    J = np.zeros(gr.N)
    for (x, mu, F) in bodies:
        Kp[x, x] += 2 * s * mu * F[2]
        J[x] += s * mu * F[1]
    e = np.zeros(gr.N)
    e[src] = 1.0
    return -J @ np.linalg.solve(Kp, e)


def dds(f, h=1e-2):
    return (8 * (f(h) - f(-h)) - (f(2 * h) - f(-2 * h))) / (12 * h)


def step(gr, mu, F):
    # s-step small against the scale 1/(2 |mu F2| G0) of the s-dependence
    return min(1e-2, 0.02 / (1 + 2 * abs(mu * F[2]) * gr.G(np.zeros(gr.D))))


def zeta_mark(gr, mu, F):
    F0, F1, F2 = F
    if F2 == 0:
        return 0.0
    G0, t = gr.G(np.zeros(gr.D)), 2 * mu * F2

    def chi(x):
        return (x - np.log1p(x)) / x**2 if abs(x) > 1e-6 else 0.5 - x / 3 + x**2 / 4

    def integrand(nu):
        g = gr.g(nu)
        return g**2 * (1 + t * G0) * chi(t * g)

    pts = [gr.mh, 10 * gr.mh] if gr.mh < 0.1 else None
    val, _ = integrate.quad(integrand, 0, 1.0, points=pts, epsabs=1e-14, epsrel=1e-11, limit=400)
    val2, _ = integrate.quad(integrand, 1.0, np.inf, epsabs=1e-14, epsrel=1e-11, limit=400)
    return 4 * F2**2 / (np.pi * G0) * (val + val2)


def zbond(gr, r, a1, a2):
    if a1 == 0 or a2 == 0:
        return 0.0

    def integrand(nu):
        g, gr_ = gr.g(nu), gr.g(nu, r)
        return np.log1p(-a1 * a2 * gr_**2 / ((1 + a1 * g) * (1 + a2 * g)))

    pts = [gr.mh, 10 * gr.mh] if gr.mh < 0.1 else None
    val, _ = integrate.quad(integrand, 0, 1.0, points=pts, epsabs=1e-15, epsrel=1e-11, limit=400)
    val2, _ = integrate.quad(integrand, 1.0, np.inf, epsabs=1e-15, epsrel=1e-11, limit=400)
    return (val + val2) / (2 * np.pi)


def bond_formulas(gr, rvec, Fs, mus, dphi, dphibar):
    """Exact (2.13)/(2.16), order-mu^2 (2.14) and leading-order (2.18) bond ratios, one per body."""
    G0, w0 = gr.G(np.zeros(gr.D)), gr.w0()
    Gr, J2r = gr.G(rvec), gr.J2(rvec)
    F0v = np.array([F[0] for F in Fs])
    F1v = np.array([F[1] for F in Fs])
    F2v = np.array([F[2] for F in Fs])
    mus = np.asarray(mus, float)
    a = 2 * mus * F2v
    v = mus * F1v
    Dv = 1 + a * G0
    Del = G0**2 - Gr**2
    B = np.array([[G0 + a[1] * Del, Gr], [Gr, G0 + a[0] * Del]]) / (Dv[0] * Dv[1] - a[0] * a[1] * Gr**2)
    Mm = B - np.diag(G0 / Dv)
    Ucl = -0.5 * v @ Mm @ v
    Zb = zbond(gr, rvec, a[0], a[1])
    wts = v * (Mm @ v) / (v @ Mm @ v) if abs(v @ Mm @ v) > 1e-12 else np.full(2, np.nan)
    eta = F2v / F1v
    meanF = F0v + F2v * w0
    S12 = F1v[0] * F1v[1] * Gr / 2 + 2 * F2v[0] * F2v[1] * J2r
    TT = Gr * (F2v[0] * F1v[1] * dphi[0] + F1v[0] * F2v[1] * dphi[1])
    dWb = -2 * np.sum(eta * v * (Mm @ v) * dphi)  # (2.13), per unit g_s
    out = dict(U_formula=Ucl + Zb, U_cl=Ucl, Z_b=Zb, w1=wts[0])
    for i in (0, 1):
        # (2.16), unfactored: (<F_i>/F1_i) dW_bond / (U dphibar), U = U_cl + Z_b
        out[f"rho_exact_{i+1}"] = meanF[i] / F1v[i] * dWb / ((Ucl + Zb) * dphibar)
        out[f"rho_mu2_{i+1}"] = meanF[i] / F1v[i] * TT / (S12 * dphibar)
        out[f"rho_lead_{i+1}"] = 2 * F0v[i] / F1v[i] * (eta @ dphi) / dphibar
    return out


def main():
    mark_rows, bond_rows, graph_info, ucl0_rows = [], [], [], []
    for (name, D, L) in GRAPHS:
        gr = Graph(D, L)
        zero = np.zeros(D, int)
        e1 = np.eye(D, dtype=int)[0]
        e2 = np.eye(D, dtype=int)[1] if D > 1 else e1
        src = gr.site(zero)
        anti = np.full(D, L // 2)
        G0, w0 = gr.G(zero), gr.w0()
        J20 = gr.J2(zero)
        graph_info.append(dict(graph=name, L=L, N=gr.N, G0=G0, w0=w0, J2_0=J20,
                               J2_over_G0=J20 / G0, ell=np.sqrt(KAPPA) / MH))
        dists = [1, 5, 10] if (D == 1 and L == 40) else [1, 5, 20] if D == 1 else [1, 2, 3] if L == 8 else [1, 3, 5]
        phi = lambda c: -gr.G(np.asarray(c))  # made field per unit g_s
        # ---- marks
        for gname in MARK_GRIPS:
            F = GRIPS[gname]
            F0, F1, F2 = F
            for (k, sg) in LEVELS:
                mu = sg * M_LEVEL[k]
                xb0 = gr.site(anti)
                cost = lambda s: energy(gr, [(xb0, mu, F)], s, 0, src) - gr.trK
                C1 = dds(cost)
                Cmark = cost(1.0) - C1
                meanF = F0 + F2 * w0
                zeta = zeta_mark(gr, mu, F)
                rho_exact = 4 * F2 * meanF / (F1**2 + zeta)
                rho_mu2 = 4 * F2 * meanF / (F1**2 + 4 * F2**2 * J20 / G0)
                rho_lead = 4 * F0 * F2 / F1**2
                Wref = {}
                for xc in [anti] + [d * e1 for d in dists]:
                    x = gr.site(xc)
                    W = dweight(gr, [(x, mu, F)], 1.0, src)
                    W1 = dds(lambda s: dweight(gr, [(x, mu, F)], s, src))
                    Wref[tuple(xc)] = (W, W1)
                Wa, W1a = Wref[tuple(anti)]
                for d in dists:
                    W, W1 = Wref[tuple(d * e1)]
                    dWmark, dW1 = (W - W1) - (Wa - W1a), W1 - W1a
                    rho_num = (dWmark / Cmark) / (dW1 / C1)
                    mark_rows.append(dict(graph=name, L=L, grip=gname, k=k, sigma=sg, d=d,
                                          C1=C1, C1_formula=mu * meanF, Cmark=Cmark,
                                          rho_num=rho_num, rho_exact=rho_exact,
                                          rho_mu2=rho_mu2, rho_lead=rho_lead,
                                          dev_exact=rho_num - rho_exact))
        # ---- bonds: single-body references with the grip of body i (level independent)
        mu_r = M_LEVEL[0]
        x_ref = gr.site(anti)
        C1r, W1_cache = {}, {}

        def W1_at(gname, xs):
            if (gname, xs) not in W1_cache:
                W1_cache[(gname, xs)] = dds(lambda s: dweight(gr, [(xs, mu_r, GRIPS[gname])], s, src))
            return W1_cache[(gname, xs)]
        for gname in GRIPS:
            C1r[gname] = dds(lambda s: energy(gr, [(x_ref, mu_r, GRIPS[gname])], s, 0, src) - gr.trK)
        mid_d = [4, 8, 12] if D == 1 else dists
        seps = [2, 4]
        cache1 = {}

        def single(kind, x, mu, gname):  # cached single-body energy ("E") or weight ("W") at s = 1
            key = (kind, x, mu, gname)
            if key not in cache1:
                b = [(x, mu, GRIPS[gname])]
                cache1[key] = energy(gr, b, 1.0, 0, src) if kind == "E" else dweight(gr, b, 1.0, src)
            return cache1[key]
        for (ga, gb) in GRIP_PAIRS:
            Fa, Fb = GRIPS[ga], GRIPS[gb]
            for (p1, p2) in PAIRS:
                mu1, mu2 = p1[1] * M_LEVEL[p1[0]], p2[1] * M_LEVEL[p2[0]]
                for r in seps:
                    rvec = r * e2

                    def pair_sites(mc):
                        return gr.site(np.asarray(mc) - rvec // 2), gr.site(np.asarray(mc) + rvec // 2)
                    xa, xbb = pair_sites(anti)
                    try:
                        Ep = energy(gr, [(xa, mu1, Fa), (xbb, mu2, Fb)], 1.0, 0, src)
                    except ValueError:
                        continue
                    E1 = single("E", xa, mu1, ga)
                    E2 = single("E", xbb, mu2, gb)
                    U = Ep - E1 - E2 + gr.trK

                    def Wbond(mc):
                        x1, x2 = pair_sites(mc)
                        return (dweight(gr, [(x1, mu1, Fa), (x2, mu2, Fb)], 1.0, src)
                                - single("W", x1, mu1, ga) - single("W", x2, mu2, gb))
                    Wb_ref = Wbond(anti)
                    for d in mid_d:
                        mc = d * e1
                        x1c, x2c = np.asarray(mc) - rvec // 2, np.asarray(mc) + rvec // 2
                        if gr.site(x1c) == src or gr.site(x2c) == src:
                            continue
                        Wb = Wbond(mc)
                        xm = gr.site(mc)
                        a1c, a2c = anti - rvec // 2, anti + rvec // 2
                        dphi = np.array([phi(x1c) - phi(a1c), phi(x2c) - phi(a2c)])
                        dphibar = phi(mc) - phi(anti)
                        mf = dphi.sum() / (2 * dphibar)
                        row = dict(graph=name, L=L, grips=f"{ga}+{gb}", pair=f"{p1}{p2}", r=r, d=d,
                                   U=U, mf=mf, J2r_over_Gr=gr.J2(rvec) / gr.G(rvec))
                        for i, gname in enumerate((ga, gb)):
                            ref = (W1_at(gname, xm) - W1_at(gname, x_ref)) / C1r[gname]
                            row[f"rho_num_{i+1}"] = ((Wb - Wb_ref) / U) / ref
                        row.update(bond_formulas(gr, rvec, (Fa, Fb), (mu1, mu2), dphi, dphibar))
                        for i in (1, 2):
                            row[f"dev_exact_{i}"] = row[f"rho_num_{i}"] - row[f"rho_exact_{i}"]
                            row[f"dev_mu2_{i}"] = row[f"rho_num_{i}"] - row[f"rho_mu2_{i}"]
                        bond_rows.append(row)
        # ---- (I5) different grips tuned to U_cl = 0: square grip + (F0, t F1, F2), labels (0,+)(0,+),
        # separation 2; t is the smaller root of v^T M v = 0 (M from the two-site block of K'^{-1})
        mu_t, rvec = M_LEVEL[0], 2 * e2
        Fa = GRIPS["square"]
        at, Gr2 = 2 * mu_t * Fa[2], gr.G(rvec)
        Dt = 1 + at * G0
        Del2 = Dt**2 - at**2 * Gr2**2
        M11, M12 = -at * Gr2**2 / (Dt * Del2), Gr2 / Del2
        t_root = (M12 - np.sqrt(M12**2 - M11**2)) / (-M11)
        Fb = (Fa[0], t_root * Fa[1], Fa[2])
        xa, xbb = gr.site(anti - rvec // 2), gr.site(anti + rvec // 2)
        Ep = energy(gr, [(xa, mu_t, Fa), (xbb, mu_t, Fb)], 1.0, 0, src)
        U = Ep - energy(gr, [(xa, mu_t, Fa)], 1.0, 0, src) - energy(gr, [(xbb, mu_t, Fb)], 1.0, 0, src) + gr.trK

        def Wbond_t(mc):
            x1, x2 = gr.site(np.asarray(mc) - rvec // 2), gr.site(np.asarray(mc) + rvec // 2)
            return (dweight(gr, [(x1, mu_t, Fa), (x2, mu_t, Fb)], 1.0, src)
                    - dweight(gr, [(x1, mu_t, Fa)], 1.0, src) - dweight(gr, [(x2, mu_t, Fb)], 1.0, src))
        Wt_ref = Wbond_t(anti)
        C1t = [dds(lambda s: energy(gr, [(x_ref, mu_t, F)], s, 0, src) - gr.trK) for F in (Fa, Fb)]
        for d in mid_d:
            mc = d * e1
            x1c, x2c = mc - rvec // 2, mc + rvec // 2
            if gr.site(x1c) == src or gr.site(x2c) == src:
                continue
            xm = gr.site(mc)
            dphi = np.array([phi(x1c) - phi(anti - rvec // 2), phi(x2c) - phi(anti + rvec // 2)])
            dphibar = phi(mc) - phi(anti)
            row = dict(graph=name, L=L, grips="square+tuned", F1_tuned=Fb[1], pair="(0, 1)(0, 1)", r=2, d=d,
                       U=U, mf=dphi.sum() / (2 * dphibar))
            Wb_t = Wbond_t(mc)
            for i, F in enumerate((Fa, Fb)):
                ref = (dds(lambda s: dweight(gr, [(xm, mu_t, F)], s, src))
                       - dds(lambda s: dweight(gr, [(x_ref, mu_t, F)], s, src))) / C1t[i]
                row[f"rho_num_{i+1}"] = ((Wb_t - Wt_ref) / U) / ref
            row.update(bond_formulas(gr, rvec, (Fa, Fb), (mu_t, mu_t), dphi, dphibar))
            for i in (1, 2):
                row[f"dev_exact_{i}"] = row[f"rho_num_{i}"] - row[f"rho_exact_{i}"]
            ucl0_rows.append(row)
        print(f"{name} L={L} done at {time.time() - T0:.1f}s", flush=True)

    # ---- m_h -> 0 at fixed L (ring L = 40), sectors with mu F2 > 0
    mh_rows = []
    for mh in MH_LIST:
        gr = Graph(1, 40, mh)
        src, anti, xd = gr.site([0]), 20, gr.site([5])
        G0, w0 = gr.G([0]), gr.w0()
        for gname in ("generic", "square", "linear"):
            F = GRIPS[gname]
            for mu in (+0.5, +0.75):
                h = step(gr, mu, F)
                cost = lambda s: energy(gr, [(anti, mu, F)], s, 0, src) - gr.trK
                C1 = dds(cost, h)
                cst = cost(1.0)
                Cmark = cst - C1
                W = {x: dweight(gr, [(x, mu, F)], 1.0, src) for x in (xd, anti)}
                W1 = {x: dds(lambda s: dweight(gr, [(x, mu, F)], s, src), h) for x in (xd, anti)}
                dW1 = W1[xd] - W1[anti]
                dWm = (W[xd] - W1[xd]) - (W[anti] - W1[anti])
                rho = (dWm / Cmark) / (dW1 / C1)
                F0, F1, F2 = F
                rho_f = 4 * F2 * (F0 + F2 * w0) / (F1**2 + zeta_mark(gr, mu, F))
                mh_rows.append(dict(kind="mark", m_h=mh, G0=G0, w0=w0, grips=gname, mu=mu, cost=cst,
                                    C1=C1, C1_formula=mu * (F0 + F2 * w0), Cmark=Cmark, rho_num=rho,
                                    rho_formula=rho_f,
                                    exists_mu_minus075=bool(1 - 2 * 0.75 * F2 * G0 > 0)))
        for (ga, gb, mu1, mu2) in (("generic", "generic", 0.5, 0.5), ("generic", "generic", 0.5, 0.75),
                                   ("square", "generic", 0.5, 0.5)):
            Fa, Fb = GRIPS[ga], GRIPS[gb]
            x1r, x2r, x1, x2 = anti - 1, anti + 1, gr.site([7]), gr.site([9])
            U = (energy(gr, [(x1r, mu1, Fa), (x2r, mu2, Fb)], 1.0, 0, src)
                 - energy(gr, [(x1r, mu1, Fa)], 1.0, 0, src) - energy(gr, [(x2r, mu2, Fb)], 1.0, 0, src) + gr.trK)

            def Wb(y1, y2):
                return (dweight(gr, [(y1, mu1, Fa), (y2, mu2, Fb)], 1.0, src)
                        - dweight(gr, [(y1, mu1, Fa)], 1.0, src) - dweight(gr, [(y2, mu2, Fb)], 1.0, src))
            dWb = Wb(x1, x2) - Wb(x1r, x2r)
            row = dict(kind="bond", m_h=mh, G0=G0, w0=w0, grips=f"{ga}+{gb}", mu=f"{mu1},{mu2}", U=U,
                       dWbond_over_U=dWb / U)
            for i, F in enumerate((Fa, Fb)):
                h = step(gr, 0.5, F)
                C1 = dds(lambda s: energy(gr, [(anti, 0.5, F)], s, 0, src) - gr.trK, h)
                xm = gr.site([8])
                ref = (dds(lambda s: dweight(gr, [(xm, 0.5, F)], s, src), h)
                       - dds(lambda s: dweight(gr, [(anti, 0.5, F)], s, src), h)) / C1
                row[f"rho_num_{i+1}"] = (dWb / U) / ref
            mh_rows.append(row)
    print(f"m_h block done at {time.time() - T0:.1f}s", flush=True)

    for fname, rows in (("g2_mark.csv", mark_rows), ("g2_bond.csv", bond_rows), ("g2_mh_limit.csv", mh_rows)):
        keys = []
        for row in rows:
            keys += [k for k in row if k not in keys]
        with open(OUT / fname, "w", newline="") as fh:
            wr = csv.DictWriter(fh, fieldnames=keys)
            wr.writeheader()
            for row in rows:
                wr.writerow({k: (f"{v:.12g}" if isinstance(v, float) else v) for k, v in row.items()})

    def mx(rows, keys, cond=lambda r: True):
        vals = [abs(r[k]) for r in rows if cond(r) for k in keys if k in r]
        return max(vals) if vals else None

    def w0_of(r):
        return next(g["w0"] for g in graph_info if g["graph"] == r["graph"] and g["L"] == r["L"])

    summary = dict(
        parameters=dict(kappa_h=KAPPA, m_h=MH, M_levels=M_LEVEL, grips=GRIPS, grip_pairs=GRIP_PAIRS),
        graphs=graph_info,
        max_abs_C1_minus_formula=max(abs(r["C1"] - r["C1_formula"]) for r in mark_rows),
        max_abs_rho_mark_num_minus_exact=mx(mark_rows, ["dev_exact"]),
        max_abs_bond_U_minus_formula=max(abs(r["U"] - r["U_formula"]) for r in bond_rows),
        max_abs_rho_bond_num_minus_exact=mx(bond_rows, ["dev_exact_1", "dev_exact_2"]),
        max_abs_rho_bond_num_minus_mu2_common=mx(bond_rows, ["dev_mu2_1"],
                                                 lambda r: r["grips"].split("+")[0] == r["grips"].split("+")[1]),
        max_abs_rho_bond_num_minus_mu2_mixed=mx(bond_rows, ["dev_mu2_1", "dev_mu2_2"],
                                                lambda r: r["grips"].split("+")[0] != r["grips"].split("+")[1]),
        rho_mark_square_by_level={f"{r['graph']}{r['L']} k={r['k']} s={r['sigma']}": r["rho_num"]
                                  for r in mark_rows if r["grip"] == "square" and r["d"] == 1},
        rho_mark_generic_by_level={f"{r['graph']}{r['L']} k={r['k']} s={r['sigma']}": r["rho_num"]
                                   for r in mark_rows if r["grip"] == "generic" and r["d"] == 1},
        square_deviation_prediction={f"{g['graph']}{g['L']}": 0.09 * (g["w0"] - g["J2_over_G0"]) for g in graph_info},
        square_bond_deviation={f"{r['graph']}{r['L']} r={r['r']} d={r['d']}":
                               dict(rho_over_mf_minus_1=r["rho_num_1"] / r["mf"] - 1,
                                    prediction_2_19=0.09 * (w0_of(r) - r["J2r_over_Gr"]))
                               for r in bond_rows if r["grips"] == "square+square" and r["pair"] == "(0, 1)(0, 1)"},
        mixed_square_pair_equal_labels={f"{r['graph']}{r['L']} r={r['r']} d={r['d']}":
                                        dict(rho_num_1=r["rho_num_1"], rho_num_2=r["rho_num_2"],
                                             lead_1=r["rho_lead_1"], lead_2=r["rho_lead_2"], mf=r["mf"])
                                        for r in bond_rows if r["grips"] == "square+square_b02"
                                        and r["pair"] == "(0, 1)(0, 1)"},
        max_abs_rho_linear=max([abs(r["rho_num"]) for r in mark_rows if r["grip"] == "linear"]
                               + [abs(r[k]) for r in bond_rows if r["grips"] == "linear+linear"
                                  for k in ("rho_num_1", "rho_num_2")]),
        max_distance_spread_rho_mark=max(
            max(r["rho_num"] for r in mark_rows if (r["graph"], r["L"], r["grip"], r["k"], r["sigma"]) == key)
            - min(r["rho_num"] for r in mark_rows if (r["graph"], r["L"], r["grip"], r["k"], r["sigma"]) == key)
            for key in {(r["graph"], r["L"], r["grip"], r["k"], r["sigma"]) for r in mark_rows}),
        ucl_zero_pairs=[{k: r[k] for k in ("graph", "L", "F1_tuned", "d", "U", "U_cl", "Z_b", "U_formula",
                                           "rho_num_1", "rho_exact_1", "rho_num_2", "rho_exact_2",
                                           "dev_exact_1", "dev_exact_2")} for r in ucl0_rows],
        max_abs_ucl_zero_rho_num_minus_exact=mx(ucl0_rows, ["dev_exact_1", "dev_exact_2"]),
        max_abs_ucl_zero_U_minus_Zb=max(abs(r["U"] - r["Z_b"]) for r in ucl0_rows),
        mh_limit_marks=[dict(m_h=r["m_h"], grip=r["grips"], mu=r["mu"], rho_num=r["rho_num"],
                             rho_formula=r["rho_formula"], cost=r["cost"], C1=r["C1"],
                             exists_mu_minus075=r["exists_mu_minus075"])
                        for r in mh_rows if r["kind"] == "mark"],
        mh_limit_bonds=[dict(m_h=r["m_h"], grips=r["grips"], mu=r["mu"], U=r["U"],
                             rho_num_1=r["rho_num_1"], rho_num_2=r["rho_num_2"])
                        for r in mh_rows if r["kind"] == "bond"],
        runtime_s=time.time() - T0,
    )
    with open(OUT / "g2_summary.json", "w") as fh:
        json.dump(summary, fh, indent=1)
    print(json.dumps({k: v for k, v in summary.items() if not k.startswith("mh_")}, indent=1)[:6000])
    os._exit(0)


if __name__ == "__main__":
    main()
