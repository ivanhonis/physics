"""Check (ii) of 07-bond-inertia: bound level E_b(P) and its curvature from the exact
diagonalization of the effective joint contract (7.2)-(7.4) in the sector P, against
the formulas (7.10)-(7.14) of item 2.

Ring of L cells; bodies (sigma1, sigma2) = (+,+) and (+,-) with rest costs M1, M2 of their
levels, tau = 1; field c0 = tau/r, m_h = c0/ell.  The members are heavy, abar*M_k > Omega_max
(square grip) and > Omega_max/2 (linear grip), Omega_max = max_q omega_q, for every r used:
no member in the branch + can decay with one or two quanta (condition (7.15), range (N_h)).
The bound levels are then not isolated (2 sum_{sigma_i=+} Mbar_i + dE > m_h): the curvature
checked is that of the formal second-order coefficients.  Grips: square (4 F0 F2 = F1^2) and linear (F2 = 0).
F1 is set (proportional to c0) so that the static bond is the same for every r; two
binding strengths: a 'deep' one (a_b < ell) and a 'shallow' one (a_b > ell).
Self-energies of the single bodies are not included (they cancel in D at this order).
Sectors of the periodic ring: the joint label is P = 2 pi m / L (m integer) and the sector is
spanned by the allowed labels p1 = 2 pi n / L, p2 = P - p1 (n = 0..L-1); no twisted labels.
"""
import json
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.linalg import eigh

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
AIRY1 = 1.0187929716  # first zero of Ai'


def setup(L, ell, r, tau, M1, M2, F0, F1, F2, sg1=1, sg2=1):
    c0 = tau / r; mh = c0 / ell; kap = c0**2
    n = np.arange(L); qs = 2 * np.pi * n / L
    om = np.sqrt(mh**2 + 4 * kap * np.sin(qs / 2)**2)
    w0 = np.sum(1 / (2 * L * om)); abar = F0 + F2 * w0
    Mb1, Mb2 = abar * M1, abar * M2
    I1, I2 = sg1 * Mb1 / tau**2, sg2 * Mb2 / tau**2          # signed inertias (7.1)
    return dict(L=L, n=n, om=om, c0=c0, mh=mh, kap=kap, tau=tau, r=r, M1=M1, M2=M2,
                F0=F0, F1=F1, F2=F2, Mb1=Mb1, Mb2=Mb2, I1=I1, I2=I2, I=I1 + I2,
                mred=I1 * I2 / (I1 + I2), mu12=sg1 * sg2 * M1 * M2, sg1=sg1, sg2=sg2,
                rest=sg1 * Mb1 + sg2 * Mb2)


def hamiltonian(P, s, static=False):
    L, n, om, tau = s["L"], s["n"], s["om"], s["tau"]
    ks = 2 * np.pi * n / L
    p1 = ks; p2 = P - ks                     # allowed ring labels; P is a multiple of 2 pi / L
    e1 = s["sg1"] * np.sqrt(s["Mb1"]**2 + tau**2 * np.sin(p1)**2)
    e2 = s["sg2"] * np.sqrt(s["Mb2"]**2 + tau**2 * np.sin(p2)**2)
    th1 = np.arctan2(tau * np.sin(p1), s["Mb1"]); th2 = np.arctan2(tau * np.sin(p2), s["Mb2"])
    if static:
        C = np.ones((L, L)); D1 = np.zeros((L, L)); D2 = np.zeros((L, L))
    else:
        C = np.cos((th1[:, None] + th1[None, :]) / 2) * np.cos((th2[:, None] + th2[None, :]) / 2)
        D1 = e1[None, :] - e1[:, None]; D2 = e2[:, None] - e2[None, :]   # rows k', cols k
    m = (n[None, :] - n[:, None]) % L                                   # q = k - k'
    wq2 = om[m]**2
    U = -s["mu12"] * s["F1"]**2 * C / (2 * L) * (1 / (wq2 - D1**2) + 1 / (wq2 - D2**2))
    ratio = max(np.max(np.abs(D1) / np.sqrt(wq2)), np.max(np.abs(D2) / np.sqrt(wq2)))
    if s["F2"] != 0:
        for mi in range(L):
            kp = (n - mi) % L
            ob = om[(mi - n) % L]; Om = om + ob; w = Om / (om * ob)
            d2 = np.concatenate([D1[kp, n], D2[kp, n]])**2
            S = (1 / (Om[None, :]**2 - d2[:, None])) @ w
            U[kp, n] += -s["mu12"] * s["F2"]**2 * C[kp, n] / (2 * L**2) * (S[:L] + S[L:])
            ratio = max(ratio, np.sqrt(d2.max()) / Om.min())
    if static:
        return U, ratio                      # static mutual kernel only
    return U + np.diag(e1 + e2), ratio


