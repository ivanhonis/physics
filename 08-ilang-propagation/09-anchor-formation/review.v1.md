# Review: 09-anchor-formation v1

- **Subproject:** 08-ilang-propagation
- **Package:** 09-anchor-formation
- **Reviewed version:** v1
- **Date:** 2026-10-26

---
VERDICT: minor issues

## Issues

### I1. The code report puts a marginal member among the cases without formation
- **Location:** Code, `check_formation.py`, cubic torus, "Formation times" ("Where $`1/(b-1)\ge0.5`$ (near anchor at $`\rho\ge4`$; ...), there is no formation, as (9.11) predicts").
- **Severity:** minor
- **Problem:** For the near anchor at $`\rho=4`$, $`b=3`$ and $`1/(b-1)=0.5=\varepsilon`$, the marginal member, which (9.11) does not decide. `formation_check.txt` reports formation there at $`c_0\lambda/\rho=9.91`$ at both sizes: the finite-$`\rho`$ plateau is $`0.496`$, against the prediction $`0.487`$ at finite $`\rho`$. The sentence states the opposite. With strict inequality the near-anchor cases without formation start at $`\rho=6`$.
- **Fix:** Use the strict inequality, and report the $`\rho=4`$ case as the output gives it.

### I2. Two summary ranges of the uniform check leave out the stiffer anchor
- **Location:** Code, `check_uniform.py`.
- **Severity:** minor
- **Problem:** "$`\nu_0^{-1/2}/T_U=1.00006`$ to $`1.00001`$" and "to $`0.03/L^2`$ (relative)" omit the run with $`\kappa_a=4`$, which gives $`1.00017`$ and $`0.05/L^2`$ in `uniform_check.txt`.
- **Fix:** Give the ranges over all runs reported in the output, or name the runs they cover.
