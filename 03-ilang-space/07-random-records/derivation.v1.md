# Random record operators: the generic leading-order witness geometry

- **Subproject:** 03-ilang-space
- **Package:** 03-ilang-space/07-random-records
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-08

## Setup and assumptions

**Description** (setting of 05, as quoted in question.md). Two objects $`a`$, $`c`$ of different types, each the only instance of its type; part $`A=\{a\}`$. Contract $`C=\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$; initial state $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\phi_h\neq0`$ for every $`h`$, so all $`n:=d_{T(a)}\ge2`$ places of $`a`$ enter (5.10)–(5.14). $`d_c:=\dim\mathcal H_c\ge2`$; orthonormal basis $`e_1=\lvert\chi\rangle,e_2,\dots,e_{d_c}`$ of $`\mathcal H_c`$; $`K_{ab}:=\langle e_a\vert K\vert e_b\rangle`$. $`E`$ denotes expectation over the ensemble.

**Inputs** (05-recording-contract@v1). With $`g(v,w):=\mathrm{Re}\langle v\vert w\rangle`$, $`(\mathcal H_c,g)`$ is a real Euclidean space of dimension $`2d_c`$; $`h\sim_0h'`$ means $`u_h=u_{h'}`$; $`\dim_0:=\dim_{\mathbb R}\mathrm{aff}_{\mathbb R}\{u_h\}`$.
- (5.10): $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$, $`\lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle`$, where $`d_0`$ is the leading-order distance, $`\alpha(h,h';\lambda)=\lambda d_0(h,h')+o(\lambda)`$.
- (5.11): $`\bigl(H_V/{\sim_0},d_0\bigr)\cong\bigl(\{u_h\},\lVert\cdot\rVert\bigr)\subset(\mathcal H_c,g)`$.
- (5.13): $`\langle\chi\vert u_h\rangle=0`$.
- (5.14): $`\dim_0\le\min\bigl(d_{T(a)}-1,\,2d_c-2\bigr)`$.

**Ensembles** (definitions of question.md). $`K_1,\dots,K_n`$ i.i.d. from
- $`\mathrm{GUE}(s)`$: $`K=K^\dagger`$; $`K_{ab}`$ ($`a<b`$) complex Gaussian with independent real and imaginary parts $`N(0,s^2/2)`$; $`K_{aa}`$ real $`N(0,s^2)`$; all independent.
- $`\mathrm{GOE}(s)`$: $`K`$ real symmetric in the basis $`(e_a)`$; $`K_{ab}`$ ($`a<b`$) real $`N(0,s^2)`$; $`K_{aa}`$ real $`N(0,2s^2)`$; all independent.

**Real coordinates.** The vectors $`\{e_a,\,ie_a\}_{a\ge2}`$ are $`g`$-orthonormal ($`g(e_a,ie_b)=\mathrm{Re}(i\delta_{ab})=0`$, $`g(ie_a,ie_b)=\delta_{ab}`$) and span $`\chi^\perp=\mathrm{span}_{\mathbb C}\{e_2,\dots,e_{d_c}\}`$. For $`v=\sum_{a\ge2}v_ae_a`$: $`g(e_a,v)=\mathrm{Re}v_a`$, $`g(ie_a,v)=\mathrm{Im}v_a`$, and $`\lVert v\rVert^2=g(v,v)=\sum_{a\ge2}\bigl[(\mathrm{Re}v_a)^2+(\mathrm{Im}v_a)^2\bigr]`$. So $`(\chi^\perp,g)\cong\mathbb R^{2(d_c-1)}`$ isometrically. Likewise $`\chi^\perp_{\mathbb R}:=\mathrm{span}_{\mathbb R}\{e_2,\dots,e_{d_c}\}`$ is a real subspace of $`(\mathcal H_c,g)`$ with $`g`$-orthonormal basis $`e_2,\dots,e_{d_c}`$, so $`(\chi^\perp_{\mathbb R},g)\cong\mathbb R^{d_c-1}`$.

**Assumptions.** (i) The $`K_h`$ are random but $`\lambda`$-independent (A5); every statement concerns the leading-order geometry (5.10)–(5.14), valid as $`\lambda\to0^+`$. (ii) "Almost surely" and "in probability" refer to the ensemble of descriptions. (iii) No meaning is attached to the configuration beyond these definitions (M1, M4).

