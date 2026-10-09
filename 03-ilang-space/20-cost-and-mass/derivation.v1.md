# Cost on the background, and the inertia of a body

- **Subproject:** 03-ilang-space
- **Package:** 03-ilang-space/20-cost-and-mass
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-09

## Setup and assumptions

- **Item 1.** Any description satisfying A1–A7; $`b`$ is the only instance of its type $`T`$, $`A=\{b\}`$. Inputs (2.1), (2.2): $`\lvert\Psi\rangle=\sum_h\lvert h\rangle\otimes\lvert\psi_h\rangle`$, $`(V_A)_{hh'}=\langle\psi_{h'}\vert\psi_h\rangle`$, $`p_h=\lVert\psi_h\rVert^2`$. Notation: $`Q_h:=\lvert h\rangle\langle h\rvert\otimes\mathbb 1_{\bar A}`$; for a set $`R`$ of places $`Q_R:=\sum_{h\in R}Q_h`$, $`\bar Q:=\mathbb 1-Q_R`$, $`p_R:=\sum_{h\in R}p_h`$.
- **Items 2–4.** Body–medium setting of the question: $`C_{hh'}=t_{hh'}\mathbb 1_c`$ ($`h\neq h'`$), $`C_{hh}=t_{hh}\mathbb 1_c+K_h`$; the cost edges between different places are the hopping edges $`E`$. Background vectors $`u_h=(K_h-\epsilon_h)\chi`$ (5.10), (17.2); they are fixed by the start and do not depend on $`\lambda`$. Notation: $`\hat K_h:=C_{hh}-\Omega_h\mathbb 1_c=K_h-\epsilon_h`$, so that $`u_h=\hat K_h\chi`$ and $`\langle\chi\vert\hat K_h\vert\chi\rangle=0`$; $`\Delta_{hh'}:=u_h-u_{h'}`$.
- **Inputs from 17**, used as quoted: (17.1), (17.4), (17.11)–(17.12), (17.15), (17.19), (17.22), and from Step 9 of 17 the decomposition $`P_j\to\Pi_\xi`$, $`D_\xi=\xi M`$, $`U_\xi=e^{-i(C_b+\xi M)\lambda}`$, $`U_\xi^\dagger SU_\xi=e^{-i\xi\lambda}S`$.
- $`C`$ does not depend on $`\lambda`$; $`\lambda\ge0`$. Items 1, 2 are exact for every $`\lambda`$; item 3 is at $`\lambda=0`$. On the infinite chain all sums over $`m`$ converge absolutely, since $`\lvert\langle\psi_m\vert Y\vert\psi_n\rangle\rvert\le\lVert Y\rVert\sqrt{p_mp_n}`$ and $`\sum_mp_m=1`$; shifts of the summation index are therefore allowed.

## Derivation

### Step 1. Block form and the cost identity (item 1a)

Inserting $`\sum_hQ_h=\mathbb 1`$ on both sides of $`C`$, and using $`(\langle h\rvert\otimes\mathbb 1)\lvert\Psi\rangle=\lvert\psi_h\rangle`$ (2.1) in (1.9):

```math
C=\sum_{h,h'}\lvert h\rangle\langle h'\rvert\otimes C_{hh'},\quad C_{h'h}=C_{hh'}^\dagger,\qquad
i\frac{\mathrm d}{\mathrm d\lambda}\lvert\psi_h\rangle=\sum_{h'}C_{hh'}\lvert\psi_{h'}\rangle .
\tag{20.1}
```

In the setting of items 2–4 the second equation is (17.1). The definitions read $`L_h=\langle\Psi\vert Q_hCQ_h\vert\Psi\rangle`$ and $`L_{hh'}=2\mathrm{Re}\langle\Psi\vert Q_hCQ_{h'}\vert\Psi\rangle`$. Now $`L=\sum_{h,h'}\langle\psi_h\vert C_{hh'}\vert\psi_{h'}\rangle`$. The diagonal terms are the $`L_h`$, which are real because $`C_{hh}`$ is self-adjoint. For $`h\neq h'`$ the terms $`(h,h')`$ and $`(h',h)`$ are complex conjugates by $`C_{h'h}=C_{hh'}^\dagger`$, so together they give $`L_{hh'}`$. Hence, for every state and every $`\lambda`$,

