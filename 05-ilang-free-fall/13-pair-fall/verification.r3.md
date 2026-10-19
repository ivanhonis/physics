# External verification: 13-pair-fall

- **Subproject:** 05-ilang-free-fall
- **Package:** 13-pair-fall
- **Verified version:** v5
- **External round:** 3 of 3
- **Date:** 2026-10-11T22:30:05+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The first-order motion, common secular acceleration, and leading-order comparison with the free parts follow correctly from the quoted inputs. The treatment of the two orders of limits answers the restricted version of item 2(c), including its allowance for an undecided class between the necessary and sufficient conditions. The supplied code implements the stated symmetric-difference checks, and its outputs support the reported numerical comparisons. The remaining issues concern overstatements of clock-reading resolution and qualifications lost in the summaries.

## Issues

### I1. Reading-resolution hierarchy is not a necessary condition
- **Location:** Step 7.1, rate parameter and reading; Eq. (13.35); Result, item 4
- **Severity:** minor
- **Problem:** The Lipschitz bound on $`P_N`$ and the quoted big-$`O`$ remainder provide upper bounds, not lower bounds on either the signal or the actual error. Consequently, failure of (13.35) means that the supplied error estimate cannot establish resolution; it does not prove that a reading cannot resolve the correction. The actual remainder might be much smaller than its bound. Conversely, satisfying this hierarchy alone does not establish resolution at an advance where the reading distribution has vanishing first-order sensitivity to the rate.
- **Suggested fix:** Describe (13.35) as a conservative control hierarchy for separating a generic rate signal from the quoted error bound, rather than a necessary condition for actual resolution. Retain the distinction between the rate parameter and an operationally inferred rate, and qualify any positive resolution claim by the reading distribution’s sensitivity at the chosen advance.

### I2. Three-object requirement loses its exceptions in the result
- **Location:** Result, item 1; Step 1.4
- **Severity:** minor
- **Problem:** The result states unconditionally that a binding carrying a factor of the field would require a three-object term forbidden by A5. Step 1.4 correctly identifies the conditions for a genuinely three-object component, but those conditions disappear from the summary. For example, if the field factor is $`\Phi=\gamma\mathbb 1_f`$, then $`U\otimes\Phi`$ is simply the admissible pair term $`\gamma U`$, extended by the identity on the field. Likewise, a factorized expression whose body operator has only single-object components can reduce to a sum of pair terms.
- **Suggested fix:** Carry the qualification from Step 1.4 into the result: the obstruction applies to a non-scalar field factor multiplying a genuinely two-body binding component. Name the scalar and reducible cases explicitly.

### I3. Clock–fall matching condition is only leading-order
- **Location:** Step 7.3, equal to τᵢ²; Result, item 4
- **Severity:** minor
- **Problem:** The detailed argument correctly derives the condition $`g_j/g_i=\mathsf z_i(u)`$ only at leading order, using $`\varrho_i=g_i`$. The result subsequently says that $`\mathsf w_i^2`$ equals $`\tau_i^2`$ only on the member (13.23), without retaining that qualification. Beyond leading order, matching the pair’s acceleration to the free part’s acceleration is not the same as matching $`-a_{\rm pair}/\varrho_i`$ to $`\tau_i^2`$, because $`\varrho_i\neq g_i`$ in general. The exact acceleration-matching member discussed in Step 6.4 therefore cannot also be identified as the exact clock–fall matching member.
- **Suggested fix:** State explicitly in the result that (13.23) is the leading-order clock–fall matching condition. If an exact matching claim is retained, use $`a_{\rm pair}=-\tau_i^2\varrho_i`$, with $`\varrho_i`$ from (13.21), rather than equality with the free-part acceleration.

## Focus points

None given.
