"""Check of 07-ilang-weight/04-weight-of-bond, derivation v1.

N_f = 1 field object, t_f = 1, held pair (g1 at x1, g2 at x2 = x1 + r) and held
source (g_s at x_s = 0).  The exact lowest eigenvalue of h = C_1 + sum_i g_i P_{x_i}
(dense diagonalisation) is compared with the formulas (4.1)-(4.13).
Run from the project root:
  .venv/Scripts/python.exe 07-ilang-weight/04-weight-of-bond/code/v1/check_weight_of_bond.py
"""
import itertools
from pathlib import Path

import numpy as np
from scipy.linalg import eigh

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
LOG = []


def log(s=""):
    print(s)
    LOG.append(s)


def hop(D, L):
    """C_1 = -t_f * adjacency of the D-torus of side L (t_f = 1)."""
    N = L ** D
    co = np.array(list(itertools.product(range(L), repeat=D)))
    H = np.zeros((N, N))
    for mu in range(D):
        sh = co.copy()
        sh[:, mu] = (sh[:, mu] + 1) % L
        j = np.ravel_multi_index(sh.T, (L,) * D)
        H[np.arange(N), j] -= 1.0
        H[j, np.arange(N)] -= 1.0
    return H


def tables(D, L):
    """ell = Lambda^+ and ell2 = (Lambda^+)^2 as functions of the displacement (FFT)."""
    k = 2 * np.pi * np.fft.fftfreq(L)
    g = np.meshgrid(*([k] * D), indexing="ij")
    om = sum(4 * np.sin(x / 2) ** 2 for x in g)
    inv = np.zeros_like(om)
    inv[om > 1e-12] = 1 / om[om > 1e-12]
    return np.real(np.fft.ifftn(inv)), np.real(np.fft.ifftn(inv ** 2))


def site(x, L):
    return int(np.ravel_multi_index(tuple(np.mod(x, L)), (L,) * len(x)))


def emin(H0, pts, top=False):
    H = H0.copy()
    for i, g in pts:
        H[i, i] += g
    n = H.shape[0]
    idx = [n - 1, n - 1] if top else [0, 0]
    return eigh(H, eigvals_only=True, subset_by_index=idx)[0]


