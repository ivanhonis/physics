# External verification: 06-own-mark

- **Subproject:** 06-ilang-source
- **Package:** 06-own-mark
- **Verified version:** v2
- **External round:** 1 of 3
- **Date:** 2026-10-19T11:53:17+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The core second-order resolvent calculation is consistent, and the stated parameter regions establish the negative results for common clock rescaling and the inertia–cost relation. The supplied code implements the sector contract and supports the reported cubic scaling of the truncation errors. Some auxiliary validity statements are too broad, and the rest-only control does not explicitly provide the requested second-order curvature.

## Issues

### I1. The small-τ expansion needs an additional nonresonance condition
- **Location:** Step 6, Eq. (6.11), and the corresponding Result bullet
- **Severity:** minor
- **Problem:** Condition (6.4) at nonzero τ does not ensure that expansion around τ = 0 is regular. For example, take $`L=3`$, $`N_f=1`$, $`t_f=1`$, and $`M_k=3/2`$. Both nonzero field labels have $`\varepsilon_q=2M_k=3`$. The upper starting level satisfies (6.4) for every $`\tau>0`$, because recoil removes the coincidence, but (6.11) has a zero denominator. More generally, the expansion also involves the detuning $`2M_k-\varepsilon_q`$, which is absent from the stated error scales. This does not invalidate the later sign argument in its safer region $`2t_fN_f<M_k`$.
- **Suggested fix:** Restrict (6.11) to parameters nonresonant at τ = 0 and state the necessary smallness relative to the detuning, or simply restrict this auxiliary expansion to the sufficient region used in the inertia comparison. Qualify its error estimates accordingly.

### I2. The quoted perturbative isolation scale is not justified
- **Location:** Step 3, paragraph following Eq. (6.4)
- **Severity:** minor
- **Problem:** The quantity $`M_k\sqrt{n/L}`$ is an individual transition-amplitude scale, not the norm of the perturbation controlling isolation of the full sector eigenvalue. Multiple channels contribute, and coupling (c) also contains vertices proportional to τ. Thus the stated condition involving the spectral distance divided by this scale is not established as a sufficient perturbative range throughout the declared class. The existence of some sufficiently small neighborhood in γ remains correct.
- **Suggested fix:** Give a sufficient bound using the full sector perturbation norm, such as $`|\gamma|\|\partial_\gamma C_k(P)\|<\delta/2`$ for unperturbed spectral separation $`\delta`$, or justify a sharper bound specific to these contracts. Retain the individual vertex scale only as a heuristic estimate if intended.

### I3. Exact concavity does not imply monotonicity at every perturbative order
- **Location:** Step 7, control (i), and the corresponding Result bullet
- **Severity:** minor
- **Problem:** Strict concavity of $`\varepsilon_0(g)`$ establishes that the exact held-body spacings strictly decrease with k for fixed nonzero γ. It does not establish that their changes strictly decrease at every Taylor order. Indeed, the first-order spacing change is the same $`\gamma n\delta_c`$ for every k, as already derived. Higher Taylor coefficients need not individually have the concavity of the exact function.
- **Suggested fix:** Replace “at every order” with an exact statement for each fixed nonzero γ, and separately retain the demonstrated second-order statement.

### I4. The rest-only motion-coupled control lacks its second-order curvature
- **Location:** Step 7, control (ii), inertia discussion for coupling (c′)
- **Severity:** minor
- **Problem:** For (c′), the derivation gives the second-order energy shift at $`P=0`$, but gives the curvature and curvature inertia only through first order. This establishes the negative inertia–cost comparison, but does not fully answer item 4’s request for the item-3 curvature through second order. The $`P=0`$ vertex supplied there is insufficient by itself to differentiate twice in P.
- **Suggested fix:** State the general-P vertex for (c′) and its insertion into the existing resolvent formula, together with the second-order mean-field curvature. An unevaluated finite-sum derivative, analogous to (6.10), would suffice for this short-argument control.

## Focus points

None given.
