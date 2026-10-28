# External verification: 07-bond-inertia

- **Subproject:** 08-ilang-propagation
- **Package:** 07-bond-inertia
- **Verified version:** v6
- **External round:** 2 of 3
- **Date:** 2026-10-25T16:11:45+01:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The second-order mutual kernel, its held limit, and the leading inertia formula (7.10) are consistently derived; the supplied code supports these calculations within the tested regimes. The distinction between isolated levels and formal coefficients is also made explicitly. Remaining problems concern the power counting of lattice-enhanced corrections, the reference used for finite-extent weighing, and qualifications at large distances and vanishing leading coefficients.

## Issues

### I1. Lattice-enhanced correction is assigned the wrong order
- **Location:** Step 7, paragraph following Eq. (7.9)
- **Severity:** minor
- **Problem:** The assertion that the next inversion term $`D^2/I`$ is relatively $`O(|\Delta E|/\bar M)`$ is not valid when the lattice contribution dominates. Indeed,
  ```math
  \frac{D_{\rm lattice}}{I}
  =\frac{4I_1I_2\langle T\rangle}{I}
  =4m_{\rm red}\langle T\rangle
  =2\langle k^2\rangle,
  ```
  which is controlled by the inverse squared binding size, not generally by $`|\Delta E|/\bar M`$. The numerical examples explicitly enter this lattice-dominated regime. The broader error list already includes $`a_b^{-2}`$, so this does not invalidate the leading formula, but the subsequent power-counting statement is incorrect.
- **Suggested fix:** State the inversion condition as $`|D/I|\ll1`$, and count its correction using both $`|\Delta E|/|\sigma_1\bar M_1+\sigma_2\bar M_2|`$ and $`\langle k^2\rangle`$, with the appropriate exclusions near cancellations.

### I2. Finite-extent fall comparison changes its field reference
- **Location:** Step 9, Eq. (7.13) and paragraph Variation of the field over the pair
- **Severity:** minor
- **Problem:** The claimed finite-extent correction $`O((a_b/\ell)^2|\Delta E|/\bar M)`$ applies after normalizing to the members’ inertia-weighted average field gradient. It does not apply directly to the displayed comparison with the position-independent local ratio $`w_i/I_i=\kappa`$, if the pair weight is referenced to the field at its centre or midpoint. For example, equal positive-branch members at $`X\pm\xi/2`$ already give a first-order member contribution proportional to
  ```math
  \kappa\left\langle\cosh\frac{\xi}{2\ell}\right\rangle
  =\kappa\left[1+\frac{\langle\xi^2\rangle}{8\ell^2}+\cdots\right],
  ```
  without a factor $`|\Delta E|/\bar M`$. The text invokes the inertia-weighted reference, but does not explicitly change the definition on the left-hand side of (7.13). This matters because the question asks specifically for the mutual contribution.
- **Suggested fix:** Define the finite-extent comparison explicitly as subtraction of the members’ force contributions at their own places, or normalize both sides to their inertia-weighted average gradient. Otherwise include the unsuppressed member finite-extent term.

### I3. Large-distance velocity expansion needs an additional restriction
- **Location:** Step 4, Eq. (7.6) and its following paragraph
- **Severity:** minor
- **Problem:** The $`V^2`$ expansion above the pinning length is not uniform in separation. Its correction contains $`V^2|r|/(c_0^2\ell)`$, so small $`V/c_0`$ alone does not justify truncation when $`|r|/\ell`$ is arbitrarily large. The unexpanded range $`\ell\sqrt{1-V^2/c_0^2}`$ and its truncated expansion have different validity statements.
- **Suggested fix:** Require
  ```math
  \frac{V^2|r|}{c_0^2\ell}\ll1
  ```
  for the displayed large-distance Taylor formula, or retain the unexpanded continuum kernel when discussing larger separations.

### I4. Linear-grip fall criterion uses an excluded leading cancellation
- **Location:** Step 8, excluded cancellations; Step 9, Eq. (7.14); Result
- **Severity:** minor
- **Problem:** The derivation excludes $`r=\sqrt2`$ in the deep regime because the leading bond-inertia term vanishes, but subsequently lists the linear grip at exactly $`r=\sqrt2`$ as satisfying the fall criterion. At this point both the leading held-bond weight and the leading constant contribution to $`D`$ vanish. The retained kinetic and lattice terms then determine the first nonzero comparison, and they do not generally satisfy $`w_b=\kappa D`$.
- **Suggested fix:** Distinguish cancellation of the leading constant contribution from equality at the first nonzero order. Either retain the exclusion in the fall result or explicitly evaluate the remaining terms of (7.13) at $`s=0,\ r=\sqrt2`$.

## Focus points

None given.
