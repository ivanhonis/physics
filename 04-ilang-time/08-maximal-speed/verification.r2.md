# External verification: 08-maximal-speed

- **Subproject:** 04-ilang-time
- **Package:** 08-maximal-speed
- **Verified version:** v2
- **External round:** 2 of 2
- **Date:** 2026-10-10T14:14:34+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The replacement family, invariance analysis, speed bounds, and conditions for equal maximal speeds are correctly derived. The moving-clock and inertia comparisons also follow at the stated approximation orders, and the effective-contract construction appropriately resolves the booking dependence of individual body costs. Two limited claims need qualification: momentum concentration does not establish the position-moment assumption used for uniform bounds, and zero diagonal rebooking is sufficient but not necessary to retain the displayed rest eigenvalue.

## Issues

### I1. Momentum concentration does not guarantee a finite position moment
- **Location:** Step 7, part 3, paragraph beginning “The starts of 05 and 06”
- **Severity:** minor
- **Problem:** The quoted inputs specify momentum-concentrated starts, but this alone does not imply that $`\|\hat x_T\phi_T\|`$ is finite or scales as $`|x_T^0|+1/\delta p_T`$. On an infinite chain, finiteness of this moment requires suitable differentiability of the momentum-space amplitude; a narrowly supported amplitude can fail that condition. Consequently, the uniform-limit argument is justified for the explicitly assumed finite-moment starts, but its asserted applicability to the quoted starts is not established.
- **Suggested fix:** Restrict this statement to wavepacket families with a finite, uniformly bounded position moment. To claim the stated $`1/\delta p_T`$ scaling, specify a suitably regular rescaled momentum envelope, or quote an input that supplies it. Retain the stated finite-size-first procedure for other starts.

### I2. Zero diagonal rebooking is not necessary to preserve the rest eigenvalue
- **Location:** Step 9, paragraph following Eq. (8.24)
- **Severity:** minor
- **Problem:** The statement that recovering $`M_k^T`$ as the positive eigenvalue of a displayed body contract “needs $`\alpha^T=0`$” is too strong. For example, choose
  ```math
  \alpha^T_{(x,s,a)}=\delta\,\mathbf 1_{s=2},\qquad 0<\delta<m_T.
  ```
  At plane-wave label zero, the displayed body eigenvalues become $`M_k^T`$ and $`-M_k^T+\delta`$. Thus its positive eigenvalue remains $`M_k^T`$ for every clock level despite nonzero $`\alpha^T`$. The general non-invariance of displayed rest eigenvalues remains correct, but this claimed necessary condition—and the corresponding “displayed description only” wording—is inaccurate.
- **Suggested fix:** Describe $`\alpha^T=0`$ as a sufficient booking that recovers the quoted rest-cost interpretation, not a necessary condition. Preserve the convention-independent formulation using the effective branch gap.

## Focus points

None given.
