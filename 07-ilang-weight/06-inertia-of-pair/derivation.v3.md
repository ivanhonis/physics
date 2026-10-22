# Inertia of a pair bound through the field

- **Subproject:** 07-ilang-weight
- **Package:** 06-inertia-of-pair
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-21

## Changes from previous version

- Scope (note of 2026-10-21 in question.md): items 2–5 now concern only the selected level ($`\nu=0`$, $`s_\beta=+1`$). Alternating extreme levels and excited levels are reduced to one sentence in Step 2 and one open issue. Affects Steps 2–7, Result and checks 2, 3. Reason: the note; I2, I5, excited-level part of I1.
- Setup: B2 replaced by the no-cancellation condition $`\bar x\ll1`$ on the pair inertia, which implies the inverse-expansion condition. Reason: I1.
- Step 2: (6.3) states when the selected level is bound ($`s_\beta=+1`$) and that $`f_0>0`$ on every relative ring; (6.4) is restricted to that level. Reason: note, I5.
- Step 3: $`b_0>0`$, $`0<\beta_0<1`$; zeros of the curvature are located through $`\sum_\rho b_0/m`$. Reason: I1.
- Step 4: (6.8) is derived under B2, with remainders $`O(\bar x^2)`$ and $`O(\varepsilon^3/\beta_0)`$; outside B2 the unexpanded (6.6) is kept; level dependence is given for the two classes. Reason: I1, note.
- Step 5: (6.17) is stated for the selected level; the equality family gets the spectral hierarchy (H) and a window for $`\tau/M`$, and is stated as unverified in the full contract; the comparison between levels is removed. Reason: I3, I2, note.
- Step 6: (6.14) now has an additive error, with the relative form only under non-cancellation (N), and the case $`g_1+g_2=0`$ treated separately; (6.13) is qualified accordingly. Reason: I4.
- Step 7, (6.15): $`s_\beta`$ removed; the $`t_f`$-dependence of B2 added. Reason: I2, I1.
- Code: set C (alternating) and the level $`\nu=1`$ of the sign rule removed. Set D added ($`\sigma_i=-1`$, $`g_1+g_2=0`$). New outputs: $`\bar x`$, $`A_0`$, the sign of $`f_0`$, expanded against unexpanded inverse curvature, and the acceleration of set D against a single body. Reason: note, I1, I4.

## Response to verification

- **I1:** Accepted and fixed in the Setup (B2) and in Steps 3 and 4. The inverse expansion needs $`\lvert A_0\rvert\ll\lvert m_0\rvert\beta_0`$. Since $`b_0>0`$ for the selected level, this follows from $`\bar x=\max_\rho\lvert m(\rho)-m_0\rvert/\lvert m_0\rvert\ll1`$ (new B2), which by (6.7) also controls cancellation of $`\mu_1+\mu_2`$. (6.8) and its consequences ((6.10), (6.14), (6.15), (6.17)) are restricted to B2. Outside B2 the unexpanded $`1/\sum_\rho b_0/m`$ is kept, and curvature zeros are located through it. The excited-level part (zeros of $`\beta_\nu`$) is settled by the note: excited levels are out of scope for items 2–5.
- **I2:** Accepted and settled by the note. Levels with $`s_\beta=-1`$ are out of scope for items 2–5, and Steps 4–7 now concern only $`s_\beta=+1`$. There $`K_0=2\bar t_0(\beta_0-1)`$ has no finite offset, $`\lvert K_0\rvert=\lvert\bar t_0\rvert\frac{a_0}34^{1/3}\chi^{2/3}`$, and $`D^{\rm lat}_0\to0`$ as $`t_f^{-2/3}`$; the locus (6.17)(ii) uses only this case.
- **I3:** Accepted and fixed in Step 5. The family now has $`\tau/M=\varepsilon^{1/2}`$, inside a window bounded below by the hierarchy (H): the width of $`\mathcal G`$ is $`\simeq0.81M\chi^{2/3}`$, the first field excitation $`\simeq0.24T\tau^2/M`$, and their ratio is $`\simeq55\varepsilon^{3/2}/T^3\to0`$. Hence $`\delta\simeq\omega_1`$. The remainders of the quoted inputs are stated at fixed $`n,L,t_f`$ and are not shown to be uniform along the family, so the equality is stated as unverified in the full contract; only the zero of the leading-order $`\Delta_0`$ is claimed.
- **I4:** Accepted and fixed in Step 6. (6.14) has an additive $`O(\beta_0\varepsilon^2g_s/\lvert\mu_1+\mu_2\rvert)`$ error. The relative form holds only under (N), $`\lvert g_1+g_2\rvert\gg\varepsilon\max_i\lvert g_i\rvert`$. For $`g_1+g_2=0`$: $`\Pi_0`$ is of second order and so differs from each $`\Pi_i`$ at first order. Its second-order value is not determined, nor is the factorized form of (6.13) at that order; the code (set D) shows the latter off by a factor of about 2.
- **I5:** Accepted and settled by the note. Alternating levels are out of scope, and Step 2 claims sign alternation only near contact. The one-sign statement for the selected level holds on every relative ring, including odd ones ($`L\equiv2`$ mod 4): all bonds have one sign, so Perron–Frobenius applies without gauge or frustration.

## Setup and assumptions

**Setting (assumptions, M8, M9).** As in question.md: $`N_f\ge1`$ field objects ($`c=+1`$) on a ring of even $`L\ge6`$ places with own term $`C_1=-t_f\sum_x(\lvert x\rangle\langle x+1\rvert+{\rm h.c.})`$, $`\Phi_x`$ the number at $`x`$, $`n=N_f/L`$; two Model D bodies $`b_1,b_2`$ of different types, clock levels $`k_i`$ with half-gaps $`M_i`$, branches $`\sigma_i`$, coupled by (a) or (c) with constants $`\gamma_i`$, $`g_i:=\sigma_i\gamma_iM_i`$, no pair term between them, records at $`\kappa\to0`$; the field in its lowest state adapted to the bodies; regime R (R1, R2) as stated there. Order counting: $`\varepsilon:=\max_i\lvert\gamma_i\rvert`$ ($`g_i=O(\varepsilon)`$). Speeds of (2.14): $`c_i=\tau_i`$ (a), $`c_i=\tau_i(1+\gamma_in)`$ (c); $`s_c:=+1`$ (a), $`-1`$ (c).

**Inputs** (verbatim in question.md). From 07-ilang-weight/02-two-free-bodies: the joint translation $`\mathcal T=e^{-i\hat P}`$, $`[\mathcal T,C]=0`$ (2.1); $`E(x_1,x_2)=\sigma_1M_1+\sigma_2M_2+N_f\varepsilon_0(x_1,x_2)`$ (2.3); the band contract $`H_{\rm eff}=W+K_1+K_2+O(\tau^4)`$, $`W={\rm diag}\,E(j,l)`$ (2.10), $`K_i`$ moving $`b_i`$ by $`0,\pm2`$; $`E''_{k_1,\sigma_1}(0)=-8\bar\kappa`$ (2.11), hence $`\mu_i=-1/(8\bar\kappa_i)`$; $`\mu_i=\sigma_iR_i/c_i^2+O(\gamma_i^2)`$ with $`R_i=M_i(1+\gamma_in)+O(\gamma_i^3)`$ (2.14); $`\delta\kappa(j,l)/\bar\kappa=\mp\gamma_1\overline{\delta\rho}_l(j)+r_1`$, $`\gamma_1\delta\rho_l(y)=\sigma_1M^{(2)}(y,l)/M_1+O(\gamma_1g_2^2)`$, $`r_1=O(\varepsilon^3)`$ (2.16), upper sign (a). From 06-ilang-source/04-profile: $`M=N_f[\varepsilon_0(g_1,g_2)-\varepsilon_0(g_1,0)-\varepsilon_0(0,g_2)+\varepsilon_0(0,0)]`$ (4.2). From 06-ilang-source/07-dressed-fall: $`a_{k,\sigma}(0)=-E''_{k,\sigma}(0)\sum_j\phi_{j+1}\phi_{j-1}W'_{k,\sigma}(j)+O(g_s^2)+O(\tau^4\gamma g_s)`$ (7.7). From 07-ilang-weight/04-weight-of-bond: $`\ell(r)=\frac{L^2-1}{12L}-\frac{r(L-r)}{2L}`$ and $`E(r)-E(r')=\frac{ng_1g_2}{t_fL}[r(L-r)-r'(L-r')]+O(n\lvert g_1g_2\rvert\ell_0\eta/t_f)`$ (4.3); $`W_i(x)=ng_i\phi(x)+O(\varepsilon^2g_s)`$ with $`\phi(x)=-\frac{2g_s}{t_f}\ell(x-x_s)`$ (4.5); $`W_{\rm pair}=W_1(x_1)+W_2(x_2)+W_b`$ with $`W_b`$ (4.7).

**Notation.** $`\bar t_0:=\bar\kappa_1+\bar\kappa_2=-\tfrac18(\mu_1^{-1}+\mu_2^{-1})`$; $`m_0:=\mu_1+\mu_2`$; $`S:=c_1^{-2}+c_2^{-2}`$; $`F:=n\lvert g_1g_2\rvert/t_f`$; binding ratio $`\chi:=F/\lvert\bar t_0\rvert`$; signs $`s_e:={\rm sgn}(g_1g_2)`$, $`s_\mu:={\rm sgn}(\mu_1^{-1}+\mu_2^{-1})=-{\rm sgn}\,\bar t_0`$, $`s_\beta:=s_es_\mu`$; $`c_{\min}`$, $`c_{\max}`$ the smaller and the larger of $`c_1,c_2`$; $`E_i(P)`$ the band level of $`b_i`$ alone with the field, $`E_\varnothing`$ the lowest eigenvalue of the field alone.

