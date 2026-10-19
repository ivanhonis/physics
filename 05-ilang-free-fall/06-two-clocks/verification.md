# External verification: 06-two-clocks

- **Subproject:** 05-ilang-free-fall
- **Package:** 06-two-clocks
- **Verified version:** v2
- **External round:** 1 of 2
- **Date:** 2026-10-11T10:27:17+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The response formulas, common-rescaling conditions, and rest-fall equivalences are algebraically correct, including the corrected distinction between equal level offsets and $`V_k=V_\circ`$. The main named-gap tables and response–fall identities follow from the quoted inputs. Two statements about reading statistics and moving-label gaps are too broad, and the treatment of zero level gaps does not cover the full stated scope of arbitrary level offsets.

## Issues

### I1. Finite-width level-gap statistics can be periodic
- **Location:** Step 3, paragraph following Eq. (6.7)
- **Severity:** minor
- **Problem:** The statement “At a finite spread neither is [periodic]” is false in the class [L]. For example, choose two levels with identical local masses and hopping parameters but distinct offsets:
  ```math
  M_{x_0,k+1}=M_{x_0,k},\qquad
  \tau_{k+1}\zeta^0_{k+1}(x_0)=\tau_k\zeta^0_k(x_0),\qquad
  V_{x_0,k+1}\ne V_{x_0,k}.
  ```
  Their branch eigenvectors coincide and their positive-branch energy difference is independent of $`p`$. The first reading in (6.7) is then exactly periodic for any normalized finite-width label packet, with frequency $`V_{x_0,k+1}-V_{x_0,k}`$.
- **Suggested fix:** Qualify the nonperiodicity statement as generic, and state the constant-gap exception. A continuous superposition of label contributions need not involve a continuous range of distinct frequencies.

### I2. Some moving-label gaps respond identically in variants (a) and (c)
- **Location:** Step 16, final paragraph after Eq. (6.28)
- **Severity:** minor
- **Problem:** “They differ in every gap with a moving label” is false for gaps between different levels. For a positive-branch gap between levels $`k\ne k'`$, the response difference between variants (c) and (a) is
  ```math
  \rho^{(c)}_\gamma-\rho^{(a)}_\gamma
  =\frac{g\tau^2}{\Omega^0_\gamma}
  \left[
  \frac{\sin^2p}{\omega_k(p)}
  -\frac{\sin^2p'}{\omega_{k'}(p')}
  \right].
  ```
  One can choose nonzero, sufficiently small $`p,p'`$ so that the bracket vanishes while $`\Omega^0_\gamma\ne0`$. Such moving-label gaps have response $`g`$ in both variants.
- **Suggested fix:** Restrict the statement to admissible moving-label gaps inside one level, for which it is correct, or say that the variants generally differ for moving-label gaps. The named band-gap comparison remains valid.

### I3. Zero level gaps are excluded despite the stated scope
- **Location:** Setup, notation following Eq. (6.1); Step 14, Eq. (6.24); Open issues
- **Severity:** minor
- **Problem:** The question includes all level offsets, but the derivation additionally assumes every adjacent level gap is nonzero at zero gradients. This is a genuine restriction: choosing $`V_{k+1}-V_k=-(M_{k+1}-M_k)`$ makes that level gap zero and its response undefined. Consequently, the level-gap equivalences in (6.24) are conditional results, not results for all offsets as the scope and result summary suggest. If only some adjacent gaps are admissible, equality of the relevant offset-gradient combination need only be imposed across those adjacent pairs; constancy across all levels does not follow from those comparisons.
- **Suggested fix:** Explicitly delimit the nondegenerate scope of the level-gap row and summary, and state what happens for excluded labels: their response is undefined. If comparisons involving only the remaining admissible level gaps are intended, give the corresponding conditions without assuming all adjacent pairs are connected.

## Focus points

None given.
