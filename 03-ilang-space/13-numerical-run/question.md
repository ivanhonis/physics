# Question: 13-numerical-run

- **Subproject:** 03-ilang-space
- **Package:** 13-numerical-run
- **Equation tags:** (13.k)
- **Created:** 2026-10-08

## Goal

Run a precommitted numerical test of the witness geometry, in five parts, T1–T5. Parts T1–T4 test results quoted under "Inputs" on concrete, non-trivial systems. Part T5 determines, on a larger system, whether local records produce a one-dimensional chain at finite $\lambda$.

**Precommitment.** Every model, parameter, seed, grid, tolerance and decision rule is fixed in this question before the run. None of them may be changed. If a part cannot be run as specified, report that, and do not modify the part. Every reported number must be produced by the scripts and saved as raw output. A decision is "pass" or "fail" by the stated rule only. No other criterion may be substituted after the run.

**Common conventions for the code.**
- Random numbers come from `numpy.random.default_rng(seed)`, with the seeds given below.
- $\mathrm{GUE}(s)$ and $\mathrm{GOE}(s)$ are the ensembles defined in 07-random-records (quoted below), drawn in the stated basis.
- Evolution is exact and uses the block structure (12.8). Each needed vector $e^{-iM_h\lambda}\lvert\omega\rangle$ is computed with `scipy.linalg.expm` for small spaces, or with `scipy.sparse.linalg.expm_multiply` for large ones.
- $W$ and $\alpha$ follow (2.11) and (3.5). Places with $1-W<10^{-12}$ are the same point. $N_V$ follows (4.3), and $\ell$ follows (4.6).
- A fitted slope is the least-squares slope of $\log\lvert y\rvert$ against $\log\lambda$ over the stated grid.
- $\lvert0\rangle$ denotes the $+1$ eigenvector of $\sigma_z$, and $\sigma^{(k)}$ a Pauli matrix on cell $k$.

**T1. Leading order** (tests (5.10)).
- **Setting.** The setting of 05: $n=8$ places and $d_c=6$, with $\lvert\chi\rangle=e_1$. The records are $K_h$ i.i.d. $\mathrm{GUE}(1)$ with seed 1301, and the probe state is uniform, $\phi_h=1/\sqrt8$.
- **Grid.** $\lambda\in\{10^{-1},\,3\cdot10^{-2},\,10^{-2},\,3\cdot10^{-3},\,10^{-3}\}$.
- **Determine** $E(\lambda):=\max_{h\neq h'}\bigl\lvert\alpha(h,h';\lambda)/\lambda-d_0(h,h')\bigr\rvert/d_0(h,h')$, with $d_0$ from (5.10).
- **Decision.** Pass iff $E(10^{-3})<10^{-2}$ and the fitted slope of $E$ is $\ge0.9$.

**T2. Generic dimension and distances** (tests (7.6), (7.7), (7.10), (7.11)).
- **(a) Rank.** For every $d_c\in\{2,3,5,9\}$ and $n\in\{3,6,12,20\}$:
  - draw $\mathrm{GUE}(1)$ records with seed $1302+100\,d_c+n$, and determine the numerical affine rank of $\{u_h\}$. This is the number of singular values of the real matrix of the differences $u_h-u_{h_1}$, written in real coordinates, that exceed $10^{-9}$ times the largest one.
  - Do the same for $\mathrm{GOE}(1)$ records with seed $1402+100\,d_c+n$, in real coordinates.

  **Decision.** Pass iff every rank equals the value quoted in (7.7) or (7.11), respectively.
- **(b) Distances.** For $d_c=9$, draw $4000$ independent pairs of records: $\mathrm{GUE}(1)$ with seed 1303, and $\mathrm{GOE}(1)$ with seed 1304. Determine the sample mean and the sample relative standard deviation of $d_0^2$.

  **Decision.** Pass iff, for both ensembles, the mean lies within $3\%$ of the quoted mean and the relative standard deviation lies within $10\%$ of the quoted value.