**Standard facts used without proof.** (F1) Linear images of jointly Gaussian variables are Gaussian; functions of independent variables are independent; if $`X_1,\dots,X_k`$ are i.i.d. $`N(0,\sigma^2)`$, then $`\sum_jX_j^2=\sigma^2\chi^2_k`$, with density of a Gamma law of shape $`k/2`$ and scale $`2\sigma^2`$, mean $`k\sigma^2`$, variance $`2k\sigma^4`$. A complex Gaussian vector with zero mean and zero pseudo-covariance is circularly symmetric. (F2) Independent random vectors with absolutely continuous laws on $`\mathbb R^m`$ are almost surely in general position: any $`k\le m+1`$ of them are affinely independent. (F3) Chebyshev's inequality, Cauchy–Schwarz, the union bound.

## Derivation

### Step 1. The record vector is the first column of $`K_h`$ (both ensembles)

$`\langle K_h\rangle=\langle\chi\vert K_h\vert\chi\rangle=(K_h)_{11}`$ and, by completeness of $`(e_a)`$, $`K_h\lvert\chi\rangle=\sum_a(K_h)_{a1}e_a`$. Hence (5.10) gives

```math
\lvert u_h\rangle=\sum_{a=2}^{d_c}(K_h)_{a1}\,e_a\;\in\chi^\perp ,
\qquad\text{(7.1)}
```

in agreement with (5.13). Since $`\chi`$ and the basis are fixed, $`u_h`$ is a function of $`K_h`$ alone. The $`K_h`$ are i.i.d., so by (F1) the $`u_h`$, $`h=1,\dots,n`$, are **independent and identically distributed**. For given $`K_h`$, replacing $`\chi`$ by $`e^{i\varphi}\chi`$ (1.2) multiplies every $`u_h`$ by $`e^{i\varphi}`$, a $`g`$-isometry; $`d_0`$ and $`\dim_0`$ are unchanged (M6).

### Step 2. GUE: circularly symmetric Gaussian record vectors

Put $`z_{h,a}:=(K_h)_{a1}=(K_h)_{1a}^{*}`$ for $`a=2,\dots,d_c`$ (self-adjointness). The $`(K_h)_{1a}`$, $`a\ge2`$, are distinct strictly upper entries, hence independent, each with independent real and imaginary parts $`N(0,s^2/2)`$; complex conjugation flips the sign of the imaginary part and preserves this law. Therefore

```math
\mathrm{Re}z_{h,a},\ \mathrm{Im}z_{h,a}\quad(a=2,\dots,d_c)\quad\text{are i.i.d. } N(0,s^2/2),
\qquad\text{(7.2)}
```

so $`Ez_{h,a}=0`$, $`E[z_{h,a}z_{h,b}^{*}]=s^2\delta_{ab}`$, and $`E[z_{h,a}z_{h,b}]=0`$ (for $`a=b`$: $`E(\mathrm{Re}z)^2-E(\mathrm{Im}z)^2+2iE[\mathrm{Re}z\mathrm{Im}z]=0`$; for $`a\neq b`$: independence). For a unit vector $`e=\sum_{a\ge2}c_ae_a\in\chi^\perp`$, $`\langle e\vert u_h\rangle=\sum_ac_a^{*}z_{h,a}`$ and

```math
E\bigl\lvert\langle e\vert u_h\rangle\bigr\rvert^2=\sum_{a,b}c_a^{*}c_b\,E[z_{h,a}z_{h,b}^{*}]=s^2\sum_a\lvert c_a\rvert^2=s^2,
\qquad
E\,\langle e\vert u_h\rangle^2=0 .
\qquad\text{(7.3)}
```

Thus $`u_h`$ is Gaussian (F1), with mean $`0`$, covariance $`E\lvert u_h\rangle\langle u_h\rvert=s^2\mathbb 1_{\chi^\perp}`$, $`\mathbb 1_{\chi^\perp}=\mathbb 1-\lvert\chi\rangle\langle\chi\rvert`$, and zero pseudo-covariance: it is circularly symmetric. Its density on $`\chi^\perp`$, with respect to Lebesgue measure in the real coordinates, is

