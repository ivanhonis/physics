# External verification: 10-loop-data

- **Subproject:** 03-ilang-space
- **Package:** 10-loop-data
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-08T16:56:20+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The overlap expansion, loop-phase signs, metric bound, vanishing cases, and examples are correctly derived. The derivation answers all requested items and carefully controls the small-$`\lambda`$ phase branch. Two minor qualifications are needed: the geometric interpretation of saturation excludes a degenerate case, and one consistency check presents a leading-order equality as exact.

## Issues

### I1. Saturation reformulation needs a nondegeneracy qualification
- **Location:** Step 5(iii), discussion following Eq. (10.14).
- **Severity:** minor
- **Problem:** Equation (10.14) correctly includes $`v=u_{h_2}-u_{h_1}=0`$. However, its subsequent reformulation as the two conditions $`g(v,w)=0`$ and $`w\in\mathbb Cv`$ is equivalent only when $`v\neq0`$. If $`v=0`$ and $`w\neq0`$, the leading-order bound is trivially saturated, but $`w\notin\mathbb Cv=\{0\}`$. Such coincident record vectors are permitted by the setting.
- **Suggested fix:** Explicitly restrict the two-condition interpretation to $`v\neq0`$, retaining $`v=0`$ as the separate trivial saturation case already included in (10.14).

### I2. Leading-order saturation is written as an exact phase equality
- **Location:** Consistency check 3, final sentence.
- **Severity:** minor
- **Problem:** The statement that the unit triangle “gives $`\lvert\Phi\rvert=\lambda^2`$” is not exact. The preceding consistency check establishes
  ```math
  |\Phi|=\arctan(\tan^2\lambda)
  =\lambda^2+\frac23\lambda^4+O(\lambda^6)
  ```
  near zero. Saturation concerns only the leading $`\lambda^2`$ coefficient.
- **Suggested fix:** Write $`\lvert\Phi\rvert=\lambda^2+O(\lambda^4)`$, or explicitly state that the leading coefficient saturates the bound.

## Focus points

None given.
