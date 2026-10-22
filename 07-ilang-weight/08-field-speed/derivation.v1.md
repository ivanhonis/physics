# Speed of the made field: front, formation of the static mark and long range

- **Subproject:** 07-ilang-weight
- **Package:** 08-field-speed
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-21

## Setup and assumptions

- **Class** (question; M8). $`N_f\ge1`$ identical field objects ($`c=+1`$) on the torus $`X_f=\mathbb Z_L^D`$, $`D\in\{1,2,3\}`$, $`L`$ even, $`|X_f|=L^D`$; no pair terms among them; own term $`C_1=-t_fA`$, $`A`$ the nearest-neighbour adjacency, $`t_f>0`$; $`\Phi_x`$ the number of field objects at $`x`$, $`n=N_f/|X_f|`$. $`\Lambda=2D\mathbb 1-A`$ has the eigenvalues $`\omega(\mathbf k)=\sum_\mu4\sin^2(k_\mu/2)`$, $`\mathbf k\in(2\pi/L)\mathbb Z_L^D`$.
- **Source** (assumption). The term $`g_s(\lambda)\Phi_{x_s}`$, $`g_s(\lambda)=0`$ for $`\lambda<0`$: (i) sudden, $`g_s(\lambda)=g_s`$ for $`\lambda\ge0`$; (ii) gradual, $`g_s(\lambda)=g_sf(\lambda/T)`$, $`f\in C^\infty(\mathbb R)`$ nondecreasing, $`f=0`$ on $`(-\infty,0]`$, $`f=1`$ on $`[1,\infty)`$. (i) is the evolution (1.9) for $`\lambda\ge0`$. (ii) has a $`\lambda`$-dependent coefficient, which A5 excludes for contracts; it is used as the question states it, as an effective description of a source switched on from outside, with $`i\,\mathrm d\Psi/\mathrm d\lambda=C(\lambda)\Psi`$.
- **Start** (assumption; M9, A11). At $`\lambda\le0`$ the field is in its lowest state without source.
- **Made field.** $`\delta\rho(x,\lambda)=\langle\Phi_x\rangle_\lambda-n`$; the static mark $`\delta\rho_{\rm st}`$ is the same quantity in the lowest state with constant $`g_s`$. Both are fixed by the state and by the operators $`\Phi_x`$, which are symmetric in the identical objects (M6).
- **Distances.** $`r=x-x_s`$ with $`|r_\mu|\le L/2`$; $`\rho=\lVert r\rVert_\infty`$, $`|r|`$ the Euclidean length, $`d=\sum_\mu|r_\mu|`$ the graph distance. Along a lattice axis $`d=\rho=|r|`$.
- **Regime** (A13). First order in $`g_s`$ at fixed $`L`$ and $`\lambda`$, remainder $`O(g_s^2)`$; every large-distance statement is a leading order, stated with its limit.
- **Inputs.** (4.4) of 06-ilang-source/04-profile:
```math
M^{(2)}(x_1,x_2)=-\frac{2n\,g_1g_2}{t_f}\,\Lambda^+(x_1,x_2),\qquad \Lambda^+(x,y)=\frac1{\lvert X_f\rvert}\sum_{\mathbf k\neq0}\frac{e^{i\mathbf k\cdot(x-y)}}{\omega(\mathbf k)},\qquad \sum_{x_2\in X_f}M^{(2)}(x_1,x_2)=0;
```
(4.4) of 07-ilang-weight/04-weight-of-bond, with $`\ell(\mathbf r)=\Lambda^+(x,x+\mathbf r)`$: $`\ell(0)-\ell(\mathbf r)=\frac{\ln|\mathbf r|}{2\pi}+\frac{2\gamma_E+3\ln2}{4\pi}+O(|\mathbf r|^{-2})-\frac{|\mathbf r|^2}{4L^2}`$ for $`D=2`$, and $`=G_0-\frac1{4\pi|\mathbf r|}+O(|\mathbf r|^{-3})-\frac{|\mathbf r|^2}{6L^3}`$, $`G_0=0.2527310`$, for $`D=3`$.

## Derivation

### Step 1. Exact reduction and first-order response

Without pair terms and with $`c=+1`$, $`C(\lambda)=\sum_{i=1}^{N_f}h_i(\lambda)`$ on the symmetric subspace, $`h(\lambda)=-t_fA+g_s(\lambda)|x_s\rangle\langle x_s|`$. The lowest state of $`-t_fA`$ is $`\psi_0=|X_f|^{-1/2}\sum_x|x\rangle`$, nondegenerate (Perron–Frobenius, connected graph), with eigenvalue $`-2Dt_f`$; the lowest admissible state is $`\psi_0^{\otimes N_f}`$. The evolution of a sum of one-object terms keeps a product of identical states a product, $`\Psi(\lambda)=\psi(\lambda)^{\otimes N_f}`$ with $`i\dot\psi=h(\lambda)\psi`$. Hence $`\langle\Phi_x\rangle_\lambda=N_f|\psi(x,\lambda)|^2`$ exactly: the made field of $`N_f`$ objects is $`N_f`$ times that of one, at every order in $`g_s`$. First-order Dyson expansion around $`e^{2iDt_f\lambda}\psi_0`$, with $`\langle x_s|\psi_0\rangle=|X_f|^{-1/2}`$:

```math
\delta\rho(x,\lambda)=2n\int_0^\lambda g_s(\lambda')\mathrm{Im}\mathcal U(x-x_s,\lambda-\lambda')\,\mathrm d\lambda'+O(g_s^2),\qquad \mathcal U(r,s)=\langle x_s+r|e^{-ist_f\Lambda}|x_s\rangle=\frac1{|X_f|}\sum_{\mathbf k}e^{i\mathbf k\cdot r-it_f\omega(\mathbf k)s}.\qquad\text{(8.1)}
```

The lowest state with constant $`g_s`$ is, at first order, $`\psi_0-\sum_{\mathbf k\ne0}|\mathbf k\rangle\langle\mathbf k|g_s|x_s\rangle\langle x_s|\psi_0\rangle/(t_f\omega(\mathbf k))`$, so

