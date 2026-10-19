"""Check for 05-ilang-free-fall/11-bound-pair, derivation v2 (role: check).

Part 1 is the check of v1, unchanged: numerical diagonalization of the fibre contract H(P)
of (11.1) on the finite range r = -L..L (open ends), for diagonal on-site bindings, and
comparison with the derivation:
  - exact relations (11.5)-(11.9) of item 2 (all parameter sets),
  - the bound-level equation (11.10) of item 3(a) (all sets),
  - the closed forms (11.12), (11.14), (11.16) of items 3 and 4 (sets in the regime R),
  - the scaling of the deviations with epsilon (scan).
Two solvers are used for the same matrix: a dense one (all eigenvectors, once per
set and P) and a banded shift-and-invert one (for the finite differences and the
doubled range); their bound levels are compared.
In the outputs of Part 1, "Gamma" is the expectation value of the symmetry Xi of Step 6.

Part 2 checks what is new in v2:
  - I3: the reading statistics of the clock of a part, (11.19), with the rate at the mean level,
        the rate to first order (11.25) and its closed form in the regime R (11.26);
  - I4: the order eps^6 of the contribution of w22 to the bound level;
  - I5: the bound eigenvector at j(P) = 0;
  - I2: twofold bound levels: (11.23), (11.24) and the identities for every eigenvector;
  - I1: the operator C_bod of (11.21) on a small system given in the places.
Outputs: output/check_bound_pair.json, output/check_bound_pair.txt
"""
import json
from pathlib import Path

import numpy as np
from scipy.linalg import solve_banded
from scipy.optimize import minimize_scalar

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

# ---------------------------------------------------------------------------
# Part 2: checks of what is new in derivation v2
# ---------------------------------------------------------------------------
new = {}


def dense(P, p, L, eta=0.5, W0=None, theta=1.0):
    """Dense H(P) with all eigenvectors and its parts. W0: a general on-site binding
    (4x4, order 11, 12, 21, 22) used instead of the diagonal p['w']."""
    A1, A2, V1, V2, Z1, Z2, U = fibre_ops(P, p, L, eta)
    if W0 is not None:
        U = np.zeros_like(A1)
        U[4 * L:4 * L + 4, 4 * L:4 * L + 4] = W0
    H = A1 + A2 + p["M1"] * Z1 + p["M2"] * Z2 + theta * U
    E, X = np.linalg.eigh(H)
    return E, X, dict(A1=A1, A2=A2, V1=V1, V2=V2, Z1=Z1, Z2=Z2, U=U)


def P_ring(a, vartheta, N):
    """P_N(a; vartheta) of (5.1) of 04-ilang-time/05-moving-clock."""
    k = np.arange(N)
    return float(abs(np.mean(np.exp(2j * np.pi * k * (a - vartheta) / N))) ** 2)


def closed_d2M(p, part):
    """Second derivative of the closed form (11.12) at P=0 with respect to M_part (used in (11.26))."""
    M1, M2, t1, t2 = p["M1"], p["M2"], p["tau1"], p["tau2"]
    w = p["w"][0]
    sg = np.sign(w)
    a1, a2 = t1 ** 2 / (4 * M1), t2 ** 2 / (4 * M2)
    a, ai, Mi = a1 + a2, (a1 if part == 1 else a2), (M1 if part == 1 else M2)
    u = abs(w) / a
    lam = 1 + sg / np.sqrt(1 + u * u)
    return float(ai / Mi ** 2 * (2 * lam + sg * ai / a * u * u / (1 + u * u) ** 1.5))


