# Question: 09-unsharp-field

- **Subproject:** 05-ilang-free-fall
- **Package:** 09-unsharp-field
- **Equation tags:** (9.k)
- **Created:** 2026-10-11

## Goal

Determine what the results on the fall of a body, on its independence of the clock level, on the clock rate and on the relation (4.24) become when the field that acts on the body is static and is not in a sharp state. This is the first part of criterion 8.

**Setting.**
- **Objects.** A body $`b`$, a field $`f`$ and a recording medium $`c`$, of pairwise different types, one instance each.
- **Contract (the class $`\mathcal S`$ of static fields).** In the order $`b`$, $`f`$, $`c`$:
  ```math
  C=\sum_{\nu\in\mathcal N}C^{(\nu)}_b\otimes P_\nu\otimes\mathbb 1_c+\mathbb 1_b\otimes C_f\otimes\mathbb 1_c+\sum_x\lvert x\rangle\langle x\rvert\otimes\mathbb 1_f\otimes\kappa\,x\,X .
  ```
  Here $`\mathcal N`$ is a finite set of **sectors**; the $`P_\nu`$ are orthogonal projectors on $`\mathcal H_f`$ with $`P_\nu P_{\nu'}=\delta_{\nu\nu'}P_\nu`$ and $`\sum_\nu P_\nu=\mathbb 1_f`$; $`C_f`$ is self-adjoint on $`\mathcal H_f`$ with $`[C_f,P_\nu]=0`$ for all $`\nu`$; every **sector contract** $`C^{(\nu)}_b`$ is a self-adjoint operator on $`\mathcal H_b`$ of the class $`\mathcal C_{\rm lev}`$ with linear level profiles (next item); the last term is the record term of Model D, with $`\kappa>0`$ and $`X`$ self-adjoint on $`\mathcal H_c`$. Two different sectors have sector contracts that differ by more than a real multiple of $`\mathbb 1_b`$. The first sum is one pair term between $`b`$ and $`f`$ (A5). $`C`$ is the contract (2.1) with $`r=\{c\}`$, the field operators $`\Phi_\nu=P_\nu`$ and $`B_\nu=C^{(\nu)}_b`$. These field operators commute with each other and with $`C_f`$ (a **static** field, (2.15)), and the sector generator of the sector $`\nu`$ is $`C^{(\nu)}=C^{(\nu)}_b\otimes\mathbb 1_c+\sum_x\lvert x\rangle\langle x\rvert\otimes\kappa\,x\,X`$.
- **Sector contracts (the class $`\mathcal C_{\rm lev}`$).** A member of $`\mathcal C_{\rm lev}`$ has the places $`(x,s,a)`$ of Model D, with $`x`$ on a chain $`\lvert x\rvert\le L`$ and $`x\in\mathbb Z`$ as the limit of long chains (A1), and, with the vectors $`\lvert f_k\rangle`$ of Model D, the contract
  ```math
  C_b=\sum_{k=0}^{N-1}C^{(k)}\otimes\lvert f_k\rangle\langle f_k\rvert,\qquad C^{(k)}=\frac{\tau_k}2\sum_x\zeta_{x,k}\Bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\Bigr)+\sum_x\lvert x\rangle\langle x\rvert\otimes\bigl(M_{x,k}\,\sigma_3+V_{x,k}\,\mathbb 1_2\bigr),
  ```
  with real numbers $`\tau_k>0`$, $`\zeta_{x,k}>0`$, $`M_{x,k}>0`$ and $`V_{x,k}`$. $`C^{(k)}`$ is the **level block** of the clock level $`k`$; the level is conserved. **Linear level profiles:** $`M_{x,k}=M_k+G_kx`$, $`V_{x,k}=-\mathcal F_kx`$, $`\zeta_{x,k}=1+g_{\zeta,k}(x+\tfrac12)`$, with $`M_k>0`$, $`\lvert G_k\rvert(L+1)<M_k`$ and $`\lvert g_{\zeta,k}\rvert(L+1)<1`$. The **level data** are $`\tau_k`$ and $`M_k`$; the **gradients** are $`G_k`$, $`\mathcal F_k`$ and $`g_{\zeta,k}`$. The class $`\mathcal C`$ of 03-clock-and-fall with its linear profiles is the subclass $`\tau_k=\tau`$, $`M_k=m+d_k`$, $`G_k=m\,g_m+d_k\,g_\eta`$, $`\mathcal F_k=\mathcal F`$, $`g_{\zeta,k}=g_\zeta`$, with $`d_k:=\frac{2\pi k}{N\lambda_0}`$; Model D is its member with all gradients zero. All sector contracts have the same places (one $`N`$). The level data and the gradients of the sector $`\nu`$ are written $`\tau^\nu_k`$, $`M^\nu_k`$, $`G^\nu_k`$, $`\mathcal F^\nu_k`$, $`g^\nu_{\zeta,k}`$.
