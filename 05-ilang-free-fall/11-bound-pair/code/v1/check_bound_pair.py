"""Check for 05-ilang-free-fall/11-bound-pair, derivation v1 (role: check).

Numerical diagonalization of the fibre contract H(P) of (11.1) on the finite
range r = -L..L (open ends), for diagonal on-site bindings, and comparison with
the derivation:
  - exact relations (11.5)-(11.9) of item 2 (all parameter sets),
  - the bound-level equation (11.10) of item 3(a) (all sets),
  - the closed forms (11.12), (11.14), (11.16) of items 3 and 4 (sets in the regime R),
  - the scaling of the deviations with epsilon (scan).
Two solvers are used for the same matrix: a dense one (all eigenvectors, once per
set and P) and a banded shift-and-invert one (for the finite differences and the
doubled range); their bound levels are compared.
In the outputs, "Gamma" is the expectation value of the symmetry Xi of Step 6.
Outputs: output/check_bound_pair.json, output/check_bound_pair.txt
"""
import json
from pathlib import Path

import numpy as np
from scipy.linalg import solve_banded

OUT = Path(__file__).parent / "output"
OUT.mkdir(parents=True, exist_ok=True)

s0 = np.eye(2)
sx = np.array([[0.0, 1.0], [1.0, 0.0]])
sz = np.diag([1.0, -1.0])
SX1, SX2 = np.kron(sx, s0), np.kron(s0, sx)
SZ1, SZ2 = np.kron(sz, s0), np.kron(s0, sz)


def fibre_ops(P, p, L, eta):
    """Fibre operators on r=-L..L; index 4*(r+L)+2*(s1-1)+(s2-1)."""
    n = 2 * L + 1
    S = np.eye(n, k=-1)          # (S psi)(r) = psi(r-1)
    Sd = S.T
    e1, e2 = np.exp(1j * eta * P), np.exp(1j * (1 - eta) * P)
    A1 = 0.5j * p["tau1"] * np.kron(e1 * Sd - np.conj(e1) * S, SX1)
    A2 = 0.5j * p["tau2"] * np.kron(e2 * S - np.conj(e2) * Sd, SX2)
    V1 = -0.5 * p["tau1"] * np.kron(e1 * Sd + np.conj(e1) * S, SX1)
    V2 = -0.5 * p["tau2"] * np.kron(e2 * S + np.conj(e2) * Sd, SX2)
    Z1, Z2 = np.kron(np.eye(n), SZ1), np.kron(np.eye(n), SZ2)
    U = np.zeros((4 * n, 4 * n))
    U[4 * L:4 * L + 4, 4 * L:4 * L + 4] = np.diag(p["w"])   # w11, w12, w21, w22
    return A1, A2, V1, V2, Z1, Z2, U


def bands(P, p, nq=4001):
    """The four two-body bands (11.2) at the total label P: (lower edge, upper edge)."""
    q = np.linspace(-np.pi, np.pi, nq)
    om1 = np.sqrt(p["M1"] ** 2 + p["tau1"] ** 2 * np.sin(0.5 * P + q) ** 2)
    om2 = np.sqrt(p["M2"] ** 2 + p["tau2"] ** 2 * np.sin(0.5 * P - q) ** 2)
    return {f"{a:+d}{b:+d}": (float((a * om1 + b * om2).min()), float((a * om1 + b * om2).max()))
            for a in (1, -1) for b in (1, -1)}


def edge(P, p):
    """Edge of the (++) band next to the level: lower edge for w11<0, upper edge for w11>0."""
    return bands(P, p)["+1+1"][0 if p["w"][0] < 0 else 1]


