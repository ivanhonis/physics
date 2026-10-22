# External verification: 07-inertia-of-pair-full-grip

- **Subproject:** 07-ilang-weight
- **Package:** 07-inertia-of-pair-full-grip
- **Verified version:** v2
- **External round:** 2 of 3
- **Date:** 2026-10-21T20:23:52+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The leading mutual-mark calculation and the resulting double counting of the binding cost in the inertia are substantially supported by the band analysis. However, the numerical weight check uses a source that follows the pair’s midpoint, rather than the stipulated held source, and its operator is not an admissible pair contract. The neglect of the ring-flux contribution is also unjustified over the stated small-width regime, affecting the claimed accuracy of the fall factor.

## Issues

### I1. The numerical source is not a held source of the stated description
- **Location:** Step 5, Weight of the selected level; code midpoint_weights and the exact-eigenvalue source check
- **Severity:** major
- **Problem:** The source used in the code is located at a fixed distance from the instantaneous midpoint of the two bodies. In laboratory coordinates its operator has the form
  ```math
  g_s\sum_{j,l}|j,l\rangle\langle j,l|\otimes
  \Phi_{j+h(l-j)/2+s},
  ```
  with the stated interpolation for half-integer midpoints. This depends jointly on both bodies and the field and is generally a three-object contract, forbidden by A5. It is not the stipulated held-source term $`g_s\Phi_{x_s}`$, which breaks joint translation symmetry and cannot simply be added within a fixed-$`P`$ sector. Consequently, agreement between the density calculation and these eigenvalue derivatives verifies Hellmann–Feynman for the conditional probe, not the required exact-eigenvalue check with a held source. The derivation also does not establish that this conditional eigenvalue shift, including its kinetic contribution, equals the effective weight governing motion in the admissible fixed-source contract.
- **Suggested fix:** Perform the required check with the actual fixed-source operator in the laboratory-coordinate contract. Derive the relation between its effective potential for a localized pair and the midpoint-conditioned internal density, including the approximation and error bounds. If the conditional operator is retained as an auxiliary mathematical probe, label it accordingly rather than treating its eigenvalues as those of the stated held-source description.

### I2. The ring-flux remainder is not uniformly exponentially small in the stated regime
- **Location:** Setup S4; Step 2, Bound level; Step 5, Leading order
- **Severity:** major
- **Problem:** S4 assumes only $`w\ll L`$, but assigns the continuum-tail estimate $`\exp[-O((L/w)^{3/2})]`$ to the flux contribution. That estimate does not apply uniformly to the lattice problem, especially for $`w\ll1`$, which the package explicitly includes through its small-$`\beta_0`$ claims. For example, at $`L=6`$ the relative ring has three sites. In the tightly localized limit, a circuit around this ring contributes at order $`\kappa^3/F^2`$, whereas the local curvature is of order $`\kappa^2/F`$; the relative flux correction is therefore $`O(\kappa/F)=O(w^3)`$, not exponentially small in $`w^{-3/2}`$. This can exceed the retained relative mutual correction $`O(\eta)`$ while S1–S4 hold. Although (7.5) retains a flux remainder explicitly, Step 5 drops it when asserting the general leading fall factor with only $`O(\eta,\tau^2/d^2)`$ errors.
- **Suggested fix:** Retain and bound the actual discrete-ring flux contribution wherever small $`w`$ is allowed. Alternatively, state additional restrictions sufficient for the continuum tail estimate and require the flux correction to be small against the particular retained terms, not merely against the total curvature.

### I3. The source hierarchy does not control every displayed remainder
- **Location:** Setup S6; Step 5, Eq. (7.12)
- **Severity:** minor
- **Problem:** The statement that S6 makes every remainder in (7.12) small is not established. In particular, S6 explicitly controls $`\eta/\kappa_s`$ and $`w/(L\kappa_s)`$, but not
  ```math
  \frac{\delta_m\tau^2}{\kappa_s d^2}.
  ```
  For comparable fixed body parameters this may follow from sharper binding estimates, but the class also permits arbitrarily unequal couplings. The derivation supplies neither such a uniform estimate nor the additional inequality needed for the displayed error bound to be useful in that range.
- **Suggested fix:** Add $`\delta_m\tau^2/d^2\ll\kappa_s`$ to the hierarchy, or replace this bound by a sharper estimate and demonstrate explicitly that the existing assumptions control it for the allowed parameter ratios.

## Focus points

None given.
