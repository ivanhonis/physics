# External verification: 07-limits

- **Subproject:** 05-ilang-free-fall
- **Package:** 07-limits
- **Verified version:** v3
- **External round:** 2 of 2
- **Date:** 2026-10-11T11:14:44+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The exact level mixture, the drift-acceleration conditions, and the first-order treatment of centered record fluctuations are largely sound. However, the derivation explicitly leaves substantial parts of items 1(f) and 2(c)–(d) unresolved, despite their inclusion in the requested scope. The replacement of the record-induced acceleration by selected secular terms does not answer the sharp-label acceleration question, and several smaller issues concern conventions, bounds, and approximation regimes.

## Issues

### I1. The requested coherence result remains incomplete
- **Location:** Step 5, parts 3, 7 and 8; Result, item 1(f); Open issues
- **Severity:** major
- **Problem:** The question covers every smooth $`g`$, including all starts at rest, and asks for the order and leading dependence of the modulus deviation. The derivation provides the complete first-order functional, but leaves the second-order result unresolved for every start except the real Gaussian class E1. Thus, for many permitted starts—including definite-parity starts—it establishes only the absence of a first-order term, not the first nonvanishing order or its requested dependence on position spread. Moreover, the estimate (7.32), used to justify the Gaussian result, includes second-order amplitudes and mixed contributions whose scaling is asserted without a supporting calculation. Calling these results “order estimates” does not by itself justify them.
- **Suggested fix:** Supply the general second-order perturbative functional and sufficient physicist-formal estimates to determine the requested order and spread dependence in the stated class. For (7.32), give a short calculation supporting the scaling of the uncomputed second-order and mixed contributions; a rigorous bound is not required.

### I2. Secular acceleration does not replace the requested sharp-label acceleration
- **Location:** Step 8, parts 1–3; Eqs. (7.15)–(7.18) and (7.34); Result, items 2(c) and 2(d)
- **Severity:** major
- **Problem:** The derivation restricts its answer to derivatives of selected secular velocity terms, rather than determining the acceleration requested for a sharp label. This distinction changes both the leading behavior and the level-independence conditions. For example, differentiating the last term of (7.13) produces the sharp-label contribution
  ```math
  \kappa^2\sigma_X^2\,\sigma\omega\,\theta'^2\omega'\lambda^2
  \sin(2\omega\lambda),
  ```
  in addition to other oscillatory terms. It is not contained in (7.15), is not smaller pointwise than the secular acceleration, and depends on the level through its oscillation frequency even when $`\tau_k/M_k`$ is common. The derivation acknowledges this unresolved behavior. Item 2(d) likewise receives only necessary comparisons for selected terms, not a controlled range giving the requested relative accuracy at the retained record orders.
- **Suggested fix:** Determine the acceleration from the complete second-order coefficient (7.13), and provide the corresponding third-order result or an adequate remainder estimate. If window averaging is used, specify the averaging and sharp-label limits and control the retained remainders sufficiently to establish the stated accuracy range; distinguish its level-independence conditions from those of the secular coefficient alone.

### I3. The periodic uncertainty inequality is incorrect
- **Location:** Step 7, part 4; Step 8, part 1, following Eq. (7.33)
- **Severity:** minor
- **Problem:** The repeatedly used inequality $`X_g\ge 1/(2\delta p)`$ is not valid for every smooth periodic $`g`$. The permitted choice $`g=1`$ has $`X_g=0`$ and, on the rest arc, $`\delta p^2=\pi^2/3`$. Integration by parts actually gives
  ```math
  2\delta p\,X_g\ge \left|1-|g(\pi)|^2\right|,
  ```
  with the boundary term already recognized elsewhere in this derivation. Consequently, the displayed universal lower bound on $`c_1[g]`$ is false. Also, $`X_g/\Lambda\to0`$ is a sufficient condition furnished by the bound, not a demonstrated necessary condition for combining the limits.
- **Suggested fix:** Retain the boundary term in the uncertainty inequality, or use an explicitly asymptotic narrow-packet bound justified with a periodic test function. Describe the window condition as sufficient unless necessity is independently established.

### I4. The effective-contract convention is inconsistent in the exact total contract
- **Location:** Setup and assumptions; Step 1, part 1; Step 6
- **Severity:** minor
- **Problem:** The setting says that the blocks $`C^{(k)}`$ contain the effective profiles, including $`\kappa x\langle X\rangle`$. Nevertheless, Step 1 writes the total contract using those blocks plus $`\kappa\hat x\otimes X`$. Taken literally, this counts the mean record term twice. Step 6 instead uses the intended centered fluctuation $`\kappa(X-\langle X\rangle)`$. Level conservation and the mixture identity survive either convention, but the identification of the gradients and the first-order record cancellation does not.
- **Suggested fix:** With effective blocks, write the exact total contract using $`\kappa\hat x\otimes(X-\langle X\rangle\mathbb 1)`$. Alternatively, distinguish the bare and effective blocks throughout.

### I5. The level-specific speed bound is not the quoted full maximal-speed formula
- **Location:** Step 8, part 3; Eq. (7.17); Open issues
- **Severity:** minor
- **Problem:** The substitution $`v_{\max,k}=\tau_kd_0`$ is not established by the quoted (5.11), whose hopping is diagonal and identical in the clock label. With level-dependent $`\tau_k`$, the hopping operator in the specified clock place basis contains
  ```math
  T_{\rm clock}=\sum_k\tau_k|f_k\rangle\langle f_k|,
  ```
  which generally has off-diagonal clock-place matrix elements. The full place-basis row-sum bound therefore need not equal a particular $`\tau_kd_0`$. A bound restricted to one conserved level can still be obtained, but it is a different statement requiring justification.
- **Suggested fix:** Derive the level-restricted bound directly from the velocity operator, and distinguish it from the maximal-speed bound for the complete body contract in the original place basis.

### I6. The small-velocity and background formulas need a near-rest regime
- **Location:** Step 8, part 1, Eq. (7.15); Step 8, part 3, Eq. (7.17)
- **Severity:** minor
- **Problem:** The expansion
  ```math
  \delta a^{(2)}
  =-\kappa^2\sigma_X^2\lambda
  \left(4+3\tau_k^2/M_k^2\right)v+O(v^3)
  ```
  requires expansion about $`p_0=0`$, not merely small $`v`$. Small velocity also occurs near $`p_0=\pi/2`$, where the coefficient instead approaches
  ```math
  4-\frac{3\tau_k^2}{M_k^2+\tau_k^2}.
  ```
  The setup permits arbitrary $`p_0`$, but this restriction is not stated alongside (7.15). Equation (7.17) then displays the near-rest second-order term together with the rest value of the third-order term as an equality, without marking the omitted velocity-dependent terms.
- **Suggested fix:** State the near-$`p_0=0`$ regime explicitly, including the required small-label conditions, and display the omitted velocity orders in (7.17). Retain the exact $`p_0`$-dependent expression when discussing arbitrary labels.

## Focus points

None given.
