# External verification: 08-field-speed

- **Subproject:** 07-ilang-weight
- **Package:** 08-field-speed
- **Verified version:** v3
- **External round:** 3 of 3
- **Date:** 2026-10-21T18:28:44+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The first-order response, torus averaging bound, axial front speed, and quadratic scale for forming the long-range mark are consistent with the stated contracts and the supplied numerical checks. The remaining problems concern an unjustified upgrade from pointwise scaling limits to all-later-time statements, an unstated band restriction in the packet-speed discussion, and two local algebraic/asymptotic slips. These do not overturn the principal first-order results.

## Issues

### I1. Pointwise scaling estimates do not establish uniform formation thereafter
- **Location:** Steps 4–6, Eqs. (8.9), (8.10) and (8.15)
- **Severity:** minor
- **Problem:** The asymptotics are obtained at fixed ζ or fixed c, but the formation criterion requires accuracy at every subsequent λ within the stated regime. Pointwise convergence for each fixed scaling variable does not itself justify that uniform assertion. In particular, (8.15) establishes accuracy at every fixed c > 1, but the subsequent wording “from λ = cρ/√κ_h on” also encompasses c growing with ρ, which the stationary-phase argument does not cover. The same distinction affects the all-later-time interpretation of (8.10). This is a missing uniformity argument, not evidence that the claimed scales are wrong.
- **Suggested fix:** Supply uniform remainder estimates over the relevant later-time domain, including its large-time endpoint, or consistently describe these results as formation in the pointwise scaling-limit sense. Keep that interpretation distinct from the genuinely uniform running-average bound (8.11).

### I2. A general two-band packet need not move with an average of band group velocities
- **Location:** Step 7, paragraph following Eq. (8.17)
- **Severity:** minor
- **Problem:** The statement “A packet moves with an average of group velocities” requires a single-band preparation, band-incoherent state, or an appropriate asymptotic/time-averaged interpretation. For a coherent superposition of the two Model D branches, the instantaneous velocity contains interband terms. Indeed, at k = 0 the band group velocities vanish, while the velocity operator is −τσ₁ and can have expectation ±τ. Thus the weaker condition involving m_a bounds all band group velocities but does not, without a state restriction, bound every packet’s instantaneous velocity below the field front.
- **Suggested fix:** State the necessary band-preparation or long-time interpretation. Retain τ < 2t_f as the state-independent sufficient comparison, and label the weaker condition as a comparison of band group velocities.

### I3. Incorrect sign in the finite-size static-reference example
- **Location:** Step 8, Static mark bullet
- **Severity:** minor
- **Problem:** After giving the source-site value $`-ng_sL/(6t_f)`$, the text says that both listed values lie below −n for sufficiently large $`|g_s|L/t_f`$, while discussing g_s < 0. For negative g_s, the source-site value is positive, not below −n. The antipodal value is negative and already suffices for the intended counterexample.
- **Suggested fix:** Separate the signs: for g_s > 0 use the source-site value; for g_s < 0 use the antipodal value. The stated sufficient condition $`|g_s|L/t_f>12`$ for failure somewhere on the ring can remain.

### I4. Incorrect relative order quoted for the front integration-by-parts remainder
- **Location:** Step 3, paragraph immediately preceding Eq. (8.6)
- **Severity:** minor
- **Problem:** The derivative-integral correction is described as $`O(\rho^{-2/3})`$ relative to the boundary term. In the Airy window, $`J_\rho=O(\rho^{-1/3})`$ and $`J_\rho'=O(\rho^{-2/3})`$, so the first derivative correction is generally $`O(\rho^{-1/3})`$ relative to the leading term, away from its zeros. A uniform relative estimate is unavailable at those zeros. The absolute remainder actually displayed in (8.6), $`O(\rho^{-p_D-1/3})`$, is consistent with the correct counting.
- **Suggested fix:** Replace the quoted relative order with an absolute remainder estimate, justified by another integration by parts or an equivalent oscillatory-integral estimate. This preserves (8.6) and its front-speed conclusion.

## Focus points

None given.
