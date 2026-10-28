# Weighing of the own mark and of the bond against the grip, oscillator cells

- **Subproject:** 08-ilang-propagation
- **Package:** 02-grip-weight
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-24

## Changes from previous version

- Step 1, "Limit": for (G2) grips with (2.5) the form core now follows from the equivalence of the positive quadratic form norms. The false claim of a relative form bound below one is removed (I1).
- Step 3, after (2.5): the two-body condition is stated as the condition for the pair and both single-body references. The pair alone can have a lowest eigenvector without it (I4).
- Step 5, item (iv): replaced by a weighted Galerkin argument (Agmon bound in the number of quanta, uniform in $`M`$; strong convergence of the compressed reduced resolvents; form-norm convergence for third-order terms with a linear middle factor). Convergence is now claimed only for the coefficients through order $`\theta^2`$ (Gθ) and $`\beta^3`$ (GΦ), which are the ones the results use (I2).
- Step 5, "Where this eigenvalue is the lowest": the claim that the continued eigenvalue stops being the lowest is replaced by the absence of a neighbourhood that does not depend on $`M`$. The remainder orders are formal where $`C`$ has no lowest eigenvalue (I3).
- Step 2 and Step 6, midpoint factor for $`d\gg\ell`$: now given with the lattice decay vector $`t^*(\hat d)`$, and in the scaling regime with the lattice error $`O(\lvert\mathbf r\rvert/\ell^3)`$. The referral error is changed the same way (I6).
- Step 7(b), (2.16): the unfactored ratio, valid whenever $`U\ne0`$; the factored form only for $`U_{\rm cl}\ne0`$; "Reference and excluded members" updated (I5).
- Result: the entries (2.9)–(2.10), (2.11)–(2.13) and (2.15)–(2.16) are changed to match.
- Code (v3): `check_compression.py` adds the Taylor coefficients for an unbounded (Gθ) grip (I2). `check_g2_ratios.py` computes the exact bond ratio from the unfactored (2.16) and adds, on every graph, a pair of different grips with $`U_{\rm cl}=0`$ (I5). Both scripts were rerun.

## Response to verification

- I1: Accepted and fixed in Step 1, "Limit". For $`K'>0`$ the norms $`q\cdot K'q`$ and $`q\cdot Kq`$ are equivalent, the linear term is infinitesimally form-bounded, and the Hermite core is therefore a form core of $`C`$ for every stable (G2) grip. The relative-bound argument is kept only for bounded grips (bound 0).
- I2: Accepted and fixed in Step 5, item (iv). The missing weighted estimate is supplied: because $`\Pi`$ commutes with the number of quanta $`N`$, an Agmon estimate gives $`\langle\Omega_M,e^{2\epsilon N}\Omega_M\rangle\le C`$ uniformly in $`M`$. Together with strong convergence of the reduced resolvents and form-norm convergence of $`R_MV\Omega_M`$, the first- and second-order coefficients converge for every polynomially bounded grip, and so do third-order terms with a linear middle factor. The claim is limited to orders $`\le\theta^2`$ (Gθ) and $`\le\beta^3`$ (GΦ). Code (ii) adds an unbounded grip.
- I3: Accepted and fixed in Step 5, "Where this eigenvalue is the lowest", and in the Result entry (2.9)–(2.10).
- I4: Accepted and fixed in Step 3, after (2.5).
- I5: Accepted and fixed in Step 7(b), (2.16), and in "Reference and excluded members"; checked in Code (i) on a pair with $`U_{\rm cl}=0`$.
- I6: Accepted and fixed in Step 2 (decay vector), Step 6 (midpoint factor and referral) and the Result entry (2.11)–(2.13). The unrestricted form uses the lattice decay vector. The scaling-regime form carries the extra error $`O(\lvert\mathbf r\rvert/\ell^3)`$, which is small for $`\lvert\mathbf r\rvert\ll\ell^3`$ and so in the range $`d\ll\ell^3`$ of (2.4).

## Setup and assumptions

- **Field** (M8), as in the question: oscillator cells on $`X_f`$ (ring, square or cubic torus of side $`L\ge3`$, $`N_f=L^D`$ cells). With the graph Laplacian $`\Delta`$, $`K:=\kappa_h\Delta+m_h^2\mathbb 1`$ and $`H=\tfrac12p\cdot p+\tfrac12q\cdot Kq`$; normal modes $`\omega_k^2=m_h^2+\kappa_h\sum_{j=1}^D4\sin^2(k_j/2)`$, $`k\in(2\pi/L)\mathbb Z_L^D`$; pinning length $`\ell:=\sqrt{\kappa_h}/m_h`$. The $`M`$ places of a cell are the $`M`$ lowest number states of $`\tfrac12(p_x^2+q_x^2)`$, and at finite $`M`$ the whole total contract $`C`$ (field, bodies, source) is compressed, $`C_M:=\Pi C\Pi`$ (choice of this package).
- **Bodies** (M8, A15): held Model D bodies, $`\tau=0`$, no term of their own. The labels $`(x_b,k,\sigma)`$ are conserved ($`S`$ commutes with $`C`$), and in that sector $`S`$ acts as $`\mu:=\sigma M_k`$, $`M_k=m+2\pi k/(N\lambda_0)>0`$.
- **Grips.** (G2) as in the question. (G) as restricted by note (a) of the question:
  - (Gθ) $`F=F(0)+\theta f`$, $`f(0)=0`$, $`f'(0)=1`$, expanded in $`\theta`$ at fixed $`f`$;
  - (GΦ) $`F=F(0)\Phi(\beta q)`$, $`F(0)\ne0`$, $`\Phi(0)=1`$, $`\Phi'(0)\ne0`$, expanded in $`\beta`$ at fixed $`\Phi`$.

  Here $`f`$ and $`\Phi`$ are smooth, and each of their derivatives is bounded by a polynomial. Two bodies may carry different grips (note (b)). In (GΦ) they share $`\beta`$; this is no restriction, since $`\Phi_i(\beta_iq)=\tilde\Phi_i(\beta q)`$ with the fixed shape $`\tilde\Phi_i(x)=\Phi_i(\beta_ix/\beta)`$ at fixed ratios $`\beta_i/\beta`$.
- **Source** (M8, A15): $`g_sq_{x_s}`$, first order in $`g_s`$. **State** (M9, A11): as in the question; Steps 1 and 5 fix the sense of $`M\to\infty`$.
- **Definitions** of the question: cost, $`C^{(1)}`$, $`C^{\rm mark}`$, weight $`W`$, bond, $`\rho_{\rm mark}`$, and $`\rho_{{\rm bond},i}`$ with the reference of note (b).
- **Notation.** $`\langle\cdot\rangle_0`$ is the lowest eigenvector of $`H`$ (a Gaussian). $`a_n:=\langle F^{(n)}(q_x)\rangle_0`$ ($`n\ge0`$) is a Gaussian average of variance $`w_0`$; $`a_n^{(i)}`$ is the same for the grip of body $`i`$. $`\Delta\phi:=\phi(x)-\phi(x')`$.
- **Dimensions:** $`[C]=E`$, $`[q]=E^{-1/2}`$, $`[K]=E^2`$, $`[F]=1`$, $`[\mu]=E`$, $`[g_s]=E^{3/2}`$, $`[\beta]=E^{1/2}`$.
- **Standard mathematics** (allowed by the question): Gaussian lowest eigenvector of a positive quadratic contract; Sherman–Morrison, matrix determinant lemma; min-max; strong resolvent convergence of compressions (monotone convergence of forms); Rayleigh–Schrödinger perturbation theory for an isolated eigenvalue; Wick's theorem, the Mehler (Hermite) expansion, Gaussian integration by parts and the heat equation for Gaussian averages; lattice Fourier sums, their continuum limits and their saddle-point asymptotics.

## Derivation

### Step 1. Sector, limit $`M\to\infty`$, shift by the made field

In the sector of held bodies at $`x_i`$ with labels $`(k_i,\sigma_i)`$: $`C=H+g_sq_{x_s}+\sum_i\mu_iF_i(q_{x_i})`$.

*Limit.* $`\mathrm{ran}\Pi_M`$ grows with $`M`$. The union of these subspaces (finite sums of products of Hermite functions) is a form core of $`H`$. It is also a form core of $`C`$, with an equivalent form norm, in two cases:
- every bounded grip (relative form bound 0);
- every (G2) grip with (2.5), one body or two (Step 3). Here $`K'>0`$, so $`cK\le K'\le c'K`$ with $`c,c'>0`$ (positive matrices of finite size). The quadratic parts of $`C`$ and $`H`$ then have equivalent form norms, and the linear term $`\mu F_1q_b`$ is infinitesimally form-bounded. No relative bound below one is needed; such a bound fails for large $`\mu F_2>0`$.

In both cases min-max makes the lowest eigenvalue of $`C_M`$ nonincreasing in $`M`$, and it tends to the lowest eigenvalue of $`C`$ (Rayleigh–Ritz). For a (G2) grip that violates (2.5), the quadratic form of $`C`$ is continuous in the form norm of $`H`$ and unbounded below, and the union is dense in that norm. So the lowest eigenvalue of $`C_M`$ tends to $`-\infty`$. For (G), where $`C`$ need not be bounded below, the limit is taken coefficient by coefficient (Step 5). Statements about $`C`$ are statements about these limits (Code (ii)).

*Shift.* Let $`\phi:=-g_sK^{-1}e_{x_s}`$, $`\phi(x)=-g_sG(x-x_s)`$ (the made field), and $`U:=\exp(-i\sum_x\phi(x)p_x)`$. Then $`U^\dagger q_xU=q_x+\phi(x)`$, and with $`K\phi=-g_se_{x_s}`$:
```math
U^\dagger CU=H+\sum_i\mu_iF_i\bigl(q_{x_i}+\phi(x_i)\bigr)-\tfrac12g_s^2G(0).
\qquad\text{(2.1)}
```
So with the source, every eigenvalue is the one without the source for the shifted grips $`F_{c_i}(q):=F_i(q+c_i)`$, $`c_i=\phi(x_i)`$, minus a term that does not depend on the bodies. For one body, the eigenvalue $`E[F]`$ of $`H+\mu F(q_{x_b})`$ does not depend on $`x_b`$ (translations of the torus). The $`s`$-expansion commutes with the shift ($`(sF)_c=sF_c`$). Hence, at first order in $`g_s`$, for $`X\in\{\text{cost},C^{(1)},C^{\rm mark}\}`$:
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

