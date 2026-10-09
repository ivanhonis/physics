# Question: 16-common-space

- **Subproject:** 03-ilang-space
- **Package:** 16-common-space
- **Equation tags:** (16.k)
- **Created:** 2026-10-08

## Goal

Determine how the leading-order witness geometries of two objects of different types, recorded by one medium, are related. Determine which relations between them are well defined, which of them the joint view fixes, and when the points of one type can be matched with the points of the other. This is the common-space question (criterion 12) for two types. The notation introduced below ($`K^A_h`$, $`K^B_k`$, $`u^A_h`$, $`u^B_k`$, $`X_A`$, $`X_B`$, correspondence) is fixed for later packages.

**Setting.**
- **Objects.** Three objects of pairwise different types, each the only instance of its type, so (1.11) imposes no constraint: $`a`$ of type $`A`$ with places $`h\in H_A`$, $`b`$ of type $`B`$ with places $`k\in H_B`$, where $`d_A,d_B\ge2`$, and the medium $`c`$.
- **Contracts.** Each of $`a`$ and $`b`$ is recorded by the medium:
  ```math
  C=\sum_h\lvert h\rangle\langle h\rvert_a\otimes K^A_h+\sum_k\lvert k\rangle\langle k\rvert_b\otimes K^B_k ,
  ```
  with $`K^A_h`$ and $`K^B_k`$ self-adjoint on $`\mathcal H_c`$, each term extended by the identity on the other object.
- **Start.** $`\lvert\phi\rangle_a\otimes\lvert\vartheta\rangle_b\otimes\lvert\chi\rangle_c`$, with $`\phi_h\neq0`$ and $`\vartheta_k\neq0`$ for all $`h,k`$.
- **Notation.** $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, $`\lvert u^A_h\rangle:=(K^A_h-\langle K^A_h\rangle)\lvert\chi\rangle`$, $`\lvert u^B_k\rangle:=(K^B_k-\langle K^B_k\rangle)\lvert\chi\rangle`$, and $`g(v,w):=\mathrm{Re}\langle v\vert w\rangle`$.

1. **Split.**
   - (a) Determine all families $`(K'^A_h,K'^B_k)`$ of self-adjoint operators on $`\mathcal H_c`$ that give the same $`C`$.
   - (b) Determine how $`u^A_h`$ and $`u^B_k`$ change under these replacements, and which functions of the record vectors are well defined (M6). In particular, determine whether $`\lVert u^A_h-u^B_k\rVert`$ is well defined.

2. **Views.**
   - (a) Determine the leading-order distance $`d_0`$ of three views in terms of the record vectors: the view of $`\{a\}`$ (companion $`\{b,c\}`$), the view of $`\{b\}`$ (companion $`\{a,c\}`$), and the view of $`\{a,b\}`$ (companion $`\{c\}`$). State whether the setting of 11 applies to each of these cuts.
   - (b) Determine whether $`d_0`$ of the view of $`\{a\}`$ depends on the $`K^B_k`$ or on $`\vartheta`$.
   - (c) Determine which quantities that involve both types the view of $`\{a,b\}`$ fixes at leading order.

3. **Correspondences.** Let $`X_A`$ and $`X_B`$ be the sets of leading-order points of the views of $`\{a\}`$ and of $`\{b\}`$, where places at $`d_0=0`$ form one point. A **correspondence** is a bijection $`\pi:D_A\to D_B`$ between subsets $`D_A\subseteq X_A`$ and $`D_B\subseteq X_B`$ with $`\lvert D_A\rvert\ge2`$ that satisfies the following. For all $`x,x'\in D_A`$, the joint places $`(h,k')`$ and $`(h',k)`$ have $`d_0=0`$ in the view of $`\{a,b\}`$, where $`h\in x`$, $`h'\in x'`$, $`k\in\pi(x)`$ and $`k'\in\pi(x')`$. In words: at leading order, the medium does not witness which object stands at which of two matched points.
   - (a) Determine a necessary and sufficient condition on the record vectors under which $`\pi`$ is a correspondence.
   - (b) Determine whether every correspondence is an isometry from $`(D_A,d_0)`$ onto $`(D_B,d_0)`$.
   - (c) Determine a necessary and sufficient condition under which a correspondence with $`D_A=X_A`$ and $`D_B=X_B`$ exists, and whether it is then unique.

4. **Examples.** The places are $`h_1,\dots,h_n`$ of $`a`$ and $`k_1,\dots,k_n`$ of $`b`$, with $`n\ge2`$; $`i`$ and $`j`$ are indices.
   - (a) **One line.** $`K^A_{h_i}=i\,X`$ and $`K^B_{k_j}=j\,X+Y`$, where $`X,Y`$ are self-adjoint on $`\mathcal H_c`$ and $`\sigma_X:=(\langle X^2\rangle-\langle X\rangle^2)^{1/2}>0`$.
   - (b) **Two directions.** $`\mathcal H_c=\mathbb C^2`$, $`\lvert\chi\rangle=\lvert0\rangle`$ with $`\sigma_z\lvert0\rangle=\lvert0\rangle`$, $`K^A_{h_i}=i\,\sigma_x`$ and $`K^B_{k_j}=j\,\sigma_y`$.

   For each example, determine $`d_0`$ of the three views of item 2, the quantities of item 2(c), and all correspondences.

