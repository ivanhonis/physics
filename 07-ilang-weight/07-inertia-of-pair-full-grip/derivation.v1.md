# Inertia and weight of a pair bound through the field, full grip

- **Subproject:** 07-ilang-weight
- **Package:** 07-inertia-of-pair-full-grip
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-21

## Setup and assumptions

**Description (M8).** The field, the two bodies, the full grip and the field state of `question.md`: ring of even length $`L\ge6`$, $`N_f\ge1`$ field objects with own term $`C_1`$, $`n=N_f/L`$; Model D bodies $`b_1,b_2`$ of different types, own contract the motion term $`A`$ with $`\tau_i`$, rest and clock term only in the pair term $`\gamma_i\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m_i+D_i)\otimes\Phi_x`$; no pair term between $`b_1,b_2`$; records at $`\kappa\to0`$. $`D_i`$ commutes with every term, so the clock level $`k_i`$ is conserved and on branch $`\sigma`$ the pair term is $`\sigma\gamma_iM_i\Phi_x`$; $`g_i=\sigma_i\gamma_iM_i`$ for the selected branches.

**Inputs** (quoted in `question.md`): (2.1), (2.10) of 07-ilang-weight/02-two-free-bodies; (4.2) of 06-ilang-source/04-profile; (4.2), (4.5), (4.7) of 07-ilang-weight/04-weight-of-bond (ring, $`\mathcal X=L`$); (5.1), (5.3), (5.4), (5.7), (5.14) of 07-ilang-weight/05-inertia-of-mark (FG: $`\theta=0`$, $`K=T_-`$, $`v=\tau`$); (6.1), (6.5), (6.6), (6.8), (6.9), (6.13) of 07-ilang-weight/06-inertia-of-pair. Their notation is used unchanged ($`\ell,\ell_0,\ell^{(2)},\phi,B,\eta,\mu_i,\kappa_i,\bar\kappa_i,\bar t_0,d_i,U,f_0,b_0,\beta_0,m,\Delta E_0,K_0,\langle\cdot\rangle_0,W_{\rm pair}`$). On $`0\le x\le L`$, $`\ell(x)=\ell_0-\frac{x(L-x)}{2L}`$, $`\ell_0=\frac{L^2-1}{12L}`$ (it solves $`\Lambda\ell=\delta_0-\frac1L`$, $`\sum_x\ell=0`$, by substitution). $`F:=ng_1g_2/t_f`$; $`'`$ is the central difference in the place.

**Assumptions** (M8, M9; each a choice of the package).
- **S1** Field state: the lowest state adapted to the bodies (A11): in the group $`\mathcal G`$ every field object is in the lowest one-object state of the held configuration.
- **S2** Band regime: $`\max_i\tau_i\ll d`$, with $`d\simeq\min\big(2n\lvert g_1\rvert,2n\lvert g_2\rvert,\varepsilon_1-2n(g_1^++g_2^+)\big)`$, $`g^+:=\max(g,0)`$, the distance of $`\mathcal G`$ to the other held levels ((5.4) for each body and for the joint flip, leading order in $`\eta`$). Omitted: relative $`O(\tau^2/d^2)`$.
- **S3** Field: $`\eta=\max_i\lvert g_i\rvert\ell_0/t_f\ll1`$ and $`N_f\eta\ll1`$. Omitted: relative $`O(\eta)`$ in mutual terms, $`O(N_f\eta^2)`$ in field overlaps.
- **S4** Binding: $`w\ll L`$, $`w:=(4\lvert\bar t_0\rvert/\lvert F\rvert)^{1/3}`$. Omitted: the flux term of (6.6) (exponentially small in $`(L/w)^{3/2}`$) and $`\langle V\rangle_0/\lvert B(0)\rvert=O(w/L)`$.
- **S5** Regime of item 3 (ii): $`1-\beta_0\ll\eta`$ (hence $`w\gg1`$).
- **S6** Source: a held source $`g_s`$ at $`x_s`$, weights to first order in $`g_s`$; pair centre $`X`$ at distance $`s`$ from $`x_s`$, $`w\ll s\le L/2`$, $`u:=s/L`$.
- Out of the class (tuned): $`\lvert\tau_1^2g_2+\tau_2^2g_1\rvert`$ small against $`\max(\tau_1^2\lvert g_2\rvert,\tau_2^2\lvert g_1\rvert)`$ (this is $`\mu_1^{-1}+\mu_2^{-1}`$ small, by Step 1); in item 4, $`\lvert g_1+g_2\rvert`$ small against $`\max\lvert g_i\rvert`$.

## Derivation

### Step 1. Held levels, half-gaps and odd parts

