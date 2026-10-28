# Review: 07-bond-inertia v3

- **Subproject:** 08-ilang-propagation
- **Package:** 07-bond-inertia
- **Reviewed version:** v3
- **Date:** 2026-10-25

---
VERDICT: minor issues

## Issues

### I1. The speed statement for the isolated range fails at a member, and the parts of (N) are not all covered
- **Location:** Step 8 ("One speed", the bullet on (I)); Result (7.12); twin 7.12.
- **Severity:** minor
- **Problem:**
  - The bullet on (I) states "the speed depends on the binding" for every level of (I). For mixed branches the exact condition of (7.12) has solutions with $`\lambda_{C,1}\lambda_{C,2}=4/(1-r^2)`$ and $`r<1`$. In (I) $`\lambda_{C,i}`$ is not restricted, so such levels lie in (I). There the deep and the shallow speed coincide ($`\tau/\sqrt{2-r^2}`$), and one speed holds for every binding strength.
  - (7.12) gives the speed "in each part of (N)", but its three bullets do not cover (N$`_l`$) outside (I) with $`r\ell`$ not large. This part includes $`r<1/(2\ell)`$ with $`E_b(0)\ge A`$, where the lattice part need not be small.
- **Fix:** State the speed of (I) with its exception for mixed branches. Cover every part of (N), or say which general formula holds in the remaining part. Make the same changes in the twin.