*Made field at large distances* ($`L\to\infty`$ first). In the scaling regime $`\ell\gg1`$ (weak pinning), the Fourier integral tends to its continuum form, with relative errors $`O(\lvert d\rvert^{-2}+\ell^{-2})`$ for $`1\ll\lvert d\rvert\lesssim\ell`$. For $`\lvert d\rvert\gg\ell`$ the decay rate carries an error $`O(\ell^{-3})`$ (see below), so the exponential forms hold for $`\ell\ll\lvert d\rvert\ll\ell^3`$:
```math
G(d)\simeq
\begin{cases}
\dfrac{e^{-\alpha\lvert d\rvert}}{2\kappa_h\sinh\alpha}\ \ (\cosh\alpha=1+\tfrac1{2\ell^2},\text{ exact on the chain at every }\ell)\ \simeq\dfrac{\ell}{2\kappa_h}e^{-\lvert d\rvert/\ell}, & D=1,\\[2mm]
\dfrac{K_0(\lvert d\rvert/\ell)}{2\pi\kappa_h}\to\dfrac{\ln(2\ell/\lvert d\rvert)-\gamma_E}{2\pi\kappa_h}\ (\lvert d\rvert\ll\ell),\ \ \dfrac{1}{2\pi\kappa_h}\sqrt{\dfrac{\pi\ell}{2\lvert d\rvert}}e^{-\lvert d\rvert/\ell}\ (\lvert d\rvert\gg\ell), & D=2,\\[2mm]
\dfrac{e^{-\lvert d\rvert/\ell}}{4\pi\kappa_h\lvert d\rvert}\to\dfrac1{4\pi\kappa_h\lvert d\rvert}\ (1\ll\lvert d\rvert\ll\ell), & D=3.
\end{cases}
\qquad\text{(2.4)}
```
At any $`\ell`$ and $`\lvert d\rvert\gg\max(1,\ell)`$, the saddle point of the lattice Fourier integral gives $`G(d)\asymp\lvert d\rvert^{-(D-1)/2}e^{-\alpha(\hat d)\lvert d\rvert}`$. The decay rate $`\alpha(\hat n):=\max\{\hat n\cdot t:\sum_j4\sinh^2(t_j/2)\le\ell^{-2}\}`$ depends on the direction for $`D\ge2`$. It is attained at the *decay vector* $`t^*(\hat n)`$, and $`t^*(\hat d)=\nabla_d[\alpha(\hat d)\lvert d\rvert]`$; the Hessian of $`\alpha(\hat d)\lvert d\rvert`$ is $`O(\lvert t^*\rvert/\lvert d\rvert)`$ (homogeneity of degree one). Along an axis $`\cosh\alpha=1+1/(2\ell^2)`$, as on the chain. For $`\ell\gg1`$, $`\alpha(\hat n)=\ell^{-1}+O(\ell^{-3})`$ and $`t^*(\hat n)=\hat n/\ell+O(\ell^{-3})`$, since $`4\sinh^2(t/2)=t^2+O(t^4)`$. Below the pinning length ($`\ell\gg1`$) the made field is long-range for $`D=3`$ ($`1/\lvert d\rvert`$), logarithmic for $`D=2`$ and linear for $`D=1`$; above it, it decays exponentially. On a finite torus $`G`$ is the sum over images; for $`L\ll\ell`$, $`G(d)=1/(N_fm_h^2)+G_{\rm per}(d)+O(m_h^2)`$, and the uniform part cancels in $`\Delta\phi`$.

### Step 3. (G2): existence and cost

With one body (no source), $`C=H+\mu F_0+\mu F_1q_b+\mu F_2q_b^2`$ is quadratic, with matrix $`K':=K+a\,e_be_b^{T}`$, $`a:=2\mu F_2`$. By the determinant lemma $`\det K'=\det K\,(1+aG_0)`$, and by interlacing at most one eigenvalue of $`K'`$ lies below the spectrum of $`K`$. So $`K'>0`$ iff $`D_\mu:=1+aG_0>0`$. For $`D_\mu<0`$, $`C`$ has a direction of negative curvature. For $`D_\mu=0`$, $`K'`$ has the null vector $`K^{-1}e_b`$, on which the linear term is $`\mu F_1G_0\ne0`$. In both cases $`C`$ is unbounded below. With Step 1:
```math
\text{a lowest eigenvector exists }(M\to\infty)\iff 1+2\sigma M_kF_2G_0>0;\ \text{otherwise the lowest eigenvalue of }C_M\to-\infty .
\qquad\text{(2.5)}
```
For both branches this reads $`2M_k\lvert F_2\rvert G_0<1`$.

For two bodies, the pair and both single bodies (all three enter the bond, Step 6) have lowest eigenvectors iff $`D_1,D_2>0`$ and $`\Delta_2:=D_1D_2-a_1a_2G(\mathbf r)^2>0`$. Given $`D_1>0`$, adding $`a_2e_{x_2}e_{x_2}^T`$ moves at most one eigenvalue below the spectrum, and $`\det K'_{12}=\det K\,\Delta_2`$ (determinant lemma). The pair alone needs only $`K'_{12}>0`$. That can hold with $`D_1<0`$ when $`a_2>0`$, since then $`[(K+a_2e_{x_2}e_{x_2}^T)^{-1}]_{x_1x_1}<G_0`$. Such pairs have no bond in the sense of the question, because $`\text{cost}_1`$ does not exist.

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

### Step 5. (G): lowest orders

*Consequences of the class* (note (a)). For (Gθ) and (GΦ):
- (i) every $`a_n`$ is finite, and $`\langle F^{(n)}(q_x+c)\rangle_0`$ is smooth in $`c`$ with $`\partial_ca_n=a_{n+1}`$: the integrand is dominated by a polynomial times the Gaussian, so one may differentiate under the integral.
- (ii) Let $`(q',q)`$ be a Gaussian pair with variances $`w_0`$ and covariance $`c`$, $`\lvert c\rvert\le w_0`$, and let $`g,h`$ have polynomially bounded derivatives. Then $`\mathrm{Cov}(g(q'),h(q))=\sum_{n\ge1}\langle g^{(n)}\rangle_0\langle h^{(n)}\rangle_0\,c^n/n!`$, absolutely convergent. This is Mehler's formula; convergence follows from Parseval for the Hermite coefficients $`\langle g^{(n)}\rangle_0w_0^{n/2}/\sqrt{n!}`$ and Cauchy–Schwarz. Moreover $`\partial_c\langle g(q')h(q)\rangle=\langle g'(q')h'(q)\rangle`$ (Gaussian integration by parts).
- (iii) The matrix elements of $`\Pi F(q_x)\Pi`$ are finite.
- (iv) *Compressed coefficients.* Fix $`g_s`$. Let $`H_g:=H+g_sq_{x_s}+\mu F(0)`$, with lowest eigenvalue $`E_g`$ and eigenvector $`\Omega`$, and let $`E_M`$, $`\Omega_M`$ be those of $`\Pi H_g\Pi`$. Let $`N:=\sum_xn_x`$ be the total number of quanta of the cell oscillators $`\frac12(p_x^2+q_x^2)`$. $`\Pi`$ commutes with $`N`$.
  - *Ritz limits.* $`E_M\downarrow E_g`$ and $`\Omega_M\to\Omega`$ in $`L^2`$ (phase fixed), because the ranges exhaust a form core and $`E_g`$ is simple and isolated. By min-max the second eigenvalue of $`\Pi H_g\Pi`$ is $`\ge E_g+m_h`$, so its gap is $`\ge m_h/2`$ for large $`M`$.
  - *Weighted bound* (Agmon estimate in $`N`$). Write $`H_g=\sum_{j=-2}^2H_j`$, where $`H_j`$ raises $`N`$ by $`j`$. $`H_{\pm2}`$ are the terms $`a_xa_y`$, $`a_x^\dagger a_y^\dagger`$ with coefficient $`\frac14(K-\mathbb 1)_{xy}`$, and $`H_{\pm1}`$ is the source term. Then $`e^{\epsilon N}H_ge^{-\epsilon N}=\sum_je^{j\epsilon}H_j`$. Put $`\varphi:=e^{\epsilon N}\Omega_M\in\mathrm{ran}\Pi`$; it satisfies $`e^{\epsilon N}\Pi H_g\Pi e^{-\epsilon N}\varphi=E_M\varphi`$. The real part of the corresponding expectation value is
  $`E_M\lVert\varphi\rVert^2=\langle\varphi,H_g\varphi\rangle+\sum_{j=1,2}(\cosh j\epsilon-1)\langle\varphi,(H_j+H_{-j})\varphi\rangle\ge(c_1-C\epsilon^2)\langle\varphi,N\varphi\rangle-C'\lVert\varphi\rVert^2`$.
  Here $`c_1>0`$ comes from $`H_g\ge c_1N-{\rm const}`$ (since $`H\ge\min(1,m_h^2)(N+N_f/2)`$), $`\lvert\langle\varphi,(H_j+H_{-j})\varphi\rangle\rvert\le C''\langle\varphi,(N+1)\varphi\rangle`$, and $`C'`$ is uniform because $`E_M`$ is nonincreasing. For $`C\epsilon^2\le c_1/2`$, the sum of $`e^{2\epsilon n}\lVert P_n\Omega_M\rVert^2`$ over the levels $`n\ge4C'/c_1`$ of $`N`$ is bounded by its sum over the finitely many levels below. So $`\langle\Omega_M,e^{2\epsilon N}\Omega_M\rangle\le C_\epsilon`$ uniformly in $`M`$. Since $`\langle q_b^{2j}\rangle\le C_j\langle(N+1)^j\rangle`$, every polynomial moment of $`q_b`$ in $`\Omega_M`$ is bounded uniformly in $`M`$. With $`\Omega_M\to\Omega`$ and Cauchy–Schwarz, $`P(q_b)\Omega_M\to P(q_b)\Omega`$ in $`L^2`$ for every polynomially bounded $`P`$.
  - *Resolvents.* $`e^{-(\Pi H_g\Pi-E_M)\tau}\Pi\to e^{-(H_g-E_g)\tau}`$ strongly (monotone convergence of forms). The reduced resolvents $`R_M=\int_0^\infty e^{-(\Pi H_g\Pi-E_M)\tau}Q_M\,d\tau`$, where $`Q_M`$ projects onto $`\mathrm{ran}\Pi\ominus\Omega_M`$, are bounded by $`2/m_h`$. So they converge strongly (dominated convergence).
  - *Coefficients.* For polynomially bounded $`V`$, the first two Rayleigh–Schrödinger coefficients $`\langle\Omega_M,V\Omega_M\rangle`$ and $`-\langle V\Omega_M,R_MV\Omega_M\rangle`$ converge to those of $`H_g+V`$. Consider a third-order term $`\langle\psi_M,V'\psi_M\rangle-E_{1,M}\lVert\psi_M\rVert^2`$ with $`\psi_M:=R_MV\Omega_M`$ and a middle factor $`V'`$ linear in $`q`$. It converges too. Indeed $`\psi_M\to\psi`$ in $`L^2`$, and $`\langle\psi_M,(H_g-E_M)\psi_M\rangle=\langle\psi_M,V\Omega_M\rangle\to\langle\psi,(H_g-E_g)\psi\rangle`$. So $`\psi_M\to\psi`$ in the form norm, which bounds $`q_b`$.

  The coefficient of $`\theta^n`$ (Gθ) is the $`n`$-th order coefficient for $`V=\mu f(q_b)`$. At fixed $`M`$, $`\Pi\Phi(\beta q_b)\Pi`$ is smooth in $`\beta`$, with derivatives $`\Pi\Phi^{(m)}(\beta q_b)q_b^m\Pi`$. So the coefficient of $`\beta^n`$ (GΦ) is a sum of $`k`$-th order terms ($`k\le n`$) in the polynomials $`P_m=\mu F(0)\Phi^{(m)}(0)q_b^m/m!`$ with $`\sum m=n`$. For $`n\le3`$ the only third-order term has $`m=(1,1,1)`$. Hence, at fixed $`g_s`$, the Taylor coefficients of the eigenvalue of $`C_M`$ connected to the lowest one converge as $`M\to\infty`$ to the coefficients for $`C`$ through order $`\theta^2`$ (Gθ) and $`\beta^3`$ (GΦ). The same holds for two bodies, with $`V=V_1+V_2`$. These are all the orders that (2.9)–(2.14) and (2.17) use. Higher coefficients are not claimed to converge. The first order in $`g_s`$ is taken after this limit (Code (ii) checks a bounded and an unbounded grip).