```math
\delta\rho_{\rm st}(r)=-\frac{2ng_s}{t_f}\Lambda^+(r).\qquad\text{(8.2)}
```

With $`\mathrm{Im}\mathcal U=-|X_f|^{-1}\sum_{\mathbf k}\cos(\mathbf k\cdot r)\sin(t_f\omega s)`$ and $`\int_0^\lambda\sin(t_f\omega s)\,\mathrm ds=(1-\cos t_f\omega\lambda)/(t_f\omega)`$, the sudden switching gives, for $`\lambda\ge0`$,

```math
\delta\rho(r,\lambda)=\delta\rho_{\rm st}(r)+\frac{2ng_s}{t_f}R(r,\lambda),\qquad R(r,\lambda)=\frac1{|X_f|}\sum_{\mathbf k\ne0}\frac{\cos(\mathbf k\cdot r)\cos(t_f\omega(\mathbf k)\lambda)}{\omega(\mathbf k)}.\qquad\text{(8.3)}
```

$`R(r,0)=\Lambda^+(r)`$, so $`\delta\rho(r,0)=0`$; $`R`$ is a finite sum of cosines and does not decay.

### Step 2. Free propagator and Kapteyn bound

By the Jacobi–Anger expansion $`e^{iz\cos k}=\sum_mi^mJ_m(z)e^{imk}`$ and Poisson summation over the torus,

```math
\mathcal U(r,s)=\sum_{\mathbf m\in\mathbb Z^D}\mathcal U_\infty(r+L\mathbf m,s),\qquad \mathcal U_\infty(r,s)=e^{-2iDt_fs}\prod_{\mu=1}^Di^{r_\mu}J_{r_\mu}(2t_fs).\qquad\text{(8.4)}
```

Kapteyn's inequality gives, for integer $`m\ge0`$ and $`0\le u\le m`$, $`|J_m(u)|\le e^{-m\eta(u/m)}`$ with $`\eta(z)=\mathrm{artanh}\sqrt{1-z^2}-\sqrt{1-z^2}`$, which decreases from $`\infty`$ to $`0`$ on $`(0,1]`$ and equals $`\tfrac13(2(1-z))^{3/2}(1+O(1-z))`$ near $`z=1`$. With $`|J_m|\le1`$ for the other factors, $`|\mathcal U_\infty(r,s)|\le e^{-\rho\,\eta(2t_fs/\rho)}`$ for $`2t_fs\le\rho`$; $`R\eta(c/R)`$ increases with $`R`$ (its derivative is $`\eta+\sqrt{1-z^2}>0`$).

### Step 3. The front (item 1)

**Ahead of the front.** Let $`\rho\le L/2`$ and $`2t_f\lambda<\rho`$. Every image ($`\mathbf m\ne0`$) has $`\rho_{\mathbf m}=\lVert r+L\mathbf m\rVert_\infty\ge L-\rho\ge\rho`$, so (8.1) and Step 2 give, for both switchings,

```math
|\delta\rho(r,\lambda)|\le2n\lambda\max_{\lambda'}|g_s(\lambda')|\sum_{\mathbf m}e^{-\rho_{\mathbf m}\eta(2t_f\lambda/\rho_{\mathbf m})}\qquad(2t_f\lambda<\rho\le L/2),\qquad\text{(8.5)}
```

which is exponentially small in $`\rho`$ at fixed $`2t_f\lambda/\rho<1`$; the $`\mathbf m=0`$ term dominates. For every start of the $`N_f`$ objects, at first order, $`\Delta\langle\Phi_x\rangle=-i\int_0^\lambda g_s(\lambda')\langle[\Phi^H_x(\lambda),\Phi^H_{x_s}(\lambda')]\rangle\mathrm d\lambda'`$ is a sum of one-object commutators of norm $`\le2|\mathcal U(r,\lambda-\lambda')|`$, so (8.5) holds with $`2n`$ replaced by $`2N_f`$.

**At the front, $`D=1`$.** Here $`\mathrm{Im}\mathcal U_\infty=J_r(2t_fs)\sin(r\pi/2-2t_fs)`$, and (8.1) is $`\frac{ng_s}{t_f}\int_0^{2t_f\lambda}J_r(u)\sin(\frac{r\pi}2-u)\mathrm du`$. One integration by parts leaves $`\int J_r'(u)\cos(\frac{r\pi}2-u)\mathrm du`$, which is $`O(r^{-2/3})`$ near $`u=r`$: $`J_r'=O(r^{-2/3})`$ there, and $`J_r(u)e^{\pm iu}`$ has no stationary point (the local frequency of $`J_r`$ is $`\sqrt{1-r^2/u^2}<1`$). With the Airy form $`J_r(r+\xi(r/2)^{1/3})=(2/r)^{1/3}[\mathrm{Ai}(-\xi)+O(r^{-2/3})]`$:

```math
\delta\rho(r,\lambda)=\frac{ng_s}{t_f}\Bigl[\Bigl(\frac2r\Bigr)^{1/3}\mathrm{Ai}\Bigl(\frac{r-2t_f\lambda}{(r/2)^{1/3}}\Bigr)\cos\Bigl(\frac{r\pi}2-2t_f\lambda\Bigr)+O(r^{-2/3})\Bigr]\qquad(|2t_f\lambda-r|=O(r^{1/3})).\qquad\text{(8.6)}
```

The envelope reaches $`0.6749\,(n|g_s|/t_f)\,r^{-1/3}`$ at $`2t_f\lambda=r+1.019(r/2)^{1/3}`$. **$`D>1`$.** The time-dependent part of (8.3) is $`\frac{2ng_s}{t_f}\mathrm{Re}\int\frac{\mathrm d^D\mathbf k}{(2\pi)^D}\frac{e^{i\mathbf k\cdot r-it_f\omega\lambda}}{\omega}`$; near $`\rho=2t_f\lambda`$ its stationary points are those of $`\mathcal U_\infty`$ ($`\sin k_\mu=r_\mu/(2t_f\lambda)`$), where $`\omega\ge2`$. So the change at the front is of the order $`(n|g_s|/t_f)|\mathcal U_\infty|`$: each factor with $`|r_\mu|=\rho`$ contributes $`\rho^{-1/3}`$, each other factor $`\rho^{-1/2}`$. The largest decay exponent is that of the axes, $`p_D=\frac13+\frac{D-1}2`$.

