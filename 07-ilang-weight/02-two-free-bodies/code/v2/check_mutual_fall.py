"""Check of item 3 (mutual fall) of 07-ilang-weight/02-two-free-bodies, v2.

Two Model D bodies of different types (each in one clock level: half-gap M_i, motion amplitude tau_i,
branch sigma_i, coupling (a) or (c) with constant gamma_i) and N_f = 1 field object on a ring of L places.
The total contract commutes with the joint translation (2.1); it is diagonalized in the L sectors of the
total plane-wave label P (representative: field object at y = 0, body positions relative to it).

Start (R3): product of real Gaussian envelopes phi_i centred at c_i, in the adiabatic basis
|x1,sigma1,x2,sigma2> (x) Omega(x1,x2) (Omega the lowest or highest field state of the held problem),
projected on the band (the levels connected to that group) and normalized.

Observables (Step 5, (2.18)):
  chart mean position <xhat_i>, xhat_i = sum_x chi_i(x) P_x^(i), chi_i(x) the representative of x in the
  window {c_i - L//2, ..., c_i - L//2 + L - 1}; the cut bond joins the last and the first place of it;
  a_i    = d^2<xhat_i>/dlambda^2 at 0 = -<[C,[C,xhat_i]]>, exact (full-space reconstruction of the state);
  a^w_i  = <i[C,v_i]>, v_i the winding current; eps_i = a_i - a^w_i (cut term, (2.18));
  a_evol = second derivative at 0 of <xhat_i>(lambda) from the joint evolution on [0, 60] (polynomial fit);
  p_i^cut(lambda): weight of body i on the four places around the cut, at 0 and max over the run;
  prediction (2.12): -E''_i sum (dchi_i(j)/2) w_i(j,l) d_i W(j,l) - (L/64) E''_i^2 Xi_i, E''_i from the band
  of the single body with the field, dchi_i(j) = chi_i(j+1) - chi_i(j-1), Xi_i the cut sum of (2.12);
  winding prediction (dchi = 2, no Xi term) for a^w_i;
  exact zeroth-order part a_i^(0) (same start, the other body uncoupled) and the ratio of the mutual parts
  (a_1 - a_1^(0)) / (a_2 - a_2^(0)) against -E''_1/E''_2 (2.13).
Isolation (R1): tau = 0 distances of the group to the levels with one branch flipped (delta_1), with the
  same branches and an excited field (delta_f), with both branches flipped (delta_2), delta = min of these;
  the same for each body alone; exact gap of the band at tau != 0 and weight of the band outside the group;
  tau'_i/delta_1 and tau'^2/(delta_1 delta), tau' = tau (a), tau (1 + |gamma| N_f) (c).
Conserved operator (2.17): ||[Q_i, C]|| with Q_i = (sum_x (-1)^x P_x^(i)) sigma_3^(i), on body i and the
  field object, for L = 14 (even) and L = 13 (odd, control).
Output: output/mutual_fall.json and output/mutual_fall.log
"""
import json
from pathlib import Path

import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

L = 14
TF = 0.5
LAM_MAX = 60.0
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S3 = np.diag([1.0, -1.0]).astype(complex)
I2 = np.eye(2)
IDX = {+1: 0, -1: 1}
PPOLY = np.polynomial.polynomial


def shift(n, k):
    """|x> -> |x+k> on a ring of n places."""
    S = np.zeros((n, n))
    for x in range(n):
        S[(x + k) % n, x] = 1.0
    return S


def h_field(pts, n=L):
    H = -TF * (shift(n, 1) + shift(n, -1))
    for x, g in pts:
        H[x, x] += g
    return H


def field_state(pts, top):
    w, V = np.linalg.eigh(h_field(pts))
    if top:
        v, e = V[:, -1], w[-1]
        v = v * np.sign(np.sum(v * (-1.0) ** np.arange(L)))
    else:
        v, e = V[:, 0], w[0]
        v = v * np.sign(np.sum(v))
    return e, v


