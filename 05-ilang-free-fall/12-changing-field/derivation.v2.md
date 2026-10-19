# A body in a changing field: gradient seen, fall from rest, level dependence

- **Subproject:** 05-ilang-free-fall
- **Package:** 12-changing-field
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-11

## Changes from previous version

- **Unchanged, word for word:** Setup; Steps 1–5; Step 6 up to and including (12.10); Step 7 except Result 2(b) as listed below; Step 8; in Step 9 the derivations of (12.14) and (12.15); in Step 10 the display (12.16); Step 11 item 2(b) and the controls (b); the three consistency checks. The tags (12.1)–(12.17) and their displays are unchanged; none is renumbered or withdrawn. New tags: (12.18)–(12.22).
- **Step 6 (I1).** The sentence "(12.9) describes a fixed start as long as $`\lambda\ll\lambda_g`$" is withdrawn. It is replaced by "Ranges of a fixed start" with (12.18): one range per quantity, each derived from the bound of that quantity, with the quantity against which the error is small.
- **Step 7 (I3).** Result 2(b): the sentence "the only part that grows" is now a statement on the limit functions (12.11), (12.12), and one sentence on a fixed start is added after it. The rest of Step 7 is word for word.
- **Step 9 (I1, I3).** The sentences on growth carry their order of limits and class of sequences. New paragraph "Between the two orders" with the exact (12.19) for a real start at resonance. Result 3(b) is rewritten: ranges per quantity, and what "distinguishes the level" means in each order.
- **Step 10 (I2).** (12.16) is kept and named for what it is: the exact criterion for the distance of the response from the quasistatic value. New: the level spread (12.20) with its exact criterion, its relation to (12.16), the closed form (12.21) below and above all gaps, the exceptional members, and a separate statement (12.22) on the complete acceleration. The sentence of v1 on the relative size of the parts of frequency $`2M_k`$ is replaced by part (B).
- **Step 11 (I4, I2).** Items 1 and 3 of (a): declarations for $`y\neq0`$, the case $`y=0`$, and the two criteria kept apart.
- **Step 12, Result, Open issues:** corrected accordingly.

## Response to verification

- **I1: Accepted and fixed** in Step 6 ("Ranges of a fixed start", (12.18)), Step 9 ("Between the two orders", (12.19), and Result 3(b)), Step 12 and Result. The verifier's term $`-2\tau^4\gamma_1\delta p^2\lambda^2\cos(2M\lambda)`$ is reproduced as the regime before dephasing of (12.19).
- **I2: Accepted and fixed** in Step 10 ((12.16) restated in words; (12.20)–(12.22)), Step 11(a) item 3, Step 12 (third row) and Result. The verifier's two-level example is the exceptional member "nearly equal data" of (A2).
- **I3: Accepted and fixed** in Step 7 (Result 2(b)), Step 9 (order (I) paragraph, the sentence after the limit $`\delta p\to0`$, Result 3(b)), Step 12 (second row) and Result.
- **I4: Accepted and fixed** in Step 11(a), item 1 and the lead sentence of item 3.

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

**Ranges of a fixed start.** Let $`w_g:=\delta p^2+2\rho_g`$, $`\Gamma_\lambda:=\sup_{[0,\lambda]}\lvert\gamma\rvert`$, and $`v_{\chi_g}`$ the first expression of (12.9) at $`\chi=\chi_g`$. The velocity bound stated above and (12.10) are, for every smooth $`g`$ at rest and every continuous $`\gamma`$ (exact),

```math
\bigl\lvert v^{(1)}_g-v_{\chi_g}\bigr\rvert\le E_v:=4\tau^2\Gamma_\lambda\,\lambda\Bigl(u+\frac{\tau^2\lambda}{M}\Bigr)w_g,\qquad\bigl\lvert a^{(1)}_g-a_{\chi_g}\bigr\rvert\le E_a:=\tau^2\Gamma_\lambda(1+4M\lambda)\Bigl(u+\frac{2\tau^2\lambda}{M}\Bigr)w_g,\qquad\lambda_g:=\frac{M}{\tau^2w_g},\quad\lambda_a:=\min\Bigl\{\frac{1}{Mu\,w_g},\frac{1}{\tau\sqrt{w_g}}\Bigr\}.\qquad\text{(12.18)}
```

A range in which (12.9) describes a fixed start is a statement on one quantity and is taken from the bound of that quantity. Each of the following is *sufficient* and holds for every continuous $`\gamma`$:
- *Velocity, against its growing drift* $`\tau^2\lvert\gamma_0\rvert\lambda`$ ($`\gamma`$ of Step 7, $`\gamma_0\neq0`$): the relative error is at most $`E_v/(\tau^2\lvert\gamma_0\rvert\lambda)=4(\Gamma_\lambda/\lvert\gamma_0\rvert)(u+\tau^2\lambda/M)\,w_g`$, small if $`u\,w_g\ll\lvert\gamma_0\rvert/\Gamma_\lambda`$ and $`\lambda\ll(\lvert\gamma_0\rvert/\Gamma_\lambda)\,\lambda_g`$.
- *Velocity, against a bounded oscillating part*, e.g. the part of frequency $`\Omega`$ of (12.11) with the amplitude $`\tau^2\lvert\gamma_1\rvert/\Omega`$: $`E_v\ll\tau^2\lvert\gamma_1\rvert/\Omega`$, i.e. $`4\Omega\lambda\,(u+\tau^2\lambda/M)\,w_g\ll\lvert\gamma_1\rvert/\Gamma_\lambda`$, a shorter range than that of the drift.
- *Acceleration, against its amplitude* $`\tau^2\Gamma_\lambda`$ (off resonance (12.12) is bounded and oscillating and has no growing part): the relative error is at most $`(1+4M\lambda)(u+2\tau^2\lambda/M)\,w_g`$, small if $`u\,w_g\ll1`$ and $`\lambda\ll\lambda_a`$.

$`\lambda_a\le\lambda_g`$ and $`\lambda_a/\lambda_g\le\tau\sqrt{w_g}/M\to0`$: the range $`\lambda\ll\lambda_g`$ of the drift of the velocity covers neither the acceleration nor the oscillating parts of the velocity. The member $`1/(\tau\sqrt{w_g})`$ of $`\lambda_a`$ is attained, up to a numerical factor, when $`\gamma`$ contains the frequency $`2M_k`$ ((12.19), Step 9). For a $`\gamma`$ without a frequency near $`2M_k`$ a longer range for the acceleration is not excluded; it is not derived here.

### Step 7. One field frequency, $`\gamma(\lambda)=\gamma_0+\gamma_1\cos(\Omega\lambda+\vartheta)`$ (item 2b)

$`y(\lambda)=\int_0^\lambda\mathrm ds\,f(s)\sin(2M(\lambda-s))`$ is the solution of $`y''+4M^2y=2Mf`$, $`y(0)=y'(0)=0`$. For $`f=\cos(\Omega s+\vartheta)`$ and $`\Omega\neq2M`$ this gives $`y=\bigl[2M(\cos(\Omega\lambda+\vartheta)-\cos\vartheta\cos2M\lambda)+\Omega\sin\vartheta\sin2M\lambda\bigr]/(4M^2-\Omega^2)`$. Inserting into (12.9), for $`\Omega\neq2M_k`$ ($`M=M_k`$):

