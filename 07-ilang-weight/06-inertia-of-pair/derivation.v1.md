# Inertia of a pair bound through the field

- **Subproject:** 07-ilang-weight
- **Package:** 06-inertia-of-pair
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-21

## Setup and assumptions

**Setting (assumptions, M8, M9).** As in question.md: $`N_f\ge1`$ field objects ($`c=+1`$) on a ring of even $`L\ge6`$ places with own term $`C_1=-t_f\sum_x(\lvert x\rangle\langle x+1\rvert+{\rm h.c.})`$, $`\Phi_x`$ the number at $`x`$, $`n=N_f/L`$; two Model D bodies $`b_1,b_2`$ of different types, clock levels $`k_i`$ with half-gaps $`M_i`$, branches $`\sigma_i`$, coupled by (a) or (c) with constants $`\gamma_i`$, $`g_i:=\sigma_i\gamma_iM_i`$, no pair term between them, records at $`\kappa\to0`$; the field in its lowest state adapted to the bodies; regime R (R1, R2) as stated there. Order counting: $`\varepsilon:=\max_i\lvert\gamma_i\rvert`$ ($`g_i=O(\varepsilon)`$). Speeds of (2.14): $`c_i=\tau_i`$ (a), $`c_i=\tau_i(1+\gamma_in)`$ (c); $`s_c:=+1`$ (a), $`-1`$ (c).

**Inputs** (verbatim in question.md). From 07-ilang-weight/02-two-free-bodies: the joint translation $`\mathcal T=e^{-i\hat P}`$, $`[\mathcal T,C]=0`$ (2.1); $`E(x_1,x_2)=\sigma_1M_1+\sigma_2M_2+N_f\varepsilon_0(x_1,x_2)`$ (2.3); the band contract $`H_{\rm eff}=W+K_1+K_2+O(\tau^4)`$, $`W={\rm diag}\,E(j,l)`$ (2.10), $`K_i`$ moving $`b_i`$ by $`0,\pm2`$; $`E''_{k_1,\sigma_1}(0)=-8\bar\kappa`$ (2.11), hence $`\mu_i=-1/(8\bar\kappa_i)`$; $`\mu_i=\sigma_iR_i/c_i^2+O(\gamma_i^2)`$ with $`R_i=M_i(1+\gamma_in)+O(\gamma_i^3)`$ (2.14); $`\delta\kappa(j,l)/\bar\kappa=\mp\gamma_1\overline{\delta\rho}_l(j)+r_1`$, $`\gamma_1\delta\rho_l(y)=\sigma_1M^{(2)}(y,l)/M_1+O(\gamma_1g_2^2)`$, $`r_1=O(\varepsilon^3)`$ (2.16), upper sign (a). From 06-ilang-source/04-profile: $`M=N_f[\varepsilon_0(g_1,g_2)-\varepsilon_0(g_1,0)-\varepsilon_0(0,g_2)+\varepsilon_0(0,0)]`$ (4.2). From 06-ilang-source/07-dressed-fall: $`a_{k,\sigma}(0)=-E''_{k,\sigma}(0)\sum_j\phi_{j+1}\phi_{j-1}W'_{k,\sigma}(j)+O(g_s^2)+O(\tau^4\gamma g_s)`$ (7.7). From 07-ilang-weight/04-weight-of-bond: $`\ell(r)=\frac{L^2-1}{12L}-\frac{r(L-r)}{2L}`$ and $`E(r)-E(r')=\frac{ng_1g_2}{t_fL}[r(L-r)-r'(L-r')]+O(n\lvert g_1g_2\rvert\ell_0\eta/t_f)`$ (4.3); $`W_i(x)=ng_i\phi(x)+O(\varepsilon^2g_s)`$ with $`\phi(x)=-\frac{2g_s}{t_f}\ell(x-x_s)`$ (4.5); $`W_{\rm pair}=W_1(x_1)+W_2(x_2)+W_b`$ with $`W_b`$ (4.7).

**Notation.** $`\bar t_0:=\bar\kappa_1+\bar\kappa_2=-\tfrac18(\mu_1^{-1}+\mu_2^{-1})`$; $`F:=n\lvert g_1g_2\rvert/t_f`$; binding ratio $`\chi:=F/\lvert\bar t_0\rvert`$; $`E_i(P)`$ the band level of $`b_i`$ alone with the field, $`E_\varnothing`$ the lowest eigenvalue of the field alone.

**Binding regime B (assumption).** B1: the relative level $`\nu`$ considered decays on a scale $`\xi_\nu\ll L`$ (for the extreme level: $`\chi L^3\gg1`$; $`\xi_0\simeq(4/\chi)^{1/3}`$ for $`\chi\lesssim1`$, $`\xi_0\simeq1`$ for $`\chi\gtrsim1`$). B2: $`\lvert\bar t_0\rvert\gg\varepsilon^2\max_i\lvert\bar\kappa_i\rvert`$ (the relative hopping does not cancel). B3: $`\lvert\beta_\nu\rvert\gg\tau'^2/(\delta_1\delta)`$ with $`\beta_\nu`$ of (6.5), so that the order-$`\tau^4`$ terms dropped by R2 stay small (Step 3).

**Class.** Couplings (a), (c), $`N_f\ge1`$, even $`L\ge6`$, all branch combinations, both signs of $`\gamma_1\gamma_2`$, under R and B. Results are at order $`\tau_i^2`$ in the band contract and, unless stated otherwise, at leading order in $`\varepsilon`$ at fixed $`\chi`$.

## Derivation

### Step 1. The band contract in a sector of $`P`$

