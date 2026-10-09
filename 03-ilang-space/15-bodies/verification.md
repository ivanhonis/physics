# External verification: 15-bodies

- **Subproject:** 03-ilang-space
- **Package:** 15-bodies
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-08T14:42:29+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The product-state evolutions, exact cyclic-subspace criterion, leading-order record-sum criterion, and both example metrics are correctly derived. However, distinguishability of entire medium-state orbits is incorrectly promoted to recoverability from an instantaneous exact medium state, which fails at revivals. The derivation also overstates what the bodies’ views forget: their normalized witness geometries do not supply \(D\), but their full views determine the configuration relative to the specified background.

## Issues

### I1. Exact-state recoverability does not follow from leading-order distinguishability
- **Location:** Step 7, final sentence; Steps 8–9, “Answer”; corresponding statements in “Result.”
- **Severity:** major
- **Problem:** The implication “functions of the leading-order medium state, and therefore also of the exact one” needs a time-domain qualification. Equations (15.16) and (15.19) correctly characterize equality **for every \(\lambda\)**, but this compares entire state orbits. It does not establish recoverability from the instantaneous view \(V_{\{c\}}(\lambda)\), which is the defined state of the medium. For example, (15.18) gives
  \[
  E_{i_1i_2}(\pi)
  =(-1)^{\sum_l\nu_l}\chi
  =\chi
  \]
  for every window configuration, since \(\sum_l\nu_l=2m\). Nevertheless, in the symmetric family, \(\{h_1,h_1\}\) has \(D=0\), whereas \(\{h_1,h_2\}\) has \(D=\sqrt2\). Thus the window’s instantaneous exact medium state does not always determine \(D\), despite satisfying (15.14). The small-\(n\) line conclusions likewise require qualification; admissible choices such as \(X=\sigma_x\), \(\chi=|0\rangle\) have revivals.
- **Suggested fix:** State separately that the conclusions hold for the leading-order equivalence classes and for the entire medium-state orbits. Where leading-order distinguishability holds, exact distinguishability also holds for sufficiently small nonzero \(\lambda\), uniformly over the finitely many starts. Do not claim recoverability from an arbitrary instantaneous exact state.

### I2. Full body views retain the configuration
- **Location:** Step 5, concluding paragraph; “Result,” second bullet; “Open issues,” first bullet.
- **Severity:** minor
- **Problem:** The correct calculation of normalized witness weights does not justify “\(D\) cannot be seen in the views of the bodies” or “it is recorded only in the medium.” Within the fixed description assumed throughout, the diagonal entries of the single-instance view give the occupation numbers:
  \[
  n_h=2\langle h|V_{\{b_1\}}|h\rangle .
  \]
  These recover the unordered place multiset, including double occupation. Applying the known quotient \(h\mapsto[h]_0\) then recovers the configuration and hence \(D\). The pair view also retains this information in its support. Place-basis indices are type data, not forbidden instance identifiers. What is independent of \(D\) for distinct occupied places is the numerical normalized witness geometry, not the complete views.
- **Suggested fix:** Restrict the information-loss claim to the abstract normalized witness geometries calculated in (15.9)–(15.10). Explicitly distinguish those geometries from the full place-indexed views, which determine the configuration and \(D\) once the background is specified. Remove the assertion that \(D\) is recorded only in the medium.

## Focus points

None given.
