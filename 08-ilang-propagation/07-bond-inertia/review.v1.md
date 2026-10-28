# Review: 07-bond-inertia v1

- **Subproject:** 08-ilang-propagation
- **Package:** 07-bond-inertia
- **Reviewed version:** v1
- **Date:** 2026-10-25

---
VERDICT: major errors

## Issues

### I1. The bound levels of (7.7) are not isolated, and the members can decay at second order
- **Location:** Step 6 "Isolation" (ii), assumption (D), Step 8 code check (ii), Results (7.7)–(7.14); twin.
- **Severity:** major
- **Problem:** Step 6 (ii) states that for $`(+,+)`$ the states with field quanta lie at least $`m_h`$ above the bound level. This counts only states whose members stay in their own bands. A member in the branch $`+`$ can emit field quanta and drop to its branch $`-`$, with the weight $`\sin^2\vartheta`$ of the branch-changing matrix element, which is nonzero for $`\tau>0`$.
  - (a) With one or two quanta this channel is open at second order in $`\delta F`$, the order of the whole package, unless $`\Omega_{\max}<2\bar M_i`$ ($`F_2=0`$) or $`\Omega_{\max}<\bar M_i`$ ($`F_2\neq0`$) for every member in the branch $`+`$, where $`\Omega_{\max}=\sqrt{m_h^2+4\kappa_h}\approx2c_0`$. The parameters of code check (ii) ($`\bar M_{1,2}\approx0.5,0.4`$ with $`\tau=1`$ and $`c_0=\tau/r`$) violate this. The members there have a decay width at second order, which the effective contract without self-energies cannot show.
  - (b) Even where (a) holds, states of a member's branch $`-`$ with several quanta reach its branch-$`+`$ energy whenever $`\bar M_i\ge m_h/2`$. The $`(+,+)`$ and mixed bound levels are then not isolated eigenvalues of the full contract.
  - (c) The only combination of isolated members, $`(-,-)`$, has no bound level near label $`0`$ by (7.7).

  So, as written, (7.9)–(7.14) describe formal coefficients of levels that are not isolated, and for the parameters of the check, levels with a width of the same order as the effects computed. Assumption (D) controls only the same-band transfers.
- **Fix:** Follow the question's new note (dated 2026-10-25). State isolation as a gap to every sector of field excitations, and say which bound levels have it. Give the condition under which no member can decay with one or two quanta (no resonance with its branch $`-`$ at the order computed), and restrict the results to it. Name the second-order coefficients of the levels that are not isolated as formal coefficients. Redo code check (ii) at parameters that satisfy that condition.
  - Say what the condition implies for $`\lambda_{C,i}=\tau/\bar M_i`$ at $`r\le1`$. With $`\Omega_{\max}\approx2c_0`$, it needs $`\bar M_i\gtrsim c_0`$ ($`F_2=0`$), i.e. $`\lambda_{C,i}\lesssim r`$.
  - Give the size of the lattice part of (7.12) there, in the deep and in the shallow regime. Restate (7.11), (7.12) and (7.14) for that range, in particular the claim "for every binding strength", which relies on $`\lambda_{C,i}\to\infty`$.