def solve_full(P, p, L, eta=0.5):
    """Dense diagonalization; bound level = eigenvector of largest weight at (r=0, s=11)."""
    A1, A2, V1, V2, Z1, Z2, U = fibre_ops(P, p, L, eta)
    H = A1 + A2 + p["M1"] * Z1 + p["M2"] * Z2 + U
    E, X = np.linalg.eigh(H)
    b = int(np.argmax(np.abs(X[4 * L, :]) ** 2))
    psi = X[:, b]
    ex = lambda O: float(np.real(np.vdot(psi, O @ psi)))
    amp = X.conj().T @ ((eta * V1 + (1 - eta) * V2) @ psi)
    mask = np.ones(len(E), bool)
    mask[b] = False
    resolvent_sum = float(np.sum(np.abs(amp[mask]) ** 2 / (E[mask] - E[b])))
    d2H = -(eta ** 2) * ex(A1) - (1 - eta) ** 2 * ex(A2)
    r = np.repeat(np.arange(-L, L + 1), 4)
    Gam = ((-1.0) ** np.abs(r)) * np.tile(np.diag(SZ1 @ SZ2), 2 * L + 1)   # symmetry Xi of Step 6
    return dict(E=float(E[b]), s3_1=ex(Z1), s3_2=ex(Z2), A1=ex(A1), A2=ex(A2), U=ex(U),
                V1=ex(V1), V2=ex(V2), Epp_formula=d2H - 2 * resolvent_sum,
                weight0=float(np.abs(psi[4 * L]) ** 2),
                tail=float(np.sum(np.abs(psi[np.abs(r) > L // 2]) ** 2)),
                Gamma=float(np.real(np.sum(Gam * np.abs(psi) ** 2))))


def solve(P, p, L, ref, eta=0.5, theta=1.0):
    """Banded solver: the eigenvalue of H(P) nearest to ref, by inverse iteration from the
    vector (r=0, s=11), four steps at the shift ref and then Rayleigh-quotient steps."""
    n = 4 * (2 * L + 1)
    low = np.zeros((8, n), complex)              # lower band storage: low[k, j] = H[j+k, j]
    low[0, :] = np.tile(np.diag(p["M1"] * SZ1 + p["M2"] * SZ2), 2 * L + 1)
    low[0, 4 * L:4 * L + 4] += theta * np.array(p["w"])
    e1, e2 = np.exp(1j * eta * P), np.exp(1j * (1 - eta) * P)
    B = -0.5j * p["tau1"] * np.conj(e1) * SX1 + 0.5j * p["tau2"] * e2 * SX2   # block (r+1, r): coefficient of S
    for s_row in range(4):
        for s_col in range(4):
            low[4 + s_row - s_col, s_col:n - 4:4] = B[s_row, s_col]
    full = np.zeros((15, n), complex)            # storage of solve_banded: full[7+i-j, j] = H[i, j]
    for k in range(8):
        full[7 + k, :n - k] = low[k, :n - k]
        if k:
            full[7 - k, k:] = np.conj(low[k, :n - k])

    def matvec(v):
        out = low[0] * v
        for k in range(1, 8):
            out[k:] += low[k, :n - k] * v[:n - k]
            out[:n - k] += np.conj(low[k, :n - k]) * v[k:]
        return out

    v = np.zeros(n, complex)
    v[4 * L] = 1.0
    shift, E = ref, ref
    for it in range(12):
        m = full.copy()
        m[7] -= shift
        try:
            v = solve_banded((7, 7), m, v)
        except np.linalg.LinAlgError:
            break
        v /= np.linalg.norm(v)
        Hv = matvec(v)
        E = float(np.real(np.vdot(v, Hv)))
        if np.linalg.norm(Hv - E * v) < 1e-13:
            break
        if it >= 3:
            shift = E
    assert abs(v[4 * L]) ** 2 > 0.05, "banded solver left the bound level"
    return E


def d1(f, x, h):
    return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)


def d2(f, x, h):
    return (-f(x + 2 * h) + 16 * f(x + h) - 30 * f(x) + 16 * f(x - h) - f(x - 2 * h)) / (12 * h * h)


def green(E, P, p, nq=4096, eta=0.5):
    """Coefficients of (11.10): G_{s1 s2}(E,P) and g_x(E,P), as sums over q."""
    q = -np.pi + 2 * np.pi * np.arange(nq) / nq
    p1, p2 = eta * P + q, (1 - eta) * P - q
    om1 = np.sqrt(p["M1"] ** 2 + p["tau1"] ** 2 * np.sin(p1) ** 2)
    om2 = np.sqrt(p["M2"] ** 2 + p["tau2"] ** 2 * np.sin(p2) ** 2)
    G, gx = {}, 0.0
    for sg1 in (1, -1):
        for sg2 in (1, -1):
            den = 4 * (sg1 * om1 + sg2 * om2 - E)
            gx += np.mean(sg1 * sg2 * p["tau1"] * p["tau2"] * np.sin(p1) * np.sin(p2) / (om1 * om2 * den))
            for t1 in (1, 2):
                for t2 in (1, 2):
                    c1, c2 = (1 if t1 == 1 else -1), (1 if t2 == 1 else -1)
                    G[(t1, t2)] = G.get((t1, t2), 0.0) + np.mean(
                        (1 + c1 * sg1 * p["M1"] / om1) * (1 + c2 * sg2 * p["M2"] / om2) / den)
    return G, gx


def green_direct(E, P, p, nq=4096, eta=0.5):
    """<r=0|(H0(P)-E)^(-1)|r=0> as a 4x4 matrix, by inverting h_P(q)-E on the q grid."""
    q = -np.pi + 2 * np.pi * np.arange(nq) / nq
    p1, p2 = eta * P + q, (1 - eta) * P - q
    h = (-p["tau1"] * np.sin(p1))[:, None, None] * SX1 + (-p["tau2"] * np.sin(p2))[:, None, None] * SX2 \
        + p["M1"] * SZ1 + p["M2"] * SZ2 - E * np.eye(4)
    return np.linalg.inv(h).mean(axis=0)


def F_plus(E, P, p):
    """The factor F_+ of (11.10) (sector Xi=+1)."""
    G, gx = green(E, P, p)
    w11, _, _, w22 = p["w"]
    return (1 + w11 * G[(1, 1)]) * (1 + w22 * G[(2, 2)]) - w11 * w22 * gx ** 2


def root_F_plus(Eb, P, p, gap):
    lo, hi = Eb - 0.3 * gap, Eb + 0.3 * gap
    flo, fhi = F_plus(lo, P, p), F_plus(hi, P, p)
    if flo * fhi > 0:
        return None
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        fm = F_plus(mid, P, p)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def closed(P, p):
    """Closed forms of item 3 (leading order in R); expectation values at P=0."""
    M1, M2, t1, t2 = p["M1"], p["M2"], p["tau1"], p["tau2"]
    w = p["w"][0]
    sg = np.sign(w)
    a1, a2 = t1 ** 2 / (4 * M1), t2 ** 2 / (4 * M2)
    a = a1 + a2
    j = np.sqrt(a1 ** 2 + a2 ** 2 + 2 * a1 * a2 * np.cos(2 * P))
    root0 = np.sqrt(w * w + a * a)
    c = 1 + sg * a / root0
    return dict(E=M1 + M2 + a + sg * np.sqrt(w * w + j * j),
                Ep=-sg * 2 * a1 * a2 * np.sin(2 * P) / np.sqrt(w * w + j * j),
                Epp0=-sg * 4 * a1 * a2 / root0, Ebind=a + sg * root0,
                s3_1=1 - a1 / M1 * c, s3_2=1 - a2 / M2 * c, A1=2 * a1 * c, A2=2 * a2 * c,
                U=sg * w * w / root0, a=a, u=abs(w) / a)


def with_(p, **kw):
    q = dict(p)
    q.update(kw)
    return q


SETS = {
    "A_equal_R":      dict(M1=1.0, M2=1.0, tau1=0.10, tau2=0.10, w=[-0.0040, 0.0030, -0.0020, 0.0060]),
    "B_unequal_R":    dict(M1=1.0, M2=1.7, tau1=0.20, tau2=0.12, w=[-0.0100, 0.0050, -0.0040, 0.0080]),
    "C_above_band_R": dict(M1=1.0, M2=0.8, tau1=0.10, tau2=0.15, w=[0.0200, -0.0050, 0.0030, -0.0100]),
    "D_wide_R":       dict(M1=1.3, M2=1.0, tau1=0.15, tau2=0.20, w=[-0.0040, 0.0020, 0.0010, 0.0030]),
    "E_order_one":    dict(M1=1.0, M2=1.3, tau1=1.00, tau2=0.80, w=[-0.6000, 0.2000, -0.1500, 0.3000]),
}
REGIME_R = {"A_equal_R", "B_unequal_R", "C_above_band_R", "D_wide_R"}
P_VALUES = [-0.30, -0.15, 0.0, 0.15, 0.30]
L = 120
HP, HX = 0.01, 1e-3

results, lines = {}, []


def say(s):
    lines.append(s)
    print(s, flush=True)


say(f"range of r: -L..L with L={L} (open ends); convergence: comparison with L={2 * L} and weight at |r|>L/2")
say(f"finite differences: 5-point, step {HP} in P, relative step {HX} in M_i, tau_i, theta; convention eta=1/2")

for name, p in SETS.items():
    say(f"\n=== set {name}: {p}  max tau_i/M_i = {max(p['tau1'] / p['M1'], p['tau2'] / p['M2']):.3f}")
    res = dict(params=p, P={})
    keys = ("dM", "dtau", "dtheta", "euler", "V1", "V2", "V12", "Epp", "eq310", "green", "conv", "tail", "eta",
            "solvers", "closed_E", "closed_Ep")
    worst = dict.fromkeys(keys, 0.0)
    for P in P_VALUES:
        o = solve_full(P, p, L)
        bd = bands(P, p)
        gap = min(abs(o["E"] - e) for lohi in bd.values() for e in lohi)
        inside = any(lo <= o["E"] <= hi for lo, hi in bd.values())
        e0 = edge(P, p)

        def fE(PP=P, pp=p, **kw):
            """Banded bound level at changed P or data; the reference follows the band edge."""
            return solve(PP, pp, L, o["E"] + edge(PP, pp) - e0, **kw)

        solvers = abs(fE() - o["E"])
        conv = abs(solve(P, p, 2 * L, o["E"]) - o["E"])
        eta_dep = max(abs(fE(eta=e) - o["E"]) for e in (0.0, 1.0, 0.3))
        # item 2(a): derivatives of E_b against expectation values
        dM1 = d1(lambda x: fE(pp=with_(p, M1=x)), p["M1"], HX * p["M1"])
        dM2 = d1(lambda x: fE(pp=with_(p, M2=x)), p["M2"], HX * p["M2"])
        dt1 = p["tau1"] * d1(lambda x: fE(pp=with_(p, tau1=x)), p["tau1"], HX * p["tau1"])
        dt2 = p["tau2"] * d1(lambda x: fE(pp=with_(p, tau2=x)), p["tau2"], HX * p["tau2"])
        dth = d1(lambda x: fE(theta=x), 1.0, HX)
        euler = p["M1"] * o["s3_1"] + p["M2"] * o["s3_2"] + o["A1"] + o["A2"] + o["U"] - o["E"]
        # items 2(b), 2(c)
        Ep = d1(lambda x: fE(PP=x), P, HP)
        Epp = d2(lambda x: fE(PP=x), P, HP)
        # item 3(a): coefficients against a direct inversion, root against E_b
        G, gx = green(o["E"], P, p)
        Gd = green_direct(o["E"], P, p)
        gerr = max(abs(G[(1, 1)] - Gd[0, 0]), abs(G[(1, 2)] - Gd[1, 1]), abs(G[(2, 1)] - Gd[2, 2]),
                   abs(G[(2, 2)] - Gd[3, 3]), abs(gx - Gd[0, 3]), abs(gx - Gd[1, 2]),
                   abs(Gd[0, 1]), abs(Gd[0, 2]), abs(Gd[1, 3]), abs(Gd[2, 3])) / np.abs(Gd).max()
        root = root_F_plus(o["E"], P, p, gap)
        c = closed(P, p)
        res["P"][f"{P:+.2f}"] = dict(
            E=o["E"], isolation=gap, inside_band=inside, weight0=o["weight0"], Gamma=o["Gamma"],
            tail=o["tail"], conv_2L=conv, eta_dependence=eta_dep, dense_minus_banded=solvers,
            dM1=[dM1, o["s3_1"]], dM2=[dM2, o["s3_2"]], dtau1=[dt1, o["A1"]], dtau2=[dt2, o["A2"]],
            dtheta=[dth, o["U"]], euler_residual=euler, Ep=[Ep, o["V1"], o["V2"]], Epp=[Epp, o["Epp_formula"]],
            green_rel_error=float(gerr), eq_3a_root=root,
            eq_3a_root_minus_E=(None if root is None else root - o["E"]),
            closed_E=float(c["E"]), closed_Ep=float(c["Ep"]))
        for k, v in (("dM", max(abs(dM1 - o["s3_1"]), abs(dM2 - o["s3_2"]))),
                     ("dtau", max(abs(dt1 - o["A1"]), abs(dt2 - o["A2"]))), ("dtheta", abs(dth - o["U"])),
                     ("euler", abs(euler)), ("V1", abs(Ep - o["V1"])), ("V2", abs(Ep - o["V2"])),
                     ("V12", abs(o["V1"] - o["V2"])), ("Epp", abs(Epp - o["Epp_formula"])),
                     ("eq310", np.inf if root is None else abs(root - o["E"])), ("green", float(gerr)),
                     ("conv", conv), ("tail", o["tail"]), ("eta", eta_dep), ("solvers", solvers),
                     ("closed_E", abs(c["E"] - o["E"])), ("closed_Ep", abs(c["Ep"] - Ep))):
            worst[k] = max(worst[k], float(v))
        say(f"P={P:+.2f}  E_b={o['E']:.12f}  isolation={gap:.3e}  in a band: {inside}  weight(r=0,11)={o['weight0']:.4f}"
            f"  Gamma={o['Gamma']:+.6f}  E_b'={Ep:+.6e}  <V1>={o['V1']:+.6e}  <V2>={o['V2']:+.6e}"
            f"  E_b''={Epp:+.6e}  (11.9)={o['Epp_formula']:+.6e}")
    res["max_abs_deviation"] = worst
    say("max |deviation| over the P values:")
    say(f"  2(a): dE/dM_i - <sigma3_i> {worst['dM']:.2e}; tau_i dE/dtau_i - <A_i> {worst['dtau']:.2e};"
        f" dE/dtheta - <U> {worst['dtheta']:.2e}; Euler residual {worst['euler']:.2e}")
    say(f"  2(b): E_b' - <V1> {worst['V1']:.2e}; E_b' - <V2> {worst['V2']:.2e}; <V1> - <V2> {worst['V12']:.2e}")
    say(f"  2(c): E_b'' (finite difference) - formula (11.9) {worst['Epp']:.2e}")
    say(f"  3(a): coefficients of (11.10) against direct inversion (relative) {worst['green']:.2e};"
        f" root of (11.10) - E_b {worst['eq310']:.2e}")
    say(f"  numerics: |E_b(L) - E_b(2L)| {worst['conv']:.2e}; weight at |r|>L/2 {worst['tail']:.2e};"
        f" dependence on eta {worst['eta']:.2e}; dense - banded {worst['solvers']:.2e}")
    # closed forms at P = 0
    o0 = solve_full(0.0, p, L)
    c0 = closed(0.0, p)
    Epp0 = o0["Epp_formula"]
    eps2 = max(p["tau1"] / p["M1"], p["tau2"] / p["M2"]) ** 2
    cmp0 = {k: [o0[k], float(c0[k])] for k in ("s3_1", "s3_2", "A1", "A2", "U")}
    cmp0["Ebind"] = [o0["E"] - p["M1"] - p["M2"], float(c0["Ebind"])]
    cmp0["Epp0"] = [Epp0, float(c0["Epp0"])]
    m1, m2 = p["M1"] / p["tau1"] ** 2, p["M2"] / p["tau2"] ** 2
    mb = 1.0 / Epp0
    item4 = dict(mb_over_m1_plus_m2=[mb / (m1 + m2), float(-np.sign(p["w"][0]) * np.sqrt(1 + c0["u"] ** 2))],
                 mb_minus_m1_m2=[mb - m1 - m2, -4 * m1 * m2 * (o0["E"] - p["M1"] - p["M2"])])
    res["closed_forms_P0"] = dict(u=float(c0["u"]), a=float(c0["a"]), eps2=eps2, compare=cmp0, item4=item4,
                                  max_dE_over_P=worst["closed_E"], max_dEp_over_P=worst["closed_Ep"],
                                  rel_dev_Epp0=float(abs(Epp0 - c0["Epp0"]) / abs(c0["Epp0"])))
    tag = "regime R" if name in REGIME_R else "control, outside R"
    say(f"closed forms (items 3, 4), {tag}: |w11|/a = {c0['u']:.3f}, (max tau/M)^2 = {eps2:.3e}")
    say(f"  max_P |E_b - (11.12)| = {worst['closed_E']:.3e}  = {worst['closed_E'] / (eps2 ** 2):.3f} * (tau/M)^4;"
        f"  max_P |E_b' - d(11.12)/dP| = {worst['closed_Ep']:.3e}")
    say(f"  E_b''(0): numeric {Epp0:+.8e}  closed {c0['Epp0']:+.8e}  rel.dev {abs(Epp0 - c0['Epp0']) / abs(c0['Epp0']):.3e}"
        f"  = {abs(Epp0 - c0['Epp0']) / abs(c0['Epp0']) / eps2:.3f} * (tau/M)^2")
    for k, (num, cl) in cmp0.items():
        say(f"  {k:6s} numeric {num:+.10e}  closed {cl:+.10e}  diff {num - cl:+.2e}")
    say(f"  m_b/(m_1+m_2): numeric {item4['mb_over_m1_plus_m2'][0]:+.6f}  (11.16) {item4['mb_over_m1_plus_m2'][1]:+.6f};"
        f"  m_b-(m_1+m_2): numeric {item4['mb_minus_m1_m2'][0]:+.6e}  -4 m_1 m_2 E_bind {item4['mb_minus_m1_m2'][1]:+.6e}")
    results[name] = res

# epsilon scan: tau_i = eps*tauhat_i, w = eps^2*what, for the data of set B (eps = 1)
say("\n=== epsilon scan on set B_unequal_R (tau -> eps*tau, w -> eps^2*w)")
base = SETS["B_unequal_R"]
scan, prev = [], None
for eps in (1.0, 0.5, 0.25, 0.125):
    p = with_(base, tau1=eps * base["tau1"], tau2=eps * base["tau2"], w=[eps * eps * x for x in base["w"]])
    o0, c0 = solve_full(0.0, p, L), closed(0.0, p)
    row = dict(eps=eps, dE_P0=o0["E"] - c0["E"], dE_P03=solve_full(0.3, p, L)["E"] - closed(0.3, p)["E"],
               rel_dEpp0=(o0["Epp_formula"] - c0["Epp0"]) / c0["Epp0"], d_s3_1=o0["s3_1"] - c0["s3_1"],
               d_s3_2=o0["s3_2"] - c0["s3_2"])
    row = {k: float(v) for k, v in row.items()}
    if prev:
        row["ratio_to_previous"] = {k: prev[k] / row[k] for k in row if k != "eps"}
    scan.append(row)
    prev = {k: v for k, v in row.items() if k != "ratio_to_previous"}
    say(f"eps={eps:6.3f}  E_b-(11.12): P=0 {row['dE_P0']:+.4e}, P=0.3 {row['dE_P03']:+.4e};  rel.dev E_b''(0) {row['rel_dEpp0']:+.4e};"
        f"  <sigma3_i>-(11.14): {row['d_s3_1']:+.4e}, {row['d_s3_2']:+.4e}")
    if "ratio_to_previous" in row:
        say("          ratios to the previous eps: " + ", ".join(f"{k} {v:.2f}" for k, v in row["ratio_to_previous"].items()))
say("expected for halving eps: 16 for E_b and <sigma3_i> (next order eps^4), 4 for the relative deviation of E_b''(0)")
results["epsilon_scan_set_B"] = scan
results["settings"] = dict(L=L, L_check=2 * L, P_values=P_VALUES, eta=0.5, h_P=HP, h_rel_parameters=HX)

(OUT / "check_bound_pair.json").write_text(json.dumps(results, indent=1), encoding="utf-8")
(OUT / "check_bound_pair.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