**Binding regime B (assumption).**
- B1: the selected level (Step 2) decays on a scale $`\xi_0\ll L`$; this needs $`\chi L^3\gg1`$, with $`\xi_0\simeq(4/\chi)^{1/3}`$ for $`\chi\lesssim1`$ and $`\xi_0\simeq1`$ for $`\chi\gtrsim1`$.
- B2 (no cancellation of the pair inertia): $`\bar x:=\max_\rho\lvert m(\rho)-m_0\rvert/\lvert m_0\rvert\ll1`$, with $`m(\rho)`$ of (6.5).
  - By (6.7) it holds if $`S\max_\rho\lvert\bar M^{(2)}(\rho)\rvert\ll\lvert\mu_1+\mu_2\rvert`$ and $`\varepsilon^3(\lvert\mu_1\rvert+\lvert\mu_2\rvert)\ll\lvert\mu_1+\mu_2\rvert`$.
  - For $`\sigma_1=\sigma_2`$ it holds when $`\lvert M^{(2)}(0)\rvert\ll\min_iR_i`$. For $`\sigma_1=-\sigma_2`$ it fails near $`\mu_1+\mu_2=0`$.
  - It implies that the relative hopping $`t(\rho;0)=-m(\rho)/(8m_1(\rho)m_2(\rho))=\bar t_0(1+O(\bar x,\varepsilon^2))`$ does not cancel on any bond.
- B3: $`\beta_0\gg\tau'^2/(\delta_1\delta)`$, with $`\beta_0`$ of (6.5), so that the order-$`\tau^4`$ terms dropped by R2 stay small (Step 3).
- B4 (ring hierarchy): the ring remainder $`\rho_L`$ of (6.16) is small against every retained relative term: $`\lvert\rho_L\rvert\ll1-\beta_0`$ for the leading statements, and $`\lvert\rho_L\rvert\ll\lvert M^{(2)}(0)\rvert/R_i`$ where the mark terms are kept.

**Class.** Item 1: couplings (a), (c), $`N_f\ge1`$, even $`L\ge6`$, all branch combinations, both signs of $`\gamma_1\gamma_2`$, under R and $`\chi L^3\gg1`$. Items 2–5: the descriptions of this class in which the selected level is bound ($`s_\beta=+1`$, (6.3)), under R and B. Results are at order $`\tau_i^2`$ in the band contract and, unless stated otherwise, at leading order in $`\varepsilon`$ at fixed $`\chi`$.

## Derivation

### Step 1. The band contract in a sector of $`P`$

By (2.1) the group $`\mathcal G`$ and (2.10) are invariant under $`\mathcal T`$; take every held field state $`\Omega_{jl}`$ real (lowest state of a real symmetric contract) and $`\Omega_{j+1,l+1}`$ the translate of $`\Omega_{jl}`$. Then $`E(j,l)=E(l-j)`$, and with $`\rho:=l-j`$ define $`\kappa_1(\rho):=\langle e_{j+1,l}\vert K_1\vert e_{j-1,l}\rangle`$ (the $`\kappa(j,l)`$ of (2.16)), $`\kappa_2(\rho):=\langle e_{j,l+1}\vert K_2\vert e_{j,l-1}\rangle`$, and $`d_i(r)`$ the diagonal of $`K_i`$. They are real: two motion terms give $`(\mp i\sigma_1)(\mp i\sigma_1)`$ or $`\sigma_1^2`$, and field overlaps and denominators are real. They are even in $`\rho`$: the reflection $`x\to-x`$ of all places times $`\sigma_3`$ on both bodies maps $`A\to A`$, $`B\to B`$ and (a), (c) into themselves. By (2.16) and its $`1\leftrightarrow2`$ form, $`\kappa_i(\rho)=\bar\kappa_i(1+O(\varepsilon^2))`$; the same energy-denominator argument gives $`d_i(r)=\bar d_i(1+O(\varepsilon^2))`$. A $`\mathcal T`$-eigenstate with $`\mathcal T\psi=e^{-iP}\psi`$ is $`\psi(j,l)=e^{iPj}g(l-j)`$, and $`H_{\rm eff}`$ acts on $`g`$ as
```math
(h_Pg)(r)=U(r)g(r)+t(r+1;P)\,g(r+2)+t(r-1;P)^*g(r-2),\qquad t(\rho;P):=\kappa_1(\rho)e^{-2iP}+\kappa_2(\rho),\qquad U:=E+d_1+d_2. \qquad\text{(6.1)}
```
Each $`K_i`$ moves its body by an even number of places, so $`r`$ even and $`r`$ odd form two separate rings of $`L/2`$ sites. (6.1) is defined for every real $`P`$: it is the sector contract with body 1 as representative, continued in $`P`$ (the continuation used throughout and in the code). $`E_b(P)`$ is an eigenvalue of $`h_P`$.

### Step 2. Bound levels and the selected level (item 1)

By (2.3) and (4.2), $`E(r)=E_1^{(0)}+E_2^{(0)}-E_\varnothing+M(r)`$, $`E_i^{(0)}`$ the $`\tau=0`$ level of $`b_i`$ alone with the field. Second-order perturbation of $`\varepsilon_0`$ (one-object ground state $`L^{-1/2}\sum_x\lvert x\rangle`$, excitation energies $`2t_f(1-\cos q)`$) gives the mixed term $`-2g_1g_2\ell(r)/(t_fL)`$, consistent with (4.3):
```math
M(r)=M^{(2)}(r)+O\big(n\lvert g_1g_2\rvert\ell_0\eta/t_f\big),\quad M^{(2)}(r)=-\frac{2ng_1g_2}{t_f}\ell(r),\quad U(r)-U(0)=V(r)+O\big(n\lvert g_1g_2\rvert\ell_0\eta/t_f\big)+O(\varepsilon^2\lvert\bar\kappa\rvert),\quad V(r):=\frac{ng_1g_2}{t_fL}\,r(L-r). \qquad\text{(6.2)}
```
$`V`$ is even and monotone in $`\lvert r\rvert`$ on $`[0,L/2]`$. Near $`r=0`$ it rises like $`F\lvert r\rvert`$ for $`g_1g_2>0`$ (a well) and falls like $`-F\lvert r\rvert`$ for $`g_1g_2<0`$ (a hill).

*Criterion of localization:* the real eigenvector $`f`$ of $`h_0`$ decays away from $`r=0`$ on a scale $`\xi\ll L`$, so that its weight near $`r=L/2`$ is exponentially small in $`L/\xi`$ (B1).

The uniform relative band is $`2\bar t_0\cos2k`$. Its edge at $`k=0`$, where both bodies are near $`p_i=0`$ (near rest), is the bottom for $`s_\mu=+1`$ (positive relative inertia) and the top for $`s_\mu=-1`$. *Selected level* (item 1, note of 2026-10-21): the extreme level at that edge, the lowest if $`s_\mu=+1`$ and the highest if $`s_\mu=-1`$.

On a chain the sign of the hopping is a gauge ($`f(r)\to(-1)^{r/2}f(r)`$). So a well binds levels below the band and a hill above it, for either sign of $`\bar t_0`$ (standard for one-dimensional chains), and the level near the opposite extremum $`r=L/2`$ fails the criterion. The selected level is therefore bound iff a well sits at the bottom with $`s_\mu=+1`$ or a hill at the top with $`s_\mu=-1`$, i.e. iff $`s_e=s_\mu`$. Then every bond $`t(\rho;0)`$ of each sublattice ring has the sign of $`\bar t_0`$ (B2). $`-s_\mu h_0`$ is irreducible on the ring with nonnegative off-diagonal elements, so Perron–Frobenius gives an extreme eigenvector $`f_0>0`$ on the whole ring, for every even $`L`$, without gauge or frustration. With $`g_1g_2=\sigma_1\sigma_2\gamma_1\gamma_2M_1M_2`$:
```math
\text{bound levels: the lowest if }\sigma_1\sigma_2\gamma_1\gamma_2>0,\ \text{the highest if }<0;\qquad\text{selected level bound}\iff s_\beta:=s_es_\mu=+1,\ \text{and then }f_0>0. \qquad\text{(6.3)}
```
Examples:
- $`\sigma_i=+1`$ ($`\mu_i>0`$): the selected level is the lowest and is bound for $`\gamma_1\gamma_2>0`$.
- $`\sigma_i=-1`$ ($`\mu_i<0`$): it is the highest and is bound for $`\gamma_1\gamma_2<0`$.
- $`\sigma_1=-\sigma_2`$: $`s_\mu`$ is the sign of the $`\mu_i`$ of smaller modulus.

For $`s_\beta=-1`$ the bound levels lie at the other edge, with an envelope that alternates in sign near contact (bodies near $`p_1=-p_2=\pm\pi/2`$). They, and the excited bound levels (with nodes), are named here only: items 2–5 concern the selected level.

With uniform hopping and the ring flux dropped (B1), the gauge leaves the magnitude $`\lvert\bar t(P)\rvert=(\bar\kappa_1^2+\bar\kappa_2^2+2\bar\kappa_1\bar\kappa_2\cos2P)^{1/2}`$. With $`E_i(0)=E_i^{(0)}+\bar d_i+2\bar\kappa_i`$ the selected level is
```math
E_b(P)=E_1(0)+E_2(0)-E_\varnothing+M(0)-2\bar t_0+s_e\Big[-2\lvert\bar t(P)\rvert+a_0\big(4\lvert\bar t(P)\rvert F^2\big)^{1/3}\Big],\qquad s_e:={\rm sgn}(g_1g_2), \qquad\text{(6.4)}
```
for $`s_\beta=+1`$ and $`F\ll\lvert\bar t(P)\rvert`$ (weak binding), up to relative corrections $`O(\chi^{2/3})`$ and $`O(\xi_0/L)`$. Reason: the continuum limit of the chain, $`-4\tau_hf''+F\lvert r\rvert f=(\epsilon+2\tau_h)f`$ with $`\tau_h=\lvert\bar t(P)\rvert`$, has its extreme level at $`a_0`$ in units of $`(4\tau_hF^2)^{1/3}`$, where $`a_0=1.0188`$ is the first zero of $`{\rm Ai}'`$ (even ground state). This holds for both classes ($`r`$ even, $`r`$ odd), which differ at $`O(\chi^{2/3})`$. Outside weak binding $`E_b(P)`$ is an eigenvalue of (6.1).

### Step 3. Curvature of the bound level (item 2)

