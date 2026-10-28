"""Check for 08-ilang-propagation/05-anchor, derivation v1.

Field of oscillator cells without pinning, anchor (kappa_a/2) q_h^2, held bodies with grips
F(q) = F0 + F1 q + F2 q^2, held sources g q_xs.  In a sector of the held bodies the uncompressed
contract is C_f = 1/2 p.p + 1/2 q.A q + b.q + c0, and for A > 0 its exact lowest eigenvalue is
E0 = c0 + 1/2 Tr sqrt(A) - 1/2 b.A^{-1}.b  (computed here by dense or sparse linear algebra).
The script compares this with the closed forms of the derivation:
 (i)   existence conditions (5.4)-(5.6), (5.10);
 (ii)  mutual cost of two sources (5.14)-(5.16) against the separation, two distances from the anchor;
 (iii) cost, weight, bond and the ratios rho_mark, rho_bond,i (5.18)-(5.22), two levels,
       both branches, three distances from the anchor;
 plus the asymptotic statements (5.13), (5.15), (5.23)-(5.25) from the closed forms at large L.
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
            agree, tot = 0, 0
            for _ in range(40):
                al = rng.uniform(-2.0, 2.0, size=2) / np.diag(G2)
                A = Ka.copy(); A[i1, i1] += al[0]; A[i2, i2] += al[1]
                num = lam_min(A) > 0
                pred = np.linalg.eigvalsh(np.linalg.inv(G2) + np.diag(al))[0] > 0
                agree += int(num == pred); tot += 1
            P(f" anchor, two bodies, random (alpha1, alpha2): criterion (5.10) agrees with lambda_min in {agree}/{tot}\n")


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
    combos2 = [((0, 1), (0, 1)), ((0, -1), (0, -1)), ((1, 1), (1, 1)), ((1, -1), (1, -1)), ((0, 1), (1, -1))]
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
                    tkey = tuple(sorted((i, 2 * s * mu * GRIPS[g][2]) for (i, mu, g) in bodies))
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
            maxdev = 0.0
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
                        if F2 == 0:
                            rho_num = (r[i][3] - r[ip][3]) / (r[i][2] - r[ip][2]) * \
                                (0.5 * (r[i][0] + r[ip][0])) / (0.5 * (r[i][1] + r[ip][1]))
                            P(f"    grip={g:9s} k={k} sigma={sg:+d}: rho_mark numerical={rho_num:+.3e} predicted=0")
                            continue
                        rho_num = (r[i][3] - r[ip][3]) / (r[i][2] - r[ip][2]) * \
                            (0.5 * (r[i][0] + r[ip][0])) / (0.5 * (r[i][1] + r[ip][1]))
                        wb = 0.5 * (w(i) + w(ip)); Sb = 0.5 * (Sig(i, i) + Sig(ip, ip))
                        rho_pred = 4 * F2 * (F0 + F2 * wb) / (F1 ** 2 * Gb + F2 ** 2 * Sb) * \
                            (Gm[i] * ph[i] - Gm[ip] * ph[ip]) / (ph[i] - ph[ip])
                        lead = 4 * F0 * F2 / F1 ** 2 * (1 + amark)
                        P(f"    grip={g:9s} k={k} sigma={sg:+d}: rho_mark numerical={rho_num:.8f} "
                          f"predicted (5.20)={rho_pred:.8f} leading (4F0F2/F1^2)(1+a_mark)={lead:.6f}")
                # bond: pair x1 = X, x2 = X + 2 e2 (ring: X + 2 e), translated by e; square grip
                e2 = np.array([0, 1, 0]) if D == 3 else ex
                Y1, Y2 = X, X + 2 * e2
                Y1p, Y2p = Y1 + ex, Y2 + ex
                Ym, Ymp = X + e2, X + e2 + ex
                Ys = Y2p + 2 * ex if D == 1 else Ymp + Rp * ex
                js = [lat.site(v) for v in (Y1, Y2, Y1p, Y2p, Ym, Ymp)]
                jsrc = lat.site(Ys)
                phi = lambda v: -lat.Ga(v, Ys, h)
                G12, G12p = lat.Ga(Y1, Y2, h), lat.Ga(Y1p, Y2p, h)
                dphi1, dphi2 = phi(Y1) - phi(Y1p), phi(Y2) - phi(Y2p)
                dphim = phi(Ym) - phi(Ymp)
                mr = (dphi1 + dphi2) / (2 * dphim)
                abond = (0.5 * (phi(Y1) + phi(Y1p)) + 0.5 * (phi(Y2) + phi(Y2p))) * (G12 - G12p) / \
                    (2 * 0.5 * (G12 + G12p) * dphim)
                P(f"  bond (square grips), pair separation 2, source at {list(Ys)}: m_r={mr:.6f}, a_bond={abond:+.6f}")
                F0, F1, F2 = GRIPS["square"]
                for (c1, c2) in combos2:
                    mu1, mu2 = c1[1] * MK[c1[0]], c2[1] * MK[c2[0]]
                    def bond(a, b_):
                        B = {}; Wb = {}
                        for s in S:
                            e12 = E([(a, mu1, "square"), (b_, mu2, "square")], s, jsrc)
                            e1 = E([(a, mu1, "square")], s, jsrc); e2_ = E([(b_, mu2, "square")], s, jsrc)
                            e0 = E([], 0.0, jsrc)
                            bb = [e12[t] - e1[t] - e2_[t] + e0[t] for t in range(3)]
                            B[s] = bb[2]; Wb[s] = 0.5 * (bb[0] - bb[1])
                        return stencil(B)[1], stencil(Wb)[1], stencil(B)[0]
                    B2, W2, B1 = bond(js[0], js[1]); B2p, W2p, B1p = bond(js[2], js[3])
                    out = []
                    for ii, mui in ((1, mu1), (2, mu2)):
                        rm = single(js[4], mui, "square", jsrc); rmp = single(js[5], mui, "square", jsrc)
                        rho_num = ((W2 - W2p) / (0.5 * (B2 + B2p))) / ((rm[2] - rmp[2]) / (0.5 * (rm[0] + rmp[0])))
                        # closed forms (5.19), (5.21) at order mu1 mu2
                        Bp = lambda y1, y2, j1, j2: -mu1 * mu2 * (F1 ** 2 * lat.Ga(y1, y2, h) + F2 ** 2 * Sig(j1, j2))
                        Wp = lambda y1, y2: -2 * mu1 * mu2 * lat.Ga(y1, y2, h) * F1 * F2 * (phi(y1) + phi(y2))
                        Bbar = 0.5 * (Bp(Y1, Y2, js[0], js[1]) + Bp(Y1p, Y2p, js[2], js[3]))
                        C1bar = 0.5 * (mui * (F0 + F2 * w(js[4])) + mui * (F0 + F2 * w(js[5])))
                        rho_pred = ((Wp(Y1, Y2) - Wp(Y1p, Y2p)) / Bbar) / (mui * F1 * dphim / C1bar)
                        out.append(f"rho_bond,{ii} num={rho_num:.8f} pred={rho_pred:.8f}")
                    P(f"    (k,sigma)=({c1[0]},{c1[1]:+d}),({c2[0]},{c2[1]:+d}): B2={B2:+.6e} (s^1 part {B1:+.1e}); "
                      + "; ".join(out) + f"; leading m_r+a_bond={mr + abond:.6f}")
            P(f" max relative deviation of C1, Cmark, W1, Wmark from (5.18) over this lattice: {maxdev:.2e}\n")


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
    P("\n(5.25) ring: a_mark for a body between anchor and source (d=10, d+1, source at d+1+3) -> 1 as L -> inf")
    for L in (32, 64, 256, 1024, 4096):
        Gm = lambda x: 1 / KA + x * (L - x) / (KH * L)
        xs = 14
        ph = lambda x: -(1 / KA + (x * (L - x) + xs * (L - xs) - abs(xs - x) * (L - abs(xs - x))) / (2 * KH * L))
        a = 0.5 * (ph(10) + ph(11)) * (Gm(10) - Gm(11)) / (0.5 * (Gm(10) + Gm(11)) * (ph(10) - ph(11)))
        P(f"  L={L:5d}: a_mark={a:.6f}")
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
