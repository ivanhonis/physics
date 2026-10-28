"""Check of item 3: formation of the long-range part of the made field of oscillator cells
(M -> infinity), A_x = B_x = q_x, source g_s q_0 switched on at lambda = 0.

Made field per unit g_s on a torus of side L (exact for the harmonic contract):
    da(x, lam) = -(1/L^D) sum_k cos(k.x) (1 - cos(W_k lam)) / W_k^2,  W_k^2 = m^2 + sum_i f(k_i),
    f(k) = a (1 - cos k) + b (1 - cos 2k),  c0^2 = a/2 + 2b.
By Poisson summation it is the infinite-lattice made field plus its images at x + n L (n != 0).
A finite-range harmonic lattice has no strictly compact propagation support, so the images are not
zero before the first image front, only exponentially small there (contour shift, Step 7(i)).
Image check (size refinement): Delta recomputed on a larger torus L_ref at every STRIDE-th lam of the
grid; the largest |Delta_L - Delta_Lref| on each window [0, lam_max] is reported.
Static mark: infinite lattice, da_st(x) = -G(x), G(x) = int_0^inf e^{-m^2 t} prod_i g_t(x_i) dt.
Criterion (4.11): D = 3 value ratio, D = 1 discrete-gradient ratio, |Delta| <= EPS for all
lam in [lam_f, lam_max] (finite-window value), lam_max = min(0.9 (L - rho - 1) / v_front, end of the
lambda grid) (before the image front); the same with lam_max / 2 (horizon check). Arrival (4.11):
first lam with |Delta + 1| >= ETA rho^(-1/2). fold_check: membership of the separable K in note (d).
"""
import json, os, sys, threading
from pathlib import Path
import numpy as np
from scipy import special, optimize
from scipy.integrate import simpson, cumulative_trapezoid

WALL_S = 3000
_t = threading.Timer(WALL_S, lambda: (sys.stderr.write("wall-clock limit\n"), os._exit(3)))
_t.daemon = True
_t.start()

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
EPS, ETA, A_ARR = 0.1, 0.1, 0.5          # formation accuracy; arrival threshold ETA rho^-A_ARR
STRIDE = 20                               # lam subsampling of the image check
KS = {"nn": (2.0, 0.0), "control": (14.0, -3.0)}   # (a, b); both have c0 = 1


def f1(k, a, b):
    return a * (1 - np.cos(k)) + b * (1 - np.cos(2 * k))


def speeds(a, b, m=0.0):
    k = np.linspace(1e-6, np.pi, 200001)
    fp = a * np.sin(k) + 2 * b * np.sin(2 * k)
    v_front = float(np.max(fp / (2 * np.sqrt(m**2 + f1(k, a, b)))))   # max d W / d k_1 (k_perp = 0)
    g = np.linspace(0, np.pi, 161)
    F, Fp = f1(g, a, b), a * np.sin(g) + 2 * b * np.sin(2 * g)
    num = Fp[:, None, None]**2 + Fp[None, :, None]**2 + Fp[None, None, :]**2
    den = 4 * (m**2 + F[:, None, None] + F[None, :, None] + F[None, None, :])
    den[0, 0, 0] = np.inf
    return {"c0": float(np.sqrt(a / 2 + 2 * b)), "v_front_axis": v_front,
            "v_slope_max_grad": float(max(np.sqrt(np.max(num / den)), v_front))}


def g_t(t, ns, a, b, alpha, nk=4000):
    kc = min(np.pi, np.sqrt(80.0 / (alpha * t)))
    k = np.linspace(0.0, kc, nk)
    w = np.full(nk, kc / (nk - 1)); w[0] *= 0.5; w[-1] *= 0.5
    return (np.cos(np.outer(ns, k)) @ (np.exp(-t * f1(k, a, b)) * w)) / np.pi


def static_axis(D, ns, a, b, m):
    """G(n e_1) on the infinite lattice for n in ns (Laplace representation)."""
    kg = np.linspace(1e-3, np.pi, 4000)
    alpha = float(np.min(f1(kg, a, b) / kg**2))
    ts = np.logspace(-5, np.log10(60.0 / m**2), 4000)
    ns = np.asarray(ns)
    vals = np.empty((len(ts), len(ns)))
    for i, t in enumerate(ts):
        g = g_t(t, np.append(ns, 0), a, b, alpha)
        vals[i] = np.exp(-m**2 * t) * g[:-1] * g[-1]**(D - 1) * t
    return simpson(vals, x=np.log(ts), axis=0)


def made_ring(L, rhos, a, b, m, lams):
    k = 2 * np.pi * np.arange(L) / L
    W = np.sqrt(m**2 + f1(k, a, b))
    C = np.cos(np.outer(rhos, k))
    out = np.empty((len(lams), len(rhos)))
    for i0 in range(0, len(lams), 200):
        lm = lams[i0:i0 + 200]
        S = 2 * np.sin(np.outer(lm, W) / 2)**2 / W**2
        out[i0:i0 + 200] = -(S @ C.T) / L
    return out


