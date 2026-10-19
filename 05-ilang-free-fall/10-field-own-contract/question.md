# Question: 10-field-own-contract

- **Subproject:** 05-ilang-free-fall
- **Package:** 10-field-own-contract
- **Equation tags:** (10.k)
- **Created:** 2026-10-11

## Goal

Determine what a body sees when the field has a contract of its own that does not commute with the operators through which it acts on the body, and the field starts in a nondegenerate eigenvector of that contract: the factor that the body sees, the first corrections to it, and their effect on the fall, on its independence of the clock level, on the clock and on the relation (4.24). This is the second part of criterion 8.

**Setting.**
- **Objects.** A body $`b`$, a field $`f`$ and a recording medium $`c`$, of pairwise different types, one instance each. In item 4 the field is replaced by one object for every position.
- **Contract (the class $`\mathcal D`$).** In the order $`b`$, $`f`$, $`c`$:
  ```math
  C=A\otimes\mathbb 1_f\otimes\mathbb 1_c+\sum_x\bigl(\lvert x\rangle\langle x\rvert\otimes G\bigr)\otimes\Phi_x\otimes\mathbb 1_c+\mathbb 1_b\otimes C_f\otimes\mathbb 1_c+\sum_x\lvert x\rangle\langle x\rvert\otimes\mathbb 1_f\otimes\kappa\,x\,X,\qquad G:=\sigma_3\otimes(m\mathbb 1_N+D).
  ```
  Here $`A`$ is the motion term of Model D on the chain $`\lvert x\rvert\le L`$ ($`x\in\mathbb Z`$ as the limit of long chains, A1), $`G`$ acts on the branch label and the clock label, the $`\Phi_x`$ and $`C_f`$ are self-adjoint operators on a finite-dimensional $`\mathcal H_f`$, and the last term is the record term of Model D. The second term is a lapse-type pair term of the base problem in which the factor multiplies the rest and clock term; the motion term carries no factor. $`C`$ is the contract (2.1) with $`r=\{c\}`$, $`B_x=\lvert x\rangle\langle x\rvert\otimes G`$ and $`C_{br}=A\otimes\mathbb 1_c+\sum_x\lvert x\rangle\langle x\rvert\otimes\kappa\,x\,X`$. The $`\Phi_x`$ need not commute with each other or with $`C_f`$. The class and the start are assumptions of this package (M8).
- **Start of the field.** $`\varphi_0`$ is an eigenvector of $`C_f`$, $`C_f\varphi_0=e_0\varphi_0`$, with a simple eigenvalue $`e_0`$, and $`\Delta_f:=\min\{\lvert e-e_0\rvert:\ e\in\mathrm{spec}C_f,\ e\neq e_0\}>0`$ is the **gap of the field**. $`e_0`$ need not be the lowest eigenvalue. The start is $`\Psi_0=\phi\otimes\varphi_0\otimes\chi`$ with $`\phi`$ a start of the body and $`\chi`$ the state of the medium, $`\sigma_X>0`$. This choice of the state of the field is an assumption (A11, M9).
- **Mean profile and fluctuation.** $`N(x):=\langle\varphi_0\vert\Phi_x\vert\varphi_0\rangle`$, assumed positive; $`\tilde\Phi_x:=\Phi_x-N(x)\mathbb 1_f`$; $`\varepsilon_x:=\lVert\tilde\Phi_x\varphi_0\rVert`$ and $`\varepsilon:=\max_x\varepsilon_x`$. The field is sharp in $`\varphi_0`$ if and only if $`\varepsilon=0`$; then (2.3) holds with $`n_x=N(x)`$.
- **Scales and regime.** $`d_k:=\frac{2\pi k}{N\lambda_0}`$, $`M_k:=m+d_k`$, $`M_{\max}:=M_{N-1}`$, $`N_{\max}:=\max_xN(x)`$. Two small numbers are used: $`\epsilon_1:=\varepsilon\,M_{\max}/\Delta_f`$ (the fluctuating part of the pair term against the gap of the field) and $`\epsilon_2:=(\tau+N_{\max}M_{\max})/\Delta_f`$ (the body against the gap of the field; a **fast field** has $`\epsilon_2\ll1`$). Results are asked as an expansion in $`\epsilon_1`$ whose coefficients are expanded in $`\epsilon_2`$; the package states the range of $`\lambda`$ on which each statement holds. Records: the weak-record regime, $`\kappa\to0`$ at fixed $`\lambda`$, chain and start, as in 04-branch-fall.
- **The classes $`\mathcal C`$ and $`\mathcal C_{\rm lev}`$.** A member of $`\mathcal C_{\rm lev}`$ has the places $`(x,s,a)`$ of Model D and, with the vectors $`\lvert f_k\rangle`$ of Model D, the contract
  ```math
  C_b=\sum_{k=0}^{N-1}C^{(k)}\otimes\lvert f_k\rangle\langle f_k\rvert,\qquad C^{(k)}=\frac{\tau_k}2\sum_x\zeta_{x,k}\Bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\Bigr)+\sum_x\lvert x\rangle\langle x\rvert\otimes\bigl(M_{x,k}\,\sigma_3+V_{x,k}\,\mathbb 1_2\bigr),
  ```
  with real numbers $`\tau_k>0`$, $`\zeta_{x,k}>0`$, $`M_{x,k}>0`$ and $`V_{x,k}`$; $`C^{(k)}`$ is the **level block** of the clock level $`k`$. **Linear level profiles:** $`M_{x,k}=M_k+G_kx`$, $`V_{x,k}=V_k-\mathcal F_kx`$, $`\zeta_{x,k}=1+g_{\zeta,k}(x+\tfrac12)`$; the **gradients** of the level $`k`$ are $`G_k`$, $`\mathcal F_k`$, $`g_{\zeta,k}`$, and the numbers $`V_k`$ are the **level offsets**. The class $`\mathcal C`$ of 03-clock-and-fall is the subclass $`\tau_k=\tau`$, $`\zeta_{x,k}=\zeta_x`$, $`M_{x,k}=m_x+\eta_xd_k`$, $`V_{x,k}=V_x`$. The results quoted from 04-branch-fall were derived with $`V_k=0`$ and concern starts in one level.
