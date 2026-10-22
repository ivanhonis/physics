"""Check of items 1 and 2 of 07-ilang-weight/08-field-speed against the exact
evolution of one field object (N_f = 1, n = 1/|X|) from its lowest state, on a
ring and on a cubic torus, with the source g_s Phi_{x_s} switched on suddenly
and gradually.

The source sits at x_s = 0. The one-object contract -t_f A + g(lam)|0><0| and
the start (uniform state) are invariant under the point group of the torus that
fixes 0, so the state stays in the invariant sector (orbit basis); the
evolution there is exact. With psi = exp(-i E0 lam)(c0 + g chi), chi solves
i chi' = (H - E0) chi + f P c0 exactly. The made field is reported in units of
2 n g_s / t_f:  phi = delta rho / (2 n g_s / t_f);  static mark phi_st = -Lambda^+.
"""
import itertools
import json
import math
import time
from pathlib import Path

import numpy as np
import scipy.sparse as sp
from scipy.special import erfc, jv

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
TF = 1.0
LOG = []
RES = {}


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    LOG.append(s)


# ---------------------------------------------------------------- lattice and sector
def sector(L, D):
    h = L // 2
    base = h + 1
    reps = np.array(list(itertools.combinations_with_replacement(range(base), D)), dtype=np.int64)

    def key(a):
        a = np.sort(np.minimum(a % L, (-a) % L), axis=-1)
        k = np.zeros(a.shape[:-1], dtype=np.int64)
        for mu in range(D):
            k = k * base + a[..., mu]
        return k

    rk = key(reps)
    assert np.all(np.diff(rk) > 0)
    # orbit size: sign choices times distinct permutations
    signs = np.prod(np.where((reps == 0) | (reps == h), 1, 2), axis=1)
    # distinct permutations: D! / prod over values of (multiplicity)!; for sorted reps of length <= 3
    perm_div = np.ones(len(reps))
    if D == 2:
        perm_div = np.where(reps[:, 0] == reps[:, 1], 2.0, 1.0)
    elif D == 3:
        e01, e12 = reps[:, 0] == reps[:, 1], reps[:, 1] == reps[:, 2]
        perm_div = np.where(e01 & e12, 6.0, np.where(e01 | e12, 2.0, 1.0))
    size = (signs * math.factorial(D) / perm_div).astype(float)
    assert abs(size.sum() - L ** D) < 0.5
    rows, cols = [], []
    for mu in range(D):
        for s in (1, -1):
            y = reps.copy()
            y[:, mu] += s
            rows.append(np.arange(len(reps)))
            cols.append(np.searchsorted(rk, key(y)))
    rows, cols = np.concatenate(rows), np.concatenate(cols)
    n = sp.coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(reps),) * 2).tocsr().tocoo()
    H0 = sp.csr_matrix((-TF * np.sqrt(size[n.row] / size[n.col]) * n.data, (n.row, n.col)), shape=n.shape)
    X = float(L ** D)

    def axis(d):
        a = np.zeros((1, D), dtype=np.int64)
        a[0, 0] = d
        return int(np.searchsorted(rk, key(a))[0])

    return dict(L=L, D=D, M=len(reps), size=size, H0=H0, X=X, c0=np.sqrt(size / X), E0=-2.0 * D * TF, axis=axis)


def lam_plus_axis(L, D, rmax):
    """Lambda^+(r e_1) on the torus from its Fourier sum, (4.4) of 06-ilang-source/04-profile; also S_2."""
    k = 2 * np.pi * np.arange(L) / L
    w1 = 4 * np.sin(k / 2) ** 2
    others = np.zeros(1)
    for _ in range(D - 1):
        others = (others[:, None] + w1[None, :]).ravel()
    S = np.zeros(L)
    S2 = 0.0
    for i in range(L):
        tot = w1[i] + others
        if i == 0:
            tot = tot[1:]
        S[i] = (1 / tot).sum()
        S2 += (1 / tot ** 2).sum()
    r = np.arange(rmax + 1)
    return (np.cos(np.outer(r, k)) @ S) / L ** D, S2 / L ** D


def phi_from_chi(sec, sel, chi, g):
    c0, size = sec["c0"][sel][:, None], sec["size"][sel][:, None]
    return TF * sec["X"] * (c0 * chi.real + 0.5 * g * np.abs(chi) ** 2) / size


