# External verification: 03-weight-of-mark

- **Subproject:** 07-ilang-weight
- **Package:** 03-weight-of-mark
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-20T22:39:34+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The finite-graph reduction, rank-one eigenpair, cost formula, and first-order source response are correct. The perturbative coefficients also support the stated generic failure of weight–cost proportionality beyond leading order. Corrections are needed to the regime of the coupling-(a) comparison, some large-distance remainder estimates, and the claimed coverage of the numerical checks.

## Issues

### I1. Coupling-(a) comparison needs an additional density-dependent regime
- **Location:** Setup and assumptions, Regime; Step 6(c), Eq. (3.15); Result
- **Severity:** minor
- **Problem:** The stated condition $`|g_b|\ell_0/t_f\ll1`$ controls the field expansion but does not alone control the weight–cost ratio in (3.15). In particular, $`F^{(a)}`$ is undefined at the allowed value $`1+\gamma n=0`$, where the leading rest and mark costs cancel. More generally, retaining $`\gamma n`$ without expanding it gives an additional contribution
  ```math
  B^{(a)}
  =g_b\frac{[\Theta_D]}{[\delta N]}
  +\frac{\gamma n}{1+\gamma n}\frac{g_b\ell_0}{t_f}
  +O(g_b^2).
  ```
  The omitted contribution is $`O(\gamma^2)`$ at fixed $`n`$, as the derivation formally states, but need not be small compared with the displayed correction throughout the declared regime for arbitrary $`N_f`$.
- **Suggested fix:** Explicitly state that these ratio expansions take $`\gamma\to0`$ at fixed density, and give a practical restriction such as $`|\gamma|n\ll1`$. Alternatively, retain the density-dependent contribution and state the conditions excluding a zero or near-zero cost denominator. Restrict the corresponding distance-dependent claims for coupling (a) accordingly.

### I2. Some large-distance remainder bounds are not uniform in the stated range
- **Location:** Step 5, square-torus asymptotics; Step 6(d), errors after Eq. (3.16); Step 6(e), cubic branch-pair asymptotics
- **Severity:** minor
- **Problem:** Two finite-size contributions are understated:
  - On the square torus, the omitted contribution to $`B`$ involving $`[\ell^{(2)}]/(|X_f|[\ell])`$ is generally of size
    \[
    O\!\left(\eta\,\frac{R^2\log(L/R)}{L^2}\right)
    \]
    for non-cancelling pairs at comparable distances $`R`$, not simply $`O(\eta R^2/L^2)`$.
  - In the cubic branch-pair formula, the exact coefficient contains
    \[
    -\frac{2\ell_0}{t_f^2|X_f|}
      \frac{[\ell^{(2)}]}{[\ell]}.
    \]
    Since $`[\ell^{(2)}]/[\ell]\sim |r||r'|/2`$ for comparable radial separations, its contribution is generally $`O(|r||r'|/L^3)`$. This is not uniformly $`O(L^{-2})`$ throughout $`1\ll |r|,|r'|\ll L`$; distances of order $`L^{3/4}`$ already violate that bound. The leading distance laws remain valid, but the quoted errors are too strong.
- **Suggested fix:** Include the logarithmic square-torus correction and the cubic $`|r||r'|/L^3`$ correction, or narrow the joint distance–size regime to one supporting the stated bounds. Specify that relative-error statements require non-cancelling leading place differences.

### I3. Numerical checks do not fully cover the claimed weight and distance tests
- **Location:** Code, run_graph checks A and D–J; distance_scan; Step 4 and Step 6(d), numerical-check descriptions
- **Severity:** minor
- **Problem:** Check A is the only direct sourced-eigenvalue check, and it uses one positive $`g_b`$, without scanning the two levels and both branches. The subsequent weight and proportionality checks use the one-point eigenvector density rather than differences of the two-point eigenvalues. Moreover, A normalizes its error by the maximum density, so its quoted error is not a relative error on the generally much smaller weight difference. Finally, every distance scan fixes $`r'`$ at the antipode, outside the stated asymptotic regime $`|r'|\ll L`$; those scans therefore do not directly validate the large-distance proportionality errors in that regime.
- **Suggested fix:** Add direct symmetric-source eigenvalue differences for representative levels, both branches and both couplings on the required graph sizes, including a $`\gamma`$ scan. Add distance scans with both separations satisfying $`1\ll |r|,|r'|\ll L`$, and distinguish density-normalized errors from relative errors in weight differences.

## Focus points

None given.