```math
L=\sum_hL_h+\sum_{\{h,h'\}}L_{hh'},\qquad L_{hh'}=0\ \text{unless }\{h,h'\}\text{ is a cost edge}.
\tag{20.2}
```

**Conventions.** (i) *Placement (A5):* $`L_h`$ and $`L_{hh'}`$ involve only the total $`C`$, $`\Psi`$ and $`Q_h`$. Moving a single-object term to another pair term changes the contract list but not $`C`$, so it changes nothing. (ii) *Common phase (1.2):* both are sesquilinear in $`\Psi`$, so they are invariant. (iii) *Phase split (1.6):* $`\psi_h=a_h\lvert E_h\rangle`$ is defined by (2.1) directly from $`\Psi`$, so no split enters. (iv) *Labels in $`\bar A`$ (M6):* a relabelling of identical-type objects in $`\bar A`$ acts as a permutation unitary $`P`$ on $`\mathcal H_{\bar A}`$, $`\Psi\to P\Psi`$, $`C\to PCP^\dagger`$. Since $`b`$ is unique of its type, $`P`$ commutes with $`Q_h`$, so both quantities are unchanged. Hence every site and edge cost is free of these conventions, and so is every aggregate of them on background points.

### Step 2. Shift $`C\to C+c\mathbb 1`$ (item 1b)

The shift adds $`c\mathbb 1_{\bar A}`$ to every $`C_{hh}`$ and leaves $`C_{hh'}`$ ($`h\neq h'`$) unchanged. The evolved state changes by $`e^{-ic\lambda}`$, which cancels in sesquilinear quantities. Hence

```math
L_h\to L_h+c\,p_h,\qquad L_{hh'}\to L_{hh'},\qquad L\to L+c .
\tag{20.3}
```

Every edge cost is invariant; no single site cost is (unless $`p_h=0`$). A real combination $`\sum_h\alpha_hL_h+\sum\beta_{hh'}L_{hh'}`$, with coefficients that may depend on the state, is invariant iff $`\sum_h\alpha_hp_h=0`$. If the coefficients are state independent, this forces $`\alpha_h=0`$. Examples of invariant combinations:

```math
L_h-p_hL,\qquad L_R-p_RL,\qquad \frac{L_h}{p_h}-\frac{L_{h'}}{p_{h'}}\quad(p_h,p_{h'}>0).
\tag{20.4}
```

### Step 3. Rate of change of $`L_R`$ (item 1c)

1. The algebra of Step 1, restricted to $`R`$, gives $`L_R=\langle\Psi\vert Q_RCQ_R\vert\Psi\rangle`$.
2. By (1.9), for a $`\lambda`$-independent operator $`B`$: $`\frac{\mathrm d}{\mathrm d\lambda}\langle\Psi\vert B\vert\Psi\rangle=i\langle\Psi\vert[C,B]\vert\Psi\rangle`$.
3. Split $`C=Q_RCQ_R+Q_RC\bar Q+\bar QCQ_R+\bar QC\bar Q`$. Since $`Q_R\bar Q=0`$, the outer block $`\bar QC\bar Q`$ commutes with $`Q_RCQ_R`$, and $`[C,Q_RCQ_R]=\bar QCQ_RCQ_R-Q_RCQ_RC\bar Q`$. The second operator is the adjoint of the first, so $`i\langle[C,Q_RCQ_R]\rangle=2\mathrm{Im}\langle Q_RCQ_RC\bar Q\rangle`$. Written in blocks:

```math
\frac{\mathrm dL_R}{\mathrm d\lambda}=\sum_{h\in R}\sum_{k\notin R}2\mathrm{Im}\langle\zeta^R_h\vert C_{hk}\vert\psi_k\rangle,
\qquad \lvert\zeta^R_h\rangle:=\sum_{h'\in R}C_{hh'}\lvert\psi_{h'}\rangle .
\tag{20.5}
```