```math
\begin{aligned}v^{(1)}_{k,\sigma}(\lambda)={}&\underbrace{-\tau^2\gamma_0\,\lambda}_{\text{grows}}\;\underbrace{-\,\tau^2\gamma_1\Bigl[\frac{\sin(\Omega\lambda+\vartheta)}{\Omega}+\sigma\chi\,\frac{2M\cos(\Omega\lambda+\vartheta)}{4M^2-\Omega^2}\Bigr]}_{\text{frequency }\Omega}\\&\underbrace{+\,\sigma\chi\tau^2\Bigl[\frac{\gamma_0}{2M}\cos2M\lambda+\gamma_1\frac{2M\cos\vartheta\cos2M\lambda-\Omega\sin\vartheta\sin2M\lambda}{4M^2-\Omega^2}\Bigr]}_{\text{frequency }2M_k}\;\underbrace{+\,\tau^2\Bigl[\frac{\gamma_1\sin\vartheta}{\Omega}-\frac{\sigma\chi\gamma_0}{2M}\Bigr]}_{\text{constant}}\end{aligned}\qquad\text{(12.11)}
```

```math
\begin{aligned}a^{(1)}_{k,\sigma}(\lambda)={}&-\tau^2\gamma_0\;\underbrace{-\,\tau^2\gamma_1\Bigl[\cos(\Omega\lambda+\vartheta)-\sigma\chi\,\frac{2M\Omega\,\sin(\Omega\lambda+\vartheta)}{4M^2-\Omega^2}\Bigr]}_{\text{frequency }\Omega}\\&\underbrace{-\,\sigma\chi\tau^2\Bigl[\gamma_0\sin2M\lambda+\gamma_1\frac{4M^2\cos\vartheta\sin2M\lambda+2M\Omega\sin\vartheta\cos2M\lambda}{4M^2-\Omega^2}\Bigr]}_{\text{frequency }2M_k}\end{aligned}\qquad\text{(12.12)}
```

(12.12) follows from the second formula of (12.9) (equivalently, $`\mathrm d/\mathrm d\lambda`$ of (12.11)); $`v^{(1)}(0)=0`$ and $`a^{(1)}(0)=-\tau^2\gamma(0)`$ hold. **Result 2(b).** *Class:* $`\mathcal S_\chi`$, every level, both branches, all $`\gamma_0,\gamma_1,\vartheta`$, $`\Omega>0`$, $`\Omega\neq2M_k`$. *Order:* (I). *Status:* exact evaluation of the limit (12.9). In the limit functions (12.11), (12.12) the only part that grows is the drift $`-\tau^2\gamma_0\lambda`$ of the velocity; the acceleration has no growing part. This is a statement on the limit (I); a fixed start is described by it within the ranges of (12.18), and in the long run its velocity carries the growing oscillation of (12.15). The parts of frequency $`2M_k`$ are proportional to $`\chi`$ and are present already for a constant $`\gamma`$ (they are the bounded rest of (4.7)).

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

The following are statements on the limit (I) of a class $`\mathcal S_\chi`$, i.e. on the limit functions (12.11), (12.14), not on a fixed start at all $`\lambda`$. The limit velocity carries an oscillation of frequency $`2M_k`$ whose amplitude grows linearly, $`\tfrac12\lvert\chi\gamma_1\rvert\tau^2\lambda`$ (the limit acceleration: $`\lvert\chi\gamma_1\rvert\tau^2M_k\lambda`$). In every level $`k'`$ with $`2M_{k'}\neq\Omega`$ the oscillating parts of the limit are bounded, by (12.11). For $`\chi=0`$ nothing grows in the limit (I) besides the drift, and no level is distinguished there.

*Order (II): fixed smooth $`g`$ (any $`p_0`$), $`\lambda\to\infty`$.* In (12.7) write $`\int_0^\lambda\mathrm ds\,e^{i\Omega s}\sin(2\omega\Delta)=e^{i\Omega\lambda}\int_0^\lambda\mathrm du\,e^{-i\Omega u}\sin2\omega u`$. By stationary phase, $`\langle W\sin2\omega u\rangle_g`$ decays like $`u^{-3/2}`$ for the weight $`W=\omega'^2/\omega`$, which vanishes to second order at all critical points of $`\omega`$ ($`\sin p\cos p=0`$); so the term of (12.7) with the factor $`\lambda`$ gives $`\lambda`$ times a convergent integral. The terms with $`k_1`$ and with $`j_g`$ have weights decaying like $`u^{-1/2}`$ and $`u^{-1}`$ and contribute $`O(\lambda^{1/2})`$. With the $`\gamma_0`$ part as in Step 5, for **every** $`\Omega>0`$ (leading order, rest $`O(\lambda^{1/2})`$):

```math
v^{(1)}_g(\lambda)=\lambda\Bigl\{\gamma_0\langle\alpha_0\rangle_g+\gamma_1\mathrm{Re}\bigl[c_g(\Omega)\,e^{i(\Omega\lambda+\vartheta)}\bigr]\Bigr\}+o(\lambda),\qquad c_g(\Omega):=-\lim_{\epsilon\to0^+}\Bigl\langle\frac{4M^2\omega'^2}{4\omega^2-(\Omega-i\epsilon)^2}\Bigr\rangle_g .\qquad\text{(12.15)}
```

Then $`\delta p\to0`$ at rest: $`\langle\alpha_0\rangle_g\to-\tau^2`$; for $`\Omega<2M_k`$, $`\lvert c_g\rvert\le4\tau^4\delta p^2/(4M^2-\Omega^2)\to0`$; for $`\Omega=2M_k`$, $`4\omega^2-4M^2=4\tau^2\sin^2p`$ gives $`c_g=-\langle M^2\tau^2\cos^2p/\omega^2\rangle_g\to-\tau^2`$ for **every** sequence at rest, whatever $`\chi_g`$; for $`\Omega>2M_k`$, $`c_g\to0`$ along sequences that vanish on a fixed neighbourhood of $`\{p:2\omega_k(p)=\Omega\}`$ (an empty set for $`\Omega>2\sqrt{M_k^2+\tau^2}`$).

Before this limit the coefficient does not vanish: for a fixed smooth $`g`$ and $`0<\Omega<2M_k`$, $`c_g(\Omega)=-\langle4M^2\omega'^2/(4\omega^2-\Omega^2)\rangle_g<0`$, because the integrand is positive except at the four zeros of $`\omega'`$. By (12.15) the velocity of a fixed start therefore carries, in every level and at every field frequency below the gap, an oscillation of frequency $`\Omega`$ with the linearly growing amplitude $`\lvert\gamma_1c_g(\Omega)\rvert\lambda`$; at rest it is of order $`\delta p^2`$ and disappears only in the subsequent limit $`\delta p\to0`$.

*Between the two orders: a fixed real start at resonance.* Let $`g`$ be real and at rest ($`j_g=0`$, hence $`\chi_g=\rho_g=0`$; a member of a sequence of $`\mathcal S_0`$) and $`\gamma=\gamma_1\cos(2M_k\lambda+\vartheta)`$ (a $`\gamma_0`$ adds the terms of Step 5, by linearity). Put $`j_g=0`$ into (12.7) and into $`\partial_\lambda\mathcal K_g`$ of Step 6 and use, with $`\eta(p):=\omega-M=\tau^2\sin^2p/(\omega+M)\le\tau^2\sin^2p/2M`$, the exact integral $`\int_0^\lambda\mathrm ds\,\cos(2Ms+\vartheta)\sin(2\omega\Delta)=\frac\lambda2\frac{\sin\eta\lambda}{\eta\lambda}\sin((\omega+M)\lambda+\vartheta)+\frac{\cos(2M\lambda+\vartheta)-\cos(2\omega\lambda-\vartheta)}{4(\omega+M)}`$ and its analogue with $`\cos(2\omega\Delta)`$ (first term with $`\cos((\omega+M)\lambda+\vartheta)`$, second term $`\frac{\sin(2M\lambda+\vartheta)+\sin(2\omega\lambda-\vartheta)}{4(\omega+M)}`$). With $`q_g:=\langle\sin^2p\rangle_g\le\delta p^2`$, for all $`\lambda\ge0`$ (exact):