By S1, non-interacting objects in the lowest state all occupy the lowest one-object level, so the held level of $`\mathcal G`$ is $`E(j,l)=N_f\varepsilon_0(g_1\,\text{at}\,j,\,g_2\,\text{at}\,l)`$ and the mutual term $`M(r)`$, $`r=l-j`$, is (4.2) of 06-ilang-source/04-profile. Define, with the other coupling held fixed,
```math
\sigma_iR_i:=\tfrac{N_f}2\big[\varepsilon_0(g_i)-\varepsilon_0(-g_i)\big],\quad c_i^2:=\frac{\sigma_iR_i}{\mu_i},\quad M_i^{o}(r):=\tfrac12\big[M(g_i)-M(-g_i)\big](r),\quad M_i^e:=M-M_i^o,\quad \bar f(\rho):=\tfrac14\big[f(\rho-1)+2f(\rho)+f(\rho+1)\big].\qquad\text{(7.1)}
```
$`\sigma_iR_i`$ is the branch-odd part of the cost (5.3) ($`\theta=0`$). Rayleigh–Schrödinger perturbation of $`\varepsilon_0`$ in $`\sum_ag_a\delta_{x_a}`$, with $`\varepsilon_q-\varepsilon_0=2t_f(1-\cos q)`$ and $`\frac1L\sum_{q\ne0}\frac{e^{iqx}}{2(1-\cos q)}=\ell(x)`$, gives $`N_f\varepsilon_0=-2N_ft_f+n\sum_ag_a-\frac n{t_f}\sum_{a,b}g_ag_b\ell(x_a-x_b)+O(n\lvert g\rvert\eta^2)`$. Hence $`\sigma_iR_i=ng_i[1+O(\eta^2)]`$; $`M=B(r)[1+O(\eta)]`$ with $`B`$ of (4.2) of 04-weight-of-bond, and since $`B\propto g_1g_2`$ is odd in each coupling, $`M_1^o=M_2^o=B[1+O(\eta)]`$, $`M_i^e=O(\eta B)`$. In (5.3) the field state of the flipped branch differs at first order in $`g_i`$ by a vector of squared norm $`O(\eta^2)`$ per object, so $`c_i^2=\tau_i^2[1+O(N_f\eta^2)]`$ and $`\mu_i=ng_i\tau_i^{-2}[1+O(N_f\eta^2)]`$; in particular $`\mathrm{sign}\mu_i=\mathrm{sign}g_i`$.

### Step 2. Band contract and selected level (item 1)

The derivation of (2.10) uses only that $`\mathcal G`$ is isolated and that each motion term moves one body by one place and flips its branch; the full grip changes only the held levels ($`\theta=0`$ in (5.1)). So (2.10) holds under S2 with error $`O(\tau^4/d^3)`$, and with (2.1) the ansatz $`\psi(j,l)=e^{iPj}g(l-j)`$ gives (6.1) unchanged (the double step of $`b_1`$ carries the relative field coordinates: phase $`e^{-2iP}`$). Each motion term conserves $`x_i`$ plus the branch index mod 2, so the parity of $`r`$ is conserved in $`\mathcal G`$; each parity class has its own selected level and everything below holds for either.

*Amplitudes.* The double step of $`b_i`$ across the relative bond $`\rho`$ passes through the held level with $`b_i`$ flipped at relative place $`\rho`$. Since $`M(-g_i)=-M_i^o+M_i^e`$, the gap from the held level at $`r=\rho\mp1`$ is
```math
\Delta_i(r;\rho)=2\sigma_iR_i+M_i^o(r)+M_i^o(\rho)+M_i^e(r)-M_i^e(\rho).\qquad\text{(7.2)}
```
Second-order Schrieffer–Wolff with symmetrized denominators gives $`\kappa_i(\rho)=-\frac{\tau_i^2a_i^2}8\big[\Delta_i(\rho-1;\rho)^{-1}+\Delta_i(\rho+1;\rho)^{-1}\big]`$, up to the excited-state term of (5.3); for $`M=0`$ this is $`\bar\kappa_i=-1/(8\mu_i)`$ of (5.3). Expanding in $`M/\sigma_iR_i=O(\eta)`$ (the $`M_i^e`$ terms combine to a second difference, negligible), the **local inertia** of $`b_i`$ is
```math
m_i(\rho):=-\frac1{8\kappa_i(\rho)}=\mu_i+\frac{\bar M_i^o(\rho)}{c_i^2}+O(\lvert\mu_i\rvert\eta^2)=\mu_i+\frac{\bar B(\rho)}{\tau_i^2}\big[1+O(\eta)\big].\qquad\text{(7.3)}
```
The partner's mark changes each body's local inertia by the bond average of the mutual term over that body's own $`\tau_i^2`$. The same gaps give $`d_i(r)=-2\bar\kappa_i[1-\bar M_i^o(r)/\sigma_iR_i]`$. (6.5) and (6.6) hold: they use only the form (6.1), a real $`f_0`$ at $`P=0`$, and Hellmann–Feynman in the bond magnitudes and the flux.

