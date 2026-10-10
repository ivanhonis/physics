# Common maximal speed: two body types recorded by one medium

- **Subproject:** 04-ilang-time
- **Package:** 08-maximal-speed
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-10

## Changes from previous version

- **Step 7, part 3 (I1).** Withdrawn: the claim that the starts of 05 and 06 have, by their concentration near a plane-wave label, a position moment of order $`\lvert x^0_T\rvert+1/\delta p_T`$. A position moment bounded uniformly in the chain length is now a stated condition on the starts. A counterexample, a sufficient class of starts with its bound (8.27), and the procedure for all other starts are given. The order of the limits in the setup, the Result and the key result (8.23) are worded accordingly.
- **Step 9 (I2).** Withdrawn: "this needs $`\alpha^T=0`$" and "in the displayed Model D description only". The displayed description is a sufficient booking for reading $`M^T_k`$ as the rest eigenvalue, not a necessary one. The exact statements stand after (8.24) and after (8.16); the Result, the key result (8.16) and check 2 (iii) follow.
- **Own corrections of the same kind** (wording made exact, no result changed): Step 6 ("nothing follows"); Step 7, part 1 ("holds in one description only", "nothing about the spectrum"), part 3 ("grows like $`\kappa_TL_T`$") and part 4 ("every quoted result ... only", "none of the quoted formulas"); Open issues (two uses of "only").
- **Tags.** (8.1)–(8.26) keep their meaning; (8.27) is new; no tag is retired.

## Response to verification

- **I1: Accepted and fixed in Step 7, part 3.** Concentration near a plane-wave label does not bound $`\lVert\hat x_T\phi_T\rVert`$; the step gives a start for which it is infinite on $`\mathbb Z`$. The uniform bounds and the interchange of $`\kappa_T\to0`$ with $`L_T\to\infty`$ are now claimed only for starts with a position moment bounded uniformly in $`L_T`$. The $`1/\delta p_T`$ scaling is proven for a regular rescaled envelope (8.27). For all other starts the finite-size-first order is kept, and item 3 is stated in that order (Setup, order of the limits).
- **I2: Accepted and fixed in Step 9**, paragraphs after (8.24) and after (8.16), and in Step 7, part 4. $`\alpha^T=0`$ is described as sufficient, not necessary; the example of the verification is given after (8.24) and is consistency check 2 (iii). The convention-independent formulation with the branch gap is unchanged.

## Setup and assumptions

**Setting (question.md).** Objects $`a`$ (type $`A`$, places $`h\in H_A`$), $`b`$ (type $`B`$, places $`k\in H_B`$) and the medium $`c`$; the three types are pairwise different and each has one instance, so (1.11) imposes nothing. The contract is

```math
C=C_A\otimes\mathbb 1_b\otimes\mathbb 1_c+\mathbb 1_a\otimes C_B\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert_a\otimes\mathbb 1_b\otimes K^A_h+\sum_k\mathbb 1_a\otimes\lvert k\rangle\langle k\rvert_b\otimes K^B_k ,
```

with $`C_A=\sum_{h,h'}t^A_{hh'}\lvert h\rangle\langle h'\rvert`$, $`C_B=\sum_{k,k'}t^B_{kk'}\lvert k\rangle\langle k'\rvert`$, $`K^A_h`$, $`K^B_k`$ self-adjoint, no contract between $`a`$ and $`b`$, and the start $`\lvert\phi\rangle_a\otimes\lvert\vartheta\rangle_b\otimes\lvert\chi\rangle_c`$. All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.

**Quoted definitions.** $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$; $`u^A_h:=(K^A_h-\langle K^A_h\rangle)\chi`$, $`u^B_k:=(K^B_k-\langle K^B_k\rangle)\chi`$, all in $`\mathcal N=\{v:\langle\chi\vert v\rangle=0\}`$; $`g(v,w)=\mathrm{Re}\langle v\vert w\rangle`$; $`d^a_0(h,h')=\lVert u^A_h-u^A_{h'}\rVert`$, $`d^b_0(k,k')=\lVert u^B_k-u^B_{k'}\rVert`$ (16.8); $`\bar x_a=\sum_hp^a_hu^A_h`$, $`v_a=\mathrm d\bar x_a/\mathrm d\lambda`$, and likewise for $`b`$; $`a^A_{hh'}=\lvert t^A_{hh'}\rvert d^a_0(h,h')`$, $`v^A_{\max}=\varrho(a^A)`$, and likewise for $`B`$.

**Inputs.** (16.3), (16.4), (16.8), (16.11), (16.13) of 03-ilang-space/16-common-space; (17.4), (17.7), (17.15), (17.20) of 03-ilang-space/17-motion; (5.11), (5.22), (5.25), (5.28), (5.29) of 05-moving-clock; (6.7), (6.15), (6.16), (6.20) of 06-inertia-internal-energy.

**Notation of this package.** $`T\in\{A,B\}`$ labels the type; $`\phi_A:=\phi`$, $`\phi_B:=\vartheta`$. In items 2 and 3, $`e_T:=(X_T-\langle X_T\rangle)\chi`$ with $`\lVert e_T\rVert=\sigma_{X_T}>0`$. The *record step* $`\ell_T`$ and the *hop modulus* $`\eta_T`$ are: for a chain (17.20), $`\ell_T:=e_T`$ and $`\eta_T:=t_T`$; for Model D, $`\ell_T:=\kappa_Te_T`$ and $`\eta_T:=\tau_T/2`$. $`d_1^T:=\lVert\ell_T\rVert`$ is the distance of neighbouring points ($`d_1`$ of (6.20) for Model D). The *displayed Model D description* is the one of the question: $`C_T=C^{\rm D}_T:=A_T+B_T`$ and $`K^T_x=\kappa_T\,x\,X_T`$; $`\hat x_T`$ is its position label, as an operator on $`\mathcal H_T`$, and $`\lVert\hat x_T\phi_T\rVert`$ is the *position moment* of the start. In item 3: $`\rho_T:=\tau_T/\bar\mu_T`$, $`\nu`$ is the common drift speed and $`\beta_T:=\nu/v^T_{\max}`$.