```math
p(u)=(\pi s^2)^{-(d_c-1)}\exp\bigl(-\lVert u\rVert^2/s^2\bigr).
\qquad\text{(7.4)}
```

It depends on $`u`$ only through $`\lVert u\rVert`$, so it does not depend on the choice of $`e_2,\dots,e_{d_c}`$. In the real Euclidean space $`(\chi^\perp,g)`$ the law is isotropic with variance $`s^2/2`$ per $`g`$-unit direction; the complex covariance $`s^2`$ and the real variance $`s^2/2`$ describe the same law.

### Step 3. GUE: distances

Let $`h\neq h'`$ and $`w:=u_h-u_{h'}`$. By Step 1 and (7.2), the $`2(d_c-1)`$ real coordinates of $`w`$ are i.i.d. $`N(0,s^2)`$, each being the difference of two independent $`N(0,s^2/2)`$ variables. With $`\lVert w\rVert^2`$ the sum of their squares, (F1) gives

```math
d_0(h,h')^2=\lVert u_h-u_{h'}\rVert^2\;\overset{d}{=}\;s^2\,\chi^2_{2(d_c-1)},
\qquad
p_{d_0^2}(x)=\frac{x^{d_c-2}\,e^{-x/(2s^2)}}{(d_c-2)!\,(2s^2)^{d_c-1}}\quad(x>0),
\qquad\text{(7.5)}
```

```math
E\,d_0^2=2(d_c-1)\,s^2,\qquad
\mathrm{Var}d_0^2=4(d_c-1)\,s^4,\qquad
\frac{\sqrt{\mathrm{Var}d_0^2}}{E\,d_0^2}=\frac{1}{\sqrt{d_c-1}} .
\qquad\text{(7.6)}
```

These depend only on $`s`$ and $`d_c`$: not on $`h,h'`$, $`n`$, $`\phi`$, $`\chi`$ or the basis. The mean also follows from (7.3): $`E\,d_0^2=E\lVert u_h\rVert^2+E\lVert u_{h'}\rVert^2=2(d_c-1)s^2`$. Since $`d_0^2`$ has a density, $`P\bigl(d_0(h,h')=0\bigr)=0`$. Almost surely $`\sim_0`$ is therefore trivial, and by (5.11) the leading-order space consists of $`n`$ distinct points $`u_h`$ of $`(\chi^\perp,g)`$.

### Step 4. GUE: dimension

By (7.1), all $`u_h`$ lie in $`\chi^\perp\cong\mathbb R^{2(d_c-1)}`$, and $`\dim_0=\mathrm{rank}_{\mathbb R}\{u_h-u_1\}_{h=2}^{n}\le\min\bigl(n-1,2(d_c-1)\bigr)`$. This is (5.14). The $`u_h`$ are independent with the density (7.4), so by (F2) they are almost surely in general position. If $`n\le2d_c-1`$, all $`n`$ points are affinely independent and $`\dim_0=n-1`$. Otherwise, any $`2d_c-1`$ of them are affinely independent and span an affine subspace of dimension $`2(d_c-1)`$, so $`\dim_0\ge2(d_c-1)`$. Hence

```math
\dim_0=\min\bigl(n-1,\;2(d_c-1)\bigr)\qquad\text{almost surely},
\qquad\text{(7.7)}
```

and the bound (5.14) is attained.

### Step 5. GOE: the real variant

Now $`z_{h,a}:=(K_h)_{a1}=(K_h)_{1a}`$ is real for $`a\ge2`$, and these are distinct strictly upper entries, i.i.d. $`N(0,s^2)`$. By (7.1), $`u_h\in\chi^\perp_{\mathbb R}`$, with i.i.d. $`N(0,s^2)`$ coordinates in the $`g`$-orthonormal basis $`e_2,\dots,e_{d_c}`$:

```math
u_h\sim N\bigl(0,\,s^2\mathbb 1_{\chi^\perp_{\mathbb R}}\bigr),\qquad
p(u)=(2\pi s^2)^{-(d_c-1)/2}\exp\bigl(-\lVert u\rVert^2/(2s^2)\bigr),
\qquad\text{(7.8)}
```