4. **Which blocks enter.** Every term contains exactly one boundary block $`C_{hk}`$ ($`h\in R`$, $`k\notin R`$), linearly. The interior blocks $`C_{hh'}`$ ($`h,h'\in R`$, diagonal blocks included) enter through $`\zeta^R_h`$. Exterior blocks $`C_{kk'}`$ ($`k,k'\notin R`$) do not enter. Hence **$`L_R`$ can change only through the boundary blocks**: if all of them vanish, $`L_R`$ is constant. The rate is not a function of the boundary blocks alone, however. It is weighted by the interior blocks and by the branch vectors on both sides, and through $`\zeta^R_h`$ it depends on $`R`$; it is not a sum of $`R`$-independent pair currents. In the setting of items 2–4 the boundary blocks are $`t_{hk}\mathbb 1_c`$, so cost crosses the boundary of $`R`$ only along hopping edges.
5. Under $`C\to C+c\mathbb 1`$, $`\zeta^R_h\to\zeta^R_h+c\psi_h`$. The rate therefore gains $`c\sum_{h\in R,k\notin R}2\mathrm{Im}\langle\psi_h\vert C_{hk}\vert\psi_k\rangle=c\,\mathrm dp_R/\mathrm d\lambda`$ (by (20.6) below), consistent with $`L_R\to L_R+cp_R`$.

### Step 4. Acceleration (item 2)

1. By (20.1), $`\dot p_h=2\mathrm{Re}\langle\psi_h\vert\dot\psi_h\rangle`$. The term with $`C_{hh}`$ drops out because it is real, so

```math
\frac{\mathrm dp_h}{\mathrm d\lambda}=\sum_{h'\neq h}J_{h'\to h},\qquad J_{h'\to h}:=2\mathrm{Im}\langle\psi_h\vert C_{hh'}\vert\psi_{h'}\rangle=-J_{h\to h'} .
\tag{20.6}
```

   With $`C_{hh'}=t_{hh'}\mathbb 1_c`$ and (2.2) this is (17.4).
2. Since the $`u_h`$ do not depend on $`\lambda`$: $`a=\sum_h\ddot p_hu_h=\sum_{h\neq h'}\dot J_{h'\to h}u_h=\sum_{\{h,h'\}}\dot J_{h'\to h}\Delta_{hh'}`$, by antisymmetry.
3. By (20.1), $`\langle\dot\psi_h\rvert=i\sum_k\langle\psi_k\rvert C_{kh}`$, so $`\frac{\mathrm d}{\mathrm d\lambda}\langle\psi_h\vert C_{hh'}\vert\psi_{h'}\rangle=i\sum_k\bigl[\langle\psi_k\vert C_{kh}C_{hh'}\vert\psi_{h'}\rangle-\langle\psi_h\vert C_{hh'}C_{h'k}\vert\psi_k\rangle\bigr]`$. Separating $`k=h`$ in the first sum and $`k=h'`$ in the second gives the exact identity

```math
a(\lambda)=\sum_{\{h,h'\}\in E}\bigl[A_{hh'}+B_{hh'}\bigr]\Delta_{hh'},\qquad
\begin{aligned}
A_{hh'}&=2\mathrm{Re}\bigl[\langle\eta_h\vert C_{hh'}\vert\psi_{h'}\rangle-\langle\psi_h\vert C_{hh'}\vert\eta_{h'}\rangle\bigr],\quad \lvert\eta_h\rangle:=\textstyle\sum_{k\neq h}C_{hk}\lvert\psi_k\rangle,\\
B_{hh'}&=2\mathrm{Re}\langle\psi_h\vert C_{hh}C_{hh'}-C_{hh'}C_{h'h'}\vert\psi_{h'}\rangle .
\end{aligned}
\tag{20.7}
```

   $`A`$ and $`B`$ are antisymmetric under $`h\leftrightarrow h'`$ and contain the factor $`C_{hh'}`$, so only cost edges contribute. The sum runs over $`E`$.
