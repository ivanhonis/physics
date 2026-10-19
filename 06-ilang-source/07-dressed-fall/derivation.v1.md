# Weight and fall of a body with its own mark in the field of a held source

- **Subproject:** 06-ilang-source
- **Package:** 07-dressed-fall
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-19

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
- (6.2) of 06-own-mark: the total contract on level $`k`$ for (a) and (c). (6.7): $`E_{k,\sigma}(P)|_{\tau=0}=\sigma M_k+N_f\varepsilon_0(\sigma\gamma M_k)`$. (6.10): $`E''_{k,\sigma}(0)=\sigma\frac{\tau^2}{M_k}(1-\gamma n+\gamma^2n^2)`$ (a), $`\sigma\frac{\tau^2}{M_k}(1+\gamma n)`$ (c), $`+\Delta''_{k,\sigma}+O(\gamma^3)`$, $`\Delta''_{k,\sigma}=O(\gamma^2)`$. Isolation (6.4), sufficient for $`\sigma=+`$ at $`P=0`$: $`2t_fN_f<M_k`$.

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

where $`u'=u(x')`$. `code/v1/check_weight.py` confirms (7.4) to $`6\times10^{-15}`$, (7.3)$`=`$(7.5) and (7.5) against the exact (7.2) (section "Code").

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

### Step 5. Regime R and the drift acceleration

**Regime R (assumption of the package).**
- **R1 (band dynamics).** The body is a packet in the dressed level $`E_{k,\sigma}(P)`$ of 06-own-mark, isolated under (6.4) of 06-own-mark. The packet is centred at $`P=0`$ and at a place $`x_0\ne x_s`$, narrow in $`P`$ on the scale of the band curvature and narrow in $`x`$ on the scale on which $`W'`$ changes. The source acts within the level through the weight, with effective contract $`E_{k,\sigma}(\hat P)+W_{k,\sigma}(\hat x)`$. Transitions out of the level are neglected: the change of $`W`$ over one place, $`O(n|g_s|\gamma M_k/t_f)`$, is small against the isolation gap.
- **R2 (the field follows the body; order in $`\tau`$).** The body is heavy, $`\tau^2\ll M_kt_f`$: its recoil for a transfer $`q`$, $`\approx\tau^2q^2/(2M_k)`$, is small against the field excitation $`\varepsilon_q\approx t_fq^2`$, so the field follows the body adiabatically. The weight is taken at $`\tau=0`$ (Steps 1–4), so the acceleration is obtained at its lowest order, $`\tau^2`$. Relative corrections of order $`\tau^2/(M_kt_f)`$ and $`\tau^2/M_k^2`$ (moving cloud, packet spread) are not computed.

The curvature is taken without the source, (6.10). Its dependence on $`g_s`$ enters below only at $`O(g_s^2)`$, because $`W'=O(g_s)`$. With $`\dot x=\partial_PE_{k,\sigma}`$ and $`\dot P=-W'_{k,\sigma}`$ (Ehrenfest for the effective contract), a start from rest at $`P=0`$ gives

```math
a_{k,\sigma}(0)=-E''_{k,\sigma}(0)\,W'_{k,\sigma}(x_0).
\qquad\text{(7.7)}
```

### Step 6. Acceleration through relative order $`\gamma`$

Through order $`\gamma`$, (6.10) gives $`E''_{k,\sigma}(0)=\sigma\frac{\tau^2}{M_k}(1+\epsilon\gamma n)+O(\gamma^2)`$, with $`\epsilon=-1`$ for (a) and $`\epsilon=+1`$ for (c) ($`\Delta''=O(\gamma^2)`$). From (7.6), $`W'=\sigma M_k\gamma\,\delta N'(x_0)+M_k^2\gamma^2\Theta'(x_0)+O(g_s\gamma^3)+O(g_s^2)`$. For $`r_0:=(x_0-x_s)\bmod L\in\{1,\dots,L-1\}`$:
- $`u'(x_0)=L-2r_0`$;
- $`(u^2)'(x_0)=u'(x_0)\,[u(x_0+1)+u(x_0-1)]=(L-2r_0)(2u(x_0)-2)`$;
- $`L^2+2-4u(x_0)=(L-2r_0)^2+2`$.

Hence $`\delta N'(x_0)=\frac{ng_s(L-2r_0)}{Lt_f}`$ and $`\Theta'(x_0)=-\frac{ng_s(L-2r_0)[(L-2r_0)^2+2]}{6L^2t_f^2}`$. Inserting into (7.7), the factors $`\sigma^2=1`$ and $`M_k/M_k`$ cancel in the leading term:

```math
a_{k,\sigma}(0)=-\frac{\tau^2\gamma\,ng_s\,(L-2r_0)}{Lt_f}\Bigl[1+\epsilon\gamma n-\sigma\,\frac{\gamma M_k}{t_f}\,\frac{(L-2r_0)^2+2}{6L}\Bigr]+O(\tau^2g_s\gamma^3)+O(g_s^2),\qquad x_0\ne x_s .
\qquad\text{(7.8)}
```

