"""Check (item 3, leading order in 1/S): mutual cost of two held sources on the cubic torus.

Units J S = 1.  C_2 = 1/2 P^T T P + 1/2 Q^T V Q, T_k = z(1+gamma_k), V_k = z(1-gamma_k); q1 = Q, q2 = E P.
(1) Transverse direction sources (linear in q): separation part from ghat; single objects, two-object cells,
    and a single object against a cell along the separation (midpoint against end-point separation).
(2) Static quadratic sources dH_i = 1/2 Q^T A_i Q + 1/2 P^T B_i P (along-n sources on objects and cells; changed
    links R2 in four orientation pairs): E_12 = -2 int_0^inf dtau <dH_1(tau) dH_2(0)>_c, Wick with G_QQ, G_PP and
    G_QP = (i/2) F (tau > 0); far from the push: the two zero modes (k = 0, k = Q) are left out.  R2 is compared
    with the continuum formula at the separation of the link midpoints.
(3) Held spin R1 with the retarded vertex of Step 12, K(nu) = a(nu) 1 + b(nu) eps (per unit |g'| s_b):
    a = nu^2/(nu^2+D^2), b = sgn(sigma) eps_x D nu/(nu^2+D^2), D = |g'|/J;
    E_12 = -1/2 int dnu/2pi Tr[K1 G12 K2 G21], lattice G(nu) at (r,0,0) by summing over (k2,k3) for each k1,
    tori L = 32, 64, 128, 256; against the continuum crossover function
    J S E/(|g'1 g'2| s1 s2) = -kappa_par F(beta)/r^3, beta = 2 r D / sqrt(2z) (A), and against the same with the
    off-diagonal part G12 = G0 (1 + gam eps), gam = -(eps1+eps2) nu/T_0, of the continuum covariance (B).
Output: output/spinwave_mutual.txt
"""
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import ive
from scipy import fft as sfft

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
Z = 6
CS = np.sqrt(2 * Z)                       # speed of the copies, units J S = 1
KAP = np.sqrt(2 * Z) / (32 * np.pi ** 3)  # kappa_par
PRE = np.sqrt(3) / (8 * np.pi ** 3)       # prefactor of (8.17)


def kgrid(L):
    k = 2 * np.pi * np.arange(L) / L
    c = np.cos(k)
    g = (c[:, None, None] + c[None, :, None] + c[None, None, :]) / 3.0
    return g


def ghat(L):
    k = 2 * np.pi * np.arange(L) / L
    lap = 2 * ((1 - np.cos(k))[:, None, None] + (1 - np.cos(k))[None, :, None] + (1 - np.cos(k))[None, None, :])
    inv = np.zeros_like(lap)
    inv[lap > 1e-12] = 1.0 / lap[lap > 1e-12]
    return np.real(np.fft.ifftn(inv))


def ghat_inf(x):
    """Infinite cubic lattice: (Lap^{-1})(x) = int_0^inf prod_i e^{-2t} I_{x_i}(2t) dt."""
    f = lambda t: np.prod([ive(abs(int(c)), 2 * t) for c in x])
    return quad(f, 0, np.inf, limit=400, epsabs=1e-13, epsrel=1e-11)[0]


def eps(x):
    return (-1) ** (int(sum(x)) % 2)


def check_58(L=6, eta=0.7):
    n = L ** 3
    co = np.array(np.unravel_index(np.arange(n), (L,) * 3)).T
    adj = np.zeros((n, n))
    for d in range(3):
        sh = co.copy(); sh[:, d] = (sh[:, d] + 1) % L
        j = np.ravel_multi_index(sh.T, (L,) * 3)
        adj[np.arange(n), j] += 1; adj[j, np.arange(n)] += 1
    V = Z * np.eye(n) - adj
    V[0, 0] += eta
    Ga = np.linalg.inv(V)
    g = ghat(L).ravel()
    dif = lambda a, b: np.ravel_multi_index(tuple((co[a] - co[b]) % L), (L,) * 3)
    err = 0.0
    for a, b in [(5, 17), (40, 101), (3, 3), (0, 77)]:
        f = 1 / eta + g[dif(a, b)] - g[dif(a, 0)] - g[dif(b, 0)] + g[0]
        err = max(err, abs(f - Ga[a, b]))
    return err


