"""Numerical check for 13-pair-fall, derivation v4 (role: check).

The script of v3 with the paths changed and one table added (second_derivative_table,
for Step 5.3: the second derivative at lambda = 0 of the function c_i(lambda; P) of
(13.29), against (13.29) and (13.30)); the evolution, its parameters and the other
tables are unchanged.

A packet of a bound pair of two Model D bodies is built from the numerical bound
level of the fibre contract H(P) (11.1), put on a finite chain |x_i| <= L and
evolved by C_bod (13.2) with small gradients (Chebyshev expansion of
exp(-i C_bod lambda)). The first order in the gradients is a symmetric
difference of two evolutions (+eps, -eps).

Compared with the derivation:
  (13.7)  slope of the first-order velocities of both parts = <alpha>_g, with
          alpha(P) of (13.8) computed from the numerical bound level;
  (13.10) first-order change of the mean label separation = lambda <beta>_g + bounded;
  (13.13) closed form of the drift acceleration from rest in the regime R;
  (13.22) derivative of the clock ratio Gamma_i = dE_b(0)/dM_i in the data M_1, M_2
          (second derivatives of the level), from the numerical bound level at P = 0,
          and with it the term of order eps^2 of (13.18);
  Step 5.3 d<K>_P/dP and f_i = Re F_{i,Lambda}(P) for windows [0, Lambda], from the
          numerical bound level at P = 0 and P = 0.2, and the identity (13.6);
  (13.29), (13.30) the second derivative at lambda = 0 of
          c_i(lambda; P) = Re <V_i psi| R exp(-i (H - E_b) lambda) |K psi>, from the
          numerical bound level at P = 0.1 and P = 0.2.

Sets: S1-S3 in the regime R (tau_i/M_i <= 0.2; S2 with tau_1 != tau_2, M_1 != M_2;
S3 with w_11 > 0), S4 with tau_i/M_i of order one, S5 a control (binding of range 1
without symmetry, moving packet). Each with the common gradient, with g_1 only,
and with a plain gradient in the place of kappa<X>.

Run from the project root:
  .venv/Scripts/python.exe 05-ilang-free-fall/13-pair-fall/code/v4/pair_fall_check.py
Optional arguments: names of sets or variants (default: all).
Outputs: output/results.json, output/summary.txt, output/first_order_motion.png
"""
import os
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import json
import sys
import time
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import scipy.sparse as sp
from scipy.special import jv

try:                                    # in-place Y += A X; the public product is the fallback
    from scipy.sparse._sparsetools import csr_matvecs
except ImportError:
    csr_matvecs = None

OUT = Path(__file__).parent / "output"
ETA = 0.5                      # phase convention of (11.1); results do not depend on it
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S3 = np.diag([1.0, -1.0]).astype(complex)
I2 = np.eye(2, dtype=complex)
S1A, S1B = np.kron(S1, I2), np.kron(I2, S1)      # branch index = 2*s1 + s2
S3A, S3B = np.kron(S3, I2).real.diagonal(), np.kron(I2, S3).real.diagonal()


def diag_w(w11, w12, w21, w22):
    return {0: np.diag([w11, w12, w21, w22]).astype(complex)}


def control_w():
    """Binding of the class W with range 1: not diagonal, no symmetry r -> -r or P -> -P."""
    w = diag_w(-0.5, 0.3, -0.2, 0.4)
    w1 = np.zeros((4, 4), dtype=complex)
    w1[0, 0] = -0.6
    w1[0, 1], w1[1, 0] = 0.3j, -0.3j
    w1[0, 3], w1[3, 0] = 0.2 + 0.15j, 0.2 - 0.15j
    w[1] = w1
    return w


# tau_i, M_i, binding, packet (P0, half support Pc, centre label xc), chain L, fibre range rmax,
# range of lambda, sampling step (a number, or an interval from which the step with the largest
# alias margin is taken), gradient eps (g); the plain gradient is eps*(M1+M2)/2;
# cfgs: 0 common gradient, 1 g1 only, 2 plain gradient
BASE = {
    "S1": dict(t1=0.20, M1=1.0, t2=0.20, M2=1.0, W=diag_w(-0.020, 0.012, 0.012, 0.016), R=True, lam_max=3000.0, dlam=(32.0, 44.0), eps=5e-7),
    "S2": dict(t1=0.20, M1=1.0, t2=0.18, M2=1.25, W=diag_w(-0.020, 0.010, -0.006, 0.020), R=True, lam_max=3000.0, dlam=(32.0, 44.0), eps=5e-7),
    "S3": dict(t1=0.20, M1=1.0, t2=0.17, M2=0.9, W=diag_w(0.022, -0.010, 0.007, -0.015), R=True, lam_max=3000.0, dlam=(32.0, 44.0), eps=5e-7),
    "S4": dict(t1=1.00, M1=1.0, t2=0.80, M2=1.2, W=diag_w(-0.9, 0.3, -0.2, 0.4), R=False, lam_max=200.0, dlam=1.0, eps=2e-6),
    "S5": dict(t1=1.00, M1=1.0, t2=0.80, M2=1.2, W=control_w(), R=False, lam_max=400.0, dlam=1.0, eps=2e-6,
               P0=0.2, Pc=0.4, xc=-12),
}
DEFAULT = dict(P0=0.0, Pc=0.5, xc=0, L=60, rmax=48, cfgs=(0, 1, 2))
# convergence variants: one numerical parameter changed, only the configuration "g1 only"
VARIANTS = {
    "S1_L45": ("S1", dict(L=45)),
    "S1_eps2": ("S1", dict(eps=1e-6)),
    "S1_Pc035": ("S1", dict(Pc=0.35)),
    "S1_dlam": ("S1", dict(dlam=(20.0, 28.0))),
    "S4_L45": ("S4", dict(L=45)),
    "S5_L75": ("S5", dict(L=75)),
    "S5_long": ("S5", dict(L=75, lam_max=600.0, xc=-15)),
}
LABELS = ("common gradient g1=g2", "g1 only (g2=0)", "plain gradient")


# ---------------------------------------------------------------- fibre H(P)
def bands(P, p):
    q = np.linspace(-np.pi, np.pi, 4001)
    o1 = np.sqrt(p["M1"] ** 2 + p["t1"] ** 2 * np.sin(q) ** 2)
    o2 = np.sqrt(p["M2"] ** 2 + p["t2"] ** 2 * np.sin(P - q) ** 2)
    out = []
    for s1 in (1, -1):
        for s2 in (1, -1):
            e = s1 * o1 + s2 * o2
            out.append((e.min(), e.max()))
    return out


def fibre_ops(P, p, rmax):
    nr = 2 * rmax + 1
    S = np.eye(nr, k=-1).astype(complex)            # (S psi)(r) = psi(r-1)
    Sd = S.T
    e1, e2 = np.exp(1j * ETA * P), np.exp(1j * (1 - ETA) * P)
    A1 = 0.5j * p["t1"] * np.kron(e1 * Sd - np.conj(e1) * S, S1A)
    A2 = 0.5j * p["t2"] * np.kron(e2 * S - np.conj(e2) * Sd, S1B)
    V1 = -0.5 * p["t1"] * np.kron(e1 * Sd + np.conj(e1) * S, S1A)
    V2 = -0.5 * p["t2"] * np.kron(e2 * S + np.conj(e2) * Sd, S1B)
    H = A1 + A2 + np.diag(np.kron(np.ones(nr), p["M1"] * S3A + p["M2"] * S3B))
    for r, Wr in p["W"].items():
        i = (r + rmax) * 4
        H[i:i + 4, i:i + 4] += Wr
    d2H = -ETA ** 2 * A1 - (1 - ETA) ** 2 * A2
    return H, V1, V2, d2H


