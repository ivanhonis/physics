# Moving clock: a ring clock carried by a body in the record background

- **Subproject:** 04-ilang-time
- **Package:** 05-moving-clock
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-10

## Changes from previous version

- **Items 3 and 4 are now first order in $`\epsilon`$ on the tick scale** (fixed $`\lambda/\lambda_0`$). v1 dropped the curvature of $`\omega_k`$ in $`d_k`$, whose accumulated phase is first order there. Step 6 now expands about the centre of the clock band and keeps it. The rate of the carried clock is $`\Gamma`$ of (5.20) instead of $`\gamma=m/\omega_0`$: $`m`$ is replaced by $`\bar\mu=m+\langle0\vert D\vert0\rangle`$.
- New equations (5.20)–(5.29). The v1 tags (5.13)–(5.19) are retired and not reused. Their formulas are (5.21), (5.22) and (5.26)–(5.29) with $`\bar\mu\to m`$; they hold at leading (zeroth) order in $`\epsilon`$ only.
- Step 7 distinguishes the tick of the first-order distribution from the behaviour of the reading near it, (5.23).
- Step 8 is new: the velocity of the item-3 start to first order, with its oscillating part. Step 9 (item 4, Step 8 of v1) uses the mean velocity (5.25).
- Step 2: the convergence of $`\bar x`$ and $`v`$ in the chain limit now rests on the bounded commutator $`i[C,x]`$.
- Setup [S] and Step 6(iii): $`p_0`$ and $`\delta p`$ are the mean and the standard deviation of the packet, and the spread errors are uniform second-order bounds. The error term of (5.8) is accordingly $`O(\delta p^2)`$.
- Steps 1, 3, 4, 5 and the equations (5.1)–(5.12) are otherwise unchanged.

## Response to verification

- **I1: Accepted and fixed in Steps 6–9.**
  - The quadratic term of $`\omega_k`$ is kept: Step 6(ii), (5.20). The first-order distribution is (5.21), with rate $`\Gamma=\gamma\bigl[1+\frac{(N-1)\epsilon}2(1-\gamma^2)\bigr]+O((N\epsilon)^2)`$. For $`N=2`$ this is the rate of the verifier's example (check 3).
  - Tick and ratio: (5.22). The nominal tick is separated from the finite-$`\epsilon`$ reading in (5.23) and the items after it.
  - The velocity is carried to the same order in Step 8, and the relations of item 4 are (5.26)–(5.29).
  - Every neglected term is listed with its order after (5.21) and (5.25). The v1 formulas are labelled leading order.
- **I2: Accepted and fixed in Step 2, items (a)–(d).** Superexponential tails are claimed for finitely supported starts only. For the packets, norm convergence gives the reading probabilities; $`v`$ and $`\bar x`$ converge by the bounded commutator $`i[C,x]`$.
- **I3: Accepted and fixed in Setup [S] and Step 6(iii).** The spread bound is second order in $`\delta p`$, uniform in $`p_0`$, and does not vanish at $`p_0=0,\pm\pi/2`$.

## Setup and assumptions

- **System.** The body $`b`$ and the medium $`c`$ are each the only instance of their type, so no swap condition (1.11) applies. The joint space is $`\mathcal H=\mathcal H_b\otimes\mathcal H_c`$, with $`\mathcal H_c`$ finite-dimensional (A1).
  - Item 1: $`\mathcal H_b=\mathcal H_X\otimes\mathbb C^N`$, with places $`(x,a)`$.
  - Items 2–4: $`\mathcal H_b=\ell^2(\mathbb Z)\otimes\mathbb C^2\otimes\mathbb C^N`$ (position, branch, clock label), with places $`(x,s,a)`$, obtained as the limit of Step 2.
  - Contract: $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$ with $`K_h=K_x`$.
  - Start: $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$. We take $`\lambda\ge0`$ (A9 restricted).
- **Clock reading** (A8). It is applied at a stated $`\lambda`$. Its projectors are $`\Pi_a=\mathbb 1\otimes\lvert a\rangle\langle a\rvert\otimes\mathbb 1_c`$, with $`\lvert a\rangle\langle a\rvert`$ on the clock-label factor. By (1.3), $`q(a;\lambda)=\lVert\Pi_a\Psi(\lambda)\rVert^2`$ with $`\Psi(\lambda)=e^{-iC\lambda}(\phi\otimes\chi)`$.
- **Branch label.** $`\sigma_3\lvert1\rangle=\lvert1\rangle`$, $`\sigma_3\lvert2\rangle=-\lvert2\rangle`$, $`\sigma_1\lvert1\rangle=\lvert2\rangle`$. Spinors are written as columns $`(\beta_1,\beta_2)^T`$.
- **Clock inputs (02-clock@v2).** Take (2.9) with $`\alpha_m=0`$, $`\varepsilon=0`$, $`\ell_k=k`$. Then $`D=\sum_{k=0}^{N-1}d_k\lvert f_k\rangle\langle f_k\rvert`$, $`d_k=\frac{2\pi k}{N\lambda_0}`$, satisfies $`e^{-iD\lambda_0}=S`$. By (2.12) with $`c=0`$, it has the minimal spread for the start $`\lvert0\rangle`$.
  - (2.13) is its reading distribution. It is written below with the place called $`a`$, since $`m`$ denotes the parameter of $`B`$.
  - Since $`\langle a\vert f_k\rangle=N^{-1/2}e^{2\pi ika/N}`$, (2.13) is a geometric sum:
```math
P_N(a;\vartheta):=\Bigl\lvert\frac1N\sum_{k=0}^{N-1}e^{2\pi ik(a-\vartheta)/N}\Bigr\rvert^2=\frac{\sin^2(\pi\vartheta)}{N^2\sin^2\bigl(\pi(\vartheta-a)/N\bigr)},\qquad p(a;\lambda)=P_N(a;\lambda/\lambda_0)\ \text{in (2.13)}.
\qquad\text{(5.1)}
```
- **Space inputs (03-ilang-space).**
  - By (5.10) and (5.11) of 03-ilang-space/05-recording-contract, the background point of a place $`h`$ is $`u_h=(K_h-\langle K_h\rangle)\chi`$, and the distance is $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$. Both depend only on $`K_h`$ and $`\chi`$. (5.10) of 03-ilang-space/05-recording-contract is stated for $`\phi_h\neq0`$; only $`u_h`$ and $`d_0`$ are used below.
  - From 03-ilang-space/17-motion: the definitions $`\bar x=\sum_hp_hu_h`$ and $`v=\mathrm d\bar x/\mathrm d\lambda`$; the bound (17.7), $`\lVert v\rVert\le v_{\max}:=\varrho(a)\le\max_h\sum_{h'}\lvert t_{hh'}\rvert d_0(h,h')`$ with $`a_{hh'}=\lvert t_{hh'}\rvert d_0(h,h')`$; the chain relations (17.15); and the chain value (17.20), $`v_{\max}=2t\sigma_X`$.
