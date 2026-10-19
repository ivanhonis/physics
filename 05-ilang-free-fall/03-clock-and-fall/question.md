# Question: 03-clock-and-fall

- **Subproject:** 05-ilang-free-fall
- **Package:** 03-clock-and-fall
- **Equation tags:** (3.k)
- **Created:** 2026-10-10

## Goal

For a body of the Model D kind whose contract contains position-dependent factors, determine how the rate of the carried clock depends on the place of the body, and how the body accelerates from rest, and compare several ways in which the factors can enter. This is criterion 2 and the part of criterion 3 that concerns a body at rest.

**Setting.**
- **Objects.** A body $`b`$, the only instance of its type, and a recording medium $`c`$, one object of another type. There is no field object in this package: the position-dependent factors are written into the body's own contract, which is an admissible description (A10) and an assumption of this package (M8). How such factors arise from a field object is the subject of 02-field-object.
- **Body contract (the class $`\mathcal C`$).** Places $`(x,s,a)`$ as for Model D, with $`x\in\mathbb Z`$ as the limit of long finite chains (A1); state how the limit is taken. With real numbers $`m_x>0`$, $`\eta_x>0`$, $`\zeta_x>0`$ and $`V_x`$:
  ```math
  C_b=A_\zeta+\sum_x\lvert x\rangle\langle x\rvert\otimes\Bigl[\sigma_3\otimes(m_x\mathbb 1_N+\eta_xD)+V_x\,\mathbb 1_2\otimes\mathbb 1_N\Bigr],\qquad A_\zeta=\frac\tau2\sum_x\zeta_x\Bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\Bigr)\otimes\mathbb 1_N ,
  ```
  with $`\tau>0`$ and $`D`$, $`\lambda_0`$, $`N`$ as for Model D. Model D is the member $`m_x=m`$, $`\eta_x=1`$, $`\zeta_x=1`$, $`V_x=0`$. $`m_x`$ is the **rest profile**, $`\eta_x`$ the **clock profile**, $`\zeta_x`$ the **bond profile** and $`V_x`$ the **plain part**. With $`d_k:=\frac{2\pi k}{N\lambda_0}`$, the on-site block at $`x`$ on the clock level $`k`$ (clock label in $`\lvert f_k\rangle`$) is $`(m_x+\eta_xd_k)\,\sigma_3+V_x\mathbb 1_2`$.
- **Records.** $`K_x=\kappa\,x\,X`$ as for Model D. The profiles above are those of the effective body contract (8.19): the term $`\kappa\,x\,\langle X\rangle`$ of the records is counted in the plain part $`V_x`$.
- **Linear profiles.** $`m_x=m\,(1+g_m x)`$, $`\eta_x=1+g_\eta x`$, $`\zeta_x=1+g_\zeta(x+\tfrac12)`$, $`V_x=-\mathcal F\,x`$, on a chain $`\lvert x\rvert\le L`$ with $`\lvert g_\bullet\rvert(L+1)<1`$. The **gradients** are $`g_m`$, $`g_\eta`$, $`g_\zeta`$ and $`\mathcal F`$. Named variants, each with one number $`g`$:
  - (a) a factor on the rest and clock term: $`g_m=g_\eta=g`$, $`g_\zeta=0`$, $`\mathcal F=0`$;
  - (b1) a factor on the rest term only: $`g_m=g`$, the others zero;
  - (b2) a factor on the clock term only: $`g_\eta=g`$, the others zero;
  - (c) a factor on the whole body contract: $`g_m=g_\eta=g_\zeta=g`$, $`\mathcal F=0`$;
  - (d) a plain gradient: $`\mathcal F\neq0`$, the others zero (the case of 06-inertia-internal-energy and 09-proper-time).