By (2.1) the group $`\mathcal G`$ and (2.10) are invariant under $`\mathcal T`$; take every held field state $`\Omega_{jl}`$ real (lowest state of a real symmetric contract) and $`\Omega_{j+1,l+1}`$ the translate of $`\Omega_{jl}`$. Then $`E(j,l)=E(l-j)`$, and with $`\rho:=l-j`$ define $`\kappa_1(\rho):=\langle e_{j+1,l}\vert K_1\vert e_{j-1,l}\rangle`$ (the $`\kappa(j,l)`$ of (2.16)), $`\kappa_2(\rho):=\langle e_{j,l+1}\vert K_2\vert e_{j,l-1}\rangle`$, and $`d_i(r)`$ the diagonal of $`K_i`$. They are real (two motion terms give $`(\mp i\sigma_1)(\mp i\sigma_1)`$ or $`\sigma_1^2`$, field overlaps and denominators are real) and even in $`\rho`$ (the reflection $`x\to-x`$ of all places times $`\sigma_3`$ on both bodies maps $`A\to A`$, $`B\to B`$ and (a), (c) into themselves). By (2.16) and its $`1\leftrightarrow2`$ form, $`\kappa_i(\rho)=\bar\kappa_i(1+O(\varepsilon^2))`$; the same energy-denominator argument gives $`d_i(r)=\bar d_i(1+O(\varepsilon^2))`$. A $`\mathcal T`$-eigenstate with $`\mathcal T\psi=e^{-iP}\psi`$ is $`\psi(j,l)=e^{iPj}g(l-j)`$, and $`H_{\rm eff}`$ acts on $`g`$ as
```math
(h_Pg)(r)=U(r)g(r)+t(r+1;P)\,g(r+2)+t(r-1;P)^*g(r-2),\qquad t(\rho;P):=\kappa_1(\rho)e^{-2iP}+\kappa_2(\rho),\qquad U:=E+d_1+d_2. \qquad\text{(6.1)}
```
Each $`K_i`$ moves its body by an even number of places, so $`r`$ even and $`r`$ odd form two separate rings of $`L/2`$ sites. (6.1) is defined for every real $`P`$: it is the sector contract with body 1 as representative, continued in $`P`$ (the continuation used throughout and in the code). $`E_b(P)`$ is an eigenvalue of $`h_P`$.

### Step 2. Bound levels (item 1)

By (2.3) and (4.2), $`E(r)=E_1^{(0)}+E_2^{(0)}-E_\varnothing+M(r)`$, $`E_i^{(0)}`$ the $`\tau=0`$ level of $`b_i`$ alone with the field. Second-order perturbation of $`\varepsilon_0`$ (one-object ground state $`L^{-1/2}\sum_x\lvert x\rangle`$, excitation energies $`2t_f(1-\cos q)`$) gives the mixed term $`-2g_1g_2\ell(r)/(t_fL)`$, consistent with (4.3):
```math
M(r)=M^{(2)}(r)+O\big(n\lvert g_1g_2\rvert\ell_0\eta/t_f\big),\quad M^{(2)}(r)=-\frac{2ng_1g_2}{t_f}\ell(r),\quad U(r)-U(0)=V(r)+O\big(n\lvert g_1g_2\rvert\ell_0\eta/t_f\big)+O(\varepsilon^2\lvert\bar\kappa\rvert),\quad V(r):=\frac{ng_1g_2}{t_fL}\,r(L-r). \qquad\text{(6.2)}
```
$`V`$ is even, monotone in $`\lvert r\rvert`$ on $`[0,L/2]`$, rises like $`F\lvert r\rvert`$ near $`r=0`$ for $`g_1g_2>0`$ (well) and falls like $`-F\lvert r\rvert`$ for $`g_1g_2<0`$ (hill). *Criterion of localization:* the real eigenvector $`f_\nu`$ of $`h_0`$ decays away from $`r=0`$ on a scale $`\xi_\nu\ll L`$, so that its weight near $`r=L/2`$ is exponentially small in $`L/\xi_\nu`$ (B1). On a chain the sign of the hopping is a gauge ($`f(r)\to(-1)^{r/2}f(r)`$; on the ring up to terms exponentially small by B1), so the edges of the spectrum of $`h_0`$ depend on $`\lvert\bar t_0\rvert`$ and $`V`$ only; a well binds levels below the uniform band $`2\bar t_0\cos2k`$, a hill above it (standard for one-dimensional chains), and the level near the opposite extremum $`r=L/2`$ fails the criterion. The extreme eigenvector of a real chain is of one sign iff the hoppings have the sign that puts that edge at $`k=0`$ (Perron–Frobenius); $`t(\rho;0)`$ has the sign of $`\bar t_0`$ by B2. With $`g_1g_2=\sigma_1\sigma_2\gamma_1\gamma_2M_1M_2`$:
```math
\text{bound levels: the lowest if }\sigma_1\sigma_2\gamma_1\gamma_2>0,\ \text{the highest if }\sigma_1\sigma_2\gamma_1\gamma_2<0;\qquad f_\nu\ \text{of one sign}\iff g_1g_2\,(\mu_1^{-1}+\mu_2^{-1})>0. \qquad\text{(6.3)}
```
In the second case of (6.3) the bound level is made of bodies near $`p_i=0`$; otherwise of bodies near $`p_i=\pm\pi/2`$ ($`f_\nu`$ alternates). For $`\sigma_1=\sigma_2=+1`$ it is the lowest level with $`\gamma_1\gamma_2>0`$; for $`\sigma_1=\sigma_2=-1`$ the highest level with $`\gamma_1\gamma_2<0`$, where the relative motion has negative inertia ($`\mu_1^{-1}+\mu_2^{-1}<0`$). With uniform hopping and the ring flux dropped (B1), the gauge leaves the magnitude $`\lvert\bar t(P)\rvert=(\bar\kappa_1^2+\bar\kappa_2^2+2\bar\kappa_1\bar\kappa_2\cos2P)^{1/2}`$, and with $`E_i(0)=E_i^{(0)}+\bar d_i+2\bar\kappa_i`$:
```math
E_b(P)=E_1(0)+E_2(0)-E_\varnothing+M(0)-2\bar t_0+s_e\Big[-2\lvert\bar t(P)\rvert+a_\nu\big(4\lvert\bar t(P)\rvert F^2\big)^{1/3}\Big],\qquad s_e:={\rm sgn}(g_1g_2), \qquad\text{(6.4)}
```
for $`F\ll\lvert\bar t(P)\rvert`$ (weak binding), up to relative corrections $`O(\chi^{2/3})`$ and $`O(\xi_\nu/L)`$: the continuum limit of the chain of step 2, $`-4\tau_hf''+F\lvert r\rvert f=(\epsilon+2\tau_h)f`$, has the Airy levels $`a_0=1.0188`$ (first zero of $`{\rm Ai}'`$), $`a_1=2.3381`$ (first zero of $`{\rm Ai}`$) in units $`(4\tau_hF^2)^{1/3}`$. Outside weak binding $`E_b(P)`$ is the extreme eigenvalue of (6.1).

