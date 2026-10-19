# Clock rate and acceleration from rest of a body with position-dependent factors

- **Subproject:** 05-ilang-free-fall
- **Package:** 03-clock-and-fall
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-10

## Changes from previous version

- **Step 8 (I1).** New: the clock distribution of the named start at zeroth order in the gradients and finite $`W`$, exactly (3.34) and to first order in the level spacing (3.35); the advance and the rate at finite $`W`$ (3.36). (3.22) is unchanged as a bound; it is now stated as the wide-start approximation, with its range.
- **(3.23), (3.24), (3.25) (I1).** Statements changed, tags kept. (3.23): the rate $`\eta_{x_0}/\lambda_0`$ is the wide-start limit of the finite-width rate (3.36), with the correction and its bounds. (3.24): the ratio at finite $`W`$ carries the factor $`(1-\varsigma_W(x_1))/(1-\varsigma_W(x_2))`$, evaluated for the five variants. (3.25): the clock column is stated for the wide start and for finite $`W`$.
- **Step 8 (I2).** New (3.37): the exact first-order term in the gradients. "Lowest order allowed by a symmetry", "upper bound" and "first nonzero order" are separate columns of Table 8.1; the parts of item 3(b) that are not determined are named. The position spread of the start is now written $`\sigma_W`$ (v2 used $`s_W`$ for two different quantities).
- **Step 5.2 (I3).** $`A_2`$ of (3.26) is given explicitly (a refinement; the statement of (3.26) is otherwise unchanged). The late-time estimate of the oscillating part is corrected for every gradient.
- **Consistency check 1 (I4).** Units of the velocity density (3.26) and of its coefficients corrected.
- Unchanged in statement: (3.1)–(3.22), (3.27)–(3.33).

## Response to verification

- **I1: Accepted and fixed in Step 8, parts (i)–(iv), and Step 9.** The finite-$`W`$ distribution, advance and rate are derived (3.34)–(3.36). (3.23) and (3.24) are stated with the approximation (wide start), its range and the finite-width corrections; the dependence on $`m`$, $`N`$, $`\lambda_0`$, $`\tau`$ and the levels is listed with bounds. The statement about the rate is separate from the bound on $`q`$. Carried into (3.24), the table of Step 9, (3.25) and the Result section.
- **I2: Accepted and fixed in Step 8, part (v).** Table 8.1 keeps the three notions apart; first nonzero orders are proven where stated, and the undetermined parts are named.
- **I3: Accepted and fixed in Step 5.2.** The plain gradient has a growing oscillating part of the same order as $`G_k`$; the bond gradient has a decaying one.
- **I4: Accepted and fixed in Consistency check 1.**

## Setup and assumptions

- **System.** Body $`b`$ (only instance of its type) and medium $`c`$; $`C=C_b\otimes\mathbb 1_c+\sum_xP_x\otimes K_x`$ with $`P_x=\lvert x\rangle\langle x\rvert`$, $`K_x=\kappa xX`$; start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`\lambda\ge0`$. The class $`\mathcal C`$, the linear profiles and the starts are assumptions of this package (M8).
- **Effective body contract.** By (8.19) of 04-ilang-time/08-maximal-speed, $`C_{\rm eff}=C_b+\sum_x\langle K_x\rangle P_x`$. It is again a member of $`\mathcal C`$; its plain part contains $`\kappa x\langle X\rangle`$. All profiles below are those of $`C_{\rm eff}`$. With $`\hat x:=\sum_xxP_x`$,
```math
C=C_{\rm eff}\otimes\mathbb 1_c+\kappa\,\hat x\otimes\bigl(X-\langle X\rangle\bigr).\qquad\text{(3.1)}
```
- **M6.** By (8.1), the replacements that leave $`C`$ unchanged add real numbers $`\alpha_h`$ to the diagonal entries of $`C_b`$ at the places $`h=(x,s,a)`$ and subtract $`\alpha_h\mathbb 1_c`$ from the record of $`h`$; both terms of (3.1) are unchanged by them, for every dependence of $`\alpha_h`$ on the place. With a second body, (8.1) also allows $`Z`$, which changes $`C_{\rm eff}`$ by a multiple of $`\mathbb 1`$ only (8.20). A quantity is therefore well defined if it is a function of $`C_{\rm eff}`$ modulo $`\mathbb 1`$ and of the start. On the clock level $`k`$ (the contract commutes with $`\lvert f_k\rangle\langle f_k\rvert`$, so $`k`$ is conserved) the on-site block at $`x`$ is $`M_{x,k}\sigma_3+V_x\mathbb 1_2`$, $`M_{x,k}:=m_x+\eta_xd_k`$, and the hopping block from $`x`$ to $`x+1`$ is $`T_x=-\tfrac{i\tau}{2}\zeta_x\sigma_1`$. The well-defined quantities used are
```math
E^{\pm}_{x,k}:=V_x\pm M_{x,k}\ (\text{modulo a common constant}),\quad \Delta_{x,k}:=2M_{x,k},\quad t_x:=\lVert T_x\rVert=\tfrac{\tau\zeta_x}{2},\quad \delta E^{\pm}_{x,k}:=E^{\pm}_{x+1,k}-E^{\pm}_{x,k},\quad\delta t_x:=t_x-t_{x-1}.\qquad\text{(3.2)}
```
The profiles are functions of these: $`m_x=\tfrac12\Delta_{x,0}`$, $`\eta_xd_k=\tfrac12(\Delta_{x,k}-\Delta_{x,0})`$, $`V_{x+1}-V_x=\tfrac12(\delta E^+_{x,k}+\delta E^-_{x,k})`$.
- **Chain.** Positions $`\lvert x\rvert\le L`$, bonds $`x\to x+1`$ for $`-L\le x<L`$, open ends; in sums, $`\zeta_{-L-1}=\zeta_L:=0`$. "$`x\in\mathbb Z`$" is the limit $`L\to\infty`$ at fixed start and fixed $`\lambda`$ (Step 1).
- **Notation.** $`R_x:=\lvert x+1\rangle\langle x\rvert`$, $`R:=\sum_x\zeta_xR_x`$; $`\tilde\phi_X(p):=\sum_xe^{-ipx}\phi_X(x)`$, so $`\hat x=i\partial_p`$ on the infinite chain; $`\langle f\rangle_W:=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert\tilde\phi_X(p)\rvert^2f(p)`$, with $`\langle1\rangle_W=1`$; $`\delta_W^2:=\sum_x(\phi_X(x+1)-\phi_X(x))^2=\langle4\sin^2\tfrac p2\rangle_W=O(W^{-2})`$, and $`\langle\sin^2p\rangle_W\le\delta_W^2`$. For linear profiles $`M_{x,k}=M_k+G_kx`$ with $`M_k=m+d_k`$ and $`G_k:=m\,g_m+d_k\,g_\eta`$; $`\omega_k(p)=\sqrt{M_k^2+\tau^2\sin^2p}`$ as in (5.6); $`b_1:=(\tau+M_k)\lvert g_\zeta\rvert+\lvert G_k\rvert+\lvert\mathcal F\rvert`$.
- **Inputs used** (as quoted in the question): (5.6), (5.20), (5.21), (5.22); (6.12), (6.13), (6.24), (6.14), (6.15), (6.20); (8.1), (8.19), (8.20); (9.1), (9.11), (9.12); (17.15) of 03-ilang-space/17-motion. Standard facts: Duhamel formula, Taylor's theorem, first-order perturbation theory in a term of the contract, the stationary-phase estimate for a phase with nondegenerate stationary points.
- **Orders.** Every statement is marked *exact* or *order estimate*; $`c`$ denotes a pure number that may differ from line to line. An order estimate is a bound that is rigorous up to the value of $`c`$, unless a leading term is stated explicitly.

## Derivation

### Step 1. Weak records and the long chain

Decompose $`\chi`$ over the eigenvalues $`\xi`$ of $`X`$. In the sector $`\xi`$ the body evolves with $`C_{\rm eff}+\epsilon_\xi\hat x`$, $`\epsilon_\xi=\kappa(\xi-\langle X\rangle)`$, with weights $`w_\xi`$, $`\sum_\xi w_\xi\epsilon_\xi=0`$, $`\sum_\xi w_\xi\epsilon_\xi^2=\kappa^2\sigma_X^2`$. For a body operator $`O`$, $`f(\epsilon):=\langle\phi\vert e^{i(C_{\rm eff}+\epsilon\hat x)\lambda}Oe^{-i(C_{\rm eff}+\epsilon\hat x)\lambda}\vert\phi\rangle`$ has $`\lvert f''\rvert\le(2\lambda\lVert\hat x\rVert)^2\lVert O\rVert`$ (Duhamel, twice), and $`\lVert\hat x\rVert=L`$. Taylor's theorem and the vanishing first moment give, **exactly**, on the chain $`\lvert x\rvert\le L`$, for every member of $`\mathcal C`$, every start and every $`\lambda`$,
```math
\Bigl\lvert\langle O\otimes\mathbb 1_c\rangle_{\Psi(\lambda)}-\langle\phi\vert e^{iC_{\rm eff}\lambda}Oe^{-iC_{\rm eff}\lambda}\vert\phi\rangle\Bigr\rvert\le2\,\kappa^2\sigma_X^2\,L^2\lambda^2\,\lVert O\rVert .\qquad\text{(3.3)}
```
In the weak-record regime ($`\kappa\to0`$ at fixed $`\lambda`$, chain, start and fixed $`C_{\rm eff}`$) the place weights and the clock statistics are those of $`e^{-iC_{\rm eff}\lambda}\phi`$; what is neglected is bounded by (3.3). From here on $`\kappa=0`$ unless stated.

*Finite propagation.* In the Dyson series in $`A_\zeta`$ (interaction picture of the on-site part, which is diagonal in $`x`$) each factor moves $`x`$ by one, and $`\lVert A_\zeta\rVert\le\tau\zeta_{\max}`$ on every chain, open ends included (a hopping operator with amplitudes of modulus $`\le h`$ has norm $`\le2h`$). Hence, with $`\theta:=\tau\zeta_{\max}\lambda`$,
```math
\bigl\lVert\text{part of }e^{-iC_{\rm eff}\lambda}\phi\text{ farther than }r\text{ from the support of }\phi\bigr\rVert\le e^{\theta}\,\frac{\theta^{\,r}}{r!}\qquad(\text{exact}).\qquad\text{(3.4)}
```
Two chains that agree within the distance $`r`$ of the support give evolved states that differ in norm by at most $`2e^\theta\theta^r/r!`$, and expectations of $`O`$ that differ by at most $`4\lVert O\rVert e^\theta\theta^r/r!`$. The limit $`L\to\infty`$ at fixed start and fixed $`\lambda`$ therefore exists whenever $`\sup_x\zeta_x<\infty`$; for unbounded $`\zeta_x`$ the results below hold on every finite chain and the limit is not claimed.

### Step 2. The operators (item 1)

Only $`A_\zeta=-\tfrac{i\tau}{2}(R-R^\dagger)\otimes\sigma_1`$ fails to commute with $`\hat x`$ (the record term of (3.1) and the on-site terms are diagonal in $`x`$). With $`[R_x,\hat x]=-R_x`$:
```math
\frac{\mathrm d\bar x_{\rm lab}}{\mathrm d\lambda}=\langle\hat v\otimes\mathbb 1_c\rangle,\qquad \hat v:=i[C_{\rm eff},\hat x]=-\frac\tau2\sum_x\zeta_x\bigl(R_x+R_x^\dagger\bigr)\otimes\sigma_1\otimes\mathbb 1_N .\qquad\text{(3.5)}
```
Exact for every $`\kappa`$. Next $`\hat a:=i[C_{\rm eff},\hat v]`$ has three parts: $`i[A_\zeta,\hat v]=-\tfrac{\tau^2}{2}[R,R^\dagger]`$ with $`RR^\dagger=\sum_x\zeta_{x-1}^2P_x`$, $`R^\dagger R=\sum_x\zeta_x^2P_x`$; the $`\sigma_3`$ part, by $`\sigma_3\sigma_1=i\sigma_2`$, gives an anticommutator; the plain part uses $`[P_{x'},R_x]=(\delta_{x',x+1}-\delta_{x',x})R_x`$. With $`\mathsf M_x:=m_x\mathbb 1_N+\eta_xD`$,
```math
\hat a=\frac{\tau^2}{2}\sum_x\bigl(\zeta_x^2-\zeta_{x-1}^2\bigr)P_x+\frac\tau2\sum_x\zeta_x\Bigl[(R_x+R_x^\dagger)\otimes\sigma_2\otimes(\mathsf M_x+\mathsf M_{x+1})+(V_{x+1}-V_x)\,(-iR_x+iR_x^\dagger)\otimes\sigma_1\otimes\mathbb 1_N\Bigr].\qquad\text{(3.6)}
```
On the open chain the first sum contains the end terms $`\tfrac{\tau^2}{2}(\zeta_{-L}^2P_{-L}-\zeta_{L-1}^2P_L)`$. Since $`i[\hat x,\hat v]=A_\zeta`$, the second derivative is, **exactly** for every $`\kappa`$, every member and every start,
```math
\frac{\mathrm d^2\bar x_{\rm lab}}{\mathrm d\lambda^2}=\bigl\langle\hat a\otimes\mathbb 1_c+\kappa\,A_\zeta\otimes(X-\langle X\rangle)\bigr\rangle_{\Psi(\lambda)} .\qquad\text{(3.7)}
```
The second term vanishes at $`\lambda=0`$ (product start) and is bounded in modulus by $`2\kappa^2\sigma_X^2\,\tau\zeta_{\max}L\lambda`$ (sector argument of Step 1, exact); it is neglected in the weak-record regime. For uniform profiles and $`V_x=-\mathcal Fx`$, (3.5)–(3.6) are (6.12).

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
*Recentring (exact).* With $`y=x-x_0`$ the contract has the same form about $`x_0`$, with $`(\tau,M_k,g_\zeta)\to(\tau^0,M^0_k,g^0_\zeta):=\bigl(\tau(1+g_\zeta x_0),\,M_{x_0,k},\,g_\zeta/(1+g_\zeta x_0)\bigr)`$, $`G_k`$, $`\mathcal F`$ and $`\tau^0g^0_\zeta=\tau g_\zeta`$ unchanged, plus $`V_{x_0}\mathbb 1`$. Local and original parameters differ at second order in the gradients. Note $`\tau^0=t_{x_0-1}+t_{x_0}`$.

