# External verification: 06-inertia-internal-energy

- **Subproject:** 04-ilang-time
- **Package:** 06-inertia-internal-energy
- **Verified version:** v2
- **External round:** 2 of 2
- **Date:** 2026-10-10T13:22:50+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The edge-cost calculations, the responses at λ = 0, and the leading linear averaged inverse inertia for Model D are correct. The distinction between uniform and position-dependent on-site blocks is also substantively correct, and body E supplies a valid counterexample to unrestricted clock independence. However, the finite-force averaging remainder is not valid uniformly over the stated interval regime: it omits accumulated interbranch phase drift when the averaging interval starts sufficiently late. There is also a minor overstatement concerning factorization of the internal state.

## Issues

### I1. Averaging remainder misses accumulated interbranch phase drift
- **Location:** Step 5e, Eqs. (6.14) and (6.19)
- **Severity:** major
- **Problem:** The claimed bound $`R=O(T^2(1+\tau^2/M_k^2)\sum_\xi w_\xi|\mathcal F_\xi|^3)`$ does not follow from the stated adiabatic estimate and is false uniformly for the allowed intervals. Already for the single-force evolution, the interbranch phase is
  ```math
  \Phi(\lambda)=2M_k\lambda+
  \frac{\tau^2\mathcal F^2\lambda^3}{3M_k}+\cdots .
  ```
  The velocity contains the oscillatory contribution
  ```math
  -\frac{\tau^2\mathcal F}{2M_k^2}\sin\Phi(\lambda).
  ```
  Expanding this contribution to cubic order produces a term in the normalized averaged remainder
  ```math
  -\frac{\tau^2\mathcal F^3}{6M_k^2\Lambda}
  \left[T^3\cos(2M_kT)-\lambda_1^3\cos(2M_k\lambda_1)\right].
  ```
  This secular term can also be obtained directly by expanding the two-level equations. For $`\lambda_1\gg\Lambda`$, suitable endpoint phases make its size $`O(|\mathcal F|^3T^3/\Lambda)`$, rather than the asserted $`O(|\mathcal F|^3T^2)`$. Both conditions in (6.14) can hold in this situation. Real branch eigenvectors eliminate the Berry connection, not this dynamical-phase correction. The exact fixed-interval linear coefficient and the leading result (6.15) remain unaffected.
- **Suggested fix:** Retain the exact linear averaged coefficient, but replace the finite-force remainder by an estimate that controls the accumulated phase and endpoint contributions. Alternatively, restrict the averaging intervals, for example by requiring $`\lambda_1=O(\Lambda)`$, and justify the remainder under that additional restriction. Express record-induced force-independent contributions additively rather than through $`R/\mathcal F`$.

### I2. Non-scalar on-site differences do not necessarily prevent factorization
- **Location:** Step 6c, paragraph beginning “Otherwise”
- **Severity:** minor
- **Problem:** The statement that otherwise “the internal state does not factor from the position” is too strong. Non-scalar differences between the $`T_{xx}`$ do not necessarily entangle position and clock. If the blocks have a common eigenvector $`\eta`$, a start $`\phi_X\otimes\eta`$ remains factorized, with position evolving under the corresponding scalar site potential. Body E at a fixed clock level is itself an example: its clock vector $`\lvert f_k\rangle`$ remains unchanged, although its position response depends on $`k`$. Thus clock-level dependence need not arise through loss of factorization.
- **Suggested fix:** Qualify the claim as a generic possibility for arbitrary internal starts, rather than a necessary consequence of non-scalar on-site differences. Distinguish position–clock entanglement from clock-level-dependent scalar position dynamics.

## Focus points

None given.
