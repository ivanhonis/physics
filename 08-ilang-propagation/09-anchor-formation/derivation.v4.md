# Formation of the anchored made field: place-dependent and uniform parts

- **Subproject:** 08-ilang-propagation
- **Package:** 09-anchor-formation
- **Version:** v4
- **Mode:** external regeneration
- **Date:** 2026-10-26

## Changes from previous version

- Step 6, new (9.20), (9.10), (9.18), Result 4 (I1): the pole of the localized mode is no longer dropped from the anchor kernel. Only the residue of the complete response is the localized mode's share; the rest of the pole term is kept, rewritten with the resolvent identity (9.20) as free kernels averaged with exponentially decaying weights, and bounded. (9.10) and (9.18) are re-derived for every $`\kappa_a\ne\kappa_h/\gamma_3`$ with these terms; (9.18) gains the term $`Ce^{-d_x/\xi}/d_s`$.
- Step 6, $`D=1`$ (I1): the anchor kernel on the line has the poles of the localized mode at every $`\kappa_a`$; they are kept in the same way, and $`\beta=1`$ is re-derived.
- Step 8, *Every later $`\lambda`$*, Result 7 (I1): the exact gradient now contains the integrable kernel $`k_c`$ and the pole sum. With the Bessel form of the free gradient and Landau's bound, $`\sup_\lambda\lvert\nabla\delta a^\infty-F(\rho,\cdot)-F(m,\cdot)\rvert=O(\rho^{-1/6})`$, which re-establishes (9.13) for every later $`\lambda`$.
- Setup, Step 6, Result, Open issues (I2): the exclusion of $`\kappa_a=\kappa_h/\gamma_3`$ now rests on the question's note of 2026-10-26 (after round 2), and what holds there is stated.
- Step 9, new (9.19), (9.15), Result 9, consistency check 3 (I3): the continuum string is replaced by the discrete secular equation of the anchored ring. Labels, weights and phases come from it, and the remainder of (9.15) is bounded with its range of $`\alpha`$ and $`\tau`$.
- Code: `check_formation.py` adds an above-threshold run ($`\kappa_a=8`$) with the image bound and the localized mode, and the uniform deviation on the line; `check_uniform.py` adds checks of (9.19), of the exact mode sum and of the remainder of (9.15). Every output under `code/v4/output/` comes from the v4 run.

## Response to verification

- I1: Accepted and fixed in Step 6 and Step 8. The localized mode is now separated at the level of the complete response. Its share is the residue $`-\psi_b(x)\psi_b(x_s)(1-\cos\omega_b\lambda)/\nu_b`$, which is exponentially small. The rest of the pole term of the anchor kernel is kept: by (9.20) it becomes a superposition of free kernels at the places $`y-z`$, with the weights $`\gamma_b(z)`$. Its weight combines with the integrable part to $`\chi(0)=1/c_\phi`$ on the cubic lattice and to $`1`$ on the line. Every term is bounded uniformly in $`\lambda`$. On the cubic lattice this gives (9.10) and (9.18) for every $`\kappa_a\ne\kappa_h/\gamma_3`$, with the additional term $`Ce^{-d_x/\xi}/d_s`$ in (9.18). On the line the transform $`1/(1+\kappa_a\gamma_s(0))`$ is split into $`1+\hat k_c+c_1/(s^2+\nu_b)`$, with $`\int k_c=-1-c_1/\nu_b\ne0`$, as the verifier noted. The pole sum restores the total weight, and $`\sup_\lambda\lvert\nabla\delta a^\infty-F(\rho)-F(m)\rvert=O(\rho^{-1/6})`$, so (9.13) holds for every later $`\lambda`$. The statements that use these bounds, (9.11), (9.12), (9.13) and (9.16), stand as stated.
- I2: Accepted. The question's note of 2026-10-26 (after round 2) permits excluding $`\kappa_a=\kappa_h/\gamma_3`$ from the positive formation statements and from the image asymptotics. The exclusion is stated in Setup, Step 6, the Result and the Open issues, together with what holds at the threshold: (9.2)–(9.9), (9.14), (9.17), the $`\lambda`$-mean in (9.18), and every statement that no formation occurs. The ring results do not involve this member.
- I3: Accepted and fixed in Step 9. The labels come from the discrete secular equation (9.19), and the mode weights and phases come from the discrete eigenvectors; no continuum description is used. The remainder of (9.15) is bounded by $`C[(1+\tau)/\kappa_a+\tau^{2/3}/(\kappa_hL^{1/3})+(1+\kappa_h^2/\kappa_a^2)\log L/(\kappa_hL)]`$ for $`\kappa_aL\ge8\kappa_h`$, uniformly in $`\alpha\in[0,1]`$ and $`\tau\ge0`$. The code checks (9.19), the exact mode sum and the scaling of the remainder at three values of $`\alpha`$, three values of $`\kappa_a`$ and three sizes.

## Setup and assumptions

**Field, anchor, source, start** (assumptions, M8, M9, A11). The setting of question.md: oscillator cells at the places of a ring ($`D=1`$) or a cubic torus ($`D=3`$) of side $`L`$, contract $`C_M`$ plus the anchor $`\frac{\kappa_a}2q_h^2`$ plus the source term $`g_sq_{x_s}`$ of a held object, listed at every $`\lambda\ge0`$ (A9 restricted to $`\lambda\ge0`$); at $`\lambda=0`$ the state is the lowest eigenvector $`\Omega`$ of the contract without the source term. As $`M\to\infty`$ the contract becomes $`H_a+g_sq_{x_s}`$ with $`H_a=\frac12\sum_xp_x^2+\frac12\sum_{x,y}q_x(K_a)_{xy}q_y`$, $`K_a=\kappa_h\Delta+\kappa_aP_h`$. $`K_a>0`$, because the kernel of $`\Delta`$ is spanned by the uniform vector $`\mathbf 1`$ and $`\langle\mathbf 1,P_h\mathbf 1\rangle=1`$. So $`\Omega`$ is nondegenerate, and the contract with the source has a lowest eigenvector.

**Inputs and notation.** I use (4.10)–(4.14) and (4.19) of 04-formation@v4, and (5.8), (5.9), (5.11), (5.15), (5.18) and the weighing of 05-anchor@v3, as quoted in question.md, with $`g,r,\gamma_\nu,R,G_a,c_\phi,\gamma_3,\Gamma,w,\Sigma`$ defined there. The labels are $`\mathbf k\in\frac{2\pi}L\mathbb Z_L^D`$, with $`\Omega_{\mathbf k}^2=\hat K_0(\mathbf k)=2\kappa_h\sum_i(1-\cos k_i)`$ and $`c_0=\sqrt{\kappa_h}`$. $`\tilde\gamma_\nu:=\gamma_\nu-1/(L^D\nu^2)`$ is the part of $`\gamma_\nu`$ from the labels $`\mathbf k\ne0`$ ($`\tilde\gamma_\nu\to g`$ as $`\nu\to0`$), and $`\gamma,\tilde\gamma,R`$ are continued to complex $`\nu=s`$ off the spectrum. Normal modes: $`K_a\psi_n=\nu_n\psi_n`$, $`\nu_n=\omega_n^2`$, $`\nu_0<\nu_1\le\dots`$. Distances: $`\rho=\lvert x-x_s\rvert`$, $`d_s=\lvert x_s-h\rvert`$, $`d_x=\lvert x-h\rvert`$ are Euclidean separations of lattice places, as in 04-formation and 05-anchor. Their relation to the distances of 03-ilang-space is the coupling map used there, and it is not needed here. Ratios: $`w=c_0\lambda/\rho`$, $`a=d_s/\rho`$, $`b=d_x/\rho`$. $`\theta`$ is the unit step. Units: with $`[\lambda]=E^{-1}`$ ($`E`$ a unit of cost), $`[q]=E^{-1/2}`$, $`[\kappa_h]=[\kappa_a]=E^2`$, $`[g_s]=E^{3/2}`$, $`[\delta a]=[g]=[c_\phi]=E^{-2}`$, and $`[c_0]=E`$ (places per unit $`\lambda`$).

**Made field** (question.md): $`\delta a(x,\lambda)=\partial_{g_s}\langle q_x\rangle_\lambda\vert_{g_s=0}`$; $`\delta a_{\rm st}`$ is the same in the lowest eigenvector with the source, and $`u:=\delta a-\delta a_{\rm st}`$.

**Criteria.**
- *Along an axis:* (4.11) applied to the place-dependent part $`\delta a^\perp`$ of Step 3.
  - $`D=3`$: $`\Delta_3^\perp(\rho,\lambda):=\delta a^\perp(x_s+\rho\mathbf e_1,\lambda)/\delta a^\perp_{\rm st}(x_s+\rho\mathbf e_1)-1`$. The reference value is $`\delta a^\perp_{\rm st}=g(x-h)-g(x-x_s)`$, the static part with zero place average. With $`L\to\infty`$ first it is the place difference $`\delta a_{\rm st}(x)-\delta a_{\rm st}(y)`$ with $`\lvert y\rvert\to\infty`$.
  - $`D=1`$: $`\Delta_1`$ of (4.11), with $`\nabla`$ taken along the ring from the source toward the anchor. Place differences remove every uniform part.
- *On a shell:* (4.19) with $`\delta a^\perp`$ in place of $`\delta a`$ and $`\varphi_\ell(x)=\Phi((x-x_s)/\ell)`$, for weights $`\Phi`$ that depend only on $`\lvert y\rvert`$ (question note (a)).
- *Uniform part* $`\bar U`$ of Step 3 (criterion stated before use): it has reached its static value to accuracy $`\varepsilon\in(0,1)`$ from $`\lambda_f`$ on if

```math
\lvert\bar U(\lambda)-\bar U_{\rm st}\rvert\le\varepsilon\,\lvert\bar U_{\rm st}\rvert\qquad\text{for every }\lambda\ge\lambda_f .
\qquad\text{(9.1)}
```

**Excluded members** (cancellations).
- $`x_s=h`$: by (5.8), $`\delta a_{\rm st}\equiv-1/\kappa_a`$, so there is no place-dependent part.
- $`D=3`$: places with $`g(x-h)=g(x-x_s)`$ (in the scaling limit $`b=1`$), where the reference value vanishes.
- $`D=1`$: places beyond the source as seen from the anchor, or beyond the anchor, where the $`L\to\infty`$ limit of the static gradient vanishes ((5.11) on the line).
- Places within $`O(1)`$ of $`x_s`$ or $`h`$, where the place-dependent part is not dominated by its long-range part. The limits $`\rho,d_s,d_x\to\infty`$ remove them.
- Shell: $`a=d_s/\ell\le2`$, where the shell reaches $`h`$. For $`a>2`$ the weighted reference does not vanish (Step 7).
- $`D=3`$, $`\kappa_a=\kappa_h/\gamma_3`$, where the localized mode reaches the top of the band. This member is excluded from the image asymptotics ((9.10), second part of (9.18)) and from the positive formation statements, as the question's note of 2026-10-26 (after round 2) permits. At this member (9.2)–(9.9), (9.14), (9.17), the $`\lambda`$-mean in (9.18), and every statement that no formation occurs still hold.

**Orders.** $`g_s\to0`$ (the means are exactly linear in $`g_s`$, Step 1) and $`M\to\infty`$ come first. Then either
- (O1): $`L\to\infty`$ before every limit in $`\lambda`$; up to exponentially small terms this is the same as $`\lambda`$ below the wrap time with $`\rho,d_s,d_x\ll L`$ (Step 5); or
- (O2): $`\lambda`$ grows with $`L`$.

## Derivation

### Step 1. Means at $`M\to\infty`$

Fix $`L`$, $`g_s`$ and a bounded interval of $`\lambda`$.
- On every vector with finitely many levels, the compressed contract with the source acts as $`H_a+g_sq_{x_s}`$ once $`M`$ exceeds those levels by two.
- $`H_a+g_sq_{x_s}`$ is essentially self-adjoint on these vectors. So the evolutions converge strongly, uniformly in $`\lambda`$ on bounded intervals (Trotter–Kato), and the lowest eigenvectors converge, since the lowest eigenvalue is isolated and simple.
- The level moments of the states stay bounded, so $`\langle q_x\rangle_\lambda`$ converges.

This is how $`M\to\infty`$ first is used: at fixed $`L,g_s,\lambda`$. All later limits act on the limit.

In the limit, (1.9) gives the Heisenberg equations $`\mathrm dq_x/\mathrm d\lambda=p_x`$ and $`\mathrm dp_x/\mathrm d\lambda=-(K_aq)_x-g_s\delta_{xx_s}`$. They are linear. Hence:
- The means $`\bar q_x=\langle q_x\rangle_\lambda`$ obey $`\ddot{\bar q}=-K_a\bar q-g_se_{x_s}`$ with $`\bar q(0)=\dot{\bar q}(0)=0`$; the initial data vanish because $`\Omega`$ is even under $`(q,p)\to(-q,-p)`$.
- $`q-\bar q`$ obeys the source-free equations, under which $`\Omega`$ is stationary. So the state at $`\lambda`$ is $`\Omega`$ displaced by $`(\bar q,\bar p)`$, and every connected equal-time correlation, for example $`\langle q_x^2\rangle_\lambda-\langle q_x\rangle_\lambda^2=w(x)`$, is that of $`\Omega`$ at every $`\lambda`$. $`\Gamma`$ and $`\Sigma`$ of 05-anchor are static response coefficients of the contract (changes of lowest eigenvectors under added terms), not correlations of the evolving state.
- $`\bar q`$ is exactly linear in $`g_s`$.

With the normal modes,