*Bound level.* $`U(r)-U(0)=V(r)[1+O(\eta,\tau^2/d^2)]`$ with $`V(r):=B(r)-B(0)=F\,r(L-r)/L`$ on $`0\le r\le L`$. Near the edge $`P=0`$, $`k=0`$ of the relative band, (6.1) has relative hop $`\bar t_0=-\frac18(\mu_1^{-1}+\mu_2^{-1})`$: the selected level is the lowest if $`\bar t_0<0`$, the highest if $`\bar t_0>0`$. It is bound at $`r\approx0`$ iff the extremum of $`V`$ at $`r=0`$ pushes it out of the band: a minimum ($`F>0`$) for the lowest, a maximum ($`F<0`$) for the highest, i.e. $`g_1g_2(\mu_1^{-1}+\mu_2^{-1})>0`$. With Step 1:
```math
\text{selected level bound}\iff\tau_1^2g_2+\tau_2^2g_1>0,\qquad g_i=\sigma_i\gamma_iM_i .\qquad\text{(7.4)}
```
Both $`g_i>0`$: bound, lowest. Both $`g_i<0`$: not bound. Opposite signs: bound (highest) iff the inequality holds. Otherwise the extreme level sits at $`r\approx L/2`$, where $`V`$ has its other extremum (control: case D of the code). In the continuum limit of (6.1), $`-4\lvert\bar t_0\rvert\partial_r^2+\lvert F\rvert\lvert r\rvert`$, the width is $`w`$ of S4 and $`1-\beta_0=O(w^{-2})`$; $`f_0>0`$ (Perron–Frobenius), so $`b_0>0`$ and $`0<\beta_0\le1`$.

### Step 3. Inertia of the pair (item 2)

By (7.3), $`m(\rho)=\mu_1+\mu_2+\delta m(\rho)`$, $`\delta m=\sum_i\bar M_i^o/c_i^2`$. In (6.6), $`1/\sum_\rho b_0/m`$ is exact in the constant part of $`\delta m`$ and first order in its variation ($`O(\lvert\mu\rvert\eta^2w^2/L^2)`$ omitted):
```math
D_0=\underbrace{(\mu_1+\mu_2)\frac{1-\beta_0}{\beta_0}}_{D^{\rm lat}}+\underbrace{\frac1{\beta_0^2}\sum_\rho b_0(\rho)\sum_i\frac{\bar M_i^o(\rho)}{c_i^2}}_{D^{\rm mark}}+O\Big((\lvert\mu_1\rvert+\lvert\mu_2\rvert)\big[\eta^2+\tfrac{\tau^2}{d^2}(\eta+1-\beta_0)\big]\Big),\quad D^{\rm mark}=\Big(\frac1{\tau_1^2}+\frac1{\tau_2^2}\Big)\frac{\sum_\rho b_0\bar B}{\beta_0^2}\big[1+O(\eta)\big].\qquad\text{(7.5)}
```
This is (6.8) with $`s_c=+1`$ and $`c_i=\tau_i`$, the full-grip speeds of (5.7), plus the flux remainder of (6.6). $`D^{\rm lat}`$ comes from the lattice form of the bands, $`D^{\rm mark}`$ from the mutual term. Each body's inertia counts the part of $`M`$ odd in its own coupling, and at leading order this is all of $`M`$ for each body.

### Step 4. Cost of the bond and inertia against cost (item 3)

