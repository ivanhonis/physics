# Question: 04-branch-fall

- **Subproject:** 05-ilang-free-fall
- **Package:** 04-branch-fall
- **Equation tags:** (4.k)
- **Created:** 2026-10-10

## Goal

For a body whose clock level is conserved and whose level blocks have the Model D form with position-dependent parameters, determine how a start that lies in one branch accelerates, at rest and in motion, and determine exactly which position dependences give an acceleration that is the same for all clock levels. This is the part of criterion 3 that concerns a moving body, criterion 4, the part of criterion 6 that concerns the lattice and the speed, and criterion 5 at leading order.

**Setting.**
- **Objects.** A body $`b`$, the only instance of its type, and a recording medium $`c`$, one object of another type, with the records $`K_x=\kappa\,x\,X`$ as for Model D. There is no field object: the position dependence is written into the body's own contract, which is an admissible description (A10) and an assumption of this package (M8).
- **Body contract (the class $`\mathcal C_{\rm lev}`$).** Places $`(x,s,a)`$ as for Model D, with $`x`$ on a chain $`\lvert x\rvert\le L`$ and $`x\in\mathbb Z`$ as the limit of long chains (A1). With the vectors $`\lvert f_k\rangle`$ of Model D,
  ```math
  C_b=\sum_{k=0}^{N-1}C^{(k)}\otimes\lvert f_k\rangle\langle f_k\rvert,\qquad C^{(k)}=\frac{\tau_k}2\sum_x\zeta_{x,k}\Bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\Bigr)+\sum_x\lvert x\rangle\langle x\rvert\otimes\bigl(M_{x,k}\,\sigma_3+V_{x,k}\,\mathbb 1_2\bigr),
  ```
  with real numbers $`\tau_k>0`$, $`\zeta_{x,k}>0`$, $`M_{x,k}>0`$ and $`V_{x,k}`$. $`C^{(k)}`$ is the **level block** of the clock level $`k`$; the level is conserved. The class $`\mathcal C`$ of 03-clock-and-fall is the subclass $`\tau_k=\tau`$, $`\zeta_{x,k}=\zeta_x`$, $`M_{x,k}=m_x+\eta_xd_k`$, $`V_{x,k}=V_x`$, with $`d_k:=\frac{2\pi k}{N\lambda_0}`$; Model D is its member $`m_x=m`$, $`\eta_x=1`$, $`\zeta_x=1`$, $`V_x=0`$.
- **Linear level profiles.** For every level $`k`$: $`M_{x,k}=M_k+G_kx`$, $`V_{x,k}=-\mathcal F_kx`$, $`\zeta_{x,k}=1+g_{\zeta,k}(x+\tfrac12)`$, with $`M_k>0`$, $`\lvert G_k\rvert(L+1)<M_k`$ and $`\lvert g_{\zeta,k}\rvert(L+1)<1`$. The **gradients of the level $`k`$** are $`G_k`$, $`\mathcal F_k`$ and $`g_{\zeta,k}`$. For the class $`\mathcal C`$ with the linear profiles of 03-clock-and-fall: $`M_k=m+d_k`$, $`G_k=m\,g_m+d_k\,g_\eta`$, $`\mathcal F_k=\mathcal F`$, $`g_{\zeta,k}=g_\zeta`$.
- **Records and regime.** As in 03-clock-and-fall: the level profiles are those of the effective body contract (8.19), so the term $`\kappa\,x\,\langle X\rangle`$ of the records is counted in every $`V_{x,k}`$; the mean position label is $`\bar x_{\rm lab}(\lambda):=\sum_xx\,p_x(\lambda)`$, with $`p_x`$ the place weights of the view of the body; results are asked in the weak-record regime, $`\kappa\to0`$ at fixed $`\lambda`$, chain and start. State the order of what is neglected.
- **Zeroth-order level block.** With all gradients of the level $`k`$ set to zero the level block is $`C^{(k)}_0=-\tau_k\sin\hat p\,\sigma_1+M_k\sigma_3`$, the block (5.5) with $`\tau\to\tau_k`$ and $`\mu_k\to M_k`$. Its eigenvalues are $`\pm\omega_k(p)`$, $`\omega_k(p):=\sqrt{M_k^2+\tau_k^2\sin^2p}`$, with the eigenvectors $`\beta_{k,\pm}(p)`$ of (5.6) (same substitution). The **branch** $`\sigma\in\{+,-\}`$ of the level $`k`$ is spanned by the vectors $`\lvert p\rangle\otimes\beta_{k,\sigma}(p)\otimes\lvert f_k\rangle`$.
- **Starts.** For a level $`k`$, a branch $`\sigma`$ and a smooth $`2\pi`$-periodic function $`g`$ with $`\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g\rvert^2=1`$, the **branch start** $`B_{k,\sigma}[g]`$ is
  ```math
  \lvert\phi\rangle=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\,g(p)\,\lvert p\rangle\otimes\beta_{k,\sigma}(p)\otimes\lvert f_k\rangle
  ```
  on the infinite chain. $`\langle F\rangle_g:=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g(p)\rvert^2F(p)`$. The start is **concentrated at $`p_0`$** with the spread $`\delta p`$ if, on the arc $`(p_0-\pi,p_0+\pi]`$, the weight $`\lvert g\rvert^2\frac{\mathrm dp}{2\pi}`$ has the mean $`p_0`$ and the variance $`\delta p^2`$; it is **at rest** if $`p_0=0`$. The start lies in a branch of the zeroth-order level block and is not adapted to the gradients; this is part of the assumption (M9).
