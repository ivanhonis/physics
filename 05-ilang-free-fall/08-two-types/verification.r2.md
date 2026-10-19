# External verification: 08-two-types

- **Subproject:** 05-ilang-free-fall
- **Package:** 08-two-types
- **Verified version:** v4
- **External round:** 2 of 2
- **Date:** 2026-10-11T11:22:24+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The main conditions for level-independent fall, equal fall, and equal clock response follow correctly from the quoted inputs. The classification of equivalences is substantially justified, and v4 appropriately distinguishes transported statements from quantities not defined outside the relevant subclasses. The remaining problems concern exceptional cases in the invariance claims, an omitted scalar compensation, and the accuracy stated for the finite-width clock response.

## Issues

### I1. The equivalence table needs qualifications for invariant exceptional cases
- **Location:** Step 8(c), Eq. (8.18), and the paragraph defining “same” and “not the same”
- **Severity:** minor
- **Problem:** The table correctly identifies which statements are invariant throughout the whole class, but its stated interpretation is stronger: “not the same” means that some equivalent description changes the truth value for the given contract. That is false for some admissible contracts. For example, when both effective gradient sets vanish, FA remains false because the accelerations remain zero, while RD remains true because both responses remain zero. More generally, Eq. (8.20) already shows that FA cannot change from false to true if either level-independence condition fails or the two nonzero falls have opposite signs.
- **Suggested fix:** Label the affected entries “not invariant in general,” or give the contract-dependent exceptions. With independent re-timings, FA can change truth value precisely when both level-independence conditions hold and $`g_{\eta,1}g_{\eta,2}>0`$. RD can change truth value precisely when its two slopes are nonzero and have the same sign; otherwise its truth value is fixed.

### I2. The finite-width bound omits the clock-level expansion accuracy
- **Location:** Setup, Regime and orders, “Ideal and finite-width response”; Result, item 3
- **Severity:** minor
- **Problem:** The finite-width argument uses Eq. (3.36), which is explicitly quoted as a result to first order in the clock-level spacing. The derivation nevertheless presents the resulting response bound without that qualification and allows arbitrary clock parameters. Consequently, the displayed bound controls the width correction within the quoted clock approximation, not necessarily the entire error of the actual finite-width clock response. The ideal wide-start conclusions may avoid this limitation, but that does not establish the unqualified finite-width bound.
- **Suggested fix:** State the clock-level expansion regime and order where Eq. (3.36) is used, and distinguish the width bound from the omitted level-spacing remainder. If no level-spacing restriction is needed for the ideal limit, justify that separately.

### I3. The fixed-contract replacement formula omits the compensating scalar term
- **Location:** Step 5(c), Eq. (8.22)
- **Severity:** minor
- **Problem:** Eq. (8.22) claims an “if and only if” characterization of replacements leaving $`C`$ unchanged, while permitting $`C_f'=C_f+c\mathbb 1_f`$. The other displayed conditions preserve the coefficients of $`b_1`$ and $`b_2`$, but do not cancel the resulting $`c\mathbb 1`$ in the total contract. In the stated family with body contracts $`C_i^{\rm D}+\beta_i b_i`$, there is no displayed scalar parameter providing that cancellation. The later prose mentions “and −c,” but the characterization itself remains incomplete.
- **Suggested fix:** Include the compensating $`-c\mathbb 1_{b_1b_2c}`$ in the reduced/body-medium contract, as in Eq. (2.20), or require $`c=0`$ in the family as presently parameterized.

### I4. The zero coupling is an exception to the non-invariance of θᵢγ
- **Location:** Step 5(c), Eq. (8.13)
- **Severity:** minor
- **Problem:** Under condition (N), the statement that the value of $`\theta_i\gamma`$ is not well defined overlooks an uncoupled type. If $`\theta_i=0`$, the fixed-contract argument proves that $`\theta_i'=0`$ in every equivalent parameterization of this family. Thus $`\theta_i\gamma=0`$ is invariant, even though the other body may satisfy the nonzero-interaction condition. The shift $`\theta_i\gamma\mapsto\theta_i\gamma+a\theta_i`$ demonstrates non-invariance only when $`\theta_i\neq0`$.
- **Suggested fix:** Qualify the non-invariance claim by $`\theta_i\neq0`$, and state explicitly that the value is identically zero and invariant for an uncoupled type under (N).

## Focus points

None given.
