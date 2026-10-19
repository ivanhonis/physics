# Weight and fall of a body with its own mark in the field of a held source

- **Subproject:** 06-ilang-source
- **Package:** 07-dressed-fall
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-19

## Changes from previous version

- Setup: (6.4) of 06-own-mark is quoted in full (dated note of the question), replacing the sufficient inequality for $`\sigma=+`$ (I3).
- Step 5: Regime R rewritten. R1 is now a self-contained isolation gap $`\delta_{k,\sigma}`$ of the band, derived from (6.4), with a smallness condition on the coupling, and a stated class of starts. R2 is now the coefficient of $`\tau^2`$ of a sequential expansion, with the two independent small-motion conditions (I1, I2, I3).
- Step 5: (7.7) is now the exact acceleration of the projected lattice contract at order $`\tau^2`$, with the envelope sum $`\sum_j\phi_{j+1}\phi_{j-1}W'(j)`$. It replaces the local Ehrenfest form $`-E''W'(x_0)`$. The central slope is now derived, from the hops by two places of the band, and is no longer read from (5.7) (I1).
- Step 6: $`W'`$ is evaluated at every place of the packet and averaged. In (7.8) and (7.9) this adds the factor $`c_\phi`$ and the packet term $`12s_\phi^2`$ in the geometric factor, and (7.8) gets the remainder $`O(\tau^4\gamma g_s)`$ (I1, I2).
- Result (7.7)–(7.9), consistency check 2, Open issues, Code: changed accordingly. `check_weight.py` adds a check of (7.7) and (7.8) for packets.

## Response to verification

- I1: Accepted and fixed in Steps 5 and 6. The acceleration is now derived exactly for the projected lattice contract at order $`\tau^2`$ and first order in $`g_s`$, (7.7). It keeps the packet-dependent force average: the factor $`c_\phi=\langle\cos2\hat P\rangle`$ and the variance term $`12s_\phi^2`$ in (7.8) and (7.9). No width approximation is used.
- I2: Accepted and fixed in Step 5 (R2) and (7.8). The result is stated as the coefficient of $`\tau^2`$, with remainder $`O(\tau^4\gamma g_s)`$, and with the conditions $`\tau\ll M_k`$ and $`\tau^2\ll M_k\delta_{k,\sigma}`$, named as independent.
- I3: Accepted and fixed in Step 5 (R1), using (6.4) as now quoted. R1 gives the gap $`\delta_{k,\sigma}`$ for both branches and every $`P`$, and the smallness of the coupling and the source against it.

## Setup and assumptions

**Description (assumptions of the package, M8, M9).**
- *Field.* $`N_f\ge1`$ identical field objects ($`c=+1`$) on the ring $`\mathbb Z_L`$, $`L\ge5`$, no pair terms among them, own term $`C_1=-t_f\sum_x(\lvert x\rangle\langle x+1\rvert+\lvert x+1\rangle\langle x\rvert)`$, $`t_f>0`$; $`\Phi_x`$ the number of field objects at $`x`$, $`n=N_f/L`$. With $`\Lambda`$ the ring Laplacian, $`C_1=-2t_f+t_f\Lambda`$; $`G:=\Lambda^+`$, and $`\omega_{\min}=4\sin^2(\pi/L)`$ is the smallest nonzero eigenvalue of $`\Lambda`$. *State:* the lowest state adapted to the bodies present.
- *Source.* A held body (A15) at $`x_s`$, in an eigenvector of its coupled operator with eigenvalue $`g_s`$: pair term $`g_s\Phi_{x_s}`$.
- *Body.* Model D on the same ring, level $`k`$ with half-gap $`M_k=m+d_k>0`$, branch $`\sigma=\pm1`$, coupling (a) or (c) as in (6.2) of 06-own-mark. Records at $`\kappa\to0`$. Its own change of the field is kept.
- *Shorthand.* $`g_b:=\sigma\gamma M_k`$; $`P_y:=\lvert y\rangle\langle y\rvert`$; $`r:=(x-x_s)\bmod L\in\{0,\dots,L-1\}`$, $`u(x):=r(L-r)`$; $`G_0:=G(x,x)`$; for a function $`f`$ on the ring, $`f'(x_0):=\frac12[f(x_0+1)-f(x_0-1)]`$ (central lattice slope).
- *Weakness (W).* $`|g_b|+|g_s|<t_f\omega_{\min}/2`$. All expansions at fixed $`L,N_f,t_f,M_k`$.
- *Regime R* of item 2: stated in Step 5.

