# Clock rate and acceleration from rest of a body with position-dependent factors

- **Subproject:** 05-ilang-free-fall
- **Package:** 03-clock-and-fall
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-10

## Setup and assumptions

- **System.** Body $`b`$ (only instance of its type) and medium $`c`$; $`C=C_b\otimes\mathbb 1_c+\sum_xP_x\otimes K_x`$ with $`P_x=\lvert x\rangle\langle x\rvert`$, $`K_x=\kappa xX`$; start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`\lambda\ge0`$. The class $`\mathcal C`$, the linear profiles and the starts are assumptions of this package (M8).
- **Effective body contract.** By (8.19) of 04-ilang-time/08-maximal-speed, $`C_{\rm eff}=C_b+\sum_x\langle K_x\rangle P_x`$. It is again a member of $`\mathcal C`$; its plain part contains $`\kappa x\langle X\rangle`$. All profiles below are those of $`C_{\rm eff}`$. With $`\hat x:=\sum_xxP_x`$,
```math
C=C_{\rm eff}\otimes\mathbb 1_c+\kappa\,\hat x\otimes\bigl(X-\langle X\rangle\bigr).\qquad\text{(3.1)}
```
- **M6.** A replacement $`C_b\to C_b+\sum_x\alpha_xP_x`$, $`K_x\to K_x-\alpha_x\mathbb 1_c`$ leaves both terms of (3.1) unchanged; the family (8.1) with a second body changes $`C_{\rm eff}`$ by a multiple of $`\mathbb 1`$ only (8.20). A quantity is therefore well defined if it is a function of $`C_{\rm eff}`$ modulo $`\mathbb 1`$. On the clock level $`k`$ (the contract commutes with $`\lvert f_k\rangle\langle f_k\rvert`$, so $`k`$ is conserved) the on-site block at $`x`$ is $`M_{x,k}\sigma_3+V_x\mathbb 1_2`$, $`M_{x,k}:=m_x+\eta_xd_k`$, and the hopping block from $`x`$ to $`x+1`$ is $`T_x=-\tfrac{i\tau}{2}\zeta_x\sigma_1`$. The well-defined quantities used are
```math
E^{\pm}_{x,k}:=V_x\pm M_{x,k}\ (\text{modulo a common constant}),\quad \Delta_{x,k}:=2M_{x,k},\quad t_x:=\lVert T_x\rVert=\tfrac{\tau\zeta_x}{2},\quad \delta E^{\pm}_{x,k}:=E^{\pm}_{x+1,k}-E^{\pm}_{x,k},\quad\delta t_x:=t_x-t_{x-1}.\qquad\text{(3.2)}
```
The profiles are functions of these: $`m_x=\tfrac12\Delta_{x,0}`$, $`\eta_xd_k=\tfrac12(\Delta_{x,k}-\Delta_{x,0})`$, $`V_{x+1}-V_x=\tfrac12(\delta E^+_{x,k}+\delta E^-_{x,k})`$.
- **Chain.** Positions $`\lvert x\rvert\le L`$, bonds $`x\to x+1`$ for $`-L\le x<L`$, open ends; in sums, $`\zeta_{-L-1}=\zeta_L:=0`$. "$`x\in\mathbb Z`$" is the limit $`L\to\infty`$ at fixed start and fixed $`\lambda`$ (Step 1).
- **Notation.** $`R_x:=\lvert x+1\rangle\langle x\rvert`$, $`R:=\sum_x\zeta_xR_x`$; $`\tilde\phi_X(p):=\sum_xe^{-ipx}\phi_X(x)`$, so $`\hat x=i\partial_p`$ on the infinite chain. For linear profiles $`M_{x,k}=M_k+G_kx`$ with $`M_k=m+d_k`$ and $`G_k:=m\,g_m+d_k\,g_\eta`$.
- **Inputs used** (as quoted in the question): (5.21), (5.22); (6.12), (6.13), (6.24), (6.14), (6.15), (6.20); (8.19), (8.20); (9.12); (17.15) of 03-ilang-space/17-motion. Standard facts: Duhamel formula, Taylor's theorem, first-order perturbation theory in a term of the contract.
- **Orders.** Every statement is marked *exact* or *order estimate*; $`c`$ denotes a pure number that may differ from line to line.

## Derivation

### Step 1. Weak records and the long chain

Decompose $`\chi`$ over the eigenvalues $`\xi`$ of $`X`$. In the sector $`\xi`$ the body evolves with $`C_{\rm eff}+\epsilon_\xi\hat x`$, $`\epsilon_\xi=\kappa(\xi-\langle X\rangle)`$, with weights $`w_\xi`$, $`\sum_\xi w_\xi\epsilon_\xi=0`$, $`\sum_\xi w_\xi\epsilon_\xi^2=\kappa^2\sigma_X^2`$. For a body operator $`O`$, $`f(\epsilon):=\langle\phi\vert e^{i(C_{\rm eff}+\epsilon\hat x)\lambda}Oe^{-i(C_{\rm eff}+\epsilon\hat x)\lambda}\vert\phi\rangle`$ has $`\lvert f''\rvert\le(2\lambda\lVert\hat x\rVert)^2\lVert O\rVert`$ (Duhamel, twice). Taylor's theorem and the vanishing first moment give, **exactly**, for every member of $`\mathcal C`$, every start and every $`\lambda`$,
```math
\Bigl\lvert\langle O\otimes\mathbb 1_c\rangle_{\Psi(\lambda)}-\langle\phi\vert e^{iC_{\rm eff}\lambda}Oe^{-iC_{\rm eff}\lambda}\vert\phi\rangle\Bigr\rvert\le2\,\kappa^2\sigma_X^2\,L^2\lambda^2\,\lVert O\rVert .\qquad\text{(3.3)}
```
In the weak-record regime ($`\kappa\to0`$ at fixed $`\lambda`$, chain, start and fixed $`C_{\rm eff}`$) the place weights and the clock statistics are those of $`e^{-iC_{\rm eff}\lambda}\phi`$; what is neglected is bounded by (3.3). From here on $`\kappa=0`$ unless stated.