With $`f_0`$ real, $`E_b(0)=\sum_rf_0^2U+2\sum_\rho b_0\,t(\rho;0)`$, $`E_i(0)=E_i^{\rm held}+\bar d_i+2\bar\kappa_i`$, $`E^{\rm held}_{\rm pair}(r)=E_1^{\rm held}+E_2^{\rm held}-E_\varnothing+M(r)`$ (definition (4.2)). The partner shifts $`d_i`$ and $`\kappa_i`$ by the relative amount $`-\bar M_i^o/\sigma_iR_i`$ (Step 2), and $`\bar d_i=-2\bar\kappa_i`$, so these shifts cancel up to the factor $`1-\beta_0`$:
```math
\Delta E_0=\langle M\rangle_0+K_0\big[1+O(\eta)\big],\qquad K_0=2\bar t_0(\beta_0-1)=\tfrac14(\mu_1^{-1}+\mu_2^{-1})(1-\beta_0).\qquad\text{(7.6)}
```
**(i)** Since $`(\mu_1+\mu_2)/(\mu_1^{-1}+\mu_2^{-1})=\mu_1\mu_2`$, $`D^{\rm lat}=4\mu_1\mu_2K_0/\beta_0`$; and $`\sum_\rho b_0\bar B/\beta_0^2=\langle M\rangle_0[1+O(\eta,1-\beta_0)]`$. With $`v=\tau_i`$, the speed of (5.7) of either body, and $`j\neq i`$:
```math
D_0-\frac{\Delta E_0}{\tau_i^2}=\frac{4\mu_1\mu_2}{\beta_0}K_0\Big[1-\frac{\beta_0}{4\mu_1\mu_2\tau_i^2}\Big]+\frac{\langle M\rangle_0}{\tau_j^2}\big[1+O(\eta,1-\beta_0)\big],\qquad\lvert4\mu_1\mu_2\tau_i^2\rvert=\frac{(2n\lvert g_1\rvert)(2n\lvert g_2\rvert)}{\tau_j^2}\ge\frac{d^2}{\tau_j^2}\gg1.\qquad\text{(7.7)}
```
Both terms are nonzero: the lattice part exceeds $`K_0/v^2`$ by the factor $`\ge d^2/\tau_j^2`$, and the mark part exceeds $`\langle M\rangle_0/v^2`$ by $`\langle M\rangle_0/\tau_j^2`$. Both terms have the sign of $`D^{\rm lat}`$ when $`g_1g_2<0`$ ($`\mu_1\mu_2K_0>0`$, $`\langle M\rangle_0>0`$), so then (i) never holds; for $`g_1,g_2>0`$ it holds only on the surface where the two terms cancel, a tuned relation between $`1-\beta_0`$ and $`\eta`$. Elsewhere, no.

**(ii)** In S5, $`D^{\rm lat}\ll\lvert D^{\rm mark}\rvert`$, and by (7.7) $`\lvert K_0\rvert\le\lvert D^{\rm lat}\rvert/\lvert4\mu_1\mu_2\rvert\ll2\tau_{\max}^2d^{-2}\lvert\langle M\rangle_0\rvert`$, so $`\Delta E_0=\langle M\rangle_0`$ at leading order and
```math
D_0=\Big(\frac1{\tau_1^2}+\frac1{\tau_2^2}\Big)\Delta E_0\Big[1+O\Big(\eta,\frac{1-\beta_0}\eta,\frac{\tau^2}{d^2}\Big)\Big];\qquad\text{equal speeds }\tau_1=\tau_2=v:\ D_0=\frac{2\Delta E_0}{v^2}.\qquad\text{(7.8)}
```
The binding cost has inertia, but $`(\tau_1^{-2}+\tau_2^{-2})\Delta E_0\ne\Delta E_0/\tau_i^2`$: the mutual term is odd in both couplings, so it enters both half-gaps (7.3) but the cost only once. It approaches $`\Delta E_0/\tau_i^2`$ only for $`\tau_i/\tau_j\to0`$, with relative deviation $`\tau_i^2/\tau_j^2`$.

### Step 5. Weight and fall (item 4)

*Weight of the selected level.* The source enters (2.10) through the held levels at first order in $`g_s`$, so (6.13) carries over: $`W_0'=\sum_rf_0^2(\partial_1+\partial_2)W_{\rm pair}`$ plus the kinetic part. By (7.3) with the source in place of the partner, $`\kappa_i,d_i`$ change by the relative amount $`-\phi`$ ($`M^o_{is}=ng_i\phi`$). So the kinetic energies weigh $`-(\text{kinetic energy})\,\phi'`$, and the bond part of this is $`-K_0\phi'`$; all such terms are relative $`O(\tau^2/d^2)`$ against $`ng\phi'`$.

*Lattice identities.* For $`1\le x\le L-1`$: $`\ell'(x)=-\frac12(1-\frac{2x}L)`$; $`(\ell^2)'=(2\ell+\frac1L)\ell'`$ (as $`\Lambda\ell=-\frac1L`$ there); and since $`\Lambda\ell^{(2)}=\ell`$, $`\ell^{(2)}`$ is even about $`0`$ and $`L/2`$, the cubic $`-\frac{Lx}{12}+\frac{x^2}4-\frac{x^3}{6L}=\frac{x(L-x)}{6}\ell'(x)`$ is $`(\ell^{(2)})'`$. Inserting these into the derivative of $`2\ell_0\ell+\ell^2-\frac2L\ell^{(2)}`$ in (4.5) gives $`4\ell_0\kappa_s\ell'`$ with $`\kappa_s`$ below, and $`\phi'=-\frac{2g_s}{t_f}\ell'`$:
```math
W_i'(X)=\phi'\big[ng_i+2\kappa_sC_i^{(2)}\big],\qquad C_i^{(2)}:=-\frac{ng_i^2\ell_0}{t_f},\qquad\kappa_s:=\frac{L^2(1-2u)^2+2}{L^2-1}=(1-2u)^2+O(L^{-2}),\qquad\text{(7.9)}
```
up to relative $`O(\eta^2)`$. $`C_i^{(2)}`$ is the second-order even part of the cost; it is weighed with $`2\kappa_s`$ but has no inertia by (5.3).

