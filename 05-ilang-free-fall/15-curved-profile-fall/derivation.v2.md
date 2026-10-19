# Fall from rest in curved level profiles: curvature terms and local slope

- **Subproject:** 05-ilang-free-fall
- **Package:** 15-curved-profile-fall
- **Version:** v2
- **Mode:** internal regeneration
- **Date:** 2026-10-18

## Changes from previous version

- Step 3: the block $`S_{-+}`$ of the generator is given explicitly, (15.15), and $`\lVert S_{-+}g\rVert`$, $`v_{\rm osc}`$ and $`\sup_\lambda\lvert A_{\rm osc}\rvert`$ are bounded in $`\tau`$, $`M`$, the slopes, the curvatures, $`W`$ and the fourth-moment width $`W_4`$, (15.16) (review I1).
- Step 6: the absence of a $`W^2`$ term is stated for the non-oscillating part only; the curvature part of the oscillating terms is shown to depend on $`\eta g`$ and $`\eta^2g`$, with the bound (15.16) at $`G=\mathcal F=0`$ (review I2).
- Step 7: the window term of (15.11) is replaced by its explicit bound, the window condition on $`M\Lambda`$ is stated, and the joint limit of (15.12) uses $`(1+W_n+W_{4,n}^2)/\Lambda_n\to0`$ instead of $`v_{\rm osc}(g_n)/\Lambda_n\to0`$ (review I1).
- Result: new entry (15.15)–(15.16); entries (15.10), (15.11), (15.12) updated accordingly (review I1, I2).
- Open issues: the item on the unbounded $`v_{\rm osc}`$ is removed (review I1). Methods used: Sylvester equation added.

## Setup and assumptions

**Description (assumption of the package, M8).** A body $`b`$, the only instance of its type, with places $`(x,s,a)`$, recorded by a medium $`c`$ through $`K_x=\kappa xX`$. The clock level $`k`$ is conserved, and on it the body's contract is the level block of the question with $`\zeta_{x,k}=1`$ and the quadratic level profiles $`M_{x,k}=M_k+G_ky+\tfrac12H_ky^2>0`$, $`V_{x,k}=-\mathcal F_ky-\tfrac12\mathcal H_ky^2`$, $`y=x-x_0`$. In Steps 1–7 the level is fixed and its index is dropped: $`\tau,M,G,\mathcal F,H,\mathcal H`$ ($`\mathcal H`$ is the curvature of $`V`$, not a Hilbert space). $`\varepsilon`$ is the joint size of $`G,\mathcal F,H,\mathcal H`$.

**Regime and order (A13).** Weak records: $`\kappa\to0`$ at fixed $`\lambda`$, chain and start, with $`\kappa x\langle X\rangle`$ counted in $`V_{x,k}`$, so the body evolves with $`C^{(k)}`$. First order jointly in $`G,\mathcal F,H,\mathcal H`$ at fixed $`\lambda`$, start and chain, then a long chain: at fixed $`\lambda`$ the hopping is nearest-neighbour, so a start far inside a long chain does not feel its ends, and the computation is done on $`x\in\mathbb Z`$. $`O(\varepsilon^2)`$ is a second-order remainder at fixed $`\lambda`$ and start.

**Plane waves, branches, start.** $`\lvert p\rangle:=\sum_xe^{ipx}\lvert x\rangle`$. The block with all slopes and curvatures zero is $`C_0=\int\frac{\mathrm dp}{2\pi}\lvert p\rangle\langle p\rvert\otimes h(p)`$ with

```math
h(p)=M\sigma_3-\tau\sin p\,\sigma_1,\qquad h\beta_\pm=\pm\omega\beta_\pm,\qquad \omega(p)=\sqrt{M^2+\tau^2\sin^2p}\ \ge M>0 .
\qquad\text{(15.1)}
```

$`h`$ is real symmetric, so $`\beta_+=(\cos\frac\theta2,\sin\frac\theta2)`$, $`\beta_-=(-\sin\frac\theta2,\cos\frac\theta2)`$ with $`\tan\theta=-\tau\sin p/M`$, $`\lvert\theta\rvert<\pi/2`$, are real, smooth and $`2\pi`$-periodic. The start is $`\psi_0=B_{k,+}[g]=\int\frac{\mathrm dp}{2\pi}g(p)\lvert p\rangle\otimes\beta_+(p)\otimes\lvert f_k\rangle`$, $`g`$ smooth, $`2\pi`$-periodic, $`\int\frac{\mathrm dp}{2\pi}\lvert g\rvert^2=1`$; another phase convention for $`\beta_+`$ multiplies $`g`$ by a $`p`$-dependent phase, and all formulas refer to the real convention. $`\langle F\rangle_g:=\int\frac{\mathrm dp}{2\pi}\lvert g\rvert^2F`$. At rest: $`\langle p\rangle_g=0`$ on $`(-\pi,\pi]`$; $`\delta p^2:=\langle p^2\rangle_g`$, $`\kappa_4:=\langle p^4\rangle_g/\delta p^4`$. The start is not adapted to the profiles (M9).