From (3.5)–(3.6), $`\hat v=\hat v_0+\hat v_1`$ with $`\hat v_0=C_0'(\hat p)=-\tau\cos\hat p\,\sigma_1`$ and $`\hat v_1=\tfrac12\{\hat x,B'(\hat p)\}`$, and $`\hat a=\hat a_0+\hat a_1+\hat a_2`$ with $`\hat a_0=2\tau M_k\cos\hat p\,\sigma_2`$ and
```math
\hat a_1=\tau^2g_\zeta+\tfrac12\{\hat x,F_a(\hat p)\}+\mathcal F\tau\sin\hat p\,\sigma_1,\qquad F_a(p):=2\tau(M_kg_\zeta+G_k)\cos p\,\sigma_2 .
```

### Step 4. Acceleration to first order in the gradients (item 2(a))

Infinite chain, start $`S_k(x_0)`$. Let $`U_t(p):=e^{-iC_0(p)t}`$, $`\chi_t(p):=U_t\lvert1\rangle=\bigl(\cos\omega t-i\tfrac{M_k}{\omega}\sin\omega t\bigr)\lvert1\rangle+i\tfrac{\tau\sin p}{\omega}\sin\omega t\,\lvert2\rangle`$, $`\omega=\omega_k(p)`$. The zeroth-order state is $`\psi_0(\lambda)=\tilde\phi_X\chi_\lambda`$, and $`\psi_1(\lambda)=-i\int_0^\lambda\mathrm ds\,U_{\lambda-s}C_1\psi_0(s)`$ (first-order perturbation theory). For spinor functions $`u,v`$ and $`\xi:=-\partial_p\arg\tilde\phi_X`$ (that is, $`\xi\lvert\tilde\phi_X\rvert^2:=\mathrm{Re}[\tilde\phi_X^{*}\,i\partial_p\tilde\phi_X]`$), an integration by parts gives the identity
```math
\bigl\langle\tilde\phi_Xu\bigm\vert\tfrac12\{\hat x,F(\hat p)\}\bigm\vert\tilde\phi_Xv\bigr\rangle=\Bigl\langle\xi\,u^\dagger Fv+\tfrac i2\bigl[u^\dagger F\,\partial_pv-(\partial_pu^\dagger)Fv\bigr]\Bigr\rangle_W.
```
*Parity.* $`C_0(-p)=\sigma_3C_0(p)\sigma_3`$, $`B(-p)=\sigma_3B(p)\sigma_3`$, $`\chi_t(-p)=\sigma_3\chi_t(p)`$, $`\sigma_3\sigma_2\sigma_3=-\sigma_2`$, and $`\phi_X`$ real makes $`\lvert\tilde\phi_X\rvert^2`$ and $`\xi`$ even. Consequences, all exact: the zeroth-order acceleration $`\langle\psi_0\vert\hat a_0\vert\psi_0\rangle`$ vanishes for all $`\lambda`$; every term with $`\xi`$ (which carries $`x_0`$ and any asymmetry of $`w`$) has an odd coefficient and integrates to zero. With $`u_s^\dagger:=\chi_\lambda^\dagger\,\hat a_0(p)\,U_{\lambda-s}`$, the first-order coefficient $`a^{(1)}=\langle\psi_0\vert\hat a_1\vert\psi_0\rangle+2\mathrm{Re}\langle\psi_0\vert\hat a_0\vert\psi_1\rangle`$ is, **exactly** (first Taylor coefficient, infinite chain, every real $`\phi_X`$, every $`x_0`$),
```math
a^{(1)}(\lambda)=\bigl\langle\alpha(p,\lambda)\bigr\rangle_W,\quad
\alpha:=\tau^2g_\zeta+\mathcal F\tau\sin p\,\chi_\lambda^\dagger\sigma_1\chi_\lambda-\mathrm{Im}\bigl[\chi_\lambda^\dagger F_a\partial_p\chi_\lambda\bigr]+\int_0^\lambda\!\mathrm ds\mathrm{Re}\bigl[u_s^\dagger B\,\partial_p\chi_s-(\partial_pu_s^\dagger)B\chi_s\bigr],\qquad\text{(3.10)}
```
with $`\alpha`$ smooth and even in $`p`$ and independent of $`x_0`$. This is the acceleration of item 2(a) for the named start at finite $`W`$; it is written $`a^{(1)}_W`$ where the width matters.

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
This is the limit of a wide start at fixed $`\lambda`$. The third term grows with $`\lambda`$: on the level $`k`$ the two branch components move in opposite directions in $`p`$ under $`G_k\hat x\sigma_3`$, so the oscillation between the branches has an amplitude proportional to $`\lambda`$.

*What the limits require.* With $`p^2\le\tfrac{\pi^2}{4}\,4\sin^2\tfrac p2`$ and the evenness of $`\alpha`$,
```math
\bigl\lvert a^{(1)}_W(\lambda)-a^{(1)}_\infty(\lambda)\bigr\rvert\le\frac{\pi^2}{8}\,\delta_W^2\,\sup_p\lvert\partial_p^2\alpha\rvert\ \ (\text{exact}),\qquad \sup_p\lvert\partial_p^2\alpha\rvert\le c\,\tau\,b_1\,(1+M_k\lambda)(1+\tau\lambda)^3\ \ (\text{order estimate}),\qquad\text{(3.12)}
```
for all $`\lambda\ge0`$ (each $`\partial_p`$ of $`U_t`$ costs at most a factor $`c(1+\tau t)`$, by Duhamel; no norm of an operator on the chain enters). Requirements:
- $`L`$: on the open chain $`\lvert x\rvert\le L`$ with $`r:=L-\lvert x_0\rvert-W>0`$, the zeroth-order coefficient is not zero but at most $`c\,\tau(\tau+M_k)\,e^{\tau\lambda}(\tau\lambda)^r/r!`$ in modulus, and the first-order coefficient differs from (3.10) by at most $`c\,\tau\,b_1L\,\bigl(1+(\tau+M_k)\lambda\bigr)\,e^{\tau\lambda}(\tau\lambda)^r/r!`$ (order estimates, from (3.4) with $`\lVert\hat a_0\rVert\le2\tau(\tau+M_k)`$ and $`\lVert\hat a_1\rVert\le4\tau b_1L`$, both valid with the end terms of (3.6); see Step 5). The limit is $`r\to\infty`$ at fixed $`\lambda`$; the corrections are negligible once $`r\gg e\,\tau\lambda`$.
- $`x_0`$: nothing on the infinite chain ((3.10) does not depend on $`x_0`$).
- $`W`$: $`W\to\infty`$ at fixed $`\lambda`$; by (3.12) the absolute error is at most $`c\,\delta_W^2\,\tau b_1(1+M_k\lambda_{\max})(1+\tau\lambda_{\max})^3`$ on $`[0,\lambda_{\max}]`$ (sufficient, order estimate).
- $`\lambda`$: fixed. None of the limits is uniform in $`\lambda`$; Step 5 shows that the wide-start form fails for $`\lambda\gtrsim\lambda_W:=M_kW^2/\tau^2`$.

In the background (17.15) the acceleration is $`\kappa\,a^{(1)}\,e`$.

### Step 5. Window averages (item 2(b))

For the window $`[\lambda_1,T]`$, $`T=\lambda_1+\Lambda`$, the average of an acceleration is $`\overline a=(v(T)-v(\lambda_1))/\Lambda`$ (exact). The first-order velocity of the named start is $`v^{(1)}_W(\lambda)=\langle\nu(p,\lambda)\rangle_W`$ with $`\nu:=\int_0^\lambda\alpha(p,s)\,\mathrm ds`$ ((3.10) and $`v(0)=0`$ by (3.8)).

**5.1 Finite $`W`$: structure of $`\nu`$.** Level $`k`$, infinite chain, $`\omega=\omega_k(p)`$. Let $`P_\pm(p)`$ project on the eigenvectors $`\beta_{k,\pm}`$ of $`C_0(p)`$ (5.6), $`\Sigma:=P_+-P_-`$, so $`C_0=\omega\Sigma`$. For a matrix function $`O(p)`$ write $`O_{\rm d}:=\sum_\sigma P_\sigma OP_\sigma`$, $`O_{\rm o}:=O-O_{\rm d}`$, $`O^I(s):=e^{iC_0s}Oe^{-iC_0s}=O_{\rm d}+(P_+OP_-e^{2i\omega s}+\text{h.c.})`$. Facts, from (5.6) (the eigenvectors are real, $`\beta_\pm'=\pm\tfrac{\theta'}2\beta_\mp`$, $`\cos\theta=M_k/\omega`$, $`\sin\theta=-\tau\sin p/\omega`$):
- $`\Sigma'=\theta'\bigl(\lvert\beta_-\rangle\langle\beta_+\rvert+\lvert\beta_+\rangle\langle\beta_-\rvert\bigr)`$ is off-diagonal, and $`V:=\hat v_0^I(\lambda)=\omega'\Sigma+\omega(\Sigma')^I(\lambda)`$;
- $`\hat x^I(s)=\hat x+X(s)`$, $`X(s)=\int_0^s\hat v_0^I=s\,\omega'\Sigma+X_{\rm o}(s)`$, where $`X_{\rm o}`$ is bounded and off-diagonal, with the $`s`$-independent part $`\tfrac i2\Sigma\Sigma'`$;
- $`b_\sigma:=\langle\beta_\sigma\vert B\vert\beta_\sigma\rangle=\sigma h-\mathcal F`$ with $`h(p):=(g_\zeta\tau^2\sin^2p+G_kM_k)/\omega`$; $`b_{\rm o}:=\langle\beta_+\vert B\vert\beta_-\rangle`$; $`b_\sigma'=(B')_{\sigma\sigma}+\sigma\theta'b_{\rm o}`$; $`\{\Sigma',B_{\rm o}\}=2\theta'b_{\rm o}\mathbb 1`$.

First-order perturbation theory for the Heisenberg velocity gives $`\hat v^{(1)}(\lambda)=\hat v_1^I(\lambda)+i\int_0^\lambda\mathrm ds\,[C_1^I(s),V]`$, with $`\hat v_1^I=\tfrac12\{\hat x+X(\lambda),(B')^I(\lambda)\}`$ and $`C_1^I(s)=\tfrac12\{\hat x+X(s),B^I(s)\}`$. With $`[\hat x,f(\hat p)]=if'(\hat p)`$,
```math
\hat v^{(1)}(\lambda)=\tfrac12\{\hat x,Y\}+\mathcal N,\qquad\mathcal N:=\tfrac12\bigl\{X(\lambda),(B')^I(\lambda)\bigr\}-\tfrac12\Bigl\{\partial_pV,\int_0^\lambda\!B^I\Bigr\}+i\int_0^\lambda\!\mathrm ds\,\bigl[\tfrac12\{X(s),B^I(s)\},V\bigr],
```
where $`Y:=(B')^I(\lambda)+i\int_0^\lambda[B^I(s),V]\,\mathrm ds`$ obeys $`Y(-p)=-\sigma_3Y(p)\sigma_3`$. In the start $`\tilde\phi_X\lvert1\rangle`$ the first term gives $`\langle\xi\,Y_{11}\rangle_W=0`$ (parity, as in Step 4), so $`\nu=\mathcal N_{11}`$ (exact). The terms of $`\mathcal N`$ that are linear in $`\lambda`$ and do not oscillate are:
- from the first anticommutator: $`\lambda\,\omega'\Sigma(B')_{\rm d}`$ (the off-diagonal part of $`(B')^I`$ anticommutes with $`\Sigma`$);
- from the second: $`-\lambda\,\omega''\Sigma B_{\rm d}-\tfrac{\lambda\omega'}2\{\Sigma',B_{\rm d}\}`$, and $`+\tfrac{\lambda\omega'}2\{\Sigma',B_{\rm o}\}`$ from the product of the term $`2i\lambda\omega'\omega P_+\Sigma'P_-e^{2i\omega\lambda}+\text{h.c.}`$ of $`\partial_pV`$ with the oscillating part $`P_+BP_-(e^{2i\omega\lambda}-1)/(2i\omega)+\text{h.c.}`$ of $`\int_0^\lambda B^I`$;
- from the commutator: $`i\lambda\omega'\bigl[\tfrac12\{\tfrac i2\Sigma\Sigma',B_{\rm d}\},\Sigma\bigr]=+\tfrac{\lambda\omega'}2\{\Sigma',B_{\rm d}\}`$.

