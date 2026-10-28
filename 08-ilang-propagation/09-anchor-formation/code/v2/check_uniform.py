"""Check (iii) of 09-anchor-formation: the uniform part U(l) = place average of da(x,l) (item 3).

Exact solution of the linear equations of the means (M -> infinity),
    d^2 q/dl^2 = -K_a q - e_{x_s},  q(0) = dq/dl(0) = 0,  K_a = kappa_h*Lap + kappa_a*P_h.
Cubic torus L = 8, 12, 16, 20 (kappa_a = 1; RK4, dt = 0.05) against (9.14):
    U(l) = U_st [1 - cos(l/T_U)] + O(1/L) U_st,  T_U = sqrt(L^3 c_phi^(L)),  c_phi^(L) = 1/kappa_a + g_L(0),
    U_st = -[c_phi^(L) - g_L(x_s-h)];
  plus two variations at L = 12 (anchor farther, kappa_a = 4), the lowest normal mode of K_a from
  a sparse eigen-solver, and the slow image: place-dependent part of psi_0(x)psi_0(x_s)/nu_0 against
  -(1-beta_L) g_L(x-h), beta_L = g_L(x_s-h)/c_phi^(L).
Ring L = 128, 256, 512 (kappa_a = 1, d_s = L/4; exact eigen-decomposition) against (9.15):
    U(l) = -(L/2kappa_h) [f(alpha) - f(alpha+tau)/2 - f(alpha-tau)/2],  tau = c_0 l/L, alpha = d_s/L,
  f the odd 2-periodic extension of x(1-x).
Ring with a weak anchor (kappa_a L << kappa_h; L = 32, 64): the slow-mode form of (9.14) with
  c_phi^(L) = 1/kappa_a + (L^2-1)/(12 kappa_h L), T_U = sqrt(L c_phi^(L)).
"""
from pathlib import Path
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
KH = 1.0
C0 = np.sqrt(KH)


def g_torus(L, ys):
    """g_L(y) = L^-3 sum_{k != 0} cos(k.y) / (kappa_h Lap)(k), for an array ys of shape (3, M)."""
    ks = 2 * np.pi * np.arange(L) / L
    k1, k2, k3 = [k.ravel() for k in np.meshgrid(ks, ks, ks, indexing="ij")]
    om2 = 2 * KH * (3 - np.cos(k1) - np.cos(k2) - np.cos(k3))
    nz = om2 > 1e-12
    out = []
    for c in range(0, ys.shape[1], 512):
        y = ys[:, c:c + 512]
        ph = np.cos(k1[nz, None] * y[0] + k2[nz, None] * y[1] + k3[nz, None] * y[2])
        out.append((ph / om2[nz, None]).sum(0) / L ** 3)
    return np.concatenate(out)


def lap3(q):
    return 6 * q - sum(np.roll(q, s, axis=a) for a in range(3) for s in (1, -1))


def run_cubic(L, h, ka, lmax, dt=0.05):
    q = np.zeros((L, L, L))
    p = np.zeros_like(q)
    src = np.zeros_like(q)
    src[0, 0, 0] = 1.0
    hh = tuple(v % L for v in h)

    def acc(qq):
        a = -KH * lap3(qq) - src
        a[hh] -= ka * qq[hh]
        return a

    n = int(round(lmax / dt))
    U = np.zeros(n + 1)
    for m in range(1, n + 1):
        k1q, k1p = p, acc(q)
        k2q, k2p = p + 0.5 * dt * k1p, acc(q + 0.5 * dt * k1q)
        k3q, k3p = p + 0.5 * dt * k2p, acc(q + 0.5 * dt * k2q)
        k4q, k4p = p + dt * k3p, acc(q + dt * k3q)
        q = q + dt / 6 * (k1q + 2 * k2q + 2 * k3q + k4q)
        p = p + dt / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
        U[m] = q.mean()
    return np.arange(n + 1) * dt, U