```math
\begin{aligned}v^{(1)}_g(\lambda)&=-\tau^2\!\int_0^\lambda\!\mathrm ds\,\gamma(s)-\gamma_1\lambda^2\Bigl\langle\frac{M^2\omega'^2}{\omega}\,\frac{\sin\eta\lambda}{\eta\lambda}\,\sin\bigl((\omega+M)\lambda+\vartheta\bigr)\Bigr\rangle_g+r^v_g(\lambda),\qquad&\lvert r^v_g(\lambda)\rvert&\le4\tau^2u\,\lvert\gamma_1\rvert\,\lambda\,q_g,\\a^{(1)}_g(\lambda)&=-\tau^2\gamma(\lambda)-2\gamma_1\lambda^2\Bigl\langle M^2\omega'^2\,\frac{\sin\eta\lambda}{\eta\lambda}\,\cos\bigl((\omega+M)\lambda+\vartheta\bigr)\Bigr\rangle_g+r^a_g(\lambda),\qquad&\lvert r^a_g(\lambda)\rvert&\le\tau^2u\,\lvert\gamma_1\rvert\,(1+5M\lambda)\,q_g .\end{aligned}\qquad\text{(12.19)}
```

The rests collect the terms without the factor $`\lambda^2`$ (those of $`k_0+\tau^2`$, of $`k_1`$, and the second terms of the two integrals); they are bounded with the elementary bounds of Step 6 and $`\lvert\int_0^\lambda\mathrm ds\cdots\rvert\le\lambda`$. The velocity and the acceleration are each obtained from their own kernel.
- *Before dephasing*, $`(2u+\tau^2\lambda/M)\langle\sin^4p\rangle_g\ll q_g`$ (for a narrow Gaussian: $`u\,\delta p^2\ll1`$ and $`\lambda\ll\lambda_g/3`$). Since $`\lvert M^2\omega'^2-\tau^4\sin^2p\rvert\le\tau^4u\sin^4p`$ and $`\lvert\frac{\sin x}{x}\cos(a+x)-\cos a\rvert\le2\lvert x\rvert`$ (the same with sines), the two averages are $`\frac{\tau^4}{M}q_g\sin(2M\lambda+\vartheta)`$ and $`\tau^4q_g\cos(2M\lambda+\vartheta)`$ up to the relative error $`(2u+\tau^2\lambda/M)\langle\sin^4p\rangle_g/q_g`$. The finite-width terms are then $`-\frac{\tau^4\gamma_1q_g}{M}\lambda^2\sin(2M_k\lambda+\vartheta)`$ in the velocity and $`-2\tau^4\gamma_1q_g\,\lambda^2\cos(2M_k\lambda+\vartheta)`$ in the acceleration. They grow like $`\lambda^2`$, faster than the terms linear in $`\lambda`$ of the bounds. Against the amplitudes $`\tau^2\lvert\gamma_1\rvert/2M`$ and $`\tau^2\lvert\gamma_1\rvert`$ of the sharp-label velocity and acceleration both have the relative size $`2\tau^2q_g\lambda^2`$, which is one at $`\lambda=1/(\tau\sqrt{2q_g})\ll\lambda_g`$. The term $`8\tau^2\lambda^2w_g`$ of (12.10) is thus attained up to the factor 4.
- *After dephasing*, $`\lambda\to\infty`$ at fixed $`g`$: $`\lambda\frac{\sin\eta\lambda}{\eta\lambda}\sin((\omega+M)\lambda+\vartheta)=[\cos(2M\lambda+\vartheta)-\cos(2\omega\lambda+\vartheta)]/2\eta`$, and the velocity of (12.19), with the term of $`r^v_g`$ proportional to $`\lambda`$, becomes $`\lambda\gamma_1c_g(2M_k)\cos(2M_k\lambda+\vartheta)+O(\lambda^{1/2})`$, which is (12.15).
- *Not derived:* a closed form for $`\lambda\sim\lambda_g`$ through $`\delta p`$ and $`\chi_g`$ alone (the averages of (12.19) depend on the whole weight $`\lvert g\rvert^2`$); the analogue of (12.19) for starts with $`j_g\neq0`$, for which only (12.6), (12.7) and the bounds (12.18), (12.10) hold.

**Result 3(b), the two orders.** Each statement is on the named quantity, in the named order and class.
- *Order (I), class $`\mathcal S_\chi`$, $`\Omega=2M_k`$.* The limit velocity has the growing part $`-\sigma\chi\tau^2\gamma_1\frac\lambda2\sin(2M_k\lambda+\vartheta)`$ and the limit acceleration the growing part $`-\sigma\chi\tau^2\gamma_1M_k\lambda\cos(2M_k\lambda+\vartheta)`$, by (12.14). A fixed start has these growing parts, with $`\chi=\chi_g`$, up to the relative errors $`8(\Gamma_\lambda/\lvert\chi_g\gamma_1\rvert)(u+\tau^2\lambda/M)\,w_g`$ (velocity, from $`E_v`$) and, for $`M\lambda\ge1`$, $`5(\Gamma_\lambda/\lvert\chi_g\gamma_1\rvert)(u+2\tau^2\lambda/M)\,w_g`$ (acceleration, from $`E_a`$): sufficient is $`u\,w_g\ll\lvert\chi_g\gamma_1\rvert/\Gamma_\lambda`$ and $`\lambda\ll(\lvert\chi_g\gamma_1\rvert/\Gamma_\lambda)\,\lambda_g`$. The bounded parts of (12.14) are described only for $`\lambda\ll\lambda_a`$. For $`\chi_g=0`$ the range is empty: a fixed real start has no part growing like $`\lambda`$ but the oscillation growing like $`q_g\lambda^2`$ of (12.19).
- *Order (II), fixed smooth start, $`\lambda\to\infty`$.* By (12.15) the velocity has, in every level and at every $`\Omega>0`$, an oscillation of frequency $`\Omega`$ with the amplitude $`\lvert\gamma_1c_g(\Omega)\rvert\lambda`$; $`c_g(\Omega)<0`$ for $`0<\Omega<2M_k`$. After the subsequent limit $`\delta p\to0`$ at rest the coefficient is: $`-\tau^2\gamma_1\lambda\cos(2M_k\lambda+\vartheta)`$ at $`\Omega=2M_k`$, for every sequence at rest and independent of $`\chi`$; zero for $`\Omega<2M_{k'}`$ and for $`\Omega>2\sqrt{M_{k'}^2+\tau^2}`$, for every sequence at rest; zero for $`2M_{k'}<\Omega\le2\sqrt{M_{k'}^2+\tau^2}`$ for the sequences that vanish on a fixed neighbourhood of $`\{p:2\omega_{k'}(p)=\Omega\}`$, and not determined without this restriction (Open issues).
- *Comparison.* The two orders give different growing oscillations at $`\Omega=2M_k`$ (sine with the coefficient $`-\sigma\chi\tau^2\gamma_1/2`$ against cosine with $`-\tau^2\gamma_1`$), so the limits do not commute there; (12.19) shows the passage from one to the other for a real start. Both agree on the drift $`-\tau^2\gamma_0\lambda`$ and, for $`\Omega<2M_k`$ and after $`\delta p\to0`$, on the absence of any other growth.
- *What distinguishes the level $`k`$ with $`2M_k=\Omega`$.* The field frequency equals the gap $`2\omega_k(0)`$ between its two branches at rest. In the limit (I) with $`\chi\neq0`$ it is the only level whose limit velocity has a growing oscillation. In order (II) it is the only level whose growing oscillation survives the sharp-label limit, for the sequences named above. It is not true that an oscillation of the velocity of a fixed start grows only in this level.

