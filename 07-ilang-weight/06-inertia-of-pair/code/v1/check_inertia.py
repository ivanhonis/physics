"""Check of item 2 of 07-ilang-weight/06-inertia-of-pair (and of the numbers of items 1, 3).

Two Model D bodies (one clock level each: half-gap M_i, branch sigma_i), N_f = 1 field object
on a ring of L places, couplings (a) and (c).  The exact sector contract H(P) of bodies and
field (body 1 at place 0 as representative) is continued to real P; the curvature of the
exact bound level at P = 0 is compared with (6.6) evaluated on the band contract at order
tau^2 (second-order Schrieffer-Wolff on the tau = 0 levels), and with mu_1 + mu_2.
Branch basis (|+>, i|->): the motion term is real, -i sigma_1 -> J.
"""
import json
from pathlib import Path

import numpy as np

OUT = Path(__file__).parent / "output"
J = np.array([[0.0, 1.0], [-1.0, 0.0]])
SG = np.array([1.0, -1.0])  # branch index 0: sigma = +1, 1: sigma = -1


def bidx(sig):
    return 0 if sig > 0 else 1


def ground(h):
    w, v = np.linalg.eigh(h)
    g = v[:, 0]
    return w[0], g * np.sign(g.sum())


def field_hop(L, tf):
    h = np.zeros((L, L))
    for y in range(L):
        h[y, (y + 1) % L] = h[(y + 1) % L, y] = -tf
    return h


# ---------------------------------------------------------------- one body + field, sector
def body_sector(L, tf, b, cpl):
    cc = 1.0 if cpl == "c" else 0.0
    n = 2 * L
    ix = lambda s, y: s * L + y
    H0 = np.zeros((n, n)); B = np.zeros((n, n))
    hf = field_hop(L, tf)
    for s in range(2):
        H0[s * L:(s + 1) * L, s * L:(s + 1) * L] += hf
        for y in range(L):
            a = ix(s, y)
            H0[a, a] += SG[s] * b["M"] * (1 + b["gam"] * (y == 0))
            f = 1 + cc * b["gam"] * 0.5 * ((y == 0) + (y == 1))
            for sp in range(2):  # right hop 0 -> 1, frame shift y -> y-1, phase e^{-iP}
                B[ix(sp, (y - 1) % L), a] += 0.5 * b["tau"] * J[sp, s] * f
    return H0, B


def curvature(H0, B, sel_vec, mode):
    """E''(0) of the eigenvector of H(0)=H0+B+B^T selected by overlap with sel_vec (G-weight)."""
    H = H0 + B + B.T
    w, v = np.linalg.eigh(H)
    gw = np.abs(sel_vec.T @ v) ** 2 if sel_vec.ndim == 1 else (np.abs(sel_vec.T @ v) ** 2).sum(0)
    cand = np.where(gw > 0.5)[0]
    k = cand[np.argmin(w[cand])] if mode == "low" else cand[np.argmax(w[cand])]
    H1 = -1j * (B - B.T)
    H2 = -(B + B.T)
    x = v[:, k]
    d = w[k] - w
    d[k] = np.inf
    m1 = v.conj().T @ (H1 @ x)
    E2 = (x @ H2 @ x) + 2 * np.sum(np.abs(m1) ** 2 / d)
    return w[k], E2.real, v[:, k], gw[k]


def sw_scalar(H0, V, gvec):
    """Second-order SW energy of the single G state gvec (V complex allowed)."""
    w, U = np.linalg.eigh(H0)
    a = np.argmax(np.abs(U.T @ gvec))
    Vt = U.T @ V @ U
    d = w[a] - w
    d[a] = np.inf
    return w[a] + np.sum(np.abs(Vt[:, a]) ** 2 / d)