def clock_check(p, part, N, D, ticks):
    """Item 5(a), (11.19) and (11.25): exact reading statistics of the clock label of one part
    for a pair in the bound level at P=0 (sharp total label, no records), against
    P_N(a; Gamma*lambda/lambda_0) with three choices of Gamma."""
    key = f"M{part}"
    m = p[key]
    lam0 = 2 * np.pi * (N - 1) / (N * D)          # tick parameter with the level spread d_{N-1} = D
    d = D * np.arange(N) / (N - 1)
    dbar = 0.5 * D
    lev = [dense(0.0, with_(p, **{key: m + dk}), L)[:2] for dk in d]
    E0, X0, ops = dense(0.0, p, L)
    b = int(np.argmax(np.abs(X0[4 * L, :]) ** 2))
    psi0 = X0[:, b]
    Z = ops[f"Z{part}"]
    g0 = np.inf                                     # isolation of the bound level over the levels of the clock
    for E, X in lev:
        bk = int(np.argmax(np.abs(X[4 * L, :]) ** 2))
        g0 = min(g0, float(np.min(np.abs(np.delete(E, bk) - E[bk]))))
    G0 = float(np.real(np.vdot(psi0, Z @ psi0)))                     # <sigma3_i>_0 at M_i = m_i (rate of v1)
    amp = X0.conj().T @ (Z @ psi0)
    mask = np.ones(len(E0), bool)
    mask[b] = False
    d2E = float(-2 * np.sum(np.abs(amp[mask]) ** 2 / (E0[mask] - E0[b])))   # d^2 E_b / d M_i^2 at m_i
    Gmean = solve_full(0.0, with_(p, **{key: m + dbar}), L)[f"s3_{part}"]   # <sigma3_i>_0 at the mean level
    Gfirst = G0 + dbar * d2E                                                # (11.25)
    coef = [X.conj().T @ psi0 for E, X in lev]      # start: eigenvector of the level 0 on every level
    q = np.zeros((len(ticks), N))
    for it, t in enumerate(ticks):
        vec = np.array([X @ (np.exp(-1j * E * t * lam0) * c) for (E, X), c in zip(lev, coef)])
        for a in range(N):
            q[it, a] = np.linalg.norm(np.exp(2j * np.pi * np.arange(N) * a / N) @ vec / N) ** 2

    def table(G):
        return np.array([[P_ring(a, G * t, N) for a in range(N)] for t in ticks])

    def dev(G, tmax=None):
        sel = np.ones(len(ticks), bool) if tmax is None else (np.asarray(ticks) <= tmax + 1e-12)
        return float(np.max(np.abs(q - table(G))[sel]))

    fit = minimize_scalar(lambda G: float(np.sum((q - table(G)) ** 2)), bounds=(Gmean - 0.05, Gmean + 0.05),
                          method="bounded", options=dict(xatol=1e-13))
    cm = closed(0.0, with_(p, **{key: m + dbar}))
    c0 = closed(0.0, p)
    return dict(part=part, N=N, D=D, lambda0=lam0, g0=g0, D_over_g0=D / g0, D_over_M=D / m, sum_q_minus_1=float(
        np.max(np.abs(q.sum(axis=1) - 1))), Gamma_level0=G0, Gamma_mean_level=Gmean, Gamma_first_order=Gfirst,
        Gamma_fit=float(fit.x), d2E_dM2=d2E, d2E_dM2_closed=closed_d2M(p, part),
        Gamma_closed_11_20_at_mean=float(cm[f"s3_{part}"]),
        Gamma_closed_11_26=float(c0[f"s3_{part}"] + dbar * closed_d2M(p, part)),
        dev_mean_level=dev(Gmean), dev_level0=dev(G0), dev_first_order=dev(Gfirst),
        dev_mean_level_first_revolution=dev(Gmean, N), dev_level0_first_revolution=dev(G0, N))