*Finite propagation.* In the Dyson series in $`A_\zeta`$ (interaction picture of the on-site part, which is diagonal in $`x`$) each factor moves $`x`$ by one and $`\lVert A_\zeta\rVert\le\tau\zeta_{\max}`$. Hence, with $`\theta:=\tau\zeta_{\max}\lambda`$,
```math
\bigl\lVert\text{part of }e^{-iC_{\rm eff}\lambda}\phi\text{ farther than }r\text{ from the support of }\phi\bigr\rVert\le e^{\theta}\,\frac{\theta^{\,r}}{r!}\qquad(\text{exact}).\qquad\text{(3.4)}
```
Two chains that agree within the distance $`r`$ of the support give expectations of $`O`$ that differ by at most $`4\lVert O\rVert e^\theta\theta^r/r!`$. The limit $`L\to\infty`$ at fixed start and fixed $`\lambda`$ therefore exists whenever $`\sup_x\zeta_x<\infty`$; for unbounded $`\zeta_x`$ the results below hold on every finite chain and the limit is not claimed.

### Step 2. The operators (item 1)

Only $`A_\zeta=-\tfrac{i\tau}{2}(R-R^\dagger)\otimes\sigma_1`$ fails to commute with $`\hat x`$ (the record term of (3.1) and the on-site terms are diagonal in $`x`$). With $`[R_x,\hat x]=-R_x`$:
```math
\frac{\mathrm d\bar x_{\rm lab}}{\mathrm d\lambda}=\langle\hat v\otimes\mathbb 1_c\rangle,\qquad \hat v:=i[C_{\rm eff},\hat x]=-\frac\tau2\sum_x\zeta_x\bigl(R_x+R_x^\dagger\bigr)\otimes\sigma_1\otimes\mathbb 1_N .\qquad\text{(3.5)}
```
Exact for every $`\kappa`$. Next $`\hat a:=i[C_{\rm eff},\hat v]`$ has three parts: $`i[A_\zeta,\hat v]=-\tfrac{\tau^2}{2}[R,R^\dagger]`$ with $`RR^\dagger=\sum_x\zeta_{x-1}^2P_x`$, $`R^\dagger R=\sum_x\zeta_x^2P_x`$; the $`\sigma_3`$ part, by $`\sigma_3\sigma_1=i\sigma_2`$, gives an anticommutator; the plain part uses $`[P_{x'},R_x]=(\delta_{x',x+1}-\delta_{x',x})R_x`$. With $`\mathsf M_x:=m_x\mathbb 1_N+\eta_xD`$,
```math
\hat a=\frac{\tau^2}{2}\sum_x\bigl(\zeta_x^2-\zeta_{x-1}^2\bigr)P_x+\frac\tau2\sum_x\zeta_x\Bigl[(R_x+R_x^\dagger)\otimes\sigma_2\otimes(\mathsf M_x+\mathsf M_{x+1})+(V_{x+1}-V_x)\,(-iR_x+iR_x^\dagger)\otimes\sigma_1\otimes\mathbb 1_N\Bigr].\qquad\text{(3.6)}
```
Since $`i[\hat x,\hat v]=A_\zeta`$, the second derivative is, **exactly** for every $`\kappa`$, every member and every start,
```math
\frac{\mathrm d^2\bar x_{\rm lab}}{\mathrm d\lambda^2}=\bigl\langle\hat a\otimes\mathbb 1_c+\kappa\,A_\zeta\otimes(X-\langle X\rangle)\bigr\rangle_{\Psi(\lambda)} .\qquad\text{(3.7)}
```
The second term vanishes at $`\lambda=0`$ (product start) and is bounded by $`2\kappa^2\sigma_X^2\,\tau\zeta_{\max}L\lambda`$ (sector argument of Step 1); it is neglected in the weak-record regime. For uniform profiles and $`V_x=-\mathcal Fx`$, (3.5)–(3.6) are (6.12).

*Starts $`S_k`$, $`S'_k`$.* In $`\lvert1\rangle`$ and in $`\lvert2\rangle`$, $`\langle\sigma_1\rangle=\langle\sigma_2\rangle=0`$. Hence, exactly, for both starts and every $`\kappa`$,
```math
\frac{\mathrm d\bar x_{\rm lab}}{\mathrm d\lambda}(0)=0,\qquad\frac{\mathrm d^2\bar x_{\rm lab}}{\mathrm d\lambda^2}(0)=\frac{\tau^2}{2}\sum_x\bigl(\zeta_x^2-\zeta_{x-1}^2\bigr)\phi_X(x)^2=2\sum_x\bigl(t_x^2-t_{x-1}^2\bigr)\phi_X(x)^2 ,\qquad\text{(3.8)}
```
which is $`\tau^2g_\zeta\bigl(1+g_\zeta\bar x_{\rm lab}(0)\bigr)`$ for linear profiles (support inside the chain). It depends on the bond profile only, and not on $`k`$, $`m`$, the branch or the clock.

### Step 3. Linear profiles: decomposition