**Inputs (quoted in question.md).**
- (4.2) of 04-profile: $`E(g)=N_f\varepsilon_0(g)`$ for the field with held point terms. (4.4) of 04-profile: $`M^{(2)}(x_1,x_2)=-\frac{2ng_1g_2}{t_f}\Lambda^+(x_1,x_2)`$.
- (5.8) of 05-made-field-scale: $`\delta N(y)=-\frac{2ng_s}{t_f}\Lambda^+(y,x_s)+O(N_fg_s^2/(t_f^2\omega_{\min}^2))`$. (5.7): $`a_{k,\sigma}(0)=-\tau_{\rm loc}(x_0)^2\gamma N'(x_0)/\nu(x_0)`$, $`\nu=1+\gamma N_\varphi`$, $`\tau_{\rm loc}=\tau`$ (a), $`\tau\nu`$ (c). Its second form, with $`r\propto\nu`$, reads $`N'`$ as the central slope; we use the same slope throughout.
- (6.2) of 06-own-mark: the total contract on level $`k`$ for (a) and (c). (6.7): $`E_{k,\sigma}(P)|_{\tau=0}=\sigma M_k+N_f\varepsilon_0(\sigma\gamma M_k)`$. (6.10): $`E''_{k,\sigma}(0)=\sigma\frac{\tau^2}{M_k}(1-\gamma n+\gamma^2n^2)`$ (a), $`\sigma\frac{\tau^2}{M_k}(1+\gamma n)`$ (c), $`+\Delta''_{k,\sigma}+O(\gamma^3)`$, $`\Delta''_{k,\sigma}=O(\gamma^2)`$. (6.4): with $`\omega_k(p)=\sqrt{M_k^2+\tau^2\sin^2p}`$, the start $`(P,\sigma,k)`$ is a simple eigenvalue of its sector at $`\gamma=0`$ iff $`\sigma\omega_k(P)\ne\sigma'\omega_k(P-Q)+E_{\rm exc}`$ for every excited field eigenstate $`(Q,E_{\rm exc})`$ and $`\sigma'=\pm`$.

## Derivation

### Step 1. The held body is an exactly decoupled block

For $`\tau=0`$ the motion term vanishes, and the extra term of (c) in (6.2) is proportional to $`\tau`$; (a) and (c) give the same total contract. Every remaining term is diagonal in the body's position label and commutes with $`\sigma_3`$ and with $`D`$, and the source stays on its eigenvector. The total contract therefore leaves invariant the block of body place $`x`$, branch $`\sigma`$ and level $`k`$, and on it acts as $`\sigma M_k+c_s+\sum_{j=1}^{N_f}h_x^{(j)}`$, with $`c_s`$ the source's own constant and

```math
h_x:=C_1+g_bP_x+g_sP_{x_s}.
\qquad\text{(7.1)}
```

The field objects are identical with $`c=+1`$ and no pair terms among them, so the lowest field eigenvalue is $`N_f\varepsilon_0(x)`$, with $`\varepsilon_0(x)`$ the lowest eigenvalue of $`h_x`$ ((4.2) of 04-profile). At $`g_b=g_s=0`$ it is $`-2t_f`$, simple, with gap $`t_f\omega_{\min}`$. Under (W), $`\lVert h_x-C_1\rVert<t_f\omega_{\min}/2`$, so it stays simple and isolated and is analytic in $`(g_b,g_s)`$ (analytic perturbation theory). It is the eigenvalue connected to the body with the field in its lowest state. Hence, exactly for $`\tau=0`$ and both couplings,

```math
W_{k,\sigma}(x)-W_{k,\sigma}(x')=N_f\bigl[\varepsilon_0(x)-\varepsilon_0(x')\bigr],\qquad \varepsilon_0(x)=\min\mathrm{spec}h_x .
\qquad\text{(7.2)}
```

At $`g_s=0`$ this eigenvalue is $`\sigma M_k+N_f\varepsilon_0(\sigma\gamma M_k)`$, which is (6.7).

### Step 2. Expansion to first order in $`g_s`$, through $`g_b^2`$

A rotation of the ring maps $`h_x`$ to $`h_{x'}`$ when only one of the two point terms is present, so $`\varepsilon_0(x)`$ depends on $`x`$ only through the mixed coefficients $`g_b^ag_s^c`$, $`a,c\ge1`$. At first order in $`g_s`$ and through $`g_b^2`$ these are $`g_bg_s`$ and $`g_b^2g_s`$. We use Rayleigh–Schrödinger theory with $`\phi_0=L^{-1/2}\sum_y\lvert y\rangle`$, $`V=g_bP_x+g_sP_{x_s}`$ and reduced resolvent $`R=Q(-2t_f-C_1)^{-1}Q=-G/t_f`$. The standard formulas are $`E^{(2)}=\langle VRV\rangle`$ and $`E^{(3)}=\langle VRVRV\rangle-\langle V\rangle\langle VR^2V\rangle`$, and $`\langle\phi_0\rvert P_yXP_{y'}\lvert\phi_0\rangle=X(y,y')/L`$. Then:
- $`g_bg_s`$ comes from $`2\langle P_xRP_{x_s}\rangle=-\frac{2}{Lt_f}G(x,x_s)`$;
- $`g_b^2g_s`$ comes from the three orderings in $`\langle VRVRV\rangle`$, $`\frac{1}{Lt_f^2}[2G_0G(x,x_s)+G(x,x_s)^2]`$, and from $`-\frac{1}{L^2t_f^2}[(G^2)(x,x)+2(G^2)(x,x_s)]`$. Both $`G_0`$ and $`(G^2)(x,x)`$ are independent of $`x`$.

