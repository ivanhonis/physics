# External verification: 18-mediated-effect

- **Subproject:** 03-ilang-space
- **Package:** 18-mediated-effect
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-08T21:10:25+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The exact reduction and the principal short-$`\lambda`$ probability coefficients are consistent with the stated model, including the qubit example’s $`\lambda^6`$ probability changes. However, the derivation explicitly leaves the leading position influence in item 5 undetermined, so it does not fully answer the requested example. There are also minor errors in a claimed necessary condition and in the asserted convention-invariance of intermediate operators.

## Issues

### I1. Leading position influence in the example is not determined
- **Location:** Step 9, Eq. (18.14), and “Open issues”
- **Severity:** major
- **Problem:** Item 5 asks for the leading terms of $`\delta\bar x`$, at derive depth. The calculation establishes only that its $`\lambda^6`$ coefficient vanishes and that $`\delta\bar x=O(\lambda^8)`$. It neither computes the first nonzero coefficient nor proves exact vanishing. The open-issues section explicitly acknowledges that even non-vanishing remains unsettled. Thus a requested leading influence remains unanswered.
- **Suggested fix:** Complete the Taylor calculation through the first nonzero position coefficient, including the dependence on $`m`$, $`n`$, and chain ends where relevant, or establish exact vanishing under the stated conditions.

### I2. Incorrect “exactly when” condition
- **Location:** Step 6, item 2(b), immediately after Eq. (18.10)
- **Severity:** minor
- **Problem:** The coefficient need not reduce to $`\lvert t_{h\beta}\rvert^2s_{h\beta}/12`$ only when the record-mean correction and the $`\tau_x`$ correction vanish separately: those corrections can cancel. For example, with two body places, their combined correction is
  ```math
  \frac{|t_{h\beta}|^2}{6}
  \bigl(\epsilon_h-\epsilon_\beta+t_{hh}-t_{\beta\beta}\bigr)
  \mathrm{Im}\langle\Delta D_h\rangle.
  ```
  Choosing $`t_{hh}-t_{\beta\beta}=-(\epsilon_h-\epsilon_\beta)`$, with both remaining factors nonzero, gives the claimed reduction while both individual corrections are nonzero.
- **Suggested fix:** State that separate vanishing is sufficient. The necessary-and-sufficient condition is that the sum of the two corrections vanish.

### I3. Intermediate operators are not strictly placement-invariant
- **Location:** Step 2, final sentence of “Invariance”; Step 3’s invariance justification
- **Severity:** minor
- **Problem:** The claim that $`R_\sigma`$, $`D_x`$, and $`D_x(s)`$ themselves are invariant overlooks reassignment of diagonal single-body terms. An allowed redistribution
  ```math
  t_{xx}\longmapsto t_{xx}-e_x,\qquad
  K_x\longmapsto K_x+e_x\mathbb 1_c
  ```
  leaves the total contract unchanged; it can implement moving a single-body term between its pair-term placements. Nevertheless,
  ```math
  R_\sigma\longmapsto R_\sigma+e_\beta\mathbb 1_c,\qquad
  D_x(s)\longmapsto D_x(s)+(e_x-e_\beta)\mathbb 1_c.
  ```
  Thus these operators are not invariant as asserted. The full evolution remains invariant through compensation by the diagonal part of $`C_b`$; the nested commutator coefficients also remain unchanged because the added terms are scalar.
- **Suggested fix:** Qualify this assertion to distinguish medium-only reassignment from diagonal-body reassignment. Use full diagonal blocks to formulate strict invariance, and explicitly account for the compensating changes of $`t_{xx}`$.

## Focus points

None given.
