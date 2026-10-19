# A body in a changing field: gradient seen, fall from rest, level dependence

- **Subproject:** 05-ilang-free-fall
- **Package:** 12-changing-field
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-11

## Setup and assumptions

**Model (assumption of the package, M8).** One body $`b`$ (Model D), one field $`f`$, one medium $`c`$, of pairwise different types (no swap condition). The contract of the question is (2.1) of 02-field-object with $`r=\{c\}`$ and one index:

```math
C=C_{br}\otimes\mathbb 1_f+B\otimes Y+\mathbb 1_{br}\otimes C_f,\qquad C_{br}:=C_{\rm D}\otimes\mathbb 1_c+\sum_x\lvert x\rangle\langle x\rvert\otimes\kappa\,x\,X,\qquad B:=\hat x\otimes G\otimes\mathbb 1_c ,
```

with $`G=\sigma_3\otimes(m\mathbb 1_N+D)`$, $`Y`$ and $`C_f`$ self-adjoint on a finite-dimensional $`\mathcal H_f`$, $`\lVert Y\rVert(L+1)<1`$, all contracts independent of $`\lambda`$ (A5), $`\lambda\ge0`$. The start is $`\Psi_0=\Psi_{br}\otimes\varphi`$ with $`\Psi_{br}=\phi\otimes\chi`$ and $`\varphi`$ any unit vector (A11).

**Gradient seen.** With $`P_e`$ the eigenprojectors of $`C_f`$ and $`\nu`$ running over the field frequencies ($`\nu=0`$ included),

```math
\gamma(\lambda)=\langle\varphi\vert e^{iC_f\lambda}Ye^{-iC_f\lambda}\vert\varphi\rangle=\sum_\nu\hat\gamma_\nu\,e^{i\nu\lambda},\qquad\hat\gamma_\nu:=\sum_{e-e'=\nu}\langle\varphi\vert P_eYP_{e'}\vert\varphi\rangle,\qquad\hat\gamma_{-\nu}=\hat\gamma_\nu^{*} ,\qquad\text{(12.1)}
```

a real trigonometric polynomial. It is constant on $`\lambda\ge0`$ iff $`\hat\gamma_\nu=0`$ for every $`\nu\neq0`$ (always so for the exceptional member $`Y=y\,\mathbb 1_f`$).

**Level notation.** Inside one level $`M:=M_k`$, $`\omega:=\omega_k`$, $`\theta:=\theta_k`$, a prime is $`\partial_p`$, $`\Delta:=\lambda-s`$, $`u:=1+\tau^2/M^2`$. From (5.6) of 04-ilang-time/05-moving-clock: $`\cos\theta=M/\omega`$, $`\sin\theta=-\tau\sin p/\omega`$, $`\omega'=\tau^2\sin p\cos p/\omega`$, $`\theta'=-\tau M\cos p/\omega^2`$, $`\omega\omega''+\omega'^2=\tau^2\cos2p`$.

**Functionals of a branch start $`B_{k,\sigma}[g]`$** (all integrals over $`(-\pi,\pi]`$):

```math
j_g(p):=\mathrm{Re}\bigl(g^{*}\,i\,g'\bigr),\qquad\chi_g:=2\int\frac{\mathrm dp}{2\pi}\,\sin p\;j_g=\langle\phi\vert\{\sin\hat p,\hat x\}\vert\phi\rangle,\qquad\rho_g:=\int\frac{\mathrm dp}{2\pi}\,\lvert\sin p\rvert\,\sin^2\tfrac p2\,\lvert j_g\rvert .\qquad\text{(12.2)}
```

$`j_g`$ is the position density of the start ($`\int\frac{\mathrm dp}{2\pi}j_g=\bar x_{\rm lab}(0)`$, because $`\beta_{k,\sigma}^{T}\beta_{k,\sigma}'=0`$); $`\chi_g`$ is its **position–label correlation**. The **class $`\mathcal S_\chi`$** ($`\chi\in\mathbb R`$) consists of the sequences of branch starts at rest with $`\delta p\to0`$, $`\rho_g\to0`$ and $`\chi_g\to\chi`$. Members: $`g=e^{-ipx_0}\times(\text{real function})`$ with fixed $`x_0\in\mathbb Z`$ gives $`j_g=x_0\lvert g\rvert^2`$, hence $`\mathcal S_0`$; a chirped start $`g\propto\exp[-(1+i\chi)p^2/4\delta p^2]`$ (smoothly cut off at $`\pm\pi`$) gives $`\mathcal S_\chi`$; a member of $`\mathcal S_0`$ evolved freely over $`\lambda_e`$ has $`\chi_g`$ increased by $`2\sigma\lambda_e\langle\omega'\sin p\rangle_g`$.

**Orders and regimes (A13).**
- First order in $`Y`$ at fixed $`\lambda`$, start and chain, then a long chain; for smooth $`g`$ the position amplitudes decay faster than any power, so the first-order coefficients of the chain $`\lvert x\rvert\le L`$ converge to those of the infinite chain.
- Records (items 2–4): $`\kappa\to0`$ at fixed $`\lambda`$, chain and start, $`\langle X\rangle=0`$. The medium has no contract of its own, so the $`O(\kappa)`$ term of the view of $`b`$ contains one factor $`\langle X\rangle`$ and vanishes ((8.19) of 04-ilang-time/08-maximal-speed); the place weights are those of $`\kappa=0`$ up to $`O(\kappa^2)`$.
- Two orders of limits for starts at rest: **(I)** $`\delta p\to0`$ at fixed $`\lambda`$; **(II)** $`\lambda\to\infty`$ at a fixed start, then $`\delta p\to0`$. They do not commute (Step 9).
- Inputs: as quoted in the question; (5.11) of 04-ilang-time/05-moving-clock and (8.1), (8.20) of 04-ilang-time/08-maximal-speed are not needed.

## Derivation

### Step 1. First order in the field (item 1a)

$`C_{br}\otimes\mathbb 1_f`$ and $`\mathbb 1_{br}\otimes C_f`$ commute. With $`B(s):=e^{iC_{br}s}Be^{-iC_{br}s}`$, $`Y(s):=e^{iC_fs}Ye^{-iC_fs}`$, the Dyson expansion in the term $`B\otimes Y`$ (convergent in finite dimension) gives

```math
\Psi(\lambda)=e^{-i(C_{br}+C_f)\lambda}\Bigl[\Psi_{br}\otimes\varphi-i\int_0^\lambda\mathrm ds\,B(s)\Psi_{br}\otimes Y(s)\varphi\Bigr]+O(\lVert Y\rVert^2).
```

Taking the partial trace over $`f`$ with $`\mathrm{Tr}_f\bigl[Y(s)\lvert\varphi\rangle\langle\varphi\rvert\bigr]=\gamma(s)\in\mathbb R`$, and $`\rho_0:=\lvert\Psi_{br}\rangle\langle\Psi_{br}\rvert`$:

```math
V(\lambda)=e^{-iC_{br}\lambda}\Bigl\{\rho_0-i\int_0^\lambda\mathrm ds\,\gamma(s)\,\bigl[B(s),\rho_0\bigr]\Bigr\}e^{iC_{br}\lambda}+O(\lVert Y\rVert^2).\qquad\text{(12.3)}
```

For a schedule, $`p(r_1,\dots,r_k)=\lVert\Pi_kU(\lambda_k-\lambda_{k-1})\cdots\Pi_1U(\lambda_1)\Psi_0\rVert^2`$ with projectors acting on $`\mathcal H_{br}`$ only; every first-order term contains exactly one factor $`Y(s)`$, $`s\in[0,\lambda_k]`$, between $`\langle\varphi\rvert`$ and $`\lvert\varphi\rangle`$, hence again $`\gamma(s)`$.

**Result 1(a).** *Class:* every $`C_f`$, $`Y`$, $`\varphi`$, every $`\Psi_{br}`$ (any $`\kappa`$). *Status:* exact first-order coefficient. The first-order term of the view of $`\{b,c\}`$ at $`\lambda`$, and of every schedule ending at $`\lambda_k`$, depends on $`(\varphi,C_f,Y)`$ only through the one real function $`\gamma`$ on $`[0,\lambda]`$ (on $`[0,\lambda_k]`$), i.e. through the finitely many numbers $`\hat\gamma_\nu`$ of (12.1). *Control:* the second-order term contains $`\langle\varphi\vert Y(s)Y(s')\vert\varphi\rangle`$, which is not a function of $`\gamma`$ (Step 3).

### Step 2. The generator and the two special cases (item 1b)

```math
C_{\rm eff}(\lambda):=C_{br}+\gamma(\lambda)\,B=C_{\rm D}\otimes\mathbb 1_c+\gamma(\lambda)\,\hat x\otimes G\otimes\mathbb 1_c+\sum_x\lvert x\rangle\langle x\rvert\otimes\kappa\,x\,X,\qquad i\,\frac{\mathrm d}{\mathrm d\lambda}\Psi_{\rm eff}=C_{\rm eff}(\lambda)\Psi_{\rm eff},\quad\Psi_{\rm eff}(0)=\Psi_{br}.\qquad\text{(12.4)}
```

Its Dyson expansion is that of Step 1 with $`Y(s)\to\gamma(s)`$, so $`V(\lambda)=\lvert\Psi_{\rm eff}(\lambda)\rangle\langle\Psi_{\rm eff}(\lambda)\rvert+O(\lVert Y\rVert^2)`$, and the same for every schedule: the body sees the factor $`1+\gamma(\lambda)x`$ on its rest and clock term.

- *Admissible?* By A5 the operators of a contract do not depend on $`\lambda`$. $`C_{\rm eff}(\lambda)`$ is the contract of an admissible description iff $`\gamma`$ is constant, i.e. iff $`\hat\gamma_\nu=0`$ for all $`\nu\neq0`$; it is then $`C_{\rm red}`$ of (2.3) of 02-field-object with $`n_1=\gamma`$ (a body with a place-dependent own term, A10, and its medium). Otherwise: **no**; it is a derived generator, not a description.
- *Sharp and stationary* ($`Y\varphi=\gamma\varphi`$, $`C_f\varphi=e_f\varphi`$): $`\gamma(\lambda)=\gamma`$, and by (2.3) $`\Psi(\lambda)=e^{-ie_f\lambda}e^{-iC_{\rm red}\lambda}\Psi_{br}\otimes\varphi`$: the statement of (a) holds at all orders in $`Y`$.
- *Field with (2.11)*: $`e^{-iC_f\lambda}\varphi`$ lies in the span of the $`C_f^{\,k}\varphi`$, so $`Ye^{-iC_f\lambda}\varphi=\gamma e^{-iC_f\lambda}\varphi`$ and $`\gamma(\lambda)=\gamma`$; by (2.12) $`V(\lambda)=\lvert\Psi_{\rm red}(\lambda)\rangle\langle\Psi_{\rm red}(\lambda)\rvert`$ exactly. The field changes with $`\lambda`$ ($`V_f`$ of (2.12)), the body does not see it.

### Step 3. Where the generator fails (item 1c)

Let $`\varphi`$ be sharp, $`Y\varphi=\gamma\varphi`$, with (2.11) violated. The view produced by (12.4) is pure at all orders, and by Step 2 it agrees with $`V(\lambda)`$ at the orders $`Y^0`$ and $`Y^1`$. By (2.14) of 02-field-object with $`J=\{1\}`$, $`B_1=B`$, $`n_1=\gamma`$:

```math
1-\mathrm{Tr}V(\lambda)^2=\frac{\lambda^4}{2}\,\Gamma\,\bigl\lVert(Y-\gamma)\,C_f\varphi\bigr\rVert^2+O(\lambda^5),\qquad\Gamma=\langle B^2\rangle_{\Psi_{br}}-\langle B\rangle_{\Psi_{br}}^2 ,\qquad\text{(12.5)}
```

which is homogeneous of degree two in $`Y`$. **Result 1(c):** the view first differs from the one of the generator at order $`Y^2`$ and at order $`\lambda^4`$, if $`(Y-\gamma)C_f\varphi\neq0`$ and $`\Gamma\neq0`$. Exceptional members: if (2.11) first fails at $`k_0>1`$, then $`(Y-\gamma(s))e^{-iC_fs}\varphi=O(s^{k_0})`$; the second-order difference of the views is bilinear in this vector at two parameters $`s,s'\le\lambda`$ and is integrated twice, so the order is $`Y^2`$ and $`\lambda^{2k_0+2}`$; if $`\Psi_{br}`$ is an eigenvector of $`B`$ ($`\Gamma=0`$) the coefficient of $`\lambda^4`$ vanishes.

### Step 4. First-order velocity in a gradient that changes with $`\lambda`$ (item 2a)

*Reduction.* By Step 2 and the record regime, the first-order place weights of a branch start are those of the body alone under $`C_{\rm D}+\gamma(\lambda)\hat x\otimes G`$. $`D`$ is conserved, and on the level $`k`$ the generator is, by (5.5) of 04-ilang-time/05-moving-clock ((4.2) of 04-branch-fall with $`B(p)=\gamma M\sigma_3`$, now with $`\gamma`$ depending on $`\lambda`$),

```math
C^{(k)}(\lambda)=C_0+\gamma(\lambda)\,M\,\hat x\,\sigma_3,\qquad C_0=-\tau\sin\hat p\,\sigma_1+M\sigma_3 .
```