def sparse_Ka(L, h, ka):
    one = sp.identity(L, format="csr")
    shift = sp.csr_matrix((np.ones(L), (np.arange(L), (np.arange(L) + 1) % L)), shape=(L, L))
    lap1 = 2 * one - shift - shift.T
    lap = (sp.kron(sp.kron(lap1, one), one) + sp.kron(sp.kron(one, lap1), one)
           + sp.kron(sp.kron(one, one), lap1))
    K = (KH * lap).tolil()
    ih = np.ravel_multi_index(tuple(v % L for v in h), (L, L, L))
    K[ih, ih] += ka
    return K.tocsc(), ih


def cubic_case(L, h, ka, lines, csv, tag):
    coords = np.array(np.unravel_index(np.arange(L ** 3), (L, L, L)))
    g0 = g_torus(L, np.zeros((3, 1)))[0]
    gsh = g_torus(L, -np.array(h, dtype=float)[:, None])[0]
    cphi = 1 / ka + g0
    Ust = -(cphi - gsh)
    TU = np.sqrt(L ** 3 * cphi)
    lam, U = run_cubic(L, h, ka, 2.2 * np.pi * TU)
    pred = Ust * (1 - np.cos(lam / TU))
    dev = np.max(np.abs(U - pred)) / abs(Ust)
    first = lam < 2 * np.pi * TU
    lmin = lam[first][np.argmin(U[first])]
    # lowest normal mode (independent, sparse shift-invert)
    K, ih = sparse_Ka(L, h, ka)
    nu, psi = eigsh(K, k=1, sigma=0, which="LM")
    nu0, psi0 = nu[0], psi[:, 0]
    A0 = psi0 * psi0[0] / nu0
    A0perp = A0 - A0.mean()
    beta = gsh / cphi
    gxh = g_torus(L, coords - np.array(h)[:, None] % L)
    img = -(1 - beta) * gxh
    dimg = np.max(np.abs(A0perp - img)) / np.max(np.abs(img))
    lines.append(f"  L={L:2d} kappa_a={ka} h-x_s={h}: c_phi^(L)={cphi:.5f} U_st={Ust:.5f} T_U={TU:.2f}; "
                 f"1/sqrt(nu_0)={1/np.sqrt(nu0):.2f} (ratio {1/np.sqrt(nu0)/TU:.5f}); "
                 f"max|U-pred|/|U_st|={dev:.2e} (x L = {dev*L:.4f}); "
                 f"first minimum at l/(pi T_U)={lmin/(np.pi*TU):.4f}, U_min/U_st={U[first].min()/Ust:.4f}; "
                 f"U(2 pi T_U)/U_st={np.interp(2*np.pi*TU, lam, U)/Ust:+.4f}; "
                 f"slow image: max|A0perp+(1-beta)g(x-h)|/max|.|={dimg:.2e} (x L^2 = {dimg*L*L:.2f}), beta_L={beta:.4f}")
    for j in range(0, len(lam), 20):
        csv.append(f"3,{tag},{L},{ka},{lam[j]:.3f},{U[j]:.6e},{pred[j]:.6e}")


def fext(x):
    y = np.mod(x + 1, 2) - 1  # in [-1, 1)
    return np.where(y >= 0, y * (1 - y), y * (1 + y))


