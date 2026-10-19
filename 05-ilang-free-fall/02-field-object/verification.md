# External verification: 02-field-object

- **Subproject:** 05-ilang-free-fall
- **Package:** 02-field-object
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-10T18:39:42+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The tensor-product evolution, purity criterion, static-field mixtures, and fixed-operator convention analysis are largely mathematically correct. However, the derivation treats effective reduced generators as admissible Ilanguage descriptions without checking A5: when the field is removed and no other objects remain, a nonzero contract cannot generally be realized. The claimed classification of all reduced contracts also omits the pairwise restriction. Some statements about the leading purity-loss order need qualification for starts whose displayed coefficient vanishes.

## Issues

### I1. Reduced description need not be admissible when r is empty
- **Location:** Steps 2, 4, 6 and 8; Results for items 1b and 5b
- **Severity:** major
- **Problem:** A5 permits only contracts between distinct objects; a single-object term can be booked into a pair term only when another object exists. Thus, after removing the field with $`r=\emptyset`$, the displayed $`C_{\rm red}`$ is an effective generator but generally not an admissible contract for the remaining singleton description. This invalidates the unconditional “yes” in Step 2. For example, take a two-place body, $`B_1=\sigma_1`$, $`\Phi_1=\mathbb 1_f`$, $`C_{br}=C_f=0`$, and $`r=\emptyset`$. The full body–field pair term is admissible and the field is sharp and stationary. Starting the body in $`\lvert0\rangle`$, its place-1 reading probability is $`\sin^2\lambda`$. A description containing only the body has no allowed pair contracts, hence $`C=0`$, and cannot reproduce those statistics.
- **Suggested fix:** Distinguish an exact effective reduced generator from an admissible reduced description. Establish admissibility when at least two objects remain; for $`r=\emptyset`$, determine whether the zero contract reproduces the schedules and otherwise report that no reduced description with the stipulated object list exists. Apply the same distinction to the body-alone reductions in Step 8.

### I2. Classification of reduced contracts omits A5
- **Location:** Step 2, Eq. (2.7)
- **Severity:** minor
- **Problem:** Equation (2.7) correctly characterizes schedule-equivalent self-adjoint generators, but not necessarily admissible Ilanguage contracts. An arbitrary diagonal commuting $`\Delta`$ can contain irreducible terms acting on three or more objects. For example, with three remaining two-place objects and $`C_{\rm red}=0`$, $`\Delta=Z_b\otimes Z_{r_1}\otimes Z_{r_2}`$ satisfies (2.7) and leaves all stated reading statistics unchanged, but cannot be expressed as a sum of A5 pair terms.
- **Suggested fix:** State the classification first at the generator level, and restrict the admissible contracts to those members for which $`C_{\rm red}+\Delta`$ has an allowed pairwise decomposition.

### I3. Possible purity-loss order is sometimes stated as an actual leading order
- **Location:** Step 5, sentences following Eq. (2.14); Result for item 2b
- **Severity:** minor
- **Problem:** The expansion gives the first candidate order determined by the field, not necessarily the actual leading order for every body start. The coefficient can vanish for a particular $`\Psi_{br}`$, even when the field criterion fails. For example, use the field in (2.13), $`B_1=\beta\sigma_3`$, $`C_{br}=0`$, and a body start that is an eigenvector of $`\sigma_3`$. The full state remains a product for all $`\lambda`$, so there is no purity loss at any order. Likewise, the unqualified statement that a non-sharp field “starts at $`\lambda^2`$” is not valid for every start.
- **Suggested fix:** Consistently call these the lowest possible or first candidate powers. State that, under LI, the displayed coefficient is attained nontrivially by some start, while a particular start may have a higher leading order or no purity loss.

## Focus points

None given.
