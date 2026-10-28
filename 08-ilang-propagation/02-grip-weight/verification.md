# External verification: 02-grip-weight

- **Subproject:** 08-ilang-propagation
- **Package:** 02-grip-weight
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-24T19:40:42+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The exact single-body quadratic formulas and the common-grip quadratic bond formulas are largely consistent, and the supplied numerical outputs support those formulas in the tested regimes. However, the general-grip results require assumptions not supplied by the stated class, and the square-grip criterion does not follow from the local derivative assumptions used to derive it. The treatment also leaves different grips on the two bodies unresolved and overstates the validity of several distance asymptotics. These affect substantive parts of items 2–4, rather than only presentation.

## Issues

### I1. The general-grip formulas lack sufficient domain and regularity assumptions
- **Location:** Setup; Step 1, Limit; Step 5, Eqs. (2.9)–(2.10)
- **Severity:** major
- **Problem:** Class (G) assumes smoothness only at zero, whereas the calculation uses derivatives of every order over the entire Gaussian distribution, differentiates their averages, and asserts convergence of compressed perturbation coefficients. Even the additional condition $`\mathrm{Var}F(q_x)<\infty`$ does not justify these operations. For example,
  ```math
  f(q)=\sin\!\bigl(q+e^{q^4}-1\bigr)
  ```
  is bounded, globally smooth, has $`f(0)=0`$ and $`f'(0)=1`$, and gives a well-defined bounded perturbation with an isolated lowest eigenvalue for sufficiently small θ. Nevertheless, its derivatives need not have absolutely convergent Gaussian averages, so the stated $`a_n`$ are not defined as ordinary expectations. Other grips permitted by the original class grow so rapidly that even the matrix elements defining $`\Pi F(q)\Pi`$ diverge. The blanket form-core and min-max assertions consequently do not apply to the whole class.
- **Suggested fix:** State explicit admissibility, domain, Gaussian-integrability, differentiation, and perturbation assumptions. Alternatively, formulate the second-order answer using Hermite coefficients and state the summability conditions needed for its shift derivative. Delimit the original class members for which the requested coefficients or compressed contracts do not exist.

### I2. Local derivative bounds do not imply the square-grip criterion
- **Location:** Step 7(c)–(d), Eqs. (2.17)–(2.18)
- **Severity:** major
- **Problem:** The assumption $`F^{(n)}(0)=O(F(0)\beta^n)`$ controls only the Taylor jet at zero. It does not imply
  ```math
  \langle F^{(n)}(q)\rangle_0
  =F^{(n)}(0)+O(F(0)\beta^n\varepsilon^2),
  ```
  because the Gaussian samples values away from zero. A counterexample is
  ```math
  F_\beta(q)=F_0\bigl[(1+\beta q)^2+\beta h(q)\bigr],
  ```
  where $`h`$ is a smooth compactly supported bump vanishing near zero and chosen with $`\langle h''\rangle_0\ne0`$. This family satisfies all the displayed derivative assumptions and the square condition at zero, but
  ```math
  a_2=F_0\bigl(2\beta^2+\beta\langle h''\rangle_0\bigr),
  ```
  contradicting the claimed average expansion. Such grips have well-defined Gaussian moments and stable contracts for sufficiently small β. Thus the asserted criterion is not a theorem under its stated assumptions.
- **Suggested fix:** Impose global control of the grip on the fluctuation scale—for example a fixed scaled shape $`F(q)=F_0\Phi(\beta q)`$, together with appropriate tail and derivative bounds—and derive the error estimate under those conditions. Restrict Eqs. (2.17)–(2.18) and the corresponding result statements accordingly.

### I3. Different grips on the two bodies are not covered by the bond conclusions
- **Location:** Step 6, Eqs. (2.11)–(2.13); Step 7, excluded members and bond ratios
- **Severity:** major
- **Problem:** The question permits two grips of the same class, not necessarily the same grip. Equation (2.11) initially allows different grips, but the weight, exact quadratic ratio, and classification subsequently specialize to a common grip. This also invalidates the unrestricted statement that a (G2) bond never vanishes and that its classical and zero-point parts have the same sign. For example, take quadratic grips with linear coefficient $`b`$ in both bodies and quadratic coefficients $`c`$ and $`-c`$. Their leading bond is
  ```math
  -\mu_1\mu_2\bigl[b^2G(r)-4c^2J_2(r)\bigr],
  ```
  which vanishes when $`c^2=b^2G(r)/(4J_2(r))`$. Scaling the grips sufficiently small preserves stability. These cancellations are not among the listed exclusions.
- **Suggested fix:** Retain separate grip coefficients in the bond weight and ratio calculations, and identify vanishing bond profiles and denominators. State the common-grip results as a specialization, not as the answer for the entire requested class.

### I4. The first-order pair reference is not equal to the stated midpoint reference
- **Location:** Step 7, Reference and excluded members; code/v1/check_g2_ratios.py, bond normalization
- **Severity:** minor
- **Problem:** The assertion that the single-body midpoint reference equals the pair’s first-order weight per unit first-order cost whenever $`\mu_1+\mu_2\ne0`$ is false without a field-uniformity approximation. For a common grip, the actual pair quantity is
  ```math
  \frac{\Delta W_{12}^{(1)}}{C_{12}^{(1)}}
  =\frac{a_1}{a_0}
  \frac{\mu_1\Delta\phi_1+\mu_2\Delta\phi_2}{\mu_1+\mu_2},
  ```
  not $`(a_1/a_0)\Delta\bar\phi`$. Even for equal labels it contains the midpoint factor $`m_{\mathbf r}`$. Moreover, the question explicitly requests exclusion of pairs whose first-order costs cancel, whereas the code includes such pairs using a replacement single-body reference. The wording “referred to the midpoint” needs clarification to settle which normalization is intended.
