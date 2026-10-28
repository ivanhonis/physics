# External verification: 06-mark-inertia

- **Subproject:** 08-ilang-propagation
- **Package:** 06-mark-inertia
- **Verified version:** v3
- **External round:** 2 of 3
- **Date:** 2026-10-25T09:57:22+01:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The second-order spectral formula and the expansion of the inverse curvature are consistent, and the supplied independent diagonalisation checks support those formulas at the tested parameters. However, the cubic-torus window classification uses interpolated crossings as if they were established boundaries, and some claimed windows contradict the refined numerical results supplied with the derivation. Several additional claims about finite-size control, finite-pinning level dependence, and numerical curvature accuracy require qualification or further checks.

## Issues

### I1. Claimed windows contradict the refined numerical results
- **Location:** Step 10, finding (c), Eq. (6.14), and crossings and grid_tests in torus_mark_inertia.py
- **Severity:** major
- **Problem:** The reported crossings are obtained by linear interpolation on the coarse ε grid, not by solving $`\rho_i(\varepsilon)=1`$. They are nevertheless used as window endpoints in the claimed classification. There is a direct contradiction at ℓ = 32 and r = 2: the text gives the window [1.453, 2.380), whereas Part D2 reports a refined, isolated point at ε = 1.434 with ξ* = 0.5056 > 0. That point admits a grip with ρ = 1 but lies outside the stated window. Consequently, the “iff” classification using these windows is not supported even on the refined grid.
- **Suggested fix:** Determine the crossings by root-finding using the lattice sums, with numerical error estimates, and update the classification. Alternatively, report only the individual sampled points satisfying the undivided condition in (6.13), and identify the coarse interpolations as estimates rather than window boundaries.

### I2. Finite-pinning level dependence does not follow from the displayed asymptotics
- **Location:** Step 7, Next order in 1/ℓ
- **Severity:** minor
- **Problem:** The assertion that two lower levels have different ρ at finite ℓ is inferred from the increasing term $`2\varepsilon_kR`$. But (6.9) retains an uncontrolled $`O(\delta_\ell)`$ remainder of comparable or larger order. Differences of that remainder between levels could cancel the displayed contribution, especially for arbitrarily close clock levels. The supplied checks establish differences for the tested levels, not the general finite-ℓ assertion.
- **Suggested fix:** Restrict this statement to the tested members and the controlled heavy regime, or derive a sufficiently precise subleading expansion or monotonicity argument. Preserve the distinction between the established leading limit $`2-r^2`$ and finite-ℓ conclusions.

### I3. Finite-size control omits the distance to the excitation threshold
- **Location:** Setup and assumptions, Limits; Step 3
- **Severity:** minor
- **Problem:** The claim that the dressed lattice sums have exponentially small finite-size errors controlled by L/ℓ, supplemented only by Lε/τ for light levels, is not uniform over the stated isolated-state class. Near an excitation threshold, a denominator can have the local form $`d(q)=\Delta+a(q-q_*)^2+\cdots`$, with isolation gap Δ > 0. Its complex zeros approach the real momentum axis on a scale proportional to $`\sqrt{\Delta/a}`$, independently of the field’s pinning singularities. Thus an arbitrarily small positive isolation gap introduces an additional finite-size scale not covered by the stated conditions.
- **Suggested fix:** State the finite-size estimates with explicit dependence on the isolation gap, or restrict them to a class bounded away from threshold. Distinguish the pinning-controlled errors of the held-field sums from those of the dressed resolvent sums.

### I4. Curvature accuracy is not checked in the most sensitive regimes
- **Location:** torus_mark_inertia.py, analyse and curv; Step 10, numerical findings and Part F
- **Severity:** minor
- **Problem:** The numerical curvatures use Richardson finite differences with $`h=\min(10^{-2},0.05\varepsilon/\tau)`$, but no h-refinement test is supplied. This controls the spinor variation scale, not the potentially much smaller variation scale associated with an excitation denominator near threshold. The brute-force checks of $`S_i(P)`$, and convergence with L, do not establish the accuracy of $`S_i''(0)`$. This is particularly relevant to the light upper branches near their isolation boundary and to the quoted crossing locations.
- **Suggested fix:** Check convergence under successive reductions of h at the light-level and smallest-gap points, and propagate the resulting uncertainty into ρ, ξ*, and the crossings. Analytic differentiation of the summands would also settle this issue.

## Focus points

None given.
