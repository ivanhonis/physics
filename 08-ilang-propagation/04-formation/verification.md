# External verification: 04-formation

- **Subproject:** 08-ilang-propagation
- **Package:** 04-formation
- **Verified version:** v2
- **External round:** 1 of 3
- **Date:** 2026-10-24T20:18:40+02:00
- **Focus points:** none

---
VERDICT: major errors

## Summary

The spectral response formulas, the Cauchy–Schwarz bound, and the exact oscillator response are substantially correct. However, the derivation does not establish the requested spatial formation result for conserved densities or cover the full oscillator class in the question. The stationary-phase assumptions are insufficiently justified, the claimed front speed conflicts with the stated arrival criterion, and the conserved-field numerical check uses the wrong criterion in three dimensions.

## Issues

### I1. Mode formation is not equivalent to formation at a distance
- **Location:** Step 4, Eqs. (4.6)–(4.9), and Open issues
- **Severity:** major
- **Problem:** The modal inequalities are valid necessary conditions for the newly introduced label criterion, but identifying $`1/|\mathbf q|`$ with a distance does not establish the corresponding spatial formation claim. A fixed Fourier component can oscillate forever while its inverse transform approaches the static field at each distant place. Indeed, the oscillator example has exactly this property, and the one-object conserved field also has permanently oscillating individual components. Thus the modal $`\lambda_{\rm form}`$ can be infinite even when spatial formation occurs on a finite, distance-dependent scale. Equation (4.8) supplies a genuine spatial obstruction only for whole-shell formation, with additional assumptions, and only for $`B=A`$; the general spatial conclusion asserted for $`B\ne A`$ is not derived.
- **Suggested fix:** Retain (4.6)–(4.9) as modal bounds, but establish their consequence for a stated spatial formation criterion. In particular, extend the shell argument using the assumed bound on $`\chi_B`$, and distinguish the resulting uniform spatial obstruction from any unproved single-place claim.

### I2. Conservation assumptions are stronger than those in item 2
- **Location:** Step 3 and Eq. (4.5)
- **Severity:** minor
- **Problem:** The question assumes conservation of $`N=\sum_x A_x`$ by the total contract and finite-range number-moving terms. Step 3 additionally assumes $`[A_x,A_y]=0`$ and conservation by every listed term separately. These are explicitly stated, but no reduction from the question’s class to this narrower class is supplied. Consequently, the claimed answer for all conserved densities in class F has an unaddressed hypothesis gap.
- **Suggested fix:** Justify the reduction or derive the quadratic sum-rule bound directly from total conservation and locality. For example, the evenness of $`f_A(\mathbf q)`$, its vanishing at zero, and the finite-range double-commutator expansion provide a route that does not require the stated termwise assumptions.

### I3. The oscillator class is narrowed without settling the excluded cases
- **Location:** Step 5, oscillator class assumptions; Result for Eq. (4.14)
- **Severity:** major
- **Problem:** The question requires $`\hat K>0`$ and the stated expansion near zero. The derivation additionally requires $`\hat K_0(\mathbf k)>0`$ for every $`\mathbf k\ne0`$. This excludes admissible fields with additional soft points. For example,
  ```math
  \hat K(\mathbf k)=m_h^2+\sum_i\sin^2 k_i
  ```
  satisfies the question’s finite-range, symmetry, positivity, and small-label assumptions with $`c_0=1`$. On even tori it separates into parity sublattices, so a source at zero produces no static or dynamic response at an odd axial separation. The three-dimensional ratio in (4.11) is then undefined there; on the ring, the difference does not remove the sublattice-dependent divergent constant in the manner assumed in Step 6. These cases require an answer rather than exclusion by an added assumption.
- **Suggested fix:** State the unique-soft-point condition as a sufficient subclass condition, and address the other members of the question’s oscillator class, including cases where the proposed criterion is undefined or does not isolate the long-range part.

### I4. Finite caustic sets do not justify the asserted remainder estimates
- **Location:** Step 6(b), Eq. (4.14), and Result for Eq. (4.14)
- **Severity:** major
- **Problem:** Finiteness of the set of caustic values does not imply that each caustic contributes only $`O(\rho^{-1/3})`$ relative to the static response. That rate requires additional conditions on degeneracy order and transverse Hessians. Already in one dimension, a stationary point whose first nonzero phase derivative has order $`p>3`$ contributes $`O(\rho^{-1/p})`$, despite there being only finitely many caustic values. Higher-dimensional degeneracies require further conditions. The argument given for the two examples establishes isolated zeros of a second derivative, not their simplicity. Moreover, fixed-$`w`$ stationary phase does not by itself establish the asserted uniformity for all $`w\ge1+\eta`$, which is needed by the “for every later $`\lambda`$” criterion. Making the theorem conditional on “the stationary-phase estimates” leaves these required estimates assumed rather than derived.
- **Suggested fix:** State and verify the actual degeneracy conditions needed for the estimates, and supply the uniform large-$`w`$ control used in the all-future formation claim. Otherwise restrict the theorem and its rate claims to dispersions for which those estimates have been established, leaving the remaining requested class explicitly unsettled.

