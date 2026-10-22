# External verification: 02-two-free-bodies

- **Subproject:** 07-ilang-weight
- **Package:** 02-two-free-bodies
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-20T22:59:02+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The lowest-state held-body calculation is sound: the exact separation and exchange symmetries, the second- and third-order mutual terms, and the failure of factorization are supported by the supplied code. The free-body analysis has substantial problems, however: it identifies a winding current with the derivative of a position operator on a finite ring, and it uses labeled states and observables that are inadmissible for identical-type bodies. The requested highest-state treatment on odd rings is also explicitly left unfinished. Additional issues concern conserved quantities, packet-width approximations, and the isolation conditions used in the numerical checks.

## Issues

### I1. Ring current is not the derivative of the stated mean position
- **Location:** Steps 5–6, Eqs. (2.12)–(2.13); check_mutual_fall.py, body_ops and run_case
- **Severity:** major
- **Problem:** The derivation uses $`[x_1,S_\pm]=\pm S_\pm`$, treating every forward ring hop as a displacement of $`+1`$. This is false for the diagonal coordinate operator $`X=\sum_{x=0}^{L-1}xP_x`$: for example,
  ```math
  [X,T]=T-L|0\rangle\langle L-1|.
  ```
  Consequently, the double-commutator calculation omits boundary terms. The code likewise assigns displacement $`+1`$ to every forward bond, including the wrapping bond; its velocity is a winding-current operator, not $`i[C,X]`$. Its evolution check therefore validates the acceleration of that current, not the claimed second derivative of the mean position. Arbitrary real envelopes in R3 do not justify neglecting the distinction.
- **Suggested fix:** Define the drift observable operationally and derive its relation to mean-position motion. If using a local coordinate chart, restrict the starts and evolution interval appropriately and bound the boundary-tail errors. Make the numerical observable match that definition, and include the corresponding finite-ring errors in (2.12)–(2.13).

### I2. Identical-type bodies are treated as labeled objects
- **Location:** Setup R3; Step 1; Steps 4–6; Consistency check 3
- **Severity:** major
- **Problem:** The stated class includes bodies of the same type, but the vectors $`e_{jl}`$ and the product-envelope start are generally not in the required swap-invariant or swap-sign-changing subspace. For such bodies, $`x_1`$, $`x_2`$, and the individual $`D_i`$ are also not label-invariant observables; in general they do not even preserve the admissible subspace. A mirror-symmetric pair of labeled envelopes is not, by itself, a symmetrized or antisymmetrized state. Thus the claimed individual accelerations and conservation statements are not well defined throughout the stated class, contrary to M6 and A6.
- **Suggested fix:** Perform the same-type calculation in the admissible family subspace and specify label-independent observables identifying the two spatial packets, where possible. Distinguishable types may be used for the labeled calculation, but the requested same-type cases require a separate admissible treatment.

### I3. Highest states on odd rings remain unanswered
- **Location:** Step 2; Step 3; Directions in Step 6; Open issues
- **Severity:** major
- **Problem:** The question’s scope includes every $`L\ge5`$, and item 3 requests the branch-dependent directions for both lowest and highest field states. The derivation handles highest states only for even $`L`$, explicitly leaving odd $`L`$ open. On odd rings the uncoupled highest level is degenerate, so neither the lowest-state perturbation calculation nor the even-ring spectral inversion settles the required eigenvalue branch, start dependence, leading mutual interaction, or acceleration directions. Acknowledging the degeneracy does not answer these requested cases.
- **Suggested fix:** Treat the degenerate highest eigenspace on odd rings, specify the admissible selected starts or branches, and derive the requested held interaction and free-body conclusions with their validity conditions.

### I4. An exact body-only conserved quantity is omitted
- **Location:** Step 1 and the conserved-quantities Result bullet
- **Severity:** minor
- **Problem:** For even $`L`$, each distinguishable body has the additional exact conserved operator
  ```math
  Q_i=\left(\sum_x(-1)^xP_x^{(i)}\right)\sigma_3^{(i)}.
  ```
  Position parity and $`\sigma_3`$ each anticommute with the motion hopping, so their product commutes with it, including the field-dependent bond factors of coupling (c). It also commutes with the rest coupling and the field contract. The answer concerning quantities conserved by the bodies alone therefore omits a nontrivial conserved quantity built directly from their places.
- **Suggested fix:** Include these conserved operators and their consequences. For identical-type bodies, state the corresponding permutation-invariant conserved combinations rather than labeled individual operators.

### I5. The correction evaluated at the mean separation needs another approximation
- **Location:** Step 7, the ratio formula following Eq. (2.16)
- **Severity:** minor
- **Problem:** Replacing the correction inside the acceleration sums by $`\bar M^{(2)}(\bar d)`$ is not justified merely by calling the packets “broad.” For equal Gaussian widths, the correction generally involves a force-weighted average of the smoothed mutual term,
  ```math
  \frac{\sum_{j,l}p_{jl}\,\bar M^{(2)}(l-j)\,\mathcal M'(l-j)}
  {\sum_{j,l}p_{jl}\,\mathcal M'(l-j)},
  ```
  not its value at the mean separation. Broad packets suppress lattice-envelope effects but need not be narrow relative to the spatial variation of the interaction. No additional scale hierarchy or error estimate is supplied.
- **Suggested fix:** Retain the weighted-average expression, or state a packet-size versus interaction-variation condition and estimate the error in replacing it by a value at $`\bar d`$.

### I6. The isolation conditions used analytically and numerically are incomplete
- **Location:** Setup R1; Step 4, Eq. (2.11); Code summary for check_mutual_fall.py
- **Severity:** minor
- **Problem:** Joint two-body isolation in R1 does not by itself establish isolation of the single-body levels used to define $`\bar\kappa`$ and the inertias. That additional condition is needed when importing (6.10). Moreover, the numerical claim “R1 holds: $`2M_i-4t_f\ge1.2`$” checks only a branch-energy separation, not the gap from the selected group to all other levels. Same-branch field excitations also matter: the uncoupled field gap for the numerical ring is $`4t_f\sin^2(\pi/14)\simeq0.099`$, comparable to or smaller than the largest motion amplitudes used. The overlap-based band-selection assertions do not establish the stated $`\tau_i\ll\delta`$ condition.
- **Suggested fix:** State the required single-body isolation assumptions explicitly. Compute and report the full relevant two-body and single-body spectral gaps for the numerical cases, and compare the motion-operator norms with those gaps; otherwise qualify which runs are outside the stated asymptotic regime.

## Focus points

None given.
