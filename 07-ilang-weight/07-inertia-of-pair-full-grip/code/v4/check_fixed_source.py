"""Fixed held source g_s Phi_{x_s} in laboratory coordinates (07-inertia-of-pair-full-grip, N_f = 1, t_f = 1).

The source acts on the field at the fixed place x_s = 0; no P sectors. Centre contract (7.14): h_c = E_b(P) + V,
V = first-order matrix of the source between the Bloch states Psi_P of the selected level; its P = 0 symbol (row sum)
W_ex(X) = sum_P e^{iPX} <Psi_P|g_s Phi|Psi_0>, midpoint gauge, against W_0(X) = g_s rho_0(x_s - X) (7.15).
Parts (command-line argument; default: all):
  exact   EXACT, full laboratory space (bodies j, l, field y, branches), L = 12, 16: eigenvalues of C + g Phi_{x_s}
          in the selected band against h_c with V from (ME) exact matrix elements, (mid) W_0, (held) held-field
          average without kinetic part, (nobond) the two bodies without bond; row sums against W_0.
  me64    EXACT first order (exact Bloch eigenvectors) and BAND (band contract (2.10) in laboratory coordinates
          with the fixed source), L = 64: W_ex' against W_0', pair and bond.
  me128   EXACT first order and BAND, L = 128, case R (the largest exact size run: one shift-invert solve per P).
  bandS1, bandS2  BAND, L = 256: W_ex' and the lowest band eigenvalues with the fixed source.
Outputs: output/fixed_source_<part>.txt, output/fixed_source_<part>.json.
"""
import json
import sys
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

sys.path.insert(0, str(Path(__file__).parent))
from check_pair_full_grip import (TF, SX, shift, field, band_contract, body_kappa, body_level, pair_ops,  # noqa: E402
                                  parity_idx, params)

OUT = Path(__file__).parent / "output"
LOG = []


def log(s=""):
    print(s, flush=True)
    LOG.append(s)


