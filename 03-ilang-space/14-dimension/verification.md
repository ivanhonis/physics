# External verification: 14-dimension

- **Subproject:** 03-ilang-space
- **Package:** 14-dimension
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-08T14:38:55+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The multichannel decomposition, dimension bounds, generic classification, minimum medium dimensions, and both examples are correctly derived under the stated assumptions. The loop-phase calculations also follow the supplied sign conventions. One attainment condition for commuting records is too strong when the number of places, rather than the cell dimension, limits the affine dimension; this does not affect the subsequent full-support generic classification.

## Issues

### I1. Full spectral support is not always necessary to attain the dimension bound
- **Location:** Step 5.4, immediately after Eq. (14.12).
- **Severity:** minor
- **Problem:** The claim that attaining \(\min(n-1,d_c-1)\) additionally requires \(r_\chi=d_c\) is false when \(n<d_c\). In that regime, \(n\) supported joint eigenspaces can suffice. For example, take \(n=4\), \(d_c=5\), \(K_h=|e_h\rangle\langle e_h|\) for \(h=1,\ldots,4\), and
  \[
  |\chi_c\rangle=\tfrac12(e_1+e_2+e_3+e_4).
  \]
  These commuting operators have five one-dimensional joint eigenspaces, but \(r_\chi=4<5\). Nevertheless,
  \[
  u_h=\tfrac12e_h-\tfrac14\chi_c
  \]
  have affine dimension \(3=\min(n-1,d_c-1)\). The rank formula in Eq. (14.12) itself is correct.
- **Suggested fix:** Retaining the preceding full-rank condition, replace \(r_\chi=d_c\) by \(r_\chi\ge\min(n,d_c)\). Full spectral support is necessary for this saturation only when \(n\ge d_c\).

## Focus points

None given.
