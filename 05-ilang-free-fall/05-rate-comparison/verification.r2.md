# External verification: 05-rate-comparison

- **Subproject:** 05-ilang-free-fall
- **Package:** 05-rate-comparison
- **Verified version:** v2
- **External round:** 2 of 2
- **Date:** 2026-10-10T22:50:51+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The central equivalence theorem and its applications to hopping, immobile bodies, and two bodies sharing a medium are sound. The distinction between comparisons within one schedule and comparisons between two runs is also handled correctly. The remaining issues concern an overstrong claim about clock marginals, an unstated parameter-normalization convention, and qualifications needed when discussing ratios for arbitrary advance rules.

## Issues

### I1. Nonconstant position factors can preserve a clock marginal
- **Location:** Step 9(b), first paragraph under Rates from the two runs, wide starts
- **Severity:** minor
- **Problem:** The assertion that a clock reading under $`C'`$ corresponds to a clock reading at one value of the parameter under $`C`$ “only if $`a_x`$ is constant on the support” is too strong if “corresponds” means equality of the reading statistics for the specified start. For example, take equal weights at two occupied positions, $`\eta_0=1`$, $`\eta_1=2`$, and $`a_0=1/2`$, $`a_1=2`$. Equation (5.24) then gives
  ```math
  p^{C'}_{\lambda'}=\tfrac12\pi_{2\lambda'/\lambda_0}
  +\tfrac12\pi_{\lambda'/\lambda_0}
  =p^C_{\lambda'},
  ```
  despite the unequal factors. The necessity claim is valid for a uniform mapping of the position-resolved contributions, or when equality is required for every start, but not generally for one clock marginal.
- **Suggested fix:** Specify that the statement concerns the prescribed event-by-event mapping, or require correspondence for every start. Otherwise state constancy of $`a_x`$ as a sufficient condition and allow accidental equality of clock marginals.

### I2. An invariant example requires a clock-normalization convention
- **Location:** Step 10(c), Equal parameters of two types
- **Severity:** minor
- **Problem:** The list of quantities preserved by (5.20) includes $`\tau^{(i)}\lambda_0^{(i)}`$. This is not invariant for a general body of class $`\mathcal C`$ under the fixed-$`\lambda_0`$ convention K2: one may write the scaled contract with $`\tau'=\tau/a_i`$, $`\eta'_x=\eta_x/a_i`$, and $`\lambda'_0=\lambda_0`$, giving $`\tau'\lambda'_0=\tau\lambda_0/a_i`$. The stated invariant applies when the clock coefficient is held fixed—for example, Model D with its normalized coefficient—or when $`\lambda'_0=a_i\lambda_0`$ is explicitly chosen.
- **Suggested fix:** State the normalization under which this example is invariant. For the general class form, use the convention-independent product $`\tau\lambda_0/\eta_x`$, or its corresponding hopping version.

### I3. Flat-clock rate ratios need an existence qualification
- **Location:** Step 9(b), statement 1; Eq. (5.17); Result, item 4
- **Severity:** minor
- **Problem:** Identical clock statistics guarantee identical advances under the same rule, but do not guarantee that their rate ratio exists. Property (R) alone permits, for example, the rule $`\Theta\equiv0`$, which gives two zero rates and an undefined ratio. Consequently, the statements that the flat description gives ratio $`1`$ “for every rule” are broader than justified. Step 10(c) correctly includes rate-existence and nonzero-denominator qualifications, but Step 9 does not consistently do so.
- **Suggested fix:** Say that the advances and rates are equal, and that the ratio is $`1`$ wherever the common rate exists and is nonzero. Alternatively, explicitly require the advance rule to reproduce the dial advance for uniform clocks.

## Focus points

None given.