**Exact statements, statements to an order, and order of the limits.**
- Exact, for every finite system (A1): Steps 1–6; in Step 7, (8.19)–(8.23); in Step 9, the identities (8.16), (8.24), (8.25) and the equivalences (8.17), (8.18), (8.26), as statements about the quantities defined there. Chains on $`\mathbb Z`$ are the limits $`L_T\to\infty`$ of open chains with $`L_T`$ positions; item 3 uses them, with $`v^T_{\max}=\tau_Td_1^T`$ (8.7). The bound (8.27) is exact for a chain on $`\mathbb Z`$.
- To an order: (8.11) (leading order in $`\kappa_A`$, $`\kappa_B`$, with the remainder (8.23)); Step 8 (in addition first order in $`\epsilon_T`$, leading order in the spread $`\delta p_T`$, expansion in small labels $`p_{0T}`$); in Step 9, only the statement that $`I^T_k`$ is the inertia (first order in the force, average over long $`\lambda`$-intervals).
- Order of the limits in item 3: (i) $`\kappa_A,\kappa_B\to0`$ at fixed $`\lambda`$, fixed starts and fixed finite $`L_T`$; (ii) $`L_T\to\infty`$; (iii) the orders of 05 and 06 in $`\epsilon_T`$, $`\delta p_T`$ and the force; (iv) last, small $`p_{0T}`$. By (8.23), (i) and (ii) commute for starts whose position moment is bounded uniformly in $`L_T`$. This is a condition on the starts; concentration near a plane-wave label does not imply it (Step 7, part 3).

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

with $`\alpha^A_h,\alpha^B_k\in\mathbb R`$ and $`Z=Z^\dagger`$ on $`\mathcal H_c`$ arbitrary. The parametrization is one-to-one: $`\alpha^A_h=t'^A_{hh}-t^A_{hh}`$, $`\alpha^B_k=t'^B_{kk}-t^B_{kk}`$ and $`Z=K'^A_h-K^A_h+\alpha^A_h\mathbb 1_c`$ are read off the replacement. For $`\alpha^A=\alpha^B=0`$, (8.1) is (16.3). The data $`\alpha^A_h=c`$, $`\alpha^B_k=-c`$, $`Z=c\,\mathbb 1_c`$ ($`c\in\mathbb R`$) leave every $`K`$ unchanged and give $`C_A\mapsto C_A+c\,\mathbb 1_a`$, $`C_B\mapsto C_B-c\,\mathbb 1_b`$: a constant moved between the two body contracts.

These are conventions of the description (A5, M6): $`Z`$ moves a single-object term of $`c`$ between the pair terms $`a`$–$`c`$ and $`b`$–$`c`$; $`\alpha^A_h`$ and $`\alpha^B_k`$ move a single-object term of a body between the two parts in which its pair term with $`c`$ is written. In particular the diagonal of a displayed body contract is fixed only up to an arbitrary real function of the place, so its spectrum is not well defined (used in Step 7).

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

A quantity is well defined (M6) iff it is invariant under both lines of (8.2), for all $`\alpha^A`$, $`\alpha^B`$, $`Z`$, $`\theta`$. Since $`\langle e^{i\theta}v\vert e^{i\theta}w\rangle=\langle v\vert w\rangle`$:

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
*Model D.* The record vector of the place $`(x,s,a)`$ is $`x\,\ell_T`$ up to a common shift. The off-diagonal entries of $`C_T`$ come from $`A_T`$, which joins $`(x,s,a)`$ to $`(x\pm1,s',a)`$, $`s'\neq s`$, with modulus $`\tau_T/2`$ and $`d_0=\kappa_T\sigma_{X_T}`$, and from $`B_T`$, which joins places with the same $`x`$, where $`d_0=0`$. So $`a^T=\frac{\tau_T}2\kappa_T\sigma_{X_T}`$ times the adjacency matrix of $`2N_T`$ disjoint paths with $`L_T`$ vertices; $`m_T`$, $`N_T`$, $`\lambda_{0T}`$ do not enter. In both families, exactly,

```math
v^T_{\max}=2\,\eta_T\,d_1^T\cos\frac{\pi}{L_T+1}\ \xrightarrow[L_T\to\infty]{}\ 2\,\eta_T\,d_1^T=
\begin{cases}2\,t_T\,\sigma_{X_T}&\text{chain, (17.20)},\\ \tau_T\,\kappa_T\,\sigma_{X_T}&\text{Model D, (5.11)}.\end{cases}
\qquad\text{(8.7)}
```

Hence, for chains on $`\mathbb Z`$ and for finite chains with $`L_A=L_B\ge2`$, exactly,

```math
\text{(a) chains: } v^A_{\max}=v^B_{\max}\iff t_A\,\sigma_{X_A}=t_B\,\sigma_{X_B};\qquad
\text{(b) Model D: } v^A_{\max}=v^B_{\max}\iff\tau_A\,\kappa_A\,\sigma_{X_A}=\tau_B\,\kappa_B\,\sigma_{X_B}.
\qquad\text{(8.8)}
```

For finite chains in general the exact condition is $`\eta_Ad_1^A\cos\frac{\pi}{L_A+1}=\eta_Bd_1^B\cos\frac{\pi}{L_B+1}`$; for $`L_A=L_B=1`$ both maximal speeds vanish, whatever the parameters.

### Step 5. The language does not imply equal maximal speeds (item 2c)

**No.** Take two open chains with the same $`L\ge2`$, $`X_A=X_B=X`$ with $`\sigma_X>0`$, and $`t_A=r\,t_B`$, $`r>0`$. This is an admissible description: finitely many objects and places (A1); $`C`$ self-adjoint and independent of $`\lambda`$, a sum of the pair terms $`a`$–$`c`$ and $`b`$–$`c`$ (Laws 3, 4, A5); a unit product start (A3); no identical instances, so Law 5 and A6 impose nothing; Laws 1, 2 and A2, A4, A7–A9 do not restrict the contract. By (8.7),

```math
\frac{v^A_{\max}}{v^B_{\max}}=\frac{t_A\,\sigma_{X_A}}{t_B\,\sigma_{X_B}}=r\qquad\text{takes every value in }(0,\infty).
\qquad\text{(8.9)}
```

In general, multiplying the off-diagonal entries $`t^A_{hh'}`$, $`h\neq h'`$, by $`s>0`$ maps admissible descriptions to admissible descriptions, multiplies $`v^A_{\max}`$ by $`s`$ and leaves $`v^B_{\max}`$ unchanged, by (8.6). Equality of the maximal speeds is a condition on the description.

