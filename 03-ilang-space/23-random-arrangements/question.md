# Question: 23-random-arrangements

- **Subproject:** 03-ilang-space
- **Package:** 23-random-arrangements
- **Equation tags:** (23.k)
- **Created:** 2026-10-09

## Goal

Determine by a precommitted numerical run, in parts T1–T4, two properties of the small-$`\lambda`$ chain geometry $`\ell_0`$ of quasi-local records in two dimensions:
- whether non-periodic (random) arrangements of places give an isotropic large-scale geometry;
- how robust the neighbour graph and $`\ell_0`$ are against small changes of the records.

22 showed that every fixed periodic arrangement gives a polygonal, anisotropic norm (22.29). This package tests random arrangements numerically; it addresses criterion 4. Isotropy means the same as in 22: the large-scale distance is a Euclidean norm.

**Precommitment.**
- Every model, parameter, seed, size, window, tolerance and decision rule is fixed in this question before the run. None may be changed.
- If a part cannot be run as specified, report that, and do not modify the part.
- Every reported number must be produced by the scripts and saved as raw output.
- A decision follows the stated rule only. No other criterion may be substituted after the run.
- Parts marked exploratory have no decision.

**Common setting.**
- **Medium.** An $`L\times L`$ torus of qubit cells $`l\in(\mathbb Z/L\mathbb Z)^2`$, with $`\chi=\lvert0\cdots0\rangle`$ (one object, as in 15 and 22). $`\lvert v\rvert_T`$ is the Euclidean length of the minimal image of $`v`$ on the torus.
- **Places and records.** Places $`h`$ have centres $`c_h`$. In T1–T3 the centres are grid points; in T4 they are not. The records are
  ```math
  K_h=\sum_l\kappa(l-c_h)\,\sigma_x^{[l]}
  ```
  with one of two kernels, where $`\xi=2`$:
  - **separable:** $`\kappa_{\rm sep}(v)=e^{-(\lvert v_1\rvert_T+\lvert v_2\rvert_T)/\xi}`$, where $`\lvert v_k\rvert_T`$ is the minimal-image absolute value of the coordinate;
  - **isotropic:** $`\kappa_{\rm iso}(v)=e^{-\lvert v\rvert_T/\xi}`$.
- **Distances.** By (22.2), $`d_0(h,h')^2=\sum_l(\kappa(l-c_h)-\kappa(l-c_{h'}))^2`$. With the overlap $`S(h,h'):=\sum_l\kappa(l-c_h)\kappa(l-c_{h'})`$, this is $`d_0^2=S(h,h)+S(h',h')-2S(h,h')`$.
- **Neighbour graph.** $`N_0`$ is the graph of (4.3) applied to $`d_0`$: $`\{x,x'\}`$ is an edge iff no third place $`y`$ has $`\max\bigl(d_0(x,y),d_0(y,x')\bigr)<d_0(x,x')`$. A tie keeps the edge, as the strict inequality requires.
  - Where (N1)/(N2) of 22 decide, this is the small-$`\lambda`$ neighbour graph.
  - Report the number of pairs whose status rests on a tie.
- **Chain distance.** $`\ell_0`$ is the $`d_0`$-weighted shortest-path distance in $`N_0`$ (22.4).
- **Numerical exactness.**
  - For far pairs, $`d_0`$ is close to its saturation value, and the decisions rest on very small differences.
  - All comparisons that decide neighbours must be made without cancellation. For example, compare overlaps where the norms are equal, or compare $`d_0^2-S(0)`$-type quantities computed directly from their small terms. Never subtract nearly equal large numbers.
  - Overlaps $`S`$ of far pairs must be computed with relative (not only absolute) accuracy. Sums of positive terms qualify; FFT-based correlations do not, for values below $`10^{-12}S(0)`$.
  - Where all places have equal norms by symmetry, the code must make displacements that are equivalent under the symmetries of the torus grid give bitwise identical overlaps.
  - Report the smallest decisive margin found in each part. If it is below $`100`$ times the estimated rounding error, report the affected pairs.
- **Random numbers** come from `numpy.random.default_rng(seed)`, with the seeds given below.
- **Ratios and angles.** For a pair at torus displacement $`\Delta`$ with $`r:=\lvert\Delta\rvert_T`$, the ratio is $`\varrho:=\ell_0/r`$. The folded angle $`\varphi\in[0,\pi/4]`$ is the angle of $`\Delta`$ reduced by the symmetries of the square (reflections in the axes and diagonals).

**T1. Code check on a periodic lattice** (tests (22.25)–(22.26)).
- **Setting.** $`L=32`$, places at all $`L^2`$ grid points, separable kernel.
- **Determine** $`N_0`$ and $`\ell_0`$.
- **Decision.** Pass iff both hold:
  - $`N_0`$ is exactly the 4-neighbour torus grid;
  - $`\max\bigl\lvert\ell_0-\rho\lVert\Delta\rVert_{1,T}\bigr\rvert\le10^{-9}\rho L`$ over all pairs, where $`\rho:=d_0`$ of a unit step and $`\lVert\Delta\rVert_{1,T}`$ is the minimal-image $`\ell^1`$ length.