Multiplying by $`N_f`$:

```math
W_{k,\sigma}(x)=\text{const}-\frac{2ng_sg_b}{t_f}G(x,x_s)+\frac{ng_sg_b^2}{t_f^2}\Bigl[2G_0\,G(x,x_s)+G(x,x_s)^2-\frac2L(G^2)(x,x_s)\Bigr]+R_W,
\qquad\text{(7.3)}
```

with $`R_W=O(g_s^2)+O(g_sg_b^3)`$. The coefficients of $`R_W`$ are bounded by $`N_f`$ times powers of $`1/(t_f\omega_{\min})`$ (Cauchy estimates on the polydisc of analyticity, where $`|\varepsilon_0+2t_f|\le|g_b|+|g_s|`$). The $`g_bg_s`$ term is $`M^{(2)}(x,x_s)`$ of (4.4) of 04-profile with $`g_1=g_b`$, $`g_2=g_s`$.

### Step 3. Closed form on the ring

$`G(\cdot,x_s)`$ is the zero-sum solution of $`\Lambda f=\delta_{x_s}-1/L`$, and $`(G^2)(\cdot,x_s)`$ the zero-sum solution of $`\Lambda f=G(\cdot,x_s)`$ (since $`\Lambda G=\mathbb 1-J/L`$ and $`GJ=0`$, with $`J`$ the all-ones matrix). Write $`\Delta^2f(r)=f(r+1)+f(r-1)-2f(r)`$.
- As polynomials in $`r`$, $`\Delta^2u=-2`$ and $`\Delta^2u^2=2L^2+2-12u`$. These hold for $`r=1,\dots,L-1`$, where the periodic values $`u(0)=u(L)=0`$ agree with the polynomial.
- At $`r=0`$, $`f(-1)=f(1)`$.
- $`\sum_rr(L-r)=L(L^2-1)/6`$.

These give

```math
G(x,x_s)=G_0-\frac{u}{2L},\quad G_0=\frac{L^2-1}{12L},\qquad (G^2)(x,x_s)=c_L-\frac{u}{12L}-\frac{u^2}{24L},
\qquad\text{(7.4)}
```

with $`c_L`$ independent of $`x`$. Check at $`r=0`$: $`2f(0)-2f(1)`$ equals $`1-1/L`$ for $`G`$, and $`\frac{L-1}{6L}+\frac{(L-1)^2}{12L}=G_0`$ for $`G^2`$. Inserting (7.4) into (7.3) and collecting powers of $`u`$ (coefficient of $`u`$: $`\frac{1}{6L^2}-\frac{2G_0}{L}=-\frac{L^2-2}{6L^2}`$; of $`u^2`$: $`\frac1{4L^2}+\frac1{12L^2}=\frac1{3L^2}`$) gives

```math
W_{k,\sigma}(x)-W_{k,\sigma}(x')=\frac{ng_sg_b}{Lt_f}\Bigl[\Bigl(1-\frac{(L^2-2)\,g_b}{6Lt_f}\Bigr)(u-u')+\frac{g_b}{3Lt_f}\,(u^2-u'^2)\Bigr]+R_W,\qquad g_b=\sigma\gamma M_k,
\qquad\text{(7.5)}
```

where $`u'=u(x')`$. `code/v2/check_weight.py` confirms (7.4) to $`6\times10^{-15}`$, (7.3)$`=`$(7.5) and (7.5) against the exact (7.2) (section "Code").

### Step 4. Factorization of the weight

With $`\gamma\,\delta N=-\frac{2n\gamma g_s}{t_f}G(\cdot,x_s)`$ from (5.8), (7.5) reads

```math
W_{k,\sigma}(x)-W_{k,\sigma}(x')=\sigma M_k\,\gamma\bigl[\delta N(x)-\delta N(x')\bigr]+M_k^2\gamma^2\bigl[\Theta(x)-\Theta(x')\bigr]+R_W,\qquad \Theta:=\frac{ng_s}{3L^2t_f^2}\Bigl(u^2-\frac{L^2-2}{2}\,u\Bigr).
\qquad\text{(7.6)}
```

