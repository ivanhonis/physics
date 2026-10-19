# Review: 07-limits v4

- **Subproject:** 05-ilang-free-fall
- **Package:** 07-limits
- **Reviewed version:** v4
- **Date:** 2026-10-11

---
VERDICT: major errors

## Issues

### I1. Case A without a window does not give (7.16): the acceleration of third order in the records at rest
- **Location:** Step 8, part 2, the table (7.44), row A ("fixed smooth $`g`$; $`\mathcal D_k\to\infty`$ or a long window"), the paragraph "Case A" with (7.16), and the sentence "Without a window"; Step 8, part 3 (case A); Step 10, row "Records"; Result, the bullets "(7.41), (7.44)" and "(7.15), (7.16), (7.33)"; key results 7.44 and 7.16 and the definition of the cases A and B in the JSON twin
- **Severity:** major
- **Problem:** The defining condition of case A offers two alternatives, "$`\mathcal D_k\to\infty`$" (no window) or a long window, and assigns (7.15) and (7.16) to both. For the order $`\kappa^3`$ at rest the first alternative is false. The instantaneous acceleration is $`a_3[g](\lambda)=3s_3\lambda^2+\partial_\lambda R_3(\lambda)`$. By Step 7, part 4, of this version, $`R_3`$ is an oscillating term with the rate $`2\omega_k`$ and the size $`O(t_k\nu_k\lambda^3\mathcal D_k^{-1/2})`$, that is $`\propto\lambda^{5/2}`$ at rest. A bound or an estimate of an oscillating term does not bound its derivative: $`\partial_\lambda R_3`$ is of the order of $`2M_k`$ times that size, also $`\propto\lambda^{5/2}`$, and it grows faster than the secular term $`3s_3\lambda^2`$. So for a fixed smooth $`g`$ at rest $`a_3[g](\lambda)/\lambda^2`$ has no limit for $`\lambda\to\infty`$, and the dephasing alone does not lead to (7.16). A direct numerical integration made for this review (real Gaussian label weight at rest, $`\delta p=0.25`$, $`\tau=0.7`$, $`M=1.3`$, $`\lambda`$ up to $`400`$, $`\mathcal D_k`$ between $`1`$ and $`9`$) shows $`a_3[g](\lambda)`$ oscillating around $`3s_3\lambda^2`$ with an amplitude between $`1.1`$ and $`1.5`$ times $`3s_3\lambda^2`$, increasing with $`\lambda`$, while the window averages agree with the identity of (7.33). (7.16) is therefore the derivative of the secular velocity term, and the leading part of a window average under a condition on the window; it is not the acceleration after dephasing. The sentence after (7.16), "that it is the fastest-growing part rests on the estimate of $`R_3`$", holds for the velocity and for window averages only. At the order $`\kappa^2`$ the statement "Without a window" is supported only for $`p_0`$ "away from the stationary points of $`\omega_k`$", without the scale on which this is meant, while (7.15) is used near rest, where the label weight can contain the stationary point $`p=0`$.
- **Fix:** Define case A separately for the two orders, and state for each quantity the order of limits in which it is obtained.
  - Order $`\kappa^3`$: (7.16) holds for the window average, with the identity of (7.33); state the condition on the window under which the rest $`\bigl(R_3(\lambda_1+\Lambda)-R_3(\lambda_1)\bigr)/\Lambda`$ is small against $`3s_3\bar\lambda^2`$, and the size of the term $`\Lambda^2/12`$. Determine the instantaneous acceleration $`a_3[g](\lambda)`$ of a fixed smooth $`g`$ at rest for $`\mathcal D_k\gg1`$: the size and the growth in $`\lambda`$ of its oscillating part against $`3s_3\lambda^2`$ (an order estimate with its calculation suffices), and state that without a window it is not (7.16). State the dependence on the level of each of the two quantities.
  - Order $`\kappa^2`$: state the no-window statement with its range: how far $`p_0`$ has to be from a stationary point on the scale of $`\delta p`$, and what holds for a label weight that contains a stationary point (in particular near rest).
  - Bring the table (7.44), Step 8, part 3, the row "Records" of (7.22), the Result and the JSON twin in line with this.

### I2. (7.46) is called necessary without a proof
- **Location:** Step 8, part 4, the sentence "It is also necessary up to factors of order one when the record terms of the levels differ by relative amounts of order one"; the wording "has to mean (7.46)" at the end of Step 8 and in the Result, bullet "(7.17), (7.18), (7.34), (7.46)"
- **Severity:** minor
- **Problem:** The left side of (7.46) is a sum of upper bounds and of one estimate. Two things separate it from the record terms themselves. First, $`\varrho_{2,\rm rest}`$ is a bound that contains $`X_g`$; the rest it bounds can be far smaller, for example for a label weight that is nearly even about $`p_0=0`$, for which $`\langle v_2\rangle_g`$ is nearly zero while $`c_1[g]`$ is not. Second, the terms have signs: the term of order $`\kappa^2`$ is proportional to $`v`$ and the term of order $`\kappa^3`$ to $`\sigma\mu_3`$, so they can cancel, while (7.46) adds their absolute values. So the fall can be the same for all levels to the accuracy $`\delta_{\rm acc}`$ while (7.46) fails by more than a factor of order one. The condition is proven as sufficient only.
- **Fix:** State (7.46) as a sufficient condition. State as necessary only what is proven: the condition on the difference of the window-averaged record terms of two levels, and, if wanted, the regime in which it reduces to conditions on $`\varrho_2`$ and $`\varrho_3`$ (with the conditions under which the rests are small and the two terms do not cancel). Word the answer to "what the weak-record regime has to mean" accordingly, in Step 8 and in the Result.

### I3. "No further reduction to moments exists" is asserted without a proof
- **Location:** Step 5, part 6, first sentence
- **Severity:** minor
- **Problem:** For starts at rest that are not narrow, the sentence says that no further reduction of (7.24) and (7.35) to moments exists. That the functions $`\rho`$ and $`j`$ enter as a whole is shown; that no reduction exists is a claim about all possible reductions and is not proven.
- **Fix:** Say that no reduction to finitely many moments is derived here, and keep the statement that the results are the exact functionals (7.24), (7.35) with the case distinction (7.36).

Everything else of v4 stays as it is, with the same tags: Steps 1–4, 6, 7 and 9; Step 5 apart from the sentence of I3; in Step 8 the exact acceleration (7.41), case B with (7.42) and (7.43), the bound (7.33), the level speed bound (7.45), (7.17), (7.18) and (7.34); the consistency checks; the open issues that are not affected. Checked for this review and found correct: (7.35), (7.37), (7.38), (7.40), (7.41), the first line of (7.42) and its window bound, and, by a direct numerical integration, (7.13) and both lines of (7.43).
