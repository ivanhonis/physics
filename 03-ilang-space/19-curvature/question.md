# Question: 19-curvature

- **Subproject:** 03-ilang-space
- **Package:** 19-curvature
- **Equation tags:** (19.k)
- **Created:** 2026-10-08

## Goal

Determine the curvature of the derived background, and how it changes with the state: with the state of the medium and with a body. The curvature is defined below as the curvature of the infinitesimal form of the witness angle on a dense family of places. The notions defined below (record family, background metric $g$, rescaled metric $\hat g$, background curvature) are fixed for later packages. They mean only what their definitions say (M1, M4). The parameter $x$ below only labels places of the description and carries no geometry of its own; all geometry comes from the witness angle (3.5).

**Setting.**
- **Objects.** All objects have pairwise different types, and each is the only instance of its type, so (1.11) imposes no constraint.
  - A probe $a$, whose places $h$ are labelled by points $x_h$ of an open set $U\subseteq\mathbb R^k$.
  - A medium $c$: one object, or in example 4(b) two cells.
  - Optionally a body $b$, localized at $\beta_0$, with record operator $B:=B_{\beta_0}$ as in 06. Without a body, set $B=0$.
- **Record family.** A smooth map $x\mapsto K(x)$ from $U$ to self-adjoint operators on $\mathcal H_c$, with $K_h=K(x_h)$.
  - The contract is $C=\sum_h\lvert h\rangle\langle h\rvert_a\otimes K_h$, plus $\sum_\beta\lvert\beta\rangle\langle\beta\rvert_b\otimes B_\beta$ if the body is present.
  - The start is $\lvert\phi\rangle_a\,(\otimes\lvert\beta_0\rangle_b)\otimes\lvert\chi\rangle_c$, with $\phi_h\neq0$ for all $h$.
  - We consider families of descriptions whose places become dense in $U$ (A1); state how the limit is taken.
- **Branch states.** $\psi_x(\lambda):=e^{-\mathrm i(K(x)+B)\lambda}\lvert\chi\rangle$ for $x\in U$. By (5.4) and (6.6), the witness weight of two places is $W(x,x';\lambda)=\lvert\langle\psi_{x'}(\lambda)\vert\psi_x(\lambda)\rangle\rvert^2$.
- **Notation.** $\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle$, $\tilde X:=X-\langle X\rangle$, $\partial_a:=\partial/\partial x^a$. The record map is $u(x):=\widetilde{K(x)}\,\chi$, as in (5.10), and $g(v,w):=\operatorname{Re}\langle v\vert w\rangle$ on $\mathcal H_c$.

**Definitions.**
- **Background metric.** The pullback of the Fubini–Study metric by $x\mapsto\psi_x(\lambda)$:
  $$g_{ab}(x;\lambda):=\operatorname{Re}\langle\partial_a\psi_x\vert\partial_b\psi_x\rangle-\operatorname{Re}\bigl(\langle\partial_a\psi_x\vert\psi_x\rangle\langle\psi_x\vert\partial_b\psi_x\rangle\bigr),\qquad \hat g_{ab}:=\lambda^{-2}g_{ab}.$$
- **Background curvature.** The Riemann curvature of $g$, or of $\hat g$, wherever the metric is non-degenerate. For $k=2$ this is the Gaussian curvature.

1. **Metric.**
   - (a) Determine the relation between $g$ and the witness angle of nearby places, $\alpha(x,x+\varepsilon v;\lambda)$ as $\varepsilon\to0$.
   - (b) Determine $\hat g_{ab}(x;\lambda)=\hat g^{(0)}_{ab}(x)+\lambda\,\hat g^{(1)}_{ab}(x)+O(\lambda^2)$ in terms of $K$, $\partial K$, $\chi$ and $B$. Express $\hat g^{(0)}$ through the record map $u$, and split $\hat g^{(1)}$ into a body-free part and a body part.
   - (c) Relate $\hat g^{(0)}$ and $\hat g^{(1)}$ to (5.10) and to (6.9)–(6.11) at infinitesimal separation.