Their sum is $`\lambda\sum_\sigma P_\sigma a_\sigma`$ with $`a_\sigma=\sigma(\omega'b_\sigma'-\omega''b_\sigma)=\omega'h'-\omega''h+\sigma\mathcal F\omega''`$. Every other term of $`\mathcal N`$ is bounded in $`\lambda`$, or is $`\lambda^j`$ ($`j\le2`$) times $`e^{\pm2i\omega\lambda}`$. The $`j=2`$ terms come from $`s\,\omega'\Sigma`$ and $`2i\lambda\omega'\omega(\dots)`$ multiplied by $`B_{\rm d}=h\Sigma-\mathcal F`$; the part $`h\Sigma`$ drops out ($`\{\Sigma,\Sigma\}`$ is a multiple of $`\mathbb 1`$ and commutes, and off-diagonal terms anticommute with $`\Sigma`$), so they carry the factor $`\mathcal F`$ only. Their sum is $`\mathcal F\tfrac{\lambda^2}{2}\,\omega\omega'\,\langle1\vert(-i)[(\Sigma')^I(\lambda),\Sigma]\vert1\rangle=\mathcal F\lambda^2\,\omega\omega'\,\theta'\sin\theta\,\sin(2\omega\lambda)`$, and $`\theta'\sin\theta=M_k\omega'/\omega^2`$. With $`\langle1\vert P_\pm\vert1\rangle=\tfrac12(1\pm M_k/\omega)`$ and $`(\omega^2)''=2\tau^2\cos2p`$, **exactly**,
```math
\nu(p,\lambda)=a_{\rm sec}(p)\,\lambda+\nu_0(p)+\mathrm{Re}\sum_{j=0}^{2}\lambda^jA_j(p)\,e^{2i\omega_k(p)\lambda},\qquad a_{\rm sec}(p)=\frac{g_\zeta\tau^4\sin^2p-G_k\tau^2M_k\cos2p}{\omega_k^2}+\mathcal F\,\frac{\tau^2M_k\bigl(M_k^2\cos2p-\tau^2\sin^4p\bigr)}{\omega_k^4},\qquad\text{(3.26)}
```
with $`\nu_0`$, $`A_j`$ smooth, $`2\pi`$-periodic and linear in the gradients, and
```math
A_2(p)=-i\,\mathcal F\,\frac{M_k}{\omega_k(p)}\,\omega_k'(p)^2,\qquad\text{that is}\qquad\mathrm{Re}\bigl[\lambda^2A_2e^{2i\omega_k\lambda}\bigr]=\mathcal F\,\frac{M_k}{\omega_k}\,\omega_k'^{\,2}\,\lambda^2\sin(2\omega_k\lambda)
```
(the form $`A_2=\mathcal F\omega_k'\tilde A_2`$ of v2, with $`\tilde A_2=-iM_k\omega_k'/\omega_k`$). At $`p=0`$: $`a_{\rm sec}(0)=\tfrac{\tau^2}{M_k}(\mathcal F-G_k)`$, $`A_2(0)=0`$, $`A_1(0)=\tau^2G_k/M_k`$, $`A_0(0)=-\tfrac{i\tau^2}{2M_k^2}(M_kg_\zeta-\mathcal F)`$, read off from (3.13). The amplitudes $`\nu_0`$, $`A_0`$, $`A_1`$ are not given in closed form for $`p\neq0`$.

**5.2 Finite $`W`$: the long window.** The stationary points of $`\omega_k`$ are $`p\in\{0,\pm\tfrac\pi2,\pi\}`$, with $`\omega_k''=\pm\tau^2/\omega_k\neq0`$ there. For smooth periodic $`f`$, $`\int f\,e^{2i\omega_k\lambda}\mathrm dp=O(\lambda^{-1/2})`$ (stationary phase); for $`j=2`$, $`\lambda^2\omega_k'e^{2i\omega_k\lambda}=\tfrac{\lambda}{2i}\partial_pe^{2i\omega_k\lambda}`$ and one integration by parts reduce the term to $`\lambda\,O(\lambda^{-1/2})`$. Hence $`v^{(1)}_W(\lambda)=\bar a_W\lambda+O_W(\lambda)`$ with $`\lvert O_W(\lambda)\rvert\le c_W(1+\lambda)^{1/2}`$ for all $`\lambda\ge0`$; $`c_W`$ depends on the start and the parameters and is linear in the gradients. Therefore, for every finite $`W`$ and every $`\lambda_1`$, the limit exists (**exact**) and
```math
\lim_{\Lambda\to\infty}\overline{a^{(1)}_W}=\bar a_W:=\langle a_{\rm sec}(p)\rangle_W=g_\zeta\,\tau^4s_W-\frac{\tau^2G_k}{M_k}\Bigl[1-(2M_k^2+\tau^2)\,s_W\Bigr]+\frac{\tau^2\mathcal F}{M_k}\,f_W,\qquad\text{(3.27)}
```
```math
s_W:=\Bigl\langle\frac{\sin^2p}{\omega_k^2}\Bigr\rangle_W,\quad f_W:=\Bigl\langle\frac{M_k^2(M_k^2\cos2p-\tau^2\sin^4p)}{\omega_k^4}\Bigr\rangle_W;\qquad0<s_W\le\frac{\delta_W^2}{M_k^2},\quad0\le1-f_W\le2(M_k^2+\tau^2)\,s_W\quad(\text{exact}),
```
the last from $`1-f(p)=\sin^2p\,(M_k^2+\tau^2)(2M_k^2+\tau^2\sin^2p)/\omega_k^4`$. At finite window, $`\overline{a^{(1)}_W}=\bar a_W+[O_W(T)-O_W(\lambda_1)]/\Lambda`$ (exact), and the deviation from $`\bar a_W`$ is at most $`2c_W(1+T)^{1/2}/\Lambda`$ (order estimate). *Coefficients in the long-window limit at finite $`W`$:* of $`g_\zeta`$: $`\tau^4s_W`$; of $`g_m`$: $`-\tfrac{\tau^2m}{M_k}[1-(2M_k^2+\tau^2)s_W]`$; of $`g_\eta`$: the same with $`m\to d_k`$; of $`\mathcal F`$: $`\tfrac{\tau^2}{M_k}f_W`$.

*The oscillating part $`O_W`$ at late $`\lambda`$, for every gradient.* The weight $`\lvert\tilde\phi_X\rvert^2`$ has the width $`1/W`$ in $`p`$, and $`2\omega_k\lambda\simeq2M_k\lambda+\tau^2p^2\lambda/M_k`$ near $`p=0`$.
- *$`\lambda\ll\lambda_W`$.* The $`G_k`$ part keeps its wide-start form $`\tfrac{\tau^2G_k}{M_k}\lambda\cos(2M_k\lambda)`$ of (3.13), up to a fraction $`c\,\lambda/\lambda_W`$ (order estimate). The plain gradient has, in addition to the bounded term of (3.13), the $`j=2`$ term, with $`\bigl\lvert\lambda^2\langle\mathrm{Re}A_2e^{2i\omega_k\lambda}\rangle_W\bigr\rvert\le\lvert\mathcal F\rvert\,\tau^4\delta_W^2\lambda^2/M_k^2`$ (exact, from $`\omega_k'^{\,2}\le\tau^4\sin^2p/M_k^2`$): a fraction $`c\,\lambda/\lambda_W`$ of the secular term $`\tfrac{\tau^2\lvert\mathcal F\rvert}{M_k}\lambda`$, which can exceed the bounded oscillation $`\tfrac{\tau^2\lvert\mathcal F\rvert}{2M_k^2}`$ of (3.13) once $`\lambda\gtrsim W/\tau`$.
- *$`\lambda\gg\max(\lambda_W,1/M_k)`$* (order estimates: leading stationary-phase terms of the point $`p=0`$, with $`\int\mathrm dp\,e^{iap^2}=(\pi/a)^{1/2}e^{i\pi/4}`$, $`\int\mathrm dp\,p^2e^{iap^2}=\tfrac{\sqrt\pi}{2}a^{-3/2}e^{3i\pi/4}`$, $`a=\tau^2\lambda/M_k`$, and $`\lvert\tilde\phi_X(0)\rvert^2=(\sum_x\phi_X(x))^2=:c_0W`$, $`c_0\le2`$):
```math
O_W(\lambda)\simeq\frac{c_0}{2\sqrt\pi}\,\frac{\tau^2G_k}{M_k}\,(\lambda_W\lambda)^{1/2}\cos\bigl(2M_k\lambda+\tfrac\pi4\bigr)+\frac{c_0}{4\sqrt\pi}\,\frac{\tau^2\mathcal F}{M_k}\,(\lambda_W\lambda)^{1/2}\sin\bigl(2M_k\lambda+\tfrac{3\pi}4\bigr)+O\Bigl(\frac{\tau^2b_1}{M_k}\Bigl(\frac{\lambda_W}{\lambda}\Bigr)^{1/2}\Bigr),
```
the first term from $`A_1(0)=\tau^2G_k/M_k`$, the second from $`A_2\simeq-i\mathcal F\tau^4p^2/M_k^2`$. The oscillating part of the plain gradient therefore grows as $`\lambda^{1/2}`$, with the same order as that of $`G_k`$; setting $`G_k=0`$ does not remove the growth. Only the bond gradient has a decaying oscillating part, of the order $`\tfrac{\tau^2\lvert g_\zeta\rvert}{M_k}(\lambda_W/\lambda)^{1/2}`$ times a number that depends on $`\tau/M_k`$ and $`w`$ (it comes from $`A_0(0)`$ and from the curvature of $`A_1`$ at $`p=0`$, which is not computed). The stationary points $`\pm\tfrac\pi2`$, $`\pi`$ add terms with the same powers of $`\lambda`$ and the weights $`\lvert\tilde\phi_X(\pm\tfrac\pi2)\rvert^2`$, $`\lvert\tilde\phi_X(\pi)\rvert^2`$, which are smaller than any power of $`1/W`$ for smooth $`w`$.
- *Consequence.* For every gradient the deviation $`[O_W(T)-O_W(\lambda_1)]/\Lambda`$ of the window average from $`\bar a_W`$ is of the order $`\tfrac{\tau^2(\lvert G_k\rvert+\lvert\mathcal F\rvert)}{M_k}(\lambda_WT)^{1/2}/\Lambda`$ for $`T\gg\lambda_W`$; the limit (3.27) is reached for $`\Lambda\gg\lambda_W`$ (at fixed $`\lambda_1`$), and the remainder stays sublinear, as used above.

**5.3 Wide start first.** Integrating (3.11) with $`v(0)=0`$ (exact consequences of (3.11)):
```math
v^{(1)}_\infty(\lambda)=\frac{\tau^2}{M_k}(\mathcal F-G_k)\,\lambda+\frac{\tau^2G_k}{M_k}\,\lambda\cos(2M_k\lambda)+\frac{\tau^2}{2M_k^2}\,(M_kg_\zeta-\mathcal F)\sin(2M_k\lambda).\qquad\text{(3.13)}
```
With $`\rho`$ of (6.24) and $`\varsigma:=\bigl(T\cos(2M_kT)-\lambda_1\cos(2M_k\lambda_1)\bigr)/\Lambda`$, exactly for every window,
```math
\overline{a^{(1)}_\infty}=\frac{\tau^2}{M_k}\Bigl[(\mathcal F-G_k)+G_k\,\varsigma+(M_kg_\zeta-\mathcal F)\,\rho\Bigr],\qquad\lvert\rho\rvert\le\frac1{M_k\Lambda},\qquad\varsigma=\cos(2M_kT)+\frac{\lambda_1}{\Lambda}\bigl[\cos(2M_kT)-\cos(2M_k\lambda_1)\bigr].\qquad\text{(3.14)}
```
By (3.12), $`\overline{a^{(1)}_\infty}=\lim_{W\to\infty}\overline{a^{(1)}_W}`$ at a fixed window. *Coefficients for a long window* ($`\Lambda\to\infty`$ at fixed $`\lambda_1`$):
- of $`\mathcal F`$: $`\tfrac{\tau^2}{M_k}(1-\rho)\to\tfrac{\tau^2}{M_k}`$ (absolute error $`\le\tau^2/(M_k^2\Lambda)`$);
- of $`g_\zeta`$: $`\tau^2\rho\to0`$ (absolute error $`\le\tau^2/(M_k\Lambda)`$);
- of $`g_m`$ and $`g_\eta`$: $`-\tfrac{\tau^2m}{M_k}(1-\varsigma)`$ and $`-\tfrac{\tau^2d_k}{M_k}(1-\varsigma)`$. **These have no limit:** $`1-\varsigma=2\sin^2(M_kT)+O(\lambda_1/\Lambda)`$ takes every value in $`[0,2]`$ however long the window is. Example: over $`[0,n\pi/M_k]`$ the $`G_k`$ part of the average is exactly $`0`$; over $`[\tfrac{\pi}{2M_k},\tfrac{\pi}{2M_k}+\tfrac{n\pi}{M_k}]`$ it is $`-2\tau^2G_k/M_k`$.

