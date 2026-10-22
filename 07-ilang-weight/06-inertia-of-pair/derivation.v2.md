# Inertia of a pair bound through the field

- **Subproject:** 07-ilang-weight
- **Package:** 06-inertia-of-pair
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-21

## Changes from previous version

- Setup: signs $`s_\mu`$, $`s_\beta`$ and speeds $`c_{\min},c_{\max}`$ introduced; binding regime B extended by B4 (ring hierarchy). Reason: I2, I5.
- Step 2: the one-sign statement of (6.3) restricted to the extreme level; alternating extreme levels and excited levels (nodes) stated separately; $`a_\nu`$ for all levels. Reason: I2.
- Step 3: ring remainder $`\rho_L`$ defined and bounded, new (6.16); accuracy of the independence of the continuation stated. Reason: I5.
- Step 4: (6.8) with the ring remainder and signed $`\beta_\nu`$; level dependence for weakly bound and excited levels; unbound limit corrected for $`s_\beta=-1`$. Reason: I2, I5.
- Step 5: (6.10) restricted to the failure of a universal identity; new (6.17): sign rule that excludes or allows individual equalities, a family inside R and B with an equality, level dependence of a fitted ratio. The all-$`L`$ argument and the opposite-sign remark of v1 are removed. Reason: I4.
- Step 6: source projected with the $`P`$-dependent bound eigenvectors; new (6.18), the centre conjugate to $`P`$; (6.13) rederived from the double commutator with its errors; (6.14) with $`E''_{\rm line}`$ and signed $`\beta_\nu`$. Reason: I3, I2, I5.
- Step 7: R1 window from the held-sector spectra; $`4N_ft_f`$ bound only sufficient; $`\delta`$ the minimal spectral distance; $`s_\beta`$ in (6.15). Reason: I1, I2.
- Consistency checks: dimension of $`\Pi`$ corrected; checks 2 and 3 with $`s_\beta`$, $`s_e`$. Reason: I6, I2.
- Code: set A has exactly equal speeds also for (c); set C (alternating extreme level) added; new checks of (6.16), of the R1 gaps, of (6.17) on a line chain, of the projected contract with $`P`$-dependent eigenvectors and of (6.13). Reason: I7, I1–I5.

## Response to verification

- **I1:** Accepted and fixed in Step 7. R1 is stated through the distances between the held-sector spectra. $`4N_ft_f\le2R_i-\delta_1`$ is one of two sufficient conditions; the excluded $`t_f`$ are resonance intervals, listed for $`N_f=1`$. $`\delta`$ is the minimal spectral distance, not the field gap. Code: R1 holds at $`t_f=40`$, $`L=12`$ ($`\delta_1=2.6`$) and fails by resonance at $`L=16`$.
- **I2:** Accepted and fixed in Steps 2, 4, 6, 7 and checks 2, 3. $`s_\beta`$ is kept in all weak-binding and limiting formulas, and the one-sign property is claimed only for the extreme level with $`s_\beta=+1`$. Alternating extreme levels ($`\beta_0\to-1`$, inertia $`\to-(\mu_1+\mu_2)`$) and excited levels (sign change of $`\beta_\nu`$) are treated separately. Code: set C.
- **I3:** Accepted and fixed in Step 6. The source is projected with $`f_{\nu,P}=e^{i\theta_P}F_{\nu,P}`$, and $`P`$ is conjugate to the centre (6.18). The narrow-momentum error is $`O(w^{-2})`$, and the shift by $`\theta'`$ leaves the weight differences unchanged up to $`O(\varepsilon^2g_s)`$. (6.13) follows from the double commutator, interband terms included. Code: the projected contract reproduces the doublet splittings, while the frozen profile reproduces only the main spacing; (6.13) is tested directly.
- **I4:** Accepted and fixed in Step 5. (6.10) states only the failure of a universal identity. (6.17) proves exclusion for $`s_c=-\sigma_1\sigma_2s_\beta`$. For $`s_c=\sigma_1\sigma_2s_\beta`$ it gives a codimension-one set of equalities, including a family inside R and B, valid for one level at a time. The uncontrolled all-$`L`$ argument is removed.
- **I5:** Accepted and fixed in the Setup (B4), Step 3 ((6.16)) and Steps 4–6. The ring remainder enters (6.8) and (6.10), and B4 requires it to be smaller than every retained term. The curvature is independent of the continuation to relative accuracy $`\lvert\rho_L\rvert`$. The code sets do not meet B4 for the mark terms; this is stated.
- **I6:** Accepted and fixed in consistency check 1: $`\Pi_\nu,\Pi_i\sim[C]^2`$.
- **I7:** Accepted and fixed in the code: for (c), $`\tau_2=\tau_1(1+\gamma_1n)/(1+\gamma_2n)`$, so set A has $`c_1=c_2`$ for both couplings.

## Setup and assumptions

**Setting (assumptions, M8, M9).** As in question.md: $`N_f\ge1`$ field objects ($`c=+1`$) on a ring of even $`L\ge6`$ places with own term $`C_1=-t_f\sum_x(\lvert x\rangle\langle x+1\rvert+{\rm h.c.})`$, $`\Phi_x`$ the number at $`x`$, $`n=N_f/L`$; two Model D bodies $`b_1,b_2`$ of different types, clock levels $`k_i`$ with half-gaps $`M_i`$, branches $`\sigma_i`$, coupled by (a) or (c) with constants $`\gamma_i`$, $`g_i:=\sigma_i\gamma_iM_i`$, no pair term between them, records at $`\kappa\to0`$; the field in its lowest state adapted to the bodies; regime R (R1, R2) as stated there. Order counting: $`\varepsilon:=\max_i\lvert\gamma_i\rvert`$ ($`g_i=O(\varepsilon)`$). Speeds of (2.14): $`c_i=\tau_i`$ (a), $`c_i=\tau_i(1+\gamma_in)`$ (c); $`s_c:=+1`$ (a), $`-1`$ (c).

**Inputs** (verbatim in question.md). From 07-ilang-weight/02-two-free-bodies: the joint translation $`\mathcal T=e^{-i\hat P}`$, $`[\mathcal T,C]=0`$ (2.1); $`E(x_1,x_2)=\sigma_1M_1+\sigma_2M_2+N_f\varepsilon_0(x_1,x_2)`$ (2.3); the band contract $`H_{\rm eff}=W+K_1+K_2+O(\tau^4)`$, $`W={\rm diag}\,E(j,l)`$ (2.10), $`K_i`$ moving $`b_i`$ by $`0,\pm2`$; $`E''_{k_1,\sigma_1}(0)=-8\bar\kappa`$ (2.11), hence $`\mu_i=-1/(8\bar\kappa_i)`$; $`\mu_i=\sigma_iR_i/c_i^2+O(\gamma_i^2)`$ with $`R_i=M_i(1+\gamma_in)+O(\gamma_i^3)`$ (2.14); $`\delta\kappa(j,l)/\bar\kappa=\mp\gamma_1\overline{\delta\rho}_l(j)+r_1`$, $`\gamma_1\delta\rho_l(y)=\sigma_1M^{(2)}(y,l)/M_1+O(\gamma_1g_2^2)`$, $`r_1=O(\varepsilon^3)`$ (2.16), upper sign (a). From 06-ilang-source/04-profile: $`M=N_f[\varepsilon_0(g_1,g_2)-\varepsilon_0(g_1,0)-\varepsilon_0(0,g_2)+\varepsilon_0(0,0)]`$ (4.2). From 06-ilang-source/07-dressed-fall: $`a_{k,\sigma}(0)=-E''_{k,\sigma}(0)\sum_j\phi_{j+1}\phi_{j-1}W'_{k,\sigma}(j)+O(g_s^2)+O(\tau^4\gamma g_s)`$ (7.7). From 07-ilang-weight/04-weight-of-bond: $`\ell(r)=\frac{L^2-1}{12L}-\frac{r(L-r)}{2L}`$ and $`E(r)-E(r')=\frac{ng_1g_2}{t_fL}[r(L-r)-r'(L-r')]+O(n\lvert g_1g_2\rvert\ell_0\eta/t_f)`$ (4.3); $`W_i(x)=ng_i\phi(x)+O(\varepsilon^2g_s)`$ with $`\phi(x)=-\frac{2g_s}{t_f}\ell(x-x_s)`$ (4.5); $`W_{\rm pair}=W_1(x_1)+W_2(x_2)+W_b`$ with $`W_b`$ (4.7).

