"""Check (ii) of 07-bond-inertia: bound level E_b(P) and its curvature from the exact
diagonalization of the effective joint contract (7.2)-(7.4) in the sector P, against
the formulas (7.10)-(7.14) of item 2.

Ring of L cells; bodies (sigma1, sigma2) = (+,+) with rest costs M1, M2 of their levels,
tau = 1; field c0 = tau/r, m_h = c0/ell.  Grips: square (4 F0 F2 = F1^2) and linear (F2 = 0).
F1 is set (proportional to c0) so that the static bond is the same for every r; two
binding strengths: a 'deep' one (a_b < ell) and a 'shallow' one (a_b > ell).
Self-energies of the single bodies are not included (they cancel in D at this order).
"""
import json
import time
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
    p1 = P * s["I1"] / s["I"] + ks; p2 = P * s["I2"] / s["I"] - ks
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


def analyse(s):
    L, tau, r = s["L"], s["tau"], s["r"]
    h = 0.015 * abs(s["I"]) * tau            # P <= 3h keeps the pair velocity P/I below 0.045 tau
    H0, ratio = hamiltonian(0.0, s)
    up = s["mred"] < 0                       # bound level above the band (mixed branches)
    sel = [L - 2, L - 1] if up else [0, 1]
    E, V = eigh(H0, subset_by_index=sel)
    if up:
        E, V = E[::-1], V[:, ::-1]
    E0, psi = E[0], V[:, 0]
    Ps = h * np.arange(1, 4); EP = []
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
                P=list(Ps), E_b_P_num=list(EP), E_b_P_formula=list(EPf),
                max_EP_dev_over_shift=float(np.max(np.abs(EP - EPf) / (EP - E0))),
                quartic_coeff=b, max_transfer_over_quantum=ratio,
                D_over_I=D_num / (I1 + I2))


import sys
L = int(sys.argv[1]) if len(sys.argv) > 1 else 1024
ell = float(sys.argv[2]) if len(sys.argv) > 2 else 30.0
tau, M1, M2, F0 = 1.0, 0.5, 0.4, 1.0
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
            s = setup(L, ell_, r, tau, M1, M2, F0, F1, F2, sg1, sg2)
            res = analyse(s); res.update(strength=strength, grip=grip)
            results.append(res)
            print(f"{sg1:+d}{sg2:+d} {strength:9s} {grip:6s} r={r:.2f} size={res['rms_size']:.1f} "
                  f"dE={res['dE']:.3e} T/dE={res['T_over_dE']:.3f} D_num={res['D_num']:.4e} "
                  f"D_lin={res['D_num_lin']:.4e} D_form={res['D_formula']:.4e} "
                  f"D_gen={res['D_general']:.4e} dev/dE={res['dev_over_dE']:.3f} "
                  f"devlin/dE={res['dev_lin_over_dE']:.3f} scale={res['expected_scale']:.3f} "
                  f"D/I={res['D_over_I']:.3f} EPdev={res['max_EP_dev_over_shift']:.3f} "
                  f"ratio={res['max_transfer_over_quantum']:.2f} gap={res['gap_to_next']:.2e} "
                  f"wpi={res['weight_pi_valley']:.2f} t={time.time() - t0:.0f}s", flush=True)
summary = {"parameters": {"L": L, "tau": tau, "M_k1": M1, "M_k2": M2, "F0": F0,
                          "regimes": regimes, "r": [0.5, 1.0, 1.4], "P": "h, 2h, 3h with h = 0.015 |I| tau"},
           "max_dev_lin_over_dE": max(x["dev_lin_over_dE"] for x in results),
           "max_dev_over_dE": max(x["dev_over_dE"] for x in results),
           "results": results}
(OUT / "bound_pair_check.json").write_text(json.dumps(summary, indent=1, default=float))
print("max dev/dE:", summary["max_dev_over_dE"], " max devlin/dE:", summary["max_dev_lin_over_dE"])
