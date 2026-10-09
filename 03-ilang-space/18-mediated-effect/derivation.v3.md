# Mediated effect of a source on a moving body

- **Subproject:** 03-ilang-space
- **Package:** 18-mediated-effect
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-08

## Changes from previous version

- **I1.** Step 10 (paragraph *Result*) and the Result section now say explicitly that (18.16) is the leading term of $\delta\bar x$ for every $2\le m\le n-1$ and $t>0$, except at the isolated point $m=2<n-1$, $t^2=8$. That point is excluded from the item-5 result, and its leading term is not computed.
- **I2.** Consistency check 1: the dimensional check of Step 10 now treats the dimensionless moment $\delta\langle\mathcal N\rangle$ (its $\lambda^8$ coefficient is $[C]^8$) separately from the position $\delta\bar x$ (one more factor $\kappa$, so its $\lambda^8$ coefficient is $[C]^9$).
- All other steps and all tags (18.1)–(18.16) are unchanged.

## Response to verification

- **I1:** Accepted and fixed in Step 10 (paragraph *Result*) and in the Result section. Item 5 is answered for all parameters except the isolated point $m=2<n-1$, $t^2=8$, which is excluded. There the $\lambda^8$ coefficient vanishes, so the leading term is of order $\lambda^{10}$ or higher and is not computed (Open issues).
- **I2:** Accepted and fixed in Consistency check 1. $\delta\langle\mathcal N\rangle$ has the factors $m\sigma^2t^2\kappa^4$ and $\sigma^2t^4\kappa^2$ ($[C]^8$). $\delta\bar x=\kappa\,\delta\langle\mathcal N\rangle\lvert1\rangle$ has the factors $m\sigma^2t^2\kappa^5$ and $\sigma^2t^4\kappa^3$ ($[C]^9$).

## Setup and assumptions