### Step 10. Accuracy $`\delta`$ and the general statement (item 3c)

**Quantities compared.** All statements of this step are on the limit (I). On the level $`k`$ the starts form a class $`\mathcal S_{\chi_k}`$ on the branch $`\sigma_k`$; $`c_k:=\sigma_k\chi_k`$ and $`h_k(\Omega):=2M_k\Omega/(4M_k^2-\Omega^2)`$, so that $`\mathcal A_{k,\sigma_k}(\Omega)=-\tau^2[1+i\,c_kh_k(\Omega)]`$ by (12.13). Two quantities are kept apart: **(A)** the *response at the field frequency* $`\mathcal A_{k,\sigma}(\Omega)`$, the coefficient of the part of frequency $`\Omega`$ of (12.12), defined for $`\Omega\neq2M_k`$ (for every $`\Omega>0`$ if $`\chi_k=0`$, by (12.14)); **(B)** the *complete acceleration* $`a^{(1)}_{k,\sigma}(\lambda)`$ of (12.9), which contains in addition the parts of frequency $`2M_k`$, depending on the level and on the start. Relative accuracies are normalized by $`\tau^2=\lvert\mathcal A_{k,\sigma}(0)\rvert`$, the response to a constant gradient, which is common to all levels.

**(A1) Distance from the quasistatic value.** By (12.13), $`\lvert\mathcal A_{k,\sigma}(\Omega)+\tau^2\rvert\le\delta\,\tau^2`$ iff $`2M_k\Omega\lvert\chi\rvert\le\delta\,\lvert4M_k^2-\Omega^2\rvert`$, a quadratic inequality in $`\Omega`$:

```math
\bigl\lvert\mathcal A_{k,\sigma}(\Omega)+\tau^2\bigr\rvert\le\delta\,\tau^2\ \text{ for all levels}\iff\Omega\notin\bigcup_k\bigl(\Omega^{(k)}_-,\Omega^{(k)}_+\bigr),\qquad\Omega^{(k)}_\mp:=\frac{M_k}{\delta}\Bigl(\sqrt{\chi^2+4\delta^2}\mp\lvert\chi\rvert\Bigr),\quad\Omega^{(k)}_-\Omega^{(k)}_+=4M_k^2 .\qquad\text{(12.16)}
```

*Class, order, status:* one class $`\mathcal S_\chi`$ on all levels, order (I), exact (iff). For $`\chi=0`$ the intervals are empty: every field frequency. For $`\delta\ll\lvert\chi\rvert`$: $`\Omega^{(k)}_-\approx2\delta M_k/\lvert\chi\rvert`$; the low-frequency condition for all levels is $`\Omega\le\Omega^{(0)}_-`$ ($`M_0=m`$ is the smallest). *What (12.16) is the criterion for:* in every level and both branches the response at $`\Omega`$ lies within $`\delta\tau^2`$ of $`-\tau^2`$, i.e. $`\lvert\chi\rvert\max_k\lvert h_k(\Omega)\rvert\le\delta`$. It is not the criterion for the agreement between the levels; that is (A2). Below, $`\Omega^{(k)}_\mp(\delta')`$ are the numbers of (12.16) at the tolerance $`\delta'`$.

**(A2) Agreement between the levels.** The quantity compared is the **level spread**

```math
\mathcal D(\Omega):=\max_{k,k'}\frac{\bigl\lvert\mathcal A_{k,\sigma_k}(\Omega)-\mathcal A_{k',\sigma_{k'}}(\Omega)\bigr\rvert}{\tau^2}=\max_kc_kh_k(\Omega)-\min_kc_kh_k(\Omega),\qquad h_k(\Omega)-h_{k'}(\Omega)=\frac{2\Omega\,(M_{k'}-M_k)\,(4M_kM_{k'}+\Omega^2)}{(4M_k^2-\Omega^2)(4M_{k'}^2-\Omega^2)},\qquad\text{(12.20)}
```

and "the response at the field frequency is the same for all levels to the relative accuracy $`\delta`$" means $`\mathcal D(\Omega)\le\delta`$. (Normalizing by $`\lvert\mathcal A_{k,\sigma}\rvert\ge\tau^2`$ instead gives a smaller number, so $`\mathcal D\le\delta`$ is then sufficient.) *Class, order, status:* classes $`\mathcal S_{\chi_k}`$, order (I), $`\Omega`$ different from every $`2M_k`$ with $`\chi_k\neq0`$; exact.
1. *Necessary and sufficient.* $`\max_kc_kh_k(\Omega)-\min_kc_kh_k(\Omega)\le\delta`$. For one class $`\mathcal S_\chi`$ and one branch on all levels: $`\lvert\chi\rvert\max_{k,k'}\lvert h_k(\Omega)-h_{k'}(\Omega)\rvert\le\delta`$, with the second formula of (12.20). If both branches of all levels are compared in one class, $`\mathcal D(\Omega)=2\lvert\chi\rvert\max_k\lvert h_k(\Omega)\rvert`$, and the criterion is (12.16) at the tolerance $`\delta/2`$: $`\Omega\notin\bigcup_k(\Omega^{(k)}_-(\delta/2),\Omega^{(k)}_+(\delta/2))`$.
2. *Relation to (12.16), one class and one branch.* By the triangle inequality $`\mathcal D\le2\lvert\chi\rvert\max_k\lvert h_k\rvert`$: (12.16) at the tolerance $`\delta/2`$ is **sufficient** at every $`\Omega`$. If $`\Omega<2M_0=2m`$ or $`\Omega>2M_{N-1}`$, all $`h_k`$ have one sign and $`\mathcal D<\lvert\chi\rvert\max_k\lvert h_k\rvert`$: (12.16) at $`\delta`$ is sufficient, and not necessary. If $`2M_0<\Omega<2M_{N-1}`$, the $`h_k`$ have both signs and $`\mathcal D\ge\lvert\chi\rvert\max_k\lvert h_k\rvert`$: (12.16) at $`\delta`$ is **necessary**, and (12.16) at $`\delta/2`$ sufficient.
3. *Below and above all gaps, one class and one branch.* $`h_k(\Omega)`$ decreases with $`M_k`$ on each side of $`M_k=\Omega/2`$, so the extreme levels are $`k=0`$ and $`k=N-1`$ ($`M_{N-1}=m+d_{N-1}`$ is the largest):