- **Weak-record regime [W]** (items 2–4, as fixed in item 2(b)).
  - Everything is computed at $`\kappa=0`$, except that positions are the background points $`u_h=O(\kappa)`$. Then $`\Psi(\lambda)=(e^{-iC_b\lambda}\phi)\otimes\chi`$, and the view of $`b`$ is that of $`C_b`$ alone.
  - By Duhamel's formula and Step 2(d), the exact state differs from this one by at most $`\kappa\lVert X\rVert\int_0^\lambda\lVert x\,e^{-iC_b\lambda'}\phi\rVert\,\mathrm d\lambda'\le\kappa\lVert X\rVert\lambda\bigl(\lVert x\phi\rVert+\tfrac12\tau\lambda\bigr)`$. [W] is valid while this is $`\ll1`$.
- **Starts near $`p_0`$ [S].** $`g`$ is smooth and $`2\pi`$-periodic, with $`\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g\rvert^2=1`$. On the arc $`(p_0-\pi,p_0+\pi]`$ the weight $`\lvert g\rvert^2\frac{\mathrm dp}{2\pi}`$ has mean $`p_0`$ and variance $`\delta p^2\ll1`$. For every $`2\pi`$-periodic $`C^2`$ function $`F`$, Taylor's theorem with remainder then gives, uniformly in $`p_0`$,
```math
\Bigl\lvert\int\frac{\mathrm dp}{2\pi}\lvert g\rvert^2F(p)-F(p_0)\Bigr\rvert\le\tfrac12\,\delta p^2\,\sup_p\lvert F''(p)\rvert .
```
- **Clock parameter.** $`\epsilon:=\frac{2\pi}{N\lambda_0m}`$, so $`d_k=km\epsilon`$ and $`m\epsilon\lambda=\frac{2\pi}N\vartheta_0`$ with $`\vartheta_0:=\lambda/\lambda_0`$. "First order in $`\epsilon`$" means: at fixed $`N`$, $`\tau/m`$, $`p_0`$ and $`\vartheta_0`$ (the tick scale), with a remainder $`O(\epsilon^2)`$. Bounds are given with their $`N`$-dependence; they need $`N\epsilon(1+\vartheta_0)\le1`$.

## Derivation

### Step 1. Decoupled body (item 1)

Since $`K_{(x,a)}=K_x`$, the record term is $`\sum_x\lvert x\rangle\langle x\rvert\otimes\mathbb 1_N\otimes K_x`$. Order the factors as $`(\mathcal H_X\otimes\mathcal H_c)\otimes\mathbb C^N`$; this relabelling of tensor factors changes no reading. Then $`C=G\otimes\mathbb 1_N+\mathbb 1\otimes D'`$, with $`G:=H\otimes\mathbb 1_c+\sum_x\lvert x\rangle\langle x\rvert\otimes K_x`$.

The two terms act on different factors and commute. Hence $`e^{-iC\lambda}=e^{-iG\lambda}\otimes e^{-iD'\lambda}`$ and $`\Psi(\lambda)=e^{-iG\lambda}(\phi_X\otimes\chi)\otimes e^{-iD'\lambda}\eta`$. $`\Pi_a`$ acts on the last factor only, and $`e^{-iG\lambda}`$ is unitary, so
```math
q(a;\lambda)=\bigl\lvert\langle a\vert e^{-iD'\lambda}\vert\eta\rangle\bigr\rvert^2\qquad\text{for all }\lambda .
\qquad\text{(5.2)}
```
This holds exactly, for every $`\chi`$, every $`K_x`$ and every $`\kappa`$. The answer to each of the three questions is no: $`q`$ depends neither on $`H`$, nor on $`\phi_X`$, nor on the $`K_x`$ (nor on $`\chi`$). For $`D'=D`$ and $`\eta=\lvert0\rangle`$, (5.2) is (2.13).

The model of items 2–4 is not of this form: $`B`$ contains $`\sigma_3\otimes D`$, which does not commute with $`A\propto\sigma_1`$.

### Step 2. The infinite chain as a limit (item 2)

**Finite chains.** Take $`\Lambda_L=\{-L,\dots,L\}`$, keep in $`A`$ only the bonds inside $`\Lambda_L`$, and restrict $`B`$ and the records to $`\Lambda_L`$. This gives $`C^{(L)}`$; the same expressions on $`\ell^2(\mathbb Z)`$ give $`C^{(\infty)}`$.

**Locality bound.** Write $`C^{(\cdot)}=A^{(\cdot)}\otimes\mathbb 1_c+Q`$, where $`Q`$ (the $`B`$ term and the records) is diagonal in $`x`$. $`A`$ is $`\frac\tau2`$ times a sum of two operators of norm 1, so $`\lVert A\rVert\le\tau`$. Expand $`e^{-iC\lambda}`$ in powers of $`A`$ around $`e^{-iQ\lambda}`$ (Dyson series). The term of order $`n`$ moves $`x`$ by at most $`n`$ and has norm at most $`(\tau\lambda)^n/n!`$. For a start supported in $`\lvert x\rvert\le R`$, therefore, for both $`C^{(L)}`$ and $`C^{(\infty)}`$:
```math
\bigl\lVert\Pi_{\lvert x\rvert\ge L}\,e^{-iC^{(\cdot)}\lambda}(\phi\otimes\chi)\bigr\rVert\le\sum_{n\ge L-R}\frac{(\tau\lambda)^n}{n!} .
\qquad\text{(5.3)}
```
On vectors supported in $`\Lambda_L`$, $`C^{(\infty)}-C^{(L)}`$ is the hopping out of the sites $`x=\pm L`$. Its norm is at most $`\tau\lVert\Pi_{\lvert x\rvert\ge L}\,\cdot\,\rVert`$. By Duhamel's formula, the two evolved states therefore differ by at most $`\tau\lambda\sum_{n\ge L-R}(\tau\lambda)^n/n!\to0`$.

**How the limit is taken.** First $`L\to\infty`$, at fixed $`\lambda`$, $`\kappa`$ and start; then $`\kappa\to0`$ [W], then the small spread [S], then the expansion in $`\epsilon`$. On $`\Lambda_L`$ the start is the normalized restriction $`\phi^{(L)}`$ of $`\phi`$.
- (a) *Finitely supported starts.* By (5.3) the tails are superexponentially small in $`L-R`$, and the evolved states converge in norm.
- (b) *Starts with $`\lVert x\phi\rVert<\infty`$.* These include the packets used below: their $`\phi_x`$ decay faster than any power of $`x`$, because $`g\beta`$ is smooth and periodic. $`\phi^{(L)}\to\phi`$ in norm, and unitarity carries an approximation of the start to every $`\lambda`$. With (a), the evolved states converge in norm; hence every reading probability ($`q`$, $`p_h`$) converges.
- (c) *Velocity.* Norm convergence does not control the unbounded label $`x`$. But $`x`$ commutes with $`Q`$, and $`[T,x]=-T`$ for $`T=\sum_x\lvert x+1\rangle\langle x\rvert`$, so $`i[C^{(\cdot)},x]=-\frac\tau2(T+T^\dagger)\otimes\sigma_1\otimes\mathbb 1_N\otimes\mathbb 1_c`$ (bonds inside $`\Lambda_L`$ for $`C^{(L)}`$), of norm $`\le\tau`$ for every $`L`$. $`\mathrm d\bar x_{\rm lab}/\mathrm d\lambda`$ (Step 4) is its expectation. These operators converge strongly as $`L\to\infty`$, so by (b) the velocity converges at every $`\lambda`$, and it is bounded by $`\tau`$.
- (d) *Mean position.* $`\bar x_{\rm lab}(\lambda)=\bar x_{\rm lab}(0)+\int_0^\lambda(\mathrm d\bar x_{\rm lab}/\mathrm d\lambda')\,\mathrm d\lambda'`$. The first term converges since $`\sum_x\lvert x\rvert\lvert\phi_x\rvert^2<\infty`$, the second by (c) and bounded convergence. The same commutator gives $`\lVert x\Psi(\lambda)\rVert\le\lVert x\phi\rVert+\tau\lambda`$, uniformly in $`L`$.