### Step 3. Curvature of the bound level (item 2)

Let $`f_\nu`$ be the real normalized eigenvector of $`h_0`$ for $`E_b(0)`$ and
```math
b_\nu(\rho):=f_\nu(\rho-1)f_\nu(\rho+1),\qquad\beta_\nu:=\sum_\rho b_\nu(\rho),\qquad m(\rho):=-\frac1{8\kappa_1(\rho)}-\frac1{8\kappa_2(\rho)}. \qquad\text{(6.5)}
```
By Cauchy–Schwarz $`\lvert\beta_\nu\rvert\le1`$, with equality only if $`f_\nu(r+2)=\pm f_\nu(r)`$ for all $`r`$, excluded by B1: $`\lvert\beta_\nu\rvert<1`$.
1. Gauge $`g(r)\to e^{i\theta(r)}g(r)`$ removes the phases of all bonds of the ring of (6.1) except their sum $`\tilde\Phi(P):=\sum_\rho\arg t(\rho;P)-\sum_\rho\arg t(\rho;0)`$, put on one bond; the bond magnitudes become $`s_\rho(P):={\rm sgn}\,t(\rho;0)\,\lvert t(\rho;P)\rvert`$, real. So $`E_b(P)=\epsilon_\nu(\{s_\rho(P)\},\tilde\Phi(P))`$.
2. $`\lvert t(\rho;P)\rvert^2=t(\rho;0)^2-4\kappa_1\kappa_2\sin^2P`$ is even in $`P`$: $`s_\rho'(0)=0`$, $`s_\rho''(0)=-4\kappa_1(\rho)\kappa_2(\rho)/t(\rho;0)`$ (B2: $`t(\rho;0)\neq0`$). $`\tilde\Phi`$ is odd in $`P`$ with $`\tilde\Phi'(0)=\sum_\rho{\rm Im}\,\partial_P\ln t=-2\sum_\rho\kappa_1/(\kappa_1+\kappa_2)`$. $`\epsilon_\nu`$ is even in $`\tilde\Phi`$ (complex conjugation).
3. Hellmann–Feynman: $`\partial\epsilon_\nu/\partial s_\rho=2b_\nu(\rho)`$. Hence, exactly for the band contract,
```math
E_b''(0)=\sum_\rho\frac{b_\nu(\rho)}{m(\rho)}+\tilde\Phi'(0)^2\,\partial_{\tilde\Phi}^2\epsilon_\nu,\qquad\tilde\Phi'(0)\simeq-\frac{L\mu_2}{\mu_1+\mu_2}. \qquad\text{(6.6)}
```
The second term (*ring term*) needs the amplitude of $`f_\nu`$ around the ring: $`\partial^2_{\tilde\Phi}\epsilon_\nu`$ is exponentially small in $`L/\xi_\nu`$, the term vanishes as $`L\to\infty`$, and it depends on the continuation (body 2 as representative replaces $`\mu_2`$ by $`\mu_1`$). The first term is the inverse inertia of the bound level on the line. If $`\kappa_i(\rho)=\bar\kappa_i`$, $`m=\mu_1+\mu_2`$ and, on the line, $`1/E_b''(0)=(\mu_1+\mu_2)/\beta_\nu`$. The order-$`\tau^4`$ terms dropped by R2 change $`E_b''`$ by $`O(\tau'^4/(\delta_1^2\delta))`$, relative $`O(\tau'^2/(\beta_\nu\delta_1\delta))`$: small by B3.

### Step 4. Local inertia and the difference from $`\mu_1+\mu_2`$ (item 2)