- **Linear profiles of the field (item 3).** $`\Phi_x=N_0+x\,Y`$ with self-adjoint operators $`N_0`$, $`Y`$ on $`\mathcal H_f`$, $`\langle\varphi_0\vert N_0\vert\varphi_0\rangle=1`$ and $`g:=\langle\varphi_0\vert Y\vert\varphi_0\rangle`$, so that $`N(x)=1+g\,x`$, with $`\lvert g\rvert(L+1)<1`$. $`N_0`$ and $`Y`$ need not commute with each other or with $`C_f`$. "First order in the gradient operator" means first order in $`Y`$, that is jointly in $`g`$ and in $`Y-g\,\mathbb 1_f`$.

1. **First order.**
   - (a) Determine the operator $`\hat C:=(\mathbb 1_b\otimes\langle\varphi_0\rvert\otimes\mathbb 1_c)\,C\,(\mathbb 1_b\otimes\lvert\varphi_0\rangle\otimes\mathbb 1_c)`$ on $`\mathcal H_b\otimes\mathcal H_c`$, and the member of the class $`\mathcal C`$ that its body part is. State whether $`\hat C`$ is the contract of an admissible description of $`b`$ and $`c`$, and how $`N(x)`$ and $`\hat C`$ change under the replacements (2.20).
   - (b) Let $`\Pi_0:=\mathbb 1_b\otimes\lvert\varphi_0\rangle\langle\varphi_0\rvert\otimes\mathbb 1_c`$ and $`\Psi(\lambda)=e^{-iC\lambda}\Psi_0`$. Determine a bound on $`\lVert(\mathbb 1-\Pi_0)\Psi(\lambda)\rVert`$ in terms of $`\varepsilon`$, $`\Delta_f`$ and the scales of the body, with the range of $`\lambda`$ on which it holds; an order estimate with stated conditions suffices where no bound is derived.
   - (c) State to which order in $`\epsilon_1`$, and on which range of $`\lambda`$, the statistics of every schedule of readings on $`b`$ and $`c`$ are those of the description with the contract $`\hat C`$, that is of the body in a sharp field with the profile $`N(x)`$.

