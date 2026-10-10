# External verification: 03-relational-time

- **Subproject:** 04-ilang-time
- **Package:** 03-relational-time
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-10T07:40:09+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The main spectral calculations, conditional-state construction, crossing-contract counterexample, and finite-difference error bound are correct. The derivation appropriately distinguishes stationary reading statistics from stationarity of the state, and exact clock-step relations from approximate derivative relations. Two statements need qualifications, and the bookkeeping independence of the generator split should be made explicit to establish compliance with M6.

## Issues

### I1. Minimal cost spread is asserted outside its stated range
- **Location:** Setup and assumptions, Clock bullet
- **Severity:** minor
- **Problem:** Input (2.12) minimizes $`\Delta C_K`$ for the localized start $`\lvert0\rangle`$, not for an arbitrary clock view. The global eigenstates considered here can give nonuniform weights in the clock’s Fourier basis, for which the chosen consecutive spectral branches need not minimize the spread. Thus “this clock has minimal spread $`\Delta C_K`$” needs a state qualification. This assertion is not used subsequently.
- **Suggested fix:** State that this generator attains the minimum in (2.12) for the localized clock start, rather than asserting an unqualified minimum for the clock views used in this package.

### I2. Nonproduct correlations need not affect a specified reading
- **Location:** Step 3, paragraph following Eq. (3.4)
- **Severity:** minor
- **Problem:** For a fixed partition reading on $`R`$, its statistics can remain independent of $`m`$ even when the full conditional place distribution depends on $`m`$. Coarse-graining can hide the correlations; the one-outcome reading is an immediate example. Nonproduct joint place statistics imply that **some** reading on $`R`$ has outcome-dependent statistics, not that every specified reading does.
- **Suggested fix:** Insert the existential quantifier. For a specified partition, use the narrower condition that at least one coarse-grained conditional probability in (3.4) depends on $`m`$.

### I3. Booking independence of the generator split is not established
- **Location:** Setup and assumptions, Contracts bullet; Step 9
- **Severity:** minor
- **Problem:** The rate comparison uses $`C_R`$, whereas $`C_\partial`$ is described as collecting contracts across the cut. It is not explained how this split remains unchanged when an $`R`$-only term is booked in a crossing pair rather than an internal pair, as A5 permits. Under a literal contract-list grouping, the same total $`C`$ could then acquire different $`C_R`$, changing the reference evolution and the applicability of Step 9. The issue disappears if the supplied split is fixed by operator support independently of pair booking, but that interpretation is not stated.
- **Suggested fix:** Explicitly specify that all $`R`$-only contributions enter $`C_R`$ regardless of the pair in which they are booked, or otherwise establish that the supplied decomposition is booking-independent. This would settle the M6 concern without changing the calculations.

## Focus points

None given.
