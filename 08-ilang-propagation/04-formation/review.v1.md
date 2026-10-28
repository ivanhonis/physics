# Review: 04-formation v1

- **Subproject:** 08-ilang-propagation
- **Package:** 04-formation
- **Reviewed version:** v1
- **Date:** 2026-10-24

---
VERDICT: minor issues

## Issues

### I1. The conditions of the stationary-phase step are missing from the Result
- **Location:** Step 6(b), Step 7, the Result bullets (4.14) and (4.15); twin key results 4.14 and 4.15.
- **Severity:** minor
- **Problem:** (4.14) and the clause "the first change arrives with $`v_{\rm front}`$" of (4.15) rest on stationary-phase estimates and on the assumption that the set of degenerate stationary values (caustics) of $`\hat K^{1/2}`$ is finite. The Result states them for the whole class without this condition; it appears only under "Open issues".
- **Fix:** State the condition in (4.14), (4.15), the Result and the twin: the class for which the theorem is claimed is the class of $`K`$ with a finite caustic set, under the stationary-phase estimates of Step 6(b). Say for which members this is shown: the nearest-neighbour contract, with its caustics at $`w\approx2.41`$ and $`3.15`$, and the control (4.16).

### I2. The question now restricts items 2 and 3
- **Location:** Step 4 after (4.9), Step 5, the Result bullets (4.9) and (4.14), Open issues; twin.
- **Severity:** minor
- **Problem:** A dated note of the question (2026-10-24) restricts item 2, for $`B\ne A`$, to source operators with a self-response that is at most long-range. It restricts item 3 to the ring and the cubic torus. The first Open issue (sources with $`\limsup\lvert\mathbf q\rvert^4\chi_B>0`$) and "the square torus is not treated" are now out of scope, and (4.9) answers item 2 completely within the restricted class.
- **Fix:** State the answer of item 2 for $`B\ne A`$ within the restricted class as the conclusion of (4.9), keeping the general necessary condition. Mark the two cases as out of scope by the note instead of open. Nothing else changes.
