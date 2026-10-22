# External verification: 07-inertia-of-pair-full-grip

- **Subproject:** 07-ilang-weight
- **Package:** 07-inertia-of-pair-full-grip
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-21T18:03:45+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The derivation gives a plausible leading-order explanation for the mutual term entering both bodies’ inertias, and the curvature calculations provide useful partial support. However, the stated band regime omits a potentially resonant joint branch flip, and the hierarchy used to suppress the lattice contribution is insufficient for the full parameter class. The weight-to-inertia conclusions also require additional restrictions on the source position. Consequently, the principal conclusions are not established throughout the claimed scope, and the required numerical check of the selected bound level’s weight is incomplete.

## Issues

### I1. Missing joint-flip gap in the band regime
- **Location:** Setup S2; Step 2, band-contract reduction
- **Severity:** major
- **Problem:** The stated distance $`d`$ includes single-body branch flips and field excitations, but not the held sector in which both branches are flipped. Its leading separation from the selected sector is $`2n|g_1+g_2|`$, which can be arbitrarily smaller than the listed distances without cancellation of $`\tau_1^2g_2+\tau_2^2g_1`$. For example, $`g_1=-g_2`$ with unequal $`\tau_i`$ avoids the excluded relative-hopping cancellation, yet the selected and jointly flipped held spectra are degenerate: reflection interchanges the locations of the positive and negative sources. Thus S2's formula can report a nonzero distance when the proposed group is not isolated. The quoted single-group Schrieffer–Wolff reduction is then unjustified.
- **Suggested fix:** Determine the distance to all relevant held sectors, including the joint flip, using the actual held spectra. State the additional nonresonance condition needed for the scalar band contract, and do not apply that contract where the selected group is degenerate with the jointly flipped sector.

### I2. S5 does not ensure that the mutual contribution dominates
- **Location:** Setup S5; Step 4, Eq. (7.8); Step 5, Eq. (7.12)
- **Severity:** major
- **Problem:** The implication $`1-\beta_0\ll\eta\Rightarrow |D^{\rm lat}|\ll|D^{\rm mark}|`$ requires restrictions on parameter ratios that are not stated. For example, take positive $`g_i`$ and equal $`\tau_i`$, and write $`\eta_i=g_i\ell_0/t_f`$. In the broad, localized-pair regime, the displayed formulas themselves give
  ```math
  \frac{|D^{\rm lat}|}{|D^{\rm mark}|}
  \simeq
  \frac{1-\beta_0}{\beta_0}
  \frac{\eta_1+\eta_2}{4\eta_1\eta_2}.
  ```
  When $`g_2\ll g_1`$, domination requires $`1-\beta_0\ll\eta_2`$, not merely $`1-\beta_0\ll\eta=\eta_1`$. Such unequal couplings are allowed and involve neither excluded cancellation. Therefore S5 can hold while the lattice term dominates, invalidating the subsequent leading-order identification of $`D_0`$ with the mutual contribution.
- **Suggested fix:** Replace S5 by an explicit comparison,
  ```math
  |\mu_1+\mu_2|(1-\beta_0)
  \ll |B(0)|(\tau_1^{-2}+\tau_2^{-2}),
  ```
  with the appropriate $`\beta_0`$ factors, or state sufficient comparability assumptions on the couplings and speeds. Check all omitted terms against this actual mutual scale.

