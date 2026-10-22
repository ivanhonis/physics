"""Check of item 2 (held bodies) of 07-ilang-weight/02-two-free-bodies.

N_f = 1 field object on a ring of L places, own term C_1 = -t_f sum (|x><x+1| + h.c.),
two held bodies acting as point terms g_1 P_{x1} + g_2 P_{x2}, g_i = sigma_i gamma_i M_i.
Compares the exact mutual term
    M(x1,x2) = eps0(g1,g2) - eps0(g1,0) - eps0(0,g2) + eps0(0,0)        (N_f = 1, n = 1/L)
with the closed forms (2.6)-(2.8) of the derivation, and checks translation, reflection and
exchange invariance (2.4), the non-product form at third order (2.9) and the highest-state map (2.5).
Output: output/held_pair.json and output/held_pair.log
"""
import json
from pathlib import Path

import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)


def h_field(L, tf, pts):
    H = np.zeros((L, L))
    for x in range(L):
        H[x, (x + 1) % L] -= tf
        H[(x + 1) % L, x] -= tf
    for x, g in pts:
        H[x, x] += g
    return H


def eps(L, tf, pts, top=False):
    w = np.linalg.eigvalsh(h_field(L, tf, pts))
    return w[-1] if top else w[0]


def mutual(L, tf, g1, g2, x1, x2, top=False):
    return (eps(L, tf, [(x1, g1), (x2, g2)], top) - eps(L, tf, [(x1, g1)], top)
            - eps(L, tf, [(x2, g2)], top) + eps(L, tf, [], top))


def lam_closed(L, d):
    u = d * (L - d)
    return (L**2 - 1) / (12 * L) - u / (2 * L)


def lam2_closed(L, d):
    u = d * (L - d)
    return (L**2 - 1) * (L**2 + 11) / (720 * L) - u / (12 * L) - u**2 / (24 * L)


def m2_closed(L, tf, g1, g2, d, n):
    return -2 * n * g1 * g2 / tf * lam_closed(L, d)


def m3_closed(L, tf, g1, g2, d, n):
    u = d * (L - d)
    b3 = (20 * u**2 - 10 * (L**2 - 2) * u + (L**2 - 1) * (L**2 - 4)) / (60 * L**2)
    return n / tf**2 * g1 * g2 * (g1 + g2) * b3


