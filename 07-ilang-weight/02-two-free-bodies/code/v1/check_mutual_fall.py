"""Check of item 3 (mutual fall) of 07-ilang-weight/02-two-free-bodies.

Two Model D bodies (each in one clock level, half-gap M_i, motion amplitude tau_i, branch sigma_i,
coupling (a) or (c) with constant gamma_i) and N_f = 1 field object on a ring of L places.
The total contract commutes with the joint translation, so it is diagonalized in the L sectors of the
total plane-wave label P (relative coordinates, field object at y = 0 in the representative).

Start: the product of real Gaussian envelopes phi1, phi2 in the adiabatic basis
|x1,sigma1,x2,sigma2> (x) Omega(x1,x2) (Omega = field state, lowest or highest, of the held problem),
projected on the isolated group of levels connected to it (the band), and normalized.
Exact accelerations at lambda = 0: a_i = i <[C, v_i]>, v_i = i[C, x_i] (minimal-image displacement).
Joint evolution: <v_i>(lambda) from the exact evolution inside the band, slope at 0 from a cubic fit.
Prediction (2.12): a_i = -E''_i sum w_i(j,l) d_i W(j,l), E''_i from the band of the single body with the
field (same parameters), W the exact held eigenvalue. Deviation dev_i = a_i/pred_i - 1 at
tau-scale s = 1, 1/2, 1/4, extrapolated to s -> 0 (coefficient of tau^2) and compared with the
in-situ estimate (2.16).
Output: output/mutual_fall.json and output/mutual_fall.log
"""
import json
from pathlib import Path

import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

L = 14
TF = 0.5
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S3 = np.diag([1.0, -1.0]).astype(complex)
I2 = np.eye(2)
IDX = {+1: 0, -1: 1}


def shift(L, k):
    """|x> -> |x+k>."""
    S = np.zeros((L, L))
    for x in range(L):
        S[(x + k) % L, x] = 1.0
    return S


def h_field(pts):
    H = -TF * (shift(L, 1) + shift(L, -1))
    for x, g in pts:
        H[x, x] += g
    return H


def field_state(pts, top):
    w, V = np.linalg.eigh(h_field(pts))
    if top:
        v, e = V[:, -1], w[-1]
        v = v * np.sign(np.sum(v * (-1.0) ** np.arange(L)))
    else:
        v, e = V[:, 0], w[0]
        v = v * np.sign(np.sum(v))
    return e, v


def body_ops(b):
    """Own term + coupling (field object at y = 0) and velocity of one body, on (x, s): index 2x+s."""
    M, tau, gam, cpl = b["M"], b["tau"], b["gamma"], b["coupling"]
    P0 = np.zeros((L, L)); P0[0, 0] = 1.0
    H = np.kron(np.eye(L), M * S3) + gam * M * np.kron(P0, S3)
    V = np.zeros((2 * L, 2 * L), dtype=complex)
    for x in range(L):
        f = 1.0
        if cpl == "c":
            f += gam * 0.5 * ((x == 0) + ((x + 1) % L == 0))
        E = np.zeros((L, L)); E[(x + 1) % L, x] = 1.0  # |x+1><x|
        H = H + 0.5 * tau * f * (np.kron(E, -1j * S1) + np.kron(E.T, 1j * S1))
        V = V - 0.5 * tau * f * (np.kron(E, S1) + np.kron(E.T, S1))
    return H, V


