# External verification: 03-held-sources

- **Subproject:** 06-ilang-source
- **Package:** 03-held-sources
- **Verified version:** v2
- **External round:** 2 of 3
- **Date:** 2026-10-19T09:48:58+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The perturbative response formulas, trace sum rules, ordered-mixture results, and explicit matrix examples are correct. The derivation also appropriately distinguishes adapted-state costs from the conserved cost of a source-independent start, and acknowledges the reference dependence of the perturbative decomposition. Remaining problems are an overbroad invariance claim for trivial body couplings, an unqualified rank assignment at degenerate levels, and potentially misleading wording about the self-energy factor of one half.

## Issues

### I1. Sharpness is not invariant for scalar body couplings
- **Location:** Result entry for equations (3.18) and (3.19); Step 9, items 1–2
- **Severity:** minor
- **Problem:** The Result labels the exact sharpness/nonresponse statements as [I], asserting that sharpness at the occupied places does not depend on the writing of the contract. The uniqueness argument supporting this assertion requires both $`G_i`$ and $`\Phi_{x_i}`$ to be non-scalar, but the Result does not retain that restriction. For example, take $`G_1=G_2=\mathbb 1`$, $`C_f=\sigma_3`$, and $`\Phi_{x_1}=\Phi_{x_2}=\sigma_3`$. The total contract on the field is $`3\sigma_3`$, and $`\lvert0\rangle`$ is sharp at both places. The equally admissible writing
  ```math
  C_f'=3\sigma_3-2\sigma_1,\qquad
  \Phi'_{x_1}=\Phi'_{x_2}=\sigma_1,\qquad
  G_i'=\mathbb 1
  ```
  leaves the total contract unchanged, but $`\lvert0\rangle`$ is not sharp at either place. Thus the claimed [I] interpretation fails in an allowed part of the stated class.
- **Suggested fix:** Retain the non-scalar-factor restrictions when claiming that sharpness is intrinsic to the total contract. Treat scalar-coupling cases separately, without assigning an invariant meaning to sharpness or to response relative to the listed $`C_f`$.

### I2. Rank assignment requires a non-degenerate reference eigenvalue
- **Location:** Step 9, item 2, paragraph preceding equation (3.26)
- **Severity:** minor
- **Problem:** The assertion
  ```math
  E_n(g)=E_\alpha^{(k)},\qquad k=\#\{m:e_m\le e_n\},
  ```
  is stated without restricting $`e_n`$ to be non-degenerate. For a degenerate level, Weyl’s inequality identifies a cluster of eigenvalues, not one eigenvalue of the displayed rank. The proposed $`k`$ selects the last rank in that cluster and cannot represent all its branches, consistently with the ambiguity already explained in Step 3.
- **Suggested fix:** Explicitly restrict this rank identification to a simple reference eigenvalue. For a degenerate level, identify the corresponding block of ranks and use its spectral projector or level sum unless an individual branch has separately been specified.

### I3. The self-energy factor does not imply a half-strength felt field
- **Location:** Step 7, item 3, sentence immediately following equation (3.20)
- **Severity:** minor
- **Problem:** “A source thus feels … half of its own” conflates a total-cost accounting factor with the field response. Equation (3.20) correctly gives
  ```math
  \Sigma_i=\tfrac12 g_i\,\delta N^{(i)}(x_i),
  ```
  but the pair-term expectation contains the full induced field. Likewise, Hellmann–Feynman gives, through the stated order,
  ```math
  \frac{\partial E_n}{\partial g_i}
  =\bar\Phi_n(x_i)+\delta N_n^{(i)}(x_i)
  +\delta N_n^{(j)}(x_i)+O(g^2),
  ```
  with no factor of one half on the self-induced response. The half factor belongs to the total self-energy after the field’s own cost is included. No separate operational meaning of “feels” is derived for these held bodies.
- **Suggested fix:** Describe equation (3.20) as a relation between mutual energy, self-energy, and induced expectation values. Remove or qualify the statement about feeling half of one’s own field.

## Focus points

None given.
