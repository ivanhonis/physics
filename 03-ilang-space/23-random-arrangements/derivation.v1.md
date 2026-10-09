# Random arrangements: isotropy and robustness of the small-λ chain geometry (precommitted numerical run)

- **Subproject:** 03-ilang-space
- **Package:** 23-random-arrangements
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-09

## Setup and assumptions

**Inputs (quoted in question.md).**
- (4.3): $`x\sim x'`$ iff no $`y`$ has $`\max(\alpha(x,y),\alpha(y,x'))<\alpha(x,x')`$. (4.6): the chain distance.
- (5.10): $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$.
- (22.2): for $`K_h=\sum_lk_{h,l}\sigma_x^{[l]}`$ and $`\chi=\lvert0\cdots0\rangle`$, $`\lvert u_h\rangle=\sum_lk_{h,l}\lvert e_l\rangle`$.
- (N1)/(N2) of 22: $`N_0`$ is the small-λ neighbour graph wherever they decide. (22.4): $`\ell_0`$.
- (22.25)–(22.26): grid graph and $`\ell_0=\rho\lVert\Delta\rVert_1`$ for the separable kernel. (22.29): periodic arrangements give a polygonal norm.

**Model.** This is the common setting of question.md: an $`L\times L`$ torus, $`k_{h,l}=\kappa(l-c_h)`$ with $`\xi=2`$, so that $`u_h(l)=\kappa(l-c_h)>0`$. $`N_0`$ is (4.3) applied to $`d_0`$, and a tie keeps the edge. $`\ell_0`$ is (22.4), $`\varrho=\ell_0/r`$, and $`\varphi`$ is the folded angle. Floating point is binary64 with unit roundoff $`u=2^{-53}`$.

**Conventions.** These realize what question.md leaves open. They were fixed before the run and not changed.
- **C1.** T2 places: grid point $`(l_1,l_2)`$ is a place iff `default_rng(seed).random((L,L))[l1,l2] < p`. Places are ordered row-major.
- **C2.** T3: $`g_h`$ is row $`h`$ of `default_rng(2321).standard_normal((n,L*L))`, in the order of C1, with cell index $`l_1L+l_2`$, divided by its norm.
- **C3.** T4: the offset of place $`h`$ is row $`h`$ of `default_rng(2331).random((n,2))`. $`r`$, $`\varphi`$ and "long" use the shifted centres. (d) is divided by T3's value at $`\varepsilon=0`$, i.e. by the same places unshifted.
- **C4.** Pairs are unordered pairs of distinct places. $`r`$-windows are closed. The $`\varphi`$-bins are $`[k\pi/16,(k+1)\pi/16)`$, with the last bin closed. Grid displacements never hit the inner bin boundaries, because $`\tan(k\pi/16)`$ is irrational for $`k=1,2,3`$.
- **C5.** An edge is long iff $`r^2>16/p=160`$. This is an exact integer test on the grid; for example, $`\Delta=(12,4)`$ is not long.

## Derivation

### Step 1. Exact overlaps on the grid

For grid centres, translation invariance on the torus gives
```math
S(h,h')=S(\Delta):=\sum_l\kappa(l)\,\kappa(l-\Delta),\qquad d_0^2=2S(0)-2S(\Delta)=D_2(\Delta):=\sum_l\bigl(\kappa(l)-\kappa(l-\Delta)\bigr)^2,\qquad \Delta=c_{h'}-c_h .
\qquad\text{(23.1)}
```
Both kernels depend on $`(\lvert v_1\rvert_T,\lvert v_2\rvert_T)`$ symmetrically, so they are invariant under the symmetry group $`D_4`$ of the torus grid. Substituting $`l\to gl`$ then gives $`S(g\Delta)=S(\Delta)`$.

The code evaluates every $`\kappa`$ value correctly rounded, from a 50-digit Decimal. $`S`$ and $`D_2`$ are tabulated once per canonical displacement $`0\le d_2\le d_1\le L/2`$, as `math.fsum` sums. Equivalent displacements read the same entry, so their overlaps are bitwise identical.

