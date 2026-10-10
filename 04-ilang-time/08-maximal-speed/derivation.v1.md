# Common maximal speed: two body types recorded by one medium

- **Subproject:** 04-ilang-time
- **Package:** 08-maximal-speed
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-10

## Setup and assumptions

**Setting (question.md).** Objects $`a`$ (type $`A`$, places $`h\in H_A`$), $`b`$ (type $`B`$, places $`k\in H_B`$) and the medium $`c`$; the three types are pairwise different and each has one instance, so (1.11) imposes nothing. The contract is

```math
C=C_A\otimes\mathbb 1_b\otimes\mathbb 1_c+\mathbb 1_a\otimes C_B\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert_a\otimes\mathbb 1_b\otimes K^A_h+\sum_k\mathbb 1_a\otimes\lvert k\rangle\langle k\rvert_b\otimes K^B_k ,
```

with $`C_A=\sum_{h,h'}t^A_{hh'}\lvert h\rangle\langle h'\rvert`$, $`C_B=\sum_{k,k'}t^B_{kk'}\lvert k\rangle\langle k'\rvert`$, $`K^A_h`$, $`K^B_k`$ self-adjoint, no contract between $`a`$ and $`b`$, and the start $`\lvert\phi\rangle_a\otimes\lvert\vartheta\rangle_b\otimes\lvert\chi\rangle_c`$. All contracts are independent of $`\lambda`$ (A5).

**Quoted definitions.** $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$; $`u^A_h:=(K^A_h-\langle K^A_h\rangle)\chi`$, $`u^B_k:=(K^B_k-\langle K^B_k\rangle)\chi`$, all in $`\mathcal N=\{v:\langle\chi\vert v\rangle=0\}`$; $`g(v,w)=\mathrm{Re}\langle v\vert w\rangle`$; $`d^a_0(h,h')=\lVert u^A_h-u^A_{h'}\rVert`$, $`d^b_0(k,k')=\lVert u^B_k-u^B_{k'}\rVert`$ (16.8); $`\bar x_a=\sum_hp^a_hu^A_h`$, $`v_a=\mathrm d\bar x_a/\mathrm d\lambda`$, and likewise for $`b`$; $`a^A_{hh'}=\lvert t^A_{hh'}\rvert d^a_0(h,h')`$, $`v^A_{\max}=\varrho(a^A)`$, and likewise for $`B`$.

**Inputs.** (16.3), (16.4), (16.8), (16.11), (16.13) of 03-ilang-space/16-common-space; (17.4), (17.7), (17.15), (17.20) of 03-ilang-space/17-motion; (5.11), (5.22), (5.25), (5.28), (5.29) of 05-moving-clock; (6.7), (6.15), (6.16), (6.20) of 06-inertia-internal-energy.

**Notation of this package.** $`T\in\{A,B\}`$ labels the type. In items 2 and 3, $`e_T:=(X_T-\langle X_T\rangle)\chi`$ with $`\lVert e_T\rVert=\sigma_{X_T}>0`$. The *record step* $`\ell_T`$ and the *hop modulus* $`\eta_T`$ are: for a chain (17.20), $`\ell_T:=e_T`$ and $`\eta_T:=t_T`$; for Model D, $`\ell_T:=\kappa_Te_T`$ and $`\eta_T:=\tau_T/2`$. $`d_1^T:=\lVert\ell_T\rVert`$ is the distance of neighbouring points ($`d_1`$ of (6.20) for Model D). In item 3: $`\rho_T:=\tau_T/\bar\mu_T`$, $`\nu`$ is the common drift speed and $`\beta_T:=\nu/v^T_{\max}`$.

**Exact statements and statements to an order.**
- Steps 1–6 (items 1 and 2) are exact, for finite systems (A1); the chains on $`\mathbb Z`$ of (17.20) and (5.11) are the limits $`L\to\infty`$ of open chains with $`L`$ positions.
- Steps 7–9 (item 3) use the weak-record regime for both bodies: leading order in $`\kappa_A`$ and $`\kappa_B`$ at fixed $`\lambda`$ and fixed start. Step 8 uses in addition the orders of (5.28), (5.29): first order in $`\epsilon_T`$, leading order in the spread $`\delta p_T`$, and small labels $`p_{0T}^2\ll1`$. Step 9 uses the orders of (6.20): first order in the force, average over long $`\lambda`$-intervals.

