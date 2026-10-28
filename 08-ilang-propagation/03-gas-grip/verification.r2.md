# External verification: 03-gas-grip

- **Subproject:** 08-ilang-propagation
- **Package:** 03-gas-grip
- **Verified version:** v4
- **External round:** 2 of 3
- **Date:** 2026-10-24T19:57:07+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The affine characterization of grips admissible within pair terms is well supported, and most of the eigenvalue and weighing algebra is consistent with the quoted inputs. However, the claimed necessary-and-sufficient criterion for weighing the self-cost is false when the allowed grip fraction μ approaches zero; an admissible finite-ring example satisfies every stated smallness condition but contradicts the criterion. The large-size uniformity of several remainder estimates also remains insufficiently justified.

## Issues

### I1. False weighing criterion near μ = 0
- **Location:** Step 4, Eq. (3.8)(i), and its corresponding Result item
- **Severity:** major
- **Problem:** Equation (3.13) gives
  ```math
  w^{\rm self}-1=\frac{1+\zeta-\mu+O(\chi q)}{\mu}.
  ```
  Consequently, the asserted equivalence
  ```math
  w^{\rm self}=1+O(\chi q)
  \iff \mu=1+\zeta+O(\chi q)
  ```
  does not follow without additional bounds on μ. In particular, an $`O(\chi q)`$ uncertainty before division becomes $`O(\chi q/|\mu|)`$ afterwards. The stated regimes exclude neither small μ nor μ approaching zero.

  There is a concrete counterexample on the ring with $`L=4`$, $`r=2`$, and $`r'=1`$. Here
  ```math
  \ell_0=\frac5{16},\qquad T_2=\frac38,\qquad
  T_3=\frac7{128},\qquad \zeta=-1,\qquad q=\frac{69}{25}.
  ```
  Expanding the quoted cost and weight series gives
  ```math
  \frac{\Delta W-\Delta W^{(1)}}{\Omega C^{\rm self}}
  =\frac{26}{25}\chi+O(\chi^2)
  ```
  for $`g_b>0`$. Choose an admissible family of affine grips with
  ```math
  \alpha=\frac{nt_f}{M_k\ell_0}-n\beta,\qquad \beta>0,
  ```
  so that $`\mu=\chi`$. Then $`\chi q\to0`$, $`|\mu|\chi\to0`$, and the right-hand condition in (3.8)(i) holds, but
  ```math
  w^{\rm self}=\frac{26}{25}+O(\chi),
  ```
  not $`1+O(\chi q)`$. None of the listed cancellation exclusions removes this example.
- **Suggested fix:** Restrict the stated equivalence to a regime in which $`|\mu|`$ is bounded above and bounded away from zero, or retain the explicit $`1/\mu`$ error amplification and formulate a criterion with the accuracy actually available. For small μ, higher-order information is required to decide equality to the claimed tolerance.

### I2. Uniform remainder control is not established
- **Location:** Step 4, remainder estimates following Eq. (3.13); Step 5, Eq. (3.9); Open issues, second bullet
- **Severity:** minor
- **Problem:** The derivation bounds the displayed second- and third-order place-difference quotients using $`T_2`$, $`T_3`$, and $`q`$, but then uses $`\chi q\ll1`$ as a sufficient control condition for the complete relative expansions, including growing-size and distance limits. The Open issues section explicitly acknowledges that higher orders contain further place-difference quotients that have not been bounded. Fixed-graph analyticity justifies a Taylor remainder with graph-dependent constants; it does not by itself establish that $`q`$ controls those constants uniformly in the families used for the torus conclusions. This is an unresolved justification gap, rather than a demonstrated counterexample to the distance conclusions.
- **Suggested fix:** Either establish uniform bounds for the higher-order remainder on the stated graph families, or restrict the expansion claims to fixed finite graphs and state the additional control needed before taking size and distance limits.

## Focus points

None given.