- *Leading term.* $`-\tau^2\gamma\,\delta N'(x_0)`$ is the same for all levels and both branches.
- *Relative order $`\gamma`$.* The universal part is $`\epsilon\gamma n`$. The part that depends on level and branch is

```math
\Delta_{k,\sigma}(x_0)=-\sigma\,\frac{\gamma M_k}{t_f}\,\frac{(L-2r_0)^2+2}{6L}.
\qquad\text{(7.9)}
```

  It is odd in the branch, proportional to the half-gap $`M_k`$, and nonzero for every $`x_0\ne x_s`$ when $`\gamma\ne0`$, because its geometric factor is $`\ge1/(3L)`$. For $`\gamma g_s\ne0`$ and off the antipode $`L=2r_0`$, where $`a=0`$ by reflection symmetry, the fall therefore depends on level and branch at relative order $`\gamma`$, with parameter $`\gamma M_k/t_f`$. In the class there is no control. Control for the universal leading term: the coupling $`\sigma_3\otimes\mathbb 1_N`$ of Step 4 gives $`a=-\tau^2\gamma\,\delta N'/M_k`$, level-dependent already at leading order.

## Result

- **(7.2)** [formula] Class: the held body ($`\tau=0`$), couplings (a) and (c), $`N_f\ge1`$, $`L\ge5`$, every level and branch, lowest adapted field state, (W). The weight difference is exactly $`N_f[\varepsilon_0(x)-\varepsilon_0(x')]`$, with $`\varepsilon_0(x)`$ the lowest eigenvalue of one field object with the two held point terms $`g_b=\sigma\gamma M_k`$ at $`x`$ and $`g_s`$ at $`x_s`$, (7.1).
- **(7.3)** [formula] Same class. At first order in $`g_s`$ and through second order in $`\gamma`$, the weight is $`-\frac{2ng_sg_b}{t_f}\Lambda^+(x,x_s)+\frac{ng_sg_b^2}{t_f^2}[2G_0\Lambda^+(x,x_s)+\Lambda^+(x,x_s)^2-\frac2L(\Lambda^{+2})(x,x_s)]`$ up to an $`x`$-independent constant, with remainder $`O(g_s^2)+O(g_sg_b^3)`$ at fixed $`L,N_f,t_f`$.
- **(7.5)** [formula] Same class and order. On the ring, $`W_{k,\sigma}(x)-W_{k,\sigma}(x')=\frac{ng_sg_b}{Lt_f}[(1-\frac{(L^2-2)g_b}{6Lt_f})(u-u')+\frac{g_b}{3Lt_f}(u^2-u'^2)]`$, with $`u=r(L-r)`$; (7.4) gives $`\Lambda^+`$ and $`\Lambda^{+2}`$ explicitly.
- **(7.6)** [theorem] Same class and order. The weight is $`\sigma M_k\gamma\,\delta N(x)+M_k^2\gamma^2\Theta(x)`$.
  - At first order in $`\gamma`$ it is proportional, for all levels and both branches, to the one function $`\gamma\,\delta N(x)`$ of (5.8), with the factor $`\sigma M_k`$ (the eigenvalue of $`\sigma_3\otimes(m\mathbb 1_N+D)`$, the rest-and-clock cost).
  - Through second order, for $`\gamma g_s\ne0`$, it is not proportional to one function times a factor. The shape of its place dependence changes at relative order $`\gamma`$ between the two branches of every level, and between levels with different $`M_k`$.
  - No member of the class is a control.
- **(7.7)** [formula] Under regime R (R1 band dynamics in the isolated dressed level, R2 heavy body $`\tau^2\ll M_kt_f`$ with the weight at $`\tau=0`$, lowest order $`\tau^2`$), at first order in $`g_s`$, the drift acceleration from rest at $`P=0`$ is $`a_{k,\sigma}(0)=-E''_{k,\sigma}(0)W'_{k,\sigma}(x_0)`$, with central lattice slope.
- **(7.8)** [formula] Under R, both couplings, $`x_0\ne x_s`$, inside (6.4), at first order in $`g_s`$ and through relative order $`\gamma`$: $`a_{k,\sigma}(0)=-\frac{\tau^2\gamma ng_s(L-2r_0)}{Lt_f}[1+\epsilon\gamma n-\sigma\frac{\gamma M_k}{t_f}\frac{(L-2r_0)^2+2}{6L}]`$, with $`\epsilon=-1`$ (a), $`+1`$ (c). The remainder is $`O(\tau^2g_s\gamma^3)+O(g_s^2)`$.
- **(7.9)** [negative] Same conditions.
  - The fall of a body with its own mark is the same for all levels and both branches at leading order, $`-\tau^2\gamma\,\delta N'(x_0)`$.
  - It is not the same at relative order $`\gamma`$. A level- and branch-dependent term $`\Delta_{k,\sigma}=-\sigma\frac{\gamma M_k}{t_f}\frac{(L-2r_0)^2+2}{6L}`$ appears, of first order in the parameter $`\gamma M_k/t_f`$, odd in $`\sigma`$ and proportional to $`M_k`$. For $`\gamma g_s\ne0`$ the level and branch dependence of the fall is present at every $`x_0\ne x_s`$ off the antipode $`L=2r_0`$ (where $`a=0`$), for every member of the class.

