"""Check of item 4 of 07-ilang-weight/06-inertia-of-pair against exact eigenvalues with a held source.

Two Model D bodies and N_f = 1 field object on a ring of L places (set A of check_inertia.py),
plus a held source g_s Phi_{x_s}.  The exact contract (all places, no sector) is diagonalized near
the bottom of the bound band, where the bound pair sits in the weight well opposite the source.
Its levels are compared with the reduced description E_b(P) + W_nu(X) of Step 6 of the derivation
(E_b(P_k) exact sector levels at the allowed P_k, W_nu(X) the f_nu^2 average (6.11) of the exact
first-order weights of the held pair), and with the same description in which the pair band is
rescaled to the inertia mu_1 + mu_2 (the value that would make the fall factor equal to that of
the free bodies).
"""
import json
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla

from check_inertia import (OUT, J, SG, SETS, bidx, ground, field_hop, pair_block, band_data,
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


def sector_level(L, tf, b1, b2, cpl, par, mode, P):
    H0, B1, V2, U0, w0, gi, rs = pair_block(L, tf, b1, b2, cpl, par)
    G = U0[:, gi]
    w, v = np.linalg.eigh(H0 + V2 + np.exp(-1j * P) * B1 + np.exp(1j * P) * B1.T)
    c = np.where((np.abs(G.T @ v) ** 2).sum(0) > 0.5)[0]
    return w[c].min() if mode == "low" else w[c].max()


def run(L, tf, cpl, gs, nlev=4):
    b1, b2, par, mode = SETS["A"]
    xs = 0
    s1g, s2g = bidx(b1["sig"]), bidx(b2["sig"])
    # held weights (first order in g_s): W(j,l) = g_s |Omega_jl(x_s)|^2, single bodies W_i(x)
    hf = field_hop(L, tf)
    Om = {}
    Wpair = np.zeros((L, L))
    for j in range(L):
        for l in range(L):
            h = hf.copy(); h[j, j] += b1["sig"] * b1["gam"] * b1["M"]; h[l, l] += b2["sig"] * b2["gam"] * b2["M"]
            _, o = ground(h)
            Om[(j, l)] = o
            Wpair[j, l] = gs * o[xs] ** 2
    W1 = np.zeros(L); W2 = np.zeros(L)
    for x in range(L):
        h = hf.copy(); h[x, x] += b1["sig"] * b1["gam"] * b1["M"]; W1[x] = gs * ground(h)[1][xs] ** 2
        h = hf.copy(); h[x, x] += b2["sig"] * b2["gam"] * b2["M"]; W2[x] = gs * ground(h)[1][xs] ** 2
    # relative level f_nu (band contract, P = 0) and the pair weight W_nu(X), (6.11)
    bd = band_data(L, tf, b1, b2, cpl, par, mode)
    rsg = [((r + L // 2) % L) - L // 2 for r in bd["rs"]]  # signed separations
    Wnu = np.array([sum(bd["f"][k] ** 2 * Wpair[(X - r // 2) % L, (X + r // 2) % L] for k, r in enumerate(rsg))
                    for X in range(L)])
    # pair band at the allowed P_k (exact sector levels) and reduced description
    Ps = 2 * np.pi * np.arange(L) / L
    Eb = np.array([sector_level(L, tf, b1, b2, cpl, par, mode, P) for P in Ps])
    F = np.exp(1j * np.outer(np.arange(L), Ps)) / np.sqrt(L)  # <X|P_k>
    H0b, B1b, V2b = bd["H0"], bd["B1"], bd["V2"]
    _, Epp, _, _ = curvature(H0b + V2b, B1b, bd["U0"][:, bd["gi"]], mode)
    d1, d2 = body_data(L, tf, b1, cpl), body_data(L, tf, b2, cpl)
    mu = d1["mu"] + d2["mu"]
    s_free = 1 / (mu * Epp)  # rescales the band curvature to 1/(mu_1 + mu_2)
    def model(Eband):
        Hm = F @ np.diag(Eband) @ F.conj().T + np.diag(Wnu)
        return np.linalg.eigvalsh(Hm)[:nlev]
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
    # fall factors at a place midway between the source and the well: Pi = E'' * (W(X+1)-W(X-1))/2
    X = L // 4
    dWnu = (Wnu[X + 1] - Wnu[X - 1]) / 2
    dW1, dW2 = (W1[X + 1] - W1[X - 1]) / 2, (W2[X + 1] - W2[X - 1]) / 2
    return dict(L=L, coupling=cpl, g_s=gs, exact_levels=ex.tolist(), model_levels=Em.tolist(),
                alt_levels=Ealt.tolist(), exact_spacings=np.diff(ex).tolist(), model_spacings=np.diff(Em).tolist(),
                alt_spacings=np.diff(Ealt).tolist(), beta=float(bd["b"].sum()), s_free=float(s_free),
                max_abs_dev_model=float(np.max(np.abs(ex - Em))), G_weights=np.sort(Gw)[::-1][:nlev].tolist(),
                dWnu_over_dW1_plus_dW2=float(dWnu / (dW1 + dW2)), Epp_times_mu_sum=float(Epp * mu),
                # Pi_pair / [(mu_1 Pi_1 + mu_2 Pi_2)/(mu_1+mu_2)] with Pi_i = dW_i / mu_i
                Pi_pair_over_weighted_single=float(Epp * dWnu * mu / (dW1 + dW2)))


def weight_ratio_scaling(L, tf, cpl, gs, scales=(1.0, 0.3, 0.1, 0.03)):
    """dW_nu/(dW_1+dW_2) at X = L/4 with the relative profile f_nu of set A kept fixed and the
    couplings gamma_i scaled: tends to 1 as the couplings go to zero (first order in g_i)."""
    b1, b2, par, mode = SETS["A"]
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
        lines.append("  exact spacings " + " ".join(f"{x:.6e}" for x in r["exact_spacings"]))
        lines.append("  model spacings " + " ".join(f"{x:.6e}" for x in r["model_spacings"]))
        lines.append("  alt   spacings " + " ".join(f"{x:.6e}" for x in r["alt_spacings"]))
        lines.append(f"  max |exact - model| level = {r['max_abs_dev_model']:.3e}   G-weights {np.round(r['G_weights'], 4).tolist()}")
        lines.append(f"  dW_nu/(dW_1+dW_2) = {r['dWnu_over_dW1_plus_dW2']:.5f}   "
                     f"Pi_pair / inertia-weighted Pi_i = {r['Pi_pair_over_weighted_single']:.5f}")
    sc = weight_ratio_scaling(16, 1.0, "a", -0.01)
    lines.append("dW_nu/(dW_1+dW_2) at X=L/4, L=16, f_nu of set A fixed, couplings scaled: "
                 + "  ".join(f"scale={x['scale']}: {x['ratio']:.5f}" for x in sc))
    txt = "\n".join(lines)
    print(txt)
    (OUT / "weight_check.txt").write_text(txt + "\n")
    (OUT / "weight_check.json").write_text(json.dumps(dict(cases=res, weight_ratio_scaling=sc), indent=1))
