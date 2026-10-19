# External verification: 04-profile

- **Subproject:** 06-ilang-source
- **Package:** 04-profile
- **Verified version:** v3
- **External round:** 2 of 3
- **Date:** 2026-10-19T10:38:09+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The central second-order resolvent calculation, ring closed form, torus asymptotics, and pole-cleared secular equation are consistent with the stated contracts. The argument for the higher-order remainder bound is also sound, and the supplied code supports the principal quantitative claims. The remaining issues concern an incorrectly labelled error normalization, an overstatement of relative finite-size accuracy near zeros, and the unspecified decay scale in the all-order cell-field control.

## Issues

### I1. Breakdown errors use the wrong denominator
- **Location:** Step 5, final paragraph; Step 6, numerical comparison; output/exact_ring.txt
- **Severity:** minor
- **Problem:** Step 5 states that at γ = 3 the second-order form is wrong by “25–59% of the exact value.” However, the reported quantity is `rel2 = (M_exact - M2)/M2`, normalized by the second-order value, not the exact value. For example, at L = 64 and d = 16, the output gives $`M_{\rm exact}=1.88729\times10^{-5}`$ and $`M^{(2)}=4.58658\times10^{-5}`$. Their difference is approximately 59% of $`M^{(2)}`$, but 143% of $`M_{\rm exact}`$. Across the listed γ = 3 cases, the errors relative to the exact value are approximately 34–143%, rather than 25–59%.
- **Suggested fix:** Label these percentages consistently as errors relative to $`M^{(2)}`$, or recompute them using $`\lvert M_{\rm exact}\rvert`$ as the denominator. The conclusion that second order has broken down is unaffected.

### I2. Relative finite-size scaling fails near zeros
- **Location:** Step 6, continuum-scaling paragraph; Result (4.10)–(4.12)
- **Severity:** minor
- **Problem:** The assertion that $`ML^2/t_f`$ depends only on γ and d/L “up to relative $`O(L^{-2})`$” needs a restriction away from zeros of the limiting mutual cost. The individual eigenvalue expansions give an additive finite-size correction, but subtraction into the mutual cost can cancel the leading term. Such zeros already occur in the small-γ limit, where the leading coefficient is proportional to $`w-1/6`$. Near a zero, the relative correction can be larger than $`O(L^{-2})`$, or be undefined. Likewise, the displayed equality $`M=(t_f/L^2)(Y^2-2y^2)`$ omits the finite-size remainder when Y and y are the roots of the limiting equations.
- **Suggested fix:** State the scaling additively, for example
  ```math
  \frac{ML^2}{t_f}=\mathscr F(\gamma,d/L)+O(L^{-2}),
  ```
  with its parameter range specified. Claim relative $`O(L^{-2})`$ accuracy only where $`\lvert\mathscr F\rvert`$ is bounded away from zero.

### I3. The full control-field decay scale is not supplied
- **Location:** Step 7, Control field (b); Eq. (4.20); Open issues
- **Severity:** minor
- **Problem:** The locality argument establishes the required faster-than-any-power decay of the full cell-field mutual cost, but leaves $`F(d)`$ entirely qualitative. The explicit length $`\xi`$ belongs only to the second-order coefficient; the full-cost length is estimated on an 18-cell chain. As the derivation itself acknowledges, this does not establish the full mutual cost’s asymptotic decay length. Thus the requested quantitative decay-scale characterization of the control field remains incomplete, although its qualitative short-range property is established.
- **Suggested fix:** Supply a quantitative spatial scale in the locality bound for $`F`$, with its dependence on J and the uniform gap bound, or derive an asymptotic decay rate for the full mutual cost. Keep the distinction between the exact second-order length and the finite-range numerical fit explicit.

## Focus points

None given.
