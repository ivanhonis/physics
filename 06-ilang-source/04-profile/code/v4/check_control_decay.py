"""Check (iii) of 06-ilang-source/04-profile.

(a) Field with one shared empty place, (4.14): one field object with places {empty} + an open chain of L places,
    own term C1 = Delta * sum_x |x><x| - J * sum_x (|x><x+1| + h.c.), coupled operator Phi_x = |x><empty| + h.c.
    Second-order mutual cost from the single-object contract (generic form (4.3)):
        M2 = -2 g1 g2 Re <phi|Phi_x1 R Phi_x2|phi>,
    compared with -g1 g2 exp(-d/xi) / (J sinh(1/xi)), cosh(1/xi) = Delta/(2J); decay length fitted from ln|M2|.
(b) The same field beyond second order: exact M(d) by diagonalization, against its large-d limit
    g1^2 g2^2 (A11 B22 + A22 B11), A = K^{-1}, B = K^{-2}, K = C1 restricted to the chain (Step 7).
(c) Cell field (4.20): one field object with places {0,1}^L (L cells of an open chain), own term
    Cf = Delta sum_y n_y - J sum_y (s+_y s-_{y+1} + h.c.), coupled operator Phi_x = sigma^x_x.
    Exact M(d) by sparse diagonalization, against M2 = -2 g1 g2 K^{-1}(x1, x2) (K: the L x L chain block),
    and the decay length fitted from ln|M| against xi.
    Against the explicit bound (4.20), g1 = g2 = g, r1 = r2 = (Delta - 2 rho)/4:
        |M| <= 24 g^2 / (Delta - 2 rho) * (J/rho)^d,  J < rho < Delta/2 - 2 g,
    minimized over rho for each d; bound decay length 1/ln(rho_max/J), rho_max = Delta/2 - 2g.
(d) Cell field, order of vanishing in the hopping (Step 7): on a short chain, M(J)/M(J/2) -> 2^d as J -> 0.
"""
from pathlib import Path
import numpy as np
import scipy.sparse as sp
from scipy.linalg import eigh, solve, eigvalsh
from scipy.sparse.linalg import eigsh

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
LOG = []


def out(s=""):
    print(s)
    LOG.append(s)


# ---------------- (a) second order of the shared-empty-place field ----------------
L, J, x1 = 400, 1.0, 100           # chain of L places (indices 1..L), place 0 = empty
out(f"(a) Shared empty place, second order: open chain of L = {L} places, J = {J}, x1 = {x1}, g1 = g2 = 1, N_f = 1")


def shared_contract(Delta, n=L + 1):
    C = np.zeros((n, n))
    for x in range(1, n):
        C[x, x] = Delta
        if x + 1 < n:
            C[x, x + 1] = C[x + 1, x] = -J
    return C


for ratio in [2.02, 2.1, 2.5, 3.0]:
    Delta = ratio * J
    n = L + 1
    C = shared_contract(Delta)
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

# ---------------- (b) the shared-empty-place field beyond second order ----------------
out("")
out("(b) Shared empty place, exact M(d) = eps0(g,g) - eps0(g,0) - eps0(0,g) + eps0(0,0), N_f = 1, Delta/J = 3, "
    f"L = {L}, x1 = {x1}")
out("    limit = g1^2 g2^2 (A11 B22 + A22 B11) (fourth order, d -> infinity), A = K^{-1}, B = K^{-2}")
Delta = 3.0 * J
C = shared_contract(Delta)
K = C[1:, 1:]
Ki = np.linalg.inv(K)
K2 = Ki @ Ki


def eps0(srcs):
    h = C.copy()
    for x, g in srcs:
        h[x, 0] += g
        h[0, x] += g
    return eigvalsh(h, subset_by_index=[0, 0])[0]


E00 = eps0([])
out(f"    eps0(0,0) = {E00:.1e}")
out("    g      d:        1           10          40          160       limit(d=160)   M(160)/limit - 1")
for g in [0.05, 0.1, 0.2]:
    E1 = eps0([(x1, g)])
    Ms = {}
    for d in [1, 10, 40, 160]:
        Ms[d] = eps0([(x1, g), (x1 + d, g)]) - E1 - eps0([(x1 + d, g)]) + E00
    a, b = x1 - 1, x1 + 160 - 1
    lim = g**4 * (Ki[a, a] * K2[b, b] + Ki[b, b] * K2[a, a])
    out(f"    {g:4.2f}     " + "  ".join(f"{Ms[d]: .3e}" for d in [1, 10, 40, 160]) + f"   {lim: .4e}     {Ms[160]/lim - 1: .2e}")

# ---------------- (c) the cell field ----------------
Lc = 18
out("")
out(f"(c) Cell field: {Lc} cells (places {{0,1}}^{Lc}, dimension {2**Lc}), J = 1, x1 = 2 (cells 0..{Lc-1}), "
    "g1 = g2 = g; exact M by sparse diagonalization (eigsh)")


