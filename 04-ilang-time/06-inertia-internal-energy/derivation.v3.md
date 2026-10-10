# Inertia and internal energy: response at λ = 0 and averaged response

- **Subproject:** 04-ilang-time
- **Package:** 06-inertia-internal-energy
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-10

## Changes from previous version

- **Step 5e rewritten (I1).**
  - v2 gave the error of the average as $`r=-\rho+R/\mathcal F`$ with $`R=O(T^2\dots)`$, (6.19). That estimate is not valid for every interval allowed by (6.14): on intervals that start late, $`\lambda_1\gg\Lambda`$, the accumulated interbranch phase adds a term of order $`T^3/\Lambda`$. (6.19) is withdrawn; its tag is retired and not reused.
  - (6.14) keeps its quantity, its leading term and both conditions. Its error is now additive, $`\mathcal E`$.
  - New: (6.24), the exact first-order coefficient at a fixed interval; (6.25), an exact bound on the deviation of the velocity from the branch velocity; (6.26), an exact bound on $`\mathcal E`$ for every interval with $`\mathcal F_{\max}T\le\pi/2`$; (6.27), an order estimate of the part beyond first order, with the accumulated phase.
  - Every statement is marked as exact or as an order estimate, with its conditions (5e, item iv).
- **Step 6c (I2).** The sentence on the loss of factorization is replaced by two cases: a common eigenvector (product state, level-dependent scalar position dynamics) and a general internal start.
- **Step 6b.** The variation of the response with $`\lambda`$ is bounded exactly, including the record term. This is a precision; (6.17) is unchanged.
- Steps 1–4, 5a–5d, 5f, 6a, body E and Step 7 are unchanged in content, and so are the tags (6.1)–(6.17) and (6.20)–(6.23). (6.18) stays retired. Check 3 of v2 ((6.21) against (6.12)) remains valid; because of the limit of three checks it is replaced by a check of the new bounds.

## Response to verification

- **I1: Accepted and fixed in Step 5e ((6.14), (6.24)–(6.27)) and Step 5f.** The verifier's term is confirmed: the interbranch phase is $`2M_k\lambda+\tau^2f^2\lambda^3/(3M_k)+\dots`$, and expanding it gives a secular term of size up to $`\tau^2\lvert f\rvert^3T^3/(3M_k^2\Lambda)`$. The fix follows the first suggestion and does not restrict the intervals.
  - The linear coefficient $`(1-\rho)`$ is kept and stated as exact, (6.24).
  - The finite-force remainder is bounded by (6.26), an exact inequality for every $`\lambda_1\ge0`$. It bounds the endpoint oscillation by its amplitude, (6.25), and never expands the phase.
  - (6.27) shows the accumulated phase explicitly, as an order estimate. The v2 estimate is recovered only for $`\lambda_1\lesssim\Lambda`$.
  - The error is additive, including the record-induced part that does not depend on $`F`$.
- **I2: Accepted and fixed in Step 6c, and in the last bullet of Step 7.** Position–clock entanglement and level-dependent scalar position dynamics are now distinguished; body E at a fixed level is named as an example of the second without the first.

## Setup and assumptions

