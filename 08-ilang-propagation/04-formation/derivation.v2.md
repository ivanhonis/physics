# Formation of the made field: bound, conserved densities and oscillator cells

- **Subproject:** 08-ilang-propagation
- **Package:** 04-formation
- **Version:** v2
- **Mode:** internal regeneration
- **Date:** 2026-10-24

## Changes from previous version

- Step 6(b), (4.14): the finiteness of the caustic set is now a stated condition of the stationary-phase step and of (4.14), with a short argument that it holds for the nearest-neighbour contract and the control (4.16) (review I1).
- Step 7, (4.15): the arrival with $`v_{\rm front}`$ and $`v_{\rm form}=c_0`$ carry the same condition (review I1).
- Step 4, (4.9): within the class of the question's note (a), $`\chi_B\le s_B/\lvert\mathbf q\rvert^2`$, the answer of item 2 for $`B\ne A`$ is stated as the conclusion of (4.9) (no linear formation, $`\lambda_{\rm form}\ge(1-\varepsilon)s_0/(\sqrt{c_As_B}\,\lvert\mathbf q\rvert^2)`$); stronger sources are out of scope (review I2).
- Step 5, Result (4.14), Open issues: the square torus is out of scope by note (b); the two former open issues on stronger sources and on the square torus are removed (review I2).
- Code: the unchanged scripts were run again in `code/v2/`; every cited number is unchanged.

## Setup and assumptions

**Class F** (assumption, M8). A field of finitely many objects with finitely many places each (A1) on a torus $`X_f=\mathbb Z_L^D`$, contract $`C_F`$ a sum of pair terms of finite range (A5), invariant under the translations: unitaries $`U_y`$ with $`U_yC_FU_y^\dagger=C_F`$, $`U_yA_xU_y^\dagger=A_{x+y}`$, $`U_yB_xU_y^\dagger=B_{x+y}`$, where $`A_x`$ (read) and $`B_x`$ (coupled to the source) are self-adjoint translates acting near $`x`$. The source sits at $`x_s=0`$ (translation).

**Source and start** (assumption, M8, M9, A11). The contract is $`C_F+g_sB_0`$ at every $`\lambda\ge0`$; at $`\lambda=0`$ the state is the lowest eigenvector $`\Omega`$ of $`C_F`$, assumed nondegenerate, eigenvalue $`E_0`$. Since $`U_y\Omega`$ is again a lowest eigenvector, $`U_y\Omega=e^{ip_0\cdot y}\Omega`$. Eigenvectors $`\lvert n\rangle`$ of $`C_F`$ are chosen with $`U_y\lvert n\rangle=e^{ip_n\cdot y}\lvert n\rangle`$; $`\omega_n=E_n-E_0>0`$ for $`n\neq0`$.

**Made field.** $`\delta a(x,\lambda)=\partial_{g_s}\langle A_x\rangle_\lambda\vert_{g_s=0}`$ (first order: the limit $`g_s\to0`$ of the coefficient is taken first); $`\delta a_{\rm st}(x)`$ the same in the lowest eigenvector of $`C_F+g_sB_0`$ (simple for small $`\lvert g_s\rvert`$). Label components $`Y_{\mathbf q}=\sum_xe^{-i\mathbf q\cdot x}Y_x`$ for operators, $`\delta a_{\mathbf q}=\sum_xe^{-i\mathbf q\cdot x}\delta a(x)`$, $`\mathbf q\in(2\pi/L)\mathbb Z^D`$; $`Y_{\mathbf q}^\dagger=Y_{-\mathbf q}`$.

**Inputs** (quoted in the question, with their settings). (8.10), (8.14), (8.15) of 07-ilang-weight/08-field-speed; (5.11) of 04-ilang-time/05-moving-clock, $`v_{\max}=\tau\kappa\sigma_X`$; (4.15) of 06-ilang-source/04-profile, $`d_\Gamma(\pi(m),\pi(m'))=k\lvert m-m'\rvert`$.

**Mathematics used** (M5): first-order (Duhamel) perturbation of $`e^{-i(C_F+g_sB_0)\lambda}`$, Cauchy–Schwarz, Fourier series on tori, closed forms of explicit Fourier integrals (Bessel functions), stationary phase. All are applied to the stated operators; no field equation is used (M4).

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

Assumption (M8): $`N=\sum_xA_x`$ with $`[A_x,A_y]=0`$; $`C_F=\sum_\gamma h_\gamma`$, the translates of finitely many terms, $`\nu`$ terms per place, each with $`[h_\gamma,N]=0`$ (the terms that move the number have finite range). Let $`x_\gamma`$ be a reference place of $`h_\gamma`$, and $`R_A`$, $`n_A`$ the largest distance from $`x_\gamma`$ to, and the largest number of, places $`x`$ with $`[h_\gamma,A_x]\neq0`$.

Because $`\sum_x[h_\gamma,A_x]=[h_\gamma,N]=0`$, and $`\sum_y[A_y,[h_\gamma,A_x]]=[[N,h_\gamma],A_x]+[h_\gamma,[N,A_x]]=0`$, the phases may be replaced by their differences from $`e^{\mp i\mathbf q\cdot x_\gamma}`$:

```math
[A_{\mathbf q}^\dagger,[C_F,A_{\mathbf q}]]=\sum_\gamma\sum_{x,y}\bigl(e^{i\mathbf q\cdot y}-e^{i\mathbf q\cdot x_\gamma}\bigr)\bigl(e^{-i\mathbf q\cdot x}-e^{-i\mathbf q\cdot x_\gamma}\bigr)[A_y,[h_\gamma,A_x]].
```

