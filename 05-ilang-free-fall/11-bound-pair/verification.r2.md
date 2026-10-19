# External verification: 11-bound-pair

- **Subproject:** 05-ilang-free-fall
- **Package:** 11-bound-pair
- **Verified version:** v2
- **External round:** 2 of 2
- **Date:** 2026-10-11T14:54:16+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The fibre contract, derivative identities, on-site resolvent equation, and leading-order bound-state formulas are consistent, and the supplied code and outputs support the numerical claims. The curvature and clock-rate calculations also check out in their stated fixed-parameter regimes. Remaining issues concern the distinction between listed and reconstructed quantities, the exclusion of isolated flat-band eigenvalues, and some missing conditions on limits and wave packets.

## Issues

### I1. Inconsistent answer about the binding-cost expression
- **Location:** Setup, Step 2, Eqs. (11.4), (11.21), (11.22), and Result item 1
- **Severity:** minor
- **Problem:** The Setup redefines $`E_b`$ and $`M_i`$ using $`C_{\rm bod}`$, and Step 2 establishes that these reconstructed quantities are invariant under every replacement (11.3). Consequently, $`E_b(P)-(M_1+M_2)`$, computed with those definitions, is invariant as well. The subsequent unqualified conclusion that “the literal expression is not well defined” conflicts with this. The discussion alternates between the eigenvalue of the listed $`C_{\rm pair}`$, the eigenvalue of $`C_{\rm bod}`$, and invariance under adding a constant to the total $`C`$; these are different questions.
- **Suggested fix:** State separately that the expression formed from listed coefficients and the listed pair contract is not invariant, whereas the expression formed from the reconstructed quantities is invariant under fixed-$`C`$ replacements. Explain separately that subtracting the reconstructed band edge additionally removes sensitivity to an overall constant added to $`C`$.

### I2. Isolation does not establish finite multiplicity
- **Location:** Setup, Multiplicity; Steps 3–5a
- **Severity:** minor
- **Problem:** The question’s definition requires a square-summable eigenvector and isolation from the rest of the spectrum; it does not explicitly require exclusion from the essential spectrum or finite multiplicity. The derivation nevertheless asserts that every bound level lies outside the bands and therefore has finite multiplicity. Its own equal-data example shows the distinction: at $`P=0`$, the mixed-band point $`0`$ is isolated from the other spectral values and has square-summable eigenvectors of infinite multiplicity. Simply declaring this point “not a bound level” does not follow from the stated pointwise conditions. Whether such a point can belong to a bound-level function on the required interval is not settled in the derivation.
- **Suggested fix:** Justify why no bound level allowed by the question can include an isolated flat essential-spectrum point. Otherwise, delimit the finite-multiplicity perturbation results explicitly and acknowledge the remaining exceptional case. An argument concerning continuation over the interval of total labels would settle this issue.

### I3. Wide and tight limits need an explicit order of limits
- **Location:** Steps 7–9, Eqs. (11.12)–(11.17)
- **Severity:** minor
- **Problem:** The $`O(\epsilon^4)`$ energy remainder and the relative $`O(\epsilon^2)`$ inertia remainder are established for fixed nonzero $`u`$ and fixed hatted data. They are then used in limits $`u\to0`$ and $`u\to\infty`$ without stating whether those limits follow $`\epsilon\to0`$, or specifying a joint validity range. In the wide-pair limit the isolation is approximately $`a u^2/2`$, so the norm estimate used to establish persistence of the level is not uniform as $`u\to0`$. In the tight-pair limit, increasing the hatted binding must still preserve the separation from the other branch groups required by the block reduction.
- **Suggested fix:** State that the displayed wide and tight forms are ordered limits of the leading-order coefficients: first $`\epsilon\to0`$ at fixed nonzero $`u`$, then $`u\to0`$ or $`u\to\infty`$. If joint limits are intended, give sufficient inequalities ensuring that the neglected terms remain smaller than the relevant isolation and branch gaps.

### I4. Mean-position identities require packet regularity
- **Location:** Step 4, Eq. (11.8), and the claim “for every g”
- **Severity:** minor
- **Problem:** Normalization $`\int |g(P)|^2\,dP=1`$ alone does not ensure that either mean position exists in the infinite-chain limit. For example, a sharp cutoff in $`g`$ can produce position probabilities with a divergent absolute first moment. Thus the bounded velocity expectation is defined, but identifying it with the derivative of a mean position cannot be claimed for every normalized $`g`$. Likewise, the $`O(\delta P^2)`$ expansion requires suitable support and bounded derivatives of the selected level.
- **Suggested fix:** Restrict the mean-position statements to packets with finite position moments and support within an interval where the bound branch is sufficiently smooth and isolated. Smooth, compactly supported $`g`$ inside such an interval is a sufficient condition. Alternatively, retain the velocity-expectation identity for general normalized packets without asserting existence of their mean positions.

## Focus points

None given.
