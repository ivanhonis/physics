# Question: 06-body-in-medium

- **Subproject:** 03-ilang-space
- **Package:** 06-body-in-medium
- **Equation tags:** (6.k)
- **Created:** 2026-10-08

## Goal

Determine whether, and how, a body changes the witness geometry that a probe sees in a recording medium. The notation introduced below ($p$, $b$, $c$, $K_h$, $B_\beta$, $\beta_0$, $W^{(\beta)}$, $D$, $\tilde D$, $c_3^{(\beta)}$) is fixed for later packages. "Probe", "body" and "medium" are names for the three objects; no physical meaning is attached to them (M1, M4).

**Setting.**
- **Objects.** A description with three objects: the probe $p$, the body $b$ and the medium $c$. The three have pairwise different types, and each is the only instance of its type, so (1.11) imposes no constraint. The part is $A=\{p\}$, and its companion is $\bar A=\{b,c\}$. $\mathcal H_c:=\mathcal H_{T(c)}$ is finite-dimensional (A1).
- **Contracts.** There are two recording contracts, one between $p$ and $c$ and one between $b$ and $c$:
  $$C=\sum_{h}\lvert h\rangle\langle h\rvert_p\otimes K_h+\sum_{\beta}\lvert\beta\rangle\langle\beta\rvert_b\otimes B_\beta ,$$
  where $h$ runs over the places of $p$ and $\beta$ over the places of $b$. Each $K_h$ and $B_\beta$ is self-adjoint on $\mathcal H_c$ and acts as the identity on the third object. The two contracts both act on $c$ and need not commute.
- **Initial state.** The initial state is a product, $\lvert\Psi(0)\rangle=\lvert\phi\rangle_p\otimes\lvert\beta_0\rangle_b\otimes\lvert\chi\rangle_c$. Here $\lvert\phi\rangle=\sum_h\phi_h\lvert h\rangle$ with $\phi_h\neq0$ for every $h$, the body sits at the single place $\beta_0$, and $\lvert\chi\rangle$ is a unit vector.
- **Expectations.** Expectations are taken in $\lvert\chi\rangle$, as in 05-recording-contract: $\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle$. For a pair of places $h,h'$ of $p$, write $D:=K_h-K_{h'}$ and $\tilde D:=D-\langle D\rangle$.

1. **Exact evolution.** Derive $\lvert\Psi(\lambda)\rangle$. Show that the body stays at $\beta_0$, and that the weights of $p$ do not depend on $\lambda$. Derive the witness data of the probe:
   $$W^{(\beta_0)}(h,h';\lambda)=\bigl\lvert\langle\chi\vert e^{i(K_{h'}+B_{\beta_0})\lambda}e^{-i(K_h+B_{\beta_0})\lambda}\vert\chi\rangle\bigr\rvert^2 .$$
   Note that $W^{(\beta_0)}$ with $B_{\beta_0}=0$ is the witness data (5.6) of the medium without the body.

2. **No effect for commuting records.** Show that if $B_{\beta_0}$ commutes with $K_h$ and with $K_{h'}$, then $W^{(\beta_0)}(h,h';\lambda)$ equals its value at $B_{\beta_0}=0$ for every $\lambda$. In particular, a body whose record operator is a multiple of the identity has no effect.

3. **Small $\lambda$.** Expand to third order:
   $$W^{(\beta_0)}(h,h';\lambda)=1-\lambda^2\operatorname{Var}_\chi(D)+\lambda^3c_3^{(\beta_0)}(h,h')+O(\lambda^4).$$
   Show that the second-order term does not depend on the body. Derive $c_3^{(\beta_0)}$ explicitly, and separate it into its value at $B_{\beta_0}=0$ and the body-dependent part. For $d_0(h,h')>0$, derive the corresponding expansion of the witness angle to second order: $\alpha^{(\beta_0)}(h,h';\lambda)=\lambda d_0(h,h')+\lambda^2\alpha_2^{(\beta_0)}(h,h')+O(\lambda^3)$.

4. **Example.** The medium is a qubit, $\mathcal H_c=\mathbb C^2$ with Pauli matrices $\sigma_x,\sigma_y,\sigma_z$, and $\lvert\chi\rangle=\lvert0\rangle$ with $\sigma_z\lvert0\rangle=\lvert0\rangle$. The places of $p$ are $h_1,\dots,h_n$ with $K_{h_i}=i\,X$, where $X:=\sigma_x+\sigma_z$. The places of $b$ carry $B_{\beta}=\beta\,\sigma_y$, with $\beta$ ranging over a finite set of real numbers that label the places of $b$. Derive $W^{(\beta_0)}(h_i,h_j;\lambda)$ to order $\lambda^3$ and $\alpha^{(\beta_0)}(h_i,h_j;\lambda)$ to order $\lambda^2$. Describe how the probe's distances depend on the place $\beta_0$ of the body. Contrast with $B_\beta=\beta X$, which commutes with every $K_{h_i}$.

## Inputs

From 02-view-content@v1. Notation fixed there: $p_h:=\langle h\vert V_A\vert h\rangle$, $H_V:=\{h:p_h>0\}$, $\lvert\psi_h\rangle:=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle$, $G_{hh'}=\langle E_{h'}\vert E_h\rangle$.

Eq. (2.1):