### Step 6. Common points (item 2d)

Let both chains have $`L`$ positions, with labels $`j_T,\dots,j_T+L-1`$. Positions are the points: places at one position have $`d_0=0`$, different positions have $`d_0=\lvert x-x'\rvert d_1^T>0`$. So $`\lvert X_A\rvert=\lvert X_B\rvert=L`$ and $`U_T-\bar u^T=\{(j-\tfrac{L-1}2)\ell_T:\ j=0,\dots,L-1\}`$. By (16.13), a correspondence with $`D_A=X_A`$, $`D_B=X_B`$ exists iff $`L\ge2`$ and these two centred sets are equal. Their elements of largest norm are $`\pm\tfrac{L-1}2\ell_T`$, so equality forces $`\ell_B=\pm\ell_A`$; conversely $`\ell_B=\pm\ell_A`$ gives equal sets. Therefore, exactly, for every $`L\ge2`$,

```math
\text{full correspondence}\iff\ell_B=\pm\ell_A\ \Longrightarrow\ d_1^A=d_1^B;\qquad\text{then}\quad v^A_{\max}=v^B_{\max}\iff\eta_A=\eta_B .
\qquad\text{(8.10)}
```

- Records: the two types have the same record vectors up to one translation $`t_\pi\in\mathcal N`$ (16.11), which the replacement (8.1) with $`z=t_\pi/2`$ removes; neighbouring points are equally far apart for both types. For chains: $`(X_B-\langle X_B\rangle)\chi=\pm(X_A-\langle X_A\rangle)\chi`$, hence $`\sigma_{X_A}=\sigma_{X_B}`$. For Model D: $`\kappa_B(X_B-\langle X_B\rangle)\chi=\pm\kappa_A(X_A-\langle X_A\rangle)\chi`$, hence $`\kappa_A\sigma_{X_A}=\kappa_B\sigma_{X_B}`$. Since the first statement of (8.10) is an equivalence, nothing else follows: $`\kappa_T`$ and $`X_T`$ are restricted through $`\ell_T`$ alone, and $`t_T`$, $`\tau_T`$, $`m_T`$, $`N_T`$, $`\lambda_{0T}`$ not at all.
- Condition: by (8.7) with equal $`L`$ and equal $`d_1^T`$, $`v^A_{\max}=v^B_{\max}`$ iff $`t_A=t_B`$ (chains), iff $`\tau_A=\tau_B`$ (Model D). Common points remove the records from the condition (8.8) and leave the hopping.

### Step 7. Effective body contracts; why the one-body results apply (item 3a)

**1. A convention-independent split (exact; setting of item 1).** By (8.1), a displayed body contract is fixed only up to $`\mathrm{diag}(\alpha^T)`$ and the record operators only up to scalars. A statement about the spectrum of a displayed $`C_T`$, or about record terms "of first order in $`\kappa`$", therefore depends on the booking: it can hold in one description and fail in another. Take instead the partial expectation of $`C`$ in the medium start. Because there is no contract between $`a`$ and $`b`$, it is a sum of two one-body operators, the **effective body contracts**:

```math
C^{\rm eff}_A\otimes\mathbb 1_b+\mathbb 1_a\otimes C^{\rm eff}_B:=(\mathbb 1_{ab}\otimes\langle\chi\rvert)\,C\,(\mathbb 1_{ab}\otimes\lvert\chi\rangle),\qquad
C^{\rm eff}_A=C_A+\sum_h\langle K^A_h\rangle\lvert h\rangle\langle h\rvert,\quad
C^{\rm eff}_B=C_B+\sum_k\langle K^B_k\rangle\lvert k\rangle\langle k\rvert .
\qquad\text{(8.19)}
```

The left side is built from $`C`$ and $`\chi`$ alone, and its split into two one-body operators is unique up to a constant. Indeed, by (8.1) the $`\alpha`$'s cancel in $`t'_{hh}+\langle K'_h\rangle`$, and

```math
\text{(8.1):}\quad C^{\rm eff}_A\mapsto C^{\rm eff}_A+\langle Z\rangle\,\mathbb 1_a,\quad C^{\rm eff}_B\mapsto C^{\rm eff}_B-\langle Z\rangle\,\mathbb 1_b;\qquad \chi\mapsto e^{i\theta}\chi:\quad C^{\rm eff}_A,\ C^{\rm eff}_B\ \text{unchanged}.
\qquad\text{(8.20)}
```

Hence, for one type, the eigenvectors of $`C^{\rm eff}_T`$ and the differences of its eigenvalues are well defined (M6), and so is the sum of an eigenvalue of $`C^{\rm eff}_A`$ and one of $`C^{\rm eff}_B`$. A single eigenvalue of $`C^{\rm eff}_T`$ is not. Of a displayed $`C_T`$ with at least two places, neither the eigenvalues nor the spectral width are: the largest and the smallest eigenvalue enclose every diagonal entry, and (8.1) makes the difference of two diagonal entries arbitrary. By (1.8) the cost of the start is $`L=\langle\phi\vert C^{\rm eff}_A\vert\phi\rangle+\langle\vartheta\vert C^{\rm eff}_B\vert\vartheta\rangle`$ exactly: $`C^{\rm eff}_T`$ gives body $`T`$ its share of the cost, fixed up to the constant.

The rest, $`\hat C_{\rm rec}:=C-C^{\rm eff}_A-C^{\rm eff}_B`$ (identities suppressed), is invariant under (8.1). It has $`K-\langle K\rangle`$ in place of the $`K`$'s, so $`\hat C_{\rm rec}(\phi'\otimes\vartheta'\otimes\chi)=\sum_{h,k}\phi'_h\vartheta'_k\lvert hk\rangle\otimes(u^A_h+u^B_k)`$. Let $`\phi(s):=e^{-iC^{\rm eff}_As}\phi`$ and $`\vartheta(s):=e^{-iC^{\rm eff}_Bs}\vartheta`$; the two effective contracts act on different factors and commute. Duhamel's formula $`e^{-iC\lambda}=e^{-iC_0\lambda}-i\int_0^\lambda e^{-iC(\lambda-s)}\hat C_{\rm rec}\,e^{-iC_0s}\,\mathrm ds`$ with $`C_0:=C-\hat C_{\rm rec}`$, the unitarity of $`e^{-iC(\lambda-s)}`$ and the orthonormality of the $`\lvert hk\rangle`$ give, for $`\lambda\ge0`$,