Let $`f_0`$ be the real normalized eigenvector of $`h_0`$ for $`E_b(0)`$ of the selected level ($`f_0>0`$ by (6.3)), and
```math
b_0(\rho):=f_0(\rho-1)f_0(\rho+1),\qquad\beta_0:=\sum_\rho b_0(\rho),\qquad m(\rho):=-\frac1{8\kappa_1(\rho)}-\frac1{8\kappa_2(\rho)}. \qquad\text{(6.5)}
```
$`b_0>0`$. By Cauchy–Schwarz $`\beta_0\le1`$, with equality only if $`f_0(r+2)=f_0(r)`$ for all $`r`$, which B1 excludes; hence $`0<\beta_0<1`$.
1. A gauge $`g(r)\to e^{i\theta(r)}g(r)`$ removes the phases of all bonds of the ring of (6.1) except their sum $`\tilde\Phi(P):=\sum_\rho\arg t(\rho;P)-\sum_\rho\arg t(\rho;0)`$, which is put on one bond. The bond magnitudes become $`s_\rho(P):={\rm sgn}\,t(\rho;0)\,\lvert t(\rho;P)\rvert`$, real. So $`E_b(P)=\epsilon_0(\{s_\rho(P)\},\tilde\Phi(P))`$.
2. $`\lvert t(\rho;P)\rvert^2=t(\rho;0)^2-4\kappa_1\kappa_2\sin^2P`$ is even in $`P`$, so $`s_\rho'(0)=0`$ and $`s_\rho''(0)=-4\kappa_1(\rho)\kappa_2(\rho)/t(\rho;0)`$ (B2: $`t(\rho;0)\neq0`$). $`\tilde\Phi`$ is odd in $`P`$, with $`\tilde\Phi'(0)=\sum_\rho{\rm Im}\,\partial_P\ln t=-2\sum_\rho\kappa_1/(\kappa_1+\kappa_2)`$. $`\epsilon_0`$ is even in $`\tilde\Phi`$ (complex conjugation).
3. Hellmann–Feynman: $`\partial\epsilon_0/\partial s_\rho=2b_0(\rho)`$. Hence, exactly for the band contract,
```math
E_b''(0)=\sum_\rho\frac{b_0(\rho)}{m(\rho)}+\tilde\Phi'(0)^2\,\partial_{\tilde\Phi}^2\epsilon_0,\qquad\tilde\Phi'(0)\simeq-\frac{L\mu_2}{\mu_1+\mu_2}. \qquad\text{(6.6)}
```

The same derivation holds for any bound level with its own $`b_\nu`$. The second term (*ring term*) is the only place where the continuation enters: body 2 as representative replaces $`\mu_2`$ by $`\mu_1`$ in $`\tilde\Phi'(0)`$.

Write $`E''_{\rm line}:=\sum_\rho b_0/m`$ and $`E_b''(0)=E''_{\rm line}(1+\rho_L)`$. Since $`b_0>0`$ on every bond, $`E''_{\rm line}`$ has the sign of $`m`$ whenever $`m(\rho)`$ has one sign along the ring, in particular under B2 (the sign of $`m_0`$). So $`E''_{\rm line}`$ can vanish only if $`m(\rho)`$ changes sign along the ring, which B2 excludes.

$`\partial^2_{\tilde\Phi}\epsilon_0`$ does not depend on which bond carries the flux; put it on the bond $`(r_*,r_*+2)`$ farthest from contact, with amplitude $`s_*`$. Use second-order perturbation in $`\tilde\Phi`$: the first-order term is $`-2s_*b_0(r_*+1)`$, and the matrix elements are $`\lvert s_*\rvert\,\lvert f_{\nu'}(r_*)f_0(r_*+2)-f_{\nu'}(r_*+2)f_0(r_*)\rvert`$. Cauchy–Schwarz and $`\sum_{\nu'}f_{\nu'}(r)^2=1`$ then give
```math
\lvert\rho_L\rvert\le\frac{\tilde\Phi'(0)^2}{\lvert E''_{\rm line}\rvert}\Big[2\lvert s_*b_0(r_*+1)\rvert+\frac{4s_*^2}{\Delta_0}\big(f_0(r_*)^2+f_0(r_*+2)^2\big)\Big], \qquad\text{(6.16)}
```
with $`\Delta_0`$ the distance of $`\epsilon_0`$ from the other levels of $`h_0`$. By B1 the right side is exponentially small in $`L/\xi_0`$ (times $`L^2`$). Both continuations obey (6.16), so $`E_b''(0)`$ is independent of the continuation to relative accuracy $`\lvert\rho_L\rvert`$, which B4 makes smaller than every retained term. If $`\kappa_i(\rho)=\bar\kappa_i`$, then $`m=\mu_1+\mu_2`$ and $`1/E''_{\rm line}=(\mu_1+\mu_2)/\beta_0`$. The order-$`\tau^4`$ terms dropped by R2 change $`E_b''`$ by $`O(\tau'^4/(\delta_1^2\delta))`$, a relative $`O(\tau'^2/(\beta_0\delta_1\delta))`$, small by B3.

### Step 4. Local inertia and the difference from $`\mu_1+\mu_2`$ (item 2)

$`m(\rho)=m_1(\rho)+m_2(\rho)`$ with $`m_i(\rho):=-1/(8\kappa_i(\rho))`$. By (2.11), $`m_i`$ is the inertia $`b_i`$ would have with the amplitude it has at distance $`\rho`$ from the other body. By (2.16), $`m_1=\mu_1(1\pm\sigma_1\bar M^{(2)}(\rho)/M_1+O(\varepsilon^3))`$, and by (2.14) $`\mu_1\sigma_1/M_1=(R_1/M_1)/c_1^2\,(1+O(\gamma_1^2))=c_1^{-2}(1+O(\varepsilon))`$; the same holds for $`b_2`$. With $`\bar M^{(2)}(\rho):=\tfrac14[M^{(2)}(\rho-1)+2M^{(2)}(\rho)+M^{(2)}(\rho+1)]`$:
```math
m(\rho)=\mu_1+\mu_2+s_c\,\bar M^{(2)}(\rho)\Big(\frac1{c_1^2}+\frac1{c_2^2}\Big)+O\big(\varepsilon^3(\lvert\mu_1\rvert+\lvert\mu_2\rvert)\big). \qquad\text{(6.7)}
```
Each body's local inertia contains the second-order mutual term divided by the square of its own speed: once per body, with the sign $`s_c`$.

