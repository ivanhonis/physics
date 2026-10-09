# Large-scale geometry of the derived space: continuum limits, dimension, betweenness and geodesics

- **Subproject:** 03-ilang-space
- **Package:** 22-large-scale-geometry
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-09

## Setup and assumptions

- **Setting (question.md).**
  - Probe $b$ with places $h$, the only instance of its type, and medium $c$.
  - Recording contract $C=\sum_h\lvert h\rangle\langle h\rvert\otimes K_h$, start $\lvert\phi\rangle\otimes\lvert\chi\rangle$ with all $\phi_h\neq0$, and $\lambda\ge0$.
  - All distances are those of the view of $\{b\}$. In items 2–3 the medium is one object made of qubit cells, with $\chi=\lvert0\cdots0\rangle$.
- **Inputs, as quoted:** $\alpha$ (3.5); (4.1); neighbours (4.3) and $N_V$; $\ell$ (4.6)–(4.7); $d_0,u_h$ (5.10)–(5.11); (5.17)–(5.18); the hypotheses of (11.11); (15.17); (15.18) with Step 9 of 15; the qubit-plane branch state of 19; (19.16)–(19.17).
- **Definitions** ($\ell_0$, family, continuum-like, dimension, betweenness, geodesic, isotropy): as in question.md. Infinite media are limits of finite ones, fixed in Step 1.
- **Standard facts used (M5):**
  - (G1) If finite sets $A_n$ in a metric space $Z$ converge in Hausdorff distance to a compact $Y\subseteq Z$, then $(A_n,d_Z)\to(Y,d_Z)$ in the Gromov–Hausdorff (GH) sense. The diameter is GH-continuous.
  - (G2) A compact length space is geodesic, so any two of its points have a midpoint.
  - (G3) Euclidean plane: $y$ is between $x$ and $z$ iff $y\in[x,z]$, and the segment is the unique geodesic. For $\lVert v\rVert_1=\lvert v_1\rvert+\lvert v_2\rvert$: $y$ is between iff each $y_k$ lies between $x_k$ and $z_k$ (the box), and the geodesics are the curves with both coordinates monotone. Convex sets of normed planes are length spaces.
  - (G4) A bi-Lipschitz image of a planar set with interior has Hausdorff dimension 2; that of a segment has dimension 1.
  - (G5) Bloch sphere: for unit $\psi,\psi'\in\mathbb C^2$ with Bloch vectors $\mathbf n,\mathbf n'$, $\lvert\langle\psi'\vert\psi\rangle\rvert=\cos(\Theta/2)$ with $\Theta=\angle(\mathbf n,\mathbf n')$. Hence $\arccos\lvert\langle\cdot\vert\cdot\rangle\rvert$ is the great-circle distance of the round sphere $\mathbb S$ of radius $1/2$, which has Gaussian curvature 4.
  - (G6) Periodic metrics: stated in Step 10.

## Derivation

### Step 1. Witness angle in the recording setting

