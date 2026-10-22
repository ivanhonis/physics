# Two free bodies under the field they make

- **Subproject:** 07-ilang-weight
- **Package:** 02-two-free-bodies
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-20

## Setup and assumptions

- **Field** (assumption, M8): $`N_f\ge1`$ identical field objects ($`c=+1`$) on the ring $`\mathbb Z_L`$, $`L\ge5`$, no pair terms among them, own term $`C_1=-t_f\sum_x(\lvert x\rangle\langle x+1\rvert+\mathrm{h.c.})`$, $`t_f>0`$; $`\Phi_x`$ the number of field objects at $`x`$, $`n:=N_f/L`$.
- **Bodies** (assumption): Model D bodies $`b_1,b_2`$ on the same ring of position labels, in clock levels $`k_i`$ with half-gaps $`M_i:=M^{(i)}_{k_i}>0`$, motion amplitudes $`\tau_i`$, each coupled by (a) or (c) with a real constant $`\gamma_i`$ (either sign); no pair term between $`b_1`$ and $`b_2`$; records at $`\kappa\to0`$ (medium terms dropped). Write $`S_i:=\sigma_3\otimes(m_i\mathbb 1+D_i)`$, $`\Gamma_i`$ the coupling term of $`b_i`$, $`A_i'`$ its motion term ($`A_i`$ for (a); $`A_i`$ plus its $`\gamma_i`$-part for (c)), and
```math
g_i:=\sigma_i\gamma_iM_i ,\qquad \sigma_i\in\{+1,-1\}\ \text{the branch of } b_i.
```
- **Held bodies** (A15): $`\tau_i=0`$ at fixed $`x_1,x_2`$. **Field state** (M9): lowest; highest where stated.
- **Inputs** (quoted in question.md): (4.2), (4.4) of 06-ilang-source/04-profile ($`M`$, $`M^{(2)}=-\frac{2ng_1g_2}{t_f}\Lambda^+(x_1,x_2)`$, $`\Lambda^+`$ the pseudo-inverse of the ring Laplacian $`\Delta`$); (6.10) of 06-ilang-source/06-own-mark (dressed curvature $`E''_{k,\sigma}(0)`$, error $`O(\gamma^3)`$); (7.1), (7.2), (7.7) of 06-ilang-source/07-dressed-fall.
- **Regime of item 3** (assumption, named R): **R1** (isolated band) in each sector of the conserved labels of Step 1 the $`\tau=0`$ group $`\mathcal G=\{e_{jl}\}`$, $`e_{jl}:=\lvert j\,\sigma_1k_1,\ l\,\sigma_2k_2\rangle\otimes\Omega_{jl}`$ ($`\Omega_{jl}`$ the lowest, resp. highest, field state of the held problem with $`b_1`$ at $`j`$, $`b_2`$ at $`l`$) is separated from all other $`\tau=0`$ levels by a gap $`\delta>0`$, and $`\tau_i\ll\delta`$; **R2** (order) accelerations at order $`\tau_i^2`$, relative errors $`O(\tau^2/\delta^2)`$; **R3** (starts) $`\Psi(0)=\mathcal U\psi`$, $`\psi=\sum_{j,l}\phi^1_j\phi^2_l\,e_{jl}`$ with real normalized envelopes, $`\mathcal U`$ the band transformation of Step 4. *First order in the place dependence* means: linear in quantities that vanish when the other body is uncoupled (the mutual term $`M`$ and the change of a body's hopping caused by the other body).
- **Gauges.** $`\Omega_{jl}`$ is real, positive for the lowest state (Perron–Frobenius) and $`(-1)^y`$-positive for the highest (on every object). With $`U_b=\mathrm{diag}(1,i)`$ on each branch label, $`U_b\sigma_1U_b^\dagger=\sigma_2`$, so $`C`$ is a real matrix and a real start has $`\langle i[C,x_i]\rangle=0`$: it starts from rest.

## Derivation

### Step 1. Conserved quantities (item 1)

Let $`\mathcal T:=T^{(b_1)}T^{(b_2)}\prod_\alpha T^{(\alpha)}`$, $`T\lvert x\rangle=\lvert x+1\rangle`$ on every position label. $`A_i`$, $`B_i`$ and $`C_1`$ are built from $`\sum_x\lvert x+1\rangle\langle x\rvert`$ and $`\sum_x\lvert x\rangle\langle x\rvert`$; under $`\mathcal T`$ the couplings go to $`\sum_xP^{(i)}_{x+1}\otimes S_i\otimes\Phi_{x+1}`$ and the (c) bond factors $`\tfrac12(\Phi_x+\Phi_{x+1})`$ to those of the shifted bond. $`\mathcal T`$ commutes with the swaps of field objects. Hence
```math
[\mathcal T,C]=0,\qquad \mathcal T^L=\mathbb 1,\qquad \mathcal T=e^{-i\hat P},\quad P=p_1+p_2+\textstyle\sum_\alpha q_\alpha\in\tfrac{2\pi}{L}\mathbb Z_L , \qquad\text{(2.1)}
```
the total plane-wave label of bodies and field is conserved. Further: $`C`$ acts on the clock label of $`b_i`$ only through $`\mathbb 1`$ and $`D_i`$, so $`[D_i,C]=0`$ and $`k_i`$ is conserved; the joint reflection $`\mathcal R`$ ($`x\to-x`$ on all labels, times $`\sigma_3`$ on both branch labels) commutes with $`C`$ (the reversal flips the sign of the $`\sigma_1`$ terms, $`\sigma_3`$ flips it back) and $`\mathcal R\mathcal T\mathcal R^\dagger=\mathcal T^{-1}`$, so every level satisfies $`E(P)=E(-P)`$; $`C`$ itself and $`\sum_x\Phi_x=N_f`$ are conserved. **Bodies alone.** For $`\mathcal T_b:=T^{(b_1)}T^{(b_2)}`$, which commutes with $`C_{\rm D}^{(i)}`$ and $`C_1`$,
```math
\mathcal T_bC\mathcal T_b^\dagger-C=\sum_i\gamma_i\sum_xP^{(i)}_x\otimes S_i\otimes(\Phi_{x-1}-\Phi_x)\;+\;(\text{(c): bond terms, off-diagonal in }x_i)\neq0 \qquad\text{(2.2)}
```
whenever $`(\gamma_1,\gamma_2)\ne0`$: $`S_i`$ is invertible ($`m_i>0`$), $`\Phi_{x-1}\neq\Phi_x`$, and terms on different position labels, or diagonal and off-diagonal ones, cannot cancel. So the plane-wave label of the bodies is not conserved (the field takes the recoil); the bodies alone conserve their clock levels $`k_1,k_2`$, and, when held, also $`x_i`$ and $`\sigma_i`$ ($`C`$ is then diagonal in them).

### Step 2. Held bodies: exact form (item 2)

At $`\tau_i=0`$ couplings (a) and (c) coincide (the (c) addition is proportional to $`\tau_i`$). In the sector $`(x_i,\sigma_i,k_i)`$, $`S_i=\sigma_iM_i`$ and $`C=\sigma_1M_1+\sigma_2M_2+\sum_\alpha h^{(\alpha)}`$ with $`h=C_1+g_1P_{x_1}+g_2P_{x_2}`$, i.e. (7.1) with $`g_b\to g_1`$, $`g_s\to g_2`$. Without pair terms the field eigenvalues are $`\sum_jn_j\varepsilon_j(h)`$, $`\sum_jn_j=N_f`$. By Perron–Frobenius ($`-h`$ irreducible with non-negative off-diagonal entries) $`\varepsilon_0(h)`$ is simple for all real $`g_i`$, hence analytic and connected to $`\gamma_i=0`$:
```math
E(x_1,x_2)=\sigma_1M_1+\sigma_2M_2+N_f\,\varepsilon_0(x_1,x_2)=\mathrm{const}+M(x_1,x_2), \qquad\text{(2.3)}
```
with $`M`$ of (4.2); the one-body terms do not depend on the positions because $`C_1`$ is translation invariant. The ring maps $`x\to x+a`$ and $`x\to x_1+x_2-x`$ leave $`C_1`$ invariant, the second exchanges the two places. Hence, **exactly** (every order in $`g_i`$):
```math
M(x_1,x_2)=\mathcal M(\lvert x_2-x_1\rvert_L),\qquad M(g_1@x_1,g_2@x_2)=M(g_1@x_2,g_2@x_1),\qquad F_1=-F_2 , \qquad\text{(2.4)}
```
where $`F_i:=-\tfrac12[E(x_i+1)-E(x_i-1)]`$ (other label fixed): for $`E=f(x_2-x_1)`$, $`F_1=-\tfrac12[f(d-1)-f(d+1)]=-F_2`$. The force with which $`b_1`$ acts on $`b_2`$ is opposite and equal to that with which $`b_2`$ acts on $`b_1`$. **Highest state.** For even $`L`$, $`U_f:=\prod_\alpha(-1)^{y_\alpha}`$ gives $`U_fC_1U_f=-C_1`$, $`U_f\Phi_xU_f=\Phi_x`$, and $`\sigma_2`$ anticommutes with $`\sigma_1,\sigma_3`$; so $`\mathcal W:=U_f\,\sigma_2^{(1)}\sigma_2^{(2)}`$ satisfies
```math
\mathcal WC\mathcal W^\dagger=-C,\qquad M_{\rm top}(g_1,g_2)=-M_{\rm low}(-g_1,-g_2)\quad(L\ \text{even}). \qquad\text{(2.5)}
```
The $`(\sigma_1,\sigma_2,\text{highest})`$ problem is the $`(-\sigma_1,-\sigma_2,\text{lowest})`$ problem with $`C\to-C`$; since $`e^{-iC\lambda}\mathcal W\Psi=\mathcal We^{iC\lambda}\Psi`$, accelerations from rest are equal. Odd $`L`$: Open issues.

### Step 3. The mutual term order by order (item 2)

Lowest state (highest: by (2.5)). $`C_1+2t_f=t_f\Delta`$, the lowest one-object state is uniform $`u`$, the gap is $`4t_f\sin^2(\pi/L)`$, and the reduced resolvent is $`R=-\Lambda^+/t_f`$. Rayleigh–Schrödinger perturbation theory in $`V=g_1P_{x_1}+g_2P_{x_2}`$ ($`\lVert V\rVert\le\lvert g_1\rvert+\lvert g_2\rvert`$) converges for $`\lvert g_1\rvert+\lvert g_2\rvert<2t_f\sin^2(\pi/L)`$ (Kato). On the ring ($`D=1`$), with $`u:=d(L-d)`$, $`d\in\{0,\dots,L-1\}`$:
```math
\Lambda^+(d)=\frac{L^2-1}{12L}-\frac{u}{2L},\qquad (\Lambda^+)^2(d)=\frac{(L^2-1)(L^2+11)}{720L}-\frac{u}{12L}-\frac{u^2}{24L}. \qquad\text{(2.6)}
```
Proof: the second differences of $`u`$ and $`u^2`$ are $`-2`$ and $`2L^2+2-12u`$ (use $`(L-2d)^2=L^2-4u`$) for $`d\neq0`$, so $`\Delta`$ maps the right-hand sides to $`\delta_{d0}-\frac1L`$ and to $`\Lambda^+(d)`$; the constants give zero mean ($`\sum_du=L(L^2-1)/6`$, $`\sum_du^2=L(L^4-1)/30`$). With (4.4):
```math
M^{(2)}(d)=-\frac{2n}{t_f}g_1g_2\Lambda^+(d)=\frac{n\,g_1g_2}{6t_fL}\bigl[6u-(L^2-1)\bigr]. \qquad\text{(2.7)}
```
Third order: $`E^{(3)}=\langle u\vert VRVRV\vert u\rangle-E^{(1)}\langle u\vert VR^2V\vert u\rangle`$, $`V\lvert u\rangle=L^{-1/2}\sum_ig_i\lvert x_i\rangle`$, $`E^{(1)}=(g_1+g_2)/L`$. Keeping the terms containing both $`g_1`$ and $`g_2`$ and using (2.6) ($`\Lambda_d:=\Lambda^+(d)`$, $`(\Lambda^2)_d:=(\Lambda^+)^2(d)`$):
```math
M^{(3)}(d)=\frac{n}{t_f^2}g_1g_2(g_1+g_2)\Bigl[\Lambda_d^2+2\Lambda_0\Lambda_d-\tfrac{(\Lambda^2)_0+2(\Lambda^2)_d}{L}\Bigr]=\frac{n\,g_1g_2(g_1+g_2)}{60\,t_f^2L^2}\bigl[20u^2-10(L^2-2)u+(L^2-1)(L^2-4)\bigr]. \qquad\text{(2.8)}
```
**Product form.** At second order $`M^{(2)}=g_1\cdot g_2\cdot F_2(d)`$, $`F_2=-2n\Lambda^+/t_f`$: one number per body ($`g_i`$, the same for acting and for being acted upon) times one function of $`d`$, for every pair of the class. At third order it fails:
```math
\nexists\ p_1(g_1),\,p_2(g_2),\,F(d):\quad M=p_1p_2F(d)+O(g^4)\ \text{for all }g_1,g_2\text{ near }0 . \qquad\text{(2.9)}
```
Proof: such a form makes $`M(d)/M(0)=F(d)/F(0)`$ independent of $`g_i`$ ($`M^{(2)}(0)\ne0`$ since $`\Lambda_0>0`$). Expanding, the $`O(g_1+g_2)`$ term of $`M(d)/M(0)`$ vanishes only if $`B_3(d)\Lambda_0=B_3(0)\Lambda_d`$ for all $`d`$, with $`B_3`$ the bracket of (2.8). $`B_3`$ is quadratic in $`u`$ with leading coefficient $`1/(3L^2)\neq0`$, $`\Lambda`$ is linear in $`u`$, and $`u`$ takes the three distinct values $`0,L-1,2L-4`$ at $`d=0,1,2`$ ($`L\ge5`$): impossible. (Among pairs with $`g_1g_2\neq0`$, $`M^{(3)}\equiv0`$ only for $`g_1+g_2=0`$.)
**Controls.** (2.4) fails in the wider class with a non-uniform on-site field term $`\sum_xv_x\Phi_x`$: the one-body terms then depend on $`x_i`$ and $`F_1+F_2\neq0`$. The second-order product form has no control in the class ((2.7) holds for all its members); its failure at third order is (2.9).

### Step 4. Band dynamics of the free bodies (item 3)

By R1 there is a Schrieffer–Wolff unitary $`\mathcal U=e^{S}`$, $`S=-S^\dagger=O(\tau/\delta)`$ off-diagonal with respect to the projector $`\mathcal P_0`$ on $`\mathcal G`$, such that $`H:=\mathcal U^\dagger C\mathcal U`$ is block diagonal; the band is $`\mathcal U\,\mathrm{Ran}\,\mathcal P_0`$ (standard). In the basis $`e_{jl}`$:
```math
H_{\rm eff}=\mathcal P_0H\mathcal P_0=W+K_1+K_2+O(\tau^4),\qquad W=\mathrm{diag}\,E(j,l)\ \text{of (2.3)}. \qquad\text{(2.10)}
```
$`\mathcal P_0A_i'\mathcal P_0=0`$ because $`A_i'\propto\sigma_1`$ flips $`\sigma_i`$; so the first-order part is $`W`$, and $`K_i`$, the second-order term of $`A_i'`$, moves $`b_i`$ by $`r\in\{0,\pm2\}`$ and leaves the other body fixed (a product $`A_1'A_2'`$ flips both branches and leaves $`\mathcal G`$). In the real gauge $`K_1`$ is real symmetric; let $`\kappa(j,l):=\langle e_{j+1,l}\vert K_1\vert e_{j-1,l}\rangle=\bar\kappa+\delta\kappa(j,l)`$, where $`\bar\kappa`$ is the same amplitude for $`b_1`$ alone with the field and $`\delta\kappa\to0`$ as $`g_2\to0`$. For $`b_1`$ alone the Bloch sums $`\sum_je^{iPj}e_j`$ have total label $`P`$ (2.1), so its dressed level is $`E_{k_1,\sigma_1}(P)=\sum_r\bar\kappa_re^{-iPr}`$ with $`r\in\{0,\pm2\}`$ at order $`\tau^2`$, and
```math
E''_{k_1,\sigma_1}(0)=-\textstyle\sum_rr^2\bar\kappa_r=-8\bar\kappa , \qquad\text{(2.11)}
```
the curvature (6.10). The same holds for $`b_2`$. For the highest state ($`L`$ even) the gauge gives $`\mathcal Te_j=(-1)^{N_f}e_{j+1}`$, which shifts $`P`$ by $`\pi N_f`$ but does not change (2.11) since $`r`$ is even, and by (2.5) $`E''_{\rm top,\sigma}=-E''_{{\rm low},-\sigma}`$, of sign $`\sigma`$.

### Step 5. Accelerations from rest (item 3)

$`a_1:=\frac{\mathrm d^2}{\mathrm d\lambda^2}\langle x_1\rangle\big|_0=-\langle\Psi\vert[C,[C,x_1]]\vert\Psi\rangle=-\langle\psi\vert[H_{\rm eff},[H_{\rm eff},X_1]]\vert\psi\rangle`$, $`X_1:=\mathcal P_0\mathcal U^\dagger x_1\mathcal U\mathcal P_0`$, because $`H`$ is block diagonal and $`\psi\in\mathrm{Ran}\,\mathcal P_0`$. Write $`S=S_++S_-+S_2`$ (parts moving $`b_1`$ by $`\pm1`$, and moving $`b_2`$). Then $`[x_1,S_\pm]=\pm S_\pm`$, $`\mathcal P_0[x_1,S]\mathcal P_0=0`$, and $`\tfrac12\mathcal P_0[[x_1,S],S]\mathcal P_0=\mathcal P_0[S_+,S_-]\mathcal P_0`$ moves nobody: $`X_1=x_1+\xi_1`$ with $`\xi_1`$ diagonal in $`e_{jl}`$ and $`O(\tau^2/\delta^2)`$. Since $`W,x_1,\xi_1`$ are diagonal and $`[K_2,x_1]=0`$, $`a_1=-\langle\psi\vert[W,[K_1,x_1]]\vert\psi\rangle+O(\tau^4)`$. With $`\langle e_{j\pm1,l}\vert[K_1,x_1]\vert e_{j\mp1,l}\rangle=\mp2\kappa(j,l)`$ this gives $`a_1=8\sum_{j,l}\kappa\,\phi^1_{j+1}\phi^1_{j-1}(\phi^2_l)^2\,\partial_1W`$. At first order in the place dependence $`\kappa\to\bar\kappa`$, and by (2.11):
```math
a_1=-E''_{k_1,\sigma_1}(0)\sum_{j,l}\phi^1_{j+1}\phi^1_{j-1}(\phi^2_l)^2\,\partial_1W(j,l),\qquad a_2=-E''_{k_2,\sigma_2}(0)\sum_{j,l}(\phi^1_j)^2\phi^2_{l+1}\phi^2_{l-1}\,\partial_2W(j,l), \qquad\text{(2.12)}
```
with $`\partial_1W(j,l):=\tfrac12[W(j+1,l)-W(j-1,l)]`$, $`\partial_2`$ likewise, $`W`$ the exact held eigenvalue (2.3) (lowest or highest), at order $`\tau_i^2`$ with relative errors $`O(\tau^2/\delta^2)`$, and $`\partial_2W=-\partial_1W=\mathcal M'(l-j):=\tfrac12[\mathcal M(d+1)-\mathcal M(d-1)]`$ by (2.4).

### Step 6. Ratio, inertias, rest costs and directions (item 3)

For real Gaussian envelopes $`\phi^i_j\propto e^{-(j-\bar x_i)^2/4w_i^2}`$ (width $`w_i\ll L`$), $`\phi^i_{j+1}\phi^i_{j-1}=e^{-1/2w_i^2}(\phi^i_j)^2`$ exactly on $`\mathbb Z`$, so both sums in (2.12) are $`\mp e^{-1/2w_i^2}\sum_{j,l}(\phi^1_j\phi^2_l)^2\mathcal M'(l-j)`$ and
```math
\frac{a_1}{a_2}=-\frac{E''_{k_1,\sigma_1}(0)}{E''_{k_2,\sigma_2}(0)}\,e^{(w_2^{-2}-w_1^{-2})/2},\qquad w_1=w_2:\ \ \frac{a_1}{a_2}=-\frac{\mu_2}{\mu_1},\quad \mu_1a_1+\mu_2a_2=0,\quad \mu_i:=\frac1{E''_{k_i,\sigma_i}(0)} . \qquad\text{(2.13)}
```
This holds for the exact $`M`$ (every order in $`g_i`$) and to the order to which $`E''`$ is known ((6.10): $`O(\gamma^3)`$). For other envelopes the factor is $`\langle\mathcal M'\rangle_1/\langle\mathcal M'\rangle_2`$ with the weights of (2.12). **Rest costs.** Let $`R_i`$ be half the difference of the $`\tau=0`$ eigenvalues of $`b_i`$ alone in its two branches (field lowest), a difference of eigenvalues (M6): $`R_i=M_i+\tfrac{N_f}2[\varepsilon_0(\gamma_iM_i)-\varepsilon_0(-\gamma_iM_i)]=M_i(1+\gamma_in)+O(\gamma_i^3)`$, since the odd part of $`\varepsilon_0(g)`$ is $`g/L+O(g^3)`$. From (6.10), $`\frac1{1-x+x^2}=1+x+O(x^3)`$ and $`\Delta''=O(\gamma^2)`$:
```math
\mu_i=\sigma_i\frac{R_i}{\tau_i^2}+O(\gamma_i^2)\ \ \text{(a)},\qquad \mu_i=\sigma_i\frac{R_i}{\tau_i^2(1+\gamma_in)^2}+O(\gamma_i^2)\ \ \text{(c)}, \qquad\text{(2.14)}
```
so for $`w_1=w_2`$, $`a_1/a_2=-\sigma_1\sigma_2\,(R_2/\tau_2^2)/(R_1/\tau_1^2)\,[1+O(\gamma^2)]`$ for (a), with $`\tau_i\to\tau_i(1+\gamma_in)`$ for (c). **Directions.** By (2.7), for $`1\le d\le L-1`$, $`\mathcal M'(d)=\frac{ng_1g_2}{t_fL}(L-2d)`$ at second order (exact central difference of a quadratic), $`\mathcal M'(0)=0`$. Take $`\bar x_1<\bar x_2`$ with the separations concentrated in $`0<d<L/2`$ (shorter arc). Then $`a_1=E''_1\langle\mathcal M'\rangle_1`$ and $`a_2=-E''_2\langle\mathcal M'\rangle_2`$ with $`\langle\mathcal M'\rangle_i`$ of the sign of $`g_1g_2=\sigma_1\sigma_2\gamma_1\gamma_2M_1M_2`$, and $`\mathrm{sgn}E''_i=\sigma_i`$ for small $`\gamma_in`$ (6.10). Hence, at second order in the couplings:
```math
\text{lowest state: towards each other}\iff\sigma_1=\sigma_2=\mathrm{sgn}(\gamma_1\gamma_2);\quad\text{apart}\iff\sigma_1=\sigma_2=-\mathrm{sgn}(\gamma_1\gamma_2);\quad \sigma_1\neq\sigma_2:\ \mathrm{sgn}a_1=\mathrm{sgn}a_2 , \qquad\text{(2.15)}
```
and for the highest state ($`L`$ even) the same with $`\sigma_i\to-\sigma_i`$, by (2.5).

### Step 7. Where the ratio deviates from the ratio of inertias (item 3)

At first order in the place dependence (2.13) holds for equal widths. The first coupling-dependent deviation is $`\delta\kappa`$, the change of $`b_1`$'s hopping caused by $`b_2`$; it multiplies $`\partial W`$ and is thus of second order in the place dependence. Leading term, coupling (a): in $`\kappa`$ the intermediate states are $`b_1`$ at $`j`$ in branch $`-\sigma_1`$ with field states $`\chi`$; expanding the symmetrized denominators $`2\sigma_1M_1+(\varepsilon_{\Omega}-\varepsilon_\chi)`$ around $`2\sigma_1M_1`$ and using $`\sum_\chi\lvert\chi\rangle\langle\chi\rvert(\varepsilon_{\Omega_{j\mp1,l}}-\varepsilon_\chi)\Omega_{j\mp1,l}=g_1(\Phi_{j\mp1}+\Phi_j)\Omega_{j\mp1,l}`$ gives $`\kappa\propto\langle\Omega_{j+1,l}\vert\Omega_{j-1,l}\rangle-\frac{\gamma_1}{4}\langle\Omega_{j+1,l}\vert\Phi_{j-1}+2\Phi_j+\Phi_{j+1}\vert\Omega_{j-1,l}\rangle+O(\gamma_1^2)`$. At leading order in $`g_1`$ the matrix element is the field density $`n+\delta\rho_l(y)`$ made by $`b_2`$ alone; the overlap depends on $`l`$ only at $`O(g_1^2g_2)`$. For (c) the bond factors add $`+2\gamma_1\times`$ the same average. Hence
```math
\frac{\delta\kappa(j,l)}{\bar\kappa}=\mp\gamma_1\,\overline{\delta\rho}_l(j)\,[1+O(\gamma_1)],\qquad \overline{\delta\rho}_l(j):=\tfrac14[\delta\rho_l(j-1)+2\delta\rho_l(j)+\delta\rho_l(j+1)],\qquad \gamma_1\delta\rho_l(y)=\frac{\sigma_1M^{(2)}(y,l)}{M_1}+O(g_2^2), \qquad\text{(2.16)}
```
upper sign (a), lower (c) (the last identity: $`\delta\rho_l(y)=-\frac{2ng_2}{t_f}\Lambda^+(y-l)`$ at first order, so $`g_1\delta\rho_l=M^{(2)}`$; highest state likewise with $`M^{(2)}_{\rm top}`$). Each $`a_i`$ of (2.12) acquires the factor $`1\mp\gamma_i\overline{\delta\rho}`$ inside its sum, and for broad equal-width starts the ratio becomes $`-\frac{\mu_2}{\mu_1}\bigl[1\mp\bar M^{(2)}(\bar d)\bigl(\frac{\sigma_1}{M_1}-\frac{\sigma_2}{M_2}\bigr)\bigr]`$: a deviation of relative order $`\gamma_1\gamma_2`$, which vanishes for $`\sigma_1=\sigma_2`$, $`M_1=M_2`$. Each body's inertia is changed in place by the other's mark. **Controls** of (2.13): unequal widths (factor $`e^{(w_2^{-2}-w_1^{-2})/2}`$), and (2.16).

## Result

- **(2.1)–(2.2)** [class: both couplings, all $`N_f\ge1`$, $`L\ge5`$; exact] Conserved: the total plane-wave label $`P`$ of bodies and field (joint translation $`\mathcal T`$), the clock levels $`k_1,k_2`$ ($`D_1,D_2`$), $`C`$, $`\sum_x\Phi_x`$; the joint reflection maps $`P\to-P`$. The plane-wave label of the bodies alone is not conserved for $`(\gamma_1,\gamma_2)\ne0`$; held bodies also conserve $`x_i,\sigma_i`$.
- **(2.3)–(2.4)** [held bodies, both couplings, lowest (likewise highest) state; exact, every order in $`g_i`$] The eigenvalue is $`\sigma_1M_1+\sigma_2M_2+N_f\varepsilon_0`$; it depends on the positions only through the ring distance, is unchanged when the two bodies exchange places, and $`F_1=-F_2`$ (action equals reaction).
- **(2.5)** [$`L`$ even, exact] $`\mathcal WC\mathcal W^\dagger=-C`$: the highest field state with branches $`(\sigma_1,\sigma_2)`$ is the lowest with $`(-\sigma_1,-\sigma_2)`$ and $`C\to-C`$; $`M_{\rm top}(g_1,g_2)=-M_{\rm low}(-g_1,-g_2)`$.
- **(2.6)–(2.8)** [ring, lowest state, $`\lvert g_1\rvert+\lvert g_2\rvert<2t_f\sin^2(\pi/L)`$] Closed forms of $`\Lambda^+`$, $`(\Lambda^+)^2`$, $`M^{(2)}`$ and $`M^{(3)}`$.
- **(2.9)** [same class] At second order the mutual term is a product $`g_1g_2F_2(d)`$ (yes); at third order no product $`p_1(g_1)p_2(g_2)F(d)`$ exists (no); $`M^{(3)}=0`$ for pairs with $`g_1+g_2=0`$.
- **(2.11)–(2.12)** [regime R1–R3, both couplings, lowest or (even $`L`$) highest state; order $`\tau_i^2`$, first order in the place dependence, relative errors $`O(\tau^2/\delta^2)`$] The drift accelerations from rest are $`a_i=-E''_{k_i,\sigma_i}(0)\times`$ the envelope-weighted symmetric gradient of the exact held eigenvalue, with $`E''`$ the curvature (6.10) of the isolated dressed body.
- **(2.13)–(2.14)** [same, real Gaussian envelopes of widths $`w_i\ll L`$, $`\sum_{j,l}(\phi^1_j\phi^2_l)^2\mathcal M'(l-j)\neq0`$] $`a_1/a_2=-(E''_1/E''_2)e^{(w_2^{-2}-w_1^{-2})/2}`$; for equal widths $`a_1/a_2=-\mu_2/\mu_1`$ and $`\mu_1a_1+\mu_2a_2=0`$, for every order in $`g_i`$ of the mutual term and to the order of (6.10); $`\mu_i=\sigma_iR_i/\tau_i^2+O(\gamma_i^2)`$ for (a), $`\mu_i=\sigma_iR_i/[\tau_i(1+\gamma_in)]^2+O(\gamma_i^2)`$ for (c), $`R_i`$ the rest cost.
- **(2.15)** [same, second order in the couplings, small $`\gamma_in`$, separations on the shorter arc] Lowest state: towards each other iff $`\sigma_1=\sigma_2=\mathrm{sgn}(\gamma_1\gamma_2)`$, apart iff $`\sigma_1=\sigma_2=-\mathrm{sgn}(\gamma_1\gamma_2)`$, same direction iff $`\sigma_1\ne\sigma_2`$; highest state ($`L`$ even): $`\sigma_i\to-\sigma_i`$.
- **(2.16)** [same; second order in the place dependence, leading order in $`\gamma_1`$] The first coupling-dependent deviation of the ratio from $`-\mu_2/\mu_1`$: the hopping of each body is changed by the other's mark by the relative amount $`\mp\gamma_i\overline{\delta\rho}`$, giving a relative deviation of order $`\gamma_1\gamma_2`$, $`\mp\bar M^{(2)}(\sigma_1/M_1-\sigma_2/M_2)`$ for broad equal-width starts.

## Consistency checks

1. **Dimensions.** $`C,\tau_i,M_i,t_f,g_i\sim\lambda^{-1}`$; $`\gamma_i,n,\Lambda^+`$ dimensionless; $`M^{(2)}\sim g^2/t_f`$, $`M^{(3)}\sim g^3/t_f^2\sim\lambda^{-1}`$; $`E''\sim\tau^2/M\sim\lambda^{-1}`$, so $`a_i\sim\lambda^{-2}`$ as $`\mathrm d^2\langle x\rangle/\mathrm d\lambda^2`$ with dimensionless $`x`$.
2. **Held source and test body.** For $`\tau_2\to0`$ and $`\phi^2_l=\delta_{l,x_s}`$, (2.12) is (7.7) with $`W`$ of (7.2), $`g_s=g_2`$. For $`\gamma_1\to0`$: $`a_1=-(\sigma_1\tau_1^2/M_1)\langle\partial_1M^{(2)}\rangle=-\tau_1^2\gamma_1\langle\partial_1\delta\rho\rangle`$, independent of $`\sigma_1`$ and $`k_1`$: the common local scale of 06-ilang-source at leading order.
3. **Equal bodies.** Same type, coupling, $`\gamma`$, branch and widths, mirror-symmetric start: $`a_1=-a_2`$ by the exchange symmetry, and (2.13) gives $`-\mu_2/\mu_1=-1`$.

## Open issues

- Odd $`L`$, highest state: the highest one-object level of $`C_1`$ is twofold degenerate; the mutual term then starts at first order in $`g`$ and is not treated.
- The coefficient of (2.16) beyond its leading order in $`\gamma_i`$ is not derived; the code finds corrections of relative first order in $`\gamma_i`$ that are large for coupling (c).
- R1 is assumed: for large $`N_f`$ the isolation from multi-object field excitations at distance $`2M_i`$ is not derived.
- Whether (2.13) holds beyond order $`\tau^2`$ for broad starts is not derived.

## Code

- `code/v1/check_held_pair.py` (check of Steps 2–3): $`N_f=1`$, $`L=8`$ and $`L=13`$, $`t_f=1`$, unequal $`(g_1,g_2)=(0.04,-0.07),(0.05,-0.03),(0.03,0.06)`$; exact $`M`$ from the lowest eigenvalue with two held point terms. Output `code/v1/output/held_pair.json`, `held_pair.log`. Results: (2.6) to $`6\cdot10^{-15}`$; translation, reflection, exchange, $`F_1+F_2=0`$ and the map (2.5) to $`4\cdot10^{-15}`$; $`\max\lvert M-M^{(2)}-M^{(3)}\rvert`$ falls by $`15.9`$–$`16.4`$ when $`g`$ is halved ($`O(g^4)`$); the odd part of $`M`$ in $`g`$ matches $`M^{(3)}`$ to $`O(g^5)`$; (odd part)$`/M^{(2)}`$ varies with $`d`$ (e.g. $`L=13`$: $`-0.003`$ to $`-0.056`$), as (2.9) requires.
- `code/v1/check_mutual_fall.py` (check of Steps 4–7): $`N_f=1`$, $`L=14`$, $`t_f=0.5`$, two Model D bodies and the field object, diagonalized in the $`L`$ sectors of (2.1); start (R3) by projecting $`\psi`$ on the band; exact $`a_i=i\langle[C,v_i]\rangle`$ and the slope of $`\langle v_i\rangle(\lambda)`$ from the joint evolution; prediction (2.12) with $`E''_i`$ from the band of the single body with the field. Output `code/v1/output/mutual_fall.json`, `mutual_fall.log`. Cases (R1 holds: $`2M_i-4t_f\ge1.2`$): A (a), $`\sigma=(+,+)`$, lowest; B (c), $`(+,-)`$, lowest; C (a), $`(-,-)`$, highest; D (c), $`(+,+)`$, widths $`1.1,1.6`$; E (c), $`(+,+)`$; A and E also with $`\gamma_i/2`$; $`M_i\in[1.6,3]`$, $`\gamma_i\in[0.01,0.03]`$, $`\tau_i=s\,(0.08\text{–}0.15)`$, $`s=1,\tfrac12,\tfrac14`$; centres $`3,8`$; equal widths $`1.3`$. Results: $`v_i(0)\le10^{-17}`$ (from rest); evolution slope = exact $`a_i`$ to $`2.4\cdot10^{-7}`$; (2.12) matches the exact $`a_i`$ to $`2.0\cdot10^{-3}`$ at $`s=1`$ and $`1.2\cdot10^{-4}`$ at $`s=\tfrac14`$ (the $`\tau^2`$ decrease of R2); $`a_1/a_2`$ matches $`-E''_1/E''_2`$ for equal widths to $`3.0\cdot10^{-4}`$ ($`s=1`$), $`5\cdot10^{-5}`$ ($`s=\tfrac14`$); D: $`a_1/a_2=-0.53682`$ against $`-E''_1/E''_2=-0.66719`$, factor $`0.8046`$ against $`e^{(w_2^{-2}-w_1^{-2})/2}=0.8042`$ (ring wrap); C reproduces A to all printed digits ((2.5)); A, C, D, E move towards each other, B in the same direction ((2.15)). The $`\tau^2`$ coefficient of $`a_i/(2.12)-1`$ (fit in $`s^2,s^4`$) against the leading term of (2.16): A $`(-4.76,-3.61)`$ vs $`(-4.80,-3.29)`$, A at $`\gamma/2`$ $`(-1.13,-0.80)`$ vs $`(-1.16,-0.78)`$, E $`(3.28,1.71)`$ vs $`(4.80,3.29)`$, E at $`\gamma/2`$ $`(0.97,0.60)`$ vs $`(1.16,0.78)`$, all $`\times10^{-5}`$: the deviation scales as $`\gamma_1\gamma_2`$ and the leading term is approached linearly in $`\gamma`$; ratio deviations: A $`-1.15`$ vs $`-1.51`$, E $`1.57`$ vs $`1.51`$, B $`-6.39`$ vs $`-6.81`$ ($`\times10^{-5}`$).

## Methods used

- translation, reflection and sublattice symmetries; Perron–Frobenius
- Rayleigh–Schrödinger perturbation theory; lattice Green function of the ring
- Schrieffer–Wolff (quasi-degenerate) perturbation theory; Heisenberg equations for mean positions
- Gaussian envelope identities; numerical diagonalization by sectors
