# Question: 07-limits

- **Subproject:** 05-ilang-free-fall
- **Package:** 07-limits
- **Equation tags:** (7.k)
- **Created:** 2026-10-11

## Goal

Determine the limits of the level-independent fall and of the relation (4.24) that the earlier packages left open: a start in a superposition of clock levels, the records of the medium beyond the effective body contract, and the operator of the body that a factor multiplies. Collect, for every source of a deviation, the order at which it enters. This is criterion 6.

**Setting.**
- **Objects.** A body $`b`$, the only instance of its type, and a recording medium $`c`$, one object of another type, with the records $`K_x=\kappa\,x\,X`$ as for Model D. There is no field object: the position dependence is written into the body's own contract, which is an admissible description (A10) and an assumption of this package (M8).
- **Body contract (the class $`\mathcal C_{\rm lev}`$).** Places $`(x,s,a)`$ as for Model D, with $`x`$ on a chain $`\lvert x\rvert\le L`$ and $`x\in\mathbb Z`$ as the limit of long chains (A1). With the vectors $`\lvert f_k\rangle`$ of Model D,
  ```math
  C_b=\sum_{k=0}^{N-1}C^{(k)}\otimes\lvert f_k\rangle\langle f_k\rvert,\qquad C^{(k)}=\frac{\tau_k}2\sum_x\zeta_{x,k}\Bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\Bigr)+\sum_x\lvert x\rangle\langle x\rvert\otimes\bigl(M_{x,k}\,\sigma_3+V_{x,k}\,\mathbb 1_2\bigr),
  ```
  with real numbers $`\tau_k>0`$, $`\zeta_{x,k}>0`$, $`M_{x,k}>0`$ and $`V_{x,k}`$. $`C^{(k)}`$ is the **level block** of the clock level $`k`$; the level is conserved. The class $`\mathcal C`$ of 03-clock-and-fall is the subclass $`\tau_k=\tau`$, $`\zeta_{x,k}=\zeta_x`$, $`M_{x,k}=m_x+\eta_xd_k`$, $`V_{x,k}=V_x`$, with $`d_k:=\frac{2\pi k}{N\lambda_0}`$; Model D is its member $`m_x=m`$, $`\eta_x=1`$, $`\zeta_x=1`$, $`V_x=0`$.
- **Linear level profiles.** For every level $`k`$: $`M_{x,k}=M_k+G_kx`$, $`V_{x,k}=V_k-\mathcal F_kx`$, $`\zeta_{x,k}=1+g_{\zeta,k}(x+\tfrac12)`$, with $`M_k>0`$, $`\lvert G_k\rvert(L+1)<M_k`$ and $`\lvert g_{\zeta,k}\rvert(L+1)<1`$. The **gradients of the level $`k`$** are $`G_k`$, $`\mathcal F_k`$ and $`g_{\zeta,k}`$; the real numbers $`V_k`$ are the **level offsets**. For the class $`\mathcal C`$ with the linear profiles of 03-clock-and-fall: $`M_k=m+d_k`$, $`G_k=m\,g_m+d_k\,g_\eta`$, $`\mathcal F_k=\mathcal F`$, $`g_{\zeta,k}=g_\zeta`$, $`V_k=0`$. The results quoted from 04-branch-fall were derived with $`V_k=0`$ and concern starts in one level; state why a level offset does not change them.
- **Records and regime.** As in 04-branch-fall: the level profiles are those of the effective body contract, (8.19) of 04-ilang-time/08-maximal-speed, so the term $`\kappa\,x\,\langle X\rangle`$ of the records is counted in every $`V_{x,k}`$; the mean position label is $`\bar x_{\rm lab}(\lambda):=\sum_xx\,p_x(\lambda)`$, with $`p_x`$ the place weights of the view of the body; unless an item says otherwise, results are asked in the weak-record regime, $`\kappa\to0`$ at fixed $`\lambda`$, chain and start.
- **Zeroth-order level block and branches.** With all gradients of the level $`k`$ set to zero the level block is $`C^{(k)}_0=-\tau_k\sin\hat p\,\sigma_1+M_k\sigma_3`$ (plus $`V_k\mathbb 1`$), the block (5.5) of 04-ilang-time/05-moving-clock with $`\tau\to\tau_k`$ and $`\mu_k\to M_k`$. Its eigenvalues are $`V_k\pm\omega_k(p)`$, $`\omega_k(p):=\sqrt{M_k^2+\tau_k^2\sin^2p}`$, with the eigenvectors $`\beta_{k,\pm}(p)`$ of (5.6) of 04-ilang-time/05-moving-clock (same substitution). The **branch** $`\sigma\in\{+,-\}`$ of the level $`k`$ is spanned by the vectors $`\lvert p\rangle\otimes\beta_{k,\sigma}(p)\otimes\lvert f_k\rangle`$.
- **Branch starts.** For a level $`k`$, a branch $`\sigma`$ and a smooth $`2\pi`$-periodic function $`g`$ with $`\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g\rvert^2=1`$, the **branch start** $`B_{k,\sigma}[g]`$ is
  ```math
  \lvert\phi\rangle=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\,g(p)\,\lvert p\rangle\otimes\beta_{k,\sigma}(p)\otimes\lvert f_k\rangle
  ```
  on the infinite chain. $`\langle F\rangle_g:=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g(p)\rvert^2F(p)`$. The start is **concentrated at $`p_0`$** with the spread $`\delta p`$ if, on the arc $`(p_0-\pi,p_0+\pi]`$, the weight $`\lvert g\rvert^2\frac{\mathrm dp}{2\pi}`$ has the mean $`p_0`$ and the variance $`\delta p^2`$; it is **at rest** if $`p_0=0`$. The start lies in a branch of the zeroth-order level block and is not adapted to the gradients (M9).