2. **Leading-order curvature.**
   - (a) Determine the curvature of $\hat g^{(0)}$ in terms of the record map $u$ and its derivatives.
   - (b) Determine a sufficient condition under which $\hat g^{(0)}$ is flat.
   - (c) Determine whether $\hat g^{(0)}$ and its curvature depend on the body, and how they depend on the medium state $\chi$.

3. **Body-induced curvature** ($k=2$).
   - (a) Determine the change of the Gaussian curvature of $\hat g$ at order $\lambda$ caused by the body part of $\hat g^{(1)}$.
   - (b) Determine a sufficient condition under which this change vanishes.

4. **Examples** ($k=2$).
   - (a) **Qubit plane.** $\mathcal H_c=\mathbb C^2$, $\lvert\chi\rangle=\lvert0\rangle$ with $\sigma_z\lvert0\rangle=\lvert0\rangle$, and $K(x,y)=x\,\sigma_x+y\,\sigma_y$.
     - Without a body, determine $g(x,y;\lambda)$ exactly for every $\lambda$, and its Gaussian curvature.
     - With a body whose $B$ is an arbitrary self-adjoint operator on $\mathbb C^2$, determine whether the Gaussian curvature of $g$ changes where $g$ is non-degenerate.
   - (b) **Commuting plane.** Two qubit cells $c_1,c_2$ of different types, $\lvert\chi\rangle=\lvert0\rangle\otimes\lvert0\rangle$, $K(x,y)=x\,\sigma_x^{(1)}+y\,\sigma_x^{(2)}$, no body. Determine $g$ exactly for every $\lambda$, and its Gaussian curvature.
   - (c) **Curved record map.** $\mathcal H_c=\mathbb C^3$ with orthonormal basis $e_1=\chi,e_2,e_3$, and $K(\theta,\varphi)=\lvert u(\theta,\varphi)\rangle\langle e_1\rvert+\lvert e_1\rangle\langle u(\theta,\varphi)\rvert$ with
     $$u(\theta,\varphi)=R\bigl(\sin\theta\cos\varphi\,e_2+\sin\theta\sin\varphi\,e_3+\cos\theta\,\mathrm i\,e_2\bigr),\qquad R>0,\quad 0<\theta<\pi,\ 0<\varphi<2\pi .$$
     Determine $\hat g^{(0)}$ and its Gaussian curvature. Determine the body part of $\hat g^{(1)}$ for every self-adjoint $B$ on $\mathbb C^3$.

## Inputs

From 03-witness-distance@v1. Notation fixed there: $h\approx h'$ iff $W(h,h')=1$; $X_V:=H_V/{\approx}$; $\alpha(x,x'):=\arccos\sqrt{W(x,x')}\in[0,\pi/2]$.

Eq. (3.5). Here $\alpha$ is a metric on $X_V$.

$$
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}}
=\frac{\lvert\langle h\vert V_A\vert h'\rangle\rvert}{\sqrt{\langle h\vert V_A\vert h\rangle\langle h'\vert V_A\vert h'\rangle}},\qquad h\in x,\ h'\in x' .
$$

From 05-recording-contract@v1. These hold in the setting of 05: one recorded object, one medium object, the recording contract $\sum_h\lvert h\rangle\langle h\rvert\otimes K_h$, and the start $\lvert\phi\rangle\otimes\lvert\chi\rangle$ with $\phi_h\neq0$ for all $h$. Notation fixed there: $h\sim_0h'$ iff $u_h=u_{h'}$.

Eq. (5.4), the unit branch states:

$$
\lvert E_h(\lambda)\rangle=e^{-iK_h\lambda}\lvert\chi\rangle,\qquad
\varrho_h(\lambda)=e^{-iK_h\lambda}\lvert\chi\rangle\langle\chi\rvert e^{iK_h\lambda}.
$$

Eq. (5.6):

$$
W(h,h';\lambda)=\bigl\lvert\langle\chi\vert e^{iK_{h'}\lambda}e^{-iK_h\lambda}\vert\chi\rangle\bigr\rvert^2 .
$$

Eq. (5.10):

$$
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
$$

Eq. (5.11):

$$
\bigl(H_V/{\sim_0},\,d_0\bigr)\;\cong\;\bigl(\{u_h:h\in H_V\},\,\lVert\cdot\rVert\bigr)\subset(\mathcal H_c,g).
$$