**5.4 The two orders of the limits.** From (3.27) and the exact bounds on $`s_W`$, $`f_W`$ (with $`\lvert g_\zeta\rvert\tau^4/M_k^2\le\tfrac{\tau^2}{M_k}(1+\tfrac{\tau^2}{M_k^2})M_k\lvert g_\zeta\rvert`$), and from 5.3:
```math
\bigl\lvert\bar a_W-a_{\rm sec}\bigr\rvert\le2\,\delta_W^2\,\frac{\tau^2}{M_k}\Bigl(1+\frac{\tau^2}{M_k^2}\Bigr)b_1\ \ (\text{exact}),\qquad\lim_{W\to\infty}\lim_{\Lambda\to\infty}\overline{a^{(1)}_W}=a_{\rm sec},\qquad\lim_{\Lambda\to\infty}\lim_{W\to\infty}\overline{a^{(1)}_W}\ \text{does not exist if }G_k\neq0 .\qquad\text{(3.28)}
```
The limits **do not commute** when $`G_k\neq0`$. They commute for the coefficients of $`\mathcal F`$ and $`g_\zeta`$ (both orders give $`\tau^2/M_k`$ and $`0`$). Here $`a_{\rm sec}`$ is the **secular acceleration**, an additional result, defined by the displacement obtained from (3.13):
```math
\bar x^{(1)}_{\rm lab}(\lambda)-\bar x_{\rm lab}(0)=\tfrac12\,a_{\rm sec}\,\lambda^2+\frac{\tau^2G_k}{2M_k^2}\,\lambda\sin(2M_k\lambda)+\frac{\tau^2}{2M_k^3}\bigl(M_kg_\zeta-\mathcal F-G_k\bigr)\sin^2(M_k\lambda),\qquad\boxed{\;a_{\rm sec}:=\frac{\tau^2}{M_k}\bigl(\mathcal F-G_k\bigr)\;}\qquad\text{(3.15)}
```
It is not the window average of item 2(b); its relation to it is (3.28). It is also the long-window limit of the doubly averaged wide-start acceleration $`\tfrac{2}{\Lambda^2}\int_0^\Lambda(\Lambda-\lambda)a^{(1)}_\infty\,\mathrm d\lambda`$, with the absolute error (exact, from (3.15))
```math
\Bigl\lvert\frac{2\bigl[\bar x^{(1)}_{\rm lab}(\Lambda)-\bar x_{\rm lab}(0)\bigr]}{\Lambda^2}-a_{\rm sec}\Bigr\rvert\le\frac{\tau^2\lvert G_k\rvert}{M_k^2\,\Lambda}+\frac{\tau^2\lvert M_kg_\zeta-\mathcal F-G_k\rvert}{M_k^3\,\Lambda^2}.\qquad\text{(3.32)}
```
A relative error $`\le\varrho^{-1}\bigl[(M_k\Lambda)^{-1}+(M_k\Lambda)^{-2}\bigr]`$ follows only under the condition $`\lvert\mathcal F-G_k\rvert\ge\varrho\,\max(\lvert G_k\rvert,\lvert M_kg_\zeta-\mathcal F-G_k\rvert)`$ with some $`\varrho>0`$.

**5.5 Range of validity of the first-order treatment.** (3.10), (3.11), (3.13)–(3.15), (3.26)–(3.28) are exact statements about the first Taylor coefficient on the infinite chain. *Remainder (exact).* Take any chain, open ends included, all of whose positions lie within $`\ell`$ of the expansion point (the position $`0`$ with the parameters $`\tau`$, $`M_k`$, or $`x_0`$ with the local parameters of Step 3), and scale the gradients by a common $`\varepsilon\in[0,1]`$: $`C=C_0+\varepsilon C_1`$, $`\hat v=\hat v_0+\varepsilon\hat v_1`$, $`\hat a=\hat a_0+\varepsilon\hat a_1+\varepsilon^2\hat a_2`$ with $`\hat a_0=i[C_0,\hat v_0]`$, $`\hat a_1=i[C_0,\hat v_1]+i[C_1,\hat v_0]`$, $`\hat a_2=i[C_1,\hat v_1]`$. On this chain, with $`\Omega_k:=\tau+M_k`$: $`\lVert C_0\rVert\le\Omega_k`$, $`\lVert\hat v_0\rVert\le\tau`$, $`\lVert C_1\rVert\le\ell\,(\lvert G_k\rvert+\lvert\mathcal F\rvert+\tau\lvert g_\zeta\rvert)\le\ell b_1`$, $`\lVert\hat v_1\rVert\le\tau\lvert g_\zeta\rvert\ell`$, hence
```math
\lVert\hat a_0\rVert\le2\tau\Omega_k,\qquad\lVert\hat a_1\rVert\le4\tau\,b_1\ell,\qquad\lVert\hat a_2\rVert\le2\tau\,(b_1\ell)^2/\Omega_k .
```
These follow from the commutators, so the end terms of (3.6) are included ($`\lVert\hat a_0\rVert\ge\tau^2/2`$ on the open chain is consistent with $`2\tau\Omega_k`$). For $`f(\varepsilon)=\langle\phi\vert U_\varepsilon^\dagger\hat aU_\varepsilon\vert\phi\rangle`$, Duhamel's formula gives $`\lVert\partial_\varepsilon^jU_\varepsilon\rVert\le(\lambda\lVert C_1\rVert)^j`$, so $`\lvert f''\rvert\le4(\lambda b_1\ell)^2\lVert\hat a\rVert+4\lambda b_1\ell\,\lVert\partial_\varepsilon\hat a\rVert+2\lVert\hat a_2\rVert`$. If $`b_1\ell\le\Omega_k`$, then $`\lVert\hat a\rVert\le8\tau\Omega_k`$ and $`\lVert\partial_\varepsilon\hat a\rVert\le8\tau b_1\ell`$, and Taylor's theorem gives, for every start on the chain, all $`\lambda\ge0`$ and $`\kappa=0`$,
```math
\bigl\lvert a(\lambda)-a^{(0)}_\ell(\lambda)-a^{(1)}_\ell(\lambda)\bigr\rvert\le16\,\tau\,(\tau+M_k)\,\Bigl[b_1\,\ell\,\bigl(\lambda+(\tau+M_k)^{-1}\bigr)\Bigr]^2\qquad\bigl(b_1\ell\le\tau+M_k\bigr),\qquad\text{(3.16)}
```
where $`a^{(0)}_\ell`$, $`a^{(1)}_\ell`$ are the Taylor coefficients on that chain. *Order estimates.* On the long chain, apply (3.16) to the sub-chain within $`\ell=W+r`$ of $`x_0`$; by (3.4) this costs at most $`c\,\tau(\tau+M_k+\lvert\mathcal F\rvert)\,e^{\theta}\theta^r/r!`$ in $`a(\lambda)`$, and $`a^{(0)}_\ell`$, $`a^{(1)}_\ell`$ differ from $`0`$ and (3.10) by the edge terms of Step 4. The first-order treatment therefore has an absolute error below a fraction $`\epsilon_{\rm tol}`$ of the scale $`\tau^2b_1/M_k`$ of (3.11) if $`16\,b_1\ell^2\bigl(1+(\tau+M_k)\lambda\bigr)^2\le\epsilon_{\rm tol}\,\tau`$ and $`r\gg e\,\tau\lambda`$. This is a sufficient condition; it is not shown to be necessary. For the long window of 5.2 it has to hold up to $`\lambda=T\gg\lambda_W`$, which it does for small enough gradients at fixed $`W`$ and $`T`$ (the order of limits of the question); otherwise only the regime $`T\ll\lambda_W`$ of (3.14) lies inside the range. For variant (d) the quoted (6.14) gives the range $`\mathcal F_{\max}T\ll\min(1,M_k/\tau)`$.

### Step 6. Well-defined form, variants, other branch (items 2(c)–(e))

*(c).* With (3.2) at $`x_0`$ (to first order in the gradients every position of the chain gives the same result): $`\tau=2t`$, $`M_k=\tfrac12\Delta_k`$, $`G_k=\tfrac12\delta\Delta_k=\tfrac12(\delta E^+_k-\delta E^-_k)`$, $`\mathcal F=-\tfrac12(\delta E^+_k+\delta E^-_k)`$, $`g_\zeta=\delta t/t`$, $`\omega_k^2=\tfrac14\Delta_k^2+4t^2\sin^2p`$. The averaged acceleration of item 2(b) for the start $`S_k`$, at finite $`W`$ in the long-window limit, is
```math
\bar a_W=16\,t^3\,\delta t\;s_W-\frac{4t^2}{\Delta_k}\,\delta\Delta_k\Bigl[1-\bigl(\tfrac12\Delta_k^2+4t^2\bigr)s_W\Bigr]-\frac{4t^2}{\Delta_k}\bigl(\delta E^+_k+\delta E^-_k\bigr)f_W ,\qquad\text{(3.29)}
```
where $`s_W`$, $`f_W`$ are functions of $`\Delta_k`$, $`t`$ and the place amplitudes $`\phi_X`$ of the start only. With the wide start first (3.14), and in the limit $`W\to\infty`$ of (3.29) (additional result),
```math
\overline{a^{(1)}_\infty}=\frac{8t^2}{\Delta_k}\Bigl[-\delta E^+_k+\tfrac12\,\delta\Delta_k\,\varsigma+\Bigl(\tfrac{\Delta_k}{2}\tfrac{\delta t}{t}+\tfrac12(\delta E^+_k+\delta E^-_k)\Bigr)\rho\Bigr],\qquad a_{\rm sec}=\lim_{W\to\infty}\bar a_W=-\frac{8t^2}{\Delta_k}\,\delta E^+_k ,\qquad\text{(3.17)}
```
where $`\rho,\varsigma`$ depend on the contract through $`\Delta_k`$ only. Only gaps, norms of hopping blocks and differences of on-site eigenvalues between neighbouring positions occur; no single cost occurs, so all three expressions are invariant under (8.1), place-dependent replacements included.

*(e), other branch.* Conjugation with $`\sigma_1`$ leaves $`A_\zeta`$, $`\hat v`$, $`V_x`$, $`g_\zeta`$, $`\mathcal F`$ unchanged and maps $`\lvert2\rangle\to\lvert1\rangle`$, $`(M_k,G_k)\to(-M_k,-G_k)`$; Steps 4 and 5 hold for either sign of $`M_k`$, and $`s_W`$, $`f_W`$ are even in $`M_k`$. Under this map only the $`\mathcal F`$ term of (3.26) changes sign. For $`S'_k(x_0)`$ at finite $`W`$, long window:
```math
\bar a'_W=g_\zeta\,\tau^4s_W-\frac{\tau^2G_k}{M_k}\Bigl[1-(2M_k^2+\tau^2)\,s_W\Bigr]-\frac{\tau^2\mathcal F}{M_k}\,f_W ,\qquad\text{(3.30)}
```
with the bound and the non-commutation of (3.28) unchanged ($`a_{\rm sec}\to a'_{\rm sec}`$). With the wide start first, and the limit $`W\to\infty`$ of (3.30) (additional result):
```math
a'^{(1)}_\infty=\tau^2g_\zeta\cos(2M_k\lambda)-\frac{2\tau^2}{M_k}(\mathcal F+G_k)\sin^2(M_k\lambda)-2\tau^2G_k\lambda\sin(2M_k\lambda),\qquad a'_{\rm sec}=-\frac{\tau^2}{M_k}(\mathcal F+G_k)=+\frac{8t^2}{\Delta_k}\,\delta E^-_k,\qquad\text{(3.18)}
```
and $`\overline{a'^{(1)}_\infty}=a'_{\rm sec}+\tfrac{\tau^2}{M_k}[G_k\varsigma+(M_kg_\zeta+\mathcal F)\rho]`$.

