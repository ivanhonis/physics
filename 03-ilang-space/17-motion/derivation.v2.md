# Motion of a hopping body in the background of a recording medium

- **Subproject:** 03-ilang-space
- **Package:** 17-motion
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-08

## Changes from previous version

- Step 7 (item 3) is extended, as I1 of `verification.md` requires. Item 3 asks for the leading **nonvanishing** orders, and v1 gave only the generic ones. v2 adds:
  - the walk form of $`c_n(h)`$;
  - the general coefficient formula (17.24);
  - the general selection rule for the first nonzero coefficient of $`p_h`$ (17.25), and of $`s^2`$, $`\bar x-u_\beta`$ and $`v`$ (17.26), including cancellations between shortest paths and between background points;
  - the explicit $`\lambda^4`$ coefficients for the case in which the $`\lambda^2`$ and $`\lambda^3`$ coefficients vanish: $`w_4`$, and (17.27).
- The statement that the records "enter first at $`\lambda^4`$" now reads: $`\lambda^4`$ is the earliest possible order. Step 7 also states when this order is attained.
- Result item 3 and the first "Open issues" bullet are updated to match.
- All other steps are unchanged. Equations (17.1)–(17.23) keep their tags and meanings. New tags: (17.24)–(17.27).

## Response to verification

- I1: Accepted and fixed in Step 7. (17.25) gives the leading term of $`p_h`$ at the first $`n_h`$ with $`c_n(h)\neq0`$. This covers the interference case $`(t^n)_{h\beta}=0`$. (17.26) gives the leading orders of $`s^2`$, $`\bar x-u_\beta`$ and $`v`$ through the set $`D`$ of reached places at another background point. The leading order of $`s^2`$ is $`\lambda^m`$, with a strictly positive coefficient, and $`\bar x`$ starts at the first nonzero $`w_N`$, $`N\ge m`$. Step 7 gives $`w_4`$ for the case $`w_2=w_3=0`$, and (17.27) for the case in which all neighbours of $`\beta`$ lie at $`u_\beta`$. The $`\lambda^4`$ record onset is now called the earliest possible order, together with the condition under which it is attained. The three-place example of I1 has $`n_2=2`$, $`c_2(2)=t^2\chi`$, $`D=\{2\}`$ and $`m=4`$. For it, (17.25)–(17.27) give exactly the values stated in I1: $`p_2\sim t^4\lambda^4/4`$, $`\bar x-u_0\sim\tfrac{t^4\lambda^4}{4}e`$, $`v\sim t^4\lambda^3e`$ and $`s^2\sim\tfrac{t^4\lambda^4}{4}\lVert e\rVert^2`$.

## Setup and assumptions

- Objects: body $`b`$ (type $`T`$, places $`h\in H_T`$, $`d_T\ge2`$) and medium $`c`$, each the only instance of its type. $`\mathcal H=\mathcal H_T\otimes\mathcal H_c`$ is finite-dimensional (A1), except in the chain limit of Step 9.
- Contract: $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, $`C_b=\sum_{h,h'}t_{hh'}\lvert h\rangle\langle h'\rvert`$, $`t_{hh'}=t_{h'h}^*`$, $`K_h=K_h^\dagger`$, all independent of $`\lambda`$ (A5). $`t`$ is the matrix $`(t_{hh'})`$ and $`(t^n)_{hh'}`$ are the entries of its powers (diagonal included). $`E`$ is the set of edges $`\{h,h'\}`$ ($`h\ne h'`$, $`t_{hh'}\neq0`$) of the hopping graph. Start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$, $`\lambda\ge0`$.
- Notation: $`\langle X\rangle=\langle\chi\vert X\vert\chi\rangle`$, $`\epsilon_h:=\langle K_h\rangle`$, $`\lvert u_h\rangle=(K_h-\epsilon_h)\lvert\chi\rangle`$, so $`\langle\chi\vert u_h\rangle=0`$, and $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$. $`\mathcal H_c`$ carries $`g(v,w)=\mathrm{Re}\langle v\vert w\rangle`$ with norm $`\lVert\cdot\rVert`$.
- Inputs: (2.1) and (2.2) give $`\lvert\Psi\rangle=\sum_h\lvert h\rangle\otimes\lvert\psi_h\rangle`$, $`(V_b)_{hh'}=\langle\psi_{h'}\vert\psi_h\rangle`$ and $`p_h=\lVert\psi_h\rVert^2`$. (2.11) gives $`W(h,h')=\lvert(V_b)_{hh'}\rvert^2/(p_hp_{h'})`$. (11.6), (11.8) and (11.10) give $`d_0`$ in the setting of 11. (5.10) and (5.11) give the background $`(H_T/{\sim_0},d_0)\cong(\{u_h\},\lVert\cdot\rVert)\subset(\mathcal H_c,g)`$.
- Convention: $`W(h,h';\lambda)\,p_hp_{h'}`$ stands for $`\lvert(V_b)_{hh'}\rvert^2`$. This expression is also defined when $`p_hp_{h'}=0`$, and then it vanishes by Cauchy–Schwarz.
- Items 1(a) and 3 are statements for $`\lambda\to0^+`$; items 2, 4 and 5 are exact.

## Derivation

### Step 1. Branch equations

Inserting (2.1) into (1.9) and projecting on $`\langle h\rvert\otimes\mathbb 1_c`$:

