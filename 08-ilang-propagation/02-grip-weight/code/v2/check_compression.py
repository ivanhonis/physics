"""Check (ii) of 08-ilang-propagation/02-grip-weight (v2).

Ring of three oscillator cells. The total contract C = H + mu F(q_0) is compressed
to the M lowest levels of 1/2(p^2 + q^2) in every cell, C_M = Pi C Pi.
 - (G2) grip F = F0 + F1 q + F2 q^2: lowest eigenvalue of C_M (with and without the
   body) for increasing M against the exact uncompressed value (2.6).
 - (G) grip F = F0 + theta f, f = sin q + b (1 - cos q) (smooth, bounded derivatives):
   (a) the lowest eigenvalue of C_M at several theta, for increasing M, against an
       independent reference for the uncompressed contract: a sinc (Colbert-Miller)
       position grid in all three cells, on two grids;
   (b) the first and second Taylor coefficients in theta of the eigenvalue of C_M
       connected to the lowest one, against mu <f> and -mu^2 S of (2.9);
   (c) the residual of the reference against the second-order expression, divided by theta^3.
Output: output/compression.json.
"""
import json
import os
import threading
import time
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla
from scipy import integrate

WALL_LIMIT_S = 1500
threading.Timer(WALL_LIMIT_S, lambda: os._exit(3)).start()
T0 = time.time()
OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

KAPPA, MH = 1.0, 1.0
MS = [4, 6, 8, 10, 12, 16, 20, 24, 32]
G2 = (1.0, 0.5, 0.2)
F0G, B, MU_G = 1.0, 0.5, 0.75
THETAS = [0.05, 0.1, 0.2, 0.4]
GRIDS = [(0.30, 17), (0.24, 23)]  # (spacing h, half-number n): points j h, j = -n..n

# uncompressed 3-ring: K = (m^2 + 2 kappa) 1 - kappa (adjacency of the triangle)
K = (MH**2 + 2 * KAPPA) * np.eye(3) - KAPPA * (np.ones((3, 3)) - np.eye(3))
wk = np.sqrt(np.linalg.eigvalsh(K))
G0 = np.linalg.inv(K)[0, 0]
w0 = 0.5 * np.mean(1 / wk)


def fgrip(x):
    return np.sin(x) + B * (1 - np.cos(x))


def exact_g2(mu, F):
    F0, F1, F2 = F
    Kp = K.copy()
    Kp[0, 0] += 2 * mu * F2
    J = np.array([mu * F1, 0, 0])
    return mu * F0 + 0.5 * np.sum(np.sqrt(np.linalg.eigvalsh(Kp))) - 0.5 * J @ np.linalg.solve(Kp, J)


def cell_ops(M):
    n = np.arange(M)
    q = np.diag(np.sqrt((n[:-1] + 1) / 2), 1)
    q = q + q.T
    q2 = np.diag(n + 0.5) + np.diag(np.sqrt((n[:-2] + 1) * (n[:-2] + 2)) / 2, 2)
    q2 = np.triu(q2) + np.triu(q2, 1).T
    p2 = np.diag(n + 0.5) - np.diag(np.sqrt((n[:-2] + 1) * (n[:-2] + 2)) / 2, 2)
    p2 = np.triu(p2) + np.triu(p2, 1).T
    return q, q2, p2


def compressed_function(M, fun, extra=60):
    """Pi fun(q) Pi on the M lowest levels, from a much larger truncation."""
    qb, _, _ = cell_ops(M + extra)
    lam, U = np.linalg.eigh(qb)
    return ((U * fun(lam)) @ U.T)[:M, :M]


def field_contract(M):
    q, q2, p2 = cell_ops(M)
    I = sp.identity(M, format="csr")

    def on(op, x):
        mats = [I, I, I]
        mats[x] = sp.csr_matrix(op)
        return sp.kron(sp.kron(mats[0], mats[1]), mats[2], format="csr")
    H = sum(on(0.5 * p2 + 0.5 * (MH**2 + 2 * KAPPA) * q2, x) for x in range(3))
    for (x, y) in [(0, 1), (1, 2), (2, 0)]:
        mats = [I, I, I]
        mats[x] = sp.csr_matrix(q)
        mats[y] = sp.csr_matrix(q)
        H = H - KAPPA * sp.kron(sp.kron(mats[0], mats[1]), mats[2], format="csr")
    return H, on


def lowest(A, v0=None):
    vals, vecs = sla.eigsh(A, k=1, which="SA", tol=1e-13, v0=v0, maxiter=200000)
    return vals[0], vecs[:, 0]


def dvr_lowest(theta, h, n):
    """Lowest eigenvalue of H + mu (F0 + theta f(q_0)) on a sinc position grid in each cell."""
    j = np.arange(-n, n + 1)
    x = h * j
    dj = j[:, None] - j[None, :]
    # Colbert-Miller kinetic matrix of 1/2 p^2: (1/(2h^2)) [pi^2/3 on the diagonal, 2(-1)^k/k^2 off it]
    T1 = np.where(dj == 0, np.pi**2 / 6, (-1.0) ** np.abs(dj) / np.where(dj == 0, 1, dj) ** 2) / h**2
    q0, q1, q2 = x[:, None, None], x[None, :, None], x[None, None, :]
    V = 0.5 * (K[0, 0] * q0**2 + K[1, 1] * q1**2 + K[2, 2] * q2**2
               + 2 * K[0, 1] * q0 * q1 + 2 * K[1, 2] * q1 * q2 + 2 * K[0, 2] * q0 * q2)
    V = V + MU_G * (F0G + theta * fgrip(q0))
    m = len(x)
    shape = (m, m, m)

    def mv(v):
        p = v.reshape(shape)
        out = V * p
        out = out + np.tensordot(T1, p, axes=(1, 0))
        out = out + np.moveaxis(np.tensordot(T1, p, axes=(1, 1)), 0, 1)
        out = out + np.moveaxis(np.tensordot(T1, p, axes=(1, 2)), 0, 2)
        return out.ravel()
    A = sla.LinearOperator((m**3, m**3), matvec=mv, dtype=float)
    # start: Gaussian lowest eigenvector of the field, exp(-1/2 q K^{1/2} q)
    Ks = np.real(np.linalg.eigh(K)[1] @ np.diag(wk) @ np.linalg.eigh(K)[1].T)
    g0 = np.exp(-0.5 * (Ks[0, 0] * q0**2 + Ks[1, 1] * q1**2 + Ks[2, 2] * q2**2
                        + 2 * Ks[0, 1] * q0 * q1 + 2 * Ks[1, 2] * q1 * q2 + 2 * Ks[0, 2] * q0 * q2)).ravel()
    vals = sla.eigsh(A, k=1, which="SA", tol=1e-14, v0=g0, ncv=60, maxiter=100000, return_eigenvectors=False)
    return float(vals[0]), m


