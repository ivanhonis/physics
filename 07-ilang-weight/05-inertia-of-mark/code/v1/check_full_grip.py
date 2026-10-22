"""Check of 05-inertia-of-mark (v1): full grip, N_f = 1, exact sector contract (6.1).

Compares the curvature of the exact dressed level at P = 0 with (5.2) and (5.6),
and the ratios of items 2 and 3 ((5.7), (5.10)) with the same exact data.
Output: output/check_full_grip.txt
"""
from pathlib import Path
import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
lines = []


def log(s=""):
    lines.append(s)


t_f, g_s = 1.0, 1.0
m, Nclk, lam0 = 1.0, 2, 2.5 * np.pi              # M_k = m + 2 pi k/(N lam0): 1.0, 1.4
Ms = [m + 2 * np.pi * k / (Nclk * lam0) for k in range(Nclk)]
sx = np.array([[0, 1], [1, 0]], complex)
sz = np.diag([1.0, -1.0]).astype(complex)


def ring(L):
    Tp = np.roll(np.eye(L), 1, axis=0)            # T_+ |r> = |r+1>
    c1 = -t_f * (Tp + Tp.T)
    P0 = np.zeros((L, L)); P0[0, 0] = 1.0
    return Tp, Tp.T, c1, P0


def ground(L, g):
    _, _, c1, P0 = ring(L)
    w, V = np.linalg.eigh(c1 + g * P0)
    phi = V[:, 0] * np.sign(V[0, 0] if abs(V[0, 0]) > 1e-12 else V[1, 0])
    return w[0], phi


def sector(L, g, tau):
    """C(P) = C0 + e^{-iP} Cp + e^{iP} Cp^dag, full grip, N_f = 1, (5.1)."""
    _, Tm, c1, P0 = ring(L)
    C0 = np.kron(np.eye(2), c1) + g * np.kron(sz, P0)
    Cp = 0.5 * tau * np.kron(-1j * sx, Tm)
    return C0, Cp


def exact_curv(L, g, tau, sig):
    C0, Cp = sector(L, g, tau)
    C = C0 + Cp + Cp.conj().T
    d1 = -1j * Cp + 1j * Cp.conj().T             # dC/dP at P = 0
    d2 = -(Cp + Cp.conj().T)                       # d2C/dP2 at P = 0
    w, V = np.linalg.eigh(C)
    _, phi = ground(L, sig * g)
    ref = np.kron(np.eye(2)[:, 0 if sig > 0 else 1], phi)
    i = np.argmax(abs(V.conj().T @ ref))
    psi = V[:, i]
    a = V.conj().T @ (d1 @ psi)
    mask = np.arange(len(w)) != i
    E2 = np.real(psi.conj() @ d2 @ psi) + 2 * np.sum(abs(a[mask]) ** 2 / (w[i] - w[mask]))
    w0 = np.linalg.eigvalsh(C0)
    e0s = ground(L, sig * g)[0]
    j = np.argmin(abs(w0 - e0s))
    dist = np.min(abs(np.delete(w0, j) - e0s))     # isolation distance d_sigma
    return E2, dist


def J_tau2(L, g, sig):
    """(5.2): J = <phi_s| T_- (E0_s - h_{-s})^{-1} T_- |phi_s>, E'' = 2 tau^2 J."""
    Tp, Tm, c1, P0 = ring(L)
    e0, phi = ground(L, sig * g)
    return (Tp @ phi) @ np.linalg.solve(e0 * np.eye(L) - (c1 - sig * g * P0), Tm @ phi)


def sums(L):
    q = 2 * np.pi * np.arange(1, L) / L
    eps = 2 * t_f * (1 - np.cos(q))
    s1 = np.sum(1 / eps) / L
    s2 = np.sum(1 / eps ** 2) / L
    S2 = np.sum((1 + np.cos(q)) / eps ** 2) / L
    Lam = 2 * np.eye(L) - ring(L)[0] - ring(L)[1]
    ell = np.linalg.pinv(Lam)
    return s1, s2, S2, ell[:, 0], (ell @ ell)[:, 0]


# ---- 0. sector contract (6.1)/(5.1) against the full contract, L = 6
L, g, tau = 6, 0.3, 0.2
Tp, Tm, c1, P0 = ring(L)
A = 0.5 * tau * (np.kron(np.kron(Tp, -1j * sx), np.eye(L)))
A = A + A.conj().T
Cf = A + np.kron(np.eye(2 * L), c1)
for x in range(L):
    Px = np.zeros((L, L)); Px[x, x] = 1
    Cf = Cf + g * np.kron(np.kron(np.diag(np.eye(L)[x]), sz), Px)
full = np.sort(np.linalg.eigvalsh(Cf))
sec = []
for jP in range(L):
    C0, Cp = sector(L, g, tau)
    P = 2 * np.pi * jP / L
    sec += list(np.linalg.eigvalsh(C0 + np.exp(-1j * P) * Cp + np.exp(1j * P) * Cp.conj().T))
log("0. Sector contract vs full contract (L=6, gamma*M=0.3, tau=0.2): max |eig diff| = %.2e"
    % np.max(abs(full - np.sort(sec))))
