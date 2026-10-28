"""Check for 08-ilang-propagation/05-anchor, derivation v3.

Field of oscillator cells without pinning, anchor (kappa_a/2) q_h^2, held bodies with grips
F(q) = F0 + F1 q + F2 q^2, held sources g q_xs.  In a sector of the held bodies the uncompressed
contract is C_f = 1/2 p.p + 1/2 q.A q + b.q + c0, and for A > 0 its exact lowest eigenvalue is
E0 = c0 + 1/2 Tr sqrt(A) - 1/2 b.A^{-1}.b  (computed here by dense or sparse linear algebra).
The script compares this with the closed forms of the derivation:
 (i)   existence conditions (5.4)-(5.6), (5.10), the pair criterion (5.26), and a pair whose bodies
       meet the one-body condition while the pair does not;
 (ii)  mutual cost of two sources (5.14)-(5.16) against the separation, two distances from the anchor;
 (iii) cost, weight, bond and the ratios rho_mark, rho_bond,i (5.18)-(5.22), two levels,
       both branches, three distances from the anchor; bonds for common square, non-square,
       8F0F2=F1^2 and linear grips and for a mixed (square, non-square) pair, with the existence of
       the pair block at s = 1;
 plus the asymptotic statements (5.13), (5.15), (5.23)-(5.25), the mirror placement of (5.27), the pair
 control of (5.27) (N/D -> 0 while a_bond does not tend to 0) and the line formula (5.28) from the closed
 forms at large L.
Outputs: output/existence.txt, output/mutual_cost.txt, output/weighing.txt, output/asymptotics.txt
"""
import numpy as np
from pathlib import Path
from scipy import linalg as sla, sparse as sp
from scipy.sparse import linalg as spla
from scipy.special import ive
from scipy.integrate import quad
from scipy.optimize import brentq

OUT = Path(__file__).parent / "output"
OUT.mkdir(parents=True, exist_ok=True)

KH, KA = 1.0, 0.7                      # kappa_h, kappa_a
MK = {0: 1.0, 1: 1.5}                  # M_k of the two levels used (m = 1, 2 pi/(N lambda_0) = 0.5)
GRIPS = {                              # (F0, F1, F2)
    "square":    (1.0, 0.6, 0.09),     # 4 F0 F2 = F1^2  (beta_hat = b_hat = 0.3)
    "nonsquare": (1.0, 0.6, 0.03),     # beta_hat / b_hat = 1/3
    "eight":     (1.0, 0.6, 0.045),    # 8 F0 F2 = F1^2  (beta_hat / b_hat = 1/2)
    "linear":    (1.0, 0.6, 0.0),
    "negF2":     (1.0, 0.6, -0.05),
}
HS = 0.01                              # step of the s-stencil
COMBOS_A = [((0, 1), (0, 1)), ((0, -1), (0, -1)), ((1, 1), (1, 1)), ((1, -1), (1, -1)), ((0, 1), (1, -1))]
COMBOS_B = [((0, 1), (1, -1)), ((1, -1), (0, 1))]   # each body: both levels, both branches
BOND_SETS = [("square", "square", COMBOS_A), ("nonsquare", "nonsquare", COMBOS_B), ("eight", "eight", COMBOS_B),
             ("linear", "linear", COMBOS_B), ("square", "nonsquare", COMBOS_B)]


def crit526(a1, a2, g1, g2, g12):
    """(5.26): A > 0 for two bodies with the anchor (determinant and trace of Gamma_2^{-1} + diag(alpha))."""
    return bool((1 + a1 * g1) * (1 + a2 * g2) > a1 * a2 * g12 ** 2 and g1 + g2 + (a1 + a2) * (g1 * g2 - g12 ** 2) > 0)


class Lattice:
    """Ring (D=1) or cubic torus (D=3) of side L; Laplacian and pseudo-inverse Green function."""

    def __init__(self, D, L):
        self.D, self.L, self.n = D, L, L ** D
        idx = np.arange(self.n).reshape((L,) * D)
        r = np.concatenate([idx.ravel()] * D)
        c = np.concatenate([np.roll(idx, -1, axis=ax).ravel() for ax in range(D)])
        adj = sp.coo_matrix((np.ones(len(r)), (r, c)), shape=(self.n, self.n))
        adj = (adj + adj.T).tocsr()
        self.lap = (sp.diags(np.asarray(adj.sum(axis=1)).ravel()) - adj).tocsr()
        k = 2 * np.pi * np.fft.fftfreq(L)
        grids = np.meshgrid(*([k] * D), indexing="ij")
        dh = sum(2 - 2 * np.cos(kk) for kk in grids)
        inv = np.zeros_like(dh)
        inv[dh > 1e-12] = 1 / dh[dh > 1e-12]
        self.g = np.real(np.fft.ifftn(inv)) / KH      # g(x) = (kappa_h Delta)^+ (x)

    def site(self, x):
        x = np.atleast_1d(x)
        return int(np.ravel_multi_index(tuple(int(c) % self.L for c in x), (self.L,) * self.D))

    def gx(self, x):
        x = np.atleast_1d(x)
        return self.g[tuple(int(c) % self.L for c in x)]

    def Ga(self, x, y, h):            # (5.8)
        x, y, h = (np.atleast_1d(v) for v in (x, y, h))
        return 1 / KA + self.gx(x - y) - self.gx(x - h) - self.gx(y - h) + self.gx(0 * x)

    def Ka_sparse(self, h):
        e = np.zeros(self.n)
        e[self.site(h)] = KA
        return (KH * self.lap + sp.diags(e)).tocsc()


def lam_min(A):
    return sla.eigh(A, eigvals_only=True, subset_by_index=[0, 0])[0]


