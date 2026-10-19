# Review: 04-branch-fall v1

- **Subproject:** 05-ilang-free-fall
- **Package:** 04-branch-fall
- **Reviewed version:** v1
- **Date:** 2026-10-10

---
VERDICT: minor issues

## Issues

### I1. The fixed-lambda sharp-label limit and the commutation criterion are stated beyond the class of starts for which they are proven
- **Location:** Step 4, part 3 (sentence after (4.13)) and part 4, Eq. (4.14); Result, item 1; the sentence "The limits commute at rest" wherever it occurs
- **Severity:** minor
- **Problem:** (4.13) is derived for families of starts that are centred at $`x_c`$, that is, for which $`\xi_g\frac{\mathrm dp}{2\pi}\to x_c\,\delta_{p_0}`$. The criterion (4.14) for the commutation of the limits "long window" and "sharp label", and the Result, are stated without this hypothesis. The sentence "For a family that is not centred, the term with $`\xi_g`$ need not converge unless $`\theta'B_\perp(p_0)=0`$" asserts convergence for every family when $`\theta'B_\perp(p_0)=0`$; this is not proven and is false as a statement about the value of the limit. For a family whose $`\xi_g`$ is not asymptotically $`x_c\lvert g\rvert^2`$, for example $`g`$ with a phase that is quadratic in $`p-p_0`$ with a coefficient of the order $`1/\delta p^2`$, $`\int\frac{\mathrm dp}{2\pi}\xi_gF`$ tends to a term with $`F'(p_0)`$ that depends on the family, also when $`F(p_0)=0`$; if the coefficient of the phase is not bounded in these units, the limit does not exist. So at fixed $`\lambda`$ the sharp-label limit of the first-order acceleration, the form (4.13), the criterion (4.14) and "the limits commute at rest" are established for centred families only. The drift acceleration (4.11) is not affected: it is proven for every $`g`$.
- **Fix:** State (4.13), (4.14) and the corresponding sentences of the Result for the class of families for which they are proven, and name that class in the statements themselves. For families outside it, say exactly what is proven and what is not: either extend the proof to a wider, explicitly named class (for example families for which $`\int\frac{\mathrm dp}{2\pi}\xi_gF`$ converges for every smooth periodic $`F`$, with the limit functional stated), with the resulting form of the fixed-$`\lambda`$ limit and of the commutation statement at rest and in motion, or state that this part of item 1(b) is not determined for them. Remove the unproven sentence or replace it by a proven one. Everything else of v1 stays as it is, with the same tags.