def level(P, p, rmax):
    """Bound level of H(P) attached to the band B_++ and the functions of item 2."""
    nr = 2 * rmax + 1
    H, V1, V2, d2H = fibre_ops(P, p, rmax)
    vals, vecs = np.linalg.eigh(H)
    b = int(np.argmax(np.abs(vecs[rmax * 4, :]) ** 2))     # weight on r = 0, branch |11>
    psi = vecs[:, b] * np.exp(-1j * np.angle(vecs[rmax * 4, b]))
    Eb = vals[b]
    dE = vals - Eb
    gap = np.min(np.abs(np.delete(dE, b)))
    dE[b] = np.inf

    def Rap(x):                                           # Q (H - Eb)^-1 Q x
        return vecs @ ((vecs.conj().T @ x) / dE)

    rvec = np.kron(np.arange(-rmax, rmax + 1), np.ones(4))
    s3 = [np.kron(np.ones(nr), S3A), np.kron(np.ones(nr), S3B)]
    Mi = [p["M1"], p["M2"]]
    vpsi = (ETA * V1 + (1 - ETA) * V2) @ psi
    Rv = Rap(vpsi)
    E1 = np.vdot(psi, vpsi).real
    E2 = np.vdot(psi, d2H @ psi).real - 2 * np.vdot(vpsi, Rv).real

    def ev(d):
        return np.vdot(psi, d * psi).real

    dPr = -2 * np.vdot(rvec * psi, Rv).real
    alpha, beta, s3m = [], [], []
    for i in range(2):
        s3m.append(ev(s3[i]))
        dPs3 = -2 * np.vdot(s3[i] * psi, Rv).real
        rRs3 = 2 * np.vdot(rvec * psi, Rap(s3[i] * psi)).real
        alpha.append(-Mi[i] * (E2 * s3m[i] - E1 * dPs3))          # coefficient of g_i  (13.8)
        beta.append(-Mi[i] * (s3m[i] * dPr + E1 * rRs3))          # coefficient of g_i  (13.10)
    alpha.append(-2 * E2)                                         # coefficient of kappa<X>
    beta.append(-2 * dPr)
    bd = bands(P, p)
    dist_band = min(min(abs(Eb - lo), abs(Eb - hi)) for lo, hi in bd)
    inside = any(lo <= Eb <= hi for lo, hi in bd)
    return dict(Eb=Eb, psi=psi, E1=E1, E2=E2, s3=s3m, alpha=alpha, beta=beta, gap=gap,
                freqs=np.abs(np.delete(vals - Eb, b)),
                v1=np.vdot(psi, V1 @ psi).real, v2=np.vdot(psi, V2 @ psi).real,
                rmean=ev(rvec), dist_band=dist_band, inside=inside,
                tail=float(np.abs(psi[:4]).max() + np.abs(psi[-4:]).max()))


def closed_form(p):
    """Leading order in R, (13.13): coefficients of g_1, g_2, kappa<X> at P0 = 0."""
    t1, t2, w = p["t1"], p["t2"], p["W"][0][0, 0].real
    a1, a2 = t1 ** 2 / (4 * p["M1"]), t2 ** 2 / (4 * p["M2"])
    u = abs(w) / (a1 + a2)
    pref = np.sign(w) / np.sqrt(1 + u * u) / (p["M1"] / t1 ** 2 + p["M2"] / t2 ** 2)
    return [pref * p["M1"], pref * p["M2"], 2 * pref], u


def closed_form_packet(p, Pg, wg2):
    """(11.12) averaged over |g|^2: -<E_b''> (g1 M1 + g2 M2 + 2 kappa<X>)."""
    w = p["W"][0][0, 0].real
    a1, a2 = p["t1"] ** 2 / (4 * p["M1"]), p["t2"] ** 2 / (4 * p["M2"])
    j2 = a1 * a1 + a2 * a2 + 2 * a1 * a2 * np.cos(2 * Pg)
    s = np.sqrt(w * w + j2)
    E2 = np.sign(w) * (-8 * a1 * a2 * np.cos(2 * Pg) / (2 * s) - (4 * a1 * a2 * np.sin(2 * Pg)) ** 2 / (4 * s ** 3))
    m = -np.sum(wg2 * E2)
    return [m * p["M1"], m * p["M2"], 2 * m]