- **Records and regime.** As in 04-branch-fall, applied in every sector: the level profiles of the sector $`\nu`$ are those of its effective body contract, (8.19) of 04-ilang-time/08-maximal-speed for the sector generator $`C^{(\nu)}`$, so the term $`\kappa\,x\,\langle X\rangle`$ of the records is counted in every $`V^\nu_{x,k}`$. The mean position label is $`\bar x_{\rm lab}(\lambda):=\sum_xx\,p_x(\lambda)`$, with $`p_x`$ the place weights of the view of the body. Unless an item says otherwise, results are asked in the weak-record regime, $`\kappa\to0`$ at fixed $`\lambda`$, chain and start.
- **Start, weights and sector means.** The start is $`\Psi_0=\phi\otimes\varphi\otimes\chi`$, with $`\phi`$ the start of the body named in each item, $`\varphi`$ any unit vector of $`\mathcal H_f`$ and $`\chi`$ the state of the medium, $`\sigma_X>0`$. $`w_\nu:=\lVert P_\nu\varphi\rVert^2`$ and $`S:=\{\nu:w_\nu>0\}`$. The field is **sharp** if $`S`$ has one element. For numbers $`F^\nu`$, $`F'^\nu`$ attached to the sectors: $`\langle F\rangle_w:=\sum_\nu w_\nu F^\nu`$, $`{\rm Cov}_w(F,F'):=\langle FF'\rangle_w-\langle F\rangle_w\langle F'\rangle_w`$ and $`{\rm Var}_w(F):={\rm Cov}_w(F,F)`$.
- **Branches and branch starts of a sector.** With all gradients of the sector $`\nu`$ set to zero, the level block of the level $`k`$ is $`-\tau^\nu_k\sin\hat p\,\sigma_1+M^\nu_k\sigma_3`$, the block (5.5) of 04-ilang-time/05-moving-clock with $`\tau\to\tau^\nu_k`$ and $`\mu_k\to M^\nu_k`$. Its eigenvalues are $`\pm\omega^\nu_k(p)`$, $`\omega^\nu_k(p):=\sqrt{(M^\nu_k)^2+(\tau^\nu_k)^2\sin^2p}`$, with the eigenvectors $`\beta^\nu_{k,\pm}(p)`$ of (5.6) of 04-ilang-time/05-moving-clock (same substitution). For a level $`k`$, a branch $`\sigma\in\{+,-\}`$ and a smooth $`2\pi`$-periodic function $`g`$ with $`\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g\rvert^2=1`$, the **branch start** $`B^\nu_{k,\sigma}[g]`$ of the sector $`\nu`$ is
  ```math
  \lvert\phi\rangle=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\,g(p)\,\lvert p\rangle\otimes\beta^\nu_{k,\sigma}(p)\otimes\lvert f_k\rangle
  ```
  on the infinite chain. $`\langle F\rangle_g:=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g(p)\rvert^2F(p)`$. The start is **concentrated at $`p_0`$** with the spread $`\delta p`$ if, on the arc $`(p_0-\pi,p_0+\pi]`$, the weight $`\lvert g\rvert^2\frac{\mathrm dp}{2\pi}`$ has the mean $`p_0`$ and the variance $`\delta p^2`$; it is **at rest** if $`p_0=0`$. A branch start is not adapted to the gradients (M9).
