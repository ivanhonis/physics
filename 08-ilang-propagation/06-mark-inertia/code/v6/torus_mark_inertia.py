"""Computation script of 08-ilang-propagation/06-mark-inertia, derivation v4.

Changes in v4 (verification.r2.md):
- S_i''(0) by analytic differentiation of the summands in P (no finite-difference step);
  Part E checks it against exact diagonalisation, Part G against Richardson finite
  differences with steps h0, h0/2, h0/4 at the points of smallest isolation gap (I4).
- Crossings rho_i,- = 1 by Brent root-finding on the lattice sums, with an error estimate
  (root tolerance; for the two-quantum part the binning, from a lattice with dE/2); the
  windows are built from the roots and checked against every computed point (I1).
- y_ab from direct evaluation at the stated levels instead of interpolation (I1).
- Part G also compares L = 64 and L = 128 at ell = 8 at the smallest-gap points (I3).

Cubic torus (D = 3) of side L, body chain along lattice axis 1, Q = q_1; in
Part F also the ring (D = 1).  The lattice sums of (6.3) are evaluated for the
one-quantum (F1^2) and the two-quantum (F2^2) part separately:
    S_i(P) = << cos^2(th)/(E + a) + sin^2(th)/(E + b) >>_i ,
    a = sigma [omega(P-Q) - omega(P)],  b = -sigma [omega(P-Q) + omega(P)],
with <<f>>_1 = sum_q c_q^2 f(Omega_q, q_1) and
     <<f>>_2 = 2 sum_{q,q'} c_q^2 c_q'^2 f(Omega_q + Omega_q', q_1 + q_1'),
so that E^(2) = -M_k^2 (F1^2 S_1 + F2^2 S_2).  Derived quantities:
    rho_i = -(eps^2/tau^2) S_i''(0)/S_i(0)        (6.6), per part
    t     = rho_1 S_1(0)/G0                        (bracket of (6.12)-(6.13))
    xi*   = S_1(0)(1-rho_1)/(S_2(0)(rho_2-1))      (F2^2/(c0 F1^2) at which rho = 1)
Isolation (6.4), L = infinity: (k, sigma) is isolated iff b_k > sigma*eps_k with
b_k = min_q [Omega_q - omega_k(q_1)]; the minimum lies at q_2 = q_3 = 0, so b_k
is the same function on the ring and the torus.  Thresholds: the lower branch is
isolated iff eps_k > eps_-(r), the upper branch iff eps_k < eps_+(r) < m_h/2.
Only isolated states are evaluated, except in Part E (formula check, both
branches; the upper branch there is a formal coefficient).
One-quantum sums are exact mode sums over classes.  Two-quantum sums (v3): for
each q_1 the one-quantum energies are put on a grid of step dE with linear
(cloud-in-cell) weights, which keep the zeroth and first moments; the pair
measure per total q_1 is the convolution (cyclic in q_1, linear in E), done by
FFT, and the excess variance of the binning is removed to second order
(term -V f''/2).  Checked against brute-force pair sums (Part A).
Units: c0 = sqrt(kappa_h) = 1, F0 = 1, so eps_k = M_k.
"""
from itertools import combinations_with_replacement
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
LOG = []


def log(s=""):
    print(s, flush=True)
    LOG.append(s)


def omega(p, tau, eps):
    return np.sqrt(eps**2 + (tau * np.sin(p))**2)


def theta(p, tau, eps):
    return np.arctan(tau * np.sin(p) / eps)


# ------------------------------------------------------------------ isolation (6.4), L = infinity
_QQ = np.linspace(0.0, np.pi, 400001)


def b_min(tau, eps, mh):
    """b_k = min_q [Omega_q - omega_k(q_1)] (c0 = 1), attained at q_2 = q_3 = 0."""
    return np.min(np.sqrt(mh**2 + 2 * (1 - np.cos(_QQ))) - omega(_QQ, tau, eps))


def thresholds(tau, mh):
    """(eps_-, eps_+): lower branch isolated iff eps > eps_-, upper iff eps < eps_+."""
    gm = lambda e: b_min(tau, e, mh) + e          # increasing in eps
    gp = lambda e: b_min(tau, e, mh) - e          # decreasing in eps
    e0 = 1e-10
    if gm(e0) > 0:
        em = 0.0
    else:
        lo, hi = e0, 50.0
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            lo, hi = (lo, mid) if gm(mid) > 0 else (mid, hi)
        em = hi
    if gp(e0) <= 0:
        ep = 0.0
    else:
        lo, hi = e0, mh
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            lo, hi = (mid, hi) if gp(mid) > 0 else (lo, mid)
        ep = lo
    return em, ep


def lower_gap(tau, eps, mh):
    return b_min(tau, eps, mh) + eps


def upper_gap(tau, eps, mh):
    return b_min(tau, eps, mh) - eps


# ------------------------------------------------------------------ lattice sums
def _terms(P, sigma, tau, eps, Q):
    wP, tP = omega(P, tau, eps), theta(P, tau, eps)
    p = P - Q
    th = 0.5 * (tP + theta(p, tau, eps))
    wp = omega(p, tau, eps)
    return np.cos(th)**2, sigma * (wp - wP), np.sin(th)**2, -sigma * (wp + wP)


