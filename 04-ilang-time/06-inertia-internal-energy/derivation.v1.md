# Inertia and internal energy: response at λ = 0 and averaged response

- **Subproject:** 04-ilang-time
- **Package:** 06-inertia-internal-energy
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-10

## Setup and assumptions

**Inputs** (as quoted in question.md).
- (2.9), (2.12) of 02-clock: a uniform ring clock with tick $`\lambda_0`$ and $`\theta_m=0`$ has $`e^{-iC_K\lambda_0}=S`$ and $`C_K=\sum_k\frac{2\pi\ell_k}{N\lambda_0}\lvert f_k\rangle\langle f_k\rvert`$ with $`\ell_k\equiv k`$. Its spread is minimal iff the $`\ell_k`$ are $`N`$ consecutive integers.
- (5.10) of 03-ilang-space/05-recording-contract: $`\lvert u_h\rangle=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$, and $`g(v,w)=\mathrm{Re}\langle v\vert w\rangle`$.
- (17.15) of 03-ilang-space/17-motion: for $`K_{h_m}=mX`$, $`u_{h_m}=m\,e`$ with $`e=(X-\langle X\rangle)\chi`$, $`\lVert e\rVert=\sigma_X>0`$, and $`\bar x=\bar m\,e`$.
- (20.10) of 03-ilang-space/20-cost-and-mass: for a uniform gradient, $`a(0)=a_0+\mu F`$ with $`\mu=-\sum_{\{h,h'\}\in E}L_{hh'}(0)\,\Delta_{hh'}\,g(\Delta_{hh'},\cdot)`$, where $`L_{hh'}(0)=2\mathrm{Re}[t_{hh'}\phi_h^*\phi_{h'}]`$ and $`\Delta_{hh'}=u_h-u_{h'}`$.

**Setting.** As in question.md:
- a body $`b`$, the only instance of its type, and a medium $`c`$;
- the contract $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, with $`K_h`$ depending only on the position label $`x_h`$;
- a product start $`\phi\otimes\chi`$, $`\lambda\ge0`$, and contracts that do not depend on $`\lambda`$.

Notation: $`\hat x:=\sum_hx_h\lvert h\rangle\langle h\rvert`$ on $`\mathcal H_b`$ and $`\bar m:=\sum_hx_h\,p_h`$. Clock places are labelled $`a\in\mathbb Z_N`$; these are the $`\lvert m\rangle`$ of 02-clock.

**Model D on $`\mathbb Z`$ (A1).**
- Model D is taken on the finite chains $`x\in\{-L,\dots,L\}`$. The terms of $`A`$ act only between neighbours of the chain; $`B`$ and $`K_x`$ are unchanged.
- The start has its position weight in $`\lvert x\rvert\le W`$, up to tails that vanish in the limit.
- $`\lambda`$ stays in a bounded range $`[0,\lambda_{\max}]`$, and the limit $`L\to\infty`$ is taken first.
- The hopping part of $`C_b`$ is nearest-neighbour with norm $`\le\tau`$. By the standard propagation bound, weight therefore spreads over at most $`O(\tau\lambda)`$ sites, up to tails. Hence $`p_x`$, $`\bar m`$ and their $`\lambda`$-derivatives converge to their values on $`\mathbb Z`$ once $`L\gg W+\tau\lambda_{\max}`$.

On $`\mathbb Z`$, the plane waves are $`\lvert p\rangle=\sum_xe^{ipx}\lvert x\rangle`$ with $`p\in(-\pi,\pi]`$, and $`\Phi(x)=\int\frac{dp}{2\pi}e^{ipx}\tilde\Phi(p)`$. In this representation $`\hat S:=\sum_x\lvert x+1\rangle\langle x\rvert`$ acts as $`e^{-ip}`$ and $`\hat x`$ acts as $`i\partial_p`$.

**Approximations, used in item 3 and Step 6 only.**
- (W) Weak records: used once, in Step 5a.
- (F) First order in the force: Steps 5d–5f and 6.
- (Cst) Start concentrated at $`p_0=0`$: Step 5c.

Their ranges of validity are stated in (6.14).

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

Model D needs both extensions: its diagonal is not uniform (the $`\sigma_3`$ term), and the start of item 2 has zero amplitudes.

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

**Decoupled body.** For the start $`\phi_X\otimes\eta`$ with $`\lVert\eta\rVert=1`$, we have $`\phi_x=\phi_X(x)\eta`$ and $`L_{xx'}(0)=2\mathrm{Re}[t_{xx'}\phi_X(x)^*\phi_X(x')]`$. Hence
```math
\mu=-\sum_{\{x,x'\},\,x\neq x'}2\mathrm{Re}\bigl[t_{xx'}\phi_X(x)^*\phi_X(x')\bigr]\,\Delta_{xx'}\,g(\Delta_{xx'},\cdot\,).
\qquad\text{(6.4)}
```
This is the value of (20.10) for the body without internal labels, with hopping $`t_{xx'}`$ and start $`\phi_X`$. It depends neither on $`\eta`$ nor on the $`T_{xx}`$.

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
To first order in the sector force, $`\ddot{\bar m}`$ is linear in $`\mathcal F_\xi`$. The mixture therefore gives the single evolution by $`C_b-\mathcal F\hat x`$, up to $`O(\mathcal F^2+\kappa^2\sigma_X^2)`$. Dropping the $`\kappa^2\sigma_X^2`$ term is the weak-record approximation, and it is used nowhere else.

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
- The start is $`w_q(0)=\tilde\phi(q)\lvert+_k(q)\rangle`$ with $`\int\frac{dq}{2\pi}\lvert\tilde\phi\rvert^2=1`$. Here $`\lvert+_k(q)\rangle`$ is the real eigenvector of the positive branch, and $`\lvert+_k(0)\rangle=\lvert1\rangle`$ by (6.7).
- The integrand is continuous in $`q`$. For a start concentrated at $`q=0`$, the integral therefore tends, on bounded $`\lambda`$-intervals, to the value of the two-level problem $`i\dot w=C_k(\mathcal F\lambda)w`$ with $`w(0)=\lvert1\rangle`$.

**5d. First order (F).** $`C_k(\mathcal F\lambda)=M_k\sigma_3-\tau\mathcal F\lambda\,\sigma_1+O(\mathcal F^3)`$. To first order, $`w_1=e^{-iM_k\lambda}`$ and $`w_2=e^{iM_k\lambda}\gamma`$, with $`\dot\gamma=i\tau\mathcal F\lambda\,e^{-2iM_k\lambda}`$ and $`\gamma(0)=0`$. Then
```math
\langle\sigma_2\rangle=2\mathrm{Im}(w_1^*w_2)=2\tau\mathcal F\int_0^\lambda\lambda'\cos\bigl(2M_k(\lambda-\lambda')\bigr)d\lambda'=\tau\mathcal F\sin^2(M_k\lambda)/M_k^2 .
```
The term $`\mathcal F\tau\sin(\mathcal F\lambda)\langle\sigma_1\rangle`$ is $`O(\mathcal F^2)`$.

Also $`a_0(\lambda)=0`$: at $`F=0`$ the state stays in the positive branch, and $`\langle+\vert\sigma_2\vert+\rangle=0`$ for real vectors. Using (6.12) and $`\bar x=\kappa\bar m e`$:
```math
a(\lambda)=\frac{2\tau^2}{M_k}\,\sin^2(M_k\lambda)\;\kappa^2\,g(e,F)\,e+O(F^2)\qquad(\text{fixed }\lambda).
\qquad\text{(6.13)}
```

**5e. Average.** $`\frac1\Lambda\int_{\lambda_1}^{\lambda_1+\Lambda}2\sin^2(M_k\lambda)\,d\lambda=1-\rho`$ with $`\lvert\rho\rvert\le1/(M_k\Lambda)`$.

Averaging needs $`\Lambda\gg1/M_k`$, which goes beyond fixed $`\lambda`$. For this, use the standard first-order adiabatic response of a branch to a uniform gradient. It holds when there are no branch transitions, $`\lvert\mathcal F\rvert\tau\ll M_k^2`$. It has two parts:
- a part $`\mathcal F\omega_k''(\mathcal F\lambda)`$ that does not oscillate;
- a part of amplitude $`\approx\lvert\mathcal F\rvert\tau^2/M_k`$ that oscillates at frequency $`2\omega_k\approx2M_k`$.

At fixed $`\lambda`$, its first order is (6.13). Since $`\omega_k''(q)=\frac{\tau^2}{M_k}\bigl[1+O\bigl(q^2(1+\tau^2/M_k^2)\bigr)\bigr]`$,
```math
\overline{a}=\frac{\tau^2}{M_k}\,\kappa^2\,g(e,F)\,e\,\Bigl[1+O\Bigl(\frac{1}{M_k\Lambda}\Bigr)\Bigr],\qquad
\frac{1}{2M_k}\ll\Lambda,\qquad \mathcal F_{\max}\,(\lambda_1+\Lambda)\ll\min\Bigl(1,\frac{M_k}{\tau}\Bigr),
\qquad\text{(6.14)}
```
with $`\mathcal F_{\max}:=\max_\xi\lvert\mathcal F_\xi\rvert`$.
- The first condition says that $`\Lambda`$ is long compared with the inverse gap.
- The second keeps the drift $`\mathcal F_\xi\lambda`$ of every sector inside the region where $`\omega_k''\approx\omega_k''(0)`$. This is the condition for first order in $`F`$ and for weak records.
- Together the two conditions imply $`\mathcal F_{\max}\tau\ll M_k^2`$.
- The chain limit requires $`L\gg W+\tau(\lambda_1+\Lambda)`$.

**5f. Averaged inverse inertia.** The coefficient of $`F`$ in (6.14) is
```math
\mu_{\rm av}(k)=\frac{\tau^2}{M_k}\,\kappa^2\,e\,g(e,\cdot\,)=\frac{\tau^2}{m+d_k}\,\kappa^2\,e\,g(e,\cdot\,).
\qquad\text{(6.15)}
```
```math
M_k\,\mu_{\rm av}(k)=\tau^2\kappa^2\,e\,g(e,\cdot\,)\ \ \text{for every }k,\qquad \frac{M_k}{\tau^2}=\frac{m}{\tau^2}+\frac{2\pi k}{N\lambda_0\,\tau^2}.
\qquad\text{(6.16)}
```
So $`\mu_{\rm av}(k)`$ decreases strictly with $`d_k`$. The scalar inertia $`M_k/\tau^2`$ is the rest cost (6.7) divided by $`\tau^2`$. The clock cost $`d_k`$ adds to it with the same coefficient $`1/\tau^2`$ as the rest term $`m`$.

### Step 6. Decoupled body on the chain

Take $`T_{x+1,x}=t\mathbb 1_N`$ with $`t\neq0`$, and $`T_{xx}=D'`$, an arbitrary self-adjoint clock term that is the same for all $`x`$. Then
```math
C_b-\mathcal F\hat x=(\omega(\hat p)-\mathcal F\hat x)\otimes\mathbb 1_N+\mathbb 1\otimes D',\qquad \omega(p)=te^{-ip}+t^*e^{ip} .
```
The two parts commute, and $`\bar m`$ involves only the first. Hence $`\hat v=\omega'(\hat p)`$ and $`i[C_b,\hat v]=0`$, so $`\ddot{\hat x}=-i\mathcal F[\hat x,\omega'(\hat p)]=\mathcal F\omega''(\hat p)`$ exactly.

Since $`\frac{d}{d\lambda}\langle\omega''(\hat p)\rangle=O(\mathcal F)`$, $`a(\lambda)=a(0)+O(F^2\lambda)`$: the response does not oscillate and equals its own average. By (6.2), $`\langle\omega''(\hat p)\rangle_0=-2\sum_x\mathrm{Re}[t^*\phi_X(x)^*\phi_X(x+1)]=-\sum_xL_{x,x+1}(0)`$. With $`\Delta_{x,x+1}=-\kappa e`$ this gives
```math
\mu_{\rm av}=\mu=\kappa^2\,\langle\phi_X\vert\omega''(\hat p)\vert\phi_X\rangle\,e\,g(e,\cdot\,)\ \xrightarrow{\ \text{concentrated at }p_0\ }\ -2\mathrm{Re}\bigl(t^*e^{ip_0}\bigr)\,\kappa^2\,e\,g(e,\cdot\,).
\qquad\text{(6.17)}
```
This is independent of the clock level, of $`\eta`$ and of $`D'`$; Step 5a applies unchanged.

### Step 7. Item 4: comparison

```math
\text{Model D: }\ \mu=0\neq\mu_{\rm av}(k)=\frac{\tau^2}{M_k}\,\kappa^2e\,g(e,\cdot\,);\qquad
\text{decoupled body: }\ \mu=\mu_{\rm av}.
\qquad\text{(6.18)}
```
**Decoupled body.** Its velocity commutes with $`C_b`$, so the free acceleration vanishes. The gradient term $`\mathcal F\omega''(\hat p)`$ is then the whole response, already at $`\lambda=0`$. Its value is fixed by the edge costs between points, which is the content of (20.10).

**Model D.** The velocity $`-\tau\cos\hat p\,\sigma_1`$ connects the two branches.
- At $`\lambda=0`$ the $`s=1`$ start has no edge cost between points, which gives (6.10).
- The response comes from interference between two terms: the admixture of the negative branch that the gradient induces, of amplitude $`\propto\mathcal F\tau/M_k^2`$, and the free acceleration $`2\tau M_k\cos\hat p\,\sigma_2`$.
- It builds up as $`\sin^2(M_k\lambda)`$, and its average is the branch curvature $`\tau^2/M_k`$.
- The clock cost enters through the gap, because $`D`$ sits in the branch term $`\sigma_3\otimes(m\mathbb 1+D)`$. In the decoupled body the clock term commutes with position and hopping, and drops out.

## Result

- **(6.1)** The inverse inertia $`\mu`$ of (20.10) of 03-ilang-space/20-cost-and-mass is the coefficient of $`F`$ for a uniform gradient added to any diagonal, and for every product start.
- **Item 1.**
  - (6.2): $`L_{hh'}(0)`$ in terms of the blocks, and $`L_{xx'}(0)=2\mathrm{Re}\langle\phi_x\vert T_{xx'}\vert\phi_{x'}\rangle`$.
  - (6.3): $`\mu=-\sum_{x\neq x'}L_{xx'}(0)\Delta_{xx'}g(\Delta_{xx'},\cdot)`$. Edges inside one point do not contribute.
  - (6.4): for the decoupled body, $`\mu`$ depends neither on $`\eta`$ nor on the $`T_{xx}`$.
- **Model D.**
  - (6.7): rest cost $`M_k=m+d_k`$.
  - (6.9): edge costs at $`\lambda=0`$, nonzero only on the clock edges of branch $`s=1`$.
  - (6.10): $`\mu=0`$.
- **Item 3.**
  - (6.13): $`a(\lambda)=\frac{2\tau^2}{M_k}\sin^2(M_k\lambda)\,\kappa^2g(e,F)e`$.
  - (6.14): its average $`\frac{\tau^2}{M_k}\kappa^2g(e,F)e`$, for $`1/(2M_k)\ll\Lambda`$ and $`\mathcal F_{\max}(\lambda_1+\Lambda)\ll\min(1,M_k/\tau)`$.
  - (6.15): $`\mu_{\rm av}(k)=\frac{\tau^2}{m+d_k}\kappa^2e\,g(e,\cdot)`$.
  - (6.16): the inertia is the rest cost over $`\tau^2`$; the clock cost $`d_k`$ adds to it like $`m`$.
  - (6.17): for the decoupled chain body, $`\mu_{\rm av}=\mu=\kappa^2\langle\omega''\rangle e\,g(e,\cdot)`$, independent of the clock level.
- **Item 4, (6.18).** $`\mu`$ and $`\mu_{\rm av}`$ coincide for the decoupled body, whose velocity commutes with $`C_b`$. They differ for Model D, whose velocity mixes the branches.

## Consistency checks

1. **Dimensions and $`\tau\to0`$.** $`C`$, $`\tau`$, $`m`$, $`d_k`$ and $`\mathcal F`$ have the dimension $`1/[\lambda]`$, and $`\ddot{\bar m}\sim\mathcal F\tau^2/M_k`$ has the dimension $`1/[\lambda]^2`$. In (6.9), $`2\pi/(N^2\lambda_0)`$ is a cost. As $`\tau\to0`$, $`\hat v=0`$, and (6.13) and (6.15) vanish. Passed.
2. **$`\lambda=0`$ by an independent route.** For the item-2 start with any $`\phi_X`$, $`\langle1\vert\sigma_2\vert1\rangle=\langle1\vert\sigma_1\vert1\rangle=0`$ in (6.12) gives $`a(0)=0`$ for every $`F`$. This agrees with (6.10), which was obtained from (20.10) through edge costs, and with $`a_0=0`$. Also, (6.13) vanishes at $`\lambda=0`$. Passed.
3. **Cost sum rule at one point.** The site costs of $`D`$ on the $`s=1`$ places of $`x`$ sum to $`\lvert\phi_X(x)\rvert^2\pi(N-1)/(N\lambda_0)`$. The edge costs (6.9) sum, by the Dirichlet-kernel sum $`\sum_{n=1}^{N-1}\sin((2k+1)\pi n/N)/\sin(\pi n/N)=N-1-2k`$, to $`-\lvert\phi_X(x)\rvert^2\pi(N-1-2k)/(N\lambda_0)`$. The total is $`d_k\lvert\phi_X(x)\rvert^2=\langle f_k\vert D\vert f_k\rangle\lvert\phi_X(x)\rvert^2`$. Passed.

## Open issues

- A ticking clock, i.e. a superposition of levels, is not treated. Since the level is conserved, the averaged response is the level-weighted mean of (6.15); whether this mixture is the inertia of one body is left open.
- Beyond fixed $`\lambda`$, Model D uses the stated standard adiabatic response of a branch, and the concentration limit. For wide packets the average is expected to be $`\langle\omega_k''\rangle`$, but this is not derived here.
- Second order in $`\kappa`$ (decoherence by the records, $`\kappa^2\sigma_X^2`$) and in $`F`$ (drift beyond the quadratic region, Bloch oscillation, branch transitions) is not treated.
- The meaning of $`\tau`$ as a maximal speed, and of $`M_k/\tau^2`$, belongs to criteria 4 and 6; it is outside this package (M1, M3).

## Methods used

- Heisenberg equations of motion (double commutators)
- Affine dependence of the acceleration on the diagonal of the contract
- Fourier transform on $`\mathbb Z`$, plane waves, two-branch dispersion
- Method of characteristics (drift of the plane-wave label in a uniform gradient)
- First-order time-dependent perturbation theory; adiabatic perturbation theory (stated)
- Conserved record observable: exact mixture decomposition of the view
- Geometric and Dirichlet-kernel sums
- Limit of finite chains with a propagation bound