```math
\delta a(x,\lambda)=-\Bigl[\frac{1-\cos(\sqrt{K_a}\,\lambda)}{K_a}\Bigr]_{xx_s},\qquad u(x,\lambda)=\Bigl[\frac{\cos(\sqrt{K_a}\,\lambda)}{K_a}\Bigr]_{xx_s},\qquad \delta a_{\rm st}(x)=-G_a(x,x_s).
\qquad\text{(9.2)}
```

The last identity holds because the lowest eigenvector with the source is $`\Omega`$ displaced to $`\bar q=-g_sK_a^{-1}e_{x_s}`$, so $`g_s\delta a_{\rm st}=\phi_a`$ of (5.11). $`u`$ is the anchored analogue of (4.10). Its Laplace transform, for $`{\rm Re}\,s>0`$, is

```math
\widehat{\delta a}(x,s)=\int_0^\infty e^{-s\lambda}\delta a(x,\lambda)\,\mathrm d\lambda=-\frac1s\Bigl[\frac1{s^2+K_a}\Bigr]_{xx_s}=-\frac{R_{xx_s}(s)}{s},
\qquad\text{(9.3)}
```

with $`R`$ of (5.9) continued from $`\nu>0`$ to $`\nu=s`$.

### Step 2. The image at the anchor

The anchor acts on the means as the force $`-\kappa_a\bar q_h`$ on the cell $`h`$. Define the *image strength* $`\sigma_h(\lambda):=-\kappa_a\delta a(h,\lambda)`$. Let $`S_0(y,\lambda)=[\sin(\sqrt{\kappa_h\Delta}\,\lambda)/\sqrt{\kappa_h\Delta}]_{y0}`$ be the free response and $`\delta a_0(y,\lambda)=-\int_0^\lambda S_0(y,\lambda')\,\mathrm d\lambda'`$ the free made field (no anchor). On the torus the label $`\mathbf k=0`$ contributes $`\lambda/L^D`$ to $`S_0`$ and $`-\lambda^2/2L^D`$ to $`\delta a_0`$. Duhamel's formula for the free equation with the two forces $`-g_se_{x_s}`$ and $`g_s\sigma_he_h`$ gives

```math
\delta a(x,\lambda)=\delta a_0(x-x_s,\lambda)+\int_0^\lambda S_0(x-h,\lambda-\lambda')\,\sigma_h(\lambda')\,\mathrm d\lambda',\qquad
\sigma_h(\lambda)=-\kappa_a\,\delta a_0(h-x_s,\lambda)-\kappa_a\!\int_0^\lambda\! S_0(0,\lambda-\lambda')\,\sigma_h(\lambda')\,\mathrm d\lambda' .
\qquad\text{(9.4)}
```

This is a Volterra equation for $`\sigma_h`$, with $`\hat\sigma_h(s)=\kappa_a\gamma_s(x_s-h)/\{s[1+\kappa_a\gamma_s(0)]\}`$. Since $`\hat S_0(y,s)=\gamma_s(y)`$, the Laplace transform of (9.4) is (9.3) with (5.9). So the made field is the free field of the source plus the free field of an image at $`h`$, whose strength $`\sigma_h(\lambda)`$ the anchor sets. By (5.8) the static image strength is $`\kappa_aG_a(h,x_s)=1`$. The code check (i) confirms (9.4) against the exact (9.2).

### Step 3. Uniform part and place-dependent part

Sum the equation of the means over all places; since $`\sum_x(\Delta v)_x=0`$, $`\frac{\mathrm d^2}{\mathrm d\lambda^2}\sum_x\bar q_x=-g_s[1-\sigma_h(\lambda)]`$: the place sum is driven by the net force of source and image. The uniform part is the place average, i.e. the component along the zero mode $`\mathbf 1`$ of $`\kappa_h\Delta`$; the place-dependent part is the rest:

```math
\bar U(\lambda):=\frac1{L^D}\sum_x\delta a(x,\lambda)=-\frac1{L^D}\int_0^\lambda(\lambda-\lambda')\,\bigl[1-\sigma_h(\lambda')\bigr]\,\mathrm d\lambda',\qquad \delta a^\perp:=\delta a-\bar U .
\qquad\text{(9.5)}
```

Since $`\sum_xg(x)=0`$, the place average of (5.11) is its uniform shift. So the static values are exactly the two parts of (5.11):

```math
\bar U_{\rm st}=-\Bigl[\frac1{\kappa_a}+\frac{r(x_s,h)}2\Bigr],\qquad \delta a^\perp_{\rm st}(x)=g(x-h)-g(x-x_s)=-\tfrac12\bigl[r(x,h)-r(x,x_s)\bigr].
\qquad\text{(9.6)}
```

Place differences of $`\delta a`$ equal those of $`\delta a^\perp`$. To transform (9.5), use $`\hat\sigma_h`$ of Step 2 and $`\gamma_s=1/(L^Ds^2)+\tilde\gamma_s`$; the label $`\mathbf k=0`$ cancels in the numerator:

```math
\hat{\bar U}(s)=-\frac1s\;\frac{1+\kappa_a\bigl[\tilde\gamma_s(0)-\tilde\gamma_s(x_s-h)\bigr]}{\kappa_a+L^Ds^2\bigl[1+\kappa_a\tilde\gamma_s(0)\bigr]} .
\qquad\text{(9.7)}
```

The lowest normal mode of $`K_a`$ is not used for the separation. It is not uniform: it carries an image at $`h`$ ((9.14)). On the ring at large $`L`$ it is not separated from the other modes either (Step 9).

### Step 4. Finite $`L`$: mean value and recurrence

(9.2) is a finite sum of terms $`\cos(\omega_n\lambda)`$ with $`\omega_n>0`$. Hence, for every $`L`$, on both graphs and at every place,

```math
\lim_{T\to\infty}\frac1T\int_0^T\delta a(x,\lambda)\,\mathrm d\lambda=\delta a_{\rm st}(x),\qquad
\forall\,\lambda_f,\eta>0\ \ \exists\,\lambda>\lambda_f:\ \max_x\lvert\delta a(x,\lambda)\rvert<\eta ,
\qquad\text{(9.8)}
```

and the same holds for $`\bar U`$ and $`\delta a^\perp`$. The second statement follows from Dirichlet's simultaneous approximation theorem: there are arbitrarily large $`\lambda`$ at which every $`\omega_n\lambda`$ lies within any given distance of $`2\pi\mathbb Z`$, and there (9.2) vanishes up to that distance. At such $`\lambda`$:
- $`\Delta_3^\perp=\Delta_1=-1`$;
- the left side of (4.19) equals the sum on its right side without the factor $`\varepsilon`$;
- $`\lvert\bar U-\bar U_{\rm st}\rvert=\lvert\bar U_{\rm st}\rvert`$.

So at fixed $`L`$ neither part meets (4.11), (4.19) or (9.1) for any $`\varepsilon<1`$, and the static values are reached only as $`\lambda`$-means. Formation in the sense of (4.11) and (4.19) therefore needs order (O1).

### Step 5. Order (O1): finite propagation, speeds and the free field

*Finite propagation.* $`(1-\cos\sqrt X\lambda)/X=\sum_{n\ge1}(-1)^{n+1}\lambda^{2n}X^{n-1}/(2n)!`$, and $`(K_a^{n-1})_{xy}=0`$ when $`n-1`$ is below the graph distance $`\lvert x-y\rvert_1`$.
- So the torus field at fixed places and the field of the same equations on $`\mathbb Z^D`$ (anchor at $`h`$) differ only by terms that wind around the torus. These are bounded by $`\sum_{n>\ell}\lambda^{2n}\lVert K_a\rVert^{n-1}/(2n)!`$, with $`\ell`$ of order $`L`$.
- They stay exponentially small up to the wrap time $`\simeq(L-\rho)/c_0`$. The reason is that $`\sin(\lambda\Omega)/\Omega`$ and $`(1-\cos\lambda\Omega)/\Omega^2`$ are entire functions of $`\Omega^2_{\mathbf k}`$, hence of $`\mathbf k`$. Shifting the contour by $`\mathbf k\to\mathbf k+is\hat y`$ with small $`s>0`$ gives the factor $`e^{-s(\lvert y\rvert-c_0\lambda)+O(s^3\lambda)}`$, since $`\lvert{\rm Im}\,\Omega\rvert\le c_0s+O(s^3)`$. So every free kernel is $`O(e^{-c_\delta\lvert y\rvert})`$ for $`c_0\lambda\le(1-\delta)\lvert y\rvert`$.
- By (9.5), $`\lvert\bar U(\lambda)\rvert\le\lambda^2\sup\lvert1-\sigma_h\rvert/(2L^D)`$.

Hence in order (O1), at every fixed $`\lambda`$, $`\bar U\to0`$ and $`\delta a^\perp\to\delta a^\infty`$, the field on $`\mathbb Z^D`$.

*Speeds.* $`\lvert\nabla_{\mathbf k}\Omega_{\mathbf k}\rvert^2=\kappa_h\sum_i\sin^2k_i/\sum_i4\sin^2(k_i/2)\le c_0^2`$, with equality only as $`\mathbf k\to0`$. So the largest slope of the normal-mode frequency is its slope $`c_0`$ at small labels, and the front of the free field is at $`c_0\lambda=\rho`$, up to an Airy layer of width $`O(\rho^{1/3})`$. The anchor is a rank-one term. It leaves the continuous spectrum $`[0,4D\kappa_h]`$ of $`\kappa_h\Delta`$ on $`\mathbb Z^D`$ unchanged and adds at most one normal mode $`\psi_b`$ above it, localized at $`h`$, with $`\nu_b=\omega_b^2`$ solving $`1+\kappa_a\gamma_{i\omega_b}(0)=0`$. It exists for $`D=1`$ at every $`\kappa_a`$, with $`\nu_b=2\kappa_h+\sqrt{4\kappa_h^2+\kappa_a^2}`$, and for $`D=3`$ iff $`\kappa_a>\kappa_h/\gamma_3`$, since $`\gamma(0)=-\gamma_3/\kappa_h`$ at the top of the band (shift $`\mathbf k\to\mathbf k+(\pi,\pi,\pi)`$). Its share of $`\delta a(x,\cdot)`$ is $`-\psi_b(x)\psi_b(x_s)(1-\cos\omega_b\lambda)/\nu_b=O(e^{-(d_x+d_s)/\xi})`$. This share is the residue of the complete response (9.3) at $`s=\pm i\omega_b`$.

*Free field.* On $`\mathbb Z^D`$, $`\delta a_0(y,\lambda)=-\int\frac{\mathrm d^Dk}{(2\pi)^D}e^{i\mathbf k\cdot y}\,\frac{1-\cos\Omega_{\mathbf k}\lambda}{\Omega_{\mathbf k}^2}`$.
- $`D=3`$: the static part is $`-g_\infty(y)=-\frac1{4\pi\kappa_h\rho}+O(\rho^{-3})`$ (input). In the oscillating part put $`\mathbf k=\mathbf q/\rho`$.
  - Small $`\lvert\mathbf k\rvert`$ gives $`\frac1{2\pi^2\kappa_h\rho}\int_0^\infty\frac{\sin q}q\cos(qw)\,\mathrm dq=\frac{\theta(1-w)}{4\pi\kappa_h\rho}`$: the angular average of $`e^{iq_1}`$ is $`\sin q/q`$, and the last step is Dirichlet's integral.
  - The rest of the zone is a smooth oscillatory integral, of order at most $`\rho^{-4/3}`$ along $`\mathbf e_1`$. The order $`\rho^{-4/3}`$ occurs at the fold caustics $`w=1+\sqrt2,\sqrt2+\sqrt3`$ of condition (d) of 04-formation, which covers these phases for the nearest-neighbour contract at $`m_h\to0`$ (question note (b)). In other directions the order is at most $`\lvert y\rvert^{-7/6}`$, by (9.17) below. The angular average and the step are the same in every direction.
  - The cubic term of $`\Omega_{\mathbf k}`$ only smooths the step over $`\lvert w-1\rvert=O(\rho^{-2/3})`$.
- $`D=1`$: the same steps with the factor $`e^{ik}-1`$ give the static gradient $`\frac1{2\kappa_h}`$ (Dirichlet kernel) and the oscillating gradient $`-\frac{\theta(1-w)}{2\kappa_h}`$, with remainder $`O(\rho^{-1/2})`$.

Hence, as $`\rho\to\infty`$ at fixed $`w\ne1`$,

```math
\rho\,\delta a_0(\rho\mathbf e_1,\lambda)\to-\frac{\theta(w-1)}{4\pi\kappa_h}\quad(D=3),\qquad \nabla\delta a_0(\rho,\lambda)\to\frac{\theta(w-1)}{2\kappa_h}\quad(D=1).
\qquad\text{(9.9)}
```

*Uniform bounds on the free field ($`D=3`$).* (4.11) and (4.19) ask for every $`\lambda\ge\lambda_f`$, so limits at fixed $`w`$ do not suffice. Let $`u_0:=\delta a_0+g_\infty`$ be the oscillating part, and fix $`\delta>0`$. Split the labels with a smooth cutoff $`\chi_0(\mathbf k)`$, equal to 1 near $`\mathbf k=0`$ and supported where $`\lvert\nabla\Omega\rvert>c_0/(1+\delta/2)`$.
- *Low labels.* In spherical coordinates $`\mathrm d^3k/\Omega^2=c_0^{-2}(1+O(k^2))\,\mathrm dk\,\mathrm d\sigma`$ is smooth, and $`\Omega=c_0k-c_0\alpha(\hat k)k^3+O(k^5)`$ with $`\alpha=\sum_i\hat k_i^4/24\in[\frac1{72},\frac1{24}]`$.
  - For $`c_0\lambda\ge(1+\delta)\lvert y\rvert`$ the radial derivative of the phase $`k\lvert y\rvert\cos\vartheta+\lambda\Omega`$ is at least of order $`\lambda`$. Two integrations by parts in $`k`$ leave a purely imaginary boundary term at $`k=0`$, plus $`O(\lambda^{-2})`$. Since $`u_0`$ is the real part of this integral, its low-label part is $`O(\lambda^{-2})`$. The same steps give $`O(\lambda^{-2})`$ for the low-label part of $`S_0`$, whose amplitude vanishes at $`k=0`$.
  - Across the front, uniform Airy asymptotics in $`(\lvert y\rvert-c_0\lambda)/\lambda^{1/3}`$ apply ($`\alpha`$ is bounded away from 0). For $`\delta a_0`$ they give the step of height $`1/(4\pi\kappa_h\lvert y\rvert)`$, smoothed over $`O(\lvert y\rvert^{1/3})`$. For $`S_0`$ they give a layer of height $`O(\lvert y\rvert^{-4/3})`$ whose oscillating tail has $`\int\lvert S_0\rvert\,\mathrm d\lambda=O(\lvert y\rvert^{-1/2})`$.