**Notation.** $`\bar t_0:=\bar\kappa_1+\bar\kappa_2=-\tfrac18(\mu_1^{-1}+\mu_2^{-1})`$; $`F:=n\lvert g_1g_2\rvert/t_f`$; binding ratio $`\chi:=F/\lvert\bar t_0\rvert`$; signs $`s_e:={\rm sgn}(g_1g_2)`$, $`s_\mu:={\rm sgn}(\mu_1^{-1}+\mu_2^{-1})=-{\rm sgn}\,\bar t_0`$, $`s_\beta:=s_es_\mu`$; $`c_{\min}`$, $`c_{\max}`$ the smaller and the larger of $`c_1,c_2`$; $`E_i(P)`$ the band level of $`b_i`$ alone with the field, $`E_\varnothing`$ the lowest eigenvalue of the field alone.

**Binding regime B (assumption).** B1: the relative level $`\nu`$ considered decays on a scale $`\xi_\nu\ll L`$ (for the extreme level: $`\chi L^3\gg1`$; $`\xi_0\simeq(4/\chi)^{1/3}`$ for $`\chi\lesssim1`$, $`\xi_0\simeq1`$ for $`\chi\gtrsim1`$). B2: $`\lvert\bar t_0\rvert\gg\varepsilon^2\max_i\lvert\bar\kappa_i\rvert`$ (the relative hopping does not cancel). B3: $`\lvert\beta_\nu\rvert\gg\tau'^2/(\delta_1\delta)`$ with $`\beta_\nu`$ of (6.5), so that the order-$`\tau^4`$ terms dropped by R2 stay small (Step 3). B4 (ring hierarchy): the ring remainder $`\rho_L`$ of (6.16) is small against every retained relative term, $`\lvert\rho_L\rvert\ll1-\lvert\beta_\nu\rvert`$ for the leading statements and $`\lvert\rho_L\rvert\ll\lvert M^{(2)}(0)\rvert/R_i`$ where the mark terms are kept.

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
$`V`$ is even, monotone in $`\lvert r\rvert`$ on $`[0,L/2]`$, rises like $`F\lvert r\rvert`$ near $`r=0`$ for $`g_1g_2>0`$ (well) and falls like $`-F\lvert r\rvert`$ for $`g_1g_2<0`$ (hill). *Criterion of localization:* the real eigenvector $`f_\nu`$ of $`h_0`$ decays away from $`r=0`$ on a scale $`\xi_\nu\ll L`$, so that its weight near $`r=L/2`$ is exponentially small in $`L/\xi_\nu`$ (B1). On a chain the sign of the hopping is a gauge ($`f(r)\to(-1)^{r/2}f(r)`$; on the ring up to terms exponentially small by B1), so the edges of the spectrum of $`h_0`$ depend on $`\lvert\bar t_0\rvert`$ and $`V`$ only; a well binds levels below the uniform band $`2\bar t_0\cos2k`$, a hill above it (standard for one-dimensional chains), and the level near the opposite extremum $`r=L/2`$ fails the criterion. On each sublattice chain, Perron–Frobenius applied to $`\mp h_0`$ fixes the *extreme* eigenvector: $`f_0(r+2)/f_0(r)`$ has one sign, positive if the bonds $`t(\rho;0)`$ (sign of $`\bar t_0`$ by B2) put that edge at $`k=0`$, negative otherwise. The excited levels $`\nu\ge1`$ of the same chain have $`\nu`$ sign changes of their envelope (Sturm oscillation). With $`g_1g_2=\sigma_1\sigma_2\gamma_1\gamma_2M_1M_2`$:
```math
\text{bound levels: the lowest if }\sigma_1\sigma_2\gamma_1\gamma_2>0,\ \text{the highest if }<0;\qquad\text{extreme level: }f_0\ \text{of one sign if }s_\beta=+1,\quad f_0(r)f_0(r+2)<0\ \text{if }s_\beta=-1. \qquad\text{(6.3)}
```
For $`s_\beta=+1`$ the extreme level is made of bodies near $`p_i=0`$; for $`s_\beta=-1`$ of bodies near $`p_1=-p_2=\pm\pi/2`$, where each band (2.11) has the inertia $`-\mu_i`$. Examples: $`\sigma_i=+1`$ gives the lowest level, of one sign, for $`\gamma_1\gamma_2>0`$ and the highest, alternating, for $`\gamma_1\gamma_2<0`$; $`\sigma_i=-1`$ gives the highest level, of one sign and with negative relative inertia, for $`\gamma_1\gamma_2<0`$. With uniform hopping and the ring flux dropped (B1), the gauge leaves the magnitude $`\lvert\bar t(P)\rvert=(\bar\kappa_1^2+\bar\kappa_2^2+2\bar\kappa_1\bar\kappa_2\cos2P)^{1/2}`$, and with $`E_i(0)=E_i^{(0)}+\bar d_i+2\bar\kappa_i`$:
```math
E_b(P)=E_1(0)+E_2(0)-E_\varnothing+M(0)-2\bar t_0+s_e\Big[-2\lvert\bar t(P)\rvert+a_\nu\big(4\lvert\bar t(P)\rvert F^2\big)^{1/3}\Big],\qquad s_e:={\rm sgn}(g_1g_2), \qquad\text{(6.4)}
```
for $`F\ll\lvert\bar t(P)\rvert`$ (weak binding), up to relative corrections $`O(\chi^{2/3})`$ and $`O(\xi_\nu/L)`$: the continuum limit of the chain, $`-4\tau_hf''+F\lvert r\rvert f=(\epsilon+2\tau_h)f`$, has the levels $`a_\nu`$ in units $`(4\tau_hF^2)^{1/3}`$, $`a_\nu`$ the merged increasing sequence of the zeros of $`{\rm Ai}'`$ ($`\nu`$ even) and $`{\rm Ai}`$ ($`\nu`$ odd): $`a_0=1.0188`$, $`a_1=2.3381`$, $`a_2=3.2482`$. Outside weak binding $`E_b(P)`$ is an eigenvalue of (6.1).

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

The second term (*ring term*) is the only place where the continuation enters: body 2 as representative replaces $`\mu_2`$ by $`\mu_1`$ in $`\tilde\Phi'(0)`$. Write $`E''_{\rm line}:=\sum_\rho b_\nu/m`$ and $`E_b''(0)=E''_{\rm line}(1+\rho_L)`$. $`\partial^2_{\tilde\Phi}\epsilon_\nu`$ does not depend on which bond carries the flux; put it on the bond $`(r_*,r_*+2)`$ farthest from contact, with amplitude $`s_*`$. Second-order perturbation in $`\tilde\Phi`$ (first-order term $`-2s_*b_\nu(r_*+1)`$; matrix elements $`\lvert s_*\rvert\,\lvert f_{\nu'}(r_*)f_\nu(r_*+2)-f_{\nu'}(r_*+2)f_\nu(r_*)\rvert`$), Cauchy–Schwarz and $`\sum_{\nu'}f_{\nu'}(r)^2=1`$ give
```math
\lvert\rho_L\rvert\le\frac{\tilde\Phi'(0)^2}{\lvert E''_{\rm line}\rvert}\Big[2\lvert s_*b_\nu(r_*+1)\rvert+\frac{4s_*^2}{\Delta_\nu}\big(f_\nu(r_*)^2+f_\nu(r_*+2)^2\big)\Big], \qquad\text{(6.16)}
```
$`\Delta_\nu`$ the distance of $`\epsilon_\nu`$ from the other levels of $`h_0`$. By B1 the right side is exponentially small in $`L/\xi_\nu`$ (times $`L^2`$). Both continuations obey (6.16), so $`E_b''(0)`$ is independent of the continuation to relative accuracy $`\lvert\rho_L\rvert`$, which B4 makes smaller than every retained term. If $`\kappa_i(\rho)=\bar\kappa_i`$, $`m=\mu_1+\mu_2`$ and $`1/E''_{\rm line}=(\mu_1+\mu_2)/\beta_\nu`$. The order-$`\tau^4`$ terms dropped by R2 change $`E_b''`$ by $`O(\tau'^4/(\delta_1^2\delta))`$, relative $`O(\tau'^2/(\beta_\nu\delta_1\delta))`$: small by B3.

### Step 4. Local inertia and the difference from $`\mu_1+\mu_2`$ (item 2)

