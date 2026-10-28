"""Check of item 2: the field of 06-ilang-source/04-profile (one field object, t_f = 1, first
order in g_s; per unit 2 n g_s), A_x = B_x = Phi_x (a conserved density), infinite lattice.
    made:   drho(rho e_1, lam) = -int_0^lam Im[e^{2iDs} (-i)^rho J_rho(2s) J_0(2s)^{D-1}] ds
    static: D = 3: -int_0^inf e^{-6t} I_rho(2t) I_0(2t)^2 dt ; D = 1: gradient = +1/2.
Criterion of (8.10) in both dimensions: ratio of the discrete radial differences along the axis,
Delta = (made(rho+1) - made(rho)) / (static(rho+1) - static(rho)) - 1, |Delta| <= EPS for every lam in
[lam_f, lam_max] (finite-window value, lam_max = 3 x prediction; horizon check with 1.5 x prediction).
Prediction of the continuum scaling limit: lam_form = rho^2 / (4 zeta_D(EPS)), zeta_D the first zero of
|F_D(zeta)| - EPS, F_1 = V, F_3 = 2 zeta V' - V, V(zeta) = sqrt(2 zeta/pi) int_0^1 (cos + sin)(zeta b^2) db.
"""
import json, os, sys, threading
from pathlib import Path
import numpy as np
from scipy import special, integrate, optimize

WALL_S = 900
_t = threading.Timer(WALL_S, lambda: (sys.stderr.write("wall-clock limit\n"), os._exit(3)))
_t.daemon = True
_t.start()

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
EPS = 0.1


def Dz(z):
    v, _ = integrate.quad(lambda b: np.cos(z * b * b) + np.sin(z * b * b), 0, 1)
    return np.sqrt(2 * z / np.pi) * v


def zeta_of_eps(eps):
    return optimize.brentq(lambda z: Dz(z) - eps, 1e-8, 0.5)


def D3z(z):
    """3D radial-derivative scaling function 2 z V'(z) - V(z), V = Dz (value ratio)."""
    v, _ = integrate.quad(lambda b: b * b * (np.cos(z * b * b) - np.sin(z * b * b)), 0, 1)
    return 2 * np.sqrt(2 / np.pi) * z**1.5 * v


def zeta3_of_eps(eps):
    zs = np.linspace(1e-4, 3.0, 3001)
    d = np.array([abs(D3z(x)) for x in zs])
    i = int(np.argmax(d > eps))
    return optimize.brentq(lambda x: abs(D3z(x)) - eps, zs[i - 1], zs[i])


def made_axis(D, ns, lam_max, ds):
    s = np.arange(0.0, lam_max + ds, ds)
    ph = np.exp(2j * D * s)
    J0 = special.j0(2 * s)
    out = []
    for n in ns:
        integrand = np.imag(ph * (-1j)**n * special.jv(n, 2 * s) * J0**(D - 1))
        out.append(-integrate.cumulative_trapezoid(integrand, s, initial=0.0))
    return s, np.array(out).T


def static3(n):
    f = lambda u: np.exp(u) * special.ive(n, 2 * np.exp(u)) * special.ive(0, 2 * np.exp(u))**2
    v, _ = integrate.quad(f, -30, 20, limit=4000, points=[0.0, np.log(n * n + 1.0)])
    tail = 2 * np.exp(-10.0) / (4 * np.pi)**1.5            # large-t tail, e^{-2t} I_n(2t) ~ (4 pi t)^{-1/2}
    return -(v + tail)


def lam_form(lams, Delta):
    bad = np.nonzero(np.abs(Delta) > EPS)[0]
    if not len(bad):
        return float(lams[0])
    return float(lams[bad[-1] + 1]) if bad[-1] + 1 < len(lams) else None


if __name__ == "__main__":
    z = zeta_of_eps(EPS)
    z3 = zeta3_of_eps(EPS)
    res = {"EPS": EPS, "zeta_eps": z, "pi_eps2_over_2": np.pi * EPS**2 / 2,
           "zeta3_eps": z3, "zeta3_leading_8_10": (3 * np.sqrt(2 * np.pi) * EPS / 4)**(2 / 3), "runs": []}
    for D, rhos, ds in [(1, [4, 8, 16, 32], 0.02), (3, [4, 8, 16, 32, 64], 0.01)]:
        rows = []
        for r in rhos:
            pred = r**2 / (4 * (z if D == 1 else z3))
            lmax = 3.0 * pred
            lams, m = made_axis(D, [r, r + 1], lmax, ds)
            st = 0.5 if D == 1 else static3(r + 1) - static3(r)   # static radial difference
            Delta = (m[:, 1] - m[:, 0]) / st - 1
            lf = lam_form(lams, Delta)
            half = lams <= 1.5 * pred
            lf2 = lam_form(lams[half], Delta[half])
            lin = (lams >= 2.0 * r) & (lams <= 4.0 * r)     # lambdas linear in the distance
            rows.append({"rho": r, "static_difference": st, "lam_form": lf, "pred_scaling": pred,
                         "lam_form_over_pred": lf / pred if lf else None,
                         "lam_form_half_window": lf2,
                         "max_abs_Delta_second_half_window": float(np.max(np.abs(Delta[~half]))),
                         "max_abs_Delta_lam_2rho_to_4rho": float(np.max(np.abs(Delta[lin])))})
        lr = np.log([x["rho"] for x in rows]); lf_ = np.log([x["lam_form"] for x in rows])
        res["runs"].append({"D": D, "rows": rows, "fit_exponent_all": float(np.polyfit(lr, lf_, 1)[0]),
                            "exponent_last_two": float((lf_[-1] - lf_[-2]) / (lr[-1] - lr[-2]))})
    with open(OUT / "conserved_density_formation.json", "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))
