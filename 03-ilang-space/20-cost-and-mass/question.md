# Question: 20-cost-and-mass

- **Subproject:** 03-ilang-space
- **Package:** 20-cost-and-mass
- **Equation tags:** (20.k)
- **Created:** 2026-10-09

## Goal

Determine how the cost (1.8) is distributed over the places and points of the background, which parts of this distribution are free of every convention of the description, and how the motion of a body responds to it. In particular, determine whether the response of a body to a cost gradient (its inertia) is governed by a cost of the body, and if so by which. The notions defined below (site cost, edge cost, site cost per unit weight, acceleration, force, inverse inertia) are fixed for later packages. They mean only what their definitions say (M1, M2, M4). Acceleration is a rate of change with respect to $`\lambda`$; a physical time is criterion 8 and not part of this package.

**Setting for item 1 (general).** Any description satisfying A1–A7. An object $`b`$ of type $`T`$ with places $`h\in H_T`$ is the only instance of $`T`$. The part is $`A=\{b\}`$, and $`\bar A`$ is its companion. The branch vectors $`\lvert\psi_h\rangle`$ are those of (2.1), and $`p_h=\lVert\psi_h\rVert^2`$ (2.2).

**Setting for items 2–4 (body and medium).** As in 17:
- **Objects.** A body $`b`$ of type $`T`$ with places $`h\in H_T`$ and $`d_T\ge2`$, the only instance of $`T`$. A medium $`c`$: one object of another type, the only instance of its type.
- **Contract.** One pair term between $`b`$ and $`c`$:
  ```math
  C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h,\qquad C_b=\sum_{h,h'}t_{hh'}\lvert h\rangle\langle h'\rvert ,
  ```
  with complex numbers $`t_{hh'}=t_{h'h}^*`$ and $`K_h`$ self-adjoint on $`\mathcal H_c`$. By A5 this pair term contains every single-object term; a term acting on $`c`$ alone is contained in the $`K_h`$ (the same operator added to every $`K_h`$). The **hopping graph** joins two places $`h\neq h'`$ iff $`t_{hh'}\neq0`$.
- **Start.** $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with unit vectors $`\phi\in\mathcal H_T`$ and $`\chi\in\mathcal H_c`$.
- **Notation.** $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, $`\epsilon_h:=\langle K_h\rangle`$, $`\lvert u_h\rangle:=(K_h-\epsilon_h)\lvert\chi\rangle`$ as in (5.10), and $`g(v,w):=\mathrm{Re}\langle v\vert w\rangle`$ on $`\mathcal H_c`$. $`V_b(\lambda)`$ is the view of $`\{b\}`$.

**Definitions.**
- **Blocks.** $`C_{hh'}:=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\,C\,\bigl(\lvert h'\rangle\otimes\mathbb 1_{\bar A}\bigr)`$, an operator on $`\mathcal H_{\bar A}`$, with $`C_{h'h}=C_{hh'}^\dagger`$. In the setting of items 2–4, $`C_{hh'}=t_{hh'}\mathbb 1_c`$ for $`h\neq h'`$ and $`C_{hh}=t_{hh}\mathbb 1_c+K_h`$.
- **Site cost and edge cost.** For a place $`h`$, and for an unordered pair $`\{h,h'\}`$ of different places:
  ```math
  L_h(\lambda):=\langle\psi_h\vert C_{hh}\vert\psi_h\rangle,\qquad L_{hh'}(\lambda):=2\mathrm{Re}\langle\psi_h\vert C_{hh'}\vert\psi_{h'}\rangle .
  ```
  The **cost edges** are the pairs with $`C_{hh'}\neq0`$. Where a background (5.11) is defined (items 2–4), a point $`x`$ of it carries the site costs of its places and the edge costs of the pairs inside $`x`$. The edge cost of a pair of places in different points is attached to that pair of points.
- **Site cost per unit weight** (items 3–4): $`\Omega_h:=\langle\chi\vert C_{hh}\vert\chi\rangle=t_{hh}+\epsilon_h`$. For the product start, $`L_h(0)=p_h(0)\,\Omega_h`$.
- **Position, velocity, acceleration** (as in 17): $`\bar x(\lambda):=\sum_hp_h(\lambda)\,u_h`$, $`v:=\mathrm d\bar x/\mathrm d\lambda`$, $`a:=\mathrm d^2\bar x/\mathrm d\lambda^2`$.
- **Uniform cost gradient, force, inverse inertia** (item 3). The site costs per unit weight have a uniform gradient if there is a vector $`f\in\mathcal H_c`$ with $`\Omega_h-\Omega_{h'}=g\bigl(f,u_h-u_{h'}\bigr)`$ for all $`h,h'`$. The **force** is $`F:=-f`$. Vary the description only through the diagonal entries $`t_{hh}`$; this changes the $`\Omega_h`$ and nothing else. Let $`a_0`$ be the value of $`a(0)`$ when all $`\Omega_h`$ are equal. The **inverse inertia** $`\mu`$ is the real-linear map on $`(\mathcal H_c,g)`$, if one exists, such that $`a(0)=a_0+\mu F`$ for every uniform gradient.

