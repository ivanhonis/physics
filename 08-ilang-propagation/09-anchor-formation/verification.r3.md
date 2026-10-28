# External verification: 09-anchor-formation

- **Subproject:** 08-ilang-propagation
- **Package:** 09-anchor-formation
- **Verified version:** v5
- **External round:** 3 of 3
- **Date:** 2026-10-26T20:12:15+01:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The exact finite-volume response, the uniform/place-dependent split, and the recurrence argument are consistent with the stated quadratic contract. The main formation conclusions are supported by the uniform estimates presented, and the numerical checks are appropriately distinguished from all-time formation tests. There is one unsupported strengthening of the image asymptotics and two minor formula/definition errors; none appears to change the principal conclusions.

## Issues

### I1. Image waveform estimate is stronger than the established control
- **Location:** Step 6, paragraph following Eq. (9.10); Step 7, third bullet
- **Severity:** minor
- **Problem:** The fixed-ratio asymptotics of the image strength do not, by themselves, justify replacing its convolution with $`S_0`$ by the delayed waveform $`-\beta\,\delta a_0`$. In particular, the Step 7 assertion $`\rho I=O(\rho^{-1})`$, at fixed positive $`a,b`$, needs more control of the convolution error than is supplied by (9.10). The subsequently proved bound (9.18) establishes the weaker, but sufficient, estimate
  ```math
  \rho\sup_\lambda |I|=O(\rho^{-1/6})
  ```
  in this scaling. Thus the limiting profile and formation argument need not rely on the stronger assertion.
- **Suggested fix:** Use (9.18) directly to show that the normalized image contribution vanishes in Step 7. Qualify the delayed-waveform statement as an asymptotic interpretation unless a convolution-error estimate establishing that stronger asymptotic is supplied.

### I2. Ring inverse-square mode sum is only asymptotically stated correctly
- **Location:** Step 9, weak-anchor ring paragraph
- **Severity:** minor
- **Problem:** The equality
  ```math
  L^{-1}\sum_{k\ne0}\hat K_0(k)^{-2}
  =\frac{L^3}{720\kappa_h^2}
  ```
  omits finite-size terms. For the nearest-neighbour ring, the exact sum is
  ```math
  \frac1L\sum_{k\ne0}\hat K_0(k)^{-2}
  =\frac{(L^2-1)(L^2+11)}{720\kappa_h^2L}
  =\frac{L^3}{720\kappa_h^2}+O\!\left(\frac{L}{\kappa_h^2}\right).
  ```
  The leading order used in the weak-anchor argument is correct, so this does not invalidate its stated scaling.
- **Suggested fix:** Replace the equality by the exact expression or explicitly mark it as a large-$`L`$ asymptotic.

### I3. The zero-distance Bessel kernel requires a separate definition
- **Location:** Step 6, D = 1 discussion defining E and its subsequent pole decomposition
- **Severity:** minor
- **Problem:** The integral definition
  ```math
  E(n,\lambda)=\int_0^{2c_0\lambda}\frac{2nJ_{2n}(u)}u\,du
  ```
  gives the stated Laplace pair for positive integer $`n`$, but cannot be used literally at $`n=0`$: its integrand is then zero, whereas $`\zeta_s^0/s=1/s`$ requires $`E(0,\lambda)=1`$. Zero arguments occur subsequently in $`E(|z|,\lambda)`$ and $`E(|d_s-z|,\lambda)`$. Their contributions cancel in the displayed combined expression for $`d_s>0`$, so the main result is unaffected, but the individual transform statements are not well defined as written.
- **Suggested fix:** State the integral formula for $`n\ge1`$ and define $`E(0,\lambda)=1`$ separately, with the endpoint convention at $`\lambda=0`$ specified if needed.

## Focus points

None given.
