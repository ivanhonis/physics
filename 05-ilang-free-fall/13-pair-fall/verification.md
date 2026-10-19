# External verification: 13-pair-fall

- **Subproject:** 05-ilang-free-fall
- **Package:** 13-pair-fall
- **Verified version:** v3
- **External round:** 1 of 3
- **Date:** 2026-10-11T20:48:35+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The first-order velocity calculation and the resulting drift coefficients are consistent with the quoted inputs, and the numerical evolution supports those coefficients. However, the derivation expressly leaves unresolved part of the limit-commutation question required by item 2(c), including the bound pairs at rest used in items 3 and 4. There are also minor problems with a multiplicative remainder at cancelling gradients, the justification of the clock-response remainder, and an unsupported numerical relaxation claim.

## Issues

### I1. Required limit-commutation statement is left unresolved
- **Location:** Step 5.3; Result, item 2(c); Open issues, second bullet
- **Severity:** major
- **Problem:** Item 2(c) requires a statement about whether the two limits commute on the reported sequence class. The amendment exempts evaluation of the quantity obtained in the other order, not the determination of its existence or commutativity. The derivation instead gives a sufficient condition for failure and explicitly decides nothing when fᵢ vanishes for every window, including every diagonal on-site bound level at P₀ = 0 used subsequently. Moreover, vanishing at P₀ does not remove the phase-sensitive obstruction on the unrestricted class S(P₀, I): packet phases can vary increasingly rapidly while preserving the mean and variance of |g|², and can amplify a nonzero window kernel arbitrarily close to P₀. Thus the pointwise condition fᵢ(P₀) = 0 does not settle these exceptional cases.
- **Suggested fix:** Complete the existence and commutation analysis for the stated sequence class, including the fᵢ(P₀) = 0 members. Use the full phase-dependent fixed-window functional, rather than only its response to a constant spatial shift. The identically zero-gradient member can immediately be settled: both iterated limits are zero and commute.

### I2. Multiplicative remainder fails when the leading numerator cancels
- **Location:** Step 6.5, Eq. (13.16)
- **Severity:** minor
- **Problem:** Equation (13.16) writes the entire acceleration as the leading numerator multiplied by $`1+O(\epsilon^2)`$, without excluding a vanishing numerator. This does not follow from (13.13), whose individual gradient coefficients have different corrections. For example, using the supplied S2 coefficients with $`\kappa\langle X\rangle=0`$ and $`g_2=-0.8g_1`$, the leading numerator $`g_1M_1+g_2M_2`$ vanishes, whereas the numerical exact drift coefficient is
  ```math
  \frac{a_{\rm pair}}{g_1}
  =-0.009993906706+0.8(0.012514456790)
  \simeq1.7659\times10^{-5},
  ```
  not zero. This is an allowed higher-order contribution, but the displayed multiplicative remainder incorrectly eliminates it.
- **Suggested fix:** Restrict the multiplicative form to non-cancelling numerators, as already done for (13.15) and (13.19), and give an additive remainder controlled by the sum of the absolute gradient contributions on cancelling members.

### I3. Second-derivative remainder needs an explicit uniform-neighbourhood justification
- **Location:** Step 7.2, remainder of Eq. (13.22); Open issues, seventh bullet
- **Severity:** minor
- **Problem:** The Cauchy estimate is valid if the remainder is holomorphic and $`O(\epsilon^4)`$ on a complex neighbourhood in M₁ and M₂ whose radius is independent of ε. The quoted input states analyticity and a remainder bounded uniformly “near real data,” in the context of the first derivatives producing (11.14); it does not explicitly specify this ε-independent complex neighbourhood. The derivation acknowledges that it is adopting this stronger reading, but nevertheless concludes that no remainder assumption is being made. The numerical scaling checks support the proposed order at the tested data, but cannot establish the required uniform premise. This is an ambiguity rather than a demonstrated failure of the estimate.
- **Suggested fix:** Confirm that the quoted upstream premise includes the stated ε-independent holomorphic neighbourhood in M₁ and M₂, or supply the local uniform estimate needed here. Until then, identify the second-derivative remainder and the results depending on its values as conditional on that interpretation.

### I4. Numerical relaxation is claimed without supporting evidence
- **Location:** Step 4.4; Code, item 2b
- **Severity:** minor
- **Problem:** The supplied computation establishes bounded first-order separation over its finite evolution range and a small smoothly weighted slope. It does not establish relaxation to a constant. For example, S1 with g₁ only still has substantial half-window separation slopes and an endpoint different from its observed maximum; a small full-window slope can result from averaging oscillations. The analytic result (13.10) proves boundedness under the stated symmetry, not convergence, and finite-chain unitary evolution generally retains recurrences.
- **Suggested fix:** Replace “relaxes to a constant/non-zero value” by the supported finite-range boundedness statement, unless an asymptotic argument establishing convergence in the specified long-chain limit is supplied.

## Focus points

None given.