def smooth_step(u):
    u = np.clip(np.asarray(u, float), 0.0, 1.0)
    a = np.where(u > 0, np.exp(-1 / np.where(u > 0, u, 1)), 0.0)
    b = np.where(u < 1, np.exp(-1 / np.where(u < 1, 1 - u, 1)), 0.0)
    return a / (a + b)


# ---------------------------------------------------------------- evolutions
def sudden_dense(sec, g, lams, sel, chunk=2000, eig=None):
    if eig is None:
        H = sec["H0"].toarray()
        H[0, 0] += g
        eig = np.linalg.eigh(H)
    E, V = eig
    mu = E - sec["E0"]
    mu = np.where(np.abs(mu) < 1e-14, 1e-14, mu)
    Vs = V[sel, :] * (V[0, :] / np.sqrt(sec["X"]))[None, :]
    out = np.empty((len(sel), len(lams)))
    for i in range(0, len(lams), chunk):
        lc = lams[i:i + chunk]
        chi = Vs @ (np.expm1(-1j * np.outer(mu, lc)) / mu[:, None])
        out[:, i:i + chunk] = phi_from_chi(sec, sel, chi, g)
    return out


def first_order_dense(sec, lams, sel, chunk=2000):
    E, V = np.linalg.eigh(sec["H0"].toarray())
    eps = E - sec["E0"]
    pos = eps > 1e-9
    w = V[sel][:, pos] * V[0, pos][None, :] / np.sqrt(sec["size"][sel])[:, None]
    st = -TF * (w @ (1 / eps[pos]))
    out = np.empty((len(sel), len(lams)))
    for i in range(0, len(lams), chunk):
        lc = lams[i:i + chunk]
        out[:, i:i + chunk] = TF * (w @ ((np.cos(np.outer(eps[pos], lc)) - 1) / eps[pos][:, None]))
    return out, st


class Cheb:
    """Chebyshev expansions of exp(-i x dl) and (exp(-i x dl) - 1)/x on [a, b] (spectrum of A = H - E0)."""

    def __init__(self, a, b, dl):
        self.c, self.h = (a + b) / 2, (b - a) / 2
        K = int(self.h * dl + 12 * (self.h * dl) ** (1 / 3) + 20)
        k = np.arange(K)
        pref = np.where(k == 0, 1.0, 2.0) * (-1j) ** k

        def cU(s):
            return np.exp(-1j * self.c * s) * pref * jv(k, self.h * s)

        # exp(-i x dl) = sum_k cU_k(dl) T_k(y);  (exp(-i x dl) - 1)/x = -i int_0^dl exp(-i x s) ds
        xg, wg = np.polynomial.legendre.leggauss(int((abs(self.c) + self.h) * dl) + 64)
        s = 0.5 * dl * (xg + 1)
        cUd = cU(dl)
        cPd = -1j * 0.5 * dl * sum(wq * cU(sq) for wq, sq in zip(wg, s))
        assert abs(jv(K - 1, self.h * dl)) < 1e-17
        keep = np.where((np.abs(cUd) > 1e-17) | (np.abs(cPd) > 1e-17 * dl))[0]
        Kt = max(int(keep.max()) + 1, 2)
        self.coef = np.stack([cUd[:Kt], cPd[:Kt]], axis=1)  # columns: U, Phi

    def apply(self, matvec, V, coef):
        """sum_k T_k(A~) V * coef[k]; V has shape (M, ncol), coef (K, ncol)."""
        t0, t1 = V, (matvec(V) - self.c * V) / self.h
        s = coef[0] * t0 + coef[1] * t1
        for ck in coef[2:]:
            t0, t1 = t1, 2 * (matvec(t1) - self.c * t1) / self.h - t0
            s = s + ck * t1
        return s


def a_op(sec):
    return (sec["H0"] - sec["E0"] * sp.identity(sec["M"], format="csr")).tocsr().astype(complex)


def a_matvec(A0, gval):
    def mv(v):
        o = A0 @ v
        o[0] += gval * v[0]
        return o

    return mv


def propagate_const(sec, g, chi0, dl, nstep, sel):
    """Exact evolution with constant source g from chi0; phi at k*dl, k = 1..nstep."""
    D = sec["D"]
    ch = Cheb(-0.1 - abs(g), 4 * D * TF + 0.1 + abs(g), dl)
    mv = a_matvec(a_op(sec), g)
    b = np.zeros((sec["M"], 1), complex)
    b[0] = 1 / np.sqrt(sec["X"])
    w = ch.apply(mv, b, ch.coef[:, 1:2])[:, 0]
    chi = chi0.astype(complex)[:, None]
    out = np.empty((len(sel), nstep))
    for k in range(nstep):
        chi = ch.apply(mv, chi, ch.coef[:, 0:1])
        chi[:, 0] += w
        out[:, k] = phi_from_chi(sec, sel, chi[sel], g)[:, 0]
    return out, chi[:, 0]