independent for different $`h`$ (Step 1). Hence $`E\,g(e,u_h)^2=s^2`$ for every unit $`e\in\chi^\perp_{\mathbb R}`$, and $`E\lVert u_h\rVert^2=(d_c-1)s^2`$ as for the GUE. The coordinates of $`u_h-u_{h'}`$ ($`h\neq h'`$) are i.i.d. $`N(0,2s^2)`$, so by (F1)

```math
d_0(h,h')^2\;\overset{d}{=}\;2s^2\,\chi^2_{d_c-1},
\qquad
p_{d_0^2}(x)=\frac{x^{(d_c-3)/2}\,e^{-x/(4s^2)}}{\Gamma\bigl(\tfrac{d_c-1}{2}\bigr)\,(4s^2)^{(d_c-1)/2}}\quad(x>0),
\qquad\text{(7.9)}
```

```math
E\,d_0^2=2(d_c-1)\,s^2,\qquad
\mathrm{Var}d_0^2=8(d_c-1)\,s^4,\qquad
\frac{\sqrt{\mathrm{Var}d_0^2}}{E\,d_0^2}=\sqrt{\frac{2}{d_c-1}} ,
\qquad\text{(7.10)}
```

which again depend only on $`s`$ and $`d_c`$. Again $`\sim_0`$ is almost surely trivial. The argument of Step 4 in $`\chi^\perp_{\mathbb R}\cong\mathbb R^{d_c-1}`$, with the density (7.8), gives

```math
\dim_0=\min\bigl(n-1,\;d_c-1\bigr)\qquad\text{almost surely}.
\qquad\text{(7.11)}
```

For $`n>d_c`$ this is strictly below the bound (5.14), so the GOE does not attain (5.14) there.

### Step 6. Unified form

Let $`m=2(d_c-1)`$ (GUE) or $`m=d_c-1`$ (GOE), and let $`\mathcal R_m:=(\chi^\perp,g)`$ or $`(\chi^\perp_{\mathbb R},g)`$ respectively. Let $`\sigma^2:=2(d_c-1)s^2/m`$, that is, $`\sigma^2=s^2`$ (GUE) or $`2s^2`$ (GOE). Steps 1–5 then read: the $`u_h`$ are i.i.d. isotropic Gaussian points $`N\bigl(0,\tfrac{\sigma^2}{2}\mathbb 1_m\bigr)`$ in the $`m`$-dimensional Euclidean space $`\mathcal R_m`$, and

```math
d_0(h,h')^2\overset{d}{=}\sigma^2\chi^2_m,\qquad
E\,d_0^2=m\sigma^2=2(d_c-1)s^2,\qquad
\frac{\sqrt{\mathrm{Var}d_0^2}}{E\,d_0^2}=\sqrt{\frac{2}{m}},\qquad
\dim_0\overset{\text{a.s.}}{=}\min(n-1,m).
\qquad\text{(7.12)}
```

Since $`\mathrm{GUE}(s)`$ and $`\mathrm{GOE}(s)`$ are the images of the $`s=1`$ ensembles under $`K\mapsto sK`$, (7.1) gives $`u_h\mapsto su_h`$. The law of every ratio of distances is therefore independent of $`s`$.

### Step 7. Regime (a): $`n`$ fixed, $`d_c\to\infty`$

Fix $`h\neq h'`$ and set $`X:=d_0(h,h')^2/(m\sigma^2)`$. By (7.12), $`EX=1`$ and $`\mathrm{Var}X=2/m`$. Let $`\bar d:=E\,d_0(h,h')`$; it is common to all pairs, because all pairs $`(u_h,u_{h'})`$ have the same law. Put $`Y:=\sqrt X`$ and $`\mu:=EY=\bar d/(\sigma\sqrt m)`$. For $`x\ge0`$, $`\lvert\sqrt x-1\rvert=\lvert x-1\rvert/(\sqrt x+1)\le\lvert x-1\rvert`$, and Cauchy–Schwarz gives

```math
\lvert\mu-1\rvert\le E\lvert Y-1\rvert\le E\lvert X-1\rvert\le\sqrt{2/m}.
\qquad\text{(7.13)}
```

