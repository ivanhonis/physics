# External verification: 06-inertia-internal-energy

- **Subproject:** 04-ilang-time
- **Package:** 06-inertia-internal-energy
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-10T12:55:53+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The block reduction of the instantaneous inverse inertia, the edge-cost calculation, and Model D’s fixed-λ linear response are algebraically sound. The leading averaged response proportional to τ²/(m + d_k) is also supported in the stated narrow-packet, weak-force regime. However, the conclusions for the decoupled body cover a narrower class than the question specifies, and the identification of a scalar inertia omits the background-coordinate normalization. Some limit and averaging error statements also need qualification.

## Issues

### I1. Arbitrary on-site blocks are not covered by the decoupled-body result
- **Location:** Step 6, Eq. (6.17), and Step 7
- **Severity:** major
- **Problem:** Item 1 defines the decoupled body by off-diagonal blocks proportional to the identity while allowing arbitrary $`T_{xx}`$. Step 6 instead imposes $`T_{xx}=D'`$, identical at every position. This extra restriction is essential: for position-dependent $`T_{xx}`$, the on-site operator generally does not commute with the hopping velocity. For example,
  ```math
  [V,S]=\sum_x |x+1\rangle\langle x|\otimes
  (T_{x+1,x+1}-T_{xx}),
  \qquad
  V=\sum_x|x\rangle\langle x|\otimes T_{xx}.
  ```
  Consequently, the free acceleration need not vanish, the force response need not remain constant to first order, and its average can depend on the internal state. Neither clock independence nor $`\mu_{\rm av}=\mu`$ follows for the full class specified in the question.
- **Suggested fix:** Identify spatially uniform on-site internal blocks as a necessary condition for the stated factorization and coincidence result. Address the allowed position-dependent blocks by stating that their averaged response requires their particular dynamics and has no universal clock-independent formula under the given assumptions.

### I2. Scalar inertia is identified without the background-coordinate factor
- **Location:** Step 5f, Eqs. (6.15)–(6.16), and Result
- **Severity:** minor
- **Problem:** The inverse-inertia map in (6.15) is correct, but the subsequent statement that the scalar inertia is $`M_k/\tau^2`$ does not use the background position and force normalization. With $`n=e/\sigma_X`$, its nonzero eigenvalue is
  ```math
  \mu_{\rm av}n
  =\frac{\tau^2\kappa^2\sigma_X^2}{M_k}\,n.
  ```
  Thus the scalar inertia corresponding to the defined background-space response is $`M_k/(\tau^2\kappa^2\sigma_X^2)`$. The quantity $`M_k/\tau^2`$ instead describes the response of the dimensionless position label to its conjugate scalar force $`\mathcal F`$.
- **Suggested fix:** Distinguish label-coordinate inertia from background-space inertia and state both normalizations explicitly. The proportionality to rest cost survives this correction.

### I3. Vanishing probability tails do not guarantee convergence of the mean position
- **Location:** Setup and assumptions, Model D on Z
- **Severity:** minor
- **Problem:** The finite-chain limit asserts convergence of $`\bar m`$ from localization within $`|x|\le W`$ “up to tails that vanish,” but vanishing tail probability alone is insufficient for a first moment. A tail of probability $`L^{-1/2}`$ at $`x=\lfloor L/2\rfloor`$ vanishes in probability while contributing approximately $`\sqrt L/2`$ to the mean. The propagation bound does not repair this initial-moment problem.
- **Suggested fix:** Require compactly supported initial states, or convergence with uniformly controlled position moments and weighted tails. State the order of the chain-size and momentum-concentration limits under those conditions.

### I4. The averaged error estimate is not complete for force-dependent long intervals
- **Location:** Step 5e, Eq. (6.14)
- **Severity:** minor
- **Problem:** Equation (6.14) displays only the relative averaging error $`O(1/(M_k\Lambda))`$. The argument also discards the variation of branch curvature along the drift, whose relative size is
  ```math
  O\!\left((\mathcal F_{\max}T)^2
  \left(1+\frac{\tau^2}{M_k^2}\right)\right),
  \qquad T=\lambda_1+\Lambda,
  ```
  as well as finite-packet and higher-order record/force effects. The stated small-drift condition makes this correction small, but does not make it bounded by the displayed averaging error. This matters when intervals are allowed to grow as the force decreases.
- **Suggested fix:** Include the additional discarded-error scales, or explicitly describe (6.14) as a first-order coefficient obtained at fixed interval before the long-interval limit. Likewise, identify (6.15) as the leading long-interval coefficient rather than the exact coefficient for every finite averaging interval.

## Focus points

None given.