*(d), variants.* Let $`u_W:=(2M_k^2+\tau^2)s_W`$ and $`u^{\rm c}_W:=2(M_k^2+\tau^2)s_W`$; exactly, $`0<u_W\le(2+\tfrac{\tau^2}{M_k^2})\delta_W^2`$ and $`0<u^{\rm c}_W\le2(1+\tfrac{\tau^2}{M_k^2})\delta_W^2`$. From (3.27), for the start $`S_k`$ at finite $`W`$ in the long-window limit,
```math
\bar a_W:\quad\text{(a)}\ -g\tau^2(1-u_W),\quad\text{(b1)}\ -g\tau^2\tfrac{m}{M_k}(1-u_W),\quad\text{(b2)}\ -g\tau^2\tfrac{d_k}{M_k}(1-u_W),\quad\text{(c)}\ -g\tau^2(1-u^{\rm c}_W),\quad\text{(d)}\ \tfrac{\tau^2\mathcal F}{M_k}f_W ,\qquad\text{(3.31)}
```
and their limits $`W\to\infty`$ (additional result, $`M_k=m+d_k`$, $`d_k=2\pi k/(N\lambda_0)`$):
```math
a_{\rm sec}:\quad\text{(a)}\ -g\tau^2,\qquad\text{(b1)}\ -g\tau^2\frac{m}{m+d_k},\qquad\text{(b2)}\ -g\tau^2\frac{d_k}{m+d_k},\qquad\text{(c)}\ -g\tau^2,\qquad\text{(d)}\ \frac{\tau^2\mathcal F}{m+d_k}.\qquad\text{(3.19)}
```

**Table 6.1: the window average of item 2(b), start $`S_k`$ and start $`S'_k`$.**

| Variant | finite $`W`$, $`\Lambda\to\infty`$: $`\bar a_W`$ ($`S_k`$) | $`\bar a'_W`$ ($`S'_k`$) | wide start first, window $`[\lambda_1,T]`$ ($`S_k`$) | the same for $`S'_k`$ | $`\Lambda\to\infty`$ after $`W\to\infty`$ |
| --- | --- | --- | --- | --- | --- |
| (a) | $`-g\tau^2(1-u_W)`$ | equal to $`\bar a_W`$ | $`-g\tau^2(1-\varsigma)`$ | equal | no limit |
| (b1) | $`-g\tau^2\frac{m}{M_k}(1-u_W)`$ | equal to $`\bar a_W`$ | $`-g\tau^2\frac{m}{M_k}(1-\varsigma)`$ | equal | no limit |
| (b2) | $`-g\tau^2\frac{d_k}{M_k}(1-u_W)`$ | equal to $`\bar a_W`$ | $`-g\tau^2\frac{d_k}{M_k}(1-\varsigma)`$ | equal | no limit for $`k\ge1`$; $`0`$ for $`k=0`$ |
| (c) | $`-g\tau^2(1-u^{\rm c}_W)`$ | equal to $`\bar a_W`$ | $`-g\tau^2(1-\varsigma-\rho)`$ | equal | no limit |
| (d) | $`\frac{\tau^2\mathcal F}{M_k}f_W`$ | $`-\frac{\tau^2\mathcal F}{M_k}f_W`$ | $`\frac{\tau^2\mathcal F}{M_k}(1-\rho)`$ | $`-\frac{\tau^2\mathcal F}{M_k}(1-\rho)`$ | $`\pm\frac{\tau^2\mathcal F}{M_k}`$ |

**Table 6.2: dependence of the window average on the body (start $`S_k`$; the answers for $`S'_k`$ are the same).** "At $`\delta_W^2`$" means: only through $`u_W`$, $`u^{\rm c}_W`$ or $`f_W`$, with a variation bounded by the exact bounds above and vanishing as $`W\to\infty`$.

| Variant | $`\bar a_W`$ depends on $`m`$ | on $`k`$ | on $`N`$, $`\lambda_0`$ | on $`\tau`$ | wide start first: depends on $`m`$, $`k`$ (and on $`N`$, $`\lambda_0`$ for $`k\ge1`$) |
| --- | --- | --- | --- | --- | --- |
| (a) | yes, at $`\delta_W^2`$ | yes, at $`\delta_W^2`$ | yes for $`k\ge1`$, at $`\delta_W^2`$ | yes | yes, at order one, through $`\varsigma`$ |
| (b1) | yes (order one for $`k\ge1`$; at $`\delta_W^2`$ for $`k=0`$) | yes | yes for $`k\ge1`$ | yes | yes, at order one |
| (b2) | yes for $`k\ge1`$ (it is $`0`$ for $`k=0`$) | yes | yes for $`k\ge1`$ | yes | yes, at order one |
| (c) | yes, at $`\delta_W^2`$ | yes, at $`\delta_W^2`$ | yes for $`k\ge1`$, at $`\delta_W^2`$ | yes | yes, at order one, through $`\varsigma`$ and $`\rho`$ |
| (d) | yes | yes | yes for $`k\ge1`$ | yes | yes; through $`\rho`$ the extra dependence vanishes as $`1/(M_k\Lambda)`$ |

That the dependence at $`\delta_W^2`$ is really present: $`\partial u^{\rm c}_W/\partial(M_k^2)=-2\tau^2\langle\sin^2p\cos^2p/\omega_k^4\rangle_W<0`$ for every start (exact), and $`\partial u_W/\partial(M_k^2)=-\tau^2\langle\sin^2p\cos2p/\omega_k^4\rangle_W`$, which is negative for wide starts ($`\langle\sin^2p\rangle_W>2\langle\sin^4p\rangle_W`$ at leading order in $`1/W`$; order estimate). In the iterated limit $`W\to\infty`$ after $`\Lambda\to\infty`$ the entries of (a) and (c) become $`-g\tau^2`$ for every $`m`$, $`k`$, $`N`$, $`\lambda_0`$; they still depend on $`\tau`$. The bond gradient alone gives $`\bar a_W=g\tau^4s_W\to0`$. In (a), (b1), (b2), (c) the two branches have the same window average in every column; in (d) they have opposite ones.

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
Let $`C_{\rm loc}`$ be the uniform member of $`\mathcal C`$ with the profiles at $`x_0`$ and $`q_{\rm loc}`$ its distribution for the same start. In this step the parameters are the local ones of Step 3: $`\tau^0`$, $`m^0:=m_{x_0}`$, $`\eta^0:=\eta_{x_0}`$, $`M_k:=m^0+\eta^0d_k`$, $`\omega_k=\sqrt{M_k^2+\tau^{0\,2}\sin^2p}`$, and, as in (5.20), $`\bar\mu:=m^0+\eta^0\bar d=\tfrac1N\sum_kM_k`$, $`\bar\omega(p):=\sqrt{\bar\mu^2+\tau^{0\,2}\sin^2p}`$, $`\Gamma(p):=\bar\mu/\bar\omega(p)`$. The levels obey $`M_k-\bar\mu=\tfrac{2\pi\eta^0}{N\lambda_0}\bigl(k-\tfrac{N-1}2\bigr)`$, $`\lvert M_k-\bar\mu\rvert<\upsilon\,m^0`$ with $`\upsilon:=\pi\eta^0/(\lambda_0m^0)`$.

**(i) Zeroth order in the gradients at finite $`W`$.** Under $`C_{\rm loc}`$, $`\psi_k=\tilde\phi_X\,\chi_{k,\lambda}(p)`$ with $`\chi_{k,\lambda}=e^{-i\omega_k\lambda}P^{(k)}_+\lvert1\rangle+e^{i\omega_k\lambda}P^{(k)}_-\lvert1\rangle`$ (Step 4, projectors of Step 5.1 for the level $`k`$). Hence, **exactly** (infinite chain, every $`W`$, all orders in the level spacing),
```math
q_{\rm loc}(a;\lambda)=\bigl\langle Q(a;p,\lambda)\bigr\rangle_W,\qquad Q(a;p,\lambda):=\Bigl\lVert\frac1N\sum_{k=0}^{N-1}e^{2\pi ika/N}\,\chi_{k,\lambda}(p)\Bigr\rVert^2 .\qquad\text{(3.34)}
```
*First order in the level spacing, in the form of (5.21).* Replace $`\omega_k\to\bar\omega+\Gamma\,(M_k-\bar\mu)`$ and $`P^{(k)}_\pm\to\bar P_\pm`$ (the projectors at the level $`\bar\mu`$). The vectors $`\bar P_\pm\lvert1\rangle`$ are orthogonal with squared norms $`\tfrac12(1\pm\Gamma)`$, and $`\Gamma(M_k-\bar\mu)\lambda=\tfrac{2\pi}{N}\bigl(k-\tfrac{N-1}2\bigr)\Gamma\eta^0\lambda/\lambda_0`$, so the two geometric sums are $`P_N(a;\pm\Gamma\eta^0\lambda/\lambda_0)`$:
```math
q_{\rm loc}=q^{(1)}_W+\mathcal R_W,\quad q^{(1)}_W(a;\lambda):=\Bigl\langle\tfrac{1+\Gamma(p)}2\,P_N\Bigl(a;\Gamma(p)\frac{\eta^0\lambda}{\lambda_0}\Bigr)+\tfrac{1-\Gamma(p)}2\,P_N\Bigl(a;-\Gamma(p)\frac{\eta^0\lambda}{\lambda_0}\Bigr)\Bigr\rangle_W,\quad\lvert\mathcal R_W\rvert\le\delta_W^2\frac{\tau^{0\,2}}{m^{0\,2}}\,\upsilon\Bigl[4+\upsilon+\pi\upsilon\frac{\eta^0\lambda}{\lambda_0}\Bigr]\ (\text{exact}).\qquad\text{(3.35)}
```
*Proof of the bound,* with $`s:=\tau^0\sin p`$. (1) Phases: $`f(M)=\sqrt{M^2+s^2}`$ has $`0\le f''=s^2/f^3\le s^2/m^{0\,3}`$ for $`M\ge m^0`$, so $`\lvert\omega_k-\bar\omega-\Gamma(M_k-\bar\mu)\rvert\le\tfrac12\upsilon^2s^2/m^0`$; replacing the phases changes each $`\chi_k`$ by at most $`e_1:=\tfrac12\upsilon^2s^2\lambda/m^0`$ in norm and $`Q`$ by at most $`2e_1`$. (2) Spinors: with $`\Sigma(\theta)\lvert1\rangle=(\cos\theta,\sin\theta)`$, the change of $`\chi_k`$ is $`-i\sin(\cdot)\,(\Sigma_k-\bar\Sigma)\lvert1\rangle=-2i\sin(\cdot)\sin(\tfrac{\theta_k-\bar\theta}2)\,n`$, $`n`$ a real unit vector $`(-\sin\theta_{\rm m},\cos\theta_{\rm m})`$ with $`\theta_{\rm m}`$ between $`\theta_k`$ and $`\bar\theta`$; $`\lvert\theta_k-\bar\theta\rvert\le\upsilon\lvert s\rvert/m^0`$ (from $`\lvert\partial\theta/\partial M\rvert=\lvert s\rvert/\omega^2`$), and $`\lvert\langle\chi\vert n\rangle\rvert\le2\lvert s\rvert/m^0`$ for every vector $`\chi=\cos\varphi\lvert1\rangle-i\sin\varphi\,\bar\Sigma\lvert1\rangle`$ of the first-order form. The cross term is at most $`4\upsilon s^2/m^{0\,2}`$ and the square term at most $`\upsilon^2s^2/m^{0\,2}`$. Summing, $`\lvert Q-Q^{(1)}\rvert\le\tfrac{s^2}{m^{0\,2}}\upsilon\,[\upsilon m^0\lambda+4+\upsilon]`$, $`\upsilon m^0\lambda=\pi\eta^0\lambda/\lambda_0`$, and $`\langle s^2\rangle_W\le\tau^{0\,2}\delta_W^2`$.

*What $`\mathcal R_W`$ contains.* One term of first order in the level spacing: with $`b:=\tau^{0\,2}\sin^2p/(4\bar\omega^3)`$ and $`M_\pm:=(M_k-\bar\mu)\pm(M_{k'}-\bar\mu)`$, its contribution to $`\chi_{k'}^\dagger\chi_k`$ is $`b\,\bigl\{M_+\bigl[e^{-i\Gamma M_-\lambda}-e^{i\Gamma M_-\lambda}\bigr]-2iM_-\sin\bigl((2\bar\omega+\Gamma M_+)\lambda\bigr)\bigr\}`$ (first-order change of the weights $`\cos\tfrac{\theta_k}2\cos\tfrac{\theta_{k'}}2`$, and the overlap of the upper branch of one level with the lower branch of the other). Its modulus is at most $`\upsilon s^2/m^{0\,2}`$, so it changes $`q`$ by at most $`\upsilon\,\delta_W^2\tau^{0\,2}/m^{0\,2}`$ for all $`\lambda`$; it does not grow. The rest of $`\mathcal R_W`$ is of second order in the level spacing, and it contains the only term that grows with $`\lambda`$.