**Plane waves.** On $`\ell^2(\mathbb Z)`$ we use the standard Fourier facts.
- The plane waves are $`\lvert p\rangle=\sum_xe^{ipx}\lvert x\rangle`$, $`p\in(-\pi,\pi]`$, with $`\langle p\vert p'\rangle=2\pi\delta(p-p')`$.
- $`T\lvert p\rangle=e^{-ip}\lvert p\rangle`$.
- A vector $`\psi=\int\frac{\mathrm dp}{2\pi}\lvert p\rangle\otimes G(p)`$ has $`\lVert\psi\rVert^2=\int\frac{\mathrm dp}{2\pi}\lVert G\rVert^2`$.
- The position label acts as $`G\mapsto i\partial_pG`$, for smooth periodic $`G`$ (integration by parts).

### Step 3. Anticommutation and spectrum (item 2(a))

In terms of $`T`$, $`A=\frac\tau2\bigl(-i(T-T^\dagger)\bigr)\otimes\sigma_1\otimes\mathbb 1_N`$ and $`B=\mathbb 1\otimes\sigma_3\otimes M`$, with $`M:=m\mathbb 1_N+D`$. On the position and clock factors the factors of $`A`$ and $`B`$ commute, and $`\sigma_1\sigma_3+\sigma_3\sigma_1=0`$. Hence
```math
AB+BA=0,\qquad C_b^2=A^2+B^2 .
\qquad\text{(5.4)}
```
Further, $`-i(T-T^\dagger)\lvert p\rangle=-2\sin p\,\lvert p\rangle`$ and $`M\lvert f_k\rangle=\mu_k\lvert f_k\rangle`$. So
```math
C_b\bigl(\lvert p\rangle\otimes\beta\otimes\lvert f_k\rangle\bigr)=\lvert p\rangle\otimes C_k(p)\beta\otimes\lvert f_k\rangle,\qquad C_k(p):=-\tau\sin p\,\sigma_1+\mu_k\sigma_3,\qquad\mu_k:=m+d_k .
\qquad\text{(5.5)}
```
By (5.4), $`C_k(p)^2=(\mu_k^2+\tau^2\sin^2p)\mathbb 1`$; moreover $`\mathrm{Tr}C_k=0`$. Write $`C_k=\omega_k(\sin\theta_k\sigma_1+\cos\theta_k\sigma_3)`$, with $`\cos\theta_k=\mu_k/\omega_k>0`$. The half-angle formulas then give the generalized eigenvectors $`\lvert p\rangle\otimes\beta_{k,\pm}(p)\otimes\lvert f_k\rangle`$ of $`C_b`$, with eigenvalues $`\pm\omega_k(p)`$:
```math
\omega_k(p)=\sqrt{\mu_k^2+\tau^2\sin^2p},\quad
\beta_{k,+}=\begin{pmatrix}\cos\frac{\theta_k}2\\ \sin\frac{\theta_k}2\end{pmatrix},\quad
\beta_{k,-}=\begin{pmatrix}-\sin\frac{\theta_k}2\\ \cos\frac{\theta_k}2\end{pmatrix},\quad
\tan\theta_k(p)=-\frac{\tau\sin p}{\mu_k},\ \ \lvert\theta_k\rvert<\frac\pi2 .
\qquad\text{(5.6)}
```
The two branches are separated by the gap $`2\mu_k\ge2m>0`$. The spinors $`\beta_{k,\pm}`$ are real, of unit length, and smooth and $`2\pi`$-periodic in $`p`$.

### Step 4. Background positions and velocity (item 2(b))

Every place has $`u_{(x,s,a)}=\kappa x(X-\langle X\rangle)\chi=\kappa x\,e`$, with $`\lVert e\rVert=\sigma_X`$. Hence $`d_0(h,h')=\kappa\sigma_X\lvert x-x'\rvert`$: this is (17.15) of 03-ilang-space/17-motion with $`X\to\kappa X`$. By (5.11) of 03-ilang-space/05-recording-contract, all places with the same $`x`$ are one background point. With $`P(x;\lambda):=\sum_{s,a}p_{(x,s,a)}(\lambda)`$,
```math
\bar x(\lambda)=\kappa\,\bar x_{\rm lab}(\lambda)\,e,\qquad\bar x_{\rm lab}:=\sum_xx\,P(x;\lambda),\qquad v=\kappa\,\frac{\mathrm d\bar x_{\rm lab}}{\mathrm d\lambda}\,e .
\qquad\text{(5.7)}
```
**Start.** $`\phi=\psi_{k,+}\otimes\lvert f_k\rangle`$, with $`\psi_{k,+}:=\int\frac{\mathrm dp}{2\pi}g(p)\lvert p\rangle\otimes\beta_{k,+}(p)`$. Under [W], (5.6) gives the evolved amplitude $`G(p,\lambda)=g(p)e^{-i\omega_k(p)\lambda}\beta_{k,+}(p)`$.

**Mean position.** By Step 2,
```math
\bar x_{\rm lab}=\int\frac{\mathrm dp}{2\pi}G^\dagger i\partial_pG=\int\frac{\mathrm dp}{2\pi}\bigl(ig^*\partial_pg+\lambda\lvert g\rvert^2\partial_p\omega_k+i\lvert g\rvert^2\beta_{k,+}^T\partial_p\beta_{k,+}\bigr).
```
The last term vanishes, because $`\beta_{k,+}`$ is real and of unit length. So $`\bar x_{\rm lab}`$ is exactly linear in $`\lambda`$, with the group velocity as slope; the last equality is [S]:
```math
\frac{\mathrm d\bar x_{\rm lab}}{\mathrm d\lambda}=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g(p)\rvert^2\,\partial_p\omega_k(p)=\partial_p\omega_k(p_0)+O(\delta p^2).
\qquad\text{(5.8)}
```
With $`\hat e:=e/\sigma_X`$:
```math
v=\kappa\sigma_X\,w_k(p_0)\,\hat e,\qquad w_k(p):=\partial_p\omega_k(p)=\frac{\tau^2\sin p\cos p}{\sqrt{\mu_k^2+\tau^2\sin^2p}} .
\qquad\text{(5.9)}
```