say("\n=== new in v2, I3: reading statistics of the clock of a part, (11.19), (11.25), (11.26)")
say("start: bound eigenvector of the level 0 on every level, clock label in |0>, total label P=0 sharp, no records;")
say("readings at lambda = t*lambda_0, t = 0.25, 0.5, ..., 2N; deviation = max over a and t of |q - P_N(a; Gamma*t)|")
clock_runs = []
for name, part, N, D in (("E_order_one", 1, 4, 0.06), ("B_unequal_R", 1, 4, 0.10), ("B_unequal_R", 2, 5, 0.10)):
    prev = None
    for DD in (D, D / 2, D / 4):
        ticks = list(np.arange(1, 8 * N + 1) * 0.25)
        r = clock_check(SETS[name], part, N, DD, ticks)
        r["set"] = name
        if prev:
            r["ratio_to_previous"] = dict(dev_mean_level=prev["dev_mean_level"] / r["dev_mean_level"],
                                          dev_level0=prev["dev_level0"] / r["dev_level0"],
                                          dev_first_order=prev["dev_first_order"] / r["dev_first_order"])
        clock_runs.append(r)
        prev = r
        say(f"set {name}, clock of part {part}, N={N}, spread D={DD:.4f} (D/g0={r['D_over_g0']:.3f}, D/m={r['D_over_M']:.4f},"
            f" lambda_0={r['lambda0']:.2f})")
        say(f"  Gamma: level 0 (v1) {r['Gamma_level0']:.10f}; mean level (11.19) {r['Gamma_mean_level']:.10f};"
            f" first order (11.25) {r['Gamma_first_order']:.10f}; least-squares fit {r['Gamma_fit']:.10f}")
        say(f"  d2E_b/dM^2 at m: spectral sum {r['d2E_dM2']:+.8e}; closed form of (11.26) {r['d2E_dM2_closed']:+.8e};"
            f"  closed (11.20) at the mean level {r['Gamma_closed_11_20_at_mean']:.10f}; closed (11.26) {r['Gamma_closed_11_26']:.10f}")
        say(f"  deviation of the statistics: Gamma at the mean level {r['dev_mean_level']:.3e} (t<=N: {r['dev_mean_level_first_revolution']:.3e});"
            f" first order {r['dev_first_order']:.3e}; Gamma of the level 0 {r['dev_level0']:.3e} (t<=N: {r['dev_level0_first_revolution']:.3e})")
        if prev and "ratio_to_previous" in r:
            say("  ratios to the previous spread: " + ", ".join(f"{k} {v:.2f}" for k, v in r["ratio_to_previous"].items()))
say("expected for halving the spread at fixed lambda/lambda_0: 4 with Gamma at the mean level, 2 with Gamma of the level 0")
new["I3_clock"] = clock_runs

say("\n=== new in v2, I4: order of the contribution of w22 (set B, tau -> eps*tau, w -> eps^2*w)")
rows, prev = [], None
for eps in (2.0, 1.0, 0.5, 0.25):
    p = with_(base, tau1=eps * base["tau1"], tau2=eps * base["tau2"], w=[eps * eps * x for x in base["w"]])
    pz = with_(p, w=p["w"][:3] + [0.0])
    Ea, Xa, _ = dense(0.0, p, L)
    Ez, Xz, _ = dense(0.0, pz, L)
    ba, bz = int(np.argmax(np.abs(Xa[4 * L, :]) ** 2)), int(np.argmax(np.abs(Xz[4 * L, :]) ** 2))
    dE = float(Ea[ba] - Ez[bz])
    wt = 0.5 * float(np.abs(Xa[4 * L + 3, ba]) ** 2 + np.abs(Xz[4 * L + 3, bz]) ** 2)   # |<22|psi(0)>|^2
    row = dict(eps=eps, w22=p["w"][3], dE=dE, w22_times_weight=p["w"][3] * wt, weight_22_at_0=wt)
    if prev:
        row["ratio_to_previous"] = dict(dE=prev["dE"] / dE, weight_22_at_0=prev["weight_22_at_0"] / wt)
    rows.append(row)
    prev = row
    say(f"eps={eps:6.3f}  E_b(w22) - E_b(w22=0) = {dE:+.6e};  w22*|<22|psi(0)>|^2 = {row['w22_times_weight']:+.6e};"
        f"  |<22|psi(0)>|^2 = {wt:.6e}" + ("" if "ratio_to_previous" not in row else
        f";  ratios to the previous eps: dE {row['ratio_to_previous']['dE']:.2f}, weight {row['ratio_to_previous']['weight_22_at_0']:.2f}"))
