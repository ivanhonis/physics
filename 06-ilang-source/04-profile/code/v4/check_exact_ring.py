"""Check (ii) of 06-ilang-source/04-profile.

One field object on a ring of L places, two sources at distance d.
Exact mutual cost M = E(g1,g2) - E(g1,0) - E(0,g2) + E(0,0) from
  (a) exact diagonalization of h = C1 + g1 P_x1 + g2 P_x2,
  (b) the pole-cleared eigenvalue equation: F(eps) = delta * [(4.10) LHS - RHS], delta = eps + 2 t_f,
      with the ring Green function (4.11); eps0(g) = smallest zero of F on (-inf, eps1), eps1 = -2t cos(2pi/L)
      (F = det(eps - h) / prod_{k != 0}(eps - eps_k): no pole at eps = -2t, so q = 0 is included;
      F is evaluated in the variable delta, q = 2 arcsin(sqrt(delta/4t)), q = i theta for delta < 0),
  (c) for g1 = g2 the reduced equation (4.12), t sin q sin(qL/2) - g cos(qd/2) cos(q(L-d)/2) = 0,
against the second-order form (4.5) and the third-order term (4.8).
Plus unequal and mixed-sign sources, including roots at q = 0 (delta = 0).
Plus the exact finite-L bracket of (4.8) on the ring (Step 5).
Plus the mean over placements (4.17): Mbar = (1/L) sum_y M(0, y), y = 0..L-1 (y = 0: both sources on
place 0), so that E(0, d) - mean_y E(0, y) = M(d) - Mbar; (4.17) states that Mbar = O(g1^2 g2^2).
Plus the additive continuum scaling (4.21): M L^2 / t_f = F(gamma, u) + O(gamma^2 L^-2), F = Y^2 - 2 y^2 with
Y, y the lowest roots of Y sin(Y/2) = gamma cos(Yu/2) cos(Y(1-u)/2) and y tan(y/2) = gamma/2.
"""
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
LOG = []


def out(s=""):
    print(s)
    LOG.append(s)


t = 1.0


def ring(L):
    return -t * (np.eye(L, k=1) + np.eye(L, k=-1) + np.eye(L, k=L - 1) + np.eye(L, k=-(L - 1)))


def E_exact(C1, sources):
    h = C1.copy()
    for x, g in sources:
        h[x, x] += g
    return eigh(h, eigvals_only=True, subset_by_index=[0, 0])[0]


def ell(d, L):
    """Step 3: Lambda^+(x, x+d) on the ring."""
    return (L * L - 1) / (12 * L) - d * (L - d) / (2 * L)


def qofd(delta):
    """q with delta = eps + 2t = 4 t sin^2(q/2); q = i theta for delta < 0."""
    return 2 * np.arcsin(np.sqrt(complex(delta / (4 * t))))


def F_cleared(delta, g1, g2, d, L):
    """delta * [(1 - g1 G0)(1 - g2 G0) - g1 g2 Gd^2] with the ring Green function (4.11), written as
    delta (1 - (g1+g2) G0) + g1 g2 (G0 - Gd) delta (G0 + Gd); at delta = 0 the limit
    -(g1 + g2)/L - 2 g1 g2 (l0 - ld)/(L t)."""
    if delta == 0.0:
        return -(g1 + g2) / L - 2 * g1 * g2 * (ell(0, L) - ell(d, L)) / (L * t)
    q = qofd(delta)
    den = t * np.sin(q) * np.sin(q * L / 2)
    G0 = np.cos(q * L / 2) / (2 * den)
    Gm = -np.sin(q * (L - d) / 2) * np.sin(q * d / 2) / den       # G0 - Gd
    Gp = np.cos(q * (L - d) / 2) * np.cos(q * d / 2) / den         # G0 + Gd
    return float(np.real(delta * (1 - (g1 + g2) * G0) + g1 * g2 * Gm * (delta * Gp)))


