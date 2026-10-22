# External verification: 06-inertia-of-pair

- **Subproject:** 07-ilang-weight
- **Package:** 06-inertia-of-pair
- **Verified version:** v3
- **External round:** 3 of 3
- **Date:** 2026-10-21T09:54:07+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The relative-chain reduction, flux contribution to the curvature, and controlled inverse expansion are largely consistent within their stated domains. However, the claimed control of the order-τ² approximation does not cover nearly cancelling opposite-branch hoppings, and the bound-level classification uses a non-cancellation assumption absent from its advertised class. Item 4 also remains incomplete at the first nonzero order for an explicitly included cancellation case. The numerical checks support the tested same-branch descriptions but do not resolve these analytical gaps.

## Issues

### I1. Fourth-order control is insufficient near cancellation of the relative hopping
- **Location:** Setup B3; Step 3, final paragraph; Steps 4–7
- **Severity:** major
- **Problem:** The asserted curvature error $`O(\tau'^4/(\delta_1^2\delta))`$ does not follow from an operator error of that size. An eigenvalue curvature contains reduced resolvents within the relative-motion band, so its stability also depends on the selected relative-level gap and the relative kinetic scale. For opposite branches, $`\bar\kappa_1+\bar\kappa_2`$ can be arbitrarily small while R, B2 and B3 still hold. This is a genuine problem: already without the field, the relative dispersion contains
  ```math
  \sqrt{M_1^2+\tau_1^2\sin^2p}
  -\sqrt{M_2^2+\tau_2^2\sin^2p}.
  ```
  Tuning $`\tau_1^2/M_1\approx\tau_2^2/M_2`$ suppresses its order-τ² term without generally suppressing its order-τ⁴ term. Weak marks can satisfy B2 while leaving that fourth-order dispersion dominant over the retained relative hopping. B3, which involves β₀ but not this cancellation or the relative-level gap, does not exclude such descriptions.
- **Suggested fix:** Establish a bound on the curvature error using the selected relative-level gap and the relevant momentum derivatives. Add a hierarchy ensuring that omitted relative-motion terms are small compared with the retained relative dispersion, or retain the necessary fourth-order terms in the cancellation regime. Restrict subsequent conclusions accordingly.

### I2. The bound-level classification uses an assumption absent from its class
- **Location:** Setup, Class; Step 2, derivation of Eq. (6.3); Result, Eq. (6.3)
- **Severity:** major
- **Problem:** Item 1 is advertised for R and $`\chi L^3\gg1`$, without B2. Nevertheless, its Perron–Frobenius argument explicitly uses B2 to conclude that every $`t(\rho;0)`$ has the sign of $`\bar t_0`$. The individual estimates $`\kappa_i=\bar\kappa_i(1+O(\varepsilon^2))`$ do not imply this when the two $`\bar\kappa_i`$ have opposite signs and nearly cancel. Their sum can change sign between bonds, invalidating both the asserted globally positive eigenvector and the use of a single uniform-band edge to classify the selected level. At exact cancellation, χ and the stated sign criterion are not defined.
- **Suggested fix:** Apply an explicit relative-hopping non-cancellation condition to item 1 as well, and exclude the zero-hopping case from that classification unless it is treated separately. State Eq. (6.3) only on the class for which its sign argument is established.

### I3. The first nonzero weight and fall comparison are left unresolved for an included case
- **Location:** Step 6, Vanishing first-order weight; Result, Eqs. (6.13)–(6.14); Open issues
- **Severity:** major
- **Problem:** For $`g_1+g_2=0`$, which is inside the stated class and is explicitly represented by set D, the derivation supplies only an $`O(\varepsilon^2g_s)`$ estimate for the weight difference and its curvature product. It expressly leaves their first nonzero coefficient and the applicability of the factorized form of (7.7) undetermined. Thus item 4 is not completed for this part of the class. The numerical factor-of-two discrepancy already shows that the ordinary factorization cannot simply be extended to that order. The unquoted bond function B is not missing model information: the finite field contract is fully specified, and the required coefficient can be derived from it.
- **Suggested fix:** Derive the necessary third-order held-field eigenvalue coefficient, or equivalently the second-order source-weight coefficient, directly from the stated field matrix. Evaluate the resulting bound-level weight difference and distinguish its curvature product from the unprojected instantaneous acceleration where they differ.

### I4. The stated held-spectrum gap formula omits configuration dependence
- **Location:** Step 7, R1 from the held spectra; Step 5, equality family
- **Severity:** minor
- **Problem:** The distances to singly flipped held levels are not generally exactly $`\lvert2\sigma_iR_i-\omega_n^{(i)}\rvert`$, because Rᵢ is defined for a body alone. In the pair, reversing a branch changes the mutual field contribution, and one motion term also changes a body’s position. Moreover, the distance between the entire group $`\mathcal G`$ and another spectral group must account for their configuration-dependent widths. Consequently, the exact assertion that negative branches have distances ≥ 2Rᵢ is unsupported; the qualitative absence of a weak-coupling resonance near the rest gap can still hold with corrections.
- **Suggested fix:** Express the gaps using differences of the actual held-pair eigenvalues at the connected configurations, and account for group widths when asserting a uniform separation. Present the Rᵢ-based formulas and resonance intervals as leading-order estimates with explicit margins.

### I5. The hopping-of-the-field discussion drops single-body corrections at an order retained elsewhere
- **Location:** Step 7, opening paragraph and subsequent scaling conclusions
- **Severity:** minor
- **Problem:** The statement that μᵢ, $`\bar\kappa_i`$, and $`\bar t_0`$ do not depend on t_f “at the orders used” is too strong. Input (2.14) leaves order-γ² corrections to μᵢ, and the isolated-body amplitudes computed by the supplied code include field-dependent corrections at that order. The package retains order-ε² mutual-mark effects elsewhere, so it cannot simultaneously treat all isolated-body quantities as t_f-independent through that order.
- **Suggested fix:** Restrict the stated power laws to leading order in the weak-coupling expansion, treating isolated-body parameters at that accuracy. If second-order t_f dependence is claimed, include the corresponding isolated-body corrections and their effect on β₀ and the comparison terms.

## Focus points

None given.
