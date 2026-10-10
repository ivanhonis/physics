# External verification: 08-maximal-speed

- **Subproject:** 04-ilang-time
- **Package:** 08-maximal-speed
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-10T13:54:42+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The rebooking transformations, velocity bound, chain spectra, and leading-order comparison of moving-clock ratios are largely correct. However, the derivation does not establish the required convention independence of its rest cost: the half-gap of the displayed body contract changes under allowed branch-dependent diagonal rebookings. Consequently, the claimed well-defined inertia–rest-cost relation is not established as written. There are also a parametrization error and a missing qualification concerning the infinite-chain weak-record limit.

## Issues

### I1. Rest-cost invariance is checked against too few rebookings
- **Location:** Step 7, final paragraph; Step 9, Eqs. (8.16)–(8.18)
- **Severity:** major
- **Problem:** Step 7 argues that $`M_k`$, interpreted as half the body-contract gap, is well defined because a *uniform* diagonal shift does not change that gap. But (8.1) permits arbitrary place-dependent diagonal shifts. For example, choose
  ```math
  \alpha^A_{(x,s,a)}=\delta(\sigma_3)_{ss},\qquad \alpha^B=0,\qquad Z=0.
  ```
  Then
  ```math
  C_A'=C_A+\delta\,\sigma_3\otimes\mathbb1_N,\qquad
  K'^A_{(x,s,a)}=\kappa_AxX_A-\delta(\sigma_3)_{ss}\mathbb1_c.
  ```
  The full $`C`$, all centered record vectors, all velocities, and the maximal-speed bound remain unchanged. Nevertheless, the half-gap of $`C_A'`$ at label zero is $`M_k+\delta`$, rather than $`M_k`$. Thus the stated definition of rest cost is not invariant under all the conventions already identified in Step 1. In this representative, the scalar part transferred into the record terms also survives at zeroth order in $`\kappa_A`$, so it cannot be discarded when identifying the effective body contract. Equation (8.16) is valid in the displayed Model D representative, but its promotion to an M6-compliant physical relation requires an additional argument.
- **Suggested fix:** Define the rest gap using a convention-independent effective contract extracted from the full contract family, retaining any zeroth-order scalar record terms. Alternatively, specify and justify an invariant reconstruction of the canonical Model D split. Then establish that this gap, rather than the gap of an arbitrary displayed $`C_T`$, is the rest cost entering the inertia relation.

### I2. Claimed redundancy does not give the same replacement
- **Location:** Step 1, paragraph immediately after Eq. (8.1)
- **Severity:** minor
- **Problem:** Replacing the parameter data by $`(\alpha^A+c,\alpha^B-c,Z+c\mathbb1_c)`$ leaves the new $`K`$'s unchanged, but changes the new body contracts by
  ```math
  C_A'\mapsto C_A'+c\mathbb1_a,\qquad
  C_B'\mapsto C_B'-c\mathbb1_b.
  ```
  Hence these data do not give the same replacement tuple. They give distinct replacements with the same total $`C`$.
- **Suggested fix:** Delete the claimed parametrization redundancy, or describe it explicitly as an additional redistribution of opposite constant body terms that leaves the total contract unchanged.

### I3. Weak-record estimate is not justified uniformly in chain length
- **Location:** Setup and assumptions; Step 7, Eq. (8.11)
- **Severity:** minor
- **Problem:** The Duhamel argument establishes (8.11) for each fixed finite chain. Its elementary operator-norm bound, however, grows with chain length because the record coupling contains the unbounded position label: $`\|C_{\rm rec}\|`$ scales as $`\kappa_T L_T`$. The derivation subsequently uses infinite-chain Model D formulas without specifying an order of limits or localization conditions sufficient to make the state-level estimate uniform. Concentration near a plane-wave label alone does not supply the needed position-moment bound.
- **Suggested fix:** State that the weak-record limit is taken first at fixed finite size, with the subsequent infinite-chain limit justified separately, or impose suitable localized starts and give a state-dependent Duhamel estimate uniform in chain length. Either would settle this applicability issue.

## Focus points

None given.