```math
\mathcal D(\Omega)=\lvert\chi\rvert\,\frac{2\Omega\,(M_{N-1}-M_0)\,(4M_0M_{N-1}+\Omega^2)}{(4M_0^2-\Omega^2)(4M_{N-1}^2-\Omega^2)}\quad(\Omega<2M_0\ \text{or}\ \Omega>2M_{N-1});\qquad0<\Omega<2m:\ \ \mathcal D(\Omega)\le\delta\iff\Omega\le\Omega_\delta,\quad\Omega_\delta=\frac{2\delta}{\lvert\chi\rvert}\,\frac{M_0M_{N-1}}{M_{N-1}-M_0}\Bigl(1+O\bigl(\Omega_\delta^2/m^2\bigr)\Bigr).\qquad\text{(12.21)}
```

   On $`(0,2m)`$ the numerator increases and the denominator decreases, so $`\mathcal D`$ increases from $`0`$ to $`\infty`$ and $`\Omega_\delta`$ is its unique solution of $`\mathcal D=\delta`$; $`\Omega_\delta\ge\Omega^{(0)}_-(\delta)`$, larger by the factor $`M_{N-1}/(M_{N-1}-M_0)`$ at leading order. On $`(2M_{N-1},\infty)`$ the same expression decreases from $`\infty`$ to $`0`$, and $`\mathcal D\le\delta`$ above its unique solution there ($`\approx2\lvert\chi\rvert(M_{N-1}-M_0)/\delta`$ when this is $`\gg2M_{N-1}`$).
4. *Exceptional members.* (i) $`\chi_k=0`$ on all levels: $`\mathcal D(\Omega)=0`$ at every $`\Omega>0`$, the $`2M_k`$ included. (ii) Levels with nearly equal data: a pair contributes $`\lvert\chi\rvert\lvert h_k-h_{k'}\rvert\propto\lvert M_k-M_{k'}\rvert`$, so $`\mathcal D\le\delta`$ can hold where (12.16) fails; e.g. two levels $`M_1=M_0(1+\varepsilon)`$, $`\Omega=M_0`$, $`\chi=1`$, one branch: $`\mathcal D=\frac{10}9\varepsilon+O(\varepsilon^2)`$ while $`\lvert\chi h_0\rvert=\frac23`$. Exactly equal data of two levels do not occur in Model D ($`N\ge2`$), so for one class with $`\chi\neq0`$ and one branch $`\mathcal D(\Omega)>0`$ at every $`\Omega`$ (Step 8). (iii) $`\Omega`$ at or near a $`2M_k`$ with $`\chi_k\neq0`$: at $`\Omega=2M_k`$ the response $`\mathcal A_{k,\sigma}`$ does not exist (the part grows, (12.14)); $`\mathcal D(\Omega)\to\infty`$ for $`\Omega\to2M_k`$. In a window of length $`\Lambda`$ the part of frequency $`\Omega`$ is separated from the part of frequency $`2M_k`$ only if $`\Lambda\gg1/\lvert\Omega-2M_k\rvert`$, and for a fixed start the window must lie in the range $`\lambda\ll\lambda_a`$ of (12.18).

**(B) The complete acceleration.** By (12.9), with $`y_k`$ the solution of $`y_k''+4M_k^2y_k=2M_k\gamma`$, $`y_k(0)=y_k'(0)=0`$ (Step 7),

```math
a^{(1)}_{k,\sigma}(\lambda)=-\tau^2\gamma(\lambda)+\sigma\chi\,R_k[\gamma](\lambda),\qquad R_k[\gamma](\lambda):=-2M_k\tau^2\!\int_0^\lambda\!\mathrm ds\,\gamma(s)\cos\bigl(2M_k(\lambda-s)\bigr)=-\tau^2\,y_k'(\lambda).\qquad\text{(12.22)}
```

- *Exactly the same, necessary and sufficient.* For a continuous $`\gamma`$ that does not vanish identically on $`[0,\lambda_1]`$: the complete accelerations of all levels coincide on $`[0,\lambda_1]`$ **iff $`\chi_k=0`$ on every level**. Proof for two levels $`k\neq k'`$: $`c_ky_k'=c_{k'}y_{k'}'`$ gives $`z:=c_ky_k=c_{k'}y_{k'}`$, and the difference of the two equations gives $`4(M_k^2-M_{k'}^2)\,z=2(c_kM_k-c_{k'}M_{k'})\,\gamma`$ with $`M_k\neq M_{k'}`$. If not both $`c`$ vanish, either $`z\equiv0`$, or $`\gamma`$ is a constant multiple of $`z`$ and $`z`$ solves a homogeneous linear equation of second order with $`z(0)=z'(0)=0`$; in both cases $`z\equiv0`$, hence $`\gamma\equiv0`$. Exceptional member: $`\gamma\equiv0`$ (for example $`y=0`$ in Step 11), where all accelerations vanish.
- *To the accuracy $`\delta`$, sufficient only.* For $`\gamma`$ of Step 7 and $`\Omega\neq2M_k`$, (12.12) gives $`\lvert a^{(1)}_{k,\sigma}(\lambda)+\tau^2\gamma(\lambda)\rvert\le\lvert\chi\rvert\tau^2\bigl[\lvert\gamma_0\rvert+\lvert\gamma_1\rvert\frac{2M_k+\Omega}{\lvert2M_k-\Omega\rvert}\bigr]`$ for all $`\lambda\ge0`$. Hence $`2\max_k\lvert\chi_k\rvert\frac{2M_k+\Omega}{\lvert2M_k-\Omega\rvert}\le\delta`$ is sufficient for the complete accelerations of all levels and both branches to agree within $`\delta\,\tau^2(\lvert\gamma_0\rvert+\lvert\gamma_1\rvert)`$ at every $`\lambda\ge0`$. A necessary and sufficient condition is not derived. The condition is one on the start rather than on the field frequency: the part of frequency $`2M_k`$ of (12.12) has the amplitude $`\lvert\chi\rvert\tau^2\lvert\gamma(0)\rvert`$ for $`\Omega\to0`$, so lowering $`\Omega`$ does not remove it.
- *Window average.* The average of (12.12) over $`[\lambda_1,\lambda_1+\Lambda]`$ equals $`[v^{(1)}_{k,\sigma}(\lambda_1+\Lambda)-v^{(1)}_{k,\sigma}(\lambda_1)]/\Lambda`$, which by (12.11) is $`-\tau^2\gamma_0+O(1/\Lambda)`$ for every level, branch and $`\chi`$ if $`\Omega\neq2M_k`$: the drift acceleration of the limit (I) is the same for all levels at every such field frequency. At $`\Omega=2M_k`$ with $`\chi\neq0`$ the average does not converge, by (12.14).

**General $`\gamma(\lambda)`$.** By (12.9), linear in $`\gamma`$, and (12.1): (12.22) holds for every continuous $`\gamma`$; if no $`\lvert\nu\rvert`$ equals $`2M_k`$, $`a^{(1)}_{k,\sigma}(\lambda)=\sum_\nu\mathcal A_{k,\sigma}(\nu)\hat\gamma_\nu e^{i\nu\lambda}+(\text{terms of frequency }2M_k)`$, with $`\mathcal A_{k,\sigma}(-\nu)=\mathcal A_{k,\sigma}(\nu)^{*}`$, and (A1), (A2) apply to each $`\lvert\nu\rvert`$ separately. The statement that replaces "the fall is the same for all levels": *in the limit (I), the first-order acceleration from rest at $`\lambda`$ is $`-\tau^2`$ times the gradient seen at the same $`\lambda`$, for all levels and both branches, plus a term proportional to the position–label correlation $`\chi`$ of the start, which filters $`\gamma`$ at the frequency $`2M_k`$ of the level.* For $`\chi=0`$ the first term is all, for every $`\gamma(\cdot)`$ (limit (I); a fixed start within the ranges of (12.18)). In order (II) the coefficient of $`\lambda`$ in the velocity, after $`\delta p\to0`$ along any sequence at rest, is $`-\tau^2\gamma_0`$ ($`\gamma_0=\hat\gamma_0`$) for all levels if every field frequency in $`\gamma`$ is below $`2m`$; this condition is sufficient, and a frequency $`\lvert\nu\rvert=2M_k`$ adds the term of (12.15) in the level $`k`$.

