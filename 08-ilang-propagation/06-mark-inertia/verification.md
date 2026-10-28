# External verification: 06-mark-inertia

- **Subproject:** 08-ilang-propagation
- **Package:** 06-mark-inertia
- **Verified version:** v2
- **External round:** 1 of 3
- **Date:** 2026-10-25T08:42:28+01:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The second-order spectral sums and the supplied finite-Fock-space checks are largely consistent. However, condition (U) does not establish the isolated positive-branch eigenstate required by the question, and several conclusions incorrectly classify such states as isolated. The cubic-torus classification also relies on sampled monotonicity and convexity rather than establishing the continuous claims needed for its “if and only if” results; substantial parts of the requested scope remain unresolved.

## Issues

### I1. Positive-branch isolation is not established by condition U
- **Location:** Step 3, Eq. (6.4); Step 10, Isolated states; Eqs. (6.14)–(6.15)
- **Severity:** major
- **Problem:** Condition (U) excludes resonances only with one- and two-quantum states. Isolation of an eigenvalue of the full contract requires separation from *all* field-excitation sectors, regardless of the perturbative order at which they couple.

  For example, take $`c_0=\tau=1`$, $`m_h=1/8`$, and $`\varepsilon_k=4`$. On both graphs, $`\Omega_{\max}<\varepsilon_k`$, so the stated sufficient condition for (U) holds even when $`F_2\ne0`$. In infinite volume, choose $`q`$ along the body axis with $`\Omega_q=2`$. A four-quantum state containing two quanta at $`q`$ and two at $`-q`$ has total momentum zero and excitation cost $`8`$. Together with the negative-branch body at momentum zero, its cost is
  ```math
  E_f-4+8=E_f+4,
  ```
  exactly the positive-branch vacuum level. Varying the momenta supplies arbitrarily nearby spectral values, so that level is not isolated.

  The observation that higher-quantum channels first contribute to a generic self-energy at higher perturbative order does not restore spectral isolation or justify isolated-eigenvalue analyticity. The truncated diagonalizations validate the formal second-order coefficients, not isolation in the full system. The acknowledged open issue about higher quanta therefore affects the assumed state and the interpretation of the reported results, not merely a higher-order refinement.
- **Suggested fix:** State a full-spectrum gap condition, including every excitation sector, wherever an actual isolated analytic eigenvalue is claimed. Restrict positive-branch eigenvalue conclusions to cases satisfying that condition; where the gap closes, distinguish formal second-order coefficients from the eigenvalue and inertia specified in the question. Do not include states satisfying only (U) in a set described as isolated states.

### I2. Sampled lattice sums do not establish the cubic-torus classification
- **Location:** Step 10, Findings and Items 2–3; Eqs. (6.14)–(6.15); Open issues; torus_mark_inertia.py, parts D and D2
- **Severity:** major
- **Problem:** The decisive arguments use strict monotonicity of $`\xi^*_{k,-}`$ and $`\psi`$, and strict convexity of $`\varphi`$, to exclude common grips for different levels. The code checks differences and secant slopes at finitely many sampled values. These checks do not establish those properties between samples, nor do they exclude an intervening turning point or an equality at unsampled levels.

  Likewise, the finite comparisons in $`L`$ and $`\ell`$ do not establish persistence of the classification in the stated order of limits. In particular, the two-quantum part is not checked at the largest pinning lengths used for the one-quantum part. The reported calculations omit $`r>3`$, other intervals between the nine sampled ratios, and part of the isolated lower-branch region near its threshold.

  Restricting parts of the Result section to the computed grid appropriately limits the evidence, but then items 2 and 3 have not been settled for the class requested in the question. The unrestricted “iff” presentation in Step 10 and the claim that the cubic-torus items are now settled are unsupported.
- **Suggested fix:** Separate exact consequences of the spectral sums from numerical observations. Supply justified continuous bounds for any monotonicity, convexity, or exclusion property used in a classification, including its limiting regime; otherwise retain those classifications only as sampled numerical findings and explicitly leave the unestablished portions of the requested scope unresolved.

### I3. Singular tuning cases are omitted from the grip criterion
- **Location:** Step 10, Eq. (6.13), Findings (b), and Eq. (6.14)
- **Severity:** minor
- **Problem:** The equivalence
  ```math
  \rho=1\iff
  \xi=\frac{S_1(1-\rho_1)}{c_0S_2(\rho_2-1)}\ge0
  ```
  divides by $`\rho_2-1`$ without handling its zero. If $`\rho_2=1`$ but $`\rho_1\ne1`$, no finite $`\xi`$ works: the one-quantum contribution has strictly positive weight because $`F_1\ne0`$. Thus “1 lies between $`\rho_1`$ and $`\rho_2`$” is not sufficient when 1 is attained only at the second endpoint. If both ratios equal 1, every finite $`\xi`$ works, rather than one distinguished $`\xi^*`$.

  This matters at the window boundary identified by $`\rho_2=1`$; it cannot be included as an attainable finite-grip endpoint without qualification.
- **Suggested fix:** Use the undivided condition
  ```math
  S_1(\rho_1-1)+\xi c_0S_2(\rho_2-1)=0
  ```
  and list its singular cases explicitly. Distinguish attained endpoints from limits requiring $`\xi\to\infty`$, and adjust the window and uniqueness statements accordingly.

## Focus points

None given.
