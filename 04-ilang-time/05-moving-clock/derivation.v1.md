# Moving clock: a ring clock carried by a body in the record background

- **Subproject:** 04-ilang-time
- **Package:** 05-moving-clock
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-10

## Setup and assumptions

- **System.** The body $`b`$ and the medium $`c`$ are each the only instance of their type, so no swap condition (1.11) applies. The joint space is $`\mathcal H=\mathcal H_b\otimes\mathcal H_c`$, with $`\mathcal H_c`$ finite-dimensional (A1).
  - Item 1: $`\mathcal H_b=\mathcal H_X\otimes\mathbb C^N`$, with places $`(x,a)`$.
  - Items 2–4: $`\mathcal H_b=\ell^2(\mathbb Z)\otimes\mathbb C^2\otimes\mathbb C^N`$ (position, branch, clock label), with places $`(x,s,a)`$, obtained as the limit of Step 2.
  - Contract: $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$ with $`K_h=K_x`$.
  - Start: $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$. We take $`\lambda\ge0`$ (A9 restricted).
- **Clock reading** (A8). It is applied at a stated $`\lambda`$. Its projectors are $`\Pi_a=\mathbb 1\otimes\lvert a\rangle\langle a\rvert\otimes\mathbb 1_c`$, with $`\lvert a\rangle\langle a\rvert`$ on the clock-label factor. By (1.3), $`q(a;\lambda)=\lVert\Pi_a\Psi(\lambda)\rVert^2`$ with $`\Psi(\lambda)=e^{-iC\lambda}(\phi\otimes\chi)`$.
- **Branch label.** $`\sigma_3\lvert1\rangle=\lvert1\rangle`$, $`\sigma_3\lvert2\rangle=-\lvert2\rangle`$, $`\sigma_1\lvert1\rangle=\lvert2\rangle`$. Spinors are written as columns $`(\beta_1,\beta_2)^T`$.
- **Clock inputs (02-clock@v2).** Take (2.9) with $`\alpha_m=0`$, $`\varepsilon=0`$, $`\ell_k=k`$. Then $`D=\sum_{k=0}^{N-1}d_k\lvert f_k\rangle\langle f_k\rvert`$, $`d_k=\frac{2\pi k}{N\lambda_0}`$, satisfies $`e^{-iD\lambda_0}=S`$. By (2.12) with $`c=0`$, it has the minimal spread for the start $`\lvert0\rangle`$.
  - (2.13) is its reading distribution. It is written below with the place called $`a`$, since $`m`$ denotes the mass parameter.
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
  - By Duhamel's formula, the exact state differs from this one by at most $`\int_0^\lambda\lVert\sum_x\lvert x\rangle\langle x\rvert\otimes K_x\Psi_0(\lambda')\rVert\mathrm d\lambda'\le\kappa\lVert X\rVert\lambda\sup_{\lambda'\le\lambda}\langle x^2\rangle_{\lambda'}^{1/2}`$. [W] is valid while this is $`\ll1`$.
- **Starts near $`p_0`$.** $`g`$ is smooth and $`2\pi`$-periodic, with $`\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g\rvert^2=1`$ and $`\lvert g\rvert^2`$ concentrated within $`\delta p`$ of $`p_0`$.
- **Clock parameter.** $`\epsilon:=\frac{2\pi}{N\lambda_0m}`$, so $`d_k=km\epsilon\le(N-1)m\epsilon`$. Item 3 needs $`N\epsilon\ll1`$.

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

**How the limit is taken.**
- First $`L\to\infty`$, at fixed $`\lambda`$, $`\kappa`$ and start. Then the order $`\kappa\to0`$ of [W], the leading order in the spread, and the expansion in $`\epsilon`$.
- Starts with rapidly decaying tails are approximated in norm by finitely supported ones; unitarity preserves the error.
- By (5.3) the tails stay superexponentially small. Hence $`q`$, $`p_h`$, $`\bar x`$ and $`v`$ converge.

**Plane waves.** On $`\ell^2(\mathbb Z)`$ we use the standard Fourier facts.
- The plane waves are $`\lvert p\rangle=\sum_xe^{ipx}\lvert x\rangle`$, $`p\in(-\pi,\pi]`$, with $`\langle p\vert p'\rangle=2\pi\delta(p-p')`$.
- With $`T:=\sum_x\lvert x+1\rangle\langle x\rvert`$, $`T\lvert p\rangle=e^{-ip}\lvert p\rangle`$.
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
The last term vanishes, because $`\beta_{k,+}`$ is real and of unit length. So $`\bar x_{\rm lab}`$ is exactly linear in $`\lambda`$, with the group velocity as slope:
```math
\frac{\mathrm d\bar x_{\rm lab}}{\mathrm d\lambda}=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g(p)\rvert^2\,\partial_p\omega_k(p)=\partial_p\omega_k(p_0)+O(\delta p).
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

### Step 6. Clock reading of the moving clock (item 3)

**Start.** $`\phi=\psi_{0,+}\otimes\lvert0\rangle`$. Write $`\beta_0:=\beta_{0,+}`$, $`\beta_{0,-}`$ for the other spinor of level $`0`$, and $`\omega:=\omega_0`$. Since $`\lvert0\rangle=N^{-1/2}\sum_k\lvert f_k\rangle`$, (5.5), [W] and Step 2 give
```math
q(a;\lambda)=\int\frac{\mathrm dp}{2\pi}\lvert g(p)\rvert^2\,\lVert\Phi_a(p,\lambda)\rVert^2,\qquad
\Phi_a:=\frac1N\sum_{k=0}^{N-1}e^{2\pi ika/N}\,e^{-iC_k(p)\lambda}\beta_0(p).
\qquad\text{(5.12)}
```
**Meaning of "first order in $`\epsilon`$".** Amplitudes are kept to first order in $`d_k/m\le(N-1)\epsilon`$. Phases $`\omega_k\lambda`$ are kept to first order in $`d_k`$, but $`d_k\lambda=2\pi k\lambda/(N\lambda_0)`$ is kept to all orders, since it is $`O(1)`$ at the $`\lambda`$ of interest.

*(i) Branch mixing.*
- $`\beta_{k,\pm}`$ is $`\beta_{0,\pm}`$ rotated by $`-\delta_k`$, with $`\delta_k:=(\theta_0-\theta_k)/2`$.
- $`\lvert\partial_\mu\theta\rvert=\tau\lvert\sin p\rvert/(\mu^2+\tau^2\sin^2p)\le1/(2\mu)`$, so $`\lvert\delta_k\rvert\le d_k/(4m)`$.
- Expanding $`\beta_0=\cos\delta_k\,\beta_{k,+}+\sin\delta_k\,\beta_{k,-}`$ and rotating back gives $`e^{-iC_k\lambda}\beta_0=\bigl(e^{-i\omega_k\lambda}+2i\sin^2\delta_k\sin\omega_k\lambda\bigr)\beta_0+i\sin2\delta_k\sin\omega_k\lambda\,\beta_{0,-}`$.
- Since $`\beta_0\perp\beta_{0,-}`$, the first-order term enters $`\lVert\Phi_a\rVert^2`$ only squared: $`\lVert\Phi_a\rVert^2=\bigl\lvert\frac1N\sum_ke^{2\pi ika/N-i\omega_k\lambda}\bigr\rvert^2+O((N\epsilon)^2)`$.
- There is thus no first-order correction. The same argument holds for any other reference level used to define "the positive branch".

*(ii) Dispersion.* Expand $`\omega_k`$ in $`d_k`$ by Taylor's theorem, using $`\partial_d^2\sqrt{(m+d)^2+\tau^2\sin^2p}=\tau^2\sin^2p/\omega_k^3\in[0,1/m]`$:
```math
\omega_k(p)=\omega(p)+\gamma(p)\,d_k+r_k(p),\qquad\gamma(p):=\frac{m}{\omega(p)}=\frac{m}{\sqrt{m^2+\tau^2\sin^2p}},\qquad0\le r_k\le\frac{d_k^2}{2m}.
\qquad\text{(5.13)}
```
Equivalently, by Hellmann–Feynman, $`\gamma=\cos\theta_0=\beta_0^T\sigma_3\beta_0`$: the clock term $`\sigma_3\otimes D`$ averaged in the positive branch.
- The common phase $`e^{-i\omega\lambda}`$ drops out of the modulus.
- Dropping $`r_k\lambda`$ changes $`\lVert\Phi_a\rVert^2`$ by at most $`2\max_kr_k\lambda\le2\pi\frac{(N-1)^2}{N}\epsilon\frac\lambda{\lambda_0}`$.
- With $`\gamma d_k\lambda=2\pi k\gamma\lambda/(N\lambda_0)`$, (5.1) gives $`\lVert\Phi_a\rVert^2=P_N(a;\gamma(p)\lambda/\lambda_0)`$.

*(iii) Spread.* Replacing $`\gamma(p)`$ by $`\gamma(p_0)`$ shifts the argument by $`O(\delta p\,\lvert\gamma'(p_0)\rvert\,\lambda/\lambda_0)`$. To leading order in $`\delta p`$:
```math
q(a;\lambda)=P_N\Bigl(a;\gamma(p_0)\frac{\lambda}{\lambda_0}\Bigr)=\frac{\sin^2\bigl(\pi\gamma(p_0)\lambda/\lambda_0\bigr)}{N^2\sin^2\bigl(\pi(\gamma(p_0)\lambda/\lambda_0-a)/N\bigr)},\qquad\gamma(p_0)=\frac{m}{\sqrt{m^2+\tau^2\sin^2p_0}} .
\qquad\text{(5.14)}
```
This is (2.13) with $`\lambda`$ replaced by $`\gamma(p_0)\lambda`$. The neglected terms are:
- $`O((N\epsilon)^2)`$ from (i);
- $`O(N\epsilon\,\lambda/\lambda_0)`$ from (ii);
- $`O(\delta p\,\lvert\gamma'(p_0)\rvert\,\lambda/\lambda_0)`$ from (iii);
- $`O(\kappa)`$ from [W].

### Step 7. Tick and ratio (item 3)

By (5.1), $`P_N(\cdot\,;\vartheta)`$ is concentrated on a single place iff $`\vartheta\in\mathbb Z`$, and then on $`a\equiv\vartheta`$. The reading starts at $`\vartheta=0`$. The first $`\lambda>0`$ at which it gives $`a=1`$ with certainty is therefore $`\gamma(p_0)\lambda=\lambda_0`$. Since $`\gamma(0)=1`$,
```math
\lambda_0(p_0)=\frac{\lambda_0}{\gamma(p_0)}=\lambda_0\sqrt{1+\frac{\tau^2}{m^2}\sin^2p_0},\qquad
R(p_0):=\frac{\lambda_0(p_0)}{\lambda_0(0)}=\frac{\omega(p_0)}{m}=\sqrt{1+\frac{\tau^2}{m^2}\sin^2p_0}\ \ge1 .
\qquad\text{(5.15)}
```
Relative to its rest rate, the carried clock advances at the rate $`\gamma(p_0)=1/R\le1`$. The rate equals $`1`$ only for $`\sin p_0=0`$. It is smallest at $`p_0=\pm\pi/2`$, where it equals $`m/W`$, with $`W:=\sqrt{m^2+\tau^2}`$.

### Step 8. Rate and velocity (item 4)

**The velocity used.** To the order of item 3 we may set $`\mu_k\to m`$ in (5.9). Then all levels of the item-3 start move, up to $`O(N\epsilon)`$, with $`\lVert v\rVert=\kappa\sigma_X\,w`$, where $`w:=\lvert w_0(p_0)\rvert`$. By (5.11), $`\lVert v\rVert/v_{\max}=w/\tau`$.

**Exact relation.** By (5.15), $`\tau^2\sin^2p_0=m^2(R^2-1)`$ and $`\tau^2\cos^2p_0=W^2-m^2R^2`$. Inserting these in $`w^2=\tau^4\sin^2p_0\cos^2p_0/\omega^2`$ gives
```math
m^2R^4-(W^2+m^2-w^2)R^2+W^2=0 .
\qquad\text{(5.16)}
```
The discriminant is $`\bigl((W-m)^2-w^2\bigr)\bigl((W+m)^2-w^2\bigr)`$. It is nonnegative iff $`w\le W-m`$, consistent with (5.10). The roots are
```math
R=\frac{\sqrt{(W+m)^2-w^2}\mp\sqrt{(W-m)^2-w^2}}{2m},\qquad\text{sign }-\text{ for }\sin^2p_0\le\frac{m}{m+W},\quad\text{sign }+\text{ for }\sin^2p_0\ge\frac{m}{m+W}.
\qquad\text{(5.17)}
```
- Squaring confirms the roots; their product is $`W/m`$.
- $`R`$ increases with $`\sin^2p_0`$, while $`w`$ increases up to $`u_*`$ and then decreases; this fixes the sign.
- At $`w=0`$: $`R=1`$ ($`p_0=0,\pi`$) and $`R=W/m`$ ($`p_0=\pm\pi/2`$). At $`w=W-m`$ both roots equal $`\sqrt{W/m}`$.
- So $`R`$ is a two-valued function of $`\lVert v\rVert`$. The branch through $`p_0=0`$ has the sign $`-`$.

**Small $`p_0`$.** $`\omega=m+\frac{\tau^2p_0^2}{2m}+O(p_0^4)`$ and $`w=\frac{\tau^2\lvert p_0\rvert}{m}+O(\lvert p_0\rvert^3)`$. Let $`v_{\rm top}:=\kappa\sigma_X(W-m)`$ be the largest velocity (5.10) at $`\mu_k=m`$. Then
```math
R=1+\frac{\lVert v\rVert^2}{2v_{\max}^2}+O(p_0^4)=1+\frac{W-m}{2(W+m)}\,\frac{\lVert v\rVert^2}{v_{\rm top}^2}+O(p_0^4).
\qquad\text{(5.18)}
```
**Comparison.** Exactly, $`1-w^2/\tau^2=(m^2+\tau^2\sin^4p_0)/\omega^2`$. Hence
```math
R^2\Bigl(1-\frac{\lVert v\rVert^2}{v_{\max}^2}\Bigr)=1+\frac{\tau^2}{m^2}\sin^4p_0 .
\qquad\text{(5.19)}
```
- In units of the bound $`v_{\max}`$ of (17.7) of 03-ilang-space/17-motion, the coefficient in (5.18) is universal: $`\frac12`$ for all $`\tau,m`$. In units of the largest velocity $`v_{\rm top}`$ it depends on $`\tau/m`$.
- By (5.19), $`R=(1-\lVert v\rVert^2/v_{\max}^2)^{-1/2}\sqrt{1+\tau^2\sin^4p_0/m^2}`$. The correction factor is $`1+O(p_0^4)`$.
  - At fixed $`\lVert v\rVert/v_{\max}<1`$ on the branch through $`p_0=0`$, the factor tends to $`1`$ as $`m/\tau\to0`$, since there $`\sin p_0=O(m/\tau)`$.
- Always $`\lVert v\rVert/v_{\max}\le(W-m)/\tau<1`$: the bound is never reached, and $`R`$ stays finite. On the branch through $`p_0=0`$, $`R\le\sqrt{W/m}`$, with equality at $`v_{\rm top}`$.

## Result

- **(5.2)** Decoupled body: $`q(a;\lambda)=\lvert\langle a\vert e^{-iD'\lambda}\vert\eta\rangle\rvert^2`$, exactly, for all $`\lambda`$. It does not depend on $`H`$, $`\phi_X`$, the $`K_x`$ or $`\chi`$.
- **(5.3)** The infinite chain is the limit $`L\to\infty`$, taken first at fixed $`\lambda`$. It is controlled by the locality bound (5.3).
- **(5.4)** $`AB+BA=0`$ and $`C_b^2=A^2+B^2`$. **(5.6)** For each level $`d_k`$, the eigenvalues are $`\pm\omega_k(p)=\pm\sqrt{(m+d_k)^2+\tau^2\sin^2p}`$, with eigenvectors $`\lvert p\rangle\otimes\beta_{k,\pm}(p)\otimes\lvert f_k\rangle`$.
- **(5.9)** $`v=\kappa\sigma_X\,w_k(p_0)\hat e`$, with $`w_k=\tau^2\sin p_0\cos p_0/\omega_k(p_0)`$. **(5.10)** Largest velocity: $`\kappa\sigma_X(\sqrt{\mu_k^2+\tau^2}-\mu_k)`$. **(5.11)** Bound (17.7) of 03-ilang-space/17-motion: $`v_{\max}=\tau\kappa\sigma_X`$, strictly larger.
- **(5.14)** $`q(a;\lambda)=P_N(a;\gamma(p_0)\lambda/\lambda_0)`$, i.e. (2.13) with $`\lambda\to\gamma(p_0)\lambda`$, where $`\gamma(p_0)=m/\sqrt{m^2+\tau^2\sin^2p_0}`$.
- **(5.15)** $`\lambda_0(p_0)=\lambda_0\sqrt{1+(\tau/m)^2\sin^2p_0}`$, and $`R=\lambda_0(p_0)/\lambda_0(0)=\omega(p_0)/m\ge1`$.
- **(5.17)** Exact relation: $`R=\bigl[\sqrt{(W+m)^2-w^2}\mp\sqrt{(W-m)^2-w^2}\bigr]/(2m)`$, a two-valued function of $`w=\lVert v\rVert/(\kappa\sigma_X)`$.
- **(5.18)** Small $`p_0`$: $`R=1+\lVert v\rVert^2/(2v_{\max}^2)+O(p_0^4)`$; the coefficient is universal only in units of the bound $`v_{\max}`$.
- **(5.19)** $`R^2(1-\lVert v\rVert^2/v_{\max}^2)=1+(\tau/m)^2\sin^4p_0`$.

## Consistency checks

1. **Dimensions.** $`[\tau]=[m]=[d_k]=[C]=[\lambda]^{-1}`$, so $`\epsilon`$, $`\gamma`$, $`R`$ and $`w/\tau`$ are dimensionless. $`[v]=[\kappa\sigma_X][C]`$, consistent with (5.9)–(5.11) and (5.17)–(5.19). Passed.
2. **$`p_0=0`$ and $`\tau\to0`$.**
   - At $`p=0`$, $`C_k(0)=\mu_k\sigma_3`$ and $`\beta_0(0)=(1,0)^T`$ is an eigenvector of every $`C_k(0)`$. (5.12) then gives exactly $`P_N(a;\lambda/\lambda_0)`$, i.e. (2.13), with no $`\epsilon`$ expansion. This agrees with (5.14) at $`\gamma(0)=1`$ and with (5.2).
   - Also $`v=0`$ by (5.9), and $`R=1`$ by (5.17) with sign $`-`$.
   - For $`\tau\to0`$ the same holds for every $`p_0`$, and (5.10) and (5.11) tend to $`0`$. Passed.
3. **$`N=2`$.** Directly, $`\lVert\Phi_0\rVert^2=\frac14\lvert1+e^{-i\pi\gamma\lambda/\lambda_0}\rvert^2=\cos^2(\pi\gamma\lambda/(2\lambda_0))`$. (5.14) gives $`\sin^2(\pi\vartheta)/(4\sin^2(\pi\vartheta/2))=\cos^2(\pi\vartheta/2)`$ with $`\vartheta=\gamma\lambda/\lambda_0`$. Passed.

## Open issues

- The curvature $`r_k`$ of $`\omega_k`$ in $`d_k`$ gives corrections $`O(N\epsilon\lambda/\lambda_0)`$ to (5.14) and relative corrections $`O(N\epsilon)`$ to $`\lambda_0(p_0)`$. A treatment consistent at fixed $`\lambda/\lambda_0`$ would replace $`\gamma(p_0)`$ by a level-weighted rate between $`\gamma`$ at $`\mu=m`$ and at $`\mu=m+d_{N-1}`$; this is not computed.
- The interbranch admixture of the item-3 start, of order $`N\epsilon`$, adds oscillating velocity terms of order $`N\epsilon`$; these are not computed.
- Effects of the records beyond leading order in $`\kappa`$ are out of scope: the drift from $`\langle X\rangle`$, and the decoherence of the view.
- (5.10) of 03-ilang-space/05-recording-contract assumes $`\phi_h\ne0`$ for all $`h`$, but the item-3 start has $`\phi_h=0`$ for $`a\ne0`$. Only $`u_h`$ and $`d_0`$ are used here, and they do not depend on $`\phi`$.
- The comparison of two carried clocks between two meetings is left to a later package.

## Methods used

- tensor-product factorization of commuting generators
- Dyson series and Duhamel formula (locality bound)
- Fourier analysis on $`\mathbb Z`$, plane waves, position as $`i\partial_p`$
- anticommuting (Clifford) terms, $`2\times2`$ diagonalization, half-angle formulas
- group velocity
- Taylor expansion with remainder bounds, Hellmann–Feynman
- geometric sums
- spectral radius of path adjacency matrices