- **Orders.** "First order in the gradients of the level $`k`$" means: first order jointly in $`G_k`$, $`\mathcal F_k`$, $`g_{\zeta,k}`$ at fixed $`\lambda`$, fixed start and fixed chain, followed by the limit of a long chain; state how a branch start is placed on a finite chain and how that limit is taken. The limits of a long window and of a sharp label ($`\delta p\to0`$ at fixed $`p_0`$) are taken as each item states.

1. **Drift of a branch start.** One level $`k`$, one branch $`\sigma`$, a start $`B_{k,\sigma}[g]`$, linear level profiles.
   - (a) Determine the velocity $`\mathrm d\bar x_{\rm lab}/\mathrm d\lambda`$ at zeroth order and at first order in the gradients of the level $`k`$, as functions of $`\lambda`$. Write the first-order velocity as a part that is linear in $`\lambda`$ plus a rest; determine the coefficient of $`\lambda`$ exactly, as an average $`\langle\cdot\rangle_g`$; determine how the rest behaves for $`\lambda\to\infty`$ (bounded or growing, with the power and the reason), with a bound that holds for all $`\lambda\ge0`$.
   - (b) Determine the average of the first-order acceleration over a window $`[\lambda_1,\lambda_1+\Lambda]`$ and its limit $`\Lambda\to\infty`$ at fixed $`g`$. Determine the limit of a sharp label of the first-order acceleration at fixed $`\lambda`$. Determine whether the limits "long window" and "sharp label" commute. The **drift acceleration** $`a_{k,\sigma}(p_0)`$ is the limit of a long window followed by the limit of a sharp label, if it exists.
   - (c) Compare with the start $`S_k`$ of 03-clock-and-fall, (3.26)–(3.28): state which terms of (3.26) are absent or changed for a branch start at rest, and why.

2. **Rest and motion.**
   - (a) Determine $`a_{k,\sigma}(p_0)`$ in closed form for every $`p_0`$, and its value at rest.
   - (b) Let $`v:=\sigma\,\omega_k'(p_0)`$ (state what this quantity is for a branch start at zero gradients). Determine $`a_{k,\sigma}`$ as a function of $`v`$ to second order in $`v`$: its value at $`v=0`$ and the coefficient of $`v^2`$, separately for the three gradients.
   - (c) Express the value at rest and the coefficient of $`v^2`$ through quantities of the level $`k`$ that are well defined (M6): the gap between the on-site eigenvalues, the norm of the hopping block, and their differences between neighbouring positions, in the manner of (3.2). State which replacements they are invariant under.

3. **Level-independent fall.** Bodies of $`\mathcal C_{\rm lev}`$ with $`N\ge2`$ levels and linear level profiles.
   - (a) From rest. Determine the necessary and sufficient condition on $`(\tau_k,M_k,G_k,\mathcal F_k,g_{\zeta,k})_k`$ under which $`a_{k,+}(0)`$ is the same for all levels $`k`$; the same for $`a_{k,-}(0)`$; and the condition under which both hold with the same value.
   - (b) In motion. Determine the necessary and sufficient condition under which $`a_{k,+}`$, as a function of the drift velocity $`v`$, is the same for all levels through the order $`v^2`$. Determine it exactly, and then in the regime $`M_k\ll\tau_k`$ for all $`k`$, to leading order in $`M_k/\tau_k`$; state which terms are dropped in that regime.
   - (c) The class $`\mathcal C`$. Translate the conditions of (a) and (b) into conditions on $`(g_m,g_\eta,g_\zeta,\mathcal F)`$, for $`N=2`$ and for $`N\ge3`$ levels.

