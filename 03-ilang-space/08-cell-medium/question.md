# Question: 08-cell-medium

- **Subproject:** 03-ilang-space
- **Package:** 08-cell-medium
- **Equation tags:** (8.k)
- **Created:** 2026-10-08

## Goal

Determine how the effect of a body on a probe's witness geometry depends on where the body is recorded, when the medium consists of cells coupled by contracts. Specifically: when does the effect vanish, at which order in $`\lambda`$ does it first appear, and what is its first coefficient? The notation introduced below ($`c_1,c_2,\dots`$, $`J`$, $`J_k`$, $`P_k`$, $`Q_k`$, $`r`$, $`c_4^{(\beta_0)}`$) is fixed for later packages. "Probe", "body", "cell" and "link" are names only; no physical meaning is attached to them (M1, M4).

**Setting (two cells).**
- **Objects.** Four objects: the probe $`p`$, the body $`b`$, and the cells $`c_1`$ and $`c_2`$. They have pairwise different types, and each is the only instance of its type, so (1.11) imposes no constraint. The part is $`A=\{p\}`$, and its companion is $`\{b,c_1,c_2\}`$.
- **Contracts.** There are three pair contracts:
  ```math
  C=\sum_h\lvert h\rangle\langle h\rvert_p\otimes K_h+\sum_\beta\lvert\beta\rangle\langle\beta\rvert_b\otimes B_\beta+J .
  ```
  - $`K_h`$ is self-adjoint on $`\mathcal H_{c_1}`$: the probe is recorded by $`c_1`$ only.
  - $`B_\beta`$ is self-adjoint on $`\mathcal H_{c_2}`$: the body is recorded by $`c_2`$ only.
  - $`J`$ is a self-adjoint operator on $`\mathcal H_{c_1}\otimes\mathcal H_{c_2}`$, the link.

  Each operator acts as the identity on the other objects. Write the link as a finite sum $`J=\sum_kP_k\otimes Q_k`$ with $`P_k`$ self-adjoint on $`\mathcal H_{c_1}`$ and $`Q_k`$ self-adjoint on $`\mathcal H_{c_2}`$; such a decomposition always exists.
- **Initial state.** A product: $`\lvert\Psi(0)\rangle=\lvert\phi\rangle_p\otimes\lvert\beta_0\rangle_b\otimes\lvert\chi_1\rangle\otimes\lvert\chi_2\rangle`$, with $`\phi_h\neq0`$ for every $`h`$. Write $`\lvert\chi\rangle:=\lvert\chi_1\rangle\otimes\lvert\chi_2\rangle`$.
- **Notation.** For a pair $`h,h'`$ of places of $`p`$, $`D:=K_h-K_{h'}`$ and $`\tilde D:=D-\langle D\rangle`$, as in 06-body-in-medium. Here $`D`$ acts on $`c_1`$ only.

**Use of 06.** The derivation of (6.6)–(6.12) uses only three facts:
- $`K_h`$, $`K_{h'}`$ and the operator common to both branches are self-adjoint;
- they act on a finite-dimensional medium;
- the medium starts in a unit vector.

Here the medium is $`c_1c_2`$, and both branches share $`B_{\beta_0}+J`$. State this, and then apply (6.6)–(6.12) with $`\mathcal H_c\to\mathcal H_{c_1}\otimes\mathcal H_{c_2}`$, $`\lvert\chi\rangle\to\lvert\chi_1\rangle\otimes\lvert\chi_2\rangle`$ and $`B_{\beta_0}\to B_{\beta_0}+J`$.

1. **Exact evolution.** Derive $`\lvert\Psi(\lambda)\rangle`$. Show that the body stays at $`\beta_0`$, and give the probe's witness data,
   ```math
   W^{(\beta_0)}(h,h';\lambda)=\bigl\lvert\langle\chi\vert e^{i(K_{h'}+B_{\beta_0}+J)\lambda}e^{-i(K_h+B_{\beta_0}+J)\lambda}\vert\chi\rangle\bigr\rvert^2 .
   ```
   Define the body-dependent part of $`W^{(\beta_0)}`$ as $`W^{(\beta_0)}`$ minus its value at $`B_{\beta_0}=0`$.