$`m(\rho)=m_1(\rho)+m_2(\rho)`$, $`m_i(\rho):=-1/(8\kappa_i(\rho))`$: by (2.11), $`m_i`$ is the inertia $`b_i`$ would have with the amplitude it has at distance $`\rho`$ from the other body. By (2.16), $`m_1=\mu_1(1\pm\sigma_1\bar M^{(2)}(\rho)/M_1+O(\varepsilon^3))`$, and by (2.14) $`\mu_1\sigma_1/M_1=(R_1/M_1)/c_1^2\,(1+O(\gamma_1^2))=c_1^{-2}(1+O(\varepsilon))`$; the same for $`b_2`$. With $`\bar M^{(2)}(\rho):=\tfrac14[M^{(2)}(\rho-1)+2M^{(2)}(\rho)+M^{(2)}(\rho+1)]`$:
```math
m(\rho)=\mu_1+\mu_2+s_c\,\bar M^{(2)}(\rho)\Big(\frac1{c_1^2}+\frac1{c_2^2}\Big)+O\big(\varepsilon^3(\lvert\mu_1\rvert+\lvert\mu_2\rvert)\big). \qquad\text{(6.7)}
```
Each body's local inertia contains the second-order mutual term divided by the square of its own speed: once per body, with the sign $`s_c`$. Insert (6.7) into the first term of (6.6), $`1/m=(\mu_1+\mu_2)^{-1}(1-\eta)+O(\eta^2)`$ with $`\eta=O(\varepsilon^2)`$, and invert:
```math
D_\nu:=\frac1{E_b''(0)}-\mu_1-\mu_2=\underbrace{(\mu_1+\mu_2)\frac{1-\beta_\nu}{\beta_\nu}}_{D^{\rm lat}_\nu}+\underbrace{\frac{s_c}{\beta_\nu^2}\Big(\frac1{c_1^2}+\frac1{c_2^2}\Big)\sum_\rho b_\nu(\rho)\bar M^{(2)}(\rho)}_{D^{\rm mark}_\nu}+O\Big(\frac{\varepsilon^3(\lvert\mu_1\rvert+\lvert\mu_2\rvert)}{\beta_\nu^2}\Big), \qquad\text{(6.8)}
```
on the line (ring term of (6.6) dropped), $`\beta_\nu`$ and $`b_\nu`$ of the full band chain. $`D^{\rm lat}_\nu`$ is of order zero in $`\varepsilon`$ at fixed $`\chi`$ and nonzero for every bound level ($`\lvert\beta_\nu\rvert<1`$); for $`0<\beta_\nu<1`$ it has the sign of $`\mu_1+\mu_2`$. It comes from $`K_1+K_2`$: the $`P`$-dependence of the relative hopping $`\lvert t(\rho;P)\rvert`$, i.e. from the form $`\cos2p`$ of each body's band (2.11), together with $`W`$, which localizes $`f_\nu`$. $`D^{\rm mark}_\nu`$ is of order $`\varepsilon^2`$ and comes from the dependence of $`K_i`$ on the other body's mark (2.16). $`D_\nu`$ is the leading difference; $`D^{\rm lat}_\nu`$ dominates when $`1-\beta_\nu\gg\lvert M^{(2)}(0)\rvert/R_i`$. *Level dependence:* through $`\beta_\nu`$; in weak binding (Step 7) $`1-\beta_\nu\simeq\frac{a_\nu}6(4\chi^2)^{1/3}`$, larger for higher relative levels. *Control:* none in the class ($`\lvert\beta_\nu\rvert<1`$); in the wider class of unbound pairs on the line, $`\chi\to0`$ gives $`\beta_0\to1`$ and $`D_0\to0`$.

### Step 5. Inertia against cost (item 3)

As in (4.2), the cost of the bound pair is $`\Delta E_\nu:=E_b(0)-E_1(0)-E_2(0)+E_\varnothing`$: eigenvalues of the total contracts of four descriptions (pair, $`b_1`$ alone, $`b_2`$ alone, field alone), so no split of contract terms enters (M6). With $`E_b(0)=\langle f_\nu\vert h_0\vert f_\nu\rangle=\sum_rf_\nu^2U+2\sum_\rho b_\nu\,t(\rho;0)`$ and Step 1,
```math
\Delta E_\nu=\langle M\rangle_\nu+K_\nu+O(\varepsilon^2\lvert\bar\kappa\rvert),\qquad K_\nu:=2\bar t_0(\beta_\nu-1),\qquad\langle M\rangle_\nu=\sum_rf_\nu(r)^2M(r)=M(0)+\langle V\rangle_\nu+O\big(n\lvert g_1g_2\rvert\ell_0\eta/t_f\big). \qquad\text{(6.9)}
```
$`K_\nu`$ is the kinetic cost of the relative motion. Since $`\mu_1+\mu_2=-\bar t_0/(8\bar\kappa_1\bar\kappa_2)`$ and $`\mu_1\mu_2=1/(64\bar\kappa_1\bar\kappa_2)`$, $`D^{\rm lat}_\nu=4\mu_1\mu_2K_\nu/\beta_\nu`$, and splitting $`\bar M^{(2)}=M(0)+\bar V`$ in (6.8):
```math
D_\nu=\frac{4\mu_1\mu_2}{\beta_\nu}K_\nu+\frac{s_c}{\beta_\nu}\Big(\frac1{c_1^2}+\frac1{c_2^2}\Big)M(0)+\frac{s_c}{\beta_\nu^2}\Big(\frac1{c_1^2}+\frac1{c_2^2}\Big)\sum_\rho b_\nu\bar V,\qquad\frac{\Delta E_\nu}{c^2}=\frac{K_\nu+M(0)+\langle V\rangle_\nu}{c^2}. \qquad\text{(6.10)}
```
At fixed $`n,g_i,t_f,\tau_i,M_i`$ the contact value $`M(0)=-\frac{ng_1g_2}{t_f}\frac{L^2-1}{6L}`$ grows like $`L`$, while $`K_\nu`$, $`\beta_\nu`$, $`b_\nu`$, $`\langle V\rangle_\nu`$ change only by $`O(\xi_\nu/L)`$ (B1). *Equal speeds* $`c_1=c_2=c`$ (named condition): $`D_\nu=\Delta E_\nu/c^2`$ for all $`L`$ would need the coefficients of $`M(0)`$ to agree, $`2s_c/\beta_\nu=1`$, impossible since $`\lvert\beta_\nu\rvert<1`$; the coefficients of $`K_\nu`$ differ as well, $`4\mu_1\mu_2c^2/\beta_\nu=4\sigma_1\sigma_2R_1R_2/(\beta_\nu c^2)`$, of size $`(R/c)^2\gg1`$ by R1. For $`\sigma_1=\sigma_2`$, $`f_\nu`$ of one sign and $`1-\beta_\nu\gg\lvert M(0)\rvert/R_i`$, $`D_\nu\simeq D^{\rm lat}_\nu`$ has the sign of $`\mu_1+\mu_2`$ while $`\Delta E_\nu\simeq M(0)`$ has the opposite sign when $`\langle\lvert r\rvert\rangle_\nu\ll L/6`$: the pair has more inertia and less cost than its parts ($`\sigma_i=+1`$). *Unequal speeds:* a single $`c`$ would need $`c^{-2}=4\mu_1\mu_2/\beta_\nu`$ and $`c^{-2}=s_c(c_1^{-2}+c_2^{-2})/\beta_\nu`$, incompatible since the first is larger by $`\sim R_1R_2/c^2`$; in particular neither $`c_1`$ nor $`c_2`$ works. *Control:* none in the class.

