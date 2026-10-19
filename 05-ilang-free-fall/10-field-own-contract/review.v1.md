# Review: 10-field-own-contract v1

- **Subproject:** 05-ilang-free-fall
- **Package:** 10-field-own-contract
- **Reviewed version:** v1
- **Date:** 2026-10-11

---
VERDICT: minor issues

## Issues

### I1. The phase of the hopping is said to change nothing for a start in one level
- **Location:** Step 2(b), the last two sentences on the phase $`\arg(1-M_k^2c_x)`$ ("this unitary is diagonal in $`(x,s,k)`$, so it changes no position or branch statistics and nothing for a start in one level"); Step 3(a), the sentence on the uniform phase $`\theta_k`$; Step 5, the table and (10.21); Result, item 2
- **Severity:** minor
- **Problem:** The unitary that removes the phase from the contract also acts on the start. The position statistics of the contract with the phase and a start $`\phi`$ are those of the contract without the phase and the start $`U\phi`$, and $`U\phi\neq\phi`$ for a start in one level: its plane-wave label is shifted. Step 3(a) says this ("it shifts the plane-wave label of the level block, $`p\to p-\theta_k`$"), in contradiction to Step 2(b). The consequence is not drawn: with the linear profiles of the field the phase $`\theta_k=M_k^2\mathrm{Im}\rho_Y`$ is uniform, the level block has the eigenvalues $`\pm\omega_k(p-\theta_k)`$, and a branch start at rest ($`p_0=0`$) has at zero gradients the velocity $`\sigma\,\omega_k'(-\theta_k)`$, which is of first order in $`Y`$, different from zero for $`\mathrm{Im}\rho_Y\neq0`$, odd in the branch and dependent on the level. That the drift acceleration changes only at second order in $`Y`$ is correct; but a motion of the body that depends on the level, at the order of the first corrections, is not named, and the summary of the orders does not contain it.
- **Fix:** Correct the sentence of Step 2(b): state what the unitary does to the start and for which statistics the two descriptions agree. Determine, for the linear profiles of the field, the velocity of a branch start at rest that the phase produces (its order in $`\epsilon_1`$, $`\epsilon_2`$ and in $`Y`$, its dependence on the level and the branch, and the condition under which it vanishes), and state that it is a velocity and not a drift acceleration. Add it to the table of Step 5 and to the Result.

### I2. The plain gradient of the records is dropped without a condition
- **Location:** Step 3(a), the sentence "The mean record $`\kappa\langle X\rangle x`$ of (8.19) adds $`-\kappa\langle X\rangle`$ to every $`\mathcal F_k`$ and vanishes at leading order in $`\kappa`$"; (10.13), (10.14), (10.17), (10.20); the rows "Fall from rest independent of the level" and "Relation (4.24)" of the table; Result, item 3; the key results of the JSON twin for these tags
- **Severity:** minor
- **Problem:** In 04-branch-fall, whose (4.16) is used, "leading order in $`\kappa`$" means that the body evolves by the effective body contract (8.19) of 04-ilang-time/08-maximal-speed, and the plain gradient $`-\kappa\langle X\rangle`$ of that contract is one of the first-order gradients. With it, $`\mathcal F_k=\gamma_1M_k^2-\kappa\langle X\rangle`$, and $`a_{k,\sigma}(0)`$ has the further term $`-\sigma\tau_k^2\kappa\langle X\rangle/\hat M_k`$, which depends on the level and is odd in the branch already at zeroth order in $`\epsilon_1`$. So "at first order in $`\epsilon_1`$ the fall from rest is level-independent in both branches", the equivalences (10.14), the defect (10.17) and the table hold as stated only for $`\langle X\rangle=0`$.
- **Fix:** Keep the term. State $`\langle X\rangle=0`$ as the condition under which (10.13), (10.14), (10.17), (10.20) and the two rows of the table hold as written, and give for $`\langle X\rangle\neq0`$ the additional term of $`a_{k,\sigma}(0)`$ and what it does to the statements (which of them fail, and the size of the term against $`\sigma\tau^2\gamma_1M_k`$ and against $`-\tau^2g`$).

### I3. A remark to the reviewer stands in the open issues
- **Location:** Open issues, first item ("whether it should be part of the regime of the question is for the main model")
- **Severity:** minor
- **Problem:** The third small number $`\epsilon_3`$ is needed: without it the two blocks of the contract are not separated. It is an assumption of this package in addition to the regime of the question, and it is stated as such in the Setup. The open issue, however, addresses the reviewer instead of stating this.
- **Fix:** State in the Setup and in the Result that the regime R1 with $`\epsilon_3\ll1`$ is a condition of every order estimate of this package, in addition to the two small numbers of the question, and that members of the class with $`\epsilon_3`$ not small are covered by the statements of R0 only. Reword or remove the open issue.

Everything else of v1 stays as it is, with the same tags: Step 1 with (10.1)–(10.7); Step 2 with (10.8)–(10.11) apart from the two sentences of I1; Step 3 with (10.12), (10.15), (10.16) and, apart from the condition of I2, (10.13), (10.14), (10.17); Step 4 with (10.18)–(10.20); the consistency checks. Checked for this review and found correct: (10.3), (10.4), the estimate (10.6), the Sylvester equation and $`H_{\rm eff}`$ of (10.8), $`H^{(2)}`$ of (10.9), the coefficient $`c_x`$ and $`H^{(3)}`$ of (10.10), the blocks (10.11), the level data (10.12), $`\beta`$ of (10.13), (10.14), (10.15), the rate $`\bar r`$ and the defect (10.17), and the exact on-site solution (10.19) with its expansion and the overlap.
