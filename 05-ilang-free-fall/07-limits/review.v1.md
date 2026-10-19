# Review: 07-limits v1

- **Subproject:** 05-ilang-free-fall
- **Package:** 07-limits
- **Reviewed version:** v1
- **Date:** 2026-10-11

---
VERDICT: major errors

## Issues

### I1. The order of the first deviation of the coherences is answered for even starts only
- **Location:** Step 5, parts 2 and 3, Eq. (7.9), (7.10); Result, line of (7.8)–(7.10); Step 10, row "Superposition of levels"; Open issues, first item; key results 7.9 and 7.10 of the JSON twin
- **Severity:** major
- **Problem:** Item 1(f) asks for the order in the gradients at which $`\lvert\Gamma_{kk'}\rvert`$ first deviates from its value at zero gradients, and for the leading term, for a start at rest. The class of item 1 is every $`g`$; a start at rest is one whose label weight is concentrated at $`p_0=0`$, and neither $`g`$ nor $`\lvert g\rvert^2`$ has to be even. The parity argument of (7.9) is exact, but it holds for even $`g`$ only, and the text says that for other starts "a first-order term is not excluded". So for the class that the question names, the order of the first deviation is not determined. The Result and the table of Step 10 nevertheless state "second order in the gradients" without the restriction to even $`g`$, and the gap is recorded under "Open issues" only.
- **Fix:** Determine the first order in the gradients of $`\lvert\Gamma_{kk'}\rvert`$ for a general start at rest (complex $`g`$, a label weight that is not even): whether it vanishes, and if it does not, its leading dependence on $`\lambda`$, on the level data and on the start. For its coefficient an order estimate with stated conditions suffices, as the question allows. State the class of starts for which the first deviation is of second order, and the class for which it is of first order, and for the latter whether a level-independent fall removes it. Bring the Result, the row of the table and the JSON twin in line, so that each states its class.

### I2. Two statements that hold only under a condition that is not stated
- **Location:** Step 3, the sentence after Eq. (7.5) ("In $`\mathcal C_{\rm lev}`$ equality at one $`p_0`$ is one condition ... and needs $`\tau_k\neq\tau_{k'}`$"); Step 9, part 1, the sentence after Eq. (7.20) ("For $`\tau_k=\tau`$ the upper and the lower condition coincide ...")
- **Severity:** minor
- **Problem:** The first statement fails for two levels with equal data, $`\tau_k=\tau_{k'}`$ and $`M_k=M_{k'}`$, for which the velocities are equal at every $`p_0`$, as the next sentence of the text itself says. The second writes the common value as $`-g\,w`$ and solves for $`u_k`$, which presumes $`g\neq0`$; for $`g=0`$ the condition is on $`\mathcal F_U/M_k`$ alone.
- **Fix:** State each sentence with the condition under which it holds, and treat the excluded case.

Everything else of v1 stays as it is, with the same tags: (7.1)–(7.8), the parity statement (7.9) for even $`g`$, the estimate (7.10) with its conditions (E1)–(E3), (7.11)–(7.22), the consistency checks and the remaining open issues.