def body_ops(b):
    """Own term + coupling (field object at y = 0) and winding current of one body, on (x, s): 2x+s."""
    M, tau, gam, cpl = b["M"], b["tau"], b["gamma"], b["coupling"]
    P0 = np.zeros((L, L)); P0[0, 0] = 1.0
    H = np.kron(np.eye(L), M * S3) + gam * M * np.kron(P0, S3)
    V = np.zeros((2 * L, 2 * L), dtype=complex)
    for x in range(L):
        f = 1.0
        if cpl == "c":
            f += gam * 0.5 * ((x == 0) + ((x + 1) % L == 0))
        E = np.zeros((L, L)); E[(x + 1) % L, x] = 1.0  # |x+1><x|
        H = H + 0.5 * tau * f * (np.kron(E, -1j * S1) + np.kron(E.T, 1j * S1))
        V = V - 0.5 * tau * f * (np.kron(E, S1) + np.kron(E.T, S1))
    return H, V


def body_field_ops(b, n):
    """Terms of C that act on body i, on (x, s) (x) field place y, ring of n places (N_f = 1).
    Returns C_loc and Q_i = Pi sigma_3."""
    M, tau, gam, cpl = b["M"], b["tau"], b["gamma"], b["coupling"]
    Ix = np.eye(n)

    def op(Ax, As, Ay):
        return np.kron(np.kron(Ax, As), Ay)

    C = op(Ix, I2, h_field([], n)).astype(complex)
    for x in range(n):
        Px = np.zeros((n, n)); Px[x, x] = 1.0
        C = C + M * op(Px, S3, Ix) + gam * M * op(Px, S3, Px)
    for x in range(n):
        E = np.zeros((n, n)); E[(x + 1) % n, x] = 1.0
        fac = Ix.copy()
        if cpl == "c":
            Ph = np.zeros((n, n)); Ph[x, x] += 0.5; Ph[(x + 1) % n, (x + 1) % n] += 0.5
            fac = fac + gam * Ph
        F = 0.5 * tau * op(E, -1j * S1, fac)
        C = C + F + F.conj().T
    Q = op(np.diag((-1.0) ** np.arange(n)), S3, Ix)
    return C, Q


def chart(c):
    """Chart values chi(x) in the window {c - L//2, ..., c - L//2 + L - 1}; cut bond (top, top+1)."""
    lo = c - L // 2
    x = np.arange(L)
    chi = (lo + (x - lo) % L).astype(float)
    top = (lo + L - 1) % L
    near = [(top + k) % L for k in (-1, 0, 1, 2)]
    return chi, top, near


def tau_prime(b):
    return b["tau"] * (1 + abs(b["gamma"])) if b["coupling"] == "c" else b["tau"]


def tau0_gaps(b1, b2, top):
    """Distances of the tau = 0 group from the other tau = 0 levels (two bodies; each body alone)."""
    sel = L - 1 if top else 0
    g1 = b1["sigma"] * b1["gamma"] * b1["M"]
    g2 = b2["sigma"] * b2["gamma"] * b2["M"]
    a1, a2 = b1["sigma"] * b1["M"], b2["sigma"] * b2["M"]

    def spec(pts):
        return np.linalg.eigvalsh(h_field(pts))

    EG, same, f1, f12 = [], [], [], []
    for d in range(L):
        e = spec([(0, g1), (d, g2)])
        EG.append(a1 + a2 + e[sel])
        same.extend(a1 + a2 + np.delete(e, sel))
        f1.extend(-a1 + a2 + spec([(0, -g1), (d, g2)]))
        f1.extend(a1 - a2 + spec([(0, g1), (d, -g2)]))
        f12.extend(-a1 - a2 + spec([(0, -g1), (d, -g2)]))
    EG = np.array(EG)

    def dist(S):
        return float(np.min(np.abs(EG[:, None] - np.array(S)[None, :])))

    out = {"delta_1": dist(f1), "delta_f": dist(same), "delta_2": dist(f12)}
    out["delta"] = min(out["delta_1"], out["delta_f"], out["delta_2"])
    for i, (b, g) in enumerate(((b1, g1), (b2, g2))):
        sM = b["sigma"] * b["M"]
        e, em = spec([(0, g)]), spec([(0, -g)])
        eg = sM + e[sel]
        out[f"body{i + 1}"] = {"delta_1": float(np.min(np.abs(eg - (-sM + em)))),
                               "delta_f": float(np.min(np.abs(eg - (sM + np.delete(e, sel)))))}
    return out


