# Review: 15-curved-profile-fall v1

- **Subproject:** 05-ilang-free-fall
- **Package:** 15-curved-profile-fall
- **Reviewed version:** v1
- **Date:** 2026-10-18

---
VERDICT: minor issues

## Issues

### I1. The window condition of item 2 is not stated in the quantities that the question names
- **Location:** Step 3 (v_osc), Step 7, (15.11), (15.12), Result (15.11)–(15.12); "Open issues", first item
- **Severity:** minor
- **Problem:** Item 2 asks for the conditions on $`H_k`$, $`\mathcal H_k`$, $`W`$, $`\delta p`$ and $`\lambda`$ under which the window average equals (4.16) up to a stated relative error. (15.11) contains the term $`2v_{\rm osc}/\Lambda`$, but $`v_{\rm osc}=4\int\frac{\mathrm dp}{2\pi}\omega\lvert f\rvert`$ is not bounded in these quantities, so the window length that the criterion needs is not given; the joint limit of (15.12) likewise rests on $`v_{\rm osc}(g_n)/\Lambda_n\to0`$ without saying how $`v_{\rm osc}`$ scales along the family. "Open issues" lists this, but it is part of what item 2 asks.
- **Fix:** Give an explicit upper bound on $`v_{\rm osc}`$ (or directly on the window average of $`A_{\rm osc}`$) in terms of $`\tau`$, $`M`$, the slopes, the curvatures and moments of the start ($`W`$, $`\delta p`$, or the norms of $`\eta g`$, $`\eta^2g`$, $`g'`$), and state the condition on $`\Lambda`$ in (15.11) and along the families of (15.12) with it. Remove the item from "Open issues".

### I2. "There is no term in $`W^2`$" is stated without its restriction to the non-oscillating part
- **Location:** Result (15.10); twin key result 15.10
- **Severity:** minor
- **Problem:** The sentence reads as a statement on the whole curvature contribution. Step 3 shows that $`S_{-+}`$ contains the part $`\frac H4\eta\frac\nu\omega\eta`$, so the oscillating amplitude $`f`$, and with it the curvature part of $`A_{\rm osc}`$, contains second moments of the position of the start. Only for the non-oscillating part is the absence of a $`W^2`$ term derived.
- **Fix:** State the absence of a $`W^2`$ term for the non-oscillating part only, and say how the curvature part of the oscillating terms depends on the start, with the bound of I1. Same in the twin.
