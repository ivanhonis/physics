# External verification: 08-two-types

- **Subproject:** 05-ilang-free-fall
- **Package:** 08-two-types
- **Verified version:** v2
- **External round:** 1 of 2
- **Date:** 2026-10-11T10:23:28+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The equal-fall conditions, clock-response conditions, and scaling rules are largely correct within the stated linear-profile contract family. However, the claimed M6 invariance of the field-coupling parameters fails for admissible degenerate fields, and the analysis of equivalent descriptions does not cover the full equivalence class required by item 6. There are also missing qualifications concerning zero denominators, discrete same-distance comparisons, and the asymptotic regimes of the quoted rates and accelerations.

## Issues

### I1. Coupling invariance fails for a degenerate field
- **Location:** Step 5(c), Eq. (8.13); Step 5(d), Eq. (8.14)
- **Severity:** major
- **Problem:** The scope allows every self-adjoint Φ, including Φ = 0. In that case the total contract is independent of both θ₁ and θ₂. For example, changing $`(\theta_1,\theta_2)=(1,1)`$ to $`(2,1)`$ leaves every contract operator and the total $`C`$ unchanged, but changes “θ₁ = θ₂,” the value of θ₁/θ₂, and, when $`d_{0,1}=d_{0,2}`$, “θ₁/d₀,₁ = θ₂/d₀,₂.” Thus these are not M6-invariant statements over the claimed class. Checking only the listed common shifts and rescalings misses replacements available when the interaction is degenerate; the common-coupling claims inherit this problem.
- **Suggested fix:** Treat zero/scalar field interactions separately. Establish the parameter invariance only where the nonzero interaction part of the total contract identifies the coupling ratios, and state that the listed numerical coupling conditions are not intrinsic in the degenerate cases.

### I2. The analysis excludes allowed equivalent descriptions
- **Location:** Step 7 opening and lemma; Step 8; Open issues, second item
- **Severity:** major
- **Problem:** The question defines an equivalence using any admissible pairwise $`C'`$ on the same objects; it does not require $`C'`$ to retain linear profiles and the single-operator record form. The lemma adds precisely that restriction, so it does not establish the requested conclusions for every equivalence. This exclusion is substantive: define
  ```math
  Q_1=\sum_x(-1)^xP_x^{(1)}\otimes\sigma_3\otimes\mathbb 1_{N_1}.
  ```
  This operator is diagonal in the places and commutes with $`C`$, since hopping changes both position parity and the branch sign. Consequently $`C'=C+\varepsilon Q_1`$ is an allowed equivalence with all factors equal to one, by the quoted (5.19), but it changes the rest profile to $`m_x+\varepsilon(-1)^x`$, outside the linear-profile family. The derivation explicitly leaves such equivalences open while presenting item 6 as settled.
- **Suggested fix:** Analyze the allowed equivalences outside the restricted family and establish whether the requested quantities and statements remain defined and invariant there. Where they do not, derive and state that limitation rather than using the restricted-family lemma as an all-equivalences result.

### I3. Ratios need nonzero-denominator qualifications
- **Location:** Step 1(b), table following Eq. (8.3); Step 5(c), Eq. (8.13); Step 8(d), Eq. (8.19)
- **Severity:** minor
- **Problem:** “All ratios are well defined” is asserted although the scope permits zero responses and accelerations. The value θ₁/θ₂ is likewise undefined when θ₂ = 0. Equation (8.19), which is presented for an arbitrary pair with unequal maximal speeds, can have either a zero acceleration denominator or a zero clock-response denominator. The later zero-gradient consistency check does not supply these missing domains.
- **Suggested fix:** Add nonzero-denominator conditions to every quotient statement. Use cross-multiplied equalities or the individual transformation rules where zero values must be included.

### I4. Exact same-distance comparisons are not always available
- **Location:** Step 3, Same distance bullet
- **Severity:** minor
- **Problem:** RD correctly compares normalized first-order responses, but its interpretation as comparing two actual lattice intervals of the same nonzero length needs qualification. Such intervals require integers $`n_1,n_2`$ satisfying $`n_1d_{0,1}=n_2d_{0,2}`$, within both chains. For example, if κ₁/κ₂ = √2, no such nonzero intervals exist. The unrestricted setting therefore does not always support the literal comparison described in this bullet.
- **Suggested fix:** Distinguish comparison of normalized response slopes from comparison of realizable equal-length intervals. Qualify the latter by the existence of appropriate intervals in both lattices.

### I5. The limiting observables need a compatible chain regime
- **Location:** Setup and assumptions, Regime and orders; Result, opening class statement
- **Severity:** minor
- **Problem:** The quoted rate uses a wide-start limit, and the quoted drift acceleration uses a long-window average followed by a sharp plane-wave-label limit. These are then assigned to all finite chains with L ≥ 1, without specifying a long-chain limit or a hierarchy keeping the packet and evolution away from boundaries. On a fixed finite chain, the wide-start limit cannot be taken as written. The shorthand $`|g|L\ll1`$ also does not specify the scale controlling the dimensionful scalar gradient ℱ.
- **Suggested fix:** State the compatible chain, packet-width, averaging-window, and gradient limits—and their order—or delimit the conclusions to the corresponding asymptotic family. Include the appropriate dimensionless smallness condition for ℱ and distinguish ideal wide-start responses from finite-width ones.

## Focus points

None given.