### Step 5. Largest velocity and the bound (17.7) of 03-ilang-space/17-motion (item 2(b))

**Largest velocity.** With $`u=\sin^2p_0`$, $`w_k^2=\tau^4u(1-u)/(\mu_k^2+\tau^2u)`$. It vanishes at $`u=0`$ and $`u=1`$, and its $`u`$-derivative vanishes iff $`\tau^2u^2+2\mu_k^2u-\mu_k^2=0`$. The root in $`[0,1]`$ is $`u_*=\mu_k/(\mu_k+W_k)`$, with $`W_k:=\sqrt{\mu_k^2+\tau^2}`$. There $`\mu_k^2+\tau^2u_*=\mu_kW_k`$ and $`1-u_*=W_k/(\mu_k+W_k)`$, so $`w_k^2=\tau^4/(\mu_k+W_k)^2`$:
```math
\max_{p_0}\lVert v\rVert=\kappa\sigma_X\,(W_k-\mu_k)=\kappa\sigma_X\frac{\tau^2}{\sqrt{\mu_k^2+\tau^2}+\mu_k},\qquad\text{attained at }\sin^2p_0=\frac{\mu_k}{\mu_k+W_k}.
\qquad\text{(5.10)}
```
**The bound.**
- $`A`$ has $`\lvert t_{hh'}\rvert=\tau/2`$ between $`(x,s,a)`$ and $`(x\pm1,\bar s,a)`$, $`\bar s\ne s`$.
- The off-diagonal entries of $`B`$ come from $`D`$, which is not diagonal on the clock places. They join places with equal $`x`$, where $`d_0=0`$.
- Hence $`a_{hh'}=\frac\tau2\kappa\sigma_X`$ on the edges $`(x,s,a)`$–$`(x\pm1,\bar s,a)`$, and $`a_{hh'}=0`$ otherwise.
- This graph is the disjoint union of $`2N`$ chains $`\{(x,s,a):x+s\equiv c\ (\mathrm{mod}\ 2)\}`$, along which $`d_0=\kappa\sigma_X\lvert x-x'\rvert`$.
- $`a`$ depends only on $`\lvert t_{hh'}\rvert`$ and $`d_0`$. Each chain is therefore that of (17.20) of 03-ilang-space/17-motion, with $`t=\tau/2`$ and $`X\to\kappa X`$.

$`\varrho(a)`$ is the maximum over the components, so
```math
v_{\max}=\tau\,\kappa\sigma_X=\max_h\sum_{h'}\lvert t_{hh'}\rvert\,d_0(h,h') .
\qquad\text{(5.11)}
```
On $`\Lambda_L`$, $`\varrho(a)=\tau\kappa\sigma_X\cos\frac{\pi}{2L+2}\to\tau\kappa\sigma_X`$.

In units of $`\kappa\sigma_X`$: $`v`$ is $`w_k(p_0)`$, its largest value is $`W_k-\mu_k`$, and the bound is $`\tau`$. The bound is not reached, since $`(W_k-\mu_k)/\tau=\sqrt{(W_k-\mu_k)/(W_k+\mu_k)}<1`$.

### Step 6. Clock reading of the moving clock, to first order in $`\epsilon`$ (item 3)

**Start.** $`\phi=\psi_{0,+}\otimes\lvert0\rangle`$: the clock label is exactly in the place $`\lvert0\rangle`$, and the branch spinor is that of level $`0`$. Write $`\beta_0:=\beta_{0,+}`$, and $`\beta_{0,-}`$ for the other spinor of level $`0`$. Since $`\lvert0\rangle=N^{-1/2}\sum_k\lvert f_k\rangle`$, (5.5), [W] and Step 2 give
```math
q(a;\lambda)=\int\frac{\mathrm dp}{2\pi}\lvert g(p)\rvert^2\,\lVert\Phi_a(p,\lambda)\rVert^2,\qquad
\Phi_a:=\frac1N\sum_{k=0}^{N-1}e^{2\pi ika/N}\,e^{-iC_k(p)\lambda}\beta_0(p).
\qquad\text{(5.12)}
```
**Order counting.** A phase $`d_k\lambda=2\pi k\vartheta_0/N`$ is $`O(1)`$ and is kept exactly. A term $`\propto d_k^n\lambda/m^{n-1}`$ of a phase is of order $`\epsilon^{n-1}`$. The quadratic term of $`\omega_k`$ in $`d_k`$ is therefore first order and is kept; the cubic term is second order.

*(i) Branch mixing: second order.*
- $`\beta_{k,\pm}`$ is $`\beta_{0,\pm}`$ rotated by $`-\delta_k`$, with $`\delta_k:=(\theta_0-\theta_k)/2`$. Since $`\lvert\partial_\mu\theta\rvert=\tau\lvert\sin p\rvert/(\mu^2+\tau^2\sin^2p)\le1/(2\mu)`$, we have $`\lvert\delta_k\rvert\le d_k/(4m)\le\delta:=(N-1)\epsilon/4`$.
- Expanding $`\beta_0=\cos\delta_k\,\beta_{k,+}+\sin\delta_k\,\beta_{k,-}`$ and rotating back gives $`e^{-iC_k\lambda}\beta_0=\bigl(e^{-i\omega_k\lambda}+2i\sin^2\delta_k\sin\omega_k\lambda\bigr)\beta_0+i\sin2\delta_k\sin\omega_k\lambda\,\beta_{0,-}`$.
- Since $`\beta_0\perp\beta_{0,-}`$, the term of first order in $`\delta_k`$ enters $`\lVert\Phi_a\rVert^2`$ only squared. With $`\mathcal A_a(p,\lambda):=\frac1N\sum_ke^{2\pi ika/N-i\omega_k(p)\lambda}`$: $`\bigl\lvert\lVert\Phi_a\rVert^2-\lvert\mathcal A_a\rvert^2\bigr\rvert\le8\delta^2+4\delta^4\le(N\epsilon)^2`$, uniformly in $`\lambda`$ and $`p`$.
- The same holds for any other reference level used to define "the positive branch".