**T1b. Periodic lattice, isotropic kernel** (reference; exploratory).
- **Setting.** $`L=32`$, places at all grid points, isotropic kernel.
- **Determine** the neighbour offsets of $`N_0`$ and $`B_{\rm per}`$. Here $`B_{\rm per}`$ is the ratio of the mean $`\varrho`$ over pairs with $`\varphi\in[3\pi/16,\pi/4]`$ to the mean $`\varrho`$ over pairs with $`\varphi\in[0,\pi/16]`$, for $`r\in[8,14]`$.

**T2. Random arrangements: isotropy.**
- **Setting.** Isotropic kernel. The places are a random subset of the grid points: each point is included independently with probability $`p=0.1`$.
  - Sizes $`L\in\{64,128\}`$.
  - Five realizations per size: seeds $`2301,\dots,2305`$ for $`L=64`$ and $`2311,\dots,2315`$ for $`L=128`$.
- **Determine** for each realization:
  - $`N_0`$ and $`\ell_0`$;
  - the mean degree and the maximum degree of $`N_0`$, and its number of connected components;
  - for the pairs with $`r\in[L/8,L/4]`$, the mean $`\varrho`$ in four bins of $`\varphi`$ of width $`\pi/16`$;
  - $`B:=`$ (mean $`\varrho`$ in the bin $`[3\pi/16,\pi/4]`$) / (mean $`\varrho`$ in the bin $`[0,\pi/16]`$).
- **Report** for each size the mean of $`B`$ over the five realizations and its standard error $`\mathrm{SE}`$ (sample standard deviation $`/\sqrt5`$).
- **Decision, at $`L=128`$.**
  - *Isotropy supported* iff $`\lvert\bar B-1\rvert<0.02`$ and $`\lvert\bar B-1\rvert<2\,\mathrm{SE}`$.
  - *Anisotropy detected* iff $`\bar B-1>0.02`$ and $`\bar B-1>3\,\mathrm{SE}`$.
  - *Inconclusive* otherwise.
  - Report $`\bar B`$ at $`L=64`$ as well; it is not part of the decision.

**T3. Robustness against a small non-local admixture.**
- **Setting.** The first $`L=128`$ realization of T2 (seed 2311). Each record vector is changed to $`u_h\to u_h+\varepsilon g_h`$, where the $`g_h`$ are independent standard Gaussian vectors on all $`L^2`$ cells, normalized to unit length (seed 2321). In operator form, $`K_h\to K_h+\varepsilon\sum_lg_{h,l}\sigma_x^{[l]}`$.
  - $`\varepsilon\in\{10^{-12},10^{-9},10^{-6},10^{-4},10^{-2}\}`$.
  - Norms are no longer equal. Use the exactness rule of the common setting, with $`d_0^2`$ split into its large constant and its small terms.
- **Determine** for each $`\varepsilon`$:
  - (a) the number of edges of $`N_0(\varepsilon)`$ that are not edges of $`N_0(0)`$;
  - (b) the number of **long edges**, i.e. edges with $`r>4/\sqrt p`$;
  - (c) the maximum degree;
  - (d) the mean $`\varrho`$ over pairs with $`r\in[16,32]`$, divided by its value at $`\varepsilon=0`$;
  - (e) (exploratory) the length of the shortest long edge.
- **Decision.**
  - *Fragile* iff for some $`\varepsilon\le10^{-4}`$, (b) $`>0`$ and $`\lvert(\mathrm d)-1\rvert>0.05`$.
  - *Robust* iff for all $`\varepsilon`$ (including $`10^{-2}`$), (b) $`=0`$ and $`\lvert(\mathrm d)-1\rvert<0.01`$.
  - *Intermediate* otherwise.

**T4. Continuous centres** (exploratory, no decision).
- **Setting.** $`L=128`$, isotropic kernel. The centres are the T2 places of seed 2311, each shifted by an independent uniform offset in $`[0,1)^2`$ (seed 2331). Kernel values use the shifted centres; the norms then differ.
- **Determine** quantities (b)–(d) of T3 for this arrangement, and the spread (max − min) of the norms $`S(h,h)`$.

## Inputs

From 04-neighbours@v1. Eq. (4.3), neighbours, for distinct points $`x,x'`$:

```math
x\sim x'\;:\Longleftrightarrow\;x\asymp x'\ \text{ and there is no } y\in X_V \text{ with } \max\bigl(\alpha(x,y),\alpha(y,x')\bigr)<\alpha(x,x') .
```