say("expected for halving eps: 64 for the contribution of w22 to E_b (order eps^6), 16 for the weight (order eps^4)")
new["I4_w22"] = rows

say("\n=== new in v2, I5: equal data (a_1 = a_2) at P = pi/2, where j(P) = 0 (set A, tau -> eps*tau, w -> eps^2*w)")
rows, prev = [], None
baseA = SETS["A_equal_R"]
for eps in (1.0, 0.5, 0.25):
    p = with_(baseA, tau1=eps * baseA["tau1"], tau2=eps * baseA["tau2"], w=[eps * eps * x for x in baseA["w"]])
    E, X, _ = dense(0.5 * np.pi, p, L)
    b = int(np.argmax(np.abs(X[4 * L, :]) ** 2))
    a = p["tau1"] ** 2 / (4 * p["M1"]) + p["tau2"] ** 2 / (4 * p["M2"])
    row = dict(eps=eps, E=float(E[b]), closed_E=p["M1"] + p["M2"] + a + p["w"][0],
               dE=float(E[b] - (p["M1"] + p["M2"] + a + p["w"][0])),
               one_minus_weight_r0_11=float(1 - np.abs(X[4 * L, b]) ** 2),
               weight_r_not_0_in_11=float(np.sum(np.abs(X[0::4, b]) ** 2) - np.abs(X[4 * L, b]) ** 2))
    if prev:
        row["ratio_to_previous"] = dict(dE=prev["dE"] / row["dE"],
                                        one_minus_weight=prev["one_minus_weight_r0_11"] / row["one_minus_weight_r0_11"])
    rows.append(row)
    prev = row
    say(f"eps={eps:6.3f}  E_b = {row['E']:.12f}  M_1+M_2+a+w11 = {row['closed_E']:.12f}  difference {row['dE']:+.3e};"
        f"  1 - weight(r=0,11) = {row['one_minus_weight_r0_11']:.3e};  weight of 11 at r != 0: {row['weight_r_not_0_in_11']:.3e}"
        + ("" if "ratio_to_previous" not in row else f";  ratios: dE {row['ratio_to_previous']['dE']:.2f},"
           f" 1-weight {row['ratio_to_previous']['one_minus_weight']:.2f}"))
say("expected: psi_P = delta_{r,0}|11> up to O(eps) (1 - weight of order eps^2), E_b = M_1+M_2+a+w11 up to O(eps^4)")
new["I5_j_zero"] = rows


