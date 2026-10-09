# Mediated effect of a source on a moving body

- **Subproject:** 03-ilang-space
- **Package:** 18-mediated-effect
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-08

## Setup and assumptions

Setting, notation and definitions as in question.md: source $`s`$ (places $`\sigma`$, no hopping), moving body $`b`$ (places $`h`$, hopping $`t_{hh'}`$, records $`K_h`$), medium $`c`$; start $`\lvert\sigma_0\rangle\lvert\beta\rangle\lvert\chi\rangle`$; $`\langle X\rangle=\langle\chi\vert X\vert\chi\rangle`$, $`\tilde X=X-\langle X\rangle`$, $`u_h=\tilde K_h\chi`$ (5.10); $`p_h(\lambda;\sigma_0)`$ the place weights of $`V_{\{b\}}`$ (2.2); $`\bar x=\sum_hp_hu_h`$; influence $`\delta p_h=p_h(\cdot;\sigma)-p_h(\cdot;\sigma')`$. Further notation used below:
```math
\Delta:=B_\sigma-B_{\sigma'},\qquad D_x:=K_x-K_\beta\ (x\in H_T,\ D_\beta=0),\qquad \tau_x:=t^*_{h\beta}t_{hx}t_{x\beta},\qquad h\sim\beta:\ t_{h\beta}\neq0,\ h\neq\beta .
```
Inputs used: (2.1), (2.2), (5.10), (6.4), (6.11), (6.14), (6.15), (8.15), (17.24) as quoted in question.md. Contracts are $`\lambda`$-independent, $`\lambda\ge0`$; items 2–5 are Taylor statements as $`\lambda\to0^+`$ (all expansions converge, A1). The diagonal entries $`t_{hh}`$ are allowed; they are covered by all formulas.

## Derivation

### Step 1. Reduction (item 1a)

Every term of $`C`$ is diagonal in the source places ($`C_b`$, $`K_h`$, $`C_c`$ act trivially on $`s`$), so
```math
C=\sum_\sigma\lvert\sigma\rangle\langle\sigma\rvert\otimes C^{(\sigma)},\qquad
C^{(\sigma)}=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h+\mathbb 1_b\otimes(C_c+B_\sigma),
```
```math
\lvert\Psi(\lambda)\rangle=\lvert\sigma_0\rangle\otimes e^{-\mathrm iC^{(\sigma_0)}\lambda}\bigl(\lvert\beta\rangle\otimes\chi\bigr),\qquad V_{\{s\}}(\lambda)=\lvert\sigma_0\rangle\langle\sigma_0\rvert .
\qquad\text{(18.1)}
```
The source stays at $`\sigma_0`$ for every $`\lambda`$ (as in (6.4)); $`b`$ and $`c`$ are driven by the **reduced contract** $`C^{(\sigma_0)}`$, in which the source acts only as the medium term $`B_{\sigma_0}`$.

Since $`\sum_x\lvert x\rangle\langle x\rvert=\mathbb 1_b`$, (18.1) can be rewritten with the medium operator $`R_\sigma:=K_\beta+C_c+B_\sigma`$:
```math
C^{(\sigma)}=C_b\otimes\mathbb 1+\mathbb 1\otimes R_\sigma+\sum_x\lvert x\rangle\langle x\rvert\otimes D_x .
\qquad\text{(18.2)}
```
Interaction picture with respect to $`\mathbb 1\otimes R_\sigma`$: $`e^{-\mathrm iC^{(\sigma)}\lambda}=(\mathbb 1\otimes e^{-\mathrm iR_\sigma\lambda})\,\mathcal T\exp\bigl(-\mathrm i\int_0^\lambda C_I(s)\,\mathrm ds\bigr)`$ with
```math
C_I(s)=C_b\otimes\mathbb 1+\sum_x\lvert x\rangle\langle x\rvert\otimes D_x(s),\qquad D_x(s):=e^{\mathrm iR_\sigma s}D_xe^{-\mathrm iR_\sigma s} .
\qquad\text{(18.3)}
```
The prefactor is a unitary on the companion of $`b`$, hence it leaves $`V_{\{b\}}`$ unchanged ((2.2): $`\psi_h\to e^{-\mathrm iR\lambda}\psi_h`$). **$`p_h(\lambda;\sigma)`$ depends on the source only through the operator functions $`D_x(s)`$.**

