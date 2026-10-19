# Review: 06-own-mark v1

- **Subproject:** 06-ilang-source
- **Package:** 06-own-mark
- **Reviewed version:** v1
- **Date:** 2026-10-19

---
VERDICT: minor issues

## Issues

### I1. The isolation condition (6.4) is dropped from the spacing and inertia results
- **Location:** Result (6.8), (6.9), (6.12), (6.13) (rest-only spacings and inertia); Step 5 (last paragraph); twin entries 6.8, 6.9, 6.12, 6.13
- **Severity:** minor
- **Problem:** (6.8), (6.10) and (6.12) rest on the second-order expansion (6.5), which is established only under (6.4). The Result states (6.10) "under (6.4)", but (6.8), (6.9), (6.12) and the second-order parts of (6.13) are stated with only the conditions $`2t_f<m`$ (c), $`4t_f\le m`$ (a) or $`2t_f<M_k`$, for every $`N_f\ge1`$. For $`N_f\ge2`$ these conditions do not imply (6.4): by Step 3 the excitation energies reach $`4t_fN_f`$, so for $`\sigma=+`$ an excitation with two or more objects can meet $`M_k+\omega_k(Q)`$ when $`2t_f<M_k\le2t_fN_f`$, and Step 3 itself gives only $`2t_fN_f<M_k`$ as sufficient. At such a coincidence the start is degenerate at $`\gamma=0`$ and the Rayleigh–Schrödinger second order of (6.5) is not established.
- **Fix:** State every second-order result under (6.4) (or under the sufficient condition $`2t_fN_f<M_k`$ at $`P=0`$ for $`\sigma=+`$), in the steps, the Result and the twin.
