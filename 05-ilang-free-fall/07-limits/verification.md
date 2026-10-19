# External verification: 07-limits

- **Subproject:** 05-ilang-free-fall
- **Package:** 07-limits
- **Verified version:** v2
- **External round:** 1 of 2
- **Date:** 2026-10-11T10:31:41+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The exact level-mixture result, the acceleration conditions at rest, and the algebra concerning the operator under the factor are sound. However, several conclusions are asserted for a broader class of starts than the arguments support: finite-width starts can have equal level velocities, and concentration in label does not by itself remove the label-cut term. The coherence calculation also contains an incorrect remainder claim and leaves part of its stated scope unanswered. Finally, the record-induced secular velocity coefficients are not sufficient to establish the claimed window-averaged accelerations and relative-accuracy conditions.

## Issues

### I1. Equal velocities are possible for finite-width starts
- **Location:** Step 3, after Eq. (7.5); Result, item 1(d)
- **Severity:** major
- **Problem:** The sharp-label velocities are strictly ordered in class $`\mathcal C`$ when $`\sin 2p_0\neq0`$, but this does not imply the stated claim that no finite-width start of the defined class can have equal component velocities. For example, take
  ```math
  |g(p)|^2=1+\epsilon\cos(p-p_0),\qquad 0<|\epsilon|<1.
  ```
  This is normalized and has mean $`p_0`$ on the specified arc. Since every $`\omega_k'(p)`$ is π-periodic with zero integral, its integral against both the constant and first harmonic vanishes. Thus $`v_k=0`$ for every level, including when $`\sin2p_0\neq0`$.
- **Suggested fix:** Restrict the strict-ordering conclusion to the sharp-label limit, or impose an appropriate support condition on the finite-width weight. Retain $`v_k=\sigma\langle\omega_k'\rangle_g`$ as the general finite-width result.

### I2. Concentration does not remove the label-cut contribution
- **Location:** Step 4, Eq. (7.7) and its order-of-limits statement
- **Severity:** major
- **Problem:** The exact continuity equation correctly retains the boundary term, but the claim that $`\delta p\to0`$ removes it does not follow from the definition of concentration. Variance convergence controls integrated weight, not the point value $`|g(\pi)|^2`$. A sequence can consist of a narrowing central packet plus a smooth periodic bump at the cut whose width tends to zero while $`|g(\pi)|^2`$ remains a fixed positive number $`c`$. Its variance still tends to zero, whereas the first-order rate tends to
  ```math
  (\mathcal F_k-\sigma G_k)(1-c),
  ```
  rather than $`\mathcal F_k-\sigma G_k`$. Consequently, the claimed universal sharp-label rate and its subsequent equivalences do not hold for every sequence allowed by the question.
- **Suggested fix:** Require the starts to vanish near the cut, or impose a condition ensuring $`|g(p_0+\pi)|^2\to0`$. Otherwise retain the cut contribution in the limiting rate and in the level-independence conditions.

### I3. The neglected inter-branch contribution is not bounded in λ
- **Location:** Step 5, condition (E2) preceding Eq. (7.10)
- **Severity:** minor
- **Problem:** Condition (E2) says that the neglected inter-branch contribution produces a second-order term bounded in λ. First-order perturbation theory generally contains an inter-branch amplitude proportional to
  ```math
  \omega_k'(p)\,
  \langle\beta_{k,-\sigma}|B_k(p)|\beta_{k,\sigma}\rangle
  \int_0^\lambda s\,e^{\pm2i\omega_k(p)s}\,ds.
  ```
  The integral has a boundary term proportional to λ. For example, a rest-term gradient with nonzero packet spread makes the prefactor nonzero away from $`p=0`$. The amplitude can therefore grow linearly, and its second-order contribution need not be bounded. Step 5, part 6 itself recognizes this linear growth.
- **Suggested fix:** Replace the boundedness assertion with an estimate that includes the growing term and its suppression by packet width. Establish when that estimate is smaller than the terms retained in (7.10); the stated lower bound on λ alone does not establish this.

### I4. The coherence result does not cover all starts in the stated scope
- **Location:** Step 5, parts 3–7; Result, item 1(f); Open issues
- **Severity:** major
- **Problem:** Item 1(f) is asked for every smooth $`g`$, but the second-order leading term is supplied only for real Gaussian starts satisfying (E1)–(E3), and the first-order leading estimate only for narrow starts satisfying (F1)–(F3). For other parity starts, broad starts at rest, and several non-parity cases, the derivation expressly leaves the relevant leading deviation undetermined. Moreover, (7.24) leaves the inter-branch part unspecified rather than providing a complete first-order functional. Reflection symmetry establishes the absence of a first-order term for parity starts, not that their first nonzero deviation necessarily occurs at second order.
- **Suggested fix:** Supply the missing perturbative contributions and leading-order statements for the remaining starts, or explicitly identify an unresolved part of item 1(f) rather than presenting the package as answering its full scope. Replace “is of second order” with “has no first-order term” where only symmetry has been established.

### I5. Secular velocity coefficients do not establish the claimed averaged acceleration
- **Location:** Step 7, after Eq. (7.14); Step 8, Eqs. (7.15)–(7.18)
- **Severity:** major
- **Problem:** The stated suppression of sharp-label oscillations by a window, with relative size $`O(1/(M_k\Lambda))`$, is not valid for the acceleration average used earlier. For a sharp generic label, (7.13) contains
  ```math
  v_2(\lambda)=\frac{\sigma\lambda^2}{2}
  \left[\omega'''-\theta'^2\omega'\cos(2\omega\lambda)\right]+O(\lambda).
  ```
  Therefore,
  ```math
  \frac1\Lambda\int_0^\Lambda \dot v_2(s)\,ds
  =\frac{\sigma\Lambda}{2}
  \left[\omega'''-\theta'^2\omega'\cos(2\omega\Lambda)\right]+O(1).
  ```
  The oscillatory boundary term is of the same λ order as the secular contribution, not relatively suppressed by $`1/(M_k\Lambda)`$. Dephasing at fixed smooth $`g`$ can change this conclusion, but the required scaled large-window limit and its nonuniformity in packet width are not established. Equations (7.15)–(7.16) are derivatives of selected secular velocity terms; (7.18) consequently does not control the full observed acceleration or its relative error.
- **Suggested fix:** Define precisely how the secular acceleration is extracted and justify the order of averaging, large-window scaling, and sharp-label limits. Include the remaining contributions in the accuracy estimate, or restrict (7.18) explicitly to the selected secular terms.

### I6. Normalized coherence formulas require a nonzero reference coherence
- **Location:** Step 5, Eq. (7.24) and its stated generality
- **Severity:** minor
- **Problem:** The formula
  ```math
  \left(\frac{|\Gamma|}{|\Gamma^{(0)}|}\right)_1
  =\mathrm{Re}\frac{\Gamma^{(1)}}{\Gamma^{(0)}}
  ```
  requires $`\Gamma^{(0)}\neq0`$, but (7.24) is stated for every smooth $`g`$ and every λ. Destructive phase averaging can make the zero-gradient coherence vanish. At such a point the normalized expression is undefined, and the leading modulus is generally $`|\Gamma^{(1)}|`$, with a nonanalytic dependence on a signed perturbation parameter.
- **Suggested fix:** State the nonzero-reference condition for normalized expansions and treat zeros using the unnormalized coherence and its modulus.

## Focus points

None given.
