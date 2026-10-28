"""Check (item 1): exact diagonalization of exchange cells with a push.

C = J sum_<xy> S_x.S_y - h_p S^3_h  (J = 1, n = e_3), spin S = 1/2 and S = 1.
Clusters: rings of even size L (S=1/2: 8,12,16,20; S=1: 6,8,10,12) and the
16-object periodic cubic cluster Z^3 / Lambda, Lambda spanned by (2,2,0),(2,0,2),(0,2,2).
C commutes with M = sum_x S^3_x.  The two lowest eigenvalues are computed in EVERY sector
M = -NS, ..., NS, at h_p = 0 and at the sampled push strengths HPS.  In each sector the lowest
eigenvalue is simple (Perron-Frobenius after the Marshall sign change; the push is diagonal),
so the lowest eigenvector of C is unique iff the lowest sector value lies strictly below the
lowest values of all other sectors and below the second value of its own sector.
Output: output/ed_push.txt
"""
from pathlib import Path
from collections import deque
import itertools
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
HPS = [0.01, 0.1, 0.3, 1.0, 3.0, 10.0]


def ring(L):
    links = [(i, (i + 1) % L) for i in range(L)]
    eps = np.array([(-1) ** i for i in range(L)])
    return links, eps


def cubic16():
    A = np.array([[2, 2, 0], [2, 0, 2], [0, 2, 2]]).T  # columns are the periods
    Ainv = np.linalg.inv(A)

    def same(u, v):
        c = Ainv @ (np.array(u) - np.array(v))
        return np.allclose(c, np.round(c))

    reps = []
    for p in itertools.product(range(4), repeat=3):
        if not any(same(p, q) for q in reps):
            reps.append(p)
    assert len(reps) == 16

    def idx(p):
        return [k for k, q in enumerate(reps) if same(p, q)][0]

    links = set()
    for k, p in enumerate(reps):
        nb = set()
        for d in np.eye(3, dtype=int):
            for s in (1, -1):
                j = idx(tuple(np.array(p) + s * d))
                nb.add(j)
                links.add(tuple(sorted((k, j))))
        assert len(nb) == 6
    links = sorted(links)
    assert len(links) == 48
    eps = np.array([(-1) ** (sum(p) % 2) for p in reps])
    for a, b in links:
        assert eps[a] != eps[b]
    return links, eps, reps


def distances(links, n, h=0):
    adj = [[] for _ in range(n)]
    for a, b in links:
        adj[a].append(b)
        adj[b].append(a)
    d = [-1] * n
    d[h] = 0
    q = deque([h])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if d[v] < 0:
                d[v] = d[u] + 1
                q.append(v)
    return np.array(d)


def sector(n, S2, M2):
    """Basis states (digit arrays, digit = m + S) with 2*sum(m) = M2; S2 = 2S."""
    d = S2 + 1
    codes = np.arange(d ** n, dtype=np.int64)
    digits = np.zeros((codes.size, n), dtype=np.int8)
    c = codes.copy()
    for i in range(n):
        digits[:, i] = c % d
        c //= d
    tot = 2 * digits.sum(axis=1).astype(np.int64) - n * S2
    keep = tot == M2
    return codes[keep], digits[keep]


def build(n, S2, M2, links, J=1.0):
    S = S2 / 2.0
    d = S2 + 1
    codes, digits = sector(n, S2, M2)
    m = digits.astype(float) - S
    diag = np.zeros(codes.size)
    rows, cols, vals = [], [], []
    for a, b in links:
        diag += J * m[:, a] * m[:, b]
        for i, j in ((a, b), (b, a)):  # S^+_i S^-_j
            ok = (digits[:, i] < S2) & (digits[:, j] > 0)
            src = np.nonzero(ok)[0]
            new = codes[src] + d ** i - d ** j
            dst = np.searchsorted(codes, new)
            amp = 0.5 * J * np.sqrt(S * (S + 1) - m[src, i] * (m[src, i] + 1)) \
                * np.sqrt(S * (S + 1) - m[src, j] * (m[src, j] - 1))
            rows.append(dst); cols.append(src); vals.append(amp)
    if rows:
        off = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                            shape=(codes.size, codes.size))
    else:
        off = sp.csr_matrix((codes.size, codes.size))
    return off, diag, m


def lowest(H, k=1):
    if H.shape[0] <= 1500:
        w, v = np.linalg.eigh(H.toarray())
        return w[:k], v[:, :k]
    w, v = eigsh(H, k=k, which="SA", tol=1e-12)
    o = np.argsort(w)
    return w[o], v[:, o]


def run(name, n, S2, links, eps, out):
    dist = distances(links, n)
    far = np.nonzero(dist == dist.max())[0]
    out.append(f"\n## {name}: N={n}, S={S2}/2, links={len(links)}, far sites {[int(f) for f in far]}"
               f" at distance {dist.max()}; sectors searched: all M = {-n * S2 / 2:g}, ..., {n * S2 / 2:g}")
    hps = [0.0] + HPS
    res = {hp: [] for hp in hps}
    for M2 in range(-n * S2, n * S2 + 1, 2):
        off, diag, m = build(n, S2, M2, links)
        for hp in hps:
            H = off + sp.diags(diag - hp * m[:, 0])
            k = 2 if H.shape[0] > 1 else 1
            w, v = lowest(H, k=k)
            e2 = w[1] if k == 2 else np.inf
            p = np.abs(v[:, 0]) ** 2
            sz = p @ m
            res[hp].append((w[0], e2, M2, float(np.mean(eps[far] * sz[far])), float(sz[0])))
    out.append("h_p/J   M_low   E_low            E_next (all sectors)   gap        unique   m(far)=eps*<S3_far>   m(h)")
    for hp in hps:
        best = min(res[hp], key=lambda t: t[0])
        nxt = min([best[1]] + [t[0] for t in res[hp] if t[2] != best[2]])
        uniq = best[0] < nxt - 1e-9
        out.append(f"{hp:6.2f}  {best[2] / 2:5.1f}  {best[0]:.10f}   {nxt:.10f}        {nxt - best[0]:.3e}  {uniq!s:6s}"
                   f"   {best[3]: .6f}            {best[4]: .6f}")
    b0 = min(res[0.0], key=lambda t: t[0])
    n0 = min([b0[1]] + [t[0] for t in res[0.0] if t[2] != b0[2]])
    out.append(f"no push: lowest eigenvector in M=0 and unique (a total-spin singlet): {b0[2] == 0 and b0[0] < n0 - 1e-9}")


def main():
    out = ["# ED check, item 1: exchange cells, J=1, push -h_p S^3_h at h=0 (class +); all sectors of M searched"]
    for L in (8, 12, 16, 20):
        links, eps = ring(L)
        run(f"ring L={L}", L, 1, links, eps, out)
    links, eps, reps = cubic16()
    out.append("\n16-object cubic cluster sites (representatives mod Lambda): " + str(reps))
    out.append("links: each site x to x+e_i, i=1,2,3 (mod Lambda); 48 links, 6 distinct neighbours each")
    run("cubic cluster 16", 16, 1, links, eps, out)
    for L in (6, 8, 10, 12):
        links, eps = ring(L)
        run(f"ring L={L}", L, 2, links, eps, out)
    (OUT / "ed_push.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