*(ii) Dispersion about the band centre.* Let $`\bar d:=\frac1N\sum_kd_k=\frac{N-1}2m\epsilon=\langle0\vert D\vert0\rangle`$, $`\bar\mu:=m+\bar d`$ and $`j:=k-\frac{N-1}2`$. Then $`d_k-\bar d=m\epsilon j`$, and the values of $`j`$ are symmetric about $`0`$. Taylor's theorem in $`d`$ about $`\bar d`$, with $`\partial_d\omega=\mu/\omega`$, $`\partial_d^2\omega=\tau^2\sin^2p/\omega^3`$ and $`\lvert\partial_d^3\omega\rvert=3\mu\tau^2\sin^2p/\omega^5\le1/m^2`$, gives
```math
\omega_k=\bar\omega+\Gamma\,m\epsilon j+\tfrac12\bar c\,(m\epsilon j)^2+\bar\rho_k,\qquad
\bar\omega(p):=\sqrt{\bar\mu^2+\tau^2\sin^2p},\quad\Gamma(p):=\frac{\bar\mu}{\bar\omega(p)},\quad\bar c:=\frac{\tau^2\sin^2p}{\bar\omega^3}\le\frac1m,\quad\lvert\bar\rho_k\rvert\le\frac{(m\epsilon\lvert j\rvert)^3}{6m^2}.
\qquad\text{(5.20)}
```
- With $`m\epsilon\lambda=\frac{2\pi}N\vartheta_0`$: $`\omega_k\lambda=\bar\omega\lambda+\frac{2\pi}Nj\,\Gamma\vartheta_0+\zeta j^2+\bar\rho_k\lambda`$, where $`\zeta:=\frac{\pi\epsilon}N\,m\bar c\,\vartheta_0\le\frac{\pi\epsilon}N\vartheta_0`$ and $`\lvert\bar\rho_k\rvert\lambda\le\frac\pi{24}(N\epsilon)^2\vartheta_0`$ (using $`\lvert j\rvert<N/2`$).
- The factors $`e^{-i\bar\omega\lambda}`$ and $`e^{i\pi(N-1)a/N}`$ are common to all $`k`$ and drop out of the modulus. With $`y:=a-\Gamma\vartheta_0`$, $`\lvert\mathcal A_a\rvert=\bigl\lvert\frac1N\sum_je^{2\pi ijy/N}e^{-i\zeta j^2}e^{-i\bar\rho_k\lambda}\bigr\rvert`$.
- Expand $`e^{-i\zeta j^2}=1-i\zeta j^2+O(\zeta^2j^4)`$. By the symmetry $`j\to-j`$, both $`\mathcal D(y):=\frac1N\sum_je^{2\pi ijy/N}=\frac{\sin\pi y}{N\sin(\pi y/N)}`$ and $`\mathcal E(y):=\frac1N\sum_jj^2e^{2\pi ijy/N}`$ are real. Hence $`\lvert\mathcal D-i\zeta\mathcal E\rvert^2=\mathcal D^2+\zeta^2\mathcal E^2`$: about the band centre the curvature has no first-order effect. Its whole first-order effect is the change of the rate from $`\gamma=m/\omega_0`$ to $`\Gamma`$.
- By (5.1), $`\mathcal D(y)^2=P_N(a;\Gamma\vartheta_0)`$. The terms of order $`\zeta^2`$ change $`\lvert\mathcal A_a\rvert^2`$ by at most $`\frac14(N\epsilon\vartheta_0)^2`$, and the phases $`\bar\rho_k\lambda`$ by at most $`\frac\pi{12}(N\epsilon)^2\vartheta_0`$ to leading order.

*(iii) Spread.* By (i) and (ii), $`\lVert\Phi_a(p,\lambda)\rVert^2=P_N(a;\Gamma(p)\vartheta_0)`$ up to the stated terms, uniformly in $`p`$. Apply [S] to $`F(p)=P_N(a;\Gamma(p)\vartheta_0)`$. From $`P_N=\mathcal D^2`$, $`\lvert\mathcal D'\rvert\le\frac\pi2`$ and $`\lvert\mathcal D''\rvert\le\frac{\pi^2}3`$: $`\lvert\partial_\vartheta P_N\rvert\le\pi`$ and $`\lvert\partial_\vartheta^2P_N\rvert\le\frac{7\pi^2}6`$. With $`r:=\tau/\bar\mu`$ and $`\Gamma=(1+r^2\sin^2p)^{-1/2}`$: $`\lvert\Gamma'\rvert\le\frac{r^2}2`$ and $`\lvert\Gamma''\rvert\le r^2+\frac34r^4`$. The replacement $`\Gamma(p)\to\Gamma(p_0)`$ therefore costs at most
```math
\mathcal R_{\rm S}:=\frac{\delta p^2}2\Bigl[\frac{7\pi^2}{24}\,r^4\vartheta_0^2+\pi\bigl(r^2+\tfrac34r^4\bigr)\vartheta_0\Bigr],
```
uniformly in $`p_0`$; the bound does not vanish at the stationary points $`p_0=0,\pm\frac\pi2`$ of $`\Gamma`$.

**Result.**
```math
q(a;\lambda)=P_N\Bigl(a;\Gamma(p_0)\frac{\lambda}{\lambda_0}\Bigr)+\mathcal R,\qquad
\Gamma(p_0)=\frac{\bar\mu}{\sqrt{\bar\mu^2+\tau^2\sin^2p_0}}=\gamma\Bigl[1+\frac{(N-1)\epsilon}2\bigl(1-\gamma^2\bigr)\Bigr]+O\bigl((N\epsilon)^2\bigr),\quad\gamma:=\frac m{\omega_0(p_0)} .
\qquad\text{(5.21)}
```
This is (2.13) with $`\lambda`$ replaced by $`\Gamma(p_0)\lambda`$, and $`\bar\mu=m+\frac{\pi(N-1)}{N\lambda_0}`$. The neglected terms $`\mathcal R`$ are:
- in $`\epsilon`$, second order only: $`\lvert\mathcal R_\epsilon\rvert\le(N\epsilon)^2(1+\vartheta_0)^2`$, from branch mixing ($`\le(N\epsilon)^2`$), the quadratic dispersion at second order ($`\le\frac14(N\epsilon\vartheta_0)^2`$) and the cubic dispersion ($`\lesssim\frac\pi{12}(N\epsilon)^2\vartheta_0`$);
- in the spread: $`\mathcal R_{\rm S}=O(\delta p^2)`$;
- in the records: $`O(\kappa)`$, from [W].

No term of first order in $`\epsilon`$ is neglected. The v1 form $`P_N(a;\gamma\lambda/\lambda_0)`$ differs from (5.21) by up to $`\pi(\Gamma-\gamma)\vartheta_0=O(N\epsilon\,\vartheta_0)`$: it is the leading order only.

### Step 7. Tick and ratio (item 3)

By (5.1), $`P_N(\cdot\,;\vartheta)`$ is concentrated on a single place iff $`\vartheta\in\mathbb Z`$, and then on $`a\equiv\vartheta`$. To first order, (5.21) is the distribution (2.13) of a uniform ring clock with tick $`\lambda_0/\Gamma(p_0)`$: starting from $`a=0`$, it gives $`a=1`$ with certainty first at $`\Gamma(p_0)\lambda=\lambda_0`$. Since $`\Gamma(0)=1`$, with $`\omega:=\omega_0(p_0)`$:
```math
\lambda_0(p_0)=\frac{\lambda_0}{\Gamma(p_0)},\qquad
R(p_0):=\frac{\lambda_0(p_0)}{\lambda_0(0)}=\frac{\bar\omega(p_0)}{\bar\mu}=\sqrt{1+\frac{\tau^2}{\bar\mu^2}\sin^2p_0}=\frac\omega m\Bigl[1-\frac{(N-1)\epsilon}2\,\frac{\tau^2\sin^2p_0}{\omega^2}\Bigr]+O\bigl((N\epsilon)^2\bigr)\ \ge1 .
\qquad\text{(5.22)}
```
Relative to its rest rate, the carried clock advances at the rate $`\Gamma(p_0)=1/R\le1`$. The rate equals $`1`$ only for $`\sin p_0=0`$. It is smallest at $`p_0=\pm\pi/2`$, where it equals $`\bar\mu/\bar W`$, with $`\bar W:=\sqrt{\bar\mu^2+\tau^2}`$. At leading order, $`R=\omega/m`$ (v1).

