# External verification: 08-typical-or-forced

- **Subproject:** 06-ilang-source
- **Package:** 08-typical-or-forced
- **Verified version:** v2
- **External round:** 2 of 3
- **Date:** 2026-10-19T13:39:17+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The first-order coupling classification, dimension counting, and finite-volume susceptibility formula are sound. The proof that long range holds on an open dense subset of class F is also convincing, and the supplied code supports the finite-volume formulas and the stated examples. Remaining issues concern the scope of the large-distance profile, the interpretation of the perturbative bound, an omitted trivial coupling, and one numerical normalization.

## Issues

### I1. The leading profile is established only along selected sizes
- **Location:** Step 10, Eq. (8.10), and Result
- **Severity:** minor
- **Problem:** The subsequential statement is justified, but it does not establish a leading profile for unrestricted $`L\to\infty`$ on the stated generic set. This distinction matters: take the admissible scalar band $`h(k)=2t[1-\cos(k-\theta)]`$, with $`\phi=1`$ and irrational $`\theta/(2\pi)`$. It belongs to $`U\cap\mathrm F`$, but when $`\eta_L=\mathrm{dist}(L\theta/(2\pi),\mathbb Z+\tfrac12)`$ is small, the two lowest grid states have a gap asymptotic to $`8\pi^2t\eta_L/L^2`$. Their contribution to a fixed-distance difference of $`\chi_0/(2n)`$ is of order $`1/(L\eta_L)`$. Allowed irrational choices can make this contribution survive or diverge along other sequences. Thus the safe subsequence cannot silently stand in for the unrestricted thermodynamic profile requested in item 2. The uniform-in-$`L`$ long-range classification itself is unaffected.
- **Suggested fix:** Explicitly state that the general full-sequence profile need not exist, explain the near-grid-degeneracy obstruction, and identify Eq. (8.10) solely as the leading profile in the specified subsequential limit.

### I2. A sufficient analyticity bound is called the convergence radius
- **Location:** Step 8 and Open issues, second bullet
- **Severity:** minor
- **Problem:** The quantity $`\Delta_L/(2N_f\|\phi\|)`$ supplies a sufficient disk of analyticity; it is not established as the actual convergence radius. Nor does the derivation establish that it “shrinks as $`L^{-2}`$.” Only $`\Delta_L\le C/L^2`$ is proved, and near grid ties it can be much smaller. Moreover, at the fixed density stipulated in F2, $`N_f\propto L^D`$, so the displayed sufficient disk has size at most $`O(L^{-D-2})`$, not $`O(L^{-2})`$.
- **Suggested fix:** Consistently call this a sufficient finite-volume perturbative bound. Remove the assertion about the actual convergence radius and its $`L^{-2}`$ scaling; retain the proved gap upper bound and the absence of a demonstrated uniform perturbative regime.

### I3. The zero coupling is unnecessarily excluded from the scaling subset
- **Location:** Step 5, Eq. (8.5), and Result
- **Severity:** minor
- **Problem:** The question does not require a nonzero coupling or nonzero fall. The coupling $`Q_x=0`$, corresponding to $`\alpha=0`$, satisfies R3, has equal zero fall on both branches and all levels, and leaves both on-site blocks and hopping multiplied by the same factor $`\nu=1`$. Consequently, the requested subset includes the origin, whereas $`\mathcal S_2`$ excludes it.
- **Suggested fix:** Include $`\alpha=0`$ in $`\mathcal S_2`$, or distinguish the full subset from its nontrivial part. The dimension and exceptional-set conclusions remain unchanged.

### I4. The reported oscillation values omit their normalization
- **Location:** Step 10, numerical-check paragraph
- **Severity:** minor
- **Problem:** The values $`1.5,3.0,6.0`$ are values of $`\Omega(L/4)/(2n)`$, not of $`\Omega(L/4)`$. The code uses $`N_f=1`$, hence $`2n=2/L`$; the corresponding unnormalized oscillations are approximately $`0.075`$ at all three sizes. The code and output headers use the normalization correctly, but the prose incorrectly claims that the unnormalized oscillation grows proportionally to $`L`$.
- **Suggested fix:** Restore “$`\Omega(L/4)/(2n)`$” in this paragraph and distinguish the one-object numerical normalization from the fixed-density limit. These data still support failure of a uniform exponential bound.

## Focus points

None given.