- *High labels* (amplitudes vanishing near $`\mathbf k=0`$).
  - In every direction, the dispersive bound of the lattice wave equation on $`\mathbb Z^3`$ applies: $`C(1+\lambda)^{-7/6}`$, uniformly in $`y`$. Its exponent is set by the points with all $`k_i=\pm\frac\pi2`$, where the Hessian of $`\Omega`$ has rank one.
  - Along $`\mathbf e_1`$, the stationary points of $`\rho k_1\pm\lambda\Omega`$ lie on the lines $`k_2,k_3\in\{0,\pi\}`$. There $`\partial_2^2\Omega,\partial_3^2\Omega=\kappa_h\cos k_{2,3}/\Omega\ne0`$, and $`\partial_1^2\Omega`$ vanishes only at the maxima of $`\kappa_h\sin k_1/\Omega`$ on the lines with one or two labels $`\pi`$. These are folds, at $`w=1+\sqrt2`$ and $`\sqrt2+\sqrt3`$ (condition (d), note (b)). As $`v=\rho/\lambda\to0`$ the stationary points tend to the corners $`\mathbf k\in\{0,\pi\}^3\setminus\{0\}`$, which are nondegenerate. Stationary phase uniform in $`v\in[0,c_0/(1+\delta)]`$ then gives $`O(\lambda^{-4/3})`$.
- Ahead of the front all kernels are exponentially small (contour shift above).

Together, for $`y\ne0`$, with $`C`$ independent of $`\lambda`$ and of the direction:

```math
\sup_{c_0\lambda\ge(1+\delta)\rho}\rho\,\lvert u_0(\rho\mathbf e_1,\lambda)\rvert\le C_\delta\,\rho^{-1/3},\qquad
\sup_{\lambda\ge0}\lvert\delta a_0(y,\lambda)\rvert\le\frac C{\lvert y\rvert},\qquad
\int_0^\infty\lvert S_0(y,\lambda)\rvert\,\mathrm d\lambda\le\frac C{\lvert y\rvert^{1/6}} .
\qquad\text{(9.17)}
```

The last bound is $`\int_{(1-\delta)\lvert y\rvert/c_0}^\infty C\lambda^{-7/6}\,\mathrm d\lambda`$, plus the Airy tail and the low-label $`O(\lambda^{-2})`$.

### Step 6. Order (O1): the image strength

By Step 2, $`\hat\sigma_h(s)=\frac{\gamma_s(x_s-h)}s\,\chi(s)`$, with $`\chi(s)=\kappa_a/[1+\kappa_a\gamma_s(0)]`$ on $`\mathbb Z^D`$. The first factor is the transform of $`A(x_s-h,\cdot)`$, $`A(y,\lambda):=-\delta a_0(y,\lambda)`$, which by (9.9) is a step at $`c_0\lambda=d_s`$. By (9.17) and $`\lvert\delta a_0(0,\lambda)\rvert\le2g_\infty(0)`$, $`\lvert A(y,\lambda)\rvert\le C/(1+\lvert y\rvert)`$ for $`D=3`$.

*Pole of the localized mode.* Where the localized mode exists, $`1+\kappa_a\gamma_s(0)`$ vanishes at $`s^2=-\nu_b`$. Put $`\gamma_b:=(\kappa_h\Delta-\nu_b)^{-1}e_0`$ on $`\mathbb Z^D`$. It is real and even, it decays exponentially with a length $`\xi`$, $`\sum_z\gamma_b(z)=-1/\nu_b`$ (sum the equation $`(\kappa_h\Delta-\nu_b)\gamma_b=e_0`$ over places), and $`\psi_b=\gamma_b(\cdot-h)/\lVert\gamma_b\rVert`$. Since $`\partial_{s^2}\gamma_s(0)=-\lVert\gamma_b\rVert^2`$ at $`s^2=-\nu_b`$, the pole term of $`\chi`$ is $`c_b/(s^2+\nu_b)`$ with $`c_b=-\lVert\gamma_b\rVert^{-2}`$. This term is not localized by itself: convolved with the free kernels it produces continuous-spectrum and static parts, for example, on $`\mathbb Z^3`$, the share $`c_bg_\infty(x_s-h)/\nu_b`$ of the $`\lambda`$-mean of $`\sigma_h`$. Only the residue of the complete response is the localized mode's share. So the pole term is kept and rewritten with the resolvent identity

```math
\gamma_s(y)=\gamma_b(y)-(s^2+\nu_b)\sum_z\gamma_b(z)\,\gamma_s(y-z) .
\qquad\text{(9.20)}
```

For a product $`f(s^2)`$ of factors $`\gamma_s(y_i)`$, it gives $`f(s^2)/(s^2+\nu_b)=f(-\nu_b)/(s^2+\nu_b)+{}`$terms in which one factor $`\gamma_s(y_i)`$ is replaced by $`-\sum_z\gamma_b(z)\gamma_s(y_i-z)`$ and the factors before it by $`\gamma_b(y_j)`$. These are free kernels at the places $`y_i-z`$, averaged with the exponentially decaying weights $`\gamma_b(z)`$. Only the first term carries the pole; after division by $`s`$ it is $`f(-\nu_b)(1-\cos\omega_b\lambda)/\nu_b`$.

- $`D=3`$: $`\chi`$ is the transform of $`\kappa_a\delta(\lambda)+K_c(\lambda)`$, plus, for $`\kappa_a>\kappa_h/\gamma_3`$, the pole term $`c_b\sin(\omega_b\lambda)/\omega_b`$.
  - For $`\kappa_a\ne\kappa_h/\gamma_3`$, $`1+\kappa_a\gamma_s(0)`$ has no zero on the band. Its singularities there (band edges, van Hove points) are of square-root type, so $`K_c=O(\lambda^{-3/2})`$ is integrable.
  - At $`\kappa_a=\kappa_h/\gamma_3`$ the zero sits at the top edge, and the kernel decays only as $`\lambda^{-1/2}`$. This member is excluded here (question note of 2026-10-26, after round 2).
  - The total weight is $`\chi(0)=\kappa_a+\hat K_c(0)+c_b/\nu_b=\kappa_a/(1+\kappa_a\gamma_3/\kappa_h)=1/c_\phi`$, with $`c_b:=0`$ for $`\kappa_a<\kappa_h/\gamma_3`$.
  - With (9.20), $`\sigma_h=(\kappa_a\delta+K_c)*A(h-x_s,\cdot)-c_b\sum_z\gamma_b(z)A(h-x_s-z,\cdot)+c_b\gamma_b(h-x_s)(1-\cos\omega_b\lambda)/\nu_b`$, where $`*`$ is the convolution on $`[0,\lambda]`$.
  - By (9.9), $`A(h-x_s-z,\lambda)\to g_\infty(x_s-h)\theta(c_0\lambda-d_s)`$ at fixed $`z`$ and fixed $`c_0\lambda/d_s\ne1`$. Dominated convergence ($`K_c\in L^1`$, and $`\sum_z\lvert\gamma_b(z)\rvert d_s/(1+\lvert h-x_s-z\rvert)`$ bounded) gives the weight $`\kappa_a+\hat K_c(0)-c_b\sum_z\gamma_b(z)=\chi(0)`$, and the last term is $`O(e^{-d_s/\xi})`$. This is (9.10) for $`\kappa_a\ne\kappa_h/\gamma_3`$, the pole term included.
- $`D=1`$: $`\gamma_s(y)=\gamma_s(0)\zeta_s^{\lvert y\rvert}`$ with $`\gamma_s(0)=[s\sqrt{s^2+4\kappa_h}]^{-1}\to\infty`$. So $`\hat\sigma_h=\frac{\zeta_s^{d_s}}s[1-\hat K_1(s)]`$ with $`\hat K_1:=1/(1+\kappa_a\gamma_s(0))`$.
  - $`\zeta_s^n/s`$ is the transform of $`E(n,\lambda):=\int_0^{2c_0\lambda}2nJ_{2n}(u)\,\mathrm du/u`$ (Laplace pair of $`\nu J_\nu(at)/t`$, with $`\zeta_s=[(\sqrt{s^2+4\kappa_h}-s)/2c_0]^2`$). $`E`$ is bounded, and $`E(n,\lambda)\to\theta(c_0\lambda-n)`$ as $`n\to\infty`$ at fixed $`c_0\lambda/n\ne1`$.
  - $`\hat K_1`$ has the poles of the localized mode at every $`\kappa_a`$. Write $`\hat K_1=1+\hat k_c+c_1/(s^2+\nu_b)`$ with $`c_1=c_b/\kappa_a`$. On the imaginary axis the only other singular points of $`\hat K_1`$ are the square-root points $`s=\pm2ic_0`$; at $`s=0`$ it is analytic, $`\hat K_1=2c_0s/\kappa_a+\dots`$. So $`k_c=O(\lambda^{-3/2})`$ is integrable, with $`\hat k_c(0)=-1-c_1/\nu_b\ne0`$.
  - Dividing (9.20) by $`\gamma_s(0)`$, and using it at $`y=0`$, gives $`\frac{\zeta_s^n}{s^2+\nu_b}=\frac{\zeta_b^n}{s^2+\nu_b}-\sum_z\gamma_b(z)\bigl[\zeta_s^{\lvert n-z\rvert}-\zeta_b^n\zeta_s^{\lvert z\rvert}\bigr]`$, with $`\zeta_b^n=\gamma_b(n)/\gamma_b(0)`$ and $`\lvert\zeta_b\rvert<1`$. Hence
  $`\sigma_h=-k_c*E(d_s,\cdot)+c_1\sum_z\gamma_b(z)\bigl[E(\lvert d_s-z\rvert,\cdot)-\zeta_b^{d_s}E(\lvert z\rvert,\cdot)\bigr]-c_1\zeta_b^{d_s}(1-\cos\omega_b\lambda)/\nu_b`$.
  - The weights of the terms with $`E(\approx d_s,\cdot)`$ add up to $`-\hat k_c(0)+c_1\sum_z\gamma_b(z)=1`$, and the terms with $`\zeta_b^{d_s}`$ are exponentially small. So $`\sigma_h\to\theta(c_0\lambda-d_s)`$. The anchor takes the arriving force over $`\lambda\sim2c_0/\kappa_a`$, the scale of $`\hat K_1=2c_0s/\kappa_a+\dots`$.

Hence, as $`d_s\to\infty`$, on the scale $`\lambda\propto d_s`$,

```math
\sigma_h(\lambda)\to\beta\,\theta(c_0\lambda-d_s),\qquad \beta=\frac{g_\infty(x_s-h)}{c_\phi}=\frac{1+O(d_s^{-2})}{4\pi\kappa_hc_\phi d_s}\quad(D=3,\ \kappa_a\ne\kappa_h/\gamma_3),\qquad \beta=1\quad(D=1).
\qquad\text{(9.10)}
```

By (9.4) the image adds $`-\beta\,\delta a_0(x-h,\lambda-d_s/c_0)`$, a free field from $`h`$ that arrives at $`x`$ at $`c_0\lambda=d_s+d_x`$.

*$`D=3`$: $`\lambda`$-mean and image bound in order (O1).* Let $`\delta a^\infty=-[(1-\cos\sqrt{K_a}\lambda)K_a^{-1}]_{xx_s}`$ be the field on $`\mathbb Z^3`$ with the anchor (Step 5).
- *$`\lambda`$-mean.* The spectral measure of $`K_a`$ on $`\mathbb Z^3`$ has no atom at 0, and the mean of $`\cos\omega\lambda`$ vanishes for $`\omega>0`$, the localized mode included. So the $`\lambda`$-mean of $`\delta a^\infty`$ is $`-(K_a^{-1})_{xx_s}`$. By (5.9) on $`\mathbb Z^3`$ at $`\nu\to0`$, this is the first part of (9.18), for every $`\kappa_a`$.
- *Pointwise limit.* The continuous-spectrum part of $`\delta a^\infty-(\text{mean})`$ tends to 0 as $`\lambda\to\infty`$ (Riemann–Lebesgue). For $`\kappa_a>\kappa_h/\gamma_3`$ the localized mode adds the persistent oscillation $`\psi_b(x)\psi_b(x_s)\cos(\omega_b\lambda)/\nu_b`$, of size $`O(e^{-(d_x+d_s)/\xi})`$. So a pointwise limit exists only without this mode.
- *Image bound* ($`\kappa_a\ne\kappa_h/\gamma_3`$). By (9.4), $`I:=\delta a^\infty-\delta a_0(x-x_s,\cdot)=S_0(x-h)*\sigma_h`$, with $`\hat I=\chi(s)Q(s^2)/s`$ and $`Q:=\gamma_s(x-h)\gamma_s(h-x_s)`$. Since $`A(y,0)=0`$ and $`\partial_\lambda A=S_0`$, the part with $`\kappa_a\delta+K_c`$ is $`A(x-h)*(\kappa_a\delta+K_c)*S_0(h-x_s)`$. It is bounded by $`\sup\lvert A(x-h,\cdot)\rvert\,(\kappa_a+\lVert K_c\rVert_1)\int\lvert S_0(h-x_s,\cdot)\rvert`$. For $`\kappa_a>\kappa_h/\gamma_3`$, (9.20) turns the pole part $`c_bQ/[s(s^2+\nu_b)]`$ into three terms:
  - the residue $`c_bQ(-\nu_b)(1-\cos\omega_b\lambda)/\nu_b=-\psi_b(x)\psi_b(x_s)(1-\cos\omega_b\lambda)/\nu_b`$, the localized mode's share of Step 5, of size $`O(e^{-(d_x+d_s)/\xi})`$;
  - $`-c_b\sum_z\gamma_b(z)\,A(x-h-z)*S_0(h-x_s)`$, bounded by $`\lvert c_b\rvert\sum_z\lvert\gamma_b(z)\rvert\sup\lvert A(x-h-z,\cdot)\rvert\int\lvert S_0(h-x_s,\cdot)\rvert`$. Since $`\sum_z\lvert\gamma_b(z)\rvert/(1+\lvert y-z\rvert)\le C/(1+\lvert y\rvert)`$, it is of the order of the first part;
  - $`-c_b\gamma_b(x-h)\sum_z\gamma_b(z)A(h-x_s-z,\cdot)`$, bounded by $`Ce^{-d_x/\xi}/d_s`$.

  With (9.17) this is the second part of (9.18):