- *First order in $`\gamma`$.* The weight is one function of the place, $`\gamma\,\delta N(x)`$, times the factor $`\sigma M_k`$. This factor is the eigenvalue of the coupled operator $`\sigma_3\otimes(m\mathbb 1_N+D)`$ on the level and branch, i.e. the body's rest-and-clock cost. This is the weight of a test body in the made field.
- *Second order in $`\gamma`$.* The factor is $`M_k^2`$, the same for both branches, and $`\Theta`$ is not affine in $`\delta N`$: $`\delta N`$ is affine in $`u`$, $`\Theta`$ has the $`u^2`$ coefficient $`\frac{ng_s}{3L^2t_f^2}\ne0`$, and $`1,u,u^2`$ are linearly independent functions on the ring for $`L\ge4`$ (the distances $`0,1,2`$ give the distinct values $`0`$, $`L-1`$, $`2(L-2)`$ of $`u`$). In (7.5) the ratio of the $`u^2`$ to the $`u`$ coefficient is $`\frac{g_b}{3Lt_f}+O(g_b^2)`$, fixed by the orders $`\gamma,\gamma^2`$ alone. Two pairs $`(k,\sigma)`$ with different $`g_b`$ therefore have different place dependences at relative order $`\gamma`$. The two branches of every level always differ ($`g_b=\pm\gamma M_k`$, $`M_k>0`$, $`\gamma\ne0`$), and so do two levels with $`M_k\ne M_{k'}`$. Through second order in $`\gamma`$ the level enters only through $`\sigma M_k`$, but as a change of the shape of the place dependence, not as a factor.
- *Origin.* By Hellmann–Feynman, $`\partial_{g_s}N_f\varepsilon_0|_{g_s=0}=N_f\lvert\phi_0(x_s;g_b,x)\rvert^2`$, the field made by the body itself at the source's place. The $`\gamma^2`$ term is the nonlinearity of this made field in the body's coupling, i.e. the body's own mark.
- *Class and control (M9).* The second-order statement holds for every member of the class (it requires $`g_s\ne0`$, $`\gamma\ne0`$); there is no control in the class. Control for the first-order factor: a body coupled by $`\sigma_3\otimes\mathbb 1_N`$ in place of $`\sigma_3\otimes(m\mathbb 1_N+D)`$ has $`g_b=\sigma\gamma`$ and the factor $`\sigma`$, not $`\sigma M_k`$.

### Step 5. Regime R and the projected lattice acceleration

**Regime R (assumption of the package).**
- **R1 (isolated band).** At $`\gamma=g_s=0`$ the band of the start, $`\sigma\omega_k(P)`$ for all $`P`$ with the field in its lowest state, lies at distance at least $`\delta_{k,\sigma}`$ from the rest of the spectrum on level $`k`$, where
  ```math
  \delta_{k,-}=\min(t_f\omega_{\min}-\eta_k,\,2M_k),\qquad \delta_{k,+}=\min(t_f\omega_{\min}-\eta_k,\,2M_k-4t_fN_f),\qquad \eta_k:=\sqrt{M_k^2+\tau^2}-M_k\le\frac{\tau^2}{2M_k}.
  ```
  The reason is that every excited field eigenstate has $`t_f\omega_{\min}\le E_{\rm exc}\le4t_fN_f`$ (lowest: one object moved to $`q=\pm2\pi/L`$; highest: every object at the top of its band, $`\le2t_f`$), and that $`M_k\le\omega_k\le M_k+\eta_k`$. Same-branch states with an excited field therefore lie at distance $`\ge t_f\omega_{\min}-\eta_k`$, and other-branch states at distance $`\ge2M_k`$ ($`\sigma=-`$) or $`\ge2M_k-4t_fN_f`$ ($`\sigma=+`$). $`\delta_{k,\sigma}>0`$ implies (6.4) for every $`P`$.
  - *Assumption:* $`\delta_{k,\sigma}>0`$, i.e. $`\eta_k<t_f\omega_{\min}`$ (sufficient: $`\tau^2<2M_kt_f\omega_{\min}`$), and for $`\sigma=+`$ also $`2t_fN_f<M_k`$.
  - *Assumption:* $`N_f\bigl(|\gamma|(M_k+\tau)+|g_s|\bigr)<\delta_{k,\sigma}/2`$. The left side bounds the norm of the coupling and source terms of (6.2) and of $`g_s\Phi_{x_s}`$, since $`\lVert\Phi_x\rVert=N_f`$.
  - *Consequence:* the Neumann series of the resolvent converges on a contour at distance $`\delta_{k,\sigma}/2`$ around the band. The spectral projector $`\Pi`$ of the $`L`$ eigenvalues of the band is therefore analytic in $`\gamma,g_s`$, and analytic in $`\tau`$ near $`0`$. $`C`$ commutes with $`\Pi`$, so a start in $`{\rm ran}\,\Pi`$ stays there, and no transitions out of the level occur.
- **Start (assumption, M9).** $`\Psi=\sum_j\phi_j\lvert j\rangle\!\rangle`$, where $`\lvert j\rangle\!\rangle\in{\rm ran}\,\Pi`$ is the image under Kato's transformation from $`\tau=0`$ of the held state $`\lvert j,\sigma,k\rangle\otimes\lvert\Omega_j\rangle`$ of Step 1, with $`\Omega_j`$ the lowest field state with the body at $`j`$.
  - The envelope $`\phi`$ is real, nonnegative and symmetric about a place $`x_0\ne x_s`$. It is supported on an arc of at most $`L-4`$ consecutive places that does not contain $`x_s`$, and it has $`c_\phi:=\sum_j\phi_{j+1}\phi_{j-1}>0`$. This class is nonempty for $`L\ge7`$. (7.7) below uses only that $`\phi`$ is real and the condition on its support.
  - The position $`X`$ of the body is counted from a cut that has two places outside the arc on each side. $`s_\phi^2:=c_\phi^{-1}\sum_j\phi_{j+1}\phi_{j-1}(j-x_0)^2\ge0`$, with $`j-x_0`$ counted along the arc.