4. **Clock rate and fall in the class $`\mathcal C`$.** With the rate at a place (3.23), in its wide-start form:
   - (a) Determine whether a rate that depends on the place implies that $`a_{k,+}(0)`$ is the same for all levels, and whether the converse holds.
   - (b) Assume that $`a_{k,+}(0)`$ is the same for all levels and not zero. Determine its relation to the rates at neighbouring positions. Express the relation in the background of (17.15), with the acceleration of $`\bar x`$, the distance $`d_0`$ of neighbouring positions and the bound (5.11), and state whether $`m`$, $`N`$, $`\lambda_0`$, $`\tau`$, the level $`k`$ or the plain gradient $`\mathcal F`$ appear in it.
   - (c) Determine the same for the lower branch, $`a_{k,-}(0)`$.
   - (d) State how the two rates that enter are compared, and what the comparison relies on.

5. **Variants.** Evaluate $`a_{k,+}(0)`$, $`a_{k,-}(0)`$ and the coefficient of $`v^2`$ of item 2(b) for the variants (a), (b1), (b2), (c), (d) of 03-clock-and-fall (quoted under "Inputs"), and for the variant
   - (f) a constant under the factor: the on-site block of the level $`k`$ is $`(1+gx)\bigl[(m+d_k)\,\sigma_3+c_{\rm f}\,\mathbb 1_2\bigr]`$ with a real number $`c_{\rm f}`$, that is $`g_m=g_\eta=g`$, $`g_\zeta=0`$, $`\mathcal F=-c_{\rm f}\,g`$.

   For each variant state whether the fall is the same for all levels: from rest in the upper branch, from rest in the lower branch, and through the order $`v^2`$.

## Inputs

From 05-moving-clock@v3 of 04-ilang-time. Setting there: one Model D body with the contract $`C_b=C_{\rm D}`$ of the base problem, the records $`K_x=\kappa xX`$ and the start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`d_k:=\frac{2\pi k}{N\lambda_0}`$; the plane waves $`\lvert p\rangle=\sum_xe^{ipx}\lvert x\rangle`$, $`p\in(-\pi,\pi]`$.

Eq. (5.5):

```math
C_b\bigl(\lvert p\rangle\otimes\beta\otimes\lvert f_k\rangle\bigr)=\lvert p\rangle\otimes C_k(p)\beta\otimes\lvert f_k\rangle,\qquad C_k(p):=-\tau\sin p\,\sigma_1+\mu_k\sigma_3,\qquad\mu_k:=m+d_k .
```

Eq. (5.6), the eigenvalues $`\pm\omega_k(p)`$ and the real eigenvectors $`\lvert p\rangle\otimes\beta_{k,\pm}(p)\otimes\lvert f_k\rangle`$ of $`C_b`$:

```math
\omega_k(p)=\sqrt{\mu_k^2+\tau^2\sin^2p},\quad
\beta_{k,+}=\begin{pmatrix}\cos\frac{\theta_k}2\\ \sin\frac{\theta_k}2\end{pmatrix},\quad
\beta_{k,-}=\begin{pmatrix}-\sin\frac{\theta_k}2\\ \cos\frac{\theta_k}2\end{pmatrix},\quad
\tan\theta_k(p)=-\frac{\tau\sin p}{\mu_k},\ \ \lvert\theta_k\rvert<\frac\pi2 .
```

Eq. (5.11), the bound (17.7) of 03-ilang-space/17-motion for this $`C_b`$ (the maximal speed):

```math
v_{\max}=\tau\,\kappa\sigma_X=\max_h\sum_{h'}\lvert t_{hh'}\rvert\,d_0(h,h') .
```

From 08-maximal-speed@v3 of 04-ilang-time. Setting there: two bodies $`a`$, $`b`$ of different types and a medium $`c`$, with body contracts $`C_A`$, $`C_B`$ (diagonal entries $`t^A_{hh}`$, $`t^B_{kk}`$) and records $`K^A_h`$, $`K^B_k`$.

