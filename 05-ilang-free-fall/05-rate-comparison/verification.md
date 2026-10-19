# External verification: 05-rate-comparison

- **Subproject:** 05-ilang-free-fall
- **Package:** 05-rate-comparison
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-10T22:27:08+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The derivation of the equivalence conditions and the classifications with all classes read is sound, including the treatment of pair-term admissibility and diagonal freedom. However, Step 10 turns the exact schedule re-timing identity into clock-rate claims that require unstated assumptions about functioning starts and constant, positive rates; those claims are not valid for the stated class of arbitrary body contracts. The treatment of the prescribed wide-start two-run protocol also needs clarification, and two smaller statements concerning diagonal generation and A8 are inaccurate.

## Issues

### I1. Unstated assumptions in the clock-rate transformation
- **Location:** Step 10(c), paragraphs following Eq. (5.21)
- **Severity:** major
- **Problem:** Equation (5.21) correctly establishes equality of schedule statistics at corresponding re-timed arguments. It does not imply the stated equal-λ rate ratio $`(r_1/r_2)(a_2/a_1)`$ for arbitrary $`C_1,C_2`$ and every start. If an operational clock advance has an instantaneous rate $`r_i(\lambda)`$, the transformation is
  ```math
  r_i^{C'}(\lambda')=\frac1{a_i}r_i^C(\lambda'/a_i),
  ```
  so pairing readings at the same numerical $`\lambda'`$ gives
  ```math
  \frac{r_1^{C'}(\lambda')}{r_2^{C'}(\lambda')}
  =\frac{a_2}{a_1}
  \frac{r_1^C(\lambda'/a_1)}{r_2^C(\lambda'/a_2)}.
  ```
  The simplified formula requires constant rates. Moreover, arbitrary body contracts and arbitrary starts need not supply a readable, nonzero clock rate at all. Consequently, the claims that every positive ratio occurs and that the rate ratio is invariant exactly in row 2 of Eq. (5.19) are not established over the stated scope.
- **Suggested fix:** Keep Eq. (5.21) as the exact general result. State the operational definition of rate and its start dependence, use the argument-dependent transformation above, and restrict the simplified ratio and “every positive number” statements to functioning clocks with constant positive rates in a stated regime.

### I2. The no-hopping two-run argument uses different starts
- **Location:** Step 9(b), Eq. (5.17), and Open issues
- **Severity:** minor
- **Problem:** The prescribed starts $`S_{\rm clock}(x_i)`$ have support over many positions; they are not starts inside the single block $`x_i`$. Conservation of $`P_x`$ at $`\tau=0`$ therefore does not give $`p^C_\lambda=p^{C'}_{a_{x_i}\lambda}`$ for these starts. Their clock statistics are mixtures of the contributions from all occupied blocks, generally re-timed by different factors. The parameter transformation of $`\eta_{x_1}/\eta_{x_2}`$, and the flat-profile control (5.13), do establish parameter non-invariance, but the operational argument presented for the actual wide-start protocol is incomplete. The quoted rate formulas also carry gradient and level-spacing approximations that are not retained explicitly in Step 9.
- **Suggested fix:** Apply the flat-profile control to the actual wide starts, accounting for the position mixture, and state the approximation orders inherited from Eqs. (3.23), (3.24), and (3.36). Separate the exact transformation of profile parameters from the asymptotic interpretation as a measured rate ratio.

### I3. Equal-λ comparisons still rely on A8
- **Location:** Step 9, paragraph “What the comparison is (A8)”
- **Severity:** minor
- **Problem:** The derivation says that the two-run comparison does not use the order of λ and cites A8’s third bullet. That bullet expressly says that a comparison of readings taken at equal λ uses the order of λ. The absence of a joint schedule correctly distinguishes this protocol from two events in one evolution, but it does not remove its reliance on the externally specified equal-λ pairing across runs.
- **Suggested fix:** State that the comparison is not a joint-schedule statistic but nevertheless relies on the shared equal-λ prescription of A8, measured from the respective starts. Remove the contrary assertion about A8’s third bullet.

### I4. Unread classes do not necessarily prevent diagonal generation
- **Location:** Step 1, paragraph (G)
- **Severity:** minor
- **Problem:** “If some class is not read, (G) fails” is too strong. For example, if an object has two singleton blocks and one is read, its projector and the identity already generate the projector of the unread block by complementation. With the other objects fully read, all joint-place diagonal operators are still generated. What fails in general is the guarantee of diagonal generation, not generation itself.
- **Suggested fix:** Replace this statement by “If some classes are not read, (G) is not guaranteed and is not assumed below.” This correction does not affect the subsequent conservative necessary/sufficient treatment.

## Focus points

None given.