**Error bound.** Each positive term carries a relative error of at most $`3u`$, and fsum adds at most $`u`$. The relative error of every entry is therefore at most $`4u`$, even for the far pairs. Fifty-digit recomputation of 12 entries per table gives a largest relative error of $`1.09u`$.

**Why direct overlaps are needed.** At $`L=128`$ the smallest overlap is $`S_{\min}=1.06\times10^{-16}`$, against $`S(0)=6.507`$. This is below $`u\,S(0)`$, so $`d_0`$ computed as $`2S(0)-2S`$ would erase the far-pair information. All decisions below therefore compare $`S`$ directly (Step 2).

**Distinct values.** The isotropic tables have pairwise distinct values. The smallest relative gaps are $`1.5\times10^{-5}`$ ($`L=32`$), $`3.4\times10^{-7}`$ ($`L=64`$) and $`1.5\times10^{-8}`$ ($`L=128`$), all far above $`8u`$. The separable $`L=32`$ table has a single coincidence, $`S(15,1)=S(16,0)`$, and it is an exact identity:
- $`S_{\rm sep}(\Delta)=s(\Delta_1)s(\Delta_2)`$, with $`s(\delta)=\sum_{l\in\mathbb Z_{32}}q^{\lvert l\rvert_T+\lvert l-\delta\rvert_T}`$ and $`q=e^{-1/2}`$;
- counting the two arcs gives $`s(0)=(1+q^2)\frac{1-q^{32}}{1-q^2}`$, $`s(1)=2q\frac{1-q^{32}}{1-q^2}`$, $`s(15)=16q^{15}(1+q^2)`$ and $`s(16)=32q^{16}`$;
- hence $`s(15)s(1)=s(16)s(0)`$.

**Consequence.** On the grid, the computed order of two overlaps equals the exact order, and computed equality occurs exactly where the true values are equal.

### Step 2. Decision arithmetic without cancellation

Write
```math
d_0(h,h')^2=C+\sigma_{hh'}+w_h+w_{h'}+z_{hh'},\qquad \sigma_{hh'}:=-2S(h,h'),
\qquad\text{(23.2)}
```
where $`C`$ is common to all pairs, and $`w`$ (per place) and $`z`$ (per pair) are the small parts. For $`y\notin\{x,x'\}`$, the term $`C`$ and the shared place term cancel exactly:
```math
\begin{aligned}
T_1&:=d_0(x,y)^2-d_0(x,x')^2=(\sigma_{xy}-\sigma_{xx'})+\bigl[(w_y+z_{xy})-(w_{x'}+z_{xx'})\bigr],\\
T_2&:=d_0(y,x')^2-d_0(x,x')^2=(\sigma_{yx'}-\sigma_{xx'})+\bigl[(w_y+z_{yx'})-(w_x+z_{xx'})\bigr].
\end{aligned}
\qquad\text{(23.3)}
```
Since $`d_0\ge0`$, $`y`$ blocks $`\{x,x'\}`$ iff $`\max(T_1,T_2)<0`$. Hence
```math
\{x,x'\}\in N_0\iff m(x,x'):=\min_{y\ne x,x'}\max(T_1,T_2)\ \ge 0,\qquad \text{tie}\iff m=0 .
\qquad\text{(23.4)}
```
- **How the code evaluates (23.3).** Overlap parts are subtracted only from each other. Equal entries give exactly $`0`$, and IEEE subtraction has the exact sign. Small parts are combined only among themselves. Nearly equal large numbers are never subtracted.
- **Margin and its error.** The decisive margin is $`m`$. Its error estimate $`E_m`$ is taken at the minimizing $`y`$ from the input errors. A difference between identical table entries contributes zero error. Each graph reports the pair with the smallest $`\lvert m\rvert/E_m`$, and all pairs with $`\lvert m\rvert/E_m<100`$.
- **Equal norms** (T1, T1b, T2, and T3 at $`\varepsilon=0`$): $`C=2S(0)`$ and $`w=z=0`$. By Step 1, every decision is then exact and every tie is a true tie. Edge weights are $`\sqrt{D_2}`$.

