# Random arrangements: isotropy and robustness of the small-λ chain geometry (precommitted numerical run)

- **Subproject:** 03-ilang-space
- **Package:** 23-random-arrangements
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-09

## Changes from previous version

Trigger: `verification.md` (external round 1, verdict "minor issues", I1–I5). Models, parameters, seeds, sizes, windows, tolerances and decision rules are unchanged. All other text is copied from v1.
- **Code.** `code/v2/arrangements.py` is v1 plus validation and reporting: the all-witness edge check, the smallest absolute margin, the $D_2$ check and per-part summaries. The decision routine and every computed quantity are unchanged. All parts were rerun. `code/v2/compare_v1.py` compares every number saved by v1 with v2: all 848 saved values are identical (0 differences; `output/compare_v1.json`). The graphs, edge counts, ratios, $B$ values and decisions therefore reproduce v1 exactly.
- **Step 1** (I3): the $4u$ bound is restricted to $S$. A difference-aware bound for $D_2$ (23.12) is added, with 50-digit validation.
- **Step 2** (I1, I2): edges are certified against every witness (23.13). The smallest absolute margin is reported separately from the smallest margin-to-error ratio.
- **Step 8a** (new; I1, I2): the margin audit of all 19 graphs.
- **Steps 6, 9, Open issues** (I4): the grid ties are exact at every λ (23.14). The finite-λ caveat is removed, and the sensitivity to changing the records is stated separately.
- **Step 9** (I5): the general locality condition is replaced by the observed facts.
- **Result, Code, Methods used:** updated accordingly.

## Response to verification

- **I1:** Accepted and fixed in Step 2 (23.13) and Step 8a. Every edge of T3 ($\varepsilon>0$) and T4 is checked against every witness. All 13157 edge decisions (11041 in T3, 2116 in T4) are certified, with $q\ge7.4\times10^7$. None is uncertified, and none has $q<100$. In the equal-norm cases the comparisons are exact table comparisons (Step 1), so they need no error allowance; the same check, run there as well, certifies every edge.
- **I2:** Accepted and fixed in Step 2 and Step 8a. Every graph reports the smallest nonzero $\lvert m\rvert$, with its pair and $E_m$, separately from the smallest $\lvert m\rvert/E_m$.
- **I3:** Accepted and fixed in Step 1. The $4u$ bound now covers only $S$. $D_2$ gets its own difference-aware bound (23.12), validated by 50-digit recomputation of 11 entries per table.
- **I4:** Accepted and fixed in Step 6 (23.14), Step 9 and Open issues. Each grid tie is a $D_4$ tie, and by (22.2) it is a tie of $\alpha$ at every λ. The tie pairs therefore have the small-λ status that the tie rule gives. No tie that is not a symmetry tie occurs, so no finite-λ caveat remains. The sensitivity to changing the records is stated separately.
- **I5:** Accepted and fixed in Step 9. The step now states the observed long edges and the *intermediate* decision for this realization and perturbation, and claims no general locality condition.

## Setup and assumptions