## Inputs

From 02-view-content@v1. Notation fixed there: $`p_h:=\langle h\vert V_A\vert h\rangle`$, $`H_V:=\{h:p_h>0\}`$, $`\lvert\psi_h\rangle:=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle`$, $`G_{hh'}=\langle E_{h'}\vert E_h\rangle`$.

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

Eq. (2.11):

```math
W(h)=1,\qquad W(h,h')=\lvert G_{hh'}\rvert^2=\frac{\lvert(V_A)_{hh'}\rvert^2}{p_hp_{h'}} .
```

From 03-witness-distance@v1. Notation fixed there: $`h\approx h'`$ iff $`W(h,h')=1`$; $`X_V:=H_V/{\approx}`$; $`\alpha(x,x'):=\arccos\sqrt{W(x,x')}\in[0,\pi/2]`$.

Eq. (3.5). Here $`\alpha`$ is a metric on $`X_V`$.

```math
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}}
=\frac{\lvert\langle h\vert V_A\vert h'\rangle\rvert}{\sqrt{\langle h\vert V_A\vert h\rangle\langle h'\vert V_A\vert h'\rangle}},\qquad h\in x,\ h'\in x' .
```

From 05-recording-contract@v1. These hold in the setting of 05: one recorded object, one medium object, the recording contract $`\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, and the start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\phi_h\neq0`$ for all $`h`$. Notation fixed there: $`h\sim_0h'`$ iff $`u_h=u_{h'}`$.

Eq. (5.10):

```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
```

Eq. (5.11):

```math
\bigl(H_V/{\sim_0},\,d_0\bigr)\;\cong\;\bigl(\{u_h:h\in H_V\},\,\lVert\cdot\rVert\bigr)\subset(\mathcal H_c,g).
```

From 11-cut-boundary@v1. These hold in the setting of 11:
- A1–A7 hold, $`\mathcal H=\mathcal H_A\otimes\mathcal H_{\bar A}`$ for a part $`A`$ with $`\bar A\neq\emptyset`$, and no type has objects on both sides of the cut;
- $`C=C_A+C_{\bar A}+C_\partial`$, with $`C_\partial=\sum_nA_n\otimes B_n`$, $`A_n=A_n^\dagger`$ on $`\mathcal H_A`$ and $`B_n=B_n^\dagger`$ on $`\mathcal H_{\bar A}`$;
- the initial state is the product $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\phi_h\neq0`$ for every joint place $`h`$ of $`A`$, and $`\langle B\rangle:=\langle\chi\vert B\vert\chi\rangle`$;
- $`Q_\chi:=\mathbb 1_{\bar A}-\lvert\chi\rangle\langle\chi\rvert`$, and $`v_h`$ is the first-order coefficient of $`\psi_h/\phi_h`$ in (11.5).

Eq. (11.6):

```math
Q_\chi\lvert v_h\rangle=Q_\chi C_{\bar A}\lvert\chi\rangle+\lvert u_h\rangle,\qquad
\lvert u_h\rangle=\frac{1}{\phi_h}\,Q_\chi\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)C_\partial\bigl(\lvert\phi\rangle\otimes\lvert\chi\rangle\bigr).
```

Eq. (11.8):

```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert .
```

Eq. (11.10), when every $`A_n`$ is diagonal in the place basis:

```math
\lvert u_h\rangle=\sum_n\langle h\vert A_n\vert h\rangle\bigl(B_n-\langle B_n\rangle\bigr)\lvert\chi\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle,\qquad K_h:=\sum_n\langle h\vert A_n\vert h\rangle B_n=K_h^\dagger .
```

## Assumptions

- The setting under "Goal". All contracts are independent of $`\lambda`$ (A5).
- "Leading order" refers to $`\lambda\to0^+`$. Item 1(a) is exact.

## Scope

- In scope:
  - two objects of different types recorded by one medium;
  - the split freedom, and the leading-order geometry of the three views;
  - correspondences;
  - the two examples.
- Out of scope:
  - localized states (bodies), and identical instances;
  - contracts between $`a`$ and $`b`$, and several media;
  - loop data, and orders beyond the leading one;
  - any rule that selects a correspondence beyond the definition;
  - any physical or spatial meaning beyond the definitions (M1, M4).

## Depth

- Item 1: derive.
- Item 2: derive.
- Item 3: derive.
- Item 4: derive.

## Expected result

- Item 1: the general form of the replacements, and a statement of which quantities are well defined.
- Item 2: closed forms for the three distances; a yes/no answer; a list of quantities.
- Item 3: an equivalence; a yes/no answer; an equivalence with a uniqueness statement.
- Item 4: closed forms, and the lists of correspondences.

Give every main result a tag $`(16.k)`$.

Consistency checks, at most three: for example $`k`$-independent $`K^B_k`$, the exchange of the roles of $`a`$ and $`b`$, and a rescaling of $`C`$.

## Code

None.
