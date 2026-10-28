# Weighing of the own mark and of the bond against the grip, oscillator cells

- **Subproject:** 08-ilang-propagation
- **Package:** 02-grip-weight
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-24

## Setup and assumptions

- **Field** (M8), as in the question: oscillator cells on $`X_f`$ (ring, square or cubic torus of side $`L\ge3`$, $`N_f=L^D`$ cells). With the graph Laplacian $`\Delta`$, $`K:=\kappa_h\Delta+m_h^2\mathbb 1`$ and $`H=\tfrac12p\cdot p+\tfrac12q\cdot Kq`$; normal modes $`\omega_k^2=m_h^2+\kappa_h\sum_{j=1}^D4\sin^2(k_j/2)`$, $`k\in(2\pi/L)\mathbb Z_L^D`$; pinning length $`\ell:=\sqrt{\kappa_h}/m_h`$. The $`M`$ places of a cell are the $`M`$ lowest number states of $`\tfrac12(p_x^2+q_x^2)`$, and at finite $`M`$ the whole total contract $`C`$ (field, bodies, source) is compressed, $`C_M:=\Pi C\Pi`$ (choice of this package).
- **Bodies** (M8, A15): held Model D bodies, $`\tau=0`$, no term of their own. The labels $`(x_b,k,\sigma)`$ are conserved ($`S`$ commutes with $`C`$), and in that sector $`S`$ acts as $`\mu:=\sigma M_k`$, $`M_k=m+2\pi k/(N\lambda_0)>0`$. Grip classes (G2), (G) as in the question; for (G), $`F=F(0)+\theta f`$.
- **Source** (M8, A15): $`g_sq_{x_s}`$, first order in $`g_s`$. **State** (M9, A11): as in the question; Step 1 fixes the sense of $`M\to\infty`$.
- **Definitions** of the question: cost, $`C^{(1)}`$, $`C^{\rm mark}`$, weight $`W`$, bond, $`\rho_{\rm mark}`$, $`\rho_{\rm bond}`$. Notation: $`\langle\cdot\rangle_0`$ is the lowest eigenvector of $`H`$ (a Gaussian); $`a_n:=\langle F^{(n)}(q_x)\rangle_0`$ ($`n\ge0`$; a Gaussian average of variance $`w_0`$); $`\Delta\phi:=\phi(x)-\phi(x')`$.
- **Dimensions:** $`[C]=E`$, $`[q]=E^{-1/2}`$, $`[K]=E^2`$, $`[F]=1`$, $`[\mu]=E`$, $`[g_s]=E^{3/2}`$.
- **Standard mathematics** (allowed by the question): Gaussian lowest eigenvector of a positive quadratic contract; Sherman–Morrison, matrix determinant lemma; min-max; Rayleigh–Schrödinger perturbation theory for an isolated eigenvalue; Wick's theorem and the Mehler (Hermite) expansion for a Gaussian pair; lattice Fourier sums and their continuum limits.

## Derivation

### Step 1. Sector, limit $`M\to\infty`$, shift by the made field

In the sector of held bodies at $`x_i`$ with labels $`(k_i,\sigma_i)`$: $`C=H+g_sq_{x_s}+\sum_i\mu_iF(q_{x_i})`$.

*Limit.* $`\mathrm{ran}\Pi_M`$ grows with $`M`$, and the union of these subspaces (finite sums of products of Hermite functions) is a form core of $`C`$. By min-max the lowest eigenvalue of $`C_M`$ is nonincreasing in $`M`$ and tends to $`\inf\mathrm{spec}C`$: to the lowest eigenvalue of $`C`$ if it exists, to $`-\infty`$ if $`C`$ is unbounded below. Statements about $`C`$ are statements about this limit (Code (ii)).

*Shift.* Let $`\phi:=-g_sK^{-1}e_{x_s}`$, $`\phi(x)=-g_sG(x-x_s)`$ (the made field), and $`U:=\exp(-i\sum_x\phi(x)p_x)`$. Then $`U^\dagger q_xU=q_x+\phi(x)`$, and with $`K\phi=-g_se_{x_s}`$:
```math
U^\dagger CU=H+\sum_i\mu_iF\bigl(q_{x_i}+\phi(x_i)\bigr)-\tfrac12g_s^2G(0).
\qquad\text{(2.1)}
```
So with the source every eigenvalue is the one without the source for the shifted grips $`F_{c_i}(q):=F(q+c_i)`$, $`c_i=\phi(x_i)`$, minus a term that does not depend on the bodies. For one body, the eigenvalue $`E[F]`$ of $`H+\mu F(q_{x_b})`$ does not depend on $`x_b`$ (translations of the torus). The $`s`$-expansion commutes with the shift ($`(sF)_c=sF_c`$). Hence, at first order in $`g_s`$, for $`X\in\{\text{cost},C^{(1)},C^{\rm mark}\}`$:
```math
W_X(x)-W_X(x')=\partial_cX[F_c]\big|_{c=0}\,\Delta\phi,\qquad
\rho_{\rm mark}=\frac{\partial_c\ln C^{\rm mark}[F_c]}{\partial_c\ln C^{(1)}[F_c]}\Big|_{c=0}.
\qquad\text{(2.2)}
```
Every weight at first order in $`g_s`$ thus has the profile $`\Delta\phi`$, and $`\rho_{\rm mark}`$ does not depend on $`x,x'`$ or on the distance to the source.

*Fixed by the total contract.* $`C^{(1)}=\frac{d}{ds}E_0\bigl(C_\emptyset+s(C_b-C_\emptyset)\bigr)|_{s=0}`$, where $`C_b,C_\emptyset`$ are the total contracts with and without the body and $`C_b-C_\emptyset=\mu F(q_{x_b})`$ (the body has no term of its own). So the cost, $`C^{(1)}`$ and $`C^{\rm mark}`$ are fixed by the two total contracts, whatever pair term the single-body part $`\mu F(0)`$ is listed in (A5, M6). The lowest eigenvalue of the field alone drops out. By Hellmann–Feynman, $`C^{(1)}=\mu\langle F\rangle_0=\mu a_0`$ for every grip, so $`\partial_c\ln C^{(1)}=a_1/a_0`$ for every level and both branches.

### Step 2. Field constants and the made field

