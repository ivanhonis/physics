# Weight of a bond made through the field

- **Subproject:** 07-ilang-weight
- **Package:** 04-weight-of-bond
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-21

## Changes from previous version

- Step 7, (4.14) and Result: "unchanged" now refers only to the leading-order ratios. The exact relation is $`\rho^{\max}(\sigma)=\rho^{\min}(-\sigma)`$, with every branch reversed; the part of an exact ratio that is odd in the couplings reverses sign (I1).
- Step 5 and Step 6, (4.13): the bound on the degree-$`\ge2`$ part of the cost difference now carries the factor $`n`$. It is compared with the leading cost differences, which gives the relative error $`\epsilon_C`$, $`\lvert\epsilon_C\rvert\le c_*\eta`$, uniform in $`n`$, $`L`$, $`D`$ and the places. The $`1+O(\eta)`$ of (4.13) is written out through $`\epsilon_C`$ (I2).
- Step 6: new (4.17), $`\rho_0=\beta_L\ell_0+\rho_L`$ at fixed places. The square-torus control is now an explicit family, $`\gamma_i\propto\ell_0(L)^{-5}`$, with $`\eta K\to0`$ and a stated source regime; along it the exact ratio diverges. The full-grip answer, the Controls and Result (4.12) and (4.17) are updated (I3).
- Code: paths moved to `code/v3/`. Added two checks: the exact mirrored ratios (4.14), and the fixed-place decomposition (4.17) on the square torus.

## Response to verification

- **I1:** Accepted and fixed in Step 7, (4.14), and in Result (4.14). The leading ratios $`\rho_0`$, $`\rho_0^{\rm mid}`$ and the factor $`\frac{1+n\gamma_i}{n\gamma_i}`$ are unchanged. Exactly, the highest-state ratio at branches σ equals the lowest-state ratio at branches $`-\sigma`$ (all body couplings reversed), for both couplings. The code now checks this equality for the exact ratios, as well as the reversal of the first correction.
- **I2:** Accepted and fixed in Step 5. The bound is $`c_*n\lvert g_A-g_B\rvert\eta`$. Divided by the leading differences $`n\lvert g_A-g_B\rvert`$ (full grip) and $`(1+n\gamma_i)\lvert g_A-g_B\rvert/\gamma_i`$ (coupling (a)), it gives the uniform relative $`O(\eta)`$, which (4.13) uses.
- **I3:** Accepted and fixed in Step 6, paragraph "Square torus at fixed places" with (4.17), and in the Controls. The family has $`\gamma_i(L)=\gamma_i^{(0)}\ell_0(L)^{-5}`$ and any $`\lvert g_s(L)\rvert\le t_f/(24\ell_0(L))`$. Along it η is in the regime, $`\eta K=O(1/\ell_0)\to0`$, and $`\rho_i^{\rm fg}=\beta\ell_0+O(1)`$ diverges where $`\beta\ne0`$. The failure of the leading coefficient at fixed couplings is stated separately.

## Setup and assumptions

- **Field (assumption, M8).** $`N_f\ge1`$ identical field objects ($`c=+1`$) without pair terms among them, on $`X_f`$: a ring ($`D=1`$), a square torus ($`D=2`$) or a cubic torus ($`D=3`$) of side $`L\ge3`$; $`\mathcal X:=\lvert X_f\rvert=L^D`$, $`n:=N_f/\mathcal X`$; own term $`C_1=-t_f\sum_{\{x,y\}}(\lvert x\rangle\langle y\rvert+\lvert y\rangle\langle x\rvert)`$, $`t_f>0`$; $`\Phi_x`$ the number of field objects at $`x`$. On one object $`C_1=t_f(\Lambda-2D)`$, $`\Lambda`$ the graph Laplacian. As in (4.4) of 06-ilang-source/04-profile,
```math
\ell(\mathbf x):=\Lambda^+(\mathbf x)=\frac1{\mathcal X}\sum_{\mathbf k\ne0}\frac{e^{i\mathbf k\cdot\mathbf x}}{\omega(\mathbf k)},\qquad \ell^{(2)}(\mathbf x):=(\Lambda^+)^2(\mathbf x)=\frac1{\mathcal X}\sum_{\mathbf k\ne0}\frac{e^{i\mathbf k\cdot\mathbf x}}{\omega(\mathbf k)^2},\qquad \omega(\mathbf k)=\sum_{\mu=1}^D4\sin^2\frac{k_\mu}2 ,
```
even functions of the displacement with $`\Lambda\ell=\delta_{\mathbf x,0}-\mathcal X^{-1}`$, $`\Lambda\ell^{(2)}=\ell`$, $`\sum_{\mathbf x}\ell=\sum_{\mathbf x}\ell^{(2)}=0`$; $`\ell_0:=\ell(0)`$.
- **Pair and source (assumption, M8, A15).** Two held Model D bodies ($`\tau=0`$) at $`x_1`$ and $`x_2=x_1+\mathbf r`$, on levels $`k_i`$ and branches $`\sigma_i`$ (half-gaps $`M^{(i)}_{k_i}`$), each coupled by coupling (a) or by the full grip with constant $`\gamma_i>0`$; no pair term between them; $`g_i:=\sigma_i\gamma_iM^{(i)}_{k_i}`$. One held source at $`x_s`$ with pair term $`g_s\Phi_{x_s}`$, first order in $`g_s`$. $`\mathbf R:=x_1-x_s`$, and $`d`$ is the length of the shortest representative of $`\mathbf R`$. Separations are those of field places; their relation to the distances of 03-ilang-space (M2) is not used.
- **State (assumption, M9, A11).** The eigenvector of the total contract connected, as the couplings go to zero, to the bodies in their internal states and every field object in the lowest one-object state. The mirrored highest state is treated in Step 7.
- **Regime (A13).** $`\eta:=\max(\lvert g_1\rvert,\lvert g_2\rvert)\,\ell_0/t_f<1/12`$ and $`\lvert g_s\rvert\ell_0/t_f<1/12`$. Step 2 shows that the expansion in the couplings converges there, with coefficient bounds that do not depend on $`L`$, $`D`$ or the places. First order in $`g_s`$. Here $`\ell_0=(L^2-1)/(12L)`$ (ring), $`\ell_0\simeq\frac1{2\pi}\ln L+0.049`$ (square torus, value from the code), $`\ell_0\to0.2527`$ (cubic torus).
- **Inputs** (quoted in question.md): (4.2) of 06-ilang-source/04-profile, $`E=N_f\varepsilon_0(g)`$ and the bond $`M`$ as a combination of four descriptions; (4.4) there, $`M^{(2)}=-\frac{2ng_1g_2}{t_f}\Lambda^+(x_1,x_2)`$ with $`\sum_{x_2}M^{(2)}=0`$; (4.8) there, the third-order bond; (7.1)–(7.3) of 06-ilang-source/07-dressed-fall, the one-object contract $`h_x`$, the weight as the place dependence of $`N_f\varepsilon_0`$, and its expansion on the ring.
- **Standard mathematics (M5).** Krein's formula for a finite-rank perturbation, the matrix determinant lemma, the contraction-mapping principle, Cauchy estimates for holomorphic functions of several variables, the Hellmann–Feynman theorem, Fourier analysis on tori, asymptotics of the lattice Green functions of $`\mathbb Z^2`$ and $`\mathbb Z^3`$.

## Derivation

### Step 1. Reduction to one field object

With $`\tau=0`$ the total contract commutes with the position label of each body, with $`\sigma_3`$ and with $`D`$. In the sector of given $`(x_i,k_i,\sigma_i)`$ it acts as $`c+\sum_{j=1}^{N_f}h^{(j)}`$, with $`h^{(j)}`$ acting on field object $`j`$ as
```math
h=C_1+g_1P_{x_1}+g_2P_{x_2}+g_sP_{x_s},\qquad c=\sigma_1M^{(1)}_{k_1}+\sigma_2M^{(2)}_{k_2}\ \text{(coupling (a))},\qquad c=0\ \text{(full grip)},
```
up to the place-independent own term of the source. By (4.2) of 06-ilang-source/04-profile the eigenvalue of the stated state is $`E=c+N_f\varepsilon_0(h)`$, with $`\varepsilon_0`$ the lowest eigenvalue of $`h`$. Every quantity below is a difference of eigenvalues of total contracts, so it is fixed by them (M6), and A5 replacements do not change it. $`E`$ depends on the bodies only through the set $`\{(x_1,g_1),(x_2,g_2)\}`$. For bodies of one type it is therefore the eigenvalue of the (anti)symmetrized admissible state, and it does not depend on labels (Law 5). The two couplings differ only by the constant $`c`$. They give the same bond profile and the same weights, and differ in the costs of levels (Step 5).

### Step 2. Exact finite-rank form, control, and the series

$`C_1`$ has the isolated lowest eigenvalue $`-2Dt_f`$, with eigenvector $`u=\mathcal X^{-1/2}\sum_x\lvert x\rangle`$; its next eigenvalue is $`-2Dt_f+t_f\omega_{\min}`$, $`\omega_{\min}=4\sin^2(\pi/L)`$. Take $`V=\sum_ag_aP_{x_a}`$ over the point terms present, $`a\in\{1,2,s\}`$, with $`g:=\mathrm{diag}(g_a)`$ and $`e:=(1,\dots,1)^T`$. For $`\lvert\delta\rvert<t_f\omega_{\min}`$, or real $`\delta<t_f\omega_{\min}`$, let
```math
R_{ab}(\delta):=\frac1{\mathcal X}\sum_{\mathbf k\ne0}\frac{e^{i\mathbf k\cdot(x_a-x_b)}}{t_f\omega(\mathbf k)-\delta},\qquad R_{ab}(0)=\frac{\ell_{ab}}{t_f},
```
the reduced resolvent of $`C_1`$ at $`-2Dt_f+\delta`$ between the points.

