# Review: 04-profile v1

- **Subproject:** 06-ilang-source
- **Package:** 04-profile
- **Reviewed version:** v1
- **Date:** 2026-10-19

---
VERDICT: major errors

## Issues

### I1. The value and the sign of the mutual cost depend on the zero of the source operator (M6)
- **Location:** Setup ("Mutual cost", (4.1): "computed from the total contract and the state only"); Step 2 (last sentence of (4.4)); Step 3 and (4.5) (sign, "negative iff"); Step 4 and (4.6), (4.7) ("both are negative"); (4.13), (4.14); Result (4.1), (4.4)–(4.7), (4.13), (4.14)
- **Severity:** major
- **Problem:** (4.1) is a double difference that switches the sources off ($`g_i=0`$). Under the replacement $`G_i\to G_i+c`$, $`C_f\to C_f-c\,\Phi_{x_i}`$, which leaves the total contract unchanged (A5, M6), the eigenvalue of the body becomes $`g_i+c`$ and "switching off" refers to another reference contract; the double difference changes. The claim of the Setup that $`M`$ is computed from the total contract and the state only is therefore not shown, and the statements on the value and the sign of $`M`$ (positive somewhere, negative iff ..., negative on the tori, opposite in the highest state, the sign of the control) are statements on a split-dependent quantity. What the total contract and the state fix is the dependence of the total cost on the places of the sources at fixed bodies; on a vertex-transitive graph the single-source terms do not depend on the place, so differences such as $`M(d)-M(d')`$ equal differences of the total cost.
- **Fix:** State which quantities are invariant under the replacements of the listed terms (the dependence of the total cost on the places, its differences between configurations, and whatever else is), show it, and restate every value and sign statement on $`M`$ as a statement on the invariant quantity (for example the dependence on $`d`$ and its monotonicity), or mark it explicitly as a statement in the stated split. Keep the formulas; change the claims.
