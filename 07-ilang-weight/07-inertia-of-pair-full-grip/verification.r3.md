# External verification: 07-inertia-of-pair-full-grip

- **Subproject:** 07-ilang-weight
- **Package:** 07-inertia-of-pair-full-grip
- **Verified version:** v3
- **External round:** 3 of 3
- **Date:** 2026-10-22T00:43:52+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The second-order gap calculation gives a plausible mechanism for the mutual term to enter both bodies’ local inertias, and the numerical sector calculations support much of that calculation. However, the cost comparison has an incorrect remainder in the explicitly included small-width regime, and the fixed-source fall calculation depends on locality and moment estimates that are not established. The required exact fixed-source eigenvalue check in the mutual-term-dominated regime is also missing. Consequently, the package does not yet establish all its stated inertia–cost and weight–inertia conclusions over the claimed class.

## Issues

### I1. Cost comparison drops a finite bond-average correction
- **Location:** Step 4, derivation preceding Eq. (7.7), and Eq. (7.7)
- **Severity:** major
- **Problem:** The replacement
  ```math
  \frac{\sum_\rho b_0(\rho)\bar B(\rho)}{\beta_0}
  =\langle M\rangle_0+O(\eta|B(0)|,\ |F|w)
  ```
  is incorrect for $`w\ll1`$, which is explicitly included in S4 and in the claimed validity of (7.7). In the even-relative-position class, as $`w\to0`$, $`f_0`$ concentrates at $`r=0`$, while the normalized bond weights concentrate at $`\rho=\pm1`$. Consequently,
  ```math
  \langle M\rangle_0\longrightarrow B(0)[1+O(\eta)],
  \qquad
  \frac{\sum b_0\bar B}{\beta_0}\longrightarrow
  \bar B(1)=B(0)+F\left(1-\frac{3}{2L}\right).
  ```
  The discrepancy is $`O(F)`$, not $`O(Fw)`$. Thus (7.7) omits a correction of relative order $`1/L`$ to its mark contribution; this is not covered by its stated $`O(\eta+w/L+\tau^2/d^2)`$ remainder at fixed $`L`$. Step 3 correctly used $`\max(w,1)/L`$, but Step 4 loses that qualification.
- **Suggested fix:** Retain the bond-weighted $`\bar B`$ in the general cost comparison, or use an error involving $`\max(w,1)/L`$ and delimit when it is small. Restrict the replacement by $`\langle M\rangle_0`$ with the stated $`w/L`$ accuracy to the broad-pair regime.

### I2. Odd-parity extension has different tight-binding asymptotics
- **Location:** Step 2, paragraph beginning “Group and distances,” and final paragraph on the bound level
- **Severity:** minor
- **Problem:** The statement that “everything below holds for either” relative-position parity conflicts with the subsequent small-$`w`$ asymptotics. In the odd-relative-position class, the coincident binding minimum is replaced by the two degenerate sites $`r=\pm1`$. As the hopping tends to zero, the selected symmetric extreme state has weight $`1/2`$ on each site, giving $`\beta_0\to1/2`$, not $`\beta_0=O(w^3)`$. Its mean potential displacement from $`B(0)`$ is also $`O(F)`$, rather than $`O(Fw)`$. These distinctions matter because the package includes narrow pairs and claims validity for either parity class.
- **Suggested fix:** State the narrow-pair asymptotics separately for the two parity classes, and amend the width and potential-average estimates accordingly. Alternatively, explicitly restrict the affected statements and starts to the even-relative-position class.

### I3. Fixed-source reduction lacks the quantitative estimates needed for the fall result
- **Location:** Step 5, “Fixed source and centre contract,” “Relation to the internal density,” and Eq. (7.15)
- **Severity:** major
- **Problem:** The projected source matrix in (7.14) is a valid first-order construction under an appropriate spectral-gap condition, but the subsequent reduction to the midpoint-conditioned density is not established with the quoted errors. Smoothness of $`u_P`$ alone does not imply that its Fourier kernel $`G(a;k)`$ has “a range of a few places,” nor does it supply the componentwise first- and second-moment bounds used in (7.15). Even the constant-hop relative problem has a momentum-dependent internal phase whose derivative scales with the pair width; eigenvector derivatives can additionally involve the small relative-level gap. The overlap phase condition fixes a total first moment at $`P=0`$, not the required componentwise bounds. Likewise, the assertion that the remaining source operator changes the acceleration only by $`O(w^2/w_X^2)`$ is not derived for this nonlocal projected operator or related explicitly to the physical midpoint observable. Finally, $`w_X\gg w`$ alone does not make that error smaller than the mutual-order effect being compared.
- **Suggested fix:** Establish quantitative kernel-moment or eigenvector-derivative estimates, including their dependence on $`w`$, the relative gap, and unequal body parameters, and use them to justify (7.15). Derive the acceleration for the projected physical position observable and state a start-width hierarchy that places its errors below the retained mutual-order contribution. The numerical agreement at the sampled parameters can support, but cannot replace, these estimates.

### I4. Required exact fixed-source check in regime S5 is absent
- **Location:** Code section; check_fixed_source.py; output/fixed_source_bandS1.txt and output/fixed_source_bandS2.txt
- **Severity:** major
- **Problem:** The question requires item 4 to be checked against exact eigenvalues with a held source, including a case in the regime of item 3(ii). The full laboratory-space exact eigenvalue tests are only at $`L=12,16`$, and no S5 diagnostic is supplied for those cases. The designated S5 cases S1 and S2 instead diagonalize the second-order band contract with the source. Their exact full-contract calculations concern the source-free $`P=0`$ density or the explicitly auxiliary midpoint-following probe, not eigenvalues with a fixed held source. Thus the supplied checks do not meet the stated requirement. Agreement with (7.14) constructed from exact matrix elements verifies first-order projection, but does not independently validate the analytic reduction to (7.12).
- **Suggested fix:** Supply an exact full-contract fixed-source eigenvalue check for a parameter set demonstrably satisfying the stated S5 hierarchy, and compare the mutual-order weight/fall prediction with that check. Clearly distinguish that result from band-contract diagonalization and auxiliary-probe tests.

## Focus points

None given.
