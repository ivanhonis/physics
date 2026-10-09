# External verification: 20-cost-and-mass

- **Subproject:** 03-ilang-space
- **Package:** 20-cost-and-mass
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-09T06:47:26+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The cost decomposition, regional cost rate, acceleration formula, and initial inverse-inertia tensor are algebraically consistent and answer the requested items. The chain calculations and comparisons with the supplied motion formulas are also correct. The only issue is an insufficient justification of convergence on the infinite chain; for the stipulated finite-support starts, this can be repaired without changing the results.

## Issues

### I1. Normalization does not justify all infinite-chain sums
- **Location:** Setup and assumptions, final bullet; Step 6, infinite-chain calculations.
- **Severity:** minor
- **Problem:** The assertion that “all sums over $`m`$ converge absolutely” follows from normalization and the bounded-operator estimate is too strong. That estimate controls overlaps at a fixed index separation, but not sums containing factors of $`m`$, such as the mean position and the site-cost sum involving $`K_{h_m}=mX`$. A normalized distribution proportional to $`m^{-2}`$ for $`m\ge1`$, for example, has a divergent first moment. The finite-support initial states used here avoid this problem, but their required moment bounds under evolution are not established by the stated argument. Likewise, “for every state” in the chain acceleration discussion should not include states whose position expectation is undefined.
- **Suggested fix:** Explicitly restrict the infinite-chain statements to the stipulated finite-support starts, or to a suitable finite-moment domain, and supply the missing bound. The quoted identity (17.17), for example, gives
  ```math
  \|M U_\xi(\lambda)\phi\|
  \le \|M\phi\|+2t\lambda,
  ```
  including the $`\xi=0`$ limit. Together with the finite spectral mixture, this controls the position and site-cost sums. Use Cauchy–Schwarz separately for the fixed-separation overlap sums and telescoping operations.

## Focus points

None given.