def _terms_d(P, sigma, tau, eps, Q):
    """As _terms, with first and second P-derivatives: (A, A', A''), (a, a', a''), (b, b', b''), B.
    A = cos^2(thb), B = sin^2(thb) = 1 - A, thb = (theta(P) + theta(P - Q))/2."""
    def wd(p):
        s, c = np.sin(p), np.cos(p)
        w = np.sqrt(eps**2 + (tau * s)**2)
        w1 = tau**2 * s * c / w
        w2 = tau**2 * np.cos(2 * p) / w - (tau**2 * s * c)**2 / w**3
        t1 = eps * tau * c / w**2
        t2 = -eps * tau * s / w**2 - 2 * eps * tau * c * w1 / w**3
        return w, w1, w2, np.arctan(tau * s / eps), t1, t2
    W0, W1, W2, T0, T1, T2 = wd(P)
    w, w1, w2, th, t1, t2 = wd(P - Q)
    tb, tb1, tb2 = 0.5 * (T0 + th), 0.5 * (T1 + t1), 0.5 * (T2 + t2)
    A = (np.cos(tb)**2, -np.sin(2 * tb) * tb1, -2 * np.cos(2 * tb) * tb1**2 - np.sin(2 * tb) * tb2)
    a = (sigma * (w - W0), sigma * (w1 - W1), sigma * (w2 - W2))
    b = (-sigma * (w + W0), -sigma * (w1 + W1), -sigma * (w2 + W2))
    return A, a, b, np.sin(tb)**2


def _frac(c, x, E, n):
    """Value and second P-derivative of c/(E + x)^n, n in {1, 3}; c, x = (f, f', f'')."""
    d = E + x[0]
    if n == 1:
        return c[0] / d, c[2] / d - 2 * c[1] * x[1] / d**2 + 2 * c[0] * x[1]**2 / d**3 - c[0] * x[2] / d**2
    return (c[0] / d**3,
            c[2] / d**3 - 6 * c[1] * x[1] / d**4 + 12 * c[0] * x[1]**2 / d**5 - 3 * c[0] * x[2] / d**4)


def _sum_d(E, w, A, a, b, B0, wV=None):
    """(S, S'') of sum w [A/(E+a) + B/(E+b)] - sum wV [A/(E+a)^3 + B/(E+b)^3] (binning variance term)."""
    B = (B0, -A[1], -A[2])
    fa, fa2 = _frac(A, a, E, 1)
    fb, fb2 = _frac(B, b, E, 1)
    s0, s2 = np.sum(w * (fa + fb)), np.sum(w * (fa2 + fb2))
    if wV is not None:
        ga, ga2 = _frac(A, a, E, 3)
        gb, gb2 = _frac(B, b, E, 3)
        s0 -= np.sum(wV * (ga + gb))
        s2 -= np.sum(wV * (ga2 + gb2))
    return s0, s2


class Torus:
    def __init__(self, L, ell, pairs=True, dE=1e-3):
        self.L, self.ell, self.mh = L, ell, 1.0 / ell
        k = 2 * np.pi * np.arange(L) / L
        s1 = 2 * (1 - np.cos(k))
        u, n = np.unique(np.round((s1[:, None] + s1[None, :]).ravel(), 12), return_counts=True)
        self.k = k
        self.Om = np.sqrt(self.mh**2 + s1[:, None] + u[None, :])      # (L, U) mode classes
        self.w = n[None, :] / (2 * L**3 * self.Om)                      # multiplicity * c_q^2
        self.G0 = 2 * np.sum(self.w / self.Om)
        self.w0 = np.sum(self.w)
        self.Omax = np.sqrt(self.mh**2 + 12)
        self.R1 = np.sum(self.w * (np.sin(k)**2)[:, None] / self.Om**2) / np.sum(self.w / self.Om)
        self.pairs = pairs
        if pairs:
            self._pairs(dE)

    def _pairs(self, dE):
        L = self.L
        x = self.Om / dE
        g = np.floor(x).astype(np.int64)
        t = x - g
        nb = int(g.max()) + 2
        h, hv = np.zeros((L, nb)), np.zeros((L, nb))
        for i in range(L):
            wi, ti, gi = self.w[i], t[i], g[i]
            h[i] = np.bincount(gi, wi * (1 - ti), nb) + np.bincount(gi + 1, wi * ti, nb)
            vi = wi * ti * (1 - ti) * dE**2
            hv[i] = np.bincount(gi, vi * (1 - ti), nb) + np.bincount(gi + 1, vi * ti, nb)
        n2 = 2 * nb
        Hf = np.fft.rfft2(h, s=(L, n2))
        W = 2 * np.fft.irfft2(Hf * Hf, s=(L, n2))
        V = 4 * np.fft.irfft2(Hf * np.fft.rfft2(hv, s=(L, n2)), s=(L, n2))
        omin, omax = self.Om.min(axis=1), self.Om.max(axis=1)
        E = dE * np.arange(n2)
        ii = np.arange(L)
        mask = np.zeros((L, n2), dtype=bool)
        for m in range(L):
            j = (m - ii) % L
            lo, hi = np.min(omin + omin[j]), np.max(omax + omax[j])
            mask[m] = (E >= lo - 3 * dE) & (E <= hi + 3 * dE)
        mi, gi = np.nonzero(mask)
        self.pm, self.pE, self.pW, self.pV = mi, E[gi], W[mi, gi], V[mi, gi]
        self.dE = dE
        sq = np.sin(self.k[self.pm])**2
        self.J2 = 0.5 * np.sum(self.pW / self.pE - self.pV / self.pE**3)
        self.R2 = np.sum(self.pW * sq / self.pE**2 - 3 * self.pV * sq / self.pE**4) / (2 * self.J2)

    def S1(self, P, sigma, tau, eps):
        A, a, B, b = _terms(P, sigma, tau, eps, self.k)
        E = self.Om
        return np.sum(self.w * (A[:, None] / (E + a[:, None]) + B[:, None] / (E + b[:, None])))

    def S2(self, P, sigma, tau, eps):
        A, a, B, b = _terms(P, sigma, tau, eps, self.k)
        m, E = self.pm, self.pE
        x, y = E + a[m], E + b[m]
        f = A[m] / x + B[m] / y
        f2 = 2 * A[m] / x**3 + 2 * B[m] / y**3
        return np.sum(self.pW * f - 0.5 * self.pV * f2)

    def S1d(self, sigma, tau, eps):
        """(S_1(0), S_1''(0)), analytic in P."""
        A, a, b, B0 = _terms_d(0.0, sigma, tau, eps, self.k)
        col = lambda t: tuple(z[:, None] for z in t)
        return _sum_d(self.Om, self.w, col(A), col(a), col(b), B0[:, None])

    def S2d(self, sigma, tau, eps):
        """(S_2(0), S_2''(0)), analytic in P, on the binned pair measure."""
        A, a, b, B0 = _terms_d(0.0, sigma, tau, eps, self.k)
        m = self.pm
        sel = lambda t: tuple(z[m] for z in t)
        return _sum_d(self.pE, self.pW, sel(A), sel(a), sel(b), B0[m], self.pV)