- **Orders and sector quantities.** "First order in the gradients" means: first order jointly in the gradients of all sectors of $`S`$ and of all levels involved, at fixed $`\lambda`$, fixed start and fixed chain, followed by the limit of a long chain. For a member of $`\mathcal C_{\rm lev}`$, the **drift acceleration** $`a_{k,\sigma}(p_0)`$ of 04-branch-fall is the first-order acceleration of $`\bar x_{\rm lab}`$ for a branch start, averaged over a long window, followed by the limit of a sharp label, (4.10), (4.11). The **sector drift acceleration** $`a^\nu_{k,\sigma}(p_0)`$ is this quantity for the sector contract $`C^{(\nu)}_b`$. The **sector displacement** $`\Delta x^\nu_{k,\sigma}(\lambda)`$ is the first-order term of $`\bar x_{\rm lab}(\lambda)-\bar x_{\rm lab}(0)`$ for the evolution with the sector generator $`C^{(\nu)}`$ from the start $`B^\nu_{k,\sigma}[g]\otimes\chi`$.
- **Subclasses.**
  - $`\mathcal S_{\rm grad}`$ (only the gradients depend on the sector): $`\tau^\nu_k=\tau_k`$ and $`M^\nu_k=M_k`$ for all $`\nu`$. The branches and the branch starts are then the same in all sectors and are written $`B_{k,\sigma}[g]`$.
  - $`\mathcal S^{\mathcal C}_{\rm grad}`$: the members of $`\mathcal S_{\rm grad}`$ whose sector contracts are of the class $`\mathcal C`$ with one set $`\tau`$, $`m`$, $`N`$, $`\lambda_0`$ and with the linear profiles of 03-clock-and-fall, with the gradients $`g^\nu_m`$, $`g^\nu_\eta`$, $`g^\nu_\zeta`$, $`\mathcal F^\nu`$.
  - $`\mathcal S_{\rm a}`$ (a factor on the rest and clock term): $`C^{(\nu)}_b=A+\sum_x(n^\nu+\gamma^\nu x)\,\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m\mathbb 1_N+D)`$, with $`A`$ the motion term of Model D and real numbers $`n^\nu>0`$, $`\gamma^\nu`$ with $`\lvert\gamma^\nu\rvert(L+1)<n^\nu`$. This is the lapse-type pair term of the base problem with $`G=\sigma_3\otimes(m\mathbb 1_N+D)`$ and $`\Phi_x=\sum_\nu(n^\nu+\gamma^\nu x)P_\nu`$.
  - $`\mathcal S_{\rm c}`$ (a factor on the whole body contract): $`C^{(\nu)}_b=\tfrac12\bigl\{n^\nu\mathbb 1+\gamma^\nu\hat x,\ C_{\rm D}\bigr\}`$ (anticommutator), with $`C_{\rm D}`$ the contract of Model D and the same conditions on $`n^\nu`$, $`\gamma^\nu`$.

  In $`\mathcal S_{\rm a}`$ and $`\mathcal S_{\rm c}`$ the value $`n^\nu`$ of the factor at $`x=0`$ depends on the sector, and with it the level data. For these two subclasses $`\bar n:=\langle n\rangle_w`$ and $`\bar\gamma:=\langle\gamma\rangle_w`$.

1. **The mixture.** For every member of $`\mathcal S`$ and every start $`\phi\otimes\varphi\otimes\chi`$:
   - (a) Express the place weights $`p_x(\lambda)`$ of the view of the body, the mean position label, and the joint statistics of the position label and the clock label at one $`\lambda`$ through the quantities of the sectors. State what is exact and what it rests on.
   - (b) For a reading on the body at $`\lambda_1`$ with the outcome $`r`$, determine the weights with which the sectors enter the statistics of all later readings on the body and the medium. State the condition under which a given reading leaves the weights unchanged.
   - (c) Determine which of the following are well defined (M6) under the replacements (2.20) and under $`C^{(\nu)}_b\to C^{(\nu)}_b+c_\nu\mathbb 1_b`$, $`C_f\to C_f-\sum_\nu c_\nu P_\nu`$ with real $`c_\nu`$: the weights $`w_\nu`$; a sector contract; the differences $`C^{(\nu)}_b-C^{(\nu')}_b`$; the level data and the gradients of a sector.

