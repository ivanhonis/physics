# External verification: 06-inertia-of-pair

- **Subproject:** 07-ilang-weight
- **Package:** 06-inertia-of-pair
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-21T08:33:18+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The relative-chain construction and the curvature formula (6.6) are sound for an isolated, nondegenerate relative level, and the supplied numerical results support that formula in the tested cases. However, several conclusions are extended beyond what is derived: the field-hopping restriction is not necessary, some branch-dependent signs are lost, and coefficient mismatches are incorrectly used to exclude individual inertia–cost equalities. The source projection also requires additional justification before its stated first-order accuracy and error estimates can be accepted.

## Issues

### I1. The upper bound on field hopping is not necessary

- **Location:** Step 7, Eq. (6.15), and Open issues
- **Severity:** major
- **Problem:** The assertion that R1 requires $`4N_ft_f<2M_i-\delta_1`$ for a positive-branch body is false for the finite-ring descriptions under consideration. The field excitation energies are discrete. Their extending above $`2M_i`$ does not imply that any excitation lies close to the branch-flip energy. For example, with $`N_f=1`$, sufficiently large $`t_f`$ makes the first nonzero field excitation $`4t_f\sin^2(\pi/L)`$ exceed all relevant branch-energy differences; the zero-excitation branch-flip levels remain separated as well. Small couplings and sufficiently small motion terms can then satisfy R1 despite violating the proposed upper bound.
- **Suggested fix:** Present this inequality only as a sufficient condition avoiding crossings throughout the field excitation bandwidth. Determine the actual allowed ranges from the distances between the finite held-sector spectra, and revise the claimed $`t_f`$ window accordingly. Likewise, identify $`\delta`$ with the relevant minimum spectral distance rather than automatically with the field gap.

### I2. Branch-dependent signs and excited-level nodes are omitted

- **Location:** Step 2, Eq. (6.3); Steps 4 and 7; Consistency checks 2 and 3
- **Severity:** major
- **Problem:** Several statements valid for the nonalternating extreme level are asserted for the whole stated class. For the extreme contact-localized level, weak binding gives
  ```math
  \beta_0\simeq s_\beta\left[1-\frac{a_0}{6}(4\chi^2)^{1/3}\right],
  \qquad
  s_\beta=\mathrm{sgn}\!\left[g_1g_2(\mu_1^{-1}+\mu_2^{-1})\right],
  ```
  not always the positive expression used in Step 7. For example, two positive-branch bodies with $`g_1g_2<0`$ have a highest, alternating contact-localized level, for which $`\beta_0\to-1`$. Its inertia therefore approaches $`-(\mu_1+\mu_2)`$, not $`\mu_1+\mu_2`$, in the stated uniform-hopping line approximation. Thus the unbound consistency check and the general claim that increasing $`t_f`$ brings the pair toward its parts are incorrect for this branch choice. Also, Perron–Frobenius establishes the one-sign property only for the appropriate extreme eigenvector; excited relative levels have nodes even when the sign condition in (6.3) holds. The even-sector tight-binding curvature quoted in consistency check 3 similarly needs the spectral-edge sign.
- **Suggested fix:** Retain $`s_\beta`$ in the weak-binding and limiting formulas, restrict the one-sign assertion to the extreme level, and state separately the results for relative excited levels and alternating extreme levels.

### I3. The first-order source projection freezes a momentum-dependent internal state

- **Location:** Step 6, Eqs. (6.11)–(6.13); code/check_weight.py
- **Severity:** major
- **Problem:** The bound relative eigenvector generally depends on $`P`$, both through the bond phases and through $`\lvert t(P)\rvert`$. Projection onto the actual bound band therefore gives source matrix elements involving
  ```math
  f_{\nu,P'}(r)^*f_{\nu,P}(r),
  ```
  rather than $`f_{\nu,0}(r)^2`$ for every pair of momenta. Consequently, the projected contract is not generally $`E_b(\hat P)+W_\nu(\hat X)+O(g_s^2)`$ with (6.11). The omitted terms can be linear in $`g_s`$; they are not automatically $`O(\tau^4\gamma g_s)`$. A narrow-momentum, slowly varying source approximation may recover the leading fall factor, but its additional errors have not been derived. The code tests the frozen-profile model itself and therefore does not resolve this projection gap. Its good agreement for the main spacing also does not establish the asserted accuracy for the much smaller doublet splittings.