**Inputs** (04-branch-fall@v3, quoted in the question; here $`g_{\zeta,k}=0`$, $`\sigma=+`$). (4.7): the coefficient of $`\lambda`$ in the first-order velocity of $`B_{k,+}[g]`$ is $`\langle a_{k,+}\rangle_g`$, $`a_{k,+}(p)=-\frac{G_kM_k\tau_k^2\cos2p}{\omega_k^2}+\mathcal F_k\frac{\tau_k^2(M_k^2\cos2p-\tau_k^2\sin^4p)}{\omega_k^3}`$. (4.11): $`\lvert\langle a_{k,\sigma}\rangle_g-a_{k,\sigma}(p_0)\rvert\le\frac12\sup_p\lvert a_{k,\sigma}''\rvert\,\delta p^2`$ for a start concentrated at $`p_0`$, and drift acceleration $`=\lim_{\delta p\to0}\lim_{\Lambda\to\infty}\overline{a^{(1)}}=a_{k,\sigma}(p_0)`$. (4.16): $`a_{k,\sigma}(0)=\frac{\tau_k^2}{M_k}(\sigma\mathcal F_k-G_k)`$. (4.19): for linear profiles, $`a_{k,+}(0)=a_+\ \forall k\iff\frac{\tau_k^2}{M_k}(\mathcal F_k-G_k)=a_+\ \forall k`$.

## Derivation

### Step 1. Branch representation

Write a state as $`\int\frac{\mathrm dp}{2\pi}\lvert p\rangle\otimes\bigl(u_+(p)\beta_+(p)+u_-(p)\beta_-(p)\bigr)`$, with Pauli matrices $`\rho_{1,2,3}`$ on $`(u_+,u_-)`$. Since $`x\,e^{ipx}=-i\partial_pe^{ipx}`$, integration by parts on the circle gives $`\hat x=i\partial_p`$ on the amplitude $`u_+\beta_++u_-\beta_-`$; with $`\partial_p\beta_+=\alpha\beta_-`$, $`\partial_p\beta_-=-\alpha\beta_+`$, $`\alpha:=\theta'/2`$, and the expansion of $`\sigma_3`$ in $`\beta_\pm`$:

```math
\hat x=\xi+\alpha\rho_2,\quad \xi:=i\partial_p,\quad \sigma_3=\mu\rho_3+\nu\rho_1,\quad C_0=\omega\rho_3,\qquad
\alpha=-\frac{\tau M\cos p}{2\omega^2},\ \ \mu=\frac M\omega,\ \ \nu=\frac{\tau\sin p}{\omega}.
\qquad\text{(15.2)}
```

Let $`\eta:=\xi-x_0`$, so $`\hat y:=\hat x-x_0=\eta+\alpha\rho_2`$. For a function $`f(p)`$: $`[\eta,f]=if'`$ and $`e^{i\omega\lambda}\eta e^{-i\omega\lambda}=\eta+\omega'\lambda`$. The start has $`u_+=g`$, $`u_-=0`$; centred means $`\langle g\vert\eta\vert g\rangle=0`$, and $`W^2=\langle\psi_0\vert\hat y^2\vert\psi_0\rangle=\lVert\eta g\rVert^2+\langle\alpha^2\rangle_g\ge\lVert\eta g\rVert^2`$. The position–momentum density of the start is

```math
j(p):=\mathrm{Re}\bigl[g^*(\eta g)\bigr]=-\mathrm{Im}(g^*\partial_pg)-x_0\lvert g\rvert^2,\qquad \int\tfrac{\mathrm dp}{2\pi}\,j=0 .
\qquad\text{(15.3)}
```

At zero order $`u_-`$ stays $`0`$ and $`u_+(\lambda)=u_0(\lambda):=e^{-i\omega\lambda}g`$, so $`\bar x_{\rm lab}=x_0+\lambda\langle\omega'\rangle_g`$ and the zero-order acceleration vanishes.

### Step 2. The profile term in the branch representation

$`C_1:=C^{(k)}-C_0=\delta M(\hat y)\sigma_3+V(\hat y)`$ with $`\delta M(y)=Gy+\frac12Hy^2`$, $`V(y)=-\mathcal Fy-\frac12\mathcal Hy^2`$ (diagonal in $`x`$, hence functions of $`\hat x`$). As $`\hat y`$ and $`\sigma_3`$ commute, $`\hat y\sigma_3=\frac12\{\hat y,\sigma_3\}`$ and $`\hat y^2\sigma_3=\hat y\sigma_3\hat y`$. Multiplying the blocks $`\hat y_{\pm\pm}=\eta`$, $`\hat y_{+-}=-i\alpha`$, $`\hat y_{-+}=i\alpha`$, $`(\sigma_3)_{\pm\pm}=\pm\mu`$, $`(\sigma_3)_{\pm\mp}=\nu`$, and using $`[\eta,f]=if'`$:

```math
\begin{aligned}
(C_1)_{++}&=\tfrac G2\{\eta,\mu\}+\tfrac H2\,\eta\mu\eta-\mathcal F\eta-\tfrac{\mathcal H}2\eta^2+Q,\qquad Q:=-\tfrac H2\bigl[(\nu\alpha)'+\mu\alpha^2\bigr]-\tfrac{\mathcal H}2\alpha^2,\\
(C_1)_{-+}&=\tfrac G2\{\eta,\nu\}+\tfrac H2\bigl[\eta\nu\eta-\nu\alpha^2+(\alpha\mu)'\bigr]-i\mathcal F\alpha-\tfrac{i\mathcal H}2\{\alpha,\eta\},\qquad (C_1)_{+-}=(C_1)_{-+}^\dagger .
\end{aligned}
\qquad\text{(15.4)}
```