*Velocity.* $`\frac{\mathrm d}{\mathrm d\lambda}\bar x_{\rm lab}=\langle i[C^{(k)}(\lambda),\hat x]\rangle=\langle\hat V\rangle`$ with $`\hat V=\partial_pC_0=-\tau\cos\hat p\,\sigma_1`$, because $`\hat x\sigma_3`$ commutes with $`\hat x=i\partial_p`$. With $`\phi_0(\lambda)=e^{-iC_0\lambda}\phi`$ (amplitude $`g\,e^{-i\sigma\omega\lambda}\beta_\sigma`$) and the first-order term $`\phi_1(\lambda)=-iM\int_0^\lambda\mathrm ds\,\gamma(s)\,e^{-iC_0\Delta}\,\hat x\sigma_3\,\phi_0(s)`$, the first-order velocity is $`v^{(1)}(\lambda)=2\mathrm{Re}\langle\phi_0(\lambda)\vert\hat V\vert\phi_1(\lambda)\rangle`$.

*Branch basis.* From (5.6) of 04-ilang-time/05-moving-clock: $`\sigma_3\beta_\sigma=\sigma\cos\theta\,\beta_\sigma-\sin\theta\,\beta_{-\sigma}`$, $`\hat V\beta_\sigma=\sigma\omega'\beta_\sigma+\omega\theta'\beta_{-\sigma}`$, $`\beta_\sigma'=\sigma\tfrac{\theta'}2\beta_{-\sigma}`$. Writing $`e^{i\sigma\omega s}\partial_p\bigl[g\,e^{-i\sigma\omega s}\sigma_3\beta_\sigma\bigr]=u_\sigma\beta_\sigma+u_{-\sigma}\beta_{-\sigma}`$,

```math
u_\sigma=\sigma\bigl[(g'-i\sigma\omega'sg)\cos\theta-\tfrac12\theta'g\sin\theta\bigr],\qquad u_{-\sigma}=-(g'-i\sigma\omega'sg)\sin\theta-\tfrac12\theta'g\cos\theta ,
```

```math
\langle\phi_0(\lambda)\vert\hat V\vert\phi_1(\lambda)\rangle=M\int_0^\lambda\mathrm ds\,\gamma(s)\int\frac{\mathrm dp}{2\pi}\,g^{*}\Bigl[\sigma\omega'\,u_\sigma+\omega\theta'\,e^{2i\sigma\omega\Delta}\,u_{-\sigma}\Bigr].
```

*Real part.* Use $`\mathrm{Re}(g^{*}g')=\tfrac12(\lvert g\rvert^2)'`$, $`\mathrm{Im}(g^{*}g')=-j_g`$, integrate the terms with $`(\lvert g\rvert^2)'`$ by parts ($`g`$ smooth and periodic), and use $`\omega\theta'\sin\theta=M\omega'/\omega`$, $`(\omega'\cos\theta)'+\omega'\theta'\sin\theta=\omega''\cos\theta`$, $`(\omega\theta'\sin\theta)'-\omega\theta'^2\cos\theta=(\omega\theta')'\sin\theta`$. The two terms that carry $`s`$ and $`\Delta`$ as factors combine to $`s+\Delta=\lambda`$. The result is

```math
\boxed{\;v^{(1)}_g(\lambda)=\int_0^\lambda\mathrm ds\;\gamma(s)\,\mathcal K_g(\lambda,s)\;}\qquad\text{(12.6)}
```

```math
\mathcal K_g(\lambda,s)=\Bigl\langle k_0+k_1\cos\bigl(2\omega(\lambda-s)\bigr)\Bigr\rangle_g-2\sigma M^2\int\frac{\mathrm dp}{2\pi}\,\frac{\omega'}{\omega}\,\sin\bigl(2\omega(\lambda-s)\bigr)\,\Bigl[j_g+\sigma\lambda\,\omega'\lvert g\rvert^2\Bigr],\qquad\text{(12.7)}
```

```math
k_0(p)=-\frac{M^2\omega''}{\omega}=-\frac{M^2\tau^2\bigl(M^2\cos2p-\tau^2\sin^4p\bigr)}{\omega^4},\qquad k_1(p)=M(\omega\theta')'\sin\theta=-\frac{M^2\tau^2(M^2+\tau^2)\sin^2p}{\omega^4}.
```

**Result 2(a).** *Class:* every level, both branches, every smooth $`g`$, every continuous $`\gamma`$. *Status:* exact first-order coefficient at $`\kappa\to0`$, $`\langle X\rangle=0`$. The bracket $`j_g+\sigma\lambda\omega'\lvert g\rvert^2`$ is the position density of the free motion at $`\lambda`$. Case distinction: if $`j_g=x_0\lvert g\rvert^2`$ the kernel is the average $`\langle\cdot\rangle_g`$ of an explicit function of $`(p,\lambda,s)`$, the bracket being $`(x_0+\sigma\lambda\omega')\lvert g\rvert^2`$; in general the start enters through $`j_g`$ as well, and no formula through $`\lvert g\rvert^2`$ alone exists (*control:* two starts with equal $`\lvert g\rvert^2`$ and different chirp have different kernels, Step 6).

### Step 5. Check against (4.7) for a constant $`\gamma`$

For $`\gamma(s)=\gamma`$, $`\int_0^\lambda\mathrm ds\,\sin(2\omega\Delta)=(1-\cos2\omega\lambda)/2\omega`$ and $`\int_0^\lambda\mathrm ds\,\cos(2\omega\Delta)=\sin(2\omega\lambda)/2\omega`$. The terms that grow are $`\gamma\lambda\langle k_0-M^2\omega'^2/\omega^2\rangle_g`$; the term $`\gamma\lambda M^2\langle\omega'^2\omega^{-2}\cos2\omega\lambda\rangle_g`$ is bounded for $`\lambda\ge0`$ after one integration by parts in $`p`$ ($`\cos2\omega\lambda=\partial_p\sin2\omega\lambda/2\omega'\lambda`$), and all others are bounded. With $`\omega\omega''+\omega'^2=\tau^2\cos2p`$:

```math
v^{(1)}_g(\lambda)=\gamma\,\lambda\,\langle\alpha_0\rangle_g+(\text{bounded}),\qquad\alpha_0(p):=-\frac{M_k^2\tau^2\cos2p}{\omega_k^2},
```

which is (4.7) of 04-branch-fall with $`G_k=\gamma M_k`$, $`\mathcal F_k=0`$, $`g_{\zeta,k}=0`$. The check passes.

### Step 6. Starts at rest, sharp label at fixed $`\lambda`$: kernel, velocity, acceleration (item 2b)

*Elementary bounds, all $`p`$, $`0\le s\le\lambda`$* (from the explicit forms; the last one uses $`1-\cos p=2\sin^2\frac p2`$, $`0\le\omega-M\le2\tau^2\sin^2\frac p2/M`$ and the mean value theorem for $`w\mapsto\sin(2w\Delta)/w^2`$ on $`w\ge M`$):