- **Orders.** "First order in the gradients" means: first order jointly in the gradients of the levels involved, at fixed $`\lambda`$, fixed start and fixed chain, followed by the limit of a long chain. The **drift acceleration** $`a_{k,\sigma}(p_0)`$ of 04-branch-fall is the first-order acceleration of $`\bar x_{\rm lab}`$ for a branch start, averaged over a long window, followed by the limit of a sharp label, (4.10), (4.11).
- **Level components.** A vector of the body is written $`\sum_k\psi_k\otimes\lvert f_k\rangle`$, with $`\psi_k`$ a vector of the position and branch labels, the **level component**. Its **label weight** is $`\lVert c_k(p)\rVert^2\frac{\mathrm dp}{2\pi}`$, with $`c_k(p)\in\mathbb C^2`$ the plane-wave amplitudes of $`\psi_k`$; its mean on the arc $`(p_0-\pi,p_0+\pi]`$, divided by $`\lVert\psi_k\rVert^2`$, is the **mean label** of the level $`k`$.
- **Level-superposed starts.** For a branch $`\sigma`$, complex numbers $`\alpha_k`$ with $`\sum_k\lvert\alpha_k\rvert^2=1`$ and a function $`g`$ as for a branch start, the start $`\Phi_\sigma[\alpha,g]:=\sum_k\alpha_k\,B_{k,\sigma}[g]`$ has the same $`g`$ in every level. $`\bar x_k(\lambda)`$ is the mean position label of its normalized level component $`k`$. The **coherence** of two levels is $`\Gamma_{kk'}(\lambda):=\langle\psi_{k'}(\lambda)\vert\psi_k(\lambda)\rangle/(\alpha_{k'}^*\alpha_k)`$, for $`\alpha_k\alpha_{k'}\neq0`$. This class of starts is an assumption (M9).