- **Regime.** Weak records, as in 04-ilang-time. With $`p_x(\lambda)`$ the place weights of the view of the body, the **mean position label** is $`\bar x_{\rm lab}(\lambda):=\sum_xx\,p_x(\lambda)`$, and the position in the background (17.15) is $`\bar x=\kappa\,\bar x_{\rm lab}\,e`$. The label $`\bar x_{\rm lab}(\lambda)`$ and the clock statistics are asked in the limit $`\kappa\to0`$ at fixed $`\lambda`$, fixed chain and fixed start; state the order of what is neglected.
- **Starts.** The start of the system is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$. For a position $`x_0`$, the body starts in one of:
  - $`S_k(x_0)`$: $`\phi=\phi_X\otimes\lvert1\rangle\otimes\lvert f_k\rangle`$ with $`\phi_X(x)=c_W\,w\bigl((x-x_0)/W\bigr)`$, where $`w`$ is real and smooth with support in $`[-1,1]`$ and $`c_W`$ normalizes; branch label $`s=1`$, clock level $`k`$. Its mean plane-wave label is $`0`$ ("at rest").
  - $`S'_k(x_0)`$: the same with the branch label $`s=2`$.
  - $`S_{\rm clock}(x_0)`$: the same as $`S_k(x_0)`$ with the clock label in the place $`\lvert0\rangle`$ instead of $`\lvert f_k\rangle`$.
- **Clock reading.** One class per clock label, with statistics $`q(a;\lambda)`$.
- **Orders.** "First order in the gradients" means: first order jointly in $`g_m,g_\eta,g_\zeta,\mathcal F`$ at fixed $`\lambda`$, fixed start and fixed chain, taken before the limit of a long chain and before any limit of a wide start. "First order in the level spacing" is meant as in (5.21).

1. **Exact relations.** For every member of $`\mathcal C`$ (arbitrary profiles) and every start of the body, in the weak-record regime:
   - Determine the operators whose expectations are $`\mathrm d\bar x_{\rm lab}/\mathrm d\lambda`$ and $`\mathrm d^2\bar x_{\rm lab}/\mathrm d\lambda^2`$.
   - Determine $`\mathrm d^2\bar x_{\rm lab}/\mathrm d\lambda^2`$ at $`\lambda=0`$ for the starts $`S_k(x_0)`$ and $`S'_k(x_0)`$.

2. **Acceleration from rest.** Linear profiles, start $`S_k(x_0)`$.
   - (a) Determine $`\mathrm d^2\bar x_{\rm lab}/\mathrm d\lambda^2`$ to first order in the gradients as a function of $`\lambda`$, and its limit for a wide start ($`W\to\infty`$ after the limit of a long chain). State what the limit requires of $`W`$, $`L`$, $`x_0`$ and $`\lambda`$.
   - (b) Determine the average of this acceleration over windows $`[\lambda_1,\lambda_1+\Lambda]`$ that are long compared with the inverse of the gap between the two branches, and the coefficient of each gradient in the average in the limit of a long window. State the range in which the first-order treatment is valid, and say for each statement whether it is exact or an order estimate.
   - (c) Express the averaged acceleration through quantities that are well defined (M6): the on-site blocks and the hopping blocks of the effective body contract (8.19) and their differences between neighbouring positions.
   - (d) Evaluate the averaged acceleration for the variants (a), (b1), (b2), (c) and (d). For each variant, determine whether it depends on $`m`$, on the clock level $`k`$, on $`N`$ and $`\lambda_0`$, and on $`\tau`$.
   - (e) Determine the averaged acceleration for the start $`S'_k(x_0)`$, for the same variants.

