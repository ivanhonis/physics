# Formation of the made field: bound, conserved densities and oscillator cells

- **Subproject:** 08-ilang-propagation
- **Package:** 04-formation
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-24

## Changes from previous version

- Step 3, (4.5): $`f_A\le c_A\lvert\mathbf q\rvert^2`$ is derived from the conservation of $`N`$ by $`C_F`$ and the finite range alone, with the constant $`c_A=\tfrac12\sum_d\lvert d\rvert^2\lvert F_A(d)\rvert`$, which depends on $`C_F`$ only through the total contract (I2, I9).
- Step 4, (4.19), (4.8): a spatial criterion, formation in the mean on a shell, is stated before use. (4.8) now holds for $`B=A`$ and for every source of note (a), and carries the answer of item 2. (4.6), (4.7) and (4.9) are restated as bounds on one label component (I1).
- Step 6(c), (4.20): the control of item 2 is shown under the same criterion (4.19) (I1, launch note).
- Step 5: the class of item 3 is that of the question's notes (c) and (d) (I3, I4).
- Step 6(b): the nearest-neighbour contract and the control (4.16) are shown to be members of note (d), and the estimates are made uniform on $`w\ge1+\eta`$ and on $`w\le1-\eta`$ (I4).
- Step 5, (4.11); Step 7, (4.15): the arrival threshold is now $`\eta\rho^{-1/2}`$; with a fixed threshold the arrival moves with $`c_0`$. $`v_{\rm front}`$ is now defined on the stationary points of the axial ray, and $`v_{\rm proj}`$ is added (I5, I6).
- Step 9, (4.18), Consistency check 2: the conserved field is checked with the criterion of (8.10) in both dimensions (note (e)), with $`\zeta_3(0.1)`$ computed. Every formation value is now a finite-window value, given with its window and a half-window check. The ring has $`L=16384`$; the scripts were edited and run again in `code/v3/` (I7, I8).

## Response to verification

- I1: Accepted and fixed in Step 4 and Step 6(c). The label bounds (4.6), (4.7) and (4.9) are kept as statements about one label component. The answer of item 2 now rests on a spatial criterion stated before use: formation in the mean on the shell $`\ell\le\lvert x\rvert\le2\ell`$, (4.19), which formation at every place of the shell implies. (4.8) is extended to every source with $`\chi_B\le s_B/\lvert\mathbf q\rvert^2`$. Formation at a single place is listed under Open issues.
- I2: Accepted and fixed in Step 3. $`f_A`$ is a finite trigonometric sum that is even and vanishes at $`\mathbf q=0`$, so (4.5) needs only the conservation of $`N`$ by $`C_F`$ and the finite range. Neither termwise conservation nor $`[A_x,A_y]=0`$ is used.
- I3: Accepted. The single soft point is now the class condition of the question's note (c). Members with further soft points, such as $`m_h^2+\sum_i\sin^2k_i`$, are out of scope by that note (Step 5).
- I4: Accepted and fixed in Steps 5 and 6(b). The degeneracy conditions are those of note (d): one degenerate direction, with a nonzero third derivative along it. They are verified for both examples: $`\Omega_b'''=g'''/(2\Omega_b)\ne0`$ at every zero of $`\Omega_b''`$, and the critical points are nondegenerate. The uniformity for large $`w`$ comes from the nondegenerate critical points (lattice part) and from the critical point $`\mathbf p=0`$ (small labels).
- I5: Accepted and fixed in (4.11) and Step 7. With a fixed threshold the precursor, of relative size $`O(\rho^{-1/3})`$, eventually falls below the threshold, and the arrival moves with $`c_0`$. Arrival with the front speed is stated for the threshold $`\eta\rho^{-1/2}`$, together with an exponential bound ahead of the front.
- I6: Accepted and fixed in Steps 6(b) and 7. $`v_{\rm front}`$ is now defined on the stationary points of the axial ray ($`\nabla\Omega\parallel\mathbf e_1`$). It is distinguished from $`v_{\rm proj}=\sup\partial_{k_1}\Omega\ge v_{\rm front}`$; the two are equal for separable $`\hat K_0`$, which includes both examples.
- I7: Accepted and fixed in `conserved_density_formation.py` and Step 9(ii). In $`D=3`$ the check now uses the ratio of the radial lattice differences and the three-dimensional threshold $`\zeta_3(\varepsilon)`$ of $`F_3=2\zeta V'-V`$. The former value check is removed.
- I8: Accepted and fixed in both scripts and in Step 9. Every computed formation value is a finite-window value $`\lambda^{\rm win}_{\rm form}`$, given with its window. As a horizon check, the value on the half window and the largest $`\lvert\Delta\rvert`$ on the second half of the window are reported. The all-future statement rests on the uniform estimates of Step 6(b).
- I9: Accepted and fixed in Step 3. $`c_A`$ is now defined by the expectations $`F_A(d)=\langle\Omega\vert[A_d,[C_F,A_0]]\vert\Omega\rangle`$, and its bound by $`\lVert A_0\rVert\,\lVert[C_F,A_0]\rVert`$. Both depend on $`C_F`$ only through the total contract.

## Setup and assumptions

**Class F** (assumption, M8). A field of finitely many objects with finitely many places each (A1) on a torus $`X_f=\mathbb Z_L^D`$, contract $`C_F`$ a sum of pair terms of finite range (A5), invariant under the translations: unitaries $`U_y`$ with $`U_yC_FU_y^\dagger=C_F`$, $`U_yA_xU_y^\dagger=A_{x+y}`$, $`U_yB_xU_y^\dagger=B_{x+y}`$, where $`A_x`$ (read) and $`B_x`$ (coupled to the source) are self-adjoint translates acting near $`x`$. The source sits at $`x_s=0`$ (translation).

**Source and start** (assumption, M8, M9, A11). The contract is $`C_F+g_sB_0`$ at every $`\lambda\ge0`$; at $`\lambda=0`$ the state is the lowest eigenvector $`\Omega`$ of $`C_F`$, assumed nondegenerate, eigenvalue $`E_0`$. Since $`U_y\Omega`$ is again a lowest eigenvector, $`U_y\Omega=e^{ip_0\cdot y}\Omega`$. Eigenvectors $`\lvert n\rangle`$ of $`C_F`$ are chosen with $`U_y\lvert n\rangle=e^{ip_n\cdot y}\lvert n\rangle`$; $`\omega_n=E_n-E_0>0`$ for $`n\neq0`$.

**Made field.** $`\delta a(x,\lambda)=\partial_{g_s}\langle A_x\rangle_\lambda\vert_{g_s=0}`$ (first order: the limit $`g_s\to0`$ of the coefficient is taken first); $`\delta a_{\rm st}(x)`$ the same in the lowest eigenvector of $`C_F+g_sB_0`$ (simple for small $`\lvert g_s\rvert`$). Label components $`Y_{\mathbf q}=\sum_xe^{-i\mathbf q\cdot x}Y_x`$ for operators, $`\delta a_{\mathbf q}=\sum_xe^{-i\mathbf q\cdot x}\delta a(x)`$, $`\mathbf q\in(2\pi/L)\mathbb Z^D`$; $`Y_{\mathbf q}^\dagger=Y_{-\mathbf q}`$.

**Inputs** (quoted in the question, with their settings). (8.10), (8.14), (8.15) of 07-ilang-weight/08-field-speed; (5.11) of 04-ilang-time/05-moving-clock, $`v_{\max}=\tau\kappa\sigma_X`$; (4.15) of 06-ilang-source/04-profile, $`d_\Gamma(\pi(m),\pi(m'))=k\lvert m-m'\rvert`$.

**Mathematics used** (M5): first-order (Duhamel) perturbation of $`e^{-i(C_F+g_sB_0)\lambda}`$, Cauchy–Schwarz, Fourier series on tori, Parseval and Poisson summation, closed forms of explicit Fourier integrals (Bessel functions), stationary phase (uniform in a parameter, with Airy functions at folds), contour shifts. All are applied to the stated operators; no field equation is used (M4).

## Derivation

### Step 1. First-order response in spectral form

With $`\langle A_x\rangle_\lambda=\langle\Omega\vert e^{i(C_F+g_sB_0)\lambda}A_xe^{-i(C_F+g_sB_0)\lambda}\vert\Omega\rangle`$, Duhamel's formula and $`e^{-iC_F\lambda}\Omega=e^{-iE_0\lambda}\Omega`$ give $`\delta a(x,\lambda)=-i\int_0^\lambda\mathrm ds\,\langle\Omega\vert[A_x(s),B_0]\vert\Omega\rangle`$, $`A_x(s)=e^{iC_Fs}A_xe^{-iC_Fs}`$. Inserting the eigenvectors (the $`n=0`$ terms cancel in the commutator) and integrating over $`s`$:

```math
\delta a(x,\lambda)=-\sum_{n\neq0}\Bigl[\langle\Omega\vert A_x\vert n\rangle\langle n\vert B_0\vert\Omega\rangle\,g_\lambda(\omega_n)+\langle\Omega\vert B_0\vert n\rangle\langle n\vert A_x\vert\Omega\rangle\,\overline{g_\lambda(\omega_n)}\Bigr],\qquad g_\lambda(\omega)=\frac{1-e^{-i\omega\lambda}}{\omega}.
\qquad\text{(4.1)}
```