def ring_case(L, lines, csv, ka=1.0):
    ds = L // 4
    i = np.arange(L)
    K = np.zeros((L, L))
    K[i, i] = 2 * KH
    K[i, (i + 1) % L] = -KH
    K[i, (i - 1) % L] = -KH
    K[ds, ds] += ka
    w2, V = np.linalg.eigh(K)
    tau = np.linspace(0, 4, 2001)
    lam = tau * L / C0
    U = -((V.sum(0) / L) * V[0] / w2) @ (1 - np.cos(np.sqrt(w2)[:, None] * lam[None, :]))
    alpha = ds / L
    Uc = -(L / (2 * KH)) * (fext(alpha) - 0.5 * fext(alpha + tau) - 0.5 * fext(alpha - tau))
    Ust = -(1 / ka + ds * (L - ds) / (2 * KH * L))
    dev = np.max(np.abs(U - Uc)) / abs(Ust)
    dev1 = np.max(np.abs(U - Uc)[tau <= 2]) / abs(Ust)
    first = tau < 2
    tmin = tau[first][np.argmin(U[first])]
    lines.append(f"  L={L:3d} d_s={ds}: U_st={Ust:.3f}; max|U-U_cont|/|U_st| over tau<=2: {dev1:.4f} (x L = {dev1*L:.2f}), "
                 f"over tau<=4: {dev:.4f}; first minimum at c0 l/L = {tmin:.4f} (pred 1), U_min/U_st={U[first].min()/Ust:.4f} (pred 2); "
                 f"U(c0 l = 2L)/U_st = {np.interp(2.0, tau, U)/Ust:+.4f} (pred 0)")
    for j in range(0, len(tau), 4):
        csv.append(f"1,ring,{L},{ka},{lam[j]:.3f},{U[j]:.6e},{Uc[j]:.6e}")


def ring_weak(L, ka, lines, csv):
    ds = L // 4
    i = np.arange(L)
    K = np.zeros((L, L))
    K[i, i] = 2 * KH
    K[i, (i + 1) % L] = -KH
    K[i, (i - 1) % L] = -KH
    K[ds, ds] += ka
    w2, V = np.linalg.eigh(K)
    cphi = 1 / ka + (L * L - 1) / (12 * KH * L)
    TU = np.sqrt(L * cphi)
    Ust = -(1 / ka + ds * (L - ds) / (2 * KH * L))
    lam = np.linspace(0, 2.2 * np.pi * TU, 4001)
    U = -((V.sum(0) / L) * V[0] / w2) @ (1 - np.cos(np.sqrt(w2)[:, None] * lam[None, :]))
    pred = Ust * (1 - np.cos(lam / TU))
    dev = np.max(np.abs(U - pred)) / abs(Ust)
    lines.append(f"  L={L} kappa_a={ka} (kappa_a L/kappa_h = {ka*L/KH:.3f}): T_U={TU:.1f} (wrap L/c0 = {L/C0:.0f}), "
                 f"1/sqrt(nu_0)/T_U = {1/np.sqrt(w2[0])/TU:.5f}, max|U-pred|/|U_st| = {dev:.4f}")
    for j in range(0, len(lam), 8):
        csv.append(f"1,ring_weak,{L},{ka},{lam[j]:.3f},{U[j]:.6e},{pred[j]:.6e}")


def main():
    lines = ["Check (iii): the uniform part (item 3)", f"kappa_h = {KH}, c_0 = {C0}", "",
             "CUBIC TORUS, kappa_a = 1, h - x_s = (2,1,0): prediction (9.14)"]
    csv = ["D,case,L,kappa_a,lambda,U_exact,U_pred"]
    for L in (8, 12, 16, 20):
        cubic_case(L, (2, 1, 0), 1.0, lines, csv, "sizes")
    lines.append("CUBIC TORUS, L = 12: anchor farther and stiffer anchor")
    cubic_case(12, (5, 4, 3), 1.0, lines, csv, "far_anchor")
    cubic_case(12, (2, 1, 0), 4.0, lines, csv, "kappa_a_4")
    lines += ["", "RING, kappa_a = 1, d_s = L/4: prediction (9.15)"]
    for L in (128, 256, 512):
        ring_case(L, lines, csv)
    lines += ["", "RING, weak anchor kappa_a L << kappa_h: slow-mode form (9.14) with c_phi^(L) = 1/kappa_a + (L^2-1)/(12 kappa_h L)"]
    for L, ka in ((32, 0.004), (64, 0.002), (64, 0.0005)):
        ring_weak(L, ka, lines, csv)
    (OUT / "uniform_check.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (OUT / "uniform_U.csv").write_text("\n".join(csv) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