def made_torus3(L, rhos, a, b, m, lams):
    h = L // 2
    k = 2 * np.pi * np.arange(h + 1) / L
    wt = np.full(h + 1, 2.0); wt[0] = 1.0; wt[h] = 1.0
    F = f1(k, a, b)
    W2 = m**2 + F[:, None, None] + F[None, :, None] + F[None, None, :]
    W = np.sqrt(W2)
    W23 = wt[None, :, None] * wt[None, None, :] / W2
    C = wt[None, :] * np.cos(np.outer(rhos, k))
    out = np.empty((len(lams), len(rhos)))
    for i, lm in enumerate(lams):
        S = np.sum(2 * np.sin(W * (lm / 2))**2 * W23, axis=(1, 2))
        out[i] = -(C @ S) / L**3
    return out


def formation(lams, Delta, lam_max, eta):
    sel = lams <= lam_max
    lm, d = lams[sel], np.abs(Delta[sel])
    bad = np.nonzero(d > EPS)[0]
    lf = float(lm[bad[-1] + 1]) if len(bad) and bad[-1] + 1 < len(lm) else (float(lm[0]) if not len(bad) else None)
    arr = np.nonzero(np.abs(Delta[sel] + 1) >= eta)[0]
    return lf, (float(lm[arr[0]]) if len(arr) else None)


def fold_check(a, b, D, delta=0.05):
    """Note (d) for separable K (m -> 0): stationary points of k_1 rho -+ lam W lie on the branches
    k_perp in {0, pi}^(D-1), c_b = g(k_perp); Omega_b'' = N_b / (4 h^1.5), N_b = 2 g'' h - g'^2,
    h = c_b + g(k_1); at a zero of N_b the third derivative is g3 / (2 Omega_b) (fold iff g3 != 0)."""
    g = lambda k: a * (1 - np.cos(k)) + b * (1 - np.cos(2 * k))
    g1 = lambda k: a * np.sin(k) + 2 * b * np.sin(2 * k)
    g2 = lambda k: a * np.cos(k) + 4 * b * np.cos(2 * k)
    g3 = lambda k: -a * np.sin(k) - 8 * b * np.sin(2 * k)
    c0 = np.sqrt(a / 2 + 2 * b)
    k = np.linspace(delta, np.pi, 200001)
    out = {"min_gprime_over_sin_0_pi": float(np.min(g1(k[:-1]) / np.sin(k[:-1]))),
           "g2_at_0": float(g2(0.0)), "g2_at_pi": float(g2(np.pi)), "branches": []}
    for nb in range(D):
        cb = nb * g(np.pi)
        N = lambda kk: 2 * g2(kk) * (cb + g(kk)) - g1(kk)**2
        Nk = N(k)
        idx = np.nonzero(Nk[:-1] * Nk[1:] < 0)[0]
        zs = [optimize.brentq(N, k[i], k[i + 1]) for i in idx]
        W = lambda kk: np.sqrt(cb + g(kk))
        out["branches"].append({"transverse_pi": nb, "c_b": float(cb),
                                "v_axial_max": float(np.max(g1(k) / (2 * W(k)))),
                                "N_at_pi": float(N(np.pi)), "N_at_delta": float(N(delta)),
                                "folds": [{"k": float(z), "cos_k": float(np.cos(z)),
                                           "Omega_b_third": float(g3(z) / (2 * W(z))),
                                           "w_caustic": float(c0 * 2 * W(z) / g1(z))} for z in zs]})
    return out


def kg_constant():
    """sup_{Y>=0} |1 - I_mu(Y)|, I_mu(Y) = int_0^Y J1(y)/sqrt(y^2+mu^2) dy."""
    y = np.linspace(0, 400, 400001)
    res = {}
    for mu in [1e-3, 1e-2, 0.1, 0.5, 1.0]:
        I = cumulative_trapezoid(special.j1(y) / np.sqrt(y**2 + mu**2), y, initial=0)
        res[str(mu)] = {"sup_abs_1_minus_I": float(np.max(np.abs(1 - I))),
                        "min_I": float(np.min(I)), "max_I": float(np.max(I))}
    return res