```math
\begin{aligned}
&G(x)=\tfrac1{N_f}\textstyle\sum_k e^{ik\cdot x}\omega_k^{-2},\quad G_0:=G(0),\quad w_0:=\langle q_x^2\rangle_0=\tfrac1{2N_f}\textstyle\sum_k\omega_k^{-1},\quad g_r(\nu):=[(K+\nu^2)^{-1}]_{x+r,x},\ g:=g_0,\\
&c_r(\tau):=\langle q_{x+r}e^{-(H-E_f)\tau}q_x\rangle_0=\tfrac1{2N_f}\textstyle\sum_k\cos(k\cdot r)\,e^{-\omega_k\tau}\omega_k^{-1},\quad J_n(r):=\int_0^\infty c_r(\tau)^n\,d\tau,\quad J_n:=J_n(0),\\
&J_1(r)=\tfrac12G(r),\quad \textstyle\int_0^\infty g_r(\nu)^2d\nu=2\pi J_2(r),\quad 0<c_r(\tau)\le c_0(\tau)\le w_0,\quad J_n(r)\le w_0^{\,n-1}J_1(r),\quad J_2\le\tfrac12w_0G_0.
\end{aligned}
\qquad\text{(2.3)}
```
Here $`g_r(\nu)=2\int_0^\infty c_r(\tau)\cos\nu\tau\,d\tau`$ and Parseval give the integral of $`g_r^2`$. $`c_r>0`$ because $`c_r(\lvert\tau\rvert)`$ is the kernel of $`(-\partial_\tau^2+K)^{-1}`$, whose semigroup preserves positivity ($`K`$ has nonpositive off-diagonal entries). $`c_r\le c_0`$ by Cauchy–Schwarz for $`e^{-(H-E_f)\tau/2}q_{x+r}\Omega`$ and $`e^{-(H-E_f)\tau/2}q_x\Omega`$, with translation invariance; $`c_0`$ is decreasing.

*Made field at large distances* ($`L\to\infty`$ with $`L\gg\ell`$, then $`\lvert d\rvert\gg1`$; continuum limit of the Fourier integral, relative corrections $`O(\lvert d\rvert^{-2},\ell^{-2})`$):
```math
G(d)\simeq
\begin{cases}
\dfrac{e^{-\alpha\lvert d\rvert}}{2\kappa_h\sinh\alpha}\ \ (\cosh\alpha=1+\tfrac1{2\ell^2},\text{ exact on the chain})\ \simeq\dfrac{\ell}{2\kappa_h}e^{-\lvert d\rvert/\ell}, & D=1,\\[2mm]
\dfrac{K_0(\lvert d\rvert/\ell)}{2\pi\kappa_h}\to\dfrac{\ln(2\ell/\lvert d\rvert)-\gamma_E}{2\pi\kappa_h}\ (\lvert d\rvert\ll\ell),\ \ \dfrac{1}{2\pi\kappa_h}\sqrt{\dfrac{\pi\ell}{2\lvert d\rvert}}e^{-\lvert d\rvert/\ell}\ (\lvert d\rvert\gg\ell), & D=2,\\[2mm]
\dfrac{e^{-\lvert d\rvert/\ell}}{4\pi\kappa_h\lvert d\rvert}\to\dfrac1{4\pi\kappa_h\lvert d\rvert}\ (1\ll\lvert d\rvert\ll\ell), & D=3.
\end{cases}
\qquad\text{(2.4)}
```
Below the pinning length the made field is long-range for $`D=3`$ ($`1/\lvert d\rvert`$), logarithmic for $`D=2`$ and linear for $`D=1`$; above it, it decays as $`e^{-\lvert d\rvert/\ell}`$. On a finite torus $`G`$ is the sum over images; for $`L\ll\ell`$, $`G(d)=1/(N_fm_h^2)+G_{\rm per}(d)+O(m_h^2)`$, and the uniform part cancels in $`\Delta\phi`$.

### Step 3. (G2): existence and cost

With one body (no source), $`C=H+\mu F_0+\mu F_1q_b+\mu F_2q_b^2`$ is quadratic, with matrix $`K':=K+a\,e_be_b^{T}`$, $`a:=2\mu F_2`$. By the determinant lemma $`\det K'=\det K\,(1+aG_0)`$, and by interlacing at most one eigenvalue of $`K'`$ lies below the spectrum of $`K`$. So $`K'>0`$ iff $`D_\mu:=1+aG_0>0`$. For $`D_\mu<0`$, $`C`$ has a direction of negative curvature. For $`D_\mu=0`$, $`K'`$ has the null vector $`K^{-1}e_b`$, on which the linear term is $`\mu F_1G_0\ne0`$. In both cases $`C`$ is unbounded below. With Step 1:
```math
\text{a lowest eigenvector exists }(M\to\infty)\iff 1+2\sigma M_kF_2G_0>0;\ \text{otherwise the lowest eigenvalue of }C_M\to-\infty .
\qquad\text{(2.5)}
```
For both branches this reads $`2M_k\lvert F_2\rvert G_0<1`$. For two bodies, the condition is $`D_1,D_2>0`$ and $`D_1D_2>a_1a_2G(r)^2`$.

For $`D_\mu>0`$: $`E=\mu F_0+\frac12\mathrm{Tr}\sqrt{K'}-\frac12\mu^2F_1^2(K'^{-1})_{bb}`$, and $`(K'^{-1})_{bb}=G_0/D_\mu`$ by Sherman–Morrison. The zero-point part follows from three facts: $`\sqrt A=\pi^{-1}\int_0^\infty dz\,z^{-1/2}A(A+z)^{-1}`$; $`\mathrm{Tr}[(K'+z)^{-1}-(K+z)^{-1}]=\partial_z\ln(1+a[(K+z)^{-1}]_{bb})`$; and an integration by parts ($`z=\nu^2`$). Together they give $`\frac12\mathrm{Tr}(\sqrt{K'}-\sqrt K)=Z(a):=\frac1{2\pi}\int_0^\infty\ln(1+a\,g(\nu))\,d\nu`$; for one mode this is $`\frac12(\sqrt{\omega^2+a}-\omega)`$. $`F\to sF`$ maps $`a\to sa`$, and $`Z'(0)=\frac1{2\pi}\int g\,d\nu=\frac12w_0`$. Hence
```math
\text{cost}=\mu F_0-\frac{\mu^2F_1^2G_0}{2D_\mu}+Z(2\mu F_2),\qquad
C^{(1)}=\mu(F_0+F_2w_0)=\mu\langle F\rangle_0,\qquad
C^{\rm mark}=-\frac{\mu^2G_0}{2D_\mu}\bigl(F_1^2+\zeta\bigr),
\qquad\text{(2.6)}
```
with $`\chi(y):=(y-\ln(1+y))/y^2=\int_0^1t\,dt/(1+ty)`$ and
```math
\zeta:=\frac{4F_2^2}{\pi G_0}\int_0^\infty g(\nu)^2\,(1+2\mu F_2G_0)\,\chi\bigl(2\mu F_2g(\nu)\bigr)\,d\nu\ \ge0,\qquad
\zeta=\frac{4F_2^2J_2}{G_0}\bigl[1+O(\mu F_2G_0)\bigr].
\qquad\text{(2.7)}
```
$`\zeta`$ is the zero-point part of the mark beyond first order ($`\zeta=-2D_\mu[Z(a)-\tfrac12aw_0]/(\mu^2G_0)`$). Since $`g(\nu)<G_0`$ for $`\nu>0`$, $`\partial_y[(1+yG_0)/(1+tyg)]=(G_0-tg)/(1+tyg)^2>0`$. So, at fixed $`F_2^2\neq0`$, $`\zeta`$ is strictly increasing in $`\sigma M_kF_2`$. $`C^{\rm mark}<0`$ for every (G2) grip with (2.5).