### Step 11. Example and controls (item 4)

**(a) The field (2.13) coupled as a gradient.** $`e^{-iC_f\lambda}\lvert0\rangle=\cos(\gamma_f\lambda)\lvert0\rangle-i\sin(\gamma_f\lambda)\lvert1\rangle`$, hence

```math
\gamma(\lambda)=y\sin^2(\gamma_f\lambda)=\tfrac y2-\tfrac y2\cos(2\gamma_f\lambda):\qquad\gamma_0=\tfrac y2,\quad\gamma_1=-\tfrac y2,\quad\Omega=2\lvert\gamma_f\rvert,\quad\vartheta=0 .\qquad\text{(12.17)}
```

- *Item 1, $`y\neq0`$.* $`\varphi`$ is sharp ($`n_1=0`$) and not stationary: (2.11) fails at $`k=1`$, $`YC_f\varphi=y\gamma_f\lvert1\rangle\neq0`$. $`\gamma`$ is not constant, so $`C_{\rm eff}(\lambda)`$ is not a contract; by (12.5) $`1-\mathrm{Tr}V^2=\tfrac12\lambda^4\,\Gamma\,y^2\gamma_f^2+O(\lambda^5)`$.
- *Item 1, $`y=0`$* (allowed by the question). $`Y=0`$ and the pair term is absent. (2.11) holds with $`n_1=0`$, $`\gamma(\lambda)=0`$ for all $`\lambda`$, and $`C_{\rm eff}=C_{br}`$ is a constant, admissible contract; by (2.12) the view of $`\{b,c\}`$ is pure and is that of the body and the medium alone, at all orders. The state of the field still changes ($`V_f`$ of (2.12)); the body does not see it. Items 2 and 3 are then empty: $`\gamma_0=\gamma_1=0`$, all first-order velocities and accelerations vanish, and (12.5) gives zero.
- *Item 2(b)*, class $`\mathcal S_\chi`$, order (I), $`\lvert\gamma_f\rvert\neq M_k`$, from (12.11), (12.12):
```math
v^{(1)}_{k,\sigma}=-\frac{\tau^2y}2\Bigl[\lambda-\frac{\sin2\gamma_f\lambda}{2\gamma_f}+\frac{\sigma\chi}{2M_k}\Bigl(1+\frac{\gamma_f^2\cos2M_k\lambda-M_k^2\cos2\gamma_f\lambda}{M_k^2-\gamma_f^2}\Bigr)\Bigr],\qquad a^{(1)}_{k,\sigma}=-\tau^2y\Bigl[\sin^2\gamma_f\lambda+\sigma\chi\,\frac{\gamma_f\bigl(M_k\sin2\gamma_f\lambda-\gamma_f\sin2M_k\lambda\bigr)}{2(M_k^2-\gamma_f^2)}\Bigr].
```
  The body starts with zero acceleration and drifts with $`-\tfrac12\tau^2y\,\lambda`$, the fall in the mean gradient $`y/2`$.
- *Item 3, $`y\neq0`$, limit (I).* $`\mathcal A_{k,\sigma}(2\lvert\gamma_f\rvert)=-\tau^2\bigl[1+i\sigma\chi\,M_k\lvert\gamma_f\rvert/(M_k^2-\gamma_f^2)\bigr]`$ for $`\lvert\gamma_f\rvert\neq M_k`$; in one class $`\mathcal S_\chi`$ it is the same for all levels iff $`\chi=0`$, and then $`a^{(1)}_{k,\sigma}=-\tau^2y\sin^2\gamma_f\lambda`$ for every $`\gamma_f`$. It lies within $`\delta\tau^2`$ of $`-\tau^2`$ in every level iff $`\lvert\chi\rvert M_k\lvert\gamma_f\rvert\le\delta\lvert M_k^2-\gamma_f^2\rvert`$ for all $`k`$, by (12.16). It is the same for all levels to the accuracy $`\delta`$ (one branch) iff $`\mathcal D(2\lvert\gamma_f\rvert)=\lvert\chi\rvert\max_{k,k'}\bigl\lvert\frac{M_k\lvert\gamma_f\rvert}{M_k^2-\gamma_f^2}-\frac{M_{k'}\lvert\gamma_f\rvert}{M_{k'}^2-\gamma_f^2}\bigr\rvert\le\delta`$, by (12.20); for $`\lvert\gamma_f\rvert<m`$ iff $`2\lvert\gamma_f\rvert\le\Omega_\delta`$, by (12.21). The complete acceleration displayed above is the same for all levels iff $`\chi=0`$, by (12.22). At $`\lvert\gamma_f\rvert=M_k`$: in the limit (I) of $`\mathcal S_\chi`$ the growing part of the velocity of the level $`k`$ is $`+\sigma\chi\tfrac14\tau^2y\,\lambda\sin2M_k\lambda`$ and no other level has one, by (12.14); in order (II), after $`\delta p\to0`$ along any sequence at rest, it is $`+\tfrac12\tau^2y\,\lambda\cos2M_k\lambda`$, by (12.15), while a fixed start has the growing oscillation $`-\tfrac y2\lambda\mathrm{Re}[c_g(2\lvert\gamma_f\rvert)e^{2i\lvert\gamma_f\rvert\lambda}]`$ in every level.

**(b) Controls.**
- *Sharp and stationary field:* $`\gamma(\lambda)=\gamma`$, $`\gamma_1=0`$. (12.6) reduces to (4.7) (Step 5); (12.9) gives $`a^{(1)}_{k,\sigma}=-\tau^2\gamma\,[1+\sigma\chi\sin2M_k\lambda]`$, whose window average and drift are (4.10), (4.11), (4.16) of 04-branch-fall, $`-\tau^2\gamma`$. Of item 3 only $`\mathcal A_{k,\sigma}(0)=-\tau^2`$ remains; there is no field frequency and no resonance. By (2.3) the body sees the contract $`C_{\rm red}`$ at all orders in $`Y`$.
- *$`[Y,C_f]=0`$, not sharp:* $`Y(s)=Y`$, so $`\gamma(\lambda)=\langle\varphi\vert Y\vert\varphi\rangle=:\bar\gamma`$ is constant although $`\varphi`$ need not be stationary. Results 1(a), 1(b) and items 2, 3 with $`\gamma_0=\bar\gamma`$, $`\gamma_1=0`$ describe it: at first order it acts as a sharp stationary field with the gradient $`\bar\gamma`$, and $`C_{\rm eff}`$ is an admissible contract. Result 1(c), (12.5) and the two special cases of Step 2 do not: $`Y`$ is conserved, $`V(\lambda)=\sum_yw_y\lvert\Psi_y(\lambda)\rangle\langle\Psi_y(\lambda)\rvert`$ with $`w_y`$ the weights of $`\varphi`$ on the eigenspaces of $`Y`$ and $`\Psi_y=e^{-i(C_{br}+yB)\lambda}\Psi_{br}`$, and $`1-\mathrm{Tr}V^2=2\lambda^2\,\Gamma\,\bigl(\langle Y^2\rangle_\varphi-\bar\gamma^2\bigr)+O(\lambda^3)`$: the difference from the generator is of order $`Y^2`$ already at $`\lambda^2`$ (the static field that is not sharp, outside this package).

### Step 12. Summary (item 5)