4. **Split by diagonal blocks.** The *hopping part* $`a^{\rm hop}:=\sum_EA_{hh'}\Delta_{hh'}`$ contains only off-diagonal blocks. The *cost part* $`a^{\rm cost}:=\sum_EB_{hh'}\Delta_{hh'}`$ contains each diagonal block once. With $`C_{hh'}=t_{hh'}\mathbb 1_c`$, $`B_{hh'}=2\mathrm{Re}[t_{hh'}\langle\psi_h\vert C_{hh}-C_{h'h'}\vert\psi_{h'}\rangle]`$, so diagonal blocks enter only through **differences $`C_{hh}-C_{h'h'}`$ across hopping edges**. Inserting $`C_{hh}=\Omega_h\mathbb 1_c+\hat K_h`$ and $`L_{hh'}=2\mathrm{Re}[t_{hh'}\langle\psi_h\vert\psi_{h'}\rangle]`$:

```math
B_{hh'}(\lambda)=L_{hh'}(\lambda)\,(\Omega_h-\Omega_{h'})+Z_{hh'}(\lambda),\qquad Z_{hh'}:=2\mathrm{Re}\bigl[t_{hh'}\langle\psi_h\vert\hat K_h-\hat K_{h'}\vert\psi_{h'}\rangle\bigr],
\tag{20.8}
```

   and $`A_{hh'}=2\mathrm{Re}[t_{hh'}(\langle\eta_h\vert\psi_{h'}\rangle-\langle\psi_h\vert\eta_{h'}\rangle)]`$ with $`\eta_h=\sum_{k\neq h}t_{hk}\psi_k`$. The cost part thus has two terms: site-cost-per-weight differences weighted by edge costs, and a record term $`Z`$. Both parts also depend on all blocks implicitly, through $`\psi_h(\lambda)`$.
5. **Invariance.** $`u_h=(C_{hh}-\Omega_h)\chi`$ and $`\Omega_h`$ are functions of $`C_{hh}`$ and $`\chi`$, and (20.7) contains only blocks of the total $`C`$. Hence $`a`$ does not depend on the placement of single-object terms; in particular $`K_h\to K_h+c_h`$, $`t_{hh}\to t_{hh}-c_h`$ leaves $`C_{hh}`$, $`u_h`$, $`a`$ unchanged. Under $`C\to C+c\mathbb 1`$: $`\psi_h(\lambda)\to e^{-ic\lambda}\psi_h(\lambda)`$ cancels; $`\eta_h`$, $`C_{hh}C_{hh'}-C_{hh'}C_{h'h'}`$, $`\Omega_h-\Omega_{h'}`$, $`\hat K_h`$ and $`u_h`$ are unchanged. So $`a`$, and each of $`A`$, $`L_{hh'}(\Omega_h-\Omega_{h'})`$ and $`Z`$ separately, is unchanged. The phase split of the start sends $`u_h\to e^{i\varphi}u_h`$ and $`a\to e^{i\varphi}a`$, the common isometry of 17.

### Step 5. Inertia at $`\lambda=0`$ (item 3)

For the product start, $`\psi_h(0)=\phi_h\chi`$ and $`\eta_h(0)=(\tau\phi)_h\chi`$ with $`(\tau\phi)_h:=\sum_{k\neq h}t_{hk}\phi_k`$. Hence $`L_{hh'}(0)=2\mathrm{Re}[t_{hh'}\phi_h^*\phi_{h'}]`$, and $`Z_{hh'}(0)=2\mathrm{Re}[t_{hh'}\phi_h^*\phi_{h'}]\,\langle\chi\vert\hat K_h-\hat K_{h'}\vert\chi\rangle=0`$.

**(a)** By (20.7)–(20.8), for arbitrary $`\Omega_h`$:

```math
a(0)=a_0+\sum_{\{h,h'\}\in E}L_{hh'}(0)\,(\Omega_h-\Omega_{h'})\,\Delta_{hh'},\qquad
a_0=\sum_{\{h,h'\}\in E}2\mathrm{Re}\Bigl[t_{hh'}\bigl((\tau\phi)_h^*\phi_{h'}-\phi_h^*(\tau\phi)_{h'}\bigr)\Bigr]\Delta_{hh'} .
\tag{20.9}
```

$`a_0`$ contains only the off-diagonal $`t_{hh'}`$, $`\phi`$ and the $`u_h`$, none of which changes when the $`t_{hh}`$ vary. Choosing $`t_{hh}=\text{const}-\epsilon_h`$ makes all $`\Omega_h`$ equal and removes the second term. So $`a_0`$ in (20.9) is the $`a_0`$ of the definition.

