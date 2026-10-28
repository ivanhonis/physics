"""Computation script of 08-ilang-propagation/06-mark-inertia, derivation v2.

Cubic torus (D = 3) of side L, body chain along lattice axis 1, Q = q_1.
The lattice sums of (6.3) are evaluated for the one-quantum (F1^2) and the
two-quantum (F2^2) part separately:
    S_i(P) = << cos^2(th)/(E + a) + sin^2(th)/(E + b) >>_i ,
    a = sigma [omega(P-Q) - omega(P)],  b = -sigma [omega(P-Q) + omega(P)],
with <<f>>_1 = sum_q c_q^2 f(Omega_q, q_1) and
     <<f>>_2 = 2 sum_{q,q'} c_q^2 c_q'^2 f(Omega_q + Omega_q', q_1 + q_1'),
so that E^(2) = -M_k^2 (F1^2 S_1 + F2^2 S_2).  Derived quantities:
    rho_i = -(eps^2/tau^2) S_i''(0)/S_i(0)        (6.6), per part
    t     = -(eps^2/tau^2) S_1''(0)/G0 = T/G0      (bracket of (6.12))
    xi*   = S_1(0)(1-rho_1)/(S_2(0)(rho_2-1))      (F2^2/(c0 F1^2) at which rho = 1)
    R_i   = <<sin^2 Q/E^2>>_i / <<1/E>>_i          (6.1)
One-quantum sums are exact mode sums; two-quantum sums use, for each total
q_1 = Q, a histogram of the pair energies with bin width dE and the exact
zeroth, first and second moments in each bin (error ~ (dE/d)^3, d the distance
to the pole); this is checked against brute-force pair sums on a small torus.
Part E: exact diagonalisation of the total contract restricted to <= 2 field
quanta on the torus L = 4, against the formula (as in Part A of
check_mark_inertia.py for the ring).
Units: c0 = sqrt(kappa_h) = 1, F0 = 1, so eps_k = M_k.
"""
from itertools import combinations_with_replacement
from pathlib import Path

import numpy as np

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