### Step 2. Sufficient condition and invariance (item 1b)

Suppose
```math
[\Delta,\;K_h+C_c+B_{\sigma'}]=0\qquad\text{for every }h\in H_T .
\qquad\text{(18.4)}
```
Taking differences over $`h`$ gives $`[\Delta,D_x]=0`$, and $`h=\beta`$ gives $`[\Delta,R_{\sigma'}]=0`$. Then $`e^{\mathrm iR_\sigma s}=e^{\mathrm iR_{\sigma'}s}e^{\mathrm i\Delta s}`$ and $`D_x^{(\sigma)}(s)=D_x^{(\sigma')}(s)`$ for all $`s,x`$, so by Step 1 the whole view $`V_{\{b\}}`$ coincides for $`\sigma`$ and $`\sigma'`$: $`\delta p_h(\lambda)=0`$ and $`\delta\bar x(\lambda)=0`$ for every $`\lambda`$. Special cases: $`\Delta\propto\mathbb 1`$; or $`\Delta`$ commuting separately with all $`K_h`$, $`C_c`$ and $`B_{\sigma'}`$.

*Invariance.* The total $`C`$ is convention-independent (A5), hence so are its blocks $`C_{\sigma h,\sigma h}:=(\langle\sigma h\rvert\otimes\mathbb 1_c)C(\lvert\sigma h\rangle\otimes\mathbb 1_c)=t_{hh}+K_h+C_c+B_\sigma`$. Thus $`\Delta=C_{\sigma h,\sigma h}-C_{\sigma' h,\sigma' h}`$ (any $`h`$) is invariant, and (18.4) reads $`[\Delta,C_{\sigma'h,\sigma'h}]=0`$ ($`t_{hh}`$ is a number): the condition is invariant. The separate commutators $`[\Delta,K_h]`$, $`[\Delta,C_c]`$ are *not* (moving a medium term $`E`$ from $`C_c`$ into all $`K_h`$ changes them by $`\pm[\Delta,E]`$). The influence is invariant, since $`p_h`$ is computed from the state (18.1), which depends only on the total $`C`$. The same holds for $`R_\sigma`$, $`D_x`$ and $`D_x(s)`$, which are differences or sums of the blocks.

### Step 3. Leading source dependence of $`D_x(s)`$

Treat items 2 and 3 together: one medium object with $`C_c=0`$ is the case $`r=0`$ below (no $`J_k`$). $`R_\sigma=R_{\sigma'}+\Delta`$ and $`D_x(s)=\sum_k\frac{(\mathrm is)^k}{k!}\mathrm{ad}_{R_\sigma}^k(D_x)`$. In the chain, $`D_x`$ acts on $`c_1`$ and $`\Delta`$ on $`c_{r+1}`$. Each $`\mathrm{ad}_{J_k}`$ enlarges the support by at most one cell; $`K_\beta`$ and $`B_{\sigma'}`$ do not enlarge it; $`\Delta`$ commutes with every operator on $`c_1\cdots c_r`$. So the shortest $`\Delta`$-dependent word is $`\mathrm{ad}_\Delta\mathrm{ad}_{J_r}\cdots\mathrm{ad}_{J_1}`$, which is (8.15) with $`B_{\beta_0}\to\Delta`$, $`D\to D_x`$:
```math
\delta D_x(s):=D_x^{(\sigma)}(s)-D_x^{(\sigma')}(s)=\frac{s^{r+1}}{(r+1)!}\,Y_r^{(x)}+O(s^{r+2}),\qquad
Y_r^{(x)}:=\mathrm i^{\,r+1}\bigl[\Delta,[J_r,[\cdots[J_1,D_x]\cdots]]\bigr],
\qquad\text{(18.5)}
```
with $`Y_0^{(x)}=\mathrm i[\Delta,D_x]`$ and $`Y_r^{(\beta)}=0`$. Since $`D_x(s)`$ is self-adjoint for every $`s`$, every Taylor coefficient of $`\delta D_x`$ is self-adjoint; in particular $`\langle Y_r^{(x)}\rangle\in\mathbb R`$. By Step 2, $`\delta D_x`$ and hence $`Y_r^{(x)}`$ do not depend on the A5 convention.

### Step 4. Dyson expansion and order counting