def F412(delta, g, d, L):
    """(4.12) for g1 = g2 = g: t sin q sin(qL/2) - g cos(qd/2) cos(q(L-d)/2);
    one source (d = None): 2 t sin q sin(qL/2) - g cos(qL/2)."""
    q = qofd(delta)
    if d is None:
        return float(np.real(2 * t * np.sin(q) * np.sin(q * L / 2) - g * np.cos(q * L / 2)))
    return float(np.real(t * np.sin(q) * np.sin(q * L / 2) - g * np.cos(q * d / 2) * np.cos(q * (L - d) / 2)))


def smallest_zero(f, L, gneg):
    """eps = -2t + delta for the smallest zero delta of f on (-inf, delta1), delta1 = eps1 + 2t:
    f < 0 below every eigenvalue; scan upward in delta."""
    dmax = 2 * t * (1 - np.cos(2 * np.pi / L))
    neg = -np.geomspace(gneg + 1e-3, 1e-18, 3000)
    pos = np.concatenate([np.geomspace(1e-18, dmax / 2, 3000),
                          dmax - np.geomspace(dmax / 2, dmax * 1e-12, 3000)])
    ds = np.concatenate([neg, [0.0], pos])
    vals = [f(x) for x in ds]
    assert vals[0] < 0
    for a, b, fa, fb in zip(ds[:-1], ds[1:], vals[:-1], vals[1:]):
        if fb == 0.0:
            return -2 * t + b
        if np.sign(fa) != np.sign(fb):
            return -2 * t + brentq(f, a, b, xtol=1e-20, rtol=1e-15)
    raise RuntimeError("no root below eps1")


def eps_cleared(g1, g2, d, L):
    return smallest_zero(lambda x: F_cleared(x, g1, g2, d, L), L, max(0, -g1) + max(0, -g2))