*Second order.* At zero coupling the lowest eigenvalue of $`H+\mu F(0)`$ is nondegenerate, with gap $`m_h`$. Take $`V=\mu(F-F(0))`$ and $`\delta F=F-\langle F\rangle_0`$, and let $`q(\tau)=e^{(H-E_f)\tau}qe^{-(H-E_f)\tau}`$. Rayleigh–Schrödinger theory gives $`E=E_f+\mu a_0-\mu^2\int_0^\infty\langle\delta F(q_b(\tau))\,\delta F(q_b(0))\rangle_0d\tau+\dots`$, by $`\sum_{n\ne0}\lvert V_{n0}\rvert^2/(E_n-E_0)=\int_0^\infty\langle\delta V e^{-(H-E_0)\tau}\delta V\rangle d\tau`$. By Wick's theorem, $`(q_{x+r}(\tau),q_x(0))`$ is a Gaussian pair with covariance $`c_r(\tau)`$. So (ii) gives, with $`S(\mathbf r):=\sum_{n\ge1}a_n^2J_n(\mathbf r)/n!`$, $`T(\mathbf r):=\sum_{n\ge1}a_na_{n+1}J_n(\mathbf r)/n!`$, $`S:=S(0)`$, $`T:=T(0)`$:
```math
\text{cost}=\mu a_0-\mu^2S+R_3,\quad C^{(1)}=\mu a_0,\quad C^{\rm mark}=-\mu^2S+R_3,\quad S>0,\qquad R_3=O(\theta^3)\ \text{(Gθ)},\ O(\beta^4)\ \text{(GΦ)} .
\qquad\text{(2.9)}
```
$`S>0`$ because $`J_n>0`$ and $`\delta F\ne0`$ has a nonzero Hermite coefficient. Under the shift, $`\partial_ca_n=a_{n+1}`$ (i); by (2.2):
```math
\Delta W^{(1)}=\mu a_1\Delta\phi,\qquad \Delta W^{\rm mark}=-2\mu^2T\,\Delta\phi+R_3',\qquad R_3'=O(\theta^3)\ \text{(Gθ)},\ O(\beta^5)\ \text{(GΦ)}.
\qquad\text{(2.10)}
```

*Order counting for (GΦ).* Expand $`V=\mu F(0)\sum_{m\ge1}\beta^m\Phi^{(m)}(0)q_b^m/m!`$ inside each Rayleigh–Schrödinger term; every term is a finite Gaussian expectation by (i). The $`k`$-th order term has $`k`$ factors $`V`$, each at least of order $`\beta`$. Its part in which every factor is linear in $`q_b`$ vanishes for $`k\ge3`$, because for a linear grip the eigenvalue is exactly quadratic in the grip (Step 3 with $`F_2=0`$). So the $`k`$-th order term is $`O(\beta^{k+1})`$ for $`k\ge3`$. In its weight, $`\partial_c`$ replaces one factor $`F`$ by $`F'=F(0)\beta\Phi'(\beta(q+c))`$, whose constant part drops out for $`k\ge2`$. So the weight of the $`k`$-th order term is $`O(\beta^{k+2})`$ for $`k\ge3`$. This gives $`R_3`$ and $`R_3'`$ in (2.9)–(2.10): corrections of relative order $`\beta^2`$ to the second-order terms, which carry the sign of $`\mu`$ and so depend on the level and the branch. In (G2) they are the expansion of $`1/D_\mu`$ in $`u:=2M_k\lvert F_2\rvert G_0`$.

*Orders of the second-order terms in (GΦ).* Let $`\varepsilon^2:=\beta^2w_0`$. The heat equation $`\partial_s\langle g\rangle_s=\frac12\langle g''\rangle_s`$ for a centred Gaussian of variance $`s`$ gives $`\langle\Phi^{(n)}(\beta q_x)\rangle_0=\Phi^{(n)}(0)+O(\varepsilon^2)`$. By (ii), $`T(\mathbf r)=\int_0^\infty h(c_{\mathbf r}(\tau))d\tau`$ with $`h(c):=\mathrm{Cov}(F'(q'),F(q))`$. Here $`h(0)=0`$, $`h'(0)=a_1a_2`$, and $`\lvert h''(c)\rvert=\lvert\langle F'''(q')F''(q)\rangle\rvert\le(\langle F'''^2\rangle_0\langle F''^2\rangle_0)^{1/2}`$ by Cauchy–Schwarz. Hence $`\lvert T(\mathbf r)-a_1a_2J_1(\mathbf r)\rvert\le\frac12(\langle F'''^2\rangle_0\langle F''^2\rangle_0)^{1/2}J_2(\mathbf r)`$, and likewise $`\lvert S(\mathbf r)-a_1^2J_1(\mathbf r)\rvert\le\frac12\langle F''^2\rangle_0J_2(\mathbf r)`$. With $`J_2(\mathbf r)\le w_0J_1(\mathbf r)`$ (2.3) and $`\langle F^{(n)}(q)^2\rangle_0=F(0)^2\beta^{2n}[\Phi^{(n)}(0)^2+O(\varepsilon^2)]`$:
```math
a_0=F(0)[1+O(\varepsilon^2)],\quad a_n=F(0)\beta^n[\Phi^{(n)}(0)+O(\varepsilon^2)],\quad
S(\mathbf r)=F(0)^2\beta^2J_1(\mathbf r)[\Phi'(0)^2+O(\varepsilon^2)],\quad
T(\mathbf r)=F(0)^2\beta^3J_1(\mathbf r)[\Phi'(0)\Phi''(0)+O(\varepsilon^2)],
\qquad\text{(2.22)}
```
uniformly in $`\mathbf r`$. The same bounds hold for the two-grip sums $`S_{12},T_{12},T_{21}`$ of Step 6, with $`\Phi_1,\Phi_2`$. So in (GΦ) the mark first appears at order $`\beta^2`$ and, if $`\Phi''(0)\ne0`$, its weight at order $`\beta^3`$. In (Gθ), $`a_n=\theta\langle f^{(n)}\rangle_0`$ ($`n\ge1`$) gives $`S=\theta^2S_f`$ and $`T=\theta^2T_f`$, with $`S_f:=\sum_n\langle f^{(n)}\rangle_0^2J_n/n!`$ and $`T_f:=\sum_n\langle f^{(n)}\rangle_0\langle f^{(n+1)}\rangle_0J_n/n!`$. So the mark first appears at order $`\theta^2`$, and so does its weight if $`T_f\ne0`$.

*Mark weight vanishing at the lowest order* (note (c)):
```math
\text{(Gθ) with }T_f=0:\ \Delta W^{\rm mark}=O(\theta^3);\qquad \text{(GΦ) with }\Phi''(0)=0:\ \Delta W^{\rm mark}=O(\beta^5).
\qquad\text{(2.23)}
```
So $`\theta^3`$, resp. $`\beta^5`$, is the lowest order at which a nonzero mark weight can appear; its value is not computed. Examples: an odd $`f`$ (each product in $`T_f`$ contains an even derivative of $`f`$, which is odd and averages to zero), and $`\Phi-1`$ odd. For $`\Phi''(0)=0`$: $`a_2=O(\beta^4)`$ by the heat equation, so $`a_1a_2J_1=O(\beta^5)`$; the bound above is $`O(\beta^5)`$; and $`R_3'=O(\beta^5)`$. The mark itself stays at $`\theta^2`$, resp. $`\beta^2`$. Hence $`\rho_{\rm mark}=O(1)`$ for (Gθ) with $`F(0)\ne0`$, and $`\rho_{\rm mark}=O(\beta^2)`$ for (GΦ). For the linear grip the mark weight vanishes at every order (Step 4).

*Where this eigenvalue is the lowest.* Suppose $`\mu F(0)(\Phi(x)-1)\ge-A-Bx^2`$ for all $`x`$ (resp. $`\mu\theta f(q)\ge-\lvert\theta\rvert(A+Bq^2)`$), with constants $`A,B\ge0`$. Take (GΦ) and $`\eta>0`$. Splitting at $`\lvert\beta q_b\rvert=\eta`$ gives $`V\ge-\lvert\mu F(0)\rvert c_\eta-\gamma q_b^2`$, with $`c_\eta:=\sup_{\lvert x\rvert\le\eta}\lvert\Phi(x)-1\rvert`$ and $`\gamma:=(A/\eta^2+B)\beta^2`$. The quadratic contract $`H-\gamma q_b^2`$ has its two lowest eigenvalues at $`E_f+O(\gamma)`$ and $`E_f+m_h+O(\gamma)`$. By min-max, the second eigenvalue of $`C-\mu F(0)`$ is $`\ge E_f+m_h-O(\gamma)-\lvert\mu F(0)\rvert c_\eta`$, while the connected eigenvalue is $`E_f+O(\beta^2)`$. Choosing first $`\eta`$, then $`\beta`$ small makes the connected eigenvalue the only one below $`E_f+\mu F(0)+m_h/2`$, hence the lowest. For (Gθ) the same holds with $`\gamma=\lvert\theta\rvert B`$ and $`\lvert\theta\rvert A`$ in place of $`\lvert\mu F(0)\rvert c_\eta`$. If instead $`\mu F(0)\Phi(x)`$ (resp. $`\mu\theta f(q)`$) tends to $`-\infty`$ faster than $`x^2`$ (resp. $`q^2`$) along some direction, $`C`$ has no lowest eigenvalue, for every $`\beta\ne0`$ (resp. for that $`\theta`$). Hermite expansions converge in the Schwartz topology, and $`\langle C\rangle`$ is continuous in it. So the lowest eigenvalue of $`C_M`$ tends to $`-\infty`$ as $`M\to\infty`$ at every such fixed $`\beta`$ (resp. $`\theta`$). Hence no neighbourhood of $`\beta=0`$ (resp. $`\theta=0`$) that does not depend on $`M`$ keeps the lowest eigenvalue of $`C_M`$ near $`E_f+\mu F(0)`$. At each $`M`$, the eigenvalue of $`C_M`$ connected to the lowest one at $`\beta=0`$ is smooth in $`\beta`$. It may stay the lowest through avoided crossings; this is not determined here. (2.9)–(2.10) then state the limits of its Taylor coefficients ((iv)). Their remainders $`O(\theta^3)`$, $`O(\beta^4)`$, $`O(\beta^5)`$ are formal orders of the coefficient series: the remainder has no Taylor coefficient below that order. They are not remainder bounds for an eigenvalue of $`C`$, since $`C`$ has no lowest eigenvalue.

### Step 6. Bond