```math
\lim_{T\to\infty}\frac1T\int_0^T\delta a^\infty(x,\lambda)\,\mathrm d\lambda=-g_\infty(x-x_s)+\beta\,g_\infty(x-h),\qquad
\sup_{\lambda\ge0}\lvert I(x,\lambda)\rvert\le\frac C{d_x\,d_s^{1/6}}+\frac{C\,e^{-d_x/\xi}}{d_s}+O\bigl(e^{-(d_x+d_s)/\xi}\bigr)\ \ (\kappa_a\ne\kappa_h/\gamma_3).
\qquad\text{(9.18)}
```

The last two terms are present only for $`\kappa_a>\kappa_h/\gamma_3`$.

The $`L\to\infty`$ limit of (5.11) is instead $`-[c_\phi-g_\infty(x_s-h)]-g_\infty(x-x_s)+g_\infty(x-h)`$. So in (O1) the uniform part and an image of strength $`1-\beta`$ are missing even from the $`\lambda`$-mean: they never form. The image of strength 1 in (5.11) expresses the balance of forces on the finite torus ($`\sigma_h^{\rm st}=1`$); on $`\mathbb Z^3`$ the anchor takes only the share $`\beta`$ of the force of the source.

### Step 7. Formation on the cubic torus

Take order (O1), then $`\rho\to\infty`$ along $`\mathbf e_1`$ at fixed $`w`$, $`a`$ and $`b\ne1`$. In (O1), $`\delta a^\perp=\delta a^\infty`$ at every $`\lambda`$ (Step 5), so

```math
\Delta_3^\perp=\frac{-g_\infty(x-h)+u_0(\rho\mathbf e_1,\lambda)+I(x,\lambda)}{g_\infty(x-h)-g_\infty(\rho\mathbf e_1)} .
```

- By (9.6), $`\rho\,\delta a^\perp_{\rm st}\to(\frac1b-1)/4\pi\kappa_h`$, and $`-g_\infty(x-h)/\delta a^\perp_{\rm st}\to1/(b-1)`$.
- By (9.9), $`\rho\,u_0\to\theta(1-w)/4\pi\kappa_h`$. By (9.10) and (9.4), the image contributes $`O(\beta\rho/d_x)=O(1/\rho)`$ at fixed $`w`$ ($`\kappa_a\ne\kappa_h/\gamma_3`$).

So

```math
\lim\Delta_3^\perp(\rho,\lambda)=\begin{cases}-1,&w<1,\\[2pt] \dfrac1{b-1},&w>1,\end{cases}\qquad
\lim_{\rho\to\infty}\frac{c_0\lambda_{\rm form}(\rho;\varepsilon)}\rho=1\ \ \text{if } b>1+\frac1\varepsilon,\qquad \lambda_{\rm form}(\rho;\varepsilon)=\infty\ \ \text{for all large }\rho\ \text{if } \lvert b-1\rvert<\frac1\varepsilon .
\qquad\text{(9.11)}
```

The profile holds at fixed $`w\ne1`$ for $`\kappa_a\ne\kappa_h/\gamma_3`$. The two statements on $`\lambda_{\rm form}`$ need every later $`\lambda`$:
- *Middle* ($`\kappa_a\ne\kappa_h/\gamma_3`$). By (9.17) and (9.18), uniformly in $`c_0\lambda\ge(1+\delta)\rho`$, $`\lvert\Delta_3^\perp+g_\infty(x-h)/\delta a^\perp_{\rm st}\rvert\le C_\delta\rho^{-1/3}+C(a\rho)^{-1/6}/\lvert1-b\rvert`$, which tends to 0. At $`w=1-\delta`$, $`\Delta_3^\perp\to-1`$. So for $`\frac1{b-1}<\varepsilon`$ and large $`\rho`$, $`(1-\delta)\rho<c_0\lambda_{\rm form}\le(1+\delta)\rho`$. As in (4.14), $`\lambda_{\rm form}-\rho/c_0=O(\rho^{1/3})`$ once the caustic wakes and the image term are below $`\varepsilon-\frac1{b-1}`$.
- *Right* (every $`\kappa_a`$). If $`\lvert\Delta_3^\perp\rvert\le\varepsilon`$ for all $`\lambda\ge\lambda_f`$, its $`\lambda`$-mean obeys the same bound. By (9.18) that mean is $`(\beta-1)g_\infty(x-h)/\delta a^\perp_{\rm st}`$, which tends to $`\frac1{b-1}`$ since $`\beta=O(1/\rho)`$. So $`\lambda_{\rm form}=\infty`$ for large $`\rho`$ when $`\lvert b-1\rvert<1/\varepsilon`$. This rests on an exact identity of the mean, not on a limit at fixed $`w`$.

The marginal member $`b=1+1/\varepsilon`$ is not decided by (9.11).
- *Far from the anchor* ($`d_s,d_x\to\infty`$ at fixed $`\rho`$, then $`\rho\to\infty`$; $`\kappa_a\ne\kappa_h/\gamma_3`$). By (9.18), $`\rho\sup_\lambda\lvert I\rvert\to0`$, and the reference tends to $`-g_\infty(\rho\mathbf e_1)`$. So $`\Delta_3^\perp\to-u_0(\rho\mathbf e_1,\lambda)/g_\infty(\rho\mathbf e_1)`$ uniformly in $`\lambda`$. By (9.17) and (9.9), the $`\limsup`$ and $`\liminf`$ over $`d_s,d_x`$ of $`c_0\lambda_{\rm form}/\rho`$ both tend to 1 as $`\rho\to\infty`$, for every $`\varepsilon\in(0,1)`$. The place-dependent part forms within a $`\lambda`$ linear in $`\rho`$. The formation speed is $`c_0`$, equal to the front speed and to the largest slope of the normal-mode frequency, and independent of $`\kappa_a`$. The middle statement of (9.11) gives the same for $`b\to\infty`$ after $`\rho\to\infty`$.
- *Distances to $`h`$ comparable with $`\rho`$:* it does not form to accuracy below $`1/\lvert b-1\rvert`$, because the missing image of (5.11) is a fixed fraction of the reference value.

The code check (ii) (`check_formation.py`, cubic part) is a finite-window check: $`c_0\lambda\le40`$, i.e. $`w\le40/\rho`$. It tests the profile, not the bound for every later $`\lambda`$, which rests on (9.17) and (9.18). It finds, at $`\rho=3`$ to $`16`$, $`\Delta_3^\perp=-1`$ before the front and a later plateau equal to $`1/(b-1)`$ (from $`0.04`$ to $`2.0`$), to within $`0.006`$ at $`\rho\ge12`$, with wakes decaying about as $`\rho^{-0.4}`$. The $`\lambda`$-mean $`(\beta-1)g_\infty(x-h)/\delta a^\perp_{\rm st}`$, computed by the script, is $`0.74`$ to $`1.98`$ for the near anchor at $`\rho\ge6`$. So by the argument of the right statement, these members do not form at $`\varepsilon=0.5`$ at any later $`\lambda`$. Above the threshold ($`\kappa_a=8`$, near anchor), the plateau again follows the finite-$`\rho`$ prediction, to within $`0.03`$ at $`\rho\ge8`$. In the window, $`\max\lvert I\rvert\,d_xd_s^{1/6}=0.0037`$, of the form of (9.18).

*Shell* ($`\Phi`$ depending only on $`\lvert y\rvert`$, question note (a)). Take order (O1), then $`\ell\to\infty`$ at fixed $`w=c_0\lambda/\ell`$ and $`a=d_s/\ell>2`$.
- *Static.* Write $`z=(x-x_s)/\ell`$ and $`H=(h-x_s)/\ell`$, with $`\lvert H\rvert=a>2`$. Since $`\Phi`$ is radial, the shell sum of $`1/\lvert x-h\rvert`$ is $`\ell^2\int\Phi(z)\lvert z-H\rvert^{-1}\mathrm d^3z\,(1+o(1))=\ell^2\int\Phi/a\,(1+o(1))`$. This is the mean-value property of the harmonic function $`\lvert z-H\rvert^{-1}`$ on the spheres $`\lvert z\rvert\le2`$, which do not reach $`H`$. With $`\theta_a:=\int\Phi/(a\int\Phi\lvert z\rvert^{-1})\in(\frac1a,\frac2a)`$, the reference sum is $`-\frac{\ell^2}{4\pi\kappa_h}\int\Phi\lvert z\rvert^{-1}(1-\theta_a)(1+o(1))`$. It does not vanish, since $`\theta_a<2/a<1`$.
- *Free part.* By Poisson summation, $`\sum_x\varphi_\ell(x)u_0(x-x_s,\lambda)=\int\ell^3\hat\Phi(\ell\mathbf k)\cos(\lambda\Omega)\Omega^{-2}\frac{\mathrm d^3k}{(2\pi)^3}+O(\ell^{-\infty})`$. On compact ranges of $`w`$ it tends to the continuum value $`\frac{\ell^2}{4\pi\kappa_h}\int_{\lvert z\rvert>w}\Phi\lvert z\rvert^{-1}`$. For large $`w`$, note that $`\hat\Phi`$ is radial. Along each ray the amplitude $`k^2\hat\Phi(\ell k)/\Omega^2`$ is even in $`k`$ and the phase $`\lambda\Omega`$ is odd, so the radial integral runs over the whole line with no boundary term. Its phase derivative is at least $`c_0\lambda/2`$ where $`\hat\Phi(\ell\mathbf k)`$ is not negligible, which gives $`O(\ell^2w^{-N})`$ uniformly in $`\ell`$.
- *Image.* By (9.18), $`\lvert\sum_x\varphi_\ell I\rvert=O(\ell^3\cdot\ell^{-7/6})`$, negligible against $`\ell^2`$ ($`\kappa_a\ne\kappa_h/\gamma_3`$).
- Define $`\Psi(w):=\int_{\lvert z\rvert>w}\Phi\lvert z\rvert^{-1}/\int\Phi\lvert z\rvert^{-1}`$: continuous and nonincreasing, equal to $`1`$ for $`w\le1`$ and to $`0`$ for $`w\ge2`$. Then, uniformly in $`w\ge0`$, the left side of (4.19) divided by the sum on its right side (without $`\varepsilon`$) tends to $`\lvert\Psi(w)-\theta_a\rvert/(1-\theta_a)`$. By (9.18), the $`\lambda`$-mean of the same ratio tends to $`\theta_a/(1-\theta_a)`$, for every $`\kappa_a`$.

So, with $`w_\varepsilon:=\min\{w:\Psi(w)\le\theta_a+\varepsilon(1-\theta_a)\}\in[1,2]`$,

```math
\text{(4.19) for }\delta a^\perp:\quad\lim_{\ell\to\infty}\frac{c_0\lambda_{\rm form}}\ell=w_\varepsilon\ \ \text{if}\ \theta_a<\frac\varepsilon{1+\varepsilon},\qquad \lambda_{\rm form}=\infty\ \text{for all large }\ell\ \ \text{if}\ \theta_a>\frac\varepsilon{1+\varepsilon} .
\qquad\text{(9.12)}
```

The first statement assumes $`\kappa_a\ne\kappa_h/\gamma_3`$ and that $`\Psi`$ is strictly decreasing at $`w_\varepsilon`$; the second holds for every $`\kappa_a`$, by the $`\lambda`$-mean argument. The marginal member $`\theta_a=\varepsilon/(1+\varepsilon)`$ is not decided. As $`a\to\infty`$, the field forms in the mean by $`c_0\lambda\le2\ell`$ for every $`\varepsilon`$. For $`a<(1+\varepsilon)/\varepsilon`$ it never does, since $`\theta_a>1/a`$.

*Order (O2).* By (9.8) neither criterion holds at fixed $`L`$. Beyond the wrap time, the slow mode of (9.14) adds to $`u`$ the image $`-(1-\beta_L)g(x-h)\cos(\lambda/T_U)`$. This is an oscillation of relative size $`(1-\beta_L)\lvert g(x-h)\rvert/\lvert\delta a^\perp_{\rm st}(x)\rvert`$, which tends to $`1/\lvert b-1\rvert`$.

### Step 8. Formation on the ring (control)