1. **The cost on the background** (setting of item 1).
   - (a) Determine whether $`\sum_hL_h+\sum_{\{h,h'\}}L_{hh'}=L`$ holds. Determine whether $`L_h`$ and $`L_{hh'}`$ depend on the placement of single-object terms (A5), on the common phase (1.2), or on the phase split (1.6).
   - (b) Replacing $`C`$ by $`C+c\,\mathbb 1`$ with real $`c`$ changes every evolution only by a common phase, so it changes no reading. Determine how $`L_h`$ and $`L_{hh'}`$ change under this replacement, and which of them, or which combinations of them, are unchanged.
   - (c) For a set $`R`$ of places (for example all places of a set of background points), let $`L_R`$ be the sum of the site costs of the places in $`R`$ and of the edge costs of the pairs inside $`R`$. Determine $`\mathrm dL_R/\mathrm d\lambda`$ exactly. Determine which blocks $`C_{hh'}`$ it depends on, in particular whether $`L_R`$ can change only through blocks with one place in $`R`$ and the other outside $`R`$.

2. **Acceleration.** For every $`\lambda`$, determine an exact expression for $`a(\lambda)`$ in terms of the blocks $`C_{hh'}`$, the branch vectors $`\psi_h(\lambda)`$ and the $`u_h`$. Determine which parts of it depend on the diagonal blocks $`C_{hh}`$, and through which combinations of them. Determine whether the result depends on the placement of single-object terms (A5) or changes under $`C\to C+c\,\mathbb 1`$.

3. **Inertia.** For the product start at $`\lambda=0`$:
   - (a) Determine $`a(0)`$ for arbitrary $`\Omega_h`$.
   - (b) Assume a uniform cost gradient. Determine $`a_0`$ and $`\mu`$. Determine whether $`\mu`$ is symmetric with respect to $`g`$. Determine whether it is a function of the edge costs $`L_{hh'}(0)`$ and the background alone, of the site costs, or of the total cost $`L`$. Determine when it is positive semidefinite.
   - (c) Determine $`a_0`$ and $`\mu`$ for a localized start $`\phi=\lvert\beta\rangle`$, and compare $`a_0`$ with (17.11)–(17.12).

4. **Example: chain with linear records.** The chain of 17: infinite chain $`h_m`$, $`m\in\mathbb Z`$, $`C_b=t\sum_m\bigl(\lvert h_m\rangle\langle h_{m+1}\rvert+\lvert h_{m+1}\rangle\langle h_m\rvert\bigr)`$ with $`t>0`$, $`K_{h_m}=m\,X`$, $`X=\sum_\xi\xi\,\Pi_\xi`$, $`\sigma_X>0`$, and $`e:=(X-\langle X\rangle)\chi`$.
   - (a) Determine the $`\Omega_{h_m}`$. Determine whether they have a uniform gradient, and if so the force $`F`$.
   - (b) For the start $`2^{-1/2}\bigl(\lvert h_0\rangle+e^{i\theta}\lvert h_1\rangle\bigr)\otimes\lvert\chi\rangle`$ with real $`\theta`$, determine the edge cost at $`\lambda=0`$, $`\mu`$, $`a_0`$ and $`a(0)`$. Compare $`a(0)`$ with the derivative of (17.22) at $`\lambda=0`$. Determine for which $`\theta`$ the map $`\mu`$ is positive semidefinite. For the start $`\lvert h_0\rangle\otimes\lvert\chi\rangle`$, determine $`\mu`$ and $`a(0)`$ and compare with (17.19).
   - (c) Start of (b), $`\lambda>0`$. If item 3(b) expresses $`\mu`$ through the edge costs at $`\lambda=0`$, let $`\mu(\lambda)`$ be the same expression with the edge costs $`L_{hh'}(\lambda)`$. Determine $`a(\lambda)`$, and whether $`a(\lambda)=\mu(\lambda)F`$ holds. If it does not, determine the difference.

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

