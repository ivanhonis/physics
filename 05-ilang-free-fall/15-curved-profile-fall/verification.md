# External verification: 15-curved-profile-fall

- **Subproject:** 05-ilang-free-fall
- **Package:** 15-curved-profile-fall
- **Verified version:** v2
- **External round:** 1 of 3
- **Date:** 2026-10-18T12:34:24+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The first-order acceleration formula, its separation into oscillating and non-oscillating terms, and the window-averaging bounds are consistent with the stated perturbative regime. The factor-class counterexamples correctly show that exact level independence fails for finite-width starts, while the stated local-slope limit restores it. Two minor issues remain: an auxiliary envelope moment is misidentified as a physical position moment, and the pure-curvature case of the control family needs a short additional argument.

## Issues

### I1. Auxiliary fourth moment is not the body’s position fourth moment
- **Location:** Step 3, Eq. (15.16) and following paragraph
- **Severity:** minor
- **Problem:** The definition $`W_4^4=\langle g|\eta^4|g\rangle`$ is a fourth moment of the scalar envelope, not the physical position distribution of $`B_{k,+}[g]`$. Since $`\hat y=\eta+\alpha\rho_2`$, the actual fourth position moment is
  ```math
  \langle\psi_0|\hat y^4|\psi_0\rangle
  =\|(\eta^2+\alpha^2)g\|^2+\|\{\alpha,\eta\}g\|^2,
  ```
  which generally differs from $`\|\eta^2g\|^2`$. The bounds themselves consistently use the explicitly defined envelope norm, so their algebra is unaffected.
- **Suggested fix:** Identify $`W_4`$ as an auxiliary envelope fourth-moment width throughout. If a condition in terms of the body’s physical fourth position moment is intended, derive the required comparison separately.

### I2. Pure-curvature control is not explicitly established
- **Location:** Step 8(b) and Result entry (15.14)
- **Severity:** minor
- **Problem:** The explicit control argument covers $`g_n\ne0`$, but the question also includes $`g_n=0`$, $`h_n\ne0`$. The final observation that $`b_k(0)`$ depends on the level is not by itself sufficient: the constant part of $`b_k`$ cancels from $`c_g`$ because $`\int j=0`$, and the secular coefficient involves $`b_k\omega_k'`$, not $`b_k(0)`$ alone. Thus the pure-curvature conclusion is asserted without the short argument requested for this case.
- **Suggested fix:** Apply the chirped, even-density starts used in Step 8(a) to the control coefficients. For sufficiently small momentum support, the unequal $`p^2`$ coefficients of $`b_k`$ and $`b_l`$ give $`c_{g,k}\ne c_{g,l}`$, while the secular terms vanish by parity. State the flat-profile exception separately.

## Focus points

None given.