On level $`k`$, with $`A_1=-\tau\sin\hat p\,\sigma_1`$ and $`(x+\tfrac12)R_x=\tfrac12\{\hat x,R_x\}`$, the level block is, exactly,
```math
C^{(k)}=C_0+C_1,\qquad C_0=-\tau\sin\hat p\,\sigma_1+M_k\sigma_3,\qquad C_1=\tfrac12\{\hat x,B(\hat p)\},\qquad B(p):=-g_\zeta\tau\sin p\,\sigma_1+G_k\sigma_3-\mathcal F .\qquad\text{(3.9)}
```
*Recentring (exact).* With $`y=x-x_0`$ the contract has the same form about $`x_0`$, with $`(\tau,M_k,g_\zeta)\to(\tau^0,M^0_k,g^0_\zeta):=\bigl(\tau(1+g_\zeta x_0),\,M_{x_0,k},\,g_\zeta/(1+g_\zeta x_0)\bigr)`$, $`G_k`$ and $`\mathcal F`$ unchanged, plus $`V_{x_0}\mathbb 1`$. Local and original parameters differ at second order in the gradients.

From (3.6), $`\hat a=\hat a_0+\hat a_1+\hat a_2`$ with $`\hat a_0=2\tau M_k\cos\hat p\,\sigma_2`$ and
```math
\hat a_1=\tau^2g_\zeta+\tfrac12\{\hat x,F_a(\hat p)\}+\mathcal F\tau\sin\hat p\,\sigma_1,\qquad F_a(p):=2\tau(M_kg_\zeta+G_k)\cos p\,\sigma_2 .
```

### Step 4. Acceleration to first order in the gradients (item 2(a))

Infinite chain, start $`S_k(x_0)`$. Let $`U_t(p):=e^{-iC_0(p)t}`$, $`\chi_t(p):=U_t\lvert1\rangle=\bigl(\cos\omega t-i\tfrac{M_k}{\omega}\sin\omega t\bigr)\lvert1\rangle+i\tfrac{\tau\sin p}{\omega}\sin\omega t\,\lvert2\rangle`$, $`\omega=\omega_k(p)`$. The zeroth-order state is $`\psi_0(\lambda)=\tilde\phi_X\chi_\lambda`$, and $`\psi_1(\lambda)=-i\int_0^\lambda\mathrm ds\,U_{\lambda-s}C_1\psi_0(s)`$ (first-order perturbation theory). For spinor functions $`u,v`$ and $`\xi:=-\partial_p\arg\tilde\phi_X`$, an integration by parts gives the identity
```math
\bigl\langle\tilde\phi_Xu\bigm\vert\tfrac12\{\hat x,F(\hat p)\}\bigm\vert\tilde\phi_Xv\bigr\rangle=\int\frac{\mathrm dp}{2\pi}\lvert\tilde\phi_X\rvert^2\Bigl\{\xi\,u^\dagger Fv+\tfrac i2\bigl[u^\dagger F\,\partial_pv-(\partial_pu^\dagger)Fv\bigr]\Bigr\}.
```
*Parity.* $`C_0(-p)=\sigma_3C_0(p)\sigma_3`$, $`B(-p)=\sigma_3B(p)\sigma_3`$, $`\chi_t(-p)=\sigma_3\chi_t(p)`$, $`\sigma_3\sigma_2\sigma_3=-\sigma_2`$, and $`\phi_X`$ real makes $`\lvert\tilde\phi_X\rvert^2`$ and $`\xi`$ even. Consequences, all exact: the zeroth-order acceleration $`\langle\psi_0\vert\hat a_0\vert\psi_0\rangle`$ vanishes for all $`\lambda`$; every term with $`\xi`$ (which carries $`x_0`$ and any asymmetry of $`w`$) has an odd coefficient and integrates to zero. With $`u_s^\dagger:=\chi_\lambda^\dagger\,\hat a_0(p)\,U_{\lambda-s}`$, the first-order coefficient $`a^{(1)}=\langle\psi_0\vert\hat a_1\vert\psi_0\rangle+2\mathrm{Re}\langle\psi_0\vert\hat a_0\vert\psi_1\rangle`$ is, **exactly** (first Taylor coefficient, infinite chain, every real $`\phi_X`$, every $`x_0`$),
```math
a^{(1)}(\lambda)=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert\tilde\phi_X(p)\rvert^2\alpha(p,\lambda),\quad
\alpha:=\tau^2g_\zeta+\mathcal F\tau\sin p\,\chi_\lambda^\dagger\sigma_1\chi_\lambda-\mathrm{Im}\bigl[\chi_\lambda^\dagger F_a\partial_p\chi_\lambda\bigr]+\int_0^\lambda\!\mathrm ds\mathrm{Re}\bigl[u_s^\dagger B\,\partial_p\chi_s-(\partial_pu_s^\dagger)B\chi_s\bigr],\qquad\text{(3.10)}
```
with $`\alpha`$ smooth and even in $`p`$ and independent of $`x_0`$.