## Derivation

### Step 1. Replacements that leave $`C`$ unchanged, and their action (item 1a)

Write $`t'^A_{hh}=t^A_{hh}+\alpha^A_h`$, $`t'^B_{kk}=t^B_{kk}+\alpha^B_k`$, $`K'^A_h=K^A_h+\Delta^A_h`$, $`K'^B_k=K^B_k+\Delta^B_k`$, with $`\alpha^A_h,\alpha^B_k`$ real and $`\Delta^A_h,\Delta^B_k`$ self-adjoint (the new operators must be self-adjoint). With $`\mathbb 1_a=\sum_h\lvert h\rangle\langle h\rvert`$ and $`\mathbb 1_b=\sum_k\lvert k\rangle\langle k\rvert`$,

```math
C'-C=\sum_{h,k}\lvert h\rangle\langle h\rvert_a\otimes\lvert k\rangle\langle k\rvert_b\otimes\bigl[(\alpha^A_h+\alpha^B_k)\mathbb 1_c+\Delta^A_h+\Delta^B_k\bigr].
```

The projectors $`\lvert h\rangle\langle h\rvert\otimes\lvert k\rangle\langle k\rvert`$ are linearly independent, so $`C'=C`$ iff every bracket vanishes: $`\Delta^A_h+\alpha^A_h\mathbb 1_c=-(\Delta^B_k+\alpha^B_k\mathbb 1_c)`$ for all $`h,k`$. The left side does not depend on $`k`$ and the right side not on $`h`$, so both equal one self-adjoint operator $`Z`$. Conversely every such choice gives $`C'=C`$. Hence all replacements are

```math
t'^A_{hh}=t^A_{hh}+\alpha^A_h,\quad K'^A_h=K^A_h+Z-\alpha^A_h\mathbb 1_c,\qquad
t'^B_{kk}=t^B_{kk}+\alpha^B_k,\quad K'^B_k=K^B_k-Z-\alpha^B_k\mathbb 1_c ,
\qquad\text{(8.1)}
```

with $`\alpha^A_h,\alpha^B_k\in\mathbb R`$ and $`Z=Z^\dagger`$ on $`\mathcal H_c`$ arbitrary. The data $`(\alpha^A,\alpha^B,Z)`$ and $`(\alpha^A+c,\alpha^B-c,Z+c\mathbb 1_c)`$, $`c\in\mathbb R`$, give the same replacement. For $`\alpha^A=\alpha^B=0`$, (8.1) is (16.3). These are conventions of the description (A5, M6): $`Z`$ moves a single-object term of $`c`$ between the pair terms $`a`$–$`c`$ and $`b`$–$`c`$; $`\alpha^A_h`$ and $`\alpha^B_k`$ move a single-object term of a body between the two parts in which its pair term with $`c`$ is written.

*Action.* Multiples of $`\mathbb 1_c`$ cancel in $`K-\langle K\rangle`$, so $`u^A_h\mapsto u^A_h+z`$ and $`u^B_k\mapsto u^B_k-z`$ with $`z=(Z-\langle Z\rangle)\chi`$; every $`z\in\mathcal N`$ occurs (16.4). $`C`$ and the start are unchanged, hence so are $`\Psi(\lambda)`$, the views and the place weights $`p^a_h`$, $`p^b_k`$. With $`\sum_hp^a_h=\sum_kp^b_k=1`$:

```math
\begin{aligned}
\text{replacement (8.1):}\quad&\bar x_a\mapsto\bar x_a+z,\quad\bar x_b\mapsto\bar x_b-z,\quad v_a\mapsto v_a,\quad v_b\mapsto v_b,\quad v^A_{\max}\mapsto v^A_{\max},\quad v^B_{\max}\mapsto v^B_{\max};\\
\chi\mapsto e^{i\theta}\chi:\quad&(\bar x_a,\bar x_b,v_a,v_b)\mapsto e^{i\theta}(\bar x_a,\bar x_b,v_a,v_b),\quad v^A_{\max}\mapsto v^A_{\max},\quad v^B_{\max}\mapsto v^B_{\max}.
\end{aligned}
\qquad\text{(8.2)}
```

