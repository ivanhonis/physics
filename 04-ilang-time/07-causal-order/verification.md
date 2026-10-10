# External verification: 07-causal-order

- **Subproject:** 04-ilang-time
- **Package:** 07-causal-order
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-10T12:58:58+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The outcome-averaged influence formula, locality expansion, qubit examples, and factorial influence bound are sound. The analyticity argument correctly rules out a delayed onset of nonzero influence, and the nontransitivity example is valid. However, the requested statement about every positive-delay pair for a fixed generic chain remains unresolved: the fixed-delay genericity result does not answer that question. There are also minor problems concerning non-influencing chains, degenerate inputs, and which bound is attained at leading order.

## Issues

### I1. The all-delay genericity question remains unanswered
- **Location:** Step 9(ii), Eq. (7.20), Result item 4, and Open issues
- **Severity:** major
- **Problem:** Equation (7.20) establishes generic influence for each prescribed delay, with an exceptional null set that may depend on that delay. The question instead asks whether a fixed chain with generic pair terms has influence for every pair of events with increasing λ. These quantifiers cannot be interchanged: exceptional delays may depend on the contracts. The countable-union argument for rational delays does not settle all real delays, and the nongeneric periodic example does not settle the generic case. The derivation explicitly acknowledges that this requested subitem remains undecided.
- **Suggested fix:** Supply and justify the all-delay conclusion for a fixed generic chain. Keep the fixed-delay and rational-delay results explicitly distinct from that conclusion; until the missing conclusion is established, mark this goal item as incomplete.

### I2. The fixed-contract discussion omits permanently absent influence
- **Location:** Step 9(ii), paragraph Fixed C
- **Severity:** minor
- **Problem:** This paragraph states, for a fixed C, that failures of influence occur only at discrete exceptional delays and never at sufficiently small positive delays. That requires $`\mathcal I_{ij}\neq\emptyset`$, the nonempty alternative in (7.14). For an allowed chain with a cut link between distinct cells $`i,j`$, influence is absent at every delay, as the derivation’s own consistency check correctly establishes. In that case the exceptional-delay set is all of $`(0,\infty)`$, not discrete.
- **Suggested fix:** Qualify the paragraph by assuming $`\mathcal I_{ij}\neq\emptyset`$, and separately retain the alternative that no positive delay permits influence.

### I3. Degenerate allowed inputs are not covered by the stated formulas
- **Location:** Step 6(a), Eq. (7.9), and Step 8, Eqs. (7.15)–(7.17)
- **Severity:** minor
- **Problem:** A one-class reading is allowed, but for $`m=1`$ the maximum in (7.9) is over an empty index set. Also, the setting permits $`\lVert J\rVert=0`$. Then the bound’s left-hand side in the threshold equation is identically zero, so there is no unique root $`\delta_\epsilon(r)`$; the strict-monotonicity assertion and finite-boundary discussion do not apply. These cases do not invalidate the substantive bound, but its presentation does not cover every allowed reading and contract system.
- **Suggested fix:** Handle $`m=1`$ separately with $`\delta P=0`$. State the threshold-root and moving-boundary derivation for $`\lVert J\rVert>0`$; when $`\lVert J\rVert=0`$, influence between distinct cells is identically zero and the guaranteed small-influence region is the entire domain, optionally represented by $`\delta_\epsilon(r)=\infty`$.

### I4. Leading-order attainment is attributed to the looser bound
- **Location:** Step 6(c), paragraph Leading order, and Result item 3
- **Severity:** minor
- **Problem:** The examples attain the reading-dependent bound
  ```math
  2(1-1/m)\sum_{k\ge r}\frac{(2\lVert J\rVert\delta)^k}{k!}
  ```
  at leading order when $`m=2`$. They do not attain the simplified bound $`2\sum_{k\ge r}(2\lVert J\rVert\delta)^k/k!`$ quoted in Result item 3: its leading coefficient is twice the examples’ coefficient. Indeed, the stronger reading-dependent bound precludes exact leading-order attainment of that simplified coefficient for any finite $`m`$.
- **Suggested fix:** Specify that the reading-dependent version of (7.12) is attained at leading order by the qubit examples, and remove the attainment claim for the simplified, reading-independent bound.

## Focus points

None given.