def pert(kind, x, e=None):
    """Return (A, B) as lists of (site, site, value), per unit strength."""
    x = tuple(x)
    if kind == "along":
        A = [(x, x, -eps(x))]
        return A, A
    if kind == "along_cell":
        x2 = (x[0], x[1] + 1, x[2])
        A = [(x, x, -eps(x)), (x2, x2, -eps(x))]
        return A, A
    if kind == "link":
        y = tuple(np.array(x) - np.array(e))
        A = [(x, x, 1), (y, y, 1), (x, y, -1), (y, x, -1)]
        B = [(x, x, 1), (y, y, 1), (x, y, 1), (y, x, 1)]
        return A, B
    raise ValueError(kind)


def contraction(M1, M2, L):
    w, i1, i2 = [], [], []
    for a, b, u in M1:
        for c, d, v in M2:
            w.append(u * v)
            i1.append(np.ravel_multi_index(tuple(np.mod(np.array(a) - np.array(c), L)), (L,) * 3))
            i2.append(np.ravel_multi_index(tuple(np.mod(np.array(b) - np.array(d), L)), (L,) * 3))
    return np.array(w), np.array(i1), np.array(i2)


def mutual_quadratic(L, configs, nodes=300):
    g = kgrid(L)
    om = Z * np.sqrt(np.clip(1 - g ** 2, 0, None))
    mask = om > 1e-9
    Tk = np.where(mask, Z * (1 + g), 0.0)
    Vk = np.where(mask, Z * (1 - g), 0.0)
    omm = np.where(mask, om, 1.0)
    pre = []
    for (A1, B1), (A2, B2) in configs:
        pre.append((contraction(A1, A2, L), contraction(B1, B2, L),
                    contraction(A1, B2, L), contraction(B1, A2, L)))
    s, ws = np.polynomial.legendre.leggauss(nodes)
    lo, hi = np.log(1e-7), np.log(200.0)
    sv = 0.5 * (hi - lo) * s + 0.5 * (hi + lo)
    wv = 0.5 * (hi - lo) * ws
    acc = np.zeros(len(configs))
    for sj, wj in zip(sv, wv):
        tau = np.exp(sj)
        ex = np.where(mask, np.exp(-omm * tau), 0.0)
        GQ = sfft.ifftn(Tk / (2 * omm) * ex, workers=-1).real.ravel()
        GP = sfft.ifftn(Vk / (2 * omm) * ex, workers=-1).real.ravel()
        F = sfft.ifftn(ex, workers=-1).real.ravel()
        for n, (qq, pp, qp, pq) in enumerate(pre):
            val = 0.5 * np.sum(qq[0] * GQ[qq[1]] * GQ[qq[2]]) + 0.5 * np.sum(pp[0] * GP[pp[1]] * GP[pp[2]]) \
                - 0.125 * (np.sum(qp[0] * F[qp[1]] * F[qp[2]]) + np.sum(pq[0] * F[pq[1]] * F[pq[2]]))
            acc[n] += wj * tau * val
    return -2 * acc


def cont_link(e1, e2, e12, R):
    """Continuum (8.17) integral: J E/(delta1 delta2 S) for two changed links (unit vectors e1, e2 from y to x,
    e12 = eps_x1 eps_x2) whose midpoints are separated by the vector R."""
    R = np.asarray(R, float); Rn = np.linalg.norm(R); Rh = R / Rn
    E1 = np.r_[0, e1]; E2 = np.r_[0, e2]; t0 = np.r_[1.0, 0, 0, 0]
    M1 = np.outer(E1, E1) - (2 / Z) * np.outer(t0, t0)
    M2 = np.outer(E2, E2) - (2 / Z) * np.outer(t0, t0)

    def C(t):
        X = np.r_[t, Rh]; rho = np.linalg.norm(X); n = X / rho
        I = np.eye(4) - 4 * np.outer(n, n)
        cross = I[0, 0] * (E1 @ I @ E2) - (I @ E1)[0] * (I @ E2)[0]
        return (4 * np.trace(M1 @ I @ M2 @ I) - (16 / Z) * e12 * cross) / rho ** 8
    val = quad(C, -np.inf, np.inf, epsabs=1e-14, epsrel=1e-12)[0]
    return -np.sqrt(2 * Z) / (16 * np.pi ** 4) * val / Rn ** 7


