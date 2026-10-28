# External verification: 07-bond-inertia

- **Subproject:** 08-ilang-propagation
- **Package:** 07-bond-inertia
- **Verified version:** v5
- **External round:** 1 of 3
- **Date:** 2026-10-25T15:17:05+01:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The second-order mutual kernel (7.2) is well supported by the supplied matrix-element check, and the algebra leading from the continuum moving-bond expression to (7.10) is consistent under its approximations. However, the fall calculation uses a locally uniform external field in a regime where a distant pinned source does not produce one, and it omits dressing corrections needed to compare the pair with its dressed members. The deep-binding formulas also require an additional restriction on the quadratic grip that is absent from the stated class. There are further problems with perturbative remainder orders and the interpretation of the finite-ring numerical check.

## Issues

### I1. A distant pinned source is not uniform over a shallow pair
- **Location:** Step 9, Eqs. (7.13)–(7.14), and Open issues
- **Severity:** major
- **Problem:** The condition that the pair size is small compared with its distance $`d`$ from the source does not justify the uniform-field approximation used here. On the infinite pinned chain, the continuum profile away from the source is proportional to $`e^{-d/\ell}`$. For two placements symmetric about a midpoint,
  ```math
  \frac{\phi(X+\xi/2)+\phi(X-\xi/2)}{2\phi(X)}
  =\cosh\!\left(\frac{\xi}{2\ell}\right),
  ```
  provided neither placement crosses the source. Thus the midpoint correction is controlled by separation divided by $`\ell`$, not separation divided by $`d`$. Sending the source farther away does not make it approach one. In particular, the shallow regime $`a_b\gg\ell`$ is incompatible with the locally uniform approximation, so its fall criteria and the claimed correction $`O((a_b/d)^2)`$ do not follow for the stipulated distant held source.
- **Suggested fix:** Require the pair’s spatial extent to be small compared with the external profile’s variation length, which here requires $`a_b\ll\ell`$, and replace the stated gradient-error estimate accordingly. Do not apply (7.13)–(7.14) to shallow pairs under this source without retaining the spatial dependence of the source profile throughout the pair.

### I2. Dressed member weights and inertias are replaced by bare quantities
- **Location:** Assumption B, Step 1, Step 7, and Step 9
- **Severity:** major
- **Problem:** The question defines $`I_i`$ from the curvature of each body dressed alone at the same order. Equation (7.1) instead supplies the inertia of the first-order band, and the second-order self-energy curvature is never calculated. Its cancellation from the subtraction defining $`D`$ does not determine the requested $`I_i`$. More importantly, Step 9 uses $`w_i=\mu_iF_1`$ and a common $`w_i/I_i=F_1\tau^2/\bar a`$, although both quantities acquire dressing corrections. These corrections matter at the order at which the binding-induced change in the fall ratio is retained. For example, already in the held, leading-grip limit,
  ```math
  \Sigma_i=-\frac{\mu_i^2F_1^2}{2}G(0),
  \qquad
  \partial_\phi\Sigma_i=-2\mu_i^2F_1F_2G(0),
  ```
  so the dressed weight is not simply $`\mu_iF_1`$. No calculation establishes that the dressed members have a common weight-to-inertia ratio or that these terms cancel from the comparison in (7.13).
- **Suggested fix:** Calculate the single-body self-energy contributions needed for $`E_i(0)`$, $`E_i''(0)`$, and $`\partial_\phi E_i(0)`$, and use the resulting dressed quantities in the comparison. Alternatively, explicitly limit (7.13) to an incremental mutual contribution; it then does not by itself answer whether the pair falls like its dressed members.

### I3. The deep Airy approximation is not valid for every stated quadratic grip
- **Location:** Step 6, Eq. (7.8), and Result entries (7.8), (7.11), and (7.14)
- **Severity:** major
- **Problem:** The deep-binding calculation retains the one-quantum slope
  $`\lambda=\mu_1\mu_2F_1^2/(2c_0^2)`$ and discards the two-quantum contribution, whose relative size is itself given as
  ```math
  \frac{2F_2^2}{\pi F_1^2c_0}\ln\!\frac{\ell}{a_b}.
  ```
  None of assumptions (A)–(E), including $`u\ll1`$, makes this quantity small. Within the stated class, $`F_1`$ can be arbitrarily small relative to $`F_2`$, while both remain perturbatively weak. The two-quantum bond can then dominate confinement, and its $`|\xi|\ln(\ell/|\xi|)`$ dependence cannot be replaced by the linear potential used to obtain the Airy energy, kinetic expectation, and size. The stated deep error estimates consequently do not cover all the claimed grips.
- **Suggested fix:** State the displayed ratio being much smaller than one as an additional condition for the Airy formulas, and delimit the corresponding deep-binding and fall claims. For grips outside that restriction, retain the full second-order potential rather than claiming the same Airy formulas and error orders.

### I4. Cubic terms in the grip expansion are incorrectly omitted
- **Location:** Assumption B and Eqs. (7.3)–(7.4)
- **Severity:** minor
- **Problem:** For a general quadratic grip, the remainder after second-order elimination is not $`O(\delta F^4)`$. Three vertices can give nonzero contributions proportional to $`F_1^2F_2`$ and $`F_2^3`$; Gaussian parity does not remove them. This is visible even for held sources: expanding the exact shifted quadratic problem involves
  ```math
  -\tfrac12 j^{T}(K+2D)^{-1}j,
  ```
  with $`j`$ linear in $`F_1`$ and $`D`$ linear in $`F_2`$, producing a cubic $`j^{T}K^{-1}DK^{-1}j`$ term. Absorbing the first-order tadpole into $`\bar a`$ does not remove these contributions. The separately assumed small parameter $`u`$ can help control them, but does not change their perturbative order.
- **Suggested fix:** Use a general $`O(\delta F^3)`$ remainder and identify the cubic corrections controlled by $`u`$. Reserve the fourth-order statement for the linear-grip case or another explicitly justified scaling.

### I5. The curvature code does not diagonalize the stated finite-ring sectors
- **Location:** Code check (ii), Code section, and check_bound_pair.py, hamiltonian and analyse
- **Severity:** minor
- **Problem:** On a periodic ring, both individual body labels and the joint label must lie on the appropriate $`2\pi/L`$ grid. The code instead chooses arbitrary $`P=h,2h,3h`$ and sets
  $`p_1=(I_1/I)P+2\pi n/L`$, $`p_2=(I_2/I)P-2\pi n/L`$. These are generally not allowed periodic-ring labels. The matrices therefore provide a continuously twisted/interpolated finite-volume family, not exact diagonalizations in sectors of the specified periodic ring. For a localized bound state at large $`L`$, this may approximate the thermodynamic dispersion well, but that distinction and its finite-size error are not established by the supplied outputs.
- **Suggested fix:** Perform the check using allowed joint labels and an allowed individual-momentum grid, or identify the twisted-boundary construction explicitly and demonstrate convergence to the periodic-ring thermodynamic result before describing the numerical check as an exact finite-ring sector calculation.

## Focus points

None given.