**(ii) Advance and rate at finite $`W`$.** By (3.35), $`q^{(1)}_W`$ is a mixture of the distributions $`P_N(a;\vartheta)`$ over the advances $`\vartheta=\pm\Gamma(p)\eta^0\lambda/\lambda_0`$ with the weights $`\tfrac12(1\pm\Gamma(p))\lvert\tilde\phi_X(p)\rvert^2\tfrac{\mathrm dp}{2\pi}`$: on the part of the start in the upper branch of the level block the clock label advances, on the part in the lower branch it recedes (the on-site clock term is $`\sigma_3\otimes\eta^0D`$). It has the form $`P_N(a;\vartheta)`$ with a single $`\vartheta`$ only for $`\tau^0=0`$ or in the limit $`W\to\infty`$. **Definition.** The advance in $`q`$ is the mean advance of the mixture, and the rate is its derivative:
```math
\vartheta_W(\lambda):=\Bigl\langle\tfrac{1+\Gamma}2\Gamma-\tfrac{1-\Gamma}2\Gamma\Bigr\rangle_W\frac{\eta^0\lambda}{\lambda_0}=(1-\varsigma_W)\frac{\eta^0\lambda}{\lambda_0},\qquad r_W(x_0):=\frac{\mathrm d\vartheta_W}{\mathrm d\lambda}=\frac{\eta^0}{\lambda_0}\,(1-\varsigma_W),\qquad\varsigma_W(x_0):=\Bigl\langle\frac{\tau^{0\,2}\sin^2p}{\bar\mu^2+\tau^{0\,2}\sin^2p}\Bigr\rangle_W,\qquad\text{(3.36)}
```
```math
\frac{\tau^{0\,2}\langle\sin^2p\rangle_W}{\bar\mu^2+\tau^{0\,2}}\le\varsigma_W\le\delta_W^2\,\frac{\tau^{0\,2}}{\bar\mu^2}\le\delta_W^2\,\frac{\tau^{0\,2}}{m^{0\,2}}\qquad(\text{exact}).
```
($`\varsigma_W`$ carries a subscript; it is not the window factor $`\varsigma`$ of (3.14).) Statements, all for the first-order form at zeroth order in the gradients, infinite chain, $`\kappa=0`$:
- *Rate.* $`r_W`$ is exactly constant in $`\lambda`$, for all $`\lambda\ge0`$. This is a statement about the rate itself; it does not follow from, and does not need, a bound on $`q`$. The remainder $`\mathcal R_W`$ grows linearly with $`\lambda`$ and defines no advance at this order.
- *Spread.* The variance of the advance in the mixture is $`\langle\Gamma^2\rangle_W(1-\langle\Gamma^2\rangle_W)(\eta^0\lambda/\lambda_0)^2\le\varsigma_W(\eta^0\lambda/\lambda_0)^2`$, and with $`\lvert\partial_\vartheta^2P_N\rvert<2\pi^2/3`$ and the vanishing first moment, $`\lvert q^{(1)}_W-P_N(a;\vartheta_W)\rvert\le\tfrac{\pi^2}{3}\varsigma_W(\eta^0\lambda/\lambda_0)^2`$ (exact).
- *Dependence on the body at finite $`W`$.* On $`\lambda_0`$ and $`\eta^0`$: through the prefactor. On $`m^0`$ and $`\tau^0`$: yes, through $`\varsigma_W`$, with a relative size of at most $`\delta_W^2\tau^{0\,2}/m^{0\,2}`$; the dependence is really present, since $`\partial\varsigma_W/\partial(\tau^{0\,2}/\bar\mu^2)=\langle\sin^2p\,(1+\tau^{0\,2}\sin^2p/\bar\mu^2)^{-2}\rangle_W>0`$ (exact). On $`N`$ and the level structure: the prefactor uses only the common spacing of adjacent levels; beyond it they enter through the reference level $`\bar\mu`$ of $`\varsigma_W`$, and moving that level within the range of the levels changes $`r_W`$ by at most $`\tfrac{\eta^0}{\lambda_0}\,2\upsilon\,\delta_W^2\tau^{0\,2}/m^{0\,2}`$, which is the order of $`\mathcal R_W`$: this dependence is **not determined** at first order in the level spacing.
- *M6.* $`\eta^0/\lambda_0=\tfrac{N}{4\pi}(\Delta_{x_0,k+1}-\Delta_{x_0,k})`$, $`\bar\mu=\tfrac1{2N}\sum_k\Delta_{x_0,k}`$, $`\tau^0=t_{x_0-1}+t_{x_0}`$, and $`\langle\cdot\rangle_W`$ uses the place amplitudes of the start: $`r_W`$ is a function of $`C_{\rm eff}`$ modulo $`\mathbb 1`$ and of the start, invariant under (8.1).

**(iii) Wide start (exact, infinite chain).** From Step 4, $`\chi_{k,\lambda}=e^{-i\omega_k\lambda}\lvert1\rangle+r_k`$ with $`r_k=i\sin(\omega_k\lambda)\bigl[(1-\tfrac{M_k}{\omega_k})\lvert1\rangle+\tfrac{\tau^0\sin p}{\omega_k}\lvert2\rangle\bigr]`$, so $`\lvert\langle1\vert r_k\rangle\rvert\le\tfrac{s^2}{2M_k^2}`$ and $`\lVert r_k\rVert^2\le\tfrac{s^2}{M_k^2}`$; and $`\lvert(\omega_k-\omega_{k'})-(M_k-M_{k'})\rvert\le\lvert M_k-M_{k'}\rvert\tfrac{s^2}{2m^{0\,2}}`$ with $`\lvert M_k-M_{k'}\rvert<\tfrac{2\pi\eta^0}{\lambda_0}`$. Hence $`\lvert\chi_{k',\lambda}^\dagger\chi_{k,\lambda}-e^{-i(M_k-M_{k'})\lambda}\rvert\le\tfrac{s^2}{m^{0\,2}}(2+\pi\eta^0\lambda/\lambda_0)`$. Since $`M_k-M_{k'}`$ is exactly linear in $`k-k'`$, the geometric sum gives $`P_N`$: $`\lvert q_{\rm loc}-P_N(a;\eta^0\lambda/\lambda_0)\rvert\le\delta_W^2(\tau^0/m^0)^2(2+\pi\eta^0\lambda/\lambda_0)`$.

**(iv) Gradients, ends, records.** *(Exact, every chain that contains the start, every real $`w`$.)* On the full clock space $`C=C_{\rm loc}+C_1`$ with $`C_1=\sum_yy\,P_y\otimes\bigl[\sigma_3\otimes(mg_m+g_\eta D)-\mathcal F\bigr]`$ plus the bond part $`\tfrac{\tau g_\zeta}{2}\sum_y(y+\tfrac12)(R_y\otimes(-i\sigma_1)+\text{h.c.})`$, $`y=x-x_0`$. For every vector $`\psi`$, $`\lVert C_1\psi\rVert\le b_{\rm cl}\,(\lVert\hat y\psi\rVert+\tfrac12)`$ with
```math
b_{\rm cl}:=m\lvert g_m\rvert+d_{N-1}\lvert g_\eta\rvert+\lvert\mathcal F\rvert+\tau\lvert g_\zeta\rvert\qquad(d_{N-1}=\lVert D\rVert),
```
and under $`C_{\rm loc}`$, $`\lVert\hat y\psi(s)\rVert\le W+\tau^0s`$, because $`\lVert[C_{\rm loc},\hat y]\rVert=\lVert\hat v\rVert\le\tau^0`$ on every chain, open ends included. Duhamel's formula gives $`\lVert\psi(\lambda)-\psi_{\rm loc}(\lambda)\rVert\le b_{\rm cl}\lambda(W+\tfrac12+\tfrac12\tau^0\lambda)`$ and $`\lvert q-q_{\rm loc}\rvert\le2\lVert\psi-\psi_{\rm loc}\rVert`$. By (3.4), $`q_{\rm loc}`$ on the chain and on the infinite chain differ by at most $`4e^{\theta_0}\theta_0^r/r!`$, $`\theta_0=\tau^0\lambda`$, $`r`$ the distance from the support of the start to the nearer end; the records add at most (3.3). Together, **exactly**, on the chain $`\lvert x\rvert\le L`$, for every real $`w`$:
```math
q(a;\lambda)=P_N\Bigl(a;\frac{\eta_{x_0}\lambda}{\lambda_0}\Bigr)+\mathcal R_{\rm cl},\qquad\lvert\mathcal R_{\rm cl}\rvert\le\delta_W^2\frac{\tau^{0\,2}}{m_{x_0}^2}\Bigl(2+\frac{\pi\eta_{x_0}\lambda}{\lambda_0}\Bigr)+2\,b_{\rm cl}\,\lambda\Bigl(W+\tfrac12+\tfrac12\tau^0\lambda\Bigr)+4e^{\theta_0}\frac{\theta_0^{\,r}}{r!}+2\kappa^2\sigma_X^2L^2\lambda^2 .\qquad\text{(3.22)}
```
*Answer to item 3(b), and the two orders of the limits.*
- *Gradients first (the limit of the question:* $`g_\bullet W\to0`$, $`g_\bullet\tau\lambda\to0`$, $`\mathcal F\lambda\to0`$ at fixed $`W`$, $`\lambda`$ and profiles at $`x_0`$, on chains with $`r\to\infty`$, $`\kappa\to0`$). The last three terms of (3.22) vanish and $`q\to q_{\rm loc}`$, which is (3.34) exactly and (3.35) to first order in the level spacing. The first term of (3.22) does **not** vanish in this limit: at finite $`W`$ the zeroth-order distribution is the mixture (3.35), not $`P_N(a;\eta_{x_0}\lambda/\lambda_0)`$. Then $`W\to\infty`$: $`q_{\rm loc}\to P_N(a;\eta_{x_0}\lambda/\lambda_0)`$ at fixed $`\lambda`$, and $`r_W\to\eta_{x_0}/\lambda_0`$.
- *Wide start first.* Inside the class $`W<L-\lvert x_0\rvert<1/\lvert g_\bullet\rvert`$, so $`W\to\infty`$ at fixed $`g_m,g_\eta,g_\zeta\neq0`$ is not available, and for the largest admissible $`W`$ the term $`b_{\rm cl}\lambda W`$ is not small: at $`\tau=0`$ the exact distribution $`\sum_x\phi_X(x)^2P_N(a;\eta_x\lambda/\lambda_0)`$ then has advances spread over $`g_\eta W\lambda/\lambda_0`$, and no rate at $`x_0`$ results. For variant (d) alone the order is available: by (9.11)–(9.12) at $`p_0=0`$, $`q\to P_N(a;\vartheta_1(\lambda))`$ up to $`\mathcal R_1`$, and then $`\mathcal F\to0`$ gives $`P_N(a;\lambda/\lambda_0)`$, the same as in the other order.
- *Joint regime.* The single-advance form needs $`\delta_W^2\tfrac{\tau^{0\,2}}{m^{0\,2}}(2+\pi\eta^0\lambda/\lambda_0)\ll1`$ and $`b_{\rm cl}\lambda(W+\tau^0\lambda)\ll1`$ together.

**Definition of the rate at $`x_0`$, with its approximation.**
```math
\text{rate at }x_0:=\lim_{W\to\infty}r_W(x_0)=\frac{\eta_{x_0}}{\lambda_0}=\frac{N}{2\pi}\bigl(E^+_{x_0,k+1}-E^+_{x_0,k}\bigr),\ \ \text{tick }\frac{\lambda_0}{\eta_{x_0}};\qquad\text{at finite }W:\ \ r_W=\frac{\eta_{x_0}}{\lambda_0}(1-\varsigma_W),\ \ \text{tick }\frac{\lambda_0}{\eta_{x_0}(1-\varsigma_W)},\ \ \Bigl\lvert r_W-\frac{\eta_{x_0}}{\lambda_0}\Bigr\rvert\le\frac{\eta_{x_0}}{\lambda_0}\,\delta_W^2\frac{\tau^{0\,2}}{m_{x_0}^2}.\qquad\text{(3.23)}
```
$`\eta_{x_0}/\lambda_0`$ is a difference of on-site eigenvalues (M6), the spacing of adjacent clock levels at $`x_0`$. It is the rate in the **wide-start approximation** $`\varsigma_W\to0`$. Range: for the rate, $`\delta_W^2\tau^{0\,2}/m_{x_0}^2\ll1`$, for all $`\lambda`$; for the description of $`q`$ by the single advance $`\eta_{x_0}\lambda/\lambda_0`$, in addition $`\delta_W^2\tfrac{\tau^{0\,2}}{m_{x_0}^2}\pi\eta_{x_0}\lambda/\lambda_0\ll1`$, that is, a number of ticks small compared with $`m_{x_0}^2/(\pi\tau^{0\,2}\delta_W^2)`$. The wide-start rate depends on $`\eta_{x_0}`$ and $`\lambda_0`$ only; the finite-width correction $`-\varsigma_W`$ depends on $`m`$ and $`\tau`$ as stated in (ii).