### Step 3. Block diagonalization at first order and the oscillating terms

Define the anti-self-adjoint, branch-off-diagonal $`S`$ by

```math
S_{+-}:=\int_0^\infty\!\mathrm ds\;e^{-s\omega}(C_1)_{+-}e^{-s\omega},\qquad S_{-+}:=-S_{+-}^\dagger .
\qquad\text{(15.5)}
```

The integral converges since $`\omega\ge M>0`$, and integrating $`\partial_s(e^{-s\omega}Xe^{-s\omega})`$ gives $`\omega S_{+-}+S_{+-}\omega=(C_1)_{+-}`$. Hence $`[S,C_0]`$ cancels the off-diagonal part of $`C_1`$, and $`C':=e^SC^{(k)}e^{-S}=C_0+C_1^{\rm d}+O(\varepsilon^2)`$, $`C_1^{\rm d}`$ the diagonal blocks. Taking adjoints, $`\omega S_{-+}+S_{-+}\omega=-(C_1)_{-+}`$, whose solution is unique since $`\omega\ge M>0`$. For a function $`u(p)`$, $`[\eta,u]=iu'`$ gives $`\omega\{u,\eta\}+\{u,\eta\}\omega=2\{\omega u,\eta\}`$ and $`\omega\,\eta u\eta+\eta u\eta\,\omega=2\eta\,\omega u\,\eta-(u\omega')'`$, so solving degree by degree in $`\eta`$ with (15.4):

```math
S_{-+}=-\frac H4\,\eta\,\frac\nu\omega\,\eta-\frac12\Bigl\{\frac{G\nu-i\mathcal H\alpha}{2\omega},\eta\Bigr\}-\frac1{2\omega}\Bigl[\frac H2\bigl((\alpha\mu)'-\nu\alpha^2\bigr)+\frac H4\Bigl(\frac{\nu\omega'}{\omega}\Bigr)'-i\mathcal F\alpha\Bigr].
\qquad\text{(15.15)}
```

Write $`\bar x_{\rm lab}=\langle\Psi'(\lambda)\vert\hat x'\vert\Psi'(\lambda)\rangle`$ with $`\Psi'(\lambda)=e^{-iC'\lambda}e^S\psi_0`$, $`\hat x'=e^S\hat xe^{-S}`$. At first order $`\Psi'_+=e^{-iE\lambda}g`$ with $`E:=\omega+(C_1)_{++}`$, $`\Psi'_-=e^{i\omega\lambda}S_{-+}g`$, $`\hat x'_{++}=\xi+i(S_{+-}\alpha+\alpha S_{-+})`$, $`\hat x'_{+-}=-i\alpha`$. Hence

```math
\bar x_{\rm lab}(\lambda)=\langle e^{-iE\lambda}g\vert\xi\vert e^{-iE\lambda}g\rangle+P(\lambda)+X_{\rm osc}(\lambda)+O(\varepsilon^2),\qquad
X_{\rm osc}:=2\mathrm{Re}\!\int\!\tfrac{\mathrm dp}{2\pi}\,e^{2i\omega(p)\lambda}f(p),\quad f:=-i\alpha\,g^*\,(S_{-+}g),
\qquad\text{(15.6)}
```

with $`P(\lambda):=\langle u_0(\lambda)\vert i(S_{+-}\alpha+\alpha S_{-+})\vert u_0(\lambda)\rangle`$. By (15.15) the degree-2 part of $`S_{+-}=-S_{-+}^\dagger`$ is $`\frac H4\eta\frac\nu\omega\eta`$, which enters $`S_{+-}\alpha-\alpha S_{+-}^\dagger`$ as $`\frac H4[\eta\frac\nu\omega\eta,\alpha]=\frac{iH}4\{\eta,\frac{\nu\alpha'}{\omega}\}`$, of degree 1. An operator of degree $`\le1`$ in $`\eta`$ has, under $`e^{i\omega\lambda}\eta e^{-i\omega\lambda}=\eta+\omega'\lambda`$, an expectation of degree $`\le1`$ in $`\lambda`$: $`P''=0`$. Every term of $`X_{\rm osc}`$ carries $`e^{2i\omega(p)\lambda}`$ under the $`p`$-integral; these are the **oscillating terms**, with acceleration $`A_{\rm osc}:=X_{\rm osc}''=-8\mathrm{Re}\int\frac{\mathrm dp}{2\pi}\omega^2e^{2i\omega\lambda}f`$, bounded uniformly in $`\lambda`$ by $`8\int\frac{\mathrm dp}{2\pi}\omega^2\lvert f\rvert`$, and $`\lvert X_{\rm osc}'\rvert\le v_{\rm osc}:=4\int\frac{\mathrm dp}{2\pi}\omega\lvert f\rvert`$.