Expand (18.3) in the hops. The $`n`$-hop part of $`\psi_h`$ (notation (2.1)) is
```math
\psi_h^{[n]}=(-\mathrm i)^n\sum_{w}t_w\int_{0<s_1<\cdots<s_n<\lambda}V_{w_n}(\lambda,s_n)\cdots V_{w_0}(s_1,0)\,\chi ,\qquad V_x(b,a)=\mathcal T e^{-\mathrm i\int_a^bD_x},
```
summed over walks $`w=(\beta=w_0,\dots,w_n=h)`$ with $`t_w=\prod_jt_{w_{j+1}w_j}`$. Every hop and every insertion of $`D`$ adds one power of $`\lambda`$; by (18.5) an insertion of $`\delta D`$ adds $`r+2`$ powers. For $`h`$ at graph distance $`n`$ from $`\beta`$, $`\psi_h^{[k]}=0`$ for $`k<n`$, so $`\delta p_h=O(\lambda^{2n+r+2})`$. At this order only $`\delta\psi_h^{[n]}`$ with one $`\delta D`$ and no $`D`$ contributes. The time spent on $`w_j`$ is the interval $`(s_j,s_{j+1})`$ ($`s_0=0`$, $`s_{n+1}=\lambda`$), and the Beta integral gives
```math
\delta\psi_h^{[n]}=-\mathrm i(-\mathrm i)^n\sum_wt_w\sum_{j=0}^n a_j\,Y_r^{(w_j)}\chi,\qquad a_j=\binom{r+1+j}{j}\frac{\lambda^{n+r+2}}{(n+r+2)!}.
```
With $`\psi_h^{[n]}=(-\mathrm i)^n(t^n)_{h\beta}\frac{\lambda^n}{n!}\chi+\dots`$, we get $`\delta\lVert\psi_h^{[n]}\rVert^2=2\mathrm{Re}\langle\psi_h^{[n]}\vert\delta\psi_h^{[n]}\rangle`$, and therefore
```math
\delta p_h=\frac{2\lambda^{2n+r+2}}{n!\,(n+r+2)!}\mathrm{Im}\Bigl[(t^n)^*_{h\beta}\sum_wt_w\sum_{j=1}^{n-1}\binom{r+1+j}{j}\langle Y_r^{(w_j)}\rangle\Bigr]+O(\lambda^{2n+r+3}) .
\qquad\text{(18.6)}
```
The terms $`j=0`$ ($`Y^{(\beta)}=0`$) and $`j=n`$ (common to all $`w`$, giving $`\mathrm{Im}(\lvert(t^n)_{h\beta}\rvert^2\cdot\text{real})=0`$) drop. Equivalently, the bracket is $`\sum_{w,w'}\mathrm{Im}(t^*_{w'}t_w)\,\mu_w`$ with real $`\mu_w`$. So (18.6) vanishes for $`n=1`$, and whenever all products $`t^*_{w'}t_w`$ of shortest walks are real (real hopping, or a unique shortest path); then $`\delta p_h=O(\lambda^{2n+r+3})`$.

### Step 5. Neighbours and $`\beta`$: order $`r+5`$