Reasons. First line: $`z`$ does not depend on $`\lambda`$; $`d^a_0`$, $`d^b_0`$ contain only differences of record vectors of one type; the off-diagonal $`t`$ are not replaced, and $`a^T_{hh}=0`$ for any $`t^T_{hh}`$ because $`d_0(h,h)=0`$. Second line: $`\langle X\rangle`$ is unchanged, so every record vector is multiplied by $`e^{i\theta}`$ (16.4); the state changes by a common phase (1.2), so the views are unchanged; norms of differences, hence $`d_0`$ and $`a^T`$, are unchanged. Phases of $`\phi`$ and $`\vartheta`$ change nothing.

### Step 2. Well-defined quantities (item 1b)

A quantity is well defined (M6) iff it is invariant under both lines of (8.2). Since $`\langle e^{i\theta}v\vert e^{i\theta}w\rangle=\langle v\vert w\rangle`$:

```math
\begin{aligned}
&\text{well defined:}&&\lVert v_a\rVert,\quad\lVert v_b\rVert,\quad g(v_a,v_b),\quad\lVert v_a-v_b\rVert,\quad v^A_{\max},\quad v^B_{\max},\quad v^A_{\max}/v^B_{\max}\ \ (\text{if }v^B_{\max}>0);\\
&\text{not well defined:}&&\bar x_a-\bar x_b\ \ (\text{neither the vector nor its norm}).
\end{aligned}
\qquad\text{(8.3)}
```

Indeed $`\bar x_a-\bar x_b\mapsto\bar x_a-\bar x_b+2z`$ with $`z\in\mathcal N`$ arbitrary, and $`\bar x_a-\bar x_b\in\mathcal N`$: at a given $`\lambda`$ it can be given any value in $`\mathcal N`$, for example $`0`$. (For $`\dim\mathcal H_c=1`$ all record vectors vanish and the statement is empty.) In addition, the norm of its change between two values of $`\lambda`$ is well defined, being the norm of an integral of $`v_a-v_b`$.

### Step 3. The bound for one body in the presence of the other (item 1c)

Let $`\lvert\psi_h\rangle:=(\langle h\rvert_a\otimes\mathbb 1_{bc})\lvert\Psi\rangle\in\mathcal H_b\otimes\mathcal H_c`$, so that $`p^a_h=\lVert\psi_h\rVert^2`$ and $`(V_a)_{h'h}=\langle\psi_h\vert\psi_{h'}\rangle`$ by (1.5). From (1.9), $`i\,\mathrm d\psi_h/\mathrm d\lambda=\sum_{h'}t^A_{hh'}\psi_{h'}+Q_h\psi_h`$ with $`Q_h:=C_B\otimes\mathbb 1_c+\mathbb 1_b\otimes K^A_h+\sum_k\lvert k\rangle\langle k\rvert_b\otimes K^B_k`$ self-adjoint. Then $`\mathrm dp^a_h/\mathrm d\lambda=2\mathrm{Re}\langle\psi_h\vert\dot\psi_h\rangle`$, and $`\langle\psi_h\vert Q_h\vert\psi_h\rangle`$ is real, so

```math
\frac{\mathrm dp^a_h}{\mathrm d\lambda}=\sum_{h'}J^a_{h'\to h},\qquad J^a_{h'\to h}:=2\mathrm{Im}\bigl[t^A_{hh'}\,(V_a)_{h'h}\bigr]=-J^a_{h\to h'} .
\qquad\text{(8.4)}
```

This is (17.4) with $`V_b`$ replaced by $`V_a`$: the body $`b`$, its contract and its records enter only through the view $`V_a`$. By the antisymmetry, $`v_a=\sum_h\dot p^a_hu^A_h=\tfrac12\sum_{h,h'}J^a_{h'\to h}(u^A_h-u^A_{h'})`$. With $`\lvert J^a_{h'\to h}\rvert\le2\lvert t^A_{hh'}\rvert\,\lvert(V_a)_{h'h}\rvert`$, the Cauchy–Schwarz inequality $`\lvert(V_a)_{h'h}\rvert\le q_hq_{h'}`$, $`q_h:=\sqrt{p^a_h}`$, and the Rayleigh bound for the real symmetric matrix $`a^A`$ and the unit vector $`q`$:

```math
\lVert v_a(\lambda)\rVert\le\sum_{h,h'}a^A_{hh'}\,q_h(\lambda)\,q_{h'}(\lambda)\le\varrho(a^A)=v^A_{\max}\qquad\text{for every start }\phi\otimes\vartheta\otimes\chi\text{ and every }\lambda\in\mathbb R .
\qquad\text{(8.5)}
```