def gradual(sec, g, T, sel, dl_ramp, n_after=100):
    """Evolution with g(lam) = g f(lam/T): exponential midpoint rule on [0, T] (step dl_ramp),
    exact constant-source evolution on [T, 2T]; phi on a grid of [0, 2T]."""
    D = sec["D"]
    nr = int(np.ceil(T / dl_ramp))
    dl = T / nr
    ch = Cheb(-0.1 - abs(g), 4 * D * TF + 0.1 + abs(g), dl)
    A0 = a_op(sec)
    V = np.zeros((sec["M"], 2), complex)  # columns: chi, b
    V[0, 1] = 1 / np.sqrt(sec["X"])
    every = max(1, nr // 100)
    lam_rec, ph_rec = [0.0], [np.zeros(len(sel))]
    for k in range(nr):
        fm = float(smooth_step((k + 0.5) * dl / T))
        Y = ch.apply(a_matvec(A0, g * fm), V, ch.coef)
        V[:, 0] = Y[:, 0] + fm * Y[:, 1]
        if (k + 1) % every == 0 or k == nr - 1:
            lam_rec.append((k + 1) * dl)
            ph_rec.append(phi_from_chi(sec, sel, V[sel, 0:1], g)[:, 0])
    chi = V[:, 0].copy()
    ph2, _ = propagate_const(sec, g, chi, T / n_after, n_after, sel)
    lam_all = np.concatenate([np.array(lam_rec), T + T / n_after * np.arange(1, n_after + 1)])
    return lam_all, np.concatenate([np.array(ph_rec).T, ph2], axis=1)


# ---------------------------------------------------------------- scaling functions, helpers
def gD(zeta, D):
    """Re Gamma(D/2, -i zeta)/Gamma(D/2): gradient ratio (8.9) for D = 1, 3."""
    z = np.sqrt(np.asarray(zeta, float)) * np.exp(-1j * np.pi / 4)
    if D == 1:
        return erfc(z).real
    return (erfc(z) + 2 * z / np.sqrt(np.pi) * np.exp(-z * z)).real


def zeta_star(eps, D):
    zz = np.linspace(1e-7, 5, 500001)
    bad = np.abs(1 - gD(zz, D)) > eps
    return float(zz[np.argmax(bad)])


def eta(z):
    w = np.sqrt(1 - z ** 2)
    return np.arctanh(w) - w


def last_entry(lams, dev, eps):
    bad = np.where(np.abs(dev) > eps)[0]
    if len(bad) == 0:
        return float(lams[0])
    return float(lams[min(bad[-1] + 1, len(lams) - 1)])


def powerfit(x, y):
    p = np.polyfit(np.log(x), np.log(y), 1)
    return float(p[0]), float(np.exp(p[1]))


def grad(ph, lp, ds):
    """Central-difference gradient along the axis and its static value; ph rows are (d-1, d+1) pairs."""
    G = np.array([(ph[2 * i + 1] - ph[2 * i]) / 2 for i in range(len(ds))])
    Gst = np.array([(-lp[d + 1] + lp[d - 1]) / 2 for d in ds])
    return G, Gst


# ================================================================ item 1: front
def front(sec, g, ds, dl, lam_max, p_f, eps_f, fit_min, label):
    D = sec["D"]
    sel = [sec["axis"](int(d)) for d in ds]
    v0 = np.zeros(sec["M"], complex)
    t0 = time.time()
    nst = int(round(lam_max / dl))
    ph, _ = propagate_const(sec, g, v0, dl, nst, sel)
    lams = dl * np.arange(1, nst + 1)
    arr = np.array([lams[np.argmax(np.abs(ph[i]) >= 0.5 * eps_f * d ** -p_f)] for i, d in enumerate(ds)])
    big = ds >= fit_min
    slope = np.polyfit(ds[big], arr[big], 1)[0]
    kap = []
    for i, d in enumerate(ds):
        z = 2 * TF * lams / d
        logb = np.log(TF * lams) - d * eta(np.minimum(z, 1 - 1e-12))
        m = (z <= 0.95) & (logb > np.log(1e-9))
        kap.append(float(np.max(np.abs(ph[i][m]) / np.exp(logb[m]))))
    win = [np.abs(2 * TF * lams - d) <= 3 * d ** (1 / 3) for d in ds]
    peak = np.array([np.max(np.abs(ph[i][win[i]])) for i in range(len(ds))])
    pe, pc = powerfit(ds[big], peak[big])
    res = dict(criterion=f"first lam with |delta rho| >= eps (n g/t) rho^-p, i.e. |phi| >= (eps/2) rho^-p; eps={eps_f}, p={p_f}",
               rho=ds.tolist(), arrival=arr.tolist(), arrival_times_2t_over_rho=(2 * TF * arr / ds).tolist(),
               speed_linear_fit=float(1 / slope), fit_min_rho=int(fit_min),
               max_ratio_to_kapteyn_bound_ahead=max(kap), front_peak_phi=peak.tolist(),
               front_peak_exponent=pe, front_peak_prefactor=pc)
    if D == 1:
        fd = {}
        for i, d in enumerate(ds):
            if d >= 64:
                fr = 0.5 * jv(d, 2 * TF * lams[win[i]]) * np.cos(d * np.pi / 2 - 2 * TF * lams[win[i]])
                fd[int(d)] = float(np.max(np.abs(ph[i][win[i]] - fr)) / np.max(np.abs(fr)))
        res["front_form_rel_dev"] = fd
        res["front_peak_times_d13"] = (peak * ds ** (1 / 3)).tolist()
        ahead = {}
        for i, d in enumerate(ds):
            m = 2 * TF * lams <= 0.8 * d
            ahead[int(d)] = float(np.max(np.abs(ph[i][m])))
        res["max_abs_phi_for_2tlam_le_0p8rho"] = ahead
    log(f"[{label}] front ({time.time() - t0:.0f}s):", res)
    return res


# ================================================================ item 2 (i): formation, sudden
def formation_sudden(sec, g, lp, ds, dl, lam_w, epsF, fit_min, label):
    D = sec["D"]
    sel = [sec["axis"](int(d + s)) for d in ds for s in (-1, 1)]
    v0 = np.zeros(sec["M"], complex)
    t0 = time.time()
    nst = int(lam_w / dl)
    ph, _ = propagate_const(sec, g, v0, dl, nst, sel)
    lams = dl * np.arange(1, nst + 1)
    G, Gst = grad(ph, lp, ds)
    zs = zeta_star(epsF, D)
    lf, coll = [], {}
    for i, d in enumerate(ds):
        ratio = G[i] / Gst[i]
        lf.append(last_entry(lams, 1 - ratio, epsF))
        zeta = d ** 2 / (4 * TF * lams)
        m = zeta <= 0.5
        coll[int(d)] = float(np.max(np.abs(ratio[m] - gD(zeta[m], D))))
    lf = np.array(lf)
    big = ds >= fit_min
    a, c = powerfit(ds[big], lf[big])
    res = dict(window_end=float(lam_w), eps=epsF, zeta_star=zs, d=ds.tolist(), lam_form=lf.tolist(),
               lam_form_pred=(ds ** 2 / (4 * TF * zs)).tolist(), fit_exponent=a, fit_min_d=int(fit_min),
               fit_prefactor=c, pred_prefactor=1 / (4 * TF * zs), max_dev_from_scaling_fn_zeta_le_0p5=coll)
    log(f"[{label}] formation sudden ({time.time() - t0:.0f}s):", res)
    return res


# ================================================================ item 2 (ii): gradual
def formation_gradual(sec, g, lp, ds, Ts, epsG, label, dl_ramp, n_after=100):
    sel = [sec["axis"](int(d + s)) for d in ds for s in (-1, 1)]
    Emat = np.zeros((len(ds), len(Ts)))
    for j, T in enumerate(Ts):
        t0 = time.time()
        lam_all, ph = gradual(sec, g, T, sel, dl_ramp, n_after)
        f = smooth_step(lam_all / T)
        G, Gst = grad(ph, lp, ds)
        for i in range(len(ds)):
            Emat[i, j] = np.max(np.abs(G[i] - f * Gst[i])) / abs(Gst[i])
        log(f"[{label}] gradual T={T:.2f} ({time.time() - t0:.0f}s): E={Emat[:, j].round(4).tolist()}")
    Tf = []
    for i in range(len(ds)):
        above = np.where(Emat[i] > epsG)[0]
        j = above[-1] + 1 if len(above) else 0
        if j == 0 or j >= len(Ts):
            Tf.append(float("nan"))
            continue
        x0, x1 = np.log(Ts[j - 1]), np.log(Ts[j])
        y0, y1 = np.log(Emat[i, j - 1]), np.log(Emat[i, j])
        Tf.append(float(np.exp(x0 + (np.log(epsG) - y0) * (x1 - x0) / (y1 - y0))))
    Tf = np.array(Tf)
    ok = np.isfinite(Tf)
    a, c = powerfit(ds[ok], Tf[ok])
    nu = (ds[:, None] ** 2 / (TF * Ts[None, :])).ravel()
    m = (nu < 0.5) & (Emat.ravel() > 0)
    ae, ce = powerfit(nu[m], Emat.ravel()[m])
    res = dict(criterion="E(d,T) = max over lam in [0,2T] of |grad phi - f(lam/T) grad phi_st| / |grad phi_st|",
               eps=epsG, d=ds.tolist(), T=Ts.tolist(), E=Emat.round(6).tolist(), T_form=Tf.tolist(),
               fit_exponent=a, fit_prefactor=c, E_vs_nu_exponent_nu_lt_0p5=ae, E_vs_nu_prefactor=ce)
    log(f"[{label}] gradual:", {k: v for k, v in res.items() if k not in ("E", "T")})
    return res


# ================================================================ first order, sum rule, lambda-average
def small_checks(sec, g, lp, S2, lams, rs, label, running=()):
    sel = [sec["axis"](int(r)) for r in rs]
    H = sec["H0"].toarray()
    H[0, 0] += g
    E, V = np.linalg.eigh(H)
    ph = sudden_dense(sec, g, lams, sel, eig=(E, V))
    ph1, st = first_order_dense(sec, lams, sel)
    res = dict(L=sec["L"], D=sec["D"], g_s_over_t_f=g, sector_dim=sec["M"], S2=float(S2),
               static_sector_vs_fourier=float(np.max(np.abs(st + lp[rs]))),
               exact_vs_first_order_rel=float(np.max(np.abs(ph - ph1)) / abs(lp[0])))
    a_ = V.T @ sec["c0"]
    davg = np.array([((a_ ** 2) @ (V[o] ** 2) - sec["c0"][o] ** 2) / sec["size"][o] * TF * sec["X"] / (2 * g) for o in sel])
    res["infinite_lambda_average_vs_static_rel"] = float(np.max(np.abs(davg + lp[rs])) / abs(lp[0]))
    phs = sudden_dense(sec, g, lams[[0, len(lams) // 2, -1]], list(range(sec["M"])), eig=(E, V))
    res["sum_rule_max_abs"] = float(np.max(np.abs((phs * sec["size"][:, None]).sum(axis=0))))
    run = {}
    dE = E[:, None] - E[None, :]
    for cL in running:
        Lam = cL * sec["L"] ** 2 / TF
        x = -1j * dE * Lam
        K = np.where(np.abs(dE) > 1e-14, np.expm1(x) / np.where(np.abs(dE) > 1e-14, x, 1.0), 1.0)
        devs, devx = [], []
        for o, r, da in zip(sel, rs, davg):
            w = a_ * V[o]
            avg = (np.einsum("i,ij,j->", w, K, w).real - sec["c0"][o] ** 2) / sec["size"][o] * TF * sec["X"] / (2 * g)
            devs.append(abs(avg + lp[r]))
            devx.append(abs(avg - da))
        run[f"{cL}L^2/t"] = dict(max_dev_from_static_phi=float(max(devs)), max_dev_from_exact_average_phi=float(max(devx)),
                                 bound_S2_over_tLambda=float(S2 / (TF * Lam)))
    if running:
        res["running_average"] = run
    log(f"[{label}] small checks:", res)
    return res


def integrator_checks():
    """Chebyshev propagation against dense diagonalization; step convergence of the midpoint rule."""
    sec = sector(16, 3)
    g = 1e-3
    sel = [sec["axis"](d) for d in range(9)]
    lams = 0.05 * np.arange(1, 401)
    ph, _ = propagate_const(sec, g, np.zeros(sec["M"], complex), 0.05, 400, sel)
    ph_big, _ = propagate_const(sec, g, np.zeros(sec["M"], complex), 2.0, 10, sel)
    ref = sudden_dense(sec, g, lams, sel)
    l1, p1 = gradual(sec, g, 20.0, sel, 0.2)
    l2, p2 = gradual(sec, g, 20.0, sel, 0.05)
    G1, G2 = (p1[4] - p1[2]) / 2, (p2[4] - p2[2]) / 2
    res = dict(cube_L=16, cheb_vs_dense_step_0p05=float(np.max(np.abs(ph - ref))),
               cheb_vs_dense_step_2=float(np.max(np.abs(ph_big - ref[:, 39::40]))),
               midpoint_step_0p2_vs_0p05_max_abs_phi=float(np.max(np.abs(p1 - p2))),
               midpoint_step_0p2_vs_0p05_rel_gradient_d3=float(np.max(np.abs(G1 - G2)) / np.max(np.abs(G2))))
    log("[integrator checks]", res)
    return res


if __name__ == "__main__":
    T0 = time.time()
    RES["integrator_checks"] = integrator_checks()
    # ---------------- ring L = 1024 (dense): first order, sum rule, lambda-average; gradual switching
    sec = sector(1024, 1)
    lp, S2 = lam_plus_axis(1024, 1, 512)
    RES["ring_L1024"] = small_checks(sec, 1e-5, lp, S2, np.linspace(1, 2000, 2000), np.array([0, 8, 64, 256]),
                                     "ring L=1024", running=(1.0, 4.0, 16.0))
    RES["ring_L1024"]["gradual"] = formation_gradual(sec, 1e-5, lp, np.array([4, 6, 8, 12, 16]),
                                                     np.geomspace(20, 8000, 14), 0.2, "ring L=1024", 0.2)
    # ---------------- ring L = 16384: front, and sudden formation before the wrap time
    L = 16384
    sec = sector(L, 1)
    lp, S2 = lam_plus_axis(L, 1, 64)
    RES["ring_L16384"] = dict(L=L, g_s_over_t_f=1e-5, sector_dim=sec["M"])
    RES["ring_L16384"]["front"] = front(sec, 1e-5, np.array([16, 24, 32, 48, 64, 96, 128, 160, 192, 256, 320, 384]),
                                        0.02, 205.0, 0.5, 0.1, 64, "ring L=16384")
    RES["ring_L16384"]["formation_sudden"] = formation_sudden(sec, 1e-5, lp, np.array([6, 8, 12, 16, 24, 32, 40]),
                                                              0.5, 0.45 * L / TF, 0.2, 12, "ring L=16384")
    # ---------------- cube L = 32 (dense): first order, sum rule, lambda-average
    sec = sector(32, 3)
    lp, S2 = lam_plus_axis(32, 3, 16)
    RES["cube_L32"] = small_checks(sec, 1e-3, lp, S2, np.linspace(0.1, 300, 3000), np.arange(0, 17), "cube L=32",
                                   running=(1.0, 4.0))
    # ---------------- cube L = 160: front, and sudden formation before the wrap time
    L = 160
    sec = sector(L, 3)
    lp, S2 = lam_plus_axis(L, 3, 16)
    RES["cube_L160"] = dict(L=L, g_s_over_t_f=1e-3, sector_dim=sec["M"])
    RES["cube_L160"]["front"] = front(sec, 1e-3, np.array([6, 8, 10, 12, 16, 20, 24, 32, 40, 48, 56, 64]),
                                      0.05, 38.0, 1.5, 0.1, 12, "cube L=160")
    RES["cube_L160"]["formation_sudden"] = formation_sudden(sec, 1e-3, lp, np.array([3, 4, 5, 6, 7, 8, 9]),
                                                            0.1, 0.45 * L / TF, 0.1, 4, "cube L=160")
    # ---------------- cube L = 128: gradual switching
    L = 128
    sec = sector(L, 3)
    lp, S2 = lam_plus_axis(L, 3, 16)
    RES["cube_L128"] = dict(L=L, g_s_over_t_f=1e-3, sector_dim=sec["M"])
    RES["cube_L128"]["gradual"] = formation_gradual(sec, 1e-3, lp, np.array([3, 4, 5, 6, 7]), np.geomspace(4, 200, 11),
                                                    0.1, "cube L=128", 0.2)
    log(f"total time {time.time() - T0:.0f}s")
    (OUT / "check_front_formation.json").write_text(json.dumps(RES, indent=1))
    (OUT / "check_front_formation.log").write_text("\n".join(LOG) + "\n")
