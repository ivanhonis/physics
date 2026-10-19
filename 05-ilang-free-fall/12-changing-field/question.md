# Question: 12-changing-field

- **Subproject:** 05-ilang-free-fall
- **Package:** 12-changing-field
- **Equation tags:** (12.k)
- **Created:** 2026-10-11

## Goal

Determine what a body sees when the field is not stationary, so that the factor it produces changes with $`\lambda`$: through which quantities of the field the body depends on it at first order, how the body falls in a gradient that changes with $`\lambda`$, and under which condition this fall is the same for all clock levels. This is the third part of criterion 8.

**Setting.**
- **Objects.** A body $`b`$, a field $`f`$ and a recording medium $`c`$, of pairwise different types, one instance each.
- **Contract.** In the order $`b`$, $`f`$, $`c`$:
  ```math
  C=C_{\rm D}\otimes\mathbb 1_f\otimes\mathbb 1_c+\bigl(\hat x\otimes G\bigr)\otimes Y\otimes\mathbb 1_c+\mathbb 1_b\otimes C_f\otimes\mathbb 1_c+\sum_x\lvert x\rangle\langle x\rvert\otimes\mathbb 1_f\otimes\kappa\,x\,X,\qquad G:=\sigma_3\otimes(m\mathbb 1_N+D),
  ```
  with $`C_{\rm D}`$ the contract of Model D on the chain $`\lvert x\rvert\le L`$ ($`x\in\mathbb Z`$ as the limit of long chains, A1), $`\hat x:=\sum_xx\,\lvert x\rangle\langle x\rvert`$, and self-adjoint operators $`Y`$ (the **gradient operator**) and $`C_f`$ on a finite-dimensional $`\mathcal H_f`$, $`\lVert Y\rVert(L+1)<1`$. This is the lapse-type pair term of the base problem with the factor $`\Phi_x=\mathbb 1_f+x\,Y`$ on the rest and clock term $`\sum_x\lvert x\rangle\langle x\rvert\otimes G`$; the motion term carries no factor. $`C`$ is the contract (2.1) with $`r=\{c\}`$. $`Y`$ need not commute with $`C_f`$. The form of the contract is an assumption of this package (M8).
- **Start of the field.** Any unit vector $`\varphi`$ of $`\mathcal H_f`$; the start is $`\Psi_0=\phi\otimes\varphi\otimes\chi`$, with $`\phi`$ a start of the body and $`\chi`$ the state of the medium, $`\sigma_X>0`$. Named cases: *sharp and stationary*, $`Y\varphi=\gamma\varphi`$ and $`C_f\varphi=e_f\varphi`$; *sharp and not stationary*, $`Y\varphi=\gamma\varphi`$ while (2.11) fails; *not sharp*. No state of the field is preferred (A11).
- **The gradient seen at $`\lambda`$.** $`\gamma(\lambda):=\langle\varphi\vert e^{iC_f\lambda}\,Y\,e^{-iC_f\lambda}\vert\varphi\rangle`$. The **field frequencies** are the differences $`e-e'`$ of eigenvalues of $`C_f`$.
- **Levels, branches and branch starts.** $`d_k:=\frac{2\pi k}{N\lambda_0}`$, $`M_k:=m+d_k`$. On the clock level $`k`$ the contract of Model D acts as the block (5.5) of 04-ilang-time/05-moving-clock, with the eigenvalues $`\pm\omega_k(p)`$ and the eigenvectors $`\beta_{k,\pm}(p)`$ of (5.6) of 04-ilang-time/05-moving-clock. For a level $`k`$, a branch $`\sigma\in\{+,-\}`$ and a smooth $`2\pi`$-periodic function $`g`$ with $`\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g\rvert^2=1`$, the **branch start** $`B_{k,\sigma}[g]`$ is
  ```math
  \lvert\phi\rangle=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\,g(p)\,\lvert p\rangle\otimes\beta_{k,\sigma}(p)\otimes\lvert f_k\rangle
  ```
  on the infinite chain. $`\langle F\rangle_g:=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g(p)\rvert^2F(p)`$. The start is **concentrated at $`p_0`$** with the spread $`\delta p`$ if, on the arc $`(p_0-\pi,p_0+\pi]`$, the weight $`\lvert g\rvert^2\frac{\mathrm dp}{2\pi}`$ has the mean $`p_0`$ and the variance $`\delta p^2`$; it is **at rest** if $`p_0=0`$. A **sharp-label limit** is a limit along a sequence of such starts with $`\delta p\to0`$; the package names the class of sequences for which each limit is taken.