```math
\bigl\lVert\Psi(\lambda)-\phi(\lambda)\otimes\vartheta(\lambda)\otimes\chi\bigr\rVert\le\varsigma(\lambda):=\int_0^\lambda\Bigl(\sum_{h,k}\lvert\phi_h(s)\rvert^2\,\lvert\vartheta_k(s)\rvert^2\,\lVert u^A_h+u^B_k\rVert^2\Bigr)^{1/2}\mathrm ds,
\qquad
\bigl\lVert V_a(\lambda)-\lvert\phi(\lambda)\rangle\langle\phi(\lambda)\rvert\bigr\rVert_1\le2\,\varsigma(\lambda),
\qquad\text{(8.21)}
```

and likewise for $`V_b`$. The second bound holds because the partial trace does not increase the trace norm and $`\lVert\,\lvert\psi\rangle\langle\psi\rvert-\lvert\psi'\rangle\langle\psi'\rvert\,\rVert_1\le2\lVert\psi-\psi'\rVert`$. (8.21) is exact, for every description of item 1, every product start and every finite size. $`\varsigma`$ is invariant under (8.1), because $`z`$ cancels in $`u^A_h+u^B_k`$ and (8.20) changes $`\phi(s)`$, $`\vartheta(s)`$ by phases, and under the phase of $`\chi`$. The convention-independent form of the weak-record regime is $`\varsigma(\lambda)\ll1`$: the view of each body is then the one generated by its own effective body contract.

**2. Model D types.** In the displayed description, (8.19) gives $`C^{\rm eff}_T=C^{\rm D}_T+\kappa_T\langle X_T\rangle\hat x_T`$. By (8.20), in every description of the family (8.1),

```math
C^{\rm eff}_T=C^{\rm D}_T+\gamma_T\,\hat x_T+c_T\,\mathbb 1,\qquad\gamma_T:=\kappa_T\langle X_T\rangle,\qquad c_A=-c_B=\langle Z\rangle .
\qquad\text{(8.22)}
```

$`C^{\rm D}_T+c_T\mathbb 1`$ is the part of $`C^{\rm eff}_T`$ that commutes with the translations of the position label, and $`\gamma_T\hat x_T`$ is a uniform cost gradient of first order in $`\kappa_T`$, of the kind treated in 06. The displayed body contract of a rebooked description is $`C^{\rm D}_T+\mathrm{diag}(\alpha^T)`$ instead, and its records contain the scalars $`-\alpha^T_h`$ at zeroth order in $`\kappa_T`$; (8.19) puts them back. A cost gradient with a force $`F`$, as in 06, is a further diagonal term of $`C^{\rm eff}_T`$ and is included in $`C^{\rm D}_T`$ below.

The record vectors are $`u^T_{(x,s,a)}=x\,\ell_T`$ in the displayed description, so $`\lVert u^A_h+u^B_k\rVert\le d_1^A\lvert x_a\rvert+d_1^B\lvert x_b\rvert`$. All diagonal terms commute with $`\hat x_T`$, so $`[C^{\rm eff}_T,\hat x_T]=[A_T,\hat x_T]`$, of norm $`\tau_T\cos\frac{\pi}{L_T+1}\le\tau_T`$; hence $`\lVert\hat x_T\phi_T(s)\rVert\le\lVert\hat x_T\phi_T\rVert+\tau_Ts`$. With the Minkowski inequality in (8.21), and with Duhamel's formula once more for $`C^{\rm eff}_T`$ against $`C^{\rm D}_T+c_T\mathbb 1`$ (the phases cancel, $`c_A+c_B=0`$):

```math
\varsigma(\lambda)\le\sum_{T}d_1^T\,\Lambda_T(\lambda),\qquad
\Bigl\lVert\Psi(\lambda)-e^{-iC^{\rm D}_A\lambda}\phi\otimes e^{-iC^{\rm D}_B\lambda}\vartheta\otimes\chi\Bigr\rVert\le\sum_{T}\bigl(d_1^T+\lvert\gamma_T\rvert\bigr)\Lambda_T(\lambda),\qquad
\Lambda_T(\lambda):=\lambda\,\lVert\hat x_T\phi_T\rVert+\tfrac12\tau_T\lambda^2 .
\qquad\text{(8.23)}
```

Both bounds are exact. Since $`d_1^T+\lvert\gamma_T\rvert=\kappa_T(\sigma_{X_T}+\lvert\langle X_T\rangle\rvert)`$, they give

```math
\lvert\Psi(\lambda)\rangle=e^{-iC^{\rm D}_A\lambda}\lvert\phi\rangle\otimes e^{-iC^{\rm D}_B\lambda}\lvert\vartheta\rangle\otimes\lvert\chi\rangle+O(\kappa_A)+O(\kappa_B),\qquad
V_a(\lambda)=e^{-iC^{\rm D}_A\lambda}\lvert\phi\rangle\langle\phi\rvert e^{iC^{\rm D}_A\lambda}+O(\kappa_A)+O(\kappa_B),
\qquad\text{(8.11)}
```

and likewise for $`V_b`$, with the remainders bounded by (8.23) and twice (8.23). In the same way $`[C,\hat x_T]=[A_T,\hat x_T]`$ gives $`\lVert\hat x_T\Psi(\lambda)\rVert\le\lVert\hat x_T\phi_T\rVert+\tau_T\lambda`$, so the mean position label differs from its leading-order value by at most $`2(\lVert\hat x_T\phi_T\rVert+\tau_T\lambda)`$ times the right side of (8.23).

**3. Uniformity and order of the limits.** The right sides of (8.23) contain $`L_A`$, $`L_B`$ only through the position moments $`\lVert\hat x_T\phi_T\rVert`$ of the starts. The weak-record regime for both bodies is $`(d_1^T+\lvert\gamma_T\rvert)\Lambda_T(\lambda)\ll1`$ for $`T=A,B`$. For starts with $`\lVert\hat x_T\phi_T\rVert`$ bounded uniformly in $`L_T`$, the limits $`\kappa_T\to0`$ and $`L_T\to\infty`$ therefore commute.

