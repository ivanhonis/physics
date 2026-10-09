# Question: 18-mediated-effect

- **Subproject:** 03-ilang-space
- **Package:** 18-mediated-effect
- **Equation tags:** (18.k)
- **Created:** 2026-10-08

## Goal

Determine whether, and how, one body changes the motion of another body through a recording medium. Determine:
- the lowest order in $`\lambda`$ at which the place of the first body enters the place weights of the second, and the coefficient;
- how this order depends on the distance between the two bodies in a medium of cells;
- whether the effect depends on the first body's cost.

The notions defined below (source, moving body, reduced contract, influence) are fixed for later packages. They mean only what their definitions say (M1, M2, M4).

**Setting.**
- **Objects.** All objects have pairwise different types, and each is the only instance of its type, so (1.11) imposes no constraint.
  - A **source** $`s`$ of type $`S`$, with places $`\sigma\in H_S`$.
  - A **moving body** $`b`$ of type $`T`$, with places $`h\in H_T`$ and $`d_T\ge2`$.
  - A medium $`c`$: one object, or in item 3 the cells $`c_1,\dots,c_L`$.
- **Contracts.**
  ```math
  C=\sum_\sigma\lvert\sigma\rangle\langle\sigma\rvert_s\otimes B_\sigma+C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert_b\otimes K_h+C_c ,\qquad C_b=\sum_{h,h'}t_{hh'}\lvert h\rangle\langle h'\rvert ,
  ```
  - $`t_{hh'}=t_{h'h}^*`$; the hopping graph joins $`h\neq h'`$ iff $`t_{hh'}\neq0`$;
  - $`B_\sigma`$ and $`K_h`$ are self-adjoint on $`\mathcal H_c`$;
  - $`C_c`$ is a self-adjoint operator on the medium alone;
  - each term is extended by the identity on the other objects;
  - the source does not hop.

  By A5, $`C_b\otimes\mathbb 1_c`$ and $`C_c`$ are parts of pair terms, and their placement is a convention.
- **Start.** $`\lvert\sigma_0\rangle_s\otimes\lvert\beta\rangle_b\otimes\lvert\chi\rangle_c`$, with a unit vector $`\chi`$.
- **Notation.** $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, $`\tilde X:=X-\langle X\rangle`$, and $`\lvert u_h\rangle:=\tilde K_h\lvert\chi\rangle`$ as in (5.10). $`p_h(\lambda;\sigma_0)`$ are the place weights of the view of $`\{b\}`$ for the start above. The position of $`b`$ in its own background is $`\bar x(\lambda;\sigma_0):=\sum_hp_h(\lambda;\sigma_0)\,u_h`$, as in 17.

**Definition (influence).** For two source places $`\sigma,\sigma'`$, the influence of the source on $`b`$ is
```math
\delta p_h(\lambda):=p_h(\lambda;\sigma)-p_h(\lambda;\sigma'),\qquad \delta\bar x(\lambda):=\bar x(\lambda;\sigma)-\bar x(\lambda;\sigma'),
```
the change of the motion of $`b`$ when the source is moved from $`\sigma'`$ to $`\sigma`$, with everything else fixed.

1. **Reduction.**
   - (a) Determine the exact state. Determine whether the source stays at $`\sigma_0`$, and which contract drives $`b`$ and $`c`$ (the reduced contract).
   - (b) Determine a sufficient condition, in terms of $`B_\sigma-B_{\sigma'}`$, the $`K_h`$ and $`C_c`$, under which $`\delta p_h(\lambda)=0`$ for every $`\lambda`$ and every $`h`$. Determine whether this condition and the influence are invariant under the A5 placement convention.

2. **Leading influence on the motion** ($`C_c=0`$, one medium object).
   - (a) For $`h=\beta`$ and for $`h`$ a neighbour of $`\beta`$ in the hopping graph, determine the lowest order in $`\lambda`$ at which $`\delta p_h`$ can be nonzero, and its coefficient. Determine also the lowest possible order for places at graph distance $`n\ge2`$ from $`\beta`$.
   - (b) For a neighbour $`h`$ of $`\beta`$, compare the coefficient of (a) with the source part of (6.11) for the pair $`(h,\beta)`$, taken with $`B_\sigma-B_{\sigma'}`$ in place of $`B_{\beta_0}`$. Determine whether one is a function of the other.
   - (c) Determine the lowest order at which $`\delta\bar x`$ can be nonzero, and its coefficient.