```math
0\le k_0+\tau^2\le2\tau^2u\sin^2p,\quad\lvert k_1\rvert\le\tau^2u\sin^2p,\quad2M^2\lambda\frac{\omega'^2}{\omega}\le\frac{2\tau^4\lambda}{M}\sin^2p,\quad\Bigl\lvert\frac{\omega'}{\omega}\sin(2\omega\Delta)-\frac{\tau^2}{M^2}\sin(2M\Delta)\sin p\Bigr\rvert\le\frac{4\tau^2}{M^2}\Bigl(u+\frac{\tau^2\lambda}{M}\Bigr)\lvert\sin p\rvert\sin^2\tfrac p2 .
```

At rest $`\langle\sin^2p\rangle_g\le\delta p^2`$. Inserting into (12.7), with (12.2): for **every** smooth $`g`$ at rest,

```math
\Bigl\lvert\mathcal K_g(\lambda,s)-K_{\chi_g}(\lambda-s)\Bigr\rvert\le4\tau^2\Bigl(u+\frac{\tau^2\lambda}{M}\Bigr)\bigl(\delta p^2+2\rho_g\bigr),\qquad\boxed{\;K_\chi(\Delta):=-\tau^2\bigl[1+\sigma\,\chi\,\sin(2M_k\Delta)\bigr]\;}\qquad\text{(12.8)}
```

**Kernel in closed form.** *Class:* sequences of $`\mathcal S_\chi`$, every level, both branches. *Order:* (I), $`\delta p\to0`$ at fixed $`\lambda`$, uniformly in $`s\in[0,\lambda]`$. *Status:* limit, with the exact bound (12.8) for each member. $`\mathcal K_g\to K_\chi`$; for a sequence with $`\rho_g\to0`$ the limit exists iff $`\chi_g`$ converges (for $`\sin2M_k\Delta\neq0`$). The level enters only through the term $`\sigma\chi\sin(2M_k\Delta)`$: for $`\chi=0`$ the kernel is $`-\tau^2`$, without memory.

**Velocity and acceleration, any continuous $`\gamma`$.** From (12.6) and (12.8), with the error at most $`4\tau^2\lambda\sup_{[0,\lambda]}\lvert\gamma\rvert\,(u+\tau^2\lambda/M)(\delta p^2+2\rho_g)`$ for each member, the limit of the velocity is the first formula of (12.9). The acceleration is derived on its own: by the Leibniz rule $`a^{(1)}_g(\lambda)=\gamma(\lambda)\mathcal K_g(\lambda,\lambda)+\int_0^\lambda\mathrm ds\,\gamma(s)\,\partial_\lambda\mathcal K_g(\lambda,s)`$, where

```math
\mathcal K_g(\lambda,\lambda)=\langle k_0+k_1\rangle_g=-\Bigl\langle\frac{M^2\tau^2\cos^2p}{\omega^2}\Bigr\rangle_g,\quad\partial_\lambda\mathcal K_g=-\Bigl\langle\Bigl(2\omega k_1+\frac{2M^2\omega'^2}{\omega}\Bigr)\sin(2\omega\Delta)+4M^2\lambda\,\omega'^2\cos(2\omega\Delta)\Bigr\rangle_g-4\sigma M^2\!\int\!\frac{\mathrm dp}{2\pi}\,\omega'\cos(2\omega\Delta)\,j_g ,
```

and the same bounds give $`\lvert\mathcal K_g(\lambda,\lambda)+\tau^2\rvert\le\tau^2u\,\delta p^2`$ and $`\lvert\partial_\lambda\mathcal K_g+2\sigma\chi_gM\tau^2\cos(2M\Delta)\rvert\le4M\tau^2(u+2\tau^2\lambda/M)(\delta p^2+2\rho_g)`$. Hence, in the limit (I) of the class $`\mathcal S_\chi`$,

```math
\boxed{\;v^{(1)}_{k,\sigma}(\lambda)=-\tau^2\!\int_0^\lambda\!\mathrm ds\,\gamma(s)\bigl[1+\sigma\chi\sin\bigl(2M_k(\lambda-s)\bigr)\bigr],\qquad a^{(1)}_{k,\sigma}(\lambda)=-\tau^2\gamma(\lambda)-2\sigma\chi M_k\tau^2\!\int_0^\lambda\!\mathrm ds\,\gamma(s)\cos\bigl(2M_k(\lambda-s)\bigr)\;}\qquad\text{(12.9)}
```

and for every smooth $`g`$ at rest, with $`a_{\chi_g}`$ the second expression of (12.9) at $`\chi=\chi_g`$ (exact bound):

```math
\bigl\lvert a^{(1)}_g(\lambda)-a_{\chi_g}(\lambda)\bigr\rvert\le\tau^2\sup_{[0,\lambda]}\lvert\gamma\rvert\,(1+4M\lambda)\Bigl(u+\frac{2\tau^2\lambda}{M}\Bigr)\bigl(\delta p^2+2\rho_g\bigr).\qquad\text{(12.10)}
```

(12.9) describes a fixed start as long as $`\lambda\ll\lambda_g:=M/\bigl[\tau^2(\delta p^2+2\rho_g)\bigr]`$.

### Step 7. One field frequency, $`\gamma(\lambda)=\gamma_0+\gamma_1\cos(\Omega\lambda+\vartheta)`$ (item 2b)

$`y(\lambda)=\int_0^\lambda\mathrm ds\,f(s)\sin(2M(\lambda-s))`$ is the solution of $`y''+4M^2y=2Mf`$, $`y(0)=y'(0)=0`$. For $`f=\cos(\Omega s+\vartheta)`$ and $`\Omega\neq2M`$ this gives $`y=\bigl[2M(\cos(\Omega\lambda+\vartheta)-\cos\vartheta\cos2M\lambda)+\Omega\sin\vartheta\sin2M\lambda\bigr]/(4M^2-\Omega^2)`$. Inserting into (12.9), for $`\Omega\neq2M_k`$ ($`M=M_k`$):

```math
\begin{aligned}v^{(1)}_{k,\sigma}(\lambda)={}&\underbrace{-\tau^2\gamma_0\,\lambda}_{\text{grows}}\;\underbrace{-\,\tau^2\gamma_1\Bigl[\frac{\sin(\Omega\lambda+\vartheta)}{\Omega}+\sigma\chi\,\frac{2M\cos(\Omega\lambda+\vartheta)}{4M^2-\Omega^2}\Bigr]}_{\text{frequency }\Omega}\\&\underbrace{+\,\sigma\chi\tau^2\Bigl[\frac{\gamma_0}{2M}\cos2M\lambda+\gamma_1\frac{2M\cos\vartheta\cos2M\lambda-\Omega\sin\vartheta\sin2M\lambda}{4M^2-\Omega^2}\Bigr]}_{\text{frequency }2M_k}\;\underbrace{+\,\tau^2\Bigl[\frac{\gamma_1\sin\vartheta}{\Omega}-\frac{\sigma\chi\gamma_0}{2M}\Bigr]}_{\text{constant}}\end{aligned}\qquad\text{(12.11)}
```

