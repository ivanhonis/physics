# External verification: 03-gas-grip

- **Subproject:** 08-ilang-propagation
- **Package:** 03-gas-grip
- **Verified version:** v3
- **External round:** 1 of 3
- **Date:** 2026-10-24T19:31:46+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The characterization of admissible grips as affine functions, and the reduction of their weights to the full-grip results, are sound. However, the subsequent geometric classification relies on nonuniform estimates for ratios of lattice-kernel differences: excluding an exactly zero denominator does not justify the stated bounds. This affects the claimed regimes in which the self-cost and the bond are weighed alike. There are also missing cancellation exclusions and an explicitly unresolved source geometry within the requested scope.

## Issues

### I1. Uncontrolled difference quotients invalidate the geometric classification
- **Location:** Step 4, Eq. (3.14), and the conclusions in Eqs. (3.8) and (3.11)
- **Severity:** major
- **Problem:** The assertions $`T_2=O(1)`$ on the square torus and $`T_2=O(|r||r'|/\mathcal X)`$ on the cubic torus do not follow from the displayed asymptotics for the individual kernels. Here
  ```math
  T_2=\frac{2[\ell^{(2)}]}{\mathcal X[\ell]},
  ```
  and the only imposed restriction is $`[\ell]\ne0`$. Differences of $`\ell`$ can be anomalously small without corresponding cancellation of $`[\ell^{(2)}]`$.

  This is a genuine obstruction for arbitrary comparisons, not merely an issue with bounding individual error terms. At macroscopic positions on a growing square torus, $`\ell(Ls)`$ approaches the continuum torus inverse-Laplacian kernel $`G(s)`$, while $`\ell^{(2)}(Ls)/L^2`$ approaches its squared-inverse kernel $`H(s)`$. These kernels do not share all level sets. Approximating positions with $`G(s)=G(t)`$ but $`H(s)\ne H(t)`$ therefore produces nonzero denominators tending to zero while the numerator divided by $`\mathcal X`$ remains nonzero. Consequently, the asserted uniform estimate for $`T_2`$, and hence the stated distance-only estimates for $`\zeta`$, fail. The same conditioning problem also affects relative remainder estimates obtained after division by $`[\ell]`$.
- **Suggested fix:** Retain $`T_2`$ exactly unless a suitable non-degeneracy condition on the comparison is imposed and justified. State the allowed comparisons and propagate their conditioning into the remainders. Restrict the distance-only conclusions about $`\zeta`$ and simultaneous weighing accordingly.

### I2. The cubic squared-inverse asymptotic omits a finite-size correction
- **Location:** Step 4, paragraph “ζ on the three graphs,” cubic-torus bullet
- **Severity:** minor
- **Problem:** The formula
  ```math
  \ell^{(2)}(y)-\ell^{(2)}(0)=-\frac{|y|}{8\pi}+O(1)
  ```
  is stated without a range relating $`|y|`$ to $`L`$. On a finite cubic torus there is generally a correction of order $`|y|^2/L`$, which is not bounded when $`|y|`$ grows sufficiently rapidly with $`L`$. In particular, the stated formula is not valid uniformly over shortest representatives or at distances of order $`L`$, both of which are subsequently discussed.
- **Suggested fix:** Include the finite-size correction and specify the joint large-distance/large-size regime. Then check its contribution to the relevant difference quotients under the non-degeneracy conditions needed for I1.

### I3. Required cancellation exclusions are incomplete
- **Location:** Steps 3–6 and the exclusions accompanying Results (3.5)–(3.11)
- **Severity:** minor
- **Problem:** The question explicitly requires naming cancellations of costs and denominators. The derivation lists $`\beta=0`$, $`\alpha+\beta n=0`$, and $`[\ell]=0`$, but does not explicitly exclude $`g_s=0`$, zero bond-cost differences $`\Delta_{\mathbf r\mathbf r'}\ell=0`$, or zero source-gradient differences $`\Delta_{\mathbf e}\ell(\mathbf R)=0`$. These last two make the bond ratio undefined and occur naturally by graph symmetry. Exact total-cost and level-gap cancellations are also not named. For example, a particular state has zero total cost when
  ```math
  \alpha=-\frac{N_f[\varepsilon_0(\sigma\beta M_k)-\varepsilon_0(0)]}{\sigma M_k}.
  ```
  The condition $`|\mu|\chi\ll1`$ protects some asymptotic formulas from such cancellation, but does not supply the explicit cancellation accounting requested.
- **Suggested fix:** Add a consolidated list of the zero-denominator and cost-cancellation conditions, distinguishing exact cancellations from near-cancellations excluded by the perturbative regime. Attach these exclusions to every ratio that uses them.

### I4. The requested ring classification remains partly unresolved
- **Location:** Step 6, “Mark and bond together,” and Open issues
- **Severity:** minor
- **Problem:** The derivation expressly leaves the midpoint bond criterion unevaluated when the source lies on the arc between the bodies. That geometry was not removed from the package’s scope. The general factorization by $`1/\mu_i`$ remains useful there, but the announced determination of which grips weigh both contributions is supplied only in the geometries where the quoted midpoint result applies. In general, the leading conditions are $`\mu=1+\zeta`$ for the self-cost and $`\mu=\rho_0^{\rm mid}`$ for the bond; the latter has not been evaluated in this remaining ring case.
- **Suggested fix:** Evaluate the leading midpoint ratio from the supplied expression for $`S`$ in the source-on-arc geometry and complete the weighing criterion, including its denominator exclusions.

### I5. The nonlinear example is not an admissible control under A5
- **Location:** Step 7 and the reference to Eq. (3.12) as a control in Result (3.6)
- **Severity:** minor
- **Problem:** For $`N_f\ge2`$, the example $`F(\Phi)=\Phi^2`$ is proved to require a three-object term with the stated objects. It is therefore not an admissible Ilanguage description under A5 and cannot serve as the admissible control required by M9. Its binomial calculation is a valid mathematical illustration, but calling it a control does not satisfy that methodological requirement.
- **Suggested fix:** Label it explicitly as a mathematical illustration outside the admissible description class, and use an admissible affine grip as the control where appropriate—or state that the relevant exact characterization has no counterexample within its class.

## Focus points

None given.