Two held bodies sit at $`x_1`$ and $`x_2=x_1+\mathbf r`$, with labels $`\mu_i`$, grips $`F^{(i)}`$ of the class (they may differ, note (b)) and no pair term between them. Define $`U(\mathbf r):=\text{cost}_{12}-\text{cost}_1-\text{cost}_2`$, fixed by four lowest eigenvalues; its $`\mathbf r`$-dependence is the bond. The cross term of second-order perturbation theory in $`V_1+V_2`$, with (ii) for the Gaussian pair $`(q_{x_2}(\tau),q_{x_1}(0))`$ of covariance $`c_{\mathbf r}(\tau)`$, gives
```math
U(\mathbf r)=-2\mu_1\mu_2S_{12}(\mathbf r)+O(\mu^3),\quad S_{12}(\mathbf r):=\sum_{n\ge1}\frac{a_n^{(1)}a_n^{(2)}J_n(\mathbf r)}{n!};\qquad \text{(G2): }U=-\mu_1\mu_2\bigl[F_1^{(1)}F_1^{(2)}G(\mathbf r)+4F_2^{(1)}F_2^{(2)}J_2(\mathbf r)\bigr]+O(\mu^3).
\qquad\text{(2.11)}
```
$`O(\mu^3)`$ is third order in the body–field coupling: $`O(\theta^3)`$ for (Gθ), relative $`O(\beta^2)`$ for (GΦ) (Step 5). For a common grip, $`S_{12}=S(\mathbf r)>0`$, so at this order $`U<0`$ for $`\sigma_1=\sigma_2`$ and $`U>0`$ for $`\sigma_1=-\sigma_2`$. For different grips $`S_{12}(\mathbf r)`$ can vanish. An example is (G2) with $`F_1^{(1)}=F_1^{(2)}=b`$, $`F_2^{(1)}=-F_2^{(2)}=c`$ and $`c^2=b^2G(\mathbf r)/(4J_2(\mathbf r))`$; it is stable once both grips are scaled down. The shift acts on each grip separately, $`\partial_{c_i}a_n^{(i)}=a_{n+1}^{(i)}`$. So
```math
\Delta W_{\rm bond}=-2\mu_1\mu_2\bigl[T_{12}(\mathbf r)\Delta\phi_1+T_{21}(\mathbf r)\Delta\phi_2\bigr]+O(\mu^3),\quad T_{12}:=\sum_{n\ge1}\frac{a_{n+1}^{(1)}a_n^{(2)}J_n(\mathbf r)}{n!},\ T_{21}:=\sum_{n\ge1}\frac{a_n^{(1)}a_{n+1}^{(2)}J_n(\mathbf r)}{n!},\qquad \Delta\phi_1+\Delta\phi_2=2m_{\mathbf r}\,\Delta\bar\phi,
\qquad\text{(2.12)}
```
where $`\Delta\bar\phi:=\phi(\bar x)-\phi(\bar x')`$ at the midpoints ($`\bar x=x_1+\mathbf r/2`$, $`\mathbf r`$ with even components) and $`m_{\mathbf r}`$ is the *midpoint factor*. For a common grip $`T_{12}=T_{21}=T(\mathbf r)`$ and $`\Delta W_{\rm bond}=-4\mu_1\mu_2m_{\mathbf r}T(\mathbf r)\Delta\bar\phi`$. Take a far reference ($`\phi(\bar x')\to0`$), $`d:=\lvert\bar x-x_s\rvert\gg\lvert\mathbf r\rvert`$ and $`L\to\infty`$ first. Then (2.4) and the expansion of $`\phi(\bar x\pm\mathbf r/2)`$ give:
- $`D=3`$, $`1\ll d\ll\ell`$: $`m_{\mathbf r}-1=(3(\mathbf r\cdot\hat d)^2-\lvert\mathbf r\rvert^2)/(8d^2)+O(\lvert\mathbf r\rvert^2/(d\ell)+\lvert\mathbf r\rvert^4/d^4)`$;
- $`D=2`$, $`1\ll d\ll\ell`$: $`m_{\mathbf r}-1=(2(\mathbf r\cdot\hat d)^2-\lvert\mathbf r\rvert^2)/(8d^2[\ln(2\ell/d)-\gamma_E])+O(\lvert\mathbf r\rvert^2/\ell^2+\lvert\mathbf r\rvert^4/d^4)`$;
- $`D=1`$, both bodies on one side of the source, any reference on that side: $`m_r=\cosh(\alpha r/2)`$ exactly;
- every $`D`$, any $`\ell`$, $`d\gg\max(1,\ell)`$: the lattice form of Step 2, with the decay vector $`t^*=t^*(\hat d)`$, gives $`m_{\mathbf r}=\cosh(t^*\cdot\mathbf r/2)\bigl[1+O\bigl(\lvert\mathbf r\rvert/d+\lvert t^*\rvert\lvert\mathbf r\rvert^2/d\bigr)\bigr]`$. Here the first-order terms of the prefactor $`\lvert d\rvert^{-(D-1)/2}`$ enter only with $`\tanh(t^*\cdot\mathbf r/2)`$, and the second-order term of the exponent is bounded by the Hessian of Step 2. For $`D=1`$, $`t^*=\alpha`$, and the form is exact (above).
- scaling regime $`\ell\gg1`$, $`d\gg\ell`$: with $`t^*=\hat d/\ell+O(\ell^{-3})`$, $`m_{\mathbf r}=\cosh\bigl((\mathbf r\cdot\hat d)/(2\ell)\bigr)\bigl[1+O(\lvert\mathbf r\rvert/d+\lvert\mathbf r\rvert^2/(d\ell)+\lvert\mathbf r\rvert/\ell^3)\bigr]`$. The last term is the lattice correction; it is small for $`\lvert\mathbf r\rvert\ll\ell^3`$, and so in the range $`d\ll\ell^3`$ of (2.4). For $`\lvert\mathbf r\rvert\ll\ell`$ this is $`m_{\mathbf r}-1=(\mathbf r\cdot\hat d)^2/(8\ell^2)+O(\lvert\mathbf r\rvert^4/\ell^4+\lvert\mathbf r\rvert^2/(d\ell)+\lvert\mathbf r\rvert^2/\ell^4)`$. For $`\lvert\mathbf r\rvert\gtrsim\ell`$, $`m_{\mathbf r}`$ grows exponentially in $`\lvert t^*\cdot\mathbf r\rvert`$.

If the pair is referred to $`x_1`$ instead of $`\bar x`$, the factor becomes $`(\Delta\phi_1+\Delta\phi_2)/(2\Delta\phi_1)=1+(\mathbf r\cdot\nabla\phi)/(2\phi)+O(\lvert\mathbf r\rvert^2/\min(d,\ell)^2)`$ for $`\lvert\mathbf r\rvert\ll\min(d,\ell)`$. That is a first-order error: $`-(\mathbf r\cdot\hat d)/(2d)`$ for $`D=3`$, $`d\ll\ell`$, and $`-t^*(\hat d)\cdot\mathbf r/2`$ for $`d\gg\max(1,\ell)`$ ($`\simeq-(\mathbf r\cdot\hat d)/(2\ell)`$ in the scaling regime).

*(G2) exactly.* The exact pair cost is the two-body form of Step 3, $`U=U_{\rm cl}+Z_b`$. Let $`v_i:=\mu_iF_1^{(i)}`$, $`a_i:=2\mu_iF_2^{(i)}`$, $`D_i:=1+a_iG_0`$ and $`\eta_i:=F_2^{(i)}/F_1^{(i)}`$. The shift changes only $`v_i`$, with $`\partial_{c_i}v_i=2\eta_iv_i`$, and leaves $`K'`$ unchanged. So
```math
U_{\rm cl}=-\tfrac12v^{T}\mathbb M v,\quad \mathbb M_{ij}:=(K'^{-1})_{x_ix_j}-\delta_{ij}\frac{G_0}{D_i},\quad
Z_b=\frac1{2\pi}\int_0^\infty\ln\Bigl[1-\frac{a_1a_2\,g_{\mathbf r}^2}{(1+a_1g)(1+a_2g)}\Bigr]d\nu,\quad
\Delta W_{\rm bond}=-2\sum_i\eta_i\,\Delta\phi_i\,v_i(\mathbb Mv)_i .
\qquad\text{(2.13)}
```
The zero-point part $`Z_b`$ of the bond is not weighed. With $`\Delta_2>0`$ (Step 3), $`\mathbb M_{12}=G(\mathbf r)/\Delta_2`$ and $`\mathbb M_{ii}=-a_jG(\mathbf r)^2/(D_i\Delta_2)`$ ($`j\ne i`$). For a common grip this gives $`v^T\mathbb Mv=2\mu_1\mu_2F_1^2G(\mathbf r)[1-G(\mathbf r)F_2(\mu_1/D_1+\mu_2/D_2)]/\Delta_2`$. The bracket is positive, because $`\mu_iF_2/D_i<1/(2G_0)`$ and $`0<G(\mathbf r)\le G_0`$. The integrand of $`Z_b`$ is $`\ln(1-x)`$ with $`x`$ of the sign of $`a_1a_2=4\mu_1\mu_2F_2^2`$. So for a common grip $`U_{\rm cl}`$ and $`Z_b`$ both have the sign of $`-\mu_1\mu_2`$, and $`U\ne0`$. For different grips $`U`$ can vanish (example above).

### Step 7. Weighing ratios and which grips weigh

*Reference and excluded members.* By note (b), $`\rho_{{\rm bond},i}`$ refers the bond weight per unit of bond, $`\Delta W_{\rm bond}/U`$, to $`\Delta W^{(1)}/C^{(1)}=\Delta\bar\phi\,a_1^{(i)}/a_0^{(i)}`$. This is the value for a single body with the grip of body $`i`$ at the midpoint (Step 1), the same for every level and branch. It differs from the pair's own first-order quantity $`\sum_i\mu_ia_1^{(i)}\Delta\phi_i/\sum_i\mu_ia_0^{(i)}`$, which is not used. Pairs with $`\mu_1a_0^{(1)}+\mu_2a_0^{(2)}=0`$ are therefore admitted. Excluded members (vanishing denominators):
- $`a_0^{(i)}=\langle F^{(i)}\rangle_0=0`$: $`C^{(1)}=0`$ for every level; in (G2), $`F_0=-F_2w_0`$;
- $`a_1^{(i)}=\langle F^{(i)\prime}\rangle_0=0`$: $`C^{(1)}`$ is not weighed; in (G2) this is excluded by $`F_1\ne0`$;
- $`\Delta\bar\phi=0`$;
- $`U(\mathbf r)=0`$: never for a common grip (Step 6; exactly in (G2), at order $`\mu^2`$ otherwise), but possible for different grips at some separations (at order $`\mu^2`$, where $`S_{12}(\mathbf r)=0`$).

$`U_{\rm cl}=0`$ with $`U=Z_b\ne0`$ is not excluded. It occurs for different (G2) grips with $`a_1,a_2>0`$: $`\mathbb M`$ is then indefinite, so $`v^T\mathbb Mv=0`$ for some $`v\ne0`$. There the unfactored form of (2.16) applies.

$`C^{\rm mark}`$ does not vanish: in (G2) $`C^{\rm mark}<0`$, and at order $`\mu^2`$, $`C^{\rm mark}=-\mu^2S`$ with $`S>0`$.

*(a) Order $`\mu^2`$, every pair of grips of the class.* From (2.2), (2.9)–(2.12):
```math
\rho_{{\rm mark},i}=\frac{2a_0^{(i)}T_i}{a_1^{(i)}S_i},\qquad
\rho_{{\rm bond},i}=\frac{a_0^{(i)}}{a_1^{(i)}}\,\frac{T_{12}(\mathbf r)\Delta\phi_1+T_{21}(\mathbf r)\Delta\phi_2}{S_{12}(\mathbf r)\,\Delta\bar\phi};\qquad
\text{common grip: }\rho_{\rm bond}=m_{\mathbf r}\,\rho(\mathbf r),\quad \rho(\mathbf r):=\frac{2a_0\,T(\mathbf r)}{a_1\,S(\mathbf r)} .
\qquad\text{(2.14)}
```
Here $`T_i,S_i`$ are $`T,S`$ for the grip of body $`i`$, and $`\rho_{\rm mark}=\rho(0)`$. $`\mu`$ cancels, so at this order both ratios are the same for every level and both branches (for the bond, for every pair of labels). $`\rho_{\rm mark}`$ does not depend on the distance to the source. $`\rho_{{\rm bond},i}`$ depends on it through $`\Delta\phi_1/\Delta\bar\phi`$ and $`\Delta\phi_2/\Delta\bar\phi`$; for a common grip only through $`m_{\mathbf r}`$ (Step 6), so that $`\rho_{\rm bond}/m_{\mathbf r}=\rho(\mathbf r)`$ does not.

