"""Check (iii) of 06-ilang-source/04-profile.

Control field (4.14): one field object with places {empty} + an open chain of L places,
own term C1 = Delta * sum_x |x><x| - J * sum_x (|x><x+1| + h.c.), coupled operator Phi_x = |x><empty| + h.c.
Second-order mutual cost from the single-object contract (generic form (4.3)):
    M2 = -2 g1 g2 Re <phi|Phi_x1 R Phi_x2|phi>,
compared with -g1 g2 exp(-d/xi) / (J sinh(1/xi)), cosh(1/xi) = Delta/(2J); decay length fitted from ln|M2|.
"""
from pathlib import Path
import numpy as np
from scipy.linalg import eigh, solve

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
LOG = []


def out(s=""):
    print(s)
    LOG.append(s)


L, J, x1 = 400, 1.0, 100           # chain of L places (indices 1..L), place 0 = empty
out(f"Control field on an open chain of L = {L} places, J = {J}, x1 = {x1}, g1 = g2 = 1, N_f = 1")
for ratio in [2.02, 2.1, 2.5, 3.0]:
    Delta = ratio * J
    n = L + 1
    C = np.zeros((n, n))
    for x in range(1, n):
        C[x, x] = Delta
        if x + 1 < n:
            C[x, x + 1] = C[x + 1, x] = -J
    e, v = eigh(C)
    phi, eps = v[:, 0], e[0]
    P0 = np.outer(phi, phi)
    A = C - eps * np.eye(n) + (e[1] - e[0]) * P0           # invertible; equals C - eps on phi-perp

    def R_apply(u):
        """Reduced resolvent of C at eps applied to u."""
        return solve(A, u - phi * (phi @ u), assume_a="sym")

    def Phi_apply(x, u):
        """Coupled operator Phi_x = |x><empty| + |empty><x| applied to u."""
        w = np.zeros(n)
        w[x] += u[0]
        w[0] += u[x]
        return w

    theta = np.arccosh(Delta / (2 * J))
    xi = 1 / theta
    ds = np.arange(1, 161)
    M2 = np.array([-2 * (phi @ Phi_apply(x1, R_apply(Phi_apply(x1 + d, phi)))) for d in ds])
    form = -np.exp(-ds * theta) / (J * np.sinh(theta))
    ok = np.abs(form) > 1e-12 * abs(form[0])
    rel = np.max(np.abs(M2[ok] / form[ok] - 1))
    slope = np.polyfit(ds[ok], np.log(np.abs(M2[ok])), 1)[0]
    out(f"Delta/J = {ratio}: phi = |empty> (overlap {abs(phi[0]):.15f}), gap = {e[1]-e[0]:.4f}; "
        f"xi = 1/arccosh(Delta/2J) = {xi:.5f}; fitted decay length = {-1/slope:.5f}; "
        f"max |M2/(4.14) - 1| over d = 1..{ds[ok][-1]} = {rel:.1e}")
    out("   d  : " + "  ".join(f"{d:>9d}" for d in [1, 5, 10, 20, 40, 80]))
    out("   M2 : " + "  ".join(f"{M2[d-1]: .2e}" for d in [1, 5, 10, 20, 40, 80]))
    out("   d^6 |M2| : " + "  ".join(f"{d**6*abs(M2[d-1]):.2e}" for d in [1, 5, 10, 20, 40, 80]))

(OUT / "control_decay.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
