"""Check of 07-ilang-weight/07-inertia-of-pair-full-grip (N_f = 1, t_f = 1).

Item 1: distance of the group G from all other held levels of its parity class (field excitations,
single flips, joint flip), from the exact held spectra. Item 2: curvature in P of the exact bound level
of two full-grip bodies and one field object (sector contract continued in P) against (7.3), (7.5).
Item 3: cost (7.6), (7.8). Item 4: weight of the selected level from exact eigenvalues of the sector
contract with a source at fixed distance from the pair's midpoint (first order in g_s, odd part), and
Gamma_b = W_b'/D_0 against (7.9)-(7.12); held-field averages (v1) for comparison.
Outputs: output/check_log.txt, output/check_results.json.
"""
import json
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

OUT = Path(__file__).parent / "output"
TF = 1.0
SX = np.array([[0.0, 1.0], [1.0, 0.0]])
GS = 1e-5  # source strength (weights are taken as odd parts in g_s)
LOG = []


def log(s=""):
    print(s, flush=True)
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


def ground(L, src):  # spectrum, eigenvectors, positive ground vector
    e, u = np.linalg.eigh(field(L, src))
    return e, u, u[:, 0] * np.sign(u[:, 0].sum())


def ell(L, x):
    x = np.mod(x, L)
    return (L * L - 1) / (12 * L) - x * (L - x) / (2 * L)


def curv(f, d):  # E''(0) by Richardson; E(P) = E(-P) (sigma3 x sigma3 times conjugation)
    e0, e1, e2 = f(0.0), f(d), f(2 * d)
    return (4 * 2 * (e1 - e0) / d**2 - 2 * (e2 - e0) / (2 * d) ** 2) / 3, e0


def mindist(a, b):  # min |x - y| over x in a, y in b
    b = np.sort(np.asarray(b))
    i = np.clip(np.searchsorted(b, a), 1, len(b) - 1)
    return float(np.min(np.minimum(np.abs(a - b[i - 1]), np.abs(a - b[i]))))


# ---------- one body (sector contract (5.1), full grip); basis (branch, field place - body place) ----------
def body_level(L, g, tau, P, vec=False):
    S = shift(L)
    H = sp.kron(sp.identity(2), -TF * (S + S.T)) + sp.kron(sp.diags([1.0, -1.0]), sp.diags((np.arange(L) == 0) * g))
    A = 0.5 * tau * np.exp(-1j * P) * sp.kron(sp.csr_matrix(-1j * SX), S)
    w, v = np.linalg.eigh((H + A + A.conj().T).toarray())
    om = ground(L, [(0, g)])[2]
    i = np.argmax(np.abs(om @ v[:L, :]) ** 2)
    return (w[i], v[:, i]) if vec else w[i]


def body_kappa(L, g, tau):  # hop amplitude of the band contract of one body (second-order Schrieffer-Wolff)
    e0, _, om = ground(L, [(0, g)])
    ek, uk, _ = ground(L, [(0, -g)])
    return -tau**2 / 4 * np.sum((uk.T @ np.roll(om, -1)) * (uk.T @ np.roll(om, 1)) / (e0[0] - ek))


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
    return (H0 + A1 + A1.conj().T + A2 + A2.conj().T).tocsr()


def parity_idx(L):  # the class r + s1 + s2 even (conserved), which contains the selected level
    s1, s2, r, _ = np.meshgrid(*(np.arange(k) for k in (2, 2, L, L)), indexing='ij')
    return np.flatnonzero(((s1 + s2 + r) % 2 == 0).ravel())