| Quantity | Stationary sharp field | What a field that is not stationary changes | Order in $`Y`$ | Field frequencies | Tags |
|---|---|---|---|---|---|
| Factor that the body sees | the number $`1+\gamma x`$; contract $`C_{\rm red}`$, exact | the function $`1+\gamma(\lambda)x`$; generator $`C_{\rm eff}(\lambda)`$, not a contract; beyond first order the view is mixed | $`Y^1`$: only $`\gamma(\cdot)`$; difference at $`Y^2`$ ($`\lambda^4`$ for a sharp start) | those with $`\hat\gamma_\nu\neq0`$; none under (2.11) or $`[Y,C_f]=0`$ | (12.1), (12.3)–(12.5) |
| Drift acceleration from rest | $`-\tau^2\gamma`$, (4.16) | (I): $`a^{(1)}=-\tau^2\gamma(\lambda)`$ plus a memory term $`\propto\chi`$; drift $`-\tau^2\gamma_0`$. A fixed start: drift of the velocity for $`\lambda\ll\lambda_g`$, acceleration for $`\lambda\ll\lambda_a`$ (sufficient ranges). (II): coefficient of $`\lambda`$ in the velocity $`\gamma_0\langle\alpha_0\rangle_g+\gamma_1\mathrm{Re}[c_ge^{i(\Omega\lambda+\vartheta)}]`$ | $`Y^1`$ | all. Limit (I) of $`\mathcal S_\chi`$, $`\chi\neq0`$: an oscillation of the limit velocity grows only in the level with $`2M_k=\nu`$; $`\chi=0`$: in none. (II), fixed start: an oscillation grows in every level at every $`\nu`$; after $`\delta p\to0`$ it remains at $`\nu=2M_k`$, and vanishes for $`\nu<2M_k`$ (every sequence at rest) and for $`\nu>2M_k`$ along sequences vanishing near $`\{2\omega_k=\nu\}`$ | (12.8)–(12.12), (12.14), (12.15), (12.18), (12.19) |
| Independence of the clock level | yes, $`-\tau^2`$ | Limit (I). Response at $`\Omega`$: $`\chi=0`$: $`-\tau^2`$ in every level at every frequency; $`\chi\neq0`$: distance from $`-\tau^2`$ of relative size $`\lvert\chi\rvert\,2M_k\Omega/\lvert4M_k^2-\Omega^2\rvert`$, spread between levels $`\mathcal D(\Omega)`$; not defined at $`\Omega=2M_k`$. Complete acceleration: the same for all levels iff $`\chi=0`$ ($`\gamma\not\equiv0`$). Window-averaged acceleration: $`-\tau^2\gamma_0`$ for all levels, $`\Omega\neq2M_k`$. (II): the level with $`2M_k=\Omega`$ differs for every $`\chi`$ | $`Y^1`$ | spread $`\le\delta`$: iff (12.20); for $`\Omega<2m`$ iff $`\Omega\le\Omega_\delta`$. Within $`\delta`$ of $`-\tau^2`$ in every level: iff $`\Omega\notin\bigcup_k(\Omega^{(k)}_-,\Omega^{(k)}_+)`$; this is sufficient for the spread at $`\delta/2`$ (at $`\delta`$ below $`2m`$ and above $`2M_{N-1}`$), necessary at $`\delta`$ between $`2m`$ and $`2M_{N-1}`$. Complete acceleration: no condition on $`\Omega`$ alone; sufficient $`2\lvert\chi\rvert\max_k\frac{2M_k+\Omega}{\lvert2M_k-\Omega\rvert}\le\delta`$ | (12.13), (12.14), (12.16), (12.20)–(12.22) |

## Result

Each result with its class, order of limits and status.

- **(12.3), (12.4)** — every $`C_f`$, $`Y`$, $`\varphi`$, $`\Psi_{br}`$; fixed $`\lambda`$; exact first-order coefficient. The view of $`\{b,c\}`$ and every schedule depend on the field only through $`\gamma(\cdot)`$ of (12.1), and are reproduced by the generator $`C_{\rm eff}(\lambda)=C_{br}+\gamma(\lambda)B`$, which is an admissible contract iff $`\gamma`$ is constant. Exact at all orders for a sharp stationary field (2.3) and under (2.11), by (2.12).
- **(12.5)** — sharp, not stationary; expansion in $`\lambda`$ at fixed operators; exact leading term. First difference from the generator at order $`Y^2`$, $`\lambda^4`$ ($`\lambda^{2k_0+2}`$ if (2.11) first fails at $`k_0`$).
- **(12.6), (12.7)** — every level, branch, smooth $`g`$, continuous $`\gamma`$; fixed start and $`\lambda`$, $`\kappa\to0`$, $`\langle X\rangle=0`$; exact first-order coefficient. $`v^{(1)}_g=\int_0^\lambda\gamma\,\mathcal K_g`$; the kernel involves $`\lvert g\rvert^2`$ and the position density $`j_g`$.
- **(12.8)–(12.10)** — starts at rest; exact bounds for each $`g`$; limit (I) for the class $`\mathcal S_\chi`$: $`K_\chi(\Delta)=-\tau^2[1+\sigma\chi\sin2M_k\Delta]`$, velocity and acceleration (12.9), the acceleration with its own bound (12.10).
- **(12.18)** — every smooth $`g`$ at rest, every continuous $`\gamma`$; exact bounds $`E_v`$, $`E_a`$; sufficient ranges, one per quantity: the drift of the velocity for $`\lambda\ll(\lvert\gamma_0\rvert/\Gamma_\lambda)\lambda_g`$; the oscillating parts of the velocity for $`4\Omega\lambda(u+\tau^2\lambda/M)w_g\ll\lvert\gamma_1\rvert/\Gamma_\lambda`$; the acceleration, against its amplitude, for $`\lambda\ll\lambda_a\le\lambda_g`$. The range of the velocity does not cover the acceleration.
- **(12.11), (12.12)** — $`\mathcal S_\chi`$, (I), $`\Omega\neq2M_k`$; exact. Parts of frequency $`\Omega`$, of frequency $`2M_k`$ ($`\propto\chi`$), and the drift $`-\tau^2\gamma_0\lambda`$, the only growing part of the limit functions.
- **(12.13)** — $`\mathcal A_{k,\sigma}(\Omega)=-\tau^2[1+i\sigma\chi\,2M_k\Omega/(4M_k^2-\Omega^2)]`$; $`\to-\tau^2`$, i.e. (4.16), for $`\Omega\to0`$; the same for all levels iff $`\chi=0`$; leading level dependence $`-i\sigma\chi\tau^2\Omega/2M_k`$.
- **(12.14), (12.15), (12.19)** — $`\Omega=2M_k`$. Limit (I) of $`\mathcal S_\chi`$: the limit velocity of the level $`k`$, and of no other level, has an oscillation of frequency $`2M_k`$ growing linearly, coefficient $`-\sigma\chi\tau^2\gamma_1/2`$ (sine); none for $`\chi=0`$; a fixed start has it for $`\lambda\ll(\lvert\chi_g\gamma_1\rvert/\Gamma_\lambda)\lambda_g`$ (sufficient). Order (II), fixed start: leading order with rest $`O(\lambda^{1/2})`$, a growing oscillation $`\lambda\gamma_1\mathrm{Re}[c_g(\Omega)e^{i(\Omega\lambda+\vartheta)}]`$ in every level at every $`\Omega`$; after $`\delta p\to0`$ at rest its coefficient is $`-\tau^2\gamma_1`$ (cosine) at $`\Omega=2M_k`$ for every sequence, zero below $`2M_k`$ for every sequence, zero above $`2M_k`$ for sequences vanishing near $`\{2\omega_k=\Omega\}`$. The limits do not commute. (12.19): real start at resonance, exact; before dephasing the finite-width terms are $`-(\tau^4\gamma_1q_g/M)\lambda^2\sin(2M_k\lambda+\vartheta)`$ (velocity) and $`-2\tau^4\gamma_1q_g\lambda^2\cos(2M_k\lambda+\vartheta)`$ (acceleration), of relative size one at $`\lambda=1/(\tau\sqrt{2q_g})`$.
- **(12.16), (12.20), (12.21)** — limit (I), response at the field frequency, normalized by $`\tau^2`$. (12.16), one class $`\mathcal S_\chi`$, exact iff: the response lies within $`\delta\tau^2`$ of $`-\tau^2`$ in every level iff $`\Omega\notin\bigcup_k(\Omega^{(k)}_-,\Omega^{(k)}_+)`$. (12.20): the level spread $`\mathcal D(\Omega)`$; the response is the same for all levels to the accuracy $`\delta`$ iff $`\mathcal D(\Omega)\le\delta`$; (12.16) at $`\delta/2`$ is sufficient (necessary and sufficient if both branches are compared), (12.16) at $`\delta`$ is sufficient outside $`[2M_0,2M_{N-1}]`$ and necessary inside. (12.21): for $`0<\Omega<2m`$, one class and branch, iff $`\Omega\le\Omega_\delta\approx\frac{2\delta}{\lvert\chi\rvert}\frac{M_0M_{N-1}}{M_{N-1}-M_0}`$. Exceptional members: $`\chi=0`$ (spread zero), nearly equal level data, $`\Omega`$ at or near a $`2M_k`$.
- **(12.22)** — limit (I), every continuous $`\gamma`$: $`a^{(1)}_{k,\sigma}(\lambda)=-\tau^2\gamma(\lambda)+\sigma\chi R_k[\gamma](\lambda)`$. For $`\gamma\not\equiv0`$ the complete acceleration is the same for all levels iff $`\chi_k=0`$ on every level; to the accuracy $`\delta`$ only the sufficient condition $`2\max_k\lvert\chi_k\rvert\frac{2M_k+\Omega}{\lvert2M_k-\Omega\rvert}\le\delta`$ is derived; its window average is $`-\tau^2\gamma_0`$ for all levels if $`\Omega\neq2M_k`$.
- **(12.17)** — the two-place field: $`\gamma(\lambda)=y\sin^2\gamma_f\lambda`$, with the evaluations of Step 11 and the two controls; sharp and not stationary, with a generator that is not a contract, for $`y\neq0`$; for $`y=0`$ the body sees no field and $`C_{\rm eff}=C_{br}`$ is a contract.