Only $`x,y`$ with $`[h_\gamma,A_x]\ne0\ne[h_\gamma,A_y]`$ contribute (with $`[A_x,A_y]=0`$, $`[A_y,[h_\gamma,A_x]]=[[A_y,h_\gamma],A_x]`$), each phase difference is at most $`\lvert\mathbf q\rvert R_A`$ in modulus, and there are $`\nu\lvert X_f\rvert`$ terms $`\gamma`$. Hence

```math
0\le f_A(\mathbf q)\le c_A\lvert\mathbf q\rvert^2,\qquad c_A=4\,\nu\,n_A^2R_A^2\,\max_\gamma\lVert h_\gamma\rVert\,\lVert A_0\rVert^2 ,
\qquad\text{(4.5)}
```

for every $`L`$; $`c_A`$ is fixed by $`C_F`$ and $`A`$. The same holds for the highest eigenvector.

### Step 4. No formation within a linear $`\lambda`$ for conserved densities (item 2)

**Label criterion** (stated before use). The label component $`\mathbf q`$ has formed to accuracy $`\varepsilon\in(0,1)`$ from $`\lambda_f`$ on if $`\lvert\delta a_{\mathbf q}(\lambda)-\delta a^{\rm st}_{\mathbf q}\rvert\le\varepsilon\lvert\delta a^{\rm st}_{\mathbf q}\rvert`$ for every $`\lambda\ge\lambda_f`$ (order: $`g_s\to0`$, then $`L\to\infty`$ at fixed $`\mathbf q`$, or $`\lambda`$ below the wrap time); $`\lambda_{\rm form}(\mathbf q;\varepsilon)`$ is the least such $`\lambda_f`$, and $`1/\lvert\mathbf q\rvert`$ the associated distance. It is not the arrival of a first change. **Long-range mark** in label form: $`\lvert\delta a^{\rm st}_{\mathbf q}\rvert\ge s_0/\lvert\mathbf q\rvert^2`$, $`s_0>0`$, for $`\lvert\mathbf q\rvert\le q_1`$; on the cubic torus an inverse-distance place dependence $`s/\lvert x\rvert`$ with a summable remainder has $`\delta a^{\rm st}_{\mathbf q}=4\pi s/\lvert\mathbf q\rvert^2+O(1)`$.

Formation at $`\lambda`$ requires $`\lvert\delta a_{\mathbf q}(\lambda)\rvert\ge(1-\varepsilon)\lvert\delta a^{\rm st}_{\mathbf q}\rvert`$; with (4.4) and (4.5), for every source operator $`B`$,

```math
\lambda_{\rm form}(\mathbf q;\varepsilon)\ \ge\ \frac{(1-\varepsilon)\,\lvert\delta a^{\rm st}_{\mathbf q}\rvert}{\lvert\mathbf q\rvert\sqrt{c_A\,\chi_B(\mathbf q)}} .
\qquad\text{(4.6)}
```

*$`B=A`$.* Then $`\chi_B=\lvert\delta a^{\rm st}_{\mathbf q}\rvert`$, and with the long-range mark

```math
\lambda_{\rm form}(\mathbf q;\varepsilon)\ \ge\ \frac{1-\varepsilon}{\lvert\mathbf q\rvert}\sqrt{\frac{\lvert\delta a^{\rm st}_{\mathbf q}\rvert}{c_A}}\ \ge\ \frac{1-\varepsilon}{\lvert\mathbf q\rvert^{2}}\sqrt{\frac{s_0}{c_A}}\qquad(\lvert\mathbf q\rvert\le q_1).
\qquad\text{(4.7)}
```

For every $`\beta>0`$, $`\lambda_{\rm form}(\mathbf q;\varepsilon)>\beta/\lvert\mathbf q\rvert`$ as soon as $`\lvert\mathbf q\rvert<(1-\varepsilon)\sqrt{s_0/c_A}/\beta`$: the long-range part cannot form within a $`\lambda`$ linear in the distance; it needs a $`\lambda`$ at least quadratic in it.

*Position form* ($`B=A`$, cubic torus). For real $`\varphi`$, Parseval gives $`\sum_x\varphi(x)\delta a(x,\lambda)=\lvert X_f\rvert^{-1}\sum_{\mathbf q}\overline{\hat\varphi(\mathbf q)}\,\delta a_{\mathbf q}(\lambda)`$. If also $`\chi_A(\mathbf q)\le s_1/\lvert\mathbf q\rvert^2`$ for all $`\mathbf q`$ (the mark is at most long-range), (4.4)–(4.5) give $`\lvert\sum_x\varphi\,\delta a(\cdot,\lambda)\rvert\le\lambda\sqrt{c_As_1}\,\lvert X_f\rvert^{-1}\sum_{\mathbf q}\lvert\hat\varphi(\mathbf q)\rvert`$. Take $`\varphi(x)=\Phi(x/\ell)`$ with $`\Phi\ge0`$ smooth on the shell $`1\le\lvert y\rvert\le2`$; as $`L\to\infty`$, $`\lvert X_f\rvert^{-1}\sum_{\mathbf q}\lvert\hat\varphi\rvert\to\lVert\hat\Phi\rVert_1=\int\lvert\hat\Phi(\mathbf p)\rvert\,\mathrm d^3p/(2\pi)^3`$, independent of $`\ell`$. If the made field has formed at every place of the shell $`\ell\le\lvert x\rvert\le2\ell`$ ($`\lvert\delta a-\delta a_{\rm st}\rvert\le\varepsilon\lvert\delta a_{\rm st}\rvert`$ there) and $`\delta a_{\rm st}=s/\lvert x\rvert+o(\lvert x\rvert^{-1})`$, then $`\lvert\sum_x\varphi\,\delta a\rvert\ge(1-\varepsilon)\lvert s\rvert\ell^2\int\Phi(y)\lvert y\rvert^{-1}\mathrm d^3y\,(1+o(1))`$, hence