This is a condition on the starts. The quoted inputs specify the starts of 05 and 06 as concentrated near a plane-wave label, in a given branch and with a given clock label; this does not bound the position moment. Example: plane-wave amplitudes that are constant for $`\lvert p-p_{0T}\rvert\le\delta p_T`$ and zero elsewhere give, on $`\mathbb Z`$, $`\phi_x\propto e^{ip_{0T}x}\sin(\delta p_T\,x)/x`$, for which $`\sum_xx^2\lvert\phi_x\rvert^2=\infty`$. A sufficient class is the following. On $`\mathbb Z`$ write $`\phi_{T,(x,s,a)}=(2\pi)^{-1/2}\int_{-\pi}^{\pi}e^{ipx}\,\tilde\phi_{T,sa}(p)\,\mathrm dp`$. For $`\tilde\phi_T`$ periodic and absolutely continuous, integration by parts and Parseval's identity give $`\lVert\hat x_T\phi_T\rVert=\lVert\mathrm d\tilde\phi_T/\mathrm dp\rVert_{L^2}`$. Let

```math
\tilde\phi_T(p)=e^{-ipx^0_T}\,\delta p_T^{-1/2}\,f\Bigl(\frac{p-p_{0T}}{\delta p_T}\Bigr)\,\xi_T(p)
\quad\Longrightarrow\quad
\lVert\hat x_T\phi_T\rVert\le\lvert x^0_T\rvert+\frac{\lVert f'\rVert_{L^2}}{\delta p_T}+c_\xi ,
\qquad\text{(8.27)}
```

where $`f`$ is a fixed envelope of compact support with $`\int\lvert f\rvert^2=1`$ and $`\int\lvert f'\rvert^2<\infty`$, $`\delta p_T`$ is small enough for the support to lie inside one period, and $`\xi_T(p)`$ is a unit internal vector (branch and clock labels) with $`\lVert\mathrm d\xi_T/\mathrm dp\rVert\le c_\xi`$. The bound follows from the product rule and the triangle inequality. For the upper-branch vectors of $`C^{\rm D}_T`$, taken with real components, $`c_\xi=\tau_T/(2m_T)`$ suffices, the branch gap being at least $`2m_T>0`$. The normalized truncations of such a start to the finite chains have position moments at most $`\lVert\hat x_T\phi_T\rVert/\lVert P_{L_T}\phi_T\rVert`$, where $`P_{L_T}`$ is the projector onto the positions of the chain and commutes with $`\hat x_T`$; these are bounded uniformly for large $`L_T`$.

Because the bound (8.27) grows as $`\delta p_T\to0`$ and $`\Lambda_T`$ grows with $`\lambda`$, the limit $`\kappa_T\to0`$ is taken first, at fixed $`\delta p_T`$ and fixed $`\lambda`$ (a tick, or an averaging interval). For a start whose position moment is not bounded uniformly in $`L_T`$, (8.21) and (8.23) still hold at every finite $`L_T`$, where $`\lVert\hat x_T\phi_T\rVert`$ is at most the largest $`\lvert x\rvert`$ of the chain. (8.23) then does not justify the interchange of the limits, and they are taken in the order of the setup: $`\kappa_T\to0`$ at fixed finite $`L_T`$, before $`L_T\to\infty`$. In that order the statements of part 4 hold for every start.

**4. Application to each body, and well-defined quantities.**
- By (8.11) the leading-order view of each body is the one generated by its own contract $`C^{\rm D}_T`$ and its own start. The other body, its contract, its records and its start do not enter. The one-body setting of 05 and 06 is the same argument with the other body removed, and it has the same effective contract (8.22).
- By (8.6) the differences $`x\,\ell_T`$ of the record vectors of a body, hence the background (17.15) in which its position is measured, depend only on its own records and on $`\chi`$.
- The quoted results of 05 and 06 on the motion of a body and of its clock, (5.22)–(5.29) and (6.15)–(6.20), are statements about these two things, expressed through the parameters of $`C^{\rm D}_T`$ and of the records: the place weights of the view of the body (position, branch and clock labels) and the differences of its record vectors. (5.11) is (8.7), and (6.7) is a statement about $`C^{\rm D}_T`$ (Step 9).

Hence (5.11)–(5.29) and (6.7)–(6.20) hold for $`a`$ with the parameters of type $`A`$ and for $`b`$ with those of type $`B`$, with "$`O(\kappa)`$" bounded by (8.23).

Under the whole family (8.1) and the phase of $`\chi`$, the following are invariant: the starts and the views, hence the ticks and $`R_T`$ (functions of the clock-label weights of the view); $`\lVert\bar v_T\rVert`$, by (8.2); $`v^T_{\max}`$; the parameters $`\tau_T`$, $`N_T`$, $`\lambda_{0T}`$ (off-diagonal entries of $`C_T`$), $`\bar\mu_T`$ and $`m_T`$ (half the difference of the diagonal entries of $`C^{\rm eff}_T`$ at $`s=1`$ and $`s=2`$, at equal $`x`$ and $`a`$, is $`\bar\mu_T`$), $`d_1^T`$ and $`\gamma_T`$; hence $`\rho_T`$ and $`\epsilon_T`$. "The branch of positive eigenvalue" of 05 and 06 is the upper branch of $`C^{\rm D}_T+c_T\mathbb 1`$. Not invariant are the diagonal, the eigenvalues and the spectral width of a displayed $`C_T`$, and the eigenvalues of $`C^{\rm eff}_T`$ (8.20). The parameters $`m_T`$, $`\bar\mu_T`$ and $`M^T_k`$ of the quoted formulas are therefore read off $`C^{\rm eff}_T`$ as above; read off the displayed body contract of a rebooked description, they can come out different (check 2).

### Step 8. Moving clocks (item 3b)

Let $`\nu:=\lVert\bar v_a\rVert=\lVert\bar v_b\rVert`$ for the drift velocities (5.25) of the two clock-carrying starts. By Step 7, (5.28) holds for each type with its own $`v^T_{\max}`$ of (8.7): $`R_T=1+\nu^2/\bigl(2(v^T_{\max})^2\bigr)+O(p_{0T}^4)`$. By (5.22) and (5.25), $`\beta_T^2=\rho_T^2p_{0T}^2+O(p_{0T}^4)`$, so the two labels are small together. Subtracting,

```math
R_A-R_B=\frac{\nu^2}2\Bigl[\frac1{(v^A_{\max})^2}-\frac1{(v^B_{\max})^2}\Bigr]+O(p_{0A}^4)+O(p_{0B}^4)
=\frac{\nu^2}2\Bigl[\frac1{\tau_A^2\kappa_A^2\sigma_{X_A}^2}-\frac1{\tau_B^2\kappa_B^2\sigma_{X_B}^2}\Bigr]+\dots
\qquad\text{(8.12)}
```