*(b) (G2), exact in the grip.* (2.6)–(2.8) and (2.13) give
```math
\rho_{\rm mark}=\frac{4F_2\langle F\rangle_0}{F_1^2+\zeta(\sigma M_kF_2)},
\qquad\text{(2.15)}
```
```math
\begin{aligned}
&\rho_{{\rm bond},i}=\frac{\langle F^{(i)}\rangle_0}{F_1^{(i)}}\,\frac{\Delta W_{\rm bond}}{U\,\Delta\bar\phi}=-\frac{2\langle F^{(i)}\rangle_0}{F_1^{(i)}\,(U_{\rm cl}+Z_b)}\sum_j\eta_jv_j(\mathbb Mv)_j\frac{\Delta\phi_j}{\Delta\bar\phi}\quad(U\ne0);\\
&U_{\rm cl}\ne0:\ \rho_{{\rm bond},i}=\frac{4\langle F^{(i)}\rangle_0}{F_1^{(i)}\,(1+Z_b/U_{\rm cl})}\sum_j\eta_jw_j\frac{\Delta\phi_j}{\Delta\bar\phi},\quad w_j:=\frac{v_j(\mathbb Mv)_j}{v^T\mathbb Mv};\qquad
\text{common grip: }\rho_{\rm bond}=\frac{4F_2\langle F\rangle_0}{F_1^2+\zeta_b}\sum_jw_j\frac{\Delta\phi_j}{\Delta\bar\phi},\quad \zeta_b:=\frac{F_1^2Z_b}{U_{\rm cl}}=\frac{4F_2^2J_2(\mathbf r)}{G(\mathbf r)}\bigl[1+O(u)\bigr],
\end{aligned}
\qquad\text{(2.16)}
```
with $`u:=2\max_iM_{k_i}\lvert F_2^{(i)}\rvert G_0`$. The first line is (2.13) inserted into the reference of note (b), with $`a_0^{(i)}/a_1^{(i)}=\langle F^{(i)}\rangle_0/F_1^{(i)}`$. For $`U_{\rm cl}\ne0`$, $`\Delta W_{\rm bond}=4U_{\rm cl}\sum_j\eta_jw_j\Delta\phi_j`$ and $`U=U_{\rm cl}(1+Z_b/U_{\rm cl})`$ give the second line. For a common grip $`U_{\rm cl}\ne0`$ always (Step 6). Here $`\sum_jw_j=1`$. For a common grip and equal labels $`w_j=\frac12`$, and the sum is $`m_{\mathbf r}`$. In general $`w_j=\frac12+O(uG(\mathbf r)/G_0)`$ at fixed ratios of the grip coefficients. For a common grip and unequal labels the bond is therefore weighed at the place $`\sum_jw_jx_j`$, not at the midpoint. Referred to the midpoint, this adds $`(w_1-\frac12)(\Delta\phi_1-\Delta\phi_2)/\Delta\bar\phi=O\bigl(u\,\tfrac{G(\mathbf r)}{G_0}\,\tfrac{\lvert\mathbf r\rvert}{\min(d,\ell)}\bigr)`$ to the sum ($`\lvert\mathbf r\rvert\ll\min(d,\ell)`$), a label dependence beyond order $`\mu^2`$. Code (i) reproduces (2.15) and (2.16) from exact lowest eigenvalues, for common and for different grips, including a pair with $`U_{\rm cl}=0`$ (Code section).

*(c) Fixed shape (GΦ).* By (2.22), $`a_0^{(i)}/a_1^{(i)}=[1+O(\varepsilon^2)]/(\beta\Phi_i'(0))`$, and (2.14) gives, uniformly in $`\mathbf r`$ at order $`\mu^2`$,
```math
\rho_{{\rm mark},i}=\frac{2\Phi_i''(0)}{\Phi_i'(0)^2}+O(\varepsilon^2),\qquad
\rho_{{\rm bond},i}=\frac{\kappa_1\Delta\phi_1+\kappa_2\Delta\phi_2}{\Phi_i'(0)\,\Delta\bar\phi}+O(\varepsilon^2)\,\frac{\lvert\Delta\phi_1\rvert+\lvert\Delta\phi_2\rvert}{\lvert\Delta\bar\phi\rvert},\qquad \kappa_j:=\frac{\Phi_j''(0)}{\Phi_j'(0)} .
\qquad\text{(2.17)}
```
For a common grip, $`\rho(\mathbf r)=2\Phi''(0)/\Phi'(0)^2+O(\varepsilon^2)=2F(0)F''(0)/F'(0)^2+O(\varepsilon^2)`$ uniformly in $`\mathbf r`$. The higher orders of perturbation theory add relative corrections $`O(\beta^2)`$, which depend on the level and the branch (Step 5).

*(d) Which grips weigh.* By (2.17), at leading order in $`\beta`$:
```math
\rho_{{\rm mark},i}=1\ \text{and}\ \rho_{{\rm bond},i}=m_{\mathbf r}\ (i=1,2)\ \text{for every level and both branches}\iff 2\Phi_i''(0)=\Phi_i'(0)^2\ (i=1,2)\ \text{and}\ \Phi_1'(0)=\Phi_2'(0)\iff F^{(i)}(q)=F^{(i)}(0)(1+\hat\beta q)^2+O(q^3)\ \text{with a common}\ \hat\beta .
\qquad\text{(2.18)}
```
- *If:* $`\kappa_j=\Phi'(0)/2`$ for both bodies gives $`\rho_{{\rm bond},i}=(\Delta\phi_1+\Delta\phi_2)/(2\Delta\bar\phi)=m_{\mathbf r}`$.
- *Only if:* $`\rho_{{\rm mark},i}=1`$ is $`2\Phi_i''(0)=\Phi_i'(0)^2`$. Then $`\rho_{{\rm bond},1}=m_{\mathbf r}`$ reads $`\Phi_2'(0)\Delta\phi_2=\Phi_1'(0)\Delta\phi_2`$, so $`\Phi_1'(0)=\Phi_2'(0)`$ wherever $`\Delta\phi_2\ne0`$.
- *In terms of $`F`$:* this is the *square grip* $`2F(0)F''(0)=F'(0)^2`$, i.e. $`(\sqrt{\lvert F\rvert})''(0)=0`$, in (G2) $`4F_0F_2=F_1^2`$, with a common $`\hat\beta:=F'(0)/(2F(0))=\beta\Phi'(0)/2`$. The values $`F^{(i)}(0)`$ are free.
- *Range:* it holds at every distance from the source and every separation, on the three graphs, for all $`L`$, $`\kappa_h`$, $`m_h>0`$ in the regime $`\varepsilon,u\ll1`$ where the leading order holds. Since $`m_{\mathbf r}=1+O(\lvert\mathbf r\rvert^2/\min(d,\ell)^2)`$ for $`\lvert\mathbf r\rvert\ll\min(d,\ell)`$ (Step 6), $`\rho_{\rm bond}=1`$ there. At larger separations $`\rho_{\rm bond}=m_{\mathbf r}\ne1`$ is set by the shape of the made field, not by the grip.
- *First deviation otherwise:* $`\rho_{{\rm mark},i}-1=(2\Phi_i''(0)-\Phi_i'(0)^2)/\Phi_i'(0)^2+O(\beta^2)`$, the same at every distance and not vanishing as $`\beta\to0`$. For square grips with $`\hat\beta_1\ne\hat\beta_2`$, $`\rho_{{\rm bond},i}=(\hat\beta_1\Delta\phi_1+\hat\beta_2\Delta\phi_2)/(2\hat\beta_i\Delta\bar\phi)+O(\beta^2)`$, which is $`(\hat\beta_1+\hat\beta_2)/(2\hat\beta_i)+O(\lvert\mathbf r\rvert/\min(d,\ell))`$: its parameter is $`\hat\beta_2/\hat\beta_1`$, independent of the distance at this order.
- *Controls:* the linear grip ($`\rho=0`$); (G2) with $`4F_0F_2\neq F_1^2`$; square grips with $`\hat\beta_1\ne\hat\beta_2`$.

For (Gθ) see (2.20)(iii) and (2.23).

*(e) First deviation for a common square (G2) grip.* Insert $`a_0=F_0(1+\beta^2w_0)`$, $`a_1=2F_0\beta`$, $`a_2=2F_0\beta^2`$, $`a_{n\ge3}=0`$ (here $`\beta=\hat\beta`$) into (2.14), then use (2.3):
```math
\rho(\mathbf r)=\frac{1+\beta^2w_0}{1+\beta^2J_2(\mathbf r)/G(\mathbf r)},\qquad
\rho_{\rm mark}-1=\beta^2\Bigl(w_0-\frac{J_2}{G_0}\Bigr)+O(\varepsilon^4)\in\Bigl[\frac{\beta^2w_0}2,\beta^2w_0\Bigr)+O(\varepsilon^4),\qquad
\frac{\rho_{\rm bond}}{m_{\mathbf r}}-1=\beta^2\Bigl(w_0-\frac{J_2(\mathbf r)}{G(\mathbf r)}\Bigr)+O(\varepsilon^4).
\qquad\text{(2.19)}
```
The ratio $`J_2(\mathbf r)/G(\mathbf r)`$ decays exponentially for $`\lvert\mathbf r\rvert\gg\ell`$. In the scaling regime it is $`\simeq1/(16\pi^2\sqrt{\kappa_h}\lvert\mathbf r\rvert^2)`$ for $`D=3`$, $`1\ll\lvert\mathbf r\rvert\ll\ell`$, from the continuum $`c_{\mathbf r}(\tau)\simeq[4\pi^2\sqrt{\kappa_h}(\lvert\mathbf r\rvert^2+\kappa_h\tau^2)]^{-1}`$. So $`\rho_{\rm bond}/m_{\mathbf r}-1\to\beta^2w_0`$ at large separation. Both deviations in (2.19) are independent of the distance to the source; $`\rho_{\rm bond}`$ itself carries $`m_{\mathbf r}`$. Beyond order $`\mu^2`$, (2.15) depends on $`(k,\sigma)`$ only through $`\zeta(\sigma M_kF_2)`$, which brings a level and branch dependence of relative order $`\varepsilon^2u`$; the same holds for (2.16) with a common grip and equal labels. For unequal labels, (2.16) adds the referral term of (b). At $`w_0=\zeta=0`$ (tree level), (2.15) and (2.16) with a common grip and equal labels are exactly $`1`$ and $`m_{\mathbf r}`$ for the square grip, at every order in $`u`$. All deviations of the common square grip at equal labels therefore come from the zero-point spread of the field. Code (i) confirms (2.19) on rings and cubic tori (Code section).

*(f) What cannot be obtained.*
```math
\begin{aligned}
&\text{(i) no (G2) grip gives }\rho_{\rm mark}=1\text{ exactly for every level and both branches;}\\
&\text{(ii) at order }\mu^2\text{ no common (G2) grip gives }\rho_{\rm mark}=1\text{ and }\rho_{\rm bond}=m_{\mathbf r}\text{ at a separation with }J_2(\mathbf r)/G(\mathbf r)\ne J_2/G_0;\\
&\text{(iii) a (Gθ) grip with }F(0)\ne0,\ \langle f'\rangle_0\ne0,\ T_f\ne0\text{ has }\rho_{\rm mark}=\frac{2F(0)\,T_f}{\theta\,\langle f'\rangle_0\,S_f}+O(1),\ \lvert\rho_{\rm mark}\rvert\to\infty\ (\theta\to0).
\end{aligned}
\qquad\text{(2.20)}
```
- (i): for $`F_2=0`$, $`\rho_{\rm mark}=0`$. For $`F_2\ne0`$, $`\zeta(\sigma M_kF_2)`$ is strictly monotone in $`\sigma M_k`$ (Step 3), so the $`2N`$ values (2.15) are pairwise different ($`\langle F\rangle_0\ne0`$).
- (ii): the two conditions $`F_1^2G_0+4F_2^2J_2=4F_2\langle F\rangle_0G_0`$ and $`F_1^2G(\mathbf r)+4F_2^2J_2(\mathbf r)=4F_2\langle F\rangle_0G(\mathbf r)`$ imply $`F_2^2\,(J_2/G_0-J_2(\mathbf r)/G(\mathbf r))=0`$, and $`F_2=0`$ gives $`\rho=0`$. Since $`J_2(\mathbf r)/G(\mathbf r)\to0`$ for $`\lvert\mathbf r\rvert/\ell\to\infty`$ ($`L\to\infty`$ first) while $`J_2/G_0>0`$, a common grip weighs the mark and the bond like $`C^{(1)}`$ together only at leading order in $`\varepsilon`$.
- (iii): $`T=\theta^2T_f`$, $`S=\theta^2S_f`$, $`a_0=F(0)+O(\theta)`$ and $`a_1=\theta\langle f'\rangle_0`$ in (2.14), with $`O(\theta)`$ relative corrections to $`T/S`$. So a (Gθ) grip with $`T_f\ne0`$ never weighs its mark like $`C^{(1)}`$ at small $`\theta`$. For $`T_f=0`$, $`\rho_{\rm mark}=O(1)`$ by (2.23), and its value is decided at order $`\theta^3`$, which is not computed. (For $`F(0)=0`$, $`a_0=\theta\langle f\rangle_0`$, and (2.14) gives the finite value $`2\langle f\rangle_0T_f/(\langle f'\rangle_0S_f)+O(\theta)`$.)