- **Suggested fix:** Distinguish the exact pair normalization from a stipulated single-body midpoint normalization, and state any slowly varying field approximation needed to identify them. Explicitly exclude the requested cancellation cases rather than silently changing their reference.

### I5. The lattice and midpoint asymptotics are used outside their controlled ranges
- **Location:** Step 2, Eq. (2.4); Step 6, midpoint-factor asymptotics; Step 7(e)
- **Severity:** major
- **Problem:** The continuum screened profiles are not large-distance asymptotics with relative errors $`O(d^{-2},\ell^{-2})`$ for arbitrary fixed $`\ell`$. They require a weak-pinning scaling regime. The exact chain formula already demonstrates the problem:
  ```math
  \alpha=\ell^{-1}-\frac{1}{24\ell^3}+O(\ell^{-5}),
  ```
  so replacing $`e^{-\alpha d}`$ by $`e^{-d/\ell}`$ produces an exponent error of order $`d/\ell^3`$, which grows at large distance. In higher dimensions the fixed-pinning lattice decay is also direction dependent. Separately, the screened midpoint Taylor expansion requires $`|r|/\ell\ll1`$, not merely $`d\gg|r|`$; its fourth-order remainder is not generally $`O(|r|^4/d^4)`$. The exact one-dimensional $`\cosh(\alpha r/2)`$ makes this distinction explicit.
- **Suggested fix:** State the continuum scaling limit and its uniform distance range, or supply the fixed-pinning lattice asymptotics outside that range. Require both the appropriate source-distance condition and $`|r|\ll\ell`$ when expanding the screened midpoint factor, with corresponding error terms.

### I6. The bond ratio is incorrectly described as distance independent
- **Location:** Step 7(a), following Eq. (2.14); Result, paragraph beginning “(2.14), formula”
- **Severity:** minor
- **Problem:** Equation (2.14) gives $`\rho_{\rm bond}=m_{\mathbf r}\rho(\mathbf r)`$. The intrinsic factor $`\rho(\mathbf r)`$ is independent of the source distance, but $`m_{\mathbf r}`$ generally is not. The supplied cubic-torus data demonstrate this directly: for $`L=8`$, square grip, equal labels and $`r=2`$, the exact bond ratio changes from approximately 0.5226 to 0.7049 to 0.8008 as the midpoint distance changes. Thus the stated distance independence of both ratios contradicts both the formula and the output.
- **Suggested fix:** State distance independence only for $`\rho_{\rm mark}`$ and for $`\rho_{\rm bond}/m_{\mathbf r}`$, within the common-grip perturbative calculation. Preserve the geometric source-distance dependence in the actual bond ratio.

### I7. Vanishing second-order mark weights are not carried to their first nonzero order
- **Location:** Step 5, following Eq. (2.10); Step 7(f), Eq. (2.20)(iii)
- **Severity:** minor
- **Problem:** From $`S,T=O(\theta^2)`$, it does not follow that both the mark and its weight first appear at order $`\theta^2`$. For instance, an odd bounded grip shape such as $`f(q)=\sin q`$ has alternating vanishing Gaussian derivative averages, hence $`T=0`$, while $`S>0`$. Parity makes the next possible correction to the mark weight cubic in θ. The derivation acknowledges $`T_f=0`$ later but does not determine the first nonzero weight or the resulting weighing ratio for these admissible members. The linear grip is a different special case, with identically zero mark weight.
- **Suggested fix:** Separate nonzero-$`T`$ grips from cancellation cases. For the latter, calculate the first nonzero weight where required, or explicitly delimit which parts of the requested lowest-order answer remain unresolved.

### I8. The blanket statement about massless limits is false
- **Location:** Step 7, Dependence on m_h and L; Result, final paragraph
- **Severity:** minor
- **Problem:** “Costs and ratios have no limit” as $`m_h\to0`$ at fixed $`L`$ is too strong. The linear-grip ratios are identically zero for every positive $`m_h`$, so they do have a limit, despite the divergent cost. Also, for a quadratic grip the loss of stability in one branch does not imply absence of a limit in each individually stable sector. For example, when $`\mu F_2>0`$, the local positive quadratic term pins the finite-volume uniform mode and the cost can have a finite limit.
- **Suggested fix:** Distinguish failure of a simultaneous two-branch continuation from limits of individual sectors and individual observables. State the linear-grip ratio limit explicitly.

### I9. The required general-grip compression check does not compare against an uncompressed eigenvalue
- **Location:** code/v1/check_compression.py; Code section, check (ii)
- **Severity:** minor
- **Problem:** For (G2), the code compares compressed lowest eigenvalues with the exact uncompressed value as required. For (G), however, `E_theta_2nd_order` is only the second-order perturbative expression, not the uncompressed lowest eigenvalue. The residual $`1.4\times10^{-5}`$ therefore mixes the perturbative truncation error with any compression error. A single value of θ also does not establish the claimed cubic scaling. This is useful coefficient checking, but it is not the requested finite-θ eigenvalue comparison.
- **Suggested fix:** Obtain an independently converged uncompressed reference for the selected bounded grip and compare $`C_M`$ with it. If retaining the cubic-error claim, check several θ values or provide a bound establishing that order.

## Focus points

None given.