$`m(\rho)=m_1(\rho)+m_2(\rho)`$, $`m_i(\rho):=-1/(8\kappa_i(\rho))`$: by (2.11), $`m_i`$ is the inertia $`b_i`$ would have with the amplitude it has at distance $`\rho`$ from the other body. By (2.16), $`m_1=\mu_1(1\pm\sigma_1\bar M^{(2)}(\rho)/M_1+O(\varepsilon^3))`$, and by (2.14) $`\mu_1\sigma_1/M_1=(R_1/M_1)/c_1^2\,(1+O(\gamma_1^2))=c_1^{-2}(1+O(\varepsilon))`$; the same for $`b_2`$. With $`\bar M^{(2)}(\rho):=\tfrac14[M^{(2)}(\rho-1)+2M^{(2)}(\rho)+M^{(2)}(\rho+1)]`$:
```math
m(\rho)=\mu_1+\mu_2+s_c\,\bar M^{(2)}(\rho)\Big(\frac1{c_1^2}+\frac1{c_2^2}\Big)+O\big(\varepsilon^3(\lvert\mu_1\rvert+\lvert\mu_2\rvert)\big). \qquad\text{(6.7)}
```
Each body's local inertia contains the second-order mutual term divided by the square of its own speed: once per body, with the sign $`s_c`$. Insert (6.7) into $`E''_{\rm line}`$, $`1/m=(\mu_1+\mu_2)^{-1}(1-\eta)+O(\eta^2)`$ with $`\eta=O(\varepsilon^2)`$, and invert with $`E_b''(0)=E''_{\rm line}(1+\rho_L)`$:
```math
D_\nu:=\frac1{E_b''(0)}-\mu_1-\mu_2=\underbrace{(\mu_1+\mu_2)\frac{1-\beta_\nu}{\beta_\nu}}_{D^{\rm lat}_\nu}+\underbrace{\frac{s_c}{\beta_\nu^2}\Big(\frac1{c_1^2}+\frac1{c_2^2}\Big)\sum_\rho b_\nu(\rho)\bar M^{(2)}(\rho)}_{D^{\rm mark}_\nu}-\frac{\rho_L}{E''_{\rm line}}+O\Big(\frac{\varepsilon^3(\lvert\mu_1\rvert+\lvert\mu_2\rvert)}{\beta_\nu^2},\frac{\rho_L^2}{E''_{\rm line}}\Big), \qquad\text{(6.8)}
```
$`\beta_\nu`$ and $`b_\nu`$ of the full band chain. $`D^{\rm lat}_\nu`$ is of order zero in $`\varepsilon`$ at fixed $`\chi`$ and nonzero for every bound level ($`\lvert\beta_\nu\rvert<1`$). It has the sign of $`\mu_1+\mu_2`$ for $`0<\beta_\nu<1`$, and the opposite sign with $`\lvert D^{\rm lat}_\nu\rvert>2\lvert\mu_1+\mu_2\rvert`$ for $`\beta_\nu<0`$. It comes from $`K_1+K_2`$: the $`P`$-dependence of the relative hopping $`\lvert t(\rho;P)\rvert`$, i.e. from the form $`\cos2p`$ of each body's band (2.11), together with $`W`$, which localizes $`f_\nu`$. $`D^{\rm mark}_\nu`$ is of order $`\varepsilon^2`$ and comes from the dependence of $`K_i`$ on the other body's mark (2.16). The ring part is smaller than both by B4. *Level dependence:* in weak binding the envelope of every bound level varies slowly, so $`b_\nu(\rho)`$ has the sign $`s_\beta`$ up to the nodes, and Hellmann–Feynman for the uniform chain, $`\partial\epsilon_\nu/\partial\bar t_0=2\beta_\nu`$, applied to the bracket of (6.4) gives $`\beta_\nu\simeq s_\beta[1-\frac{a_\nu}6(4\chi^2)^{1/3}]`$: $`1-\lvert\beta_\nu\rvert`$ grows with $`\nu`$. Beyond weak binding $`\beta_\nu`$ of an excited level is not sign-definite. In the odd class the level $`\nu=1`$ has $`\beta_1\to-s_\beta/2`$ for $`\chi\to\infty`$ (antisymmetric contact pair), so $`\beta_1`$ vanishes at an intermediate $`\chi`$. There $`E''_{\rm line}=0`$ at order $`\tau^2`$, B3 fails, and the inertia of that level is set by the order-$`\tau^4`$ terms. *Control:* none in the class. In the wider class of unbound pairs on the line, $`\chi\to0`$ gives $`\beta_0\to s_\beta`$. Then $`D_0\to0`$ for $`s_\beta=+1`$, while for $`s_\beta=-1`$ $`1/E''_{\rm line}\to-(\mu_1+\mu_2)`$, the inertia of the parts at $`p_i=\pm\pi/2`$.

### Step 5. Inertia against cost (item 3)

As in (4.2), the cost of the bound pair is $`\Delta E_\nu:=E_b(0)-E_1(0)-E_2(0)+E_\varnothing`$: eigenvalues of the total contracts of four descriptions (pair, $`b_1`$ alone, $`b_2`$ alone, field alone), so no split of contract terms enters (M6). With $`E_b(0)=\langle f_\nu\vert h_0\vert f_\nu\rangle=\sum_rf_\nu^2U+2\sum_\rho b_\nu\,t(\rho;0)`$ and Step 1,
```math
\Delta E_\nu=\langle M\rangle_\nu+K_\nu+O(\varepsilon^2\lvert\bar\kappa\rvert),\qquad K_\nu:=2\bar t_0(\beta_\nu-1),\qquad\langle M\rangle_\nu=\sum_rf_\nu(r)^2M(r)=M(0)+\langle V\rangle_\nu+O\big(n\lvert g_1g_2\rvert\ell_0\eta/t_f\big). \qquad\text{(6.9)}
```
$`K_\nu`$ is the kinetic cost of the relative motion. Since $`\mu_1+\mu_2=-\bar t_0/(8\bar\kappa_1\bar\kappa_2)`$ and $`\mu_1\mu_2=1/(64\bar\kappa_1\bar\kappa_2)`$, $`D^{\rm lat}_\nu=4\mu_1\mu_2K_\nu/\beta_\nu`$, and splitting $`\bar M^{(2)}=M(0)+\bar V`$ in (6.8):
```math
D_\nu=\frac{4\mu_1\mu_2}{\beta_\nu}K_\nu+\frac{s_c}{\beta_\nu}\Big(\frac1{c_1^2}+\frac1{c_2^2}\Big)M(0)+\frac{s_c}{\beta_\nu^2}\Big(\frac1{c_1^2}+\frac1{c_2^2}\Big)\sum_\rho b_\nu\bar V-\frac{\rho_L}{E''_{\rm line}},\qquad\frac{\Delta E_\nu}{c^2}=\frac{K_\nu+M(0)+\langle V\rangle_\nu}{c^2}. \qquad\text{(6.10)}
```
*No universal identity.* The coefficients of $`K_\nu`$ ($`4\mu_1\mu_2/\beta_\nu`$ against $`c^{-2}`$, ratio of size $`R_1R_2/c^2\gg1`$ by R1) and of the contact value $`M(0)=-\frac{ng_1g_2}{t_f}\frac{L^2-1}{6L}`$ ($`s_c(c_1^{-2}+c_2^{-2})/\beta_\nu`$ against $`c^{-2}`$; $`2s_c/\beta_\nu`$ against 1 at equal speeds) differ, so (6.10) gives no identity $`D_\nu=\Delta E_\nu/c^2`$ with one speed $`c`$ fixed by the contracts. That the relation indeed fails on the class, for every $`c\ge c_{\min}`$, follows from case (i) of (6.17); whether it holds in individual descriptions is decided there.

