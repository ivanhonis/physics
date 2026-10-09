"""Shared helpers for T1-T5 of 13-numerical-run (ensembles, view, W, alpha, points, N_V, ell)."""
import json
from pathlib import Path

import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
SAME_POINT_TOL = 1e-12  # places with 1 - W < 1e-12 are the same point


def gue(rng, d, s=1.0):
    """GUE(s) of 07: off-diagonal Re/Im variance s^2/2, diagonal real variance s^2.
    Draw order: real-part matrix, then imaginary-part matrix."""
    a = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    return s * (a + a.conj().T) / 2.0


def goe(rng, d, s=1.0):
    """GOE(s) of 07: off-diagonal variance s^2, diagonal variance 2 s^2."""
    a = rng.standard_normal((d, d))
    return s * (a + a.T) / np.sqrt(2.0)


def haar_state(rng, d):
    """Haar-random unit vector: normalized complex Gaussian (real draw, then imaginary draw)."""
    z = rng.standard_normal(d) + 1j * rng.standard_normal(d)
    return z / np.linalg.norm(z)


def slope(lams, ys):
    """Least-squares slope of log|y| against log(lambda)."""
    return float(np.polyfit(np.log(np.asarray(lams, float)), np.log(np.abs(np.asarray(ys, float))), 1)[0])


def view(psis):
    """V_{hh'} = <psi_h'|psi_h> (= (1.7)); psis has rows psi_h."""
    psis = np.asarray(psis)
    return psis @ psis.conj().T


def wmat(V):
    """(2.11): W(h,h') = |V_hh'|^2 / (p_h p_h')."""
    p = np.real(np.diag(V))
    return np.abs(V) ** 2 / np.outer(p, p)


def loop_w(V, idx):
    """W(h1,...,hk) = G_{h1h2}...G_{hkh1} = V_{h1h2}...V_{hkh1}/(p_h1...p_hk)."""
    p = np.real(np.diag(V))
    w = 1.0 + 0j
    for j in range(len(idx)):
        w *= V[idx[j], idx[(j + 1) % len(idx)]] / p[idx[j]]
    return w


def alpha(W):
    """(3.5): alpha = arccos sqrt(W)."""
    return np.arccos(np.sqrt(np.clip(W, 0.0, 1.0)))


def points(W):
    """Classes of places with 1 - W < SAME_POINT_TOL (transitive closure)."""
    n = W.shape[0]
    parent = list(range(n))

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i

    for i in range(n):
        for j in range(i + 1, n):
            if 1.0 - W[i, j] < SAME_POINT_TOL:
                parent[find(j)] = find(i)
    classes = {}
    for i in range(n):
        classes.setdefault(find(i), []).append(i)
    return sorted(classes.values())


def neighbour_graph(Wp):
    """(4.3) on points: x~x' iff W(x,x')>0 and no y with max(alpha(x,y),alpha(y,x')) < alpha(x,x').
    Returns edge list, alpha matrix, and the smallest |alpha(x,x') - min_y max(...)| (diagnostic)."""
    A = alpha(Wp)
    m = Wp.shape[0]
    edges, margins = [], []
    for i in range(m):
        for j in range(i + 1, m):
            if not Wp[i, j] > 0:
                continue
            others = [y for y in range(m) if y not in (i, j)]
            best = min((max(A[i, y], A[y, j]) for y in others), default=np.inf)
            if np.isfinite(best):
                margins.append(abs(A[i, j] - best))
            if not best < A[i, j]:
                edges.append((i, j))
    return edges, A, (min(margins) if margins else None)


def path_analysis(m, edges, A):
    """Is the graph on m vertices a path graph (connected, acyclic, degrees <= 2)?
    If so: vertex order, step lengths alpha, and ell (4.6) between the two ends."""
    adj = {v: set() for v in range(m)}
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    deg = [len(adj[v]) for v in range(m)]
    seen, n_comp = set(), 0
    for s in range(m):
        if s in seen:
            continue
        n_comp += 1
        seen.add(s)
        stack = [s]
        while stack:
            v = stack.pop()
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
    connected = n_comp == 1
    acyclic = len(edges) == m - n_comp  # forest iff |E| = |V| - #components
    is_path = bool(connected and acyclic and max(deg) <= 2)
    res = {"degrees": deg, "n_components": n_comp, "connected": connected, "n_edges": len(edges),
           "acyclic": acyclic, "max_degree": max(deg), "is_path": is_path}
    if is_path:
        ends = [v for v in range(m) if deg[v] <= 1]
        order, prev = [ends[0]], None
        while len(order) < m:
            nxt = [w for w in adj[order[-1]] if w != prev][0]
            prev = order[-1]
            order.append(nxt)
        steps = [float(A[order[k], order[k + 1]]) for k in range(m - 1)]
        # ell by Floyd-Warshall on N_V with alpha weights
        D = np.full((m, m), np.inf)
        np.fill_diagonal(D, 0.0)
        for i, j in edges:
            D[i, j] = D[j, i] = A[i, j]
        for k in range(m):
            D = np.minimum(D, D[:, [k]] + D[[k], :])
        res.update({"order": order, "steps_alpha": steps,
                    "ell_ends": float(D[order[0], order[-1]]),
                    "sum_steps": float(sum(steps))})
    return res


def cjson(a):
    a = np.asarray(a)
    if np.iscomplexobj(a):
        return {"re": a.real.tolist(), "im": a.imag.tolist()}
    return a.tolist()


def save(name, data):
    with open(OUT / name, "w") as f:
        json.dump(data, f, indent=1)
