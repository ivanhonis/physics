# Review: 07-bond-inertia v2

- **Subproject:** 08-ilang-propagation
- **Package:** 07-bond-inertia
- **Reviewed version:** v2
- **Date:** 2026-10-25

---
VERDICT: major errors

## Issues

### I1. The isolation of the light-range levels is left open, although the flipped sectors at nonzero labels decide it
- **Location:** Step 6 (iii)–(v), assumption (E), (7.15), Result (7.15), Open issues; twin (7.15, open issues).
- **Severity:** major
- **Problem:** The question asks for the isolation condition, and its note asks items 2 and 3 for isolated levels. Step 6 bounds the flipped sectors only with the members at label $`0`$, gives from this a necessary condition, and leaves open whether light levels are isolated. At joint label $`0`$ the two members can carry opposite labels. So consider the sector in which every member of the branch $`+`$ is in its branch $`-`$ and one quantum is present. Its energies reach about $`-\sqrt{\bar M_1^2+\tau^2}-\sqrt{\bar M_2^2+\tau^2}+m_h`$ (members at $`\pm\pi/2`$, quantum at $`0`$) and $`-\bar M_1-\bar M_2+\Omega_{\max}`$ (members at $`0`$ and $`\pi`$, quantum at $`\pi`$), and they form an interval (continuity in the labels). In the light range $`E_b(0)`$ lies between these two values. The open issue is therefore decidable with the means of Step 6, and (7.15) does not state the isolation condition the question asks for.
- **Fix:** Determine the isolation of the bound levels near labels $`0`$ in the whole range (N), with the flipped sectors at nonzero labels of both members. State it in Step 6, (7.15), (E), the Result, the Open issues and the twin.

### I2. The Result does not state the speed of the light range
- **Location:** Result (7.12) and (7.11); twin 7.11, 7.12.
- **Severity:** minor
- **Problem:** Step 8 states that in (N$`_l`$) with $`r`$ of order one only shallow levels exist. There $`D=\frac{\Delta E}{\tau^2}[1+O(\ell/a_b,(r\ell)^{-2})]`$ at every such $`r`$, so at leading order one speed $`\tau`$ holds for every allowed binding strength. The Result's (7.12) says instead "for $`r\neq1`$ the speed depends on the binding", without this range. Its "iff" holds for (7.10) taken exactly, not at the leading order at which the light range is stated. The twin's 7.11 drops the remainder $`O(\ell/a_b)`$, and its 7.12 omits the light range at $`r\neq1`$.
- **Fix:** For each part of (N), state in the Result and the twin which speed the bond's cost takes as a function of $`r`$, at the order of each statement.

### I3. Small slips
- **Location:** Step 8 ("One speed", the case $`(+,+)`$); twin 7.15.
- **Severity:** minor
- **Problem:**
  - Under the new (D) the alternative is $`r\le1`$, not $`r<1`$.
  - The twin's 7.15 drops "$`<r/2`$ for $`F_2\neq0`$".
  - The twin's 7.15 writes the implication $`\bar M_i<m_h/2`$ as if it defined the light range.
- **Fix:** Correct these.
