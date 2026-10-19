# External verification: 09-unsharp-field

- **Subproject:** 05-ilang-free-fall
- **Package:** 09-unsharp-field
- **Verified version:** v2
- **External round:** 1 of 2
- **Date:** 2026-10-11T13:56:46+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The exact sector mixture, conditional weights after readings, and first-order averaging of the fall are correctly derived. The rest-acceleration formulas, covariance conditions, and treatment of the mean record gradient are also consistent with the quoted inputs. The remaining problems concern the maximal-speed claim for position-dependent hopping, the interpretation of the narrow-distribution expansion, and several scope and degenerate-case qualifications.

## Issues

### I1. The maximal speed in S_c is only an unperturbed reference speed
- **Location:** Step 6, Eq. (9.16), maximal-speed row and following paragraph
- **Severity:** minor
- **Problem:** The stated value $`v^\nu_{\max}=n^\nu\tau d_0`$ does not equal the hopping-row-sum bound for the full sector contract when $`\gamma^\nu\ne0`$. At an interior position $`x`$, that row sum is
  ```math
  \frac{\tau d_0}{2}\left[n^\nu+\gamma^\nu(x-\tfrac12)+n^\nu+\gamma^\nu(x+\tfrac12)\right]
  =\tau d_0(n^\nu+\gamma^\nu x).
  ```
  Thus the global bound depends on the gradient and chain extent. The explanation that the bound “contains only off-diagonal entries” does not justify dropping $`\gamma^\nu`$, because this gradient changes precisely those entries. Using $`n^\nu\tau d_0`$ as the zeroth-gradient reference speed in the first-order clock–fall relation is nevertheless legitimate: its gradient correction would affect that relation only at second order.
- **Suggested fix:** Explicitly label $`n^\nu\tau d_0`$ as the homogeneous, zeroth-gradient reference speed. If an actual bound for the full sector contract is intended, give the hopping-row-sum bound including the position dependence and boundary treatment.

### I2. Narrow n alone does not justify the advertised leading moment expansion
- **Location:** Step 8, Eq. (9.21) and the paragraph describing its remainder
- **Severity:** minor
- **Problem:** The identity and displayed remainder bound are correct, but the remainder is third order only in a *joint* small spread of $`n`$ and $`\gamma`$. The stated narrowness assumption controls $`n`$ alone; under it, $`\langle(\gamma-\bar\gamma)u^2\rangle_w/\bar\gamma`$ can be of the same order as $`{\rm Var}_w(n)/\bar n^2`$. For example, take weights $`(1/4,1/2,1/4)`$, $`n=(1-\epsilon,1,1+\epsilon)`$, and $`\gamma=(2h,h,2h)`$, with $`h`$ small enough for admissibility. Then $`{\rm Cov}_w(n,\gamma)=0`$ and $`{\rm Var}_w(n)=\epsilon^2/2`$, but
  ```math
  \frac{\bar n\langle\gamma/n\rangle_w}{\bar\gamma}
  =1+\frac23\epsilon^2+O(\epsilon^4),
  ```
  rather than $`1+\epsilon^2/2+o(\epsilon^2)`$. Consequently, the leading deviation for narrow $`n`$ alone cannot generally be expressed using just the two moments requested in the question.
- **Suggested fix:** State an additional joint-narrowness assumption before treating the remainder as higher order. Without that assumption, retain the mixed moment $`\langle(\gamma-\bar\gamma)(n-\bar n)^2\rangle_w`$ at the relevant order and explain the limitation of the requested two-moment description.

### I3. Clock–displacement degeneracies are incompletely qualified
- **Location:** Step 5(c), paragraph after Eq. (9.14); Step 8, paragraph after Eq. (9.19)
- **Severity:** minor
- **Problem:** Under the sufficient affine relation in Step 5(c), the asserted correlation $`-{\rm sgn}(x_0)`$ requires $`x_0\ne0`$, $`\lambda>0`$, and $`{\rm Var}_w(g_\eta)>0`$. If the latter variance vanishes, both relevant sector variables are constant and the correlation coefficient is undefined. At $`x_0=0`$, vanishing covariance alone does not answer the requested mutual-function condition: for positive $`\lambda`$, the constant advance and leading displacement are functions of each other iff the leading displacement is also constant on $`S`$. Similarly, Step 8’s bound $`\lambda<\epsilon\lambda_0/\sigma_w(n)`$ needs a separate zero-variance case.
- **Suggested fix:** Add the nonzero-variance and positive-$`\lambda`$ qualifications to the correlation statement, state the mutual-function condition at $`x_0=0`$, and specify that the sector advance spread remains zero for all $`\lambda`$ when $`{\rm Var}_w(n)=0`$, within the stated clock approximation.

### I4. The summary table overstates the scope of the clock results
- **Location:** Result, summary table, clock-rate, rate-ratio, and relation rows
- **Severity:** minor
- **Problem:** The table gives formulas involving $`\eta^\nu_x`$, $`g^\nu_\eta`$, and $`g^\nu_m`$ under headings covering every sector and all of $`\mathcal S_{\rm grad}`$. These quantities and the quoted clock-rate result are not defined for a general member of $`\mathcal C_{\rm lev}`$. Arbitrary level data and gradients need not produce a uniformly advancing ring clock. Step 5 correctly restricts these results to $`\mathcal S^{\mathcal C}_{\rm grad}`$, but that restriction is lost in the table.
- **Suggested fix:** Explicitly restrict the relevant table cells to class-$`\mathcal C`$ sectors and $`\mathcal S^{\mathcal C}_{\rm grad}`$. For general $`\mathcal S_{\rm grad}`$, state only the exact sector mixture unless an additional clock structure is supplied.

### I5. The reverse-order remainder-bound claim misses zero-gradient levels
- **Location:** Step 3, paragraph after Eq. (9.8)
- **Severity:** minor
- **Problem:** The assertion that the bound on the remainder grows without limit along every specified sharp-label sequence is false when $`\langle\mathsf b_k^2\rangle_w=0`$. In that case every $`R^\nu`$ vanishes, so the remainder bound is identically zero regardless of the growth of $`X_g`$. This exception is admissible even for an unsharp field: sectors may agree with zero gradients at the selected level while differing at another level.
- **Suggested fix:** Qualify the divergence statement by $`\langle\mathsf b_k^2\rangle_w>0`$, at positive fixed $`\lambda`$, and identify the zero-gradient case as having a trivial displacement-spread limit in either order.

### I6. The zero mean gradient case is omitted from item 4(c)
- **Location:** Step 8, Eqs. (9.20), (9.21), and (9.24)
- **Severity:** minor
- **Problem:** These results explicitly assume $`\bar\gamma\ne0`$, whereas item 4(c) asks for every field state and requires vanishing-gradient exceptions to be stated. When $`\bar\gamma=0`$, $`\bar\varrho=0`$, so $`\bar a/\bar\varrho`$ is undefined—even if both numerator and denominator vanish. The mean acceleration can also remain nonzero because sector correlations need not vanish. This case cannot simply be covered by the ratio formulas.
- **Suggested fix:** State explicitly that no ratio is defined for $`\bar\gamma=0`$. Treat agreement with the sharp mean-profile relation through the undivided acceleration identity; the covariance conditions can then be stated without division by $`\bar\gamma`$.

## Focus points

None given.