def body_data(L, tf, b, cpl):
    H0, B = body_sector(L, tf, b, cpl)
    s = bidx(b["sig"])
    hf = field_hop(L, tf); hf0 = hf.copy(); hf0[0, 0] += b["sig"] * b["gam"] * b["M"]
    e0, Om = ground(hf0)
    g = np.zeros(2 * L); g[s * L:(s + 1) * L] = Om
    E0, E2, _, gw = curvature(H0, B, g, "low" if b["sig"] > 0 else "high")
    # band contract (order tau^2): kappa_bar from P = 0 and P = pi/2
    Hs = lambda P: sw_scalar(H0, np.exp(-1j * P) * B + np.exp(1j * P) * B.T, g)
    kbar = (Hs(0.0) - Hs(np.pi / 2)).real / 4
    eps = lambda gg: np.linalg.eigvalsh(hf + np.diag([gg] + [0] * (L - 1)))[0]
    R = b["M"] + 0.5 * (eps(b["gam"] * b["M"]) - eps(-b["gam"] * b["M"]))
    c2 = b["tau"] ** 2 * (1 + (b["gam"] / L if cpl == "c" else 0.0)) ** 2
    return dict(E0=E0, mu=1 / E2, mubar=-1 / (8 * kbar), kbar=kbar, R=R, c2=c2, gw=gw)


# ---------------------------------------------------------------- two bodies + field, sector
def pair_sector(L, tf, b1, b2, cpl):
    cc = 1.0 if cpl == "c" else 0.0
    n = 4 * L * L
    ix = lambda s1, r, s2, y: ((s1 * L + r) * 2 + s2) * L + y
    H0 = np.zeros((n, n)); B1 = np.zeros((n, n)); V2 = np.zeros((n, n))
    for s1 in range(2):
        for r in range(L):
            for s2 in range(2):
                for y in range(L):
                    a = ix(s1, r, s2, y)
                    H0[a, a] += SG[s1] * b1["M"] * (1 + b1["gam"] * (y == 0)) \
                        + SG[s2] * b2["M"] * (1 + b2["gam"] * (y == r))
                    H0[ix(s1, r, s2, (y + 1) % L), a] += -tf
                    H0[ix(s1, r, s2, (y - 1) % L), a] += -tf
                    for t in range(2):
                        f = 1 + cc * b2["gam"] * 0.5 * ((y == r) + (y == (r + 1) % L))
                        V2[ix(s1, (r + 1) % L, t, y), a] += 0.5 * b2["tau"] * J[t, s2] * f
                        f = 1 + cc * b2["gam"] * 0.5 * ((y == (r - 1) % L) + (y == r))
                        V2[ix(s1, (r - 1) % L, t, y), a] += 0.5 * b2["tau"] * J[s2, t] * f
                        f = 1 + cc * b1["gam"] * 0.5 * ((y == 0) + (y == 1))
                        B1[ix(t, (r - 1) % L, s2, (y - 1) % L), a] += 0.5 * b1["tau"] * J[t, s1] * f
    return H0, B1, V2, ix


def pair_block(L, tf, b1, b2, cpl, par):
    """Restrict to the block of (-1)^r s1 s2 containing the band G (branches sig_i, r = par mod 2).
    Returns H0, B1, V2 on the block, the tau=0 eigenbasis U0 (block by block in (s1, r, s2)),
    its eigenvalues w0, the columns gi of U0 that form G (field ground, positive), and rs."""
    H0, B1, V2, ix = pair_sector(L, tf, b1, b2, cpl)
    pi0 = (-1) ** par * b1["sig"] * b2["sig"]
    trip = [(s1, r, s2) for s1 in range(2) for r in range(L) for s2 in range(2)
            if (-1) ** r * SG[s1] * SG[s2] == pi0]
    keep = np.array([ix(s1, r, s2, y) for (s1, r, s2) in trip for y in range(L)])
    sub = lambda A: A[np.ix_(keep, keep)]
    H0b, B1b, V2b = sub(H0), sub(B1), sub(V2)
    n = len(keep)
    U0 = np.zeros((n, n)); w0 = np.zeros(n)
    s1g, s2g = bidx(b1["sig"]), bidx(b2["sig"])
    rs, gi = [], []
    for t, (s1, r, s2) in enumerate(trip):
        sl = slice(t * L, (t + 1) * L)
        w, v = np.linalg.eigh(H0b[sl, sl])
        v[:, 0] *= np.sign(v[:, 0].sum())
        U0[sl, sl] = v; w0[sl] = w
        if (s1, s2) == (s1g, s2g):
            rs.append(r); gi.append(t * L)
    order = np.argsort(rs)
    rs = [rs[i] for i in order]; gi = np.array([gi[i] for i in order])
    return H0b, B1b, V2b, U0, w0, gi, rs


