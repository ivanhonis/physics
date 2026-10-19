# External verification: 03-held-sources

- **Subproject:** 06-ilang-source
- **Package:** 03-held-sources
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-19T09:20:44+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The reduction to a source-dependent field operator, the non-degenerate perturbation formulas, and the trace and ordered-mixture identities are substantially correct. However, the derivation leaves unresolved the base problem’s mandatory invariance under contract redistributions: its reference eigenstates and self/mutual cost decomposition depend on the conventional zero of the coupled body operators. There are also overstatements concerning degenerate branches and the interpretation of the three-place example as a comparison of total costs.

## Issues

### I1. The mutual-cost construction remains convention-dependent
- **Location:** Setup and assumptions, Reference split; Open issues, first bullet; Results concerning self and mutual costs
- **Severity:** major
- **Problem:** The derivation explicitly acknowledges that $`G_i\mapsto G_i+c\mathbb 1`$, $`C_f\mapsto C_f-c\Phi_{x_i}`$ leaves the total contract unchanged but changes the reference eigenvectors and the self/mutual decomposition. This is precisely a redistribution under which M6 requires the derived structure to be invariant; it cannot simply be deferred to another package. Fixing a split as a description assumption does not remove this requirement.

  For example, with $`C_f=-t\sigma_1`$ and $`\Phi_j=|j\rangle\langle j|`$, the original lowest-state response is
  ```math
  \chi_-(1,2)=-\frac1{4t}.
  ```
  After the stated redistribution, expanding around the new source zero instead gives
  ```math
  \chi'_-(1,2)
  =-\frac{t^2}{4(t^2+c^2/4)^{3/2}}.
  ```
  The exact operator family is merely reparameterized, but the reference state and the coefficients advertised as self and mutual costs have changed. Thus these coefficients have not yet been defined as structures of the total contract and state.
- **Suggested fix:** Define the reference sector and source variations invariantly from the total contract and stated physical states, and establish covariance under the allowed redistributions. Otherwise, restrict the formulas explicitly to split-dependent mathematical coefficients and report that an invariant self/mutual cost has not been obtained.

### I2. Degenerate level sums are confused with individual branch responses
- **Location:** Setup and assumptions, Mixtures; Step 8, item 1; Open issues, fourth bullet
- **Severity:** minor
- **Problem:** The statement “For degenerate levels, only level sums carry an analytic mutual term” is false. Level sums are guaranteed to be analytic, but individual branches can also be analytic and have nonzero mutual terms even when every level response in (3.12) vanishes.

  For example, take
  ```math
  C_f=\omega\sigma_3\otimes\mathbb 1,\qquad
  \Phi_{x_1}=\sigma_1\otimes\mathbb 1,\qquad
  \Phi_{x_2}=\sigma_1\otimes\sigma_3 .
  ```
  Both unperturbed levels are doubly degenerate. In the sector where the second $`\sigma_3`$ has eigenvalue $`s=\pm1`$, the branches are
  ```math
  E_{\pm,s}=\pm\sqrt{\omega^2+(g_1+s g_2)^2}.
  ```
  These are analytic near the origin, and the lower branches have mutual terms $`-s g_1g_2/\omega`$. Nevertheless, their mutual terms cancel within each level, so all level responses at $`(x_1,x_2)`$ vanish. Consequently, the zero-level-response exception in Step 8 must not be interpreted as zero mutual cost for every eigenstate.

  Relatedly, the mixture construction cannot generally choose eigenvectors of the perturbed operator that continue an arbitrary prescribed basis of a degenerate level. The level-uniform density operator is well defined without such a choice.
- **Suggested fix:** Replace “only level sums” by “level sums are always analytic,” distinguish level-sum conclusions from individual-state conclusions, and formulate degenerate mixtures using spectral projectors rather than continuation of arbitrary basis vectors.

### I3. The example compares mutual components, not total costs
- **Location:** Step 8, item 2, sentence beginning Under either reading
- **Severity:** minor
- **Problem:** The displayed values correctly show reversal of the mutual component and of its neighbour-minus-end difference. They do not establish the corresponding claim for the total adapted cost $`E_n`$, because the one-source terms also depend on the chosen sites.

  In fact, set $`g_1=g_2=g>0`$. In both the lowest and highest unperturbed eigenvectors, the site probabilities are $`(1/4,1/2,1/4)`$. Therefore
  ```math
  E_n(\text{sources at }1,2)-E_n(\text{sources at }1,3)
  =\frac g4+O(g^2/t)>0
  ```
  for sufficiently small $`g`$, in both states. Thus the claimed opposite close-versus-far behaviour is not true of the total cost in this example. The earlier warning that the sign of $`W`$ alone does not determine a separation preference is correct, but the later wording obscures that distinction.
- **Suggested fix:** State explicitly that the example compares only the subtracted mutual cost $`W`$. Do not describe it as opposite behaviour of the total cost unless the position-dependent one-source contributions are included.

### I4. Fully degenerate field contracts are omitted from the gap conventions
- **Location:** Setup and assumptions, Spectral notation and Regime; Steps 3–6
- **Severity:** minor
- **Problem:** The stated class includes $`C_f=\epsilon\mathbb 1`$, including a one-dimensional field. Then the sets defining $`\Delta_n`$ and $`\Delta_{\min}`$ are empty, so the minima and the stated perturbative regimes are undefined. This case is not covered by the formulas as presently conditioned, despite the claimed scope of every finite field.
- **Suggested fix:** Treat a one-level field separately, where $`C_f(g)=\epsilon\mathbb 1+V`$ is already the exact degenerate effective operator, or explicitly introduce an infinite-gap convention and explain its interpretation.

## Focus points

None given.