Let $`h\sim\beta`$. By the counting of Step 4, the $`\lambda^{r+5}`$ terms of $`\delta p_h`$ come from (i) $`\lVert\psi_h^{[1]}\rVert^2`$ with one $`\delta D`$ and one $`D`$, and (ii) $`2\mathrm{Re}\langle\psi_h^{[1]}\vert\psi_h^{[2]}\rangle`$ with one $`\delta D`$ and no $`D`$. Write $`\psi_h^{[1]}=-\mathrm it_{h\beta}\Phi`$, $`\Phi=\lambda\chi-\mathrm i\frac{\lambda^2}{2}D_h\chi+\dots`$, $`Y:=Y_r^{(h)}`$, and use the simplex integrals $`\int_0^\lambda s\,f=\frac{(r+2)\lambda^{r+3}}{(r+3)!}`$, $`\int_{0<a<b<\lambda}a\,f(a)\,\mathrm d a\,\mathrm d b=\frac{(r+2)\lambda^{r+4}}{(r+4)!}`$, $`\int_{0<a<b<\lambda}a\,f(b)\,\mathrm da\,\mathrm db=\frac{(r+2)(r+3)}{2}\frac{\lambda^{r+4}}{(r+4)!}`$ for $`f(s)=s^{r+1}/(r+1)!`$:
```math
\begin{aligned}
\delta\Phi&=-\mathrm i\tfrac{(r+2)\lambda^{r+3}}{(r+3)!}Y\chi-\tfrac{(r+2)\lambda^{r+4}}{(r+4)!}\bigl[D_hY+\tfrac{r+3}{2}YD_h\bigr]\chi+\dots,\\
\text{(i)}:\ \lvert t_{h\beta}\rvert^2\,2\mathrm{Re}\langle\Phi\vert\delta\Phi\rangle&=\lvert t_{h\beta}\rvert^2\tfrac{(r+2)\lambda^{r+5}}{(r+4)!}\bigl[(r+4)-(r+5)\bigr]\mathrm{Re}\langle D_hY\rangle .
\end{aligned}
```
The $`\lambda^{r+4}`$ term $`2\mathrm{Re}\langle\lambda\chi\vert{-\mathrm i}c\,Y\chi\rangle`$ vanishes because $`\langle Y\rangle`$ is real; the same holds for the next Taylor term of $`\delta D`$. For (ii), $`\psi_h^{[2]}=-\sum_xt_{hx}t_{x\beta}\frac{\lambda^2}{2}\chi+\mathrm i\sum_xt_{hx}t_{x\beta}\frac{(r+2)\lambda^{r+4}}{(r+4)!}\bigl[\tfrac{r+3}{2}Y_r^{(h)}+Y_r^{(x)}\bigr]\chi+\dots`$, which gives $`2\mathrm{Re}\langle\psi^{[1]}\vert\psi^{[2]}\rangle\supset\sum_x\mathrm{Re}\tau_x\frac{(r+2)\lambda^{r+5}}{(r+4)!}\bigl[(r+4)-(r+3)\bigr]\langle Y_r^{(h)}\rangle-2\sum_x\mathrm{Re}\tau_x\frac{(r+2)\lambda^{r+5}}{(r+4)!}\langle Y_r^{(x)}\rangle`$. Hence
```math
\delta p_h=\frac{(r+2)\lambda^{r+5}}{(r+4)!}\Bigl[\sum_x\mathrm{Re}\tau_x\,\bigl\langle Y_r^{(h)}-2Y_r^{(x)}\bigr\rangle-\lvert t_{h\beta}\rvert^2\mathrm{Re}\langle D_hY_r^{(h)}\rangle\Bigr]+O(\lambda^{r+6})\qquad(h\sim\beta),
\qquad\text{(18.7)}
```
where $`x`$ runs over all places with $`t_{hx}t_{x\beta}\ne0`$ (common neighbours, and $`x=h,\beta`$ if $`t_{hh},t_{\beta\beta}\ne0`$). Since $`\sum_hp_h=1`$ (2.1) and places at distance $`\ge2`$ contribute at order $`\ge r+6`$ (18.6),
```math
\delta p_\beta=-\lambda^{r+5}\sum_{h\sim\beta}\delta p_h^{(r+5)}+O(\lambda^{r+6}),
\qquad\text{(18.8)}
```
where $`\delta p_h^{(r+5)}`$ is the bracket coefficient of (18.7).

### Step 6. Item 2: one medium object, $`C_c=0`$ ($`r=0`$)

With $`\langle\mathrm i[\Delta,A]\rangle=-2\mathrm{Im}\langle\Delta A\rangle`$ and $`\mathrm{Re}\langle D\,\mathrm i[\Delta,D]\rangle=-\mathrm{Im}\langle\Delta D^2\rangle`$ (self-adjoint $`A,D,\Delta`$), (18.7) becomes, for $`h\sim\beta`$,
```math
\delta p_h=\lambda^5\Bigl[\frac{\lvert t_{h\beta}\rvert^2}{12}\mathrm{Im}\langle\Delta D_h^2\rangle+\frac16\sum_x\mathrm{Re}\tau_x\mathrm{Im}\bigl\langle\Delta(2D_x-D_h)\bigr\rangle\Bigr]+O(\lambda^6),
\qquad\text{(18.9)}
```
$`\delta p_\beta=O(\lambda^5)`$ by (18.8), and for distance $`n\ge2`$ the lowest possible order is $`2n+2`$, with coefficient (18.6) at $`r=0`$: $`\frac{4}{n!(n+2)!}\mathrm{Im}\bigl[(t^n)^*_{h\beta}\sum_wt_w\sum_{j=1}^{n-1}(j+1)\mathrm{Im}\langle D_{w_j}\Delta\rangle\bigr]`$ (otherwise $`\ge2n+3`$). The orders 2 to 4 are source-independent. At $`r=0`$, (18.5) holds with any $`C_c`$, so (18.9) holds also for $`C_c\neq0`$.