**T3. Loop phases** (tests (10.10) and (10.15), and Step 6(a) of 10).
- **(a) Generic records.** $d_c=4$ and $\lvert\chi\rangle=e_1$. Draw 50 triangles, each with three independent $\mathrm{GUE}(1)$ records, seed 1305. Use the grid $\lambda\in\{10^{-2},\,3\cdot10^{-3},\,10^{-3}\}$.
  - Consider only the triangles with $\lvert\omega(u_{h_2}-u_{h_1},u_{h_3}-u_{h_1})\rvert>10^{-2}$.
  - For these, determine the relative error $\lvert\Phi-\Phi^{(2)}\rvert/\lvert\Phi^{(2)}\rvert$, where $\Phi^{(2)}$ is the $\lambda^2$ term of (10.10), and take its maximum over the triangles.

  **Decision.** Pass iff this maximum is $<10^{-2}$ at $\lambda=10^{-3}$ and its fitted slope is $\ge0.9$.
- **(b) Negative controls.** Use the same grid and 50 triangles each.
  - **(i) Commuting records:** $K_h=x_hX$, where $X$ is one $\mathrm{GUE}(1)$ draw (seed 1306) and the $x_h$ are i.i.d. standard normal (seed 1307).
  - **(ii) Real records:** $\mathrm{GOE}(1)$ (seed 1308), with $\lvert\chi\rangle=e_1$ real.

  Determine $\max\lvert\Phi\rvert$ over the triangles at each $\lambda$, and its fitted slope. **Decision.** Pass iff the fitted slope is $\ge2.8$ in both controls.

**T4. Light cone** (tests (8.16)).
- **Medium.** A chain of $L=5$ qubit cells $c_1,\dots,c_5$, starting in the product of independent Haar-random pure states, seed 1309. The links are $J_k$ on $c_k c_{k+1}$, $k=1,\dots,4$, each a $\mathrm{GUE}(1)$ draw on $\mathbb C^4$ with seed $1310+k$.
- **Probe.** Three places, with $\phi_h=1/\sqrt3$, recorded by $c_1$: $K_h$ i.i.d. $\mathrm{GUE}(1)$ on $\mathbb C^2$, seed 1320.
- **Body.** Two places $\beta_1,\beta_2$, recorded by $c_{r+1}$: $B_\beta$ i.i.d. $\mathrm{GUE}(1)$ on $\mathbb C^2$, seed 1330. The body is at $\beta_1$. Here $r\in\{0,1,2,3\}$.
- **Grid.** $\lambda\in\{0.1,\,0.05,\,0.025,\,0.0125\}$.
- **Determine,** for each $r$:
  - the body-dependent part $\Delta W$, i.e. $W$ minus its value at $B_{\beta_1}=0$, with all other operators unchanged;
  - $\max\lvert\Delta W\rvert$ over the pairs of probe places at each $\lambda$, and its fitted slope.

**Decision.** Pass iff, for every $r$, the fitted slope is $\ge 3+r-0.2$. Report also whether each slope lies within $0.2$ of $3+r$. This is exploratory and not part of the decision.

**Negative control.** $B_{\beta_1}=0.7\,\mathbb 1$ for every $r$. Pass iff $\max\lvert\Delta W\rvert\le10^{-12}$ at every $\lambda$.

**T5. Local records and a chain at finite $\lambda$** (exploratory, with a precommitted decision rule).
- **Probe.** Ten places $h_1,\dots,h_{10}$, with $\phi_h=1/\sqrt{10}$.
- **Medium.** $L=16$ qubit cells, starting in $\lvert0\rangle^{\otimes16}$.
- **Local records.** $K_{h_i}=\sum_{k=1}^{16}f_{ik}\,\sigma_x^{(k)}$ with $f_{ik}=\exp\bigl(-(i+3-k)^2/(2\cdot1.5^2)\bigr)$.
- **Links.** $J=g\sum_{k=1}^{15}\bigl(\sigma_x^{(k)}\sigma_x^{(k+1)}+\sigma_y^{(k)}\sigma_y^{(k+1)}\bigr)$ with $g\in\{0,\,0.5\}$.
- **Nonlocal control.** $K'_{h_i}=\sum_kR_{ik}\sigma_x^{(k)}$, with $R_{ik}$ i.i.d. standard normal (seed 1340). Each row is rescaled so that $\sum_kR_{ik}^2=\sum_kf_{ik}^2$. The control uses $g=0$.
- **Grid.** $\lambda\in\{0.05,\,0.3,\,1.0\}$.