log()

# ---- 1-3. curvature, inertia vs cost, weight over inertia
r, rp = 2, 3                                      # r = x_s - x, r' = x_s - x'
for L in (8, 13):
    n = 1.0 / L
    s1, s2, S2, ell, ell2 = sums(L)
    ell0 = ell[0]
    K = 2 * n * S2 + s1 ** 2 - s2 / L
    br = lambda f: f[r] - f[rp]
    F = -2 * g_s * br(ell) / t_f
    F2 = g_s / (n * t_f ** 2) * br(ell ** 2 - 2 * ell2 / L)
    Xi = -br(ell ** 2 + 2 * ell0 * ell - 2 * ell2 / L) / (2 * t_f * br(ell))
    eps1 = 2 * t_f * (1 - np.cos(2 * np.pi / L))
    log("L = %d, N_f = 1, n = 1/L, t_f = 1, eps_1 = %.4f, ell_0 = %.5f, K_L = %.4f, Xi = %.4f"
        % (L, eps1, ell0, K, Xi))
    for gam in (0.01, 0.02, 0.3):
        log("  gamma = %.3f   (N_f*kappa_k = gamma*M_k*L/t_f = %s)"
            % (gam, ", ".join("%.3f" % (gam * M * L / t_f) for M in Ms)))
        log("    k sig   d_sig     tau/d   |E''/(2tau^2 J)-1|  E''/(5.6)-1   "
            "tau^2 mu-Cost  pred(5.7)  -C_even   E''dW/(tau^2F)-1  pred g_sig*Xi")
        res = {}
        for k, M in enumerate(Ms):
            g = gam * M
            e00 = ground(L, 0.0)[0]
            cost = {s: ground(L, s * g)[0] - e00 for s in (1, -1)}
            ceven = 0.5 * (cost[1] + cost[-1])
            for sig in (1, -1):
                tau = 1e-5
                E2, d = exact_curv(L, g, tau, sig)
                E2b, _ = exact_curv(L, g, 0.2 * d, sig)
                J = J_tau2(L, g, sig)
                pred6 = tau ** 2 / (n * sig * g) * (1 - g ** 2 * K)
                D = tau ** 2 / E2 - cost[sig]
                phi = ground(L, sig * g)[1]
                dW = g_s * (phi[r] ** 2 - phi[rp] ** 2)
                rat3 = E2 * dW / (tau ** 2 * F) - 1
                res[(k, sig)] = (D, E2 * dW / tau ** 2, cost[sig], tau ** 2 / E2, dW)
                log("    %d %+d  %.3e  %.1e   %.1e (tau=d/5: %.1e)  %+.2e   %+.4e %+.4e %+.4e   %+.4e  %+.4e"
                    % (k, sig, d, tau / d, abs(E2 / (2 * tau ** 2 * J) - 1),
                       abs(E2b / (2 * (0.2 * d) ** 2 * J) - 1), E2 / pred6 - 1,
                       D, n * ell0 * g ** 2 / t_f, -ceven, rat3, sig * g * Xi))
        # level-difference and branch-difference forms (item 2), weight over inertia spread (item 3)
        lv = res[(1, 1)][0] - res[(0, 1)][0]
        lvp = n * ell0 * gam ** 2 * (Ms[1] ** 2 - Ms[0] ** 2) / t_f
        brd = [(res[(k, 1)][3] - res[(k, -1)][3]) - (res[(k, 1)][2] - res[(k, -1)][2]) for k in range(Nclk)]
        spread = [res[key][1] for key in res]
        cw = [abs(res[(k, s)][4] - (F * res[(k, s)][2] + F2 * res[(k, s)][2] ** 2)) for k in range(Nclk) for s in (1, -1)]
        log("    item 2: level difference of tau^2 mu - Cost (k=1 minus k=0, sig=+): %+.4e, pred %+.4e"
            % (lv, lvp))
        log("    item 2: branch differences tau^2(mu_+ - mu_-) - (Cost_+ - Cost_-), k=0,1: %+.2e, %+.2e"
            "  (vs Cost_+ - Cost_- = %.3e, %.3e)"
            % (brd[0], brd[1], res[(0, 1)][2] - res[(0, -1)][2], res[(1, 1)][2] - res[(1, -1)][2]))
        log("    item 3: E''dW/tau^2 over (k,sig): min %+.5e max %+.5e, leading F = %+.5e;"
            " max |dW - (F C + F2 C^2)| = %.1e" % (min(spread), max(spread), F, max(cw)))
        odd = [0.5 * (res[(k, 1)][1] - res[(k, -1)][1]) / F for k in range(Nclk)]
        evn = [0.5 * (res[(k, 1)][1] + res[(k, -1)][1]) / F - 1 for k in range(Nclk)]
        log("    item 3: odd part of E''dW/(tau^2 F) over sig, k=0,1: %+.5e %+.5e; pred gamma*M_k*Xi:"
            " %+.5e %+.5e; even part minus 1: %+.2e %+.2e"
            % (odd[0], odd[1], gam * Ms[0] * Xi, gam * Ms[1] * Xi, evn[0], evn[1]))
    log()

(OUT / "check_full_grip.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