*Bond.* In (4.7) at $`x_{1,2}=X\mp r/2`$: $`f_0`$ is even in $`r`$ at $`P=0`$ (as $`V`$ and $`\kappa_i`$ are), so $`\langle r\rangle_0=0`$; $`W_b(X;r)-W_b(X;0)=V(r)\phi(X)`$ up to $`O(r^2/(Ls))`$; and $`W_b(X;0)`$ is (4.5) with $`g_i^2\to2g_1g_2`$. So, with the kinetic part,
```math
W_b':=W_0'-W_1'-W_2'=\phi'\big[2\kappa_sB(0)+\langle V\rangle_0-K_0\big]\big[1+O(\eta/\kappa_s)\big].\qquad\text{(7.10)}
```
*Fall factors.* By (5.14), (6.13), $`\Gamma_i:=E_i''(0)W_i'=W_i'/\mu_i`$ and $`\Gamma_{\rm pair}:=E_b''(0)W_0'`$ set the acceleration from rest $`-\Gamma`$ of a smooth start. With $`\Gamma_b:=W_b'/D_0`$ and $`1/E_b''=\mu_1+\mu_2+D_0`$, exactly,
```math
\Gamma_{\rm pair}=\frac{\mu_1\Gamma_1+\mu_2\Gamma_2+D_0\Gamma_b}{\mu_1+\mu_2+D_0},\qquad\Gamma_i=\tau_i^2\phi'\Big[1-\frac{2\kappa_sg_i\ell_0}{t_f}+O\Big(\eta^2,N_f\eta^2,\frac{\tau^2}{d^2}\Big)\Big].\qquad\text{(7.11)}
```
*Leading order.* $`W_b'`$ and $`D^{\rm mark}`$ are $`O(\eta)`$; the lattice inertia has weight $`-K_0\phi'=-\beta_0D^{\rm lat}\phi'/(4\mu_1\mu_2)`$, which is $`O(\tau^2/d^2)`$ against $`\tau^2\phi'D^{\rm lat}`$. Hence $`\Gamma_{\rm pair}=\beta_0\bar\Gamma[1+O(\eta,\tau^2/d^2)]`$ with $`\bar\Gamma:=\frac{\mu_1\Gamma_1+\mu_2\Gamma_2}{\mu_1+\mu_2}=\frac{\mu_1\tau_1^2+\mu_2\tau_2^2}{\mu_1+\mu_2}\phi'[1+O(\eta)]`$. So $`\Gamma_{\rm pair}=\Gamma_1=\Gamma_2`$ at leading order (with $`1-\beta_0\to0`$) iff $`\tau_1=\tau_2`$. For $`\tau_1\ne\tau_2`$ the bodies already fall differently; $`1-\beta_0`$ lowers the pair's fall, since the internal kinetic energy has inertia but no weight at this order.

