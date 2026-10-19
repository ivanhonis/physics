# Review: 03-held-sources v3

- **Subproject:** 06-ilang-source
- **Package:** 03-held-sources
- **Reviewed version:** v3
- **Date:** 2026-10-19

---
VERDICT: minor issues

## Issues

### I1. "A vector of the level does not select a branch" is stated for every vector
- **Location:** Step 3, item 1
- **Severity:** minor
- **Problem:** The sentence says that a vector $`\varphi_n`$ of a degenerate level does not select one of its $`d_\ell`$ branches. In the commuting case $`[A_1,A_2]=0`$ (the control of item 2), a joint eigenvector of $`A_1`$, $`A_2`$ in the level continues to one analytic branch, and so does a vector that a conserved symmetry of $`C_f`$ and the $`\Phi_x`$ assigns to one sector. The statement holds for a general vector of the level, not for every vector.
- **Fix:** State it with its condition: which vectors of the level select a branch (for example joint eigenvectors of the compressions in the commuting case, or vectors fixed by a conserved symmetry), and that a general vector does not. Adjust the Result entry (3.10)–(3.12) and the twin if they repeat the sentence.