# ---------------------------------------------------------------- infinite cubic lattice
def ginf3(x):
    """g_inf(x) of the infinite cubic lattice (kappa_h = 1): int_0^inf e^{-6t} prod_j I_{x_j}(2t) dt."""
    a, b, c = (abs(int(v)) for v in x)
    f = lambda t: ive(a, 2 * t) * ive(b, 2 * t) * ive(c, 2 * t)
    pts = [0, 1, 10, 100, 1e3, 1e4, 1e5, 1e6, 1e7]
    s = sum(quad(f, pts[i], pts[i + 1], limit=400, epsabs=1e-16, epsrel=1e-12)[0] for i in range(len(pts) - 1))
    # tail t > T from ive(n, 2t) = (4 pi t)^{-1/2} (1 - (4n^2-1)/(16 t) + O(t^-2))
    T, cc = pts[-1], sum((4 * n * n - 1) / 16 for n in (a, b, c))
    return (s + (4 * np.pi) ** -1.5 * (2 / np.sqrt(T) - cc * (2 / 3) * T ** -1.5)) / KH


def gstencil3(terms):
    """sum_j c_j g_inf(x_j) (kappa_h = 1) for sum_j c_j = 0, from one Bessel integral of the combined integrand
    (no cancellation between separately computed values); terms = [(c_j, x_j), ...]."""
    cs = [c for (c, _) in terms]
    xs = [tuple(abs(int(v)) for v in x) for (_, x) in terms]
    f = lambda t: sum(c * ive(a, 2 * t) * ive(b, 2 * t) * ive(e, 2 * t) for c, (a, b, e) in zip(cs, xs))
    pts = [0, 1, 10, 100, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8]
    s = sum(quad(f, pts[i], pts[i + 1], limit=800, epsabs=1e-24, epsrel=1e-11)[0] for i in range(len(pts) - 1))
    T = pts[-1]
    tail = -(4 * np.pi) ** -1.5 * (2 / 3) * T ** -1.5 * sum(c * sum((4 * n * n - 1) / 16 for n in x) for c, x in zip(cs, xs))
    return (s + tail) / KH


# ================================================================ (i) existence
def part_i(lines):
    P = lambda s: lines.append(s)
    P("(i) Existence of a lowest eigenvector: lambda_min(A) > 0 against the criteria of the derivation")
    P(f"kappa_h={KH}, kappa_a={KA}, levels M_k={MK}, grips (F0,F1,F2)={GRIPS}\n")
    for D, Ls in ((1, (32, 64)), (3, (8, 12))):
        for L in Ls:
            lat = Lattice(D, L)
            lapd = KH * lat.lap.toarray()
            n = lat.n
            P(f"--- {'ring' if D == 1 else 'cubic torus'} L={L}")
            # no anchor, one body: exists iff mu F2 > 0   (5.5)
            x0 = lat.site([3] * D)
            P(" no anchor, one body at a place: lambda_min(A0) and prediction [mu F2 > 0]")
            for gname in ("square", "negF2", "linear"):
                F0, F1, F2 = GRIPS[gname]
                for k in (0, 1):
                    for sg in (+1, -1):
                        mu = sg * MK[k]
                        A = lapd.copy(); A[x0, x0] += 2 * mu * F2
                        lm = lam_min(A)
                        P(f"   grip={gname:9s} k={k} sigma={sg:+d}: lambda_min={lm:+.3e}  "
                          f"exists={lm > 1e-10}  predicted={mu * F2 > 0}  b.1={mu * F1:+.2f}")
            # no anchor, two bodies with mixed signs: threshold alpha2* = -alpha1/(1+alpha1 r12)   (5.6)
            x1, x2 = lat.site([0] * D), lat.site([4] + [0] * (D - 1))
            r12 = 2 * (lat.gx([0] * D) - lat.gx([4] + [0] * (D - 1)))
            a1 = 2 * MK[1] * GRIPS["square"][2]
            def lm2(a2):
                A = lapd.copy(); A[x1, x1] += a1; A[x2, x2] += a2
                return lam_min(A)
            a2num = brentq(lm2, -a1 + 1e-9, -1e-9, xtol=1e-14)
            a2pred = -a1 / (1 + a1 * r12)
            P(f" no anchor, two bodies (separation 4): alpha1={a1:.4f}, r12={r12:.6f}: threshold alpha2 "
              f"numerical={a2num:.10f} predicted={a2pred:.10f}  rel.dev={abs(a2num / a2pred - 1):.1e}")
            # anchor: one body, threshold mu F2 = -1/(2 Gamma(x))   (5.10)
            h = [0] * D
            Ka = lapd.copy(); Ka[lat.site(h), lat.site(h)] += KA
            P(" anchor at h, one body at distance d: threshold alpha* (lambda_min=0) vs -1/Gamma(x), "
              "and which (k, sigma) of grip negF2 / square have a lowest eigenvector")
            for d in ((2, 5, 10) if D == 1 else (1, 2, 3)):
                xx = [d] + [0] * (D - 1); i = lat.site(xx)
                Gam = lat.Ga(xx, xx, h)
                def lm1(al):
                    A = Ka.copy(); A[i, i] += al
                    return lam_min(A)
                anum = brentq(lm1, -2 / Gam, -0.2 / Gam, xtol=1e-14)
                ex = []
                for gname in ("negF2", "square"):
                    for k in (0, 1):
                        for sg in (+1, -1):
                            al = 2 * sg * MK[k] * GRIPS[gname][2]
                            ok_num = lm1(al) > 0
                            ok_pred = 1 + al * Gam > 0
                            ex.append(f"{gname}:k{k}{'+' if sg > 0 else '-'}={'Y' if ok_num else 'N'}"
                                      f"{'' if ok_num == ok_pred else '(MISMATCH)'}")
                P(f"   d={d}: Gamma={Gam:.6f}  alpha* numerical={anum:.10f} predicted={-1 / Gam:.10f}  "
                  f"| {' '.join(ex)}")
            # anchor, two bodies: A > 0 iff Gamma_2^{-1} + diag(alpha) > 0   (5.10), random samples
            rng = np.random.default_rng(1)
            y1, y2 = [1] + [0] * (D - 1), [3] + [1] * (D - 1)
            i1, i2 = lat.site(y1), lat.site(y2)
            G2 = np.array([[lat.Ga(y1, y1, h), lat.Ga(y1, y2, h)], [lat.Ga(y2, y1, h), lat.Ga(y2, y2, h)]])
            g11, g22, g12 = G2[0, 0], G2[1, 1], G2[0, 1]
            agree, agree26, tot = 0, 0, 0
            for _ in range(40):
                al = rng.uniform(-2.0, 2.0, size=2) / np.diag(G2)
                A = Ka.copy(); A[i1, i1] += al[0]; A[i2, i2] += al[1]
                num = lam_min(A) > 0
                pred = np.linalg.eigvalsh(np.linalg.inv(G2) + np.diag(al))[0] > 0
                agree += int(num == pred); agree26 += int(num == crit526(al[0], al[1], g11, g22, g12)); tot += 1
            P(f" anchor, two bodies, random (alpha1, alpha2): criterion (5.10) agrees with lambda_min in {agree}/{tot}, "
              f"explicit form (5.26) in {agree26}/{tot}")
            # a pair whose bodies each meet the one-body condition (5.10) but which violates (5.26)
            lmax = np.linalg.eigvalsh(G2)[-1]
            a = 0.5 * (1 / lmax + 1 / max(g11, g22))
            A = Ka.copy(); A[i1, i1] -= a; A[i2, i2] -= a
            lm_single = []
            for ii in (i1, i2):
                A1 = Ka.copy(); A1[ii, ii] -= a
                lm_single.append(lam_min(A1))
            P(f" anchor, two bodies at {y1}, {y2} (Gamma = {g11:.6f}, {g22:.6f}, G12 = {g12:.6f}) with alpha1 = alpha2 = -a, "
              f"a = {a:.6f} between 1/lambda_max(Gamma_2) = {1 / lmax:.6f} and 1/max Gamma = {1 / max(g11, g22):.6f}:")
            P(f"   one body alone: 1 - a Gamma(x_i) = {1 - a * g11:+.4f}, {1 - a * g22:+.4f}; lambda_min = "
              f"{lm_single[0]:+.3e}, {lm_single[1]:+.3e} (exists)")
            P(f"   pair: lambda_min(A) = {lam_min(A):+.3e}; (5.26) predicts existence = {crit526(-a, -a, g11, g22, g12)}; "
              f"sufficient condition a (max Gamma + G12) < 1: {a * (max(g11, g22) + g12) < 1}\n")