**Nominal tick and actual reading.** From $`\mathcal D(y)^2=1-\frac{\pi^2(N^2-1)}{3N^2}y^2+O(y^4)`$ and (5.21), with $`\xi:=\lambda/\lambda_0(p_0)-1`$:
```math
1-q(1;\lambda)=\frac{\pi^2(N^2-1)}{3N^2}\,\xi^2+O(\xi^4)-\mathcal R .
\qquad\text{(5.23)}
```
- At $`\lambda=\lambda_0(p_0)`$ the reading gives $`a=1`$ with probability $`1-O((N\epsilon)^2)`$: with certainty to first order, not exactly.
  - The dispersion part of the deficit is $`\zeta^2\bigl(\overline{j^4}-\overline{j^2}^{\,2}\bigr)=\frac{\pi^2\epsilon^2(N^2-1)(N^2-4)}{180N^2}\frac{m^2}{\bar\mu^2}(1-\Gamma^2)^2`$. For $`N\ge3`$ and $`\sin p_0\ne0`$ it is nonzero: the levels $`\omega_k`$ are not equally spaced, so no $`\lambda`$ near $`\lambda_0(p_0)`$ gives exact certainty (cf. (2.9)).
  - Branch mixing adds a deficit of the same order, for every $`N`$; it is not computed.
- By (5.23), $`q(1;\lambda)=1-O((N\epsilon)^2)`$ in the whole window $`\lvert\xi\rvert\lesssim N\epsilon`$. The condition "certain up to the neglected order" thus locates the tick only to relative $`O(N\epsilon)`$, the size of the first-order term of (5.22).
- That term is fixed by the rate $`\Gamma`$ in (5.21): wherever $`\partial_\vartheta P_N\ne0`$, $`q`$ depends on $`\Gamma`$ at first order, with a second-order remainder. $`\lambda_0(p_0)`$ is the tick of the first-order distribution (5.21) in this sense.

### Step 8. Velocity of the item-3 start, to first order in $`\epsilon`$ (item 4)

The item-3 start is a superposition of all levels, and at level $`k\ne0`$ it is not purely in the positive branch (Step 6(i)). By Step 2(c), $`\mathrm d\bar x_{\rm lab}/\mathrm d\lambda`$ is the expectation of $`i[C_b,x]`$, which acts on $`\lvert p\rangle\otimes\cdot\otimes\lvert f_k\rangle`$ as $`\partial_pC_k(p)=-\tau\cos p\,\sigma_1`$. By (5.6), $`\beta_{k,\pm}^T(\partial_pC_k)\beta_{k,\pm}=\pm w_k`$ and $`\beta_{k,+}^T(\partial_pC_k)\beta_{k,-}=-\tau\cos p\cos\theta_k`$. The amplitude of level $`k`$ is $`N^{-1/2}g\,(\cos\delta_k\,e^{-i\omega_k\lambda}\beta_{k,+}+\sin\delta_k\,e^{i\omega_k\lambda}\beta_{k,-})`$. Hence, exactly under [W],
```math
\frac{\mathrm d\bar x_{\rm lab}}{\mathrm d\lambda}=\int\frac{\mathrm dp}{2\pi}\lvert g\rvert^2\,\frac1N\sum_{k=0}^{N-1}\Bigl[\cos2\delta_k\,w_k-\sin2\delta_k\,\tau\cos p\,\cos\theta_k\,\cos(2\omega_k\lambda)\Bigr].
\qquad\text{(5.24)}
```
- *Constant part.* $`\cos2\delta_k=1-O((N\epsilon)^2)`$. Write $`w_k=w(p;\mu_k)`$, with $`w(p;\mu):=\tau^2\sin p\cos p/\sqrt{\mu^2+\tau^2\sin^2p}`$ and $`\lvert\partial_\mu^2w\rvert\le2\tau/\mu^2`$. Since $`\frac1N\sum_k(d_k-\bar d)=0`$, the level average is $`w(p;\bar\mu)`$ up to $`\tau\epsilon^2\frac{N^2-1}{12}`$. [S] replaces $`p`$ by $`p_0`$.
- *Oscillating part.* It is of first order: to that order it equals $`w_0\gamma^2\frac1N\sum_k\frac{d_k}m\cos(2\omega_k\lambda)`$, and it cancels the first-order change of the constant part at $`\lambda=0`$. Its frequencies are $`2\omega_k\ge2m`$, so its mean vanishes. Its contribution to $`\bar x_{\rm lab}(\lambda)-\bar x_{\rm lab}(0)`$ is bounded for all $`\lambda`$ by $`\frac1N\sum_k\frac{\tau d_k}{2m}\frac1{2\omega_k}\le\frac{(N-1)\epsilon\,\tau}{8m}`$.

**The velocity used in item 4** is the mean of $`v`$ over $`[0,\lambda]`$, with $`\lambda`$ of the order of the tick. With $`\frac1{m\lambda}=\frac{N\epsilon}{2\pi\vartheta_0}`$:
```math
\bar v:=\frac{\bar x(\lambda)-\bar x(0)}{\lambda}=\kappa\sigma_X\,\bar w(p_0)\,\hat e+\mathcal R_v,\qquad\bar w(p):=w(p;\bar\mu)=\frac{\tau^2\sin p\cos p}{\sqrt{\bar\mu^2+\tau^2\sin^2p}} .
\qquad\text{(5.25)}
```
- Neglected, in units of $`\kappa\sigma_X`$: $`\tau\,O((N\epsilon)^2)`$ from the constant part; at most $`\tau\frac{N(N-1)\epsilon^2}{16\pi\vartheta_0}`$ from the oscillating part; $`\frac12\delta p^2\sup_p\lvert\partial_p^2\bar w\rvert`$ from [S]. No term of first order in $`\epsilon`$ is neglected.
- To first order, $`\bar w`$ is the velocity (5.9) of item 2(b) at $`\mu_k\to\bar\mu`$, the average of the $`w_k`$ over the levels. A single level differs from it at first order: $`w_k=\bar w\,[1-\Gamma^2(d_k-\bar d)/\bar\mu]+O(\epsilon^2)`$.
- The instantaneous $`v(\lambda)`$ of 03-ilang-space/17-motion differs from $`\bar v`$ at first order, by the oscillating part of (5.24).

### Step 9. Rate and velocity (item 4)