def single_band_curv(b, top):
    """E'' at the rest point of the band of one body with the field (N_f = 1)."""
    Hb, _ = body_ops(b)
    Sm = np.kron(shift(L, -1), I2)
    Sp = np.kron(shift(L, 1), I2)
    g = b["sigma"] * b["gamma"] * b["M"]
    _, om = field_state([(0, g)], top)
    Es = []
    for m in range(L):
        P = 2 * np.pi * m / L
        H = Hb - TF * (np.exp(-1j * P) * Sm + np.exp(1j * P) * Sp)
        w, V = np.linalg.eigh(H)
        G = np.zeros(2 * L, dtype=complex)
        for t in range(L):
            G[2 * ((-t) % L) + IDX[b["sigma"]]] = np.exp(-1j * P * t) * om[t]
        ov = np.abs(G.conj() @ V) ** 2
        k = int(np.argmax(ov))
        assert ov[k] > 0.5
        Es.append(w[k])
    Es = np.array(Es)
    rs = np.arange(-(L // 2) + 1, L // 2 + 1)
    Ps = 2 * np.pi * np.arange(L) / L
    kap = np.array([np.mean(Es * np.exp(1j * Ps * r)) for r in rs])
    Prest = np.pi if top else 0.0
    return float(np.real(-np.sum(rs ** 2 * kap * np.exp(-1j * Prest * rs))))


def gauss(center, w):
    j = np.arange(L)
    dj = (j - center + L / 2) % L - L / 2
    f = np.exp(-dj ** 2 / (4 * w ** 2))
    return f / np.linalg.norm(f)


def run_case(b1, b2, top, xc, widths, scale):
    b1 = dict(b1, tau=b1["tau"] * scale)
    b2 = dict(b2, tau=b2["tau"] * scale)
    g1 = b1["sigma"] * b1["gamma"] * b1["M"]
    g2 = b2["sigma"] * b2["gamma"] * b2["M"]
    D = 4 * L * L
    H1, V1 = body_ops(b1)
    H2, V2 = body_ops(b2)
    I = np.eye(2 * L)
    H0 = np.kron(H1, I) + np.kron(I, H2)
    v1 = np.kron(V1, I)
    v2 = np.kron(I, V2)
    Sm = np.kron(np.kron(shift(L, -1), I2), np.kron(shift(L, -1), I2))
    Sp = Sm.T
    # held problem: field states and eigenvalues W(j,l)
    W = np.zeros((L, L))
    Om = np.zeros((L, L, L))
    for j in range(L):
        for l in range(L):
            W[j, l], Om[j, l] = field_state([(j, g1), (l, g2)], top)
    phi1 = gauss(xc[0], widths[0])
    phi2 = gauss(xc[1], widths[1])
    s1, s2 = IDX[b1["sigma"]], IDX[b2["sigma"]]

    def rep(x1, x2):
        return ((2 * (x1 % L) + s1) * L + (x2 % L)) * 2 + s2

    tt = np.arange(L)
    X1 = (tt[None, :, None] + tt[:, None, None]) % L   # [t, x1, 1] -> x1 + t
    X2 = (tt[None, None, :] + tt[:, None, None]) % L   # [t, 1, x2] -> x2 + t
    F = phi1[X1] * phi2[X2] * Om[X1, X2, tt[:, None, None]]
    acc = np.zeros(2)
    lam = np.linspace(0.0, 60.0, 13)
    vel = np.zeros((len(lam), 2))
    norm2 = 0.0
    store = []
    for m in range(L):
        P = 2 * np.pi * m / L
        H = H0 - TF * (np.exp(-1j * P) * Sm + np.exp(1j * P) * Sp)
        w, V = np.linalg.eigh(H)
        # group of the held problem in this sector
        G = np.zeros((D, L), dtype=complex)
        for d in range(L):
            for t in range(L):
                G[rep(-t, d - t), d] = np.exp(-1j * P * t) * Om[0, d % L][t]
        ov = np.sum(np.abs(G.conj().T @ V) ** 2, axis=0)
        band = ov > 0.5
        assert band.sum() == L, band.sum()
        Vb, Eb = V[:, band], w[band]
        # start in this sector
        psi = np.zeros(D, dtype=complex)
        amp = np.einsum("t,txy->xy", np.exp(-1j * P * tt), F) / np.sqrt(L)
        for x1 in range(L):
            for x2 in range(L):
                psi[rep(x1, x2)] = amp[x1, x2]
        c = Vb.conj().T @ psi
        norm2 += np.vdot(c, c).real
        store.append((H, Vb, Eb, c))
    for H, Vb, Eb, c in store:
        c = c / np.sqrt(norm2)
        ps = Vb @ c
        for i, v in enumerate([v1, v2]):
            acc[i] += np.real(np.vdot(ps, 1j * (H @ (v @ ps) - v @ (H @ ps))))
            for k, la in enumerate(lam):
                pl = Vb @ (np.exp(-1j * Eb * la) * c)
                vel[k, i] += np.real(np.vdot(pl, v @ pl))
    slope = [np.polyfit(lam, vel[:, i], 3)[-2] for i in range(2)]
    # prediction
    Ec1 = single_band_curv(b1, top)
    Ec2 = single_band_curv(b2, top)
    j = np.arange(L)
    d1W = (W[(j + 1) % L, :] - W[(j - 1) % L, :]) / 2          # d1W[j, l]
    d2W = (W[:, (j + 1) % L] - W[:, (j - 1) % L]) / 2          # d2W[j, l]
    w1 = np.outer(phi1[(j + 1) % L] * phi1[(j - 1) % L], phi2 ** 2)
    w2 = np.outer(phi1 ** 2, phi2[(j + 1) % L] * phi2[(j - 1) % L])
    pred = np.array([-Ec1 * np.sum(w1 * d1W), -Ec2 * np.sum(w2 * d2W)])
    # in-situ estimate (2.16): relative change -/+ gamma_i * [1,2,1]/4-average of the change of the
    # field density made by the other body at the hopping body's site; upper sign (a), lower (c)
    drho2 = np.array([field_state([(l, g2)], top)[1] ** 2 - 1.0 / L for l in range(L)])  # [l, y]
    drho1 = np.array([field_state([(l, g1)], top)[1] ** 2 - 1.0 / L for l in range(L)])  # [j, y]
    av2 = (np.roll(drho2, 1, axis=1) + 2 * drho2 + np.roll(drho2, -1, axis=1)) / 4      # [l, y]
    av1 = (np.roll(drho1, 1, axis=1) + 2 * drho1 + np.roll(drho1, -1, axis=1)) / 4      # [j, y]
    R1 = av2.T            # R1[j, l]: average density change by body 2 (at l) around site j
    R2 = av1              # R2[j, l]: average density change by body 1 (at j) around site l
    sg = [(-1.0 if b["coupling"] == "a" else 1.0) * b["gamma"] for b in (b1, b2)]
    insitu = np.array([sg[0] * np.sum(w1 * R1 * d1W) / np.sum(w1 * d1W),
                       sg[1] * np.sum(w2 * R2 * d2W) / np.sum(w2 * d2W)])
    return {"scale": scale, "a_exact": acc.tolist(), "a_evolution": slope,
            "v_at_0": vel[0].tolist(), "a_pred": pred.tolist(), "Epp": [Ec1, Ec2],
            "dev": (acc / pred - 1).tolist(),
            "ratio_exact": acc[0] / acc[1], "ratio_pred": pred[0] / pred[1],
            "inertia_ratio": -Ec1 / Ec2, "insitu_est": insitu.tolist(),
            "c_factors": [float(np.sum(phi1[(j + 1) % L] * phi1[(j - 1) % L])),
                          float(np.sum(phi2[(j + 1) % L] * phi2[(j - 1) % L]))]}


CASES = [
    {"name": "A: (a), sigma=(+,+), lowest", "top": False,
     "b1": {"M": 2.0, "tau": 0.10, "gamma": 0.025, "sigma": +1, "coupling": "a"},
     "b2": {"M": 3.0, "tau": 0.15, "gamma": 0.02, "sigma": +1, "coupling": "a"},
     "xc": (3, 8), "widths": (1.3, 1.3)},
    {"name": "B: (c), sigma=(+,-), lowest", "top": False,
     "b1": {"M": 2.5, "tau": 0.12, "gamma": 0.02, "sigma": +1, "coupling": "c"},
     "b2": {"M": 1.6, "tau": 0.08, "gamma": 0.03, "sigma": -1, "coupling": "c"},
     "xc": (3, 8), "widths": (1.3, 1.3)},
    {"name": "C: (a), sigma=(-,-), highest", "top": True,
     "b1": {"M": 2.0, "tau": 0.10, "gamma": 0.025, "sigma": -1, "coupling": "a"},
     "b2": {"M": 3.0, "tau": 0.15, "gamma": 0.02, "sigma": -1, "coupling": "a"},
     "xc": (3, 8), "widths": (1.3, 1.3)},
    {"name": "D: (c), sigma=(+,+), lowest, unequal widths", "top": False,
     "b1": {"M": 2.0, "tau": 0.10, "gamma": 0.025, "sigma": +1, "coupling": "c"},
     "b2": {"M": 3.0, "tau": 0.15, "gamma": 0.02, "sigma": +1, "coupling": "c"},
     "xc": (3, 8), "widths": (1.1, 1.6)},
    {"name": "E: (c), sigma=(+,+), lowest", "top": False,
     "b1": {"M": 2.0, "tau": 0.10, "gamma": 0.025, "sigma": +1, "coupling": "c"},
     "b2": {"M": 3.0, "tau": 0.15, "gamma": 0.02, "sigma": +1, "coupling": "c"},
     "xc": (3, 8), "widths": (1.3, 1.3)},
]


GAMMA_SCAN = []
for base in (CASES[0], CASES[4]):
    GAMMA_SCAN.append({"name": base["name"][:2] + " with gamma_1, gamma_2 times 0.5", "top": False,
                       "b1": dict(base["b1"], gamma=base["b1"]["gamma"] * 0.5),
                       "b2": dict(base["b2"], gamma=base["b2"]["gamma"] * 0.5),
                       "xc": (3, 8), "widths": (1.3, 1.3)})


def main():
    results = []
    lines = [f"L={L} t_f={TF} N_f=1; scales s multiply tau_1, tau_2"]
    for case in CASES + GAMMA_SCAN:
        runs = [run_case(case["b1"], case["b2"], case["top"], case["xc"], case["widths"], s)
                for s in (1.0, 0.5, 0.25)]
        ss = np.array([r["scale"] for r in runs])
        A = np.vstack([np.ones(3), ss ** 2, ss ** 4]).T
        dev0 = [float(np.linalg.solve(A, np.array([r["dev"][i] for r in runs]))[0]) for i in range(2)]
        rr = np.array([r["ratio_exact"] / r["ratio_pred"] - 1 for r in runs])
        rdev0 = float(np.linalg.solve(A, rr)[0])
        res = {"case": case["name"], "params": {k: case[k] for k in ("b1", "b2", "xc", "widths", "top")},
               "runs": runs, "dev_extrapolated_tau0": dev0, "ratio_dev_extrapolated_tau0": rdev0,
               "insitu_estimate": runs[0]["insitu_est"],
               "insitu_ratio_estimate": runs[0]["insitu_est"][0] - runs[0]["insitu_est"][1]}
        results.append(res)
        lines.append(case["name"] + f"  b1={case['b1']}  b2={case['b2']}  centers={case['xc']}"
                     f" widths={case['widths']}")
        for r in runs:
            lines.append("  s={scale}: a_exact=({a0:.6e},{a1:.6e}) a_evol=({e0:.6e},{e1:.6e}) "
                         "v(0)=({v0:.1e},{v1:.1e})".format(scale=r["scale"], a0=r["a_exact"][0],
                                                           a1=r["a_exact"][1], e0=r["a_evolution"][0],
                                                           e1=r["a_evolution"][1], v0=r["v_at_0"][0],
                                                           v1=r["v_at_0"][1]))
            lines.append("        a_pred=({p0:.6e},{p1:.6e}) E''=({c0:.6e},{c1:.6e}) dev=({d0:.3e},{d1:.3e})"
                         .format(p0=r["a_pred"][0], p1=r["a_pred"][1], c0=r["Epp"][0], c1=r["Epp"][1],
                                 d0=r["dev"][0], d1=r["dev"][1]))
            lines.append("        ratio exact={re:.6f} pred={rp:.6f} -E''1/E''2={ri:.6f} c=({c0:.4f},{c1:.4f})"
                         .format(re=r["ratio_exact"], rp=r["ratio_pred"], ri=r["inertia_ratio"],
                                 c0=r["c_factors"][0], c1=r["c_factors"][1]))
        lines.append("  extrapolated (s->0) dev_i = ({:.3e}, {:.3e}); in-situ estimate (2.16) = ({:.3e}, {:.3e})"
                     .format(dev0[0], dev0[1], res["insitu_estimate"][0], res["insitu_estimate"][1]))
        lines.append("  extrapolated ratio deviation = {:.3e}; in-situ estimate = {:.3e}"
                     .format(rdev0, res["insitu_ratio_estimate"]))
        print("\n".join(lines[-12:]), flush=True)
    (OUT / "mutual_fall.json").write_text(json.dumps(results, indent=1))
    (OUT / "mutual_fall.log").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