2. **Second order.** Determine a self-adjoint operator $`H_{\rm eff}`$ on $`\mathcal H_b\otimes\mathcal H_c`$, through second order in $`\epsilon_1`$, such that $`\Pi_0\Psi(\lambda)=\bigl(e^{-iH_{\rm eff}\lambda}(\phi\otimes\chi)\bigr)\otimes\varphi_0`$ up to stated errors.
   - (a) Give its term of second order in $`\epsilon_1`$ at leading order in $`\epsilon_2`$, and the form and the order of the first correction in $`\epsilon_2`$ (an order estimate with stated conditions suffices for the correction). State the range of $`\lambda`$ on which $`H_{\rm eff}`$ reproduces the statistics of readings on $`b`$ and $`c`$ to a given accuracy.
   - (b) Determine the on-site blocks and the hopping blocks of the body part of $`H_{\rm eff}`$ on each clock level. State whether the body part is a member of $`\mathcal C_{\rm lev}`$, give its level profiles, and name every term that is not of that form.
   - (c) State which of the new terms are well defined (M6) under (2.20).

3. **Fall, clock and relation.** With the linear profiles of the field, through second order in $`\epsilon_1`$ and first order in the gradient operator:
   - (a) Determine the level data $`\tau_k`$, $`M_k`$, the gradients $`G_k`$, $`\mathcal F_k`$, $`g_{\zeta,k}`$ and the level offsets $`V_k`$ of the body part of $`H_{\rm eff}`$. State why a level offset does not change (4.7) and (4.16) for a start in one level.
   - (b) Determine the drift accelerations from rest $`a_{k,\sigma}(0)`$ by (4.16). Determine the necessary and sufficient conditions on the data of the field under which they are the same for all levels: in the upper branch, in the lower branch, and in both branches with one value. Give the order in $`\epsilon_1`$ and $`\epsilon_2`$ at which the independence of the level that holds at first order is lost.
   - (c) Determine the differences $`E^+_{x,k+1}-E^+_{x,k}`$ of the upper on-site eigenvalues $`E^+_{x,k}:=V_{x,k}+M_{x,k}`$ of neighbouring levels, state whether they are independent of $`k`$, and determine the leading effect of a dependence on $`k`$ on the clock statistics of the start $`S_{\rm clock}(x_0)`$: the range of $`\lambda`$ in which the clock statistics is that of a ring clock with one rate to a given accuracy (an order estimate suffices).
   - (d) With the rate $`\bar r(x):=\frac{N}{2\pi}\,\frac{E^+_{x,N-1}-E^+_{x,0}}{N-1}`$ (the mean level spacing), determine whether the relation (4.24) holds for the body part of $`H_{\rm eff}`$, and the leading deviation from it.

4. **Example and control: independent cells.** For every position $`x`$ of the chain let $`f_x`$ be an object with two places $`\lvert0\rangle`$, $`\lvert1\rangle`$; the objects $`f_x`$, $`b`$ and $`c`$ are of pairwise different types. The contract is that of the class $`\mathcal D`$ with $`\mathcal H_f=\bigotimes_x\mathcal H_{f_x}`$, $`C_f=\sum_xC_{f_x}`$, $`C_{f_x}=\tfrac12\Delta_x\bigl(\lvert1\rangle\langle1\rvert-\lvert0\rangle\langle0\rvert\bigr)`$ with $`\Delta_x>0`$, and $`\Phi_x=n_x\mathbb 1+\varepsilon_x\bigl(\lvert0\rangle\langle1\rvert+\lvert1\rangle\langle0\rvert\bigr)`$ acting on the cell $`f_x`$, with $`n_x>0`$ and $`\varepsilon_x\ge0`$; every pair term then holds between $`b`$ and one cell (A5). Every cell starts in $`\lvert0\rangle`$.
   - (a) Evaluate $`N(x)`$, $`\varepsilon`$, $`\Delta_f`$ and the results of item 2.
   - (b) For a body at the position $`x`$ with the branch label $`s`$ in the clock level $`k`$, the cell $`f_x`$ has the contract $`C_{f_x}\pm M_k\Phi_x`$ (sign $`+`$ for $`s=1`$, $`-`$ for $`s=2`$). Determine its eigenvalues and its lower eigenvector exactly, compare with item 2, and determine the overlap of the lower eigenvector with $`\lvert0\rangle`$. State what this overlap multiplies in the motion of the body at leading order in $`\tau/\Delta_x`$.
   - (c) For the cells with $`n_x=1+g\,x`$ whose level profiles in the body part of $`H_{\rm eff}`$ are linear in $`x`$ (item 3(b) and the quoted (4.16) are statements for linear level profiles; the package names this subclass of cells by conditions on the cell data): evaluate item 3(b). Control, within this subclass: cells with $`\varepsilon_x^2/\Delta_x`$ independent of $`x`$ against cells in which it depends on $`x`$; state which level-dependent terms of item 3 vanish and which remain. For the cells outside the subclass, state which results of items 4(a) and 4(b) hold for them; their fall is not asked in this package. (Amended on 2026-10-11, after the second external verification: the first form of this item named only $`n_x=1+g\,x`$ and did not restrict the cells to linear level profiles.)

