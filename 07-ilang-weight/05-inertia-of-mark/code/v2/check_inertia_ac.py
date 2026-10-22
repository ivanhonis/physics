"""Check of 05-inertia-of-mark (v2): couplings (a) and (c), N_f = 1.

1. (5.9): tau^2 D_{k,sigma} = tau^2 mu - tau^2 Cost/v^2 from the exact tau^2 coefficient J of (5.2)
   (exact in gamma) against the order-gamma^2 formula, and the exact curvature at small tau against 2 tau^2 J.
2. (5.12): one-speed criterion at order gamma^2. For (c), the branch average and its positive coefficient.
   For (a), the double points of the chord curve x -> (s(x), i(x)) for 5 <= L <= 16 (exhaustive search in
   symmetric functions) and parameters shared by two of them; an exact check at one double point (residual of the line through the four points of
   two levels scales as gamma^3 there, as gamma^2 at a generic pair).
Output: output/check_inertia_ac.txt
"""
from pathlib import Path
import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
lines = []
def log(s=""):
    lines.append(s)
sx = np.array([[0, 1], [1, 0]], complex)
sz = np.diag([1.0, -1.0]).astype(complex)


def ring(L, tf):
    Tp = np.roll(np.eye(L), 1, axis=0)
    return Tp, Tp.T, -tf * (Tp + Tp.T)


def proj(L, r):
    P = np.zeros((L, L)); P[r % L, r % L] = 1.0
    return P


def ground(L, tf, g):
    _, _, c1 = ring(L, tf)
    w, V = np.linalg.eigh(c1 + g * proj(L, 0))
    return w[0], V[:, 0] * np.sign(V[0, 0])


def Kop(L, gam, coup):
    _, Tm, _ = ring(L, 1.0)
    return Tm if coup == "a" else Tm @ (np.eye(L) + 0.5 * gam * (proj(L, 0) + proj(L, 1)))


def J52(L, tf, M, gam, sig, coup):
    """(5.2): J = <Omega_s| K (E0_s - C0_{-s})^{-1} K |Omega_s>, theta = 1."""
    _, _, c1 = ring(L, tf)
    e, phi = ground(L, tf, sig * gam * M)
    E0 = sig * M + e
    Cm = -sig * M * np.eye(L) + c1 - sig * gam * M * proj(L, 0)
    K = Kop(L, gam, coup)
    return phi @ K @ np.linalg.solve(E0 * np.eye(L) - Cm, K @ phi)


def exact_curv(L, tf, M, gam, tau, sig, coup):
    _, _, c1 = ring(L, tf)
    C0 = M * np.kron(sz, np.eye(L)) + np.kron(np.eye(2), c1) + gam * M * np.kron(sz, proj(L, 0))
    Cp = 0.5 * tau * np.kron(-1j * sx, Kop(L, gam, coup))
    C = C0 + Cp + Cp.conj().T
    d1 = -1j * Cp + 1j * Cp.conj().T
    d2 = -(Cp + Cp.conj().T)
    w, V = np.linalg.eigh(C)
    ref = np.kron(np.eye(2)[:, 0 if sig > 0 else 1], ground(L, tf, sig * gam * M)[1])
    i = np.argmax(abs(V.conj().T @ ref)); psi = V[:, i]
    a = V.conj().T @ (d1 @ psi); m = np.arange(len(w)) != i
    return np.real(psi.conj() @ d2 @ psi) + 2 * np.sum(abs(a[m]) ** 2 / (w[i] - w[m]))


def tau2D_exact(L, tf, M, gam, sig, coup):
    e0 = ground(L, tf, 0.0)[0]
    cost = sig * M + ground(L, tf, sig * gam * M)[0] - e0
    v2 = (1 + gam / L) ** 2 if coup == "c" else 1.0          # v^2 / tau^2, (5.7)
    return 1.0 / (2 * J52(L, tf, M, gam, sig, coup)) - cost / v2


def Fsc(y, L, coup):
    """(5.12): tau^2 D = n gamma^2 t_f F(sigma M_k / t_f) + O(gamma^3)."""
    q = 2 * np.pi * np.arange(1, L) / L; c = np.cos(q)
    if coup == "a":
        br = (1 + (1 + c) * y * (y - 1) / (y - 1 + c)) / (1 - c)
    else:
        br = (1 + c + c * c + y * (1 + c)) / (1 - c)
    return 0.5 * y * y * np.sum(br) / L


