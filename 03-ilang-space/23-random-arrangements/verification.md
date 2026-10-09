# External verification: 23-random-arrangements

- **Subproject:** 03-ilang-space
- **Package:** 23-random-arrangements
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-09T10:34:07+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The code implements the prescribed realizations, cancellation-free distance comparisons, neighbour graphs, shortest paths, and statistics. The supplied outputs support the precommitted decisions: T1 passes, T2 gives “isotropy supported,” and T3 is “intermediate.” I found no algebraic or implementation error that demonstrably changes those decisions. The remaining issues concern the numerical-margin audit, the stated scope of an error bound, and two interpretations in the discussion.

## Issues

### I1. Error at one minimizing witness does not certify every edge constraint
- **Location:** Step 2; `rng_decide`, computation of `Em`.
- **Severity:** minor
- **Problem:** For T3 and T4, the error estimate for \(m=\min_y\max(T_1,T_2)\) is taken only at the computed minimizing \(y\). This suffices to certify a non-edge when that witness is demonstrably negative, but does not generally certify an edge: another candidate can have a larger computed value and a sufficiently larger error to become negative. Thus the reported large \(|m|/E_m\) ratios alone do not establish that every edge constraint is numerically resolved. This is a validation gap, not evidence that any reported edge is wrong.
- **Suggested fix:** For edges, check the lower error allowance for every candidate witness, or demonstrate that uncertainty cannot change the minimizing witness. Such a check would settle the issue without changing the precommitted models or decision rules.

### I2. The smallest absolute decisive margin is not reported
- **Location:** Step 2; `graph_summary`; output fields named `smallest_margin`.
- **Severity:** minor
- **Problem:** The question requests the smallest decisive margin, but the code selects the pair minimizing \(|m|/E_m\), not the pair minimizing nonzero \(|m|\). Its associated `m` therefore need not be the smallest absolute margin. These quantities differ particularly for broken ties in T3, whose margins can be very small while their relative numerical certainty remains high.
- **Suggested fix:** Save and report the smallest nonzero absolute margin separately from the smallest margin-to-error ratio, retaining the corresponding pair and error estimate for each.

### I3. The \(4u\) bound does not automatically apply to \(D_2\)
- **Location:** Step 1, “Error bound”; `tables` and `table_checks`.
- **Severity:** minor
- **Problem:** As written, “the relative error of every entry” appears to cover both \(S\) and \(D_2\). The positive-product argument establishes the stated bound for overlaps \(S\), but not directly for squared differences \(D_2\): input rounding errors can be amplified in \(\kappa(l)-\kappa(l-\Delta)\). Moreover, `table_checks` recomputes only overlaps, not \(D_2\). This does not demonstrate a consequential error in the edge weights, but the stated certification is broader than the checks establish.
- **Suggested fix:** Explicitly restrict the \(4u\) bound and Decimal validation to \(S\). If the bound is intended to cover \(D_2\) as well, supply a difference-aware error estimate and corresponding validation.

### I4. The grid symmetry ties cannot be resolved by finite-\(\lambda\) corrections
- **Location:** Step 9, “What T3 shows”; Open issues, “Tie edges.”
- **Severity:** minor
- **Problem:** The derivation correctly identifies T2’s decisive ties as exact \(D_4\) ties, but subsequently says their small-\(\lambda\) status can depend on finite-\(\lambda\) corrections. For these kernels, a \(D_4\) transformation and translation permute the cell factors in
  \[
  \prod_l\left|\cos\!\bigl(\lambda[k_{h,l}-k_{h',l}]\bigr)\right|.
  \]
  Consequently, symmetry-equivalent displacements have equal \(\alpha\) at every \(\lambda\), not merely equal \(d_0\). Together with preservation of the finitely many strict inequalities for sufficiently small \(\lambda\), these ties retain their edges under the prescribed strict rule. The perturbation sensitivity is real, but finite-\(\lambda\) corrections do not resolve these particular symmetry ties.
- **Suggested fix:** Restrict the unresolved finite-\(\lambda\) caveat to non-symmetry ties, and distinguish it from the demonstrated sensitivity to changing the records.

### I5. The locality conclusion exceeds the numerical evidence
- **Location:** Step 9, “What T3 shows,” final bullet.
- **Severity:** minor
- **Problem:** “Locality of \(N_0\) is therefore conditional on the non-local part of the records being far below the far-pair overlaps” is not established as a general condition. Equation (23.3) shows that neighbour status depends on witness margins involving both overlap changes and norm changes. Comparing perturbation magnitude with far-pair overlaps alone is neither shown necessary nor shown sufficient. The run establishes the specified robustness classification for one realization and one perturbation direction.
- **Suggested fix:** State the observed appearance of long edges and the “intermediate” decision without promoting the overlap comparison to a general locality condition.

## Focus points

None given.
