# Review: 02-clock v1

- **Subproject:** 04-ilang-time
- **Package:** 02-clock
- **Reviewed version:** v1
- **Date:** 2026-10-09

---
VERDICT: minor issues

## Issues

### I1. Item 4(a) is answered completely only for the minimal member
- **Location:** Step 6, Eq. (2.17), and the second item of "Open issues"
- **Severity:** minor
- **Problem:** Item 4 concerns every self-driven uniform ring clock with $`\theta_m=0`$, i.e. every admissible choice of the $`\ell_k`$ in (2.9). It asks to determine whether the first reading changes the distribution of the second outcome, and when.
  - v1 gives a sufficient condition for "no change" that holds for every member: $`\lambda_1\in\lambda_0\mathbb Z`$ or $`\lambda_2-\lambda_1\in\lambda_0\mathbb Z`$.
  - It proves the exact condition only for the minimal member.
  - For the other members, "Open issues" records further no-change values, with an example, but no condition.

  A requested item is thus left partly unanswered. Every step that v1 does derive is correct; I checked them, including the computation of $`\hat D`$ in (2.17).
- **Fix:** Determine a necessary and sufficient condition, valid for every member with $`\theta_m=0`$, under which the first reading leaves the distribution of the second outcome unchanged. Derive it, for example from all discrete Fourier components of $`D(m)`$, as Step 6 does for one component in the minimal case. Keep the minimal-member result (2.17) as a special case of the general condition. Remove the corresponding open issue.

### I2. The extra assumption S2 is not stated in the results that use it
- **Location:** Result, items (2.14)–(2.18); Setup, S2
- **Severity:** minor
- **Problem:** Item 4 rests on S2: the state after a reading is admissible, which holds when no object of $`R`$ has the type of $`k`$. The Setup and "Open issues" state this, but the Result lines (2.14)–(2.18) do not. A later package that quotes these results would lose the condition.
- **Fix:** State the condition S2 in the Result lines of (2.14)–(2.18), or once in the Result for item 4. Keep the tags and their meanings.