def hsign(L, r):  # signed representative of the relative place
    r = np.asarray(r) % L
    return np.where(r > L // 2, r - L, r)


def bloch_P(L):
    P = 2 * np.pi * np.arange(L) / L
    return np.where(P > np.pi + 1e-12, P - 2 * np.pi, P)


def band_setup(L, g1, g2, t1, t2):
    E, Om, dd, kk, _ = band_contract(L, g1, g2, t1, t2)
    ev = np.arange(0, L, 2)
    low = (body_kappa(L, g1, t1) + body_kappa(L, g2, t2)) < 0
    U = E[ev] + dd[0][ev] + dd[1][ev]
    i0, i1 = np.arange(len(ev)), (np.arange(len(ev)) + 1) % len(ev)

    def band(P):
        h = np.diag(U).astype(complex)
        t = kk[0][ev + 1] * np.exp(-2j * P) + kk[1][ev + 1]
        h[i0, i1] += t
        h[i1, i0] += t.conj()
        w, v = np.linalg.eigh(h)
        k = 0 if low else -1
        return w[k], v[:, k]
    return dict(Om=Om, ev=ev, low=low, band=band)


def sector_selected(L, g1, g2, t1, t2, bs, P, idx):
    """Exact selected level of the sector contract at P (parity class of the selected level)."""
    eb, fb = bs['band'](P)
    H = pair_ops(L, g1, g2, t1, t2, P)[idx][:, idx]
    if len(idx) <= 3000:
        w, v = np.linalg.eigh(H.toarray())
        c = np.argsort(np.abs(w - eb))[:10]
        w, v = w[c], v[:, c]
    else:
        w, v = spla.eigsh(H.tocsc(), k=8, sigma=eb, which='LM', tol=0)
    best = (-1,)
    for k in range(len(w)):
        x = np.zeros(4 * L * L, complex)
        x[idx] = v[:, k]
        a = np.einsum('ry,ry->r', bs['Om'], x.reshape(2, 2, L, L)[0, 0])[bs['ev']]
        ov = abs(np.vdot(fb, a)) ** 2
        if ov > best[0]:
            best = (ov, w[k], x.reshape(4 * L, L))
    return best[1], best[2]


def mid_density(L, A):  # field density at distance k from the midpoint; A: (4L, L) rows (s, r), cols y - j
    pr = (np.abs(A) ** 2).reshape(4, L, L).sum(0)
    dens = np.zeros(L)
    for r in range(L):
        h = int(hsign(L, r))
        dens += np.roll(pr[r], -(h // 2)) if h % 2 == 0 else 0.5 * (np.roll(pr[r], -((h - 1) // 2)) + np.roll(pr[r], -((h + 1) // 2)))
    return dens


class RowSum:
    """P = 0 symbol of the first-order source matrix in the midpoint gauge: W_ex(X)/g_s, source at x_s = 0."""

    def __init__(self, L, A0, hrow):
        self.L, self.A0, self.hrow, self.M = L, A0, np.asarray(hrow, float), {}

    def add(self, P, A):
        ph = np.exp(-0.5j * P * self.hrow)[:, None]
        ov = np.vdot(ph * A, self.A0)  # <u_P|u_0>
        A = A * np.exp(1j * np.angle(ov))
        q = np.einsum('my,my->y', A.conj(), self.A0)
        self.M[float(P)] = np.sum(np.exp(1j * P * np.arange(self.L)) * q) / self.L

    def W(self):
        X = np.arange(self.L)
        return sum(np.exp(1j * P * X) * m for P, m in self.M.items()).real


def grad_X(W, L, s):  # central difference in X at X = x_s - s = -s
    return (W[(-s + 1) % L] - W[(-s - 1) % L]) / 2


def grad_k(rho, L, s):  # gradient in X of g_s rho(x_s - X), per unit g_s
    return (rho[(s - 1) % L] - rho[(s + 1) % L]) / 2


def densities(L, g1, g2, t1, t2, bs, A0):
    """rho_mid (exact P=0), rho_held (f0^2-average of held densities), rho_nobond (bodies without bond),
    single-body densities rho_1, rho_2 (exact P=0, from the body)."""
    _, f0 = bs['band'](0.0)
    f0 = np.abs(f0)
    rb = [np.abs(u[:L]) ** 2 + np.abs(u[L:]) ** 2 for u in (body_level(L, g, t, 0.0, vec=True)[1] for g, t in ((g1, t1), (g2, t2)))]
    held, nob = np.zeros(L), np.zeros(L)
    for i, r in enumerate(bs['ev']):
        h = int(hsign(L, r))
        held += f0[i] ** 2 * np.roll(bs['Om'][r] ** 2, -(h // 2))
        nob += f0[i] ** 2 * (np.roll(rb[0], -(h // 2)) + np.roll(rb[1], h // 2) - 1.0 / L)
    return dict(mid=mid_density(L, A0), held=held, nobond=nob, b1=rb[0], b2=rb[1])


def single_rowsum(L, g, t):  # exact first-order row sum of one body (centre = body place)
    _, u0 = body_level(L, g, t, 0.0, vec=True)
    rs = RowSum(L, u0.reshape(2, L), np.zeros(2))
    for P in bloch_P(L):
        rs.add(P, body_level(L, g, t, P, vec=True)[1].reshape(2, L))
    return rs.W()


# ---------------- EXACT: full laboratory space, basis (s1, s2, j, r = l - j, y) ----------------
def lab_ops(L, g1, g2, t1, t2):
    S, I2, IL = shift(L), sp.identity(2), sp.identity(L)
    sg = np.array([1.0, -1.0])
    s1, s2, j, r, y = np.meshgrid(*(np.arange(k) for k in (2, 2, L, L, L)), indexing='ij')
    dg = sg[s1] * g1 * (y == j) + sg[s2] * g2 * (y == (j + r) % L)
    mX = sp.csr_matrix(-1j * SX)
    A1 = 0.5 * t1 * sp.kron(sp.kron(mX, I2), sp.kron(S.T, sp.kron(S, IL)))   # j -> j+1, r -> r-1
    A2 = 0.5 * t2 * sp.kron(sp.kron(I2, mX), sp.kron(IL, sp.kron(S.T, IL)))  # l -> l+1: r -> r+1
    H = sp.kron(sp.identity(4 * L * L), -TF * (S + S.T)) + sp.diags(dg.ravel()) + A1 + A1.conj().T + A2 + A2.conj().T
    return H.tocsr(), np.flatnonzero(((s1 + s2 + r) % 2 == 0).ravel()), (y == 0).ravel().astype(float)


def centre_eigs(EP, Ps, M, g):  # eigenvalues of h_c = E_b(P) + g M (plane-wave basis)
    return np.sort(np.linalg.eigvalsh(np.diag(EP) + g * M))


def M_from_density(rho, Ps):  # M(P,P') = (1/L) sum_X rho(x_s - X) e^{-i(P-P')X}, x_s = 0; Ps[k] = 2 pi k / L
    L = len(rho)
    Wq = np.fft.fft(rho[(-np.arange(L)) % L])
    k = np.arange(L)
    return Wq[(k[:, None] - k[None, :]) % L] / L


def part_exact():
    res = []
    for name, p, svals in (("EA equal bodies", (12, 0.15, 1.0, 0.3), (2, 3, 4)),
                           ("EA equal bodies", (16, 0.15, 1.0, 0.3), (2, 3, 4, 5, 6)),
                           ("EB unequal bodies and speeds", (12, 0.15, 0.5, 0.3, 0.15), (2, 3, 4)),
                           ("EB unequal bodies and speeds", (16, 0.15, 0.5, 0.3, 0.15), (2, 3, 4, 5, 6))):
        L, g1, g2, t1, t2 = params(*p)
        bs, idx, Ps = band_setup(L, g1, g2, t1, t2), parity_idx(L), bloch_P(L)
        EP, AP = [], []
        for P in Ps:
            e, A = sector_selected(L, g1, g2, t1, t2, bs, P, idx)
            EP.append(e)
            AP.append(A)
        EP = np.array(EP)
        H, lidx, phi = lab_ops(L, g1, g2, t1, t2)
        B = np.zeros((4 * L ** 3, L), complex)
        for a, (P, A) in enumerate(zip(Ps, AP)):
            v = A.reshape(4, L, L)
            B[:, a] = np.stack([np.roll(v, jj, axis=-1) * np.exp(1j * P * jj) for jj in range(L)], axis=1).ravel() / np.sqrt(L)
        resid = float(np.max(np.linalg.norm(H @ B - B * EP[None, :], axis=0)))
        out_cls = float(np.linalg.norm(np.delete(B, lidx, axis=0)))
        Hc, Bc, pc = H[lidx][:, lidx].tocsc(), B[lidx], phi[lidx]
        Mex = Bc.conj().T @ (pc[:, None] * Bc)
        dn = densities(L, g1, g2, t1, t2, bs, AP[int(np.argmin(np.abs(Ps)))])
        Mv = {"ME": Mex, "mid": M_from_density(dn['mid'], Ps), "held": M_from_density(dn['held'], Ps),
              "nobond": M_from_density(dn['nobond'], Ps)}
        g = 1e-7
        K = L // 2 + 1
        E0 = np.sort(EP)
        sh, dev, nsel = {}, {}, []
        for sgn in (1, -1):
            w, v = spla.eigsh(Hc + sp.diags(sgn * g * pc), k=3 * L, sigma=E0.mean() + 1e-9, which='LM', tol=0)
            wt = np.linalg.norm(Bc.conj().T @ v, axis=0) ** 2
            sel = np.sort(w[wt > 0.5])
            nsel.append(int(len(sel)))
            sh[sgn] = {"exact": (sel - E0) / (sgn * g)}
            for k, M in Mv.items():
                sh[sgn][k] = (centre_eigs(EP, Ps, M, sgn * g) - E0) / (sgn * g)
        for k in Mv:
            dev[k] = [max(float(np.max(np.abs(sh[s]["exact"][:K] - sh[s][k][:K]))) for s in (1, -1)),
                      max(float(np.max(np.abs(sh[s]["exact"] - sh[s][k]))) for s in (1, -1))]
        bond = max(float(np.max(np.abs(sh[s]["mid"][:K] - sh[s]["nobond"][:K]))) for s in (1, -1))
        kin = max(float(np.max(np.abs(sh[s]["mid"][:K] - sh[s]["held"][:K]))) for s in (1, -1))
        log(f"== EXACT {name}: L={L} g1={g1:.5g} g2={g2:.5g} tau1={t1:.4g} tau2={t2:.4g} (lab dimension {len(lidx)})")
        log(f"   Bloch states of the sector contracts in laboratory coordinates: max residual {resid:.1e}, weight outside class {out_cls:.1e}")
        log(f"   band levels selected with the fixed source: {nsel} of {L}; first-order shifts (eigenvalue - E_b)/g, g={g:g}")
        log(f"   scale over the lowest {K} levels (|P|<=pi/2): bond effect max|mid-nobond|={bond:.3e}, kinetic effect max|mid-held|={kin:.3e}")
        for k in Mv:
            log(f"   max|exact - h_c[{k}]|: lowest {K}: {dev[k][0]:.3e} ({dev[k][0] / bond:.3f} of bond effect), all {L}: {dev[k][1]:.3e}")
        rs = RowSum(L, AP[int(np.argmin(np.abs(Ps)))], np.tile(hsign(L, np.arange(L)), 4))
        for P, A in zip(Ps, AP):
            rs.add(P, A)
        Wp, W1, W2 = rs.W(), single_rowsum(L, g1, t1), single_rowsum(L, g2, t2)
        rows = []
        for s in svals:
            ex = grad_X(Wp, L, s)
            exb = ex - grad_X(W1, L, s) - grad_X(W2, L, s)
            d = {k: grad_k(dn[k], L, s) for k in ("mid", "held", "nobond", "b1", "b2")}
            Wb = d["mid"] - d["b1"] - d["b2"]
            rows.append(dict(s=s, Wex=ex, W0=d["mid"], Wheld=d["held"], Wex_bond=exb, Wb=Wb,
                             Wb_held=d["held"] - d["b1"] - d["b2"], Wex1=grad_X(W1, L, s), W1=d["b1"]))
            log(f"   s={s}: W_ex'/g_s={ex:.6e} W_0'/g_s={d['mid']:.6e}; bond: W_ex,b'={exb:.4e} W_b'={Wb:.4e} "
                f"(diff/|W_b'|={(exb - Wb) / abs(Wb):.2e}; held-field average {(d['held'] - d['b1'] - d['b2'] - Wb) / abs(Wb):.2e}; "
                f"single body W_ex,1'/W_1'-1={grad_X(W1, L, s) / d['b1'] - 1:.1e})")
        res.append(dict(case=name, L=L, g1=g1, g2=g2, tau1=t1, tau2=t2, residual=resid, n_selected=nsel, K=K,
                        bond_effect=bond, kinetic_effect=kin, deviations=dev, gradients=rows))
    return res


# ---------------- EXACT first order at larger L (exact Bloch eigenvectors, v_{-P} = Z conj v_P) ----------------
def exact_rowsums(L, g1, g2, t1, t2, bs):
    idx, Ps = parity_idx(L), bloch_P(L)
    Z = np.repeat([1.0, -1.0, -1.0, 1.0], L)[:, None]
    E0, A0 = sector_selected(L, g1, g2, t1, t2, bs, 0.0, idx)
    rs = RowSum(L, A0, np.tile(hsign(L, np.arange(L)), 4))
    rs.add(0.0, A0)
    for P in Ps[(Ps > 0)]:
        _, A = sector_selected(L, g1, g2, t1, t2, bs, P, idx)
        rs.add(P, A)
        if P < np.pi - 1e-12:
            rs.add(-P, Z * A.conj())
    return rs.W(), A0, E0


# ---------------- BAND: band contract (2.10) in laboratory coordinates with the fixed source ----------------
def band_lab(L, g1, g2, t1, t2, gsrc):
    """Sparse band contract on (j, r/2), r = l - j even, with the source gsrc on the field at x_s = 0:
    exact held blocks with the source, second-order Schrieffer-Wolff through the flipped held levels."""
    ev = np.arange(0, L, 2)
    nr = len(ev)
    E, Om = np.zeros((L, nr)), np.zeros((L, nr, L))
    for j in range(L):
        e, u = np.linalg.eigh(np.array([field(L, [(j, g1), ((j + r) % L, g2), (0, gsrc)]) for r in ev]))
        E[j], Om[j] = e[:, 0], u[:, :, 0] * np.sign(u[:, :, 0].sum(1))[:, None]
    I = lambda j, r: (np.asarray(j) % L) * nr + (np.asarray(r) % L) // 2
    diag, rows, cols, vals = E.copy(), [], [], []
    ro = np.arange(1, L, 2)
    for x in range(L):
        for body, t in ((1, t1), (2, t2)):
            if body == 1:  # body 1 flipped at x, body 2 at x + r (r odd): connects (x-1, r+1) and (x+1, r-1)
                Hs = [field(L, [(x, -g1), ((x + r) % L, g2), (0, gsrc)]) for r in ro]
                ja, ra, jb, rb = (x - 1) % L, (ro + 1) % L, (x + 1) % L, (ro - 1) % L
            else:          # body 1 at x, body 2 flipped at x + r: connects (x, r-1) and (x, r+1)
                Hs = [field(L, [(x, g1), ((x + r) % L, -g2), (0, gsrc)]) for r in ro]
                ja, ra, jb, rb = x, (ro - 1) % L, x, (ro + 1) % L
            ek, uk = np.linalg.eigh(np.array(Hs))
            Oa, Ob = Om[ja, ra // 2], Om[jb, rb // 2]
            Ea, Eb = E[ja, ra // 2][:, None], E[jb, rb // 2][:, None]
            oa, ob = np.einsum('axk,ax->ak', uk, Oa), np.einsum('axk,ax->ak', uk, Ob)
            q = t ** 2 / 4
            np.add.at(diag, (np.full(len(ro), ja), ra // 2), q * np.sum(oa ** 2 / (Ea - ek), 1))
            np.add.at(diag, (np.full(len(ro), jb), rb // 2), q * np.sum(ob ** 2 / (Eb - ek), 1))
            k = -q * np.sum(oa * ob * 0.5 * (1 / (Ea - ek) + 1 / (Eb - ek)), 1)
            a, b = I(np.full(len(ro), ja), ra), I(np.full(len(ro), jb), rb)
            rows += [a, b]
            cols += [b, a]
            vals += [k, k]
    n = L * nr
    H = sp.coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n, n)).tocsr()
    return H + sp.diags(diag.ravel())


def band_lab_first_order(L, g1, g2, t1, t2):
    """The same band contract at g_s = 0 (H0) and its exact first derivative in g_s (dH), from the held spectra
    without source: dE = Omega(p)^2, dOmega = R' e_p Omega(p), and dR = R e_p e_p^T R, dR/dE = -R^2 in the
    resolvent form kappa = -(tau^2/8)[<b|R(E_a)|a> + <b|R(E_b)|a>], d = (tau^2/4)<a|R(E_a)|a>."""
    ev = np.arange(0, L, 2)
    nr = len(ev)
    G = {}
    for r in ev:
        e, U = np.linalg.eigh(field(L, [(0, g1), (r, g2)]))
        Om = U[:, 0] * np.sign(U[:, 0].sum())
        G[r] = (e[0], Om, ((U[:, 1:] / (e[0] - e[1:])) @ U[:, 1:].T) * Om[None, :])
    p = np.arange(L)  # source place in the frame of the intermediate held level
    x = (-p) % L      # its origin (place of body 1)
    I = lambda j, r: (np.asarray(j) % L) * nr + (np.asarray(r) % L) // 2
    d0, d1 = np.zeros((L, nr)), np.zeros((L, nr))
    for r in ev:
        d0[:, r // 2] = G[r][0]
        d1[x, r // 2] = G[r][1][p] ** 2
    rows, cols, v0, v1 = [], [], [], []
    for body, t in ((1, t1), (2, t2)):
        q = t ** 2 / 4
        for rho in range(1, L, 2):
            if body == 1:
                e, U = np.linalg.eigh(field(L, [(0, -g1), (rho, g2)]))
                ra, rb, sa, sb, pa, pb, ja, jb = (rho + 1) % L, rho - 1, -1, 1, (p + 1) % L, (p - 1) % L, (x - 1) % L, (x + 1) % L
            else:
                e, U = np.linalg.eigh(field(L, [(0, g1), (rho, -g2)]))
                ra, rb, sa, sb, pa, pb, ja, jb = rho - 1, (rho + 1) % L, 0, 0, p, p, x, x
            (Ea, Oa, dOa), (Eb, Ob, dOb) = G[ra], G[rb]
            a, b = U.T @ np.roll(Oa, sa), U.T @ np.roll(Ob, sb)
            da, db = U.T @ np.roll(dOa[:, pa], sa, axis=0), U.T @ np.roll(dOb[:, pb], sb, axis=0)
            dEa, dEb = Oa[pa] ** 2, Ob[pb] ** 2
            ra_, rb_ = 1 / (Ea - e), 1 / (Eb - e)

            def dG(ri, dE):
                return (db.T @ (a * ri)) + (da.T @ (b * ri)) + (U @ (b * ri)) * (U @ (a * ri)) - dE * np.sum(a * b * ri ** 2)
            k0 = -q * 0.5 * (np.sum(a * b * ra_) + np.sum(a * b * rb_))
            k1 = -q * 0.5 * (dG(ra_, dEa) + dG(rb_, dEb))
            for (jj, rr, o, do, ri, dE) in ((ja, ra, a, da, ra_, dEa), (jb, rb, b, db, rb_, dEb)):
                np.add.at(d0, (jj, np.full(L, rr // 2)), q * np.sum(o * o * ri))
                np.add.at(d1, (jj, np.full(L, rr // 2)), q * (2 * (do.T @ (o * ri)) + (U @ (o * ri)) ** 2 - dE * np.sum(o * o * ri ** 2)))
            ia, ib = I(ja, ra), I(jb, rb)
            rows += [ia, ib]
            cols += [ib, ia]
            v0 += [np.full(L, k0), np.full(L, k0)]
            v1 += [k1, k1]
    n = L * nr
    mk = lambda vals, dg: (sp.coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n, n)).tocsr()
                           + sp.diags(dg.ravel()))
    return mk(v0, d0), mk(v1, d1)


def single_band_lab(L, g, t, gsrc):  # band contract of one body in laboratory coordinates with the source
    E, Om = np.zeros(L), np.zeros((L, L))
    for j in range(L):
        e, u = np.linalg.eigh(field(L, [(j, g), (0, gsrc)]))
        E[j], Om[j] = e[0], u[:, 0] * np.sign(u[:, 0].sum())
    H = np.diag(E)
    for x in range(L):
        ek, uk = np.linalg.eigh(field(L, [(x, -g), (0, gsrc)]))
        a, b = (x - 1) % L, (x + 1) % L
        oa, ob, q = uk.T @ Om[a], uk.T @ Om[b], t ** 2 / 4
        H[a, a] += q * np.sum(oa ** 2 / (E[a] - ek))
        H[b, b] += q * np.sum(ob ** 2 / (E[b] - ek))
        H[a, b] = H[b, a] = H[a, b] - q * np.sum(oa * ob * 0.5 * (1 / (E[a] - ek) + 1 / (E[b] - ek)))
    return H


def band_rowsums(L, g1, g2, t1, t2, bs, gsrc=1e-5, fd=False):
    """First-order source term dH of the band contract in laboratory coordinates (odd part in gsrc), its row sum
    in the midpoint gauge (pair) and per body; H0 and Bloch vectors of the band contract."""
    H0, dH = band_lab_first_order(L, g1, g2, t1, t2)
    if fd:  # validation of the first derivative against finite differences of the band contract with the source
        Hp, Hm = band_lab(L, g1, g2, t1, t2, gsrc), band_lab(L, g1, g2, t1, t2, -gsrc)
        fdv = (float(abs((Hp + Hm) / 2 - H0).max() / abs(H0).max()), float(abs((Hp - Hm) / (2 * gsrc) - dH).max() / abs(dH).max()))
        log(f"   band contract with the source: analytic first order vs finite differences +-{gsrc:g}: rel. max diff H0 {fdv[0]:.1e}, dH {fdv[1]:.1e}")
    ev, Ps = bs['ev'], bloch_P(L)
    j = np.arange(L)
    F = {float(P): bs['band'](P) for P in Ps}
    Bl = lambda P: (np.exp(1j * P * j)[:, None] * F[float(P)][1][None, :]).ravel() / np.sqrt(L)
    resid = max(float(np.linalg.norm(H0 @ Bl(P) - F[float(P)][0] * Bl(P))) for P in Ps[:4])
    hr = hsign(L, ev)
    f0 = F[0.0][1]
    phi0 = (dH @ Bl(0.0)).reshape(L, len(ev))
    FT = np.fft.fft(phi0, axis=0)  # sum_j e^{-iPj} phi0(j, r), P = 2 pi k / L
    M = {}
    for k, P in enumerate(2 * np.pi * np.arange(L) / L):
        Pr = float(bloch_P(L)[k])
        f = F[Pr][1]
        f = f * np.exp(1j * np.angle(np.vdot(np.exp(-0.5j * Pr * hr) * f, f0)))
        M[Pr] = np.vdot(f, FT[k]) / np.sqrt(L)
    W = sum(np.exp(1j * P * j) * m for P, m in M.items()).real
    Ws = []
    for g, t in ((g1, t1), (g2, t2)):
        dHs = (single_band_lab(L, g, t, gsrc) - single_band_lab(L, g, t, -gsrc)) / (2 * gsrc)
        Ws.append(dHs.sum(1))  # row sum: the Wannier states of one body are its places
    return W, Ws, H0, dH, F, resid


def report(L, svals, dn, ex=None, band=None):
    """Gradients in X at distance s (per unit g_s): pair W', bond W_b' = W_pair' - W_1' - W_2', against W_0' (7.15)."""
    rows = []
    for s in svals:
        d = {k: grad_k(dn[k], L, s) for k in ("mid", "held", "b1", "b2")}
        Wb = d["mid"] - d["b1"] - d["b2"]
        row = dict(s=s, W0=d["mid"], Wb=Wb, Wb_held=d["held"] - d["b1"] - d["b2"], W1=d["b1"], W2=d["b2"])
        txt = f"   s={s}: W_0'/g_s={d['mid']:.6e}, W_b'/g_s={Wb:.4e}; held-field average (no kinetic part): W_b,held'/W_b'-1={row['Wb_held'] / Wb - 1:.2e}"
        for lab, W in (("exact", ex), ("band", band)):
            if W is None:
                continue
            Wp, W1, W2 = (grad_X(w, L, s) for w in W)
            row[lab] = dict(W=Wp, Wb=Wp - W1 - W2, W1=W1, W2=W2)
            txt += (f"\n     {lab} fixed source: W'/W_0'-1={Wp / d['mid'] - 1:.2e}, (W'-W_0')/|W_b'|={(Wp - d['mid']) / abs(Wb):.2e}, "
                    f"W_b'/W_b'(7.15)-1={(Wp - W1 - W2) / Wb - 1:.2e} (= Gamma_b ratio), W_1'/W_1'(7.15)-1={W1 / d['b1'] - 1:.1e}, W_2'/W_2'(7.15)-1={W2 / d['b2'] - 1:.1e}")
        log(txt)
        rows.append(row)
    return rows


def part_large(name, p, svals, exact=True, band=True, eig=False):
    L, g1, g2, t1, t2 = params(*p)
    bs = band_setup(L, g1, g2, t1, t2)
    log(f"== {name}: L={L} g1={g1:.5g} g2={g2:.5g} tau1={t1:.4g} tau2={t2:.4g}")
    res = dict(case=name, L=L, g1=g1, g2=g2, tau1=t1, tau2=t2)
    if exact:
        Wp, A0, E0 = exact_rowsums(L, g1, g2, t1, t2, bs)
        Wex = (Wp, single_rowsum(L, g1, t1), single_rowsum(L, g2, t2))
    else:
        E0, A0 = sector_selected(L, g1, g2, t1, t2, bs, 0.0, parity_idx(L))
        Wex = None
    dn = densities(L, g1, g2, t1, t2, bs, A0)
    Wbd = None
    if band:
        Wbp, Wbs, H0, dH, F, resid = band_rowsums(L, g1, g2, t1, t2, bs, fd=(L <= 64))
        Wbd = (Wbp, Wbs[0], Wbs[1])
        log(f"   band contract in laboratory coordinates: residual of its Bloch states {resid:.1e} (without source)")
    res['gradients'] = report(L, svals, dn, Wex, Wbd)
    if eig:  # lowest band eigenvalues of the band contract with the fixed source against centre contracts
        Ps = bloch_P(L)
        j = np.arange(L)
        B = np.stack([(np.exp(1j * P * j)[:, None] * F[float(P)][1][None, :]).ravel() / np.sqrt(L) for P in Ps], axis=1)
        EP = np.array([F[float(P)][0] for P in Ps])
        Mv = {"ME": B.conj().T @ (dH @ B), "mid": M_from_density(dn['mid'], Ps), "held": M_from_density(dn['held'], Ps)}
        nob = M_from_density(dn['nobond'], Ps)
        g, K = 1e-6, 21
        Es = np.sort(EP)
        sig = Es[0] - 1e-3 * (Es[1] - Es[0]) if bs['low'] else Es[-1] + 1e-3 * (Es[-1] - Es[-2])
        w, v = spla.eigsh((H0 + g * dH).tocsc(), k=60, sigma=sig, which='LM', tol=0)
        wt = np.linalg.norm(B.conj().T @ v, axis=0) ** 2
        sel = np.sort(w[wt > 0.5])
        sel = sel[:K] if bs['low'] else sel[-K:]
        E0s = Es[:K] if bs['low'] else Es[-K:]
        pick = (lambda a: a[:K]) if bs['low'] else (lambda a: a[-K:])
        sh = {"band": (sel - E0s) / g}
        for k, M in list(Mv.items()) + [("nobond", nob)]:
            sh[k] = (pick(centre_eigs(EP, Ps, M, g)) - E0s) / g
        bond = float(np.max(np.abs(sh["mid"] - sh["nobond"])))
        log(f"   lowest {len(sel)} band levels with the fixed source (g={g:g}), first-order shifts; bond effect max|mid-nobond|={bond:.3e}, "
            f"kinetic effect max|mid-held|={float(np.max(np.abs(sh['mid'] - sh['held']))):.3e}")
        res['eig'] = {}
        for k in Mv:
            dv = float(np.max(np.abs(sh["band"] - sh[k])))
            res['eig'][k] = dv
            log(f"     max|band - h_c[{k}]|={dv:.3e} ({dv / bond:.3f} of bond effect)")
        res['eig']['bond_effect'] = bond
    return res


PARTS = {
    "exact": lambda: part_exact(),
    "me64": lambda: [part_large("A equal bodies", (64, 0.15, 1.0, 0.3), (4, 8, 12, 16)),
                     part_large("B unequal bodies and speeds", (64, 0.15, 0.5, 0.3, 0.15), (4, 8, 12, 16))],
    "me128": lambda: [part_large("R equal bodies, v1 case", (128, 0.15, 1.0, 0.3), (8, 16, 32))],
    "bandS1": lambda: [part_large("S1 equal bodies, regime (ii)", (256, 0.10, 1.0, 0.4), (16, 32, 64), exact=False, eig=True)],
    "bandS2": lambda: [part_large("S2 equal bodies, regime (ii), smaller eta", (256, 0.05, 1.0, 0.4), (16, 32, 64), exact=False, eig=True)],
}

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for part in (sys.argv[1:] or list(PARTS)):
        LOG.clear()
        log(f"# part {part}")
        out = PARTS[part]()
        (OUT / f"fixed_source_{part}.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
        (OUT / f"fixed_source_{part}.json").write_text(json.dumps(out, indent=1, default=float), encoding="utf-8")
