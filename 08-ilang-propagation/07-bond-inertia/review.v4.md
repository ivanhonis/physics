# Review: 07-bond-inertia v4

- **Subproject:** 08-ilang-propagation
- **Package:** 07-bond-inertia
- **Reviewed version:** v4
- **Date:** 2026-10-25

---
VERDICT: minor issues

## Issues

### I1. The Result places every tuned mixed level in (I)
- **Location:** Result (7.12), bullet "(N$`_l`$) with $`r\ell`$ not large".
- **Severity:** minor
- **Problem:** The bullet ends the mixed-branch exception with "(such levels lie in (I))". Step 8 states only that the example lies in (I). In this part of (N), tuned mixed levels with $`\lambda_{C,1}\lambda_{C,2}=4/(1-r^2)`$ also occur outside (I). One case is $`r\ell`$ between $`\frac12`$ and $`1`$, where (I) is empty but (N$`_l`$) allows $`\lambda_{C,1}\lambda_{C,2}=4/(1-r^2)>4r^2\ell^2`$. These levels have formal coefficients.
- **Fix:** Say that such levels occur in (I), as in Step 8, and not that they all lie there.