Let $`0<\epsilon\le1`$ and $`m\ge32/\epsilon^2`$, so that $`\sqrt{2/m}\le\epsilon/4`$ and $`\mu\ge3/4`$. Then $`\lvert Y/\mu-1\rvert\le2\bigl(\lvert Y-1\rvert+\lvert1-\mu\rvert\bigr)\le2\lvert X-1\rvert+\epsilon/2`$, so $`\lvert d_0/\bar d-1\rvert>\epsilon`$ implies $`\lvert X-1\rvert>\epsilon/4`$. Chebyshev gives $`P(\lvert X-1\rvert>\epsilon/4)\le32/(m\epsilon^2)`$. The union bound over the $`\binom n2`$ pairs then gives

```math
P\Bigl(\max_{h\neq h'}\Bigl\lvert\frac{d_0(h,h')}{\bar d}-1\Bigr\rvert>\epsilon\Bigr)\le\frac{16\,n(n-1)}{m\,\epsilon^2}\xrightarrow[d_c\to\infty]{}0 ,
\qquad\text{(7.14)}
```

since $`m\ge d_c-1\to\infty`$ in both ensembles. By Step 6 this holds for any dependence $`s=s(d_c)`$. All normalized distances therefore converge to $`1`$ in probability, jointly. The distance matrix of $`\{u_h/\bar d\}`$ tends to that of the regular $`(n-1)`$-simplex with unit edge, and a finite subset of a Euclidean space is fixed up to isometry by its distance matrix. The normalized configuration therefore tends, up to isometry, to a regular simplex. This is consistent with (7.12): once $`m\ge n-1`$, $`\dim_0=n-1`$ almost surely. By (7.13), $`\bar d=\sigma\sqrt m\,\bigl(1+O(m^{-1/2})\bigr)\simeq s\sqrt{2(d_c-1)}`$ in both ensembles.

### Step 8. Regime (b): $`n>m+1`$

By Step 6, $`u_1,\dots,u_n`$ are $`n`$ independent Gaussian points $`N\bigl(0,\tfrac{\sigma^2}{2}\mathbb 1_m\bigr)`$ in the $`m`$-dimensional Euclidean space $`\mathcal R_m`$. Since $`\sim_0`$ is almost surely trivial, (5.11) makes the leading-order space $`(H_V/{\sim_0},d_0)`$ isometric to this configuration. By (7.12), for $`n\ge m+1`$ (in particular for $`n>m+1`$),

```math
\dim_0=m=\begin{cases}2(d_c-1)&\mathrm{GUE}(s)\\ d_c-1&\mathrm{GOE}(s)\end{cases}\qquad\text{almost surely},
\qquad\text{(7.15)}
```

independently of $`n`$. Further places only add points in the same $`\mathcal R_m`$ and never raise $`\dim_0`$. For $`n>m+1`$ the points are affinely dependent, while any $`m+1`$ of them are almost surely affinely independent. The value $`m`$ is fixed by the medium $`c`$, through $`d_c`$ and the complex or real class of the records, not by $`n`$.

## Result

1. **Record vectors (GUE):** $`u_h=\sum_{a\ge2}(K_h)_{a1}e_a`$ (7.1), i.i.d. in $`h`$, circularly symmetric complex Gaussian in $`\chi^\perp`$ with mean $`0`$ and covariance $`s^2\mathbb 1_{\chi^\perp}`$ (7.2)–(7.4); this is real variance $`s^2/2`$ per $`g`$-direction.
2. **Distances (GUE):** $`d_0^2=s^2\chi^2_{2(d_c-1)}`$ (7.5); mean $`2(d_c-1)s^2`$, variance $`4(d_c-1)s^4`$, relative standard deviation $`1/\sqrt{d_c-1}`$ (7.6). All depend only on $`s`$ and $`d_c`$; $`\sim_0`$ is trivial almost surely.
3. **Dimension (GUE):** $`\dim_0=\min(n-1,2(d_c-1))`$ almost surely (7.7); the bound (5.14) is attained.
4. **GOE:** $`u_h\sim N(0,s^2\mathbb 1)`$ in $`\chi^\perp_{\mathbb R}`$ (7.8); $`d_0^2=2s^2\chi^2_{d_c-1}`$, mean $`2(d_c-1)s^2`$, variance $`8(d_c-1)s^4`$, relative standard deviation $`\sqrt{2/(d_c-1)}`$ (7.9)–(7.10); $`\dim_0=\min(n-1,d_c-1)`$ almost surely (7.11), below (5.14) for $`n>d_c`$.
5. **Regimes:** unified form (7.12). (a) For fixed $`n`$, $`\max_{h\neq h'}\lvert d_0/\bar d-1\rvert\to0`$ in probability as $`d_c\to\infty`$, with the explicit bound (7.14): the normalized configuration tends to a regular simplex. (b) For $`n\ge m+1`$, $`\dim_0=m`$ almost surely (7.15), fixed by the medium.

