"""Check of item 4 of 07-ilang-weight/06-inertia-of-pair against exact eigenvalues with a held source.

Two Model D bodies and N_f = 1 field object on a ring of L places (set A of check_inertia.py),
plus a held source g_s Phi_{x_s}.  The exact contract (all places, no sector) is diagonalized near
the bottom of the bound band, where the bound pair sits in the weight well opposite the source.
Its levels are compared with
  (i)   the first-order projected contract on the exact bound band: E_b(P_k) + <P',v_P'| g_s Phi_xs |P,v_P>,
        with the exact P-dependent sector eigenvectors v_P (no frozen relative profile);
  (ii)  the frozen-profile description E_b(P) + W_nu(X) with W_nu of (6.11) (profile f_nu at P = 0);
  (iii) the same with the pair band rescaled to the inertia mu_1 + mu_2.
Second part: the acceleration from rest (6.13) of the centre Y conjugate to P, computed exactly from the
double commutator in the position-space band contract (order tau^2, first-order held weights), against
-E''_line sum phi^2 W'_nu, and the acceleration of the midpoint against -(beta/2) sum phi^2 (W_1'/mu_1 + W_2'/mu_2).
"""
import json
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla

from check_inertia import (OUT, J, SG, bodies, bidx, ground, field_hop, pair_block, band_data,
                           body_data, curvature)


def full_contract(L, tf, b1, b2, cpl, gs, xs, par):
    """Exact contract on all places, restricted to the block (-1)^(x2-x1) s1 s2 of the band G."""
    cc = 1.0 if cpl == "c" else 0.0
    ix = lambda x1, s1, x2, s2, y: (((x1 * 2 + s1) * L + x2) * 2 + s2) * L + y
    pi0 = (-1) ** par * b1["sig"] * b2["sig"]
    states = [(x1, s1, x2, s2, y) for x1 in range(L) for s1 in range(2) for x2 in range(L) for s2 in range(2)
              for y in range(L) if (-1) ** ((x2 - x1) % L) * SG[s1] * SG[s2] == pi0]
    pos = {ix(*s): i for i, s in enumerate(states)}
    rows, cols, vals = [], [], []
    def add(i, st, v):
        j = pos[ix(*st)]
        rows.append(j); cols.append(i); vals.append(v)
    for i, (x1, s1, x2, s2, y) in enumerate(states):
        add(i, (x1, s1, x2, s2, y), SG[s1] * b1["M"] * (1 + b1["gam"] * (y == x1))
            + SG[s2] * b2["M"] * (1 + b2["gam"] * (y == x2)) + gs * (y == xs))
        for dy in (1, -1):
            add(i, (x1, s1, x2, s2, (y + dy) % L), -tf)
        t1, t2 = 1 - s1, 1 - s2  # a motion term flips the branch (J has zero diagonal)
        for dx in (1, -1):
            # body hop x -> x+dx (bond between x and x+dx); J for right hops, J^T for left hops
            Jm = J[t1, s1] if dx == 1 else J[s1, t1]
            f = 1 + cc * b1["gam"] * 0.5 * ((y == x1) + (y == (x1 + dx) % L))
            add(i, ((x1 + dx) % L, t1, x2, s2, y), 0.5 * b1["tau"] * Jm * f)
            Jm = J[t2, s2] if dx == 1 else J[s2, t2]
            f = 1 + cc * b2["gam"] * 0.5 * ((y == x2) + (y == (x2 + dx) % L))
            add(i, (x1, s1, (x2 + dx) % L, t2, y), 0.5 * b2["tau"] * Jm * f)
    H = sp.csr_matrix((vals, (rows, cols)), shape=(len(states), len(states)))
    assert abs(H - H.T).max() < 1e-14
    return H, states, pos, ix


def sector_state(blk, mode, P):
    """Exact bound level and eigenvector of the sector contract H(P) (body 1 as representative)."""
    H0, B1, V2, U0, w0, gi, rs = blk
    G = U0[:, gi]
    w, v = np.linalg.eigh(H0 + V2 + np.exp(-1j * P) * B1 + np.exp(1j * P) * B1.T)
    c = np.where((np.abs(G.T @ v) ** 2).sum(0) > 0.5)[0]
    k = c[np.argmin(w[c])] if mode == "low" else c[np.argmax(w[c])]
    return w[k], v[:, k]