**T3.** Expanding $`\lVert u_h-u_{h'}+\varepsilon(g_h-g_{h'})\rVert^2`$ with $`\lVert u_h\rVert^2=S(0)`$ gives
```math
C=2S(0)+2\varepsilon^2,\quad w_h=2\varepsilon a_h+\varepsilon^2(n_h-1),\quad z_{hh'}=-2\varepsilon(b_{hh'}+b_{h'h})-2\varepsilon^2G_{hh'} ,
\qquad\text{(23.5)}
```
with $`b_{hh'}=\langle u_h,g_{h'}\rangle`$, $`a_h=b_{hh}`$, $`G_{hh'}=\langle g_h,g_{h'}\rangle`$ and $`n_h=\lVert g_h\rVert^2`$.
- $`b`$ and $`G`$ are BLAS sums. Their error estimate is $`\sqrt{L^2}\,u\sum\lvert\text{terms}\rvert`$. On 326 entries recomputed with fsum, the observed errors are at most 0.020 (for $`b`$) and 0.0012 (for $`G`$) of this estimate.
- Edge weights: $`d_0^2=D_2(\Delta)+2\varepsilon(a_h+a_{h'}-b_{hh'}-b_{h'h})+\varepsilon^2(n_h+n_{h'}-2G_{hh'})`$.

**T4.**
```math
C=2S(0),\quad w_h=\nu_h:=S(h,h)-S(0),\quad z=0,\quad \sigma_{hh'}=-2\textstyle\sum_l\kappa(l-c_h)\kappa(l-c_{h'}) ,
\qquad\text{(23.6)}
```
- $`\nu_h`$ is a single correctly rounded sum of $`\{\kappa(l-c_h)^2\}\cup\{-\kappa(l)^2\}`$.
- The overlaps are BLAS sums of positive terms, so they carry a relative error. The estimate is $`177u`$ (kernel-argument rounding plus summation); the observed error is at most $`18.4u`$ on 326 samples.
- Edge weights are direct sums of squared differences.

### Step 3. Chain distance and statistics

$`\ell_0`$ is computed by Dijkstra on $`N_0`$ with weights $`d_0`$. $`N_0`$ is always connected. Take any edge $`\{x,x'\}`$ of a minimum spanning tree $`\mathcal T`$ of the complete $`d_0`$-weighted graph, and suppose some $`y`$ had $`\max(d_0(x,y),d_0(y,x'))<d_0(x,x')`$. Removing $`\{x,x'\}`$ splits $`\mathcal T`$ into two parts, and one of $`\{x,y\}`$, $`\{y,x'\}`$ would reconnect them more cheaply, which is a contradiction. Hence $`\mathcal T\subseteq N_0`$. $`\varrho`$ is averaged over unordered pairs in the stated window and $`\varphi`$-bins (C4).

### Step 4. T1: code check

Separable kernel, $`L=32`$, all 1024 grid points.
- $`N_0`$ is exactly the 4-neighbour torus grid: 2048 edges, every degree 4, no ties.
- $`\rho=1.0295557`$, and $`\max\lvert\ell_0-\rho\lVert\Delta\rVert_{1,T}\rvert=0`$ against the tolerance $`10^{-9}\rho L=3.29\times10^{-8}`$.
- The smallest margin ratio is $`1.35\times10^{14}`$.
```math
\text{T1: pass.}
\qquad\text{(23.7)}
```

### Step 5. T1b: periodic lattice, isotropic kernel

- The only edge offset class is $`(1,0)`$ (2048 edges). $`N_0`$ is again the 4-neighbour grid, with $`\rho=0.93555`$ and no ties.
- For $`r\in[8,14]`$, the bin means of $`\varrho`$ are 1.0111, 1.1633, 1.2658 and 1.3150. The smallest margin ratio is $`6.3\times10^{13}`$.
```math
N_0^{\rm per}=\text{4-neighbour grid},\qquad B_{\rm per}=1.3006 .
\qquad\text{(23.8)}
```

### Step 6. T2: random arrangements

