# External verification: 10-field-own-contract

- **Subproject:** 05-ilang-free-fall
- **Package:** 10-field-own-contract
- **Verified version:** v4
- **External round:** 3 of 3
- **Date:** 2026-10-11T16:51:11+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The compression, leakage estimates, Schrieffer–Wolff expansion, and cell calculation are substantially correct under the additional separation conditions stated in the derivation. The leading fast-field results for fall, level spacings, and the clock–fall relation are also consistent with the quoted inputs. Some requested correction-level conclusions remain incomplete, and two statements about clock behaviour need narrower qualifications.

## Issues

### I1. First fast-field correction to the relation is left unevaluated
- **Location:** Step 3(d), Eqs. (10.34)–(10.36), and Step 5, relation row
- **Severity:** minor
- **Problem:** The relation is evaluated explicitly only at leading order in ε₂ and ε₃. Its first corrections are described merely as a “further defect from β and γ³”, although the package computes the corresponding corrections to both acceleration and mean spacing. This omission matters for admissible exceptional members where the leading defect vanishes. For example, take an interior field eigenvalue with symmetric excited eigenvalues ±Δ, equal real transition amplitudes, no excited-block fluctuation, and $`Y=g\mathbb 1`$. Then $`\gamma_0=\gamma_1=\gamma^{(3)}_x=0`$, but $`\rho_0>0`$: the leading defect vanishes while
  ```math
  a_{k,+}(0)=-\tau^2g\bigl(1-4\rho_0M_k^2\bigr)
  ```
  is level-dependent at the retained correction order. Furthermore, once the hopping is corrected, the maximal-speed bound is no longer automatically the bare $`\tau d_0`$.
- **Suggested fix:** Complete the short argument at the retained correction order using the corrected acceleration, mean spacing, and hopping-based maximal-speed bound. State separately the result when the leading defect vanishes, rather than leaving that case as an unspecified further correction.

### I2. Zero mean spacing does not imply a stopped clock
- **Location:** Step 3(d), paragraph following Eq. (10.36)
- **Severity:** minor
- **Problem:** The statement that $`D_0=0`$ and $`g=\gamma_1\Sigma`$ imply “no clock of the chain advances” confuses zero mean rate with stationary clock statistics. For $`N\ge3`$, the retained quadratic term can give unequal, nonzero neighbouring spacings even though the endpoint spacing—and hence $`\bar r`$—vanishes. For example, $`M_k=(1,2,3)`$, $`N(x)=1`$, and $`\gamma_x=1/4`$ give upper energies $`(3/4,1,3/4)`$, up to a common offset: the mean rate is zero, but the clock state evolves. Equation (10.30) itself correctly detects this non-affine evolution.
- **Suggested fix:** Replace the stopped-clock claim by “the mean rate vanishes at every position”. State that stationary clock statistics additionally require all relevant level energies to coincide; otherwise the zero-rate ring clock is only the finite-range approximation quantified earlier.

### I3. The orders table omits essential clock-start limits
- **Location:** Step 5, clock row and introductory regime statement
- **Severity:** minor
- **Problem:** The table states that the clock is a ring clock with one rate at first order in ε₁ without explicitly imposing the wide-start limit and zeroth order in the spatial gradients. At finite width, the quoted Eq. (3.36) gives a mixture of advances, not a single-rate ring clock, even for a sharp field. These qualifications appear in Step 3(c), but the table’s general regime statement does not carry them over.
- **Suggested fix:** Add the wide-start, fixed-λ, zeroth-gradient qualifications directly to the clock row, and distinguish the finite-width mixture from the single-rate limit.

## Focus points

None given.
