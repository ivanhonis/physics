# External verification: 10-field-own-contract

- **Subproject:** 05-ilang-free-fall
- **Package:** 10-field-own-contract
- **Verified version:** v3
- **External round:** 2 of 2
- **Date:** 2026-10-11T14:58:36+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The compression, leakage estimates, and second-order effective-contract calculation are largely consistent in the stated controlled regime. However, the clock–fall defect is obtained by an additional reciprocal expansion that is not controlled by R1, and admissible examples satisfying even the added margins make the comparison undefined. The derivation also explicitly leaves the requested fall calculation for general independent cells unanswered.

## Issues

### I1. Uncontrolled expansion of the inverse clock rate
- **Location:** Step 3(d), Eqs. (10.17) and (10.26); Step 5, relation row
- **Severity:** major
- **Problem:** At leading order, the mean clock rate and its relative gradient at the origin are
  ```math
  \bar r(0)=\lambda_0^{-1}(1-\gamma_0\Sigma),\qquad
  \frac{\bar r(1)-\bar r(0)}{\bar r(0)}
  =\frac{g-\gamma_1\Sigma}{1-\gamma_0\Sigma}.
  ```
  The derivation expands the denominator without requiring $`|\gamma_0\Sigma|\ll1`$, or even requiring $`\bar r(0)\neq0`$. Neither R1 nor (10.28) supplies these conditions: $`\gamma_0M_{\max}`$ can be large when $`\epsilon_1^2\Delta_f/M_{\max}`$ is large.

  For example, take two clock levels with $`M_0=1`$, $`M_1=2`$, $`\lambda_0=\pi`$, and a two-place field with
  ```math
  C_f=\Delta|1\rangle\langle1|,\quad
  \varphi_0=|0\rangle,\quad
  \Phi_x=(1+gx)\mathbb1+\sqrt{\Delta/3}\,\sigma_1 .
  ```
  For large $`\Delta`$, R1 and the margins in (10.28) hold, while $`\gamma_0=1/3`$, $`\gamma_1=\gamma^{(3)}_x=0`$, and $`\Sigma=3`$. Consequently, $`\bar r(0)=0`$: the relative clock-rate gradient is undefined, whereas (10.17) reports the finite defect $`\tau^2g`$. This is a genuine nonuniformity of the stated approximation, not an error covered by its advertised remainder.
- **Suggested fix:** State an additional hierarchy controlling the clock-spacing correction before expanding its reciprocal, and require a nonzero comparison rate. Alternatively, retain the denominator explicitly and treat zero-rate members separately. Restrict the defect formulas and their “if and only if” claims to the resulting validity range.

### I2. Requested general-cell fall calculation remains open
- **Location:** Step 4(c), Cells outside L; Result, Item 4; Open issues
- **Severity:** major
- **Problem:** Item 4(c) asks for the evaluation with $`n_x=1+gx`$ throughout the stated cell class, with arbitrary positive $`\Delta_x`$ and nonnegative $`\varepsilon_x`$. The derivation instead evaluates the fall only in the added subclass L and explicitly leaves the fall outside L undetermined. Correctly observing that the quoted linear-profile formulas cannot be substituted into a nonlinear effective profile does not answer the requested calculation, nor establish that the requested result cannot be obtained. In particular, the control with constant $`\varepsilon_x^2/\Delta_x`$ can still have nonlinear hopping coefficients $`c_x`$, and its remaining effect on fall is not settled.
- **Suggested fix:** Complete the requested evaluation from the effective level blocks for the full cell class, or provide a justified negative answer establishing why the requested drift quantity is not defined or cannot have the asserted interpretation there. The calculation for L should remain explicitly conditional rather than being presented as completion of item 4(c).

## Focus points

None given.
