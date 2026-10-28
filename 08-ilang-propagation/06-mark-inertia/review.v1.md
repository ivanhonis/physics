# Review: 06-mark-inertia v1

- **Subproject:** 08-ilang-propagation
- **Package:** 06-mark-inertia
- **Reviewed version:** v1
- **Date:** 2026-10-25

---
VERDICT: major errors

## Issues

### I1. Items 2 and 3 are not answered on the cubic torus
- **Location:** Step 8 ("Size of R", "D=3 otherwise"), Step 9(b), Result (6.9)–(6.12), first item of Open issues; twin.
- **Severity:** major
- **Problem:** The question asks items 2 and 3 on the ring and on the cubic torus (Scope, "Class"). On the cubic torus the derivation settles them only in the regime $`\varepsilon_k\gg c_0,\ \tau\sqrt{1+r^2}`$ of (6.10). Outside it, $`\rho_{k,\sigma}`$ and the bracket of (6.12) are left as unevaluated lattice sums, and whether one speed $`v`$ exists, and whether $`E''\Delta W`$ is the same for every level and both branches, is listed as open. An item answered on a subclass is not answered. It is also not shown whether the region of (6.10) covers the whole range in which the upper branch is isolated on the cubic torus: there (U) needs $`\varepsilon_k`$ of the order of $`\Omega_{\max}\approx2\sqrt3\,c_0`$, and $`R`$ has a finite limit of order $`1/c_0`$ (Step 8), so $`\varepsilon_kR`$ is of order one at the edge of (U).
- **Fix:** Evaluate $`\rho_{k,\sigma}`$ on the cubic torus from (6.3), numerically where no closed form is available, with $`L`$ and $`\ell`$ large enough that the sums have converged (state the check). Do this for the $`F_1^2`$ and $`F_2^2`$ parts, for each branch where it is isolated under (6.4), for several levels (values of $`\varepsilon_k/c_0`$) and for several $`r`$ including $`r=1`$. Answer item 2 there: one $`v`$ or not, as a function of $`r`$ and of $`\varepsilon_k/c_0`$. Answer item 3 there: for which grips, if any, the bracket of (6.12) is the same for every level and both branches. Say how large $`\varepsilon_kR`$ is where (U) holds. Add the computation to the code and cite its output.

### I2. The linear-grip reading of (6.11) needs its order
- **Location:** Step 9(a), Result (6.11); twin 6.11.
- **Severity:** minor
- **Problem:** (6.11) says that $`E''\Delta W`$ is the same for every level and both branches iff $`F_2=0`$, independently of $`r`$. This holds in the counting $`F_1\sim F_2`$, where the inertia of the mark enters only at the next order. For the linear grip, $`F_2=0`$ exactly, so that next-order term is the first level dependence: by (6.12) it vanishes on the ring at leading order in $`1/\ell`$ only at $`r=\sqrt2`$. As written, (6.11) can be read as universality of the linear grip at every $`r`$.
- **Fix:** State in Step 9(a), in the Result and in the twin that for $`F_2=0`$ the first dependence on the level comes from $`I^{\rm mark}`$ at the next order, as given by (6.12).