## Consistency checks

1. **Constant $`\gamma`$.** (12.6), (12.7) give the growing part $`\gamma\lambda\langle\alpha_0\rangle_g`$ with $`\alpha_0=-M_k^2\tau^2\cos2p/\omega_k^2`$, which is (4.7) with $`G_k=\gamma M_k`$ (Step 5); at rest (12.9) gives $`-\tau^2\gamma[1+\sigma\chi\sin2M_k\lambda]`$ with the window average $`-\tau^2\gamma`$, which is (4.16). Passed.
2. **A gradient pulse, by an independent route.** $`\gamma(s)=\epsilon\,\delta(s-s_0)`$ acts as $`e^{-i\epsilon M\hat x\sigma_3}`$, a shift of the label by $`\mp\epsilon M`$ on the upper and lower component. For the branch $`+`$ at rest and a narrow $`g`$: the shift inside the branch changes the velocity by $`-\epsilon M\omega''(0)=-\epsilon\tau^2`$; the amplitude on $`\beta_-`$ is $`\tfrac{\epsilon\tau}2(2pg'+g)`$ to leading order, its overlap with $`g`$ is $`\int\frac{\mathrm dp}{2\pi}g^{*}(2pg'+g)=-i\chi_g`$, and with the off-diagonal element $`-\tau`$ of $`\hat V`$ and the phase $`e^{2iM\Delta}`$ it adds $`-\epsilon\tau^2\chi_g\sin2M\Delta`$. The sum is $`\epsilon K_{\chi_g}(\Delta)`$ of (12.8). Passed.
3. **Dimensions.** $`x`$, $`p`$, $`\gamma`$, $`\chi`$, $`\delta`$ are pure numbers; $`\tau`$, $`M`$, $`\omega`$, $`\Omega`$, $`\gamma_f`$ are costs, of dimension $`1/\lambda`$. A velocity is a cost: $`\tau^2\int\mathrm ds\,\gamma`$ in (12.9); an acceleration is a cost squared: $`\tau^2\gamma`$, $`\mathcal A_{k,\sigma}`$; the kernel (12.7) is a cost squared in every term ($`M^2\lambda\omega'^2/\omega`$ included); (12.5) is a pure number ($`\Gamma`$ and $`\lVert(Y-\gamma)C_f\varphi\rVert^2`$ are costs squared). Passed.

## Open issues

- The level-dependent part of the response at fixed $`\lambda`$ is carried entirely by the position–label correlation $`\chi`$ of the start; $`\chi_g`$ grows under free motion by $`2\sigma\lambda\langle\omega'\sin p\rangle_g`$, which is why the orders (I) and (II) differ. Between the two orders only (12.19) is derived, for a real start at resonance; a formula uniform in $`\lambda`$ for starts with $`j_g\neq0`$, or through $`\delta p`$ and $`\chi_g`$ alone, is not derived; the exact (12.6), (12.7) cover it implicitly.
- The ranges of (12.18) are sufficient and uniform in $`\gamma`$. For a $`\gamma`$ without a frequency near $`2M_k`$ the acceleration may be described on a longer range than $`\lambda_a`$; this is not derived.
- For the complete acceleration only the exact-equality criterion and a sufficient condition for the accuracy $`\delta`$ are derived, (12.22); a necessary and sufficient condition for the accuracy $`\delta`$ is not.
- Order (II) for a field frequency inside the band, $`2M_k<\Omega\le2\sqrt{M_k^2+\tau^2}`$: $`c_g(\Omega)`$ of (12.15) is defined for every start, but its limit $`\delta p\to0`$ depends on the weight of the starts near the labels with $`2\omega_k(p)=\Omega`$, which $`\delta p\to0`$ does not control; it is evaluated only for sequences that vanish near these labels.
- Sequences at rest with $`\rho_g\not\to0`$ belong to no class $`\mathcal S_\chi`$; for them only (12.6), (12.7) and the bounds (12.8), (12.10), (12.18) are available.
- The growth at $`\Omega=2M_k`$ is a statement on the first-order coefficient at each fixed $`\lambda`$; the range of $`\lambda`$ in which it is the leading effect needs the second order in $`Y`$, which is outside the scope (as is the mixing behind (12.5)).

## Methods used

- Dyson expansion (first-order perturbation theory) in a pair term; interaction picture
- Partial trace and views; purity of the view
- Plane-wave representation with $`\hat x=i\partial_p`$; two-branch decomposition of the level block
- Integration by parts on periodic functions; elementary bounds with explicit constants
- Duhamel formula and the driven oscillator equation (resonance); uniqueness for linear ordinary differential equations
- Stationary phase for the long-$`\lambda`$ behaviour; order of limits
- Triangle inequality and monotonicity for the spread of a response between levels
