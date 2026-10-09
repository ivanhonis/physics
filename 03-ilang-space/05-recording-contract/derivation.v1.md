# Recording contract: exact witness data and leading-order witness geometry

- **Subproject:** 03-ilang-space
- **Package:** 05-recording-contract
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-08

## Setup and assumptions

- Two objects $`a`$, $`c`$ of different types, each the only instance of its type. There is no pair of objects of the same type, so (1.11) and Law 5 impose no constraint and $`\mathcal H_{\rm adm}=\mathcal H=\mathcal H_{T(a)}\otimes\mathcal H_c`$. Part $`A=\{a\}`$, companion $`\bar A=\{c\}`$. $`a`$ has $`d_{T(a)}`$ places (finite, A1), and $`d_c=\dim\mathcal H_c`$.
- Recording contract $`C=\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$ with $`K_h=K_h^\dagger`$ on $`\mathcal H_c`$, independent of $`\lambda`$ (A5). This is a single pair term of the form (1.10), and $`C^\dagger=\sum_h\lvert h\rangle\langle h\rvert\otimes K_h^\dagger=C`$.
- Initial state $`\lvert\Psi(0)\rangle=\lvert\phi\rangle\otimes\lvert\chi\rangle`$, $`\lvert\phi\rangle=\sum_h\phi_h\lvert h\rangle`$, $`\phi_h\neq0`$ for all $`h`$, $`\lVert\phi\rVert=\lVert\chi\rVert=1`$. $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$ and $`\mathrm{Var}_\chi X:=\langle X^2\rangle-\langle X\rangle^2`$.
- $`\lambda\ge0`$ is only the ordering parameter of (1.9) (M2). The only approximation is the expansion $`\lambda\to0^+`$ in Steps 4 and 5. Every other statement is exact for all $`\lambda\ge0`$.
- Inputs as quoted: (2.1), (2.2), (2.11) from 02-view-content@v1, and (3.1), (3.2), (3.5) from 03-witness-distance@v1, with the notation $`p_h`$, $`H_V`$, $`\lvert\psi_h\rangle`$, $`G_{hh'}`$, $`\approx`$, $`X_V`$, $`\alpha`$ fixed there. The $`\lambda`$-dependence is written explicitly: $`p_h(\lambda)`$, $`W(h,h';\lambda)`$, $`\alpha(h,h';\lambda)`$.

## Derivation

### Step 1. Exact evolution

The projectors $`\Pi_h:=\lvert h\rangle\langle h\rvert`$ satisfy $`\Pi_h\Pi_{h'}=\delta_{hh'}\Pi_h`$ and $`\sum_h\Pi_h=\mathbb 1`$ (place basis orthonormal, A2). By induction $`C^n=\sum_h\Pi_h\otimes K_h^n`$ for $`n\ge0`$ ($`n=0`$: $`\sum_h\Pi_h\otimes\mathbb 1=\mathbb 1`$). Summing the exponential series, which converges in finite dimension, gives

```math
e^{-iC\lambda}=\sum_h\lvert h\rangle\langle h\rvert\otimes e^{-iK_h\lambda},
\tag{5.1}
```

and so by (1.9)

```math
\lvert\Psi(\lambda)\rangle=\sum_h\phi_h\,\lvert h\rangle\otimes e^{-iK_h\lambda}\lvert\chi\rangle .
\tag{5.2}
```

### Step 2. Weights, $`H_V`$ and branch states

Comparing (5.2) with (2.1) gives $`\lvert\psi_h(\lambda)\rangle=\phi_h e^{-iK_h\lambda}\lvert\chi\rangle`$. Since $`e^{-iK_h\lambda}`$ is unitary and $`\lVert\chi\rVert=1`$, (2.2) gives

```math
p_h(\lambda)=\lVert\psi_h(\lambda)\rVert^2=\lvert\phi_h\rvert^2,\qquad H_V=H_{T(a)}\quad\text{for every }\lambda\ge0 ,
\tag{5.3}
```

because $`\phi_h\neq0`$ for every $`h`$. The state (5.2) has the form (1.6) with $`a_h=\phi_h`$ and the unit branch states

```math
\lvert E_h(\lambda)\rangle=e^{-iK_h\lambda}\lvert\chi\rangle,\qquad
\varrho_h(\lambda)=e^{-iK_h\lambda}\lvert\chi\rangle\langle\chi\rvert e^{iK_h\lambda}.
\tag{5.4}
```

Another phase split in (1.6) multiplies $`\lvert E_h\rangle`$ by a unit factor and leaves $`\varrho_h`$ (3.1) unchanged.

### Step 3. View and witness data

From (5.4) and (2.2) with $`\lvert\psi_h\rangle=\phi_h\lvert E_h\rangle`$:

```math
G_{hh'}(\lambda)=\langle E_{h'}\vert E_h\rangle=\langle\chi\vert e^{iK_{h'}\lambda}e^{-iK_h\lambda}\vert\chi\rangle,
\qquad
\bigl(V_A(\lambda)\bigr)_{hh'}=\phi_h\phi_{h'}^{*}\,G_{hh'}(\lambda).
\tag{5.5}
```

By (2.11), $`W=\lvert G_{hh'}\rvert^2`$:

```math
W(h,h';\lambda)=\bigl\lvert\langle\chi\vert e^{iK_{h'}\lambda}e^{-iK_h\lambda}\vert\chi\rangle\bigr\rvert^2 .
\tag{5.6}
```

$`W`$ does not depend on $`\phi`$. It is also independent of the conventions listed in M6. The common phase (1.2) and the phase split between $`\lvert\phi\rangle`$ and $`\lvert\chi\rangle`$ only multiply $`\lvert\chi\rangle`$ by a unit factor, and this factor cancels in (5.6).

### Step 4. Small-$`\lambda`$ expansion of $`W`$

Let $`A:=K_h`$, $`B:=K_{h'}`$ and $`D:=A-B`$. In finite dimension both exponentials are convergent power series, so Taylor's theorem with remainder applies:

```math
e^{iB\lambda}e^{-iA\lambda}=\mathbb 1-i\lambda D-\frac{\lambda^2}{2}\bigl(A^2+B^2-2BA\bigr)+O(\lambda^3).
\tag{5.7}
```

Taking the expectation in $`\lvert\chi\rangle`$ gives $`G_{hh'}=1-i\lambda\langle D\rangle-\tfrac{\lambda^2}{2}\mu+O(\lambda^3)`$ with $`\mu:=\langle A^2\rangle+\langle B^2\rangle-2\langle BA\rangle`$. Self-adjointness makes $`\langle A^2\rangle,\langle B^2\rangle,\langle D\rangle`$ real and gives $`\langle AB\rangle=\langle BA\rangle^*`$, so $`\mathrm{Re}\mu=\langle A^2\rangle+\langle B^2\rangle-\langle AB\rangle-\langle BA\rangle=\langle D^2\rangle`$. In $`W=G_{hh'}G_{hh'}^*`$ the first-order terms $`\mp i\lambda\langle D\rangle`$ cancel. The second order is $`\lambda^2\langle D\rangle^2-\lambda^2\mathrm{Re}\mu`$, so

```math
W(h,h';\lambda)=1-\lambda^2\mathrm{Var}_\chi(K_h-K_{h'})+O(\lambda^3).
\tag{5.8}
```

Since $`\lvert u_h\rangle-\lvert u_{h'}\rangle=(D-\langle D\rangle)\lvert\chi\rangle`$ and $`D-\langle D\rangle`$ is self-adjoint,

```math
\mathrm{Var}_\chi(K_h-K_{h'})=\langle\chi\vert(D-\langle D\rangle)^2\vert\chi\rangle=\bigl\lVert u_h-u_{h'}\bigr\rVert^2 .
\tag{5.9}
```

### Step 5. Limit of the witness angle

By (3.5), $`\alpha(h,h';\lambda)=\arccos\sqrt{W(h,h';\lambda)}\in[0,\pi/2]`$, so $`\sin^2\alpha=1-W`$. By (5.8) and (5.9) there are constants $`c,\lambda_1>0`$ such that $`1-W=\lambda^2\lVert u_h-u_{h'}\rVert^2+R(\lambda)`$ with $`\lvert R(\lambda)\rvert\le c\lambda^3`$ for $`0<\lambda\le\lambda_1`$. The radicand below equals $`\sin^2\alpha/\lambda^2\ge0`$, and $`\sqrt{\cdot}`$ is continuous on $`[0,\infty)`$, hence

```math
\frac{\sin\alpha}{\lambda}=\sqrt{\lVert u_h-u_{h'}\rVert^2+R(\lambda)/\lambda^2}\;\longrightarrow\;\lVert u_h-u_{h'}\rVert .
```

In particular $`\sin\alpha\to0`$. On $`[0,\pi/2]`$ this forces $`\alpha\to0`$, and then $`\alpha/\sin\alpha\to1`$ (the ratio is set to $`1`$ where $`\alpha=0`$). Therefore

```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
\tag{5.10}
```

The argument needs no case distinction, so it covers $`\mathrm{Var}_\chi(K_h-K_{h'})=0`$. In that case $`d_0=0`$ and $`\alpha=O(\lambda^{3/2})`$.

### Step 6. Euclidean structure and dimension

$`(\mathcal H_c,g)`$ with $`g(v,w):=\mathrm{Re}\langle v\vert w\rangle`$ is a real Euclidean space of dimension $`2d_c`$ with $`g(v,v)=\lVert v\rVert^2`$ (standard).

(i) *Isometry.* By (5.10), $`d_0(h,h')=\sqrt{g(u_h-u_{h'},u_h-u_{h'})}`$ is the Euclidean distance of $`u_h`$ and $`u_{h'}`$. So $`d_0`$ is a pseudometric on $`H_V`$ with $`d_0(h,h')=0\iff u_h=u_{h'}`$. Define $`h\sim_0h'`$ iff $`u_h=u_{h'}`$. Then $`[h]_0\mapsto u_h`$ is a well-defined, distance-preserving bijection:

```math
\bigl(H_V/{\sim_0},\,d_0\bigr)\;\cong\;\bigl(\{u_h:h\in H_V\},\,\lVert\cdot\rVert\bigr)\subset(\mathcal H_c,g).
\tag{5.11}
```

The conventions of M6 change $`\lvert\chi\rangle`$ only by a unit factor $`e^{i\theta}`$. Then $`u_h\mapsto e^{i\theta}u_h`$, which is a $`g`$-isometry. So the configuration is fixed up to a global isometry, and $`d_0`$ is invariant.

(ii) *Criterion.* $`d_0(h,h')=0`$ iff $`D\lvert\chi\rangle=\langle D\rangle\lvert\chi\rangle`$. Conversely, if $`D\lvert\chi\rangle=z\lvert\chi\rangle`$, then $`z=\langle\chi\vert D\vert\chi\rangle=\langle D\rangle`$. Hence

```math
d_0(h,h')=0\iff(K_h-K_{h'})\lvert\chi\rangle\in\mathbb C\lvert\chi\rangle .
\tag{5.12}
```

(iii) *Orthogonality.*

```math
\langle\chi\vert u_h\rangle=\langle K_h\rangle-\langle K_h\rangle\langle\chi\vert\chi\rangle=0 ,
\tag{5.13}
```

so every $`u_h`$ lies in $`\chi^\perp`$. This is a complex subspace of dimension $`d_c-1`$, that is, a real subspace of dimension $`2d_c-2`$: the $`g`$-orthogonal complement of $`\lvert\chi\rangle`$ and $`i\lvert\chi\rangle`$.

(iv) *Dimension.* Let $`\dim_0:=\dim_{\mathbb R}\mathrm{aff}_{\mathbb R}\{u_h\}`$. There are at most $`d_{T(a)}`$ points, so their affine span has dimension at most $`d_{T(a)}-1`$. By (5.13) the span lies in the linear subspace $`\chi^\perp`$. Hence

```math
\dim_0\le\min\bigl(d_{T(a)}-1,\;2d_c-2\bigr).
\tag{5.14}
```

The bound is attained. For any $`w\in\chi^\perp`$, the operator $`K=\lvert w\rangle\langle\chi\rvert+\lvert\chi\rangle\langle w\rvert`$ is self-adjoint with $`K\lvert\chi\rangle=w`$ and $`\langle K\rangle=0`$, so $`u=w`$. Let $`m`$ be the right side of (5.14). Choose $`u=0`$ for one place, a real basis of an $`m`$-dimensional real subspace of $`\chi^\perp`$ for $`m`$ further places, and $`u=0`$ for the remaining places. This gives $`\dim_0=m`$.

### Step 7. Example (a): line

In Steps 7 and 8 the imaginary unit is written $`\mathrm i`$, because $`i`$ and $`j`$ are indices. Since $`\langle K_{h_i}\rangle=i\langle X\rangle`$, we get $`u_{h_i}=i\,u_X`$ with $`\lvert u_X\rangle=(X-\langle X\rangle)\lvert\chi\rangle`$, and $`\lVert u_X\rVert^2=\mathrm{Var}_\chi X=\sigma_X^2`$ by the computation in (5.9). By (5.10),

```math
d_0(h_i,h_j)=\lvert i-j\rvert\,\sigma_X .
\tag{5.15}
```

Since $`\sigma_X>0`$, $`u_X\neq0`$, and the points $`i\,u_X`$ are distinct and equally spaced on the line $`\mathbb R u_X`$. So $`\sim_0`$ is trivial, $`(H_V,d_0)`$ is isometric to $`\sigma_X\{1,\dots,n\}\subset\mathbb R`$, and $`\dim_0=1`$ for $`n\ge2`$ ($`\dim_0=0`$ for $`n=1`$).

$`K_{h_i}=iX`$ and $`K_{h_j}=jX`$ are functions of the same $`X`$, so they commute and $`e^{\mathrm i jX\lambda}e^{-\mathrm i iX\lambda}=e^{-\mathrm i(i-j)\lambda X}`$. By (5.6), exactly for all $`\lambda\ge0`$,

```math
W(h_i,h_j;\lambda)=F\bigl((i-j)\lambda\bigr),\qquad F(s):=\bigl\lvert\langle\chi\vert e^{-\mathrm isX}\vert\chi\rangle\bigr\rvert^2 .
\tag{5.16}
```

$`F(-s)=F(s)`$, because $`\langle\chi\vert e^{\mathrm isX}\vert\chi\rangle=\langle\chi\vert e^{-\mathrm isX}\vert\chi\rangle^*`$. So $`W`$ depends only on $`\lvert i-j\rvert\lambda`$. As a cross-check, (5.8) gives $`F(s)=1-s^2\sigma_X^2+O(s^3)`$, consistent with (5.15).

### Step 8. Example (b): plane

Linearity gives $`u_{h_{(i,j)}}=i\,u_X+j\,u_Y`$, with $`\lVert u_X\rVert=\sigma_X`$, $`\lVert u_Y\rVert=\sigma_Y:=\sqrt{\mathrm{Var}_\chi Y}`$ and $`g(u_X,u_Y)=\mathrm{Cov}_\chi(X,Y)=\tfrac12\langle XY+YX\rangle-\langle X\rangle\langle Y\rangle`$. Here $`\sigma_X,\sigma_Y\ge0`$, and positivity is not assumed. With $`\Delta i:=i-i'`$ and $`\Delta j:=j-j'`$, (5.10) gives

```math
d_0\bigl(h_{(i,j)},h_{(i',j')}\bigr)=\sqrt{\sigma_X^2(\Delta i)^2+2\mathrm{Cov}_\chi(X,Y)\,\Delta i\,\Delta j+\sigma_Y^2(\Delta j)^2}\, .
\tag{5.17}
```

*Square lattice.* Suppose $`d_0=\sigma\sqrt{(\Delta i)^2+(\Delta j)^2}`$ for all pairs, with $`\sigma>0`$. Since $`n\ge2`$, the differences $`(\Delta i,\Delta j)=(1,0),(0,1),(1,1)`$ all occur, from $`(2,1),(1,2),(2,2)`$ against $`(1,1)`$. Then (5.17) gives $`\sigma_X^2=\sigma^2`$, $`\sigma_Y^2=\sigma^2`$ and $`\sigma_X^2+2\mathrm{Cov}_\chi(X,Y)+\sigma_Y^2=2\sigma^2`$. The converse is immediate from (5.17). Hence

```math
d_0=\sigma\sqrt{(\Delta i)^2+(\Delta j)^2}\ \text{ for all pairs}
\iff
\sigma_X=\sigma_Y=\sigma>0\ \text{ and }\ \mathrm{Cov}_\chi(X,Y)=0 .
\tag{5.18}
```

Equivalently, $`u_X`$ and $`u_Y`$ are $`g`$-orthogonal and have equal non-zero length. Then $`(i,j)\mapsto u_{h_{(i,j)}}`$ is an isometry from the square lattice $`\sigma\{1,\dots,n\}^2\subset\mathbb R^2`$ onto $`\{u_h\}`$.

*Dimension.* Each difference $`u_{h_{(i,j)}}-u_{h_{(1,1)}}=(i-1)u_X+(j-1)u_Y`$ is a combination of $`u_X`$ and $`u_Y`$, and both occur as differences ($`n\ge2`$). So the affine span is $`u_{h_{(1,1)}}+\mathrm{span}_{\mathbb R}\{u_X,u_Y\}`$, and $`\dim_0`$ is the rank of the real Gram matrix $`\bigl(\begin{smallmatrix}\sigma_X^2&\mathrm{Cov}\\ \mathrm{Cov}&\sigma_Y^2\end{smallmatrix}\bigr)`$. Cauchy–Schwarz gives $`\lvert\mathrm{Cov}_\chi(X,Y)\rvert\le\sigma_X\sigma_Y`$, and

```math
\dim_0=2\iff\lvert\mathrm{Cov}_\chi(X,Y)\rvert<\sigma_X\sigma_Y .
\tag{5.19}
```

$`\dim_0=1`$ if $`\lvert\mathrm{Cov}_\chi\rvert=\sigma_X\sigma_Y`$ and $`\sigma_X^2+\sigma_Y^2>0`$, and $`\dim_0=0`$ if $`\sigma_X=\sigma_Y=0`$. The square-lattice condition (5.18) implies (5.19). Only real independence matters, so (5.18) can already hold for $`d_c=2`$, where (5.14) allows $`\dim_0\le2`$. Example: $`\lvert\chi\rangle=\lvert0\rangle`$, $`X=\lvert0\rangle\langle1\rvert+\lvert1\rangle\langle0\rvert`$, $`Y=-\mathrm i\lvert0\rangle\langle1\rvert+\mathrm i\lvert1\rangle\langle0\rvert`$. Then $`u_X=\lvert1\rangle`$, $`u_Y=\mathrm i\lvert1\rangle`$, $`\sigma_X=\sigma_Y=1`$ and $`\mathrm{Cov}_\chi=0`$.

## Result

1. Exact evolution: $`e^{-iC\lambda}`$ (5.1), $`\lvert\Psi(\lambda)\rangle`$ (5.2), $`p_h(\lambda)=\lvert\phi_h\rvert^2`$ with $`H_V=H_{T(a)}`$ (5.3), branch states (5.4), view (5.5), and $`W(h,h';\lambda)`$ as expected (5.6).
2. Small $`\lambda`$: $`W=1-\lambda^2\mathrm{Var}_\chi(K_h-K_{h'})+O(\lambda^3)`$ (5.8), with $`\mathrm{Var}_\chi(K_h-K_{h'})=\lVert u_h-u_{h'}\rVert^2`$ (5.9), and $`\alpha/\lambda\to d_0=\lVert u_h-u_{h'}\rVert`$ including the zero-variance case (5.10).
3. Geometry: $`(H_V/{\sim_0},d_0)`$ is isometric to $`\{u_h\}\subset(\mathcal H_c,\mathrm{Re}\langle\cdot\vert\cdot\rangle)`$ (5.11); $`d_0=0`$ iff $`(K_h-K_{h'})\lvert\chi\rangle\propto\lvert\chi\rangle`$ (5.12); $`\langle\chi\vert u_h\rangle=0`$ (5.13); $`\dim_0\le\min(d_{T(a)}-1,\,2d_c-2)`$, and the bound is attained (5.14).
4. Line: $`d_0=\lvert i-j\rvert\sigma_X`$, $`\dim_0=1`$ (5.15), and exactly $`W=F((i-j)\lambda)`$ with $`F`$ even (5.16). Plane: $`d_0`$ (5.17); square lattice iff $`\sigma_X=\sigma_Y>0`$ and $`\mathrm{Cov}_\chi(X,Y)=0`$ (5.18); $`\dim_0=2`$ iff $`\lvert\mathrm{Cov}_\chi(X,Y)\rvert<\sigma_X\sigma_Y`$ (5.19).

No discrepancy with the expected result.

## Consistency checks

1. **$`\lambda=0`$.** (5.2) gives $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$, and (5.6) gives $`W(h,h';0)=\lvert\langle\chi\vert\chi\rangle\rvert^2=1`$ for all pairs. So all places are $`\approx`$-equivalent and $`X_V`$ is a single point.
2. **All $`K_h=K`$.** $`e^{iK\lambda}e^{-iK\lambda}=\mathbb 1`$, so $`W\equiv1`$ by (5.6). All $`u_h`$ are equal, so $`d_0\equiv0`$ and $`\dim_0=0`$, consistent with (5.8) at zero variance.
3. **$`K_h\lvert\chi\rangle=k_h\lvert\chi\rangle`$ for all $`h`$.** (5.4) gives $`\lvert E_h\rangle=e^{-ik_h\lambda}\lvert\chi\rangle`$, so $`W=\lvert e^{-i(k_h-k_{h'})\lambda}\rvert^2\equiv1`$ and $`u_h=(k_h-k_h)\lvert\chi\rangle=0`$, consistent with (5.12) and (5.13).

## Open issues

- $`d_0(h,h')=0`$ gives only $`1-W=o(\lambda^2)`$. It does not imply $`h\approx h'`$ at $`\lambda>0`$ when $`K_h`$ and $`K_{h'}`$ do not commute, because the higher orders of (5.7) contain products like $`BA`$. Conversely, $`W=1`$ at isolated $`\lambda`$ (revivals, for example $`F(s_0)=1`$ in (5.16) for integer spectrum of $`X`$) does not imply $`d_0=0`$. So $`\sim_0`$ and $`\approx`$ at finite $`\lambda`$ are different identifications. Their relation at finite $`\lambda`$ is out of scope.
- In (b), the exact finite-$`\lambda`$ form of $`W`$ is not derived. It depends only on $`(\Delta i\,\lambda,\Delta j\,\lambda)`$ when $`[X,Y]=0`$, by the argument of Step 7, but in general not otherwise. Large $`\lambda`$ is out of scope.

## Methods used

- Functional calculus for block-diagonal (controlled) operators; matrix exponential
- Taylor expansion with remainder of matrix exponentials
- Witness-rule inputs: view via partial trace (2.2), witness overlap (2.11), angle (3.5)
- Realification of a complex Hilbert space; Euclidean distance, affine span, Gram matrix, Cauchy–Schwarz