Eq. (8.1), all replacements of the diagonal entries of the body contracts and of the records that leave the total contract unchanged, with arbitrary real $`\alpha^A_h`$, $`\alpha^B_k`$ and an arbitrary self-adjoint $`Z`$ on $`\mathcal H_c`$:

```math
t'^A_{hh}=t^A_{hh}+\alpha^A_h,\quad K'^A_h=K^A_h+Z-\alpha^A_h\mathbb 1_c,\qquad
t'^B_{kk}=t^B_{kk}+\alpha^B_k,\quad K'^B_k=K^B_k-Z-\alpha^B_k\mathbb 1_c ,
```

Eq. (8.19), the effective body contracts:

```math
C^{\rm eff}_A\otimes\mathbb 1_b+\mathbb 1_a\otimes C^{\rm eff}_B:=(\mathbb 1_{ab}\otimes\langle\chi\rvert)\,C\,(\mathbb 1_{ab}\otimes\lvert\chi\rangle),\qquad
C^{\rm eff}_A=C_A+\sum_h\langle K^A_h\rangle\lvert h\rangle\langle h\rvert,\quad
C^{\rm eff}_B=C_B+\sum_k\langle K^B_k\rangle\lvert k\rangle\langle k\rvert .
```

Eq. (8.20):

```math
\text{(8.1):}\quad C^{\rm eff}_A\mapsto C^{\rm eff}_A+\langle Z\rangle\,\mathbb 1_a,\quad C^{\rm eff}_B\mapsto C^{\rm eff}_B-\langle Z\rangle\,\mathbb 1_b;\qquad \chi\mapsto e^{i\theta}\chi:\quad C^{\rm eff}_A,\ C^{\rm eff}_B\ \text{unchanged}.
```