### Step 6. Weight of the bound level and fall (item 4)

A held source $`g_s\Phi_{x_s}`$ changes the $`\tau=0`$ levels of $`\mathcal G`$ by the held-pair weight $`W_{\rm pair}(j,l)`$ at first order in $`g_s`$, and the $`K_i`$ at relative order $`\gamma_ig_s/t_f`$ (through the field states, as in (2.16)), which enters the fall at $`O(\tau^4\gamma g_s)`$ as in (7.7). Project on the bound level (distance of the source $`d_s\gg\xi_\nu`$, source terms small against the spacing of relative levels): states $`\sum_X\varphi_X\sum_rf_\nu(r)e_{X-r/2,X+r/2}`$, $`X=(j+l)/2`$, with center contract $`E_b(\hat P)+W_\nu(\hat X)+O(g_s^2)`$, where the weight of the bound level is
```math
W_\nu(X):=\sum_rf_\nu(r)^2\,W_{\rm pair}\big(X-\tfrac r2,X+\tfrac r2\big). \qquad\text{(6.11)}
```
$`W_b`$ vanishes for $`g_1=0`$ and for $`g_2=0`$, hence is $`O(g_1g_2g_s)`$; by (4.5), $`W_{\rm pair}=ng_1\phi(x_1)+ng_2\phi(x_2)+O(\varepsilon^2g_s)`$. $`\phi`$ is quadratic on each arc between images of $`x_s`$ ($`\phi''=-2g_s/(t_fL)`$), and $`\sum_rf_\nu^2\,r=0`$ ($`f_\nu^2`$ even by the reflection of Step 1). Hence, for pair positions not reaching $`x_s`$,
```math
W_\nu(X+1)-W_\nu(X-1)=n(g_1+g_2)\,[\phi(X+1)-\phi(X-1)]+O(\varepsilon^2g_s)+O(e^{-d_s/\xi_\nu}): \qquad\text{(6.12)}
```
at leading order the weight difference of the bound level is that of its members, for every level $`\nu`$. With $`E_b(P)=\sum_s\epsilon_se^{isP}`$, $`[\mathcal T_s,\hat X]=-s\mathcal T_s`$ and $`\ddot{\langle\hat X\rangle}=-\langle[H,[H,\hat X]]\rangle`$, a start with real envelope $`\varphi_X`$ in the bound band has
```math
a_\nu(0)=\sum_ss\,\epsilon_s\sum_X\varphi_{X+s}\varphi_X\,[W_\nu(X+s)-W_\nu(X)]=-E_b''(0)\sum_X\varphi_X^2W'_\nu(X)\,\big[1+O(w^{-2})\big]+O(g_s^2)+O(\tau^4\gamma g_s), \qquad\text{(6.13)}
```
$`W'_\nu(X):=\tfrac12[W_\nu(X+1)-W_\nu(X-1)]`$, $`w`$ the width of $`\varphi`$ against the range of the $`\epsilon_s`$. For one body ($`\epsilon_{\pm2}=\bar\kappa`$ only) the middle form is (7.7); so (7.7) carries over to the bound level with $`E''\to E_b''(0)`$, $`W'\to W'_\nu`$, for broad envelopes. The fall factor is $`\Pi_\nu:=E_b''(0)W'_\nu`$, and for $`b_i`$ alone $`\Pi_i:=E_i''(0)W_i'=ng_i\phi'/\mu_i=n\gamma_ic_i^2\phi'\,(1+O(\varepsilon))`$ by (4.5), (2.14). With (6.6)–(6.8) (line) and (6.12):
```math
\Pi_\nu=\beta_\nu\,\frac{\mu_1\Pi_1+\mu_2\Pi_2}{\mu_1+\mu_2}\,\big[1+O(\varepsilon)\big];\qquad\text{if }\gamma_1c_1^2=\gamma_2c_2^2:\quad\Pi_\nu-\Pi_1=-(1-\beta_\nu)\,\Pi_1+O(\varepsilon\,\Pi_1). \qquad\text{(6.14)}
```
The single bodies have equal fall factors only under the named condition $`\gamma_1c_1^2=\gamma_2c_2^2`$ (M7). Even then the bound pair differs at leading order (order zero in $`\varepsilon`$ at fixed $`\chi`$) by the factor $`\beta_\nu`$: it falls slower for $`0<\beta_\nu<1`$. The $`O(\varepsilon)`$ corrections come from the second-order weights ((4.5), $`W_b`$ of (4.7)) and from $`D^{\rm mark}`$. *Control:* none in the class; unbound pairs on the line ($`\chi\to0`$) give $`\beta_0\to1`$ and equality under the condition.