The first-order change of the lowest eigenvector of $`C_F+g_sB_0`$ is $`-\sum_{n\ne0}\lvert n\rangle\langle n\vert B_0\vert\Omega\rangle/\omega_n`$, so $`\delta a_{\rm st}`$ is (4.1) with $`g_\lambda(\omega)\to1/\omega`$. Translation covariance gives $`\langle\Omega\vert A_x\vert n\rangle=e^{i(p_0-p_n)\cdot x}\langle\Omega\vert A_0\vert n\rangle`$ and $`\langle n\vert B_x\vert\Omega\rangle=e^{i(p_n-p_0)\cdot x}\langle n\vert B_0\vert\Omega\rangle`$. Summing over $`x`$, the first term of (4.1) survives only for $`p_n=p_0-\mathbf q`$, where $`\langle n\vert B_0\vert\Omega\rangle=\lvert X_f\rvert^{-1}\langle n\vert B_{-\mathbf q}\vert\Omega\rangle`$; the second only for $`p_n=p_0+\mathbf q`$. Hence

```math
\delta a_{\mathbf q}(\lambda)=-\frac1{\lvert X_f\rvert}\sum_{n\neq0}\Bigl[\langle\Omega\vert A_{\mathbf q}\vert n\rangle\langle n\vert B_{-\mathbf q}\vert\Omega\rangle\,g_\lambda(\omega_n)+\langle\Omega\vert B_{-\mathbf q}\vert n\rangle\langle n\vert A_{\mathbf q}\vert\Omega\rangle\,\overline{g_\lambda(\omega_n)}\Bigr],
\qquad\text{(4.2)}
```

and $`\delta a^{\rm st}_{\mathbf q}`$ is (4.2) with $`g_\lambda,\overline{g_\lambda}\to1/\omega_n`$.

### Step 2. The bound on formation (item 1)

Define, for the read operator and for any translate family $`Y`$,

```math
f_A(\mathbf q)=\frac{\langle\Omega\vert[A_{\mathbf q}^\dagger,[C_F,A_{\mathbf q}]]\vert\Omega\rangle}{\lvert X_f\rvert}=\frac1{\lvert X_f\rvert}\sum_n\omega_n\bigl(\lvert\langle n\vert A_{\mathbf q}\Omega\rangle\rvert^2+\lvert\langle n\vert A_{\mathbf q}^\dagger\Omega\rangle\rvert^2\bigr),\qquad
\chi_Y(\mathbf q)=\frac1{\lvert X_f\rvert}\sum_{n\neq0}\frac{\lvert\langle n\vert Y_{\mathbf q}\Omega\rangle\rvert^2+\lvert\langle n\vert Y_{\mathbf q}^\dagger\Omega\rangle\rvert^2}{\omega_n}.
\qquad\text{(4.3)}
```

The second form of $`f_A`$ follows by expanding the double commutator in the eigenvectors (sum rule). Both are $`\ge0`$, fixed by $`C_F`$, $`A`$ or $`Y`$, and $`\Omega`$, and unchanged by the common phase of $`\Omega`$ and by every replacement of contract terms that leaves $`C_F`$ unchanged (M6). By (4.2) with $`B=A`$, $`\delta a^{\rm st}_{\mathbf q}=-\chi_A(\mathbf q)`$: $`\chi_Y`$ is the label component of the static self-mark of $`Y`$.

Since $`\lvert g_\lambda(\omega)\rvert=2\lvert\sin(\omega\lambda/2)\rvert/\omega\le\min(\lambda,2/\omega)`$, bounding (4.2) termwise and applying Cauchy–Schwarz to the joint sum over $`n`$ and the two terms, with the weights $`\omega_n^{\pm1/2}`$ (for the bound $`\lambda`$) or $`\omega_n^{-1/2}`$ on both factors (for the bound $`2/\omega`$), gives for every $`\mathbf q`$, every $`L`$ and every $`\lambda\ge0`$

```math
\lvert\delta a_{\mathbf q}(\lambda)\rvert\le\min\Bigl\{\lambda\sqrt{f_A(\mathbf q)\,\chi_B(\mathbf q)}\,,\;2\sqrt{\chi_A(\mathbf q)\,\chi_B(\mathbf q)}\Bigr\},\qquad\text{for }B=A:\ \ \Bigl\lvert\frac{\delta a_{\mathbf q}(\lambda)}{\delta a^{\rm st}_{\mathbf q}}\Bigr\rvert\le\lambda\sqrt{\frac{f_A(\mathbf q)}{\chi_A(\mathbf q)}} .
\qquad\text{(4.4)}
```

*Highest eigenvector.* If $`\Omega`$ is the nondegenerate highest eigenvector, all $`\omega_n<0`$; Steps 1–2 hold with $`\lvert\omega_n\rvert`$, and (4.4) holds with $`\lvert f_A\rvert`$ and $`\lvert\chi\rvert`$, since the sum rule still equals $`-\sum_n\lvert\omega_n\rvert(\dots)`$. For an eigenvector inside the spectrum, $`\sum_n\lvert\omega_n\rvert(\dots)`$ is not a double commutator, and Step 3 does not apply.

### Step 3. Read operators that are conserved densities