2. **No link, no effect.** Show that for $`J=0`$ the body-dependent part vanishes for every $`\lambda`$.

3. **Delay through the link.** Expand
   ```math
   W^{(\beta_0)}=1-\lambda^2\mathrm{Var}_\chi(D)+\lambda^3c_3^{(\beta_0)}+\lambda^4c_4^{(\beta_0)}+O(\lambda^5).
   ```
   - (a) Show that the body-dependent part of $`c_3^{(\beta_0)}`$ vanishes.
   - (b) Derive the body-dependent part of $`c_4^{(\beta_0)}`$ in closed form, first in operator form and then through the decomposition $`J=\sum_kP_k\otimes Q_k`$ in the product state.
   - (c) For $`d_0(h,h')>0`$, derive the corresponding body-dependent part of the witness angle at order $`\lambda^3`$.

4. **Light cone on a chain.** Let the medium be a chain of cells $`c_1,\dots,c_L`$ with pairwise different types, each the only instance of its type. Neighbouring cells are joined by links $`J_k`$, self-adjoint on $`\mathcal H_{c_k}\otimes\mathcal H_{c_{k+1}}`$, and there are no other medium contracts. The probe is recorded by $`c_1`$ ($`K_h`$ on $`c_1`$), and the body by $`c_{r+1}`$ ($`B_\beta`$ on $`c_{r+1}`$), with $`0\le r\le L-1`$. The initial state is a product over all objects. Show that the body-dependent part of $`W^{(\beta_0)}(h,h';\lambda)`$ is $`O(\lambda^{3+r})`$. For $`r=0`$, the first nonzero term can be the $`\lambda^3`$ term of 06.

5. **Example.** Two qubit cells with Pauli matrices, $`\lvert\chi_1\rangle=\lvert\chi_2\rangle=\lvert0\rangle`$ where $`\sigma_z\lvert0\rangle=\lvert0\rangle`$.
   - The places of $`p`$ are $`h_1,\dots,h_n`$, with $`K_{h_i}=i\,X_1`$ and $`X_1:=\sigma_x+\sigma_z`$ on $`c_1`$.
   - The places of $`b`$ carry $`B_\beta=\beta\,\sigma_y`$ on $`c_2`$, with real $`\beta`$ labelling the places of $`b`$.
   - The link is $`J=g\,\sigma_y\otimes\sigma_x`$ with $`g>0`$.

   Derive $`c_3^{(\beta_0)}(h_i,h_j)`$, the body-dependent part of $`c_4^{(\beta_0)}(h_i,h_j)`$, and the body-dependent part of the witness angle at order $`\lambda^3`$. Contrast with the link $`J=g\,\sigma_z\otimes\sigma_z`$.

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

From 03-witness-distance@v1. Notation fixed there: $`\alpha(x,x'):=\arccos\sqrt{W(x,x')}\in[0,\pi/2]`$, and for places $`\alpha(h,h'):=\alpha([h],[h'])`$.

Eq. (3.5). Here $`\alpha`$ is a metric on $`X_V`$.

```math
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}}
=\frac{\lvert\langle h\vert V_A\vert h'\rangle\rvert}{\sqrt{\langle h\vert V_A\vert h\rangle\langle h'\vert V_A\vert h'\rangle}},\qquad h\in x,\ h'\in x' .
```

From 05-recording-contract@v1. In the setting of 05, the leading-order distance is defined as follows.

Eq. (5.10):

```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
```

From 06-body-in-medium@v1. These hold in the setting of 06:
- objects: probe $`p`$, body $`b`$ at $`\beta_0`$, and a single medium object $`c`$;
- contracts: $`K_h`$ and $`B_\beta`$, both acting on $`c`$;
- initial state: $`\lvert\phi\rangle\otimes\lvert\beta_0\rangle\otimes\lvert\chi\rangle`$.

There, $`D=K_h-K_{h'}`$, $`\tilde D=D-\langle D\rangle`$, and $`\mathrm i`$ is the imaginary unit.