## Consistency checks

1. **Dimensions.** $`\tau,t_f,g_s,M_k`$ have the unit of the contract, $`1/\lambda`$; $`\gamma`$ and $`n`$ are pure numbers. The prefactor of (7.8) is $`\tau^2\times`$(pure number), in position labels per $`\lambda^2`$ as in (5.7), and $`\gamma M_k/t_f`$ is a pure number. Passed.
2. **Test-body limit against (5.7) with (5.8).** Dropping the own-mark term $`\Theta`$ in (7.8) leaves $`-\tau^2\gamma\,\delta N'(x_0)(1+\epsilon\gamma n)`$. (5.7) with $`N_\varphi=n+\delta N`$, at first order in $`g_s`$, gives $`-\tau^2\gamma\delta N'/\nu=-\tau^2\gamma\delta N'(1-\gamma n)+O(\gamma^3)`$ for (a), and $`-\tau^2\nu^2\gamma\delta N'/\nu=-\tau^2\gamma\delta N'(1+\gamma n)`$ for (c). The two agree through relative order $`\gamma`$. Passed.
3. **Limits.** At $`\tau\to0`$, (7.8) vanishes, as it must for the flat dressed level (6.7). At $`g_s=0`$ it vanishes by translation invariance. At the antipode $`L=2r_0`$ it vanishes by the reflection symmetry of $`W`$ about $`x_s`$. Passed.

## Open issues

- Regime R is an assumption. The corrections of relative order $`\tau^2/(M_kt_f)`$ and $`\tau^2/M_k^2`$ to the weight of a moving dressed body are not computed.
- The isolation (6.4) is quoted only for $`\sigma=+`$ at $`P=0`$. For $`\sigma=-`$, (7.8) requires the isolation condition of 06-own-mark in its full form, which is not quoted here.
- The geometric factor in (7.8) and (7.9) belongs to the central lattice slope, read from the second form of (5.7). For another lattice slope the factor changes, and so do the places where it vanishes. Wherever it is nonzero, the order $`\gamma`$ and the parameter $`\gamma M_k/t_f`$ stay the same.
- Field states other than the lowest adapted one, and the second order in $`g_s`$, are not treated (scope).

## Code

- `code/v1/check_weight.py` (check). For $`N_f=1`$, $`t_f=1`$, $`x_s=0`$, on rings $`L=8`$ and $`L=13`$, it compares $`W(x)-W(x_s)`$ from the exact lowest eigenvalue of (7.1) with (7.3), (7.5) and with the first-order term (4.4) alone. Output: `code/v1/output/check_weight.txt`.
  - (7.4) holds to $`\le6\times10^{-15}`$, and (7.3) and (7.5) agree to $`\le6\times10^{-21}`$.
  - Grid: $`M_k\in\{1,2.5\}`$, $`\sigma=\pm`$, $`\gamma\in\{0.002,0.01\}`$, $`g_s\in\{0.001,0.004\}`$. The maximal deviation is $`3\times10^{-10}`$ to $`1\times10^{-7}`$, i.e. $`5\times10^{-4}`$ to $`4\times10^{-3}`$ of the weight, dominated by the $`g_s^2`$ remainder.
  - Scaling: the part of the deviation odd in $`g_s`$ scales as $`g_b^{2.99}`$, against $`g_b^{1.99}`$ for (4.4) alone. The part even in $`g_s`$ scales as $`g_s^{2.000}`$.
  - The relative slope correction $`[W'/W'_{\rm lead}-1]/g_b`$ matches $`-[(L-2r_0)^2+2]/(6Lt_f)`$ of (7.8), (7.9) for every $`r_0`$, to $`\le1.2\times10^{-4}`$. The worst case is where $`|L-2r_0|=1`$ amplifies rounding.

## Methods used

- Block decomposition by conserved labels; non-interacting identical objects
- Rayleigh–Schrödinger perturbation theory to third order; analytic perturbation theory with Cauchy estimates
- Lattice Green function and its square on the ring (difference equations)
- Hellmann–Feynman theorem
- Effective band (Ehrenfest) dynamics in an isolated dressed level
- Numerical exact diagonalization and log-log scaling fits (check)