**(b)** For a uniform gradient, $`\Omega_h-\Omega_{h'}=g(f,\Delta_{hh'})=-g(F,\Delta_{hh'})`$. Then (20.9) gives

```math
a(0)=a_0+\mu F,\qquad \mu=-\sum_{\{h,h'\}\in E}L_{hh'}(0)\,\Delta_{hh'}\,g\bigl(\Delta_{hh'},\,\cdot\,\bigr) .
\tag{20.10}
```

- *Existence and uniqueness.* Every $`f\in\mathcal H_c`$ is realized, by $`t_{hh}=g(f,u_h)-\epsilon_h`$ (real). So the defining identity, required for all uniform gradients, fixes $`\mu`$ on all of $`\mathcal H_c`$, and (20.10) satisfies it. $`\mu F`$ depends on $`f`$ only through the $`g(f,\Delta_{hh'})`$, so the freedom in $`f`$ for given $`\Omega_h`$ does not matter.
- *Symmetry.* $`g(w,\mu w')=-\sum_EL_{hh'}(0)\,g(w,\Delta_{hh'})\,g(\Delta_{hh'},w')`$ is symmetric, because $`g`$ is. So **$`\mu`$ is $`g`$-symmetric**.
- *Which cost.* **$`\mu`$ is a function of the edge costs $`L_{hh'}(0)`$ and the background differences $`\Delta_{hh'}`$ alone.** It is unchanged by any variation of the $`t_{hh}`$, which changes every site cost $`L_h(0)=p_h\Omega_h`$ with $`p_h>0`$ arbitrarily, and $`L`$ by (20.2). It is not a function of the site costs: in Step 6(b), $`\theta=0`$ and $`\theta=\pi/2`$ have the same $`p_h`$, the same $`\Omega_h`$, hence the same site costs, but different $`\mu`$. It is not a function of $`L`$ either: $`\theta=0`$ with $`C`$ and $`\theta=\pi/2`$ with $`C+t\mathbb 1`$ have the same $`L(0)=\tfrac12\langle X\rangle+t`$, while $`\mu`$ (invariant under the shift by (20.3)) differs. The edge costs are free of all conventions (Steps 1–2), so $`\mu`$ is as well, up to the common isometry $`e^{i\varphi}`$ of the phase split.
- *Positivity.* $`g(w,\mu w)=-\sum_EL_{hh'}(0)\,g(\Delta_{hh'},w)^2`$. Hence $`\mu\ge0`$ iff this form is non-negative. It is sufficient that $`L_{hh'}(0)\le0`$ on every edge with $`\Delta_{hh'}\neq0`$; edges inside one background point do not contribute. The condition is also necessary when the nonzero $`\Delta_{hh'}`$ are linearly independent over $`\mathbb R`$: take $`w`$ dual to one of them. If all $`\Delta_{hh'}=s_{hh'}n`$ are collinear, then $`\mu\ge0`$ iff $`\sum_Es_{hh'}^2L_{hh'}(0)\le0`$.

**(c)** Localized start $`\phi=\lvert\beta\rangle`$. One of $`\phi_h,\phi_{h'}`$ vanishes on every edge, so $`L_{hh'}(0)=0`$ and $`\mu=0`$. Further, $`(\tau\phi)_h=t_{h\beta}`$ for $`h\neq\beta`$ and $`(\tau\phi)_\beta=0`$. Only edges $`\{h,\beta\}`$ contribute to (20.9), with coefficient $`2\mathrm{Re}[t_{h\beta}t_{h\beta}^*]`$:

```math
a_0=2\sum_h\lvert t_{h\beta}\rvert^2(u_h-u_\beta)=2w_2,\qquad \mu=0,\qquad a(0)=2w_2\ \text{ for all }\Omega_h .
\tag{20.11}
```

This agrees with (17.11)–(17.12): $`\mathrm dv/\mathrm d\lambda(0)=2w_2`$, and $`w_2`$ does not depend on the $`t_{hh}`$.

### Step 6. Chain with linear records (item 4)