2. **Fall when only the gradients depend on the sector.** Members of $`\mathcal S_{\rm grad}`$, starts $`B_{k,\sigma}[g]\otimes\varphi\otimes\chi`$.
   - (a) Determine, to first order in the gradients, through which functions of the weights and of the sector gradients the place weights $`p_x(\lambda)`$ depend on the state of the field. Determine the drift acceleration of the mean position label, and state in which form (4.16), (4.19), (4.22) and (4.24) hold for it.
   - (b) For a start at rest: determine the variance over the sectors of the sector displacements, $`{\rm Var}_w\bigl(\Delta x_{k,\sigma}(\lambda)\bigr)`$, in its part that grows fastest with $`\lambda`$, with its coefficient, and state the order of the limits in which it is obtained. Determine the necessary and sufficient condition on the sectors of $`S`$ under which this part vanishes for the level $`k`$ and the branch $`\sigma`$, and the condition under which it vanishes for all levels.
   - (c) Determine the necessary and sufficient condition under which the sector drift accelerations from rest are the same for all levels in every sector of $`S`$: in the upper branch, and in both branches. Determine whether a drift acceleration of the mean position label that is the same for all levels implies this condition, and give a control. State what distinguishes the two cases in readings of the position.

3. **Clock when only the gradients depend on the sector.** Members of $`\mathcal S^{\mathcal C}_{\rm grad}`$, starts $`S_{\rm clock}(x_0)\otimes\varphi\otimes\chi`$, and the rate (3.23) in its wide-start form for every sector.
   - (a) Determine the clock statistics at $`x_0`$ in terms of the sectors, the mean over the sectors of the advance and its rate, and the variance over the sectors of the advance, as functions of $`\lambda`$ and $`x_0`$. Determine the range of $`\lambda`$ in which the standard deviation of the advance over the sectors stays below a given fraction $`\epsilon`$ of one tick.
   - (b) Determine the ratio of the rates at two places $`x_1`$, $`x_2`$, with the rates defined from the mean advances of two runs compared at equal $`\lambda`$ (A8), and the first order in the gradients of $`\bigl(\bar r(x+1)-\bar r(x)\bigr)/\bar r(x)`$ for these rates $`\bar r`$.
   - (c) Determine the covariance over the sectors of the advance at $`x_0`$ and of the sector displacement of item 2(b) for the level $`k`$, in its part that grows fastest with $`\lambda`$. State the condition on the sectors under which the two are functions of each other.
   - (d) Determine the condition on the sectors and the weights under which the relation (4.24) holds between the drift acceleration of the mean position label and the rates $`\bar r`$ of (b). State separately what holds sector by sector.

4. **A factor whose value is not sharp.** Members of $`\mathcal S_{\rm a}`$ and of $`\mathcal S_{\rm c}`$.
   - (a) For each sector give the level data and the gradients, the rate at $`x`$ in the wide-start form (state the data of the class $`\mathcal C`$ to which (3.23) is applied), the bound (5.11), and the sector drift accelerations from rest in both branches. State whether these are the same for all levels within a sector, and whether (4.24) holds within a sector.
   - (b) Determine the components of the branch start $`B^{\nu_0}_{k,\sigma}[g]`$ of a reference sector $`\nu_0`$ in the two branches of another sector $`\nu`$, and the weight of the other branch for a start at rest in terms of $`\delta p`$. State for which starts and in which limit (4.16) gives the sector drift acceleration in every sector of $`S`$, for $`\mathcal S_{\rm a}`$ and for $`\mathcal S_{\rm c}`$.
   - (c) For the start $`S_{\rm clock}(0)`$: determine the mean over the sectors of the advance and its variance. Determine the mean $`\bar a`$ over the sectors of the sector drift accelerations from rest, and the number $`\bar\varrho`$, the first order in the gradients of $`\bigl(\bar r(x+1)-\bar r(x)\bigr)/\bar r(x)`$ at $`x=0`$ for the rates $`\bar r`$ defined from the mean advances. Express $`\bar a/\bar\varrho`$ through the moments of $`n`$ and $`\gamma`$ under $`w`$. Determine the necessary and sufficient condition on $`w`$ under which it equals the value that (4.24) gives for a sharp field with the factor $`\bar n+\bar\gamma x`$, and its leading deviation from that value for a narrow distribution of $`n`$, in terms of $`{\rm Var}_w(n)`$ and $`{\rm Cov}_w(n,\gamma)`$.

