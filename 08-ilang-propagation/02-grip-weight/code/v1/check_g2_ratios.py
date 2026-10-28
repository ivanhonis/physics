"""Check (i) of 08-ilang-propagation/02-grip-weight.

For (G2) grips F(q) = F0 + F1 q + F2 q^2 on rings and cubic tori, compute the
weighing ratios rho_mark and rho_bond from the exact lowest eigenvalue of the
uncompressed quadratic total contract
    E = sum_i s mu_i F0 + 1/2 Tr sqrt(K') - 1/2 J^T K'^{-1} J ,
obtained by numerical linear algebra (eigvalsh, solve) with finite differences in
s (grip scaling) and g_s (source strength), and compare them with the formulas
of the derivation: (2.15) exact G2 mark ratio, (2.16) exact G2 bond ratio,
(2.14) order-mu^2 ratio, (2.17)-(2.18) smooth-grip limit, (2.19) square-grip deviation.
Outputs: output/g2_mark.csv, output/g2_bond.csv, output/g2_summary.json.
"""
import itertools
import json
import os
import threading
import time
from pathlib import Path

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
    "square": (1.0, 0.6, 0.09),   # F0 (1 + 0.3 q)^2 : 4 F0 F2 = F1^2
    "generic": (1.0, 0.6, 0.15),  # 4 F0 F2 / F1^2 = 1.667
    "linear": (1.0, 0.6, 0.0),    # control
}
GRAPHS = [("ring", 1, 40), ("ring", 1, 80), ("cubic", 3, 8), ("cubic", 3, 12)]
LEVELS = [(0, +1), (0, -1), (1, +1), (1, -1)]
PAIRS = [((0, +1), (0, +1)), ((1, -1), (1, -1)), ((0, +1), (1, +1)), ((0, +1), (0, -1))]


class Graph:
    def __init__(self, D, L):
        self.D, self.L = D, L
        self.coords = np.array(list(itertools.product(range(L), repeat=D)))
        self.N = len(self.coords)
        idx = {tuple(c): i for i, c in enumerate(self.coords)}
        self.idx = idx
        K = np.eye(self.N) * (MH**2 + 2 * D * KAPPA)
        for i, c in enumerate(self.coords):
            for d in range(D):
                for sgn in (+1, -1):
                    c2 = c.copy()
                    c2[d] = (c2[d] + sgn) % L
                    K[i, idx[tuple(c2)]] -= KAPPA
        self.K = K
        ks = 2 * np.pi * self.coords / L  # momenta
        self.ks = ks
        self.w2 = MH**2 + KAPPA * np.sum(4 * np.sin(ks / 2) ** 2, axis=1)
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
    """Exact lowest eigenvalue of 1/2 p^2 + 1/2 q K q + sum_i s mu_i F(q_{x_i}) + g q_src."""
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


def classical(gr, bodies, s, gsrc, src):
    """g-odd part only needs the classical term; used for central differences in g."""
    Kp = gr.K.copy()
    J = np.zeros(gr.N)
    for (x, mu, F) in bodies:
        Kp[x, x] += 2 * s * mu * F[2]
        J[x] += s * mu * F[1]
    J[src] += gsrc
    return -0.5 * J @ np.linalg.solve(Kp, J)


def dweight(gr, bodies, s, src):
    # linear coefficient in g of the exact eigenvalue: E is exactly quadratic in g and the
    # trace term is g-independent (same K'), so the central difference with g = 1 is exact
    return (classical(gr, bodies, s, 1.0, src) - classical(gr, bodies, s, -1.0, src)) / 2


def dds(f, h=1e-2):
    return (8 * (f(h) - f(-h)) - (f(2 * h) - f(-2 * h))) / (12 * h)


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

    val, _ = integrate.quad(integrand, 0, np.inf, epsabs=1e-14, epsrel=1e-11, limit=400)
    return 4 * F2**2 / (np.pi * G0) * val