*Individual equalities.* For a speed $`c`$ let $`S:=c_1^{-2}+c_2^{-2}`$ and
```math
\Delta_\nu(c):=D_\nu-\frac{\Delta E_\nu}{c^2}=C_KK_\nu+C_MM(0)+\mathcal V_\nu-\frac{\rho_L}{E''_{\rm line}},\quad C_K:=\frac{4\mu_1\mu_2}{\beta_\nu}-\frac1{c^2},\quad C_M:=\frac{s_cS}{\beta_\nu}-\frac1{c^2},\quad\mathcal V_\nu:=\frac{s_cS}{\beta_\nu^2}\sum_\rho b_\nu\bar V-\frac{\langle V\rangle_\nu}{c^2}.
```
Let $`c\ge c_{\min}`$; this includes $`c_1`$, $`c_2`$ and equal speeds. Then $`S/\lvert\beta_\nu\rvert>c^{-2}`$, so $`{\rm sgn}\,C_M=s_c\,{\rm sgn}\,\beta_\nu`$ and $`\lvert C_M\rvert\ge c_{\max}^{-2}`$. Further $`4\lvert\mu_1\mu_2\rvert c^2\ge4R_1R_2/c_{\max}^2\gg1`$ (R1: $`c_i\simeq\tau_i\ll R_i`$), so $`{\rm sgn}\,C_K=\sigma_1\sigma_2\,{\rm sgn}\,\beta_\nu`$. Finally $`{\rm sgn}\,K_\nu=s_\mu`$ ($`\lvert\beta_\nu\rvert<1`$) and $`{\rm sgn}\,M(0)=-s_e`$. With $`\lvert\bar V(\rho)\rvert\le F(\lvert\rho\rvert+\frac12)`$ and $`\lvert b_\nu(\rho)\rvert\le\frac12[f_\nu(\rho-1)^2+f_\nu(\rho+1)^2]`$, $`\lvert\mathcal V_\nu\rvert\le4F(\langle\lvert r\rvert\rangle_\nu+\frac32)/(c_{\min}^2\beta_\nu^2)`$, which is below $`\lvert C_MM(0)\rvert`$ if
```math
\text{(S)}\qquad\langle\lvert r\rvert\rangle_\nu+\tfrac32<\frac{\beta_\nu^2\,(L-L^{-1})}{24}\,\frac{c_{\min}^2}{c_{\max}^2}.
```
(S) may be replaced by $`\lvert\mathcal V_\nu\rvert<\lvert C_KK_\nu\rvert`$. This holds in weak binding, where $`\langle V\rangle_\nu\simeq2\lvert K_\nu\rvert`$ (virial theorem of the linear potential) gives $`\lvert\mathcal V_\nu/C_KK_\nu\rvert=O(c_{\max}^2/R_1R_2)`$. Hence, at leading order,
```math
\begin{aligned}&\text{(i) }s_c=-\sigma_1\sigma_2s_\beta:\ \Delta_\nu(c)\neq0,\ \text{of sign }\sigma_1\sigma_2s_\mu\,{\rm sgn}\,\beta_\nu,\ \text{for every bound level and every }c\ge c_{\min},\ \text{under (S) and B4};\\&\text{(ii) }s_c=\sigma_1\sigma_2s_\beta:\ C_KK_\nu\ \text{and}\ C_MM(0)\ \text{have opposite signs, and }\Delta_\nu(c)=0\ \text{where they cancel (codimension one); at equal speeds}\\&\qquad\text{in weak binding near }L^*_\nu\simeq2\cdot4^{1/3}a_\nu\,\big\lvert C_K/C_M\big\rvert_{\beta_\nu=s_\beta}\,\chi^{-1/3}\ \text{at fixed }n,\chi.\end{aligned} \qquad\text{(6.17)}
```
$`L^*_\nu`$ solves $`\lvert C_KK_\nu\rvert=\lvert C_M\rvert FL/6`$ with $`\lvert K_\nu\rvert=\lvert\bar t_0\rvert\frac{a_\nu}34^{1/3}\chi^{2/3}`$, up to relative $`O(\chi^{2/3})`$ and $`O(c^2/R_1R_2)`$. For $`\sigma_1=\sigma_2`$ and $`s_\beta=+1`$ (sets A, B of the code), case (i) is coupling (c).

*An equality inside R and B.* Case (ii) with $`\sigma_1=\sigma_2=-1`$ (then $`\delta_1\ge2R_i`$ for every $`t_f`$, Step 7), coupling (a), $`M_i=M`$, $`\tau_i=\tau`$, $`\gamma_1=-\gamma_2=\varepsilon`$ ($`s_e=-1`$, $`s_\beta=+1`$, highest level). Take $`n=\varepsilon^{-3/4}`$, $`t_f=TM^3/(\tau^2\chi^{2/3})`$ with fixed $`T\gg2.1`$ (then $`\chi^{1/3}=4\varepsilon^{5/4}/T`$), $`\tau/M\ll\varepsilon^{1/4}/T`$, and $`L`$ near $`L^*_0\simeq13M^2/(\tau^2\chi^{1/3})`$. As $`\varepsilon\to0`$, R and B hold and the retained terms dominate the remainders:
- R1: the field gap at $`L^*_0`$ is $`\simeq0.24T\tau^2/M\gg\tau^2/(2M)`$;
- perturbative control: $`n\varepsilon\to0`$ and $`\eta\simeq1.1\varepsilon\chi^{1/3}/T\to0`$;
- B1, B4 and (S): $`L^*_0/\xi_0\simeq8M^2/\tau^2\gg1`$;
- mark expansion: $`\lvert M(0)\rvert/R\simeq0.54\chi^{2/3}\ll1`$;
- remainders: those of (6.8) are small since $`\chi^{2/3}/\varepsilon^3\propto\varepsilon^{-1/2}`$, those of (6.9) since $`4\mu_1\mu_2c^2\chi^{2/3}/\varepsilon^2\gg1`$.

$`\Delta_0`$ changes sign across $`L^*_0`$, and tuning $`\varepsilon`$ at fixed $`L`$ gives an exact zero. So $`D_0=\Delta E_0/c^2`$ with $`c=\tau`$, a speed fixed by the contracts, holds in particular descriptions.

*Not a universal speed.* In case (ii) the zero sets of different levels differ: $`L^*_\nu\propto a_\nu`$ (code, line chain: $`L^*_0=564`$, $`L^*_1=1216`$ against the estimates 553, 1269). Where $`D_0=\Delta E_0/c^2`$, the level $`\nu=1`$ has $`\Delta_1\neq0`$. A fitted $`c_\nu^2:=\Delta E_\nu/D_\nu`$ exists for each level where the signs agree, but it depends on $`\nu`$ and $`L`$: it is a property of the level, not a speed fixed by the contracts. In case (i), under (S) and B4, no level satisfies the relation with any $`c\ge c_{\min}`$.

### Step 6. Weight of the bound level and fall (item 4)

A held source $`g_s\Phi_{x_s}`$ changes the $`\tau=0`$ levels of $`\mathcal G`$ by the held-pair weight $`W_{\rm pair}(j,l)`$ at first order in $`g_s`$, and the $`K_i`$ at relative order $`\gamma_ig_s/t_f`$ (through the field states, as in (2.16)), which enters the fall at $`O(\tau^4\gamma g_s)`$ as in (7.7). Let the source be at a distance $`d_s\gg\xi_\nu`$ from the pair, and work on the line (B1, B4). The weight of the bound level is
```math
W_\nu(X):=\sum_rf_\nu(r)^2\,W_{\rm pair}\big(X-\tfrac r2,X+\tfrac r2\big). \qquad\text{(6.11)}
```
$`W_b`$ vanishes for $`g_1=0`$ and for $`g_2=0`$, hence is $`O(g_1g_2g_s)`$; by (4.5), $`W_{\rm pair}=ng_1\phi(x_1)+ng_2\phi(x_2)+O(\varepsilon^2g_s)`$. $`\phi`$ is quadratic on each arc between images of $`x_s`$ ($`\phi''=-2g_s/(t_fL)`$), and $`\sum_rf_\nu^2\,r=0`$ ($`f_\nu^2`$ even by the reflection of Step 1). Hence, for pair positions not reaching $`x_s`$,
```math
W_\nu(X+1)-W_\nu(X-1)=n(g_1+g_2)\,[\phi(X+1)-\phi(X-1)]+O(\varepsilon^2g_s)+O(e^{-d_s/\xi_\nu}): \qquad\text{(6.12)}
```
at leading order the weight difference of the bound level is that of its members, for every level $`\nu`$.