**Item 2(b).** The source part of (6.11) for the pair $`(h,\beta)`$ with $`B_{\beta_0}\to\Delta`$ is $`s_{h\beta}:=\mathrm{Im}\langle\Delta\tilde D_h^2\rangle`$. From $`D_h^2=\tilde D_h^2+2\langle D_h\rangle D_h-\langle D_h\rangle^2`$:
```math
\mathrm{Im}\langle\Delta D_h^2\rangle=s_{h\beta}+2(\epsilon_h-\epsilon_\beta)\mathrm{Im}\langle\Delta D_h\rangle .
\qquad\text{(18.10)}
```
So the coefficient (18.9) is $`\frac{\lvert t_{h\beta}\rvert^2}{12}s_{h\beta}`$ plus the record-mean term $`\frac{\lvert t_{h\beta}\rvert^2}{6}(\epsilon_h-\epsilon_\beta)\mathrm{Im}\langle\Delta D_h\rangle`$ plus the $`\tau_x`$ term. These are independent data, so the coefficient is **not** a function of $`s_{h\beta}`$: in Step 9, $`s_{h\beta}=2\sigma\ne0`$ while the coefficient vanishes. It reduces to $`\frac{\lvert t_{h\beta}\rvert^2}{12}s_{h\beta}`$ exactly when $`(\epsilon_h-\epsilon_\beta)\mathrm{Im}\langle\Delta D_h\rangle=0`$ and the $`\tau_x`$ term vanishes (e.g. no triangle through $`h,\beta`$ and $`t_{hh}=t_{\beta\beta}=0`$).

**Item 2(c).** $`\sum_h\delta p_h=0`$, and only $`\beta`$ and its neighbours carry $`\lambda^{r+5}`$ terms. Hence
```math
\delta\bar x=\lambda^{r+5}\sum_{h\sim\beta}\delta p_h^{(r+5)}\,(u_h-u_\beta)+O(\lambda^{r+6}),
\qquad\text{(18.11)}
```
i.e. the lowest order is $`\lambda^5`$ for item 2, with $`\delta p_h^{(5)}`$ from (18.9). A common shift of all $`u_h`$ (A5 convention $`K_h\to K_h+E`$) drops out.

### Step 7. Item 3: locality

By (18.6)–(18.8), the lowest order at which $`\delta p_h`$ can be nonzero is $`\lambda^{r+5}`$, at $`\beta`$ and at its neighbours. It is governed by the nested commutators $`Z_r^{(x)}=[\Delta,[J_r,[\cdots[J_1,D_x]\cdots]]]`$ of (8.15), with $`x=h`$ and the intermediate places $`x`$ of (18.7). Places at distance $`n`$ follow at order $`2n+r+2`$ (only with non-real loop products, (18.6)) or later. Each cell between the record cell $`c_1`$ and the source cell $`c_{r+1}`$ delays the influence by exactly one order. If $`Z_r^{(x)}=0`$ for all relevant $`x`$, the order is higher.

### Step 8. Item 4: cost

Write $`B_\sigma=\langle B_\sigma\rangle\mathbb 1+\tilde B_\sigma`$. By (18.1), $`C^{(\sigma)}=C^{(\sigma)}\big|_{B_\sigma\to\tilde B_\sigma}+\langle B_\sigma\rangle\mathbb 1`$, and the last term gives only the common phase $`e^{-\mathrm i\langle B_\sigma\rangle\lambda}`$ (1.2). So $`p_h(\lambda;\sigma)`$ depends on $`B_\sigma`$ only through $`\tilde B_\sigma`$, and $`\delta p_h`$ is unchanged under $`\Delta\to\Delta+c\mathbb 1`$. The cost difference of the two starts is $`L(\sigma)-L(\sigma')=\langle\Delta\rangle`$ ((1.8); $`L`$ is conserved under (1.9)), and it is A5-invariant (Step 2). Therefore
```math
\delta p_h\ \text{and}\ \delta\bar x\ \text{are independent of}\ L(\sigma)-L(\sigma')=\langle\Delta\rangle ;
\qquad\text{(18.12)}
```
the coefficients (18.7), (18.9) contain $`\Delta`$ only through commutators. Answer: **no**. Counterexamples: $`\Delta=c\mathbb 1`$ has cost difference $`c\ne0`$ and zero influence (exactly); Step 9 has $`\langle\sigma\sigma_y\rangle=0`$, so zero cost difference, and nonzero influence.

