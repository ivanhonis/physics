# Large-scale geometry of the derived space: continuum limits, dimension, betweenness and geodesics

- **Subproject:** 03-ilang-space
- **Package:** 22-large-scale-geometry
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-09

## Changes from previous version

- **Step 8 (I2).** The paragraph after (22.23) now calls the exponentially shrinking quantity a sufficient bound, obtained from the uniform remainder estimate (22.3). It states that the actual stability threshold of the neighbour graph is not determined, including whether it has an $`n`$-independent lower bound. Step 9 makes no such assertion and is unchanged.
- **Step 10 (I1).**
  - (22.29) is kept as the theorem for a fixed pattern, (F1)–(F3). The sentence that introduces (F1)–(F3) and the "Scope" bullets now point to the new parts (i)–(iii).
  - New standard results (P3): John's theorem and Blaschke selection.
  - (i) Patterns that change with $`n`$ and have at most $`E_0`$ edge orbits. Under a uniformity assumption (F4) there is no two-dimensional isotropic limit (22.32). A sufficient condition for (F4) is given, and an example shows that bounded orbit counts alone do not imply (F4).
  - (ii) Patterns with unboundedly many orbits. An explicit family of recording descriptions, built on the region graphs of line arrangements, has rescaled $`\ell_0`$ converging to a Euclidean convex body, (22.33)–(22.36).
  - (iii) What remains open, and the class of arrangements on which it depends.
- **Result and Open issues** are updated accordingly.
- All other text is unchanged. Every tag keeps its meaning; the new tags are (22.32)–(22.36).

## Response to verification

- **I1:** Accepted and fixed in Step 10.
  - (22.29) remains the theorem for a fixed pattern.
  - Part (i) treats $`n`$-dependent patterns with boundedly many orbits. Under (F4), every two-dimensional limit has a polygonal norm with at most $`2^{E_0+1}`$ vertices (22.32).
  - Part (ii) settles the literal class affirmatively, with an explicit family of valid recording descriptions, (22.33)–(22.36). The polygonal unit balls approach an ellipse there, and the limit is Euclidean.
  - The boundary recomputation is handled exactly in (ii): the recomputed graph is the induced subgraph, and $`\ell_0=d_G`$.
  - Part (iii) names what remains open: boundedly many orbits without (F4), and truncations that create new edges.
- **I2:** Accepted and fixed in Step 8 (the paragraph after (22.23)) and in Open issues. The shrinking quantity is now described as a sufficient bound. The actual thresholds, including whether they have an $`n`$-independent lower bound, are stated as not determined. Step 9 contains no corresponding assertion.

## Setup and assumptions