```math
\begin{aligned}a^{(1)}_{k,\sigma}(\lambda)={}&-\tau^2\gamma_0\;\underbrace{-\,\tau^2\gamma_1\Bigl[\cos(\Omega\lambda+\vartheta)-\sigma\chi\,\frac{2M\Omega\,\sin(\Omega\lambda+\vartheta)}{4M^2-\Omega^2}\Bigr]}_{\text{frequency }\Omega}\\&\underbrace{-\,\sigma\chi\tau^2\Bigl[\gamma_0\sin2M\lambda+\gamma_1\frac{4M^2\cos\vartheta\sin2M\lambda+2M\Omega\sin\vartheta\cos2M\lambda}{4M^2-\Omega^2}\Bigr]}_{\text{frequency }2M_k}\end{aligned}\qquad\text{(12.12)}
```

(12.12) follows from the second formula of (12.9) (equivalently, $`\mathrm d/\mathrm d\lambda`$ of (12.11)); $`v^{(1)}(0)=0`$ and $`a^{(1)}(0)=-\tau^2\gamma(0)`$ hold. **Result 2(b).** *Class:* $`\mathcal S_\chi`$, every level, both branches, all $`\gamma_0,\gamma_1,\vartheta`$, $`\Omega>0`$, $`\Omega\neq2M_k`$. *Order:* (I). *Status:* exact evaluation of the limit (12.9). The only part that grows is the drift $`-\tau^2\gamma_0\lambda`$ of the velocity; the acceleration has no growing part. The parts of frequency $`2M_k`$ are proportional to $`\chi`$ and are present already for a constant $`\gamma`$ (they are the bounded rest of (4.7)).

### Step 8. The response at the field frequency (item 3a)

Since $`\mathrm{Re}[(1+i\,b)e^{i\phi}]=\cos\phi-b\sin\phi`$, the part of (12.12) with the frequency $`\Omega`$ is $`\mathrm{Re}\bigl[\mathcal A_{k,\sigma}(\Omega)\gamma_1e^{i(\Omega\lambda+\vartheta)}\bigr]`$ with

```math
\boxed{\;\mathcal A_{k,\sigma}(\Omega)=-\tau^2\Bigl[1+i\,\sigma\,\chi\,\frac{2M_k\Omega}{4M_k^2-\Omega^2}\Bigr]\;},\qquad\Omega\neq2M_k .\qquad\text{(12.13)}
```

*Class, order, status:* as Result 2(b); exact.
- **$`\Omega\to0`$:** $`\mathcal A_{k,\sigma}\to-\tau^2`$ for every $`\chi`$, level and branch. This is (4.16) of 04-branch-fall per unit gradient: $`a_{k,\sigma}(0)=\frac{\tau^2}{M_k}(-G_k)=-\tau^2\gamma`$ for $`G_k=\gamma M_k`$, $`\mathcal F_k=0`$.
- **Same for all levels.** For two levels, $`\frac{M_k}{4M_k^2-\Omega^2}=\frac{M_{k'}}{4M_{k'}^2-\Omega^2}`$ is equivalent to $`(M_{k'}-M_k)(4M_kM_{k'}+\Omega^2)=0`$, which fails because the $`M_k=m+d_k`$ of Model D are positive and pairwise different ($`N\ge2`$). Hence, for starts of one class $`\mathcal S_\chi`$ on all levels and any $`\Omega>0`$ different from all $`2M_k`$: $`\mathcal A_{k,\sigma}(\Omega)`$ is the same for all levels **iff $`\chi=0`$**, and then also for both branches and all $`\Omega`$, with the value $`-\tau^2`$. If the classes differ between the levels ($`\chi_k`$), the condition is that $`\sigma_k\chi_kM_k/(4M_k^2-\Omega^2)`$ is the same for all levels; for all $`\Omega`$ of an interval this again means $`\chi_k=0`$ for all $`k`$.
- **Leading level dependence, $`\Omega\ll2M_k`$:** $`\mathcal A_{k,\sigma}(\Omega)=-\tau^2\bigl[1+i\sigma\chi\frac{\Omega}{2M_k}\bigl(1+O(\Omega^2/4M_k^2)\bigr)\bigr]`$: a phase shift of the response of relative size $`\lvert\chi\rvert\Omega/2M_k`$, opposite for the two branches.

### Step 9. Resonance $`\Omega=2M_k`$ and the other order of limits (item 3b)

*Order (I).* For $`f=\cos(2Ms+\vartheta)`$ the equation of Step 7 is resonant: $`y=\frac\lambda2\sin(2M\lambda+\vartheta)-\frac{\sin\vartheta\sin2M\lambda}{4M}`$. With (12.9), for the class $`\mathcal S_\chi`$ and $`\Omega=2M_k`$:

```math
v^{(1)}_{k,\sigma}(\lambda)=-\tau^2\gamma_0\lambda-\sigma\chi\,\tau^2\gamma_1\,\frac\lambda2\,\sin(2M_k\lambda+\vartheta)+(\text{bounded}),\qquad a^{(1)}_{k,\sigma}(\lambda)=-\tau^2\gamma(\lambda)-\sigma\chi\tau^2\Bigl[\gamma_1M_k\lambda\cos(2M_k\lambda+\vartheta)+\bigl(\gamma_0+\tfrac{\gamma_1}2\cos\vartheta\bigr)\sin2M_k\lambda\Bigr].\qquad\text{(12.14)}
```

The velocity carries an oscillation of frequency $`2M_k`$ whose amplitude grows linearly, $`\tfrac12\lvert\chi\gamma_1\rvert\tau^2\lambda`$ (the acceleration: $`\lvert\chi\gamma_1\rvert\tau^2M_k\lambda`$). In every other level the oscillating parts are bounded, by (12.11). For $`\chi=0`$ nothing grows besides the drift, and no level is distinguished.

*Order (II): fixed smooth $`g`$ (any $`p_0`$), $`\lambda\to\infty`$.* In (12.7) write $`\int_0^\lambda\mathrm ds\,e^{i\Omega s}\sin(2\omega\Delta)=e^{i\Omega\lambda}\int_0^\lambda\mathrm du\,e^{-i\Omega u}\sin2\omega u`$. By stationary phase, $`\langle W\sin2\omega u\rangle_g`$ decays like $`u^{-3/2}`$ for the weight $`W=\omega'^2/\omega`$, which vanishes to second order at all critical points of $`\omega`$ ($`\sin p\cos p=0`$); so the term of (12.7) with the factor $`\lambda`$ gives $`\lambda`$ times a convergent integral. The terms with $`k_1`$ and with $`j_g`$ have weights decaying like $`u^{-1/2}`$ and $`u^{-1}`$ and contribute $`O(\lambda^{1/2})`$. With the $`\gamma_0`$ part as in Step 5, for **every** $`\Omega>0`$ (leading order, rest $`O(\lambda^{1/2})`$):