- **Orders.** "First order in the field" means first order in $`Y`$, at fixed $`\lambda`$, fixed start and fixed chain, followed by the limit of a long chain. The mean position label is $`\bar x_{\rm lab}(\lambda):=\sum_xx\,p_x(\lambda)`$, with $`p_x`$ the place weights of the view of the body. Records: the weak-record regime, $`\kappa\to0`$ at fixed $`\lambda`$, chain and start, with the term $`\kappa\,x\,\langle X\rangle`$ counted as a plain gradient of the effective body contract, as in 04-branch-fall; in items 2–4 set $`\langle X\rangle=0`$.

1. **First order in the field.** For every $`C_f`$, $`Y`$, $`\varphi`$ and every start $`\phi\otimes\varphi\otimes\chi`$:
   - (a) Determine through which functions of $`(\varphi,C_f,Y)`$ the first-order term of the view of $`\{b,c\}`$, and of the statistics of every schedule of readings on $`b`$ and $`c`$, depends on the field.
   - (b) Give the generator on $`\mathcal H_b\otimes\mathcal H_c`$, depending on $`\lambda`$, that reproduces this first-order term, and state whether it is the contract of an admissible description (A5). State what (a) becomes for a sharp and stationary field, by (2.3), and for a field with (2.11), by (2.12).
   - (c) State, from (2.14) and from the first-order result, at which order in $`Y`$ and in $`\lambda`$ the view of $`\{b,c\}`$ first differs from the one produced by the generator of (b), for a sharp start that is not stationary.

2. **Fall in a gradient that changes with $`\lambda`$.** For a branch start $`B_{k,\sigma}[g]`$ of Model D:
   - (a) Determine the first-order velocity of the mean position label as a functional of $`\gamma(\cdot)`$ on $`[0,\lambda]`$, with its kernel given as an average $`\langle\cdot\rangle_g`$ of an explicit function of $`p`$. Check it against (4.7) for a constant $`\gamma`$ (there $`G_k=\gamma M_k`$, $`\mathcal F_k=0`$, $`g_{\zeta,k}=0`$).
   - (b) For starts at rest, in a sharp-label limit: determine the kernel in closed form, and the first-order velocity and acceleration for $`\gamma(\lambda)=\gamma_0+\gamma_1\cos(\Omega\lambda+\vartheta)`$ with real $`\gamma_0`$, $`\gamma_1`$, $`\vartheta`$ and $`\Omega>0`$. Separate the part that oscillates with the frequency $`\Omega`$ of the field, the parts that oscillate with other frequencies, and any part that grows with $`\lambda`$. State the order of the limits used.

3. **Independence of the clock level.**
   - (a) For $`\Omega\neq2M_k`$: determine the complex number $`\mathcal A_{k,\sigma}(\Omega)`$ for which the part of the first-order acceleration of item 2(b) that oscillates with the frequency $`\Omega`$ is $`\mathrm{Re}\bigl[\mathcal A_{k,\sigma}(\Omega)\,\gamma_1e^{i(\Omega\lambda+\vartheta)}\bigr]`$. Determine its value for $`\Omega\to0`$ and compare it with (4.16); determine the necessary and sufficient condition under which $`\mathcal A_{k,\sigma}(\Omega)`$ is the same for all levels, and its leading dependence on the level for $`\Omega\ll2M_k`$.
   - (b) For $`\Omega=2M_k`$: determine how the first-order velocity grows with $`\lambda`$, and what distinguishes this level from the others.
   - (c) State for which field frequencies, relative to the level data, the fall in the field is the same for all levels to a given relative accuracy $`\delta`$, and which statement replaces "the fall is the same for all levels" for a general $`\gamma(\lambda)`$.

4. **Example and controls.** A field with two places $`\lvert0\rangle`$, $`\lvert1\rangle`$, $`Y=y\,\lvert1\rangle\langle1\rvert`$ with a real number $`y`$, $`C_f=\gamma_f\bigl(\lvert0\rangle\langle1\rvert+\lvert1\rangle\langle0\rvert\bigr)`$ with $`\gamma_f\neq0`$, and $`\varphi=\lvert0\rangle`$: the field (2.13) coupled as a gradient.
   - (a) Determine $`\gamma(\lambda)`$ and evaluate items 2(b) and 3 for it.
   - (b) Controls: a sharp and stationary field (state what items 2 and 3 reduce to); a field with $`[Y,C_f]=0`$ that is not sharp (state $`\gamma(\lambda)`$ and which of the results of this package describe it, and which do not).

