# Question: 17-motion

- **Subproject:** 03-ilang-space
- **Package:** 17-motion
- **Equation tags:** (17.k)
- **Created:** 2026-10-08

## Goal

Determine how a body that can change its place moves in the background of a recording medium. Determine how its position changes with $\lambda$, whether the contract system bounds the rate of this change, and how the records of the medium affect the motion. The notions defined below (hopping graph, position $\bar x$, spread $s$, velocity $v$) are fixed for later packages. They mean only what their definitions say (M1, M4). The velocity is a rate of change with respect to the ordering parameter $\lambda$. Whether $\lambda$ can serve as a time is criterion 8 and not part of this package (M2).

**Setting.**
- **Objects.** A body $b$ of type $T$ with places $h\in H_T$ and $d_T\ge2$, the only instance of $T$. A medium $c$: one object of another type, the only instance of its type.
- **Contract.** One pair term between $b$ and $c$:
  $$C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h,\qquad C_b=\sum_{h,h'}t_{hh'}\lvert h\rangle\langle h'\rvert ,$$
  with complex numbers $t_{hh'}=t_{h'h}^*$ and $K_h$ self-adjoint on $\mathcal H_c$. By A5, the single-object term $C_b\otimes\mathbb 1_c$ is part of this pair term. The **hopping graph** joins two places $h\neq h'$ iff $t_{hh'}\neq0$.
- **Start.** $\lvert\phi\rangle\otimes\lvert\chi\rangle$ with unit vectors $\phi\in\mathcal H_T$ and $\chi\in\mathcal H_c$.
- **Notation.** $\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle$ and $\lvert u_h\rangle:=(K_h-\langle K_h\rangle)\lvert\chi\rangle$, as in (5.10). $V_b(\lambda)$ is the view of $\{b\}$, with place weights $p_h(\lambda)$ and witness data $W(h,h';\lambda)$ (2.11).

**Definitions.**
- **Background.** The geometry $(H_T/{\sim_0},d_0)$ of (5.10) and (5.11), built from the $u_h$, with $d_0(h,h')=\lVert u_h-u_{h'}\rVert$.
- **Position, spread, velocity.**
  $$\bar x(\lambda):=\sum_hp_h(\lambda)\,u_h,\qquad s(\lambda)^2:=\sum_hp_h(\lambda)\,\bigl\lVert u_h-\bar x(\lambda)\bigr\rVert^2,\qquad v(\lambda):=\frac{\mathrm d\bar x}{\mathrm d\lambda}.$$
  For a body whose present places all lie in one point $x$ of the background, $\bar x=u_x$ and $s=0$.

1. **Background and position.**
   - (a) Determine whether $d_0$ of the view of $b$, for a start with $\phi_h\neq0$ for all $h$, depends on the $t_{hh'}$.
   - (b) Determine whether $\bar x$, $s$ and $v$ are well defined (M6). Express $\lVert\bar x(\lambda)-u_h\rVert$ and $s(\lambda)$ through the $p_h(\lambda)$ and $d_0$ alone.

2. **Currents and maximal speed.** For every start and every $\lambda$:
   - (a) Determine $\mathrm dp_h/\mathrm d\lambda$ exactly, in terms of the $t_{hh'}$ and the matrix elements of $V_b$. Write the result as $\mathrm dp_h/\mathrm d\lambda=\sum_{h'}J_{h'\to h}$ with an antisymmetric current $J_{h'\to h}=-J_{h\to h'}$.
   - (b) Determine an upper bound on $\lvert J_{h'\to h}\rvert$ in terms of $\lvert t_{hh'}\rvert$, $p_h$, $p_{h'}$ and $W(h,h';\lambda)$.
   - (c) Determine $v(\lambda)$. Determine an upper bound on $\lVert v(\lambda)\rVert$ that holds for every start and every $\lambda$, in terms of the $t_{hh'}$ and the values of $d_0$ on the edges of the hopping graph.

3. **Localized start.** Let $\phi=\lvert\beta\rangle$. Determine $p_h(\lambda)$, $\bar x(\lambda)$, $s(\lambda)^2$ and $v(\lambda)$ at their leading nonvanishing orders in $\lambda$. Determine the lowest order in $\lambda$ at which the $K_h$ enter $p_h(\lambda)$, and the $K_h$-dependent part of the coefficient at that order.

4. **Commuting records.** Let the $K_h$ commute pairwise, with joint spectral decomposition $K_h=\sum_j\kappa_h(j)P_j$, where the $P_j$ are orthogonal projectors with $\sum_jP_j=\mathbb 1$. Determine $V_b(\lambda)$ exactly, in terms of evolutions on $\mathcal H_T$ and the weights $\langle\chi\vert P_j\vert\chi\rangle$.

5. **Example: chain with linear records.** Work on the infinite chain $h_m$, $m\in\mathbb Z$, as the limit of long finite chains with the start far from both ends (A1), and state how the limit is taken. Let $C_b=t\sum_m\bigl(\lvert h_m\rangle\langle h_{m+1}\rvert+\lvert h_{m+1}\rangle\langle h_m\rvert\bigr)$ with $t>0$, and $K_{h_m}=m\,X$, where $X=\sum_\xi\xi\,\Pi_\xi$ is self-adjoint on $\mathcal H_c$ (spectral decomposition) and $\sigma_X:=(\langle X^2\rangle-\langle X\rangle^2)^{1/2}>0$.
   - (a) For the start $\lvert h_0\rangle\otimes\lvert\chi\rangle$, determine $p_{h_m}(\lambda)$, $\bar x(\lambda)$ and $s(\lambda)^2$ for every $\lambda$, and the bound of item 2(c) for this chain.
   - (b) For the start $2^{-1/2}\bigl(\lvert h_0\rangle+e^{i\theta}\lvert h_1\rangle\bigr)\otimes\lvert\chi\rangle$ with real $\theta$, determine $\bar x(\lambda)$ and $v(\lambda)$ for every $\lambda$.
   - (c) Determine a necessary and sufficient condition on $X$ and $\chi$ under which $s(\lambda)$ of (a) stays bounded for all $\lambda$. Determine whether $\bar x(\lambda)$ of (b) then stays bounded.

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

From 03-witness-distance@v1. Notation fixed there: $h\approx h'$ iff $W(h,h')=1$; $X_V:=H_V/{\approx}$; $\alpha(x,x'):=\arccos\sqrt{W(x,x')}\in[0,\pi/2]$.

Eq. (3.5). Here $\alpha$ is a metric on $X_V$.

$$
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}}
=\frac{\lvert\langle h\vert V_A\vert h'\rangle\rvert}{\sqrt{\langle h\vert V_A\vert h\rangle\langle h'\vert V_A\vert h'\rangle}},\qquad h\in x,\ h'\in x' .
$$

From 05-recording-contract@v1. These hold in the setting of 05: one recorded object, one medium object, the recording contract $\sum_h\lvert h\rangle\langle h\rvert\otimes K_h$, and the start $\lvert\phi\rangle\otimes\lvert\chi\rangle$ with $\phi_h\neq0$ for all $h$. Notation fixed there: $g(v,w):=\operatorname{Re}\langle v\vert w\rangle$, and $h\sim_0h'$ iff $u_h=u_{h'}$.

