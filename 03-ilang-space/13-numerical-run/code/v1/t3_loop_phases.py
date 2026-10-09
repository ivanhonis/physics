"""T3 (computation): loop phases, tests (10.10), (10.15) and Step 6(a) of 10."""
import numpy as np
from scipy.linalg import expm

from common import gue, goe, view, loop_w, slope, cjson, save

dc, ntri = 4, 50
grid = [1e-2, 3e-3, 1e-3]
chi = np.zeros(dc, complex); chi[0] = 1.0     # |chi> = e_1 (real)
phi = np.full(3, 1 / np.sqrt(3))               # W is independent of phi_h != 0


def u_vec(K):
    return K @ chi - (chi.conj() @ K @ chi) * chi


def omega(v, w):
    return float(np.vdot(v, w).imag)            # Im <v|w>


def loop_phase(Ks, lam):
    psis = np.array([phi[j] * (expm(-1j * lam * Ks[j]) @ chi) for j in range(3)])  # (12.8)
    return float(np.angle(loop_w(view(psis), [0, 1, 2])))


# (a) generic GUE records
rng = np.random.default_rng(1305)
tris = [[gue(rng, dc) for _ in range(3)] for _ in range(ntri)]
om = [omega(u_vec(K[1]) - u_vec(K[0]), u_vec(K[2]) - u_vec(K[0])) for K in tris]
sel = [t for t in range(ntri) if abs(om[t]) > 1e-2]
a_rows, maxrel = [], []
for lam in grid:
    per = {}
    for t in sel:
        Phi = loop_phase(tris[t], lam)
        Phi2 = -lam ** 2 * om[t]
        per[t] = {"Phi": Phi, "Phi2": Phi2, "rel_err": abs(Phi - Phi2) / abs(Phi2)}
    maxrel.append(max(v["rel_err"] for v in per.values()))
    a_rows.append({"lambda": lam, "per_triangle": per, "max_rel_err": maxrel[-1]})
    print(f"(a) lambda={lam:.0e}  max rel err={maxrel[-1]:.6e}")
s_a = slope(grid, maxrel)
dec_a = "pass" if (maxrel[-1] < 1e-2 and s_a >= 0.9) else "fail"
print(f"(a) selected {len(sel)}/{ntri}, slope={s_a:.6f}, decision={dec_a}")

# diagnostics (not decisions): ranking of triangles at lambda = 1e-3, and an mpmath (40 digits)
# recomputation of Phi for the triangle attaining the maximum, to exclude rounding as the cause
import mpmath as mp
last = a_rows[-1]["per_triangle"]
ranking = sorted(last, key=lambda t: -last[t]["rel_err"])
diag_a = {"triangles_by_rel_err_at_1e-3": [{"triangle": t, "omega": om[t], "rel_err": last[t]["rel_err"]}
                                           for t in ranking[:5]],
          "median_rel_err_per_lambda": [float(np.median([v["rel_err"] for v in r["per_triangle"].values()]))
                                        for r in a_rows]}
mp.mp.dps = 40
t0, lam = ranking[0], mp.mpf("1e-3")
E = [mp.expm(-1j * lam * mp.matrix(tris[t0][j].tolist())) * mp.matrix(chi.tolist()) for j in range(3)]
ov = lambda a, b: sum(mp.conj(a[i]) * b[i] for i in range(dc))  # <a|b>
Wl = ov(E[1], E[0]) * ov(E[2], E[1]) * ov(E[0], E[2])           # G_12 G_23 G_31
diag_a["mpmath_check"] = {"triangle": t0, "Phi_mpmath": float(mp.arg(Wl)), "Phi_double": last[t0]["Phi"],
                          "rel_dev": float(abs(mp.arg(Wl) - last[t0]["Phi"]) / abs(mp.arg(Wl)))}
print("(a) diagnostics:", diag_a["triangles_by_rel_err_at_1e-3"][:2], diag_a["mpmath_check"])

# (b)(i) commuting records K_h = x_h X
X = gue(np.random.default_rng(1306), dc)
x = np.random.default_rng(1307).standard_normal((ntri, 3))
tris_i = [[x[t, j] * X for j in range(3)] for t in range(ntri)]
# (b)(ii) real records, GOE
rng = np.random.default_rng(1308)
tris_ii = [[goe(rng, dc).astype(complex) for _ in range(3)] for _ in range(ntri)]

b_out, dec_b_ok = {}, True
for name, T in [("i_commuting", tris_i), ("ii_real_GOE", tris_ii)]:
    rows, mx = [], []
    for lam in grid:
        ph = [loop_phase(K, lam) for K in T]
        mx.append(max(abs(p) for p in ph))
        rows.append({"lambda": lam, "Phi_per_triangle": ph, "max_abs_Phi": mx[-1]})
    s = slope(grid, mx)
    dec_b_ok &= s >= 2.8
    # diagnostic (10.15): W(-lambda) = W(lambda)^* at lambda = 1e-2, max over triangles
    diag = None
    if name == "ii_real_GOE":
        dev = []
        for K in T:
            pp = np.array([phi[j] * (expm(-1j * 1e-2 * K[j]) @ chi) for j in range(3)])
            pm = np.array([phi[j] * (expm(+1j * 1e-2 * K[j]) @ chi) for j in range(3)])
            dev.append(abs(loop_w(view(pm), [0, 1, 2]) - np.conj(loop_w(view(pp), [0, 1, 2]))))
        diag = float(max(dev))
    b_out[name] = {"per_lambda": rows, "max_abs_Phi": mx, "fitted_slope": s,
                   "diag_max_dev_W(-lam)_vs_conj_W(lam)_at_1e-2": diag}
    print(f"(b) {name}: max|Phi|={mx}, slope={s:.6f}, diag={diag}")
dec_b = "pass" if dec_b_ok else "fail"
print("(b) decision:", dec_b)

save("t3_loop_phases.json", {
    "part": "T3", "d_c": dc, "grid": grid,
    "a": {"seed": 1305, "omega_per_triangle": om, "selected_triangles": sel, "n_selected": len(sel),
          "per_lambda": a_rows, "max_rel_err": maxrel, "fitted_slope": s_a, "diagnostics": diag_a,
          "records": [[cjson(K) for K in tri] for tri in tris],
          "rule": "pass iff max rel err < 1e-2 at lambda=1e-3 and slope >= 0.9", "decision": dec_a},
    "b": {"seeds": {"X": 1306, "x_h": 1307, "GOE": 1308}, "X": cjson(X), "x_h": x.tolist(), **b_out,
          "rule": "pass iff fitted slope >= 2.8 in both controls", "decision": dec_b}})
