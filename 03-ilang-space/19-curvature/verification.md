# External verification: 19-curvature

- **Subproject:** 03-ilang-space
- **Package:** 19-curvature
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-08T23:10:16+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The exact metric formula, its small-$`\lambda`$ expansion, the leading curvature formula, and the first-order body-induced curvature variation are correctly derived on patches where $`\hat g^{(0)}`$ is non-degenerate. The three examples give the correct metric and curvature results for positive $`\lambda`$. Two subsidiary statements need correction: one-dimensional flatness does not imply a vanishing second fundamental form, and the commuting example incorrectly includes $`\lambda=0`$ in its non-degeneracy and curvature claims.

## Issues

### I1. One-dimensional flatness is incorrectly attributed to $`\mathrm{II}=0`$
- **Location:** Step 7, case (iii), following Eq. (19.11); Result, Item 2.
- **Severity:** minor
- **Problem:** The text says that the sufficient condition $`\mathrm{II}\equiv0`$ holds when $`k=1`$. This is false: an immersed curve can have a nonzero second fundamental form while its intrinsic Riemann curvature vanishes. For example, with $`\chi=\lvert0\rangle`$ and $`K(t)=\cos t\,\sigma_x+\sin t\,\sigma_y`$, the record map is $`u(t)=e^{it}\lvert1\rangle`$. Its induced metric is non-degenerate, but $`u''=-u`$ is normal to the curve, so $`\mathrm{II}_{11}\ne0`$. The claimed intrinsic flatness is nevertheless correct, as the consistency checks establish by antisymmetry.
- **Suggested fix:** Remove $`k=1`$ from the cases asserted to satisfy Eq. (19.11). State separately that every non-degenerate one-dimensional metric has zero intrinsic curvature, directly from Eq. (19.9).

### I2. The commuting example includes the degenerate point $`\lambda=0`$
- **Location:** Step 12, Eq. (19.18) and the following non-degeneracy statement; Result, Item 4(b).
- **Severity:** minor
- **Problem:** Although $`g=\lambda^2(\mathrm dx^2+\mathrm dy^2)`$ is valid at every $`\lambda\ge0`$, $`g`$ is identically zero at $`\lambda=0`$. Thus it is not non-degenerate there, and its Gaussian curvature $`\kappa_g`$ is undefined. Equation (19.18) incorrectly states $`\kappa_g=0`$ “for every $`\lambda`$,” followed by an unrestricted claim of non-degeneracy. The smoothly extended rescaled metric $`\hat g`$, by contrast, remains Euclidean at $`\lambda=0`$.
- **Suggested fix:** Restrict the non-degeneracy of $`g`$ and the assertion $`\kappa_g=0`$ to $`\lambda>0`$. State separately that $`g(x;0)=0`$, while the smooth extension of $`\hat g`$ has zero curvature also at $`\lambda=0`$.

## Focus points

None given.
