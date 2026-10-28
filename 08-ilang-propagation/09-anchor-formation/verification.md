# External verification: 09-anchor-formation

- **Subproject:** 08-ilang-propagation
- **Package:** 09-anchor-formation
- **Verified version:** v2
- **External round:** 1 of 3
- **Date:** 2026-10-26T16:25:02+01:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The exact finite-size solution, the uniform/place-dependent split, and the recurrence argument are sound, and the supplied code substantially supports those finite-size formulas and the reported oscillation scales. However, the shell-formation result incorrectly applies the mean-value property to arbitrary nonradial shell weights. The all-future formation claims also require uniform asymptotic estimates that are not established for the stated class, and the final transfer of eigenvector-based weighing to the evolving state is not justified.

## Issues

### I1. The shell calculation assumes spherical symmetry that was not imposed
- **Location:** Step 7, Shell subsection; Eq. (9.12); Result item 6
- **Severity:** major
- **Problem:** The allowed function $`\Phi`$ is an arbitrary nonnegative smooth function supported in a shell, not necessarily radial. The mean-value property therefore does not imply the asserted weighted shell sum of $`1/|x-h|`$. Writing $`H=(h-x_s)/\ell`$, the actual continuum image contribution is proportional to
  ```math
  \int \frac{\Phi(z)}{|z-H|}\,d^3z,
  ```
  not $`|H|^{-1}\int\Phi(z)\,d^3z`$. Consequently, the stated $`\theta_a`$, its bounds, and the formation/nonformation conclusions in (9.12) are generally wrong. For example, concentrating $`\Phi`$ near the part of the shell facing the anchor can substantially increase the missing-image fraction.
- **Suggested fix:** Use the actual weighted image integral and retain its dependence on the anchor direction and on $`\Phi`$. Alternatively, explicitly restrict this result to radial $`\Phi`$. Also identify and exclude cases where the weighted static reference vanishes.

### I2. Fixed-ratio asymptotics do not establish the all-future formation criterion
- **Location:** Steps 5–8; Eqs. (9.11) and (9.13); Open issues, first bullet
- **Severity:** major
- **Problem:** The criterion requires the error bound for every $`\lambda\ge\lambda_f`$, whereas the principal calculations establish limits at fixed $`w=c_0\lambda/\rho`$. The required uniform control over the entire subsequent evolution is asserted rather than derived. In particular, the fold-caustic assumption is imported from the pinned comparison problem without establishing its applicability to all propagation directions used here. A blanket fold description is not valid for the cubic dispersion: at $`k=(\pi/2,\pi/2,\pi/2)`$, the Hessian of $`\Omega_k`$ has rank one, hence two null directions rather than a single fold direction. The derivation itself leaves this stationary-phase issue open. Finite-window numerical formation times cannot close this gap.
- **Suggested fix:** Establish bounds uniform over the required future interval, including the actual degenerate stationary points, the low-label front, and the point-spectrum contributions. Until then, distinguish the demonstrated fixed-$`w`$ profiles and finite-window checks from the stronger claims about $`\lambda_{\rm form}`$.

### I3. The claimed infinite-volume long-time limit neglects persistent localized modes
- **Location:** Step 6, paragraph beginning “For D=3, the limit λ→∞”; Step 5, Speeds subsection
- **Severity:** minor
- **Problem:** Step 5 correctly notes that a sufficiently strong anchor produces a localized normal mode above the band. Its contribution is
  ```math
  \frac{\psi_b(x)\psi_b(x_s)}{\nu_b}\cos(\sqrt{\nu_b}\lambda)
  ```
  in $`u`$, and is generically nonzero at fixed source and observation places. Thus the pointwise $`\lambda\to\infty`$ limit asserted in Step 6 does not exist for those members of the class. The exponential smallness at large distances does not make the fixed-place limit exist. The threshold anchor strength also needs separate treatment in the claim about an integrable response kernel.
- **Suggested fix:** State the limit for the continuous-spectrum contribution, or as a suitable mean, and retain the persistent localized oscillation explicitly. Explain separately why it is negligible in the particular large-distance formation limits.

### I4. Static weighing coefficients are transferred to a nonstationary state without justification
- **Location:** Step 1, second bullet; Step 10; Result item 10
- **Severity:** major
- **Problem:** The quoted weighing formulas concern eigenvalue differences of the sourced contract. Preservation of the covariance under a linear displacement does not establish that those eigenvalue-based weighing coefficients describe the evolving displaced state. In particular, $`\Gamma=K_a^{-1}`$ is a static susceptibility, not an equal-time covariance whose dynamical applicability follows from displacement invariance. The noncommuting limits matter here: in three dimensions,
  ```math
  R_\infty(x,x;0)=g_\infty(0)-\frac{g_\infty(x-h)^2}{c_\phi},
  ```
  whereas the limit of the finite-torus static susceptibility is
  ```math
  \lim_{L\to\infty}G_a(x,x)
  =c_\phi+g_\infty(0)-2g_\infty(x-h).
  ```
  Their difference is $`[c_\phi-g_\infty(x-h)]^2/c_\phi`$, which remains nonzero far from the anchor. Controlling missing contributions to place differences of $`\phi_a`$ therefore does not, by itself, justify carrying over the own-mark cost and weighing. More generally, the quenched state's total cost is conserved and is not the sourced lowest eigenvalue.
- **Suggested fix:** Distinguish compatibility of static lowest-eigenvector properties with a separate response property of the same contract from weighing actually realized in the evolving state. Remove the latter inference unless the relevant dynamical observable and its relation to the quoted static coefficients are established.

### I5. The final coexistence statement omits the conditions on the grip
- **Location:** Step 10; Result item 10; Result class statement
- **Severity:** minor
- **Problem:** The quoted weighing theorem is conditional: it requires square grips with a common $`\hat\beta`$, the applicable stability conditions, and its controlled perturbative regime. Step 10 says that weighing holds in the stated placement limits without explicitly imposing those conditions, while the result's class statement only specifies the oscillator field and anchor. Read literally, the coexistence theorem consequently extends to grips for which the quoted input says weighing fails.
- **Suggested fix:** Include the square-grip, common-parameter, stability, and perturbative-order conditions explicitly in Step 10 and Result item 10.

## Focus points

None given.
