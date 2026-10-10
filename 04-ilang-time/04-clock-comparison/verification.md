# External verification: 04-clock-comparison

- **Subproject:** 04-ilang-time
- **Package:** 04-clock-comparison
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-10T07:41:12+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The propagator, joint statistics, certainty conditions, coincidence probability, and post-reading synchronization formulas are correctly derived. The environment-eigenstate reduction and the coupling classifications also follow under the question’s specified canonical definition of a minimal ring clock. Two ancillary statements need qualification: superposed environment states do not necessarily produce mixed clock views, and the discussion of equal coupling coefficients omits the zero-coupling exception.

## Issues

### I1. Superposed environment states need not give mixed clock views
- **Location:** Open issues, third bullet
- **Severity:** minor
- **Problem:** The assertion that the clock view “is not pure” for environment states that superpose eigenvectors of $`B`$ is too strong. For example, with $`A=0`$, the clock and environment remain unentangled and the clock view remains pure for every $`\lambda`$, regardless of the environment superposition. Even with nonzero coupling, the conditional clock states can coincide up to phase at particular parameter values, leaving a pure view.
- **Suggested fix:** Say that such superpositions can produce entanglement and a mixed clock view, rather than necessarily doing so.

### I2. Equal coupling coefficients have a zero-coupling exception
- **Location:** Step 9, sentence following Eq. (4.18)
- **Severity:** minor
- **Problem:** The statement that equal coefficients $`g_1=g_2`$ suffice only if $`N_1\lambda_{01}=N_2\lambda_{02}`$ omits $`g_1=g_2=0`$. In that case both clocks are uncoupled and the rate ratio is environment-independent for arbitrary $`N_i\lambda_{0i}`$. For a common coefficient $`g`$, the stated condition reduces to $`g(N_1\lambda_{01}-N_2\lambda_{02})=0`$.
- **Suggested fix:** Qualify the sentence by requiring the common coefficient to be nonzero, or explicitly include the zero-coupling alternative.

## Focus points

None given.