1. **A start in a superposition of levels.** The start $`\Phi_\sigma[\alpha,g]`$.
   - (a) Determine the place weights $`p_x(\lambda)`$ of the view of the body and the mean position label in terms of those of the single-level starts $`B_{k,\sigma}[g]`$. State whether the relation is exact in the gradients and in $`\kappa`$, and what it rests on.
   - (b) Determine the drift acceleration of the mean position label (a long window, then a sharp label, as in (4.11)). Determine the necessary and sufficient condition on the level data under which it is the same for all $`\alpha`$, and compare it with (4.19). State what distinguishes, in readings of the position, a body with a level-dependent fall in such a start from a body in one level.
   - (c) For a start at rest: determine the variance over the levels of the first-order displacements, $`\sum_k\lvert\alpha_k\rvert^2\bigl(\bar x_k-\sum_j\lvert\alpha_j\rvert^2\bar x_j\bigr)^2`$, in its part that grows fastest with $`\lambda`$, with its coefficient, and state the order of the limits in which it is obtained. Evaluate it for the variants (a), (b1), (b2), (c), (f) with $`\lvert\alpha_k\rvert^2=1/N`$.
   - (d) For a start concentrated at $`p_0\neq0`$: determine the velocities of the level components at zero gradients, and state whether a start of this class can have level components with equal velocities.
   - (e) Determine, to first order in the gradients, the rate at which the mean label of the level $`k`$ changes for a start at rest (a long window, then a sharp label). Determine the necessary and sufficient condition under which this rate is the same for all levels, and whether it can hold together with a drift acceleration that is the same for all levels and not zero.
   - (f) Express the statistics of a reading of the clock label at $`\lambda`$ through $`\alpha`$ and the coherences $`\Gamma_{kk'}(\lambda)`$, at leading order in $`\kappa`$. Determine the order in the gradients at which $`\lvert\Gamma_{kk'}\rvert`$ first deviates from its value at zero gradients, and the leading term of this deviation for a start at rest: its dependence on $`\lambda`$, on the level data and on the spread of the start in the position. An order estimate with stated conditions suffices for the coefficient. State whether the deviation vanishes when the fall is the same for all levels.

2. **Records beyond the effective body contract.** With the exact relation (4.1):
   - (a) Count $`\kappa(\xi-\langle X\rangle)`$ as a gradient. Determine whether the first-order velocity of a branch start, and with it (4.7), (4.16) and (4.19), changes when $`X`$ is not sharp in $`\chi`$, at first order jointly in $`G_k`$, $`\mathcal F_k`$, $`g_{\zeta,k}`$ and $`\kappa(\xi-\langle X\rangle)`$.
   - (b) Let all gradients of the effective body contract vanish. Determine the mean velocity of $`B_{k,\sigma}[g]`$ to second order in $`\kappa`$: the term proportional to the variance $`\sigma_X^2`$ of $`X`$ in $`\chi`$, as a function of $`\lambda`$, with its fastest-growing part and the exact coefficient of that part as an average $`\langle\cdot\rangle_g`$, and with a bound or an order estimate for the remaining part. Determine in the same way the term of third order in $`\kappa`$ that is proportional to the third central moment of $`X`$ in $`\chi`$.
   - (c) From (b), for a sharp label $`p_0`$: determine the change of the acceleration, its value at rest, its first nonvanishing order in the drift velocity $`v`$ of (4.17), and its dependence on the level and the branch. Determine for which level data of $`\mathcal C_{\rm lev}`$ it is the same for all levels, and whether this is the case in the class $`\mathcal C`$.
   - (d) Express the result of (c) in the background of (17.15), with $`d_0=\kappa\sigma_X`$ and the bound (5.11) of 04-ilang-time/05-moving-clock. Give the range of $`\lambda`$, of $`\kappa`$ and of the gradients in which this term is smaller than the drift acceleration (4.7), and state what the weak-record regime has to mean for the fall to be the same for all levels to a given relative accuracy.

3. **The operator under the factor.** Let the on-site block of the level $`k`$ be $`(1+gx)\bigl[M_k\,\sigma_3+u_k\,\mathbb 1_2\bigr]-\mathcal F_Ux\,\mathbb 1_2`$ with real numbers $`u_k`$ and $`\mathcal F_U`$: the factor multiplies $`M_k\sigma_3+u_k\mathbb 1_2`$, and a plain part common to all levels is added. The hopping factors are arbitrary.
   - (a) Determine $`a_{k,+}(0)`$ and $`a_{k,-}(0)`$, and the necessary and sufficient conditions on $`(u_k)`$, $`\mathcal F_U`$ and $`(\tau_k)`$ under which the fall from rest is the same for all levels: in the upper branch, in the lower branch, and in both with one value.
   - (b) Determine which statements about the numbers $`u_k`$ are well defined (M6): $`u_k`$, the differences $`u_k-u_{k'}`$, "$`u_k=0`$ for all $`k`$", "$`u_k`$ is proportional to $`M_k`$". Use (8.1) and (8.20) of 04-ilang-time/08-maximal-speed.
   - (c) Evaluate (a) for $`u_k=u\,M_k`$ with one number $`u`$, and for the class $`\mathcal C`$ (the variant (f) with a plain gradient added).