**Criterion (front).** Fix $`\varepsilon>0`$ and $`p>p_D`$. The change arrives at $`r`$ at $`\lambda_a(r)=\min\{\lambda\ge0:|\delta\rho(r,\lambda)|\ge\varepsilon\,(n|g_s|/t_f)\,\rho^{-p}\}`$, sudden switching. By (8.5), with $`2n|g_s|\lambda<n|g_s|\rho/t_f`$, the threshold is not reached while $`\rho\,\eta(2t_f\lambda/\rho)>(p+1)\ln\rho+\ln(1/\varepsilon)+o(1)`$, that is while $`1-2t_f\lambda/\rho>\frac12[3((p+1)\ln\rho+\ln(1/\varepsilon))/\rho]^{2/3}(1+o(1))`$. Within $`O(\rho^{1/3})`$ behind $`\rho=2t_f\lambda`$ the change reaches the order $`\rho^{-p_D}`$, above $`\varepsilon\rho^{-p}`$ for large $`\rho`$. Hence

```math
\lambda_a(r)=\frac{\rho}{2t_f}+O\Bigl(\frac{\rho^{1/3}(\ln\rho)^{2/3}}{t_f}\Bigr)\quad(\rho\to\infty,\ \rho\le L/2):\qquad v_f=2t_f\ \text{place labels per unit }\lambda\ \text{in }\lVert\cdot\rVert_\infty .\qquad\text{(8.7)}
```

In graph distance $`d/D\le\rho\le d`$, so $`\lambda_a\in[\frac d{2Dt_f},\frac d{2t_f}](1+o(1))`$: speed $`2t_f`$ along the axes, $`2Dt_f`$ along the diagonals. Code (ring $`L=16384`$ with $`\varepsilon=0.1`$, $`p=\frac12`$; cube $`L=160`$ along an axis with $`p=\frac32`$):
- Fitted speeds: $`2.036\,t_f`$ (ring, $`\rho=64`$–$`384`$) and $`2.06\,t_f`$ (cube, $`\rho=12`$–$`64`$).
- On the ring, $`2t_f\lambda_a/\rho`$ rises from $`0.87`$ at $`\rho=16`$ to $`0.971`$ at $`\rho=384`$, as the correction in (8.7) allows.
- Ahead of the front, $`|\delta\rho|`$ stays below $`0.02`$ of the bound (8.5).
- The front peak decays as $`\rho^{-0.340}`$ on the ring (prediction $`-\frac13`$; peak $`\times\rho^{1/3}=0.34`$–$`0.35`$ against $`0.337`$ in units $`2ng_s/t_f`$) and as $`\rho^{-1.322}`$ on the cube (prediction $`-\frac43`$).
- (8.6) deviates from the exact change by $`0.44,0.33,0.27,0.24`$ of the peak at $`r=64,128,256,384`$, decreasing like $`r^{-1/3}`$.

### Step 4. Behind the front: scaling form

Take $`L\to\infty`$ first, so that $`\mathcal U\to\mathcal U_\infty`$ and the $`\mathbf k`$-sums become integrals; then (8.3) reads $`\delta\rho=-\frac{2ng_s}{t_f}\int\frac{\mathrm d^D\mathbf k}{(2\pi)^D}\cos(\mathbf k\cdot r)\frac{1-\cos t_f\omega\lambda}{\omega}`$, convergent at $`\mathbf k=0`$ for every $`D`$. Let $`|r|\to\infty`$ at fixed $`\zeta=|r|^2/(4t_f\lambda)`$ (behind the front: $`\zeta<|r|/2`$, true for large $`|r|`$). At leading order only $`|\mathbf k|=O(1/|r|)`$ contributes, where $`\omega=\mathbf k^2(1+O(\mathbf k^2))`$: elsewhere the integrand oscillates on the scale $`1/|r|`$, and the other critical points of $`\omega`$ ($`k_\mu\in\{0,\pi\}`$) contribute $`O((t_f\lambda)^{-D/2})=O(|r|^{-D})`$, smaller by $`|r|^{-2}`$. With $`(1-e^{-ia\mathbf k^2})/\mathbf k^2=i\int_0^ae^{-ia'\mathbf k^2}\mathrm da'`$ and the Fresnel integral $`\int\frac{\mathrm d^D\mathbf k}{(2\pi)^D}e^{i\mathbf k\cdot r-ia'\mathbf k^2}=(4\pi ia')^{-D/2}e^{i|r|^2/4a'}`$:

```math
\delta\rho(r,\lambda)\simeq-\frac{2ng_s}{t_f}\mathrm{Re}W_D(|r|,it_f\lambda),\qquad W_D(r,\Theta)=\int_0^\Theta\frac{e^{-r^2/4s}}{(4\pi s)^{D/2}}\mathrm ds,\qquad\text{(8.8)}
```

continued along $`s=ia'`$, $`0\le a'\le t_f\lambda`$. Substituting $`u=r^2/4s`$, $`\partial_rW_D(r,\Theta)=-\Gamma(\frac D2,\frac{r^2}{4\Theta})/(2\pi^{D/2}r^{D-1})`$, and $`r^2/(4it_f\lambda)=-i\zeta`$. As $`\Theta\to\infty`$ the gradient of (8.8) tends to that of the long-range part $`\delta\rho^\infty_{\rm st}`$ of the static mark, $`\partial_{|r|}\delta\rho^\infty_{\rm st}=\frac{2ng_s}{t_f}\frac{\Gamma(D/2)}{2\pi^{D/2}|r|^{D-1}}`$. Hence

```math
\frac{\partial_{|r|}\delta\rho(r,\lambda)}{\partial_{|r|}\delta\rho^\infty_{\rm st}(r)}\simeq g_D(\zeta)=\frac{\mathrm{Re}\Gamma(D/2,-i\zeta)}{\Gamma(D/2)}=\begin{cases}\mathrm{Re}\mathrm{erfc}\sqrt{-i\zeta},&D=1,\\ \cos\zeta,&D=2,\\ \mathrm{Re}\bigl[\mathrm{erfc}\sqrt{-i\zeta}+2\sqrt{-i\zeta/\pi}\;e^{i\zeta}\bigr],&D=3,\end{cases}\qquad\text{(8.9)}
```