**Inputs (quoted in question.md).**
- (4.3): $x\sim x'$ iff no $y$ has $\max(\alpha(x,y),\alpha(y,x'))<\alpha(x,x')$. (4.6): the chain distance.
- (5.10): $d_0(h,h')=\lVert u_h-u_{h'}\rVert$.
- (22.2): for $K_h=\sum_lk_{h,l}\sigma_x^{[l]}$ and $\chi=\lvert0\cdots0\rangle$, $\lvert u_h\rangle=\sum_lk_{h,l}\lvert e_l\rangle$.
- (N1)/(N2) of 22: $N_0$ is the small-λ neighbour graph wherever they decide. (22.4): $\ell_0$.
- (22.25)–(22.26): grid graph and $\ell_0=\rho\lVert\Delta\rVert_1$ for the separable kernel. (22.29): periodic arrangements give a polygonal norm.

**Model.** This is the common setting of question.md: an $L\times L$ torus, $k_{h,l}=\kappa(l-c_h)$ with $\xi=2$, so that $u_h(l)=\kappa(l-c_h)>0$. $N_0$ is (4.3) applied to $d_0$, and a tie keeps the edge. $\ell_0$ is (22.4), $\varrho=\ell_0/r$, and $\varphi$ is the folded angle. Floating point is binary64 with unit roundoff $u=2^{-53}$.

**Conventions.** These realize what question.md leaves open. They were fixed before the run and not changed.
- **C1.** T2 places: grid point $(l_1,l_2)$ is a place iff `default_rng(seed).random((L,L))[l1,l2] < p`. Places are ordered row-major.
- **C2.** T3: $g_h$ is row $h$ of `default_rng(2321).standard_normal((n,L*L))`, in the order of C1, with cell index $l_1L+l_2$, divided by its norm.
- **C3.** T4: the offset of place $h$ is row $h$ of `default_rng(2331).random((n,2))`. $r$, $\varphi$ and "long" use the shifted centres. (d) is divided by T3's value at $\varepsilon=0$, i.e. by the same places unshifted.
- **C4.** Pairs are unordered pairs of distinct places. $r$-windows are closed. The $\varphi$-bins are $[k\pi/16,(k+1)\pi/16)$, with the last bin closed. Grid displacements never hit the inner bin boundaries, because $\tan(k\pi/16)$ is irrational for $k=1,2,3$.
- **C5.** An edge is long iff $r^2>16/p=160$. This is an exact integer test on the grid; for example, $\Delta=(12,4)$ is not long.

## Derivation

### Step 1. Exact overlaps on the grid

For grid centres, translation invariance on the torus gives
$$
S(h,h')=S(\Delta):=\sum_l\kappa(l)\,\kappa(l-\Delta),\qquad d_0^2=2S(0)-2S(\Delta)=D_2(\Delta):=\sum_l\bigl(\kappa(l)-\kappa(l-\Delta)\bigr)^2,\qquad \Delta=c_{h'}-c_h .
\tag{23.1}
$$
Both kernels depend on $(\lvert v_1\rvert_T,\lvert v_2\rvert_T)$ symmetrically, so they are invariant under the symmetry group $D_4$ of the torus grid. Substituting $l\to gl$ then gives $S(g\Delta)=S(\Delta)$.

The code evaluates every $\kappa$ value correctly rounded, from a 50-digit Decimal. $S$ and $D_2$ are tabulated once per canonical displacement $0\le d_2\le d_1\le L/2$, as `math.fsum` sums. Equivalent displacements read the same entry, so their overlaps are bitwise identical.

**Error bound.** Each positive term of $S$ carries a relative error of at most $3u$, and fsum adds at most $u$. The relative error of every $S$ entry is therefore at most $4u$, even for the far pairs. Fifty-digit recomputation of 12 entries per table gives a largest relative error of $1.09u$.

**Error bound for $D_2$.** The $4u$ bound does not apply to $D_2$, because the differences amplify input rounding. Write $a=\kappa(l)$, $b=\kappa(l-\Delta)$.
- The correctly rounded inputs and the subtraction give the difference with an error of at most $u(a+b)+u\lvert a-b\rvert$.
- The squared term then has an error of at most $2u\lvert a-b\rvert(a+b)+3u(a-b)^2$, to first order in $u$. fsum adds $uD_2$.
- Cauchy–Schwarz gives $\sum_l\lvert a-b\rvert(a+b)\le\sqrt{D_2}\,\sqrt{2S(0)+2S(\Delta)}$.

Together:
$$
\frac{\lvert\hat D_2(\Delta)-D_2(\Delta)\rvert}{D_2(\Delta)}\le2u\sqrt{\frac{2S(0)+2S(\Delta)}{D_2(\Delta)}}+4u\qquad(\Delta\ne0),\qquad \hat D_2(0)=D_2(0)=0 .
\tag{23.12}
$$
Over all tables, (23.12) is at most $14.72u$ (isotropic) and $12.17u$ (separable). Fifty-digit recomputation of 11 entries per table ($\Delta\ne0$) gives a largest relative error of $0.96u$, at most 0.16 of (23.12). The edge weights $\sqrt{D_2}$ therefore carry a relative error below $9u$.

**Why direct overlaps are needed.** At $L=128$ the smallest overlap is $S_{\min}=1.06\times10^{-16}$, against $S(0)=6.507$. This is below $u\,S(0)$, so $d_0$ computed as $2S(0)-2S$ would erase the far-pair information. All decisions below therefore compare $S$ directly (Step 2).

**Distinct values.** The isotropic tables have pairwise distinct values. The smallest relative gaps are $1.5\times10^{-5}$ ($L=32$), $3.4\times10^{-7}$ ($L=64$) and $1.5\times10^{-8}$ ($L=128$), all far above $8u$. The separable $L=32$ table has a single coincidence, $S(15,1)=S(16,0)$, and it is an exact identity:
- $S_{\rm sep}(\Delta)=s(\Delta_1)s(\Delta_2)$, with $s(\delta)=\sum_{l\in\mathbb Z_{32}}q^{\lvert l\rvert_T+\lvert l-\delta\rvert_T}$ and $q=e^{-1/2}$;
- counting the two arcs gives $s(0)=(1+q^2)\frac{1-q^{32}}{1-q^2}$, $s(1)=2q\frac{1-q^{32}}{1-q^2}$, $s(15)=16q^{15}(1+q^2)$ and $s(16)=32q^{16}$;
- hence $s(15)s(1)=s(16)s(0)$.

**Consequence.** On the grid, the computed order of two overlaps equals the exact order, and computed equality occurs exactly where the true values are equal.

### Step 2. Decision arithmetic without cancellation

Write
$$
d_0(h,h')^2=C+\sigma_{hh'}+w_h+w_{h'}+z_{hh'},\qquad \sigma_{hh'}:=-2S(h,h'),
\tag{23.2}
$$
where $C$ is common to all pairs, and $w$ (per place) and $z$ (per pair) are the small parts. For $y\notin\{x,x'\}$, the term $C$ and the shared place term cancel exactly:
$$
\begin{aligned}
T_1&:=d_0(x,y)^2-d_0(x,x')^2=(\sigma_{xy}-\sigma_{xx'})+\bigl[(w_y+z_{xy})-(w_{x'}+z_{xx'})\bigr],\\
T_2&:=d_0(y,x')^2-d_0(x,x')^2=(\sigma_{yx'}-\sigma_{xx'})+\bigl[(w_y+z_{yx'})-(w_x+z_{xx'})\bigr].
\end{aligned}
\tag{23.3}
$$
Since $d_0\ge0$, $y$ blocks $\{x,x'\}$ iff $\max(T_1,T_2)<0$. Hence
$$
\{x,x'\}\in N_0\iff m(x,x'):=\min_{y\ne x,x'}\max(T_1,T_2)\ \ge 0,\qquad \text{tie}\iff m=0 .
\tag{23.4}
$$
- **How the code evaluates (23.3).** Overlap parts are subtracted only from each other. Equal entries give exactly $0$, and IEEE subtraction has the exact sign. Small parts are combined only among themselves. Nearly equal large numbers are never subtracted.
- **Margin and its error.** The decisive margin is $m$. Its error estimate $E_m$ is taken at the minimizing $y$ from the input errors. A difference between identical table entries contributes zero error. Each graph reports the pair with the smallest $\lvert m\rvert/E_m$, and all pairs with $\lvert m\rvert/E_m<100$. Separately, it reports the pair with the smallest nonzero $\lvert m\rvert$, with its $E_m$.
- **Certification of non-edges.** A non-edge ($m<0$) with $\lvert m\rvert>E_m$ is certified by its minimizing witness: then $T_1<0$ and $T_2<0$ hold for the exact values.
- **Certification of edges.** An edge needs every witness. Let $E_1,E_2$ be the error estimates of $T_1,T_2$ for each $y$, from the same input-error model as $E_m$. Define
$$
q(x,x'):=\min_{y\ne x,x'}\max\Bigl(\frac{T_1}{E_1},\frac{T_2}{E_2}\Bigr),\qquad \{x,x'\}\in N_0\ \text{certified}\iff q(x,x')\ge1 .
\tag{23.13}
$$
  - If $q\ge1$, every $y$ has $T_1\ge E_1$ or $T_2\ge E_2$, so no $y$ blocks the exact pair.
  - $E=0$ occurs only for identical table entries. There $T=0$ exactly, and the condition counts as satisfied.
  - The code recomputes $T_1,T_2$ for every witness with the same operations as the decision routine. It checks that their minimax reproduces $m$ bitwise.
- **Equal norms** (T1, T1b, T2, and T3 at $\varepsilon=0$): $C=2S(0)$ and $w=z=0$. By Step 1, every decision is then exact and every tie is a true tie. Edge weights are $\sqrt{D_2}$. The comparisons are exact table comparisons, so these decisions need no error allowance. (23.13) is run there only as a check.

**T3.** Expanding $\lVert u_h-u_{h'}+\varepsilon(g_h-g_{h'})\rVert^2$ with $\lVert u_h\rVert^2=S(0)$ gives
$$
C=2S(0)+2\varepsilon^2,\quad w_h=2\varepsilon a_h+\varepsilon^2(n_h-1),\quad z_{hh'}=-2\varepsilon(b_{hh'}+b_{h'h})-2\varepsilon^2G_{hh'} ,
\tag{23.5}
$$
with $b_{hh'}=\langle u_h,g_{h'}\rangle$, $a_h=b_{hh}$, $G_{hh'}=\langle g_h,g_{h'}\rangle$ and $n_h=\lVert g_h\rVert^2$.
- $b$ and $G$ are BLAS sums. Their error estimate is $\sqrt{L^2}\,u\sum\lvert\text{terms}\rvert$. On 326 entries recomputed with fsum, the observed errors are at most 0.020 (for $b$) and 0.0012 (for $G$) of this estimate.
- Edge weights: $d_0^2=D_2(\Delta)+2\varepsilon(a_h+a_{h'}-b_{hh'}-b_{h'h})+\varepsilon^2(n_h+n_{h'}-2G_{hh'})$.

**T4.**
$$
C=2S(0),\quad w_h=\nu_h:=S(h,h)-S(0),\quad z=0,\quad \sigma_{hh'}=-2\textstyle\sum_l\kappa(l-c_h)\kappa(l-c_{h'}) ,
\tag{23.6}
$$
- $\nu_h$ is a single correctly rounded sum of $\{\kappa(l-c_h)^2\}\cup\{-\kappa(l)^2\}$.
- The overlaps are BLAS sums of positive terms, so they carry a relative error. The estimate is $177u$ (kernel-argument rounding plus summation); the observed error is at most $18.4u$ on 326 samples.
- Edge weights are direct sums of squared differences.

### Step 3. Chain distance and statistics

$\ell_0$ is computed by Dijkstra on $N_0$ with weights $d_0$. $N_0$ is always connected. Take any edge $\{x,x'\}$ of a minimum spanning tree $\mathcal T$ of the complete $d_0$-weighted graph, and suppose some $y$ had $\max(d_0(x,y),d_0(y,x'))<d_0(x,x')$. Removing $\{x,x'\}$ splits $\mathcal T$ into two parts, and one of $\{x,y\}$, $\{y,x'\}$ would reconnect them more cheaply, which is a contradiction. Hence $\mathcal T\subseteq N_0$. $\varrho$ is averaged over unordered pairs in the stated window and $\varphi$-bins (C4).

### Step 4. T1: code check

Separable kernel, $L=32$, all 1024 grid points.
- $N_0$ is exactly the 4-neighbour torus grid: 2048 edges, every degree 4, no ties.
- $\rho=1.0295557$, and $\max\lvert\ell_0-\rho\lVert\Delta\rVert_{1,T}\rvert=0$ against the tolerance $10^{-9}\rho L=3.29\times10^{-8}$.
- The smallest margin ratio is $1.35\times10^{14}$.
$$
\text{T1: pass.}
\tag{23.7}
$$

### Step 5. T1b: periodic lattice, isotropic kernel

- The only edge offset class is $(1,0)$ (2048 edges). $N_0$ is again the 4-neighbour grid, with $\rho=0.93555$ and no ties.
- For $r\in[8,14]$, the bin means of $\varrho$ are 1.0111, 1.1633, 1.2658 and 1.3150. The smallest margin ratio is $6.3\times10^{13}$.
$$
N_0^{\rm per}=\text{4-neighbour grid},\qquad B_{\rm per}=1.3006 .
\tag{23.8}
$$

### Step 6. T2: random arrangements

Isotropic kernel, $p=0.1$. Columns: $n$ places, $\lvert E\rvert$ edges, mean and maximum degree, tie pairs, bin means of $\varrho$ for $r\in[L/8,L/4]$, and $B$.

| $L$ | seed | $n$ | $\lvert E\rvert$ | $\bar k$ | $k_{\max}$ | ties | $\bar\varrho_1$ | $\bar\varrho_2$ | $\bar\varrho_3$ | $\bar\varrho_4$ | $B$ |
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

- Every $N_0$ has one component.
- The ties are exact $D_4$ ties (Step 1); by the stated rule they keep their edges. They are ties of $\alpha$ at every λ (23.14), so this is also their small-λ status.
- The smallest margin ratio is $2.04\times10^{9}$ at both sizes. No pair is below 100.
$$
\bar B_{64}=1.00655\pm0.00195,\qquad \bar B_{128}=0.99954\pm0.00211\ (\pm\,\mathrm{SE}),\qquad \text{decision at }L=128:\ \textit{isotropy supported}.
\tag{23.9}
$$
The rule applies because $\lvert\bar B_{128}-1\rvert=0.00046$ is below both $0.02$ and $2\,\mathrm{SE}=0.0042$.

**Symmetry ties at every λ.** By (22.2), $\cos\alpha(h,h';\lambda)=\prod_l\lvert\cos\lambda(\kappa(l-c_h)-\kappa(l-c_{h'}))\rvert$. Substitute $l=c_h+gm$ with $g\in D_4$, and use $\kappa(gv)=\kappa(v)$. The factors become those of the displacement $g^{-1}\Delta$, in permuted order. Hence, for grid centres,
$$
\alpha(h,h';\lambda)=A([\Delta];\lambda)\quad\text{for every }\lambda,\qquad [\Delta]:=\text{the }D_4\text{ class of }\Delta=c_{h'}-c_h .
\tag{23.14}
$$
- The isotropic tables have pairwise distinct values (Step 1). So every tie of T2 (and of T3 at $\varepsilon=0$) is a $D_4$ tie, and by (23.14) it is a tie of $\alpha$ at every λ.
- Such a tie witness $y$ has $\alpha(x,y)=\alpha(x,x')$ or $\alpha(y,x')=\alpha(x,x')$ at every λ. It therefore never blocks under the strict rule (4.3).
- Every other comparison of the pair is strict in $d_0$. Since $\alpha/\lambda\to d_0$ (5.10), these finitely many strict inequalities persist for small λ.
- Hence the tie rule gives the small-λ graph also for the tie pairs.

### Step 7. T3: small non-local admixture (seed 2311, $L=128$)

| $\varepsilon$ | (a) new | removed (of which $\varepsilon=0$ tie pairs) | (b) long | (c) $k_{\max}$ | (d) | (e) shortest long edge: $r$ ($d_0$) | min ratio |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 (0) | 0 | 5 | 1 | – | $2.04\times10^9$ |
| $10^{-12}$ | 0 | 175 (175) | 0 | 4 | 1.041455 | – | $2.04\times10^9$ |
| $10^{-9}$ | 0 | 175 (175) | 0 | 4 | 1.041455 | – | $2.04\times10^9$ |
| $10^{-6}$ | 0 | 175 (175) | 0 | 4 | 1.041455 | – | $2.04\times10^9$ |
| $10^{-4}$ | 61 | 175 (175) | 61 | 5 | 1.023918 | 66.40 (3.6076) | $8.6\times10^8$ |
| $10^{-2}$ | 442 | 187 (175) | 430 | 9 | 0.824974 | 46.04 (3.6072) | $1.2\times10^8$ |

- At $\varepsilon=0$, T3 reproduces T2 seed 2311 exactly: 2285 edges, 316 ties, mean $\varrho=0.921519$.
- For $\varepsilon\in\{10^{-12},10^{-9},10^{-6}\}$ the edge set is identical (symmetric difference 0). The 316 exact ties are broken by the generic perturbation: 175 tie edges disappear and the rest stay. No further ties occur.
- Every graph is connected, and no margin ratio is below 100.
- **Fragile** fails: the only $\varepsilon\le10^{-4}$ with (b) $>0$ is $10^{-4}$, where $\lvert$(d)$-1\rvert=0.024\le0.05$.
- **Robust** fails: already at $\varepsilon=10^{-12}$, $\lvert$(d)$-1\rvert=0.041\ge0.01$.
$$
\text{T3 decision: }\textit{intermediate}.
\tag{23.10}
$$

### Step 8. T4: continuous centres (exploratory)

- The norms $S(h,h)$ range from 6.21924 to 6.49758, a spread of 0.27834. The unshifted value is $S(0)=6.50724$.
- (b) 4 long edges, with $r$ from 46.48 to 80.58 (median 63.38).
- (c) maximum degree 7.
- (d) mean $\varrho=0.90617$, which is 0.98335 times the T3 value at $\varepsilon=0$ and 0.94420 times the value at $\varepsilon=10^{-12}$.
- 2116 edges, one component, no ties. The smallest margin ratio is $7.4\times10^7$.
$$
\text{T4: spread}=0.278,\quad\text{(b)}=4,\quad\text{(c)}=7,\quad\text{(d)}=0.983 .
\tag{23.11}
$$

### Step 8a. Margin audit

For every graph, the table lists:
- the smallest nonzero $\lvert m\rvert$, with its pair (centres $c_i$–$c_j$, E = edge, N = non-edge) and its $E_m$;
- the smallest $\lvert m\rvert/E_m$;
- the edges certified by (23.13), and the smallest $q$.

| graph | smallest $\lvert m\rvert$ | pair | $E_m$ | min $\lvert m\rvert/E_m$ | certified edges | min $q$ |
|---|---|---|---|---|---|---|
| T1 | 0.0691 | (0,0)–(15,16) N | $3.1\times10^{-17}$ | $1.35\times10^{14}$ | 2048/2048 | $3.9\times10^{14}$ |
| T1b | 0.490 | (0,0)–(15,16) N | $2.3\times10^{-16}$ | $6.3\times10^{13}$ | 2048/2048 | $2.3\times10^{14}$ |
| T2, 2301 | $3.66\times10^{-5}$ | (9,5)–(9,10) E | $4.3\times10^{-15}$ | $8.56\times10^{9}$ | 588/588 | $8.56\times10^{9}$ |
| T2, 2302 | $3.66\times10^{-5}$ | (8,43)–(11,47) N | $4.3\times10^{-15}$ | $8.56\times10^{9}$ | 573/573 | $8.56\times10^{9}$ |
| T2, 2303 | $3.11\times10^{-6}$ | (26,62)–(34,61) E | $1.5\times10^{-15}$ | $2.04\times10^{9}$ | 682/682 | $2.04\times10^{9}$ |
| T2, 2304 | $3.66\times10^{-5}$ | (1,28)–(60,28) E | $4.3\times10^{-15}$ | $8.56\times10^{9}$ | 551/551 | $8.56\times10^{9}$ |
| T2, 2305 | $3.66\times10^{-5}$ | (9,63)–(14,63) E | $4.3\times10^{-15}$ | $8.56\times10^{9}$ | 606/606 | $8.56\times10^{9}$ |
| T2, 2311 | $9.61\times10^{-8}$ | (45,57)–(109,122) N | $4.3\times10^{-23}$ | $2.04\times10^{9}$ | 2285/2285 | $2.04\times10^{9}$ |
| T2, 2312 | $9.81\times10^{-8}$ | (50,98)–(113,33) N | $4.4\times10^{-23}$ | $3.70\times10^{9}$ | 2430/2430 | $3.70\times10^{9}$ |
| T2, 2313 | $9.61\times10^{-8}$ | (13,12)–(76,76) N | $4.3\times10^{-23}$ | $3.70\times10^{9}$ | 2330/2330 | $8.56\times10^{9}$ |
| T2, 2314 | $9.61\times10^{-8}$ | (57,13)–(121,78) N | $4.3\times10^{-23}$ | $8.56\times10^{9}$ | 2388/2388 | $8.56\times10^{9}$ |
| T2, 2315 | $9.46\times10^{-8}$ | (13,30)–(78,94) N | $4.2\times10^{-23}$ | $3.70\times10^{9}$ | 2286/2286 | $3.70\times10^{9}$ |
| T3, $\varepsilon=0$ | $9.61\times10^{-8}$ | (45,57)–(109,122) N | $4.3\times10^{-23}$ | $2.04\times10^{9}$ | 2285/2285 | $2.04\times10^{9}$ |
| T3, $10^{-12}$ | $6.93\times10^{-16}$ | (80,92)–(82,91) N | $2.6\times10^{-26}$ | $2.04\times10^{9}$ | 2110/2110 | $2.04\times10^{9}$ |
| T3, $10^{-9}$ | $6.93\times10^{-13}$ | (80,92)–(82,91) N | $2.6\times10^{-23}$ | $2.04\times10^{9}$ | 2110/2110 | $2.04\times10^{9}$ |
| T3, $10^{-6}$ | $6.93\times10^{-10}$ | (80,92)–(82,91) N | $2.6\times10^{-20}$ | $2.04\times10^{9}$ | 2110/2110 | $2.04\times10^{9}$ |
| T3, $10^{-4}$ | $2.47\times10^{-9}$ | (47,2)–(121,76) E | $2.9\times10^{-18}$ | $8.6\times10^{8}$ | 2171/2171 | $8.6\times10^{8}$ |
| T3, $10^{-2}$ | $3.50\times10^{-8}$ | (66,3)–(124,44) N | $2.9\times10^{-16}$ | $1.2\times10^{8}$ | 2540/2540 | $1.2\times10^{8}$ |
| T4 | $5.35\times10^{-6}$ | (49.50,56.51)–(66.52,11.48) N | $7.2\times10^{-14}$ | $7.4\times10^{7}$ | 2116/2116 | $7.4\times10^{7}$ |

- **Edges.** All 13157 edges of T3 ($\varepsilon>0$) and T4 are certified against every witness. None has $q<100$; the smallest $q$ is $1.2\times10^8$ in T3 and $7.4\times10^7$ in T4. The equal-norm graphs are exact (Step 2); the check confirms every edge there as well.
- **Non-edges.** Every non-edge of all 19 graphs is certified by its minimizing witness.
- **Consistency of the check.** In every graph, the recomputed witnesses reproduce $m$ bitwise.
- **Smallest decisive margin per part:** 0.0691 (T1), 0.490 (T1b), $9.46\times10^{-8}$ (T2), $6.93\times10^{-16}$ (T3, $\varepsilon=10^{-12}$) and $5.35\times10^{-6}$ (T4). Each is at least $7.4\times10^7$ times its error estimate, so no pair is reported as affected.
- In T3 at $\varepsilon\le10^{-6}$, the smallest margins are proportional to $\varepsilon$, so their overlap part is exactly zero: the decisive witness compares identical table entries (a broken $D_4$ tie). Their ratio stays at $2.6\times10^{10}$.

### Step 9. Discussion (criterion 4)

**What T2 shows.**
- For periodic arrangements of the isotropic kernel, $N_0$ is the grid graph and $\ell_0$ is $\ell^1$-like, with $B_{\rm per}=1.30$ (23.8), as (22.29) predicts.
- Random arrangements of the same kernel show no detectable direction dependence of $\ell_0$ at $L=128$. At $L=128$, each realization's four bin means also agree to within about 1%.
- Within this test, the anisotropy of 22 is therefore a property of periodicity, and the large-scale chain distance of random arrangements is compatible with a Euclidean norm.

**What T2 does not show.**
- It does not prove convergence to a Euclidean norm. The test uses one statistic in one window, two sizes, five realizations, one kernel and one density.
- At $L=64$, $\bar B-1$ exceeds $2\,\mathrm{SE}$, although it stays below 0.02.
- $\bar\varrho$ still depends on the window and size: about 0.92–0.99 at $L=64$ and about 0.92 at $L=128$.

**What T3 shows.**
- Grid arrangements are non-generic. Their $N_0(0)$ contains exact ties, which the tie rule keeps. (N1)/(N2) do not decide these pairs. They are, however, $D_4$ ties, exact at every λ (23.14), so the tie edges are edges for all small λ. No other ties occur in any part.
- An arbitrarily small generic perturbation of the records resolves the ties. It changes $\ell_0$ by 4.1%, independently of $\varepsilon$ over six decades. This is a sensitivity of $N_0$ to changing the records, not an ambiguity of the small-λ limit.
- Long edges appear only from $\varepsilon=10^{-4}$ on: 61 at $\varepsilon=10^{-4}$, and 430 with maximum degree 9 at $\varepsilon=10^{-2}$.
- The run classifies this realization under this perturbation as *intermediate* (23.10). It does not give a general condition for the locality of $N_0$. By (23.3), a witness margin depends on overlap and norm changes together, and the run tests no size condition on the admixture as necessary or sufficient.

**T4.** Continuous centres remove the ties but introduce norm differences of order 0.1. These dominate the far-pair comparisons in (23.3), yet T4 gives only 4 long edges.

## Result

- (23.7) T1 passes: $N_0$ is the 4-neighbour grid and $\ell_0=\rho\lVert\Delta\rVert_{1,T}$ exactly.
- (23.8) T1b: the only neighbour offsets are $(\pm1,0)$ and $(0,\pm1)$; $B_{\rm per}=1.3006$.
- (23.9) T2: $\bar B_{64}=1.00655\pm0.00195$ and $\bar B_{128}=0.99954\pm0.00211$. The decision at $L=128$ is *isotropy supported*.
- (23.10) T3 decision: *intermediate*.
  - At $\varepsilon\le10^{-6}$: no new or long edges, but 175 broken tie edges and (d) $=1.0415$.
  - At $\varepsilon=10^{-4}$: 61 long edges, (d) $=1.0239$.
  - At $\varepsilon=10^{-2}$: 430 long edges, (d) $=0.8250$.
- (23.11) T4: norm spread 0.278, 4 long edges, maximum degree 7, (d) $=0.983$.
- (23.12) The $D_2$ table entries have a relative error of at most $14.72u$, validated by 50-digit recomputation.
- (23.13) Every edge of T3 ($\varepsilon>0$) and T4 (13157 in all) is certified against every witness, with $q\ge7.4\times10^7$. The equal-norm decisions are exact table comparisons. Every non-edge is certified by its minimizing witness. The smallest nonzero margins are 0.0691 (T1), 0.490 (T1b), $9.46\times10^{-8}$ (T2), $6.93\times10^{-16}$ (T3) and $5.35\times10^{-6}$ (T4). Each is at least $7.4\times10^7$ times its error estimate.
- (23.14) For grid centres, $\alpha(h,h';\lambda)$ depends only on the $D_4$ class of the displacement. All grid ties are such symmetry ties, so the tie edges are small-λ edges.
- Every decision follows its precommitted rule. Every reported number is in `code/v2/output/`. v2 reproduces every number saved by v1 exactly.

## Consistency checks

1. **T1 (code check):** passes (23.7). The neighbour graph, the weights and Dijkstra reproduce (22.25)–(22.26) with zero deviation.
2. **Symmetry of $N_0$:** each pair's decision is computed independently from both orientations. All 19 graphs (T1, T1b, 10×T2, 6×T3, T4) have 0 asymmetric decisions.
3. **Connectivity:** Step 3 requires $N_0$ to be connected. All 19 graphs have exactly one component, and no $\varrho$ is infinite.

## Open issues

- **Tie edges.** The grid ties (67–388 per graph in T2) lie where (N1)/(N2) do not decide. They are $D_4$ ties, exact at every λ (23.14), so their small-λ status is fixed: they are edges. No tie that is not a symmetry tie occurs in any part, so no tie-convention or finite-λ caveat remains.
- **Sensitivity to the records.** Separately, $N_0$ of the grid arrangement is sensitive to changes of the records. In T3, every $\varepsilon>0$ removes 175 tie edges, and already $\varepsilon=10^{-12}$ changes $\ell_0$ by 4.1% (Step 7). Which records a description uses is not decided here.
- **Error estimates.** For the BLAS sums in T3 and T4 the error estimates are statistical models, checked on samples, not rigorous bounds. The grid overlaps and $D_2$ entries (Step 1, (23.12)) are rigorously bounded.
- **Development note.** A first version of the decision routine added $-2S$ and the ε-terms before comparing. At $\varepsilon=10^{-12}$, the broken-tie pairs then fell below 100 times the error estimate, and their status was unreliable. The routine was replaced by the split comparison (23.3) that the common setting prescribes. No parameter, seed, window or rule was changed, and all reported numbers come from the final version.

## Code

All files are under `code/v2/`. Run from the project root with `.venv/Scripts/python.exe 03-ilang-space/23-random-arrangements/code/v2/arrangements.py [T1 T1b T2 T3 T4]`, then `.venv/Scripts/python.exe 03-ilang-space/23-random-arrangements/code/v2/compare_v1.py`.

**`arrangements.py` (computation).** It is `code/v1/arrangements.py` with added validation and reporting. It implements Steps 1–3 and parts T1–T4:
- correctly rounded kernels and fsum overlap tables on canonical displacements, with distinctness and 50-digit checks of $S$ and, new in v2, of $D_2$ against (23.12);
- the margin routine (23.3)–(23.4) with error estimates and tie counts; new in v2, the all-witness edge check (23.13), the smallest absolute margin, and per-part summaries (`margin_audit`);
- Dijkstra $\ell_0$ and the window and bin statistics;
- the T3 splits (23.5) and T4 splits (23.6), each with sampled fsum validation.

T4 reads `output/T3.json` for its reference value.

**`compare_v1.py` (check).** It compares every number saved in `code/v1/output/` with the same entry in `code/v2/output/`, by exact equality and without runtimes. Output: `compare_v1.json`.

**Outputs** (`code/v2/output/`, JSON, each below 25 kB), with runtimes:

| File | Content | Runtime |
|---|---|---|
| `T1.json` | T1 | 6.3 s |
| `T1b.json` | T1b | 6.4 s |
| `T2.json` | per-realization graphs, bins, $B$, $\bar B$, SE, decision, margin audit | 147.1 s |
| `T3.json` | per-ε rows (a)–(e), removed and tie counts, margins, margin audit | 279.0 s |
| `T4.json` | T4 | 57.8 s |
| `compare_v1.json` | comparison with v1 | – |

## Methods used

- relative neighbourhood graph (4.3) on the record metric $d_0$; Dijkstra shortest paths
- exact table arithmetic: correctly rounded kernel values, `math.fsum`, $D_4$-canonical displacements
- cancellation-free comparison by splitting $d_0^2$ into constant, overlap and small parts
- forward rounding-error estimates, validated against 50-digit and fsum recomputation; Cauchy–Schwarz bound for squared differences
- all-witness certification of neighbour decisions
- $D_4$ invariance of the product formula (22.2)
- minimum-spanning-tree argument for connectivity
- Monte Carlo over seeded realizations; mean and standard error