3. **Locality.** The medium is the chain of cells $`c_1,\dots,c_L`$, with $`C_c=\sum_{k=1}^{L-1}J_k`$ and $`J_k`$ self-adjoint on $`c_kc_{k+1}`$. All $`K_h`$ act on $`c_1`$, the $`B_\sigma`$ act on $`c_{r+1}`$ ($`0\le r\le L-1`$), and $`\lvert\chi\rangle=\lvert\chi_1\rangle\otimes\cdots\otimes\lvert\chi_L\rangle`$. Determine, as a function of $`r`$, the lowest order in $`\lambda`$ at which $`\delta p_h`$ can be nonzero, and the operator that governs that order.

4. **Cost.** Determine whether the leading coefficient of item 2(a) depends on the source only through the cost difference $`\langle B_\sigma-B_{\sigma'}\rangle`$.

5. **Example.** This is the qubit medium of the 06 example: $`\mathcal H_c=\mathbb C^2`$, $`\lvert\chi\rangle=\lvert0\rangle`$ with $`\sigma_z\lvert0\rangle=\lvert0\rangle`$, and $`X:=\sigma_x+\sigma_z`$.
   - The moving body has places $`h_1,\dots,h_n`$ with $`K_{h_i}=i\,X`$ ($`i`$ an index), nearest-neighbour hopping $`t_{h_ih_{i+1}}=t_{h_{i+1}h_i}=t>0`$, and no other $`t_{hh'}`$. It starts at $`h_m`$ with $`2\le m\le n-1`$.
   - The source places are a finite set of real numbers containing $`0`$, with $`B_\sigma=\sigma\,\sigma_y`$.

   Take $`\sigma'=0`$. Determine the leading terms of $`\delta p_{h_{m\pm1}}`$, $`\delta p_{h_m}`$ and $`\delta\bar x`$. Compare them with the effect of the source on the background of $`b`$ in (6.14) and (6.15).

## Inputs

From 02-view-content@v1. Notation fixed there: $`p_h:=\langle h\vert V_A\vert h\rangle`$, $`\lvert\psi_h\rangle:=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle`$.

Eq. (2.1):

```math
\lvert\Psi\rangle=\sum_h\lvert h\rangle\otimes\lvert\psi_h\rangle,
\qquad
\lvert\psi_h\rangle=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle=\sum_r\Psi_{hr}\lvert r\rangle,
\qquad
\sum_h\lVert\psi_h\rVert^2=\lVert\Psi\rVert^2=1 .
```

Eq. (2.2):

```math
V_A=\sum_{h,h'}\langle\psi_{h'}\vert\psi_h\rangle\,\lvert h\rangle\langle h'\rvert,
\qquad\text{i.e.}\qquad
(V_A)_{hh'}=\langle\psi_{h'}\vert\psi_h\rangle,
\qquad
p_h=\lVert\psi_h\rVert^2 .
```

From 05-recording-contract@v1, in the setting of 05 (one recorded object, one medium object, the recording contract $`\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, the start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\phi_h\neq0`$).

Eq. (5.10):

```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
```

From 06-body-in-medium@v1. Setting of 06, in its own notation:
- three objects of pairwise different types: a probe $`p`$ with records $`K_h`$, a body $`b`$ with records $`B_\beta`$, and a medium $`c`$;
- $`C=\sum_h\lvert h\rangle\langle h\rvert_p\otimes\mathbb 1_b\otimes K_h+\sum_\beta\mathbb 1_p\otimes\lvert\beta\rangle\langle\beta\rvert_b\otimes B_\beta`$;
- start $`\lvert\phi\rangle_p\otimes\lvert\beta_0\rangle_b\otimes\lvert\chi\rangle`$ with $`\phi_h\neq0`$;
- $`D:=K_h-K_{h'}`$, $`\tilde D:=D-\langle D\rangle`$; $`W^{(\beta_0)}`$ is the witness weight of the view of $`\{p\}`$.

There is no hopping in 06. In this question, 06's probe corresponds to the moving body $`b`$, and 06's body (records $`B_\beta`$) to the source $`s`$.

Eq. (6.4):

```math
V_{\{b\}}(\Psi(\lambda))=\lvert\beta_0\rangle\langle\beta_0\rvert ,\qquad p_b(\beta)=\delta_{\beta\beta_0}\qquad\text{for every }\lambda .
```

