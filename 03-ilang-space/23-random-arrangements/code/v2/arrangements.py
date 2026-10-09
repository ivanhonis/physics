"""Package 23-random-arrangements, code v2: parts T1, T1b, T2, T3, T4 of question.md.

Run from the project root:
  .venv/Scripts/python.exe 03-ilang-space/23-random-arrangements/code/v2/arrangements.py [T1 T1b T2 T3 T4]
(no argument: all parts in this order; T4 reads output/T3.json for its reference value).
Outputs: compact JSON summaries in code/v2/output/<part>.json.

Changes from v1 (validation and reporting only; models, parameters, seeds, windows, decision rules and
the decision routine rng_decide are unchanged):
- edge_check: all-witness certification of every edge (every y checked against its error allowance);
- graph_summary: smallest nonzero absolute margin reported separately from the smallest margin/error ratio;
- table_checks: difference-aware error bound for D2 and 50-digit recomputation of sampled D2 entries;
- part_audit: per-part minima of the margins and certification counts.

Exactness (common setting of question.md):
- kernel values exp(-arg) are correctly rounded (50-digit Decimal);
- on the grid, overlaps S(D) and d0^2-values D2(D) are tabulated once per canonical displacement
  D = (d1, d2), 0 <= d2 <= d1 <= L/2, as math.fsum sums of positive terms (correctly rounded sums);
  D4-equivalent displacements share the entry, so their overlaps are bitwise identical;
- every neighbour decision compares only the small parts of d0^2: with d0^2 = C + w_h + w_h' + eta_hh'
  (C common), the constant C and the common place term never enter a comparison.
"""
import json
import math
import sys
import time
from decimal import Decimal, getcontext
from pathlib import Path

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components, dijkstra

OUT = Path(__file__).parent / "output"
UR = 2.0 ** -53          # unit roundoff of float64
XI = 2                   # kernel range xi
P_INC = 0.1              # inclusion probability p
LONG_R2 = 160            # r > 4/sqrt(p)  <=>  r^2 > 16/p = 160
EPS_LIST = [0.0, 1e-12, 1e-9, 1e-6, 1e-4, 1e-2]
getcontext().prec = 50


# ---------------------------------------------------------------- kernel and tables
def minimg(d, L):
    """Minimal-image absolute value of integer coordinate differences on Z/LZ."""
    d = np.mod(d, L)
    return np.minimum(d, L - d)


def kernel(L, kind):
    """kappa(v), v in (Z/LZ)^2, as float K[v1, v2] (correctly rounded) and as Decimal array."""
    m = minimg(np.arange(L), L)
    cache, K, Kd = {}, np.empty((L, L)), np.empty((L, L), dtype=object)
    for i in range(L):
        for j in range(L):
            a, b = int(m[i]), int(m[j])
            key = a + b if kind == "sep" else a * a + b * b
            if key not in cache:
                arg = (Decimal(key) if kind == "sep" else Decimal(key).sqrt()) / XI
                e = (-arg).exp()
                cache[key] = (float(e), e)
            K[i, j], Kd[i, j] = cache[key]
    return K, Kd


def tables(K):
    """S(D) = sum_l K(l) K(l-D) and D2(D) = sum_l (K(l) - K(l-D))^2 on canonical D (math.fsum)."""
    H = K.shape[0] // 2
    S, D2 = np.full((H + 1, H + 1), np.nan), np.full((H + 1, H + 1), np.nan)
    for d1 in range(H + 1):
        for d2 in range(d1 + 1):
            Ks = np.roll(K, (d1, d2), axis=(0, 1))          # Ks[l] = K[l - D]
            S[d1, d2] = math.fsum((K * Ks).ravel().tolist())
            D2[d1, d2] = math.fsum(((K - Ks) ** 2).ravel().tolist())
    return S, D2


def d2_bound_UR(S0, S, D2):
    """Difference-aware relative error bound of a D2 entry, in units UR (v2):
    |D2^ - D2| <= 2u sum_l |d_l| (k_l + k'_l) + 4u D2 <= 2u sqrt(D2) sqrt(2 S0 + 2 S) + 4u D2  (Cauchy-Schwarz),
    from correctly rounded kernel values, one rounding each in the difference and the square, and fsum."""
    return 2.0 * np.sqrt(2.0 * (S0 + S) / D2) + 4.0