with the principal root. From $`\gamma(s,w)=w^s/s-w^{s+1}/(s+1)+\dots`$: $`1-g_1=\sqrt{2\zeta/\pi}\,(1+O(\zeta))`$, $`1-g_2=\frac{\zeta^2}2(1+O(\zeta^2))`$, $`1-g_3=-\frac{4\zeta^{3/2}}{3\sqrt{2\pi}}(1+O(\zeta))`$. For $`\zeta\gg1`$, $`g_1\to0`$, $`g_2`$ oscillates between $`\pm1`$, and $`g_3=2\sqrt{\zeta/\pi}\cos(\zeta-\pi/4)+o(1)`$: there the made field is a ripple of local wavenumber $`|r|/(2t_f\lambda)`$, not the static mark. In $`D=3`$ the value itself obeys $`\delta\rho/\delta\rho^\infty_{\rm st}\simeq\mathrm{Re}\mathrm{erfc}\sqrt{-i\zeta}=1-\sqrt{2\zeta/\pi}(1+O(\zeta))`$. Code (window before the wrap time): for $`\zeta\le0.5`$ the exact gradient ratio follows (8.9) within $`0.006`$ on the ring ($`|r|=6`$–$`40`$, $`L=16384`$), and within $`0.04`$ to $`0.008`$ on the cube along an axis ($`|r|=3`$–$`9`$, $`L=160`$), decreasing with $`|r|`$.

### Step 5. Formation of the static mark, sudden switching (item 2 (i))

**Criterion (formation).** The long-range part at distance $`|r|`$ is formed to accuracy $`\varepsilon`$ from $`\lambda_f`$ on if $`|1-\partial_{|r|}\delta\rho/\partial_{|r|}\delta\rho_{\rm st}|\le\varepsilon`$ for every $`\lambda\ge\lambda_f`$ in the regime of Step 4 ($`\delta\rho_{\rm st}`$ replaced by its long-range part $`\delta\rho^\infty_{\rm st}`$). By (8.9) this holds iff $`\zeta\le\zeta_D(\varepsilon)`$, the largest $`\zeta`$ below which $`|1-g_D|\le\varepsilon`$:

```math
\lambda_{\rm form}(|r|;\varepsilon)=\frac{|r|^2}{4t_f\,\zeta_D(\varepsilon)},\qquad \zeta_1=\frac{\pi\varepsilon^2}2\bigl(1+O(\varepsilon^2)\bigr),\quad \zeta_2=\sqrt{2\varepsilon}\bigl(1+O(\varepsilon)\bigr),\quad \zeta_3=\Bigl(\frac{3\sqrt{2\pi}\,\varepsilon}4\Bigr)^{2/3}\bigl(1+O(\varepsilon^{2/3})\bigr),\qquad\text{(8.10)}
```

independent of $`L`$. In $`D=3`$ the value at $`|r|`$ comes within $`\varepsilon`$ of $`\delta\rho^\infty_{\rm st}`$ at $`\lambda=|r|^2/(2\pi\varepsilon^2t_f)`$. In $`D=1,2`$ the level does not form on the infinite lattice: at fixed $`|r|`$, $`\mathrm{Re}W_1=\sqrt{t_f\lambda/2\pi}-|r|/2+o(1)`$ and $`\mathrm{Re}W_2=\frac1{4\pi}\bigl(\ln\frac{4t_f\lambda}{|r|^2}-\gamma_E\bigr)+o(1)`$ grow without bound. Code: on the ring ($`L=16384`$, $`\varepsilon=0.2`$, $`\zeta_1=0.0604`$ from (8.9), leading order $`0.0628`$), $`\lambda_{\rm form}`$ at $`|r|=6`$–$`40`$ lies within $`3.4\%`$ of (8.10), with fitted exponent $`1.98`$. On the cube along an axis ($`L=160`$, $`\varepsilon=0.1`$, $`\zeta_3=0.407`$, leading order $`0.328`$), it lies within $`5\%`$, with exponent $`2.03`$ and prefactor $`0.586`$ against $`1/(4\zeta_3)=0.614`$.

**The torus.** By (8.4), $`\delta\rho_L(r,\lambda)=\sum_{\mathbf m}\delta\rho_\infty(r+L\mathbf m,\lambda)`$ exactly at first order; by (8.5) the image terms are exponentially small for $`\lambda<(L-\rho)/(2t_f)`$, the wrap time. So (8.8)–(8.10) hold on the torus for $`\lambda`$ below the wrap time, and the formation (8.10) happens before it when $`|r|^2<2\zeta_D(\varepsilon)(L-\rho)`$. After it the wrapped changes add to (8.3) a part that does not decay. Only the $`\lambda`$-average converges, exactly: $`\omega(\mathbf k)>0`$ for $`\mathbf k\ne0`$ and $`\frac1\Lambda\int_0^\Lambda\cos(t_f\omega\lambda)\mathrm d\lambda=\frac{\sin t_f\omega\Lambda}{t_f\omega\Lambda}`$, so

```math
\Bigl|\frac1\Lambda\int_0^\Lambda\delta\rho(r,\lambda)\,\mathrm d\lambda-\delta\rho_{\rm st}(r)\Bigr|\le\frac{2n|g_s|}{t_f}\,\frac{S_2}{t_f\Lambda}\xrightarrow{\Lambda\to\infty}0,\qquad S_2=\frac1{|X_f|}\sum_{\mathbf k\ne0}\frac1{\omega(\mathbf k)^2}=O(L^{4-D}),\qquad\text{(8.11)}
```