Eq. (4.6), the chain distance:

```math
\ell(x,x'):=\min\Bigl\{\sum_{j=0}^{m-1}\alpha(y_j,y_{j+1})\;:\;y_0=x,\ y_m=x',\ y_j\sim y_{j+1}\Bigr\},
\qquad \ell(x,x'):=+\infty\ \text{between components.}
```

From 05-recording-contract@v1, in the setting of 05. Eq. (5.10):

```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
```

From 22-large-scale-geometry@v3. Qubit-cell media with $`K_h=\sum_lk_{h,l}\sigma_x^{[l]}`$, $`k_{h,l}`$ real, $`\chi=\lvert0\cdots0\rangle`$; $`\lvert e_l\rangle`$ is the place with only bit $`l`$ set. Eq. (22.2):

```math
\cos\alpha(h,h';\lambda)=\prod_l\bigl\lvert\cos(\lambda\Delta_l)\bigr\rvert,\qquad \Delta_l:=k_{h,l}-k_{h',l},\qquad
\lvert u_h\rangle=\sum_lk_{h,l}\lvert e_l\rangle,\qquad d_0(h,h')^2=\sum_l\Delta_l^2 .
```

From Step 2 of 22, verbatim:
- "**(N1)** If some $`y`$ has $`\max\bigl(d_0(x,y),d_0(y,x')\bigr)<d_0(x,x')`$, then $`x\not\sim x'`$ for all small $`\lambda`$."
- "**(N2)** If every $`y\notin\{x,x'\}`$ has $`\max\bigl(d_0(x,y),d_0(y,x')\bigr)>d_0(x,x')`$, then $`x\sim x'`$ for all small $`\lambda`$."

$`N_0`$ is the resulting small-$`\lambda`$ graph. Eq. (22.4):

```math
\ell_0(x,x')=\min\Bigl\{\textstyle\sum_jd_0(y_j,y_{j+1}):\ y_0=x,\ y_m=x',\ y_j\sim y_{j+1}\text{ in }N_0\Bigr\}.
```

From 22, item 3(a): places $`h_p`$, $`p\in\{1,\dots,n\}^2`$, on an infinite square grid of cells, with $`K_{h_p}=\sum_lq^{\lvert l_1-p_1\rvert+\lvert l_2-p_2\rvert}\sigma_x^{[l]}`$, $`0<q<1`$. Eq. (22.25):

```math
N_0=\text{square grid graph on }\{1,\dots,n\}^2 .
```

Eq. (22.26), with $`\rho`$ the $`d_0`$ of a unit step:

```math
\ell_0(h_p,h_{p'})=\rho\bigl(\lvert\Delta_1\rvert+\lvert\Delta_2\rvert\bigr).
```

Eq. (22.27):

```math
(X_n,\ell_0/n)\xrightarrow{\rm GH}\bigl([0,1]^2,\ \rho\lVert\cdot\rVert_1\bigr).
```

Eq. (22.29), under the assumptions (F1)–(F3) of 22 (a fixed periodic pattern on growing convex domains whose recomputed neighbour graphs are the induced subgraphs):

```math
\text{Periodic arrangements under (F1)--(F3): the rescaled }\ell_0\text{ never converges to an isotropic limit (polygonal stable norm).}
```

## Assumptions

- The common setting and the parts T1–T4 as specified. All contracts are independent of $`\lambda`$ (A5).
- Only the small-$`\lambda`$ quantities $`d_0`$, $`N_0`$, $`\ell_0`$ are computed; no evolution is needed.
- The torus replaces the infinite grid of 22. Torus effects are kept small by the distance windows ($`r\le L/4`$).

## Scope

- In scope: parts T1–T4, the reported numbers, the decisions, and a short discussion of what they mean for criterion 4.
- Out of scope:
  - finite $`\lambda`$;
  - other kernels, densities or sizes;
  - three dimensions;
  - analytic proofs of the observed behaviour;
  - any physical or spatial meaning beyond the definitions (M1, M4).

## Depth

- T1–T4: computation, with a short description of each script and its checks.
- Discussion: short argument. State what the decisions do and do not show.

## Expected result

- T1: a pass/fail decision.
- T1b: the neighbour offsets and one ratio.
- T2: per-realization and mean values with standard errors, and a decision.
- T3: a table over $`\varepsilon`$ and a decision.
- T4: a small table.
- Discussion: a few sentences.

Give every main result a tag $`(23.k)`$.

Consistency checks, at most three: for example T1 itself, the symmetry of $`N_0`$, and the connectivity of $`N_0`$.

## Code

Required: computation: parts T1–T4 exactly as specified. Scripts go in `code/v1/`, and outputs in `code/v1/output/`. Save outputs as compact summaries (JSON or CSV, each file below 100 kB): no full distance matrices, but every number used in the derivation. Record the runtime of each part.