class Torus:
    def __init__(self, L, ell, pairs=True, dE=2e-3):
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
        if pairs:
            self._pairs(dE)

    def _pairs(self, dE):
        L, Om, w = self.L, self.Om, self.w
        nb = int(np.ceil(2 * self.Omax / dE)) + 2
        W, M1, M2 = (np.zeros((L, nb)) for _ in range(3))
        Emin = np.full(L, np.inf)
        for i in range(L):
            for j in range(i, L):
                m = (i + j) % L
                if m > L // 2:
                    continue
                E = (Om[i][:, None] + Om[j][None, :]).ravel()
                ww = (2.0 if i != j else 1.0) * 2 * (w[i][:, None] * w[j][None, :]).ravel()
                b = (E / dE).astype(np.int64)
                d = E - (b + 0.5) * dE
                W[m] += np.bincount(b, ww, nb)
                M1[m] += np.bincount(b, ww * d, nb)
                M2[m] += np.bincount(b, ww * d * d, nb)
                Emin[m] = min(Emin[m], E.min())
        for m in range(L // 2 + 1, L):
            W[m], M1[m], M2[m], Emin[m] = W[L - m], M1[L - m], M2[L - m], Emin[L - m]
        mi, bi = np.nonzero(W > 0)
        Wv = W[mi, bi]
        mu = M1[mi, bi] / Wv
        self.pm, self.pW = mi, Wv
        self.pE = (bi + 0.5) * dE + mu
        self.pV = np.maximum(M2[mi, bi] / Wv - mu**2, 0.0)
        self.Emin2 = Emin
        self.dE = dE
        self.J2 = 0.5 * self._hist(lambda E: 1 / E, lambda E: 2 / E**3)     # J2 = <<1/E>>_2 / 2
        num = self._hist(lambda E: np.sin(self.k[self.pm])**2 / E**2,
                         lambda E: 6 * np.sin(self.k[self.pm])**2 / E**4)
        self.R2 = num / (2 * self.J2)

    def _hist(self, f, f2):
        return np.sum(self.pW * (f(self.pE) + 0.5 * self.pV * f2(self.pE)))

    def coeffs(self, P, sigma, tau, eps):
        wP, tP = omega(P, tau, eps), theta(P, tau, eps)
        p = P - self.k
        th = 0.5 * (tP + theta(p, tau, eps))
        wp = omega(p, tau, eps)
        return np.cos(th)**2, sigma * (wp - wP), np.sin(th)**2, -sigma * (wp + wP)

    def S1(self, P, sigma, tau, eps):
        A, a, B, b = self.coeffs(P, sigma, tau, eps)
        E = self.Om
        return np.sum(self.w * (A[:, None] / (E + a[:, None]) + B[:, None] / (E + b[:, None])))

    def S2(self, P, sigma, tau, eps):
        A, a, B, b = self.coeffs(P, sigma, tau, eps)
        m, E = self.pm, self.pE
        x, y = E + a[m], E + b[m]
        f = A[m] / x + B[m] / y
        f2 = 2 * A[m] / x**3 + 2 * B[m] / y**3
        return np.sum(self.pW * (f + 0.5 * self.pV * f2))

    def S2_gap(self, sigma, tau, eps, P=0.02):
        """Smallest distance of a pair-energy bin edge to a pole, over P in [0, P]."""
        g = np.inf
        for PP in (0.0, P):
            A, a, B, b = self.coeffs(PP, sigma, tau, eps)
            m, E = self.pm, self.pE
            g = min(g, np.min(np.abs(E + a[m])) - self.dE, np.min(np.abs(E + b[m])) - self.dE)
        return g


def curv(f, h=1e-2):
    f0 = f(0.0)
    c = lambda hh: 2 * (f(hh) - f0) / hh**2
    return f0, (4 * c(h) - c(2 * h)) / 3


def lower_gap(tau, eps, mh, n=40001):
    """min over q of Omega_q - (omega(q_1) - eps), L = infinity: (6.4), sigma = -1."""
    q = np.linspace(0, np.pi, n)
    return np.min(np.sqrt(mh**2 + 2 * (1 - np.cos(q))) - (omega(q, tau, eps) - eps))


def upper_ok(part, eps, Omax):
    """(U) of (6.4) at L = infinity: one quantum Omax < 2 eps; two quanta Omax < eps (margin 0.1)."""
    return eps > (Omax / 2 + 0.1 if part == 1 else Omax + 0.1)


def analyse(T, sigma, tau, eps, parts=(1, 2)):
    out = {}
    for i in parts:
        f = (lambda P: T.S1(P, sigma, tau, eps)) if i == 1 else (lambda P: T.S2(P, sigma, tau, eps))
        s0, spp = curv(f)
        out[i] = (s0, -(eps**2 / tau**2) * spp / s0)
    return out


def ok(sigma, part, tau, eps, mh, Omax):
    if sigma == -1:
        return lower_gap(tau, eps, mh) > 0.5 * mh
    return upper_ok(part, eps, Omax)


# ------------------------------------------------------------------ part A: histogram check
def part_a():
    L, ell = 12, 3.0
    log(f"PART A: lattice sums by mode classes and pair histograms vs brute-force mode and ordered-pair"
        f" sums, torus L={L}, ell={ell}")
    g = np.array(np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")).reshape(3, -1)
    q = 2 * np.pi * g / L
    Om = np.sqrt(1 / ell**2 + 2 * np.sum(1 - np.cos(q), axis=0))
    c2 = 1 / (2 * L**3 * Om)
    E = Om[:, None] + Om[None, :]
    Q = q[0][:, None] + q[0][None, :]
    ww = 2 * c2[:, None] * c2[None, :]
    cases = ((-1, 1.0, 1.0), (-1, 1.5, 3.0), (+1, 1.0, 5.0), (+1, 2.0, 6.0))
    for dE in (2e-2, 2e-3):
        T = Torus(L, ell, dE=dE)
        w1 = w2 = 0.0
        for sigma, tau, eps in cases:
            for P in (0.0, 0.02):
                wP, tP = omega(P, tau, eps), theta(P, tau, eps)
                th = 0.5 * (tP + theta(P - Q, tau, eps))
                wp = omega(P - Q, tau, eps)
                b2 = np.sum(ww * (np.cos(th)**2 / (E + sigma * (wp - wP))
                                  + np.sin(th)**2 / (E - sigma * (wp + wP))))
                th1 = 0.5 * (tP + theta(P - q[0], tau, eps))
                wp1 = omega(P - q[0], tau, eps)
                b1 = np.sum(c2 * (np.cos(th1)**2 / (Om + sigma * (wp1 - wP))
                                  + np.sin(th1)**2 / (Om - sigma * (wp1 + wP))))
                w1 = max(w1, abs(T.S1(P, sigma, tau, eps) / b1 - 1))
                w2 = max(w2, abs(T.S2(P, sigma, tau, eps) / b2 - 1))
        log(f"  dE={dE}: max relative deviation S_1 {w1:.2e}, S_2 {w2:.2e}"
            f" (cases (sigma,r,eps) = {cases}, P = 0, 0.02)")
    bR1 = np.sum(c2 * np.sin(q[0])**2 / Om**2) / np.sum(c2 / Om)
    log(f"  R_1: classes {T.R1:.12f}, brute force {bR1:.12f};"
        f"  J2: histogram {T.J2:.12f}, brute force {np.sum(c2[:, None]*c2[None, :]/E):.12f}")


# ------------------------------------------------------------------ part B: convergence in L and ell
def part_b(T8):
    log("")
    log("PART B: convergence in ell and L (c0 = 1); rho_1, rho_2 of the F1^2 and F2^2 parts")
    lattices = [(32, 4.0, True), (48, 6.0, True), (48, 8.0, True), (64, 8.0, True),
                (128, 16.0, False), (256, 32.0, False)]
    cases = [(-1, 1.0, 1.0), (-1, 1.0, 4.0), (-1, 0.5, 2.0), (+1, 1.0, 4.0), (+1, 1.0, 2.5)]
    log(f"{'L':>4s} {'ell':>5s} {'G0':>9s} {'w0':>8s} {'J2':>9s} {'R1':>8s} {'R2':>8s} |"
        + "".join(f"  s={s:+d} r={r} e={e}: rho_1, rho_2 " for s, r, e in cases))
    for L, ell, pairs in lattices:
        T = T8 if (L, ell) == (64, 8.0) else Torus(L, ell, pairs=pairs)
        row = f"{L:4d} {ell:5.1f} {T.G0:9.6f} {T.w0:8.5f} "
        row += (f"{T.J2:9.6f} {T.R1:8.5f} {T.R2:8.5f} |" if pairs else f"{'-':>9s} {T.R1:8.5f} {'-':>8s} |")
        for sigma, r, eps in cases:
            res = analyse(T, sigma, r, eps, parts=(1, 2) if pairs else (1,))
            r1 = res[1][1]
            r2 = res[2][1] if (pairs and ok(sigma, 2, r, eps, T.mh, T.Omax)) else np.nan
            row += f"  {r1:10.5f} {r2:10.5f}          "
        log(row)
    log("(rho_2 is nan where the two-quantum part is not isolated by (6.4) or not computed)")


# ------------------------------------------------------------------ part C: main table
def part_c(T):
    log("")
    log(f"PART C: main table, torus L={T.L}, ell={T.ell} (m_h={T.mh}), c0=1, F0=1, eps_k=M_k")
    log(f"  G0={T.G0:.6f}, w0={T.w0:.6f}, J2={T.J2:.6f}, R1={T.R1:.6f}, R2={T.R2:.6f}, "
        f"Omega_max={T.Omax:.4f}")
    log(f"  edge of (U): F2=0 at eps=Omega_max/2: eps*R1 = {T.Omax/2*T.R1:.4f};"
        f" F2!=0 at eps=Omega_max: eps*R1 = {T.Omax*T.R1:.4f}, eps*R2 = {T.Omax*T.R2:.4f}")
    log("  C_i = S_i(0)/S_i(0)|_{tau=0} (moving mark over held mark), rho_i of the parts, "
        "t = T/G0, xi* = F2^2/(c0 F1^2) at which rho = 1 (- if none >= 0)")
    log(f"{'r':>5s} {'eps':>5s} {'sig':>3s} {'gap':>7s} | {'C_1':>8s} {'C_2':>8s} | "
        f"{'rho_1':>9s} {'rho_2':>9s} | {'t':>9s} {'xi*':>9s}")
    grid = []
    for r in (0.25, 0.5, 1.0, 1.5, 2.0):
        for eps in (0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 16.0, 32.0):
            for sigma in (-1, +1):
                if sigma == -1:
                    gap = lower_gap(r, eps, T.mh)
                    if gap <= 0.5 * T.mh:
                        continue
                    parts = (1, 2)
                else:
                    if not upper_ok(1, eps, T.Omax):
                        continue
                    gap = 2 * eps - T.Omax
                    parts = (1, 2) if upper_ok(2, eps, T.Omax) else (1,)
                grid.append((r, eps, sigma, parts))
                res = analyse(T, sigma, r, eps, parts)
                s1, rho1 = res[1]
                C1 = s1 / (T.G0 / 2)
                t = rho1 * s1 / T.G0
                if 2 in parts:
                    s2, rho2 = res[2]
                    C2 = s2 / (2 * T.J2)
                    xi = s1 * (1 - rho1) / (s2 * (rho2 - 1))
                    xs = f"{xi:9.4f}" if xi >= 0 else f"{'-':>9s}"
                    log(f"{r:5.2f} {eps:5.1f} {sigma:+3d} {gap:7.4f} | {C1:8.5f} {C2:8.5f} | "
                        f"{rho1:9.4f} {rho2:9.4f} | {t:9.4f} {xs}")
                else:
                    log(f"{r:5.2f} {eps:5.1f} {sigma:+3d} {gap:7.4f} | {C1:8.5f} {'-':>8s} | "
                        f"{rho1:9.4f} {'-':>9s} | {t:9.4f} {'-':>9s}")
    return grid


# ------------------------------------------------------------------ part B2: convergence over the table
def part_b2(T8, grid):
    log("")
    log("PART B2: convergence over the configurations of Part C: change of rho_1 and t from"
        " (L,ell)=(64,8) to (256,32) [one quantum], of rho_2 from (48,6) to (64,8) [two quanta];"
        " absolute for eps <= 4, relative (|change|/|value at ell=8|) for eps > 4")
    T6, T32 = Torus(48, 6.0), Torus(256, 32.0, pairs=False)
    ab = {"rho_1": 0.0, "t": 0.0, "rho_2": 0.0}
    rl = {"rho_1": 0.0, "t": 0.0, "rho_2": 0.0}
    for r, eps, sigma, parts in grid:
        a8, a32 = analyse(T8, sigma, r, eps, (1,)), analyse(T32, sigma, r, eps, (1,))
        vals = {"rho_1": (a8[1][1], a32[1][1]),
                "t": (a8[1][1] * a8[1][0] / T8.G0, a32[1][1] * a32[1][0] / T32.G0)}
        if 2 in parts:
            vals["rho_2"] = (analyse(T8, sigma, r, eps, (2,))[2][1], analyse(T6, sigma, r, eps, (2,))[2][1])
        for k, (x8, xo) in vals.items():
            if eps <= 4.0:
                ab[k] = max(ab[k], abs(x8 - xo))
            else:
                rl[k] = max(rl[k], abs(x8 - xo) / abs(x8))
    log("  eps <= 4, max |change|: " + ", ".join(f"{k} {v:.4f}" for k, v in ab.items()))
    log("  eps > 4, max relative change: " + ", ".join(f"{k} {v:.4f}" for k, v in rl.items()))
    log(f"  R1: ell=8 {T8.R1:.5f}, ell=32 {T32.R1:.5f};  G0: ell=8 {T8.G0:.5f}, ell=32 {T32.G0:.5f}")
    return T32


# ------------------------------------------------------------------ part D2: one-quantum tests at ell = 32
def part_d2(T):
    log("")
    log(f"PART D2: F1^2 part only (all that items 3 and the upper-branch bound of item 2 need from it),"
        f" torus L={T.L}, ell={T.ell}; 36 values of eps in [0.1, 64]; same criteria as Part D")
    eg = np.geomspace(0.1, 64.0, 36)
    for r in (0.1, 0.5, 1.0, 1.5, 2.0, 3.0):
        lo = {e: analyse(T, -1, r, e, (1,))[1] for e in eg if lower_gap(r, e, T.mh) > 0.5 * T.mh}
        u1 = {e: analyse(T, +1, r, e, (1,))[1] for e in eg if upper_ok(1, e, T.Omax)}
        e = np.array(sorted(lo))
        r1 = np.array([lo[x][1] for x in e])
        t = np.array([lo[x][1] * lo[x][0] / T.G0 for x in e])
        phi = e * t
        d2 = 2 * np.diff(np.diff(phi) / np.diff(e)) / (e[2:] - e[:-2])
        neg = e[1:-1][d2 <= 0]
        c = np.array([x for x in sorted(u1) if x in lo])
        tp = np.array([u1[x][1] * u1[x][0] / T.G0 for x in c])
        tm = np.array([lo[x][1] * lo[x][0] / T.G0 for x in c])
        psi = c * (tm - tp)
        yb = (tp + tm) / 4
        e1 = np.interp(1.0, r1, e) if r1.min() < 1 < r1.max() else np.nan
        out = (f"r={r:4.2f}: lower eps in [{e.min():.3f},{e.max():.1f}]; rho_1,- incr {bool(np.all(np.diff(r1) > 0))},"
               f" rho_1,-=1 at eps={e1:.3f}; phi incr {bool(np.all(np.diff(phi) > 0))}, phi''>0 "
               + ("everywhere" if neg.size == 0 else f"except eps in [{neg.min():.3f},{neg.max():.3f}]")
               + f"; max rho_1,+ = {max(v[1] for v in u1.values()):.4f}")
        if c.size:
            out += f"; psi incr {bool(np.all(np.diff(psi) > 0))}; y_b in [{yb.min():.4f},{yb.max():.4f}]"
        log(out)
        if r == 1.0:
            ys = []
            for ea, eb in ((0.25, 0.5), (0.5, 1.0), (1.0, 2.0), (2.0, 4.0), (4.0, 8.0)):
                ta, tb = np.interp(ea, e, t), np.interp(eb, e, t)
                ys.append(f"({ea:g},{eb:g}) {(ea*ta - eb*tb)/(2*(ea - eb)):.4f}")
            log("   r=1, two-level grips y_ab (interpolated): " + " ".join(ys))


# ------------------------------------------------------------------ part D: fine grid, items 2 and 3
def part_d(T):
    log("")
    log(f"PART D: fine grid, 71 values of eps in [0.1, 64] (geometric), torus L={T.L}, ell={T.ell}")
    log("  lower branch where lower gap > m_h/2; upper branch where (U) holds with margin 0.1")
    log("  item 2: rho_{i,-} increasing in eps?  window [e1,e2]: rho_{1,-}(e1)=1, rho_{2,-}(e2)=1;"
        "  xi*_- monotone?  max rho_{i,+} < 1?")
    log("  item 3: phi = eps*t_- increasing and strictly convex?  psi = eps*(t_- - t_+) increasing?"
        "  y_b = (t_+ + t_-)/4")
    eg = np.geomspace(0.1, 64.0, 71)
    tabs, store, smin = [], {}, np.inf
    for r in (0.1, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0):
        tau = r
        lo = {e: analyse(T, -1, tau, e) for e in eg if lower_gap(tau, e, T.mh) > 0.5 * T.mh}
        u1 = {e: analyse(T, +1, tau, e, (1,))[1] for e in eg if upper_ok(1, e, T.Omax)}
        u2 = {e: analyse(T, +1, tau, e, (2,))[2] for e in eg if upper_ok(2, e, T.Omax)}
        store[r] = (lo, u1, u2)
        smin = min([smin] + [v[i][0] / (T.G0 / 2 if i == 1 else 2 * T.J2) for v in lo.values() for i in (1, 2)]
                   + [v[0] / (T.G0 / 2) for v in u1.values()] + [v[0] / (2 * T.J2) for v in u2.values()])
        e = np.array(sorted(lo))
        s1 = np.array([lo[x][1][0] for x in e]); r1 = np.array([lo[x][1][1] for x in e])
        s2 = np.array([lo[x][2][0] for x in e]); r2 = np.array([lo[x][2][1] for x in e])
        t = r1 * s1 / T.G0
        phi = e * t
        sl = np.diff(phi) / np.diff(e)
        d2 = 2 * np.diff(sl) / (e[2:] - e[:-2])
        xi = s1 * (1 - r1) / (s2 * (r2 - 1))
        idx = np.nonzero(xi >= 0)[0]
        if idx.size:
            fine = np.linspace(e[max(idx[0] - 1, 0)], e[min(idx[-1] + 1, len(e) - 1)], 81)
            fine = [x for x in fine if lower_gap(tau, x, T.mh) > 0.5 * T.mh]
            fx = []
            for x in fine:
                a_ = analyse(T, -1, tau, x)
                v = a_[1][0] * (1 - a_[1][1]) / (a_[2][0] * (a_[2][1] - 1))
                if v >= 0:
                    fx.append((x, v))
            fe, fv = np.array([u for u, _ in fx]), np.array([v for _, v in fx])
            wmsg = (f" xi*_- >= 0 on eps in [{fe.min():.3f},{fe.max():.3f}] (81-point refinement,"
                    f" {len(fe)} pts), xi* {fv.min():.4f}..{fv.max():.2f},"
                    f" increasing {bool(np.all(np.diff(fv) > 0))}, decreasing {bool(np.all(np.diff(fv) < 0))}")
        else:
            wmsg = " xi*_- < 0 everywhere"
        log(f"r={r:4.2f}: lower on eps in [{e.min():.3f},{e.max():.1f}] ({len(e)} pts);"
            f" rho_1,- {r1[0]:.4f}..{r1[-1]:.3f} incr {bool(np.all(np.diff(r1) > 0))};"
            f" rho_2,- {r2[0]:.4f}..{r2[-1]:.3f} incr {bool(np.all(np.diff(r2) > 0))}")
        log("  " + wmsg)
        neg = e[1:-1][d2 <= 0]
        log(f"   phi increasing {bool(np.all(np.diff(phi) > 0))}; phi'' min {d2.min():.3f} max {d2.max():.3f}"
            + ("" if neg.size == 0 else f"; phi'' <= 0 at eps in [{neg.min():.3f},{neg.max():.3f}]")
            + f"; t_- {t[0]:.4f}..{t[-1]:.3f}")
        if u1:
            eu = np.array(sorted(u1))
            r1p = np.array([u1[x][1] for x in eu])
            t1p = np.array([u1[x][1] * u1[x][0] / T.G0 for x in eu])
            com = [x for x in eu if x in lo]
            msg = f"   upper F1^2 on eps >= {eu.min():.3f}: max rho_1,+ = {r1p.max():.4f}"
            if u2:
                msg += f"; upper F2^2 on eps >= {min(u2):.3f}: max rho_2,+ = {max(v[1] for v in u2.values()):.4f}"
            log(msg)
            if com:
                c = np.array(com)
                tp = np.array([u1[x][1] * u1[x][0] / T.G0 for x in c])
                tmn = np.array([lo[x][1][1] * lo[x][1][0] / T.G0 for x in c])
                gap = np.array([lo[x][1][1] - u1[x][1] for x in c]) / (4 * c * T.R1)
                psi = c * (tmn - tp)
                mixed = [min(lo[x][1][1], lo[x][2][1]) - max(u1[x][1], u2[x][1]) for x in c if x in u2]
                yb = (tp + tmn) / 4
                d11 = min(lo[x][1][1] - u1[x][1] for x in c)
                log(f"   both branches on eps >= {c.min():.3f}: psi increasing {bool(np.all(np.diff(psi) > 0))};"
                    f" y_b in [{yb.min():.4f},{yb.max():.4f}]; min(rho_1,- - rho_1,+) = {d11:.4f};"
                    f" (rho_1,- - rho_1,+)/(4 eps R1) = {gap[0]:.4f} at eps={c[0]:.3f}, {gap[-1]:.4f} at eps={c[-1]:.1f}"
                    + ("" if not mixed else f"; F2!=0: min[min(rho_i,-) - max(rho_i,+)] = {min(mixed):.4f}"))
        tabs.append((r, e, t))
    log(f"  min over all computed points of S_i(0)/S_i(0)|_(tau=0) (both parts, both branches): {smin:.4f}")
    dmax = {}
    for sg, j in ((-1, 0), (+1, 1), (+1, 2)):
        a_, b_ = store[0.25][j], store[2.0][j]
        com = [x for x in a_ if x in b_ and x >= 2.0]
        if sg == -1:
            for i in (1, 2):
                dmax[(i, sg)] = max(abs(a_[x][i][1] - b_[x][i][1]) for x in com)
        else:
            dmax[(j, sg)] = max(abs(a_[x][1] - b_[x][1]) for x in com)
    log("  r-dependence, eps >= 2: max |rho(r=2) - rho(r=0.25)|: "
        + ", ".join(f"rho_{i},{'+' if sg > 0 else '-'} {v:.4f}" for (i, sg), v in dmax.items()))
    log("  grip y = F0 F2/F1^2 that equalises the bracket of (6.12) for two lower levels (eps_a, eps_b):")
    for r, e, t in tabs:
        out = f"   r={r:4.2f}:"
        for ea, eb in ((0.25, 0.5), (0.5, 1.0), (1.0, 2.0), (2.0, 4.0), (4.0, 8.0), (1.0, 8.0)):
            if ea >= e.min() and eb <= e.max():
                ta, tb = np.interp(ea, e, t), np.interp(eb, e, t)
                out += f" ({ea:g},{eb:g}) {(ea*ta - eb*tb)/(2*(ea - eb)):.4f}"
        log(out)


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
        f"dimension {2*ns}; M_k={Mk}, F1={F1}, F2={F2}, r={tau}, Omega_max={Om.max():.4f}")
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
        for sigma, col in ((+1, 1), (-1, 0)):
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
                _, p1 = curv(lambda P: T.S1(P, sigma, tau, eps))
                _, p2 = curv(lambda P: T.S2(P, sigma, tau, eps))
                form = -Mk**2 * (F1**2 * p1 + F2**2 * p2) + sigma * (F2 * w0 * Mk)**2 * tau**2 / eps**3
            worst = max(worst, abs(a2 / form - 1))
            label = "Cost" if comp == 0 else "E''(0)"
            log(f"  sigma={sigma:+d} {label:6s} second order: ED {a2:.10f}  formula {form:.10f}")
    log(f"  max relative deviation: {worst:.2e}")


if __name__ == "__main__":
    part_a()
    T8 = Torus(64, 8.0)
    part_b(T8)
    grid = part_c(T8)
    T32 = part_b2(T8, grid)
    part_d(T8)
    part_d2(T32)
    part_e()
    (OUT / "torus_mark_inertia.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