*Bound band with $`P`$-dependent profile.* Written symmetrically, the sector eigenvector of (6.1) is $`\psi_P(j,l)=L^{-1/2}e^{iP(j+l)/2}f_{\nu,P}(l-j)`$, with $`f_{\nu,P}`$ the eigenvector of the chain with bonds $`\kappa_1(\rho)e^{-iP}+\kappa_2(\rho)e^{iP}=e^{iP}t(\rho;P)`$, unitarily equivalent to $`h_P`$. The gauge of Step 3 gives $`f_{\nu,P}=e^{i\theta_P}F_{\nu,P}`$ with $`F_{\nu,P}`$ real and $`F_{\nu,P}=f_\nu+O(P^2)`$ ($`s_\rho`$ is even in $`P`$). From $`\arg(\kappa_1e^{-iP}+\kappa_2e^{iP})=-P\frac{\kappa_1-\kappa_2}{\kappa_1+\kappa_2}+O(P^3)`$ and $`\kappa_i=-1/(8m_i)`$, $`\theta_P=P\theta'+O(P^3)`$ with $`\theta'(r+2)-\theta'(r)=[m_2(\rho)-m_1(\rho)]/m(\rho)`$ ($`\rho=r+1`$) and $`\theta'`$ odd. Hence $`\psi_P=L^{-1/2}e^{iPY}F_{\nu,P}[1+O(P^3)]`$ with the centre
```math
Y(j,l):=\frac{j+l}2+\theta'(l-j)=\frac{\mu_1j+\mu_2l}{\mu_1+\mu_2}+O\big(\varepsilon^2\lvert l-j\rvert\big): \qquad\text{(6.18)}
```
$`P`$ is conjugate to the inertia-weighted centre, not to the midpoint. The source matrix elements on the band are $`\langle P',\nu\vert W\vert P,\nu\rangle=L^{-1}\sum_{j,l}e^{i(P-P')Y}F_{\nu,P'}F_{\nu,P}W_{\rm pair}[1+O(P^3,P'^3)]`$, not $`f_\nu^2`$ at all momenta. For a start of width $`w`$ in $`Y`$ ($`\lvert P\rvert\lesssim1/w`$), $`F_{\nu,P'}F_{\nu,P}=f_\nu^2[1+O(w^{-2})]`$. So on the band the source acts as $`\tilde W_\nu(\hat Y)`$ up to relative $`O(w^{-2})`$, with $`\tilde W_\nu(Y):=\sum_rf_\nu^2W_{\rm pair}(Y-\frac r2-\theta'(r),Y+\frac r2-\theta'(r))`$ and $`W_{\rm pair}`$ continued between places by its form on the arc. At first order in $`g_i`$, $`\tilde W_\nu-W_\nu`$ is constant on the arc: $`f_\nu^2`$ is even, $`\theta'`$ odd and $`\phi''`$ constant. So the weight differences of the band are those of (6.11), (6.12), up to $`O(\varepsilon^2g_s)`$.

*Acceleration from rest.* Take the band contract with source, $`H=H_{\rm eff}+W_{\rm pair}`$, and a start $`\psi(j,l)=\varphi(Y)f_\nu(l-j)`$, with real envelope $`\varphi`$ of width $`w`$, even about a point $`x_0`$ with $`2x_0\in\mathbb Z`$. Let $`a_\nu(0):=\frac{{\rm d}^2}{{\rm d}\lambda^2}\langle\hat Y\rangle\vert_{\lambda=0}=-\langle[H,[H,\hat Y]]\rangle`$. This needs no band projection and contains the interband terms. It is exactly linear in $`W_{\rm pair}`$, since $`[W,[W,\hat Y]]=0`$. Its $`g_s`$-independent part vanishes on the line: the reflection about $`x_0`$ (Step 1) leaves $`H_{\rm eff}`$ invariant and maps $`\hat Y-x_0\to-(\hat Y-x_0)`$ and $`\psi\to\pm\psi`$. In the linear part, $`-\sum_{a,b}\psi_a\psi_b(W_a-W_b)H_{ab}(Y_b-Y_a)`$, a hop of $`b_i`$ by $`\pm2`$ across the bond $`\rho`$ has $`H_{ab}=\kappa_i(\rho)`$ and, by (6.18), $`Y_b-Y_a=\pm2m_i(\rho)/m(\rho)`$, so $`\kappa_i(Y_b-Y_a)=\mp1/(4m(\rho))`$ for both bodies; on each bond $`\psi_a\psi_b=\varphi^2b_\nu(\rho)[1+O(w^{-2})]`$. Hence
```math
a_\nu(0)=-\sum_X\varphi_X^2\sum_\rho\frac{b_\nu(\rho)}{m(\rho)}\,(\partial_1+\partial_2)W_{\rm pair}\big\vert_{X,\rho}\big[1+O(w^{-2})\big]=-E''_{\rm line}\sum_X\varphi_X^2\,W'_\nu(X)\big[1+O(w^{-2})\big]+O(\varepsilon^2g_sE''_{\rm line})+O(g_s^2)+O(\tau^4\gamma g_s), \qquad\text{(6.13)}
```
with $`\partial_i`$ the centred difference in $`x_i`$ and $`W'_\nu(X):=\tfrac12[W_\nu(X+1)-W_\nu(X-1)]`$; the $`O(g_s^2)`$ is zero within the band contract. The second form uses $`(\partial_1+\partial_2)W_{\rm pair}=n(g_1+g_2)\phi'(X)+(\text{odd in }\rho)+O(\varepsilon^2g_s)`$, whose odd part cancels against the even $`b_\nu/m`$, and (6.12). For one body the same computation gives the leading form of (7.7). So (7.7) carries over to the bound level, for the centre $`\hat Y`$, with $`E''\to E''_{\rm line}`$ and $`W'\to W'_\nu`$. The midpoint $`(\hat x_1+\hat x_2)/2`$ moves by $`\pm1`$ per hop and gets instead $`-\frac{\beta_\nu}2\sum_X\varphi_X^2(W_1'/\mu_1+W_2'/\mu_2)`$ at $`\lambda=0`$ (uniform hopping), the instantaneous response of the relative motion.

The fall factor is $`\Pi_\nu:=E''_{\rm line}W'_\nu`$, and for $`b_i`$ alone $`\Pi_i:=E_i''(0)W_i'=ng_i\phi'/\mu_i=n\gamma_ic_i^2\phi'\,(1+O(\varepsilon))`$ by (4.5), (2.14). With $`1/E''_{\rm line}=(\mu_1+\mu_2)/\beta_\nu+D^{\rm mark}_\nu`$ and (6.12):
```math
\Pi_\nu=\beta_\nu\,\frac{\mu_1\Pi_1+\mu_2\Pi_2}{\mu_1+\mu_2}\,\big[1+O(\varepsilon)\big];\qquad\text{if }\gamma_1c_1^2=\gamma_2c_2^2:\quad\Pi_\nu-\Pi_1=-(1-\beta_\nu)\,\Pi_1+O(\varepsilon\,\Pi_1). \qquad\text{(6.14)}
```
The single bodies have equal fall factors only under the named condition $`\gamma_1c_1^2=\gamma_2c_2^2`$ (M7). Even then the bound pair differs at leading order (order zero in $`\varepsilon`$ at fixed $`\chi`$) by the factor $`\beta_\nu`$. It falls slower than its parts for $`0<\beta_\nu<1`$ and opposite to them for $`\beta_\nu<0`$; for $`s_\beta=-1`$ the parts sit at $`p_i=\pm\pi/2`$, where their own fall factors are $`-\Pi_i`$. The $`O(\varepsilon)`$ corrections come from the second-order weights ((4.5), $`W_b`$ of (4.7)) and from $`D^{\rm mark}`$. *Control:* none in the class; unbound pairs on the line with $`s_\beta=+1`$ ($`\chi\to0`$) give $`\beta_0\to1`$ and equality under the condition.

### Step 7. Dependence on $`t_f`$ (item 5)

At fixed $`n,\gamma_i,M_i,\tau_i`$: $`R_i`$, $`\mu_i`$, $`c_i`$, $`\bar\kappa_i`$, $`\bar t_0`$ do not depend on $`t_f`$ at the orders used; $`M^{(2)}`$, $`F`$ and $`\eta`$ scale as $`1/t_f`$; $`\phi\propto g_s/t_f`$.