From 06-body-in-medium@v1. Setting of 06:
- a probe $p$ with records $K_h$, a body $b$ localized at $\beta_0$ with records $B_\beta$, and a medium $c$, of pairwise different types;
- $C=\sum_h\lvert h\rangle\langle h\rvert_p\otimes\mathbb 1_b\otimes K_h+\sum_\beta\mathbb 1_p\otimes\lvert\beta\rangle\langle\beta\rvert_b\otimes B_\beta$, and the start $\lvert\phi\rangle_p\otimes\lvert\beta_0\rangle_b\otimes\lvert\chi\rangle$ with $\phi_h\neq0$;
- $D:=K_h-K_{h'}$ and $\tilde D:=D-\langle D\rangle$; $W^{(\beta_0)}$ is the witness weight of the view of $\{p\}$.

In this question 06's probe is the probe $a$, and $B=B_{\beta_0}$.

Eq. (6.6):

$$
W^{(\beta_0)}(h,h';\lambda)=\frac{\lvert(V_A)_{hh'}\rvert^2}{p_hp_{h'}}=\bigl\lvert\langle\chi\vert e^{\mathrm i(K_{h'}+B_{\beta_0})\lambda}e^{-\mathrm i(K_h+B_{\beta_0})\lambda}\vert\chi\rangle\bigr\rvert^2 .
$$

Eq. (6.9):

$$
W^{(\beta_0)}(h,h';\lambda)=1-\lambda^2\operatorname{Var}_\chi(D)+\lambda^3c_3^{(\beta_0)}(h,h')+O(\lambda^4),
$$

Eq. (6.10):

$$
c_3^{(\beta_0)}(h,h')=\operatorname{Im}\langle\chi\vert\,(K_{h'}+B_{\beta_0})\,\tilde D^2\vert\chi\rangle ,
$$

Eq. (6.11):

$$
c_3^{(\beta_0)}=c_3^{(0)}+\operatorname{Im}\langle\chi\vert B_{\beta_0}\tilde D^2\vert\chi\rangle,\qquad
c_3^{(0)}(h,h')=\operatorname{Im}\langle\chi\vert K_{h'}\tilde D^2\vert\chi\rangle,\qquad
\operatorname{Im}\langle\chi\vert B_{\beta_0}\tilde D^2\vert\chi\rangle=\frac{\langle\chi\vert[B_{\beta_0},\tilde D^2]\vert\chi\rangle}{2\mathrm i}.
$$

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $\lambda$ (A5), and $\lambda\ge0$. The map $x\mapsto K(x)$ is smooth.
- The expansions in $\lambda$ are taken at fixed $x$ as $\lambda\to0^+$. Curvatures are computed where the metric in question is non-degenerate.
- Item 4(a) and 4(b) ask for exact results at every $\lambda$.

## Scope

- In scope:
  - the background metric and its curvature on a dense family of places;
  - the leading order and the first correction in $\lambda$, and the effect of one body;
  - the three examples.
- Out of scope:
  - the chain distance of 04 and its continuum limit;
  - media of many cells with links, and the locality of curvature;
  - the relation of curvature to the cost (later work);
  - a physical time (criterion 8 is handed over);
  - any physical or spatial meaning beyond the definitions (M1, M2, M4).

## Depth

- Item 1: derive.
- Item 2: derive.
- Item 3: derive. Standard formulas of Riemannian geometry, such as the first variation of the Gaussian curvature, may be used; state them.
- Item 4: derive.

## Expected result

- Item 1: a relation between $g$ and $\alpha$; closed forms for $\hat g^{(0)}$ and $\hat g^{(1)}$, with the body part separated; statements relating them to (5.10) and (6.9)–(6.11).
- Item 2: a closed-form curvature formula; a sufficient condition; statements on the dependence on the body and on $\chi$.
- Item 3: a closed-form formula; a sufficient condition.
- Item 4: closed forms for $g$ or $\hat g$ and for the curvatures; yes/no answers where asked.

Give every main result a tag $(19.k)$.

Consistency checks, at most three: for example $k=1$, $B=0$, and a constant rescaling $K\to sK$.

## Code

None.