### Step 4. (G2): weights

$`F_c=F(\cdot+c)`$ has $`F_0\to F_0+F_1c+F_2c^2`$, $`F_1\to F_1+2F_2c`$, $`F_2\to F_2`$. So $`a`$, $`D_\mu`$, $`Z`$, $`\zeta`$ do not depend on $`c`$: the zero-point part is not weighed. By (2.2) and (2.6):
```math
W(x)-W(x')=\frac{\mu F_1}{D_\mu}\Delta\phi,\qquad
\Delta W^{(1)}=\mu F_1\,\Delta\phi,\qquad
\Delta W^{\rm mark}=-\frac{2\mu^2F_1F_2G_0}{D_\mu}\Delta\phi .
\qquad\text{(2.8)}
```

### Step 5. (G): order $`\theta^2`$

At $`\theta=0`$ the lowest eigenvalue of $`C=H+\mu F(0)`$ is nondegenerate, with gap $`m_h`$. Rayleigh–Schrödinger theory with $`V=\mu\theta f(q_b)`$ gives $`E=E_f+\mu F(0)+\mu\theta\langle f\rangle_0-\mu^2\theta^2\int_0^\infty\langle\delta f(q_b(\tau))\,\delta f(q_b(0))\rangle_0d\tau+O(\theta^3)`$. Here $`\delta f=f-\langle f\rangle_0`$ and $`q(\tau)=e^{(H-E_f)\tau}qe^{-(H-E_f)\tau}`$, by $`\sum_{n\ne0}\lvert V_{n0}\rvert^2/(E_n-E_0)=\int_0^\infty\langle\delta V e^{-(H-E_0)\tau}\delta V\rangle d\tau`$. By Wick's theorem, $`(q_b(\tau),q_b(0))`$ has the generating function of a Gaussian pair with variances $`w_0`$ and covariance $`c_0(\tau)`$. The Mehler expansion then gives $`\langle\delta F(q_b(\tau))\delta F(q_b(0))\rangle_0=\sum_{n\ge1}a_n^2c_0(\tau)^n/n!`$. For $`F`$ with $`\sum_na_n^2w_0^n/n!=\mathrm{Var}F(q_x)<\infty`$ (e.g. polynomial, or bounded with bounded derivatives):
```math
\text{cost}=\mu a_0-\mu^2S+O(\theta^3),\quad C^{(1)}=\mu a_0=\mu\bigl(F(0)+\theta\langle f\rangle_0\bigr),\quad C^{\rm mark}=-\mu^2S+O(\theta^3),\quad S:=\sum_{n\ge1}\frac{a_n^2J_n}{n!}>0 .
\qquad\text{(2.9)}
```
Under the shift, $`a_n\to\langle F^{(n)}(q_x+c)\rangle_0`$ with $`\partial_ca_n=a_{n+1}`$; by (2.2):
```math
\Delta W^{(1)}=\mu a_1\Delta\phi,\qquad \Delta W^{\rm mark}=-2\mu^2T\,\Delta\phi+O(\theta^3),\qquad T:=\sum_{n\ge1}\frac{a_na_{n+1}J_n}{n!}.
\qquad\text{(2.10)}
```
For (G), $`a_n=\theta\langle f^{(n)}\rangle_0`$ ($`n\ge1`$), so $`S,T=O(\theta^2)`$: the mark and its weight first appear at order $`\theta^2`$.

*Where this eigenvalue is the lowest.* If $`f`$ is bounded, the eigenvalue stays isolated and lowest for $`2\lvert\theta\rvert M_k\sup\lvert f\rvert<m_h`$, because each eigenvalue moves by at most $`\lVert V\rVert`$. If $`\mu\theta f(q)\to-\infty`$ faster than $`q^2`$, $`C`$ has no lowest eigenvalue for $`\theta\ne0`$. Then (2.9) describes the eigenvalue of $`C_M`$ connected to the lowest one, and it is the lowest of $`C_M`$ only for $`\lvert\theta\rvert`$ below a bound that tends to 0 as $`M\to\infty`$. The Taylor coefficients of $`C_M`$ converge to (2.9) as $`M\to\infty`$ (Code (ii)).

### Step 6. Bond

Two held bodies sit at $`x_1`$ and $`x_2=x_1+\mathbf r`$, with labels $`\mu_i`$, grips $`F^{(i)}`$ of one class and no pair term between them. Define $`U(\mathbf r):=\text{cost}_{12}-\text{cost}_1-\text{cost}_2`$, fixed by four lowest eigenvalues; its $`\mathbf r`$-dependence is the bond. The cross term of second-order perturbation theory in $`V_1+V_2`$, with the Mehler expansion for the Gaussian pair $`(q_{x_2}(\tau),q_{x_1}(0))`$ of covariance $`c_{\mathbf r}(\tau)`$, gives
```math
U(\mathbf r)=-2\mu_1\mu_2\sum_{n\ge1}\frac{a_n^{(1)}a_n^{(2)}J_n(\mathbf r)}{n!}+O(\mu^3);\qquad \text{(G2): }U=-\mu_1\mu_2\bigl[F_1^{(1)}F_1^{(2)}G(\mathbf r)+4F_2^{(1)}F_2^{(2)}J_2(\mathbf r)\bigr]+O(\mu^3).
\qquad\text{(2.11)}
```
$`O(\mu^3)`$ is third order in the body–field coupling ($`O(\theta^3)`$ for (G)). For a common grip and $`\sigma_1=\sigma_2`$, $`U=-2\mu_1\mu_2S(\mathbf r)<0`$ at this order (attraction through the field); for $`\sigma_1=-\sigma_2`$, $`U>0`$. For a common grip $`F`$, the shift $`c_i=\phi(x_i)`$ gives, with $`T(\mathbf r):=\sum_na_na_{n+1}J_n(\mathbf r)/n!`$ and $`S(\mathbf r):=\sum_na_n^2J_n(\mathbf r)/n!`$ (so $`U=-2\mu_1\mu_2S(\mathbf r)`$):
```math
\Delta W_{\rm bond}=-2\mu_1\mu_2(\Delta\phi_1+\Delta\phi_2)\,T(\mathbf r)+O(\mu^3),\qquad \Delta\phi_1+\Delta\phi_2=2m_{\mathbf r}\,\Delta\bar\phi,
\qquad\text{(2.12)}
```
where $`\Delta\bar\phi:=\phi(\bar x)-\phi(\bar x')`$ at the midpoints ($`\bar x=x_1+\mathbf r/2`$, $`\mathbf r`$ with even components) and $`m_{\mathbf r}`$ is the *midpoint factor*. For a far reference ($`\phi(\bar x')\to0`$) and $`d:=\lvert\bar x-x_s\rvert\gg\lvert\mathbf r\rvert`$, (2.4) gives $`m_{\mathbf r}=1+(\mathbf r\cdot\nabla)^2\phi/(8\phi)+O(\lvert\mathbf r\rvert^4/d^4)`$:
- $`D=3`$, $`1\ll d\ll\ell`$: $`m_{\mathbf r}-1=(3(\mathbf r\cdot\hat d)^2-\lvert\mathbf r\rvert^2)/(8d^2)`$;
- $`D=2`$, $`d\ll\ell`$: $`m_{\mathbf r}-1=(2(\mathbf r\cdot\hat d)^2-\lvert\mathbf r\rvert^2)/(8d^2[\ln(2\ell/d)-\gamma_E])`$;
- $`D=1`$, both bodies on one side: $`m_r=\cosh(\alpha r/2)`$ exactly on the chain;
- $`d\gg\ell`$, every $`D`$: $`m_{\mathbf r}-1=(\mathbf r\cdot\hat d)^2/(8\ell^2)`$.