- **R2 (sequential expansion in $`\tau`$).** The acceleration is computed at first order in $`g_s`$, as the coefficient of $`\tau^2`$ of its expansion at $`\tau=0`$. At this order the field follows the body: the dressed states carry the cloud $`\Omega_j`$ of the held body.
  - The remainder is $`O(\tau^4\gamma g_s)`$. It vanishes at $`\gamma=0`$, where the body is uncoupled, and it is not computed.
  - The part of $`a`$ that does not depend on $`g_s`$ is not part of the result. It vanishes through order $`\tau^4`$ for this support, because $`H^{(0)}`$ (below) is a constant at $`g_s=0`$ and $`\langle[K,[K,\hat x]]\rangle=0`$. Beyond that order, the dressed tails of the envelope reach the cut.
  - The energy denominators of the expansion are the branch gap $`\approx2M_k`$ and the isolation gap $`\delta_{k,\sigma}`$. The $`\tau^2`$ term therefore describes the acceleration only when $`\tau\ll M_k`$ and $`\tau^2\ll M_k\delta_{k,\sigma}`$. Neither condition implies the other.

**Acceleration.** By (1.9), $`a_{k,\sigma}(0):=\frac{\mathrm d^2}{\mathrm d\lambda^2}\langle\Psi\vert X\vert\Psi\rangle\big|_{\lambda=0}=-\langle\Psi\vert[C,[C,X]]\vert\Psi\rangle`$. Since $`[C,\Pi]=0`$, only $`\Pi C\Pi`$ and $`\Pi X\Pi`$ enter. In the orthonormal basis $`\lvert j\rangle\!\rangle`$:
- $`\Pi C\Pi=H^{(0)}+\tau^2H^{(2)}+O(\tau^4)`$, with $`H^{(0)}=\text{const}+W_{k,\sigma}(\hat x)`$ by Step 1. There is no term of first order, because $`A`$ (and the extra term of (c)) changes the branch.
- $`\Pi X\Pi=\hat x+\tau^2X^{(2)}+O(\tau^4)`$, with $`\hat x\lvert j\rangle\!\rangle=j\lvert j\rangle\!\rangle`$. There is no term of first order, because $`X`$ does not change the branch.
- $`H^{(2)}`$ and $`X^{(2)}`$ connect $`j`$ only to $`j`$ and $`j\pm2`$, because each factor of the motion term (and of the extra term of (c)) moves the body by one place.

Since $`[H^{(0)},\hat x]=0`$, the $`\tau^2`$ coefficient is $`-\langle[W,[H^{(2)},\hat x]]\rangle-\langle[W,[W,X^{(2)}]]\rangle`$.
- The second term has matrix elements $`(W(j)-W(j'))^2X^{(2)}_{jj'}=O(g_s^2)`$.
- In the first term, the $`O(g_s)`$ part of $`\tau^2H^{(2)}`$ gives $`O(g_s^2)`$ for the same reason. What remains is the source-free part $`K`$. It commutes with the joint translation $`\mathcal T\lvert j\rangle\!\rangle=\lvert j+1\rangle\!\rangle`$ and has displacements $`0,\pm2`$ only. With $`E(P)=E(-P)`$ (reflection of body and field about a place combined with $`\sigma_3`$, a symmetry of (6.2)), $`K=\text{const}+\frac{E''_{k,\sigma}(0)}4(1-\cos2\hat P)`$, with $`\cos2\hat P:=\frac12(\mathcal T^2+\mathcal T^{-2})`$ and $`E''`$ taken at order $`\tau^2`$.
- $`\phi`$ vanishes on the two places on each side of the cut. The hops by two places across the cut therefore do not contribute, and $`[\hat x,\mathcal T^{\pm2}]=\pm2\mathcal T^{\pm2}`$ may be used.
- The velocity is $`i[K,\hat x]=\frac{iE''}4(\mathcal T^2-\mathcal T^{-2})`$. Its expectation vanishes for real $`\phi`$: the start is at rest.
- With $`[W,\mathcal T^{\pm2}]=\mathcal T^{\pm2}\bigl(W(\hat x\pm2)-W(\hat x)\bigr)`$, and shifting the summation index by one place:

```math
a_{k,\sigma}(0)=-E''_{k,\sigma}(0)\sum_j\phi_{j+1}\phi_{j-1}\,W'_{k,\sigma}(j)+O(g_s^2)+O(\tau^4\gamma g_s).
\qquad\text{(7.7)}
```