So the answer is **yes**, exactly, in particular for every $`\lambda\ge0`$; the same holds for $`b`$. The product form of the start is used only to define $`\chi`$, hence the record vectors. Both sides of (8.5) are well defined by (8.3). The entries of $`a^A`$ are

```math
a^A_{hh'}=\lvert t^A_{hh'}\rvert\;\bigl\lVert\bigl(K^A_h-K^A_{h'}-\langle K^A_h-K^A_{h'}\rangle\bigr)\chi\bigr\rVert ,
\qquad\text{(8.6)}
```

so $`v^A_{\max}`$ is a function of the off-diagonal $`t^A_{hh'}`$, the differences $`K^A_h-K^A_{h'}`$ and $`\chi`$ only. It does **not** depend on $`C_B`$, on the $`K^B_k`$ or on $`\vartheta`$ (nor on $`\phi`$ or the $`t^A_{hh}`$). The only datum shared by $`v^A_{\max}`$ and $`v^B_{\max}`$ is the start $`\chi`$ of the medium. The velocity $`v_a(\lambda)`$ itself does depend on them, through $`V_a`$ in (8.4).

### Step 4. Maximal speeds of chain types and of Model D types (items 2a, 2b)

*Chain.* $`t^T_{h_mh_n}=t_T\,\delta_{\lvert m-n\rvert,1}`$ and $`d_0=\lvert m-n\rvert\sigma_{X_T}`$ (17.15), so $`a^T=t_T\sigma_{X_T}`$ times the adjacency matrix of a path with $`L_T`$ vertices, whose largest eigenvalue is $`2\cos\frac{\pi}{L_T+1}`$ (standard).
*Model D.* The record vector of the place $`(x,s,a)`$ is $`\kappa_Txe_T`$. The off-diagonal entries of $`C_T`$ come from $`A`$, which joins $`(x,s,a)`$ to $`(x\pm1,s',a)`$, $`s'\neq s`$, with modulus $`\tau_T/2`$ and $`d_0=\kappa_T\sigma_{X_T}`$, and from $`B`$, which joins places with the same $`x`$, where $`d_0=0`$. So $`a^T=\frac{\tau_T}2\kappa_T\sigma_{X_T}`$ times the adjacency matrix of $`2N_T`$ disjoint paths with $`L_T`$ vertices; $`m_T`$, $`N_T`$, $`\lambda_{0T}`$ do not enter. In both families

```math
v^T_{\max}=2\,\eta_T\,d_1^T\cos\frac{\pi}{L_T+1}\ \xrightarrow[L_T\to\infty]{}\ 2\,\eta_T\,d_1^T=
\begin{cases}2\,t_T\,\sigma_{X_T}&\text{chain, (17.20)},\\ \tau_T\,\kappa_T\,\sigma_{X_T}&\text{Model D, (5.11)}.\end{cases}
\qquad\text{(8.7)}
```

Hence, for chains on $`\mathbb Z`$ (and for finite chains with $`L_A=L_B`$), exactly,

```math
\text{(a) chains: } v^A_{\max}=v^B_{\max}\iff t_A\,\sigma_{X_A}=t_B\,\sigma_{X_B};\qquad
\text{(b) Model D: } v^A_{\max}=v^B_{\max}\iff\tau_A\,\kappa_A\,\sigma_{X_A}=\tau_B\,\kappa_B\,\sigma_{X_B}.
\qquad\text{(8.8)}
```

For finite chains with $`L_A\neq L_B`$ each side carries its factor $`\cos\frac{\pi}{L_T+1}`$.

### Step 5. The language does not imply equal maximal speeds (item 2c)

**No.** Take two open chains with the same $`L\ge2`$, $`X_A=X_B=X`$ with $`\sigma_X>0`$, and $`t_A=r\,t_B`$, $`r>0`$. This is an admissible description: finitely many objects and places (A1); $`C`$ self-adjoint and independent of $`\lambda`$, a sum of the pair terms $`a`$–$`c`$ and $`b`$–$`c`$ (Laws 3, 4, A5); a unit product start (A3); no identical instances, so Law 5 and A6 impose nothing; Laws 1, 2 and A2, A4, A7–A9 do not restrict the contract. By (8.7),

