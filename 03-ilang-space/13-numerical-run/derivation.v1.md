# Numerical run of the witness geometry: parts T1–T5

- **Subproject:** 03-ilang-space
- **Package:** 13-numerical-run
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-08

## Setup and assumptions

All models, parameters, seeds, grids, tolerances and decision rules are those of question.md, unchanged. The imaginary unit is written $\mathrm i$; $i,j,k$ are indices. All raw numbers are in `code/v1/output/*.json`. Every number below was written there by the scripts.

**Inputs used (as quoted).** (2.11), (3.5) for $W$ and $\alpha$; (4.3) for $N_V$, with $x\asymp x'$ iff $W(x,x')>0$ (4.1); (4.6) for $\ell$; (5.10) for $d_0$ and $u_h$; the ensembles $\mathrm{GUE}(s)$, $\mathrm{GOE}(s)$ of 07 and (7.6), (7.7), (7.10), (7.11); (8.16); (10.10), (10.15) and Step 6(a) of 10, with $\omega(v,w)=\operatorname{Im}\langle v\vert w\rangle$; (12.8).

**Conventions the question leaves open, fixed before the runs.**
- $\mathrm{GUE}(1)$: draw $A=X+\mathrm iY$ with $X$, then $Y$, i.i.d. standard normal $d\times d$ matrices, and set $K=(A+A^\dagger)/2$. $\mathrm{GOE}(1)$: $K=(X+X^{T})/\sqrt2$. Both realize the variances quoted from 07.
- The basis of a draw is the place basis of the medium, with $e_1=\lvert\chi\rangle$ in T1–T3. In T4 and T5, cell 1 is the leftmost tensor factor, and $\lvert0\rangle=(1,0)^{T}$.
- Haar-random qubit state: a complex Gaussian vector (real part drawn first) divided by its norm.
- Records are drawn in place order from one generator per seed. In T2(b) each pair is drawn as $K_h$, then $K_{h'}$. In T3 the triangles are drawn in sequence, and the 150 numbers $x_h$ as a $50\times3$ array, row by row. $R$ in T5 is a $10\times16$ array, row $i$ belonging to $h_i$. Triangles are numbered $0,\dots,49$ in draw order.
- "Within $3\%$ / $10\%$" means relative deviation $\le0.03$ / $\le0.10$ from the quoted value. The sample standard deviation uses $n-1$.
- T3 does not fix the probe weights. I used $\phi_h=1/\sqrt3$; by Step 1 the results do not depend on this choice.

**Setting of T4 (my reading of 08, which is not quoted in full).** The probe $a$ (places $h$) and the body $b$ (places $\beta$) form the recorded object of (12.8):

$$
C=\sum_{h,\beta}\lvert h\beta\rangle\langle h\beta\rvert\otimes M_{h\beta},\qquad
M_{h\beta}=K_h^{(c_1)}+B_\beta^{(c_{r+1})}+\sum_{k=1}^{4}J_k^{(c_kc_{k+1})} ,
$$

with start $\lvert\phi\rangle\otimes\lvert\beta_1\rangle\otimes\lvert\omega\rangle$. "The body is at $\beta_1$" means that only $\beta=\beta_1$ carries weight. So $B_{\beta_2}$ is drawn but does not enter, and the probe view is $V_{hh'}=\langle\psi_{h'\beta_1}\vert\psi_{h\beta_1}\rangle$.

**Precision.** All primary results use double precision. mpmath appears only in diagnostics (Steps 4 and 5) that check the effect of rounding. It replaces no primary result.

## Derivation

### Step 1. Common computational rule

In every part, $C=\sum_h\lvert h\rangle\langle h\rvert\otimes M_h$ with a product start, so (12.8) gives the branch vectors. Since $\lvert\Psi\rangle=\sum_h\lvert h\rangle\otimes\lvert\psi_h\rangle$, the partial trace (1.5) gives

$$
\lvert\psi_h(\lambda)\rangle=\phi_h\,e^{-\mathrm iM_h\lambda}\lvert\omega\rangle,\qquad
(V_A)_{hh'}=\langle\psi_{h'}\vert\psi_h\rangle,\qquad p_h=(V_A)_{hh} .
\tag{13.1}
$$

By (1.7), $V_{hh'}=a_ha_{h'}^{*}G_{hh'}$, so the factors $a_h$ cancel in

$$
W(h,h')=\frac{\lvert V_{hh'}\rvert^2}{p_hp_{h'}},\qquad
W(h_1,h_2,h_3)=\frac{V_{h_1h_2}V_{h_2h_3}V_{h_3h_1}}{p_{h_1}p_{h_2}p_{h_3}},\qquad
\alpha=\arccos\sqrt{W},\qquad \Phi=\arg W(h_1,h_2,h_3).
\tag{13.2}
$$

Hence $W$, $\alpha$ and $\Phi$ do not depend on the choice of $\phi_h\neq0$. Places with $1-W<10^{-12}$ are merged into one point (transitive closure). On the points, $N_V$ follows (4.3) with strict inequality, and $\ell$ follows (4.6), computed by Floyd–Warshall with weights $\alpha$. A fitted slope is `numpy.polyfit(log λ, log|y|, 1)`. T1–T4 use `scipy.linalg.expm`. T5 uses sparse operators and `scipy.sparse.linalg.expm_multiply`, and never forms a dense $65536\times65536$ matrix. Helpers: `code/v1/common.py`.

### Step 2. T1, leading order (5.10)

Method: $n=8$, $d_c=6$, seed 1301, uniform $\phi_h$. The script computes $d_0(h,h')=\lVert u_h-u_{h'}\rVert$ from (5.10) and $\alpha$ from (13.2) for all 28 pairs. Script `t1_leading_order.py`, output `t1_leading_order.json` (records, $u_h$, $d_0$, and per $\lambda$: $W$, $\alpha$, relative errors per pair). All 8 places are distinct points at every $\lambda$.

| $\lambda$ | $10^{-1}$ | $3\cdot10^{-2}$ | $10^{-2}$ | $3\cdot10^{-3}$ | $10^{-3}$ |
|---|---|---|---|---|---|
| $E(\lambda)$ | $1.1141\cdot10^{-1}$ | $3.4722\cdot10^{-2}$ | $1.1650\cdot10^{-2}$ | $3.5014\cdot10^{-3}$ | $1.1677\cdot10^{-3}$ |

$$
E(10^{-3})=1.168\cdot10^{-3}<10^{-2},\qquad \text{fitted slope}=0.9911\ge0.9\qquad\Longrightarrow\qquad \text{T1: pass.}
\tag{13.3}
$$

### Step 3. T2, generic dimension and distances (7.6), (7.7), (7.10), (7.11)

**(a)** For each of the 16 pairs $(d_c,n)$ and both ensembles, the script builds the real matrix $[\operatorname{Re}D\;\operatorname{Im}D]$, whose rows are $D_h=u_h-u_{h_1}$, and counts the singular values above $10^{-9}$ times the largest. For GOE the imaginary columns are zero, which leaves the rank unchanged. Entries are GUE rank / GOE rank:

| $d_c\backslash n$ | 3 | 6 | 12 | 20 |
|---|---|---|---|---|
| 2 | 2 / 1 | 2 / 1 | 2 / 1 | 2 / 1 |
| 3 | 2 / 2 | 4 / 2 | 4 / 2 | 4 / 2 |
| 5 | 2 / 2 | 5 / 4 | 8 / 4 | 8 / 4 |
| 9 | 2 / 2 | 5 / 5 | 11 / 8 | 16 / 8 |

All 32 ranks equal $\min(n-1,2(d_c-1))$ and $\min(n-1,d_c-1)$. Diagnostic: over all cases, the smallest kept singular-value ratio is $1.24\cdot10^{-2}$ and the largest discarded one is $8.4\cdot10^{-17}$, so the threshold is far from both. **T2(a): pass.**

**(b)** $d_c=9$, 4000 pairs per ensemble. Quoted: mean $16$; relative standard deviation $1/\sqrt8=0.35355$ (GUE) and $1/2$ (GOE).

| ensemble (seed) | mean of $d_0^2$ | rel. dev. | rel. std | rel. dev. |
|---|---|---|---|---|
| GUE (1303) | 16.0340 | 0.21 % | 0.35503 | 0.42 % |
| GOE (1304) | 16.1217 | 0.76 % | 0.49795 | 0.41 % |

**T2(b): pass.** Script `t2_dimension_distances.py`, output `t2_dimension_distances.json` (all singular values, all 8000 values of $d_0^2$).

$$
\text{T2(a): pass (32/32 ranks as in (7.7), (7.11))},\qquad \text{T2(b): pass}.
\tag{13.4}
$$

### Step 4. T3, loop phases (10.10), (10.15), Step 6(a) of 10

**(a)** $d_c=4$, seed 1305. Of the 50 triangles, 49 satisfy $\lvert\omega(u_{h_2}-u_{h_1},u_{h_3}-u_{h_1})\rvert>10^{-2}$. For these the script computes $\Phi$ by (13.2) and $\Phi^{(2)}=-\lambda^2\omega$:

| $\lambda$ | $10^{-2}$ | $3\cdot10^{-3}$ | $10^{-3}$ |
|---|---|---|---|
| $\max\lvert\Phi-\Phi^{(2)}\rvert/\lvert\Phi^{(2)}\rvert$ | 1.1873 | 0.35496 | 0.11821 |

$$
\max(10^{-3})=0.1182\not<10^{-2},\qquad\text{fitted slope}=1.0019\qquad\Longrightarrow\qquad\text{T3(a): fail.}
\tag{13.5}
$$

Diagnostics (not decisions). At $\lambda=10^{-3}$ the maximum is attained by triangle 34, with $\omega=0.02907$. The second-largest value, $0.01048$, belongs to triangle 43 ($\omega=0.6752$) and is also above $10^{-2}$. The median over the 49 triangles is $1.07\cdot10^{-3}$. A 40-digit mpmath recomputation of $\Phi$ for triangle 34 at $\lambda=10^{-3}$ agrees with the double-precision value to a relative $2.8\cdot10^{-12}$. Rounding is therefore not the cause of the failure.

**(b)** 50 triangles each:

| control | $\max\lvert\Phi\rvert$ at $10^{-2}$ | at $3\cdot10^{-3}$ | at $10^{-3}$ | fitted slope |
|---|---|---|---|---|
| (i) $K_h=x_hX$ (1306, 1307) | $4.0127\cdot10^{-5}$ | $1.0819\cdot10^{-6}$ | $4.0064\cdot10^{-8}$ | 3.0007 |
| (ii) GOE (1308) | $1.3873\cdot10^{-5}$ | $3.7444\cdot10^{-7}$ | $1.3868\cdot10^{-8}$ | 3.0002 |

$$
\text{both slopes}\ge2.8\qquad\Longrightarrow\qquad\text{T3(b): pass.}
\tag{13.6}
$$

Diagnostic: for (ii), $\max_t\lvert W(-\lambda)-W(\lambda)^*\rvert=0$ exactly at $\lambda=10^{-2}$, as stated by (10.15). Script `t3_loop_phases.py`, output `t3_loop_phases.json` (records, $\omega$ and $\Phi$, $\Phi^{(2)}$ for each triangle, diagnostics).

### Step 5. T4, light cone (8.16)

Method: $M_h^{(r)}=K_h^{(c_1)}+B_{\beta_1}^{(c_{r+1})}+\sum_kJ_k$ on $(\mathbb C^2)^{\otimes5}$. Then $\Delta W=W-W\vert_{B_{\beta_1}=0}$ for the 3 probe pairs.

| $r$ | $\max\lvert\Delta W\rvert$: $0.1$ | $0.05$ | $0.025$ | $0.0125$ | slope | threshold $3+r-0.2$ | within $0.2$ of $3+r$ |
|---|---|---|---|---|---|---|---|
| 0 | $1.899\cdot10^{-4}$ | $2.157\cdot10^{-5}$ | $3.056\cdot10^{-6}$ | $4.035\cdot10^{-7}$ | 2.9454 | 2.8 | yes |
| 1 | $7.442\cdot10^{-5}$ | $4.497\cdot10^{-6}$ | $2.740\cdot10^{-7}$ | $1.687\cdot10^{-8}$ | 4.0359 | 3.8 | yes |
| 2 | $3.157\cdot10^{-7}$ | $1.025\cdot10^{-8}$ | $3.290\cdot10^{-10}$ | $1.034\cdot10^{-11}$ | 4.9657 | 4.8 | yes |
| 3 | $2.465\cdot10^{-9}$ | $2.863\cdot10^{-11}$ | $3.699\cdot10^{-13}$ | $5.662\cdot10^{-15}$ | 6.2469 | 5.8 | no |

$$
\text{all slopes}\ge3+r-0.2\ \Longrightarrow\ \text{T4: pass};\qquad
\max\lvert\Delta W\rvert\le1.7\cdot10^{-15}\ \text{for }B_{\beta_1}=0.7\,\mathbb 1\ \Longrightarrow\ \text{control: pass}.
\tag{13.7}
$$

Diagnostic: a 40-digit mpmath Taylor propagation of the same operators gives the slopes 2.9454, 4.0359, 4.9657 and 6.2859. At $r=3$, $\lambda=0.0125$ the double-precision value deviates from the mpmath value ($5.18\cdot10^{-15}$) by $9.4\%$. Double precision is near its floor there. The decision and the exploratory flag are the same with either set. Script `t4_light_cone.py`, output `t4_light_cone.json`.

### Step 6. T5, closed form for $g=0$ (short argument)

For $g=0$, $M_{h_i}=\sum_kF_{ik}\sigma_x^{(k)}$, with $F=f$ (local) or $F=R$ (control, rescaled). The terms act on different cells and commute. Since $(\sigma_x)^2=\mathbb 1$,

$$
e^{-\mathrm iM_{h_i}\lambda}\lvert0\rangle^{\otimes16}=\bigotimes_{k=1}^{16}\bigl(\cos(\lambda F_{ik})\lvert0\rangle-\mathrm i\sin(\lambda F_{ik})\lvert1\rangle\bigr) .
$$

This is a product of unit vectors, so it equals $\lvert E_{h_i}\rangle$. The cell-wise overlap is $\cos\lambda F_{jk}\cos\lambda F_{ik}+\sin\lambda F_{jk}\sin\lambda F_{ik}=\cos\lambda(F_{ik}-F_{jk})$. With (2.11) this gives

$$
G_{h_ih_j}=\prod_{k=1}^{16}\cos\bigl(\lambda(F_{ik}-F_{jk})\bigr),\qquad
W(h_i,h_j)=\prod_{k=1}^{16}\cos^2\bigl(\lambda(F_{ik}-F_{jk})\bigr).
\tag{13.8}
$$

**Code check.** The largest absolute deviation of the numerical $W$ (expm_multiply) from (13.8) is $2.9\cdot10^{-15}$, $3.6\cdot10^{-15}$, $1.9\cdot10^{-15}$ for the local records at $\lambda=0.05,0.3,1$. For the control it is $5.3\cdot10^{-15}$, $3.6\cdot10^{-15}$, $1.9\cdot10^{-16}$.

### Step 7. T5, results

All 10 places are distinct points in every case. All $W>0$; the minimum is $8.99\cdot10^{-6}$ (control, $\lambda=1$).

| case | $\lambda$ | edges of $N_V$ | path | order | step $\alpha$ (min–max) | $\ell$(ends) |
|---|---|---|---|---|---|---|
| local, $g=0$ | 0.05 | 9 | yes | $h_1,h_2,\dots,h_{10}$ | 0.03736–0.03739 | 0.33643 |
| local, $g=0$ | 0.3 | 9 | yes | $h_1,\dots,h_{10}$ | 0.22345–0.22358 | 2.01194 |
| local, $g=0$ | 1.0 | 9 | yes | $h_1,\dots,h_{10}$ | 0.71917–0.71953 | 6.47503 |
| local, $g=0.5$ | 0.05 | 9 | yes | $h_1,\dots,h_{10}$ | 0.03736–0.03738 | 0.33635 |
| local, $g=0.5$ | 0.3 | 9 | yes | $h_1,\dots,h_{10}$ | 0.22151–0.22159 | 1.99415 |
| local, $g=0.5$ | 1.0 | 9 | yes | $h_1,\dots,h_{10}$ | 0.63056–0.63117 | 5.67630 |
| control | 0.05, 0.3, 1.0 | 12 | no | — | — | — |

At all three $\lambda$ the control graph is connected and has the same 12 edges: $\{1,8\},\{1,9\},\{2,7\},\{2,10\},\{3,6\},\{3,8\},\{4,10\},\{5,6\},\{5,10\},\{6,9\},\{7,9\},\{8,10\}$ (indices of $h_i$). It contains cycles, and its degrees are $(2,2,2,1,2,3,2,3,3,4)$. In the path cases, $\ell$ between the ends equals the sum of the nine steps. The smallest margin of the strict inequality in (4.3) over all cases is $3.6\cdot10^{-5}$ (control, $\lambda=0.05$), far above rounding. Script `t5_chain.py`, output `t5_chain.json` (all $W$ matrices, $\alpha$ on points, edges, degrees, orders, steps, $\ell$, checks).

$$
\text{local } g=0:\ N_V \text{ a path at } \lambda=0.05,0.3,1;\quad \text{control at } \lambda=0.3:\ \text{not a path}\ \Longrightarrow\ \text{T5: supported.}
\tag{13.9}
$$

## Result

| part | decision | tag | raw output |
|---|---|---|---|
| T1 leading order | pass | (13.3) | `t1_leading_order.json` |
| T2(a) ranks | pass | (13.4) | `t2_dimension_distances.json` |
| T2(b) distances | pass | (13.4) | `t2_dimension_distances.json` |
| T3(a) generic loop phases | **fail** | (13.5) | `t3_loop_phases.json` |
| T3(b) negative controls | pass | (13.6) | `t3_loop_phases.json` |
| T4 light cone | pass | (13.7) | `t4_light_cone.json` |
| T4 negative control | pass | (13.7) | `t4_light_cone.json` |
| T5 chain at finite $\lambda$ | supported | (13.9) | `t5_chain.json` |

T4 exploratory: the slope is within $0.2$ of $3+r$ for $r=0,1,2$, but not for $r=3$ (6.2469). For T5 with $g=0.5$ the results are reported without a decision: $N_V$ is the path $h_1,\dots,h_{10}$ at all three $\lambda$.

## Consistency checks

1. **Closed form (required check).** For both $g=0$ cases the numerical $W$ agrees with (13.8) to $\le5.3\cdot10^{-15}$ (Step 6).
2. **Rounding.** mpmath recomputations at 40 digits reproduce T3(a) to $2.8\cdot10^{-12}$, and reproduce the T4 slopes to four digits for $r\le2$. They give the same T4 decision for $r=3$ (Steps 4, 5).
3. **Independent propagation for $g=0.5$.** At $\lambda=1$, a 40-substep Taylor propagation agrees with expm_multiply to $8.7\cdot10^{-16}$ in the vectors and $5.6\cdot10^{-16}$ in $W$. The norms are preserved to $\le1.8\cdot10^{-15}$ in all T5 runs (`t5_chain.json`, diagnostic keys).

## Open issues

- **T3(a) fails by the stated rule.** At $\lambda=10^{-3}$ the maximal relative error is $0.118$, from triangle 34 with $\lvert\omega\rvert=0.029$, and the second largest is $0.0105$. The relative error decreases as $\lambda^{1.00}$. The tolerance $10^{-2}$ at $\lambda=10^{-3}$ is not reached on this sample.
- **T4 setting.** The setting of 08 is not quoted in full, and I used the reading stated under "Setup". At $r=3$, $\lambda=0.0125$, double precision is near its floor (Step 5); this changes neither decision nor flag.
- **Draw conventions.** The draw orders and the GUE/GOE constructions listed under "Setup" are my choices; question.md does not fix them. Other admissible choices give other samples.

## Code

All files are under `03-ilang-space/13-numerical-run/code/v1/`. They run with `.venv/Scripts/python.exe <path>` from the project root (numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0). No package was installed.
- `common.py`: shared helpers. It contains the ensembles, the view (13.1), $W$ and loop $W$ (13.2), $\alpha$, points, $N_V$ (4.3), the path test and $\ell$ (4.6), and JSON output.
- `t1_leading_order.py` (computation): T1, writes `output/t1_leading_order.json`.
- `t2_dimension_distances.py` (computation): T2(a), (b), writes `output/t2_dimension_distances.json`.
- `t3_loop_phases.py` (computation, with an mpmath diagnostic): T3(a), (b), writes `output/t3_loop_phases.json`.
- `t4_light_cone.py` (computation, with an mpmath diagnostic): T4 and its control, writes `output/t4_light_cone.json`.
- `t5_chain.py` (computation and check): T5 with sparse operators and expm_multiply, plus the closed-form check (13.8) and a Taylor diagnostic. Writes `output/t5_chain.json`.

## Methods used

- Partial trace / Gram matrix of branch vectors
- Matrix exponential (Padé `expm`), sparse truncated-Taylor `expm_multiply`, Taylor propagation
- Gaussian unitary and orthogonal ensembles, Haar-random states
- Singular value decomposition, numerical rank
- Least-squares log–log slope fits
- Relative neighbourhood condition (4.3), Floyd–Warshall shortest paths
- Product-state closed form for commuting Pauli generators
- Extended-precision cross-checks (mpmath)
