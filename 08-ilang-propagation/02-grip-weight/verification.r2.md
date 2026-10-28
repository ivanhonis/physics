# External verification: 02-grip-weight

- **Subproject:** 08-ilang-propagation
- **Package:** 02-grip-weight
- **Verified version:** v2
- **External round:** 2 of 3
- **Date:** 2026-10-24T20:28:29+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The source-shift argument, exact single-body quadratic formulas, and leading perturbative formulas for costs and weights are consistent with the supplied numerical checks. The leading square-grip criterion is also supported by the derivation. Some claims about compression limits, finite-dimensional eigenvalue branches, and domains of exact formulas need correction or additional justification; the large-distance midpoint approximation also needs its lattice-error restriction restored.

## Issues

### I1. Incorrect relative-form-bound claim
- **Location:** Step 1, “Limit”
- **Severity:** minor
- **Problem:** The statement that every stable G2 perturbation is form-bounded relative to $`H`$ with bound less than one is false. Stability permits arbitrarily large positive $`\mu F_2`$, whereas the relative form bound of the positive quadratic perturbation need not be below one. The convergence conclusion remains valid, but the stated sufficient-condition argument does not cover all the stable grips claimed.
- **Suggested fix:** For stable quadratic contracts, use positivity of $`K'`$ and equivalence of the positive quadratic-form norms to establish the Hermite form core and Rayleigh–Ritz convergence. Reserve the relative-bound-less-than-one argument for the subclass satisfying that additional condition.

### I2. Convergence of unbounded-grip Taylor coefficients needs a weighted estimate
- **Location:** Step 5, “Consequences of the class”, item (iv)
- **Severity:** minor
- **Problem:** Strong resolvent convergence and convergence of the isolated spectral gap do not, by themselves, imply convergence of perturbation coefficients involving an unbounded polynomially growing multiplication operator. The essential assertion—uniform control of polynomially weighted compressed eigenvectors—is stated without justification, and higher coefficients also involve reduced resolvents and intermediate vectors. The bounded trigonometric example in the code does not establish this assertion for the full stated class. I have not identified a counterexample for these particular quadratic Galerkin spaces, but the missing estimate is needed for the claimed coefficientwise limit.
- **Suggested fix:** Supply a short weighted Galerkin argument establishing convergence in the polynomially weighted norms required by $`F`$, together with the corresponding reduced-resolvent estimates. Alternatively, limit the convergence claim to the coefficients and grip subclasses actually justified.

### I3. Incorrect characterization of the continued finite-dimensional eigenvalue
- **Location:** Step 5, “Where this eigenvalue is the lowest”, final paragraph
- **Severity:** minor
- **Problem:** When the uncompressed contract is unbounded below, it does not follow that the eigenvalue of $`C_M`$ connected to the ground eigenvalue at zero coupling ceases to be the lowest outside a shrinking coupling interval. At finite $`M`$, avoided crossings can keep that continued branch lowest throughout; its value can then tend to $`-\infty`$ at fixed nonzero coupling. Loss of a uniform perturbative neighbourhood and loss of lowest-eigenvalue ordering are different statements.
- **Suggested fix:** Replace the asserted loss of lowest-eigenvalue status by the valid statement about the absence of a uniform perturbative neighbourhood as $`M\to\infty`$. Explicitly distinguish formal coefficientwise orders such as $`O(\theta^3)`$ from remainder bounds for an actual limiting eigenvalue when that eigenvalue does not exist.

### I4. Two-body stability criterion includes unnecessary single-body conditions
- **Location:** Step 3, immediately after Eq. (2.5)
- **Severity:** minor
- **Problem:** $`D_1,D_2>0`$ and $`\Delta_2>0`$ are not necessary for positivity of the two-body quadratic matrix itself. A positive quadratic term at one site can stabilize a negative term that would make the other single-body description unstable. For example, after adding $`a_2>0`$, the relevant inverse diagonal at site 1 is
  ```math
  b=G_0-\frac{a_2G(r)^2}{1+a_2G_0}<G_0.
  ```
  Choosing $`-1/b<a_1<-1/G_0`$ gives a stable pair although $`D_1<0`$. The stronger conditions are appropriate when both single-body reference costs must also exist, as required by the subsequent bond subtraction.
- **Suggested fix:** Qualify the stated criterion as the condition that the pair and both single-body reference descriptions are stable. Do not present it as an unrestricted necessary-and-sufficient condition for pair stability alone.

### I5. Exact bond-ratio factorization has an unlisted singular case
- **Location:** Step 7(b), Eq. (2.16), and “Reference and excluded members”
- **Severity:** minor
- **Problem:** Equation (2.16) divides by $`U_{\rm cl}`$ and $`v^T\mathbb Mv`$, but the exclusions only remove $`U=0`$. For different grips, $`U_{\rm cl}`$ can vanish while $`Z_b\ne0`$, so the bond and its weighing ratio remain defined although the displayed factorization is undefined. With $`a_1,a_2>0`$, $`\mathbb M`$ is indefinite at distinct sites, allowing nonzero choices of $`v`$ with $`v^T\mathbb Mv=0`$; meanwhile $`Z_b<0`$.
- **Suggested fix:** State Eq. (2.16) only for $`U_{\rm cl}\ne0`$, and provide the unfactored ratio obtained directly from Eq. (2.13) for the remaining cases. These cases need not be excluded from the physical weighing ratio.

### I6. Large-distance midpoint approximation omits lattice errors
- **Location:** Step 6, large-distance midpoint-factor bullet; corresponding Result bullet
- **Severity:** minor
- **Problem:** The formula
  ```math
  m_{\mathbf r}=\cosh\!\left(\frac{\mathbf r\cdot\hat d}{2\ell}\right)
  \left[1+O\!\left(\frac{|r|}{d}+\frac{|r|^2}{d\ell}\right)\right]
  ```
  is stated for $`d\gg\ell`$ without the upper-distance restriction or lattice correction introduced in Step 2. At fixed large $`\ell`$, its displayed error vanishes as $`d\to\infty`$, but even in one dimension the exact limit is $`\cosh(\alpha r/2)`$, with $`\alpha\ne\ell^{-1}`$. In higher dimensions the asymptotic local decay vector is also generally not $`\hat d/\ell`$.
- **Suggested fix:** Carry the continuum restriction, such as $`d\ll\ell^3`$, explicitly into this statement and its summary, or include the lattice correction and formulate the unrestricted asymptotic using the appropriate lattice saddle-point decay vector.

## Focus points

None given.