Eq. (6.7), for $`[B_{\beta_0},K_h]=[B_{\beta_0},K_{h'}]=0`$:

```math
G^{(\beta_0)}_{hh'}(\lambda)=\langle\chi\vert e^{\mathrm iK_{h'}\lambda}e^{-\mathrm iK_h\lambda}\vert\chi\rangle,\qquad
W^{(\beta_0)}(h,h';\lambda)=W(h,h';\lambda)\ \text{of (5.6)}\quad\text{for every }\lambda\ge0 .
```

Eq. (6.9):

```math
W^{(\beta_0)}(h,h';\lambda)=1-\lambda^2\mathrm{Var}_\chi(D)+\lambda^3c_3^{(\beta_0)}(h,h')+O(\lambda^4),
```

Eq. (6.10):

```math
c_3^{(\beta_0)}(h,h')=\mathrm{Im}\langle\chi\vert\,(K_{h'}+B_{\beta_0})\,\tilde D^2\vert\chi\rangle ,
```

Eq. (6.11):

```math
c_3^{(\beta_0)}=c_3^{(0)}+\mathrm{Im}\langle\chi\vert B_{\beta_0}\tilde D^2\vert\chi\rangle,\qquad
c_3^{(0)}(h,h')=\mathrm{Im}\langle\chi\vert K_{h'}\tilde D^2\vert\chi\rangle,\qquad
\mathrm{Im}\langle\chi\vert B_{\beta_0}\tilde D^2\vert\chi\rangle=\frac{\langle\chi\vert[B_{\beta_0},\tilde D^2]\vert\chi\rangle}{2\mathrm i}.
```

The 06 example: $`\chi=\lvert0\rangle`$, $`K_{h_i}=iX`$ with $`X=\sigma_x+\sigma_z`$, $`B_\beta=\beta\,\sigma_y`$.

Eq. (6.14):

```math
c_3^{(\beta_0)}(h_i,h_j)=2\beta_0(i-j)^2,\qquad
W^{(\beta_0)}(h_i,h_j;\lambda)=1-(i-j)^2\lambda^2+2\beta_0(i-j)^2\lambda^3+O(\lambda^4),
```

Eq. (6.15), an asymptotic statement as $`\lambda\to0^+`$ for a fixed pair:

```math
\alpha_2^{(\beta_0)}(h_i,h_j)=-\beta_0\lvert i-j\rvert,\qquad
\alpha^{(\beta_0)}(h_i,h_j;\lambda)=\lambda\lvert i-j\rvert\,(1-\beta_0\lambda)+O(\lambda^3).
```

From 08-cell-medium@v1. Setting of Step 7 of 08, in its own notation:
- a probe $`p`$ with records $`K_h`$ on cell $`c_1`$, a body $`b`$ with records $`B_\beta`$ on cell $`c_{r+1}`$, cells $`c_1,\dots,c_L`$, all of pairwise different types;
- links $`J_{\rm ch}:=\sum_{k=1}^{L-1}J_k`$ with $`J_k`$ on $`c_kc_{k+1}`$;
- $`\lvert\chi\rangle=\lvert\chi_1\rangle\otimes\cdots\otimes\lvert\chi_L\rangle`$;
- $`D=K_h-K_{h'}`$, $`M:=K_{h'}+B_{\beta_0}+J_{\rm ch}`$, $`D(s):=e^{\mathrm iMs}De^{-\mathrm iMs}`$;
- $`\Delta W^{(\beta_0)}`$ is the body-dependent part of the witness weight of the view of $`\{p\}`$.

Eq. (8.15):

```math
\delta D(s):=D(s)-D(s)\big|_{B_{\beta_0}=0}=\frac{(\mathrm is)^{r+1}}{(r+1)!}Z_r+O(s^{r+2}),\qquad
Z_r:=[B_{\beta_0},[J_r,[\cdots[J_1,D]\cdots]]],
```

with $`Z_0=[B_{\beta_0},D]`$.

Eq. (8.16):

```math
\Delta W^{(\beta_0)}=2\mathrm{Re}\bigl(G_0^*\,\delta G\bigr)+\lvert\delta G\rvert^2=2\mathrm{Re}\bigl(-\mathrm i\,a\,\lambda^{r+2}\bigr)+O(\lambda^{r+3})=O(\lambda^{3+r}).
```