From 03-ilang-space/17-motion@v2. Setting there: $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$; the start is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, $`\lvert u_h\rangle:=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$, $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$; with $`p_h(\lambda)`$ the place weights of the view of $`b`$, $`\bar x(\lambda):=\sum_hp_h(\lambda)\,u_h`$.

Eq. (17.15), for the chain $`h_m`$, $`m\in\mathbb Z`$, with $`K_{h_m}=m\,X`$, $`X`$ self-adjoint on $`\mathcal H_c`$, $`\sigma_X:=(\langle X^2\rangle-\langle X\rangle^2)^{1/2}>0`$ and $`e:=(X-\langle X\rangle)\chi`$, so that $`\lVert e\rVert=\sigma_X`$ and $`u_{h_m}=m\,e`$:

```math
d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X,\qquad \bar x=\bar m\,e,\quad \bar m:=\sum_mm\,p_{h_m},\qquad s^2=\sigma_X^2\sum_m(m-\bar m)^2p_{h_m} .
```

From 03-clock-and-fall@v3 (this subproject). Setting there: one body $`b`$ of the class $`\mathcal C`$ and a medium $`c`$ with the records $`K_x=\kappa\,x\,X`$. The class $`\mathcal C`$: places $`(x,s,a)`$ as for Model D and, with real numbers $`m_x>0`$, $`\eta_x>0`$, $`\zeta_x>0`$ and $`V_x`$,
```math
C_b=A_\zeta+\sum_x\lvert x\rangle\langle x\rvert\otimes\Bigl[\sigma_3\otimes(m_x\mathbb 1_N+\eta_xD)+V_x\,\mathbb 1_2\otimes\mathbb 1_N\Bigr],\qquad A_\zeta=\frac\tau2\sum_x\zeta_x\Bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\Bigr)\otimes\mathbb 1_N ,
```
with the linear profiles $`m_x=m\,(1+g_mx)`$, $`\eta_x=1+g_\eta x`$, $`\zeta_x=1+g_\zeta(x+\tfrac12)`$, $`V_x=-\mathcal F\,x`$ on a chain $`\lvert x\rvert\le L`$. Notation fixed there:
- $`P_x:=\lvert x\rangle\langle x\rvert`$, $`R_x:=\lvert x+1\rangle\langle x\rvert`$, $`\hat x:=\sum_xx\,P_x`$, $`\mathsf M_x:=m_x\mathbb 1_N+\eta_xD`$, $`d_k:=\frac{2\pi k}{N\lambda_0}`$; $`C_{\rm eff}`$ is the effective body contract (8.19) of 04-ilang-time/08-maximal-speed, and all profiles are those of $`C_{\rm eff}`$;
- on the clock level $`k`$ (clock label in $`\lvert f_k\rangle`$; the level is conserved): $`M_{x,k}:=m_x+\eta_xd_k`$, the on-site block $`M_{x,k}\sigma_3+V_x\mathbb 1_2`$ and the hopping block $`T_x=-\tfrac{i\tau}2\zeta_x\sigma_1`$ from $`x`$ to $`x+1`$; for the linear profiles $`M_{x,k}=M_k+G_kx`$ with $`M_k:=m+d_k`$ and $`G_k:=m\,g_m+d_k\,g_\eta`$; $`\omega_k(p):=\sqrt{M_k^2+\tau^2\sin^2p}`$; $`b_1:=(\tau+M_k)\lvert g_\zeta\rvert+\lvert G_k\rvert+\lvert\mathcal F\rvert`$;
- $`\bar x_{\rm lab}(\lambda):=\sum_xx\,p_x(\lambda)`$ is the mean position label; the weak-record regime is the limit $`\kappa\to0`$ at fixed $`\lambda`$, chain and start; "first order in the gradients" is the first order jointly in $`g_m,g_\eta,g_\zeta,\mathcal F`$ at fixed $`\lambda`$, start and chain, followed by the limit of a long chain;
- the start $`S_k(x_0)`$: $`\phi=\phi_X\otimes\lvert1\rangle\otimes\lvert f_k\rangle`$ with $`\phi_X(x)=c_W\,w\bigl((x-x_0)/W\bigr)`$, $`w`$ real and smooth with support in $`[-1,1]`$ (a bare branch label $`s=1`$); the start $`S_{\rm clock}(x_0)`$: the same with the clock label in the place $`\lvert0\rangle`$;
- $`\tilde\phi_X(p):=\sum_xe^{-ipx}\phi_X(x)`$, $`\langle f\rangle_W:=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert\tilde\phi_X(p)\rvert^2f(p)`$, and $`\delta_W^2:=\sum_x(\phi_X(x+1)-\phi_X(x))^2=O(W^{-2})`$.

The variants named there, each with one number $`g`$: (a) $`g_m=g_\eta=g`$, $`g_\zeta=0`$, $`\mathcal F=0`$; (b1) $`g_m=g`$, the others zero; (b2) $`g_\eta=g`$, the others zero; (c) $`g_m=g_\eta=g_\zeta=g`$, $`\mathcal F=0`$; (d) $`\mathcal F\neq0`$, the others zero.

Eq. (3.2), the quantities of the level $`k`$ that are well defined (functions of $`C_{\rm eff}`$ modulo $`\mathbb 1`$, invariant under (8.1)):

```math
E^{\pm}_{x,k}:=V_x\pm M_{x,k}\ (\text{modulo a common constant}),\quad \Delta_{x,k}:=2M_{x,k},\quad t_x:=\lVert T_x\rVert=\tfrac{\tau\zeta_x}{2},\quad \delta E^{\pm}_{x,k}:=E^{\pm}_{x+1,k}-E^{\pm}_{x,k},\quad\delta t_x:=t_x-t_{x-1}.
```

Eq. (3.5), exact for every member of $`\mathcal C`$:

```math
\frac{\mathrm d\bar x_{\rm lab}}{\mathrm d\lambda}=\langle\hat v\otimes\mathbb 1_c\rangle,\qquad \hat v:=i[C_{\rm eff},\hat x]=-\frac\tau2\sum_x\zeta_x\bigl(R_x+R_x^\dagger\bigr)\otimes\sigma_1\otimes\mathbb 1_N .
```

Eq. (3.6), $`\hat a:=i[C_{\rm eff},\hat v]`$:

```math
\hat a=\frac{\tau^2}{2}\sum_x\bigl(\zeta_x^2-\zeta_{x-1}^2\bigr)P_x+\frac\tau2\sum_x\zeta_x\Bigl[(R_x+R_x^\dagger)\otimes\sigma_2\otimes(\mathsf M_x+\mathsf M_{x+1})+(V_{x+1}-V_x)\,(-iR_x+iR_x^\dagger)\otimes\sigma_1\otimes\mathbb 1_N\Bigr].
```

Eq. (3.9), the level block for the linear profiles, exactly:

```math
C^{(k)}=C_0+C_1,\qquad C_0=-\tau\sin\hat p\,\sigma_1+M_k\sigma_3,\qquad C_1=\tfrac12\{\hat x,B(\hat p)\},\qquad B(p):=-g_\zeta\tau\sin p\,\sigma_1+G_k\sigma_3-\mathcal F .
```

Eq. (3.26), for the start $`S_k(x_0)`$ on the infinite chain: the first-order velocity is $`v^{(1)}_W(\lambda)=\langle\nu(p,\lambda)\rangle_W`$, and exactly, with $`\nu_0`$, $`A_j`$ smooth, $`2\pi`$-periodic and linear in the gradients,

```math
\nu(p,\lambda)=a_{\rm sec}(p)\,\lambda+\nu_0(p)+\mathrm{Re}\sum_{j=0}^{2}\lambda^jA_j(p)\,e^{2i\omega_k(p)\lambda},\qquad a_{\rm sec}(p)=\frac{g_\zeta\tau^4\sin^2p-G_k\tau^2M_k\cos2p}{\omega_k^2}+\mathcal F\,\frac{\tau^2M_k\bigl(M_k^2\cos2p-\tau^2\sin^4p\bigr)}{\omega_k^4},
```

Eq. (3.27), the long-window limit of the window average $`\overline{a^{(1)}_W}`$ of the first-order acceleration of $`S_k(x_0)`$ at finite $`W`$, with the average over $`[\lambda_1,\lambda_1+\Lambda]`$:

```math
\lim_{\Lambda\to\infty}\overline{a^{(1)}_W}=\bar a_W:=\langle a_{\rm sec}(p)\rangle_W=g_\zeta\,\tau^4s_W-\frac{\tau^2G_k}{M_k}\Bigl[1-(2M_k^2+\tau^2)\,s_W\Bigr]+\frac{\tau^2\mathcal F}{M_k}\,f_W,
```

```math
s_W:=\Bigl\langle\frac{\sin^2p}{\omega_k^2}\Bigr\rangle_W,\quad f_W:=\Bigl\langle\frac{M_k^2(M_k^2\cos2p-\tau^2\sin^4p)}{\omega_k^4}\Bigr\rangle_W;\qquad0<s_W\le\frac{\delta_W^2}{M_k^2},\quad0\le1-f_W\le2(M_k^2+\tau^2)\,s_W\quad(\text{exact}),
```

Eq. (3.15), the first-order displacement of $`S_k(x_0)`$ in the wide-start limit, which defines $`a_{\rm sec}`$:

```math
\bar x^{(1)}_{\rm lab}(\lambda)-\bar x_{\rm lab}(0)=\tfrac12\,a_{\rm sec}\,\lambda^2+\frac{\tau^2G_k}{2M_k^2}\,\lambda\sin(2M_k\lambda)+\frac{\tau^2}{2M_k^3}\bigl(M_kg_\zeta-\mathcal F-G_k\bigr)\sin^2(M_k\lambda),\qquad\boxed{\;a_{\rm sec}:=\frac{\tau^2}{M_k}\bigl(\mathcal F-G_k\bigr)\;}
```

Eq. (3.28):

```math
\bigl\lvert\bar a_W-a_{\rm sec}\bigr\rvert\le2\,\delta_W^2\,\frac{\tau^2}{M_k}\Bigl(1+\frac{\tau^2}{M_k^2}\Bigr)b_1\ \ (\text{exact}),\qquad\lim_{W\to\infty}\lim_{\Lambda\to\infty}\overline{a^{(1)}_W}=a_{\rm sec},\qquad\lim_{\Lambda\to\infty}\lim_{W\to\infty}\overline{a^{(1)}_W}\ \text{does not exist if }G_k\neq0 .
```

Eq. (3.36), for the start $`S_{\rm clock}(x_0)`$ at zeroth order in the gradients and to first order in the level spacing, with the local parameters $`\tau^0:=\tau(1+g_\zeta x_0)`$, $`m^0:=m_{x_0}`$, $`\eta^0:=\eta_{x_0}`$, $`\bar\mu:=m^0+\eta^0\frac{\pi(N-1)}{N\lambda_0}`$ and $`\Gamma(p):=\bar\mu/\sqrt{\bar\mu^2+\tau^{0\,2}\sin^2p}`$; $`\vartheta_W`$ is the mean advance of the clock distribution, $`r_W`$ the rate at finite $`W`$:

```math
\vartheta_W(\lambda):=\Bigl\langle\tfrac{1+\Gamma}2\Gamma-\tfrac{1-\Gamma}2\Gamma\Bigr\rangle_W\frac{\eta^0\lambda}{\lambda_0}=(1-\varsigma_W)\frac{\eta^0\lambda}{\lambda_0},\qquad r_W(x_0):=\frac{\mathrm d\vartheta_W}{\mathrm d\lambda}=\frac{\eta^0}{\lambda_0}\,(1-\varsigma_W),\qquad\varsigma_W(x_0):=\Bigl\langle\frac{\tau^{0\,2}\sin^2p}{\bar\mu^2+\tau^{0\,2}\sin^2p}\Bigr\rangle_W,
```

Eq. (3.23), the rate at $`x_0`$ (its wide-start form and its form at finite $`W`$), with $`E^\pm_{x,k}`$ of (3.2):

```math
\text{rate at }x_0:=\lim_{W\to\infty}r_W(x_0)=\frac{\eta_{x_0}}{\lambda_0}=\frac{N}{2\pi}\bigl(E^+_{x_0,k+1}-E^+_{x_0,k}\bigr),\ \ \text{tick }\frac{\lambda_0}{\eta_{x_0}};\qquad\text{at finite }W:\ \ r_W=\frac{\eta_{x_0}}{\lambda_0}(1-\varsigma_W),\ \ \text{tick }\frac{\lambda_0}{\eta_{x_0}(1-\varsigma_W)},\ \ \Bigl\lvert r_W-\frac{\eta_{x_0}}{\lambda_0}\Bigr\rvert\le\frac{\eta_{x_0}}{\lambda_0}\,\delta_W^2\frac{\tau^{0\,2}}{m_{x_0}^2}.
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- No object other than $`b`$ has the type of $`b`$, and $`c`$ is the only instance of its type.
- The members of $`\mathcal C_{\rm lev}`$, the linear level profiles and the branch starts are assumptions of this package (M8, M9).
- Standard facts on first-order perturbation theory in a term of the contract, on plane waves, on the averaging of oscillating terms and on stationary-phase estimates may be used; state them with their conditions.

