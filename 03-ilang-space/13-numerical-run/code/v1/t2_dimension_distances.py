"""T2 (computation): (a) affine rank of {u_h}, tests (7.7), (7.11); (b) d_0^2 statistics, tests (7.6), (7.10)."""
import numpy as np

from common import gue, goe, save


def u_vec(K):
    chi = np.zeros(K.shape[0], complex); chi[0] = 1.0  # e_1 = |chi>
    return K @ chi - (chi.conj() @ K @ chi) * chi


def affine_rank(us):
    D = us[1:] - us[0]                            # u_h - u_{h_1}
    R = np.hstack([D.real, D.imag])               # real coordinates
    sv = np.linalg.svd(R, compute_uv=False)
    return int(np.sum(sv > 1e-9 * sv[0])), sv.tolist()


# (a) ranks
rank_rows, all_ok = [], True
for dc in [2, 3, 5, 9]:
    for n in [3, 6, 12, 20]:
        for ens, base, draw, quoted in [("GUE", 1302, gue, min(n - 1, 2 * (dc - 1))),
                                        ("GOE", 1402, goe, min(n - 1, dc - 1))]:
            seed = base + 100 * dc + n
            rng = np.random.default_rng(seed)
            us = np.array([u_vec(draw(rng, dc).astype(complex)) for _ in range(n)])
            r, sv = affine_rank(us)
            ok = r == quoted
            all_ok &= ok
            sva = np.array(sv) / sv[0]
            rank_rows.append({"ensemble": ens, "d_c": dc, "n": n, "seed": seed, "rank": r,
                              "quoted": quoted, "equal": ok, "singular_values": sv,
                              "diag_min_kept_ratio": float(sva[:r].min()),
                              "diag_max_dropped_ratio": float(sva[r:].max()) if r < len(sva) else None})
            print(f"{ens} d_c={dc} n={n:2d} seed={seed} rank={r} quoted={quoted} {'ok' if ok else 'MISMATCH'}")
dec_a = "pass" if all_ok else "fail"
print("T2(a):", dec_a)

# (b) distances, d_c = 9, 4000 pairs
dc, npairs = 9, 4000
stats, ok_b = {}, True
for ens, seed, draw, q_rel in [("GUE", 1303, gue, 1 / np.sqrt(dc - 1)), ("GOE", 1304, goe, np.sqrt(2 / (dc - 1)))]:
    rng = np.random.default_rng(seed)
    d2 = np.empty(npairs)
    for t in range(npairs):
        uh = u_vec(draw(rng, dc).astype(complex))
        uk = u_vec(draw(rng, dc).astype(complex))
        d2[t] = np.linalg.norm(uh - uk) ** 2
    mean, rel = float(d2.mean()), float(d2.std(ddof=1) / d2.mean())
    q_mean = 2 * (dc - 1)
    dev_mean, dev_rel = abs(mean - q_mean) / q_mean, abs(rel - q_rel) / q_rel
    ok = bool(dev_mean <= 0.03 and dev_rel <= 0.10)
    ok_b &= ok
    stats[ens] = {"seed": seed, "sample_mean": mean, "quoted_mean": q_mean, "rel_dev_mean": dev_mean,
                  "sample_rel_std": rel, "quoted_rel_std": float(q_rel), "rel_dev_rel_std": dev_rel,
                  "within": ok, "d0_squared": d2.tolist()}
    print(f"{ens}: mean={mean:.5f} (quoted {q_mean}, dev {dev_mean:.4%}), rel std={rel:.5f} "
          f"(quoted {q_rel:.5f}, dev {dev_rel:.4%})")
dec_b = "pass" if ok_b else "fail"
print("T2(b):", dec_b)

save("t2_dimension_distances.json", {
    "part": "T2", "a_ranks": rank_rows, "a_rule": "pass iff every rank equals (7.7) resp. (7.11)",
    "a_decision": dec_a,
    "a_diag_global_min_kept_ratio": min(r["diag_min_kept_ratio"] for r in rank_rows),
    "a_diag_global_max_dropped_ratio": max(r["diag_max_dropped_ratio"] for r in rank_rows
                                           if r["diag_max_dropped_ratio"] is not None),
    "b_stats": stats, "b_sample_std": "ddof=1",
    "b_rule": "pass iff, for both ensembles, |mean-quoted|/quoted <= 3% and |relstd-quoted|/quoted <= 10%",
    "b_decision": dec_b})
