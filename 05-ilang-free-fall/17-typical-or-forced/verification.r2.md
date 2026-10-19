# External verification: 17-typical-or-forced

- **Subproject:** 05-ilang-free-fall
- **Package:** 17-typical-or-forced
- **Verified version:** v2
- **External round:** 2 of 3
- **Date:** 2026-10-18T15:29:59+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The level-by-level algebra, the exact and leading-order velocity classifications, and the codimension calculations are substantially correct. The relisting arguments also correctly distinguish the listed-term requirements R1 and R2 from requirements constructed from the total contract. The remaining issues concern identifying the frozen-clock rate with the requested rate definition, explicitly classifying branch-equal motion, and qualifying the stability conclusion.

## Issues

### I1. Identification of the frozen rate needs clarification
- **Location:** Step 3; Step 4, Eqs. (17.6)–(17.7)
- **Severity:** minor
- **Problem:** The commuting-factor calculation correctly determines the rate of the frozen contract. However, the quoted definition (3.23) is a limit of rates obtained from clock readings; the supplied quotation does not explicitly identify it with freezing before taking the wide-start limit. Thus the assertion “As in (3.23)” is not established by the available input. This matters because the resulting neighboring-place rate ratio is subsequently used at first order in the gradients to classify $`\mathcal U_5`$. The stated spatial hierarchy alone does not establish the accuracy of that ratio for the inhomogeneous evolution. Since the question requests the zeroth-gradient, wide-start form, this may be an intended order-of-limits convention rather than an incorrect result, but that identification needs to be made explicit.
- **Suggested fix:** Establish that the frozen prescription realizes the requested definition at the relevant order, or supply the missing input specifying this order of limits. For the first-order classification, it is sufficient to control the error in the neighboring-place rate ratio to $`o(\|\hat{\boldsymbol g}\|)`$; a full finite-width error estimate is not necessarily required.

### I2. Branch-equal motion is not separately classified at leading order
- **Location:** Step 2, Eq. (17.5); Result, Eqs. (17.4)–(17.5)
- **Severity:** minor
- **Problem:** Step 1 distinguishes level independence on each branch, $`\mathcal U_4^\pm`$, from a common acceleration on both branches, $`\mathcal U_4^=`$. Step 2 gives only the former interpretation in its leading-order “both branches” classification. If “both” is intended in the branch-equal sense appearing in quoted (4.19), the stated dimension-three set is too large: on $`\mathcal U_4^\pm`$, $`a_+-a_-=2\tau^2\mathcal F_1`$. The leading-order velocity coefficients also differ by $`-3\mathcal F_1`$.
- **Suggested fix:** Explicitly add the branch-equal leading-order set
  ```math
  \{g_m=g_\eta,\ \mathcal F=\mathcal F_1=0\},
  ```
  of dimension two and codimension three. Clarify that the dimension-three set in (17.5) gives level independence separately on both branches, without equality between their responses. The exact branch-equal classification remains the stated dimension-one set.

### I3. The closing stability statement is too broad
- **Location:** Step 5; Step 7; Result, Eq. (17.12)
- **Severity:** minor
- **Problem:** Equation (17.8) establishes exact linear scaling of the two requested upper-branch defects with distance from $`\mathcal U_4^+`$. For distance from $`\mathcal U_4^\pm`$, only an upper bound is established, and both upper-branch defects can vanish at positive distance. For example,
  ```math
  g_m=\gamma+\epsilon,\quad g_\eta=\gamma,\quad
  \mathcal F=m\epsilon,\quad \mathcal F_1=0
  ```
  has $`\ell_+=0`$, $`\ell_-=-2\epsilon`$, and therefore distance $`|\epsilon|`$ from $`\mathcal U_4^\pm`$, while its upper-branch level splitting and rate–fall defect both vanish. Consequently, the unqualified closing statement that the sets are “broken linearly in the distance” does not follow for these observables and every classified set.
- **Suggested fix:** Restrict the exact linear-scaling claim to distance from $`\mathcal U_4^+`$. For distance from the simultaneous-branch set, retain the stated $`O(\delta_\pm)`$ bounds and explain that a two-sided estimate requires measuring violations on both branches. Distinguish these results from stability of the velocity-order classifications.

## Focus points

None given.
