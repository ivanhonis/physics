# Review: 06-two-clocks v1

- **Subproject:** 05-ilang-free-fall
- **Package:** 06-two-clocks
- **Reviewed version:** v1
- **Date:** 2026-10-11

---
VERDICT: major errors

## Issues

### I1. The equivalence (6.21), the answer to item 3(d), is false as displayed
- **Location:** Step 12, Eq. (6.21) and the first bullet under it; Result, item 3; key result 6.21 of the JSON twin
- **Severity:** major
- **Problem:** The left side of (6.21) is "(6.11), $`V_k`$ level-independent, $`\tau_k=\tau`$". This does not imply the right side. The control of Step 9 is a counterexample: the class $`\mathcal C`$ with $`g_m=g_\eta=g_\zeta=g\neq0`$ and $`\mathcal F\neq0`$ has a common response of all gaps (6.13), equal level offsets ($`V_k=0`$) and $`\tau_k=\tau`$, but $`a_{k,\sigma}(0)=-\tau^2g+\sigma\tau^2\mathcal F/M_k`$ depends on the level. The third line of (6.17) has the correct condition, $`V_k=V_\circ`$ for all $`k`$, that is $`\mathcal F_k=0`$; "equal level offsets" is weaker, because under (6.11) it leaves a common $`\mathcal F_k=c-g_*V_k\neq0`$. The sentence below (6.21), "Both sides are the members with ... $`\mathcal F_k=0`$ and equal level offsets (left: (6.17))", does not follow from the left side as displayed. The first bullet says "a fall that is the same for all levels" without saying for which branches; the stated further conditions are those of the third line of (6.17) (both branches, one value), and for one branch alone the conditions are the first two lines of (6.17).
- **Fix:** Restate (6.21) so that both directions hold, with the condition on the plain parts in the form in which (6.17) proves it, and check the restated equivalence against the controls of Steps 9 and 10. In the two bullets say for which branches each statement is made, and give the one-branch statement with its own exact condition. Bring the Result and the JSON twin in line.

### I2. Statements that rest on the reading "equal level offsets" elsewhere
- **Location:** Step 10, Eq. (6.19) and its bullets; Step 14, Eq. (6.24), (6.25); Step 16
- **Severity:** minor
- **Problem:** After I1 the conditions on the plain parts occur in three forms in the text: "$`V_k=V_\circ`$", "$`V_k`$ level-independent" and "$`g_*V_k`$ level-independent". They are different conditions, and each is correct only together with what is assumed about $`\mathcal F_k`$ at that place ((6.19) and (6.25) assume or contain $`\mathcal F_k=0`$; (6.17) does not). The text does not say this where the forms are used, and the error of I1 arose from exchanging them.
- **Fix:** At each of these places state which condition on $`\mathcal F_k`$ is in force, so that the form of the condition on the level offsets is justified there. No result other than (6.21) is expected to change; if one does, say so in "Changes from previous version".

Everything else of v1 stays as it is, with the same tags: the responses (6.3)–(6.6), the readings (6.7) and the statement (6.8) that no reading of the local member contains the branch gap, (6.9)–(6.20), the identity (6.22), (6.23)–(6.28), and the open issues.