Assumption (the question's item 2, M8): $`N=\sum_xA_x`$ commutes with $`C_F`$, and the terms of $`C_F`$ that do not commute with the $`A_x`$ have finite range. Then $`[C_F,A_0]`$ acts on the objects within a finite distance of $`0`$, and $`R_A`$, the largest $`\lvert d\rvert`$ with $`[A_d,[C_F,A_0]]\ne0`$, is finite. (For the field of 06-ilang-source, where $`\Phi_x`$ acts on every object, $`R_A=1`$ by the nearest-neighbour hopping.) Let

```math
F_A(d)=\langle\Omega\vert[A_d,[C_F,A_0]]\vert\Omega\rangle .
```

Since $`U_x[A_d,[C_F,A_0]]U_x^\dagger=[A_{x+d},[C_F,A_x]]`$ and $`U_x\Omega`$ is $`\Omega`$ up to a phase, (4.3) gives $`f_A(\mathbf q)=\sum_{\lvert d\rvert\le R_A}e^{i\mathbf q\cdot d}F_A(d)`$, a finite sum. By the second form of (4.3), $`f_A`$ is real and even in $`\mathbf q`$ ($`A_{\mathbf q}^\dagger=A_{-\mathbf q}`$), and $`f_A(0)=\lvert X_f\rvert^{-1}\langle\Omega\vert[N,[C_F,N]]\vert\Omega\rangle=0`$. Hence $`f_A(\mathbf q)=\sum_d{\rm Re}\,F_A(d)\,(\cos\mathbf q\cdot d-1)`$. With $`1-\cos\mathbf q\cdot d\le(\mathbf q\cdot d)^2/2\le\lvert\mathbf q\rvert^2\lvert d\rvert^2/2`$ and $`\lvert F_A(d)\rvert\le\lVert[A_d,[C_F,A_0]]\rVert\le2\lVert A_0\rVert\,\lVert[C_F,A_0]\rVert`$:

```math
0\le f_A(\mathbf q)\le c_A\lvert\mathbf q\rvert^2,\qquad c_A=\tfrac12\sum_{0<\lvert d\rvert\le R_A}\lvert d\rvert^2\lvert F_A(d)\rvert\ \le\ \lVert A_0\rVert\,\lVert[C_F,A_0]\rVert\sum_{0<\lvert d\rvert\le R_A}\lvert d\rvert^2 ,
\qquad\text{(4.5)}
```

for every $`L`$. $`c_A`$ is fixed by $`C_F`$, $`A`$ and $`\Omega`$, and its bound by $`C_F`$ and $`A`$. Both depend on $`C_F`$ only through the total contract, so they are unchanged by every replacement of contract terms that leaves $`C_F`$ unchanged (M6). The bound is uniform in $`L`$ when $`A_0`$ acts on a bounded number of objects; otherwise $`c_A`$ itself is used (field of 06-ilang-source: Consistency check 2). For the highest eigenvector, (4.5) holds with $`\lvert f_A\rvert`$.

### Step 4. No formation within a linear $`\lambda`$ for conserved densities (item 2)

**Criterion** (stated before use; cubic torus, $`D=3`$). Let $`\Phi\ge0`$ be smooth on $`\mathbb R^3`$, not identically zero, supported in the shell $`1\le\lvert y\rvert\le2`$, and $`\varphi_\ell(x)=\Phi(x/\ell)`$. The made field at distance $`\ell`$ has formed in the mean to accuracy $`\varepsilon\in(0,1)`$ at $`\lambda`$ if

```math
\Bigl\lvert\sum_x\varphi_\ell(x)\bigl[\delta a(x,\lambda)-\delta a_{\rm st}(x)\bigr]\Bigr\rvert\ \le\ \varepsilon\,\Bigl\lvert\sum_x\varphi_\ell(x)\,\delta a_{\rm st}(x)\Bigr\rvert ;
\qquad\text{(4.19)}
```

it has formed from $`\lambda_f`$ on if (4.19) holds for every $`\lambda\ge\lambda_f`$, and $`\lambda^\Phi_{\rm form}(\ell;\varepsilon)`$ is the least such $`\lambda_f`$ (order: $`g_s\to0`$, $`L\to\infty`$, then $`\ell\to\infty`$). This is not the arrival of a first change. Suppose the made field has formed at every place of the shell $`\ell\le\lvert x\rvert\le2\ell`$, i.e. $`\lvert\delta a-\delta a_{\rm st}\rvert\le\varepsilon\lvert\delta a_{\rm st}\rvert`$ there, and $`\delta a_{\rm st}`$ has one sign there; then (4.19) holds. **Long-range mark:** $`\delta a_{\rm st}(x)=s/\lvert x\rvert+o(\lvert x\rvert^{-1})`$, $`s\neq0`$. **Sources** (the question's note (a)): $`\chi_B(\mathbf q)\le s_B/\lvert\mathbf q\rvert^2`$ for $`\mathbf q\ne0`$. For $`B=A`$ this holds when the remainder of the mark is summable, since then $`\chi_A(\mathbf q)=4\pi\lvert s\rvert/\lvert\mathbf q\rvert^2+O(1)`$.

*Bound.* For real $`\varphi`$, Parseval gives $`\sum_x\varphi(x)\delta a(x,\lambda)=\lvert X_f\rvert^{-1}\sum_{\mathbf q}\overline{\hat\varphi(\mathbf q)}\,\delta a_{\mathbf q}(\lambda)`$. By (4.4) and (4.5), $`\lvert\delta a_{\mathbf q}(\lambda)\rvert\le\lambda\sqrt{c_As_B}`$ for $`\mathbf q\ne0`$, and $`\delta a_{\mathbf 0}=0`$ since $`f_A(0)=0`$. Poisson summation gives $`\hat\varphi_\ell(\mathbf q)=\sum_{\mathbf n\in\mathbb Z^3}\ell^3\hat\Phi(\ell(\mathbf q+2\pi\mathbf n))`$, so as $`L\to\infty`$, $`\lvert X_f\rvert^{-1}\sum_{\mathbf q}\lvert\hat\varphi_\ell\rvert\to\int_{[-\pi,\pi]^3}\lvert\hat\varphi_\ell\rvert\,\mathrm d^3q/(2\pi)^3\le\lVert\hat\Phi\rVert_1=\int_{\mathbb R^3}\lvert\hat\Phi(\mathbf p)\rvert\,\mathrm d^3p/(2\pi)^3`$, independent of $`\ell`$. Hence $`\lvert\sum_x\varphi_\ell\,\delta a(\cdot,\lambda)\rvert\le\lambda\sqrt{c_As_B}\,\lVert\hat\Phi\rVert_1`$ for every $`\lambda\ge0`$. On the other side, formation in the mean at $`\lambda`$ requires $`\lvert\sum_x\varphi_\ell\,\delta a\rvert\ge(1-\varepsilon)\lvert\sum_x\varphi_\ell\,\delta a_{\rm st}\rvert=(1-\varepsilon)\lvert s\rvert\ell^2\int\Phi(y)\lvert y\rvert^{-1}\mathrm d^3y\,(1+o(1))`$. Therefore at every $`\lambda`$ at which (4.19) holds,

```math
\lambda\ \ge\ C_\Phi\,\ell^{2}\,(1+o(1)),\qquad C_\Phi=\frac{(1-\varepsilon)\,\lvert s\rvert\int\Phi(y)\lvert y\rvert^{-1}\mathrm d^3y}{\sqrt{c_As_B}\;\lVert\hat\Phi\rVert_1}\qquad(\ell\to\infty),
\qquad\text{(4.8)}
```

and $`\lambda^\Phi_{\rm form}(\ell;\varepsilon)\ge C_\Phi\ell^2(1+o(1))`$. For every $`\beta>0`$, $`\lambda^\Phi_{\rm form}(\ell;\varepsilon)>\beta\ell`$ for all large $`\ell`$. **The long-range part of a conserved density cannot form within a $`\lambda`$ linear in the distance**, neither in the mean on a shell nor at every place of a shell; it needs a $`\lambda`$ at least quadratic in the distance. This holds for $`B=A`$ and for every source of note (a), including fields of several kinds of objects: only the conservation of $`N`$, the locality of $`A`$ and the bound on $`\chi_B`$ were used. It also holds for the highest eigenvector, with $`\lvert f_A\rvert`$ and $`\lvert\chi\rvert`$ (Steps 2, 3). Sources with a stronger self-response are out of scope by note (a). **Control:** oscillator cells with $`A=B=q_x`$; there $`[q_x,[H,q_y]]=\delta_{xy}`$, so $`f_A=1`$, $`q_x`$ is not the density of a conserved number, and (4.20) of Step 6(c) gives formation in the sense of (4.19) within a linear $`\lambda`$.

*Label form* (bounds on one component). The label component $`\mathbf q`$ has formed to accuracy $`\varepsilon`$ from $`\lambda_f`$ on if $`\lvert\delta a_{\mathbf q}(\lambda)-\delta a^{\rm st}_{\mathbf q}\rvert\le\varepsilon\lvert\delta a^{\rm st}_{\mathbf q}\rvert`$ for every $`\lambda\ge\lambda_f`$; $`\lambda_{\rm form}(\mathbf q;\varepsilon)`$ is the least such $`\lambda_f`$ ($`L\to\infty`$ at fixed $`\mathbf q`$, or $`\lambda`$ below the wrap time). This criterion concerns one component. A component can oscillate for ever while the made field at every distant place converges (oscillator cells, (4.10)), so it does not by itself constrain formation at a distance. With a long-range mark in label form, $`\lvert\delta a^{\rm st}_{\mathbf q}\rvert\ge s_0/\lvert\mathbf q\rvert^2`$ for $`\lvert\mathbf q\rvert\le q_1`$, formation of $`\mathbf q`$ requires $`\lvert\delta a_{\mathbf q}(\lambda)\rvert\ge(1-\varepsilon)\lvert\delta a^{\rm st}_{\mathbf q}\rvert`$. With (4.4) and (4.5), this gives, for every $`B`$,

```math
\lambda_{\rm form}(\mathbf q;\varepsilon)\ \ge\ \frac{(1-\varepsilon)\,\lvert\delta a^{\rm st}_{\mathbf q}\rvert}{\lvert\mathbf q\rvert\sqrt{c_A\,\chi_B(\mathbf q)}} ,
\qquad\text{(4.6)}
```

and, for $`B=A`$ ($`\chi_B=\lvert\delta a^{\rm st}_{\mathbf q}\rvert`$),

```math
\lambda_{\rm form}(\mathbf q;\varepsilon)\ \ge\ \frac{1-\varepsilon}{\lvert\mathbf q\rvert}\sqrt{\frac{\lvert\delta a^{\rm st}_{\mathbf q}\rvert}{c_A}}\ \ge\ \frac{1-\varepsilon}{\lvert\mathbf q\rvert^{2}}\sqrt{\frac{s_0}{c_A}}\qquad(\lvert\mathbf q\rvert\le q_1).
\qquad\text{(4.7)}
```

For $`B\ne A`$, formation of $`\mathbf q`$ within $`\lambda\le\beta/\lvert\mathbf q\rvert`$ requires the first relation below. For a source of note (a), (4.6) with $`\lvert\mathbf q\rvert\sqrt{c_A\chi_B}\le\sqrt{c_As_B}`$ gives the second:

```math
\chi_B(\mathbf q)\ \ge\ \frac{(1-\varepsilon)^2s_0^2}{\beta^2c_A}\,\frac1{\lvert\mathbf q\rvert^{4}};\qquad
\chi_B(\mathbf q)\le\frac{s_B}{\lvert\mathbf q\rvert^2}\ \Longrightarrow\ \lambda_{\rm form}(\mathbf q;\varepsilon)\ \ge\ \frac{(1-\varepsilon)\,s_0}{\sqrt{c_A s_B}}\,\frac1{\lvert\mathbf q\rvert^{2}}\quad(\lvert\mathbf q\rvert\le q_1).
\qquad\text{(4.9)}
```

So under (4.5) a label component of a long-range mark cannot form before a $`\lambda\propto\lvert\mathbf q\rvert^{-2}`$, for $`B=A`$ and for every source of note (a). For any $`B`$ it is excluded within $`\lambda\le\beta/\lvert\mathbf q\rvert`$ whenever $`\lvert\mathbf q\rvert^4\chi_B(\mathbf q)\to0`$. The highest eigenvector gives the same, with $`\lvert f_A\rvert`$ and $`\lvert\chi\rvert`$.

### Step 5. Oscillator cells: the made field and the criterion (item 3)

**Class** (M8; the question's item 3 with its notes (c) and (d)). $`H=\tfrac12\sum_xp_x^2+\tfrac12\sum_{x,y}q_xK_{xy}q_y`$ and $`A_x=B_x=q_x`$. $`K`$ has finite range and is invariant under the translations and under the permutations and reflections of the axes. $`\hat K(\mathbf k)=m_h^2+\hat K_0(\mathbf k)`$ with $`\hat K_0(\mathbf k)=c_0^2\lvert\mathbf k\rvert^2+O(\lvert\mathbf k\rvert^4)`$ (isotropic at second order by the cubic symmetry), and $`m_h,c_0>0`$. $`\hat K`$ is real and even, and $`\Omega_{\mathbf k}=\hat K(\mathbf k)^{1/2}`$ are the normal-mode frequencies. Two further conditions define the class:
- (c) a single soft point, $`\hat K_0(\mathbf k)>0`$ for $`\mathbf k\ne0`$;
- (d) on $`\mathbf k\ne0`$, at $`m_h\to0`$:
  - the phases $`\rho k_1\pm\lambda\Omega_{\mathbf k}`$ have finitely many caustic values of $`\rho/\lambda`$;
  - at each degenerate stationary point there is one degenerate direction, with a nonzero third derivative along it (a fold);
  - the critical points of $`\Omega`$ are nondegenerate.

Since $`\Omega`$ depends smoothly on $`m_h^2`$ on $`\lvert\mathbf k\rvert\ge\delta`$, (d) persists for small $`m_h`$. The other members of the oscillator class are out of scope by notes (c) and (d). Limit: $`M\to\infty`$ first. The lowest eigenvector and the first-order response of the compression $`C_M`$ then become those of $`H`$ (a stated limit, standard for compressions onto growing sets of low levels).

For $`H+g_sq_0`$, quadratic plus linear, the equations of the means are closed and exact: $`\mathrm d\langle q\rangle/\mathrm d\lambda=\langle p\rangle`$, $`\mathrm d\langle p\rangle/\mathrm d\lambda=-K\langle q\rangle-g_se_0`$. The ground state of $`H`$ is invariant under $`(q,p)\to(-q,-p)`$, so $`\langle q\rangle=\langle p\rangle=0`$ at $`\lambda=0`$, and $`\langle q\rangle_\lambda=-g_sK^{-1}(1-\cos K^{1/2}\lambda)e_0`$, exactly linear in $`g_s`$. The lowest eigenvector of $`H+g_sq_0`$ is the ground state displaced by $`-g_sK^{-1}e_0`$. Hence $`\delta a_{\mathbf k}(\lambda)=-(1-\cos\Omega_{\mathbf k}\lambda)/\Omega_{\mathbf k}^2`$, $`\delta a^{\rm st}_{\mathbf k}=-1/\Omega_{\mathbf k}^2`$, and for $`L\to\infty`$

```math
u(x,\lambda):=\delta a(x,\lambda)-\delta a_{\rm st}(x)=\int_{[-\pi,\pi]^D}\frac{\mathrm d^D k}{(2\pi)^D}\,e^{i\mathbf k\cdot x}\,\frac{\cos\Omega_{\mathbf k}\lambda}{\Omega_{\mathbf k}^2}.
\qquad\text{(4.10)}
```

(With (4.3): $`f_A=1`$, $`\chi_A=\Omega_{\mathbf q}^{-2}`$, and (4.4) reads $`1-\cos\Omega_{\mathbf q}\lambda\le\lambda\Omega_{\mathbf q}`$.)

**Criterion** (stated before use; places $`\rho\mathbf e_1`$, $`\rho\in\mathbb N`$, along an axis):

```math
\Delta_3(\rho,\lambda)=\frac{\delta a(\rho\mathbf e_1,\lambda)}{\delta a_{\rm st}(\rho\mathbf e_1)}-1\ \ (D=3),\qquad
\Delta_1(\rho,\lambda)=\frac{\nabla\delta a(\rho,\lambda)}{\nabla\delta a_{\rm st}(\rho)}-1,\ \ \nabla v(\rho)=v(\rho+1)-v(\rho)\ \ (D=1);
\qquad\text{(4.11)}
```

the made field at distance $`\rho`$ has formed to accuracy $`\varepsilon\in(0,1)`$ from $`\lambda_f`$ on if $`\lvert\Delta_D(\rho,\lambda)\rvert\le\varepsilon`$ for every $`\lambda\ge\lambda_f`$; $`\lambda_{\rm form}(\rho;\varepsilon)`$ is the least such $`\lambda_f`$. The first change arrives at $`\lambda_{\rm arr}(\rho;\eta)`$, the first $`\lambda`$ with $`\lvert\Delta_D+1\rvert\ge\eta\rho^{-1/2}`$ ($`\eta>0`$ fixed; a threshold that decreases with the distance, Step 7). In $`D=3`$ the static mark at $`1\ll\rho\ll c_0/m_h`$ is dominated by its inverse-distance part. In $`D=1`$ it is a constant plus a part linear in $`\rho`$, and the difference removes the constant, as the gradient does in (8.10). The square torus is out of scope by note (b) of the question.

### Step 6. Scaling limit and the formation speed (item 3)

**Order of limits.** $`g_s\to0`$, $`M\to\infty`$, $`L\to\infty`$ (or $`\lambda`$ below the wrap time), then $`\rho\to\infty`$ along $`\mathbf e_1`$ at fixed $`w=c_0\lambda/\rho`$ and fixed $`\mu=m_h\rho/c_0`$, then $`\mu`$ small. Thus $`m_h=\mu c_0/\rho\to0`$ with $`\hat K_0`$ fixed: the distances are large against the lattice spacing and a fixed fraction $`\mu`$ of the pinning length $`c_0/m_h`$.

*(a) Small labels*, $`\lvert\mathbf k\rvert<\delta`$. With $`\mathbf k=\mathbf p/\rho`$: $`\Omega_{\mathbf k}\lambda=w\sqrt{\mu^2+p^2}\,(1+O(p^2/\rho^2))`$ and $`\Omega_{\mathbf k}^{-2}=\rho^2c_0^{-2}(\mu^2+p^2)^{-1}(1+O(p^2/\rho^2))`$. So (4.10) and the static mark tend to $`\rho^{2-D}c_0^{-2}`$ times the integrals $`\int\mathrm d^Dp\,(2\pi)^{-D}e^{ip_1}\cos(w\sqrt{\mu^2+p^2})/(\mu^2+p^2)`$ at $`w`$ and at $`w=0`$. These are standard Fourier integrals of explicit functions (M5). In $`D=3`$ (value at unit distance) and in $`D=1`$ (derivative in the place at unit distance) they give the same ratio

```math
\Delta_\infty(w,\mu)=\begin{cases}-1, & w<1,\\[2pt] e^{\mu}-1-\mu e^{\mu}\,I_\mu\bigl(\mu\sqrt{w^2-1}\bigr), & w>1,\end{cases}\qquad I_\mu(Y)=\int_0^Y\frac{J_1(y)\,\mathrm dy}{\sqrt{y^2+\mu^2}} .
\qquad\text{(4.12)}
```

In $`D=3`$, $`\partial_w`$ of the first integral is $`-(4\pi)^{-1}[\delta(w-1)-\theta(w-1)\,\mu J_1(\mu\sqrt{w^2-1})/\sqrt{w^2-1}]`$, and its value at $`w=0`$ is $`e^{-\mu}/(4\pi)`$. In $`D=1`$, $`\partial_w`$ of the place derivative is $`\tfrac12[\delta(w-1)-\theta(w-1)\,\mu J_1(\mu\sqrt{w^2-1})/\sqrt{w^2-1}]`$, starting from $`-e^{-\mu}/2`$. The substitution $`y=\mu\sqrt{w'^2-1}`$ gives $`I_\mu`$. The lobes of $`J_1`$ between its zeros alternate in sign and decrease in weight against $`1/\sqrt{y^2+\mu^2}`$, so $`0\le I_\mu(Y)\le I_\mu(j_{1,1})<1.1`$ for all $`Y\ge0`$ (checked numerically for $`10^{-3}\le\mu\le1`$: $`\min I_\mu=0`$, $`\max I_\mu\le1.092`$). Write $`\Delta_\infty=(e^\mu-1-\mu e^\mu)+\mu e^\mu(1-I_\mu)`$. Then $`0\le1-e^{\mu}(1-\mu)\le\mu^2e^\mu/2`$ and $`\lvert1-I_\mu\rvert\le1`$ give

```math
\Delta_\infty(w,\mu)=-1\ \ (w<1),\qquad \lvert\Delta_\infty(w,\mu)\rvert\le\mu e^{\mu}\bigl(1+\tfrac{\mu}{2}\bigr)\ \ (w>1).
\qquad\text{(4.13)}
```

*(b) Uniform estimates.* Fix $`\eta>0`$. A smooth cutoff splits (4.10) (and its difference $`\nabla`$ in $`D=1`$) into $`\lvert\mathbf k\rvert<2\delta`$ and $`\lvert\mathbf k\rvert>\delta`$, with $`\delta=\delta(\eta)`$ small.

On $`\lvert\mathbf k\rvert>\delta`$ the amplitude $`\Omega_{\mathbf k}^{-2}`$ (times $`e^{ik_1}-1`$ for $`\nabla`$) is smooth in $`\mathbf k`$ and $`m_h`$. The phases are $`\rho k_1\pm\lambda\Omega_{\mathbf k}=\lambda(vk_1\pm\Omega_{\mathbf k})`$, $`v=\rho/\lambda=c_0/w`$, with stationary points where $`\nabla\Omega_{\mathbf k}=\mp v\,\mathbf e_1`$, transverse components included. Let $`v_{\rm front}`$ be the largest $`\lvert\partial_{k_1}\Omega_{\mathbf k}\rvert`$ at points with $`\partial_{k_j}\Omega_{\mathbf k}=0`$ for all $`j\ge2`$ (at $`m_h\to0`$).
- For $`w\ge1+\eta`$ the large parameter is $`\lambda\ge(1+\eta)\rho/c_0`$, and $`v`$ lies in the compact set $`[0,c_0/(1+\eta)]`$.
- For $`w\le1-\eta`$ the large parameter is $`\rho`$, and $`\lambda/\rho`$ lies in $`[0,(1-\eta)/c_0]`$.

By (d), on these parameter sets the stationary points are nondegenerate or folds, with finitely many caustic values, and at $`v=0`$ they are the critical points of $`\Omega`$, which are nondegenerate. Stationary phase uniform in the parameter, with Airy functions at the folds, bounds this part by $`O(\lambda^{-D/2})`$ off the caustic values and by $`O(\lambda^{-(D-1)/2-1/3})`$ everywhere. Relative to the static value ($`\propto\rho^{-1}`$, $`D=3`$) or gradient ($`\propto\rho^0`$, $`D=1`$) this is $`O(\rho^{-1/2})`$, and $`O(\rho^{-1/3})`$ near caustic values, uniformly on each range; for $`w\ge1+\eta`$ it decreases with $`w`$.

On $`\delta\le\lvert\mathbf k\rvert<2\delta`$ and down to the scaling region $`\lvert\mathbf k\rvert=P/\rho`$, $`\lvert\nabla\Omega_{\mathbf k}\rvert=c_0(1+O(\delta^2)+O(\mu^2/P^2))`$. So for $`\delta`$ small and $`P`$ large there is no stationary point at $`\lvert w-1\rvert\ge\eta`$, and this part is small by non-stationary phase. In the scaling region, (a) holds uniformly on compact sets of $`w`$ (dominated convergence). For large $`w`$, the only critical point of $`\nu(\mathbf p)=\rho\Omega_{\mathbf p/\rho}/c_0`$ is $`\mathbf p=0`$, where $`\nu=\mu`$ exactly and the Hessian is the continuum one up to $`O(\rho^{-2})`$. Stationary phase in $`w`$ therefore reproduces the large-$`w`$ behaviour of (a) with remainders uniform in $`\rho`$.

**Members** (short argument). The nearest-neighbour contract and the control (4.16) are separable: $`\hat K_0=\sum_ig(k_i)`$ with $`g(k)=a(1-\cos k)+b(1-\cos2k)`$, where $`(a,b)=(2\kappa_h,0)`$ for the nearest neighbour and $`(14,-3)`$ for the control. Here $`g'=\sin k\,(a+4b\cos k)`$ with $`a+4b\cos k>0`$ ($`2\kappa_h`$, resp. $`14-12\cos k\ge2`$), so on $`[0,\pi]`$ $`g'`$ vanishes only at $`0`$ and $`\pi`$. Moreover $`g''(0)=a+4b=2c_0^2>0`$ and $`g''(\pi)=4b-a<0`$. Hence:
- (i) The critical points of $`\Omega`$ away from $`0`$ have all $`k_i\in\{0,\pi\}`$, with the diagonal, nonzero Hessian $`g''(k_i)/(2\Omega)`$, so they are nondegenerate.
- (ii) $`\partial_{k_j}\Omega=g'(k_j)/(2\Omega)=0`$ ($`j\ge2`$) puts the stationary points on the branches $`\mathbf k_\perp\in\{0,\pi\}^{D-1}`$. There the Hessian of $`\Omega`$ is diagonal, with transverse entries $`g''(k_j)/(2\Omega)\neq0`$ and axial entry $`\Omega_b''`$, where $`\Omega_b(k_1)=(m_h^2+c_b+g(k_1))^{1/2}`$ and $`c_b=\sum_{j\ge2}g(k_j)`$. So there is at most one degenerate direction, $`\mathbf e_1`$.
- (iii) $`\Omega_b''=N_b/(4\Omega_b^3)`$ with $`N_b=2g''\Omega_b^2-g'^2`$, a trigonometric polynomial that is not identically zero, so it has finitely many zeros and finitely many caustic values. Since $`N_b'=2g'''\Omega_b^2`$, $`\Omega_b'''=g'''/(2\Omega_b)`$ at every zero. $`N_b(\pi)=2g''(\pi)\Omega_b^2<0`$, and $`N_b(0)=2g''(0)c_b>0`$ on the side branches, so the zeros lie in $`(0,\pi)`$.
  - Nearest neighbour: $`g'''=-a\sin k\neq0`$ on $`(0,\pi)`$.
  - Control: $`g'''=\sin k\,(48\cos k-14)`$ vanishes in $`(0,\pi)`$ only at $`\cos k=7/24`$, where $`N_b>0`$ on every branch.

So every zero of $`N_b`$ is simple, a fold, and both contracts are members, in $`D=1`$ and in $`D=3`$. For the nearest neighbour at $`m_h=0`$, $`N_b=-a^2[\cos^2k-2\alpha_b\cos k+1]`$ with $`\alpha_b=1+c_b/a\in\{1,3,5\}`$. The main branch ($`\alpha_b=1`$) has no zero for $`k\ne0`$, and the side branches have one zero each, at $`\cos k=\alpha_b-\sqrt{\alpha_b^2-1}`$, with caustic values $`w=(\alpha_b+\sqrt{\alpha_b^2-1})^{1/2}=1+\sqrt2`$ and $`\sqrt2+\sqrt3`$ ($`D=3`$). For the control the caustic values are $`w=0.404`$ (the front), and in $`D=3`$ also $`0.757`$ and $`0.975`$, all below 1 (`code/v3/output/oscillator_formation.json`, `fold_check`).

Near $`w=1`$ the stationary points approach the soft point $`\mathbf k=0`$, which is outside (d). There the $`O(\lvert\mathbf k\rvert^4)`$ term of $`\hat K_0`$ smooths the step of (4.12) over a window $`\lvert c_0\lambda-\rho\rvert=O(\rho^{1/3})`$, from labels $`\lvert\mathbf k\rvert=O(\rho^{-1/3})`$. For a dispersion that is concave near $`0`$ (the nearest neighbour), a wake of relative size $`O(\rho^{-1/2}(w-1)^{-3/4})`$ follows the window, from the stationary point at $`\lvert\mathbf k\rvert\propto(w-1)^{1/2}`$.

Hence, for every $`K`$ of the class, $`\Delta_D(\rho,\rho w/c_0)\to\Delta_\infty(w,\mu)`$ uniformly on $`w\ge1+\eta`$, and $`\Delta_D\to-1`$ uniformly on $`0\le w\le1-\eta`$, for every $`\eta>0`$. The lattice part contributes $`O(\rho^{-1/3})`$ at worst. With (4.13): for every $`\varepsilon\in(0,1)`$ and every $`\mu`$ with $`\mu e^\mu(1+\mu/2)<\varepsilon`$,

```math
\lim_{\rho\to\infty}\frac{c_0\,\lambda_{\rm form}(\rho;\varepsilon)}{\rho}=1,\qquad \lambda_{\rm form}(\rho;\varepsilon)-\frac{\rho}{c_0}=O(\rho^{1/3})\ \ \text{once the caustic wakes }O(\rho^{-1/3})\text{ are below }\varepsilon-\mu e^\mu(1+\tfrac{\mu}{2}) ,
\qquad\text{(4.14)}
```

on the ring ($`D=1`$) and on the cubic torus ($`D=3`$). The long-range part forms within a $`\lambda`$ linear in the distance, at the formation speed $`v_{\rm form}=c_0`$, independent of $`\varepsilon`$. For $`\lambda<(1-\eta)\rho/c_0`$ it has not formed ($`\Delta_D\to-1`$).

*(c) Control of item 2* (short argument; $`D=3`$; class (c), note (d) not needed). In the mean (4.19) only labels $`\lvert\mathbf q\rvert\lesssim1/\ell`$ enter. By Parseval, $`\sum_x\varphi_\ell\,u(x,\lambda)=\int\mathrm d^3q\,(2\pi)^{-3}\,\overline{\hat\varphi_\ell(\mathbf q)}\cos(\Omega_{\mathbf q}\lambda)/\Omega_{\mathbf q}^2`$, and on the zone $`\hat\varphi_\ell(\mathbf q)=\ell^3\hat\Phi(\ell\mathbf q)+O(\ell^{-\infty})`$. Labels with $`\lvert\mathbf q\rvert\ge\delta`$ contribute $`O(\ell^{-\infty})`$ uniformly in $`\lambda`$, since $`\Omega_{\mathbf q}^{-2}\le1/\min_{\lvert\mathbf q\rvert\ge\delta}\hat K_0`$ by (c). With $`\mathbf q=\mathbf p/\ell`$, the rest is $`\ell^2c_0^{-2}\int\mathrm d^3p\,(2\pi)^{-3}\,\overline{\hat\Phi(\mathbf p)}\cos(w\nu(\mathbf p))/\nu(\mathbf p)^2`$, with $`w=c_0\lambda/\ell`$, $`\mu=m_h\ell/c_0`$, and $`\nu\to\sqrt{\mu^2+p^2}`$ with all derivatives on bounded sets. This converges to its continuum form uniformly in $`w\ge0`$: by dominated convergence for bounded $`w`$, and for large $`w`$ by stationary phase at $`\mathbf p=0`$, where $`\nu=\mu`$ exactly. The continuum form is the mean of $`\delta a_{\rm st}(x)\Delta_\infty(c_0\lambda/\lvert x\rvert,m_h\lvert x\rvert/c_0)`$, by (a), which is isotropic. Hence

```math
\frac{\sum_x\varphi_\ell(\delta a-\delta a_{\rm st})}{\sum_x\varphi_\ell\,\delta a_{\rm st}}\ \longrightarrow\ S_\infty(w,\mu)=\frac{\int\Phi(y)\,e^{-\mu\lvert y\rvert}\lvert y\rvert^{-1}\,\Delta_\infty(w/\lvert y\rvert,\mu\lvert y\rvert)\,\mathrm d^3y}{\int\Phi(y)\,e^{-\mu\lvert y\rvert}\lvert y\rvert^{-1}\,\mathrm d^3y}\quad\text{uniformly in }w\ge0 .
\qquad\text{(4.20)}
```

On the shell $`1\le\lvert y\rvert\le2`$, $`S_\infty=-1`$ for $`w<1`$, and by (4.13) $`\lvert S_\infty\rvert\le2\mu e^{2\mu}(1+\mu)`$ for $`w>2`$. So for every $`\varepsilon\in(0,1)`$ with $`2\mu e^{2\mu}(1+\mu)<\varepsilon`$ and every $`\eta>0`$, $`(1-\eta)\ell/c_0\le\lambda^\Phi_{\rm form}(\ell;\varepsilon)\le(2+\eta)\ell/c_0`$ for all large $`\ell`$. In this member of a stated limit ($`M\to\infty`$), the long-range part forms in the mean within a $`\lambda`$ linear in the distance.

### Step 7. Formation speed, slope and front

Let $`v_{\rm slope}=\sup_{\mathbf k}\lvert\nabla\hat K_0(\mathbf k)^{1/2}\rvert`$, the largest slope of the normal-mode frequencies, and $`v_{\rm proj}=\sup_{\mathbf k}\partial_{k_1}\hat K_0(\mathbf k)^{1/2}`$ (both at $`m_h\to0`$, the regime of Step 6), with $`v_{\rm front}`$ as in Step 6(b). On the axis $`\mathbf k=k_1\mathbf e_1`$ the reflections $`k_j\to-k_j`$ give $`\partial_{k_j}\Omega=0`$ ($`j\ge2`$), and $`\partial_{k_1}\Omega\to c_0`$ as $`k_1\to0^+`$. A supremum over the stationary points of the axial ray is at most one over all $`\mathbf k`$, and $`\partial_{k_1}\le\lvert\nabla\rvert`$. Hence

```math
v_{\rm form}=c_0\ \le\ v_{\rm front}\ \le\ v_{\rm proj}\ \le\ v_{\rm slope}.
\qquad\text{(4.15)}
```

The inequalities hold for every $`K`$ of the class; $`v_{\rm form}=c_0`$ under the conditions of (4.14). $`v_{\rm proj}`$ ignores the transverse conditions. For separable $`\hat K_0=\sum_ig(k_i)`$ the stationary points lie on the branches of Step 6(b), where $`\Omega_b'=g'/(2\Omega_b)`$ is largest for $`c_b=0`$. So $`v_{\rm front}=v_{\rm proj}=\max_kg'(k)/(2g(k)^{1/2})`$.

**Arrival.**
- (i) For $`\rho/\lambda>v_{\rm proj}`$ the made field at $`\rho\mathbf e_1`$ is exponentially small in $`\rho`$. Its integrand $`e^{ik_1\rho}(1-\cos\Omega_{\mathbf k}\lambda)/\Omega_{\mathbf k}^2`$ is entire in $`\hat K(\mathbf k)`$, and $`\lvert(1-\cos z)/z^2\rvert\le2e^{\lvert{\rm Im}\,z\rvert}`$. Shifting $`k_1\to k_1+i\sigma`$ therefore bounds the made field by $`2\lambda^2\exp[-\sigma(\rho-v_{\rm proj}\lambda)+O(\sigma^2\lambda)]`$; the same holds for $`\nabla`$.
- (ii) For $`c_0/v_{\rm front}<w\le1-\eta`$ the lattice part has stationary points (Step 6(b)), and the small-label part has none and tends to its continuum value $`0`$. The made field there is a dispersive precursor of vanishing relative size: $`\asymp\rho^{-1/3}`$ at its fold edge $`\lambda\simeq\rho/v_{\rm front}`$ (when $`v_{\rm front}>c_0`$, a fold by (d) with nonzero amplitude $`\Omega^{-2}`$), and $`O(\rho^{-1/2})`$ behind it, with a constant that grows as $`w\to1`$.

With the threshold $`\eta\rho^{-1/2}`$ of (4.11) and $`v_{\rm front}=v_{\rm proj}`$, therefore $`\lambda_{\rm arr}(\rho;\eta)v_{\rm front}/\rho\to1`$. With a fixed threshold the precursor falls below it at large $`\rho`$, and by the uniform estimates of Step 6(b) the arrival then moves with $`c_0`$. For the nearest-neighbour contract, $`\hat K_0=2\kappa_h\sum_i(1-\cos k_i)`$ and $`\lvert\nabla\hat K_0^{1/2}\rvert^2=\kappa_h\sum_i\sin^2\tfrac{k_i}2\cos^2\tfrac{k_i}2/\sum_i\sin^2\tfrac{k_i}2\le\kappa_h`$. So $`c_0=v_{\rm front}=v_{\rm proj}=v_{\rm slope}=\sqrt{\kappa_h}`$: arrival and formation coincide, as in (8.15). **Control** (a member of the class with $`c_0\ne v_{\rm slope}`$):

```math
\hat K_0(\mathbf k)=\sum_{i}\bigl[14(1-\cos k_i)-3(1-\cos2k_i)\bigr]=\sum_i(1-\cos k_i)(8-6\cos k_i),\qquad c_0=1,\quad v_{\rm front}=v_{\rm proj}=v_{\rm slope}=2.475 .
\qquad\text{(4.16)}
```

It has range 2 along the axes, the symmetries of the class, $`\hat K_0\ge2\sum_i(1-\cos k_i)`$ (note (c)), and it is a member of note (d) (Step 6(b)). The speeds are computed by `code/v3/oscillator_formation.py`. There the precursor runs ahead of the formation by the factor 2.475, with vanishing relative amplitude.

### Step 8. Speeds of bodies and field (item 4)

Let $`\ell_0`$ be the recorded distance of one step of the body's chain ($`\ell_0=\kappa\sigma_X`$ in the setting of (5.11)); by (5.11) $`v_{\max}=\tau\ell_0`$. By the coupling map (4.15) of 06-ilang-source/04-profile, one chain step is $`k`$ field steps along the ring (along a lattice axis of the tori, a stated assumption, M8). So one field step is the recorded distance $`\ell_0/k`$, and the formation speed $`c_0`$ (field steps per unit $`\lambda`$) is $`c_0\ell_0/k`$. Hence

```math
\frac{v_{\rm form}}{v_{\max}}=\frac{c_0}{k\,\tau},\qquad v_{\rm form}=v_{\max}\iff c_0=k\tau\quad(\text{nearest neighbour: }\sqrt{\kappa_h}=k\tau),
\qquad\text{(4.17)}
```

independent of $`\ell_0`$; the front moves at $`v_{\rm front}\ell_0/k\ge v_{\rm form}`$. Equality of the two speeds is a condition on the description (M7).

### Step 9. Numerical check (code)

Criterion (4.11) with $`\varepsilon=0.1`$; all numbers are from `code/v3/output/`. Every computed formation value is a finite-window value $`\lambda^{\rm win}_{\rm form}`$: the last threshold crossing on $`[0,\lambda_{\max}]`$, before the first image front, with window end $`w_{\max}=c_0\lambda_{\max}/\rho`$. Horizon check: the same on $`[0,\lambda_{\max}/2]`$, and the largest $`\lvert\Delta\rvert`$ on $`[\lambda_{\max}/2,\lambda_{\max}]`$.

*(i) Oscillator cells* (`oscillator_formation.py`; $`c_0=1`$; ring $`L=16384`$, $`m_h=5\cdot10^{-5}`$; cubic torus $`L=256`$, $`m_h=2.5\cdot10^{-4}`$; so $`\mu\le0.026`$).
- **Windows.** On the ring, $`w_{\max}`$ falls from 893 ($`\rho=16`$) to 27.9 ($`\rho=512`$) for the nearest neighbour, and from 361 to 11.3 for the control. On the torus, $`w_{\max}=23.3,\,11.6,\,7.8,\,3.9`$ (nearest neighbour) and $`9.4,\,4.7,\,3.1,\,1.6`$ (control) for $`\rho=8,16,24,48`$.
- **Horizon check.** The half-window value equals the full-window value in every case except $`\rho=48`$ on the torus. On the second half of the window the largest $`\lvert\Delta\rvert`$ is at most 0.029 on the ring, and at most 0.086 on the torus for $`\rho\le24`$.
- **Control (4.16).** $`c_0\lambda^{\rm win}_{\rm form}/\rho=1.266,\,1.162,\,1.089,\,1.053,\,1.031,\,1.018`$ for $`\rho=16,32,\dots,512`$ ($`D=1`$), and $`1.344,\,1.191,\,1.154,\,1.082`$ for $`\rho=8,16,24,48`$ ($`D=3`$).
  - The arrival (threshold $`0.1\rho^{-1/2}`$) gives $`v_{\rm front}\lambda_{\rm arr}/\rho`$ from 0.928 to 0.985 ($`D=1`$) and from 0.743 to 0.882 ($`D=3`$).
  - The precursor amplitude is $`\max\lvert\Delta_D+1\rvert`$ on $`1.2\,c_0/v_{\rm front}\le w\le0.8`$. In $`D=1`$, times $`\rho^{1/3}`$, it lies between 0.66 and 0.72 for $`\rho=32,\dots,512`$: it vanishes as $`\rho^{-1/3}`$ there. In $`D=3`$ it is $`0.41,\,0.38,\,0.37,\,0.38`$ for $`\rho=8,\dots,48`$ and is not yet decreasing, since $`w=0.8`$ is still within three front windows $`\rho^{1/3}`$ of the front.
- **Nearest neighbour.** $`c_0\lambda^{\rm win}_{\rm form}/\rho=2.47,\,1.72,\,1.43,\,1.26,\,1.16,\,1.13`$ ($`D=1`$, $`\rho=16,\dots,512`$), with $`(\lambda_{\rm form}-\rho/c_0)/\rho^{1/3}`$ between 6.4 and 9.3, bounded as (4.14) states.
  - In $`D=3`$: $`4.22,\,3.64,\,3.72`$ for $`\rho=8,16,24`$, and $`3.14`$ at $`\rho=48`$ ($`w_{\max}=3.88`$). These are set by the caustic wakes at $`w=1+\sqrt2`$ and $`\sqrt2+\sqrt3`$.
  - The largest $`\lvert\Delta_3\rvert`$ on $`1.5\le w\le3`$ falls as $`0.238,\,0.197,\,0.178,\,0.130`$, i.e. as $`\rho^{-1/3}`$: the ratio from $`\rho=8`$ to 48 is 0.546, against $`6^{-1/3}=0.550`$. It extrapolates below $`\varepsilon=0.1`$ at $`\rho\approx10^2`$.
- **Membership** (`fold_check`). The zeros of $`N_b`$ and the caustic values are those of Step 6(b), with $`\Omega_b'''=-0.414,\,-0.318`$ there (nearest neighbour, side branches) and $`-2.35,\,-2.28,\,-1.83`$ (control).

In short,

```math
\frac{c_0\lambda^{\rm win}_{\rm form}}{\rho}\Big\vert_{\rm control}=1.018\ (D=1,\ \rho=512),\ \ 1.082\ (D=3,\ \rho=48);\qquad \frac{c_0\lambda^{\rm win}_{\rm form}}{\rho}\Big\vert_{\rm n.n.}=1.13\ (D=1,\ \rho=512),\ \ 3.1\text{–}4.2\ (D=3,\ \rho\le48).
\qquad\text{(4.18)}
```

Static marks: the relative deviation from the closed or Bessel form is $`1\cdot10^{-9}`$ ($`D=1`$) and $`4\cdot10^{-13}`$ ($`D=3`$). $`I_\mu`$: $`\min=0`$, $`\max\le1.092`$, $`\sup\lvert1-I_\mu\rvert=1`$ for $`\mu=10^{-3},\dots,1`$.

*(ii) Field of 06-ilang-source* (`conserved_density_formation.py`; $`t_f=1`$, infinite lattice; the criterion of (8.10) in both dimensions, i.e. the ratio of the radial lattice differences along an axis; window $`\lambda\le3\rho^2/(4\zeta_D)`$).
- $`\lambda^{\rm win}_{\rm form}/[\rho^2/(4\zeta_D(0.1))]=1.686,\,1.320,\,1.155,\,1.076`$ for $`\rho=4,8,16,32`$ ($`D=1`$, $`\zeta_1(0.1)=0.01555`$), and $`2.291,\,1.730,\,1.391,\,1.209,\,1.108`$ for $`\rho=4,8,16,32,64`$ ($`D=3`$, $`\zeta_3(0.1)=0.4068`$). The excess over 1 halves with each doubling of $`\rho`$, an $`O(1/\rho)`$ lattice correction.
- The local exponents of $`\lambda_{\rm form}`$ in $`\rho`$ over the last two distances are 1.90 ($`D=1`$) and 1.87 ($`D=3`$).
- Horizon check: the half-window value equals the full-window value for $`\rho\ge8`$ ($`D=1`$) and $`\rho\ge16`$ ($`D=3`$).
- On the linear range $`2\rho\le\lambda\le4\rho`$ the largest $`\lvert\Delta\rvert`$ is 1.37 ($`D=1`$, $`\rho=32`$) and 3.60 ($`D=3`$, $`\rho=64`$): there is no linear formation, as (8.14) states and consistent with (4.8).

## Result

Class F and its source and start as stated (Ω the nondegenerate lowest eigenvector of $`C_F`$), first order in $`g_s`$ throughout.

- **(4.1), (4.2)** (formula; every $`L`$, every $`\lambda\ge0`$): the made field and its label components in the eigenvectors of $`C_F`$; the static mark is the same with $`g_\lambda(\omega)\to1/\omega`$.
- **(4.3)** (definition): the sum-rule weight $`f_A(\mathbf q)`$ and the static self-response $`\chi_Y(\mathbf q)`$, fixed by $`C_F`$, the read or source operator and Ω; $`\delta a^{\rm st}_{\mathbf q}=-\chi_A(\mathbf q)`$ for $`B=A`$.
- **(4.4)** (theorem, item 1): $`\lvert\delta a_{\mathbf q}(\lambda)\rvert\le\min\{\lambda\sqrt{f_A\chi_B},\,2\sqrt{\chi_A\chi_B}\}`$ for every $`\mathbf q`$, $`L`$ and $`\lambda\ge0`$; for $`B=A`$, $`\lvert\delta a_{\mathbf q}(\lambda)/\delta a^{\rm st}_{\mathbf q}\rvert\le\lambda\sqrt{f_A/\chi_A}`$. It holds for the nondegenerate highest eigenvector with $`\lvert f_A\rvert,\lvert\chi\rvert`$.
- **(4.5)** (theorem): if $`N=\sum_xA_x`$ commutes with $`C_F`$ and the terms that do not commute with the $`A_x`$ have finite range, then $`0\le f_A(\mathbf q)\le c_A\lvert\mathbf q\rvert^2`$ for every $`L`$, with $`c_A=\tfrac12\sum_d\lvert d\rvert^2\lvert F_A(d)\rvert\le\lVert A_0\rVert\,\lVert[C_F,A_0]\rVert\sum_{0<\lvert d\rvert\le R_A}\lvert d\rvert^2`$, fixed by $`C_F`$, $`A`$ and Ω (the bound by $`C_F`$ and $`A`$); for the highest eigenvector with $`\lvert f_A\rvert`$.
- **(4.6)** (theorem, one label component): under (4.5), for every source operator $`B`$, formation of the label component $`\mathbf q`$ to accuracy $`\varepsilon`$ needs $`\lambda\ge(1-\varepsilon)\lvert\delta a^{\rm st}_{\mathbf q}\rvert/(\lvert\mathbf q\rvert\sqrt{c_A\chi_B(\mathbf q)})`$.
- **(4.7)** (negative, one label component, $`B=A`$): with $`\lvert\delta a^{\rm st}_{\mathbf q}\rvert\ge s_0/\lvert\mathbf q\rvert^2`$ ($`\lvert\mathbf q\rvert\le q_1`$), $`\lambda_{\rm form}(\mathbf q;\varepsilon)\ge(1-\varepsilon)\sqrt{s_0/c_A}\,\lvert\mathbf q\rvert^{-2}`$; also for the highest eigenvector.
- **(4.8)** (negative, item 2; cubic torus, order $`g_s\to0`$, $`L\to\infty`$, then $`\ell\to\infty`$): for a conserved density as in (4.5), with any source $`B`$, $`B=A`$ included, with $`\chi_B\le s_B/\lvert\mathbf q\rvert^2`$ (note (a); several kinds of objects included; for $`B=A`$ it holds when the remainder of the mark is summable) and a long-range mark $`\delta a_{\rm st}=s/\lvert x\rvert+o(\lvert x\rvert^{-1})`$, every $`\lambda`$ at which the made field at distance $`\ell`$ has formed in the mean (4.19) satisfies $`\lambda\ge C_\Phi\ell^2(1+o(1))`$, $`C_\Phi>0`$ given in (4.8). Hence for every $`\beta>0`$, $`\lambda^\Phi_{\rm form}(\ell;\varepsilon)>\beta\ell`$ for all large $`\ell`$, and the same holds for formation at every place of the shell: the long-range part cannot form within a $`\lambda`$ linear in the distance; also for the highest eigenvector. Control: (4.20).
- **(4.9)** (negative, one label component, $`B\ne A`$; under (4.5), with a long-range mark): formation of $`\mathbf q`$ within $`\lambda\le\beta/\lvert\mathbf q\rvert`$ requires $`\chi_B(\mathbf q)\ge(1-\varepsilon)^2s_0^2/(\beta^2c_A\lvert\mathbf q\rvert^4)`$; for $`\chi_B\le s_B/\lvert\mathbf q\rvert^2`$, $`\lambda_{\rm form}(\mathbf q;\varepsilon)\ge(1-\varepsilon)s_0/(\sqrt{c_As_B}\,\lvert\mathbf q\rvert^2)`$ for $`\lvert\mathbf q\rvert\le q_1`$; also for the highest eigenvector.
- **(4.10)** (formula, oscillator class, $`M\to\infty`$ then $`L\to\infty`$): exact made field $`\delta a_{\mathbf k}(\lambda)=-(1-\cos\Omega_{\mathbf k}\lambda)/\Omega_{\mathbf k}^2`$ and its deviation from the static mark.
- **(4.11)** (definition): the formation criterion along an axis (value ratio in $`D=3`$, difference ratio in $`D=1`$), $`\lambda_{\rm form}(\rho;\varepsilon)`$, and the arrival $`\lambda_{\rm arr}(\rho;\eta)`$ with the threshold $`\eta\rho^{-1/2}`$.
- **(4.12), (4.13)** (formula, theorem; scaling limit $`\rho\to\infty`$ at fixed $`w=c_0\lambda/\rho`$, $`\mu=m_h\rho/c_0`$): $`\Delta_D\to\Delta_\infty(w,\mu)`$, equal to $`-1`$ for $`w<1`$ and bounded by $`\mu e^\mu(1+\mu/2)`$ for $`w>1`$, in $`D=1`$ and $`D=3`$.
- **(4.14)** (theorem, item 3; ring ($`D=1`$) and cubic torus ($`D=3`$); the square torus is out of scope by note (b)): for every $`K`$ of the oscillator class with a single soft point (note (c)) whose part away from $`\mathbf k=0`$ has only folds as degenerate stationary points, finitely many caustic values and nondegenerate critical points of $`\Omega`$ (note (d)), for every $`\varepsilon\in(0,1)`$ and $`\mu e^\mu(1+\mu/2)<\varepsilon`$: $`c_0\lambda_{\rm form}(\rho;\varepsilon)/\rho\to1`$. The long-range part forms within a $`\lambda`$ linear in the distance, at the speed $`c_0`$, independent of $`\varepsilon`$. The lattice correction is $`O(\rho^{1/3})`$ in $`\lambda`$ once the caustic wakes, $`O(\rho^{-1/3})`$ relative, are below $`\varepsilon-\mu e^\mu(1+\mu/2)`$. The nearest-neighbour contract is a member (caustic values: none in $`D=1`$; $`w=1+\sqrt2`$ and $`\sqrt2+\sqrt3`$ in $`D=3`$), and so is the control (4.16) (caustic values $`w=0.404`$, and in $`D=3`$ also $`0.757`$, $`0.975`$). Order: $`g_s\to0`$, $`M\to\infty`$, $`L\to\infty`$, $`\rho\to\infty`$, then $`\mu`$ small.
- **(4.15)** (theorem): $`c_0\le v_{\rm front}\le v_{\rm proj}\le v_{\rm slope}`$ for every $`K`$ of the class. Under the conditions of (4.14), $`v_{\rm form}=c_0`$. The made field is exponentially small ahead of $`\rho/\lambda=v_{\rm proj}`$. Between $`\rho/v_{\rm front}`$ and $`(1-\eta)\rho/c_0`$, for every $`\eta>0`$, it is a precursor of relative size $`O(\rho^{-1/3})`$. With the threshold $`\eta\rho^{-1/2}`$ the first change arrives with $`v_{\rm front}`$ when $`v_{\rm front}=v_{\rm proj}`$ (every separable $`\hat K_0`$); with a fixed threshold it arrives with $`c_0`$. For the nearest-neighbour contract all four speeds equal $`\sqrt{\kappa_h}`$.
- **(4.16)** (example, control of item 3): $`\hat K_0=\sum_i(1-\cos k_i)(8-6\cos k_i)`$ is a member of the class (notes (c), (d)) with $`c_0=1<v_{\rm front}=v_{\rm proj}=v_{\rm slope}=2.475`$.
- **(4.17)** (formula, item 4; ring, or a lattice axis of the tori by assumption): $`v_{\rm form}/v_{\max}=c_0/(k\tau)`$; the two speeds are equal if and only if $`c_0=k\tau`$.
- **(4.18)** (numerical, Step 9, $`\varepsilon=0.1`$, finite-window values with their windows):
  - For the control (4.16), $`c_0\lambda^{\rm win}_{\rm form}/\rho`$ tends to 1 (1.018 at $`\rho=512`$, $`D=1`$; 1.082 at $`\rho=48`$, $`D=3`$, window $`w\le1.57`$), and $`v_{\rm front}\lambda_{\rm arr}/\rho`$ tends to 1 (0.985 at $`\rho=512`$, $`D=1`$).
  - For the nearest-neighbour $`K`$, $`c_0\lambda^{\rm win}_{\rm form}/\rho=1.13`$ at $`\rho=512`$ ($`D=1`$), and lies between 3.1 and 4.2 in $`D=3`$ at $`\rho\le48`$, set by caustic wakes that decay as $`\rho^{-1/3}`$.
  - For the field of 06-ilang-source with the criterion of (8.10), $`4\zeta_D\lambda^{\rm win}_{\rm form}/\rho^2`$ tends to 1 (1.076 at $`\rho=32`$, $`D=1`$; 1.108 at $`\rho=64`$, $`D=3`$).
- **(4.19)** (definition): formation in the mean at distance $`\ell`$ on the shell $`\ell\le\lvert x\rvert\le2\ell`$ (cubic torus), with weight $`\Phi(x/\ell)`$, and $`\lambda^\Phi_{\rm form}(\ell;\varepsilon)`$; implied by formation at every place of the shell.
- **(4.20)** (example, control of item 2; oscillator cells, $`D=3`$, class (c), $`M\to\infty`$, $`L\to\infty`$, $`\ell\to\infty`$ at fixed $`\mu=m_h\ell/c_0`$): the mean deviation tends to $`S_\infty(w,\mu)`$ uniformly in $`w=c_0\lambda/\ell`$, with $`S_\infty=-1`$ for $`w<1`$ and $`\lvert S_\infty\rvert\le2\mu e^{2\mu}(1+\mu)`$ for $`w>2`$. So for $`2\mu e^{2\mu}(1+\mu)<\varepsilon<1`$, $`\lambda^\Phi_{\rm form}(\ell;\varepsilon)`$ lies between $`(1-\eta)\ell/c_0`$ and $`(2+\eta)\ell/c_0`$ for all large $`\ell`$: formation within a linear $`\lambda`$ under criterion (4.19).

## Consistency checks

1. **Dimensions.** $`g_sB`$ is a rate, so $`\delta a`$ per unit $`g_s`$ has the units $`[A][B][\lambda]`$; $`f_A\sim[A]^2/[\lambda]`$ and $`\chi_B\sim[B]^2[\lambda]`$, so both bounds of (4.4) and (4.6) are consistent, and so is (4.8), where $`c_As_B\sim[A]^2[B]^2`$ per unit $`\lambda`$ per squared distance. $`c_0`$ is in field steps per unit $`\lambda`$ and $`\tau`$ is a rate, so (4.17) is a pure number.
2. **(8.10), (8.14) as a special case.** For the field of 06-ilang-source with one field object ($`n=1/\lvert X_f\rvert`$) and $`A=B=\Phi`$, $`F_A(0)=4Dnt_f`$, $`F_A(\pm\mathbf e_i)=-2nt_f`$, so $`f_A=2n\omega_{\mathbf q}`$ and (4.5) holds with $`c_A=2Dnt_f`$. (4.2) gives one mode per label, $`\delta a_{\mathbf q}(\lambda)/\delta a^{\rm st}_{\mathbf q}=1-\cos\omega_{\mathbf q}\lambda`$, and (4.8) a $`\lambda`$ quadratic in the distance, as (8.10) and (8.14). The code reproduces $`\lambda_{\rm form}\to\rho^2/(4t_f\zeta_D)`$ with the criterion of (8.10) (Step 9). It gives $`\zeta_1(0.1)=0.01555`$, against $`\pi\varepsilon^2/2=0.01571`$, and $`\zeta_3(0.1)=0.4068`$, against the leading term $`(3\sqrt{2\pi}\varepsilon/4)^{2/3}=0.3282`$ of (8.10), within its correction $`O(\varepsilon^{2/3})`$ ($`\varepsilon^{2/3}=0.22`$).
3. **(8.15) as a special case.** For the nearest-neighbour contract in $`D=3`$ with the value criterion, $`c_0=\sqrt{\kappa_h}`$, $`w=c`$ and $`\mu=m_Y\rho`$. (4.13) gives $`\lvert\Delta\rvert\le\mu e^\mu(1+\mu/2)`$ for $`c>1`$, the same order $`O(m_Y\rho)`$ as the bound $`8.4\,m_Y\rho`$ of (8.15). The remainder $`O(\rho^{-1/2})`$ of nondegenerate stationary points matches $`o(1)=O(\rho^{-1/2})`$ for $`1<c<2`$, below the first caustic value $`c=1+\sqrt2`$.

## Open issues

- Item 2: (4.8) excludes linear formation in the mean on a shell and at every place of a shell. Formation at a single place, or on a set that is not a positive fraction of a shell, is excluded only for the field of 06-ilang-source ((8.14) and the code).
- Item 3: the front window $`\lvert c_0\lambda-\rho\rvert=O(\rho^{1/3})`$ near the soft point rests on the scaling of the labels $`\lvert\mathbf k\rvert=O(\rho^{-1/3})`$, not on note (d). The approach to $`v_{\rm form}=c_0`$ is slow when the front coincides with $`c_0`$ (nearest neighbour), and at the distances computed in $`D=3`$ it is still dominated by the caustic wakes.
- Item 3, arrival: for non-separable members with $`v_{\rm front}<v_{\rm proj}`$, the decreasing-threshold arrival speed is only bracketed by $`v_{\rm front}`$ and $`v_{\rm proj}`$.
- Numerics: the computed formation values are finite-window values; the all-future statement rests on the uniform estimates of Step 6(b).
- Item 1 for eigenvectors inside the spectrum: (4.4) holds with $`\sum_n\lvert\omega_n\rvert(\dots)`$ in place of $`f_A`$, but (4.5) does not apply.
- Item 4 on the tori rests on the assumption that the coupling map runs along a lattice axis.

## Code

- `code/v3/oscillator_formation.py` (check, items 3 and 4's speeds; edited from v2 for I4, I5, I8). It computes:
  - the exact made field (4.10) on a ring ($`L=16384`$) and a cubic torus ($`L=256`$), and the static mark on the infinite lattice by its Laplace representation, cross-checked against the closed or Bessel form for the nearest-neighbour $`K`$;
  - criterion (4.11) with $`\varepsilon=0.1`$, as finite-window values on the full window and on the half window, plus the largest $`\lvert\Delta\rvert`$ on the second half of the window;
  - the arrival with the threshold $`0.1\rho^{-1/2}`$ and the precursor amplitude;
  - the speeds $`c_0`$, $`v_{\rm front}`$ and $`v_{\rm slope}`$;
  - the membership in note (d) (`fold_check`: zeros of $`N_b`$, $`\Omega_b'''`$ there, caustic values);
  - the bounds on $`I_\mu`$ used in (4.13).

  It runs for the nearest-neighbour $`K`$ and for the control (4.16). Output: `code/v3/output/oscillator_formation.json`.
- `code/v3/conserved_density_formation.py` (check, item 2; edited from v2 for I7, I8). It computes the field of 06-ilang-source with one field object and $`A=B=\Phi`$, on the infinite chain and the infinite cubic lattice, from the Bessel-function forms of (4.1). The criterion is that of (8.10) in both dimensions (ratio of the radial lattice differences), with $`\varepsilon=0.1`$, as finite-window values with a half-window check. It compares them with $`\rho^2/(4t_f\zeta_D(\varepsilon))`$, where $`\zeta_D`$ is the first zero of $`\lvert F_D\rvert-\varepsilon`$, $`F_1=V`$, $`F_3=2\zeta V'-V`$. Output: `code/v3/output/conserved_density_formation.json`.

## Methods used

- first-order (Duhamel) perturbation, spectral representation
- sum rule of a double commutator, Cauchy–Schwarz inequality
- translation covariance, Fourier series on tori, Parseval and Poisson summation
- Fourier integrals with Bessel functions, scaling limits
- stationary phase uniform in a parameter, folds and Airy functions, contour shift
- exact equations of the means for a quadratic contract
- numerical lattice sums and Bessel-function integrals (Python)