5. **Orders.** Give a table with one row for each of: the factor that the body sees; the independence of the fall from rest of the clock level; the clock as a ring clock with one rate; the relation (4.24). For each row state the order in $`\epsilon_1`$ and in $`\epsilon_2`$ at which a field with its own contract changes it, with the tags of the results used.

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

Eq. (2.20) of 02-field-object, the replacements of $`C_{br}`$, the $`\Phi_j`$ and $`C_f`$ at fixed $`B_j`$ that leave $`C`$ unchanged (exactly these, if $`\mathbb 1_b`$ and the $`B_j`$ are linearly independent):

```math
\Phi_j\to\Phi_j+a_j\,\mathbb 1_f,\qquad C_f\to C_f+c\,\mathbb 1_f,\qquad C_{br}\to C_{br}-\sum_{j\in J}a_j\,B_j\otimes\mathbb 1_r-c\,\mathbb 1_{br},\qquad a_j,c\in\mathbb R .
```

Eq. (2.22) of 02-field-object, for a sharp and stationary $`\varphi`$, with $`C_{\rm red}`$ and $`e_f`$ of (2.3); the operator $`\hat C`$ depends only on $`C`$ and $`\varphi`$:

```math
\hat C:=C_{\rm red}+e_f\,\mathbb 1_{br}=(\mathbb 1_{br}\otimes\langle\varphi\rvert)\,C\,(\mathbb 1_{br}\otimes\lvert\varphi\rangle) ,
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

From 04-branch-fall@v3 (this subproject). Setting there: a body of the class $`\mathcal C_{\rm lev}`$ with linear level profiles (as under "Goal", with $`V_k=0`$), a medium with the records $`K_x=\kappa\,x\,X`$. With all gradients of the level $`k`$ set to zero the level block is $`-\tau_k\sin\hat p\,\sigma_1+M_k\sigma_3`$, with the eigenvalues $`\pm\omega_k(p)`$, $`\omega_k(p):=\sqrt{M_k^2+\tau_k^2\sin^2p}`$, and the eigenvectors $`\beta_{k,\pm}(p)`$ of (5.6) of 04-ilang-time/05-moving-clock with $`\tau\to\tau_k`$, $`\mu_k\to M_k`$. For a level $`k`$, a branch $`\sigma\in\{+,-\}`$ and a smooth $`2\pi`$-periodic $`g`$ with $`\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g\rvert^2=1`$, the **branch start** $`B_{k,\sigma}[g]`$ is $`\lvert\phi\rangle=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\,g(p)\,\lvert p\rangle\otimes\beta_{k,\sigma}(p)\otimes\lvert f_k\rangle`$ on the infinite chain, and $`\langle F\rangle_g:=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g(p)\rvert^2F(p)`$; it is **at rest** if the weight $`\lvert g\rvert^2\frac{\mathrm dp}{2\pi}`$ is concentrated at $`p_0=0`$. "First order in the gradients" means first order jointly in the gradients of the level $`k`$, at fixed $`\lambda`$, start and chain, followed by the limit of a long chain; records at leading order in $`\kappa`$. The **drift acceleration** $`a_{k,\sigma}(p_0)`$ is the first-order acceleration of the mean position label $`\bar x_{\rm lab}(\lambda):=\sum_xx\,p_x(\lambda)`$ for a branch start, averaged over a long window, followed by the limit of a sharp label.

Eq. (4.7) of 04-branch-fall. The first-order velocity of $`B_{k,\sigma}[g]`$ is $`\lambda\,\langle a_{k,\sigma}\rangle_g`$ plus a rest that is bounded for all $`\lambda\ge0`$, with the coefficient

```math
\boxed{\;a_{k,\sigma}(p)=\frac{g_{\zeta,k}\tau_k^4\sin^2p-G_kM_k\tau_k^2\cos2p}{\omega_k^2}+\sigma\,\mathcal F_k\,\frac{\tau_k^2\bigl(M_k^2\cos2p-\tau_k^2\sin^4p\bigr)}{\omega_k^3}\;},\qquad\lvert a_{k,\sigma}(p)\rvert\le\frac{\tau_k^2}{M_k}\,\mathsf b_k .
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
- The types of the objects are pairwise different and each has one instance, so no swap condition applies.
- The class $`\mathcal D`$, the start of the field in a nondegenerate eigenvector of its own contract with a gap, the linear profiles of the field and the cells of item 4 are assumptions of this package (M8, M9, A11). The language selects no state of the field: the results state what this class of starts gives.
- Standard perturbation theory for a nondegenerate eigenvalue separated by a gap may be used; state the form used and its conditions.
- The quoted results of 03-clock-and-fall and 04-branch-fall are used for the body part of $`\hat C`$ and of $`H_{\rm eff}`$ where it is a member of the quoted class, with their starts, their orders and their limits.
- Every limit is stated with its order: the limit of a sharp label, an average over a window, the growth of $`\lambda`$ and the expansion parameters. Where two of them do not commute, both orders are given, each with the quantity it defines. A statement about a rate of change (a velocity, an acceleration, the rate of a clock) is derived for that rate; it is not inferred from a bound or an estimate of the quantity whose derivative it is.
- Every statement with "all", "iff" or "well defined" is stated with its exceptional members (a field operator that is a multiple of the identity, $`\varepsilon=0`$, equal data of two levels); a condition that is only sufficient is called sufficient.