*Exact equation.* Put $`\varepsilon=-2Dt_f+\delta`$ with $`\delta\ne0`$. An eigenvector of $`h`$ satisfies $`\psi=-(C_1-\varepsilon)^{-1}V\psi`$. So $`\varepsilon`$ is an eigenvalue iff $`\det[1+G(\varepsilon)g]=0`$, with $`G_{ab}=\langle x_a\vert(C_1-\varepsilon)^{-1}\vert x_b\rangle=-1/(\mathcal X\delta)+R_{ab}(\delta)`$ (Krein's formula for a finite-rank perturbation). $`G`$ is $`R`$ plus a rank-one term. Where $`1+R(\delta)g`$ is invertible, the matrix determinant lemma turns the condition into
```math
\mathcal X\delta=e^{T}g\,[1+R(\delta)g]^{-1}e .\qquad\text{(4.15)}
```

*Control.* Let $`\rho:=t_f/(12\ell_0)`$ and let every $`\lvert g_a\rvert\le\rho`$, complex values allowed.
1. For $`\lvert\delta\rvert\le t_f\omega_{\min}/2`$ every term has $`\lvert t_f\omega-\delta\rvert\ge t_f\omega/2`$, so $`\lvert R_{ab}\rvert\le2\ell_0/t_f`$. The operator norm of the (at most $`3\times3`$) matrix $`R`$ is at most three times its largest entry, so $`\lVert Rg\rVert\le\frac12`$. The right side of (4.15) then has modulus at most $`\lvert e\rvert^2\rho/(1-\frac12)\le6\rho`$.
2. $`\mathcal X\ell_0=\sum_{\mathbf k\ne0}\omega^{-1}\ge2D/\omega_{\min}`$ (the $`2D`$ lowest modes). Hence $`6\rho/\mathcal X\le t_f\omega_{\min}/(4D)`$, and the map $`\delta\mapsto`$ (right side of (4.15))$`/\mathcal X`$ takes the disc $`\lvert\delta\rvert\le t_f\omega_{\min}/2`$ into itself.
3. Its derivative is $`-e^TTR'Te/\mathcal X`$, with $`T=g(1+Rg)^{-1}`$, $`\lVert T\rVert\le2\rho`$, and $`\lvert R'_{ab}\rvert\le4\ell^{(2)}_0/t_f^2\le4\ell_0/(t_f^2\omega_{\min})`$ (since $`\ell^{(2)}_0\le\ell_0/\omega_{\min}`$). Its modulus is therefore at most $`1/(\mathcal X\ell_0\omega_{\min})\le1/(2D)`$, and the map is a contraction.
4. By the contraction-mapping principle, (4.15) has exactly one root $`\delta(g)`$ in the disc. It is holomorphic in the $`g_a`$, as the uniform limit of holomorphic iterates, and $`\lvert\mathcal X\delta\rvert\le6\rho`$.
5. For real $`g_a`$, $`-2Dt_f+\delta(g)`$ is the lowest eigenvalue of $`h`$, and it is non-degenerate.
   - No eigenvalue lies below the disc: for real $`\delta<-t_f\omega_{\min}/2`$ the same bounds hold with $`\ell_0/t_f`$ in place of $`2\ell_0/t_f`$, which gives $`\lvert\delta\rvert\le4\rho/\mathcal X<t_f\omega_{\min}/2`$, a contradiction.
   - One eigenvalue lies in the disc, since $`\min\mathrm{spec}h\le\langle u\vert h\vert u\rangle=-2Dt_f+\sum_ag_a/\mathcal X`$.
   - The kernel of $`1+Gg`$, a rank-one change of the invertible $`1+Rg`$, is at most one-dimensional, and $`\psi\mapsto(\psi(x_a))_a`$ is injective on the eigenspace.
   - The case $`\delta=0`$ follows by continuity.

Cauchy's estimate on the polydisc $`\lvert g_a\rvert\le\rho`$ gives, for every monomial,
```math
\Bigl\lvert\bigl[g_1^{a}g_2^{b}g_s^{j}\bigr]\,\mathcal X\delta\Bigr\rvert\le6\,\rho^{\,1-a-b-j},\qquad\rho=\frac{t_f}{12\ell_0}.\qquad\text{(4.16)}
```
The bound does not depend on $`L`$, $`D`$ or the places. Hence the expansion of $`E=c+N_f(-2Dt_f+\delta)`$ in the couplings converges absolutely in the regime of the Setup.

*The series.* Insert $`R(\delta)=\Lambda^+/t_f+\delta(\Lambda^+)^2/t_f^2+O(\delta^2)`$ and the Neumann series of $`[1+Rg]^{-1}`$ into (4.15), and solve for δ by iteration, starting from $`\mathcal X\delta=\sum_ag_a+O(g^2)`$:
```math
\varepsilon_0=-2Dt_f+\frac{\sum_ag_a}{\mathcal X}-\frac{1}{t_f\mathcal X}\sum_{a,b}g_ag_b\,\ell_{ab}+\frac{1}{t_f^2\mathcal X}\Big[\sum_{a,b,c}g_ag_bg_c\,\ell_{ab}\ell_{bc}-\frac{\sum_cg_c}{\mathcal X}\sum_{a,b}g_ag_b\,\ell^{(2)}_{ab}\Big]+O(g^4),\qquad\text{(4.1)}
```
with $`\ell_{ab}:=\ell(x_a-x_b)`$ and $`\ell^{(2)}_{ab}:=\ell^{(2)}(x_a-x_b)`$. The $`g_1g_2`$ and $`g_1g_2(g_1+g_2)`$ terms of (4.1) are (4.4) and (4.8) of 06-ilang-source/04-profile. Its $`g_sg_b`$ and $`g_sg_b^2`$ terms are (7.3) of 06-ilang-source/07-dressed-fall (there $`\mathcal X=L`$).

*Remainders.* Sum (4.16) over the omitted monomials, for $`\eta\le1/24`$, so that each geometric sum is at most a fixed multiple of its first term. This gives additive bounds with numerical constants $`c_*`$ that do not depend on $`L`$, $`D`$ or the places. With $`\eta_i:=\lvert g_i\rvert\ell_0/t_f`$, the omitted part beyond degree $`m`$ in the body couplings is bounded as follows:
- for a term of $`E`$ that contains both $`g_1`$ and $`g_2`$ (a bond term), by $`c_*n\lvert g_1g_2\rvert(\ell_0/t_f)\,\eta^{m-1}`$;
- for the $`g_s`$-linear part of $`E`$ of a body alone, by $`c_*n\lvert g_s\rvert\eta_i^{m+1}`$; its difference between two internal states with couplings $`g_A,g_B`$ (η then also bounds $`\lvert g_A\rvert\ell_0/t_f`$ and $`\lvert g_B\rvert\ell_0/t_f`$), by $`c_*n\lvert g_s\rvert\lvert g_A-g_B\rvert(\ell_0/t_f)\,\eta^{m}`$ (mean value theorem in the one coupling);
- for a bond term of the $`g_s`$-linear part, by $`c_*n\lvert g_sg_1g_2\rvert(\ell_0/t_f)^2\eta^{m-1}`$.

A relative statement $`\bar Q\,(1+O(\eta^k))`$ below means the additive bound divided by the retained term $`\bar Q`$. Its constant depends on $`L`$ and the places through the quotient written at each result. It is not claimed where $`\bar Q`$ vanishes; there the additive bound holds.

### Step 3. The bond profile (item 1)

Without the source, through second order the only $`\mathbf r`$-dependent term of (4.1) is the $`g_1g_2`$ term. By translation invariance it does not depend on $`x_1`$:
```math
E(x_1,\mathbf r)-E(x_1,\mathbf r')=B(\mathbf r)-B(\mathbf r')+O\Big(n\lvert g_1g_2\rvert\frac{\ell_0}{t_f}\,\eta\Big),\qquad B(\mathbf r):=-\frac{2ng_1g_2}{t_f}\,\ell(\mathbf r).\qquad\text{(4.2)}
```
The remainder is the bond-term bound of Step 2 with $`m=2`$. Its leading part is the third-order bond, (4.8) of 06-ilang-source/04-profile, and $`B`$ is $`M^{(2)}`$ of (4.4) there.
- *Relative form:* $`[B(\mathbf r)-B(\mathbf r')](1+\epsilon_B)`$ with $`\epsilon_B=O(\eta\,\ell_0/\lvert\ell(\mathbf r)-\ell(\mathbf r')\rvert)`$, so $`\epsilon_B=O(\eta)`$ where $`\lvert\ell(\mathbf r)-\ell(\mathbf r')\rvert`$ is of order $`\ell_0`$.
- The code finds $`\lvert\epsilon_B\rvert`$ between $`1.5\cdot10^{-3}`$ and $`0.11`$, linear in η and not growing with $`\lvert\mathbf r\rvert`$. On the ring it depends only on $`r/L`$; on the tori it changes by at most about 20% between the two sizes (Code). This includes unit steps on rings with $`L=256`$, where the quotient above is about $`40\eta`$.
- *Fixed by the total contract:* $`E`$ itself, including its $`\mathbf r`$-independent part, since it is an eigenvalue of $`C`$ and A5 replacements leave it unchanged. Hence also the whole profile (4.2). The profile is the same for both couplings and every A5 split, and at second order it contains the couplings only through $`g_1g_2`$.
- *Not fixed by the profile alone:* its additive normalization, the zero of $`B`$. The normalization $`\sum_{\mathbf r}B=0`$ refers to the four descriptions of (4.2) of 06-ilang-source/04-profile.
- *A convention, not fixed by $`C`$:* the allocation of $`E`$ into rest costs, own marks ($`-ng_i^2\ell_0/t_f`$), bond and individual contracts (A5).

*Ring.* Let $`r`$ be the label difference mod $`L`$. The quadratic below has second difference $`1/L`$ for $`0<r<L`$, a kink of $`1`$ at $`r=0`$ and zero sum, so it is the zero-mean solution of $`\Lambda\ell=\delta-1/L`$, that is $`\Lambda^+`$:
```math
\ell(r)=\frac{L^2-1}{12L}-\frac{r(L-r)}{2L},\qquad E(r)-E(r')=\frac{ng_1g_2}{t_fL}\big[r(L-r)-r'(L-r')\big]+O\Big(n\lvert g_1g_2\rvert\frac{\ell_0}{t_f}\,\eta\Big).\qquad\text{(4.3)}
```

*Tori.* As $`L\to\infty`$ at fixed $`\mathbf r`$, $`\ell(0)-\ell(\mathbf r)`$ tends to the potential kernel of $`\mathbb Z^D`$. Its standard asymptotics, plus the smooth background forced by $`\Lambda\ell=-\mathcal X^{-1}`$ away from $`0`$, give
```math
\ell(0)-\ell(\mathbf r)=\begin{cases}\dfrac{\ln\lvert\mathbf r\rvert}{2\pi}+\dfrac{2\gamma_E+3\ln2}{4\pi}+O(\lvert\mathbf r\rvert^{-2})-\dfrac{\lvert\mathbf r\rvert^2}{4L^2}, & D=2,\\[2mm] G_0-\dfrac1{4\pi\lvert\mathbf r\rvert}+O(\lvert\mathbf r\rvert^{-3})-\dfrac{\lvert\mathbf r\rvert^2}{6L^3},\quad G_0=\Lambda^{-1}_{\mathbb Z^3}(0)=0.2527310, & D=3,\end{cases}\qquad\text{(4.4)}
```
up to higher terms in $`\lvert\mathbf r\rvert/L`$ (code: deviations scale as $`\lvert\mathbf r\rvert^{-2}`$, $`\lvert\mathbf r\rvert^{-3}`$ and as the stated background). For $`1\ll\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll L`$, therefore, $`E(\mathbf r)-E(\mathbf r')\simeq\frac{ng_1g_2}{\pi t_f}\ln\frac{\lvert\mathbf r\rvert}{\lvert\mathbf r'\rvert}`$ ($`D=2`$) and $`\simeq-\frac{ng_1g_2}{2\pi t_f}\big(\frac1{\lvert\mathbf r\rvert}-\frac1{\lvert\mathbf r'\rvert}\big)`$ ($`D=3`$). For $`g_1g_2>0`$ (equal branches) $`E`$ grows with the separation: on the ring with the graph distance, on the tori for $`1\ll\lvert\mathbf r\rvert\ll L`$. For $`g_1g_2<0`$ it falls.

### Step 4. Weight of a body and of the pair (item 2)

The weight at first order in $`g_s`$ is the $`g_s`$-linear part of $`E`$ as a function of the place, as in (7.2) of 06-ilang-source/07-dressed-fall, up to a place-independent constant. Collect the $`g_s`$-linear terms of (4.1) and put $`\phi(x):=-\frac{2g_s}{t_f}\ell(x-x_s)`$. A body alone then has
```math
W_i(x)=ng_i\,\phi(x)+\frac{ng_sg_i^2}{t_f^2}\Big[2\ell_0\,\ell(x-x_s)+\ell(x-x_s)^2-\frac2{\mathcal X}\,\ell^{(2)}(x-x_s)\Big]+O\big(n\lvert g_s\rvert\eta_i^3\big),\qquad\text{(4.5)}
```
which is (7.3) of 06-ilang-source/07-dressed-fall, now on all three graphs. The remainder is the single-body bound of Step 2 with $`m=2`$. Relative to a place difference of the leading term it is $`O(\eta_i^2\,\ell_0/\lvert\Delta\ell\rvert)`$, where $`\Delta\ell`$ is the place difference of $`\ell(\cdot-x_s)`$. The code finds a relative deviation proportional to $`\eta_i^2`$, at most $`7.8\cdot10^{-3}`$ (Code):
- on the tori it does not grow with $`d`$, and between the two sizes it changes by at most 15% (cubic) and 50% (square);
- on the ring it depends on $`d/L`$, to within 15%.

For the pair, $`W_{\rm pair}(x_1;\mathbf r)=W_1(x_1)+W_2(x_1+\mathbf r)+W_b(x_1;\mathbf r)`$ with
```math
W_b=\frac{2ng_sg_1g_2}{t_f^2}\,S+O\Big(n\lvert g_sg_1g_2\rvert\frac{\ell_0^2}{t_f^2}\,\eta\Big),\qquad S:=\ell(\mathbf r)\big(\ell_{1s}+\ell_{2s}\big)+\ell_{1s}\ell_{2s}-\frac{\ell^{(2)}_{1s}+\ell^{(2)}_{2s}}{\mathcal X},\qquad\text{(4.6)}
```
up to the place-independent $`-\frac{2ng_sg_1g_2}{t_f^2\mathcal X}\ell^{(2)}(\mathbf r)`$. The remainder is the bond-term bound of Step 2 with $`m=2`$; relative to a difference $`\Delta S`$ it is $`O(\eta\,\ell_0^2/\lvert\Delta S\rvert)`$. $`W_b`$ collects the $`g_sg_1g_2`$ terms of (4.1). The orderings with $`s`$ at an end of $`\ell_{ab}\ell_{bc}`$ give $`2\ell(\mathbf r)(\ell_{1s}+\ell_{2s})`$, those with $`s`$ in the middle give $`2\ell_{1s}\ell_{2s}`$, and the $`1/\mathcal X`$ terms give the rest. It is the $`g_s`$-linear, place-dependent part of $`E(g_1,g_2)-E(g_1,0)-E(0,g_2)+E(0,0)`$ with the source present. This is the bond of (4.2) of 06-ilang-source/04-profile weighed in the field of the source, and it is fixed by the four total contracts as that bond is. With $`\phi(x_a)=-\frac{2g_s}{t_f}\ell_{as}`$,
```math
W_b(x_1;\mathbf r)=\tfrac12B(\mathbf r)\big[\phi(x_1)+\phi(x_2)\big]+\frac{ng_1g_2}{2g_s}\,\phi(x_1)\phi(x_2)-\frac{2ng_sg_1g_2}{t_f^2\mathcal X}\big[\ell^{(2)}_{1s}+\ell^{(2)}_{2s}\big].\qquad\text{(4.7)}
```
By (4.5) the first-order cost $`ng_i`$ of a body is weighed by $`\phi`$ at its place. By (4.7) the bond is weighed by the same $`\phi`$, half at the place of each body. The second term of (4.7) is the change of the propagation between the bodies caused by the source ($`\ell_{12}\to\ell_{12}-\frac{g_s}{t_f}\ell_{1s}\ell_{s2}`$, the first-order change of the reduced resolvent), and the third is the normalization of the lowest state.

*Distance large against $`\lvert\mathbf r\rvert`$.* Let $`\mathcal C_{\rm p}(\mathbf r):=n(g_1+g_2)-\frac n{t_f}\big[(g_1^2+g_2^2)\ell_0+2g_1g_2\ell(\mathbf r)\big]`$ be the coupling-made cost of the pair through second order ((4.1) without source). Rearranging (4.5)–(4.7) exactly gives
```math
W_{\rm pair}=\mathcal C_{\rm p}(\mathbf r)\,\phi(x_1)+\frac{ng_s(g_1+g_2)^2}{t_f^2}\Big[\ell(\mathbf R)^2-\frac{2\ell^{(2)}(\mathbf R)}{\mathcal X}\Big]+\big[W_2(x_2)-W_2(x_1)\big]+\frac{2ng_sg_1g_2}{t_f^2}\,\delta S,\qquad \delta S:=\big(\ell(\mathbf r)+\ell_{1s}\big)\big(\ell_{2s}-\ell_{1s}\big)-\frac{\ell^{(2)}_{2s}-\ell^{(2)}_{1s}}{\mathcal X}.\qquad\text{(4.8)}
```
The last two terms are of first order in $`\mathbf r\cdot\nabla\ell(\mathbf R)`$. For $`\lvert\mathbf r\rvert\ll d`$ the pair is therefore weighed like one body of coupling $`g_1+g_2`$, except that its cost $`\mathcal C_{\rm p}`$ contains the bond $`B`$, and this cost is weighed by $`\phi`$ as a whole. On the ring $`\phi`$ is the quadratic (4.3). For $`1\ll d\ll L`$, by (4.4), $`\phi(x)=\text{const}+\frac{g_s}{\pi t_f}\ln d`$ ($`D=2`$) and $`\phi(x)=\text{const}-\frac{g_s}{2\pi t_fd}`$ ($`D=3`$).

### Step 5. How the weight of a single body follows its cost

Compare two internal states $`(k,\sigma)\ne(k',\sigma')`$ of body $`i`$ alone, with couplings $`g_A=\sigma\gamma_iM_k`$ and $`g_B=\sigma'\gamma_iM_{k'}`$, so $`g_A\ne g_B`$. The cost of a body alone does not depend on its place. By (4.1) without the source, its coupling-made part is $`N_f\delta(g)=n\mathcal X\delta(g)=ng+f(g)`$, where $`f(g)=n\sum_{a\ge2}c_ag^a`$ is the degree-$`\ge2`$ part of $`n\mathcal X\delta`$. By (4.16) with one coupling, $`\lvert c_a\rvert\le6\rho^{1-a}`$. For $`g`$ between $`g_B`$ and $`g_A`$, $`q:=\lvert g\rvert/\rho\le12\eta\le\frac12`$ (η bounds $`\lvert g_A\rvert\ell_0/t_f`$ and $`\lvert g_B\rvert\ell_0/t_f`$, Step 2, and $`\eta\le1/24`$). This gives $`\lvert f'(g)\rvert\le6n\sum_{a\ge2}aq^{a-1}\le36nq\le c_*n\eta`$ ($`c_*=432`$). By the mean value theorem on the segment from $`g_B`$ to $`g_A`$, $`\lvert f(g_A)-f(g_B)\rvert\le c_*n\lvert g_A-g_B\rvert\eta`$. Therefore
```math
\Delta\mathcal C_i^{\rm fg}=n(g_A-g_B)(1+\epsilon_C),\qquad \Delta\mathcal C_i^{(a)}=\frac{g_A-g_B}{\gamma_i}+\Delta\mathcal C_i^{\rm fg}=(1+n\gamma_i)(\sigma M_k-\sigma'M_{k'})\Big(1+\frac{n\gamma_i\,\epsilon_C}{1+n\gamma_i}\Big),\qquad\lvert\epsilon_C\rvert\le c_*\eta .
```
The leading differences are $`n\lvert g_A-g_B\rvert`$ and $`(1+n\gamma_i)\lvert g_A-g_B\rvert/\gamma_i`$. Relative to them the errors are at most $`c_*\eta`$ and $`c_*\eta\,n\gamma_i/(1+n\gamma_i)\le c_*\eta`$, uniformly in $`n`$, $`\gamma_i`$, $`L`$, $`D`$ and the places. By (4.5) their weight difference is $`n\gamma_i(\sigma M_k-\sigma'M_{k'})\,\phi`$ in both couplings, plus the $`g_A^2-g_B^2`$ term of (4.5) and the level-difference remainder of Step 2. Hence
```math
\Delta W_i(x)-\Delta W_i(x')=\Delta\mathcal C_i\,\big[F_i(x)-F_i(x')\big]\big(1+\epsilon_F\big),\qquad F_i=\phi\ \ \text{(full grip)},\qquad F_i=\frac{n\gamma_i}{1+n\gamma_i}\,\phi\ \ \text{(coupling (a))},\qquad\text{(4.9)}
```
with $`\epsilon_F=O\big(\eta\,(1+\lvert\Delta\ell^{(2)}\rvert/(\mathcal X\ell_0\lvert\Delta\ell\rvert))+\eta^2\ell_0/\lvert\Delta\ell\rvert\big)`$, where Δ is the place difference $`x\to x'`$ of $`\ell(\cdot-x_s)`$ and $`\ell^{(2)}(\cdot-x_s)`$. The first term contains $`\epsilon_C`$ and the $`g_A^2-g_B^2`$ term of (4.5) relative to the leading one, using $`\lvert\Delta(2\ell_0\ell+\ell^2)\rvert\le4\ell_0\lvert\Delta\ell\rvert`$. The second is the remainder.
For the full grip $`F`$ is the same for every level, branch and body. For coupling (a) it depends on the body through $`n\gamma_i`$, because the rest term of the body's own contract is not weighed at this order.

### Step 6. Is the bond weighed? (item 3)

Let $`\Delta_{\mathbf e}f(y):=f(y+\mathbf e)-f(y)`$ for a unit step $`\mathbf e`$ of the pair as a whole, and $`\Delta_{\mathbf r\mathbf r'}f:=f(\mathbf r)-f(\mathbf r')`$. Beyond the weights of the bodies at their own places, the part of the weight of the pair that depends on $`\mathbf r`$ is $`W_b`$. Its profile is compared with the bond profile (4.2) times the function (4.9). In $`\rho_i`$ all three factors are the exact ones: $`W_b`$ is the $`g_s`$-linear, place-dependent part of $`E(g_1,g_2)-E(g_1,0)-E(0,g_2)+E(0,0)`$, $`\Delta_{\mathbf r\mathbf r'}B`$ stands for the exact profile, and $`\Delta_{\mathbf e}F_i`$ for the exact quotient of (4.9).
```math
\rho_i:=\frac{\Delta_{\mathbf e}\Delta_{\mathbf r\mathbf r'}W_b(x_1;\cdot)}{\Delta_{\mathbf r\mathbf r'}B\;\Delta_{\mathbf e}F_i(x_1)},\qquad \rho_i^{\rm fg}=\rho_0+O(\eta K),\qquad \rho_0=\frac{\Delta_{\mathbf e}\Delta_{\mathbf r\mathbf r'}S}{2\,\Delta_{\mathbf r\mathbf r'}\ell\;\Delta_{\mathbf e}\ell(\mathbf R)}=1+\kappa,\qquad \kappa=\frac{\Delta_{\mathbf e}\Delta_{\mathbf r\mathbf r'}\delta S}{2\,\Delta_{\mathbf r\mathbf r'}\ell\;\Delta_{\mathbf e}\ell(\mathbf R)} .\qquad\text{(4.10)}
```
This holds for $`\ell(\mathbf r)\ne\ell(\mathbf r')`$, $`\Delta_{\mathbf e}\ell(\mathbf R)\ne0`$ and $`\eta K\ll1`$; "fg" means full grip. Here
```math
K:=\frac{(1+\lvert\rho_0\rvert)\,\ell_0^2}{\lvert\Delta_{\mathbf r\mathbf r'}\ell\;\Delta_{\mathbf e}\ell(\mathbf R)\rvert}+\frac{\lvert\rho_0\rvert\,\lvert\Delta_{\mathbf e}\ell^{(2)}(\mathbf R)\rvert}{\mathcal X\ell_0\,\lvert\Delta_{\mathbf e}\ell(\mathbf R)\rvert}.
```
- The leading terms of numerator and denominator are those of (4.6), (4.2) and (4.9), and their quotient is $`\rho_0`$.
- The remainder of the numerator, divided by the leading denominator $`4n\lvert g_sg_1g_2\,\Delta_{\mathbf r\mathbf r'}\ell\,\Delta_{\mathbf e}\ell(\mathbf R)\rvert/t_f^2`$, is $`O(\eta\ell_0^2/\lvert\Delta_{\mathbf r\mathbf r'}\ell\,\Delta_{\mathbf e}\ell(\mathbf R)\rvert)`$.
- The relative remainders $`\epsilon_B`$ and $`\epsilon_F`$ of the denominator enter multiplied by $`\rho_0`$. They are bounded by the same quotient, since $`\lvert\Delta\ell\rvert\le2\ell_0`$, plus the $`\ell^{(2)}`$ term of $`\epsilon_F`$.
- The statement is additive in ρ, so it also holds where $`\rho_0=0`$.
- $`K`$ is an upper bound from (4.16). It grows like $`d^2`$ on the cubic torus and like $`L^2`$ on the ring at fixed $`u,v`$ (below).
- The code finds $`\lvert\rho_i^{\rm fg}-\rho_0\rvert`$ linear in η, with $`\lvert\rho_i^{\rm fg}-\rho_0\rvert/\eta`$ between $`0.001`$ and $`2.4`$, while $`K`$ ranges from $`2\cdot10^{2}`$ to $`1.6\cdot10^{4}`$ over the same entries (Code).
  - On the tori this value is largest at the smallest $`d`$ tested. On the square torus it grows with $`L`$ at small $`d`$, as κ does.
  - On the ring, from $`L=64`$ to $`256`$ at fixed $`u`$, it changes by a factor between 0.3 and 2.8, while $`K`$ grows by a factor of 16.

The value $`1`$ comes from $`S-\delta S=2\ell(\mathbf r)\ell_{1s}+(\text{terms without }\mathbf r)`$. The configurations used, $`\{x_1,x_1+\mathbf r\}`$ and $`\{x_1,x_1+\mathbf r'\}`$ and their translates, share the body at $`x_1`$, so $`\rho_i`$ does not depend on labels. Neither $`\rho_0`$ nor $`\kappa`$ contains a coupling. At leading order in η the ratio is therefore exactly the same for every level, branch, $`\gamma_i`$, $`N_f`$, $`t_f`$ and sign of $`g_s`$, and for both signs of the bond ($`g_1g_2<0`$ reverses $`W_b`$ and $`B`$ together). The class contains no control at this order. At order η the exact ratio depends on levels and bodies (code).

*Expansion in $`\lvert\mathbf r\rvert/d`$.* For $`d\gg1`$, expand $`\ell_{2s}=\ell(\mathbf R+\mathbf r)`$ in δS by Taylor's theorem, with $`\partial_{\mathbf e}:=\mathbf e\cdot\nabla`$:
```math
\kappa=\frac{\big[(\ell(\mathbf r)+\ell(\mathbf R))\,\mathbf r-(\ell(\mathbf r')+\ell(\mathbf R))\,\mathbf r'\big]\cdot\nabla\partial_{\mathbf e}\ell+(\mathbf r-\mathbf r')\cdot\nabla\ell\;\partial_{\mathbf e}\ell-\mathcal X^{-1}(\mathbf r-\mathbf r')\cdot\nabla\partial_{\mathbf e}\ell^{(2)}}{2\,[\ell(\mathbf r)-\ell(\mathbf r')]\,\partial_{\mathbf e}\ell}\bigg\rvert_{\mathbf R}+\big(\text{second order in }\mathbf r/d,\ \mathbf r'/d\big).\qquad\text{(4.11)}
```
The sizes below assume $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d\ll L`$, $`\lvert\mathbf r'\rvert/\lvert\mathbf r\rvert`$ of order 2, and a place where $`\partial_{\mathbf e}\ell(\mathbf R)`$ is not anomalously small. Using (4.4):
- $`D=3`$: $`\kappa=O(\lvert\mathbf r'\rvert/d)`$. The code finds $`d\kappa\approx1.0`$ and $`2.0`$ for non-collinear $`\mathbf r,\mathbf r'`$, and smaller values for collinear ones.
- $`D=2`$: here $`\ell(\mathbf r)+\ell(\mathbf R)\simeq\frac1{2\pi}\ln\frac{L^2}{\lvert\mathbf r\rvert d}`$, so $`\kappa=O\big(\frac{\lvert\mathbf r-\mathbf r'\rvert}{d}\ln\frac{L^2}{\lvert\mathbf r\rvert d}\big)`$, which grows like $`\ln L`$ at fixed places. The code finds $`d\kappa\approx3.1,\,5.7,\,8.6`$ for $`L=128,512,2048`$.

The first-order κ consists only of relocations. When $`\mathbf r`$ changes at fixed $`x_1`$, the midpoint at which the absolute bond $`B`$ is weighed (4.7) moves by $`(\mathbf r-\mathbf r')/2`$. The $`\mathbf r`$-independent $`g_1g_2`$ terms of (4.7) taken at the midpoint, $`\frac{ng_1g_2}{2g_s}\phi^2`$ and the normalization term, move with it. Expanding these displacements reproduces (4.11) term by term.

*Midpoint as the place.* Take $`\bar x:=x_1+\mathbf r/2`$ as the place, with $`\mathbf r,\mathbf r'`$ having even components, change $`\mathbf r`$ at fixed $`\bar x`$, and define $`\rho^{\rm mid}_i`$ as in (4.10) with $`x_1\to\bar x`$. $`S`$ is symmetric in the two bodies, so expanded about $`\bar x`$ it contains only even powers of $`\mathbf r`$, and $`\rho^{\rm mid}_0=1+\kappa^{\rm mid}`$ has no first-order term. On the ring, put $`d_{1,2}=\bar d\mp r/2`$. Besides the main term $`2\ell(r)\ell(\bar d)`$, the only terms of $`S`$ that depend on both $`r`$ and $`\bar d`$ are $`\frac{r^2}{4L}\big[2\ell(\bar d)-L\ell'(\bar d)^2\big]`$, using $`\ell''=1/L`$ and $`\ell^{(2)\prime\prime}=-\ell+\text{const}`$ from $`\Lambda\ell^{(2)}=\ell`$. For the quadratic (4.3), $`2\ell-L\ell'^2=\frac{L^2-1}{6L}-\frac L4`$ is constant. For the same steps, evaluating (4.10) with (4.3) gives the ring value of $`\rho_0`$. Altogether:
```math
\kappa^{\rm mid}_{D=3}=O\Big(\frac{\lvert\mathbf r\rvert\lvert\mathbf r'\rvert}{d^2}\Big),\qquad \kappa^{\rm mid}_{D=2}=O\Big(\frac{\lvert\mathbf r'\rvert^2}{d^2}\ln\frac{L^2}{\lvert\mathbf r'\rvert d}\Big),\qquad \kappa^{\rm mid}_{\rm ring}=0,\qquad \rho_0^{\rm ring}=\frac{2(1-w)(1-2w)}{(1-2u)(1-2v)}.\qquad\text{(4.12)}
```
- On the ring, $`d_1<d_2=d_1+r`$ are the arc lengths from $`x_s`$ to the bodies, taken in the sense in which the arc from $`x_1`$ to $`x_2`$ does not contain $`x_s`$. The unit step $`\mathbf e`$ and $`r'=r-1`$ are taken in that sense.
- In (4.12), exactly on the lattice, $`u=(d_1+\frac12)/L`$, $`v=(r-\frac12)/L`$ and $`w=u+v=(d_1+r)/L`$. With $`u=d_1/L`$, $`v=r/L`$ the same expression is only the large-$`L`$ limit: at $`L=30`$, $`d_1=6`$, $`r=3`$ it gives $`1.16667`$, against the lattice value $`1.18588`$.
- Both ring statements hold for $`x_s`$ outside that arc. $`\rho_0^{\rm ring}`$ vanishes at $`w=\frac12`$ (even $`L`$, $`d_1+r=L/2`$); there (4.10) holds in its additive form.
- The code confirms both ring statements on the lattice to rounding error ($`L=40`$–$`320`$). On the tori it finds $`d^2\kappa^{\rm mid}\approx-2`$ to $`-3`$ ($`D=3`$) and $`\approx-15,-30,-47`$ ($`D=2`$, $`L=128,512,2048`$).
- For $`v\to0`$, $`\rho_0^{\rm ring}\to2(1-u)\in(0,2)`$.

*Place convention.* The question fixes the place of the pair as $`x_1`$ at fixed $`\mathbf r`$, and (4.10)–(4.11) refer to it. The midpoint $`\bar x`$ is the natural place: it treats the two bodies alike, so it does not depend on which body carries the label 1, and it has no first-order relocation. The answers below give both. They are statements about $`\rho_0`$ and $`\rho^{\rm mid}_0`$; by (4.10) the exact ratios differ from these by $`O(\eta K)`$, and the code finds them within $`2.4\,\eta`$ in all tested configurations.

*Answer for the full grip.* The bond is weighed like the costs of the bodies, by the same function $`\phi`$ placed at the midpoint of the pair:
- On the ring this is exact at leading order in η ($`\rho^{\rm mid}_0=1`$). Referred to $`x_1`$, the question's place, the ratio is $`\rho_0^{\rm ring}\neq1`$ at generic places, entirely through the relocation.
- On the cubic torus, $`\rho_0=1+O(\lvert\mathbf r'\rvert/d)`$ and $`\rho_0^{\rm mid}=1+O(\lvert\mathbf r\rvert\lvert\mathbf r'\rvert/d^2)`$.
- On the square torus the same holds only for $`d`$ large against $`\lvert\mathbf r-\mathbf r'\rvert\ln(L^2/(\lvert\mathbf r\rvert d))`$, respectively against $`\lvert\mathbf r'\rvert\ln^{1/2}(L^2/(\lvert\mathbf r'\rvert d))`$. At fixed generic places it fails as $`L\to\infty`$: by (4.17) the leading ratios grow like $`\ell_0\simeq\frac1{2\pi}\ln L`$, and the exact ratios follow them along couplings that shrink with $`L`$.

*Square torus at fixed places, $`L\to\infty`$.* Fix $`x_s`$, $`x_1`$ (or $`\bar x`$), $`\mathbf r`$, $`\mathbf r'`$, $`\mathbf e`$, the levels and the branches. Write $`\ell=\ell_0-a_L`$, so that $`a_L(0)=0`$ and $`a_L\to a`$, the potential kernel of $`\mathbb Z^2`$ (4.4). With $`a_{is}:=a_L(x_i-x_s)`$,
```math
S=3\ell_0^2-2\ell_0\big[a_L(\mathbf r)+a_{1s}+a_{2s}\big]+a_L(\mathbf r)(a_{1s}+a_{2s})+a_{1s}a_{2s}-(\ell^{(2)}_{1s}+\ell^{(2)}_{2s})/\mathcal X .
```
- Under $`\Delta_{\mathbf e}\Delta_{\mathbf r\mathbf r'}`$ the term $`3\ell_0^2`$ and $`a_L(\mathbf r)`$ in the second term drop out. The denominator $`2\Delta_{\mathbf r\mathbf r'}\ell\,\Delta_{\mathbf e}\ell(\mathbf R)`$ of $`\rho_0`$ is a product of differences of $`a_L`$.
- From $`\lvert\cos\mathbf k\cdot(\mathbf x+\mathbf e)-\cos\mathbf k\cdot\mathbf x\rvert\le\frac12\lvert\mathbf k\rvert^2\lvert2\mathbf x+\mathbf e\rvert`$ and $`\lvert\mathbf k\rvert^2\le\frac{\pi^2}4\omega(\mathbf k)`$ on $`(-\pi,\pi]^D`$: $`\lvert\Delta_{\mathbf e}\ell^{(2)}(\mathbf x)\rvert\le\frac{\pi^2}8(2\lvert\mathbf x\rvert+1)\ell_0`$, with $`\mathbf x`$ the shortest representative. So the $`\ell^{(2)}`$ term contributes $`O(\ell_0(d+\lvert\mathbf r\rvert+\lvert\mathbf r'\rvert)/\mathcal X)\to0`$.

Hence, for $`x_1`$ and in the same way for $`\bar x`$ (with $`\bar{\mathbf R}:=\bar x-x_s`$ in the denominator),
```math
\rho_0=\beta_L\,\ell_0+\rho_L,\qquad \beta_L=\frac{\Delta_{\mathbf e}\Delta_{\mathbf r\mathbf r'}\big[\ell_{1s}+\ell_{2s}\big]}{\Delta_{\mathbf r\mathbf r'}\ell\;\Delta_{\mathbf e}\ell(\mathbf R)},\qquad\text{(4.17)}
```
where $`\beta_L`$ and $`\rho_L`$ are built from differences of $`a_L`$, plus, in $`\rho_L`$, the $`\ell^{(2)}`$ term, which tends to zero. Both converge as $`L\to\infty`$ to their $`\mathbb Z^2`$ values ($`a`$ in place of $`a_L`$, no $`\ell^{(2)}`$ term).
- The code finds, for $`L=128,512,2048`$ (`code/v3/output/check_weight_of_bond.txt`, section (4.17)):
  - at $`x_1=x_s+(8,0)`$ with $`\mathbf r=(2,1)`$, $`\mathbf r'=(4,3)`$: $`\beta_L=1.303,\,1.259,\,1.257`$ and $`\rho_L=0.296,\,0.325,\,0.326`$;
  - at the midpoint $`\bar x=x_s+(8,0)`$ with $`\mathbf r=(2,2)`$, $`\mathbf r'=(4,2)`$: $`\beta_L=-1.164,\,-1.146,\,-1.145`$ and $`\rho_L=1.682,\,1.673,\,1.673`$.
- At these places the values show $`\beta:=\lim\beta_L\ne0`$ (numerically, not derived for general places). So $`\rho_0\to+\infty`$ (place $`x_1`$) and $`\rho^{\rm mid}_0\to-\infty`$ (midpoint), like $`\beta\ell_0`$.
- There $`K\asymp\ell_0^3`$. Its first term is $`(1+\lvert\rho_0\rvert)\ell_0^2/\lvert\Delta_{\mathbf r\mathbf r'}\ell\,\Delta_{\mathbf e}\ell(\mathbf R)\rvert`$ with a convergent denominator. By the bound above, its second term is at most $`\lvert\rho_0\rvert\pi^2(2d+1)/(8\mathcal X\lvert\Delta_{\mathbf e}\ell(\mathbf R)\rvert)\to0`$. The code finds $`K/\ell_0^3=1224,\,1059,\,964`$, decreasing towards its limit.

*Control family.* Take $`\gamma_i(L)=\gamma_i^{(0)}\ell_0(L)^{-5}`$ at fixed levels, branches and places, and any source with $`\lvert g_s(L)\rvert\le t_f/(24\ell_0(L))`$.
- The ratios do not depend on $`g_s`$, which cancels between $`W_b`$ and $`\Delta_{\mathbf e}F_i`$. The source bound only keeps each member in the regime of the Setup.
- Then $`\eta=O(\ell_0^{-4})`$ lies in the regime for large $`L`$, and $`\eta K=O(\ell_0^{-1})\to0`$. By (4.10), $`\rho_i^{\rm fg}=\beta_L\ell_0+\rho_L+O(\eta K)`$ diverges, and likewise $`\rho_i^{\rm mid,fg}`$.
- At fixed couplings, instead, η grows like $`\ln L`$ and leaves the regime. There only the failure of the leading coefficient is established.

*Coupling (a).* The two couplings differ only by the constant $`c`$, so $`W_b`$, the profile and the weight differences are the same. The exact ratio of the two ratios is therefore $`\Delta\mathcal C_i^{(a)}/\Delta\mathcal C_i^{\rm fg}`$, and by Step 5
```math
\rho_i^{(a)}=\frac{1+n\gamma_i}{n\gamma_i}\,\rho_i^{\rm fg}\,\big(1+O(\eta)\big),\qquad \rho_i^{{\rm mid},(a)}=\frac{1+n\gamma_i}{n\gamma_i}\,\rho_i^{\rm mid,fg}\,\big(1+O(\eta)\big).\qquad\text{(4.13)}
```
Explicitly, with the two cost differences of Step 5, $`\Delta\mathcal C_i^{(a)}/\Delta\mathcal C_i^{\rm fg}=\frac{1+n\gamma_i}{n\gamma_i}\Big(1-\frac{\epsilon_C}{(1+n\gamma_i)(1+\epsilon_C)}\Big)`$ with $`\lvert\epsilon_C\rvert\le c_*\eta`$. So the $`O(\eta)`$ is uniform in $`n`$, $`\gamma_i`$, $`L`$, $`D`$ and the places.
Wherever the full-grip ratio is near 1, this ratio is near $`(1+n\gamma_i)/(n\gamma_i)>1`$, on every graph. The bond, which is made entirely through the field, is weighed per unit cost $`(1+n\gamma_i)/(n\gamma_i)`$ times as strongly as the level costs of body $`i`$. For unequal $`\gamma_1\ne\gamma_2`$ the two bodies' functions also differ. The ratio approaches the full-grip value only for $`n\gamma_i\to\infty`$.

*Controls (M9).*
- For "yes" (full grip), three controls:
  - coupling (a) of the same class, by (4.13);
  - the square torus at fixed generic places along the control family of (4.17), where the exact ratio diverges;
  - the ring referred to $`x_1`$, by (4.12), at fixed $`L`$ with couplings so small that the $`O(\eta K)`$ of (4.10) is below $`\lvert\rho_0^{\rm ring}-1\rvert`$.
- For "no" (coupling (a)): the full grip on the cubic torus.
- For the independence of levels and branches: none in the class at leading order in η; at order η the code shows a dependence.

### Step 7. The mirrored highest state

For even $`L`$ the graphs are bipartite. The sublattice sign $`U`$ is diagonal in places with $`U^2=1`$, $`UC_1U=-C_1`$ and $`UP_xU=P_x`$, so $`\max\mathrm{spec}(C_1+V)=-\min\mathrm{spec}(C_1-V)`$, and the highest state has $`E^{\max}(g)=c-N_f\varepsilon_0(-g)`$, $`g=(g_1,g_2,g_s)`$. The body couplings $`g_i=\sigma_i\gamma_iM^{(i)}_{k_i}`$ and the constant $`c`$ are odd in the branches. Reverse every branch, $`\sigma\to-\sigma`$, including that of the second internal state used in $`F_i`$. This gives, for both couplings,
```math
E^{\max}(\sigma;g_s)=-E^{\min}(-\sigma;-g_s).
```
Cost differences (at $`g_s=0`$) therefore change sign, and $`g_s`$-linear parts (weights) are equal: $`W^{\max}(\sigma)=W^{\min}(-\sigma)`$. Each ratio has the form $`\rho_i=\Delta_{\mathbf e}\Delta_{\mathbf r\mathbf r'}W_b\,\Delta\mathcal C_i/(\text{profile}\times\text{place difference of }\Delta W_i)`$, a weight times a cost over a cost times a weight, and $`g_s`$ cancels in it. Hence, exactly and for both couplings,
```math
\rho_i^{\max}(\sigma)=\rho_i^{\min}(-\sigma),\qquad\rho_i^{{\rm mid},\max}(\sigma)=\rho_i^{{\rm mid},\min}(-\sigma);\qquad\text{at leading order: }B\to-B,\ \ \phi\to-\phi,\ \ F_i\to-F_i,\ \ W_b\to W_b,\ \ \rho_0,\ \rho_0^{\rm mid},\ \tfrac{1+n\gamma_i}{n\gamma_i}\ \text{unchanged}.\qquad\text{(4.14)}
```
- At fixed places an exact ratio is a function of the body couplings, and $`\sigma\to-\sigma`$ reverses all of them at fixed $`\gamma_i`$. At the same branches, only the leading ratios are therefore unchanged. The part of an exact ratio that is odd in the couplings reverses sign; this part contains the first correction beyond $`\rho_0`$, which is linear in them.
- The code checks the mirror identity to rounding error. It also checks the exact ratios for body 1 at $`x_1`$, full grip and coupling (a), at nominal $`\eta=0.08`$ on a ring ($`L=30`$), a square torus ($`L=12`$) and a cubic torus ($`L=8`$). $`\rho^{\max}(\sigma)`$ and $`\rho^{\min}(-\sigma)`$ agree to machine precision.
- The quotient $`(\rho^{\max}(\sigma)-\rho_0)/(\rho^{\min}(\sigma)-\rho_0)`$ is $`-1.06`$ to $`-1.10`$ for the first choice of levels and branches, where the linear correction dominates. For the second choice, with $`\lvert\rho^{\min}(\sigma)-\rho_0\rvert\le0.0051`$, the even second-order part is comparable, and the quotient is $`-0.63`$, $`+0.50`$ and $`-1.79`$.

For odd $`L`$ the highest one-object level of $`C_1`$ is degenerate, so this construction does not define a mirrored state.

## Result

Class: both couplings, every $`N_f\ge1`$, all levels and branches, equal and unequal bodies, ring and square and cubic tori of side $`L\ge3`$, held bodies, field in the stated lowest state (Step 7: highest, for even $`L`$), first order in $`g_s`$, $`\eta<1/12`$ and $`\lvert g_s\rvert\ell_0/t_f<1/12`$.

- **(4.1)** Through third order in the point couplings, the lowest one-object eigenvalue is the Taylor expansion of the root of (4.15), with reduced resolvent $`\Lambda^+/t_f`$ at the unperturbed level.
- **(4.15)** Exactly, $`\varepsilon_0=-2Dt_f+\delta`$ with $`\mathcal X\delta=e^Tg[1+R(\delta)g]^{-1}e`$. For all $`\lvert g_a\rvert\le t_f/(12\ell_0)`$ this equation has exactly one root with $`\lvert\delta\rvert\le t_f\omega_{\min}/2`$. The root is holomorphic in the couplings and, for real couplings, is the non-degenerate lowest eigenvalue, uniformly in $`L`$, $`D`$ and the places.
- **(4.16)** Every Taylor coefficient obeys $`\lvert[g_1^ag_2^bg_s^j]\mathcal X\delta\rvert\le6\rho^{1-a-b-j}`$, $`\rho=t_f/(12\ell_0)`$. Hence, for $`\eta\le1/24`$, every truncation below has an additive remainder bounded with numerical constants independent of $`L`$, $`D`$ and the places (Step 2, "Remainders"). Relative forms hold only where the stated quotients are small.
- **(4.2)** The bond profile is $`E(x_1,\mathbf r)-E(x_1,\mathbf r')=B(\mathbf r)-B(\mathbf r')+O(n\lvert g_1g_2\rvert\ell_0\eta/t_f)`$ with $`B=-\frac{2ng_1g_2}{t_f}\ell(\mathbf r)`$, independent of $`x_1`$. The relative remainder is $`O(\eta\ell_0/\lvert\ell(\mathbf r)-\ell(\mathbf r')\rvert)`$.
  - It is fixed by one total contract, and is the same for both couplings and for every A5 split. So is $`E`$ itself, including its $`\mathbf r`$-independent part.
  - The profile alone does not fix its additive normalization, the zero of $`B`$. The allocation of $`E`$ into rest costs, own marks, bond and individual contracts is a convention (A5), not fixed by $`C`$.
- **(4.3)** On the ring, $`\ell(r)=\frac{L^2-1}{12L}-\frac{r(L-r)}{2L}`$ and the profile is $`\frac{ng_1g_2}{t_fL}[r(L-r)-r'(L-r')]+O(n\lvert g_1g_2\rvert\ell_0\eta/t_f)`$.
- **(4.4)** On the tori, $`\ell(0)-\ell(\mathbf r)`$ has the forms of (4.4). The profile is logarithmic ($`D=2`$) and of the form $`1/\lvert\mathbf r\rvert`$ ($`D=3`$) for $`1\ll\lvert\mathbf r\rvert\ll L`$.
- **(4.5)** A body alone has weight $`W_i=ng_i\phi+\frac{ng_sg_i^2}{t_f^2}[2\ell_0\ell+\ell^2-\frac2{\mathcal X}\ell^{(2)}]`$ with $`\phi=-\frac{2g_s}{t_f}\ell(x-x_s)`$, on all three graphs, up to a place-independent constant and an additive $`O(n\lvert g_s\rvert\eta_i^3)`$. Relative to place differences the remainder is $`O(\eta_i^2\ell_0/\lvert\Delta\ell\rvert)`$.
- **(4.6)** The pair has weight $`W_1(x_1)+W_2(x_2)+W_b`$ with $`W_b=\frac{2ng_sg_1g_2}{t_f^2}S`$, up to an additive $`O(n\lvert g_sg_1g_2\rvert\ell_0^2\eta/t_f^2)`$.
- **(4.7)** $`W_b=\frac12B(\mathbf r)[\phi(x_1)+\phi(x_2)]`$ plus the source-modified propagation term $`\frac{ng_1g_2}{2g_s}\phi(x_1)\phi(x_2)`$ plus a normalization term. The bond is weighed by the same $`\phi`$ as the first-order costs, half at each body.
- **(4.8)** This is an exact rearrangement: the pair is weighed as $`\mathcal C_{\rm p}(\mathbf r)\phi(x_1)`$ plus a term depending only on $`g_1+g_2`$, plus terms of first order in $`\mathbf r\cdot\nabla\ell(\mathbf R)`$.
- **(4.9)** For a body alone, level differences of weight equal level differences of cost times $`F_i`$, up to a relative $`\epsilon_F=O(\eta(1+\lvert\Delta\ell^{(2)}\rvert/(\mathcal X\ell_0\lvert\Delta\ell\rvert))+\eta^2\ell_0/\lvert\Delta\ell\rvert)`$. $`F_i=\phi`$ for the full grip, the same for all levels, branches and bodies; $`F_i=\frac{n\gamma_i}{1+n\gamma_i}\phi`$ for coupling (a).
- **(4.10)** For the full grip the exact ratio of the bond's weight to bond profile times $`F`$ is $`\rho_0+O(\eta K)`$, with $`\rho_0=1+\kappa`$. It holds for $`\ell(\mathbf r)\ne\ell(\mathbf r')`$, $`\Delta_{\mathbf e}\ell(\mathbf R)\ne0`$ and $`\eta K\ll1`$, including configurations with $`\rho_0=0`$.
  - $`K`$ is the explicit place-dependent quotient of Step 6.
  - $`\rho_0`$ depends only on the graph and the places, and not on levels, branches, $`\gamma_i`$, $`N_f`$, $`t_f`$ or the sign of the bond.
- **(4.11)** For $`d\gg1`$, κ is of first order in $`\mathbf r/d`$, $`\mathbf r'/d`$, for $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d\ll L`$ at generic places. It is $`O(\lvert\mathbf r'\rvert/d)`$ on the cubic torus and $`O(\frac{\lvert\mathbf r-\mathbf r'\rvert}{d}\ln\frac{L^2}{\lvert\mathbf r\rvert d})`$ on the square torus. It consists of relocations: when $`\mathbf r`$ changes at fixed $`x_1`$, the midpoint at which the bond is weighed moves, and the $`\mathbf r`$-independent $`g_1g_2`$ terms move with it.
- **(4.12)** Referred to the midpoint, $`\kappa^{\rm mid}`$ has no first-order term:
  - it is $`O(\lvert\mathbf r\rvert\lvert\mathbf r'\rvert/d^2)`$ on the cubic torus and $`O(\frac{\lvert\mathbf r'\rvert^2}{d^2}\ln\frac{L^2}{\lvert\mathbf r'\rvert d})`$ on the square torus;
  - on the ring it is $`0`$ at leading order in η, for $`x_s`$ outside the arc between the bodies. There the ratio referred to $`x_1`$ is $`\frac{2(1-w)(1-2w)}{(1-2u)(1-2v)}`$ for unit steps, with $`u=(d_1+\frac12)/L`$, $`v=(r-\frac12)/L`$, $`w=u+v`$ (unshifted $`u,v`$: large-$`L`$ limit).
  - Answer, full grip, with the midpoint as the natural place and $`x_1`$ as the question's place: yes on the ring (midpoint, exact at leading order in η), and on the cubic torus for $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d\ll L`$. On the square torus, yes only for $`d`$ large against $`\lvert\mathbf r\rvert`$ times a logarithm of $`L`$; at fixed generic places, no as $`L\to\infty`$, by (4.17). The exact ratios differ from these by $`O(\eta K)`$.
- **(4.13)** For coupling (a) the ratio is $`\frac{1+n\gamma_i}{n\gamma_i}`$ times the full-grip ratio, times $`1-\epsilon_C/[(1+n\gamma_i)(1+\epsilon_C)]`$ with $`\lvert\epsilon_C\rvert\le c_*\eta`$, that is $`1+O(\eta)`$ uniformly in $`n`$, $`\gamma_i`$, $`L`$, $`D`$ and the places. Answer: no, on every graph. Wherever the full-grip ratio is 1 (the ring with the midpoint place; the tori in the ranges of (4.11)–(4.12)), the ratio is $`\frac{1+n\gamma_i}{n\gamma_i}(1+O(\eta))>1`$: the bond is weighed more strongly than the level costs of the bodies.
- **(4.14)** In the highest state (even $`L`$), exactly $`\rho_i^{\max}(\sigma)=\rho_i^{\min}(-\sigma)`$ and $`\rho_i^{{\rm mid},\max}(\sigma)=\rho_i^{{\rm mid},\min}(-\sigma)`$, for both couplings, with every branch reversed at fixed $`\gamma_i`$.
  - At leading order $`B`$, $`\phi`$ and $`F_i`$ change sign, $`W_b`$ does not, and $`\rho_0`$, $`\rho_0^{\rm mid}`$ and $`\frac{1+n\gamma_i}{n\gamma_i}`$ are unchanged.
  - At the same branches the exact ratios are not unchanged: their part odd in the couplings, which contains the first correction beyond $`\rho_0`$, reverses sign.
- **(4.17)** On the square torus at fixed places, $`\rho_0=\beta_L\ell_0+\rho_L`$ (likewise $`\rho_0^{\rm mid}`$), with $`\ell_0\simeq\frac1{2\pi}\ln L`$. $`\beta_L`$ and $`\rho_L`$ are built from differences of $`a_L=\ell_0-\ell`$, plus a vanishing $`\ell^{(2)}`$ term in $`\rho_L`$, and converge as $`L\to\infty`$.
  - Where $`\beta=\lim\beta_L\ne0`$, $`K\asymp\ell_0^3`$. The code finds $`\beta\approx1.26`$ and $`0.80`$ at $`x_1=x_s+(8,0)`$ and $`x_s+(16,0)`$, and $`\approx-1.15`$ at the tested midpoint.
  - Along $`\gamma_i(L)=\gamma_i^{(0)}\ell_0(L)^{-5}`$ with any $`\lvert g_s(L)\rvert\le t_f/(24\ell_0(L))`$, η is in the regime for large $`L`$ and $`\eta K=O(1/\ell_0)\to0`$. The exact full-grip ratios $`\beta_L\ell_0+\rho_L+O(\eta K)`$ diverge: this is the control for the full-grip "yes".
  - At fixed couplings only the failure of the leading coefficient is established.

## Consistency checks

1. **Dimensions.** $`g_a`$, $`t_f`$ and $`E`$ are costs, while $`\ell`$, $`\ell^{(2)}/\mathcal X`$ (per $`\ell`$) and $`\phi`$ are pure numbers. $`B\sim ng^2/t_f`$ and $`W_b\sim ng_sg^2/t_f^2`$ are costs, and $`\rho`$ and κ are pure numbers. Passed.
2. **One body and independent bodies.** For $`g_2\to0`$, $`B`$ and $`W_b`$ vanish and (4.8) reduces to (4.5) for body 1. On the cubic torus every term of $`S-\ell^{(2)}(\mathbf r)/\mathcal X`$ carries two factors of ℓ or a factor $`\ell^{(2)}/\mathcal X`$. It therefore vanishes as all separations grow, and the pair is weighed as the sum of its bodies. The code finds $`3.5\cdot10^{-5}`$, $`7.7\cdot10^{-6}`$ and $`1.9\cdot10^{-6}`$ at separations $`L/4`$ for $`L=16,32,64`$. Passed.
3. **Sum rule.** By Hellmann–Feynman, $`\partial_{g_s}\varepsilon_0=\lvert\psi_0(x_s)\rvert^2`$, so $`\sum_{x_s}\partial_{g_s}E=N_f`$ for every $`g_1,g_2`$. Every $`g_1g_2`$ term of the weight must therefore sum to zero over the place. Using $`\sum_x\ell=\sum_x\ell^{(2)}=0`$ and $`\sum_x\ell(a-x)\ell(x-b)=\ell^{(2)}(a-b)`$, $`\sum_{x_1}[S-\ell^{(2)}(\mathbf r)/\mathcal X]=\ell^{(2)}(\mathbf r)-\ell^{(2)}(\mathbf r)=0`$; the code finds at most $`10^{-15}`$. Passed.

## Open issues

- Separations are those of field places; how they relate to the distances of 03-ilang-space is not used here.
- The ratio depends on the place assigned to an extended pair. Referred to $`x_1`$, the question's place, it has the first-order relocation κ. Referred to the midpoint, the natural place, it has none. Which place the fall of a pair tests is for the packages on mutual motion and inertia.
- The $`O(\eta)`$ dependence of the ratio on levels, branches and bodies is shown only numerically (code), not derived.
- Apart from the cost differences of a body alone ($`\epsilon_C`$, used in (4.13)), the remainders are uniform in $`L`$, $`D`$ and the places only in additive form. The derived relative constants grow with $`d`$ and $`L`$ (e.g. $`K`$ of (4.10), or $`\ell_0/\lvert\Delta\ell\rvert`$ for unit steps on large rings). The code finds relative deviations of order η, or of order $`\eta^2`$ for (4.5), far below these bounds and without their growth with $`d`$ and $`L`$ in the tested ranges. A derivation of this sharper relative control is open.
- The estimates of κ and $`\kappa^{\rm mid}`$ on the tori are order estimates at generic places, checked numerically. They fail near places where $`\partial_{\mathbf e}\ell(\mathbf R)`$ vanishes. Likewise, $`\beta\ne0`$ in (4.17) is shown only at the tested places.
- Only held bodies and the lowest (or mirrored highest) field state are treated; other field states (A11) are not.
- For coupling (a) the rest term is not weighed at this order. Whether a wider class of couplings or field contracts weighs it is not decided here (M10: nothing is said about what the language enforces).

## Code

- `code/v3/check_weight_of_bond.py` (role: check). For $`N_f=1`$, $`t_f=1`$ it builds the one-object contract $`h=C_1+g_1P_{x_1}+g_2P_{x_2}+g_sP_{x_s}`$ on a ring ($`L=30,60`$), a square torus ($`L=12,20`$) and a cubic torus ($`L=8,10`$), and takes its exact lowest eigenvalue by dense diagonalization. Setup:
  - couplings $`g_i=\sigma_i\gamma_iM_{k_i}`$ with $`M_k=1+0.5k`$, $`\gamma_2=0.6\gamma_1`$ and $`\gamma_1=\eta/(2.5\ell_0)`$, for a nominal $`\eta=0.08,0.04,0.02`$; the actual $`\max\lvert g_i\rvert\ell_0/t_f`$ is $`0.4\eta`$ (first choice below) and $`0.8\eta`$ (second);
  - two choices of levels and branches, $`(k_1\sigma_1,k_2\sigma_2)=(0{+},1{+})`$ and $`(2{-},3{+})`$, the second with a repulsive bond;
  - $`g_s=0.01/\ell_0`$, with a symmetric difference in $`g_s`$;
  - the $`\ell`$, $`\ell^{(2)}`$ tables computed by FFT.

  It compares with the formulas:
  - the bond profile (4.2), the single-body weight (4.5), the bond part $`W_b`$ (4.6), and the ratios (4.10) (full grip, against both bodies), (4.13) (coupling (a)) and (4.12) (midpoint), all from exact eigenvalues;
  - the mirror identity (4.14) and the sum rule;
  - the ring form (4.3) and the torus forms (4.4) ($`D=2`$: $`L=256,1024`$; $`D=3`$: $`L=64,128`$);
  - the ring ratio (4.12) for $`L=40`$–$`320`$, and κ and $`\kappa^{\rm mid}`$ against $`d`$ ($`D=3`$: $`L=128`$; $`D=2`$: $`L=128,512,2048`$).

  Findings:
  - Every deviation from (4.2), (4.6), (4.10), (4.12) and (4.13) halves when η halves (ratio ≈ 2). The exceptions are entries at the $`10^{-4}`$ level of the $`O(g_s^2)`$ error, or entries crossing zero.
  - The deviation from (4.5) is at most $`4\cdot10^{-3}`$ and falls at least as fast as η.
  - The exact ratios tend to $`\rho_0`$, $`\rho_0^{\rm mid}`$ and $`\frac{1+n\gamma}{n\gamma}\rho_0`$. At $`\eta=0.08`$ they differ between the level choices and the two bodies, e.g. 1.234 against 1.181 on the ring with $`L=30`$.

  Exact finite-rank form (Step 2):
  - The root of (4.15), found by bisection with the kernel $`R(\delta)`$ from FFT, agrees with the exact lowest eigenvalue (sparse Lanczos) to $`2\cdot10^{-14}`$. This holds for the bodies with the source on a ring ($`L=256`$), a square torus ($`L=64`$) and a cubic torus ($`L=16`$).
  - The Hellmann–Feynman coefficient $`\lvert\psi_0(x_s)\rvert^2`$ agrees with the symmetric difference in $`g_s`$ up to $`9.9\cdot10^{-5}`$ and $`2.5\cdot10^{-5}`$ for $`g_s=0.017`$ and $`0.008`$, an $`O(g_s^2)`$ deviation.

  Distance sweeps (I5). Setup:
  - exact eigenpairs by sparse Lanczos, with the $`g_s`$-coefficient of every weight taken exactly as $`\lvert\psi_0(x_s)\rvert^2`$ (Hellmann–Feynman), so no finite source step enters;
  - full grip, body 1, both choices of levels and branches, nominal $`\eta=0.08`$ and $`0.04`$, place $`x_1`$ (or $`\bar x`$) $`=x_s+d\,\mathbf e_1`$ and $`\mathbf e=\mathbf e_1`$;
  - ring, $`L=64,256`$: $`d=L/8,L/4,3L/8`$; $`r=3`$, $`r'=2`$; midpoint $`4,2`$;
  - square torus, $`L=64,256`$: $`d=4`$–$`32`$; $`\mathbf r=(2,1)`$, $`\mathbf r'=(4,3)`$; midpoint $`(2,2)`$, $`(4,2)`$;
  - cubic torus, $`L=16,32`$: $`d=2`$–$`8`$; $`\mathbf r=(0,1,0)`$, $`\mathbf r'=(1,1,1)`$; midpoint $`(0,2,0)`$, $`(2,2,2)`$;
  - the profile for $`\mathbf r=2s\,\mathbf e_1`$ against $`s\,\mathbf e_1`$, $`s=1`$–$`16`$.

  Findings of the sweeps:
  - The deviation from (4.5) is proportional to $`\eta^2`$ (ratio ≈ 4 when η halves) and at most $`7.8\cdot10^{-3}`$. On the tori it does not grow with $`d`$, and between the two sizes it changes by at most 15% (cubic) and 50% (square). On the ring it depends on $`d/L`$, to within 15%.
  - The profile deviation $`\epsilon_B`$ is linear in η (ratio 1.93–2.22, except at one zero crossing) and lies between $`1.5\cdot10^{-3}`$ and $`0.11`$. It does not grow with $`s`$. On the tori it changes by at most about 20% between the two sizes at fixed $`s`$. On the ring it depends on $`s/L`$, and its largest value, at $`s=1`$, is 0.104 for $`L=64`$ and 0.111 for $`L=256`$.
  - $`\rho^{\rm fg}_1-\rho_0`$ is linear in η (ratio 1.76–2.03) wherever $`\lvert\rho^{\rm fg}_1-\rho_0\rvert/\eta>0.04`$; smaller deviations show the next order.
  - $`\lvert\rho^{\rm fg}_1-\rho_0\rvert/\eta`$ (actual η) lies between 0.001 and 2.4, while $`K`$ of (4.10) ranges from $`2\cdot10^2`$ to $`1.6\cdot10^4`$ over the same entries.
    - It is largest on the ring towards the antipode: 2.36 and 2.20 at $`u=3/8`$ for $`L=64`$ and $`256`$.
    - On the ring, from $`L=64`$ to $`256`$ at fixed $`u`$, it changes by a factor between 0.3 and 2.8, while $`K`$ grows by 16.
    - On the tori it is largest at the smallest $`d`$.
  - $`\rho^{\rm mid}_1-\rho^{\rm mid}_0`$ is linear in η (ratio mostly 1.8–2.1) and at most $`1.7\,\eta`$. On the ring, $`\rho^{\rm mid}_0=1`$.

  Added in v3:
  - Mirrored ratios (4.14), by dense diagonalization: the exact $`\rho^{\rm fg}_1`$ and $`\rho^{(a)}_1`$ at $`x_1`$, in the highest state at branches σ, against the lowest state at $`-\sigma`$ and at σ. Nominal $`\eta=0.08`$, $`g_s=0.01/\ell_0`$, both choices of levels and branches, on a ring ($`L=30`$), a square torus ($`L=12`$) and a cubic torus ($`L=8`$). The findings are reported in Step 7.
  - Fixed places on the square torus (4.17), for $`L=128,512,2048`$: $`\beta_L`$, $`\rho_L=\rho_0-\beta_L\ell_0`$, $`K/\ell_0^3`$ and the quotient of $`\lvert\Delta_{\mathbf e}\ell^{(2)}(\mathbf R)\rvert`$ by its bound $`\frac{\pi^2}8(2d+1)\ell_0`$. Places: $`x_1=x_s+(8,0)`$ and $`x_s+(16,0)`$ with $`\mathbf r=(2,1)`$, $`\mathbf r'=(4,3)`$; $`\bar x=x_s+(8,0)`$ with $`\mathbf r=(2,2)`$, $`\mathbf r'=(4,2)`$. Besides the values in Step 6: at $`x_1=x_s+(16,0)`$, $`\beta_L=0.899,\,0.803,\,0.797`$ and $`\rho_L=0.458,\,0.526,\,0.529`$; the quotient by the bound is between 0.05 and 0.12.

  Output: `code/v3/output/check_weight_of_bond.txt`.

## Methods used

- Reduction of held-body sectors to one field object
- Krein formula for a finite-rank perturbation; matrix determinant lemma
- Contraction mapping; Cauchy estimates in several complex variables; Neumann series
- Hellmann–Feynman theorem
- Pseudo-inverse of the graph Laplacian; Fourier analysis on tori
- Asymptotics of the lattice potential kernel ($`\mathbb Z^2`$, $`\mathbb Z^3`$)
- Taylor expansion in separation over distance; parity about the midpoint
- Bipartite sublattice symmetry
- Exact diagonalization, sparse Lanczos and Hellmann–Feynman derivatives (code check)