Data: $`t_{h_mh_{m\pm1}}=t`$, all other $`t_{hh'}=0`$ (including $`t_{hh}=0`$), $`\epsilon_{h_m}=m\langle X\rangle`$, $`\hat K_{h_m}=m(X-\langle X\rangle)`$, $`u_{h_m}=m\,e`$, $`\lVert e\rVert=\sigma_X`$ (17.15). Orient every edge as $`h=h_{m+1}`$, $`h'=h_m`$, so that $`\Delta=e`$. Write $`\psi_m:=\psi_{h_m}`$, $`p_m:=p_{h_m}`$.

**(a)** $`\Omega_{h_m}=t_{h_mh_m}+\epsilon_{h_m}=m\langle X\rangle`$. A uniform gradient needs $`g(f,(m-n)e)=(m-n)\langle X\rangle`$, i.e. $`g(f,e)=\langle X\rangle`$. This is solved by $`f=\langle X\rangle e/\sigma_X^2`$, and every other solution differs from it by a vector $`g`$-orthogonal to $`e`$, which $`\mu`$ annihilates. So the gradient is uniform, and

```math
\Omega_{h_m}=m\langle X\rangle,\qquad F=-\frac{\langle X\rangle}{\sigma_X^2}\,e .
\tag{20.12}
```

**The hopping part vanishes on the chain.** $`\eta_m=t(\psi_{m+1}+\psi_{m-1})`$, so $`A_{h_{m+1}h_m}=2t^2\mathrm{Re}\bigl[\langle\psi_{m+2}\vert\psi_m\rangle-\langle\psi_{m+1}\vert\psi_{m-1}\rangle\bigr]+2t^2(p_m-p_{m+1})`$. All $`\Delta=e`$, so $`a^{\rm hop}=e\sum_mA_{h_{m+1}h_m}=0`$ by an index shift, for every state:

```math
a^{\rm hop}(\lambda)\equiv0,\qquad a_0=0\ \text{ for every start} .
\tag{20.13}
```

**(b)** Start $`\phi_{h_0}=2^{-1/2}`$, $`\phi_{h_1}=2^{-1/2}e^{i\theta}`$. The only edge with $`\phi_h\phi_{h'}\neq0`$ is $`\{h_0,h_1\}`$. By (20.10), (20.13) and (20.12):

```math
L_{h_0h_1}(0)=t\cos\theta\ \ (\text{all other edge costs }0),\qquad \mu=-t\cos\theta\;e\,g(e,\,\cdot\,),\qquad a_0=0,\qquad a(0)=t\cos\theta\,\langle X\rangle\,e .
\tag{20.14}
```

Here $`a(0)=\mu F=-t\cos\theta\,e\,g(e,F)=t\cos\theta\,\langle X\rangle e`$. The derivative of (17.22) at $`\lambda=0`$ is $`t\sum_\xi w_\xi\,\xi\cos\theta\;e=t\cos\theta\,\langle X\rangle e`$, using $`\sum_\xi w_\xi\xi=\langle X\rangle`$: **agreement**. Since $`g(w,\mu w)=-t\cos\theta\,g(e,w)^2`$ with $`t>0`$ and $`e\neq0`$, **$`\mu`$ is positive semidefinite iff $`\cos\theta\le0`$**. It is positive on the span of $`e`$ iff $`\cos\theta<0`$, and $`\mu=0`$ at $`\cos\theta=0`$.

Start $`\lvert h_0\rangle\otimes\lvert\chi\rangle`$: by (20.11), $`\mu=0`$ and $`a_0=2t^2(u_{h_1}+u_{h_{-1}}-2u_{h_0})=0`$, hence $`a(0)=0`$. By (17.19), $`\bar x\equiv0`$, so $`a(0)=0`$: **agreement**.

**(c)** $`\lambda>0`$, start of (b). $`C(\mathbb 1\otimes\Pi_\xi)=(C_b+\xi M)\otimes\Pi_\xi`$, so $`\psi_m(\lambda)=\sum_\xi(U_\xi\phi)_m\,\Pi_\xi\chi`$ (Step 9 of 17). For any function $`q`$ of $`X`$, using $`\sum_m\varphi^*_{m+1}\varphi_m=\langle\varphi\vert S^\dagger\vert\varphi\rangle`$, $`U_\xi^\dagger S^\dagger U_\xi=e^{i\xi\lambda}S^\dagger`$ and $`\langle\phi\vert S^\dagger\vert\phi\rangle=\tfrac12e^{-i\theta}`$:

```math
\sum_m2\mathrm{Re}\bigl[t\langle\psi_{m+1}\vert q(X)\vert\psi_m\rangle\bigr]=t\sum_\xi w_\xi\,q(\xi)\cos(\xi\lambda-\theta) .
```

With $`q=1`$ this is the total edge cost $`\mathcal T(\lambda):=\sum_mL_{h_mh_{m+1}}(\lambda)=t\sum_\xi w_\xi\cos(\xi\lambda-\theta)`$. All $`\Delta=e`$, so the edge-cost expression (20.10) gives $`\mu(\lambda)=-\mathcal T(\lambda)\,e\,g(e,\cdot)`$ and $`\mu(\lambda)F=\langle X\rangle\mathcal T(\lambda)\,e`$. With $`q=X-\langle X\rangle`$ it gives $`\sum_mZ_{h_{m+1}h_m}`$. By (20.7), (20.8), (20.13), $`a=\mu(\lambda)F+e\sum_mZ_{h_{m+1}h_m}`$:

```math
a(\lambda)=t\sum_\xi w_\xi\,\xi\cos(\xi\lambda-\theta)\,e,\qquad
a(\lambda)-\mu(\lambda)F=t\sum_\xi w_\xi(\xi-\langle X\rangle)\cos(\xi\lambda-\theta)\,e=t\mathrm{Re}\Bigl[e^{-i\theta}\langle\chi\vert(X-\langle X\rangle)e^{iX\lambda}\vert\chi\rangle\Bigr]e .
\tag{20.15}
```

$`a(\lambda)`$ is the derivative of (17.22). **$`a(\lambda)=\mu(\lambda)F`$ does not hold in general.** The difference is the record term, $`t\langle\Psi\vert(S+S^\dagger)\otimes(X-\langle X\rangle)\vert\Psi\rangle\,e`$: the correlation between hopping and record fluctuation, which vanishes at $`\lambda=0`$ because the start is a product. For small $`\lambda`$ it is $`t\sigma_X^2\sin\theta\,\lambda\,e+O(\lambda^2)`$, so it is nonzero whenever $`\sin\theta\neq0`$. If $`\sin\theta=0`$, the difference is $`\pm t\sum_{\nu\ge0}c_\nu\cos(\nu\lambda)\,e`$ with $`c_\nu:=\sum_{\xi=\pm\nu}w_\xi(\xi-\langle X\rangle)`$. Cosines of distinct frequencies are linearly independent, so the identity holds for all $`\lambda`$ iff $`\sin\theta=0`$ and $`c_\nu=0`$ for every $`\nu\ge0`$. This happens, for example, when the spectrum of $`X`$ in $`\chi`$ lies in $`\{\nu,-\nu\}`$.

## Result