def zbond(gr, r, a1, a2):
    if a1 == 0 or a2 == 0:
        return 0.0

    def integrand(nu):
        g, gr_ = gr.g(nu), gr.g(nu, r)
        return np.log1p(-a1 * a2 * gr_**2 / ((1 + a1 * g) * (1 + a2 * g)))

    val, _ = integrate.quad(integrand, 0, np.inf, epsabs=1e-15, epsrel=1e-11, limit=400)
    return val / (2 * np.pi)


def main():
    mark_rows, bond_rows, graph_info = [], [], []
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
        for gname, F in GRIPS.items():
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
            # bonds
            Fd = F
            mu_r = M_LEVEL[0]
            x_ref = gr.site(anti)
            C1r = dds(lambda s: energy(gr, [(x_ref, mu_r, Fd)], s, 0, src) - gr.trK)
            W1_cache = {}

            def W1_at(xs):
                if xs not in W1_cache:
                    W1_cache[xs] = dds(lambda s: dweight(gr, [(xs, mu_r, Fd)], s, src))
                return W1_cache[xs]
            W1_ref = W1_at(x_ref)
            mid_d = [4, 8, 12] if D == 1 else dists
            seps = [2, 4]
            for (p1, p2) in PAIRS:
                mu1, mu2 = p1[1] * M_LEVEL[p1[0]], p2[1] * M_LEVEL[p2[0]]
                for r in seps:
                    rvec = r * e2
                    def pair_sites(mc):
                        return gr.site(np.asarray(mc) - rvec // 2), gr.site(np.asarray(mc) + rvec // 2)
                    # bond profile U = E_pair - E_1 - E_2 + E_0 (no source), at s = 1
                    xa, xbb = pair_sites(anti)
                    try:
                        Ep = energy(gr, [(xa, mu1, Fd), (xbb, mu2, Fd)], 1.0, 0, src)
                    except ValueError:
                        continue
                    E1 = energy(gr, [(xa, mu1, Fd)], 1.0, 0, src)
                    E2 = energy(gr, [(xbb, mu2, Fd)], 1.0, 0, src)
                    U = Ep - E1 - E2 + gr.trK

                    def Wbond(mc):
                        x1, x2 = pair_sites(mc)
                        return (dweight(gr, [(x1, mu1, Fd), (x2, mu2, Fd)], 1.0, src)
                                - dweight(gr, [(x1, mu1, Fd)], 1.0, src)
                                - dweight(gr, [(x2, mu2, Fd)], 1.0, src))
                    Wb_ref = Wbond(anti)
                    # single-body C1 weight per unit at the midpoint (level independent): C1r, W1_at
                    # formulas
                    Gr, J2r = gr.G(rvec), gr.J2(rvec)
                    a1, a2 = 2 * mu1 * F2, 2 * mu2 * F2
                    v = np.array([mu1 * F1, mu2 * F1])
                    D1, D2 = 1 + a1 * G0, 1 + a2 * G0
                    Del = G0**2 - Gr**2
                    B = np.array([[G0 + a2 * Del, Gr], [Gr, G0 + a1 * Del]]) / (D1 * D2 - a1 * a2 * Gr**2)
                    Mm = B - np.diag([G0 / D1, G0 / D2])
                    Ucl = -0.5 * v @ Mm @ v
                    Zb = zbond(gr, rvec, a1, a2)
                    wts = v * (Mm @ v) / (v @ Mm @ v)
                    meanF = F0 + F2 * w0
                    for d in mid_d:
                        mc = d * e1
                        x1c, x2c = np.asarray(mc) - rvec // 2, np.asarray(mc) + rvec // 2
                        if gr.site(x1c) == src or gr.site(x2c) == src:
                            continue
                        Wb = Wbond(mc)
                        xm = gr.site(mc)
                        W1m = W1_at(xm)
                        rho_num = ((Wb - Wb_ref) / U) / ((W1m - W1_ref) / C1r)
                        a1c, a2c = anti - rvec // 2, anti + rvec // 2
                        dphi = np.array([phi(x1c) - phi(a1c), phi(x2c) - phi(a2c)])
                        dphibar = phi(mc) - phi(anti)
                        mf = dphi.sum() / (2 * dphibar)
                        mw = (wts @ dphi) / dphibar
                        zb = F1**2 * Zb / Ucl if F2 != 0 else 0.0
                        rho_exact = 4 * F2 * meanF / (F1**2 + zb) * mw
                        rho_mu2 = 4 * F2 * meanF * Gr / (F1**2 * Gr + 4 * F2**2 * J2r) * mf
                        bond_rows.append(dict(graph=name, L=L, grip=gname, pair=f"{p1}{p2}", r=r, d=d,
                                              U=U, U_formula=Ucl + Zb, rho_num=rho_num,
                                              rho_exact=rho_exact, rho_mu2=rho_mu2,
                                              rho_lead_times_mf=4 * F0 * F2 / F1**2 * mf, mf=mf,
                                              J2r_over_Gr=J2r / Gr, dev_exact=rho_num - rho_exact,
                                              dev_mu2=rho_num - rho_mu2))
        print(f"{name} L={L} done at {time.time() - T0:.1f}s", flush=True)

    import csv
    for fname, rows in (("g2_mark.csv", mark_rows), ("g2_bond.csv", bond_rows)):
        with open(OUT / fname, "w", newline="") as fh:
            wr = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            wr.writeheader()
            for row in rows:
                wr.writerow({k: (f"{v:.12g}" if isinstance(v, float) else v) for k, v in row.items()})

    def mx(rows, key, cond=lambda r: True):
        vals = [abs(r[key]) for r in rows if cond(r)]
        return max(vals) if vals else None

    summary = dict(
        parameters=dict(kappa_h=KAPPA, m_h=MH, M_levels=M_LEVEL, grips=GRIPS),
        graphs=graph_info,
        max_abs_C1_minus_formula=max(abs(r["C1"] - r["C1_formula"]) for r in mark_rows),
        max_abs_rho_mark_num_minus_exact=mx(mark_rows, "dev_exact"),
        max_abs_bond_U_minus_formula=max(abs(r["U"] - r["U_formula"]) for r in bond_rows),
        max_abs_rho_bond_num_minus_exact=mx(bond_rows, "dev_exact"),
        max_abs_rho_bond_num_minus_mu2=mx(bond_rows, "dev_mu2"),
        rho_mark_square_by_level={f"{r['graph']}{r['L']} k={r['k']} s={r['sigma']}": r["rho_num"]
                                  for r in mark_rows if r["grip"] == "square" and r["d"] == 1},
        rho_mark_generic_by_level={f"{r['graph']}{r['L']} k={r['k']} s={r['sigma']}": r["rho_num"]
                                   for r in mark_rows if r["grip"] == "generic" and r["d"] == 1},
        square_deviation_prediction={f"{g['graph']}{g['L']}": 0.09 * (g["w0"] - g["J2_over_G0"]) for g in graph_info},
        square_bond_deviation={f"{r['graph']}{r['L']} r={r['r']} d={r['d']}":
                               dict(rho_over_mf_minus_1=r["rho_num"] / r["mf"] - 1,
                                    prediction_2_19=0.09 * (next(g["w0"] for g in graph_info if g["graph"] == r["graph"] and g["L"] == r["L"]) - r["J2r_over_Gr"]))
                               for r in bond_rows if r["grip"] == "square" and r["pair"] == "(0, 1)(0, 1)"},
        max_abs_rho_linear=max(abs(r["rho_num"]) for r in mark_rows + bond_rows if r["grip"] == "linear"),
        max_distance_spread_rho_mark=max(
            max(r["rho_num"] for r in mark_rows if (r["graph"], r["L"], r["grip"], r["k"], r["sigma"]) == key)
            - min(r["rho_num"] for r in mark_rows if (r["graph"], r["L"], r["grip"], r["k"], r["sigma"]) == key)
            for key in {(r["graph"], r["L"], r["grip"], r["k"], r["sigma"]) for r in mark_rows}),
        runtime_s=time.time() - T0,
    )
    with open(OUT / "g2_summary.json", "w") as fh:
        json.dump(summary, fh, indent=1)
    print(json.dumps(summary, indent=1))
    os._exit(0)


if __name__ == "__main__":
    main()
