"""Check (ii) of 09-anchor-formation: formation of the place-dependent part (item 2).

Exact solution of the linear equations of the means (M -> infinity),
    d^2 q/dl^2 = -K_a q - e_{x_s},  q(0) = dq/dl(0) = 0,  K_a = kappa_h*Lap + kappa_a*P_h,
in the window below the wrap time (emulating L -> infinity first):
  cubic torus L = 64, 96 by fourth-order Runge-Kutta (dt = 0.05; one run repeated with dt = 0.1);
  ring L = 1024, 2048 by the eigen-decomposition of K_a.
Cubic torus: Delta_3^perp(rho, l) = da^perp(x,l) / ref - 1 at x = x_s + rho e_1 in order (O1):
  da^perp = da - U with the place average U -> 0 at fixed l as L -> infinity (U = O(l^2/L^3) is
  printed; the field da(x,l) itself is L-independent in the window, see the size check),
  ref = g_inf(x-h) - g_inf(x-x_s) (L -> infinity limit of the place-dependent part of (5.11)),
  compared with (9.11): limit -1 (w<1), 1/(b-1) (w>1), b = |x-h|/rho; finite-rho value of the
  plateau -g_inf(x-h)/ref.  Anchor far (antipode) and near (h = x_s - 8 e_1).
  Wakes: max over 1.3 < w <= w_max of |Delta_3^perp - pred(finite rho)| = |u_0 + I|/|ref| and the w of the maximum;
  for the far anchor (free field in the window) the free-field wake max|u_0|/g_inf(rho e_1), i.e. the far-from-anchor
  limit of |Delta_3^perp| (Step 7), over w > 1.3 and over the common window 1.3 < w <= 2.5; for the near anchor the
  image part max|I|/|ref| with I = da(near) - da(far), and |u_0|/|ref| at the w of the wake maximum.
  Also printed: the end of the window w_max = c0*l_max/rho (all formation times are finite-window
  values), and the lambda-mean of Delta_3^perp in order (O1), (beta-1) g_inf(x-h)/ref with
  beta = g_inf(x_s-h)/c_phi (the static field on Z^3 with the anchor), used by the negative part of (9.11).
  Above the threshold kappa_h/gamma_3 = 3.957 (localized mode): kappa_a = 8, near anchor, L = 64; the
  localized mode (nu_b from 1 + kappa_a gamma_b(0) = 0 on Z^3 and from a sparse eigen-solver, its share
  psi_b(x)psi_b(x_s)/nu_b), and the image term I = da(near) - da(far) in the window (the far-anchor field is
  the free field there) for kappa_a = 1 and 8, scaled by d_x d_s^(1/6) as in (9.18).
Ring: Delta_1(rho, l) = grad da / grad da_st - 1 between source and anchor, gradient toward the anchor,
  reference 1/kappa_h (L -> infinity limit), compared with (9.13): -1, -1/2 for 1<w<2a-1, 0 after;
  also max|Delta_1| for w > 1.4 and the range of Delta_1 across the image front (2.6 < w < 3.4).
  Uniform form of Step 8: sup over the window of kappa_h |grad da - F(rho) - F(m)|, m = 2 d_s - rho - 1, with
  F(n,l) = (2 kappa_h)^-1 int_0^{2 c0 l} J_{2n+1}(u) du (trapezoid rule; checked against the free-ring
  gradient), for kappa_a = 0.25, 1, 4, a = 2,
  c0 l <= 8 rho; the localized eigenvalue against 2 kappa_h + sqrt(4 kappa_h^2 + kappa_a^2).
"""
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import ive, jv
from scipy.optimize import brentq
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
KH, KA = 1.0, 1.0
C0 = np.sqrt(KH)


def g_inf(x):
    """Lattice Green function of kappa_h*Lap on Z^3: int_0^inf prod_i e^{-2t} I_{x_i}(2t) dt."""
    n = [abs(int(v)) for v in x]
    f = lambda u: np.exp(u) * ive(n[0], 2 * np.exp(u)) * ive(n[1], 2 * np.exp(u)) * ive(n[2], 2 * np.exp(u))
    umax = 19.0  # ive is unreliable beyond argument ~1e9
    pts = [np.log(max(sum(v * v for v in n), 1) / 6.0)]
    val = quad(f, -20, umax, points=pts, limit=800, epsabs=1e-14, epsrel=1e-11)[0]
    val += 2.0 / (4 * np.pi) ** 1.5 / np.sqrt(np.exp(umax))  # tail (4 pi t)^{-3/2}
    return val / KH


