# Question: 06-two-clocks

- **Subproject:** 05-ilang-free-fall
- **Package:** 06-two-clocks
- **Equation tags:** (6.k)
- **Created:** 2026-10-11

## Goal

For a body whose level blocks have the Model D form with position-dependent parameters, determine how the frequency of every periodic process of the body depends on the place, under which conditions all of them respond alike, and how such a common response is related to a fall that is the same for all clock levels and to the relation (4.24) between the fall and the rates of the carried clock. This is the part of criterion 2 that concerns the contracts, the second half of criterion 4, and the part of criterion 5 that asks what the relation rests on.

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
- **Local member.** For a position $`x_0`$ the **local member** $`C_{\rm loc}(x_0)`$ is the member of $`\mathcal C_{\rm lev}`$ on the infinite chain with uniform level profiles: $`M_{x_0,k}`$ and $`V_{x_0,k}`$ at every position, and the hopping factor $`\zeta^0_k(x_0):=1+g_{\zeta,k}x_0`$ on every bond (the mean of $`\zeta_{x_0,k}`$ and $`\zeta_{x_0-1,k}`$). By (5.5), (5.6) of 04-ilang-time/05-moving-clock with $`\tau\to\tau_k\zeta^0_k(x_0)`$ and $`\mu_k\to M_{x_0,k}`$, its eigenvalues are
  ```math
  \varepsilon_{k,\sigma}(p;x_0):=V_{x_0,k}+\sigma\,\omega_k(p;x_0),\qquad\omega_k(p;x_0):=\sqrt{M_{x_0,k}^2+\tau_k^2\,\zeta^0_k(x_0)^2\sin^2p},
  ```
  for the level $`k`$, the branch $`\sigma=\pm`$ and the label $`p\in(-\pi,\pi]`$.
- **Gaps.** A **gap at $`x_0`$** is a difference $`\Omega_\gamma(x_0):=\varepsilon_{k,\sigma}(p;x_0)-\varepsilon_{k',\sigma'}(p';x_0)`$ of two eigenvalues of the local member; its **label** $`\gamma=(k,\sigma,p;k',\sigma',p')`$ does not depend on $`x_0`$. By (2.5) of 04-ilang-time/02-clock the statistics of every reading of a part that evolves by its own contract is a sum of terms $`e^{-i\Omega\lambda}`$ over the gaps $`\Omega`$ of that contract. A **process of the body at $`x_0`$** with the frequency $`\Omega_\gamma(x_0)`$ is meant in this sense: at zeroth order in the gradients, as for the rate (3.23). This reading of "at a place" is an assumption of the package (M8).
- **Response.** For a label $`\gamma`$ whose gap is not zero at zero gradients, the **response** $`\rho_\gamma`$ is the first order in the gradients of $`\bigl[\Omega_\gamma(1)-\Omega_\gamma(0)\bigr]/\Omega_\gamma(0)`$. A set of labels has the **common response** $`g_*`$ if $`\rho_\gamma=g_*`$ for every label of the set.
- **Named gaps.** For a level $`k`$:
  - the **level gap** $`\gamma_{\rm lev}(k)=(k+1,+,0;\,k,+,0)`$, for $`k\le N-2`$;
  - the **branch gap** $`\gamma_{\rm br}(k)=(k,+,0;\,k,-,0)`$;
  - the **band gap** $`\gamma_{\rm band}(k)=(k,+,\tfrac\pi2;\,k,+,0)`$.

1. **Responses.**
   - (a) Determine $`\rho_\gamma`$ for a general label $`\gamma`$ as a linear form in the gradients of the levels involved, with coefficients that are functions of the level data and of $`p`$, $`p'`$. State which gradients enter the gaps inside one level, and which enter only the gaps between two levels.
   - (b) Evaluate it for the three named gaps. For the class $`\mathcal C`$, state the relation between the level gap and the rate (3.23).
   - (c) For each named gap give a start and a reading of a body that evolves by the local member whose statistics contains this gap (a term $`e^{-i\Omega\lambda}`$ of (2.5) of 04-ilang-time/02-clock with a nonzero coefficient), and state whether that statistics is periodic in $`\lambda`$.
   - (d) State whether the gaps and the responses are well defined (M6): under the replacements (8.1) of 04-ilang-time/08-maximal-speed, and under a change of the unit of $`\lambda`$.