def band_contract(U0, w0, gi, V):
    """Second-order SW band contract on the G columns gi of the tau=0 eigenbasis U0."""
    mask = np.ones(len(w0), bool); mask[gi] = False
    Vgc = U0[:, gi].T @ V @ U0[:, mask]
    Ea, Ec = w0[gi], w0[mask]
    A = Vgc / (Ea[:, None] - Ec[None, :])
    Heff = np.diag(Ea).astype(complex) + 0.5 * (A @ Vgc.conj().T + Vgc @ A.conj().T)
    return Heff, Ea


def ell(r, L):
    r = np.mod(r, L)
    return (L * L - 1) / (12 * L) - r * (L - r) / (2 * L)


def band_data(L, tf, b1, b2, cpl, par, mode):
    """Band contract at order tau^2 at P = 0: relative level f, bonds b, kappa_i(rho), m(rho)."""
    H0, B1, V2, U0, w0, gi, rs = pair_block(L, tf, b1, b2, cpl, par)
    K1, _ = band_contract(U0, w0, gi, B1 + B1.T)
    K2, Ea = band_contract(U0, w0, gi, V2)
    K1 = (K1 - np.diag(Ea)).real; K2 = (K2 - np.diag(Ea)).real
    w, v = np.linalg.eigh(np.diag(Ea) + K1 + K2)
    k = 0 if mode == "low" else -1
    f = v[:, k]
    nr = len(rs)
    nb = lambda A: np.array([A[j, (j + 1) % nr] for j in range(nr)])  # bond (r_j, r_j + 2)
    k1, k2 = nb(K1), nb(K2)
    b = np.array([f[j] * f[(j + 1) % nr] for j in range(nr)])
    rho = np.array(rs) + 1
    return dict(H0=H0, B1=B1, V2=V2, U0=U0, w0=w0, gi=gi, rs=rs, K1=K1, K2=K2, Ea=Ea, f=f, eps=w[k],
                b=b, k1=k1, k2=k2, m=-1 / (8 * k1) - 1 / (8 * k2), rho=rho)


def mark_formula(L, tf, b1, b2, cpl, d1, d2, rho):
    """s_c (c1^-2 + c2^-2) Mbar2(rho), with M2(r) = -(2 n g1 g2 / t_f) ell(r) (quoted (4.3))."""
    n = 1.0 / L
    g1, g2 = b1["sig"] * b1["gam"] * b1["M"], b2["sig"] * b2["gam"] * b2["M"]
    M2 = lambda r: -(2 * n * g1 * g2 / tf) * ell(r, L)
    M2bar = 0.25 * (M2(rho + 1) + 2 * M2(rho) + M2(rho - 1))
    sc = 1.0 if cpl == "a" else -1.0
    return sc * (1 / d1["c2"] + 1 / d2["c2"]) * M2bar