### Step 7. Dependence on $`t_f`$ (item 5)

At fixed $`n,\gamma_i,M_i,\tau_i`$: $`R_i`$, $`\mu_i`$, $`c_i`$, $`\bar\kappa_i`$, $`\bar t_0`$ do not depend on $`t_f`$ at the orders used; $`M^{(2)}`$, $`F`$ and $`\eta`$ scale as $`1/t_f`$; $`\phi\propto g_s/t_f`$. The field gap of R1 is $`\delta\simeq4\pi^2t_f/L^2`$. For $`\sigma_i=+1`$ the levels reached by flipping $`b_i`$ include an excited field up to $`4N_ft_f`$ above its lowest state, so R1 needs $`4N_ft_f<2M_i-\delta_1`$; for $`\sigma_i=-1`$, $`\delta_1\simeq2M_i`$. With the weak-binding $`\beta_0=1-\frac{a_0}6(4\chi^2)^{1/3}`$ from $`\partial\epsilon_0/\partial\tau_h=-2\beta_0`$ applied to (6.4):
```math
\chi=\frac{n\lvert g_1g_2\rvert}{t_f\lvert\bar t_0\rvert}\propto\frac1{t_f},\quad1-\beta_0\simeq0.270\,\chi^{2/3}\propto t_f^{-2/3},\quad\frac{\tau'^2L^2}{4\pi^2\delta_1}\ll t_f\ll\frac{n\lvert g_1g_2\rvert L^3}{\lvert\bar t_0\rvert},\quad t_f<\frac{2M_i-\delta_1}{4N_f}\ (\sigma_i=+1). \qquad\text{(6.15)}
```
Hence: (6.3) does not depend on $`t_f`$, but B1 holds only below the upper bound in (6.15), with $`\xi_0\propto t_f^{1/3}`$. $`D^{\rm lat}_\nu`$ and $`1-\Pi_\nu/\Pi_1`$ fall as $`t_f^{-2/3}`$, $`D^{\rm mark}_\nu`$ and $`M(0)`$ as $`1/t_f`$. The coefficient mismatches of Step 5 ($`2s_c/\beta_\nu`$ against 1) and the factor $`\beta_\nu`$ of (6.14) do not vanish at any $`t_f`$ inside the window, since $`\lvert\beta_\nu\rvert<1`$ there. A faster field (larger $`t_f`$) weakens the binding and brings the pair's inertia and fall towards those of its parts; the limit is reached only where the pair stops being bound on the ring.

## Result

