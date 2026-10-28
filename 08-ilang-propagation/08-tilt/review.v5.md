# Review: 08-tilt v5

- **Subproject:** 08-ilang-propagation
- **Package:** 08-tilt
- **Reviewed version:** v5
- **Date:** 2026-10-26

---
VERDICT: minor issues

## Issues

### I1. The far-place check does not test the collective term with the h_eff it states, and the fixed-L statement has no remainder
- **Location:** Step 4, the paragraph on the far-site check (`spinwave_tilt.py`, decomposition of $`\Delta S-\Delta S_3`$); Result (8.7), sentence "At fixed $`\eta`$ and $`L`$ the collective rotation adds $`\frac12\sqrt{2zJS/(Nh_{\rm eff})}`$ to $`\Delta S`$ at the far place"; the same clause in the twin entry of 8.7.
- **Severity:** minor
- **Problem:** Step 4 defines $`h_{\rm eff}=(1/h_p+\hat g_L(0)/(JS))^{-1}`$ at finite $`L`$. The code computes the relaxed term with the limit value $`\gamma_3`$ in place of $`\hat g_L(0)`$ (`rel = 0.5*sqrt(12(1+eta*gam3)/(L^3 eta))`; output header "eta_eff = (1/eta + gamma_3)^-1"), and the text presents the result as the term with $`h_{\rm eff}`$. On these tori $`\hat g_L(0)=0.22461,0.23394,0.23863`$ for $`L=8,12,16`$, against $`\gamma_3=0.25273`$. With the $`h_{\rm eff}`$ of (8.6) the rest becomes $`+0.0004,+0.0011,+0.0019`$ at $`L=8`$ for $`\eta=0.1,1,10`$, and $`+0.0001`$ to $`+0.0007`$ at $`L=12`$: it grows with $`\eta`$. So the printed rest ($`\le1.1\times10^{-4}`$) does not test the stated formula at finite $`L`$. Its smallness comes from a near cancellation between $`\hat g_L(0)-\gamma_3`$ and the non-uniform part of the soft mode at the far place (Step 4 gives that part a relative norm $`O(\eta_{\rm eff}/L)`$; at the antipode $`\hat g_L(\text{far})=-0.0084,-0.0054,-0.0040`$), and the text mentions neither correction. For the same reason the far-place addition stated in (8.7) at fixed $`\eta`$ and $`L`$ holds only up to a relative correction of order $`\eta_{\rm eff}/L`$ (about $`5\%`$ at $`L=8`$, $`\eta=10`$), which the statement does not carry.
- **Fix:** Report the check as the code computes it, or compute it with the $`h_{\rm eff}`$ of (8.6). State the order of the finite-$`L`$ correction of the collective term at the far place in Step 4, in (8.7) and in its twin entry, and claim from the nine runs no more than they test.
