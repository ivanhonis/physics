# External verification: 08-field-speed

- **Subproject:** 07-ilang-weight
- **Package:** 08-field-speed
- **Verified version:** v2
- **External round:** 2 of 3
- **Date:** 2026-10-21T18:11:07+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The one-object reduction, first-order response, propagation bound, axial front speed, and quadratic long-range formation scale are substantially supported by the derivation and code. However, the requested front-arrival result remains incomplete away from lattice axes, and the finite-coupling formation claims do not control the difference between the linearized static reference and the actual lowest-state mark. The harmonic control also overstates the uniform validity of its continuum approximation near the lattice front.

## Issues

### I1. Front arrival is not determined away from the axes
- **Location:** Step 3, Eq. (8.7); Result; Open issues
- **Severity:** major
- **Problem:** For D = 2,3, the derivation establishes an upper bound on arrival time only along lattice axes. Elsewhere it establishes only exclusion of sufficiently early arrival, which does not establish that the threshold is ever reached on a linear scale. This leaves item 1 incomplete for the stated field class. Moreover, the value $`2t_f`$ is an axial speed; it is not yet a derived speed in the question’s graph distance for general directions.
- **Suggested fix:** Establish a sufficiently large front response for non-axial separation sequences under the stated threshold criterion, and determine the corresponding directional arrival times and their expression in graph distance. Keep the axial result distinguished from the general result.

### I2. Finite-coupling formation is compared with an uncontrolled static reference
- **Location:** Step 8, Formation and Negative bullets; Result, finite-coupling conditions
- **Severity:** major
- **Problem:** Equation (8.18) controls the exact evolving density relative to its first-order response. It does not control the actual static mark relative to Eq. (8.2). Consequently, the L-independent conditions given for formation and failure of formation establish comparisons with a linearized reference, not necessarily with the lowest-state mark of the fixed contract. This distinction is essential in D = 1,2: the stated conditions allow $`|g_s|\Lambda^+(0)/t_f`$ to be large by increasing L. For example, an attractive point source in D = 1 then has a localized lowest state, despite satisfying the proposed finite-window dynamical condition at a fixed distance.
- **Suggested fix:** Restrict these extensions explicitly to comparison with the first-order static reference, or bound the relevant static-value or static-gradient remainder and impose the additional L-dependent smallness conditions needed for the claimed accuracy. Do not advertise the present dynamical remainder conditions alone as sufficient for formation relative to the actual static mark.

### I3. Continuum control is not uniform through the lattice front
- **Location:** Step 6, Eq. (8.15), Formation paragraph and subsequent lattice-correction paragraph
- **Severity:** minor
- **Problem:** The sharp step and the bound for every $`\sqrt{\kappa_h}\lambda>|r|`$ are derived for the continuum dispersion, then transferred too strongly to the admissible lattice control. The acknowledged $`O(|r|^{1/3})`$ front smoothing entails a nonuniform transition region in which the lattice response need not be close to its static value immediately after $`|r|/\sqrt{\kappa_h}`$. Also, relative $`O(|r|^{-2})`$ errors do not generally describe the dynamical correction behind the front: nonzero-wavevector stationary points can produce larger algebraically decaying transients. The qualitative linear formation scale can survive, but the every-time bound stated for the lattice is not justified.
- **Suggested fix:** Separate the continuum identity from the lattice conclusion. Exclude the front transition window, or work at a fixed ratio $`\sqrt{\kappa_h}\lambda/|r|>1`$, and give the short asymptotic estimate needed to show that lattice transients are below the stated accuracy there.

### I4. The running-average numerical comparison tests a different quantity
- **Location:** Step 5, numerical check following Eq. (8.11); code function small_checks
- **Severity:** minor
- **Problem:** Equation (8.11) bounds the first-order running average minus the first-order static mark. The quoted numerical comparison instead uses the exact running average minus its exact infinite-time average. These are different quantities at nonzero coupling. Indeed, for the ring at $`\Lambda=L^2/t_f`$, the output gives deviation from the first-order static reference $`1.43171`$, exceeding the first-order bound $`1.42224`$, whereas the text quotes $`1.33710`$, the deviation from the exact infinite-time average. This does not contradict the first-order theorem, but it is not a direct verification of that theorem.
- **Suggested fix:** Check Eq. (8.11) using the first-order running average, available directly from the Fourier formula. For an exact-evolution comparison, include the appropriate finite-coupling correction and clearly identify the static reference being used.

## Focus points

None given.