since $`S_2`$ is dominated by $`|\mathbf k|=O(1/L)`$, where $`\omega^{-2}=O(L^4)`$; $`S_2=\frac{L^3}{720}(1+O(L^{-2}))`$ for $`D=1`$. The averaged field is within $`\varepsilon|\delta\rho_{\rm st}(r)|`$ for $`\Lambda\ge S_2/(\varepsilon t_f|\Lambda^+(r)|)`$: of order $`L^2/(60\varepsilon t_f)`$ ($`D=1`$, $`|r|\ll L`$, $`\Lambda^+\simeq L/12`$), $`L^2/(\varepsilon t_f\ln(L/|r|))`$ ($`D=2`$) and $`L|r|/(\varepsilon t_f)`$ ($`D=3`$). The slowest modes saturate the bound up to a factor of order one. Code (ring $`L=1024`$, units $`2ng_s/t_f`$): at $`\Lambda=1,4,16\,L^2/t_f`$ the running average of the exact evolution deviates from its $`\Lambda\to\infty`$ limit by $`1.34,0.25,0.025`$, against the bound $`1.42,0.36,0.089`$.

### Step 6. Formation, gradual switching (item 2 (ii))

Integrating (8.1) by parts in $`\lambda'`$ ($`g_s(0)=0`$), and with $`F(\nu)=\int_0^1f'(u)e^{i\nu u}\mathrm du`$:

```math
\delta\rho(r,\lambda)-\frac{g_s(\lambda)}{g_s}\delta\rho_{\rm st}(r)=\frac{2n}{t_f|X_f|}\sum_{\mathbf k\ne0}\frac{\cos(\mathbf k\cdot r)}{\omega}\int_0^\lambda g_s'(\lambda')\cos\bigl(t_f\omega(\lambda-\lambda')\bigr)\mathrm d\lambda',\qquad =\frac{2ng_s}{t_f|X_f|}\sum_{\mathbf k\ne0}\frac{\cos(\mathbf k\cdot r)}{\omega}\mathrm{Re}\bigl[e^{-it_f\omega\lambda}F(t_f\omega T)\bigr]\ (\lambda\ge T).\qquad\text{(8.12)}
```

The sudden switching is $`F\equiv1`$, which gives back (8.3). Relative to its static weight, mode $`\mathbf k`$ deviates by at most $`\min\{1,c_f/(t_f\omega T)^2\}`$ during the ramp, $`c_f=\lVert f''\rVert_\infty+\lVert f'''\rVert_1`$ (two more integrations by parts; the boundary terms vanish because $`\sin0=0`$ and $`f'(0)=f''(0)=0`$; the bound $`1`$ holds because $`f`$ is nondecreasing). After the ramp it deviates by $`|F(t_f\omega T)|\le C_m(t_f\omega T)^{-m}`$ for every $`m`$, because $`f'`$ is smooth with all derivatives zero at $`0`$ and $`1`$. So mode $`\mathbf k`$ follows iff $`t_f\omega(\mathbf k)T\gg1`$. **Criterion (following).** In the regime of Step 4, $`E_D`$ is the largest relative deviation, over $`0\le\lambda\le2T`$, of the gradient at $`|r|`$ from $`(g_s(\lambda)/g_s)\,\partial_{|r|}\delta\rho_{\rm st}`$. With $`\mathbf k=\mathbf q/|r|`$ it is a function $`E_D(\nu;f)`$ of $`\nu=|r|^2/(t_fT)`$ alone. The unfollowed modes $`|\mathbf k|\lesssim k_T=(t_fT)^{-1/2}`$ carry the relative weight $`O(\nu^{D/2})`$, and the lag of the modes $`k_T\lesssim|\mathbf k|\lesssim1/|r|`$, $`|r|\int_{k_T}\mathrm dk\,k^{D-1}(t_fk^2T)^{-2}`$ relative to $`|r|^{1-D}`$, is $`O(\nu^{D/2})`$ as well. As $`\nu\to\infty`$ the switching is sudden on the scale $`|r|`$, and $`E_D`$ tends to the deviation of (8.9) at $`\zeta\ge\nu/8`$, which is of order one. Hence, for $`T\ll L^2/t_f`$,

```math
E_D(\nu;f)=O(\nu^{D/2})\ (\nu\to0),\qquad T_{\rm form}(|r|;\varepsilon)=\frac{|r|^2}{t_f\,\nu_D(\varepsilon;f)},\qquad \nu_D\propto\varepsilon^{2/D}\quad(\varepsilon\to0),\qquad\text{(8.13)}
```

where $`\nu_D(\varepsilon;f)`$ is the largest $`\nu`$ below which $`E_D\le\varepsilon`$ (its constants depend on $`f`$); the gradient follows within $`\varepsilon`$ for every $`T\ge T_{\rm form}`$. **The whole field.** The modes $`|\mathbf k|<k_T=(t_fT)^{-1/2}`$ are not followed. In $`D=1`$ the modes $`|\mathbf k|=2\pi/L`$ alone carry the fraction $`6/\pi^2`$ of $`\Lambda^+(0)`$, so the level follows only for $`T\gtrsim L^2/(4\pi^2t_f)`$. In $`D=2`$ the unfollowed share of $`\Lambda^+(r)`$ is $`\ln(k_TL/2\pi)/\ln(L/|r|)`$ at leading logarithmic order, so the value follows to $`\varepsilon`$ for $`T\ge(L/2\pi)^2(|r|/L)^{2\varepsilon}/t_f`$. In $`D=3`$ the unfollowed share of $`1/(4\pi|r|)`$ is $`2|r|k_T/\pi`$, so $`T\ge4|r|^2/(\pi^2\varepsilon^2t_f)`$. For $`T\gg L^2/(4\pi^2t_f)`$ every mode follows. Code (ring $`L=1024`$ with $`\varepsilon=0.2`$; cube $`L=128`$ along an axis with $`\varepsilon=0.1`$): for $`\nu<0.5`$, $`E\propto\nu^{0.52}`$ on the ring and $`\nu^{1.37}`$ on the cube (predictions $`\frac12`$ and $`\frac32`$). The fitted $`T_{\rm form}`$ scales as $`|r|^{1.90}`$ ($`|r|=4`$–$`16`$) and $`|r|^{2.18}`$ ($`|r|=3`$–$`7`$).

### Step 7. Long range and finite speed (item 3)

