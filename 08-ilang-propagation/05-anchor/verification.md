# External verification: 05-anchor

- **Subproject:** 08-ilang-propagation
- **Package:** 05-anchor
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-25T08:12:15+01:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The finite-volume quadratic reduction, anchored inverse, and second-order cost and weight formulas are largely correct, and the supplied numerical checks support the configurations actually tested. However, the claimed universal weighing result far from the anchor is false for some admitted placements: the anchor contribution can remain leading when the direct source contribution cancels between placements. The pair conclusion also needs the multi-body stability condition, not merely the individual-body conditions. Several smaller issues concern the line classification, weak-grip control, and the stated coverage of the numerical checks.

## Issues

### I1. Distance from the anchor does not suffice for universal weighing
- **Location:** Step 8, Eqs. (5.23)–(5.24), Result 14
- **Severity:** major
- **Problem:** The assertion that $`d/R\to\infty`$ makes $`a_{\rm mark}`$ and $`a_{\rm bond}`$ vanish for all admitted placements needs a non-cancellation condition on the source-induced placement difference. The stated condition $`\delta\cdot\hat e_s\ne0`$ is insufficient for finite differences.

  For an explicit counterexample on the infinite cubic lattice, take
  ```math
  h=0,\quad x=(d,0,0),\quad x'=(d+2,0,0),\quad x_s=(d+1,R,0),
  ```
  with $`R\gg1`$ fixed and $`d\to\infty`$. Reflection symmetry gives
  $`g_\infty(x-x_s)=g_\infty(x'-x_s)`$. Writing
  $`t=g_\infty(x-h)-g_\infty(x'-h)\ne0`$, the exact formulas yield
  ```math
  \Delta\Gamma=-2t,\qquad \Delta\phi_a=g_st,
  ```
  and therefore
  ```math
  a_{\rm mark}
  =-\frac{2\bar\phi_a}{g_s\bar\Gamma}
  \longrightarrow
  \frac{2[c_\phi+g_\infty((1,R,0))]}{\Gamma_\infty}\ne0.
  ```
  These placements satisfy $`d\gg R\gg1`$, $`|\delta|\ll R`$, and the stated nonzero-projection condition. The weighing denominator is nonzero at every finite $`d`$, so this is not an excluded member. Consequently, common square grips do not give $`\rho_{\rm mark}\to1`$ throughout the claimed class.
- **Suggested fix:** Restrict the far-anchor theorem to placements whose direct source-induced difference has a controlled nonzero leading term, and retain the appropriate finite-displacement and $`R/d`$ errors. For unrestricted placements, use the exact expressions (5.20)–(5.21), without asserting that distance alone removes the anchor terms.

### I2. Individual stability conditions do not establish existence for a pair
- **Location:** Step 8, cubic-torus conclusion, Result 14
- **Severity:** major
- **Problem:** The pair weighing conclusion is stated under $`2M_k|F_2|\Gamma(x)<1`$, which is only the single-body condition. Two bodies can satisfy their individual conditions while their joint quadratic contract has no lowest eigenvector.

  For example, for two equal negative updates $`\alpha_1=\alpha_2=-a`$, translated far from the anchor at fixed separation, the restricted inverse matrix tends to
  ```math
  \Gamma_2=
  \begin{pmatrix}
  \Gamma_\infty&G_{12}\\
  G_{12}&\Gamma_\infty
  \end{pmatrix},
  \qquad G_{12}=c_\phi+g_\infty(\mathbf r)>0.
  ```
  Individual stability requires $`a\Gamma_\infty<1`$, whereas joint stability requires
  ```math
  a(\Gamma_\infty+G_{12})<1.
  ```
  Choosing $`1/(\Gamma_\infty+G_{12})<a<1/\Gamma_\infty`$ satisfies the stated individual conditions but makes the pair contract unstable. The formal coefficients around $`s=0`$ still exist, but they cannot then describe weighing in the lowest eigenvector of the stated full-grip pair contract.
- **Suggested fix:** Carry the full condition $`\Gamma_n^{-1}+\mathcal A>0`$ from (5.10) into every pair conclusion, for all claimed branch and level choices. Distinguish formal expansion coefficients from statements about an existing state at $`s=1`$.

### I3. The line classification omits placements that straddle the source or anchor
- **Location:** Step 8, line discussion preceding Eq. (5.25), Result 15
- **Severity:** minor
- **Problem:** It is false that the only members with $`\Delta\phi_a\ne0`$ have the body or pair between the anchor and source. A comparison can have one placement inside that interval and another outside it.

  For instance, on the line with $`h=0`$, source at $`a>1`$, and body placements $`x=a+1`$, $`x'=a-1`$,
  ```math
  \Delta\phi_a=-g_s/\kappa_h\ne0,
  ```
  but $`\phi_a(x)\ne-g_s\Gamma(x)`$. Thus $`a_{\rm mark}=1`$ and the ensuing classification do not cover all allowed nonzero-weight comparisons.
- **Suggested fix:** State explicitly that (5.25) requires both placements—and both members of the pair—to remain wholly between the anchor and source. Cover the other allowed comparisons through the piecewise field and the exact ratio formulas.

### I4. The weak-grip parameter is not valid for all real quadratic grips
- **Location:** Step 8, definition of ε² before Eq. (5.22)
- **Severity:** minor
- **Problem:** The maximum defining $`\varepsilon^2`$ contains the signed quantity $`\hat\beta\hat b\,\bar w=F_2\bar w/F_0`$. When $`F_0F_2<0`$, this term is negative and can have large magnitude without making the stated $`\varepsilon^2`$ large. Taking $`F_1`$ large can simultaneously make $`\hat\beta^2\bar\Sigma/\bar\Gamma`$ small, even though the numerator correction $`F_2\bar w/F_0`$ is order one or larger. The claimed expansion is then uncontrolled despite the stated criterion. The parameterization is also undefined for the admitted case $`F_0=0`$.
- **Suggested fix:** Use absolute values for every smallness requirement and give a separate treatment of $`F_0=0`$. State the leading-order classification only within that controlled regime.

### I5. The claimed numerical coverage of bond ratios exceeds the code
- **Location:** Step 8 numerical-validation paragraph, Code section, check_anchor.py function part_iii
- **Severity:** minor
- **Problem:** The text says that the bond ratios were checked for square, non-square, $`8F_0F_2=F_1^2`$, and linear grips. In the supplied code, the bond calculation uses only `"square"` grips; the other grips occur only in the single-body checks. In particular, neither the linear-grip bond ratio nor the general different-grip formula is numerically checked. The supplied output reflects this narrower coverage.
- **Suggested fix:** Narrow the validation claims to the cases actually tested, or add the claimed bond checks.

## Focus points

None given.