def held_weights(L, tf, b1, b2, gs, xs=0):
    """First-order held weights: pair W(j,l) = g_s |Omega_jl(x_s)|^2 and single bodies W_i(x)."""
    hf = field_hop(L, tf)
    Om, Wpair = {}, np.zeros((L, L))
    for j in range(L):
        for l in range(L):
            h = hf.copy(); h[j, j] += b1["sig"] * b1["gam"] * b1["M"]; h[l, l] += b2["sig"] * b2["gam"] * b2["M"]
            _, o = ground(h)
            Om[(j, l)] = o
            Wpair[j, l] = gs * o[xs] ** 2
    W1, W2 = np.zeros(L), np.zeros(L)
    for x in range(L):
        h = hf.copy(); h[x, x] += b1["sig"] * b1["gam"] * b1["M"]; W1[x] = gs * ground(h)[1][xs] ** 2
        h = hf.copy(); h[x, x] += b2["sig"] * b2["gam"] * b2["M"]; W2[x] = gs * ground(h)[1][xs] ** 2
    return Om, Wpair, W1, W2


def run(L, tf, cpl, gs, nlev=4):
    b1, b2, par, mode = bodies("A", L, cpl)
    xs = 0
    s1g, s2g = bidx(b1["sig"]), bidx(b2["sig"])
    Om, Wpair, W1, W2 = held_weights(L, tf, b1, b2, gs, xs)
    # relative level f_nu (band contract, P = 0) and the pair weight W_nu(X), (6.11)
    bd = band_data(L, tf, b1, b2, cpl, par, mode)
    rsg = [((r + L // 2) % L) - L // 2 for r in bd["rs"]]  # signed separations
    Wnu = np.array([sum(bd["f"][k] ** 2 * Wpair[(X - r // 2) % L, (X + r // 2) % L] for k, r in enumerate(rsg))
                    for X in range(L)])
    # exact bound band: levels E_b(P_k) and P-dependent sector eigenvectors v_P
    blk = pair_block(L, tf, b1, b2, cpl, par)
    Ps = 2 * np.pi * np.arange(L) / L
    sts = [sector_state(blk, mode, P) for P in Ps]
    Eb = np.array([s[0] for s in sts]); Vb = np.array([s[1] for s in sts]).T
    # (i) projected contract: <P',v'|Phi_xs|P,v> = (1/L) sum_x e^{i(P-P')x} <v'|Phi_{xs-x}|v>_frame
    yof = np.tile(np.arange(L), Vb.shape[0] // L)
    Wp = np.zeros((L, L), complex)
    for x in range(L):
        sel = yof == (xs - x) % L
        rho = Vb[sel].conj().T @ Vb[sel]
        Wp += np.exp(1j * (Ps[None, :] - Ps[:, None]) * x) * rho
    Wp *= gs / L
    assert np.abs(Wp - Wp.conj().T).max() < 1e-12
    Eproj = np.linalg.eigvalsh(np.diag(Eb) + Wp)[:nlev]
    # (ii), (iii) frozen-profile descriptions
    F = np.exp(1j * np.outer(np.arange(L), Ps)) / np.sqrt(L)  # <X|P_k>
    _, Epp, _, _ = curvature(bd["H0"] + bd["V2"], bd["B1"], bd["U0"][:, bd["gi"]], mode)
    d1, d2 = body_data(L, tf, b1, cpl), body_data(L, tf, b2, cpl)
    mu = d1["mu"] + d2["mu"]
    s_free = 1 / (mu * Epp)  # rescales the band curvature to 1/(mu_1 + mu_2)
    model = lambda Eband: np.linalg.eigvalsh(F @ np.diag(Eband) @ F.conj().T + np.diag(Wnu))[:nlev]
    Em = model(Eb)
    Ealt = model(Eb[0] + s_free * (Eb - Eb[0]))
    # exact contract with the source, levels near the bottom of the bound band, filtered by G-weight
    H, states, pos, ix = full_contract(L, tf, b1, b2, cpl, gs, xs, par)
    target = Em[0] - 0.3 * (Em[1] - Em[0])
    w, v = sla.eigsh(H, k=3 * nlev, sigma=target, which="LM")
    Gw = np.zeros(len(w))
    for (j, l), o in Om.items():
        if (l - j) % 2 != par:
            continue
        idx = [pos[ix(j, s1g, l, s2g, y)] for y in range(L)]
        Gw += np.abs(o @ v[idx, :]) ** 2
    ex = np.sort(w[Gw > 0.5])[:nlev]
    X = L // 4
    dWnu = (Wnu[X + 1] - Wnu[X - 1]) / 2
    dW1, dW2 = (W1[X + 1] - W1[X - 1]) / 2, (W2[X + 1] - W2[X - 1]) / 2
    return dict(L=L, coupling=cpl, g_s=gs, exact_levels=ex.tolist(), proj_levels=Eproj.tolist(),
                model_levels=Em.tolist(), alt_levels=Ealt.tolist(), exact_spacings=np.diff(ex).tolist(),
                proj_spacings=np.diff(Eproj).tolist(), model_spacings=np.diff(Em).tolist(),
                alt_spacings=np.diff(Ealt).tolist(), beta=float(bd["b"].sum()), s_free=float(s_free),
                max_abs_dev_proj=float(np.max(np.abs(ex - Eproj))), max_abs_dev_model=float(np.max(np.abs(ex - Em))),
                G_weights=np.sort(Gw)[::-1][:nlev].tolist(),
                dWnu_over_dW1_plus_dW2=float(dWnu / (dW1 + dW2)), Epp_times_mu_sum=float(Epp * mu),
                Pi_pair_over_weighted_single=float(Epp * dWnu * mu / (dW1 + dW2)))


def accel_test(name, L, tf, cpl, gs, widths=(1.0, 1.5, 2.0), wscales=(1.0, 0.05)):
    """Acceleration from rest (6.13) in the position-space band contract with first-order held weights.
    wscale < 1 scales the couplings g_i inside the held weights only (band contract and f_nu unchanged), to
    isolate the first order in g_i of the weights, on which the last step of (6.13) rests."""
    b1, b2, par, mode = bodies(name, L, cpl)
    bd = band_data(L, tf, b1, b2, cpl, par, mode)
    rs = list(bd["rs"]); nr = len(rs); idx = {r: k for k, r in enumerate(rs)}
    K1, K2, Ea, f = bd["K1"], bd["K2"], bd["Ea"], bd["f"]
    I = lambda j, r: (j % L) * nr + idx[r % L]
    N = L * nr
    H = np.zeros((N, N))
    for j in range(L):
        for k, r in enumerate(rs):
            a = I(j, r)
            H[a, a] += Ea[k] + K1[k, k] + K2[k, k]
            H[I(j + 2, r - 2), a] += K1[idx[(r - 2) % L], k]   # body 1 by +2
            H[I(j - 2, r + 2), a] += K1[idx[(r + 2) % L], k]   # body 1 by -2
            H[I(j, r + 2), a] += K2[idx[(r + 2) % L], k]       # body 2 by +2
            H[I(j, r - 2), a] += K2[idx[(r - 2) % L], k]       # body 2 by -2
    assert np.abs(H - H.T).max() < 1e-15
    H -= np.mean(np.diag(H)) * np.eye(N)  # a constant does not enter the commutators; reduces round-off
    data = {}
    for ws in wscales:
        b1w, b2w = dict(b1, gam=b1["gam"] * ws), dict(b2, gam=b2["gam"] * ws)
        data[ws] = held_weights(L, tf, b1w, b2w, gs)[1:]
    # theta'(r): theta'(r+2) - theta'(r) = (k1 - k2)/(k1 + k2) at rho = r + 1, theta' odd (even class)
    k1, k2 = bd["k1"], bd["k2"]
    step = {(rs[j] + 1) % L: (k1[j] - k2[j]) / (k1[j] + k2[j]) for j in range(nr)}
    sgn = lambda r: ((r + L // 2) % L) - L // 2
    th = {0: 0.0}
    for r in range(2, L // 2 + 1, 2):
        th[r] = th[r - 2] + step[(r - 1) % L]
        th[-r] = th[-r + 2] - step[(-r + 1) % L]
    x0 = L // 4
    Xu = np.zeros(N); Y = np.zeros(N); Fr = np.zeros(N); Rs = np.zeros(N)
    for j in range(L):
        for k, r in enumerate(rs):
            rsn = sgn(r)
            Xc = j + rsn / 2
            Xc = x0 + ((Xc - x0 + L / 2) % L) - L / 2
            a = I(j, r)
            Xu[a], Y[a], Fr[a], Rs[a] = Xc, Xc + th[rsn], f[k], rsn
    rsg = [sgn(r) for r in rs]
    Xg = np.arange(x0 - L // 2 + 2, x0 + L // 2 - 1)
    beta, Eline = bd["b"].sum(), np.sum(bd["b"] / bd["m"])
    d1, d2 = body_data(L, tf, b1, cpl), body_data(L, tf, b2, cpl)
    out = []
    for ws, (Wpair, W1, W2) in data.items():
        Wb = np.array([Wpair[j, (j + r) % L] for j in range(L) for r in rs])
        Wnu = lambda X: sum(f[k] ** 2 * Wpair[int(X - rr // 2) % L, int(X + rr // 2) % L] for k, rr in enumerate(rsg))
        dWnu = np.array([(Wnu(X + 1) - Wnu(X - 1)) / 2 for X in Xg])
        dW1 = np.array([(W1[(X + 1) % L] - W1[(X - 1) % L]) / 2 for X in Xg])
        dW2 = np.array([(W2[(X + 1) % L] - W2[(X - 1) % L]) / 2 for X in Xg])
        for wd in widths:
            psi = np.exp(-(Y - x0) ** 2 / (4 * wd ** 2)) * Fr
            psi /= np.linalg.norm(psi)
            acc = lambda Ht, Z: -psi @ (Ht @ Ht @ (Z * psi) - 2 * Ht @ (Z * (Ht @ psi)) + Z * (Ht @ Ht @ psi))
            Ht = H + np.diag(Wb)
            # a is linear in W exactly ([W,[W,Z]] = 0 for diagonal W, Z): a = a(g_s=0) + first order in g_s
            aY, a0, amid, am0 = acc(Ht, Y - x0), acc(H, Y - x0), acc(Ht, Xu - x0), acc(H, Xu - x0)
            # the g_s-independent part with the relative profile cut away from the relative cut r = L/2
            psi_c = np.exp(-(Y - x0) ** 2 / (4 * wd ** 2)) * Fr * (np.abs(Rs) < L // 3)
            psi_c /= np.linalg.norm(psi_c)
            a0cut = -psi_c @ (H @ H @ ((Y - x0) * psi_c) - 2 * H @ ((Y - x0) * (H @ psi_c)) + (Y - x0) * (H @ H @ psi_c))
            p2 = psi ** 2
            predY = -Eline * np.sum(p2 * np.interp(Y, Xg, dWnu))
            predmid = -0.5 * beta * np.sum(p2 * (np.interp(Xu, Xg, dW1) / d1["mu"] + np.interp(Xu, Xg, dW2) / d2["mu"]))
            out.append(dict(set=name, L=L, coupling=cpl, weight_scale=ws, width=wd, beta=float(beta), a_Y=float(aY),
                            a_Y_gs0=float(a0), a_Y_gs0_profile_cut=float(a0cut), pred_Y=float(predY), ratio_Y=float((aY - a0) / predY), a_mid=float(amid),
                            a_mid_gs0=float(am0), pred_mid=float(predmid), ratio_mid=float((amid - am0) / predmid),
                            aY_over_amid=float((aY - a0) / (amid - am0)),
                            pred_ratio=float(predY / predmid)))
    return out


def weight_ratio_scaling(L, tf, cpl, gs, scales=(1.0, 0.3, 0.1, 0.03)):
    """dW_nu/(dW_1+dW_2) at X = L/4 with the relative profile f_nu of set A kept fixed and the
    couplings gamma_i scaled: tends to 1 as the couplings go to zero (first order in g_i)."""
    b1, b2, par, mode = bodies("A", L, cpl)
    bd = band_data(L, tf, b1, b2, cpl, par, mode)
    rsg = [((r + L // 2) % L) - L // 2 for r in bd["rs"]]
    hf, X, out = field_hop(L, tf), L // 4, []
    for sc in scales:
        g1 = sc * b1["sig"] * b1["gam"] * b1["M"]; g2 = sc * b2["sig"] * b2["gam"] * b2["M"]
        def w(pots):
            h = hf.copy()
            for x, g in pots:
                h[x % L, x % L] += g
            return gs * ground(h)[1][0] ** 2
        Wnu = lambda Y: sum(bd["f"][k] ** 2 * w([(Y - r // 2, g1), (Y + r // 2, g2)]) for k, r in enumerate(rsg))
        dWnu = Wnu(X + 1) - Wnu(X - 1)
        dWs = w([(X + 1, g1)]) - w([(X - 1, g1)]) + w([(X + 1, g2)]) - w([(X - 1, g2)])
        out.append(dict(scale=sc, ratio=float(dWnu / dWs)))
    return out


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    res = [run(L, 1.0, cpl, -0.01) for L in (16, 20) for cpl in ("a", "c")]
    res.append(run(16, 1.0, "a", -0.005))
    lines = []
    for r in res:
        lines.append(f"L={r['L']} coupling={r['coupling']} g_s={r['g_s']} beta={r['beta']:.5f} "
                     f"E''(mu1+mu2)={r['Epp_times_mu_sum']:.5f} s_free={r['s_free']:.5f}")
        lines.append("  exact     spacings " + " ".join(f"{x:.6e}" for x in r["exact_spacings"]))
        lines.append("  projected spacings " + " ".join(f"{x:.6e}" for x in r["proj_spacings"]))
        lines.append("  frozen    spacings " + " ".join(f"{x:.6e}" for x in r["model_spacings"]))
        lines.append("  alt       spacings " + " ".join(f"{x:.6e}" for x in r["alt_spacings"]))
        lines.append(f"  max |exact - projected| level = {r['max_abs_dev_proj']:.3e}   max |exact - frozen| level = "
                     f"{r['max_abs_dev_model']:.3e}   G-weights {np.round(r['G_weights'], 4).tolist()}")
        lines.append(f"  dW_nu/(dW_1+dW_2) = {r['dWnu_over_dW1_plus_dW2']:.5f}   "
                     f"Pi_pair / inertia-weighted Pi_i = {r['Pi_pair_over_weighted_single']:.5f}")
    sc = weight_ratio_scaling(16, 1.0, "a", -0.01)
    lines.append("dW_nu/(dW_1+dW_2) at X=L/4, L=16, f_nu of set A fixed, couplings scaled: "
                 + "  ".join(f"scale={x['scale']}: {x['ratio']:.5f}" for x in sc))
    acc = []
    for name in ("A", "C"):
        for cpl in ("a", "c"):
            acc += accel_test(name, 24, 1.0, cpl, -0.01)
    lines.append("acceleration from rest (6.13), position-space band contract, L=24, g_s=-0.01, envelope centre L/4; "
                 "ratios use the first-order part a - a(g_s=0):")
    lines += [f"  set={x['set']} coupling={x['coupling']} weight_scale={x['weight_scale']} w={x['width']} beta={x['beta']:.4f}: a_Y={x['a_Y']:.6e} "
              f"(g_s=0: {x['a_Y_gs0']:.1e}, profile cut at |r|<L/3: {x['a_Y_gs0_profile_cut']:.1e}) pred_Y={x['pred_Y']:.6e} ratio={x['ratio_Y']:.5f} | a_mid={x['a_mid']:.6e} (g_s=0: {x['a_mid_gs0']:.1e}) "
              f"pred_mid={x['pred_mid']:.6e} ratio={x['ratio_mid']:.5f} | a_Y/a_mid={x['aY_over_amid']:.4f} (pred {x['pred_ratio']:.4f})" for x in acc]
    txt = "\n".join(lines)
    print(txt)
    (OUT / "weight_check.txt").write_text(txt + "\n")
    (OUT / "weight_check.json").write_text(json.dumps(dict(cases=res, weight_ratio_scaling=sc, acceleration=acc),
                                                      indent=1))