5. **Summary.** State in a table, for each of: the factor that the body sees; the drift acceleration from rest; its independence of the clock level: what a field that is not stationary changes, at which order in $`Y`$, and for which field frequencies, with the tags of the results used.

## Inputs

From 02-field-object@v2 (this subproject). Setting there: a body $`b`$, a field $`f`$ and a set $`r`$ of further objects (possibly empty), of pairwise different types, $`\mathcal H=\mathcal H_{br}\otimes\mathcal H_f`$ with $`\mathcal H_{br}:=\mathcal H_b\otimes\mathcal H_r`$; $`C_{br}`$ is a sum of pair terms among $`b`$ and the objects of $`r`$, $`C_f`$ is self-adjoint on $`\mathcal H_f`$, and $`B_j`$ (on $`\mathcal H_b`$), $`\Phi_j`$ (on $`\mathcal H_f`$), $`j\in J`$, are finite families of self-adjoint operators; $`B_j`$ also denotes $`B_j\otimes\mathbb 1_r`$. The start is $`\Psi_0=\Psi_{br}\otimes\varphi`$ and $`\lambda\ge0`$; $`V(\lambda)`$ is the view of $`\{b\}\cup r`$. A field state $`\varphi`$ is **sharp** if $`\Phi_j\varphi=n_j\varphi`$ for all $`j`$, with real numbers $`n_j`$. A **schedule** consists of readings with projectors $`\Pi_i\otimes\mathbb 1_f`$ at $`0\le\lambda_1\le\dots\le\lambda_k`$, where $`\Pi_i`$ is diagonal in the joint places of $`b`$ and $`r`$; $`p(r_1,\dots,r_k)`$ is the joint distribution of its outcomes.

Eq. (2.1) of 02-field-object, the contract:

```math
C=C_{br}\otimes\mathbb 1_f+\sum_{j\in J}B_j\otimes\mathbb 1_r\otimes\Phi_j+\mathbb 1_{br}\otimes C_f
```

Eq. (2.3) of 02-field-object, for a field state with $`\Phi_j\varphi=n_j\varphi`$ and $`C_f\varphi=e_f\varphi`$ (sharp and stationary), and every $`\Psi\in\mathcal H_{br}`$:

```math
C\,(\Psi\otimes\varphi)=\bigl((C_{\rm red}+e_f)\Psi\bigr)\otimes\varphi,\qquad C_{\rm red}:=C_{br}+\sum_{j\in J}n_j\,B_j\otimes\mathbb 1_r .
```

Eq. (2.11) of 02-field-object. Let $`\varphi`$ be sharp with the numbers $`n_j`$, and let $`\mathbb 1_b`$ and the $`B_j`$ be linearly independent. The view $`V(\lambda)`$ is pure for every $`\Psi_{br}`$ and every $`\lambda\ge0`$ if and only if

```math
\Phi_j\,C_f^{\,k}\,\varphi=n_j\,C_f^{\,k}\,\varphi\qquad\text{for all } j\in J \text{ and all } k\ge0 .
```

Eq. (2.12) of 02-field-object. If (2.11) holds (linear independence is not needed), then with $`C_{\rm red}`$ of (2.3), $`\Psi_{\rm red}(\lambda):=e^{-iC_{\rm red}\lambda}\Psi_{br}`$ and $`V_f`$ the view of $`\{f\}`$:

```math
\Psi(\lambda)=\Psi_{\rm red}(\lambda)\otimes e^{-iC_f\lambda}\varphi,\qquad V(\lambda)=\lvert\Psi_{\rm red}(\lambda)\rangle\langle\Psi_{\rm red}(\lambda)\rvert,\qquad V_f(\lambda)=\lvert e^{-iC_f\lambda}\varphi\rangle\langle e^{-iC_f\lambda}\varphi\rvert .
```

Eq. (2.13) of 02-field-object, an example: a field with two places $`\lvert0\rangle`$, $`\lvert1\rangle`$, one index, and $`\gamma\neq0`$; $`\varphi`$ is sharp and (2.11) fails at $`k=1`$:

```math
\Phi_1=\lvert1\rangle\langle1\rvert,\qquad C_f=\gamma\bigl(\lvert0\rangle\langle1\rvert+\lvert1\rangle\langle0\rvert\bigr),\qquad \varphi=\lvert0\rangle:\qquad n_1=0,\qquad \omega_1^{(1)}=\Phi_1C_f\varphi=\gamma\lvert1\rangle\neq0 .
```

