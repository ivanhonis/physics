"""Check for 07-ilang-weight/03-weight-of-mark, derivation v1.

One field object (N_f = 1, n = 1/|X|) on a ring, a square torus and a cubic torus.
Held body: point term g_b P_x, g_b = sigma*gamma*M_k; held source: point term g_s P_xs.
Exact diagonalization is compared with the closed forms of the derivation:
cost (3.2), (3.4), (3.5); weight (3.6)-(3.8); ring form (7.6); weight against cost
(3.12)-(3.17); mirror (3.18). Outputs: output/check_log.txt, output/check_results.json.
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
GHAT = (0.005, 0.01, 0.02, 0.04)        # targets for max |g_b| * ell_0 / t_f
SIZES = {1: (32, 64), 2: (12, 20), 3: (8, 12)}
LOG, RES = [], {}


def log(s=""):
    print(s)
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
    if H.shape[0] <= 2000:
        if vec:
            w, v = np.linalg.eigh(H.toarray())
            return w[0], v[:, 0]
        return np.linalg.eigvalsh(H.toarray())[0], None
    w, v = eigsh(H, k=1, which="SA", tol=0)
    return w[0], v[:, 0]


def point(n, i, g):
    return sp.csr_matrix(([g], ([i], [i])), shape=(n, n))


def exact_rho(om, g, X):
    """Lowest eigenpair of C_1 + g P_0 from (3.2)-(3.3): returns delta, eta, rho(y)."""
    wmin = om[om > 1e-12].min()
    f = lambda d: 1.0 / (X * d) - ellpow(om, 1, d / T_F)[0] / T_F - 1.0 / g
    d = brentq(f, 1e-14, T_F * wmin * (1 - 1e-12)) if g > 0 else brentq(f, -1e3, -1e-14)
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
    ap = int(np.ravel_multi_index((L // 2,) * D, (L,) * D))   # antipode: r' of the pairs
    F = -2 * (l1 - l1[ap]) / T_F                              # F / g_s, (3.13)
    F2 = (l1**2 - l1[ap] ** 2 - 2 * (l2 - l2[ap]) / X) / (n * T_F**2)
    F3 = 2 * (l1 * l2 - l1[ap] * l2[ap] + l20 * (l1 - l1[ap]) - (l3 - l3[ap]) / X) / (n**2 * T_F**3 * X)
    dN = n * F                                                # [dN(x)-dN(x')]/g_s
    dTh = n**2 * F2 - n * l0 * F / T_F                        # [Theta_D(x)-Theta_D(x')]/g_s, (3.8)
    mask = np.arange(X) != ap
    eps00 = -2 * D * T_F
    r = {"L": L, "D": D, "X": X, "ell_0": l0, "ell2_0": l20}
    log(f"\n=== {tag}: |X|={X}, ell_0={l0:.6f}, ell2_0/|X|={l20 / X:.6e}")

    # (A) weight from eigenvalues with both point terms vs Hellmann-Feynman density
    gb = 0.02 / l0
    _, v = lowest(C1 + point(X, 0, gb))
    rho_hf = v**2
    errs = {}
    rng = np.random.default_rng(D * 100 + L)
    pl = [(int(x), int(xs)) for x, xs in rng.integers(0, X, size=(4, 2))]
    for gs in (1e-3, 5e-4):
        e = 0.0
        for x, xs in pl:
            ep = lowest(C1 + point(X, x, gb) + point(X, xs, gs), vec=False)[0]
            em = lowest(C1 + point(X, x, gb) + point(X, xs, -gs), vec=False)[0]
            ydisp = np.ravel_multi_index(tuple((co[xs] - co[x]) % L), (L,) * D)
            e = max(e, abs((ep - em) / (2 * gs) - rho_hf[ydisp]) / rho_hf.max())
        errs[gs] = e
    r["A_eig_vs_HF_relerr"] = errs
    log(f"(A) eigenvalue weight vs HF density, max rel err: g_s=1e-3: {errs[1e-3]:.2e}, g_s=5e-4: {errs[5e-4]:.2e}")

    # mirror (3.18): highest eigenvalue = - lowest of mirrored signs (L even, bipartite)
    gs = 1e-3
    Hp = (C1 + point(X, 0, gb) + point(X, 3 % X, gs))
    Hm = (C1 + point(X, 0, -gb) + point(X, 3 % X, -gs))
    top = -lowest(-Hp, vec=False)[0]
    r["mirror_err"] = abs(top + lowest(Hm, vec=False)[0])
    log(f"(M) highest state = -(lowest, mirrored signs): |diff| = {r['mirror_err']:.2e}")

    # scans over levels, branches and gamma
    gams = np.array(GHAT) * T_F / (l0 * max(M_LEV))
    rows = []
    for gam in gams:
        for M in M_LEV:
            for s in (1, -1):
                g = s * gam * M
                e, v = lowest(C1 + point(X, 0, g))
                d, eta, rho_ex = exact_rho(om, g, X)
                Cm = e - eps00                                   # mark cost, (3.4)
                w = v**2 - v[ap] ** 2                            # [W(x)-W(x')]/g_s, (3.6)
                rows.append(dict(gam=gam, M=M, s=s, g=g, Cm=Cm, w=w,
                                 cost_ex_err=abs(Cm - d), rho_ex_err=np.abs(v**2 - rho_ex).max() * X))
    r["B_rho_exact_maxrelerr"] = max(q["rho_ex_err"] for q in rows)
    r["C_cost_exact_maxerr"] = max(q["cost_ex_err"] for q in rows)
    log(f"(B) density vs exact form (3.3): max |X|*|diff| = {r['B_rho_exact_maxrelerr']:.2e}")
    log(f"(C) cost vs exact root (3.2): max |diff| = {r['C_cost_exact_maxerr']:.2e}")

    # (D),(E),(H) deviations from the expansions, scaling in gamma (level M=1.5, sigma=+1)
    sel = [q for q in rows if q["M"] == M_LEV[1] and q["s"] == 1]
    gg = np.array([q["g"] for q in sel])
    devC = [abs(q["Cm"] - (n * q["g"] - n * q["g"] ** 2 * l0 / T_F)) for q in sel]
    devW = [np.abs(q["w"] - (q["g"] * dN + q["g"] ** 2 * dTh))[mask].max() for q in sel]
    devU = [np.abs(q["w"] - (F * q["Cm"] + F2 * q["Cm"] ** 2 + F3 * q["Cm"] ** 3))[mask].max() for q in sel]
    r["D_cost_2nd_slope"] = slope(gg, devC)
    r["E_weight_2nd_slope"] = slope(gg, devW)
    r["H_W_of_C_3rd_slope"] = slope(gg, devU)
    log(f"(D) cost minus 2nd-order (3.5): slope in gamma = {r['D_cost_2nd_slope']:.3f}; devs {np.array(devC)}")
    log(f"(E) weight minus 2nd-order (3.8): slope = {r['E_weight_2nd_slope']:.3f}; devs {np.array(devW)}")
    log(f"(H) weight minus F C + F2 C^2 + F3 C^3 (3.12)-(3.13): slope = {r['H_W_of_C_3rd_slope']:.3f}")

    # (F) ring: Theta_D of (3.8) against Theta of (7.6)
    if D == 1:
        rr = np.arange(L)
        u = rr * (L - rr)
        th76 = n / (3 * L**2 * T_F**2) * (u**2 - (L**2 - 2) / 2 * u)
        diff = dTh - (th76 - th76[ap])
        r["F_ring_Theta_vs_7.6_maxdiff"] = float(np.abs(diff).max())
        log(f"(F) ring: Theta_D - Theta(7.6): max |diff| = {r['F_ring_Theta_vs_7.6_maxdiff']:.2e}")

    # (I) single-level break: B = dW/(Cost*F_c) - 1, both couplings
    ibr = []
    for q in rows:
        g, gam, M, s = q["g"], q["gam"], q["M"], q["s"]
        Bfg = q["w"][mask] / (q["Cm"] * F[mask]) - 1
        pfg = (q["Cm"] * F2 / F)[mask]
        cost_a = s * M + q["Cm"]
        Fa = gam * n * F / (1 + gam * n)
        Ba = q["w"][mask] / (cost_a * Fa[mask]) - 1
        pa = (g * dTh / dN)[mask]
        ibr.append((gam, np.abs(Bfg - pfg).max(), np.abs(Ba - pa).max(), np.abs(Bfg).max(), np.abs(Ba).max()))
    ib = np.array([t for t, q in zip(ibr, rows) if q["M"] == M_LEV[1] and q["s"] == 1])
    r["I_fullgrip_break_resid_slope"] = slope(ib[:, 0], ib[:, 1])
    r["I_a_break_resid_slope"] = slope(ib[:, 0], ib[:, 2])
    r["I_fullgrip_break_size_slope"] = slope(ib[:, 0], ib[:, 3])
    r["I_a_break_size_slope"] = slope(ib[:, 0], ib[:, 4])
    log(f"(I) single level: |B| slope fg {r['I_fullgrip_break_size_slope']:.3f}, (a) {r['I_a_break_size_slope']:.3f}; "
        f"|B - B_1st| slope fg {r['I_fullgrip_break_resid_slope']:.3f}, (a) {r['I_a_break_resid_slope']:.3f}")

    # (J) level and branch differences (3.17)
    jl = []
    for gam in gams:
        Q = {(q["M"], q["s"]): q for q in rows if q["gam"] == gam}
        Fa = gam * n * F / (1 + gam * n)
        for M in M_LEV:          # branch pair (M,+),(M,-)
            p, m_ = Q[(M, 1)], Q[(M, -1)]
            g = gam * M
            Rfg = (p["w"] - m_["w"])[mask] / ((p["Cm"] - m_["Cm"]) * F[mask]) - 1
            pfg = (g**2 * (-2 * n * l0 / T_F * F2 + n**2 * F3) / F)[mask]
            Ra = (p["w"] - m_["w"])[mask] / ((2 * M + p["Cm"] - m_["Cm"]) * Fa[mask]) - 1
            pa = pfg + g**2 * (l0**2 - l20 / X) / T_F**2
            jl.append(("branch", gam, M, np.abs(Rfg - pfg).max() / np.abs(pfg).max(),
                       np.abs(Ra - pa).max() / np.abs(pa).max()))
        p, m_ = Q[(M_LEV[1], 1)], Q[(M_LEV[0], 1)]  # level pair, sigma=+1
        Rfg = (p["w"] - m_["w"])[mask] / ((p["Cm"] - m_["Cm"]) * F[mask]) - 1
        pfg = ((p["Cm"] + m_["Cm"]) * F2 / F)[mask]
        Ra = (p["w"] - m_["w"])[mask] / ((M_LEV[1] - M_LEV[0] + p["Cm"] - m_["Cm"]) * Fa[mask]) - 1
        pa = (gam * (M_LEV[0] + M_LEV[1]) * dTh / dN)[mask]
        jl.append(("level", gam, None, np.abs(Rfg - pfg).max() / np.abs(pfg).max(),
                   np.abs(Ra - pa).max() / np.abs(pa).max()))
    r["J_rel_err_of_predicted_break_smallest_gamma"] = {
        f"{k}_{M}": [fg, a] for k, gm, M, fg, a in jl if gm == gams[0]}
    log("(J) relative error of the predicted difference breaks at the smallest gamma "
        "[full grip, (a)]: " + ", ".join(f"{k}{'' if M is None else M}: {fg:.1e}, {a:.1e}"
                                        for k, gm, M, fg, a in jl if gm == gams[0]))
    log("    ... and at the largest gamma: " + ", ".join(f"{k}{'' if M is None else M}: {fg:.1e}, {a:.1e}"
                                                         for k, gm, M, fg, a in jl if gm == gams[-1]))
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
        k =2 * np.pi * np.arange(L) / L
        g1, g2 = np.meshgrid(k, k, indexing="ij")
        l1 = ellpow(4 * np.sin(g1 / 2) ** 2 + 4 * np.sin(g2 / 2) ** 2).reshape(L, L)
        res[f"2D_L{L}_ell0_minus_lnL_over_2pi"] = l1[0, 0] - np.log(L) / (2 * np.pi)
        if L == 512:   # ell(j,0) - [ell_0 - (ln j + gamma_E + 1.5 ln 2)/(2 pi) + j^2/(4 L^2)]
            res["2D_L512_ell(j)_minus_(3.10)_form"] = {
                j: l1[j, 0] - (l1[0, 0] - (np.log(j) + np.euler_gamma + 1.5 * np.log(2)) / (2 * np.pi)
                               + j**2 / (4 * L**2)) for j in (2, 4, 8, 16, 32, 64)}
    xi3 = 2.837297 / (4 * np.pi)
    for L in (32, 64, 96):
        k = 2 * np.pi * np.arange(L) / L
        gr = np.meshgrid(k, k, k, indexing="ij")
        l1 = ellpow(sum(4 * np.sin(g / 2) ** 2 for g in gr)).reshape(L, L, L)
        res[f"3D_L{L}_ell0"] = l1[0, 0, 0]
        res[f"3D_L{L}_ell0_plus_xi3_over_L"] = l1[0, 0, 0] + xi3 / L
        if L == 96:    # ell(j,0,0) - [1/(4 pi j) - xi3/L + j^2/(6 L^3)], relative to 1/(4 pi j)
            res["3D_L96_rel_dev_of_ell(j)_from_(3.11)_form"] = {
                j: (l1[j, 0, 0] - (1 / (4 * np.pi * j) - xi3 / L + j**2 / (6 * L**3))) * 4 * np.pi * j
                for j in (2, 4, 8, 16, 24)}
    log("\n(S) asymptotics of ell: " + json.dumps({k: (v if not isinstance(v, dict) else
                                                     {kk: round(float(vv), 5) for kk, vv in v.items()})
                                                 for k, v in res.items()}, default=float))
    return res


def distance_scan(D, L, data):
    """(K) break against distance along a lattice axis, r' = antipode; g_b*ell_0/t_f = +-0.05."""
    co, C1, om, l1, l2, ap = data
    X = L**D
    n = 1.0 / X
    l0 = l1[0]
    out = []
    log(f"\n(K) distance scan {D}D, L={L}: j, B_fg(num), B_fg(1st order), B_a(num), B_a(1st order), "
        f"-(eta/2)(ell(r)+ell(r')) [fg], -(g_b/t_f)ell_0 [(a) far limit]")
    for s in (1, -1):
        g = s * 0.05 / l0
        gam, M = abs(g), 1.0
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
            Fa = gam * n * Fy / (1 + gam * n)
            Ba = w / ((s * M + Cm) * Fa) - 1
            dThy = n**2 * F2y - n * l0 * Fy / T_F
            row = [s, j, Bfg, Cm * F2y / Fy, Ba, g * dThy / (n * Fy), -eta / 2 * (l1[y] + l1[ap]), -g * l0 / T_F]
            out.append(row)
            log("  s=%+d j=%2d  % .4e  % .4e  % .4e  % .4e  % .4e  % .4e" % tuple(row))
    return out


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
        return o
    (OUT / "check_results.json").write_text(json.dumps(clean(RES), indent=1), encoding="utf-8")
    (OUT / "check_log.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