def F_hat(beta, vs):
    """Continuum crossover function of (8.18) for equal held spins (beta1 = beta2 = beta), vs = sgn(s1 s2) e1 e2."""
    f = lambda u: np.exp(-u) * u ** 2 * (u ** 2 - vs * beta ** 2) / (u ** 2 + beta ** 2) ** 2
    if beta == 0:
        return 1.0
    return quad(f, 0, beta, limit=400, epsabs=1e-15, epsrel=1e-12)[0] + \
        quad(f, beta, np.inf, limit=400, epsabs=1e-15, epsrel=1e-12)[0]


def F_full(beta, r, e1, e2, s=1):
    """(8.18) including the off-diagonal part of the continuum covariance, G12 = G0 (1 + gam eps),
    gam = -(e1+e2) nu/T_0 with nu = c u/(2r); held spins with sgn(sigma1) = sgn(sigma2) = s."""
    T0 = 2 * Z

    def f(u):
        a = u ** 2 / (u ** 2 + beta ** 2)
        b1 = s * e1 * beta * u / (u ** 2 + beta ** 2)
        b2 = s * e2 * beta * u / (u ** 2 + beta ** 2)
        gam = (e1 + e2) * CS * u / (2 * r * T0)
        return np.exp(-u) * ((a * a - b1 * b2) * (1 - gam ** 2) + 2 * gam * a * (b1 + b2))
    if beta == 0:
        return quad(f, 0, np.inf, limit=400, epsabs=1e-15, epsrel=1e-12)[0]
    return quad(f, 0, beta, limit=400, epsabs=1e-15, epsrel=1e-12)[0] + \
        quad(f, beta, np.inf, limit=400, epsabs=1e-15, epsrel=1e-12)[0]


def r1_lattice(L, rs, deltas, nodes=240):
    """Lattice value of J S E_12/(|g'1 g'2| s1 s2) for held spins with sgn(sigma1) = sgn(sigma2) = +1 at 0 and
    (r,0,0).  G^QQ, G^PP, G^QP at (r,0,0) for all frequency nodes by summing over (k2,k3) for each k1
    (zero modes k = 0, Q left out)."""
    s, ws = np.polynomial.legendre.leggauss(nodes)
    lo, hi = np.log(1e-5), np.log(300.0)
    nus = np.exp(0.5 * (hi - lo) * s + 0.5 * (hi + lo))
    wv = 0.5 * (hi - lo) * ws
    k = 2 * np.pi * np.arange(L) / L
    c = np.cos(k)
    C23 = (c[:, None] + c[None, :]).ravel()
    nu2 = nus ** 2
    SQ = np.zeros((L, nodes)); SP = np.zeros((L, nodes)); SX = np.zeros((L, nodes))
    for i1 in range(L):
        g = (c[i1] + C23) / 3.0
        om2 = Z ** 2 * (1 - g ** 2)
        m = om2 > 1e-12
        g, om2 = g[m], om2[m]
        den = 1.0 / (nu2[:, None] + om2[None, :])
        SQ[i1] = den @ (Z * (1 + g))
        SP[i1] = den @ (Z * (1 - g))
        SX[i1] = -nus * den.sum(axis=1)
    cosm = np.cos(np.outer(rs, k)) / L ** 3
    GQ, GP, GX = cosm @ SQ, cosm @ SP, cosm @ SX          # (len(rs), nodes)
    acc = np.zeros((len(deltas), len(rs)))
    for ir, r in enumerate(rs):
        e1, e2 = 1, (-1) ** r
        g0, g1 = GQ[ir], e2 * GX[ir]                       # G12 = [[GQ, e2 GX], [-e1 GX, e1 e2 GP]]
        gp = e1 * e2 * GP[ir]
        for idl, D in enumerate(deltas):
            a = nu2 / (nu2 + D ** 2)
            b = D * nus / (nu2 + D ** 2)
            # Tr[K1 G12 K2 G21], K_i = a 1 + e_i b eps, G21 = G12(-nu)^T, written out for 2x2 matrices
            G12 = np.array([[g0, g1], [-e1 * GX[ir], gp]])
            G21 = np.array([[g0, e1 * GX[ir]], [-g1, gp]])
            K1 = np.array([[a, e1 * b], [-e1 * b, a]])
            K2 = np.array([[a, e2 * b], [-e2 * b, a]])
            M = np.einsum("ijn,jkn,kln,lin->n", K1, G12, K2, G21)
            acc[idl, ir] = np.sum(wv * nus * M)
    return -acc / (2 * np.pi)


