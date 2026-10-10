# External verification: 05-moving-clock

- **Subproject:** 04-ilang-time
- **Package:** 05-moving-clock
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-10T12:52:47+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The exact decoupling result, anticommutation calculation, spectrum, positive-branch velocities, and bound from 17-motion are correct. The principal problem is that the moving-clock distribution is only leading-order accurate in ε on the clock-tick scale, rather than accurate through the requested first order; the derivation explicitly leaves the relevant correction uncomputed. The rate–velocity formulas therefore hold at leading order in ε, not at the claimed first-order accuracy. There are also minor gaps in the infinite-chain moment convergence argument and the packet-spread error estimate.

## Issues

### I1. First-order clock corrections are omitted on the tick scale
- **Location:** Step 6(ii), Eqs. (5.14)–(5.19), and Open issues
- **Severity:** major
- **Problem:** The quadratic term in the energy expansion is second order in $`d_k/m`$, but its accumulated phase is first order in ε when $`\lambda/\lambda_0=O(1)`$. Consequently, discarding it does not produce a distribution accurate through first order in ε on the scale used to determine the clock tick. The derivation’s own error estimate, $`O(N\epsilon\,\lambda/\lambda_0)`$, and its first open issue acknowledge precisely this missing contribution.

  For example, take $`N=2`$, neglect packet spread and records, and set
  ```math
  \omega=\sqrt{m^2+\tau^2\sin^2p_0},\qquad \gamma=m/\omega.
  ```
  Branch mixing affects the reading probabilities only at $`O(\epsilon^2)`$, so the relevant phase difference is $`\omega_1-\omega_0`$. Its effective clock rate is
  ```math
  \frac{\omega_1-\omega_0}{d_1}
  =\gamma\left[1+\frac{\epsilon}{2}(1-\gamma^2)\right]
  +O(\epsilon^2).
  ```
  This gives a generally nonzero $`O(\epsilon)`$ correction to (5.14) at fixed $`\lambda/\lambda_0`$. Thus (5.15) supplies only the leading tick ratio, and the “exact” chain relation in Step 8 is exact only within that leading-order approximation. Setting all $`\mu_k`$ to $`m`$ also discards first-order velocity corrections, which the second open issue acknowledges.
- **Suggested fix:** Retain the phase-curvature contribution on the scaled clock interval and compute the corresponding first-order reading and rate corrections. Treat velocity corrections consistently when expressing the result in terms of velocity. Label the existing formulas as leading order in ε, and distinguish the nominal certain tick of the linearized clock from the finite-ε reading behavior.

### I2. Norm approximation does not establish convergence of position moments
- **Location:** Step 2, How the limit is taken
- **Severity:** minor
- **Problem:** Equation (5.3) establishes superexponentially small propagated tails for a finitely supported start. It does not establish such tails for every smooth Fourier packet or every rapidly decaying start: those starts may already have tails that decay more slowly than exponentially. Moreover, approximation in Hilbert-space norm controls reading probabilities, but by itself does not control the expectation of the unbounded position operator. Therefore the statement “Hence … $`\bar x`$ and $`v`$ converge” needs an additional argument.
- **Suggested fix:** Restrict the superexponential-tail statement to finitely supported starts. For the smooth packets actually used, establish convergence in a position-weighted norm or provide a uniform tail-moment estimate. Velocity convergence can be justified separately using the bounded commutator $`i[C,x]`$.

### I3. Packet-spread error estimate fails at stationary points
- **Location:** Step 6(iii) and the neglected terms following Eq. (5.14)
- **Severity:** minor
- **Problem:** The stated spread error $`O(\delta p\,|\gamma'(p_0)|\,\lambda/\lambda_0)`$ vanishes at $`p_0=0`$ and $`p_0=\pm\pi/2`$, although a finite-width packet there still samples different values of $`\gamma(p)`$. At those points the leading spread correction is generally quadratic in the width, not zero. Thus the listed error estimate is not valid throughout the stated range of $`p_0`$.
- **Suggested fix:** Include the second-order Taylor remainder, for example a contribution controlled by $`(\delta p)^2\sup|\gamma''|\,\lambda/\lambda_0`$, together with the appropriate derivatives of $`P_N`$. Alternatively, give a uniform bound using the variation of $`\gamma`$ across the packet.

## Focus points

None given.