```math
\frac{v^A_{\max}}{v^B_{\max}}=\frac{t_A\,\sigma_{X_A}}{t_B\,\sigma_{X_B}}=r\qquad\text{takes every value in }(0,\infty).
\qquad\text{(8.9)}
```

In general, $`C_A\mapsto s\,C_A`$ ($`s>0`$) maps admissible descriptions to admissible descriptions, multiplies $`v^A_{\max}`$ by $`s`$ and leaves $`v^B_{\max}`$ unchanged, by (8.6). Equality of the maximal speeds is a condition on the description.

### Step 6. Common points (item 2d)

Let both chains have $`L`$ positions, with labels $`j_T,\dots,j_T+L-1`$. Positions are the points: places at one position have $`d_0=0`$, different positions have $`d_0=\lvert x-x'\rvert d_1^T>0`$. So $`\lvert X_A\rvert=\lvert X_B\rvert=L`$, $`U_T=\{j\,\ell_T\}`$ and $`U_T-\bar u^T=\{(j-\tfrac{L-1}2)\ell_T:\ j=0,\dots,L-1\}`$. By (16.13), a correspondence with $`D_A=X_A`$, $`D_B=X_B`$ exists iff $`L\ge2`$ and these two centred sets are equal. Their elements of largest norm are $`\pm\tfrac{L-1}2\ell_T`$, so equality forces $`\ell_B=\pm\ell_A`$; conversely $`\ell_B=\pm\ell_A`$ gives equal sets. Therefore

```math
\text{full correspondence}\iff\ell_B=\pm\ell_A\ \Longrightarrow\ d_1^A=d_1^B;\qquad\text{then}\quad v^A_{\max}=v^B_{\max}\iff\eta_A=\eta_B .
\qquad\text{(8.10)}
```

- Records: the two types have the same record vectors up to one translation $`t_\pi\in\mathcal N`$ (16.11), which a replacement (8.1) removes; neighbouring points are equally far apart for both types. For chains: $`(X_B-\langle X_B\rangle)\chi=\pm(X_A-\langle X_A\rangle)\chi`$, hence $`\sigma_{X_A}=\sigma_{X_B}`$. For Model D: $`\kappa_B(X_B-\langle X_B\rangle)\chi=\pm\kappa_A(X_A-\langle X_A\rangle)\chi`$, hence $`\kappa_A\sigma_{X_A}=\kappa_B\sigma_{X_B}`$. Nothing follows for $`X_A`$, $`X_B`$ as operators, nor for $`t_T`$, $`\tau_T`$, $`m_T`$, $`N_T`$, $`\lambda_{0T}`$.
- Condition: by (8.7) with equal $`L`$ and equal $`d_1^T`$, exactly, $`v^A_{\max}=v^B_{\max}`$ iff $`t_A=t_B`$ (chains), iff $`\tau_A=\tau_B`$ (Model D). Common points remove the records from the condition (8.8) and leave the hopping.

### Step 7. Why the one-body results apply to each body (item 3a)

Split $`C=C_0+C_{\rm rec}`$ with $`C_0:=C_A\otimes\mathbb 1\otimes\mathbb 1+\mathbb 1\otimes C_B\otimes\mathbb 1`$ and $`C_{\rm rec}`$ the record terms, of first order in $`\kappa_A`$, $`\kappa_B`$. A cost gradient in the diagonal entries of a body, as in 06-inertia-internal-energy, is part of its $`C_T`$. There is no contract between $`a`$ and $`b`$, so the two terms of $`C_0`$ act on different factors and commute. Duhamel's formula $`e^{-iC\lambda}=e^{-iC_0\lambda}-i\int_0^\lambda e^{-iC(\lambda-s)}C_{\rm rec}\,e^{-iC_0s}\,\mathrm ds`$ then gives, at fixed $`\lambda`$ and fixed start,

```math
\lvert\Psi(\lambda)\rangle=e^{-iC_A\lambda}\lvert\phi\rangle\otimes e^{-iC_B\lambda}\lvert\vartheta\rangle\otimes\lvert\chi\rangle+O(\kappa_A)+O(\kappa_B),\qquad
V_a(\lambda)=e^{-iC_A\lambda}\lvert\phi\rangle\langle\phi\rvert e^{iC_A\lambda}+O(\kappa_A)+O(\kappa_B),
\qquad\text{(8.11)}
```