Eq. (2.14) of 02-field-object, for every sharp $`\varphi`$, every contract of the form (2.1) and every start $`\Psi_{br}`$, as an expansion for $`\lambda\to0`$ at fixed operators and start:

```math
1-\mathrm{Tr}V(\lambda)^2=\frac{\lambda^4}{2}\sum_{j,j'\in J}\Gamma_{jj'}\,\bigl\langle C_f\varphi\bigm\vert(\Phi_j-n_j)(\Phi_{j'}-n_{j'})\bigm\vert C_f\varphi\bigr\rangle+O(\lambda^5),\qquad \Gamma_{jj'}=\langle B_jB_{j'}\rangle_{\Psi_{br}}-\langle B_j\rangle_{\Psi_{br}}\langle B_{j'}\rangle_{\Psi_{br}} .
```

From 05-moving-clock@v3 of 04-ilang-time. Setting there: one Model D body with the contract $`C_b=C_{\rm D}`$ of the base problem, the records $`K_x=\kappa xX`$ and the start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`d_k:=\frac{2\pi k}{N\lambda_0}`$; the plane waves $`\lvert p\rangle=\sum_xe^{ipx}\lvert x\rangle`$, $`p\in(-\pi,\pi]`$.

Eq. (5.5) of 04-ilang-time/05-moving-clock:

```math
C_b\bigl(\lvert p\rangle\otimes\beta\otimes\lvert f_k\rangle\bigr)=\lvert p\rangle\otimes C_k(p)\beta\otimes\lvert f_k\rangle,\qquad C_k(p):=-\tau\sin p\,\sigma_1+\mu_k\sigma_3,\qquad\mu_k:=m+d_k .
```

Eq. (5.6) of 04-ilang-time/05-moving-clock, the eigenvalues $`\pm\omega_k(p)`$ and the real eigenvectors $`\lvert p\rangle\otimes\beta_{k,\pm}(p)\otimes\lvert f_k\rangle`$ of $`C_b`$:

```math
\omega_k(p)=\sqrt{\mu_k^2+\tau^2\sin^2p},\quad
\beta_{k,+}=\begin{pmatrix}\cos\frac{\theta_k}2\\ \sin\frac{\theta_k}2\end{pmatrix},\quad
\beta_{k,-}=\begin{pmatrix}-\sin\frac{\theta_k}2\\ \cos\frac{\theta_k}2\end{pmatrix},\quad
\tan\theta_k(p)=-\frac{\tau\sin p}{\mu_k},\ \ \lvert\theta_k\rvert<\frac\pi2 .
```

Eq. (5.11) of 04-ilang-time/05-moving-clock, the bound (17.7) of 03-ilang-space/17-motion for this $`C_b`$ (the maximal speed):

```math
v_{\max}=\tau\,\kappa\sigma_X=\max_h\sum_{h'}\lvert t_{hh'}\rvert\,d_0(h,h') .
```

From 08-maximal-speed@v3 of 04-ilang-time. Setting there: two bodies $`a`$, $`b`$ of different types and a medium $`c`$, with body contracts $`C_A`$, $`C_B`$ (diagonal entries $`t^A_{hh}`$, $`t^B_{kk}`$) and records $`K^A_h`$, $`K^B_k`$; the start is a product with the medium in $`\chi`$.

Eq. (8.1) of 04-ilang-time/08-maximal-speed, all replacements of the diagonal entries of the body contracts and of the records that leave the total contract unchanged, with arbitrary real $`\alpha^A_h`$, $`\alpha^B_k`$ and an arbitrary self-adjoint $`Z`$ on $`\mathcal H_c`$:

```math
t'^A_{hh}=t^A_{hh}+\alpha^A_h,\quad K'^A_h=K^A_h+Z-\alpha^A_h\mathbb 1_c,\qquad
t'^B_{kk}=t^B_{kk}+\alpha^B_k,\quad K'^B_k=K^B_k-Z-\alpha^B_k\mathbb 1_c ,
```

Eq. (8.19) of 04-ilang-time/08-maximal-speed, the effective body contracts:

```math
C^{\rm eff}_A\otimes\mathbb 1_b+\mathbb 1_a\otimes C^{\rm eff}_B:=(\mathbb 1_{ab}\otimes\langle\chi\rvert)\,C\,(\mathbb 1_{ab}\otimes\lvert\chi\rangle),\qquad
C^{\rm eff}_A=C_A+\sum_h\langle K^A_h\rangle\lvert h\rangle\langle h\rvert,\quad
C^{\rm eff}_B=C_B+\sum_k\langle K^B_k\rangle\lvert k\rangle\langle k\rvert .
```

