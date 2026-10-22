"""Check of 05-inertia-of-mark (v2): fall of the full grip from rest, (5.14) (I2), N_f = 1.

Joint description: body place x, branch, one field object y on a ring of L places; full-grip contract on
level k plus a held source g_s P_{x_s}. The start is the dressed band state with real envelope phi_j:
Psi = U sum_j phi_j |j,sigma> Omega_sigma(j), U the direct rotation (Schrieffer-Wolff) of the held band
onto the spectral band of the full contract. a(0) = d<v>/dlambda at 0, with v = i[C, x] (bond form), is
computed from the double commutator and from the joint evolution exp(-iC lambda); it is compared with
-E''(0) sum_j phi_{j+1} phi_{j-1} W'(j), E'' the exact curvature of the sector contract at g_s = 0 and
W(j) = g_s <Omega(j)|P_{x_s}|Omega(j)> the held weight.
Output: output/check_fall_full_grip.txt
"""
from pathlib import Path
import numpy as np
from scipy.linalg import expm

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
lines = []


def log(s=""):
    lines.append(s)


tf = 1.0
sx = np.array([[0, 1], [1, 0]], complex)
sz = np.diag([1.0, -1.0]).astype(complex)


def P(L, r):
    M = np.zeros((L, L)); M[r % L, r % L] = 1.0
    return M


def c1(L):
    Tp = np.roll(np.eye(L), 1, axis=0)
    return Tp, -tf * (Tp + Tp.T)


def curvature(L, g, tau, sig):
    """Exact curvature at P = 0 of the dressed level of (5.1) (full grip, g_s = 0) and the tau = 0 distance d."""
    Tp, h0 = c1(L)
    C0 = np.kron(np.eye(2), h0) + g * np.kron(sz, P(L, 0))
    Cp = 0.5 * tau * np.kron(-1j * sx, Tp.T)
    w0 = np.linalg.eigvalsh(C0)
    e, V = np.linalg.eigh(h0 + sig * g * P(L, 0)); phi = V[:, 0] * np.sign(V[0, 0])
    j = np.argmin(abs(w0 - e[0])); d = np.min(abs(np.delete(w0, j) - e[0]))
    C = C0 + Cp + Cp.conj().T
    d1 = -1j * Cp + 1j * Cp.conj().T
    d2 = -(Cp + Cp.conj().T)
    wc, Vc = np.linalg.eigh(C)
    i = np.argmax(abs(Vc.conj().T @ np.kron(np.eye(2)[:, 0 if sig > 0 else 1], phi))); psi = Vc[:, i]
    a = Vc.conj().T @ (d1 @ psi); m = np.arange(len(wc)) != i
    return np.real(psi.conj() @ d2 @ psi) + 2 * np.sum(abs(a[m]) ** 2 / (wc[i] - wc[m])), d, phi


def fall(L, g, sig, tau_over_d, gs, xs=0, wid=1.5):
    j0 = L // 2 - 1
    _, d, phi = curvature(L, g, 1e-5, sig)
    tau = tau_over_d * d
    E2, _, _ = curvature(L, g, tau, sig)
    Tp, h0 = c1(L)
    A = 0.5 * tau * np.kron(np.kron(Tp, -1j * sx), np.eye(L)); A = A + A.conj().T
    C = A + np.kron(np.eye(2 * L), h0 + gs * P(L, xs))
    for x in range(L):
        C = C + g * np.kron(np.kron(P(L, x), sz), P(L, x))
    v = -0.5 * tau * np.kron(np.kron(Tp + Tp.T, sx), np.eye(L))      # v = i[C, x], bond form
    b = 0 if sig > 0 else 1
    held = []
    for j in range(L):
        e, V = np.linalg.eigh(h0 + sig * g * P(L, j) + gs * P(L, xs))
        held.append(np.kron(np.kron(np.eye(L)[:, j], np.eye(2)[:, b]), V[:, 0] * np.sign(V[j, 0])))
    Pi = np.array(held).T
    wc, Vc = np.linalg.eigh(C)
    band = np.argsort(np.sum(abs(Vc.conj().T @ Pi) ** 2, axis=1))[-L:]
    Vb = Vc[:, band]
    Mo = Pi.conj().T @ Vb
    ev, EV = np.linalg.eigh(Mo @ Mo.conj().T)
    phij = np.exp(-(np.arange(L) - j0) ** 2 / (2 * wid * wid)); phij /= np.linalg.norm(phij)
    Psi = Vb @ (Mo.conj().T @ (EV @ np.diag(ev ** -0.5) @ EV.conj().T @ phij))
    a_comm = np.real(1j * (Psi.conj() @ (C @ (v @ Psi)) - Psi.conj() @ (v @ (C @ Psi))))
    lam = 1.0
    U = expm(-1j * C * lam)
    vp = np.real((U @ Psi).conj() @ v @ (U @ Psi)); vm = np.real((U.conj().T @ Psi).conj() @ v @ (U.conj().T @ Psi))
    a_evol = (vp - vm) / (2 * lam)
    W = np.array([gs * phi[(xs - j) % L] ** 2 for j in range(L)])
    pred = -E2 * sum(phij[(j + 1) % L] * phij[(j - 1) % L] * 0.5 * (W[(j + 1) % L] - W[(j - 1) % L]) for j in range(L))
    return d, tau, a_comm, a_evol, pred


log("(5.14): full grip, N_f = 1, t_f = 1, source at x_s = 0, Gaussian envelope (width 1.5) centred at L/2 - 1.")
log("a(0) from the double commutator and from the joint evolution (central difference of <v>, lambda = +-1),")
log("against -E''(0) sum_j phi_{j+1} phi_{j-1} W'(j). rel = a_comm/pred - 1; extrapolations: rel_0 = 2 rel(g_s) -")
log("rel(2 g_s) (the part that survives g_s -> 0) and rel(2 g_s) - rel(g_s) (the part linear in g_s).")
for L in (12, 16):
    for g in (0.1, 0.3):
        for sig in (-1, 1):
            for tod in (0.1, 0.05):
                res = [fall(L, g, sig, tod, gs) for gs in (1e-3, 2e-3)]
                r1 = res[0][2] / res[0][4] - 1; r2 = res[1][2] / res[1][4] - 1
                log("  L=%2d gamma*M=%.1f sig=%+d tau/d=%.2f d=%.4f | g_s=1e-3: a=%+.6e evol=%+.6e pred=%+.6e rel=%+.2e |"
                    " g_s=2e-3: rel=%+.2e | rel_0=%+.2e, linear part=%+.2e"
                    % (L, g, sig, tod, res[0][0], res[0][2], res[0][3], res[0][4], r1, r2, 2 * r1 - r2, r2 - r1))

(OUT / "check_fall_full_grip.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