For each case (local with $g=0$, local with $g=0.5$, and the control) and each $\lambda$, determine:
- the matrix $W$;
- the points;
- the neighbour graph $N_V$;
- whether $N_V$ is a path graph (connected, acyclic, all degrees at most 2), and if so, its order of places, its step lengths $\alpha$ and $\ell$ between its two ends.

**Code check.** For $g=0$ the records commute. Determine $W$ in closed form for this case, and report the maximum absolute deviation of the numerical $W$ from it.

**Decision.** "Local records produce a chain at finite $\lambda$" is supported iff two things hold:
- for the local records with $g=0$, $N_V$ is a path graph at all three $\lambda$;
- for the nonlocal control, $N_V$ is not a path graph at $\lambda=0.3$.

For $g=0.5$ the results are reported without a decision.

## Inputs

From 02-view-content@v1. Notation fixed there: $p_h:=\langle h\vert V_A\vert h\rangle$, $H_V:=\{h:p_h>0\}$, $\lvert\psi_h\rangle:=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle$, $G_{hh'}=\langle E_{h'}\vert E_h\rangle$, $W(h_1,\dots,h_k):=G_{h_1h_2}\cdots G_{h_kh_1}$.

Eq. (2.11):

$$
W(h)=1,\qquad W(h,h')=\lvert G_{hh'}\rvert^2=\frac{\lvert(V_A)_{hh'}\rvert^2}{p_hp_{h'}} .
$$

From 03-witness-distance@v1. Notation fixed there: $h\approx h'$ iff $W(h,h')=1$; $X_V:=H_V/{\approx}$; $\alpha(x,x'):=\arccos\sqrt{W(x,x')}\in[0,\pi/2]$.

Eq. (3.5):

