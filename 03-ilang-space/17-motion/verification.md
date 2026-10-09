# External verification: 17-motion

- **Subproject:** 03-ilang-space
- **Package:** 17-motion
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-08T16:09:45+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The exact current equations, velocity bound, commuting-record solution, and infinite-chain results are correct, including their signs and numerical factors. The finite-chain limit is adequately justified for the quantities used. The short-time expansions are also correct, but Item 3 does not fully determine the leading nonvanishing orders for allowed starts in which the displayed coefficients vanish.

## Issues

### I1. Exceptional leading orders remain undetermined
- **Location:** Step 7, Eqs. (17.9) and (17.11)–(17.13); first “Open issues” bullet.
- **Severity:** minor
- **Problem:** The question requests leading **nonvanishing** orders, whereas the derivation supplies generic leading orders and expressly leaves some cancellation cases unresolved. These cases need not correspond to stationary motion. For example, take three places \(0,1,2\), hopping \(t>0\) only along \(0\!-\!1\!-\!2\), start at \(0\), and records \(K_0=K_1=0\), \(K_2=X\), with \(e=(X-\langle X\rangle)\chi\neq0\). Then \(w_2=w_3=0\), and the displayed \(\lambda^2\) spread coefficient also vanishes, but
  \[
  p_2\sim \frac{t^4\lambda^4}{4},\qquad
  \bar x-u_0\sim\frac{t^4\lambda^4}{4}e,\qquad
  v\sim t^4\lambda^3e,\qquad
  s^2\sim\frac{t^4\lambda^4}{4}\|e\|^2.
  \]
  Likewise, the graph-distance expression for \(p_h\) need not identify its first nonzero term when \((t^n)_{h\beta}=0\) through path interference. The unconditional wording that records “enter first at \(\lambda^4\)” should distinguish the first *possible* order from an actual nonzero onset.
- **Suggested fix:** Use the existing \(c_n(h)\) recurrence to specify how the first nonzero coefficient is selected in cancellation cases, including position and spread. Add the next coefficients obtainable from (17.10) when the displayed lower-order coefficients vanish, and qualify the \(\lambda^4\) record onset as the earliest possible order.

## Focus points

None given.