def cell_contract(Delta, Lc=Lc, J=J):
    N = 1 << Lc
    s = np.arange(N)
    pop = sum((s >> y) & 1 for y in range(Lc))
    rows, cols, vals = [s], [s], [Delta * pop.astype(float)]
    for y in range(Lc - 1):
        m = ((s >> y) & 1) != ((s >> (y + 1)) & 1)
        rows.append(s[m])
        cols.append(s[m] ^ ((1 << y) | (1 << (y + 1))))
        vals.append(-J * np.ones(m.sum()))
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(N, N))


def sigx(x, Lc=Lc):
    N = 1 << Lc
    s = np.arange(N)
    return sp.csr_matrix((np.ones(N), (s, s ^ (1 << x))), shape=(N, N))


SX = [sigx(x) for x in range(Lc)]
v0 = np.zeros(1 << Lc)
v0[0] = 1.0


def ground(H):
    return eigsh(H, k=1, which="SA", tol=0, v0=v0 + 1e-3)[0][0]


xa = 2
ds = np.arange(1, 15)
for ratio, g in [(3.0, 0.1), (3.0, 0.2), (2.5, 0.1)]:
    Delta = ratio * J
    Cf = cell_contract(Delta)
    Kc = Delta * np.eye(Lc) - J * (np.eye(Lc, k=1) + np.eye(Lc, k=-1))
    Kci = np.linalg.inv(Kc)
    xi = 1 / np.arccosh(Delta / (2 * J))
    assert np.abs(Cf @ v0).max() == 0.0   # the vacuum is an exact eigenvector with cost 0, the lowest (Step 7);
    E0 = 0.0                              # eigsh does not resolve this isolated one-dimensional sector, so it is set
    E1 = ground(Cf + g * SX[xa])
    Ms, M2s = [], []
    for d in ds:
        xb = xa + d
        Ms.append(ground(Cf + g * SX[xa] + g * SX[xb]) - E1 - ground(Cf + g * SX[xb]) + E0)
        M2s.append(-2 * g * g * Kci[xa, xb])
    Ms, M2s = np.array(Ms), np.array(M2s)
    fit = (ds >= 2) & (ds <= 12)
    xi_M = -1 / np.polyfit(ds[fit], np.log(np.abs(Ms[fit])), 1)[0]
    xi_M2 = -1 / np.polyfit(ds[fit], np.log(np.abs(M2s[fit])), 1)[0]
    ratio_r = Ms / M2s
    out(f"Delta/J = {ratio}, g = {g} (|g1|+|g2| = {2*g} < (Delta-2J)/2 = {(Delta-2*J)/2}): E0 = 0 (vacuum), xi = {xi:.5f}; "
        f"fitted decay length on 2 <= d <= 12: of M {xi_M:.5f}, of M2 {xi_M2:.5f}")
    out("   d      : " + " ".join(f"{d:>9d}" for d in ds))
    out("   M      : " + " ".join(f"{m: .2e}" for m in Ms))
    out("   M/M2   : " + " ".join(f"{r:9.5f}" for r in ratio_r))
    out(f"   M/M2 over 1 <= d <= 14: min {ratio_r.min():.5f}, max {ratio_r.max():.5f}; "
        f"over 4 <= d <= 14: spread {ratio_r[3:].max() - ratio_r[3:].min():.1e}")
    rho_max = Delta / 2 - 2 * g
    rhos = np.linspace(J, rho_max, 2002)[1:-1]
    bound = np.array([np.min(24 * g * g / (Delta - 2 * rhos) * (J / rhos) ** d) for d in ds])
    out(f"   bound (4.20): " + " ".join(f"{b: .2e}" for b in bound))
    out(f"   max_d |M|/bound = {np.max(np.abs(Ms) / bound):.2e} (<= 1 required); bound decay length "
        f"1/ln(rho_max/J) = {1/np.log(rho_max/J):.3f}, its g -> 0 limit 1/ln(Delta/2J) = {1/np.log(Delta/(2*J)):.3f}, "
        f"xi = {xi:.3f}")

# ---------------- (d) order of vanishing in the hopping ----------------
Ls, Delta, g, xa = 10, 3.0, 0.3, 2
out("")
out(f"(d) Cell field, {Ls} cells, Delta = {Delta}, g1 = g2 = g = {g}, x1 = {xa}: exact M by dense diagonalization at hopping J;")
out("    Step 7: M = O(J^d), so M(J)/M(J/2) -> 2^d as J -> 0; listed: [M(J)/M(J/2)] / 2^d")
SXs = [sigx(x, Ls).toarray() for x in range(Ls)]


def low(H):
    return eigvalsh(H, subset_by_index=[0, 0])[0]


out("    J \\ d : " + "  ".join(f"{d:>9d}" for d in range(1, 6)))
for Jh in [0.4, 0.2, 0.1]:
    row = []
    for Jx in [Jh, Jh / 2]:
        H0 = cell_contract(Delta, Ls, Jx).toarray()
        E0, E1 = low(H0), low(H0 + g * SXs[xa])
        row.append([low(H0 + g * SXs[xa] + g * SXs[xa + d]) - E1 - low(H0 + g * SXs[xa + d]) + E0 for d in range(1, 6)])
    out(f"    {Jh:5.3f}  : " + "  ".join(f"{row[0][k] / row[1][k] / 2 ** (k + 1):9.5f}" for k in range(5)))

(OUT / "control_decay.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