$C$ is block-diagonal in the places of $b$. Hence $\lvert\Psi(\lambda)\rangle=\sum_h\phi_h\lvert h\rangle\otimes\lvert E_h\rangle$ with $\lvert E_h\rangle=e^{-iK_h\lambda}\lvert\chi\rangle$. By (1.7), $\langle h\vert V\vert h'\rangle=\phi_h\phi_{h'}^*\langle E_{h'}\vert E_h\rangle$ and $p_h=\lvert\phi_h\rvert^2$, so (3.5) gives

$$
\cos\alpha(h,h';\lambda)=\bigl\lvert\langle E_{h'}(\lambda)\vert E_h(\lambda)\rangle\bigr\rvert .
\tag{22.1}
$$

Places are the same point iff their branch states agree up to a phase.

**Qubit cells.** Let $K_h=\sum_lk_{h,l}\sigma_x^{[l]}$ with $k_{h,l}$ real. As in Step 9 of 15, $\lvert E_h\rangle=\bigotimes_l\bigl(\cos(k_{h,l}\lambda)\lvert0\rangle-i\sin(k_{h,l}\lambda)\lvert1\rangle\bigr)$, and one cell contributes the overlap $\cos(k_{h',l}\lambda)\cos(k_{h,l}\lambda)+\sin(k_{h',l}\lambda)\sin(k_{h,l}\lambda)$. This is (15.18) for one probe, with $\nu_l\to k_{h,l}$. Moreover $\langle\chi\vert\sigma_x^{[l]}\vert\chi\rangle=0$ and $\sigma_x^{[l]}\lvert\chi\rangle=\lvert e_l\rangle$ (orthonormal), so (5.10) gives

$$
\cos\alpha(h,h';\lambda)=\prod_l\bigl\lvert\cos(\lambda\Delta_l)\bigr\rvert,\qquad \Delta_l:=k_{h,l}-k_{h',l},\qquad
\lvert u_h\rangle=\sum_lk_{h,l}\lvert e_l\rangle,\qquad d_0(h,h')^2=\sum_l\Delta_l^2 .
\tag{22.2}
$$

**Infinite media.** In 2(b) and 3(a), $0<k_{h,l}\le1$ and $\sum_l\Delta_l^2<\infty$.
- The finite description $D_{n,R}$ keeps the places and has the cells $\Lambda_R=\{1-R,\dots,n+R\}$ (in 3(a), $\Lambda_R^2$). Each $K_h$ is truncated to these cells.
- For $0<\lambda<\pi/2$ every factor in (22.2) lies in $(0,1]$, so the product converges as $R\to\infty$, at fixed $n$ and $\lambda$.
- **The limit description** is defined by $\alpha:=\lim_R\alpha^{(R)}$ and $d_0:=\lim_Rd_0^{(R)}$, that is, by (22.2) with $l$ running over $\mathbb Z$ (resp. $\mathbb Z^2$). $N_V$, $\ell$ and $\ell_0$ are computed from this $\alpha$.
- Since $-\ln\cos x=\tfrac{x^2}2(1+O(x^2))$ uniformly for $\lvert x\rvert\le1$, and $\sum_l\Delta_l^4\le\sum_l\Delta_l^2$,

$$
\alpha(h,h';\lambda)=\lambda\,d_0(h,h')\bigl(1+O(\lambda^2)\bigr)\quad\text{uniformly in the pair}.
\tag{22.3}
$$

- Translation invariance. The product runs over all cells, and $\kappa$ is even in each coordinate (in 3(a) also symmetric under exchanging the coordinates). Hence $\alpha(h_p,h_{p'};\lambda)$ depends only on $p-p'$, and it is invariant under coordinate reflections (and, in 3(a), the exchange) of $p-p'$.
- The strict $d_0$-inequalities used below are finitely many. They persist for $D_{n,R}$ when $R\ge R_0(n)$. Hence long finite chains have the same small-$\lambda$ graphs, and their $\ell_0$ converge to the values found below.

### Step 2. Small-$\lambda$ neighbour graph and $\ell_0$

Take a description with finitely many places, all $d_0(h,h')>0$. By (5.10) or (22.3), for small $\lambda$ every place is its own point and all points are related (4.1). For distinct $x,x'$:
- **(N1)** If some $y$ has $\max\bigl(d_0(x,y),d_0(y,x')\bigr)<d_0(x,x')$, then $x\not\sim x'$ for all small $\lambda$.
- **(N2)** If every $y\notin\{x,x'\}$ has $\max\bigl(d_0(x,y),d_0(y,x')\bigr)>d_0(x,x')$, then $x\sim x'$ for all small $\lambda$. For $y\in\{x,x'\}$ the maximum equals $\alpha(x,x')$, which is never $<$.

Both follow from $\alpha/\lambda\to d_0$ and finiteness: there is a $\lambda_n>0$ below which all the strict inequalities used hold.

In every family below, each pair falls under (N1) or (N2). So (4.3) is decided directly, even where ties violate the hypotheses of (11.11). Call the resulting graph $N_0$.

For $\lambda<\lambda_n$, $\ell$ is the minimum over the finitely many simple $N_0$-chains of their $\alpha$-lengths, because cutting out a loop shortens a chain. Divided by $\lambda$, each $\alpha$-length tends to the corresponding $d_0$-length. Hence

$$
\ell_0(x,x')=\min\Bigl\{\textstyle\sum_jd_0(y_j,y_{j+1}):\ y_0=x,\ y_m=x',\ y_j\sim y_{j+1}\text{ in }N_0\Bigr\}.
\tag{22.4}
$$

A minimizing chain is called **$\ell_0$-shortest**. A chain that is not $\ell_0$-shortest has $\alpha$-length $>\ell$ for small $\lambda$. So for small $\lambda$ every $\ell$-geodesic is $\ell_0$-shortest.

### Step 3. Item 1(a)

(5.17) applied to $X/n$ and $Y/n$ (standard deviation $\sigma/n$, covariance 0) gives

$$
d_0\bigl(h_{(i,j)},h_{(i',j')}\bigr)=\tfrac{\sigma}{n}\sqrt{(\Delta i)^2+(\Delta j)^2}.
\tag{22.5}
$$

So $(X_n,d_0)$ is isometric to the grid $\{(\sigma i/n,\sigma j/n)\}$ in the Euclidean plane, consistent with (5.11). The grid lies within Hausdorff distance $\sigma/(\sqrt2n)$ of the square, so by (G1)

$$
(X_n,d_0)\xrightarrow{\rm GH}Y_a=\bigl([0,\sigma]^2,\lvert\cdot\rvert_2\bigr).
\tag{22.6}
$$

- $Y_a$ is a compact convex set, hence a length space and continuum-like.
- Its dimension is 2, and it is flat.
- Betweenness and geodesics (G3): $y$ is between $x$ and $z$ iff $y\in[x,z]$. In $X_n$, the between points are the grid points on the segment. The geodesic is unique: the straight segment.
- $Y_a$ is isotropic.

### Step 4. Item 1(b)

**(11.11) fails.** For index points $x=(0,0)$, $y=(1,2)$, $x'=(2,1)$: $\max(\sqrt5,\sqrt2)=\sqrt5$, which is a tie. So we decide by Step 2. Let $\Delta=x'-x$ in index units, and let $\hat e_1,\hat e_2$ be the unit lattice steps.

- **$\lVert\Delta\rVert_1=1$: (N2).** For $y\notin\{x,x'\}$, both $y-x$ and $x'-y$ are nonzero lattice vectors, so both distances are $\ge\sigma/n$. Both equal $\sigma/n$ only if both vectors are unit steps. But their sum $\Delta$ would then have $\lVert\cdot\rVert_1\in\{0,2\}$, a contradiction. So the maximum is strictly larger than $\sigma/n$.
- **$\lVert\Delta\rVert_2>1$: (N1).** Let $\hat e$ be a unit step toward $x'$ along an axis with $\hat e\cdot\Delta\ge1$, and set $y=x+\hat e$; it lies in the bounding box, hence in the grid. Then $d_0(x,y)=\sigma/n<d_0(x,x')$. Also $\lvert\Delta-\hat e\rvert_2^2=\lvert\Delta\rvert_2^2-2\hat e\cdot\Delta+1<\lvert\Delta\rvert_2^2$.

Hence, for $\lambda<\lambda_n$,

$$
N_0:\quad h_{(i,j)}\sim h_{(i',j')}\iff\lvert\Delta i\rvert+\lvert\Delta j\rvert=1\quad\text{(square grid graph)}.
\tag{22.7}
$$

All edges have $d_0=\sigma/n$, so (22.4) counts edges:

$$
\ell_0=\tfrac{\sigma}{n}\bigl(\lvert\Delta i\rvert+\lvert\Delta j\rvert\bigr),\qquad
(X_n,\ell_0)\xrightarrow{\rm GH}Y_b=\bigl([0,\sigma]^2,\lVert\cdot\rVert_1\bigr).
\tag{22.8}
$$

$Y_b$ is a compact length space. Its dimension is 2 (G4), since $\lvert v\rvert_2\le\lVert v\rVert_1\le\sqrt2\lvert v\rvert_2$. The limit is again the square, now with the taxicab norm:

$$
Y_b\ \text{continuum-like},\ \dim Y_b=2 .
\tag{22.9}
$$

**Comparison with (a).**
- **Betweenness.** Under $d_0$ the between points form the segment; under $\ell_0$ they form the axis-parallel box spanned by $x,z$ (G3).
- **Geodesics.** In $Y_b$ every curve with both coordinates monotone is a geodesic. It is unique only if $x,z$ lie on an axis-parallel line; in $Y_a$ the geodesic is always unique. In $X_n$ the $\ell_0$-shortest chains are the monotone lattice paths:

$$
\#\{\ell_0\text{-shortest chains}\}=\binom{\lvert\Delta i\rvert+\lvert\Delta j\rvert}{\lvert\Delta i\rvert}\quad(\text{one under }d_0\text{ in the limit}).
\tag{22.10}
$$

  - At fixed small $\lambda$, the $\ell$-geodesics are among these chains (Step 2).
  - If $[X,Y]=0$, then $e^{iK_{h'}\lambda}e^{-iK_h\lambda}=e^{iX\lambda/n}$ on every horizontal edge (and $e^{iY\lambda/n}$ on every vertical one). By (22.1) all edges of one direction then have the same $\alpha$, and all (22.10) chains are $\ell$-geodesics.
  - Otherwise, $O(\lambda^2)$ terms of $\alpha$ that $d_0$ does not fix may select a subset.
- **Isotropy.** $Y_a$ is isotropic. $Y_b$ is not, because the $\lVert\cdot\rVert_1$ ball is a square.
  - This holds intrinsically. If a unit ball has a boundary segment $[v,w]$ with $v\neq w$, then $x+tv$ and $x+tw$ are both midpoints of $x$ and $x+t(v+w)$.
  - In subsets of Euclidean spaces, midpoints are unique. So $Y_b$ is isometric to no Euclidean subset.
- **Largest ratio.** $\ell_0/d_0=(\lvert\Delta i\rvert+\lvert\Delta j\rvert)/\sqrt{(\Delta i)^2+(\Delta j)^2}$, with equality iff $\lvert\Delta i\rvert=\lvert\Delta j\rvert\ge1$:

$$
\max\ell_0/d_0=\sqrt2\approx1.414 .
\tag{22.11}
$$

### Step 5. Item 1(c)

**Branch states.** By Step 11 of 19, $E_h=\cos t\lvert0\rangle+e^{i\mu}\sin t\lvert1\rangle$ with $t=\lambda r$ and $\mu=\phi-\pi/2$. The Bloch vector is $(\sin2t\cos\mu,\sin2t\sin\mu,\cos2t)$. By (22.1) and (G5),

$$
\alpha(h,h';\lambda)=\text{great-circle distance on }\mathbb S\ (\text{radius }1/2)\text{ between }F_\lambda(x_h,y_h)\text{ and }F_\lambda(x_{h'},y_{h'}).
\tag{22.12}
$$

**The map $F_\lambda$.** $F_\lambda$ sends $(r,\phi)$ to the point at distance $\lambda r$ from $N=[\lvert0\rangle]$ along the meridian of azimuth $\phi-\pi/2$. This holds for $\lambda r\le\pi/2$; beyond that, the meridian runs on past the antipode $S_0=[\lvert1\rangle]$. So $X_n=F_\lambda(\text{lattice points})$ as a subset of $(\mathbb S,\alpha)$.

**Convergence.** By (19.16), $g\le\lambda^2(\mathrm dr^2+r^2\mathrm d\phi^2)$, since $\lvert\sin2\lambda r\rvert\le2\lambda r$. So $F_\lambda$ is $\lambda$-Lipschitz. The lattice points lie within $3r_0/n$ of every point of the closed disc $\bar D$. By (G1),

$$
(X_n,\alpha)\xrightarrow{\rm GH}Y_c=\bigl(F_\lambda(\bar D),\alpha\bigr)=
\begin{cases}\text{closed cap }\{\alpha(N,\cdot)\le\lambda r_0\}\subset\mathbb S, & \lambda r_0<\pi/2,\\ \text{all of }\mathbb S\cong\mathbb{CP}^1, & \lambda r_0\ge\pi/2.\end{cases}
\tag{22.13}
$$

In all cases $\dim Y_c=2$ (G4) and the Gaussian curvature is $4$, in agreement with $\kappa_g=4$ of (19.17). For the rescaled $\alpha/\lambda$ the sphere has radius $1/(2\lambda)$ and curvature $4\lambda^2=\hat\kappa$. Only $\lambda r_0$ matters:

- **(i) $\lambda r_0\le\pi/4$.**
  - The cap lies in a closed hemisphere and is convex, so it is a compact geodesic space: continuum-like.
  - Geodesics are minimizing great-circle arcs, and $y$ is between $x,z$ iff it lies on such an arc.
  - Geodesics are unique except for antipodal pairs. Those occur only on the boundary for $\lambda r_0=\pi/4$, and then there is a one-parameter family of geodesics.
  - Radial segments of the disc map to meridians, which are geodesics; other segments do not.
- **(ii) $\pi/4<\lambda r_0<\pi/2$.**
  - Take boundary points with azimuths differing by $\pi$. They are at distance $\pi-2\lambda r_0$, and their unique minimizing arc passes through $S_0$.
  - $S_0$ is at distance $\pi/2>\lambda r_0$ from $N$, so $S_0\notin Y_c$.
  - A midpoint in $Y_c$ would be the sphere midpoint $S_0$, so these points have none. By (G2), $Y_c$ is not a length space and not continuum-like.
  - Geodesics exist only for pairs whose minimizing arc stays in the cap.
- **(iii) $\lambda r_0\ge\pi/2$.**
  - Places with $\lambda r=\pi/2$ merge into the point $S_0$, and further places merge beyond that.
  - $Y_c=\mathbb S$ is a compact geodesic space: continuum-like.
  - Geodesics are great-circle arcs, unique except between antipodal (orthogonal) points, which are joined by a circle of geodesics.

### Step 6. Item 2(a): $\alpha$ and $N_V$

Here $k_{h_i,l}=[l\in w_i]$, so $\Delta_l\in\{0,\pm1\}$, nonzero exactly on $w_i\triangle w_j$, and $\lvert w_i\triangle w_j\rvert=2\min(\lvert i-j\rvert,m)$ by (15.17). By (22.2), for $\lambda\in(0,\pi/2)$,

$$
\alpha(h_i,h_j)=\alpha_k:=\arccos\bigl((\cos\lambda)^{2k}\bigr),\qquad k=\min(\lvert i-j\rvert,m),\qquad 0<\alpha_1<\dots<\alpha_m<\tfrac\pi2 .
\tag{22.14}
$$

So all places are distinct points and all points are related. Since $\alpha$ is strictly increasing in $k$, (4.3) holds exactly when no $y$ has $\max(k(i,y),k(y,j))<k(i,j)$. Let $r=\lvert i-j\rvert$ with $i<j$:
- **$r=1$.** A witness would need $k(i,y)=k(y,j)=0$, which is impossible. Edge.
- **$2\le r\le m$.** $y=i+1$ is a witness, with $k(i,y)=1$ and $k(y,j)=r-1$. No edge.
- **$m<r\le2m-2$.** $y=i+m-1$ gives $k(i,y)=m-1$ and $k(y,j)=\min(r-m+1,m)\le m-1<m$. No edge.
- **$r\ge2m-1$.** A witness needs $\lvert i-y\rvert,\lvert y-j\rvert\le m-1$, hence $r\le2m-2$. There is none, so the tie at $k=m$ keeps the edge.

Hence, for every $\lambda\in(0,\pi/2)$,

$$
h_i\sim h_j\iff\lvert i-j\rvert=1\ \ \text{or}\ \ \lvert i-j\rvert\ge2m-1 .
\tag{22.15}
$$

### Step 7. Item 2(a): $\ell$, diameter, continuum

The graph has "steps" (edges with $r=1$, length $\alpha_1$) and "jumps" (edges with $r\ge2m-1$, length $\alpha_m$). A chain with $J$ jumps and $S$ steps has length $J\alpha_m+S\alpha_1$. Let $1\le r\le2m-2$.

**Lower bounds.**
- $J=0$: $S\ge r$.
- $J=1$: if the jump goes from $p$ to $p'$, then $S\ge\lvert i-p\rvert+\lvert p'-j\rvert\ge\lvert p-p'\rvert-r\ge2m-1-r$.
- $J\ge2$: the length is at least $2\alpha_m$.

**Attainment.**
- The bound for $J=1$ is attained by the jump $(i-s)\to(j+t)$ with $s+t=2m-1-r$. This chain exists iff $n\ge2m$.
- $2\alpha_m$ is attained by $i\to y\to j$ if some $y$ has $\lvert y-i\rvert,\lvert y-j\rvert\ge2m-1$.
  - Such a $y$ is missing only if $i\le2m-1$ and $j\ge n-2m+2$.
  - That forces $n\le6m-5$.

Therefore

$$
\ell(h_i,h_j)=\begin{cases}
r\,\alpha_1, & n\le2m-1,\\
\min\{r\alpha_1,\ \alpha_m+(2m-1-r)\alpha_1,\ 2\alpha_m\}, & n\ge6m-4,\ 1\le r\le2m-2,\\
\alpha_m, & r\ge2m-1 .
\end{cases}
\tag{22.16}
$$

For $2m\le n\le6m-5$ and $r\le2m-2$, $\ell=\min\{r\alpha_1,\alpha_m+(2m-1-r)\alpha_1,\ell_{\ge2}\}$. Here $\ell_{\ge2}\ge2\alpha_m$ is the shortest chain with at least two jumps in the explicit graph (22.15); it equals $2\alpha_m$ whenever such a $y$ exists.

**Diameter.**
- For distinct points, $\ell\ge\alpha\ge\alpha_1$.
- If $r\le2m-2$, then $\ell\le r\alpha_1$. If $r\ge2m-1$, then $\ell=\alpha_m\le m\alpha_1$ by the triangle inequality of $\alpha$.
- Hence, for all $n$,

$$
\operatorname{diam}(X_n,\ell)\le(2m-2)\alpha_1;\qquad
\operatorname{diam}=\max\Bigl\{\alpha_m,\max_{1\le r\le2m-2}\min\{r\alpha_1,\alpha_m+(2m-1-r)\alpha_1,2\alpha_m\}\Bigr\}\in[\alpha_m,2\alpha_m]\ \ (n\ge6m-4).
\tag{22.17}
$$

Example $m=2$. Since $2\alpha_1<\alpha_1+\alpha_2<2\alpha_2$, we get $\ell=\alpha_1,2\alpha_1,\alpha_2$ for $r=1,2,\ge3$. Also $\cos2\alpha_1=2\cos^4\lambda-1<\cos^4\lambda$, so $2\alpha_1>\alpha_2$. Hence $\operatorname{diam}=2\alpha_1$ for every $n\ge3$.

**Not continuum-like.** Suppose $(X_n,\ell/s_n)\to Y$, a compact length space with $D_Y:=\operatorname{diam}Y>0$.
1. By (G1) and (22.17), $s_n\le2(2m-2)\alpha_1/D_Y$ for large $n$.
2. So distinct points are at distance $\ge\alpha_1/s_n\ge\delta:=D_Y/(4m-4)$.
3. Take correspondences of distortion $\epsilon_n\to0$. If $d_Y(y,y')<\delta-\epsilon_n$, the partners of $y,y'$ are closer than $\delta$, hence equal, so $d_Y(y,y')\le\epsilon_n$.
4. Therefore $Y$ is $\delta$-separated, and being compact, it is finite.
5. Repeated midpoints (G2) would give distinct points closer than $\delta$, a contradiction.

The same argument holds for $\ell_0$: by (22.15) $N_0$ is the same graph, and $\ell_0$ is (22.16) with $\alpha_k\to\sqrt{2k}$, following (15.17). Hence

$$
\text{for every }\lambda\in(0,\tfrac\pi2)\text{ and every choice of }s_n:\ (X_n,\ell/s_n)\text{ and }(X_n,\ell_0/s_n)\text{ are not continuum-like.}
\tag{22.18}
$$

### Step 8. Item 2(b)

Here $k_{h_i,l}=q^{\lvert l-i\rvert}$, with the limit of Step 1. Then $\langle u_i\vert u_j\rangle=\sum_{l\in\mathbb Z}q^{\lvert l-i\rvert+\lvert l-j\rvert}$, with $r:=\lvert i-j\rvert$. The $r+1$ cells between $i$ and $j$ contribute $q^r$ each, and a cell beyond the ends at distance $s\ge1$ contributes $q^{r+2s}$. So $\langle u_i\vert u_j\rangle=G(r):=q^r(r+\beta)$ with $\beta:=\frac{1+q^2}{1-q^2}$, and

$$
d_0(h_i,h_j)=\sqrt{2\bigl[\beta(1-q^r)-r\,q^r\bigr]},\qquad
d_0^2(r)-d_0^2(r-1)=2(1-q)q^{r-1}\Bigl(r-\tfrac{q}{1+q}\Bigr)>0,\qquad d_0(1)=\rho_1:=\sqrt{\tfrac{2(1-q)}{1+q}} .
\tag{22.19}
$$

$d_0$ is strictly increasing in $r$ and saturates at $\sqrt{2\beta}$.

**Neighbour graph.** On a line, $\max(\lvert x-y\rvert,\lvert y-x'\rvert)=\lvert x-x'\rvert$ is impossible for distinct points. So there are no ties, and (11.11) applies; Step 2 gives the same graph:
- for $r\ge2$, $y=i+1$ is a witness (N1);
- for $r=1$, every other $y$ is at index distance $\ge2$ from one of the two (N2).

$$
N_0:\ h_i\sim h_j\iff\lvert i-j\rvert=1 .
\tag{22.20}
$$

$$
\ell_0(h_i,h_j)=\rho_1\lvert i-j\rvert .
\tag{22.21}
$$

By the translation invariance of Step 1, all edges have the same $\alpha_e(\lambda)$, so $\ell=\lvert i-j\rvert\alpha_e(\lambda)$ exactly for $\lambda<\lambda_n$. The points $\rho_1i/n$ fill $[0,\rho_1]$, so

$$
(X_n,\ell_0/n)\xrightarrow{\rm GH}\bigl([0,\rho_1],\lvert\cdot\rvert\bigr),
\tag{22.22}
$$

a continuum-like limit of dimension 1. Betweenness is the order. The geodesic is unique (the segment), and there is a unique shortest chain.

**Margins.** For $r\ge2$, the missing edge rests on a witness $y$ between $i$ and $j$. Its margin is $d_0(r)-d_0(r')$ with $r'=\max(\lvert i-y\rvert,\lvert y-j\rvert)\in[\lceil r/2\rceil,r-1]$. The largest margin (midpoint witness) and the smallest margin (neighbouring witness) are, by (22.19), with $s=\lceil r/2\rceil$:

$$
\delta(r)=\frac{2\bigl[q^s(s+\beta)-q^r(r+\beta)\bigr]}{d_0(r)+d_0(s)}\sim\frac{(s+\beta)\,q^{s}}{\sqrt{2\beta}},\qquad
\Delta(r)=\frac{2(1-q)q^{r-1}\bigl(r-\frac q{1+q}\bigr)}{d_0(r)+d_0(r-1)}\sim\frac{(1-q)\,r\,q^{r-1}}{\sqrt{2\beta}}\quad(r\to\infty).
\tag{22.23}
$$

The edges ($r=1$) rest on the margin $d_0(2)-d_0(1)=O(1)$.

The decisions for $r\ge2$ rest on margins that are exponentially small in $r$. By (22.3), the derivation through $d_0$ certifies (22.20) only while the relative $O(\lambda^2)$ corrections stay below $\delta(r)/d_0(r)$ for all $r\le n-1$. The certified threshold $\lambda_n$ therefore decays exponentially in $n$.

### Step 9. Item 3(a)

Here $k_{h_p,l}=q^{\lvert l_1-p_1\rvert}q^{\lvert l_2-p_2\rvert}$, so $u_p$ factorizes. With $r_k=\lvert p_k-p'_k\rvert$ and $G$ from Step 8, $\langle u_p\vert u_{p'}\rangle=G(r_1)G(r_2)$. Hence

$$
d_0(h_p,h_{p'})=\Phi(r_1,r_2):=\sqrt{2\bigl[\beta^2-q^{r_1+r_2}(r_1+\beta)(r_2+\beta)\bigr]}.
\tag{22.24}
$$

$G>0$, and $G$ is strictly decreasing, because $G(r)-G(r+1)=\tfrac12[d_0^2(r+1)-d_0^2(r)]>0$ by (22.19). So $\Phi$ is symmetric and strictly increasing in each argument.

**(11.11) fails.** For $p=(1,1)$, $y=(2,3)$, $p'=(3,2)$: $\max(\Phi(1,2),\Phi(1,1))=\Phi(2,1)$, a tie.

**Step 2 decides every pair.**
- $\lVert\Delta\rVert_1=1$ falls under (N2), by the argument of Step 4 with $\Phi$ in place of the Euclidean distance.
- $\lVert\Delta\rVert_1\ge2$ falls under (N1), with $y=x+\hat e$ as in Step 4. Then $\Phi(1,0)<\Phi(\lvert\Delta_1\rvert,\lvert\Delta_2\rvert)$, and lowering one argument of $\Phi$ by 1 lowers it strictly.

$$
N_0=\text{square grid graph on }\{1,\dots,n\}^2 .
\tag{22.25}
$$

All edges have the same length $\rho:=\Phi(1,0)=\sqrt{2\beta(\beta-G(1))}=\frac{\sqrt{2(1+q^2)}}{1+q}$, so

$$
\ell_0(h_p,h_{p'})=\rho\bigl(\lvert\Delta_1\rvert+\lvert\Delta_2\rvert\bigr),
\tag{22.26}
$$

$$
(X_n,\ell_0/n)\xrightarrow{\rm GH}\bigl([0,1]^2,\ \rho\lVert\cdot\rVert_1\bigr).
\tag{22.27}
$$

- **Dimension:** 2.
- **Betweenness:** the axis-parallel box spanned by $x,z$.
- **Geodesics:** all curves with both coordinates monotone. They are unique iff $x,z$ lie on an axis-parallel line.
- **Shortest chains.** By Step 1, every grid edge has the same $\alpha_e(\lambda)$ (translation, reflection and exchange symmetry). So for $\lambda<\lambda_n$, $\ell=\lVert\Delta\rVert_1\alpha_e(\lambda)$ exactly, and

$$
\#\{\ell\text{-geodesics}\}=\#\{\ell_0\text{-shortest chains}\}=\binom{\lvert\Delta_1\rvert+\lvert\Delta_2\rvert}{\lvert\Delta_1\rvert}.
\tag{22.28}
$$

- **Isotropy: no.** The unit ball $\{\lVert v\rVert_1\le1/\rho\}$ is a square, and by the intrinsic argument of Step 4 no rescaling or re-embedding makes the limit Euclidean.

### Step 10. Item 3(b)

**Standard results (G6).**
- **(P1)** *Burago's theorem on periodic metrics, graph version.* Let $\Gamma\cong\mathbb Z^2$ act freely on a connected graph with finitely many vertex and edge orbits, with $\Gamma$-invariant positive edge lengths. Let $\pi$ be a $\Gamma$-equivariant map of the vertices into $\mathbb R^2$, where $\Gamma$ acts by a lattice of translations.
  - Then there is a norm $\lVert\cdot\rVert_{\rm st}$ (the stable norm) and a constant $C$ with $\lvert d(x,y)-\lVert\pi x-\pi y\rVert_{\rm st}\rvert\le C$.
  - Hence, for a compact convex body $B$ and $X_n=\pi^{-1}(nB)$, $(X_n,d/n)\to(B,\lVert\cdot\rVert_{\rm st})$ in GH.
- **(P2)** *Kotani–Sunada.* The unit ball of $\lVert\cdot\rVert_{\rm st}$ is the convex polygon $\operatorname{conv}\{\gamma(c)/w(c)\}$.
  - Here $c$ runs over the finitely many simple cycles of the finite quotient graph that have a nonzero translation $\gamma(c)$, and $w(c)$ is the length of $c$.
  - Reason: a shortest path projects to a closed walk, which decomposes into simple cycles. So $\lVert v\rVert_{\rm st}$ is the value of a finite linear program, a piecewise linear function of $v$.

**Application.**
- By hypothesis, $N_0$ is $\Gamma$-periodic with finitely many edge orbits, and the edge weights $d_0(e)>0$ are $\Gamma$-invariant.
- By (22.3), $\alpha(e)/\lambda\to d_0(e)$ uniformly over the finitely many edge orbits. So $\ell_0$ is the $d_0$-weighted graph distance (22.4).
- If $N_0$ is disconnected, $\ell_0=\infty$ between components, and there is no limit.
- Otherwise (P1)–(P2) give a limit $(B,\lVert\cdot\rVert_{\rm st})$ whose unit ball is a polygon. A polygon is never an ellipse, and by Step 4 the limit is not even intrinsically Euclidean.
- Check against 3(a): the quotient graph has one vertex and loops with $\gamma=\pm\hat e_1,\pm\hat e_2$ and $w=\rho$. Then $\operatorname{conv}\{\pm\hat e_k/\rho\}$ is the unit ball of $\rho\lVert\cdot\rVert_1$, as in (22.27).

$$
\text{Periodic arrangements: the rescaled }\ell_0\text{ never converges to an isotropic limit (polygonal stable norm).}
\tag{22.29}
$$

## Result

- **1(a)** $d_0=\frac\sigma n\sqrt{\Delta i^2+\Delta j^2}$ (22.5).
  - Limit: the Euclidean square $[0,\sigma]^2$ (22.6), of dimension 2 and flat.
  - Betweenness is the segment; geodesics are unique straight segments; the limit is isotropic.
- **1(b)** For small $\lambda$, $N_0$ is the square grid graph (22.7), decided directly from (4.3) despite ties.
  - $\ell_0=\frac\sigma n(\lvert\Delta i\rvert+\lvert\Delta j\rvert)$, with limit $([0,\sigma]^2,\lVert\cdot\rVert_1)$ (22.8)–(22.9).
  - Betweenness is the box. There are $\binom{\lvert\Delta i\rvert+\lvert\Delta j\rvert}{\lvert\Delta i\rvert}$ shortest chains (22.10), all $\ell$-geodesics if $[X,Y]=0$.
  - The limit is not isotropic. $\max\ell_0/d_0=\sqrt2$ (22.11).
- **1(c)** $\alpha$ is the great-circle distance on the sphere of radius $1/2$ (22.12).
  - Limit (22.13): the cap of radius $\lambda r_0$ (for $\lambda r_0<\pi/2$) or the whole $\mathbb{CP}^1$ (for $\lambda r_0\ge\pi/2$).
  - Dimension 2, curvature 4.
  - Length space iff $\lambda r_0\le\pi/4$ or $\lambda r_0\ge\pi/2$. Geodesics are great-circle arcs.
- **2(a)** $\alpha=\arccos(\cos^{2\min(r,m)}\lambda)$ (22.14).
  - $N_V$ has the edges $r=1$ and $r\ge2m-1$, for every $\lambda\in(0,\pi/2)$ (22.15).
  - $\ell$ is given by (22.16). The diameter is at most $(2m-2)\alpha_1$, independent of $n$ (22.17).
  - **Not continuum-like** for any $s_n$, for $\ell$ and for $\ell_0$ (22.18).
- **2(b)** $d_0$ is given by (22.19). $N_0$ is the path (22.20) and $\ell_0=\rho_1\lvert i-j\rvert$ (22.21).
  - Limit: the segment $[0,\rho_1]$, of dimension 1 (22.22).
  - Decisive margins are $\sim(\lceil r/2\rceil+\beta)q^{\lceil r/2\rceil}/\sqrt{2\beta}$ (22.23).
- **3(a)** $d_0=\Phi(r_1,r_2)$ (22.24). $N_0$ is the grid (22.25) and $\ell_0=\rho\lVert\Delta\rVert_1$ (22.26).
  - Limit: $([0,1]^2,\rho\lVert\cdot\rVert_1)$ (22.27), of dimension 2. Betweenness is the box; geodesics are non-unique.
  - There are $\binom{\lvert\Delta_1\rvert+\lvert\Delta_2\rvert}{\lvert\Delta_1\rvert}$ shortest chains (22.28). The limit is **not isotropic**.
- **3(b)** **No**: the limit norm of a periodic arrangement is polygonal (22.29).
- **Goal.**
  - Compact local records give no large-scale continuum through $\ell$, because saturation ties create long edges.
  - Exponential tails do give one through $\ell_0$ with $s_n=n$, of dimension 1 and 2.
  - The large-scale geometry is the $\ell^1$ norm, not isotropic, and periodicity cannot make it isotropic.

## Consistency checks

1. **Dimensions.** $\alpha$ and $\ell$ are angles. $\lambda d_0$ and $\lambda\ell_0$ are dimensionless, because $K_h$ carries the inverse unit of $\lambda$: $d_0,\ell_0\propto\sigma$ in 1(a)–(b). In 1(c), only $\lambda r_0$ enters the case distinction.
2. **Small $\lambda$.**
   - (22.14) gives $\alpha_k=\arccos(1-k\lambda^2+O(\lambda^4))$, so $\alpha_k/\lambda\to\sqrt{2k}$, which is (15.17).
   - In 1(c), $u_h=(x_h+iy_h)\lvert1\rangle$, so $d_0$ is Euclidean. This is (22.5) with $\sigma_X=\sigma_Y=1$ and $\operatorname{Cov}=\operatorname{Re}\langle0\vert\sigma_x\sigma_y\vert0\rangle=0$.
   - It matches the $\lambda r_0\to0$ limit of (22.13) rescaled by $1/\lambda$: a cap of radius $r_0$ on a sphere of radius $1/(2\lambda)$ tends to the flat disc.
3. **$q\to0$ in 2(b) against $m=1$.**
   - (22.19) tends to $\sqrt2$ for all $r\ge1$, which is (15.17) with $m=1$. There (22.15) gives the complete graph, through ties.
   - The path (22.20) does not tend to it. This is consistent with the margins (22.23) vanishing as $q\to0$: the neighbour relation is not continuous where its margins vanish.

## Open issues

- 2(a), $2m\le n\le6m-5$: (22.16) leaves $\ell_{\ge2}$ unevaluated for the pairs near both ends. It is a finite computation in the explicit graph (22.15) and is bounded by (22.17). It does not affect the family result (22.18).
- 1(b), non-commuting $X,Y$: which of the (22.10) chains are $\ell$-geodesics at fixed small $\lambda$ depends on $O(\lambda^2)$ terms of $\alpha$, not on $d_0$.
- 2(b), 3(a): the small-$\lambda$ thresholds $\lambda_n$ shrink with $n$ (22.23). The fixed-$\lambda$ neighbour graphs for large $n$ are not determined here.
- 3(b) relies on (P1)–(P2) as standard results.

## Methods used

- Partial trace of a block-diagonal evolution; product states of qubit cells
- Small-parameter expansion; strict-inequality persistence (relative neighbourhood graph)
- Weighted graph distances, shortest paths, lattice-path counting
- Gromov–Hausdorff convergence via Hausdorff convergence; separation argument
- Normed planes (Euclidean, $\ell^1$), betweenness, midpoint uniqueness
- Bloch sphere / Fubini–Study geometry of $\mathbb{CP}^1$, spherical caps and convexity
- Stable norms of periodic graphs (Burago, Kotani–Sunada)
