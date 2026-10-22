"""Check of 07-ilang-weight/07-inertia-of-pair-full-grip (N_f = 1, t_f = 1).

Item 2: curvature in P of the exact bound level of two full-grip bodies and one field
object (sector contract continued in P) against (7.3), (7.5); item 3: cost (7.6), (7.8);
item 4: weights from exact eigenvalues with a held source against (7.9)-(7.12).
Outputs: output/check_log.txt, output/check_results.json.
"""
import json
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
TF = 1.0
SX = np.array([[0.0, 1.0], [1.0, 0.0]])
LOG = []


def log(s=""):
    print(s)
    LOG.append(s)


def shift(L):  # (S g)(y) = g(y+1)
    return sp.csr_matrix((np.ones(L), (np.arange(L), (np.arange(L) + 1) % L)), shape=(L, L))


def field(L, src):  # one field object: C_1 + sum_x g_x Phi_x
    H = -TF * (np.eye(L, k=1) + np.eye(L, k=-1))
    H[0, -1] = H[-1, 0] = -TF
    for x, g in src:
        H[x % L, x % L] += g
    return H


def eps0(L, src):
    return np.linalg.eigvalsh(field(L, src))[0]


def ell(L, x):
    x = np.mod(x, L)
    return (L * L - 1) / (12 * L) - x * (L - x) / (2 * L)


def curv(f, d):  # E''(0) by Richardson; E(P) = E(-P) (sigma3 x sigma3 times conjugation)
    e0, e1, e2 = f(0.0), f(d), f(2 * d)
    return (4 * 2 * (e1 - e0) / d**2 - 2 * (e2 - e0) / (2 * d) ** 2) / 3, e0


# ---------- one body (sector contract (5.1), full grip) ----------
def body_level(L, g, tau, P):
    S = shift(L)
    H = sp.kron(sp.identity(2), -TF * (S + S.T)) + sp.kron(sp.diags([1.0, -1.0]), sp.diags((np.arange(L) == 0) * g))
    A = 0.5 * tau * np.exp(-1j * P) * sp.kron(sp.csr_matrix(-1j * SX), S)
    w, v = np.linalg.eigh((H + A + A.conj().T).toarray())
    om = np.linalg.eigh(field(L, [(0, g)]))[1][:, 0]
    return w[np.argmax(np.abs(om @ v[:L, :]) ** 2)]


# ---------- pair: sector contract, basis ((s1,s2), r = l-j, y = field place - j) ----------
def pair_ops(L, g1, g2, t1, t2, P):
    S, I2, IL = shift(L), sp.identity(2), sp.identity(L)
    sg, r, y = np.array([1.0, -1.0]), np.arange(L), np.arange(L)
    dg = (sg[:, None, None, None] * g1 * (y == 0)[None, None, None, :]
          + sg[None, :, None, None] * g2 * (y[None, :] == r[:, None])[None, None, :, :])
    H0 = sp.kron(sp.identity(4 * L), -TF * (S + S.T)) + sp.diags(dg.ravel())
    mX = sp.csr_matrix(-1j * SX)
    A1 = 0.5 * t1 * np.exp(-1j * P) * sp.kron(sp.kron(mX, I2), sp.kron(S, S))
    A2 = 0.5 * t2 * sp.kron(sp.kron(I2, mX), sp.kron(S.T, IL))
    V1, V2 = (A1 + A1.conj().T).tocsr(), (A2 + A2.conj().T).tocsr()
    return (H0 + V1 + V2).tocsc(), V1, V2


def held_blocks(L, g1, g2):
    out = {}
    for s1, s2 in ((0, 0), (1, 0), (0, 1)):
        es, us = zip(*[np.linalg.eigh(field(L, [(0, (1 - 2 * s1) * g1), (r, (1 - 2 * s2) * g2)])) for r in range(L)])
        out[(s1, s2)] = (np.array(es), np.array(us))
    return out


