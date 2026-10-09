# External verification: 22-large-scale-geometry

- **Subproject:** 03-ilang-space
- **Package:** 22-large-scale-geometry
- **Verified version:** v2
- **External round:** 2 of 2
- **Date:** 2026-10-09T09:01:41+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The calculations for the explicitly specified square, qubit-disc, window, and exponential-tail families are consistent, including the revised window-chain distance and diameter formulas. The periodic-graph results also support the conditional conclusion under (F1)–(F3). However, those additional assumptions substantially restrict item 3(b), leaving its stated class of families unresolved. A smaller issue concerns the distinction between sufficient small-$`\lambda`$ bounds and actual neighbour-graph stability thresholds.

## Issues

### I1. Item 3(b) is answered only for a narrower family
- **Location:** Step 10, assumptions (F1)–(F3), “Scope,” Eq. (22.29), and Result
- **Severity:** major
- **Problem:** The question assumes periodicity and finitely many edge orbits, but does not require one fixed pattern throughout the sequence, growing domains of the form $`nB`$, or the boundary compatibility asserted in (F3). Step 10 establishes a valid conditional result after adding all these requirements, then explicitly leaves the remaining families uncovered. In particular, finitely many edge orbits in each member does not imply a fixed polygonal stable norm throughout the family: polygonal unit balls can approach an ellipse. Thus the standard periodic-graph theorem does not settle whether the class stated in item 3(b) can have an isotropic limit.
- **Suggested fix:** Retain (22.29) as a conditional theorem, but complete the determination requested in item 3(b) under its stated assumptions. In particular, distinguish fixed-pattern families from $`n`$-dependent periodic patterns and address the effects of recomputing neighbours at the boundary. Any affirmative claim should be supported by a family of valid recording descriptions, not merely by convergence of abstract polygons.

### I2. Shrinking certified bounds are conflated with shrinking stability thresholds
- **Location:** Step 8, paragraph following Eq. (22.23); Open issues, second bullet
- **Severity:** minor
- **Problem:** The exponentially small $`d_0`$-margins, combined with the uniform $`O(\lambda^2)`$ estimate, yield a sufficient small-$`\lambda`$ bound that shrinks exponentially with $`n`$. They do not establish that the actual range over which the neighbour graph remains a path must shrink: pairwise higher-order corrections could cancel or preserve the relevant inequalities. The statement that certification works “only while” this error estimate is below the margin is too strong, and the later assertion that the thresholds themselves shrink obscures this distinction. The corresponding assertion for 3(a) is also not separately demonstrated.
- **Suggested fix:** Describe the shrinking quantities as sufficient bounds obtained from the uniform remainder estimate. State explicitly that the actual graph-stability thresholds, including whether they admit an $`n`$-independent lower bound, are not determined here.

## Focus points

None given.