# ================================================================ (ii) mutual cost
def part_ii(lines):
    P = lambda s: lines.append(s)
    P("(ii) Mutual cost of two held sources E12 = -g1 g2 (A^{-1})_{x1 x2} from the exact E0 "
      "(sparse LU of A) against (5.14) E12 = -g1 g2 G_a(x1,x2); g1 = g2 = 1")
    P(f"kappa_h={KH}, kappa_a={KA}\n")
    # ring
    for L in (64, 256):
        lat = Lattice(1, L); h = [0]
        lu = spla.splu(lat.Ka_sparse(h))
        P(f"--- ring L={L}: pair on one side of the anchor, x1 = h + d1, x2 = x1 + s")
        for d1 in (4, 16):
            e = np.zeros(lat.n); e[lat.site([d1])] = 1.0
            col = lu.solve(e)
            row = []
            for s in (1, 2, 4, 8, 16):
                ex = -col[lat.site([d1 + s])]
                fo = -lat.Ga([d1], [d1 + s], h)
                row.append(f"s={s}: {ex:.10f} (formula {fo:.10f})")
            P(f"  d1={d1}: " + "; ".join(row))
            P(f"         L->inf value (5.16) on the line: -(1/kappa_a + d1/kappa_h) = {-(1 / KA + d1 / KH):.10f}")
        e = np.zeros(lat.n); e[lat.site([5])] = 1.0
        col = lu.solve(e)
        P(f"  opposite sides x1=h+5, x2=h-7: exact {-col[lat.site([-7])]:.10f}, formula "
          f"{-lat.Ga([5], [-7], h):.10f}, -1/kappa_a = {-1 / KA:.10f}")
    # cubic torus
    g0inf = ginf3([0, 0, 0])
    gcache = {}
    def gi(x):
        key = tuple(sorted(abs(int(v)) for v in x))
        if key not in gcache:
            gcache[key] = ginf3(key)
        return gcache[key]
    for L in (16, 32):
        rs = (2, 4, 6, 8) if L == 16 else (2, 4, 6, 8, 12, 16)
        lat = Lattice(3, L); h = np.array([0, 0, 0])
        lu = spla.splu(lat.Ka_sparse(h))
        P(f"--- cubic torus L={L}: pair along x with midpoint h + D e_y, x1,2 = h + D e_y -/+ (r/2) e_x")
        for Dm in (0, 6):
            res = []
            for r in rs:
                y1 = h + np.array([-r // 2, Dm, 0]); y2 = h + np.array([r // 2, Dm, 0])
                e = np.zeros(lat.n); e[lat.site(y1)] = 1.0
                ex = -lu.solve(e)[lat.site(y2)]
                fo = -lat.Ga(y1, y2, h)
                linf = -(1 / KA + gi(y1 - y2) - gi(y1 - h) - gi(y2 - h) + g0inf)
                cont = -(1 / KA + g0inf) - (1 / (4 * np.pi * KH)) * (1 / r - 2 / np.hypot(Dm, r / 2))
                res.append((r, ex, fo, linf, cont))
            P(f"  D={Dm}:  r | exact E12 | formula (5.14), this L | L=inf lattice, (5.14) with g_inf | continuum image form (5.15)")
            for (r, ex, fo, linf, cont) in res:
                P(f"     {r:2d} | {ex:.10f} | {fo:.10f} | {linf:.10f} | {cont:.10f}")
            P("        effective coefficient c(r) = [E12(r)-E12(r')] / [-(1/(4 pi kappa_h))(1/r - 1/r')], consecutive r:")
            for j in range(1, len(res)):
                (r0, e0, _, l0, _), (r1, e1, _, l1, _) = res[j - 1], res[j]
                den = -(1 / (4 * np.pi * KH)) * (1 / r1 - 1 / r0)
                pc = (1 / r1 - 2 / np.hypot(Dm, r1 / 2) - 1 / r0 + 2 / np.hypot(Dm, r0 / 2)) / (1 / r1 - 1 / r0)
                P(f"        r={r0}->{r1}: exact {(e1 - e0) / den:+.4f}, L=inf lattice {(l1 - l0) / den:+.4f}, "
                  f"continuum image form {pc:+.4f}")
        # one source at the anchor
        vals = []
        e = np.zeros(lat.n); e[lat.site(h)] = 1.0
        col = lu.solve(e)
        for y in ([3, 0, 0], [5, 2, 1], [L // 2, L // 2, L // 2]):
            vals.append(-col[lat.site(y)])
        P(f"  source 1 at the anchor, source 2 at three places: E12 = {', '.join(f'{v:.12f}' for v in vals)}; "
          f"-1/kappa_a = {-1 / KA:.12f}")
    P("")


# ================================================================ (iii) weighing
def stencil(f):
    """f: dict s -> value with f(0)=0. Returns (first derivative, half second derivative) at s=0."""
    h = HS
    d1 = (8 * (f[h] - f[-h]) - (f[2 * h] - f[-2 * h])) / (12 * h)
    d2 = (16 * (f[h] + f[-h]) - (f[2 * h] + f[-2 * h])) / (24 * h * h)
    return d1, d2


def part_iii(lines):
    P = lambda s: lines.append(s)
    P("(iii) Cost, weight, bond and weighing ratios at order s^2 from the exact E0 (dense; s-stencil "
      f"step {HS}) against (5.18)-(5.22); g_s = +-1 (the g_s-linear part is exact)")
    P(f"kappa_h={KH}, kappa_a={KA}, levels M_k={MK}\n")
    S = (-2 * HS, -HS, HS, 2 * HS)
    combos1 = [(k, sg) for k in (0, 1) for sg in (+1, -1)]
    for D, Ls, ds, Rp in ((1, (32, 64), (2, 5, 10), 3), (3, (8, 12), (1, 2, 3), 1)):
        for L in Ls:
            lat = Lattice(D, L); n = lat.n
            h = np.zeros(D, dtype=int)
            Ka = KH * lat.lap.toarray(); Ka[lat.site(h), lat.site(h)] += KA
            lam, U = np.linalg.eigh(Ka); om = np.sqrt(lam)
            Mab = 1 / (om[:, None] * om[None, :] * (om[:, None] + om[None, :]))
            w = lambda i: 0.5 * np.sum(U[i] ** 2 / om)
            Sig = lambda i, j: (U[i] * U[j]) @ Mab @ (U[i] * U[j])
            Tc, Ec = {}, {}

            def E(bodies, s, xs):
                """Exact E0 = c0 + 1/2 Tr sqrt(A) - 1/2 b.A^-1.b with source +1, -1, 0 at site xs."""
                key = (tuple(bodies), s, xs)
                if key not in Ec:
                    A = Ka.copy(); b = np.zeros(n); c0 = 0.0
                    for (i, mu, g) in bodies:
                        F0, F1, F2 = GRIPS[g]
                        A[i, i] += 2 * s * mu * F2; b[i] += s * mu * F1; c0 += s * mu * F0
                    tkey = tuple(sorted((i, 2 * s * mu * GRIPS[g][2]) for (i, mu, g) in bodies if GRIPS[g][2] != 0))
                    if tkey not in Tc:
                        lam_ = sla.eigvalsh(A)
                        assert lam_[0] > 0
                        Tc[tkey] = 0.5 * np.sqrt(lam_).sum()
                    cf = sla.cho_factor(A)
                    es = np.zeros(n); es[xs] = 1.0
                    Ec[key] = [c0 + Tc[tkey] - 0.5 * bb @ sla.cho_solve(cf, bb) for bb in (b + es, b - es, b)]
                return Ec[key]

            def single(i, mu, g, xs):
                """C1, Cmark, W1, Wmark of one body at site i (source at xs, g_s = 1)."""
                C = {s: E([(i, mu, g)], s, xs)[2] - E([], 0.0, xs)[2] for s in S}
                W = {s: 0.5 * ((E([(i, mu, g)], s, xs)[0] - E([], 0.0, xs)[0])
                               - (E([(i, mu, g)], s, xs)[1] - E([], 0.0, xs)[1])) for s in S}
                return stencil(C) + stencil(W)

            P(f"=== {'ring' if D == 1 else 'cubic torus'} L={L}, anchor h=0; body placements x=h+d e, x'=h+(d+1) e, "
              f"source at h+(d+1+{Rp}) e")
            maxdev, maxdev20, maxdev19, maxdev21 = 0.0, 0.0, 0.0, 0.0
            for d in ds:
                ex = np.array([1] + [0] * (D - 1))
                X, Xp, Xs = h + d * ex, h + (d + 1) * ex, h + (d + 1 + Rp) * ex
                i, ip, isrc = lat.site(X), lat.site(Xp), lat.site(Xs)
                Gm = {i: lat.Ga(X, X, h), ip: lat.Ga(Xp, Xp, h)}
                ph = {i: -lat.Ga(X, Xs, h), ip: -lat.Ga(Xp, Xs, h)}
                Gb = 0.5 * (Gm[i] + Gm[ip]); pb = 0.5 * (ph[i] + ph[ip])
                amark = pb * (Gm[i] - Gm[ip]) / (Gb * (ph[i] - ph[ip]))
                P(f" d={d}: Gamma(x)={Gm[i]:.6f}, w(x)={w(i):.6f}, Sigma(x)={Sig(i, i):.6f}, phi_a(x)={ph[i]:.6f}; "
                  f"a_mark={amark:+.6f}")
                for g in ("square", "nonsquare", "eight", "linear"):
                    F0, F1, F2 = GRIPS[g]
                    for (k, sg) in combos1:
                        mu = sg * MK[k]
                        r = {j: single(j, mu, g, isrc) for j in (i, ip)}
                        # closed forms (5.18)
                        for j in (i, ip):
                            pred = (mu * (F0 + F2 * w(j)), -0.5 * mu ** 2 * (F1 ** 2 * Gm[j] + F2 ** 2 * Sig(j, j)),
                                    mu * F1 * ph[j], -2 * mu ** 2 * F1 * F2 * Gm[j] * ph[j])
                            for a, bb in zip(r[j], pred):
                                maxdev = max(maxdev, abs(a - bb) / max(abs(bb), 1e-12) if abs(bb) > 1e-12 else abs(a))
                        exist = "Y" if all(1 + 2 * mu * F2 * Gm[j] > 0 for j in (i, ip)) else "N"
                        if F2 == 0:
                            rho_num = (r[i][3] - r[ip][3]) / (r[i][2] - r[ip][2]) * \
                                (0.5 * (r[i][0] + r[ip][0])) / (0.5 * (r[i][1] + r[ip][1]))
                            maxdev20 = max(maxdev20, abs(rho_num))
                            P(f"    grip={g:9s} k={k} sigma={sg:+d}: rho_mark numerical={rho_num:+.3e} predicted=0  "
                              f"[block at s=1 by (5.10): {exist}]")
                            continue
                        rho_num = (r[i][3] - r[ip][3]) / (r[i][2] - r[ip][2]) * \
                            (0.5 * (r[i][0] + r[ip][0])) / (0.5 * (r[i][1] + r[ip][1]))
                        wb = 0.5 * (w(i) + w(ip)); Sb = 0.5 * (Sig(i, i) + Sig(ip, ip))
                        rho_pred = 4 * F2 * (F0 + F2 * wb) / (F1 ** 2 * Gb + F2 ** 2 * Sb) * \
                            (Gm[i] * ph[i] - Gm[ip] * ph[ip]) / (ph[i] - ph[ip])
                        maxdev20 = max(maxdev20, abs(rho_num / rho_pred - 1))
                        lead = 4 * F0 * F2 / F1 ** 2 * (1 + amark)
                        P(f"    grip={g:9s} k={k} sigma={sg:+d}: rho_mark numerical={rho_num:.8f} "
                          f"predicted (5.20)={rho_pred:.8f} leading (4F0F2/F1^2)(1+a_mark)={lead:.6f}  "
                          f"[block at s=1 by (5.10): {exist}]")
                # bond: pair x1 = X, x2 = X + 2 e2 (ring: X + 2 e), translated by e
                e2 = np.array([0, 1, 0]) if D == 3 else ex
                Y1, Y2 = X, X + 2 * e2
                Y1p, Y2p = Y1 + ex, Y2 + ex
                Ym, Ymp = X + e2, X + e2 + ex
                Ys = Y2p + 2 * ex if D == 1 else Ymp + Rp * ex
                js = [lat.site(v) for v in (Y1, Y2, Y1p, Y2p, Ym, Ymp)]
                jsrc = lat.site(Ys)
                phi = lambda v: -lat.Ga(v, Ys, h)
                G12, G12p = lat.Ga(Y1, Y2, h), lat.Ga(Y1p, Y2p, h)
                Gam1, Gam2, Gam1p, Gam2p = (lat.Ga(v, v, h) for v in (Y1, Y2, Y1p, Y2p))
                dphi1, dphi2 = phi(Y1) - phi(Y1p), phi(Y2) - phi(Y2p)
                dphim = phi(Ym) - phi(Ymp)
                mr = (dphi1 + dphi2) / (2 * dphim)
                Gbar, dG = 0.5 * (G12 + G12p), G12 - G12p
                pb1, pb2 = 0.5 * (phi(Y1) + phi(Y1p)), 0.5 * (phi(Y2) + phi(Y2p))
                abond = (pb1 + pb2) * dG / (2 * Gbar * dphim)
                S12b = 0.5 * (Sig(js[0], js[1]) + Sig(js[2], js[3]))
                wmb = 0.5 * (w(js[4]) + w(js[5]))
                P(f"  bond, pair separation 2, source at {[int(c) for c in Ys]}: m_r={mr:.6f}, a_bond={abond:+.6f}")
                for (g1, g2, combos) in BOND_SETS:
                    (F01, F11, F21), (F02, F12, F22) = GRIPS[g1], GRIPS[g2]
                    be1, be2 = 2 * F21 / F11, 2 * F22 / F12
                    Psi = lambda y1, y2: be1 * phi(y1) + be2 * phi(y2)
                    dPsi, Psib = Psi(Y1, Y2) - Psi(Y1p, Y2p), 0.5 * (Psi(Y1, Y2) + Psi(Y1p, Y2p))
                    P(f"   grips (body 1, body 2) = ({g1}, {g2}):")
                    for (c1, c2) in combos:
                        mu1, mu2 = c1[1] * MK[c1[0]], c2[1] * MK[c2[0]]
                        al1, al2 = 2 * mu1 * F21, 2 * mu2 * F22
                        # existence of the pair block at s = 1, both placements: lambda_min(A) against (5.26)
                        ex_num, ex_pred = [], []
                        for (a_, b_, ga, gb, gab) in ((js[0], js[1], Gam1, Gam2, G12), (js[2], js[3], Gam1p, Gam2p, G12p)):
                            A = Ka.copy(); A[a_, a_] += al1; A[b_, b_] += al2
                            ex_num.append("Y" if lam_min(A) > 0 else "N")
                            ex_pred.append("Y" if crit526(al1, al2, ga, gb, gab) else "N")

                        def bond(a_, b_):
                            B = {}; Wb = {}
                            for s in S:
                                e12 = E([(a_, mu1, g1), (b_, mu2, g2)], s, jsrc)
                                e1 = E([(a_, mu1, g1)], s, jsrc); e2_ = E([(b_, mu2, g2)], s, jsrc)
                                e0 = E([], 0.0, jsrc)
                                bb = [e12[t] - e1[t] - e2_[t] + e0[t] for t in range(3)]
                                B[s] = bb[2]; Wb[s] = 0.5 * (bb[0] - bb[1])
                            return stencil(B)[1], stencil(Wb)[1]
                        B2, W2 = bond(js[0], js[1]); B2p, W2p = bond(js[2], js[3])
                        # (5.19) for different grips
                        B19 = lambda y1, y2, j1, j2: -mu1 * mu2 * (F11 * F12 * lat.Ga(y1, y2, h) + F21 * F22 * Sig(j1, j2))
                        W19 = lambda y1, y2: -2 * mu1 * mu2 * lat.Ga(y1, y2, h) * (F11 * F22 * phi(y2) + F21 * F12 * phi(y1))
                        for num, pred in ((B2, B19(Y1, Y2, js[0], js[1])), (B2p, B19(Y1p, Y2p, js[2], js[3])),
                                          (W2, W19(Y1, Y2)), (W2p, W19(Y1p, Y2p))):
                            maxdev19 = max(maxdev19, abs(num - pred) / abs(pred) if abs(pred) > 1e-12 else abs(num))
                        out = []
                        for ii, mui, gi in ((1, mu1, g1), (2, mu2, g2)):
                            F0i, F1i, F2i = GRIPS[gi]
                            bhi, bei = F1i / (2 * F0i), 2 * F2i / F1i
                            rm = single(js[4], mui, gi, jsrc); rmp = single(js[5], mui, gi, jsrc)
                            rho_num = ((W2 - W2p) / (0.5 * (B2 + B2p))) / ((rm[2] - rmp[2]) / (0.5 * (rm[0] + rmp[0])))
                            rho_pred = (Gbar * dPsi + Psib * dG) / (Gbar + 0.25 * be1 * be2 * S12b) * \
                                (1 + bei * bhi * wmb) / (2 * bhi * dphim)                                  # (5.21)
                            lead = (be1 * dphi1 + be2 * dphi2) / (2 * bhi * dphim) + \
                                (be1 * pb1 + be2 * pb2) * dG / (2 * bhi * Gbar * dphim)                    # (5.22)
                            maxdev21 = max(maxdev21, abs(rho_num / rho_pred - 1) if abs(rho_pred) > 1e-12 else abs(rho_num))
                            out.append(f"rho_bond,{ii} num={rho_num:+.8f} (5.21)={rho_pred:+.8f} lead(5.22)={lead:+.6f}")
                        P(f"    (k,sigma)=({c1[0]},{c1[1]:+d}),({c2[0]},{c2[1]:+d}): pair block at s=1 (both placements) "
                          f"lambda_min>0: {'/'.join(ex_num)}, (5.26): {'/'.join(ex_pred)}; B={B2:+.6e}; " + "; ".join(out))
            P(f" max relative deviation over this lattice: C1, Cmark, W1, Wmark from (5.18): {maxdev:.2e}; "
              f"rho_mark from (5.20): {maxdev20:.2e}; B, W_bond from (5.19): {maxdev19:.2e}; "
              f"rho_bond,i from (5.21): {maxdev21:.2e} (absolute deviation where the prediction is 0)\n")


# ================================================================ asymptotics from closed forms
def part_asym(lines):
    P = lambda s: lines.append(s)
    P("Asymptotic statements from the closed forms (no eigenvalue computation)")
    g0 = ginf3([0, 0, 0])
    P(f"gamma_3 = kappa_h g_inf(0) = {g0 * KH:.10f}")
    for x in ([4, 0, 0], [8, 0, 0], [16, 0, 0], [6, 6, 6]):
        r = np.linalg.norm(x)
        P(f"  g_inf({x}) * 4 pi kappa_h |x| = {ginf3(x) * 4 * np.pi * KH * r:.6f}")
    P("\n(5.15) orders of the limits on the infinite cubic lattice (L -> inf first), anchor at 0, g1 = g2 = 1;"
      " c(r) as in mutual_cost.txt")
    E12 = lambda y1, y2: -(1 / KA + g0 + ginf3(np.subtract(y1, y2)) - ginf3(y1) - ginf3(y2))
    for lab, Dm, rr in (("(a) midpoint (0,40,0), r << D", 40, (4, 8, 16)), ("(c) midpoint at the anchor", 0, (8, 16, 32, 64))):
        vals = [E12([-r // 2, Dm, 0], [r // 2, Dm, 0]) for r in rr]
        cs = [(vals[j] - vals[j - 1]) / (-(1 / (4 * np.pi * KH)) * (1 / rr[j] - 1 / rr[j - 1])) for j in range(1, len(rr))]
        P(f"  {lab}: " + ", ".join(f"c({rr[j - 1]}->{rr[j]})={cs[j - 1]:+.4f}" for j in range(1, len(rr))))
    lim = -(1 / KA + g0 - ginf3([3, 0, 0]))
    P("  (b) x1=(3,0,0) fixed, x2=(3+r,0,0): 4 pi kappa_h r^2 [E12 - E12(r=inf)] -> -(x1-h).r_hat = -3: " +
      ", ".join(f"r={r}: {4 * np.pi * KH * r * r * (E12([3, 0, 0], [3 + r, 0, 0]) - lim):+.4f}" for r in (8, 16, 32, 64)))
    cphi = 1 / KA + g0
    Ginf = 1 / KA + 2 * g0
    P(f"\n(5.23) a_mark on the infinite cubic lattice (L -> inf first), collinear: anchor 0, body d, d+1, "
      f"source d+1+R'; prediction a_mark ~ (2 c_phi/Gamma_inf) (R/d)^2 with c_phi=1/kappa_a+gamma_3/kappa_h="
      f"{cphi:.6f}, Gamma_inf={Ginf:.6f}, R=R'+1/2, d->d+1/2")
    for Rp in (3, 6):
        for d in (8, 16, 32, 64):
            Gm = lambda x: 1 / KA + 2 * (g0 - ginf3([x, 0, 0]))
            ph = lambda x: -(1 / KA + g0 + ginf3([x - (d + 1 + Rp), 0, 0]) - ginf3([x, 0, 0]) - ginf3([d + 1 + Rp, 0, 0]))
            a = 0.5 * (ph(d) + ph(d + 1)) * (Gm(d) - Gm(d + 1)) / (0.5 * (Gm(d) + Gm(d + 1)) * (ph(d) - ph(d + 1)))
            pred = 2 * cphi / Ginf * ((Rp + 0.5) / (d + 0.5)) ** 2
            P(f"  R'={Rp} d={d:3d}: a_mark={a:+.6e}  prediction={pred:+.6e}  ratio={a / pred:.4f}")
    P("\n(5.24) a_bond on the infinite cubic lattice: pair (d,0,0),(d,2,0) -> translated by e_x, source (d+1+R',1,0)")
    for Rp in (3, 6):
        for d in (8, 16, 32, 64):
            xs = np.array([d + 1 + Rp, 1, 0])
            phi = lambda v: -(1 / KA + g0 + ginf3(np.array(v) - xs) - ginf3(v) - ginf3(xs))
            G12 = lambda v1, v2: 1 / KA + g0 + ginf3(np.array(v1) - np.array(v2)) - ginf3(v1) - ginf3(v2)
            Y1, Y2, Y1p, Y2p = [d, 0, 0], [d, 2, 0], [d + 1, 0, 0], [d + 1, 2, 0]
            Gb = 0.5 * (G12(Y1, Y2) + G12(Y1p, Y2p))
            dphim = phi([d, 1, 0]) - phi([d + 1, 1, 0])
            a = 0.5 * (phi(Y1) + phi(Y1p) + phi(Y2) + phi(Y2p)) * (G12(Y1, Y2) - G12(Y1p, Y2p)) / (2 * Gb * dphim)
            R = Rp + 0.5; dd = np.hypot(d + 0.5, 1.0)
            pred = 2 * cphi / (cphi + ginf3([0, 2, 0])) * (R / dd) ** 2 * ((d + 0.5) / dd)
            P(f"  R'={Rp} d={d:3d}: a_bond={a:+.6e}  prediction={pred:+.6e}  ratio={a / pred:.4f}")
    P("\n(5.27) mirror placement on the infinite cubic lattice (control): anchor 0, body at (d,0,0) and (d+2,0,0), "
      "source at (d+1,R,0); Delta g_s = 0 by reflection, so a_mark = -2 phi_bar/(g_s Gamma_bar) -> "
      "2 [c_phi + g_inf((1,R,0))]/Gamma_inf as d -> inf")
    for R in (3, 6):
        lim = 2 * (cphi + ginf3([1, R, 0])) / Ginf
        for d in (8, 16, 32, 64):
            xs = np.array([d + 1, R, 0])
            Gm = lambda v: 1 / KA + 2 * (g0 - ginf3(v))
            ph = lambda v: -(1 / KA + g0 + ginf3(np.array(v) - xs) - ginf3(v) - ginf3(xs))
            x, xp = [d, 0, 0], [d + 2, 0, 0]
            dgs = ginf3(np.array(x) - xs) - ginf3(np.array(xp) - xs)
            dph = ph(x) - ph(xp)
            a = 0.5 * (ph(x) + ph(xp)) * (Gm(x) - Gm(xp)) / (0.5 * (Gm(x) + Gm(xp)) * dph)
            P(f"  R={R} d={d:3d}: Delta g_s={dgs:+.1e}, Delta phi_a={dph:+.3e}, a_mark={a:+.6f}, limit={lim:.6f}")
    glim = ginf3([1, 0, 0])
    P("\n(5.27) pair control on the infinite cubic lattice: anchor 0, source e_x, pair x_1,2=(d,+-t,0) translated by e_x, "
      "d=n^3, t=n^4; N=Dg_h(x1)+Dg_h(x2), D=Dg_s(xbar), H=Dg_h(xbar) at the midpoint xbar=(d,0,0) (differences by "
      "combined Bessel integrals); a_bond = (phibar1+phibar2) DeltaG12 / (2 Gbar12 Delta phibar) with DeltaG12=-N, "
      f"Delta phibar=-g_s(D-H), g_s=1; predicted: N/D->0, H/D->1, N/(D-H)->1, m_r->0, a_bond -> -(c_phi-g_inf(e_x))/c_phi "
      f"= {-(cphi - glim) / cphi:.6f}")
    for nn in (2, 3, 4, 5, 6):
        d, t = nn ** 3, nn ** 4
        N = 2 * gstencil3([(1, [d, t, 0]), (-1, [d + 1, t, 0])])
        Dd = gstencil3([(1, [d - 1, 0, 0]), (-1, [d, 0, 0])])
        H = gstencil3([(1, [d, 0, 0]), (-1, [d + 1, 0, 0])])
        DmH = gstencil3([(1, [d - 1, 0, 0]), (-2, [d, 0, 0]), (1, [d + 1, 0, 0])])
        dphj = gstencil3([(1, [d - 1, t, 0]), (-2, [d, t, 0]), (1, [d + 1, t, 0])])  # = -Delta phi_j / g_s
        phi = lambda v: -(cphi + ginf3(np.subtract(v, [1, 0, 0])) - ginf3(v) - glim)
        G12 = lambda v1, v2: cphi + ginf3(np.subtract(v1, v2)) - ginf3(v1) - ginf3(v2)
        X1, X2, X1p, X2p = [d, t, 0], [d, -t, 0], [d + 1, t, 0], [d + 1, -t, 0]
        pbsum = 0.5 * (phi(X1) + phi(X1p) + phi(X2) + phi(X2p))
        Gb = 0.5 * (G12(X1, X2) + G12(X1p, X2p))
        ab = pbsum * (-N) / (2 * Gb * (-DmH))
        mr = (2 * dphj) / (2 * DmH)
        P(f"  n={nn} d={d:4d} t={t:5d}: N/D={N / Dd:.4e}  H/D={H / Dd:.6f}  N/(D-H)={N / DmH:.6f}  "
          f"(D-H)/(D-H directly)={(Dd - H) / DmH:.6f}  m_r={mr:+.4e}  a_bond={ab:+.6f}")
    P("\n(5.25) ring: a_mark for a body between anchor and source (d=10, d+1, source at d+1+3) -> 1 as L -> inf")
    for L in (32, 64, 256, 1024, 4096):
        Gm = lambda x: 1 / KA + x * (L - x) / (KH * L)
        xs = 14
        ph = lambda x: -(1 / KA + (x * (L - x) + xs * (L - xs) - abs(xs - x) * (L - abs(xs - x))) / (2 * KH * L))
        a = 0.5 * (ph(10) + ph(11)) * (Gm(10) - Gm(11)) / (0.5 * (Gm(10) + Gm(11)) * (ph(10) - ph(11)))
        P(f"  L={L:5d}: a_mark={a:.6f}")
    L, xs, Kr = 4096, 20, KH / KA
    P(f"\n(5.28) line, every comparison: a_mark from the ring closed forms (5.8), (5.11) at L={L} against (5.28); "
      f"anchor 0, source at {xs}")
    rr = lambda a_, b_: (abs(a_ - b_) % L) * (L - abs(a_ - b_) % L) / (KH * L)
    Gr = lambda x: 1 / KA + rr(x, 0)
    phr = lambda x: -(1 / KA + 0.5 * (rr(x, 0) + rr(xs, 0) - rr(x, xs)))
    def line528(x, xp):
        dm = lambda v: (abs(v), min(abs(v), xs) if v > 0 else 0)
        (d1, m1), (d2, m2) = dm(x), dm(xp)
        return (Kr + 0.5 * (m1 + m2)) * (d1 - d2) / ((Kr + 0.5 * (d1 + d2)) * (m1 - m2))
    for (x, xp, lab) in ((12, 11, "between anchor and source"), (21, 19, "straddling the source"),
                         (25, 15, "straddling the source"), (5, -7, "across the anchor"), (8, -3, "across the anchor")):
        a = 0.5 * (phr(x) + phr(xp)) * (Gr(x) - Gr(xp)) / (0.5 * (Gr(x) + Gr(xp)) * (phr(x) - phr(xp)))
        P(f"  x={x:3d}, x'={xp:3d} ({lab}): a_mark ring={a:+.6f}  (5.28)={line528(x, xp):+.6f}")
    P("\n(5.13) anchored line (L = inf): w(d) and Sigma(d) from the resolvent (5.9); predictions "
      "w(10d)-w(d) -> ln10/(2 pi sqrt(kappa_h)), Sigma(d)/d -> 2 ln2/(pi kappa_h^{3/2})")
    def Rdd(nu, d):
        t = nu * nu / (2 * KH)
        sq = np.sqrt(t * t + 2 * t)
        g0n = 1 / (KH * 2 * sq)                         # 1/(kappa_h (1/z - z)), 1/z = 1 + t + sq
        one_m = -np.expm1(-2 * d * np.log1p(t + sq))    # 1 - z^{2d}
        return (g0n + KA * g0n * g0n * one_m) / (1 + KA * g0n)
    def wS(d):
        f1 = lambda u: np.exp(u) * Rdd(np.exp(u), d)
        f2 = lambda u: np.exp(u) * Rdd(np.exp(u), d) ** 2
        lo, hi = -40.0, 25.0
        w_ = quad(f1, lo, hi, limit=800, epsabs=1e-13)[0] / np.pi
        S_ = 2 * quad(f2, lo, hi, limit=800, epsabs=1e-13)[0] / np.pi
        return w_, S_
    prev = None
    for d in (10, 100, 1000, 10000):
        w_, S_ = wS(d)
        inc = "" if prev is None else f"  w(d)-w(d/10)={w_ - prev:.6f}"
        P(f"  d={d:6d}: w={w_:.6f}  Sigma/d={S_ / d:.6f}  Gamma={1 / KA + d / KH:.3f}{inc}")
        prev = w_
    P(f"  predictions: ln10/(2 pi)={np.log(10) / (2 * np.pi):.6f}, 2 ln2/pi={2 * np.log(2) / np.pi:.6f}")


if __name__ == "__main__":
    for name, fn in (("existence.txt", part_i), ("mutual_cost.txt", part_ii),
                     ("weighing.txt", part_iii), ("asymptotics.txt", part_asym)):
        lines = []
        fn(lines)
        (OUT / name).write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("wrote", OUT / name, flush=True)