Eq. (5.10):

$$
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
$$

Eq. (5.11):

$$
\bigl(H_V/{\sim_0},\,d_0\bigr)\;\cong\;\bigl(\{u_h:h\in H_V\},\,\lVert\cdot\rVert\bigr)\subset(\mathcal H_c,g).
$$

From 11-cut-boundary@v1. These hold in the setting of 11:
- A1–A7 hold, $\mathcal H=\mathcal H_A\otimes\mathcal H_{\bar A}$ for a part $A$ with $\bar A\neq\emptyset$, and no type has objects on both sides of the cut;
- $C=C_A+C_{\bar A}+C_\partial$, with $C_\partial=\sum_nA_n\otimes B_n$, $A_n=A_n^\dagger$ on $\mathcal H_A$ and $B_n=B_n^\dagger$ on $\mathcal H_{\bar A}$;
- the initial state is the product $\lvert\phi\rangle\otimes\lvert\chi\rangle$ with $\phi_h\neq0$ for every joint place $h$ of $A$, and $\langle B\rangle:=\langle\chi\vert B\vert\chi\rangle$;
- $Q_\chi:=\mathbb 1_{\bar A}-\lvert\chi\rangle\langle\chi\rvert$, and $v_h$ is the first-order coefficient of $\psi_h/\phi_h$ in (11.5).

Eq. (11.6):

$$
Q_\chi\lvert v_h\rangle=Q_\chi C_{\bar A}\lvert\chi\rangle+\lvert u_h\rangle,\qquad
\lvert u_h\rangle=\frac{1}{\phi_h}\,Q_\chi\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)C_\partial\bigl(\lvert\phi\rangle\otimes\lvert\chi\rangle\bigr).
$$

Eq. (11.8):

$$
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert .
$$

Eq. (11.10), when every $A_n$ is diagonal in the place basis:

$$
\lvert u_h\rangle=\sum_n\langle h\vert A_n\vert h\rangle\bigl(B_n-\langle B_n\rangle\bigr)\lvert\chi\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle,\qquad K_h:=\sum_n\langle h\vert A_n\vert h\rangle B_n=K_h^\dagger .
$$

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $\lambda$ (A5), and $\lambda\ge0$.
- Item 1(a) and item 3 are statements for $\lambda\to0^+$. Items 2, 4 and 5 are exact.

## Scope

- In scope:
  - one body that changes place by the hopping term and is recorded by one medium;
  - the items above, including the infinite-chain limit of item 5.
- Out of scope:
  - several bodies;
  - contracts internal to the medium, and media of several cells;
  - how the body's own records change the background seen by other objects;
  - a physical time (criterion 8);
  - examples with non-commuting records, and local (window) records with hopping;
  - any physical or spatial meaning beyond the definitions (M1, M2, M4).

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: derive.
- Item 4: short argument.
- Item 5: derive. Standard results for the evolution on the chain may be used; state them.

## Expected result

- Item 1: a yes/no answer; a statement on well-definedness; two identities.
- Item 2: an exact equation; an inequality; a closed form and an inequality.
- Item 3: leading-order expressions; an order, and the $K_h$-dependent part of its coefficient.
- Item 4: a closed form.
- Item 5: closed forms for $p_{h_m}$, $\bar x$, $s^2$ and $v$; the value of the bound; an equivalence and a yes/no answer.

Give every main result a tag $(17.k)$.

Consistency checks, at most three: for example no hopping ($t_{hh'}=0$ for $h\neq h'$), all $K_h$ equal, and $\sum_h\mathrm dp_h/\mathrm d\lambda=0$.

## Code

None.