and likewise for $`V_b`$. Three facts follow.
1. At leading order the view of each body is that of its own body contract alone, which is the defining property of the weak-record regime, and it equals the leading-order view of the one-body setting with the same $`C_T`$ and the same start.
2. By (8.6) the record vectors $`\kappa_Txe_T`$ of a body, hence the background (17.15) in which its position is measured, are those of the one-body setting with the medium start $`\chi`$.
3. Every quoted result of 05-moving-clock and 06-inertia-internal-energy is a statement about these two things only: the place weights of the body (position, branch and clock labels) and its record vectors.

Hence (5.11)–(5.29) and (6.7)–(6.20) hold for $`a`$ with the parameters of type $`A`$ and for $`b`$ with those of type $`B`$, with "$`O(\kappa)`$" read as "$`O(\kappa_A)+O(\kappa_B)`$". The quantities used below are well defined: $`\lVert\bar v_T\rVert`$ by (8.2), because $`\bar x(\lambda)-\bar x(0)`$ is invariant, and $`M^T_k`$ as half the gap of (6.7), which a uniform $`\alpha^T`$ in (8.1) does not change.

### Step 8. Moving clocks (item 3b)

Let $`\nu:=\lVert\bar v_a\rVert=\lVert\bar v_b\rVert`$ for the drift velocities (5.25) of the two clock-carrying starts. By Step 7, (5.28) holds for each type with its own $`v^T_{\max}`$ of (8.7): $`R_T=1+\nu^2/\bigl(2(v^T_{\max})^2\bigr)+O(p_{0T}^4)`$. By (5.22) and (5.25), $`\beta_T^2=\rho_T^2p_{0T}^2+O(p_{0T}^4)`$, so the two labels are small together. Subtracting,

```math
R_A-R_B=\frac{\nu^2}2\Bigl[\frac1{(v^A_{\max})^2}-\frac1{(v^B_{\max})^2}\Bigr]+O(p_{0A}^4)+O(p_{0B}^4)
=\frac{\nu^2}2\Bigl[\frac1{\tau_A^2\kappa_A^2\sigma_{X_A}^2}-\frac1{\tau_B^2\kappa_B^2\sigma_{X_B}^2}\Bigr]+\dots
\qquad\text{(8.12)}
```

To this order (second order in $`p_{0T}`$, first order in $`\epsilon_T`$, leading order in $`\delta p_T`$, $`\kappa_A`$, $`\kappa_B`$) the tick ratio of type $`T`$ is the function $`\nu\mapsto1+\nu^2/\bigl(2(v^T_{\max})^2\bigr)`$ of the drift speed. The two functions are equal iff their coefficients are:

```math
R_A(\nu)=R_B(\nu)\ \text{to this order}\iff v^A_{\max}=v^B_{\max}\iff\tau_A\,\kappa_A\,\sigma_{X_A}=\tau_B\,\kappa_B\,\sigma_{X_B} .
\qquad\text{(8.13)}
```

No condition arises on $`m_T`$, $`N_T`$, $`\lambda_{0T}`$, nor on $`\tau_T`$ and $`\kappa_T\sigma_{X_T}`$ separately.

*The relations (5.29).* By (5.22), $`\sin^2p_{0T}=(R_T^2-1)/\rho_T^2`$. Inserting this in (5.29) eliminates the label and gives the relation between tick ratio and drift speed of type $`T`$, at the orders of (5.29):

```math
R_T^2\bigl(1-\beta_T^2\bigr)=1+\frac{(R_T^2-1)^2}{\rho_T^2}
\quad\Longrightarrow\quad
R_T=1+\frac{\beta_T^2}2+\Bigl(\frac38+\frac1{2\rho_T^2}\Bigr)\beta_T^4+O(\beta_T^6).
\qquad\text{(8.14)}
```

(With $`r:=R_T^2-1`$ the relation reads $`r=\beta_T^2+\beta_T^2r+r^2/\rho_T^2`$; iterating, $`r=\beta_T^2+(1+\rho_T^{-2})\beta_T^4+O(\beta_T^6)`$, and $`R_T=1+\tfrac r2-\tfrac{r^2}8+\dots`$) Under (8.13), $`\beta_A=\beta_B=:\beta`$ and