- **Setting (question.md).**
  - Probe $`b`$ with places $`h`$, the only instance of its type, and medium $`c`$.
  - Recording contract $`C=\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with all $`\phi_h\neq0`$, and $`\lambda\ge0`$.
  - All distances are those of the view of $`\{b\}`$. In items 2–3 the medium is one object made of qubit cells, with $`\chi=\lvert0\cdots0\rangle`$.
- **Inputs, as quoted:** $`\alpha`$ (3.5); (4.1); neighbours (4.3) and $`N_V`$; $`\ell`$ (4.6)–(4.7); $`d_0,u_h`$ (5.10)–(5.11); (5.17)–(5.18); the hypotheses of (11.11); (15.17); (15.18) with Step 9 of 15; the qubit-plane branch state of 19; (19.16)–(19.17).
- **Definitions** ($`\ell_0`$, family, continuum-like, dimension, betweenness, geodesic, isotropy): as in question.md. Infinite media are limits of finite ones, fixed in Step 1.
- **Standard facts used (M5):**
  - (G1) If finite sets $`A_n`$ in a metric space $`Z`$ converge in Hausdorff distance to a compact $`Y\subseteq Z`$, then $`(A_n,d_Z)\to(Y,d_Z)`$ in the Gromov–Hausdorff (GH) sense. The diameter is GH-continuous.
  - (G2) A compact length space is geodesic, so any two of its points have a midpoint.
  - (G3) Euclidean plane: $`y`$ is between $`x`$ and $`z`$ iff $`y\in[x,z]`$, and the segment is the unique geodesic. For $`\lVert v\rVert_1=\lvert v_1\rvert+\lvert v_2\rvert`$: $`y`$ is between iff each $`y_k`$ lies between $`x_k`$ and $`z_k`$ (the box), and the geodesics are the curves with both coordinates monotone. Convex sets of normed planes are length spaces.
  - (G4) A bi-Lipschitz image of a planar set with interior has Hausdorff dimension 2; that of a segment has dimension 1.
  - (G5) Bloch sphere: for unit $`\psi,\psi'\in\mathbb C^2`$ with Bloch vectors $`\mathbf n,\mathbf n'`$, $`\lvert\langle\psi'\vert\psi\rangle\rvert=\cos(\Theta/2)`$ with $`\Theta=\angle(\mathbf n,\mathbf n')`$. Hence $`\arccos\lvert\langle\cdot\vert\cdot\rangle\rvert`$ is the great-circle distance of the round sphere $`\mathbb S`$ of radius $`1/2`$, which has Gaussian curvature 4.
  - (G6) Periodic metrics: stated in Step 10.

## Derivation

### Step 1. Witness angle in the recording setting

$`C`$ is block-diagonal in the places of $`b`$. Hence $`\lvert\Psi(\lambda)\rangle=\sum_h\phi_h\lvert h\rangle\otimes\lvert E_h\rangle`$ with $`\lvert E_h\rangle=e^{-iK_h\lambda}\lvert\chi\rangle`$. By (1.7), $`\langle h\vert V\vert h'\rangle=\phi_h\phi_{h'}^*\langle E_{h'}\vert E_h\rangle`$ and $`p_h=\lvert\phi_h\rvert^2`$, so (3.5) gives

```math
\cos\alpha(h,h';\lambda)=\bigl\lvert\langle E_{h'}(\lambda)\vert E_h(\lambda)\rangle\bigr\rvert .
\qquad\text{(22.1)}
```

Places are the same point iff their branch states agree up to a phase.

**Qubit cells.** Let $`K_h=\sum_lk_{h,l}\sigma_x^{[l]}`$ with $`k_{h,l}`$ real. As in Step 9 of 15, $`\lvert E_h\rangle=\bigotimes_l\bigl(\cos(k_{h,l}\lambda)\lvert0\rangle-i\sin(k_{h,l}\lambda)\lvert1\rangle\bigr)`$, and one cell contributes the overlap $`\cos(k_{h',l}\lambda)\cos(k_{h,l}\lambda)+\sin(k_{h',l}\lambda)\sin(k_{h,l}\lambda)`$. This is (15.18) for one probe, with $`\nu_l\to k_{h,l}`$. Moreover $`\langle\chi\vert\sigma_x^{[l]}\vert\chi\rangle=0`$ and $`\sigma_x^{[l]}\lvert\chi\rangle=\lvert e_l\rangle`$ (orthonormal), so (5.10) gives

```math
\cos\alpha(h,h';\lambda)=\prod_l\bigl\lvert\cos(\lambda\Delta_l)\bigr\rvert,\qquad \Delta_l:=k_{h,l}-k_{h',l},\qquad
\lvert u_h\rangle=\sum_lk_{h,l}\lvert e_l\rangle,\qquad d_0(h,h')^2=\sum_l\Delta_l^2 .
\qquad\text{(22.2)}
```

**Infinite media.** In 2(b) and 3(a), $`0<k_{h,l}\le1`$ and $`\sum_l\Delta_l^2<\infty`$.
- The finite description $`D_{n,R}`$ keeps the places and has the cells $`\Lambda_R=\{1-R,\dots,n+R\}`$ (in 3(a), $`\Lambda_R^2`$). Each $`K_h`$ is truncated to these cells.
- For $`0<\lambda<\pi/2`$ every factor in (22.2) lies in $`(0,1]`$, so the product converges as $`R\to\infty`$, at fixed $`n`$ and $`\lambda`$.
- **The limit description** is defined by $`\alpha:=\lim_R\alpha^{(R)}`$ and $`d_0:=\lim_Rd_0^{(R)}`$, that is, by (22.2) with $`l`$ running over $`\mathbb Z`$ (resp. $`\mathbb Z^2`$). $`N_V`$, $`\ell`$ and $`\ell_0`$ are computed from this $`\alpha`$.
- Since $`-\ln\cos x=\tfrac{x^2}2(1+O(x^2))`$ uniformly for $`\lvert x\rvert\le1`$, and $`\sum_l\Delta_l^4\le\sum_l\Delta_l^2`$,

```math
\alpha(h,h';\lambda)=\lambda\,d_0(h,h')\bigl(1+O(\lambda^2)\bigr)\quad\text{uniformly in the pair}.
\qquad\text{(22.3)}
```

- Translation invariance. The product runs over all cells, and $`\kappa`$ is even in each coordinate (in 3(a) also symmetric under exchanging the coordinates). Hence $`\alpha(h_p,h_{p'};\lambda)`$ depends only on $`p-p'`$, and it is invariant under coordinate reflections (and, in 3(a), the exchange) of $`p-p'`$.
- The strict $`d_0`$-inequalities used below are finitely many. They persist for $`D_{n,R}`$ when $`R\ge R_0(n)`$. Hence long finite chains have the same small-$`\lambda`$ graphs, and their $`\ell_0`$ converge to the values found below.

### Step 2. Small-$`\lambda`$ neighbour graph and $`\ell_0`$

Take a description with finitely many places, all $`d_0(h,h')>0`$. By (5.10) or (22.3), for small $`\lambda`$ every place is its own point and all points are related (4.1). For distinct $`x,x'`$:
- **(N1)** If some $`y`$ has $`\max\bigl(d_0(x,y),d_0(y,x')\bigr)<d_0(x,x')`$, then $`x\not\sim x'`$ for all small $`\lambda`$.
- **(N2)** If every $`y\notin\{x,x'\}`$ has $`\max\bigl(d_0(x,y),d_0(y,x')\bigr)>d_0(x,x')`$, then $`x\sim x'`$ for all small $`\lambda`$. For $`y\in\{x,x'\}`$ the maximum equals $`\alpha(x,x')`$, which is never $`<`$.

Both follow from $`\alpha/\lambda\to d_0`$ and finiteness: there is a $`\lambda_n>0`$ below which all the strict inequalities used hold.

In the families 1(b), 2(b) and 3(a), each pair falls under (N1) or (N2) (Steps 4, 8, 9). So (4.3) is decided directly there, even where ties violate the hypotheses of (11.11). Call the resulting graph $`N_0`$.

The compact windows 2(a) are an exception. For $`m=2`$ and $`n=4`$, the pair $`h_1,h_4`$ has $`d_0=2`$ by (15.17). Both candidates $`y=h_2,h_3`$ give $`\max=2`$, a tie, so neither (N1) nor (N2) applies. There (4.3) is decided from the exact $`\alpha`$ (22.14), for every $`\lambda\in(0,\pi/2)`$ (Step 6). The resulting $`N_V`$ (22.15) does not depend on $`\lambda`$, and $`N_0:=N_V`$.

For $`\lambda<\lambda_n`$, $`\ell`$ is the minimum over the finitely many simple $`N_0`$-chains of their $`\alpha`$-lengths, because cutting out a loop shortens a chain. Divided by $`\lambda`$, each $`\alpha`$-length tends to the corresponding $`d_0`$-length. Hence

```math
\ell_0(x,x')=\min\Bigl\{\textstyle\sum_jd_0(y_j,y_{j+1}):\ y_0=x,\ y_m=x',\ y_j\sim y_{j+1}\text{ in }N_0\Bigr\}.
\qquad\text{(22.4)}
```

A minimizing chain is called **$`\ell_0`$-shortest**. A chain that is not $`\ell_0`$-shortest has $`\alpha`$-length $`>\ell`$ for small $`\lambda`$. So for small $`\lambda`$ every $`\ell`$-geodesic is $`\ell_0`$-shortest.

### Step 3. Item 1(a)

(5.17) applied to $`X/n`$ and $`Y/n`$ (standard deviation $`\sigma/n`$, covariance 0) gives

```math
d_0\bigl(h_{(i,j)},h_{(i',j')}\bigr)=\tfrac{\sigma}{n}\sqrt{(\Delta i)^2+(\Delta j)^2}.
\qquad\text{(22.5)}
```

So $`(X_n,d_0)`$ is isometric to the grid $`\{(\sigma i/n,\sigma j/n)\}`$ in the Euclidean plane, consistent with (5.11). The grid lies within Hausdorff distance $`\sigma/(\sqrt2n)`$ of the square, so by (G1)

```math
(X_n,d_0)\xrightarrow{\rm GH}Y_a=\bigl([0,\sigma]^2,\lvert\cdot\rvert_2\bigr).
\qquad\text{(22.6)}
```

- $`Y_a`$ is a compact convex set, hence a length space and continuum-like.
- Its dimension is 2, and it is flat.
- Betweenness and geodesics (G3): $`y`$ is between $`x`$ and $`z`$ iff $`y\in[x,z]`$. In $`X_n`$, the between points are the grid points on the segment. The geodesic is unique: the straight segment.
- $`Y_a`$ is isotropic.

### Step 4. Item 1(b)

**(11.11) fails.** For index points $`x=(0,0)`$, $`y=(1,2)`$, $`x'=(2,1)`$: $`\max(\sqrt5,\sqrt2)=\sqrt5`$, which is a tie. So we decide by Step 2. Let $`\Delta=x'-x`$ in index units, and let $`\hat e_1,\hat e_2`$ be the unit lattice steps.

- **$`\lVert\Delta\rVert_1=1`$: (N2).** For $`y\notin\{x,x'\}`$, both $`y-x`$ and $`x'-y`$ are nonzero lattice vectors, so both distances are $`\ge\sigma/n`$. Both equal $`\sigma/n`$ only if both vectors are unit steps. But their sum $`\Delta`$ would then have $`\lVert\cdot\rVert_1\in\{0,2\}`$, a contradiction. So the maximum is strictly larger than $`\sigma/n`$.
- **$`\lVert\Delta\rVert_2>1`$: (N1).** Let $`\hat e`$ be a unit step toward $`x'`$ along an axis with $`\hat e\cdot\Delta\ge1`$, and set $`y=x+\hat e`$; it lies in the bounding box, hence in the grid. Then $`d_0(x,y)=\sigma/n<d_0(x,x')`$. Also $`\lvert\Delta-\hat e\rvert_2^2=\lvert\Delta\rvert_2^2-2\hat e\cdot\Delta+1<\lvert\Delta\rvert_2^2`$.

Hence, for $`\lambda<\lambda_n`$,

```math
N_0:\quad h_{(i,j)}\sim h_{(i',j')}\iff\lvert\Delta i\rvert+\lvert\Delta j\rvert=1\quad\text{(square grid graph)}.
\qquad\text{(22.7)}
```

All edges have $`d_0=\sigma/n`$, so (22.4) counts edges:

```math
\ell_0=\tfrac{\sigma}{n}\bigl(\lvert\Delta i\rvert+\lvert\Delta j\rvert\bigr),\qquad
(X_n,\ell_0)\xrightarrow{\rm GH}Y_b=\bigl([0,\sigma]^2,\lVert\cdot\rVert_1\bigr).
\qquad\text{(22.8)}
```

$`Y_b`$ is a compact length space. Its dimension is 2 (G4), since $`\lvert v\rvert_2\le\lVert v\rVert_1\le\sqrt2\lvert v\rvert_2`$. The limit is again the square, now with the taxicab norm:

```math
Y_b\ \text{continuum-like},\ \dim Y_b=2 .
\qquad\text{(22.9)}
```

**Comparison with (a).**
- **Betweenness.** Under $`d_0`$ the between points form the segment; under $`\ell_0`$ they form the axis-parallel box spanned by $`x,z`$ (G3).
- **Geodesics.** In $`Y_b`$ every curve with both coordinates monotone is a geodesic. It is unique only if $`x,z`$ lie on an axis-parallel line; in $`Y_a`$ the geodesic is always unique. In $`X_n`$ the $`\ell_0`$-shortest chains are the monotone lattice paths:

```math
\#\{\ell_0\text{-shortest chains}\}=\binom{\lvert\Delta i\rvert+\lvert\Delta j\rvert}{\lvert\Delta i\rvert}\quad(\text{one under }d_0\text{ in the limit}).
\qquad\text{(22.10)}
```

  - At fixed small $`\lambda`$, the $`\ell`$-geodesics are among these chains (Step 2).
  - If $`[X,Y]=0`$, then $`e^{iK_{h'}\lambda}e^{-iK_h\lambda}=e^{iX\lambda/n}`$ on every horizontal edge (and $`e^{iY\lambda/n}`$ on every vertical one). By (22.1) all edges of one direction then have the same $`\alpha`$, and all (22.10) chains are $`\ell`$-geodesics.
  - Otherwise, $`O(\lambda^2)`$ terms of $`\alpha`$ that $`d_0`$ does not fix may select a subset.
- **Isotropy.** $`Y_a`$ is isotropic. $`Y_b`$ is not, because the $`\lVert\cdot\rVert_1`$ ball is a square.
  - This holds intrinsically. If a unit ball has a boundary segment $`[v,w]`$ with $`v\neq w`$, then $`x+tv`$ and $`x+tw`$ are both midpoints of $`x`$ and $`x+t(v+w)`$.
  - In subsets of Euclidean spaces, midpoints are unique. So $`Y_b`$ is isometric to no Euclidean subset.
- **Largest ratio.** $`\ell_0/d_0=(\lvert\Delta i\rvert+\lvert\Delta j\rvert)/\sqrt{(\Delta i)^2+(\Delta j)^2}`$, with equality iff $`\lvert\Delta i\rvert=\lvert\Delta j\rvert\ge1`$:

```math
\max\ell_0/d_0=\sqrt2\approx1.414 .
\qquad\text{(22.11)}
```

### Step 5. Item 1(c)

**Branch states.** By Step 11 of 19, $`E_h=\cos t\lvert0\rangle+e^{i\mu}\sin t\lvert1\rangle`$ with $`t=\lambda r`$ and $`\mu=\phi-\pi/2`$. The Bloch vector is $`(\sin2t\cos\mu,\sin2t\sin\mu,\cos2t)`$. By (22.1) and (G5),

```math
\alpha(h,h';\lambda)=\text{great-circle distance on }\mathbb S\ (\text{radius }1/2)\text{ between }F_\lambda(x_h,y_h)\text{ and }F_\lambda(x_{h'},y_{h'}).
\qquad\text{(22.12)}
```

**The map $`F_\lambda`$.** $`F_\lambda`$ sends $`(r,\phi)`$ to the point at distance $`\lambda r`$ from $`N=[\lvert0\rangle]`$ along the meridian of azimuth $`\phi-\pi/2`$. This holds for $`\lambda r\le\pi/2`$; beyond that, the meridian runs on past the antipode $`S_0=[\lvert1\rangle]`$. So $`X_n=F_\lambda(\text{lattice points})`$ as a subset of $`(\mathbb S,\alpha)`$.

**Convergence.** By (19.16), $`g\le\lambda^2(\mathrm dr^2+r^2\mathrm d\phi^2)`$, since $`\lvert\sin2\lambda r\rvert\le2\lambda r`$. So $`F_\lambda`$ is $`\lambda`$-Lipschitz. The lattice points lie within $`3r_0/n`$ of every point of the closed disc $`\bar D`$. By (G1),

```math
(X_n,\alpha)\xrightarrow{\rm GH}Y_c=\bigl(F_\lambda(\bar D),\alpha\bigr)=
\begin{cases}\text{closed cap }\{\alpha(N,\cdot)\le\lambda r_0\}\subset\mathbb S, & \lambda r_0<\pi/2,\\ \text{all of }\mathbb S\cong\mathbb{CP}^1, & \lambda r_0\ge\pi/2.\end{cases}
\qquad\text{(22.13)}
```

In all cases $`\dim Y_c=2`$ (G4) and the Gaussian curvature is $`4`$, in agreement with $`\kappa_g=4`$ of (19.17). For the rescaled $`\alpha/\lambda`$ the sphere has radius $`1/(2\lambda)`$ and curvature $`4\lambda^2=\hat\kappa`$. Only $`\lambda r_0`$ matters:

- **(i) $`\lambda r_0\le\pi/4`$.**
  - The cap lies in a closed hemisphere and is convex, so it is a compact geodesic space: continuum-like.
  - Geodesics are minimizing great-circle arcs, and $`y`$ is between $`x,z`$ iff it lies on such an arc.
  - Geodesics are unique except for antipodal pairs. Those occur only on the boundary for $`\lambda r_0=\pi/4`$, and then there is a one-parameter family of geodesics.
  - Radial segments of the disc map to meridians, which are geodesics; other segments do not.
- **(ii) $`\pi/4<\lambda r_0<\pi/2`$.**
  - Take boundary points with azimuths differing by $`\pi`$. They are at distance $`\pi-2\lambda r_0`$, and their unique minimizing arc passes through $`S_0`$.
  - $`S_0`$ is at distance $`\pi/2>\lambda r_0`$ from $`N`$, so $`S_0\notin Y_c`$.
  - A midpoint in $`Y_c`$ would be the sphere midpoint $`S_0`$, so these points have none. By (G2), $`Y_c`$ is not a length space and not continuum-like.
  - Geodesics exist only for pairs whose minimizing arc stays in the cap.
- **(iii) $`\lambda r_0\ge\pi/2`$.**
  - Places with $`\lambda r=\pi/2`$ merge into the point $`S_0`$, and further places merge beyond that.
  - $`Y_c=\mathbb S`$ is a compact geodesic space: continuum-like.
  - Geodesics are great-circle arcs, unique except between antipodal (orthogonal) points, which are joined by a circle of geodesics.

### Step 6. Item 2(a): $`\alpha`$ and $`N_V`$

Here $`k_{h_i,l}=[l\in w_i]`$, so $`\Delta_l\in\{0,\pm1\}`$, nonzero exactly on $`w_i\triangle w_j`$, and $`\lvert w_i\triangle w_j\rvert=2\min(\lvert i-j\rvert,m)`$ by (15.17). By (22.2), for $`\lambda\in(0,\pi/2)`$,

```math
\alpha(h_i,h_j)=\alpha_k:=\arccos\bigl((\cos\lambda)^{2k}\bigr),\qquad k=\min(\lvert i-j\rvert,m),\qquad 0<\alpha_1<\dots<\alpha_m<\tfrac\pi2 .
\qquad\text{(22.14)}
```

So all places are distinct points and all points are related. Since $`\alpha`$ is strictly increasing in $`k`$, (4.3) holds exactly when no $`y`$ has $`\max(k(i,y),k(y,j))<k(i,j)`$. Let $`r=\lvert i-j\rvert`$ with $`i<j`$:
- **$`r=1`$.** A witness would need $`k(i,y)=k(y,j)=0`$, which is impossible. Edge.
- **$`2\le r\le m`$.** $`y=i+1`$ is a witness, with $`k(i,y)=1`$ and $`k(y,j)=r-1`$. No edge.
- **$`m<r\le2m-2`$.** $`y=i+m-1`$ gives $`k(i,y)=m-1`$ and $`k(y,j)=\min(r-m+1,m)\le m-1<m`$. No edge.
- **$`r\ge2m-1`$.** A witness needs $`\lvert i-y\rvert,\lvert y-j\rvert\le m-1`$, hence $`r\le2m-2`$. There is none, so the tie at $`k=m`$ keeps the edge.

Hence, for every $`\lambda\in(0,\pi/2)`$,

```math
h_i\sim h_j\iff\lvert i-j\rvert=1\ \ \text{or}\ \ \lvert i-j\rvert\ge2m-1 .
\qquad\text{(22.15)}
```

### Step 7. Item 2(a): $`\ell`$, diameter, continuum

The graph has "steps" (edges with $`r=1`$, length $`\alpha_1`$) and "jumps" (edges with $`r\ge2m-1`$, length $`\alpha_m`$). A chain with $`J`$ jumps and $`S`$ steps has length $`J\alpha_m+S\alpha_1`$. Let $`1\le r\le2m-2`$.

For $`n\ge2m`$ put $`A:=n-2m+1\ge1`$. A place $`k`$ has a jump to the right iff $`k\le A`$, and a jump to the left iff $`k\ge2m`$. Define the step counts to these two sets and, for a pair $`i<j`$, two combinations of them:

```math
\eta^{\rm R}_k:=\max(0,k-A),\quad \eta^{\rm L}_k:=\max(0,2m-k),\quad
E_2:=\min\bigl(\eta^{\rm R}_i+\eta^{\rm R}_j,\ \eta^{\rm L}_i+\eta^{\rm L}_j\bigr),\quad
E_3:=\min\bigl(\eta^{\rm R}_i+\eta^{\rm L}_j,\ \eta^{\rm L}_i+\eta^{\rm R}_j\bigr).
\qquad\text{(22.30)}
```

**Lower bounds.**
- $`J=0`$: $`S\ge r`$.
- $`J=1`$: if the jump goes from $`p`$ to $`p'`$, then $`S\ge\lvert i-p\rvert+\lvert p'-j\rvert\ge\lvert p-p'\rvert-r\ge2m-1-r`$.
- $`J\ge2`$: a rightward jump starts at $`p\le A`$ and ends at $`\ge2m`$; a leftward jump starts at $`\ge2m`$ and ends at $`\le A`$. The steps before the first jump and those after the last jump are distinct. Hence:
  - first and last jump in opposite directions: $`S\ge E_2`$, so the length is $`\ge2\alpha_m+E_2\alpha_1`$;
  - same direction and $`J\ge3`$: $`S\ge E_3`$, so the length is $`\ge3\alpha_m+E_3\alpha_1`$;
  - same direction and $`J=2`$: the two jumps displace by $`\ge2(2m-1)`$ one way, so $`S\ge4m-2-r`$, and the length exceeds $`\alpha_m+(2m-1-r)\alpha_1`$.

**Attainment.**
- The bound for $`J=1`$ is attained by the jump $`(i-s)\to(j+t)`$ with $`s+t=2m-1-r`$. This chain exists iff $`n\ge2m`$.
- For $`n\ge2m`$, the places $`1`$ and $`n`$ are joined by a jump. In the chains below, each arrow into or out of $`1`$ or $`n`$ is a jump, and every other arrow is a run of steps.
  - $`E_2`$ is attained by $`i\to\min(i,A)\to n\to\min(j,A)\to j`$ or by $`i\to\max(i,2m)\to1\to\max(j,2m)\to j`$.
  - $`E_3`$ is attained by $`i\to\min(i,A)\to n\to1\to\max(j,2m)\to j`$ or by $`i\to\max(i,2m)\to1\to n\to\min(j,A)\to j`$.

Therefore

```math
\ell(h_i,h_j)=\begin{cases}
r\,\alpha_1, & n\le2m-1,\\
\min\{r\alpha_1,\ \alpha_m+(2m-1-r)\alpha_1,\ 2\alpha_m+E_2\alpha_1,\ 3\alpha_m+E_3\alpha_1\}, & n\ge2m,\ 1\le r\le2m-2,\\
\alpha_m, & r\ge2m-1 .
\end{cases}
\qquad\text{(22.16)}
```

For $`n\ge6m-4`$, every pair with $`r\le2m-2`$ has $`E_2=0`$. If $`j\le A`$, then $`\eta^{\rm R}_i=\eta^{\rm R}_j=0`$. Otherwise $`j\ge n-2m+2\ge4m-2`$, so $`i\ge2m`$ and $`\eta^{\rm L}_i=\eta^{\rm L}_j=0`$. So (22.16) reduces there to $`\min\{r\alpha_1,\ \alpha_m+(2m-1-r)\alpha_1,\ 2\alpha_m\}`$.

**Diameter.**
- For distinct points, $`\ell\ge\alpha\ge\alpha_1`$.
- If $`r\le2m-2`$, then $`\ell\le r\alpha_1`$. If $`r\ge2m-1`$, then $`\ell=\alpha_m\le m\alpha_1`$ by the triangle inequality of $`\alpha`$. Hence $`\mathrm{diam}\le(2m-2)\alpha_1`$ for all $`n`$.
- **Exact value for $`n\ge2m`$.** Put $`\zeta:=\alpha_m/\alpha_1\in(1,m]`$, $`w:=4m-1-n=2m-A`$ and $`g(r):=\min\{r\alpha_1,\ \alpha_m+(2m-1-r)\alpha_1\}`$.
  - By (22.16), a pair with $`r\le2m-2`$ has $`\ell=\min\{g(r),\,2\alpha_m+e\,\alpha_1\}`$, with $`e:=\min(E_2,\zeta+E_3)`$.
  - Pairs with $`r\ge2m-1`$ give $`\alpha_m`$, which is less than $`\min\{g(2m-2),2\alpha_m\}`$. Indeed $`(2m-2)\alpha_1>\alpha_m`$: for $`m\ge3`$ because $`\alpha_m\le m\alpha_1`$, and for $`m=2`$ by the Example below.
  - So the diameter is $`\max_r\min\{g(r),\,2\alpha_m+h_n(r)\alpha_1\}`$, with $`h_n(r):=\max_ie(i,i+r)`$.
- **Evaluation of $`h_n`$.** $`\eta^{\rm R}_k=0`$ iff $`k\le A`$, and $`\eta^{\rm L}_k=0`$ iff $`k\ge2m`$. Classify the pairs $`i<j=i+r`$:
  - If $`j\le A`$ or $`i\ge2m`$, then $`E_2=0`$, so $`e=0`$. Otherwise $`i\le2m-1`$ and $`j\ge A+1`$, and four cases remain.
  - **LR**, $`i\le A`$ and $`j\ge2m`$. Then $`E_3=0`$ and $`E_2=\min(j-A,\,2m-i)`$. Both entries are $`\ge\max(1,w)`$ and they sum to $`r+w`$. So the best pair gives $`\lfloor(r+w)/2\rfloor`$, and such pairs exist iff $`r\ge\max(w,2-w)`$.
  - **MR**, $`A<i\le2m-1<j`$, with $`t:=i-A`$.
    - Here $`E_3=\min(t,w+r)=t`$ and $`E_2=\min(2t+r,\,w-t)=w-t`$, because $`j\ge2m`$ gives $`t+r\ge w`$.
    - Hence $`e=\min(w-t,\zeta+t)=\frac{w+\zeta}2-\bigl\lvert t-\frac{w-\zeta}2\bigr\rvert`$, with $`t\in T_r`$, since $`j\le n`$ means $`t+r\le2m-1`$.
    - The reflection $`k\mapsto n+1-k`$ exchanges $`\eta^{\rm R}`$ and $`\eta^{\rm L}`$. So the pairs with $`i\le A<j\le2m-1`$ give the same values.
  - **MM**, $`A<i<j\le2m-1`$ (so $`r\le w-2`$), with $`t:=i-A`$. Here $`E_3=w-r`$ and $`E_2=\min(2t+r,\,2w-2t-r)`$. $`E_2`$ is largest at $`t=\lfloor(w-r)/2\rfloor`$, where it equals $`w-\varepsilon_r`$.

```math
\begin{aligned}
h_n(r)&=\max\{0,\ C_{\rm LR},\ C_{\rm MR},\ C_{\rm MM}\},\\
C_{\rm LR}&=\min\bigl(\lfloor\tfrac{r+w}2\rfloor,\ \zeta\bigr)\qquad\text{if }r\ge\max(w,2-w),\\
C_{\rm MR}&=\tfrac{w+\zeta}2-\mathrm{dist}\bigl(\tfrac{w-\zeta}2,\,T_r\bigr)\qquad\text{if }T_r:=\mathbb Z\cap\bigl[\max(1,w-r),\,\min(w-1,2m-1-r)\bigr]\neq\emptyset,\\
C_{\rm MM}&=\min\bigl(w-\varepsilon_r,\ \zeta+w-r\bigr)\qquad\text{if }r\le w-2,\quad \varepsilon_r:=1\text{ if }w-r\text{ is odd, else }0 .
\end{aligned}
\qquad\text{(22.31)}
```

A candidate whose condition fails is omitted. Hence, for every $`n`$, $`m\ge2`$ and $`\lambda\in(0,\pi/2)`$,

```math
\mathrm{diam}(X_n,\ell)=\begin{cases}
(n-1)\,\alpha_1, & n\le2m-1,\\
\max\limits_{1\le r\le2m-2}\min\bigl\{r\alpha_1,\ \alpha_m+(2m-1-r)\alpha_1,\ 2\alpha_m+h_n(r)\,\alpha_1\bigr\}, & n\ge2m,
\end{cases}
\qquad
\mathrm{diam}(X_n,\ell)\le(2m-2)\alpha_1 .
\qquad\text{(22.17)}
```

Two special cases. Let $`G:=\max_rg(r)=\alpha_1\bigl[\tfrac{2m-1+\zeta}2-\mathrm{dist}\bigl(\tfrac{2m-1+\zeta}2,\{1,\dots,2m-2\}\bigr)\bigr]`$; this holds because $`g(r)=\alpha_1\bigl[\tfrac{2m-1+\zeta}2-\bigl\lvert r-\tfrac{2m-1+\zeta}2\bigr\rvert\bigr]`$.
- **$`n=2m`$.** Here $`w=2m-1`$ and $`T_r=\{2m-1-r\}`$, so $`C_{\rm MR}=g(r)/\alpha_1`$. Hence $`\mathrm{diam}=G`$.
- **$`n\ge6m-4`$.** Here $`w\le3-2m`$, so $`r+w\le1`$ and $`h_n\equiv0`$. Hence $`\mathrm{diam}=\min\{G,2\alpha_m\}\in[\alpha_m,2\alpha_m]`$.

Example $`m=2`$. Since $`2\alpha_1<\alpha_1+\alpha_2<2\alpha_2`$, we get $`\ell=\alpha_1,2\alpha_1,\alpha_2`$ for $`r=1,2,\ge3`$. Also $`\cos2\alpha_1=2\cos^4\lambda-1<\cos^4\lambda`$, so $`2\alpha_1>\alpha_2`$. Hence $`\mathrm{diam}=2\alpha_1`$ for every $`n\ge3`$.

**Not continuum-like.** Suppose $`(X_n,\ell/s_n)\to Y`$, a compact length space with $`D_Y:=\mathrm{diam}Y>0`$.
1. By (G1) and (22.17), $`s_n\le2(2m-2)\alpha_1/D_Y`$ for large $`n`$.
2. So distinct points are at distance $`\ge\alpha_1/s_n\ge\delta:=D_Y/(4m-4)`$.
3. Take correspondences of distortion $`\epsilon_n\to0`$. If $`d_Y(y,y')<\delta-\epsilon_n`$, the partners of $`y,y'`$ are closer than $`\delta`$, hence equal, so $`d_Y(y,y')\le\epsilon_n`$.
4. Therefore $`Y`$ is $`\delta`$-separated, and being compact, it is finite.
5. Repeated midpoints (G2) would give distinct points closer than $`\delta`$, a contradiction.

The same argument holds for $`\ell_0`$: by (22.15) $`N_0`$ is the same graph, and $`\ell_0`$ is (22.16) with $`\alpha_k\to\sqrt{2k}`$, following (15.17). Hence

```math
\text{for every }\lambda\in(0,\tfrac\pi2)\text{ and every choice of }s_n:\ (X_n,\ell/s_n)\text{ and }(X_n,\ell_0/s_n)\text{ are not continuum-like.}
\qquad\text{(22.18)}
```

### Step 8. Item 2(b)

Here $`k_{h_i,l}=q^{\lvert l-i\rvert}`$, with the limit of Step 1. Then $`\langle u_i\vert u_j\rangle=\sum_{l\in\mathbb Z}q^{\lvert l-i\rvert+\lvert l-j\rvert}`$, with $`r:=\lvert i-j\rvert`$. The $`r+1`$ cells between $`i`$ and $`j`$ contribute $`q^r`$ each, and a cell beyond the ends at distance $`s\ge1`$ contributes $`q^{r+2s}`$. So $`\langle u_i\vert u_j\rangle=G(r):=q^r(r+\beta)`$ with $`\beta:=\frac{1+q^2}{1-q^2}`$, and

```math
d_0(h_i,h_j)=\sqrt{2\bigl[\beta(1-q^r)-r\,q^r\bigr]},\qquad
d_0^2(r)-d_0^2(r-1)=2(1-q)q^{r-1}\Bigl(r-\tfrac{q}{1+q}\Bigr)>0,\qquad d_0(1)=\rho_1:=\sqrt{\tfrac{2(1-q)}{1+q}} .
\qquad\text{(22.19)}
```

$`d_0`$ is strictly increasing in $`r`$ and saturates at $`\sqrt{2\beta}`$.

**Neighbour graph.** On a line, $`\max(\lvert x-y\rvert,\lvert y-x'\rvert)=\lvert x-x'\rvert`$ is impossible for distinct points. So there are no ties, and (11.11) applies; Step 2 gives the same graph:
- for $`r\ge2`$, $`y=i+1`$ is a witness (N1);
- for $`r=1`$, every other $`y`$ is at index distance $`\ge2`$ from one of the two (N2).

```math
N_0:\ h_i\sim h_j\iff\lvert i-j\rvert=1 .
\qquad\text{(22.20)}
```

```math
\ell_0(h_i,h_j)=\rho_1\lvert i-j\rvert .
\qquad\text{(22.21)}
```

By the translation invariance of Step 1, all edges have the same $`\alpha_e(\lambda)`$, so $`\ell=\lvert i-j\rvert\alpha_e(\lambda)`$ exactly for $`\lambda<\lambda_n`$. The points $`\rho_1i/n`$ fill $`[0,\rho_1]`$, so

```math
(X_n,\ell_0/n)\xrightarrow{\rm GH}\bigl([0,\rho_1],\lvert\cdot\rvert\bigr),
\qquad\text{(22.22)}
```

a continuum-like limit of dimension 1. Betweenness is the order. The geodesic is unique (the segment), and there is a unique shortest chain.

**Margins.** For $`r\ge2`$, the missing edge rests on a witness $`y`$ between $`i`$ and $`j`$. Its margin is $`d_0(r)-d_0(r')`$ with $`r'=\max(\lvert i-y\rvert,\lvert y-j\rvert)\in[\lceil r/2\rceil,r-1]`$. The largest margin (midpoint witness) and the smallest margin (neighbouring witness) are, by (22.19), with $`s=\lceil r/2\rceil`$:

```math
\delta(r)=\frac{2\bigl[q^s(s+\beta)-q^r(r+\beta)\bigr]}{d_0(r)+d_0(s)}\sim\frac{(s+\beta)\,q^{s}}{\sqrt{2\beta}},\qquad
\Delta(r)=\frac{2(1-q)q^{r-1}\bigl(r-\frac q{1+q}\bigr)}{d_0(r)+d_0(r-1)}\sim\frac{(1-q)\,r\,q^{r-1}}{\sqrt{2\beta}}\quad(r\to\infty).
\qquad\text{(22.23)}
```

The edges ($`r=1`$) rest on the margin $`d_0(2)-d_0(1)=O(1)`$.

The decisions for $`r\ge2`$ rest on margins that are exponentially small in $`r`$. With the uniform remainder estimate (22.3), a sufficient condition for (22.20) is that the relative $`O(\lambda^2)`$ corrections stay below $`\delta(r)/d_0(r)`$ for all $`r\le n-1`$. The sufficient bound on $`\lambda`$ obtained in this way decays exponentially in $`n`$. It is a bound from the remainder estimate, not the stability threshold of the graph: the higher-order terms of $`\alpha`$ for the different pairs may cancel or preserve the inequalities beyond it. The actual threshold below which $`N_V`$ is the path (22.20), including whether it has an $`n`$-independent lower bound, is not determined here.

### Step 9. Item 3(a)

Here $`k_{h_p,l}=q^{\lvert l_1-p_1\rvert}q^{\lvert l_2-p_2\rvert}`$, so $`u_p`$ factorizes. With $`r_k=\lvert p_k-p'_k\rvert`$ and $`G`$ from Step 8, $`\langle u_p\vert u_{p'}\rangle=G(r_1)G(r_2)`$. Hence

```math
d_0(h_p,h_{p'})=\Phi(r_1,r_2):=\sqrt{2\bigl[\beta^2-q^{r_1+r_2}(r_1+\beta)(r_2+\beta)\bigr]}.
\qquad\text{(22.24)}
```

$`G>0`$, and $`G`$ is strictly decreasing, because $`G(r)-G(r+1)=\tfrac12[d_0^2(r+1)-d_0^2(r)]>0`$ by (22.19). So $`\Phi`$ is symmetric and strictly increasing in each argument.

**(11.11) fails.** For $`p=(1,1)`$, $`y=(2,3)`$, $`p'=(3,2)`$: $`\max(\Phi(1,2),\Phi(1,1))=\Phi(2,1)`$, a tie.

**Step 2 decides every pair.**
- $`\lVert\Delta\rVert_1=1`$ falls under (N2), by the argument of Step 4 with $`\Phi`$ in place of the Euclidean distance.
- $`\lVert\Delta\rVert_1\ge2`$ falls under (N1), with $`y=x+\hat e`$ as in Step 4. Then $`\Phi(1,0)<\Phi(\lvert\Delta_1\rvert,\lvert\Delta_2\rvert)`$, and lowering one argument of $`\Phi`$ by 1 lowers it strictly.

```math
N_0=\text{square grid graph on }\{1,\dots,n\}^2 .
\qquad\text{(22.25)}
```

All edges have the same length $`\rho:=\Phi(1,0)=\sqrt{2\beta(\beta-G(1))}=\frac{\sqrt{2(1+q^2)}}{1+q}`$, so

```math
\ell_0(h_p,h_{p'})=\rho\bigl(\lvert\Delta_1\rvert+\lvert\Delta_2\rvert\bigr),
\qquad\text{(22.26)}
```

```math
(X_n,\ell_0/n)\xrightarrow{\rm GH}\bigl([0,1]^2,\ \rho\lVert\cdot\rVert_1\bigr).
\qquad\text{(22.27)}
```

- **Dimension:** 2.
- **Betweenness:** the axis-parallel box spanned by $`x,z`$.
- **Geodesics:** all curves with both coordinates monotone. They are unique iff $`x,z`$ lie on an axis-parallel line.
- **Shortest chains.** By Step 1, every grid edge has the same $`\alpha_e(\lambda)`$ (translation, reflection and exchange symmetry). So for $`\lambda<\lambda_n`$, $`\ell=\lVert\Delta\rVert_1\alpha_e(\lambda)`$ exactly, and

```math
\#\{\ell\text{-geodesics}\}=\#\{\ell_0\text{-shortest chains}\}=\binom{\lvert\Delta_1\rvert+\lvert\Delta_2\rvert}{\lvert\Delta_1\rvert}.
\qquad\text{(22.28)}
```

- **Isotropy: no.** The unit ball $`\{\lVert v\rVert_1\le1/\rho\}`$ is a square, and by the intrinsic argument of Step 4 no rescaling or re-embedding makes the limit Euclidean.

### Step 10. Item 3(b)

**Standard results (G6).**
- **(P1)** *Burago's theorem on periodic metrics, graph version.* Let $`\Gamma\cong\mathbb Z^2`$ act freely on a connected graph with finitely many vertex and edge orbits, with $`\Gamma`$-invariant positive edge lengths. Let $`\pi`$ be a $`\Gamma`$-equivariant map of the vertices into $`\mathbb R^2`$, where $`\Gamma`$ acts by a lattice of translations.
  - Then there is a norm $`\lVert\cdot\rVert_{\rm st}`$ (the stable norm) and a constant $`C`$ with $`\lvert d(x,y)-\lVert\pi x-\pi y\rVert_{\rm st}\rvert\le C`$.
  - Hence, for a compact convex body $`B`$ and $`X_n=\pi^{-1}(nB)`$, $`(X_n,d/n)\to(B,\lVert\cdot\rVert_{\rm st})`$ in GH.
- **(P2)** *Kotani–Sunada.* The unit ball of $`\lVert\cdot\rVert_{\rm st}`$ is the convex polygon $`\mathrm{conv}\{\gamma(c)/w(c)\}`$.
  - Here $`c`$ runs over the finitely many simple cycles of the finite quotient graph that have a nonzero translation $`\gamma(c)`$, and $`w(c)`$ is the length of $`c`$.
  - Reason: if $`x`$ and $`x+v`$ lie in one $`\Gamma`$-orbit, a path between them projects to a closed walk of the quotient graph, which splits into simple cycles. So, up to bounded terms, the distance is the value of the finite linear program $`\min\{\sum_cn_cw(c):n_c\ge0,\ \sum_cn_c\gamma(c)=v\}`$, which is piecewise linear in $`v`$. General endpoints are joined to such pairs by paths of bounded length.
- **(P3)** *John's theorem and Blaschke selection.*
  - Every centrally symmetric convex body $`K\subset\mathbb R^2`$ has a linear $`T`$ with $`\mathbb B\subseteq TK\subseteq\sqrt2\,\mathbb B`$, where $`\mathbb B`$ is the Euclidean unit disc.
  - Compact convex sets inside one fixed disc have Hausdorff-convergent subsequences, with compact convex limits. If convex bodies containing $`\mathbb B`$ converge, their gauges converge uniformly on bounded sets.

**Assumptions on the family.** (P1) concerns one fixed periodic graph on growing domains. The family of 3(b) is first taken as follows; patterns that change with $`n`$ are treated in (i)–(iii) after (22.29).
- **(F1) Fixed pattern.**
  - There is one arrangement on the whole plane, independent of $`n`$.
  - It has places $`\Xi`$ with finitely many $`\Gamma`$-orbits, a $`\Gamma`$-equivariant $`\pi:\Xi\to\mathbb R^2`$, and cells permuted by $`\Gamma`$.
  - The records are carried along by $`\Gamma`$, as in 3(a): $`K_h=\sum_lk_{h,l}\sigma_x^{[l]}`$ with $`k_{\gamma h,\gamma l}=k_{h,l}`$ and $`\sum_lk_{h,l}^2<\infty`$. The medium is infinite in the sense of Step 1.
  - Then $`d_0`$ (22.2) is $`\Gamma`$-invariant. The small-$`\lambda`$ graph $`N_0^\infty`$ on $`\Xi`$, decided by (N1)–(N2), is $`\Gamma`$-periodic with finitely many edge orbits. Let $`d_\infty`$ be its $`d_0`$-weighted graph distance.
- **(F2) Growing domains.**
  - $`X_n:=\pi^{-1}(nB)`$ for one compact convex $`B`$ with interior.
  - $`D_n`$ keeps the places $`X_n`$. Its medium is not cut at the boundary of $`nB`$ but is the limit of Step 1, so $`d_0`$ on $`X_n`$ is the restriction of the pattern's $`d_0`$.
- **(F3) Boundary compatibility.**
  - The neighbour graph of $`D_n`$ is recomputed on $`X_n`$. Removing places removes only possible witnesses, so every edge of $`N_0^\infty`$ inside $`X_n`$ stays an edge.
  - Assume conversely that every non-edge pair in $`X_n`$ keeps an (N1)-witness in $`X_n`$.
  - Assume also that the $`d_0`$-weighted distance $`d_n`$ of the induced graph $`N_0^\infty[X_n]`$ satisfies $`d_n\le d_\infty+C'`$ on $`X_n`$, for a constant $`C'`$.

**Application.**
- By (F1), $`N_0^\infty`$ is $`\Gamma`$-periodic with finitely many edge orbits, and the edge weights $`d_0(e)>0`$ are $`\Gamma`$-invariant.
- By (22.4), $`\ell_0`$ of $`D_n`$ is the $`d_0`$-weighted distance of its recomputed graph. By (F2)–(F3) this graph is $`N_0^\infty[X_n]`$ with the pattern's weights, so $`\ell_0=d_n`$ on $`X_n`$. A chain in $`N_0^\infty[X_n]`$ is a chain in $`N_0^\infty`$, so $`d_\infty\le d_n\le d_\infty+C'`$.
- If $`N_0^\infty`$ is disconnected, $`\ell_0=\infty`$ between components (for large $`n`$), and there is no limit.
- Otherwise:
  - (P1) for $`d_\infty`$ gives $`\bigl\lvert\ell_0(x,y)-\lVert\pi x-\pi y\rVert_{\rm st}\bigr\rvert\le C+C'`$ on $`X_n`$.
  - The map $`x\mapsto\pi x/n`$ has distortion $`\le(C+C')/n`$ for $`\ell_0/n`$, and its image converges to $`B`$ in Hausdorff distance. So $`(X_n,\ell_0/n)\to(B,\lVert\cdot\rVert_{\rm st})`$.
  - By (P2), its unit ball is a polygon. A polygon is never an ellipse, and by Step 4 the limit is not even intrinsically Euclidean.
- Check against 3(a): the quotient graph has one vertex and loops with $`\gamma=\pm\hat e_1,\pm\hat e_2`$ and $`w=\rho`$. Then $`\mathrm{conv}\{\pm\hat e_k/\rho\}`$ is the unit ball of $`\rho\lVert\cdot\rVert_1`$, as in (22.27). There (F1)–(F3) hold with $`C'=0`$: the witnesses $`x+\hat e`$ and the monotone lattice paths stay in the box spanned by the pair, hence in $`X_n`$.
- **Scope.** (22.29) concerns one fixed pattern. Patterns that change with $`n`$ are treated in (i)–(iii) below, and (iii) names the truncations not covered.

```math
\text{Periodic arrangements under (F1)--(F3): the rescaled }\ell_0\text{ never converges to an isotropic limit (polygonal stable norm).}
\qquad\text{(22.29)}
```

**(i) Patterns that change with $`n`$, with boundedly many orbits.**
- **(F1')** $`D_n`$ is built on its own pattern $`\mathcal P_n`$ as in (F1), with lattice $`\Gamma_n`$, map $`\pi_n`$, graph $`N_{0,n}^\infty`$, distance $`d_{\infty,n}`$ and stable norm $`\lVert\cdot\rVert_{{\rm st},n}`$. The quotient graphs $`Q_n:=N_{0,n}^\infty/\Gamma_n`$ have at most $`E_0`$ edges, with $`E_0`$ independent of $`n`$.
- **(F2')–(F3')** (F2) and (F3) hold for each $`n`$, with a compact convex $`B_n`$ in place of $`nB`$ and constants $`C'_n`$.
- **(F4) Uniformity at the scale $`s_n`$.** Let $`D_n:=\sup_{x,y}\bigl\lvert d_{\infty,n}(x,y)-\lVert\pi_nx-\pi_ny\rVert_{{\rm st},n}\bigr\rvert`$, finite by (P1), and $`\rho_n:=\max_{b\in B_n}\min_{x\in X_n}\lVert b-\pi_nx\rVert_{{\rm st},n}`$. Assume $`(D_n+C'_n+\rho_n)/s_n\to0`$.

Argument:
1. **Boundedly many vertices.** A simple cycle of $`Q_n`$ is fixed by its edge set and its orientation, so $`Q_n`$ has at most $`2^{E_0+1}`$ of them. By (P2), the unit ball $`K_n`$ of $`\lVert\cdot\rVert_{{\rm st},n}`$ is a centrally symmetric polygon with at most $`M:=2^{E_0+1}`$ vertices.
2. **Normalization.** By (P3) choose a linear $`T_n`$ with $`\mathbb B\subseteq T_nK_n\subseteq\sqrt2\,\mathbb B`$, and put $`N_n(u):=\lVert T_n^{-1}u\rVert_{{\rm st},n}`$. Then $`\lvert u\rvert/\sqrt2\le N_n(u)\le\lvert u\rvert`$.
3. **Distortion.** As in the Application, $`\ell_0=d_n`$ and $`d_{\infty,n}\le d_n\le d_{\infty,n}+C'_n`$ on $`X_n`$. So $`f_n(x):=T_n\pi_nx/s_n`$ satisfies $`\bigl\lvert\ell_0(x,y)/s_n-N_n(f_nx-f_ny)\bigr\rvert\le(D_n+C'_n)/s_n`$. Its image lies in $`Z_n:=T_nB_n/s_n`$ and is $`\rho_n/s_n`$-dense there for $`N_n`$.
4. **Limit.** Suppose $`(X_n,\ell_0/s_n)\to Y`$. The diameters are bounded, so by step 2 the $`Z_n`$ lie, after translation, in one fixed disc. By (P3) a subsequence has $`Z_n\to Z`$, compact and convex, and $`T_nK_n\to K`$. $`K`$ is the convex hull of the limits of the at most $`M`$ vertices, so it is a polygon with at most $`M`$ vertices, and $`\mathbb B\subseteq K`$. Hence $`N_n\to N_K`$ uniformly on bounded sets, and by step 3 and (G1), $`(X_n,\ell_0/s_n)\to(Z,N_K)`$ along the subsequence. GH limits are unique up to isometry, so $`Y\cong(Z,N_K)`$.
5. **No isotropy.** If $`Z`$ has interior, $`Y`$ has dimension 2 (G4). $`K`$ is a polygon, not an ellipse, and the midpoint argument of Step 4, applied at an interior point of $`Z`$, shows that $`Y`$ is isometric to no Euclidean subset. If $`Z`$ has no interior, it is a segment and $`Y`$ has dimension 1. Every norm on a line is Euclidean, so this degenerate case is excluded.

```math
\text{(F1')--(F4), at most }E_0\text{ edge orbits: every two-dimensional limit of }(X_n,\ell_0/s_n)\text{ has a polygonal norm with at most }2^{E_0+1}\text{ vertices; it is not isotropic.}
\qquad\text{(22.32)}
```

**When (F4) holds.** Let the pairs $`(Q_n,\tau_n)`$ run through finitely many combinatorial types, where $`\tau_n`$ gives each edge of $`Q_n`$ its translation (up to $`GL(2,\mathbb Z)`$ and the choice of lifts). Let the cell size $`a_n`$, $`C'_n`$ and $`\rho_n`$ be $`o(s_n)`$, where $`a_n`$ is the largest edge weight plus the $`\lVert\cdot\rVert_{{\rm st},n}`$-spread of $`\pi_n`$ over one set of orbit representatives. Then $`D_n\le c\,a_n`$, with $`c`$ depending only on the type, so (F4) holds. Short argument:
- Lower bound: a path from $`x`$ to $`y`$, closed by a fixed path of $`Q_n`$, projects to a closed walk. It splits into simple cycles, so its weight is at least $`\lVert\cdot\rVert_{{\rm st},n}`$ of its translation (P2).
- Upper bound: the linear program of (P2) has two equality constraints, so an optimum uses at most two cycles $`c_1,c_2`$, with coefficients $`t_1,t_2`$. Traverse $`\lfloor t_i\rfloor`$ copies of $`c_i`$, reached and left along lifted paths of at most $`E_0`$ edges. The residual $`(t_1-\lfloor t_1\rfloor)\gamma(c_1)+(t_2-\lfloor t_2\rfloor)\gamma(c_2)\in\Gamma_n`$ lies in a finite set fixed by the type, and each of its elements is the translation of a fixed closed walk.
- Every added piece has a type-bounded number of edges, hence weight at most $`c\,a_n`$.

**Bounded orbit counts do not imply (F4).** Take one vertex orbit and three loop orbits with translations $`(1,0)`$, $`(L,1)`$, $`(0,K)`$, $`K\ge2`$, all of weight 1. A walk from $`x`$ to $`x+(0,1)`$ uses the loops $`m_1,m_2,m_3`$ times (signed), with $`m_1+Lm_2=0`$ and $`m_2+Km_3=1`$. Then $`m_2\neq0`$, so the weight is at least $`L+1`$, while $`\lVert(0,1)\rVert_{\rm st}\le1/K`$. So $`D\ge L`$, although the cell is fixed. Whether such graphs arise as small-$`\lambda`$ neighbour graphs of recording descriptions is not determined here.

**(ii) Patterns with unboundedly many orbits: an isotropic family.** The plane and its lines only index places and cells (M5), as $`\mathbb Z^2`$ does in 3(a).
- **Arrangement.** For $`k\ge2`$ let $`\theta_j:=\pi j/k`$, and let $`a_j\in\mathbb Z^2`$ be the componentwise rounding of $`k(\cos\theta_j,\sin\theta_j)`$, $`j=0,\dots,k-1`$.
  - Then $`\lvert a_j-k(\cos\theta_j,\sin\theta_j)\rvert\le1/\sqrt2`$. So the direction of $`a_j`$ is within $`\arcsin\bigl(1/(\sqrt2k)\bigr)<\pi/(2k)`$ of $`\theta_j`$, and the $`a_j`$ are pairwise non-parallel.
  - The lines are $`L_{j,m}:=\{p\in\mathbb R^2:\langle a_j,p\rangle=m\}`$, $`m\in\mathbb Z`$, with positive sides $`L_{j,m}^+:=\{\langle a_j,p\rangle>m\}`$. The arrangement is locally finite, and its regions (the components of the complement) are bounded.
  - Translations by $`\mathbb Z^2`$ permute the lines, preserve the positive sides, and permute the regions.
- **Description $`D_n`$.** Fix a compact convex $`B`$ with interior, and let $`k=k_n\to\infty`$.
  - Places $`h_R`$: the regions $`R`$ that meet the interior of $`nB`$.
  - Medium: one qubit cell for each line that meets $`nB`$, with $`\chi=\lvert0\cdots0\rangle`$.
  - Records $`K_{h_R}=\sum_L[R\subseteq L^+]\,\sigma_x^{[L]}`$.
  - $`D_n`$ is the restriction of the $`\mathbb Z^2`$-invariant pattern with $`k_{\gamma R,\gamma L}=k_{R,L}`$. A line that does not meet $`nB`$ has $`\Delta_L=0`$ for all pairs in $`X_n`$, so further cells would not change (22.2) on $`X_n`$. In the whole pattern $`\sum_Lk_{R,L}^2=\infty`$, but $`\sum_L\Delta_L^2<\infty`$, which is all that Step 1 uses.
- **Distances.** By (22.2), $`\Delta_L=\pm1`$ exactly on the set $`{\rm sep}(R,R')`$ of lines separating $`R`$ and $`R'`$, and $`\Delta_L=0`$ otherwise. Let $`G_k`$ be the region graph, $`R\sim_GR'`$ iff $`\lvert{\rm sep}(R,R')\rvert=1`$, and $`d_G`$ its graph distance on $`X_n`$ (chains in $`X_n`$).
  - Every edge changes the side of exactly one line, so every chain from $`R`$ to $`R'`$ crosses each separating line. Its length is at least $`\lvert{\rm sep}\rvert`$.
  - Take $`p\in R`$ and $`p'\in R'`$ in the interior of $`nB`$, with $`[p,p']`$ avoiding the crossing points of lines. The segment stays in $`nB`$ (convexity), and it crosses each separating line once and no other line. The regions it passes form a chain in $`X_n`$ of length $`\lvert{\rm sep}\rvert`$.
  - $`{\rm sep}(R,R'')={\rm sep}(R,R')\triangle{\rm sep}(R',R'')`$, so the parity of $`\lvert{\rm sep}\rvert`$ forbids triangles in $`G_k`$.

```math
\cos\alpha(h_R,h_{R'};\lambda)=(\cos\lambda)^{d_G(R,R')},\qquad d_0(h_R,h_{R'})=\sqrt{d_G(R,R')},\qquad d_G(R,R')=\lvert{\rm sep}(R,R')\rvert\ \text{ on }X_n .
\qquad\text{(22.33)}
```

- **Neighbour graph, for every $`\lambda\in(0,\pi/2)`$.** By (22.33), $`\alpha<\pi/2`$, distinct regions are distinct points, and $`\alpha`$ is strictly increasing in $`d_G`$.
  - $`d_G=1`$: every other $`y`$ has $`\max(d_G(R,y),d_G(y,R'))\ge2`$, since there are no triangles. There is no witness: edge.
  - $`d_G\ge2`$: the second region of the segment chain lies in $`X_n`$ and gives $`\max(1,d_G-1)<d_G`$. No edge.
  - Edges have $`\alpha=\lambda`$ and $`d_0=1`$, so

```math
N_V=G_k[X_n],\qquad \ell=\lambda\,d_G,\qquad \ell_0=d_G\qquad\text{on }X_n,\ \text{for every }\lambda\in(0,\tfrac\pi2).
\qquad\text{(22.34)}
```

- **Large scale.** Take $`p\in R`$, $`p'\in R'`$ off the lines. Family $`j`$ contributes the integers strictly between $`\langle a_j,p\rangle`$ and $`\langle a_j,p'\rangle`$; their number differs from $`\lvert\langle a_j,p-p'\rangle\rvert`$ by less than 1. Hence $`\lvert d_G(R,R')-N_k(p-p')\rvert<k`$, with $`N_k(v):=\sum_j\lvert\langle a_j,v\rangle\rvert`$.
  - For a unit vector $`u`$ at angle $`\varphi`$, the rounding gives $`\bigl\lvert N_k(u)-k\sum_j\lvert\cos(\theta_j-\varphi)\rvert\bigr\rvert\le k/\sqrt2`$.
  - $`\lvert\cos(\cdot-\varphi)\rvert`$ is $`\pi`$-periodic and 1-Lipschitz, with integral 2 over a period. The Riemann sum therefore gives $`\bigl\lvert\sum_j\lvert\cos(\theta_j-\varphi)\rvert-2k/\pi\bigr\rvert\le\pi/2`$. Together:

```math
N_k(v)=\tfrac{2k^2}{\pi}\lvert v\rvert\,\bigl(1+\varepsilon_k(v)\bigr),\qquad\lvert\varepsilon_k(v)\rvert<\tfrac4k .
\qquad\text{(22.35)}
```

- **Limit.** Put $`s_n:=2k_n^2n/\pi`$ and map $`R\mapsto p_R/n`$, with $`p_R\in R`$ as above.
  - The distortion for $`\ell_0/s_n`$ against $`\lvert\cdot\rvert`$ is at most $`\pi/(2k_nn)+4\mathrm{diam}(B)/k_n\to0`$.
  - Each region lies in a parallelogram cell of the families $`j=0`$ and $`j=\lfloor k/2\rfloor`$, of diameter at most 2. So the image is within $`2/n`$ of $`B`$ in Hausdorff distance.
  - By (G1) and (G3):

```math
(X_n,\ell_0/s_n)\xrightarrow{\rm GH}\bigl(B,\lvert\cdot\rvert_2\bigr),\ \text{and }(X_n,\ell/(\lambda s_n))\text{ likewise for every }\lambda\in(0,\tfrac\pi2):\ \text{continuum-like, of dimension 2, isotropic.}
\qquad\text{(22.36)}
```

- Each pattern $`\mathcal P_k`$ is periodic with finitely many edge orbits. Its number of region orbits is at least $`k/2`$: each region lies in a strip of width $`1/k`$ between lines of family 0 and has diameter at most 2, so its area is at most $`2/k`$, while a unit cell has area 1. This is consistent with (22.32).
- Check: for $`k=2`$, $`a_0=(2,0)`$ and $`a_1=(0,2)`$. The regions are squares of side $`1/2`$, $`G_2`$ is the square grid graph, and $`N_2=2\lVert\cdot\rVert_1`$, as in 3(a).
- The records are half-plane indicators, not local records of the kind of items 2–3.

**(iii) What remains open.**
- Patterns with uniformly bounded orbit counts for which (F4) fails, that is, whose defect $`D_n`$ is not $`o(s_n)`$ (cycle translations unbounded relative to $`s_n`$, as in the example of (i)). (P1) holds for each member, but its constant is not uniform, and no standard result on limits of such families is used here. Whether they can have an isotropic limit is not determined.
- Truncations whose recomputed neighbour graph gains edges at the boundary, so that no (F3)-type bound holds. Such edges can shorten $`\ell_0`$ by amounts not controlled here.
- Local records on patterns with growing cells: (22.36) uses half-plane records. Whether local records of the kind of items 2–3 can give an isotropic limit is not determined.

## Result

- **1(a)** $`d_0=\frac\sigma n\sqrt{\Delta i^2+\Delta j^2}`$ (22.5).
  - Limit: the Euclidean square $`[0,\sigma]^2`$ (22.6), of dimension 2 and flat.
  - Betweenness is the segment; geodesics are unique straight segments; the limit is isotropic.
- **1(b)** For small $`\lambda`$, $`N_0`$ is the square grid graph (22.7), decided directly from (4.3) despite ties.
  - $`\ell_0=\frac\sigma n(\lvert\Delta i\rvert+\lvert\Delta j\rvert)`$, with limit $`([0,\sigma]^2,\lVert\cdot\rVert_1)`$ (22.8)–(22.9).
  - Betweenness is the box. There are $`\binom{\lvert\Delta i\rvert+\lvert\Delta j\rvert}{\lvert\Delta i\rvert}`$ shortest chains (22.10), all $`\ell`$-geodesics if $`[X,Y]=0`$.
  - The limit is not isotropic. $`\max\ell_0/d_0=\sqrt2`$ (22.11).
- **1(c)** $`\alpha`$ is the great-circle distance on the sphere of radius $`1/2`$ (22.12).
  - Limit (22.13): the cap of radius $`\lambda r_0`$ (for $`\lambda r_0<\pi/2`$) or the whole $`\mathbb{CP}^1`$ (for $`\lambda r_0\ge\pi/2`$).
  - Dimension 2, curvature 4.
  - Length space iff $`\lambda r_0\le\pi/4`$ or $`\lambda r_0\ge\pi/2`$. Geodesics are great-circle arcs.
- **2(a)** $`\alpha=\arccos(\cos^{2\min(r,m)}\lambda)`$ (22.14).
  - $`N_V`$ has the edges $`r=1`$ and $`r\ge2m-1`$, for every $`\lambda\in(0,\pi/2)`$ (22.15).
  - $`\ell`$ is given exactly for every $`n`$ by (22.16), with the hub-chain terms (22.30).
  - The diameter is given exactly for every $`n`$ by (22.17) with (22.31). It equals $`G`$ for $`n=2m`$ and $`\min\{G,2\alpha_m\}`$ for $`n\ge6m-4`$, and it is at most $`(2m-2)\alpha_1`$, independent of $`n`$.
  - **Not continuum-like** for any $`s_n`$, for $`\ell`$ and for $`\ell_0`$ (22.18).
- **2(b)** $`d_0`$ is given by (22.19). $`N_0`$ is the path (22.20) and $`\ell_0=\rho_1\lvert i-j\rvert`$ (22.21).
  - Limit: the segment $`[0,\rho_1]`$, of dimension 1 (22.22).
  - Decisive margins are $`\sim(\lceil r/2\rceil+\beta)q^{\lceil r/2\rceil}/\sqrt{2\beta}`$ (22.23).
- **3(a)** $`d_0=\Phi(r_1,r_2)`$ (22.24). $`N_0`$ is the grid (22.25) and $`\ell_0=\rho\lVert\Delta\rVert_1`$ (22.26).
  - Limit: $`([0,1]^2,\rho\lVert\cdot\rVert_1)`$ (22.27), of dimension 2. Betweenness is the box; geodesics are non-unique.
  - There are $`\binom{\lvert\Delta_1\rvert+\lvert\Delta_2\rvert}{\lvert\Delta_1\rvert}`$ shortest chains (22.28). The limit is **not isotropic**.
- **3(b)** **Yes**, the rescaled $`\ell_0`$ can converge to an isotropic limit, but only through patterns that change with $`n`$:
  - **No** for a fixed periodic pattern on growing convex domains whose recomputed graphs are the induced subgraphs, (F1)–(F3): the limit norm is polygonal (22.29).
  - **No** for patterns that change with $`n`$ with at most $`E_0`$ edge orbits, under the uniformity (F4): every two-dimensional limit has a polygonal norm with at most $`2^{E_0+1}`$ vertices (22.32). (F4) holds for finitely many combinatorial types with cells small compared with $`s_n`$.
  - **Yes** for patterns with unboundedly many orbits: line arrangements with $`k_n\to\infty`$ directions and half-plane records give $`N_V=G_k[X_n]`$ and $`\ell_0=d_G`$ for every $`\lambda\in(0,\pi/2)`$ (22.33)–(22.34), and the Euclidean limit $`(B,\lvert\cdot\rvert_2)`$ with $`s_n=2k_n^2n/\pi`$ (22.35)–(22.36).
  - Open: bounded orbit counts without (F4), truncations that create edges, and local records with growing cells.
- **Goal.**
  - Compact local records give no large-scale continuum through $`\ell`$, because saturation ties create long edges.
  - Exponential tails do give one through $`\ell_0`$ with $`s_n=n`$, of dimension 1 and 2.
  - The large-scale geometry is the $`\ell^1`$ norm, not isotropic. A fixed periodic pattern, (F1)–(F3), cannot make it isotropic, nor can boundedly many orbits under (F4). Periodic patterns with growing cells and half-plane records can (22.36).

## Consistency checks

1. **Dimensions.** $`\alpha`$ and $`\ell`$ are angles. $`\lambda d_0`$ and $`\lambda\ell_0`$ are dimensionless, because $`K_h`$ carries the inverse unit of $`\lambda`$: $`d_0,\ell_0\propto\sigma`$ in 1(a)–(b). In 1(c), only $`\lambda r_0`$ enters the case distinction.
2. **Small $`\lambda`$.**
   - (22.14) gives $`\alpha_k=\arccos(1-k\lambda^2+O(\lambda^4))`$, so $`\alpha_k/\lambda\to\sqrt{2k}`$, which is (15.17).
   - In 1(c), $`u_h=(x_h+iy_h)\lvert1\rangle`$, so $`d_0`$ is Euclidean. This is (22.5) with $`\sigma_X=\sigma_Y=1`$ and $`\mathrm{Cov}=\mathrm{Re}\langle0\vert\sigma_x\sigma_y\vert0\rangle=0`$.
   - It matches the $`\lambda r_0\to0`$ limit of (22.13) rescaled by $`1/\lambda`$: a cap of radius $`r_0`$ on a sphere of radius $`1/(2\lambda)`$ tends to the flat disc.
3. **$`q\to0`$ in 2(b) against $`m=1`$.**
   - (22.19) tends to $`\sqrt2`$ for all $`r\ge1`$, which is (15.17) with $`m=1`$. There (22.15) gives the complete graph, through ties.
   - The path (22.20) does not tend to it. This is consistent with the margins (22.23) vanishing as $`q\to0`$: the neighbour relation is not continuous where its margins vanish.

## Open issues

- 1(b), non-commuting $`X,Y`$: which of the (22.10) chains are $`\ell`$-geodesics at fixed small $`\lambda`$ depends on $`O(\lambda^2)`$ terms of $`\alpha`$, not on $`d_0`$.
- 2(b), 3(a): the uniform remainder estimate (22.3) gives only sufficient small-$`\lambda`$ bounds. In 2(b), with the margins (22.23), these bounds shrink exponentially with $`n`$; for 3(a) the margins are not computed here. The actual stability thresholds of the neighbour graphs, including whether they have an $`n`$-independent lower bound, are not determined, and neither are the fixed-$`\lambda`$ neighbour graphs for large $`n`$.
- 3(b): (22.29) and (22.32) rely on (P1)–(P3) as standard results and on (F1)–(F4). Not determined (Step 10 (iii)):
  - patterns with uniformly bounded orbit counts for which (F4) fails;
  - truncations that create new edges at the boundary;
  - whether local records, rather than the half-plane records of (22.36), can give an isotropic limit on patterns with growing cells.

## Methods used

- Partial trace of a block-diagonal evolution; product states of qubit cells
- Small-parameter expansion; strict-inequality persistence (relative neighbourhood graph)
- Weighted graph distances, shortest paths, lattice-path counting
- Gromov–Hausdorff convergence via Hausdorff convergence; separation argument
- Normed planes (Euclidean, $`\ell^1`$), betweenness, midpoint uniqueness
- Bloch sphere / Fubini–Study geometry of $`\mathbb{CP}^1`$, spherical caps and convexity
- Stable norms of periodic graphs (Burago, Kotani–Sunada)
- John's theorem, Blaschke selection, linear-programming rounding
- Line arrangements and their region graphs (separating-line counts), Riemann sums
