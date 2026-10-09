# External verification: 16-common-space

- **Subproject:** 03-ilang-space
- **Package:** 16-common-space
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-08T16:07:05+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The split freedom, the three leading-order metrics, and the translation criterion for correspondences are correctly derived. The existence and uniqueness arguments for full correspondences and both example geometries are also sound. The remaining problems are qualifications and overstatements: the trivial-medium exception is lost in some conclusions, and several statements claim more than the leading-order geometric analysis establishes.

## Issues

### I1. Missing qualification for a one-dimensional medium
- **Location:** Step 2.5; Step 4.2; Result, “Split”.
- **Severity:** minor
- **Problem:** The setting permits \(\dim\mathcal H_c=1\). In that case \(\mathcal N=\{0\}\), all record vectors vanish, and \(\|u^A_h-u^B_k\|=0\) is well defined. Consequently, the unqualified Result statement that this quantity is not well defined and ranges over \([0,\infty)\) is false in this allowed case. The lists of non-well-defined record quantities and the statement that the leading geometry does not fix \(\|w_{hk}\|\) likewise need this exception. Step 2 correctly notices the degeneracy, but does not consistently carry it through.
- **Suggested fix:** Qualify these assertions by \(\dim\mathcal H_c\ge2\), and state that all record-vector quantities in question vanish for a one-dimensional medium.

### I2. Overstatement about cross-type distances
- **Location:** Result, “2c”: “it does not fix any distance between a point of \(A\) and a point of \(B\)”.
- **Severity:** minor
- **Problem:** What is proved is that the unshifted expression \(\|u^A_h-u^B_k\|\) is split dependent. The blanket statement about *any* cross-type distance is stronger and conflicts with the Gram-matrix characterization. For example,
  \[
  \bigl\|(u^A_x-\bar u^A)-(u^B_y-\bar u^B)\bigr\|
  \]
  is split invariant and determined by that Gram matrix. Also, when the unique full correspondence exists, identification through it supplies cross-type distances from the already determined metric.
- **Suggested fix:** Restrict the conclusion to the raw cross-type distance \(\|u^A_h-u^B_k\|\), or to the absence of a prescribed relative alignment without an additional identification. Do not assert that no cross-type distance can be determined.

### I3. Ambiguous claim that \(Y\) drops out of every view
- **Location:** Step 6, second bullet; Result, “Examples”.
- **Severity:** minor
- **Problem:** The calculation establishes that \(Y\) drops out of the three \(d_0\) geometries and their mixed displacement products. It does not establish independence of the full views. In general, \(e^{-i((i+j)X+Y)\lambda}\) cannot be factored into a common medium unitary and an \(X\)-dependent unitary when \(X\) and \(Y\) do not commute; higher-order view data can therefore depend on \(Y\). If “view” is intended only as shorthand for its leading-order geometry, this is a wording issue rather than an error in the calculation.
- **Suggested fix:** Say explicitly that \(Y\) drops out of the leading-order witness distances and mixed displacement products, not out of the full views.

## Focus points

None given.