def run_case(L, tf, b1, b2, cpl, par, mode):
    bd = band_data(L, tf, b1, b2, cpl, par, mode)
    H0, B1, V2, U0, gi = bd["H0"], bd["B1"], bd["V2"], bd["U0"], bd["gi"]
    G = U0[:, gi]
    # exact bound level and its curvature: H(P) = H0 + V2 + e^{-iP}B1 + e^{iP}B1^T (body 1 as representative)
    Eb, Ebpp, _, gw = curvature(H0 + V2, B1, G, mode)
    def lev(P):  # finite-difference cross-check of the continuation in P
        w, v = np.linalg.eigh(H0 + V2 + np.exp(-1j * P) * B1 + np.exp(1j * P) * B1.T)
        c = np.where((np.abs(G.T @ v) ** 2).sum(0) > 0.5)[0]
        return w[c].min() if mode == "low" else w[c].max()
    h = 2e-3
    Ebpp_fd = (lev(h) - 2 * lev(0.0) + lev(-h)) / h ** 2
    # curvature of the band-contract level on the ring (same continuation)
    def band_lev(P):
        hP, _ = band_contract(U0, bd["w0"], gi, np.exp(-1j * P) * B1 + np.exp(1j * P) * B1.T + V2)
        e = np.linalg.eigvalsh(hP)
        return e[0] if mode == "low" else e[-1]
    Epp_band = (band_lev(h) - 2 * band_lev(0.0) + band_lev(-h)) / h ** 2
    # (6.6): sum_rho b/m plus the ring term Phi'(0)^2 d^2 eps / dPhi^2
    b, m, k1, k2 = bd["b"], bd["m"], bd["k1"], bd["k2"]
    Epp_66 = np.sum(b / m)
    h0 = np.diag(bd["Ea"]) + bd["K1"] + bd["K2"]
    nr = len(bd["rs"])
    def eF(F):
        hF = h0.astype(complex); hF[nr - 1, 0] *= np.exp(1j * F); hF[0, nr - 1] *= np.exp(-1j * F)
        e = np.linalg.eigvalsh(hF)
        return e[0] if mode == "low" else e[-1]
    d2F = (eF(1e-2) - 2 * eF(0.0) + eF(-1e-2)) / 1e-4
    dPhi = -2 * np.sum(k1 / (k1 + k2))
    ring = dPhi ** 2 * d2F
    beta = b.sum()
    d1, d2 = body_data(L, tf, b1, cpl), body_data(L, tf, b2, cpl)
    mu, mub = d1["mu"] + d2["mu"], d1["mubar"] + d2["mubar"]
    Dmark = np.sum(b * mark_formula(L, tf, b1, b2, cpl, d1, d2, bd["rho"])) / beta ** 2
    Dlat = mu * (1 - beta) / beta
    dE = Eb - d1["E0"] - d2["E0"] + (-2 * tf)  # cost difference: pair - body 1 - body 2 + field alone
    n = 1.0 / L
    g1, g2 = b1["sig"] * b1["gam"] * b1["M"], b2["sig"] * b2["gam"] * b2["M"]
    return dict(L=L, coupling=cpl, parity=par, level=mode, Gweight=float(gw), Eb0=Eb,
                inv_Epp_exact=1 / Ebpp, inv_Epp_fd=1 / Ebpp_fd, inv_Epp_band_ring=1 / Epp_band,
                inv_Epp_66=1 / Epp_66, inv_Epp_66_plus_ring=1 / (Epp_66 + ring), ring_term_rel=ring / Epp_66,
                beta=beta, mu1=d1["mu"], mu2=d2["mu"], mu_sum=mu, mubar_sum=mub, mu_over_beta=mu / beta,
                rel_dev_band_ring_vs_exact=Ebpp / Epp_band - 1,
                rel_dev_66ring_vs_exact=Ebpp / (Epp_66 + ring) - 1,
                rel_dev_mu_over_beta_vs_exact=(mu / beta) * Ebpp - 1,
                D_exact=1 / Ebpp - mu, D_lat=Dlat, D_mark_formula=Dmark, D_lat_plus_mark=Dlat + Dmark,
                sigR_over_c2_mu=[b1["sig"] * d1["R"] / d1["c2"] / d1["mu"], b2["sig"] * d2["R"] / d2["c2"] / d2["mu"]],
                kappa_bar=[d1["kbar"], d2["kbar"]], chi=n * abs(g1 * g2) / tf / abs(d1["kbar"] + d2["kbar"]),
                participation=1 / np.sum(bd["f"] ** 4), dE_cost=dE,
                D_over_dE_times_c1sq=(1 / Ebpp - mu) * d1["c2"] / dE,
                D_over_dE_times_c2sq=(1 / Ebpp - mu) * d2["c2"] / dE)