def degenerate_check(p, P0, E0):
    """I2: a twofold bound level. On-site binding W0 = -G(E0,P0)^(-1) on span(|11>,|22>) (G of Step 6),
    diagonal on |12>,|21>; then 1 + G W0 vanishes on that span and E0 is a twofold level of H(P0)."""
    Gd = green_direct(E0, P0, p)
    blk = np.ix_([0, 3], [0, 3])
    W0 = np.diag([0.0, 0.15, -0.10, 0.0]).astype(complex)
    W0[blk] = -np.linalg.inv(Gd[blk])
    W0 = 0.5 * (W0 + W0.conj().T)
    par0 = dict(P=P0, M1=p["M1"], M2=p["M2"], tau1=p["tau1"], tau2=p["tau2"], theta=1.0)
    eta = 0.5

    def at(**kw):
        v = dict(par0)
        v.update(kw)
        pp = with_(p, M1=v["M1"], M2=v["M2"], tau1=v["tau1"], tau2=v["tau2"])
        E, X, ops = dense(v["P"], pp, L, eta=eta, W0=W0, theta=v["theta"])
        return E, X, ops, np.argsort(np.abs(E - E0))

    E, X, ops, idx = at()
    pair = idx[:2]
    Eb = float(E[pair].mean())
    Phi = X[:, pair]                                # orthonormal basis of the level, as returned by the solver
    rest = np.ones(len(E), bool)
    rest[pair] = False
    Veta = eta * ops["V1"] + (1 - eta) * ops["V2"]
    dH = dict(M1=ops["Z1"], M2=ops["Z2"], tau1=ops["A1"] / p["tau1"], tau2=ops["A2"] / p["tau2"], theta=ops["U"], P=Veta)
    amp = X[:, rest].conj().T @ (Veta @ Phi)
    h2P = Phi.conj().T @ ((-(eta ** 2) * ops["A1"] - (1 - eta) ** 2 * ops["A2"]) @ Phi) \
        - 2 * amp.conj().T @ (amp / (E[rest] - Eb)[:, None])      # second-order matrix of (11.24)
    steps = dict(P=HP, M1=HX * p["M1"], M2=HX * p["M2"], tau1=HX * p["tau1"], tau2=HX * p["tau2"], theta=HX)
    r_lab = np.repeat(np.arange(-L, L + 1), 4)
    out = dict(P0=P0, E0=E0, W0_block_11_22=np.real(W0[blk]).tolist(), level=Eb, splitting=float(abs(E[pair[0]] - E[pair[1]])),
               isolation=float(abs(E[idx[2]] - Eb)), tail=float(np.sum(np.abs(Phi[np.abs(r_lab) > L // 2]) ** 2)), xi={})
    bases = {}
    for xi, O in dH.items():
        h = Phi.conj().T @ (O @ Phi)
        e, c = np.linalg.eigh(h)
        second_order = bool(xi == "P" and abs(e[1] - e[0]) < 1e-8)
        if second_order:                             # equal first derivatives: branch vectors from the second order
            c = c @ np.linalg.eigh(c.conj().T @ h2P @ c)[1]
        B = Phi @ c                                  # branch vectors of the parameter xi
        bases[xi] = c
        vals, quality = {}, 1.0
        for s in (-2, -1, 1, 2):
            E_, X_, _, idx_ = at(**{xi: par0[xi] + s * steps[xi]})
            pr = idx_[:2]
            ov = np.abs(B.conj().T @ X_[:, pr]) ** 2          # [branch, eigenvector]
            j0 = int(np.argmax(ov[0]))
            vals[(0, s)], vals[(1, s)] = float(E_[pr[j0]]), float(E_[pr[1 - j0]])
            quality = min(quality, float(ov[0, j0]), float(ov[1, 1 - j0]))
        hh = steps[xi]
        res = dict(branch_overlap_min=quality, second_order_branches=second_order,
                   matrix_eigenvalues=[float(np.real(np.vdot(c[:, n], h @ c[:, n]))) for n in (0, 1)],
                   slopes_finite_difference=[(-vals[(n, 2)] + 8 * vals[(n, 1)] - 8 * vals[(n, -1)] + vals[(n, -2)]) / (12 * hh)
                                             for n in (0, 1)])
        res["max_abs_deviation"] = float(max(abs(a - b) for a, b in zip(res["matrix_eigenvalues"], res["slopes_finite_difference"])))
        if xi == "P":
            res["second_derivative_11_24"] = [float(np.real(np.vdot(c[:, n], h2P @ c[:, n]))) for n in (0, 1)]
            res["second_derivative_finite_difference"] = [
                (-vals[(n, 2)] + 16 * vals[(n, 1)] - 30 * Eb + 16 * vals[(n, -1)] - vals[(n, -2)]) / (12 * hh * hh) for n in (0, 1)]
            res["max_abs_deviation_second"] = float(max(abs(a - b) for a, b in zip(
                res["second_derivative_11_24"], res["second_derivative_finite_difference"])))
            # the term that (11.9) with Q_P = 1 - |psi><psi| would contain for the other vector of the level
            res["term_of_11_9_from_the_level"] = dict(numerator=float(abs(np.vdot(Phi[:, 1], Veta @ Phi[:, 0])) ** 2),
                                                      denominator=float(E[pair[1]] - E[pair[0]]))
        out["xi"][xi] = res
    # identities for every eigenvector of the level
    rng = np.random.default_rng(11)
    worst = dict(euler=0.0, V12=0.0, mean_rule=0.0)
    for _ in range(5):
        cc = rng.normal(size=2) + 1j * rng.normal(size=2)
        cc /= np.linalg.norm(cc)
        psi = Phi @ cc
        ex = lambda O: float(np.real(np.vdot(psi, O @ psi)))
        worst["euler"] = max(worst["euler"], abs(p["M1"] * ex(ops["Z1"]) + p["M2"] * ex(ops["Z2"]) + ex(ops["A1"])
                                                 + ex(ops["A2"]) + ex(ops["U"]) - Eb))
        worst["V12"] = max(worst["V12"], abs(ex(ops["V1"]) - ex(ops["V2"])))
        for xi in ("M1", "theta"):
            wts = np.abs(bases[xi].conj().T @ cc) ** 2
            worst["mean_rule"] = max(worst["mean_rule"], abs(ex(dH[xi]) - float(wts @ np.array(out["xi"][xi]["slopes_finite_difference"]))))
    out["every_eigenvector"] = dict(worst, norm_Pi_V1_minus_V2_Pi=float(np.linalg.norm(Phi.conj().T @ ((ops["V1"] - ops["V2"]) @ Phi))))
    # the branch vectors of different parameters
    out["overlap_of_branch_0_of_M1_with_branch_0_of"] = {xi: float(abs(np.vdot(bases["M1"][:, 0], bases[xi][:, 0])) ** 2)
                                                         for xi in dH if xi != "M1"}
    hU = Phi.conj().T @ (ops["U"] @ Phi)
    out["U_in_the_branch_vectors_of_M1"] = [float(np.real(np.vdot(bases["M1"][:, n], hU @ bases["M1"][:, n]))) for n in (0, 1)]
    return out


say("\n=== new in v2, I2: twofold bound levels (on-site binding W0 = -G(E0,P0)^(-1) on span(|11>,|22>))")
pX = dict(M1=1.0, M2=0.7, tau1=0.5, tau2=0.35, w=[0.0, 0.0, 0.0, 0.0])
deg = {}
for label, P0 in (("X_P0_0.3", 0.3), ("X_P0_0", 0.0)):
    o = degenerate_check(pX, P0, 1.0)
    deg[label] = o
    bd = {k: (round(v[0], 4), round(v[1], 4)) for k, v in bands(P0, pX).items()}
    say(f"set {label}: M = {pX['M1']}, {pX['M2']}; tau = {pX['tau1']}, {pX['tau2']}; P0 = {P0};"
        f" W0 on (11,22) = {np.round(o['W0_block_11_22'], 6).tolist()}; bands {bd}")
    say(f"  level {o['level']:.12f}, splitting of the two eigenvalues {o['splitting']:.2e}, distance to the next eigenvalue {o['isolation']:.4f},"
        f" weight at |r|>L/2 {o['tail']:.1e}")
    for xi, r in o["xi"].items():
        say(f"  {xi:5s}: eigenvalues of Pi dH Pi {r['matrix_eigenvalues'][0]:+.9f}, {r['matrix_eigenvalues'][1]:+.9f};"
            f" slopes of the branches (finite differences) {r['slopes_finite_difference'][0]:+.9f}, {r['slopes_finite_difference'][1]:+.9f};"
            f" max dev {r['max_abs_deviation']:.1e}; overlap with the branch vectors >= {r['branch_overlap_min']:.6f}"
            + ("; branch vectors from the second order" if r["second_order_branches"] else ""))
        if xi == "P":
            say(f"         E'' of the branches: (11.24) {r['second_derivative_11_24'][0]:+.8f}, {r['second_derivative_11_24'][1]:+.8f};"
                f" finite differences {r['second_derivative_finite_difference'][0]:+.8f}, {r['second_derivative_finite_difference'][1]:+.8f};"
                f" max dev {r['max_abs_deviation_second']:.1e}")
            t = r["term_of_11_9_from_the_level"]
            say(f"         (11.9) with Q_P = 1 - |psi><psi|, term of the other vector of the level in the basis of the solver:"
                f" |<psi'|V_eta|psi>|^2 = {t['numerator']:.3e} over E' - E = {t['denominator']:.3e}")
    ev = o["every_eigenvector"]
    say(f"  every eigenvector (5 random vectors of the level): residual of (11.6) {ev['euler']:.1e}; <V1> - <V2> {ev['V12']:.1e};"
        f" ||Pi (V1 - V2) Pi|| {ev['norm_Pi_V1_minus_V2_Pi']:.1e}; <dH> - weighted mean of the branch slopes (M1, theta) {ev['mean_rule']:.1e}")
    say("  |<branch 0 of M1 | branch 0 of xi>|^2: " + ", ".join(f"{k} {v:.4f}" for k, v in o["overlap_of_branch_0_of_M1_with_branch_0_of"].items()))
    say(f"  <U> in the two branch vectors of M1: {o['U_in_the_branch_vectors_of_M1'][0]:+.6f}, {o['U_in_the_branch_vectors_of_M1'][1]:+.6f}"
        f"  against the slopes of the branches of theta: {o['xi']['theta']['slopes_finite_difference'][0]:+.6f}, {o['xi']['theta']['slopes_finite_difference'][1]:+.6f}")
new["I2_degenerate"] = deg


def listing_check():
    """I1: C_bod = <chi|C|chi> of (11.21) on a small system given in the places (two bodies with a branch
    label on an open chain of 4 positions, a medium with 3 places)."""
    rng = np.random.default_rng(5)
    n, dc = 4, 3
    hop = np.eye(n, k=-1)

    def body(tau, M):
        return 0.5 * tau * (np.kron(hop, -1j * sx) + np.kron(hop.T, 1j * sx)) + M * np.kron(np.eye(n), sz)

    I8, Ic = np.eye(2 * n), np.eye(dc)
    xh = np.kron(np.diag(np.arange(n, dtype=float)), np.eye(2))
    C1, C2 = np.kron(body(0.6, 1.0), I8), np.kron(I8, body(0.45, 0.7))
    x12 = np.kron(xh, I8) + np.kron(I8, xh)
    U = np.zeros((64, 64))
    wv = np.array([[-0.5, 0.2], [-0.15, 0.3]])
    for x in range(n):
        for s1 in range(2):
            for s2 in range(2):
                i = (2 * x + s1) * 8 + 2 * x + s2
                U[i, i] = wv[s1, s2]
    Cpair = C1 + C2 + U
    Xr = rng.normal(size=(dc, dc)) + 1j * rng.normal(size=(dc, dc))
    Xr = 0.5 * (Xr + Xr.conj().T)
    chi = rng.normal(size=dc) + 1j * rng.normal(size=dc)
    chi /= np.linalg.norm(chi)
    mean = float(np.real(np.vdot(chi, Xr @ chi)))
    Xc = Xr - mean * Ic                               # <chi|Xc|chi> = 0
    phi = rng.normal(size=64) + 1j * rng.normal(size=64)
    phi /= np.linalg.norm(phi)
    alpha = np.kron(0.3 * np.kron(np.eye(n), sz) + 0.2 * np.eye(8), I8)             # h*sigma3 of b_1 and a constant
    beta = np.kron(I8, 0.25 * 0.5 * 0.45 * (np.kron(hop, -1j * sx) + np.kron(hop.T, 1j * sx)) - 0.1 * np.eye(8))

    def bod(C):
        return np.einsum("a,iajb,b->ij", chi.conj(), C.reshape(64, dc, 64, dc), chi)

    def evolve(G, v, lam):
        E, Y = np.linalg.eigh(G)
        return Y @ (np.exp(-1j * E * lam) * (Y.conj().T @ v))

    out, lam = dict(scan=[]), 3.0
    for kappa in (0.04, 0.02, 0.01):
        row = dict(kappa=kappa)
        for tag, Xm in (("centred", Xc), ("not_centred", Xr)):
            C = np.kron(Cpair, Ic) + kappa * np.kron(x12, Xm)                       # listing of the question
            CB = np.kron(Cpair - alpha - beta, Ic) + (kappa * np.kron(x12, Xm) + np.kron(alpha + beta, Ic))   # another listing
            Cbod = bod(C)
            Psi = evolve(C, np.kron(phi, chi), lam).reshape(64, dc)
            view = Psi @ Psi.conj().T
            proj = lambda v: np.outer(v, v.conj())
            row[tag] = dict(
                total_contract_listing_B_minus_A=float(np.linalg.norm(CB - C)),
                Cbod_listing_B_minus_A=float(np.linalg.norm(bod(CB) - Cbod)),
                Cbod_minus_listed_Cpair_A=float(np.linalg.norm(Cbod - Cpair)),
                Cbod_minus_listed_Cpair_A_minus_gradient=float(np.linalg.norm(
                    Cbod - Cpair - kappa * (mean if tag == "not_centred" else 0.0) * x12)),
                Cbod_minus_listed_Cpair_B=float(np.linalg.norm(Cbod - (Cpair - alpha - beta))),
                view_minus_evolution_by_Cbod=float(np.linalg.norm(view - proj(evolve(Cbod, phi, lam)))),
                view_minus_evolution_by_listed_Cpair_A=float(np.linalg.norm(view - proj(evolve(Cpair, phi, lam)))),
                view_minus_evolution_by_listed_Cpair_B=float(np.linalg.norm(view - proj(evolve(Cpair - alpha - beta, phi, lam)))))
        out["scan"].append(row)
    out["mean_of_X_not_centred"] = mean
    return out


say("\n=== new in v2, I1: the operator C_bod = <chi|C|chi> of (11.21), small system in the places (dimension 64 x 3)")
lc = listing_check()
say(f"listing A: the terms of the question; listing B: h*sigma3 of b_1, a constant and a part of the motion term of b_2 listed"
    f" in the record terms; <chi|X|chi> = {lc['mean_of_X_not_centred']:+.4f} for the medium that is not centred; lambda = 3")
for row in lc["scan"]:
    for tag in ("centred", "not_centred"):
        r = row[tag]
        say(f"kappa={row['kappa']:.3f} {tag:11s}: ||C_B - C_A|| {r['total_contract_listing_B_minus_A']:.1e};"
            f" ||C_bod(B) - C_bod(A)|| {r['Cbod_listing_B_minus_A']:.1e}; ||C_bod - C_pair(A)|| {r['Cbod_minus_listed_Cpair_A']:.3e}"
            f" (minus the gradient: {r['Cbod_minus_listed_Cpair_A_minus_gradient']:.1e}); ||C_bod - C_pair(B)|| {r['Cbod_minus_listed_Cpair_B']:.3f};"
            f" view against evolution by C_bod {r['view_minus_evolution_by_Cbod']:.3e}, by C_pair(A) {r['view_minus_evolution_by_listed_Cpair_A']:.3e},"
            f" by C_pair(B) {r['view_minus_evolution_by_listed_Cpair_B']:.3f}")
say("expected for halving kappa: the view against the evolution by C_bod falls by 4 (second order);"
    " by the listed C_pair(A) with a medium that is not centred it falls by 2")
new["I1_listing"] = lc
results["new_in_v2"] = new

(OUT / "check_bound_pair.json").write_text(json.dumps(results, indent=1), encoding="utf-8")
(OUT / "check_bound_pair.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
