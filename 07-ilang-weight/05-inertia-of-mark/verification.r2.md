# External verification: 05-inertia-of-mark

- **Subproject:** 07-ilang-weight
- **Package:** 05-inertia-of-mark
- **Verified version:** v2
- **External round:** 2 of 3
- **Date:** 2026-10-21T09:31:35+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The sector construction, the order-τ² resolvent formula, and the principal weak-mark expansions are substantially supported by the supplied numerical checks. However, the full-grip acceleration derivation incorrectly identifies an oriented-bond velocity with the commutator of a position operator on a finite ring, and the code checks the former rather than the latter. Item 2 also remains incomplete for the exceptional coupling-(a) descriptions that retain one speed through order γ². Some numerical classification claims and a large-ring limit additionally require qualification.

## Issues

### I1. The acceleration derivation uses an invalid position commutator on the ring
- **Location:** Step 7, “(7.7) for FG,” parts 3–4; equation (5.14); check_fall_full_grip.py
- **Severity:** major
- **Problem:** On a finite ring, the diagonal label operator $`\hat x=\mathrm{diag}(0,\ldots,L-1)`$ does not satisfy the chain commutator used here. A hop across the chosen cut changes that label by $`1-L`$, not by $`1`$. Consequently, the asserted cancellations in the transformed position operator and the acceleration calculation acquire boundary terms. In particular, translation invariance does not imply that the double commutator with this diagonal position operator vanishes. The code avoids these terms by using the oriented-bond observable
  ```math
  v=-\frac{\tau}{2}(T_++T_-)\otimes\sigma_1,
  ```
  but its comment identifying this with $`i[C,\hat x]`$ is false on the ring. Thus the numerical agreement does not verify the observable used in the written derivation, and no localization assumption suppressing the cut contributions is stated.
- **Suggested fix:** Define acceleration through the appropriate ring displacement or oriented-bond velocity observable and derive its effective-band image consistently. Alternatively, restrict the position-based argument to starts localized away from a cut and include a controlled boundary-error estimate. Make the code and derivation use the same observable.

### I2. The first failure order is not derived for the exceptional one-speed descriptions
- **Location:** Step 6, equation (5.12), coupling-(a) double points; Result; Open issues
- **Severity:** major
- **Problem:** The straight-line criterion establishes when one speed exists through order γ², but the derivation finds admissible two-level descriptions satisfying that criterion and then stops. For those descriptions, it has not supplied the requested first order at which inertia–cost proportionality changes, or established that it persists. The supplied L = 7 exact-data check already indicates a nonzero order-γ³ residual at one such double point, but this is not an analytic derivation and does not settle the other exceptional descriptions. This is a substantive gap in item 2 for the stated class, rather than merely a question about higher accuracy in an already excluded case.
- **Suggested fix:** Evaluate the next-order one-speed condition for the exceptional descriptions and determine their first failure order, with the required conditions and errors. Otherwise explicitly mark item 2 as unsettled for these admissible cases rather than presenting it as completed.

### I3. An incomplete root search is used for exclusion claims
- **Location:** Step 6, “One speed at order γ², whole non-resonant class”; check_inertia_ac.py; Result
- **Severity:** minor
- **Problem:** The exact criterion (5.12) is useful, but the stronger statement that only the listed isolated two-level ratios work is not established by the search. The algorithm detects sign changes along numerically tracked root branches over bounded grids; it does not exclude tangential intersections, missed branches, or roots outside the search range. The two grids actually return different counts at L = 15. Likewise, finding no shared ratio among the detected double points does not exclude three-level solutions. The qualifications in “Open issues” and parts of “Result” are appropriate, but conflict with categorical wording elsewhere, including the claimed exclusions in the large- and small-$`t_f`$ regions.
- **Suggested fix:** Retain (5.12) as the necessary-and-sufficient result and describe the root lists strictly as numerical findings. Remove exclusion claims based on search completeness unless completeness is established by an appropriate algebraic or certified numerical argument.

### I4. The large-ring branch-isolation claim is false for negative γ
- **Location:** Step 8, “Isolation, (a) and (c),” large-L bullet; final large-L discussion
- **Severity:** minor
- **Problem:** The statement that $`d_{k,+}\to0`$ at fixed density and fixed γ implicitly treats σ = + as the upper spectral branch even after taking a nonuniform large-L limit. For γ < 0, its field block is attractive. Writing $`g=|\gamma|M_k`$,
  ```math
  E^0_+-E^0_-=2M_k+N_f\bigl[\varepsilon_0(-g)-\varepsilon_0(+g)\bigr]\longrightarrow-\infty
  ```
  at fixed $`n`$. The σ = + level therefore becomes the global lowest level, and its isolation distance approaches the positive attractive binding gap
  ```math
  \sqrt{4t_f^2+g^2}-2t_f,
  ```
  rather than zero. The bare excitation-sum argument is also not uniform in this fixed-γ limit.
- **Suggested fix:** Distinguish the branch label σ from spectral ordering in this limit. State a controlled ordered weak-coupling limit if using bare excitation sums, or use the exact held-block spectra and track which branch is attractive for each sign of γ.

## Focus points

None given.