- **(6.1)** Class above, order $`\tau^2`$: in the sector $`P`$ (body 1 as representative, continued to real $`P`$) the band contract is the relative chain $`h_P`$ with bond amplitudes $`t(\rho;P)=\kappa_1(\rho)e^{-2iP}+\kappa_2(\rho)`$ and separate rings for $`r`$ even and odd.
- **(6.2)** Leading order in $`\varepsilon`$: $`M^{(2)}(r)=-2ng_1g_2\ell(r)/t_f`$ and the relative potential $`V(r)=\frac{ng_1g_2}{t_fL}r(L-r)`$, a well at contact for $`g_1g_2>0`$ and a hill for $`g_1g_2<0`$.
- **(6.3)** Under R and B, every branch combination and both signs of $`\gamma_1\gamma_2`$: bound levels exist; they are the lowest levels of relative motion if $`\sigma_1\sigma_2\gamma_1\gamma_2>0`$ and the highest if $`<0`$. They are made of bodies near rest iff $`g_1g_2(\mu_1^{-1}+\mu_2^{-1})>0`$; e.g. $`\sigma_i=+1`$ with $`\gamma_1\gamma_2>0`$ (lowest), or $`\sigma_i=-1`$ with $`\gamma_1\gamma_2<0`$ (highest, negative relative inertia).
- **(6.4)** Leading order in $`\varepsilon`$, uniform hopping, weak binding $`F\ll\lvert\bar t(P)\rvert`$, up to $`O(\chi^{2/3})`$ and $`O(\xi_\nu/L)`$: $`E_b(P)=E_1(0)+E_2(0)-E_\varnothing+M(0)-2\bar t_0+s_e[-2\lvert\bar t(P)\rvert+a_\nu(4\lvert\bar t(P)\rvert F^2)^{1/3}]`$, with $`a_0=1.0188`$, $`a_1=2.3381`$.
- **(6.5)** Definitions: bond weights $`b_\nu`$, bond overlap $`\beta_\nu`$ with $`\lvert\beta_\nu\rvert<1`$ for every bound level, local pair inertia $`m(\rho)`$.
- **(6.6)** Exact for the band contract (order $`\tau^2`$, B2): $`E_b''(0)=\sum_\rho b_\nu(\rho)/m(\rho)`$ plus a ring term that depends on the continuation and is exponentially small in $`L/\xi_\nu`$ (times $`L^2`$).
- **(6.7)** Order $`\varepsilon^2`$, error $`O(\varepsilon^3)`$: $`m(\rho)=\mu_1+\mu_2+s_c\bar M^{(2)}(\rho)(c_1^{-2}+c_2^{-2})`$; the mutual term enters each body's inertia once, over its own speed squared, with sign $`+`$ for (a) and $`-`$ for (c).
- **(6.8)** On the line, through order $`\varepsilon^2`$: $`1/E_b''(0)-\mu_1-\mu_2=D^{\rm lat}_\nu+D^{\rm mark}_\nu`$. The leading part $`D^{\rm lat}_\nu=(\mu_1+\mu_2)(1-\beta_\nu)/\beta_\nu`$, from the $`P`$-dependence of $`K_1+K_2`$ with the binding by $`W`$, is nonzero for every bound level and, in weak binding, grows with the level of relative motion. $`D^{\rm mark}_\nu=O(\varepsilon^2)`$ comes from the $`\rho`$-dependence of $`K_i`$. No description of the class has $`D^{\rm lat}_\nu=0`$; it vanishes only for unbound pairs ($`\beta_\nu\to1`$).
- **(6.9)** Order $`\tau^2`$, through $`\varepsilon^2`$: the cost of the bound pair is $`\Delta E_\nu=\langle M\rangle_\nu+K_\nu`$ with the kinetic cost $`K_\nu=2\bar t_0(\beta_\nu-1)`$.
- **(6.10)** Negative, leading order, both couplings: $`1/E_b''(0)-\mu_1-\mu_2=\Delta E_\nu/c^2`$ does not hold as an identity on the class. For equal speeds the coefficients of the contact value $`M(0)`$ differ ($`2s_c/\beta_\nu`$ against 1), and so do those of $`K_\nu`$ ($`4\mu_1\mu_2/\beta_\nu`$ against $`c^{-2}`$). For unequal speeds no single speed fits, neither $`c_1`$ nor $`c_2`$. For $`\sigma_1=\sigma_2`$, bodies near rest, $`\langle\lvert r\rvert\rangle_\nu\ll L/6`$ and $`1-\beta_\nu\gg\lvert M(0)\rvert/R_i`$, the difference of inertia and that of cost have opposite signs. No control in the class.
- **(6.11)** Definition: the weight of the bound level is the $`f_\nu^2`$-average of the held-pair weight, at first order in $`g_s`$.
- **(6.12)** First order in $`g_i`$ and $`g_s`$, source far from the pair: the weight difference of the bound level is that of its members, $`n(g_1+g_2)\Delta\phi`$, for every level.
- **(6.13)** (7.7) carries over to the bound level, with $`E_b''(0)`$ and $`W'_\nu`$, for envelopes broad against the range of the harmonics of $`E_b(P)`$, at first order in $`g_s`$, up to $`O(\tau^4\gamma g_s)`$.
- **(6.14)** Negative, leading order (order zero in $`\varepsilon`$ at fixed $`\chi`$), both couplings: $`\Pi_\nu=\beta_\nu(\mu_1\Pi_1+\mu_2\Pi_2)/(\mu_1+\mu_2)`$. Even under the named condition $`\gamma_1c_1^2=\gamma_2c_2^2`$ the bound level's fall factor is $`\beta_\nu\Pi_1\neq\Pi_1`$; the first order of the difference is $`-(1-\beta_\nu)\Pi_1`$, with corrections $`O(\varepsilon\Pi_1)`$. No control in the class.
- **(6.15)** Item 5, at fixed $`n,\gamma_i,M_i,\tau_i`$: $`\chi\propto1/t_f`$. The deviations of items 2 and 4 fall as $`t_f^{-2/3}`$ (weak binding) and the mark terms as $`1/t_f`$. B1 and R1 confine $`t_f`$ to the window of (6.15), with an upper bound $`t_f<(2M_i-\delta_1)/(4N_f)`$ for $`\sigma_i=+1`$. No $`t_f`$ inside the window removes the negatives (6.10), (6.14).

## Consistency checks

1. *Dimensions.* $`P`$ is dimensionless, so $`\mu_i`$, $`m`$, $`1/E_b''`$ have the dimension $`[C]^{-1}`$. So do $`\bar M^{(2)}/c_i^2`$ and $`\mu_1\mu_2K_\nu`$ ($`c_i^2\sim[C]^2`$), and $`\Pi_\nu,\Pi_i\sim[C]`$; $`\beta_\nu`$, $`\chi`$ are pure numbers. Passed.
2. *Unbound limit $`\chi\to0`$ on the line* (e.g. $`\gamma_2\to0`$): $`\beta_0=1-0.270\chi^{2/3}\to1`$ and $`M^{(2)}\to0`$, so $`1/E_b''(0)\to\mu_1+\mu_2`$. This agrees with minimizing $`E_1(p_1)+E_2(p_2)`$ at fixed $`p_1+p_2=P`$, whose curvature is $`-8\bar\kappa_1\bar\kappa_2/(\bar\kappa_1+\bar\kappa_2)=1/(\mu_1+\mu_2)`$. Passed.
3. *Tight binding $`\chi\to\infty`$.* Even class: $`f_0\simeq\delta_{r0}`$, $`\beta_0\simeq1/\chi`$, so $`E_b''(0)\simeq8\bar\kappa_1\bar\kappa_2/F`$. This agrees with direct second-order perturbation of the contact state, $`-\lvert\bar t(P)\rvert^2/F`$. Odd class: $`f_0\simeq(\delta_{r,1}\pm\delta_{r,-1})/\sqrt2`$, $`\beta_0\to\frac12`$, so $`1/E_b''(0)=2(\mu_1+\mu_2)`$. This agrees with the two-site level $`V(1)-\lvert\bar t(P)\rvert`$. Passed.