3. **Clock rate at a place.**
   - (a) **Uniform profiles.** Let $`m_x=m_\ast`$, $`\eta_x=\eta_\ast`$, $`\zeta_x=\zeta_\ast`$, $`V_x=V_\ast`$ for all $`x`$. For the clock-carrying start of 05-moving-clock built with this contract (concentrated near a plane-wave label $`p_0`$, spinor of the upper branch of level $`0`$, clock label in $`\lvert0\rangle`$), determine $`q(a;\lambda)`$ to first order in the level spacing, in the form of (5.21), and the tick at $`p_0=0`$ as a function of $`m_\ast`$, $`\eta_\ast`$, $`\zeta_\ast`$ and $`V_\ast`$.
   - (b) **Linear profiles.** For the start $`S_{\rm clock}(x_0)`$, determine $`q(a;\lambda)`$ to first order in the level spacing and to zeroth order in the gradients at fixed $`g_\bullet x_0`$: the limit $`g_\bullet W\to0`$, $`g_\bullet\tau\lambda\to0`$, $`\mathcal F\lambda\to0`$ at fixed values of the profiles at $`x_0`$. Define from it the **rate at $`x_0`$**, the rate of change of the advance in $`q`$ with $`\lambda`$. Determine the order (the powers of $`g_\bullet W`$ and of the gradients times $`\lambda`$) at which the width of the start and the beginning motion first change $`q`$, with the reason.
   - (c) **Two places.** For two positions $`x_1\neq x_2`$, determine the ratio of the rates at $`x_1`$ and at $`x_2`$, for the variants (a), (b1), (b2), (c) and (d). State how the two rates are compared, and whether the ratio depends on the unit of $`\lambda`$, on $`m`$, on $`N`$ and $`\lambda_0`$.

4. **Comparison.** For each of the five variants state: whether the acceleration from rest is the same for all clock levels and all $`m`$; whether the clock rate depends on the place. State which variants have both properties.

## Inputs

From 05-moving-clock@v3 of 04-ilang-time. Setting there: one Model D body with the contract $`C_b=C_{\rm D}`$ of the base problem, the records $`K_x=\kappa xX`$, and the start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$. Notation fixed there:
- $`d_k:=\frac{2\pi k}{N\lambda_0}`$, $`\epsilon:=\frac{2\pi}{N\lambda_0m}`$ (the level spacing relative to the rest term), so $`d_k=km\epsilon`$;
- the plane waves $`\lvert p\rangle=\sum_xe^{ipx}\lvert x\rangle`$, $`p\in(-\pi,\pi]`$;
- $`P_N(a;\vartheta)=\sin^2(\pi\vartheta)/\bigl(N^2\sin^2(\pi(\vartheta-a)/N)\bigr)`$, the reading distribution of the ring clock at rest as a function of the advance $`\vartheta`$ ((5.1) there), and $`\gamma:=m/\omega_0(p_0)`$;
- the weak-record regime, and the clock-carrying start (concentrated near $`p_0`$ with spread $`\delta p`$, spinor of the positive branch of level $`0`$, clock label in $`\lvert0\rangle`$).

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

Eq. (5.20), with $`\bar d:=\frac1N\sum_kd_k=\frac{N-1}2m\epsilon=\langle0\vert D\vert0\rangle`$, $`\bar\mu:=m+\bar d`$ and $`j:=k-\frac{N-1}2`$:

```math
\omega_k=\bar\omega+\Gamma\,m\epsilon j+\tfrac12\bar c\,(m\epsilon j)^2+\bar\rho_k,\qquad
\bar\omega(p):=\sqrt{\bar\mu^2+\tau^2\sin^2p},\quad\Gamma(p):=\frac{\bar\mu}{\bar\omega(p)},\quad\bar c:=\frac{\tau^2\sin^2p}{\bar\omega^3}\le\frac1m,\quad\lvert\bar\rho_k\rvert\le\frac{(m\epsilon\lvert j\rvert)^3}{6m^2}.
```

Eq. (5.21), for the clock-carrying start in the weak-record regime; the remainder is $`\mathcal R=O\bigl((N\epsilon)^2(1+\lambda/\lambda_0)^2\bigr)+O(\delta p^2)+O(\kappa)`$:

```math
q(a;\lambda)=P_N\Bigl(a;\Gamma(p_0)\frac{\lambda}{\lambda_0}\Bigr)+\mathcal R,\qquad
\Gamma(p_0)=\frac{\bar\mu}{\sqrt{\bar\mu^2+\tau^2\sin^2p_0}}=\gamma\Bigl[1+\frac{(N-1)\epsilon}2\bigl(1-\gamma^2\bigr)\Bigr]+O\bigl((N\epsilon)^2\bigr),\quad\gamma:=\frac m{\omega_0(p_0)} .
```