```math
\lambda\ \ge\ \frac{(1-\varepsilon)\,\lvert s\rvert\int\Phi(y)\lvert y\rvert^{-1}\mathrm d^3y}{\sqrt{c_As_1}\;\lVert\hat\Phi\rVert_1}\;\ell^{2}\,(1+o(1))\qquad(\ell\to\infty).
\qquad\text{(4.8)}
```

*$`B\neq A`$* (any operator, fields of several kinds of objects included: only the conservation of $`N`$ and the locality of $`A`$ were used). By (4.6), formation within $`\lambda\le\beta/\lvert\mathbf q\rvert`$ at labels with a long-range mark requires the first relation below; for a source operator whose self-response is at most long-range, $`\chi_B(\mathbf q)\le s_B/\lvert\mathbf q\rvert^2`$ (the class of the question's note (a): a held body or a local source), (4.6) with $`\lvert\mathbf q\rvert\sqrt{c_A\chi_B}\le\sqrt{c_As_B}`$ gives the second:

```math
\chi_B(\mathbf q)\ \ge\ \frac{(1-\varepsilon)^2s_0^2}{\beta^2c_A}\,\frac1{\lvert\mathbf q\rvert^{4}};\qquad
\chi_B(\mathbf q)\le\frac{s_B}{\lvert\mathbf q\rvert^2}\ \Longrightarrow\ \lambda_{\rm form}(\mathbf q;\varepsilon)\ \ge\ \frac{(1-\varepsilon)\,s_0}{\sqrt{c_A s_B}}\,\frac1{\lvert\mathbf q\rvert^{2}}\quad(\lvert\mathbf q\rvert\le q_1).
\qquad\text{(4.9)}
```

The first relation is an exact necessary condition: the static self-mark of the source operator must grow at least as $`\lvert\mathbf q\rvert^{-4}`$ in label space (on the cubic torus, at least linearly in the distance); linear formation is excluded for every $`B`$ with $`\lvert\mathbf q\rvert^4\chi_B(\mathbf q)\to0`$ as $`\mathbf q\to0`$. In the class of note (a) the first relation fails for $`\lvert\mathbf q\rvert<(1-\varepsilon)s_0/(\beta\sqrt{c_As_B})`$ and the second gives the answer of item 2 for $`B\ne A`$: the long-range part of a conserved density cannot form within a $`\lambda`$ linear in the distance; it needs a $`\lambda`$ at least quadratic in it, as for $`B=A`$. Sources with a stronger self-response are out of scope by note (a).

The highest eigenvector gives the same, with $`\lvert f_A\rvert`$, $`\lvert\chi\rvert`$ (Step 2). **Control** (short argument): oscillator cells with $`A=B=q_x`$ in the limit $`M\to\infty`$ (Step 5). There $`[q_x,[H,q_y]]=\delta_{xy}`$, so $`f_A(\mathbf q)=1`$; $`q_x`$ is not the density of a conserved number, (4.5) fails, and Step 6 shows formation at the speed $`c_0`$.

### Step 5. Oscillator cells: the made field and the criterion (item 3)

**Class** (M8). $`H=\tfrac12\sum_xp_x^2+\tfrac12\sum_{x,y}q_xK_{xy}q_y`$, $`A_x=B_x=q_x`$, $`K`$ of finite range, invariant under the translations and the permutations and reflections of the axes, $`\hat K(\mathbf k)=m_h^2+\hat K_0(\mathbf k)`$ with $`\hat K_0(\mathbf k)=c_0^2\lvert\mathbf k\rvert^2+O(\lvert\mathbf k\rvert^4)`$ (isotropic at second order by the cubic symmetry), $`\hat K_0(\mathbf k)>0`$ for $`\mathbf k\ne0`$ (the pinning is the term $`m_h^2`$, assumption), $`m_h,c_0>0`$. $`\hat K`$ is real and even; $`\Omega_{\mathbf k}=\hat K(\mathbf k)^{1/2}`$ are the normal-mode frequencies. Limit: $`M\to\infty`$ first; the lowest eigenvector and the first-order response of the compression $`C_M`$ then become those of $`H`$ (stated limit, standard for compressions onto growing sets of low levels).

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

the made field at distance $`\rho`$ has formed to accuracy $`\varepsilon\in(0,1)`$ from $`\lambda_f`$ on if $`\lvert\Delta_D(\rho,\lambda)\rvert\le\varepsilon`$ for every $`\lambda\ge\lambda_f`$; $`\lambda_{\rm form}(\rho;\varepsilon)`$ is the least such $`\lambda_f`$. The first change arrives at $`\lambda_{\rm arr}(\rho;\eta)`$, the first $`\lambda`$ with $`\lvert\Delta_D+1\rvert\ge\eta`$. In $`D=3`$ the static mark at $`1\ll\rho\ll c_0/m_h`$ is dominated by its inverse-distance part; in $`D=1`$ it is a constant plus a part linear in $`\rho`$, and the difference removes the constant, as the gradient does in (8.10). The square torus is out of scope by note (b) of the question.

### Step 6. Scaling limit and the formation speed (item 3)

**Order of limits.** $`g_s\to0`$, $`M\to\infty`$, $`L\to\infty`$ (or $`\lambda`$ below the wrap time), then $`\rho\to\infty`$ along $`\mathbf e_1`$ at fixed $`w=c_0\lambda/\rho`$ and fixed $`\mu=m_h\rho/c_0`$ (so $`m_h=\mu c_0/\rho\to0`$ with $`\hat K_0`$ fixed: distances large against the lattice spacing and a fixed fraction $`\mu`$ of the pinning length $`c_0/m_h`$), then $`\mu`$ small.

*(a) Small labels*, $`\lvert\mathbf k\rvert<\delta`$. With $`\mathbf k=\mathbf p/\rho`$: $`\Omega_{\mathbf k}\lambda=w\sqrt{\mu^2+p^2}\,(1+O(p^2/\rho^2))`$ and $`\Omega_{\mathbf k}^{-2}=\rho^2c_0^{-2}(\mu^2+p^2)^{-1}(1+O(p^2/\rho^2))`$, so (4.10) and the static mark tend to $`\rho^{2-D}c_0^{-2}`$ times the integrals $`\int\mathrm d^Dp\,(2\pi)^{-D}e^{ip_1}\cos(w\sqrt{\mu^2+p^2})/(\mu^2+p^2)`$ at $`w`$ and at $`w=0`$. These are standard Fourier integrals of explicit functions (M5); in $`D=3`$ (value at unit distance) and in $`D=1`$ (derivative in the place at unit distance) they give the same ratio

```math
\Delta_\infty(w,\mu)=\begin{cases}-1, & w<1,\\[2pt] e^{\mu}-1-\mu e^{\mu}\,I_\mu\bigl(\mu\sqrt{w^2-1}\bigr), & w>1,\end{cases}\qquad I_\mu(Y)=\int_0^Y\frac{J_1(y)\,\mathrm dy}{\sqrt{y^2+\mu^2}} .
\qquad\text{(4.12)}
```

(In $`D=3`$, $`\partial_w`$ of the first integral is $`-(4\pi)^{-1}[\delta(w-1)-\theta(w-1)\,\mu J_1(\mu\sqrt{w^2-1})/\sqrt{w^2-1}]`$ and its value at $`w=0`$ is $`e^{-\mu}/(4\pi)`$; in $`D=1`$, $`\partial_w`$ of the place derivative is $`\tfrac12[\delta(w-1)-\theta(w-1)\,\mu J_1(\mu\sqrt{w^2-1})/\sqrt{w^2-1}]`$, starting from $`-e^{-\mu}/2`$; the substitution $`y=\mu\sqrt{w'^2-1}`$ gives $`I_\mu`$.) The lobes of $`J_1`$ between its zeros alternate in sign and decrease in weight against $`1/\sqrt{y^2+\mu^2}`$, so $`0\le I_\mu(Y)\le I_\mu(j_{1,1})<1.1`$ for all $`Y\ge0`$ (checked numerically for $`10^{-3}\le\mu\le1`$: $`\min I_\mu=0`$, $`\max I_\mu\le1.092`$). Writing $`\Delta_\infty=(e^\mu-1-\mu e^\mu)+\mu e^\mu(1-I_\mu)`$ and using $`0\le1-e^{\mu}(1-\mu)\le\mu^2e^\mu/2`$ and $`\lvert1-I_\mu\rvert\le1`$:

```math
\Delta_\infty(w,\mu)=-1\ \ (w<1),\qquad \lvert\Delta_\infty(w,\mu)\rvert\le\mu e^{\mu}\bigl(1+\tfrac{\mu}{2}\bigr)\ \ (w>1).
\qquad\text{(4.13)}
```

*(b) The rest of the zone.* For $`\lvert\mathbf k\rvert\ge\delta`$ the integrand is smooth in $`\mathbf k`$ and $`m_h`$, and the phases are $`\rho\,(k_1\pm(w/c_0)\Omega_{\mathbf k})`$. Let $`v_{\rm front}=\sup_{\mathbf k}\partial_{k_1}\hat K_0(\mathbf k)^{1/2}`$. For $`\rho/\lambda>v_{\rm front}`$ there is no stationary point and the contribution is $`O(\rho^{-\infty})`$; nondegenerate stationary points contribute $`O(\rho^{-D/2})`$ to $`u`$ and to $`\nabla u`$, i.e. $`O(\rho^{-1/2})`$ relative to the static value ($`\propto\rho^{-1}`$, $`D=3`$) or gradient ($`\propto\rho^0`$, $`D=1`$). **Caustic condition** (assumption, M8): the set of caustic values, the $`w`$ at which degenerate stationary points occur, is finite; each contributes $`O(\rho^{-1/3})`$ relative. It holds for the nearest-neighbour contract and for the control (4.16) (short argument). Both are separable, $`\hat K_0=\sum_ig(k_i)`$, with $`g'`$ vanishing only at $`k\in\{0,\pi\}`$ and $`g''\ne0`$ there ($`g'=2\kappa_h\sin k`$, resp. $`g'=\sin k\,(14-12\cos k)`$). Since $`\partial_{k_i}\Omega_{\mathbf k}=g'(k_i)/(2\Omega_{\mathbf k})`$, in $`D=3`$ the stationary points lie on the four branches $`k_2,k_3\in\{0,\pi\}`$, where the Hessian of $`\Omega`$ is diagonal with the nonzero entries $`g''(k_{2,3})/(2\Omega)`$ in $`k_2,k_3`$. They are degenerate only at the zeros of $`\partial_{k_1}^2\Omega`$ along a branch ($`D=1`$: the one branch). These are finitely many on $`\lvert\mathbf k\rvert\ge\delta`$, since there this function is analytic and not identically zero ($`\Omega`$ is periodic in $`k_1`$ and not constant). For the nearest-neighbour $`K`$ the caustic values are the front $`w=c_0/v_{\rm front}`$ and, in $`D=3`$, $`w\approx2.41`$ and $`3.15`$ (the group-velocity maxima of the branches). Near $`w=1`$ the $`O(\lvert\mathbf k\rvert^4)`$ term of $`\hat K_0`$ smooths the step of (4.12) over a window $`\lvert c_0\lambda-\rho\rvert=O(\rho^{1/3})`$, with a wake of relative size $`O(\rho^{-1/2}(w-1)^{-3/4})`$ beyond it (stationary phase near $`\mathbf k=0`$).

Hence, for every $`K`$ of the class that satisfies the caustic condition, under the stationary-phase estimates of (b), $`\Delta_D(\rho,\rho w/c_0)\to\Delta_\infty(w,\mu)`$ uniformly on $`w\ge1+\eta`$ and on $`w\le1-\eta`$ for every $`\eta>0`$, at the rate $`\rho^{-1/3}`$ at worst (for $`w\to\infty`$ the stationary-phase remainders decrease with $`\lambda`$, and $`\Delta_\infty\to0`$ since $`I_\mu(\infty)=(1-e^{-\mu})/\mu`$). With (4.13), for such $`K`$: for every $`\varepsilon\in(0,1)`$ and every $`\mu`$ with $`\mu e^\mu(1+\mu/2)<\varepsilon`$,

```math
\lim_{\rho\to\infty}\frac{c_0\,\lambda_{\rm form}(\rho;\varepsilon)}{\rho}=1,\qquad \lambda_{\rm form}(\rho;\varepsilon)-\frac{\rho}{c_0}=O(\rho^{1/3})\ \ \text{once the caustic wakes }O(\rho^{-1/3})\text{ are below }\varepsilon-\mu e^\mu(1+\tfrac{\mu}{2}) ,
\qquad\text{(4.14)}
```

on the ring ($`D=1`$) and on the cubic torus ($`D=3`$): the long-range part forms within a $`\lambda`$ linear in the distance, at the formation speed $`v_{\rm form}=c_0`$, independent of $`\varepsilon`$; for $`\lambda<(1-\eta)\rho/c_0`$ it has not formed ($`\Delta_D\to-1`$). The caustic condition is shown for the nearest-neighbour contract and for the control (4.16) (Step 6(b)); for other members of the class it is assumed.

### Step 7. Formation speed, slope and front

Let $`v_{\rm slope}=\sup_{\mathbf k}\lvert\nabla\hat K_0(\mathbf k)^{1/2}\rvert`$, the largest slope of the normal-mode frequencies (at $`m_h\to0`$, the regime of Step 6). Since $`c_0=\lim_{k_1\to0^+}\partial_{k_1}\hat K_0(k_1\mathbf e_1)^{1/2}`$,

```math
v_{\rm form}=c_0\ \le\ v_{\rm front}\ \le\ v_{\rm slope}.
\qquad\text{(4.15)}
```

The inequalities hold for every $`K`$ of the class; $`v_{\rm form}=c_0`$ holds under the conditions of (4.14) (caustic condition and the estimates of Step 6(b)). Under the same conditions the first change at $`\rho\mathbf e_1`$ arrives with $`v_{\rm front}`$ (Step 6(b): no stationary point for $`\rho/\lambda>v_{\rm front}`$); between $`\rho/v_{\rm front}`$ and $`\rho/c_0`$ the made field is a short-wavelength wake of relative size $`O(\rho^{-1/3})`$, not the long-range part. For the nearest-neighbour contract, $`\hat K_0=2\kappa_h\sum_i(1-\cos k_i)`$, $`\lvert\nabla\hat K_0^{1/2}\rvert^2=\kappa_h\sum_i\sin^2\tfrac{k_i}2\cos^2\tfrac{k_i}2/\sum_i\sin^2\tfrac{k_i}2\le\kappa_h`$, so $`c_0=v_{\rm front}=v_{\rm slope}=\sqrt{\kappa_h}`$: arrival and formation coincide, as in (8.15). **Control** (a member of the class with $`c_0\ne v_{\rm slope}`$):

```math
\hat K_0(\mathbf k)=\sum_{i}\bigl[14(1-\cos k_i)-3(1-\cos2k_i)\bigr]=\sum_i(1-\cos k_i)(8-6\cos k_i),\qquad c_0=1,\quad v_{\rm front}=v_{\rm slope}=2.475 ,
\qquad\text{(4.16)}
```

of range 2 along the axes, with the symmetries of the class and $`\hat K_0\ge2\sum_i(1-\cos k_i)`$; the speeds are computed by `code/v2/oscillator_formation.py`. There the first change runs ahead of the formation by the factor 2.475.

### Step 8. Speeds of bodies and field (item 4)

Let $`\ell_0`$ be the recorded distance of one step of the body's chain ($`\ell_0=\kappa\sigma_X`$ in the setting of (5.11)); by (5.11) $`v_{\max}=\tau\ell_0`$. By the coupling map (4.15) of 06-ilang-source/04-profile, one chain step is $`k`$ field steps along the ring (along a lattice axis of the tori, a stated assumption, M8), so one field step is the recorded distance $`\ell_0/k`$, and the formation speed $`c_0`$ (field steps per unit $`\lambda`$) is $`c_0\ell_0/k`$. Hence

```math
\frac{v_{\rm form}}{v_{\max}}=\frac{c_0}{k\,\tau},\qquad v_{\rm form}=v_{\max}\iff c_0=k\tau\quad(\text{nearest neighbour: }\sqrt{\kappa_h}=k\tau),
\qquad\text{(4.17)}
```

independent of $`\ell_0`$; the front moves at $`v_{\rm front}\ell_0/k\ge v_{\rm form}`$. Equality of the two speeds is a condition on the description (M7).

### Step 9. Numerical check (code)

Criterion (4.11) with $`\varepsilon=0.1`$; all numbers from `code/v2/output/`.

*(i) Oscillator cells* (`oscillator_formation.py`; $`c_0=1`$; ring $`L=4096`$, $`m_h=5\cdot10^{-5}`$; cubic torus $`L=256`$, $`m_h=2.5\cdot10^{-4}`$; so $`\mu\le0.026`$; windows end before the first image front). *Control (4.16):* $`c_0\lambda_{\rm form}/\rho=1.266,\,1.162,\,1.089,\,1.053,\,1.031,\,1.018`$ for $`\rho=16,32,\dots,512`$ ($`D=1`$) and $`1.344,\,1.191,\,1.154,\,1.082`$ for $`\rho=8,16,24,48`$ ($`D=3`$). The arrival ($`\eta=0.01`$) gives $`v_{\rm front}\lambda_{\rm arr}/\rho`$ from 0.890 to 0.991 ($`D=1`$) and from 0.665 to 0.872 ($`D=3`$). Between the arrival and $`w=0.8`$ the mean of $`\Delta_D`$ lies between $`-1.18`$ and $`-0.99`$: the change has arrived, the long-range part has not formed. *Nearest neighbour:* $`c_0\lambda_{\rm form}/\rho=2.47,\,1.72,\,1.43,\,1.26,\,1.16,\,1.13`$ ($`D=1`$, $`\rho=16,\dots,512`$), with $`(\lambda_{\rm form}-\rho/c_0)/\rho^{1/3}`$ between 6.4 and 9.3, bounded as (4.14) states. In $`D=3`$: $`3.94,\,3.64,\,3.72,\,3.14`$ for $`\rho=8,16,24,48`$, set by the caustic wakes at $`w\approx2.41,\,3.15`$. Their largest $`\lvert\Delta_3\rvert`$ on $`1.5\le w\le3`$ falls as $`0.238,\,0.197,\,0.178,\,0.130`$, i.e. as $`\rho^{-1/3}`$ (ratio 0.546 from $`\rho=8`$ to 48, against $`6^{-1/3}=0.550`$), and extrapolates below $`\varepsilon=0.1`$ at $`\rho\approx10^2`$. In short,

$$
\frac{c_0\lambda_{\rm form}}{\rho}\Big\vert_{\rm control}=1.018\ (D=1,\ \rho=512),\ \ 1.082\ (D=3,\ \rho=48);\qquad \frac{c_0\lambda_{\rm form}}{\rho}\Big\vert_{\rm n.n.}=1.13\ (D=1,\ \rho=512),\ \ 3.1\text{–}3.9\ (D=3,\ \rho\le48).
\tag{4.18}
$$ Static marks: relative deviation from the closed or Bessel form $`10^{-9}`$ ($`D=1`$) and $`4\cdot10^{-13}`$ ($`D=3`$). $`I_\mu`$: $`\min=0`$, $`\max\le1.092`$, $`\sup\lvert1-I_\mu\rvert=1`$ for $`\mu=10^{-3},\dots,1`$.

*(ii) Field of 06-ilang-source* (`conserved_density_formation.py`; $`t_f=1`$, infinite lattice). $`\lambda_{\rm form}/[\rho^2/(4\zeta(0.1))]`$ for $`\rho=4,8,16,32`$ ($`D=1`$): 1.69, 1.32, 1.15, 1.08; for $`\rho=4,8,12,16`$ ($`D=3`$): 0.965, 0.992, 0.997, 0.998; local exponents of $`\lambda_{\rm form}`$ in $`\rho`$: 1.90 ($`D=1`$, last two) and 2.006 ($`D=3`$). At $`\lambda=2\rho`$ the deviation is $`\Delta\approx-1`$ ($`-0.96`$ and $`-1.33`$ at the largest $`\rho`$): no linear formation, as (4.7)–(4.8) require.

## Result

Class F and its source and start as stated (Ω the nondegenerate lowest eigenvector of $`C_F`$), first order in $`g_s`$ throughout.

- **(4.1), (4.2)** (formula; every $`L`$, every $`\lambda\ge0`$): the made field and its label components in the eigenvectors of $`C_F`$; the static mark is the same with $`g_\lambda(\omega)\to1/\omega`$.
- **(4.3)** (definition): the sum-rule weight $`f_A(\mathbf q)`$ and the static self-response $`\chi_Y(\mathbf q)`$, fixed by $`C_F`$, the read or source operator and Ω; $`\delta a^{\rm st}_{\mathbf q}=-\chi_A(\mathbf q)`$ for $`B=A`$.
- **(4.4)** (theorem, item 1): $`\lvert\delta a_{\mathbf q}(\lambda)\rvert\le\min\{\lambda\sqrt{f_A\chi_B},\,2\sqrt{\chi_A\chi_B}\}`$ for every $`\mathbf q`$, $`L`$ and $`\lambda\ge0`$; for $`B=A`$, $`\lvert\delta a_{\mathbf q}(\lambda)/\delta a^{\rm st}_{\mathbf q}\rvert\le\lambda\sqrt{f_A/\chi_A}`$. It holds for the nondegenerate highest eigenvector with $`\lvert f_A\rvert,\lvert\chi\rvert`$.
- **(4.5)** (theorem): if $`A`$ is the density of a number $`N`$ conserved by every term of $`C_F`$, with $`[A_x,A_y]=0`$, then $`f_A(\mathbf q)\le c_A\lvert\mathbf q\rvert^2`$ for every $`L`$, with $`c_A`$ fixed by $`C_F`$ and $`A`$.
- **(4.6)** (theorem): under (4.5), for every source operator $`B`$, formation of the label component $`\mathbf q`$ to accuracy $`\varepsilon`$ needs $`\lambda\ge(1-\varepsilon)\lvert\delta a^{\rm st}_{\mathbf q}\rvert/(\lvert\mathbf q\rvert\sqrt{c_A\chi_B(\mathbf q)})`$.
- **(4.7)** (negative, item 2, $`B=A`$): with a long-range mark $`\lvert\delta a^{\rm st}_{\mathbf q}\rvert\ge s_0/\lvert\mathbf q\rvert^2`$ ($`\lvert\mathbf q\rvert\le q_1`$), $`\lambda_{\rm form}(\mathbf q;\varepsilon)\ge(1-\varepsilon)\sqrt{s_0/c_A}\,\lvert\mathbf q\rvert^{-2}`$: the long-range part of a conserved density cannot form within a $`\lambda`$ linear in the distance; also for the highest eigenvector.
- **(4.8)** (negative, position form, $`B=A`$, cubic torus, $`L\to\infty`$ then $`\ell\to\infty`$): if moreover $`\chi_A\le s_1/\lvert\mathbf q\rvert^2`$ and $`\delta a_{\rm st}=s/\lvert x\rvert+o(\lvert x\rvert^{-1})`$, formation at every place of the shell $`\ell\le\lvert x\rvert\le2\ell`$ needs $`\lambda\ge C\ell^2(1+o(1))`$, $`C>0`$ given in (4.8).
- **(4.9)** (negative, item 2, $`B\ne A`$, several kinds of objects included; under (4.5), with a long-range mark): formation within $`\lambda\le\beta/\lvert\mathbf q\rvert`$ at long-range labels requires $`\chi_B(\mathbf q)\ge(1-\varepsilon)^2s_0^2/(\beta^2c_A\lvert\mathbf q\rvert^4)`$, so it is excluded for every $`B`$ with $`\lvert\mathbf q\rvert^4\chi_B(\mathbf q)\to0`$. For every $`B`$ of the class of the question's note (a), $`\chi_B\le s_B/\lvert\mathbf q\rvert^2`$, $`\lambda_{\rm form}(\mathbf q;\varepsilon)\ge(1-\varepsilon)s_0/(\sqrt{c_As_B}\,\lvert\mathbf q\rvert^2)`$ for $`\lvert\mathbf q\rvert\le q_1`$: the long-range part of a conserved density cannot form within a $`\lambda`$ linear in the distance; also for the highest eigenvector. Sources with a stronger self-response are out of scope (note (a)). Control: oscillator cells with $`A=B=q_x`$, where $`f_A=1`$.
- **(4.10)** (formula, oscillator class, $`M\to\infty`$ then $`L\to\infty`$): exact made field $`\delta a_{\mathbf k}(\lambda)=-(1-\cos\Omega_{\mathbf k}\lambda)/\Omega_{\mathbf k}^2`$ and its deviation from the static mark.
- **(4.11)** (definition): the formation criterion along an axis (value ratio in $`D=3`$, difference ratio in $`D=1`$), $`\lambda_{\rm form}(\rho;\varepsilon)`$ and $`\lambda_{\rm arr}(\rho;\eta)`$.
- **(4.12), (4.13)** (formula, theorem; scaling limit $`\rho\to\infty`$ at fixed $`w=c_0\lambda/\rho`$, $`\mu=m_h\rho/c_0`$): $`\Delta_D\to\Delta_\infty(w,\mu)`$, equal to $`-1`$ for $`w<1`$ and bounded by $`\mu e^\mu(1+\mu/2)`$ for $`w>1`$, in $`D=1`$ and $`D=3`$.
- **(4.14)** (theorem, item 3, on the ring ($`D=1`$) and the cubic torus ($`D=3`$); the square torus is out of scope by note (b)): for every $`K`$ of the class with a finite caustic set (the caustic condition), under the stationary-phase estimates of Step 6(b), for every $`\varepsilon\in(0,1)`$ and $`\mu e^\mu(1+\mu/2)<\varepsilon`$, $`c_0\lambda_{\rm form}(\rho;\varepsilon)/\rho\to1`$: the long-range part forms within a $`\lambda`$ linear in the distance, at the speed $`c_0`$, independent of $`\varepsilon`$; the lattice correction is $`O(\rho^{1/3})`$ in $`\lambda`$ once the caustic wakes, $`O(\rho^{-1/3})`$ relative in $`D=3`$, are below $`\varepsilon-\mu e^\mu(1+\mu/2)`$. The caustic condition is shown for the nearest-neighbour contract (caustic values: the front and, in $`D=3`$, $`w\approx2.41`$ and $`3.15`$) and for the control (4.16), and assumed for the other members. Order: $`g_s\to0`$, $`M\to\infty`$, $`L\to\infty`$, $`\rho\to\infty`$, then $`\mu`$ small.
- **(4.15)** (theorem): $`c_0\le v_{\rm front}\le v_{\rm slope}`$ for every $`K`$ of the class; under the conditions of (4.14), $`v_{\rm form}=c_0`$ and the first change arrives with $`v_{\rm front}`$; for the nearest-neighbour contract all three equal $`\sqrt{\kappa_h}`$.
- **(4.16)** (example, control of item 3): $`\hat K_0=\sum_i(1-\cos k_i)(8-6\cos k_i)`$ is in the class with $`c_0=1<v_{\rm front}=v_{\rm slope}=2.475`$.
- **(4.17)** (formula, item 4, ring, or a lattice axis of the tori by assumption): $`v_{\rm form}/v_{\max}=c_0/(k\tau)`$; the two speeds are equal if and only if $`c_0=k\tau`$.
- **(4.18)** (numerical, Step 9, $`\varepsilon=0.1`$): for the control (4.16), $`c_0\lambda_{\rm form}/\rho`$ tends to 1 (1.018 at $`\rho=512`$, $`D=1`$; 1.082 at $`\rho=48`$, $`D=3`$), and the arrival tends to $`\rho/v_{\rm front}`$. For the nearest-neighbour $`K`$, $`c_0\lambda_{\rm form}/\rho=1.13`$ at $`\rho=512`$ ($`D=1`$), and between 3.1 and 3.9 in $`D=3`$ at $`\rho\le48`$, set by caustic wakes that decay as $`\rho^{-1/3}`$. For the field of 06-ilang-source, $`4\zeta(0.1)\lambda_{\rm form}/\rho^2`$ tends to 1 (1.08 at $`\rho=32`$, $`D=1`$; 0.998 at $`\rho=16`$, $`D=3`$).

## Consistency checks

1. **Dimensions.** $`g_sB`$ is a rate, so $`\delta a`$ per unit $`g_s`$ has the units $`[A][B][\lambda]`$; $`f_A\sim[A]^2/[\lambda]`$ and $`\chi_B\sim[B]^2[\lambda]`$, so both bounds of (4.4) and (4.6) are consistent; $`c_0`$ is in field steps per unit $`\lambda`$ and $`\tau`$ is a rate, so (4.17) is a pure number.
2. **(8.10), (8.14) as a special case.** For the field of 06-ilang-source with one field object ($`n=1/\lvert X_f\rvert`$) and $`A=B=\Phi`$, (4.2) gives one mode per label, $`\delta a_{\mathbf q}(\lambda)/\delta a^{\rm st}_{\mathbf q}=1-\cos\omega_{\mathbf q}\lambda\le\lambda\omega_{\mathbf q}`$, which is (4.4) with $`f_A=2n\omega_{\mathbf q}\le2nt_f\lvert\mathbf q\rvert^2`$ (4.5); (4.7) then gives a $`\lambda`$ quadratic in the distance, as (8.10) and (8.14). The code reproduces $`\lambda_{\rm form}\to\rho^2/(4t_f\zeta)`$ with $`\zeta(0.1)=0.01555`$, against $`\zeta_1=\pi\varepsilon^2/2=0.01571`$ of (8.10) (Step 9).
3. **(8.15) as a special case.** For the nearest-neighbour contract in $`D=3`$ with the value criterion, $`c_0=\sqrt{\kappa_h}`$, $`w=c`$ and $`\mu=m_Y\rho`$; (4.13) gives $`\lvert\Delta\rvert\le\mu e^\mu(1+\mu/2)`$ for $`c>1`$, the same order $`O(m_Y\rho)`$ as the bound $`8.4\,m_Y\rho`$ of (8.15), and the remainder $`O(\rho^{-1/2})`$ of nondegenerate stationary points matches $`o(1)=O(\rho^{-1/2})`$ for $`1<c<2`$, below the first caustic at $`c\approx2.41`$.

## Open issues

- Item 2, position form: derived for formation on a whole shell (4.8); for a single place, only for the field of 06-ilang-source ((8.14) and the code).
- Item 3: the remainder estimates of Step 6(b) are stationary-phase estimates; the caustic condition is shown here only for the nearest-neighbour contract and (4.16), and is an assumption of (4.14) for the other members of the class.
- Item 3: the approach to $`v_{\rm form}=c_0`$ is slow when the front coincides with $`c_0`$ (nearest neighbour), through the $`O(\rho^{1/3})`$ window and, in $`D=3`$, the caustic wakes; at the distances computed in $`D=3`$ ($`\rho\le48`$), $`\lambda_{\rm form}`$ is still 3 to 4 times $`\rho/c_0`$ there.
- Item 1 for eigenvectors inside the spectrum: (4.4) holds with $`\sum_n\lvert\omega_n\rvert(\dots)`$ in place of $`f_A`$, but (4.5) does not apply.
- Item 4 on the tori rests on the assumption that the coupling map runs along a lattice axis.

## Code

- `code/v2/oscillator_formation.py` (check, items 3 and 4's speeds; unchanged from v1, run again): exact made field (4.10) on a ring ($`L=4096`$) and a cubic torus ($`L=256`$), static mark on the infinite lattice by its Laplace representation (cross-checked against the closed form or Bessel form for the nearest-neighbour $`K`$), criterion (4.11) with $`\varepsilon=0.1`$, $`\eta=0.01`$, for the nearest-neighbour $`K`$ and the control (4.16); speeds $`c_0`$, $`v_{\rm front}`$, $`v_{\rm slope}`$; the bounds on $`I_\mu`$ used in (4.13). Output: `code/v2/output/oscillator_formation.json`.
- `code/v2/conserved_density_formation.py` (check, item 2; unchanged from v1, run again): the field of 06-ilang-source with one field object, $`A=B=\Phi`$, on the infinite chain and cubic lattice (Bessel-function forms of (4.1)), criterion (4.11) with $`\varepsilon=0.1`$, against the continuum prediction $`\rho^2/(4t_f\zeta(\varepsilon))`$. Output: `code/v2/output/conserved_density_formation.json`.

## Methods used

- first-order (Duhamel) perturbation, spectral representation
- sum rule of a double commutator, Cauchy–Schwarz inequality
- translation covariance, Fourier series on tori, Parseval
- Fourier integrals with Bessel functions, stationary phase, scaling limits
- exact equations of the means for a quadratic contract
- numerical lattice sums and Bessel-function integrals (Python)