Below, $`\bar w:=\lvert\bar w(p_0)\rvert=\lVert\bar v\rVert/(\kappa\sigma_X)`$, and by (5.11) $`\lVert\bar v\rVert/v_{\max}=\bar w/\tau`$. The relations are identities between the first-order expressions (5.22) and (5.25). They are exact in $`p_0`$ and $`\tau/\bar\mu`$, and hold up to the second-order terms of (5.21) and (5.25).

**Exact relation on the chain.** By (5.22), $`\tau^2\sin^2p_0=\bar\mu^2(R^2-1)`$ and $`\tau^2\cos^2p_0=\bar W^2-\bar\mu^2R^2`$. Inserting these in $`\bar w^2=\tau^4\sin^2p_0\cos^2p_0/\bar\omega^2`$ gives
```math
\bar\mu^2R^4-(\bar W^2+\bar\mu^2-\bar w^2)R^2+\bar W^2=0 .
\qquad\text{(5.26)}
```
The discriminant is $`\bigl((\bar W-\bar\mu)^2-\bar w^2\bigr)\bigl((\bar W+\bar\mu)^2-\bar w^2\bigr)`$. It is nonnegative iff $`\bar w\le\bar W-\bar\mu`$, consistent with (5.10) at $`\mu_k\to\bar\mu`$. The roots are
```math
R=\frac{\sqrt{(\bar W+\bar\mu)^2-\bar w^2}\mp\sqrt{(\bar W-\bar\mu)^2-\bar w^2}}{2\bar\mu},\qquad\text{sign }-\text{ for }\sin^2p_0\le\frac{\bar\mu}{\bar\mu+\bar W},\quad\text{sign }+\text{ for }\sin^2p_0\ge\frac{\bar\mu}{\bar\mu+\bar W}.
\qquad\text{(5.27)}
```
- Squaring confirms the roots; their product is $`\bar W/\bar\mu`$.
- $`R`$ increases with $`\sin^2p_0`$, while $`\bar w`$ increases up to $`\sin^2p_0=\bar\mu/(\bar\mu+\bar W)`$ and then decreases (Step 5); this fixes the sign.
- At $`\bar w=0`$: $`R=1`$ ($`p_0=0,\pi`$) and $`R=\bar W/\bar\mu`$ ($`p_0=\pm\pi/2`$). At $`\bar w=\bar W-\bar\mu`$ both roots equal $`\sqrt{\bar W/\bar\mu}`$.
- So $`R`$ is a two-valued function of $`\lVert\bar v\rVert`$. The branch through $`p_0=0`$ has the sign $`-`$.
- Near the turning point $`\bar w=\bar W-\bar\mu`$, $`\partial R/\partial\bar w`$ diverges: there (5.27) is accurate to $`O(N\epsilon)`$ only, while (5.26) keeps its accuracy.

**Small $`p_0`$.** $`\bar\omega=\bar\mu+\frac{\tau^2p_0^2}{2\bar\mu}+O(p_0^4)`$ and $`\bar w=\frac{\tau^2\lvert p_0\rvert}{\bar\mu}+O(\lvert p_0\rvert^3)`$. Let $`v_{\rm top}:=\kappa\sigma_X(\bar W-\bar\mu)`$ be the largest velocity (5.10) at $`\mu_k\to\bar\mu`$. Then
```math
R=1+\frac{\lVert\bar v\rVert^2}{2v_{\max}^2}+O(p_0^4)=1+\frac{\bar W-\bar\mu}{2(\bar W+\bar\mu)}\,\frac{\lVert\bar v\rVert^2}{v_{\rm top}^2}+O(p_0^4).
\qquad\text{(5.28)}
```
**Comparison.** Exactly, $`1-\bar w^2/\tau^2=(\bar\mu^2+\tau^2\sin^4p_0)/\bar\omega^2`$. Hence
```math
R^2\Bigl(1-\frac{\lVert\bar v\rVert^2}{v_{\max}^2}\Bigr)=1+\frac{\tau^2}{\bar\mu^2}\sin^4p_0 .
\qquad\text{(5.29)}
```
- In units of the bound $`v_{\max}`$ of (17.7) of 03-ilang-space/17-motion, the coefficient in (5.28) is $`\frac12`$ for all $`\tau`$, $`m`$, $`N`$ and $`\epsilon`$ (to the order kept). In units of the largest velocity $`v_{\rm top}`$ it depends on $`\tau/\bar\mu`$.
- By (5.29), $`R=(1-\lVert\bar v\rVert^2/v_{\max}^2)^{-1/2}\sqrt{1+\tau^2\sin^4p_0/\bar\mu^2}`$. The correction factor is $`1+O(p_0^4)`$.
  - At fixed $`\lVert\bar v\rVert/v_{\max}<1`$ on the branch through $`p_0=0`$, the factor tends to $`1`$ as $`\bar\mu/\tau\to0`$, since there $`\sin p_0=O(\bar\mu/\tau)`$.
- Always $`\lVert\bar v\rVert/v_{\max}\le(\bar W-\bar\mu)/\tau<1`$: the bound is never reached, and $`R`$ stays finite. On the branch through $`p_0=0`$, $`R\le\sqrt{\bar W/\bar\mu}`$, with equality at $`v_{\rm top}`$.
- With $`\bar\mu\to m`$, (5.26)–(5.29) are the v1 relations; those hold at leading order in $`\epsilon`$ only, for $`R`$ and for $`\lVert\bar v\rVert`$ alike.

## Result