Isotropic kernel, $`p=0.1`$. Columns: $`n`$ places, $`\lvert E\rvert`$ edges, mean and maximum degree, tie pairs, bin means of $`\varrho`$ for $`r\in[L/8,L/4]`$, and $`B`$.

| $`L`$ | seed | $`n`$ | $`\lvert E\rvert`$ | $`\bar k`$ | $`k_{\max}`$ | ties | $`\bar\varrho_1`$ | $`\bar\varrho_2`$ | $`\bar\varrho_3`$ | $`\bar\varrho_4`$ | $`B`$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 64 | 2301 | 411 | 588 | 2.8613 | 5 | 88 | 0.94273 | 0.94571 | 0.94687 | 0.94858 | 1.00621 |
| 64 | 2302 | 415 | 573 | 2.7614 | 4 | 79 | 0.97964 | 0.97789 | 0.97899 | 0.97900 | 0.99935 |
| 64 | 2303 | 479 | 682 | 2.8476 | 5 | 110 | 0.99084 | 0.98637 | 0.99239 | 0.99804 | 1.00726 |
| 64 | 2304 | 400 | 551 | 2.7550 | 5 | 67 | 0.96678 | 0.97340 | 0.96838 | 0.97618 | 1.00973 |
| 64 | 2305 | 429 | 606 | 2.8252 | 5 | 90 | 0.96013 | 0.96585 | 0.96966 | 0.96993 | 1.01020 |
| 128 | 2311 | 1629 | 2285 | 2.8054 | 5 | 316 | 0.92164 | 0.92143 | 0.92122 | 0.92180 | 1.00018 |
| 128 | 2312 | 1707 | 2430 | 2.8471 | 5 | 388 | 0.91800 | 0.91886 | 0.91995 | 0.92259 | 1.00500 |
| 128 | 2313 | 1655 | 2330 | 2.8157 | 5 | 344 | 0.93187 | 0.92910 | 0.92642 | 0.92538 | 0.99304 |
| 128 | 2314 | 1706 | 2388 | 2.7995 | 5 | 317 | 0.92223 | 0.92162 | 0.92276 | 0.92461 | 1.00258 |
| 128 | 2315 | 1624 | 2286 | 2.8153 | 5 | 333 | 0.92473 | 0.92240 | 0.92081 | 0.92186 | 0.99690 |

- Every $`N_0`$ has one component.
- The ties are exact $`D_4`$ ties (Step 1); by the stated rule they keep their edges.
- The smallest margin ratio is $`2.04\times10^{9}`$ at both sizes. No pair is below 100.
```math
\bar B_{64}=1.00655\pm0.00195,\qquad \bar B_{128}=0.99954\pm0.00211\ (\pm\,\mathrm{SE}),\qquad \text{decision at }L=128:\ \textit{isotropy supported}.
\qquad\text{(23.9)}
```
The rule applies because $`\lvert\bar B_{128}-1\rvert=0.00046`$ is below both $`0.02`$ and $`2\,\mathrm{SE}=0.0042`$.

### Step 7. T3: small non-local admixture (seed 2311, $`L=128`$)

| $`\varepsilon`$ | (a) new | removed (of which $`\varepsilon=0`$ tie pairs) | (b) long | (c) $`k_{\max}`$ | (d) | (e) shortest long edge: $`r`$ ($`d_0`$) | min ratio |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 (0) | 0 | 5 | 1 | – | $`2.04\times10^9`$ |
| $`10^{-12}`$ | 0 | 175 (175) | 0 | 4 | 1.041455 | – | $`2.04\times10^9`$ |
| $`10^{-9}`$ | 0 | 175 (175) | 0 | 4 | 1.041455 | – | $`2.04\times10^9`$ |
| $`10^{-6}`$ | 0 | 175 (175) | 0 | 4 | 1.041455 | – | $`2.04\times10^9`$ |
| $`10^{-4}`$ | 61 | 175 (175) | 61 | 5 | 1.023918 | 66.40 (3.6076) | $`8.6\times10^8`$ |
| $`10^{-2}`$ | 442 | 187 (175) | 430 | 9 | 0.824974 | 46.04 (3.6072) | $`1.2\times10^8`$ |