MX = {}                                                    # exact M(L, gamma, d), reused for (4.21)
out("Exact mutual cost on a ring (one field object, t_f = 1), gamma = g L / t_f, w = d(L-d)/L^2")
out("rel2 = (M_exact - M2)/M2,  relx = (M_exact - M2)/M_exact (error relative to the exact value),")
out("pred3 = M3/M2 from (4.8),  rel3 = (M_exact - M2 - M3)/M2,")
out("pred3_L = -(gamma/5)(1-10w+20w^2)/(1-6w) (leading in 1/L); dev10 / dev12 = max deviation of the")
out("smallest zero of the pole-cleared (4.10) / of (4.12) from eigh (one- and two-source energies)")
for L in [64, 256]:
    C1 = ring(L)
    P0 = np.full((L, L), 1.0 / L)                          # projector on the lowest eigenvector of C1
    Lp = np.linalg.inv(C1 + 2 * t * np.eye(L) + t * P0) - P0 / t   # reduced resolvent R = L^+/t_f
    Lp2 = Lp @ Lp
    out(f"-- L = {L}")
    out("   gamma     d     w       M_exact        M2         rel2       relx       pred3      pred3_L     rel3     dev10    dev12")
    for gam in [0.03, 0.1, 0.3, 1.0, 3.0, -0.3, -1.0]:
        g = gam * t / L
        E00 = -2 * t
        E10 = E_exact(C1, [(0, g)])
        c10 = eps_cleared(g, 0.0, 0, L)
        r10 = smallest_zero(lambda x: F412(x, g, None, L), L, max(0, -g))
        for d in [1, L // 8, L // 4, L // 2]:
            E11 = E_exact(C1, [(0, g), (d, g)])
            c11 = eps_cleared(g, g, d, L)
            r11 = smallest_zero(lambda x: F412(x, g, d, L), L, max(0, -2 * g))
            Mx = E11 - 2 * E10 + E00
            w = d * (L - d) / L**2
            M2 = g * g / (t * L * L) * (d * (L - d) - (L * L - 1) / 6)
            l0, ld, q0, qd = Lp[0, 0], Lp[0, d], Lp2[0, 0], Lp2[0, d]   # R and R^2 entries (t_f = 1)
            M3 = g * g * (2 * g) / L * (2 * l0 * ld + ld**2 - (q0 + 2 * qd) / L)
            pL = -(gam / 5) * (1 - 10 * w + 20 * w * w) / (1 - 6 * w)
            dev10 = max(abs(c11 - E11), abs(c10 - E10))
            dev12 = max(abs(r11 - E11), abs(r10 - E10))
            MX[(L, gam, d)] = Mx
            out(f"   {gam:5.2f} {d:5d} {w:6.4f} {Mx: .5e} {M2: .5e} {(Mx-M2)/M2: .3e} {(Mx-M2)/Mx: .3e} {M3/M2: .3e} "
                f"{pL: .3e} {(Mx-M2-M3)/M2: .2e} {dev10:.1e}  {dev12:.1e}")

out("")
out("Unequal and mixed-sign sources (pole-cleared (4.10) against eigh):")
cases = [(64, 8, 0.3 / 64, 0.6 / 64), (64, 8, 1.0 / 64, 2.0 / 64), (64, 8, -1.0 / 64, -2.0 / 64),
         (64, 8, 1.0 / 64, -0.5 / 64), (64, 20, 3.0 / 64, -1.0 / 64), (4, 2, 1.0, -0.5), (4, 1, 1.0, -0.5)]
# a case with the root exactly at q = 0: 1/g1 + 1/g2 = -2 (l0 - ld)/t  (Step 6)
L, d, g1 = 64, 8, 1.0 / 64
cases.append((L, d, g1, 1.0 / (-2 * (ell(0, L) - ell(d, L)) / t - 1 / g1)))
for L, d, g1, g2 in cases:
    C1 = ring(L)
    ex = E_exact(C1, [(0, g1), (d, g2)])
    cl = eps_cleared(g1, g2, d, L)
    F0 = F_cleared(0.0, g1, g2, d, L)
    Mx = ex - E_exact(C1, [(0, g1)]) - E_exact(C1, [(d, g2)]) + (-2 * t)
    M2 = g1 * g2 / (t * L * L) * (d * (L - d) - (L * L - 1) / 6)
    out(f"   L={L:3d} d={d:3d} g1={g1: .5f} g2={g2: .5f}: E_eigh = {ex:.15f}, E_(4.10 cleared) = {cl:.15f}, "
        f"F(q=0) = {F0: .2e}, (M_exact - M2)/M2 = {(Mx-M2)/M2: .3e}")

out("")
out("Exact finite-L bracket of (4.8) on the ring: B_matrix = 2 l0 ld + ld^2 - (l0^(2) + 2 ld^(2))/L against")
out("B_closed = (L^2/60)(1 - 10w + 20w^2) - 1/12 + w/3 + 1/(15 L^2); max_d |B_matrix - B_closed| / max_d |B_closed|")
for L in [3, 4, 5, 16, 64, 256]:
    C1 = ring(L)
    P0 = np.full((L, L), 1.0 / L)
    Lp = np.linalg.inv(C1 + 2 * t * np.eye(L) + t * P0) - P0 / t
    Lp2 = Lp @ Lp
    ds = np.arange(L)
    Bm = 2 * Lp[0, 0] * Lp[0, ds] + Lp[0, ds] ** 2 - (Lp2[0, 0] + 2 * Lp2[0, ds]) / L
    w = ds * (L - ds) / L**2
    Bc = L * L / 60 * (1 - 10 * w + 20 * w * w) - 1 / 12 + w / 3 + 1 / (15 * L * L)
    out(f"   L={L:4d}: {np.max(np.abs(Bm - Bc)) / np.max(np.abs(Bc)):.2e}")

out("")
out("Mean over placements (4.17), g1 = g2 = g, all y = 0..L-1 (y = 0: both sources on one place):")
out("Mbar = (1/L) sum_y M(0,y); inv = E(0,d) - mean_y E(0,y) = M(d) - Mbar (computed from total contracts only);")
out("res = max_d |inv - M2 - M3| / max_d |M2| (M2, M3 from (4.5), (4.8)); (4.17): Mbar has no term of order < g^4")
out("   L    gamma    Mbar*L^2/t_f    Mbar*L^2/(t_f gamma^4)    |Mbar|/max_d|M2|   res")
for L in [64, 256]:
    C1 = ring(L)
    P0 = np.full((L, L), 1.0 / L)
    Lp = np.linalg.inv(C1 + 2 * t * np.eye(L) + t * P0) - P0 / t
    Lp2 = Lp @ Lp
    ds = np.arange(L)
    for gam in [0.1, 0.3, 1.0, -0.3, -1.0]:
        g = gam * t / L
        E00, E10 = -2 * t, E_exact(C1, [(0, g)])
        Ms = np.array([E_exact(C1, [(0, g), (y, g)]) - 2 * E10 + E00 for y in ds])
        Mbar = Ms.mean()
        M2 = g * g / (t * L * L) * (ds * (L - ds) - (L * L - 1) / 6)
        M3 = g * g * (2 * g) / L * (2 * Lp[0, 0] * Lp[0, ds] + Lp[0, ds] ** 2 - (Lp2[0, 0] + 2 * Lp2[0, ds]) / L)
        inv = Ms - Mbar
        res = np.max(np.abs(inv - M2 - M3)) / np.max(np.abs(M2))
        out(f"   {L:3d}  {gam:6.2f}  {Mbar*L*L/t: .4e}   {Mbar*L*L/(t*gam**4): .4e}            "
            f"{abs(Mbar)/np.max(np.abs(M2)):.3e}     {res:.2e}")


def lowest_s(f, gam):
    """Smallest zero s = Y^2 of f on (-(|gamma|+4)^2, 4 pi^2); f < 0 at the lower end (Step 6)."""
    ss = np.linspace(-(abs(gam) + 4) ** 2, 4 * np.pi ** 2, 40001)
    vals = [f(s) for s in ss]
    assert vals[0] < 0
    for a, b, fa, fb in zip(ss[:-1], ss[1:], vals[:-1], vals[1:]):
        if np.sign(fa) != np.sign(fb):
            return brentq(f, a, b, xtol=1e-15, rtol=1e-15)
    raise RuntimeError("no root")


def lim2(s, gam, u):
    Y = np.sqrt(complex(s))
    return float(np.real(Y * np.sin(Y / 2) - gam * np.cos(Y * u / 2) * np.cos(Y * (1 - u) / 2)))


def lim1(s, gam):
    Y = np.sqrt(complex(s))
    return float(np.real(Y * np.sin(Y / 2) - gam / 2 * np.cos(Y / 2)))


out("")
out("Additive continuum scaling (4.21): F(gamma,u) = Y^2 - 2y^2 from the limiting equations; diff = M_exact L^2/t_f - F;")
out("(4.21) states diff = O(gamma^2 L^-2), i.e. diff * L^2 / gamma^2 bounded (its gamma -> 0 value is 1/6, from (4.5))")
out("   gamma     u        F(gamma,u)     L=64: diff     diff*L^2/g^2    L=256: diff    diff*L^2/g^2   |diff|/|F| (L=256)")
for gam in [0.03, 0.1, 0.3, 1.0, 3.0, -0.3, -1.0]:
    sy = lowest_s(lambda s: lim1(s, gam), gam)
    for k in [8, 4, 2]:
        u = 1 / k
        F = lowest_s(lambda s: lim2(s, gam, u), gam) - 2 * sy
        row = []
        for L in [64, 256]:
            diff = MX[(L, gam, L // k)] * L * L / t - F
            row += [diff, diff * L * L / gam ** 2]
        out(f"   {gam:5.2f}  {u:6.4f}  {F: .6e}   {row[0]: .3e}    {row[1]: .4f}       {row[2]: .3e}    {row[3]: .4f}"
            f"        {abs(row[2] / F):.1e}")

(OUT / "exact_ring.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
