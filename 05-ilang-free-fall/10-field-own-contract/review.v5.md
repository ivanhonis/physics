# Review: 10-field-own-contract v5

- **Subproject:** 05-ilang-free-fall
- **Package:** 10-field-own-contract
- **Reviewed version:** v5
- **Date:** 2026-10-11

---
VERDICT: minor issues

## Issues

### I1. The equivalence for one speed is stated for any number
- **Location:** Step 3(d), "Answer at this order", second item ("With one speed $`w\,d_0`$ for all levels (the second or the third of (10.38), or any one number) ... it holds for all levels if and only if $`g\,\rho_0=0`$"); the same statement in the relation row of the table of Step 5, in the Result (item 3) and in the key result (10.40) of the JSON twin
- **Severity:** minor
- **Problem:** By (10.40), in the members with $`\mathcal R^{\rm lev}_k=0`$ for all $`k`$ the defect with one speed is $`\mathcal R^{(w)}_k=(w^2-\tau_k^2)\,g`$. For $`\rho_0=0`$ and $`g\neq0`$ all $`\tau_k`$ equal $`\tau`$, and the defect is $`(w^2-\tau^2)\,g`$: it vanishes for the second and the third reading of (10.38), which are then both $`\tau d_0`$, and it does not vanish for another number $`w\neq\tau`$. So "if and only if $`g\,\rho_0=0`$" holds for the two readings of (10.38) and is false for "any one number".
- **Fix:** State the equivalence for the second and the third reading of (10.38), and give separately the condition for an arbitrary number $`w`$ (from $`\mathcal R^{(w)}_k=(w^2-\tau_k^2)\,g`$). Bring the table row, the Result and the twin into agreement.

### I2. "Only" for a range that is sufficient
- **Location:** Step 3(c), paragraph after (10.37), the sentence "The statistics is then that of the standing ring clock ($`r=0`$) to the accuracy $`\eta`$ only for $`\lambda\le2\eta\,\Sigma/(N(x_0)\,d_{N-1}^2)`$, the range of (10.16)"
- **Severity:** minor
- **Problem:** (10.16) is an upper bound on the total variation, so the range that follows from it is sufficient for the accuracy $`\eta`$. The sentence states it as necessary ("only for"); that is not derived.
- **Fix:** State the range as the sufficient range of (10.16). If a statement on what happens beyond it is wanted, derive it from the phases $`\delta E_k\lambda`$ of (10.37); otherwise say that nothing is derived beyond it.
