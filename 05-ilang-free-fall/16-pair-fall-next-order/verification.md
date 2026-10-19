# External verification: 16-pair-fall-next-order

- **Subproject:** 05-ilang-free-fall
- **Package:** 16-pair-fall-next-order
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-18T13:22:40+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The requested expansions are algebraically consistent with the quoted inputs and the parameter definitions adopted in the derivation. In particular, the weight–cost difference, the acceleration ratio, and the two exceptional surfaces for the generic wide-pair correction check out. The remaining issue is the explicitly unresolved reconstruction of the inherited notation and regime, which prevents complete verification that these formulas apply to precisely the class claimed.

## Issues

### I1. Inherited parameter conventions and regime remain unverified
- **Location:** Setup and assumptions; Step 1(b); Open issues, first bullet
- **Severity:** minor
- **Problem:** The derivation adopts $`a_i=\tau_i^2/(4M_i)`$, $`a=a_1+a_2`$, and $`u=|w_{11}|/a`$ as a reconstruction of definitions omitted from the question, while leaving their agreement with the source package open. It also never fully specifies $`\mathsf R`$, $`\epsilon`$, or the fixed hatted scaling. The stated power counting suffices for the subsequent algebra, but matching several displayed identities does not by itself verify the inherited conventions or the claimed domain of validity. In particular, Step 1(b) needs the actual parameter dependence of $`u`$ under variation of $`M_i`$ at fixed $`\tau_i`$ and binding, not merely its fixed-$`u`$ power counting.
- **Suggested fix:** Supply and verify the definitions and scaling conventions from the cited packages, including what is held fixed in the mass derivatives. If they agree with those adopted here, the calculated coefficients require no change, and this open issue can be closed.

## Focus points

None given.
