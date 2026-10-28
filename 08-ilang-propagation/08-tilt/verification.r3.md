# External verification: 08-tilt

- **Subproject:** 08-ilang-propagation
- **Package:** 08-tilt
- **Verified version:** v4
- **External round:** 3 of 3
- **Date:** 2026-10-26T18:18:27+01:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The quadratic expansion, static source response, cubic-lattice spin reduction, and principal distance-decay laws are internally consistent. The supplied code supports the stated finite-cluster and Gaussian checks, within the limitations acknowledged in the derivation. Some qualifications remain necessary: the collective-mode estimate is not uniform in push strength, the dynamical argument does not cover the ring as written, and one cancellation claim for general R1 sources is incorrect. The without-push classification also leaves an explicitly requested corner unresolved.

## Issues

### I1. Collective-mode estimate omits relaxation near the push
- **Location:** Step 4, Zero modes; Eq. (8.6) and the discussion following Eq. (8.7)
- **Severity:** minor
- **Problem:** The estimate using potential weight $`h_p/N`$ treats the collective rotation as spatially uniform. At fixed, non-small $`\eta`$, the field can relax near the pushed cell, changing the leading collective restoring coefficient. On a large cubic torus, the static inverse already displayed in the derivation gives
  ```math
  h_{\rm eff}
  =\left(\frac1{h_p}+\frac{\gamma_3}{JS}\right)^{-1}.
  ```
  Consequently, the leading collective contribution far from the push contains
  ```math
  \frac12\sqrt{\frac{2zJS}{N h_{\rm eff}}},
  ```
  rather than the expression with $`h_p`$, unless $`\eta\gamma_3\ll1`$. The missing factor $`\sqrt{1+\eta\gamma_3}`$ does not disappear as $`L`$ increases at fixed $`\eta`$. This does not change the thermodynamic limit in (8.7), and the fixed-$`h_p`$, large-$`S`$ estimate remains valid at its stated leading order.
- **Suggested fix:** Restrict the displayed collective-mode estimate to weak $`\eta`$, or include the relaxed restoring coefficient and distinguish it from the thermodynamic bulk correction.

### I2. Dynamical identification is justified only in three dimensions
- **Location:** Step 6, Range for dynamics; Result, Eq. (8.10)
- **Severity:** minor
- **Problem:** The dynamical proof uses $`a(0)=\gamma_3/(JS)`$ and convergence of the integral defining $`b(\nu)/\nu`$. These are explicitly three-dimensional properties. On the ring, $`a(\nu)`$ diverges as $`1/|\nu|`$, while $`b(\nu)`$ approaches a quantity proportional to $`{\rm sgn}(\nu)/(JS)`$; the displayed argument involving finite $`a(0)`$ therefore does not apply. The surrounding identification and result are not restricted to the cubic graph.
- **Suggested fix:** Restrict this dynamical justification to $`D=3`$, or supply the ring’s small-frequency estimates and repeat the relative-error bound there. The ring asymptotics appear compatible with the claimed conclusion, but they must actually be used.

### I3. R1 off-diagonal cancellation condition is too restrictive
- **Location:** Step 12(ii), Off-diagonal part, following Eq. (8.18)
- **Severity:** minor
- **Problem:** The statement that the added term is nonzero only when $`{\rm sgn}(\sigma_1)={\rm sgn}(\sigma_2)`$ and $`\epsilon_{x_1}=\epsilon_{x_2}`$ is false for unequal impurity gaps. Writing $`K_i=a_i\mathbb1+b_i\varepsilon`$, the displayed kernel gives
  ```math
  \frac{b_i}{a_i}
  ={\rm sgn}(\sigma_i)\epsilon_{x_i}\frac{\Delta_i}{\nu}.
  ```
  Thus, for equal sublattices and opposite signs of $`\sigma_i`$, $`a_1b_2+a_2b_1`$ generally remains nonzero when $`\Delta_1\ne\Delta_2`$. The code tests equal gaps and equal signs, so it does not check this general assertion. The leading $`r^{-5}`$ conclusion is unaffected, but the stated correction and crossover qualifications are not general.
- **Suggested fix:** State the actual cancellation condition in terms of the signed gaps, or explicitly restrict that discussion to equal gaps. Also qualify relative-error statements near zeros of the leading crossover function, where an absolute error bound is required.

### I4. Without-push classification remains incomplete for allowed sources
- **Location:** Step 13, following Eq. (8.19); Open issues
- **Severity:** minor
- **Problem:** The derivation explicitly leaves non-parallel direction sources near cancellation unclassified. These sources are included in item 3(c); unlike the smallest-cell thermodynamic question, this case was not designated as one for which an undecided answer is acceptable. The variational functional supplies useful information, but the derivation does not finish determining whether these sources fix the orientation, its remaining degeneracy, or the resulting sign classification of the separation-dependent cost. It also does not explicitly identify the lowest-strength mutual contribution from minimizing the shared orientation, which is generally nonanalytic and separation-independent.
- **Suggested fix:** Complete the classification using the already-derived finite-dimensional orientation functional, and distinguish the shared-orientation contribution to the mutual cost from its $`1/r`$ separation-dependent part.

## Focus points

None given.