def analyse(s, untwist=True):
    """untwist: choose m with (I1/I) m an integer, so that the relative label k = p1 - (I1/I) P
    runs over the same grid 2 pi n / L as at P = 0 (no twist of the relative motion)."""
    L, tau, r = s["L"], s["tau"], s["r"]
    h = (0.004 if s["mred"] < 0 else 0.015) * abs(s["I"]) * tau            # P <= 3h keeps the pair velocity P/I below 0.045 tau
    H0, ratio = hamiltonian(0.0, s)
    up = s["mred"] < 0                       # bound level above the band (mixed branches)
    sel = [L - 2, L - 1] if up else [0, 1]
    E, V = eigh(H0, subset_by_index=sel)
    if up:
        E, V = E[::-1], V[:, ::-1]
    E0, psi = E[0], V[:, 0]
    dP = 2 * np.pi / L                       # spacing of the allowed joint labels
    per = Fraction(s["I1"] / s["I"]).limit_denominator(1000).denominator if untwist else 1
    mP = np.array([per * max(j, int(round(j * h / (dP * per)))) for j in (1, 2, 3)])
    twist = [float(abs(s["I1"] / s["I"] * m - round(s["I1"] / s["I"] * m))) for m in mP]
    Ps = dP * mP; EP = []
    for P in Ps:
        HP, rt = hamiltonian(P, s); ratio = max(ratio, rt)
        j = L - 1 if up else 0
        EP.append(eigh(HP, eigvals_only=True, subset_by_index=[j, j])[0])
    EP = np.array(EP)
    A = np.stack([Ps**2, Ps**4, Ps**6], axis=1)
    a, b, c = np.linalg.solve(A, EP - E0)
    Ipair = 1 / (2 * a)
    # relative label measured from the nearest band minimum (0 or pi: the two valleys of Model D)
    ks = 2 * np.pi * s["n"] / L; ks = (ks + np.pi / 2) % np.pi - np.pi / 2
    T = np.sum(np.abs(psi)**2 * ks**2) / (2 * s["mred"])
    w_pi = np.sum(np.abs(psi[np.abs(2 * np.pi * s["n"] / L - np.pi) < np.pi / 2])**2)
    dE = E0 - s["rest"]
    Ust, _ = hamiltonian(0.0, s, static=True)     # static kernel U~(k-k')/L
    Uexp = psi @ Ust @ psi
    Uq = L * Ust[0, :]                             # U~(q) at q = 2 pi j / L
    Ur = np.real(np.fft.ifft(Uq))                  # U(r), r = 0..L-1
    rr = np.where(s["n"] > L // 2, s["n"] - L, s["n"])
    rUp = rr * (np.roll(Ur, -1) - np.roll(Ur, 1)) / 2
    psir = np.fft.ifft(psi) * np.sqrt(L)           # psi(r) = L^-1/2 sum_k psi_k e^{ikr}
    rUp_exp = np.sum(np.abs(psir)**2 * rUp)
    I1, I2 = s["I1"], s["I2"]
    D_num = Ipair - I1 - I2
    D_formula = ((2 - r**2) * dE + (1 - r**2) * T) / tau**2 + 4 * I1 * I2 * T
    D_general = (3 * T + 2 * Uexp) / tau**2 - (Uexp + rUp_exp) / s["c0"]**2 + 4 * I1 * I2 * T
    lam = s["mu12"] * s["F1"]**2 / (2 * s["kap"])
    g = -Uq[0]
    rad = np.sqrt(np.sum(np.abs(psir)**2 * rr**2))
    Om_max = float(np.max(s["om"]))
    thr = Om_max if s["F2"] != 0 else Om_max / 2          # no-decay threshold (7.15), heavy range
    Mplus = [Mb for Mb, sg in ((s["Mb1"], s["sg1"]), (s["Mb2"], s["sg2"])) if sg > 0]
    decay_margin = min(Mb - thr for Mb in Mplus)          # > 0: no decay with one or two quanta
    isol_lhs = 2 * sum(Mplus) + dE - s["mh"]              # > 0: not isolated (necessary cond. fails)
    EPf = E0 + Ps**2 / (2 * (I1 + I2 + D_formula))
    return dict(r=r, F1=s["F1"], F2=s["F2"], ell=s["c0"] / s["mh"], L=L,
                branches=[s["sg1"], s["sg2"]], m_red=s["mred"],
                E_b0=E0, gap_to_next=abs(E[1] - E[0]), weight_pi_valley=w_pi, dE=dE, T=T,
                U_exp=Uexp, virial_2T=2 * T, virial_rUp=rUp_exp, rms_size=rad,
                dE_deep_asym=Ur[0] + np.sign(s["mred"]) * AIRY1
                * (lam**2 / (2 * abs(s["mred"])))**(1 / 3),
                dE_shallow_asym=-s["mred"] * g**2 / 2,
                I1=I1, I2=I2, I_pair=Ipair, D_num=D_num, D_formula=D_formula,
                D_general=D_general, D_deep_asym=(2 - r**2) * dE / tau**2,
                D_shallow_asym=dE / tau**2 - 4 * I1 * I2 * dE,
                rel_dev_D=abs(D_num - D_formula) / abs(D_formula),
                # D at first order in dE/M: I^2 (1/I - 1/I_pair) removes the trivial D^2/I term
                D_num_lin=(I1 + I2)**2 * (1 / (I1 + I2) - 1 / Ipair),
                dev_over_dE=abs(D_num - D_formula) / (abs(dE) / tau**2),
                dev_lin_over_dE=abs((I1 + I2)**2 * (1 / (I1 + I2) - 1 / Ipair) - D_formula)
                / (abs(dE) / tau**2),
                expected_scale=abs(dE) / abs(s["rest"]) + (tau / min(s["Mb1"], s["Mb2"]) / rad)**2,
                T_over_dE=T / dE,
                P=list(Ps), P_index_m=[int(x) for x in mP], relative_twist_over_2pi=twist,
                E_b_P_num=list(EP),
                E_b_P_formula=list(EPf), max_pair_velocity=float(Ps[-1] / abs(I1 + I2)),
                eps_J=2 * s["F2"]**2 * abs(np.log(s["c0"] / s["mh"] / rad))
                / (np.pi * s["F1"]**2 * s["c0"]),
                max_EP_dev_over_shift=float(np.max(np.abs(EP - EPf) / (EP - E0))),
                quartic_coeff=b, max_transfer_over_quantum=ratio,
                D_over_I=D_num / (I1 + I2), Omega_max=Om_max, decay_threshold=thr,
                decay_margin=decay_margin, isolation_lhs=isol_lhs,
                lattice_over_dE=4 * I1 * I2 * T / (dE / tau**2))


import sys
L = int(sys.argv[1]) if len(sys.argv) > 1 else 1024
ell = float(sys.argv[2]) if len(sys.argv) > 2 else 30.0
tau, M1, M2, F0 = 1.0, 5.0, 4.5, 1.0
results = []
t0 = time.time()
runs = [((1, 1), g) for g in ("square", "linear")] + [((1, -1), "linear")]
# (name, ell, target size a_b): deep a_b = ell/3; shallow a_b = 3 ell; very shallow a_b = 11 ell
regimes = [("deep", ell, ell / 3), ("shallow", ell, 3 * ell), ("v-shallow", 8.0, 88.0)]
for (sg1, sg2), grip in runs:
    mred0 = abs((M1 * M2 / (sg1 * M1 + sg2 * M2))) / tau**2
    for strength, ell_, ab in regimes:
        if sg1 != sg2 and strength == "v-shallow":
            continue
        for r in (0.5, 1.0, 1.4):
            c0 = tau / r; mh = c0 / ell_
            if strength == "deep":
                lam = 1 / (2 * mred0 * ab**3); F1 = c0 * np.sqrt(2 * lam / (M1 * M2))
            else:
                gg = 1 / (mred0 * ab); F1 = mh * np.sqrt(gg / (M1 * M2))
            F2 = F1**2 / (4 * F0) if grip == "square" else 0.0
            if (sg1, sg2, grip, strength, r) == (1, 1, "linear", "shallow", 1.0):
                F1_demo = F1
            # mixed branches: L_mixed = 3 L, so that 2 pi / L_mixed matches the small P they need
            s = setup(L if sg1 == sg2 else 3 * L, ell_, r, tau, M1, M2, F0, F1, F2, sg1, sg2)
            res = analyse(s); res.update(strength=strength, grip=grip)
            results.append(res)
            print(f"{sg1:+d}{sg2:+d} {strength:9s} {grip:6s} r={r:.2f} size={res['rms_size']:.1f} "
                  f"dE={res['dE']:.3e} T/dE={res['T_over_dE']:.3f} D_num={res['D_num']:.4e} "
                  f"D_lin={res['D_num_lin']:.4e} D_form={res['D_formula']:.4e} "
                  f"D_gen={res['D_general']:.4e} dev/dE={res['dev_over_dE']:.3f} "
                  f"devlin/dE={res['dev_lin_over_dE']:.3f} scale={res['expected_scale']:.3f} "
                  f"D/I={res['D_over_I']:.3f} EPdev={res['max_EP_dev_over_shift']:.3f} "
                  f"ratio={res['max_transfer_over_quantum']:.2f} gap={res['gap_to_next']:.2e} "
                  f"wpi={res['weight_pi_valley']:.2f} margin={res['decay_margin']:.3f} "
                  f"isol={res['isolation_lhs']:.3f} latt/dE={res['lattice_over_dE']:.3f} "
                  f"m={res['P_index_m']} L={s['L']} t={time.time() - t0:.0f}s", flush=True)
# finite-size demonstration: (+,+), shallow, linear grip, r = 1, with twisted joint labels
# (m not a multiple of the untwisting period) and untwisted ones, on rings of L and 2L cells
demo = []
for Lf in (L, 2 * L):
    s = setup(Lf, ell, 1.0, tau, M1, M2, F0, F1_demo, 0.0, 1, 1)
    for tw in (False, True):
        res = analyse(s, untwist=tw)
        demo.append({k: res[k] for k in ("L", "P_index_m", "relative_twist_over_2pi", "D_num",
                                         "D_formula", "rel_dev_D", "dE", "rms_size")}
                    | {"untwisted": tw})
        print("finite-size demo L", Lf, "untwisted", tw, "m", res["P_index_m"],
              "rel_dev_D", res["rel_dev_D"], flush=True)
summary = {"parameters": {"L": L, "L_mixed": 3 * L, "tau": tau, "M_k1": M1, "M_k2": M2, "F0": F0,
                          "regimes": regimes, "r": [0.5, 1.0, 1.4], "P": "2 pi m / L with m = per * max(j, round(j h L / (2 pi per))), j = 1, 2, 3, per the "
                          "smallest integer with (I1/I) per integer (untwisted relative label), "
                          "h = 0.015 |I| tau (+,+), 0.004 |I| tau (+,-); sector of allowed labels p1 = 2 pi n / L, p2 = P - p1"},
           "finite_size_demo": demo,
           "max_dev_lin_over_dE": max(x["dev_lin_over_dE"] for x in results),
           "max_dev_over_dE": max(x["dev_over_dE"] for x in results),
           "min_decay_margin": min(x["decay_margin"] for x in results),
           "min_isolation_lhs": min(x["isolation_lhs"] for x in results),
           "results": results}
(OUT / "bound_pair_check.json").write_text(json.dumps(summary, indent=1, default=float))
print("max dev/dE:", summary["max_dev_over_dE"], " max devlin/dE:", summary["max_dev_lin_over_dE"])