```math
R_A-R_B=\frac{\beta^4}2\Bigl(\frac{\bar\mu_A^2}{\tau_A^2}-\frac{\bar\mu_B^2}{\tau_B^2}\Bigr)+O(\beta^6);\qquad
\text{(5.29) agree}\iff\text{(8.13) and }\ \frac{\bar\mu_A}{\tau_A}=\frac{\bar\mu_B}{\tau_B},\quad\bar\mu_T=m_T+\frac{\pi(N_T-1)}{N_T\lambda_{0T}} .
\qquad\text{(8.15)}
```

So the answer is **no**: under (8.13) the left sides of (5.29) have the same form, but the right sides, as functions of $`R`$ or of $`\nu`$, agree only under the additional condition in (8.15). It is independent of (8.13), because $`v^T_{\max}`$ does not contain $`m_T`$, $`N_T`$, $`\lambda_{0T}`$. The two relations (5.29) agree at order $`\beta^2`$ and differ at order $`\beta^4`$. The same additional condition makes $`v_{\rm top}`$ of (5.28) equal, since $`v^T_{\rm top}=v^T_{\max}\bigl(\sqrt{1+\rho_T^{-2}}-\rho_T^{-1}\bigr)`$. By (8.14), the leading order (8.12) is accurate for $`\beta_T^2\ll\min(1,\rho_T^2)`$.

### Step 9. Inertia, and the relation of the conditions (items 3c, 3d)

By Step 7, (6.20) holds for each body. With $`(v^T_{\max})^2=\tau_T^2\kappa_T^2\sigma_{X_T}^2`$ from (8.7), for every clock level $`k=0,\dots,N_T-1`$,

```math
I^T_k=\frac{M^T_k}{(v^T_{\max})^2},\qquad\text{that is}\qquad M^T_k=I^T_k\,(v^T_{\max})^2,\qquad M^T_k=m_T+\frac{2\pi k}{N_T\lambda_{0T}} ,
\qquad\text{(8.16)}
```

equivalently, by (6.16), $`M^T_k\,\mu^T_{\rm av}(k)=(v^T_{\max})^2\,n_T\,g(n_T,\cdot\,)`$ with $`n_T=e_T/\sigma_{X_T}`$. As an identity between the quantities defined in (6.7), (6.20) and (5.11), (8.16) is exact; that $`I^T_k`$ is the inertia of the body holds at the orders of (6.20). The relation between background inertia and rest cost is thus a proportionality with the factor $`M^T_k/I^T_k=(v^T_{\max})^2`$, the same for all levels of one type. Hence

```math
\frac{M^A_k}{I^A_k}=\frac{M^B_{k'}}{I^B_{k'}}\ \ \text{for all levels }k,k'\ (\text{equivalently, for one pair})\iff v^A_{\max}=v^B_{\max}\iff\tau_A\,\kappa_A\,\sigma_{X_A}=\tau_B\,\kappa_B\,\sigma_{X_B} .
\qquad\text{(8.17)}
```

In addition, for the label inertia $`I^{\rm lab}_k=M_k/\tau^2`$ the relation to the rest cost is the same for both types iff $`\tau_A=\tau_B`$; this coincides with (8.17) iff $`d_1^A=d_1^B`$, for example under (8.10).

*Relation of the conditions (item 3d).* Both conditions are the equality of the maximal speeds:

```math
\text{(8.13)}\iff v^A_{\max}=v^B_{\max}\iff\text{(8.17)} .
\qquad\text{(8.18)}
```

A common maximal speed is therefore necessary and sufficient for a common leading-order law $`R=1+\nu^2/(2v_{\max}^2)`$ of moving clocks (to the order stated at (8.13)) and for a common relation $`M_k=I_k\,v_{\max}^2`$ between rest cost and background inertia (exact in the sense stated at (8.16)). The reason is that the same combination $`\tau_T\kappa_T\sigma_{X_T}`$ of (5.11) appears in (5.28) and in (6.20). A common maximal speed does not imply that (5.29) agree beyond the leading order (8.15). With common points (8.10), all three conditions become $`\tau_A=\tau_B`$.

## Result

