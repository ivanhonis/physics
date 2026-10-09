# External verification: 21-composite-body

- **Subproject:** 03-ilang-space
- **Package:** 21-composite-body
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-09T07:34:08+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The acceleration identities, the response formula \(\mu_c=\tfrac14(\mu_1+\mu_2)\), and the chain inertias are algebraically consistent. The variational argument correctly establishes sequence-independent inertia limits, and the bounded-commutator estimate correctly makes the binding contribution to the initial acceleration vanish along minimizing sequences. The remaining issues concern the claimed completeness of the A5 convention check and an overly strong statement about phase covariance.

## Issues

### I1. The A5 placement check excludes allowed regroupings
- **Location:** Step 2, discussion following Eq. (21.2); Result item 1.
- **Severity:** minor
- **Problem:** Equation (21.2) classifies representations that retain the stipulated diagonal form of \(W\) and the recording terms. This is not an exhaustive check of A5 contract-list regroupings. A5 permits an off-diagonal single-object operator \(D\) on \(b_1\) to be included in the \(b_1\)–\(b_2\) pair term as \(D\otimes\mathbb 1_2\), rather than in a body–medium pair term. Thus “off-diagonal single-object terms cannot be moved” is false as a statement about A5, even though such a move leaves the restricted parametrization used in (21.2). The main response formulas are not contradicted by regrouping, but the requested check of **every** placement is incomplete.
- **Suggested fix:** Distinguish the diagonal binding operator \(W\) from the full pair-contract operator that may also contain bookkeeping single-object contributions. Explicitly check that arbitrary regrouping leaves the total blocks \(C^{(i)}_{hh'}\), the background, and hence \(\bar R\), \(A\), and \(\mu_c\) unchanged. Clarify that the hopping edges used in the formulas are extracted from the total operator, not from a particular contract-list placement.

### I2. Phase covariance is sufficient, not necessary, for preserving the gradient operator
- **Location:** Step 2, “Phases”: “\(G_f\) stays the same if and only if \(f\mapsto R_\theta f\).”
- **Severity:** minor
- **Problem:** Simultaneously rotating \(f\) is sufficient, but not necessary. The map \(f\mapsto G_f\) has invisible directions: since every record vector belongs to \(\chi^\perp\), both \(\chi\) and \(i\chi\) lie in its real-linear kernel. For example, keeping \(f=\chi\) fixed gives \(G_f=0\) both before and after the phase rotation, without replacing \(f\) by \(R_\theta f\).
- **Suggested fix:** Replace “if and only if” by “if.” If a necessity statement is wanted, formulate it modulo the kernel of the gradient map. The covariance statement for \(\mu_c\) otherwise remains valid.

## Focus points

None given.