def main():
    out = ["# Mutual cost of two held sources, leading order in 1/S, cubic torus (units as stated per block)"]
    out.append(f"\n(5.8) with kappa_h = J S, kappa_a = h_p against direct inverse (L=6): max error {check_58():.2e}")

    out.append("\n## (1) Transverse sources: separation part J E_r/(g1 g2 (m1perp.m2perp))")
    out.append("single objects: -eps1 eps2 ghat(r); cells (x, x+e2), + on the first object: -eps1 eps2 sum ghat")
    out.append(f"ghat_inf(0) = {ghat_inf((0, 0, 0)):.7f} (gamma_3 = 0.2527310)")
    out.append("r   eps1eps2   single: J E_r/(g1g2)  4 pi r ghat_inf(r)   cells: J E_r/(g1g2)  pi r sum ghat_inf"
               "   torus check: ghat_L(r)-ghat_L(8) for L=16, 32, 64 vs ghat_inf(r)-ghat_inf(8)")
    gl = {L: ghat(L) for L in (16, 32, 64)}
    g8 = ghat_inf((8, 0, 0))
    gi = {r: ghat_inf((r, 0, 0)) for r in range(2, 10)}
    for r in range(2, 9):
        e12 = (-1) ** r
        gs = gi[r]
        gc = 2 * gs + ghat_inf((r, 1, 0)) + ghat_inf((r, -1, 0))
        tor = "  ".join(f"{gl[L][r, 0, 0] - gl[L][8, 0, 0]:.6f}" for L in (16, 32, 64))
        out.append(f"{r:2d}   {e12:+d}        {-e12 * gs: .6f}            {4 * np.pi * r * gs:.4f}"
                   f"             {-e12 * gc: .6f}         {np.pi * r * gc:.4f}            {tor}   {gs - g8:.6f}")
    out.append("single object at 0, cell (r e1, (r+1) e1) along the separation: 4 pi R [ghat(r)+ghat(r+1)]/2 with"
               " R = midpoint separation r+1/2, and with R = end-point separation r")
    for r in range(2, 9):
        s2 = gi[r] + gi[r + 1]
        out.append(f"{r:2d}   midpoint: {2 * np.pi * (r + 0.5) * s2:.5f}   end point: {2 * np.pi * r * s2:.5f}")

    out.append("\n## Continuum coefficients")
    out.append(f"along n, single:  J S E/(g1 g2) = -eps1 eps2 kappa_par / r^3, kappa_par = sqrt(2z)/(32 pi^3) = {KAP:.7f}")
    out.append(f"held spin, r >> l_b: S E/(J sig1 sig2) = +eps1 eps2 lambda / r^5, lambda = 3 sqrt3/(8 pi^3) = "
               f"{3 * np.sqrt(3) / (8 * np.pi ** 3):.7f}")
    ex, ey, ez = [1, 0, 0], [0, 1, 0], [0, 0, 1]
    geo = {"par (e1,e1)": (ex, ex, lambda e: 43 / 6 + 2.5 * e),
           "perp same (e2,e2)": (ey, ey, lambda e: 4 / 3 - 5 / 12 * e),
           "perp cross (e2,e3)": (ey, ez, lambda e: 1 / 12),
           "mixed (e1,e2)": (ex, ey, lambda e: -0.5)}
    out.append("changed links, separation r e1: J E/(d1 d2 S) * r^7 = -sqrt3/(8 pi^3) a; numerical integral against a:")
    for nm, (u, v, af) in geo.items():
        for e in (1, -1):
            num = cont_link(u, v, e, [1, 0, 0])
            out.append(f"  {nm:20s} eps1eps2={e:+d}: integral {num:.8f}   closed form a={af(e):.6f}: {-PRE * af(e):.8f}")

    out.append("\n## (2) Static quadratic sources, lattice (zero modes left out); ratio = lattice / continuum")
    out.append("columns: r, eps1eps2, along single [J S E/(g1g2), ratio], along cell [.., ratio vs 4x], then J E/(d1d2S)"
               " and ratio for links: par (e1 at 0, e1 at r e1), perp same (e2, e2), perp cross (e2, e3), mixed (e1, e2);"
               " link continuum at the midpoint separation R")
    rs = list(range(2, 13))
    Rvec = {"par": lambda r: [r, 0, 0], "perp": lambda r: [r, 0, 0],
            "cross": lambda r: [r, 0.5, -0.5], "mixed": lambda r: [r + 0.5, -0.5, 0]}
    cref = {}
    for r in rs:
        e = (-1) ** r
        cref[r] = [-e * KAP / r ** 3, -4 * e * KAP / r ** 3,
                   cont_link(ex, ex, e, Rvec["par"](r)), cont_link(ey, ey, e, Rvec["perp"](r)),
                   cont_link(ey, ez, e, Rvec["cross"](r)), cont_link(ex, ey, e, Rvec["mixed"](r))]
    ratios = {}
    for L in (32, 64, 128):
        configs = []
        for r in rs:
            x2 = (r, 0, 0)
            configs += [(pert("along", (0, 0, 0)), pert("along", x2)),
                        (pert("along_cell", (0, 0, 0)), pert("along_cell", x2)),
                        (pert("link", (0, 0, 0), ex), pert("link", x2, ex)),
                        (pert("link", (0, 0, 0), ey), pert("link", x2, ey)),
                        (pert("link", (0, 0, 0), ey), pert("link", x2, ez)),
                        (pert("link", (0, 0, 0), ex), pert("link", x2, ey))]
        res = mutual_quadratic(L, configs).reshape(len(rs), 6)
        out.append(f"L = {L}")
        ratios[L] = np.zeros_like(res)
        for i, r in enumerate(rs):
            p = np.array(cref[r])
            ratios[L][i] = res[i] / p
            row = "  ".join(f"{res[i, j]: .3e} {res[i, j] / p[j]:6.3f}" for j in range(6))
            out.append(f"{r:2d} {(-1) ** r:+d}  {row}")
        if L == 32:
            along32 = res[:, 0].copy()
    out.append("ratio extrapolated to L -> infinity: Aitken from L = 32, 64, 128 (geometric finite-size error);"
               " the L = 128 value where the change from 64 to 128 is below 1e-3 or not geometric")
    for i, r in enumerate(rs):
        x1, x2, x3 = ratios[32][i], ratios[64][i], ratios[128][i]
        d1, d2 = x2 - x1, x3 - x2
        geo_ = (np.abs(d2) > 1e-3) & (d1 * d2 > 0) & (np.abs(d2) < np.abs(d1))
        exv = np.where(geo_, x3 + d2 / np.where(geo_, d1 / np.where(geo_, d2, 1.0) - 1, 1.0), x3)
        out.append(f"{r:2d}  " + "  ".join(f"{v:6.3f}" for v in exv))

    out.append("\n## (3) Held spin R1, retarded vertex (Step 12); J S E/(|g'1 g'2| s1 s2), sgn sigma1 = sgn sigma2,"
               " so vs = eps1 eps2 = (-1)^r")
    out.append("continuum crossover function F(beta) (equal held spins), with its small-beta form 1 - pi (3+vs) beta/4"
               " and large-beta form -2 vs/beta^2 + 24 (1+2 vs)/beta^4")
    for vs in (1, -1):
        for beta in (0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0):
            Fv = F_hat(beta, vs)
            out.append(f"  vs={vs:+d} beta={beta:7.2f}: F = {Fv: .6e}   small-beta form {1 - np.pi * (3 + vs) * beta / 4: .6e}"
                       f"   large-beta form {-2 * vs / beta ** 2 + 24 * (1 + 2 * vs) / beta ** 4: .6e}")
    lo_, hi_ = 0.1, 10.0
    for _ in range(80):
        mid = 0.5 * (lo_ + hi_)
        if F_hat(mid, 1) > 0:
            lo_ = mid
        else:
            hi_ = mid
    out.append(f"  vs=+1: F changes sign at beta_0 = {0.5 * (lo_ + hi_):.5f} (r_0 = beta_0 l_b / 2); vs=-1: F > 0 at every beta")
    deltas = [0.0, 0.2, 0.5, 2.0]
    out.append("lattice against continuum: D = |g'|/J = " + ", ".join(f"{d:g}" for d in deltas)
               + f"; l_b = sqrt(2z)/D = " + ", ".join("inf" if d == 0 else f"{CS / d:.2f}" for d in deltas))
    out.append("continuum A = (8.18): -kappa_par F(beta)/r^3; continuum B = (8.18) with the off-diagonal part of the"
               " covariance (nonzero for eps1 = eps2 only)")
    out.append("columns per D: lattice value, ratio lattice/A, ratio lattice/B")
    contA = np.array([[-KAP * F_hat(2 * r * D / CS, (-1) ** r) / r ** 3 for r in rs] for D in deltas])
    contB = np.array([[-KAP * F_full(2 * r * D / CS, r, 1, (-1) ** r) / r ** 3 for r in rs] for D in deltas])
    r1 = {}
    for L in (32, 64, 128, 256):
        r1[L] = r1_lattice(L, rs, deltas)
        out.append(f"L = {L}")
        for ir, r in enumerate(rs):
            row = [f"{r1[L][idl, ir]: .4e} {r1[L][idl, ir] / contA[idl, ir]:6.3f} {r1[L][idl, ir] / contB[idl, ir]:6.3f}"
                   for idl in range(len(deltas))]
            out.append(f"{r:2d} {(-1) ** r:+d}  " + "  ".join(row))
        if L == 32:
            dev = np.max(np.abs(r1[L][0] - np.array([(-1) ** r for r in rs]) * along32) / np.abs(along32))
            out.append(f"cross-check D = 0 (frequency domain) against the along-n single column (time domain), L = 32:"
                       f" max relative difference {dev:.2e}")
    out.append("ratio lattice/B extrapolated to L -> infinity: Aitken from L = 64, 128, 256 (as in block (2))")
    for ir, r in enumerate(rs):
        x1, x2, x3 = (r1[L][:, ir] / contB[:, ir] for L in (64, 128, 256))
        d1, d2 = x2 - x1, x3 - x2
        geo_ = (np.abs(d2) > 1e-3) & (d1 * d2 > 0) & (np.abs(d2) < np.abs(d1))
        exv = np.where(geo_, x3 + d2 / np.where(geo_, d1 / np.where(geo_, d2, 1.0) - 1, 1.0), x3)
        out.append(f"{r:2d} {(-1) ** r:+d}  " + "  ".join(f"{v:7.3f}" for v in exv)
                   + "   (continuum B: " + "  ".join(f"{contB[idl, ir]: .3e}" for idl in range(len(deltas))) + ")")
    (OUT / "spinwave_mutual.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