Eq. (8.20) of 04-ilang-time/08-maximal-speed:

```math
\text{(8.1):}\quad C^{\rm eff}_A\mapsto C^{\rm eff}_A+\langle Z\rangle\,\mathbb 1_a,\quad C^{\rm eff}_B\mapsto C^{\rm eff}_B-\langle Z\rangle\,\mathbb 1_b;\qquad \chi\mapsto e^{i\theta}\chi:\quad C^{\rm eff}_A,\ C^{\rm eff}_B\ \text{unchanged}.
```

From 04-branch-fall@v3 (this subproject). Setting there: a body with the places of Model D and a conserved clock level, whose level blocks are $`C^{(k)}=\frac{\tau_k}2\sum_x\zeta_{x,k}\bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\bigr)+\sum_x\lvert x\rangle\langle x\rvert\otimes\bigl(M_{x,k}\sigma_3+V_{x,k}\mathbb 1_2\bigr)`$ with the linear level profiles $`M_{x,k}=M_k+G_kx`$, $`V_{x,k}=-\mathcal F_kx`$, $`\zeta_{x,k}=1+g_{\zeta,k}(x+\tfrac12)`$ and contracts that do not depend on $`\lambda`$; a medium with the records $`K_x=\kappa\,x\,X`$; branch starts $`B_{k,\sigma}[g]`$ as under "Goal" (with $`\tau\to\tau_k`$); first order in the gradients $`G_k`$, $`\mathcal F_k`$, $`g_{\zeta,k}`$ of the level $`k`$, at fixed $`\lambda`$, start and chain, followed by the limit of a long chain; records at leading order in $`\kappa`$. Model D is the member $`\tau_k=\tau`$, $`M_k=m+d_k`$ with all gradients zero. Inside one level the index $`k`$ is dropped: $`\tau,M,G,\mathcal F,g_\zeta,\omega`$; a prime is $`\partial_p`$; $`\mathsf b:=\lvert G\rvert+M\lvert g_\zeta\rvert+\lvert\mathcal F\rvert`$; $`X_g:=\bigl(\int\frac{\mathrm dp}{2\pi}\lvert g'\rvert^2\bigr)^{1/2}`$. The **drift acceleration** $`a_{k,\sigma}(p_0)`$ is the first-order acceleration of $`\bar x_{\rm lab}`$, averaged over a long window, followed by the limit of a sharp label.

Eq. (4.2) of 04-branch-fall, the level block for the linear level profiles on the infinite chain, exactly ($`\hat x=i\partial_p`$ on plane-wave amplitudes):

```math
C^{(k)}=C_0+C_1,\quad C_0=-\tau\sin\hat p\,\sigma_1+M\sigma_3,\quad C_1=\tfrac12\{\hat x,B(\hat p)\},\quad B(p)=-g_\zeta\tau\sin p\,\sigma_1+G\sigma_3-\mathcal F .
```

Eq. (4.5) of 04-branch-fall, the velocity of $`B_{k,\sigma}[g]`$ at zero gradients, exactly:

```math
v^{(0)}(\lambda)=\sigma\,\langle\omega_k'\rangle_g\qquad(\text{constant in }\lambda).
```

Eq. (4.7) of 04-branch-fall. The first-order velocity of $`B_{k,\sigma}[g]`$ is $`\lambda\,\langle a_{k,\sigma}\rangle_g`$ plus a rest that is bounded for all $`\lambda\ge0`$, with the coefficient

```math
\boxed{\;a_{k,\sigma}(p)=\frac{g_{\zeta,k}\tau_k^4\sin^2p-G_kM_k\tau_k^2\cos2p}{\omega_k^2}+\sigma\,\mathcal F_k\,\frac{\tau_k^2\bigl(M_k^2\cos2p-\tau_k^2\sin^4p\bigr)}{\omega_k^3}\;},\qquad\lvert a_{k,\sigma}(p)\rvert\le\frac{\tau_k^2}{M_k}\,\mathsf b_k .
```

Eq. (4.10) of 04-branch-fall, with $`a^{(1)}(\lambda)`$ the first-order acceleration of $`\bar x_{\rm lab}`$ and $`\overline{a^{(1)}}`$ its average over a window $`[\lambda_1,\lambda_1+\Lambda]`$, for all $`\lambda_1\ge0`$, $`\Lambda>0`$ and every smooth $`g`$:

