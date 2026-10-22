# External verification: 04-weight-of-bond

- **Subproject:** 07-ilang-weight
- **Package:** 04-weight-of-bond
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-20T23:03:31+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The one-field-object reduction and the second- and third-order perturbative coefficients are correct, and they support most of the qualitative comparisons. However, the claimed η-controlled regime beyond the explicit spectral-gap convergence bound is not established by the argument given, which contains a false bound. Several relative-error statements also need noncancellation conditions, the exact ring formula has inconsistent finite-step conventions, and the required exact-eigenvalue distance-scaling check is incomplete.

## Issues

### I1. Invalid justification of the η-controlled regime
- **Location:** Setup and assumptions, Regime; Step 2; Result, first bullet
- **Severity:** major
- **Problem:** The stated spectral-gap condition justifies ordinary perturbation theory, but the argument extending its control to all configurations with $`\eta\ll1`$ is invalid. In particular, the factor
  ```math
  \frac{g\,\ell^{(2)}_{ab}}{t_f\mathcal X\,\ell_{ab}}
  ```
  is not uniformly $`O(\eta)`$: $`\ell_{ab}`$ can vanish while $`\ell^{(2)}_{ab}`$ does not. On the allowed ring with $`L=5`$, for example, $`\ell(1)=0`$, whereas $`\ell^{(2)}(1)=1/25`$. The diagonal inequality quoted afterward does not bound this quotient. Consequently, the argument does not establish the claimed uniform remainder estimates outside the spectral-gap bound, particularly in the large-$`L`$ limits used later. The finite numerical tests cannot establish that uniform control.
- **Suggested fix:** Establish an absolute, finite-rank resolvent or perturbation bound controlled by η, without dividing by individual kernel entries. Alternatively, restrict the conclusions to the stated spectral-gap-controlled regime and explicitly delimit any dependence of remainder constants on $`L`$, positions and separations.

### I2. Relative remainders are asserted at zeros of retained coefficients
- **Location:** Steps 3–4 and 6, Eqs. (4.2), (4.5), (4.6) and (4.10)
- **Severity:** minor
- **Problem:** The multiplicative remainder statements require noncancellation conditions that are not supplied. Most explicitly, Eq. (4.10) excludes zero denominator factors but does not exclude $`\rho_0=0`$. Such configurations occur within the stated class: on an even ring with $`r'=r-1`$, choosing $`d_1+r=L/2`$ gives $`w=1/2`$, hence $`\rho_0=0`$, while the denominator can remain nonzero. The assertion $`\rho=\rho_0(1+O(\eta))`$ then incorrectly requires the exact ratio to vanish, rather than allowing a higher-order contribution. Analogous qualifications are needed for relative errors in profiles or weights whose retained coefficients vanish or nearly cancel.
- **Suggested fix:** State additive remainder bounds first. Convert them to relative bounds only where the relevant retained coefficients and ratio denominators have suitable lower bounds; treat vanishing leading coefficients separately.

### I3. Place-independent total eigenvalues are still fixed by the total contract
- **Location:** Step 3, paragraph beginning “Not fixed by one total contract”
- **Severity:** minor
- **Problem:** The claim that the $`\mathbf r`$-independent part of $`E`$ is not fixed by one total contract is incorrect. A specified total $`C`$ fixes its sector eigenvalues, including their place-independent contributions, and A5 redistributions leave them unchanged. What is not fixed by the bond profile alone is its additive normalization; what is convention-dependent is the allocation of total cost to rest terms, own marks and individual contracts.
- **Suggested fix:** Distinguish information unavailable from the profile alone from quantities not fixed by the total contract. Retain the convention warning for the allocation into contributions, not for the total sector eigenvalue.

### I4. Exact ring ratio uses inconsistent finite-step coordinates
- **Location:** Step 6, Eq. (4.12) and its definition of u and v
- **Severity:** minor
- **Problem:** The displayed ratio is claimed for unit lattice steps, but its accompanying definitions $`u=d_1/L`$ and $`v=r/L`$ are not the finite-step definitions used by the code. The exact lattice expression requires
  ```math
  u=\frac{d_1+1/2}{L},\qquad v=\frac{r-1/2}{L}.
  ```
  For the supplied $`L=30,d_1=6,r=3`$ configuration, the unshifted definitions give $`1.16667`$, whereas the exact lattice result is $`1.18588`$. The later code discussion acknowledges the shifts but leaves the main formula inconsistent.
- **Suggested fix:** Use the half-step-shifted definitions in Eq. (4.12), and identify the unshifted expression separately as a continuum or large-$`L`$ approximation.

### I5. Required exact-eigenvalue distance-scaling validation is missing
- **Location:** Code section; check_weight_of_bond.py, run_exact and large-graph distance tests
- **Severity:** minor
- **Problem:** The exact diagonalizations provide the required graph families, sizes and internal-state choices, and test coupling scaling. However, the distance sweeps for κ and its midpoint counterpart evaluate $`S`$ and the lattice kernels directly; they do not compare against exact lowest-eigenvalue differences. Thus they check the distance behaviour of the leading perturbative formulas, not the distance scaling of their deviation from exact eigenvalues, as required by the question.
- **Suggested fix:** Add distance sweeps using exact eigenvalue differences on each graph family, with couplings and source differentiation sufficiently controlled to distinguish distance dependence from higher-coupling and finite-source-step errors.

## Focus points

None given.