The central slope is a result of this step, not a choice: it comes from the hops by two places. The prefactor $`c_\phi=\langle\Psi\vert\cos2\hat P\vert\Psi\rangle\in(0,1]`$ is the momentum-width factor of the envelope. `code/v2/check_weight.py` confirms (7.7) with $`E''=1`$ against $`-\langle[H,[H,X]]\rangle`$ of $`H=K+W`$ on the ring (section "Code").

### Step 6. Acceleration through relative order $`\gamma`$

Through order $`\gamma`$, (6.10) gives $`E''_{k,\sigma}(0)=\sigma\frac{\tau^2}{M_k}(1+\epsilon\gamma n)+O(\gamma^2)`$, with $`\epsilon=-1`$ for (a) and $`\epsilon=+1`$ for (c) ($`\Delta''=O(\gamma^2)`$). At this order it is exactly of order $`\tau^2`$. From (7.6), $`W'(j)=\sigma M_k\gamma\,\delta N'(j)+M_k^2\gamma^2\Theta'(j)+O(g_s\gamma^3)+O(g_s^2)`$. For a place $`j`$ with $`r_j:=(j-x_s)\bmod L\in\{1,\dots,L-1\}`$:
- $`u'(j)=L-2r_j`$;
- $`(u^2)'(j)=u'(j)\,[u(j+1)+u(j-1)]=(L-2r_j)(2u(j)-2)`$;
- $`L^2+2-4u(j)=(L-2r_j)^2+2`$.

Hence $`\delta N'(j)=\frac{ng_s(L-2r_j)}{Lt_f}`$ and $`\Theta'(j)=-\frac{ng_s(L-2r_j)[(L-2r_j)^2+2]}{6L^2t_f^2}`$.

Every $`j`$ with $`\phi_{j+1}\phi_{j-1}\ne0`$ lies on the arc, so $`r_j\ne0`$ and $`L-2r_j=(L-2r_0)-2(j-x_0)`$, with $`r_0:=(x_0-x_s)\bmod L`$. The weights $`\phi_{j+1}\phi_{j-1}`$ are symmetric about $`x_0`$, so their odd moments vanish. This gives
- $`\sum_j\phi_{j+1}\phi_{j-1}(L-2r_j)=c_\phi(L-2r_0)`$;
- $`\sum_j\phi_{j+1}\phi_{j-1}(L-2r_j)^3=c_\phi(L-2r_0)[(L-2r_0)^2+12s_\phi^2]`$.

Inserting into (7.7), the factors $`\sigma^2=1`$ and $`M_k/M_k`$ cancel in the leading term:

```math
a_{k,\sigma}(0)=-\frac{\tau^2\gamma\,ng_s\,(L-2r_0)}{Lt_f}\,c_\phi\Bigl[1+\epsilon\gamma n-\sigma\,\frac{\gamma M_k}{t_f}\,\frac{(L-2r_0)^2+2+12s_\phi^2}{6L}\Bigr]+O(\tau^2g_s\gamma^3)+O(g_s^2)+O(\tau^4\gamma g_s).
\qquad\text{(7.8)}
```

- *Leading term.* $`-\tau^2\gamma\,c_\phi\,\delta N'(x_0)`$ is the same for all levels and both branches, for a common envelope.
- *Relative order $`\gamma`$.* The universal part is $`\epsilon\gamma n`$. The part that depends on level and branch is

```math
\Delta_{k,\sigma}(x_0)=-\sigma\,\frac{\gamma M_k}{t_f}\,\frac{(L-2r_0)^2+2+12s_\phi^2}{6L}.
\qquad\text{(7.9)}
```

  - It is odd in the branch and proportional to the half-gap $`M_k`$. Its geometric factor is $`\ge1/(3L)`$, because $`s_\phi^2\ge0`$. It is therefore nonzero for every start of the class when $`\gamma\ne0`$.
  - The packet term $`12s_\phi^2`$ is fixed by the start. It exceeds the lattice term $`2`$ as soon as $`s_\phi^2>1/6`$: for the triangular envelope of half-width $`2`$, $`12s_\phi^2=7.2`$ (`check_weight.py`).
  - For $`\gamma g_s\ne0`$ and off the antipode $`L=2r_0`$ (where $`a=0`$ by reflection symmetry), the fall therefore depends on level and branch at relative order $`\gamma`$, with parameter $`\gamma M_k/t_f`$.
  - In the class there is no control. Control for the universal leading term: the coupling $`\sigma_3\otimes\mathbb 1_N`$ of Step 4 gives $`a=-\tau^2\gamma\,c_\phi\,\delta N'(x_0)/M_k`$, level-dependent already at leading order.

## Result