class Graph:
    def __init__(self, D, L, build=True):
        self.D, self.L, self.X = D, L, L ** D
        self.l, self.l2 = tables(D, L)
        self.H0 = hop(D, L) if build else None

    def ell(self, a):
        return self.l[tuple(np.mod(a, self.L))]

    def ell2(self, a):
        return self.l2[tuple(np.mod(a, self.L))]

    def S(self, x1, x2, xs):
        """bracket of (4.6) without the x1-independent ell2(r) term."""
        l12, l1s, l2s = self.ell(x2 - x1), self.ell(x1 - xs), self.ell(x2 - xs)
        return l12 * (l1s + l2s) + l1s * l2s - (self.ell2(x1 - xs) + self.ell2(x2 - xs)) / self.X

    def rho0(self, x1, r, rp, e, xs):
        """leading-order ratio (4.10), lattice differences."""
        num = (self.S(x1 + e, x1 + e + r, xs) - self.S(x1, x1 + r, xs)) - (
            self.S(x1 + e, x1 + e + rp, xs) - self.S(x1, x1 + rp, xs))
        den = 2 * (self.ell(r) - self.ell(rp)) * (self.ell(x1 + e - xs) - self.ell(x1 - xs))
        return num / den

    def rho0_mid(self, xb, r, rp, e, xs):
        """leading-order ratio (4.12) with the midpoint xb as the place (r, rp with even components)."""
        S = lambda y, rr: self.S(y - rr // 2, y + rr // 2, xs)
        num = (S(xb + e, r) - S(xb, r)) - (S(xb + e, rp) - S(xb, rp))
        den = 2 * (self.ell(r) - self.ell(rp)) * (self.ell(xb + e - xs) - self.ell(xb - xs))
        return num / den


# Model D levels: M_k = m + 2 pi k / (N lambda_0), m = 1, N = 4, lambda_0 = pi
def Mk(k):
    return 1.0 + 0.5 * k


GAM2 = 0.6  # gamma_2 / gamma_1 (unequal bodies)
CHOICES = {  # (k1, s1, k2, s2) and the second level of each body used for its cost difference
    "A (k1,s1,k2,s2)=(0,+,1,+)": ((0, 1, 1, 1), ((1, 1), (2, 1))),
    "B (k1,s1,k2,s2)=(2,-,3,+)": ((2, -1, 3, 1), ((2, 1), (0, 1))),
}
ETAS = [0.08, 0.04, 0.02]


def run_exact(G, x1, r, rp, e, xb, rm, rmp, label):
    D, L, X = G.D, G.L, G.X
    xs = np.zeros(D, int)
    l0 = G.ell(np.zeros(D, int))
    gs = 0.01 / l0
    n = 1.0 / X
    s = lambda x: site(x, L)
    log(f"\n--- {label}: L={L}, x1={x1.tolist()}, r={r.tolist()}, r'={rp.tolist()}, e={e.tolist()}; "
        f"midpoint version: xbar={xb.tolist()}, r={rm.tolist()}, r'={rmp.tolist()}; ell_0={l0:.4f}, g_s={gs:.4g}")
    log(" choice | eta | rel.dev bond profile (4.2) | rel.dev W_1 (4.5) | rel.dev W_b (4.6) | "
        "rho_ex(full grip) | rho0 (4.10) | rho_ex(a)/[(1+n g1)/(n g1) rho0] (4.13) | rho_mid_ex vs rho0_mid (4.12)")
    rho_th = G.rho0(x1, r, rp, e, xs)
    rho_mid_th = G.rho0_mid(xb, rm, rmp, e, xs)
    for cname, ((k1, s1, k2, s2), lev2) in CHOICES.items():
        devs = []
        for eta in ETAS:
            gam1 = eta / l0 / 2.5
            gam = (gam1, GAM2 * gam1)
            g1, g2 = s1 * gam[0] * Mk(k1), s2 * gam[1] * Mk(k2)

            def E(pts, src):
                return emin(G.H0, pts + ([(s(xs), src)] if src else []))

            def coef(pts):  # coefficient of g_s (symmetric difference)
                return (E(pts, gs) - E(pts, -gs)) / (2 * gs)

            def Wb_ex(y1, y2):
                return (coef([(s(y1), g1), (s(y2), g2)]) - coef([(s(y1), g1)])
                        - coef([(s(y2), g2)]) + coef([]))

            def Wb_th(y1, y2):
                return 2 * n * g1 * g2 * (G.S(y1, y2, xs) - G.ell2(y2 - y1) / X)

            # item 1: bond profile
            Bex = E([(s(x1), g1), (s(x1 + r), g2)], 0) - E([(s(x1), g1), (s(x1 + rp), g2)], 0)
            Bth = -2 * n * g1 * g2 * (G.ell(r) - G.ell(rp))
            # item 2: single body 1 and bond part
            W1ex = coef([(s(x1 + e), g1)]) - coef([(s(x1), g1)])
            W1th = sum(sgn * (-2 * n * g1 * G.ell(y) + n * g1 ** 2 * (2 * l0 * G.ell(y) + G.ell(y) ** 2
                                                                     - 2 * G.ell2(y) / X))
                       for sgn, y in ((1, x1 + e), (-1, x1)))
            Wex = {}
            for tag, y1, y2 in (("r", x1, x1 + r), ("rp", x1, x1 + rp), ("er", x1 + e, x1 + e + r),
                                ("erp", x1 + e, x1 + e + rp)):
                Wex[tag] = (Wb_ex(y1, y2), Wb_th(y1, y2))
            num_ex = (Wex["er"][0] - Wex["r"][0]) - (Wex["erp"][0] - Wex["rp"][0])
            dWb_ex = Wex["er"][0] - Wex["r"][0]
            dWb_th = Wex["er"][1] - Wex["r"][1]

            # single-body place function F_i from level differences (full grip and coupling (a))
            def F(i, coupling, y):
                kk, ss = ((k1, s1), (k2, s2))[i]
                kq, sq = lev2[i]
                ga = gam[i]
                gA, gB = ss * ga * Mk(kk), sq * ga * Mk(kq)
                rest = (ss * Mk(kk) - sq * Mk(kq)) if coupling == "a" else 0.0
                dW = (coef([(s(y + e), gA)]) - coef([(s(y), gA)])) - (
                    coef([(s(y + e), gB)]) - coef([(s(y), gB)]))
                dC = rest + E([(s(y), gA)], 0) - E([(s(y), gB)], 0)
                return dW / dC

            rho_fg = [num_ex / (Bex * F(i, "fg", x1)) for i in (0, 1)]
            rho_a = [num_ex / (Bex * F(i, "a", x1)) for i in (0, 1)]
            pred_a = [(1 + n * gam[i]) / (n * gam[i]) * rho_th for i in (0, 1)]
            # midpoint version, full grip, relative to body 1
            h = lambda rr: rr // 2
            Bm = (E([(s(xb - h(rm)), g1), (s(xb + h(rm)), g2)], 0)
                  - E([(s(xb - h(rmp)), g1), (s(xb + h(rmp)), g2)], 0))
            num_m = ((Wb_ex(xb + e - h(rm), xb + e + h(rm)) - Wb_ex(xb - h(rm), xb + h(rm)))
                     - (Wb_ex(xb + e - h(rmp), xb + e + h(rmp)) - Wb_ex(xb - h(rmp), xb + h(rmp))))
            rho_m = num_m / (Bm * F(0, "fg", xb))
            dev = (abs(Bex / Bth - 1), abs(W1ex / W1th - 1), abs(dWb_ex / dWb_th - 1),
                   abs(rho_fg[0] / rho_th - 1), abs(rho_fg[1] / rho_th - 1),
                   abs(rho_a[0] / pred_a[0] - 1), abs(rho_a[1] / pred_a[1] - 1), abs(rho_m / rho_mid_th - 1))
            devs.append(dev)
            log(f" {cname[:1]} | {eta:.2f} | {dev[0]:.2e} | {dev[1]:.2e} | {dev[2]:.2e} | "
                f"{rho_fg[0]:.5f} (body1), {rho_fg[1]:.5f} (body2) | {rho_th:.5f} | "
                f"{rho_a[0] / pred_a[0]:.5f}, {rho_a[1] / pred_a[1]:.5f} | {rho_m:.5f} vs {rho_mid_th:.5f}")
        d = np.array(devs)
        ratios = d[:-1] / d[1:]
        log(f" {cname[:1]} | dev(eta)/dev(eta/2) for eta=0.08; 0.04, columns [profile, W_1, W_b, "
            "rho_fg body1, rho_fg body2, rho_a body1, rho_a body2, rho_mid]: "
            + "; ".join(" ".join(f"{x:.2f}" for x in row) for row in ratios))


def main():
    log("Check of 04-weight-of-bond v1 (N_f = 1, t_f = 1)")
    log("Couplings g_i = sigma_i gamma_i M_{k_i}, gamma_1 = eta/(2.5 ell_0), gamma_2 = 0.6 gamma_1;"
        " rel.dev = |exact/formula - 1|.")
    log("Expected: rel.dev of the third-order formulas proportional to eta (ratio ~2 when eta halves).")

    # ---------- exact eigenvalue checks, two sizes per graph ----------
    setups = [  # D, L, x1, r, r', e, xbar, r_mid, r'_mid
        (1, 30, [6], [3], [2], [1], [8], [4], [2]), (1, 60, [12], [6], [5], [1], [16], [8], [4]),
        (2, 12, [4, 0], [1, 1], [2, 2], [1, 0], [4, 0], [0, 2], [2, 2]),
        (2, 20, [6, 0], [1, 1], [2, 2], [1, 0], [6, 0], [0, 2], [2, 2]),
        (3, 8, [3, 0, 0], [0, 1, 0], [1, 1, 1], [1, 0, 0], [3, 0, 0], [0, 2, 0], [2, 2, 0]),
        (3, 10, [4, 0, 0], [0, 1, 0], [1, 1, 1], [1, 0, 0], [4, 0, 0], [0, 2, 0], [2, 2, 0]),
    ]
    for D, L, *geo in setups:
        G = Graph(D, L)
        run_exact(G, *[np.array(v) for v in geo], f"graph D={D}")

    # ---------- mirrored (highest) state on even L ----------
    log("\n--- mirror identity max spec h(g) = -min spec h(-g) (even L):")
    rng = np.random.default_rng(1)
    for D, L in ((1, 30), (2, 12), (3, 8)):
        G = Graph(D, L)
        pts = [(int(rng.integers(L ** D)), float(rng.normal()) * 0.3) for _ in range(3)]
        top = emin(G.H0, pts, top=True)
        low = emin(G.H0, [(i, -g) for i, g in pts])
        log(f" D={D}, L={L}: max + min(-g) = {top + low:.2e}")

    # ---------- sum rule (consistency check 3) ----------
    log("\n--- sum over x1 of the full g_s g1 g2 coefficient of (4.6) (incl. -ell2(r)/X): ")
    for D, L in ((1, 30), (2, 12), (3, 8)):
        G = Graph(D, L, build=False)
        xs = np.zeros(D, int)
        r = np.array([2] + [1] * (D - 1))
        tot = sum(G.S(np.array(x1), np.array(x1) + r, xs) - G.ell2(r) / G.X
                  for x1 in itertools.product(range(L), repeat=D))
        log(f" D={D}, L={L}: sum = {tot:.2e}")

    # ---------- item 1: ring closed form and torus forms ----------
    log("\n--- (4.3) ring: max |ell(r) - [(L^2-1)/(12L) - r(L-r)/(2L)]|:")
    for L in (30, 61, 200):
        G = Graph(1, L, build=False)
        rr = np.arange(L)
        log(f" L={L}: {np.max(np.abs(G.l - ((L*L-1)/(12*L) - rr*(L-rr)/(2*L)))):.2e}")
    log("--- (4.4) 2D: ell(0)-ell(r e1) - [ln r/(2 pi) + (2 gamma_E + 3 ln 2)/(4 pi)]:")
    cst2 = (2 * np.euler_gamma + 3 * np.log(2)) / (4 * np.pi)
    for L in (256, 1024):
        G = Graph(2, L, build=False)
        out = []
        for rr in (2, 4, 8, 16, 32):
            out.append(f"r={rr}: {G.l[0, 0] - G.l[rr, 0] - (np.log(rr) / (2 * np.pi) + cst2):+.2e}")
        log(f" L={L}: " + ", ".join(out))
    log("--- (4.4) 3D: ell(0)-ell(r e1) - [G_0 - 1/(4 pi r)], G_0 = 0.2527310098:")
    for L in (64, 128):
        G = Graph(3, L, build=False)
        out = []
        for rr in (2, 4, 8, 16):
            out.append(f"r={rr}: {G.l[0, 0, 0] - G.l[rr, 0, 0] - (0.2527310098 - 1 / (4 * np.pi * rr)):+.2e}")
        log(f" L={L}: " + ", ".join(out))

    # ---------- item 3: rho0 on large graphs, distance scaling ----------
    log("\n--- (4.12) ring: lattice rho0 (e=+1, r'=r-1) vs 2(1-w)(1-2w)/((1-2u)(1-2v)),"
        " u=(d+1/2)/L, v=(r-1/2)/L, w=u+v:")
    for (uu, vv) in ((0.2, 0.1), (0.1, 0.05), (0.6, 0.2)):
        row = []
        for L in (40, 80, 160, 320):
            G = Graph(1, L, build=False)
            d, rr = int(round(uu * L)), int(round(vv * L))
            lat = G.rho0(np.array([d]), np.array([rr]), np.array([rr - 1]), np.array([1]), np.array([0]))
            u, v = (d + 0.5) / L, (rr - 0.5) / L
            w = u + v
            fo = 2 * (1 - w) * (1 - 2 * w) / ((1 - 2 * u) * (1 - 2 * v))
            row.append(f"L={L}: {lat:.5f} vs {fo:.5f} (diff {lat - fo:+.1e})")
        log(f" u={uu}, v={vv}: " + "; ".join(row))
    log(" small-v limit 2(1-u): u=0.2 -> 1.6; u=0.1 -> 1.8")

    log("\n--- (4.11) 3D, L=128: rho0 - 1 and, in brackets, d*(rho0 - 1) vs d (x1=(d,0,0), e=e1):")
    G = Graph(3, 128, build=False)
    xs = np.zeros(3, int)
    for rv, rpv in (((0, 1, 0), (1, 1, 1)), ((0, 2, 0), (2, 3, 0)), ((0, 1, 0), (0, 2, 0)),
                    ((1, 0, 0), (2, 0, 0))):
        row = []
        for d in (8, 16, 32):
            rho = G.rho0(np.array([d, 0, 0]), np.array(rv), np.array(rpv), np.array([1, 0, 0]), xs)
            row.append(f"d={d}: {rho - 1:+.3e} ({d * (rho - 1):+.3f})")
        log(f" r={rv}, r'={rpv}: " + ", ".join(row))
    log("\n--- (4.11) 2D: rho0 - 1 and, in brackets, d*(rho0 - 1) vs d and L"
        " (x1=(d,0), e=e1, r=(2,1), r'=(4,3)):")
    for L in (128, 512, 2048):
        G = Graph(2, L, build=False)
        row = []
        for d in (8, 16, 32, 64):
            rho = G.rho0(np.array([d, 0]), np.array([2, 1]), np.array([4, 3]), np.array([1, 0]),
                         np.zeros(2, int))
            row.append(f"d={d}: {rho - 1:+.3e} ({d * (rho - 1):+.3f})")
        log(f" L={L}: " + ", ".join(row))

    log("\n--- (4.12) midpoint place: rho0_mid - 1 (ring; expected 0 up to rounding):")
    for L in (40, 160):
        G = Graph(1, L, build=False)
        row = []
        for db, rr, rrp in ((L // 4, 4, 2), (L // 5, 10, 4), (3 * L // 5, 12, 6)):
            k = G.rho0_mid(np.array([db]), np.array([rr]), np.array([rrp]), np.array([1]), np.array([0])) - 1
            row.append(f"(dbar,r,r')=({db},{rr},{rrp}): {k:+.1e}")
        log(f" L={L}: " + ", ".join(row))
    log("--- (4.12) midpoint place, 2D: rho0_mid - 1 and, in brackets, d^2*(rho0_mid - 1)"
        " (xbar=(d,0), e=e1, r=(2,2), r'=(4,2)):")
    for L in (128, 512, 2048):
        G = Graph(2, L, build=False)
        row = []
        for d in (8, 16, 32, 64):
            k = G.rho0_mid(np.array([d, 0]), np.array([2, 2]), np.array([4, 2]), np.array([1, 0]),
                           np.zeros(2, int)) - 1
            row.append(f"d={d}: {k:+.3e} ({d * d * k:+.1f})")
        log(f" L={L}: " + ", ".join(row))
    log("--- (4.12) midpoint place, 3D, L=128: rho0_mid - 1 and, in brackets, d^2*(rho0_mid - 1)"
        " (xbar=(d,0,0), e=e1):")
    G = Graph(3, 128, build=False)
    for rv, rpv in (((0, 2, 0), (2, 2, 2)), ((2, 0, 0), (4, 2, 0))):
        row = []
        for d in (8, 16, 32):
            k = G.rho0_mid(np.array([d, 0, 0]), np.array(rv), np.array(rpv), np.array([1, 0, 0]),
                           np.zeros(3, int)) - 1
            row.append(f"d={d}: {k:+.3e} ({d * d * k:+.2f})")
        log(f" r={rv}, r'={rpv}: " + ", ".join(row))

    log("\n--- 3D large separations (consistency check 2): W_b / (2 n g1 g2) = S - ell2(r)/X"
        " at |r|, d ~ L/4 shrinks with L:")
    for L in (16, 32, 64):
        G = Graph(3, L, build=False)
        q = L // 4
        val = G.S(np.array([q, 0, 0]), np.array([q, q, 0]), np.zeros(3, int)) - G.ell2(np.array([0, q, 0])) / G.X
        log(f" L={L}: {val:.3e}")

    (OUT / "check_weight_of_bond.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