*R1 from the held spectra.* Flipping $`b_i`$ from $`e_{jl}`$ reaches the held levels with $`b_i`$'s coupling reversed and all field states. Their distances from $`E(j,l)`$ are $`\lvert2\sigma_iR_i-\omega^{(i)}_n\rvert`$, with $`\omega^{(i)}_n\ge0`$ the excitation energies of that held field. At leading order in $`\varepsilon`$, $`\omega\in\{2t_f\sum_kn_k(1-\cos\frac{2\pi k}L):\sum_kn_k\le N_f\}`$; for $`N_f=1`$, $`\omega\in\{4t_f\sin^2(\pi k/L)\}`$. For $`\sigma_i=-1`$ all distances are $`\ge2R_i`$: no resonance condition on $`t_f`$. For $`\sigma_i=+1`$, R1 excludes the $`t_f`$ for which some $`\omega`$ lies within $`\delta_1`$ of $`2R_i`$; for $`N_f=1`$ these are the intervals $`[(2R_i-\delta_1),(2R_i+\delta_1)]/(4\sin^2(\pi k/L))`$, $`k=1,\dots,L/2`$. Sufficient conditions are $`4N_ft_f\le2R_i-\delta_1`$ (all excitations below) or $`4t_f\sin^2(\pi/L)\ge2R_i+\delta_1`$ (all above). $`\delta`$ is the distance of $`\mathcal G`$ from all other $`\tau=0`$ levels of the sector: field excitations of the $`\mathcal G`$ branches, $`\simeq4t_f\sin^2(\pi/L)`$ shifted by the marks, and doubly flipped levels $`\lvert2\sigma_1R_1+2\sigma_2R_2-\omega\rvert`$. It is not automatically the field gap. With the weak-binding $`\beta_0`$ of Step 4:
```math
\chi=\frac{n\lvert g_1g_2\rvert}{t_f\lvert\bar t_0\rvert}\propto\frac1{t_f},\quad1-s_\beta\beta_0\simeq0.270\,\chi^{2/3}\propto t_f^{-2/3},\quad\frac{\tau'^2}{\delta_1\delta}\ll1\ll\chi L^3,\quad\min_n\big\lvert2R_i-\omega^{(i)}_n\big\rvert\ge\delta_1\ \ (\sigma_i=+1). \qquad\text{(6.15)}
```
The second inequality bounds $`t_f`$ from below where $`\delta`$ is the field gap, $`t_f\gg\tau'^2/(4\delta_1\sin^2(\pi/L))`$, and $`\chi L^3\gg1`$ (B1) bounds it from above; B4 bounds it further from above, since $`\xi_0\propto t_f^{1/3}`$ while the mark terms fall as $`1/t_f`$. Hence: (6.3) does not depend on $`t_f`$. $`D^{\rm lat}_\nu`$ and, for $`s_\beta=+1`$, $`1-\Pi_\nu/\Pi_1`$ fall as $`t_f^{-2/3}`$; $`D^{\rm mark}_\nu`$ and $`M(0)`$ fall as $`1/t_f`$; the equality points of (6.17)(ii) move as $`L^*_\nu\propto t_f^{1/3}`$. No $`t_f`$ in the window gives $`\lvert\beta_\nu\rvert=1`$, so (6.10) and (6.14) persist. A faster field weakens the binding and brings the pair's inertia and fall factor towards those of its parts in the states they occupy: $`\mu_1+\mu_2`$ and the inertia-weighted $`\Pi_i`$ for $`s_\beta=+1`$, $`-(\mu_1+\mu_2)`$ and the reversed fall for $`s_\beta=-1`$. The limit is reached only where the pair stops being bound on the ring.

## Result

- **(6.1)** Class above, order $`\tau^2`$: in the sector $`P`$ (body 1 as representative, continued to real $`P`$) the band contract is the relative chain $`h_P`$ with bond amplitudes $`t(\rho;P)=\kappa_1(\rho)e^{-2iP}+\kappa_2(\rho)`$ and separate rings for $`r`$ even and odd.
- **(6.2)** Leading order in $`\varepsilon`$: $`M^{(2)}(r)=-2ng_1g_2\ell(r)/t_f`$ and the relative potential $`V(r)=\frac{ng_1g_2}{t_fL}r(L-r)`$, a well at contact for $`g_1g_2>0`$ and a hill for $`g_1g_2<0`$.
- **(6.3)** Under R and B, every branch combination and both signs of $`\gamma_1\gamma_2`$: bound levels exist; they are the lowest levels of relative motion if $`\sigma_1\sigma_2\gamma_1\gamma_2>0`$ and the highest if $`<0`$. The extreme level is of one sign (bodies near $`p_i=0`$) if $`s_\beta={\rm sgn}[g_1g_2(\mu_1^{-1}+\mu_2^{-1})]=+1`$ and alternating (bodies near $`p_1=-p_2=\pm\pi/2`$) if $`s_\beta=-1`$; excited levels have $`\nu`$ nodes of their envelope.
- **(6.4)** Leading order in $`\varepsilon`$, uniform hopping, weak binding $`F\ll\lvert\bar t(P)\rvert`$, up to $`O(\chi^{2/3})`$ and $`O(\xi_\nu/L)`$: $`E_b(P)=E_1(0)+E_2(0)-E_\varnothing+M(0)-2\bar t_0+s_e[-2\lvert\bar t(P)\rvert+a_\nu(4\lvert\bar t(P)\rvert F^2)^{1/3}]`$, with $`a_\nu`$ the merged zeros of $`{\rm Ai}'`$ and $`{\rm Ai}`$ ($`a_0=1.0188`$, $`a_1=2.3381`$, $`a_2=3.2482`$).
- **(6.5)** Definitions: bond weights $`b_\nu`$, bond overlap $`\beta_\nu`$ with $`\lvert\beta_\nu\rvert<1`$ for every bound level, local pair inertia $`m(\rho)`$.
- **(6.6)** Exact for the band contract (order $`\tau^2`$, B2): $`E_b''(0)=E''_{\rm line}(1+\rho_L)`$ with $`E''_{\rm line}=\sum_\rho b_\nu(\rho)/m(\rho)`$ and the ring remainder $`\rho_L`$, the only part that depends on the continuation.
- **(6.7)** Order $`\varepsilon^2`$, error $`O(\varepsilon^3)`$: $`m(\rho)=\mu_1+\mu_2+s_c\bar M^{(2)}(\rho)(c_1^{-2}+c_2^{-2})`$; the mutual term enters each body's inertia once, over its own speed squared, with sign $`+`$ for (a) and $`-`$ for (c).
- **(6.8)** Through order $`\varepsilon^2`$ and to first order in $`\rho_L`$: $`1/E_b''(0)-\mu_1-\mu_2=D^{\rm lat}_\nu+D^{\rm mark}_\nu-\rho_L/E''_{\rm line}`$. The leading part $`D^{\rm lat}_\nu=(\mu_1+\mu_2)(1-\beta_\nu)/\beta_\nu`$, from the $`P`$-dependence of $`K_1+K_2`$ with the binding by $`W`$, is nonzero for every bound level. It has the sign of $`\mu_1+\mu_2`$ for $`0<\beta_\nu<1`$, and the opposite sign with modulus $`>2\lvert\mu_1+\mu_2\rvert`$ for $`\beta_\nu<0`$. In weak binding $`\beta_\nu\simeq s_\beta[1-\frac{a_\nu}6(4\chi^2)^{1/3}]`$ for every weakly bound level, so $`1-\lvert\beta_\nu\rvert`$ grows with $`\nu`$. Beyond weak binding $`\beta_\nu`$ of an excited level can change sign (odd class, $`\nu=1`$: from $`s_\beta`$ to $`-s_\beta/2`$), where $`E''_{\rm line}`$ vanishes at order $`\tau^2`$. $`D^{\rm mark}_\nu=O(\varepsilon^2)`$ comes from the $`\rho`$-dependence of $`K_i`$.
- **(6.9)** Order $`\tau^2`$, through $`\varepsilon^2`$: the cost of the bound pair is $`\Delta E_\nu=\langle M\rangle_\nu+K_\nu`$ with the kinetic cost $`K_\nu=2\bar t_0(\beta_\nu-1)`$.
- **(6.10)** Negative, leading order, both couplings: $`1/E_b''(0)-\mu_1-\mu_2=\Delta E_\nu/c^2`$ is not an identity on the class for any speed $`c\ge\min(c_1,c_2)`$ (in particular $`c_1`$, $`c_2`$ and equal speeds). The coefficients of $`K_\nu`$ ($`4\mu_1\mu_2/\beta_\nu`$ against $`c^{-2}`$) and of $`M(0)`$ ($`s_c(c_1^{-2}+c_2^{-2})/\beta_\nu`$ against $`c^{-2}`$) differ, and the relation fails in every description of case (i) of (6.17).
- **(6.11)** Definition: the weight of the bound level is the $`f_\nu^2`$-average of the held-pair weight, at first order in $`g_s`$.
- **(6.12)** First order in $`g_i`$ and $`g_s`$, source far from the pair: the weight difference of the bound level is that of its members, $`n(g_1+g_2)\Delta\phi`$, for every level.
- **(6.13)** (7.7) carries over to the bound level for the centre $`\hat Y`$ of (6.18), with $`E''_{\rm line}`$ and $`W'_\nu`$. This holds on the line, for a start $`\varphi(Y)f_\nu`$ with real envelope of width $`w`$ even about a point, at first order in $`g_s`$, up to a relative $`O(w^{-2})`$ and additive $`O(\varepsilon^2g_sE''_{\rm line})`$, $`O(\tau^4\gamma g_s)`$. The midpoint of the pair has in general a different acceleration from rest.
- **(6.14)** Negative, leading order (order zero in $`\varepsilon`$ at fixed $`\chi`$), both couplings: $`\Pi_\nu=\beta_\nu(\mu_1\Pi_1+\mu_2\Pi_2)/(\mu_1+\mu_2)`$. Even under the named condition $`\gamma_1c_1^2=\gamma_2c_2^2`$ the bound level's fall factor is $`\beta_\nu\Pi_1\neq\Pi_1`$. The first order of the difference is $`-(1-\beta_\nu)\Pi_1`$, with corrections $`O(\varepsilon\Pi_1)`$; for $`\beta_\nu<0`$ the pair falls opposite to its parts. No control in the class.
- **(6.15)** Item 5, at fixed $`n,\gamma_i,M_i,\tau_i`$: $`\chi\propto1/t_f`$, and in weak binding $`1-s_\beta\beta_0\simeq0.270\chi^{2/3}`$, so the deviations of items 2 and 4 fall as $`t_f^{-2/3}`$ and the mark terms as $`1/t_f`$. The resonance condition of R1 restricts $`t_f`$ only for $`\sigma_i=+1`$: it excludes the intervals where an excitation of the held field with $`b_i`$ flipped lies within $`\delta_1`$ of $`2R_i`$. Sufficient conditions are $`4N_ft_f\le2R_i-\delta_1`$ or $`4t_f\sin^2(\pi/L)\ge2R_i+\delta_1`$. $`\tau'^2/(\delta_1\delta)\ll1\ll\chi L^3`$ bound $`t_f`$ from below (where $`\delta`$ is the field gap) and from above. No $`t_f`$ in the window removes (6.10) or (6.14).
- **(6.16)** Bound on the ring remainder at the bond farthest from contact: $`\lvert\rho_L\rvert\le\tilde\Phi'(0)^2[2\lvert s_*b_\nu\rvert+4s_*^2(f_\nu(r_*)^2+f_\nu(r_*+2)^2)/\Delta_\nu]/\lvert E''_{\rm line}\rvert`$, exponentially small in $`L/\xi_\nu`$ (times $`L^2`$). $`E_b''(0)`$ is independent of the continuation to relative accuracy $`\lvert\rho_L\rvert`$.
- **(6.17)** Leading order, every speed $`c\ge\min(c_1,c_2)`$ (including $`c_1`$, $`c_2`$ and equal speeds), every bound level. (i) If $`s_c=-\sigma_1\sigma_2s_\beta`$, then $`1/E_b''(0)-\mu_1-\mu_2\neq\Delta E_\nu/c^2`$, under (S) (or $`\lvert\mathcal V_\nu\rvert<\lvert C_KK_\nu\rvert`$, e.g. weak binding) and B4. (ii) If $`s_c=\sigma_1\sigma_2s_\beta`$, the two leading terms have opposite signs and equality holds where they cancel, a codimension-one condition; at equal speeds in weak binding this is near $`L^*_\nu\simeq2\cdot4^{1/3}a_\nu\lvert C_K/C_M\rvert\chi^{-1/3}`$. Such equalities occur inside R and B ($`\sigma_i=-1`$, coupling (a), the family of Step 5). It holds there for one level at a time, so a fitted ratio $`\Delta E_\nu/D_\nu`$ depends on the level and is not a universal speed.
- **(6.18)** On the line, the plane-wave label $`P`$ of the bound band is conjugate to the centre $`Y=\frac{j+l}2+\theta'(l-j)=\frac{\mu_1j+\mu_2l}{\mu_1+\mu_2}+O(\varepsilon^2\lvert l-j\rvert)`$. With the $`P`$-dependent profile the projected source is $`\tilde W_\nu(\hat Y)`$, whose differences equal those of $`W_\nu`$ up to $`O(\varepsilon^2g_s)`$ and relative $`O(w^{-2})`$.