5. **Summary.** Give a table with one row for each of: the rate of the clock at a place; the ratio of the rates at two places; the drift acceleration from rest; its independence of the clock level; the relation (4.24). For each row state what holds within every sector, what holds for the means over the sectors in $`\mathcal S_{\rm grad}`$, in $`\mathcal S_{\rm a}`$ and in $`\mathcal S_{\rm c}`$, and to which order, with the tags of the results used.

## Inputs

From 02-field-object@v2 (this subproject). Setting there: a body $`b`$, a field $`f`$ and a set $`r`$ of further objects (possibly empty), of pairwise different types, $`\mathcal H=\mathcal H_{br}\otimes\mathcal H_f`$ with $`\mathcal H_{br}:=\mathcal H_b\otimes\mathcal H_r`$; $`C_{br}`$ is a sum of pair terms among $`b`$ and the objects of $`r`$, $`C_f`$ is self-adjoint on $`\mathcal H_f`$, and $`B_j`$ (on $`\mathcal H_b`$), $`\Phi_j`$ (on $`\mathcal H_f`$), $`j\in J`$, are finite families of self-adjoint operators; $`B_j`$ also denotes $`B_j\otimes\mathbb 1_r`$. The start is $`\Psi_0=\Psi_{br}\otimes\varphi`$ and $`\lambda\ge0`$; $`V(\lambda)`$ is the view of $`\{b\}\cup r`$. A field state $`\varphi`$ is **sharp** if $`\Phi_j\varphi=n_j\varphi`$ for all $`j`$, with real numbers $`n_j`$. A **schedule** consists of readings with projectors $`\Pi_i\otimes\mathbb 1_f`$ at $`0\le\lambda_1\le\dots\le\lambda_k`$, where $`\Pi_i`$ is diagonal in the joint places of $`b`$ and $`r`$; $`p(r_1,\dots,r_k)`$ is the joint distribution of its outcomes.

Eq. (2.1) of 02-field-object, the contract:

```math
C=C_{br}\otimes\mathbb 1_f+\sum_{j\in J}B_j\otimes\mathbb 1_r\otimes\Phi_j+\mathbb 1_{br}\otimes C_f
```

Eq. (2.15) of 02-field-object. Let the $`\Phi_j`$ commute with each other and with $`C_f`$, with the joint spectral projectors $`P_\nu`$ labelled by the joint eigenvalues $`\nu=(\nu_j)_{j\in J}\in\mathcal N`$:

```math
\Phi_j=\sum_{\nu\in\mathcal N}\nu_j\,P_\nu,\qquad C=\sum_{\nu\in\mathcal N}C^{(\nu)}\otimes P_\nu+\mathbb 1_{br}\otimes C_f,\qquad C^{(\nu)}:=C_{br}+\sum_{j\in J}\nu_j\,B_j\otimes\mathbb 1_r .
```

Eq. (2.16) of 02-field-object, with $`w_\nu:=\lVert P_\nu\varphi\rVert^2`$, $`S:=\{\nu:w_\nu>0\}`$, $`\varphi_\nu:=P_\nu\varphi/\sqrt{w_\nu}`$ and $`\Psi^{(\nu)}(\lambda):=e^{-iC^{(\nu)}\lambda}\Psi_{br}`$; exact, for every $`\Psi_{br}`$, every $`\varphi`$ and every $`\lambda`$:

```math
\Psi(\lambda)=\sum_{\nu\in S}\sqrt{w_\nu}\;\Psi^{(\nu)}(\lambda)\otimes e^{-iC_f\lambda}\varphi_\nu,\qquad V(\lambda)=\sum_{\nu\in S}w_\nu\,\lvert\Psi^{(\nu)}(\lambda)\rangle\langle\Psi^{(\nu)}(\lambda)\rvert .
```

Eq. (2.17) of 02-field-object, for every schedule, with $`p^{(\nu)}`$ the statistics of the schedule computed with $`C^{(\nu)}`$ and the start $`\Psi_{br}`$:

```math
p(r_1,\dots,r_k)=\sum_{\nu\in S}w_\nu\,p^{(\nu)}(r_1,\dots,r_k) .
```