*Order of the mutual term (S5).* By (7.10), (7.5), (7.8),
```math
\Gamma_b=\frac{2\kappa_s\,\phi'}{\tau_1^{-2}+\tau_2^{-2}}\Big[1+O\Big(\frac\eta{\kappa_s},\frac{1-\beta_0}\eta,\frac wL,\frac{\tau^2}{d^2}\Big)\Big],\qquad \Gamma_{\rm pair}-\bar\Gamma\overset{\tau_1=\tau_2=\tau}{=}4(1-\kappa_s)\frac{g_1g_2\ell_0}{t_f(g_1+g_2)}\tau^2\phi'.\qquad\text{(7.12)}
```
For equal speeds the bond's weight and inertia both carry the factor 2 of (7.8). The weight also carries $`\kappa_s=1-\frac{4s(L-s)-3}{L^2-1}<1`$ for $`1\le s\le L/2`$, so $`\Gamma_b=\kappa_s\tau^2\phi'`$ against $`\Gamma_i=\tau^2\phi'`$ at leading order. The binding cost is weighed in the same proportion as its inertia only in the limit $`u\to0`$ ($`w\ll s\ll L`$), where $`\Gamma_b/\Gamma_i=1-4u+O(u^2,w/L,\eta)`$. For $`\tau_1\ne\tau_2`$, $`\Gamma_b\ne\Gamma_i`$ already because $`2/(\tau_1^{-2}+\tau_2^{-2})\ne\tau_i^2`$. The second equation of (7.12) is the first order of the difference, from (7.11) with $`D_0\simeq2B(0)/\tau^2`$, $`\Gamma_b-\bar\Gamma\simeq(\kappa_s-1)\tau^2\phi'`$, $`\mu_1+\mu_2\simeq n(g_1+g_2)/\tau^2`$. Besides this, $`\bar\Gamma-\Gamma_i=O(\eta)`$ for $`g_1\ne g_2`$ from the self terms of (7.11).

### Step 6. The hopping of the field (item 5)

At fixed $`n,\gamma_i,M_i,\tau_i`$ (so fixed $`g_i`$, $`\mu_i`$) and leading order: $`B,\langle M\rangle_0,D^{\rm mark},W_b'/\phi'\propto t_f^{-1}`$; $`F\propto t_f^{-1}`$, so $`w\propto t_f^{1/3}`$, and for $`w\gg1`$, $`1-\beta_0\propto t_f^{-2/3}`$, $`K_0,\langle V\rangle_0,D^{\rm lat}\propto t_f^{-2/3}`$; $`\phi'\propto g_s/t_f`$, $`\Gamma_i/\phi'`$ and $`\mu_i`$ are independent of $`t_f`$. Hence
```math
\frac{D^{\rm lat}}{\lvert D^{\rm mark}\rvert}\propto t_f^{1/3},\qquad \frac{D^{\rm mark}}{\Delta E_0}\to\frac1{\tau_1^2}+\frac1{\tau_2^2},\quad \frac{\Gamma_b}{\Gamma_i}\to\frac{2\kappa_s}{1+\tau_i^2/\tau_j^2}\quad\text{independent of }t_f.\qquad\text{(7.13)}
```
A stiffer field weakens the bond ($`\propto t_f^{-1}`$) and widens it, and S5 lies at the small-$`t_f`$ end, bounded by $`\eta\propto t_f^{-1}\ll1`$ and by $`\varepsilon_1\propto t_f`$ in S2. No value of $`t_f`$ restores the proportions of (7.8) and (7.12).

## Result

Class: full grip for both bodies, $`N_f\ge1`$, even $`L\ge6`$, S1–S4 (S5, S6 where stated), without the tuned cases.
- **(7.1)** Definitions: half-gap $`\sigma_iR_i`$, $`c_i^2=\sigma_iR_i/\mu_i=\tau_i^2[1+O(N_f\eta^2)]`$, the part $`M_i^o`$ of the mutual term odd in $`g_i`$, and the bond average $`\bar f`$.
- **(7.2), (7.3)** Under S2, S3 the band contract is (2.10)/(6.1) with gaps (7.2). Each body's local inertia is $`m_i(\rho)=\mu_i+\bar M_i^o(\rho)/c_i^2+O(\lvert\mu_i\rvert\eta^2)=\mu_i+\bar B(\rho)/\tau_i^2\,[1+O(\eta)]`$. (6.5), (6.6) hold for the full grip. Control: coupling (c) has the opposite sign of the mark part ($`s_c=-1`$ in (6.8)).
- **(7.4)** The selected level is bound at $`r\approx0`$ iff $`\tau_1^2g_2+\tau_2^2g_1>0`$: lowest if both $`g_i>0`$, highest for opposite signs, never for both $`g_i<0`$. Otherwise it sits at $`r\approx L/2`$ (control).
- **(7.5)** $`D_0=1/E_b''(0)-\mu_1-\mu_2=D^{\rm lat}+D^{\rm mark}`$ to $`O((\lvert\mu_1\rvert+\lvert\mu_2\rvert)[\eta^2+\frac{\tau^2}{d^2}(\eta+1-\beta_0)])`$ and the ring remainder. $`D^{\rm lat}=(\mu_1+\mu_2)(1-\beta_0)/\beta_0`$, and $`D^{\rm mark}=(\tau_1^{-2}+\tau_2^{-2})\beta_0^{-2}\sum_\rho b_0\bar B\,[1+O(\eta)]`$ is (6.8) with $`s_c=+1`$, $`c_i=\tau_i`$.
- **(7.6)** $`\Delta E_0=\langle M\rangle_0+K_0[1+O(\eta)]`$, $`K_0=\frac14(\mu_1^{-1}+\mu_2^{-1})(1-\beta_0)`$.
- **(7.7)** Item 3 (i), negative: $`D_0\ne\Delta E_0/v^2`$ for $`v=\tau_1`$ or $`\tau_2`$. The lattice part is $`4\mu_1\mu_2K_0/\beta_0`$, larger than $`K_0/v^2`$ by a factor $`\ge d^2/\tau_j^2`$; the mark part exceeds $`\langle M\rangle_0/v^2`$ by $`\langle M\rangle_0/\tau_j^2`$. Equality holds only on a tuned surface, which exists only for $`g_1,g_2>0`$.
- **(7.8)** Item 3 (ii), negative: in S5, $`D_0=(\tau_1^{-2}+\tau_2^{-2})\Delta E_0[1+O(\eta,(1-\beta_0)/\eta,\tau^2/d^2)]`$, i.e. $`2\Delta E_0/v^2`$ for $`\tau_1=\tau_2=v`$. It approaches $`\Delta E_0/\tau_i^2`$ only as $`\tau_i/\tau_j\to0`$.
- **(7.9), (7.10)** In S6: $`W_i'=\phi'[ng_i+2\kappa_sC_i^{(2)}]`$ up to relative $`O(\eta^2)`$, $`\kappa_s=(L^2(1-2u)^2+2)/(L^2-1)`$; $`W_b'=\phi'[2\kappa_sB(0)+\langle V\rangle_0-K_0][1+O(\eta/\kappa_s)]`$.
- **(7.11)** Exact: $`\Gamma_{\rm pair}=(\mu_1\Gamma_1+\mu_2\Gamma_2+D_0\Gamma_b)/(\mu_1+\mu_2+D_0)`$, and $`\Gamma_i=\tau_i^2\phi'[1-2\kappa_sg_i\ell_0/t_f+O(\eta^2,N_f\eta^2,\tau^2/d^2)]`$. At leading order $`\Gamma_{\rm pair}=\beta_0\bar\Gamma`$, equal to $`\Gamma_1=\Gamma_2`$ (for $`1-\beta_0\to0`$) iff $`\tau_1=\tau_2`$. Control: $`\tau_1\ne\tau_2`$.
- **(7.12)** In S5, S6: $`\Gamma_b=2\kappa_s\phi'/(\tau_1^{-2}+\tau_2^{-2})`$ to the orders stated. For $`\tau_1=\tau_2`$ the binding cost is weighed in the same proportion as its inertia only as $`u\to0`$; at finite $`u`$ it is weighed less, by $`\kappa_s<1`$, and $`\Gamma_{\rm pair}-\bar\Gamma=4(1-\kappa_s)g_1g_2\ell_0\tau^2\phi'/(t_f(g_1+g_2))`$. Control: any $`u>0`$ (e.g. $`u=1/4`$).
- **(7.13)** At fixed $`n,\gamma_i,M_i,\tau_i`$: mark quantities $`\propto t_f^{-1}`$, lattice quantities $`\propto t_f^{-2/3}`$ ($`w\gg1`$), and $`D^{\rm mark}/\Delta E_0`$, $`\Gamma_b/\Gamma_i`$ are independent of $`t_f`$ at leading order.