If the pair is referred to $`x_1`$ instead of $`\bar x`$, the factor becomes $`(\Delta\phi_1+\Delta\phi_2)/(2\Delta\phi_1)=1+(\mathbf r\cdot\nabla\phi)/(2\phi)+\dots`$. That is a first-order error: $`-(\mathbf r\cdot\hat d)/(2d)`$ for $`D=3`$, $`d\ll\ell`$, and $`-(\mathbf r\cdot\hat d)/(2\ell)`$ for $`d\gg\ell`$.

*(G2) exactly.* The exact pair cost is the two-body form of Step 3, $`U=U_{\rm cl}+Z_b`$. In it, the shift changes only $`v_i:=\mu_iF_1`$, with $`\partial_{c_i}v_i=(2F_2/F_1)v_i`$, and leaves $`K'`$ unchanged. With $`a_i=2\mu_iF_2`$, $`D_i=1+a_iG_0`$:
```math
U_{\rm cl}=-\tfrac12v^{T}\mathbb M v,\quad \mathbb M_{ij}:=(K'^{-1})_{x_ix_j}-\delta_{ij}\frac{G_0}{D_i},\quad
Z_b=\frac1{2\pi}\int_0^\infty\ln\Bigl[1-\frac{a_1a_2\,g_{\mathbf r}^2}{(1+a_1g)(1+a_2g)}\Bigr]d\nu,\quad
\Delta W_{\rm bond}=-\frac{2F_2}{F_1}\sum_i\Delta\phi_i\,v_i(\mathbb Mv)_i .
\qquad\text{(2.13)}
```
The zero-point part $`Z_b`$ of the bond is not weighed.

### Step 7. Weighing ratios and which grips weigh

*Reference and excluded members.* Step 1 gives $`\Delta W^{(1)}/C^{(1)}=\Delta\phi\,a_1/a_0`$ for every level and both branches. For the bond, the reference is a single body at the midpoint, $`\Delta\bar\phi\,a_1/a_0`$. When $`\mu_1+\mu_2\ne0`$ this equals the pair's $`C^{(1)}`$ per unit referred to the midpoint. When $`\mu_1+\mu_2=0`$ (same level, opposite branches) the pair's $`C^{(1)}`$ vanishes, and only the single-body reference is defined. Excluded members:
- $`a_0=\langle F\rangle_0=0`$: $`C^{(1)}=0`$ for every level; in (G2), $`F_0=-F_2w_0`$;
- $`a_1=\langle F'\rangle_0=0`$: $`C^{(1)}`$ is not weighed; in (G2) this is excluded by $`F_1\ne0`$;
- $`\Delta\bar\phi=0`$.

In (G2) $`C^{\rm mark}`$ and $`U`$ never vanish: $`C^{\rm mark}<0`$, and $`U_{\rm cl}`$ and $`Z_b`$ have the same sign.

*(a) Order $`\mu^2`$, every grip of (G).* From (2.2) and (2.9)–(2.12):
```math
\rho_{\rm mark}=\rho(0),\qquad \rho_{\rm bond}=m_{\mathbf r}\,\rho(\mathbf r),\qquad \rho(\mathbf r):=\frac{2a_0\,T(\mathbf r)}{a_1\,S(\mathbf r)} .
\qquad\text{(2.14)}
```
$`\mu`$ cancels. At this order both ratios are therefore the same for every level and both branches (for the bond, for every pair of labels), and they do not depend on the distance to the source.

*(b) (G2), exact in the grip.* (2.6)–(2.8) and (2.13) give
```math
\rho_{\rm mark}=\frac{4F_2\langle F\rangle_0}{F_1^2+\zeta(\sigma M_kF_2)},
\qquad\text{(2.15)}
```
```math
\rho_{\rm bond}=\frac{4F_2\langle F\rangle_0}{F_1^2+\zeta_b}\sum_iw_i\frac{\Delta\phi_i}{\Delta\bar\phi},\qquad
\zeta_b:=\frac{F_1^2Z_b}{U_{\rm cl}}=\frac{4F_2^2J_2(\mathbf r)}{G(\mathbf r)}\bigl[1+O(u)\bigr],\qquad w_i:=\frac{v_i(\mathbb Mv)_i}{v^T\mathbb Mv},
\qquad\text{(2.16)}
```
with $`u:=2\max_iM_{k_i}\lvert F_2\rvert G_0`$. Here $`\sum_iw_i=1`$, and $`w_i=\frac12`$ for equal labels, where the sum is $`m_{\mathbf r}`$; in general $`w_i=\frac12+O(uG(\mathbf r)/G_0)`$. Derivation: $`\Delta W_{\rm bond}=(4F_2/F_1)U_{\rm cl}\sum_iw_i\Delta\phi_i`$ by (2.13), and $`U=U_{\rm cl}(1+\zeta_b/F_1^2)`$. So for unequal labels the bond is weighed at the weighted place $`\sum_iw_ix_i`$, not at the midpoint. Referred to the midpoint, this adds $`(w_1-\frac12)(\Delta\phi_1-\Delta\phi_2)/\Delta\bar\phi=O\bigl(u\,\tfrac{G(\mathbf r)}{G_0}\,\tfrac{\lvert\mathbf r\rvert}{\min(d,\ell)}\bigr)`$ to the sum, a label dependence beyond order $`\mu^2`$. Code (i) reproduces (2.15) and (2.16) from exact lowest eigenvalues (Code section).