def run(L, tf, g1, g2):
    n = 1.0 / L
    res = {"L": L, "t_f": tf, "g1": g1, "g2": g2,
           "kato_bound_|g1|+|g2|<": 2 * tf * np.sin(np.pi / L) ** 2}
    # closed forms of Lambda^+ and (Lambda^+)^2 against the pseudo-inverse of the ring Laplacian
    lap = h_field(L, 1.0, []) + 2 * np.eye(L)
    lp = np.linalg.pinv(lap)
    lp2 = lp @ lp
    ds = np.arange(L)
    res["max_err_Lambda_closed"] = float(np.max(np.abs(lp[0, ds] - lam_closed(L, ds))))
    res["max_err_Lambda2_closed"] = float(np.max(np.abs(lp2[0, ds] - lam2_closed(L, ds))))
    # exact mutual term for all position pairs
    Mx = np.array([[mutual(L, tf, g1, g2, a, b) for b in range(L)] for a in range(L)])
    Md = Mx[0]
    res["max_dev_translation"] = float(np.max(np.abs(Mx - np.array(
        [[Md[(b - a) % L] for b in range(L)] for a in range(L)]))))
    res["max_dev_reflection"] = float(np.max(np.abs(Md - Md[(-ds) % L])))
    Mswap = np.array([mutual(L, tf, g2, g1, 0, d) for d in ds])
    res["max_dev_exchange"] = float(np.max(np.abs(Md - Mswap)))
    # discrete forces F1 = -dM/dx1, F2 = -dM/dx2 (symmetric differences)
    F1 = np.array([-(Mx[1, d] - Mx[L - 1, d]) / 2 for d in ds])
    F2 = np.array([-(Mx[0, (d + 1) % L] - Mx[0, (d - 1) % L]) / 2 for d in ds])
    res["max_|F1+F2|"] = float(np.max(np.abs(F1 + F2)))
    # perturbative comparison at three scales of the couplings
    scal = []
    for s in [1.0, 0.5, 0.25]:
        a1, a2 = s * g1, s * g2
        Me = np.array([mutual(L, tf, a1, a2, 0, d) for d in ds])
        Mm = np.array([mutual(L, tf, -a1, -a2, 0, d) for d in ds])
        m2 = m2_closed(L, tf, a1, a2, ds, n)
        m3 = m3_closed(L, tf, a1, a2, ds, n)
        scal.append({"scale": s,
                     "max|M|": float(np.max(np.abs(Me))),
                     "max|M-M2|": float(np.max(np.abs(Me - m2))),
                     "max|M-M2-M3|": float(np.max(np.abs(Me - m2 - m3))),
                     "max|odd part - M3|": float(np.max(np.abs((Me - Mm) / 2 - m3)))})
    res["scaling"] = scal
    res["ratio_resid4_s1_over_s0.5"] = scal[0]["max|M-M2-M3|"] / scal[1]["max|M-M2-M3|"]
    # non-product form: M3/M2 as a function of d (exact odd part / closed M2)
    Me = np.array([mutual(L, tf, g1, g2, 0, d) for d in ds])
    Mm = np.array([mutual(L, tf, -g1, -g2, 0, d) for d in ds])
    m2 = m2_closed(L, tf, g1, g2, ds, n)
    res["d"] = ds.tolist()
    res["M_exact"] = Me.tolist()
    res["M2_closed"] = m2.tolist()
    res["M3_closed"] = m3_closed(L, tf, g1, g2, ds, n).tolist()
    res["odd_part_over_M2"] = ((Me - Mm) / 2 / m2).tolist()
    # highest state: M_top(g1,g2) = -M_low(-g1,-g2) for even L
    if L % 2 == 0:
        Mt = np.array([mutual(L, tf, g1, g2, 0, d, top=True) for d in ds])
        res["max_dev_top_map"] = float(np.max(np.abs(Mt + Mm)))
    return res


def main():
    tf = 1.0
    results = [run(8, tf, 0.04, -0.07), run(13, tf, 0.05, -0.03), run(13, tf, 0.03, 0.06)]
    (OUT / "held_pair.json").write_text(json.dumps(results, indent=1))
    lines = []
    for r in results:
        lines.append(f"L={r['L']} t_f={r['t_f']} g1={r['g1']} g2={r['g2']} "
                     f"(Kato bound {r['kato_bound_|g1|+|g2|<']:.4f})")
        for k in ["max_err_Lambda_closed", "max_err_Lambda2_closed", "max_dev_translation",
                  "max_dev_reflection", "max_dev_exchange", "max_|F1+F2|", "max_dev_top_map"]:
            if k in r:
                lines.append(f"  {k}: {r[k]:.3e}")
        for s in r["scaling"]:
            lines.append("  scale {scale}: max|M|={a:.3e} max|M-M2|={b:.3e} "
                         "max|M-M2-M3|={c:.3e} max|odd-M3|={e:.3e}".format(
                             scale=s["scale"], a=s["max|M|"], b=s["max|M-M2|"],
                             c=s["max|M-M2-M3|"], e=s["max|odd part - M3|"]))
        lines.append(f"  residual ratio (scale 1 / scale 1/2): {r['ratio_resid4_s1_over_s0.5']:.2f}"
                     " (16 expected for O(g^4))")
        lines.append("  d, M_exact, M2, M3, (odd part)/M2:")
        for d in r["d"]:
            lines.append(f"   {d:2d} {r['M_exact'][d]: .6e} {r['M2_closed'][d]: .6e} "
                         f"{r['M3_closed'][d]: .6e} {r['odd_part_over_M2'][d]: .5f}")
    (OUT / "held_pair.log").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
