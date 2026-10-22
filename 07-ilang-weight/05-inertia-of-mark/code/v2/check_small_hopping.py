"""Check of 05-inertia-of-mark (v2): full grip, N_f = 1, small field hopping (I1).

1. (5.13): at t_f = 0 the curvature of the isolated lower dressed level comes only from body paths that
   wind the ring; exact curvature of the sector contract (6.1)/(5.1) against the leading winding term.
2. Order of limits at fixed tau: the exact curvature against the order-tau^2 term 2 tau^2 J of (5.2)
   (which vanishes as t_f^{2 N_f}) and the winding value, as t_f decreases.
Output: output/check_small_hopping.txt
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


def sector(L, tf, g, tau):
    Tp = np.roll(np.eye(L), 1, axis=0)
    P0 = np.zeros((L, L)); P0[0, 0] = 1.0
    C0 = np.kron(np.eye(2), -tf * (Tp + Tp.T)) + g * np.kron(sz, P0)
    Cp = 0.5 * tau * np.kron(-1j * sx, Tp.T)
    return C0, Cp, Tp, P0


def lower_level(L, tf, g, tau):
    """Lower branch sigma_l = -1 for g = gamma M_k > 0: curvature at P = 0 and the J of (5.2)."""
    C0, Cp, Tp, P0 = sector(L, tf, g, tau)
    h = -tf * (Tp + Tp.T) - g * P0
    w, V = np.linalg.eigh(h); e0, phi = w[0], V[:, 0] * np.sign(V[0, 0])
    C = C0 + Cp + Cp.conj().T
    d1 = -1j * Cp + 1j * Cp.conj().T
    d2 = -(Cp + Cp.conj().T)
    wc, Vc = np.linalg.eigh(C)
    ref = np.kron(np.eye(2)[:, 1], phi)
    i = np.argmax(abs(Vc.conj().T @ ref)); psi = Vc[:, i]
    a = Vc.conj().T @ (d1 @ psi); m = np.arange(len(wc)) != i
    E2 = np.real(psi.conj() @ d2 @ psi) + 2 * np.sum(abs(a[m]) ** 2 / (wc[i] - wc[m]))
    J = (Tp @ phi) @ np.linalg.solve(e0 * np.eye(L) - (-tf * (Tp + Tp.T) + g * P0), Tp.T @ phi)
    return E2, J


def wind(L, tau, G):
    if L % 2 == 0:
        return 2 * (-1) ** (L // 2) * L ** 2 * tau ** L / (2 ** L * G ** (L - 1))
    return -4 * L ** 2 * tau ** (2 * L) / (2 ** (2 * L) * G ** (2 * L - 1))


G = 1.0                                           # G = N_f |gamma| M_k, N_f = 1
log("1. (5.13) at t_f = 0, N_f = 1, G = |gamma| M_k = 1: exact E''(0) of the lower level vs leading winding term")
log("   L   tau/G   E'' exact        (5.13) leading   ratio    (1 - ratio)/(L tau^2/G^2)")
for L, taus in ((5, (0.1, 0.2)), (6, (0.1, 0.2)), (7, (0.2, 0.3)), (8, (0.1, 0.2))):
    for tau in taus:
        E2, _ = lower_level(L, 0.0, G, tau)
        pr = wind(L, tau, G)
        log("   %d   %.2f   %+.6e   %+.6e   %.5f   %.3f" % (L, tau, E2, pr, E2 / pr, (1 - E2 / pr) / (L * tau ** 2)))
log()

L, tau = 6, 0.2
log("2. Order of limits, L = 6, N_f = 1, G = 1, tau = %.1f (d_{k,sigma_l} -> |g| = 1 as t_f -> 0):" % tau)
log("   t_f      E'' exact       2 tau^2 J (order tau^2)   E''(t_f=0)")
E20, _ = lower_level(L, 0.0, G, tau)
for tf in (0.3, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 0.0):
    E2, J = lower_level(L, tf, G, tau) if tf > 0 else (E20, 0.0)
    log("   %.3f   %+.4e     %+.4e               %+.4e" % (tf, E2, 2 * tau ** 2 * J, E20))
log("   2 tau^2 J / (tau^2 t_f^2) at t_f = 0.001: %.4f (J = O(t_f^{2 N_f}))"
    % (2 * lower_level(L, 0.001, G, tau)[1] / 0.001 ** 2))

(OUT / "check_small_hopping.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
