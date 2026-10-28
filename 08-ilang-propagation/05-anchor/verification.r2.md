# External verification: 05-anchor

- **Subproject:** 08-ilang-propagation
- **Package:** 05-anchor
- **Verified version:** v2
- **External round:** 2 of 3
- **Date:** 2026-10-25T08:56:17+01:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The finite-volume quadratic reduction, existence criteria, anchored Green function, and second-order cost and weight formulas are sound, and the supplied code supports those formulas. However, the general necessary-and-sufficient limiting criterion stated for the bond correction is false: its numerator and its denominator involve different image differences, which cannot be interchanged without an additional condition. The restricted sufficient families (A) and (B) avoid this problem, but they do not justify the broader claim in Step 8 and Result 14. There is also a minor ambiguity in the zero-anchor consistency check.

## Issues

### I1. Incorrect limiting equivalence for the bond correction
- **Location:** Step 8, discussion following Eq. (5.27); Result 14
- **Severity:** major
- **Problem:** Write
  ```math
  N=\Delta g_h(x_1)+\Delta g_h(x_2),\qquad
  D=\Delta g_s(\bar x),\qquad H=\Delta g_h(\bar x).
  ```
  Equation (5.27) makes $`a_{\rm bond}`$ proportional to $`N/(D-H)`$, with a prefactor bounded away from zero and infinity. The derivation nevertheless asserts
  ```math
  a_{\rm bond}\to0\quad\Longleftrightarrow\quad N/D\to0.
  ```
  Unlike the one-body case, $`N`$ is not the image difference $`H`$ appearing in the denominator, so this equivalence does not follow and is false.

  An admissible counterexample after $`L\to\infty`$ is obtained with anchor $`h=0`$, source $`x_s=e_x`$, pair placements
  ```math
  x_{1,2}=(d,\pm t,0),\qquad
  x'_{1,2}=(d+1,\pm t,0),
  ```
  where $`d=n^3`$ and $`t=n^4`$. Put $`A_*=1/(4\pi\kappa_h)`$. The lattice Green-function asymptotics give
  ```math
  D\sim A_*d^{-2},\qquad
  D-H\sim2A_*d^{-3},\qquad
  N\sim2A_*d/t^3=2A_*d^{-3}.
  ```
  Consequently $`N/D\to0`$, but $`N/(D-H)\to1`$, and
  ```math
  a_{\rm bond}\longrightarrow
  -\frac{c_\phi-g_\infty(e_x)}{c_\phi}\ne0.
  ```
  The midpoint field difference is nonzero, the bond denominator is nonzero, and sufficiently weak square grips can satisfy the pair-existence condition for both branches. Thus this is not an excluded cancellation or unstable block. It directly contradicts the claimed general criterion for joint limits involving the pair separation.
- **Suggested fix:** State the exact criterion as
  ```math
  N/[D-H]\to0.
  ```
  Replace it by $`N/D\to0`$ only under an additional comparison condition on $`D-H`$, such as $`H/D\to0`$. Keep the conclusions for families (A) and (B), whose hypotheses supply the needed denominator control, but remove the unrestricted equivalence from Result 14.

### I2. Zero-anchor limit is singular for linear grips
- **Location:** Consistency checks, item 1
- **Severity:** minor
- **Problem:** The statement that, as κₐ → 0, condition (5.10) “becomes μF₂ > 0” overlooks $`F_2=0`$. For a linear grip, $`1+2\mu F_2\Gamma=1>0`$ for every positive anchor strength, however small; at exactly zero anchor strength there is no lowest eigenvector. Thus existence for positive κₐ does not converge to the existence criterion at κₐ = 0. The distinction matters because linear grips are explicitly included as a control.
- **Suggested fix:** Separate the criterion at exactly κₐ = 0 from the limit through positive anchor strengths. State that the linear-grip ground states lose their normalizable limit as the anchor is removed, rather than obtaining their failure from the limiting positivity inequality.

## Focus points

None given.