```math
i\,\frac{\mathrm d}{\mathrm d\lambda}\lvert\psi_h\rangle=\sum_{h'}t_{hh'}\lvert\psi_{h'}\rangle+K_h\lvert\psi_h\rangle,\qquad \lvert\psi_h(0)\rangle=\phi_h\lvert\chi\rangle .
\tag{17.1}
```

### Step 2. Item 1(a): the background does not depend on the hopping

The setting is that of 11 with $`A=\{b\}`$, $`\bar A=\{c\}`$, $`C_A=C_b`$, $`C_{\bar A}=0`$ and $`C_\partial=\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$. Each $`A_n=\lvert h\rangle\langle h\rvert`$ is diagonal and $`B_n=K_h`$. The two types differ, so no type has objects on both sides of the cut. By (11.8) and (11.10), for a start with all $`\phi_h\neq0`$:

```math
d_0(h,h')=\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=\bigl\lVert u_h-u_{h'}\bigr\rVert,\qquad u_h=(K_h-\epsilon_h)\chi,\quad\text{independent of the }t_{hh'} .
\tag{17.2}
```

The reason is visible in (17.1): $`\psi_h/\phi_h=\chi-i\lambda(\tau_h+K_h)\chi+O(\lambda^2)`$ with the scalar $`\tau_h=\sum_{h'}t_{hh'}\phi_{h'}/\phi_h`$. At first order the hopping adds only a multiple of $`\chi`$, and $`Q_\chi`$ removes it in (11.6). **Answer: no.** The background is that of the pure recording contract (5.10)–(5.11).

### Step 3. Item 1(b): well-definedness and two identities

(i) $`b`$ and $`c`$ are the only instances of their types, so Law 5 creates no ambiguity. The places are part of the type (A2).
(ii) The $`p_h(\lambda)`$ are diagonal elements of the view, so they are invariant under (1.2).
(iii) The partial matrix elements of $`C`$ are $`(\langle h\rvert\otimes\mathbb 1)C(\lvert h'\rangle\otimes\mathbb 1)=t_{hh'}\mathbb 1`$ for $`h\neq h'`$ and $`t_{hh}\mathbb 1+K_h`$ for $`h=h'`$. So $`C`$ fixes $`K_h`$ only up to $`K_h\to K_h+c_h\mathbb 1`$ (with $`t_{hh}\to t_{hh}-c_h`$), and $`u_h`$ is invariant under this change.
(iv) The phase split of the start, $`\phi\otimes\chi=(e^{-i\varphi}\phi)\otimes(e^{i\varphi}\chi)`$, sends every $`u_h`$ to $`e^{i\varphi}u_h`$. This is one common real-linear isometry of $`(\mathcal H_c,g)`$, the same freedom that the embedding (5.11) already carries.

Hence $`s`$ is well defined. $`\bar x`$ and $`v`$ are well defined up to the common isometry $`e^{i\varphi}`$, which acts on them and on the background points $`u_h`$ together. Every $`g`$-invariant built from $`\bar x,v,u_h`$ is well defined, e.g. $`\lVert\bar x-u_h\rVert`$, $`\lVert v\rVert`$ and $`g(v,u_h-u_{h'})`$. The weights $`p_h`$ are analytic in $`\lambda`$ (finite dimension), so $`v`$ exists.

The identities follow from $`\sum_hp_h=1`$ and $`\sum_hp_h(u_h-\bar x)=0`$. First expand $`\sum_hp_h\lVert(u_h-\bar x)+(\bar x-u_k)\rVert^2`$. Then use $`\sum_{h,h'}p_hp_{h'}\lVert u_h-u_{h'}\rVert^2=2\sum_hp_h\lVert u_h\rVert^2-2\lVert\bar x\rVert^2=2s^2`$:

```math
\bigl\lVert\bar x(\lambda)-u_k\bigr\rVert^2=\sum_hp_h(\lambda)\,d_0(h,k)^2-s(\lambda)^2,\qquad
s(\lambda)^2=\frac12\sum_{h,h'}p_h(\lambda)\,p_{h'}(\lambda)\,d_0(h,h')^2 .
\tag{17.3}
```

### Step 4. Item 2(a): currents

By (17.1), $`\dot p_h=2\mathrm{Re}\langle\psi_h\vert\dot\psi_h\rangle=2\mathrm{Im}\bigl[\sum_{h'}t_{hh'}\langle\psi_h\vert\psi_{h'}\rangle+\langle\psi_h\vert K_h\vert\psi_h\rangle\bigr]`$. The last term is real, so its imaginary part vanishes. With $`\langle\psi_h\vert\psi_{h'}\rangle=(V_b)_{h'h}`$ (2.2):

```math
\frac{\mathrm dp_h}{\mathrm d\lambda}=\sum_{h'}J_{h'\to h},\qquad J_{h'\to h}(\lambda):=2\mathrm{Im}\bigl[t_{hh'}\,(V_b(\lambda))_{h'h}\bigr]=-J_{h\to h'} .
\tag{17.4}
```

Antisymmetry: $`t=t^\dagger`$ and $`V_b=V_b^\dagger`$ give $`t_{h'h}(V_b)_{hh'}=\bigl(t_{hh'}(V_b)_{h'h}\bigr)^*`$. Hence $`J_{h\to h}=0`$, and $`J_{h'\to h}=0`$ off the edges. The $`K_h`$ enter only through the coherences $`(V_b)_{h'h}`$.

### Step 5. Item 2(b): bound on the current

$`\lvert\mathrm{Im}z\rvert\le\lvert z\rvert`$ and (2.11) give

```math
\lvert J_{h'\to h}(\lambda)\rvert\le2\lvert t_{hh'}\rvert\sqrt{W(h,h';\lambda)\,p_h(\lambda)\,p_{h'}(\lambda)}\;\le\;2\lvert t_{hh'}\rvert\sqrt{p_hp_{h'}} .
\tag{17.5}
```

The first bound is attained when $`t_{hh'}(V_b)_{h'h}`$ is purely imaginary. If an edge is completely witnessed ($`W=0`$), no current flows across it.

### Step 6. Item 2(c): velocity and maximal speed

From $`v=\sum_h\dot p_hu_h=\sum_{h,h'}J_{h'\to h}u_h`$, symmetrize with (17.4): $`v=\tfrac12\sum_{h,h'}J_{h'\to h}(u_h-u_{h'})`$. Each edge contributes twice with the same term:

```math
v(\lambda)=\sum_{\{h,h'\}\in E}2\mathrm{Im}\bigl[t_{hh'}(V_b(\lambda))_{h'h}\bigr]\,(u_h-u_{h'}) .
\tag{17.6}
```

Each term is independent of the orientation of its edge. Only edges with $`d_0(h,h')>0`$ contribute.

For the bound, let $`a_{hh'}:=\lvert t_{hh'}\rvert d_0(h,h')`$. This matrix is real, symmetric and nonnegative, and it vanishes off $`E`$. Let $`q_h:=\sqrt{p_h}`$, so that $`\sum_hq_h^2=1`$. Use the triangle inequality, (17.5), the Rayleigh quotient, and the standard bound "largest eigenvalue $`\le`$ maximal row sum" for nonnegative matrices:

```math
\lVert v(\lambda)\rVert\le\sum_{\{h,h'\}\in E}2\lvert t_{hh'}\rvert d_0(h,h')\sqrt{W(h,h';\lambda)p_hp_{h'}}\le\sum_{h,h'}a_{hh'}q_hq_{h'}\le v_{\max}:=\varrho(a)\le\max_h\sum_{h'}\lvert t_{hh'}\rvert\,d_0(h,h') .
\tag{17.7}
```

Here $`\varrho(a)`$ is the largest eigenvalue of $`a`$. The bound holds for every start and every $`\lambda`$, so $`\lVert\bar x(\lambda_2)-\bar x(\lambda_1)\rVert\le v_{\max}\lvert\lambda_2-\lambda_1\rvert`$.

### Step 7. Item 3: localized start $`\phi=\lvert\beta\rangle`$

The series $`\Psi(\lambda)=\sum_n\frac{(-i\lambda)^n}{n!}C^n(\lvert\beta\rangle\otimes\chi)`$ converges, since $`\mathcal H`$ is finite-dimensional. Define its components $`c_n(h):=(\langle h\rvert\otimes\mathbb 1)C^n(\lvert\beta\rangle\otimes\chi)`$, so that $`\psi_h(\lambda)=\sum_n\frac{(-i\lambda)^n}{n!}c_n(h)`$. They obey $`c_{n+1}(h)=\sum_{h'}t_{hh'}c_n(h')+K_hc_n(h)`$ with $`c_0(h)=\delta_{h\beta}\chi`$. Unrolling this recurrence writes $`c_n(h)`$ as a sum over walks $`\beta=h_0,h_1,\dots,h_n=h`$. Each step of a walk is either a hop along an edge, with factor $`t_{h_{k+1}h_k}`$, or a stay, with operator $`t_{h_kh_k}+K_{h_k}`$. Let $`\mathrm{dist}(h,\beta)`$ be the graph distance. Then $`c_n(h)=0`$ for $`n<\mathrm{dist}(h,\beta)`$. For $`n=\mathrm{dist}(h,\beta)`$ only the walks without stays remain, so $`c_n(h)=(t^n)_{h\beta}\chi`$. For $`h\neq\beta`$:

```math
\begin{aligned}
c_1(h)&=t_{h\beta}\chi,\qquad c_2(h)=(t^2)_{h\beta}\chi+t_{h\beta}(K_h+K_\beta)\chi,\\
\langle\chi\vert c_3(h)\rangle&=(t^3)_{h\beta}+\sum_{h'}t_{hh'}t_{h'\beta}(\epsilon_h+\epsilon_{h'}+\epsilon_\beta)+t_{h\beta}\langle K_h^2+K_hK_\beta+K_\beta^2\rangle .
\end{aligned}
\tag{17.8}
```

Inserting the series into $`p_h=\lVert\psi_h\rVert^2`$ gives an entire function of $`\lambda`$:

```math
p_h(\lambda)=\sum_{N\ge0}p_h^{(N)}\lambda^N,\qquad p_h^{(N)}=\sum_{k+l=N}\frac{i^k(-i)^l}{k!\,l!}\,\bigl\langle c_k(h)\big\vert c_l(h)\bigr\rangle .
\tag{17.24}
```

For $`h\neq\beta`$ we have $`c_0(h)=0`$, and so $`p_h^{(2)}=\lVert c_1\rVert^2`$, $`p_h^{(3)}=\mathrm{Im}\langle c_1\vert c_2\rangle`$ and $`p_h^{(4)}=\tfrac14\lVert c_2\rVert^2-\tfrac13\mathrm{Re}\langle c_1\vert c_3\rangle`$. In the $`\lambda^3`$ term, $`\mathrm{Im}[\lvert t_{h\beta}\rvert^2(\epsilon_h+\epsilon_\beta)]=0`$. Hence, for every $`h\neq\beta`$ (for non-neighbours of $`\beta`$ the first two coefficients vanish, and $`p_h^{(4)}=\tfrac14\lvert(t^2)_{h\beta}\rvert^2`$):

```math
p_h(\lambda)=\lambda^2\lvert t_{h\beta}\rvert^2+\lambda^3\mathrm{Im}\bigl[t_{h\beta}^*(t^2)_{h\beta}\bigr]+\lambda^4p_h^{(4)}+O(\lambda^5),\qquad p_\beta=1-\sum_{h\neq\beta}p_h .
\tag{17.9}
```

The $`\lambda^3`$ terms cancel in $`p_\beta`$: their sum is $`\mathrm{Im}\bigl[(t^3)_{\beta\beta}-t_{\beta\beta}(t^2)_{\beta\beta}\bigr]=0`$, because $`t=t^\dagger`$.

**Leading nonvanishing order of $`p_h`$.** For $`h\neq\beta`$ let $`n_h:=\min\{n:c_n(h)\neq0\}`$. Then $`n_h=\infty`$ iff $`p_h\equiv0`$. In (17.24), every term with $`N<2n_h`$ contains a factor $`c_k(h)=0`$. At $`N=2n_h`$ only the term $`k=l=n_h`$ remains:

```math
p_h(\lambda)=\frac{\lambda^{2n_h}}{(n_h!)^2}\bigl\lVert c_{n_h}(h)\bigr\rVert^2+O(\lambda^{2n_h+1}),\qquad n_h\ge\mathrm{dist}(h,\beta).
\tag{17.25}
```

With $`n:=\mathrm{dist}(h,\beta)`$, we have $`n_h=n`$ iff $`(t^n)_{h\beta}\neq0`$, and then the coefficient is $`\lvert(t^n)_{h\beta}\rvert^2/(n!)^2`$. If the shortest paths cancel, $`(t^n)_{h\beta}=0`$, and the recurrence must be continued until $`c_n(h)\neq0`$. For $`\beta`$ itself, (17.9) gives $`1-p_\beta=\lambda^2\sum_h\lvert t_{h\beta}\rvert^2+O(\lambda^4)`$. This is the leading order unless $`\beta`$ has no neighbour; in that case $`p_\beta\equiv1`$.

**Order at which the records enter.** By (17.24), $`p_h^{(N)}`$ with $`N\le2\mathrm{dist}(h,\beta)`$ involves only $`c_{\mathrm{dist}(h,\beta)}(h)=(t^{\mathrm{dist}(h,\beta)})_{h\beta}\chi`$, so it is independent of the $`K_h`$. At graph distance $`n\ge2`$, the $`K_h`$ therefore enter $`p_h`$ not before $`\lambda^{2n+1}`$. For $`\beta`$ and its neighbours, the $`\lambda^2`$ and $`\lambda^3`$ coefficients in (17.9) are independent of the $`K_h`$, for every choice of the $`K_h`$. The earliest possible order at which the records enter is therefore $`\lambda^4`$, both in $`p_\beta`$ and in the neighbours of $`\beta`$. Evaluate the $`\lambda^4`$ coefficient with (17.8). Use $`\mathrm{Re}\langle K_hK_\beta\rangle=\tfrac12\langle K_hK_\beta+K_\beta K_h\rangle`$ and the orthogonal split $`(K_h-K_\beta)\chi=(\epsilon_h-\epsilon_\beta)\chi+(u_h-u_\beta)`$:

```math
p_h^{(4)}=\underbrace{\tfrac14\lvert(t^2)_{h\beta}\rvert^2-\tfrac13\mathrm{Re}\bigl[t^*_{h\beta}(t^3)_{h\beta}\bigr]}_{K\text{-independent}}
\;\underbrace{-\;\tfrac{1}{12}\lvert t_{h\beta}\rvert^2d_0(h,\beta)^2}_{\text{record spread}}
\;\underbrace{-\;\tfrac{1}{12}\lvert t_{h\beta}\rvert^2(\epsilon_h-\epsilon_\beta)^2+\tfrac16\sum_{h'}\mathrm{Re}\bigl(t^*_{h\beta}t_{hh'}t_{h'\beta}\bigr)(\epsilon_h+\epsilon_\beta-2\epsilon_{h'})}_{\text{record means}} .
\tag{17.10}
```

The quadratic terms combine as $`\tfrac14\langle(K_h+K_\beta)^2\rangle-\tfrac13\mathrm{Re}\langle K_h^2+K_hK_\beta+K_\beta^2\rangle=-\tfrac1{12}\langle(K_h-K_\beta)^2\rangle`$. The linear terms come from $`\tfrac12\mathrm{Re}[t^*_{h\beta}(t^2)_{h\beta}](\epsilon_h+\epsilon_\beta)`$ and $`-\tfrac13\sum_{h'}\mathrm{Re}(t^*_{h\beta}t_{hh'}t_{h'\beta})(\epsilon_h+\epsilon_{h'}+\epsilon_\beta)`$. The "means" part is exactly the change of the $`K`$-independent part under the shift $`t_{hh}\to t_{hh}+\epsilon_h`$. The genuine record part, $`-\tfrac1{12}\lvert t_{h\beta}\rvert^2d_0(h,\beta)^2\le0`$, slows the transfer to neighbours that lie at a different background point. For $`p_\beta`$, the $`K`$-dependent part is minus the sum of these parts over $`h\neq\beta`$. The records actually enter at $`\lambda^4`$ iff the $`K`$-dependent part of (17.10) is nonzero for some $`h\neq\beta`$. It vanishes, for example, when $`K_h\chi=K_\beta\chi`$ for all neighbours $`h`$ of $`\beta`$. Otherwise the records first enter at a higher order, which is read off from (17.24).

**Position, spread, velocity.** Write $`\bar x-u_\beta=\sum_{h\neq\beta}p_h(u_h-u_\beta)=\sum_N\lambda^Nw_N`$ with $`w_N:=\sum_hp_h^{(N)}(u_h-u_\beta)`$, and insert (17.9). For $`s^2`$, use (17.3) with $`k=\beta`$, i.e. $`s^2=\sum_hp_hd_0(h,\beta)^2-\lVert\bar x-u_\beta\rVert^2`$, where $`\lVert\bar x-u_\beta\rVert^2=O(\lambda^4)`$:

```math
\bar x(\lambda)-u_\beta=\lambda^2w_2+\lambda^3w_3+O(\lambda^4),\qquad w_2=\sum_h\lvert t_{h\beta}\rvert^2(u_h-u_\beta),\quad w_3=\sum_h\mathrm{Im}\bigl[t^*_{h\beta}(t^2)_{h\beta}\bigr](u_h-u_\beta),
\tag{17.11}
```

```math
v(\lambda)=2\lambda\,w_2+3\lambda^2w_3+O(\lambda^3),\qquad v(0)=0,
\tag{17.12}
```

```math
s(\lambda)^2=\lambda^2\sum_h\lvert t_{h\beta}\rvert^2\,d_0(h,\beta)^2+O(\lambda^3).
\tag{17.13}
```

**Leading nonvanishing orders in general.** Only reached places at a background point other than $`u_\beta`$ contribute to $`w_N`$ and to $`\sum_hp_hd_0(h,\beta)^2`$. Call their set $`D:=\{h:n_h<\infty,\ u_h\neq u_\beta\}`$ and let $`m:=\min_{h\in D}2n_h\ge2`$. By (17.25), $`w_N=0`$ for $`N<m`$. The sum $`\sum_hp_hd_0(h,\beta)^2`$ of nonnegative terms starts at $`\lambda^m`$ with a positive coefficient, while $`\lVert\bar x-u_\beta\rVert^2=O(\lambda^{2m})`$ and $`2m>m`$. Since $`\bar x`$ is entire in $`\lambda`$:

```math
\begin{aligned}
s(\lambda)^2&=\lambda^m\sum_{h\in D,\;2n_h=m}\frac{\lVert c_{n_h}(h)\rVert^2}{(n_h!)^2}\,d_0(h,\beta)^2+O(\lambda^{m+1}),\\
\bar x(\lambda)-u_\beta&=\lambda^{N_0}w_{N_0}+O(\lambda^{N_0+1}),\qquad v(\lambda)=N_0\,\lambda^{N_0-1}w_{N_0}+O(\lambda^{N_0}),\qquad N_0:=\min\{N:w_N\neq0\}\ge m,
\end{aligned}
\tag{17.26}
```

with $`w_m=\sum_{h\in D,\,2n_h=m}\lVert c_{n_h}(h)\rVert^2(n_h!)^{-2}(u_h-u_\beta)`$. If $`D=\emptyset`$, then $`s\equiv0`$, $`\bar x\equiv u_\beta`$ and $`v\equiv0`$. If $`w_N=0`$ for all $`N`$, then $`\bar x\equiv u_\beta`$ and $`v\equiv0`$. The vector $`w_m`$ can vanish through cancellation between different background points. In that case $`N_0>m`$, and $`w_{N_0}`$ follows from (17.24). The low orders are explicit:

- $`m=2`$, i.e. some neighbour of $`\beta`$ lies at another background point (the generic case). The coefficient in (17.13) is positive. If $`w_2\neq0`$, then $`N_0=2`$. Otherwise $`N_0=3`$ if $`w_3\neq0`$. Otherwise $`N_0\ge4`$, with $`w_4=\sum_hp_h^{(4)}(u_h-u_\beta)`$ and $`p_h^{(4)}`$ from (17.10) for every $`h\neq\beta`$.
- $`m>2`$, i.e. all neighbours of $`\beta`$ lie at $`u_\beta`$. Then $`w_2=w_3=0`$, and the coefficient in (17.13) vanishes. We have $`m=4`$ iff some $`h`$ with $`(t^2)_{h\beta}\neq0`$ has $`u_h\neq u_\beta`$. In this case only non-neighbours contribute, with $`p_h^{(4)}=\tfrac14\lvert(t^2)_{h\beta}\rvert^2`$, and $`v=\lambda^3\sum_h\lvert(t^2)_{h\beta}\rvert^2(u_h-u_\beta)+O(\lambda^4)`$:

```math
\bar x(\lambda)-u_\beta=\frac{\lambda^4}{4}\sum_h\lvert(t^2)_{h\beta}\rvert^2(u_h-u_\beta)+O(\lambda^5),\qquad s(\lambda)^2=\frac{\lambda^4}{4}\sum_h\lvert(t^2)_{h\beta}\rvert^2d_0(h,\beta)^2+O(\lambda^5).
\tag{17.27}
```

In the generic case ($`m=2`$, $`w_2\neq0`$), the leading orders are $`\lambda^2`$ for $`\bar x-u_\beta`$, $`\lambda`$ for $`v`$ and $`\lambda^2`$ for $`s^2`$. In (17.11)–(17.13) and (17.27), the records act only through the positions $`u_h`$. Their effect on the weights can first move $`\bar x`$ at $`\lambda^4`$ (and $`v`$ at $`\lambda^3`$). The record-spread part of this effect is $`-\tfrac{\lambda^4}{12}\sum_h\lvert t_{h\beta}\rvert^2d_0(h,\beta)^2(u_h-u_\beta)`$.

### Step 8. Item 4: commuting records

Let $`D_j:=\sum_h\kappa_h(j)\lvert h\rangle\langle h\rvert`$. Then $`C=\sum_j(C_b+D_j)\otimes P_j`$. The $`P_j`$ are orthogonal projectors with $`\sum_jP_j=\mathbb 1`$, so $`e^{-iC\lambda}=\sum_jU_j(\lambda)\otimes P_j`$ and $`\Psi(\lambda)=\sum_jU_j\phi\otimes P_j\chi`$. The partial trace over $`c`$ kills the cross terms, since $`P_{j'}P_j=\delta_{jj'}P_j`$:

```math
V_b(\lambda)=\sum_jw_j\,U_j(\lambda)\lvert\phi\rangle\langle\phi\rvert U_j(\lambda)^\dagger,\qquad U_j(\lambda)=e^{-i(C_b+D_j)\lambda},\qquad w_j=\langle\chi\vert P_j\vert\chi\rangle .
\tag{17.14}
```

The view is the $`w_j`$-weighted mixture of record-free hopping evolutions with on-site terms $`\kappa_h(j)`$.

### Step 9. Item 5: the chain, its background and the limit

Let $`e:=(X-\langle X\rangle)\chi`$, so $`\lVert e\rVert=\sigma_X>0`$. Then $`u_{h_m}=m\,e`$, and

```math
d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X,\qquad \bar x=\bar m\,e,\quad \bar m:=\sum_mm\,p_{h_m},\qquad s^2=\sigma_X^2\sum_m(m-\bar m)^2p_{h_m} .
\tag{17.15}
```

The background is an equally spaced line of distinct points. Item 4 applies with $`P_j\to\Pi_\xi`$, $`w_\xi=\langle\chi\vert\Pi_\xi\vert\chi\rangle`$ (finitely many $`\xi`$, since $`\mathcal H_c`$ is finite) and $`D_\xi=\xi M`$, where $`M:=\sum_mm\lvert h_m\rangle\langle h_m\rvert`$.

**Limit.** Take the finite chains $`\{h_{-L},\dots,h_L\}`$, with $`C_b`$ and $`K_{h_m}`$ restricted to them. Let $`L\to\infty`$ at fixed $`\lambda`$. In the interaction picture with respect to the diagonal $`\xi M`$, each $`U_\xi`$ is a Dyson series in the hopping. Its $`n`$-th term has norm $`\le(2t\lambda)^n/n!`$ and moves a place by at most $`n`$ steps. For starts supported on $`\{h_0,h_1\}`$, terms of order $`<L`$ do not feel the ends. So the finite and infinite amplitudes differ by at most $`2\sum_{n\ge L}(2t\lambda)^n/n!\to0`$. The amplitude at $`h_m`$ is bounded by $`2\sum_{n\ge\lvert m\rvert-1}(2t\lambda)^n/n!`$ uniformly in $`L`$. By dominated convergence, $`p_{h_m}`$, $`\bar m`$, $`s^2`$ and $`v`$ converge to their values on $`\ell^2(\mathbb Z)`$. There $`S:=\sum_m\lvert h_m\rangle\langle h_{m+1}\rvert`$ is unitary and $`C_b=t(S+S^\dagger)`$.

**Standard results (Wannier–Stark chain).** $`[M,S]=-S`$ gives $`e^{i\xi M\lambda}Se^{-i\xi M\lambda}=e^{-i\xi\lambda}S`$. The interaction-picture generators commute, so $`U_\xi=e^{-i\xi M\lambda}\exp\bigl[-it(\zeta S+\zeta^*S^\dagger)\bigr]`$ with $`\zeta=\int_0^\lambda e^{-i\xi\lambda'}\mathrm d\lambda'`$. The Bessel generating function $`e^{(z/2)(w-w^{-1})}=\sum_nJ_n(z)w^n`$ then gives

```math
\langle h_m\vert U_\xi(\lambda)\vert h_k\rangle=e^{-i\xi\lambda(m+k)/2}\,(-i)^{m-k}J_{m-k}\bigl(z_\xi(\lambda)\bigr),\qquad z_\xi(\lambda)=\frac{4t}{\xi}\sin\frac{\xi\lambda}{2}\quad(z_0=2t\lambda).
\tag{17.16}
```

Heisenberg equations: $`\tfrac{\mathrm d}{\mathrm d\lambda}S_H=-i\xi S_H`$, so $`S_H=e^{-i\xi\lambda}S`$, and $`\tfrac{\mathrm d}{\mathrm d\lambda}M_H=it(S_H-S_H^\dagger)`$. Integrating,

```math
U_\xi^\dagger M\,U_\xi=M+\frac{t}{\xi}\Bigl[(1-e^{-i\xi\lambda})S+(1-e^{i\xi\lambda})S^\dagger\Bigr]\qquad(\xi=0:\ M+it\lambda(S-S^\dagger)).
\tag{17.17}
```

### Step 10. Item 5(a): start $`\lvert h_0\rangle\otimes\lvert\chi\rangle`$

By (17.14) and (17.16):

```math
p_{h_m}(\lambda)=\sum_\xi w_\xi\,J_m\bigl(z_\xi(\lambda)\bigr)^2 .
\tag{17.18}
```

Since $`J_{-m}^2=J_m^2`$, we get $`\bar m=0`$. By (17.17), $`\sum_mm^2p_{h_m}=\sum_\xi w_\xi\lVert U_\xi^\dagger MU_\xi h_0\rVert^2=\sum_\xi w_\xi\tfrac{2t^2}{\xi^2}\lvert1-e^{i\xi\lambda}\rvert^2`$. Hence

```math
\bar x(\lambda)=u_{h_0}=0,\qquad s(\lambda)^2=4t^2\sigma_X^2\sum_\xi w_\xi\,\frac{1-\cos\xi\lambda}{\xi^2}\qquad\Bigl(\xi=0\text{ term: }\tfrac{\lambda^2}{2}\Bigr).
\tag{17.19}
```

The bound (17.7) for this chain: $`a=t\sigma_X(S+S^\dagger)`$, whose largest spectral value and row sum are both $`2t\sigma_X`$. On the finite chain the bound is $`2t\sigma_X\cos\frac{\pi}{2L+2}`$:

```math
v_{\max}=2t\,\sigma_X .
\tag{17.20}
```

For this start, $`v\equiv0`$.

### Step 11. Item 5(b): start $`2^{-1/2}(\lvert h_0\rangle+e^{i\theta}\lvert h_1\rangle)\otimes\lvert\chi\rangle`$

Here $`\langle\phi\vert M\vert\phi\rangle=\tfrac12`$ and $`\langle\phi\vert S\vert\phi\rangle=\tfrac12e^{i\theta}`$. By (17.14), $`\bar m=\sum_\xi w_\xi\langle\phi\vert U_\xi^\dagger MU_\xi\vert\phi\rangle`$, and with (17.17):

```math
\bar x(\lambda)=\Bigl[\frac12+t\sum_\xi w_\xi\,\frac{\cos\theta-\cos(\theta-\xi\lambda)}{\xi}\Bigr]e\qquad\bigl(\xi=0\text{ term: }-\lambda\sin\theta\bigr),
\tag{17.21}
```

```math
v(\lambda)=t\sum_\xi w_\xi\sin(\xi\lambda-\theta)\;e=t\,\mathrm{Im}\Bigl[e^{-i\theta}\langle\chi\vert e^{iX\lambda}\vert\chi\rangle\Bigr]\,(X-\langle X\rangle)\lvert\chi\rangle .
\tag{17.22}
```

Hence $`\lVert v\rVert\le t\sigma_X=v_{\max}/2`$. At $`\lambda=0`$, (17.22) agrees with (17.6): $`J_{h_0\to h_1}=2\mathrm{Im}[t\cdot\tfrac12e^{-i\theta}]=-t\sin\theta`$.

### Step 12. Item 5(c): bounded spread

Every term of (17.19) is nonnegative. A term with $`\xi\neq0`$ is at most $`2w_\xi/\xi^2`$, while the $`\xi=0`$ term $`w_0\lambda^2/2`$ is unbounded iff $`w_0>0`$. Therefore

```math
\sup_\lambda s(\lambda)<\infty\iff\Pi_0\lvert\chi\rangle=0\ \ (\text{i.e. }\chi\perp\ker X),\qquad\text{then}\quad s^2\le8t^2\sigma_X^2\sum_{\xi\neq0}\frac{w_\xi}{\xi^2},\quad \Bigl\lVert\bar x_{(b)}-\tfrac12e\Bigr\rVert\le2t\sigma_X\sum_{\xi\ne0}\frac{w_\xi}{\lvert\xi\rvert}.
\tag{17.23}
```

The last bound follows from (17.21), since each term with $`\xi\neq0`$ is at most $`2w_\xi/\lvert\xi\rvert`$. If $`0\notin\mathrm{spec}X`$, the condition holds automatically. **Answer:** under this condition, $`\bar x(\lambda)`$ of (b) stays bounded (it is quasi-periodic).

## Result

- **1(a)** No: $`d_0`$ is independent of the $`t_{hh'}`$ (17.2).
- **1(b)** $`s`$ is well defined. $`\bar x`$ and $`v`$ are well defined up to the common isometry $`e^{i\varphi}`$ of the background embedding, so all their $`g`$-invariants are well defined. Identities (17.3).
- **2** Continuity equation with antisymmetric current $`J_{h'\to h}=2\mathrm{Im}[t_{hh'}(V_b)_{h'h}]`$ (17.4). Current bound $`\lvert J_{h'\to h}\rvert\le2\lvert t_{hh'}\rvert\sqrt{Wp_hp_{h'}}`$ (17.5). Velocity (17.6). Maximal speed $`\lVert v\rVert\le\varrho(\lvert t_{hh'}\rvert d_0(h,h'))\le\max_h\sum_{h'}\lvert t_{hh'}\rvert d_0(h,h')`$ (17.7).
- **3** All coefficients of $`p_h`$ (17.24), with low orders (17.9)–(17.10).
  - Leading nonvanishing orders in general: $`p_h\sim\lambda^{2n_h}\lVert c_{n_h}(h)\rVert^2/(n_h!)^2`$ (17.25); $`s^2\sim\lambda^m`$ with a positive coefficient, and $`\bar x-u_\beta\sim\lambda^{N_0}w_{N_0}`$, $`v\sim N_0\lambda^{N_0-1}w_{N_0}`$, $`N_0\ge m`$ (17.26).
  - Generic case $`m=2`$: (17.11)–(17.13), with $`w_4`$ from (17.10) if $`w_2=w_3=0`$. All neighbours of $`\beta`$ at $`u_\beta`$: (17.27).
  - The $`K_h`$ can enter $`p_h`$ at the earliest at $`\lambda^4`$, with $`K`$-dependent coefficient (17.10); the genuine record part is $`-\tfrac1{12}\lvert t_{h\beta}\rvert^2d_0(h,\beta)^2`$. They enter at $`\lambda^4`$ iff that part is nonzero for some $`h\neq\beta`$. At graph distance $`n\ge2`$ they enter not before $`\lambda^{2n+1}`$.
- **4** Closed form (17.14).
- **5** $`p_{h_m}`$ (17.18); $`\bar x=0`$ and $`s^2`$ (17.19); bound $`2t\sigma_X`$ (17.20); $`\bar x`$ and $`v`$ (17.21)–(17.22). Spread bounded iff $`\Pi_0\chi=0`$, and then $`\bar x`$ of (b) is bounded (17.23).

## Consistency checks

1. **Dimensions and conservation.** $`[t]=[K]=[\lambda]^{-1}`$, so $`[u_h]=[d_0]=[\lambda]^{-1}`$, as $`d_0=\lim\alpha/\lambda`$ requires. Further, $`[v]=[\lambda]^{-2}=[t\,d_0]`$ in (17.7), $`\lambda^4\lvert t\rvert^2d_0^2`$ in (17.10) is dimensionless, and so is $`z_\xi`$. By antisymmetry, $`\sum_h\dot p_h=\sum_{h,h'}J_{h'\to h}=0`$. The $`\lambda^3`$ terms of (17.9) cancel in $`p_\beta`$.
2. **Trivial limits.** No hopping: $`J=0`$, $`v=0`$, $`v_{\max}=0`$, and all coefficients in (17.9)–(17.13) vanish, consistent with $`p_h=\delta_{h\beta}`$. All $`K_h=K`$ equal: the two terms of $`C=C_b\otimes\mathbb 1+\mathbb 1\otimes K`$ commute, so the state stays a product and the view is record-free. Accordingly $`d_0=0`$, $`v_{\max}=0`$, $`\bar x`$ is constant, and the $`K`$-dependent part of (17.10) vanishes.
3. **Item 3 against item 5.** Expanding (17.18) for $`m=1`$ with $`J_1^2=z^2/4-z^4/16+\dots`$ and $`z_\xi=2t\lambda-t\xi^2\lambda^3/12+\dots`$ gives $`p_{h_1}=t^2\lambda^2-\bigl(t^4+\tfrac{t^2}{12}\langle X^2\rangle\bigr)\lambda^4+O(\lambda^6)`$. (17.10) gives the same result, with $`(t^2)_{h_1h_0}=0`$, $`(t^3)_{h_1h_0}=3t^3`$, no common neighbour and $`d_0^2+(\epsilon_1-\epsilon_0)^2=\sigma_X^2+\langle X\rangle^2=\langle X^2\rangle`$.

## Open issues

- Item 3: the rule (17.25)–(17.26) determines the leading nonvanishing order in every case. In closed form, however, the coefficients are given only up to $`\lambda^4`$, through (17.9)–(17.10) and (17.27). Higher coefficients are left as the finite sums (17.24) over the walk vectors $`c_n(h)`$.
- The bound (17.7) is not shown to be attained. In 5(b), $`\lVert v\rVert\le v_{\max}/2`$.
- Position and velocity are measured in the fixed background built from the start $`\chi`$ (Goal definition). How the witness geometry at finite $`\lambda`$ deviates from $`\lambda d_0`$ is not addressed.

## Methods used

- Branch (component) form of the evolution, continuity equation for place weights
- Cauchy–Schwarz, Rayleigh quotient, row-sum bound for nonnegative matrices
- Taylor/Dyson expansion in $`\lambda`$, walk expansion of the Taylor coefficients, leading-order selection for entire functions, partial trace
- Joint spectral decomposition of commuting operators
- Interaction and Heisenberg pictures, Bessel generating function (Wannier–Stark chain)
- Finite-chain limit via Dyson bounds and dominated convergence