*(c) Smooth grips.* Let $`F(0)\ne0`$, $`\beta:=F'(0)/(2F(0))`$ and $`\varepsilon^2:=\beta^2w_0\ll1`$, for grips with $`F^{(n)}(0)=O(F(0)\beta^n)`$ for all $`n`$ (e.g. $`F(0)\Phi(\beta q)`$ with $`\Phi`$ fixed). Then $`a_n=F^{(n)}(0)+O(F(0)\beta^n\varepsilon^2)`$. By $`J_n(\mathbf r)\le w_0^{n-1}J_1(\mathbf r)`$ (2.3), the terms $`n\ge2`$ of $`T(\mathbf r)`$ and $`S(\mathbf r)`$ are $`O(\varepsilon^2)`$ relative to $`J_1(\mathbf r)\,F(0)^2\beta^{3}`$ and $`J_1(\mathbf r)F(0)^2\beta^2`$, uniformly in $`\mathbf r`$. So
```math
\rho(\mathbf r)=\frac{2F(0)F''(0)}{F'(0)^2}+O(\varepsilon^2)\quad\text{uniformly in }\mathbf r .
\qquad\text{(2.17)}
```

*(d) Which grips weigh.* By (2.14) and (2.17), at order $`\mu^2`$ and leading order in $`\varepsilon`$:
```math
\rho_{\rm mark}=1\ \text{and}\ \rho_{\rm bond}=m_{\mathbf r}\ \ \text{for every level and both branches}\iff 2F(0)F''(0)=F'(0)^2\iff F(q)=F(0)(1+\beta q)^2+O(q^3).
\qquad\text{(2.18)}
```
This is the *square grip*, $`(\sqrt{\lvert F\rvert})''(0)=0`$; in (G2), $`4F_0F_2=F_1^2`$. It holds at every distance from the source and every separation, on the three graphs, for all $`L`$, $`\kappa_h`$, $`m_h>0`$ with $`\varepsilon,u\ll1`$. Otherwise $`\rho-1=(2F(0)F''(0)-F'(0)^2)/F'(0)^2+O(\varepsilon^2)`$, which does not vanish as $`\varepsilon\to0`$ and is the same at every distance. Controls: the linear grip ($`\rho=0`$), and (G2) with $`4F_0F_2\neq F_1^2`$.

*(e) First deviation for the square (G2) grip.* Insert $`a_0=F_0(1+\beta^2w_0)`$, $`a_1=2F_0\beta`$, $`a_2=2F_0\beta^2`$, $`a_{n\ge3}=0`$ into (2.14), then use (2.3):
```math
\rho(\mathbf r)=\frac{1+\beta^2w_0}{1+\beta^2J_2(\mathbf r)/G(\mathbf r)},\qquad
\rho_{\rm mark}-1=\beta^2\Bigl(w_0-\frac{J_2}{G_0}\Bigr)+O(\varepsilon^4)\in\Bigl[\frac{\beta^2w_0}2,\beta^2w_0\Bigr)+O(\varepsilon^4),\qquad
\frac{\rho_{\rm bond}}{m_{\mathbf r}}-1=\beta^2\Bigl(w_0-\frac{J_2(\mathbf r)}{G(\mathbf r)}\Bigr)+O(\varepsilon^4).
\qquad\text{(2.19)}
```
The ratio $`J_2(\mathbf r)/G(\mathbf r)`$ is $`O(e^{-\lvert\mathbf r\rvert/\ell})`$ for $`\lvert\mathbf r\rvert\gg\ell`$, and $`\simeq1/(16\pi^2\sqrt{\kappa_h}\lvert\mathbf r\rvert^2)`$ for $`D=3`$, $`1\ll\lvert\mathbf r\rvert\ll\ell`$. The latter follows from the continuum $`c_{\mathbf r}(\tau)\simeq[4\pi^2\sqrt{\kappa_h}(\lvert\mathbf r\rvert^2+\kappa_h\tau^2)]^{-1}`$. So $`\rho_{\rm bond}/m_{\mathbf r}-1\to\beta^2w_0`$ at large separation. Beyond order $`\mu^2`$, (2.15) depends on $`(k,\sigma)`$ only through $`\zeta(\sigma M_kF_2)`$, which brings a level and branch dependence of relative order $`\varepsilon^2u`$; the same holds for (2.16) with equal labels. For unequal labels, (2.16) adds the referral term of (b). At $`w_0=\zeta=0`$ (tree level), (2.15) and (2.16) with equal labels are exactly $`1`$ and $`m_{\mathbf r}`$ for the square grip, at every order in $`u`$. All deviations of the square grip at equal labels therefore come from the zero-point spread of the field. Code (i) confirms (2.19) on rings and cubic tori (Code section).

*(f) What cannot be obtained.*
```math
\begin{aligned}
&\text{(i) no (G2) grip gives }\rho_{\rm mark}=1\text{ exactly for every level and both branches;}\\
&\text{(ii) at order }\mu^2\text{ no (G2) grip gives }\rho_{\rm mark}=1\text{ and }\rho_{\rm bond}=m_{\mathbf r}\text{ at a separation with }J_2(\mathbf r)/G(\mathbf r)\ne J_2/G_0;\\
&\text{(iii) a (G) grip of fixed shape }f\text{ and }F(0)\ne0\text{ has }\rho_{\rm mark}=\frac{2F(0)\,T_f}{\theta\,\langle f'\rangle_0\,S_f}+O(1),\ \lvert\rho_{\rm mark}\rvert\to\infty\ (\theta\to0)\text{ unless }T_f=0 .
\end{aligned}
\qquad\text{(2.20)}
```
- (i): for $`F_2=0`$, $`\rho_{\rm mark}=0`$. For $`F_2\ne0`$, $`\zeta(\sigma M_kF_2)`$ is strictly monotone in $`\sigma M_k`$ (Step 3), so the $`2N`$ values (2.15) are pairwise different ($`\langle F\rangle_0\ne0`$).
- (ii): the two conditions $`F_1^2G_0+4F_2^2J_2=4F_2\langle F\rangle_0G_0`$ and $`F_1^2G(\mathbf r)+4F_2^2J_2(\mathbf r)=4F_2\langle F\rangle_0G(\mathbf r)`$ imply $`F_2^2\,(J_2/G_0-J_2(\mathbf r)/G(\mathbf r))=0`$, and $`F_2=0`$ gives $`\rho=0`$. Since $`J_2(\mathbf r)/G(\mathbf r)\to0`$ for $`\lvert\mathbf r\rvert/\ell\to\infty`$ ($`L\to\infty`$ first) while $`J_2/G_0>0`$, the mark and the bond are weighed like $`C^{(1)}`$ together only at leading order in $`\varepsilon`$.
- (iii): $`T=\theta^2T_f`$, $`S=\theta^2S_f`$ and $`a_1=\theta\langle f'\rangle_0`$ in (2.14), with $`O(\theta)`$ relative corrections to $`T/S`$. A grip of fixed shape thus weighs its mark like $`C^{(1)}`$ at small $`\theta`$ only if its curvature is tuned with $`\theta`$ as in (2.18).