Take order (O1), then $`\rho\to\infty`$ at fixed $`w`$ and $`a=d_s/\rho>1`$, with the observation place between source and anchor and the gradient toward the anchor.
- The reference is the $`L\to\infty`$ limit of $`\nabla\delta a_{\rm st}`$, which is $`1/\kappa_h`$ between source and anchor by (5.11). On the finite ring it is $`(L-d_s)/(\kappa_hL)`$.
- By (9.10), $`\beta=1`$. By (9.9), the image $`-\delta a_0(x-h,\lambda-d_s/c_0)`$ has the gradient $`\frac1{2\kappa_h}\theta(c_0\lambda-d_s-d_x)`$ toward $`h`$, and $`d_s+d_x=(2a-1)\rho`$.

So

```math
\lim\Delta_1(\rho,\lambda)=\begin{cases}-1,&w<1,\\-\tfrac12,&1<w<2a-1,\\0,&w>2a-1,\end{cases}\qquad
\lim_{\rho\to\infty}\frac{c_0\lambda_{\rm form}(\rho;\varepsilon)}\rho=\begin{cases}2a-1,&\varepsilon<\tfrac12,\\1,&\varepsilon>\tfrac12.\end{cases}
\qquad\text{(9.13)}
```

The free half of the gradient forms at the front, at speed $`c_0`$. The other half is the image, which arrives along the path $`d_s+d_x`$ at speed $`c_0`$.

*Every later $`\lambda`$.* On the line $`\gamma_s(y)=\gamma_s(0)\zeta_s^{\lvert y\rvert}`$, and (9.3) with (5.9) gives exactly, with $`m=2d_s-\rho-1`$ and $`\hat K_1`$ of Step 6,

```math
\widehat{\nabla\delta a^\infty}(\rho,s)=\hat F(\rho,s)+\hat F(m,s)\bigl[1-\hat K_1(s)\bigr].
```

- $`F(n,\cdot)`$, with transform $`\hat F(n,s)=P_n(s^2)/s`$, $`P_n:=-[\gamma_s(n+1)-\gamma_s(n)]`$, is the free gradient at the place $`n`$. From $`\zeta_s^n/\sqrt{s^2+4\kappa_h}=\mathcal L[J_{2n}(2c_0\lambda)]`$ and $`J_{\nu-1}-J_{\nu+1}=2J_\nu'`$: $`F(n,\lambda)=(2\kappa_h)^{-1}\int_0^{2c_0\lambda}J_{2n+1}(u)\,\mathrm du`$ for $`n\ge0`$, and $`F(-n-1,\cdot)=-F(n,\cdot)`$. So $`\partial_\lambda F(n,\lambda)=J_{2n+1}(2c_0\lambda)/c_0`$ and $`F(n+1,\lambda)-F(n,\lambda)=-J_{2n+2}(2c_0\lambda)/\kappa_h`$. By Landau's bound $`\lvert J_\nu(u)\rvert\le0.68\,\nu^{-1/3}`$, both are $`O(n^{-1/3})`$ uniformly in $`\lambda`$; $`F`$ is bounded.
- With $`\hat K_1=1+\hat k_c+c_1/(s^2+\nu_b)`$ (Step 6) and (9.20) applied to $`P_m`$, $`\hat F(m,s)/(s^2+\nu_b)=P_m(-\nu_b)/[s(s^2+\nu_b)]-\sum_z\gamma_b(z)\hat F(m-z,s)`$. So, exactly,

```math
\nabla\delta a^\infty(\rho,\lambda)=F(\rho,\lambda)-\bigl(k_c*F(m,\cdot)\bigr)(\lambda)+c_1\sum_z\gamma_b(z)F(m-z,\lambda)-c_1P_m(-\nu_b)\frac{1-\cos\omega_b\lambda}{\nu_b} .
```

- The last term is the localized mode's share, $`O(\lvert\zeta_b\rvert^m)`$. The weights of the middle terms add up to $`-\hat k_c(0)+c_1\sum_z\gamma_b(z)=1`$.
- Hence $`\nabla\delta a^\infty-F(\rho,\cdot)-F(m,\cdot)`$ is the sum of three pieces: $`-\int_0^\lambda k_c(\lambda')[F(m,\lambda-\lambda')-F(m,\lambda)]\,\mathrm d\lambda'`$, the piece $`F(m,\lambda)\int_\lambda^\infty k_c`$, and $`c_1\sum_z\gamma_b(z)[F(m-z,\lambda)-F(m,\lambda)]`$, up to $`O(\lvert\zeta_b\rvert^m)`$.
  - The first piece is at most $`\sup\lvert\partial_\lambda F\rvert\int_0^\Lambda\lambda'\lvert k_c\rvert+2\sup\lvert F\rvert\int_\Lambda^\infty\lvert k_c\rvert\le C(m^{-1/3}\Lambda^{1/2}+\Lambda^{-1/2})`$ for every $`\Lambda`$; take $`\Lambda=m^{1/3}`$.
  - In the second piece, either $`c_0\lambda\le(1-\delta)m`$, where $`F(m,\lambda)`$ is exponentially small, or $`\int_\lambda^\infty\lvert k_c\rvert=O(m^{-1/2})`$.
  - The third piece is at most $`C\sum_z\lvert\gamma_b(z)\rvert\lvert z\rvert m^{-1/3}`$ plus exponentially small terms.

  So, for every $`\kappa_a>0`$, $`\sup_{\lambda\ge0}\lvert\nabla\delta a^\infty(\rho,\lambda)-F(\rho,\lambda)-F(m,\lambda)\rvert=O(\rho^{-1/6})`$ at fixed $`a`$. The constant grows with the relaxation time $`2c_0/\kappa_a`$ of the anchor.

$`J_{2n+1}(u)`$ is exponentially small for $`u\le(1-\delta)(2n+1)`$. The stationary points of $`kn\pm\lambda\Omega`$ with $`\Omega'=c_0\cos(k/2)\le c_0/(1+\delta)`$ have $`\Omega''=-\frac{c_0}2\sin(k/2)\ne0`$: there are no caustics in $`D=1`$ (note (b)). So, uniformly in $`c_0\lambda\ge(1+\delta)n`$, $`F(n,\lambda)=\frac1{2\kappa_h}+O(\lambda^{-1/2})`$; and $`F`$ is exponentially small for $`c_0\lambda\le(1-\delta)n`$. Across its front, $`\kappa_hF\simeq\frac12\int_X^\infty{\rm Ai}(t)\,\mathrm dt`$ (uniform Airy asymptotics of $`J_{2n+1}`$), with $`X`$ the distance to the front in units of the Airy width $`O(n^{1/3})`$. So $`\kappa_hF`$ stays in $`[0,0.64]`$ up to $`o(1)`$, since $`0<\int_X^\infty{\rm Ai}\le1.275`$, the maximum at the first zero of $`{\rm Ai}`$. Hence, uniformly:
- $`\Delta_1\to-\frac12`$ on $`1+\delta\le w\le(2a-1)(1-\delta)`$;
- $`\Delta_1\to0`$ on $`w\ge(2a-1)(1+\delta)`$;
- $`\Delta_1\in[-\frac12,0.14]+o(1)`$ across the image front.

This gives both limits of $`\lambda_{\rm form}`$ in (9.13); the marginal $`\varepsilon=\frac12`$ is not decided.
- For $`\varepsilon<\frac12`$ and the anchor far away ($`a\to\infty`$), the place-dependent part does not form within any $`\lambda`$ linear in $`\rho`$. This uses only the lower bound $`\liminf c_0\lambda_{\rm form}/\rho\ge2a-1`$. This is the control of item 2.
- For comparable distances it forms within a $`\lambda`$ linear in $`\rho`$, with slope $`(2a-1)/c_0>1/c_0`$.
- In order (O2) the field varies on the scale $`L/c_0`$ and does not settle (Step 9 and (9.8)).

The code check (ii) (`check_formation.py`, ring part) is a finite-window check ($`w\le4`$ for $`a=2`$). It finds the plateaus $`-0.500`$ and $`0.000`$, and $`c_0\lambda_{\rm form}/\rho\to3.02`$ and $`1.02`$ at $`\rho=160`$ for $`a=2`$. Across the image front, $`\Delta_1`$ lies in $`[-0.515,0.117]`$ at $`\rho=160`$, and $`\max_{w>1.4}\lvert\Delta_1\rvert`$ falls from $`0.577`$ to $`0.530`$ between $`\rho=20`$ and $`160`$. With $`d_s=400`$, formation at $`\varepsilon=0.25`$ occurs only at $`c_0\lambda=2d_s-\rho+3`$. Over $`c_0\lambda\le8\rho`$, $`\sup_\lambda\kappa_h\lvert\nabla\delta a-F(\rho)-F(m)\rvert`$ decreases from $`\rho=20`$ to $`160`$ at $`\kappa_a=0.25,1,4`$ (to $`0.33`$, $`0.12`$, $`0.034`$).

### Step 9. The uniform part

*Order (O1).* By Step 5, $`\bar U(\lambda)\to0`$ at every $`\lambda`$. Meanwhile $`\bar U_{\rm st}\to-[c_\phi-g_\infty(x_s-h)]`$ for $`D=3`$ and $`\bar U_{\rm st}\to-[\frac1{\kappa_a}+\frac{d_s}{2\kappa_h}]`$ for $`D=1`$ at fixed $`d_s`$. So the uniform part never reaches its static value.

*Cubic torus, order (O2): the modes that enter $`\bar U`$.*
- A normal mode with $`\psi_n(h)\ne0`$ satisfies $`(\kappa_h\Delta-\nu_n)\psi_n=-\kappa_a\psi_n(h)e_h`$. So $`\psi_n\propto v_n:=(\kappa_h\Delta-\nu_n)^{-1}e_h`$, and $`\nu_n`$ solves $`1+\kappa_a\gamma_{i\sqrt\nu}(0)=0`$, i.e. $`\frac1{L^D\nu}=\frac1{\kappa_a}+\tilde\gamma_{i\sqrt\nu}(0)`$.
- Summing the mode equation over places gives $`\sum_x\psi_n=\kappa_a\psi_n(h)/\nu_n`$. Modes with $`\psi_n(h)=0`$ are orthogonal to $`\mathbf 1`$ and do not enter $`\bar U`$.
- By interlacing, the lowest root lies below the lowest nonzero eigenvalue $`\mu_1=4\kappa_h\sin^2(\pi/L)`$ of $`\kappa_h\Delta`$.

*The slow mode.* For $`D=3`$, $`L^{-3}\sum_{\mathbf k\ne0}\hat K_0^{-2}=O(L)`$, so $`\tilde\gamma_{i\omega}(x)=g(x)+O(\omega^2L)`$. With $`\nu_0=O(L^{-3})`$ this gives, with $`c_\phi^{(L)}:=\frac1{\kappa_a}+g(0)\to c_\phi`$:
- $`\nu_0^{-1}=L^3c_\phi^{(L)}[1+O(L^{-2})]`$;
- $`v_0(x)=-[c_\phi^{(L)}-g(x-h)]+O(L^{-2})`$;
- $`\lVert v_0\rVert^2=L^3c_\phi^{(L)2}[1+O(L^{-2})]`$.

*The other modes.* By Cauchy–Schwarz, their share of $`\bar U`$ is at most $`\frac2{L^3}\bigl[\sum_{n\ge1}\langle\mathbf1,\psi_n\rangle^2/\nu_n\bigr]^{1/2}\Gamma(x_s)^{1/2}`$.
- By (5.8), $`\sum_{n\ge0}\langle\mathbf1,\psi_n\rangle^2/\nu_n=\langle\mathbf1,K_a^{-1}\mathbf1\rangle=L^6c^{(L)}_\phi`$, and the mode $`n=0`$ carries $`L^6c^{(L)}_\phi[1+O(L^{-2})]`$ of it.
- $`\Gamma(x_s)=\frac1{\kappa_a}+r(x_s,h)\le2\lvert\bar U_{\rm st}\rvert`$, and $`c^{(L)}_\phi\le2\lvert\bar U_{\rm st}\rvert`$ for $`x_s\ne h`$ and large $`L`$. The last bound uses $`g(0)\to\gamma_3/\kappa_h`$, $`6\gamma_3<2`$, and $`g(0)-g(x)\ge g(0)-g(\mathbf e_1)=(1-L^{-3})/(6\kappa_h)`$ for $`x\ne0`$: $`g`$ lies below the mean of its neighbours away from $`0`$, so by the maximum principle its largest value off $`0`$ is at a neighbour of $`0`$.
- So this share is $`O(L^{-1})\lvert\bar U_{\rm st}\rvert`$.

Hence, uniformly in $`\lambda\ge0`$,

```math
T_U:=\nu_0^{-1/2}=\sqrt{L^3c^{(L)}_\phi}\,\bigl[1+O(L^{-2})\bigr],\qquad
\bar U(\lambda)=\bar U_{\rm st}\bigl[1-\cos(\lambda/T_U)\bigr]+O(L^{-1})\lvert\bar U_{\rm st}\rvert,\qquad
\frac{\psi_0(x)\psi_0(x_s)}{\nu_0}=\frac{\bigl[c^{(L)}_\phi-g(x-h)\bigr]\bigl[c^{(L)}_\phi-g(x_s-h)\bigr]}{c^{(L)}_\phi}\bigl[1+O(L^{-2})\bigr].
\qquad\text{(9.14)}
```

What (9.14) says:
- The uniform part oscillates between $`0`$ and $`2\bar U_{\rm st}`$ on the scale $`T_U\propto L^{3/2}`$.
- $`T_U`$ depends on the anchor only through $`c_\phi=\frac1{\kappa_a}+\frac{\gamma_3}{\kappa_h}`$, and not on $`d_s`$; $`d_s`$ enters $`\bar U_{\rm st}`$ and the delay $`d_s/c_0\le L/c_0`$.
- $`T_U/(L/c_0)=c_0(Lc^{(L)}_\phi)^{1/2}\to\infty`$, so the uniform part moves over many wrap times.
- The place-dependent part of the slow term is the image $`-(1-\beta_L)g(x-h)`$, with $`\beta_L:=g(x_s-h)/c^{(L)}_\phi`$; it is used in Step 7.

