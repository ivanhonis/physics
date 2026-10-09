# External verification: 22-large-scale-geometry

- **Subproject:** 03-ilang-space
- **Package:** 22-large-scale-geometry
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-09T08:22:14+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The main explicit distance formulas and continuum limits are largely sound, including the Euclidean and taxicab squares, the qubit spherical-cap regimes, and the exponential-tail limits. However, the compact-window calculation leaves a requested range of finite-size chain distances and diameters undetermined. The periodic no-isotropy conclusion also needs qualifications connecting the family of descriptions to a fixed periodic weighted graph.

## Issues

### I1. Compact-window distances and diameters remain undetermined
- **Location:** Step 7, Eqs. (22.16)–(22.17); first item under “Open issues”
- **Severity:** major
- **Problem:** For $`2m\le n\le6m-5`$, the derivation leaves $`\ell_{\ge2}`$ as another shortest-chain optimization in the same graph. This does not determine $`\ell`$ for the affected pairs. Likewise, the diameter is evaluated only in the large-$`n`$ regime; the remaining intermediate sizes receive only an upper bound. Item 2(a) explicitly requires determining $`\ell`$ and the diameter for the stated family, not merely their eventual behavior. The acknowledged omission does not affect the negative continuum result, but it leaves this requested calculation incomplete.
- **Suggested fix:** Evaluate the intermediate-size shortest-chain contribution and the resulting diameter for all remaining $`n,m,\lambda`$, rather than retaining $`\ell_{\ge2}`$ as an unevaluated optimization.

### I2. Periodic no-isotropy conclusion needs fixed-family qualifications
- **Location:** Step 10, application of (P1)–(P2), Eq. (22.29)
- **Severity:** minor
- **Problem:** The stated standard results concern one fixed periodic weighted graph, subsequently viewed on specified expanding domains. The application does not explicitly establish that the family has a fixed graph, fixed weights and a fixed finite quotient independent of $`n`$, or that its finite-description chain metrics agree with the metrics used in (P1). Finitely many edge orbits in each member separately does not suffice: a sequence of polygonal unit balls can converge to an ellipse. Boundary truncation or recomputation of the neighbour graph also requires clarification before applying the ambient-graph theorem. Thus the unconditional word “never” is broader than the application as written establishes.
- **Suggested fix:** State explicitly the fixed-periodic-pattern and growing-domain assumptions, and identify the finite-description metrics with those covered by the theorem. Under those conditions, the polygonal stable-norm conclusion is justified; otherwise qualify (22.29). Clarifying the intended family would settle this issue.

### I3. The claimed exhaustive small-$`\lambda`$ dichotomy excludes window ties
- **Location:** Step 2, “In every family below, each pair falls under (N1) or (N2)”
- **Severity:** minor
- **Problem:** This statement is false for the compact-window family. For example, take $`m=2,n=4`$ and the pair $`h_1,h_4`$. Its $`d_0`$-distance is $`2`$, and $`y=h_2`$ gives
  ```math
  \max\{d_0(h_1,h_2),d_0(h_2,h_4)\}
  =\max\{\sqrt2,2\}=2.
  ```
  Neither intermediate point gives a strict witness, so (N1) fails, while equality makes (N2) fail. Step 6 subsequently resolves these ties correctly using the exact angle formula, so the window result is not invalidated, but the universal claim and its stated justification are incorrect.
- **Suggested fix:** Exclude the compact-window family from this assertion and explicitly invoke its separate exact tie analysis when establishing its stable graph and small-$`\lambda`$ chain limit.

### I4. A general shortest path does not project to a closed walk
- **Location:** Step 10, explanatory “Reason” under (P2)
- **Severity:** minor
- **Problem:** A path projects to a closed walk in the quotient graph only when its endpoints belong to the same vertex orbit. A general shortest path between arbitrary vertices need not satisfy this condition. The polygonal stable-norm fact can remain valid, but the offered explanation is false as stated.
- **Suggested fix:** Restrict the explanation to translation paths whose endpoints project to the same quotient vertex, or account for bounded connecting paths between quotient vertices. Alternatively, omit this explanation and retain the standard result as stated.

## Focus points

None given.