*Dependence on $`m_h`$ and $`L`$.* The deviations are controlled by $`\varepsilon^2=\beta^2w_0`$ and $`u`$, with (2.5) requiring $`u<1`$.
- $`L\to\infty`$ at fixed $`m_h>0`$: $`G_0`$, $`w_0`$ and $`J_n(\mathbf r)`$ tend to finite lattice integrals in every $`D`$, and all results have limits.
- $`m_h\to0`$ at fixed $`L`$: $`G_0\ge1/(N_fm_h^2)`$ and $`w_0\ge1/(2N_fm_h)`$ diverge (the uniform mode). For $`F_2\ne0`$, (2.5) then fails in one branch once $`m_h^2\le2M_k\lvert F_2\rvert/N_f`$, and $`\varepsilon\to\infty`$; for the linear grip the cost diverges. Costs and ratios have no limit; the profiles $`\Delta\phi`$ converge.
- After $`L\to\infty`$, as $`m_h\to0`$: $`G_0`$ diverges for $`D=1`$ ($`\propto\ell`$) and $`D=2`$ ($`\propto\ln\ell`$) and tends to $`0.2527/\kappa_h`$ for $`D=3`$; $`w_0`$ diverges logarithmically for $`D=1`$ and stays finite for $`D=2,3`$.

### Step 8. Another eigenvector of the field

Take (G2) and the eigenvector $`\lvert1\rangle`$ with one quantum in the normal mode of $`K'`$ connected, as $`s\to0`$, to the uniform mode of $`K`$ (nondegenerate at fixed $`L`$). In its Fock eigenvectors the eigenvalues of the quadratic contract are $`\mu F_0-\frac12J^TK'^{-1}J+\sum_j(n_j+\frac12)\Omega_j(K')`$, with $`\Omega_j^2`$ the eigenvalues of $`K'`$. The source changes $`J`$, not $`K'`$, and the spectrum of $`K'`$ does not depend on the body's place. So the weights (2.8) and (2.13) are the same in every Fock eigenvector. In $`\lvert1\rangle`$, $`C^{(1)}=\mu(F_0+F_2\langle q_b^2\rangle_1)`$ with $`\langle q_b^2\rangle_1=w_0+1/(N_fm_h)`$ (Hellmann–Feynman). The mark gains the $`c`$-independent term $`\Omega_0(a)-m_h-a/(2N_fm_h)=O(a^2)`$, which is not weighed. Hence
```math
\rho_{\rm mark}\big|_{\lvert1\rangle}=\frac{4F_2\bigl(\langle F\rangle_0+F_2/(N_fm_h)\bigr)}{F_1^2+\zeta_1},\qquad \zeta_1-\zeta=O(F_2^2).
\qquad\text{(2.21)}
```
The answer (2.18) is unchanged. The deviation (2.19) changes, by $`\beta^2/(N_fm_h)`$ and by $`(\zeta_1-\zeta)/F_1^2`$. The first term vanishes as $`L\to\infty`$ and diverges as $`m_h\to0`$ at fixed $`L`$. Eigenvectors with $`\beta^2\langle q_b^2\rangle_n\gtrsim1`$ lose (2.18) even at leading order.

## Result

All results hold for held Model D bodies gripping a field of oscillator cells on a ring, square or cubic torus ($`m_h>0`$), in the limit $`M\to\infty`$ taken first, at first order in $`g_s`$.

