# External verification: 08-typical-or-forced

- **Subproject:** 06-ilang-source
- **Package:** 08-typical-or-forced
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-19T13:11:35+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The Bloch-response formula, the explicit short-range example, and the numerical evaluation of the response are substantially sound under F1. However, the coupling classification uses effects beyond the prescribed first order in γ, and its principal set includes couplings whose two branches fall differently. The field-contract analysis also restricts the requested class F substantially and leaves cases unresolved, so it does not establish the requested classification or genericity statement for that class.

## Issues

### I1. Higher-order effects determine the claimed first-order coupling set
- **Location:** Setup T1; Steps 4, 6 and 7; Eqs. (8.4), (8.6) and (8.7)
- **Severity:** major
- **Problem:** The question specifies first order in γ, but the restriction $`b_k=b_0`$ is inferred from effects of order γ² or higher. At fixed field expectations, the acceleration through the requested order is
  ```math
  a_{k,\sigma}(0)
  =-\tau^2\gamma N'\frac{f_k+\sigma g_k}{M_k}+O(\gamma^2).
  ```
  Thus the hopping coefficients $`b_k`$ do not affect this classification at first order. Likewise, $`h_2`$ affects the fall only beyond first order around the uncoupled body. With R3 and rest at $`p=0`$, the first-order set has $`f_k=\alpha M_k`$, $`g_k=\beta M_k`$, $`h_{2,k}=\eta_2M_k`$, $`h_1=0`$, and unrestricted $`b`$: dimension $`N+3`$, rather than 4, before requiring equality between branches. Keeping $`\gamma N_0`$ unexpanded does not justify using selected higher-order effects to impose necessary conditions while the test-body approximation neglects effects at those orders.
- **Suggested fix:** Give the classification and dimensions at the stipulated order, leaving $`b`$ unrestricted for the fall condition. If retaining the resummed effective-contract result, distinguish it from the first-order answer and provide conditions controlling the omitted effects to the orders used.

### I2. The reported principal set does not give the same fall on both branches
- **Location:** Step 4; Eq. (8.4); Result bullets for Eqs. (8.4) and (8.6)
- **Severity:** major
- **Problem:** Item 1 asks for the fall to be the same for all levels and both branches. The set $`\mathcal S_1`$ permits $`\beta\neq0`$, but its own acceleration formula gives
  ```math
  a_{k,+}(0)-a_{k,-}(0)
  =-\frac{2\tau^2(1+\gamma b_0N_0)^2\gamma\beta N'}{s(N_0)}.
  ```
  Therefore $`\mathcal S_1`$ establishes level independence separately on each branch, not equality across branches. The derivation identifies $`\beta=0`$ later, but does not impose it in the set presented as the answer to the requested condition.
- **Suggested fix:** Impose $`\beta=0`$ in the principal answer and update its dimensions and conditions consistently. Keep the larger, separately level-independent set explicitly distinguished from the requested branch-independent set.

### I3. The field classification and genericity result do not cover class F
- **Location:** Setup F1; Steps 9–12; Result section; Open issues
- **Severity:** major
- **Problem:** Class F requires a unique lowest eigenvector on each finite graph; it does not require F1’s unique, simple, quadratic continuous-zone minimum or its exact commensurability with the momentum grid. Admissible omitted examples include the finite-range scalar ring contract $`h(k)=(2-2\cos k)^2`$, with a unique finite-size lowest state and a quartic minimum, and $`h(k)=2t[1-\cos(k-\theta)]`$ with irrational $`\theta/(2\pi)`$, whose finite-size lowest state is unique but whose continuous minimum is never on the grid. Exact commensurability is not an open condition under the allowed hopping perturbations. Consequently, proving density by varying φ within F1 does not establish an open dense long-range subset of class F. Even within F1, the cases $`\bar\phi=0`$, $`C=cA`$ in dimensions two and three are explicitly left undecided, although the question requests a classification.
- **Suggested fix:** Supply a criterion and analysis covering class F as defined, including the omitted spectral minima and the higher-order cancellation cases. Establish genericity in that full class, with its coefficient topology specified; conclusions proved only under F1 must remain explicitly restricted to F1.

### I4. Perturbative and large-volume error ranges are not specified
- **Location:** Step 8 and Eqs. (8.8)–(8.11); Setup F2
- **Severity:** minor
- **Problem:** The finite-size Taylor coefficient $`\chi_0`$ is well defined, but the remainder in $`N(y)=n\bar\phi-g\chi_0(y,x_s)+O(g^2)`$ has no stated range uniform in L. Under F1 the excitation gap closes as $`L^{-2}`$, so ordinary nondegenerate perturbation theory supplies no L-independent small-coupling regime automatically. The continuum large-distance expressions also require an order of limits, or a condition such as distances much smaller than L; macroscopic distances on a torus have nonconstant finite-size corrections.
- **Suggested fix:** State that the long-range classification concerns Taylor coefficients obtained at $`g=0`$ before taking the volume limit, unless a uniform perturbative bound is supplied. Give a finite-size small-coupling condition and specify the distance-versus-L regime for the continuum asymptotics.

### I5. Numerical agreement is overstated
- **Location:** Steps 10 and 11; output/check_log.txt
- **Severity:** minor
- **Problem:** The quoted tolerances are not all supported by the supplied output. For the long-range torus example, the ratio 0.9783 differs from unity by 2.17%, exceeding the claimed 2%. For the zero-mean example at $`L=32`$, axis 2 and $`d=8`$, the reported values 0.02412 and 0.02569 differ by approximately 6.1% relative to the prediction, exceeding the claimed 5%; several smaller-size comparisons are worse. The direct-diagonalization checks do support Eq. (8.8), but the asymptotic-agreement summaries need qualification.
- **Suggested fix:** Report the actual maximum discrepancies over a clearly specified size and distance window, distinguishing agreement with the finite-size lattice prediction from agreement with the infinite-volume asymptotic expression.

## Focus points

None given.
