# Question: 08-two-types

- **Subproject:** 05-ilang-free-fall
- **Package:** 08-two-types
- **Equation tags:** (8.k)
- **Created:** 2026-10-11

## Goal

For two bodies of different types that are recorded by one medium and whose contracts carry position-dependent factors, determine the conditions under which they fall alike and under which their clocks respond alike, how the two sets of conditions are related, what a common field and a common maximal speed contribute, and which of these statements are the same in every equivalent description. This is criterion 7.

**Setting.**
- **Objects.** Two bodies $`b_1`$, $`b_2`$ of different types, each the only instance of its type, and a medium $`c`$ of a third type. There is no contract between the two bodies. In item 5 a field object $`f`$ of a fourth type is added.
- **Body contracts.** For $`i=1,2`$ the body $`b_i`$ is of the class $`\mathcal C`$ of 03-clock-and-fall (quoted under "Inputs") with its own data: $`\tau_i>0`$, $`m_i>0`$, a clock with $`N_i\ge2`$ places and the tick parameter $`\lambda_{0,i}`$ (so $`d^{(i)}_k:=\frac{2\pi k}{N_i\lambda_{0,i}}`$, $`M^{(i)}_k:=m_i+d^{(i)}_k`$), and linear profiles with the gradients $`g_{m,i}`$, $`g_{\eta,i}`$, $`g_{\zeta,i}`$, $`\mathcal F_i`$ on a chain $`\lvert x\rvert\le L`$. The position dependence is written into the bodies' own contracts in items 1–4 and 6 (A10, M8).
- **Records.** One medium records both bodies through the same operator: $`C=C_1+C_2+\kappa_1\,\hat x_1\otimes X+\kappa_2\,\hat x_2\otimes X`$ with $`\kappa_1,\kappa_2>0`$, $`X`$ self-adjoint on $`\mathcal H_c`$, and a product start with the medium in $`\chi`$, $`\sigma_X>0`$. As in 04-branch-fall, the profiles of each body are those of its effective body contract, (8.19) of 04-ilang-time/08-maximal-speed, so the term $`\kappa_i\,x\,\langle X\rangle`$ is counted in $`V^{(i)}_x`$; results are asked in the weak-record regime, $`\kappa_1,\kappa_2\to0`$ at fixed $`\lambda`$, chain and start.
- **Background quantities of a type.** By (17.15) applied to each body, the positions of $`b_i`$ have the record vectors $`u^{(i)}_x=\kappa_i\,x\,e`$. For the type $`i`$: $`d_{0,i}:=\kappa_i\sigma_X`$ is the distance of neighbouring positions; $`v_i:=\tau_i\,d_{0,i}`$ is the bound (5.11) of 04-ilang-time/05-moving-clock at zero gradients; $`a^{(i)}_{k,\sigma}(0)`$ is the drift acceleration from rest of the level $`k`$ and the branch $`\sigma`$, (4.16) of 04-branch-fall, in position labels; $`A^{(i)}_{k,\sigma}:=d_{0,i}\,a^{(i)}_{k,\sigma}(0)`$ is the coefficient of $`\hat e:=e/\sigma_X`$ in the acceleration of $`\bar x_i`$, as in (4.24). Only velocities and accelerations of the two bodies, and differences of positions of one body, are used; the position of one body relative to the other is not used.
- **Responses of the clocks.** $`r_i(x)`$ is the rate (3.23) of the type $`i`$ in its wide-start form. The **response per label** $`\varrho_i`$ is the first order in the gradients of $`\bigl(r_i(x+1)-r_i(x)\bigr)/r_i(x)`$; the **response per distance** is $`\varrho_i/d_{0,i}`$.
- **Schedules and equivalences (item 6).** As in 05-rate-comparison, with each of the three objects as one class: a **reading of an object** is a partition of its places, applied directly at a stated value of $`\lambda`$ (A8); a **schedule** is a finite list of events (an object, a reading of it, a value $`\lambda_j\ge0`$), applied in the order of increasing $`\lambda_j`$ with the evolution (1.9) between them, and its statistics is the joint distribution of the outcomes; a **re-timing** is a number $`a_o>0`$ for every object that is read and a contract $`C'`$ on the same objects (self-adjoint, independent of $`\lambda`$, a sum of pair terms), and it replaces $`\lambda_j`$ by $`a_{o_j}\lambda_j`$; it is an **equivalence of $`C`$** if, for every start and every schedule, the statistics of the re-timed schedule under $`C'`$ equal those of the original schedule under $`C`$; the **relative factor** of two objects is **detectable** if every equivalence has equal factors for them. If the medium is declared **not read**, schedules contain no event of the medium and no factor is assigned to it.