```math
v^{(1)}_g(\lambda)=\lambda\Bigl\{\gamma_0\langle\alpha_0\rangle_g+\gamma_1\mathrm{Re}\bigl[c_g(\Omega)\,e^{i(\Omega\lambda+\vartheta)}\bigr]\Bigr\}+o(\lambda),\qquad c_g(\Omega):=-\lim_{\epsilon\to0^+}\Bigl\langle\frac{4M^2\omega'^2}{4\omega^2-(\Omega-i\epsilon)^2}\Bigr\rangle_g .\qquad\text{(12.15)}
```

Then $`\delta p\to0`$ at rest: $`\langle\alpha_0\rangle_g\to-\tau^2`$; for $`\Omega<2M_k`$, $`\lvert c_g\rvert\le4\tau^4\delta p^2/(4M^2-\Omega^2)\to0`$; for $`\Omega=2M_k`$, $`4\omega^2-4M^2=4\tau^2\sin^2p`$ gives $`c_g=-\langle M^2\tau^2\cos^2p/\omega^2\rangle_g\to-\tau^2`$ for **every** sequence at rest, whatever $`\chi_g`$; for $`\Omega>2M_k`$, $`c_g\to0`$ along sequences that vanish on a fixed neighbourhood of $`\{p:2\omega_k(p)=\Omega\}`$ (an empty set for $`\Omega>2\sqrt{M_k^2+\tau^2}`$).

**Result 3(b), the two orders.** (I) defines the response of a start for $`\lambda\ll\lambda_g`$: at $`\Omega=2M_k`$ the growing part is $`-\sigma\chi\tau^2\gamma_1\frac\lambda2\sin(2M_k\lambda+\vartheta)`$. (II) defines the long-run growth rate of the velocity of a fixed start: at $`\Omega=2M_k`$ it is $`-\tau^2\gamma_1\lambda\cos(2M_k\lambda+\vartheta)`$, independent of $`\chi`$. The two differ, so the limits do not commute at resonance; both agree on the drift $`-\tau^2\gamma_0\lambda`$ and, for $`\Omega<2M_k`$, on the absence of any other growth. What distinguishes the level $`k`$ with $`2M_k=\Omega`$: the field frequency equals the gap $`2\omega_k(0)`$ between its two branches at rest, and only there an oscillation of the velocity grows linearly.

### Step 10. Accuracy $`\delta`$ and the general statement (item 3c)

By (12.13), $`\lvert\mathcal A_{k,\sigma}(\Omega)+\tau^2\rvert\le\delta\,\tau^2`$ iff $`2M_k\Omega\lvert\chi\rvert\le\delta\,\lvert4M_k^2-\Omega^2\rvert`$, a quadratic inequality in $`\Omega`$:

```math
\bigl\lvert\mathcal A_{k,\sigma}(\Omega)+\tau^2\bigr\rvert\le\delta\,\tau^2\ \text{ for all levels}\iff\Omega\notin\bigcup_k\bigl(\Omega^{(k)}_-,\Omega^{(k)}_+\bigr),\qquad\Omega^{(k)}_\mp:=\frac{M_k}{\delta}\Bigl(\sqrt{\chi^2+4\delta^2}\mp\lvert\chi\rvert\Bigr),\quad\Omega^{(k)}_-\Omega^{(k)}_+=4M_k^2 .\qquad\text{(12.16)}
```

*Class, order, status:* $`\mathcal S_\chi`$, order (I), exact (iff). For $`\chi=0`$ the intervals are empty: every field frequency. For $`\delta\ll\lvert\chi\rvert`$: $`\Omega^{(k)}_-\approx2\delta M_k/\lvert\chi\rvert`$; the low-frequency condition for all levels is $`\Omega\le\Omega^{(0)}_-`$ ($`M_0=m`$ is the smallest). The parts of frequency $`2M_k`$ in (12.12) depend on the level with the relative size $`\lvert\chi\rvert(1+2M_k/\lvert2M_k-\Omega\rvert)`$ at most; lowering $`\Omega`$ does not remove them, an average over a long window does.

**General $`\gamma(\lambda)`$.** By (12.9), linear in $`\gamma`$, and (12.1): $`a^{(1)}_{k,\sigma}(\lambda)=-\tau^2\gamma(\lambda)+\sigma\chi\,R_k[\gamma](\lambda)`$ with $`R_k[\gamma](\lambda)=-2M_k\tau^2\int_0^\lambda\mathrm ds\,\gamma(s)\cos(2M_k(\lambda-s))`$; if no $`\lvert\nu\rvert`$ equals $`2M_k`$, $`a^{(1)}_{k,\sigma}(\lambda)=\sum_\nu\mathcal A_{k,\sigma}(\nu)\hat\gamma_\nu e^{i\nu\lambda}+(\text{terms of frequency }2M_k)`$, with $`\mathcal A_{k,\sigma}(-\nu)=\mathcal A_{k,\sigma}(\nu)^{*}`$. The statement that replaces "the fall is the same for all levels": *in the limit (I), the first-order acceleration from rest at $`\lambda`$ is $`-\tau^2`$ times the gradient seen at the same $`\lambda`$, for all levels and both branches, plus a term proportional to the position–label correlation $`\chi`$ of the start, which filters $`\gamma`$ at the frequency $`2M_k`$ of the level.* For $`\chi=0`$ the first term is all, for every $`\gamma(\cdot)`$; in order (II) the growth rate of the velocity is $`-\tau^2\gamma_0`$ ($`\gamma_0=\hat\gamma_0`$) for all levels if every field frequency in $`\gamma`$ is below $`2m`$.

### Step 11. Example and controls (item 4)

**(a) The field (2.13) coupled as a gradient.** $`e^{-iC_f\lambda}\lvert0\rangle=\cos(\gamma_f\lambda)\lvert0\rangle-i\sin(\gamma_f\lambda)\lvert1\rangle`$, hence

```math
\gamma(\lambda)=y\sin^2(\gamma_f\lambda)=\tfrac y2-\tfrac y2\cos(2\gamma_f\lambda):\qquad\gamma_0=\tfrac y2,\quad\gamma_1=-\tfrac y2,\quad\Omega=2\lvert\gamma_f\rvert,\quad\vartheta=0 .\qquad\text{(12.17)}
```