*Dependence on $`m_h`$ and $`L`$.* The deviations are controlled by $`\varepsilon^2=\beta^2w_0`$ and $`u`$, and (2.5) requires $`u<1`$ for both branches.
- $`L\to\infty`$ at fixed $`m_h>0`$: $`G_0`$, $`w_0`$ and $`J_n(\mathbf r)`$ tend to finite lattice integrals in every $`D`$, and all results have limits.
- $`m_h\to0`$ at fixed $`L`$: $`G_0\ge1/(N_fm_h^2)`$ and $`w_0\ge1/(2N_fm_h)`$ diverge (the uniform mode), so $`\varepsilon\to\infty`$ and the expansions of Steps 5 and 7(c) are not uniform in $`m_h`$. For (G2):
```math
\begin{aligned}
&\text{linear grip: }\rho_{\rm mark}=\rho_{\rm bond}=0\ \text{at every }m_h,\quad \text{cost}=\mu F_0-\tfrac12\mu^2F_1^2G_0\to-\infty;\\
&F_2\ne0,\ \mu F_2<0:\ \text{no lowest eigenvector once }2M_k\lvert F_2\rvert G_0\ge1;\\
&\mu_iF_2^{(i)}>0:\ \text{cost finite},\ C^{(1)}=-C^{\rm mark}+O(1)=\mu F_2w_0+O(1)\to\infty,\ \rho_{\rm mark}=1+O(N_fm_h);\\
&\phantom{\mu_iF_2^{(i)}>0:\ }\rho_{\rm bond}\to0\ (\propto m_h)\ \text{for a common grip},\quad \lvert\rho_{{\rm bond},i}\rvert\to\infty\ (\propto1/m_h)\ \text{for different grips in general}.
\end{aligned}
\qquad\text{(2.24)}
```
Derivation. For $`\mu_iF_2^{(i)}>0`$, $`K'`$ has a finite positive limit, because $`a_i>0`$ pins the uniform mode. So the cost (2.6) and all two-body quantities (2.13) have finite limits, and $`\Delta\phi`$ converges (the uniform part cancels). For one body, $`D_\mu\simeq aG_0`$, so $`\Delta W^{\rm mark}/\Delta W^{(1)}=-2\mu F_2G_0/D_\mu=-1+O(m_h^2)`$. Moreover $`C^{(1)}=\mu(F_0+F_2w_0)`$ diverges while the cost stays finite, so $`C^{(1)}/C^{\rm mark}=-1+O(1/w_0)`$, and $`\rho_{\rm mark}\to1`$. The bond reference $`a_1^{(i)}/a_0^{(i)}=F_1^{(i)}/\langle F^{(i)}\rangle_0`$ tends to 0 like $`1/w_0`$. For a common grip, $`v=(F_1/(2F_2))\,a`$, and $`K'_\infty\mathbf 1=\sum_ia_ie_{x_i}`$ (with $`K_\infty=\kappa_h\Delta`$) gives $`\mathbb M_\infty v=0`$. So the bond weight (2.13) and $`U_{\rm cl}`$ vanish like $`1/G_0\propto m_h^2`$, while $`U\to Z_b`$; hence $`\rho_{\rm bond}\propto m_h^2w_0\propto m_h`$. For different grips ($`\eta_1\ne\eta_2`$), $`v`$ is not parallel to $`a`$, and $`\Delta W_{\rm bond}/U`$ has a nonzero limit in general. Code (i) follows the ratios on a ring down to $`m_h=10^{-3}`$. For (G) the limit is not determined: $`\varepsilon\to\infty`$.
- After $`L\to\infty`$, as $`m_h\to0`$: $`G_0`$ diverges for $`D=1`$ ($`\propto\ell`$) and $`D=2`$ ($`\propto\ln\ell`$) and tends to $`0.2527/\kappa_h`$ for $`D=3`$; $`w_0`$ diverges logarithmically for $`D=1`$ and stays finite for $`D=2,3`$.

### Step 8. Another eigenvector of the field

Take (G2) and the eigenvector $`\lvert1\rangle`$ with one quantum in the normal mode of $`K'`$ connected, as $`s\to0`$, to the uniform mode of $`K`$ (nondegenerate at fixed $`L`$). In its Fock eigenvectors the eigenvalues of the quadratic contract are $`\mu F_0-\frac12J^TK'^{-1}J+\sum_j(n_j+\frac12)\Omega_j(K')`$, with $`\Omega_j^2`$ the eigenvalues of $`K'`$. The source changes $`J`$, not $`K'`$, and the spectrum of $`K'`$ does not depend on the body's place. So the weights (2.8) and (2.13) are the same in every Fock eigenvector. In $`\lvert1\rangle`$, $`C^{(1)}=\mu(F_0+F_2\langle q_b^2\rangle_1)`$ with $`\langle q_b^2\rangle_1=w_0+1/(N_fm_h)`$ (Hellmann–Feynman). The mark gains the $`c`$-independent term $`\Omega_0(a)-m_h-a/(2N_fm_h)=O(a^2)`$, which is not weighed. Hence
```math
\rho_{\rm mark}\big|_{\lvert1\rangle}=\frac{4F_2\bigl(\langle F\rangle_0+F_2/(N_fm_h)\bigr)}{F_1^2+\zeta_1},\qquad \zeta_1-\zeta=O(F_2^2).
\qquad\text{(2.21)}
```
The answer (2.18) is unchanged. The deviation (2.19) changes, by $`\beta^2/(N_fm_h)`$ and by $`(\zeta_1-\zeta)/F_1^2`$. The first term vanishes as $`L\to\infty`$ and diverges as $`m_h\to0`$ at fixed $`L`$. Eigenvectors with $`\beta^2\langle q_b^2\rangle_n\gtrsim1`$ lose (2.18) even at leading order.

## Result

All results hold for held Model D bodies gripping a field of oscillator cells on a ring, square or cubic torus ($`m_h>0`$). The limit $`M\to\infty`$ is taken first (Steps 1 and 5), and all results are at first order in $`g_s`$. Class (G) is the one fixed by note (a) of the question: (Gθ) $`F(0)+\theta f`$ and (GΦ) $`F(0)\Phi(\beta q)`$ with polynomially bounded derivatives.

- **(2.1)–(2.2), theorem.** For every grip, the source enters the eigenvalues only by shifting the argument of each grip by the made field $`\phi(x_i)=-g_sG(x_i-x_s)`$. At first order in $`g_s`$, every weight is $`\partial_cX[F_c]\,\Delta\phi`$, and $`\rho_{\rm mark}=\partial_c\ln C^{\rm mark}/\partial_c\ln C^{(1)}`$, independent of the places and of the distance. The cost, $`C^{(1)}=\mu\langle F\rangle_0`$ and $`C^{\rm mark}`$ are fixed by the total contracts with and without the body.
- **(2.3)–(2.4), formula.** These are the field constants and the made field ($`L\to\infty`$ first). In the scaling regime $`\ell=\sqrt{\kappa_h}/m_h\gg1`$, for $`1\ll\lvert d\rvert\ll\ell^3`$, $`\phi\propto G`$ is linear, logarithmic or $`1/\lvert d\rvert`$ (for $`D=1,2,3`$) below $`\ell`$, and $`\propto e^{-\lvert d\rvert/\ell}`$ above it; the chain form $`e^{-\alpha\lvert d\rvert}/(2\kappa_h\sinh\alpha)`$ is exact at every $`\ell`$. At any $`\ell`$ and $`\lvert d\rvert\gg\max(1,\ell)`$, $`G\asymp\lvert d\rvert^{-(D-1)/2}e^{-\alpha(\hat d)\lvert d\rvert}`$, with the direction-dependent lattice rate $`\alpha(\hat n)=\ell^{-1}+O(\ell^{-3})`$.
- **(2.5), criterion.** For (G2), a lowest eigenvector exists iff $`1+2\sigma M_kF_2G_0>0`$. Otherwise the lowest eigenvalue of $`C_M`$ tends to $`-\infty`$.
- **(2.6)–(2.7), formula.** For (G2), exactly: cost $`=\mu F_0-\mu^2F_1^2G_0/(2D_\mu)+Z(2\mu F_2)`$, $`C^{(1)}=\mu(F_0+F_2w_0)`$, and $`C^{\rm mark}=-\mu^2G_0(F_1^2+\zeta)/(2D_\mu)<0`$. The zero-point term $`\zeta\ge0`$ is, for $`F_2\ne0`$, strictly monotone in $`\sigma M_kF_2`$.
- **(2.8), formula.** For (G2), exactly: $`\Delta W=\mu F_1\Delta\phi/D_\mu`$, $`\Delta W^{(1)}=\mu F_1\Delta\phi`$, $`\Delta W^{\rm mark}=-2\mu^2F_1F_2G_0\Delta\phi/D_\mu`$. The zero-point part is not weighed.
- **(2.9)–(2.10), formula.** For (G), $`C^{(1)}=\mu a_0`$ and $`\Delta W^{(1)}=\mu a_1\Delta\phi`$ hold exactly. Further, $`C^{\rm mark}=-\mu^2S`$ with $`S=\sum_{n\ge1}a_n^2J_n/n!>0`$, and $`\Delta W^{\rm mark}=-2\mu^2T\Delta\phi`$ with $`T=\sum_{n\ge1}a_na_{n+1}J_n/n!`$, up to $`O(\theta^3)`$ for (Gθ), and up to $`O(\beta^4)`$ resp. $`O(\beta^5)`$ (relative $`O(\beta^2)`$, level dependent) for (GΦ). The $`a_n`$ exist, $`\partial_ca_n=a_{n+1}`$, and the series converge absolutely. At fixed $`g_s`$, the Taylor coefficients of the compressed eigenvalue through order $`\theta^2`$ (Gθ), resp. $`\beta^3`$ (GΦ), converge to these values as $`M\to\infty`$; higher coefficients are not claimed. Where $`C`$ has no lowest eigenvalue, the remainder orders are formal orders of the coefficient series, not remainder bounds.
- **(2.22), formula.** For (GΦ), with $`\varepsilon^2=\beta^2w_0`$: $`a_n=F(0)\beta^n[\Phi^{(n)}(0)+O(\varepsilon^2)]`$, $`S(\mathbf r)=F(0)^2\beta^2J_1(\mathbf r)[\Phi'(0)^2+O(\varepsilon^2)]`$ and $`T(\mathbf r)=F(0)^2\beta^3J_1(\mathbf r)[\Phi'(0)\Phi''(0)+O(\varepsilon^2)]`$, uniformly in $`\mathbf r`$. The same holds for the two-grip sums.
- **(2.23), formula.** The mark weight vanishes at the lowest order for (Gθ) with $`T_f=0`$ (e.g. odd $`f`$) and for (GΦ) with $`\Phi''(0)=0`$ (e.g. $`\Phi-1`$ odd). A nonzero weight can first appear at order $`\theta^3`$, resp. $`\beta^5`$; its value is not computed. Then $`\rho_{\rm mark}=O(1)`$ (Gθ, $`F(0)\ne0`$), resp. $`O(\beta^2)`$.
- **(2.11)–(2.13), formula.** For two grips of the class at order $`\mu_1\mu_2`$:
  - The bond is $`U=-2\mu_1\mu_2S_{12}(\mathbf r)`$, with weight $`-2\mu_1\mu_2[T_{12}(\mathbf r)\Delta\phi_1+T_{21}(\mathbf r)\Delta\phi_2]`$.
  - For a common grip, $`U`$ has the sign of $`-\mu_1\mu_2`$; in (G2) this holds exactly. For different grips $`U`$ can vanish at some separations.
  - For (G2), exactly, $`\Delta W_{\rm bond}=-2\sum_i\eta_i\Delta\phi_iv_i(\mathbb Mv)_i`$, and the zero-point part $`Z_b`$ is not weighed.
  - The midpoint factor is $`m_{\mathbf r}=(\Delta\phi_1+\Delta\phi_2)/(2\Delta\bar\phi)`$, for a far reference, $`d\gg\lvert\mathbf r\rvert`$ and $`L\to\infty`$ first. It is $`1+O(\lvert\mathbf r\rvert^2/d^2)`$ for $`1\ll d\ll\ell`$ ($`D=2,3`$). For $`d\gg\max(1,\ell)`$ it is $`\cosh(t^*\cdot\mathbf r/2)[1+O(\lvert\mathbf r\rvert/d+\lvert t^*\rvert\lvert\mathbf r\rvert^2/d)]`$, with the lattice decay vector $`t^*(\hat d)`$; for $`D=1`$ it is exactly $`\cosh(\alpha r/2)`$. In the scaling regime, $`t^*=\hat d/\ell+O(\ell^{-3})`$ gives $`\cosh((\mathbf r\cdot\hat d)/(2\ell))[1+O(\lvert\mathbf r\rvert/d+\lvert\mathbf r\rvert^2/(d\ell)+\lvert\mathbf r\rvert/\ell^3)]`$, i.e. $`1+(\mathbf r\cdot\hat d)^2/(8\ell^2)+O(\lvert\mathbf r\rvert^4/\ell^4+\lvert\mathbf r\rvert^2/(d\ell)+\lvert\mathbf r\rvert^2/\ell^4)`$ for $`\lvert\mathbf r\rvert\ll\ell`$.
  - Referring the pair to a body instead of the midpoint gives an error of first order in $`\lvert\mathbf r\rvert/\min(d,\ell)`$.