### I3. The source-position regime is insufficient for the bond fall factor
- **Location:** Setup S6; Step 5, Eqs. (7.10)–(7.12)
- **Severity:** major
- **Problem:** Equation (7.10) retains the contribution $`\langle V\rangle_0`$, but Eq. (7.12) drops it relative to $`2\kappa_sB(0)`$ with an error written as $`O(w/L)`$. Since $`\langle V\rangle_0/B(0)=O(w/L)`$, its relative size in this comparison is actually $`O(w/(\kappa_sL))`$. S6 allows positions close to the antipode, where $`\kappa_s`$ is arbitrarily small, so this term can dominate or change the sign of the bond weight. Moreover, the displayed $`O(\eta/\kappa_s)`$ error is not small under S1–S6 alone. At $`s=L/2`$, $`\phi'=0`$, and the quoted ratios of fall factors are undefined without a limiting prescription.
- **Suggested fix:** Impose the source-position hierarchy needed for the claimed approximation, including $`\eta\ll\kappa_s`$ and $`w/L\ll\kappa_s`$, and exclude zero-gradient positions when taking ratios. Otherwise retain $`\langle V\rangle_0`$ and state conclusions using absolute, rather than uncontrolled relative, errors.

### I4. The inertia remainder loses its dependence on small β₀
- **Location:** Step 3, Eq. (7.5); Result, Eq. (7.5)
- **Severity:** minor
- **Problem:** S1–S4 allow strongly localized pairs with $`\beta_0\ll1`$, but the remainder in Eq. (7.5) has no corresponding amplification. The preceding local-inertia approximation has errors of order $`O(|\mu_i|\eta^2)`$. Inverting
  ```math
  E''_{\rm line}=\sum_\rho b_0(\rho)/m(\rho)
  ```
  generally amplifies a constant local-inertia error by $`1/\beta_0`$: a shift $`m\mapsto m+e`$ changes the inverse curvature by $`e/\beta_0`$. The quoted input (6.8) explicitly retains such $`\beta_0`$-dependent error factors. No argument is given for removing them here.
- **Suggested fix:** Restore the appropriate $`\beta_0`$-dependent remainder bounds, or restrict the stated estimate to a regime with $`\beta_0`$ bounded away from zero. If a cancellation removes this amplification, demonstrate it for the omitted local-inertia terms.

### I5. Unequal speeds do not exclude equality with either individual fall factor
- **Location:** Step 5, paragraph following Eq. (7.12)
- **Severity:** minor
- **Problem:** The statement that $`\Gamma_b\ne\Gamma_i`$ for unequal speeds overlooks the adjustable factor $`\kappa_s`$. The derivation gives
  ```math
  \frac{\Gamma_b}{\Gamma_i}
  \simeq \frac{2\kappa_s}{1+\tau_i^2/\tau_j^2}.
  ```
  If $`\tau_i<\tau_j`$, this equals one at $`\kappa_s=(1+\tau_i^2/\tau_j^2)/2`$, an accessible source position. Unequal speeds exclude a common factor shared by both individual bodies, but not accidental equality with one of them.
- **Suggested fix:** Distinguish equality with either individual body from simultaneous equality with both. Qualify the asserted individual inequality by the source position or by the $`u\to0`$ limit.

### I6. The required selected-level weight check is not performed
- **Location:** Code, run_case weight section; Code findings and Open issues
- **Severity:** major
- **Problem:** The quantities labelled `W0p_exact` and `Wbp_exact` are obtained by averaging exact *held-field* eigenvalues with the unperturbed band eigenvector $`f_0`$. They are not extracted from the source-dependent selected bound level of the moving pair. In particular, the code neither builds the source-dependent kinetic band terms nor checks their eigenvalue contribution; the derivation explicitly acknowledges that the kinetic weight is unchecked. Also, comparisons using `Wbp/(D0-Dlat)` test a modified mark-only ratio, whereas Eq. (7.12) concerns $`\Gamma_b=W_b'/D_0`$. The supplied calculations therefore check only part of item 4, not the requested selected-level weight and fall factor against exact eigenvalues with a held source.
- **Suggested fix:** Perform the source-dependent selected-level eigenvalue check required by the question, including the kinetic contribution and the stated $`\Gamma_b`$. Label the existing quantities as held-field averages, and establish an explicitly controlled mutual-dominated regime rather than relying on cancellation between the sizable corrections in case R.

## Focus points

None given.