def lap3(q):
    return 6 * q - sum(np.roll(q, s, axis=a) for a in range(3) for s in (1, -1))


def run_cubic(L, h, rhos, lmax, dt, ka=KA):
    q = np.zeros((L, L, L))
    p = np.zeros_like(q)
    src = np.zeros_like(q)
    src[0, 0, 0] = 1.0
    hh = tuple(v % L for v in h)

    def acc(qq):
        a = -KH * lap3(qq) - src
        a[hh] -= ka * qq[hh]
        return a

    nsteps = int(round(lmax / dt))
    lam = np.arange(nsteps + 1) * dt
    rec = np.zeros((len(rhos), nsteps + 1))
    U = np.zeros(nsteps + 1)
    for m in range(1, nsteps + 1):
        k1q, k1p = p, acc(q)
        k2q, k2p = p + 0.5 * dt * k1p, acc(q + 0.5 * dt * k1q)
        k3q, k3p = p + 0.5 * dt * k2p, acc(q + 0.5 * dt * k2q)
        k4q, k4p = p + dt * k3p, acc(q + dt * k3q)
        q = q + dt / 6 * (k1q + 2 * k2q + 2 * k3q + k4q)
        p = p + dt / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
        rec[:, m] = [q[r % L, 0, 0] for r in rhos]
        U[m] = q.mean()
    return lam, rec, U


def form_lambda(lam, Delta, eps):
    bad = np.nonzero(np.abs(Delta) > eps)[0]
    if len(bad) == 0:
        return lam[0]
    if bad[-1] == len(lam) - 1:
        return np.inf
    return lam[bad[-1] + 1]


