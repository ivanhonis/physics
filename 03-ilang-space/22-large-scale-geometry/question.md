# Question: 22-large-scale-geometry

- **Subproject:** 03-ilang-space
- **Package:** 22-large-scale-geometry
- **Equation tags:** (22.k)
- **Created:** 2026-10-09

## Goal

Determine when families of descriptions of growing size give a continuum-like derived space, its dimension, and its betweenness and shortest paths (geodesics). Do this for the three distances of the subproject:
- the witness angle $\alpha$ at fixed $\lambda$ (3.5);
- its small-$\lambda$ limit $d_0$ (5.10);
- the chain distance $\ell$ of the neighbour graph (4.6).

In particular, determine whether local records give a large-scale continuum through $\ell$, and whether its large-scale geometry is isotropic. This addresses criteria 4 and 5. The notions defined below (small-$\lambda$ chain distance, family, continuum-like, dimension of a family, betweenness, geodesic, isotropy) are fixed for later packages. They mean only what their definitions say (M1, M4, M5).

**Setting.** Every description has:
- a probe $b$ of type $T$ with places $h$, the only instance of $T$;
- a medium $c$, one object of another type;
- the recording contract $C=\sum_h\lvert h\rangle\langle h\rvert\otimes K_h$ of 05;
- the start $\lvert\phi\rangle\otimes\lvert\chi\rangle$ with $\phi_h\neq0$ for all $h$.

All distances are those of the view of $\{b\}$. In items 2 and 3 the medium is one object whose places are bit strings: $\mathcal H_c=\bigotimes_l\mathbb C^2$ over cells $l$, $\sigma_x^{[l]}$ acts on cell $l$, and $\lvert0\cdots0\rangle$ is the place with all bits $0$ (as in 15). $g(v,w):=\operatorname{Re}\langle v\vert w\rangle$ on $\mathcal H_c$.

**Definitions.**
- **Small-$\lambda$ chain distance.** $\ell_0(x,y):=\lim_{\lambda\to0^+}\ell(x,y;\lambda)/\lambda$, where the limit exists.
- **Family.** A sequence of descriptions $D_n$, $n=1,2,\dots$, with point sets $X_n$. One distance $d_n$ is chosen among: $d_0$; $\alpha(\cdot,\cdot;\lambda)$ at fixed $\lambda$; $\ell_0$; $\ell(\cdot,\cdot;\lambda)$ at fixed $\lambda$. Scales $s_n>0$ are given.
- **Continuum-like.** $(X_n,d_n/s_n)$ converges in the Gromov–Hausdorff sense to a compact length space $(Y,d_Y)$ with more than one point. The **dimension** of the family is the Hausdorff dimension of $Y$.
- **Betweenness.** For a distance $d$, a point $y$ is between $x$ and $z$ ($x\neq z$) iff $d(x,y)+d(y,z)=d(x,z)$.
- **Geodesic.**
  - For $\ell$: a neighbour chain from $x$ to $z$ whose $\alpha$-length equals $\ell(x,z)$ (a shortest chain).
  - For a length space $Y$: a curve from $x$ to $z$ of length $d_Y(x,z)$.
- **Isotropy.** If $Y$ is a subset of a finite-dimensional normed space with the norm distance, $Y$ is isotropic iff the norm is Euclidean, i.e. its unit ball is an ellipsoid.

1. **Direct distances.**
   - (a) **Square family of linear records.**
     - The family: places $h_{(i,j)}$ with $i,j\in\{0,\dots,n\}$, and $K_{h_{(i,j)}}=\tfrac in X+\tfrac jnY$ with $\sigma_X=\sigma_Y=\sigma>0$ and $\operatorname{Cov}_\chi(X,Y)=0$, as in (5.17)–(5.18).
     - Determine the Gromov–Hausdorff limit of $(X_n,d_0)$ ($s_n=1$), its dimension, its betweenness and its geodesics.
   - (b) **The same family under $\ell_0$.**
     - Determine $N_V$ for small $\lambda$. Where the assumptions of (11.11) fail (ties), decide the neighbour relation from (4.3) directly.
     - Determine $\ell_0$ and the Gromov–Hausdorff limit of $(X_n,\ell_0)$.
     - Compare it with (a): betweenness, geodesics (the number of shortest chains between two points), isotropy, and the largest value of $\ell_0/d_0$.
   - (c) **Qubit disc family at fixed $\lambda$.**
     - The family: $\mathcal H_c=\mathbb C^2$, $\chi=\lvert0\rangle$, and $K_h=x_h\sigma_x+y_h\sigma_y$, where $(x_h,y_h)$ runs over the points of $(r_0/n)\mathbb Z^2$ with $x^2+y^2\le r_0^2$.
     - For fixed $\lambda>0$ and $r_0>0$, determine:
       - the Gromov–Hausdorff limit of $(X_n,\alpha)$ and whether it is a length space;
       - its dimension and curvature;
       - its geodesics;
       - how these answers depend on $\lambda r_0$.

