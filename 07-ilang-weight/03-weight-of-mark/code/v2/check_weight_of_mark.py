"""Check for 07-ilang-weight/03-weight-of-mark, derivation v2.

One field object (N_f = 1, n = 1/|X|) on a ring, a square torus and a cubic torus.
Held body: point term g_b P_x, g_b = sigma*gamma*M_k; held source: point term g_s P_xs.
Weight differences are taken from exact lowest eigenvalues of C_1 + g_b P_x + g_s P_xs
(symmetric differences in g_s, Richardson-extrapolated to first order in g_s) and compared
with the closed forms of the derivation: cost (3.2), (3.4), (3.5); weight (3.6)-(3.8);
ring form (7.6); weight against cost (3.12)-(3.17), with nu = gamma*n retained for
coupling (a) (scan in nu through the factor N_f of (3.1)); mirror (3.18); distance scans
with 1 << |r|, |r'| << L; lattice asymptotics behind (3.10), (3.11), (3.16), (3.17).
Outputs: output/check_log.txt, output/check_results.json.
"""
import json
from pathlib import Path

import numpy as np
import scipy.sparse as sp
from scipy.optimize import brentq
from scipy.sparse.linalg import eigsh

OUT = Path(__file__).parent / "output"
OUT.mkdir(parents=True, exist_ok=True)
np.seterr(divide="ignore", invalid="ignore")   # F = 0 only at the reference place x', which is masked
T_F = 1.0
M_LEV = (1.0, 1.5)                      # half-gaps of two clock levels
GHAT = (0.01, 0.02, 0.04, 0.08)          # targets for max |g_b| * ell_0 / t_f
SIZES = {1: (32, 64), 2: (12, 20), 3: (8, 12)}
NU_T = (-0.5, 1.0, 4.0, 20.0)           # targets for nu = gamma*n in the coupling-(a) scan
KAPPA2 = 2 * np.pi * 0.0487655 - np.euler_gamma - 1.5 * np.log(2)
XI3 = 2.837297 / (4 * np.pi)
LOG, RES = [], {}


def log(s=""):
    print(s, flush=True)
    LOG.append(s)


def graph(D, L):
    n = L**D
    co = np.array(np.unravel_index(np.arange(n), (L,) * D)).T
    rows, cols = [], []
    for mu in range(D):
        sh = co.copy()
        sh[:, mu] = (sh[:, mu] + 1) % L
        nb = np.ravel_multi_index(tuple(sh.T), (L,) * D)
        rows += [np.arange(n), nb]
        cols += [nb, np.arange(n)]
    A = sp.csr_matrix((np.ones(2 * D * n), (np.concatenate(rows), np.concatenate(cols))), shape=(n, n))
    k = 2 * np.pi * np.arange(L) / L
    grids = np.meshgrid(*([k] * D), indexing="ij")
    om = sum(4 * np.sin(g / 2) ** 2 for g in grids)
    return co, (-T_F * A).tocsr(), om


def ellpow(om, p=1, shift=0.0):
    """(1/|X|) sum_{k!=0} e^{iky}/(omega-shift)^p as an array over displacements y."""
    inv = np.zeros_like(om)
    m = om > 1e-12
    inv[m] = 1.0 / (om[m] - shift) ** p
    return np.fft.ifftn(inv).real.ravel()


def lowest(H, vec=True):
    if H.shape[0] <= 600:
        if vec:
            w, v = np.linalg.eigh(H.toarray())
            return w[0], v[:, 0]
        return np.linalg.eigvalsh(H.toarray())[0], None
    w, v = eigsh(H, k=1, which="SA", tol=0, v0=np.ones(H.shape[0]))
    return w[0], v[:, 0]


def lowest_val(H):
    if H.shape[0] <= 600:
        return np.linalg.eigvalsh(H.toarray())[0]
    return eigsh(H, k=1, which="SA", tol=0, v0=np.ones(H.shape[0]), return_eigenvectors=False)[0]


def src_coef(base, X, y, h):
    """First-order coefficient in g_s of the lowest eigenvalue of base + g_s P_y, from exact
    eigenvalues: symmetric differences at g_s = h and h/2, Richardson-extrapolated (error O(h^4))."""
    S = [(lowest_val(base + point(X, y, hh)) - lowest_val(base + point(X, y, -hh))) / (2 * hh) for hh in (h, h / 2)]
    return (4 * S[1] - S[0]) / 3


def point(n, i, g):
    return sp.csr_matrix(([g], ([i], [i])), shape=(n, n))