To this order (second order in $`p_{0T}`$, first order in $`\epsilon_T`$, leading order in $`\delta p_T`$, $`\kappa_A`$, $`\kappa_B`$, in the order of limits of the setup) the tick ratio of type $`T`$ is the function $`\nu\mapsto1+\nu^2/\bigl(2(v^T_{\max})^2\bigr)`$ of the drift speed. The two functions are equal iff their coefficients are:

```math
R_A(\nu)=R_B(\nu)\ \text{to this order}\iff v^A_{\max}=v^B_{\max}\iff\tau_A\,\kappa_A\,\sigma_{X_A}=\tau_B\,\kappa_B\,\sigma_{X_B} .
\qquad\text{(8.13)}
```

No condition arises on $`m_T`$, $`N_T`$, $`\lambda_{0T}`$, nor on $`\tau_T`$ and $`\kappa_T\sigma_{X_T}`$ separately. Both sides of (8.12) and the condition (8.13) contain only quantities that are invariant by Step 7, part 4.

*The relations (5.29).* By (5.22), $`\sin^2p_{0T}=(R_T^2-1)/\rho_T^2`$. Inserting this in (5.29) eliminates the label and gives the relation between tick ratio and drift speed of type $`T`$, at the orders of (5.29); on the branch with $`R_T\to1`$ for $`\beta_T\to0`$ (small labels) it is solved by the series on the right:

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

"Agree" means that the relation (8.14) between $`R`$ and $`\nu`$ is the same for both types. The equivalence follows from the coefficients of $`\nu^2`$ and $`\nu^4`$ in (8.14), since $`\rho_T>0`$. So the answer is **no**: under (8.13) the left sides of (5.29) have the same form, but the right sides agree only under the additional condition in (8.15). It is independent of (8.13), because $`v^T_{\max}`$ does not contain $`m_T`$, $`N_T`$, $`\lambda_{0T}`$. The two relations agree at order $`\beta^2`$ and differ at order $`\beta^4`$. Since (5.22) holds to first order in $`\epsilon_T`$, the additional condition is fixed up to relative terms $`O((N_T\epsilon_T)^2)`$; at zeroth order it reads $`m_A/\tau_A=m_B/\tau_B`$. The same condition makes $`v_{\rm top}`$ of (5.28) equal, since $`v^T_{\rm top}=v^T_{\max}\bigl(\sqrt{1+\rho_T^{-2}}-\rho_T^{-1}\bigr)`$. By (8.14), the leading order (8.12) is accurate for $`\beta_T^2\ll\min(1,\rho_T^2)`$.

### Step 9. Inertia, and the relation of the conditions (items 3c, 3d)

*Which rest cost is well defined.* By (8.22), on the plane wave with label $`0`$ and clock level $`k`$, the translation-invariant part $`C^{\rm D}_T+c_T\mathbb 1`$ of the effective body contract has the two eigenvalues

```math
E^T_{k,\pm}=c_T\pm M^T_k,\qquad M^T_k:=m_T+\frac{2\pi k}{N_T\lambda_{0T}},\qquad\Delta^T_k:=E^T_{k,+}-E^T_{k,-}=2M^T_k ,
\qquad\text{(8.24)}
```

with $`c_A=-c_B=\langle Z\rangle`$ an arbitrary real number. By (8.20), well defined are the branch gap $`\Delta^T_k`$, the level differences $`E^T_{k,+}-E^T_{k',+}=M^T_k-M^T_{k'}`$, and the sum $`E^A_{k,+}+E^B_{k',+}`$. The rest cost $`E^T_{k,+}`$ itself is not. So whether the rest cost of (6.7), "the positive eigenvalue of the body contract", is the number $`M^T_k`$ depends on the booking:
- For the effective body contract, $`E^T_{k,+}=M^T_k`$ iff $`c_T=0`$, that is iff $`\langle Z\rangle=0`$.
- For a displayed body contract $`C^{\rm D}_T+\mathrm{diag}(\alpha^T)`$, the booking $`\alpha^T=0`$ of the displayed Model D description is sufficient, and it is not necessary. For example, $`\alpha^T_{(x,s,a)}=\delta\,\delta_{s2}`$ with $`0<\delta<m_T`$ gives, at label $`0`$ and level $`k`$, the eigenvalues $`M^T_k`$ and $`-M^T_k+\delta<0`$: the positive eigenvalue is still $`M^T_k`$, for every $`k`$. In contrast, $`\alpha^T_{(x,s,a)}=\delta\,(\sigma_3)_{ss}`$ with $`\delta>-m_T`$, $`\delta\neq0`$, gives $`\pm(M^T_k+\delta)`$ (check 2). The set of all $`\alpha^T`$ that keep the eigenvalue is not determined here; it is not used.

What is well defined is $`M^T_k`$ as half the branch gap. That is the quantity 06 uses: by (6.7) and (6.15), $`\mu^T_{\rm av}(k)=\omega_k''(0)\,\ell_T\,g(\ell_T,\cdot\,)`$ with $`\omega_k''(0)=\tau_T^2/M^T_k=2\tau_T^2/\Delta^T_k`$, the curvature of the upper branch, which does not change with $`c_T`$. Hence $`I^T_k`$ is well defined, and by Step 7 (6.20) holds for each body.

*The relation.* With $`(v^T_{\max})^2=\tau_T^2\kappa_T^2\sigma_{X_T}^2`$ from (8.7), for every clock level $`k=0,\dots,N_T-1`$,

```math
I^T_k=\frac{M^T_k}{(v^T_{\max})^2},\qquad\text{that is}\qquad M^T_k=I^T_k\,(v^T_{\max})^2,\qquad M^T_k=m_T+\frac{2\pi k}{N_T\lambda_{0T}} ,
\qquad\text{(8.16)}
```