## Open issues

- At finite $`L`$ the curvature at $`P=0`$ depends on the continuation in $`P`$ through the ring term of (6.6); in the code it is 12% at $`L=12`$ and 3% at $`L=16`$ (set A). Only the line value is a property of the bound level.
- The closed forms (6.2), (6.4), (6.15) use $`M^{(2)}`$; at $`\eta\approx0.3`$ (code) the exact binding slope is about half of $`F`$. Statements in terms of $`\beta_\nu`$, $`b_\nu`$, $`M`$ are not affected.
- The $`O(\varepsilon^3)`$ remainder of (6.7) is large at moderate couplings (code: ratio 1.40 for (a), $`-0.19`$ for (c) at $`\eta\approx0.3`$), so $`D^{\rm mark}`$ is reliable only for small $`\eta`$.
- The $`O(\varepsilon)`$ correction of (6.14) from the second-order weights is not evaluated (the bond function $`B`$ of (4.7) is not quoted); in the code it is 13–16%.
- For the even class in tight binding, $`\beta_0\sim1/\chi`$ and B3 fails when $`\chi\gtrsim\delta_1\delta/\tau'^2`$; the order-$`\tau^4`$ band contract is then needed.
- R1 for $`\sigma_i=+1`$ bounds $`t_f`$ by $`(2M_i-\delta_1)/(4N_f)`$, restrictive for many field objects; whether weakly coupled resonances with multiply excited field states can be tolerated is open.
- Out of scope: full grip, tori, the highest field state, bodies of one type, the speed of a front of the field; how typical the structure is (item 5 of the base problem).

## Code

- `code/v1/check_inertia.py` (check). It treats $`N_f=1`$, $`t_f=1`$ and two parameter sets: A ($`\sigma_i=+1`$, $`M=(3,4)`$, $`\tau_1=\tau_2=0.2`$, $`\gamma=(0.09,0.07)`$, $`r`$ even, lowest level) and B ($`\sigma_i=-1`$, $`M=(2.5,2)`$, $`\tau=(0.16,0.2)`$, $`\gamma=(0.10,-0.14)`$, $`r`$ odd, highest level). For each set it runs $`L=12,16`$ and couplings (a), (c). It builds the exact sector contract of two bodies and the field object (body 1 as representative, continued in $`P`$) and finds the exact bound level by its weight on $`\mathcal G`$ (≥0.9996). It takes its curvature at $`P=0`$ by second-order perturbation in $`P`$ (cross-checked by finite differences), and builds the band contract by second-order Schrieffer–Wolff on the $`\tau=0`$ levels. Results: (6.6) with its ring term agrees with the exact curvature to $`\le0.16\%`$ in all eight cases (the rest is order $`\tau^4`$). The ring term is 12% ($`L=12`$) and 3% ($`L=16`$) for A, 6% and 0.7% for B. $`\beta_\nu=0.69`$–$`0.79`$; $`1/E_b''(0)`$ exceeds $`\mu_1+\mu_2`$ by 22–29%. $`D\,c_i^2/\Delta E\approx-500`$ to $`-575`$ (A, equal speeds) and $`-208`$ to $`-363`$ (B): negative and far from 1, as in (6.10). The ratio of the numerical $`m(\rho)-\mu_1-\mu_2`$ to (6.7) tends to 1 as the couplings are scaled down (1.04 for (a), 0.93 for (c) at scale 0.03). The script also prints $`\sigma_iR_i/(c_i^2\mu_i)=0.98`$–$`1.00`$, a check of (2.14). Outputs: `code/v1/output/inertia_check.txt`, `code/v1/output/inertia_check.json`.
- `code/v1/check_weight.py` (check). It takes set A, couplings (a), (c), $`L=16,20`$, with a held source $`g_s=-0.01`$ (and $`-0.005`$ at $`L=16`$), and computes the exact eigenvalues of the full contract near the bottom of the bound band (weight on $`\mathcal G`$ ≥0.9997), where the pair sits in the weight well opposite the source. It compares them with the reduced description $`E_b(\hat P)+W_\nu(\hat X)`$ of Step 6, using exact sector levels $`E_b(P_k)`$ and (6.11) with exact held weights. The main level spacing agrees to 0.03% ($`L=16`$) and 0.17% ($`L=20`$); the same description with the pair inertia set to $`\mu_1+\mu_2`$ misses it by 16% and 10%. Level deviations scale as $`g_s^2`$. The levels come in nearly degenerate pairs because $`E_b(P+\pi)=E_b(P)`$. $`E_b''(0)(\mu_1+\mu_2)=0.82`$ ($`L=16`$) and $`0.86`$ ($`L=20`$), against $`\beta_0=0.79`$ and $`0.85`$; the difference is the ring term. The ratio $`\Delta W_\nu/(\Delta W_1+\Delta W_2)`$ is 0.87 at these couplings and tends to 1 as they are scaled down (0.997 at scale 0.03), as in (6.12). Outputs: `code/v1/output/weight_check.txt`, `code/v1/output/weight_check.json`.

## Methods used

- band contract (second-order Schrieffer–Wolff), plane-wave sectors of the joint translation
- gauge reduction of a chain to bond magnitudes and one flux; Hellmann–Feynman theorem
- Perron–Frobenius; Cauchy–Schwarz
- second-order perturbation theory; Airy functions (continuum limit of a linear potential)
- band projection, double commutator for the acceleration from rest
- exact diagonalization (dense and shift-invert sparse) for the code checks