# ---- 1. (5.9) against the exact tau^2 coefficient, and 2 tau^2 J against the exact curvature
log("1. (5.9): tau^2 D from the exact tau^2 coefficient J of (5.2) vs the order-gamma^2 formula; t_f = 1, N_f = 1")
log("   coup L  M_k  gamma sig   tau^2 D exact    (5.9)          (exact-(5.9))/gamma^3   |E''(tau=1e-4)/(2tau^2 J)-1|")
tf = 1.0
for coup in ("a", "c"):
    for L in (7, 13):
        for M in (1.0, 1.4):
            for gam in (0.01, 0.02):
                for sig in (1, -1):
                    ex = tau2D_exact(L, tf, M, gam, sig, coup)
                    pr = (gam ** 2 / L) * tf * Fsc(sig * M / tf, L, coup)
                    tau = 1e-4
                    E2 = exact_curv(L, tf, M, gam, tau, sig, coup)
                    log("   %s   %2d %.1f  %.2f  %+d   %+.6e   %+.6e   %+.4f            %.1e"
                        % (coup, L, M, gam, sig, ex, pr, (ex - pr) / gam ** 3,
                           abs(E2 / (2 * tau ** 2 * J52(L, tf, M, gam, sig, coup)) - 1)))
log()

# ---- 2. (5.12): branch average of (c)
log("2. (c): branch average (F_c(y)+F_c(-y))/2 = alpha_L y^2, alpha_L = <(1+c+c^2)/(1-c)>_q / 2 > 0:")
log("   " + ", ".join("L=%d: %.4f" % (L, 0.5 * np.sum((1 + np.cos(q) + np.cos(q) ** 2) / (1 - np.cos(q))) / L)
                      for L in range(5, 17) for q in [2 * np.pi * np.arange(1, L) / L]))
log()

# ---- 3. (5.12): double points of the chord curve of (a)
log("3. (a): double points (x0 < x1) of x -> (s(x), i(x)), s = [F_a(x)-F_a(-x)]/(2x), i = [F_a(x)+F_a(-x)]/2,")
log("   x = M_k/t_f. With u = x^2, s and i are rational with simple poles at u = P_m = (1 - c_m)^2, and a double")
log("   point solves E_s = beta + sum_m w_m P_m/(2 l_m) = 0, E_i = alpha + sum_m w_m p_m P_m/(2 l_m) = 0 with")
log("   l_m = s2 - P_m s1 + P_m^2 linear in (s1, s2) = (u0 + u1, u0 u1). For each s1 on a grid all roots s2 of")
log("   E_s (a polynomial of degree = number of poles) are found; sign changes of E_i along root branches are")
log("   refined by bisection. Hits on pairs of poles (spurious) are discarded. Two grids show stability.")


def chord(x, L):
    return np.array([(Fsc(x, L, "a") - Fsc(-x, L, "a")) / (2 * x), 0.5 * (Fsc(x, L, "a") + Fsc(-x, L, "a"))])


def pole_data(L):
    c = np.cos(2 * np.pi * np.arange(1, L) / L)
    al = 0.5 * np.sum((1 - c - c * c) / (1 - c)) / L
    be = 0.5 * np.sum((1 + c) / (1 - c)) / L
    keep = np.abs(c * (1 + c)) > 1e-12
    cu, cnt = np.unique(np.round(c[keep], 12), return_counts=True)
    return al, be, 1 - cu, cnt * cu * (1 + cu) / L     # F_a(y) = al y^2 + be y^3 - (y^2/2) sum w/(y - p)