def single_band_curv(b, top):
    """E'' at the rest point of the band of one body with the field (N_f = 1); band leak and exact gap."""
    Hb, _ = body_ops(b)
    Sm = np.kron(shift(L, -1), I2)
    Sp = np.kron(shift(L, 1), I2)
    g = b["sigma"] * b["gamma"] * b["M"]
    _, om = field_state([(0, g)], top)
    Es, leak, gap = [], 0.0, np.inf
    for m in range(L):
        P = 2 * np.pi * m / L
        H = Hb - TF * (np.exp(-1j * P) * Sm + np.exp(1j * P) * Sp)
        w, V = np.linalg.eigh(H)
        G = np.zeros(2 * L, dtype=complex)
        for t in range(L):
            G[2 * ((-t) % L) + IDX[b["sigma"]]] = np.exp(-1j * P * t) * om[t]
        ov = np.abs(G.conj() @ V) ** 2
        k = int(np.argmax(ov))
        assert ov[k] > 0.5
        leak = max(leak, 1 - ov[k])
        gap = min(gap, float(np.min(np.abs(np.delete(w, k) - w[k]))))
        Es.append(w[k])
    Es = np.array(Es)
    rs = np.arange(-(L // 2) + 1, L // 2 + 1)
    Ps = 2 * np.pi * np.arange(L) / L
    kap = np.array([np.mean(Es * np.exp(1j * Ps * r)) for r in rs])
    Prest = np.pi if top else 0.0
    return float(np.real(-np.sum(rs ** 2 * kap * np.exp(-1j * Prest * rs)))), leak, gap


def gauss(center, w):
    j = np.arange(L)
    dj = (j - center + L / 2) % L - L / 2
    f = np.exp(-dj ** 2 / (4 * w ** 2))
    return f / np.linalg.norm(f)


def run_case(b1, b2, top, xc, widths, scale, only_acc=False):
    b1 = dict(b1, tau=b1["tau"] * scale)
    b2 = dict(b2, tau=b2["tau"] * scale)
    if not only_acc:
        # exact zeroth-order parts a_i^(0): the same start with the other body uncoupled
        a01 = run_case(b1, dict(b2, gamma=0.0), top, xc, widths, 1.0, only_acc=True)[0]
        a02 = run_case(dict(b1, gamma=0.0), b2, top, xc, widths, 1.0, only_acc=True)[1]
    g1 = b1["sigma"] * b1["gamma"] * b1["M"]
    g2 = b2["sigma"] * b2["gamma"] * b2["M"]
    D = 4 * L * L
    H1, V1 = body_ops(b1)
    H2, V2 = body_ops(b2)
    I = np.eye(2 * L)
    H0 = np.kron(H1, I) + np.kron(I, H2)
    v1 = np.kron(V1, I)
    v2 = np.kron(I, V2)
    Sm = np.kron(np.kron(shift(L, -1), I2), np.kron(shift(L, -1), I2))
    Sp = Sm.T
    # held problem: field states and eigenvalues W(j,l)
    W = np.zeros((L, L))
    Om = np.zeros((L, L, L))
    for j in range(L):
        for l in range(L):
            W[j, l], Om[j, l] = field_state([(j, g1), (l, g2)], top)
    phi1 = gauss(xc[0], widths[0])
    phi2 = gauss(xc[1], widths[1])
    s1, s2 = IDX[b1["sigma"]], IDX[b2["sigma"]]

    def rep(x1, x2):
        return ((2 * (x1 % L) + s1) * L + (x2 % L)) * 2 + s2

    tt = np.arange(L)
    X1 = (tt[None, :, None] + tt[:, None, None]) % L   # [t, x1, 1] -> x1 + t
    X2 = (tt[None, None, :] + tt[:, None, None]) % L   # [t, 1, x2] -> x2 + t
    F = phi1[X1] * phi2[X2] * Om[X1, X2, tt[:, None, None]]
    norm2, store, leak, bgap = 0.0, [], 0.0, np.inf
    for m in range(L):
        P = 2 * np.pi * m / L
        H = H0 - TF * (np.exp(-1j * P) * Sm + np.exp(1j * P) * Sp)
        w, V = np.linalg.eigh(H)
        G = np.zeros((D, L), dtype=complex)
        for d in range(L):
            for t in range(L):
                G[rep(-t, d - t), d] = np.exp(-1j * P * t) * Om[0, d % L][t]
        ov = np.sum(np.abs(G.conj().T @ V) ** 2, axis=0)
        band = ov > 0.5
        assert band.sum() == L, band.sum()
        leak = max(leak, float(1 - ov[band].min()))
        bgap = min(bgap, float(np.min(np.abs(w[band][:, None] - w[~band][None, :]))))
        Vb, Eb = V[:, band], w[band]
        psi = np.zeros(D, dtype=complex)
        amp = np.einsum("t,txy->xy", np.exp(-1j * P * tt), F) / np.sqrt(L)
        for x1 in range(L):
            for x2 in range(L):
                psi[rep(x1, x2)] = amp[x1, x2]
        c = Vb.conj().T @ psi
        norm2 += np.vdot(c, c).real
        store.append((H, Vb, Eb, c))
    store = [(H, Vb, Eb, c / np.sqrt(norm2)) for H, Vb, Eb, c in store]
    Ebar = float(np.mean(np.concatenate([s[2] for s in store])))
    # winding-current accelerations a^w_i = <i[C, v_i]>, sector by sector
    aw = np.zeros(2)
    for H, Vb, Eb, c in store:
        ps = Vb @ c
        for i, v in enumerate((v1, v2)):
            aw[i] += np.real(np.vdot(ps, 1j * (H @ (v @ ps) - v @ (H @ ps))))

    def full(power, lam=0.0):
        """(C - Ebar)^power exp(-i C lam) Psi(0) on the full space: [t, r1, s1, r2, s2] with
        body 1 at r1 + t, body 2 at r2 + t, field object at t."""
        vecs = np.array([Vb @ (((Eb - Ebar) ** power) * np.exp(-1j * Eb * lam) * c)
                         for _, Vb, Eb, c in store])
        return (np.fft.ifft(vecs, axis=0) * np.sqrt(L)).reshape(L, L, 2, L, 2)

    chi1, cut1, near1 = chart(xc[0])
    chi2, cut2, near2 = chart(xc[1])
    pos = (tt[:, None] + tt[None, :]) % L   # pos[t, r] = r + t
    CH = [chi1[pos][:, :, None, None, None], chi2[pos][:, None, None, :, None]]
    NE = [np.isin(pos, near1)[:, :, None, None, None].astype(float),
          np.isin(pos, near2)[:, None, None, :, None].astype(float)]
    Ps0, CPs, C2Ps = full(0), full(1), full(2)
    ach = np.array([2 * np.sum(CH[i] * np.abs(CPs) ** 2)
                    - 2 * np.real(np.sum(CH[i] * np.conj(C2Ps) * Ps0)) for i in range(2)])
    vch = np.array([-2 * np.imag(np.sum(CH[i] * np.conj(CPs) * Ps0)) for i in range(2)])
    if only_acc:
        return ach
    pcut0 = np.array([np.sum(NE[i] * np.abs(Ps0) ** 2) for i in range(2)])
    # joint evolution of the chart mean positions
    lam = np.linspace(0.0, LAM_MAX, 31)
    xs = np.zeros((len(lam), 2))
    pc = np.zeros((len(lam), 2))
    for k, la in enumerate(lam):
        pr = np.abs(full(0, la)) ** 2
        xs[k] = [np.sum(CH[i] * pr) for i in range(2)]
        pc[k] = [np.sum(NE[i] * pr) for i in range(2)]
    u = lam / LAM_MAX
    aev = np.array([2 * PPOLY.polyfit(u, xs[:, i], 6)[2] / LAM_MAX ** 2 for i in range(2)])
    eps = ach - aw
    # prediction (2.12): chart weights dchi/2 and the free-packet cut term -(L/64) E''^2 Xi
    Ec1, leak1, gap1 = single_band_curv(b1, top)
    Ec2, leak2, gap2 = single_band_curv(b2, top)
    j = np.arange(L)
    d1W = (W[(j + 1) % L, :] - W[(j - 1) % L, :]) / 2          # d1W[j, l]
    d2W = (W[:, (j + 1) % L] - W[:, (j - 1) % L]) / 2          # d2W[j, l]
    dchi1 = (chi1[(j + 1) % L] - chi1[(j - 1) % L]) / 2
    dchi2 = (chi2[(j + 1) % L] - chi2[(j - 1) % L]) / 2
    w1 = np.outer(phi1[(j + 1) % L] * phi1[(j - 1) % L] * dchi1, phi2 ** 2)
    w2 = np.outer(phi1 ** 2, phi2[(j + 1) % L] * phi2[(j - 1) % L] * dchi2)
    w1w = np.outer(phi1[(j + 1) % L] * phi1[(j - 1) % L], phi2 ** 2)
    w2w = np.outer(phi1 ** 2, phi2[(j + 1) % L] * phi2[(j - 1) % L])

    def xi(phi, a):
        f = lambda k: phi[(a + k) % L]
        return 2 * (f(-1) * f(3) + f(0) * f(4) - f(-3) * f(1) - f(-2) * f(2)
                    + f(-1) ** 2 + f(0) ** 2 - f(1) ** 2 - f(2) ** 2)

    a0 = np.array([-L / 64 * Ec1 ** 2 * xi(phi1, cut1), -L / 64 * Ec2 ** 2 * xi(phi2, cut2)])
    pred1 = np.array([-Ec1 * np.sum(w1 * d1W), -Ec2 * np.sum(w2 * d2W)])
    pred = pred1 + a0
    predw = np.array([-Ec1 * np.sum(w1w * d1W), -Ec2 * np.sum(w2w * d2W)])
    # in-situ estimate (2.16): relative change -/+ gamma_i * [1,2,1]/4-average of the change of the
    # field density made by the other body at the hopping body's place; upper sign (a), lower (c)
    drho2 = np.array([field_state([(l, g2)], top)[1] ** 2 - 1.0 / L for l in range(L)])  # [l, y]
    drho1 = np.array([field_state([(l, g1)], top)[1] ** 2 - 1.0 / L for l in range(L)])  # [j, y]
    av2 = (np.roll(drho2, 1, axis=1) + 2 * drho2 + np.roll(drho2, -1, axis=1)) / 4
    av1 = (np.roll(drho1, 1, axis=1) + 2 * drho1 + np.roll(drho1, -1, axis=1)) / 4
    R1 = av2.T            # R1[j, l]: average density change by body 2 (at l) around place j
    R2 = av1              # R2[j, l]: average density change by body 1 (at j) around place l
    sg = [(-1.0 if b["coupling"] == "a" else 1.0) * b["gamma"] for b in (b1, b2)]
    insitu = np.array([sg[0] * np.sum(w1 * R1 * d1W) / np.sum(w1 * d1W),
                       sg[1] * np.sum(w2 * R2 * d2W) / np.sum(w2 * d2W)])
    tp = [tau_prime(b1), tau_prime(b2)]
    return {"scale": scale, "a_chart": ach.tolist(), "a_winding": aw.tolist(), "eps_cut": eps.tolist(),
            "pcut_0": pcut0.tolist(), "pcut_max_run": pc.max(axis=0).tolist(),
            "a_evolution": aev.tolist(), "v_chart_0": vch.tolist(),
            "a_pred": pred.tolist(), "a_pred_first_order": pred1.tolist(), "a_free_cut": a0.tolist(),
            "a_pred_winding": predw.tolist(), "Epp": [Ec1, Ec2],
            "a_zeroth_exact": [a01, a02],
            "ratio_mutual": (ach[0] - a01) / (ach[1] - a02),
            "ratio_mutual_over_inertia_minus_1": (ach[0] - a01) / (ach[1] - a02) / (-Ec1 / Ec2) - 1,
            "ratio_first_order_pred_over_inertia_minus_1": pred1[0] / pred1[1] / (-Ec1 / Ec2) - 1,
            "dev": (ach / pred - 1).tolist(), "dev_winding": (aw / predw - 1).tolist(),
            "evol_vs_exact": (aev / ach - 1).tolist(),
            "ratio_exact": ach[0] / ach[1], "ratio_pred": pred[0] / pred[1],
            "inertia_ratio": -Ec1 / Ec2, "insitu_est": insitu.tolist(),
            "band_gap_exact": bgap, "band_leak": leak,
            "single_body": [{"leak": leak1, "gap_exact": gap1}, {"leak": leak2, "gap_exact": gap2}],
            "tau_prime": tp,
            "c_factors": [float(np.sum(phi1[(j + 1) % L] * phi1[(j - 1) % L])),
                          float(np.sum(phi2[(j + 1) % L] * phi2[(j - 1) % L]))]}


CASES = [
    {"name": "A: (a), sigma=(+,+), lowest", "top": False,
     "b1": {"M": 2.0, "tau": 0.10, "gamma": 0.025, "sigma": +1, "coupling": "a"},
     "b2": {"M": 3.0, "tau": 0.15, "gamma": 0.02, "sigma": +1, "coupling": "a"},
     "xc": (3, 8), "widths": (1.3, 1.3)},
    {"name": "B: (c), sigma=(+,-), lowest", "top": False,
     "b1": {"M": 2.5, "tau": 0.12, "gamma": 0.02, "sigma": +1, "coupling": "c"},
     "b2": {"M": 1.6, "tau": 0.08, "gamma": 0.03, "sigma": -1, "coupling": "c"},
     "xc": (3, 8), "widths": (1.3, 1.3)},
    {"name": "C: (a), sigma=(-,-), highest", "top": True,
     "b1": {"M": 2.0, "tau": 0.10, "gamma": 0.025, "sigma": -1, "coupling": "a"},
     "b2": {"M": 3.0, "tau": 0.15, "gamma": 0.02, "sigma": -1, "coupling": "a"},
     "xc": (3, 8), "widths": (1.3, 1.3)},
    {"name": "D: (c), sigma=(+,+), lowest, unequal widths", "top": False,
     "b1": {"M": 2.0, "tau": 0.10, "gamma": 0.025, "sigma": +1, "coupling": "c"},
     "b2": {"M": 3.0, "tau": 0.15, "gamma": 0.02, "sigma": +1, "coupling": "c"},
     "xc": (3, 8), "widths": (1.1, 1.6)},
    {"name": "E: (c), sigma=(+,+), lowest", "top": False,
     "b1": {"M": 2.0, "tau": 0.10, "gamma": 0.025, "sigma": +1, "coupling": "c"},
     "b2": {"M": 3.0, "tau": 0.15, "gamma": 0.02, "sigma": +1, "coupling": "c"},
     "xc": (3, 8), "widths": (1.3, 1.3)},
]


GAMMA_SCAN = []
for base in (CASES[0], CASES[4]):
    GAMMA_SCAN.append({"name": base["name"][:2] + " with gamma_1, gamma_2 times 0.5", "top": False,
                       "b1": dict(base["b1"], gamma=base["b1"]["gamma"] * 0.5),
                       "b2": dict(base["b2"], gamma=base["b2"]["gamma"] * 0.5),
                       "xc": (3, 8), "widths": (1.3, 1.3)})


def q_check():
    """||[Q_i, C_loc]|| for the bodies of cases A (coupling a) and E (coupling c), L = 14 and L = 13."""
    res = []
    for case in (CASES[0], CASES[4]):
        for b in (case["b1"], case["b2"]):
            for n in (14, 13):
                Cl, Q = body_field_ops(b, n)
                res.append({"case": case["name"][:2], "coupling": b["coupling"], "M": b["M"], "L": n,
                            "norm_comm": float(np.linalg.norm(Q @ Cl - Cl @ Q, 2))})
    return res


def main():
    results = {"L": L, "t_f": TF, "N_f": 1, "lambda_max": LAM_MAX, "q_check": q_check(), "cases": []}
    lines = [f"L={L} t_f={TF} N_f=1; scales s multiply tau_1, tau_2; evolution on [0, {LAM_MAX}]"]
    for q in results["q_check"]:
        lines.append(f"  (2.17) ||[Q,C]||: case {q['case']} coupling {q['coupling']} M={q['M']} "
                     f"L={q['L']}: {q['norm_comm']:.2e}")
    for case in CASES + GAMMA_SCAN:
        gaps = tau0_gaps(case["b1"], case["b2"], case["top"])
        runs = [run_case(case["b1"], case["b2"], case["top"], case["xc"], case["widths"], s)
                for s in (1.0, 0.5, 0.25)]
        ss = np.array([r["scale"] for r in runs])
        A = np.vstack([np.ones(3), ss ** 2, ss ** 4]).T
        dev0 = [float(np.linalg.solve(A, np.array([r["dev"][i] for r in runs]))[0]) for i in range(2)]
        rr = np.array([r["ratio_exact"] / r["ratio_pred"] - 1 for r in runs])
        rdev0 = float(np.linalg.solve(A, rr)[0])
        for r in runs:
            r["tau_prime_over_delta_1"] = max(r["tau_prime"]) / gaps["delta_1"]
            r["tau_prime2_over_delta_1_delta"] = max(r["tau_prime"]) ** 2 / (gaps["delta_1"] * gaps["delta"])
        res = {"case": case["name"], "params": {k: case[k] for k in ("b1", "b2", "xc", "widths", "top")},
               "tau0_gaps": gaps, "runs": runs, "dev_extrapolated_tau0": dev0,
               "ratio_dev_extrapolated_tau0": rdev0, "insitu_estimate": runs[0]["insitu_est"],
               "insitu_ratio_estimate": runs[0]["insitu_est"][0] - runs[0]["insitu_est"][1]}
        results["cases"].append(res)
        n0 = len(lines)
        lines.append(case["name"] + f"  b1={case['b1']}  b2={case['b2']}  centres={case['xc']}"
                     f" widths={case['widths']}")
        lines.append("  tau=0 gaps: delta_1={:.4f} delta_f={:.4f} delta_2={:.4f} delta={:.4f}; body1 "
                     "(delta_1={:.4f}, delta_f={:.4f}) body2 (delta_1={:.4f}, delta_f={:.4f})".format(
                         gaps["delta_1"], gaps["delta_f"], gaps["delta_2"], gaps["delta"],
                         gaps["body1"]["delta_1"], gaps["body1"]["delta_f"],
                         gaps["body2"]["delta_1"], gaps["body2"]["delta_f"]))
        for r in runs:
            lines.append("  s={}: a=({:.6e},{:.6e}) a_evol/a-1=({:.1e},{:.1e}) v(0)=({:.1e},{:.1e})".format(
                r["scale"], *r["a_chart"], *r["evol_vs_exact"], *r["v_chart_0"]))
            lines.append("        a^w=({:.6e},{:.6e}) eps_cut=a-a^w=({:.2e},{:.2e}) "
                         "p_cut(0)=({:.1e},{:.1e}) max p_cut=({:.1e},{:.1e})".format(
                             *r["a_winding"], *r["eps_cut"], *r["pcut_0"], *r["pcut_max_run"]))
            lines.append("        a_pred=({:.6e},{:.6e}) [free-packet term ({:.2e},{:.2e}); exact a^(0)=({:.2e},{:.2e})]"
                         " E''=({:.6e},{:.6e}) dev=({:.3e},{:.3e}) dev_w=({:.3e},{:.3e})".format(
                             *r["a_pred"], *r["a_free_cut"], *r["a_zeroth_exact"], *r["Epp"], *r["dev"],
                             *r["dev_winding"]))
            lines.append("        ratio exact={:.6f} pred={:.6f} -E''1/E''2={:.6f}; mutual ratio (a-a^(0))={:.6f}, "
                         "/(-E''1/E''2)-1={:.2e} (first-order pred: {:.2e}) c=({:.4f},{:.4f})".format(
                             r["ratio_exact"], r["ratio_pred"], r["inertia_ratio"], r["ratio_mutual"],
                             r["ratio_mutual_over_inertia_minus_1"],
                             r["ratio_first_order_pred_over_inertia_minus_1"], *r["c_factors"]))
            lines.append("        band gap={:.4f} band leak={:.1e} single (gap, leak)=({:.4f},{:.1e}),"
                         "({:.4f},{:.1e}) tau'/delta_1={:.3f} tau'^2/(delta_1 delta)={:.3f}".format(
                             r["band_gap_exact"], r["band_leak"], r["single_body"][0]["gap_exact"],
                             r["single_body"][0]["leak"], r["single_body"][1]["gap_exact"],
                             r["single_body"][1]["leak"], r["tau_prime_over_delta_1"],
                             r["tau_prime2_over_delta_1_delta"]))
        lines.append("  extrapolated (s->0) dev_i = ({:.3e}, {:.3e}); in-situ estimate (2.16) = ({:.3e}, {:.3e})"
                     .format(dev0[0], dev0[1], res["insitu_estimate"][0], res["insitu_estimate"][1]))
        lines.append("  extrapolated ratio deviation = {:.3e}; in-situ estimate (2.19) = {:.3e}"
                     .format(rdev0, res["insitu_ratio_estimate"]))
        print("\n".join(lines[n0:]), flush=True)
    (OUT / "mutual_fall.json").write_text(json.dumps(results, indent=1))
    (OUT / "mutual_fall.log").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
