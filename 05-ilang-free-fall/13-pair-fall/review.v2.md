# Review: 13-pair-fall v2

- **Subproject:** 05-ilang-free-fall
- **Package:** 13-pair-fall
- **Reviewed version:** v2
- **Date:** 2026-10-11

---
VERDICT: minor issues

The displays (13.1)–(13.22) were recomputed and the script was run again with identical numbers. The issues below concern statements with "all", "only", "unless", "in general" and their exceptional members, which the question asks for under "Assumptions". The issues I1–I3 of the review of v1 are settled.

## Issues

### I1. The comparison with one part for $`g_1\neq g_2`$ lacks its exceptional member
- **Location:** Step 6, item 4, third bullet; Result, table of item 5, first row, last column; JSON twin, key result (13.15)
- **Severity:** minor
- **Problem:** For the common gradient with $`\tau_1\neq\tau_2`$ the second bullet names the member at which the pair falls like one of its parts (the value $`u_*`$). For $`g_1\neq g_2`$ the third bullet says "Otherwise not at all" and names only $`g_1M_1+g_2M_2=0`$. By (13.15) the ratio $`a_{\rm pair}/a^{(i)}`$ is also $`1`$ for one value of $`g_1/g_2`$ at a given $`u`$, for both signs of $`w_{11}`$. Step 7, item 3, and the third row of the table name this member for $`\mathsf w_i^2=\tau_i^2`$, which for $`\langle X\rangle=0`$ is the same condition at leading order. The two places do not agree, and the first row of the table and the twin follow the incomplete one.
- **Fix:** Name the member in Step 6, item 4, third bullet, with the value of $`g_1/g_2`$ and the statement that it concerns one part only. Bring the first row of the table and the key result (13.15) of the twin in line with it.

### I2. The condition for equal numbers $`\mathsf w_1^2=\mathsf w_2^2`$ at relative order $`\epsilon^2`$
- **Location:** Step 7, item 3, second bullet
- **Severity:** minor
- **Problem:** The bullet says that for $`g_1=g_2`$ the two numbers are not the same at relative order $`\epsilon^2`$ "unless $`\tau_1/\bar M_1=\tau_2/\bar M_2`$". By the remark under (13.17), the quantities $`a`$, $`u`$ and $`\Lambda`$ in (13.18) are taken with $`\bar M_i`$ for the part that is read and $`M_j`$ for the other part, so they differ between $`i=1`$ and $`i=2`$ unless the level of each part is its mean rest cost. The bracket of (13.18) is then not the same for the two parts, and the stated condition is neither shown to be necessary nor sufficient.
- **Fix:** State the condition that (13.18) gives, with the two sets of data named (for example by a label on $`u`$ and $`\Lambda`$), and say for which members it reduces to $`\tau_1/\bar M_1=\tau_2/\bar M_2`$. Use the same labels wherever $`u`$ of (13.13) and $`u`$ of (13.18) appear together.

### I3. $`\mathsf w_i^2`$ for $`g_i=0\neq g_j`$ is not given, and the member $`\varrho_i=0`$ is not located
- **Location:** Step 7, item 3, fourth bullet; table of item 5, third row; JSON twin, key result (13.19)
- **Severity:** minor
- **Problem:** Item 4(b) of the question asks for $`\mathsf w_i^2`$ wherever $`\varrho_i\neq0`$. For $`g_i=0\neq g_j`$, (13.18) gives $`\varrho_i\neq0`$ at order $`\epsilon^2`$, so the number is asked there. The bullet says that it "follows from (13.13) and (13.18)" and does not give it; its order in $`\epsilon`$ differs from that of (13.19), and the three answers of item 4(b) are not stated for it. The member $`\varrho_i=0`$, which the question names among the exceptional members, is not located: by (13.18) it lies at a ratio $`g_i/g_j`$ of order $`\epsilon^2`$.
- **Fix:** Give $`\mathsf w_i^2`$ for $`g_i=0\neq g_j`$ at leading order, with its remainder and the three answers. State the ratio $`g_i/g_j`$ at which $`\varrho_i=0`$, at the order that (13.18) determines, and that $`\mathsf w_i^2`$ is not defined there. State the range of $`g_i/g_j`$ in which (13.19) holds with its factor $`1+O(\epsilon^2)`$.

### I4. "The limits do not commute in general" without a member
- **Location:** Step 5, item 3, bullets 1 and 2; Result, item 2(c); JSON twin, key result (13.11)
- **Severity:** minor
- **Problem:** The non-existence of the limit in the other order is shown for windows with $`\mathsf f_i\neq0`$, and $`\partial_P\langle\mathcal K\rangle_{P_0}\neq0`$ is given as a sufficient condition. No member of the class is shown to satisfy it, and the members that the package treats in closed form (items 3 and 4 at $`P_0=0`$) are among those with $`\mathsf f_i=0`$. "Do not commute in general" needs at least one member.
- **Fix:** Exhibit one member of the class with $`\partial_P\langle\mathcal K\rangle_{P_0}\neq0`$, analytically from the quoted inputs or with the numerical level of the script (state which), or state the answer to item 2(c) as conditional.

### I5. Summary sentences without their order or their trivial member
- **Location:** Result, item 3, last two sentences; Step 6, item 5, last bullet; Step 6, item 2, sentence "Equivalently ..."
- **Severity:** minor
- **Problem:**
  - "Its fall is the same for all pairs of levels only if all gradients vanish" holds at fixed $`u`$. In the ordered wide-pair limit the condition is $`\langle X\rangle=0`$ and $`\tau_1^2g_1=\tau_2^2g_2`$ (Step 6, item 5), which the sentence does not say.
  - "The pair falls like its parts only for ..." and "The pair does not, at any fixed $`u`$" do not exclude the member without a fall, which the table excludes ("with a non-zero fall").
  - "Equivalently $`a_{\rm pair}=-(g_1M_1+g_2M_2+2\kappa\langle X\rangle)/\mathfrak m_b`$" follows a display with remainders; it is not said whether it is exact or at leading order. The exact form is the first line of the item.
- **Fix:** State each sentence with its order and its exceptional member, as the table and Step 6 do.
