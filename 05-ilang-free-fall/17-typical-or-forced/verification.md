# External verification: 17-typical-or-forced

- **Subproject:** 05-ilang-free-fall
- **Package:** 17-typical-or-forced
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-18T15:14:28+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The algebraic classifications of fall from rest, motion through order $`v^2`$, and the upper-branch stability defect are largely correct. However, the derivation strengthens R2 by imposing a level-independent multiplier that the stated requirement does not specify; its conclusions about R2 therefore do not answer that requirement as written. There are also narrower gaps concerning relisting invariance, the physical interpretation of the clock–fall relation, and the limiting procedure used for the local clock rate.

## Issues

### I1. R2 is replaced by a stronger requirement
- **Location:** Step 6.3; Eq. (17.10); Result entry (17.10)
- **Severity:** major
- **Problem:** Step 6.3 imposes a multiplier $`\alpha`$ that is independent of the clock level. R2, as stated in the question, only requires proportionality on every level; it does not specify that the proportionality factors coincide. Without this additional condition, every branch-traceless coupling in this class satisfies the levelwise proportionality, since
  ```math
  (\alpha_0+\alpha_1d_k)\sigma_3
  =\frac{\alpha_0+\alpha_1d_k}{M_k}(M_k\sigma_3).
  ```
  For example, choose $`n_1=1`$, $`\mathcal F_{\rm rec}=0`$, $`G=\epsilon\,\sigma_3\otimes D`$, and no motion gradient. This satisfies the stated levelwise R2, but
  ```math
  a_{k,\sigma}(0)=-\tau^2\epsilon\,\frac{d_k}{m+d_k}
  ```
  is not level-independent. Consequently, the claimed equivalence of R1 and R2, the R2 controls, and the M2 argument for R2 depend on an extra universality assumption.
- **Suggested fix:** Analyze R2 allowing level-dependent proportionality factors. Distinguish that requirement from the stronger common-multiplier condition used in the derivation, and revise its necessity, sufficiency, controls, and relisting analysis accordingly.

### I2. Identity-branch relistings need not preserve R2
- **Location:** Step 6.3, item 1
- **Severity:** minor
- **Problem:** The assertion that R2 is invariant under every relisting with $`Q=\mathbb 1_2\otimes Q'`$ checks only the traceless part of the own block. If such a $`Q`$ is added to the field pair term, it introduces a branch-identity contribution into the listed coupling, changing R2’s separate requirement that no such contribution be present. The total contract remains unchanged. This does not overturn the eventual non-invariance conclusion, but the claimed subclass of harmless relistings is too broad.
- **Suggested fix:** Restrict this invariance statement to relistings that leave the coupling unchanged, or explicitly check both the own-block traceless part and the coupling’s branch-identity part.

### I3. The spatial conversion in the clock–fall relation is assumed
- **Location:** Setup, “Use of (4.24) in C+”; Steps 4–5; Open issues
- **Severity:** minor
- **Problem:** The derivation establishes the label identity
  ```math
  a_{k,+}(0)=-\tau^2\,\frac{r(x+1)-r(x)}{r(x)}
  ```
  on the stated hyperplane, but explicitly assumes the conversion from label acceleration to spatial drift for $`\mathcal C^+`$. The quoted physical equality (4.24) applies only to $`\mathcal C`$. Thus the requested physical relation is left conditional on an additional assumption, although the conversion plausibly follows directly from the unchanged linear record embedding.
- **Suggested fix:** Supply the short kinematic argument that the same record embedding gives spatial drift acceleration $`d_0a_{k,+}(0)\hat e`$ for these level blocks, stating its weak-record accuracy and distinguishing drift acceleration from other contributions to the mean motion.

### I4. The wide-start limit needs an explicit local-limit convention
- **Location:** Regime and orders; Step 3; Eq. (17.6)
- **Severity:** minor
- **Problem:** The commuting-factor argument is exact for the frozen homogeneous contract, not for the full position-dependent contract: the actual added term $`-\mathcal F_1xD`$ does not commute with hopping. Moreover, taking $`W\to\infty`$ at fixed nonzero gradients conflicts with the stated small-profile-variation condition across the start. The derivation needs to distinguish the frozen-coefficient definition of a local rate from a limit of actual inhomogeneous evolutions before using its spatial difference at first gradient order.
- **Suggested fix:** State explicitly that the rate is defined by freezing coefficients before taking the wide-start limit, if that is the intended convention. If it is meant as an approximation to actual readings, specify the width/profile-length and observation-interval hierarchy controlling the neglected inhomogeneous terms.

## Focus points

None given.