*Value at $`p=0`$.* There $`\chi_t=e^{-iM_kt}\lvert1\rangle`$, $`\partial_p\chi_t=\tfrac{i\tau}{M_k}\sin(M_kt)\lvert2\rangle`$, $`\partial_pU_t=\tfrac{i\tau}{M_k}\sin(M_kt)\sigma_1`$, $`\hat a_0=2\tau M_k\sigma_2`$, $`\partial_p\hat a_0=0`$, $`B=G_k\sigma_3-\mathcal F`$. Then $`-\mathrm{Im}[\chi_\lambda^\dagger F_a\partial_p\chi_\lambda]=-\tfrac{2\tau^2}{M_k}(M_kg_\zeta+G_k)\sin^2(M_k\lambda)`$, and
```math
\begin{aligned}
\mathrm{Re}\bigl[u_s^\dagger B\partial_p\chi_s\bigr]&=-2\tau^2(G_k+\mathcal F)\cos\bigl(M_k(2\lambda-s)\bigr)\sin(M_ks),\\
\mathrm{Re}\bigl[(\partial_pu_s^\dagger)B\chi_s\bigr]&=\tau^2(G_k-\mathcal F)\bigl[\sin(2M_k\lambda)+\sin\bigl(2M_k(\lambda-s)\bigr)\bigr],
\end{aligned}
```
whose difference integrates to $`-2\tau^2G_k\lambda\sin(2M_k\lambda)+\tfrac{2\tau^2}{M_k}\mathcal F\sin^2(M_k\lambda)`$. Therefore
```math
\boxed{\;a^{(1)}_\infty(\lambda):=\alpha(0,\lambda)=\tau^2g_\zeta\cos(2M_k\lambda)+\frac{2\tau^2}{M_k}\bigl(\mathcal F-G_k\bigr)\sin^2(M_k\lambda)-2\tau^2G_k\,\lambda\,\sin(2M_k\lambda)\;}\qquad\text{(3.11)}
```
This is the limit of a wide start. The third term grows with $`\lambda`$: on the level $`k`$ the two branch components move in opposite directions in $`p`$ under $`G_k\hat x\sigma_3`$, so the oscillation between the branches has an amplitude proportional to $`\lambda`$.

*What the limits require.* With $`\delta_W^2:=\sum_x(\phi_X(x+1)-\phi_X(x))^2=O(W^{-2})`$, $`p^2\le\tfrac{\pi^2}{4}\,4\sin^2\tfrac p2`$ and evenness of $`\alpha`$,
```math
\bigl\lvert a^{(1)}(\lambda)-a^{(1)}_\infty(\lambda)\bigr\rvert\le\frac{\pi^2}{8}\,\delta_W^2\,\sup_p\lvert\partial_p^2\alpha\rvert\ \ (\text{exact}),\qquad \sup_p\lvert\partial_p^2\alpha\rvert\le c\,\tau\,b_1\,(1+M_k\lambda)(1+\tau\lambda)^3,\qquad\text{(3.12)}
```
with $`b_1:=(\tau+M_k)\lvert g_\zeta\rvert+\lvert G_k\rvert+\lvert\mathcal F\rvert`$; the second bound holds for all $`\lambda\ge0`$ up to the number $`c`$ (each $`\partial_p`$ of $`U_t`$ costs at most a factor $`c(1+\tau t)`$, by Duhamel). Requirements:
- $`L`$: on the chain $`\lvert x\rvert\le L`$ with $`\lvert x_0\rvert+W<L`$ the first-order coefficient differs from (3.10) by at most $`c\,\tau M_k(1+b_1L\lambda)\,e^{\tau\lambda}(\tau\lambda)^r/r!`$, $`r=L-\lvert x_0\rvert-W`$ (order estimate, from (3.4)); the limit is $`r\to\infty`$ at fixed $`\lambda`$, and the correction is negligible once $`r\gg e\,\tau\lambda`$.
- $`x_0`$: nothing on the infinite chain ((3.10) does not depend on $`x_0`$).
- $`W`$: $`W\to\infty`$ at fixed $`\lambda`$; by (3.12) the error is small on $`[0,\lambda_{\max}]`$ if $`W^2\gg(1+M_k\lambda_{\max})(1+\tau\lambda_{\max})^3`$ relative to $`\tau b_1`$ (sufficient).
- $`\lambda`$: fixed; none of the limits is uniform in $`\lambda`$.

In the background (17.15) the acceleration is $`\kappa\,a^{(1)}\,e`$.

### Step 5. Window averages (item 2(b))

Integrating (3.11) with $`\mathrm d\bar x_{\rm lab}/\mathrm d\lambda(0)=0`$ (exact consequences of (3.11)):
```math
v^{(1)}_\infty(\lambda)=\frac{\tau^2}{M_k}(\mathcal F-G_k)\,\lambda+\frac{\tau^2G_k}{M_k}\,\lambda\cos(2M_k\lambda)+\frac{\tau^2}{2M_k^2}\,(M_kg_\zeta-\mathcal F)\sin(2M_k\lambda).\qquad\text{(3.13)}
```
For the window $`[\lambda_1,T]`$, $`T=\lambda_1+\Lambda`$, with $`\rho`$ of (6.24) and $`\varsigma:=\bigl(T\cos(2M_kT)-\lambda_1\cos(2M_k\lambda_1)\bigr)/\Lambda`$, the average $`\overline a=(v(T)-v(\lambda_1))/\Lambda`$ is, exactly for every window,
```math
\overline{a^{(1)}_\infty}=\frac{\tau^2}{M_k}\Bigl[(\mathcal F-G_k)+G_k\,\varsigma+(M_kg_\zeta-\mathcal F)\,\rho\Bigr],\qquad\lvert\rho\rvert\le\frac1{M_k\Lambda},\qquad\varsigma=\cos(2M_kT)+\frac{\lambda_1}{\Lambda}\bigl[\cos(2M_kT)-\cos(2M_k\lambda_1)\bigr].\qquad\text{(3.14)}
```
*Coefficients for a long window* ($`\Lambda\to\infty`$ at fixed $`\lambda_1`$, i.e. $`\Lambda\gg1/(2M_k)`$):
- of $`\mathcal F`$: $`\tfrac{\tau^2}{M_k}(1-\rho)\to\tfrac{\tau^2}{M_k}`$ (limit exists, error $`\le\tau^2/(M_k^2\Lambda)`$);
- of $`g_\zeta`$: $`\tau^2\rho\to0`$;
- of $`g_m`$ and $`g_\eta`$: $`-\tfrac{\tau^2m}{M_k}(1-\varsigma)`$ and $`-\tfrac{\tau^2d_k}{M_k}(1-\varsigma)`$. **These have no limit:** $`1-\varsigma=2\sin^2(M_kT)+O(\lambda_1/\Lambda)`$ takes every value in $`[0,2]`$ however long the window is. Example: over $`[0,n\pi/M_k]`$ the $`G_k`$ part of $`\overline a`$ is exactly $`0`$; over $`[\tfrac{\pi}{2M_k},\tfrac{\pi}{2M_k}+\tfrac{n\pi}{M_k}]`$ it is $`-2\tau^2G_k/M_k`$.

