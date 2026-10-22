# External verification: 05-inertia-of-mark

- **Subproject:** 07-ilang-weight
- **Package:** 05-inertia-of-mark
- **Verified version:** v3
- **External round:** 3 of 3
- **Date:** 2026-10-21T10:02:02+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The finite-ring sector reduction, the order-τ² resolvent formula, and the principal weak-mark comparisons are consistent. The supplied code implements the requested single-field-object curvature checks at two ring sizes, two levels, and both branches, and the outputs support the stated perturbative orders. Remaining issues concern control of the large-ring limit for coupling (c), incomplete treatment of exceptional cancellations in item 3, and a sign error in one bound.

## Issues

### I1. Uncontrolled large-ring limit for coupling (c)
- **Location:** Step 8, L→∞ at fixed n; Result (5.11)
- **Severity:** minor
- **Problem:** The statement that (5.2) and (5.3) “still hold” for the attractive branch needs qualification for coupling (c) when τ is fixed. Although the held spectral distance tends to the positive binding gap, the stated sufficient perturbative condition is $`\tau\lVert K\rVert<d/2`$. For (c),
  ```math
  \lVert K\rVert=\max_{0\le m\le N_f}|1+\gamma m/2|
  \sim |\gamma|N_f/2,
  ```
  so this condition eventually fails as $`N_f=nL\to\infty`$. Likewise, the displayed remainder in (5.2) is not uniformly controlled by the supplied estimate. Isolation of the held level alone therefore does not establish the claimed fixed-τ continuation of the inertia calculation. This does not prove that the exact dressed level loses isolation; it identifies a missing control argument.
- **Suggested fix:** Distinguish the pointwise, finite-L coefficient of τ² from a controlled fixed-τ large-L limit. For (c), either impose an L-dependent restriction on τ that preserves the stated criterion, or supply a sharper uniform perturbative estimate before retaining the large-L claim.

### I2. Exceptional place pairs are not fully settled
- **Location:** Step 7, Eq. (5.15), and Result (5.15)
- **Severity:** minor
- **Problem:** For Ξ = 0, the displayed coefficient is useful, but the requested first non-universal order is not fully established throughout the stated class. For FG, nonvanishing is explicitly checked only for $`N_f=1`$ and six even ring sizes. For (a), the branch-odd coefficient is left as “nonzero except where this average vanishes,” without establishing whether the remaining level dependence necessarily survives at those zeros, or whether simultaneous cancellations across the body's levels are possible. The question's exemption for tuned exceptions concerns item 2, not these item-3 cases. It is therefore unclear whether all relevant exceptional cases have been covered.
- **Suggested fix:** Establish nonvanishing, or give the necessary cancellation conditions, for the full class at Ξ = 0. For FG, the missing extension can be settled directly from
  ```math
  \Psi_0=-\frac{(L^2-1)(2L^2+7)}{360L^2t_f^2}
  ```
  at these place pairs, together with $`K_L>0`$. For (a), determine whether the complete coefficient in (5.15), rather than only its branch-odd part, can be common to every level and branch; if so, the first subsequent dependence remains to be established.

### I3. Missing absolute value in the dependence bound
- **Location:** Step 7, First dependence, Ξ ≠ 0
- **Severity:** minor
- **Problem:** The bound
  ```math
  |\gamma M_k\Xi|\le \gamma M_kL/(6t_f)
  ```
  is false for the allowed negative values of γ, since its right-hand side is then negative. The definition of $`\varkappa_k`$ correctly uses $`|\gamma|`$, so this is a local sign error rather than a problem with the expansion.
- **Suggested fix:** Replace the right-hand side by $`|\gamma|M_kL/(6t_f)`$.

## Focus points

None given.
