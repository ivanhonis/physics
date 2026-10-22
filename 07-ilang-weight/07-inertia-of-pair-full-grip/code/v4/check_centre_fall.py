"""Checks of v4 (07-inertia-of-pair-full-grip, N_f = 1, t_f = 1): parity classes and the fall in the fixed source.

Parts (command-line argument; default: all):
  classes  MODEL relative contract (6.1) with constant hop tb = -w^3 F/4 and potential B(r) = -2 F ell(r), on the
           even (r even) or odd (r odd) class: beta_0, <V>_0 and the bond average Bbar_0 = sum b_0 Bbar / beta_0
           against <M>_0 = sum f_0^2 B, narrow and broad pairs (Step 2, Step 4 (i)).
  fallS1, fallS1u  BAND contract (2.10) in laboratory coordinates with the fixed held source g Phi_{x_s}, L = 256:
           internal state u_P = e^{i Theta_P} v_P (phase slope theta(P) = arctan(nu tan P), width change), and the
           fall itself: time evolution of a start at rest in the selected band (real Gaussian envelope of width w_X in
           the centre), secular acceleration of the mean midpoint (j + h/2, local chart) at first order in g (odd part
           in +-g), against -E_b''(0) W_ex' and -<E_b''(P)> W_ex' (7.15); W_ex the P = 0 symbol (row sum).
Outputs: output/centre_fall_<part>.txt, output/centre_fall_<part>.json.
"""
import json
import sys
from pathlib import Path

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply

sys.path.insert(0, str(Path(__file__).parent))
from check_pair_full_grip import ell, curv, params, body_kappa, band_contract  # noqa: E402
from check_fixed_source import band_setup, band_rowsums, bloch_P, hsign, grad_X  # noqa: E402

OUT = Path(__file__).parent / "output"
LOG = []


def log(s=""):
    print(s, flush=True)
    LOG.append(s)


def part_classes():
    res = []
    F = 1.0
    B = lambda L, x: -2 * F * ell(L, x)
    for L in (6, 8, 64, 256):
        for par, cls in ((0, "even"), (1, "odd")):
            h = np.arange(par, L, 2)
            n = len(h)
            log(f"== MODEL class {cls}, L={L}")
            for w in (0.2, 0.35, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0):
                if w > L / 8:
                    continue
                H = np.diag(B(L, h))
                tb = -w ** 3 * F / 4
                for i in range(n):
                    H[i, (i + 1) % n] += tb
                    H[(i + 1) % n, i] += tb
                f = np.abs(np.linalg.eigh(H)[1][:, 0])
                rho = h + 1  # bond between h and h + 2
                b0 = f * np.roll(f, -1)
                beta0 = b0.sum()
                M = np.sum(f ** 2 * B(L, h))
                Bbar0 = np.sum(b0 * 0.25 * (B(L, rho - 1) + 2 * B(L, rho) + B(L, rho + 1))) / beta0
                V = M - B(L, 0)
                pred_beta = w ** 3 * L / (4 * (L - 2)) if par == 0 else 0.5
                pred_diff = (1 - 1.5 / L) if par == 0 else -(L - 1) / (2 * L)
                d = dict(L=L, cls=cls, w=w, beta0=beta0, V0_over_F=V / F, Bbar0_minus_M0_over_F=(Bbar0 - M) / F,
                         narrow_beta_pred=pred_beta, narrow_diff_pred=pred_diff, B0_over_F=B(L, 0) / F)
                res.append(d)
                log(f"   w={w:5.2f}: beta0={beta0:.4e} (narrow limit {pred_beta:.4e}), <V>_0/F={V / F:.4e}, "
                    f"(Bbar_0-<M>_0)/F={(Bbar0 - M) / F:+.4e} (narrow limit {pred_diff:+.4f}; times w: {w * (Bbar0 - M) / F:+.3f}), B(0)/F={B(L, 0) / F:.3f}")
    return res


