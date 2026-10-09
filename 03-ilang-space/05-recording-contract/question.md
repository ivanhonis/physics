# Question: 05-recording-contract

- **Subproject:** 03-ilang-space
- **Package:** 05-recording-contract
- **Equation tags:** (5.k)
- **Created:** 2026-10-08

## Goal

Derive the witness geometry that a recording contract writes into the companion: the exact branch states, the witness data as functions of $\lambda$, and the leading-order geometry at small $\lambda$, together with its dimension. The notation introduced below ($K_h$, $\lvert\chi\rangle$, $u_h$, $d_0$) is fixed for later packages.

**Setting.** A description with two objects, $a$ and $c$, of different types. Each is the only instance of its type, so (1.11) imposes no constraint. The part is $A=\{a\}$ and the companion is $\bar A=\{c\}$. $T(a)$ has places $h\in H_{T(a)}$, and $\mathcal H_c:=\mathcal H_{T(c)}$ has dimension $d_c$. The contract system is a single contract between $a$ and $c$ of recording form,
$$C=\sum_{h\in H_{T(a)}}\lvert h\rangle\langle h\rvert\otimes K_h,\qquad K_h=K_h^{\dagger}\ \text{on }\mathcal H_c .$$
In this contract the place of $a$ controls the evolution of $c$. The initial state is a product, $\lvert\Psi(0)\rangle=\lvert\phi\rangle\otimes\lvert\chi\rangle$ with $\lvert\phi\rangle=\sum_h\phi_h\lvert h\rangle$, $\phi_h\neq0$ for every $h$, and $\lvert\chi\rangle$ a unit vector of $\mathcal H_c$. Expectation values and variances are taken in $\lvert\chi\rangle$: $\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle$ and $\operatorname{Var}_\chi X:=\langle X^2\rangle-\langle X\rangle^2$ for self-adjoint $X$ on $\mathcal H_c$.

1. **Exact evolution.** Derive $\lvert\Psi(\lambda)\rangle$ from (1.9). Show that the weights $p_h(\lambda)$ do not depend on $\lambda$, and that $H_V$ consists of all places of $a$. Give the branch states, and
   $$W(h,h';\lambda)=\bigl\lvert\langle\chi\vert e^{iK_{h'}\lambda}e^{-iK_h\lambda}\vert\chi\rangle\bigr\rvert^2 .$$

2. **Small $\lambda$.** Show that
   $$W(h,h';\lambda)=1-\lambda^2\operatorname{Var}_\chi(K_h-K_{h'})+O(\lambda^3),$$
   and that
   $$\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h'):=\bigl\lVert u_h-u_{h'}\bigr\rVert,\qquad \lvert u_h\rangle:=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .$$
   Here $\alpha(h,h';\lambda)$ is the witness angle between the points of $h$ and $h'$ in the view of $A$ at $\lambda$. The case $\operatorname{Var}_\chi(K_h-K_{h'})=0$ is included.

3. **Euclidean structure and dimension.** Regard $\mathcal H_c$ as a real Euclidean space with the inner product $\operatorname{Re}\langle\cdot\vert\cdot\rangle$. Show:
   - $d_0$ is the Euclidean distance of the record vectors $u_h$, so $(H_V,d_0)$ is isometric to the configuration $\{u_h\}$, up to identifying places with equal $u_h$;
   - $d_0(h,h')=0$ iff $(K_h-K_{h'})\lvert\chi\rangle$ is proportional to $\lvert\chi\rangle$;
   - every $u_h$ lies in the orthogonal complement of $\lvert\chi\rangle$.

   Define the leading-order dimension as the dimension of the real affine span of $\{u_h\}$. Bound it in terms of the number of places of $a$ and of $d_c$.

4. **Examples.**
   - (a) **Line.** The places of $a$ are $h_1,\dots,h_n$, and $K_{h_i}=i\,X$ with a self-adjoint $X$ on $\mathcal H_c$ and $\sigma_X:=\sqrt{\operatorname{Var}_\chi X}>0$. Derive $d_0(h_i,h_j)$ and the leading-order dimension. Show that $W(h_i,h_j;\lambda)$ depends on $i,j$ and $\lambda$ only through $(i-j)\lambda$, exactly, for all $\lambda$.
   - (b) **Plane.** The places of $a$ are $h_{(i,j)}$ with $i,j\in\{1,\dots,n\}$, $n\ge2$, and $K_{h_{(i,j)}}=i\,X+j\,Y$ with self-adjoint $X,Y$ on $\mathcal H_c$. Derive $d_0$. Determine when the leading-order geometry is the Euclidean square lattice, $d_0=\sigma\sqrt{(\Delta i)^2+(\Delta j)^2}$ for some $\sigma>0$, and when the leading-order dimension is $2$. State the conditions through $\sigma_X$, $\sigma_Y$ and $\operatorname{Cov}_\chi(X,Y):=\operatorname{Re}\langle u_X\vert u_Y\rangle$, where $\lvert u_X\rangle:=(X-\langle X\rangle)\lvert\chi\rangle$ and $\lvert u_Y\rangle$ is defined the same way.

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

From 03-witness-distance@v1. Notation fixed there: $h\approx h'$ iff $W(h,h')=1$; $X_V:=H_V/{\approx}$; $\alpha(x,x'):=\arccos\sqrt{W(x,x')}\in[0,\pi/2]$; for places, $\alpha(h,h'):=\alpha([h],[h'])$.