What does converge is the displacement. Integrating (3.13),
```math
\bar x^{(1)}_{\rm lab}(\lambda)-\bar x_{\rm lab}(0)=\tfrac12\,a_{\rm sec}\,\lambda^2+\frac{\tau^2G_k}{2M_k^2}\,\lambda\sin(2M_k\lambda)+\frac{\tau^2}{2M_k^3}\bigl(M_kg_\zeta-\mathcal F-G_k\bigr)\sin^2(M_k\lambda),\qquad\boxed{\;a_{\rm sec}:=\frac{\tau^2}{M_k}\bigl(\mathcal F-G_k\bigr)\;}\qquad\text{(3.15)}
```
The **secular acceleration** $`a_{\rm sec}`$ is the limit $`\Lambda\to\infty`$ of the doubly averaged acceleration $`\tfrac{2}{\Lambda^2}\int_0^\Lambda(\Lambda-\lambda)a^{(1)}_\infty\,\mathrm d\lambda=2[\bar x^{(1)}_{\rm lab}(\Lambda)-\bar x_{\rm lab}(0)]/\Lambda^2`$, with a relative error $`O(1/(M_k\Lambda))`$ (exact from (3.15)); it is also the mean of (3.14) over the window end $`T`$ over one period $`\pi/M_k`$, up to $`O(1/(M_k\Lambda))`$. The plain window average equals $`a_{\rm sec}`$ plus $`\tfrac{\tau^2}{M_k}[G_k\varsigma+(M_kg_\zeta-\mathcal F)\rho]`$.

*Range of validity of the first-order treatment.* (3.10), (3.11), (3.13)–(3.15) are exact statements about the first Taylor coefficient. For the remainder, take a chain that reaches at most $`\ell\ge1`$ sites from $`x_0`$, parameters at $`x_0`$ (Step 3), and $`b_1\ell\le M_k`$. Taylor's theorem in a common scale of the gradients, with $`\lVert C_1\rVert\le b_1\ell`$, $`\lVert\hat a\rVert\le c\tau M_k`$, $`\lVert\hat a_1\rVert\le c\tau b_1\ell`$, $`\lVert\hat a_2\rVert\le c\tau(b_1\ell)^2/M_k`$ and Duhamel's formula, gives for all $`\lambda\ge0`$
```math
\bigl\lvert a(\lambda)-a^{(0)}_\ell(\lambda)-a^{(1)}_\ell(\lambda)\bigr\rvert\le c\,\tau M_k\,\bigl[b_1\,\ell\,(\lambda+M_k^{-1})\bigr]^2 ,\qquad\text{(3.16)}
```
rigorous up to the number $`c`$; $`a^{(0)}_\ell,a^{(1)}_\ell`$ are the coefficients on that chain, which differ from $`0`$ and (3.10) by the edge terms of Step 4. The first-order treatment is valid where (3.16) is small compared with (3.11), for which $`b_1\ell^2(1+M_k\lambda)\ll\tau`$ suffices. This is a sufficient condition (order estimate); it is not shown to be necessary. For variant (d) the quoted (6.14) gives the range $`\mathcal F_{\max}T\ll\min(1,M_k/\tau)`$.

### Step 6. Well-defined form, variants, other branch (items 2(c)–(e))

*(c).* With (3.2) at $`x_0`$: $`\tau^2/M_k=8t^2/\Delta_k`$, $`G_k=\tfrac12\delta\Delta_k`$, $`\mathcal F-G_k=-\delta E^+_k`$, $`g_\zeta=\delta t/t`$, so
```math
a_{\rm sec}=-\frac{8t^2}{\Delta_k}\,\delta E^+_k,\qquad\overline{a^{(1)}_\infty}=\frac{8t^2}{\Delta_k}\Bigl[-\delta E^+_k+\tfrac12\,\delta\Delta_k\,\varsigma+\Bigl(\tfrac{\Delta_k}{2}\tfrac{\delta t}{t}+\tfrac12(\delta E^+_k+\delta E^-_k)\Bigr)\rho\Bigr],\qquad\text{(3.17)}
```
where $`\rho,\varsigma`$ depend on the contract through $`\Delta_k=2M_k`$ only. Only gaps, norms of hopping blocks and differences of on-site eigenvalues between neighbouring positions occur; no single cost occurs. The secular acceleration of the start $`S_k`$ is fixed by the neighbour difference of the *upper* on-site eigenvalue of level $`k`$.

