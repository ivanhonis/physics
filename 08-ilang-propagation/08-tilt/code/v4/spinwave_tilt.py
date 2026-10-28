"""Check (item 1(b), leading order in 1/S): first correction to m(x) far from the push.

Quadratic form (units J S = 1): C_2 = 1/2 P^T T P + 1/2 Q^T V Q with
V = Lap + eta P_h, T = E V E = Lap^+ + eta P_h, eta = h_p/(J S), E = diag(eps).
Ground-state covariances: <QQ^T> = 1/2 T^(1/2) (T^(1/2) V T^(1/2))^(-1/2) T^(1/2), same for P with T<->V.
First correction: m(x) = eps_h (S - dS(x)), dS(x) = (<Q_x^2> + <P_x^2> - 1)/2.
Output: output/spinwave_tilt.txt
"""
from pathlib import Path
import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)


def lattice(L, D):
    n = L ** D
    coords = np.array(np.unravel_index(np.arange(n), (L,) * D)).T
    adj = np.zeros((n, n))
    for d in range(D):
        sh = coords.copy()
        sh[:, d] = (sh[:, d] + 1) % L
        j = np.ravel_multi_index(sh.T, (L,) * D)
        adj[np.arange(n), j] += 1
        adj[j, np.arange(n)] += 1
    eps = (-1.0) ** coords.sum(axis=1)
    return coords, adj, eps


def sqrtm_sym(A, power):
    w, U = np.linalg.eigh(A)
    return (U * w ** power) @ U.T


def dS_push(L, D, eta):
    coords, adj, eps = lattice(L, D)
    z = 2 * D
    n = L ** D
    V = z * np.eye(n) - adj
    V[0, 0] += eta
    T = (eps[:, None] * V) * eps[None, :]
    Vh = sqrtm_sym(V, 0.5)
    Th = (eps[:, None] * Vh) * eps[None, :]
    covQ = 0.5 * Th @ sqrtm_sym(Th @ V @ Th, -0.5) @ Th
    covP = 0.5 * Vh @ sqrtm_sym(Vh @ T @ Vh, -0.5) @ Vh
    far = np.ravel_multi_index(tuple(np.full(D, L // 2)), (L,) * D)
    dS = 0.5 * (np.diag(covQ) + np.diag(covP) - 1)
    return dS[far], dS[0], np.max(np.abs(np.diag(covQ) - np.diag(covP)))


def dS3_bulk(L):
    k = 2 * np.pi * (np.arange(L) + 0.5) / L
    c = np.cos(k)
    tot = 0.0
    for c1 in c:
        g = (c1 + c[:, None] + c[None, :]) / 3.0
        tot += np.sum(1.0 / np.sqrt(1.0 - g ** 2))
    W = tot / L ** 3
    return 0.5 * (W - 1.0)


def main():
    out = ["# Leading order in 1/S: first correction dS, m = eps_h (S - dS) + O(1/S)"]
    out.append("\n## Cubic torus, L -> infinity, no push (midpoint sums): dS_3 = (W - 1)/2")
    vals = {}
    for L in (64, 128, 256):
        vals[L] = dS3_bulk(L)
        out.append(f"L={L:4d}: dS_3 = {vals[L]:.6f}")
    rich = (4 * vals[256] - vals[128]) / 3
    out.append(f"Richardson (error ~ L^-2): dS_3 = {rich:.5f}")
    out.append("\n## Cubic torus with push (exact Gaussian), far site (L/2,L/2,L/2)")
    out.append("L    eta=h_p/(JS)   dS(far)    dS(h)     zero-mode estimate sqrt(2z/(N eta))/2   max|<Q^2>-<P^2>|")
    for L in (8, 12, 16):
        for eta in (0.1, 1.0, 10.0):
            f, h, sym = dS_push(L, 3, eta)
            est = 0.5 * np.sqrt(12.0 / (L ** 3 * eta))
            out.append(f"{L:3d}  {eta:6.2f}        {f:.5f}   {h:.5f}   {est:.5f}                                {sym:.1e}")
    out.append("\n## Ring with push (exact Gaussian), eta = 1, far site L/2")
    out.append("L      dS(L/2)    dS(L/2) - (1/pi) ln(L/2)")
    ring = []
    for L in (64, 128, 256, 512, 1024):
        f, h, _ = dS_push(L, 1, 1.0)
        ring.append((L, f))
        out.append(f"{L:5d}  {f:.5f}    {f - np.log(L / 2) / np.pi:.5f}")
    sl = np.polyfit(np.log([r[0] for r in ring[-3:]]), [r[1] for r in ring[-3:]], 1)[0]
    out.append(f"slope d dS / d ln L (last three sizes) = {sl:.5f};  1/pi = {1 / np.pi:.5f} (Dirichlet image at the push)")
    (OUT / "spinwave_tilt.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