Eq. (3.1):

$$
\varrho_h:=\lvert E_h\rangle\langle E_h\rvert=\frac{\lvert\psi_h\rangle\langle\psi_h\rvert}{p_h},
\qquad
h\approx h'\;\Longleftrightarrow\;W(h,h')=1\;\Longleftrightarrow\;\varrho_h=\varrho_{h'} .
$$

Eq. (3.2):

$$
X_V:=H_V/{\approx},\qquad
\varrho_x:=\varrho_h,\qquad
W(x,x'):=W(h,h')=\operatorname{Tr}(\varrho_x\varrho_{x'})\qquad(h\in x,\ h'\in x'),
$$

Eq. (3.5). Here $\alpha$ is a metric on $X_V$.

$$
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}}
=\frac{\lvert\langle h\vert V_A\vert h'\rangle\rvert}{\sqrt{\langle h\vert V_A\vert h\rangle\langle h'\vert V_A\vert h'\rangle}},\qquad h\in x,\ h'\in x' .
$$

## Assumptions

- The setting stated under "Goal": two objects, the recording contract, and the product initial state. The places of $a$ are finitely many (A1), and $C$ does not depend on $\lambda$ (A5).
- $\lambda\ge0$. Item 2 is an expansion for $\lambda\to0^+$; all other statements hold for every $\lambda$.

## Scope

- In scope:
  - the exact evolution and the witness data for the recording contract;
  - the small-$\lambda$ expansion, and the leading-order geometry $d_0$ with its dimension;
  - the two examples.
- Out of scope:
  - contracts that change the weights of $a$;
  - large $\lambda$ (decay or revival of overlaps), and the neighbour structure of 04-neighbours at finite $\lambda$;
  - several parts, bodies and motion, and the locality of contracts;
  - any reading of $\lambda$ as physical time (M2), and any physical or spatial meaning beyond the definitions (M1, M4).

## Depth

- Item 1: derive.
- Item 2: derive.
- Item 3: short argument. That a complex Hilbert space with $\operatorname{Re}\langle\cdot\vert\cdot\rangle$ is a real Euclidean space of twice its complex dimension may be used without proof.
- Item 4 (a): derive.
- Item 4 (b): derive.

## Expected result

- Item 1: closed form of $\lvert\Psi(\lambda)\rangle$; $p_h(\lambda)=\lvert\phi_h\rvert^2$; the stated formula for $W$.
- Item 2: the expansion of $W$, and the limit $\alpha/\lambda\to\lVert u_h-u_{h'}\rVert$.
- Item 3: the isometry statement, the criterion for $d_0=0$, the orthogonality $\langle\chi\vert u_h\rangle=0$, and a bound on the leading-order dimension.
- Item 4: closed forms of $d_0$ in both examples. In (a), the exact dependence of $W$ on $(i-j)\lambda$ only. In (b), the conditions for the Euclidean square lattice and for dimension $2$.

Give every main result a tag $(5.k)$.

Consistency checks, at most three, chosen from:

- at $\lambda=0$ the state is a product, and $X_V$ is a single point;
- if all $K_h$ are equal, then $W\equiv1$ for all $\lambda$ and $d_0\equiv0$: nothing is recorded;
- if $\lvert\chi\rangle$ is an eigenvector of every $K_h$, then $W\equiv1$ for all $\lambda$ and every $u_h=0$: the companion only acquires phases.

## Code

None.