All expected results of question.md are confirmed; no discrepancy in any distribution, factor or dimension. Minor sharpening: (7.15) already holds at $`n=m+1`$.

## Consistency checks

1. **Dimensions.** The exponent $`\mathrm{Tr}K^2/s^2`$ is dimensionless, so $`s`$ carries the unit of $`K_h`$, that is, of $`C`$. By (5.10), $`d_0=\lVert u_h-u_{h'}\rVert`$ carries the unit of $`K_h`$, since $`\chi`$ is a unit vector. (7.5)–(7.6) and (7.9)–(7.10) give $`d_0^2\propto s^2`$ and $`\mathrm{Var}d_0^2\propto s^4`$, while chi-square variables and relative deviations are dimensionless. The two sides agree.
2. **Qubit medium, $`d_c=2`$.** GUE: $`u_h=z_{h,2}e_2`$ lies in the complex line $`\mathbb Ce_2\cong\mathbb R^2`$; $`m=2`$ and (7.7) gives $`\dim_0=2`$ for $`n\ge3`$, since three independent points of the plane with densities are almost surely not collinear. Directly, $`\lvert z_{h,2}-z_{h',2}\rvert^2`$ is exponential with mean $`2s^2`$, which is $`s^2\chi^2_2`$ with relative deviation $`1=1/\sqrt{d_c-1}`$, as (7.5)–(7.6) state. GOE: the points lie on the line $`\mathbb Re_2`$, $`\dim_0=1`$ for every $`n\ge2`$, and $`(x_h-x_{h'})^2`$ with $`x_h-x_{h'}\sim N(0,2s^2)`$ is $`2s^2\chi^2_1`$, matching (7.9) and (7.11).
3. **$`s\to0`$.** $`E\,d_0^2=2(d_c-1)s^2\to0`$, so every $`d_0\to0`$ in mean square and all places merge into one point, $`u_h\to0`$. This is consistent with $`K_h\to0`$ leaving no record by (5.10). For every $`s>0`$, $`\dim_0`$ and the law of $`d_0/\bar d`$ do not depend on $`s`$ (Step 6): $`s`$ only sets the unit of $`d_0`$, and the collapse occurs only at $`s=0`$.

## Open issues

- $`\mathrm{GOE}(s)`$ is defined relative to the basis $`(e_a)`$ with $`e_1=\chi`$. It therefore uses a real structure in which $`\chi`$ is real, which is not part of the description data. The results (7.8)–(7.11) are invariant under real orthogonal changes of $`e_2,\dots,e_{d_c}`$. The GUE results do not depend on the basis at all (7.4).
- Distances that share a place, such as $`d_0(1,2)`$ and $`d_0(1,3)`$, are correlated through $`u_1`$. Only the union bound was needed in (7.14); the joint law is out of scope.
- All statements are leading order in $`\lambda`$; finite $`\lambda`$ and non-Gaussian ensembles are out of scope.

## Methods used

- Matrix elements in an adapted orthonormal basis
- Gaussian ensembles (GUE, GOE) and their entry distributions
- Circularly symmetric complex Gaussian vectors, real realification of $`\mathbb C^{k}`$
- Chi-square and Gamma distributions
- General position of absolutely continuous random vectors, affine dimension
- Chebyshev inequality, Cauchy–Schwarz, union bound, convergence in probability
- Scaling argument