*(e), other branch.* Conjugation with $`\sigma_1`$ leaves $`A_\zeta`$, $`\hat v`$, $`V_x`$ unchanged, maps $`\lvert2\rangle\to\lvert1\rangle`$ and $`(M_k,G_k)\to(-M_k,-G_k)`$; the $`p=0`$ data of Step 4 hold for either sign of $`M_k`$. For $`S'_k(x_0)`$:
```math
a'^{(1)}_\infty=\tau^2g_\zeta\cos(2M_k\lambda)-\frac{2\tau^2}{M_k}(\mathcal F+G_k)\sin^2(M_k\lambda)-2\tau^2G_k\lambda\sin(2M_k\lambda),\qquad a'_{\rm sec}=-\frac{\tau^2}{M_k}(\mathcal F+G_k)=+\frac{8t^2}{\Delta_k}\,\delta E^-_k,\qquad\text{(3.18)}
```
and $`\overline{a'^{(1)}_\infty}=a'_{\rm sec}+\tfrac{\tau^2}{M_k}[G_k\varsigma+(M_kg_\zeta+\mathcal F)\rho]`$.

*(d), variants.* With $`M_k=m+d_k`$, $`d_k=2\pi k/(N\lambda_0)`$:
```math
a_{\rm sec}:\quad\text{(a)}\ -g\tau^2,\qquad\text{(b1)}\ -g\tau^2\frac{m}{m+d_k},\qquad\text{(b2)}\ -g\tau^2\frac{d_k}{m+d_k},\qquad\text{(c)}\ -g\tau^2,\qquad\text{(d)}\ \frac{\tau^2\mathcal F}{m+d_k}.\qquad\text{(3.19)}
```

| Variant | $`a_{\rm sec}`$, start $`S_k`$ | depends on $`m`$ | on $`k`$ | on $`N`$, $`\lambda_0`$ | on $`\tau`$ | $`a'_{\rm sec}`$, start $`S'_k`$ |
| --- | --- | --- | --- | --- | --- | --- |
| (a) | $`-g\tau^2`$ | no | no | no | yes | $`-g\tau^2`$ |
| (b1) | $`-g\tau^2\,m/(m+d_k)`$ | yes for $`k\ge1`$ | yes | yes for $`k\ge1`$ | yes | $`-g\tau^2\,m/(m+d_k)`$ |
| (b2) | $`-g\tau^2\,d_k/(m+d_k)`$ | yes for $`k\ge1`$ | yes | yes for $`k\ge1`$ | yes | $`-g\tau^2\,d_k/(m+d_k)`$ |
| (c) | $`-g\tau^2`$ | no | no | no | yes | $`-g\tau^2`$ |
| (d) | $`\tau^2\mathcal F/(m+d_k)`$ | yes | yes | yes for $`k\ge1`$ | yes | $`-\tau^2\mathcal F/(m+d_k)`$ |

The plain window averages are $`-g\tau^2(1-\varsigma)`$ for (a), $`-g\tau^2(1-\varsigma-\rho)`$ for (c), $`(1-\varsigma)`$ times the entry for (b1), (b2), and $`(1-\rho)`$ times the entry for (d). Through $`\varsigma`$ and $`\rho`$ they depend on $`M_k`$, hence on $`m`$, $`k`$, $`N`$, $`\lambda_0`$, in every variant; for (d) this dependence vanishes as $`1/(M_k\Lambda)`$, for the others it does not vanish. In (a), (b1), (b2), (c) both branches have the same secular acceleration; in (d) they have opposite ones. The bond gradient alone gives $`a_{\rm sec}=0`$.

### Step 7. Clock rate, uniform profiles (item 3(a))

For uniform profiles $`C_b=\zeta_\ast A_1+\sigma_3\otimes(m_\ast+\eta_\ast D)+V_\ast\mathbb 1`$ is, identically, the Model D contract with $`(\tau,m,\lambda_0)\to(\tau\zeta_\ast,\,m_\ast,\,\lambda_0/\eta_\ast)`$ plus $`V_\ast\mathbb 1`$; the vectors $`\lvert f_k\rangle`$ are unchanged and $`V_\ast\mathbb 1`$ changes only the common phase (1.2). Hence (5.21) and (5.22) hold with these substitutions. With $`\bar d=\pi(N-1)/(N\lambda_0)`$, $`\bar\mu_\ast:=m_\ast+\eta_\ast\bar d`$, $`\epsilon_\ast:=2\pi\eta_\ast/(N\lambda_0m_\ast)`$:
```math
q(a;\lambda)=P_N\Bigl(a;\Gamma_\ast(p_0)\frac{\eta_\ast\lambda}{\lambda_0}\Bigr)+\mathcal R_\ast,\qquad\Gamma_\ast(p_0)=\frac{\bar\mu_\ast}{\sqrt{\bar\mu_\ast^2+\tau^2\zeta_\ast^2\sin^2p_0}},\qquad\mathcal R_\ast=O\bigl((N\epsilon_\ast)^2(1+\eta_\ast\lambda/\lambda_0)^2\bigr)+O(\delta p^2)+O(\kappa),\qquad\text{(3.20)}
```
```math
\lambda_\ast(p_0)=\frac{\lambda_0}{\eta_\ast\,\Gamma_\ast(p_0)},\qquad\lambda_\ast(0)=\frac{\lambda_0}{\eta_\ast}.\qquad\text{(3.21)}
```
The tick at $`p_0=0`$ depends on $`\eta_\ast`$ only; it does not depend on $`m_\ast`$, $`\zeta_\ast`$ or $`V_\ast`$.

