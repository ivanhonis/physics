# External verification: 13-pair-fall

- **Subproject:** 05-ilang-free-fall
- **Package:** 13-pair-fall
- **Verified version:** v4
- **External round:** 2 of 3
- **Date:** 2026-10-11T21:40:17+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The central first-order velocity and drift-acceleration formulas are consistent with the Duhamel calculation, the commutator identities, and the quoted bound-level results. The numerical implementation and supplied outputs support those formulas for the tested parameter sets. However, the requested determination of the reversed limit order remains incomplete for the full class of item 2, and some statements about approximation orders and operational clock rates need qualification.

## Issues

### I1. Reversed-order limit classification remains incomplete
- **Location:** Step 5.3, Members that stay open; Result, item 2(c)
- **Severity:** major
- **Problem:** The derivation establishes nonexistence when $`c_i\not\equiv0`$, and establishes commutation under the stronger condition $`Q_P\mathcal K\psi_P=0`$. It leaves unresolved the case $`c_i\equiv0`$ with $`Q_P\mathcal K\psi_P\neq0`$: neither its exclusion from the admissible class nor the subsequent large-window limit is established. Thus the sufficient commuting condition does not supply the determination requested for every member of item 2. The clarification permits an open member to be identified with its reason, but here only a possibly empty conditional subclass is identified; no admissible member of it is actually specified.
- **Suggested fix:** Complete the criterion for the remaining case, or prove that it cannot occur. If actual members remain open under the question’s allowance, identify their admissible contracts and bound levels explicitly and mark item 2(c) as only partially settled.

### I2. Absolute and relative orders of the fall difference are conflated
- **Location:** Step 6.4, Common gradient with equal τ; Step 7.4
- **Severity:** minor
- **Problem:** The statement that the difference is “of order ε⁰” is correct for the acceleration ratio, not for the acceleration difference. With $`\tau_i=\epsilon\hat\tau_i`$, both free and pair accelerations are $`O(\epsilon^2)`$, and at fixed $`u`$ their nonzero leading difference is also $`O(\epsilon^2)`$. Likewise, “neither … to any order in ε” is too broad: they agree trivially through orders ε⁰ and ε¹, but disagree at the leading nonzero order ε².
- **Suggested fix:** State that the relative discrepancy is $`O(1)`$, while the absolute discrepancy is $`O(\epsilon^2)`$ times the gradient. Replace “not to any order” by “not at the leading nonzero order ε² at fixed u.”

### I3. Spectral clock-rate identities are not exact operational clock-rate identities
- **Location:** Step 7.2, Eq. (13.21); Result, item 4
- **Severity:** minor
- **Problem:** The identification $`\Gamma_i=\partial_{M_i}E_b`$ is exact as a spectral identity, but its interpretation as the rate of a clock-label reading uses the approximate distribution (11.19), with level-spacing, packet-width, and record errors. Calling (13.21) “exact in the data” does not by itself make it an exact identity for a rate inferred from finite-clock readings. In particular, the $`O(\epsilon^2)`$ corrections subsequently used in (13.24)–(13.26) require an accuracy hierarchy if they are intended as operationally resolved clock effects; the supplied conditions only require the reading remainder to be small, not smaller than those corrections.
- **Suggested fix:** Explicitly distinguish the spectral rate parameter $`n_i\Gamma_i/\lambda_{0,i}`$ from the operational rate obtained within the accuracy of (11.19). Carry the clock-reading approximation orders alongside the ε expansion, or state the additional hierarchy needed to resolve the $`O(\epsilon^2)`$ corrections.

## Focus points

None given.