**Inputs** (as quoted in question.md).
- (2.9), (2.12) of 02-clock: a uniform ring clock with tick $`\lambda_0`$ and $`\theta_m=0`$ has $`e^{-iC_K\lambda_0}=S`$ and $`C_K=\sum_k\frac{2\pi\ell_k}{N\lambda_0}\lvert f_k\rangle\langle f_k\rvert`$ with $`\ell_k\equiv k`$. Its spread is minimal iff the $`\ell_k`$ are $`N`$ consecutive integers.
- (5.10) of 03-ilang-space/05-recording-contract: $`\lvert u_h\rangle=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$, and $`g(v,w)=\mathrm{Re}\langle v\vert w\rangle`$.
- (17.15) of 03-ilang-space/17-motion: for $`K_{h_m}=mX`$, $`u_{h_m}=m\,e`$ with $`e=(X-\langle X\rangle)\chi`$, $`\lVert e\rVert=\sigma_X>0`$, $`\bar x=\bar m\,e`$ and $`d_0(h_m,h_n)=\lvert m-n\rvert\sigma_X`$.
- (20.10) of 03-ilang-space/20-cost-and-mass: for a uniform gradient, $`a(0)=a_0+\mu F`$ with $`\mu=-\sum_{\{h,h'\}\in E}L_{hh'}(0)\,\Delta_{hh'}\,g(\Delta_{hh'},\cdot)`$, where $`L_{hh'}(0)=2\mathrm{Re}[t_{hh'}\phi_h^*\phi_{h'}]`$ and $`\Delta_{hh'}=u_h-u_{h'}`$.

**Setting.** As in question.md:
- a body $`b`$, the only instance of its type, and a medium $`c`$;
- the contract $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, with $`K_h`$ depending only on the position label $`x_h`$;
- a product start $`\phi\otimes\chi`$, $`\lambda\ge0`$, and contracts that do not depend on $`\lambda`$.

Notation: $`\hat x:=\sum_hx_h\lvert h\rangle\langle h\rvert`$ on $`\mathcal H_b`$ and $`\bar m:=\sum_hx_h\,p_h`$. Clock places are labelled $`a\in\mathbb Z_N`$; these are the $`\lvert m\rangle`$ of 02-clock.

**Chains and limits (A1).**
- *Chain.* Model D, and the chain bodies of Step 6, are taken on $`x\in\{-L,\dots,L\}`$. The hopping terms act only between neighbours of the chain; every term diagonal in $`x`$ (on-site blocks, gradient, records) is unchanged.
- *Starts.* Compactly supported: $`\phi_h=0`$ for $`\lvert x_h\rvert>W`$, with $`W<L`$.
- *Propagation bound (standard).* The hopping part is nearest-neighbour with norm $`\le\tau`$ (Model D; $`2\lvert t\rvert`$ in Step 6), and every other term of $`C`$ is diagonal in $`x`$. Expand the evolution in powers of the hopping, in the interaction picture of the diagonal part. The terms of order $`n<L-W`$ are the same on the chain and on $`\mathbb Z`$, and the part of $`\Psi(\lambda)`$ at distance $`>r`$ from the support of the start has norm $`\le\sum_{n>r}(\tau\lambda)^n/n!\le(e\tau\lambda/r)^r`$.
- *Limit 1: $`L\to\infty`$*, at fixed start, $`F`$, $`\kappa`$ and $`\lambda\le\lambda_{\max}`$. The chain state converges in norm to the state on $`\mathbb Z`$, and the weighted tails $`\sum_{\lvert x\rvert>W+r}\lvert x\rvert^jp_x`$, $`j=1,2`$, are bounded by the same superexponentially small terms. Hence $`\bar m`$, $`\dot{\bar m}`$ and $`\ddot{\bar m}`$ converge uniformly on $`[0,\lambda_{\max}]`$. A vanishing tail weight alone would not give the convergence of $`\bar m`$; the compact support is what is used.
- *Limit 2: concentration*, $`W\to\infty`$ (Step 5c), taken after limit 1 at fixed $`\lambda_1`$, $`\Lambda`$, $`F`$, $`\kappa`$.
- *Then* first order in $`F`$ and leading order in $`\kappa`$, and last the long-interval limit $`M_k\Lambda\to\infty`$ (Steps 5e, 5f). The exact bounds (6.25) and (6.26) hold after limits 1 and 2, at finite $`F`$ and $`\kappa`$.

On $`\mathbb Z`$, the plane waves are $`\lvert p\rangle=\sum_xe^{ipx}\lvert x\rangle`$ with $`p\in(-\pi,\pi]`$, and $`\Phi(x)=\int\frac{dp}{2\pi}e^{ipx}\tilde\Phi(p)`$. In this representation $`\hat S:=\sum_x\lvert x+1\rangle\langle x\rvert`$ acts as $`e^{-ip}`$ and $`\hat x`$ acts as $`i\partial_p`$.

**Approximations, used in item 3 and Step 6 only.**
- (W) Weak records: Step 5a, and the record terms of (6.26), (6.27) in Step 5e.
- (F) First order in the force: Steps 5d–5f and 6.
- (Cst) Start concentrated at $`p_0=0`$: Step 5c.

Their ranges of validity are stated in (6.14), (6.26) and (6.27).

## Derivation

### Step 1. The coefficient (20.10) for any diagonal and any start

Let $`\Pi_h:=\lvert h\rangle\langle h\rvert\otimes\mathbb 1_c`$. Then $`p_h=\langle\Psi\vert\Pi_h\vert\Psi\rangle`$, and (1.9) gives $`\ddot p_h(0)=-\langle[C,[C,\Pi_h]]\rangle_{\Psi(0)}`$.

Split $`C=C_{\rm d}+C_{\rm o}`$ with $`C_{\rm d}:=\sum_h\Pi_hC\Pi_h`$. Since $`[C_{\rm d},\Pi_h]=0`$,
```math
a(0)=-\sum_hu_h\langle[C_{\rm o},[C_{\rm o},\Pi_h]]+[C_{\rm d},[C_{\rm o},\Pi_h]]\rangle .
```
This is affine in $`C_{\rm d}`$, hence in the entries $`t_{hh}`$. Its linear part depends only on $`C_{\rm o}`$ and on the start, not on the base values of the $`t_{hh}`$.

Change $`t_{hh}\to t_{hh}+\delta_h`$ with $`\delta_h-\delta_{h'}=-g(F,\Delta_{hh'})`$. From a base with all $`\Omega_h`$ equal this is the uniform gradient of 20, and by (20.10) $`a(0)`$ changes by $`\mu F`$. By affinity the change is the same from any base:
```math
a(0)\big|_{t_{hh}+\delta_h}=a(0)\big|_{t_{hh}}+\mu F,\qquad \mu\ \text{as in (20.10) of 03-ilang-space/20-cost-and-mass}.
\qquad\text{(6.1)}
```
Both sides of (6.1) are polynomials in the start amplitudes. The identity therefore extends by continuity from starts with all $`\phi_h\neq0`$ to every start.

Model D and the bodies of Step 6 need both extensions: their diagonals are not uniform, and the starts used have zero amplitudes.

### Step 2. Item 1: a body with internal labels

For $`h=(x,a)`$ and $`h'=(x',a')`$ we have $`t_{hh'}=\langle a\vert T_{xx'}\vert a'\rangle`$ and $`\phi_h=(\phi_x)_a`$. Since $`K_h`$ depends only on $`x`$, (5.10) gives $`u_h=u_x`$. Hence $`\Delta_{hh'}=\Delta_{xx'}:=u_x-u_{x'}`$, which vanishes for $`x=x'`$.

Inserting this into (20.10):
```math
L_{hh'}(0)=2\mathrm{Re}\bigl[(\phi_x)_a^*\langle a\vert T_{xx'}\vert a'\rangle(\phi_{x'})_{a'}\bigr],\qquad
L_{xx'}(0):=\sum_{a,a'}L_{(x,a)(x',a')}(0)=2\mathrm{Re}\langle\phi_x\vert T_{xx'}\vert\phi_{x'}\rangle .
\qquad\text{(6.2)}
```
Pairs with $`t_{hh'}=0`$ add zero, so the sum may run over all $`a,a'`$. Then
```math
\mu=-\sum_{\{x,x'\},\,x\neq x'}L_{xx'}(0)\,\Delta_{xx'}\,g(\Delta_{xx'},\cdot\,).
\qquad\text{(6.3)}
```
Edges between places with the same $`x`$ carry edge cost, but they have $`\Delta_{hh'}=0`$ and do not contribute.

**Decoupled body** ($`T_{xx'}=t_{xx'}\mathbb 1_N`$ for $`x\neq x'`$, arbitrary $`T_{xx}`$, also position-dependent). For the start $`\phi_X\otimes\eta`$ with $`\lVert\eta\rVert=1`$, we have $`\phi_x=\phi_X(x)\eta`$ and $`L_{xx'}(0)=2\mathrm{Re}[t_{xx'}\phi_X(x)^*\phi_X(x')]`$. Hence
```math
\mu=-\sum_{\{x,x'\},\,x\neq x'}2\mathrm{Re}\bigl[t_{xx'}\phi_X(x)^*\phi_X(x')\bigr]\,\Delta_{xx'}\,g(\Delta_{xx'},\cdot\,).
\qquad\text{(6.4)}
```
This is the value of (20.10) for the body without internal labels, with hopping $`t_{xx'}`$ and start $`\phi_X`$. By (6.1) it holds for every choice of the $`T_{xx}`$, and it depends neither on $`\eta`$ nor on the $`T_{xx}`$.

### Step 3. Model D: clock, branches, rest cost, positions, gradient

**Clock.** $`S\lvert f_k\rangle=e^{-2\pi ik/N}\lvert f_k\rangle=e^{-id_k\lambda_0}\lvert f_k\rangle`$, so $`e^{-iD\lambda_0}=S`$. By (2.9), $`D`$ is the uniform ring clock with $`\theta_m=0`$ and $`\ell_k=k`$; by (2.12) with $`c=0`$, its spread is minimal. On branch $`s`$ it enters as $`(\sigma_3)_{ss}D`$.

In the place basis, use $`\sum_{j=0}^{N-1}jz^j=N/(z-1)`$ for $`z^N=1\neq z`$ (the derivative of the geometric sum):
```math
D_{aa}=\frac{\pi(N-1)}{N\lambda_0},\qquad D_{aa'}=\frac{2\pi}{N\lambda_0}\,\frac{1}{e^{2\pi i(a-a')/N}-1}\neq0\quad(a\neq a').
\qquad\text{(6.5)}
```

**Branches.** Every term of $`C_b`$, and also $`\hat x`$, commutes with $`\mathbb 1\otimes\mathbb 1\otimes\lvert f_k\rangle\langle f_k\rvert`$, so the clock level $`k`$ is conserved. On level $`k`$, $`A`$ acts on $`\lvert p\rangle\otimes v`$ as $`\frac\tau2(-ie^{-ip}+ie^{ip})\sigma_1=-\tau\sin p\,\sigma_1`$:
```math
C_b\bigl(\lvert p\rangle\otimes v\otimes\lvert f_k\rangle\bigr)=\lvert p\rangle\otimes C_k(p)v\otimes\lvert f_k\rangle,\qquad
C_k(p)=-\tau\sin p\,\sigma_1+M_k\sigma_3,
\qquad\text{(6.6)}
```
with eigenvalues $`\pm\omega_k(p)`$, $`\omega_k(p)=\sqrt{M_k^2+\tau^2\sin^2p}`$.

**Rest cost.** $`C_k(0)=M_k\sigma_3`$, so
```math
M_k:=m+d_k=m+\frac{2\pi k}{N\lambda_0}\ \ (\text{rest cost of level }k,\ \text{eigenvector }\lvert1\rangle),\qquad\text{gap }2M_k,\qquad \omega_k''(0)=\frac{\tau^2}{M_k}.
\qquad\text{(6.7)}
```

**Positions and gradient.**
- $`K_x=\kappa xX`$ is (17.15) with $`X`$ replaced by $`\kappa X`$. Hence $`u_{(x,s,a)}=\kappa x\,e`$, $`\bar x=\kappa\bar m\,e`$ and $`\Delta_{hh'}=\kappa(x-x')e`$.
- The record means $`\epsilon_h=\kappa x\langle X\rangle`$ depend on position. Let $`F`$ be the force of the uniform gradient of $`\delta_h+\epsilon_h`$, where $`\delta_h`$ is the change of $`t_{hh}`$.
- $`F=0`$ thus means that the $`\delta_h`$ cancel the record means, the analogue of "all $`\Omega_h`$ equal" in 20. The $`B`$-diagonal is the same at every $`x`$ and does not enter, by Step 1.

Then
```math
\delta_h+\epsilon_h=-\mathcal F\,x+\text{const},\qquad \mathcal F:=\kappa\,g(e,F),\qquad \bar x=\kappa\,\bar m\,e .
\qquad\text{(6.8)}
```
Only $`g(e,F)`$ enters, as in (20.10). If $`F`$ is meant as the force of the $`\delta_h`$ alone, replace $`\mathcal F`$ by $`\mathcal F-\kappa\langle X\rangle`$; the coefficients of $`F`$ below are unchanged.

### Step 4. Item 2: response at $`\lambda=0`$

The start has the amplitudes $`\phi_{(x,s,a)}=\phi_X(x)\,\delta_{s1}\,N^{-1/2}e^{2\pi ika/N}`$. The edges of $`C_b`$ are as follows; the records, $`m\mathbb 1`$ and the gradient are diagonal.
- **(A)** $`\{(x,s,a),(x+1,s',a)\}`$ with $`s\neq s'`$, and $`t_{(x+1,s',a),(x,s,a)}=-i\tau/2`$.
- **(B)** $`\{(x,s,a),(x,s,a')\}`$ with $`a\neq a'`$, and $`t=(\sigma_3)_{ss}D_{aa'}`$, which is nonzero by (6.5).

Every (A)-edge, and every (B)-edge with $`s=2`$, has an end with $`s=2`$, where $`\phi=0`$; there $`L_{hh'}(0)=0`$.

On the (B)-edges with $`s=1`$, let $`n:=a-a'`$ and $`\vartheta:=2\pi n/N`$. Since $`\mathrm{Re}[e^{-ik\vartheta}/(e^{i\vartheta}-1)]=-\sin((k+\tfrac12)\vartheta)/(2\sin\tfrac\vartheta2)`$,
```math
L_{(x,1,a)(x,1,a')}(0)=-\frac{2\pi}{N^2\lambda_0}\,\lvert\phi_X(x)\rvert^2\,\frac{\sin\bigl((2k+1)\pi n/N\bigr)}{\sin(\pi n/N)},\qquad L_{hh'}(0)=0\ \text{on all other edges.}
\qquad\text{(6.9)}
```
The (B)-edges lie inside one point and do not enter (6.3). On the (A)-blocks, $`L_{x,x+1}(0)=2\mathrm{Re}[\phi_X(x)^*\phi_X(x+1)\,\tfrac{i\tau}{2}\langle1\vert\sigma_1\vert1\rangle]=0`$. Hence
```math
\mu=0\qquad\text{for every }\phi_X,\ k,\ N,\ \tau,\ m,\ \kappa .
\qquad\text{(6.10)}
```

### Step 5. Item 3: averaged response

**5a. Records (W).** $`C`$ contains $`c`$ only through $`\hat x\otimes X`$, so $`X`$ is conserved. Decompose $`\chi=\sum_\xi\Pi_\xi\chi`$ over the eigenspaces of $`X`$, with weights $`w_\xi:=\lVert\Pi_\xi\chi\rVert^2`$. The view of $`b`$ is then exactly the $`w_\xi`$-mixture of the pure evolutions by $`C_b-\mathcal F_\xi\hat x`$ (+const), with
```math
\mathcal F_\xi:=\mathcal F-\kappa(\xi-\langle X\rangle),\qquad \sum_\xi w_\xi\mathcal F_\xi=\mathcal F,\qquad \sum_\xi w_\xi(\mathcal F_\xi-\mathcal F)^2=\kappa^2\sigma_X^2 .
\qquad\text{(6.11)}
```
The part of $`\ddot{\bar m}`$ that is linear in the sector force sums exactly to its value at $`\mathcal F`$, as for the single evolution by $`C_b-\mathcal F\hat x`$. The weak-record approximation drops the terms of higher order in the $`\mathcal F_\xi`$; their size is given in (6.26) and (6.27). It is used nowhere else.

**5b. Equations of motion.** By (1.9), $`\frac{d}{d\lambda}\langle O\rangle=\langle i[C,O]\rangle`$. In the $`p`$-representation on level $`k`$, $`[f(p),\hat x]=-if'(p)`$. Hence $`\hat v:=i[C_k-\mathcal F\hat x,\hat x]=\partial_pC_k`$ and $`[\hat x,\hat v]=i\partial_p\hat v`$, so that
```math
\dot{\bar m}=\langle\hat v\rangle,\quad \hat v=-\tau\cos\hat p\,\sigma_1;\qquad
\ddot{\bar m}=\langle\hat a_k\rangle,\quad \hat a_k=i[C_k,\hat v]-i\mathcal F[\hat x,\hat v]=2\tau M_k\cos\hat p\,\sigma_2+\mathcal F\tau\sin\hat p\,\sigma_1 .
\qquad\text{(6.12)}
```

**5c. Drift and concentrated start (Cst).**
- With $`\hat x=i\partial_p`$, (1.9) reads $`(\partial_\lambda+\mathcal F\partial_p)\tilde\Phi=-iC_k(p)\tilde\Phi`$.
- Along $`p=q+\mathcal F\lambda`$ this gives $`\tilde\Phi(q+\mathcal F\lambda,\lambda)=w_q(\lambda)`$ with $`i\dot w_q=C_k(q+\mathcal F\lambda)w_q`$. This is the standard drift $`\dot p=\mathcal F`$ of the plane-wave label.
- Hence $`\ddot{\bar m}(\lambda)=\int\frac{dq}{2\pi}\,w_q^\dagger\,\hat a_k(q+\mathcal F\lambda)\,w_q`$.
- *Start.* $`\phi^{(W)}=\phi_X^{(W)}\otimes\lvert1\rangle\otimes\lvert f_k\rangle`$ with $`\phi_X^{(W)}(x)=c_W\varphi(x/W)`$, where $`\varphi`$ is smooth with support in $`[-1,1]`$ and $`c_W`$ normalizes. Then $`w_q(0)=\tilde\phi_W(q)\lvert1\rangle`$ and $`\lvert\tilde\phi_W(q)\rvert^2\frac{dq}{2\pi}\to\delta(q)`$ for $`W\to\infty`$: the start is concentrated at $`p_0=0`$.
- *Branch.* The real eigenvector of the positive branch is $`\lvert+_k(q)\rangle=\lvert1\rangle+O(\tau q/M_k)`$, by (6.7). The start therefore lies in the positive branch up to a part of norm $`O(\tau/(M_kW))`$. The start $`\tilde\phi_W(q)\lvert+_k(q)\rangle`$, exactly in the positive branch, differs from it by the same amount and has the same limit, because $`\hat a_k`$ is bounded.
- *Limit 2.* The integrand is $`\lvert\tilde\phi_W(q)\rvert^2`$ times a function of $`q`$ that is continuous and bounded, uniformly on bounded $`\lambda`$-intervals. For $`W\to\infty`$ the integral tends to the value of the two-level problem $`i\dot w=C_k(\mathcal F\lambda)w`$ with $`w(0)=\lvert1\rangle`$.

**5d. First order (F).** $`C_k(\mathcal F\lambda)=M_k\sigma_3-\tau\mathcal F\lambda\,\sigma_1+O(\mathcal F^3)`$. To first order, $`w_1=e^{-iM_k\lambda}`$ and $`w_2=e^{iM_k\lambda}\gamma`$, with $`\dot\gamma=i\tau\mathcal F\lambda\,e^{-2iM_k\lambda}`$ and $`\gamma(0)=0`$. Then
```math
\langle\sigma_2\rangle=2\mathrm{Im}(w_1^*w_2)=2\tau\mathcal F\int_0^\lambda\lambda'\cos\bigl(2M_k(\lambda-\lambda')\bigr)d\lambda'=\tau\mathcal F\sin^2(M_k\lambda)/M_k^2 .
```
The term $`\mathcal F\tau\sin(\mathcal F\lambda)\langle\sigma_1\rangle`$ is $`O(\mathcal F^2)`$.

Also $`a_0(\lambda)=0`$ at leading order in $`\kappa`$: at $`F=0`$ the state stays in the positive branch, and $`\langle+\vert\sigma_2\vert+\rangle=0`$ for real vectors. Using (6.12) and $`\bar x=\kappa\bar m e`$:
```math
a(\lambda)=\frac{2\tau^2}{M_k}\,\sin^2(M_k\lambda)\;\kappa^2\,g(e,F)\,e+O(F^2)\qquad(\text{fixed }\lambda).
\qquad\text{(6.13)}
```
The solution of the two-level problem is analytic in $`\mathcal F`$ at fixed $`\lambda`$, so the coefficient of $`F`$ in (6.13) is exact for every fixed $`\lambda\ge0`$.

**5e. Average.** Let $`0\le\lambda_1<T:=\lambda_1+\Lambda`$ and $`\overline{(\cdot)}:=\frac1\Lambda\int_{\lambda_1}^{T}(\cdot)\,d\lambda`$. Everything in 5e holds after limits 1 and 2. By 5a and 5c, $`\bar m=\sum_\xi w_\xi\,\bar m_{\mathcal F_\xi}`$, where $`\bar m_f`$ is the mean label of the two-level problem $`i\dot w=C_k(f\lambda)w`$, $`w(0)=\lvert1\rangle`$, so that $`\dot{\bar m}_f=w^\dagger\hat v(f\lambda)\,w`$. Two exact properties:
- $`\dot{\bar m}_f(\lambda)`$ is entire in $`f`$, because the equation is linear with coefficients entire in $`f`$;
- it is odd in $`f`$, because $`\sigma_3C_k(q)\sigma_3=C_k(-q)`$, $`\sigma_3\hat v(q)\sigma_3=-\hat v(-q)`$ and $`\sigma_3\lvert1\rangle=\lvert1\rangle`$.

**(i) Coefficient of $`F`$ at a fixed interval (exact).** By 5d, $`\ddot{\bar m}_f=\frac{2\tau^2}{M_k}\sin^2(M_k\lambda)\,f+O(f^3)`$. With (6.11), the part of $`\overline{\ddot{\bar m}}`$ that is linear in the sector forces is $`\frac{\tau^2}{M_k}(1-\rho)\,\mathcal F`$, where
```math
\rho:=\frac{\sin(2M_kT)-\sin(2M_k\lambda_1)}{2M_k\Lambda},\qquad \lvert\rho\rvert\le\frac{1}{M_k\Lambda},\qquad \overline{2\sin^2(M_k\lambda)}=1-\rho .
\qquad\text{(6.24)}
```
At first order in $`F`$ and leading order in $`\kappa`$, the coefficient of $`F`$ in $`\overline a`$ is therefore exactly $`\frac{\tau^2}{M_k}(1-\rho)\,\kappa^2e\,g(e,\cdot)`$, for every interval and every $`\lambda_1\ge0`$.

**(ii) Finite $`F`$ and $`\kappa`$ (exact bound).** Exactly, $`\overline{\ddot{\bar m}_f}=[\dot{\bar m}_f(T)-\dot{\bar m}_f(\lambda_1)]/\Lambda`$.

*Following of the branch.* Write $`C_k(q)=\omega_k\,\vec y\cdot\vec\sigma`$ with the unit vector $`\vec y(q)=(-\sin\Theta,0,\cos\Theta)`$, $`\tan\Theta=\tau\sin q/M_k`$, and let $`\vec z:=w^\dagger\vec\sigma\,w`$, a unit vector with $`\vec z(0)=\vec y(0)`$. By (1.9), $`\dot{\vec z}=2\omega_k\,\vec y\times\vec z`$. With $`\hat v=\partial_qC_k`$ and $`\vec y_\perp:=\partial_\Theta\vec y`$, at $`q=f\lambda`$:
```math
\dot{\bar m}_f=\omega_k'\,(\vec y\cdot\vec z)+\omega_k\Theta'\,(\vec y_\perp\cdot\vec z),\qquad \omega_k\Theta'=\frac{\tau M_k\cos q}{\omega_k},\qquad \omega_k'=\frac{\tau^2\sin q\cos q}{\omega_k}.
```
- In the frame that turns with $`\vec y`$ about the 2-axis, at the rate $`\dot\Theta=f\Theta'`$, $`\vec z`$ precesses about an axis that is tilted from $`\vec y`$ towards the 2-axis by the angle $`\zeta`$, with $`\tan\zeta=\lvert\dot\Theta\rvert/(2\omega_k)=\lvert f\rvert\tau M_k\lvert\cos q\rvert/(2\omega_k^3)`$.
- Precession does not change the angle $`\alpha`$ between $`\vec z`$ and this axis; only the motion of the axis does. Hence $`\lvert\dot\alpha\rvert\le\lvert\dot\zeta\rvert`$.
- For $`\lvert q\rvert\le\pi/2`$, $`\zeta`$ decreases from $`\zeta(0)\le\lvert f\rvert\tau/(2M_k^2)`$, and $`\alpha(0)=\zeta(0)`$. Hence $`\alpha\le2\zeta(0)-\zeta`$, and the angle $`\beta`$ between $`\vec z`$ and $`\vec y`$ obeys $`\beta\le\alpha+\zeta\le\lvert f\rvert\tau/M_k^2`$.

With $`\lvert\omega_k'\rvert\le\tau`$, $`\lvert\omega_k\Theta'\rvert\le\tau`$, $`1-\vec y\cdot\vec z\le\beta^2/2`$ and $`\lvert\vec y_\perp\cdot\vec z\rvert\le\beta`$:
```math
\bigl\lvert\dot{\bar m}_f(\lambda)-\omega_k'(f\lambda)\bigr\rvert\le\frac{\lvert f\rvert\tau^2}{M_k^2}\Bigl(1+\frac{\lvert f\rvert\tau}{2M_k^2}\Bigr)\qquad\text{for }\lvert f\rvert\lambda\le\frac\pi2 .
\qquad\text{(6.25)}
```
The oscillating part of the velocity is bounded by its amplitude. The bound does not use the phase of the oscillation, so it contains no term that grows with $`\lambda`$.

*Branch velocity.* By the mean value theorem, $`[\omega_k'(fT)-\omega_k'(f\lambda_1)]/\Lambda=f\,\omega_k''(q^*)`$ with $`\lvert q^*\rvert\le\lvert f\rvert T`$. From $`\omega_k''=(\tau^2\cos2q-\omega_k'^2)/\omega_k`$, with $`1-\cos2q\le2q^2`$, $`0\le\frac1{M_k}-\frac1{\omega_k}\le\frac{\tau^2q^2}{2M_k^3}`$ and $`\omega_k'^2/\omega_k\le\tau^4q^2/M_k^3`$:
```math
\Bigl\lvert\omega_k''(q)-\frac{\tau^2}{M_k}\Bigr\rvert\le\frac{\tau^2}{M_k}\,\Gamma_k\,q^2,\qquad \Gamma_k:=2+\frac{3\tau^2}{2M_k^2}.
```

*Sum over the sectors.* Define $`\mathcal E`$ by the first equation of (6.14); the linear parts sum to $`\mathcal F`$ by (6.11):
```math
\overline{a}=\frac{\tau^2}{M_k}\,\kappa\,\bigl[\mathcal F+\mathcal E\bigr]\,e=\frac{\tau^2}{M_k}\,\kappa^2\,g(e,F)\,e+\frac{\tau^2}{M_k}\,\kappa\,\mathcal E\,e,\qquad
\frac{1}{2M_k}\ll\Lambda,\qquad \mathcal F_{\max}\,T\ll\min\Bigl(1,\frac{M_k}{\tau}\Bigr),
\qquad\text{(6.14)}
```
with $`\mathcal F_{\max}:=\max_\xi\lvert\mathcal F_\xi\rvert`$ and $`\Sigma_j:=\sum_\xi w_\xi\lvert\mathcal F_\xi\rvert^j`$. The three estimates above give
```math
\lvert\mathcal E\rvert\le\Gamma_k\,T^2\,\Sigma_3+\frac{2}{M_k\Lambda}\Bigl(\Sigma_1+\frac{\tau}{2M_k^2}\,\Sigma_2\Bigr)\qquad\text{for every }0\le\lambda_1<T\text{ with }\mathcal F_{\max}T\le\frac\pi2 ,
\qquad\text{(6.26)}
```
where $`\Sigma_2=\mathcal F^2+\kappa^2\sigma_X^2`$ by (6.11), $`\Sigma_1\le\Sigma_2^{1/2}`$ and $`\Sigma_3\le\mathcal F_{\max}\Sigma_2`$.

**(iii) The part beyond first order (order estimate).** Let $`\mathcal N_f`$ be the part of $`\frac{M_k}{\tau^2}\overline{\ddot{\bar m}_f}`$ beyond first order in $`f`$. Exactly, $`\mathcal E=-\rho\,\mathcal F+\mathcal N`$ with $`\mathcal N:=\sum_\xi w_\xi\,\mathcal N_{\mathcal F_\xi}`$. At a fixed interval, $`\mathcal N_f=\mathcal N^{(3)}f^3+O(f^5)`$ by the two properties above, so
```math
\mathcal N=\mathcal N^{(3)}\Bigl[\mathcal F^3+3\mathcal F\kappa^2\sigma_X^2-\kappa^3\bigl\langle(X-\langle X\rangle)^3\bigr\rangle\Bigr]+\dots
```
These are a term of higher order in $`F`$, a record term linear in $`F`$, and a record-induced term that does not depend on $`F`$. All three are additive and of order $`\kappa^3`$ at fixed $`F`$ and fixed interval.

The size of $`\mathcal N`$ on long or late intervals follows from the precession of (ii). To leading order in $`\zeta`$, the oscillating part of $`\dot{\bar m}_f`$ is $`-\frac{f\tau^2}{2M_k^2}\sin\Upsilon_f(\lambda)`$, with the precession phase
```math
\Upsilon_f(\lambda)=\int_0^\lambda\sqrt{4\omega_k^2+\dot\Theta^2}\;d\lambda'=2M_k\lambda+\frac{\tau^2f^2\lambda^3}{3M_k}+\dots
```
Its first order, $`\Upsilon_f\to2M_k\lambda`$, gives the term $`-\rho f`$. The accumulated phase $`\Upsilon_f-2M_k\lambda`$ is not small on late intervals. Under both conditions of (6.14):
```math
\mathcal E=-\rho\,\mathcal F+\mathcal N,\qquad
\mathcal N=O\bigl(\Gamma_kT^2\Sigma_3\bigr)+O\Bigl(\frac{1}{M_k\Lambda}\sum_\xi w_\xi\lvert\mathcal F_\xi\rvert\,\min\Bigl\{1,\frac{\tau^2\mathcal F_\xi^2T^3}{M_k}\Bigr\}\Bigr).
\qquad\text{(6.27)}
```
- The first term is the variation of the branch curvature along the drift.
- The second term is the accumulated interbranch phase at the two ends of the interval. For $`\tau^2f^2T^3\ll M_k`$ its leading form in one sector is $`-\frac{\tau^2f^3}{6M_k^2\Lambda}\bigl[T^3\cos(2M_kT)-\lambda_1^3\cos(2M_k\lambda_1)\bigr]`$. For larger phases it saturates at the endpoint term of (6.26).
- The ratio of the second term to the first is at most of order $`\tau^2T/(\Gamma_kM_k^2\Lambda)`$. For $`\lambda_1\lesssim\Lambda`$ the second term is at most of the order of the first. On late intervals, $`\tau^2T\gg\Gamma_kM_k^2\Lambda`$, it dominates. An estimate $`O(T^2\Sigma_3)`$ alone holds only for $`\lambda_1\lesssim\Lambda`$.

**(iv) Conditions and status.**
- *Exact, for every interval:* the average as velocity change; the first-order coefficient (6.24); the decomposition $`\mathcal E=-\rho\mathcal F+\mathcal N`$, with $`\mathcal N`$ of third order in the sector forces at a fixed interval.
- *Exact inequalities:* (6.25), and (6.26) for every interval with $`\mathcal F_{\max}T\le\pi/2`$. They need no condition on $`\lambda_1`$, on $`\Lambda`$ or on $`\mathcal F_{\max}\tau/M_k^2`$.
- *Order estimate, under both conditions of (6.14):* the estimate of $`\mathcal N`$ in (6.27).
- *First condition*, $`\Lambda\gg1/(2M_k)`$: the interval is long compared with the inverse gap. It makes the endpoint term of (6.26) small, whatever the phases at the two ends.
- *Second condition*, $`\mathcal F_{\max}T\ll\min(1,M_k/\tau)`$: it is the condition for the first-order treatment, and it makes $`\Gamma_k(\mathcal F_{\max}T)^2\ll1`$. The drift $`\mathcal F_\xi\lambda`$ of every sector stays where $`\omega_k''\approx\omega_k''(0)`$. $`T`$ is counted from the start at $`\lambda=0`$, because the drift accumulates from the start: the condition limits the end of the interval, not only its length.
- *Every interval that satisfies both conditions* has $`\lvert\mathcal E\rvert\le\varepsilon_{\rm av}\,\Sigma_1\le\varepsilon_{\rm av}(\mathcal F^2+\kappa^2\sigma_X^2)^{1/2}`$ with $`\varepsilon_{\rm av}:=\Gamma_k(\mathcal F_{\max}T)^2+\frac{2}{M_k\Lambda}\bigl(1+\frac{\mathcal F_{\max}\tau}{2M_k^2}\bigr)\ll1`$. The two conditions together imply $`\mathcal F_{\max}\tau\ll M_k^2`$ (no branch transitions).
- *Records.* The bound is relative to $`\Sigma_1`$, not to $`\lvert\mathcal F\rvert`$. The leading term of (6.14) dominates the value of $`\overline a`$ if in addition $`\varepsilon_{\rm av}\,\kappa\sigma_X\ll\lvert\mathcal F\rvert`$. Otherwise the record-induced part of $`\mathcal E`$ that does not depend on $`F`$ can be comparable. That part vanishes identically if the distribution of $`X`$ in $`\chi`$ is symmetric about $`\langle X\rangle`$, since $`\dot{\bar m}_f`$ is odd. At a fixed interval $`\mathcal N=O(\kappa^3)`$, which is the weak-record regime of the question.
- *Values, not derivatives.* (6.26) bounds the value of $`\overline a`$. It does not bound derivatives with respect to $`F`$ at finite $`F`$ and $`\kappa`$: once the phases $`\Upsilon_{\mathcal F_\xi}`$ differ by more than 1, the derivative of the endpoint term need not be small. The coefficient of $`F`$ is therefore taken at a fixed interval, as in (i).
- Finite-packet corrections vanish in limit 2, which is taken before. The chain limit requires $`L-W\gg\tau T`$.

**5f. Averaged inverse inertia.** $`\mu_{\rm av}(k)`$ is the coefficient of $`F`$ in $`\overline a`$ at first order in $`F`$ and leading order in $`\kappa`$, in the long-interval limit $`M_k\Lambda\to\infty`$. By (6.24), at a fixed interval this coefficient is exactly $`(1-\rho)`$ times the following, and $`\lvert\rho\rvert\le1/(M_k\Lambda)`$ for every $`\lambda_1`$; the limit therefore exists and does not depend on $`\lambda_1`$:
```math
\mu_{\rm av}(k)=\frac{\tau^2}{M_k}\,\kappa^2\,e\,g(e,\cdot\,)=\frac{\tau^2}{m+d_k}\,\kappa^2\,e\,g(e,\cdot\,).
\qquad\text{(6.15)}
```
At finite $`F`$ and $`\kappa`$, (6.14) reads $`\overline a=\mu_{\rm av}(k)F+\frac{\tau^2}{M_k}\kappa\,\mathcal E\,e`$, with $`\mathcal E`$ bounded by (6.26).
```math
M_k\,\mu_{\rm av}(k)=\tau^2\kappa^2\,e\,g(e,\cdot\,)\ \ \text{for every }k,\qquad \frac{M_k}{\tau^2}=\frac{m}{\tau^2}+\frac{2\pi k}{N\lambda_0\,\tau^2}.
\qquad\text{(6.16)}
```
So $`\mu_{\rm av}(k)`$ decreases strictly with $`d_k`$, and it is inversely proportional to the rest cost (6.7).

*Two normalizations of the inertia.* Let $`n:=e/\sigma_X`$, a unit vector of $`(\mathcal H_c,g)`$, and $`d_1:=\kappa\sigma_X`$, the background distance of neighbouring points by (17.15) with $`X\to\kappa X`$. Then $`\bar x=d_1\bar m\,n`$ and $`\mathcal F=d_1\,g(n,F)`$, and
```math
\mu_{\rm av}(k)=\frac{1}{I_k}\,n\,g(n,\cdot\,),\qquad
I_k:=\frac{M_k}{\tau^2\kappa^2\sigma_X^2}=\frac{I_k^{\rm lab}}{d_1^{\,2}},\qquad
I_k^{\rm lab}:=\frac{M_k}{\tau^2}\quad\bigl(\overline{\ddot{\bar m}}=\mathcal F/I_k^{\rm lab}\bigr).
\qquad\text{(6.20)}
```
- $`I_k`$ is the **background inertia**: $`\mu_{\rm av}(k)`$ has the single nonzero eigenvalue $`1/I_k`$, on $`n`$, and vanishes on the $`g`$-orthogonal complement of $`e`$.
- $`I_k^{\rm lab}`$ is the **label inertia**: the response of the dimensionless position label $`\bar m`$ to the label force $`\mathcal F`$.
- Both are proportional to the rest cost $`M_k=m+d_k`$. The clock cost $`d_k`$ adds to each with the same coefficient as the rest term $`m`$.

### Step 6. Decoupled body on the chain

**6a. The whole class.** Take $`x\in\mathbb Z`$ (limits as in the Setup), $`T_{x+1,x}=t\mathbb 1_N`$ with $`t\neq0`$, and arbitrary self-adjoint on-site blocks $`T_{xx}`$; records and gradient as in (6.8). Let
```math
\omega(p):=te^{-ip}+t^*e^{ip},\qquad V:=\sum_x\lvert x\rangle\langle x\rvert\otimes T_{xx},\qquad G_x:=T_{x+1,x+1}-T_{xx},
```
so that $`C_b=\omega(\hat p)\otimes\mathbb 1_N+V`$ with $`\omega(\hat p)=t\hat S+t^*\hat S^\dagger`$. Since $`V`$ commutes with $`\hat x`$, the steps of 5b give $`\hat v=i[C_b-\mathcal F\hat x,\hat x]=\omega'(\hat p)=-it\hat S+it^*\hat S^\dagger`$. With $`[V,\hat S]=\sum_x\lvert x+1\rangle\langle x\rvert\otimes G_x`$:
```math
\hat v=\omega'(\hat p)\otimes\mathbb 1_N,\qquad
\ddot{\hat x}=\mathcal F\,\omega''(\hat p)+\hat a_{\rm free},\qquad
\hat a_{\rm free}:=i[V,\hat v]=\sum_x\bigl(t\,\lvert x+1\rangle\langle x\rvert+t^*\lvert x\rangle\langle x+1\rvert\bigr)\otimes G_x .
\qquad\text{(6.21)}
```
Step 5a applies to the whole class, since it uses only that $`c`$ enters through $`\hat x\otimes X`$. For the start $`\phi_X\otimes\eta`$, (6.21) gives the following.
- **At $`\lambda=0`$.** The state does not depend on $`\mathcal F`$, and $`\hat a_{\rm free}`$ does not contain $`\mathcal F`$. The coefficient of $`F`$ in $`a(0)`$ is therefore $`\kappa^2\langle\phi_X\vert\omega''(\hat p)\vert\phi_X\rangle\,e\,g(e,\cdot)`$. By (6.2), $`\langle\omega''(\hat p)\rangle_0=-2\sum_x\mathrm{Re}[t^*\phi_X(x)^*\phi_X(x+1)]=-\sum_xL_{x,x+1}(0)`$, and $`\Delta_{x,x+1}=-\kappa e`$: this is $`\mu`$ of (6.4), for every choice of the $`T_{xx}`$. Only $`a_0=\kappa\langle\hat a_{\rm free}\rangle_0\,e`$ depends on $`\eta`$ and on the $`T_{xx}`$.
- **At $`\lambda>0`$.** The coefficient of $`\mathcal F`$ in $`\ddot{\bar m}(\lambda)`$ is $`\langle\omega''(\hat p)\rangle_\lambda+\partial_{\mathcal F}\langle\hat a_{\rm free}\rangle_\lambda`$, taken at $`\mathcal F=0`$.
- **Criterion.** Since $`t\neq0`$, $`\hat a_{\rm free}=0`$ iff $`G_x=0`$ for all $`x`$, i.e. iff the on-site blocks are the same at every position. Exactly then the velocity commutes with $`C_b`$.

**6b. Uniform on-site blocks.** Let $`T_{xx}=D'`$ for all $`x`$, with any self-adjoint clock term $`D'`$. Then $`\hat a_{\rm free}=0`$ and
```math
C_b-\mathcal F\hat x=(\omega(\hat p)-\mathcal F\hat x)\otimes\mathbb 1_N+\mathbb 1\otimes D' .
```
The two parts commute, and $`\bar m`$ involves only the first. By (6.21), $`\ddot{\hat x}=\mathcal F\omega''(\hat p)`$ exactly, and $`\frac{d}{d\lambda}\omega''(\hat p)=\mathcal F\omega'''(\hat p)`$ with $`\lVert\omega'''(\hat p)\rVert\le2\lvert t\rvert`$. Applied in each sector of 5a and summed with (6.11), this gives exactly
```math
\bigl\lvert\ddot{\bar m}(\lambda)-\mathcal F\,\langle\omega''(\hat p)\rangle_0\bigr\rvert\le2\lvert t\rvert\,\lambda\,\bigl(\mathcal F^2+\kappa^2\sigma_X^2\bigr).
```
The response does not oscillate. At first order in $`F`$ and leading order in $`\kappa`$ its coefficient is the same at every $`\lambda`$, hence equal to its average over every interval; no condition of the first kind in (6.14) is needed. So
```math
\mu_{\rm av}=\mu=\kappa^2\,\langle\phi_X\vert\omega''(\hat p)\vert\phi_X\rangle\,e\,g(e,\cdot\,)\ \xrightarrow{\ \text{concentrated at }p_0\ }\ -2\mathrm{Re}\bigl(t^*e^{ip_0}\bigr)\,\kappa^2\,e\,g(e,\cdot\,).
\qquad\text{(6.17)}
```
This is independent of the clock level, of $`\eta`$ and of $`D'`$.

**6c. Position-dependent on-site blocks.** Now $`G_x\neq0`$ for some $`x`$.
- *What holds.* (6.4): $`\mu`$ is the same as in 6b and depends neither on $`\eta`$ nor on the $`T_{xx}`$. Also (6.21) and Step 5a hold.
- *What fails.* $`[C_b,\hat v]=0`$, the constancy of the response in $`\lambda`$, and with them the argument for $`\mu_{\rm av}=\mu`$.
- *Scalar differences*, $`T_{xx}=D'+\nu_x\mathbb 1_N`$. The factorization of 6b persists with $`\omega(\hat p)`$ replaced by $`\omega(\hat p)+\nu(\hat x)`$. The response at every $`\lambda`$ is that of the body without internal labels with site costs $`\nu_x`$. It is independent of the clock level, of $`\eta`$ and of $`D'`$, but it need not be constant in $`\lambda`$ or equal to $`\mu`$ (for $`\nu_x=(-1)^xM`$ it is body E below with $`m\mathbb 1_N+D`$ replaced by $`M\mathbb 1_N`$).
- *Common eigenvector.* Let $`\eta`$ be a common eigenvector of all on-site blocks, $`T_{xx}\eta=\nu_x^{(\eta)}\eta`$. Then $`C_b`$ and $`\hat x`$ map the states $`\phi_X\otimes\eta`$ to states of the same form. In every sector of 5a the state stays a product $`\phi_X(\lambda)\otimes\eta`$, and the position evolves as for the body without internal labels with site costs $`\nu_x^{(\eta)}`$. The response depends on $`\eta`$ through these scalars, unless their differences $`\nu_{x+1}^{(\eta)}-\nu_x^{(\eta)}`$ are the same for all $`\eta`$ (scalar differences). The clock level can thus enter the position dynamics without any entanglement between position and clock. Body E below at a fixed level is of this kind, with $`\eta=\lvert f_k\rangle`$ and $`\nu_x^{(\eta)}=(-1)^xM_k`$.
- *General internal start.* If $`\eta`$ is not a common eigenvector, the state need not stay a product: position and internal labels can become entangled, and generically do. This is a possibility for arbitrary internal starts, not a consequence of non-scalar differences alone.
- In both cases the term $`\partial_{\mathcal F}\langle\hat a_{\rm free}\rangle_\lambda`$ can depend on the $`T_{xx}`$ and on $`\eta`$, and no formula for the response in terms of $`t`$ alone holds for the class. The following body shows this.

**Body E.** Let $`t=-\tfrac{i\tau}{2}`$ and $`T_{xx}=(-1)^x(m\mathbb 1_N+D)`$, with records and gradient as in Model D. Define $`J\lvert x\rangle\otimes\lvert a\rangle:=\lvert x\rangle\otimes\lvert s(x)\rangle\otimes\lvert a\rangle`$, with $`s(x)=1`$ for even $`x`$ and $`s(x)=2`$ for odd $`x`$.
- $`A`$ of Model D maps $`\lvert x,s\rangle`$ to $`-\tfrac{i\tau}{2}\lvert x+1,\bar s\rangle+\tfrac{i\tau}{2}\lvert x-1,\bar s\rangle`$, where $`\bar s`$ is the other branch label, and $`\overline{s(x)}=s(x\pm1)`$. $`B`$ multiplies $`\lvert x,s(x)\rangle`$ by $`(-1)^x(m\mathbb 1_N+D)`$. Hence $`C_b^{\rm D}J=JC_b^{\rm E}`$.
- $`J`$ preserves $`x`$, so it also intertwines $`\hat x`$, the gradient and the records. It is a unitary from the places of E onto the places of Model D with $`x+s`$ odd, which span an invariant subspace of $`C`$.
- Therefore the place weights, $`\bar x`$ and $`a(\lambda)`$ of E with start $`\phi`$ are those of Model D with start $`J\phi`$, for all $`\lambda`$, $`F`$ and $`\kappa`$. (The places with $`x+s`$ even carry the body with $`T_{xx}=-(-1)^x(m\mathbb 1_N+D)`$: Model D is the direct sum of two bodies of this class.)

Take the start $`\phi=\phi_X\otimes\lvert f_k\rangle`$ with $`\phi_X(x)\propto\varphi(x/W)`$ on even $`x`$ and $`\phi_X(x)=0`$ on odd $`x`$. In the terms of E, it sits at the plane-wave label $`0`$ of the two-site cell, in the branch of positive eigenvalue $`M_k`$: at this label that branch lives on the even sites. Its image is $`J\phi=\phi_X\otimes\lvert1\rangle\otimes\lvert f_k\rangle`$, a start of item 2.
- *$`\mu`$.* Every edge between points joins an even and an odd site, so $`L_{x,x+1}(0)=0`$ in (6.4). This agrees with (6.10) for $`J\phi`$.
- *$`\mu_{\rm av}`$.* $`\tilde\phi_X(q+\pi)=\tilde\phi_X(q)`$, so $`J\phi`$ is concentrated at $`q\in\{0,\pi\}`$. Since $`\sigma_3C_k(q)\sigma_3=C_k(q+\pi)`$, $`\sigma_3\hat a_k(q)\sigma_3=\hat a_k(q+\pi)`$ and $`\sigma_3\lvert1\rangle=\lvert1\rangle`$, the integrand of 5c has period $`\pi`$ in $`q`$. The limit is the two-level problem of 5d, and Steps 5d–5f hold unchanged.

Hence
```math
\text{body E, level }k:\qquad \mu=0,\qquad \mu_{\rm av}(k)=\frac{\tau^2}{m+d_k}\,\kappa^2\,e\,g(e,\cdot\,)\neq\mu .
\qquad\text{(6.22)}
```
In the class of item 1 with position-dependent $`T_{xx}`$, $`\mu_{\rm av}`$ can thus depend on the clock level and differ from $`\mu`$, although $`\mu`$ itself depends on neither $`\eta`$ nor the $`T_{xx}`$.

### Step 7. Item 4: comparison

```math
\begin{aligned}
&\text{Model D (and body E):}&&\mu=0\neq\mu_{\rm av}(k)=\frac{\tau^2}{M_k}\,\kappa^2e\,g(e,\cdot\,);\\
&\text{decoupled body, }T_{xx}=D'\text{ at every }x:&&\mu=\mu_{\rm av}\quad\text{(6.17), independent of the clock};\\
&\text{decoupled body, }T_{xx}\text{ position-dependent:}&&\text{no general relation; }\mu\neq\mu_{\rm av}\text{ for body E (6.22)}.
\end{aligned}
\qquad\text{(6.23)}
```
Of the two bodies of the question, $`\mu`$ and $`\mu_{\rm av}`$ coincide for the decoupled body, provided its clock term is the same at every position; they differ for Model D.

**Reason.** $`\mu`$ is the coefficient of the term $`-i\mathcal F[\hat x,\hat v]`$ of the acceleration, evaluated in the start; it is fixed by the edge costs between points, which is the content of (20.10). The averaged response contains in addition the response of the free acceleration $`i[C_b,\hat v]`$ to the gradient.
- **Uniform on-site blocks.** The velocity commutes with $`C_b`$, so the free acceleration vanishes identically (6.21). The term $`\mathcal F\omega''(\hat p)`$ is the whole response, already at $`\lambda=0`$. The clock term commutes with position and hopping, and drops out.
- **Model D.** The velocity $`-\tau\cos\hat p\,\sigma_1`$ connects the two branches and does not commute with the term $`\sigma_3\otimes(m\mathbb 1+D)`$ that carries the clock.
  - At $`\lambda=0`$ the $`s=1`$ start has no edge cost between points, which gives (6.10).
  - The response comes from interference between the admixture of the negative branch that the gradient induces, of amplitude $`\propto\mathcal F\tau/M_k^2`$, and the free acceleration $`2\tau M_k\cos\hat p\,\sigma_2`$. It builds up as $`\sin^2(M_k\lambda)`$, and its average is the branch curvature $`\tau^2/M_k`$.
  - The clock cost enters through the gap $`2M_k`$.
- **Position-dependent on-site blocks.** The same mechanism acts through $`G_x\neq0`$ in (6.21). Model D is itself of this kind in each of its two invariant subspaces (body E): the dividing line is whether the term that carries the clock commutes with the velocity. It is neither whether the hopping blocks are multiples of $`\mathbb 1_N`$, nor whether position and clock become entangled (6c).

## Result

- **(6.1)** The inverse inertia $`\mu`$ of (20.10) of 03-ilang-space/20-cost-and-mass is the coefficient of $`F`$ for a uniform gradient added to any diagonal, and for every product start.
- **Item 1.**
  - (6.2): $`L_{hh'}(0)`$ in terms of the blocks, and $`L_{xx'}(0)=2\mathrm{Re}\langle\phi_x\vert T_{xx'}\vert\phi_{x'}\rangle`$.
  - (6.3): $`\mu=-\sum_{x\neq x'}L_{xx'}(0)\Delta_{xx'}g(\Delta_{xx'},\cdot)`$. Edges inside one point do not contribute.
  - (6.4): for the decoupled body, $`\mu`$ depends neither on $`\eta`$ nor on the $`T_{xx}`$, uniform or position-dependent.
- **Item 2 (Model D).**
  - (6.7): rest cost $`M_k=m+d_k`$.
  - (6.9): edge costs at $`\lambda=0`$, nonzero only on the clock edges of branch $`s=1`$.
  - (6.10): $`\mu=0`$.
- **Item 3.**
  - (6.13): $`a(\lambda)=\frac{2\tau^2}{M_k}\sin^2(M_k\lambda)\,\kappa^2g(e,F)e`$ at first order in $`F`$.
  - (6.24), exact for every interval: at first order in $`F`$ and leading order in $`\kappa`$, the coefficient of $`F`$ in the average is $`\frac{\tau^2}{M_k}(1-\rho)\kappa^2e\,g(e,\cdot)`$, with $`\lvert\rho\rvert\le1/(M_k\Lambda)`$.
  - (6.14): the average is $`\frac{\tau^2}{M_k}\kappa^2g(e,F)e+\frac{\tau^2}{M_k}\kappa\,\mathcal E\,e`$, for intervals with $`1/(2M_k)\ll\Lambda`$ (long compared with the inverse gap) and $`\mathcal F_{\max}T\ll\min(1,M_k/\tau)`$ (first-order treatment), where $`T`$ is the end of the interval.
  - (6.25), exact: the velocity differs from the branch velocity by at most $`\frac{\lvert f\rvert\tau^2}{M_k^2}\bigl(1+\frac{\lvert f\rvert\tau}{2M_k^2}\bigr)`$ while $`\lvert f\rvert\lambda\le\pi/2`$.
  - (6.26), exact for every interval with $`\mathcal F_{\max}T\le\pi/2`$ and every $`\lambda_1`$: $`\lvert\mathcal E\rvert\le\Gamma_kT^2\Sigma_3+\frac{2}{M_k\Lambda}\bigl(\Sigma_1+\frac{\tau}{2M_k^2}\Sigma_2\bigr)`$. Under both conditions of (6.14), $`\lvert\mathcal E\rvert\ll\Sigma_1`$.
  - (6.27), order estimate: $`\mathcal E=-\rho\mathcal F+\mathcal N`$, where $`\mathcal N`$ contains the curvature term $`O(\Gamma_kT^2\Sigma_3)`$ and the accumulated-phase term, which exceeds the first on late intervals.
  - (6.15): $`\mu_{\rm av}(k)=\frac{\tau^2}{m+d_k}\kappa^2e\,g(e,\cdot)`$, the coefficient at first order in $`F`$, leading order in $`\kappa`$, in the long-interval limit, for every $`\lambda_1`$.
  - (6.16), (6.20): $`\mu_{\rm av}(k)`$ is inversely proportional to the rest cost. Background inertia $`I_k=M_k/(\tau^2\kappa^2\sigma_X^2)`$, label inertia $`I_k^{\rm lab}=M_k/\tau^2`$; the clock cost $`d_k`$ adds to each like $`m`$.
  - (6.21): for the decoupled chain body with arbitrary $`T_{xx}`$, $`\ddot{\hat x}=\mathcal F\omega''(\hat p)+\hat a_{\rm free}`$, and $`\hat a_{\rm free}=0`$ iff the on-site blocks are uniform.
  - (6.17): for uniform on-site blocks, $`\mu_{\rm av}=\mu=\kappa^2\langle\omega''\rangle e\,g(e,\cdot)`$, independent of the clock level.
  - (6.22): for position-dependent on-site blocks there is no such statement; for body E, $`\mu=0`$ and $`\mu_{\rm av}(k)=\frac{\tau^2}{m+d_k}\kappa^2e\,g(e,\cdot)`$.
- **Item 4, (6.23).** $`\mu`$ and $`\mu_{\rm av}`$ coincide for the decoupled body with uniform on-site blocks, whose velocity commutes with $`C_b`$. They differ for Model D, and for body E, where the term that carries the clock does not commute with the velocity.

## Consistency checks

1. **Dimensions and $`\tau\to0`$.** $`C`$, $`\tau`$, $`m`$, $`d_k`$ and $`\mathcal F`$ have the dimension $`1/[\lambda]`$. $`I_k^{\rm lab}=M_k/\tau^2`$ has the dimension $`[\lambda]`$, so $`\mathcal F/I_k^{\rm lab}`$ has the dimension $`1/[\lambda]^2`$ of $`\ddot{\bar m}`$. $`\mu_{\rm av}F=\frac{\tau^2}{M_k}\,\kappa e\cdot\kappa g(e,F)`$ has the dimension of $`\kappa e/[\lambda]^2`$, that of $`\ddot{\bar x}`$. In (6.26), $`T^2\Sigma_3`$, $`\Sigma_1/(M_k\Lambda)`$ and $`\tau\Sigma_2/(M_k^3\Lambda)`$ have the dimension of $`\mathcal F`$, and $`\Gamma_k`$ is a number. In (6.9), $`2\pi/(N^2\lambda_0)`$ is a cost. As $`\tau\to0`$, $`\hat v=0`$, (6.13), (6.15) and the bound (6.25) vanish and $`I_k\to\infty`$. Passed.
2. **$`\lambda=0`$ by an independent route.** For the item-2 start with any $`\phi_X`$, $`\langle1\vert\sigma_2\vert1\rangle=\langle1\vert\sigma_1\vert1\rangle=0`$ in (6.12) gives $`a(0)=0`$ for every $`F`$. This agrees with (6.10), obtained from (20.10) through edge costs, and with (6.13) at $`\lambda=0`$. For body E, (6.21) gives the same: $`\langle\omega''(\hat p)\rangle_0`$ and $`\langle\hat a_{\rm free}\rangle_0`$ are sums of bond terms $`\phi_X(x)^*\phi_X(x+1)`$, which vanish for $`\phi_X`$ on even sites. Passed.
3. **The bounds (6.25), (6.26) against the first-order solution and the secular term.** Integrating (6.13) gives $`\dot{\bar m}_f=\frac{\tau^2f}{M_k}\lambda-\frac{\tau^2f}{2M_k^2}\sin(2M_k\lambda)+O(f^3)`$, and $`\omega_k'(f\lambda)=\frac{\tau^2f}{M_k}\lambda+O(f^3)`$. The difference has modulus $`\le\frac{\lvert f\rvert\tau^2}{2M_k^2}`$, half the bound (6.25). Accordingly $`\lvert\rho\rvert\le\frac{1}{M_k\Lambda}`$ uses half of the endpoint term $`\frac{2}{M_k\Lambda}`$ of (6.26). The secular term of (6.27) has size at most $`\frac{\tau^2\lvert f\rvert^3T^3}{3M_k^2\Lambda}`$; it fits into the other half, $`\frac{\lvert f\rvert}{M_k\Lambda}`$, iff $`\frac{\tau^2f^2T^3}{3M_k}\le1`$, which is exactly where the expansion of the phase is valid. For a short interval at the start, $`\lambda_1=0`$ and $`M_k\Lambda\ll1`$: $`1-\rho\approx\frac23(M_k\Lambda)^2\to0`$, in agreement with $`a(0)=0`$, and (6.26) allows this because its endpoint term is then large. Passed.

## Open issues

- A ticking clock, i.e. a superposition of levels, is not treated. Since the level is conserved, the averaged response is the level-weighted mean of (6.15); whether this mixture is the inertia of one body is left open.
- (6.26) is exact but not sharp: its endpoint term carries twice the first-order amplitude. (6.27) is an order estimate, without constants. Neither controls derivatives with respect to $`F`$ at finite $`\kappa`$. Both hold for the concentrated start, after limit 2; finite-packet corrections and wide packets are not treated (for wide packets the average is expected to be $`\langle\omega_k''\rangle`$, which is not derived here).
- No statement is made for $`\mathcal F_{\max}T>\pi/2`$ (Bloch oscillation) or for $`\mathcal F_{\max}\tau\gtrsim M_k^2`$ (branch transitions), where (6.25) is not useful.
- Position-dependent on-site blocks: only scalar differences, common eigenvectors and body E are solved. Which position-dependent blocks make $`\mu_{\rm av}`$ depend on the clock level is not classified, and a general member of the class has no gap that fixes the averaging interval.
- Second order in $`\kappa`$ (decoherence by the records, the record-induced acceleration at $`F=0`$) is only bounded by (6.26) and estimated by (6.27), not computed.
- The meaning of $`\tau`$ and of $`d_1\tau`$ as speeds, and of the inertias (6.20), belongs to criteria 4 and 6; it is outside this package (M1, M3).

## Methods used

- Heisenberg equations of motion (double commutators)
- Affine dependence of the acceleration on the diagonal of the contract
- Fourier transform on $`\mathbb Z`$, plane waves, two-branch dispersion
- Method of characteristics (drift of the plane-wave label in a uniform gradient)
- First-order perturbation theory in the force; parity and analyticity in the force
- Bloch-vector precession in a co-rotating frame (exact bound on the following of a branch)
- Averaged acceleration as velocity change over the interval; mean value theorem
- Conserved record observable: exact mixture decomposition of the view
- Invariant subspaces and unitary equivalence (staggered chain and two-branch chain)
- Propagation bound for nearest-neighbour hopping; limit of finite chains
- Geometric sums