The same argument holds on the ring for a weak anchor, $`\kappa_aL\ll\kappa_h`$, using $`L^{-1}\sum_{k\ne0}\hat K_0^{-2}=L^3/(720\kappa_h^2)`$ and $`g(0)=(L^2-1)/(12\kappa_hL)`$. There $`T_U\simeq(L/\kappa_a)^{1/2}`$, with corrections $`O(\kappa_aL/\kappa_h)`$. The code check (iii) confirms (9.14) on both graphs.

*Ring, order (O2), $`\kappa_aL\gg\kappa_h`$.* Take $`L`$ even, and let $`y\in\{0,\dots,L-1\}`$ count the places from $`h`$ along the ring; $`\tau=c_0\lambda/L`$, $`\alpha=d_s/L`$. Everything follows from the discrete eigenvalue equation of $`K_a`$.
- Modes odd under $`y\to L-y`$ vanish at $`h`$, so they are orthogonal to $`\mathbf 1`$ (above) and do not enter $`\bar U`$.
- The even modes in the band are $`\psi_j(y)=N_j\cos(k_j(y-L/2))`$, $`k_j\in(0,\pi)`$. This form solves the mode equation at every $`y\ne0`$, with $`\nu_j=4\kappa_h\sin^2(k_j/2)`$. At $`y=0`$ the equation reads $`-2\kappa_h\sin k\,\sin(kL/2)+\kappa_a\cos(kL/2)=0`$. Its sign changes give one root in each interval $`(2j\pi/L,(2j+1)\pi/L)`$:

```math
k_jL=(2j+1)\pi-2\delta_j,\qquad \delta_j=\arctan\frac{2\kappa_h\sin k_j}{\kappa_a}\in\Bigl[0,\frac{2\kappa_hk_j}{\kappa_a}\Bigr],\qquad j=0,\dots,\tfrac L2-1 .
\qquad\text{(9.19)}
```

  The remaining even mode lies above the band (the localized mode).
- Weights: $`\sum_y\cos^2(k(y-L/2))=\frac L2+\frac{\sin(kL)\cos k}{2\sin k}`$ gives $`N_j^{-2}=\frac L2+\frac{\sin(2\delta_j)\cos k_j}{2\sin k_j}=\frac L2\bigl[1+O(\frac{\kappa_h}{\kappa_aL})\bigr]`$. With $`\langle\mathbf 1,\psi_j\rangle=\kappa_a\psi_j(h)/\nu_j`$ and (9.19), $`\langle\mathbf 1,\psi_j\rangle=(-1)^jN_j\cos\delta_j\cot(k_j/2)`$ and $`\psi_j(x_s)=(-1)^jN_j\sin(k_jd_s+\delta_j)`$. So, exactly,
  $`\bar U(\lambda)=-\sum_jw_j\sin(k_jd_s+\delta_j)(1-\cos\omega_j\lambda)+\bar U_b(\lambda)`$, with $`w_j=\frac{N_j^2\cos\delta_j\cot(k_j/2)}{4\kappa_hL\sin^2(k_j/2)}`$ and $`\omega_j=2c_0\sin(k_j/2)`$. The localized mode's share obeys $`\lvert\bar U_b\rvert\le2\kappa_a/(L\nu_b^2)\le2/(\kappa_aL)`$, since $`\nu_b\ge\langle e_h,K_ae_h\rangle\ge\kappa_a`$.
- Leading term: with $`n=2j+1`$, replace $`k_j\to n\pi/L`$, $`N_j^2\to2/L`$, $`\cos\delta_j\to1`$ and $`\cot(k/2)/(4\sin^2(k/2))\to2/k^3`$, so that $`w_j\to4L/(\pi^3\kappa_hn^3)`$; replace $`\sin(k_jd_s+\delta_j)\to\sin(n\pi\alpha)`$ and $`\omega_j\lambda\to n\pi\tau`$.
- Remainder $`R`$ of these replacements, written as a telescoping sum:
  - Relative weight errors $`O(k_j^2+\kappa_h/(\kappa_aL)+\kappa_h^2k_j^2/\kappa_a^2)`$ sum to $`O(1/\kappa_a+(1+\kappa_h^2/\kappa_a^2)\log L/(\kappa_hL))`$.
  - The phase error $`\lvert\delta_j(1-2\alpha)\rvert\le2\kappa_hn\pi/(\kappa_aL)`$ sums to at most $`2/\kappa_a`$.
  - The frequency error $`\lvert\omega_j\lambda-n\pi\tau\rvert\le\tau[2\delta_j+n^3\pi^3/(24L^2)]`$ sums to at most $`2\tau/\kappa_a+C\tau^{2/3}/(\kappa_hL^{1/3})`$; split the sum at $`n\sim(L^2/\tau)^{1/3}`$.
  - The terms with $`n>L`$ add $`O(1/(\kappa_hL))`$.

So, for $`\kappa_aL\ge8\kappa_h`$ (then $`\delta_j/(n\pi)\le2\kappa_h/(\kappa_aL)\le\frac14`$, and the relative errors above are uniform in $`j`$), uniformly in $`\alpha\in[0,1]`$ and $`\tau\ge0`$, with $`C`$ independent of $`L,\kappa_h,\kappa_a,\alpha,\tau`$:

```math
\begin{aligned}
\bar U(\lambda)&=-\frac{4L}{\pi^3\kappa_h}\sum_{n\ {\rm odd}}\frac{\sin(n\pi\alpha)\,(1-\cos n\pi\tau)}{n^3}+R=-\frac L{2\kappa_h}\Bigl[f(\alpha)-\tfrac12f(\alpha+\tau)-\tfrac12f(\alpha-\tau)\Bigr]+R,\\
\lvert R\rvert&\le C\Bigl[\frac{1+\tau}{\kappa_a}+\frac{\tau^{2/3}}{\kappa_hL^{1/3}}+\Bigl(1+\frac{\kappa_h^2}{\kappa_a^2}\Bigr)\frac{\log L}{\kappa_hL}\Bigr],
\end{aligned}
\qquad\text{(9.15)}
```

where $`f`$ is the odd $`2`$-periodic extension of $`x(1-x)`$; the second form follows from $`\sum_{n\,{\rm odd}}\sin(n\pi x)/n^3=\frac{\pi^3}8x(1-x)`$ on $`[0,1]`$. Relative to $`\lvert\bar U_{\rm st}\rvert\ge L\alpha(1-\alpha)/(2\kappa_h)`$, $`R`$ is small when $`\alpha(1-\alpha)\kappa_aL\gg\kappa_h(1+\tau)`$ and $`\tau\ll L^2`$. At fixed $`\alpha\in(0,1)`$ and $`\tau`$, this holds as $`L\to\infty`$, and uniformly for $`\tau\le\tau_L`$ with $`\kappa_h\tau_L/(\kappa_aL)\to0`$. The term linear in $`\tau`$ is the drift of the phases $`2\delta_j\tau`$: the finite anchor lengthens the period by the relative amount $`\simeq4\kappa_h/(\kappa_aL)`$. What (9.15) says:
- $`\bar U=-\lambda^2/(2L)`$ until the signals reach the anchor.
- The leading term is periodic in $`\lambda`$ with period $`2L/c_0`$, and oscillates between $`0`$ ($`\tau`$ even) and $`2\bar U_{\rm st}`$ ($`\tau`$ odd).
- Its mean is $`-L\alpha(1-\alpha)/(2\kappa_h)=\bar U_{\rm st}+O(1)`$.
- Its scale is the wrap time, independent of $`\kappa_a`$ at leading order.

The code check (iii) confirms (9.19), the exact mode sum and the form of the bound on $`R`$.

So the uniform part reaches its static value in the sense of (9.1) in no order of the limits: not in (O1), where it stays $`0`$; not in (O2), where it oscillates with amplitude $`\lvert\bar U_{\rm st}\rvert`$; and not at fixed $`L`$, by (9.8). Its $`\lambda`$-mean equals $`\bar U_{\rm st}`$ at every $`L`$.

### Step 10. All three together (short argument)

Only the cubic torus carries a long-range mark, so item 4 concerns $`D=3`$. As the question's note (c) states, the three are properties of the stated description:
- (5.15) in its order (a) and the weighing of 05-anchor are properties of the lowest eigenvectors of the contracts with the sources and the bodies, on the finite torus, followed by $`L\to\infty`$;
- (9.11) is a property of the evolution from $`\Omega`$ in order (O1).

They are available together in the order

```math
g_s\to0,\ M\to\infty;\qquad L\to\infty;\qquad d/\ell\to\infty;\qquad \ell\to\infty\ \ (w\ \text{fixed}),
\qquad\text{(9.16)}
```

where $`d`$ is the smallest distance of the places involved to $`h`$, and $`\ell`$ stands for every other distance ($`\rho`$, $`\lvert\mathbf r\rvert`$, $`R`$; the comparison vector $`\delta`$ and the placements of family (A) stay fixed or grow with $`\ell`$). Here $`\kappa_a\ne\kappa_h/\gamma_3`$.

In this order:
- (5.15) gives the separation dependence $`-g_1g_2/(4\pi\kappa_h\lvert\mathbf r\rvert)`$ (its order (a), $`\lvert\mathbf r\rvert/D_X\to0`$, with $`L\to\infty`$ first and all distances $`\ge\ell\gg1`$). It comes from the source term $`g(x_1-x_2)`$ alone.
- Step 7, far from the anchor ($`d\to\infty`$ at fixed $`\rho`$, then $`\rho\to\infty`$), gives formation of the place-dependent part within a $`\lambda`$ linear in the distance, at speed $`c_0`$, for every $`\varepsilon\in(0,1)`$.
- The weighing of 05-anchor holds within (A), or within (B) with $`R/d\to0`$ at fixed $`c`$, under its own conditions. In its controlled regime, at order $`\mu^2`$ and leading order in the grip, $`\rho_{\rm mark}=1`$ and $`\rho_{{\rm bond},i}=m_{\mathbf r}`$ for every level and both branches iff the grips are square with a common $`\hat\beta`$. The same holds in the lowest eigenvector of the stated contract iff in addition (5.10) holds for one body ((5.26) of 05-anchor for a pair). For other grips the weighing fails, as quoted.

So, for square grips with a common $`\hat\beta`$ (and (5.10), (5.26) for the lowest-eigenvector form), the long-range mark, the formation within a $`\lambda`$ linear in the distance and the weighing are available together in (9.16), at leading order in $`\ell/d`$.

This does not say that a weighing is realized in the evolving state (note (c): not asked). That would need a dynamical observable. The evolving state is $`\Omega`$ displaced by the means (Step 1); its $`\lambda`$-mean in (O1) lacks the uniform part and the image of strength $`1-\beta`$ of $`\phi_a`$ ((9.18)); and its total cost is conserved, so it is not the lowest eigenvalue with the source.

The order cannot be relaxed for the places of the formation. If the source or an observation place is at a distance from $`h`$ comparable to $`\rho`$, then $`b\le a+1`$ stays bounded, and (9.11) gives $`\lambda_{\rm form}=\infty`$ for every $`\varepsilon<1/\lvert b-1\rvert`$. In order (O2), formation in the sense of (4.11) and (4.19) fails by (9.8). In no order does the state reach the lowest eigenvector of the contract with the source: the evolution from $`\Omega`$ does not relax (A11), and the static values appear only as $`\lambda`$-means.

## Result

Class for all results: the nearest-neighbour oscillator cells without pinning, with the anchor $`\frac{\kappa_a}2q_h^2`$, every $`\kappa_h,\kappa_a>0`$, every $`h`$ and every $`x_s\ne h`$, on the ring and on the cubic torus, at first order in $`g_s`$ (exact for the means). The order is $`M\to\infty`$ first; each item states its remaining order. The excluded members are those of "Setup".