```math
\Bigl\lvert\overline{a^{(1)}}-\langle a_{k,\sigma}\rangle_g\Bigr\rvert\le\frac{2\tau}{M\Lambda}\,\mathsf b\,\Bigl(X_g+\frac{\tau}{2M}\Bigr)\ \ (\text{exact}),\qquad\lim_{\Lambda\to\infty}\overline{a^{(1)}}=\langle a_{k,\sigma}\rangle_g .
```

Eq. (4.11) of 04-branch-fall, for every sequence of branch starts concentrated at $`p_0`$ with $`\delta p\to0`$:

```math
\bigl\lvert\langle a_{k,\sigma}\rangle_g-a_{k,\sigma}(p_0)\bigr\rvert\le\tfrac12\sup_p\lvert a_{k,\sigma}''\rvert\,\delta p^2\ \ (\text{exact}),\qquad\text{drift acceleration}=\lim_{\delta p\to0}\lim_{\Lambda\to\infty}\overline{a^{(1)}}=a_{k,\sigma}(p_0).
```

Eq. (4.16) of 04-branch-fall, the drift acceleration at rest:

```math
\boxed{\;a_{k,\sigma}(0)=\frac{\tau_k^2}{M_k}\,\bigl(\sigma\,\mathcal F_k-G_k\bigr)\;}
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$; the dependence on $`\lambda`$ of what the body sees comes from the state of the field alone.
- The three types are pairwise different and each has one instance, so no swap condition applies.
- The form of the contract, the product start and the branch starts are assumptions of this package (M8, M9). The results are asked for every $`\varphi`$, through $`\gamma(\lambda)`$ (A11).
- Standard first-order perturbation theory in a term of the contract, and standard facts on plane waves and on the averaging of oscillating terms, may be used; state them with their conditions.
- Every limit is stated with its order: the limit of a sharp label, an average over a window, the growth of $`\lambda`$ and the expansion parameters. Where two of them do not commute, both orders are given, each with the quantity it defines. A statement about a rate of change (a velocity, an acceleration, the rate of a clock) is derived for that rate; it is not inferred from a bound or an estimate of the quantity whose derivative it is.
- Every statement with "all", "iff" or "well defined" is stated with its exceptional members (a gradient operator that is a multiple of the identity, a field frequency that vanishes or equals a gap of the body, equal data of two levels); a condition that is only sufficient is called sufficient.

## Scope

- **Class.** Item 1: every $`C_f`$, $`Y`$, $`\varphi`$, every start of the body and of the medium. Items 2 and 3: every level and both branches of Model D, every smooth $`g`$ in 2(a), starts at rest in 2(b) and 3, every $`\gamma_0`$, $`\gamma_1`$, $`\vartheta`$, $`\Omega>0`$. Item 4: the stated field.
- **Controls.** A constant $`\gamma`$ against a $`\gamma(\lambda)`$ that changes (items 2 and 3); the two controls of item 4(b).
- In scope:
  - what the body sees of a field that is not stationary, at first order in the field;
  - the first-order velocity and acceleration of a branch start in a gradient that changes with $`\lambda`$;
  - the conditions on the field frequencies under which the fall from rest is the same for all clock levels.
- Out of scope:
  - the second order in the field beyond the statement of item 1(c); the stationary start in an eigenvector of $`C_f`$ and its second-order terms (10-field-own-contract); a static field that is not sharp (09-unsharp-field);
  - a factor that changes with $`\lambda`$ at the reference position (a term $`G\otimes N_0`$ with an operator $`N_0`$), the clock statistics in a changing field, the fall in motion and lattice terms;
  - where the field comes from, two bodies in one field, and instances of one type;
  - any physical meaning beyond the definitions (M1–M4); no theory of gravity and no theory that contains time may be used as an input.

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: derive.
- Item 4: short argument.
- Item 5: standard (a table of results with their tags).

## Expected result

- Item 1: a statement with the functions named; a generator with a yes/no answer and two special cases; orders.
- Item 2: a functional with its kernel and a check; a closed form with the separated parts and the order of the limits.
- Item 3: a closed form with a limit, an equivalence and a leading term; a growth law; a condition and a statement.
- Item 4: a function and evaluations; two controls.
- Item 5: a table.

Give every main result a tag $`(12.k)`$.

Consistency checks, at most three: for example a constant $`\gamma`$, the limit $`\Omega\to0`$, and dimensions.

## Code

None.