The long-range part at distance $`|r|`$ is carried by $`|\mathbf k|\sim1/|r|`$, whose frequencies are $`t_f\omega\sim t_f/|r|^2`$; at $`\lambda=\kappa|r|/t_f`$ their phases are $`O(\kappa/|r|)\to0`$. Quantitatively: if the criterion of Step 5 held from $`\lambda_f\le\kappa|r|/t_f`$, it would hold at $`\lambda=K|r|/t_f`$ for a fixed $`K\ge\max(\kappa,1)`$. There the continuum form applies (the relevant $`|\mathbf k|=1/(2K)`$ is small) with $`\zeta=|r|/(4K)\to\infty`$. But on $`[\zeta_D(\varepsilon),\zeta]`$, $`|1-g_D|`$ exceeds $`\tfrac12`$ for large $`\zeta`$: $`g_1\to0`$, $`g_2=-1`$ at $`\zeta=\pi`$, and $`g_3`$ is unbounded. For the gradual switching, $`T=\kappa|r|/t_f`$ gives $`\nu=|r|/\kappa\to\infty`$. Hence:

```math
\text{in the class, for every fixed }\kappa>0\text{ and }\varepsilon<\tfrac12:\quad \lambda_{\rm form}(|r|;\varepsilon)>\kappa|r|/t_f\ \text{ and }\ T_{\rm form}(|r|;\varepsilon)>\kappa|r|/t_f\ \text{ for all large }|r|.\qquad\text{(8.14)}
```

The long-range part forms only on $`\lambda\propto|r|^2/t_f`$, although the front moves with the finite speed $`2t_f`$.

**Control** (wider class: field objects with more places and pair terms among them). One field object per place $`x`$, with places $`0,\dots,M-1`$ carrying truncated oscillator operators $`q_x,p_x`$, and the contract $`\sum_xp_x^2/2+\frac\kappa2\sum_{\langle xy\rangle}(q_x-q_y)^2+g_s(\lambda)q_{x_s}`$. The pair terms join neighbouring field objects, and the source couples to $`q_{x_s}`$. For states with negligible weight on the top places ($`M`$ large compared with the occupations reached), (1.9) gives the linear equations $`\ddot{\langle q_x\rangle}=-\kappa(\Lambda\langle q\rangle)_x-g_s\delta_{x,x_s}`$ for every start. For the sudden switching from $`\langle q\rangle=\langle p\rangle=0`$, the $`\mathbf k\ne0`$ part is $`-\frac{g_s}{\kappa\omega}(1-\cos\sqrt{\kappa\omega}\,\lambda)`$. The static mark $`-\frac{g_s}\kappa\Lambda^+`$ has the same long-range part as (8.2), while the $`\mathbf k=0`$ part drifts uniformly. In $`D=3`$, with $`\int\frac{\mathrm d^3\mathbf k}{(2\pi)^3}e^{i\mathbf k\cdot r}\frac{\cos ck\lambda}{k^2}=\frac{\theta(|r|-c\lambda)}{4\pi|r|}`$:

```math
\langle q\rangle(r,\lambda)-\langle q\rangle_{\mathbf k=0}(\lambda)\simeq-\frac{g_s}{4\pi\kappa|r|}\,\theta\bigl(\sqrt\kappa\,\lambda-|r|\bigr)\qquad(|r|\gg1).\qquad\text{(8.15)}
```

The long-range part forms at the front $`|r|=\sqrt\kappa\lambda`$, linearly in $`|r|`$; the largest group velocity of $`\sqrt{\kappa\omega(\mathbf k)}`$ is $`\sqrt\kappa`$. A mode follows a gradual switching iff $`\sqrt{\kappa\omega(\mathbf k)}\,T\gg1`$, and $`|\mathbf k|\sim1/|r|`$, so here the answers of items 2 and 3 differ: $`\lambda_{\rm form},T_{\rm form}\propto|r|`$.

**Control for item 1** (wider class: own terms of unbounded range). On the ring, $`C_1'=-t_f\sum_{x\ne y}|x-y|^{-\alpha}|x\rangle\langle y|`$ ($`|x-y|`$ the ring distance, $`\alpha>1`$) has the uniform lowest state. For $`t_fs\ll1`$, $`\mathrm{Im}\mathcal U(r,s)=t_fs|r|^{-\alpha}(1+O((t_fs)^2))`$ uniformly in $`r`$, since powers of a kernel decaying like $`|r|^{-\alpha}`$, $`\alpha>1`$, decay like $`|r|^{-\alpha}`$. So at a fixed small $`\lambda_1`$,

```math
\delta\rho(r,\lambda_1)=\frac{n\,g_s\,t_f\lambda_1^2}{|r|^{\alpha}}\bigl(1+O((t_f\lambda_1)^2)\bigr),\qquad\text{(8.16)}
```

which exceeds the front threshold $`\varepsilon(n|g_s|/t_f)\rho^{-p}`$ for all large $`\rho`$ when $`p>\alpha`$. The arrival time stays bounded, and the change ahead of any line $`\lambda=\rho/v`$ is only power-law small. There is no finite front speed.

### Step 8. Speeds (item 4)

The motion term of a Model D body is, in $`k`$-space, $`A(k)=-\tau\sin k\,\sigma_1\otimes\mathbb 1_N`$, with group velocities $`\mp\tau\cos k`$, largest $`\tau`$. Its propagator has the entries $`J_r(\tau\lambda)`$ (Jacobi–Anger with $`\sin k`$), so the body's own front is at $`|x|=\tau\lambda`$ with the bound of Step 2; with the rest and clock term the bands are $`\pm\sqrt{\tau^2\sin^2k+m_a^2}`$, $`m_a>0`$ the levels of $`m\mathbb 1_N+D`$, and their group velocities are smaller than $`\tau`$. The body's position label is the field place of the couplings ($`\sum_x|x\rangle\langle x|\otimes G\otimes\Phi_x`$), along one axis of $`X_f`$. With (8.7):

```math
\frac{v_f}{\tau}=\frac{2t_f}{\tau},\qquad\text{a body moves more slowly than the front of the field iff }\ \tau<2t_f .\qquad\text{(8.17)}
```

## Result

Class: the field class of the setup ($`N_f\ge1`$, $`D=1,2,3`$, torus of even side $`L`$), source at $`x_s`$, start in the lowest state; first order in $`g_s`$ unless stated.

