# External verification: 14-pair-level-next-order

- **Subproject:** 05-ilang-free-fall
- **Package:** 14-pair-level-next-order
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-18T12:26:12+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The fourth-order effective operator, bound-level formula, Hellmann–Feynman derivatives and inertia comparison are internally consistent, and the supplied code supports their stated scaling on the tested data. However, the wide-pair result does not cover every admissible hatted data set: simultaneous cancellations leave requested leading terms undetermined. There is also an overstatement in the no-binding consistency check at total labels where the leading free band is flat.

## Issues

### I1. Required wide-pair leading terms are missing for admissible data
- **Location:** Step 7, Eq. (14.12), Result and Open issues
- **Severity:** major
- **Problem:** Item 4 requests the leading term for every member of the stated class, but the derivation stops when both displayed coefficients vanish. Such cancellations actually occur with positive, finite admissible parameters. For example, define $`\hat a_i=\hat\tau_i^2/(4M_i)`$ and choose
  ```math
  \hat a_2=1,\qquad
  \hat a_1=\frac{5-\sqrt{21}}2,\qquad
  M_2=1,\qquad
  M_1=\frac{11+\sqrt{21}}{10}.
  ```
  These give $`\gamma_c=2\gamma_m`$ and $`\gamma_s=3\gamma_m`$, so both displayed terms of $`\mathcal C`$, and therefore of the relative inertia correction, vanish. Expansion of (14.9) instead gives
  ```math
  \mathcal C=\frac92\gamma_m u^4+O(u^5),
  ```
  a nonzero leading term omitted from the answer. Thus the acknowledged open issue leaves a required part of the package unanswered, rather than merely leaving an unnecessary characterization open.
- **Suggested fix:** Complete the small-$`u`$ analysis on the simultaneous-cancellation sets, including those of the rest-term coefficients, until the first nonzero term is determined for every admissible parameter choice.

### I2. No-binding consistency check excludes an unstated degenerate case
- **Location:** Consistency checks, item 2
- **Severity:** minor
- **Problem:** The assertion that the ordered no-binding limit of (14.6) reproduces the free-band minimum through fourth order requires a nondegenerate leading minimum, in particular $`j(P)>0`$. It fails when $`a_1=a_2`$ and $`P=\pi/2`$, where the leading free band is flat. For equal $`M_i=M`$ and $`\tau_i=\tau`$, the fourth-order coefficient obtained from (14.6) as $`u\to0`$ is
  ```math
  -\frac{3\tau^4}{32M^3},
  ```
  whereas the exact free-band minimum is
  ```math
  M+\sqrt{M^2+\tau^2}
  =2M+\frac{\tau^2}{2M}-\frac{\tau^4}{8M^3}+O(\tau^6).
  ```
  The stationarity argument used in the check does not resolve a flat leading band; fourth-order terms select among its degenerate minimizers. This does not invalidate the requested results near $`P=0`$.
- **Suggested fix:** Restrict this consistency check explicitly to $`j(P)>0`$, which includes the requested neighbourhood of zero, and state that it does not apply at the flat-band degeneracy.

## Focus points

None given.