These are bounded explicitly. Use $`\frac12\{u,\eta\}g=u\,\eta g+\frac i2u'g`$, $`\eta u\eta g=u\,\eta^2g+iu'\,\eta g`$ and, from $`\omega\ge M`$, $`\omega\ge\tau\lvert\sin p\rvert`$ and $`(\nu/\omega)'=\tau\cos p\,(M^2-\tau^2\sin^2p)/\omega^4`$, $`\alpha/\omega=-\tau M\cos p/(2\omega^3)`$, $`\alpha\mu=-\tau M^2\cos p/(2\omega^3)`$, $`\nu\omega'/\omega=\tau^3\sin^2p\cos p/\omega^3`$, the elementary bounds $`\lvert\nu/\omega\rvert,\lvert(\nu/\omega)'\rvert\le\tau/M^2`$, $`\lvert\alpha/\omega\rvert\le\frac\tau{2M^2}`$, $`\lvert(\alpha/\omega)'\rvert\le\frac\tau{2M^2}(1+3r)`$, $`\lvert(\alpha\mu)'\rvert\le\frac r2(1+3r)`$, $`\lvert\nu\alpha^2\rvert\le\frac{r^2}4`$, $`\lvert(\nu\omega'/\omega)'\rvert\le5r^2`$, with $`r:=\tau/M`$. Applied term by term to (15.15), and followed by Cauchy–Schwarz in $`v_{\rm osc}=4\int\frac{\mathrm dp}{2\pi}\omega\lvert\alpha\rvert\lvert g\rvert\lvert S_{-+}g\rvert`$ with $`\omega\lvert\alpha\rvert\le\tau/2`$, in the bound of $`A_{\rm osc}`$ with $`\omega^2\lvert\alpha\rvert\le\tau M/2`$, and $`\lVert\eta g\rVert\le W`$ (Step 1), they give

```math
\begin{aligned}
&\lVert S_{-+}g\rVert\le\frac\tau{M^2}\bigl(\sigma_0+\sigma_1\lVert\eta g\rVert+\sigma_2W_4^2\bigr),\qquad v_{\rm osc}\le\frac{2\tau^2}{M^2}\bigl(\sigma_0+\sigma_1W+\sigma_2W_4^2\bigr),\qquad \sup_\lambda\lvert A_{\rm osc}\rvert\le\frac{4\tau^2}{M}\bigl(\sigma_0+\sigma_1W+\sigma_2W_4^2\bigr),\\
&\sigma_0:=\tfrac14(\lvert\mathcal F\rvert+\lvert G\rvert)+\tfrac18(1+3r)\lvert\mathcal H\rvert+\tfrac1{16}(2+17r)\lvert H\rvert,\quad \sigma_1:=\tfrac12\lvert G\rvert+\tfrac14(\lvert H\rvert+\lvert\mathcal H\rvert),\quad \sigma_2:=\tfrac14\lvert H\rvert,\quad W_4^2:=\lVert\eta^2g\rVert .
\end{aligned}
\qquad\text{(15.16)}
```

$`W_4`$ is the fourth-moment width of the position of the start about $`x_0`$ ($`W_4^4=\langle g\vert\eta^4\vert g\rangle`$), finite for smooth $`g`$, with $`W_4\ge\lVert\eta g\rVert`$ by Cauchy–Schwarz.

### Step 4. Acceleration operator of the upper branch

Under $`E`$, $`\frac{\mathrm d^2}{\mathrm d\lambda^2}\langle\xi\rangle=\langle i[E,i[E,\xi]]\rangle`$. With $`i[f,\eta]=f'`$, (15.4) gives $`i[E,\xi]=\omega'+\frac G2\{\eta,\mu'\}+\frac H2\eta\mu'\eta+Q'`$. Since $`i[\omega,\omega']=0`$, the first-order part is $`i[\omega,\frac G2\{\eta,\mu'\}+\frac H2\eta\mu'\eta]+i[(C_1)_{++},\omega']=G\omega'\mu'+\frac H2\{\omega'\mu',\eta\}-G\mu\omega''-\frac H2\{\mu\omega'',\eta\}+\mathcal F\omega''+\frac{\mathcal H}2\{\omega'',\eta\}`$ ($`Q`$ shifts the velocity by $`Q'`$ and drops out). Thus

```math
\hat A=a(p)+\tfrac12\{b(p),\eta\},\qquad a=\mathcal F\omega''+G(\omega'\mu'-\mu\omega''),\quad b=\mathcal H\omega''+H(\omega'\mu'-\mu\omega'').
\qquad\text{(15.7)}
```

With $`\omega''=\tau^2(M^2\cos2p-\tau^2\sin^4p)/\omega^3`$ and $`\omega'\mu'-\mu\omega''=-M\tau^2\cos2p/\omega^2`$:

```math
a(p)=-\frac{GM\tau^2\cos2p}{\omega^2}+\mathcal F\,\frac{\tau^2(M^2\cos2p-\tau^2\sin^4p)}{\omega^3},\qquad b(p)=-\frac{HM\tau^2\cos2p}{\omega^2}+\mathcal H\,\frac{\tau^2(M^2\cos2p-\tau^2\sin^4p)}{\omega^3}.
\qquad\text{(15.8)}
```

$`a=a_{k,+}`$ of (4.7) at $`g_{\zeta,k}=0`$, and $`b`$ is the same function of the curvatures; $`\hat A`$ is the acceleration of the linear profiles with the local slopes $`G+H\eta`$, $`\mathcal F+\mathcal H\eta`$, symmetrized.

### Step 5. First-order acceleration

$`\hat A`$ is of first order, so it is evaluated in $`u_0(\lambda)`$: $`e^{i\omega\lambda}\eta e^{-i\omega\lambda}=\eta+\omega'\lambda`$ and $`\frac12\langle g\vert\{b,\eta\}\vert g\rangle=\mathrm{Re}\langle bg\vert\eta g\rangle=\int\frac{\mathrm dp}{2\pi}bj`$. With (15.6) and $`P''=0`$:

```math
\frac{\mathrm d^2\bar x_{\rm lab}}{\mathrm d\lambda^2}=\underbrace{\langle a\rangle_g+c_g+\lambda\,\langle b\,\omega'\rangle_g}_{\bar A(\lambda)}+A_{\rm osc}(\lambda)+O(\varepsilon^2),\qquad c_g:=\int\tfrac{\mathrm dp}{2\pi}\,b\,j .
\qquad\text{(15.9)}
```

### Step 6. The curvature part

The curvatures contribute $`c_g+\lambda\langle b\omega'\rangle_g`$ to $`\bar A`$; $`c_g=\mathrm{Re}\langle bg\vert\eta g\rangle`$ is linear in $`\eta g`$ and $`\langle b\omega'\rangle_g`$ does not contain $`\eta`$, so this non-oscillating part has no term in $`W^2`$. They contribute to $`A_{\rm osc}`$ through the $`H,\mathcal H`$ terms of $`S_{-+}`$ in (15.15), which include $`-\frac H4\eta\frac\nu\omega\eta`$: this part depends on the start through $`\eta g`$ and $`\eta^2g`$, and, $`S_{-+}`$ being linear in $`(G,\mathcal F,H,\mathcal H)`$, (15.16) at $`G=\mathcal F=0`$ bounds it uniformly in $`\lambda`$ by $`\frac{4\tau^2}M(\sigma_0+\sigma_1W+\sigma_2W_4^2)\big\vert_{G=\mathcal F=0}`$. $`b`$ is even in $`p`$ and $`\omega'`$ odd, and $`b(0)=\frac{\tau^2}{M}(\mathcal H-H)`$ by (4.16) applied to $`b`$. Since $`\int j=0`$, $`c_g=\mathrm{Re}\langle(b-b(0))g\vert\eta g\rangle`$, $`\lvert b-b(0)\rvert\le\frac12b_2p^2`$ and Cauchy–Schwarz give the first bound; at rest, $`\langle b\omega'\rangle_g=\langle b\omega'-(b\omega')'(0)p\rangle_g`$, Taylor's remainder for the odd $`b\omega'`$ and $`\langle\lvert p\rvert^3\rangle_g\le\langle p^2\rangle_g^{1/2}\langle p^4\rangle_g^{1/2}`$ give the second:

```math
\lvert c_g\rvert\le\tfrac12\,b_2\,\kappa_4^{1/2}\,\delta p^2\,W,\qquad
\lvert\langle b\omega'\rangle_g\rvert\le\tfrac16\,b_3\,\kappa_4^{1/2}\,\delta p^3,\qquad b_2:=\sup_p\lvert b''\rvert,\ b_3:=\sup_p\lvert(b\omega')'''\rvert .
\qquad\text{(15.10)}
```

$`b_2,b_3`$ are linear in $`(H,\mathcal H)`$ with coefficients depending only on $`\tau,M`$. Exactly, $`c_g=0`$ if $`j\equiv0`$ (e.g. $`g=re^{-ipx_0}`$, $`r`$ real), and $`\langle b\omega'\rangle_g=0`$ if $`\lvert g\rvert^2`$ is even.

### Step 7. Local slope

Average (15.9) over a window $`[\lambda_1,\lambda_1+\Lambda]`$ with centre $`\lambda_c`$. The non-oscillating part, linear in $`\lambda`$, averages to $`\bar A(\lambda_c)`$; the oscillating part to $`[X_{\rm osc}']/\Lambda`$, at most $`2v_{\rm osc}/\Lambda\le\frac{4\tau^2}{M^2\Lambda}(\sigma_0+\sigma_1W+\sigma_2W_4^2)`$ by (15.16). With (4.11) at $`p_0=0`$ (the mean of a start at rest), $`a(0)=\frac{\tau^2}M(\mathcal F-G)`$ by (4.16), and (15.10), the window average $`\bar A_\Lambda`$ of the first-order acceleration obeys

```math
\bigl\lvert\bar A_\Lambda-a(0)\bigr\rvert\le\tfrac12a_2\,\delta p^2+\tfrac12b_2\,\kappa_4^{1/2}\delta p^2\,W+\tfrac16b_3\,\kappa_4^{1/2}\delta p^3\lvert\lambda_c\rvert+\frac{4\tau^2}{M^2\Lambda}\bigl(\sigma_0+\sigma_1W+\sigma_2W_4^2\bigr),\qquad a_2:=\sup_p\lvert a''\rvert .
\qquad\text{(15.11)}
```

A relative error $`\epsilon`$ ($`a(0)\neq0`$) holds if each term is at most $`\epsilon\lvert a(0)\rvert/4`$. For the last term, by $`\lvert a(0)\rvert=\frac{\tau^2}M\lvert\mathcal F-G\rvert`$, this is the window condition $`M\Lambda\ge16(\sigma_0+\sigma_1W+\sigma_2W_4^2)/(\epsilon\lvert\mathcal F-G\rvert)`$, at every $`\tau/M`$. At leading order in $`\tau/M`$ (with $`\mathcal F\ne G`$, $`\mathcal H\ne H`$), $`a\simeq a(0)\cos2p`$, $`b\simeq\frac{\tau^2}M(\mathcal H-H)\cos2p`$, $`b\omega'\simeq\frac{\tau^4}{4M^2}(\mathcal H-H)\sin4p`$, and the first three relative terms become $`2\delta p^2`$, $`2\kappa_4^{1/2}\delta p^2W\frac{\lvert\mathcal H-H\rvert}{\lvert\mathcal F-G\rvert}`$, $`\frac83\kappa_4^{1/2}\frac{\tau^2}M\delta p^3\lvert\lambda_c\rvert\frac{\lvert\mathcal H-H\rvert}{\lvert\mathcal F-G\rvert}`$.

Limits. For windows $`[\lambda_1,\lambda_1+\Lambda]`$ at fixed start, $`\bar A_\Lambda=\langle a\rangle_g+c_g+(\lambda_1+\frac\Lambda2)\langle b\omega'\rangle_g+O(\Lambda^{-1})`$, so $`\lim_{\Lambda\to\infty}\bar A_\Lambda`$ exists iff $`\langle b\omega'\rangle_g=0`$. Hence:

```math
\lvert g\rvert^2\ \text{even}:\quad \lim_{\delta p\to0}\ \lim_{\Lambda\to\infty}\bar A_\Lambda=\frac{\tau^2}{M}(\mathcal F-G)\quad\text{along families with }\kappa_4\ \text{bounded and}\ \delta p^2W\to0 ,
\qquad\text{(15.12)}
```

taken after first order and the long chain, in the order of (4.11); if also $`j\equiv0`$, $`c_g=0`$ and the curvatures drop out of $`\bar A`$ at every $`\delta p`$. If $`\langle b\omega'\rangle_g\ne0`$ the inner limit does not exist; a joint limit ($`\lambda_1`$ fixed) with $`\delta p_n\to0`$, $`\kappa_4`$ bounded, $`\delta p_n^2W_n\to0`$, $`\Lambda_n\delta p_n^3\to0`$ and $`(1+W_n+W_{4,n}^2)/\Lambda_n\to0`$ gives the same value: every term of (15.11) tends to $`0`$, the last by (15.16), the third since $`\lvert\lambda_c\rvert\le\lvert\lambda_1\rvert+\Lambda_n`$. Such $`\Lambda_n`$ exist iff $`(1+W_n+W_{4,n}^2)\,\delta p_n^3\to0`$: this is the product of the two conditions on $`\Lambda_n`$, and conversely $`\Lambda_n=[(1+W_n+W_{4,n}^2)/\delta p_n^3]^{1/2}`$ satisfies both. It holds, together with $`\delta p_n^2W_n\to0`$, whenever $`W_n\delta p_n`$ and $`W_{4,n}\delta p_n`$ stay bounded.

### Step 8. Level independence

To avoid a clash with the start function $`g`$, write $`n_x=1+g_ny+\frac12h_ny^2`$ (the question's $`g,h`$), and compare starts $`B_{k,+}[g]`$, $`B_{l,+}[g]`$ with the same $`g`$ ($`j`$ does not depend on the level). Let $`\bar A_k`$ be $`\bar A`$ of (15.9) on level $`k`$.

(a) Factor class: $`M_k=m+d_k`$, $`G_k=g_nM_k`$, $`H_k=h_nM_k`$, $`\mathcal F_k=\mathcal H_k=0`$, $`\tau_k=\tau`$. With $`r_k:=\tau^2/M_k^2`$, (15.8) gives $`a_k=-g_n\tau^2\cos2p/(1+r_k\sin^2p)`$, $`b_k=-h_n\tau^2\cos2p/(1+r_k\sin^2p)`$, $`b_k\omega_k'=-\frac{h_n\tau^4}{M_k}\sin p\cos p\cos2p\,(1+r_k\sin^2p)^{-3/2}`$, hence

```math
\bar A_k-\bar A_l=\tau^2(r_k-r_l)\Bigl[g_n\langle\Delta_{kl}\rangle_g+h_n\!\int\!\tfrac{\mathrm dp}{2\pi}\Delta_{kl}\,j\Bigr]+\lambda\bigl(\langle b_k\omega_k'\rangle_g-\langle b_l\omega_l'\rangle_g\bigr),\qquad \Delta_{kl}:=\frac{\sin^2p\,\cos2p}{(1+r_k\sin^2p)(1+r_l\sin^2p)} .
\qquad\text{(15.13)}
```

$`r_k\ne r_l`$ for $`k\ne l`$. For $`g_n\ne0`$, take $`g=re^{-ipx_0}`$ with $`r`$ real, even, smooth, supported in $`\lvert p\rvert<\pi/4`$, $`\delta p>0`$: then $`j\equiv0`$, the $`\lambda`$-term vanishes, $`\Delta_{kl}>0`$ for $`0<\lvert p\rvert<\pi/4`$, so $`\bar A_k-\bar A_l=g_n\tau^2(r_k-r_l)\langle\Delta_{kl}\rangle_g\ne0`$, and $`\langle\Delta_{kl}\rangle_g=\delta p^2+O(\langle p^4\rangle_g)`$ gives the leading difference $`g_n\tau^4(M_k^{-2}-M_l^{-2})\,\delta p^2`$. For $`g_n=0\ne h_n`$, take $`g=re^{-ipx_0-i\gamma(p^3/3-\delta p^2p)}`$, $`\gamma\ne0`$, with $`r`$ as before and supported where $`\Delta_{kl}`$ increases with $`\lvert p\rvert`$ (a neighbourhood of $`0`$): it is at rest and centred, $`j=\gamma(p^2-\delta p^2)\lvert g\rvert^2`$, and $`\int\Delta_{kl}j=\gamma\,\mathrm{Cov}_g(\Delta_{kl},p^2)\ne0`$, since both are increasing functions of $`\lvert p\rvert`$. The reason is that the hopping is not multiplied by $`n_x`$: $`\omega_k/M_k=(1+r_k\sin^2p)^{1/2}`$ depends on the level except at $`p=0`$. In the limit (15.12), $`\bar A_k\to a_k(0)=-g_n\tau^2`$ for every $`k`$, the case $`a_+=-g_n\tau^2`$ of (4.19).

(b) Control: $`M_k=m+d_k`$, $`G_k=mg_n`$, $`H_k=mh_n`$, rest as in (a). By (4.16), $`a_k(0)=-\tau^2mg_n/(m+d_k)`$, so already in the limit (15.12)

```math
a_k(0)-a_l(0)=\frac{\tau^2m\,g_n\,(d_k-d_l)}{(m+d_k)(m+d_l)}\ \ne0\quad(g_n\ne0,\ k\ne l),
\qquad\text{(15.14)}
```

of zeroth order in $`\delta p`$ ($`\simeq\tau^2g_n(d_k-d_l)/m`$ for $`d_k,d_l\ll m`$); $`b_k(0)=-\tau^2mh_n/(m+d_k)`$ makes the curvature terms level-dependent as well.

## Result

All results: one body in the weak-record regime, conserved level, first order jointly in the slopes and curvatures at fixed $`\lambda`$, start and chain, then a long chain.

- **(15.7)–(15.8)** (formula). For every level block with quadratic level profiles ($`\zeta=1`$), the first-order acceleration operator of the upper branch is $`\hat A=a(p)+\frac12\{b(p),\eta\}`$: $`a`$ is $`a_{k,+}`$ of (4.7) at $`g_{\zeta,k}=0`$, and $`b`$ is the same function with $`(G,\mathcal F)\to(H,\mathcal H)`$, i.e. the linear-profile acceleration with the local slopes $`G+H\eta`$, $`\mathcal F+\mathcal H\eta`$.
- **(15.9)** (formula). For every such block and every start $`B_{k,+}[g]`$ centred at $`x_0`$ with finite $`W`$: $`\mathrm d^2\bar x_{\rm lab}/\mathrm d\lambda^2=\langle a\rangle_g+c_g+\lambda\langle b\omega'\rangle_g+A_{\rm osc}(\lambda)+O(\varepsilon^2)`$, with $`c_g=\int\frac{\mathrm dp}{2\pi}bj`$, $`j`$ of (15.3), and $`A_{\rm osc}=-8\mathrm{Re}\int\frac{\mathrm dp}{2\pi}\omega^2e^{2i\omega\lambda}f`$, $`f`$ of (15.6), bounded in $`\lambda`$. The non-oscillating part is exactly linear in $`\lambda`$. No control inside the class (it is an identity at first order).
- **(15.15)–(15.16)** (formula). For every such block and every start $`B_{k,+}[g]`$ centred at $`x_0`$, the branch-off-diagonal block of the first-order block-diagonalizing generator is $`S_{-+}`$ of (15.15), so the oscillating amplitude $`f=-i\alpha g^*(S_{-+}g)`$ is explicit; at every $`\tau/M`$, $`v_{\rm osc}\le\frac{2\tau^2}{M^2}(\sigma_0+\sigma_1W+\sigma_2W_4^2)`$ and $`\lvert A_{\rm osc}(\lambda)\rvert\le\frac{4\tau^2}M(\sigma_0+\sigma_1W+\sigma_2W_4^2)`$ for all $`\lambda`$, with $`\sigma_0,\sigma_1,\sigma_2`$ linear in the slopes and curvatures and $`W_4^2=\lVert\eta^2g\rVert`$ as in (15.16). No control (an identity and upper bounds).
- **(15.10)** (theorem). The curvatures contribute $`c_g+\lambda\langle b\omega'\rangle_g`$ to the non-oscillating part; it contains $`\eta g`$ only linearly, through $`c_g=\mathrm{Re}\langle bg\vert\eta g\rangle`$, and has no term in $`W^2`$. They contribute to $`A_{\rm osc}`$ a part bounded uniformly in $`\lambda`$, which depends on the start through $`\eta g`$ and $`\eta^2g`$ and is at most $`\frac{4\tau^2}M(\sigma_0+\sigma_1W+\sigma_2W_4^2)`$ evaluated at $`G=\mathcal F=0`$, by (15.16). The contribution grows with $`\lambda`$, linearly (power 1), iff $`\langle b\omega'\rangle_g\ne0`$. For starts at rest, $`\lvert c_g\rvert\le\frac12b_2\kappa_4^{1/2}\delta p^2W`$ and $`\lvert\langle b\omega'\rangle_g\rvert\le\frac16b_3\kappa_4^{1/2}\delta p^3`$; $`c_g=0`$ if $`j\equiv0`$, $`\langle b\omega'\rangle_g=0`$ if $`\lvert g\rvert^2`$ is even. Control: a start at rest with uneven $`\lvert g\rvert^2`$ and $`\langle b\omega'\rangle_g\ne0`$ shows the growth.
- **(15.11)** (criterion). For starts at rest centred at $`x_0`$, the average of the first-order acceleration over a window of length $`\Lambda`$ and centre $`\lambda_c`$ differs from $`a(0)=\frac{\tau^2}M(\mathcal F-G)`$ by at most $`\frac12a_2\delta p^2+\frac12b_2\kappa_4^{1/2}\delta p^2W+\frac16b_3\kappa_4^{1/2}\delta p^3\lvert\lambda_c\rvert+\frac{4\tau^2}{M^2\Lambda}(\sigma_0+\sigma_1W+\sigma_2W_4^2)`$; for $`a(0)\ne0`$ the relative error is at most $`\epsilon`$ if each term is $`\le\epsilon\lvert a(0)\rvert/4`$ (sufficient), which for the last term is the window condition $`M\Lambda\ge16(\sigma_0+\sigma_1W+\sigma_2W_4^2)/(\epsilon\lvert\mathcal F-G\rvert)`$, at every $`\tau/M`$. At leading order in $`\tau/M`$, with $`\mathcal F\ne G`$ and $`\mathcal H\ne H`$, the curvature conditions read $`\kappa_4^{1/2}\delta p^2W\lvert\mathcal H-H\rvert\ll\lvert\mathcal F-G\rvert`$ and $`\kappa_4^{1/2}\frac{\tau^2}M\delta p^3\lvert\lambda_c\rvert\lvert\mathcal H-H\rvert\ll\lvert\mathcal F-G\rvert`$.
- **(15.12)** (theorem). For starts at rest centred at $`x_0`$ with even $`\lvert g\rvert^2`$: $`\lim_{\delta p\to0}\lim_{\Lambda\to\infty}\bar A_\Lambda=\frac{\tau^2}M(\mathcal F-G)`$ exactly at first order, along families with $`\kappa_4`$ bounded and $`\delta p^2W\to0`$, the limits taken after first order and the long chain, window before $`\delta p`$. For windows $`[\lambda_1,\lambda_1+\Lambda]`$ with fixed $`\lambda_1`$ and a fixed start, $`\lim_{\Lambda\to\infty}\bar A_\Lambda`$ exists iff $`\langle b\omega'\rangle_g=0`$; otherwise a joint limit that adds $`\Lambda_n\delta p_n^3\to0`$ and $`(1+W_n+W_{4,n}^2)/\Lambda_n\to0`$ to the conditions above gives the same value; such $`\Lambda_n`$ exist iff $`(1+W_n+W_{4,n}^2)\delta p_n^3\to0`$, which holds when $`W_n\delta p_n`$ and $`W_{4,n}\delta p_n`$ stay bounded.
- **(15.13)** (negative). Factor class, $`N\ge2`$: for $`g_n\ne0`$ or $`h_n\ne0`$ there are starts of the class for which the non-oscillating first-order acceleration differs between two levels; the difference is (15.13), with leading term $`g_n\tau^4(M_k^{-2}-M_l^{-2})\delta p^2`$ for a start with $`j\equiv0`$ and even $`\lvert g\rvert^2`$. Reason: $`\tau_k=\tau`$ is not multiplied by $`n_x`$. In the limit (15.12) it is level-independent, $`-g_n\tau^2`$.
- **(15.14)** (negative). Control $`M_{x,k}=mn_x+d_k`$: not the same for all levels for $`g_n\ne0`$, already in the limit (15.12), with difference $`\tau^2mg_n(d_k-d_l)/((m+d_k)(m+d_l))`$, of zeroth order in $`\delta p`$.

## Consistency checks

1. Dimensions: $`\lambda\sim[C]^{-1}`$, $`x`$ dimensionless, $`\tau,M,G,\mathcal F,H,\mathcal H\sim[C]`$; $`a`$, $`c_g`$ and $`\lambda\langle b\omega'\rangle_g`$ are all $`[C]^2`$, as is $`\mathrm d^2\bar x_{\rm lab}/\mathrm d\lambda^2`$. Passed.
2. Zero curvatures: $`b=0`$, so (15.9) gives a constant non-oscillating acceleration $`\langle a_{k,+}\rangle_g`$, i.e. the coefficient of $`\lambda`$ in the velocity of (4.7), and (15.12) reduces to (4.11) with $`a(0)`$ of (4.16). Passed.
3. $`\tau\to0`$: $`\omega'=\omega''=\mu'=\alpha=0`$, so $`a=b=f=0`$ and the first-order acceleration vanishes; exactly, $`[C^{(k)},\hat x]=0`$ at $`\tau=0`$, so $`\bar x_{\rm lab}`$ is constant. Passed.

## Open issues

- First order is not uniform in $`\lambda`$ (the non-oscillating $`\bar x_{\rm lab}`$ contains $`\lambda^3\langle b\omega'\rangle_g/6`$); long falls and second order are out of scope.
- In the factor class the level dependence at $`\delta p>0`$ comes from the unscaled hopping; whether a common factor on the hopping ($`\zeta_{x,k}\ne1`$) removes it is out of scope.

## Methods used

- plane waves and branch (band) representation
- first-order block diagonalization (Schrieffer–Wolff), explicit solution of the Sylvester equation
- Heisenberg equations and Duhamel expansion
- Taylor remainders and Cauchy–Schwarz bounds
- window averaging of oscillating terms
