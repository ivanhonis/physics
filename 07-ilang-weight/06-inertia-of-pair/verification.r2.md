# External verification: 06-inertia-of-pair

- **Subproject:** 07-ilang-weight
- **Package:** 06-inertia-of-pair
- **Verified version:** v2
- **External round:** 2 of 3
- **Date:** 2026-10-21T09:27:09+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The sector reduction and the exact curvature identity (6.6) are sound, and the supplied numerical comparisons support that identity with the ring term retained. However, the subsequent inverse-curvature expansion is not controlled throughout the stated class, particularly near sign changes of excited-level curvatures. The weak-binding cost analysis also omits the finite kinetic offset of alternating levels, giving an incorrect equality locus and some incorrect hopping-rate asymptotics. Additional qualifications are needed for the proposed equality family, vanishing leading weights, and alternating states on odd-length relative rings.

## Issues

### I1. Inverse-curvature expansion is uncontrolled near small β
- **Location:** Step 4, Eqs. (6.7)–(6.8), and the discussion of excited-level sign changes
- **Severity:** major
- **Problem:** The inversion leading to (6.8) requires more than B3. Writing $`m(\rho)=m_0+\delta m(\rho)`$, with $`m_0=\mu_1+\mu_2`$, gives
  ```math
  E''_{\rm line}
  =\frac{\beta_\nu}{m_0}
  -\frac{A_\nu}{m_0^2}+\cdots,
  \qquad
  A_\nu=\sum_\rho b_\nu(\rho)\delta m(\rho).
  ```
  Expanding its inverse requires $`|A_\nu|\ll|m_0\beta_\nu|`$. Neither B2 nor B3 implies this: B3 compares $`\beta_\nu`$ only with the discarded motion-order correction, not with the retained, spatially varying mark correction. Near an excited-level zero of $`\beta_\nu`$, $`A_\nu`$ need not vanish. Consequently, the assertion that $`\beta_\nu=0`$ makes $`E''_{\rm line}=0`$ at order $`\tau^2`$, leaving the inertia to order-$`\tau^4`$ terms, is generally false. Nonuniform $`m(\rho)`$ can instead supply a nonzero curvature already within the order-$`\tau^2`$ band contract. Near cancellation of $`\mu_1+\mu_2`$, the claimed uniform order estimates require additional care as well.
- **Suggested fix:** State the missing inverse-expansion condition explicitly, together with the condition controlling $`\delta m/m_0`$, and restrict (6.8) and its consequences to that regime. Outside it, retain $`1/\sum_\rho b_\nu(\rho)/m(\rho)`$ without expansion. Locate curvature zeros using that weighted sum, rather than $`\beta_\nu`$ alone.

### I2. Alternating levels retain a kinetic offset in weak binding
- **Location:** Step 5, Eq. (6.17) and its derivation; Step 7 and Result (6.15)
- **Severity:** major
- **Problem:** The equality-locus calculation uses
  ```math
  |K_\nu|
  =|\bar t_0|\frac{a_\nu}{3}4^{1/3}\chi^{2/3},
  ```
  but this holds only for $`s_\beta=+1`$. For an alternating level,
  ```math
  \beta_\nu=-1+\delta_\nu,\qquad
  K_\nu=2\bar t_0(\beta_\nu-1)
  =-4\bar t_0+2\bar t_0\delta_\nu,
  ```
  where $`\delta_\nu=O(\chi^{2/3})`$. The cost comparison is defined against the single-body levels at $`P=0`$, so this finite offset cannot be discarded. In the alternating case, balancing the leading kinetic and contact terms instead gives
  ```math
  L_\nu^*\simeq24\,|C_K/C_M|\,\chi^{-1},
  ```
  when that balance is applicable, not the stated $`\chi^{-1/3}`$ law. The accompanying weak-binding virial argument using $`K_\nu`$ has the same problem. Likewise, $`D_\nu^{\rm lat}`$ does not fall to zero as $`t_f^{-2/3}`$ for $`s_\beta=-1`$: it approaches $`-2(\mu_1+\mu_2)`$. The code’s equality-locus check covers only $`s_\beta=+1`$, so it does not resolve this error.
- **Suggested fix:** Separate the two signs of $`s_\beta`$ throughout the cost and $`t_f`$-dependence analysis. Keep the alternating-level kinetic offset in the cost convention actually defined in Step 5, and distinguish a quantity’s limiting offset from its $`t_f^{-2/3}`$ correction.

### I3. The proposed equality family lacks sufficient spectral control
- **Location:** Step 5, “An equality inside R and B”
- **Severity:** minor
- **Problem:** The stated inequalities do not establish R for the entire proposed scaling family. At the proposed $`L_0^*`$, the held group has width of order $`M\chi^{2/3}`$, whereas the quoted first field gap is of order $`T\tau^2/M`$. The supplied upper bound on $`\tau/M`$ does not ensure that the former is smaller than the latter. For example, taking $`\tau/M=\varepsilon^2`$ satisfies the stated upper bound but makes the quoted field gap much smaller than the width of $`\mathcal G`$. Since R uses the distance between the complete spectral sets, the field gap alone then provides no lower bound on $`\delta`$. In addition, the fixed-parameter $`O(\varepsilon^3)`$ estimates used earlier have not been made uniform under the simultaneous growth of $`n`$, $`L`$, and $`t_f`$. The leading line-chain check does not establish these missing controls.
- **Suggested fix:** Add and verify a spectral hierarchy for this family—for example, one ensuring that the width of $`\mathcal G`$ stays well below the first excitation threshold—and establish the required uniform remainder estimates. Until then, qualify the full-contract equality example as unverified rather than established.

### I4. Multiplicative fall-factor errors fail when the leading weight cancels
- **Location:** Step 6, Eq. (6.14), and Result (6.14)
- **Severity:** minor
- **Problem:** The general relation in (6.14) is written with a multiplicative $`1+O(\varepsilon)`$ error, although the class allows $`g_1+g_2=0`$, or arbitrarily strong cancellation of that sum. Equation (6.12) supplies an additive $`O(\varepsilon^2g_s)`$ remainder; it cannot be converted uniformly into a relative error when the first-order weight vanishes. For example, equal half-gaps and opposite couplings can give an alternating bound level with zero first-order pair weight, while the second-order held and bond weights generally remain position dependent. A multiplicative correction to the zero leading expression incorrectly excludes that contribution.
- **Suggested fix:** Give the general fall-factor formula with an additive error. Use the relative-error version only under an explicit noncancellation condition. For exactly vanishing leading weight, state separately what is and is not determined at the first nonzero order.

### I5. Strict alternating signs are impossible on some allowed rings
- **Location:** Step 2, Eq. (6.3), and Scope
- **Severity:** minor
- **Problem:** The scope includes $`L\equiv2\pmod4`$, for which each relative ring has an odd number $`L/2`$ of sites. A real eigenvector cannot satisfy $`f_0(r)f_0(r+2)<0`$ on every bond of an odd cycle: multiplying those inequalities contradicts $`\prod_r f_0(r)f_0(r+2)=(\prod_r f_0(r))^2\ge0`$. The alternating gauge therefore cannot globally make this ring unfrustrated, and the stated Perron–Frobenius argument does not establish the strict sign assertion. Localization can make the frustrating bond negligible for energies and curvatures, but not make the global sign statement true.
- **Suggested fix:** State the alternating-sign property only on the localized core, with the remote frustrating bond treated separately. Reserve the global strict sign statement for relative rings of even length.

## Focus points

None given.
