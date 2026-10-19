# External verification: 11-bound-pair

- **Subproject:** 05-ilang-free-fall
- **Package:** 11-bound-pair
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-11T14:04:36+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The fibre contract, the simple-eigenvalue derivative identities, and the leading upper-band bound-state formulas are largely correct, and the supplied numerical checks support those formulas in the tested regimes. However, the claims of contract-split invariance are inconsistent with M6, the treatment of degenerate bound levels does not cover the stated scope, and the clock calculation does not attain the first-order rate accuracy of the cited moving-clock formula. There are also two smaller errors concerning a subleading binding contribution and an exceptional total label.

## Issues

### I1. Incorrect claims of contract-split invariance
- **Location:** Step 2, Eqs. (11.3)–(11.4), and Result item 1
- **Severity:** major
- **Problem:** Even under the constant redistributions retained in Step 2, the table is inconsistent: $`M_i`$, defined as half a gap, remains unchanged while $`E_b`$ shifts by $`-(c_1+c_2)`$. Therefore the literal expression $`E_b(P)-(M_1+M_2)`$ is not invariant. The distance from the continuum edge is invariant under this redistribution, but that edge is no longer numerically $`M_1+M_2`$.

  More generally, M6 requires invariance under every allowed redistribution leaving total $`C`$ unchanged, not just those preserving the displayed record formula. For example, moving $`h\sigma^{(1)}_3`$ from $`C^{\rm D}_1`$ into the body–medium pair term preserves $`C`$, leaves $`U`$ finite-range, and does not change the centred record vectors. Nevertheless, the listed $`C_{\rm pair}`$, its rest coefficient, its bound eigenvectors, and generally its dispersion change. Consequently, the claimed invariance of quantities extracted from the listed $`C_{\rm pair}`$ has not been established.
- **Suggested fix:** Define the effective body operator invariantly from the total contract and the stated weak-record limit, accounting for body-only terms wherever they are listed. Define the binding-cost difference using a separately identified continuum-edge eigenvalue, rather than treating the invariant half-gaps as shifting reference costs. Reassess the well-definedness table under all M6 redistributions.

### I2. Degenerate bound levels are not covered
- **Location:** Setup and assumptions, Simple level; Steps 3–5, especially Eq. (11.9); Result scope
- **Severity:** major
- **Problem:** The question includes every bound level, whereas the derivation assumes simplicity and then claims that Eqs. (11.5)–(11.9) extend to each analytic branch of a degenerate level. In Eq. (11.9), removing only one eigenvector leaves the other vectors of the degenerate eigenspace in $`Q_P`$, so the stated inverse remains singular. Also, eigenvectors appropriate to branches under different parameter variations need not coincide; a single arbitrary vector in the degenerate eigenspace cannot generally supply all the asserted derivatives.
- **Suggested fix:** Treat degenerate levels using the full eigenspace projector, the reduced resolvent on its complement, and the appropriate effective perturbation matrices for each parameter direction. State the branch-selection conditions and distinguish the identities valid for arbitrary stationary eigenvectors from branch-dependent derivative formulas.

### I3. Clock formula omits the first-order correction to the rate
- **Location:** Step 10(a), Eq. (11.19), and Result item 5
- **Severity:** major
- **Problem:** Equation (11.19) retains only the energy term linear in $`d_k`$, giving a rate factor evaluated at $`M_i=m_i`$. This is a zeroth-order rate approximation, not the first-order rate accuracy exhibited by input (5.21). Generically, the quadratic dependence of the bound energy on $`M_i`$ produces the correction
  ```math
  \Gamma_i
  =\partial_{M_i}E_b(m_i)
  +\bar d_i\,\partial_{M_i}^{\,2}E_b(m_i)
  +O(d_{\max}^{\,2}),
  \qquad
  \bar d_i=\frac{\pi(N_i-1)}{N_i\lambda_{0,i}},
  ```
  with the other data held fixed. This correction is generally nonzero for a bound pair.

  The stated remainder does not resolve this omission: at clock-reading intervals $`\lambda\sim\lambda_{0,i}`$, its term $`\delta_i^2g_0\lambda`$ is of first order in $`\delta_i`$. Thus it permits an error precisely as large as the first-order clock-rate correction requested.
- **Suggested fix:** Include the mean-level correction, equivalently evaluating the energy derivative at the mean clock mass to the appropriate order, and justify the reading-distribution remainder on a stated range of $`\lambda/\lambda_{0,i}`$. Distinguish linear-order energy perturbation from first-order accuracy of the clock rate.

### I4. Wrong order for the contribution of w₂₂
- **Location:** Step 7, Other numbers
- **Severity:** minor
- **Problem:** The statement that $`w_{22}`$ enters this upper-band level at order $`\epsilon^4`$ is incorrect. The $`\lvert22\rangle`$ component first appears at order $`\epsilon^2`$, since reaching it requires two branch flips. Hence
  ```math
  \frac{\partial E_b}{\partial w_{22}}
  =|\psi_{22}(0)|^2=O(\epsilon^4).
  ```
  Since $`w_{22}=O(\epsilon^2)`$, its first possible contribution to the energy is generically $`O(\epsilon^6)`$, not $`O(\epsilon^4)`$.
- **Suggested fix:** Correct the stated order to $`\epsilon^6`$. Keep the overall $`O(\epsilon^4)`$ energy remainder, which receives other contributions.

### I5. Eigenvector formula is undefined at j = 0
- **Location:** Step 7, Eqs. (11.11)–(11.13), and Existence and number
- **Severity:** minor
- **Problem:** The derivation extends its result to every $`P\in(-\pi,\pi]`$, but when $`a_1=a_2`$ and $`P=\pm\pi/2`$, $`j(P)=0`$. Then $`\alpha(P)`$ is undefined and the displayed expression for $`\rho(P)`$ divides by zero. These are admissible exceptional members expressly requiring treatment under the question’s assumptions.
- **Suggested fix:** State the limiting eigenvector at $`j=0`$, which at leading order is supported at $`r=0`$ in branch $`\lvert11\rangle`$, or restrict the displayed eigenvector formula to the neighbourhood of $`P=0`$ actually requested.

## Focus points

None given.