def part_fall(name, p, runs, gs=1e-6):
    L, g1, g2, t1, t2 = params(*p)
    bs = band_setup(L, g1, g2, t1, t2)
    W, Ws, H0, dH, Fb, resid = band_rowsums(L, g1, g2, t1, t2, bs)
    ev, Ps, j = bs['ev'], bloch_P(L), np.arange(L)
    hr = hsign(L, ev).astype(float)
    mu = [-1 / (8 * body_kappa(L, g, t)) for g, t in ((g1, t1), (g2, t2))]
    nu = (mu[1] - mu[0]) / (mu[0] + mu[1])
    kk = band_contract(L, g1, g2, t1, t2)[3]
    m1, m2 = -1 / (8 * kk[0][1]), -1 / (8 * kk[1][1])  # local inertias (7.3) at the bond rho = 1
    nu_loc = (m2 - m1) / (m1 + m2)
    E2, E0 = curv(lambda P: bs['band'](P)[0], 0.02)
    log(f"== BAND {name}: L={L} g1={g1:.5g} g2={g2:.5g} tau1={t1:.4g} tau2={t2:.4g}; nu=(mu2-mu1)/(mu1+mu2)={nu:.4f}, local nu(1)={nu_loc:.4f}, "
        f"E_b''(0)={E2:.6e}, Bloch residual {resid:.1e}")
    g = {}
    for P in Ps:
        v = Fb[float(P)][1]
        g[float(P)] = v * np.exp(-1j * np.angle(v[0]))  # u_P(0) real positive
    u = {P: np.exp(-0.5j * P * hr) * v for P, v in g.items()}  # midpoint gauge
    h2_0 = float(np.sum(np.abs(u[0.0]) ** 2 * hr ** 2))
    w = float(np.sqrt(h2_0))
    res = dict(case=name, L=L, g1=g1, g2=g2, tau1=t1, tau2=t2, nu=nu, nu_local=nu_loc, Epp=E2, internal=[], fall=[])
    for k in (1, 2, 4):
        P = float(Ps[k])
        sel = (np.abs(hr) <= 2 * w) & (hr != 0)
        a = np.abs(u[P][sel]) ** 2
        th = float(np.sum(a * np.angle(u[P][sel]) * hr[sel] / 2) / np.sum(a * (hr[sel] / 2) ** 2))
        dw = float(np.sum(np.abs(u[P]) ** 2 * hr ** 2) / h2_0 - 1)
        pw = (1 - (1 - nu ** 2) * np.sin(P) ** 2) ** (1 / 3) - 1
        res['internal'].append(dict(P=P, theta=th, theta_pred=float(np.arctan(nu_loc * np.tan(P))), dh2=dw, dh2_pred=pw))
        if k == 1:
            nu_eff = np.tan(th) / np.tan(P)
        log(f"   internal state at P={P:.4f}: phase slope theta={th:.6e} (arctan(nu(1) tan P)={np.arctan(nu_loc * np.tan(P)):.6e}); "
            f"<h^2>_P/<h^2>_0-1={dw:.4e} (Airy scaling {pw:.4e}); sqrt<h^2>_0={w:.2f}")
    Epp = np.array([(bs['band'](P + 1e-2)[0] - 2 * bs['band'](P)[0] + bs['band'](P - 1e-2)[0]) / 1e-4 for P in Ps])
    Xpos = (j[:, None] + hr[None, :] / 2).ravel()
    Hrel = (H0 - E0 * sp.identity(H0.shape[0])).tocsr()
    for s, wX in runs:
        Y0 = L - s
        c = np.exp(-Ps ** 2 * wX ** 2 - 1j * Ps * Y0)
        psi = sum(c[a] * (np.exp(1j * P * j)[:, None] * g[float(P)][None, :]).ravel() for a, P in enumerate(Ps))
        psi = psi / np.linalg.norm(psi)
        Xc = Y0 + np.mod(Xpos - Y0 + L / 2, L) - L / 2
        Yc = Xc + np.tile(nu_eff * hr / 2, L)  # centre with the measured phase slope
        lmax = 1.5 * wX ** 2 / abs(E2)
        lam = np.linspace(0, lmax, 31)
        mX, mY = {}, {}
        for sg in (1, -1):
            S = expm_multiply(-1j * (Hrel + sg * gs * dH), psi, start=0, stop=lmax, num=31, endpoint=True)
            pr = np.abs(S) ** 2
            mX[sg], mY[sg] = pr @ Xc, pr @ Yc
        dX, dY = (mX[1] - mX[-1]) / (2 * gs), (mY[1] - mY[-1]) / (2 * gs)
        x = lam / lmax  # scaled for the least-squares fits
        A = np.stack([x ** 2, x ** 3, x ** 4], 1)
        aY = 2 * np.linalg.lstsq(A, dY, rcond=None)[0][0] / lmax ** 2  # centre: through the origin
        q = lam >= lmax / 4  # midpoint: secular part, offset for the bounded interband oscillation
        aX = 2 * np.linalg.lstsq(np.stack([np.ones(q.sum()), x[q] ** 2, x[q] ** 4], 1), dX[q], rcond=None)[0][1] / lmax ** 2
        Wp = grad_X(W, L, s)
        Wb = Wp - grad_X(Ws[0], L, s) - grad_X(Ws[1], L, s)
        pw = np.exp(-2 * Ps ** 2 * wX ** 2)
        Eavg = float(np.sum(pw * Epp) / np.sum(pw))
        pY = np.exp(-((j - Y0 + L / 2) % L - L / 2) ** 2 / (2 * wX ** 2))
        Wavg = float(np.sum(pY * (W[(j + 1) % L] - W[(j - 1) % L]) / 2) / np.sum(pY))
        a0, a1 = -E2 * Wp, -Eavg * Wavg
        d = dict(s=s, wX=wX, lam_max=lmax, a_midpoint=aX, a_centre=aY, a_pred=a0, a_pred_start_avg=a1,
                 Epp_start_avg=Eavg, Wex=Wp, Wex_start_avg=Wavg, Wb=Wb, bond_scale=E2 * Wb,
                 mean_X0=float(np.abs(psi) ** 2 @ Xc), rel_to_bond=(aX - a0) / abs(E2 * Wb),
                 rel_to_bond_start_avg=(aX - a1) / abs(E2 * Wb))
        res['fall'].append(d)
        log(f"   s={s}, w_X={wX}: lambda_max={lmax:.3e} (start mean {d['mean_X0']:.4f}); secular acceleration per unit g: "
            f"midpoint {aX:.6e} (fit c0 + c2 l^2 + c4 l^4 on [lmax/4, lmax]), centre (nu_eff={nu_eff:.4f}) {aY:.6e} (fit c2 l^2 + c3 l^3 + c4 l^4)")
        log(f"     (7.15) leading -E_b''(0) W_ex'(Y0)={a0:.6e}: ratio {aX / a0:.6f}, (a-pred)/|E_b'' W_b'|={(aX - a0) / abs(E2 * Wb):+.3e}")
        log(f"     with the start averages -<E_b''(P)> <W_ex'(Y)> ({Eavg / E2 - 1:+.2e}, {Wavg / Wp - 1:+.2e})={a1:.6e}: ratio {aX / a1:.6f}, "
            f"(a-pred)/|E_b'' W_b'|={(aX - a1) / abs(E2 * Wb):+.3e};  |W_b'/W_ex'|={abs(Wb / Wp):.4f}")
    return [res]


PARTS = {
    "classes": part_classes,
    "fallS1": lambda: part_fall("S1 equal bodies, regime (ii)", (256, 0.10, 1.0, 0.4), [(32, 6), (32, 8), (64, 8), (64, 12)]),
    "fallS1u": lambda: part_fall("S1u unequal bodies and speeds", (256, 0.10, 0.5, 0.4, 0.2), [(32, 8), (64, 8), (64, 12)]),
}

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for part in (sys.argv[1:] or list(PARTS)):
        LOG.clear()
        log(f"# part {part}")
        out = PARTS[part]()
        (OUT / f"centre_fall_{part}.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
        (OUT / f"centre_fall_{part}.json").write_text(json.dumps(out, indent=1, default=float), encoding="utf-8")