- *Item 1.* $`\varphi`$ is sharp ($`n_1=0`$) and not stationary; $`C_{\rm eff}(\lambda)`$ is not a contract; by (12.5) $`1-\mathrm{Tr}V^2=\tfrac12\lambda^4\,\Gamma\,y^2\gamma_f^2+O(\lambda^5)`$.
- *Item 2(b)*, class $`\mathcal S_\chi`$, order (I), $`\lvert\gamma_f\rvert\neq M_k`$, from (12.11), (12.12):
```math
v^{(1)}_{k,\sigma}=-\frac{\tau^2y}2\Bigl[\lambda-\frac{\sin2\gamma_f\lambda}{2\gamma_f}+\frac{\sigma\chi}{2M_k}\Bigl(1+\frac{\gamma_f^2\cos2M_k\lambda-M_k^2\cos2\gamma_f\lambda}{M_k^2-\gamma_f^2}\Bigr)\Bigr],\qquad a^{(1)}_{k,\sigma}=-\tau^2y\Bigl[\sin^2\gamma_f\lambda+\sigma\chi\,\frac{\gamma_f\bigl(M_k\sin2\gamma_f\lambda-\gamma_f\sin2M_k\lambda\bigr)}{2(M_k^2-\gamma_f^2)}\Bigr].
```
  The body starts with zero acceleration and drifts with $`-\tfrac12\tau^2y\,\lambda`$, the fall in the mean gradient $`y/2`$.
- *Item 3.* $`\mathcal A_{k,\sigma}(2\lvert\gamma_f\rvert)=-\tau^2\bigl[1+i\sigma\chi\,M_k\lvert\gamma_f\rvert/(M_k^2-\gamma_f^2)\bigr]`$; the same for all levels iff $`\chi=0`$, and then $`a^{(1)}_{k,\sigma}=-\tau^2y\sin^2\gamma_f\lambda`$ for every $`\gamma_f`$; to the accuracy $`\delta`$ iff $`\lvert\chi\rvert M_k\lvert\gamma_f\rvert\le\delta\lvert M_k^2-\gamma_f^2\rvert`$ for all $`k`$. At $`\lvert\gamma_f\rvert=M_k`$ the growing part of the velocity of the level $`k`$ is $`+\sigma\chi\tfrac14\tau^2y\,\lambda\sin2M_k\lambda`$ in order (I) and $`+\tfrac12\tau^2y\,\lambda\cos2M_k\lambda`$ in order (II), by (12.14), (12.15).

**(b) Controls.**
- *Sharp and stationary field:* $`\gamma(\lambda)=\gamma`$, $`\gamma_1=0`$. (12.6) reduces to (4.7) (Step 5); (12.9) gives $`a^{(1)}_{k,\sigma}=-\tau^2\gamma\,[1+\sigma\chi\sin2M_k\lambda]`$, whose window average and drift are (4.10), (4.11), (4.16) of 04-branch-fall, $`-\tau^2\gamma`$. Of item 3 only $`\mathcal A_{k,\sigma}(0)=-\tau^2`$ remains; there is no field frequency and no resonance. By (2.3) the body sees the contract $`C_{\rm red}`$ at all orders in $`Y`$.
- *$`[Y,C_f]=0`$, not sharp:* $`Y(s)=Y`$, so $`\gamma(\lambda)=\langle\varphi\vert Y\vert\varphi\rangle=:\bar\gamma`$ is constant although $`\varphi`$ need not be stationary. Results 1(a), 1(b) and items 2, 3 with $`\gamma_0=\bar\gamma`$, $`\gamma_1=0`$ describe it: at first order it acts as a sharp stationary field with the gradient $`\bar\gamma`$, and $`C_{\rm eff}`$ is an admissible contract. Result 1(c), (12.5) and the two special cases of Step 2 do not: $`Y`$ is conserved, $`V(\lambda)=\sum_yw_y\lvert\Psi_y(\lambda)\rangle\langle\Psi_y(\lambda)\rvert`$ with $`w_y`$ the weights of $`\varphi`$ on the eigenspaces of $`Y`$ and $`\Psi_y=e^{-i(C_{br}+yB)\lambda}\Psi_{br}`$, and $`1-\mathrm{Tr}V^2=2\lambda^2\,\Gamma\,\bigl(\langle Y^2\rangle_\varphi-\bar\gamma^2\bigr)+O(\lambda^3)`$: the difference from the generator is of order $`Y^2`$ already at $`\lambda^2`$ (the static field that is not sharp, outside this package).

### Step 12. Summary (item 5)

| Quantity | Stationary sharp field | What a field that is not stationary changes | Order in $`Y`$ | Field frequencies | Tags |
|---|---|---|---|---|---|
| Factor that the body sees | the number $`1+\gamma x`$; contract $`C_{\rm red}`$, exact | the function $`1+\gamma(\lambda)x`$; generator $`C_{\rm eff}(\lambda)`$, not a contract; beyond first order the view is mixed | $`Y^1`$: only $`\gamma(\cdot)`$; difference at $`Y^2`$ ($`\lambda^4`$ for a sharp start) | those with $`\hat\gamma_\nu\neq0`$; none under (2.11) or $`[Y,C_f]=0`$ | (12.1), (12.3)–(12.5) |
| Drift acceleration from rest | $`-\tau^2\gamma`$, (4.16) | (I): $`a^{(1)}=-\tau^2\gamma(\lambda)`$ plus a memory term $`\propto\chi`$; drift $`-\tau^2\gamma_0`$. (II): growth rate $`-\tau^2\gamma_0`$ plus $`\gamma_1\mathrm{Re}[c_ge^{i(\Omega\lambda+\vartheta)}]`$ | $`Y^1`$ | all; an oscillation grows only at $`\nu=2M_k`$ | (12.8)–(12.12), (12.14), (12.15) |
| Independence of the clock level | yes, $`-\tau^2`$ | $`\chi=0`$: kept at every frequency (I). $`\chi\neq0`$: relative deviation $`\lvert\chi\rvert\,2M_k\Omega/\lvert4M_k^2-\Omega^2\rvert`$. Lost at $`\Omega=2M_k`$ (in (II) for every $`\chi`$) | $`Y^1`$ | to accuracy $`\delta`$: $`\Omega\notin\bigcup_k(\Omega^{(k)}_-,\Omega^{(k)}_+)`$ | (12.13), (12.14), (12.16) |

## Result

Each result with its class, order of limits and status.