### Step 9. Item 5: the qubit example

Here $`\Delta=\sigma\sigma_y`$ ($`\sigma'=0`$), $`r=0`$, $`t`$ is real, the graph is a chain (bipartite, $`t_{hh}=0`$, no triangles) and $`\beta=h_m`$. All records including the source are Pauli vectors in one plane $`\Pi`$: $`Q_{h_i}:=K_{h_i}+B_\sigma=\vec q_i\cdot\vec\sigma`$ with $`\vec q_i=(i,\sigma,i)`$.

*Parity.* (a) Complex conjugation in the place and $`\sigma_z`$ bases maps $`C^{(\sigma)}\to C^{(-\sigma)}`$ and fixes $`\lvert h_m\rangle\chi`$, so $`p_h(\lambda;\sigma)=p_h(-\lambda;-\sigma)`$. (b) In (17.24) with $`K_h\to Q_h`$, each $`c_k(h)`$ is a sum of real hopping products times words in the $`Q`$'s applied to $`\chi`$. On a bipartite chain all walks $`\beta\to h`$ have the parity of the distance, so the number of $`Q`$'s in $`\langle c_k\vert c_l\rangle`$ has the parity of $`k+l`$. Since $`(\vec a\cdot\vec\sigma)(\vec b\cdot\vec\sigma)=\vec a\cdot\vec b+\mathrm i(\vec a\times\vec b)\cdot\vec\sigma`$ with $`\vec a\times\vec b\perp\Pi`$, an odd product of $`Q`$'s equals $`\vec v\cdot\vec\sigma`$ with real $`\vec v`$ and has a real expectation. For odd $`N=k+l`$ the factor $`\mathrm i^k(-\mathrm i)^l`$ is imaginary, so the real number $`p_h^{(N)}`$ vanishes. Hence $`p_h`$ is even in $`\lambda`$, and by (a) even in $`\sigma`$: **the influence is exactly even in $`\sigma`$.**

*Order 5.* For $`h=h_{m\pm1}`$, $`D_h=\pm X`$ and $`X^2=2\cdot\mathbb 1`$, so (18.9) gives $`\mathrm{Im}\langle\Delta D_h^2\rangle=2\sigma\mathrm{Im}\langle\sigma_y\rangle=0`$. In (18.10), $`s_{h\beta}=2\sigma`$ (as in (6.14)) is cancelled by the record-mean term $`2(\pm1)(\mp\sigma)=-2\sigma`$.

