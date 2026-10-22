# External verification: 04-weight-of-bond

- **Subproject:** 07-ilang-weight
- **Package:** 04-weight-of-bond
- **Verified version:** v2
- **External round:** 2 of 3
- **Date:** 2026-10-20T23:53:14+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The one-object reduction, perturbative coefficients, bond profile, and leading weight ratios are consistent with the stated contracts. The finite-rank argument provides appropriate additive control, and the code substantially supports the leading-order formulas. The remaining issues concern an overstatement of the highest-state symmetry for exact ratios, a missing density factor in one bound, and the coupling scaling needed for the large-size control.

## Issues

### I1. Highest-state ratios are unchanged only at leading order
- **Location:** Step 7, Eq. (4.14), and Result
- **Severity:** minor
- **Problem:** Step 6 explicitly defines exact ratios, whereas Step 7 says that all ratios are unchanged under lowest-to-highest mirroring. The exact spectral identity instead relates the highest-state ratio at the given couplings to the lowest-state ratio with all body and reference-state couplings sign-reversed. For the full grip, for example,
  ```math
  B_{\max}(g)=-B_{\min}(-g),\qquad
  (W_b)_{\max}(g)=(W_b)_{\min}(-g),
  ```
  with the corresponding sign-reversed relation for the exact single-body quotient. Thus $`\rho_0`$ is unchanged, but a nonzero correction linear in the body couplings reverses sign. Such corrections are reported numerically in the derivation. The code checks the spectral mirror identity, not equality of the exact ratios at unchanged couplings.
- **Suggested fix:** Restrict “unchanged” in (4.14) and the Result to the retained leading-order ratios, and state the sign-reversed-coupling relation for exact ratios.

### I2. Missing density factor in the cost-difference bound
- **Location:** Step 5, paragraph preceding Eq. (4.9)
- **Severity:** minor
- **Problem:** The degree-two-and-higher part of the single-body cost difference is bounded there by $`c_*|g_A-g_B|\eta`$, without $`n`$. Its second-order contribution is already
  ```math
  -\frac{n\ell_0}{t_f}(g_A^2-g_B^2),
  ```
  so the appropriate bound scales as $`c_*n|g_A-g_B|\eta`$. Since $`N_f`$, and hence $`n`$, is unrestricted, the written bound cannot hold uniformly. The subsequent relative $`O(\eta)`$ conclusion nevertheless survives.
- **Suggested fix:** Restore the factor $`n`$, and compare this corrected bound with the leading cost differences to justify the stated uniform relative error.

### I3. Large-size control needs an explicit coupling limit
- **Location:** Step 6, full-grip answer and Controls
- **Severity:** minor
- **Problem:** The divergence of the square-torus leading ratio at fixed places is established, but its use as a control for exact ratios requires a stated family of couplings. At fixed nonzero couplings, $`\eta`$ grows with $`\ln L`$, eventually leaving the perturbative regime; moreover, controlling the exact ratio requires $`\eta K\ll1`$, not merely small $`\eta`$. The text acknowledges this condition generally but does not specify how it is maintained in the advertised $`L\to\infty`$ control.
- **Suggested fix:** Either describe this explicitly as a failure of the leading coefficient, or specify an admissible family with couplings shrinking so that $`\eta(L)K(L)\to0`$, together with the required source regime.

## Focus points

None given.
