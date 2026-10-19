# Review: 08-two-types v3

- **Subproject:** 05-ilang-free-fall
- **Package:** 08-two-types
- **Reviewed version:** v3
- **Date:** 2026-10-11

---
VERDICT: minor issues

## Issues

### I1. The records, the distances and the bound are stated for all of the set of equivalent descriptions, but written down only without the term between the two bodies
- **Location:** Step 7, paragraph "What holds in every equivalent description", bullet "Contract and records", and the first line of Eq. (8.25); the "transported form" wherever it uses the hop distance, the bound and the mean position of $`C'`$ (Step 7, Step 8, Result item 6); key result 8.25 of the JSON twin
- **Severity:** minor
- **Problem:** The bullet says that the record of the place $`h`$ of $`b_i`$ in $`C'=F_1/a_1+F_2/a_2+\Delta`$ is $`\frac{\kappa_ix}{a_i}X+q_i(h)\,\delta_i`$ "plus an operator that does not depend on $`h`$", and gives the record vector and the mean position from it. For $`\varepsilon_{12}\neq0`$ this is not the whole dependence on $`h`$: the term $`\varepsilon_{12}Q_1Q_2`$ of $`\Delta`$ contributes $`q_i(h)\,\varepsilon_{12}\,Q_j`$, an operator on the other body. Then the companion of $`b_i`$ in which the record acts is no longer the medium alone, and the construction of record vectors, distances and of the bound (5.11) of 04-ilang-time/05-moving-clock, as quoted from (17.15) of 03-ilang-space/17-motion for a body and a medium, is not defined without a further step. The first line of (8.25) nevertheless states $`d'_{0,i}`$, $`v'_i`$ and the acceleration of $`\bar x'_i`$ for every $`C'\in\mathfrak E`$, and the transported form of FA, RD, $`v_1=v_2`$ and (4.24) is said to be proven on all of $`\mathfrak E`$. The step from the statistics (which the equivalence fixes) to these quantities of the space is therefore written down only for $`\varepsilon_{12}=0`$.
- **Fix:** For $`\varepsilon_{12}\neq0`$ either state how the record of a place, the record vectors and the bound are defined in such a description and prove the first line of (8.25) for it, or restrict the statements about $`d'_{0,i}`$, $`v'_i`$ and $`\bar x'_i`$ to the subset of $`\mathfrak E`$ for which they are defined, and say for the rest exactly what is proven (for example the statements about place statistics, position labels and rates) and what is not defined. Bring the table (8.18), (8.19)–(8.21), the Result and the JSON twin in line, so that each names the set for which it is proven.

Everything else of v3 stays as it is, with the same tags: (8.1)–(8.24), (8.26), the Theorem on all equivalences with its proof, the sets $`\mathfrak E_0\subset\mathfrak E_1\subset\mathfrak E`$, the condition (N), and the open issues that are not affected.