- **(8.1)** Exactly, $`\langle\Phi_x\rangle_\lambda=N_f|\psi(x,\lambda)|^2`$: the made field of $`N_f`$ objects is $`N_f`$ times that of one, at every order. At first order $`\delta\rho`$ is the time integral (8.1) of the free propagator, for either switching.
- **(8.2)** The static mark is $`-(2ng_s/t_f)\Lambda^+(r)`$.
- **(8.3)** Sudden switching, $`\lambda\ge0`$: $`\delta\rho=\delta\rho_{\rm st}+(2ng_s/t_f)R`$. On the torus $`R`$ is a finite sum of cosines and does not decay.
- **(8.4)** The propagator is the image sum of products of Bessel functions, with $`|\mathcal U_\infty|\le e^{-\rho\eta(2t_fs/\rho)}`$ for $`2t_fs\le\rho`$.
- **(8.5)** Item 1, change ahead of the front: for $`2t_f\lambda<\rho\le L/2`$, $`|\delta\rho|\le2n\lambda\max|g_s|\sum_{\mathbf m}e^{-\rho_{\mathbf m}\eta(2t_f\lambda/\rho_{\mathbf m})}`$. This is exponentially small in $`\rho`$ at fixed $`2t_f\lambda/\rho<1`$, for both switchings, and holds for every start with $`2N_f`$ in place of $`2n`$.
- **(8.6)** Item 1, change at the front: for $`D=1`$, at leading order in $`r`$ and for $`|2t_f\lambda-r|=O(r^{1/3})`$, an Airy envelope of maximum $`0.6749\,(n|g_s|/t_f)\,r^{-1/3}`$. Along an axis in $`D`$ dimensions the change at the front is of order $`\rho^{-1/3-(D-1)/2}`$.
- **(8.7)** Item 1: the front speed is finite. With the criterion $`|\delta\rho|\ge\varepsilon(n|g_s|/t_f)\rho^{-p}`$, $`p>\frac13+\frac{D-1}2`$, the sudden switching gives $`\lambda_a=\rho/(2t_f)+O(\rho^{1/3}(\ln\rho)^{2/3}/t_f)`$ as $`\rho\to\infty`$, $`\rho\le L/2`$. The speed is $`v_f=2t_f`$ place labels per unit $`\lambda`$ in $`\lVert\cdot\rVert_\infty`$: $`2t_f`$ along the axes in graph distance, $`2Dt_f`$ along the diagonals.
- **(8.8), (8.9)** Behind the front ($`L\to\infty`$ first; $`|r|\to\infty`$ at fixed $`\zeta=|r|^2/(4t_f\lambda)`$; leading order) the made field is $`-(2ng_s/t_f)\mathrm{Re}W_D(|r|,it_f\lambda)`$. Its gradient is $`g_D(\zeta)=\mathrm{Re}\Gamma(D/2,-i\zeta)/\Gamma(D/2)`$ times that of the long-range static part.
- **(8.10)** Item 2 (i), sudden switching. The long-range part (the gradient) at distance $`|r|`$ is formed to accuracy $`\varepsilon`$ from $`\lambda_{\rm form}=|r|^2/(4t_f\zeta_D(\varepsilon))`$, with $`\zeta_1=\frac{\pi\varepsilon^2}2(1+O(\varepsilon^2))`$, $`\zeta_2=\sqrt{2\varepsilon}(1+O(\varepsilon))`$, $`\zeta_3=(3\sqrt{2\pi}\varepsilon/4)^{2/3}(1+O(\varepsilon^{2/3}))`$. This scale is independent of $`L`$ and holds on the torus up to the wrap time $`(L-\rho)/(2t_f)`$. In $`D=3`$ the value at $`|r|`$ forms at $`|r|^2/(2\pi\varepsilon^2t_f)`$ (relative to $`\delta\rho^\infty_{\rm st}`$). In $`D=1,2`$ the level grows without bound on the infinite lattice.
- **(8.11)** Item 2 (i), $`\lambda`$-average on the torus. The running average of $`\delta\rho`$ tends to $`\delta\rho_{\rm st}`$, with error at most $`(2n|g_s|/t_f)S_2/(t_f\Lambda)`$, $`S_2=O(L^{4-D})`$. It is within $`\varepsilon|\delta\rho_{\rm st}(r)|`$ for $`\Lambda\ge S_2/(\varepsilon t_f|\Lambda^+(r)|)`$, of order $`L^2/(60\varepsilon t_f)`$, $`L^2/(\varepsilon t_f\ln(L/|r|))`$ and $`L|r|/(\varepsilon t_f)`$ for $`D=1,2,3`$. The instantaneous field does not converge as $`\lambda\to\infty`$, since $`R`$ is a nonconstant finite sum of cosines.
- **(8.12)** Gradual switching: the first-order deviation from the adiabatic target $`(g_s(\lambda)/g_s)\delta\rho_{\rm st}`$. Per mode it is at most $`\min\{1,c_f/(t_f\omega T)^2\}`$ during the ramp and at most $`C_m(t_f\omega T)^{-m}`$ after it.
- **(8.13)** Item 2 (ii). For $`T\ll L^2/t_f`$, at leading order, the gradient at $`|r|`$ follows the static one within $`\varepsilon`$ on $`[0,2T]`$ for every $`T\ge T_{\rm form}=|r|^2/(t_f\nu_D(\varepsilon;f))`$, with $`\nu_D\propto\varepsilon^{2/D}`$ as $`\varepsilon\to0`$ and deviation $`O((|r|^2/t_fT)^{D/2})`$. The whole field follows for $`T\gg L^2/(4\pi^2t_f)`$. The level needs $`T\gtrsim L^2/(4\pi^2t_f)`$ in $`D=1`$, and the value at $`|r|`$ needs $`T\ge(L/2\pi)^2(|r|/L)^{2\varepsilon}/t_f`$ in $`D=2`$ (leading logarithmic order) and $`T\ge4|r|^2/(\pi^2\varepsilon^2t_f)`$ in $`D=3`$.
- **(8.14)** Item 3, negative. In the class, at first order (with $`L\to\infty`$ first, or before the wrap time), the long-range part does not form on any scale linear in $`|r|`$. For every fixed $`\kappa>0`$ and $`\varepsilon<\frac12`$, $`\lambda_{\rm form}`$ and $`T_{\rm form}`$ exceed $`\kappa|r|/t_f`$ for all large $`|r|`$; the long-range part forms on $`|r|^2/t_f`$.
- **(8.15)** Control for items 2 and 3, in a wider class: field objects with more places and nearest-neighbour pair terms (harmonic lattice, $`D=3`$, coupling to $`q_{x_s}`$). For every start with zero means and $`M`$ large, the long-range part forms at the front $`|r|=\sqrt\kappa\lambda`$, linearly in $`|r|`$.
- **(8.16)** Control for item 1, in a wider class: own term with hopping $`\propto|x-y|^{-\alpha}`$, $`\alpha>1`$, on the ring. At fixed small $`\lambda_1`$ the change is $`ng_st_f\lambda_1^2|r|^{-\alpha}`$; for $`p>\alpha`$ the arrival time stays bounded, so there is no finite front speed.
- **(8.17)** Item 4: $`v_f/\tau=2t_f/\tau`$. A body moving along an axis of the field moves more slowly than the front iff $`\tau<2t_f`$ (both in place labels per unit $`\lambda`$).

