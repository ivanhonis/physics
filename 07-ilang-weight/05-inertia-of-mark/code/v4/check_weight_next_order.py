"""Check of 05-inertia-of-mark (v4): weight over inertia, place pairs with F = 0 or Xi = 0, N_f = 1 unless stated.

1. F = 0 exactly for reflection-equivalent pairs (r' = -r mod L); list of pairs with Xi = 0 for 5 <= L <= 16;
   at the Xi = 0 pairs, Psi_0 against its closed form -(L^2-1)(2L^2+7)/(360 L^2 t_f^2), and K_L > 0
   (the closed form also for even L up to 40).
2. (5.15) at L = 8, (r, r') = (3, 4) (Xi = 0): E''(0) Delta W / (tau^2 F Lambda) - 1 from the exact tau^2
   coefficient (E'' = 2 tau^2 J of (5.2), exact in gamma) and the exact first-order held weight, against the
   order-gamma^2 prediction, for the full grip, (a) and (c); for (a) also the closed form gamma^2 G(sigma M_k/t_f).
3. (a) at Xi = 0, even 6 <= L <= 16: cancellation conditions of the complete gamma^2 coefficient G:
   (i) phi(M_k^2/t_f^2) = 0 at every level, (ii) equal branch-even part at every level. Zeros of phi
   (polynomial roots, cross-checked by a sign-change count), the N_f that (ii) requires for each pair of zeros,
   and equally spaced triples of sqrt(zeros).
Output: output/check_weight_next_order.txt
"""
from pathlib import Path
import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
lines = []


def log(s=""):
    lines.append(s)


tf, gs = 1.0, 1.0


def ring(L):
    Tp = np.roll(np.eye(L), 1, axis=0)
    return Tp, Tp.T, -tf * (Tp + Tp.T)


def proj(L, r):
    P = np.zeros((L, L)); P[r % L, r % L] = 1.0
    return P


def sums(L):
    Tp, Tm, _ = ring(L)
    ell = np.linalg.pinv(2 * np.eye(L) - Tp - Tm)
    q = 2 * np.pi * np.arange(1, L) / L; eps = 2 * tf * (1 - np.cos(q))
    return (ell[:, 0], (ell @ ell)[:, 0], (ell @ ell @ ell)[:, 0], np.sum(1 / eps) / L, np.sum(1 / eps ** 2) / L,
            np.sum((1 + np.cos(q)) / eps ** 2) / L)


def coeffs(L, r, rp):
    n = 1.0 / L
    l1, l2, l3, s1, s2, S2 = sums(L)
    br = lambda f: f[r] - f[rp]
    F = -2 * gs * br(l1) / tf
    if abs(F) < 1e-13:
        return F, None, None, None
    F2 = gs / (n * tf ** 2) * br(l1 ** 2 - 2 * l2 / L)
    F3 = 2 * gs / (n ** 2 * tf ** 3 * L) * br(l1 * l2 + l2[0] * l1 - l3 / L)
    Xi = n * F2 / F - s1
    Psi0 = s1 ** 2 - s2 / L - 2 * s1 * n * F2 / F + n ** 2 * F3 / F
    KL = 2 * n * S2 + s1 ** 2 - s2 / L
    return F, Xi, Psi0, KL


log("1. F = 0 iff r' = r or r' = L - r (reflection-equivalent); Xi of (5.10) against the closed form")
log("   Xi = -(rho^2 + rho'^2 - 1)/(3 L t_f), rho = r - L/2; pairs 0 <= r < r' < L with F != 0 and Xi = 0;")
log("   at those pairs Psi_0 - K_L of (5.15) (full grip, N_f = 1), and max|Psi_0 - closed form| (v4),")
log("   closed form Psi_0 = -(L^2-1)(2L^2+7)/(360 L^2 t_f^2); K_L = 2 n S_2 + s_3 with S_2 > 0 and s_3 > 0.")


def psi0_closed(L):
    return -(L ** 2 - 1) * (2 * L ** 2 + 7) / (360 * L ** 2 * tf ** 2)