def run(D, L, rhos, m, kname, dlam, L_ref):
    a, b = KS[kname]
    sp = speeds(a, b)
    sp_m = speeds(a, b, m)
    rhos = np.asarray(rhos)
    lam_end = 0.9 * (L - rhos.max() - 1) / sp_m["v_front_axis"]
    if D == 3:
        lam_end = min(lam_end, 4.0 * rhos.max() / sp["c0"])
    lams = np.arange(dlam, lam_end + dlam, dlam)
    if D == 1:
        ns = np.concatenate([rhos, rhos + 1])
        made = made_ring(L, ns, a, b, m, lams)
        G = static_axis(1, ns, a, b, m)
        n = len(rhos)
        Delta = (made[:, n:] - made[:, :n]) / (-(G[n:] - G[:n])) - 1
        idx = np.arange(0, len(lams), STRIDE)
        mr = made_ring(L_ref, ns, a, b, m, lams[idx])
        Dref = (mr[:, n:] - mr[:, :n]) / (-(G[n:] - G[:n])) - 1
        Gref = None
        if b == 0.0:   # closed form, nearest neighbour: G(n) = e^{-th n}/(a sinh th), cosh th = 1 + m^2/a
            th = np.arccosh(1 + m**2 / a)
            Gref = np.exp(-th * ns) / (a * np.sinh(th))
            Gref = float(np.max(np.abs((Gref[n:] - Gref[:n]) / (G[n:] - G[:n]) - 1)))
    else:
        made = made_torus3(L, rhos, a, b, m, lams)
        G = static_axis(3, rhos, a, b, m)
        Delta = made / (-G) - 1
        idx = np.arange(0, len(lams), STRIDE)
        Dref = made_torus3(L_ref, rhos, a, b, m, lams[idx]) / (-G) - 1
        Gref = None
        if b == 0.0:   # cross-check of the static with the Bessel form
            ts = np.logspace(-5, np.log10(min(60.0 / m**2, 2e8)), 6000)   # ive is finite below 1e9
            v = np.array([[np.exp(-m**2 * t) * special.ive(r, a * t) * special.ive(0, a * t)**2 * t
                           for r in rhos] for t in ts])
            Gb = simpson(v, x=np.log(ts), axis=0)
            tt = np.logspace(np.log10(ts[-1]), np.log10(60.0 / m**2), 2000)   # tail, ive ~ (2 pi x)^{-1/2}
            Gb = Gb + simpson(np.exp(-m**2 * tt) * (2 * np.pi * a * tt)**-1.5 * tt, x=np.log(tt))
            Gref = float(np.max(np.abs(Gb / G - 1)))
    rows = []
    for j, r in enumerate(rhos):
        lmax = min(0.9 * (L - r - 1) / sp_m["v_front_axis"], float(lams[-1]))
        eta = ETA * r**(-A_ARR)
        lf, la = formation(lams, Delta[:, j], lmax, eta)
        lf2, _ = formation(lams, Delta[:, j], lmax / 2, eta)
        w = lams * sp["c0"] / r
        late = (w >= 1.5) & (w <= 3.0) & (lams <= lmax)
        tail = (lams >= lmax / 2) & (lams <= lmax)
        mid = (lams >= 1.2 * r / sp["v_front_axis"]) & (w <= 0.8)
        pre = float(np.max(np.abs(Delta[mid, j] + 1))) if mid.any() else None
        sel_s = lams[idx] <= lmax
        img = float(np.max(np.abs(Delta[idx][sel_s, j] - Dref[sel_s, j])))
        rows.append({"image_check_max_abs_dDelta": img,"rho": int(r), "mu": float(m * r / sp["c0"]), "lam_max": float(lmax),
                     "w_max": float(lmax * sp["c0"] / r), "arrival_threshold": float(eta),
                     "lam_arrival": la,
                     "lam_arrival_vfront_over_rho": (la * sp["v_front_axis"] / r) if la else None,
                     "lam_form": lf, "lam_form_half_window": lf2,
                     "lam_form_c0_over_rho": (lf * sp["c0"] / r) if lf else None,
                     "lam_form_minus_rho_over_c0_div_rho13": ((lf - r / sp["c0"]) / r**(1 / 3)) if lf else None,
                     "max_abs_Delta_second_half_window": float(np.max(np.abs(Delta[tail, j]))),
                     "max_abs_Delta_w_1.5_to_3": float(np.max(np.abs(Delta[late, j]))) if late.any() else None,
                     "precursor_max_abs_Delta_plus_1": pre,
                     "precursor_times_rho13": (pre * r**(1 / 3)) if pre is not None else None})
    return {"D": D, "L": L, "L_ref": L_ref, "image_check_stride": STRIDE, "K": kname, "a": a, "b": b, "m_h": m, "dlam": dlam,
            "speeds_m0": sp, "speeds_at_m": sp_m, "static_crosscheck_rel_err": Gref, "rows": rows}


if __name__ == "__main__":
    res = {"EPS": EPS, "ETA": ETA, "A_ARR": A_ARR, "kg_constant": kg_constant(),
           "fold_check": {f"{kn}_D{D}": fold_check(*KS[kn], D) for kn in KS for D in (1, 3)}, "runs": []}
    for kname in KS:
        res["runs"].append(run(1, 16384, [16, 32, 64, 128, 256, 512], 5e-5, kname, 0.05, 32768))
        res["runs"].append(run(3, 256, [8, 16, 24, 48], 2.5e-4, kname, 0.05, 384))
    with open(OUT / "oscillator_formation.json", "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1)
    for r in res["runs"]:
        print(r["D"], r["K"], r["speeds_m0"], "static check", r["static_crosscheck_rel_err"])
        for row in r["rows"]:
            print("  ", row)
    print(res["kg_constant"])
