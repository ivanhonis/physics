# Review: 08-tilt v1

- **Subproject:** 08-ilang-propagation
- **Package:** 08-tilt
- **Reviewed version:** v1
- **Date:** 2026-10-26

---
VERDICT: minor issues

## Issues

### I1. The finite-size statement of the R2 check is false for perpendicular links
- **Location:** Step 11, last paragraph ("changing by at most 0.015 from L = 64 to 128").
- **Severity:** minor
- **Problem:** In `code/v1/output/spinwave_mutual.txt` the perpendicular-link ratio changes from 1.049 to 1.072 at r = 10 and from 1.001 to 1.046 at r = 12, and its L = 32 values oscillate between 0.66 and 1.21. Only the parallel links change by at most 0.014.
- **Fix:** State the change from L = 64 to 128 for each geometry as the output gives it, and say what the perpendicular values at r ≥ 10 do and do not confirm.

### I2. The lattice check of the R1 law for r ≫ ℓ_b is quoted at a size that has not converged
- **Location:** Step 12, last paragraph of (ii).
- **Severity:** minor
- **Problem:** The quoted L = 128 ratios (1.011 to 0.986 at r = 6 to 11) still move by up to 0.14 from L = 64; at r = 10, for example, the ratio goes from 0.841 to 0.978. The same output gives Aitken values of 1.02 to 1.07 at r = 6 to 11 and 1.10 at r = 12. Neither the drift nor the extrapolated values are reported, so the sentence reads as a confirmation of the coefficient within a few per cent.
- **Fix:** Report the finite-size behaviour and the extrapolated values, with the range of r in which the extrapolation is meaningful (as Step 10 does for the along-n sources), and state what the check confirms.

### I3. The Result drops the mixed cell factor
- **Location:** Result, (8.14), and (8.16), which uses its $`c_{\rm cell}`$.
- **Severity:** minor
- **Problem:** The Result gives $`c_{\rm cell}=1`$ (single objects) or 4 (cells). Step 8 and the twin define $`c_{\rm cell}=c_1c_2`$ with $`c_i=1`$ or 2, so a single object and a cell give 2.
- **Fix:** State $`c_{\rm cell}=c_1c_2`$ in the Result.

### I4. The Result does not carry Assumption E or the basis of the R1 remainder
- **Location:** Result, preamble and (8.5)–(8.19); display (8.18), first line.
- **Severity:** minor
- **Problem:** Every result at an order in $`1/S`$ rests on Assumption E: the lowest eigenvector of the truncated expansion is taken to give the quantities of the true lowest eigenvector asymptotically, while $`\langle n_x\rangle\ll S`$. The Result and the twin state these results without it, so (8.7), for example, reads as a statement about the true $`m(x)`$. In addition, the remainder $`O(r/\ell_b)`$ of the first line of (8.18) comes from the vertex factor $`\nu^2/(\nu^2+g'^2S^2)`$, which Step 12 introduces without derivation. The display states it as a derived order.
- **Fix:** Say in the Result and in the twin which results rest on Assumption E. In (8.18), either derive the remainder or mark it, in the display and in the Result, as resting on that step.
