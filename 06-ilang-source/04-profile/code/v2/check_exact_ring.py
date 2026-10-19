"""Check (ii) of 06-ilang-source/04-profile.

One field object on a ring of L places, two sources g1 = g2 = g at distance d.
Exact mutual cost M = E(g,g) - E(g,0) - E(0,g) + E(0,0) from
  (a) exact diagonalization of h = C1 + g1 P_x1 + g2 P_x2,
  (b) the closed eigenvalue equations (4.11), (4.12),
against the second-order form (4.5) and the third-order term (4.8).
Plus one case g2 = 2 g1 for the determinant equation (4.11).
Plus the mean over placements (4.17): Mbar = (1/L) sum_y M(0, y), y = 0..L-1 (y = 0: both sources on
place 0), so that E(0, d) - mean_y E(0, y) = M(d) - Mbar; (4.17) states that Mbar = O(g1^2 g2^2).
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


def G(q, d, L):
    """(4.11): Green function of the ring at eps = -2 t cos q (q complex allowed via q = i theta)."""
    return np.cos(q * (L / 2 - d)) / (2 * t * np.sin(q) * np.sin(q * L / 2))


def root(f, L):
    """Lowest eigenvalue: the largest root theta > 0 of f(i theta) (eps0 = -2t cosh theta < -2t) if any,
    else the smallest root q in (0, 2 pi/L) (eps0 = -2t cos q)."""
    fh = lambda th: np.real(f(1j * th))
    ths = np.linspace(1.0, 1e-7, 20001)
    v = [fh(th) for th in ths]
    for a, b, fa, fb in zip(ths[:-1], ths[1:], v[:-1], v[1:]):
        if np.sign(fa) != np.sign(fb):
            th = brentq(fh, b, a, xtol=1e-16, rtol=1e-15)
            return -2 * t * np.cosh(th)
    qs = np.linspace(1e-9, 2 * np.pi / L * (1 - 1e-9), 4001)
    v = [np.real(f(q)) for q in qs]
    for a, b, fa, fb in zip(qs[:-1], qs[1:], v[:-1], v[1:]):
        if np.sign(fa) != np.sign(fb):
            q = brentq(lambda x: np.real(f(x)), a, b, xtol=1e-16, rtol=1e-15)
            return -2 * t * np.cos(q)
    raise RuntimeError("no root")


def E_closed(sources, L):
    if len(sources) == 1:
        g = sources[0][1]
        f = lambda q: np.real(1 - g * G(q, 0, L)) * np.real(np.sin(q) * np.sin(q * L / 2))
        return root(f, L)
    (x1, g1), (x2, g2) = sources
    d = abs(x2 - x1)
    f = lambda q: np.real(((1 - g1 * G(q, 0, L)) * (1 - g2 * G(q, 0, L)) - g1 * g2 * G(q, d, L) ** 2)
                          * (np.sin(q) * np.sin(q * L / 2)) ** 2)
    return root(f, L)


out("Exact mutual cost on a ring (one field object, t_f = 1), gamma = g L / t_f, w = d(L-d)/L^2")
out("rel2 = (M_exact - M2)/M2,  pred3 = M3/M2 from (4.8),  rel3 = (M_exact - M2 - M3)/M2,")
out("pred3_L = -(gamma/5)(1-10w+20w^2)/(1-6w) (leading in 1/L, (4.9)); |closed - eigh| = max deviation of (4.11) roots")
for L in [64, 256]:
    C1 = ring(L)
    P0 = np.full((L, L), 1.0 / L)                          # projector on the lowest eigenvector of C1
    Lp = np.linalg.inv(C1 + 2 * t * np.eye(L) + t * P0) - P0 / t   # reduced resolvent R = L^+/t_f
    Lp2 = Lp @ Lp
    out(f"-- L = {L}")
    out("   gamma     d     w       M_exact        M2         rel2       pred3      pred3_L     rel3     |closed-eigh|")
    for gam in [0.03, 0.1, 0.3, 1.0, 3.0, -0.3, -1.0]:
        g = gam * t / L
        E00 = -2 * t
        E10 = E_exact(C1, [(0, g)])
        c10 = E_closed([(0, g)], L)
        for d in [1, L // 8, L // 4, L // 2]:
            E11 = E_exact(C1, [(0, g), (d, g)])
            c11 = E_closed([(0, g), (d, g)], L)
            Mx = E11 - 2 * E10 + E00
            w = d * (L - d) / L**2
            M2 = g * g / (t * L * L) * (d * (L - d) - (L * L - 1) / 6)
            l0, ld, q0, qd = Lp[0, 0], Lp[0, d], Lp2[0, 0], Lp2[0, d]   # R and R^2 entries (t_f = 1)
            M3 = g * g * (2 * g) / L * (2 * l0 * ld + ld**2 - (q0 + 2 * qd) / L)
            pL = -(gam / 5) * (1 - 10 * w + 20 * w * w) / (1 - 6 * w)
            dev = max(abs(c11 - E11), abs(c10 - E10))
            out(f"   {gam:5.2f} {d:5d} {w:6.4f} {Mx: .5e} {M2: .5e} {(Mx-M2)/M2: .3e} {M3/M2: .3e} {pL: .3e} "
                f"{(Mx-M2-M3)/M2: .2e} {dev:.1e}")

out("")
out("Unequal sources g2 = 2 g1 (determinant equation (4.11)), L = 64, d = 8:")
L, d = 64, 8
C1 = ring(L)
for gam in [0.3, 1.0, -1.0]:
    g1 = gam / L
    g2 = 2 * g1
    ex = E_exact(C1, [(0, g1), (d, g2)])
    cl = E_closed([(0, g1), (d, g2)], L)
    Mx = ex - E_exact(C1, [(0, g1)]) - E_exact(C1, [(d, g2)]) + (-2 * t)
    M2 = g1 * g2 / (t * L * L) * (d * (L - d) - (L * L - 1) / 6)
    out(f"   gamma1 = {gam:5.2f}: E_eigh = {ex:.15f}, E_(4.11) = {cl:.15f}, (M_exact - M2)/M2 = {(Mx-M2)/M2: .3e}")

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

(OUT / "exact_ring.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