1. **One type in the background.** For each type $`i`$:
   - (a) State the condition under which $`A^{(i)}_{k,+}`$ is the same for all levels, and its value, from (4.22); express the value through $`v_i`$, $`d_{0,i}`$ and $`\varrho_i`$.
   - (b) Determine which of the following are well defined (M6), that is, unchanged under the replacements (8.1) of 04-ilang-time/08-maximal-speed, under a change of the unit of $`\lambda`$ ($`\lambda\to s\lambda`$ with $`C\to C/s`$), and under $`X\to tX`$, $`\kappa_i\to\kappa_i/t`$: $`\tau_i`$, $`\kappa_i`$, $`d_{0,i}`$, $`v_i`$, $`\varrho_i`$, $`\varrho_i/d_{0,i}`$, $`A^{(i)}_{k,+}`$, $`A^{(i)}_{k,+}/v_i^2`$; and the ratios of these quantities between the two types.

2. **Fall alike.** The two types **fall alike from rest** if $`A^{(i)}_{k,+}`$ has one value $`A\neq0`$ for all levels of both types.
   - (a) Determine the necessary and sufficient condition on the data of the two types. Express it through $`v_1`$, $`v_2`$ and the responses of the clocks.
   - (b) Determine the same for both branches (one value for all levels, both branches and both types).
   - (c) Determine the condition under which the accelerations in position labels, $`a^{(i)}_{k,+}(0)`$, are equal for the two types, and state whether this is a well-defined statement.

3. **Clocks respond alike.** Determine the condition under which the responses per label are equal, and the condition under which the responses per distance are equal. State which of the two compares the two clocks over the same distance of the background, and what each relies on (A8).

4. **Relation.**
   - (a) Determine whether "the two types fall alike from rest" implies "their clocks respond alike per distance", and whether the converse holds. In each direction determine the necessary and sufficient further condition.
   - (b) Give two controls within the setting, each with a fall that is the same for all levels within each type: a pair that falls alike from rest while the clocks respond differently, and a pair whose clocks respond alike while the two types fall differently.
   - (c) State what a common maximal speed, $`v_1=v_2`$, adds in each direction.

5. **A common field.** Let the body contracts be Model D contracts $`C^{\rm D}_i`$ (with $`\tau_i`$, $`m_i`$, $`N_i`$, $`\lambda_{0,i}`$), and let a field object $`f`$ with a self-adjoint $`\Phi`$ and a contract $`C_f`$ on $`\mathcal H_f`$ be coupled to both bodies:
   ```math
   C=C^{\rm D}_1+C^{\rm D}_2+\sum_{i=1,2}\kappa_i\,\hat x_i\otimes X+\sum_{i=1,2}B_i\otimes\Phi+C_f,\qquad B_i:=\theta_i\,\hat x_i\otimes\sigma_3\otimes\bigl(m_i\mathbb 1_{N_i}+D_i\bigr),
   ```
   with real numbers $`\theta_1`$, $`\theta_2`$ (the couplings per label) and $`D_i`$ the clock operator of the type $`i`$. The field starts in a state $`\varphi`$ with $`\Phi\varphi=\gamma\varphi`$ and $`C_f\varphi=e_f\varphi`$ (a sharp and stationary field; an assumption, A11).
   - (a) Determine the generator of the evolution of the two bodies and the medium (the form that (2.3) takes for two bodies coupled to one field), and the gradients $`g_{m,i}`$, $`g_{\eta,i}`$, $`g_{\zeta,i}`$, $`\mathcal F_i`$ of each type. State the range of $`\gamma`$ on a chain $`\lvert x\rvert\le L`$ for which the effective contracts are of the class $`\mathcal C`$.
   - (b) Translate the conditions of items 1(a), 2, 3 and 4 into conditions on $`\theta_1`$, $`\theta_2`$, $`\tau_1`$, $`\tau_2`$, $`\kappa_1`$, $`\kappa_2`$. Determine which of them hold for every sharp value $`\gamma`$ once they hold for one $`\gamma\neq0`$.
   - (c) Determine which of the following statements are well defined (M6): "$`\theta_1=\theta_2`$", the value of $`\theta_1/\theta_2`$, "$`\theta_1/d_{0,1}=\theta_2/d_{0,2}`$", the value of $`\theta_i\gamma`$. Use (2.20) and the replacement $`\Phi\to t\Phi`$, $`\theta_i\to\theta_i/t`$.
   - (d) State which condition on the couplings deserves the name "a common coupling" for the fall, and which for the clocks.