def double_points(L, ngrid, s1max):
    al, be, p, w = pole_data(L)
    P = p * p; a = w * P; b = w * p * P; Mp = len(P)
    S1 = np.geomspace(1e-5, s1max, ngrid)
    kap = P[None, :] ** 2 - P[None, :] * S1[:, None]

    def mul(poly, k):
        new = np.zeros((poly.shape[0], poly.shape[1] + 1))
        new[:, :-1] += k[:, None] * poly; new[:, 1:] += poly
        return new
    full = np.ones((ngrid, 1))
    for m in range(Mp):
        full = mul(full, kap[:, m])
    poly = be * full
    for m in range(Mp):
        part = np.ones((ngrid, 1))
        for mm in range(Mp):
            if mm != m:
                part = mul(part, kap[:, mm])
        poly[:, :-1] += 0.5 * a[m] * part
    comp = np.zeros((ngrid, Mp, Mp)); comp[:, 1:, :-1] = np.eye(Mp - 1); comp[:, :, -1] = -poly[:, :-1] / poly[:, -1:]
    rts = np.linalg.eigvals(comp)
    r = np.where(abs(rts.imag) < 1e-9 * (1 + abs(rts.real)), rts.real, np.nan)
    r = np.sort(np.where((r > 0) & (S1[:, None] ** 2 - 4 * r > 0), r, np.nan), axis=1)
    with np.errstate(all="ignore"):
        Ei = al + 0.5 * np.sum(b / (r[:, :, None] - P * S1[:, None, None] + P ** 2), axis=2)
    d = np.abs(r[:-1, :, None] - r[1:, None, :]); d = np.where(np.isnan(d), np.inf, d)
    k = np.argmin(d, axis=2); dmin = np.take_along_axis(d, k[:, :, None], 2)[:, :, 0]
    flip = (dmin < 0.05 * (1 + np.abs(r[:-1]))) & (np.sign(np.take_along_axis(Ei[1:], k, 1)) != np.sign(Ei[:-1]))

    def g(s1, s2ref):
        kp = P ** 2 - P * s1
        pl = be * np.poly(-kp)
        for m in range(Mp):
            pl = pl + np.r_[0, 0.5 * a[m] * np.poly(-np.delete(kp, m))]
        rr = np.roots(pl); rr = rr[abs(rr.imag) < 1e-7 * (1 + abs(rr.real))].real
        s2 = rr[np.argmin(abs(rr - s2ref))]
        return al + 0.5 * np.sum(b / (s2 - P * s1 + P * P)), s2
    sols = []
    for i, j in np.argwhere(flip):
        lo, hi, s2lo = S1[i], S1[i + 1], r[i, j]
        glo, _ = g(lo, s2lo)
        for _ in range(80):
            mid = 0.5 * (lo + hi); gm, s2m = g(mid, s2lo)
            if np.sign(gm) == np.sign(glo):
                lo, glo, s2lo = mid, gm, s2m
            else:
                hi = mid
        s1 = 0.5 * (lo + hi); _, s2 = g(s1, s2lo); disc = s1 * s1 - 4 * s2
        if disc <= 0 or s2 <= 0:
            continue
        x0, x1 = np.sqrt((s1 - np.sqrt(disc)) / 2), np.sqrt((s1 + np.sqrt(disc)) / 2)
        if min(abs(np.r_[x0 - p, x1 - p])) < 1e-7 or x1 - x0 < 1e-6:
            continue                                     # spurious: both parameters on poles
        rel = np.max(abs(chord(x0, L) - chord(x1, L))) / max(1.0, np.max(abs(chord(x0, L))))
        if rel < 1e-6 and all(abs(x0 - s[0]) + abs(x1 - s[1]) > 1e-6 for s in sols):
            sols.append((x0, x1))
    return sorted(sols), p


all_dp = {}
for L in range(5, 17):
    sa, _ = double_points(L, 200000, 100.0)
    sols, poles = double_points(L, 600000, 1000.0)
    all_dp[L] = sols
    straddle = all(np.any((poles > s[0]) & (poles < s[1])) for s in sols)
    xs = [x for s in sols for x in s]
    shared = sum(1 for i in range(len(xs)) for j in range(i + 1, len(xs)) if abs(xs[i] - xs[j]) < 1e-6)
    log("   L=%2d: %2d double points (coarser grid: %2d); each has a resonance 1-cos q between x0 and x1: %s;"
        " parameters shared by two double points (needed for N >= 3): %d" % (L, len(sols), len(sa), straddle, shared))
    log("         " + "; ".join("(%.5f, %.5f)" % s for s in sols))
log()

# ---- 4. exact check at a double point of L = 7 against a generic pair
log("4. (a), L = 7, N_f = 1, t_f = 1: residual of the least-squares line through the four points")
log("   (sigma M_k, tau^2 D_{k,sigma}) (exact tau^2 coefficient), divided by gamma^2:")
L = 7
for label, (x0, x1) in (("double point", all_dp[7][0]), ("generic pair", (1.0, 1.4))):
    out = []
    for gam in (0.002, 0.004, 0.008):
        ys, ds = [], []
        for M in (x0, x1):
            for sig in (1, -1):
                ys.append(sig * M); ds.append(tau2D_exact(L, 1.0, M, gam, sig, "a"))
        A = np.vstack([np.ones(4), ys]).T
        res = ds - A @ np.linalg.lstsq(A, ds, rcond=None)[0]
        out.append("gamma=%.3f: %.3e" % (gam, np.max(abs(res)) / gam ** 2))
    log("   %s (M_0, M_1) = (%.6f, %.6f): " % (label, x0, x1) + ", ".join(out))

(OUT / "check_inertia_ac.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
