# External verification: 02-what-a-body-presents

- **Subproject:** 06-ilang-source
- **Package:** 02-what-a-body-presents
- **Verified version:** v2
- **External round:** 2 of 3
- **Date:** 2026-10-19T10:02:10+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The first-order reduced-view equation, remainder estimates, branch-source evaluations, and bound-pair expectation identities are correctly derived. The component decomposition also provides a consistent way to distinguish quantities fixed by the total contract from contract-list conventions. One well-definedness claim is overbroad: additive source differences are invariant under start-independent shifts, but changes of source ratios are not.

## Issues

### I1. Changes of source ratios are not invariant across splits
- **Location:** Step 8, Eq. (2.14)(iii), and Result item 13(iii)
- **Severity:** minor
- **Problem:** “Their changes between two starts” includes the ratios listed in (2.14)(i)–(ii). Although a start-independent shift cancels in $`\Delta S_i`$, it does not generally cancel in $`\Delta(S_1/S_2)`$. For example, take all $`\mathring\Phi_x=\mathring\Phi\neq0`$, and two starts with totals
  ```math
  (S_1,S_2)=(q,q),\qquad(-q,q),\qquad q\neq0.
  ```
  The difference of their source ratios is $`2`$. The allowed move $`W_2=q\mathring\Phi`$, compensated in $`C_f`$, shifts $`S_2`$ to $`2q`$ in both starts without changing $`C`$. The difference of ratios then becomes $`1`$. This counterexample satisfies the identifiability condition in (2.14)(ii) and already applies at $`\lambda=0`$.
- **Suggested fix:** Restrict the across-split invariance assertion to additive differences such as $`\Delta s_x`$ and $`\Delta S_i`$. Ratios evaluated in the fixed component split remain functions of $`C`$ and the starts, but changes of those ratios are not identical across other splits. If ratios of source differences were intended instead, state that explicitly and require nonzero denominators.

## Focus points

None given.