1. **(9.2), (9.3), (9.4)** (formula; every $`L`$, both graphs, every $`\lambda\ge0`$). The made field is $`\delta a=-[(1-\cos\sqrt{K_a}\lambda)K_a^{-1}]_{xx_s}`$, with $`\delta a_{\rm st}=-G_a(x,x_s)`$ and Laplace transform $`-R_{xx_s}(s)/s`$. Equivalently, it is the free field of the source plus the free field of an image at $`h`$, whose strength $`\sigma_h=-\kappa_a\delta a(h,\cdot)`$ solves the Volterra equation (9.4); the static image strength is 1. The state at $`\lambda`$ is $`\Omega`$ displaced by the means, so its connected equal-time correlations ($`w`$ among them) are those of $`\Omega`$.
2. **(9.5), (9.6), (9.7)** (formula; every $`L`$, both graphs). The uniform part is the place average $`\bar U=-L^{-D}\int_0^\lambda(\lambda-\lambda')[1-\sigma_h]\,\mathrm d\lambda'`$, driven by the net force of source and image, with Laplace transform (9.7). The place-dependent part is $`\delta a^\perp=\delta a-\bar U`$. Their static values are exactly the uniform shift and the place-dependent part of (5.11).
3. **(9.8)** (theorem; every finite $`L`$, both graphs). The $`\lambda`$-mean of $`\delta a`$ (and of $`\bar U`$, $`\delta a^\perp`$) is the static value. For every $`\lambda_f`$ there are $`\lambda>\lambda_f`$ at which $`\delta a`$ is arbitrarily close to $`0`$. So at fixed $`L`$ neither part meets (4.11), (4.19) or (9.1) for any $`\varepsilon<1`$.
4. **(9.9), (9.10), (9.17), (9.18)** (formula; order (O1), then the stated distance $`\to\infty`$ at fixed $`w`$; (9.17) and (9.18): $`D=3`$, order (O1), bounds uniform in $`\lambda`$ and the $`\lambda`$-mean).
   - The free field forms at the front: $`\rho\,\delta a_0\to-\theta(w-1)/(4\pi\kappa_h)`$ ($`D=3`$) and $`\nabla\delta a_0\to\theta(w-1)/(2\kappa_h)`$ ($`D=1`$). The front speed equals the largest slope $`c_0`$ of the normal-mode frequency.
   - The image strength tends to $`\beta\,\theta(c_0\lambda-d_s)`$, with $`\beta=g_\infty(x_s-h)/c_\phi`$ for $`D=3`$ ($`\kappa_a\ne\kappa_h/\gamma_3`$) and $`\beta=1`$ for $`D=1`$ (every $`\kappa_a`$). The pole terms of the localized mode in the anchor kernel are included.
   - Uniform bounds (9.17): $`\rho\lvert u_0(\rho\mathbf e_1,\lambda)\rvert\le C_\delta\rho^{-1/3}`$ for $`c_0\lambda\ge(1+\delta)\rho`$; $`\lvert\delta a_0(y,\lambda)\rvert\le C/\lvert y\rvert`$ for all $`\lambda`$; $`\int_0^\infty\lvert S_0(y,\lambda)\rvert\,\mathrm d\lambda\le C\lvert y\rvert^{-1/6}`$.
   - (9.18): for every $`\kappa_a`$, the $`\lambda`$-mean of the field on $`\mathbb Z^3`$ is $`-g_\infty(x-x_s)+\beta g_\infty(x-h)`$. For $`\kappa_a\ne\kappa_h/\gamma_3`$, the image term obeys $`\sup_\lambda\lvert I\rvert\le C/(d_xd_s^{1/6})+Ce^{-d_x/\xi}/d_s+O(e^{-(d_x+d_s)/\xi})`$, the pole terms of the anchor kernel included. For $`\kappa_a>\kappa_h/\gamma_3`$, the localized mode adds a persistent oscillation of size $`O(e^{-(d_x+d_s)/\xi})`$.
   - In order (O1) the uniform part and, for $`D=3`$, an image of strength $`1-\beta`$ never form: they are missing from the $`\lambda`$-mean.
5. **(9.11)** (criterion; cubic torus, order (O1), then $`\rho\to\infty`$ along $`\mathbf e_1`$ at fixed $`w`$, $`a`$, $`b\ne1`$).
   - For $`\kappa_a\ne\kappa_h/\gamma_3`$: $`\Delta_3^\perp\to-1`$ for $`w<1`$ and $`\to1/(b-1)`$ for $`w>1`$. If $`b>1+1/\varepsilon`$, then $`c_0\lambda_{\rm form}/\rho\to1`$, uniformly controlled in every later $`\lambda`$: formation within a $`\lambda`$ linear in the distance, at speed $`c_0`$ (equal to the front speed and the largest slope, independent of $`\kappa_a`$).
   - For every $`\kappa_a`$: if $`\lvert b-1\rvert<1/\varepsilon`$, then $`\lambda_{\rm form}=\infty`$ for all large $`\rho`$ (by the $`\lambda`$-mean).
   - The marginal $`b=1+1/\varepsilon`$ is not decided.
   - Far from the anchor ($`d_s,d_x\to\infty`$ at fixed $`\rho`$, then $`\rho\to\infty`$; $`\kappa_a\ne\kappa_h/\gamma_3`$): $`c_0\lambda_{\rm form}/\rho\to1`$ for every $`\varepsilon\in(0,1)`$.
6. **(9.12)** (criterion; cubic torus, radial $`\Phi`$, order (O1), then $`\ell\to\infty`$ at fixed $`w`$ and $`a=d_s/\ell>2`$, where the weighted reference $`\propto1-\theta_a`$ does not vanish).
   - If $`\theta_a<\varepsilon/(1+\varepsilon)`$, $`\kappa_a\ne\kappa_h/\gamma_3`$, and $`\Psi`$ is strictly decreasing at $`w_\varepsilon`$: (4.19) for $`\delta a^\perp`$ holds with $`c_0\lambda_{\rm form}/\ell\to w_\varepsilon\in[1,2]`$.
   - If $`\theta_a>\varepsilon/(1+\varepsilon)`$ (every $`\kappa_a`$): $`\lambda_{\rm form}=\infty`$ for all large $`\ell`$.
   - So the field forms in the mean by $`c_0\lambda\le2\ell`$ as $`a\to\infty`$, and never forms for $`a<(1+\varepsilon)/\varepsilon`$.
7. **(9.13)** (negative, control; ring, every $`\kappa_a>0`$, order (O1), then $`\rho\to\infty`$ at fixed $`w`$ and $`a=d_s/\rho>1`$, observation between source and anchor). Uniformly in $`\lambda`$, $`\nabla\delta a^\infty=F(\rho,\lambda)+F(2d_s-\rho-1,\lambda)+O(\rho^{-1/6})`$, with the free gradient $`F(n,\lambda)=(2\kappa_h)^{-1}\int_0^{2c_0\lambda}J_{2n+1}(u)\,\mathrm du`$; the localized mode and the pole terms of the anchor kernel are included. $`\Delta_1\to-1`$, $`-\frac12`$, $`0`$ on $`w<1`$, $`1<w<2a-1`$, $`w>2a-1`$, uniformly for $`w`$ at distance $`\ge\delta`$ from $`1`$ and $`2a-1`$. Across the image front, $`\Delta_1\in[-\frac12,0.14]+o(1)`$. For $`\varepsilon<\frac12`$, $`c_0\lambda_{\rm form}/\rho\to2a-1`$; for $`\varepsilon>\frac12`$, it tends to $`1`$. With the anchor far away ($`a\to\infty`$) and $`\varepsilon<\frac12`$, the place-dependent part does not form within any $`\lambda`$ linear in $`\rho`$.
8. **(9.14)** (formula; cubic torus, every $`\lambda\ge0`$, as $`L\to\infty`$; and the ring with $`\kappa_aL\ll\kappa_h`$, with corrections $`O(\kappa_aL/\kappa_h)`$ and $`T_U\simeq(L/\kappa_a)^{1/2}`$). $`\bar U=\bar U_{\rm st}[1-\cos(\lambda/T_U)]+O(L^{-1})\lvert\bar U_{\rm st}\rvert`$, with $`T_U=\sqrt{L^3c^{(L)}_\phi}\,[1+O(L^{-2})]`$, which depends on $`\kappa_a`$ only through $`c_\phi`$ and not on $`d_s`$. The slow mode carries the oscillating image $`-(1-\beta_L)g(x-h)`$.
9. **(9.15), (9.19)** (formula; ring, $`L`$ even, $`\kappa_aL\ge8\kappa_h`$, $`L\to\infty`$ at fixed $`\tau=c_0\lambda/L`$ and $`\alpha=d_s/L`$). The even modes in the band have the labels (9.19), $`k_jL=(2j+1)\pi-2\delta_j`$ with $`\delta_j=\arctan(2\kappa_h\sin k_j/\kappa_a)`$. $`\bar U`$ is the leading term of (9.15) plus a remainder $`R`$. The leading term is periodic with period $`2L/c_0`$ and lies between $`0`$ and $`2\bar U_{\rm st}`$. The remainder obeys $`\lvert R\rvert\le C[(1+\tau)/\kappa_a+\tau^{2/3}/(\kappa_hL^{1/3})+(1+\kappa_h^2/\kappa_a^2)\log L/(\kappa_hL)]`$, uniformly in $`\alpha\in[0,1]`$ and $`\tau\ge0`$. It is small against $`\lvert\bar U_{\rm st}\rvert`$ when $`\alpha(1-\alpha)\kappa_aL\gg\kappa_h(1+\tau)`$ and $`\tau\ll L^2`$. Together with items 3 and 4 (negative): the uniform part reaches its static value (9.1) in no order of the limits, on both graphs; it reaches it only as a $`\lambda`$-mean.
10. **(9.16)** (theorem, short argument; cubic torus, $`\kappa_a\ne\kappa_h/\gamma_3`$, grips square with a common $`\hat\beta`$). In the order $`L\to\infty`$, then $`d/\ell\to\infty`$, then $`\ell\to\infty`$ at fixed $`w`$, three properties of the description are available together at leading order in $`\ell/d`$:
    - the long-range mark (5.15)(a) and the weighing of 05-anchor within (A), or within (B) with $`R/d\to0`$ at fixed $`c`$, as properties of lowest eigenvectors. The weighing holds in its controlled regime, at order $`\mu^2`$ and leading order in the grip; for the lowest eigenvector of the stated contract it holds iff in addition (5.10) holds ((5.26) of 05-anchor for a pair);
    - the formation of the place-dependent part within a $`\lambda`$ linear in the distance at speed $`c_0`$, for every $`\varepsilon\in(0,1)`$, as a property of the evolution from $`\Omega`$.

    A weighing realized in the evolving state is not claimed. Formation fails for small $`\varepsilon`$ when the source or an observation place is at a distance from $`h`$ comparable to $`\rho`$, and it fails in order (O2).

## Consistency checks

1. **Dimensions.** $`[K_a^{-1}]=E^{-2}=[\delta a]`$ in (9.2). $`\beta=g/c_\phi`$ is dimensionless, and so are (9.11), (9.13). $`[T_U]=[(L^3c_\phi)^{1/2}]=E^{-1}=[\lambda]`$, and the ring scale $`L/c_0`$ also has dimension $`E^{-1}`$. $`[L/\kappa_h]=E^{-2}=[\bar U]`$ in (9.15), and each term of the bound on $`R`$ ($`1/\kappa_a`$, $`1/\kappa_h`$ times numbers) has dimension $`E^{-2}`$; $`\delta_j`$ in (9.19) is a number. In Step 6, $`[c_b]=[\lVert\gamma_b\rVert^{-2}]=E^4=[\chi][s^2]`$, as the pole term $`c_b/(s^2+\nu_b)`$ of $`\chi`$ requires. Passed.
2. **Comparison with (4.12)–(4.13) at small $`m_h`$.** For $`b\to\infty`$, (9.11) gives $`\Delta_3^\perp\to-\theta(1-w)`$. This is (4.12) at $`\mu=0`$, since $`e^0-1-0=0`$ for $`w>1`$, and it is the $`\mu\to0`$ limit of the bound (4.13). Far from the anchor, the unpinned anchored field forms like the pinned field at $`\mu\to0`$. Passed.
3. **Limit $`\kappa_a\to\infty`$** (a fixed cell). $`c_\phi\to\gamma_3/\kappa_h`$, so $`T_U\to(L^3\gamma_3/\kappa_h)^{1/2}`$ stays finite. $`\beta\to g_\infty(x_s-h)/g_\infty(0)<1`$: even a fixed cell takes only part of the force on $`\mathbb Z^3`$. For $`D=1`$ the anchor time $`2c_0/\kappa_a\to0`$. In (9.19), $`\delta_j\to0`$: the even modes become exactly $`\sin(n\pi y/L)`$, $`n`$ odd, those of a chain whose anchor cell is held fixed, and the terms in $`1/\kappa_a`$ of the bound in (9.15) vanish. (9.6) goes to $`\bar U_{\rm st}=-r(x_s,h)/2`$, which is (5.11) at $`1/\kappa_a=0`$. (9.11), (9.13) and (9.15) are unchanged at leading order. Passed.

## Open issues

- The bounds (9.17), (9.18) are stated without their constants. (9.17) uses two standard results: the dispersive bound $`\lambda^{-7/6}`$ of the lattice wave equation on $`\mathbb Z^3`$, and uniform Airy asymptotics of the low-label front. At $`\rho\le16`$ the code shows wakes of $`0.30`$ to $`0.16`$, decaying about as $`\rho^{-0.4}`$. So at these distances, formation at $`\varepsilon\lesssim0.3`$ is delayed beyond $`c_0\lambda\approx\rho`$, and the code's formation times are finite-window values.
- At the threshold $`\kappa_a=\kappa_h/\gamma_3`$ ($`D=3`$) the anchor kernel decays only as $`\lambda^{-1/2}`$. This member is excluded, as the question's note of 2026-10-26 (after round 2) permits: (9.10), the second part of (9.18), the profile and positive parts of (9.11) and (9.12), and (9.16) are not derived there. The statements that no formation occurs hold there.
- The constants of the kernels $`K_c`$, $`k_c`$ and of the pole terms (Steps 6 and 8) are not computed. The orders $`O(\rho^{-1/6})`$ on the line and $`C/(d_xd_s^{1/6})`$ on the cubic lattice are upper bounds.
- The shell criterion is treated only for radial $`\Phi`$ (question note (a)).
- The error terms of (9.14) are upper bounds. The code finds deviations far below them. The bound on $`R`$ in (9.15) is an upper bound with an unspecified constant $`C`$; the code finds $`\lvert R\rvert\le1.9(1+\tau)/\kappa_a`$ for $`\kappa_a=1,4`$, and $`\lvert R\rvert\approx0.06\,\tau^{2/3}L^{-1/3}`$ for a nearly fixed anchor cell.
- In order (O2) on the cubic torus, the part of the field from the modes other than the slow one is controlled beyond the wrap time only by (9.8). No criterion restricted to a window of $`\lambda`$ is studied.
- Item 4 uses the weighing of 05-anchor as quoted in words. Whether a weighing is realized in the evolving state, through a dynamical observable, is not studied (question note (c)).
- The ring with $`\kappa_aL`$ comparable to $`\kappa_h`$ is not treated. (9.14) and (9.15) are its two limits.

## Code