# ---------------------------------------------------------------- real chain
def real_ops(p, L):
    n = 2 * L + 1
    x = np.arange(-L, L + 1).astype(float)
    T = sp.eye(n, k=-1, format="csr", dtype=complex)        # |x+1><x|
    Xs = sp.diags(np.kron(x, np.ones(2))).tocsr()
    Id = sp.identity(2 * n, format="csr", dtype=complex)

    def body(t, M):
        h = 0.5 * t * (sp.kron(T, -1j * S1) + sp.kron(T.T, 1j * S1)) + M * sp.kron(sp.identity(n), S3)
        h = h.tocsr()
        return h, (1j * (h @ Xs - Xs @ h)).tocsr()          # V = i [C, x]

    h1, v1 = body(p["t1"], p["M1"])
    h2, v2 = body(p["t2"], p["M2"])
    rows, cols, data = [], [], []
    for r, Wr in p["W"].items():
        i2 = np.arange(n)
        i1 = i2 + r
        ok = (i1 >= 0) & (i1 < n)
        i1, i2 = i1[ok], i2[ok]
        for a in range(4):
            for b in range(4):
                if Wr[a, b] != 0:
                    rows.append((i1 * 2 + a // 2) * 2 * n + i2 * 2 + a % 2)
                    cols.append((i1 * 2 + b // 2) * 2 * n + i2 * 2 + b % 2)
                    data.append(np.full(len(i1), Wr[a, b]))
    dim = 4 * n * n
    U = sp.csr_matrix((np.concatenate(data), (np.concatenate(rows), np.concatenate(cols))), shape=(dim, dim))
    H0 = (sp.kron(h1, Id) + sp.kron(Id, h2) + U).tocsr()
    one = np.ones(2 * n)
    x1 = np.kron(np.kron(x, np.ones(2)), one)
    x2 = np.kron(one, np.kron(x, np.ones(2)))
    s31 = np.kron(np.kron(np.ones(n), [1.0, -1.0]), one)
    s32 = np.kron(one, np.kron(np.ones(n), [1.0, -1.0]))
    # gauge with real hopping: psi'(x1, x2) = (-i)^(x1 + x2) psi(x1, x2)
    ph = np.array([1, -1j, -1, 1j])[np.rint(x1 + x2).astype(int) % 4]
    G = sp.diags(ph)

    def gauged(A):
        B = (G @ A @ G.conj()).tocsr()
        Br, Bi = B.real.tocsr(), B.imag.tocsr()
        Br.eliminate_zeros()
        Bi.eliminate_zeros()
        return Br, Bi

    Hr, Hi = gauged(H0)
    K = []
    for V in (sp.kron(v1, Id), sp.kron(Id, v2)):
        Vr, Vi = gauged(V)
        assert Vr.nnz == 0                                  # V' = i K with K real, antisymmetric
        K.append(Vi)
    return dict(H0=H0, Hr=Hr, Hi=Hi, K=K, ph=ph, x1=x1, x2=x2,
                D=[p["M1"] * x1 * s31, p["M2"] * x2 * s32, x1 + x2], n=n, x=x)


def packet(p, L, rmax, Pg, coef, psis):
    """Phi(x1,s1,x2,s2) = sum_j coef_j (2 pi)^-1/2 e^{i P_j (eta x1 + (1-eta) x2)} psi_j(x1-x2)."""
    n = 2 * L + 1
    x = np.arange(-L, L + 1)
    ridx = x[:, None] - x[None, :] + 2 * L
    Phi = np.zeros((n, n, 4), dtype=complex)
    pad = np.zeros((4 * L + 1, 4), dtype=complex)
    lo = 2 * L - rmax
    for Pj, cj, psi in zip(Pg, coef, psis):
        if cj == 0:
            continue
        pad[:] = 0
        ps = psi.reshape(2 * rmax + 1, 4)
        if lo >= 0:
            pad[lo:lo + 2 * rmax + 1] = ps
        else:
            pad[:] = ps[-lo:-lo + 4 * L + 1]
        ph = np.exp(1j * Pj * ETA * x)[:, None] * np.exp(1j * Pj * (1 - ETA) * x)[None, :]
        Phi += cj * ph[:, :, None] * pad[ridx]
    Phi /= np.sqrt(2 * np.pi)
    return Phi.reshape(n, n, 2, 2).transpose(0, 2, 1, 3).reshape(-1)


def cheb_coef(z):
    """exp(-i z h) = sum_k c_k T_k(h) with c_k = (2 - delta_k0) (-i)^k J_k(z)."""
    kmax = int(z + 12 * z ** (1 / 3) + 30)
    k = np.arange(kmax + 1)
    c = jv(k, z) * np.array([1, -1j, -1, 1j])[k % 4]
    c[1:] *= 2
    keep = np.nonzero(np.abs(c) > 1e-16)[0].max() + 1
    return c[:keep]


def slope(lam, v, lo, hi):
    """Smooth-window average of dv/dlambda: -int W' v with W = 8/(3T) sin^4 on [lo, hi]."""
    T = hi - lo
    m = (lam >= lo - 1e-9) & (lam <= hi + 1e-9)
    th = np.pi * (lam[m] - lo) / T
    dW = 8 / (3 * T) * 4 * np.sin(th) ** 3 * np.cos(th) * np.pi / T
    return float(-np.sum(dW * v[m]) * (lam[1] - lam[0]))


# ---------------------------------------------------------------- one task
def run(task):
    name, p = task
    t0 = time.time()
    L, rmax, eps = p["L"], p["rmax"], p["eps"]
    epsf = eps * 0.5 * (p["M1"] + p["M2"])
    # packet weight g(P) = c cos^4(pi (P-P0) / (2 Pc)), class G(P_0)
    nP = 161
    Pg = np.linspace(p["P0"] - p["Pc"], p["P0"] + p["Pc"], nP)
    dP = Pg[1] - Pg[0]
    g = np.cos(np.pi * (Pg - p["P0"]) / (2 * p["Pc"])) ** 4
    g /= np.sqrt(np.sum(g * g) * dP)
    wg2 = g * g * dP
    gc = g * np.exp(-1j * Pg * p["xc"])                       # joint shift of the packet by xc labels
    lev = [level(P, p, rmax) for P in Pg]
    Eb = np.array([l["Eb"] for l in lev])
    E1 = np.array([l["E1"] for l in lev])
    E2 = np.array([l["E2"] for l in lev])

    def avg(f):
        return float(np.sum(wg2 * np.array(f)))

    Pm = avg(Pg)
    dPsp = np.sqrt(avg((Pg - Pm) ** 2))
    alpha_g = [avg([l["alpha"][i] for l in lev]) for i in range(3)]
    beta_g = [avg([l["beta"][i] for l in lev]) for i in range(3)]
    l0 = level(p["P0"], p, rmax)
    fd1 = np.gradient(Eb, dP)
    fd2 = np.gradient(fd1, dP)
    core = slice(8, nP - 8)
    info = dict(
        Eb_P0=l0["Eb"], dEb_P0=l0["E1"], d2Eb_P0=l0["E2"], s3_P0=l0["s3"], rmean_P0=l0["rmean"],
        gap_min=float(min(l["gap"] for l in lev)), dist_band_min=float(min(l["dist_band"] for l in lev)),
        inside_band=bool(any(l["inside"] for l in lev)), tail_max=float(max(l["tail"] for l in lev)),
        V1_minus_V2_max=float(max(abs(l["v1"] - l["v2"]) for l in lev)),
        fd_check_dE=float(np.max(np.abs(fd1 - E1)[core])), fd_check_d2E=float(np.max(np.abs(fd2 - E2)[core])),
        P_mean=Pm, delta_P=dPsp, alpha_g=alpha_g, beta_g=beta_g, alpha_P0=l0["alpha"], beta_P0=l0["beta"],
        mean_dE_packet=avg(E1))
    # sampling step: the rest of the first-order motion oscillates with the frequencies |E_n(P) - E_b(P)|;
    # a sum over samples at the step dlam aliases the multiples of 2 pi / dlam onto zero frequency
    freqs = np.concatenate([l["freqs"] for l in lev])

    def margin(dl):
        fs = 2 * np.pi / dl
        return float(np.min(np.abs(freqs - np.maximum(1, np.rint(freqs / fs)) * fs)))

    if isinstance(p["dlam"], tuple):
        cand = np.arange(p["dlam"][0], p["dlam"][1] + 1e-9, 0.25)
        dlam = float(cand[int(np.argmax([margin(c) for c in cand]))])
    else:
        dlam = float(p["dlam"])
    info["alias_margin"] = margin(dlam)
    # start on the chain
    ops = real_ops(p, L)
    psis = [l["psi"] for l in lev]
    Phi = packet(p, L, rmax, Pg, gc * dP, psis)
    res = ops["H0"] @ Phi - packet(p, L, rmax, Pg, gc * Eb * dP, psis)
    info["packet_norm"] = float(np.linalg.norm(Phi))
    info["packet_residual"] = float(np.linalg.norm(res))
    Phi /= np.linalg.norm(Phi)
    # runs: common gradient, g1 only, plain gradient; each with + and -
    sel = list(p["cfgs"])
    nc = 2 * len(sel)
    cfg = [(eps, eps, 0.0), (eps, 0.0, 0.0), (0.0, 0.0, epsf)]
    par = [eps, eps, epsf]
    pred = [alpha_g[0] + alpha_g[1], alpha_g[0], alpha_g[2]]
    pred_b = [beta_g[0] + beta_g[1], beta_g[0], beta_g[2]]
    pred0 = [l0["alpha"][0] + l0["alpha"][1], l0["alpha"][0], l0["alpha"][2]]
    Dg = np.zeros((Phi.size, nc))
    for c, ci in enumerate(sel):
        g1, g2, f = cfg[ci]
        d = g1 * ops["D"][0] + g2 * ops["D"][1] + f * ops["D"][2]
        Dg[:, 2 * c], Dg[:, 2 * c + 1] = d, -d
    wn = sum(np.linalg.norm(Wr, 2) for Wr in p["W"].values())
    scale = 1.03 * (np.hypot(p["M1"], p["t1"]) + np.hypot(p["M2"], p["t2"]) + wn + np.abs(Dg).max())
    # real arithmetic: Psi[0] real parts, Psi[1] imaginary parts of the runs
    H2 = ((2 / scale) * ops["Hr"]).tocsr()
    dim = H2.shape[0]
    D2 = (2 / scale) * Dg
    tmp = np.empty_like(D2)
    rows = np.unique(ops["Hi"].nonzero()[0])                  # complex entries of the binding only
    Hi2 = (2 / scale) * ops["Hi"][rows] if len(rows) else None

    def step2(F, Y):                                          # Y <- 2 h F - Y, h = C_bod / scale
        np.negative(Y, out=Y)
        for a in range(2):
            if csr_matvecs is None:
                Y[a] += H2 @ F[a]
            else:
                csr_matvecs(dim, dim, nc, H2.indptr, H2.indices, H2.data, F[a].ravel(), Y[a].ravel())
            np.multiply(D2, F[a], out=tmp)
            Y[a] += tmp
        if Hi2 is not None:
            Y[0][rows] -= Hi2 @ F[1]
            Y[1][rows] += Hi2 @ F[0]
        return Y

    coef = cheb_coef(scale * dlam)
    nst = int(round(p["lam_max"] / dlam))
    lam = dlam * np.arange(nst + 1)
    Phig = ops["ph"] * Phi
    Psi = np.stack([np.repeat(Phig.real[:, None], nc, axis=1), np.repeat(Phig.imag[:, None], nc, axis=1)])
    obs = np.zeros((nst + 1, 4, nc))

    def measure(k):
        w2 = Psi[0] ** 2 + Psi[1] ** 2
        for i in range(2):                                    # <V_i> = -2 Re^T K_i Im
            obs[k, i] = -2 * np.einsum("ij,ij->j", Psi[0], ops["K"][i] @ Psi[1])
        obs[k, 2] = ops["x1"] @ w2
        obs[k, 3] = ops["x2"] @ w2
        return w2

    measure(0)
    for k in range(1, nst + 1):
        f0 = Psi
        f1 = step2(Psi, np.zeros_like(Psi))
        f1 *= 0.5
        acc = coef[0].real * f0
        for j in range(1, len(coef)):
            if j > 1:
                f0, f1 = f1, step2(f1, f0)                    # T_j = 2 h T_{j-1} - T_{j-2}
            if j % 2 == 0:
                for a in range(2):
                    np.multiply(f1[a], coef[j].real, out=tmp)
                    acc[a] += tmp
            else:                                             # i c (re + i im) = c (-im + i re)
                np.multiply(f1[1], coef[j].imag, out=tmp)
                acc[0] -= tmp
                np.multiply(f1[0], coef[j].imag, out=tmp)
                acc[1] += tmp
        Psi = acc
        w2 = measure(k)
    info["norm_drift"] = float(np.max(np.abs(np.sum(w2, axis=0) - 1)))
    info["v0_start"] = [float(obs[0, 0, 0]), float(obs[0, 1, 0])]
    edge = (np.abs(ops["x1"]) > L - 3) | (np.abs(ops["x2"]) > L - 3)
    info["edge_weight_end"] = float(np.sum(w2[edge, 0]))
    T = lam[-1]
    out = dict(name=name, info=info, configs=[], lam=lam.tolist(), series={})
    for c, ci in enumerate(sel):
        lab = LABELS[ci]
        fo = (obs[:, :, 2 * c] - obs[:, :, 2 * c + 1]) / (2 * par[ci])    # first order per unit gradient
        v1, v2, sep = fo[:, 0], fo[:, 1], fo[:, 2] - fo[:, 3]
        s1, s2 = slope(lam, v1, 0, T), slope(lam, v2, 0, T)
        half = [slope(lam, v, T / 2, T) for v in (v1, v2)] + [slope(lam, v, 0, T / 2) for v in (v1, v2)]
        ssep = slope(lam, sep, 0, T)
        ssep_half = [slope(lam, sep, 0, T / 2), slope(lam, sep, T / 2, T)]
        out["configs"].append(dict(
            config=lab, predicted_slope=pred[ci], alpha_P0=pred0[ci], slope_v1=s1, slope_v2=s2,
            rel_dev_v1=s1 / pred[ci] - 1, rel_dev_v2=s2 / pred[ci] - 1,
            half_window_rel_dev=[h / pred[ci] - 1 for h in half],
            two_point_rel_dev=[float(v1[-1] / T / pred[ci] - 1), float(v2[-1] / T / pred[ci] - 1)],
            rest_sup=[float(np.max(np.abs(v1 - pred[ci] * lam))), float(np.max(np.abs(v2 - pred[ci] * lam)))],
            linear_part_end=float(abs(pred[ci]) * T),
            sep_predicted_slope=pred_b[ci], sep_slope=ssep, sep_slope_half_windows=ssep_half, sep_end=float(sep[-1]),
            sep_max_abs=float(np.max(np.abs(sep))), sep_minus_linear_sup=float(np.max(np.abs(sep - pred_b[ci] * lam)))))
        out["series"][lab] = dict(v1=v1.tolist(), v2=v2.tolist(), sep=sep.tolist())
    if p["R"] and len(sel) == 3:
        cf, u = closed_form(p)
        cfp = closed_form_packet(p, Pg, wg2)

        def comb(z):
            return [z[0] + z[1], z[0], z[2]]

        out["closed_form"] = dict(u=u, eps2=[(p["t1"] / p["M1"]) ** 2, (p["t2"] / p["M2"]) ** 2],
                                  closed_P0=comb(cf), closed_packet=comb(cfp), level_P0=pred0,
                                  slope_v1=[c["slope_v1"] for c in out["configs"]])
    out["numerics"] = dict(L=L, chain_sites=2 * L + 1, dim=int(Phi.size), rmax=rmax, nP=nP, Pc=p["Pc"], P0=p["P0"], xc=p["xc"],
                           lam_max=float(T), dlam=dlam, window_half_width=6 * np.pi / T, eps=eps, eps_plain=epsf, cheb_terms=int(len(coef)),
                           seconds=round(time.time() - t0, 1))
    return out


def scaling_table():
    """alpha(0) from the numerical level against (13.13) at tau -> s tau, w -> s^2 w."""
    rows = []
    for name in ("S1", "S2", "S3"):
        for s in (1.0, 0.5, 0.25):
            p = BASE[name]
            q = dict(p, t1=p["t1"] * s, t2=p["t2"] * s, W={0: p["W"][0] * s * s})
            l0 = level(0.0, q, 64)
            cf, u = closed_form(q)
            rows.append(dict(set=name, s=s, tau_over_M=[q["t1"] / q["M1"], q["t2"] / q["M2"]], u=u,
                             level=l0["alpha"], closed=cf,
                             rel_dev=[l0["alpha"][i] / cf[i] - 1 for i in range(3)]))
    return rows


def clock_ratio(p, rmax):
    """Numerical level at P = 0: Gamma_i = <sigma_3^(i)>_0 = dE_b(0)/dM_i and its derivative in the data,
    T[i][j] = M_j dGamma_i/dM_j = M_j d^2E_b(0)/dM_i dM_j = -2 M_j Re <sigma_3^(i) psi| R |sigma_3^(j) psi>."""
    nr = 2 * rmax + 1
    vals, vecs = np.linalg.eigh(fibre_ops(0.0, p, rmax)[0])
    b = int(np.argmax(np.abs(vecs[rmax * 4, :]) ** 2))        # weight on r = 0, branch |11>
    psi = vecs[:, b]
    dE = vals - vals[b]
    dE[b] = np.inf
    s3 = [np.kron(np.ones(nr), S3A), np.kron(np.ones(nr), S3B)]
    Mi = [p["M1"], p["M2"]]
    c = [vecs.conj().T @ (s * psi) for s in s3]
    G = [float(np.vdot(psi, s * psi).real) for s in s3]
    T = [[float(-2 * Mi[j] * np.sum(c[i].conj() * c[j] / dE).real) for j in range(2)] for i in range(2)]
    return G, T


def clock_ratio_closed(p):
    """Leading order in R: Gamma_i of (11.20) and M_j times the second derivatives (13.22)."""
    t, M, w = [p["t1"], p["t2"]], [p["M1"], p["M2"]], p["W"][0][0, 0].real
    a = [t[i] ** 2 / (4 * M[i]) for i in range(2)]
    asum = a[0] + a[1]
    u, sg = abs(w) / asum, np.sign(w)
    lam = 1 + sg / np.sqrt(1 + u * u)
    d2 = sg * u * u / (asum * (1 + u * u) ** 1.5)             # second derivative of a + sgn(w) sqrt(w^2 + a^2) in a
    G = [1 - a[i] / M[i] * lam for i in range(2)]
    T = [[(2 * a[i] / M[i] * lam if i == j else 0.0) + a[i] * a[j] / M[i] * d2 for j in range(2)] for i in range(2)]
    return G, T, u


def clock_ratio_table():
    """Derivative of the clock ratio in the data against (13.22), and rho_i - g_i against (13.18),
    at tau -> s tau, w -> s^2 w (numerical level at P = 0, fibre |r| <= 64)."""
    rows, h = [], 1e-4
    for name in ("S1", "S2", "S3"):
        for s in (1.0, 0.5, 0.25):
            p = BASE[name]
            q = dict(p, t1=p["t1"] * s, t2=p["t2"] * s, W={0: p["W"][0] * s * s})
            G, T = clock_ratio(q, 64)
            Gc, Tc, u = clock_ratio_closed(q)
            T48 = clock_ratio(q, 48)[1]
            fd = [[0.0, 0.0], [0.0, 0.0]]                     # symmetric difference of Gamma_i in M_j
            for j, key in enumerate(("M1", "M2")):
                Gp = clock_ratio(dict(q, **{key: q[key] * (1 + h)}), 64)[0]
                Gm = clock_ratio(dict(q, **{key: q[key] * (1 - h)}), 64)[0]
                for i in range(2):
                    fd[i][j] = (Gp[i] - Gm[i]) / (2 * h)
            ij = [(i, j) for i in range(2) for j in range(2)]
            # rho_i - g_i per unit gradient, (13.21) against (13.18): common gradient, g1 only, g2 only
            rho = [[(T[i][0] + T[i][1]) / G[i], T[i][0] / G[i], T[i][1] / G[i]] for i in range(2)]
            rhoc = [[Tc[i][0] + Tc[i][1], Tc[i][0], Tc[i][1]] for i in range(2)]
            rows.append(dict(
                set=name, s=s, tau_over_M=[q["t1"] / q["M1"], q["t2"] / q["M2"]], u=u,
                Gamma=G, Gamma_closed=Gc, one_minus_Gamma_rel_dev=[(1 - G[i]) / (1 - Gc[i]) - 1 for i in range(2)],
                T=T, T_closed=Tc, T_rel_dev=[[T[i][j] / Tc[i][j] - 1 for j in range(2)] for i in range(2)],
                T_abs_dev=[[T[i][j] - Tc[i][j] for j in range(2)] for i in range(2)],
                fd_rel_dev=float(max(abs(fd[i][j] / T[i][j] - 1) for i, j in ij)),
                rmax48_rel_change=float(max(abs(T48[i][j] / T[i][j] - 1) for i, j in ij)),
                rho_minus_g=rho, rho_minus_g_closed=rhoc,
                rho_rel_dev=[[rho[i][k] / rhoc[i][k] - 1 for k in range(3)] for i in range(2)]))
    return rows


def other_order_table():
    """Step 5.3 of the derivation (the limits of item 2(c) in the other order). From the numerical level at
    P = 0 and P = 0.2, per unit gradient (common gradient; g1 only):
      d<sigma_3^(i)>_P/dP = -2 Re <sigma_3^(i) psi| R |V_eta psi>,   dK = d<K>_P/dP = sum_i g_i M_i d<sigma_3^(i)>_P/dP,
      f_i = Re F_{i,Lambda}(P) for the windows [0, Lambda],  F_{i,lambda} = <V_i psi| R (1 - exp(-i (H - E_b) lambda)) |K psi>,
      identity (13.6): 2 Re <V_i psi| R |K psi> = -dK for i = 1, 2.
    Fibre |r| <= 96, against 64; d<sigma_3>/dP also by a symmetric difference in P (fibre |r| <= 64). For the sets
    in the regime R the leading order from (11.12), differentiated once in M_i and once in P, is given for
    comparison (a check of the table; no statement of the derivation rests on it)."""
    rows, hP, wins = [], 1e-4, (5.0, 10.0, 20.0)
    for name, p in BASE.items():
        Mi, ti = [p["M1"], p["M2"]], [p["t1"], p["t2"]]
        for P in (0.0, 0.2):
            res = {}
            for rmax in (64, 96):
                nr = 2 * rmax + 1
                H, V1, V2, _ = fibre_ops(P, p, rmax)
                vals, vecs = np.linalg.eigh(H)
                b = int(np.argmax(np.abs(vecs[rmax * 4, :]) ** 2))    # weight on r = 0, branch |11>
                psi = vecs[:, b]
                keep = np.arange(len(vals)) != b
                dE = (vals - vals[b])[keep]
                Uq = vecs[:, keep].conj().T                           # components in Q h
                cV = [Uq @ (V @ psi) for V in (V1, V2)]
                c3 = [Uq @ (np.kron(np.ones(nr), s) * psi) for s in (S3A, S3B)]
                cVe = ETA * cV[0] + (1 - ETA) * cV[1]
                ds3 = [float(-2 * np.sum(c3[i].conj() * cVe / dE).real) for i in range(2)]
                cK = [Mi[0] * c3[0] + Mi[1] * c3[1], Mi[0] * c3[0]]   # Q K psi per unit gradient: common, g1 only
                dK = [Mi[0] * ds3[0] + Mi[1] * ds3[1], Mi[0] * ds3[0]]
                id136 = [[float(2 * np.sum(cV[i].conj() * cK[c] / dE).real + dK[c]) for c in range(2)] for i in range(2)]
                f = [[[float(np.sum(cV[i].conj() * cK[c] * (1 - np.exp(-1j * dE * lam)) / dE).real) for lam in wins]
                      for c in range(2)] for i in range(2)]
                res[rmax] = dict(ds3=ds3, dK=dK, id136=id136, f=f)
            lv = level(P, p, 64)
            sp_, sm_ = level(P + hP, p, 64)["s3"], level(P - hP, p, 64)["s3"]
            fd = [(sp_[i] - sm_[i]) / (2 * hP) for i in range(2)]
            closed = None
            if p["R"]:
                w = p["W"][0][0, 0].real
                a = [ti[i] ** 2 / (4 * Mi[i]) for i in range(2)]
                j2 = a[0] ** 2 + a[1] ** 2 + 2 * a[0] * a[1] * np.cos(2 * P)
                closed = [float(np.sign(w) * a[i] / Mi[i] * 2 * a[1 - i] * np.sin(2 * P)
                                * (w * w + a[1 - i] ** 2 + a[0] * a[1] * np.cos(2 * P)) / (w * w + j2) ** 1.5) for i in range(2)]
            r64, r96 = res[64], res[96]
            idx = [(i, c, k) for i in range(2) for c in range(2) for k in range(len(wins))]
            rows.append(dict(
                set=name, P=P, dEb=float(lv["E1"]), gap=float(lv["gap"]), dist_band=float(lv["dist_band"]),
                inside_band=bool(lv["inside"]), ds3=r96["ds3"], ds3_closed=closed, dK=r96["dK"],
                id136_abs_dev=float(max(abs(v) for row in r96["id136"] for v in row)),
                ds3_fd_abs_dev=float(max(abs(fd[i] - r64["ds3"][i]) for i in range(2))),
                ds3_change_64_96=float(max(abs(r64["ds3"][i] - r96["ds3"][i]) for i in range(2))),
                windows=list(wins), f=r96["f"],
                f_change_64_96=float(max(abs(r64["f"][i][c][k] - r96["f"][i][c][k]) for i, c, k in idx))))
    return rows


def second_derivative_table():
    """Step 5.3 of the derivation, (13.29) and (13.30). With c_i(lambda; P) = Re <V_i psi| R exp(-i (H - E_b) lambda) |K psi>,
    the second derivative at lambda = 0 is -Re <V_i psi| (H - E_b) |K psi>. From the numerical level at P = 0.1 and
    P = 0.2 (fibre |r| <= 96, against 64), per unit gradient (the gradient of one part only, K = M_c sigma_3^(c)):
      spectral sum       -Re sum_n conj(<n|V_i psi>) <n|K psi> (E_n - E_b)   (the levels n of the fibre other than the bound level),
      double commutator  -1/2 <[V_i, [H, K]]>_P                              (13.29), every binding,
      (13.29)            -M_i tau_i^2 Im <sigma_3^(i) T_i^2>_P for the gradient of the same part and 0 for the gradient of the
                         other part (a binding that commutes with K: the sets S1-S4, not the control S5), with
                         T_1 = e^{i eta P} S^dagger, T_2 = e^{i (1 - eta) P} S,
      (13.30)            sgn(w) M_i tau_i^2 a_j sin(2P) / sqrt(w^2 + j(P)^2), j != i: the leading order in R (sets S1-S3)."""
    rows = []
    for name, p in BASE.items():
        Mi, ti = [p["M1"], p["M2"]], [p["t1"], p["t2"]]
        for P in (0.1, 0.2):
            res = {}
            for rmax in (64, 96):
                nr = 2 * rmax + 1
                H, V1, V2, _ = fibre_ops(P, p, rmax)
                vals, vecs = np.linalg.eigh(H)
                b = int(np.argmax(np.abs(vecs[rmax * 4, :]) ** 2))    # weight on r = 0, branch |11>
                psi = vecs[:, b]
                keep = np.arange(len(vals)) != b
                dE = (vals - vals[b])[keep]
                Uq = vecs[:, keep].conj().T                           # components in Q h
                S = np.eye(nr, k=-1).astype(complex)                  # (S psi)(r) = psi(r-1)
                T2 = [np.exp(2j * ETA * P) * np.kron(S.T @ S.T, np.eye(4)),
                      np.exp(2j * (1 - ETA) * P) * np.kron(S @ S, np.eye(4))]
                s3 = [np.kron(np.ones(nr), s) for s in (S3A, S3B)]
                Vs = (V1, V2)
                spec = [[0.0, 0.0], [0.0, 0.0]]                       # [part i][gradient of the part c]
                comm = [[0.0, 0.0], [0.0, 0.0]]
                for i in range(2):
                    vpsi = Vs[i] @ psi
                    cV = Uq @ vpsi
                    for c in range(2):
                        kd = Mi[c] * s3[c]                            # diagonal of K
                        spec[i][c] = float(-np.sum(cV.conj() * (Uq @ (kd * psi)) * dE).real)
                        HK = H * kd[None, :] - kd[:, None] * H        # [H, K]
                        comm[i][c] = float(-0.5 * np.vdot(psi, Vs[i] @ (HK @ psi) - HK @ vpsi).real)
                f29 = [float(-Mi[i] * ti[i] ** 2 * np.vdot(psi, s3[i] * (T2[i] @ psi)).imag) for i in range(2)]
                res[rmax] = dict(spec=spec, comm=comm, f29=f29)
            closed = None
            if p["R"]:
                w = p["W"][0][0, 0].real
                a = [ti[i] ** 2 / (4 * Mi[i]) for i in range(2)]
                j2 = a[0] ** 2 + a[1] ** 2 + 2 * a[0] * a[1] * np.cos(2 * P)
                closed = [float(np.sign(w) * Mi[i] * ti[i] ** 2 * a[1 - i] * np.sin(2 * P) / np.sqrt(w * w + j2)) for i in range(2)]
            r64, r96 = res[64], res[96]
            ic = [(i, c) for i in range(2) for c in range(2)]
            rows.append(dict(
                set=name, P=P, own=[r96["spec"][0][0], r96["spec"][1][1]], cross=[r96["spec"][0][1], r96["spec"][1][0]],
                commutator_abs_dev=float(max(abs(r96["spec"][i][c] - r96["comm"][i][c]) for i, c in ic)),
                f1329=r96["f29"], f1329_abs_dev=[r96["spec"][i][i] - r96["f29"][i] for i in range(2)],
                closed=closed,
                closed_rel_dev=None if closed is None else [r96["spec"][i][i] / closed[i] - 1 for i in range(2)],
                change_64_96=float(max(abs(r64["spec"][i][c] - r96["spec"][i][c]) for i, c in ic))))
    return rows


def fibre_range_table():
    """Coefficients (13.8), (13.10) at P0 for the fibre ranges |r| <= 32, 48 against 64."""
    rows = []
    for name, p in BASE.items():
        q = dict(DEFAULT, **p)
        ref = level(q["P0"], q, 64)
        for rmax in (32, 48):
            l = level(q["P0"], q, rmax)
            da = max(abs(l["alpha"][i] / ref["alpha"][i] - 1) for i in range(3))
            db = max(abs(l["beta"][i] - ref["beta"][i]) for i in range(3))
            rows.append(dict(set=name, rmax=rmax, tail=l["tail"], alpha_rel_change=da, beta_abs_change=db))
    return rows


def main():
    t0 = time.time()
    OUT.mkdir(exist_ok=True)
    oth = other_order_table()               # cheap; before the evolutions
    sdt = second_derivative_table()         # cheap; before the evolutions
    names = sys.argv[1:] or list(BASE) + list(VARIANTS)
    tasks = []
    for nm in names:
        if nm in BASE:
            tasks.append((nm, dict(DEFAULT, **BASE[nm])))
        else:
            b, ch = VARIANTS[nm]
            tasks.append((nm, dict(dict(DEFAULT, **BASE[b]), cfgs=(1,), **ch)))
    with Pool(min(len(tasks), max(1, (os.cpu_count() or 2) - 2))) as pool:
        results = pool.map(run, tasks, chunksize=1)
    res = {r["name"]: r for r in results}
    scal = scaling_table()
    frng = fibre_range_table()
    clk = clock_ratio_table()
    pad = " " * 22
    lines = []
    for nm, r in res.items():
        nu, inf = r["numerics"], r["info"]
        lines.append(f"== {nm}: chain |x_i|<={nu['L']} ({nu['chain_sites']} sites, dim {nu['dim']}), fibre |r|<={nu['rmax']}, "
                     f"packet cos^4 on |P-{nu['P0']}|<={nu['Pc']} (delta P={inf['delta_P']:.4f}), centre label {nu['xc']}, "
                     f"lambda<={nu['lam_max']:.0f} step {nu['dlam']} (alias margin {inf['alias_margin']:.3f}, window half width "
                     f"{nu['window_half_width']:.4f}), eps={nu['eps']:.1e}, {nu['seconds']} s")
        lines.append(f"   level: E_b={inf['Eb_P0']:.8f} E_b'={inf['dEb_P0']:+.3e} E_b''={inf['d2Eb_P0']:+.6e} "
                     f"<s3>={inf['s3_P0'][0]:.6f},{inf['s3_P0'][1]:.6f} gap>={inf['gap_min']:.3e} "
                     f"dist to bands>={inf['dist_band_min']:.3e} inside band: {inf['inside_band']}")
        lines.append(f"   checks: |<V1>-<V2>|<={inf['V1_minus_V2_max']:.1e}, FD(E_b') {inf['fd_check_dE']:.1e}, "
                     f"FD(E_b'') {inf['fd_check_d2E']:.1e}, fibre tail {inf['tail_max']:.1e}, packet norm {inf['packet_norm']:.10f}, "
                     f"residual {inf['packet_residual']:.1e}, norm drift {inf['norm_drift']:.1e}, edge weight {inf['edge_weight_end']:.1e}")
        for c in r["configs"]:
            lines.append(f"   {c['config']:<22} slope v1 {c['slope_v1']:+.8e} v2 {c['slope_v2']:+.8e} | (13.7) {c['predicted_slope']:+.8e} | "
                         f"rel dev {c['rel_dev_v1']:+.1e} {c['rel_dev_v2']:+.1e} | half windows {max(abs(h) for h in c['half_window_rel_dev']):.1e} | "
                         f"two-point {c['two_point_rel_dev'][0]:+.1e} {c['two_point_rel_dev'][1]:+.1e} | "
                         f"rest sup {c['rest_sup'][0]:.2e} {c['rest_sup'][1]:.2e} (linear part at end {c['linear_part_end']:.2e})")
            lines.append(f"   {pad} separation: slope {c['sep_slope']:+.4e} (half windows {c['sep_slope_half_windows'][0]:+.4e} "
                         f"{c['sep_slope_half_windows'][1]:+.4e}) | (13.10) <beta>_g {c['sep_predicted_slope']:+.4e} | "
                         f"max |sep| {c['sep_max_abs']:.3e} | sup |sep - lambda<beta>| {c['sep_minus_linear_sup']:.3e}")
        if "closed_form" in r:
            cf = r["closed_form"]
            for i, lab in enumerate(("common", "g1 only", "plain")):
                lines.append(f"   closed form {lab:<8} (13.13) {cf['closed_P0'][i]:+.6e} | level at P0 {cf['level_P0'][i]:+.6e} "
                             f"(rel {cf['level_P0'][i] / cf['closed_P0'][i] - 1:+.2e}) | (11.12) packet average {cf['closed_packet'][i]:+.6e} "
                             f"vs evolution {cf['slope_v1'][i]:+.6e} (rel {cf['slope_v1'][i] / cf['closed_packet'][i] - 1:+.2e}); "
                             f"u={cf['u']:.3f}, (tau/M)^2={cf['eps2'][0]:.3f},{cf['eps2'][1]:.3f}")
    conv = []
    lines.append("== convergence (configuration g1 only): relative change of the slopes against the base run")
    for nm in res:
        if nm in VARIANTS and VARIANTS[nm][0] in res:
            b, ch = VARIANTS[nm]
            cb = [c for c in res[b]["configs"] if c["config"] == LABELS[1]][0]
            cv = res[nm]["configs"][0]
            row = dict(variant=nm, base=b, changed=ch, rel_dev_variant=[cv["rel_dev_v1"], cv["rel_dev_v2"]],
                       rel_dev_base=[cb["rel_dev_v1"], cb["rel_dev_v2"]],
                       slope_change=[cv["slope_v1"] / cb["slope_v1"] - 1, cv["slope_v2"] / cb["slope_v2"] - 1],
                       sep_slope=[cv["sep_slope"], cb["sep_slope"]])
            conv.append(row)
            lines.append(f"   {nm:<10} {str(ch):<22} slope change v1 {row['slope_change'][0]:+.1e} v2 {row['slope_change'][1]:+.1e} | "
                         f"rel dev from (13.7): variant {cv['rel_dev_v1']:+.1e} {cv['rel_dev_v2']:+.1e}, base {cb['rel_dev_v1']:+.1e} {cb['rel_dev_v2']:+.1e} | "
                         f"separation slope: variant {cv['sep_slope']:+.4e}, base {cb['sep_slope']:+.4e}")
    lines.append("== fibre range: change of the coefficients (13.8), (13.10) at P0 against |r|<=64")
    for row in frng:
        lines.append(f"   {row['set']} |r|<={row['rmax']}: tail of psi {row['tail']:.1e}, alpha rel change {row['alpha_rel_change']:.1e}, "
                     f"beta abs change {row['beta_abs_change']:.1e}")
    lines.append("== scaling of the deviation from (13.13): tau -> s tau, w -> s^2 w (numerical level at P0=0, fibre |r|<=64)")
    for row in scal:
        lines.append(f"   {row['set']} s={row['s']:<5} tau/M={row['tau_over_M'][0]:.3f},{row['tau_over_M'][1]:.3f} u={row['u']:.3f} "
                     f"rel dev of coefficients (g1, g2, plain): {row['rel_dev'][0]:+.3e} {row['rel_dev'][1]:+.3e} {row['rel_dev'][2]:+.3e}")
    lines.append("== clock ratio Gamma_i = dE_b(0)/dM_i and its derivative in the data, T_ij = M_j dGamma_i/dM_j, against (11.20), "
                 "(13.22): tau -> s tau, w -> s^2 w (numerical level at P0=0, fibre |r|<=64)")
    for row in clk:
        td, ta, rd = row["T_rel_dev"], row["T_abs_dev"], row["rho_rel_dev"]
        lines.append(f"   {row['set']} s={row['s']:<5} tau/M={row['tau_over_M'][0]:.3f},{row['tau_over_M'][1]:.3f} u={row['u']:.3f} "
                     f"1-Gamma_i rel dev {row['one_minus_Gamma_rel_dev'][0]:+.3e} {row['one_minus_Gamma_rel_dev'][1]:+.3e} | "
                     f"T_11 {row['T'][0][0]:+.6e} T_12 {row['T'][0][1]:+.6e} T_21 {row['T'][1][0]:+.6e} T_22 {row['T'][1][1]:+.6e} | "
                     f"rel dev from (13.22) {td[0][0]:+.3e} {td[0][1]:+.3e} {td[1][0]:+.3e} {td[1][1]:+.3e} | "
                     f"abs dev {ta[0][0]:+.2e} {ta[0][1]:+.2e} {ta[1][0]:+.2e} {ta[1][1]:+.2e}")
        lines.append(f"   {pad} rho_i - g_i, (13.21) against (13.18), rel dev (common, g1 only, g2 only): part 1 {rd[0][0]:+.3e} {rd[0][1]:+.3e} "
                     f"{rd[0][2]:+.3e} | part 2 {rd[1][0]:+.3e} {rd[1][1]:+.3e} {rd[1][2]:+.3e} | symmetric difference in M_j against "
                     f"the resolvent {row['fd_rel_dev']:.1e} | fibre |r|<=48 against 64 {row['rmax48_rel_change']:.1e}")
    lines.append("== other order of the limits (Step 5.3): d<sigma_3^(i)>_P/dP, d<K>_P/dP and f_i = Re F_{i,Lambda}(P) for the windows "
                 "[0, Lambda], per unit gradient (numerical level, fibre |r|<=96; changes against |r|<=64)")
    for row in oth:
        cl = "" if row["ds3_closed"] is None else (f" | leading order from (11.12) {row['ds3_closed'][0]:+.6e} "
                                                   f"{row['ds3_closed'][1]:+.6e}")
        lines.append(f"   {row['set']} P={row['P']:<4} E_b'={row['dEb']:+.6e} gap {row['gap']:.3e} dist to bands {row['dist_band']:.3e} "
                     f"inside band: {row['inside_band']} | d<s3>/dP {row['ds3'][0]:+.6e} {row['ds3'][1]:+.6e}{cl} | "
                     f"d<K>/dP common {row['dK'][0]:+.6e} g1 only {row['dK'][1]:+.6e} | (13.6) abs dev {row['id136_abs_dev']:.1e} | "
                     f"symmetric difference in P abs dev {row['ds3_fd_abs_dev']:.1e} | |r|<=64 against 96: d<s3>/dP "
                     f"{row['ds3_change_64_96']:.1e}, f {row['f_change_64_96']:.1e}")
        for c, lab in enumerate(("common", "g1 only")):
            lines.append(f"   {pad} f_i {lab:<8} " + " | ".join(
                f"Lambda={lam:g}: f_1 {row['f'][0][c][k]:+.6e} f_2 {row['f'][1][c][k]:+.6e}" for k, lam in enumerate(row["windows"])))
    lines.append("== second derivative at lambda = 0 of c_i(lambda; P) = Re <V_i psi| R exp(-i (H - E_b) lambda) |K psi> (Step 5.3, "
                 "(13.29), (13.30)), per unit gradient (numerical level, fibre |r|<=96; changes against |r|<=64)")
    for row in sdt:
        cl = "" if row["closed"] is None else (f" | (13.30) {row['closed'][0]:+.6e} {row['closed'][1]:+.6e} "
                                               f"(rel dev {row['closed_rel_dev'][0]:+.3e} {row['closed_rel_dev'][1]:+.3e})")
        lines.append(f"   {row['set']} P={row['P']:<4} part 1 with g1 only {row['own'][0]:+.6e}, part 2 with g2 only {row['own'][1]:+.6e} | "
                     f"part 1 with g2 only {row['cross'][0]:+.2e}, part 2 with g1 only {row['cross'][1]:+.2e} | "
                     f"double commutator abs dev {row['commutator_abs_dev']:.1e} | (13.29) for a binding that commutes with K "
                     f"{row['f1329'][0]:+.6e} {row['f1329'][1]:+.6e} (abs dev {row['f1329_abs_dev'][0]:+.1e} "
                     f"{row['f1329_abs_dev'][1]:+.1e}){cl} | |r|<=64 against 96: {row['change_64_96']:.1e}")
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        show = [nm for nm in ("S1", "S2", "S3", "S4", "S5") if nm in res]
        fig, ax = plt.subplots(2, len(show), figsize=(4.2 * len(show), 6.4), squeeze=False)
        for j, nm in enumerate(show):
            lam = np.array(res[nm]["lam"])
            for c, col in zip(res[nm]["configs"], ("C0", "C1", "C2")):
                s = res[nm]["series"][c["config"]]
                ax[0, j].plot(lam, s["v1"], col, lw=1.2, label=c["config"])
                ax[0, j].plot(lam, s["v2"], col, lw=0.8, ls=":")
                ax[0, j].plot(lam, c["predicted_slope"] * lam, "k--", lw=0.6)
                ax[1, j].plot(lam, s["sep"], col, lw=1.0)
                ax[1, j].plot(lam, c["sep_predicted_slope"] * lam, "k--", lw=0.6)
            ax[0, j].set_title(f"{nm}: first-order velocities (solid 1, dotted 2)", fontsize=9)
            ax[1, j].set_title("first-order separation; dashed: linear parts of (13.7), (13.10)", fontsize=9)
            ax[1, j].set_xlabel("lambda")
        ax[0, 0].legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(OUT / "first_order_motion.png", dpi=110)
    except Exception as exc:                                   # the figure is not needed for the check
        lines.append(f"figure skipped: {exc}")
    lines.append(f"total run time {time.time() - t0:.1f} s")
    (OUT / "summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    slim = {nm: {k: v for k, v in r.items() if k not in ("series", "lam")} for nm, r in res.items()}
    (OUT / "results.json").write_text(json.dumps(dict(sets=slim, convergence=conv, fibre_range=frng, scaling=scal, clock_ratio=clk,
                                                      other_order=oth, second_derivative=sdt), indent=1, default=float),
                                           encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