- **(12.3), (12.4)** — every $`C_f`$, $`Y`$, $`\varphi`$, $`\Psi_{br}`$; fixed $`\lambda`$; exact first-order coefficient. The view of $`\{b,c\}`$ and every schedule depend on the field only through $`\gamma(\cdot)`$ of (12.1), and are reproduced by the generator $`C_{\rm eff}(\lambda)=C_{br}+\gamma(\lambda)B`$, which is an admissible contract iff $`\gamma`$ is constant. Exact at all orders for a sharp stationary field (2.3) and under (2.11), by (2.12).
- **(12.5)** — sharp, not stationary; expansion in $`\lambda`$ at fixed operators; exact leading term. First difference from the generator at order $`Y^2`$, $`\lambda^4`$ ($`\lambda^{2k_0+2}`$ if (2.11) first fails at $`k_0`$).
- **(12.6), (12.7)** — every level, branch, smooth $`g`$, continuous $`\gamma`$; fixed start and $`\lambda`$, $`\kappa\to0`$, $`\langle X\rangle=0`$; exact first-order coefficient. $`v^{(1)}_g=\int_0^\lambda\gamma\,\mathcal K_g`$; the kernel involves $`\lvert g\rvert^2`$ and the position density $`j_g`$.
- **(12.8)–(12.10)** — starts at rest; exact bounds for each $`g`$; limit (I) for the class $`\mathcal S_\chi`$: $`K_\chi(\Delta)=-\tau^2[1+\sigma\chi\sin2M_k\Delta]`$, velocity and acceleration (12.9), the acceleration with its own bound (12.10).
- **(12.11), (12.12)** — $`\mathcal S_\chi`$, (I), $`\Omega\neq2M_k`$; exact. Parts of frequency $`\Omega`$, of frequency $`2M_k`$ ($`\propto\chi`$), and the drift $`-\tau^2\gamma_0\lambda`$.
- **(12.13)** — $`\mathcal A_{k,\sigma}(\Omega)=-\tau^2[1+i\sigma\chi\,2M_k\Omega/(4M_k^2-\Omega^2)]`$; $`\to-\tau^2`$, i.e. (4.16), for $`\Omega\to0`$; the same for all levels iff $`\chi=0`$; leading level dependence $`-i\sigma\chi\tau^2\Omega/2M_k`$.
- **(12.14), (12.15)** — $`\Omega=2M_k`$: linear growth of an oscillation of frequency $`2M_k`$ in the level $`k`$ only; coefficient $`-\sigma\chi\tau^2\gamma_1/2`$ (sine) in order (I), $`-\tau^2\gamma_1`$ (cosine) in order (II), leading order with rest $`O(\lambda^{1/2})`$; the limits do not commute.
- **(12.16)** — $`\mathcal S_\chi`$, (I), exact iff: the response at $`\Omega`$ is level-independent to the relative accuracy $`\delta`$ iff $`\Omega\notin\bigcup_k(\Omega^{(k)}_-,\Omega^{(k)}_+)`$; for a general $`\gamma`$: $`a^{(1)}_{k,\sigma}(\lambda)=-\tau^2\gamma(\lambda)+\sigma\chi R_k[\gamma](\lambda)`$.
- **(12.17)** — the two-place field: $`\gamma(\lambda)=y\sin^2\gamma_f\lambda`$, with the evaluations of Step 11 and the two controls.

## Consistency checks

1. **Constant $`\gamma`$.** (12.6), (12.7) give the growing part $`\gamma\lambda\langle\alpha_0\rangle_g`$ with $`\alpha_0=-M_k^2\tau^2\cos2p/\omega_k^2`$, which is (4.7) with $`G_k=\gamma M_k`$ (Step 5); at rest (12.9) gives $`-\tau^2\gamma[1+\sigma\chi\sin2M_k\lambda]`$ with the window average $`-\tau^2\gamma`$, which is (4.16). Passed.
2. **A gradient pulse, by an independent route.** $`\gamma(s)=\epsilon\,\delta(s-s_0)`$ acts as $`e^{-i\epsilon M\hat x\sigma_3}`$, a shift of the label by $`\mp\epsilon M`$ on the upper and lower component. For the branch $`+`$ at rest and a narrow $`g`$: the shift inside the branch changes the velocity by $`-\epsilon M\omega''(0)=-\epsilon\tau^2`$; the amplitude on $`\beta_-`$ is $`\tfrac{\epsilon\tau}2(2pg'+g)`$ to leading order, its overlap with $`g`$ is $`\int\frac{\mathrm dp}{2\pi}g^{*}(2pg'+g)=-i\chi_g`$, and with the off-diagonal element $`-\tau`$ of $`\hat V`$ and the phase $`e^{2iM\Delta}`$ it adds $`-\epsilon\tau^2\chi_g\sin2M\Delta`$. The sum is $`\epsilon K_{\chi_g}(\Delta)`$ of (12.8). Passed.
3. **Dimensions.** $`x`$, $`p`$, $`\gamma`$, $`\chi`$, $`\delta`$ are pure numbers; $`\tau`$, $`M`$, $`\omega`$, $`\Omega`$, $`\gamma_f`$ are costs, of dimension $`1/\lambda`$. A velocity is a cost: $`\tau^2\int\mathrm ds\,\gamma`$ in (12.9); an acceleration is a cost squared: $`\tau^2\gamma`$, $`\mathcal A_{k,\sigma}`$; the kernel (12.7) is a cost squared in every term ($`M^2\lambda\omega'^2/\omega`$ included); (12.5) is a pure number ($`\Gamma`$ and $`\lVert(Y-\gamma)C_f\varphi\rVert^2`$ are costs squared). Passed.

## Open issues

- The level-dependent part of the response at fixed $`\lambda`$ is carried entirely by the position–label correlation $`\chi`$ of the start; $`\chi_g`$ grows under free motion by $`2\sigma\lambda\langle\omega'\sin p\rangle_g`$, which is why the orders (I) and (II) differ. A formula uniform in $`\lambda`$ between $`\lambda\ll\lambda_g`$ and $`\lambda\gg\lambda_g`$ is not derived; the exact (12.6), (12.7) cover it implicitly.
- Order (II) for a field frequency inside the band, $`2M_k<\Omega\le2\sqrt{M_k^2+\tau^2}`$: $`c_g(\Omega)`$ of (12.15) is defined for every start, but its limit $`\delta p\to0`$ depends on the weight of the starts near the labels with $`2\omega_k(p)=\Omega`$, which $`\delta p\to0`$ does not control; it is evaluated only for sequences that vanish near these labels.
- Sequences at rest with $`\rho_g\not\to0`$ belong to no class $`\mathcal S_\chi`$; for them only (12.6), (12.7) and the bounds (12.8), (12.10) are available.
- The growth at $`\Omega=2M_k`$ is a statement on the first-order coefficient at each fixed $`\lambda`$; the range of $`\lambda`$ in which it is the leading effect needs the second order in $`Y`$, which is outside the scope (as is the mixing behind (12.5)).

## Methods used

- Dyson expansion (first-order perturbation theory) in a pair term; interaction picture
- Partial trace and views; purity of the view
- Plane-wave representation with $`\hat x=i\partial_p`$; two-branch decomposition of the level block
- Integration by parts on periodic functions; elementary bounds with explicit constants
- Duhamel formula and the driven oscillator equation (resonance)
- Stationary phase for the long-$`\lambda`$ behaviour; order of limits