- **(2.1)–(2.2), theorem.** For every grip, the source enters the eigenvalues only by shifting the argument of each grip by the made field $`\phi(x_i)=-g_sG(x_i-x_s)`$. At first order in $`g_s`$, every weight is $`\partial_cX[F_c]\,\Delta\phi`$, and $`\rho_{\rm mark}=\partial_c\ln C^{\rm mark}/\partial_c\ln C^{(1)}`$, independent of the places and of the distance. The cost, $`C^{(1)}=\mu\langle F\rangle_0`$ and $`C^{\rm mark}`$ are fixed by the total contracts with and without the body.
- **(2.3)–(2.4), formula.** These are the field constants and the made field. At $`\lvert d\rvert\gg1`$ and $`L\gg\ell`$, $`\phi\propto G`$ is linear, logarithmic or $`1/\lvert d\rvert`$ (for $`D=1,2,3`$) below $`\ell=\sqrt{\kappa_h}/m_h`$, and $`\propto e^{-\lvert d\rvert/\ell}`$ above it.
- **(2.5), criterion.** For (G2), a lowest eigenvector exists iff $`1+2\sigma M_kF_2G_0>0`$. Otherwise the lowest eigenvalue of $`C_M`$ tends to $`-\infty`$.
- **(2.6)–(2.7), formula.** For (G2), exactly: cost $`=\mu F_0-\mu^2F_1^2G_0/(2D_\mu)+Z(2\mu F_2)`$, $`C^{(1)}=\mu(F_0+F_2w_0)`$, and $`C^{\rm mark}=-\mu^2G_0(F_1^2+\zeta)/(2D_\mu)<0`$. The zero-point term $`\zeta\ge0`$ is, for $`F_2\ne0`$, strictly monotone in $`\sigma M_kF_2`$.
- **(2.8), formula.** For (G2), exactly: $`\Delta W=\mu F_1\Delta\phi/D_\mu`$, $`\Delta W^{(1)}=\mu F_1\Delta\phi`$, $`\Delta W^{\rm mark}=-2\mu^2F_1F_2G_0\Delta\phi/D_\mu`$. The zero-point part is not weighed.
- **(2.9)–(2.10), formula.** For (G) with $`\mathrm{Var}F(q_x)<\infty`$, at order $`\theta^2`$: $`C^{\rm mark}=-\mu^2\sum_{n\ge1}a_n^2J_n/n!`$ and $`\Delta W^{\rm mark}=-2\mu^2\sum_{n\ge1}a_na_{n+1}J_n/n!\;\Delta\phi`$; $`C^{(1)}=\mu a_0`$ and $`\Delta W^{(1)}=\mu a_1\Delta\phi`$ hold exactly.
- **(2.11)–(2.13), formula.** At order $`\mu_1\mu_2`$ the bond is $`U=-2\mu_1\mu_2\sum_na_n^{(1)}a_n^{(2)}J_n(\mathbf r)/n!`$, with weight $`-2\mu_1\mu_2(\Delta\phi_1+\Delta\phi_2)T(\mathbf r)`$ for a common grip. For $`d\gg\lvert\mathbf r\rvert`$ and a far reference, the midpoint factor is $`m_{\mathbf r}=1+O(\lvert\mathbf r\rvert^2/d^2)`$ for $`d\ll\ell`$ and $`1+O(\lvert\mathbf r\rvert^2/\ell^2)`$ for $`d\gg\ell`$. Reference to a body instead of the midpoint gives an error of first order in $`\lvert\mathbf r\rvert/\min(d,\ell)`$. For (G2), the weight is exactly $`-(2F_2/F_1)\sum_i\Delta\phi_iv_i(\mathbb Mv)_i`$, and the zero-point part $`Z_b`$ is not weighed.
- **(2.14), formula.** At order $`\mu^2`$, for every grip: $`\rho_{\rm mark}=\rho(0)`$ and $`\rho_{\rm bond}=m_{\mathbf r}\rho(\mathbf r)`$ with $`\rho(\mathbf r)=2a_0T(\mathbf r)/(a_1S(\mathbf r))`$. These are the same for every level and both branches and independent of the distance to the source. Excluded are $`\langle F\rangle_0=0`$, $`\langle F'\rangle_0=0`$ and $`\Delta\bar\phi=0`$, together with the pair $`C^{(1)}`$ for $`\mu_1+\mu_2=0`$.
- **(2.15)–(2.16), formula.** For (G2), exactly: $`\rho_{\rm mark}=4F_2\langle F\rangle_0/(F_1^2+\zeta)`$ and $`\rho_{\rm bond}=4F_2\langle F\rangle_0\sum_iw_i\Delta\phi_i/[(F_1^2+\zeta_b)\Delta\bar\phi]`$. The bond is weighed at the place $`\sum_iw_ix_i`$; this is the midpoint for equal labels and is shifted at relative order $`uG(\mathbf r)/G_0`$ otherwise.
- **(2.17)–(2.18), criterion.** For grips with $`F(0)\ne0`$, $`F^{(n)}(0)=O(F(0)\beta^n)`$ and $`\varepsilon^2=\beta^2w_0\ll1`$, at order $`\mu^2`$: $`\rho(\mathbf r)=2F(0)F''(0)/F'(0)^2+O(\varepsilon^2)`$ uniformly in $`\mathbf r`$. Hence, at leading order in $`\varepsilon`$, $`\rho_{\rm mark}=1`$ and $`\rho_{\rm bond}=m_{\mathbf r}`$ for every level and both branches iff $`2F(0)F''(0)=F'(0)^2`$: the square grip $`F=F(0)(1+\beta q)^2+O(q^3)`$, in (G2) $`4F_0F_2=F_1^2`$. This holds at every distance and separation, on all three graphs, and for all $`L,\kappa_h,m_h>0`$ with $`\varepsilon,u\ll1`$. Otherwise the deviation does not vanish as $`\varepsilon\to0`$.
- **(2.19), formula.** For the square (G2) grip at order $`\mu^2`$: $`\rho_{\rm mark}-1=\beta^2(w_0-J_2/G_0)+O(\varepsilon^4)`$, which lies in $`[\beta^2w_0/2,\beta^2w_0)`$ and is distance-independent. $`\rho_{\rm bond}/m_{\mathbf r}-1=\beta^2(w_0-J_2(\mathbf r)/G(\mathbf r))+O(\varepsilon^4)`$, which tends to $`\beta^2w_0`$ at separations $`\gg\ell`$. Beyond order $`\mu^2`$, level dependence enters at relative order $`\varepsilon^2u`$ for the mark and for the bond with equal labels. At tree level the square grip weighs the mark, and the bond with equal labels, exactly.
- **(2.20), negative.** (i) No (G2) grip has $`\rho_{\rm mark}=1`$ exactly for every level and both branches. (ii) At order $`\mu^2`$, no (G2) grip has $`\rho_{\rm mark}=1`$ and $`\rho_{\rm bond}=m_{\mathbf r}`$ at any separation with $`J_2(\mathbf r)/G(\mathbf r)\ne J_2/G_0`$; this includes all separations $`\lvert\mathbf r\rvert\gg\ell`$ ($`L\to\infty`$ first). (iii) A (G) grip of fixed shape with $`F(0)\ne0`$ has $`\lvert\rho_{\rm mark}\rvert\to\infty`$ as $`\theta\to0`$ unless $`T_f=0`$.
- **(2.21), formula.** In the (G2) eigenvector with one quantum in the uniform mode, the weights are unchanged, and (2.18) holds at leading order. The deviation changes by $`\beta^2/(N_fm_h)`$ and by an $`O(F_2^2)`$ zero-point term.
- **Dependence on $`m_h`$ and $`L`$ (Step 7).** All results have limits as $`L\to\infty`$ at fixed $`m_h>0`$. As $`m_h\to0`$ at fixed $`L`$, costs and ratios have no limit: for $`F_2\ne0`$ the existence condition (2.5) fails in one branch, and the linear-grip cost diverges.

## Consistency checks

1. **Dimensions.** $`[a_n]=E^{n/2}`$, $`[J_n]=E^{-n-1}`$, $`[G]=E^{-2}`$, $`[w_0]=E^{-1}`$. So $`\mu^2a_n^2J_n`$ has dimension $`E`$, $`\rho(\mathbf r)`$ is dimensionless, $`\beta^2w_0`$ and $`\beta^2J_2/G_0`$ are dimensionless, and $`u=2M_k\lvert F_2\rvert G_0`$ is dimensionless. Passed.
2. **(G) against (G2) and the linear grip.** (2.9)–(2.10) with $`a_1=F_1`$, $`a_2=2F_2`$, $`a_{n\ge3}=0`$ give $`C^{\rm mark}=-\mu^2(F_1^2G_0/2+2F_2^2J_2)`$ and $`\Delta W^{\rm mark}=-2\mu^2F_1F_2G_0\Delta\phi`$. These are the order-$`\mu^2`$ terms of (2.6)–(2.8) with $`\zeta\simeq4F_2^2J_2/G_0`$. For $`F_2=0`$ both give $`\rho=0`$. Passed.
3. **Square grip at tree level.** Without the zero-point part, (2.1) and (2.6) give for $`F=F_0(1+\beta q)^2`$ the shifted cost $`\mu F_0(1+\beta c)^2/(1+2\mu F_0\beta^2G_0)=\mu F(c)/D_\mu`$. This is proportional to $`F(c)`$ for every $`\mu`$, so mark and $`C^{(1)}`$ are weighed alike, consistent with (2.15) at $`w_0=\zeta=0`$. Passed.

