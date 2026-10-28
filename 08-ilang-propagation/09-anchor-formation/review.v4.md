# Review: 09-anchor-formation v4

- **Subproject:** 08-ilang-propagation
- **Package:** 09-anchor-formation
- **Reviewed version:** v4
- **Date:** 2026-10-26

---
VERDICT: minor issues

## Issues

### I1. The reported wake sizes are not those of the output
- **Location:** Step 6, paragraph on code check (ii), cubic part ("with wakes decaying about as $`\rho^{-0.4}`$"); Code, `check_formation.py`, cubic torus, "Wakes"; Open issues, first bullet; the first entry of `open_issues` in the twin.
- **Severity:** minor
- **Problem:** The text defines the wake as $`\max_{w>1.3}\lvert\Delta_3^\perp-{\rm pred}\rvert`$ and states that it falls from $`0.30`$ to $`0.16`$ between $`\rho=3`$ and $`16`$, about as $`\rho^{-0.4}`$. `formation_check.txt` prints this quantity for every run, and no run shows that range. Far anchor: $`0.318,0.291,0.249,0.279,0.233,0.236`$ at $`L=64`$ and $`0.312,0.284,0.238,0.262,0.210,0.200`$ at $`L=96`$, for $`\rho=3,4,6,8,12,16`$. Near anchor: $`0.408,0.401,0.384,0.469,0.447,0.472`$ at both sizes, which do not decrease. For the near anchor the maximum is taken where the image front passes the probe inside the window ($`w`$ near $`b`$), so it is not a wake of the free field. The decay exponent and the statement "consistent with the $`O(\rho^{-1/3})`$ caustic wakes of Step 5" rest on the wrong range. The sentence has been in the text since v1.
- **Fix:** Report the quantity as the output gives it, for each anchor placement and size, or change the measure in the code (for example its window) and report what the code then computes. Restate the decay statement, the Open-issues bullet and its twin entry from the corrected numbers, and claim for six finite distances no more than they show.
