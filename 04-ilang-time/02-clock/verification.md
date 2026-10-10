# External verification: 02-clock

- **Subproject:** 04-ilang-time
- **Package:** 02-clock
- **Verified version:** v2
- **External round:** 1 of 2
- **Date:** 2026-10-10T06:50:21+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The spectral calculations, classification of ring-clock generators, two-reading criterion—including the N = 3 example—and resolution bound are correct. Two qualifications remain: the general clock-reading claims need admissibility and label-independence conditions, and the Result section omits the stationary exception when summarizing indexing intervals. Neither issue changes the calculations for admissible, label-independent clocks.

## Issues

### I1. General clock-reading claims need admissibility qualifications
- **Location:** Steps 1–3, especially Eq. (2.6); Setup assumption S2; Open issues
- **Severity:** minor
- **Problem:** S2 correctly qualifies the sequential-reading results, but the earlier clock-reading claims remain unrestricted. A place partition does not necessarily define an admissibility-preserving reading when identical-type instances are involved. For example, for two identical invariant-family objects in the admissible state $`\lvert v\rangle\otimes\lvert v\rangle`$, with both place amplitudes of $`v`$ nonzero, reading one object's place and obtaining $`0`$ produces $`\lvert0\rangle\otimes\lvert v\rangle`$, which violates (1.11). Equality of the two singleton views, as noted after (2.3), establishes label-independent statistics but does not establish a permissible reading operation. Thus (2.4)–(2.6) remain valid as formal distribution formulas, but identifying every ticking place distribution with an available clock reading needs an additional qualification.
- **Suggested fix:** Explicitly condition the clock/readability conclusions on a label-independent part and admissibility-preserving reading projectors. For ring clocks, propagate the sufficient restriction that no object of $`R`$ has the clock's type beyond item 4. For more general parts, distinguish the formal place distribution from a reading compatible with A3, A6 and M6.

### I2. Result summary omits stationary views
- **Location:** Result, bullet summarizing Eqs. (2.7)–(2.8)
- **Severity:** minor
- **Problem:** The statement “Otherwise the maximal indexing intervals are half-open of length $`\tau=2\pi/\omega_*`$” also includes the stationary case $`[C_K,V_0]=0`$. In that case $`\omega_*`$ is undefined, the recurrence group is $`\mathbb R`$, and no interval of positive length is indexed. Step 3 handles this correctly; the summary does not.
- **Suggested fix:** Restrict the half-open-interval statement to nonstationary views with commensurate active gaps, and separately state the stationary exception.

## Focus points

None given.
