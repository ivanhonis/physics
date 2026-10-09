# External verification: 11-cut-boundary

- **Subproject:** 03-ilang-space
- **Package:** 11-cut-boundary
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-08T16:58:41+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The core derivations are correct: the product-state factorization, generalized record vectors, leading-order distance, small-\(\lambda\) neighbour graph, and both examples follow from the stated inputs. The graph proof correctly uses stability of the relevant strict inequalities. Minor corrections are needed to the contract-splitting convention and to several auxiliary claims about distance ordering, identical-type instances, and scaling.

## Issues

### I1. Local-term regrouping changes the fixed cut notation
- **Location:** Setup, “Splitting of the contract system”; Step 5.
- **Severity:** minor
- **Problem:** The question defines \(C_A,C_{\bar A},C_\partial\) by the endpoints of the listed contracts. The derivation instead assigns a packed single-object term to the side on which it acts, even when its listed pair crosses the cut. This is a different decomposition. Although the resulting \(d_0\) is unchanged, the prescribed vectors \(u_h\) need not be unchanged: moving \(\mathbb 1_A\otimes D'\) out of \(C_\partial\) removes the common vector \(Q_\chi D'\chi\). The tension in the question’s two-object example does not justify silently changing notation explicitly fixed for later packages.
- **Suggested fix:** Retain the endpoint-defined split and distinguish any optional regrouping from it. In example (a), the packed term \(C_A^{\mathrm{example}}\otimes\mathbb 1\) can remain in \(C_\partial\); its contribution to every \(u_h\) is zero, so the stated distance result still follows.

### I2. Full distance ordering need not be preserved
- **Location:** Step 4, final sentence.
- **Severity:** minor
- **Problem:** The claim that “the order of the \(\alpha\) values is the order of the \(d_0\) values” is stronger than what was proved. The genericity condition excludes zero margins in the lune comparisons, but permits equal leading-order distances. For example, three equally spaced collinear record vectors satisfy the condition while their two adjacent distances are equal. Higher-order corrections can split such a tie. This does not invalidate the preceding neighbour-graph proof.
- **Suggested fix:** State only that strict comparisons between unequal leading-order distances, and all the relevant lune-comparison signs, are preserved for sufficiently small positive \(\lambda\).

### I3. The restriction on when item 2 is informative is too strong
- **Location:** Open issues, “Identical-type objects inside \(A\),” concluding paragraph.
- **Severity:** minor
- **Problem:** Repeated swap-invariant instances invalidate item 3’s pairwise-distinctness hypothesis, but do not make item 2 uninformative. For example, take two identical two-place objects in \(A\), a full-support symmetric product \(\phi\), and
  \[
  C_\partial=(Z_a+Z_b)\otimes B,\qquad \sigma_\chi(B)>0.
  \]
  This is a sum of admissible pair contracts. Its record vectors are proportional to \(2,0,0,-2\), giving nonzero distances between different permutation classes despite the repeated type.
- **Suggested fix:** Restrict the concluding exclusion to item 3. For item 2, retain the distinction already established: repeated sign-changing instances obstruct full support, whereas repeated swap-invariant instances force duplicate record vectors but can still yield nontrivial leading-order geometry.

### I4. Scaling requires a sign qualification
- **Location:** Consistency checks, item 1.
- **Severity:** minor
- **Problem:** From \(u_h\mapsto s u_h\), the norm-defined distance transforms as \(d_0\mapsto |s|d_0\), not \(s d_0\), unless \(s>0\). The check does not state that restriction, although it correctly uses \(|s|\) for the standard deviation immediately afterward.
- **Suggested fix:** Specify \(s>0\) for the dimensional rescaling, or use \(d_0\mapsto |s|d_0\) and qualify the corresponding one-sided parameter rescaling.

## Focus points

None given.