$$
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}}
=\frac{\lvert\langle h\vert V_A\vert h'\rangle\rvert}{\sqrt{\langle h\vert V_A\vert h\rangle\langle h'\vert V_A\vert h'\rangle}},\qquad h\in x,\ h'\in x' .
$$

From 04-neighbours@v1.

Eq. (4.3):

$$
x\sim x'\;:\Longleftrightarrow\;x\asymp x'\ \text{ and there is no } y\in X_V \text{ with } \max\bigl(\alpha(x,y),\alpha(y,x')\bigr)<\alpha(x,x') ,
$$

where $x\asymp x'$ means $W(x,x')>0$ (4.1).

Eq. (4.6):

$$
\ell(x,x'):=\min\Bigl\{\sum_{j=0}^{m-1}\alpha(y_j,y_{j+1})\;:\;y_0=x,\ y_m=x',\ y_j\sim y_{j+1}\Bigr\},
\qquad \ell(x,x'):=+\infty\ \text{between components.}
$$

From 05-recording-contract@v1. This holds in the setting of 05: one recorded object $a$, a medium $c$, the recording contract $\sum_h\lvert h\rangle\langle h\rvert\otimes K_h$, and the start $\lvert\phi\rangle\otimes\lvert\chi\rangle$.

Eq. (5.10):

$$
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
$$

From 07-random-records@v1. In a basis $e_1=\lvert\chi\rangle,e_2,\dots,e_{d_c}$ of $\mathcal H_c$:
- $\mathrm{GUE}(s)$ has density $\propto\exp(-\operatorname{Tr}K^2/(2s^2))$; equivalently, $K_{ab}$ ($a<b$) is complex Gaussian with independent real and imaginary parts of variance $s^2/2$, and $K_{aa}$ is real Gaussian with variance $s^2$;
- $\mathrm{GOE}(s)$ is real symmetric with density $\propto\exp(-\operatorname{Tr}K^2/(4s^2))$; equivalently, $K_{ab}$ ($a<b$) is real Gaussian with variance $s^2$, and $K_{aa}$ is real Gaussian with variance $2s^2$.

The record vectors are independent across places.

Eq. (7.6), GUE:

$$
E\,d_0^2=2(d_c-1)\,s^2,\qquad
\operatorname{Var}d_0^2=4(d_c-1)\,s^4,\qquad
\frac{\sqrt{\operatorname{Var}d_0^2}}{E\,d_0^2}=\frac{1}{\sqrt{d_c-1}} .
$$

Eq. (7.7):

$$
\dim_0=\min\bigl(n-1,\;2(d_c-1)\bigr)\qquad\text{almost surely},
$$

Eq. (7.10), GOE:

$$
E\,d_0^2=2(d_c-1)\,s^2,\qquad
\operatorname{Var}d_0^2=8(d_c-1)\,s^4,\qquad
\frac{\sqrt{\operatorname{Var}d_0^2}}{E\,d_0^2}=\sqrt{\frac{2}{d_c-1}} ,
$$

Eq. (7.11):

$$
\dim_0=\min\bigl(n-1,\;d_c-1\bigr)\qquad\text{almost surely}.
$$

From 08-cell-medium@v1. This holds in the setting of 08 on a chain of cells $c_1,\dots,c_L$ with neighbour links:
- the probe is recorded by $c_1$, and the body by $c_{r+1}$;
- the initial state is a product;
- $\Delta W$ is the body-dependent part, and $G_0$ is the overlap at $B_{\beta_0}=0$.

Eq. (8.16):

$$
\Delta W^{(\beta_0)}=2\operatorname{Re}\bigl(G_0^*\,\delta G\bigr)+\lvert\delta G\rvert^2=2\operatorname{Re}\bigl(-\mathrm i\,a\,\lambda^{r+2}\bigr)+O(\lambda^{r+3})=O(\lambda^{3+r}).
$$

From 10-loop-data@v1. Notation fixed there: $\omega(v,w):=\operatorname{Im}\langle v\vert w\rangle$, and the loop phase $\Phi(h_1,\dots,h_k;\lambda):=\arg W(h_1,\dots,h_k;\lambda)$, in the setting of 05. Step 6(a) of 10 states that the $\lambda^2$ term of every loop phase vanishes when the records commute pairwise.

Eq. (10.10):

$$
\Phi(h_1,h_2,h_3;\lambda)=-\lambda^2\,\omega\bigl(u_{h_2}-u_{h_1},\,u_{h_3}-u_{h_1}\bigr)+O(\lambda^3).
$$

Eq. (10.15). This holds for real records, i.e. every $K_h$ real symmetric in a basis in which $\lvert\chi\rangle$ is real.

$$
W(h_1,\dots,h_k;-\lambda)=W(h_1,\dots,h_k;\lambda)^* .
$$

From 12-identical-probes@v1. This holds for $C=\sum_h\lvert h\rangle\langle h\rvert\otimes M_h$ with $M_h=M_h^\dagger$, and the product start $\lvert\Phi\rangle\otimes\lvert\omega\rangle$ with $\Phi_h\neq0$.

Eq. (12.8):

$$
\lvert\psi_h(\lambda)\rangle=\Phi_h\,e^{-iM_h\lambda}\lvert\omega\rangle .
$$

## Assumptions

- The models, parameters, seeds, grids, tolerances and decision rules stated under "Goal", unchanged.
- Double-precision arithmetic, unless a part cannot reach its tolerance in double precision. In that case extended precision (mpmath) may be used for that part only; report this.

## Scope

- In scope: exactly T1–T5 as specified, the raw outputs, and the decisions by the stated rules.
- Out of scope:
  - any change of a parameter, seed, grid, tolerance or rule;
  - additional tests that are reported as decisions; extra diagnostic output is allowed if it is labelled as such;
  - any physical or spatial interpretation of the results (M1, M4).

## Depth

- T1–T4: computation as specified. The derivation file states the method, the results and the decisions, and cites the scripts and output files at each step.
- T5: computation as specified. The closed form for $g=0$ is a short argument, derived in the file.

## Expected result

For each part:
- a table of the determined quantities;
- the decision by the stated rule, pass or fail;
- the names of the output files that hold the raw data.

A final table lists all decisions. Give the main results tags $(13.k)$.

## Code

Required: computation and check.
- **Computation:** parts T1–T5 exactly as specified under "Goal". The raw output of each part goes to a JSON or CSV file in `code/v1/output/`: matrices, per-pair and per-triangle values, fitted slopes, and decisions.
- **Check:** the closed-form comparison of T5 for $g=0$.