All files are under `code/v4/`. Each script runs from the project root with `.venv/Scripts/python.exe` and writes to `code/v4/output/`; every output there comes from the v4 run. "Exact solution" means the solution of the linear equations of the means at $`M\to\infty`$ (Step 1), computed from the eigen-decomposition of $`K_a`$ or by fourth-order Runge–Kutta. $`\kappa_h=1`$ ($`c_0=1`$).

- `check_made_field.py` (check; item 1). On the ring at $`L=64,96`$ and the cubic torus at $`L=8,12`$, with $`\kappa_a=1`$, the anchor at two distances from the source and three places each, it compares the image representation (9.4) with the exact (9.2) up to $`\lambda=3L`$. It also compares the force formula (9.5) with the exact place average, and checks the static split (9.6) and the static image strength 1. Output: `code/v4/output/made_field_check.txt`. The largest relative deviation is $`7.7\times10^{-6}`$ (trapezoid rule); the static split agrees to $`10^{-12}`$.
- `check_formation.py` (check; item 2). Outputs: `code/v4/output/formation_check.txt`, `code/v4/output/formation_Delta.csv`.
  - *Cubic torus.* $`L=64,96`$; Runge–Kutta with $`\mathrm d\lambda=0.05`$ up to $`\lambda=40`$, below the wrap time. Anchor far (antipode, $`d_s=55,83`$) and near ($`h=x_s-8\mathbf e_1`$); $`\rho=3,4,6,8,12,16`$ along $`\mathbf e_1`$. Reference: $`g_\infty(x-h)-g_\infty(x-x_s)`$, with $`g_\infty`$ from the Bessel-integral representation ($`g_\infty(0)=0.2527310`$).
  - *Order (O1) emulated.* The field at the probe places is the same at both sizes to $`2\times10^{-7}`$ (finite propagation), and the time-step error is $`9\times10^{-6}`$. The finite-$`L`$ place average equals $`-\lambda^2/2L^3`$ to $`0.5\%`$; it vanishes in order (O1), so $`\Delta_3^\perp=\delta a/{\rm ref}-1`$.
  - *Before the front:* $`\Delta_3^\perp=-1.000`$ for $`w<0.6`$ in all cases.
  - *Plateau* (mean over $`1.6<w\le3`$): it follows the finite-$`\rho`$ prediction $`-g_\infty(x-h)/{\rm ref}`$, i.e. $`1/(b-1)`$, over the range $`0.04`$ to $`2.0`$. Deviations: $`\le0.08`$ at $`\rho=3`$, $`\le0.025`$ at $`\rho=6`$, $`\le0.014`$ at $`\rho=8`$, $`\le0.006`$ at $`\rho=12,16`$.
  - *Wakes:* $`\max_{w>1.3}\lvert\Delta_3^\perp-{\rm pred}\rvert`$ falls from $`0.30`$ to $`0.16`$ (in units of the free field) between $`\rho=3`$ and $`16`$, about as $`\rho^{-0.4}`$, consistent with the $`O(\rho^{-1/3})`$ caustic wakes of Step 5.
  - *$`\lambda`$-mean in order (O1)* (computed, not simulated): $`(\beta-1)g_\infty(x-h)/{\rm ref}`$ with $`\beta=g_\infty(x_s-h)/c_\phi`$. For the far anchor it equals the finite-$`\rho`$ plateau prediction to $`0.001`$. For the near anchor it is $`0.354,0.483,0.736,0.986,1.484,1.981`$ for $`\rho=3,\dots,16`$, against $`1/(b-1)=0.375`$ to $`2.000`$.
  - *Formation times* (finite-window values; the window ends at $`w_{\max}=40/\rho=13.3`$ to $`2.5`$): at $`\varepsilon=0.5`$ (far anchor, $`L=96`$), $`c_0\lambda_{\rm form}/\rho=1.00,1.05,1.04,1.03,1.02,1.23`$ for $`\rho=3,\dots,16`$. ($`\lambda_{\rm form}`$ is the first $`\lambda`$ from which $`\lvert\Delta_3^\perp\rvert\le\varepsilon`$ up to the end of the window $`\lambda=40`$.) Where $`1/(b-1)>0.5`$ (near anchor at $`\rho\ge6`$, $`1/(b-1)=0.75`$ to $`2.0`$), there is no formation within the window, as (9.11) predicts. Since the $`\lambda`$-mean exceeds $`0.5`$ there, there is none at any later $`\lambda`$ either. The marginal members $`1/(b-1)=0.5=\varepsilon`$ ($`b=3`$) are not decided by (9.11); there the finite-$`\rho`$ corrections decide. For the near anchor at $`\rho=4`$ (plateau $`0.496`$, finite-$`\rho`$ prediction $`0.487`$), $`c_0\lambda_{\rm form}/\rho=9.91`$ at both sizes, just before the end of the window at $`w=10`$. For the far anchor at $`L=64`$, $`\rho=16`$ (plateau $`0.501`$, finite-$`\rho`$ prediction $`0.499`$), there is no formation within the window ($`w\le2.5`$). At $`\varepsilon=0.2,0.3`$ the wakes, which still exceed $`\varepsilon-1/(b-1)`$ at these $`\rho`$, delay formation to $`c_0\lambda/\rho\approx1.6`$–$`4.2`$ or beyond the window.
  - *Ring.* $`L=1024,2048`$, exact.
    - (a) $`a=2`$, $`\rho=20,40,80,160`$: the plateau is $`-0.500`$ (to $`0.004`$) on $`1.4<w<2.6`$ and $`0.000`$ (to $`0.007`$) on $`w>3.4`$. $`c_0\lambda_{\rm form}/\rho=3.08,3.06,3.03,3.02`$ at $`\varepsilon=0.25`$ (prediction 3) and $`1.34,1.20,1.12,1.02`$ at $`\varepsilon=0.6`$ (prediction 1), identical at both sizes. $`\max_{w>1.4}\lvert\Delta_1\rvert=0.577,0.561,0.543,0.530`$. Across the image front ($`2.6<w<3.4`$), $`\Delta_1`$ lies in $`[-0.544,0.069]`$ at $`\rho=20`$ and in $`[-0.515,0.117]`$ at $`\rho=160`$, approaching the range $`[-\frac12,0.14]`$ of Step 8.
    - (b) $`d_s=400`$, $`\rho=10,20,40,80`$: $`\Delta_1`$ has mean $`-0.500`$ on $`1.4\rho<c_0\lambda<0.9(2d_s-\rho)`$, with largest deviation $`0.11`$ to $`0.045`$. Formation at $`\varepsilon=0.25`$ occurs at $`c_0\lambda=2d_s-\rho+3`$, i.e. $`c_0\lambda_{\rm form}/\rho=79,39,19,9`$.
    - (c) Uniform form of Step 8 ($`L=2048`$, $`a=2`$, $`c_0\lambda\le8\rho`$, which covers the image front at $`w=3`$ and the later regime). The Bessel form of $`F`$ agrees with the free-ring gradient to $`1.2\times10^{-7}`$. $`\sup_\lambda\kappa_h\lvert\nabla\delta a-F(\rho)-F(m)\rvert`$ for $`\rho=20,40,80,160`$ is $`0.440,0.406,0.369,0.331`$ at $`\kappa_a=0.25`$, $`0.215,0.182,0.152,0.125`$ at $`\kappa_a=1`$, and $`0.065,0.052,0.042,0.034`$ at $`\kappa_a=4`$. So it decreases at every $`\kappa_a`$, with local exponents from $`0.12`$ to $`0.32`$ that grow with $`\rho`$. It is larger for the slower anchor (relaxation time $`2c_0/\kappa_a`$), as Step 8 states. The localized eigenvalue equals $`2\kappa_h+\sqrt{4\kappa_h^2+\kappa_a^2}`$ to six digits.
  - *Above the threshold* ($`\kappa_a=8>\kappa_h/\gamma_3=3.957`$; $`L=64`$, near anchor, same window). The localized eigenvalue from $`1+\kappa_a\gamma_b(0)=0`$ on $`\mathbb Z^3`$ and from a sparse eigen-solver agree: $`\nu_b=14.789619`$. Its share $`\psi_b(x)\psi_b(x_s)/\nu_b`$ at the probes is below $`10^{-16}`$. The plateau follows $`1/(b-1)`$ from $`0.437`$ to $`1.970`$ (prediction at finite $`\rho`$: $`0.357`$ to $`1.997`$; here $`\beta=0.026`$, and the image arrives inside the window). The $`\lambda`$-mean in order (O1) is $`0.348`$ to $`1.944`$. In the window, $`\max\lvert I\rvert\,d_xd_s^{1/6}=0.0037`$ at all six $`\rho`$, against $`0.0011`$ for $`\kappa_a=1`$; here $`I`$ is the near-anchor field minus the far-anchor field, which is the free field in the window. Formation at $`\varepsilon=0.5`$ occurs within the window only for $`\rho=3,4`$ ($`c_0\lambda_{\rm form}/\rho=3.83`$, $`9.90`$); for $`\rho\ge6`$ the $`\lambda`$-mean exceeds $`0.5`$, so there is no formation at any later $`\lambda`$.
- `check_uniform.py` (check; item 3). On the cubic torus at $`L=8,12,16,20`$ with $`\kappa_a=1`$ (Runge–Kutta, $`\mathrm d\lambda=0.05`$, over $`2.2\pi T_U`$), plus $`L=12`$ with a farther anchor and with $`\kappa_a=4`$, it compares $`\bar U`$ with (9.14). The relative deviations are $`3.2\times10^{-4}`$, $`1.5\times10^{-4}`$, $`8.3\times10^{-5}`$, $`5.5\times10^{-5}`$ for $`L=8,12,16,20`$, $`1.3\times10^{-4}`$ for the farther anchor and $`9.6\times10^{-4}`$ for $`\kappa_a=4`$. Over all six runs, $`\nu_0^{-1/2}/\sqrt{L^3c^{(L)}_\phi}`$ lies between $`1.00001`$ and $`1.00017`$ (from a sparse eigen-solver): $`1.00006`$ to $`1.00001`$ for $`L=8`$ to $`20`$, $`1.00003`$ for the farther anchor, $`1.00017`$ for $`\kappa_a=4`$. The first minimum lies at $`\lambda/(\pi\sqrt{L^3c^{(L)}_\phi})=1.000\pm0.0002`$, where $`\bar U/\bar U_{\rm st}=2.000`$. The place-dependent part of the slow term matches $`-(1-\beta_L)g(x-h)`$ to $`0.03/L^2`$ (relative) in the five runs with $`\kappa_a=1`$ and to $`0.05/L^2`$ for $`\kappa_a=4`$. On the ring at $`L=128,256,512`$ ($`d_s=L/4`$, exact), it compares $`\bar U`$ with (9.15). The deviation stays at about 3 in absolute value for $`c_0\lambda\le2L`$ (relative $`30/L`$) and about 5 for $`c_0\lambda\le4L`$. The first minimum lies at $`c_0\lambda/L=1+4.1/L`$, with $`\bar U/\bar U_{\rm st}=2.000`$, consistent with the period lengthening $`4\kappa_h/(\kappa_aL)`$ of (9.19); $`\bar U(2L/c_0)/\bar U_{\rm st}=0.019`$, $`0.005`$, $`0.0013`$.
  - *Discrete derivation of (9.15)* ($`L=128,256,512`$, $`\kappa_a=1,4`$, $`\alpha=\frac18,\frac14,\frac12`$, exact). The $`L/2`$ even in-band labels of (9.19) agree with the eigenvalues of $`K_a`$ to $`2\times10^{-15}`$, and the top eigenvalue equals the line value $`2\kappa_h+\sqrt{4\kappa_h^2+\kappa_a^2}`$ to six digits. The exact mode sum of Step 9 reproduces $`\bar U`$ to $`2\times10^{-7}`$ or better; the difference is the localized mode's share, below its bound $`2/(\kappa_aL)`$. Over $`\tau\le8`$, $`\max\lvert R\rvert\kappa_a/(1+\tau)`$ lies between $`1.16`$ and $`1.88`$ in all 18 cases, independent of $`L`$ and of $`\kappa_a`$: the remainder grows linearly in $`\tau`$ with slope $`\propto1/\kappa_a`$, as bounded in (9.15). For a nearly fixed anchor cell ($`\kappa_a=10^4`$, $`\alpha=\frac14`$), $`\max_{\tau\le T}\lvert R\rvert/(T^{2/3}L^{-1/3})=0.058`$ to $`0.061`$ for $`T=8,32`$ and all three sizes, the dispersive term of (9.15).
  - On the weak-anchor ring ($`\kappa_aL=0.128,0.032`$), (9.14) holds to $`10^{-4}`$. Outputs: `code/v4/output/uniform_check.txt`, `code/v4/output/uniform_U.csv`.

## Methods used

- Heisenberg equations of a quadratic contract; displaced lowest eigenvector; Trotter–Kato convergence of compressions
- Normal modes, rank-one (Sherman–Morrison) updates, secular equation, interlacing
- Duhamel formula, Volterra equation, Laplace transform
- Dirichlet's simultaneous approximation (recurrence), mean values of quasi-periodic functions
- Finite propagation of power series; stationary phase; lattice Green functions; Dirichlet integral
- Mean-value property of harmonic functions; discrete secular equation of the anchored ring, telescoping bounds of mode sums
- Contour shift of entire integrands; stationary phase uniform in a parameter, folds, Airy asymptotics; dispersive bound of the lattice wave equation; Poisson summation
- $`\lambda`$-means of spectral integrals, Riemann–Lebesgue lemma, convolution bounds (Young)
- Residue of the localized mode in the complete response; resolvent identity for the pole terms of the anchor kernel
- Laplace pairs of Bessel functions; Landau's bound $`\lvert J_\nu\rvert\le0.68\,\nu^{-1/3}`$
- Cauchy–Schwarz bounds
- Numerics: eigen-decomposition, fourth-order Runge–Kutta, trapezoid rule for Volterra equations