class Ring:
    def __init__(self, L, ell):
        self.L, self.ell, self.mh = L, ell, 1.0 / ell
        self.k = 2 * np.pi * np.arange(L) / L
        self.Om = np.sqrt(self.mh**2 + 2 * (1 - np.cos(self.k)))
        self.c2 = 1 / (2 * L * self.Om)
        self.G0 = 2 * np.sum(self.c2 / self.Om)

    @staticmethod
    def _S(P, sigma, tau, eps, E, Q, w):
        A, a, B, b = _terms(P, sigma, tau, eps, Q)
        return np.sum(w * (A / (E + a) + B / (E + b)))

    def S1(self, P, sigma, tau, eps):
        return self._S(P, sigma, tau, eps, self.Om, self.k, self.c2)

    def S2(self, P, sigma, tau, eps, chunk=256):
        s, Om, k, c2 = 0.0, self.Om, self.k, self.c2
        for i in range(0, self.L, chunk):
            sl = slice(i, i + chunk)
            s += self._S(P, sigma, tau, eps, Om[sl, None] + Om[None, :], k[sl, None] + k[None, :],
                         2 * c2[sl, None] * c2[None, :])
        return s

    def S1d(self, sigma, tau, eps):
        A, a, b, B0 = _terms_d(0.0, sigma, tau, eps, self.k)
        return _sum_d(self.Om, self.c2, A, a, b, B0)

    def S2d(self, sigma, tau, eps, chunk=256):
        s0 = s2 = 0.0
        Om, k, c2 = self.Om, self.k, self.c2
        for i in range(0, self.L, chunk):
            sl = slice(i, i + chunk)
            A, a, b, B0 = _terms_d(0.0, sigma, tau, eps, k[sl, None] + k[None, :])
            x0, x2 = _sum_d(Om[sl, None] + Om[None, :], 2 * c2[sl, None] * c2[None, :], A, a, b, B0)
            s0, s2 = s0 + x0, s2 + x2
        return s0, s2


def curv(f, h, f0=None):
    """Richardson-extrapolated second derivative at 0 of an even function (used only as a check)."""
    f0 = f(0.0) if f0 is None else f0
    c = lambda hh: 2 * (f(hh) - f0) / hh**2
    return f0, (4 * c(h) - c(2 * h)) / 3


def analyse(T, sigma, tau, eps, parts=(1, 2)):
    """{i: (S_i(0), rho_i)}; S_i''(0) by analytic differentiation of the summands (v4)."""
    out = {}
    for i in parts:
        s0, spp = T.S1d(sigma, tau, eps) if i == 1 else T.S2d(sigma, tau, eps)
        out[i] = (s0, -(eps**2 / tau**2) * spp / s0)
    return out


def roots(T, r, part, e, y, Th=None):
    """Roots of rho_{part,-}(eps) = 1 by Brent's method in each grid interval where y = rho - 1
    changes sign.  Returns (root, error estimate): residual-based for part 1 (exact mode sum);
    for part 2 the binning error, |rho_2 - 1| at the root on the lattice Th with dE/2, over the slope."""
    out = []
    g = lambda x, TT=T: analyse(TT, -1, r, x, (part,))[part][1] - 1
    for i in np.nonzero(np.sign(y[:-1]) * np.sign(y[1:]) < 0)[0]:
        x = brentq(g, e[i], e[i + 1], xtol=1e-10, rtol=1e-12)
        d = 1e-4 * x
        slope = (g(x + d) - g(x - d)) / (2 * d)
        res = abs(g(x))
        if part == 2 and Th is not None:
            res = max(res, abs(g(x, Th)))
        out.append((x, res / abs(slope) + 1e-10))
    return out


