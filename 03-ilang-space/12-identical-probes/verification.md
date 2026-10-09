# External verification: 12-identical-probes

- **Subproject:** 03-ilang-space
- **Package:** 12-identical-probes
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-08T17:02:13+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The preservation criterion and the single- and two-probe leading-order distances are derived correctly. The derivation also correctly identifies that Goal 1(b) is false for the total operator: swap invariance requires an \(h\)-independent \(\Delta_h\), not necessarily \(\Delta=0\). Two peripheral claims need qualification, but neither affects the principal formulas or the partner-as-witness result.

## Issues

### I1. Nonunique decomposition is not automatically a description convention
- **Location:** Step 3, discussion following Eq. (12.6); Result, item 1.
- **Severity:** minor
- **Problem:** Equation (12.6) correctly describes all redistributions preserving the total operator \(C\). However, identifying this freedom as an A5/M6 convention of the complete description is not established. A5 explicitly includes the individual contract operators in the description, and the redistribution changes their individual costs:
  \[
  L_1\longmapsto L_1+\operatorname{Tr}(X V_c),\qquad
  L_2\longmapsto L_2-\operatorname{Tr}(X V_c).
  \]
  Thus equality of total operators establishes identical evolution and total cost, but does not by itself declare the complete contract lists equivalent.
- **Suggested fix:** Describe (12.6) as nonuniqueness of the decomposition at fixed total \(C\), and retain the correctly proved insensitivity of the leading geometry to that redistribution. Qualify the stronger “convention” claim unless equivalence of contract lists is explicitly assumed.

### I2. Nonconstant record differences need not produce unequal distances
- **Location:** Step 7, final bullet concerning \(h\)-dependent \(\Delta_h\).
- **Severity:** minor
- **Problem:** The statement that Step 6 “would give different values” for the two probes when \(\Delta_h\) depends on \(h\) is too strong. For example, take
  \[
  K^{(2)}_h=K^{(1)}_h-r_h\mathbb 1_c
  \]
  with real, nonconstant \(r_h\). Then \(\Delta_h=r_h\mathbb 1_c\) is nonconstant, but
  \[
  Q_\chi K^{(2)}_h\chi=Q_\chi K^{(1)}_h\chi,
  \]
  so both probes have exactly the same leading-order distances for the product initial state. Loss of admissibility means that (2.16) is no longer guaranteed; it does not imply that its geometric equalities necessarily fail.
- **Suggested fix:** Replace “would give different values” by “can give different values,” and “(2.16) does not hold outside \(\mathcal H_{\rm adm}\)” by “(2.16) need not hold outside \(\mathcal H_{\rm adm}\).”

## Focus points

None given.
