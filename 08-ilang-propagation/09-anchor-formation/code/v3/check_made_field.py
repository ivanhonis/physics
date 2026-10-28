"""Check (i) of 09-anchor-formation: the made field of item 1.

Exact solution of the linear equations of the means (M -> infinity):
    d^2 q/dl^2 = -K_a q - e_{x_s},  q(0) = dq/dl(0) = 0,
computed from the eigen-decomposition of K_a = kappa_h*Lap + kappa_a*P_h.
It is compared with the derived expressions of item 1:
  (9.4) image representation: free torus kernels S_0, da_0 plus the image at the
        anchor with strength sigma_h from the Volterra equation;
  (9.5) uniform part (place average) from the force balance,
        U(l) = -L^{-D} int_0^l (l-l') [1 - sigma_h(l')] dl',
        and the static split (9.6) of (5.11).
Ring L = 64, 96 and cubic torus L = 8, 12; anchor at two distances; three places.
"""
from pathlib import Path
import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
KH, KA = 1.0, 1.0


def idx(c, L):
    return int(np.ravel_multi_index(tuple(int(v) % L for v in c), (L,) * len(c)))


def laplacian(L, D):
    N = L ** D
    grid = np.arange(N).reshape((L,) * D)
    lap = np.zeros((N, N))
    rows = np.arange(N)
    for ax in range(D):
        for sh in (1, -1):
            lap[rows, np.roll(grid, sh, axis=ax).ravel()] -= 1.0
    lap[rows, rows] += 2 * D
    return lap


def modes(L, D):
    ks = 2 * np.pi * np.arange(L) / L
    kk = np.meshgrid(*([ks] * D), indexing="ij")
    om2 = 2 * KH * sum(1 - np.cos(k) for k in kk)
    return [k.ravel() for k in kk], om2.ravel()


def free_kernels(y, t, kk, om2, L, D):
    """S_0(y,t) and da_0(y,t) on the torus (zero mode included)."""
    ph = np.cos(sum(k * yi for k, yi in zip(kk, y)))
    nz = om2 > 1e-12
    ph, w2 = ph[nz], om2[nz]
    S = np.zeros_like(t)
    A = np.zeros_like(t)
    for c in range(0, len(w2), 128):
        om = np.sqrt(w2[c:c + 128])[:, None]
        arg = om * t[None, :]
        S += (ph[c:c + 128, None] * np.sin(arg) / om).sum(0)
        A += (ph[c:c + 128, None] * (1 - np.cos(arg)) / om ** 2).sum(0)
    S = (S + t) / L ** D
    A = -(A + t ** 2 / 2) / L ** D
    return S, A


