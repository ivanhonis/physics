# External verification: 03-clock-and-fall

- **Subproject:** 05-ilang-free-fall
- **Package:** 03-clock-and-fall
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-10T19:22:19+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The exact commutator formulas and the infinite-chain, wide-start first-order acceleration are consistent with the stated contract. In particular, the nonconvergence of the ordinary window average when the rest profile has a gradient follows from the derived oscillatory term; it should not be discarded merely because universality was anticipated. However, the final comparison substitutes a newly defined secular acceleration for the acceleration requested in the question, and the finite-width averaging problem remains unanswered. The stated finite-chain remainder estimate also relies on an operator-norm bound that fails at open boundaries.

## Issues

### I1. Secular acceleration substitutes for the requested acceleration
- **Location:** Step 9, comparison table and Eq. (3.25); Result, Item 4
- **Severity:** major
- **Problem:** The table establishes universality of $`a_{\rm sec}`$, defined using a double average or the quadratic displacement coefficient, rather than of the ordinary window-averaged acceleration in item 2(b). The derivation itself shows that these observables differ substantially: for variant (a),
  ```math
  \overline{a^{(1)}_\infty}=-g\tau^2(1-\varsigma),
  ```
  and $`\varsigma`$ retains an order-one dependence on $`M_k=m+d_k`$, however long the window is. Variant (c) has the same persistent dependence. Thus the assertion that variants (a) and (c) have both requested properties is not established for either the instantaneous acceleration or the specified window average. The qualification following Eq. (3.25) identifies this distinction but does not make the table an answer to item 4.
- **Suggested fix:** Answer item 4 using the specified acceleration observable. Keep the secular result separately identified as an additional result, rather than using it to claim the requested universality.

### I2. Window averaging is evaluated only after the wide-start limit
- **Location:** Step 5; Steps 6 and 9, statements about averaged accelerations
- **Severity:** major
- **Problem:** Equation (3.10) gives the first-order acceleration for a finite-width start, but Step 5 averages only its wide-start limit, Eq. (3.11). The question asks for the acceleration and its window average for the stated starts, which include finite $`W`$. No finite-$`W`$ averaged formula or long-window gradient coefficients are derived. This omission matters because momentum-dependent branch frequencies can dephase upon integration over $`|\tilde\phi_X(p)|^2`$. The wide-start and long-window limits cannot simply be interchanged: Eq. (3.12) explicitly gives an error growing with the window endpoint, and the derivation states that the wide-start limit is not uniform in $`\lambda`$.
- **Suggested fix:** Average Eq. (3.10) for finite $`W`$, determine its long-window coefficients, and distinguish that result from taking $`W\to\infty`$ before the long-window limit. Carry this distinction into the variant and other-branch evaluations.

### I3. The remainder proof omits open-boundary acceleration terms
- **Location:** Step 5, derivation of Eq. (3.16)
- **Severity:** major
- **Problem:** The asserted bound $`\|\hat a\|\le c\tau M_k`$ is false on the stated finite open chain without an additional restriction on $`\tau/M_k`$. Even with zero gradients, Eq. (3.6) contains
  ```math
  \frac{\tau^2}{2}(P_{-L}-P_L).
  ```
  Consequently $`\|\hat a^{(0)}\|\ge\tau^2/2`$, which cannot be bounded by $`c\tau M_k`$ with a pure, parameter-independent number $`c`$ as $`M_k/\tau\to0`$. The condition $`b_1\ell\le M_k`$ does not remedy this, since it imposes no restriction on $`\tau/M_k`$. Therefore the supplied proof does not establish Eq. (3.16) or its advertised general validity range.
- **Suggested fix:** Include the boundary contribution in the operator-norm estimates, or separately bound its expectation using propagation estimates for starts sufficiently far from the ends. Recalculate the remainder bound and the sufficient validity condition accordingly.

### I4. General clock-correction orders are not established
- **Location:** Step 8, “First corrections” and Eq. (3.22)
- **Severity:** minor
- **Problem:** The reflection argument establishes absence of terms of odd total gradient degree only for even $`w`$. It does not establish the first nonzero powers of $`\lambda`$, nor that the second-order coefficient is nonzero for each relevant coupling. The width calculation is exact only at $`\tau=0`$, whereas the class assumes $`\tau>0`$; the beginning-motion calculation is supplied only for variant (d). Moreover, the “gradient terms below” in $`\mathcal R_{\rm cl}`$ are not given a general finite-$`\tau`$ bound. Thus the claimed general orders in item 3(b) remain insufficiently justified, especially for the allowed asymmetric starts.
- **Suggested fix:** Supply finite-$`\tau`$ estimates establishing the first nonzero width and motion corrections, including their powers of the gradients and $`\lambda`$, and distinguish symmetric from asymmetric starts. An explicit bounded remainder would settle this issue without requiring all second-order coefficients.

### I5. The double-average error is not generally a relative error
- **Location:** Step 5, paragraph following Eq. (3.15)
- **Severity:** minor
- **Problem:** The claim of a relative error $`O(1/(M_k\Lambda))`$ is invalid when $`a_{\rm sec}=0`$, and is not uniform near the cancellation $`\mathcal F=G_k`$. Equation (3.15) instead gives the absolute bound
  ```math
  \left|\frac{2[\bar x^{(1)}_{\rm lab}(\Lambda)-\bar x_{\rm lab}(0)]}{\Lambda^2}-a_{\rm sec}\right|
  \le
  \frac{\tau^2|G_k|}{M_k^2\Lambda}
  +\frac{\tau^2|M_kg_\zeta-\mathcal F-G_k|}{M_k^3\Lambda^2}.
  ```
  Dividing by $`a_{\rm sec}`$ introduces gradient ratios that can diverge.
- **Suggested fix:** State the absolute error bound. Describe it as a relative estimate only under an explicit noncancellation condition on $`\mathcal F-G_k`$.

## Focus points

None given.