### Step 8. Clock rate, linear profiles (item 3(b))

Start $`S_{\rm clock}(x_0)`$, $`\lvert0\rangle=N^{-1/2}\sum_k\lvert f_k\rangle`$. With $`\psi_k(\lambda):=e^{-iC^{(k)}\lambda}(\phi_X\otimes\lvert1\rangle)`$, exactly at $`\kappa=0`$,
```math
q(a;\lambda)=\frac1{N^2}\sum_{k,k'}e^{2\pi i(k-k')a/N}\,\langle\psi_{k'}(\lambda)\vert\psi_k(\lambda)\rangle .
```
*Zeroth order in the gradients at fixed profiles at $`x_0`$:* $`C^{(k)}\to-\tau^0\sin\hat p\,\sigma_1+M_{x_0,k}\sigma_3+V_{x_0}`$ (Step 3). From $`\chi_t`$ of Step 4, $`\chi_{k',\lambda}^\dagger\chi_{k,\lambda}=e^{-i(\omega_k-\omega_{k'})\lambda}+O(\tau^{0\,2}p^2/m_{x_0}^2)`$ and $`\lvert(\omega_k-\omega_{k'})-(M_{x_0,k}-M_{x_0,k'})\rvert\le\lvert M_{x_0,k}-M_{x_0,k'}\rvert\,\tau^{0\,2}p^2/(2m_{x_0}^2)`$, while $`M_{x_0,k}-M_{x_0,k'}=\eta_{x_0}\tfrac{2\pi(k-k')}{N\lambda_0}`$ is exactly linear in $`k`$. Summing the geometric series,
```math
q(a;\lambda)=P_N\Bigl(a;\frac{\eta_{x_0}\lambda}{\lambda_0}\Bigr)+\mathcal R_{\rm cl},\qquad\mathcal R_{\rm cl}=O\Bigl(\frac{\tau^{0\,2}}{m_{x_0}^2}\,\delta_W^2\,\bigl(1+\eta_{x_0}\lambda/\lambda_0\bigr)\Bigr)+(\text{gradient terms below})+O\bigl(\kappa^2\sigma_X^2L^2\lambda^2\bigr).\qquad\text{(3.22)}
```
At rest $`\Gamma=1`$ for every level, so the first-order form in the level spacing has no correction of higher order in the level spacing except with the factor $`\delta_W^2=O(W^{-2})`$. **Definition:** the advance is $`\vartheta_{x_0}(\lambda)=\eta_{x_0}\lambda/\lambda_0`$, and
```math
\text{rate at }x_0:=\frac{\mathrm d\vartheta_{x_0}}{\mathrm d\lambda}=\frac{\eta_{x_0}}{\lambda_0}=\frac{N}{2\pi}\bigl(E^+_{x_0,k+1}-E^+_{x_0,k}\bigr),\qquad\text{tick }\frac{\lambda_0}{\eta_{x_0}} .\qquad\text{(3.23)}
```
It is a difference of on-site eigenvalues (M6), the spacing of adjacent clock levels at $`x_0`$.

*First corrections.*
- *Reason for the order.* Let $`\Pi`$ be the reflection $`y\to-y`$ about $`x_0`$ times $`\sigma_3`$. Then $`\Pi C_0\Pi=C_0`$ and $`\Pi C_1\Pi=-C_1`$ (parameters at $`x_0`$), the clock reading commutes with $`\Pi`$, and for $`w`$ even the start is $`\Pi`$-invariant. Hence, exactly (infinite chain, $`w`$ even), $`q`$ is an even function of $`(g_m,g_\eta,g_\zeta,\mathcal F)`$ jointly at fixed profiles at $`x_0`$: no first-order term.
- *$`w`$ not even.* By the identity of Step 4 with $`u=\chi_{k'}`$, $`v=\chi_k`$, the first-order change of $`\langle\psi_{k'}\vert\psi_k\rangle`$ at $`p=0`$ is the factor $`-i\lambda\,g_\eta(d_k-d_{k'})\,\bar y_0`$, $`\bar y_0:=\bar x_{\rm lab}(0)-x_0=O(W)`$: the rate is $`\eta`$ at the mean position of the start. This is first order in $`g_\eta W`$ and is a relabelling of the place; the other first-order terms carry $`\delta_W^2`$.
- *Width.* At $`\tau=0`$ the contract is diagonal in $`x`$ and, exactly, $`q(a;\lambda)=\sum_x\phi_X(x)^2P_N(a;\eta_x\lambda/\lambda_0)`$, a mixture of clocks with different rates. Expanding about the mean position, the width first changes $`q`$ at order $`(g_\eta\,s_W\,\lambda/\lambda_0)^2`$, $`s_W^2:=\sum_x(x-\bar x_{\rm lab}(0))^2\phi_X(x)^2\le W^2`$: second power of $`g_\eta W`$, and through the clock gradient only.
- *Beginning motion.* By the evenness above, it first changes $`q`$ at second order in the gradients times $`\lambda`$. For variant (d), (9.12) at $`p_0=0`$ gives $`\vartheta=\tfrac{\lambda}{\lambda_0}\bigl[1-\tfrac{\tau^2\mathcal F^2\lambda^2}{6\bar\mu^2}+O((\mathcal F\lambda)^4)\bigr]`$, order $`(\tau\mathcal F\lambda/\bar\mu)^2`$. For the other variants the second-order coefficient is not computed here.

### Step 9. Two places and comparison (items 3(c), 4)

