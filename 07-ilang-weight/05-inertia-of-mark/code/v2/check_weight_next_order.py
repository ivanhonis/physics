"""Check of 05-inertia-of-mark (v2): weight over inertia, place pairs with F = 0 or Xi = 0 (I5), N_f = 1.

1. F = 0 exactly for reflection-equivalent pairs (r' = -r mod L); list of pairs with Xi = 0 for 5 <= L <= 16.
2. (5.15) at L = 8, (r, r') = (3, 4) (Xi = 0): E''(0) Delta W / (tau^2 F Lambda) - 1 from the exact tau^2
   coefficient (E'' = 2 tau^2 J of (5.2), exact in gamma) and the exact first-order held weight, against the
   order-gamma^2 prediction, for the full grip, (a) and (c).
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
log("   at those pairs Psi_0 - K_L of (5.15) (full grip, N_f = 1).")
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
        extra = "; Psi_0 - K_L = %.5f/t_f^2" % (P0 - K0)
    log("   L=%2d: F = 0 exactly on the %d reflection-equivalent pairs: %s; max|Xi - closed form| = %.1e;"
        " Xi = 0 on: %s%s" % (L, len(zeroF), refl, dev, xi0, extra))
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

(OUT / "check_weight_next_order.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
