# External verification: 06-mark-inertia

- **Subproject:** 08-ilang-propagation
- **Package:** 06-mark-inertia
- **Verified version:** v5
- **External round:** 3 of 3
- **Date:** 2026-10-25T11:28:44+01:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The second-order dressed-level formula, the inverse-curvature expansion, and the weight formulas are consistent with the stated contract and perturbative counting. The supplied diagonalisation code provides an independent check of the required second-order coefficients, and its outputs support the reported agreement. The remaining problems concern an overstatement of finite-size uniformity and two subleading ring asymptotics; they do not invalidate the leading large-volume common-speed result.

## Issues

### I1. The heavy-body odd-part estimate is not uniform in finite volume
- **Location:** Step 8, Eq. (6.10), first relation and its stated finite-size range
- **Severity:** minor
- **Problem:** The first relation is claimed for every $`L`$ and $`\ell`$, but its derivation uses an estimate that fails when the uniform mode dominates at fixed $`L`$. For example, take the linear grip, fixed $`L\ge32`$, $`r\le1`$, and fixed heavy $`\varepsilon_k`$, then let $`m_h\to0`$. The zero mode gives
  ```math
  \langle\!\langle1/E\rangle\!\rangle\sim\frac{F_1^2}{2Lm_h^2},
  \qquad R=O(m_h^2).
  ```
  Its lower-branch curvature ratio is $`4\varepsilon_k/(m_h+2\varepsilon_k)`$, while its formal upper-branch ratio is $`4\varepsilon_k/(2\varepsilon_k-m_h)`$. Consequently,
  ```math
  \rho_{k,-}-\rho_k^{\rm e}
  =-\frac{m_h}{\varepsilon_k}+O(m_h^2),
  ```
  rather than the asserted $`2\varepsilon_kR[1+O(\varepsilon_k^{-2})]=O(m_h^2)`$. The neglected other-branch contribution therefore cannot be bounded uniformly as claimed.
- **Suggested fix:** Restrict this estimate to the large-volume regime $`L\gg\ell`$, with the other stated finite-size conditions, or retain the uniform-mode contribution explicitly. Keep the exact finite-$`L`$ formulas (6.3) and (6.6) separate from this asymptotic estimate.

### I2. The first rapidity identity has an overly strong error estimate
- **Location:** Step 6, Eq. (6.7), first relation
- **Severity:** minor
- **Problem:** For the two-quantum contribution, convergence of the limiting rapidity integrals does not imply the stated relative $`O(\ell^{-1})`$ error. Configurations with one soft momentum and the other of lattice order produce logarithmic corrections. For example, using centered momenta and $`c_0=1`$, the coefficient relevant to this soft–hard contribution contains the nonzero finite part
  ```math
  \mathrm{FP}\int_{-\pi}^{\pi}
  \left[
  \frac{q^2}{(2|\sin(q/2)|)^4}
  -\frac{1}{2(2|\sin(q/2)|)^2}
  \right]\,dq
  =\frac{\pi}{6}(4\ln2-1).
  ```
  Integration over the soft partner supplies $`\ln\ell`$. Thus the discrepancy can be $`O(\ln\ell)`$ against a leading sum of order $`\ell`$, rather than having the claimed relative $`O(\ell^{-1})`$ bound.
- **Suggested fix:** Replace the relative error in this relation by $`O(\ln\ell/\ell)`$, or supply an additional cancellation establishing the stronger estimate. The weaker bound is already absorbed by the later $`O(\delta_\ell)`$ remainder, so the leading conclusions need not change.

### I3. The ring heavy-body scale depends on the grip
- **Location:** Step 8, Size of R paragraph
- **Severity:** minor
- **Problem:** The statement that the ring heavy regime “requires $`\varepsilon_k\gg c_0\ell/\ln\ell`$” applies to the one-quantum, linear-grip contribution, not to every grip in (G2). The two-quantum numerator has a soft-momentum contribution of order $`\ln^2\ell`$, so
  ```math
  R_1=\Theta\!\left(\frac{\ln\ell}{c_0\ell}\right),
  \qquad
  R_2=\Theta\!\left(\frac{\ln^2\ell}{c_0\ell}\right).
  ```
  The supplied Part B output also exhibits this distinction. With a fixed nonzero two-quantum contribution, the condition $`\varepsilon_kR\gg1+r^2`$ can therefore be reached on the smaller scale $`c_0\ell/\ln^2\ell`$, up to grip-dependent constants.
- **Suggested fix:** State the heavy condition primarily as $`\varepsilon_kR\gg1+r^2`$. Identify $`c_0\ell/\ln\ell`$ as the linear-grip scale, or as a stronger sufficient condition for the general case, rather than a necessary scale for every grip.

## Focus points

None given.