- **(20.2)** $`L=\sum_hL_h+\sum_{\{h,h'\}}L_{hh'}`$ exactly. Site and edge costs are free of the placement of single-object terms, of the common phase, of the phase split and of relabelling in $`\bar A`$.
- **(20.3)–(20.4)** Under $`C\to C+c\mathbb 1`$: $`L_h\to L_h+cp_h`$, $`L_{hh'}`$ invariant. The invariant combinations are exactly those with $`\sum_h\alpha_hp_h=0`$, e.g. $`L_h-p_hL`$, $`L_R-p_RL`$, $`L_h/p_h-L_{h'}/p_{h'}`$.
- **(20.5)** $`\mathrm dL_R/\mathrm d\lambda=\sum_{h\in R,k\notin R}2\mathrm{Im}\langle\zeta^R_h\vert C_{hk}\vert\psi_k\rangle`$. Each term contains exactly one boundary block, exterior blocks do not enter, and $`L_R`$ is constant if all boundary blocks vanish.
- **(20.7)–(20.8)** $`a=a^{\rm hop}+a^{\rm cost}`$. The diagonal blocks enter explicitly only through $`C_{hh}-C_{h'h'}`$ on hopping edges, as $`L_{hh'}(\Omega_h-\Omega_{h'})`$ plus the record term $`Z_{hh'}`$. $`a`$ is independent of placement and invariant under $`C\to C+c\mathbb 1`$.
- **(20.9)–(20.10)** $`a(0)=a_0+\sum_EL_{hh'}(0)(\Omega_h-\Omega_{h'})\Delta_{hh'}`$ and $`\mu=-\sum_EL_{hh'}(0)\,\Delta_{hh'}g(\Delta_{hh'},\cdot)`$. $`\mu`$ is $`g`$-symmetric and a function of the edge costs and the background alone, not of the site costs or of $`L`$. It is positive semidefinite iff $`-\sum_EL_{hh'}(0)g(\Delta_{hh'},w)^2\ge0`$ for all $`w`$, which holds in particular if all edge costs are $`\le0`$. **The inertia is governed by the edge (hopping) cost of the body.**
- **(20.11)** Localized start: $`\mu=0`$ and $`a_0=a(0)=2w_2`$, in agreement with (17.11)–(17.12).
- **(20.12)–(20.15)** Chain: $`\Omega_{h_m}=m\langle X\rangle`$ and $`F=-\langle X\rangle e/\sigma_X^2`$. For the start of 4(b): $`L_{h_0h_1}(0)=t\cos\theta`$, $`\mu=-t\cos\theta\,e\,g(e,\cdot)`$, $`a_0=0`$, $`a(0)=t\cos\theta\langle X\rangle e`$ (agrees with (17.22)), and $`\mu\ge0`$ iff $`\cos\theta\le0`$. For the start $`\lvert h_0\rangle`$: $`\mu=0`$ and $`a(0)=0`$ (agrees with (17.19)). For $`\lambda>0`$, $`a(\lambda)\neq\mu(\lambda)F`$ in general, with the difference given in (20.15).

## Consistency checks

1. **Dimensions.** Let $`[C]=\kappa`$ and $`[\lambda]=\kappa^{-1}`$. Then $`[u_h]=[\Omega_h]=[L]=\kappa`$ and $`[a]=\kappa^3`$. In (20.9), $`L\,\Omega\,\Delta`$ and $`t^2u`$ are both $`\kappa^3`$. From $`g(f,\Delta)=\Delta\Omega`$, $`f`$ is dimensionless, so $`[\mu]=\kappa^3`$. In (20.14)–(20.15), $`t\langle X\rangle e`$ is $`\kappa^3`$. In (20.5), $`C^2\psi^2`$ is $`\kappa^2=[L]/[\lambda]`$.
2. **No hopping; equal records.** If $`t_{hh'}=0`$ for $`h\neq h'`$, then $`E=\emptyset`$, so $`a\equiv0`$ and $`\mu=0`$. By (20.5) and (20.6) every $`L_R`$ and every $`p_h`$ is constant, as it must be for block-diagonal $`C`$. If all $`K_h`$ are equal, all $`u_h`$ coincide and $`\Delta=0`$, so $`a\equiv0`$ and $`\mu=0`$, consistent with $`\bar x`$ being constant.
3. **Conservation of $`L`$.** For $`R`$ = all places, $`\bar Q=0`$ and (20.5) gives $`\mathrm dL/\mathrm d\lambda=0`$. The shift check of Step 3.5 reproduces (20.3).

## Open issues

- $`\mu`$ is defined at $`\lambda=0`$ only. 4(c) shows that its edge-cost extension $`\mu(\lambda)`$ misses the record term $`Z`$ for $`\lambda>0`$. Whether a convention-free inertia exists for $`\lambda>0`$ is not addressed here.
- For general (neither independent nor collinear) edge vectors $`\Delta_{hh'}`$, positivity of $`\mu`$ is stated as positivity of the quadratic form in (20.10), not as a condition on single edge costs.

## Methods used

- block decomposition with respect to place projectors
- derivative of expectation values via commutators (Heisenberg form)
- antisymmetric pair currents and telescoping sums
- spectral decomposition of a conserved medium operator
- real quadratic forms and positivity
- linear independence of trigonometric functions