*Order 6.* The Δ-dependent $`\lambda^6`$ terms of $`p_{h_{m\pm1}}`$ come only from the one-hop part: $`\psi^{[2]}=0`$, and in $`2\mathrm{Re}\langle\psi^{[1]}\vert\psi^{[3]}\rangle`$ one $`\delta D`$ without $`D`$ gives (real)$`\times\mathrm i\langle Y\rangle`$, whose real part is zero. The one-hop part is $`t^2\lVert\Phi\rVert^2`$ with $`\Phi=\int_0^\lambda U(s)\chi\,\mathrm ds`$, $`U(s)=e^{\mathrm iQ_hs}e^{-\mathrm iQ_\beta s}`$, and
```math
\lVert\Phi\rVert^2=\sum_{n,n'}\frac{\lambda^{n+n'+2}\langle U_{n'}\chi\vert U_n\chi\rangle}{(n+1)!(n'+1)!},\qquad U_n=\sum_k\binom nk(\mathrm iQ_h)^k(-\mathrm iQ_\beta)^{n-k}.
```
With $`d=\pm1`$, $`A_h=\lvert\vec q_h\rvert^2`$, $`A_\beta=\lvert\vec q_\beta\rvert^2`$, $`W=\sigma_z-\sigma_x`$, $`Q_hQ_\beta=\vec q_h\cdot\vec q_\beta+\mathrm i\sigma dW`$, and $`\langle X\rangle=\langle W\rangle=1`$, $`\langle\sigma_y\rangle=0`$, $`W^2=2`$:
$`U_1=\mathrm idX`$, $`U_2=-2+2\mathrm i\sigma dW`$, $`U_3=-\mathrm i[(A_h+3A_\beta)Q_h-(A_\beta+3A_h)Q_\beta]`$, $`U_4=A_h^2+6A_hA_\beta+A_\beta^2-4(A_h+A_\beta)Q_hQ_\beta`$. Their $`\sigma`$-dependent parts are $`\mathrm{Re}\langle U_4\rangle\ni8\sigma^2`$, $`\mathrm{Re}\langle U_1\chi\vert U_3\chi\rangle\ni-8\sigma^2`$ and $`\lVert U_2\chi\rVert^2=4+8\sigma^2`$. The $`\lambda^6`$ coefficient $`\frac{2\mathrm{Re}\langle U_4\rangle}{5!}+\frac{2\mathrm{Re}\langle U_1\chi\vert U_3\chi\rangle}{2!\,4!}+\frac{\lVert U_2\chi\rVert^2}{3!^2}`$ has the $`\sigma`$-part $`\sigma^2\bigl(\frac{16}{120}-\frac{16}{48}+\frac{8}{36}\bigr)=\frac{\sigma^2}{45}`$, the same for $`d=\pm1`$. Distance-2 places: order 6 vanishes by (18.6) (real $`t`$), order 7 by parity. Hence
```math
\delta p_{h_{m\pm1}}=\frac{t^2\sigma^2}{45}\lambda^6+O(\lambda^8),\qquad
\delta p_{h_m}=-\frac{2t^2\sigma^2}{45}\lambda^6+O(\lambda^8),\qquad \delta p_{h_{m\pm k}}=O(\lambda^8)\ (k\ge2).
\qquad\text{(18.13)}
```
Only one-hop amplitudes enter, so (18.13) holds for every $`2\le m\le n-1`$.

*Position.* $`u_{h_i}=\mathrm i(X-1)\lvert0\rangle=\mathrm i\lvert1\rangle`$, so $`\delta\bar x=\lvert1\rangle\sum_ii\,\delta p_{h_i}`$. At order 6 this is $`\frac{t^2\sigma^2}{45}[(m+1)+(m-1)-2m]=0`$, and odd orders vanish. Hence
```math
\delta\bar x=O(\lambda^8),\qquad\text{even in }\sigma .
\qquad\text{(18.14)}
```

*Comparison with (6.14), (6.15).* On the background of $`b`$, the source acts at first order in $`\sigma`$ and reverses with its sign: $`W`$ changes by $`2\sigma(i-j)^2\lambda^3`$, and the derived distance $`\alpha(h_i,h_j)=\lambda\lvert i-j\rvert(1-\sigma\lambda)`$ changes at relative order $`\lambda`$. On the motion of $`b`$ there is no effect at first order in $`\sigma`$, at any order in $`\lambda`$. The leading effect is $`\propto\sigma^2\lambda^6`$, at relative order $`\lambda^4`$ with respect to the hopping weight $`t^2\lambda^2`$. It is the same for both signs of $`\sigma`$, symmetric between $`h_{m\pm1}`$, and moves no weight from $`h_m`$ to one side; the position shift starts at $`\lambda^8`$ at the earliest. The motion is therefore not determined by the background deformation: the (6.11)-based guess $`\frac{t^2}{12}s_{h\beta}\lambda^5=\frac{\sigma t^2}{6}\lambda^5`$ is cancelled exactly by (18.10).

## Result

