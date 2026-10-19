# External verification: 10-field-own-contract

- **Subproject:** 05-ilang-free-fall
- **Package:** 10-field-own-contract
- **Verified version:** v2
- **External round:** 1 of 2
- **Date:** 2026-10-11T14:17:49+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The compression, leading second-order on-site correction, and first hopping correction are largely consistent with the stated Schrieffer–Wolff construction. However, the corrected body contract is not necessarily in the positive-mass class claimed, even within the stated fast-field regime. The independent-cell fall calculation also covers only an additional linear-profile subclass, not the arbitrary cell data requested. Some accuracy and validity statements need narrower qualifications.

## Issues

### I1. Corrected on-site masses need not be positive
- **Location:** Step 2(b), Eq. (10.11), and Step 3(c)
- **Severity:** major
- **Problem:** Membership in $`\mathcal C_{\rm lev}`$ requires $`M_{x,k}>0`$, but R1 does not ensure
  ```math
  N(x)M_k+\gamma_x^{(3)}M_k^3>0.
  ```
  For example, take
  ```math
  C_f=\mathrm{diag}(0,\Delta),\qquad
  \varphi_0=|0\rangle,\qquad
  \Phi_x=\begin{pmatrix}n&v\\v&n+a\end{pmatrix},
  \quad a<0.
  ```
  Then $`N(x)=n>0`$, $`\gamma_x^{(3)}=av^2/\Delta^2<0`$, and all three perturbative parameters can be small. Nevertheless, choosing $`n<|a|v^2M_0^2/\Delta^2`$ makes the retained corrected mass negative on every level. Thus the claimed classification with first corrections is false for allowed members, and $`V_{x,k}+M_{x,k}`$ is then not the upper on-site eigenvalue.
- **Suggested fix:** Retain the unconditional classification only at leading order in $`\epsilon_2,\epsilon_3`$. For the corrected classification and “upper eigenvalue” interpretation, impose and state a positive-mass margin relative to the corrections and remainder; otherwise explicitly identify failure of the class condition.

### I2. Arbitrary cell data are replaced by linear cell profiles
- **Location:** Step 4(c), Eq. (10.20), and its control discussion
- **Severity:** major
- **Problem:** The question allows arbitrary positive $`\Delta_x`$ and arbitrary nonnegative $`\varepsilon_x`$. Step 4(c) instead assumes
  ```math
  \gamma_x=\gamma_0+\gamma_1x,\qquad \rho_{xx}=\rho_0+\rho_1x,
  ```
  an additional restriction not implied by $`n_x=1+gx`$. Without it, the effective scalar potential and hopping generally do not have the linear profiles required by (4.16), and the finite difference called $`\gamma_1`$ need not be constant. For instance, constant $`\Delta_x`$ and $`\varepsilon_x^2/\Delta_x=\gamma_0+\delta(-1)^x>0`$ are admissible but have alternating gradients. The assertion that any position dependence of $`\gamma_x`$ gives a nonzero single $`\gamma_1`$ and the stated drift acceleration is therefore unjustified.
- **Suggested fix:** State explicitly that (10.20) and the associated independence conditions apply only to linear, weakly varying cell profiles. Address the remaining cell descriptions separately, or explain why the quoted linear-profile drift result cannot settle their fall; do not present the linear calculation as covering every cell description in scope.

### I3. A sufficient gap criterion is presented as necessary
- **Location:** Setup and assumptions, A third number of the class; Regimes; final Open issues bullet
- **Severity:** minor
- **Problem:** Small $`\epsilon_3`$ and the R1 inequality are sufficient norm conditions for the stated perturbative construction, not necessary conditions for spectral separation or an effective description. Consequently, “without it the two diagonal blocks … are not separated” and “where … ≥1 … the expansion fails” are too strong. A sharp field remains exactly reducible even with arbitrarily large $`\nu`$; large excited-sector terms can also increase rather than close the relevant gap. Additionally, the stated limit $`\|\hat C-e_0\|\to\tau+N_{\max}M_{\max}`$ is an upper bound, not generally an equality.
- **Suggested fix:** Replace these claims by “separation is not guaranteed” and “the displayed norm-based expansion is not controlled.” Write the body norm estimate with ≤, and preserve the explicitly identified sharp-field exception.

### I4. Clock accuracy does not include the retained cubic correction
- **Location:** Step 3(c), Eqs. (10.15)–(10.16), and the clock row of Step 5
- **Severity:** minor
- **Problem:** Equation (10.15) retains the first $`\epsilon_3`$ correction, but the clock accuracy range in (10.16) controls only the quadratic term $`-\gamma_xM_k^2`$. It therefore supplies a leading-order-in-$`\epsilon_3`$ range, not a range for all terms retained in Step 3. This matters especially for an interior field eigenvalue: $`\gamma_x`$ can cancel to zero while $`\gamma_x^{(3)}\neq0`$, so the “all λ” case based on $`\gamma_x=0`$ does not survive the cubic correction for three or more levels. The independence of neighboring spacings is likewise assessed only after dropping that correction.
- **Suggested fix:** Qualify (10.16) and its summaries explicitly as leading order in $`\epsilon_2,\epsilon_3`$, with the quoted local-clock approximations. Add an order estimate for the cubic spectral-curvature error and state the spacing-independence conditions at the retained order, including cancellation cases.

## Focus points

None given.
