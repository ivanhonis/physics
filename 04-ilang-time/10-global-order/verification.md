# External verification: 10-global-order

- **Subproject:** 04-ilang-time
- **Package:** 10-global-order
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-10T17:07:47+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The sequential-reading formula, single-event commutator conditions, equivalence theorem, three examples, and order-exchange bound are correct under the stated assumptions. The derivation answers all five requested items and correctly identifies the schedule’s application of the reading update—not reversible evolution—as fixing the direction. A minor qualification is needed where the general characterizations cease to state explicitly the pair-term restriction imposed by A5.

## Issues

### I1. Pair-term restriction is dropped in some characterizations
- **Location:** Step 6, Consequences; Consistency checks 1–2; Open issues
- **Severity:** minor
- **Problem:** Step 6 correctly establishes that an asymmetric equivalence exists iff there is a split with $`F_2`$ a sum of allowed pair terms, but subsequently calls “not split” the exact criterion for detectable common now. The definition of “split” in (10.5) does not include that locality requirement, so the unqualified statement is stronger than the established criterion. Similarly, the consistency checks describe the equivalences of a diagonal contract as all triples with arbitrary real diagonal $`D`$, whereas for more than two objects an arbitrary diagonal operator can contain irreducible three-object terms and violate A5. The setup and final proviso partly supply the intended qualification, but these characterizations should retain it explicitly.
- **Suggested fix:** State the exact criterion as the absence of a split whose components are sums of allowed pair terms. Wherever diagonal $`D`$ parameterizes admissible contracts, explicitly require $`D`$ to satisfy A5 as well as the stated diagonal and commutation conditions.

## Focus points

None given.