- **(5.2)** Decoupled body: $`q(a;\lambda)=\lvert\langle a\vert e^{-iD'\lambda}\vert\eta\rangle\rvert^2`$, exactly, for all $`\lambda`$. It does not depend on $`H`$, $`\phi_X`$, the $`K_x`$ or $`\chi`$.
- **(5.3)** The infinite chain is the limit $`L\to\infty`$, taken first at fixed $`\lambda`$. It is controlled by the locality bound (5.3) and, for $`\bar x`$ and $`v`$, by $`\lVert i[C,x]\rVert\le\tau`$.
- **(5.4)** $`AB+BA=0`$ and $`C_b^2=A^2+B^2`$.
- **(5.6)** For each level $`d_k`$, the eigenvalues are $`\pm\omega_k(p)=\pm\sqrt{(m+d_k)^2+\tau^2\sin^2p}`$, with eigenvectors $`\lvert p\rangle\otimes\beta_{k,\pm}(p)\otimes\lvert f_k\rangle`$.
- **(5.9)** $`v=\kappa\sigma_X\,w_k(p_0)\hat e`$, with $`w_k=\tau^2\sin p_0\cos p_0/\omega_k(p_0)`$.
- **(5.10)** Largest velocity: $`\kappa\sigma_X(\sqrt{\mu_k^2+\tau^2}-\mu_k)`$.
- **(5.11)** Bound (17.7) of 03-ilang-space/17-motion: $`v_{\max}=\tau\kappa\sigma_X`$, strictly larger.
- **(5.20)** $`\bar\mu=m+\langle0\vert D\vert0\rangle=m+\frac{\pi(N-1)}{N\lambda_0}`$, $`\bar\omega=\sqrt{\bar\mu^2+\tau^2\sin^2p}`$, rate $`\Gamma=\bar\mu/\bar\omega`$.
- **(5.21)** To first order in $`\epsilon`$: $`q(a;\lambda)=P_N(a;\Gamma(p_0)\lambda/\lambda_0)`$, i.e. (2.13) with $`\lambda\to\Gamma(p_0)\lambda`$; remainder $`O((N\epsilon)^2(1+\lambda/\lambda_0)^2)+O(\delta p^2)+O(\kappa)`$.
- **(5.22)** $`\lambda_0(p_0)=\lambda_0/\Gamma(p_0)`$ and $`R=\lambda_0(p_0)/\lambda_0(0)=\sqrt{1+(\tau/\bar\mu)^2\sin^2p_0}=\frac\omega m\bigl[1-\frac{(N-1)\epsilon}2\frac{\tau^2\sin^2p_0}{\omega^2}\bigr]+O((N\epsilon)^2)`$.
- **(5.23)** Near the tick, $`1-q(1;\lambda)=\frac{\pi^2(N^2-1)}{3N^2}\xi^2+O((N\epsilon)^2)`$: the certainty is exact only to first order, and the certainty condition alone fixes the tick only to relative $`O(N\epsilon)`$.
- **(5.24)** Velocity of the item-3 start: a constant part and a first-order part oscillating at the frequencies $`2\omega_k`$.
- **(5.25)** Mean velocity over the tick: $`\bar v=\kappa\sigma_X\bar w(p_0)\hat e`$, $`\bar w=\tau^2\sin p_0\cos p_0/\bar\omega(p_0)`$, to first order in $`\epsilon`$.
- **(5.26)** Exact relation on the chain: $`\bar\mu^2R^4-(\bar W^2+\bar\mu^2-\bar w^2)R^2+\bar W^2=0`$.
- **(5.27)** $`R=\bigl[\sqrt{(\bar W+\bar\mu)^2-\bar w^2}\mp\sqrt{(\bar W-\bar\mu)^2-\bar w^2}\bigr]/(2\bar\mu)`$, a two-valued function of $`\bar w=\lVert\bar v\rVert/(\kappa\sigma_X)`$.
- **(5.28)** Small $`p_0`$: $`R=1+\lVert\bar v\rVert^2/(2v_{\max}^2)+O(p_0^4)`$; the coefficient is universal only in units of the bound $`v_{\max}`$.
- **(5.29)** $`R^2(1-\lVert\bar v\rVert^2/v_{\max}^2)=1+(\tau/\bar\mu)^2\sin^4p_0`$.

## Consistency checks

1. **Dimensions.** $`[\tau]=[m]=[d_k]=[\bar\mu]=[C]=[\lambda]^{-1}`$, so $`\epsilon`$, $`\Gamma`$, $`R`$, $`\zeta`$, $`m\bar c`$ and $`\bar w/\tau`$ are dimensionless. $`[v]=[\kappa\sigma_X][C]`$, consistent with (5.9)–(5.11) and (5.25)–(5.29). Passed.
2. **$`p_0=0`$ and $`\tau\to0`$.**
   - At $`p=0`$, $`C_k(0)=\mu_k\sigma_3`$ and $`\beta_0(0)=(1,0)^T`$ is an eigenvector of every $`C_k(0)`$. (5.12) then gives exactly $`P_N(a;\lambda/\lambda_0)`$, i.e. (2.13), with no $`\epsilon`$ expansion. In (5.21): $`\Gamma(0)=1`$, $`\delta_k=0`$, $`\bar c=0`$ and $`\bar\rho_k=0`$, so no $`\epsilon`$-remainder. This agrees with (5.2).
   - Also $`w_k(0)=0`$ and $`\sin2\delta_k=0`$ in (5.24), so $`v=0`$; and $`R=1`$ by (5.27) with sign $`-`$.
   - For $`\tau\to0`$ the same holds for every $`p_0`$, and (5.10) and (5.11) tend to $`0`$. Passed.
3. **$`N=2`$.** Without branch mixing, (5.12) gives exactly $`q(0;\lambda)=\cos^2\bigl((\omega_1-\omega_0)\lambda/2\bigr)`$, and (5.21) gives $`P_2(0;\vartheta)=\cos^2(\pi\vartheta/2)`$ with $`\vartheta=\Gamma\lambda/\lambda_0`$. With $`d_1=\pi/\lambda_0`$ they agree iff $`(\omega_1-\omega_0)/d_1=\Gamma`$. The secant slope differs from the midpoint derivative $`\Gamma`$ by at most $`\frac{d_1^2}{24}\sup\lvert\partial_d^3\omega\rvert\le\frac{\epsilon^2}{24}`$, and $`\Gamma=\gamma[1+\frac\epsilon2(1-\gamma^2)]+O(\epsilon^2)`$ is the rate of the verifier's example. The v1 rate $`\gamma`$ fails this check at first order. No chirp remains, in agreement with the factor $`N^2-4`$ in Step 7. Passed.

## Open issues

- Terms of second order in $`\epsilon`$ are not computed: branch mixing, and the dispersion beyond (5.20). They make the certainty at the tick inexact at $`O((N\epsilon)^2)`$ and limit (5.21) to $`N\epsilon\,\lambda/\lambda_0\ll1`$, i.e. to fewer than about $`1/(N\epsilon)`$ ticks.
- The first-order term of the tick (5.22) is defined through the rate of the first-order distribution (5.21). The certainty condition of item 3, applied to the actual reading, resolves the tick only to relative $`O(N\epsilon)`$, by (5.23). Whether a later package needs a sharper operational definition of the tick is left to it.
- "In the branch of positive eigenvalue" is read as the product start with the spinor of level $`0`$, so that the clock label is exactly in $`\lvert0\rangle`$. The start projected on the positive branch of every level gives the same (5.21) and (5.25) to this order, without the oscillating part of (5.24); its clock label is in $`\lvert0\rangle`$ only up to $`O((N\epsilon)^2)`$ in the reading. This alternative is not worked out here.
- Effects of the records beyond leading order in $`\kappa`$ are out of scope: the drift from $`\langle X\rangle`$, and the decoherence of the view.
- (5.10) of 03-ilang-space/05-recording-contract assumes $`\phi_h\ne0`$ for all $`h`$, but the item-3 start has $`\phi_h=0`$ for $`a\ne0`$. Only $`u_h`$ and $`d_0`$ are used here, and they do not depend on $`\phi`$.
- The comparison of two carried clocks between two meetings is left to a later package.

## Methods used

- tensor-product factorization of commuting generators
- Dyson series and Duhamel formula (locality bound)
- bounded commutator $`i[C,x]`$ (velocity operator), strong convergence
- Fourier analysis on $`\mathbb Z`$, plane waves, position as $`i\partial_p`$
- anticommuting (Clifford) terms, $`2\times2`$ diagonalization, half-angle formulas
- group velocity, Hellmann–Feynman
- Taylor expansion with remainder bounds about the band centre, symmetry of the level sum
- geometric sums (Dirichlet kernel)
- spectral radius of path adjacency matrices
