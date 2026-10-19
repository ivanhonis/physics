# Review: 12-changing-field v2

- **Subproject:** 05-ilang-free-fall
- **Package:** 12-changing-field
- **Reviewed version:** v2
- **Date:** 2026-10-11

---
VERDICT: minor issues

## Issues

### I1. Ranges of a fixed start are quoted without all their conditions
- **Location:** Step 6, the sentence after the three ranges of (12.18); Step 9, Result 3(b), first bullet; Step 12, table, row "Drift acceleration from rest"; Result, bullet for (12.14), (12.15), (12.19); JSON twin, key result (12.14)
- **Severity:** minor
- **Problem:** (12.18) gives the range of the drift of the velocity as $`u\,w_g\ll\lvert\gamma_0\rvert/\Gamma_\lambda`$ and $`\lambda\ll(\lvert\gamma_0\rvert/\Gamma_\lambda)\,\lambda_g`$. The sentence after the list and the table of Step 12 quote it as "$`\lambda\ll\lambda_g`$". For a gradient that mostly oscillates, $`\lvert\gamma_0\rvert\ll\Gamma_\lambda`$, the range $`\lambda\ll\lambda_g`$ does not make the error small against the drift, so the quoted form is not a sufficient range. In the same way the range of the growing part at resonance is derived in Result 3(b) with the two conditions $`u\,w_g\ll\lvert\chi_g\gamma_1\rvert/\Gamma_\lambda`$ and $`\lambda\ll(\lvert\chi_g\gamma_1\rvert/\Gamma_\lambda)\,\lambda_g`$, and the Result list and the twin call the second one alone sufficient.
- **Fix:** Wherever a range of (12.18) or of Result 3(b) is quoted, give all its conditions with their factors, or refer to the display without restating a shortened form. State the comparison of $`\lambda_a`$ with the range of the drift with the factor $`\lvert\gamma_0\rvert/\Gamma_\lambda`$, or for the case in which this factor is of order one, named as such.

### I2. "Only" for the range of the bounded parts at resonance
- **Location:** Step 9, Result 3(b), first bullet, the sentence "The bounded parts of (12.14) are described only for $`\lambda\ll\lambda_a`$"
- **Severity:** minor
- **Problem:** The sentence says that the bounded parts are not described beyond $`\lambda_a`$. What is derived is a sufficient range; Step 6 states that a longer range is not excluded. In addition $`\lambda_a`$ is defined from the bound $`E_a`$ of the acceleration, while the sentence covers the bounded parts of the velocity as well, whose range has to be taken from $`E_v`$ against their amplitude.
- **Fix:** State, as sufficient ranges and one per quantity, the range in which the bounded parts of the velocity of (12.14) are described (from $`E_v`$ against their amplitude) and the range for the acceleration (from $`E_a`$), and say what is not derived beyond them.