def midpoint_weights(L, z):  # source of unit strength at distance z from the pair's midpoint j + r/2
    w = np.zeros((L, L))
    for r in range(L):
        h = r - L if r > L // 2 else r
        for a in ([h // 2] if h % 2 == 0 else [(h - 1) // 2, (h + 1) // 2]):
            w[r, (z + a) % L] += 1.0 if h % 2 == 0 else 0.5
    return np.tile(w.ravel(), 4)


def band_contract(L, g1, g2, t1, t2):
    """Band contract (2.10) at P = 0 from the exact held blocks (class r even): E(r), d_i(r) on even r,
    kappa_i(rho) on odd rho (bond between rho-1 and rho+1); held spectra of the class."""
    E, Om = np.zeros(L), np.zeros((L, L))
    spec = {"G": [], "exc": [], "flip": [], "joint": []}
    for r in range(0, L, 2):
        e, _, om = ground(L, [(0, g1), (r, g2)])
        E[r], Om[r] = e[0], om
        spec["G"].append(e[0])
        spec["exc"] += list(e[1:])
        spec["joint"] += list(np.linalg.eigvalsh(field(L, [(0, -g1), (r, -g2)])))
    dd, kk = np.zeros((2, L)), np.zeros((2, L))
    for rm in range(1, L, 2):
        up, dn = (rm + 1) % L, rm - 1
        for i, (src, t, fu, fd) in enumerate((([(0, -g1), (rm, g2)], t1, np.roll(Om[up], -1), np.roll(Om[dn], 1)),
                                              ([(0, g1), (rm, -g2)], t2, Om[up], Om[dn]))):
            ek, uk = np.linalg.eigh(field(L, src))
            spec["flip"] += list(ek)
            ou, od, q = uk.T @ fu, uk.T @ fd, t**2 / 4
            dd[i, up] += q * np.sum(ou**2 / (E[up] - ek))
            dd[i, dn] += q * np.sum(od**2 / (E[dn] - ek))
            kk[i, rm] = -q * np.sum(ou * od * 0.5 * (1 / (E[up] - ek) + 1 / (E[dn] - ek)))
    return E, Om, dd, kk, {k: np.array(v) for k, v in spec.items()}


def run_case(name, L, g1, g2, t1, t2, dist=(), eig_s=None, d=0.02):
    n, l0 = 1.0 / L, ell(L, 0)
    ev = np.arange(0, L, 2)
    rs = np.where(ev > L // 2, ev - L, ev)  # signed even r
    E, Om, dd, kk, spec = band_contract(L, g1, g2, t1, t2)
    kb1, kb2 = body_kappa(L, g1, t1), body_kappa(L, g2, t2)
    low = (kb1 + kb2) < 0  # positive relative inertia: lowest edge
    U = E[ev] + dd[0][ev] + dd[1][ev]
    i0, i1 = np.arange(len(ev)), (np.arange(len(ev)) + 1) % len(ev)

    def band(P):
        h = np.diag(U).astype(complex)
        t = kk[0][ev + 1] * np.exp(-2j * P) + kk[1][ev + 1]  # <r|h|r+2>, bond rho = r+1
        h[i0, i1] += t
        h[i1, i0] += t.conj()
        w, v = np.linalg.eigh(h)
        k = 0 if low else -1
        return w[k], v[:, k]

    idx = parity_idx(L)
    cache = {}

    def exact(P):
        if P not in cache:
            eb, fb = band(P)
            w, v = spla.eigsh(pair_ops(L, g1, g2, t1, t2, P)[idx][:, idx].tocsc(), k=8, sigma=eb, which='LM', tol=0)
            best = (-1,)
            for k in range(len(w)):
                x = np.zeros(4 * L * L, complex)
                x[idx] = v[:, k]
                a = np.einsum('ry,ry->r', Om, x.reshape(2, 2, L, L)[0, 0])[ev]
                ov = abs(np.vdot(fb, a)) ** 2
                if ov > best[0]:
                    best = (ov, w[k], np.sum(np.abs(a) ** 2), x)
            cache[P] = best
        return cache[P]

    Eb2, Eb0 = curv(lambda P: exact(P)[1], d)
    ov0, _, gw0, v0 = exact(0.0)
    ovmin = min(c[0] for c in cache.values())
    Ebb2, _ = curv(lambda P: band(P)[0], d)
    mu = [1.0 / curv(lambda P: body_level(L, g, t, P), d)[0] for g, t in ((g1, t1), (g2, t2))]
    E1, E2 = body_level(L, g1, t1, 0.0), body_level(L, g2, t2, 0.0)
    D0 = 1.0 / Eb2 - mu[0] - mu[1]
    # band-contract quantities at P = 0
    _, f0 = band(0.0)
    f0 = (f0 * np.exp(-1j * np.angle(f0[0]))).real
    rho = (ev + 1) % L
    b0 = f0 * np.roll(f0, -1)  # f0(rho-1) f0(rho+1), rho = r+1
    k1, k2 = kk[0][ev + 1], kk[1][ev + 1]
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
    delta_m = abs(mu[0] + mu[1]) * (1 - beta0) / (abs(B(0)) * (1 / t1**2 + 1 / t2**2))  # S5 parameter
    # distances of G from the other held levels of its class (item 1, S2)
    G = spec["G"]
    dfl, djo = mindist(G, np.concatenate([spec["flip"], spec["exc"]])), mindist(G, spec["joint"])
    dall = min(dfl, djo)
    djo_lead = 2 * n * abs(g1 + g2) - 1.5 * abs(B(0))
    # local inertia (7.3): m_i(rho) - mubar_i against Mbar_i^odd(rho)/c_i^2 and Mbar^(2)(rho)/tau_i^2, |rho| <= 3
    near = np.abs(np.where(rho > L // 2, rho - L, rho)) <= 3
    loc, loc2 = [], []
    for k, kb, c, Mi, t in ((k1, kb1, cb[0], Mo[0], t1), (k2, kb2, cb[1], Mo[1], t2)):
        sh = (-1 / (8 * k) + 1 / (8 * kb))[near]
        loc.append(float(np.max(np.abs(sh / (bar(Mi) / c)[near] - 1))))
        loc2.append(float(np.max(np.abs(sh / (bar(B(ra)) / t**2)[near] - 1))))
    res = dict(case=name, L=L, g1=g1, g2=g2, tau1=t1, tau2=t2, eta=max(abs(g1), abs(g2)) * l0 / TF,
               w=w_est, mean_abs_r=float(np.sum(f0**2 * np.abs(rs))), overlap=ov0, min_overlap=ovmin,
               group_weight=gw0, selected="lowest" if low else "highest", d_all=dall, d_flip=dfl, d_joint=djo,
               d_joint_lead=djo_lead, tau_over_d=max(t1, t2) / dall, mu1=mu[0], mu2=mu[1],
               mu1_band=-1 / (8 * kb1), mu2_band=-1 / (8 * kb2),
               Epp_exact=Eb2, Epp_band=Ebb2, Epp_66=float(np.sum(b0 / (-1 / (8 * k1) - 1 / (8 * k2)))), beta0=beta0,
               delta_m=delta_m, D0_exact=D0, D0_band=Dband, Dlat=Dlat, Dmark_odd=Dmark, Dmark_lead=Dmark2,
               D0_formula=Dlat + Dmark, D0_resummed=Dres, D0_lead=Dlat + Dmark2, local_inertia_relerr_odd=loc,
               local_inertia_relerr_lead=loc2, dE0_exact=dE0, M_avg=Mavg, M_odd_avg=Moavg,
               M0_second_order=float(B(0)), K0=K0, dE0_formula=Mavg + K0)
    log(f"== {name}: L={L} g1={g1:.5g} g2={g2:.5g} tau1={t1:.4g} tau2={t2:.4g} eta={res['eta']:.3f} w={w_est:.2f}")
    log(f"   held spectra of the class: d={dall:.4e} (flips and excitations {dfl:.4e}, joint flip {djo:.4e}; "
        f"leading 2n|g1+g2|-1.5|B(0)|={djo_lead:.4e}); max tau/d={max(t1, t2) / dall:.3f}")
    log(f"   selected {res['selected']} level, <|r|>={res['mean_abs_r']:.2f}, overlap={ov0:.6f} (min over P {ovmin:.6f}), group weight={gw0:.6f}")
    log(f"   E''(0): exact={Eb2:.6e} band(2.10)={Ebb2:.6e} (6.6) sum b0/m={res['Epp_66']:.6e}  rel. band-exact={(Ebb2 - Eb2) / Eb2:.2e}")
    log(f"   mu1={mu[0]:.6e} mu2={mu[1]:.6e} (band: {-1 / (8 * kb1):.6e}, {-1 / (8 * kb2):.6e}) beta0={beta0:.5f}")
    log(f"   Dlat={Dlat:.4e} Dmark(odd parts)={Dmark:.4e} Dmark(lead)={Dmark2:.4e} |Dlat/Dmark|={abs(Dlat / Dmark):.3f} delta_m(S5)={delta_m:.3f}")
    log(f"   D0: exact={D0:.6e} band={Dband:.6e} (7.5)={Dlat + Dmark:.6e} resummed={Dres:.6e} leading={Dlat + Dmark2:.6e}")
    log(f"   deviation from exact D0 / (|Dlat|+|Dmark|): band {(Dband - D0) / Sc:.2e}, (7.5) {(Dlat + Dmark - D0) / Sc:.2e}, resummed {(Dres - D0) / Sc:.2e}, leading {(Dlat + Dmark2 - D0) / Sc:.2e}")
    log(f"   local inertia (7.3), max rel. error near r=0: odd parts {loc[0]:.2e}, {loc[1]:.2e}; second order {loc2[0]:.2e}, {loc2[1]:.2e}")
    log(f"   cost: dE0 exact={dE0:.6e} <M>+K0={Mavg + K0:.6e} (<M>={Mavg:.4e}, M2(0)={B(0):.4e}, K0={K0:.4e}); (<M1odd>+<M2odd>)/<M>={(Moavg[0] + Moavg[1]) / Mavg:.4f}")
    log(f"   D0_exact/dE0={D0 / dE0:.6e} vs 1/tau1^2+1/tau2^2={1 / t1**2 + 1 / t2**2:.6e} (ratio {D0 / dE0 / (1 / t1**2 + 1 / t2**2):.4f}), 1/tau1^2={1 / t1**2:.6e}")
    # ---------- item 4: weights ----------
    # exact selected level: field density at distance z from the pair's midpoint in the exact P=0 eigenvector
    # (first-order shift of the selected level by a source g_s at that place, Hellmann-Feynman)
    pr = (np.abs(v0) ** 2).reshape(4, L, L).sum(0)
    dens = np.zeros(L)
    for r in range(L):
        h = r - L if r > L // 2 else r
        dens += np.roll(pr[r], -(h // 2)) if h % 2 == 0 else 0.5 * (np.roll(pr[r], -((h - 1) // 2)) + np.roll(pr[r], -((h + 1) // 2)))
    dens_b = [np.abs(u[:L]) ** 2 + np.abs(u[L:]) ** 2 for u in (body_level(L, g, t, 0.0, vec=True)[1] for g, t in ((g1, t1), (g2, t2)))]
    res['weight'] = []
    for s in dist:
        dz = lambda f: -GS * (f[(s + 1) % L] - f[(s - 1) % L]) / 2
        W0p, W1p, W2p = dz(dens), dz(dens_b[0]), dz(dens_b[1])
        phip = -(2 * GS / TF) * (ell(L, 1 - s) - ell(L, -1 - s)) / 2
        u = s / L
        ks = (L * L * (1 - 2 * u) ** 2 + 2) / (L * L - 1)
        Vavg = np.sum(f0**2 * n * g1 * g2 / TF * np.mod(rs, L) * (L - np.mod(rs, L)) / L)
        Cev = [-n * g**2 / TF * l0 for g in (g1, g2)]
        # held-field average (v1): f0^2-average of exact held weights, no kinetic part
        X, xs = 0, s
        Wh = lambda src: (eps0(L, src + [(xs, GS)]) - eps0(L, src + [(xs, -GS)])) / 2
        dW = lambda fun: (fun(X + 1) - fun(X - 1)) / 2
        Wp = lambda Xc: np.sum([f0[i] ** 2 * Wh([(Xc - rs[i] // 2, g1), (Xc - rs[i] // 2 + rs[i], g2)]) for i in range(len(ev))])
        W0h, W1h, W2h = dW(Wp), dW(lambda x: Wh([(x, g1)])), dW(lambda x: Wh([(x, g2)]))
        Wbh = W0h - W1h - W2h
        Wbp = W0p - W1p - W2p
        Wbf = phip * (2 * ks * B(0) + Vavg - K0)  # (7.10)
        G1, G2, Gp, Gb = W1p / mu[0], W2p / mu[1], Eb2 * W0p, Wbp / D0
        Gb_lead = 2 * ks * phip / (1 / t1**2 + 1 / t2**2)  # (7.12)
        Gb_f = Wbf / (Dlat + Dmark2)
        Gb_r = (Wbh - K0 * phip) / (Dlat + Dmark)  # same structure with exact held weights and exact odd parts of M
        wr = dict(s=s, u=u, kappa_s=ks, phip=phip, W0p=W0p, W1p=W1p, W2p=W2p, Wbp=Wbp, Wbp_formula=Wbf,
                  W0p_heldavg=W0h, Wbp_heldavg=Wbh, kinetic=(Wbp - Wbh) / phip, kinetic_formula=-K0,
                  Gamma1=G1, Gamma2=G2, Gamma_pair=Gp, Gamma_bond=Gb, Gamma_bond_lead=Gb_lead,
                  Gamma_bond_formula=Gb_f, Gamma_bond_refined=Gb_r, eta_over_ks=res['eta'] / ks, w_over_Lks=w_est / (L * ks))
        log(f"   source at distance s={s} from the midpoint (u={u:.4f}, kappa_s={ks:.4f}; eta/kappa_s={wr['eta_over_ks']:.3f}, w/(L kappa_s)={wr['w_over_Lks']:.3f}):")
        log(f"     exact selected level: W0'/phi'={W0p / phip:.6e}  Wb'/phi'={Wbp / phip:.6e}  (7.10): {Wbf / phip:.6e}")
        log(f"     held-field average:   W0'/phi'={W0h / phip:.6e}  Wb'/phi'={Wbh / phip:.6e};  kinetic part (exact - held avg)/phi'={wr['kinetic']:.4e} vs -K0={-K0:.4e}")
        log(f"     Gamma/phi': body1={G1 / phip:.6e} (tau1^2={t1**2:.6e}) body2={G2 / phip:.6e} (tau2^2={t2**2:.6e}) pair={Gp / phip:.6e}")
        log(f"     Gamma_b=Wb'/D0: /phi'={Gb / phip:.6e}  (7.12) lead={Gb_lead / phip:.6e} (ratio {Gb / Gb_lead:.4f})  (7.10)/(7.5)={Gb_f / phip:.6e} (ratio {Gb / Gb_f:.4f})  refined={Gb_r / phip:.6e} (ratio {Gb / Gb_r:.4f})")
        log(f"     Gamma_b/Gamma_1={Gb / G1:.4f}  Gamma_b/Gamma_2={Gb / G2:.4f}  lead 2kappa_s/(1+tau1^2/tau2^2)={2 * ks / (1 + t1**2 / t2**2):.4f}")
        if s == eig_s:  # the same weight from exact eigenvalues of the sector contract with the source, +-g_s
            H0 = pair_ops(L, g1, g2, t1, t2, 0.0)[idx][:, idx].tocsc()
            dE = {}
            for z in (s - 1, s + 1):
                src = midpoint_weights(L, z)[idx]
                for sg in (1, -1):
                    w, v = spla.eigsh(H0 + sp.diags(sg * GS * src), k=6, sigma=Eb0, which='LM', tol=0)
                    dE[z, sg] = w[np.argmax(np.abs(v.conj().T @ v0[idx]))]
            W0e = -((dE[s + 1, 1] - dE[s + 1, -1]) - (dE[s - 1, 1] - dE[s - 1, -1])) / 4
            wr['W0p_eigenvalues'] = W0e
            log(f"     exact eigenvalues with the source (+-g_s): W0'/phi'={W0e / phip:.6e}, rel. diff. to the density form {(W0e - W0p) / W0p:.2e}; Wb'/phi' from them {(W0e - W1p - W2p) / phip:.6e}")
        res['weight'].append(wr)
    return res


def params(L, eta1, q, r1, r2=None):
    """g1 from eta1 = |g1| l0 / t_f, g2 = q g1, tau_i = r_i d with d = 2 n min|g_i|."""
    r2 = r1 if r2 is None else r2
    g1 = eta1 * TF / ell(L, 0)
    d = 2 * min(abs(g1), abs(q * g1)) / L
    return L, g1, q * g1, r1 * d, r2 * d


CASES = [("A equal bodies", (32, 0.15, 1.0, 0.3), (), None),
         ("A equal bodies", (64, 0.15, 1.0, 0.3), (8, 16), 8),
         ("A' equal bodies, smaller eta", (64, 0.05, 1.0, 0.3), (8, 16), None),
         ("A'' equal bodies, smaller eta and tau/d", (64, 0.05, 1.0, 0.15), (), None),
         ("B unequal bodies and speeds", (32, 0.15, 0.5, 0.3, 0.15), (), None),
         ("B unequal bodies and speeds", (64, 0.15, 0.5, 0.3, 0.15), (8, 16), None),
         ("R equal bodies, v1 case", (128, 0.15, 1.0, 0.3), (8, 16, 32), None),
         ("S1 equal bodies, regime (ii)", (256, 0.10, 1.0, 0.4), (16, 32, 64), 32),
         ("S2 equal bodies, regime (ii), smaller eta", (256, 0.05, 1.0, 0.4), (16, 32, 64), None),
         ("C mixed signs, bound at top", (48, 0.075, -2.0, 0.15, 0.3), (), None),
         ("D control: both negative, not bound", (48, -0.15, 1.0, 0.3), (), None)]

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    results = [run_case(name, *params(*p), dist=dist, eig_s=es) for name, p, dist, es in CASES]
    (OUT / "check_log.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
    (OUT / "check_results.json").write_text(json.dumps(results, indent=1, default=float), encoding="utf-8")
