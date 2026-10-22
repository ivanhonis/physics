# External verification: 02-two-free-bodies

- **Subproject:** 07-ilang-weight
- **Package:** 02-two-free-bodies
- **Verified version:** v2
- **External round:** 2 of 3
- **Date:** 2026-10-21T00:05:49+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The exact conservation and held-body results, including the third-order failure of product factorization, are consistent with the stated contracts. The leading mutual-acceleration formula and its relation to the dressed curvatures are also supported by the supplied code and outputs within the stated band regime. The remaining issues concern the justification and error accounting of the next-order correction in Step 7.

## Issues

### I1. Uncontrolled denominator expansion
- **Location:** Step 7, derivation preceding Eq. (2.16)
- **Severity:** minor
- **Problem:** The denominators are expanded around $`2\sigma_1M_1`$, but R1 bounds their distance from zero; it does not make field-excitation energies small compared with $`2M_1`$. Thus R1 alone does not justify the indicated denominator expansion throughout the stated class. The leading coefficient in (2.16) can plausibly be justified without that additional hierarchy, using the held-state eigenvalue identities on both sides of an exact resolvent identity, but that argument is not supplied.
- **Suggested fix:** Replace the denominator expansion by an exact resolvent-identity calculation through first order in $`g_1`$, explicitly bounding the remainder using the isolation gap. Alternatively, state an additional hierarchy that controls the expansion and restrict the result accordingly.

### I2. Incomplete coupling-order remainder
- **Location:** Step 7, Eq. (2.19)
- **Severity:** minor
- **Problem:** The stated remainder $`O((\bar M^{(2)}/M_i)^2)`$ accounts for expanding the ratio, but not for the higher coupling orders already omitted from (2.16). Under $`\gamma_i\mapsto\epsilon\gamma_i`$, the displayed relative correction is $`O(\epsilon^2)`$, and omitted hopping and density corrections generally contribute $`O(\epsilon^3)`$; the displayed squared remainder is only $`O(\epsilon^4)`$. The discussion of the numerical results acknowledges these higher-order corrections, so the accuracy statement accompanying (2.19) is incomplete.
- **Suggested fix:** Include the omitted higher-coupling-order remainder explicitly—for example $`O(\epsilon^3)`$ under common coupling scaling—separately from the ratio-expansion, finite-$`\tau`$, and cut errors. State that its constants depend on the relevant isolation gaps.

## Focus points

None given.