- **Suggested fix:** Project the source using the momentum-dependent bound eigenvectors. Then derive the narrow-momentum and spatial-gradient approximation leading to (6.11)–(6.13), including its errors. Distinguish numerical support for the leading main spacing from verification of the complete first-order projected contract.

### I4. Coefficient mismatches do not exclude equality for individual descriptions

- **Location:** Step 5, Eq. (6.10), and Result (6.10)
- **Severity:** major
- **Problem:** Different coefficients of $`K_\nu`$, $`M(0)`$, and the relative-potential averages rule out a parameter-independent identity, but they do not prove that the complete expressions cannot coincide for a particular description or relative level. Contributions with different coefficients can cancel. Accordingly, “no control in the class” and the unrestricted assertion that “no single speed fits” are not established by this argument. The proposed variation over all $`L`$ is also uncontrolled: at fixed couplings, $`\eta\sim |g|L/t_f`$ grows, while the field gap shrinks, eventually invalidating the perturbative expansion and regime R.
- **Suggested fix:** Restrict the conclusion to the demonstrated failure of a universal identity. Separately establish whether individual equalities are excluded or possible within R and B, and distinguish a universal speed fixed by the contracts from a level-dependent fitted ratio.

### I5. The finite-ring error is not controlled at the claimed mark order

- **Location:** Steps 3–6, Eqs. (6.6)–(6.14), and Open issues
- **Severity:** minor
- **Problem:** The derivation acknowledges that the finite-ring curvature depends on the continuation convention, then drops the ring term when giving the inertia and fall comparisons. B1 alone does not make that error smaller than the retained $`O(\varepsilon^2)`$ mark contribution. At fixed $`\chi`$ and $`L`$, the ring correction need not decrease as $`\varepsilon^2`$ does. Indeed, the supplied ring corrections of approximately 3–12% exceed the displayed mark corrections substantially. Moreover, an actual $`L\to\infty`$ limit at fixed listed parameters does not automatically preserve R or the weak-source expansion.
- **Suggested fix:** Include the ring remainder in the comparison formulas and impose a hierarchy making it smaller than any retained mark-order effect. If using a joint large-ring limit, specify the parameter scaling that preserves R, binding, and perturbative control. State explicitly the accuracy to which the resulting inertia is convention-independent.

### I6. The fall factor has the wrong stated dimension

- **Location:** Consistency check 1
- **Severity:** minor
- **Problem:** Since $`P`$ and the position labels are dimensionless, $`E_b''`$ and $`W_\nu'`$ both have dimension $`[C]`$. Thus
  ```math
  \Pi_\nu=E_b''W_\nu'
  ```
  has dimension $`[C]^2`$, not $`[C]`$. This is also the dimension of acceleration with respect to $`\lambda`$.
- **Suggested fix:** Correct the dimensional statement for $`\Pi_\nu`$ and $`\Pi_i`$.

### I7. Set A does not have equal speeds for coupling (c)

- **Location:** Code summary for check_inertia.py and parameter set A
- **Severity:** minor
- **Problem:** Set A has equal $`\tau_i`$, but for coupling (c)
  ```math
  c_1=0.2(1+0.09/L),\qquad c_2=0.2(1+0.07/L),
  ```
  so its speeds are unequal. The numerical summary nevertheless labels set A as the equal-speed case without restricting that statement to coupling (a).
- **Suggested fix:** Correct the label. If the numerical check is intended to test the equal-speed condition for coupling (c), adjust the motion parameters to satisfy that condition exactly.

## Focus points

None given.