def exact_rho(om, g, X):
    """Lowest eigenpair of C_1 + g P_0 from (3.2)-(3.3): returns delta, eta, rho(y)."""
    wmin = om[om > 1e-12].min()
    f = lambda d: 1.0 / (X * d) - ellpow(om, 1, d / T_F)[0] / T_F - 1.0 / g
    d = (brentq(f, 1e-14, T_F * wmin * (1 - 1e-12), xtol=1e-300) if g > 0
         else brentq(f, -1e3, -1e-14, xtol=1e-300))
    eta = X * d / T_F
    ld = ellpow(om, 1, d / T_F)
    l2d0 = np.sum(ld**2)
    return d, eta, (1 - eta * ld) ** 2 / (X + eta**2 * l2d0)


def slope(x, y):
    return float(np.polyfit(np.log(np.abs(x)), np.log(np.abs(y)), 1)[0])


def run_graph(D, L):
    tag = f"D{D}_L{L}"
    co, C1, om = graph(D, L)
    X = L**D
    n = 1.0 / X
    l1, l2, l3 = ellpow(om, 1), ellpow(om, 2), ellpow(om, 3)
    l0, l20 = l1[0], l2[0]
    ap = int(np.ravel_multi_index((L // 2,) * D, (L,) * D))   # antipode: r' of the scans K
    eps00 = -2 * D * T_F
    r = {"L": L, "D": D, "X": X, "ell_0": l0, "ell2_0": l20}
    log(f"\n=== {tag}: |X|={X}, ell_0={l0:.6f}, ell2_0/|X|={l20 / X:.6e}")

    # (M) mirror (3.18): highest eigenvalue = - lowest of mirrored signs (L even, bipartite)
    gb = 0.02 / l0
    top = -lowest_val(-(C1 + point(X, 0, gb) + point(X, 3 % X, 1e-3)))
    r["M_mirror_err"] = abs(top + lowest_val(C1 + point(X, 0, -gb) + point(X, 3 % X, -1e-3)))
    log(f"(M) highest state = -(lowest, mirrored signs): |diff| = {r['M_mirror_err']:.2e}")

    # place pairs: r = y (4 random places), r' = ref (not the antipode); leading difference [ell] non-cancelling
    ref = int(np.ravel_multi_index(tuple([L // 3] + [1] * (D - 1)), (L,) * D))
    dl_all = np.abs(l1 - l1[ref])
    rng = np.random.default_rng(7 * D + L)
    P, seen = [], set()
    for y in rng.permutation(X):          # four places with different values of ell (no lattice images)
        key = round(float(l1[y]), 9)
        if y not in (0, ref) and dl_all[y] > 0.05 * dl_all.max() and key not in seen and len(P) < 4:
            P.append(int(y))
            seen.add(key)
    P = np.array(P)
    r["pairs_r_and_rprime"] = [[co[y].tolist() for y in P], co[ref].tolist()]
    F = -2 * (l1[P] - l1[ref]) / T_F                                      # F / g_s, (3.13)
    F2 = (l1[P] ** 2 - l1[ref] ** 2 - 2 * (l2[P] - l2[ref]) / X) / (n * T_F**2)
    F3 = 2 * (l1[P] * l2[P] - l1[ref] * l2[ref] + l20 * (l1[P] - l1[ref]) - (l3[P] - l3[ref]) / X) / (n**2 * T_F**3 * X)
    dN = n * F                                                             # [delta N]/g_s
    dTh = n**2 * F2 - n * l0 * F / T_F                                     # [Theta_D]/g_s, (3.8)
    T2 = 2 * (l2[P] - l2[ref]) / (X * (l1[P] - l1[ref]))
    lsum = l1[P] + l1[ref]

    def Ba1(g, nu):    # first-order break of coupling (a), (3.15), nu = gamma*n retained
        return -g / (2 * T_F) * (lsum + 2 * l0 / (1 + nu) - T2)

    # rows: levels, branches, gamma; weights from exact two-point eigenvalues
    gams = np.array(GHAT) * T_F / (l0 * max(M_LEV))
    h = 0.02 * T_F / l0                     # source strength for the eigenvalue differences
    rows = []
    for gam in gams:
        for M in M_LEV:
            for s in (1, -1):
                g = s * gam * M
                base = C1 + point(X, 0, g)
                e, v = lowest(base)
                d, eta, rho_ex = exact_rho(om, g, X)
                S = {int(y): src_coef(base, X, int(y), h) for y in list(P) + [ref]}
                w = np.array([S[int(y)] - S[ref] for y in P])           # [W(x)-W(x')]/(N_f g_s), eigenvalues
                rows.append(dict(gam=gam, M=M, s=s, g=g, Cm=e - eps00, w=w, wd=v**2 - v[ref] ** 2,
                                 wex=rho_ex[P] - rho_ex[ref], rhomax=rho_ex.max(), cost_ex_err=abs(e - eps00 - d),
                                 rho_ex_err=np.abs(v**2 - rho_ex).max() * X))

    # (A) eigenvalue weight differences against the closed form (3.7)
    r["A_weight_rel_err"] = max(float(np.max(np.abs(q["w"] - q["wex"]) / np.abs(q["wex"]))) for q in rows)
    r["A_weight_density_normalized_err"] = max(float(np.max(np.abs(q["w"] - q["wex"])) / q["rhomax"]) for q in rows)
    log(f"(A) eigenvalue weight difference vs (3.7), 4 pairs x 16 states: max relative error "
        f"{r['A_weight_rel_err']:.2e} (density-normalized {r['A_weight_density_normalized_err']:.2e})")
    r["B_rho_exact_maxrelerr"] = max(q["rho_ex_err"] for q in rows)
    r["C_cost_exact_maxerr"] = max(q["cost_ex_err"] for q in rows)
    log(f"(B) density vs exact form (3.3): max |X|*|diff| = {r['B_rho_exact_maxrelerr']:.2e}")
    log(f"(C) cost vs exact root (3.2): max |diff| = {r['C_cost_exact_maxerr']:.2e}")

    # (D),(E),(H) deviations from the expansions, scaling in gamma (level M=1.5, sigma=+1)
    sel = [q for q in rows if q["M"] == M_LEV[1] and q["s"] == 1]
    gg = np.array([q["g"] for q in sel])
    devC = [abs(q["Cm"] - (n * q["g"] - n * q["g"] ** 2 * l0 / T_F)) for q in sel]
    devW = [np.abs(q["w"] - (q["g"] * dN + q["g"] ** 2 * dTh)).max() for q in sel]
    # (H) is an expansion of the function W(C) of (3.12): density at all places, relative to r' = ref
    mk = np.arange(X) != ref
    Fx = -2 * (l1 - l1[ref]) / T_F
    F2x = (l1**2 - l1[ref] ** 2 - 2 * (l2 - l2[ref]) / X) / (n * T_F**2)
    F3x = 2 * (l1 * l2 - l1[ref] * l2[ref] + l20 * (l1 - l1[ref]) - (l3 - l3[ref]) / X) / (n**2 * T_F**3 * X)
    devU = [np.abs(q["wd"] - (Fx * q["Cm"] + F2x * q["Cm"] ** 2 + F3x * q["Cm"] ** 3))[mk].max() for q in sel]
    r["D_cost_2nd_slope"] = slope(gg, devC)
    r["E_weight_2nd_slope"] = slope(gg, devW)
    r["H_W_of_C_3rd_slope"] = slope(gg, devU)
    log(f"(D) cost minus 2nd-order (3.5): slope in gamma = {r['D_cost_2nd_slope']:.3f}")
    log(f"(E) eigenvalue weight minus 2nd-order (3.8): slope = {r['E_weight_2nd_slope']:.3f}; devs {np.array(devW)}")
    log(f"(H) density weight minus F C + F2 C^2 + F3 C^3 (3.13): slope = {r['H_W_of_C_3rd_slope']:.3f}")

    # (F) ring: Theta_D of (3.8) against Theta of (7.6)
    if D == 1:
        rr = np.arange(L)
        u = rr * (L - rr)
        th76 = n / (3 * L**2 * T_F**2) * (u**2 - (L**2 - 2) / 2 * u)
        Fa_ = -2 * (l1 - l1[ap]) / T_F
        F2a_ = (l1**2 - l1[ap] ** 2 - 2 * (l2 - l2[ap]) / X) / (n * T_F**2)
        diff = (n**2 * F2a_ - n * l0 * Fa_ / T_F) - (th76 - th76[ap])
        r["F_ring_Theta_vs_7.6_maxdiff"] = float(np.abs(diff).max())
        log(f"(F) ring: Theta_D - Theta(7.6): max |diff| = {r['F_ring_Theta_vs_7.6_maxdiff']:.2e}")

    # (I) single-level break from eigenvalue weights: B = dW/(Cost*F_c) - 1, both couplings
    ibr = []
    for q in rows:
        g, gam, M, s, w, Cm = q["g"], q["gam"], q["M"], q["s"], q["w"], q["Cm"]
        nu = gam * n
        Bfg = w / (Cm * F) - 1
        Ba = w / ((s * M + Cm) * gam * n * F / (1 + nu)) - 1
        ibr.append((gam, np.abs(Bfg - Cm * F2 / F).max(), np.abs(Ba - Ba1(g, nu)).max(),
                    np.abs(Bfg).max(), np.abs(Ba).max()))
    ib = np.array([t for t, q in zip(ibr, rows) if q["M"] == M_LEV[1] and q["s"] == 1])
    r["I_fullgrip_break_size_slope"] = slope(ib[:, 0], ib[:, 3])
    r["I_a_break_size_slope"] = slope(ib[:, 0], ib[:, 4])
    r["I_fullgrip_break_resid_slope"] = slope(ib[:, 0], ib[:, 1])
    r["I_a_break_resid_slope"] = slope(ib[:, 0], ib[:, 2])
    r["I_fullgrip_break_resid_slope_3_largest_gamma"] = slope(ib[1:, 0], ib[1:, 1])
    chi2 = np.array([(abs(q["g"]) * l0 / T_F) ** 2 for q in rows])
    r["I_max_resid_over_chi2"] = [float(np.max(np.array([t[1] for t in ibr]) / chi2)),
                                  float(np.max(np.array([t[2] for t in ibr]) / chi2))]
    log(f"(I) single level: |B| slope fg {r['I_fullgrip_break_size_slope']:.3f}, (a) {r['I_a_break_size_slope']:.3f}; "
        f"|B - B_1st| slope fg {r['I_fullgrip_break_resid_slope']:.3f} (3 largest gamma "
        f"{r['I_fullgrip_break_resid_slope_3_largest_gamma']:.3f}), (a) {r['I_a_break_resid_slope']:.3f}; "
        f"max |B - B_1st|/chi^2: fg {r['I_max_resid_over_chi2'][0]:.3f}, (a) {r['I_max_resid_over_chi2'][1]:.3f}")

    # (J) level and branch differences (3.17), eigenvalue weights
    jl = []
    for gam in gams:
        Q = {(q["M"], q["s"]): q for q in rows if q["gam"] == gam}
        nu = gam * n
        Fa = gam * n * F / (1 + nu)
        for M in M_LEV:          # branch pair (M,+),(M,-)
            p, m_ = Q[(M, 1)], Q[(M, -1)]
            g = gam * M
            Rfg = (p["w"] - m_["w"]) / ((p["Cm"] - m_["Cm"]) * F) - 1
            pfg = g**2 * (-2 * n * l0 / T_F * F2 + n**2 * F3) / F
            Ra = (p["w"] - m_["w"]) / ((2 * M + p["Cm"] - m_["Cm"]) * Fa) - 1
            pa = pfg + g**2 * (l0**2 - l20 / X) / (T_F**2 * (1 + nu))
            jl.append(("branch", gam, M, np.abs(Rfg - pfg).max() / np.abs(pfg).max(),
                       np.abs(Ra - pa).max() / np.abs(pa).max()))
        p, m_ = Q[(M_LEV[1], 1)], Q[(M_LEV[0], 1)]  # level pair, sigma=+1
        Rfg = (p["w"] - m_["w"]) / ((p["Cm"] - m_["Cm"]) * F) - 1
        pfg = (p["Cm"] + m_["Cm"]) * F2 / F
        Ra = (p["w"] - m_["w"]) / ((M_LEV[1] - M_LEV[0] + p["Cm"] - m_["Cm"]) * Fa) - 1
        pa = Ba1(gam * (M_LEV[0] + M_LEV[1]), nu)
        jl.append(("level", gam, None, np.abs(Rfg - pfg).max() / np.abs(pfg).max(),
                   np.abs(Ra - pa).max() / np.abs(pa).max()))
    r["J_rel_err_of_predicted_break_smallest_gamma"] = {
        f"{k}_{M}": [fg, a] for k, gm, M, fg, a in jl if gm == gams[0]}
    r["J_rel_err_of_predicted_break_largest_gamma"] = {
        f"{k}_{M}": [fg, a] for k, gm, M, fg, a in jl if gm == gams[-1]}
    log("(J) relative error of the predicted difference breaks at the smallest gamma "
        "[full grip, (a)]: " + ", ".join(f"{k}{'' if M is None else M}: {fg:.1e}, {a:.1e}"
                                        for k, gm, M, fg, a in jl if gm == gams[0]))
    log("    ... and at the largest gamma: " + ", ".join(f"{k}{'' if M is None else M}: {fg:.1e}, {a:.1e}"
                                                         for k, gm, M, fg, a in jl if gm == gams[-1]))

    # (T) coupling (a) with nu = gamma*n of order one: N_f from (3.1), one-object eigenvalues
    tl = {}
    for nu_t in NU_T:
        res, res0, gl = [], [], []
        for q in rows:
            g, gam, M, s, w, Cm = q["g"], q["gam"], q["M"], q["s"], q["w"], q["Cm"]
            sg = np.sign(nu_t)
            gp, sp_ = sg * gam, sg * s              # (gamma', sigma') with the same g_b
            Nf = max(1, int(round(abs(nu_t) * X / gam)))
            nn = Nf / X
            nu = gp * nn
            Ba = Nf * w / ((sp_ * M + Nf * Cm) * gp * nn * F / (1 + nu)) - 1
            chi, mu = abs(g) * l0 / T_F, abs(nu / (1 + nu))
            res.append(np.abs(Ba - Ba1(g, nu)).max() / (chi**2 * (1 + mu) ** 2))
            res0.append(np.abs(Ba - Ba1(g, 0.0)).max() / np.abs(Ba - Ba1(g, nu)).max())
            if M == M_LEV[1] and s == 1:
                gl.append((gam, np.abs(Ba - Ba1(g, nu)).max()))
        gl = np.array(gl)
        tl[str(nu_t)] = {"max_resid_over_chi2(1+|nu/(1+nu)|)^2": max(res),
                         "min_ratio_resid_nu0_to_resid_nu": min(res0), "resid_slope_in_gamma": slope(gl[:, 0], gl[:, 1])}
    r["T_nu_scan"] = tl
    log("(T) coupling (a), nu = gamma n: " + "; ".join(
        f"nu={k}: max |B-B_1st(nu)|/(chi^2(1+|nu/(1+nu)|)^2) = {v['max_resid_over_chi2(1+|nu/(1+nu)|)^2']:.2f}, "
        f"slope {v['resid_slope_in_gamma']:.2f}, |B-B_1st(0)|/|B-B_1st(nu)| >= {v['min_ratio_resid_nu0_to_resid_nu']:.0f}"
        for k, v in tl.items()))
    # nu = -1 exactly: gamma' = -|X|/N_f
    Nf = int(round(X / gams[1]))
    gp, M, y = -X / Nf, M_LEV[1], int(P[0])
    out = {}
    for sp_ in (1, -1):
        g = sp_ * gp * M
        base = C1 + point(X, 0, g)
        Cm = lowest_val(base) - eps00
        w = src_coef(base, X, y, h) - src_coef(base, X, ref, h)
        out[sp_] = (sp_ * M + Nf * Cm, Nf * w)
    pred = l0 * M**2 * gp / T_F
    r["T_nu_minus_one"] = {"N_f": Nf, "cost_+": out[1][0], "cost_-": out[-1][0], "cost_pred": pred,
                           "dW_+/cost_+": out[1][1] / out[1][0], "dW_-/cost_-": out[-1][1] / out[-1][0]}
    log(f"    nu=-1 (N_f={Nf}): Cost_+ = {out[1][0]:.5e}, Cost_- = {out[-1][0]:.5e}, -ell_0 M^2/(n t_f) = {pred:.5e}; "
        f"dW/Cost: + {out[1][1] / out[1][0]:.4e}, - {out[-1][1] / out[-1][0]:.4e}")
    return r, (co, C1, om, l1, l2, ap)


def full_operator_check(D, L, gam=0.05, m=1.0, Nclock=2):
    """(R) reduction (3.1): spectrum of the full contract (body labels sigma, a; field) at tau=0
    equals the union over (k, sigma) of theta*sigma*M_k + spec(C_1 + sigma*gam*M_k P_x + g_s P_xs)."""
    co, C1, om = graph(D, L)
    X = L**D
    lam0 = 2 * np.pi                                       # gives M_k = m + k/2
    fk = np.exp(2j * np.pi * np.outer(np.arange(Nclock), np.arange(Nclock)) / Nclock) / np.sqrt(Nclock)
    Dc = (2 * np.pi / (Nclock * lam0)) * fk @ np.diag(np.arange(Nclock)) @ fk.conj().T
    body = np.kron(np.diag([1.0, -1.0]), m * np.eye(Nclock) + Dc)   # sigma_3 (x) (m 1 + D)
    x, xs, gs = 0, X // 3, 1e-3
    Px = np.zeros((X, X)); Px[x, x] = 1
    Ps = np.zeros((X, X)); Ps[xs, xs] = 1
    out = {}
    Mk = m + np.arange(Nclock) / 2
    for theta, name in ((1, "a"), (0, "full_grip")):
        H = theta * np.kron(body, np.eye(X)) + gam * np.kron(body, Px) \
            + np.kron(np.eye(2 * Nclock), C1.toarray() + gs * Ps)
        full = np.sort(np.linalg.eigvalsh(H))
        red = np.sort(np.concatenate([theta * s * M + np.linalg.eigvalsh(C1.toarray() + s * gam * M * Px + gs * Ps)
                                      for s in (1, -1) for M in Mk]))
        out[name] = float(np.abs(full - red).max())
    log(f"(R) {D}D L={L}: full contract vs reduction (3.1), max |diff|: (a) {out['a']:.2e}, full grip {out['full_grip']:.2e}")
    return out


def asymptotics():
    """(S) large-distance forms of ell = Lambda^+ used in (3.9)-(3.11) and (3.16)."""
    res = {}
    for L in (64, 128, 256, 512):
        k = 2 * np.pi * np.arange(L) / L
        g1, g2 = np.meshgrid(k, k, indexing="ij")
        l1 = ellpow(4 * np.sin(g1 / 2) ** 2 + 4 * np.sin(g2 / 2) ** 2).reshape(L, L)
        res[f"2D_L{L}_ell0_minus_lnL_over_2pi"] = l1[0, 0] - np.log(L) / (2 * np.pi)
        if L == 512:   # ell(j,0) - [ell_0 - (ln j + gamma_E + 1.5 ln 2)/(2 pi) + j^2/(4 L^2)]
            res["2D_L512_ell(j)_minus_(3.10)_form"] = {
                j: l1[j, 0] - (l1[0, 0] - (np.log(j) + np.euler_gamma + 1.5 * np.log(2)) / (2 * np.pi)
                               + j**2 / (4 * L**2)) for j in (2, 4, 8, 16, 32, 64)}
    for L in (32, 64, 96):
        k = 2 * np.pi * np.arange(L) / L
        gr = np.meshgrid(k, k, k, indexing="ij")
        l1 = ellpow(sum(4 * np.sin(g / 2) ** 2 for g in gr)).reshape(L, L, L)
        res[f"3D_L{L}_ell0"] = l1[0, 0, 0]
        res[f"3D_L{L}_ell0_plus_xi3_over_L"] = l1[0, 0, 0] + XI3 / L
        if L == 96:    # ell(j,0,0) - [1/(4 pi j) - xi3/L + j^2/(6 L^3)], relative to 1/(4 pi j)
            res["3D_L96_rel_dev_of_ell(j)_from_(3.11)_form"] = {
                j: (l1[j, 0, 0] - (1 / (4 * np.pi * j) - XI3 / L + j**2 / (6 * L**3))) * 4 * np.pi * j
                for j in (2, 4, 8, 16, 24)}
    log("\n(S) asymptotics of ell: " + json.dumps({k: (v if not isinstance(v, dict) else
                                                     {kk: round(float(vv), 5) for kk, vv in v.items()})
                                                 for k, v in res.items()}, default=float))
    return res


def distance_scan(D, L, data):
    """(K) break against distance along a lattice axis, r' = antipode, from the eigenvector density;
    g_b*ell_0/t_f = +-0.05."""
    co, C1, om, l1, l2, ap = data
    X = L**D
    n = 1.0 / X
    l0 = l1[0]
    out = []
    log(f"\n(K) distance scan {D}D, L={L} (r' = antipode, density): j, B_fg(num), B_fg(1st order), B_a(num), "
        f"B_a(1st order), -(eta/2)(ell(r)+ell(r')) [fg], -(g_b/t_f)ell_0 [(a) far limit]")
    for s in (1, -1):
        g = s * 0.05 / l0
        gam, M = abs(g), 1.0
        nu = gam * n
        e, v = lowest(C1 + point(X, 0, g))
        Cm = e + 2 * D * T_F
        eta = Cm / (n * T_F)
        for j in range(1, L // 2 + 1):
            y = np.ravel_multi_index((j,) + (0,) * (D - 1), (L,) * D)
            if y == ap:
                continue
            Fy = -2 * (l1[y] - l1[ap]) / T_F
            F2y = (l1[y] ** 2 - l1[ap] ** 2 - 2 * (l2[y] - l2[ap]) / X) / (n * T_F**2)
            w = v[y] ** 2 - v[ap] ** 2
            Bfg = w / (Cm * Fy) - 1
            Fa = gam * n * Fy / (1 + nu)
            Ba = w / ((s * M + Cm) * Fa) - 1
            dThy = n**2 * F2y - n * l0 * Fy / (T_F * (1 + nu))
            row = [s, j, Bfg, Cm * F2y / Fy, Ba, g * dThy / (n * Fy), -eta / 2 * (l1[y] + l1[ap]), -g * l0 / T_F]
            out.append(row)
            log("  s=%+d j=%2d  % .4e  % .4e  % .4e  % .4e  % .4e  % .4e" % tuple(row))
    return out


def asym_scan(D, L, js):
    """(K2) breaks from exact eigenvalue weights for pairs r = j e_1, r' = 2j e_1 with 1 << |r|,|r'| << L,
    both levels and branches, against the first-order breaks (3.14), (3.15) and the forms (3.16)."""
    co, C1, om = graph(D, L)
    X = L**D
    n = 1.0 / X
    l1, l2 = ellpow(om, 1), ellpow(om, 2)
    l0 = l1[0]
    gam = 0.03 * T_F / (l0 * M_LEV[1])
    nu = gam * n
    h = 0.02 * T_F / l0
    idx = lambda j: int(np.ravel_multi_index((j,) + (0,) * (D - 1), (L,) * D))
    places = sorted(set(js) | {2 * j for j in js})
    out = []
    log(f"\n(K2) {D}D L={L}, r = j e1, r' = 2j e1, eigenvalue weights, max|g_b| ell_0/t_f = 0.03: "
        f"M, s, j, B_fg num, 1st, (3.16); B_a num, 1st, (3.16); |num-1st|/chi^2 [fg, a]; |1st-(3.16)|/(|eta| e) [fg, a]")
    for M in M_LEV:
        for s in (1, -1):
            g = s * gam * M
            base = C1 + point(X, 0, g)
            Cm = lowest_val(base) + 2 * D * T_F
            S = {j: src_coef(base, X, idx(j), h) for j in places}
            eta, chi = Cm / (n * T_F), abs(g) * l0 / T_F
            for j in js:
                a, b = idx(j), idx(2 * j)
                w = S[j] - S[2 * j]
                dl = l1[a] - l1[b]
                F = -2 * dl / T_F
                T2 = 2 * (l2[a] - l2[b]) / (X * dl)
                Bfg, Bfg1 = w / (Cm * F) - 1, -eta / 2 * (l1[a] + l1[b] - T2)
                Ba = w / ((s * M + Cm) * gam * n * F / (1 + nu)) - 1
                Ba1 = -g / (2 * T_F) * (l1[a] + l1[b] + 2 * l0 / (1 + nu) - T2)
                R, Rl = 2 * j, j
                if D == 1:     # r, r' << L form: -eta L/12 and -(g_b L/12 t_f)(1 + 1/(1+nu)); scale e = (|r|+|r'|)/3
                    Bfgas, Baas, e = -eta * L / 12, -g * L / (12 * T_F) * (1 + 1 / (1 + nu)), (j + 2 * j) / 3
                elif D == 2:
                    Bfgas = -eta / (4 * np.pi) * (np.log(L**2 / (j * 2 * j)) + 2 * KAPPA2)
                    Baas = Bfgas * (g / T_F) / eta - g * l0 / ((1 + nu) * T_F)
                    e = Rl**-2 + R**2 * np.log(L / R) / L**2
                else:
                    Bfgas = -eta / (8 * np.pi) * (1 / j + 1 / (2 * j)) + eta * XI3 / L
                    Baas = -g / T_F * ((1 / j + 1 / (2 * j)) / (8 * np.pi) - XI3 / L + l0 / (1 + nu))
                    e = Rl**-3 + R**2 / L**3
                row = [M, s, j, Bfg, Bfg1, Bfgas, Ba, Ba1, Baas, abs(Bfg - Bfg1) / chi**2, abs(Ba - Ba1) / chi**2,
                       abs(Bfg1 - Bfgas) / (abs(eta) * e), abs(Ba1 - Baas) / (abs(eta) * e)]
                out.append(row)
                log("  M=%.1f s=%+d j=%2d  % .4e % .4e % .4e | % .4e % .4e % .4e | %.2f %.2f | %.2f %.2f" % tuple(row))
    return out


def coeff_asymptotics():
    """(U) lattice sums behind the large-distance errors: square torus 2[l2]/(|X|[l]) against
    R^2 ln(L/R)/L^2; cubic torus 2[l2]/(|X|[l]) against |r||r'|/L^3 and the branch-pair coefficient
    t_f^2 (n^2 F_3 - 2 n l0 F_2/t_f)/F against l0 (l(r) + l(r') - |r||r'|/L^3); r = j e1, r' = 2j e1."""
    res = {}
    for L in (64, 128, 256, 512):
        k = 2 * np.pi * np.arange(L) / L
        g1, g2 = np.meshgrid(k, k, indexing="ij")
        om = 4 * np.sin(g1 / 2) ** 2 + 4 * np.sin(g2 / 2) ** 2
        l1, l2 = ellpow(om, 1).reshape(L, L), ellpow(om, 2).reshape(L, L)
        for j in (2, 4, 8):
            R = 2 * j
            T2 = 2 * (l2[j, 0] - l2[R, 0]) / (L**2 * (l1[j, 0] - l1[R, 0]))
            res[f"2D_L{L}_j{j}"] = {"T2*L^2/R^2": T2 * L**2 / R**2, "T2*L^2/(R^2 ln(L/R))": T2 * L**2 / (R**2 * np.log(L / R))}
    for L in (32, 64, 128):
        k = 2 * np.pi * np.arange(L) / L
        gr = np.meshgrid(k, k, k, indexing="ij")
        om = sum(4 * np.sin(g / 2) ** 2 for g in gr)
        l1, l2, l3 = (ellpow(om, p).reshape(L, L, L) for p in (1, 2, 3))
        X, l0, l20 = L**3, l1[0, 0, 0], l2[0, 0, 0]
        for j in (2, 4, 8):
            R = 2 * j
            if R > L // 4:
                continue
            a, b = (j, 0, 0), (R, 0, 0)
            dl = l1[a] - l1[b]
            T2 = 2 * (l2[a] - l2[b]) / (X * dl)
            num3 = 2 * (l1[a] * l2[a] - l1[b] * l2[b] + l20 * dl - (l3[a] - l3[b]) / X) / X
            num2 = l1[a] ** 2 - l1[b] ** 2 - 2 * (l2[a] - l2[b]) / X
            Kbr = (num3 - 2 * l0 * num2) / (-2 * dl)
            lead, corr = l0 * (l1[a] + l1[b]), l0 * j * R / L**3
            res[f"3D_L{L}_j{j}"] = {"T2*L^3/(|r||r'|)": T2 * L**3 / (j * R),
                                    "(K_br-l0(l+l'))*L^2": (Kbr - lead) * L**2,
                                    "(K_br-l0(l+l'-|r||r'|/L^3))*L^2": (Kbr - lead + corr) * L**2,
                                    "(K_br-l0(l+l'))/(l0|r||r'|/L^3)": (Kbr - lead) / corr}
    log("\n(U) lattice sums: " + json.dumps({k: {kk: round(float(vv), 4) for kk, vv in v.items()}
                                              for k, v in res.items()}))
    return res


if __name__ == "__main__":
    data = {}
    for D, Ls in SIZES.items():
        for L in Ls:
            RES[f"D{D}_L{L}"], data[(D, L)] = run_graph(D, L)
    scans = {}
    for D, Ls in SIZES.items():
        scans[f"D{D}_L{Ls[-1]}"] = distance_scan(D, Ls[-1], data[(D, Ls[-1])])
    # larger cubic torus for the distance dependence (sparse Lanczos)
    co, C1, om = graph(3, 20)
    l1, l2 = ellpow(om, 1), ellpow(om, 2)
    ap = int(np.ravel_multi_index((10, 10, 10), (20,) * 3))
    RES["D3_L20"] = {"ell_0": l1[0]}
    log(f"\n=== D3_L20: ell_0={l1[0]:.6f}")
    scans["D3_L20"] = distance_scan(3, 20, (co, C1, om, l1, l2, ap))
    RES["distance_scans_columns"] = ["sigma", "j", "B_fg_num", "B_fg_1st", "B_a_num", "B_a_1st",
                                     "-(eta/2)(ell(r)+ell(r'))", "-(g_b/t_f)ell_0"]
    RES["distance_scans"] = scans
    RES["K2_columns"] = ["M", "sigma", "j", "B_fg_num", "B_fg_1st", "B_fg_(3.16)", "B_a_num", "B_a_1st", "B_a_(3.16)",
                         "|B_fg_num-1st|/chi^2", "|B_a_num-1st|/chi^2", "|B_fg_1st-(3.16)|/(|eta| e)",
                         "|B_a_1st-(3.16)|/(|eta| e)"]
    RES["K2_asymptotic_regime_scans"] = {f"D{D}_L{L}": asym_scan(D, L, js)
                                         for D, L, js in ((1, 128, (2, 4, 8, 16)), (2, 48, (2, 3, 4, 6)),
                                                          (3, 32, (2, 3, 4)))}
    RES["U_lattice_sums"] = coeff_asymptotics()
    log("")
    RES["R_reduction_full_operator"] = {f"D{D}_L{L}": full_operator_check(D, L)
                                        for D, L in ((1, 32), (2, 8), (3, 6))}
    RES["S_asymptotics"] = asymptotics()

    def clean(o):
        if isinstance(o, dict):
            return {str(k): clean(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [clean(v) for v in o]
        if isinstance(o, (np.floating, np.integer)):
            return o.item()
        if isinstance(o, np.ndarray):
            return clean(o.tolist())
        return o
    (OUT / "check_results.json").write_text(json.dumps(clean(RES), indent=1), encoding="utf-8")
    (OUT / "check_log.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