From 05-recording-contract@v1. These hold in the setting of 05: one recorded object, one medium object, the recording contract $`\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, and the start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\phi_h\neq0`$ for all $`h`$. Notation fixed there: $`g(v,w):=\mathrm{Re}\langle v\vert w\rangle`$, and $`h\sim_0h'`$ iff $`u_h=u_{h'}`$.

Eq. (5.10):

```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
```

Eq. (5.11):

```math
\bigl(H_V/{\sim_0},\,d_0\bigr)\;\cong\;\bigl(\{u_h:h\in H_V\},\,\lVert\cdot\rVert\bigr)\subset(\mathcal H_c,g).
```

From 17-motion@v2. These hold in the setting of items 2–4 above. Notation fixed there: $`E`$ is the set of edges of the hopping graph, $`(t^n)_{hh'}`$ are the entries of the powers of the matrix $`t=(t_{hh'})`$, and for the chain $`S:=\sum_m\lvert h_m\rangle\langle h_{m+1}\rvert`$, $`M:=\sum_mm\,\lvert h_m\rangle\langle h_m\rvert`$, $`C_b=t(S+S^\dagger)`$, $`w_\xi=\langle\chi\vert\Pi_\xi\vert\chi\rangle`$.

Eq. (17.1):

```math
i\,\frac{\mathrm d}{\mathrm d\lambda}\lvert\psi_h\rangle=\sum_{h'}t_{hh'}\lvert\psi_{h'}\rangle+K_h\lvert\psi_h\rangle,\qquad \lvert\psi_h(0)\rangle=\phi_h\lvert\chi\rangle .
```

Eq. (17.2):

```math
d_0(h,h')=\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=\bigl\lVert u_h-u_{h'}\bigr\rVert,\qquad u_h=(K_h-\epsilon_h)\chi,\quad\text{independent of the }t_{hh'} .
```

From Step 3 of 17, verbatim: "The partial matrix elements of $`C`$ are $`(\langle h\rvert\otimes\mathbb 1)C(\lvert h'\rangle\otimes\mathbb 1)=t_{hh'}\mathbb 1`$ for $`h\neq h'`$ and $`t_{hh}\mathbb 1+K_h`$ for $`h=h'`$. So $`C`$ fixes $`K_h`$ only up to $`K_h\to K_h+c_h\mathbb 1`$ (with $`t_{hh}\to t_{hh}-c_h`$), and $`u_h`$ is invariant under this change." "The phase split of the start, $`\phi\otimes\chi=(e^{-i\varphi}\phi)\otimes(e^{i\varphi}\chi)`$, sends every $`u_h`$ to $`e^{i\varphi}u_h`$." "$`\bar x`$ and $`v`$ are well defined up to the common isometry $`e^{i\varphi}`$, which acts on them and on the background points $`u_h`$ together."

Eq. (17.4):

```math
\frac{\mathrm dp_h}{\mathrm d\lambda}=\sum_{h'}J_{h'\to h},\qquad J_{h'\to h}(\lambda):=2\mathrm{Im}\bigl[t_{hh'}\,(V_b(\lambda))_{h'h}\bigr]=-J_{h\to h'} .
```

Eq. (17.6):

```math
v(\lambda)=\sum_{\{h,h'\}\in E}2\mathrm{Im}\bigl[t_{hh'}(V_b(\lambda))_{h'h}\bigr]\,(u_h-u_{h'}) .
```

Eqs. (17.11) and (17.12), for the start $`\phi=\lvert\beta\rangle`$:

```math
\bar x(\lambda)-u_\beta=\lambda^2w_2+\lambda^3w_3+O(\lambda^4),\qquad w_2=\sum_h\lvert t_{h\beta}\rvert^2(u_h-u_\beta),\quad w_3=\sum_h\mathrm{Im}\bigl[t^*_{h\beta}(t^2)_{h\beta}\bigr](u_h-u_\beta),
```

```math
v(\lambda)=2\lambda\,w_2+3\lambda^2w_3+O(\lambda^3),\qquad v(0)=0 .
```

Eq. (17.14), for commuting records $`K_h=\sum_j\kappa_h(j)P_j`$ with orthogonal projectors $`P_j`$, $`\sum_jP_j=\mathbb 1`$, and $`D_j:=\sum_h\kappa_h(j)\lvert h\rangle\langle h\rvert`$:

