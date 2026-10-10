# External verification: 05-moving-clock

- **Subproject:** 04-ilang-time
- **Package:** 05-moving-clock
- **Verified version:** v2
- **External round:** 2 of 2
- **Date:** 2026-10-10T13:20:15+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The decoupled result, spectral calculation, velocity bound, and first-order clock-reading distribution are consistent with the stated approximations. However, item 4 replaces the velocity specified in the question with a tick-averaged velocity associated with the centre of the clock band. These velocities differ at first order in ε, so this substitution changes the requested rate–velocity relation at the very order being derived.

## Issues

### I1. Rate–velocity relation uses a different velocity from the requested one
- **Location:** Steps 8–9, Eqs. (5.25)–(5.29)
- **Severity:** major
- **Problem:** Item 4 asks for the tick ratio as a function of the velocity from item 2(b), which for clock level $`d_k`$ is
  ```math
  w_k(p_0)=\frac{\tau^2\sin p_0\cos p_0}
  {\sqrt{\mu_k^2+\tau^2\sin^2p_0}},\qquad \mu_k=m+d_k.
  ```
  Instead, Step 8 defines a new, tick-averaged velocity using $`\bar\mu=m+\bar d`$, and Step 9 substitutes that velocity throughout. The derivation itself correctly observes that both a specified level’s velocity and the carried clock’s instantaneous velocity differ from this replacement at first order.

  This is not merely a change of notation. Combining the tick ratio (5.22) with the requested level-$`k`$ velocity gives, near $`p_0=0`$,
  ```math
  R
  =1+\frac{\mu_k^2}{\bar\mu^2}
  \frac{\lVert v_k\rVert^2}{2v_{\max}^2}
  +O(p_0^4),
  ```
  within the same first-order accuracy in ε. For $`k=0`$,
  ```math
  \frac{m^2}{\bar\mu^2}
  =1-(N-1)\epsilon+O(\epsilon^2),
  ```
  so the coefficient differs at first order from the universal $`1/2`$ asserted in (5.28). Likewise, the largest velocity used in Step 9 is evaluated at $`\bar\mu`$, rather than at the level $`\mu_k`$ specified in item 2(b). Equations (5.26)–(5.29) therefore establish relations for the newly introduced averaged velocity, not the relations requested in item 4.
- **Suggested fix:** Retain the velocity and clock level specified in item 2(b) when eliminating $`p_0`$, and retain their first-order difference from the band-centre velocity. If the relation is instead intended for the carried clock’s instantaneous velocity, include the oscillating term in (5.24) and state its dependence on λ. The tick-averaged relations may remain as additional results, but should not replace the requested relations or support a universal coefficient for the specified velocity.

## Focus points

None given.