def mark_check(L, tf, b1, b2, cpl, par, mode, scales=(1.0, 0.3, 0.1, 0.03)):
    """Ratio [m(rho) - mubar_1 - mubar_2] / [s_c (c1^-2+c2^-2) Mbar2(rho)] at the contact bonds, couplings scaled."""
    out = []
    for s in scales:
        c1, c2 = dict(b1), dict(b2)
        c1["gam"] *= s; c2["gam"] *= s
        bd = band_data(L, tf, c1, c2, cpl, par, mode)
        d1, d2 = body_data(L, tf, c1, cpl), body_data(L, tf, c2, cpl)
        num = bd["m"] - d1["mubar"] - d2["mubar"]
        pred = mark_formula(L, tf, c1, c2, cpl, d1, d2, bd["rho"])
        j = np.argsort(np.abs(((bd["rho"] + L // 2) % L) - L // 2))[:2]  # bonds nearest to contact
        out.append(dict(scale=s, coupling=cpl, ratio_contact=float(np.mean(num[j] / pred[j])),
                        ratio_all=[float(x) for x in num / pred]))
    return out


SETS = {  # (body 1, body 2, parity of r, extreme level); t_f = 1, M_i > 2 t_f so that R1 holds for sigma = +1
    "A": (dict(M=3.0, tau=0.20, gam=0.09, sig=+1), dict(M=4.0, tau=0.20, gam=0.07, sig=+1), 0, "low"),
    "B": (dict(M=2.5, tau=0.16, gam=0.10, sig=-1), dict(M=2.0, tau=0.20, gam=-0.14, sig=-1), 1, "high"),
}

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    tf = 1.0
    res = []
    for name, (b1, b2, par, mode) in SETS.items():
        for L in (12, 16):
            for cpl in ("a", "c"):
                r = run_case(L, tf, b1, b2, cpl, par, mode)
                r["set"] = name
                res.append(r)
    keys = ["set", "L", "coupling", "level", "chi", "beta", "inv_Epp_exact", "inv_Epp_fd", "inv_Epp_band_ring",
            "inv_Epp_66", "inv_Epp_66_plus_ring", "mu_sum", "mu_over_beta", "rel_dev_band_ring_vs_exact",
            "rel_dev_66ring_vs_exact", "rel_dev_mu_over_beta_vs_exact", "ring_term_rel", "D_exact", "D_lat",
            "D_mark_formula", "D_lat_plus_mark", "dE_cost", "D_over_dE_times_c1sq", "D_over_dE_times_c2sq"]
    fmt = lambda k, v: f"{k}={v:.6g}" if isinstance(v, (float, np.floating)) else f"{k}={v}"
    lines = ["  ".join(fmt(k, r[k]) for k in keys) for r in res]
    mk = []
    for cpl in ("a", "c"):
        b1, b2, par, mode = SETS["A"]
        mk += mark_check(12, tf, b1, b2, cpl, par, mode)
    lines.append("mark term check (set A, L=12): ratio of m(rho)-mubar_1-mubar_2 to the mark term of (6.7) at contact bonds")
    lines += [f"  coupling={x['coupling']} scale={x['scale']} ratio={x['ratio_contact']:.4f}" for x in mk]
    txt = "\n".join(lines)
    print(txt)
    (OUT / "inertia_check.txt").write_text(txt + "\n")
    conv = lambda o: o.tolist() if isinstance(o, np.ndarray) else float(o)
    (OUT / "inertia_check.json").write_text(json.dumps(dict(cases=res, mark_check=mk), indent=1, default=conv))