- **(2.14), formula.** At order $`\mu^2`$, for every pair of grips of the class: $`\rho_{{\rm mark},i}=2a_0^{(i)}T_i/(a_1^{(i)}S_i)`$ and $`\rho_{{\rm bond},i}=(a_0^{(i)}/a_1^{(i)})(T_{12}\Delta\phi_1+T_{21}\Delta\phi_2)/(S_{12}\Delta\bar\phi)`$, with the single-body reference of note (b). For a common grip, $`\rho_{\rm bond}=m_{\mathbf r}\rho(\mathbf r)`$ with $`\rho(\mathbf r)=2a_0T(\mathbf r)/(a_1S(\mathbf r))`$. The ratios are the same for every level and both branches. $`\rho_{\rm mark}`$ and, for a common grip, $`\rho_{\rm bond}/m_{\mathbf r}`$ do not depend on the distance to the source; $`\rho_{\rm bond}`$ does, through $`\Delta\phi_j/\Delta\bar\phi`$. Excluded are $`a_0^{(i)}=0`$, $`a_1^{(i)}=0`$, $`\Delta\bar\phi=0`$ and separations with $`U=0`$ (different grips only).
- **(2.15)–(2.16), formula.** For (G2), exactly:
  - $`\rho_{\rm mark}=4F_2\langle F\rangle_0/(F_1^2+\zeta)`$.
  - Whenever $`U\ne0`$: $`\rho_{{\rm bond},i}=-2\langle F^{(i)}\rangle_0\sum_j\eta_jv_j(\mathbb Mv)_j\Delta\phi_j/[F_1^{(i)}(U_{\rm cl}+Z_b)\Delta\bar\phi]`$. For $`U_{\rm cl}\ne0`$ this equals $`4\langle F^{(i)}\rangle_0\sum_j\eta_jw_j\Delta\phi_j/[F_1^{(i)}(1+Z_b/U_{\rm cl})\Delta\bar\phi]`$. Pairs of different grips with $`U_{\rm cl}=0\ne Z_b`$ exist and are not excluded.
  - For a common grip $`U_{\rm cl}\ne0`$, and the bond is weighed at the place $`\sum_jw_jx_j`$. This is the midpoint for equal labels; otherwise it is shifted at relative order $`uG(\mathbf r)/G_0`$.
- **(2.17)–(2.18), criterion.** For (GΦ) at order $`\mu^2`$, uniformly in $`\mathbf r`$: $`\rho_{{\rm mark},i}=2\Phi_i''(0)/\Phi_i'(0)^2+O(\varepsilon^2)`$ and $`\rho_{{\rm bond},i}=(\kappa_1\Delta\phi_1+\kappa_2\Delta\phi_2)/(\Phi_i'(0)\Delta\bar\phi)+O(\varepsilon^2)(\lvert\Delta\phi_1\rvert+\lvert\Delta\phi_2\rvert)/\lvert\Delta\bar\phi\rvert`$, with $`\kappa_j=\Phi_j''(0)/\Phi_j'(0)`$; higher orders add relative $`O(\beta^2)`$.
  - Hence, at leading order in $`\beta`$, $`\rho_{{\rm mark},i}=1`$ and $`\rho_{{\rm bond},i}=m_{\mathbf r}`$ for both bodies, every level and both branches iff both grips are square, $`2F(0)F''(0)=F'(0)^2`$ (in (G2) $`4F_0F_2=F_1^2`$), with a common $`\hat\beta=F'(0)/(2F(0))`$.
  - This holds at every distance and separation, on all three graphs, and for all $`L,\kappa_h,m_h>0`$ with $`\varepsilon,u\ll1`$. $`\rho_{\rm bond}=m_{\mathbf r}=1+O(\lvert\mathbf r\rvert^2/\min(d,\ell)^2)`$ for $`\lvert\mathbf r\rvert\ll\min(d,\ell)`$.
  - Otherwise $`\rho_{{\rm mark},i}-1=(2\Phi_i''(0)-\Phi_i'(0)^2)/\Phi_i'(0)^2`$ does not vanish as $`\beta\to0`$. Square grips with $`\hat\beta_1\ne\hat\beta_2`$ have $`\rho_{{\rm bond},i}\to(\hat\beta_1+\hat\beta_2)/(2\hat\beta_i)`$ for $`\lvert\mathbf r\rvert\ll\min(d,\ell)`$.
- **(2.19), formula.** For a common square (G2) grip at order $`\mu^2`$:
  - $`\rho_{\rm mark}-1=\beta^2(w_0-J_2/G_0)+O(\varepsilon^4)`$, which lies in $`[\beta^2w_0/2,\beta^2w_0)`$ and is independent of the distance to the source.
  - $`\rho_{\rm bond}/m_{\mathbf r}-1=\beta^2(w_0-J_2(\mathbf r)/G(\mathbf r))+O(\varepsilon^4)`$, also independent of that distance, which tends to $`\beta^2w_0`$ at separations $`\gg\ell`$.
  - Beyond order $`\mu^2`$, level dependence enters at relative order $`\varepsilon^2u`$ for the mark and for the bond with equal labels. At tree level the square grip weighs the mark, and the bond with equal labels, exactly.
- **(2.20), negative.**
  - (i) No (G2) grip has $`\rho_{\rm mark}=1`$ exactly for every level and both branches.
  - (ii) At order $`\mu^2`$, no common (G2) grip has $`\rho_{\rm mark}=1`$ and $`\rho_{\rm bond}=m_{\mathbf r}`$ at any separation with $`J_2(\mathbf r)/G(\mathbf r)\ne J_2/G_0`$; this includes all separations $`\lvert\mathbf r\rvert\gg\ell`$ ($`L\to\infty`$ first).
  - (iii) A (Gθ) grip with $`F(0)\ne0`$, $`\langle f'\rangle_0\ne0`$ and $`T_f\ne0`$ has $`\lvert\rho_{\rm mark}\rvert\to\infty`$ as $`\theta\to0`$.
- **(2.21), formula.** In the (G2) eigenvector with one quantum in the uniform mode, the weights are unchanged, and (2.18) holds at leading order. The deviation changes by $`\beta^2/(N_fm_h)`$ and by an $`O(F_2^2)`$ zero-point term.
- **(2.24), formula.** As $`m_h\to0`$ at fixed $`L`$, for (G2):
  - The linear grip has $`\rho_{\rm mark}=\rho_{\rm bond}=0`$ at every $`m_h`$, while its cost diverges.
  - For $`F_2\ne0`$, the branch with $`\mu F_2<0`$ loses its lowest eigenvector.
  - In sectors with $`\mu_iF_2^{(i)}>0`$: the cost has a finite limit; $`C^{(1)}`$ and $`C^{\rm mark}`$ diverge as $`\pm\mu F_2w_0`$; $`\rho_{\rm mark}=1+O(N_fm_h)\to1`$; $`\rho_{\rm bond}\to0`$ for a common grip, while $`\lvert\rho_{{\rm bond},i}\rvert\to\infty`$ for different grips in general.
  - For (G) the expansion parameter $`\varepsilon^2=\beta^2w_0`$ diverges. As $`L\to\infty`$ at fixed $`m_h>0`$, all results have limits.

## Consistency checks

1. **Dimensions.** $`[a_n]=E^{n/2}`$, $`[J_n]=E^{-n-1}`$, $`[G]=E^{-2}`$, $`[w_0]=E^{-1}`$, $`[\beta]=E^{1/2}`$. So $`\mu^2a_n^2J_n`$ has dimension $`E`$; $`\rho(\mathbf r)`$, $`\kappa_j/\Phi_i'(0)`$, $`\varepsilon^2=\beta^2w_0`$, $`\beta^2J_2/G_0`$ and $`u=2M_k\lvert F_2\rvert G_0`$ are dimensionless. Passed.
2. **(G) against (G2) and the linear grip.** (2.9)–(2.12) with $`a_1=F_1`$, $`a_2=2F_2`$, $`a_{n\ge3}=0`$ give $`C^{\rm mark}=-\mu^2(F_1^2G_0/2+2F_2^2J_2)`$, $`\Delta W^{\rm mark}=-2\mu^2F_1F_2G_0\Delta\phi`$ and the two-grip bond weight $`-2\mu_1\mu_2G(\mathbf r)[F_2^{(1)}F_1^{(2)}\Delta\phi_1+F_1^{(1)}F_2^{(2)}\Delta\phi_2]`$. These are the order-$`\mu^2`$ terms of (2.6)–(2.8) and (2.13), with $`\zeta\simeq4F_2^2J_2/G_0`$. For $`F_2=0`$ all give $`\rho=0`$. Passed.
3. **Square grip at tree level.** Without the zero-point part, (2.1) and (2.6) give for $`F=F_0(1+\beta q)^2`$ the shifted cost $`\mu F_0(1+\beta c)^2/(1+2\mu F_0\beta^2G_0)=\mu F(c)/D_\mu`$. This is proportional to $`F(c)`$ for every $`\mu`$, so mark and $`C^{(1)}`$ are weighed alike, consistent with (2.15) at $`w_0=\zeta=0`$. Passed.

## Open issues

- (G) beyond the leading order in $`\beta`$: the level-dependent relative corrections $`O(\beta^2)`$ to (2.17)–(2.18) are bounded but computed only for (G2) (through $`\zeta`$ and $`u`$).
- The values of the first nonzero mark weights of (2.23) ($`\theta^3`$, $`\beta^5`$), and hence $`\rho_{\rm mark}`$ for (Gθ) with $`T_f=0`$, are not computed (not asked by note (c)).
- The limit $`m_h\to0`$ at fixed $`L`$ is determined only for (G2) grips.
- The fields of 06-ilang-source and 07-ilang-weight (03-gas-grip), $`m_h=0`$ with an anchor, and the formation speed are outside this package.
- Whether the square grip with a common $`\hat\beta`$, or the tuned grip $`4F_2\langle F\rangle_0=F_1^2+\zeta`$, is selected by anything in the language is not addressed (item 6, M10).

## Code