def sw(L, bl, V, key):  # second-order band contract part of one body, (2.10)
    E00, U00 = bl[(0, 0)]
    G = np.zeros((4 * L * L, L), complex)
    for r in range(L):
        G[r * L:(r + 1) * L, r] = U00[r][:, 0]
    W = (V @ G).reshape(2, 2, L, L, L)[key[0], key[1]]
    Eb, Ub = bl[key]
    C = np.einsum('ryk,rya->rka', Ub.conj(), W).reshape(L * L, L)
    T = (C / (E00[None, :, 0] - Eb.reshape(L * L)[:, None])).conj().T @ C
    return 0.5 * (T + T.conj().T)


def run_case(name, L, g1, g2, t1, t2, dist=(), d=0.02):
    n = 1.0 / L
    l0 = ell(L, 0)
    ev = np.arange(0, L, 2)
    rs = np.where(ev > L // 2, ev - L, ev)  # signed even r
    bl = held_blocks(L, g1, g2)
    bl1, bl2 = held_blocks(L, g1, 0.0), held_blocks(L, 0.0, g2)

    def heff(P, b=bl):
        _, V1, V2 = pair_ops(L, g1, g2, t1, t2, P)
        h1, h2 = sw(L, b, V1, (1, 0)), sw(L, b, V2, (0, 1))
        return np.diag(b[(0, 0)][0][:, 0]) + h1 + h2, h1, h2

    kb1 = sw(L, bl1, pair_ops(L, g1, g2, t1, t2, 0.0)[1], (1, 0))[0, 2].real
    kb2 = sw(L, bl2, pair_ops(L, g1, g2, t1, t2, 0.0)[2], (0, 1))[0, 2].real
    low = (kb1 + kb2) < 0  # positive relative inertia: lowest edge

    def band(P):
        h = heff(P)[0][np.ix_(ev, ev)]
        w, v = np.linalg.eigh(h)
        i = 0 if low else -1
        return w[i], v[:, i]

    U00 = bl[(0, 0)][1]

    def exact(P):
        eb, fb = band(P)
        H = pair_ops(L, g1, g2, t1, t2, P)[0]
        w, v = spla.eigsh(H, k=10, sigma=eb, which='LM', tol=0)
        best = (-1, None, None)
        for k in range(len(w)):
            x = v[:, k].reshape(2, 2, L, L)[0, 0]
            a = np.einsum('ry,ry->r', U00[:, :, 0].conj(), x)[ev]
            ov = abs(np.vdot(fb, a)) ** 2
            if ov > best[0]:
                best = (ov, w[k], np.sum(np.abs(a) ** 2))
        return best

    ovs = []

    def exact_e(P):
        ov, e, _ = exact(P)
        ovs.append(ov)
        return e

    Eb2, Eb0 = curv(exact_e, d)
    ov0, _, gw0 = exact(0.0)
    ovmin = min(ovs)
    Ebb2, _ = curv(lambda P: band(P)[0], d)
    mu = [1.0 / curv(lambda P: body_level(L, g, t, P), d)[0] for g, t in ((g1, t1), (g2, t2))]
    E1, E2 = body_level(L, g1, t1, 0.0), body_level(L, g2, t2, 0.0)
    D0 = 1.0 / Eb2 - mu[0] - mu[1]
    # band-contract quantities at P = 0
    _, f0 = band(0.0)
    f0 = (f0 * np.exp(-1j * np.angle(f0[0]))).real
    _, h1, h2 = heff(0.0)
    rho = (ev + 1) % L
    b0 = f0 * np.roll(f0, -1)                       # f0(rho-1) f0(rho+1), rho = r+1
    k1 = np.array([h1[r, (r + 2) % L].real for r in ev])
    k2 = np.array([h2[r, (r + 2) % L].real for r in ev])
    beta0 = b0.sum()
    B = lambda x: -2 * n * g1 * g2 / TF * ell(L, x)
    ra = np.arange(L)
    bar = lambda f: 0.25 * (f[(rho - 1) % L] + 2 * f[rho] + f[(rho + 1) % L])
    Mfull = lambda a, b: np.array([eps0(L, [(0, a), (r, b)]) - eps0(L, [(0, a)]) - eps0(L, [(0, b)]) + eps0(L, []) for r in ra])
    Mpp = Mfull(g1, g2)
    Mo = [(Mpp - Mfull(-g1, g2)) / 2, (Mpp - Mfull(g1, -g2)) / 2]  # parts of M odd in g1, in g2
    sR = [(eps0(L, [(0, g)]) - eps0(L, [(0, -g)])) / 2 for g in (g1, g2)]
    cb = [sR[0] * (-8 * kb1), sR[1] * (-8 * kb2)]  # c_i^2 = sigma_i R_i / mu_i (band contract)
    ce = [sR[0] / mu[0], sR[1] / mu[1]]            # c_i^2 with the exact mu_i
    Dlat = (mu[0] + mu[1]) * (1 - beta0) / beta0
    Dmark2 = (1 / t1**2 + 1 / t2**2) * np.sum(b0 * bar(B(ra))) / beta0**2
    dmo = bar(Mo[0]) / ce[0] + bar(Mo[1]) / ce[1]
    Dmark = np.sum(b0 * dmo) / beta0**2
    Dres = 1 / np.sum(b0 / (mu[0] + mu[1] + dmo)) - mu[0] - mu[1]
    Dband = 1 / Ebb2 + 1 / (8 * kb1) + 1 / (8 * kb2)
    Sc = abs(Dlat) + abs(Dmark)
    Mavg = np.sum(f0**2 * Mpp[ev])
    Moavg = [np.sum(f0**2 * Mo[0][ev]), np.sum(f0**2 * Mo[1][ev])]
    K0 = 2 * (-1 / (8 * mu[0]) - 1 / (8 * mu[1])) * (beta0 - 1)
    dE0 = Eb0 - E1 - E2 + (-2 * TF)
    w_est = (4 * abs(kb1 + kb2) / abs(n * g1 * g2 / TF)) ** (1 / 3)
    # local inertia (7.3): m_i(rho) - mubar_i against Mbar_i^odd(rho)/c_i^2 and Mbar^(2)(rho)/tau_i^2, |rho| <= 3
    near = np.abs(np.where(rho > L // 2, rho - L, rho)) <= 3
    loc, loc2 = [], []
    for k, kb, c, Mi, t in ((k1, kb1, cb[0], Mo[0], t1), (k2, kb2, cb[1], Mo[1], t2)):
        sh = (-1 / (8 * k) + 1 / (8 * kb))[near]
        loc.append(float(np.max(np.abs(sh / (bar(Mi) / c)[near] - 1))))
        loc2.append(float(np.max(np.abs(sh / (bar(B(ra)) / t**2)[near] - 1))))
    res = dict(case=name, L=L, g1=g1, g2=g2, tau1=t1, tau2=t2, eta=max(abs(g1), abs(g2)) * l0 / TF,
               w=w_est, mean_abs_r=float(np.sum(f0**2 * np.abs(rs))), overlap=ov0, min_overlap=ovmin,
               group_weight=gw0, selected="lowest" if low else "highest", mu1=mu[0], mu2=mu[1],
               Epp_exact=Eb2, Epp_band=Ebb2, Epp_66=float(np.sum(b0 / (-1 / (8 * k1) - 1 / (8 * k2)))), beta0=beta0,
               D0_exact=D0, D0_band=Dband, Dlat=Dlat, Dmark_odd=Dmark, Dmark_lead=Dmark2, D0_formula=Dlat + Dmark,
               D0_resummed=Dres, D0_lead=Dlat + Dmark2, local_inertia_relerr_odd=loc, local_inertia_relerr_lead=loc2,
               dE0_exact=dE0, M_avg=Mavg, M_odd_avg=Moavg, M0_second_order=float(B(0)), K0=K0, dE0_formula=Mavg + K0)
    log(f"== {name}: L={L} g1={g1:.5g} g2={g2:.5g} tau1={t1:.4g} tau2={t2:.4g} eta={res['eta']:.3f} w={w_est:.2f}")
    log(f"   selected {res['selected']} level, <|r|>={res['mean_abs_r']:.2f}, overlap={ov0:.6f} (min over P {ovmin:.6f}), group weight={gw0:.6f}")
    log(f"   E''(0): exact={Eb2:.6e} band(2.10)={Ebb2:.6e} (6.6) sum b0/m={res['Epp_66']:.6e}  rel. band-exact={(Ebb2 - Eb2) / Eb2:.2e}")
    log(f"   mu1={mu[0]:.6e} mu2={mu[1]:.6e} beta0={beta0:.5f} Dlat={Dlat:.4e} Dmark(odd parts)={Dmark:.4e} Dmark(lead)={Dmark2:.4e} Dlat/|Dmark|={abs(Dlat / Dmark):.3f}")
    log(f"   D0: exact={D0:.6e} band={Dband:.6e} (7.5)={Dlat + Dmark:.6e} resummed={Dres:.6e} leading={Dlat + Dmark2:.6e}")
    log(f"   deviation from exact D0 / (|Dlat|+|Dmark|): band {(Dband - D0) / Sc:.2e}, (7.5) {(Dlat + Dmark - D0) / Sc:.2e}, resummed {(Dres - D0) / Sc:.2e}, leading {(Dlat + Dmark2 - D0) / Sc:.2e}")
    log(f"   local inertia (7.3), max rel. error near r=0: odd parts {loc[0]:.2e}, {loc[1]:.2e}; second order {loc2[0]:.2e}, {loc2[1]:.2e}")
    log(f"   cost: dE0 exact={dE0:.6e} <M>+K0={Mavg + K0:.6e} (<M>={Mavg:.4e}, M2(0)={B(0):.4e}, K0={K0:.4e}); (<M1odd>+<M2odd>)/<M>={(Moavg[0] + Moavg[1]) / Mavg:.4f}")
    log(f"   (D0_exact-Dlat)/dE0={(D0 - Dlat) / dE0:.6e} vs 1/tau1^2+1/tau2^2={1 / t1**2 + 1 / t2**2:.6e}, 1/tau1^2={1 / t1**2:.6e}; D0_exact/dE0={D0 / dE0:.6e}")
    # ---------- item 4: weights from exact eigenvalues with a held source ----------
    gs, res['weight'] = 1e-3, []
    for s in dist:
        X, xs = 0, s
        Wh = lambda src: (eps0(L, src + [(xs, gs)]) - eps0(L, src + [(xs, -gs)])) / 2
        dW = lambda fun: (fun(X + 1) - fun(X - 1)) / 2
        Wp = lambda Xc: np.sum([f0[i] ** 2 * Wh([(Xc - rs[i] // 2, g1), (Xc - rs[i] // 2 + rs[i], g2)]) for i in range(len(ev))])
        W0p, W1p, W2p = dW(Wp), dW(lambda x: Wh([(x, g1)])), dW(lambda x: Wh([(x, g2)]))
        phip = dW(lambda x: -2 * gs / TF * ell(L, x - xs))
        u = s / L
        ks = (L * L * (1 - 2 * u) ** 2 + 2) / (L * L - 1)
        Vavg = np.sum(f0**2 * n * g1 * g2 / TF * np.mod(rs, L) * (L - np.mod(rs, L)) / L)
        Cev = [-n * g**2 / TF * l0 for g in (g1, g2)]
        W0f = phip * (n * (g1 + g2) + 2 * ks * (Cev[0] + Cev[1] + B(0)) + Vavg)
        Wbp, Wbf = W0p - W1p - W2p, phip * (2 * ks * B(0) + Vavg)
        G1, G2, Gp, Gb = W1p / mu[0], W2p / mu[1], Eb2 * W0p, Wbp / D0
        Gm = Wbp / (D0 - Dlat)  # bond weight over the exact mark part of the inertia
        Gp_lead = phip * (g1 + g2) / (g1 / t1**2 + g2 / t2**2)
        Gb_lead = 2 * ks * phip / (1 / t1**2 + 1 / t2**2)
        wr = dict(s=s, u=u, kappa_s=ks, W0p_exact=W0p, W0p_formula=W0f, Wbp_exact=Wbp, Wbp_formula=Wbf,
                  Gamma1=G1, Gamma2=G2, Gamma_pair=Gp, Gamma_pair_lead=Gp_lead, Gamma_bond=Gb,
                  Gamma_bond_lead=Gb_lead, Gamma_mark=Gm, Gamma_bond_formula=Wbf / (Dlat + Dmark2), phip=phip)
        res['weight'].append(wr)
        log(f"   source at s={s} (u={u:.3f}, kappa_s={ks:.4f}), linear in g_s:")
        log(f"     W0' exact={W0p:.6e} formula(7.10)={W0f:.6e};  Wb' exact={Wbp:.6e} formula={Wbf:.6e}")
        log(f"     Gamma/phi': body1={G1 / phip:.6e} (tau1^2={t1**2:.6e}) body2={G2 / phip:.6e} (tau2^2={t2**2:.6e})")
        log(f"     Gamma_pair/phi'={Gp / phip:.6e} lead={Gp_lead / phip:.6e};  Gamma_bond/phi'={Gb / phip:.6e} lead(7.12)={Gb_lead / phip:.6e} formula={wr['Gamma_bond_formula'] / phip:.6e}")
        log(f"     Wb'/(D0_exact-Dlat)/phi'={Gm / phip:.6e} vs kappa_s*2/(1/tau1^2+1/tau2^2)={Gb_lead / phip:.6e};  Gamma_bond/Gamma_1={Gb / G1:.4f}, Wb'/(D0-Dlat)/Gamma_1={Gm / G1:.4f}")
    return res


def params(L, eta1, q, r1, r2=None):
    """g1 from eta1 = |g1| l0 / t_f, g2 = q g1, tau_i = r_i d with d = 2 n min|g_i|."""
    r2 = r1 if r2 is None else r2
    g1 = eta1 * TF / ell(L, 0)
    d = 2 * min(abs(g1), abs(q * g1)) / L
    return L, g1, q * g1, r1 * d, r2 * d


if __name__ == "__main__":
    cases = [("A equal bodies", (32, 0.15, 1.0, 0.3), ()),
             ("A equal bodies", (64, 0.15, 1.0, 0.3), (8, 16)),
             ("A' equal bodies, smaller eta", (64, 0.05, 1.0, 0.3), (8, 16)),
             ("A'' equal bodies, smaller eta and tau/d", (64, 0.05, 1.0, 0.15), ()),
             ("B unequal bodies and speeds", (32, 0.15, 0.5, 0.3, 0.15), ()),
             ("B unequal bodies and speeds", (64, 0.15, 0.5, 0.3, 0.15), (8, 16)),
             ("R equal bodies, regime (ii)", (128, 0.15, 1.0, 0.3), (16, 32)),
             ("C mixed signs, bound at top", (48, 0.075, -2.0, 0.15, 0.3), ()),
             ("D control: both negative, not bound", (48, -0.15, 1.0, 0.3), ())]
    results = [run_case(name, *params(*p), dist=dist) for name, p, dist in cases]
    (OUT / "check_log.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
    (OUT / "check_results.json").write_text(json.dumps(results, indent=1, default=float), encoding="utf-8")