def cubic_part(lines, csv):
    rhos = [3, 4, 6, 8, 12, 16]
    lmax = 40.0
    lines.append("CUBIC TORUS (window below the wrap time; reference = L->infinity limit)")
    lines.append(f"  g_inf(0) = {g_inf((0, 0, 0)):.7f} (gamma_3/kappa_h = 0.2527310)")
    gr = {r: g_inf((r, 0, 0)) for r in rhos}
    cphi = 1.0 / KA + g_inf((0, 0, 0))
    store = {}
    for L in (64, 96):
        for name, h in (("far", (L // 2, L // 2, L // 2)), ("near", (-8, 0, 0))):
            lam, rec, U = run_cubic(L, h, rhos, lmax, 0.05)
            store[(L, name)] = (lam, rec, U)
            beta = g_inf(h) / cphi
            lines.append(f"  L={L} anchor {name}: h-x_s={h}, |h-x_s|={np.linalg.norm(h):.2f}; "
                         f"finite-L place average U(lambda_max)={U[-1]:.3e} "
                         f"(-lambda_max^2/2L^3 = {-lmax**2/(2*L**3):.3e}; -> 0 in order (O1))")
            for i, r in enumerate(rhos):
                xh = np.array((r, 0, 0)) - np.array(h)
                gxh = g_inf(xh)
                ref = gxh - gr[r]
                b = np.linalg.norm(xh) / r
                D = rec[i] / ref - 1  # order (O1): U -> 0
                w = C0 * lam / r
                sel = (w > 1.6) & (w <= 3.0)
                plat = D[sel].mean()
                pred_fin = -gxh / ref
                mean_O1 = (beta - 1) * gxh / ref
                sw = w > 1.3
                dev = np.abs(D[sw] - pred_fin)  # = |u_0 + I| / |ref|
                jw = np.argmax(dev)
                wake, w_wake = dev[jw], w[sw][jw]
                if name == "far":  # in the window the far-anchor field is the free field: u_0 = da + g_inf(rho e_1)
                    rel = np.abs(rec[i] + gr[r]) / gr[r]
                    jf = np.argmax(rel[sw])
                    extra = (f"free-field wake max|u_0|/g_inf(rho e1): w>1.3 {rel[sw][jf]:.3f} at w={w[sw][jf]:.2f}, "
                             f"1.3<w<=2.5 {rel[sw & (w <= 2.5)].max():.3f}")
                else:  # image term I = da(near) - da(far), the far-anchor field being the free field in the window
                    I = rec[i] - store[(L, "far")][1][i]
                    w_img = (np.linalg.norm(h) + np.linalg.norm(xh)) / r
                    extra = (f"image part max_(w>1.3)|I|/|ref| {np.max(np.abs(I[sw])) / abs(ref):.3f} "
                             f"(image front at w={w_img:.2f}); |u_0|/|ref| at the wake maximum {abs(rec[i][sw][jw] - I[sw][jw] + gr[r]) / abs(ref):.3f}")
                lf = [form_lambda(lam, D, e) for e in (0.2, 0.3, 0.5)]
                lines.append(f"    rho={r:2d} b={b:6.2f}: plateau(1.6<w<=min(3,w_max))={plat:+.3f}  "
                             f"pred(finite rho) {pred_fin:+.3f}  pred 1/(b-1) {1/(b-1):+.3f}  "
                             f"wake max_(w>1.3)|D-pred| {wake:.3f} at w={w_wake:.2f}  {extra}  "
                             f"min D(w<0.6)={D[w < 0.6].min():+.3f}  lambda-mean (O1) {mean_O1:+.3f}  "
                             f"w_max={C0*lmax/r:.1f}  c0*l_form/rho within window (eps=.2,.3,.5) = " +
                             ", ".join("not formed" if np.isinf(x) else f"{C0*x/r:.2f}" for x in lf))
                for j in range(0, len(lam), 4):
                    csv.append(f"3,{L},{name},{r},{lam[j]:.3f},{D[j]:.6f}")
    # size independence below the wrap time and time-step check
    for name in ("far", "near"):
        a, b_ = store[(64, name)], store[(96, name)]
        d = np.max(np.abs(a[1] - b_[1]))
        lines.append(f"  size check ({name}): max_l,rho |da_64 - da_96| = {d:.2e} "
                     f"(max |da| = {np.max(np.abs(b_[1])):.2e})")
    lam, rec2, _ = run_cubic(64, (-8, 0, 0), rhos, lmax, 0.1)
    d = np.max(np.abs(rec2 - store[(64, "near")][1][:, ::2]))
    lines.append(f"  time-step check (L=64 near): max |da(dt=0.1) - da(dt=0.05)| = {d:.2e}")
    above_threshold(lines, csv, store, rhos, lmax, gr)


def gamma_b0(nu):
    """(nu - kappa_h Lap)^{-1}_{00} on Z^3 for nu > 12 kappa_h: int_0^inf e^{-(nu-12kh)t} ive(0,2kh t)^3 dt."""
    f = lambda t: np.exp(-(nu - 12 * KH) * t) * ive(0, 2 * KH * t) ** 3
    return quad(f, 0, np.inf, limit=800, epsabs=1e-13, epsrel=1e-11)[0]


def sparse_Ka(L, h, ka):
    one = sp.identity(L, format="csr")
    shift = sp.csr_matrix((np.ones(L), (np.arange(L), (np.arange(L) + 1) % L)), shape=(L, L))
    lap1 = 2 * one - shift - shift.T
    lap = (sp.kron(sp.kron(lap1, one), one) + sp.kron(sp.kron(one, lap1), one)
           + sp.kron(sp.kron(one, one), lap1))
    K = (KH * lap).tolil()
    ih =np.ravel_multi_index(tuple(v % L for v in h), (L, L, L))
    K[ih, ih] = K[ih, ih] + ka
    return K.tocsc()


def above_threshold(lines, csv, store, rhos, lmax, gr):
    L, h, ka8 = 64, (-8, 0, 0), 8.0
    lines.append(f"  ABOVE THRESHOLD: kappa_a = {ka8} > kappa_h/gamma_3 = {KH/g_inf((0,0,0)):.4f}; L={L}, near anchor h-x_s={h}")
    lam, rec8, U8 = run_cubic(L, h, rhos, lmax, 0.05, ka=ka8)
    nub_inf = brentq(lambda nu: gamma_b0(nu) - 1 / ka8, 12 * KH + 1e-6, 12 * KH + 10 * ka8)
    K = sparse_Ka(L, h, ka8)
    nu, psi = eigsh(K, k=1, which="LA")
    nub, psib = nu[0], psi[:, 0]
    lines.append(f"    localized mode: nu_b from 1 + kappa_a gamma_b(0) = 0 on Z^3: {nub_inf:.8f}; sparse eigen-solver (L=64): {nub:.8f}")
    cphi8 = 1.0 / ka8 + g_inf((0, 0, 0))
    beta8 = g_inf(h) / cphi8
    lam1, rec_far, _ = store[(L, "far")]
    rec_near1 = store[(L, "near")][1]
    i0 = np.ravel_multi_index((0, 0, 0), (L, L, L))
    for i, r in enumerate(rhos):
        xh = np.array((r, 0, 0)) - np.array(h)
        dx, ds = np.linalg.norm(xh), np.linalg.norm(h)
        gxh = g_inf(xh)
        ref = gxh - gr[r]
        b = dx / r
        D = rec8[i] / ref - 1
        w = C0 * lam / r
        plat = D[(w > 1.6) & (w <= 3.0)].mean()
        I8 = rec8[i] - rec_far[i]
        I1 = rec_near1[i] - rec_far[i]
        ix = np.ravel_multi_index((r % L, 0, 0), (L, L, L))
        share = psib[ix] * psib[i0] / nub
        lf = form_lambda(lam, D, 0.5)
        lines.append(f"    rho={r:2d} b={b:5.2f}: plateau={plat:+.3f}  pred(finite rho) {-gxh/ref:+.3f}  1/(b-1) {1/(b-1):+.3f}  "
                     f"lambda-mean (O1) {(beta8-1)*gxh/ref:+.3f} (beta={beta8:.4f})  min D(w<0.6)={D[w < 0.6].min():+.3f}  "
                     f"c0*l_form/rho (eps=.5, window) = {'not formed' if np.isinf(lf) else f'{C0*lf/r:.2f}'};  "
                     f"max_window|I|*d_x*d_s^(1/6): kappa_a=1 {np.max(np.abs(I1))*dx*ds**(1/6):.4f}, kappa_a=8 {np.max(np.abs(I8))*dx*ds**(1/6):.4f};  "
                     f"localized share psi_b(x)psi_b(x_s)/nu_b = {share:+.2e}")
        for j in range(0, len(lam), 4):
            csv.append(f"3,{L},near_ka8,{r},{lam[j]:.3f},{D[j]:.6f}")


def ring_eig(L, h):
    lap = np.zeros((L, L))
    i = np.arange(L)
    lap[i, i] = 2
    lap[i, (i + 1) % L] = -1
    lap[i, (i - 1) % L] = -1
    K = KH * lap
    K[h % L, h % L] += KA
    return np.linalg.eigh(K)


def ring_field(w2, V, sites, lam):
    c = 1 - np.cos(np.sqrt(w2)[:, None] * lam[None, :])
    return np.array([-(V[s % len(w2)] * V[0] / w2) @ c for s in sites])


def ring_part(lines, csv):
    lines.append("")
    lines.append("RING (exact eigen-decomposition; window below the wrap time; reference grad = 1/kappa_h)")
    lines.append("  (a) anchor at d_s = 2 rho (a = 2): prediction -1 (w<1), -1/2 (1<w<3), 0 (w>3)")
    for L in (1024, 2048):
        for r in (20, 40, 80, 160):
            ds = 2 * r
            w2, V = ring_eig(L, ds)
            lam = np.linspace(0, 4 * r / C0, 1601)
            f = ring_field(w2, V, (r, r + 1), lam)
            D = (f[1] - f[0]) * KH - 1
            w = C0 * lam / r
            p1 = D[(w > 1.4) & (w < 2.6)].mean()
            p2 = D[w > 3.4].mean()
            mx = np.max(np.abs(D[w > 1.4]))
            tr = D[(w > 2.6) & (w < 3.4)]
            lf = [form_lambda(lam, D, e) for e in (0.25, 0.6)]
            lines.append(f"    L={L} rho={r:3d}: plateau(1.4<w<2.6)={p1:+.3f}  plateau(w>3.4)={p2:+.3f}  "
                         f"max|D|(w>1.4)={mx:.3f}  D across image front (2.6<w<3.4) in [{tr.min():+.3f}, {tr.max():+.3f}]  "
                         f"c0*l_form/rho: eps=0.25 -> {C0*lf[0]/r:.2f} (pred 3), eps=0.6 -> {C0*lf[1]/r:.2f} (pred 1);"
                         f"  finite-L ref grad*kappa_h = {(L-ds)/L:.3f}")
            for j in range(0, len(lam), 8):
                csv.append(f"1,{L},a2,{r},{lam[j]:.3f},{D[j]:.6f}")
    lines.append("  (b) anchor far, d_s = 400: prediction -1/2 until c0*l = 2 d_s - rho, then 0")
    for L in (1024, 2048):
        ds = 400
        w2, V = ring_eig(L, ds)
        lam = np.linspace(0, 900 / C0, 3601)
        for r in (10, 20, 40, 80):
            f = ring_field(w2, V, (r, r + 1), lam)
            D = (f[1] - f[0]) * KH - 1
            sel = (lam > 1.4 * r / C0) & (lam < 0.9 * (2 * ds - r) / C0)
            lf = form_lambda(lam, D, 0.25)
            lines.append(f"    L={L} rho={r:3d}: mean D on 1.4 rho < c0 l < 0.9(2d_s-rho) = {D[sel].mean():+.3f}, "
                         f"max|D+1/2| there = {np.max(np.abs(D[sel] + 0.5)):.3f};  c0*l_form(eps=0.25) = "
                         f"{C0*lf:.1f} (pred 2d_s-rho = {2*ds-r}), c0*l_form/rho = {C0*lf/r:.1f}")
            for j in range(0, len(lam), 8):
                csv.append(f"1,{L},far,{r},{lam[j]:.3f},{D[j]:.6f}")


def F_bessel(n, lam):
    """Free gradient on the line: (2 kappa_h)^-1 int_0^{2 c0 l} J_{2n+1}(u) du (trapezoid rule, step 0.004)."""
    X = 2 * C0 * lam
    u = np.linspace(0, X.max(), int(X.max() / 0.004) + 2)
    J = jv(2 * n + 1, u)
    cum = np.concatenate(([0.0], np.cumsum(0.5 * (J[1:] + J[:-1]) * np.diff(u))))
    return np.interp(X, u, cum) / (2 * KH)


def F_free_ring(n, lam, L):
    """Free gradient at place n on the ring without anchor (zero mode removed), by the mode sum."""
    ks = 2 * np.pi * np.arange(1, L) / L
    om = 2 * C0 * np.abs(np.sin(ks / 2))
    amp = (np.exp(1j * ks) - 1) * np.exp(1j * ks * n) / om ** 2
    out = np.zeros_like(lam)
    for c in range(0, len(ks), 256):
        out -= (amp[c:c + 256, None] * (1 - np.cos(om[c:c + 256, None] * lam[None, :]))).sum(0).real
    return out / L


def ring_uniform(lines):
    lines.append("  (c) uniform form of Step 8: sup_window kappa_h|grad da - F(rho) - F(m)|, a = 2, m = 3 rho - 1, c0 l <= 8 rho, L = 2048")
    L = 2048
    Fcache = {}
    bess = []
    for ka in (0.25, 1.0, 4.0):
        row = []
        for r in (20, 40, 80, 160):
            ds = 2 * r
            i = np.arange(L)
            K = np.zeros((L, L))
            K[i, i] = 2 * KH
            K[i, (i + 1) % L] = -KH
            K[i, (i - 1) % L] = -KH
            K[ds, ds] += ka
            w2, V = np.linalg.eigh(K)
            lam = np.linspace(0, 8 * r / C0, 3201)
            f = ring_field(w2, V, (r, r + 1), lam)
            grad = f[1] - f[0]
            m = 2 * ds - r - 1
            if r not in Fcache:
                Fr, Fm = F_bessel(r, lam), F_bessel(m, lam)
                dF = max(np.max(np.abs(Fr - F_free_ring(r, lam, L))), np.max(np.abs(Fm - F_free_ring(m, lam, L)))) * KH
                Fcache[r] = (Fr, Fm, dF)
            Fr, Fm, dF = Fcache[r]
            dev = np.max(np.abs(grad - Fr - Fm)) * KH
            row.append(f"rho={r}: {dev:.4f}")
            if ka == 1.0:
                bess.append(f"rho={r}: {dF:.1e}")
            if r == 160:
                nub = w2[-1]
        lines.append(f"    kappa_a={ka}: " + ";  ".join(row) + f";  localized eigenvalue {nub:.6f} vs 2kh+sqrt(4kh^2+ka^2) = {2*KH+np.sqrt(4*KH**2+ka**2):.6f}")
    lines.append("    Bessel form of F (n = rho and m) against the free-ring gradient, max kappa_h|diff|: " + ";  ".join(bess))


def main():
    lines = ["Check (ii): formation of the place-dependent part (item 2)",
             f"kappa_h = {KH}, kappa_a = {KA}, c_0 = {C0}", ""]
    csv = ["D,L,anchor,rho,lambda,Delta"]
    cubic_part(lines, csv)
    ring_part(lines, csv)
    ring_uniform(lines)
    (OUT / "formation_check.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (OUT / "formation_Delta.csv").write_text("\n".join(csv) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