## Consistency checks

1. *Dimensions.* $`P`$ and the positions are dimensionless, so $`E_b''`$, $`E_i''`$, $`W'_\nu`$, $`W_i'`$ have the dimension $`[C]`$, and $`\mu_i`$, $`m`$, $`1/E_b''`$ have $`[C]^{-1}`$. So do $`\bar M^{(2)}/c_i^2`$ and $`\mu_1\mu_2K_\nu`$ ($`c_i^2\sim[C]^2`$). $`\Pi_\nu`$, $`\Pi_i`$ and $`a_\nu(0)`$ have $`[C]^2`$, the dimension of a second derivative in $`\lambda`$. $`\beta_\nu`$, $`\chi`$, $`\rho_L`$ are pure numbers. Passed.
2. *Unbound limit $`\chi\to0`$ on the line* (e.g. $`\gamma_2\to0`$): $`\beta_0\to s_\beta`$ and $`M^{(2)}\to0`$, so $`1/E_b''(0)\to s_\beta(\mu_1+\mu_2)`$. This agrees with the extremum of $`E_1(p_1)+E_2(p_2)`$ at fixed $`p_1+p_2=P`$. For $`s_\beta=+1`$ it lies at $`p_i=0`$, with curvature $`1/(\mu_1+\mu_2)`$. For $`s_\beta=-1`$ it lies at $`p_1=-p_2=\pi/2`$, where the local inertias are $`-\mu_i`$ and the curvature is $`-1/(\mu_1+\mu_2)`$. Passed.
3. *Tight binding $`\chi\to\infty`$.* Even class: $`f_0\simeq\delta_{r0}`$, $`f_0(\pm2)\simeq\bar t_0/(E_b-U(2))`$, so $`\beta_0\simeq s_\beta/\chi`$ and $`E_b''(0)\simeq s_e\,8\bar\kappa_1\bar\kappa_2/F`$. This agrees with direct second-order perturbation of the contact state, $`E_b(P)=U(0)-s_e\lvert\bar t(P)\rvert^2/F`$. Odd class, extreme level: $`f_0\simeq(\delta_{r,1}+s_\beta\delta_{r,-1})/\sqrt2`$, $`\beta_0\to s_\beta/2`$, so $`1/E_b''(0)=2s_\beta(\mu_1+\mu_2)`$. This agrees with the two-site level $`U(1)-s_e\lvert\bar t(P)\rvert`$, whose curvature is $`4s_e\bar\kappa_1\bar\kappa_2/\lvert\bar t_0\rvert`$. Passed.

## Open issues

- The code sets do not meet B4 for the mark terms: $`\lvert\rho_L\rvert=0.6`$–$`12\%`$, against $`\lvert D^{\rm mark}\rvert\approx0.2`$–$`0.3\%`$ of $`1/E_b''`$. The code therefore checks (6.6) with the ring term included.
- The closed forms (6.2), (6.4), (6.15), (6.17) use $`M^{(2)}`$; at $`\eta\approx0.3`$ (code) the exact binding slope is about half of $`F`$. Statements in terms of $`\beta_\nu`$, $`b_\nu`$, $`M`$ are not affected.
- The $`O(\varepsilon^3)`$ remainder of (6.7) is large at moderate couplings (code: ratio 1.40 for (a), $`-0.19`$ for (c) at $`\eta\approx0.3`$), so $`D^{\rm mark}`$ is reliable only for small $`\eta`$.
- The $`O(\varepsilon)`$ corrections of (6.13), (6.14) from the second-order weights are not evaluated (the bond function $`B`$ of (4.7) is not quoted). In the code they are 13–16% in $`\Delta W_\nu/(\Delta W_1+\Delta W_2)`$. In the acceleration they reach 50% for set C, where $`g_1+g_2`$ is small against $`\lvert g_i\rvert`$.
- On the ring, (6.13) has a $`g_s`$-independent part from the relative cut $`r=L/2`$, where the reflection argument fails. In the code it is up to 0.6% of the first-order part (set A) and drops to $`10^{-4}`$ of it when the profile is cut there; it is not bounded analytically.
- For the even class in tight binding, $`\beta_0\sim1/\chi`$, and B3 fails when $`\chi\gtrsim\delta_1\delta/\tau'^2`$; the order-$`\tau^4`$ band contract is then needed. The same holds near the sign change of $`\beta_\nu`$ of excited levels.
- For $`\sigma_i=+1`$ and $`N_f>1`$ the excitation energies near $`2R_i`$ become dense, and the windows of (6.15) shrink. Whether weakly coupled resonances (matrix elements $`O(\gamma^k)`$ for $`k`$ excited objects) can be tolerated is open.
- The family with an equality in (6.17)(ii) needs very large rings ($`L^*_0\propto M^2/(\tau^2\chi^{1/3})`$) and rests on the stated orders of the remainders of (6.7) and (6.9). It was checked only on the leading-order line chain.
- Out of scope: full grip, tori, the highest field state, bodies of one type, the speed of a front of the field; how typical the structure is (item 5 of the base problem).