2. **Local records in one dimension.** The medium is a chain of qubit cells $l$, with $\chi=\lvert0\cdots0\rangle$, and $K_{h_i}=\sum_l\kappa(l-i)\,\sigma_x^{[l]}$ for the places $h_i$, $i=1,\dots,n$.
   - (a) **Compact windows.**
     - The family: $\kappa(s)=1$ for $s\in\{0,\dots,m-1\}$ and $0$ otherwise, with $m\ge2$. This is the window medium of 15, with $L=n+m-1$ cells.
     - For every $\lambda\in(0,\pi/2)$, determine $\alpha$, $N_V$ and $\ell$, and the diameter of $(X_n,\ell)$.
     - Determine whether $(X_n,\ell/s_n)$ is continuum-like for some choice of $s_n$.
   - (b) **Exponential tails.**
     - The family: $\kappa(s)=q^{\lvert s\rvert}$ with $0<q<1$, over the cells $l\in\mathbb Z$. Treat this as a limit of long finite chains with the places far from the ends, and state how the limit is taken.
     - Determine $d_0$, $N_V$ for small $\lambda$, $\ell_0$, and the Gromov–Hausdorff limit of $(X_n,\ell_0/n)$.
     - For pairs of places at index distance $r$, determine how large the differences of $d_0$ are on which the neighbour relation depends, as a function of $r$.

3. **Local records in two dimensions.**
   - (a) **Square grid with exponential tails.**
     - The family: the medium is a square grid of qubit cells $l\in\mathbb Z^2$ (as a limit, as in 2(b)), with $\chi=\lvert0\cdots0\rangle$. The places are $h_p$ with $p\in\{1,\dots,n\}^2$, and $K_{h_p}=\sum_lq^{\lvert l_1-p_1\rvert+\lvert l_2-p_2\rvert}\,\sigma_x^{[l]}$ with $0<q<1$.
     - Determine $d_0$, $N_V$ for small $\lambda$, and $\ell_0$.
     - Determine the Gromov–Hausdorff limit of $(X_n,\ell_0/n)$: its dimension, its betweenness, its geodesics (uniqueness and the number of shortest chains), and its isotropy.
   - (b) **Periodic arrangements.**
     - The family: descriptions invariant under a rank-2 lattice of translations that acts on the places and on the cells, whose small-$\lambda$ neighbour graph is periodic with finitely many edge orbits.
     - Determine whether the rescaled $\ell_0$ can converge to an isotropic limit. Standard results may be used; state them.

## Inputs

From 03-witness-distance@v1. Notation fixed there: points $x\in X_V$ are classes of present places with $W=1$; $\alpha(x,x'):=\arccos\sqrt{W(x,x')}\in[0,\pi/2]$. Eq. (3.5); here $\alpha$ is a metric on $X_V$:

$$
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}}
=\frac{\lvert\langle h\vert V_A\vert h'\rangle\rvert}{\sqrt{\langle h\vert V_A\vert h\rangle\langle h'\vert V_A\vert h'\rangle}},\qquad h\in x,\ h'\in x' .
$$

From 04-neighbours@v1. Eq. (4.1), related points:

$$
x\asymp x'\;:\Longleftrightarrow\;W(x,x')>0\;\Longleftrightarrow\;\alpha(x,x')<\pi/2 .
$$

Eq. (4.3), neighbours, for distinct $x,x'\in X_V$:

$$
x\sim x'\;:\Longleftrightarrow\;x\asymp x'\ \text{ and there is no } y\in X_V \text{ with } \max\bigl(\alpha(x,y),\alpha(y,x')\bigr)<\alpha(x,x') .
$$

$N_V$ is the graph on $X_V$ whose edges are the neighbour pairs. Eq. (4.6), the chain distance:

$$
\ell(x,x'):=\min\Bigl\{\sum_{j=0}^{m-1}\alpha(y_j,y_{j+1})\;:\;y_0=x,\ y_m=x',\ y_j\sim y_{j+1}\Bigr\},
\qquad \ell(x,x'):=+\infty\ \text{between components.}
$$

Eq. (4.7):

$$
\ell\ \text{is an extended metric on } X_V,\qquad \ell\ge\alpha,\qquad \ell(x,x')=\alpha(x,x')\ \text{ if } x\sim x' .
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

Eq. (5.17), for $K_{h_{(i,j)}}=iX+jY$, with $\Delta i:=i-i'$ and $\Delta j:=j-j'$:

$$
d_0\bigl(h_{(i,j)},h_{(i',j')}\bigr)=\sqrt{\sigma_X^2(\Delta i)^2+2\operatorname{Cov}_\chi(X,Y)\,\Delta i\,\Delta j+\sigma_Y^2(\Delta j)^2}\, .
$$

Eq. (5.18):

$$
d_0=\sigma\sqrt{(\Delta i)^2+(\Delta j)^2}\ \text{ for all pairs}
\iff
\sigma_X=\sigma_Y=\sigma>0\ \text{ and }\ \operatorname{Cov}_\chi(X,Y)=0 .
$$

From 11-cut-boundary@v1. In the recording setting, (11.11) holds for all sufficiently small $\lambda>0$ under two assumptions: the $u_h$ are pairwise distinct; and for all distinct places $x,y,x'$, $\max\bigl(d_0(x,y),d_0(y,x')\bigr)\neq d_0(x,x')$. Then every place is its own point, every two points are related, and

$$
x\sim x'\;\Longleftrightarrow\;\text{no }y\text{ with }\max\bigl(d_0(x,y),d_0(y,x')\bigr)<d_0(x,x') .
$$

From 15-bodies@v3, window medium. The medium is one object whose places are the bit strings of length $L$, with $\chi=\lvert0\cdots0\rangle$, windows $w_i:=\{i,\dots,i+m-1\}\subseteq\{1,\dots,L\}$, and records $K_{h_i}=\sum_{l\in w_i}\sigma_x^{[l]}$. $\lvert e_l\rangle$ is the place with only bit $l$ set. Eq. (15.17), where $D$ is the two-body distance of 15:

$$
\lvert u_{h_i}\rangle=\sum_{l\in w_i}\lvert e_l\rangle,\qquad
d_0(h_i,h_j)=\sqrt{\lvert w_i\triangle w_j\rvert}=\sqrt{2\min(\lvert i-j\rvert,m)},\qquad
D=\sqrt{2\min(\lvert i_1-i_2\rvert,m)} .
$$

From Step 9 of 15, verbatim: "**Medium state.** $K_{h_{i_1}h_{i_2}}=\sum_l\nu_l\,\sigma_x^{[l]}$ with $\nu_l:=[l\in w_{i_1}]+[l\in w_{i_2}]\in\{0,1,2\}$. The terms commute and act on different bits, and $e^{-i\theta\sigma_x}=\cos\theta-i\sin\theta\,\sigma_x$, so" Eq. (15.18), for the two-body states of 15:

$$
\lvert E_{i_1i_2}(\lambda)\rangle=\bigotimes_{l=1}^{L}\bigl(\cos(\nu_l\lambda)\lvert0\rangle-i\sin(\nu_l\lambda)\lvert1\rangle\bigr),\qquad
\bigl\lvert\langle E_{i_1'i_2'}\vert E_{i_1i_2}\rangle\bigr\rvert=\prod_{l}\bigl\lvert\cos\bigl((\nu_l-\nu_l')\lambda\bigr)\bigr\rvert .
$$

From 19-curvature@v2. Setting of 19: places labelled by $x\in U\subseteq\mathbb R^k$, records $K(x)$, branch states $\psi_x(\lambda)=e^{-iK(x)\lambda}\lvert\chi\rangle$ (without a body), and the background metric $g_{ab}(x;\lambda):=\operatorname{Re}\langle\partial_a\psi_x\vert\partial_b\psi_x\rangle-\operatorname{Re}\bigl(\langle\partial_a\psi_x\vert\psi_x\rangle\langle\psi_x\vert\partial_b\psi_x\rangle\bigr)$, the pullback of the Fubini–Study metric. Eq. (19.1):

$$
\alpha(x,x+\varepsilon v;\lambda)^2=\varepsilon^2g_{ab}(x;\lambda)v^av^b+O(\varepsilon^3),\qquad
\lim_{\varepsilon\to0^+}\frac{\alpha(x,x+\varepsilon v;\lambda)}{\varepsilon}=\sqrt{g_{ab}(x;\lambda)v^av^b}.
$$

For the qubit plane of 19 ($\mathcal H_c=\mathbb C^2$, $\chi=\lvert0\rangle$, $K(x,y)=x\sigma_x+y\sigma_y$, polar coordinates $(x,y)=r(\cos\phi,\sin\phi)$), from Step 11 of 19, verbatim: "$\psi_x=\cos t\,\lvert0\rangle+e^{\mathrm i\mu}\sin t\,\lvert1\rangle$ with $t=\lambda r$ and $\mu=\phi-\pi/2$." Eq. (19.16):

$$
g=\lambda^2\mathrm dr^2+\tfrac14\sin^2(2\lambda r)\,\mathrm d\phi^2,\qquad
g_{ab}=\lambda^2\frac{x^ax^b}{r^2}+\frac{\sin^2(2\lambda r)}{4r^2}\Bigl(\delta_{ab}-\frac{x^ax^b}{r^2}\Bigr),
$$

Eq. (19.17), where $\hat g=\lambda^{-2}g$:

$$
\hat\kappa=4\lambda^2,\qquad \kappa_g=4\qquad\text{wherever $g$ is non-degenerate, for every }\lambda>0 .
$$

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $\lambda$ (A5), and $\lambda\ge0$.
- Families of descriptions of growing size are limits in the sense of A1. Infinite media in 2(b) and 3(a) are limits of long finite ones; state how each limit is taken.
- Standard facts of metric geometry may be used without proof: Gromov–Hausdorff convergence, Hausdorff dimension, length spaces, normed spaces, the geometry of the round sphere and of $\mathbb{CP}^1$, and results on periodic metrics. State the facts used.

## Scope

- In scope:
  - the families listed in items 1–3;
  - the three distances $d_0$, $\alpha$, $\ell$ (with $\ell_0$);
  - betweenness, geodesics, dimension and isotropy of the limits.
- Out of scope:
  - random or non-periodic arrangements of records (a later package);
  - media with internal contracts;
  - bodies;
  - motion;
  - finite-$\lambda$ revivals beyond the stated ranges;
  - three or more dimensions;
  - any physical or spatial meaning beyond the definitions (M1, M4).

## Depth

- Item 1(a): short argument.
- Item 1(b): derive.
- Item 1(c): short argument.
- Item 2: derive.
- Item 3(a): derive.
- Item 3(b): standard (state the results and apply them).

## Expected result

- Item 1:
  - (a) and (c): limits named explicitly (metric space, dimension, curvature); geodesics and betweenness described; a case distinction in $\lambda r_0$ for (c).
  - (b): an explicit neighbour graph, a closed form for $\ell_0$, the limit, and a numerical value for the largest ratio.
- Item 2:
  - (a): exact $\alpha$, $N_V$, $\ell$, a value or bound for the diameter, and a yes/no answer.
  - (b): closed forms for $d_0$ and $\ell_0$, the limit, and an asymptotic expression in $r$.
- Item 3:
  - (a): explicit $d_0$, $N_V$ and $\ell_0$; the limit with its norm; a count of shortest chains; a yes/no answer for isotropy.
  - (b): a yes/no answer with the standard result it rests on.

Give every main result a tag $(22.k)$.

Consistency checks, at most three: for example $m=1$ or $q\to0$, the small-$\lambda r_0$ limit of 1(c) against 1(a), and dimensions.

## Code

None.