- **Reduction (18.1)–(18.3):** the source stays at $`\sigma_0`$; $`b,c`$ evolve under $`C^{(\sigma_0)}`$; $`p_h`$ depends on the source only through $`D_x(s)=e^{\mathrm iR_\sigma s}(K_x-K_\beta)e^{-\mathrm iR_\sigma s}`$, $`R_\sigma=K_\beta+C_c+B_\sigma`$.
- **No influence (18.4):** $`[B_\sigma-B_{\sigma'},K_h+C_c+B_{\sigma'}]=0`$ for all $`h`$ is sufficient. It is A5-invariant, as is the influence; the separate commutators with $`K_h`$ and $`C_c`$ are not.
- **Leading orders (18.6)–(18.9), (18.11):** at $`\beta`$ and its neighbours, $`\delta p_h=O(\lambda^{r+5})`$ with coefficient (18.7) ($`r=0`$: (18.9)); $`\delta\bar x=O(\lambda^{r+5})`$ with coefficient (18.11). Distance $`n\ge2`$: order $`2n+r+2`$ (18.6), which needs non-real loop products of shortest walks; otherwise $`\ge2n+r+3`$.
- **2(b) (18.10):** the coefficient equals $`\frac{\lvert t_{h\beta}\rvert^2}{12}s_{h\beta}`$ plus a record-mean term and a triangle term, so it is not a function of the (6.11) source part.
- **Locality (Step 7):** order $`\lambda^{r+5}`$, governed by $`Z_r^{(x)}=[\Delta,[J_r,\dots[J_1,K_x-K_\beta]]]`$, one order per intermediate cell.
- **Cost (18.12):** no; the influence is independent of the cost difference $`\langle B_\sigma-B_{\sigma'}\rangle`$.
- **Example (18.13), (18.14):** $`\delta p_{h_{m\pm1}}=t^2\sigma^2\lambda^6/45`$, $`\delta p_{h_m}=-2t^2\sigma^2\lambda^6/45`$, $`\delta\bar x=O(\lambda^8)`$; the influence is exactly even in $`\sigma`$, unlike the background effect (6.14), (6.15), which is odd in $`\sigma`$.

## Consistency checks

1. **Dimensions.** $`[t]=[K]=[\Delta]=[J]=[C]=[\lambda]^{-1}`$. The coefficient of (18.7) scales as $`[C]^{r+5}`$ (both terms), that of (18.6) as $`[C]^{2n+r+2}`$. In (18.13), restoring a record scale $`K_{h_i}=\mathrm i\kappa X`$ gives $`t^2\sigma^2\kappa^2/45\sim[C]^6`$.
2. **Limits.** $`t\to0`$: $`p_h=\delta_{h\beta}`$ exactly, and every coefficient is $`\propto t^2`$. $`\Delta\propto\mathbb 1`$, or (18.4) holds: all $`Y_r^{(x)}=0`$ and the influence vanishes. $`\sigma\to0`$ in (18.13): zero.
3. **Special case (17.10).** For $`C_c=0`$ the reduced contract is the 17 contract with records $`K_h+B_\sigma`$. (17.10) depends on the records only through $`d_0(h,\beta)`$ and differences of $`\epsilon`$'s, which are invariant under this common shift, so $`\delta p_h^{(4)}=0`$, as Step 6 states. In addition, the first term of (18.9) agrees with a direct Taylor expansion of $`\lVert\Phi\rVert^2`$, whose $`\lambda^5`$ coefficient is $`\frac1{12}\mathrm{Im}\langle Q_\beta D_h^2\rangle`$.

## Open issues

- In the example, the leading coefficient of $`\delta\bar x`$, at order $`\lambda^8`$ or later, is not computed. It needs the $`\lambda^8`$ terms of the 2-, 4- and 6-hop parts, and for $`m\le3`$ or $`m\ge n-2`$ also the chain ends. Even its non-vanishing is open.
- (18.6), (18.7) give the lowest *possible* orders. Nonzero instances: (18.9) for generic records. For (18.6), a square $`\beta,x,y,h`$ with $`n=2`$ gives $`\frac16\mathrm{Im}(t_x^*t_y)\mathrm{Im}\langle(K_y-K_x)\Delta\rangle`$, where $`t_x=t_{hx}t_{x\beta}`$ and $`t_y=t_{hy}t_{y\beta}`$. Exact vanishing conditions beyond these are not classified.
- (18.4) is sufficient, not necessary.

## Methods used

- block decomposition in the conserved source place
- interaction picture, Dyson (time-ordered) expansion
- adjoint expansion and support counting of nested commutators
- simplex and Beta integrals
- Pauli algebra; antiunitary (complex-conjugation) symmetry and a parity argument
