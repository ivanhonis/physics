# External verification: 03-clock-and-fall

- **Subproject:** 05-ilang-free-fall
- **Package:** 03-clock-and-fall
- **Verified version:** v2
- **External round:** 2 of 2
- **Date:** 2026-10-10T20:23:21+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The acceleration operators and the principal first-order acceleration and window-average formulas are consistent, including the distinction between the two orders of the wide-start and long-window limits. The clock-rate conclusions need a clearer qualification concerning finite packet width, and the requested first nonzero orders of several clock corrections remain undetermined. There is also an incorrect late-time estimate for the oscillating force contribution and a dimensional-check error.

## Issues

### I1. Local clock rate requires an additional wide-packet qualification
- **Location:** Step 8, equations (3.22)–(3.23); Step 9, equation (3.24)
- **Severity:** minor
- **Problem:** The bound (3.22) is useful, but its finite-width term survives the zeroth-gradient limit specified in item 3(b). Thus that limit alone does not establish a single advance $`\eta_{x_0}\lambda/\lambda_0`$, or a tick $`\lambda_0/\eta_{x_0}`$, for the prescribed finite-$`W`$ start. For example, with uniform profiles, expansion of the clock-level coherences gives the coefficient
  ```math
  A_W(\lambda)=
  \left\langle
  \frac{m_\ast^2}{\omega(p)^2}\lambda+
  \frac{\tau_\ast^2\sin^2p}{2\omega(p)^3}\sin(2\omega(p)\lambda)
  \right\rangle_W,
  \qquad
  \omega(p)^2=m_\ast^2+\tau_\ast^2\sin^2p,
  ```
  multiplying $`\eta_\ast(d_k-d_{k'})`$, rather than simply $`\lambda`$. This shows a finite-width, mass-dependent clock response even when every gradient vanishes. Equations (3.23)–(3.24) are therefore leading narrow-momentum/rest-clock results, not unrestricted results of the stated local-gradient limit. Moreover, an absolute bound on $`q`$ does not by itself bound the error in an inferred rate or tick.
- **Suggested fix:** Explicitly identify the additional narrow-momentum approximation and its range, for example requiring the finite-width term in (3.22) to be small over the comparison interval. State the rate and ratio as leading results in that approximation, and delimit their finite-width corrections; alternatively, retain the finite-$`W`$ local clock response when answering the specified zeroth-gradient limit.

### I2. Bounds do not determine all requested first correction orders
- **Location:** Step 8, “First corrections: what is proven,” equation (3.33), and Open issues
- **Severity:** minor
- **Problem:** Item 3(b) asks for the powers at which width and beginning motion first change $`q`$. The derivation establishes general upper bounds and, for symmetric starts, the absence of odd total gradient degree. Neither establishes that the allowed second-order terms are actually present. The text correctly acknowledges that several coefficients are not proven nonzero, but nevertheless says that width and motion “first enter” at the quoted powers. The same distinction applies to the first-order motion bound for asymmetric starts.
- **Suggested fix:** Consistently distinguish “lowest symmetry-allowed order” or “upper-bound order” from “first nonzero order.” Supply the missing arguments for the latter where required by item 3(b), or explicitly identify that portion of the requested result as unresolved rather than answered.

### I3. Late-time oscillation estimate omits a force contribution
- **Location:** Step 5.2, paragraph beginning “Rate (order estimate)”
- **Severity:** minor
- **Problem:** The stated growing oscillating term is proportional only to $`|G_k|`$. At finite $`W`$, the plain-gradient variant can also have a growing oscillating first-order velocity contribution. In particular, its quadratic-in-$`\lambda`$ oscillating term includes
  ```math
  \mathcal F\,\frac{M_k}{\omega_k(p)}
  \bigl(\omega_k'(p)\bigr)^2\lambda^2
  \sin(2\omega_k(p)\lambda).
  ```
  Near a nondegenerate stationary point this amplitude vanishes quadratically, so stationary phase produces a contribution of order $`\lambda^{1/2}`$ for generic packet weights. Consequently, setting $`G_k=0`$ does not generally remove the growing oscillating remainder. This does not invalidate the long-window limit (3.27), since the remainder remains sublinear.
- **Suggested fix:** Include the $`\mathcal F`$ contribution in the late-time estimate, or restrict the quoted $`|G_k|`$-dependent estimate explicitly to the corresponding gradient contribution.

### I4. Dimensional check assigns acceleration units to a velocity formula
- **Location:** Consistency checks, item 1, reference to equation (3.26)
- **Severity:** minor
- **Problem:** Equation (3.26) describes $`\nu`$, the first-order velocity, and therefore has units $`1/\lambda`$. Its secular coefficient $`a_{\rm sec}(p)`$ has units $`1/\lambda^2`$, but the consistency check assigns $`1/\lambda^2`$ to equation (3.26) as a whole.
- **Suggested fix:** Check the units of $`\nu`$ and $`a_{\rm sec}(p)`$ separately, and correct the stated units of the velocity decomposition.

## Focus points

None given.
