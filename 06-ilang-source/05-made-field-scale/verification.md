# External verification: 05-made-field-scale

- **Subproject:** 06-ilang-source
- **Package:** 05-made-field-scale
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-19T11:37:26+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The partial-expectation contract, its level blocks, the response kernel, and the signs of the resulting graph-coordinate profiles are largely correct. However, the derivation does not establish the requested first-order reduced dynamics: its joint-state error is of the same order as the retained coupling correction. It also identifies field-graph separation with the spatial distance supplied by the recording medium without establishing that identification; the finite ring provides an explicit incompatibility. Additional issues concern the invariant extraction of on-site blocks and the stated approximation ranges.

## Issues

### I1. The error bound does not establish first-order effective dynamics
- **Location:** Step 1, Eqs. (5.1)–(5.2), and Result
- **Severity:** major
- **Problem:** Equation (5.2) gives a joint-state error of order $`|\gamma\lambda|`$. The retained correction to the body generator is itself first order in $`\gamma`$, so this bound alone does not establish that the body evolves by the stated effective contract through first order. For a non-sharp field, the omitted joint-state term is generically nonzero at that order. For product starts, tracing over the field does cancel the first-order fluctuation contribution, but that cancellation—and an appropriate reduced-view remainder—is not derived. Consequently, the central first-order evolution claim is stronger than the result proved.
- **Suggested fix:** Derive the reduced body–medium evolution in the interaction picture, explicitly showing that the first-order fluctuation term vanishes after the field trace. Give a second-order remainder for that reduced evolution, with its time range, and distinguish it from the first-order joint-state error in (5.2).

### I2. Field-graph distance is not established as the recorded spatial distance
- **Location:** S3, Steps 4 and 6, Eqs. (5.13)–(5.14), and the signs discussion
- **Severity:** major
- **Problem:** The formulas use ring distance and Euclidean nearest-image separation on the tori as physical distances, but the specified record contract establishes only the linear record geometry $`K_x=\kappa xX`$. On the finite ring, the closing bond has $`K_{L-1}-K_0=\kappa(L-1)X`$, not a one-step record increment. Thus the quoted uniform $`d_0`$, direction $`\hat e`$, and maximal-speed background do not apply globally to that ring. A shorter graph arc need not point toward the source in the recorded geometry. On the higher-dimensional tori, recording the test body's single line likewise does not establish the transverse distance to an arbitrary source. The profile formulas are valid as functions of graph coordinates, but the claimed physical distance dependence and “towards the source” interpretation do not follow.
- **Suggested fix:** Distinguish graph separation from the distance supplied by the recording medium. Delimit the local intervals where the quoted spatial background applies, and report the missing global identification rather than claiming physical ring/toroidal distance results throughout the stated setting.

### I3. Invariant extraction of the two-dimensional on-site blocks is unspecified
- **Location:** Step 2, Eq. (5.3), and the M6 discussion
- **Severity:** minor
- **Problem:** The invariant partial expectation $`\bar C_\varphi`$ acts on the body and medium together. Its on-site blocks therefore also contain the medium operator $`K_x`$. The derivation then extracts a two-dimensional block with $`V_{x,k}=E_\varphi`$, excluding the record background, without specifying an invariant extraction rule. For example, adding $`f_x\mathbb 1`$ to the listed body term and subtracting it from the body–medium pair term leaves $`C`$ unchanged, but changes the nominal body block if the newly listed record term is simply excluded. Invariance of $`\bar C_\varphi`$ alone does not settle this separation. Gap ratios are less vulnerable, but the scalar part of R3 requires clarification.
- **Suggested fix:** Specify how these blocks are extracted from the total contract and the stated start, and verify invariance under the place-dependent relisting above. If the quoted recording background already supplies such a prescription, state and cite it explicitly.

### I4. The source-response validity hierarchy is not stated
- **Location:** Steps 5–6, Eqs. (5.8) and (5.11)–(5.14)
- **Severity:** minor
- **Problem:** The response expansion is applied without stating a weak-source condition relative to the finite-size gap. A sufficient condition for the quoted perturbative estimate is $`|g_s|\ll t_f\omega_{\min}`$. This matters especially when combining the expansion with large-$`L`$ asymptotics, since $`\omega_{\min}\sim L^{-2}`$. Expanding the clock ratio also requires the source-induced lapse correction to be small compared with $`1+\gamma n`$; positivity alone does not supply that hierarchy. The displayed $`O(g_s^2)`$ notation hides constants that can grow with $`L`$ or become large near $`1+\gamma n=0`$.
- **Suggested fix:** State the weak-source and lapse-expansion conditions explicitly, including how $`g_s`$ is controlled when $`L`$ grows. State when the omitted errors are smaller than the clock and acceleration signals whose signs are asserted.

### I5. The nonstationary error bound has the wrong integration path for negative λ
- **Location:** Step 1, Eq. (5.2), and the first Result item
- **Severity:** minor
- **Problem:** For $`\lambda<0`$, Duhamel's estimate involves field fluctuations along the negative-$`\lambda`$ trajectory. Equation (5.2) instead integrates $`\sigma_\Phi(\mu)`$ over positive $`\mu`$. For a general nonstationary field state, $`\sigma_\Phi(-\mu)`$ need not equal $`\sigma_\Phi(\mu)`$. The claimed bound therefore does not follow for every real $`\lambda`$, although the stationary-state specialization is unaffected.
- **Suggested fix:** Integrate along the actual trajectory, using $`\sigma_\Phi(\mathrm{sgn}(\lambda)\mu)`$, or use a supremum over $`|\mu|\le|\lambda|`$.

### I6. Curvature errors are omitted from the ring accuracy claim
- **Location:** Steps 4 and 6, Eqs. (5.7) and (5.13), and Result
- **Severity:** minor
- **Problem:** The ring acceleration is described as “exact in $`L`$ at first order in $`g_s`$,” but the comparison with the clock ratio also makes a local-slope approximation. Away from the source,
  ```math
  \partial_\varrho\Lambda^+=-\tfrac12+\frac{\varrho}{L},
  \qquad
  \Lambda^+(\varrho+1)-\Lambda^+(\varrho)
  =-\tfrac12+\frac{\varrho+\tfrac12}{L}.
  ```
  Their difference produces a curvature correction of first order in $`g_s`$, not an $`O(g_s^2)`$ correction. The stated smooth curvature of $`\Lambda^+`$ also has the wrong sign: it is $`+1/L`$, not $`-1/L`$. On an off-source line through a torus, $`w\ll\varrho`$ alone is additionally insufficient near a point where the projected slope nearly vanishes.
- **Suggested fix:** Qualify the ring acceleration as a local-slope result, include its curvature/discrete-difference error separately from the source-coupling remainder, and correct the curvature sign. Retain the directional condition $`|\partial_\ell^2N|w\ll|\partial_\ell N|`$ for the torus results rather than replacing it solely by $`w\ll\varrho`$.

## Focus points

None given.