Setting, notation and definitions as in question.md:
- source $s$ (places $\sigma$, no hopping), moving body $b$ (places $h$, hopping $t_{hh'}$, records $K_h$), medium $c$;
- start $\lvert\sigma_0\rangle\lvert\beta\rangle\lvert\chi\rangle$;
- $\langle X\rangle=\langle\chi\vert X\vert\chi\rangle$, $\tilde X=X-\langle X\rangle$, $u_h=\tilde K_h\chi$ (5.10);
- $p_h(\lambda;\sigma_0)$ are the place weights of $V_{\{b\}}$ (2.2), and $\bar x=\sum_hp_hu_h$;
- influence $\delta p_h=p_h(\cdot;\sigma)-p_h(\cdot;\sigma')$.

Further notation used below:
$$
\Delta:=B_\sigma-B_{\sigma'},\qquad D_x:=K_x-K_\beta\ (x\in H_T,\ D_\beta=0),\qquad \tau_x:=t^*_{h\beta}t_{hx}t_{x\beta},\qquad h\sim\beta:\ t_{h\beta}\neq0,\ h\neq\beta .
$$
Inputs used: (2.1), (2.2), (5.10), (6.4), (6.11), (6.14), (6.15), (8.15), (17.24), as quoted in question.md.
- Contracts are $\lambda$-independent, and $\lambda\ge0$.
- Items 2–5 are Taylor statements as $\lambda\to0^+$; all expansions converge (A1).
- Diagonal entries $t_{hh}$ are allowed, and all formulas cover them.

## Derivation

### Step 1. Reduction (item 1a)

Every term of $C$ is diagonal in the source places ($C_b$, $K_h$, $C_c$ act trivially on $s$), so
$$
C=\sum_\sigma\lvert\sigma\rangle\langle\sigma\rvert\otimes C^{(\sigma)},\qquad
C^{(\sigma)}=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h+\mathbb 1_b\otimes(C_c+B_\sigma),
$$
$$
\lvert\Psi(\lambda)\rangle=\lvert\sigma_0\rangle\otimes e^{-\mathrm iC^{(\sigma_0)}\lambda}\bigl(\lvert\beta\rangle\otimes\chi\bigr),\qquad V_{\{s\}}(\lambda)=\lvert\sigma_0\rangle\langle\sigma_0\rvert .
\tag{18.1}
$$
The source stays at $\sigma_0$ for every $\lambda$ (as in (6.4)). $b$ and $c$ are driven by the **reduced contract** $C^{(\sigma_0)}$, in which the source acts only as the medium term $B_{\sigma_0}$.

Since $\sum_x\lvert x\rangle\langle x\rvert=\mathbb 1_b$, (18.1) can be rewritten with the medium operator $R_\sigma:=K_\beta+C_c+B_\sigma$:
$$
C^{(\sigma)}=C_b\otimes\mathbb 1+\mathbb 1\otimes R_\sigma+\sum_x\lvert x\rangle\langle x\rvert\otimes D_x .
\tag{18.2}
$$
In the interaction picture with respect to $\mathbb 1\otimes R_\sigma$, $e^{-\mathrm iC^{(\sigma)}\lambda}=(\mathbb 1\otimes e^{-\mathrm iR_\sigma\lambda})\,\mathcal T\exp\bigl(-\mathrm i\int_0^\lambda C_I(s)\,\mathrm ds\bigr)$, with
$$
C_I(s)=C_b\otimes\mathbb 1+\sum_x\lvert x\rangle\langle x\rvert\otimes D_x(s),\qquad D_x(s):=e^{\mathrm iR_\sigma s}D_xe^{-\mathrm iR_\sigma s} .
\tag{18.3}
$$
The prefactor is a unitary on the companion of $b$, so it leaves $V_{\{b\}}$ unchanged ((2.2): $\psi_h\to e^{-\mathrm iR\lambda}\psi_h$). **$p_h(\lambda;\sigma)$ depends on the source only through the operator functions $D_x(s)$.**

### Step 2. Sufficient condition and invariance (item 1b)

Suppose
$$
[\Delta,\;K_h+C_c+B_{\sigma'}]=0\qquad\text{for every }h\in H_T .
\tag{18.4}
$$
- Taking differences over $h$ gives $[\Delta,D_x]=0$, and $h=\beta$ gives $[\Delta,R_{\sigma'}]=0$.
- Then $e^{\mathrm iR_\sigma s}=e^{\mathrm iR_{\sigma'}s}e^{\mathrm i\Delta s}$, so $D_x^{(\sigma)}(s)=D_x^{(\sigma')}(s)$ for all $s,x$.
- By Step 1 the whole view $V_{\{b\}}$ coincides for $\sigma$ and $\sigma'$: $\delta p_h(\lambda)=0$ and $\delta\bar x(\lambda)=0$ for every $\lambda$.

Special cases: $\Delta\propto\mathbb 1$; or $\Delta$ commutes separately with all $K_h$, $C_c$ and $B_{\sigma'}$.

*Invariance.* The total $C$ is convention-independent (A5), and so are its blocks $C_{\sigma h,\sigma h}:=(\langle\sigma h\rvert\otimes\mathbb 1_c)C(\lvert\sigma h\rangle\otimes\mathbb 1_c)=t_{hh}+K_h+C_c+B_\sigma$.
- $\Delta=C_{\sigma h,\sigma h}-C_{\sigma' h,\sigma' h}$ (any $h$) is invariant.
- (18.4) reads $[\Delta,C_{\sigma'h,\sigma'h}]=0$ ($t_{hh}$ is a number), so the condition is invariant.
- The separate commutators $[\Delta,K_h]$, $[\Delta,C_c]$ are *not* invariant: moving a medium term $E$ from $C_c$ into all $K_h$ changes them by $\pm[\Delta,E]$.
- The influence is invariant, since $p_h$ is computed from the state (18.1), which depends only on the total $C$.

The split of a block into $t_{hh}$ and $K_h$ is not unique either. A diagonal single-body term of $b$ can be written in $C_b$ or in the $b$–$c$ term: $t_{xx}\to t_{xx}-e_x$, $K_x\to K_x+e_x\mathbb 1_c$ ($e_x\in\mathbb R$).
- Medium-only reassignments (between $C_c$, all $K_h$, all $B_\sigma$) leave $R_\sigma$, $D_x$ and $D_x(s)$ unchanged.
- The diagonal body reassignment gives $R_\sigma\to R_\sigma+e_\beta\mathbb 1$, $D_x\to D_x+(e_x-e_\beta)\mathbb 1$ and $D_x(s)\to D_x(s)+(e_x-e_\beta)\mathbb 1$. The shift of $t_{xx}$ compensates these in $C^{(\sigma)}$.
- Strictly invariant are the blocks, $R_\sigma+t_{\beta\beta}=C_{\sigma\beta,\sigma\beta}$, $D_x+t_{xx}-t_{\beta\beta}$, and every quantity in which these $\sigma$-independent scalars cancel: $\delta D_x(s):=D_x^{(\sigma)}(s)-D_x^{(\sigma')}(s)$, its Taylor coefficients, and the full coefficients of $\delta p_h$.

### Step 3. Leading source dependence of $D_x(s)$

Items 2 and 3 are treated together: one medium object with $C_c=0$ is the case $r=0$ below (no $J_k$). $R_\sigma=R_{\sigma'}+\Delta$ and $D_x(s)=\sum_k\frac{(\mathrm is)^k}{k!}\mathrm{ad}_{R_\sigma}^k(D_x)$. In the chain, $D_x$ acts on $c_1$ and $\Delta$ on $c_{r+1}$.
- Each $\mathrm{ad}_{J_k}$ enlarges the support by at most one cell.
- $K_\beta$ and $B_{\sigma'}$ do not enlarge it.
- $\Delta$ commutes with every operator on $c_1\cdots c_r$.

So the shortest $\Delta$-dependent word is $\mathrm{ad}_\Delta\mathrm{ad}_{J_r}\cdots\mathrm{ad}_{J_1}$, which is (8.15) with $B_{\beta_0}\to\Delta$, $D\to D_x$:
$$
\delta D_x(s):=D_x^{(\sigma)}(s)-D_x^{(\sigma')}(s)=\frac{s^{r+1}}{(r+1)!}\,Y_r^{(x)}+O(s^{r+2}),\qquad
Y_r^{(x)}:=\mathrm i^{\,r+1}\bigl[\Delta,[J_r,[\cdots[J_1,D_x]\cdots]]\bigr],
\tag{18.5}
$$
with $Y_0^{(x)}=\mathrm i[\Delta,D_x]$ and $Y_r^{(\beta)}=0$.
- $D_x(s)$ is self-adjoint for every $s$, so every Taylor coefficient of $\delta D_x$ is self-adjoint; in particular $\langle Y_r^{(x)}\rangle\in\mathbb R$.
- $\delta D_x$, and hence $Y_r^{(x)}$, does not depend on the A5 convention. Medium reassignments leave $D_x^{(\sigma)}(s)$ unchanged. The diagonal body reassignment adds the same scalar $(e_x-e_\beta)\mathbb 1$ to $D_x^{(\sigma)}(s)$ and $D_x^{(\sigma')}(s)$ (Step 2).

### Step 4. Dyson expansion and order counting

Expand (18.3) in the hops. The $n$-hop part of $\psi_h$ (notation (2.1)) is
$$
\psi_h^{[n]}=(-\mathrm i)^n\sum_{w}t_w\int_{0<s_1<\cdots<s_n<\lambda}V_{w_n}(\lambda,s_n)\cdots V_{w_0}(s_1,0)\,\chi ,\qquad V_x(b,a)=\mathcal T e^{-\mathrm i\int_a^bD_x},
$$
summed over walks $w=(\beta=w_0,\dots,w_n=h)$, with $t_w=\prod_jt_{w_{j+1}w_j}$.

*Counting.* Every hop and every insertion of $D$ adds one power of $\lambda$. By (18.5), an insertion of $\delta D$ adds $r+2$ powers. For $h$ at graph distance $n$ from $\beta$, $\psi_h^{[k]}=0$ for $k<n$, so $\delta p_h=O(\lambda^{2n+r+2})$. At this order only $\delta\psi_h^{[n]}$ with one $\delta D$ and no $D$ contributes.

*Coefficient.* The time spent on $w_j$ is the interval $(s_j,s_{j+1})$ ($s_0=0$, $s_{n+1}=\lambda$), and the Beta integral gives
$$
\delta\psi_h^{[n]}=-\mathrm i(-\mathrm i)^n\sum_wt_w\sum_{j=0}^n a_j\,Y_r^{(w_j)}\chi,\qquad a_j=\binom{r+1+j}{j}\frac{\lambda^{n+r+2}}{(n+r+2)!}.
$$
With $\psi_h^{[n]}=(-\mathrm i)^n(t^n)_{h\beta}\frac{\lambda^n}{n!}\chi+\dots$, we get $\delta\lVert\psi_h^{[n]}\rVert^2=2\operatorname{Re}\langle\psi_h^{[n]}\vert\delta\psi_h^{[n]}\rangle$, and therefore
$$
\delta p_h=\frac{2\lambda^{2n+r+2}}{n!\,(n+r+2)!}\operatorname{Im}\Bigl[(t^n)^*_{h\beta}\sum_wt_w\sum_{j=1}^{n-1}\binom{r+1+j}{j}\langle Y_r^{(w_j)}\rangle\Bigr]+O(\lambda^{2n+r+3}) .
\tag{18.6}
$$
- The term $j=0$ drops because $Y^{(\beta)}=0$.
- The term $j=n$ drops because it is common to all $w$ and gives $\operatorname{Im}(\lvert(t^n)_{h\beta}\rvert^2\cdot\text{real})=0$.
- Equivalently, the bracket is $\sum_{w,w'}\operatorname{Im}(t^*_{w'}t_w)\,\mu_w$ with real $\mu_w$.

So (18.6) vanishes for $n=1$, and whenever all products $t^*_{w'}t_w$ of shortest walks are real (real hopping, or a unique shortest path). Then $\delta p_h=O(\lambda^{2n+r+3})$.

### Step 5. Neighbours and $\beta$: order $r+5$

Let $h\sim\beta$. By the counting of Step 4, the $\lambda^{r+5}$ terms of $\delta p_h$ come from:
- (i) $\lVert\psi_h^{[1]}\rVert^2$ with one $\delta D$ and one $D$;
- (ii) $2\operatorname{Re}\langle\psi_h^{[1]}\vert\psi_h^{[2]}\rangle$ with one $\delta D$ and no $D$.

Write $\psi_h^{[1]}=-\mathrm it_{h\beta}\Phi$ with $\Phi=\lambda\chi-\mathrm i\frac{\lambda^2}{2}D_h\chi+\dots$, and $Y:=Y_r^{(h)}$. For $f(s)=s^{r+1}/(r+1)!$, the simplex integrals are
- $\int_0^\lambda s\,f=\frac{(r+2)\lambda^{r+3}}{(r+3)!}$;
- $\int_{0<a<b<\lambda}a\,f(a)\,\mathrm d a\,\mathrm d b=\frac{(r+2)\lambda^{r+4}}{(r+4)!}$;
- $\int_{0<a<b<\lambda}a\,f(b)\,\mathrm da\,\mathrm db=\frac{(r+2)(r+3)}{2}\frac{\lambda^{r+4}}{(r+4)!}$.

They give
$$
\begin{aligned}
\delta\Phi&=-\mathrm i\tfrac{(r+2)\lambda^{r+3}}{(r+3)!}Y\chi-\tfrac{(r+2)\lambda^{r+4}}{(r+4)!}\bigl[D_hY+\tfrac{r+3}{2}YD_h\bigr]\chi+\dots,\\
\text{(i)}:\ \lvert t_{h\beta}\rvert^2\,2\operatorname{Re}\langle\Phi\vert\delta\Phi\rangle&=\lvert t_{h\beta}\rvert^2\tfrac{(r+2)\lambda^{r+5}}{(r+4)!}\bigl[(r+4)-(r+5)\bigr]\operatorname{Re}\langle D_hY\rangle .
\end{aligned}
$$
The $\lambda^{r+4}$ term $2\operatorname{Re}\langle\lambda\chi\vert{-\mathrm i}c\,Y\chi\rangle$ vanishes because $\langle Y\rangle$ is real; the same holds for the next Taylor term of $\delta D$.

For (ii),
$$
\psi_h^{[2]}=-\sum_xt_{hx}t_{x\beta}\frac{\lambda^2}{2}\chi+\mathrm i\sum_xt_{hx}t_{x\beta}\frac{(r+2)\lambda^{r+4}}{(r+4)!}\bigl[\tfrac{r+3}{2}Y_r^{(h)}+Y_r^{(x)}\bigr]\chi+\dots,
$$
so $2\operatorname{Re}\langle\psi^{[1]}\vert\psi^{[2]}\rangle$ contains
$$
\sum_x\operatorname{Re}\tau_x\frac{(r+2)\lambda^{r+5}}{(r+4)!}\bigl[(r+4)-(r+3)\bigr]\langle Y_r^{(h)}\rangle-2\sum_x\operatorname{Re}\tau_x\frac{(r+2)\lambda^{r+5}}{(r+4)!}\langle Y_r^{(x)}\rangle .
$$
Hence
$$
\delta p_h=\frac{(r+2)\lambda^{r+5}}{(r+4)!}\Bigl[\sum_x\operatorname{Re}\tau_x\,\bigl\langle Y_r^{(h)}-2Y_r^{(x)}\bigr\rangle-\lvert t_{h\beta}\rvert^2\operatorname{Re}\langle D_hY_r^{(h)}\rangle\Bigr]+O(\lambda^{r+6})\qquad(h\sim\beta),
\tag{18.7}
$$
where $x$ runs over all places with $t_{hx}t_{x\beta}\ne0$: the common neighbours, and $x=h,\beta$ if $t_{hh},t_{\beta\beta}\ne0$. Since $\sum_hp_h=1$ (2.1) and places at distance $\ge2$ contribute only at order $\ge r+6$ (18.6),
$$
\delta p_\beta=-\lambda^{r+5}\sum_{h\sim\beta}\delta p_h^{(r+5)}+O(\lambda^{r+6}),
\tag{18.8}
$$
where $\delta p_h^{(r+5)}$ is the bracket coefficient of (18.7).

### Step 6. Item 2: one medium object, $C_c=0$ ($r=0$)

For self-adjoint $A,D,\Delta$, $\langle\mathrm i[\Delta,A]\rangle=-2\operatorname{Im}\langle\Delta A\rangle$ and $\operatorname{Re}\langle D\,\mathrm i[\Delta,D]\rangle=-\operatorname{Im}\langle\Delta D^2\rangle$. With these, (18.7) becomes, for $h\sim\beta$,
$$
\delta p_h=\lambda^5\Bigl[\frac{\lvert t_{h\beta}\rvert^2}{12}\operatorname{Im}\langle\Delta D_h^2\rangle+\frac16\sum_x\operatorname{Re}\tau_x\operatorname{Im}\bigl\langle\Delta(2D_x-D_h)\bigr\rangle\Bigr]+O(\lambda^6).
\tag{18.9}
$$
- $\delta p_\beta=O(\lambda^5)$ by (18.8).
- For distance $n\ge2$ the lowest possible order is $2n+2$, with coefficient (18.6) at $r=0$, $\frac{4}{n!(n+2)!}\operatorname{Im}\bigl[(t^n)^*_{h\beta}\sum_wt_w\sum_{j=1}^{n-1}(j+1)\operatorname{Im}\langle D_{w_j}\Delta\rangle\bigr]$; otherwise the order is $\ge2n+3$.
- The orders 2 to 4 are source-independent.
- At $r=0$, (18.5) holds for any $C_c$, so (18.9) holds also for $C_c\neq0$.

**Item 2(b).** The source part of (6.11) for the pair $(h,\beta)$, with $B_{\beta_0}\to\Delta$, is $s_{h\beta}:=\operatorname{Im}\langle\Delta\tilde D_h^2\rangle$. From $D_h^2=\tilde D_h^2+2\langle D_h\rangle D_h-\langle D_h\rangle^2$:
$$
\operatorname{Im}\langle\Delta D_h^2\rangle=s_{h\beta}+2(\epsilon_h-\epsilon_\beta)\operatorname{Im}\langle\Delta D_h\rangle .
\tag{18.10}
$$
So the coefficient (18.9) has three parts: $\frac{\lvert t_{h\beta}\rvert^2}{12}s_{h\beta}$, the record-mean term $\frac{\lvert t_{h\beta}\rvert^2}{6}(\epsilon_h-\epsilon_\beta)\operatorname{Im}\langle\Delta D_h\rangle$, and the $\tau_x$ term.
- These are independent data, so the coefficient is **not** a function of $s_{h\beta}$. In Step 9, $s_{h\beta}=2\sigma\ne0$ while the coefficient vanishes.
- It reduces to $\frac{\lvert t_{h\beta}\rvert^2}{12}s_{h\beta}$ exactly when the *sum* of the record-mean term and the $\tau_x$ term vanishes.
- Separate vanishing is sufficient: $(\epsilon_h-\epsilon_\beta)\operatorname{Im}\langle\Delta D_h\rangle=0$, and e.g. no triangle through $h,\beta$ and $t_{hh}=t_{\beta\beta}=0$.
- It is not necessary. For $H_T=\{h,\beta\}$ the sum is $\frac{\lvert t_{h\beta}\rvert^2}{6}(\epsilon_h-\epsilon_\beta+t_{hh}-t_{\beta\beta})\operatorname{Im}\langle\Delta D_h\rangle$. It vanishes for $t_{hh}-t_{\beta\beta}=\epsilon_\beta-\epsilon_h\ne0$, with both terms nonzero.
- Only this sum (and $s_{h\beta}$) is A5-invariant: the diagonal body reassignment of Step 2 shifts the two terms by $\pm\frac{\lvert t_{h\beta}\rvert^2}{6}(e_h-e_\beta)\operatorname{Im}\langle\Delta D_h\rangle$.

**Item 2(c).** $\sum_h\delta p_h=0$, and only $\beta$ and its neighbours carry $\lambda^{r+5}$ terms. Hence
$$
\delta\bar x=\lambda^{r+5}\sum_{h\sim\beta}\delta p_h^{(r+5)}\,(u_h-u_\beta)+O(\lambda^{r+6}),
\tag{18.11}
$$
so the lowest order for item 2 is $\lambda^5$, with $\delta p_h^{(5)}$ from (18.9). A common shift of all $u_h$ (the A5 convention $K_h\to K_h+E$) drops out.

### Step 7. Item 3: locality

By (18.6)–(18.8), the lowest order at which $\delta p_h$ can be nonzero is $\lambda^{r+5}$, at $\beta$ and at its neighbours.
- It is governed by the nested commutators $Z_r^{(x)}=[\Delta,[J_r,[\cdots[J_1,D_x]\cdots]]]$ of (8.15), with $x=h$ and the intermediate places $x$ of (18.7).
- Places at distance $n$ follow at order $2n+r+2$ (only with non-real loop products, (18.6)) or later.
- Each cell between the record cell $c_1$ and the source cell $c_{r+1}$ delays the influence by exactly one order.
- If $Z_r^{(x)}=0$ for all relevant $x$, the order is higher.

### Step 8. Item 4: cost

Write $B_\sigma=\langle B_\sigma\rangle\mathbb 1+\tilde B_\sigma$. By (18.1), $C^{(\sigma)}=C^{(\sigma)}\big|_{B_\sigma\to\tilde B_\sigma}+\langle B_\sigma\rangle\mathbb 1$.
- The last term gives only the common phase $e^{-\mathrm i\langle B_\sigma\rangle\lambda}$ (1.2). So $p_h(\lambda;\sigma)$ depends on $B_\sigma$ only through $\tilde B_\sigma$, and $\delta p_h$ is unchanged under $\Delta\to\Delta+c\mathbb 1$.
- The cost difference of the two starts is $L(\sigma)-L(\sigma')=\langle\Delta\rangle$ ((1.8); $L$ is conserved under (1.9)). It is A5-invariant (Step 2).

Therefore
$$
\delta p_h\ \text{and}\ \delta\bar x\ \text{are independent of}\ L(\sigma)-L(\sigma')=\langle\Delta\rangle ;
\tag{18.12}
$$
the coefficients (18.7), (18.9) contain $\Delta$ only through commutators. Answer: **no**. Counterexamples:
- $\Delta=c\mathbb 1$ has cost difference $c\ne0$ and zero influence (exactly);
- in Step 9, $\langle\sigma\sigma_y\rangle=0$, so the cost difference is zero, and the influence is nonzero.

### Step 9. Item 5: the qubit example, place weights

Here $\Delta=\sigma\sigma_y$ ($\sigma'=0$), $r=0$, $t$ is real, and $\beta=h_m$. The graph is a chain: bipartite, $t_{hh}=0$, no triangles. All records, the source included, are Pauli vectors in one plane $\Pi$: $Q_{h_i}:=K_{h_i}+B_\sigma=\vec q_i\cdot\vec\sigma$ with $\vec q_i=(i,\sigma,i)$.

*Parity.*
- (a) Complex conjugation in the place and $\sigma_z$ bases maps $C^{(\sigma)}\to C^{(-\sigma)}$ and fixes $\lvert h_m\rangle\chi$, so $p_h(\lambda;\sigma)=p_h(-\lambda;-\sigma)$.
- (b) In (17.24) with $K_h\to Q_h$, each $c_k(h)$ is a sum of real hopping products times words in the $Q$'s applied to $\chi$.
  - On a bipartite chain all walks $\beta\to h$ have the parity of the distance, so the number of $Q$'s in $\langle c_k\vert c_l\rangle$ has the parity of $k+l$.
  - $(\vec a\cdot\vec\sigma)(\vec b\cdot\vec\sigma)=\vec a\cdot\vec b+\mathrm i(\vec a\times\vec b)\cdot\vec\sigma$ with $\vec a\times\vec b\perp\Pi$. Hence an odd product of $Q$'s equals $\vec v\cdot\vec\sigma$ with real $\vec v$ and has a real expectation.
  - For odd $N=k+l$ the factor $\mathrm i^k(-\mathrm i)^l$ is imaginary, so the real number $p_h^{(N)}$ vanishes.

Hence $p_h$ is even in $\lambda$, and by (a) even in $\sigma$: **the influence is exactly even in $\sigma$.**

*Order 5.* For $h=h_{m\pm1}$, $D_h=\pm X$ and $X^2=2\cdot\mathbb 1$, so in (18.9) $\operatorname{Im}\langle\Delta D_h^2\rangle=2\sigma\operatorname{Im}\langle\sigma_y\rangle=0$. In (18.10), the record-mean term $2(\pm1)(\mp\sigma)=-2\sigma$ cancels $s_{h\beta}=2\sigma$ (as in (6.14)).

*Order 6.* The $\Delta$-dependent $\lambda^6$ terms of $p_{h_{m\pm1}}$ come only from the one-hop part. Indeed $\psi^{[2]}=0$, and in $2\operatorname{Re}\langle\psi^{[1]}\vert\psi^{[3]}\rangle$ one $\delta D$ without $D$ gives (real)$\times\mathrm i\langle Y\rangle$, whose real part is zero. The one-hop part is $t^2\lVert\Phi\rVert^2$ with $\Phi=\int_0^\lambda U(s)\chi\,\mathrm ds$, $U(s)=e^{\mathrm iQ_hs}e^{-\mathrm iQ_\beta s}$, and
$$
\lVert\Phi\rVert^2=\sum_{n,n'}\frac{\lambda^{n+n'+2}\langle U_{n'}\chi\vert U_n\chi\rangle}{(n+1)!(n'+1)!},\qquad U_n=\sum_k\binom nk(\mathrm iQ_h)^k(-\mathrm iQ_\beta)^{n-k}.
$$
Notation: $d=\pm1$, $A_h=\lvert\vec q_h\rvert^2$, $A_\beta=\lvert\vec q_\beta\rvert^2$, $W=\sigma_z-\sigma_x$, so $Q_hQ_\beta=\vec q_h\cdot\vec q_\beta+\mathrm i\sigma dW$; also $\langle X\rangle=\langle W\rangle=1$, $\langle\sigma_y\rangle=0$, $W^2=2$. Then
- $U_1=\mathrm idX$, $U_2=-2+2\mathrm i\sigma dW$;
- $U_3=-\mathrm i[(A_h+3A_\beta)Q_h-(A_\beta+3A_h)Q_\beta]$;
- $U_4=A_h^2+6A_hA_\beta+A_\beta^2-4(A_h+A_\beta)Q_hQ_\beta$.

Their $\sigma$-dependent parts are $\operatorname{Re}\langle U_4\rangle\ni8\sigma^2$, $\operatorname{Re}\langle U_1\chi\vert U_3\chi\rangle\ni-8\sigma^2$ and $\lVert U_2\chi\rVert^2=4+8\sigma^2$. The $\lambda^6$ coefficient is
$$
\frac{2\operatorname{Re}\langle U_4\rangle}{5!}+\frac{2\operatorname{Re}\langle U_1\chi\vert U_3\chi\rangle}{2!\,4!}+\frac{\lVert U_2\chi\rVert^2}{3!^2}.
$$
Its $\sigma$-part is $\sigma^2\bigl(\frac{16}{120}-\frac{16}{48}+\frac{8}{36}\bigr)=\frac{\sigma^2}{45}$, the same for $d=\pm1$. For distance-2 places, order 6 vanishes by (18.6) (real $t$) and order 7 by parity. Hence
$$
\delta p_{h_{m\pm1}}=\frac{t^2\sigma^2}{45}\lambda^6+O(\lambda^8),\qquad
\delta p_{h_m}=-\frac{2t^2\sigma^2}{45}\lambda^6+O(\lambda^8),\qquad \delta p_{h_{m\pm k}}=O(\lambda^8)\ (k\ge2).
\tag{18.13}
$$
Only one-hop amplitudes enter, so (18.13) holds for every $2\le m\le n-1$.

*Position, orders $\le7$.* $u_{h_i}=\mathrm i(X-1)\lvert0\rangle=\mathrm i\lvert1\rangle$, so $\delta\bar x=\lvert1\rangle\sum_ii\,\delta p_{h_i}$. At order 6 this is $\frac{t^2\sigma^2}{45}[(m+1)+(m-1)-2m]=0$, and odd orders vanish. Hence
$$
\delta\bar x=O(\lambda^8),\qquad\text{even in }\sigma .
\tag{18.14}
$$

### Step 10. Item 5: leading position influence

*Moment and word expansion.* Let $\mathcal N:=\sum_jj\lvert h_j\rangle\langle h_j\rvert$. By (18.14), $\delta\bar x=\delta\langle\mathcal N\rangle\,\lvert1\rangle$ with $\langle\mathcal N\rangle(\lambda)=\sum_jj\,p_{h_j}$.
- With $K_{h_j}=jX$, $B_\sigma=\sigma\sigma_y$, $C_c=0$, the reduced contract (18.1) is $H=C_b\otimes\mathbb 1+\mathcal N\otimes X+\sigma\,\mathbb 1\otimes\sigma_y$, with $C_b=t\sum_j(\lvert h_j\rangle\langle h_{j+1}\rvert+\text{h.c.})$.
- By (1.9), $\langle\mathcal N\rangle(\lambda)=\sum_k\frac{\lambda^k}{k!}\langle L^k(\mathcal N\otimes\mathbb 1)\rangle_0$, with $LY:=\mathrm i[H,Y]$ and $\langle\cdot\rangle_0$ the expectation in $\lvert h_m\rangle\lvert0\rangle$.

The products $X^2=W^2=2$, $XW=-WX=-2\mathrm i\sigma_y$, $X\sigma_y=-\sigma_yX=\mathrm iW$, $W\sigma_y=-\sigma_yW=-\mathrm iX$ give, for every body operator $A$,
$$
\begin{aligned}
L(A\otimes\mathbb 1)&=\mathsf tA\otimes\mathbb 1+\mathsf nA\otimes X, &
L(A\otimes X)&=\mathsf tA\otimes X+2\,\mathsf nA\otimes\mathbb 1+2\sigma A\otimes W,\\
L(A\otimes W)&=\mathsf tA\otimes W+2\,\mathsf aA\otimes\sigma_y-2\sigma A\otimes X, &
L(A\otimes\sigma_y)&=\mathsf tA\otimes\sigma_y-\mathsf aA\otimes W,
\end{aligned}
\tag{18.15}
$$
with $\mathsf tA:=\mathrm i[C_b,A]$, $\mathsf nA:=\mathrm i[\mathcal N,A]$, $\mathsf aA:=\{\mathcal N,A\}$, and $\langle\mathbb 1\rangle=\langle X\rangle=\langle W\rangle=1$, $\langle\sigma_y\rangle=0$.

So $\langle L^8\mathcal N\rangle_0$ is a sum over *words*: sequences of 8 steps $\mathsf t,\mathsf n,\mathsf a,\sigma$, each following one arrow of (18.15) on the label graph $\mathbb 1\overset{\mathsf n}{-}X\overset{\sigma}{-}W\overset{\mathsf a}{-}\sigma_y$ ($\mathsf t$ keeps the label). Let $q,s,\rho$ count the $\mathsf t$-, $\sigma$- and ($\mathsf n$ or $\mathsf a$)-steps, $q+s+\rho=8$.
- A word's body operator is a sum of products with $q$ factors $C_b$ and factors $\mathcal N$. Its value at $h_m$ is therefore a sum over closed walks of $q$ hops, so $q$ is even.
- $\delta\langle\mathcal N\rangle$ is even in $\sigma$ (Step 9) and a word is $\propto\sigma^s$, so only even $s\ge2$ contribute. Then $\rho$ is even.

*Walks on $\mathbb Z$.* Extend the chain to $\mathbb Z$ with $K_{h_j}=jX$ for all $j$. A closed walk from $h_m$ that leaves $\{h_1,\dots,h_n\}$ has $q\ge2m$ or $q\ge2(n+1-m)$, so words with $q<4$ have the same value on both. On $\mathbb Z$, write operators as $\sum_kg_k(\mathcal N)\Theta^k$, with $\Theta\lvert h_{j+1}\rangle=\lvert h_j\rangle$ and $\Theta^{-k}:=\Theta^{\dagger k}$. With $\Theta g(\mathcal N)=g(\mathcal N+1)\Theta$,
$$
\mathsf t(g\Theta^k)=\mathrm it\bigl[(g(\mathcal N{+}1)-g)\Theta^{k+1}+(g(\mathcal N{-}1)-g)\Theta^{k-1}\bigr],\quad \mathsf n(g\Theta^k)=-\mathrm ik\,g\Theta^k,\quad \mathsf a(g\Theta^k)=(2\mathcal N+k)\,g\Theta^k,
$$
and $\langle h_m\vert g\Theta^k\vert h_m\rangle=\delta_{k0}g(m)$. In particular $\mathsf t\mathcal N=\Gamma:=\mathrm it(\Theta-\Theta^\dagger)$, $\mathsf n\Gamma=C_b$, $\mathsf nC_b=-\Gamma$ and $\mathsf n\mathcal N=0$; these hold on the chain too. $\mathsf t$ annihilates every operator with constant $g_k$.

*Selection.*
- (i) The first step is $\mathsf t$: $\mathsf n\mathcal N=0$, and $\sigma$, $\mathsf a$ do not act on label $\mathbb 1$.
- (ii) On $\mathbb Z$, $\mathsf t$ and $\mathsf n$ keep $g_k$ constant after the first step, so the second $\mathsf t$-step must follow an $\mathsf a$-step.
- (iii) The final label is not $\sigma_y$, so $\mathsf a$-steps come in pairs, and reaching $W$ needs an $\mathsf n$. Hence $\rho\ge3$, so $\rho\ge4$, and $q=s=2$, $\rho=4$. The only label path with two $\sigma$-, two $\mathsf a$- and two $\mathsf n$-steps is $\mathbb 1\to X\to W\to\sigma_y\to W\to X\to\mathbb 1$.
- (iv) After the first $\mathsf t$ the operator has $k=\pm1$. $\mathsf n$ and $\mathsf a$ keep $k$, and $\mathsf n$ kills $k=0$, so the second $\mathsf t$ comes last.

The unique bulk word is
$$
\mathcal N\xrightarrow{\mathsf t}\Gamma\xrightarrow{\mathsf n}C_b\otimes X\xrightarrow{\sigma}2\sigma C_b\otimes W\xrightarrow{\mathsf a}4\sigma\,\mathsf aC_b\otimes\sigma_y\xrightarrow{\mathsf a}-4\sigma\,\mathsf a^2C_b\otimes W\xrightarrow{\sigma}8\sigma^2\mathsf a^2C_b\otimes X\xrightarrow{\mathsf n}16\sigma^2\,\mathsf n\mathsf a^2C_b\xrightarrow{\mathsf t}16\sigma^2\,\mathsf t\mathsf n\mathsf a^2C_b .
$$
Here $\mathsf n\mathsf a^2C_b=-\mathrm it[(2\mathcal N+1)^2\Theta-(2\mathcal N-1)^2\Theta^\dagger]$. The $k=0$ part of $\mathsf t$ of it at $h_m$ is $\mathrm it\cdot\mathrm it\,\{-[(2m-1)^2-(2m+1)^2]+[(2m+1)^2-(2m-1)^2]\}=-16mt^2$. Bulk value: $-256\,m\sigma^2t^2$.

*Chain ends.* Words with $q\ge4$ vanish on $\mathbb Z$ by (ii)–(iii). They differ on the chain only if $m=2$ or $m=n-1$.
- They have $s=\rho=2$ and $q=4$: no $\mathsf a$-pair fits, and $q\ge6$ leaves no $\mathsf n$. Their label path is $\mathbb 1\to X\to W\to X\to\mathbb 1$, with factor $1\cdot2\sigma\cdot(-2\sigma)\cdot2=-8\sigma^2$.
- On the chain $\mathsf t\Gamma=2t^2(P_1-P_n)$, with $P_j:=\lvert h_j\rangle\langle h_j\rvert$.
- $\mathsf tC_b=0$, $\mathsf n$ kills diagonal operators, and the last step cannot be $\mathsf n$. So the body orders are $\mathsf t\mathsf n\mathsf n\mathsf t\mathsf t\mathsf t$ and $\mathsf t\mathsf t\mathsf t\mathsf n\mathsf n\mathsf t$, with the $\sigma$-steps between the $\mathsf n$'s. Both give $-8\sigma^2\cdot(-\mathsf t^3\Gamma)$ ($\mathsf n^2=-1$ on hops $\pm1$).
- $\langle h_m\vert\mathsf t^2P_1\vert h_m\rangle=2\lvert\langle h_m\vert C_b\vert h_1\rangle\rvert^2=2t^2\delta_{m,2}$, and likewise for $P_n$. The end value is $2\cdot8\sigma^2\cdot4t^4(\delta_{m,2}-\delta_{m,n-1})$.

*Result.* Divide $-256m\sigma^2t^2+64\sigma^2t^4(\delta_{m,2}-\delta_{m,n-1})$ by $8!$, and use that odd orders vanish (Step 9):
$$
\delta\bar x=-\frac{\sigma^2t^2}{630}\Bigl[4m-t^2\bigl(\delta_{m,2}-\delta_{m,n-1}\bigr)\Bigr]\lambda^8\,\lvert1\rangle+O(\lambda^{10}),\qquad 2\le m\le n-1 .
\tag{18.16}
$$
- For $3\le m\le n-2$ it is $-\frac{2m}{315}\sigma^2t^2\lambda^8\lvert1\rangle$.
- At $m=2<n-1$ the bracket is $8-t^2$; at $m=n-1>2$ it is $4(n-1)+t^2$; for $n=3$ it is $8$.

So the $\lambda^8$ coefficient is nonzero for every $\sigma\ne0$, $t>0$, $2\le m\le n-1$, except at the isolated point $m=2<n-1$, $t^2=8$ (in record units; $t^2=8\kappa^2$ for $K_{h_i}=\mathrm i\kappa X$, Check 1). **(18.16) therefore gives the leading term of $\delta\bar x$ everywhere in the parameter range of item 5 except at this point, which is excluded from the item-5 result.** At that point the leading term is of order $\lambda^{10}$ or higher (odd orders vanish), and it is not computed.

*Comparison with (6.14), (6.15).*
- On the background of $b$, the source acts at first order in $\sigma$ and reverses with its sign. $W$ changes by $2\sigma(i-j)^2\lambda^3$, and the derived distance $\alpha(h_i,h_j)=\lambda\lvert i-j\rvert(1-\sigma\lambda)$ changes at relative order $\lambda$. Both depend on $i,j$ only through $\lvert i-j\rvert$.
- On the motion of $b$ there is no effect at first order in $\sigma$, at any order in $\lambda$. The leading weight change is $\propto\sigma^2\lambda^6$ (18.13). It is at relative order $\lambda^4$ with respect to the hopping weight $t^2\lambda^2$, and symmetric between $h_{m\pm1}$.
- The position shift (18.16) comes two orders later, $\propto\sigma^2\lambda^8$. In the bulk it points to smaller index for both signs of $\sigma$. It grows with $m$, i.e. with the start record entering $R_\sigma=K_{h_m}+B_\sigma=mX+\sigma\sigma_y$. The translation-invariant background (6.15) has no such dependence.

The motion is therefore not determined by the background deformation: (18.10) cancels exactly the (6.11)-based guess $\frac{t^2}{12}s_{h\beta}\lambda^5=\frac{\sigma t^2}{6}\lambda^5$.

## Result

- **Reduction (18.1)–(18.3):** the source stays at $\sigma_0$, and $b,c$ evolve under $C^{(\sigma_0)}$. $p_h$ depends on the source only through $D_x(s)=e^{\mathrm iR_\sigma s}(K_x-K_\beta)e^{-\mathrm iR_\sigma s}$, with $R_\sigma=K_\beta+C_c+B_\sigma$.
- **No influence (18.4):** $[B_\sigma-B_{\sigma'},K_h+C_c+B_{\sigma'}]=0$ for all $h$ is sufficient.
  - The condition is A5-invariant, and so is the influence. The separate commutators with $K_h$ and $C_c$ are not.
  - $R_\sigma$, $D_x$, $D_x(s)$ are invariant only up to scalars compensated by $t_{xx}$. $\delta D_x(s)$ and $Y_r^{(x)}$ are invariant.
- **Leading orders (18.6)–(18.9), (18.11):**
  - At $\beta$ and its neighbours, $\delta p_h=O(\lambda^{r+5})$, with coefficient (18.7) ((18.9) for $r=0$).
  - $\delta\bar x=O(\lambda^{r+5})$, with coefficient (18.11).
  - At distance $n\ge2$ the order is $2n+r+2$ (18.6), which needs non-real loop products of shortest walks; otherwise it is $\ge2n+r+3$.
- **2(b) (18.10):** the coefficient is $\frac{\lvert t_{h\beta}\rvert^2}{12}s_{h\beta}$ plus a record-mean term and a $\tau_x$ term, so it is not a function of the (6.11) source part. It equals $\frac{\lvert t_{h\beta}\rvert^2}{12}s_{h\beta}$ iff the sum of the two extra terms vanishes.
- **Locality (Step 7):** order $\lambda^{r+5}$, governed by $Z_r^{(x)}=[\Delta,[J_r,\dots[J_1,K_x-K_\beta]]]$, one order per intermediate cell.
- **Cost (18.12):** no; the influence is independent of the cost difference $\langle B_\sigma-B_{\sigma'}\rangle$.
- **Example (18.13), (18.16):**
  - $\delta p_{h_{m\pm1}}=t^2\sigma^2\lambda^6/45$ and $\delta p_{h_m}=-2t^2\sigma^2\lambda^6/45$.
  - $\delta\bar x=-\frac{\sigma^2t^2}{630}[4m-t^2(\delta_{m,2}-\delta_{m,n-1})]\lambda^8\lvert1\rangle+O(\lambda^{10})$. This is the leading term for every $2\le m\le n-1$, $t>0$, except at the isolated point $m=2<n-1$, $t^2=8$. There its coefficient vanishes; that point is excluded, and its leading term is not computed.
  - The influence is exactly even in $\sigma$. The background effect (6.14), (6.15) is odd in $\sigma$ and depends only on $\lvert i-j\rvert$.

## Consistency checks

1. **Dimensions.** $[t]=[K]=[\Delta]=[J]=[C]=[\lambda]^{-1}$. $p_h$ and $\langle\mathcal N\rangle$ are dimensionless, while $[u_h]=[\bar x]=[K]=[C]$.
   - The coefficient of (18.7) scales as $[C]^{r+5}$ (both terms), and that of (18.6) as $[C]^{2n+r+2}$.
   - Restore a record scale, $K_{h_i}=\mathrm i\kappa X$. In (18.13) this gives $t^2\sigma^2\kappa^2/45\sim[C]^6$.
   - In Step 10 every $\mathsf n$- and $\mathsf a$-step carries a factor $\kappa$. So the $\lambda^8$ coefficient of the dimensionless moment $\delta\langle\mathcal N\rangle$ has the bulk term $\propto m\sigma^2t^2\kappa^4$ (two $\mathsf n$, two $\mathsf a$) and the end term $\propto\sigma^2t^4\kappa^2$ (two $\mathsf n$), both $[C]^8$.
   - The position carries one more factor: $u_{h_i}=\mathrm i\kappa\lvert1\rangle$, so $\delta\bar x=\kappa\,\delta\langle\mathcal N\rangle\lvert1\rangle$. The $\lambda^8$ coefficient of $\delta\bar x$ is $-\frac{\sigma^2t^2\kappa^3}{630}\bigl[4m\kappa^2-t^2(\delta_{m,2}-\delta_{m,n-1})\bigr]\lvert1\rangle$. Its bulk and end terms are $\propto m\sigma^2t^2\kappa^5$ and $\propto\sigma^2t^4\kappa^3$, both $[C]^9=[\bar x]\,[\lambda]^{-8}$. The excluded point reads $t^2=8\kappa^2$.
2. **Limits.**
   - $t\to0$: $p_h=\delta_{h\beta}$ exactly, and every coefficient is $\propto t^2$.
   - $\Delta\propto\mathbb 1$, or (18.4) holds: all $Y_r^{(x)}=0$, and the influence vanishes.
   - $\sigma\to0$ in (18.13), (18.16): zero.
3. **Special cases.**
   - For $C_c=0$ the reduced contract is the 17 contract with records $K_h+B_\sigma$. (17.10) depends on the records only through $d_0(h,\beta)$ and differences of $\epsilon$'s, which are invariant under this common shift. So $\delta p_h^{(4)}=0$, as Step 6 states.
   - The first term of (18.9) agrees with a direct Taylor expansion of $\lVert\Phi\rVert^2$, whose $\lambda^5$ coefficient is $\frac1{12}\operatorname{Im}\langle Q_\beta D_h^2\rangle$.
   - The word calculus of Step 10 applied to $P_1$ at $m=2$ (word $\mathsf t\mathsf n\sigma\sigma\mathsf n\mathsf t$, value $16\sigma^2t^2$) gives $\delta p_{h_1}^{(6)}=t^2\sigma^2/45$, as in (18.13).
   - The bulk term of (18.16) is the order-$t^2$ part $t^2\,\delta(\lVert\Phi_+\rVert^2-\lVert\Phi_-\rVert^2)$, where $\Phi_d$ belongs to $h=h_{m+d}$.
     - Since $U(s)=A+\mathrm i\vec v\cdot\vec\sigma$ with real $A,\vec v$, $\lVert\Phi_d\rVert^2=(\int A)^2+\lvert\int\vec v\rvert^2$ is independent of $\chi$.
     - Its $\lambda^6$ and $\lambda^8$ coefficients are $\frac1{90}+\frac{\sigma^2}{45}$ and $-\frac1{2520}-\frac{\sigma^2c}{630}-\frac{\sigma^2}{420}$, with $c=\vec q_h\cdot\vec q_\beta=2m(m+d)+\sigma^2$.
     - The $d$-odd part gives $-\frac{2m}{315}\sigma^2t^2$, as in (18.16).

## Open issues

- At $m=2<n-1$ and $t^2=8$ (record scale 1) the $\lambda^8$ coefficient of $\delta\bar x$ vanishes. The leading term there ($\lambda^{10}$ or later) is not computed.
- (18.6), (18.7) give the lowest *possible* orders.
  - Nonzero instances: (18.9) for generic records. For (18.6), a square $\beta,x,y,h$ with $n=2$ gives $\frac16\operatorname{Im}(t_x^*t_y)\operatorname{Im}\langle(K_y-K_x)\Delta\rangle$, where $t_x=t_{hx}t_{x\beta}$ and $t_y=t_{hy}t_{y\beta}$.
  - Exact vanishing conditions beyond these are not classified.
- (18.4) is sufficient, not necessary.

## Methods used

- block decomposition in the conserved source place
- interaction picture, Dyson (time-ordered) expansion
- adjoint expansion and support counting of nested commutators
- simplex and Beta integrals
- Pauli algebra; antiunitary (complex-conjugation) symmetry and a parity argument
- Heisenberg moment expansion, superoperator word counting with selection rules
- closed-walk (light-cone) argument for chain-end corrections