**(v) First corrections in the gradients.** Let $`\xi_y:=\xi-x_0`$ (Step 4, for $`\hat y`$), so $`\langle\xi_y\rangle_W=\bar y_0:=\bar x_{\rm lab}(0)-x_0`$, $`\xi_y\equiv0`$ for even $`w`$, and $`\lvert\langle\xi_yf\rangle_W\rvert\le\lVert\hat y\phi\rVert\sup\lvert f\rvert\le W\sup\lvert f\rvert`$. On the level $`k`$, $`C^{(k)}=C^{(k)}_{\rm loc}+\tfrac12\{\hat y,B_k(\hat p)\}`$ exactly (Step 3), and $`B_k=\partial_yC^{(k)}_{\rm loc}`$ is the derivative of the local block along the profiles, $`(\tau^0,M_k,V)\to(\tau^0+\tau g_\zeta y,\,M_k+G_ky,\,V-\mathcal Fy)`$. In the first-order change of $`\langle\psi_{k'}\vert\psi_k\rangle`$ the identity of Step 4 gives $`\xi_y`$ times $`\partial_y(\chi_{k'}^\dagger\chi_k)`$ (Duhamel), plus terms $`\tfrac i2[u^\dagger B\partial_pv-(\partial_pu^\dagger)Bv]`$ whose $`11`$ elements are odd in $`p`$ (products of matrices with $`O(-p)=\sigma_3O(p)\sigma_3`$ and one $`p`$-derivative) and average to zero. Hence, **exactly** (infinite chain, every real $`w`$, first Taylor coefficient in the gradients at fixed profiles at $`x_0`$),
```math
\delta^{(1)}q(a;\lambda)=\bigl\langle\xi_y(p)\,\partial_yQ(a;p,\lambda)\bigr\rangle_W,\qquad\lvert\delta^{(1)}q\rvert\le2\,b_{\rm cl}\,\lambda\,W,\qquad\partial_yQ(a;0,\lambda)=g_\eta\frac{\lambda}{\lambda_0}\,\partial_\vartheta P_N\Bigl(a;\frac{\eta_{x_0}\lambda}{\lambda_0}\Bigr),\qquad\text{(3.37)}
```
where $`\partial_yQ`$ is the derivative of (3.34) along the profiles ($`\mathcal F`$ drops out of it: $`V`$ is a common phase). Consequences:
- The first-order term is the local distribution taken at the place $`x_0+\xi_y(p)`$: it is a term of the position and width of the start. The beginning motion (every term without $`\xi_y`$) contributes **nothing** at first order, for every real $`w`$; the plain gradient contributes nothing at first order at all.
- With $`\lvert\partial_yQ(p)-\partial_yQ(0)\rvert\le\tfrac{\pi^2}{8}4\sin^2\tfrac p2\sup\lvert\partial_p^2\partial_yQ\rvert`$ and $`\lVert4\sin^2\tfrac{\hat p}2\phi\rVert=O(W^{-2})`$: $`\delta^{(1)}q=g_\eta\,\bar y_0\,\tfrac{\lambda}{\lambda_0}\,\partial_\vartheta P_N+O\bigl(b_{\rm cl}\lambda(1+\tau^0\lambda)^2/W\bigr)`$ (order estimate); at $`\tau=0`$ the second term is exactly zero, in agreement with the exact $`q=\sum_x\phi_X(x)^2P_N(a;\eta_x\lambda/\lambda_0)`$.
- *Even $`w`$, chain symmetric about $`x_0`$.* Let $`\Pi`$ be the reflection $`y\to-y`$ times $`\sigma_3`$. Then $`\Pi C_{\rm loc}\Pi=C_{\rm loc}`$, $`\Pi C_1\Pi=-C_1`$, the clock reading commutes with $`\Pi`$, and the start is $`\Pi`$-invariant. Hence $`q`$ is an even function of $`(g_m,g_\eta,g_\zeta,\mathcal F)`$ jointly at fixed profiles at $`x_0`$ (exact): no term of odd total degree. With the second-order Duhamel formula and $`\lVert\hat y^{\,n}\psi(s)\rVert\le c\,(W+1+\tau_{\max}s)^n`$, $`n\le2`$, $`\tau_{\max}:=\tau\max_x\zeta_x`$,
```math
\lvert q-q_{\rm loc}\rvert\le c\,\Bigl[b_{\rm cl}\,\lambda\,\bigl(W+1+\tau_{\max}\lambda\bigr)\Bigr]^2\qquad(\text{order estimate; even }w,\ \text{symmetric chain}).\qquad\text{(3.33)}
```
For every real $`w`$ on the infinite chain the same bound holds for $`q-q_{\rm loc}-\delta^{(1)}q`$. On a chain that is not symmetric about $`x_0`$ the end term of (3.22) is added.
- *Second order, width.* With $`\sigma_W^2:=\sum_x(x-\bar x_{\rm lab}(0))^2\phi_X(x)^2\le W^2`$: at $`\tau=0`$ the exact mixture gives, about the mean position, $`q=P_N+\tfrac12\partial_\vartheta^2P_N\,(g_\eta\sigma_W\lambda/\lambda_0)^2+O\bigl((g_\eta W\lambda/\lambda_0)^3\bigr)`$. For $`\tau>0`$ the second-order term is $`\tfrac12\sigma_W^2(g_\eta\lambda/\lambda_0)^2\partial_\vartheta^2P_N`$ plus terms with at most one power of $`W`$ at fixed $`\lambda`$ (order estimate: only the term with both factors $`\hat y`$ acting on the start carries $`W^2`$, and it is $`\tfrac12\sigma_W^2\partial_y^2Q(a;0,\lambda)`$ to leading order in $`1/W`$).
- *Second order, motion, variant (d).* The start of 09-proper-time with $`p_0=0`$ and $`g_1=\tilde\phi_X`$ differs from $`S_{\rm clock}`$ by at most $`\delta_W\tau^0/(2m^0)`$ in norm ($`\lVert\beta_{0,+}(p)-\lvert1\rangle\rVert\le\tau^0\lvert\sin p\rvert/(2m^0)`$), for all $`\lambda`$ and $`\mathcal F`$. By (9.11)–(9.12), $`q=P_N(a;\vartheta_1)+O(\delta_W\tau^0/m^0)+\mathcal R_1`$ with $`\vartheta_1=\tfrac{\lambda}{\lambda_0}\bigl[1-\tfrac{\tau^2\mathcal F^2\lambda^2}{6\bar\mu^2}+O((\mathcal F\lambda)^4)\bigr]`$: for a wide start the coefficient of $`(\mathcal F\lambda)^2`$ is not zero.

**Table 8.1: the order at which the width and the beginning motion change $`q`$.** The three notions are separate columns; "not determined" means that this package proves only the bound of the third column.

| Effect | Lowest order allowed (exact symmetry or identity) | Upper bound (proven) | First nonzero order (proven) | Not determined |
| --- | --- | --- | --- | --- |
| Position of the start, $`\bar y_0\neq0`$ | first power of the gradients | $`2b_{\rm cl}\lambda W`$, (3.37) | first power, $`g_\eta\bar y_0\lambda/\lambda_0`$, if $`g_\eta\neq0`$: exact at $`\tau=0`$; for $`\tau>0`$ for wide starts with $`\bar y_0\propto W`$ (order estimate). Its leading part vanishes if the rate is taken at $`\bar x_{\rm lab}(0)`$ | $`g_\eta=0`$ (variants (b1), (d), bond gradient): only $`O(b_{\rm cl}\lambda(1+\tau^0\lambda)^2/W)`$ is proven; at $`\tau=0`$ it is exactly zero |
| Width, even $`w`$ | second power (odd orders vanish, exact) | (3.33) | second power, $`(g_\eta\sigma_W\lambda/\lambda_0)^2`$, if $`g_\eta\neq0`$: exact at $`\tau=0`$; for $`\tau>0`$ for wide starts (order estimate) | $`g_\eta=0`$: the terms with $`W^2`$ vanish; whether a width term of second order exists is not determined |
| Beginning motion | second power, for every real $`w`$ (the first-order motion term is zero, (3.37)) | $`c[b_{\rm cl}\lambda(1+\tau_{\max}\lambda)]^2`$ at $`W`$-independent order, from (3.33) | variant (d): second power, relative change $`-(\tau\mathcal F\lambda)^2/(6\bar\mu^2)`$ of the advance, for wide starts (order estimate) | $`g_m`$, $`g_\zeta`$ and the motion part of $`g_\eta`$: whether the second-order coefficient is nonzero is not determined |

### Step 9. Two places and comparison (items 3(c), 4)

*Procedure.* The rates at $`x_1`$ and $`x_2`$ are taken from two runs of the same description (same contract list, starts $`S_{\rm clock}(x_1)`$ and $`S_{\rm clock}(x_2)`$ with the same $`w`$ and $`W`$), with the clock reading applied at the same value of $`\lambda`$ in both. The comparison relies on A8: readings at equal $`\lambda`$ are compared through the order of $`\lambda`$, which is not a time (M1). The ratio of rates is the ratio of the advances (3.36) at equal $`\lambda`$, the inverse ratio of the ticks; it does not depend on the $`\lambda`$ chosen. With $`\varkappa_i:=\tau^0(x_i)/\bar\mu(x_i)`$, by (3.36) and (3.23),
```math
\frac{r_W(x_1)}{r_W(x_2)}=\frac{\eta_{x_1}}{\eta_{x_2}}\cdot\frac{1-\varsigma_W(x_1)}{1-\varsigma_W(x_2)}\ \xrightarrow[W\to\infty]{}\ \frac{\eta_{x_1}}{\eta_{x_2}}=\frac{1+g_\eta x_1}{1+g_\eta x_2}:\quad\text{(a), (b2), (c)}:\ \frac{1+gx_1}{1+gx_2};\quad\text{(b1), (d)}:\ 1;\qquad\Bigl\lvert\frac{1-\varsigma_W(x_1)}{1-\varsigma_W(x_2)}-1\Bigr\rvert\le\delta_W^2\,\lvert\varkappa_1^2-\varkappa_2^2\rvert\,(1+\varkappa_2^2).\qquad\text{(3.24)}
```
The bound is exact: $`\varsigma_W=\langle\varkappa^2\sin^2p/(1+\varkappa^2\sin^2p)\rangle_W`$ has $`0<\partial\varsigma_W/\partial\varkappa^2\le\langle\sin^2p\rangle_W\le\delta_W^2`$ and $`1-\varsigma_W\ge1/(1+\varkappa^2)`$; the same $`\langle\cdot\rangle_W`$ serves both runs. The ratios named in (3.24) are those of the wide-start approximation of (3.23). The finite-width factor, variant by variant ($`\bar d=\pi(N-1)/(N\lambda_0)`$):

| Variant | $`\varkappa_x`$ | finite-width factor | ratio at finite $`W`$ depends on $`m`$, $`\tau`$ | on $`N`$, $`\lambda_0`$ |
| --- | --- | --- | --- | --- |
| (a) | $`\tau/[(1+gx)(m+\bar d)]`$ | $`\neq1`$ for $`gx_1\neq gx_2`$ | yes, at relative order $`\delta_W^2`$, within the bound of (3.24) | only through $`\bar d`$: not determined at this order |
| (b1) | $`\tau/[m(1+gx)+\bar d]`$ | $`\neq1`$ for $`gx_1\neq gx_2`$: the ratio is not $`1`$ | yes, at relative order $`\delta_W^2`$ | only through $`\bar d`$: not determined |
| (b2) | $`\tau/[m+(1+gx)\bar d]`$ | differs from $`1`$ only through $`\bar d`$, by at most $`2\delta_W^2\tau^2\bar d\lvert g(x_1-x_2)\rvert(1+\varkappa_2^2)/m^3`$, the order of $`\mathcal R_W`$: not determined | not determined | not determined |
| (c) | $`\tau/(m+\bar d)`$ for all $`x`$ | exactly $`1`$ | no | no |
| (d) | $`\tau/(m+\bar d)`$ for all $`x`$ | exactly $`1`$ | no | no |

For (c), $`C_{\rm loc}(x)=(1+gx)`$ times the Model D contract exactly, so $`q_{\rm loc}`$ at $`x`$ is the Model D distribution at $`(1+gx)\lambda`$: the ratio $`(1+gx_1)/(1+gx_2)`$ holds at every $`W`$ and to all orders in the level spacing. For (d) the local contracts at $`x_1`$ and $`x_2`$ differ by a multiple of $`\mathbb 1`$ and $`q_{\rm loc}`$ is the same. In no variant does the ratio depend on the unit of $`\lambda`$ ($`\varsigma_W`$ is invariant under a rescaling of $`\lambda`$). In the wide-start approximation the ratio depends on none of $`m`$, $`N`$, $`\lambda_0`$, $`\tau`$. *Accuracy.* The rates are defined at zeroth order in the gradients, so (3.24) is exact for them; how well $`q`$ of each run is described by them is given by (3.35), (3.37), (3.33) and (3.22).

*Comparison (item 4), first order in the gradients.* "The acceleration from rest" is the acceleration of item 2(a), (3.10)/(3.11), and its window average of item 2(b).

