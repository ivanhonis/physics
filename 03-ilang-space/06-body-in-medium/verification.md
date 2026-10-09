# External verification: 06-body-in-medium

- **Subproject:** 03-ilang-space
- **Package:** 06-body-in-medium
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-08T16:51:25+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The exact evolution, commuting-record result, cubic coefficient, and qubit example are derived correctly. The witness-angle expansion is also correct as a fixed-pair asymptotic expansion for \(d_0>0\). The only issue is that the stated norm-small condition is not, by itself, a sufficient quantitative validity condition for the angle expansion when \(d_0\) is very small.

## Issues

### I1. Quantitative validity of the angle expansion near \(d_0=0\)
- **Location:** Setup and assumptions, final sentence of “Assumptions”; Step 6.
- **Severity:** minor
- **Problem:** The claim that the expansions are quantitatively useful whenever
  \[
  \lambda\bigl(\|K_h+B_{\beta_0}\|+\|K_{h'}+B_{\beta_0}\|\bigr)\ll1
  \]
  needs an additional qualification for \(\alpha\). Step 6 expands
  \[
  \sqrt{1-\lambda c_3/d_0^2+O(\lambda^2)},
  \]
  whose smallness conditions can be substantially stronger when \(d_0\) is small. For example, take \(\chi=|0\rangle\), \(K_{h'}=0\), \(K_h=\sigma_z+\varepsilon\sigma_x\), and \(B_{\beta_0}=\sigma_y\), with \(\varepsilon>0\). The derived formulas give \(d_0=\varepsilon\), \(c_3=2\varepsilon\), and
  \[
  \alpha=\varepsilon\lambda-\lambda^2+O(\lambda^3).
  \]
  For \(\varepsilon\ll\lambda\ll1\), the advertised norm condition holds, but the truncation is negative and cannot approximate the nonnegative angle reliably. This does not invalidate the stated asymptotics as \(\lambda\to0^+\) with the operators fixed.
- **Suggested fix:** Restrict the norm-small criterion to the overlap and \(W\) expansions, and describe the angle expansion explicitly as a fixed-pair asymptotic result. For a finite-\(\lambda\) quantitative criterion, additionally require \(\lambda|c_3|/d_0^2\ll1\) and control the \(O(\lambda^4)\) remainder in \(W\) relative to \(\lambda^2d_0^2\).

## Focus points

None given.
