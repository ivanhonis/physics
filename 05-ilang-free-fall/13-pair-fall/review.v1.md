# Review: 13-pair-fall v1

- **Subproject:** 05-ilang-free-fall
- **Package:** 13-pair-fall
- **Reviewed version:** v1
- **Date:** 2026-10-11

---
VERDICT: minor issues

## Issues

### I1. Derivatives of leading-order forms are used without a stated basis
- **Location:** Step 7, Eqs. (13.18), (13.19), (13.20); Result, item 4; Open issues, fourth item
- **Severity:** minor
- **Problem:** The relative change $`\varrho_i`$ is a derivative of the rate (13.17) in the data of the two parts. The quoted (11.14), (11.20) give the values of $`\langle\sigma^{(i)}_3\rangle_0`$ and $`\Gamma_i`$ up to $`O(\epsilon^4)`$, not their derivatives in $`M_1`$, $`M_2`$. v1 names this as an assumption for the term of order $`\epsilon^2`$ of (13.18) and says that (13.19) and (13.20) do not use it. They do use a statement of the same kind: "$`\varrho_i=g_i`$ at leading order", and with it the factors $`1+O(\epsilon^2)`$ of (13.19) and (13.20), needs that the derivative of $`\Gamma_i-1`$ in the data vanishes for $`\epsilon\to0`$. So the basis of the leading order of $`\varrho_i`$ is not stated, and the sentence on what (13.19), (13.20) use is not correct.
- **Fix:** The question now quotes, with (11.14), the statement of 11-bound-pair that licenses the differentiation of (11.12) in the data with remainders that stay $`O(\epsilon^4)`$ (see the amended intro of (11.14) in question.md). Derive (13.18), (13.19) and (13.20) from it, state for each which derivative is used and to which order, and remove the assumption. If a derivative is still needed that this input does not cover, name it with the result that needs it.

### I2. Key result (13.19) of the twin drops the exceptional members
- **Location:** JSON twin, key result (13.19); Step 7, item 3, first bullet
- **Severity:** minor
- **Problem:** The twin states "it is not $`\tau_i^2`$" without a condition. The text lists the exceptional members: for the common gradient the value $`u_*`$ at which one of the two ratios is $`1`$, and for $`g_1\neq g_2`$ one value of $`g_1/g_2`$ at a given $`u`$. The summary says more than the result it cites.
- **Fix:** State the key result with its exceptional members, as the text does. Read the other key results and the table of item 5 against their displays in the same way.

### I3. The other order of the limits after the amendment of the question
- **Location:** Step 5, item 3; Result, item 2(c); Open issues, second item
- **Severity:** minor
- **Problem:** The question asked for both orders of the limits, each with the quantity it defines; v1 shows that the limit with the sharp total label first does not exist on the class in general and leaves the quantity on a subclass uncharacterized, as an open issue. The question has been amended: the drift acceleration is defined with the window first, and for the other order only the statement whether the limits commute on the class, with what is shown, is asked; its evaluation is not asked.
- **Fix:** Keep the argument of Step 5.3. State its result as the answer to the amended item 2(c) (what is shown: non-existence on the class, dependence on the place of the packet), and remove the open issue or restate it as outside the scope of the question.
