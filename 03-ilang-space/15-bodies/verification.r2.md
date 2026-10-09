# External verification: 15-bodies

- **Subproject:** 03-ilang-space
- **Package:** 15-bodies
- **Verified version:** v2
- **External round:** 2 of 2
- **Date:** 2026-10-08T16:08:54+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The exact evolution, partial traces, leading-order overlap expansion, and cyclic-subspace criterion are correct. The split and label invariance arguments, configuration-distinguishability condition, and both examples are also sound. Two isolated statements overstate what the medium determines; they conflict with qualifications and counterexamples correctly given elsewhere in the derivation.

## Issues

### I1. Instantaneous recoverability claims overlook constant-distance cases
- **Location:** Step 7, “Leading order, orbit and instantaneous state,” item 3; Result, “Line” bullet.
- **Severity:** minor
- **Problem:** Step 7 states without qualification that the configuration and $`D`$ are not functions of the instantaneous medium state at every $`\lambda`$. The Result’s line summary similarly says “but not at every $`\lambda`$” for all its positive cases, including $`c_T=-1,\ n=2`$. In that case there is only one configuration, so both the configuration and $`D`$ are functions of the medium state at every $`\lambda`$, as Step 8 correctly acknowledges. More generally, failure to recover the configuration does not imply failure to recover $`D`$: in the fermionic window example with $`m=1`$, $`D=\sqrt2`$ is constant across all configurations and remains recoverable even at complete revivals.
- **Suggested fix:** Use “not necessarily functions … at every $`\lambda`$” and distinguish configuration recovery from distance recovery. Preserve explicitly the singleton-configuration and constant-$`D`$ exceptions already identified in Steps 8 and 9.

### I2. The full-view discussion still implies that the medium generally encodes $`D`$
- **Location:** Step 5, final sentence: “The medium carries $`D`$ in a different form, through the pair vector $`s`$.”
- **Severity:** minor
- **Problem:** This unqualified statement is false in general. The medium’s leading-order state records the pair-vector sum, which need not determine $`D`$. For example, the symmetric line configurations $`\{h_1,h_3\}`$ and $`\{h_2,h_2\}`$ have the same pair vector and identical medium states for every $`\lambda`$, but distances $`2\sigma_X`$ and $`0`$. Steps 7 and 8 correctly establish this limitation, so the sentence creates an internal inconsistency rather than a computational error.
- **Suggested fix:** State that the medium records the pair vector $`s`$, and that this determines $`D`$ only when $`D`$ is constant on each realizable fibre of the pair-sum map, as explained in Step 7.

## Focus points

None given.
