# External verification: 07-dressed-fall

- **Subproject:** 06-ilang-source
- **Package:** 07-dressed-fall
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-19T12:55:51+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The held-body calculation is correct: the third-order perturbative coefficient, the ring formulas, and the loss of weight factorization follow from the stated contract. The supplied code correctly checks this calculation and supports its stated coupling-order scaling. The fall calculation, however, does not establish the claimed finite-ring acceleration coefficient: it treats a local-packet approximation as an Ehrenfest identity and omits packet-dependent contributions at the retained coupling order. The isolation domain and the bookkeeping of finite-motion errors also need clarification.

## Issues

### I1. The acceleration formula lacks control of lattice and packet effects
- **Location:** Step 5, Eq. (7.7), and Step 6, Eqs. (7.8)–(7.9)
- **Severity:** major
- **Problem:** For the effective lattice contract $`E(\hat P)+W(\hat x)`$, the equations $`\dot x=\partial_PE`$, $`\dot P=-W'`$, with $`W'`$ the central lattice difference, are not general Ehrenfest identities. They require a local-packet approximation whose errors must be controlled. Regime R1 states qualitative narrowness conditions, but neither derives this approximation nor includes its errors in the acceleration.

  This matters at the order being calculated. At lowest order in $`\tau`$, the source-free band has kinetic part
  ```math
  E(P)=\text{const}+\frac{E''(0)}4(1-\cos 2P).
  ```
  For a real envelope $`\psi_j`$, its exact effective-lattice acceleration is
  ```math
  \langle\ddot x\rangle
  =-E''(0)\sum_j\psi_{j+1}\psi_{j-1}\,
  \frac{W(j+1)-W(j-1)}2,
  ```
  rather than Eq. (7.7). Replacing this expression by the value at $`x_0`$ introduces both a finite-momentum factor and spatial averaging errors.

  In particular, the retained own-mark force is cubic in $`L-2r`$. For a symmetric packet, averaging it introduces a contribution proportional to the packet's spatial variance, still of order $`\tau^2g_s\gamma^2`$. It is therefore not covered by either remainder in Eq. (7.8). A narrow-momentum packet generally has a width exceeding one site, so this contribution can exceed the retained lattice correction “+2” in Eq. (7.9). The advertised coefficient, independent of packet shape and valid throughout the stated finite-ring class, has consequently not been derived.
- **Suggested fix:** Derive the projected lattice acceleration and specify quantitative momentum-width and spatial-width approximations, including their errors. Either retain the packet-dependent force average or state a controlled spatial-gradient regime in which it can be replaced by a local value; qualify Eqs. (7.8)–(7.9), especially their finite-lattice geometric factor, accordingly.

### I2. Finite-motion errors are absent from the stated accuracy
- **Location:** Regime R2; Eq. (7.8); Result entries for Eqs. (7.7)–(7.9)
- **Severity:** minor
- **Problem:** R2 acknowledges uncomputed relative corrections of order $`\tau^2/(M_kt_f)`$ and $`\tau^2/M_k^2`$, but the displayed acceleration remainder contains only higher coupling orders. Thus the result's stated error does not describe the approximation actually used. Moreover, $`\tau^2\ll M_kt_f`$ alone does not imply $`\tau^2/M_k^2\ll1`$ throughout the stated parameter class.
- **Suggested fix:** Explicitly state the required small-motion conditions and include the associated mixed motion–coupling errors. Alternatively, label the result consistently as the coefficient of $`\tau^2`$ in a sequential expansion, rather than giving a remainder that suggests fixed-$`\tau`$ coupling accuracy.

### I3. The isolation condition is not supplied for the full claimed scope
- **Location:** Setup and assumptions; Regime R1; Open issues
- **Severity:** minor
- **Problem:** The derivation invokes the full condition (6.4) of 06-own-mark, but that condition is not among the quoted inputs. Only a sufficient inequality for the positive branch is supplied. The derivation itself acknowledges this omission, leaving the advertised applicability to both branches without an explicit, checkable isolation domain. The assumption “isolated dressed level” can support a conditional calculation, but reference to an unavailable condition does not specify that domain.
- **Suggested fix:** State a self-contained spectral-gap condition for the dressed level over the packet's momentum support, together with the smallness requirements relative to that gap, or supply the permitted verbatim input covering both branches.

## Focus points

None given.
