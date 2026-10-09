# External verification: 24-background-stability

- **Subproject:** 03-ilang-space
- **Package:** 24-background-stability
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-09T13:09:21+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The finite-dimensional analytic argument correctly establishes the generic partition, isolated mergers, discrete graph-change events, and a positive initial stability scale. The trajectory construction and the explicit qubit-line and window-medium calculations are consistent with the supplied definitions and inputs. The main shortcoming is that the requested neighbour-event set for the general-\(X\) line is left as a candidate superset rather than characterized exactly.

## Issues

### I1. General-\(X\) neighbour-event set is not fully determined
- **Location:** Step 8.2, “\(\Lambda_N\) in general”; Result 3(b); Open issues.
- **Severity:** minor
- **Problem:** Item 3 requests \(\Lambda_N\) for each example, but Step 8.2 gives only
  \[
  \Lambda_N\subseteq
  \{\lambda:F(k\lambda)=F(k'\lambda)\}
  \cup\{\lambda:F(k\lambda)=0\}.
  \]
  These candidate events need not change any edge. For example, with \(F(s)=\cos^2s\) and \(n=3\), \(\lambda=\pi/4\) is a candidate because \(F(2\lambda)=0\), but the neighbour graph remains the same path around that value. The derivation correctly acknowledges this incompleteness, but therefore does not finish the requested determination.
- **Suggested fix:** Give an exact implicit candidate-retention rule using (24.1): outside \(\Lambda_{\mathcal P}\), retain a candidate precisely when some edge indicator differs between the candidate value and either adjacent zero-free interval, or between the two adjacent intervals. This would characterize \(\Lambda_N\) in terms of \(F\) without requiring closed-form roots.

## Focus points

None given.