### I5. The claimed arrival speed contradicts the fixed-threshold arrival criterion
- **Location:** Step 5, Eq. (4.11); Step 7, Eqs. (4.15)–(4.16)
- **Severity:** major
- **Problem:** Arrival is defined using a fixed relative threshold $`\eta`$, but the precursor between $`\rho/v_{\rm front}`$ and $`\rho/c_0`$ is stated to vanish as $`O(\rho^{-1/3})`$. It therefore eventually falls below every fixed positive $`\eta`$. More directly, the claimed uniform convergence to $`\Delta_\infty=-1`$ for $`w\le1-\delta`$ implies that the threshold cannot be crossed there at sufficiently large distance. For sufficiently small $`\mu`$, it is crossed just beyond $`w=1`$. Thus, under the derivation’s own estimates, the fixed-threshold arrival speed tends to $`c_0`$, not to $`2.475\,c_0`$ for the control. The finite-distance numerical arrivals do not resolve this asymptotic contradiction.
- **Suggested fix:** Distinguish a vanishing-amplitude dispersive precursor front from fixed-relative-threshold arrival. Either change the front criterion with a stated threshold limit or retain (4.11) and correct the associated arrival-speed claim.

### I6. A maximal velocity component is not generally an axial point-front speed
- **Location:** Step 6(b) and Step 7, definition of v_front and Eq. (4.15)
- **Severity:** minor
- **Problem:** For observation at $`\rho\mathbf e_1`$, stationary points require the full condition
  ```math
  \nabla\Omega(\mathbf k)=\pm(\rho/\lambda)\mathbf e_1,
  ```
  including vanishing transverse components. The quantity $`\sup_{\mathbf k}\partial_{k_1}\Omega(\mathbf k)`$ gives an upper bound on axial stationary propagation, but maximizing the first component does not generally enforce those transverse conditions for a nonseparable dispersion. The no-stationary-point argument proves an upper bound, not the asserted arrival equality. The separable examples avoid this gap, but the general class has not been covered.
- **Suggested fix:** Establish equality for the stated class or distinguish the maximal projected slope from the front along an axial ray. State the full stationary-point condition when identifying a point-front speed.

### I7. The conserved-field code does not implement the required three-dimensional criterion
- **Location:** Step 9(ii), Consistency check 2, and conserved_density_formation.py
- **Severity:** major
- **Problem:** The question specifies the criterion of input (8.10) for the field of 06-ilang-source, which uses the radial derivative of the made and static fields. In three dimensions the code instead uses the value ratio `m[:, 0] / st - 1`. It also uses the same `Dz` and `zeta_eps` for both dimensions. This checks the value-profile scaling function, not the three-dimensional derivative criterion, whose quoted small-$`\varepsilon`$ behavior is $`\zeta_3\propto\varepsilon^{2/3}`$, rather than $`\zeta_1\propto\varepsilon^2`$. Consequently, the reported three-dimensional agreement near 0.998 is not a reproduction of (8.10), despite the consistency-check claim.
- **Suggested fix:** Implement the radial derivative or a controlled lattice difference in three dimensions and use the corresponding three-dimensional scaling threshold. Alternatively, identify these outputs solely as checks of the different value criterion and do not present them as the required check of (8.10).

### I8. Finite-window crossing times are presented as all-future formation times
- **Location:** Step 9, Eq. (4.18), and the formation routines in both scripts
- **Severity:** minor
- **Problem:** Both routines return the last threshold crossing within a finite sampled interval. This is not the definition requiring the error bound for every later $`\lambda`$. The oscillator computation additionally uses a finite torus, where recurrence ultimately prevents permanent formation under that definition. The scripts document their finite windows, but the text subsequently labels their outputs as $`\lambda_{\rm form}`$ without preserving that qualification. No horizon-extension check or tail estimate is supplied to identify the finite-window values with infinite-lattice formation times.
- **Suggested fix:** Label the outputs as finite-window formation estimates and state their windows alongside the reported values. Establish stability under increasing the horizon or use an applicable tail bound before identifying them with the all-future quantity.

### I9. The explicit constant is not fixed by the total contract
- **Location:** Step 3, Eq. (4.5), and subsequent claims about c_A
- **Severity:** minor
- **Problem:** The displayed $`c_A`$ depends on the chosen decomposition into $`h_\gamma`$, including the number of terms and their maximum norm. Adding cancelling local terms, or splitting and regrouping terms while preserving $`C_F`$, changes this number. Therefore the assertion that this particular constant is fixed by $`C_F`$ and $`A`$ is not correct under M6. The sum-rule quantity $`f_A`$ itself is invariant, and the inequality can remain valid with different conservative constants.
- **Suggested fix:** Treat the displayed expression as a decomposition-dependent estimate of an intrinsic bound, rather than an invariant quantity. Formulate the final lower bounds using an intrinsically specified constant and explain how the displayed expression bounds it.

## Focus points

None given.