2. **Common response.**
   - (a) One level. Determine the necessary and sufficient condition on $`(M_k,\tau_k,G_k,g_{\zeta,k})`$ under which all gaps inside the level $`k`$ (both branches, all $`p`$, $`p'`$) have a common response, and its value.
   - (b) All levels. Determine the necessary and sufficient condition on the level data, the level offsets and the gradients under which all gaps of the body that are not zero at zero gradients have a common response $`g_*`$. Give the general form of the level profiles that satisfy it, to first order in the gradients.
   - (c) The class $`\mathcal C`$. Translate (a) and (b) into conditions on $`(g_m,g_\eta,g_\zeta,\mathcal F)`$, for every $`N\ge2`$. For the variants (a), (b1), (b2), (c), (d), (f) state which of the three named gaps have equal responses.
   - (d) State the form of (b) without the first-order approximation: the condition on the on-site blocks and the hopping factors of the local members at two positions $`x_0`$, $`x_1`$ under which every gap at $`x_1`$ is one common multiple of the gap with the same label at $`x_0`$. Both directions are asked.

3. **Common response and fall.** With (4.16), (4.17) and (4.19):
   - (a) Assume that all gaps have a common response $`g_*\neq0`$ (item 2(b)). Determine $`a_{k,\sigma}(0)`$ for all levels and both branches. Determine the necessary and sufficient further conditions under which $`a_{k,+}(0)`$ is the same for all levels; the same for $`a_{k,-}(0)`$; and the same for both with one value. State which of the further conditions concern the plain parts and which the numbers $`\tau_k`$.
   - (b) Conversely, assume that $`a_{k,+}(0)`$ and $`a_{k,-}(0)`$ are the same for all levels, with one value $`a\neq0`$. Determine which gaps then have a common response, and which need not. Give a control: a member of $`\mathcal C_{\rm lev}`$ with this property whose gaps have no common response.
   - (c) Under the assumption of (a) together with its further conditions, determine the coefficient $`c_{2,k,\sigma}`$ of (4.17), and whether $`a_{k,\sigma}`$ is the same for all levels through the order $`v^2`$: exactly, and to leading order in $`M_k/\tau_k`$.
   - (d) State the answer to the question of criterion 4: whether a common response of the periodic processes of a body implies a fall that is the same for all levels, and conversely, with the exact further conditions in each direction.

4. **What the relation between response and fall rests on.**
   - (a) For every member of $`\mathcal C_{\rm lev}`$ with linear level profiles, determine the relation between $`a_{k,\sigma}(0)`$, the response of the branch gap of the level $`k`$ and the remaining well-defined differences of (4.18). State which part of it holds for every member, and which term vanishes under which condition.
   - (b) The relation (4.24) contains the response of the level gap. For each of the three named gaps, determine the necessary and sufficient conditions under which the relation holds for all levels with the response of that gap in the place of $`\bigl(r(x+1)-r(x)\bigr)/r(x)`$. Determine the condition under which it holds with the response of every gap.
   - (c) For a member of $`\mathcal C_{\rm lev}`$ whose numbers $`\tau_k`$ depend on the level, determine the bound (5.11) of 04-ilang-time/05-moving-clock (one number for the body), and state which speed enters the relation of each level.
   - (d) State the order to which each relation of (b) holds: in the gradients, in the drift velocity (with (4.17)), in $`M_k/\tau_k`$ and in $`\kappa`$.

5. **Control: where the factor sits.** For the variants (a) (a factor on the rest and clock term), (c) (a factor on the whole body contract) and (f) (a constant under the factor), give a table: the responses of the three named gaps; $`a_{k,+}(0)`$ and $`a_{k,-}(0)`$; whether the relation of item 4(b) holds with each named gap. State what distinguishes (a) from (c) in the readings of one body.

## Inputs

From 02-clock@v2 of 04-ilang-time. Setting there: a part $`K`$ with a companion, whose view $`V_K(\lambda)`$ evolves by its own contract $`C_K`$ alone (a self-driven part); $`V_0:=V_K(0)`$; $`C_K=\sum_jE_jP_j`$ is the spectral decomposition; $`p(r;\lambda)=\mathrm{Tr}(\Pi_rV_K(\lambda))`$ is the probability of the outcome $`r`$ of a reading on $`K`$ with the class projectors $`\Pi_r`$.

Eq. (2.5) of 04-ilang-time/02-clock:

```math
V_K(\lambda)=\sum_{j,l}e^{-i(E_j-E_l)\lambda}P_jV_0P_l,\qquad
p(r;\lambda)=\sum_{j,l}e^{-i(E_j-E_l)\lambda}\mathrm{Tr}\bigl(\Pi_rP_jV_0P_l\bigr).
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

Eq. (4.18) of 04-branch-fall. For the level $`k`$ of $`C_{\rm eff}`$: $`E^\pm_{x,k}=V_{x,k}\pm M_{x,k}`$ (modulo a common constant), the gap $`\Delta_{x,k}=2M_{x,k}`$, the norm of the hopping block $`t_{x,k}=\tfrac12\tau_k\zeta_{x,k}`$; for the linear profiles the differences between neighbouring positions are $`\delta E^\pm_k=\pm G_k-\mathcal F_k`$, $`\delta\Delta_k=2G_k`$, $`\delta t_k=\tfrac12\tau_kg_{\zeta,k}`$, and the reference values are $`\Delta_k:=\Delta_{0,k}=2M_k`$ and $`\bar t_k:=\tfrac12(t_{0,k}+t_{-1,k})=\tfrac12\tau_k`$. These are functions of $`C_{\rm eff}`$ modulo $`\mathbb 1`$, invariant under (8.1) of 04-ilang-time/08-maximal-speed:

```math
a_{k,\sigma}(0)=-\sigma\,\frac{8\,\bar t_k^{\,2}}{\Delta_k}\,\delta E^{\sigma}_k,\qquad
c_{2,k,\sigma}=\frac{\delta t_k}{\bar t_k}+\frac{\delta\Delta_k}{\Delta_k}\Bigl(1+\frac{\Delta_k^2}{8\bar t_k^{\,2}}\Bigr)+\sigma\,\frac{\delta E^+_k+\delta E^-_k}{\Delta_k}\Bigl(\frac32+\frac{\Delta_k^2}{8\bar t_k^{\,2}}\Bigr).
```

Eq. (4.19) of 04-branch-fall, for every member of $`\mathcal C_{\rm lev}`$ with linear level profiles and $`N\ge2`$ levels:

```math
\begin{aligned}
a_{k,+}(0)=a_+\ \forall k&\iff\frac{\tau_k^2}{M_k}(\mathcal F_k-G_k)=a_+\ \forall k,\qquad
a_{k,-}(0)=a_-\ \forall k\iff\frac{\tau_k^2}{M_k}(\mathcal F_k+G_k)=-a_-\ \forall k,\\
\text{both, with }a_+=a_-=a&\iff\mathcal F_k=0\ \text{ and }\ \frac{\tau_k^2G_k}{M_k}=-a\quad\forall k .
\end{aligned}
```

Eq. (4.22) of 04-branch-fall, for the class $`\mathcal C`$ and every $`N\ge2`$:

```math
a_{k,+}(0)\ \text{level-independent}\iff\mathcal F=m(g_m-g_\eta);\qquad a_{k,-}(0)\ \text{level-independent}\iff\mathcal F=-m(g_m-g_\eta);\qquad\text{value }-\tau^2g_\eta\text{ in each case};
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
- The members of $`\mathcal C_{\rm lev}`$, the linear level profiles, the local member as the meaning of "at a place", and the branch starts are assumptions of this package (M8, M9).
- A result for this class shows what such descriptions give; it does not show that the language selects them (M10).

## Scope

- **Class.** Items 1–4: every member of $`\mathcal C_{\rm lev}`$ with linear level profiles and $`N\ge2`$ levels, all level offsets, both branches, all labels. Items 2(c) and 5: the class $`\mathcal C`$ and the six named variants.
- **Controls.** The variant (a) against the variant (c); the variants (b1), (b2), (d), (f); the control asked in item 3(b); members with level-dependent $`\tau_k`$.
- In scope:
  - the gaps of the local member, their responses to the place and the conditions for a common response;
  - the relation between a common response and a fall that is the same for all levels, in both directions;
  - the conditions under which the relation (4.24) holds with the frequency of a given process.
- Out of scope:
  - processes that are not processes of the local member (for example an oscillation of the body in a well of the profile), and the second order in the gradients;
  - the comparison of two clocks inside one description by a protocol (05-rate-comparison), bodies of two types, a field object and fields that are not sharp;
  - a start in a superposition of levels and the records beyond leading order in $`\kappa`$ (07-limits);
  - any physical meaning beyond the definitions (M1–M4); no theory of gravity and no theory that contains time may be used as an input.

## Depth

- Item 1: (a), (b) derive; (c), (d) short argument.
- Item 2: derive.
- Item 3: derive.
- Item 4: (a), (b) derive; (c), (d) short argument.
- Item 5: short argument.

## Expected result

- Item 1: a linear form with its coefficients; three values; three examples; two yes/no answers.
- Item 2: an equivalence with a value; an equivalence with the general form of the profiles; conditions on four numbers and a table; an exact equivalence.
- Item 3: closed forms and three equivalences; a statement with a control; a coefficient and two yes/no answers; a statement in two directions.
- Item 4: a relation with a statement of what is an identity; for each named gap an equivalence; a number and a statement; a list of orders.
- Item 5: a table and a statement.

Give every main result a tag $`(6.k)`$.

Consistency checks, at most three: for example all gradients zero, the variant (c) against an exact rescaling of the whole level block, and a body with $`\tau_k\to0`$.

## Code

None.