- **(7.2)** [formula] Class: the held body ($`\tau=0`$), couplings (a) and (c), $`N_f\ge1`$, $`L\ge5`$, every level and branch, lowest adapted field state, (W). The weight difference is exactly $`N_f[\varepsilon_0(x)-\varepsilon_0(x')]`$, with $`\varepsilon_0(x)`$ the lowest eigenvalue of one field object with the two held point terms $`g_b=\sigma\gamma M_k`$ at $`x`$ and $`g_s`$ at $`x_s`$, (7.1).
- **(7.3)** [formula] Same class. At first order in $`g_s`$ and through second order in $`\gamma`$, the weight is $`-\frac{2ng_sg_b}{t_f}\Lambda^+(x,x_s)+\frac{ng_sg_b^2}{t_f^2}[2G_0\Lambda^+(x,x_s)+\Lambda^+(x,x_s)^2-\frac2L(\Lambda^{+2})(x,x_s)]`$ up to an $`x`$-independent constant, with remainder $`O(g_s^2)+O(g_sg_b^3)`$ at fixed $`L,N_f,t_f`$.
- **(7.5)** [formula] Same class and order. On the ring, $`W_{k,\sigma}(x)-W_{k,\sigma}(x')=\frac{ng_sg_b}{Lt_f}[(1-\frac{(L^2-2)g_b}{6Lt_f})(u-u')+\frac{g_b}{3Lt_f}(u^2-u'^2)]`$, with $`u=r(L-r)`$; (7.4) gives $`\Lambda^+`$ and $`\Lambda^{+2}`$ explicitly.
- **(7.6)** [theorem] Same class and order. The weight is $`\sigma M_k\gamma\,\delta N(x)+M_k^2\gamma^2\Theta(x)`$.
  - At first order in $`\gamma`$ it is proportional, for all levels and both branches, to the one function $`\gamma\,\delta N(x)`$ of (5.8), with the factor $`\sigma M_k`$ (the eigenvalue of $`\sigma_3\otimes(m\mathbb 1_N+D)`$, the rest-and-clock cost).
  - Through second order, for $`\gamma g_s\ne0`$, it is not proportional to one function times a factor. The shape of its place dependence changes at relative order $`\gamma`$ between the two branches of every level, and between levels with different $`M_k`$.
  - No member of the class is a control.
- **(7.7)** [formula] Conditions: regime R, both couplings.
  - R1: the band of level $`k`$ and branch $`\sigma`$ is isolated, $`\delta_{k,\sigma}>0`$, with $`N_f(|\gamma|(M_k+\tau)+|g_s|)<\delta_{k,\sigma}/2`$.
  - The start lies in the band, with a real envelope $`\phi`$ supported on an arc of at most $`L-4`$ places that does not contain $`x_s`$.
  - R2: the acceleration is the coefficient of $`\tau^2`$, at first order in $`g_s`$.

  Under these conditions, the drift acceleration from rest at $`P=0`$ is $`a_{k,\sigma}(0)=-E''_{k,\sigma}(0)\sum_j\phi_{j+1}\phi_{j-1}W'_{k,\sigma}(j)`$, with the central slope. The remainder is $`O(g_s^2)+O(\tau^4\gamma g_s)`$.
- **(7.8)** [formula] Conditions: as for (7.7); every start of the class (envelope nonnegative and symmetric about $`x_0\ne x_s`$, $`c_\phi>0`$; nonempty for $`L\ge7`$); first order in $`g_s`$; through relative order $`\gamma`$. Then $`a_{k,\sigma}(0)=-\frac{\tau^2\gamma ng_s(L-2r_0)}{Lt_f}c_\phi[1+\epsilon\gamma n-\sigma\frac{\gamma M_k}{t_f}\frac{(L-2r_0)^2+2+12s_\phi^2}{6L}]`$.
  - $`\epsilon=-1`$ for (a) and $`+1`$ for (c).
  - $`c_\phi=\langle\cos2\hat P\rangle\in(0,1]`$, and $`s_\phi^2`$ is the variance of the weights $`\phi_{j+1}\phi_{j-1}`$.
  - The remainder is $`O(\tau^2g_s\gamma^3)+O(g_s^2)+O(\tau^4\gamma g_s)`$. The $`\tau^2`$ term describes the acceleration only for $`\tau\ll M_k`$ and $`\tau^2\ll M_k\delta_{k,\sigma}`$.
- **(7.9)** [negative] Same conditions.
  - The fall of a body with its own mark is the same for all levels and both branches at leading order: $`-\tau^2\gamma\,c_\phi\,\delta N'(x_0)`$, for a common envelope.
  - It is not the same at relative order $`\gamma`$. A level- and branch-dependent term $`\Delta_{k,\sigma}=-\sigma\frac{\gamma M_k}{t_f}\frac{(L-2r_0)^2+2+12s_\phi^2}{6L}`$ appears. It is of first order in the parameter $`\gamma M_k/t_f`$, odd in $`\sigma`$ and proportional to $`M_k`$. Its geometric factor depends on the start through $`s_\phi^2`$ and is $`\ge1/(3L)`$.
  - For $`\gamma g_s\ne0`$, the level and branch dependence of the fall is present for every member of the class and every start of the class with $`L\ne2r_0`$. At the antipode $`L=2r_0`$, $`a=0`$.

## Consistency checks

