# External verification: 03-gas-grip

- **Subproject:** 08-ilang-propagation
- **Package:** 03-gas-grip
- **Verified version:** v5
- **External round:** 3 of 3
- **Date:** 2026-10-24T20:22:13+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The affine-grip characterization and the principal cost and weighing formulas are consistent with the stated contracts and quoted inputs. The rank-one resolvent calculation also supports the revised uniform remainder estimates. Some subsequent “if and only if” conclusions, however, impose exact restrictions on the grip where the formulas establish only accuracy-dependent or asymptotic restrictions.

## Issues

### I1. Exact necessity is stronger than the weighing ratios establish
- **Location:** Step 4, Criterion after Eq. (3.8); Step 6, discussion after Eq. (3.11) and Mark and bond together; corresponding Result entries
- **Severity:** minor
- **Problem:** The exact identity $`\rho_i^F=\rho_i^{\rm fg}/\mu_i`$ implies that equality with the **full-grip ratio** requires $`\mu_i=1`$, provided that ratio is nonzero. It does not imply that weighing the bond like the first-order cost requires $`\mu_i=1`$ at a fixed finite geometry. From (3.10), the latter condition is instead
  ```math
  \mu_i=1+\kappa^{\rm mid}+O(\eta K).
  ```
  For example, choosing $`\mu_i=1+\kappa^{\rm mid}\neq1`$ gives $`\rho_i^{{\rm mid},F}=1+O(\eta K/|\mu_i|)`$, despite $`\alpha_i\neq0`$. Likewise, approximate agreement allows nonzero $`\alpha_i/(n\beta_i)`$ within the stated error tolerance. The inference after (3.8) that “where $`\zeta\to0`$, (i) is $`\mu=1`$” also needs qualification: its stated condition remains $`\mu=1+\zeta+O(\chi q)`$, unless an additional order of limits or fixed-parameter requirement is imposed.
- **Suggested fix:** Distinguish exact equality with the full-grip ratio, finite-geometry agreement to a specified accuracy, and universal agreement in a distant-source limit. Retain the accuracy-dependent conditions supplied by (3.8) and (3.10). State $`\alpha=0`$ as necessary only when the grip ratio is fixed independently of the vanishing geometric and perturbative errors and agreement is required in the limiting regime, or uniformly over the relevant configurations. Apply the same qualification to the combined mark-and-bond conclusion.

## Focus points

None given.
