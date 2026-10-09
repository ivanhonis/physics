# External verification: 05-recording-contract

- **Subproject:** 03-ilang-space
- **Package:** 05-recording-contract
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-08T11:02:17+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The exact evolution, witness-overlap expansion, and angle limit are correctly derived, including the zero-variance case. The Euclidean quotient, sharp dimension bound, and conditions for the line and plane examples are also correct. The only issue is an omitted qualification in the result summary; the derivation itself handles that boundary case correctly.

## Issues

### I1. Line dimension stated without the singleton exception
- **Location:** Result, item 4; compare Step 7.
- **Severity:** minor
- **Problem:** The summary states that the line example has $\dim_0=1$ without requiring $n\ge2$. The question allows $n=1$, for which the configuration contains one point and its affine dimension is $0$. Step 7 correctly states both cases, so this is a summary-level inconsistency rather than a derivation error.
- **Suggested fix:** State “$\dim_0=1$ for $n\ge2$, and $\dim_0=0$ for $n=1$” in the result summary.

## Focus points

None given.