6. **Equivalent descriptions.** For the contract of the setting (items 1–4), with both bodies of the class $`\mathcal C`$ with $`\tau_i>0`$, and with the results (5.19)–(5.21) and (5.25) of 05-rate-comparison:
   - (a) Determine when the relative factor of the two bodies is detectable: with the medium read, and with the medium not read.
   - (b) For the equivalence (5.20) with the factors $`a_1`$, $`a_2`$, determine how the following change: $`\tau_i`$, $`m_i`$, $`\lambda_{0,i}`$, $`\kappa_i`$, the gradients, $`d_{0,i}`$, $`v_i`$, $`\varrho_i`$, $`\varrho_i/d_{0,i}`$, $`A^{(i)}_{k,+}`$, $`A^{(i)}_{k,+}/v_i^2`$.
   - (c) Determine which of the following statements are the same in every equivalent description, with the medium read and with the medium not read: "the two types fall alike from rest" (item 2); "$`v_1=v_2`$"; "the clocks respond alike per label"; "the clocks respond alike per distance"; the relation (4.24) for each type separately.
   - (d) With the medium not read: for a pair with $`v_1\neq v_2`$, determine whether an equivalent description exists in which $`v'_1=v'_2`$, and what the accelerations $`A'^{(i)}_{k,+}`$ and the responses of the clocks are in it. Determine which condition on the original data is necessary and sufficient for the existence of an equivalent description in which the two types fall alike from rest.
   - (e) State what "two types fall alike" and "their clocks respond alike" can mean in a way that does not depend on the choice among equivalent descriptions: when the relative factor of the two bodies is detectable, and when it is not.

## Inputs

