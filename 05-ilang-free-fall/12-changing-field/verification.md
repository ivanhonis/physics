# External verification: 12-changing-field

- **Subproject:** 05-ilang-free-fall
- **Package:** 12-changing-field
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-11T14:31:36+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The first-order reduction to the field expectation γ(λ), the branch-start response kernel, and its fixed-λ sharp-label limit are well supported. However, the stated finite-width validity range is incorrect for acceleration, and the claimed necessary-and-sufficient accuracy criterion measures proximity to the quasistatic response rather than independence between clock levels. The long-run resonance summary also overstates the exclusivity of resonance, and the example omits its allowed zero-coupling case.

## Issues

### I1. Incorrect finite-width validity range for acceleration
- **Location:** Step 6, after Eq. (12.10); Step 9, Result 3(b)
- **Severity:** major
- **Problem:** The statement that (12.9) describes a fixed start whenever $`\lambda\ll\lambda_g=M/[\tau^2(\delta p^2+2\rho_g)]`$ is not valid for acceleration. The acceleration bound (12.10) contains an additional factor growing like $`M\lambda`$, so this range does not even ensure a small bounded error. There is an actual counterexample: for real, narrow Gaussian starts with $`j_g=0`$, driven at $`\gamma(\lambda)=\gamma_1\cos(2M\lambda)`$, expansion of the supplied kernel in the pre-dephasing regime gives an acceleration correction containing
  ```math
  -2\tau^4\gamma_1\,\delta p^2\lambda^2\cos(2M\lambda).
  ```
  At $`\lambda\sim1/(\tau\delta p)`$, this is comparable to the sharp-label acceleration, although $`\lambda/\lambda_g\to0`$. This concerns the first-order coefficient itself, independently of higher orders in $`Y`$.
- **Suggested fix:** Retain the fixed-λ limit, but remove the asserted common time range for velocity and acceleration. A sufficient acceleration-control condition follows directly from (12.10):
  ```math
  (1+4M\lambda)\left(u+\frac{2\tau^2\lambda}{M}\right)
  (\delta p^2+2\rho_g)\ll1.
  ```
  State separate validity conditions for the two rates.

### I2. Accuracy criterion is not equivalent to level independence
- **Location:** Step 10, Eq. (12.16); Step 12; Result bullet for Eq. (12.16)
- **Severity:** major
- **Problem:** Equation (12.16) correctly characterizes
  ```math
  |\mathcal A_{k,\sigma}+\tau^2|\le\delta\tau^2
  ```
  for every level. It does not characterize, as subsequently claimed, whether the responses are level-independent to relative accuracy δ. Responses can be almost equal across levels while sharing a substantial deviation from $`-\tau^2`$. For example, take two levels $`M_0=m`$, $`M_1=m(1+\epsilon)`$, with $`\Omega=m`$, $`\chi=1`$, and the same branch. Their responses differ by $`O(\epsilon\tau^2)`$, but both deviate from $`-\tau^2`$ by approximately $`2\tau^2/3`$. Thus they can agree to accuracy δ when $`\epsilon\ll\delta`$, while failing (12.16). Moreover, the level-dependent $`2M_k`$ terms in (12.12) prevent this frequency-component criterion from establishing equality of the complete acceleration.
- **Suggested fix:** Label (12.16) as the exact criterion for proximity to the quasistatic coefficient, and as only a sufficient universality condition with an explicitly specified tolerance. For an iff statement about agreement between levels, compare the response coefficients pairwise and define the normalization of the relative error. Keep that statement separate from equality of the complete acceleration, including its start-dependent terms.

### I3. Overstated exclusivity of resonance in the long-run limit
- **Location:** Step 9, Result 3(b); Step 12, drift-acceleration row; Result bullet for Eqs. (12.14)–(12.15)
- **Severity:** minor
- **Problem:** The statements that a growing oscillation occurs “only” in the level satisfying $`\Omega=2M_k`$ are too broad for order (II). Equation (12.15) itself gives a secular oscillation for a fixed smooth start at nonresonant frequencies. In particular, for $`0<\Omega<2M`$,
  ```math
  c_g(\Omega)=-\left\langle
  \frac{4M^2\omega'^2}{4\omega^2-\Omega^2}
  \right\rangle_g<0
  ```
  for any nontrivial smooth normalized start. This contribution disappears only after the subsequent sharp-label limit. Above $`2M`$, the claimed disappearance additionally requires the support restriction stated in Step 9; concentration alone does not suffice, as the Open issues section correctly acknowledges.
- **Suggested fix:** Qualify the exclusive-resonance statements by their limit order and sequence class. Distinguish fixed-start secular growth in (12.15) from the subsequent sharp-label limit, and carry the stated support restriction into the summary and result list.

### I4. Zero-coupling exception omitted from the example
- **Location:** Step 11(a), Item 1
- **Severity:** minor
- **Problem:** The question permits $`y=0`$, but the example unconditionally declares the field sharp and not stationary in the package’s defined sense, and declares $`C_{\rm eff}`$ not to be a contract. For $`y=0`$, $`Y=0`$, condition (2.11) holds, $`\gamma(\lambda)=0`$, and $`C_{\rm eff}=C_{br}`$ is an admissible constant contract. The field’s own state can evolve, but the body sees no coupling.
- **Suggested fix:** Restrict those declarations to $`y\neq0`$, and state the trivial $`y=0`$ exception explicitly.

## Focus points

None given.