for L in range(5, 17):
    zeroF = [(r, rp) for r in range(L) for rp in range(r + 1, L) if abs(coeffs(L, r, rp)[0]) < 1e-13]
    refl = all((rp == L - r) for r, rp in zeroF) and len(zeroF) == (L - 1) // 2
    dev = max(abs(coeffs(L, r, rp)[1] + ((r - L / 2) ** 2 + (rp - L / 2) ** 2 - 1) / (3 * L * tf))
              for r in range(L) for rp in range(r + 1, L) if coeffs(L, r, rp)[1] is not None)
    xi0 = [(r, rp) for r in range(L) for rp in range(r + 1, L)
           if coeffs(L, r, rp)[1] is not None and abs(coeffs(L, r, rp)[1]) < 1e-12]
    extra = ""
    if xi0:
        _, _, P0, K0 = coeffs(L, *xi0[0])
        dpsi = max(abs(coeffs(L, *pr)[2] - psi0_closed(L)) for pr in xi0)
        _, _, _, s1_, s2_, S2_ = sums(L)
        extra = ("; Psi_0 - K_L = %.5f/t_f^2; max|Psi_0 - closed form| = %.1e; S_2 = %.4f, s_3 = %.4f"
                 % (P0 - K0, dpsi, S2_, s1_ ** 2 - s2_ / L))
    log("   L=%2d: F = 0 exactly on the %d reflection-equivalent pairs: %s; max|Xi - closed form| = %.1e;"
        " Xi = 0 on: %s%s" % (L, len(zeroF), refl, dev, xi0, extra))