def main():
    res = dict(parameters=dict(kappa_h=KAPPA, m_h=MH, G2_grip=G2,
                               G_grip=dict(F0=F0G, b=B, mu=MU_G, thetas=THETAS), dvr_grids=GRIDS),
               field=dict(omega=wk.tolist(), G0=G0, w0=w0))
    # analytic (M -> infinity) Taylor coefficients for f = sin q + b (1 - cos q)
    c = lambda tau: np.sum(np.exp(-wk * tau) / wk) / 6.0
    S_int, _ = integrate.quad(lambda t: np.sinh(c(t)) + B**2 * (np.cosh(c(t)) - 1), 0, np.inf, epsabs=1e-14, limit=400)
    T_int, _ = integrate.quad(lambda t: 1 - np.exp(-c(t)), 0, np.inf, epsabs=1e-14, limit=400)
    Sf = np.exp(-w0) * S_int
    Tf = B * np.exp(-w0) * T_int
    E_field_exact = 0.5 * np.sum(wk)
    E1_exact = MU_G * B * (1 - np.exp(-w0 / 2))
    E2_exact = -MU_G**2 * Sf

    # (a) independent reference: sinc grids, theta = 0 checks the grid against the exact field value
    ref = {}
    for th in [0.0] + THETAS:
        vals = [dvr_lowest(th, h, n)[0] for (h, n) in GRIDS]
        ref[th] = dict(E_grid_coarse=vals[0], E_grid_fine=vals[1], grid_difference=vals[1] - vals[0])
    ref[0.0]["exact"] = E_field_exact + MU_G * F0G
    print(f"grid references done at {time.time() - T0:.1f}s", flush=True)

    rows_g2, rows_g = [], []
    for M in MS:
        H, on = field_contract(M)
        q, q2, _ = cell_ops(M)
        E_f, Om = lowest(H)
        row = dict(M=M, E_field=E_f, E_field_exact=E_field_exact)
        for mu in (+0.75, -0.75):
            F0, F1, F2 = G2
            V = on(F0 * np.eye(M) + F1 * q + F2 * q2, 0) * mu
            E_b, _ = lowest(H + V, v0=Om)
            row[f"E_body_mu{mu:+}"] = E_b
            row[f"E_body_exact_mu{mu:+}"] = exact_g2(mu, G2)
            row[f"cost_mu{mu:+}"] = E_b - E_f
            row[f"cost_exact_mu{mu:+}"] = exact_g2(mu, G2) - E_field_exact
        rows_g2.append(row)
        # (G): (b) Taylor coefficients by Rayleigh-Schroedinger on the finite matrix
        fM = compressed_function(M, fgrip)
        V = on(fM, 0) * MU_G
        VO = V @ Om
        E1 = Om @ VO
        rhs = VO - E1 * Om
        A = sla.LinearOperator(H.shape, matvec=lambda x: H @ x - E_f * x + Om * (Om @ x), dtype=float)
        sol, info = sla.cg(A, rhs, rtol=1e-13, atol=0, maxiter=20000)
        E2 = -rhs @ sol
        rg = dict(M=M, E1=E1, E1_exact=E1_exact, E2=E2, E2_exact=E2_exact, cg_info=int(info))
        # (a) lowest eigenvalue of C_M at several theta against the grid reference
        for th in THETAS:
            Eth, _ = lowest(H + on(F0G * np.eye(M), 0) * MU_G + th * V, v0=Om)
            rg[f"E_CM_theta{th}"] = Eth
            rg[f"err_vs_reference_theta{th}"] = Eth - ref[th]["E_grid_fine"]
        rows_g.append(rg)
        print(f"M={M} done at {time.time() - T0:.1f}s", flush=True)
    # (c) residual of the reference against the second-order expression
    cubic = {}
    for th in THETAS:
        E2nd = E_field_exact + MU_G * F0G + th * E1_exact + th**2 * E2_exact
        cubic[th] = dict(E_reference=ref[th]["E_grid_fine"], E_second_order=E2nd,
                         residual=ref[th]["E_grid_fine"] - E2nd,
                         residual_over_theta3=(ref[th]["E_grid_fine"] - E2nd) / th**3)
    res["G2"] = rows_g2
    res["G"] = rows_g
    res["G_reference"] = {str(k): v for k, v in ref.items()}
    res["G_residual_against_second_order"] = {str(k): v for k, v in cubic.items()}
    res["G_weight_coefficient_T"] = Tf
    res["runtime_s"] = time.time() - T0
    with open(OUT / "compression.json", "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))
    os._exit(0)


if __name__ == "__main__":
    main()