MARGIN = 0.2      # lower branch evaluated where b_k + eps_k > MARGIN * m_h


# ------------------------------------------------------------------ part A: pair-sum check
def part_a():
    L, ell = 12, 3.0
    log(f"PART A: lattice sums by mode classes and FFT pair convolution vs brute-force mode and ordered-pair"
        f" sums, torus L={L}, ell={ell}")
    g = np.array(np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")).reshape(3, -1)
    q = 2 * np.pi * g / L
    Om = np.sqrt(1 / ell**2 + 2 * np.sum(1 - np.cos(q), axis=0))
    c2 = 1 / (2 * L**3 * Om)
    E = Om[:, None] + Om[None, :]
    Q = q[0][:, None] + q[0][None, :]
    ww = 2 * c2[:, None] * c2[None, :]
    cases = ((-1, 1.0, 1.0), (-1, 1.5, 3.0), (-1, 0.5, 0.2), (+1, 0.5, 0.05))
    for dE in (1e-2, 1e-3):
        T = Torus(L, ell, dE=dE)
        w1 = w2 = 0.0
        for sigma, tau, eps in cases:
            for P in (0.0, 0.02):
                A, a, B, b = _terms(P, sigma, tau, eps, Q)
                b2 = np.sum(ww * (A / (E + a) + B / (E + b)))
                A1, a1, B1, b1_ = _terms(P, sigma, tau, eps, q[0])
                b1 = np.sum(c2 * (A1 / (Om + a1) + B1 / (Om + b1_)))
                w1 = max(w1, abs(T.S1(P, sigma, tau, eps) / b1 - 1))
                w2 = max(w2, abs(T.S2(P, sigma, tau, eps) / b2 - 1))
        log(f"  dE={dE}: max relative deviation S_1 {w1:.2e}, S_2 {w2:.2e}"
            f" (cases (sigma,r,eps) = {cases}, P = 0, 0.02)")
    bR1 = np.sum(c2 * np.sin(q[0])**2 / Om**2) / np.sum(c2 / Om)
    log(f"  R_1: classes {T.R1:.12f}, brute force {bR1:.12f};  J2: FFT {T.J2:.12f},"
        f" brute force {np.sum(c2[:, None]*c2[None, :]/E):.12f}")


# ------------------------------------------------------------------ part B: convergence in L and ell
def part_b(T8):
    log("")
    log("PART B: convergence in ell and L (c0 = 1); rho_1, rho_2 of the F1^2 and F2^2 parts, lower branch")
    lattices = [(32, 4.0), (48, 6.0), (64, 8.0), (128, 16.0), (256, 32.0)]
    cases = [(1.0, 1.0), (1.0, 4.0), (0.5, 2.0), (2.0, 2.0), (3.0, 4.0)]
    log(f"{'L':>4s} {'ell':>5s} {'G0':>9s} {'w0':>8s} {'J2':>9s} {'R1':>8s} {'R2':>8s} |"
        + "".join(f"  r={r} e={e}: rho_1, rho_2 " for r, e in cases))
    Ts = {}
    for L, ell in lattices:
        T = T8 if (L, ell) == (64, 8.0) else Torus(L, ell)
        Ts[(L, ell)] = T
        row = f"{L:4d} {ell:5.1f} {T.G0:9.6f} {T.w0:8.5f} {T.J2:9.6f} {T.R1:8.5f} {T.R2:8.5f} |"
        for r, eps in cases:
            res = analyse(T, -1, r, eps)
            row += f"  {res[1][1]:9.5f} {res[2][1]:9.5f}     "
        log(row)
    return Ts


# ------------------------------------------------------------------ part C: main table
def part_c(T):
    log("")
    log(f"PART C: main table, lower branch (isolated), torus L={T.L}, ell={T.ell} (m_h={T.mh}), c0=1, F0=1,"
        f" eps_k=M_k")
    log(f"  G0={T.G0:.6f}, w0={T.w0:.6f}, J2={T.J2:.6f}, R1={T.R1:.6f}, R2={T.R2:.6f}, "
        f"Omega_max={T.Omax:.4f}")
    log("  C_i = S_i(0)/S_i(0)|_{tau=0} (moving mark over held mark), rho_i of the parts, "
        "t = T/G0, xi* = F2^2/(c0 F1^2) at which rho = 1 (- if none finite >= 0)")
    log(f"{'r':>5s} {'eps':>5s} {'gap':>7s} | {'C_1':>8s} {'C_2':>8s} | "
        f"{'rho_1':>9s} {'rho_2':>9s} | {'t':>9s} {'xi*':>9s}")
    grid = []
    for r in (0.25, 0.5, 1.0, 1.5, 2.0):
        for eps in (0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 16.0, 32.0):
            gap = lower_gap(r, eps, T.mh)
            if gap <= MARGIN * T.mh:
                continue
            grid.append((r, eps))
            res = analyse(T, -1, r, eps)
            (s1, rho1), (s2, rho2) = res[1], res[2]
            xi = s1 * (1 - rho1) / (s2 * (rho2 - 1))
            xs = f"{xi:9.4f}" if xi >= 0 else f"{'-':>9s}"
            log(f"{r:5.2f} {eps:5.1f} {gap:7.4f} | {s1/(T.G0/2):8.5f} {s2/(2*T.J2):8.5f} | "
                f"{rho1:9.4f} {rho2:9.4f} | {rho1*s1/T.G0:9.4f} {xs}")
    return grid


# ------------------------------------------------------------------ part B2: convergence over the table
def part_b2(Ts, grid):
    log("")
    log("PART B2: convergence over the configurations of Part C: change of rho_1, rho_2 and t from"
        " (L,ell)=(64,8) to (128,16) and to (256,32); absolute for eps <= 4, relative for eps > 4")
    T8 = Ts[(64, 8.0)]
    for key in ((128, 16.0), (256, 32.0)):
        To = Ts[key]
        ab = {"rho_1": 0.0, "rho_2": 0.0, "t": 0.0}
        rl = {"rho_1": 0.0, "rho_2": 0.0, "t": 0.0}
        for r, eps in grid:
            a8, ao = analyse(T8, -1, r, eps), analyse(To, -1, r, eps)
            vals = {"rho_1": (a8[1][1], ao[1][1]), "rho_2": (a8[2][1], ao[2][1]),
                    "t": (a8[1][1] * a8[1][0] / T8.G0, ao[1][1] * ao[1][0] / To.G0)}
            for k_, (x8, xo) in vals.items():
                if eps <= 4.0:
                    ab[k_] = max(ab[k_], abs(x8 - xo))
                else:
                    rl[k_] = max(rl[k_], abs(x8 - xo) / abs(x8))
        log(f"  to {key}: eps <= 4 max |change|: " + ", ".join(f"{k_} {v:.4f}" for k_, v in ab.items())
            + ";  eps > 4 max relative change: " + ", ".join(f"{k_} {v:.4f}" for k_, v in rl.items()))


# ------------------------------------------------------------------ part D: fine grid, items 2 and 3
def grid_tests(T, rs, eg, tag, Th, members=True):
    log(f"  thresholds (L = infinity): eps_-(r) [lower isolated above], eps_+(r) [upper isolated below],"
        f" m_h/2 = {T.mh/2:.4f}")
    tabs, smin = [], np.inf
    for r in rs:
        em, ep = thresholds(r, T.mh)
        lo = {e: analyse(T, -1, r, e) for e in eg if lower_gap(r, e, T.mh) > MARGIN * T.mh}
        e = np.array(sorted(lo))
        s1 = np.array([lo[x][1][0] for x in e]); r1 = np.array([lo[x][1][1] for x in e])
        s2 = np.array([lo[x][2][0] for x in e]); r2 = np.array([lo[x][2][1] for x in e])
        smin = min(smin, np.min(s1 / (T.G0 / 2)), np.min(s2 / (2 * T.J2)))
        t = r1 * s1 / T.G0
        phi = e * t
        d2 = 2 * np.diff(np.diff(phi) / np.diff(e)) / (e[2:] - e[:-2])
        R1, R2 = roots(T, r, 1, e, r1 - 1), roots(T, r, 2, e, r2 - 1, Th)
        log(f"r={r:4.2f}: eps_-={em:.4f}, eps_+={ep:.4f}; lower computed on eps in [{e.min():.3f},{e.max():.1f}]"
            f" ({len(e)} pts); rho_1,- {r1[0]:.4f}..{r1[-1]:.3f} incr {bool(np.all(np.diff(r1) > 0))};"
            f" rho_2,- {r2[0]:.4f}..{r2[-1]:.3f} incr {bool(np.all(np.diff(r2) > 0))}")
        log("   roots (Brent, +- error estimate): rho_1,- = 1 at eps "
            + (", ".join(f"{x:.4f} (+-{dx:.0e})" for x, dx in R1) or "none")
            + ";  rho_2,- = 1 at eps " + (", ".join(f"{x:.4f} (+-{dx:.0e})" for x, dx in R2) or "none"))
        win = (r1 - 1) * (r2 - 1) < 0
        pts = [(x, bool(w_)) for x, w_ in zip(e, win)]
        if np.any(win):
            ia, ib = np.nonzero(win)[0][[0, -1]]
            fine = np.linspace(e[max(ia - 1, 0)], e[min(ib + 1, len(e) - 1)], 81)
            fx = []
            for x in fine:
                if lower_gap(r, x, T.mh) <= MARGIN * T.mh:
                    continue
                a_ = analyse(T, -1, r, x)
                pts.append((x, bool((a_[1][1] - 1) * (a_[2][1] - 1) < 0)))
                if (a_[1][1] - 1) * (a_[2][1] - 1) < 0:
                    fx.append((x, a_[1][0] * (1 - a_[1][1]) / (a_[2][0] * (a_[2][1] - 1))))
            fe, fv = np.array([u for u, _ in fx]), np.array([v for _, v in fx])
            log(f"   finite xi* >= 0 [(rho_1-1)(rho_2-1) < 0] on eps in [{fe.min():.3f},{fe.max():.3f}]"
                f" (81-point refinement, {len(fe)} pts): xi* {fv[0]:.4f} at {fe[0]:.3f} .. {fv[-1]:.2f} at"
                f" {fe[-1]:.3f}; increasing {bool(np.all(np.diff(fv) > 0))},"
                f" decreasing {bool(np.all(np.diff(fv) < 0))}")
        else:
            log("   (rho_1-1)(rho_2-1) >= 0 at every computed point")
        bnd = ([(e[0] - 1e-12, "edge of computed range")]
               + sorted([(x, "rho_1=1") for x, _ in R1] + [(x, "rho_2=1") for x, _ in R2])
               + [(e[-1] + 1e-12, "edge of computed range")])
        wins, ok = [], True
        for (a0, na), (b0, nb_) in zip(bnd[:-1], bnd[1:]):
            ins = [w_ for x, w_ in pts if a0 < x < b0]
            ok = ok and (all(ins) or not any(ins))
            if ins and all(ins):
                wins.append(f"[{a0:.4f} ({na}), {b0:.4f} ({nb_})]")
        log("   windows of finite xi* >= 0 between consecutive roots: " + ("; ".join(wins) or "none")
            + f"; all {len(pts)} computed points (grid and refinement) consistent with them: {ok}")
        neg = e[1:-1][d2 <= 0]
        log(f"   phi increasing {bool(np.all(np.diff(phi) > 0))}; phi'' min {d2.min():.3f} max {d2.max():.3f}"
            + ("" if neg.size == 0 else f"; phi'' <= 0 at eps in [{neg.min():.3f},{neg.max():.3f}]")
            + f"; t_- {t[0]:.4f}..{t[-1]:.3f}; at eps={e[-1]:.1f}: rho_1,- - 2 eps R1 = {r1[-1]-2*e[-1]*T.R1:.4f},"
            f" rho_1,-/(2 eps R1) = {r1[-1]/(2*e[-1]*T.R1):.4f}")
        tabs.append((r, e, t, lo))
    log(f"  min over all computed points of S_i(0)/S_i(0)|_(tau=0): {smin:.4f}")
    log("  grip y = F0 F2/F1^2 that equalises the bracket of (6.12) for two lower levels (eps_a, eps_b),"
        " direct evaluation at the stated levels:")
    tval = lambda r, x: (lambda a_: a_[1][1] * a_[1][0] / T.G0)(analyse(T, -1, r, x, (1,)))
    for r, e, t, _ in tabs:
        out = f"   r={r:4.2f}:"
        for ea, eb in ((0.25, 0.5), (0.5, 1.0), (1.0, 2.0), (2.0, 4.0), (4.0, 8.0), (1.0, 8.0)):
            if min(lower_gap(r, ea, T.mh), lower_gap(r, eb, T.mh)) > MARGIN * T.mh:
                ta, tb = tval(r, ea), tval(r, eb)
                out += f" ({ea:g},{eb:g}) {(ea*ta - eb*tb)/(2*(ea - eb)):.4f}"
        log(out)
    if members:
        log(f"  members with stated margins (exact evaluation at the stated eps, r = 1), {tag}:")
        a4 = analyse(T, -1, 1.0, 4.0)
        log(f"   item 2: level eps=4: rho_1,- = {a4[1][1]:.4f}, rho_2,- = {a4[2][1]:.4f}"
            f" -> rho_- >= {min(a4[1][1], a4[2][1]):.4f} > 1 for every grip")
        xs = []
        for x in (1.2, 2.0):
            a_ = analyse(T, -1, 1.0, x)
            xs.append(a_[1][0] * (1 - a_[1][1]) / (a_[2][0] * (a_[2][1] - 1)))
        log(f"   item 2: levels eps=1.2, 2.0: xi* = {xs[0]:.4f}, {xs[1]:.4f}")
        tt = {}
        for x in (1.0, 2.0, 3.0):
            a_ = analyse(T, -1, 1.0, x, (1,))
            tt[x] = a_[1][1] * a_[1][0] / T.G0
        y12 = (2 * tt[2.0] - 1 * tt[1.0]) / 2
        y23 = (3 * tt[3.0] - 2 * tt[2.0]) / 2
        log(f"   item 3: levels eps=1,2,3: t_- = {tt[1.0]:.4f}, {tt[2.0]:.4f}, {tt[3.0]:.4f};"
            f" y_12 = {y12:.4f}, y_23 = {y23:.4f}")


def part_d(T):
    log("")
    log(f"PART D: fine grid, 71 values of eps in [0.1, 64] (geometric), torus L={T.L}, ell={T.ell};"
        f" lower branch where b_k + eps_k > {MARGIN} m_h")
    log("  item 2: rho_{i,-} increasing on the grid?  crossings of rho_i,- = 1; points with finite xi* >= 0;"
        "  item 3: phi = eps*t_- increasing and convex at the grid points?")
    grid_tests(T, (0.1, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0), np.geomspace(0.1, 64.0, 71),
               f"L={T.L}, ell={T.ell}", Torus(T.L, T.ell, dE=T.dE / 2))


def part_d2(T):
    log("")
    log(f"PART D2: as Part D, both parts, torus L={T.L}, ell={T.ell}; 36 values of eps in [0.1, 64]")
    grid_tests(T, (0.1, 0.5, 1.0, 1.5, 2.0, 3.0), np.geomspace(0.1, 64.0, 36), f"L={T.L}, ell={T.ell}",
               Torus(T.L, T.ell, dE=T.dE / 2))


# ------------------------------------------------------------------ part E: ED on torus L = 4
def part_e():
    log("")
    L, ell = 4, 2.0
    mh = 1 / ell
    g = np.array(np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")).reshape(3, -1)
    q = 2 * np.pi * g / L
    Om = np.sqrt(mh**2 + 2 * np.sum(1 - np.cos(q), axis=0))
    c2 = 1 / (2 * L**3 * Om)
    n = len(Om)
    states = [()] + [(i,) for i in range(n)] + list(combinations_with_replacement(range(n), 2))
    idx = {s: i for i, s in enumerate(states)}
    ns = len(states)
    A = np.zeros((ns, ns))
    cq = np.sqrt(c2)
    for j, s in enumerate(states):
        for m in set(s):
            t = list(s)
            t.remove(m)
            A[idx[tuple(t)], j] += cq[m] * np.sqrt(s.count(m))
    Ef = np.array([Om[list(s)].sum() if s else 0.0 for s in states])
    Qn = np.array([q[0][list(s)].sum() if s else 0.0 for s in states])
    q0 = A + A.T
    nq2 = A @ A + A.T @ A.T + 2 * A.T @ A
    w0 = np.sum(c2)
    S1m, S3m = np.array([[0.0, 1.0], [1.0, 0.0]]), np.diag([1.0, -1.0])
    Mk, F1, F2, tau = 5.0, 0.3, 0.1, 1.0
    eps = Mk
    log(f"PART E: ED of the contract restricted to <= 2 field quanta, cubic torus L={L}, ell={ell}, "
        f"dimension {2*ns}; M_k={Mk}, F1={F1}, F2={F2}, r={tau}, Omega_max={Om.max():.4f}"
        f" (sigma=+1: formal coefficients, the upper branch is not isolated here)")
    base = (np.kron(np.diag(Ef), np.eye(2)) + eps * np.kron(np.eye(ns), S3m)
            - tau * np.kron(np.diag(np.sin(-Qn)), S1m))
    V = Mk * np.kron(F1 * q0 + F2 * (nq2 + w0 * np.eye(ns)), S3m)
    H1 = -tau * np.kron(np.diag(np.cos(-Qn)), S1m)
    H2 = tau * np.kron(np.diag(np.sin(-Qn)), S1m)
    svals = [0.01, 0.02, 0.04]
    res = {}
    for s in [0.0] + svals + [-x for x in svals]:
        E, Vv = np.linalg.eigh(base + s * V)
        out = {}
        for sigma in (+1, -1):
            ref = np.zeros(2 * ns)
            ref[0 if sigma == +1 else 1] = 1.0
            j = int(np.argmax(np.abs(Vv.T @ ref)))
            psi = Vv[:, j]
            d1 = Vv.T @ (H1 @ psi)
            msk = np.arange(len(E)) != j
            out[sigma] = (E[j], psi @ H2 @ psi + 2 * np.sum(d1[msk]**2 / (E[j] - E[msk])))
        res[s] = out
    sarr = np.array(svals)
    T = Torus(L, ell)
    worst = 0.0
    for sigma in (+1, -1):
        for comp in (0, 1):
            f0 = res[0.0][sigma][comp]
            even = np.array([(res[x][sigma][comp] + res[-x][sigma][comp]) / 2 - f0 for x in svals])
            a2 = np.linalg.solve(np.vstack([sarr**2, sarr**4, sarr**6]).T, even)[0]
            if comp == 0:
                form = -Mk**2 * (F1**2 * T.S1(0.0, sigma, tau, eps) + F2**2 * T.S2(0.0, sigma, tau, eps))
            else:
                _, p1 = T.S1d(sigma, tau, eps)
                _, p2 = T.S2d(sigma, tau, eps)
                form = -Mk**2 * (F1**2 * p1 + F2**2 * p2) + sigma * (F2 * w0 * Mk)**2 * tau**2 / eps**3
            worst = max(worst, abs(a2 / form - 1))
            label = "Cost" if comp == 0 else "E''(0)"
            log(f"  sigma={sigma:+d} {label:6s} second order: ED {a2:.10f}  formula {form:.10f}")
    log(f"  max relative deviation: {worst:.2e}")


# ------------------------------------------------------------------ part F: light levels
def part_f():
    log("")
    ell = 8.0
    mh = 1 / ell
    log(f"PART F: light levels eps_k < eps_+(r) (upper branch isolated), ell={ell} (m_h={mh}),"
        f" eps = f*eps_+, both branches, both parts; ring and cubic torus")
    lat = [("ring", Ring(2048, ell)), ("ring", Ring(4096, ell)), ("torus", Torus(128, ell)),
           ("torus", Torus(256, ell))]
    log(f"{'graph':>6s} {'L':>5s} {'r':>5s} {'eps_+':>8s} {'f':>4s} {'eps':>8s} | {'rho_1,+':>9s} {'rho_2,+':>9s}"
        f" {'rho_1,-':>9s} {'rho_2,-':>9s}")
    ext = {}
    for r in (0.25, 0.5, 0.75, 1.0):
        em, ep = thresholds(r, mh)
        for f in (0.3, 0.5, 0.7, 0.9):
            eps = f * ep
            for name, T in lat:
                if name == "ring" and T.L == 4096:
                    parts = (1,)
                else:
                    parts = (1, 2)
                up, dn = analyse(T, +1, r, eps, parts), analyse(T, -1, r, eps, parts)
                v = [up[1][1], up[2][1] if 2 in parts else np.nan, dn[1][1], dn[2][1] if 2 in parts else np.nan]
                log(f"{name:>6s} {T.L:5d} {r:5.2f} {ep:8.5f} {f:4.1f} {eps:8.5f} | "
                    + " ".join(f"{x:9.4f}" for x in v))
                key = (name, T.L)
                lo_, hi_ = ext.get(key, (np.inf, -np.inf))
                vv = [x for x in v if np.isfinite(x)]
                ext[key] = (min(lo_, min(vv)), max(hi_, max(vv)))
    log("  range of all rho_{i,sigma} above, per lattice: "
        + "; ".join(f"{k[0]} L={k[1]}: [{a:.4f}, {b:.4f}]" for k, (a, b) in ext.items()))
    return lat


# ------------------------------------------------------------------ part G: curvature and finite-size checks
def part_g(T8, T32, lat):
    log("")
    log("PART G: accuracy of S_i''(0) (I4) and finite size (I3) at the points of smallest isolation gap."
        " Analytic rho_i against Richardson finite differences with h0 = min(1e-2, 0.05 eps/tau) (step of v3),"
        " h0/2, h0/4: max |rho_i(h) - rho_i(analytic)| over the cases")
    ring, torus = lat[0][1], lat[2][1]
    cases = []
    for r in (0.25, 0.5, 0.75, 1.0):
        ep = thresholds(r, 1 / 8.0)[1]
        for name, T in (("ring", ring), ("torus", torus)):
            for sg in (+1, -1):
                cases.append((f"light {name} L={T.L}", T, sg, r, 0.9 * ep))
    eg8, eg32 = np.geomspace(0.1, 64.0, 71), np.geomspace(0.1, 64.0, 36)
    edge = {}
    for T, eg, rs in ((T8, eg8, (1.25, 1.5, 2.0, 3.0)), (T32, eg32, (1.5, 2.0, 3.0))):
        for r in rs:
            x = min(z for z in eg if lower_gap(r, z, T.mh) > MARGIN * T.mh)
            edge[(T.L, r)] = x
            cases.append((f"lower edge torus L={T.L} ell={T.ell}", T, -1, r, x))
    dev = {}
    for name, T, sg, r, eps in cases:
        an = analyse(T, sg, r, eps)
        gap = (upper_gap(r, eps, T.mh) if sg == 1 else lower_gap(r, eps, T.mh)) / T.mh
        h0 = min(1e-2, 0.05 * eps / r)
        for i in (1, 2):
            f = (lambda P: T.S1(P, sg, r, eps)) if i == 1 else (lambda P: T.S2(P, sg, r, eps))
            f0 = an[i][0]
            for j, h in enumerate((h0, h0 / 2, h0 / 4)):
                _, spp = curv(f, h, f0)
                d = abs(-(eps**2 / r**2) * spp / f0 - an[i][1])
                key = (name, i, j)
                dev[key] = max(dev.get(key, 0.0), d)
        log(f"  {name:28s} sigma={sg:+d} r={r:4.2f} eps={eps:.5f} gap/m_h={gap:.3f}:"
            f" rho_1={an[1][1]:.6f} rho_2={an[2][1]:.6f}")
    for name in dict.fromkeys(c[0] for c in cases):
        log(f"  {name:28s}: " + "; ".join(
            f"rho_{i}: " + ", ".join(f"{dev[(name, i, j)]:.1e}" for j in range(3)) for i in (1, 2))
            + "  (h0, h0/2, h0/4)")
    T128 = torus if torus.L == 128 else Torus(128, 8.0)
    dmax = 0.0
    for r in (1.25, 1.5, 2.0, 3.0):
        x = edge[(64, r)]
        a64, a128 = analyse(T8, -1, r, x), analyse(T128, -1, r, x)
        dmax = max(dmax, abs(a64[1][1] - a128[1][1]), abs(a64[2][1] - a128[2][1]))
        log(f"  finite size, lower edge r={r:4.2f} eps={x:.4f}: rho_1 {a64[1][1]:.6f} (L=64) {a128[1][1]:.6f}"
            f" (L=128); rho_2 {a64[2][1]:.6f} (L=64) {a128[2][1]:.6f} (L=128)")
    log(f"  max |rho_i(L=64) - rho_i(L=128)| at these points: {dmax:.2e}")


if __name__ == "__main__":
    part_a()
    T8 = Torus(64, 8.0)
    Ts = part_b(T8)
    grid = part_c(T8)
    part_b2(Ts, grid)
    part_d(T8)
    part_d2(Ts[(256, 32.0)])
    part_e()
    lat = part_f()
    part_g(T8, Ts[(256, 32.0)], lat)
    (OUT / "torus_mark_inertia.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