log("   closed form of Psi_0 at the pairs (L/2 - 1, L/2), (L/2, L/2 + 1), even 18 <= L <= 40:")
worst = 0.0
for L in range(18, 41, 2):
    for pr in ((L // 2 - 1, L // 2), (L // 2, L // 2 + 1)):
        F_, Xi_, P0_, K0_ = coeffs(L, *pr)
        worst = max(worst, abs(P0_ - psi0_closed(L)) / abs(psi0_closed(L)), abs(Xi_) * L)
log("   max relative |Psi_0 - closed form| and max L|Xi| over these pairs: %.1e" % worst)
log()


def ground(L, g):
    _, _, c1 = ring(L)
    w, V = np.linalg.eigh(c1 + g * proj(L, 0))
    return w[0], V[:, 0] * np.sign(V[0, 0])


def J52(L, M, gam, sig, coup):
    Tp, Tm, c1 = ring(L)
    th = 0.0 if coup == "fg" else 1.0
    e, phi = ground(L, sig * gam * M)
    K = Tm if coup != "c" else Tm @ (np.eye(L) + 0.5 * gam * (proj(L, 0) + proj(L, 1)))
    Cm = -th * sig * M * np.eye(L) + c1 - sig * gam * M * proj(L, 0)
    return phi @ K @ np.linalg.solve((th * sig * M + e) * np.eye(L) - Cm, K @ phi), phi


def Dsc(L, M, gam, sig, coup):
    """(5.9): tau^2 D at order gamma^2."""
    q = 2 * np.pi * np.arange(1, L) / L; c = np.cos(q); eps = 2 * tf * (1 - c)
    if coup == "a":
        br = (tf + 2 * M * (1 + c) * (M - sig * tf) / (2 * sig * M - eps)) / (1 - c)
    else:
        br = (tf * (1 + c + c * c) + sig * M * (1 + c)) / (1 - c)
    return gam ** 2 * M ** 2 / (2 * tf ** 2) * np.sum(br) / L / L


L, r, rp = 8, 3, 4
n = 1.0 / L
F, Xi, Psi0, KL = coeffs(L, r, rp)
s1 = sums(L)[3]
log("2. (5.15) at L = 8, (r, r') = (3, 4): F = %.6f, Xi = %.1e, Psi_0 = %.6f, K_L = %.6f, Psi_0 - K_L = %.6f"
    % (F, Xi, Psi0, KL, Psi0 - KL))
log("   coup  M_k  gamma  sig   exact ratio-1     prediction      (exact-pred)/gamma^3   branch-odd part: exact, pred")
for coup, Ms in (("fg", (1.0, 1.4)), ("a", (1.2, 1.6)), ("c", (1.2, 1.6))):
    for M in Ms:
        for gam in (0.01, 0.02):
            g = gam * M
            vals = {}
            for sig in (1, -1):
                J, phi = J52(L, M, gam, sig, coup)
                dW = gs * (phi[r] ** 2 - phi[rp] ** 2)
                Lam = 1.0 if coup == "fg" else (n * gam / (1 + gam * n) if coup == "a" else n * gam * (1 + gam * n))
                ex = 2 * J * dW / (F * Lam) - 1
                if coup == "fg":
                    pr = (Psi0 - KL) * g * g
                else:
                    pr = Psi0 * g * g - sig * (Dsc(L, M, gam, sig, coup) - n * s1 * g * g) / M
                vals[sig] = (ex, pr)
            odd_ex = 0.5 * (vals[1][0] - vals[-1][0]); odd_pr = 0.5 * (vals[1][1] - vals[-1][1])
            for sig in (1, -1):
                ex, pr = vals[sig]
                log("   %-3s  %.1f  %.2f   %+d   %+.6e   %+.6e   %+.4f              %+.4e %+.4e"
                    % (coup, M, gam, sig, ex, pr, (ex - pr) / gam ** 3, odd_ex, odd_pr))
log("   (c): predicted branch-odd part -sigma gamma^2 M_k n (L-2)(L-4)/(6 L t_f) at gamma = 0.02, M = 1.2: %+.4e"
    % (-(0.02 ** 2) * 1.2 * n * (L - 2) * (L - 4) / (6 * L * tf)))


def avg(L, f):
    q = 2 * np.pi * np.arange(1, L) / L
    return np.sum(f(np.cos(q))) / L


def G_closed(L, nn, y):
    """(a) at Xi = 0: complete gamma^2 coefficient of (5.15), y = sigma M_k / t_f (v4)."""
    return psi0_closed(L) * tf ** 2 * y * y - 0.5 * nn * y * y * (y - 1) * avg(L, lambda c: (1 + c) / ((1 - c) * (y - 1 + c)))


dev = 0.0
for M in (1.2, 1.6):
    for gam in (0.01, 0.02):
        for sig in (1, -1):
            pr = Psi0 * (gam * M) ** 2 - sig * (Dsc(L, M, gam, sig, "a") - n * s1 * (gam * M) ** 2) / M
            dev = max(dev, abs(gam ** 2 * G_closed(L, n, sig * M / tf) - pr) / abs(pr))
log("   (a): closed form gamma^2 G(sigma M_k/t_f) against the prediction column: max relative deviation %.1e" % dev)
log()

log("3. (a) at Xi = 0 (even L): G(y) = y^2 [Psi_0 t_f^2 - n A_L + (n/2) psi(y^2)] + (n/2) y^3 phi(y^2), y = sigma M_k/t_f,")
log("   A_L = (L-1)(L-2)/(6L), phi(u) = <c(1+c)/((1-c)(u-(1-c)^2))>_q, psi(u) = <c(1+c)/(u-(1-c)^2)>_q, c = cos q.")
log("   Common to all levels and branches iff (i) phi(x_k^2) = 0 for every level, x_k = M_k/t_f, and (ii) the branch-even")
log("   part is equal at every level; (ii) for two zeros u_a, u_b of phi fixes n = N_f/L uniquely.")


def phipsi(L):
    j = np.arange(1, L // 2)
    c = np.cos(2 * np.pi * j / L)
    keep = np.abs(c * (1 + c)) > 1e-12
    c = c[keep]
    W = 2 * c * (1 + c) / ((1 - c) * L)
    return c, W, (1 - c) ** 2


ident = 0.0
for L in range(6, 17, 2):
    c, W, p = phipsi(L)
    for y in (0.37, -0.81, 1.9, -2.6):
        nn = 3.0 / L
        u = y * y
        ph = np.sum(W / (u - p)); ps = np.sum(W * (1 - c) / (u - p))
        A = (L - 1) * (L - 2) / (6 * L)
        alt = y * y * (psi0_closed(L) * tf ** 2 - nn * A + 0.5 * nn * ps) + 0.5 * nn * y ** 3 * ph
        ident = max(ident, abs(alt - G_closed(L, nn, y)) / abs(G_closed(L, nn, y)))
log("   identity of the even/odd split against G (L = 6..16 even, four y, N_f = 3): max relative deviation %.1e" % ident)
summ = []
for L in range(6, 41, 2):
    c, W, p = phipsi(L)
    order = np.argsort(p); c, W, p = c[order], W[order], p[order]
    P = np.zeros(len(p))
    for i in range(len(p)):
        P = P + W[i] * np.poly(np.delete(p, i))
    rts = np.roots(P)
    Z = np.sort(np.array([z.real for z in rts if abs(z.imag) < 1e-9 and z.real > 0]))
    for _ in range(8):                                      # Newton polish of the roots on phi itself
        Z = Z - np.array([np.sum(W / (z - p)) / -np.sum(W / (z - p) ** 2) for z in Z]).reshape(Z.shape)
    # cross-check: sign changes of phi on each interval between consecutive poles, and above the largest pole
    edges = np.concatenate(([0.0], p, [1e4]))
    nsc = 0
    for a, b in zip(edges[:-1], edges[1:]):
        uu = (np.geomspace(a + 1e-9, b, 400001) if b > 10 else a + (b - a) * np.linspace(1e-7, 1 - 1e-7, 400001))
        f = np.array([np.sum(W / (x - p)) for x in uu[:: 100]]) if False else (W[None, :] / (uu[:, None] - p[None, :])).sum(1)
        nsc += int(np.sum(np.sign(f[1:]) != np.sign(f[:-1])))
    res = max([abs(np.sum(W / (z - p))) * z for z in Z], default=0.0)
    A = (L - 1) * (L - 2) / (6 * L)
    ps = lambda u: np.sum(W * (1 - c) / (u - p))
    Nf_req = []
    for ia in range(len(Z)):
        for ib in range(ia + 1, len(Z)):
            ua, ub = Z[ia], Z[ib]
            den = A * (ua - ub) - 0.5 * (ua * ps(ua) - ub * ps(ub))
            Nf_req.append(L * psi0_closed(L) * tf ** 2 * (ua - ub) / den)
    pos = [x for x in Nf_req if x > 0]
    dist = min([abs(x - round(x)) for x in pos if round(x) >= 1], default=float("nan"))
    xs = np.sqrt(Z)
    tri = sum(1 for a in range(len(xs)) for b in range(a + 1, len(xs)) for d in range(b + 1, len(xs))
              if abs((xs[b] - xs[a]) - (xs[d] - xs[b])) < 1e-9)
    reso = [z for z in Z if min(abs(z - 1), abs(z - 4)) < 1e-9]
    # proof ingredients: at zeros of phi, psi(u) = -<w/(sqrt(u) + 1 - c)>; kappa'(u) = -(1/4)<w (x+2a)/(x+a)^2> < A_L
    om = lambda x: np.sum(W / (x + 1 - c))
    dpsi = max([abs(ps(z) + om(np.sqrt(z))) for z in Z], default=0.0)
    xg = np.geomspace(1e-4, 1e3, 20001)
    a_ = 1 - c
    kprime = -0.25 * (W[None, :] * (xg[:, None] + 2 * a_[None, :]) / (xg[:, None] + a_[None, :]) ** 2).sum(1)
    summ.append((L, len(Z), nsc, len(Nf_req), len(pos), max(Nf_req, default=float("nan")), tri, len(reso), dpsi,
                 np.max(kprime) - A, A))
    if L > 16:
        continue
    log("   L=%2d: %d poles; zeros of phi: %d (roots), %d (sign changes), max|u phi(u)| at roots %.1e;"
        " x = M_k/t_f at the zeros: %s" % (L, len(p), len(Z), nsc, res, np.array2string(xs, precision=5)))
    log("         N_f required by (ii) for the %d pairs: %s; positive: %d; min distance of a positive one to an"
        " integer >= 1: %.3g; equally spaced triples: %d; zeros at u = 1 or 4: %d"
        % (len(Nf_req), np.array2string(np.array(Nf_req), precision=4), len(pos), dist, tri, len(reso)))
log("   summary, even 6 <= L <= 40: L, zeros (roots), zeros (sign changes), pairs, pairs with N_f > 0, max required N_f,"
    " equally spaced triples, zeros at u = 1 or 4, max|psi + <w/(x+1-c)>| at the zeros,")
log("   max over x in [1e-4, 1e3] of kappa'(u) - A_L (negative: (ii) needs N_f < 0), A_L")
for t in summ:
    log("   L=%2d: %2d %2d  pairs %3d  positive %d  max N_f %+.4f  triples %d  resonant %d  %.1e  %+.4f  %.4f" % t)

(OUT / "check_weight_next_order.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
