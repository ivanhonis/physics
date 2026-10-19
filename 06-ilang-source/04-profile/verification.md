# External verification: 04-profile

- **Subproject:** 06-ilang-source
- **Package:** 04-profile
- **Verified version:** v2
- **External round:** 1 of 3
- **Date:** 2026-10-19T09:43:25+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The reduction to a single field object, the second-order resolvent formula, and the ring profile are correct, and the supplied numerical checks support those calculations. The treatment of split dependence also usefully distinguishes the mutual-cost convention from invariant differences of total costs. However, the proposed gapped control has an exponentially decaying second-order coefficient, not an exponentially decaying full mutual cost, and the claimed large-volume accuracy ranges are not established by the third-order calculation alone. There are also smaller qualifications needed for the exact ring equation and the asymptotic formulas.

## Issues

### I1. The control field does not have a short-range full mutual cost
- **Location:** Step 7, control field; Eq. (4.14); Result (4.14)
- **Severity:** major
- **Problem:** Equation (4.14) correctly establishes exponential decay at second order, but this particular control has a distance-independent mutual contribution at fourth order. For one field object, eliminating the excited block gives
  ```math
  \varepsilon=-v^\dagger(K-\varepsilon)^{-1}v,\qquad
  v=g_1|x_1\rangle+g_2|x_2\rangle.
  ```
  On an infinite chain, put $`A_0=K^{-1}(x,x)>0`$ and $`B_0=K^{-2}(x,x)>0`$. As the separation tends to infinity, the off-diagonal resolvent entries vanish, but
  ```math
  M(d)\longrightarrow
  2N_f g_1^2g_2^2 A_0B_0+O(g^6),
  ```
  rather than zero. Both sources share the same single empty place, so their self-energy responses are not independent even at arbitrarily large separation. Consequently, small coupling compared with the gap does not make (4.14) a uniformly accurate relative approximation at large distance. Subtracting the total cost at a far-source configuration removes this constant, but that is not the mutual cost defined in (4.1).
- **Suggested fix:** Explicitly limit this example to exponential decay of the second-order coefficient and acknowledge that it does not establish the requested short-range full mutual cost. To complete item 3, provide an admissible control whose full mutual cost has the claimed decay, with its approximation regime stated.

### I2. The stated accuracy ranges lack higher-order control
- **Location:** Step 5; Eq. (4.9); Result (4.9)
- **Severity:** major
- **Problem:** The third-order calculation identifies plausible expansion parameters, but it does not establish that the second-order expression has relative accuracy $`\epsilon`$ throughout the stated ranges. In particular, the square and cubic criteria permit couplings far outside the only convergence regime actually supplied, $`\|V\|<2t_f\sin^2(\pi/L)`$. No argument controls fourth and higher orders uniformly in $`L`$ in those enlarged regimes. The ring computations support selected equal-source cases, but do not supply that missing control for the stated class. Calling the criteria “leading order” and listing the missing remainder estimate under Open issues does not establish the quantitative accuracy claim needed by item 2.
- **Suggested fix:** Add a short finite-rank resolvent or secular-equation argument showing that higher orders are controlled by the proposed dimension-dependent small parameters, including the normalization used near zeros of $`M^{(2)}`$. Otherwise restrict the accuracy claim to a justified fixed-size or norm-gap regime and present (4.9) only as an estimated breakdown scale.

### I3. The exact ring prescription omits eigenvalues at resolvent poles
- **Location:** Step 6; Eqs. (4.10)–(4.12); Result (4.10)–(4.12)
- **Severity:** minor
- **Problem:** The determinant equation is derived only for $`\varepsilon\notin\mathrm{spec}C_1`$, but the subsequent root prescription is presented as covering every real pair of couplings. Nonzero mixed-sign couplings can put the lowest eigenvalue exactly at the unperturbed lowest eigenvalue, which is excluded from both prescribed open root intervals. For example, on a four-place ring with $`t_f=1`$, opposite sources $`g_1=1`$, $`g_2=-1/2`$ have lowest eigenvalue $`-2`$: the positive vector $`(1,3/2,2,3/2)`$ is its eigenvector. Here $`q=0`$, and (4.10) is undefined.
- **Suggested fix:** Include the spectral-pole cases explicitly, for example through a pole-cleared characteristic equation with the appropriate limiting prescription. State how the $`q=0`$ case is selected.

### I4. A large-ring third-order expression is written as an exact identity
- **Location:** Step 5, Ring paragraph
- **Severity:** minor
- **Problem:** After using $`\ell^{(2)}_d=L^3c+O(L)`$, the derivation says that the bracket in (4.8) “is” $`L^2(1-10w+20w^2)/60`$, and then gives an equality for $`M^{(3)}/M^{(2)}`$. These are large-$`L`$ expressions, not finite-ring identities. The exact bracket is
  ```math
  \frac{L^2}{60}(1-10w+20w^2)
  -\frac1{12}+\frac w3+\frac1{15L^2}.
  ```
  The denominator of the exact ratio also retains the $`1/(6L^2)`$ term in (4.5). The code correctly uses the exact matrix expression, so this is a qualification missing from the text rather than an error in that numerical check.
- **Suggested fix:** Mark both displayed expressions as large-$`L`$ approximations and retain their error terms, or supply the finite-$`L`$ expressions.

### I5. Radial monotonicity is overstated for the tori
- **Location:** Step 4; Results (4.6) and (4.7)
- **Severity:** minor
- **Problem:** The leading continuum terms are radial and increase with $`|\mathbf d|`$ for $`g_1g_2>0`$, but the exact second-order lattice sums are not functions of $`|\mathbf d|`$ alone. Lattice corrections and the higher finite-torus terms depend on direction. Thus the unqualified statements that, “at second order,” the total cost increases with $`|\mathbf d|`$ are stronger than the derived leading asymptotics. Mean subtraction in (4.17) does not remove this anisotropy.
- **Suggested fix:** State radial dependence and monotonicity only at the leading continuum order, with the displayed lattice and finite-size errors. Keep exact finite-torus statements expressed in terms of the vector separation.

## Focus points

None given.