## Open issues

- (G) beyond order $`\theta^2`$: the level dependence of $`\rho_{\rm mark}`$ at order $`\mu^3`$ was obtained only for (G2) (through $`\zeta`$), not for general $`F`$.
- The fields of 06-ilang-source and 07-ilang-weight (03-gas-grip), $`m_h=0`$ with an anchor, and the formation speed are outside this package.
- Whether the square grip, or the tuned grip $`4F_2\langle F\rangle_0=F_1^2+\zeta`$, is selected by anything in the language is not addressed (item 6, M10).

## Code

- `code/v1/check_g2_ratios.py` (check, item (i) of the question; cited in Step 7).
  - *Setup.* Rings $`L=40,80`$ and cubic tori $`L=8,12`$, with $`\kappa_h=1`$, $`m_h=0.3`$ ($`\ell=3.3`$). Levels $`M_0=0.5`$, $`M_1=0.75`$, both branches. Three grips $`(F_0,F_1,F_2)`$: square $`(1,0.6,0.09)`$ ($`\beta=0.3`$), generic $`(1,0.6,0.15)`$, linear $`(1,0.6,0)`$.
  - *Method.* The exact lowest eigenvalue $`\sum_is\mu_iF_0+\frac12\mathrm{Tr}\sqrt{K'}-\frac12J^TK'^{-1}J`$ of the uncompressed contract is computed by dense linear algebra. $`C^{(1)}`$ and $`W^{(1)}`$ come from 4-point differences in $`s`$, and weights from central differences in $`g_s`$, which are exact because the eigenvalue is quadratic in $`g_s`$. Marks are evaluated at three distances from the source per graph. Bonds are evaluated at separations $`2,4`$, three midpoint distances and four label pairs: $`(0,+)(0,+)`$, $`(1,-)(1,-)`$, $`(0,+)(1,+)`$, $`(0,+)(0,-)`$.
  - *Results* (`output/g2_summary.json`):
    - $`\lvert C^{(1)}-\mu\langle F\rangle_0\rvert\le3.4\cdot10^{-10}`$.
    - $`\rho_{\rm mark}`$ agrees with (2.15) to $`3.7\cdot10^{-9}`$, and its spread over distances is $`\le1.3\cdot10^{-10}`$.
    - $`U`$ agrees with $`U_{\rm cl}+Z_b`$ (2.13) to $`1.2\cdot10^{-12}`$, and $`\rho_{\rm bond}`$ with (2.16) to $`1.9\cdot10^{-9}`$.
    - Linear grip: $`\lvert\rho\rvert\le1.4\cdot10^{-10}`$.
    - Square grip: $`\rho_{\rm mark}-1\in[0.0357,0.0381]`$ on the rings against $`\beta^2(w_0-J_2/G_0)=0.0372`$, and $`\in[0.0154,0.0157]`$ on the cubic tori against $`0.0157`$ ($`L=8`$) and $`0.0155`$ ($`L=12`$). The level spread is $`\le0.0024`$.
    - Square-grip bond, equal labels: $`\rho_{\rm bond}/m_{\mathbf r}-1=0.0430,\,0.0452`$ (rings, $`\lvert\mathbf r\rvert=2,4`$) against $`0.0436,\,0.0454`$ of (2.19); $`0.02004,\,0.02014`$ ($`L=8`$) against $`0.02004,\,0.02014`$. The values are the same at all midpoint distances.
    - Generic grip: $`\rho_{\rm mark}=1.742`$–$`1.760`$ (rings) and $`1.700`$–$`1.702`$ (cubic) against $`1.750`$ and $`1.701`$ of (2.14), with leading value $`4F_0F_2/F_1^2=1.667`$.
    - The order-$`\mu^2`$ bond formula (2.14) differs from the exact ratio by up to $`0.11`$, for unequal labels on the rings ($`u\approx0.3`$, $`G(\mathbf r)/G_0\approx0.55`$, $`\lvert\mathbf r\rvert\sim\ell`$). This is the referral term of Step 7(b).
  - *Outputs:* `output/g2_mark.csv`, `output/g2_bond.csv`, `output/g2_summary.json`.
- `code/v1/check_compression.py` (check, item (ii); cited in Steps 1 and 5).
  - *Setup.* Ring of three cells, $`\kappa_h=m_h=1`$ ($`\omega_k=1,2,2`$, $`G_0=1/2`$, $`w_0=1/3`$), $`M=4,\dots,24`$; sparse matrices, lowest eigenvalue by Lanczos.
  - *(G2)*, grip $`(1,0.5,0.2)`$ with $`\mu=\pm0.75`$. The lowest eigenvalue of $`C_M`$ decreases monotonically in $`M`$ to the exact value of (2.6); the error is $`2.6\cdot10^{-2}`$ at $`M=4`$, $`1.0\cdot10^{-6}`$ at $`M=12`$ and $`2\cdot10^{-13}`$ at $`M=24`$, and the costs converge likewise.
  - *(G)*, grip $`F=1+\theta(\sin q+\frac12(1-\cos q))`$ with $`\mu=0.75`$. The Taylor coefficients of $`C_M`$, from Rayleigh–Schrödinger theory on the finite matrix, converge to $`\mu\langle f\rangle_0=0.0575694`$ and $`-\mu^2S/\theta^2=-0.1033310`$ of (2.9): errors $`4.6\cdot10^{-3}`$ and $`6\cdot10^{-4}`$ at $`M=4`$, and $`\le8\cdot10^{-13}`$ at $`M=24`$. At $`\theta=0.1`$, the lowest eigenvalue differs from the second-order expression by $`1.4\cdot10^{-5}`$, of order $`\theta^3`$.
  - *Output:* `output/compression.json`.

## Methods used

- Sector reduction, unitary shift by the made field
- Gaussian lowest eigenvector of a quadratic contract; Sherman–Morrison, matrix determinant lemma, interlacing
- Min-max for compressions
- Rayleigh–Schrödinger perturbation theory; Wick theorem, Mehler expansion; imaginary-$`\lambda`$ correlation functions
- Lattice Green functions on rings and tori, continuum asymptotics
- Numerical linear algebra (dense and sparse eigenvalues, finite differences)