From 17-motion@v2. Setting of 17:
- a body $`b`$ with hopping $`C_b=\sum t_{hh'}\lvert h\rangle\langle h'\rvert`$ and records $`K_h`$, and a medium $`c`$; contract $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$; start $`\lvert\beta\rangle\otimes\lvert\chi\rangle`$;
- $`c_n(h):=(\langle h\rvert\otimes\mathbb 1)C^n(\lvert\beta\rangle\otimes\chi)`$, which obey $`c_{n+1}(h)=\sum_{h'}t_{hh'}c_n(h')+K_hc_n(h)`$ with $`c_0(h)=\delta_{h\beta}\chi`$;
- $`\epsilon_h:=\langle K_h\rangle`$; $`(t^n)_{hh'}`$ are the entries of the powers of the matrix $`t`$.

Eq. (17.8), for $`h\neq\beta`$:

```math
\begin{aligned}
c_1(h)&=t_{h\beta}\chi,\qquad c_2(h)=(t^2)_{h\beta}\chi+t_{h\beta}(K_h+K_\beta)\chi,\\
\langle\chi\vert c_3(h)\rangle&=(t^3)_{h\beta}+\sum_{h'}t_{hh'}t_{h'\beta}(\epsilon_h+\epsilon_{h'}+\epsilon_\beta)+t_{h\beta}\langle K_h^2+K_hK_\beta+K_\beta^2\rangle .
\end{aligned}
```

Eq. (17.24):

```math
p_h(\lambda)=\sum_{N\ge0}p_h^{(N)}\lambda^N,\qquad p_h^{(N)}=\sum_{k+l=N}\frac{i^k(-i)^l}{k!\,l!}\,\bigl\langle c_k(h)\big\vert c_l(h)\bigr\rangle .
```

Eq. (17.10), the $`\lambda^4`$ coefficient of $`p_h`$ for $`h\neq\beta`$:

```math
p_h^{(4)}=\underbrace{\tfrac14\lvert(t^2)_{h\beta}\rvert^2-\tfrac13\mathrm{Re}\bigl[t^*_{h\beta}(t^3)_{h\beta}\bigr]}_{K\text{-independent}}
\;\underbrace{-\;\tfrac{1}{12}\lvert t_{h\beta}\rvert^2d_0(h,\beta)^2}_{\text{record spread}}
\;\underbrace{-\;\tfrac{1}{12}\lvert t_{h\beta}\rvert^2(\epsilon_h-\epsilon_\beta)^2+\tfrac16\sum_{h'}\mathrm{Re}\bigl(t^*_{h\beta}t_{hh'}t_{h'\beta}\bigr)(\epsilon_h+\epsilon_\beta-2\epsilon_{h'})}_{\text{record means}} .
```

## Assumptions

- The setting and the definition under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- Item 1 is exact. Items 2–5 are statements for $`\lambda\to0^+`$.
- A result about the source must be stated in a form that is invariant under the A5 placement convention, for example through $`B_\sigma-B_{\sigma'}`$.

## Scope

- In scope:
  - one source that does not hop, and one moving body that hops and is recorded;
  - one medium object, and in item 3 a chain of cells;
  - the leading orders and the example.
- Out of scope:
  - both bodies moving, a delocalized source, and identical-type bodies;
  - orders beyond the leading source-dependent one;
  - curvature, which belongs to a later package;
  - a physical time (criterion 8 is handed over; all rates are with respect to $`\lambda`$);
  - any physical or spatial meaning beyond the definitions (M1, M2, M4).

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: short argument.
- Item 4: short argument.
- Item 5: derive.

## Expected result

- Item 1: a closed form for the state and the reduced contract; a sufficient condition; a statement on invariance.
- Item 2: orders and closed-form coefficients; a yes/no answer, and the relation if there is one; an order and a coefficient for $`\delta\bar x`$.
- Item 3: an order as a function of $`r`$, and the governing operator.
- Item 4: a yes/no answer with a short argument or counterexample.
- Item 5: closed-form leading terms, and a statement comparing them with (6.14) and (6.15).

Give every main result a tag $`(18.k)`$.

Consistency checks, at most three: for example $`B_\sigma=B_{\sigma'}`$, no hopping, and the $`t\to0`$ or $`\sigma\to0`$ limit of item 5.

## Code

None.