equivalently, by (6.16), $`M^T_k\,\mu^T_{\rm av}(k)=(v^T_{\max})^2\,n_T\,g(n_T,\cdot\,)`$ with $`n_T=e_T/\sigma_{X_T}`$. (8.16) is an exact identity between the quantities defined in (6.7), (6.20) and (5.11). Read with $`M^T_k=\Delta^T_k/2`$, it holds in every description of the family (8.1). Read with $`M^T_k`$ as the rest cost, the positive eigenvalue of a body contract at label $`0`$ and level $`k`$, it holds in a description iff that eigenvalue equals $`M^T_k`$ there, because $`I^T_k`$ and $`v^T_{\max}`$ are invariant. This is the case **in the displayed Model D description**; for the effective body contract iff $`\langle Z\rangle=0`$; and for a rebooked displayed contract in some cases and not in others (the two examples after (8.24)). That $`I^T_k`$ is the inertia of the body holds at the orders of (6.20). The convention-independent relations between background inertia and rest cost are, exactly,

```math
\Delta^T_k=2\,I^T_k\,(v^T_{\max})^2,\qquad E^T_{k,+}-E^T_{k',+}=\bigl(I^T_k-I^T_{k'}\bigr)(v^T_{\max})^2;\qquad\text{whereas}\quad E^T_{k,+}=c_T+I^T_k\,(v^T_{\max})^2 .
\qquad\text{(8.25)}
```

The first two contain only well-defined quantities. The third shows that the relation between the rest cost and the background inertia is affine, with the well-defined slope $`(v^T_{\max})^2`$ and the conventional intercept $`c_T`$. A proportionality of rest cost and inertia is a property of the bookings with $`\langle Z\rangle=0`$, not of the system.

*The condition.* The factor $`M^T_k/I^T_k=(v^T_{\max})^2`$ is the same for all levels of one type. Hence, with $`M^T_k=\Delta^T_k/2`$,

```math
\frac{M^A_k}{I^A_k}=\frac{M^B_{k'}}{I^B_{k'}}\ \ \text{for all levels }k,k'\ (\text{equivalently, for one pair})\iff v^A_{\max}=v^B_{\max}\iff\tau_A\,\kappa_A\,\sigma_{X_A}=\tau_B\,\kappa_B\,\sigma_{X_B} .
\qquad\text{(8.17)}
```

In convention-independent form, for two Model D types in every description of the family (8.1), and with the second statement for $`N_A,N_B\ge2`$:

```math
\frac{\Delta^A_k}{I^A_k}=\frac{\Delta^B_{k'}}{I^B_{k'}}\ \ \forall k,k'
\iff
\frac{E^A_{k,+}-E^A_{l,+}}{I^A_k-I^A_l}=\frac{E^B_{k',+}-E^B_{l',+}}{I^B_{k'}-I^B_{l'}}\ \ \forall k\neq l,\ k'\neq l'
\iff v^A_{\max}=v^B_{\max} .
\qquad\text{(8.26)}
```

The affine relations $`E_+=c_T+I\,(v^T_{\max})^2`$ of the two types coincide iff $`v^A_{\max}=v^B_{\max}`$ and $`c_A=c_B`$, that is $`\langle Z\rangle=0`$. The second requirement is a convention and not a condition on the types. In addition, for the label inertia $`I^{\rm lab}_k=M_k/\tau^2`$ the relation to $`M_k=\Delta_k/2`$ is the same for both types iff $`\tau_A=\tau_B`$; this coincides with (8.17) iff $`d_1^A=d_1^B`$, for example under (8.10).

*Relation of the conditions (item 3d).* Both conditions are the equality of the maximal speeds:

```math
\text{(8.13)}\iff v^A_{\max}=v^B_{\max}\iff\text{(8.17)}\iff\text{(8.26)} .
\qquad\text{(8.18)}
```

A common maximal speed is therefore necessary and sufficient for a common leading-order law $`R=1+\nu^2/(2v_{\max}^2)`$ of moving clocks (to the order stated at (8.13)), and for a common relation $`\Delta_k=2I_k\,v_{\max}^2`$ between branch gap and background inertia, equivalently a common slope $`v_{\max}^2`$ of rest cost against inertia (exact in the sense stated at (8.25)). The reason is that the same combination $`\tau_T\kappa_T\sigma_{X_T}`$ of (5.11) appears in (5.28) and in (6.20). A common maximal speed does not imply that (5.29) agree beyond the leading order (8.15). With common points (8.10), all these conditions become $`\tau_A=\tau_B`$.

## Result

- **Item 1.** (a) All replacements: (8.1), parametrized one-to-one; action on the six quantities and under the phase of $`\chi`$: (8.2). (b) Well-defined quantities: (8.3); $`\bar x_a-\bar x_b`$ is not well defined. (c) Yes: the bound (8.5) holds exactly for every product start and every $`\lambda`$; $`v^A_{\max}`$ does not depend on $`C_B`$, $`K^B_k`$, $`\vartheta`$ (8.6).
- **Item 2.** (a), (b) Maximal speeds (8.7) and the conditions (8.8). (c) No (8.9). (d) A full correspondence holds iff $`\ell_B=\pm\ell_A`$, which gives equal distances of neighbouring points; then the maximal speeds are equal iff $`t_A=t_B`$, respectively $`\tau_A=\tau_B`$ (8.10).
- **Item 3.** (a) Effective body contracts (8.19) and their transformation (8.20); the exact bound (8.21); for Model D the form (8.22), the bounds (8.23), which are uniform in the chain length for starts with a uniformly bounded position moment (a sufficient class: (8.27)), and the factorization (8.11). (b) $`R_A-R_B`$ at leading order (8.12); the condition (8.13); the relation (8.14) and the answer no (8.15). (c) $`I^T_k=M^T_k/(v^T_{\max})^2`$ (8.16), where $`M^T_k`$ is half the branch gap in every description of the family (8.1) and the rest eigenvalue in the displayed description, a sufficient booking and not a necessary one; the condition (8.17); the rest eigenvalues and the branch gap (8.24); the convention-independent relations (8.25) and condition (8.26). (d) All conditions are $`v^A_{\max}=v^B_{\max}`$ (8.18).

## Consistency checks

