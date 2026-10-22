# External verification: 08-field-speed

- **Subproject:** 07-ilang-weight
- **Package:** 08-field-speed
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-21T17:40:34+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The one-object reduction, first-order response formulas, and exponential propagation bound are sound, and they support the principal distinction between a ballistic disturbance front and slower formation of the long-range mark. However, the gradual-switching calculation leaves the fixed-contract model, and some of its stated accuracy guarantees are false for the permitted ramps. The harmonic-lattice control also lacks the static lowest state needed for the claimed comparison. Several additional asymptotic and scope claims require correction.

## Issues

### I1. Gradual switching is not implemented within the stated closed model
- **Location:** Setup and assumptions, Source; Step 6
- **Severity:** major
- **Problem:** The derivation explicitly replaces the fixed contract by an externally prescribed $`C(\lambda)`$. This is not an admissible description under A3 and A5, and no autonomous source/controller realization or controlled approximation to one is provided. The question’s switching prescription exposes a conflict with the base formalization; it does not establish that this enlarged evolution is available within it. Consequently, the gradual-switching results are calculations in an extended, externally driven model, not yet results within the requested closed class.
- **Suggested fix:** Supply an autonomous implementation and quantify the approximation to the prescribed ramp, or delimit the gradual-switching results as belonging only to an enlarged formalism and report the corresponding obstruction in the original class.

### I2. The stated value-following time is not a guarantee for the allowed ramps
- **Location:** Step 6, paragraph “The whole field”; Result, Eq. (8.13)
- **Severity:** major
- **Problem:** The sharp “unfollowed-mode” cutoff gives a scaling estimate, not the asserted sufficient inequality
  ```math
  T\ge \frac{4r^2}{\pi^2\varepsilon^2t_f}
  ```
  in $`D=3`$. Its coefficient cannot be independent of $`f`$. For example, the continuum response already derived gives, at the end of the ramp,
  ```math
  \frac{|\delta\rho(r,T)-\delta\rho_{\rm st}^\infty(r)|}
  {|\delta\rho_{\rm st}^\infty(r)|}
  \sim
  \frac{r}{\sqrt{2\pi t_fT}}
  \int_0^1\frac{f'(u)}{\sqrt{1-u}}\,du .
  ```
  The integral can be arbitrarily large for an allowed smooth ramp concentrated near $`u=1`$. Thus the displayed universal time bound can fail even at the ramp endpoint, before considering the maximum deviation during the ramp.
- **Suggested fix:** Derive the accuracy constants from the actual ramp-response kernel. Retain $`T=O_f(r^2/(\varepsilon^2t_f))`$ as a scaling statement unless a valid, explicitly $`f`$-dependent sufficient bound is supplied. Likewise, label the sharp-cutoff estimates in the other dimensions according to the accuracy they actually establish.

### I3. The harmonic control has no static lowest-state mark
- **Location:** Step 7, harmonic-lattice control; Eq. (8.15)
- **Severity:** major
- **Problem:** The untruncated harmonic contract has a free uniform mode. Without the source this mode has no normalizable lowest state; with the single source its contract contains a linear potential and is unbounded below. The expression $`-g_s\Lambda^+/\kappa`$ is therefore a projected stationary solution for the nonzero modes, not the mark in a lowest state of the stated sourced contract. Subtracting the drifting uniform mode does not establish the required static-state comparison. Finite oscillator truncation supplies a lowest eigenvector, but the derivation does not show that this eigenvector lies in the regime where the harmonic equations approximate the finite matrices.
- **Suggested fix:** Give an admissible control with a controlled lowest state and a well-defined static mark, including its uniform-mode treatment and truncation errors. Otherwise restrict the claim to transient nonzero-mode dynamics and withdraw the claimed lowest-state control for static formation.