- At $`\varepsilon=0`$, T3 reproduces T2 seed 2311 exactly: 2285 edges, 316 ties, mean $`\varrho=0.921519`$.
- For $`\varepsilon\in\{10^{-12},10^{-9},10^{-6}\}`$ the edge set is identical (symmetric difference 0). The 316 exact ties are broken by the generic perturbation: 175 tie edges disappear and the rest stay. No further ties occur.
- Every graph is connected, and no margin ratio is below 100.
- **Fragile** fails: the only $`\varepsilon\le10^{-4}`$ with (b) $`>0`$ is $`10^{-4}`$, where $`\lvert`$(d)$`-1\rvert=0.024\le0.05`$.
- **Robust** fails: already at $`\varepsilon=10^{-12}`$, $`\lvert`$(d)$`-1\rvert=0.041\ge0.01`$.
```math
\text{T3 decision: }\textit{intermediate}.
\qquad\text{(23.10)}
```

### Step 8. T4: continuous centres (exploratory)

- The norms $`S(h,h)`$ range from 6.21924 to 6.49758, a spread of 0.27834. The unshifted value is $`S(0)=6.50724`$.
- (b) 4 long edges, with $`r`$ from 46.48 to 80.58 (median 63.38).
- (c) maximum degree 7.
- (d) mean $`\varrho=0.90617`$, which is 0.98335 times the T3 value at $`\varepsilon=0`$ and 0.94420 times the value at $`\varepsilon=10^{-12}`$.
- 2116 edges, one component, no ties. The smallest margin ratio is $`7.4\times10^7`$.
```math
\text{T4: spread}=0.278,\quad\text{(b)}=4,\quad\text{(c)}=7,\quad\text{(d)}=0.983 .
\qquad\text{(23.11)}
```

### Step 9. Discussion (criterion 4)

**What T2 shows.**
- For periodic arrangements of the isotropic kernel, $`N_0`$ is the grid graph and $`\ell_0`$ is $`\ell^1`$-like, with $`B_{\rm per}=1.30`$ (23.8), as (22.29) predicts.
- Random arrangements of the same kernel show no detectable direction dependence of $`\ell_0`$ at $`L=128`$. At $`L=128`$, each realization's four bin means also agree to within about 1%.
- Within this test, the anisotropy of 22 is therefore a property of periodicity, and the large-scale chain distance of random arrangements is compatible with a Euclidean norm.

**What T2 does not show.**
- It does not prove convergence to a Euclidean norm. The test uses one statistic in one window, two sizes, five realizations, one kernel and one density.
- At $`L=64`$, $`\bar B-1`$ exceeds $`2\,\mathrm{SE}`$, although it stays below 0.02.
- $`\bar\varrho`$ still depends on the window and size: about 0.92–0.99 at $`L=64`$ and about 0.92 at $`L=128`$.

**What T3 shows.**
- Grid arrangements are non-generic. Their $`N_0(0)`$ contains exact ties, which the tie rule keeps; (N1)/(N2) do not decide these pairs.
- An arbitrarily small generic perturbation resolves the ties. It changes $`\ell_0`$ by 4.1%, independently of $`\varepsilon`$ over six decades.
- Long edges appear only from $`\varepsilon=10^{-4}`$ on.
- The far-pair neighbour structure rests on overlaps down to $`10^{-16}S(0)`$. A non-local admixture whose overlaps exceed those of the potential blockers creates long edges, up to 430 of them with maximum degree 9 at $`\varepsilon=10^{-2}`$.
- Locality of $`N_0`$ is therefore conditional on the non-local part of the records being far below the far-pair overlaps.

**T4.** Continuous centres remove the ties but introduce norm differences of order 0.1. These dominate the far-pair comparisons in (23.3), yet T4 gives only 4 long edges.

## Result

