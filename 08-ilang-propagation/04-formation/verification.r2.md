# External verification: 04-formation

- **Subproject:** 08-ilang-propagation
- **Package:** 04-formation
- **Verified version:** v3
- **External round:** 2 of 3
- **Date:** 2026-10-24T21:13:04+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The spectral response formulas, double-commutator bound and shell-averaged obstruction are consistent. The oscillator calculation supports formation at speed c₀ in the stated scaling regime, and the code implements the advertised response formulas and finite-window criteria. Some thermodynamic-limit qualifications need to be made explicit, and two numerical claims overstate what the calculations establish.

## Issues

### I1. Uniformity assumptions for the thermodynamic limit are incomplete
- **Location:** Step 3, paragraph following Eq. (4.5); Step 4, Eq. (4.8)
- **Severity:** minor
- **Problem:** Bounded support of A₀ alone does not make c_A uniform in L. Its displayed bound also involves ‖A₀‖ and ‖[C_F,A₀]‖, which can grow if local dimensions, operator normalizations or coupling strengths vary with L. Class F, as stated, does not explicitly exclude these possibilities. The finite-L inequalities remain correct, but obtaining a positive, size-independent C_Φ after taking L → ∞ requires uniform control of c_A and s_B, together with a nonzero limiting long-range coefficient s.
- **Suggested fix:** State these uniformity requirements explicitly for the thermodynamic-limit theorem. Replace the assertion that bounded support suffices by bounded support together with uniform local operator and interaction bounds, or directly assume the required uniform bounds on c_A and s_B.

### I2. Scope of the self-source conclusion needs clarification
- **Location:** Step 4, source assumptions and conclusion following Eq. (4.8); Result entry for Eq. (4.8)
- **Severity:** minor
- **Problem:** The spatial proof assumes χ_B(q) ≤ s_B/|q|², including when B = A. For the self-source case, the derivation supplies only a sufficient condition—summability of the remainder of the static mark—for obtaining this bound. The assumed real-space asymptotic s/|x| + o(1/|x|) does not itself establish the pointwise Fourier bound by the argument given. Note (a) explicitly introduces its restriction while discussing a source coupled to another operator, so its intended applicability to B = A is not entirely clear.
- **Suggested fix:** Clarify that the susceptibility restriction also applies to the self-source case, if that is the intended scope. Otherwise supply the missing argument for B = A without that additional restriction, and avoid an unqualified self-source exclusion until it is established.

### I3. The measured precursor exponent is overstated
- **Location:** Step 9(i), control precursor-amplitude bullet
- **Severity:** minor
- **Problem:** The conclusion that the ring precursor “vanishes as ρ⁻¹ᐟ³ there” is stronger than the data support. Its measurement interval, 1.2 c₀/v_front ≤ w ≤ 0.8, stays a fixed distance from both the control’s fold at w ≈ 0.404 and the soft-point front at w = 1. On that interval the stationary points are nondegenerate, so Step 6(b) gives an O(ρ⁻¹ᐟ²) estimate. An approximately constant precursor × ρ¹ᐟ³ over the reported finite distances can be a transient effective scaling; it does not establish an asymptotic ρ⁻¹ᐟ³ law.
- **Suggested fix:** Describe this as a finite-distance observation rather than an asymptotic exponent, and retain the nondegenerate stationary-phase estimate away from the fold.

### I4. Pre-image finite-torus dynamics are not exactly infinite-lattice dynamics
- **Location:** oscillator_formation.py, module docstring; Step 9(i), interpretation of numerical windows
- **Severity:** minor
- **Problem:** The code docstring says that the torus made field “equals the infinite-lattice made field before the first image front arrives.” A finite-range harmonic lattice does not have strictly compact propagation support: its matrix-function expansion produces nonzero tails at arbitrarily large separations for nonzero λ. Consequently, periodic images contribute before their front, although those contributions can be exponentially small. This matters because the code compares torus dynamics with an infinite-lattice static mark.
- **Suggested fix:** Replace “equals” by an explicitly approximate statement and use the contour-shift estimate from Step 7, or a size-refinement check, to bound image contamination over the numerical windows.

## Focus points

None given.