Eq. (6.6):

```math
W^{(\beta_0)}(h,h';\lambda)=\frac{\lvert(V_A)_{hh'}\rvert^2}{p_hp_{h'}}=\bigl\lvert\langle\chi\vert e^{\mathrm i(K_{h'}+B_{\beta_0})\lambda}e^{-\mathrm i(K_h+B_{\beta_0})\lambda}\vert\chi\rangle\bigr\rvert^2 .
```

Eq. (6.7). This holds if $`[B_{\beta_0},K_h]=[B_{\beta_0},K_{h'}]=0`$.

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

Eq. (6.12):

```math
\alpha^{(\beta_0)}(h,h';\lambda)=\lambda d_0(h,h')+\lambda^2\alpha_2^{(\beta_0)}(h,h')+O(\lambda^3),\qquad
\alpha_2^{(\beta_0)}=-\frac{c_3^{(\beta_0)}}{2d_0},
```

## Assumptions

- The settings stated under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- Items 3–5 are expansions for $`\lambda\to0^+`$. Items 1 and 2 hold for every $`\lambda`$.

## Scope

- In scope:
  - the probe's witness data with the body recorded by a different cell;
  - the order and the first coefficient of the body-dependent part;
  - the light-cone bound on a chain;
  - the qubit example.
- Out of scope:
  - medium states that are not products;
  - identical-type objects (Law 5);
  - large $`\lambda`$;
  - the dependence of the effect on a distance in the derived geometry, as opposed to the number of links;
  - the relation to the cost $`L`$ (1.8), and motion;
  - any reading of $`\lambda`$ as time (M2), and any reading of the effect as gravity.

## Depth

- Item 1: short argument.
- Item 2: short argument.
- Item 3: derive. The Baker–Campbell–Hausdorff formula to third order and the cumulant expansion of $`\langle e^{-i\lambda H}\rangle`$ to fourth order may be used without proof.
- Item 4: short argument. A counting of operator supports and commutators suffices.
- Item 5: derive.

## Expected result

The main model expects the following. Derive each statement independently, and report any discrepancy in a sign or a factor.

- Item 2: an exact equality for every $`\lambda`$.
- Item 3:
  - the body-dependent part of $`c_3^{(\beta_0)}`$ is $`\mathrm{Im}\langle\chi\vert B_{\beta_0}\tilde D^2\vert\chi\rangle=0`$ in the product state;
  - the body-dependent part of $`c_4^{(\beta_0)}`$ is
    $`\tfrac16\langle\chi\vert\{\tilde D,[B_{\beta_0},[J,D]]\}\vert\chi\rangle=-\tfrac23\sum_k\mathrm{Im}\langle\chi_1\vert P_k\tilde D^2\vert\chi_1\rangle\,\mathrm{Im}\langle\chi_2\vert B_{\beta_0}Q_k\vert\chi_2\rangle ;`$
  - the body-dependent part of $`\alpha`$ at order $`\lambda^3`$ is $`-\lambda^3`$ times this quantity divided by $`2d_0`$.
- Item 4: the bound $`O(\lambda^{3+r})`$.
- Item 5:
  - $`c_3^{(\beta_0)}(h_i,h_j)=0`$;
  - the body-dependent part of $`c_4^{(\beta_0)}`$ is $`\tfrac43\,g\,\beta_0\,(i-j)^2`$;
  - the body-dependent part of $`\alpha`$ is $`-\tfrac23\,g\,\beta_0\,\lvert i-j\rvert\,\lambda^3`$;
  - for $`J=g\,\sigma_z\otimes\sigma_z`$ the body-dependent part of $`c_4^{(\beta_0)}`$ vanishes.

Give every main result a tag $`(8.k)`$.

Consistency checks, at most three, chosen from:
- with $`J=0`$ the body-dependent part vanishes, in agreement with (6.7);
- with $`B_{\beta_0}=\beta_0\mathbb 1`$ there is no effect;
- with the body recorded by $`c_1`$ instead of $`c_2`$ ($`r=0`$), the $`\lambda^3`$ term of (6.11) returns.

## Code

None.