- (23.7) T1 passes: $`N_0`$ is the 4-neighbour grid and $`\ell_0=\rho\lVert\Delta\rVert_{1,T}`$ exactly.
- (23.8) T1b: the only neighbour offsets are $`(\pm1,0)`$ and $`(0,\pm1)`$; $`B_{\rm per}=1.3006`$.
- (23.9) T2: $`\bar B_{64}=1.00655\pm0.00195`$ and $`\bar B_{128}=0.99954\pm0.00211`$. The decision at $`L=128`$ is *isotropy supported*.
- (23.10) T3 decision: *intermediate*.
  - At $`\varepsilon\le10^{-6}`$: no new or long edges, but 175 broken tie edges and (d) $`=1.0415`$.
  - At $`\varepsilon=10^{-4}`$: 61 long edges, (d) $`=1.0239`$.
  - At $`\varepsilon=10^{-2}`$: 430 long edges, (d) $`=0.8250`$.
- (23.11) T4: norm spread 0.278, 4 long edges, maximum degree 7, (d) $`=0.983`$.
- Every decision follows its precommitted rule. Every reported number is in `code/v1/output/`.

## Consistency checks

1. **T1 (code check):** passes (23.7). The neighbour graph, the weights and Dijkstra reproduce (22.25)–(22.26) with zero deviation.
2. **Symmetry of $`N_0`$:** each pair's decision is computed independently from both orientations. All 19 graphs (T1, T1b, 10×T2, 6×T3, T4) have 0 asymmetric decisions.
3. **Connectivity:** Step 3 requires $`N_0`$ to be connected. All 19 graphs have exactly one component, and no $`\varrho`$ is infinite.

## Open issues

- **Tie edges.** The grid ties (67–388 per graph in T2) lie where (N1)/(N2) do not decide. Their small-λ status, and hence $`\ell_0`$ at the 4% level, depends on the tie convention or on finite-λ corrections, which are out of scope.
- **Error estimates.** For the BLAS sums in T3 and T4 the error estimates are statistical models, checked on samples, not rigorous bounds. The grid overlaps (Step 1) are rigorously bounded.
- **Development note.** A first version of the decision routine added $`-2S`$ and the ε-terms before comparing. At $`\varepsilon=10^{-12}`$, the broken-tie pairs then fell below 100 times the error estimate, and their status was unreliable. The routine was replaced by the split comparison (23.3) that the common setting prescribes. No parameter, seed, window or rule was changed, and all reported numbers come from the final version.

## Code

All files are under `code/v1/`. Run from the project root with `.venv/Scripts/python.exe 03-ilang-space/23-random-arrangements/code/v1/arrangements.py [T1 T1b T2 T3 T4]`.

**`arrangements.py` (computation).** It implements Steps 1–3 and parts T1–T4:
- correctly rounded kernels and fsum overlap tables on canonical displacements, with distinctness and 50-digit checks;
- the margin routine (23.3)–(23.4) with error estimates and tie counts;
- Dijkstra $`\ell_0`$ and the window and bin statistics;
- the T3 splits (23.5) and T4 splits (23.6), each with sampled fsum validation.

T4 reads `output/T3.json` for its reference value.

**Outputs** (`code/v1/output/`, JSON, each below 25 kB), with runtimes:

| File | Content | Runtime |
|---|---|---|
| `T1.json` | T1 | 5.4 s |
| `T1b.json` | T1b | 5.3 s |
| `T2.json` | per-realization graphs, bins, $`B`$, $`\bar B`$, SE, decision | 146.2 s |
| `T3.json` | per-ε rows (a)–(e), removed and tie counts, margins | 256.1 s |
| `T4.json` | T4 | 54.9 s |

## Methods used

- relative neighbourhood graph (4.3) on the record metric $`d_0`$; Dijkstra shortest paths
- exact table arithmetic: correctly rounded kernel values, `math.fsum`, $`D_4`$-canonical displacements
- cancellation-free comparison by splitting $`d_0^2`$ into constant, overlap and small parts
- forward rounding-error estimates, validated against 50-digit and fsum recomputation
- minimum-spanning-tree argument for connectivity
- Monte Carlo over seeded realizations; mean and standard error