*Inverse expansion.* Write $`m=m_0+\delta m`$ and $`A_0:=\sum_\rho b_0\,\delta m`$. Expanding $`1/E''_{\rm line}=[\sum_\rho b_0/(m_0+\delta m)]^{-1}`$ in $`\delta m`$ requires $`\lvert A_0\rvert\ll\lvert m_0\rvert\beta_0`$. Since $`b_0>0`$, $`\lvert A_0\rvert\le\bar x\lvert m_0\rvert\beta_0`$, so B2 implies this condition, and $`1/E''_{\rm line}=m_0/\beta_0+A_0/\beta_0^2+O(\bar x^2\lvert m_0\rvert/\beta_0)`$. With (6.7) and $`E_b''(0)=E''_{\rm line}(1+\rho_L)`$:
```math
D_0:=\frac1{E_b''(0)}-\mu_1-\mu_2=\underbrace{(\mu_1+\mu_2)\frac{1-\beta_0}{\beta_0}}_{D^{\rm lat}_0}+\underbrace{\frac{s_c}{\beta_0^2}\Big(\frac1{c_1^2}+\frac1{c_2^2}\Big)\sum_\rho b_0(\rho)\bar M^{(2)}(\rho)}_{D^{\rm mark}_0}-\frac{\rho_L}{E''_{\rm line}}+O\Big(\frac{\varepsilon^3(\lvert\mu_1\rvert+\lvert\mu_2\rvert)}{\beta_0},\frac{\bar x^2\lvert m_0\rvert}{\beta_0},\frac{\rho_L^2}{E''_{\rm line}}\Big). \qquad\text{(6.8)}
```
$`\beta_0`$ and $`b_0`$ are those of the full band chain. The terms of (6.8):
- $`D^{\rm lat}_0`$ is of order zero in $`\varepsilon`$ at fixed $`\chi`$ and nonzero, since $`0<\beta_0<1`$. It has the sign of $`\mu_1+\mu_2`$. It comes from $`K_1+K_2`$ (the $`P`$-dependence of the relative hopping $`\lvert t(\rho;P)\rvert`$, i.e. the form $`\cos2p`$ of each body's band (2.11)), together with $`W`$, which localizes $`f_0`$.
- $`D^{\rm mark}_0`$ comes from the dependence of $`K_i`$ on the other body's mark (2.16). It obeys $`\lvert D^{\rm mark}_0\rvert\le\bar x\lvert m_0\rvert/\beta_0`$ up to the $`O(\varepsilon^3)`$ remainder, and is of order $`\varepsilon^2`$ at fixed $`n,t_f,L`$.
- The ring part is smaller than both by B4.

*Outside B2* (near $`\mu_1+\mu_2=0`$, possible only for $`\sigma_1=-\sigma_2`$, or a mark comparable with $`\lvert m_0\rvert/S`$), (6.8) is not used. There $`1/E_b''(0)=[(1+\rho_L)\sum_\rho b_0(\rho)/m(\rho)]^{-1}`$ by (6.6), with $`m(\rho)`$ of (6.5) unexpanded.

*Dependence on the level* (the selected level of the two classes). In weak binding, Hellmann–Feynman for the uniform chain, $`\partial\epsilon_0/\partial\bar t_0=2\beta_0`$, applied to the bracket of (6.4), gives $`\beta_0\simeq1-\frac{a_0}6(4\chi^2)^{1/3}\simeq1-0.270\chi^{2/3}`$ in both classes. In tight binding $`\beta_0\simeq1/\chi`$ (even class) and $`\beta_0\to\frac12`$ (odd class; check 3). So $`D^{\rm lat}_0`$ grows from $`\simeq0.270\chi^{2/3}m_0`$ to $`\simeq\chi m_0`$ (even) or $`m_0`$ (odd).

*Control:* none in the class. In the wider class of unbound pairs on the line, $`\chi\to0`$ gives $`\beta_0\to1`$ and $`D_0\to0`$.

### Step 5. Inertia against cost (item 3)

As in (4.2), the cost of the bound pair is $`\Delta E_0:=E_b(0)-E_1(0)-E_2(0)+E_\varnothing`$. These are eigenvalues of the total contracts of four descriptions (pair, $`b_1`$ alone, $`b_2`$ alone, field alone), so no split of contract terms enters (M6). With $`E_b(0)=\langle f_0\vert h_0\vert f_0\rangle=\sum_rf_0^2U+2\sum_\rho b_0\,t(\rho;0)`$ and Step 1,
```math
\Delta E_0=\langle M\rangle_0+K_0+O(\varepsilon^2\lvert\bar\kappa\rvert),\qquad K_0:=2\bar t_0(\beta_0-1),\qquad\langle M\rangle_0=\sum_rf_0(r)^2M(r)=M(0)+\langle V\rangle_0+O\big(n\lvert g_1g_2\rvert\ell_0\eta/t_f\big). \qquad\text{(6.9)}
```
$`K_0`$ is the kinetic cost of the relative motion, of sign $`s_\mu`$. Since $`\mu_1+\mu_2=-\bar t_0/(8\bar\kappa_1\bar\kappa_2)`$ and $`\mu_1\mu_2=1/(64\bar\kappa_1\bar\kappa_2)`$, $`D^{\rm lat}_0=4\mu_1\mu_2K_0/\beta_0`$. Splitting $`\bar M^{(2)}=M^{(2)}(0)+\bar V`$ in (6.8) (B2):
```math
D_0=\frac{4\mu_1\mu_2}{\beta_0}K_0+\frac{s_cS}{\beta_0}M(0)+\frac{s_cS}{\beta_0^2}\sum_\rho b_0\bar V-\frac{\rho_L}{E''_{\rm line}},\qquad\frac{\Delta E_0}{c^2}=\frac{K_0+M(0)+\langle V\rangle_0}{c^2}. \qquad\text{(6.10)}
```
*No universal identity.* The coefficients of the two leading terms differ:
- of $`K_0`$: $`4\mu_1\mu_2/\beta_0`$ against $`c^{-2}`$, a ratio of size $`R_1R_2/c^2\gg1`$ by R1;
- of the contact value $`M(0)=-\frac{ng_1g_2}{t_f}\frac{L^2-1}{6L}`$: $`s_cS/\beta_0`$ against $`c^{-2}`$; at equal speeds, $`2s_c/\beta_0`$ against 1.

So (6.10) gives no identity $`D_0=\Delta E_0/c^2`$ with one speed $`c`$ fixed by the contracts. That the relation indeed fails on the class, for every $`c\ge c_{\min}`$, follows from case (i) of (6.17); whether it holds in individual descriptions is decided there.

*Individual equalities.* For a speed $`c`$ let
```math
\Delta_0(c):=D_0-\frac{\Delta E_0}{c^2}=C_KK_0+C_MM(0)+\mathcal V_0-\frac{\rho_L}{E''_{\rm line}},\quad C_K:=\frac{4\mu_1\mu_2}{\beta_0}-\frac1{c^2},\quad C_M:=\frac{s_cS}{\beta_0}-\frac1{c^2},\quad\mathcal V_0:=\frac{s_cS}{\beta_0^2}\sum_\rho b_0\bar V-\frac{\langle V\rangle_0}{c^2}.
```
Let $`c\ge c_{\min}`$; this includes $`c_1`$, $`c_2`$ and equal speeds. The signs of the terms:
- $`S/\beta_0>c^{-2}`$, so $`{\rm sgn}\,C_M=s_c`$ and $`\lvert C_M\rvert\ge c_{\max}^{-2}`$.
- $`4\lvert\mu_1\mu_2\rvert c^2\ge4R_1R_2/c_{\max}^2\gg1`$ (R1: $`c_i\simeq\tau_i\ll R_i`$), so $`{\rm sgn}\,C_K=\sigma_1\sigma_2`$.
- $`{\rm sgn}\,K_0=s_\mu`$ and $`{\rm sgn}\,M(0)=-s_e=-s_\mu`$.

With $`\lvert\bar V(\rho)\rvert\le F(\lvert\rho\rvert+\frac12)`$ and $`b_0(\rho)\le\frac12[f_0(\rho-1)^2+f_0(\rho+1)^2]`$, $`\lvert\mathcal V_0\rvert\le4F(\langle\lvert r\rvert\rangle_0+\frac32)/(c_{\min}^2\beta_0^2)`$, which is below $`\lvert C_MM(0)\rvert`$ if
```math
\text{(S)}\qquad\langle\lvert r\rvert\rangle_0+\tfrac32<\frac{\beta_0^2\,(L-L^{-1})}{24}\,\frac{c_{\min}^2}{c_{\max}^2}.
```
(S) may be replaced by $`\lvert\mathcal V_0\rvert<\lvert C_KK_0\rvert`$. This holds in weak binding, where $`\langle V\rangle_0\simeq2\lvert K_0\rvert`$ (virial theorem of the linear potential) gives $`\lvert\mathcal V_0/C_KK_0\rvert=O(c_{\max}^2/R_1R_2)`$. Hence, at leading order and under B2,
```math
\begin{aligned}&\text{(i) }s_c=-\sigma_1\sigma_2:\ \Delta_0(c)\neq0,\ \text{of sign }\sigma_1\sigma_2s_\mu,\ \text{for every }c\ge c_{\min},\ \text{under (S) and B4};\\&\text{(ii) }s_c=\sigma_1\sigma_2:\ C_KK_0\ \text{and}\ C_MM(0)\ \text{have opposite signs, and }\Delta_0(c)=0\ \text{where they cancel (codimension one); at equal speeds}\\&\qquad\text{in weak binding near }L^*_0\simeq2\cdot4^{1/3}a_0\,\big\lvert C_K/C_M\big\rvert_{\beta_0=1}\,\chi^{-1/3}\ \text{at fixed }n,\chi.\end{aligned} \qquad\text{(6.17)}
```
$`L^*_0`$ solves $`\lvert C_KK_0\rvert=\lvert C_M\rvert FL/6`$ with $`\lvert K_0\rvert=\lvert\bar t_0\rvert\frac{a_0}34^{1/3}\chi^{2/3}`$ (Step 4), up to relative $`O(\chi^{2/3})`$ and $`O(c^2/R_1R_2)`$. For $`\sigma_1=\sigma_2`$ (code sets A, B, D), case (i) is coupling (c) and case (ii) coupling (a); for $`\sigma_1=-\sigma_2`$ the reverse.

*An equality of the leading-order expressions inside R and B.* Take case (ii) with:
- $`\sigma_1=\sigma_2=-1`$ (then $`\delta_1\ge2R_i`$ for every $`t_f`$, Step 7), coupling (a), $`M_i=M`$, $`\tau_i=\tau`$, $`\gamma_1=-\gamma_2=\varepsilon`$. Then $`s_e=s_\mu=-1`$, $`s_\beta=+1`$, the selected level is the highest, and B2 holds since $`\sigma_1=\sigma_2`$.
- $`n=\varepsilon^{-3/4}`$, $`\tau/M=\varepsilon^{1/2}`$, and $`t_f=TM^3/(\tau^2\chi^{2/3})`$ with fixed $`T\gg2.1`$; then $`\chi^{1/3}=4\varepsilon^{5/4}/T`$.
- $`L`$ near $`L^*_0\simeq13M^2/(\tau^2\chi^{1/3})`$.

As $`\varepsilon\to0`$:
- spectral hierarchy (H): the width of $`\mathcal G`$ in a sector, $`W_{\mathcal G}\simeq\lvert V(L/2)\rvert=FL/4\simeq0.81M\chi^{2/3}`$, stays below the first excitation of the held field, $`\omega_1\simeq4\pi^2t_f/L^2\simeq0.24T\tau^2/M`$: $`W_{\mathcal G}/\omega_1\simeq55\varepsilon^{3/2}/T^3\to0`$. So the field-excited levels of the $`\mathcal G`$ branches lie at least $`\omega_1-W_{\mathcal G}\simeq\omega_1`$ from $`\mathcal G`$, the flipped levels at least $`2R-W_{\mathcal G}`$, and $`\delta\simeq\omega_1`$. (H) needs $`\tau/M\gg7.4\,\varepsilon^{5/4}T^{-3/2}`$.
- R1: $`\tau\ll\delta_1\simeq2M`$ and $`\tau^2/(\delta_1\delta)\simeq2.1/T\ll1`$;
- perturbative control: $`n\varepsilon=\varepsilon^{1/4}\to0`$ and $`\eta\simeq1.1\varepsilon\chi^{1/3}/T\to0`$;
- B1, B4 and (S): $`L^*_0/\xi_0\simeq8M^2/\tau^2=8/\varepsilon\gg1`$;
- B2 and the mark expansion: $`\bar x\simeq\lvert M(0)\rvert/M\simeq0.54\chi^{2/3}\to0`$;
- remainders against the cancelling terms, $`\lvert C_KK_0\rvert\simeq0.54M\chi^{2/3}/\tau^2`$. Those of (6.8), as stated, are smaller by $`0.23T^2\varepsilon^{1/2}`$ and $`O(\chi^{2/3})`$. That of (6.9) is smaller by $`(\tau/M)^2T^2/(69\varepsilon^{1/2})=\varepsilon^{1/2}T^2/69`$, or by $`O(\varepsilon)`$ if counted by the actual size $`\lvert\bar\kappa\rvert\chi^{2/3}`$ of the mark. Together with the lower bound from (H), this sets the window $`7.4\,\varepsilon^{5/4}T^{-3/2}\ll\tau/M\ll8\varepsilon^{1/4}/T`$.

So the leading-order $`\Delta_0`$ of (6.8)–(6.10) changes sign across $`L^*_0`$, and tuning $`\varepsilon`$ at fixed $`L`$ gives an exact zero: $`D_0=\Delta E_0/c^2`$ with $`c=\tau`$ at leading order.

*Status:* the remainders of the quoted inputs (2.14), (2.16), (4.3), and hence those of (6.7)–(6.9), are stated at fixed $`n,L,t_f`$. Along this family $`n,L,t_f\to\infty`$ together, and their uniformity is not established here. The equality in the full contract is therefore **unverified**. Established are (H), R, B and the zero of the leading-order $`\Delta_0`$ (code: line chain).

*Not a universal speed.* In case (ii) the zero is a codimension-one condition. At fixed $`c_i`$ the fitted ratio $`c_0^2:=\Delta E_0/D_0`$, where positive, varies with $`L`$ and $`\chi`$ and equals $`c^2`$ only at $`L^*_0`$: it is a property of the description, not a speed fixed by the contracts. In case (i), under (S) and B4, the relation holds for no $`c\ge c_{\min}`$.

### Step 6. Weight of the bound level and fall (item 4)

A held source $`g_s\Phi_{x_s}`$ changes the $`\tau=0`$ levels of $`\mathcal G`$ by the held-pair weight $`W_{\rm pair}(j,l)`$ at first order in $`g_s`$. It changes the $`K_i`$ at relative order $`\gamma_ig_s/t_f`$ (through the field states, as in (2.16)), which enters the fall at $`O(\tau^4\gamma g_s)`$, as in (7.7). Let the source be at a distance $`d_s\gg\xi_0`$ from the pair, and work on the line (B1, B4). The weight of the bound level is
```math
W_0(X):=\sum_rf_0(r)^2\,W_{\rm pair}\big(X-\tfrac r2,X+\tfrac r2\big). \qquad\text{(6.11)}
```
$`W_b`$ vanishes for $`g_1=0`$ and for $`g_2=0`$, hence is $`O(g_1g_2g_s)`$; by (4.5), $`W_{\rm pair}=ng_1\phi(x_1)+ng_2\phi(x_2)+O(\varepsilon^2g_s)`$. $`\phi`$ is quadratic on each arc between images of $`x_s`$ ($`\phi''=-2g_s/(t_fL)`$), and $`\sum_rf_0^2\,r=0`$ ($`f_0^2`$ is even by the reflection of Step 1). Hence, for pair positions not reaching $`x_s`$,
```math
W_0(X+1)-W_0(X-1)=n(g_1+g_2)\,[\phi(X+1)-\phi(X-1)]+O(\varepsilon^2g_s)+O(e^{-d_s/\xi_0}): \qquad\text{(6.12)}
```
at leading order the weight difference of the bound level is that of its members.

*Bound band with $`P`$-dependent profile.* Written symmetrically, the sector eigenvector of (6.1) is $`\psi_P(j,l)=L^{-1/2}e^{iP(j+l)/2}f_{0,P}(l-j)`$, with $`f_{0,P}`$ the eigenvector of the chain with bonds $`\kappa_1(\rho)e^{-iP}+\kappa_2(\rho)e^{iP}=e^{iP}t(\rho;P)`$; this chain is unitarily equivalent to $`h_P`$. The gauge of Step 3 gives $`f_{0,P}=e^{i\theta_P}F_{0,P}`$ with $`F_{0,P}`$ real and $`F_{0,P}=f_0+O(P^2)`$ ($`s_\rho`$ is even in $`P`$). From $`\arg(\kappa_1e^{-iP}+\kappa_2e^{iP})=-P\frac{\kappa_1-\kappa_2}{\kappa_1+\kappa_2}+O(P^3)`$ and $`\kappa_i=-1/(8m_i)`$: $`\theta_P=P\theta'+O(P^3)`$, with $`\theta'(r+2)-\theta'(r)=[m_2(\rho)-m_1(\rho)]/m(\rho)`$ ($`\rho=r+1`$) and $`\theta'`$ odd. Hence $`\psi_P=L^{-1/2}e^{iPY}F_{0,P}[1+O(P^3)]`$ with the centre
```math
Y(j,l):=\frac{j+l}2+\theta'(l-j)=\frac{\mu_1j+\mu_2l}{\mu_1+\mu_2}+O\big(\varepsilon^2\lvert l-j\rvert\big): \qquad\text{(6.18)}
```
$`P`$ is conjugate to the inertia-weighted centre, not to the midpoint.

The source matrix elements on the band are $`\langle P',0\vert W\vert P,0\rangle=L^{-1}\sum_{j,l}e^{i(P-P')Y}F_{0,P'}F_{0,P}W_{\rm pair}[1+O(P^3,P'^3)]`$, not $`f_0^2`$ at all momenta. For a start of width $`w`$ in $`Y`$ ($`\lvert P\rvert\lesssim1/w`$), $`F_{0,P'}F_{0,P}=f_0^2[1+O(w^{-2})]`$. So on the band the source acts as $`\tilde W_0(\hat Y)`$ up to relative $`O(w^{-2})`$. Here $`\tilde W_0(Y):=\sum_rf_0^2W_{\rm pair}(Y-\frac r2-\theta'(r),Y+\frac r2-\theta'(r))`$, with $`W_{\rm pair}`$ continued between places by its form on the arc. At first order in $`g_i`$, $`\tilde W_0-W_0`$ is constant on the arc: $`f_0^2`$ is even, $`\theta'`$ odd and $`\phi''`$ constant. So the weight differences of the band are those of (6.11), (6.12), up to $`O(\varepsilon^2g_s)`$.

*Acceleration from rest.* Take the band contract with source, $`H=H_{\rm eff}+W_{\rm pair}`$, and a start $`\psi(j,l)=\varphi(Y)f_0(l-j)`$, with a real envelope $`\varphi`$ of width $`w`$ that is even about a point $`x_0`$ with $`2x_0\in\mathbb Z`$. Let $`a_0(0):=\frac{{\rm d}^2}{{\rm d}\lambda^2}\langle\hat Y\rangle\vert_{\lambda=0}=-\langle[H,[H,\hat Y]]\rangle`$.
- This needs no band projection and contains the interband terms.
- It is exactly linear in $`W_{\rm pair}`$, since $`[W,[W,\hat Y]]=0`$.
- Its $`g_s`$-independent part vanishes on the line: the reflection about $`x_0`$ (Step 1) leaves $`H_{\rm eff}`$ invariant and maps $`\hat Y-x_0\to-(\hat Y-x_0)`$ and $`\psi\to\pm\psi`$.

The linear part is $`-\sum_{a,b}\psi_a\psi_b(W_a-W_b)H_{ab}(Y_b-Y_a)`$. A hop of $`b_i`$ by $`\pm2`$ across the bond $`\rho`$ has $`H_{ab}=\kappa_i(\rho)`$ and, by (6.18), $`Y_b-Y_a=\pm2m_i(\rho)/m(\rho)`$, so $`\kappa_i(Y_b-Y_a)=\mp1/(4m(\rho))`$ for both bodies. On each bond $`\psi_a\psi_b=\varphi^2b_0(\rho)[1+O(w^{-2})]`$. Hence
```math
a_0(0)=-\sum_X\varphi_X^2\sum_\rho\frac{b_0(\rho)}{m(\rho)}\,(\partial_1+\partial_2)W_{\rm pair}\big\vert_{X,\rho}\big[1+O(w^{-2})\big]=-E''_{\rm line}\sum_X\varphi_X^2\,W'_0(X)\big[1+O(w^{-2})\big]+O(\varepsilon^2g_sE''_{\rm line})+O(g_s^2)+O(\tau^4\gamma g_s), \qquad\text{(6.13)}
```
with $`\partial_i`$ the centred difference in $`x_i`$ and $`W'_0(X):=\tfrac12[W_0(X+1)-W_0(X-1)]`$; the $`O(g_s^2)`$ is zero within the band contract.

The second form of (6.13) uses $`(\partial_1+\partial_2)W_{\rm pair}=n(g_1+g_2)\phi'(X)+(\text{odd in }\rho)+O(\varepsilon^2g_s)`$, whose odd part cancels against the even $`b_0/m`$, and (6.12). It is informative only where $`n\lvert g_1+g_2\rvert\lvert\phi'\rvert`$ exceeds its additive remainders, i.e. under (N) below. For one body the same computation gives the leading form of (7.7). So (7.7) carries over to the bound level, for the centre $`\hat Y`$, with $`E''\to E''_{\rm line}`$ and $`W'\to W'_0`$. The midpoint $`(\hat x_1+\hat x_2)/2`$ moves by $`\pm1`$ per hop and gets instead $`-\frac{\beta_0}2\sum_X\varphi_X^2(W_1'/\mu_1+W_2'/\mu_2)`$ at $`\lambda=0`$ (uniform hopping), the instantaneous response of the relative motion.

*Fall factor.* $`\Pi_0:=E''_{\rm line}W'_0`$, and for $`b_i`$ alone $`\Pi_i:=E_i''(0)W_i'=ng_i\phi'/\mu_i+O(\varepsilon^2g_s/\lvert\mu_i\rvert)`$ by (4.5), with $`ng_i\phi'/\mu_i=n\gamma_ic_i^2\phi'(1+O(\varepsilon))`$ by (2.14). By (6.12) and (4.5), $`W'_0=W'_1+W'_2+O(\varepsilon^2g_s)=\mu_1\Pi_1+\mu_2\Pi_2+O(\varepsilon^2g_s)`$, and by B2, $`E''_{\rm line}=(\beta_0/m_0)(1+O(\bar x))`$. Hence, with an additive error,
```math
\Pi_0=\frac{\beta_0}{\mu_1+\mu_2}\Big[(\mu_1\Pi_1+\mu_2\Pi_2)\big(1+O(\bar x)\big)+O(\varepsilon^2g_s)\Big],\qquad\mu_1\Pi_1+\mu_2\Pi_2=n(g_1+g_2)\phi'+O(\varepsilon^2g_s). \qquad\text{(6.14)}
```
*Relative form.* It holds under the non-cancellation condition (N): $`n\lvert g_1+g_2\rvert\lvert\phi'\rvert`$ is large against the second-order weight differences ($`O(\varepsilon^2g_s)`$); at fixed $`n,t_f,L`$ this reads $`\lvert g_1+g_2\rvert\gg\varepsilon\max_i\lvert g_i\rvert`$. Then $`\Pi_0=\beta_0\frac{\mu_1\Pi_1+\mu_2\Pi_2}{\mu_1+\mu_2}[1+O(\varepsilon\max_i\lvert g_i\rvert/\lvert g_1+g_2\rvert)+O(\bar x)]`$.

Under the named condition $`\gamma_1c_1^2=\gamma_2c_2^2`$ (M7), $`\Pi_2=\Pi_1(1+O(\varepsilon))`$ and $`n(g_1+g_2)\phi'=(\mu_1+\mu_2)\Pi_1(1+O(\varepsilon))`$. So (N) reads $`\lvert\mu_1+\mu_2\rvert\gg\varepsilon\max_i\lvert\mu_i\rvert`$, and then
```math
\Pi_0-\Pi_1=-(1-\beta_0)\Pi_1+O\big(\varepsilon\Pi_1\max_i\lvert\mu_i\rvert/\lvert\mu_1+\mu_2\rvert\big)+O(\bar x\Pi_1),
```
which for $`\sigma_1=\sigma_2`$ is $`O(\varepsilon\Pi_1)+O(\bar x\Pi_1)`$. The single bodies have equal fall factors only under that named condition. Even then the bound pair differs at leading order (order zero in $`\varepsilon`$ at fixed $`\chi`$) by the factor $`\beta_0\in(0,1)`$: it falls slower than its parts.

*Vanishing first-order weight.* Let $`g_1+g_2=0`$, i.e. $`\sigma_1\gamma_1M_1=-\sigma_2\gamma_2M_2`$. This is compatible with $`s_\beta=+1`$ and B2 (e.g. the family of Step 5); under the named condition it would need $`\mu_1+\mu_2=O(\varepsilon\max_i\lvert\mu_i\rvert)`$. (N) then fails.
- Determined: $`W'_0=O(\varepsilon^2g_s)`$, and by (6.14) $`\Pi_0=O(\beta_0\varepsilon^2g_s/\lvert m_0\rvert)`$. The pair's fall factor is of second order in the couplings, while each body's, $`\Pi_i=(ng_i\phi'/\mu_i)(1+O(\varepsilon))`$, is of first order. So $`\Pi_0-\Pi_i=-\Pi_i[1+O(\varepsilon\lvert\mu_i\rvert/\lvert m_0\rvert)]`$: the pair differs from each body at first order.
- Not determined: the value and sign of $`\Pi_0`$ at second order, which needs the second-order terms of (4.5) and $`W_b`$ of (4.7), whose bond function $`B`$ is not quoted.
- Not determined either: the factorized form of (6.13) at that order. The first form, with the $`b_0/m`$-average of $`(\partial_1+\partial_2)W_{\rm pair}`$, is derived. Its replacement by $`E''_{\rm line}W'_0`$ (an $`f_0^2`$-average) is not, since the $`\rho`$-dependence of the second-order gradient enters both at the same order. In code set D the two differ by a factor of 2.0–2.2.

*Control:* none in the class for (6.14) under (N). Unbound pairs on the line ($`\chi\to0`$) give $`\beta_0\to1`$, and equality under the named condition.

### Step 7. Dependence on $`t_f`$ (item 5)

At fixed $`n,\gamma_i,M_i,\tau_i`$: $`R_i`$, $`\mu_i`$, $`c_i`$, $`\bar\kappa_i`$, $`\bar t_0`$ do not depend on $`t_f`$ at the orders used; $`M^{(2)}`$, $`F`$ and $`\eta`$ scale as $`1/t_f`$; $`\phi\propto g_s/t_f`$.

*R1 from the held spectra.* Flipping $`b_i`$ from $`e_{jl}`$ reaches the held levels with $`b_i`$'s coupling reversed and all field states. Their distances from $`E(j,l)`$ are $`\lvert2\sigma_iR_i-\omega^{(i)}_n\rvert`$, with $`\omega^{(i)}_n\ge0`$ the excitation energies of that held field. At leading order in $`\varepsilon`$, $`\omega\in\{2t_f\sum_kn_k(1-\cos\frac{2\pi k}L):\sum_kn_k\le N_f\}`$; for $`N_f=1`$, $`\omega\in\{4t_f\sin^2(\pi k/L)\}`$.
- For $`\sigma_i=-1`$ all distances are $`\ge2R_i`$: there is no resonance condition on $`t_f`$.
- For $`\sigma_i=+1`$, R1 excludes the $`t_f`$ for which some $`\omega`$ lies within $`\delta_1`$ of $`2R_i`$. For $`N_f=1`$ these are the intervals $`[(2R_i-\delta_1),(2R_i+\delta_1)]/(4\sin^2(\pi k/L))`$, $`k=1,\dots,L/2`$.
- Sufficient conditions are $`4N_ft_f\le2R_i-\delta_1`$ (all excitations below) or $`4t_f\sin^2(\pi/L)\ge2R_i+\delta_1`$ (all above).

$`\delta`$ is the distance of $`\mathcal G`$ from all other $`\tau=0`$ levels of the sector. These are the field excitations of the $`\mathcal G`$ branches, at least $`\omega_1-W_{\mathcal G}`$ away with $`\omega_1\simeq4t_f\sin^2(\pi/L)`$ shifted by the marks, and the doubly flipped levels $`\lvert2\sigma_1R_1+2\sigma_2R_2-\omega\rvert`$. So $`\delta`$ is not automatically the field gap. With the weak-binding $`\beta_0`$ of Step 4:
```math
\chi=\frac{n\lvert g_1g_2\rvert}{t_f\lvert\bar t_0\rvert}\propto\frac1{t_f},\quad1-\beta_0\simeq0.270\,\chi^{2/3}\propto t_f^{-2/3},\quad\frac{\tau'^2}{\delta_1\delta}\ll1\ll\chi L^3,\quad\min_n\big\lvert2R_i-\omega^{(i)}_n\big\rvert\ge\delta_1\ \ (\sigma_i=+1). \qquad\text{(6.15)}
```
The bounds on $`t_f`$:
- The second inequality bounds $`t_f`$ from below where $`\delta`$ is the field gap: $`t_f\gg\tau'^2/(4\delta_1\sin^2(\pi/L))`$.
- $`\chi L^3\gg1`$ (B1) bounds it from above. B4 bounds it further from above, since $`\xi_0\propto t_f^{1/3}`$ while the mark terms fall as $`1/t_f`$.
- In B2 the mark part of $`\bar x`$ falls as $`1/t_f`$; the cancellation of $`\mu_1+\mu_2`$ does not depend on $`t_f`$.

Hence:
- (6.3) does not depend on $`t_f`$.
- $`D^{\rm lat}_0`$ and the relative deviation $`1-\beta_0`$ of $`\Pi_0`$ from the inertia-weighted $`\Pi_i`$ fall as $`t_f^{-2/3}`$; $`D^{\rm mark}_0`$ and $`M(0)`$ fall as $`1/t_f`$; the equality points of (6.17)(ii) move as $`L^*_0\propto t_f^{1/3}`$.
- No $`t_f`$ in the window gives $`\beta_0=1`$, so (6.10) and (6.14) persist.

A faster field weakens the binding and brings the pair's inertia and fall factor towards $`\mu_1+\mu_2`$ and the inertia-weighted $`\Pi_i`$. The limit is reached only where the pair stops being bound on the ring.

## Result

- **(6.1)** Class above, order $`\tau^2`$: in the sector $`P`$ (body 1 as representative, continued to real $`P`$) the band contract is the relative chain $`h_P`$ with bond amplitudes $`t(\rho;P)=\kappa_1(\rho)e^{-2iP}+\kappa_2(\rho)`$ and separate rings for $`r`$ even and odd.
- **(6.2)** Leading order in $`\varepsilon`$: $`M^{(2)}(r)=-2ng_1g_2\ell(r)/t_f`$ and the relative potential $`V(r)=\frac{ng_1g_2}{t_fL}r(L-r)`$, a well at contact for $`g_1g_2>0`$ and a hill for $`g_1g_2<0`$.
- **(6.3)** Under R and $`\chi L^3\gg1`$, for every branch combination and both signs of $`\gamma_1\gamma_2`$, bound levels exist: the lowest relative levels if $`\sigma_1\sigma_2\gamma_1\gamma_2>0`$, the highest if $`<0`$. The selected level is the extreme level at the $`k=0`$ edge of the relative band (bodies near rest): the lowest if $`s_\mu=+1`$, the highest if $`s_\mu=-1`$. It is bound iff $`s_\beta={\rm sgn}[g_1g_2(\mu_1^{-1}+\mu_2^{-1})]=+1`$, and then $`f_0>0`$ on the whole relative ring. Bound levels with $`s_\beta=-1`$ (alternating near contact) and excited bound levels are named only.
- **(6.4)** Selected level, $`s_\beta=+1`$, leading order in $`\varepsilon`$, uniform hopping, weak binding $`F\ll\lvert\bar t(P)\rvert`$, up to $`O(\chi^{2/3})`$ and $`O(\xi_0/L)`$: $`E_b(P)=E_1(0)+E_2(0)-E_\varnothing+M(0)-2\bar t_0+s_e[-2\lvert\bar t(P)\rvert+a_0(4\lvert\bar t(P)\rvert F^2)^{1/3}]`$, with $`a_0=1.0188`$ the first zero of $`{\rm Ai}'`$.
- **(6.5)** Definitions for the selected level: bond weights $`b_0>0`$, bond overlap $`0<\beta_0<1`$, local pair inertia $`m(\rho)`$.
- **(6.6)** Exact for the band contract (order $`\tau^2`$): $`E_b''(0)=E''_{\rm line}(1+\rho_L)`$ with $`E''_{\rm line}=\sum_\rho b_0(\rho)/m(\rho)`$ and the ring remainder $`\rho_L`$, the only part that depends on the continuation. Since $`b_0>0`$, $`E''_{\rm line}`$ can vanish only if $`m(\rho)`$ changes sign along the ring, which B2 excludes.
- **(6.7)** Order $`\varepsilon^2`$, error $`O(\varepsilon^3(\lvert\mu_1\rvert+\lvert\mu_2\rvert))`$: $`m(\rho)=\mu_1+\mu_2+s_c\bar M^{(2)}(\rho)(c_1^{-2}+c_2^{-2})`$. The mutual term enters each body's inertia once, over its own speed squared, with sign $`+`$ for (a) and $`-`$ for (c).
- **(6.8)** Selected level, under B2, which implies the inverse-expansion condition $`\lvert A_0\rvert\le\bar x\lvert\mu_1+\mu_2\rvert\beta_0\ll\lvert\mu_1+\mu_2\rvert\beta_0`$. Through order $`\varepsilon^2`$, to first order in $`\rho_L`$, with remainders $`O(\varepsilon^3(\lvert\mu_1\rvert+\lvert\mu_2\rvert)/\beta_0,\bar x^2\lvert\mu_1+\mu_2\rvert/\beta_0)`$: $`1/E_b''(0)-\mu_1-\mu_2=D^{\rm lat}_0+D^{\rm mark}_0-\rho_L/E''_{\rm line}`$.
  - The leading part $`D^{\rm lat}_0=(\mu_1+\mu_2)(1-\beta_0)/\beta_0`$ comes from the $`P`$-dependence of $`K_1+K_2`$ with the binding by $`W`$. It is nonzero, with the sign of $`\mu_1+\mu_2`$.
  - $`D^{\rm mark}_0`$ comes from the $`\rho`$-dependence of $`K_i`$, with $`\lvert D^{\rm mark}_0\rvert\le\bar x\lvert\mu_1+\mu_2\rvert/\beta_0`$.
  - $`\beta_0\simeq1-0.270\chi^{2/3}`$ in weak binding (both classes); in tight binding $`\beta_0\simeq1/\chi`$ (even class) and $`\beta_0\to\frac12`$ (odd class).
  - Outside B2 (near $`\mu_1+\mu_2=0`$) only (6.6), unexpanded, is derived.
- **(6.9)** Selected level, order $`\tau^2`$, through $`\varepsilon^2`$: the cost of the bound pair is $`\Delta E_0=\langle M\rangle_0+K_0`$, with the kinetic cost $`K_0=2\bar t_0(\beta_0-1)`$ of sign $`s_\mu`$.
- **(6.10)** Negative, selected level, leading order, both couplings, under R and B: $`1/E_b''(0)-\mu_1-\mu_2=\Delta E_0/c^2`$ is not an identity on the class for any speed $`c\ge\min(c_1,c_2)`$, in particular $`c_1`$, $`c_2`$ and equal speeds. The coefficients of $`K_0`$ ($`4\mu_1\mu_2/\beta_0`$ against $`c^{-2}`$) and of $`M(0)`$ ($`s_c(c_1^{-2}+c_2^{-2})/\beta_0`$ against $`c^{-2}`$) differ, and the relation fails in every description of case (i) of (6.17).
- **(6.11)** Definition: the weight of the bound level is the $`f_0^2`$-average of the held-pair weight, at first order in $`g_s`$.
- **(6.12)** First order in $`g_i`$ and $`g_s`$, source far from the pair: the weight difference of the bound level is that of its members, $`n(g_1+g_2)\Delta\phi`$, with additive error $`O(\varepsilon^2g_s)`$.
- **(6.13)** (7.7) carries over to the bound level for the centre $`\hat Y`$ of (6.18), with $`E''_{\rm line}`$ and $`W'_0`$. This holds on the line, for a start $`\varphi(Y)f_0`$ with a real envelope of width $`w`$ even about a point, at first order in $`g_s`$, up to a relative $`O(w^{-2})`$ and additive $`O(\varepsilon^2g_sE''_{\rm line})`$, $`O(\tau^4\gamma g_s)`$; it is informative under (N). The first form (the $`b_0/m`$-average of $`(\partial_1+\partial_2)W_{\rm pair}`$) holds also for $`g_1+g_2=0`$. The midpoint of the pair has in general a different acceleration from rest.
- **(6.14)** Negative, selected level, both couplings, under R and B.
  - With additive error: $`\Pi_0=\frac{\beta_0}{\mu_1+\mu_2}[(\mu_1\Pi_1+\mu_2\Pi_2)(1+O(\bar x))+O(\varepsilon^2g_s)]`$.
  - Under (N), $`\lvert g_1+g_2\rvert\gg\varepsilon\max_i\lvert g_i\rvert`$: $`\Pi_0=\beta_0(\mu_1\Pi_1+\mu_2\Pi_2)/(\mu_1+\mu_2)`$ up to relative $`O(\varepsilon\max_i\lvert g_i\rvert/\lvert g_1+g_2\rvert)+O(\bar x)`$.
  - Under the named condition $`\gamma_1c_1^2=\gamma_2c_2^2`$ and (N): $`\Pi_0-\Pi_1=-(1-\beta_0)\Pi_1+O(\varepsilon\Pi_1\max_i\lvert\mu_i\rvert/\lvert\mu_1+\mu_2\rvert)+O(\bar x\Pi_1)`$, so the bound level falls slower than its parts at leading order.
  - For $`g_1+g_2=0`$: $`\Pi_0=O(\beta_0\varepsilon^2g_s/\lvert\mu_1+\mu_2\rvert)`$ is of second order, so it differs from each $`\Pi_i`$ at first order. Its second-order value is not determined (the bond function of (4.7) is not quoted), and neither is the factorized form of (6.13) at that order.
  - No control in the class.
- **(6.15)** Item 5, selected level, at fixed $`n,\gamma_i,M_i,\tau_i`$:
  - $`\chi\propto1/t_f`$; in weak binding $`1-\beta_0\simeq0.270\chi^{2/3}`$, so the deviations of items 2 and 4 fall as $`t_f^{-2/3}`$, and the mark terms and the mark part of $`\bar x`$ (B2) as $`1/t_f`$.
  - The resonance condition of R1 restricts $`t_f`$ only for $`\sigma_i=+1`$: it excludes the intervals where an excitation of the held field with $`b_i`$ flipped lies within $`\delta_1`$ of $`2R_i`$. Sufficient conditions are $`4N_ft_f\le2R_i-\delta_1`$ or $`4t_f\sin^2(\pi/L)\ge2R_i+\delta_1`$.
  - $`\tau'^2/(\delta_1\delta)\ll1\ll\chi L^3`$ bound $`t_f`$ from below (where $`\delta`$ is the field gap) and from above.
  - No $`t_f`$ in the window removes (6.10) or (6.14).
- **(6.16)** Bound on the ring remainder at the bond farthest from contact: $`\lvert\rho_L\rvert\le\tilde\Phi'(0)^2[2\lvert s_*b_0\rvert+4s_*^2(f_0(r_*)^2+f_0(r_*+2)^2)/\Delta_0]/\lvert E''_{\rm line}\rvert`$, exponentially small in $`L/\xi_0`$ (times $`L^2`$). $`E_b''(0)`$ is independent of the continuation to relative accuracy $`\lvert\rho_L\rvert`$.
- **(6.17)** Selected level, leading order, under B2, every speed $`c\ge\min(c_1,c_2)`$ (including $`c_1`$, $`c_2`$ and equal speeds).
  - (i) If $`s_c=-\sigma_1\sigma_2`$, then $`1/E_b''(0)-\mu_1-\mu_2\neq\Delta E_0/c^2`$. This needs (S), or $`\lvert\mathcal V_0\rvert<\lvert C_KK_0\rvert`$ (e.g. weak binding), and B4.
  - (ii) If $`s_c=\sigma_1\sigma_2`$, the two leading terms have opposite signs and equality holds where they cancel, a codimension-one condition. At equal speeds in weak binding this is near $`L^*_0\simeq2\cdot4^{1/3}a_0\lvert C_K/C_M\rvert\chi^{-1/3}`$.
  - For the leading-order expressions such a zero occurs along a family that satisfies R (with the spectral hierarchy (H)) and B ($`\sigma_i=-1`$, coupling (a), Step 5). Whether it occurs in the full contract is unverified, since the quoted remainders are not shown to be uniform along the family. A fitted ratio $`\Delta E_0/D_0`$ varies with $`L`$ and $`\chi`$ and is not a speed fixed by the contracts.
- **(6.18)** On the line, the plane-wave label $`P`$ of the bound band is conjugate to the centre $`Y=\frac{j+l}2+\theta'(l-j)=\frac{\mu_1j+\mu_2l}{\mu_1+\mu_2}+O(\varepsilon^2\lvert l-j\rvert)`$. With the $`P`$-dependent profile the projected source is $`\tilde W_0(\hat Y)`$, whose differences equal those of $`W_0`$ up to $`O(\varepsilon^2g_s)`$ and relative $`O(w^{-2})`$.

## Consistency checks

1. *Dimensions.* $`P`$ and the positions are dimensionless, so $`E_b''`$, $`E_i''`$, $`W'_0`$, $`W_i'`$ have the dimension $`[C]`$, and $`\mu_i`$, $`m`$, $`1/E_b''`$ have $`[C]^{-1}`$. So do $`\bar M^{(2)}/c_i^2`$ and $`\mu_1\mu_2K_0`$ ($`c_i^2\sim[C]^2`$). $`\Pi_0`$, $`\Pi_i`$ and $`a_0(0)`$ have $`[C]^2`$, the dimension of a second derivative in $`\lambda`$. $`\beta_0`$, $`\chi`$, $`\rho_L`$, $`\bar x`$ are pure numbers. Passed.
2. *Unbound limit $`\chi\to0`$ on the line* (e.g. $`\gamma_2\to0`$): $`\beta_0\to1`$ and $`M^{(2)}\to0`$, so $`1/E_b''(0)\to\mu_1+\mu_2`$. This agrees with the curvature of $`E_1(p_1)+E_2(p_2)`$ at fixed $`p_1+p_2=P`$ at its extremum $`p_i=0`$ (bodies at rest), $`1/(\mu_1+\mu_2)`$. Passed.
3. *Tight binding $`\chi\to\infty`$.* Even class: $`f_0\simeq\delta_{r0}`$ and $`f_0(\pm2)\simeq\bar t_0/(E_b-U(2))`$, so $`\beta_0\simeq1/\chi`$ and $`E_b''(0)\simeq s_e\,8\bar\kappa_1\bar\kappa_2/F`$. This agrees with direct second-order perturbation of the contact state, $`E_b(P)=U(0)-s_e\lvert\bar t(P)\rvert^2/F`$. Odd class: $`f_0\simeq(\delta_{r,1}+\delta_{r,-1})/\sqrt2`$, $`\beta_0\to\frac12`$, so $`1/E_b''(0)=2(\mu_1+\mu_2)`$. This agrees with the two-site level $`U(1)-s_e\lvert\bar t(P)\rvert`$, whose curvature is $`4s_e\bar\kappa_1\bar\kappa_2/\lvert\bar t_0\rvert`$. Passed.

## Open issues

- Bound levels with $`s_\beta=-1`$ (bodies near $`p_1=-p_2=\pm\pi/2`$) and excited bound levels are out of scope for items 2–5 (note of 2026-10-21). (6.6) holds for them, but their inertia, cost and fall are not derived here.
- Outside B2 (near $`\mu_1+\mu_2=0`$, $`\sigma_1=-\sigma_2`$) only the unexpanded (6.6) is available; the cost comparison and the fall factor there are not derived.
- The code sets do not meet B4 for the mark terms: $`\lvert\rho_L\rvert=0.2`$–$`12\%`$, against $`\lvert D^{\rm mark}\rvert\approx0.2`$–$`0.3\%`$ of $`1/E_b''`$. The code therefore checks (6.6) with the ring term included.
- The closed forms (6.2), (6.4), (6.15), (6.17) use $`M^{(2)}`$; at $`\eta\approx0.3`$ (code) the exact binding slope is about half of $`F`$. Statements in terms of $`\beta_0`$, $`b_0`$, $`M`$ are not affected.
- The $`O(\varepsilon^3)`$ remainder of (6.7) is large at moderate couplings (code: ratio 1.40 for (a), $`-0.19`$ for (c) at $`\eta\approx0.3`$), so $`D^{\rm mark}`$ is reliable only for small $`\eta`$.
- The second-order corrections of (6.13), (6.14) are not evaluated (the bond function $`B`$ of (4.7) is not quoted). In the code they are 13–16% in $`\Delta W_0/(\Delta W_1+\Delta W_2)`$. For $`g_1+g_2=0`$ (set D) the second-order fall is not given by the factorized form (factor 2.0–2.2).
- On the ring, (6.13) has a $`g_s`$-independent part from the relative cut $`r=L/2`$, where the reflection argument fails. In the code it is up to 0.6% of the first-order part (set A) and drops to $`10^{-4}`$ of it when the profile is cut there; it is not bounded analytically.
- For the even class in tight binding, $`\beta_0\sim1/\chi`$, and B3 fails when $`\chi\gtrsim\delta_1\delta/\tau'^2`$; the order-$`\tau^4`$ band contract is then needed.
- For $`\sigma_i=+1`$ and $`N_f>1`$ the excitation energies near $`2R_i`$ become dense, and the windows of (6.15) shrink. Whether weakly coupled resonances (matrix elements $`O(\gamma^k)`$ for $`k`$ excited objects) can be tolerated is open.
- The equality family of (6.17)(ii) is unverified in the full contract. It needs the remainders of (2.14), (2.16), (4.3) uniformly in $`n,L,t_f\to\infty`$, and it was checked only on the leading-order line chain.
- Out of scope: full grip, tori, the highest field state, bodies of one type, the speed of a front of the field; how typical the structure is (item 5 of the base problem).

## Code

- `code/v3/check_inertia.py` (check). It treats $`N_f=1`$, $`t_f=1`$ and three parameter sets, all with $`s_\beta=+1`$:
  - A: $`\sigma_i=+1`$, $`M=(3,4)`$, $`\tau_1=0.2`$, $`\gamma=(0.09,0.07)`$, $`r`$ even, lowest level; $`\tau_2=\tau_1`$ for (a) and $`\tau_2=\tau_1(1+\gamma_1/L)/(1+\gamma_2/L)`$ for (c), so that $`c_1=c_2`$ exactly for both couplings.
  - B: $`\sigma_i=-1`$, $`M=(2.5,2)`$, $`\tau=(0.16,0.2)`$, $`\gamma=(0.10,-0.14)`$, $`r`$ odd, highest level, unequal speeds.
  - D: $`\sigma_i=-1`$, $`M=(3,3)`$, $`\tau=0.2`$, $`\gamma=(0.09,-0.09)`$ ($`g_1+g_2=0`$), $`r`$ even, highest level, speeds equalized as in A.

  Each set runs at $`L=12,16`$ for couplings (a) and (c). The script builds the exact sector contract (body 1 as representative, continued in $`P`$) and finds the exact bound level by its weight on $`\mathcal G`$ ($`\ge0.998`$). It takes the curvature by second-order perturbation in $`P`$ (cross-checked by finite differences) and builds the band contract by second-order Schrieffer–Wolff. Results:
  - (6.6) with its ring term agrees with the exact curvature to $`\le0.28\%`$ in all 12 cases.
  - $`f_0>0`$ in all cases. $`\beta_0=0.69`$–$`0.79`$ (A), $`0.77`$–$`0.78`$ (B), $`0.51`$–$`0.57`$ (D). $`1/E_b''(0)=(1.22`$–$`1.29)(\mu_1+\mu_2)`$ for A, B and $`(1.76`$–$`1.92)(\mu_1+\mu_2)`$ for D.
  - B2: $`\bar x=0.0011`$–$`0.0054`$ and $`\lvert A_0\rvert/(\lvert m_0\rvert\beta_0)=0.0003`$–$`0.005`$. The expanded inverse $`m_0/\beta_0+A_0/\beta_0^2`$ differs from the unexpanded $`1/E''_{\rm line}`$ by $`\le3\times10^{-6}`$ (relative), i.e. $`O(\bar x^2)`$.
  - $`\rho_L`$ is 12% and 3% (A, $`L=12,16`$), 6% and 0.6% (B), 2.6–2.8% and 0.2% (D). The bound (6.16) holds in all cases and exceeds $`\lvert\rho_L\rvert`$ by factors 5.7–11.
  - $`D\,c^2/\Delta E`$ is $`-500`$ to $`-575`$ (A), $`-208`$ to $`-363`$ (B, with $`c_1`$ or $`c_2`$) and $`-562`$ to $`-734`$ (D): far from 1, since these $`L`$ lie far below $`L^*_0`$.
  - The ratio of the numerical $`m(\rho)-\mu_1-\mu_2`$ to (6.7) tends to 1 as the couplings are scaled down (1.04 for (a), 0.93 for (c) at scale 0.03).
  - R1 gaps from the held-sector spectra at $`t_f=1`$: $`\delta_1=2.0`$ (A), $`3.9`$ (B), $`5.9`$ (D); $`\delta=0.12`$–$`0.23`$, below the free field gaps $`0.268`$ ($`L=12`$) and $`0.152`$ ($`L=16`$); the width of $`\mathcal G`$ is $`0.010`$–$`0.018`$, so (H) holds. At $`t_f=40`$, $`\delta_1=2.6`$ (A), $`4.0`$ (B), $`6.0`$ (D) for $`L=12`$; for $`L=16`$, A has a resonance ($`\delta_1=0.024`$, $`4t_f\sin^2(\pi/16)\simeq2R_1`$), while B and D ($`\sigma_i=-1`$) keep $`4.0`$ and $`6.0`$.
  - Sign rule (6.17) on the leading-order line chain ($`\chi=0.05`$, $`\sigma_i=-1`$, $`s_e=-1`$, $`4\mu_1\mu_2c^2=64`$, selected level): $`\Delta_0`$ changes sign for (a) at $`L=564`$, against the estimate 553, and never for (c) in $`100\le L\le3000`$.

  Outputs: `code/v3/output/inertia_check.txt`, `code/v3/output/inertia_check.json`.
- `code/v3/check_weight.py` (check). Set A, couplings (a) and (c), $`L=16,20`$, held source $`g_s=-0.01`$ (and $`-0.005`$ at $`L=16`$). It computes the exact eigenvalues of the full contract near the bottom of the bound band (weight on $`\mathcal G\ge0.9997`$) and compares them with three reductions: (i) the first-order projected contract $`E_b(P_k)+\langle P',v_{P'}\vert g_s\Phi_{x_s}\vert P,v_P\rangle`$ with the exact $`P`$-dependent sector eigenvectors; (ii) the frozen description $`E_b(\hat P)+W_0(\hat X)`$ with (6.11); (iii) the same with the pair inertia set to $`\mu_1+\mu_2`$. Results:
  - Main level spacing: (i) is within 0.15% and (ii) within 0.17% of the exact value; (iii) misses it by 10–20%.
  - Splittings of the near-degenerate pairs ($`E_b(P+\pi)=E_b(P)`$): (i) reproduces the first to 0.2–1.2% and the second to 3.5–10%; (ii) misses them by up to a factor 30. So the main spacing tests the product $`E_b''W_0''`$, while only (i) tests the complete first-order projected contract.
  - The common level offsets ($`\approx10^{-5}`$) scale as $`g_s^2`$.
  - $`\Delta W_0/(\Delta W_1+\Delta W_2)`$ is 0.84–0.87 at these couplings and tends to 1 as they are scaled down (0.997 at scale 0.03), as in (6.12).

  Second part, sets A and D at $`L=24`$: the script computes $`a(0)=-\langle[H,[H,\hat Z]]\rangle`$ exactly in the position-space band contract (exact Schrieffer–Wolff amplitudes, held weights), for $`\hat Z=\hat Y`$ of (6.18) and for the midpoint. The start is $`\varphi(Y)f_0`$ with a Gaussian envelope of width $`w=1,1.5,2`$ centred at $`L/4`$. Results:
  - Set A, with the couplings in the weights scaled by 0.05 (first order in $`g_i`$): the first-order part of $`a_Y`$ over the right side of (6.13) is 0.88, 0.95, 0.97, a trend $`O(w^{-2})`$. At full couplings it is 0.90–0.99. The $`g_s`$-independent part is up to 0.6% of the first-order part at full couplings; with the profile cut at $`\lvert r\rvert<L/3`$ it drops to $`10^{-4}`$.
  - Set D ($`g_1+g_2=0`$): $`a_Y`$ over the leading form of (7.7) for body 1 alone at the same place is 0.084–0.087, 0.025–0.027 and 0.008–0.009 for the couplings in the weights scaled by 1, 0.3, 0.1. It is linear in the scale, so the pair falls at second order and each body at first. $`a_Y`$ over the factorized form $`-E''_{\rm line}\sum\varphi^2W'_0`$ is 1.9–2.2 at all scales and widths.

  Outputs: `code/v3/output/weight_check.txt`, `code/v3/output/weight_check.json`.

## Methods used

- band contract (second-order Schrieffer–Wolff), plane-wave sectors of the joint translation
- gauge reduction of a chain to bond magnitudes and one flux; Hellmann–Feynman theorem
- Perron–Frobenius; Cauchy–Schwarz
- second-order perturbation theory; Airy functions (continuum limit of a linear potential), virial theorem
- controlled inversion of a weighted harmonic mean; sign analysis of coefficients; scaling families of descriptions
- reflection symmetry; double commutator for the acceleration from rest; band projection with momentum-dependent eigenvectors
- exact diagonalization (dense and shift-invert sparse) for the code checks