## Consistency checks

1. **Static limit.** The $`\lambda`$-average (8.11) gives (8.2), and $`\Theta\to\infty`$ in the gradient of (8.8) gives the gradient of its long-range part. By Hellmann–Feynman ($`\partial E/\partial g_2=\langle\Phi_{x_2}\rangle`$), $`M^{(2)}(x_1,x_2)=g_2\,\delta\rho_{{\rm st},1}(x_2)`$, which is (4.4) of 06-ilang-source/04-profile. The gradient limit of (8.9) is the $`d`$-dependence of (4.4) of 07-ilang-weight/04-weight-of-bond: $`-\ln|r|/2\pi`$ for $`D=2`$, $`1/(4\pi|r|)`$ for $`D=3`$. Code: the exact $`\lambda\to\infty`$ average differs from $`-\Lambda^+`$ by $`1.1\cdot10^{-3}`$ (ring) and $`3.7\cdot10^{-4}`$ (cube) of $`|\Lambda^+(0)|`$, the $`O(g_s)`$ second order. Passed.
2. **Sum rule.** $`\sum_x\delta\rho(x,\lambda)=0`$ at every $`\lambda`$, from (8.3) ($`\sum_r\cos\mathbf k\cdot r=0`$ for $`\mathbf k\ne0`$), as $`\sum_{x_2}M^{(2)}=0`$ in (4.4). Code: $`|\sum_x\delta\rho|\le9\cdot10^{-11}`$ in units $`2ng_s/t_f`$. Passed.
3. **Dimensions.** $`g_s`$, $`t_f`$ and $`\tau`$ have the units of $`C`$, and $`\lambda`$ the inverse units. $`\delta\rho`$, $`g_s/t_f`$, $`t_f\lambda`$, $`\zeta`$ and $`\nu`$ are numbers; $`v_f`$ and $`\tau`$ are place labels per unit $`\lambda`$; the scales (8.10), (8.13) are $`\propto|r|^2/t_f`$. Passed.

## Open issues

- On the torus, the size of the wrapped changes after the wrap time is not derived for the sudden switching; the instantaneous formation statements hold up to the wrap time, or with $`L\to\infty`$ first.
- The constants $`\nu_D(\varepsilon;f)`$ of (8.13) are not given in closed form, and $`D=2`$ is not checked numerically (the code covers the ring and the cube, as the question requires).
- Second order in $`g_s`$, and starts other than the lowest state: only (8.5) is derived for every start.
- Since the long-range part forms only on $`|r|^2/t_f`$, it is open how far out the long-range mark of a moving body is formed. Moving sources are out of scope.
- The meaning of (8.17) rests on identifying the body's position label with the field place along an axis. The relation to the distances of 03-ilang-space is out of scope.
- Whether a field with linear long-wavelength frequencies, as in (8.15), is selected by anything in the language is item 5, and is not addressed (M10).

## Code

- `code/v1/check_front_formation.py` (role: check). It evolves one field object ($`N_f=1`$, which suffices by (8.1)) exactly from its lowest state, with the source switched on suddenly and gradually ($`f`$ the $`C^\infty`$ step $`e^{-1/u}/(e^{-1/u}+e^{-1/(1-u)})`$). The evolution runs in the sector invariant under the point group of the torus fixing $`x_s`$, which the state never leaves. Constant contracts are propagated by Chebyshev expansion, which agrees with dense diagonalization to $`2\cdot10^{-15}`$ (cube $`L=16`$). The ramp uses the exponential midpoint rule with step $`0.2/t_f`$; a step of $`0.05/t_f`$ changes the gradient by $`5\cdot10^{-5}`$ relative. Lattices: rings $`L=1024`$, $`16384`$; cubic tori $`L=32`$, $`128`$, $`160`$. Couplings: $`g_s/t_f=10^{-5}`$ (ring), $`10^{-3}`$ (cube); the exact evolution differs from (8.3) by $`3.7\cdot10^{-5}`$ and $`7.9\cdot10^{-4}`$ of $`|\Lambda^+(0)|`$. It checks (8.3), (8.5)–(8.7), (8.9)–(8.11) and (8.13), with the fits quoted in Steps 3–6.
- Outputs: `code/v1/output/check_front_formation.json` (all numbers) and `code/v1/output/check_front_formation.log` (run log).

## Methods used

- Reduction of non-interacting identical objects to one object; first-order Dyson expansion; Hellmann–Feynman
- Fourier analysis on tori, Poisson summation, Jacobi–Anger expansion
- Kapteyn's inequality, Airy asymptotics of Bessel functions, stationary phase
- Fresnel–Gaussian integrals, analytic continuation of the integrated heat kernel, incomplete Gamma function
- Integration by parts in time (adiabatic following), Riemann–Lebesgue decay of smooth ramps
- Ehrenfest equations of a quadratic contract (control)
- Numerical check: exact evolution in the symmetric sector, Chebyshev propagation, exponential midpoint rule