## Consistency checks

1. **Dimensions.** $`g,\tau,t_f,M,K_0`$ are energies (rates in $`\lambda`$); $`P,r,u,\phi,\kappa_s`$ are dimensionless. So $`\mu,D`$ are inverse energies, and (7.3), (7.5), (7.7), (7.8) are consistent ($`M/\tau^2`$, $`\mu_1\mu_2K_0`$). $`\Gamma=E''W'`$ and $`\tau^2\phi'`$ are both energy squared per place.
2. **$`g_2\to0`$** (no binding): $`B,M_i^o,W_b',D^{\rm mark}\to0`$ linearly, (7.3) gives $`m_1\to\mu_1`$, $`F\to0`$ so $`w\to\infty`$ (S4 fails, as it must), and (7.9) is the single-body weight of (4.5).
3. **Coincident held pair $`r=0`$** ($`\langle V\rangle_0=K_0=0`$). (7.9) plus (7.10) give $`\phi'[n(g_1+g_2)+2\kappa_s(C_1^{(2)}+C_2^{(2)}+B(0))]=\phi'[nG+2\kappa_sC_G^{(2)}]`$, $`G=g_1+g_2`$, as must hold: two point couplings at one place are one coupling $`G`$.

## Open issues

- The code check has $`N_f=1`$, so S5 is reached only moderately ($`D^{\rm lat}/\lvert D^{\rm mark}\rvert=0.21`$ at $`L=128`$, $`\eta=0.15`$). The $`O(\eta)`$ corrections have large coefficients ($`\langle M_1^o+M_2^o\rangle_0/\langle M\rangle_0=2.11`$ at $`\eta=0.05`$, $`2.40`$ at $`\eta=0.15`$).
- The kinetic weight $`-K_0\phi'`$ in (7.10) is derived, not checked: the code uses held weights.
- The fall itself (time evolution) is not simulated; $`\Gamma`$ is taken from (5.14), (6.13).
- $`\kappa_s`$ is a property of the ring (zero mode). Other geometries are out of scope (tori).
- $`c_i^2=\tau_i^2[1+O(N_f\eta^2)]`$ is an estimate of the overlap corrections of (5.3), not derived in detail.