def table_checks(S, D2, Kd):
    """Distinctness of table values; 50-digit check of selected entries (relative error in units UR).
    v2: also the D2 table: difference-aware bound (d2_bound_UR) and 50-digit recomputation of the picks."""
    H = S.shape[0] - 1
    srt = np.sort(S[~np.isnan(S)])
    dup = [v for v in np.unique(srt) if np.count_nonzero(S == v) > 1]
    dups = [[[int(p), int(q)] for p, q in np.argwhere(S == v)] for v in dup[:10]]
    picks = [(0, 0), (1, 0), (1, 1), (2, 1), (H // 4, H // 8), (H // 2, H // 4), (H // 2, H // 2),
             (3 * H // 4, H // 3), (H, 0), (H, H // 2), (H, H - 1), (H, H)]
    flat, worst = Kd.ravel().tolist(), Decimal(0)
    worstD, worstDb, S0 = Decimal(0), 0.0, float(S[0, 0])
    for d1, d2 in picks:
        sh = np.roll(Kd, (d1, d2), axis=(0, 1)).ravel().tolist()
        ex = sum(x * y for x, y in zip(flat, sh))
        worst = max(worst, abs((Decimal(float(S[d1, d2])) - ex) / ex))
        if (d1, d2) != (0, 0):                      # D2(0) = 0 exactly (fsum of exact zeros)
            exD = sum((x - y) * (x - y) for x, y in zip(flat, sh))
            eD = abs((Decimal(float(D2[d1, d2])) - exD) / exD)
            worstD = max(worstD, eD)
            worstDb = max(worstDb, float(eD) / UR / float(d2_bound_UR(S0, S[d1, d2], D2[d1, d2])))
    pos = ~np.isnan(D2) & (D2 > 0)
    return dict(n_entries=int(srt.size), all_values_distinct=bool(np.all(np.diff(srt) > 0)),
                n_coinciding_values=len(dup), coinciding_entries_first10=dups,
                min_rel_gap_between_distinct_values=float(np.min((np.diff(srt) / srt[1:])[np.diff(srt) > 0])),
                decimal_check_max_rel_err_in_UR=float(worst) / UR, assumed_rel_err_in_UR=4.0,
                S0=float(S[0, 0]), S_min=float(srt[0]),
                D2_zero_entry_exact=bool(D2[0, 0] == 0.0),
                D2_bound_rel_err_in_UR_max=float(d2_bound_UR(S0, S[pos], D2[pos]).max()),
                D2_decimal_check_n=len(picks) - 1,
                D2_decimal_check_max_rel_err_in_UR=float(worstD) / UR,
                D2_decimal_check_max_err_over_bound=worstDb)


def canon(c1, c2, L):
    """Canonical displacement indices (max, min of minimal-image |D1|, |D2|) for all pairs."""
    m1 = minimg(c1[None, :] - c1[:, None], L)
    m2 = minimg(c2[None, :] - c2[:, None], L)
    return np.maximum(m1, m2), np.minimum(m1, m2)


def places(L, seed):
    """T2 places: grid point (l1, l2) included iff rng.random((L, L))[l1, l2] < p."""
    mask = np.random.default_rng(seed).random((L, L)) < P_INC
    return np.nonzero(mask)


# ---------------------------------------------------------------- neighbour graph (4.3)
def rng_decide(sig, z, w, cid, Esig, Ez, Ew):
    """d0^2(h,h') = C + sig_hh' + (w_h + w_h' + z_hh'):  C common constant, sig = -2 S (overlap part),
    w (per place) and z (per pair, symmetric) the small parts.  y blocks {x,x'} iff
      T1 = (sig_xy - sig_xx') + ((w_y + z_xy) - (w_x' + z_xx')) < 0  and
      T2 = (sig_yx' - sig_xx') + ((w_y + z_yx') - (w_x + z_xx')) < 0,
    i.e. iff max(d0(x,y), d0(y,x')) < d0(x,x').  C and the common place term never enter; overlap parts
    are compared among themselves (difference exactly 0 for the same table entry), small parts among
    themselves.  m[x,x'] = min_{y != x,x'} max(T1, T2): edge iff m >= 0 (a tie m == 0 keeps the edge).
    Em: error estimate of m at the minimizing y: err of the larger of T1, T2 if they are separated by more
    than err T1 + err T2, else the larger error (cid: table-entry id of each pair, None: all distinct)."""
    n = len(w)
    sig = sig.copy()
    np.fill_diagonal(sig, np.inf)                    # excludes y = x and y = x'
    if z is not None:
        W1T = z + w[None, :]                         # W1T[x', y] = w_y + z_yx'
    m, ys = np.empty((n, n)), np.empty((n, n), dtype=np.intp)
    b1, b2, b3, cols = np.empty((n, n)), np.empty((n, n)), np.empty((n, n)), np.arange(n)
    with np.errstate(invalid="ignore"):
        for x in range(n):
            s = sig[x]
            np.subtract(s[None, :], s[:, None], out=b1)          # b1[x', y] = sig_xy - sig_xx'
            np.subtract(sig, s[:, None], out=b2)                 # b2[x', y] = sig_x'y - sig_xx'
            if z is not None:
                v, t = w + z[x], w[x] + z[x]
                np.subtract(v[None, :], v[:, None], out=b3)      # (w_y + z_xy) - (w_x' + z_xx')
                b1 += b3
                np.subtract(W1T, t[:, None], out=b3)             # (w_y + z_yx') - (w_x + z_xx')
                b2 += b3
            np.maximum(b1, b2, out=b1)
            b1[x, :] = np.inf
            y = np.argmin(b1, axis=1)
            ys[x], m[x] = y, b1[cols, y]
    np.fill_diagonal(m, np.nan)
    I, J = cols[:, None], cols[None, :]
    same1 = (cid[I, ys] == cid) if cid is not None else False
    same2 = (cid[ys, J] == cid) if cid is not None else False
    E1 = np.where(same1, 0.0, Esig[I, ys] + Esig)
    E2 = np.where(same2, 0.0, Esig[ys, J] + Esig)
    if Ez is not None:
        E1 = E1 + Ez[I, ys] + Ez + Ew[ys] + Ew[J]
        E2 = E2 + Ez[ys, J] + Ez + Ew[ys] + Ew[I]
    with np.errstate(invalid="ignore"):          # T1, T2 at the minimizing y (same operations as above)
        T1 = sig[I, ys] - sig
        T2 = sig[ys, J] - sig
        if z is not None:
            T1 += (w[ys] + z[I, ys]) - (w[J] + z)
            T2 += (w[ys] + z[ys, J]) - (w[I] + z)
        Es = E1 + E2
        Em = np.where(T1 - T2 > Es, E1, np.where(T2 - T1 > Es, E2, np.maximum(E1, E2)))
    return m, ys, Em


def edge_check(m, ei, ej, wit, c1, c2, batch=128, limit=40):
    """v2: all-witness certification of every edge {x,x'} (m >= 0).  For every y != x,x', T1 and T2 are
    recomputed with the same operations as in rng_decide (hence the same computed values), with the error
    allowances E1, E2 of the same model as Em.  y cannot block if T1 >= E1 or T2 >= E2 (then the exact T1 or
    T2 is >= 0); E = 0 occurs only for identical table entries, where the computed difference is the exact 0.
    q(x,x') := min_y max(T1/E1, T2/E2); the edge is certified iff q >= 1."""
    sig, z, w, cid, Esig, Ez, Ew = wit
    ne = len(ei)
    q, yq = np.empty(ne), np.empty(ne, dtype=np.intp)
    det = np.empty((ne, 4))
    reproduces_m = True
    for s0 in range(0, ne, batch):
        X, Xp = ei[s0:s0 + batch], ej[s0:s0 + batch]
        rows = np.arange(len(X))
        sxx = sig[X, Xp][:, None]
        with np.errstate(invalid="ignore"):
            T1 = sig[X] - sxx                                    # sig_xy - sig_xx'
            T2 = sig[Xp] - sxx                                   # sig_x'y - sig_xx'
        Exx = Esig[X, Xp][:, None]
        if cid is not None:
            cxx = cid[X, Xp][:, None]
            E1 = np.where(cid[X] == cxx, 0.0, Esig[X] + Exx)
            E2 = np.where(cid[Xp] == cxx, 0.0, Esig[Xp] + Exx)
        else:
            E1, E2 = Esig[X] + Exx, Esig[Xp] + Exx
        if z is not None:
            T1 += (w[None, :] + z[X]) - (w[Xp] + z[X, Xp])[:, None]
            T2 += (z[Xp] + w[None, :]) - (w[X] + z[X, Xp])[:, None]
            E1 = E1 + Ez[X] + Ez[X, Xp][:, None] + Ew[None, :] + Ew[Xp][:, None]
            E2 = E2 + Ez[Xp] + Ez[X, Xp][:, None] + Ew[None, :] + Ew[X][:, None]
        T1[rows, X] = T1[rows, Xp] = np.inf                     # y = x, x' excluded
        T2[rows, X] = T2[rows, Xp] = np.inf
        reproduces_m &= bool(np.array_equal(np.min(np.maximum(T1, T2), axis=1), m[X, Xp]))
        with np.errstate(divide="ignore", invalid="ignore"):
            r1 = np.where(E1 > 0, T1 / E1, np.where(T1 >= 0, np.inf, -np.inf))
            r2 = np.where(E2 > 0, T2 / E2, np.where(T2 >= 0, np.inf, -np.inf))
        qy = np.maximum(r1, r2)
        k = np.argmin(qy, axis=1)
        q[s0:s0 + batch], yq[s0:s0 + batch] = qy[rows, k], k
        det[s0:s0 + batch] = np.stack([T1[rows, k], E1[rows, k], T2[rows, k], E2[rows, k]], axis=1)

    def rec(t):
        a, b, y = int(ei[t]), int(ej[t]), int(yq[t])
        return dict(i=a, j=b, y=y, ci=[float(c1[a]), float(c2[a])], cj=[float(c1[b]), float(c2[b])],
                    cy=[float(c1[y]), float(c2[y])], q=float(q[t]), T1=float(det[t, 0]), E1=float(det[t, 1]),
                    T2=float(det[t, 2]), E2=float(det[t, 3]))
    t0 = int(np.argmin(q)) if ne else None
    bad = np.nonzero(q < 1)[0]
    low = np.nonzero(q < 100)[0]
    return dict(n_edges=ne, n_edges_certified=int(np.count_nonzero(q >= 1)),
                n_edges_q_below_100=int(low.size), min_q=(rec(t0) if ne else None),
                n_edges_q_infinite=int(np.count_nonzero(np.isinf(q))),
                uncertified_edges=[rec(t) for t in bad[:limit]],
                edges_q_below_100=[rec(t) for t in low[:limit]],
                recomputed_T_reproduce_m=reproduces_m)


def graph_summary(m, Em, c1, c2, limit=40, wit=None):
    n = m.shape[0]
    A = m >= 0                                       # NaN diagonal -> False
    iu = np.triu_indices(n, 1)
    Au = A[iu]
    ei, ej = iu[0][Au], iu[1][Au]
    deg = np.bincount(np.concatenate([ei, ej]), minlength=n)
    tie = m == 0
    nz = (~np.eye(n, dtype=bool)) & ~tie
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = np.where(nz, np.abs(m) / Em, np.inf)
    k = int(np.argmin(ratio))
    i, j = divmod(k, n)
    fl = ((ratio < 100) | (ratio.T < 100))[iu]
    fi, fj = iu[0][fl], iu[1][fl]
    flagged = [dict(i=int(a), j=int(b), ci=[float(c1[a]), float(c2[a])], cj=[float(c1[b]), float(c2[b])],
                    m=float(m[a, b]), Em=float(Em[a, b]), ratio=float(ratio[a, b]))
               for a, b in zip(fi[:limit], fj[:limit])]
    summ = dict(n_places=n, n_edges=int(ei.size), mean_degree=2.0 * ei.size / n, max_degree=int(deg.max()),
                asymmetric_decisions=int(np.count_nonzero(A != A.T)),
                tie_pairs=int(np.count_nonzero((tie | tie.T)[iu])),
                smallest_margin=dict(pair=[i, j], m=float(m[i, j]), Em=float(Em[i, j]),
                                     ratio_margin_over_error=float(ratio[i, j])),
                pairs_ratio_below_100=int(fl.sum()), flagged_pairs=flagged)
    # v2: smallest nonzero absolute margin, separately from the smallest margin/error ratio above
    with np.errstate(invalid="ignore"):
        absm = np.where(nz, np.abs(m), np.inf)
    ka = int(np.argmin(absm))
    ia, ja = divmod(ka, n)
    summ["smallest_abs_margin"] = dict(pair=[ia, ja], ci=[float(c1[ia]), float(c2[ia])],
                                       cj=[float(c1[ja]), float(c2[ja])], m=float(m[ia, ja]),
                                       Em=float(Em[ia, ja]), ratio_margin_over_error=float(ratio[ia, ja]),
                                       is_edge=bool(A[ia, ja]))
    # v2: non-edges are certified by the minimizing witness iff |m| >= Em there (both T1, T2 < 0 exactly)
    nonedge = (~A & ~np.eye(n, dtype=bool))[iu]
    cert = ((ratio >= 1) | (ratio.T >= 1))[iu]
    summ["n_nonedges"] = int(nonedge.sum())
    summ["n_nonedges_certified_by_minimizing_witness"] = int(np.count_nonzero(nonedge & cert))
    if wit is not None:
        summ["edge_check"] = edge_check(m, ei, ej, wit, c1, c2)
    return summ, ei, ej, deg


def part_audit(graphs):
    """v2: per-part minima over the graphs (label -> graph summary) of the margins and certification counts."""
    lab_a = min(graphs, key=lambda g: abs(graphs[g]["smallest_abs_margin"]["m"]))
    lab_r = min(graphs, key=lambda g: graphs[g]["smallest_margin"]["ratio_margin_over_error"])
    withq = {g: s for g, s in graphs.items() if s.get("edge_check") and s["edge_check"]["min_q"]}
    lab_q = min(withq, key=lambda g: withq[g]["edge_check"]["min_q"]["q"]) if withq else None
    return dict(n_graphs=len(graphs),
                smallest_abs_margin=dict(graph=lab_a, **graphs[lab_a]["smallest_abs_margin"]),
                smallest_ratio=dict(graph=lab_r, **graphs[lab_r]["smallest_margin"]),
                smallest_edge_q=(dict(graph=lab_q, **withq[lab_q]["edge_check"]["min_q"]) if lab_q else None),
                total_edges=sum(s["n_edges"] for s in graphs.values()),
                total_edges_certified=sum(s["edge_check"]["n_edges_certified"] for s in withq.values()),
                total_edges_q_below_100=sum(s["edge_check"]["n_edges_q_below_100"] for s in withq.values()),
                total_nonedges=sum(s["n_nonedges"] for s in graphs.values()),
                total_nonedges_certified=sum(s["n_nonedges_certified_by_minimizing_witness"]
                                             for s in graphs.values()),
                all_recomputed_T_reproduce_m=all(s["edge_check"]["recomputed_T_reproduce_m"]
                                                 for s in withq.values()))


def chain(n, ei, ej, wt):
    G = csr_matrix((wt, (ei, ej)), shape=(n, n))
    ncomp = int(connected_components(G, directed=False)[0])
    return dijkstra(G, directed=False), ncomp


def window_rho(ell, r2, phi, lo, hi):
    """Mean rho = ell/r over unordered pairs with lo <= r <= hi, and in four phi bins of width pi/16."""
    iu = np.triu_indices(ell.shape[0], 1)
    R2 = r2[iu]
    sel = (R2 >= lo * lo) & (R2 <= hi * hi)
    rho = ell[iu][sel] / np.sqrt(R2[sel])
    kb = np.minimum((phi[iu][sel] / (np.pi / 16)).astype(int), 3)
    bins = [float(rho[kb == q].mean()) for q in range(4)]
    return dict(r_window=[lo, hi], n_pairs=int(sel.sum()), mean_rho=float(rho.mean()),
                bin_means=bins, bin_counts=[int(np.sum(kb == q)) for q in range(4)],
                B=bins[3] / bins[0], n_infinite=int(np.sum(~np.isfinite(rho))))


def equal_norm_case(L, c1, c2, S, D2, lo, hi):
    """Places on grid points (equal norms): d0^2 = 2 S0 - 2 S, i.e. sig = -2 S and no small parts."""
    n = len(c1)
    a, b = canon(c1, c2, L)
    Sp = S[a, b]
    wit = (-2.0 * Sp, None, np.zeros(n), a * (L // 2 + 1) + b, 8 * UR * Sp, None, None)
    m, ys, Em = rng_decide(*wit)
    summ, ei, ej, deg = graph_summary(m, Em, c1, c2, wit=wit)
    ell, ncomp = chain(n, ei, ej, np.sqrt(D2[a[ei, ej], b[ei, ej]]))
    summ["components"] = ncomp
    r2 = (a * a + b * b).astype(float)
    win = window_rho(ell, r2, np.arctan2(b, a), lo, hi)
    return summ, win, dict(m=m, a=a, b=b, ell=ell, ei=ei, ej=ej, deg=deg)


# ---------------------------------------------------------------- parts
def part_T1():
    L = 32
    K, Kd = kernel(L, "sep")
    S, D2 = tables(K)
    c1, c2 = np.divmod(np.arange(L * L), L)
    summ, win, d = equal_norm_case(L, c1, c2, S, D2, 8, 14)
    A = d["m"] >= 0
    grid4 = bool(np.array_equal(A, (d["a"] == 1) & (d["b"] == 0)))
    rho = math.sqrt(D2[1, 0])
    dev = float(np.max(np.abs(d["ell"] - rho * (d["a"] + d["b"]))))
    tol = 1e-9 * rho * L
    return dict(L=L, kernel="separable", table_checks=table_checks(S, D2, Kd), graph=summ,
                N0_is_4_neighbour_grid=grid4, rho_unit_step=rho, max_abs_dev_ell0_minus_rho_l1=dev,
                tolerance=tol, decision="pass" if (grid4 and dev <= tol) else "fail")


def part_T1b():
    L = 32
    K, Kd = kernel(L, "iso")
    S, D2 = tables(K)
    c1, c2 = np.divmod(np.arange(L * L), L)
    summ, win, d = equal_norm_case(L, c1, c2, S, D2, 8, 14)
    offs = {}
    for p, q in zip(d["a"][d["ei"], d["ej"]], d["b"][d["ei"], d["ej"]]):
        offs[f"({p},{q})"] = offs.get(f"({p},{q})", 0) + 1
    return dict(L=L, kernel="isotropic", table_checks=table_checks(S, D2, Kd), graph=summ,
                edge_offset_classes_canonical=offs, rho_unit_step=math.sqrt(D2[1, 0]),
                window=win, B_per=win["B"])


def part_T2():
    res = dict(sizes={})
    for L, seeds in ((64, range(2301, 2306)), (128, range(2311, 2316))):
        K, Kd = kernel(L, "iso")
        S, D2 = tables(K)
        reals = []
        for seed in seeds:
            c1, c2 = places(L, seed)
            summ, win, _ = equal_norm_case(L, c1, c2, S, D2, L // 8, L // 4)
            reals.append(dict(seed=seed, graph=summ, window=win))
        Bs = np.array([r["window"]["B"] for r in reals])
        res["sizes"][str(L)] = dict(table_checks=table_checks(S, D2, Kd), realizations=reals,
                                    B_values=Bs.tolist(), B_mean=float(Bs.mean()),
                                    SE=float(Bs.std(ddof=1) / math.sqrt(len(Bs))))
    s = res["sizes"]["128"]
    dev, se = s["B_mean"] - 1.0, s["SE"]
    if abs(dev) < 0.02 and abs(dev) < 2 * se:
        dec = "isotropy supported"
    elif dev > 0.02 and dev > 3 * se:
        dec = "anisotropy detected"
    else:
        dec = "inconclusive"
    res["decision_L128"] = dec
    res["margin_audit"] = part_audit({f"L{L}_seed{r['seed']}": r["graph"] for L in (64, 128)
                                      for r in res["sizes"][str(L)]["realizations"]})
    return res


def part_T3():
    L, N = 128, 128 * 128
    K, Kd = kernel(L, "iso")
    S, D2 = tables(K)
    c1, c2 = places(L, 2311)
    n = len(c1)
    a, b = canon(c1, c2, L)
    Sp, D2p, r2, cid = S[a, b], D2[a, b], a * a + b * b, a * (L // 2 + 1) + b
    phi = np.arctan2(b, a)
    U = np.empty((n, N))
    for h in range(n):
        U[h] = np.roll(K, (c1[h], c2[h]), axis=(0, 1)).ravel()     # u_h[l] = kappa(l - c_h)
    G = np.random.default_rng(2321).standard_normal((n, N))
    G /= np.linalg.norm(G, axis=1)[:, None]
    nrm = np.array([math.fsum((g * g).tolist()) for g in G])
    B = U @ G.T                                   # B[h,h'] = <u_h, g_h'>
    Babs = U @ np.abs(G).T                        # sum of |terms| of each B entry
    GG = G @ G.T
    samp = [(h, (7 * h + 3) % n) for h in range(0, n, 5)]
    errB = max(abs(math.fsum((U[h] * G[k]).tolist()) - B[h, k]) / (math.sqrt(N) * UR * Babs[h, k])
               for h, k in samp)
    errG = max(abs(math.fsum((G[h] * G[k]).tolist()) - GG[h, k]) / (math.sqrt(N) * UR) for h, k in samp)
    del U, G
    av, Bs, Gs = np.diag(B).copy(), B + B.T, 0.5 * (GG + GG.T)
    Eb = math.sqrt(N) * UR * Babs
    Ebs, eG = Eb + Eb.T, math.sqrt(N) * UR
    del B, GG, Babs
    rows, base_edges, base_rho = [], None, None
    for eps in EPS_LIST:
        t0 = time.perf_counter()
        # d0^2 = [2 S0 + 2 eps^2] + (-2 S) + (w_h + w_h' + z_hh'): constant, overlap part, small parts
        w = 2 * eps * av + eps ** 2 * (nrm - 1)
        z = -2 * eps * Bs - 2 * eps ** 2 * Gs
        Ew = 2 * eps * np.diag(Eb) + eps ** 2 * eG + 4 * UR * np.abs(w)
        Ez = 2 * eps * Ebs + 2 * eps ** 2 * eG + 4 * UR * np.abs(z)
        if eps == 0:
            wit = (-2.0 * Sp, None, np.zeros(n), cid, 8 * UR * Sp, None, None)
        else:
            wit = (-2.0 * Sp, z, w, cid, 8 * UR * Sp, Ez, Ew)
        m, ys, Em = rng_decide(*wit)
        summ, ei, ej, deg = graph_summary(m, Em, c1, c2, wit=wit)
        del z, Ez, wit
        d2e = (D2p[ei, ej] + 2 * eps * (av[ei] + av[ej] - Bs[ei, ej])
               + eps ** 2 * (nrm[ei] + nrm[ej] - 2 * Gs[ei, ej]))
        ell, ncomp = chain(n, ei, ej, np.sqrt(d2e))
        win = window_rho(ell, r2.astype(float), phi, 16, 32)
        edges = set(zip(ei.tolist(), ej.tolist()))
        if eps == 0:
            base_edges, base_rho = edges, win["mean_rho"]
            tz = (m == 0) | (m == 0).T
            tie_set = set(zip(*[q.tolist() for q in np.nonzero(np.triu(tz, 1))]))
        if eps == 1e-12:
            gen_edges = edges
        long_mask = r2[ei, ej] > LONG_R2
        row = dict(eps=eps, a_new_edges=len(edges - base_edges), removed_edges=len(base_edges - edges),
                   removed_edges_that_are_eps0_tie_pairs=len((base_edges - edges) & tie_set),
                   sym_diff_vs_eps_1e12=(len(edges ^ gen_edges) if eps >= 1e-12 else None),
                   b_long_edges=int(long_mask.sum()), c_max_degree=int(deg.max()),
                   d_mean_rho=win["mean_rho"], d_ratio=win["mean_rho"] / base_rho,
                   components=ncomp, graph=summ, n_window_pairs=win["n_pairs"])
        if long_mask.any():
            k = int(np.argmin(np.where(long_mask, r2[ei, ej], 10 ** 9)))
            row["e_shortest_long_edge"] = dict(r=math.sqrt(r2[ei[k], ej[k]]), d0=float(np.sqrt(d2e[k])),
                                               ci=[int(c1[ei[k]]), int(c2[ei[k]])],
                                               cj=[int(c1[ej[k]]), int(c2[ej[k]])])
            row["long_edge_r_values"] = sorted(np.sqrt(r2[ei, ej][long_mask]).round(4).tolist())[:200]
        else:
            row["e_shortest_long_edge"] = None
        row["runtime_s"] = time.perf_counter() - t0
        rows.append(row)
        print(f"  T3 eps={eps:g}: new={row['a_new_edges']} long={row['b_long_edges']} "
              f"maxdeg={row['c_max_degree']} d={row['d_ratio']:.6f} ({row['runtime_s']:.1f}s)", flush=True)
    small = [r for r in rows if 0 < r["eps"] <= 1e-4]
    fragile = any(r["b_long_edges"] > 0 and abs(r["d_ratio"] - 1) > 0.05 for r in small)
    robust = all(r["b_long_edges"] == 0 and abs(r["d_ratio"] - 1) < 0.01 for r in rows if r["eps"] > 0)
    return dict(L=L, seed_places=2311, seed_noise=2321, n_places=n,
                validation=dict(max_B_err_over_estimate=errB, max_G_err_over_estimate=errG,
                                n_samples=len(samp), estimate_B="sqrt(N)*UR*sum|terms|",
                                estimate_G="sqrt(N)*UR"),
                rows=rows, decision="fragile" if fragile else ("robust" if robust else "intermediate"),
                margin_audit=part_audit({f"eps={r['eps']:g}": r["graph"] for r in rows}),
                margin_audit_eps_positive=part_audit({f"eps={r['eps']:g}": r["graph"] for r in rows
                                                      if r["eps"] > 0}))


def part_T4():
    L, N = 128, 128 * 128
    K, _ = kernel(L, "iso")
    S0 = math.fsum((K * K).ravel().tolist())
    K2neg = (-(K * K)).ravel()
    c1, c2 = places(L, 2311)
    n = len(c1)
    off = np.random.default_rng(2331).random((n, 2))
    f1, f2 = off[:, 0], off[:, 1]
    lv = np.arange(L)

    def absdisp(dint, f):           # |minimal image of dint + f| on the circle of length L
        mm = np.mod(dint, L)
        v = mm + f
        return np.abs(np.where(v > L / 2, (mm - L) + f, v))

    U = np.empty((n, N))
    for h in range(n):
        v1, v2 = absdisp(lv - c1[h], -f1[h]), absdisp(lv - c2[h], -f2[h])
        U[h] = np.exp(-np.sqrt(v1[:, None] ** 2 + v2[None, :] ** 2) / XI).ravel()
    nu = np.array([math.fsum(np.concatenate([U[h] * U[h], K2neg]).tolist()) for h in range(n)])
    S4 = U @ U.T
    S4 = np.triu(S4) + np.triu(S4, 1).T
    samp = [(h, (7 * h + 3) % n) for h in range(0, n, 5)]
    errS = max(abs(math.fsum((U[h] * U[k]).tolist()) - S4[h, k]) / (UR * S4[h, k]) for h, k in samp)
    w1 = absdisp(c1[None, :] - c1[:, None], f1[None, :] - f1[:, None])
    w2 = absdisp(c2[None, :] - c2[:, None], f2[None, :] - f2[:, None])
    r2 = w1 ** 2 + w2 ** 2
    phi = np.arctan2(np.minimum(w1, w2), np.maximum(w1, w2))
    rmax_half = math.sqrt(2) * (L / 2 + 1) / XI
    eS = (rmax_half + 3 + math.sqrt(N)) * UR
    # d0^2 = 2 S0 + (-2 S_hh') + (nu_h + nu_h'):  constant, overlap part, small (norm-deviation) parts
    Ew = np.full(n, (rmax_half + 4) * UR * S0)
    zero = np.zeros((n, n))
    wit = (-2.0 * S4, zero, nu, None, 2 * (eS + 4 * UR) * S4, zero, Ew)
    m, ys, Em = rng_decide(*wit)
    summ, ei, ej, deg = graph_summary(m, Em, c1 + f1, c2 + f2, wit=wit)
    del wit
    d2e = np.array([math.fsum(((U[i] - U[j]) ** 2).tolist()) for i, j in zip(ei, ej)])
    del U
    ell, ncomp = chain(n, ei, ej, np.sqrt(d2e))
    win = window_rho(ell, r2, phi, 16, 32)
    ref, ref1 = json.loads((OUT / "T3.json").read_text())["rows"][:2]
    assert ref["eps"] == 0.0 and ref1["eps"] == 1e-12
    long_mask = r2[ei, ej] > LONG_R2
    return dict(L=L, seed_places=2311, seed_offsets=2331, n_places=n,
                norms=dict(S0_unshifted=S0, min=S0 + float(nu.min()), max=S0 + float(nu.max()),
                           spread=float(nu.max() - nu.min())),
                validation=dict(max_S_rel_err_in_UR_blas_vs_fsum=errS, assumed_rel_err_in_UR=eS / UR),
                graph=summ, components=ncomp,
                b_long_edges=int(long_mask.sum()), c_max_degree=int(deg.max()),
                d_mean_rho=win["mean_rho"], d_ratio_to_T3_eps0=win["mean_rho"] / ref["d_mean_rho"],
                ratio_to_T3_eps_1e12=win["mean_rho"] / ref1["d_mean_rho"],
                T3_eps0_mean_rho=ref["d_mean_rho"], n_window_pairs=win["n_pairs"],
                long_edge_r_quantiles=(np.quantile(np.sqrt(r2[ei, ej][long_mask]), [0, .25, .5, .75, 1]).tolist()
                                       if long_mask.any() else None))


PARTS = dict(T1=part_T1, T1b=part_T1b, T2=part_T2, T3=part_T3, T4=part_T4)

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name in (sys.argv[1:] or list(PARTS)):
        t0 = time.perf_counter()
        print(f"running {name}", flush=True)
        res = PARTS[name]()
        res["part"], res["runtime_s"] = name, time.perf_counter() - t0
        (OUT / f"{name}.json").write_text(json.dumps(res, indent=1, default=float))
        print(f"{name} done in {res['runtime_s']:.1f} s", flush=True)
