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
  Also printed: the end of the window w_max = c0*l_max/rho (all formation times are finite-window
  values), and the lambda-mean of Delta_3^perp in order (O1), (beta-1) g_inf(x-h)/ref with
  beta = g_inf(x_s-h)/c_phi (the static field on Z^3 with the anchor), used by the negative part of (9.11).
Ring: Delta_1(rho, l) = grad da / grad da_st - 1 between source and anchor, gradient toward the anchor,
  reference 1/kappa_h (L -> infinity limit), compared with (9.13): -1, -1/2 for 1<w<2a-1, 0 after;
  also max|Delta_1| for w > 1.4 and the range of Delta_1 across the image front (2.6 < w < 3.4).
"""
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import ive

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


def run_cubic(L, h, rhos, lmax, dt):
    q = np.zeros((L, L, L))
    p = np.zeros_like(q)
    src = np.zeros_like(q)
    src[0, 0, 0] = 1.0
    hh = tuple(v % L for v in h)

    def acc(qq):
        a = -KH * lap3(qq) - src
        a[hh] -= KA * qq[hh]
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
                wake = np.max(np.abs(D[w > 1.3] - pred_fin))
                lf = [form_lambda(lam, D, e) for e in (0.2, 0.3, 0.5)]
                lines.append(f"    rho={r:2d} b={b:6.2f}: plateau(1.6<w<=min(3,w_max))={plat:+.3f}  "
                             f"pred(finite rho) {pred_fin:+.3f}  pred 1/(b-1) {1/(b-1):+.3f}  wake max_(w>1.3)|D-pred| {wake:.3f}  "
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


def main():
    lines = ["Check (ii): formation of the place-dependent part (item 2)",
             f"kappa_h = {KH}, kappa_a = {KA}, c_0 = {C0}", ""]
    csv = ["D,L,anchor,rho,lambda,Delta"]
    cubic_part(lines, csv)
    ring_part(lines, csv)
    (OUT / "formation_check.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (OUT / "formation_Delta.csv").write_text("\n".join(csv) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