- `code/v3/check_g2_ratios.py` (check, item (i) of the question; cited in Step 7 and in (2.24)).
  - *Setup.* Rings $`L=40,80`$ and cubic tori $`L=8,12`$, with $`\kappa_h=1`$, $`m_h=0.3`$ ($`\ell=3.3`$). Levels $`M_0=0.5`$, $`M_1=0.75`$, both branches. Grips $`(F_0,F_1,F_2)`$: square $`(1,0.6,0.09)`$ ($`\hat\beta=0.3`$), generic $`(1,0.6,0.15)`$, linear $`(1,0.6,0)`$, and, in pairs only, square $`(1,0.4,0.04)`$ ($`\hat\beta=0.2`$). Bonds are computed for the three common grips and for the pairs square($`0.3`$)+square($`0.2`$) and square+generic.
  - *Method.* The exact lowest eigenvalue $`\sum_is\mu_iF_0^{(i)}+\frac12\mathrm{Tr}\sqrt{K'}-\frac12J^TK'^{-1}J`$ of the uncompressed contract is computed by dense linear algebra. $`C^{(1)}`$ and $`W^{(1)}`$ come from 4-point differences in $`s`$. Weights are the exact linear coefficient in $`g_s`$, $`-J_b^TK'^{-1}e_{x_s}`$; the eigenvalue is quadratic in $`g_s`$ and its trace part does not depend on $`g_s`$. Marks are evaluated at three distances from the source per graph. Bonds are evaluated at separations $`2,4`$, three midpoint distances and four label pairs: $`(0,+)(0,+)`$, $`(1,-)(1,-)`$, $`(0,+)(1,+)`$, $`(0,+)(0,-)`$. The reference of $`\rho_{{\rm bond},i}`$ is computed from a single body with the grip of body $`i`$ at the midpoint (note (b)). The exact formula compared is the unfactored (2.16). On every graph one further pair, labels $`(0,+)(0,+)`$, $`\lvert\mathbf r\rvert=2`$, has the square grip and the grip $`(1,tF_1,0.09)`$, with $`t`$ the smaller root of $`v^T\mathbb Mv=0`$, so that $`U_{\rm cl}=0`$ (I5).
  - *Results* (`output/g2_summary.json`, `output/g2_mark.csv`, `output/g2_bond.csv`):
    - $`\lvert C^{(1)}-\mu\langle F\rangle_0\rvert\le3.4\cdot10^{-10}`$.
    - $`\rho_{\rm mark}`$ agrees with (2.15) to $`3.7\cdot10^{-9}`$; its spread over distances is $`\le1.7\cdot10^{-13}`$.
    - $`U`$ agrees with $`U_{\rm cl}+Z_b`$ (2.13) to $`8.7\cdot10^{-13}`$. Both $`\rho_{{\rm bond},i}`$ agree with (2.16) to $`1.2\cdot10^{-9}`$, for common and for different grips.
    - Pair with $`U_{\rm cl}=0`$ ($`\lvert U_{\rm cl}\rvert\le10^{-16}`$; tuned $`F_1=0.0213`$ on the rings, $`9.4\cdot10^{-4}`$ and $`7.0\cdot10^{-4}`$ on the cubic tori): $`U`$ agrees with $`Z_b`$ to $`6.7\cdot10^{-13}`$, with $`Z_b=-2.1\cdot10^{-4}`$ (rings) and $`-5.3\cdot10^{-7}`$, $`-3.7\cdot10^{-7}`$ (cubic). Both $`\rho_{{\rm bond},i}`$ (from $`97`$ to $`2.5\cdot10^6`$, large because $`U`$ is small) agree with the unfactored (2.16) to a relative $`1.8\cdot10^{-6}`$. That is the accuracy of $`U`$ on the cubic tori; on the rings the agreement is $`\le1.8\cdot10^{-10}`$.
    - Linear grip: $`\lvert\rho\rvert\le2.2\cdot10^{-13}`$.
    - Square grip: $`\rho_{\rm mark}-1\in[0.0357,0.0381]`$ on the rings against $`\beta^2(w_0-J_2/G_0)=0.0372`$, and $`\in[0.0154,0.0157]`$ on the cubic tori against $`0.0157`$ ($`L=8`$) and $`0.0155`$ ($`L=12`$). The level spread is $`\le0.0024`$.
    - Common square grip, equal labels: $`\rho_{\rm bond}/m_{\mathbf r}-1=0.0430,\,0.0452`$ (rings, $`\lvert\mathbf r\rvert=2,4`$) against $`0.0436,\,0.0454`$ of (2.19); $`0.02004,\,0.02014`$ ($`L=8`$) and $`0.01998,\,0.02012`$ ($`L=12`$), the same as (2.19) to the digits shown. The values are the same at all midpoint distances, while $`m_{\mathbf r}`$ itself ranges from $`0.23`$ to $`0.91`$ on the cubic tori.
    - Generic grip: $`\rho_{\rm mark}=1.742`$–$`1.760`$ (rings) and $`1.700`$–$`1.702`$ (cubic) against $`1.750`$ and $`1.701`$ of (2.14), with leading value $`4F_0F_2/F_1^2=1.667`$.
    - Different square grips ($`\hat\beta=0.3,0.2`$), equal labels: $`\rho_{{\rm bond},1}`$ and $`\rho_{{\rm bond},2}`$ differ by the factor $`1.46`$–$`1.48`$, against $`\hat\beta_1/\hat\beta_2=1.5`$ at leading order. They lie within $`5\,\%`$ (rings, $`\varepsilon^2=0.047`$) and $`2.1\,\%`$ (cubic, $`\varepsilon^2=0.020`$) of the leading values $`(\hat\beta_1\Delta\phi_1+\hat\beta_2\Delta\phi_2)/(2\hat\beta_i\Delta\bar\phi)`$ of (2.18).
    - The order-$`\mu^2`$ formula (2.14) differs from the exact ratio by up to $`0.11`$ for a common grip, for unequal labels on the rings ($`u\approx0.3`$, $`G(\mathbf r)/G_0\approx0.55`$, $`\lvert\mathbf r\rvert\sim\ell`$). This is the referral term of Step 7(b). For different grips the difference is up to $`0.042`$.
  - *Limit $`m_h\to0`$* (`output/g2_mh_limit.csv`; ring $`L=40`$, $`m_h=0.3,0.1,0.03,0.01,0.003,0.001`$, sectors $`\mu>0`$):
    - $`\rho_{\rm mark}`$ agrees with (2.15) to $`3.2\cdot10^{-7}`$. For the generic grip it runs $`1.744,1.771,1.782,1.693,1.449,1.220`$ ($`\mu=0.5`$), towards 1, while $`C^{(1)}`$ grows from $`0.54`$ to $`1.48`$ and the cost settles at $`0.27`$.
    - The branch $`\mu=-0.75`$ has no lowest eigenvector from $`m_h=0.1`$ (generic) and $`m_h=0.03`$ (square) on.
    - Linear grip: $`\rho=0`$, cost $`-1125`$ and $`-2531`$ at $`m_h=10^{-3}`$.
    - Common generic grip, $`r=2`$: $`\rho_{\rm bond}=1.86,1.79,1.61,0.73,0.11,0.021`$, towards 0.
    - Square+generic: $`\rho_{{\rm bond},1}=1.34,\dots,1.79,2.82`$ and $`\rho_{{\rm bond},2}=1.38,\dots,2.15,3.84`$, growing. Its $`U`$ changes sign between $`m_h=0.03`$ and $`0.01`$ at equal labels, an instance of a vanishing two-grip bond profile.
  - *Outputs:* `output/g2_mark.csv`, `output/g2_bond.csv`, `output/g2_mh_limit.csv`, `output/g2_summary.json`.
- `code/v3/check_compression.py` (check, item (ii); cited in Steps 1 and 5).
  - *Setup.* Ring of three cells, $`\kappa_h=m_h=1`$ ($`\omega_k=1,2,2`$, $`G_0=1/2`$, $`w_0=1/3`$), $`M=4,\dots,32`$; sparse matrices, lowest eigenvalue by Lanczos.
  - *(G2)*, grip $`(1,0.5,0.2)`$ with $`\mu=\pm0.75`$. The lowest eigenvalue of $`C_M`$ decreases monotonically in $`M`$ to the exact value of (2.6). The error is $`2.6\cdot10^{-2}`$ at $`M=4`$, $`1.0\cdot10^{-6}`$ at $`M=12`$, $`2\cdot10^{-13}`$ at $`M=24`$ and $`\le2.5\cdot10^{-14}`$ at $`M=32`$; the costs converge likewise.
  - *(G)*, grip $`F=1+\theta(\sin q+\frac12(1-\cos q))`$ with $`\mu=0.75`$, class (Gθ), at $`\theta=0.05,0.1,0.2,0.4`$. All four lie in the range $`2\lvert\theta\rvert\mu\sup\lvert f\rvert<m_h`$ ($`\sup\lvert f\rvert=1.618`$) where the eigenvalue is the lowest.
    - *Reference.* The uncompressed lowest eigenvalue is computed independently on a sinc (Colbert–Miller) position grid in all three cells, with spacings $`0.30`$ ($`35^3`$ points) and $`0.24`$ ($`47^3`$ points). The two grids agree to $`\le1.1\cdot10^{-14}`$, and at $`\theta=0`$ they reproduce the exact value $`3.25`$ to $`7\cdot10^{-15}`$.
    - *Compressed eigenvalue.* The lowest eigenvalue of $`C_M`$ lies above the reference and decreases monotonically, down to round-off at $`M=32`$. The error is $`2.3`$–$`2.5\cdot10^{-2}`$ at $`M=4`$, $`0.6`$–$`0.9\cdot10^{-6}`$ at $`M=12`$, $`0.5`$–$`4.6\cdot10^{-13}`$ at $`M=24`$, and $`\le1.0\cdot10^{-14}`$ at $`M=32`$, for all four $`\theta`$.
    - *Taylor coefficients.* From Rayleigh–Schrödinger theory on the finite matrix, they converge to $`\mu\langle f\rangle_0=0.0575694`$ and $`-\mu^2S/\theta^2=-0.1033310`$ of (2.9). The errors are $`4.6\cdot10^{-3}`$ and $`6\cdot10^{-4}`$ at $`M=4`$, $`\le8\cdot10^{-13}`$ at $`M=24`$, and $`\le3.1\cdot10^{-15}`$ at $`M=32`$.
    - *Remainder.* The residual of the reference against the second-order expression, divided by $`\theta^3`$, is $`0.01397,0.01401,0.01407,0.01414`$ for the four $`\theta`$: the remainder of (2.9) is cubic in $`\theta`$.
  - *Unbounded (Gθ) grip* $`f=q+q^2/2+q^3/6`$, $`\mu=0.75`$ (Step 5 (iv)). Here $`C`$ is unbounded below for $`\theta\ne0`$. The first two Taylor coefficients of the compressed eigenvalue converge to $`\mu\langle f\rangle_0=\mu w_0/2=0.125`$ and $`-\mu^2S=-\mu^2[(1+w_0/2)^2J_1+J_2/2+J_3/6]=-0.2032769`$ of (2.9). Their errors are $`1.0\cdot10^{-2}`$ and $`6.6\cdot10^{-3}`$ at $`M=4`$, $`6.8\cdot10^{-7}`$ and $`7.2\cdot10^{-7}`$ at $`M=12`$, $`1.1\cdot10^{-13}`$ and $`3.3\cdot10^{-13}`$ at $`M=24`$, and $`\le6.2\cdot10^{-15}`$ at $`M=32`$.
  - *Output:* `output/compression.json`.

## Methods used

- Sector reduction, unitary shift by the made field
- Gaussian lowest eigenvector of a quadratic contract; Sherman–Morrison, matrix determinant lemma, interlacing
- Min-max for compressions; strong resolvent convergence of compressions; Agmon (weighted) estimate in the number of quanta
- Rayleigh–Schrödinger perturbation theory and order counting; Wick theorem, Mehler expansion, Gaussian integration by parts, heat equation for Gaussian averages; imaginary-$`\lambda`$ correlation functions
- Lattice Green functions on rings and tori, continuum and saddle-point asymptotics
- Numerical linear algebra (dense and sparse eigenvalues, finite differences); sinc position grid (Colbert–Miller)