```math
V_b(\lambda)=\sum_jw_j\,U_j(\lambda)\lvert\phi\rangle\langle\phi\rvert U_j(\lambda)^\dagger,\qquad U_j(\lambda)=e^{-i(C_b+D_j)\lambda},\qquad w_j=\langle\chi\vert P_j\vert\chi\rangle .
```

Eq. (17.15), for the chain:

```math
d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X,\qquad \bar x=\bar m\,e,\quad \bar m:=\sum_mm\,p_{h_m},\qquad s^2=\sigma_X^2\sum_m(m-\bar m)^2p_{h_m} .
```

From Step 9 of 17, verbatim: "Item 4 applies with $`P_j\to\Pi_\xi`$, $`w_\xi=\langle\chi\vert\Pi_\xi\vert\chi\rangle`$ (finitely many $`\xi`$, since $`\mathcal H_c`$ is finite) and $`D_\xi=\xi M`$". "Heisenberg equations: $`\tfrac{\mathrm d}{\mathrm d\lambda}S_H=-i\xi S_H`$, so $`S_H=e^{-i\xi\lambda}S`$, and $`\tfrac{\mathrm d}{\mathrm d\lambda}M_H=it(S_H-S_H^\dagger)`$. Integrating,"

Eq. (17.17):

```math
U_\xi^\dagger M\,U_\xi=M+\frac{t}{\xi}\Bigl[(1-e^{-i\xi\lambda})S+(1-e^{i\xi\lambda})S^\dagger\Bigr]\qquad(\xi=0:\ M+it\lambda(S-S^\dagger)).
```

Eq. (17.19), for the start $`\lvert h_0\rangle\otimes\lvert\chi\rangle`$:

```math
\bar x(\lambda)=u_{h_0}=0,\qquad s(\lambda)^2=4t^2\sigma_X^2\sum_\xi w_\xi\,\frac{1-\cos\xi\lambda}{\xi^2}\qquad\Bigl(\xi=0\text{ term: }\tfrac{\lambda^2}{2}\Bigr).
```

Eq. (17.22), for the start $`2^{-1/2}\bigl(\lvert h_0\rangle+e^{i\theta}\lvert h_1\rangle\bigr)\otimes\lvert\chi\rangle`$:

```math
v(\lambda)=t\sum_\xi w_\xi\sin(\xi\lambda-\theta)\;e=t\,\mathrm{Im}\Bigl[e^{-i\theta}\langle\chi\vert e^{iX\lambda}\vert\chi\rangle\Bigr]\,(X-\langle X\rangle)\lvert\chi\rangle .
```

## Assumptions

- The settings and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- Items 1 and 2 are exact for every $`\lambda`$. Item 3 concerns $`\lambda=0`$. Item 4 is exact; the infinite chain is the limit of 17 (finite sums for starts of finite support).

## Scope

- In scope:
  - the site and edge costs of one object's places, and their aggregation onto background points;
  - one body with hopping, recorded by one medium (the setting of 17);
  - the response of its position to the site costs per unit weight, at $`\lambda=0`$ (item 3) and in the chain example (item 4).
- Out of scope:
  - several bodies, composite bodies, and bodies of identical types;
  - whether the cost of one body acts on other bodies;
  - contracts internal to the medium beyond single-object terms, and media of several cells;
  - a physical time (criterion 8);
  - any physical or spatial meaning beyond the definitions (M1, M2, M4).

## Depth

- Item 1(a), 1(b): short argument.
- Item 1(c): derive.
- Item 2: derive.
- Item 3: derive.
- Item 4(a), 4(b): derive.
- Item 4(c): short argument.

## Expected result

- Item 1: an identity and invariance statements; transformation rules and the list of invariant quantities; an exact expression for the rate of change and a statement on which blocks enter.
- Item 2: an exact identity as finite sums over places, split into two parts; invariance statements.
- Item 3: a closed form for $`a(0)`$; $`a_0`$ and $`\mu`$ as explicit finite sums; yes/no answers with conditions; the values for a localized start.
- Item 4: closed forms in $`t`$, $`\theta`$, $`\langle X\rangle`$, $`\sigma_X`$, $`w_\xi`$, $`\xi`$ and $`e`$; agreement or disagreement with (17.19) and (17.22); a condition on $`\theta`$; a yes/no answer and, if no, a closed form of the difference.

Give every main result a tag $`(20.k)`$.

Consistency checks, at most three: for example no hopping ($`t_{hh'}=0`$ for $`h\neq h'`$), all $`K_h`$ equal, and conservation of $`L`$.

## Code

None.
