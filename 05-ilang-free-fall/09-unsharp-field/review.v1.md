# Review: 09-unsharp-field v1

- **Subproject:** 05-ilang-free-fall
- **Package:** 09-unsharp-field
- **Reviewed version:** v1
- **Date:** 2026-10-11

---
VERDICT: major errors

## Issues

### I1. In the subclasses with a factor whose value is not sharp, the plain gradient of the records is set to zero
- **Location:** Step 6, the sentence "it vanishes at the leading order in $`\kappa`$ used here", the table (9.16) and the two "yes" answers after it; Step 7, the use of $`a^\nu_{k,+}=a^\nu_{k,-}`$ and (9.18); Step 8, (9.19), (9.20), (9.21); Result, the columns "Within every sector", "Means in $`\mathcal S_{\rm a}`$" and "Means in $`\mathcal S_{\rm c}`$"; the key results 9.16–9.21 of the JSON twin
- **Severity:** major
- **Problem:** The setting of the question counts the term $`\kappa\,x\,\langle X\rangle`$ of the records in every $`V^\nu_{x,k}`$: the level profiles of a sector are those of its effective body contract, (8.19) of 04-ilang-time/08-maximal-speed. In $`\mathcal S_{\rm a}`$ and $`\mathcal S_{\rm c}`$ every sector therefore has the plain gradient $`\mathcal F^\nu_k=-\kappa\langle X\rangle`$, as Step 6 itself notes. v1 then drops it "at the leading order in $`\kappa`$". In 04-branch-fall, whose results are used here, "leading order in $`\kappa`$" means that the body evolves by the effective body contract, and the plain gradient of that contract is one of the gradients of the first order; (4.16) contains it. With it, $`a^\nu_{k,\sigma}(0)=\frac{(\tau^\nu_k)^2}{M^\nu_k}\bigl(\sigma\mathcal F^\nu_k-G^\nu_k\bigr)`$ has a part that depends on the level and is odd in the branch whenever $`\langle X\rangle\neq0`$. So the statements of Step 6 ("the same for all levels and both branches", "(4.24) holds", both "yes" without a condition), the value of $`\bar a`$ in (9.19), the equivalences and the leading deviation of (9.20), (9.21), and the entries "always" and "yes, both branches" of the table hold as stated only for $`\langle X\rangle=0`$. In Step 7 the equality $`a^\nu_{k,+}(p)=a^\nu_{k,-}(p)`$ is used for the two branch components and needs the same condition. The subclass $`\mathcal S_{\rm grad}`$ is not affected, because its $`\mathcal F^\nu_k`$ are general.
- **Fix:** Keep $`\mathcal F^\nu_k=-\kappa\langle X\rangle`$ in the level data of $`\mathcal S_{\rm a}`$ and $`\mathcal S_{\rm c}`$. State every result of Steps 6–8 and every entry of the table with its condition on $`\langle X\rangle`$: what holds for every $`\langle X\rangle`$, what holds if and only if $`\langle X\rangle=0`$, and for $`\langle X\rangle\neq0`$ the part of the sector drift accelerations and of $`\bar a`$ that depends on the level and the branch, with its size against the part produced by the field. Redo the argument of Step 7 without assuming $`a^\nu_{k,+}=a^\nu_{k,-}`$. Bring the JSON twin in line.

### I2. The example of a reading that leaves the weights unchanged is not a reading
- **Location:** Step 1(b), the sentence after (9.3) "Example: a reading of the clock level ..."
- **Severity:** minor
- **Problem:** A reading is a partition of the joint places (A4); the schedules of (2.17) use projectors that are diagonal in the places. The clock levels $`\lvert f_k\rangle`$ are not places of the body, so "a reading of the clock level" is not a reading of the language.
- **Fix:** Replace the example by a reading of the places whose distribution is the same in all sectors of $`S`$ (state why it is), or remove it.

### I3. The statements on the order of the limits in Step 3 are not derived, although the quoted (4.10) gives the constants
- **Location:** Step 3, the sentence after (9.8) "The last two limits commute only along sequences with $`R_i(g)/\lambda\to0`$; ... the bound in (9.7) diverges with the position spread $`X_g`$ of the start, and the inputs define no quantity in that order"; the bound $`{\rm rem}'`$ of (9.14); Open issues, second item
- **Severity:** minor
- **Problem:** The constants $`R_i(g)`$ are left unspecified, with the remark that their form in terms of $`X_g`$ is not quoted. The quoted bound (4.10), taken for the window $`[0,\lambda]`$, bounds the rest of the first-order velocity of (4.7) explicitly, with $`X_g`$ in it. Without this, two statements of the sentence are not supported: that the limits commute "only" along the named sequences (a condition that is sufficient is called necessary), and that the bound diverges with $`X_g`$ (nothing about $`R_i`$ was derived).
- **Fix:** Use (4.10) to give the remainder of (9.7), and of (9.14), with explicit constants, including the first-order velocity at $`\lambda=0`$. State the condition on sequences of starts and $`\lambda`$ under which $`\lambda\to\infty`$ and $`\delta p\to0`$ can be combined as a sufficient condition, and state what is and what is not shown for the other order of the limits.

Everything else of v1 stays as it is, with the same tags: Step 1 apart from the example of I2, with (9.1)–(9.4); Step 2 with (9.5), (9.6); in Step 3 the identities (9.7)–(9.9) apart from the constants and the sentence of I3; Step 4 with (9.10), (9.11); Step 5 with (9.12)–(9.15); in Step 7 the identity and the bound (9.17). Checked for this review and found correct: (9.2), (9.3), (9.4), the remainder of (9.7), (9.8), (9.9), (9.10), the control (9.11), (9.12)–(9.15), (9.17), and, for $`\langle X\rangle=0`$, the table (9.16) and (9.19)–(9.21).