From 03-ilang-space/17-motion@v2. Setting there: $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$; the start is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, $`\lvert u_h\rangle:=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$, $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$; with $`p_h(\lambda)`$ the place weights of the view of $`b`$, $`\bar x(\lambda):=\sum_hp_h(\lambda)\,u_h`$.

Eq. (17.15) of 03-ilang-space/17-motion, for the chain $`h_m`$, $`m\in\mathbb Z`$, with $`K_{h_m}=m\,X`$, $`X`$ self-adjoint on $`\mathcal H_c`$, $`\sigma_X:=(\langle X^2\rangle-\langle X\rangle^2)^{1/2}>0`$ and $`e:=(X-\langle X\rangle)\chi`$, so that $`\lVert e\rVert=\sigma_X`$ and $`u_{h_m}=m\,e`$:

```math
d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X,\qquad \bar x=\bar m\,e,\quad \bar m:=\sum_mm\,p_{h_m},\qquad s^2=\sigma_X^2\sum_m(m-\bar m)^2p_{h_m} .
```

From 05-moving-clock@v3 of 04-ilang-time. Setting there: one Model D body with the contract $`C_b=C_{\rm D}`$ of the base problem, the records $`K_x=\kappa xX`$ and the start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$.

Eq. (5.11) of 04-ilang-time/05-moving-clock, the bound (17.7) of 03-ilang-space/17-motion for this $`C_b`$ (the maximal speed), with $`t_{hh'}`$ the entries of $`C_b`$ and $`d_0(h,h')`$ the distances of (17.15):

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

Eq. (3.36) of 03-clock-and-fall, for the start $`S_{\rm clock}(x_0)`$ at zeroth order in the gradients and to first order in the level spacing, with the local parameters $`\tau^0:=\tau(1+g_\zeta x_0)`$, $`m^0:=m_{x_0}`$, $`\eta^0:=\eta_{x_0}`$, $`\bar\mu:=m^0+\eta^0\frac{\pi(N-1)}{N\lambda_0}`$ and $`\Gamma(p):=\bar\mu/\sqrt{\bar\mu^2+\tau^{0\,2}\sin^2p}`$. The clock statistics is, to this order, a mixture of the distributions of a ring clock with the advances $`\pm\Gamma(p)\eta^0\lambda/\lambda_0`$ and the weights $`\tfrac12(1\pm\Gamma(p))\lvert\tilde\phi_X(p)\rvert^2\frac{\mathrm dp}{2\pi}`$; $`\vartheta_W`$ is defined as the mean advance of this mixture, and $`r_W`$ is the rate at finite $`W`$:

```math
\vartheta_W(\lambda):=\Bigl\langle\tfrac{1+\Gamma}2\Gamma-\tfrac{1-\Gamma}2\Gamma\Bigr\rangle_W\frac{\eta^0\lambda}{\lambda_0}=(1-\varsigma_W)\frac{\eta^0\lambda}{\lambda_0},\qquad r_W(x_0):=\frac{\mathrm d\vartheta_W}{\mathrm d\lambda}=\frac{\eta^0}{\lambda_0}\,(1-\varsigma_W),\qquad\varsigma_W(x_0):=\Bigl\langle\frac{\tau^{0\,2}\sin^2p}{\bar\mu^2+\tau^{0\,2}\sin^2p}\Bigr\rangle_W,
```

Eq. (3.23) of 03-clock-and-fall, the rate at $`x_0`$ (its wide-start form and its form at finite $`W`$), with $`E^{\pm}_{x,k}:=V_x\pm M_{x,k}`$:

```math
\text{rate at }x_0:=\lim_{W\to\infty}r_W(x_0)=\frac{\eta_{x_0}}{\lambda_0}=\frac{N}{2\pi}\bigl(E^+_{x_0,k+1}-E^+_{x_0,k}\bigr),\ \ \text{tick }\frac{\lambda_0}{\eta_{x_0}};\qquad\text{at finite }W:\ \ r_W=\frac{\eta_{x_0}}{\lambda_0}(1-\varsigma_W),\ \ \text{tick }\frac{\lambda_0}{\eta_{x_0}(1-\varsigma_W)},\ \ \Bigl\lvert r_W-\frac{\eta_{x_0}}{\lambda_0}\Bigr\rvert\le\frac{\eta_{x_0}}{\lambda_0}\,\delta_W^2\frac{\tau^{0\,2}}{m_{x_0}^2}.
```

From 04-branch-fall@v3 (this subproject). Setting there: one body with a conserved clock level whose level blocks have the Model D form with position-dependent parameters (the class $`\mathcal C`$ is a subclass), and a medium with the records $`K_x=\kappa\,x\,X`$. On the level $`k`$ the zeroth-order block has the eigenvalues $`\pm\omega_k(p)`$, $`\omega_k(p)=\sqrt{M_k^2+\tau_k^2\sin^2p}`$, and two branches $`\sigma=\pm`$. A **branch start** lies in one branch of one level; it is at rest if its plane-wave label is concentrated at $`p_0=0`$. The **drift acceleration** $`a_{k,\sigma}(p_0)`$ is the acceleration of the mean position label $`\bar x_{\rm lab}`$ at first order in the gradients of the level, averaged over a long window, followed by the limit of a sharp label; records at leading order in $`\kappa`$. For the class $`\mathcal C`$: $`\tau_k=\tau`$, $`M_k=m+d_k`$, $`G_k=m\,g_m+d_k\,g_\eta`$, $`\mathcal F_k=\mathcal F`$.

Eq. (4.16) of 04-branch-fall, the drift acceleration at rest:

```math
\boxed{\;a_{k,\sigma}(0)=\frac{\tau_k^2}{M_k}\,\bigl(\sigma\,\mathcal F_k-G_k\bigr)\;}
```

Eq. (4.22) of 04-branch-fall, for the class $`\mathcal C`$ and every $`N\ge2`$:

```math
a_{k,+}(0)\ \text{level-independent}\iff\mathcal F=m(g_m-g_\eta);\qquad a_{k,-}(0)\ \text{level-independent}\iff\mathcal F=-m(g_m-g_\eta);\qquad\text{value }-\tau^2g_\eta\text{ in each case};
```

Eq. (4.24) of 04-branch-fall, for the class $`\mathcal C`$ under the hypothesis $`a_{k,+}(0)=a\neq0`$ for all $`k`$, at first order in the gradients and at leading order in $`\kappa`$. Here $`r(x)=\eta_x/\lambda_0`$ is the rate (3.23) in its wide-start form, $`d_0:=\kappa\sigma_X`$ is the distance of neighbouring positions in the background of (17.15), $`\bar x=d_0\,\bar x_{\rm lab}\,\hat e`$ with $`\hat e:=e/\sigma_X`$, and $`v_{\max}=\tau d_0`$ is the bound (5.11) of 04-ilang-time/05-moving-clock:

```math
\boxed{\;\frac{\mathrm d^2\bar x}{\mathrm d\lambda^2}\Big\vert_{\rm drift}=d_0\,a_{k,+}(0)\,\hat e=-\,\frac{v_{\max}^2}{d_0}\;\frac{r(x+1)-r(x)}{r(x)}\;\hat e\;}
```

From 05-rate-comparison@v3 (this subproject). Setting there: the definitions of readings, schedules, re-timings, equivalences and detectable relative factors as under "Goal"; two bodies $`b_1`$, $`b_2`$ of different types with arbitrary self-adjoint body contracts $`C_1`$, $`C_2`$, position labels with $`\hat x_i=\sum_xx\,P^{(i)}_x`$, no contract between the bodies, and one medium $`c`$: $`C=C_1+C_2+\kappa_1\,\hat x_1\otimes X+\kappa_2\,\hat x_2\otimes X`$; each object is one class, with the factors $`a_1`$, $`a_2`$, $`a_c`$. Notation: $`F_i:=C_i+\kappa_i\hat x_i\otimes X`$; $`J_i:=[C_i,\hat x_i]`$ ($`J_i\neq0`$ iff $`C_i`$ has an entry between places with different position labels); "$`X`$ diagonal" means diagonal in the places of the medium; $`\Delta`$ is a real operator, diagonal in the joint places, a sum of pair terms, with $`[C,\Delta]=0`$.

Eq. (5.19) of 05-rate-comparison, all equivalences when all three objects are read:

```math
\begin{array}{l|l|l}
\text{case} & \text{factors} & C'\\\hline
X\text{ diagonal} & a_1,a_2,a_c\ \text{free} & F_1/a_1+F_2/a_2+\Delta\\
X\text{ not diagonal},\ J_1\neq0,\ J_2\neq0 & a_1=a_2=a_c=\alpha & C/\alpha+\Delta\\
X\text{ not diagonal},\ J_1=0,\ J_2\neq0 & a_2=a_c,\ a_1\ \text{free} & C_1/a_1+(C-C_1)/a_c+\Delta\\
X\text{ not diagonal},\ J_1\neq0,\ J_2=0 & a_1=a_c,\ a_2\ \text{free} & C_2/a_2+(C-C_2)/a_c+\Delta\\
X\text{ not diagonal},\ J_1=J_2=0 & a_1,a_2,a_c\ \text{free} & C_1/a_1+C_2/a_2+(\kappa_1\hat x_1+\kappa_2\hat x_2)\otimes X/a_c+\Delta
\end{array}
```

Eq. (5.20) of 05-rate-comparison, when the medium is not read:

```math
\Bigl(a_1,\ a_2;\ \ C'=\frac{C_1}{a_1}+\frac{C_2}{a_2}+\frac{\kappa_1}{a_1}\hat x_1\otimes X+\frac{\kappa_2}{a_2}\hat x_2\otimes X\Bigr)\ \text{is an equivalence for all }a_1,a_2>0,\ \text{for every }C_1,C_2,\ \kappa_1,\kappa_2>0\ \text{and }X .
```

Eq. (5.21) of 05-rate-comparison, for the schedule that reads the clock label of $`b_1`$ at $`\lambda_1`$ and that of $`b_2`$ at $`\lambda_2`$ (outcomes $`j_1`$, $`j_2`$), every start and the equivalence (5.20); exact, for arbitrary $`C_1`$, $`C_2`$. Every parameter that enters $`C_i`$ linearly and $`\kappa_i`$ are divided by $`a_i`$; the tick parameter $`\lambda_0/\eta_x`$ of $`b_i`$ and every value of $`\lambda`$ at which $`b_i`$ is read are multiplied by $`a_i`$:

```math
P_C(j_1,j_2;\lambda_1,\lambda_2)=P_{C'}(j_1,j_2;a_1\lambda_1,a_2\lambda_2):\qquad(\lambda_1,\lambda_2)\mapsto(a_1\lambda_1,a_2\lambda_2),\qquad C_i\mapsto\frac{C_i}{a_i},\quad\kappa_i\mapsto\frac{\kappa_i}{a_i} .
```

Eq. (5.22) of 05-rate-comparison, definitions: $`\Pi_j`$ is the projector onto the places of a body with the clock label $`j`$, and $`D`$ the clock operator of Model D; $`p_\lambda`$ is the **clock statistics**, $`\pi_u`$ the **dial**. An **advance** is a function $`\vartheta(\lambda)=\Theta\bigl[(p_\mu)_{0\le\mu\le\lambda}\bigr]`$ with a rule $`\Theta`$ that has the property (R): the family $`\mu\mapsto p_{\mu/\alpha}`$ on $`[0,\alpha\lambda]`$ gets the same value as $`\mu\mapsto p_\mu`$ on $`[0,\lambda]`$, for every $`\alpha>0`$. The **rate** is $`r(\lambda;\Psi_0,C):=\mathrm d\vartheta/\mathrm d\lambda`$ where the derivative exists.

```math
p_\lambda(j):=\bigl\lVert\Pi_j\,e^{-iC\lambda}\Psi_0\bigr\rVert^2,\qquad
\pi_u(j):=\bigl\lvert\langle j\vert e^{-iDu\lambda_0}\vert0\rangle\bigr\rvert^2=\frac{\sin^2\pi(j-u)}{N^2\sin^2\bigl(\pi(j-u)/N\bigr)},\qquad
\text{uniform clock, rate }r>0\text{ on }[0,\Lambda]:\ \ p_\lambda=\pi_{r\lambda}\ \ (0\le\lambda\le\Lambda,\ r\Lambda\le1).
```

Eq. (5.25) of 05-rate-comparison, for every equivalence with the factors $`a_1`$, $`a_2`$ of the bodies (the medium read or not), every start and a rate $`r_i`$ of $`b_i`$ for a rule with (R), wherever the rates exist and the denominators do not vanish:

```math
r_i^{C'}(\lambda')=\frac1{a_i}\,r_i^{C}\Bigl(\frac{\lambda'}{a_i}\Bigr),\qquad\frac{r_1^{C'}(\lambda')}{r_2^{C'}(\lambda')}=\frac{a_2}{a_1}\cdot\frac{r_1^{C}(\lambda'/a_1)}{r_2^{C}(\lambda'/a_2)};\qquad\text{two uniform clocks, rates }r_1,r_2\text{ on }[0,\Lambda]:\ \ \frac{r'_1}{r'_2}=\frac{r_1}{r_2}\cdot\frac{a_2}{a_1}\ \text{ on }0<\lambda'\le\min(a_1,a_2)\Lambda,
```

From 02-field-object@v2 (this subproject). Setting there: a body $`b`$, a field $`f`$ and a set $`r`$ of further objects, of pairwise different types, $`\mathcal H=\mathcal H_{br}\otimes\mathcal H_f`$ with $`\mathcal H_{br}:=\mathcal H_b\otimes\mathcal H_r`$; $`C_{br}`$ is a sum of pair terms among $`b`$ and the objects of $`r`$, $`C_f`$ is self-adjoint on $`\mathcal H_f`$, and $`B_j`$ (on $`\mathcal H_b`$), $`\Phi_j`$ (on $`\mathcal H_f`$) are finite families of self-adjoint operators.

Eq. (2.1) of 02-field-object, the contract:

```math
C=C_{br}\otimes\mathbb 1_f+\sum_{j\in J}B_j\otimes\mathbb 1_r\otimes\Phi_j+\mathbb 1_{br}\otimes C_f
```

Eq. (2.3) of 02-field-object, for a field state with $`\Phi_j\varphi=n_j\varphi`$ and $`C_f\varphi=e_f\varphi`$, and every $`\Psi\in\mathcal H_{br}`$:

```math
C\,(\Psi\otimes\varphi)=\bigl((C_{\rm red}+e_f)\Psi\bigr)\otimes\varphi,\qquad C_{\rm red}:=C_{br}+\sum_{j\in J}n_j\,B_j\otimes\mathbb 1_r .
```

Eq. (2.20) of 02-field-object, the replacements of $`C_{br}`$, the $`\Phi_j`$ and $`C_f`$ at fixed $`B_j`$ that leave $`C`$ unchanged (exactly these, if $`\mathbb 1_b`$ and the $`B_j`$ are linearly independent):

```math
\Phi_j\to\Phi_j+a_j\,\mathbb 1_f,\qquad C_f\to C_f+c\,\mathbb 1_f,\qquad C_{br}\to C_{br}-\sum_{j\in J}a_j\,B_j\otimes\mathbb 1_r-c\,\mathbb 1_{br},\qquad a_j,c\in\mathbb R .
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- The four types are pairwise different and each has one instance, so no swap condition applies.
- The bodies of the class $`\mathcal C`$, the linear profiles, the common medium with one operator $`X`$, and in item 5 the form of the coupling and the sharp and stationary state of the field are assumptions of this package (M8, A11). Equal parameters of the two types are never assumed (M7); every equality between the two types is a condition that the package determines.
- The drift accelerations and the rates are those of the quoted results, with their starts and orders; a comparison at equal $`\lambda`$ uses the order of $`\lambda`$ (A8), and the package says where it relies on it.

## Scope

- **Class.** Items 1–4 and 6: all pairs of bodies of the class $`\mathcal C`$ with linear profiles, all $`\kappa_1,\kappa_2>0`$ and every $`X`$ and $`\chi`$ with $`\sigma_X>0`$; in item 6 also the cases of $`X`$ diagonal and not diagonal in the places of the medium. Item 5: all pairs of Model D bodies, all $`\theta_1`$, $`\theta_2`$ and every sharp value $`\gamma`$ in the stated range.
- **Controls.** The two controls of item 4(b); the medium read against not read, and $`X`$ diagonal against not diagonal (item 6).
- In scope:
  - the conditions for two types to fall alike and for their clocks to respond alike, at first order in the gradients and from rest;
  - the relation of these conditions to the maximal speeds and to the couplings to one field;
  - the behaviour of all these statements under the equivalences of 05-rate-comparison.
- Out of scope:
  - the fall in motion (the order $`v^2`$), the lattice terms and the records beyond leading order in $`\kappa`$ (04-branch-fall, 07-limits);
  - a field that is not sharp, a field that responds to the bodies, and any term between the two bodies;
  - instances of one type (Law 5);
  - any physical meaning beyond the definitions (M1–M4); no theory of gravity and no theory that contains time may be used as an input.

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: short argument.
- Item 4: derive.
- Item 5: (a) short argument; (b), (c) derive; (d) short argument.
- Item 6: derive.

## Expected result

- Item 1: a condition with a value; a table of yes/no answers.
- Item 2: an equivalence, expressed in two ways; an equivalence; a condition with a yes/no answer.
- Item 3: two conditions and a statement.
- Item 4: two yes/no answers with the further conditions; two controls; a statement.
- Item 5: a generator with the gradients and a range; conditions on six numbers with a list of yes/no answers; four yes/no answers; a statement.
- Item 6: conditions; a list of transformation rules; a table of yes/no answers for the two cases; a yes/no answer with values and an equivalence; a statement.

Give every main result a tag $`(8.k)`$.

Consistency checks, at most three: for example two types with identical data, one of the two gradients set to zero, and the equivalence (5.20) with $`a_1=a_2`$.

## Code

None.
