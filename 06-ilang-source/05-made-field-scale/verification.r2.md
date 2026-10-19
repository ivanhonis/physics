# External verification: 05-made-field-scale

- **Subproject:** 06-ilang-source
- **Package:** 05-made-field-scale
- **Verified version:** v2
- **External round:** 2 of 3
- **Date:** 2026-10-19T12:01:13+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The effective-contract calculation, reduced-view error estimate, R3 test, and lowest-state response are consistent. The derivation also correctly distinguishes rest-and-clock scaling from whole-contract scaling and separates graph separation from recorded distance. The main omission is an explicit momentum-width and branch-control regime for applying the point-rest acceleration formula to localized starts; the stated spatial linearity condition alone is insufficient.

## Issues

### I1. Packet and branch-control conditions are not explicit
- **Location:** Setup assumption S6; Step 4, Eq. (5.7); Result entry for Eq. (5.7)
- **Severity:** minor
- **Problem:** S6 controls the spatial variation of the profile across a start, but does not specify the momentum width or the control of transitions between branches. A localized packet with mean momentum zero need not have the acceleration obtained by evaluating the band dynamics at $`p=0`$: averaging over nonzero momenta generally introduces level-dependent corrections through the band dispersion. Consequently, the claim for every level and every start satisfying the written S6 conditions needs an additional packet approximation. Referring to the “conditions of (4.16)” does not make this explicit, since the quoted input does not state those quantitative conditions.
- **Suggested fix:** State the narrow-momentum and branch-following conditions used in applying (4.16), together with the associated errors. For example, identify the required smallness of the momentum spread relative to both the lattice scale and the local gap-to-hopping ratio, and specify the gradient-to-gap condition controlling branch mixing. Qualify the universality claim by these errors, or quote the precise inherited start class and bounds that already supply them.

## Focus points

None given.