## Code

- `code/v1/check_pair_full_grip.py` (role: check; $`N_f=1`$, $`t_f=1`$). It builds the exact sector contract of two full-grip bodies and one field object continued in $`P`$ (basis: branches, $`r`$, relative field place), finds the selected level by its overlap with the band contract, and takes $`E_b''(0)`$ by Richardson differences. It builds the band contract (2.10) numerically (Schrieffer–Wolff over the exact held blocks) and compares $`D_0`$ with (7.5), $`m_i(\rho)`$ with (7.3), and $`\Delta E_0`$ with (7.6). It computes weights from exact lowest eigenvalues of the field with held couplings and a held source ($`\pm g_s`$, odd part) against (7.9)–(7.12). Cases: A (equal bodies, $`\eta=0.15`$, $`\tau/d=0.3`$, $`L=32,64`$), A′ ($`\eta=0.05`$, $`L=64`$), A″ ($`\eta=0.05`$, $`\tau/d=0.15`$, $`L=64`$), B (unequal $`g_i`$ and $`\tau_i`$, $`L=32,64`$), R (S5, $`L=128`$), C (opposite signs), D (both negative).
- Outputs: `code/v1/output/check_log.txt` (readable log), `code/v1/output/check_results.json` (all numbers).
- Findings (all from `check_log.txt`):
  - Item 1: the selected levels have overlap $`\ge0.984`$ with the band contract at every $`P`$ used. $`E_b''(0)`$ of (2.10) and of (6.6) agree with each other to about $`10^{-6}`$, and with the exact value to 1.0–4.6%. At $`L=64`$ this difference falls from 2.9% (A) to 1.45% (A′) to 0.99% (A″), with $`\eta`$ and $`\tau/d`$. Case C is bound at the top ($`\langle\lvert r\rvert\rangle=0.14`$). In case D the extreme level sits at the antipode ($`\langle\lvert r\rvert\rangle=21.4`$, $`L=48`$), as (7.4) states.
  - Item 2: (7.3) holds near $`r=0`$ to 2.5% ($`\eta=0.15`$) and 0.26% ($`\eta=0.05`$) in the odd-part form, and to 9–25% and 4.8% in the form with $`\bar B`$. (7.5) reproduces $`D_0`$ of the band contract to 0.1–2% of $`\lvert D^{\rm lat}\rvert+\lvert D^{\rm mark}\rvert`$, and the exact $`D_0`$ to 3–11% of it (the band-versus-exact part).
  - Item 3: $`\Delta E_0`$ agrees with $`\langle M\rangle_0+K_0`$ to 0.7–3.2%. $`(D_0-D^{\rm lat})/\Delta E_0=1.03\,(\tau_1^{-2}+\tau_2^{-2})=2.06/\tau^2`$ in A′. In R (S5), $`D_0/\Delta E_0=1.016\,(\tau_1^{-2}+\tau_2^{-2})`$; there the corrections $`D^{\rm lat}/D^{\rm mark}=-0.21`$ and $`O(\eta)`$ partly cancel.
  - Item 4: $`W_0'`$ agrees with (7.9)+(7.10) (held part) to 0.3–7%, and $`\Gamma_i/\phi'`$ with (7.11) to 2–4% (R). $`W_b'/[(D_0-D^{\rm lat})\phi']`$ agrees with $`2\kappa_s/(\tau_1^{-2}+\tau_2^{-2})`$ to 7–20% (A′, R), within $`O(\eta/\kappa_s,w/s)`$. In R, $`\Gamma_b/\Gamma_1=0.76`$ at $`u=1/8`$ and $`0.40`$ at $`u=1/4`$ ($`\kappa_s=0.56,0.25`$): the bond is weighed below the single bodies' proportion, and more so at larger $`u`$. In case B ($`\tau_1\neq\tau_2`$) $`\Gamma_1/\phi'`$ and $`\Gamma_2/\phi'`$ differ by a factor 3.6–3.7, as (7.11) states.

## Methods used

- Rayleigh–Schrödinger and Schrieffer–Wolff perturbation theory
- Bloch sectors of the joint translation, band contract
- Hellmann–Feynman theorem, Perron–Frobenius
- Lattice Green function on the ring (pseudo-inverse of the Laplacian)
- Continuum limit of the relative motion (linear potential)
- Exact diagonalization, shift-invert Lanczos, Richardson extrapolation (code)