def run(D, L, xs, h, places, lines):
    N = L ** D
    lap = laplacian(L, D)
    K = KH * lap
    ih, isrc = idx(h, L), idx(xs, L)
    K[ih, ih] += KA
    w2, V = np.linalg.eigh(K)
    lmax = 3.0 * L
    dt = 0.005 if D == 3 else 0.01
    t = np.arange(0.0, lmax + dt / 2, dt)
    n = len(t)
    # --- derived: Volterra equation for sigma_h (trapezoid rule) ---
    kk, om2 = modes(L, D)
    S00, _ = free_kernels(np.zeros(D), t, kk, om2, L, D)
    _, A_hs = free_kernels(np.subtract(h, xs), t, kk, om2, L, D)
    f = -KA * A_hs
    sig = np.zeros(n)
    for m in range(1, n):
        conv = 0.5 * S00[m] * sig[0] + np.dot(S00[m - 1:0:-1], sig[1:m])
        sig[m] = f[m] - KA * dt * conv  # S00[0] = 0
    # evaluation times
    ev = np.linspace(0, n - 1, 241).astype(int)
    lam = t[ev]
    errs = []
    for p in places:
        ip = idx(p, L)
        exact = -(V[ip] * V[isrc] / w2) @ (1 - np.cos(np.sqrt(w2)[:, None] * lam[None, :]))
        S_ph, _ = free_kernels(np.subtract(p, h), t, kk, om2, L, D)
        _, A_ps = free_kernels(np.subtract(p, xs), t, kk, om2, L, D)
        img = np.array([dt * (np.dot(S_ph[m:0:-1], sig[:m]) + 0.5 * S_ph[0] * sig[m]
                              - 0.5 * S_ph[m] * sig[0]) if m > 0 else 0.0 for m in ev])
        derived = A_ps[ev] + img
        errs.append(np.max(np.abs(derived - exact)) / np.max(np.abs(exact)))
    # uniform part: exact place average vs force formula
    ones_proj = V.sum(0) / N
    U_exact = -(ones_proj * V[isrc] / w2) @ (1 - np.cos(np.sqrt(w2)[:, None] * lam[None, :]))
    g1 = 1.0 - sig
    U_der = []
    for m in ev:
        if m == 0:
            U_der.append(0.0)
            continue
        integ = (t[m] - t[:m + 1]) * g1[:m + 1]
        U_der.append(-dt * (integ.sum() - 0.5 * integ[0] - 0.5 * integ[-1]) / N)
    U_der = np.array(U_der)
    errU = np.max(np.abs(U_der - U_exact)) / np.max(np.abs(U_exact))
    # static split of (5.11)
    Ginv = V @ np.diag(1 / w2) @ V.T
    da_st = -Ginv[:, isrc]
    # g = (kappa_h Lap)^+ from the plane-wave modes (k = 0 excluded)
    nz = om2 > 1e-12
    coords = np.array(np.unravel_index(np.arange(N), (L,) * D))

    def g_of(y):  # y: array (D, M) of displacements
        ph = np.cos(sum(kk[a][nz, None] * y[a][None, :] for a in range(D)))
        return (ph / om2[nz, None]).sum(0) / N

    g_xh = g_of(coords - np.array(h)[:, None])
    g_xs = g_of(coords - np.array(xs)[:, None])
    g0 = g_of(np.zeros((D, 1)))[0]
    g_sh = g_of((np.array(h) - np.array(xs))[:, None])[0]
    r_sh = 2 * (g0 - g_sh)
    U_st_pred = -(1 / KA + r_sh / 2)
    perp_pred = g_xh - g_xs
    e_split = max(abs(da_st.mean() - U_st_pred),
                  np.max(np.abs(da_st - da_st.mean() - perp_pred))) / np.max(np.abs(da_st))
    # Bohr mean of sigma_h -> 1 (static image strength on the torus)
    sig_static = -KA * da_st[ih]
    lines.append(f"D={D} L={L} xs={tuple(xs)} h={tuple(h)} |h-xs|={np.linalg.norm(np.subtract(h, xs)):.3f} "
                 f"lambda_max={lmax:.0f} dt={dt}")
    for p, e in zip(places, errs):
        lines.append(f"   place {tuple(p)}: max|derived(9.4)-exact|/max|exact| = {e:.2e}")
    lines.append(f"   uniform part (9.5) force formula vs exact place average: rel. err = {errU:.2e}")
    lines.append(f"   static split (9.6): rel. err = {e_split:.2e};  static image strength -kappa_a*da_st(h) = {sig_static:.12f}")
    return max(errs + [errU, e_split])


def main():
    lines = ["Check (i): made field of item 1 against the exact solution of the means",
             f"kappa_h = {KH}, kappa_a = {KA}, c_0 = sqrt(kappa_h) = {np.sqrt(KH)}", ""]
    worst = 0.0
    for L in (64, 96):
        for h in ((3,), (17,)):
            worst = max(worst, run(1, L, (0,), h, [(-6,), (4,), (11,)], lines))
    for L in (8, 12):
        for h in ((1, 1, 0), (3, 2, 1)):
            worst = max(worst, run(3, L, (0, 0, 0), h, [(2, 0, 0), (1, -2, 1), (-3, 1, 2)], lines))
    lines += ["", f"largest relative deviation over all cases: {worst:.2e}"]
    (OUT / "made_field_check.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
