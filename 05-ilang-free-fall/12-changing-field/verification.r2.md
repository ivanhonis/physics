# External verification: 12-changing-field

- **Subproject:** 05-ilang-free-fall
- **Package:** 12-changing-field
- **Verified version:** v3
- **External round:** 2 of 2
- **Date:** 2026-10-11T15:12:28+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The first-order reduction to the field expectation γ(λ), the velocity kernel, and the sharp-label response formulas are consistent with the stated contract and quoted inputs. The derivation carefully distinguishes fixed-start results from sharp-label limits and derives acceleration independently of velocity bounds. Two summary-level overstatements need qualification: a secular oscillation need not have a nonzero coefficient at every field frequency, and nonstationarity alone does not imply a changing effective generator or a mixed reduced view.

## Issues

### I1. A secular oscillation is not guaranteed at every frequency
- **Location:** Step 9, Result 3(b), order (II); Step 12, drift acceleration row; Result, discussion of (12.15)
- **Severity:** minor
- **Problem:** These passages assert a growing oscillation for every fixed smooth start and every Ω > 0. Equation (12.15) establishes its coefficient $`c_g(\Omega)`$, but that coefficient can vanish inside the band $`2M<\Omega<2\sqrt{M^2+\tau^2}`$. For example, choose smooth momentum weights supported away from the resonant labels, with support on both sides of $`2\omega(p)=\Omega`$. The denominator in (12.15) then has opposite signs on the two supports, and their relative weights can be adjusted so the real integral vanishes; the imaginary part is zero because the weights vanish near resonance. Symmetric supports also permit such a start to be at rest. The separately established nonvanishing result below the gap is correct.
- **Suggested fix:** State that (12.15) gives a potentially growing oscillatory term, present when $`\gamma_1c_g(\Omega)\neq0`$. Retain the unconditional nonvanishing statement below the gap for $`\gamma_1\neq0`$, and qualify the repeated “every frequency” claims.

### I2. The summary drops exceptions to changing and mixed views
- **Location:** Step 12, factor that the body sees row
- **Severity:** minor
- **Problem:** The nonstationary-field column states without qualification that the effective generator is not a contract and that the view is mixed beyond first order. Nonstationarity of the field state does not imply either conclusion: γ can remain constant, and a nonstationary field satisfying (2.11) produces an exactly pure reduced view by (2.12). The stated λ⁴ onset for a sharp start also requires the nonzero coefficient conditions in Step 3; higher first-failure index or exceptional body starts can postpone it. These exceptions are correctly discussed elsewhere but are absent from the requested summary table.
- **Suggested fix:** Qualify the row: the generator is inadmissible when γ is nonconstant; mixing is generally possible at second order but is absent under (2.11); and the λ⁴ purity-loss term applies when both factors in (12.5) are nonzero.

## Focus points

None given.