$$
\lvert\Psi\rangle=\sum_h\lvert h\rangle\otimes\lvert\psi_h\rangle,
\qquad
\lvert\psi_h\rangle=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle=\sum_r\Psi_{hr}\lvert r\rangle,
\qquad
\sum_h\lVert\psi_h\rVert^2=\lVert\Psi\rVert^2=1 .
$$

Eq. (2.2):

$$
V_A=\sum_{h,h'}\langle\psi_{h'}\vert\psi_h\rangle\,\lvert h\rangle\langle h'\rvert,
\qquad\text{i.e.}\qquad
(V_A)_{hh'}=\langle\psi_{h'}\vert\psi_h\rangle,
\qquad
p_h=\lVert\psi_h\rVert^2 .
$$

Eq. (2.11):

$$
W(h)=1,\qquad W(h,h')=\lvert G_{hh'}\rvert^2=\frac{\lvert(V_A)_{hh'}\rvert^2}{p_hp_{h'}} .
$$

From 03-witness-distance@v1. Notation fixed there: $\alpha(x,x'):=\arccos\sqrt{W(x,x')}\in[0,\pi/2]$, and for places $\alpha(h,h'):=\alpha([h],[h'])$.

Eq. (3.5). Here $\alpha$ is a metric on $X_V$.

$$
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}}
=\frac{\lvert\langle h\vert V_A\vert h'\rangle\rvert}{\sqrt{\langle h\vert V_A\vert h\rangle\langle h'\vert V_A\vert h'\rangle}},\qquad h\in x,\ h'\in x' .
$$

From 05-recording-contract@v1. These hold in the setting of 05: two objects $a$ and $c$, the part $A=\{a\}$, the recording contract $C=\sum_h\lvert h\rangle\langle h\rvert\otimes K_h$, and the initial state $\lvert\phi\rangle\otimes\lvert\chi\rangle$. In (5.9), $D=K_h-K_{h'}$.

Eq. (5.1):

$$
e^{-iC\lambda}=\sum_h\lvert h\rangle\langle h\rvert\otimes e^{-iK_h\lambda},
$$

Eq. (5.6):

$$
W(h,h';\lambda)=\bigl\lvert\langle\chi\vert e^{iK_{h'}\lambda}e^{-iK_h\lambda}\vert\chi\rangle\bigr\rvert^2 .
$$

Eq. (5.8):

$$
W(h,h';\lambda)=1-\lambda^2\operatorname{Var}_\chi(K_h-K_{h'})+O(\lambda^3).
$$

Eq. (5.9):

$$
\operatorname{Var}_\chi(K_h-K_{h'})=\langle\chi\vert(D-\langle D\rangle)^2\vert\chi\rangle=\bigl\lVert u_h-u_{h'}\bigr\rVert^2 .
$$

Eq. (5.10):

$$
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
$$

## Assumptions

- The setting stated under "Goal". The contracts do not depend on $\lambda$ (A5), and $\lambda\ge0$.
- Items 3 and 4 are expansions for $\lambda\to0^+$. The other statements hold for every $\lambda$.

## Scope

- In scope:
  - the probe's witness data in the presence of a body localized at one place;
  - the commuting case;
  - the expansion to third order in $W$ and to second order in $\alpha$;
  - the qubit example.
- Out of scope:
  - bodies in superposition, and identical-type probes or bodies (Law 5);
  - media with many objects, and any dependence of the effect on a distance between probe and body;
  - the relation of the effect to the cost $L$ (1.8) of the body;
  - large $\lambda$, motion, and the neighbour structure of 04-neighbours;
  - any reading of $\lambda$ as time (M2), and any reading of the effect as gravity.

## Depth

- Item 1: derive.
- Item 2: short argument.
- Item 3: derive. Standard expansions (Baker–Campbell–Hausdorff to third order, cumulant expansion of $\langle e^{-i\lambda H}\rangle$) may be used without proof.
- Item 4: derive.

## Expected result

- Item 1: closed forms of $\lvert\Psi(\lambda)\rangle$ and of $W^{(\beta_0)}$; the body stays at $\beta_0$.
- Item 2: an exact equality for every $\lambda$.
- Item 3: an explicit formula for $c_3^{(\beta_0)}$ and for $\alpha_2^{(\beta_0)}$. The main model expects the body-dependent part of $c_3^{(\beta_0)}$ to be $\operatorname{Im}\langle\chi\vert B_{\beta_0}\tilde D^{\,2}\vert\chi\rangle$, and $\alpha_2^{(\beta_0)}=-c_3^{(\beta_0)}/(2d_0)$. Derive both and report any discrepancy.
- Item 4: closed forms to the stated orders. The main model expects $c_3^{(\beta_0)}=2\beta_0(i-j)^2$ and $\alpha^{(\beta_0)}(h_i,h_j;\lambda)=\lambda\lvert i-j\rvert\,(1-\beta_0\lambda)+O(\lambda^3)$, and no effect for $B_\beta=\beta X$. Derive these and report any discrepancy.

Give every main result a tag $(6.k)$.

Consistency checks, at most three, chosen from:
- with $B_{\beta_0}=0$ the results reduce to (5.6), (5.8) and (5.10);
- with $B_{\beta_0}=\beta_0\mathbb 1$ there is no effect;
- in item 4 with $B_\beta=\beta X$ there is no effect, in agreement with item 2.

## Code

None.
