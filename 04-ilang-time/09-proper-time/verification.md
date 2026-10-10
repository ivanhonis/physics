# External verification: 09-proper-time

- **Subproject:** 04-ilang-time
- **Package:** 09-proper-time
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-10T13:56:16+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The central derivation is consistent with the stipulated weak-record and fixed-parameter expansion regimes. In particular, the adiabatic calculation, cancellation of the first-order even phase in the clock distribution, and meeting advances support the principal results. There are minor errors concerning periodicity and inversion of the speed–rate relation, and the chain-limit argument needs to be connected explicitly to the stated positive-branch starts.

## Issues

### I1. Incorrect period assigned to the plane-wave label
- **Location:** Step 6, paragraph following Eq. (9.18)
- **Severity:** minor
- **Problem:** The statement that “the label motion has period π/𝓕” contradicts Eq. (9.1). The label $`p_0+\mathcal F\lambda`$, taken modulo $`2\pi`$, has period $`2\pi/\mathcal F`$. It is $`\bar\omega`$, $`\Gamma`$, $`\bar w`$, and the retained displacement that have period $`\pi/\mathcal F`$. This does not invalidate the meeting times, which depend on $`\sin^2p`$.
- **Suggested fix:** Replace “label motion” with “the retained displacement and rate functions,” and distinguish their period from the label’s period.

### I2. The second invertible speed branch is omitted
- **Location:** Step 5, paragraph following Eq. (9.14)
- **Severity:** minor
- **Problem:** The text identifies monotonicity of $`b`$ in $`|\sin p|`$ only with
  ```math
  \sin^2p\le\frac{\bar\mu}{\bar\mu+\sqrt{\bar\mu^2+\tau^2}}.
  ```
  There is also a monotonically decreasing branch above this threshold. Consequently, the rate can be recovered from the speed on either branch if the branch is specified; it cannot be recovered uniquely from speed across both branches.
- **Suggested fix:** State both monotonic branches and explain that inversion requires choosing one. Retain the lower branch as the one relevant to the small-label approximation.

### I3. Chain-limit justification does not cover the stated starts directly
- **Location:** Setup and assumptions, S2–S3
- **Severity:** minor
- **Problem:** S2 establishes boundary suppression for compactly supported starts, whereas S3 specifies an exact positive-branch momentum-space spinor. For $`m,\tau>0`$, its momentum-dependent spinor generally produces noncompact position-space tails. The derivation does not explain how these starts are obtained from the finite-chain descriptions, or control their initial tails when passing to the limit. For the displacement, control of position moments is also needed, not just convergence of state norms.
- **Suggested fix:** Specify a finite-chain truncation or approximation of the S3 starts, state the required tail and position-moment conditions, and explain that the truncation errors vanish together with the boundary errors. Alternatively, explicitly restrict the start family to sufficiently regular localized packets for which these controls hold.

## Focus points

None given.