## Scope

- **Class.** Items 1 and 2: every member of $`\mathcal C_{\rm lev}`$ with linear level profiles, every level, both branches, every $`g`$. Item 3: all such bodies with $`N\ge2`$ levels. Item 4: the class $`\mathcal C`$ with the linear profiles of 03-clock-and-fall. Item 5: the six named variants.
- **Controls.** The lower branch; the bare start of 03-clock-and-fall (item 1(c)); the variants (b1), (b2), (d) and (f).
- In scope:
  - the velocity and the drift acceleration of a branch start, at rest and in motion, to first order in the gradients;
  - the order of the limits of a long window and of a sharp label;
  - the conditions for a fall that is the same for all levels, at rest and through the order $`v^2`$;
  - the relation between a level-independent fall and the place dependence of the clock rate, at leading order.
- Out of scope:
  - a start in a superposition of levels or of branches, and a clock that ticks during the fall (a later package);
  - the second order in the gradients, profiles that are not linear, and long falls;
  - effects of the records beyond leading order in $`\kappa`$ (a later package);
  - bodies of two types, a field object, and fields that are not sharp;
  - the comparison of clocks at two places inside one description (05-rate-comparison);
  - any physical meaning beyond the definitions (M1–M4); no theory of gravity may be used as an input.

## Depth

- Item 1: derive.
- Item 2: derive.
- Item 3: derive.
- Item 4: short argument.
- Item 5: short argument.

## Expected result

- Item 1: a closed form with a coefficient and a bound; two limits and a yes/no answer; a comparison.
- Item 2: a closed form; an expansion with its coefficients; expressions in well-defined quantities.
- Item 3: three equivalences; an equivalence, exactly and in the stated regime; conditions on four numbers.
- Item 4: two yes/no answers with examples; a relation and a list of yes/no answers; the same for the other branch; a statement.
- Item 5: a table.

Give every main result a tag $`(4.k)`$.

Consistency checks, at most three: for example all gradients zero, a start at rest in the upper branch against (3.28), and $`\tau_k\to0`$.

## Code

None.
