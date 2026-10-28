# External verification: 08-tilt

- **Subproject:** 08-ilang-propagation
- **Package:** 08-tilt
- **Verified version:** v2
- **External round:** 1 of 3
- **Date:** 2026-10-26T16:18:07+01:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The finite-volume symmetry results, quadratic expansion, and transverse static response are largely consistent with the stated operators. However, the no-push orientation claim fails for admissible nearly cancelling sources, and the long-distance R1 result relies on a multiplet projection not justified in the stated weak-coupling regime. There are also omissions in the long-wavelength anchor identification, the treatment of general R2 geometries, and some numerical claims. These prevent the package from establishing its full stated conclusions.

## Issues

### I1. Nonzero resultant source does not always select the claimed orientation
- **Location:** Step 13, Eq. (8.19), Result
- **Severity:** major
- **Problem:** The assertion that every nonzero effective field selects $`\hat{\mathbf n}^*=-\mathbf h_{\rm eff}/|\mathbf h_{\rm eff}|`$ is not uniform near cancellation and can give an unstable stationary point. For example, take collinear sources with $`\epsilon_{x_1}=+1`$, $`\epsilon_{x_2}=-1`$, $`g_1=g>0`$, and $`g_2=g(1-t)`$, where $`t>0`$. The proposed orientation gives $`a_1=g`$, $`a_2=-g(1-t)`$. Its displayed reduced quadratic form has determinant
  ```math
  \ell gt-g^2(1-t),
  ```
  which is negative when $`t<g/(\ell+g)`$, despite $`\mathbf h_{\rm eff}=gt\,\mathbf m\ne0`$. This is compatible with arbitrarily weak sources. Thus the claimed orientation, and the consequent absence of a classical $`1/r`$ term for all collinear sources with nonzero resultant, do not hold throughout the stated class.
- **Suggested fix:** State the noncancellation regime required for the first-order orientation selection, check the full positivity criterion, and treat the nearly balanced crossover separately. Restrict Eq. (8.19) to its established regime.

### I2. The R1 multiplet projection is not controlled by the stated hierarchy
- **Location:** Step 12(ii), second line of Eq. (8.18)
- **Severity:** major
- **Problem:** The inference that the pair $`b,x`$ stays in its isolated lowest multiplet merely because $`\nu\ll |g'|S`$ is unjustified. The exchange terms connecting $`x`$ to its neighbours do not preserve that multiplet, and their scale is $`JS`$, while the assumed hierarchy is $`|g'|\ll J`$. Low observation frequency alone does not permit replacing the pair by its isolated-multiplet projection. Consequently, the spin-length-defect vertex, its matching coefficient, and hence the quoted R1 prefactor have not been derived from the actual weakly coupled impurity model. The numerical calculation checks the assumed defect model, not this matching step.
- **Suggested fix:** Derive the low-frequency impurity action in the exchange background, including its antisymmetric response, or supply a controlled power-counting argument showing that the isolated-pair projection gives the retained vertex despite the stated hierarchy. Explicitly state the required scaling of $`s_b`$ with $`S`$.

### I3. A mixed anchor term is missing from the long-wavelength identification
- **Location:** Step 6, long-wavelength identification; Eq. (8.10)
- **Severity:** minor
- **Problem:** Using the smooth-field decomposition subsequently employed in Step 11,
  ```math
  \tilde Q=\phi_1-\epsilon\pi_2,\qquad
  \tilde P=\pi_1+\epsilon\phi_2,
  ```
  the push contains
  ```math
  \frac{h_p}{2}\bigl(\phi_1^2+\phi_2^2+\pi_1^2+\pi_2^2\bigr)_h
  +h_p\epsilon_h(\pi_1\phi_2-\phi_1\pi_2)_h .
  ```
  The identification includes the local kinetic correction but omits the mixed term coupling the two copies. That term is at the same quadratic order in $`1/S`$, and has fewer low-frequency derivatives than the retained kinetic correction. Thus “two independent copies plus a local kinetic term” is not the stated quadratic contract.
- **Suggested fix:** Include the mixed term and explain its effect, or explicitly formulate a lowest-derivative limit in which it and the higher-derivative kinetic correction are both discarded. Keep the exact static identification separate from this dynamical approximation.

### I4. Cell asymptotic remainders require midpoint separations
- **Location:** Step 8, Eq. (8.14); Step 10, Eq. (8.16)
- **Severity:** minor
- **Problem:** The factor $`c_1c_2`$ gives the leading monopole coefficient, but the asserted remainders are not valid for the endpoint-based separation used earlier and arbitrary cell orientations. For example, a single-object source at $`0`$ and a cell at $`(r\mathbf e_1,r\mathbf e_1+\mathbf e_1)`$ give
  ```math
  \hat g(r\mathbf e_1)+\hat g((r+1)\mathbf e_1)
  =\frac{2}{4\pi r}-\frac{1}{4\pi r^2}+O(r^{-3}).
  ```
  Equation (8.14) omits this $`r^{-2}`$ term. Similarly, Eq. (8.16) generally has a relative $`O(r^{-1})`$ correction with such a separation convention.
- **Suggested fix:** Define cell separation using the cell midpoints, including mixed single-object/cell cases, or retain the dipole corrections and weaken the stated remainders.

### I5. General R2 signs and cancellations are not resolved
- **Location:** Step 11, Eq. (8.17), Open issues
- **Severity:** minor
- **Problem:** The question includes arbitrary changed-link sources, but signs are evaluated only for two parallel-link geometries. Other allowed geometries need not have the same sign. For example, the displayed integral itself gives, for mutually perpendicular links with one parallel to the separation,
  ```math
  \mathcal E^{R2}_{12}
  =+\frac{\sqrt3}{16\pi^3}\frac{\delta_1\delta_2S}{Jr^7}
  ```
  at leading order: repulsion for $`\delta_1\delta_2>0`$. The requested identification of vanishing leading coefficients is also absent for general geometries. Providing an unevaluated general integral does not complete the requested sign and cancellation classification.
- **Suggested fix:** Evaluate the angular coefficient for the remaining link geometries and identify its sign-changing and vanishing members, with the applicable separation convention.

### I6. The short-distance R1 remainder remains an unsupported estimate
- **Location:** Step 12(i), first line of Eq. (8.18)
- **Severity:** minor
- **Problem:** The symmetric response is integrated with a useful bound, but the antisymmetric contribution is assigned an $`O(r/\ell_b)`$ remainder only from its size at a typical frequency. That does not bound the full frequency integral, particularly its low-frequency region. The derivation candidly labels this an estimate, but item 3(b) requires a derivation of the retained R1 result and its regime.
- **Suggested fix:** Evaluate the antisymmetric contraction or bound its full frequency integral, including the low-frequency region, before assigning the displayed remainder.

### I7. The ED search does not by itself establish the global ground-state sector
- **Location:** Step 5; ed_push.py, run
- **Severity:** minor
- **Problem:** With the push, the code searches only total-spin-component sectors $`M=0,1,2`$. No argument excludes negative sectors or sectors with $`M>2`$, since full rotational symmetry is then absent. The output therefore establishes the minimum among the searched sectors, not independently the global lowest eigenvector. Also, “for all $`h_p\le10J`$” exceeds the six sampled push strengths.
- **Suggested fix:** Supply a sector-ordering argument applicable with the local push, search all potentially competing sectors, or qualify the numerical statements as restricted-sector results at the sampled strengths.

## Focus points

None given.
