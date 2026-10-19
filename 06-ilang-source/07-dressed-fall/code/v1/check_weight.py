"""Check of item 1 of 06-ilang-source/07-dressed-fall, derivation v1.

N_f = 1 field object on rings of L = 8 and L = 13 places, t_f = 1, source at x_s = 0.
Held body: point term g_b = sigma*gamma*M_k at x; source: point term g_s at x_s.
Exact: W(x) - W(x_s) = eps0(x) - eps0(x_s), eps0 the lowest eigenvalue of
C_1 + g_b|x><x| + g_s|x_s><x_s| (7.1), (7.2). Compared with the operator form (7.3), the ring
form (7.5) and the first-order term (4.4) alone; the deviation is split into its parts
odd and even in g_s, whose scaling in gamma and g_s is fitted. Also checks the slope
factor of (7.8), (7.9): [W'/W'_lead - 1]/g_b -> -((L-2 r0)^2 + 2)/(6 L t_f).
"""
from pathlib import Path

import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
T_F, XS = 1.0, 0
LINES = []


def log(s=""):
    LINES.append(s)


def hop(L):
    c = np.zeros((L, L))
    for x in range(L):
        c[x, (x + 1) % L] = c[(x + 1) % L, x] = -T_F
    return c


def w_exact(L, gb, gs):
    c1 = hop(L)
    e = []
    for x in range(L):
        h = c1.copy()
        h[x, x] += gb
        h[XS, XS] += gs
        e.append(np.linalg.eigvalsh(h)[0])
    e = np.array(e)
    return e - e[XS]


def green(L):
    lap = 2 * np.eye(L) + hop(L) / T_F
    return np.linalg.pinv(lap)


def w_operator(L, gb, gs, order2=True):
    n, G = 1.0 / L, green(L)
    G2 = G @ G
    x = np.arange(L)
    gr = G[x, XS]
    w = -2 * n * gs * gb / T_F * gr
    if order2:
        w = w + n * gs * gb**2 / T_F**2 * (2 * G[x, x] * gr + gr**2 - 2.0 / L * G2[x, XS])
    return w - w[XS]


def u_of(L):
    r = (np.arange(L) - XS) % L
    return r * (L - r)


def w_ring(L, gb, gs):
    n, u = 1.0 / L, u_of(L)
    return n * gs * gb / (L * T_F) * ((1 - (L**2 - 2) * gb / (6 * L * T_F)) * u + gb / (3 * L * T_F) * u**2)


def dev(L, gb, gs, f):
    return np.max(np.abs(w_exact(L, gb, gs) - f(L, gb, gs)))


def dev_parts(L, gb, gs):
    dp = w_exact(L, gb, gs) - w_ring(L, gb, gs)
    dm = w_exact(L, gb, -gs) - w_ring(L, gb, -gs)
    return np.max(np.abs(dp - dm)) / 2, np.max(np.abs(dp + dm)) / 2


def slope(xs, ys):
    return np.polyfit(np.log(xs), np.log(ys), 1)[0]


for L in (8, 13):
    om = 4 * np.sin(np.pi / L) ** 2
    log(f"=== L = {L}, N_f = 1, t_f = 1, x_s = 0, omega_min = {om:.6f} (gap t_f*omega_min) ===")
    G = green(L)
    u = u_of(L)
    G0 = (L**2 - 1) / (12 * L)
    e1 = np.max(np.abs(G[np.arange(L), XS] - (G0 - u / (2 * L))))
    G2 = (G @ G)[np.arange(L), XS]
    p = G2 - (-u / (12 * L) - u**2 / (24 * L))
    e2 = np.max(np.abs(p - p[0]))
    e3 = max(np.max(np.abs(w_operator(L, g, 1e-3) - w_ring(L, g, 1e-3))) for g in (0.03, -0.03))
    log(f"closed forms (7.4): max|G_r - (G_0 - u/2L)| = {e1:.1e}; (G^2)_r - (-u/12L - u^2/24L) const to {e2:.1e};"
        f" max|(7.3) - (7.5)| = {e3:.1e}")

    log("grid: max_x |W_exact - W_(7.5)| and relative to max_x |W_exact|, two levels, both branches")
    log("  M_k  sigma  gamma    g_s      g_b/gap    dev          rel.dev     dev of (4.4) alone")
    for M in (1.0, 2.5):
        for sg in (+1, -1):
            for gam in (0.002, 0.01):
                for gs in (0.001, 0.004):
                    gb = sg * gam * M
                    we = w_exact(L, gb, gs)
                    d = dev(L, gb, gs, w_ring)
                    d1 = dev(L, gb, gs, lambda L_, a, b: w_operator(L_, a, b, False))
                    log(f"  {M:3.1f}  {sg:+d}    {gam:6.3f}  {gs:6.3f}  {gb / om:+8.4f}  {d:10.3e}  "
                        f"{d / np.max(np.abs(we)):10.3e}  {d1:10.3e}")

    gs = 0.002 * om
    gbs = om * np.array([0.02, 0.04, 0.08, 0.16])
    odd = [dev_parts(L, g, gs)[0] for g in gbs]
    first = []
    for g in gbs:
        dp = w_exact(L, g, gs) - w_operator(L, g, gs, False)
        dm = w_exact(L, g, -gs) - w_operator(L, g, -gs, False)
        first.append(np.max(np.abs(dp - dm)) / 2)
    log(f"gamma scaling at g_s = 0.002 gap, g_b/gap = {[float(round(v, 3)) for v in gbs / om]}:")
    log(f"  g_s-odd deviation of (7.5): {['%.3e' % v for v in odd]}, slope in g_b = {slope(gbs, odd):.3f}"
        " (expected 3)")
    log(f"  g_s-odd deviation of (4.4) alone: {['%.3e' % v for v in first]}, slope in g_b = "
        f"{slope(gbs, first):.3f} (expected 2)")
    gb = 0.05 * om
    gss = om * np.array([0.002, 0.004, 0.008, 0.016])
    even = [dev_parts(L, gb, g)[1] for g in gss]
    log(f"g_s scaling at g_b = 0.05 gap, g_s/gap = {[float(round(v, 3)) for v in gss / om]}:")
    log(f"  g_s-even deviation of (7.5): {['%.3e' % v for v in even]}, slope in g_s = {slope(gss, even):.3f}"
        " (expected 2)")

    log("slope factor of (7.8), (7.9): [W'(x0)/W'_lead(x0) - 1]/g_b, odd part in g_s and in g_b (both branches), Richardson in g_b")
    gs, g = 2e-3 * om, 0.01 * om
    for r0 in range(1, L):
        if 2 * r0 == L:
            continue
        x0 = (XS + r0) % L

        def ratio(gb):
            wo = (w_exact(L, gb, gs) - w_exact(L, gb, -gs)) / 2
            wp = 0.5 * (wo[(x0 + 1) % L] - wo[(x0 - 1) % L])
            return wp / ((1.0 / L) * gs * gb * (L - 2 * r0) / (L * T_F))
        c1 = (ratio(g) - ratio(-g)) / (2 * g)
        c2 = (ratio(g / 2) - ratio(-g / 2)) / g
        c = (4 * c2 - c1) / 3  # Richardson step in g_b
        pred = -((L - 2 * r0) ** 2 + 2) / (6 * L * T_F)
        log(f"  r0 = {r0:2d}: numeric {c:+.6f}, predicted {pred:+.6f}, diff {c - pred:+.1e}")
    log()

(OUT / "check_weight.txt").write_text("\n".join(LINES) + "\n", encoding="utf-8")
print("\n".join(LINES))
