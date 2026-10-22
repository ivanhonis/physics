# External verification: 05-inertia-of-mark

- **Subproject:** 07-ilang-weight
- **Package:** 05-inertia-of-mark
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-21T08:17:41+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The order-τ² resolvent formula and the weak-mark full-grip expansion are largely consistent, and the supplied code meaningfully checks them for the requested sizes, levels and branches. However, the fixed-τ, small-field-hopping conclusions extrapolate the expansion beyond its validity and include an incorrect claim about isolation. The extension of the fall law to the full grip is not derived, and the common-speed question remains unresolved for part of the stated parameter class.

## Issues

### I1. Small-hopping conclusions do not follow from the order-τ² expansion
- **Location:** Step 8, “t_f small against τ”; Result, item 4
- **Severity:** major
- **Problem:** Two distinct problems occur here. First, failure of the sufficient perturbative condition $`\tau<d/2`$ does not prove that the exact dressed level is not isolated; therefore the assertion that the upper branch “is not isolated” is unjustified. Second, $`J=O(t_f^{2N_f})`$ only describes the coefficient of τ². It does not imply that the exact inertia diverges as $`t_f\to0`$ at fixed nonzero τ, because the omitted higher orders can then dominate. On a finite even ring, virtual body paths winding around the ring generate a nonzero term proportional to $`\tau^L\cos(LP)`$ even at $`t_f=0`$. For example, $`N_f=1`$, $`L=6`$, and $`\tau\ll|\gamma|M_k`$ give such a contribution at order τ⁶ in the continued sector contract. Thus the exact curvature need not tend to zero in the stated fixed-τ limit.
- **Suggested fix:** Distinguish failure of the τ-expansion criterion from actual spectral non-isolation. Restrict the inertia-divergence statement to the order-τ² coefficient, or control the higher-order terms and specify an ordering of limits in which they remain negligible. Account for finite-ring winding terms when discussing the exact continued-sector curvature.

### I2. The full-grip fall law is asserted rather than derived
- **Location:** Step 7, “(7.7) for FG”; Open issues
- **Severity:** major
- **Problem:** Equation (7.7) was supplied only for couplings (a) and (c). An isolated band, a held weight, and a cosine dispersion at zero source are not by themselves sufficient to establish its extension to FG: the source-dependent effective hopping and the effective body-position operator must also be controlled. The argument never calculates those terms or establishes their cancellation at the required order. In particular, the remainder $`O(\tau^4\gamma g_s)`$ cannot simply be inherited when the FG isolation gap vanishes with γ. The derivation explicitly acknowledges that the error term has not been re-derived. The numerical check evaluates curvature times held weight, not acceleration, so it does not settle this extension.
- **Suggested fix:** Derive the source-perturbed effective contract and the relevant position response through order $`\tau^2g_s`$, showing that they yield (7.7). State a remainder with its dependence on the FG isolation gap and the necessary smallness condition on the source.

### I3. The common-speed question remains unsettled at intermediate hopping
- **Location:** Step 6, discussion following Eq. (5.9); Result, Eq. (5.9)
- **Severity:** major
- **Problem:** The question asks whether one speed works throughout the stated regime. The derivation excludes such a speed only in two hopping limits, then leaves open possible isolated intermediate values of $`t_f`$. Analyticity establishes that possible solutions are exceptional, not whether they exist or which descriptions satisfy the condition. This leaves item 2 incomplete for the stated class. For coupling (c), the displayed formula already gives a stronger conclusion:
  ```math
  \frac{D^{(c)}_{k,+}+D^{(c)}_{k,-}}2
  =
  \frac{n\gamma^2M_k^2}{2t_f\tau^2}
  \left\langle\frac{1+\cos q+\cos^2q}{1-\cos q}\right\rangle_q
  +O(\gamma^3).
  ```
  Its coefficient is strictly positive. This branch-even quantity varies with $`M_k^2`$, and an order-γ² adjustment of the common speed cannot remove it. Hence coupling (c) has no intermediate exceptions at this order when there are distinct levels.
- **Suggested fix:** Complete the common-speed test throughout the stated nonresonant class. For (c), use the branch average above to exclude exceptions. For (a), resolve the remaining equality conditions rather than stopping at the statement that any solutions would be isolated.

### I4. The hopping discussion omits multi-object isolation resonances
- **Location:** Step 4, final paragraph; Step 8, “Isolation, (a) and (c)”
- **Severity:** minor
- **Problem:** Avoiding $`2M_k=\varepsilon_q`$ controls the displayed second-order denominators, but it does not characterize isolation for $`N_f\ge2`$. The quoted condition (6.4) also excludes resonances with sums of excitation energies. For example, on $`L=6`$, two field objects can each have excitation energy $`3t_f`$. Taking $`M_k=3t_f`$ gives a resonance at $`2M_k=6t_f`$, although the stated inequality $`4t_f<2M_k`$ holds. The earlier assumption of the full condition (6.4) excludes this example, so this does not invalidate formulas used strictly under that assumption, but the item-4 discussion is incomplete as an isolation criterion.
- **Suggested fix:** Retain the full many-object excitation condition in the hopping discussion, distinguish it from avoidance of the denominators in (5.9), and state the associated bound involving τ and the actual spectral distance.

### I5. Exceptional place pairs invalidate the stated first-dependence order
- **Location:** Step 7, Eq. (5.10) and “First dependence”; Result, Eq. (5.10)
- **Severity:** minor
- **Problem:** The factored formula assumes $`F\ne0`$, and the claimed first relative-order-γ dependence also requires $`\Xi\ne0`$. Neither condition is stated. There are nontrivial allowed place pairs with $`F\ne0`$ but $`\Xi=0`$: for example, on $`L=8`$, source separations $`r=3`$ and $`r'=4`$ give exactly this cancellation. For such pairs the first dependence must be sought at a higher order. When the two separations are reflection-equivalent, $`F=0`$, the displayed quotient defining $`\Xi`$ is undefined and the weight difference instead vanishes by symmetry.
- **Suggested fix:** State the generic conditions $`F\ne0`$ and $`\Xi\ne0`$, handle reflection-equivalent pairs separately, and determine the next nonzero dependence when $`\Xi=0`$, as required by the first-order claim.

## Focus points

None given.