### I4. The ballistic-time argument uses the continuum asymptotics outside their derived limit
- **Location:** Step 7, argument preceding Eq. (8.14)
- **Severity:** minor
- **Problem:** Equations (8.8)–(8.9) were derived for $`r\to\infty`$ at fixed $`\zeta=r^2/(4t_f\lambda)`$. Step 7 applies them at $`\lambda=Kr/t_f`$, where $`\zeta\to\infty`$ and the relevant stationary wave number remains of order $`1/K`$. Merely choosing a fixed large $`K`$ does not control the quadratic-dispersion approximation: the omitted phase $`t_f\lambda\,O(k^4)`$ grows as $`r/K^3`$. Thus this particular proof of (8.14) is invalid, although the quadratic formation result can support the conclusion by another argument.
- **Suggested fix:** Infer the exclusion of linear formation times using a fixed-$`\zeta`$ time at which the accuracy criterion fails, or provide lattice stationary-phase estimates valid in the ballistic-time regime.

### I5. No uniform perturbative regime is given for the growing scales
- **Location:** Setup and assumptions, Regime; Steps 3–7
- **Severity:** minor
- **Problem:** An $`O(g_s^2)`$ remainder at fixed $`L,\lambda`$ does not control the subsequent limits with $`\lambda\sim r`$, $`\lambda\sim r^2`$, or $`\lambda\to\infty`$. Static perturbation theory is also nonuniform in $`L`$, particularly in $`D=1,2`$, where the first-order local coefficient grows with system size. The text does not explicitly make all these results statements about the derivative at $`g_s=0`$, nor give joint small-coupling conditions ensuring that the finite-$`g_s`$ remainder is smaller than the detection or formation tolerance.
- **Suggested fix:** State the order of the $`g_s`$, distance, size, and duration limits explicitly. Where claims concern an actual small nonzero coupling, give sufficient perturbative conditions relative to the stated accuracy.

### I6. The multidimensional arrival estimate needs a nonvanishing response argument
- **Location:** Step 3, D > 1 front discussion and criterion; Eq. (8.7)
- **Severity:** minor
- **Problem:** The exponential bound establishes absence of early detection. The multidimensional stationary-phase discussion then gives decay orders for individual contributions, but does not establish that their sum reaches the claimed order somewhere in the specified front window. Oscillatory cancellations matter for the density response, and the numerical checks cover axes only. A nonvanishing-window estimate is needed to justify the upper bound on arrival time for all directions claimed in (8.7).
- **Suggested fix:** Give the leading multidimensional front response and show that its maximum over the stated window has the required lower bound, including relevant direction and torus-image cases; alternatively restrict the arrival claim to directions for which this is established.

### I7. The averaging bound is incorrectly described as a formation scale
- **Location:** Step 5, discussion following Eq. (8.11)
- **Severity:** minor
- **Problem:** Equation (8.11) is a valid sufficient upper bound, but the assertion that the slowest modes saturate it up to an order-one factor is not generally true at the quoted threshold. In $`D=3`$, for example, $`r\ll L`$ gives the quoted threshold $`\Lambda\sim Lr/t_f\ll L^2/t_f`$; the slowest-mode sine arguments are then small, so replacing their sines by one is far from saturation. Local formation can instead occur on an $`r^2/t_f`$ scale independent of $`L`$. The displayed $`Lr/t_f`$ expression therefore should not be presented as the actual averaging formation scale.
- **Suggested fix:** Label these expressions as sufficient upper bounds and remove the saturation assertion, unless matching lower bounds are derived in specified regimes.

### I8. The body-speed condition is sufficient, not necessary as stated
- **Location:** Step 8; Eq. (8.17)
- **Severity:** minor
- **Problem:** Comparing the motion-only maximal velocity $`\tau`$ with $`2t_f`$ gives an “if and only if” condition for those two maxima, not for whether an actual Model D body moves more slowly than the field front. The derivation itself notes that the rest term reduces the body’s group velocities. For a level $`m_a>0`$, the full-band maximum is
  ```math
  v_{\max,a}=\sqrt{m_a^2+\tau^2}-m_a,
  ```
  which can be below $`2t_f`$ even when $`\tau>2t_f`$. A particular packet can of course move still more slowly.
- **Suggested fix:** State that $`\tau<2t_f`$ guarantees that all motion-only group velocities, and hence all full-band group velocities, are below the axial front speed. Reserve “iff” for the explicit comparison $`\tau< v_f`$, or use the full-band maximum when discussing a specified body level.

## Focus points

None given.
