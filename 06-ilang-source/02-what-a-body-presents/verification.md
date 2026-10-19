# External verification: 02-what-a-body-presents

- **Subproject:** 06-ilang-source
- **Package:** 02-what-a-body-presents
- **Verified version:** v1
- **External round:** 1 of 3
- **Date:** 2026-10-19T09:40:19+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The first-order reduced equation, its remainder estimate, and the branch and pair expectation-value calculations are substantially correct. The central problem is the claimed well-definedness of the source field, its total, and cross-body ratios: the argument restricts admissible relistings in a way that does not satisfy M6. There are also smaller issues concerning scalar generators, the norm estimate on odd rings, and the extension to packets on finite open chains.

## Issues

### I1. Source invariance is established only under restricted relistings
- **Location:** Step 8, Eqs. (2.12)–(2.14); Result items 11–13
- **Severity:** major
- **Problem:** The “Rule” compares only representatives retaining a specially restricted coupling form, whereas M6 requires invariance under every contract relisting that preserves $`C`$. For example, take coupling (a), two positions, and $`\Phi_1=Z`$, $`\Phi_2=X`$ on a field qubit. The allowed replacement
  ```math
  C_{bf}'=C_{bf}+\gamma\delta\,\mathbb 1_b\otimes Z,\qquad
  C_f'=C_f-\gamma\delta Z
  ```
  leaves $`C`$ unchanged and remains perturbatively small. Reading the source from the relisted pair term gives $`s_1'=s_1+\gamma\delta`$, hence $`S'=S+\gamma\delta`$, despite $`\mathring\Phi_1\ne\mathring\Phi_2`$. This changes cross-body ratios as well. Step 8 already recognizes this attribution ambiguity, but then excludes it when deriving (2.14). Restricting to special representatives does not, by itself, establish the required invariance; an invariant canonical extraction from $`C`$ would have to be defined and justified.
- **Suggested fix:** Distinguish the invariant total effective generator, modulo identity, from the source attributed to a listed pair term. Remove the unrestricted well-definedness claims in (2.14), or supply a genuinely $`C`$-based extraction prescription and prove that it gives the same result after every allowed relisting. The narrower constant-shift calculation in (2.13) does not suffice for this purpose.

### I2. The stationary-generator criterion retains unobservable scalar terms
- **Location:** Step 4, Eq. (2.5); Result item 4
- **Severity:** minor
- **Problem:** The stated condition is correct for literal constancy of the particular matrix $`G_f(\lambda)`$, but is too strong as a criterion for evolution under a fixed field contract. A $`\lambda`$-dependent multiple of $`\mathbb 1_f`$ has no effect on the view. For example, with $`\Phi_x=\mathbb 1_f`$ in coupling (a), a two-branch superposition can make $`\langle B\rangle`$ oscillate, so the displayed $`G_f`$ varies, while the field evolves exactly under the fixed contract $`C_f`$. This also conflicts with the modulo-identity treatment in Step 8.
- **Suggested fix:** State the physically relevant criterion as $`\mathring\Gamma_\nu=0`$ for every nonzero frequency, and distinguish it from literal constancy of the chosen representative $`G_f`$.

### I3. The even–odd bond argument fails on odd rings
- **Location:** Step 1, operator-norm estimate following Eq. (2.2)
- **Severity:** minor
- **Problem:** On a periodic chain with odd $`n`$, the even-indexed bonds are not disjoint: the closing bond overlaps another even-indexed bond. Thus the given argument does not establish the claimed bound for all rings allowed by S3. The bound itself can still be obtained.
- **Suggested fix:** Replace the parity argument with a weighted-shift estimate, or explicitly restrict that argument to open chains and even rings and provide the corresponding estimate for odd rings.

### I4. The packet formula is not justified for finite open chains
- **Location:** Assumption S3; Step 5, paragraph beginning “A normalized packet”
- **Severity:** minor
- **Problem:** The continuous-$`p`$ packet formula and the assertion that both operators are block-diagonal in $`p`$ apply to the translation-invariant infinite chain, not to a finite open chain. Open boundaries destroy that momentum decomposition. The acknowledged absence of boundary estimates leaves this extension without its stated range of validity.
- **Suggested fix:** State an explicit infinite-chain limit for this paragraph, including the conditions needed to neglect boundaries, or formulate the packet result as a discrete momentum sum on the finite ring.

## Focus points

None given.