| Variant | (3.10)/(3.11) the same for all $`k`$, $`m`$ (at $`\lambda>0`$) | $`\bar a_W`$ (finite $`W`$, $`\Lambda\to\infty`$) the same | $`\lim_{W\to\infty}\bar a_W`$ the same | window average with the wide start first the same | clock rate depends on the place: wide start | at finite $`W`$ |
| --- | --- | --- | --- | --- | --- | --- |
| (a) | no | no; $`\lvert\bar a_W+g\tau^2\rvert\le\lvert g\rvert\tau^2(2+\tfrac{\tau^2}{M_k^2})\delta_W^2`$ | yes, $`-g\tau^2`$ | no (order one, no long-window limit) | yes | yes |
| (b1) | no | no | no | no | no | yes, at relative order $`\delta_W^2\tau^2/m^2`$, through $`\varsigma_W`$ |
| (b2) | no | no | no | no | yes | yes |
| (c) | no | no; $`\lvert\bar a_W+g\tau^2\rvert\le2\lvert g\rvert\tau^2(1+\tfrac{\tau^2}{M_k^2})\delta_W^2`$ | yes, $`-g\tau^2`$ | no (order one, no long-window limit) | yes | yes |
| (d) | no | no | no | no (the limit $`\tfrac{\tau^2\mathcal F}{M_k}`$ exists and depends on $`k`$, $`m`$) | no | no (exactly) |

In the first column, (3.11) is a non-constant function of $`M_k\lambda`$ in every variant (for (a): $`-2g\tau^2[\sin^2(M_k\lambda)+M_k\lambda\sin(2M_k\lambda)]`$); only at $`\lambda=0`$ is the acceleration the same for all $`k`$ and $`m`$, by (3.8). Therefore:
```math
\begin{aligned}&\text{For the acceleration of item 2(a), and for its window average at finite }W\text{ or with the wide start taken first, no variant has an acceleration from rest}\\&\text{that is the same for all }k\text{ and }m.\ \text{In the iterated limit }\Lambda\to\infty\text{, then }W\to\infty\text{, with the clock rate in the wide-start approximation (3.23), the variants (a) and (c),}\\&\text{and only these among the five, have both properties (window average }-g\tau^2\text{; place-dependent clock rate). At finite }W\text{ they have the first up to the bounds of the table;}\\&\text{(b1) then also has a place-dependent rate, at relative order }\delta_W^2\tau^2/m^2\text{, but not the first property.}\end{aligned}\qquad\text{(3.25)}
```

## Result

- **Item 1.** Operators (3.5), (3.6) and the exact second derivative (3.7); values at $`\lambda=0`$ (3.8), equal for $`S_k`$ and $`S'_k`$.
- **Item 2(a).** First-order acceleration at finite $`W`$ (3.10), its wide-start limit (3.11), requirements (3.12) and Step 4.
- **Item 2(b).** Finite $`W`$: structure (3.26) with $`A_2`$ explicit; the long-window limit $`\bar a_W`$ exists and is (3.27), with its coefficients; the oscillating remainder grows as $`\lambda^{1/2}`$ for $`G_k\neq0`$ and for $`\mathcal F\neq0`$ alike, and decays for the bond gradient (Step 5.2). Wide start first: (3.13), (3.14); the coefficients of $`g_m`$, $`g_\eta`$ have no long-window limit. The two limits do not commute for $`G_k\neq0`$ (3.28). Remainder of the first-order treatment (3.16), exact on the open chain; the range is a sufficient condition.
- **Item 2(c).** (3.29) for $`\bar a_W`$; (3.17) for the wide-start-first average.
- **Item 2(d), 2(e).** (3.31), (3.30), Tables 6.1 and 6.2.
- **Item 3(a).** Uniform profiles (3.20), tick (3.21).
- **Item 3(b).** At zeroth order in the gradients and finite $`W`$ the distribution is (3.34) exactly and, to first order in the level spacing, the mixture (3.35) of forward and backward advances, with an exact remainder. The advance is its mean, and the rate is $`r_W=\tfrac{\eta_{x_0}}{\lambda_0}(1-\varsigma_W)`$, constant in $`\lambda`$ (3.36), with $`0<\varsigma_W\le\delta_W^2\tau^{0\,2}/m_{x_0}^2`$. In the wide-start approximation $`q=P_N(a;\eta_{x_0}\lambda/\lambda_0)`$ within (3.22), and the rate at $`x_0`$ is $`\eta_{x_0}/\lambda_0`$ (3.23). At finite $`W`$ the rate depends on $`m`$ and $`\tau`$ at relative order $`\delta_W^2\tau^2/m^2`$; its dependence on $`N`$ and the level structure beyond the common spacing is not determined at this order. First corrections in the gradients: the exact first-order term (3.37) is a position term, and the motion has none; (3.33); Table 8.1 gives, separately, the lowest allowed order, the proven bound, the proven first nonzero order (clock gradient: first power for an off-centre start, second power for an even one; plain gradient: second power of $`\mathcal F\lambda`$) and what is not determined (width for $`g_\eta=0`$; second-order motion coefficients of $`g_m`$, $`g_\zeta`$, $`g_\eta`$).
- **Item 3(c).** Ratio (3.24): $`\eta_{x_1}/\eta_{x_2}`$ in the wide-start approximation; at finite $`W`$ times $`(1-\varsigma_W(x_1))/(1-\varsigma_W(x_2))`$, which is exactly $`1`$ in (c) and (d), differs from $`1`$ in (a) and (b1) (dependence on $`m`$, $`\tau`$ at relative order $`\delta_W^2`$), and is not determined in (b2). No dependence on the unit of $`\lambda`$.
- **Item 4.** Table of Step 9 and (3.25).
- **Additional result (not an answer to an item).** The secular acceleration $`a_{\rm sec}`$ (3.15), with (3.17)–(3.19) and the absolute error (3.32); it equals $`\lim_{W\to\infty}\lim_{\Lambda\to\infty}`$ of the window average (3.28).
- **Controls (M9).** A window average independent of $`k`$ and $`m`$ fails in (b1), (b2), (d) in every limit, and in (a), (c) at finite $`W`$ and with the wide start first; a place-dependent rate fails in (d) at every $`W`$ and in (b1) for the wide start; equal fall of the two branches fails in (d) (start $`S'_k`$); a rate independent of $`m`$ and $`\tau`$ fails at finite $`W`$ (3.36).

## Consistency checks

1. **Dimensions and zero gradients.** With $`x`$ a pure label, $`\tau`$, $`M_k`$, $`G_k`$, $`\mathcal F`$, $`b_1`$, $`b_{\rm cl}`$ have the unit $`1/\lambda`$ and $`g_\bullet`$ none; $`s_W`$ has the unit $`\lambda^2`$; $`u_W`$, $`f_W`$, $`\varsigma_W`$, $`\upsilon`$, $`\varkappa`$ have none; $`\lambda_W`$ has the unit $`\lambda`$. Accelerations, (3.8), (3.11), (3.15), (3.16), (3.27), (3.28), (3.32) and the coefficient $`a_{\rm sec}(p)`$: $`1/\lambda^2`$. Velocities, (3.13), the density $`\nu`$ of (3.26), $`\nu_0`$, $`A_0`$ and the late-time form of $`O_W`$ ($`\tfrac{\tau^2G_k}{M_k}(\lambda_W\lambda)^{1/2}`$): $`1/\lambda`$; $`A_1`$: $`1/\lambda^2`$; $`A_2=-i\mathcal FM_k\omega_k'^{\,2}/\omega_k`$: $`1/\lambda^3`$, so that $`\lambda^jA_j`$ has the unit $`1/\lambda`$ for each $`j`$. Rates (3.23), (3.36): $`1/\lambda`$. (3.22), (3.33), (3.34), (3.35), (3.37), $`\vartheta_W`$: none. For zero gradients (3.6) is $`\hat a_0`$ of (6.12), (3.11) and (3.27) vanish, (3.37) vanishes, $`q=q_{\rm loc}`$, and (3.24) is $`1`$ at every $`W`$. Passed.
2. **Variant (d), including the new $`A_2`$.** (3.5)–(3.6) reduce to (6.12); (3.11) gives $`\tfrac{2\tau^2}{M_k}\mathcal F\sin^2(M_k\lambda)`$, the label form of (6.13); (3.14) gives $`\tfrac{\tau^2}{M_k}\mathcal F(1-\rho)`$, in agreement with (6.24), (6.15) and $`\overline{\ddot{\bar m}}=\mathcal F/I^{\rm lab}_k`$ of (6.20), and both orders of the limits give $`\tau^2\mathcal F/M_k`$. Second route to $`A_2`$: with the exact shift $`p\to p+\mathcal F\lambda`$ of (9.1), the first-order velocity is $`\mathcal F\lambda\langle\partial_p\hat v_0\rangle+\mathcal F\int_0^\lambda s\,\langle-i[V(\lambda),V(s)]\rangle\,\mathrm ds`$; its only term with $`\lambda^2`$ is $`\mathcal F\tfrac{\lambda^2}2\omega\omega'\langle-i[(\Sigma')^I(\lambda),\Sigma]\rangle=\mathcal F\tfrac{M_k}{\omega_k}\omega_k'^{\,2}\lambda^2\sin(2\omega_k\lambda)`$, as in (3.26), its secular term is $`\mathcal F\omega_k''\tfrac{M_k}{\omega_k}\lambda`$, as in $`a_{\rm sec}(p)`$, and at $`p=0`$ the whole expression is the $`\mathcal F`$ part of (3.13). For (d) the clock has no first-order term (3.37), in agreement with the evenness of $`\vartheta_1`$ of (9.12) in $`\mathcal F`$ at $`p_0=0`$. Passed.
3. **Independent routes for the clock results, and $`\tau\to0`$.** (i) Duhamel in the level: the coefficient of $`-i(M_k-M_{k'})`$ in $`\chi_{k'}^\dagger\chi_k`$ at first order is $`\int_0^\lambda\langle1\vert\sigma_3^I(s)\vert1\rangle\mathrm ds=\Gamma^2\lambda+\tfrac{\tau^2\sin^2p}{2\omega^3}\sin(2\omega\lambda)`$; its secular part is the mean advance of (3.36), its oscillating part is the first-order term of $`\mathcal R_W`$ stated in Step 8(i), and its $`\lambda`$-derivative is $`1`$ at $`\lambda=0`$ and lies in $`[1-2\tau^2\sin^2p/\omega^2,1]`$. (ii) The upper-branch part of (3.35) alone is the form (3.20) of the clock-carrying start. (iii) Variant (c): the exact proportionality $`C_{\rm loc}(x)=(1+gx)C_{\rm D}`$ gives the ratio $`(1+gx_1)/(1+gx_2)`$ at every $`W`$, as (3.24) with equal $`\varsigma_W`$. (iv) $`\tau\to0`$: all accelerations vanish as $`\tau^2`$, $`\varsigma_W\to0`$, $`\mathcal R_W\to0`$, and $`q`$ becomes the exact mixture over places of Step 8. (v) The branch function $`E_\sigma(p,x)=\sigma\sqrt{M_{x,k}^2+\tau^2\zeta(x)^2\sin^2p}+V_x`$ with $`\dot x=\partial_pE_\sigma`$, $`\dot p=-\partial_xE_\sigma`$ reproduces the three coefficients of $`a_{\rm sec}(p)`$ in (3.26). Passed.

## Open issues

- The amplitudes $`\nu_0`$, $`A_0`$, $`A_1`$ of (3.26) are not given in closed form for $`p\neq0`$; the constant $`c_W`$ is not determined. The late-time forms of Step 5.2 are leading stationary-phase terms; the statements for $`\lambda\ll\lambda_W`$ assume $`W\ge\tau/M_k`$; the coefficient of the decaying bond-gradient oscillation is not computed.
- (3.27) and (3.14) are statements about the first Taylor coefficient. The range (3.16) is a sufficient condition; the sharp range is not determined, and the growing oscillation beyond first order is not derived here; it belongs to the package on long falls.
- For variant (a) the dependence of $`\bar a_W`$ on $`M_k`$ is shown to be present for wide starts only (order estimate); for variant (c) it is exact for every start.
- Clock at finite $`W`$: the advance is defined as the mean of the mixture (3.35), which is fixed by the description (the level coherences of the clock's view) and not by $`q`$ alone; it is defined from the first-order form only. The dependence of $`r_W`$ and of the ratio (3.24) on $`N`$, $`\lambda_0`$ and the level structure beyond the common level spacing is of the order of $`\mathcal R_W`$ and is not determined; it needs the second order in the level spacing. This includes the finite-width factor of variant (b2).
- Item 3(b), first nonzero orders: not determined for the width when $`g_\eta=0`$, and for the second-order motion coefficients of $`g_m`$, $`g_\zeta`$ and $`g_\eta`$ (Table 8.1, last column). Proven there: the vanishing of the first order of the motion, and the upper bounds.
- For unbounded bond profiles the limit of a long chain is not shown.
- The two rates are compared across two runs through A8; a comparison inside one description is not treated.

## Methods used

- Heisenberg equations of motion, commutators on a chain
- Effective body contract and sector decomposition of the records
- First-order perturbation theory (Duhamel), Taylor remainder bounds with explicit operator norms on the open chain
- Plane-wave representation, band projectors, parity and reflection symmetry
- Separation of secular and oscillating terms; stationary-phase estimates with vanishing amplitudes
- Finite-propagation (Dyson series) bound
- Window averaging of oscillating terms; iterated limits
- Spectrum of a ring clock (geometric sum); mixtures of clock distributions and their mean advance
- Scaling symmetry of a contract multiplied by a common factor
