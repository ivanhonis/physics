# Review: 06-mark-inertia v4

- **Subproject:** 08-ilang-propagation
- **Package:** 06-mark-inertia
- **Reviewed version:** v4
- **Date:** 2026-10-25

---
VERDICT: minor issues

## Issues

### I1. The gap bound of the numerical findings is stated for all of Step 10
- **Location:** Setup and assumptions, Limits (dressed sums, last sub-bullet).
- **Severity:** minor
- **Problem:** The sentence says that the numerical findings of Step 10 are for $`\Delta_k>0.2\,m_h`$. Finding (f) and Part G also evaluate light levels whose upper-branch gaps are $`0.022`$–$`0.1\,m_h`$, and at the smallest of these gaps the torus values at $`L=128`$ and $`256`$ differ by $`0.067`$. The bound holds only for the lower-branch findings, as the Open issues state.
- **Fix:** State the gap range of each finding: the lower-branch findings for $`\Delta_k>0.2\,m_h`$, the light levels down to $`0.022\,m_h`$.

### I2. Two cited torus numbers do not match the v4 output
- **Location:** Step 10, findings (e) and (f).
- **Severity:** minor
- **Problem:**
  - In (f), the upper end of $`\rho_{i,-}`$ on the torus is given as $`0.148`$. The v4 output (Part F, range line) gives $`0.1473`$.
  - In (e), the range $`\rho_{1,-}/(2\varepsilon_kR_1)=1.025`$–$`1.030`$ is the range at $`\ell=8`$. At $`\ell=32`$ the output gives $`1.020`$–$`1.031`$, and the sentence states no bracketed value, so it reads as holding at both $`\ell`$.
- **Fix:** Cite the v4 values, at both $`\ell`$.