1. **Dimensions.** $`\tau,t_f,g_s,M_k`$ have the unit of the contract, $`1/\lambda`$; $`\gamma`$ and $`n`$ are pure numbers. The prefactor of (7.8) is $`\tau^2\times`$(pure number), in position labels per $`\lambda^2`$ as in (5.7), and $`\gamma M_k/t_f`$ is a pure number. Passed.
2. **Test-body limit against (5.7) with (5.8).** Dropping the own-mark term $`\Theta`$ in (7.8) leaves $`-\tau^2\gamma\,c_\phi\,\delta N'(x_0)(1+\epsilon\gamma n)`$. (5.7) with $`N_\varphi=n+\delta N`$, at first order in $`g_s`$, gives $`-\tau^2\gamma\delta N'/\nu=-\tau^2\gamma\delta N'(1-\gamma n)+O(\gamma^3)`$ for (a), and $`-\tau^2\nu^2\gamma\delta N'/\nu=-\tau^2\gamma\delta N'(1+\gamma n)`$ for (c). The two agree through relative order $`\gamma`$, up to the common momentum-width factor $`c_\phi`$, which (5.7) as quoted does not show. Passed.
3. **Limits.** At $`\tau\to0`$, (7.8) vanishes, as it must for the flat dressed level (6.7). At $`g_s=0`$ it vanishes by translation invariance. At the antipode $`L=2r_0`$ it vanishes by the reflection symmetry of $`W`$ about $`x_s`$. Passed.

## Open issues

- Regime R is an assumption. The order $`\tau^4`$ of the acceleration (moving cloud, admixture of the other branch) is not computed.
- The isolation and smallness conditions of R1 are sufficient conditions (norm bounds), not necessary ones.
- (7.8) is derived for envelopes symmetric about a place. For other real envelopes (7.7) still holds, and the centre and the third moment of the weights $`\phi_{j+1}\phi_{j-1}`$ enter.
- Field states other than the lowest adapted one, and the second order in $`g_s`$, are not treated (scope).

## Code

- `code/v2/check_weight.py` (check). For $`N_f=1`$, $`t_f=1`$, $`x_s=0`$, on rings $`L=8`$ and $`L=13`$, it compares $`W(x)-W(x_s)`$ from the exact lowest eigenvalue of (7.1) with (7.3), (7.5) and with the first-order term (4.4) alone. Output: `code/v2/output/check_weight.txt`.
  - (7.4) holds to $`\le6\times10^{-15}`$, and (7.3) and (7.5) agree to $`\le6\times10^{-21}`$.
  - Grid: $`M_k\in\{1,2.5\}`$, $`\sigma=\pm`$, $`\gamma\in\{0.002,0.01\}`$, $`g_s\in\{0.001,0.004\}`$. The maximal deviation is $`3\times10^{-10}`$ to $`1\times10^{-7}`$, i.e. $`5\times10^{-4}`$ to $`4\times10^{-3}`$ of the weight, dominated by the $`g_s^2`$ remainder.
  - Scaling: the part of the deviation odd in $`g_s`$ scales as $`g_b^{2.99}`$, against $`g_b^{1.99}`$ for (4.4) alone. The part even in $`g_s`$ scales as $`g_s^{2.000}`$.
  - The local relative slope correction $`[W'(x_0)/W'_{\rm lead}(x_0)-1]/g_b`$ matches $`-[(L-2r_0)^2+2]/(6Lt_f)`$, the $`s_\phi=0`$ part of (7.9), for every $`r_0`$, to $`\le1.2\times10^{-4}`$. The worst case is where $`|L-2r_0|=1`$ amplifies rounding.
  - Packets, for (7.7) and (7.8). It computes $`-\langle[H,[H,X]]\rangle`$ for $`H=\frac14(1-\cos2\hat P)+W`$ ($`E''=1`$), with $`W`$ the exact weight, for triangular envelopes of half-width $`h=1`$ ($`L=8`$) and $`h=1,\dots,4`$ ($`L=13`$), at every allowed $`x_0`$, with the cut three places beyond the arc.
    - $`\langle[K,[K,X]]\rangle=0`$ exactly.
    - The leading ratio, which includes $`c_\phi`$ ($`0.167`$ to $`0.800`$), is $`1`$ to $`\le3\times10^{-6}`$.
    - The geometric factor matches $`-[(L-2r_0)^2+2+12s_\phi^2]/(6Lt_f)`$, with $`12s_\phi^2`$ from $`0`$ to $`26.1`$, to $`\le1.2\times10^{-4}`$.

## Methods used

- Block decomposition by conserved labels; non-interacting identical objects
- Rayleigh–Schrödinger perturbation theory to third order; analytic perturbation theory with Cauchy estimates
- Lattice Green function and its square on the ring (difference equations)
- Hellmann–Feynman theorem
- Isolation of a spectral band by norm bounds and a resolvent contour; Kato's transformation to the held basis
- Heisenberg double commutator for the projected lattice contract; moments of a symmetric envelope
- Numerical exact diagonalization and log-log scaling fits (check)