*Procedure.* The rates at $`x_1`$ and $`x_2`$ are taken from two runs of the same description (same contract list, starts $`S_{\rm clock}(x_1)`$ and $`S_{\rm clock}(x_2)`$), with the clock reading applied at the same value of $`\lambda`$ in both. The comparison relies on A8: readings at equal $`\lambda`$ are compared through the order of $`\lambda`$, which is not a time (M1). The ratio of rates is the ratio of the advances at equal $`\lambda`$, the inverse ratio of the ticks. By (3.23),
```math
\frac{\text{rate at }x_1}{\text{rate at }x_2}=\frac{\eta_{x_1}}{\eta_{x_2}}=\frac{1+g_\eta x_1}{1+g_\eta x_2}:\qquad\text{(a), (b2), (c)}:\ \frac{1+gx_1}{1+gx_2};\qquad\text{(b1), (d)}:\ 1 .\qquad\text{(3.24)}
```
It holds to the order of (3.22). It does not depend on the unit of $`\lambda`$ (a rescaling of $`\lambda`$ rescales both rates), nor on $`m`$, $`N`$, $`\lambda_0`$ in any variant.

*Comparison (item 4), first order in the gradients, wide start:*

| Variant | $`a_{\rm sec}`$ from rest the same for all $`k`$ and all $`m`$ | clock rate depends on the place |
| --- | --- | --- |
| (a) | yes, $`-g\tau^2`$ | yes |
| (b1) | no | no |
| (b2) | no | yes |
| (c) | yes, $`-g\tau^2`$ | yes |
| (d) | no | no |

```math
\text{Both properties: the variants (a) and (c), and only these among the five.}\qquad\text{(3.25)}
```
The statement for (a) and (c) is for the secular acceleration (3.15). The plain window average (3.14) and the function (3.11) depend on $`k`$ and $`m`$ in (a) and (c) as well, through $`\cos(2M_kT)`$ and $`\sin(2M_k\lambda)`$, with an amplitude that does not decrease.

## Result

- **Item 1.** Operators (3.5), (3.6) and the exact second derivative (3.7); values at $`\lambda=0`$ (3.8), equal for $`S_k`$ and $`S'_k`$.
- **Item 2.** First-order acceleration (3.10) and its wide-start limit (3.11), with the requirements (3.12); velocity (3.13); window average (3.14), whose coefficients of $`g_m`$, $`g_\eta`$ have no long-window limit; secular acceleration and displacement (3.15); remainder (3.16); well-defined form (3.17); other branch (3.18); variants (3.19) and table.
- **Item 3.** Uniform profiles (3.20), tick (3.21); linear profiles (3.22), rate (3.23), orders of the first corrections (Step 8); ratio (3.24).
- **Item 4.** Table of Step 9 and (3.25).
- **Controls (M9).** A fall independent of $`k`$ and $`m`$ fails in (b1), (b2), (d); a place-dependent rate fails in (b1), (d); equal fall of the two branches fails in (d) (start $`S'_k`$).

## Consistency checks

1. **Dimensions and zero gradients.** With $`x`$ a pure label, $`\tau`$, $`M_k`$, $`G_k`$, $`\mathcal F`$ have the unit $`1/\lambda`$ and $`g_\bullet`$ none; (3.8), (3.11), (3.15) have the unit $`1/\lambda^2`$, (3.23) $`1/\lambda`$. For zero gradients (3.6) is $`\hat a_0`$ of (6.12), (3.11) vanishes, (3.22) is $`P_N(a;\lambda/\lambda_0)`$ and (3.24) is $`1`$. Passed.
2. **Variant (d).** (3.5)–(3.6) reduce to (6.12); (3.11) gives $`\tfrac{2\tau^2}{M_k}\mathcal F\sin^2(M_k\lambda)`$, the label form of (6.13); (3.14) gives $`\tfrac{\tau^2}{M_k}\mathcal F(1-\rho)`$, in agreement with (6.24), (6.15) and $`\overline{\ddot{\bar m}}=\mathcal F/I^{\rm lab}_k`$ of (6.20). Passed.
3. **$`\tau\to0`$ and order $`\tau^2`$.** All accelerations are $`\propto\tau^2`$ and vanish; the clock formula becomes the exact mixture of Step 8. An independent expansion to order $`\tau^2`$ in the interaction picture of the on-site term (hopping block phases $`e^{i(2M_k+G_k(2x+1))\lambda\sigma_3}`$) reproduces the three terms of (3.13), including $`-\tfrac{2\tau^2G_k}{M_k}\lambda\sin^2(M_k\lambda)`$ for the $`G_k`$ part. Passed.

## Open issues

- At strict first order (the order of limits of the question) the plain window average of the acceleration has no long-window limit when $`G_k\neq0`$; this is proven. What happens to the growing oscillation of (3.11) beyond first order (in particular when $`\lvert G_k\rvert W\lambda`$ is not small, where the branch oscillation has different phases across the start) is not derived here; it belongs to the package on long falls.
- The range (3.16) is a sufficient condition; the sharp range of the first-order treatment is not determined.
- The second-order coefficient of the beginning motion in $`q`$ is given only for variant (d).
- For unbounded bond profiles the limit of a long chain is not shown.
- The two rates are compared across two runs through A8; a comparison inside one description is not treated.

## Methods used

- Heisenberg equations of motion, commutators on a chain
- Effective body contract and sector decomposition of the records
- First-order perturbation theory (Duhamel), Taylor remainder bounds
- Plane-wave representation, parity and reflection symmetry
- Finite-propagation (Dyson series) bound
- Window averaging of oscillating terms
- Spectrum of a ring clock (geometric sum)
