# External verification: 04-branch-fall

- **Subproject:** 05-ilang-free-fall
- **Package:** 04-branch-fall
- **Verified version:** v2
- **External round:** 1 of 2
- **Date:** 2026-10-10T22:37:05+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The first-order branch dynamics, drift acceleration, and level-independence conditions are consistently derived. The revised sharp-label analysis correctly exposes the dependence on the phase structure of the start and distinguishes it from the family-independent drift limit. The clock-rate relation and variant table follow from the stated inputs and approximations. One estimate concerning corrections beyond first order omits a term and needs a clearer range of validity; this does not affect the principal first-order results.

## Issues

### I1. Second-order window correction omits a constant term
- **Location:** Step 3, paragraph immediately following Eq. (4.9)
- **Severity:** minor
- **Problem:** The claimed window-acceleration correction $`O(\tau L^2\mathsf b'^2\lambda)`$ does not follow from (4.9) over the stated range. For a window $`[0,\lambda]`$, dividing that bound by $`\lambda`$ retains both terms:
  ```math
  2\tau L^2\mathsf b'\bigl(\lambda\mathsf b'+|g_\zeta|\bigr).
  ```
  The omitted contribution can genuinely remain nonzero as the window shrinks. For example, with $`G=\mathcal F=0`$, away from boundary terms the quadratic acceleration operator is
  ```math
  i[C_1,\hat v_1]=\tau^2g_\zeta^2\hat x.
  ```
  Thus a translated branch start with nonzero mean position has a nonzero second-order acceleration already at $`\lambda=0`$. The quoted $`O(\lambda)`$ estimate therefore requires additional large-window restrictions and is not an all-window correction estimate.
- **Suggested fix:** Retain the $`O(\tau L^2\mathsf b'|g_\zeta|)`$ term for windows starting at zero. For general windows, give the endpoint bound obtained from (4.9), or derive a separate acceleration-remainder bound. If the existing estimate is intended only asymptotically for long windows, state that restriction explicitly.

## Focus points

None given.