1. **Dimensions and rescaling.** Let $`\mathsf c=[\lambda]^{-1}`$, the dimension of a cost. Then $`t`$, $`\tau`$, $`m`$, $`M`$, $`E`$, $`\Delta`$, $`\gamma`$, $`K`$ and, because $`u=(K-\langle K\rangle)\chi`$, the record vectors and $`d_1`$ have dimension $`\mathsf c`$. So $`[v_{\max}]=[\eta\,d_1]=\mathsf c^2=[\bar x/\lambda]`$; $`\varsigma`$, $`d_1\Lambda`$, $`\beta`$, $`\rho`$, $`R`$ are dimensionless; $`[I_k]=[M/v_{\max}^2]=\mathsf c^{-3}`$, the inverse of $`[a/F]=\mathsf c^3`$ ($`g(u,F)`$ is a cost, so $`F`$ is dimensionless); in (8.25), $`\mathsf c=\mathsf c^{-3}\mathsf c^{4}`$. The rescaling $`\kappa_T\mapsto s\kappa_T`$, $`X_T\mapsto X_T/s`$ leaves the records unchanged and gives $`\sigma_{X_T}\mapsto\sigma_{X_T}/s`$, $`\langle X_T\rangle\mapsto\langle X_T\rangle/s`$: $`d_1^T`$, $`\gamma_T`$, $`v^T_{\max}`$, $`I^T_k`$, the bounds (8.23) and the conditions (8.8), (8.10), (8.13), (8.15), (8.17), (8.26) are unchanged. Passed.
2. **The rebookings of the two verification rounds.** (i) $`\alpha^A_{(x,s,a)}=\delta\,(\sigma_3)_{ss}`$, $`\alpha^B=0`$, $`Z=0`$: the displayed contract becomes $`C^{\rm D}_A+\delta\,\sigma_3\otimes\mathbb 1_N`$, with half-gap $`M^A_k+\delta`$ at label $`0`$, and $`\langle K'^A_h\rangle=\gamma_Ax-\delta(\sigma_3)_{ss}`$. (8.19) gives $`C^{\rm eff}_A=C^{\rm D}_A+\gamma_A\hat x_A`$, unchanged, as (8.20) states for $`\langle Z\rangle=0`$; so $`\Delta^A_k`$, $`I^A_k`$ and (8.25) are unchanged, while the half-gap of the displayed contract is not. (ii) $`\alpha^A=c`$, $`\alpha^B=-c`$, $`Z=c\,\mathbb 1_c`$: $`E^A_{k,+}=M^A_k+c`$ and $`E^B_{k',+}=M^B_{k'}-c`$; gaps, level differences and the sum are unchanged, and the proportionality $`E_+=I\,v_{\max}^2`$ is lost. (iii) $`\alpha^A_{(x,s,a)}=\delta\,\delta_{s2}`$ with $`0<\delta<m_A`$, $`\alpha^B=0`$, $`Z=0`$: at label $`0`$ and level $`k`$ the displayed contract is $`\mathrm{diag}(M^A_k,\,-M^A_k+\delta)`$ in the branch label; its positive eigenvalue is still $`M^A_k`$ although $`\alpha^A\neq0`$, its gap is $`2M^A_k-\delta`$, and $`C^{\rm eff}_A`$, $`\Delta^A_k`$ and (8.25) are unchanged. Under $`a\leftrightarrow b`$: $`Z\mapsto-Z`$, $`c_A\leftrightarrow c_B`$, and all conditions are symmetric. Passed.
3. **Equal parameters, and a special case of (8.14).** For equal parameters, (8.8), (8.13), (8.17), (8.26) hold and (8.12), (8.15) vanish. For $`\rho_T=1`$, $`\sin^2p_0=0.01`$: (5.22) gives $`R=\sqrt{1.01}=1.0049876`$, and (5.22), (5.25) give $`\beta^2=0.01\cdot0.99/1.01=0.0098020`$. The expansion (8.14) gives $`1+0.0049010+0.875\cdot0.00009608=1.0049851`$. The difference $`2.5\cdot10^{-6}`$ is of order $`\beta^6=9.4\cdot10^{-7}`$. Passed.

## Open issues

- Equality of the maximal speeds is a condition on the description (8.9); nothing in this package selects it (out of scope).
- The rest cost as a cost is not well defined; well defined are the branch gap, cost differences within a type and the total of the two bodies (8.24). A later package that needs $`E=I\,v_{\max}^2`$ as a proportionality must state the booking $`\langle Z\rangle=0`$ as a convention; nothing in this setting singles it out.
- The quoted inputs do not say whether the starts of 05 and 06 have a position moment bounded uniformly in the chain length. Item 3 holds for every start in the order $`\kappa_T\to0`$ before $`L_T\to\infty`$. The reverse order, a chain on $`\mathbb Z`$ first and the expansion in $`\kappa_T`$ afterwards, is justified here only for starts with a uniformly bounded position moment, for example those of (8.27).
- The gradient $`\gamma_T=\kappa_T\langle X_T\rangle`$ of (8.22) is convention-independent and of the same order in $`\kappa_T`$ as the force on the position label $`\mathcal F=\kappa\,g(e,F)`$ of 06. It does not enter $`\mu_{\rm av}`$, which is the coefficient of $`F`$, and its effect on the views is bounded by (8.23). For $`\langle X_T\rangle\neq0`$ it should add an $`F`$-independent mean acceleration of order $`\kappa_T^2`$, which the quoted results do not describe; whether 06 accounts for it cannot be checked from the quoted inputs.
- Item 3 inherits the orders of 05 and 06. Beyond leading order in $`\kappa`$ (out of scope), the influence of $`b`$ on the view of $`a`$ vanishes if $`\kappa_A=0`$ or $`\kappa_B=0`$, so it is of order $`\kappa_A\kappa_B`$.
- $`v^T_{\max}`$ is an upper bound. The drift speeds (5.25) of Model D do not exceed $`v^T_{\rm top}<v^T_{\max}`$, which depends on $`\rho_T`$ as well; equal $`v_{\max}`$ does not give equal $`v_{\rm top}`$ (8.15).
- Chain types and Model D types are compared, as the question asks. For all other types this package gives the general statements (8.1)–(8.6), (8.9) and (8.19)–(8.21), and no closed form.

## Methods used

- Linear independence of place projectors; rebooking of single-object terms (A5)
- Invariance analysis under description conventions (M6)
- Partial expectation in the medium start (effective one-body contracts)
- Continuity equation for place weights, Cauchy–Schwarz inequality, Rayleigh bound for a symmetric matrix
- Spectrum of the path-graph adjacency matrix
- Duhamel formula with state-dependent bounds; commutator bound for the position moment; Minkowski inequality; contractivity of the partial trace
- Fourier series and Parseval's identity for the position moment of a wave packet
- Elimination of a parameter and power-series inversion