- **Item 1.** (a) All replacements: (8.1); action on the six quantities and under the phase of $`\chi`$: (8.2). (b) Well-defined quantities: (8.3); $`\bar x_a-\bar x_b`$ is not well defined. (c) Yes: the bound (8.5) holds exactly for every product start and every $`\lambda`$; $`v^A_{\max}`$ does not depend on $`C_B`$, $`K^B_k`$, $`\vartheta`$ (8.6).
- **Item 2.** (a), (b) Maximal speeds (8.7) and the conditions (8.8). (c) No (8.9). (d) A full correspondence holds iff $`\ell_B=\pm\ell_A`$, which gives equal distances of neighbouring points; then the maximal speeds are equal iff $`t_A=t_B`$, respectively $`\tau_A=\tau_B`$ (8.10).
- **Item 3.** (a) Factorization (8.11). (b) $`R_A-R_B`$ at leading order (8.12); the condition (8.13); the relation (8.14) and the answer no (8.15). (c) $`I^T_k=M^T_k/(v^T_{\max})^2`$ (8.16) and the condition (8.17). (d) Both conditions are $`v^A_{\max}=v^B_{\max}`$ (8.18).

## Consistency checks

1. **Dimensions and rescaling.** Let $`\mathsf c=[\lambda]^{-1}`$ (cost) and $`\mathsf L=[u]`$. Then $`[v_{\max}]=[\eta\,d_1]=\mathsf{cL}=[\bar x/\lambda]`$; $`\beta`$, $`\rho`$, $`R`$ are dimensionless; $`[I_k]=[M/v_{\max}^2]=\mathsf c^{-1}\mathsf L^{-2}`$, which is the inverse of $`[a/F]=\mathsf{Lc}^2/(\mathsf c/\mathsf L)`$. The rescaling $`\kappa_T\mapsto s\kappa_T`$, $`X_T\mapsto X_T/s`$ leaves the records unchanged and gives $`\sigma_{X_T}\mapsto\sigma_{X_T}/s`$: $`d_1^T`$, $`v^T_{\max}`$, $`I^T_k`$ and the conditions (8.8), (8.10), (8.13), (8.15), (8.17) are unchanged. Passed.
2. **Equal parameters and exchange of $`a`$ and $`b`$.** For equal parameters, (8.8), (8.13), (8.17) hold and (8.12), (8.15) vanish. Under $`a\leftrightarrow b`$, (8.1) goes into itself with $`Z\mapsto-Z`$, $`\alpha^A\leftrightarrow\alpha^B`$, (8.2) with $`z\mapsto-z`$; (8.12) and (8.15) change sign; (8.3) and all conditions are symmetric. Passed.
3. **Special case of (8.14).** $`\rho_T=1`$, $`\sin^2p_0=0.01`$: (5.22) gives $`R=\sqrt{1.01}=1.0049876`$, and (5.22), (5.25) give $`\beta^2=0.01\cdot0.99/1.01=0.0098020`$. The expansion (8.14) gives $`1+0.0049010+0.875\cdot0.00009608=1.0049851`$. The difference $`2.5\cdot10^{-6}`$ is of order $`\beta^6=9.4\cdot10^{-7}`$. Passed.

## Open issues

- Equality of the maximal speeds is a condition on the description (8.9); nothing in this package selects it (out of scope).
- Item 3 inherits the orders of 05-moving-clock and 06-inertia-internal-energy. Beyond leading order in $`\kappa`$ (out of scope): the influence of $`b`$ on the view of $`a`$ vanishes if $`\kappa_A=0`$ or $`\kappa_B=0`$, so it is of order $`\kappa_A\kappa_B`$; and the mean $`\langle X_T\rangle`$ can be rebooked by (8.1), with $`\alpha^T_x\propto x`$, as a uniform cost gradient on body $`T`$ of first order in $`\kappa_T`$.
- $`v^T_{\max}`$ is an upper bound. The drift speeds (5.25) of Model D do not exceed $`v^T_{\rm top}<v^T_{\max}`$, which depends on $`\rho_T`$ as well; equal $`v_{\max}`$ does not give equal $`v_{\rm top}`$ (8.15).
- Only chain types and Model D types are compared, as the question asks; other types are covered only by (8.5), (8.6) and (8.9).

## Methods used

- Linear independence of place projectors; rebooking of single-object terms (A5)
- Invariance analysis under description conventions (M6)
- Continuity equation for place weights, Cauchy–Schwarz inequality, Rayleigh bound for a symmetric matrix
- Spectrum of the path-graph adjacency matrix
- Duhamel (first-order perturbation) expansion in the record strength
- Elimination of a parameter and power-series inversion
