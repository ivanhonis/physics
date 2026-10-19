# Review: 08-two-types v1

- **Subproject:** 05-ilang-free-fall
- **Package:** 08-two-types
- **Reviewed version:** v1
- **Date:** 2026-10-11

---
VERDICT: minor issues

## Issues

### I1. The conditions of item 5 are displayed without the condition on the record mean under which they are exact
- **Location:** Step 5(b), Eq. (8.12) and the two sentences before it; Step 5(d), Eq. (8.14); Result, item 5; key results 8.12 and 8.14 of the JSON twin
- **Severity:** minor
- **Problem:** By (8.11) the effective plain gradient is $`\mathcal F_i=-\kappa_i\langle X\rangle`$, so $`(\mathrm L_i)`$ holds exactly only for $`\langle X\rangle=0`$. For $`\langle X\rangle\neq0`$ the fall of each type depends on the level, $`A^{(i)}_{k,+}=-d_{0,i}\tau_i^2\bigl(\gamma\theta_i+\kappa_i\langle X\rangle/M^{(i)}_k\bigr)`$, and FA as defined in item 2 fails for every $`\theta_1`$, $`\theta_2`$. The text says this before (8.12), but (8.12), (8.14), the Result and the twin state "FA $`\iff\kappa_1\tau_1^2\theta_1=\kappa_2\tau_2^2\theta_2\neq0`$" as an equivalence without the condition; the qualification stands only in the running text and under "Open issues". The sentence "at the leading order in $`\kappa_i`$ $`(\mathrm L_i)`$ holds for every $`\langle X\rangle`$" gives no size for what is dropped. The dropped term is of first order in $`\kappa_i`$ in the acceleration $`a^{(i)}_{k,+}(0)`$, of the relative size $`\kappa_i\langle X\rangle/(M^{(i)}_k\gamma\theta_i)`$; it is not among the terms $`O(\kappa^2\sigma_X^2)`$ that (4.16) neglects, and at first order in the gradients $`\mathcal F_i`$ counts as a gradient like $`\gamma\theta_i`$.
- **Fix:** State (8.12) and (8.14) with their condition inside the displays: exactly for $`\langle X\rangle=0`$; and for $`\langle X\rangle\neq0`$ say what holds exactly (FA fails) and what holds approximately, with the relative size of the level-dependent part and the range of $`\kappa_i`$, $`\langle X\rangle`$, $`\gamma\theta_i`$ on which it is small. State which of the conditions of (8.12) do not need $`(\mathrm L_i)`$ at all. Bring the Result and the JSON twin in line.

### I2. The comparison of (8.6) with FA is stated as an equivalence that fails for a zero common value
- **Location:** Step 2(c), last sentence after Eq. (8.6)
- **Severity:** minor
- **Problem:** "By (8.4) it coincides with FA iff $`d_{0,1}=d_{0,2}`$" is not true as stated: for $`\kappa_1=\kappa_2`$ and $`\tau_1^2g_{\eta,1}=\tau_2^2g_{\eta,2}=0`$ the statement (8.6) holds and FA fails, because FA requires a nonzero common value.
- **Fix:** State the comparison with the case of a zero common value treated, in both directions.

Everything else of v1 stays as it is, with the same tags: (8.1)–(8.5), (8.7)–(8.11), (8.13), the lemma (8.17) with its proof, (8.15), (8.16), (8.18)–(8.21), and the open issues that are not affected.