## Code

- `code/v2/check_inertia.py` (check). It treats $`N_f=1`$, $`t_f=1`$ and three parameter sets:
  - A: $`\sigma_i=+1`$, $`M=(3,4)`$, $`\tau_1=0.2`$, $`\gamma=(0.09,0.07)`$, $`r`$ even, lowest level; $`\tau_2=\tau_1`$ for (a) and $`\tau_2=\tau_1(1+\gamma_1/L)/(1+\gamma_2/L)`$ for (c), so that $`c_1=c_2`$ exactly for both couplings.
  - B: $`\sigma_i=-1`$, $`M=(2.5,2)`$, $`\tau=(0.16,0.2)`$, $`\gamma=(0.10,-0.14)`$, $`r`$ odd, highest level, unequal speeds.
  - C: $`\sigma_i=+1`$, $`M=(3,4)`$, $`\gamma=(0.10,-0.05)`$, $`r`$ even, highest level, alternating ($`s_\beta=-1`$), speeds equalized as in A.

  Each set runs at $`L=12,16`$ for couplings (a) and (c). The script builds the exact sector contract (body 1 as representative, continued in $`P`$) and finds the exact bound level by its weight on $`\mathcal G`$ ($`\ge0.998`$). It takes the curvature by second-order perturbation in $`P`$ (cross-checked by finite differences) and builds the band contract by second-order Schrieffer–Wolff. Results:
  - (6.6) with its ring term agrees with the exact curvature to $`\le0.27\%`$ in all 12 cases.
  - $`\beta_\nu=0.69`$–$`0.79`$ (A), $`0.77`$–$`0.78`$ (B) and $`-0.58`$ to $`-0.65`$ (C). $`1/E_b''(0)=(1.22`$–$`1.29)(\mu_1+\mu_2)`$ for A, B and $`(-1.52`$ to $`-1.64)(\mu_1+\mu_2)`$ for C: the alternating level has negative inertia although both bodies have positive inertia.
  - $`\rho_L`$ is 12% and 3% (A, $`L=12,16`$) and 6% and 0.7% (B, C). The bound (6.16) holds in all cases and exceeds $`\lvert\rho_L\rvert`$ by factors 6–11.
  - $`D\,c^2/\Delta E`$ is $`-500`$ to $`-575`$ (A), $`-208`$ to $`-363`$ (B, with $`c_1`$ or $`c_2`$) and $`-1043`$ to $`-1112`$ (C): far from 1, since these $`L`$ lie far below $`L^*_\nu`$.
  - The ratio of the numerical $`m(\rho)-\mu_1-\mu_2`$ to (6.7) tends to 1 as the couplings are scaled down (1.04 for (a), 0.93 for (c) at scale 0.03).
  - R1 gaps from the held-sector spectra: at $`t_f=1`$, $`\delta_1=2.0`$ (A, C) and $`3.9`$ (B), and $`\delta=0.228`$ ($`L=12`$), $`0.123`$ ($`L=16`$), below the free field gaps $`0.268`$, $`0.152`$. At $`t_f=40`$, $`\delta_1=2.6`$ (A), $`4.0`$ (B), $`2.7`$ (C) for $`L=12`$ (all excitations above $`2R_i`$), but $`0.024`$ (A) and $`0.023`$ (C) for $`L=16`$ (resonance $`4t_f\sin^2(\pi/16)\simeq2R_1`$), while B keeps $`4.0`$.
  - Sign rule (6.17) on the leading-order line chain ($`\chi=0.05`$, $`\sigma_i=-1`$, $`s_e=-1`$, $`4\mu_1\mu_2c^2=64`$): $`\Delta_\nu`$ changes sign for (a) at $`L=564`$ ($`\nu=0`$) and $`L=1216`$ ($`\nu=1`$), against the estimates 553 and 1269, and never for (c) in $`100\le L\le3000`$.

  Outputs: `code/v2/output/inertia_check.txt`, `code/v2/output/inertia_check.json`.
- `code/v2/check_weight.py` (check). Set A, couplings (a) and (c), $`L=16,20`$, held source $`g_s=-0.01`$ (and $`-0.005`$ at $`L=16`$). It computes the exact eigenvalues of the full contract near the bottom of the bound band (weight on $`\mathcal G\ge0.9997`$) and compares them with three reductions: (i) the first-order projected contract $`E_b(P_k)+\langle P',v_{P'}\vert g_s\Phi_{x_s}\vert P,v_P\rangle`$ with the exact $`P`$-dependent sector eigenvectors; (ii) the frozen description $`E_b(\hat P)+W_\nu(\hat X)`$ with (6.11); (iii) the same with the pair inertia set to $`\mu_1+\mu_2`$. Results:
  - Main level spacing: (i) is within 0.15% and (ii) within 0.17% of the exact value; (iii) misses it by 10–20%.
  - Splittings of the near-degenerate pairs ($`E_b(P+\pi)=E_b(P)`$): (i) reproduces the first to 0.2–1.2% and the second to 3.5–10%; (ii) misses them by up to a factor 30. So the main spacing tests the product $`E_b''W_\nu''`$, while only (i) tests the complete first-order projected contract.
  - The common level offsets ($`\approx10^{-5}`$) scale as $`g_s^2`$.
  - $`\Delta W_\nu/(\Delta W_1+\Delta W_2)`$ is 0.87 at these couplings and tends to 1 as they are scaled down (0.997 at scale 0.03), as in (6.12).

  Second part, sets A and C at $`L=24`$: the script computes $`a(0)=-\langle[H,[H,\hat Z]]\rangle`$ exactly in the position-space band contract (exact Schrieffer–Wolff amplitudes, first-order held weights), for $`\hat Z=\hat Y`$ of (6.18) and for the midpoint. The start is $`\varphi(Y)f_\nu`$ with a Gaussian envelope of width $`w=1,1.5,2`$ centred at $`L/4`$. Results:
  - With the weights' couplings scaled by 0.05 (first order in $`g_i`$), the first-order part of $`a_Y`$ over the right side of (6.13) is 0.88, 0.95, 0.97 (A) and 1.02, 1.00, 0.99 (C). The trend is $`O(w^{-2})`$.
  - For set C, $`a_Y/a_{\rm mid}=0.61`$, 0.59, 0.58 against the predicted 0.58: $`\hat Y`$, not the midpoint, carries (6.13).
  - At full couplings the ratio is 0.90–0.99 (A) and 0.47–0.65 (C, second-order weights).
  - The $`g_s`$-independent part is up to 0.6% of the first-order part (A); with the profile cut at $`\lvert r\rvert<L/3`$ it drops to $`10^{-4}`$ of the first-order part.

  Outputs: `code/v2/output/weight_check.txt`, `code/v2/output/weight_check.json`.

## Methods used

- band contract (second-order Schrieffer–Wolff), plane-wave sectors of the joint translation
- gauge reduction of a chain to bond magnitudes and one flux; Hellmann–Feynman theorem
- Perron–Frobenius, Sturm oscillation; Cauchy–Schwarz
- second-order perturbation theory; Airy functions (continuum limit of a linear potential), virial theorem
- sign analysis of coefficients; scaling families of descriptions
- reflection symmetry; double commutator for the acceleration from rest; band projection with momentum-dependent eigenvectors
- exact diagonalization (dense and shift-invert sparse) for the code checks