Eq. (2.19) of 02-field-object. For such a field the view $`V(\lambda)`$ is pure for every $`\Psi_{br}`$ and every $`\lambda\ge0`$ if and only if

```math
\sum_{j\in J}(\nu_j-\nu'_j)\,B_j\in\mathbb R\,\mathbb 1_b\qquad\text{for all }\nu,\nu'\in S .
```

Eq. (2.20) of 02-field-object, the replacements of $`C_{br}`$, the $`\Phi_j`$ and $`C_f`$ at fixed $`B_j`$ that leave $`C`$ unchanged (exactly these, if $`\mathbb 1_b`$ and the $`B_j`$ are linearly independent):

```math
\Phi_j\to\Phi_j+a_j\,\mathbb 1_f,\qquad C_f\to C_f+c\,\mathbb 1_f,\qquad C_{br}\to C_{br}-\sum_{j\in J}a_j\,B_j\otimes\mathbb 1_r-c\,\mathbb 1_{br},\qquad a_j,c\in\mathbb R .
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

Eq. (3.36) of 03-clock-and-fall, for the start $`S_{\rm clock}(x_0)`$ at zeroth order in the gradients and to first order in the level spacing, with the local parameters $`\tau^0:=\tau(1+g_\zeta x_0)`$, $`m^0:=m_{x_0}`$, $`\eta^0:=\eta_{x_0}`$, $`\bar\mu:=m^0+\eta^0\frac{\pi(N-1)}{N\lambda_0}`$ and $`\Gamma(p):=\bar\mu/\sqrt{\bar\mu^2+\tau^{0\,2}\sin^2p}`$. The clock statistics is, to this order, a mixture of the distributions of a ring clock with the advances $`\pm\Gamma(p)\eta^0\lambda/\lambda_0`$ and the weights $`\tfrac12(1\pm\Gamma(p))\lvert\tilde\phi_X(p)\rvert^2\frac{\mathrm dp}{2\pi}`$; $`\vartheta_W`$ is defined as the mean advance of this mixture, and $`r_W`$ is the rate at finite $`W`$:

```math
\vartheta_W(\lambda):=\Bigl\langle\tfrac{1+\Gamma}2\Gamma-\tfrac{1-\Gamma}2\Gamma\Bigr\rangle_W\frac{\eta^0\lambda}{\lambda_0}=(1-\varsigma_W)\frac{\eta^0\lambda}{\lambda_0},\qquad r_W(x_0):=\frac{\mathrm d\vartheta_W}{\mathrm d\lambda}=\frac{\eta^0}{\lambda_0}\,(1-\varsigma_W),\qquad\varsigma_W(x_0):=\Bigl\langle\frac{\tau^{0\,2}\sin^2p}{\bar\mu^2+\tau^{0\,2}\sin^2p}\Bigr\rangle_W,
```

Eq. (3.23) of 03-clock-and-fall, the rate at $`x_0`$ (its wide-start form and its form at finite $`W`$), with $`E^{\pm}_{x,k}:=V_x\pm M_{x,k}`$:

```math
\text{rate at }x_0:=\lim_{W\to\infty}r_W(x_0)=\frac{\eta_{x_0}}{\lambda_0}=\frac{N}{2\pi}\bigl(E^+_{x_0,k+1}-E^+_{x_0,k}\bigr),\ \ \text{tick }\frac{\lambda_0}{\eta_{x_0}};\qquad\text{at finite }W:\ \ r_W=\frac{\eta_{x_0}}{\lambda_0}(1-\varsigma_W),\ \ \text{tick }\frac{\lambda_0}{\eta_{x_0}(1-\varsigma_W)},\ \ \Bigl\lvert r_W-\frac{\eta_{x_0}}{\lambda_0}\Bigr\rvert\le\frac{\eta_{x_0}}{\lambda_0}\,\delta_W^2\frac{\tau^{0\,2}}{m_{x_0}^2}.
```

From 04-branch-fall@v3 (this subproject). Setting there: a body of the class $`\mathcal C_{\rm lev}`$ with linear level profiles (as under "Goal", one contract in the place of a sector contract), a medium with the records $`K_x=\kappa\,x\,X`$, branch starts $`B_{k,\sigma}[g]`$ as under "Goal"; first order in the gradients of the level $`k`$; records at leading order in $`\kappa`$. Inside one level the index $`k`$ is dropped: $`\tau,M,G,\mathcal F,g_\zeta,\omega`$; a prime is $`\partial_p`$; $`\mathsf b:=\lvert G\rvert+M\lvert g_\zeta\rvert+\lvert\mathcal F\rvert`$; $`X_g:=\bigl(\int\frac{\mathrm dp}{2\pi}\lvert g'\rvert^2\bigr)^{1/2}`$.

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

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- The three types are pairwise different and each has one instance, so no swap condition applies.
- The class $`\mathcal S`$ and its subclasses, the linear level profiles, the product start, the branch starts and the starts $`S_{\rm clock}(x_0)`$ are assumptions of this package (M8, M9). No state of the field is preferred (A11): every result is asked for every $`\varphi`$, through the weights $`w_\nu`$.
- The quoted results of 03-clock-and-fall and 04-branch-fall are used for each sector contract, with their starts, their orders and their limits; the package says where a statement needs a limit to be uniform over the sectors of $`S`$.
- A comparison of two runs at equal $`\lambda`$ uses the order of $`\lambda`$ (A8); the package says where it relies on it.
- Every limit is stated with its order: the limit of a sharp label, an average over a window, the growth of $`\lambda`$ and the expansion parameters. Where two of them do not commute, both orders are given, each with the quantity it defines. A statement about a rate of change (a velocity, an acceleration, the rate of a clock) is derived for that rate; it is not inferred from a bound or an estimate of the quantity whose derivative it is.
- Every statement with "all", "iff" or "well defined" is stated with its exceptional members (a sector of weight zero, sectors with equal data, a gradient that vanishes); a condition that is only sufficient is called sufficient.

## Scope

- **Class.** Item 1: every member of $`\mathcal S`$, every start. Item 2: every member of $`\mathcal S_{\rm grad}`$, both branches, every level, every $`\varphi`$. Item 3: every member of $`\mathcal S^{\mathcal C}_{\rm grad}`$, every $`x_0`$ on the chain, every $`\varphi`$. Item 4: every member of $`\mathcal S_{\rm a}`$ and of $`\mathcal S_{\rm c}`$, every $`\varphi`$. Item 5: as the results state.
- **Controls.** A sharp field ($`S`$ with one element) against a field that is not sharp, in every item; in item 2(c) a member whose mean drift acceleration is the same for all levels while its sector drift accelerations are not; in item 4(c) a distribution with a sharp $`n`$ against one in which $`n`$ is not sharp.
- In scope:
  - the statistics of the body and of its clock as a mixture over the sectors;
  - the fall, its independence of the level, the clock rate and the relation (4.24): sector by sector, and for the means over the sectors, at first order in the gradients;
  - the spread over the sectors of the displacement and of the advance of the clock, and their covariance.
- Out of scope:
  - a field whose operators do not commute with each other or with its own contract (10-field-own-contract and later packages);
  - the second order in the gradients within a sector, the fall in motion (the order $`v^2`$), lattice terms, and records beyond leading order in $`\kappa`$;
  - readings on the field, two bodies in one field, and instances of one type;
  - any physical meaning beyond the definitions (M1–M4); no theory of gravity and no theory that contains time may be used as an input.

## Depth

- Item 1: short argument.
- Item 2: (a) short argument; (b), (c) derive.
- Item 3: short argument.
- Item 4: (a), (b) short argument; (c) derive.
- Item 5: standard (a table of results with their tags).

## Expected result

- Item 1: relations with a statement on exactness; a formula for the weights with a condition; four yes/no answers.
- Item 2: a statement on the dependence with a closed form; a leading term with two equivalences; an equivalence, a yes/no answer and a control.
- Item 3: a mixture with a mean, a variance and a range; a closed form and its first order; a leading term with a condition; a condition and a statement.
- Item 4: lists of data with yes/no answers; components with a weight and a statement; two means, a variance, a closed form, an equivalence and a leading term.
- Item 5: a table.

Give every main result a tag $`(9.k)`$.

Consistency checks, at most three: for example a sharp field, two sectors with equal weights, and all gradients zero.

## Code

None.