## Scope

- **Class.** Items 1 and 2: every member of $`\mathcal D`$ and every $`\varphi_0`$ as stated, every start of the body. Item 3: the members with the linear profiles of the field, every $`N_0`$, $`Y`$, $`C_f`$ and $`\varphi_0`$ as stated, branch starts at rest and the starts $`S_{\rm clock}(x_0)`$. Item 4(a), 4(b): the cells, every $`\Delta_x>0`$, $`n_x>0`$, $`\varepsilon_x\ge0`$. Item 4(c): the subclass of these cells with $`n_x=1+g\,x`$ and linear level profiles.
- **Controls.** A sharp and stationary field ($`\varepsilon=0`$) against $`\varepsilon>0`$, in every item; the cells with $`\varepsilon_x^2/\Delta_x`$ independent of $`x`$ against cells in which it depends on $`x`$, within the subclass of item 4(c).
- In scope:
  - the factor that the body sees when the field is in a nondegenerate eigenvector of its own contract, and the error of this description;
  - the terms of second order in the fluctuating part of the pair term, for a fast field, and their effect on the fall from rest, on the clock and on the relation (4.24);
  - the exactly solvable on-site problem of a cell.
- Out of scope:
  - a field that is not in an eigenvector of its own contract (a later package), and a degenerate eigenvalue;
  - a field that is slow against the body ($`\epsilon_2`$ not small) beyond the statement of where the expansion fails;
  - the fall in motion (the order $`v^2`$), the second order in the gradient operator, lattice terms, and records beyond leading order in $`\kappa`$;
  - the fall in level profiles that are not linear in $`x`$ (a later package);
  - where the field comes from, two bodies in one field, and instances of one type;
  - any physical meaning beyond the definitions (M1–M4); no theory of gravity and no theory that contains time may be used as an input.

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: (a), (b) derive; (c), (d) short argument.
- Item 4: short argument.
- Item 5: standard (a table of results with their tags).

## Expected result

- Item 1: an operator with its class data, a yes/no answer and transformation rules; a bound or an estimate with its range; an order with a range.
- Item 2: an operator with a leading term, an estimate of the correction and a range; blocks with a yes/no answer and a list of terms; yes/no answers.
- Item 3: level data with a reason; closed forms, three equivalences and an order; a closed form, a yes/no answer and a range; a yes/no answer with a leading term.
- Item 4: evaluations; exact eigenvalues and an eigenvector, a comparison, an overlap and a statement; an evaluation and a control.
- Item 5: a table.

Give every main result a tag $`(10.k)`$.

Consistency checks, at most three: for example a sharp field ($`\varepsilon=0`$), the exact eigenvalue of a cell against the second-order term, and a field operator that commutes with $`C_f`$.

## Code

None.