Eq. (5.22), the tick of the first-order distribution (5.21) and its ratio to the tick at $`p_0=0`$, with $`\omega:=\omega_0(p_0)`$:

```math
\lambda_0(p_0)=\frac{\lambda_0}{\Gamma(p_0)},\qquad
R(p_0):=\frac{\lambda_0(p_0)}{\lambda_0(0)}=\frac{\bar\omega(p_0)}{\bar\mu}=\sqrt{1+\frac{\tau^2}{\bar\mu^2}\sin^2p_0}=\frac\omega m\Bigl[1-\frac{(N-1)\epsilon}2\,\frac{\tau^2\sin^2p_0}{\omega^2}\Bigr]+O\bigl((N\epsilon)^2\bigr)\ \ge1 .
```

From 06-inertia-internal-energy@v3 of 04-ilang-time. Setting there: one Model D body with a uniform cost gradient added to its diagonal entries; start concentrated near the plane-wave label $`0`$ with branch label $`s=1`$ and clock level $`k`$; weak records. Notation fixed there:
- $`M_k:=m+d_k`$, the rest cost of level $`k`$; the gap between the branches at rest is $`2M_k`$;
- $`\bar m`$ is the mean position label (called $`\bar x_{\rm lab}`$ here), $`\hat x`$ and $`\hat p`$ the position label and the plane-wave label as operators, $`C_k(p)`$ the block (5.5) with $`\mu_k=M_k`$;
- $`\mathcal F`$ is the force on the position label: the on-site entries of the effective body contract are $`-\mathcal F x`$ plus a constant, and $`\mathcal F=\kappa\,g(e,F)`$ for a force $`F\in\mathcal H_c`$, with $`g(v,w)=\mathrm{Re}\langle v\vert w\rangle`$ and $`e=(X-\langle X\rangle)\chi`$;
- $`a:=\mathrm d^2\bar x/\mathrm d\lambda^2`$; $`\overline{(\cdot)}`$ is the average over $`[\lambda_1,T]`$ with $`T=\lambda_1+\Lambda`$; $`n:=e/\sigma_X`$ and $`d_1:=\kappa\sigma_X`$.

Eq. (6.12):

```math
\dot{\bar m}=\langle\hat v\rangle,\quad \hat v=-\tau\cos\hat p\,\sigma_1;\qquad
\ddot{\bar m}=\langle\hat a_k\rangle,\quad \hat a_k=i[C_k,\hat v]-i\mathcal F[\hat x,\hat v]=2\tau M_k\cos\hat p\,\sigma_2+\mathcal F\tau\sin\hat p\,\sigma_1 .
```

Eq. (6.13), at first order in $`F`$:

```math
a(\lambda)=\frac{2\tau^2}{M_k}\,\sin^2(M_k\lambda)\;\kappa^2\,g(e,F)\,e+O(F^2)\qquad(\text{fixed }\lambda).
```

Eq. (6.24), exact for every interval:

```math
\rho:=\frac{\sin(2M_kT)-\sin(2M_k\lambda_1)}{2M_k\Lambda},\qquad \lvert\rho\rvert\le\frac{1}{M_k\Lambda},\qquad \overline{2\sin^2(M_k\lambda)}=1-\rho .
```

Eq. (6.14), which defines the additive error $`\mathcal E`$. Here $`\mathcal F_{\max}:=\max_\xi\lvert\mathcal F_\xi\rvert`$ over the sector forces $`\mathcal F_\xi:=\mathcal F-\kappa(\xi-\langle X\rangle)`$, with $`\xi`$ the eigenvalues of $`X`$ that occur in $`\chi`$; $`\mathcal E`$ is bounded there, in (6.26), for every interval with $`\mathcal F_{\max}T\le\pi/2`$:

```math
\overline{a}=\frac{\tau^2}{M_k}\,\kappa\,\bigl[\mathcal F+\mathcal E\bigr]\,e=\frac{\tau^2}{M_k}\,\kappa^2\,g(e,F)\,e+\frac{\tau^2}{M_k}\,\kappa\,\mathcal E\,e,\qquad
\frac{1}{2M_k}\ll\Lambda,\qquad \mathcal F_{\max}\,T\ll\min\Bigl(1,\frac{M_k}{\tau}\Bigr),
```

Eq. (6.15), the averaged inverse inertia: the coefficient of $`F`$ in $`\overline a`$ at first order in $`F`$, leading order in $`\kappa`$, in the long-interval limit:

```math
\mu_{\rm av}(k)=\frac{\tau^2}{M_k}\,\kappa^2\,e\,g(e,\cdot\,)=\frac{\tau^2}{m+d_k}\,\kappa^2\,e\,g(e,\cdot\,).
```

Eq. (6.20), the background inertia $`I_k`$ and the label inertia $`I^{\rm lab}_k`$:

```math
\mu_{\rm av}(k)=\frac{1}{I_k}\,n\,g(n,\cdot\,),\qquad
I_k:=\frac{M_k}{\tau^2\kappa^2\sigma_X^2}=\frac{I_k^{\rm lab}}{d_1^{\,2}},\qquad
I_k^{\rm lab}:=\frac{M_k}{\tau^2}\quad\bigl(\overline{\ddot{\bar m}}=\mathcal F/I_k^{\rm lab}\bigr).
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

Eq. (8.24), for a Model D type $`T`$: the two eigenvalues, on the plane wave with label $`0`$ and clock level $`k`$, of the part $`C^{\rm D}_T+c_T\mathbb 1`$ of the effective body contract that commutes with the translations of the position label, where $`c_A=-c_B=\langle Z\rangle`$ under (8.1):

```math
E^T_{k,\pm}=c_T\pm M^T_k,\qquad M^T_k:=m_T+\frac{2\pi k}{N_T\lambda_{0T}},\qquad\Delta^T_k:=E^T_{k,+}-E^T_{k,-}=2M^T_k ,
```

From 09-proper-time@v2 of 04-ilang-time. Setting there: a Model D body (body $`1`$) with the additional term $`G=-\mathcal F\hat x`$, $`\hat x:=\sum_xx\,P_x`$ (a plain gradient), in the weak-record regime; its start is $`\lvert\phi_1\rangle=\int\frac{\mathrm dp}{2\pi}g_1(p)\,\lvert p\rangle\otimes\beta_{0,+}(p)\otimes\lvert0\rangle`$ with $`g_1`$ concentrated near $`p_0`$ with variance $`\delta p^2`$; $`q_1(a;\lambda)`$ is its clock reading distribution, and $`\Gamma`$ is the function of (5.20).

Eq. (9.1), exact at $`\kappa=0`$, where $`\beta_k(p,\lambda)`$ solves $`i\,\partial_\lambda\beta_k=C_k(p+\mathcal F\lambda)\,\beta_k`$ with $`\beta_k(p,0)=\beta_{0,+}(p)`$:

```math
\lvert\psi_1(\lambda)\rangle=\int\frac{\mathrm dp}{2\pi}\,g_1(p)\,\lvert p+\mathcal F\lambda\rangle\otimes\frac1{\sqrt N}\sum_{k=0}^{N-1}\beta_k(p,\lambda)\otimes\lvert f_k\rangle,
\qquad
p(\lambda):=p_0+\mathcal F\lambda\ \ (\mathrm{mod}\ 2\pi),
```

Eq. (9.11):

```math
q_1(a;\lambda)=P_N\bigl(a;\vartheta_1(\lambda)\bigr)+\mathcal R_1,\qquad\mathcal R_1=O(\epsilon^2)+O(\delta p^2)+O(\kappa),
```

Eq. (9.12):

```math
\vartheta_1(\lambda):=\frac1{\lambda_0}\int_0^\lambda\Gamma\bigl(p_0+\mathcal F\lambda'\bigr)\,\mathrm d\lambda'=\frac{\mathcal I(p_0+\mathcal F\lambda)-\mathcal I(p_0)}{\mathcal F\lambda_0},\qquad
\mathcal I(\varphi):=\int_0^\varphi\frac{\bar\mu\,\mathrm dp}{\sqrt{\bar\mu^2+\tau^2\sin^2p}} .
```

Eq. (9.13):

```math
\lambda_0\,\frac{\mathrm d\vartheta_1}{\mathrm d\lambda}=\Gamma\bigl(p(\lambda)\bigr)=\frac{\bar\mu}{\sqrt{\bar\mu^2+\tau^2\sin^2p(\lambda)}} ,
```

From 03-ilang-space/17-motion@v2. Setting there: $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$; the start is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, $`\lvert u_h\rangle:=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$, $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$; with $`p_h(\lambda)`$ the place weights of the view of $`b`$, $`\bar x(\lambda):=\sum_hp_h(\lambda)\,u_h`$.

Eq. (17.15), for the chain $`h_m`$, $`m\in\mathbb Z`$, with $`K_{h_m}=m\,X`$, $`X`$ self-adjoint on $`\mathcal H_c`$, $`\sigma_X:=(\langle X^2\rangle-\langle X\rangle^2)^{1/2}>0`$ and $`e:=(X-\langle X\rangle)\chi`$, so that $`\lVert e\rVert=\sigma_X`$ and $`u_{h_m}=m\,e`$:

```math
d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X,\qquad \bar x=\bar m\,e,\quad \bar m:=\sum_mm\,p_{h_m},\qquad s^2=\sigma_X^2\sum_m(m-\bar m)^2p_{h_m} .
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- No object other than $`b`$ has the type of $`b`$, and $`c`$ is the only instance of its type.
- The members of the class $`\mathcal C`$, the linear profiles and the starts $`S_k`$, $`S'_k`$, $`S_{\rm clock}`$ are assumptions of this package (M8). The branch label of a start is part of the assumption (M9); item 2(e) asks for the other branch.
- Standard facts on first-order perturbation theory in a term of the contract, on plane waves and on the averaging of oscillating terms may be used; state them with their conditions.

## Scope

- **Class.** Item 1: every member of $`\mathcal C`$ and every start. Items 2 and 3(b), 3(c): linear profiles and the stated starts. Item 3(a): uniform profiles and the clock-carrying start. Item 4: the five named variants.
- **Controls.** The variants (b1), (b2) and (d), and the start $`S'_k`$, are the controls of this package.
- In scope:
  - the exact velocity and acceleration operators of the class;
  - the acceleration from rest to first order in the gradients, and its average;
  - the rate of the carried clock at a place, and the ratio of the rates at two places;
  - the comparison of the five variants.
- Out of scope:
  - a body that starts with a nonzero plane-wave label, the dependence of the acceleration on the speed, and long falls (a later package);
  - a clock in a superposition of levels that falls over many ticks, beyond item 3(b) (a later package);
  - necessary and sufficient conditions for a fall that does not depend on the body, and the relation between the clock rates and the acceleration (a later package; this package supplies the formulas);
  - a field object, and fields that are not sharp (02-field-object);
  - effects of the records beyond leading order in $`\kappa`$;
  - any physical meaning beyond the definitions (M1–M4); no theory of gravity may be used as an input.

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: derive.
- Item 4: short argument.

## Expected result

- Item 1: two operators in closed form; two values.
- Item 2: a closed form in $`\lambda`$ and its limit with conditions; a closed form for the average, its coefficients, a range of validity; an expression in well-defined quantities; a table for the variants with yes/no answers; a table for the other branch.
- Item 3: a distribution to the stated order and a closed form for the tick; a distribution to the stated order, a definition and the orders of the first corrections; ratios for the five variants with yes/no answers.
- Item 4: a table of yes/no answers.

Give every main result a tag $`(3.k)`$.

Consistency checks, at most three: for example all gradients zero, variant (d) against (6.13)–(6.15), and $`\tau\to0`$.

## Code

None.