4. **Orders.** Give a table with one row for each of: the lattice; the drift velocity; a start in a superposition of levels; the records; the operator under the factor; a plain gradient. For each row state the order, in the gradients, in $`v`$, in $`M_k/\tau_k`$, in $`\kappa`$ and in $`\lambda`$, at which it changes (i) the statement that the fall is the same for all levels and (ii) the relation (4.24), with the tags of the results used: (4.17), (4.20)–(4.25) and those of this package.

## Inputs

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

From 03-ilang-space/17-motion@v2. Setting there: $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$; the start is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, $`\lvert u_h\rangle:=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$, $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$; with $`p_h(\lambda)`$ the place weights of the view of $`b`$, $`\bar x(\lambda):=\sum_hp_h(\lambda)\,u_h`$.

Eq. (17.15) of 03-ilang-space/17-motion, for the chain $`h_m`$, $`m\in\mathbb Z`$, with $`K_{h_m}=m\,X`$, $`X`$ self-adjoint on $`\mathcal H_c`$, $`\sigma_X:=(\langle X^2\rangle-\langle X\rangle^2)^{1/2}>0`$ and $`e:=(X-\langle X\rangle)\chi`$, so that $`\lVert e\rVert=\sigma_X`$ and $`u_{h_m}=m\,e`$:

```math
d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X,\qquad \bar x=\bar m\,e,\quad \bar m:=\sum_mm\,p_{h_m},\qquad s^2=\sigma_X^2\sum_m(m-\bar m)^2p_{h_m} .
```

From 03-clock-and-fall@v3 (this subproject). Setting there: one body $`b`$ of the class $`\mathcal C`$ and a medium $`c`$ with the records $`K_x=\kappa\,x\,X`$. The class $`\mathcal C`$: places $`(x,s,a)`$ as for Model D and, with real numbers $`m_x>0`$, $`\eta_x>0`$, $`\zeta_x>0`$ and $`V_x`$,
```math
C_b=A_\zeta+\sum_x\lvert x\rangle\langle x\rvert\otimes\Bigl[\sigma_3\otimes(m_x\mathbb 1_N+\eta_xD)+V_x\,\mathbb 1_2\otimes\mathbb 1_N\Bigr],\qquad A_\zeta=\frac\tau2\sum_x\zeta_x\Bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\Bigr)\otimes\mathbb 1_N ,
```
with the linear profiles $`m_x=m\,(1+g_mx)`$, $`\eta_x=1+g_\eta x`$, $`\zeta_x=1+g_\zeta(x+\tfrac12)`$, $`V_x=-\mathcal F\,x`$ on a chain $`\lvert x\rvert\le L`$. Notation fixed there:
- $`P_x:=\lvert x\rangle\langle x\rvert`$, $`\hat x:=\sum_xx\,P_x`$, $`d_k:=\frac{2\pi k}{N\lambda_0}`$; $`C_{\rm eff}`$ is the effective body contract (8.19) of 04-ilang-time/08-maximal-speed, and all profiles are those of $`C_{\rm eff}`$;
- on the clock level $`k`$ (clock label in $`\lvert f_k\rangle`$; the level is conserved): $`M_{x,k}:=m_x+\eta_xd_k`$, the on-site block $`M_{x,k}\sigma_3+V_x\mathbb 1_2`$ and the hopping block $`T_x=-\tfrac{i\tau}2\zeta_x\sigma_1`$ from $`x`$ to $`x+1`$; for the linear profiles $`M_{x,k}=M_k+G_kx`$ with $`M_k:=m+d_k`$ and $`G_k:=m\,g_m+d_k\,g_\eta`$;
- the start $`S_{\rm clock}(x_0)`$: $`\phi=\phi_X\otimes\lvert1\rangle\otimes\lvert0\rangle`$ with $`\phi_X(x)=c_W\,w\bigl((x-x_0)/W\bigr)`$, $`w`$ real and smooth with support in $`[-1,1]`$ (a bare branch label $`s=1`$ and the clock label in the place $`\lvert0\rangle`$);
- $`\tilde\phi_X(p):=\sum_xe^{-ipx}\phi_X(x)`$, $`\langle f\rangle_W:=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert\tilde\phi_X(p)\rvert^2f(p)`$, and $`\delta_W^2:=\sum_x(\phi_X(x+1)-\phi_X(x))^2=O(W^{-2})`$.

The variants named there, each with one number $`g`$: (a) $`g_m=g_\eta=g`$, $`g_\zeta=0`$, $`\mathcal F=0`$; (b1) $`g_m=g`$, the others zero; (b2) $`g_\eta=g`$, the others zero; (c) $`g_m=g_\eta=g_\zeta=g`$, $`\mathcal F=0`$; (d) $`\mathcal F\neq0`$, the others zero. The variant (f) of 04-branch-fall, a constant under the factor: the on-site block of the level $`k`$ is $`(1+gx)\bigl[(m+d_k)\,\sigma_3+c_{\rm f}\,\mathbb 1_2\bigr]`$ with a real number $`c_{\rm f}`$, that is $`g_m=g_\eta=g`$, $`g_\zeta=0`$, $`\mathcal F=-c_{\rm f}\,g`$.

Eq. (3.2) of 03-clock-and-fall, the quantities of the level $`k`$ that are well defined (functions of $`C_{\rm eff}`$ modulo $`\mathbb 1`$, invariant under (8.1) of 04-ilang-time/08-maximal-speed), with $`\lVert T_x\rVert`$ the norm of the hopping block:

```math
E^{\pm}_{x,k}:=V_x\pm M_{x,k}\ (\text{modulo a common constant}),\quad \Delta_{x,k}:=2M_{x,k},\quad t_x:=\lVert T_x\rVert=\tfrac{\tau\zeta_x}{2},\quad \delta E^{\pm}_{x,k}:=E^{\pm}_{x+1,k}-E^{\pm}_{x,k},\quad\delta t_x:=t_x-t_{x-1}.
```

Eq. (3.36) of 03-clock-and-fall, for the start $`S_{\rm clock}(x_0)`$ at zeroth order in the gradients and to first order in the level spacing, with the local parameters $`\tau^0:=\tau(1+g_\zeta x_0)`$, $`m^0:=m_{x_0}`$, $`\eta^0:=\eta_{x_0}`$, $`\bar\mu:=m^0+\eta^0\frac{\pi(N-1)}{N\lambda_0}`$ and $`\Gamma(p):=\bar\mu/\sqrt{\bar\mu^2+\tau^{0\,2}\sin^2p}`$. The clock statistics is, to this order, a mixture of the distributions of a ring clock with the advances $`\pm\Gamma(p)\eta^0\lambda/\lambda_0`$ and the weights $`\tfrac12(1\pm\Gamma(p))\lvert\tilde\phi_X(p)\rvert^2\frac{\mathrm dp}{2\pi}`$; $`\vartheta_W`$ is defined as the mean advance of this mixture, and $`r_W`$ is the rate at finite $`W`$:

```math
\vartheta_W(\lambda):=\Bigl\langle\tfrac{1+\Gamma}2\Gamma-\tfrac{1-\Gamma}2\Gamma\Bigr\rangle_W\frac{\eta^0\lambda}{\lambda_0}=(1-\varsigma_W)\frac{\eta^0\lambda}{\lambda_0},\qquad r_W(x_0):=\frac{\mathrm d\vartheta_W}{\mathrm d\lambda}=\frac{\eta^0}{\lambda_0}\,(1-\varsigma_W),\qquad\varsigma_W(x_0):=\Bigl\langle\frac{\tau^{0\,2}\sin^2p}{\bar\mu^2+\tau^{0\,2}\sin^2p}\Bigr\rangle_W,
```

Eq. (3.23) of 03-clock-and-fall, the rate at $`x_0`$ (its wide-start form and its form at finite $`W`$), with $`E^{\pm}_{x,k}:=V_x\pm M_{x,k}`$:

```math
\text{rate at }x_0:=\lim_{W\to\infty}r_W(x_0)=\frac{\eta_{x_0}}{\lambda_0}=\frac{N}{2\pi}\bigl(E^+_{x_0,k+1}-E^+_{x_0,k}\bigr),\ \ \text{tick }\frac{\lambda_0}{\eta_{x_0}};\qquad\text{at finite }W:\ \ r_W=\frac{\eta_{x_0}}{\lambda_0}(1-\varsigma_W),\ \ \text{tick }\frac{\lambda_0}{\eta_{x_0}(1-\varsigma_W)},\ \ \Bigl\lvert r_W-\frac{\eta_{x_0}}{\lambda_0}\Bigr\rvert\le\frac{\eta_{x_0}}{\lambda_0}\,\delta_W^2\frac{\tau^{0\,2}}{m_{x_0}^2}.
```

From 04-branch-fall@v3 (this subproject). Setting there: a body of the class $`\mathcal C_{\rm lev}`$ with linear level profiles (as under "Goal", with $`V_k=0`$), a medium with the records $`K_x=\kappa\,x\,X`$, branch starts $`B_{k,\sigma}[g]`$ as under "Goal"; first order in the gradients of the level $`k`$; records at leading order in $`\kappa`$. Inside one level the index $`k`$ is dropped: $`\tau,M,G,\mathcal F,g_\zeta,\omega`$; a prime is $`\partial_p`$; $`\mathsf b:=\lvert G\rvert+M\lvert g_\zeta\rvert+\lvert\mathcal F\rvert`$; $`X_g:=\bigl(\int\frac{\mathrm dp}{2\pi}\lvert g'\rvert^2\bigr)^{1/2}`$.

Eq. (4.1) of 04-branch-fall, exact, with the spectral decomposition $`X=\sum_\xi\xi\,Q_\xi`$; $`p^{[\xi]}`$ are the place weights of the body alone under $`C_b+\kappa\xi\hat x`$, that is with the plain gradients $`\mathcal F^{\rm body}_k-\kappa\xi`$, where $`\mathcal F^{\rm body}_k`$ is the plain gradient of the body contract itself:

```math
p_x(\lambda)=\sum_\xi\lVert Q_\xi\chi\rVert^2\,p^{[\xi]}_x(\lambda),
```

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

Eq. (4.17) of 04-branch-fall, with $`v:=\sigma\,\omega_k'(p_0)`$, the velocity of the branch start at zero gradients in position labels per unit of $`\lambda`$; the two coefficients are exact, $`O(v^4)`$ is an order estimate at fixed level data:

```math
a_{k,\sigma}=\frac{\tau^2}{M}(\sigma\mathcal F-G)+c_{2,k,\sigma}\,v^2+O(v^4),\qquad
c_{2,k,\sigma}=g_\zeta+\frac GM\Bigl(1+\frac{2M^2}{\tau^2}\Bigr)-\sigma\,\frac{\mathcal F}{M}\Bigl(\frac32+\frac{2M^2}{\tau^2}\Bigr).
```

Eq. (4.19) of 04-branch-fall, for every member of $`\mathcal C_{\rm lev}`$ with linear level profiles and $`N\ge2`$ levels:

```math
\begin{aligned}
a_{k,+}(0)=a_+\ \forall k&\iff\frac{\tau_k^2}{M_k}(\mathcal F_k-G_k)=a_+\ \forall k,\qquad
a_{k,-}(0)=a_-\ \forall k\iff\frac{\tau_k^2}{M_k}(\mathcal F_k+G_k)=-a_-\ \forall k,\\
\text{both, with }a_+=a_-=a&\iff\mathcal F_k=0\ \text{ and }\ \frac{\tau_k^2G_k}{M_k}=-a\quad\forall k .
\end{aligned}
```

Eq. (4.20) of 04-branch-fall. $`a_{k,+}`$ is the same function of $`v`$ through the order $`v^2`$ for all $`k`$ if and only if (i) $`\frac{\tau_k^2}{M_k}(\mathcal F_k-G_k)=a_0`$ for all $`k`$ and (ii) $`c_{2,k,+}`$ does not depend on $`k`$; with (i) inserted in (4.17), exactly:

```math
c_{2,k,+}=g_{\zeta,k}-\frac{\mathcal F_k}{2M_k}-\frac{a_0}{\tau_k^2}\Bigl(1+\frac{2M_k^2}{\tau_k^2}\Bigr)\quad\text{independent of }k .
```

Eq. (4.21) of 04-branch-fall, in the regime $`M_k\ll\tau_k`$, with $`c^{(0)}_{2,k}:=g_{\zeta,k}+\frac{G_k}{M_k}-\frac{3\mathcal F_k}{2M_k}`$; to leading order the condition is (i) together with

```math
c^{(0)}_{2,k}=g_{\zeta,k}-\frac{\mathcal F_k}{2M_k}-\frac{a_0}{\tau_k^2}\quad\text{independent of }k;\qquad\text{then exactly}\quad c_{2,k,+}-c_{2,k',+}=-2a_0\Bigl(\frac{M_k^2}{\tau_k^4}-\frac{M_{k'}^2}{\tau_{k'}^4}\Bigr).
```

Eq. (4.22) of 04-branch-fall, for the class $`\mathcal C`$ and every $`N\ge2`$:

```math
a_{k,+}(0)\ \text{level-independent}\iff\mathcal F=m(g_m-g_\eta);\qquad a_{k,-}(0)\ \text{level-independent}\iff\mathcal F=-m(g_m-g_\eta);\qquad\text{value }-\tau^2g_\eta\text{ in each case};
```

Eq. (4.23) of 04-branch-fall, for the class $`\mathcal C`$: the conditions under which $`a_{k,+}`$ is the same for all levels through the order $`v^2`$ (exactly for $`N=2`$ and for $`N\ge3`$, and to leading order in $`M_k/\tau`$):

```math
\begin{aligned}
N=2:&\quad\mathcal F=m(g_m-g_\eta)=-\frac{4g_\eta}{\tau^2}\,m\Bigl(m+\frac{\pi}{\lambda_0}\Bigr)\Bigl(2m+\frac{\pi}{\lambda_0}\Bigr),\quad g_\eta,\ g_\zeta\ \text{free};\\
N\ge3:&\quad g_m=g_\eta=0,\ \mathcal F=0,\quad g_\zeta\ \text{free}\quad(\text{so }a_0=0);\\
M_k\ll\tau,\ \text{leading order, every }N\ge2:&\quad\mathcal F=0,\ g_m=g_\eta=:g,\quad g_\zeta\ \text{free}.
\end{aligned}
```

Eq. (4.24) of 04-branch-fall, for the class $`\mathcal C`$ under the hypothesis $`a_{k,+}(0)=a\neq0`$ for all $`k`$, at first order in the gradients and at leading order in $`\kappa`$. Here $`r(x)=\eta_x/\lambda_0`$ is the rate (3.23) in its wide-start form, $`d_0:=\kappa\sigma_X`$ is the distance of neighbouring positions in the background of (17.15), $`\bar x=d_0\,\bar x_{\rm lab}\,\hat e`$ with $`\hat e:=e/\sigma_X`$, and $`v_{\max}=\tau d_0`$ is the bound (5.11) of 04-ilang-time/05-moving-clock:

```math
\boxed{\;\frac{\mathrm d^2\bar x}{\mathrm d\lambda^2}\Big\vert_{\rm drift}=d_0\,a_{k,+}(0)\,\hat e=-\,\frac{v_{\max}^2}{d_0}\;\frac{r(x+1)-r(x)}{r(x)}\;\hat e\;}
```

Eq. (4.25) of 04-branch-fall, the variants, with $`\tau_k=\tau`$, $`M_k=m+d_k`$ and $`\ell_k:=1+2M_k^2/\tau^2`$; "same for all levels" is meant for every $`N\ge2`$ and $`g\neq0`$ (in (f) also $`c_{\rm f}\neq0`$); the last three columns: from rest in the upper branch, from rest in the lower branch, through the order $`v^2`$:

```math
\begin{array}{l|c|c|c|c|c|c}
\text{variant}&a_{k,+}(0)&a_{k,-}(0)&c_{2,k,\sigma}&\text{rest, upper}&\text{rest, lower}&\text{through }v^2\\\hline
\text{(a)}&-\tau^2g&-\tau^2g&g\,\ell_k&\text{yes}&\text{yes}&\text{exactly no; leading order in }M_k/\tau\text{ yes}\\
\text{(b1)}&-\tau^2\frac{mg}{M_k}&-\tau^2\frac{mg}{M_k}&\frac{mg}{M_k}\ell_k&\text{no}&\text{no}&\text{no}\\
\text{(b2)}&-\tau^2\frac{d_kg}{M_k}&-\tau^2\frac{d_kg}{M_k}&\frac{d_kg}{M_k}\ell_k&\text{no}&\text{no}&\text{no}\\
\text{(c)}&-\tau^2g&-\tau^2g&g\,(1+\ell_k)&\text{yes}&\text{yes}&\text{exactly no; leading order in }M_k/\tau\text{ yes}\\
\text{(d)}&+\frac{\tau^2\mathcal F}{M_k}&-\frac{\tau^2\mathcal F}{M_k}&-\sigma\frac{\mathcal F}{M_k}\bigl(\tfrac12+\ell_k\bigr)&\text{no}&\text{no}&\text{no}\\
\text{(f)}&-\tau^2g\bigl(1+\frac{c_{\rm f}}{M_k}\bigr)&-\tau^2g\bigl(1-\frac{c_{\rm f}}{M_k}\bigr)&g\,\ell_k+\sigma\frac{c_{\rm f}g}{M_k}\bigl(\tfrac12+\ell_k\bigr)&\text{no}&\text{no}&\text{no}
\end{array}
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- No object other than $`b`$ has the type of $`b`$, and $`c`$ is the only instance of its type.
- The members of $`\mathcal C_{\rm lev}`$, the linear level profiles, the branch starts and the level-superposed starts are assumptions of this package (M8, M9).
- Standard facts on perturbation theory in a term of the contract, on plane waves and on the averaging of oscillating terms may be used; state them with their conditions.

## Scope

- **Class.** Item 1: every member of $`\mathcal C_{\rm lev}`$ with linear level profiles, both branches, every $`\alpha`$ and every $`g`$. Item 2: the same members with zero gradients in (b)–(d), every level, both branches, every $`\chi`$ with finite moments of $`X`$. Item 3: the stated on-site blocks with arbitrary hopping factors. Item 4: as the quoted results state.
- **Controls.** A body with a level-dependent fall against one with a level-independent fall (item 1); a sharp $`X`$ against a spread one, and a symmetric distribution of $`X`$ against a skewed one (item 2); $`u_k=0`$ against $`u_k\neq0`$ (item 3).
- In scope:
  - the position statistics, the label drift and the coherences of a start in a superposition of levels;
  - the leading effect of the records beyond the effective body contract on the mean velocity and acceleration;
  - the dependence of the fall on the operator that the factor multiplies;
  - a table of the orders of all deviations.
- Out of scope:
  - the second order in the gradients beyond what item 1(f) asks, profiles that are not linear, and long falls;
  - terms that mix the records beyond the effective contract with the gradients $`G_k`$, $`g_{\zeta,k}`$ (third order);
  - bodies of two types, a field object, and fields that are not sharp;
  - any physical meaning beyond the definitions (M1–M4); no theory of gravity and no theory that contains time may be used as an input.

## Depth

- Item 1: (a)–(d) short argument; (e) derive; (f) short argument.
- Item 2: (a) short argument; (b), (c) derive; (d) short argument.
- Item 3: short argument.
- Item 4: standard (a table of results with their tags).

## Expected result

- Item 1: a relation with a yes/no answer; a closed form and an equivalence; a leading term with a table; values and a yes/no answer; a rate, an equivalence and a yes/no answer; a formula, an order and a leading term with its conditions.
- Item 2: a yes/no answer with its reason; two leading terms with bounds or estimates; a closed form with its expansion and an equivalence; an expression in background quantities and a range.
- Item 3: closed forms and three equivalences; four yes/no answers; two evaluations.
- Item 4: a table.

Give every main result a tag $`(7.k)`$.

Consistency checks, at most three: for example one level only ($`\alpha_k=\delta_{kk_0}`$), a sharp $`X`$, and all gradients zero.

## Code

None.
