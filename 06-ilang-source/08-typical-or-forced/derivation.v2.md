# Typical or forced: couplings and field contracts of the made field

- **Subproject:** 06-ilang-source
- **Package:** 08-typical-or-forced
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-19

## Changes from previous version

- Setup T1, Steps 3, 4, 6, 7: item 1 is answered at first order in $`\gamma`$; $`b`$ and $`h_2`$ drop out of the fall; $`\mathcal S_1`$ now imposes $`\beta=0`$ (dimension $`N+2`$); the larger set $`\mathcal S_1^{\pm}`$ ($`\beta`$ free) is kept apart; $`\mathcal S_1^0`$ is removed (its members now lie in $`\mathcal S_1`$, at $`\alpha=\eta_2=0`$). (I1, I2)
- Step 5: $`\mathcal S_2\subset\mathcal S_1`$ with $`b=\alpha\mathbb 1_N`$; the requirement for $`\mathcal S_1`$ is restated ($`W_*`$ anticommutes with $`\sigma_1`$). (I1, I2)
- Setup item 2: F1 replaced by F0 (coefficient space $`P`$ with its topology; class F requires uniqueness at every side, no commensurability) and the generic set $`U=`$ G1 ∩ G2; F2 states the order of limits. (I3, I4)
- Step 8: (8.8) for every member of class F, at the grid momentum $`k_L`$ of the lowest state; finite-$`L`$ convergence radius of the expansion in $`g`$. (I3, I4)
- Step 9: new necessary condition (8.14) for short range; (8.9) restricted to G1. (I3)
- Step 10: long range proved on $`U`$ for every $`k_0`$ through (8.14); for $`r=1`$ for every member with $`\phi\neq0`$; new genericity statement (8.15); (8.10) with its order of limits; numerical statements corrected. (I3, I4, I5)
- Step 11: restricted to G1 with $`k_0=0`$, inside the complement of (8.15); numerical statements corrected. (I3, I5)
- Step 12: (8.12) stated through limits $`L\to\infty`$; (Z) holds uniformly in $`L`$ for every $`k_0`$. Step 13: membership in class F stated. (I3)
- Code: `code/v2/check_response.py` adds the torus $`L=64`$ through (8.8) and logs maximal deviations over stated windows. (I5)
- Result, consistency check 1, Open issues, Methods used: updated accordingly.

## Response to verification

- **I1:** Accepted and fixed in Setup T1 and Steps 3, 4, 6, 7. The sets are now at first order in $`\gamma`$, where $`a_{k,\sigma}(0)=-\tau^2\gamma N'(f_k+\sigma g_k)/M_k+O(\gamma^2)`$ and $`b`$, $`h_2`$ do not enter. (8.3) is kept as a property of $`C_{\rm eff}`$ as it stands, and it is no longer used to impose conditions.
- **I2:** Accepted and fixed in Steps 4 and 6. $`\mathcal S_1`$ imposes $`\beta=0`$; the set with a level-independent fall on each branch separately is $`\mathcal S_1^{\pm}`$.
- **I3:** Accepted and fixed in Setup F0 and Steps 8–12, within the scope fixed by the dated note of the question. Class F is taken as defined, with the topology of its coefficient space. Long range is proved on the open dense set $`U`$ for every $`k_0`$, commensurate or not, and the complement of $`U`$ is shown closed with empty interior (8.15). The verifier's examples: $`2t[1-\cos(k-\theta)]`$ with $`\phi\neq0`$ lies in $`U`$ and is long range; the quartic minimum lies in the complement. The classification inside the complement (quartic or degenerate minima, $`\bar\phi=0`$ with $`C=cA`$) is not asked by the note; (8.11) is kept only as a statement for G1 with $`k_0=0`$.
- **I4:** Accepted and fixed in Setup F2 and Steps 8, 10. The classification concerns the Taylor coefficient $`\chi_0`$ at each finite $`L`$, before $`L\to\infty`$. The finite-$`L`$ range of the expansion is $`\lvert g\rvert<\Delta_L/(2N_f\lVert\phi\rVert)`$ with $`\Delta_L\le C/L^2`$; no $`L`$-uniform regime is claimed. (8.10) is the limit $`L\to\infty`$ at fixed distances ($`1\ll\lvert d\rvert\ll L`$).
- **I5:** Accepted and fixed in Steps 10, 11 and the code. The maximal deviations are now given over stated windows, separately against the lattice form at the same $`L`$ and against the $`L\to\infty`$ value.

## Setup and assumptions

**Item 1.** One Model D body ($`M_k=m+d_k>0`$, $`d_k=2\pi k/(N\lambda_0)`$ the $`N`$ distinct eigenvalues of $`D`$) is coupled to the field of 04-profile by $`\gamma\sum_xQ_x\otimes\Phi_x`$, with $`Q_x`$ in class C (question). A real function of $`D`$ is the list of its $`N`$ values, written $`f_k:=f(d_k)`$, so class C $`\cong\mathbb R^{5N}`$. The inputs are (5.3)–(5.5) of 05-made-field-scale, (17.11) of 05-ilang-free-fall/17-typical-or-forced and (4.16) of 05-ilang-free-fall/04-branch-fall, as quoted in the question. Assumptions:
- **T1 (test body, first order in $`\gamma`$).** As in 05-made-field-scale, the body evolves under the partial expectation of the total contract in the field state, $`C_{\rm eff}=C_{\rm D}+\gamma\sum_xN_\varphi(x)Q_x+E_\varphi`$. Its own change of the field is neglected, which is an error of order $`\gamma^2`$ (A15). Item 1 is therefore answered at first order in $`\gamma`$: the sets (8.2), (8.4), (8.5), their dimensions (8.6) and the breaking (8.7) keep the terms of order $`\gamma`$ and drop those of order $`\gamma^2`$. (8.1) and (8.3) are written for $`C_{\rm eff}`$ as it stands (exact in $`\gamma N_\varphi`$, with $`M_k+\gamma f_kN_\varphi(x_0)>0`$). They are properties of $`C_{\rm eff}`$, not of the full description beyond first order.
- **T2 (fall).** The fall is the acceleration of a branch start at rest at the band point $`p=0`$, at first order in the gradients of $`N_\varphi`$ (the regime of (4.16)).
- **T3 (field states).** "Every field state" includes states with $`N_\varphi(x+1)\neq N_\varphi(x)`$ at any $`x`$, and slowly varying profiles with any local value $`N_0`$ in an interval and any small slope $`N'\neq0`$ (product states of field objects placed at chosen sites, and their superpositions).

**Item 2.** Class F as in the question; $`\phi_x:=\lvert x\rangle\langle x\rvert\otimes\phi`$ on one object, $`\Phi_x=\sum_j\phi_x^{(j)}`$. Translation invariance and finite range give $`h=\sum_{a\in R}\sum_x\lvert x+a\rangle\langle x\rvert\otimes h_a`$ with finitely many $`r\times r`$ blocks $`h_a=h_{-a}^\dagger`$, and Hermitian Bloch matrices $`h(k)=\sum_ae^{-ik\cdot a}h_a`$ (trigonometric polynomials), with eigenvalues $`\epsilon_0(k)\le\epsilon_1(k)\le\dots`$ and eigenvectors $`w_\ell(k)`$. At side $`L`$, $`k`$ runs over the grid $`\frac{2\pi}L\mathbb Z^D`$ (mod $`2\pi`$). The inputs are (3.6), (4.4) and (4.20), as quoted. Assumptions:
- **F0 (coefficient topology).** Fix $`D`$, $`r`$ and a finite range $`R\supseteq\{0,\pm e_1,\dots,\pm e_D\}`$. A member is a point $`p=((h_a)_{a\in R},\phi)`$ of the real vector space $`P`$ of these coefficients, with its Euclidean topology. It belongs to class F iff $`h`$ has a unique lowest eigenvector at every side $`L`$. That eigenvector is then a Bloch state $`u_0=\lvert X_f\rvert^{-1/2}\sum_xe^{ik_L\cdot x}\lvert x\rangle\otimes w_L`$ at a grid momentum $`k_L`$, with $`w_L:=w_0(k_L)`$, $`\epsilon_L:=\epsilon_0(k_L)`$, $`\bar\phi_L:=\langle w_L\vert\phi\vert w_L\rangle`$. $`\Delta_L>0`$ is the distance of $`\epsilon_L`$ from the rest of the spectrum of $`h`$.
- **G1, G2 (generic set).** G1: over the continuous zone, $`\min_{k,\ell}\epsilon_\ell(k)=:\epsilon_0`$ is attained only at one $`k_0`$ and only by $`\ell=0`$, with $`\epsilon_0(k_0+q)-\epsilon_0=q^{\mathsf T}Aq+O(q^3)`$, $`A>0`$. G2: $`\bar\phi:=\langle w_0\vert\phi\vert w_0\rangle\neq0`$, with $`w_0:=w_0(k_0)`$. $`U\subset P`$ is the set where G1 and G2 hold. No commensurability of $`k_0`$ with the grid is assumed.
- **F2 (state, order, limit).** The field state is the lowest state (M9, named). The made field is the term of order $`g`$ of the Taylor expansion at $`g=0`$, taken at each finite $`L`$ ($`\chi_0`$ of (3.6)). $`L\to\infty`$ is taken afterwards, at fixed $`p`$ and fixed density $`n=N_f/\lvert X_f\rvert`$. Since $`\chi_0/(2n)`$ does not depend on $`N_f`$ (8.8), the range criterion is a property of $`p`$. Distances are graph distances on $`X_f`$.

## Derivation

### Step 1. Effective level blocks in class C

$`C_{\rm D}`$ and every $`Q_x`$ act on the clock label only through functions of $`D`$, so $`C_{\rm eff}`$ commutes with $`D`$ and the level $`k`$ is conserved. On level $`k`$, the terms $`\Pi_x[\dots]`$ give on-site terms. The identity $`\sum_xN(x)\frac12(A_x+A_{x-1})=\sum_xA_x\bar N_x`$, with $`\bar N_x:=\frac12(N(x)+N(x+1))`$, rescales the bond $`(x,x+1)`$. With $`N=N_\varphi`$:
```math
B_{x,k}=M_k\sigma_3+\gamma N(x)\,W_k+E_\varphi,\quad W_k:=f_k\sigma_3+g_k\mathbb 1_2+h_{1,k}\sigma_1+h_{2,k}\sigma_2,\qquad \tau_{x,x+1;k}=\tau\bigl(1+\gamma b_k\bar N_x\bigr),\qquad\text{(8.1)}
```
where $`\frac12\tau_{x,x+1;k}(-i\sigma_1)`$ is the hopping on $`(x,x+1)`$. For couplings (a) and (c) this is (5.3).

### Step 2. R3 at every place

By (8.1), $`B_{x+1,k}-B_{x,k}=\gamma\,\Delta N(x)\,W_k`$. If $`\Delta N(x)\neq0`$, a level-independent $`\Gamma(x)`$ with $`\gamma\Delta N(x)W_k=M_k\Gamma(x)`$ for all $`k`$ exists iff $`W_k/M_k`$ does not depend on $`k`$. By T3 such states exist at every $`x`$. Conversely, $`W_k=M_kW_*`$ gives R3 in every state, with $`\Gamma(x)=\gamma\Delta N(x)W_*`$. Since $`\{\mathbb 1_2,\sigma_i\}`$ is a basis:
```math
\text{R3 at every place in every field state}\iff(f,g,h_1,h_2)=(\alpha,\beta,\eta_1,\eta_2)\,(m\mathbb 1_N+D),\qquad W_*=\alpha\sigma_3+\beta\mathbb 1_2+\eta_1\sigma_1+\eta_2\sigma_2,\qquad\text{(8.2)}
```
with real $`\alpha,\beta,\eta_1,\eta_2`$ and $`b`$ unrestricted.

### Step 3. Rest and fall at $`p=0`$

Freeze the level-$`k`$ blocks at $`x_0`$, with $`N_0:=N(x_0)`$ and $`N':=N'(x_0)`$. The motion term gives $`-\tau\sin p\,\sigma_1`$ on $`\sum_xe^{ipx}\lvert x\rangle`$, so $`H_k(p)=v_k+\mathbf d_k(p)\cdot\boldsymbol\sigma`$, with $`\mathbf d_k=(-\tau_k\sin p+\gamma N_0h_{1,k},\ \gamma N_0h_{2,k},\ \mu_k)`$, $`\mu_k=M_k+\gamma f_kN_0`$, $`v_k=\gamma g_kN_0+E_\varphi`$ and $`\tau_k=\tau(1+\gamma b_kN_0)`$. Branch $`\sigma=\pm`$ has $`E_{k,\sigma}=v_k+\sigma\lvert\mathbf d_k\rvert`$.

(i) At $`p=0`$, $`\partial_pE_{k,\sigma}=\sigma d_1\partial_pd_1/\lvert\mathbf d_k\rvert`$, which gives the velocity in (8.3). At first order in $`\gamma`$ it is $`-\sigma\tau\gamma N_0h_{1,k}/M_k+O(\gamma^2)`$, so it vanishes for every level in every state iff $`h_1=0`$. At $`p=0`$, $`h_1`$ changes $`\lvert\mathbf d_k\rvert`$, its $`x`$-derivative and $`\partial_p^2E_{k,\sigma}`$ only at order $`\gamma^2`$. At first order it therefore enters only through this velocity.

(ii) Let $`h_1=0`$. On level $`k`$, the rotation $`U=\sum_x\lvert x\rangle\langle x\rvert\otimes e^{-i\theta_k(x)\sigma_1/2}`$ takes $`\mu_k\sigma_3+\gamma Nh_{2,k}\sigma_2`$ to $`\tilde\mu_k\sigma_3`$ for a suitable angle $`\theta_k(x)`$, where $`\tilde\mu_k:=(\mu_k^2+\gamma^2N^2h_{2,k}^2)^{1/2}`$. $`U`$ commutes with $`\sigma_1`$ and with every position reading. It turns the bond operator $`-i\sigma_1`$ into $`-i\sigma_1\cos\frac{\delta\theta}2-\sin\frac{\delta\theta}2\,\mathbb 1_2`$, with $`\delta\theta=\theta_k(x+1)-\theta_k(x)`$. The change of the $`\sigma_1`$ part is of second order in the gradients. The branch-diagonal hop is of first order, and its variation in $`x`$ is of second order. At first order, the rotated blocks therefore have the form of (4.16), with $`G_k=\tilde\mu_k'`$, $`\mathcal F_k=-v_k'`$ and the local hopping $`\tau_k`$:
```math
v_{k,\sigma}(0)=-\frac{\sigma\,\tau_k\,\gamma N_0\,h_{1,k}}{\lvert\mathbf d_k(0)\rvert};\qquad h_1=0:\quad a_{k,\sigma}(0)=-\frac{\tau_k^2}{\tilde\mu_k}\bigl(\sigma v_k'+\tilde\mu_k'\bigr)\Big|_{x_0}.\qquad\text{(8.3)}
```

### Step 4. Level- and branch-independent fall: the set $`\mathcal S_1`$

At first order in $`\gamma`$: $`\tilde\mu_k=M_k+\gamma f_kN_0+O(\gamma^2)`$ ($`h_2`$ enters $`\tilde\mu_k`$ only quadratically), $`\tilde\mu_k'=\gamma f_kN'+O(\gamma^2)`$, $`v_k'=\gamma g_kN'`$ and $`\tau_k^2=\tau^2+O(\gamma)`$. With $`h_1=0`$, (8.3) becomes $`a_{k,\sigma}(0)=-\tau^2\gamma N'(f_k+\sigma g_k)/M_k+O(\gamma^2)`$. This is also (4.16) with $`G_k=\gamma f_kN'`$, $`\mathcal F_k=-\gamma g_kN'`$. Neither $`b`$ nor $`h_2`$ enters at this order. States with $`N'\neq0`$ exist (T3), so the fall is the same for all levels and both branches iff $`(f_k+\sigma g_k)/M_k=\alpha`$ for all $`k`$ and $`\sigma`$, i.e. $`g=0`$ and $`f=\alpha(m\mathbb 1_N+D)`$. With (i) and (8.2):
```math
\begin{aligned}
&\mathcal S_1=\bigl\{h_1=0,\ g=0,\ (f,h_2)=(\alpha,\eta_2)(m\mathbb 1_N+D),\ b\ \text{free}\bigr\},\qquad a_{k,\sigma}(0)=-\tau^2\gamma\alpha N'+O(\gamma^2);\\
&\mathcal S_1^{\pm}=\bigl\{h_1=0,\ (f,g,h_2)=(\alpha,\beta,\eta_2)(m\mathbb 1_N+D),\ b\ \text{free}\bigr\},\qquad a_{k,\sigma}(0)=-\tau^2\gamma N'(\alpha+\sigma\beta)+O(\gamma^2).
\end{aligned}\qquad\text{(8.4)}
```
$`\mathcal S_1^{\pm}`$ is the set with R3 and rest. On it the fall is level-independent on each branch, but $`a_{k,+}-a_{k,-}=-2\tau^2\gamma\beta N'`$, so $`\mathcal S_1=\mathcal S_1^{\pm}\cap\{\beta=0\}`$. On $`\mathcal S_1`$ the fall vanishes at this order iff $`\alpha=0`$.

### Step 5. Pure local scale $`\mathcal S_2`$ and the requirement

"The hopping changes by the same local factor as the on-site blocks" means two things: $`B_{x,k}-E_\varphi=\nu(x)M_k\sigma_3`$ with one function $`\nu`$, and $`\tau_{x,x+1;k}=\tau\frac12(\nu(x)+\nu(x+1))`$. By (8.1), the first holds in every state iff $`W_k=\alpha M_k\sigma_3`$ (then $`\nu=1+\gamma\alpha N`$), and the second iff $`b_k=\alpha`$. Define the body's own contract at $`x`$, $`C_{{\rm D},x}:=\Pi_xB+\frac12(A_x+A_{x-1})`$, so that $`\sum_xC_{{\rm D},x}=C_{\rm D}`$. The two conditions select the couplings $`Q_x=\alpha C_{{\rm D},x}`$. Also, $`\sum_xQ_x=\mathbb 1_X\otimes W(D)+A\,b(D)`$; its place-diagonal and off-diagonal parts equal those of $`\alpha C_{\rm D}=\alpha A+\mathbb 1_X\otimes\alpha\sigma_3(m+D)`$ iff $`W=\alpha\sigma_3(m+D)`$ and $`b=\alpha`$. Hence
```math
\mathcal S_2=\{Q_x=\alpha\,C_{{\rm D},x},\ \alpha\neq0\}=\Bigl\{\textstyle\sum_xQ_x=\alpha\,C_{\rm D},\ \alpha\neq0\Bigr\},\qquad C_{\rm eff}=\sum_x\nu(x)\,C_{{\rm D},x}+E_\varphi,\qquad a(0)=-\tau^2\gamma\alpha N'+O(\gamma^2),\qquad\text{(8.5)}
```
with $`\mathcal S_2\subset\mathcal S_1`$ ($`\eta_2=0`$, $`b=\alpha\mathbb 1_N`$; the fall follows from (8.4)). The conditions of the larger sets can also be written with the terms of $`C_{\rm D}`$:
- (8.2): the on-site part of $`Q_x`$ is $`W_*\,\lvert\Pi_xB\rvert`$, with one branch operator $`W_*`$ for all levels, where $`\lvert\Pi_xB\rvert=\Pi_x\otimes\mathbb 1_2\otimes(m+D)`$ is the modulus of the body's own on-site term;
- $`\mathcal S_1`$ in (8.4): in addition, $`W_*`$ anticommutes with $`\sigma_1`$, the branch operator of the motion term, since $`\{W_*,\sigma_1\}=2\beta\sigma_1+2\eta_1\mathbb 1_2`$. The bond part of $`Q_x`$ is free.

### Step 6. Dimensions

Each set is described by linear conditions on $`(f,g,h_1,h_2,b)\in\mathbb R^{5N}`$:
```math
\dim\mathcal S_{\rm R3}=N+4,\qquad\dim\mathcal S_1^{\pm}=N+3,\qquad\dim\mathcal S_1=N+2,\qquad\dim\mathcal S_2=1,\qquad\dim(\text{class C})=5N .\qquad\text{(8.6)}
```
Here $`\mathcal S_{\rm R3}`$ is the set (8.2). For $`N\ge2`$ the codimensions $`4N-4`$, $`4N-3`$, $`4N-2`$ and $`5N-1`$ are positive, so every set lies in a proper linear subspace.

### Step 7. Breaking at first order

Expand around $`P_0=\bigl((\alpha,0,0,\eta_2)(m+D),\,b\bigr)\in\mathcal S_1`$; $`\mathcal S_1`$ contains (a), (c) and $`\mathcal S_2`$. The deviation is $`(\delta f,\delta g,\delta h_1,\delta h_2,\delta b)`$, with $`\delta W_k:=\delta f_k\sigma_3+\delta g_k\mathbb 1_2+\delta h_{1,k}\sigma_1+\delta h_{2,k}\sigma_2`$. The block difference follows exactly from (8.1). The rest velocity follows from Step 3 (i), and the fall from Step 4, which at first order in $`\gamma`$ is linear in $`(f,g)`$ and does not contain $`h_1`$, $`h_2`$, $`b`$:
```math
\begin{aligned}
&B_{x+1,k}-B_{x,k}=M_k\,\gamma\Delta N(x)\,W_*+\gamma\Delta N(x)\,\delta W_k,\qquad v_{k,\sigma}(0)=-\sigma\tau\gamma N_0\,\frac{\delta h_{1,k}}{M_k}+O(\gamma^2),\\
&a_{k,\sigma}(0)=-\tau^2\gamma N'\Bigl[\alpha+\frac{\delta f_k+\sigma\,\delta g_k}{M_k}\Bigr]+O(\gamma^2).
\end{aligned}\qquad\text{(8.7)}
```
So R3 breaks iff $`\delta W_k/M_k`$ depends on $`k`$. The fall becomes level-dependent through $`\delta f_k/M_k`$ and branch-dependent through $`\delta g_k/M_k`$. $`\delta b`$ and $`\delta h_2`$ do not enter at order $`\gamma`$.

### Step 8. Response in class F

Without pair terms, $`C_f=\sum_jh^{(j)}`$. On the symmetric space ($`c=+1`$), its lowest state is $`\varphi_0=u_0^{\otimes N_f}`$, unique by F0. $`\Phi_x`$ is a sum of one-object operators, so $`\Phi_x\varphi_0`$ lies in the span of $`\varphi_0`$ and of the symmetrized states $`\varphi_{(n)}`$ with one object in an excited eigenvector $`u_n`$ of $`h`$. These have $`\langle\varphi_{(n)}\vert\Phi_x\vert\varphi_0\rangle=\sqrt{N_f}\langle u_n\vert\phi_x\vert u_0\rangle`$ and cost $`\epsilon_n-\epsilon_L>0`$. Inserted in (3.6), with Bloch eigenvectors $`u_{k\ell}=\lvert X_f\rvert^{-1/2}\sum_xe^{ik\cdot x}\lvert x\rangle\otimes w_\ell(k)`$ and $`\langle u_0\vert\phi_x\vert u_{k\ell}\rangle=\lvert X_f\rvert^{-1}e^{i(k-k_L)\cdot x}\langle w_L\vert\phi\vert w_\ell(k)\rangle`$, this gives, with $`q:=k-k_L`$ on the grid and $`d:=x-y`$:
```math
\chi_0(x,y)=\frac{2n}{\lvert X_f\rvert}\sum_{q}\cos(q\cdot d)\,S_L(q),\qquad S_L(q)=\sum_{\ell:\,(q,\ell)\neq(0,0)}\frac{\lvert\langle w_L\vert\phi\vert w_\ell(k_L+q)\rangle\rvert^2}{\epsilon_\ell(k_L+q)-\epsilon_L}=\bigl\langle w_L\big\vert\phi\,(h(k_L+q)-\epsilon_L)^{-1}\phi\big\vert w_L\bigr\rangle\ \ (q\neq0).\qquad\text{(8.8)}
```
Every term of $`S_L`$ is $`\ge0`$. The source $`g\Phi_{x_s}`$ moves the lowest state by $`-gQ_0\Phi_{x_s}\varphi_0`$ at first order. The made field is therefore $`N(y)=n\bar\phi_L-g\chi_0(y,x_s)+O(g^2)`$, where $`N_{\varphi_0}=N_f\langle u_0\vert\phi_y\vert u_0\rangle=n\bar\phi_L`$. At fixed $`L`$ the lowest state is analytic in $`g`$ for $`\lvert g\rvert<\Delta_L/(2N_f\lVert\phi\rVert)`$ (isolated simple eigenvalue, $`\lVert\Phi_{x_s}\rVert\le N_f\lVert\phi\rVert`$; standard), which is the range of the $`O(g^2)`$ term. On G1, $`\Delta_L\le C'/L^2`$ (Step 10), so this range shrinks with $`L`$. No $`L`$-uniform small-coupling regime is claimed, and the range classification concerns $`\chi_0`$ (F2). The cross term of second-order perturbation theory gives the mutual cost of two sources, $`-g_1g_2\chi_0(x_1,x_2)`$. Summing (8.8) over $`y`$ gives $`\sum_y\chi_0(x,y)=2n\,S_L(0)`$. The code check confirms (8.8) against direct diagonalization (`check_log.txt`: deviation $`\le6\times10^{-12}`$ on rings and tori).

### Step 9. Two criteria on $`S_L`$, and the singular part

The grid is symmetric, so only the even part $`S_{L,\rm e}(q):=\frac12(S_L(q)+S_L(-q))`$ enters (8.8), and $`\sum_ye^{-iq\cdot(y-x_s)}\chi_0(y,x_s)=2nS_{L,\rm e}(q)`$ for $`q\neq0`$.

(i) **Necessary.** Let the field be short range, $`\lvert\chi_0(y,x_s)-\chi_0(y',x_s)\rvert\le2nCe^{-d/\xi}`$ for all $`L`$ and all $`y,y'`$ at distance $`\ge d`$ from $`x_s`$. Take $`y'`$ at maximal distance; then the bound holds with $`d=\lvert y-x_s\rvert`$ for every $`y`$. Since $`\sum_ye^{-iq\cdot(y-x_s)}=0`$ for $`q\neq0`$, the constant $`\chi_0(y',x_s)`$ may be subtracted, and with $`c_D(d+1)^{D-1}`$ bounding the number of places at distance $`d`$:
```math
\text{short range}\ \Longrightarrow\ \bigl\lvert S_{L,\rm e}(q)\bigr\rvert\le C\sum_{d\ge0}c_D(d+1)^{D-1}e^{-d/\xi}=:K<\infty\qquad\text{for all }L\text{ and all grid }q\neq0.\qquad\text{(8.14)}
```

(ii) **Sufficient.** Suppose that for $`L\ge L_0`$, $`S_{L,\rm e}`$ is the restriction to the grid of a $`2\pi`$-periodic function, analytic and bounded by $`K'`$ on the strip $`\lvert\mathrm{Im}\,q_\mu\rvert<\eta`$, with $`K',\eta`$ independent of $`L`$. Then its Fourier coefficients decay as $`e^{-\eta'\lvert d\rvert}`$ for every $`\eta'<\eta`$, uniformly in $`L`$ (shift each $`q_\mu`$ into the strip). The finite sum (8.8) is the sum of their periodic images plus a $`d`$-independent term of order $`\lvert X_f\rvert^{-1}`$ (from $`q=0`$). Hence the field is short range; the finitely many $`L<L_0`$ are absorbed into $`C`$.

(iii) **Singular part on G1.** Let $`S(q):=\langle w_0\vert\phi(h(k_0+q)-\epsilon_0)^{-1}\phi\vert w_0\rangle`$ for $`q\neq0`$. If $`k_0=0`$, then $`k_L=k_0`$, $`\epsilon_L=\epsilon_0`$ and $`S_L=S`$ on the grid for every $`L`$. By G1, $`h(k)-\epsilon_0`$ is invertible for real $`k\neq k_0`$, so $`S`$ is real-analytic on the torus minus $`q=0`$. Near $`k_0`$, $`\epsilon_0(k)`$ is an isolated simple eigenvalue, and its spectral projector $`P_0(k)`$ is analytic:
```math
S(q)=\frac{\lvert F(q)\rvert^2}{\epsilon_0(k_0+q)-\epsilon_0}+S_{\rm an}(q),\qquad\lvert F(q)\rvert^2:=\langle w_0\vert\phi P_0(k_0+q)\phi\vert w_0\rangle,\quad\lvert F(0)\rvert^2=\bar\phi^2,\qquad\text{(8.9)}
```
with $`\lvert F\rvert^2`$ and $`S_{\rm an}`$ analytic. For $`k_0=0`$, by (ii), the field is short range whenever $`S_{\rm e}`$ extends analytically to $`q=0`$. Otherwise the leading non-analytic homogeneous term of $`S_{\rm e}`$ at $`q=0`$ fixes the large-distance form (Steps 10–11).

### Step 10. $`\bar\phi\neq0`$: long range on $`U`$, and genericity

**Long range.** Let $`p\in U\cap{}`$F. By G1, $`\epsilon_0(k)-\epsilon_0\ge c_1\lvert k-k_0\rvert^2`$ on the zone (quadratic near $`k_0`$, bounded below elsewhere; torus distance). The grid point nearest to $`k_0`$ lies within $`\pi\sqrt D/L`$, so $`\epsilon_L-\epsilon_0\le C/L^2`$ and $`\lvert k_L-k_0\rvert\le c/L`$. With $`q_L:=\frac{2\pi}Le_1`$, this gives $`\epsilon_0(k_L\pm q_L)-\epsilon_L\le C'/L^2`$ (hence $`\Delta_L\le C'/L^2`$), and $`\lvert\langle w_L\vert\phi\vert w_0(k_L\pm q_L)\rangle\rvert^2\to\bar\phi^2`$ by continuity of $`w_0(k)`$ near $`k_0`$. Keeping only the lowest-band term of the nonnegative sum (8.8), $`S_{L,\rm e}(q_L)\ge\bar\phi^2L^2/(4C')`$ for large $`L`$. This is unbounded, so by (8.14) the made field is long range, for every $`k_0`$, commensurate with the grid or not. For $`r=1`$ the same holds for every member of class F with $`\phi\neq0`$: then $`S_L(\pm q_L)=\phi^2/(\epsilon(k_L\pm q_L)-\epsilon_L)`$, and $`0<\epsilon(k_L\pm q_L)-\epsilon_L\le\lVert\nabla\epsilon\rVert_\infty\,2\pi/L`$.

**Leading form.** Take $`L\to\infty`$ along sides with $`L\lvert k_L-k_0\rvert\to0`$. This holds for every side if $`k_0=0`$, and such sides exist for every $`k_0`$ (Dirichlet's simultaneous approximation). Then $`\epsilon_0(k_L+q)-\epsilon_L=q^{\mathsf T}Aq\,(1+o(1))`$ for $`\lvert q\rvert=O(1/L)`$ and $`\ge c\lvert q\rvert^2`$ for all grid $`q\neq0`$. So the Riemann sums (8.8) for differences $`\chi_0(y,x_s)-\chi_0(y',x_s)`$ at fixed $`y,y'`$ converge to the integrals with $`S`$ of (8.9), dominated by $`C\lvert q\rvert^2/\lvert q\rvert^2`$. Now $`S_{\rm e}(q)=\bar\phi^2/(q^{\mathsf T}Aq)+[\text{even terms of degree }0]+\dots`$, because the terms of degree $`-1`$ are odd. The Fourier integral of $`1/(q^{\mathsf T}Aq)`$ is the Green function $`\mathcal G_A`$ of $`-\nabla^{\mathsf T}A\nabla`$ (standard, up to a constant for $`D=1,2`$). An even function of degree $`0`$ gives $`O(\lvert d\rvert^{-D})`$ for $`d\neq0`$. In $`D=1`$, $`S-\bar\phi^2/(Aq^2)`$ is analytic up to an odd term. In the limit $`L\to\infty`$ at fixed $`y,y'`$ (taken first; at finite $`L`$ the form describes $`1\ll\lvert d\rvert,\lvert d'\rvert\ll L`$):
```math
\begin{aligned}
&\chi_0(y,x_s)-\chi_0(y',x_s)=2n\bar\phi^2\bigl[\mathcal G_A(y-x_s)-\mathcal G_A(y'-x_s)\bigr]+R,\\
&\mathcal G_A(d)=-\frac{\lvert d\rvert}{2A}\ (D=1),\qquad-\frac{\ln(d^{\mathsf T}A^{-1}d)}{4\pi\sqrt{\det A}}\ (D=2),\qquad\frac{1}{4\pi\sqrt{\det A}\,(d^{\mathsf T}A^{-1}d)^{1/2}}\ (D=3),
\end{aligned}\qquad\text{(8.10)}
```
with $`R=O(e^{-\min(\lvert d\rvert,\lvert d'\rvert)/\xi})`$ for $`D=1`$ and $`R=O(\lvert d\rvert^{-D}+\lvert d'\rvert^{-D})`$ for $`D=2,3`$, where $`d=y-x_s`$ and $`d'=y'-x_s`$. Along an axis, $`\mathcal G_A(d)-\mathcal G_A(2d)`$ is proportional to $`d`$, $`\ln2`$ and $`1/d`$ respectively. The made field is $`N(y)-N(y')=-g\times`$(8.10).

**Genericity.** G1 is open in $`P`$: the lowest eigenvalue is continuous in $`(k,p)`$, simple and analytic near $`k_0`$ with positive Hessian, and above $`\epsilon_0+c`$ away from a neighbourhood of $`k_0`$; a small change of $`p`$ keeps one nondegenerate minimum near $`k_0`$ (implicit function theorem) and none elsewhere. On G1, $`w_0`$ and $`\bar\phi`$ are continuous, so $`U`$ is open. $`U`$ is dense: given $`p`$, a minimizer $`k_*`$ of $`\epsilon_0`$ and a lowest eigenvector $`v`$ of $`h(k_*)`$, add the nearest-neighbour term with Bloch matrix $`\delta\,w(k)\mathbb 1_r`$, $`w(k)=\sum_\mu(1-\cos(k_\mu-k_{*\mu}))`$, and the on-site term $`-\delta'\lvert v\rangle\langle v\rvert`$, with $`\delta,\delta'>0`$ small. The new lowest eigenvalue is $`\ge\epsilon_0(k)-\delta'+\delta w(k)>\epsilon_0(k_*)-\delta'`$ for $`k\neq k_*`$. At $`k_*`$ it equals $`\epsilon_0(k_*)-\delta'`$ and is simple ($`v`$ is an eigenvector, and $`v^\perp`$ is untouched). Its Hessian is $`\ge\delta\mathbb 1`$. So G1 holds, and $`\phi\to\phi+\epsilon\mathbb 1_r`$ ($`\bar\phi\to\bar\phi+\epsilon`$) gives G2. The same perturbation, with $`k_*`$ a minimizer on the grid of side $`L`$, makes the lowest eigenvalue at side $`L`$ simple, which is an open condition. So class F is a countable intersection of open dense subsets of $`P`$, dense by Baire's theorem. A nonempty relatively open subset $`V\cap{}`$F of class F therefore meets $`U`$, because $`V\cap U`$ is open and nonempty. Hence, in the topology of F0:
```math
U\cap\text{F is open and dense in class F; its complement F}\setminus U\text{ (G1 fails, or }\bar\phi=0\text{) is closed in F with empty interior; on G1}\cap\text{F, short range requires }\bar\phi=0.\qquad\text{(8.15)}
```

The code check confirms (8.10) (`check_log.txt`). On the rings $`L=40,80,160`$, the ratio of the differences $`\chi_0(d)-\chi_0(L/2)`$ to those of the lattice form of $`\bar\phi^2/(q^{\mathsf T}Aq)`$ at the same $`L`$ differs from 1 by at most $`4.8\times10^{-5}`$ over $`6\le d\le L/2-6`$, and the oscillation $`\Omega(L/4)=1.5,3.0,6.0`$ grows $`\propto L`$. On the tori, the same ratio over $`3\le d\le L/4`$ differs from 1 by at most $`2.2\%`$ ($`L=20`$), $`1.6\%`$ ($`L=32`$) and $`1.1\%`$ ($`L=64`$, through (8.8)). The maximum is at $`d=3`$; at $`d=L/4=16`$ ($`L=64`$) the deviation is below $`0.2\%`$, as expected from the remainder $`R`$.

### Step 11. $`\bar\phi=0`$ on G1 with $`k_0=0`$ (inside the complement)

The members with $`\bar\phi=0`$ lie in the complement of (8.15). Their classification is not asked (question, note of 2026-10-19). For members of G1 with $`k_0=0`$ ($`S_L=S`$ for every $`L`$), the leading order of (8.9) gives the following. $`\lvert F(q)\rvert^2=q^{\mathsf T}Cq+O(q^3)`$, with $`C:=\frac12\nabla_q\nabla_q^{\mathsf T}\lvert F\rvert^2\big|_0\ge0`$. In a smooth gauge $`F(q)=\mathbf c\cdot q+O(q^2)`$, so $`C=\mathrm{Re}\,\mathbf c\,\mathrm{Re}\,\mathbf c^{\mathsf T}+\mathrm{Im}\,\mathbf c\,\mathrm{Im}\,\mathbf c^{\mathsf T}`$ has rank $`\le2`$.

For $`D=1`$, write $`\lvert F\rvert^2=q^2v(q)`$ and $`\epsilon_0(k_0+q)-\epsilon_0=q^2u(q)`$ with $`v,u`$ analytic and $`u(0)=A>0`$. Then $`S`$ is analytic at $`0`$ and the field is short range (Step 9 (ii)).

For $`D=2,3`$, the leading term of $`S_{\rm e}`$ is $`q^{\mathsf T}Cq/q^{\mathsf T}Aq`$, of degree 0; the next even term has degree 2. With $`q_\mu q_\nu\leftrightarrow-\partial_\mu\partial_\nu`$:
```math
\bar\phi=0,\ D=2,3:\qquad\chi_0(y,x_s)=-2n\sum_{\mu,\nu}C_{\mu\nu}\,\partial_\mu\partial_\nu\mathcal G_A(y-x_s)+c_L+O(\lvert y-x_s\rvert^{-D-1}),\qquad\text{(8.11)}
```
where $`c_L`$ does not depend on $`y`$. The leading term is homogeneous of degree $`-D`$. It vanishes for all $`d\neq0`$ iff $`q^{\mathsf T}Cq/q^{\mathsf T}Aq`$ is constant, i.e. $`C=cA`$; for $`D=3`$ the rank bound then forces $`C=0`$.

The code check (`check_log.txt`) illustrates both cases. For the 1D member with $`\bar\phi=0`$ and no conserved sector, the fitted decay rate of $`\lvert\chi_0(d)-\chi_0(L/2)\rvert`$ over $`4\le d\le14`$ is $`1.03774`$ ($`L=40`$) and $`1.03749`$ ($`L=80,160`$). The distance of the nearest complex zero of $`\det(h(k)-\epsilon_0)`$ from the real axis is $`1.03749`$. For the 2D member of the same construction, $`Y(d):=d^2(\chi_0(d)-\chi_0(\text{corner}))/(2n)`$ is negative along axis 1 and positive along axis 2, as (8.11) requires. Against the lattice form of the leading term of (8.11) at the same $`L`$, the maximal relative deviation over $`8\le d\le L/2-2`$ is $`7.4\%`$ ($`L=20`$), $`6.1\%`$ ($`L=32`$) and $`6.1\%`$ ($`L=64`$, through (8.8)), and $`2.0\%`$ over $`16\le d\le30`$ at $`L=64`$. It decreases with $`d`$, consistent with the remainder of (8.11). Against the $`L\to\infty`$ values $`-0.01937`$ and $`+0.02325`$, the deviation is at most $`2.8\%`$ over $`8\le d\le12`$ at $`L=64`$. For $`d\gtrsim L/4`$, $`Y(d)`$ grows through the finite-size images (order $`(d/L)^2`$).

### Step 12. Conditions stated through the contract

(i) **Long range.** Every member of class F conserves the number of field objects, $`\sum_xn_x=N_f`$ with $`n_x:=\sum_j(\lvert x\rangle\langle x\rvert\otimes\mathbb 1_r)^{(j)}`$. On G1 this number is carried by a band that becomes gapless as $`L\to\infty`$. By Step 10, on G1 the made field is long range, with the Coulomb-type form (8.10), when $`\Phi_x`$ carries the density of this conserved number in the lowest state:
```math
\bar\phi=\lim_{L\to\infty}\frac{\langle\varphi_0\vert\Phi_x\vert\varphi_0\rangle}{\langle\varphi_0\vert n_x\vert\varphi_0\rangle}\neq0\iff\lim_{L\to\infty}\frac{\lvert X_f\rvert}{\sqrt{N_f}}\,\bigl\lvert\langle\varphi_{q_L}\vert\Phi_x\vert\varphi_0\rangle\bigr\rvert=\lvert\bar\phi\rvert\neq0,\qquad\text{(8.12)}
```
where $`\varphi_q`$ is the lowest-band one-object excitation at momentum $`k_L+q`$ and $`q_L=\frac{2\pi}Le_1`$. The ratio equals $`\bar\phi_L\to\bar\phi`$. The right-hand form follows from $`\lvert\langle u_q\vert\phi_x\vert u_0\rangle\rvert=\lvert X_f\rvert^{-1}\lvert\langle w_0(k_L+q)\vert\phi\vert w_L\rangle\rvert`$ and the continuity of $`w_0`$ near $`k_0`$. It does not change under $`\Phi_x\to\Phi_x+c\mathbb 1`$ (M6).

(ii) **Short range, sufficient condition (Z).** Suppose there is a Hermitian $`Z`$ on $`\mathbb C^r`$ with $`[h,\mathbb 1\otimes Z]=0`$, so that the charge $`\sum_jZ^{(j)}`$ is conserved by $`C_f`$. Suppose further that $`w_0`$ lies in an eigenspace of $`Z`$ with projector $`P_Z`$, and $`P_Z\phi P_Z=0`$ ($`\Phi_x`$ changes the charge). Then $`[h(k),Z]=0`$, by continuity $`w_0(k)\in P_Z`$ near $`k_0`$, and $`\phi w_L\in(1-P_Z)`$ for large $`L`$. Hence $`S_L(q)=\langle w_L\vert\phi(1-P_Z)(h(k_L+q)-\epsilon_L)^{-1}(1-P_Z)\phi\vert w_L\rangle`$. By G1, the bands of $`h(k)`$ on $`(1-P_Z)`$ stay above $`\epsilon_0+g_Z`$, $`g_Z>0`$, on the whole zone, and $`\epsilon_L\to\epsilon_0`$. So for large $`L`$, $`S_L`$ is the restriction of a function analytic and bounded on a strip of fixed width, uniformly in $`L`$. By Step 9 (ii) the field is short range in every $`D`$, for every $`k_0`$. Such members have $`\bar\phi=0`$.

### Step 13. A short-range member

Take $`r=2`$, $`h=(C_1+2Dt_f)\otimes\mathbb 1_2+\Delta\,\mathbb 1\otimes\lvert2\rangle\langle2\rvert`$ with $`t_f,\Delta>0`$, and $`\phi=\sigma_1`$; (Z) holds with $`Z=\sigma_3`$. Then $`h(k)=\mathrm{diag}(t_f\omega(k),\,t_f\omega(k)+\Delta)`$, $`k_0=0`$, $`w_0=\lvert1\rangle`$, G1 holds with $`A=t_f\mathbb 1`$, and the lowest eigenvector is unique at every side (class F). Moreover $`S_L(q)=1/(t_f\omega(q)+\Delta)`$ for every $`q`$, including $`q=0`$. The 1D lattice sum is standard:
```math
\chi_0(x,y)=\frac{2n}{\lvert X_f\rvert}\sum_q\frac{\cos(q\cdot d)}{t_f\omega(q)+\Delta};\qquad D=1:\ \chi_0=\frac{n}{t_f\sinh\kappa}\,\frac{\cosh\kappa(\frac L2-d)}{\sinh\frac{\kappa L}2},\quad\cosh\kappa=1+\frac{\Delta}{2t_f},\ 0\le d\le L.\qquad\text{(8.13)}
```
For every $`D`$, shifting each $`q_\mu`$ by $`\pm i\eta`$ with $`\cosh\eta<1+\Delta/(2Dt_f)`$ keeps $`\mathrm{Re}(t_f\omega+\Delta)>0`$. Hence $`\lvert\chi_0(x,y)\rvert\le C_\eta e^{-\eta\,\mathrm{dist}(x,y)}`$ uniformly in $`L`$. The code check confirms the 1D form to $`2\times10^{-13}`$.

## Result

Class C, test body (T1), every field state (T3); the sets, dimensions and breaking at first order in $`\gamma`$, the fall at first order in the gradients (T2) at the band point $`p=0`$. (8.1) and (8.3) hold for $`C_{\rm eff}`$ as it stands (exact in $`\gamma N_\varphi`$).
- **(8.1)** The effective level-$`k`$ blocks are $`B_{x,k}=M_k\sigma_3+\gamma N(x)W_k+E_\varphi`$ and $`\tau_{x,x+1;k}=\tau(1+\gamma b_k\bar N_x)`$.
- **(8.2)** R3 holds at every place in every field state iff $`(f,g,h_1,h_2)=(\alpha,\beta,\eta_1,\eta_2)(m\mathbb 1_N+D)`$, with $`b`$ free; then $`\Gamma(x)=\gamma\Delta N(x)W_*`$.
- **(8.3)** For $`C_{\rm eff}`$, the start at $`p=0`$ has velocity $`v_{k,\sigma}(0)=-\sigma\tau_k\gamma N_0h_{1,k}/\lvert\mathbf d_k(0)\rvert`$, which is $`-\sigma\tau\gamma N_0h_{1,k}/M_k+O(\gamma^2)`$; it is at rest in every state iff $`h_1=0`$. For $`h_1=0`$ the fall is $`a_{k,\sigma}(0)=-\tau_k^2(\sigma v_k'+\tilde\mu_k')/\tilde\mu_k`$.
- **(8.4)** At first order in $`\gamma`$ the fall from rest is $`a_{k,\sigma}(0)=-\tau^2\gamma N'(f_k+\sigma g_k)/M_k+O(\gamma^2)`$; $`b`$ and $`h_2`$ do not enter. The couplings with R3 at every place, rest at $`p=0`$, and a fall equal across levels and across the two branches in every field state form $`\mathcal S_1=\{h_1=0,\ g=0,\ (f,h_2)=(\alpha,\eta_2)(m\mathbb 1_N+D),\ b\text{ free}\}`$, with $`a_{k,\sigma}(0)=-\tau^2\gamma\alpha N'+O(\gamma^2)`$ (zero at this order iff $`\alpha=0`$). The larger set $`\mathcal S_1^{\pm}=\{h_1=0,\ (f,g,h_2)=(\alpha,\beta,\eta_2)(m\mathbb 1_N+D),\ b\text{ free}\}`$ (R3 and rest) has a level-independent fall on each branch, $`a_{k,\sigma}(0)=-\tau^2\gamma N'(\alpha+\sigma\beta)+O(\gamma^2)`$, which differs between the branches iff $`\beta\neq0`$. Control: the rest-only coupling (r) lies outside $`\mathcal S_1^{\pm}`$.
- **(8.5)** The subset on which, in addition, the on-site blocks scale by one local factor $`\nu`$ and the hopping by $`\frac12(\nu(x)+\nu(x+1))`$ is $`\mathcal S_2=\{Q_x=\alpha C_{{\rm D},x}\}=\{\sum_xQ_x=\alpha C_{\rm D}\}`$, $`\alpha\neq0`$. On $`\mathcal S_2`$, $`C_{\rm eff}=\sum_x\nu(x)C_{{\rm D},x}+E_\varphi`$ and $`a(0)=-\tau^2\gamma\alpha N'+O(\gamma^2)`$. Coupling (a) lies in $`\mathcal S_1`$ but not in $`\mathcal S_2`$; coupling (c) lies in $`\mathcal S_2`$. The sets (8.2), $`\mathcal S_1`$ and $`\mathcal S_2`$ are selected by requirements written with the terms of $`C_{\rm D}`$ (Step 5). For $`\mathcal S_1`$, the on-site part of $`Q_x`$ is $`W_*\lvert\Pi_xB\rvert`$, with one branch operator $`W_*`$ that anticommutes with the branch operator $`\sigma_1`$ of the motion term. For $`\mathcal S_2`$, a uniform field rescales the body's own contract.
- **(8.6)** $`\dim\mathcal S_{\rm R3}=N+4`$, $`\dim\mathcal S_1^{\pm}=N+3`$, $`\dim\mathcal S_1=N+2`$, $`\dim\mathcal S_2=1`$, inside $`\dim(\text{class C})=5N`$. For $`N\ge2`$ every set lies in a proper linear subspace, so each is nowhere dense and of measure zero: exceptional, not typical. Every member of class C is admissible, so within class C the language does not select these couplings (M10).
- **(8.7)** At first order in $`\gamma`$ and in a deviation from $`P_0\in\mathcal S_1`$, R3 breaks by $`\gamma\Delta N(x)\,\delta W_k`$; this defect is exact and is absent iff $`\delta W_k/M_k`$ is level-independent. The rest at $`p=0`$ breaks by $`v_{k,\sigma}(0)=-\sigma\tau\gamma N_0\delta h_{1,k}/M_k`$. The fall becomes $`a_{k,\sigma}(0)=-\tau^2\gamma N'[\alpha+(\delta f_k+\sigma\delta g_k)/M_k]`$: it is level-dependent through $`\delta f_k/M_k`$ and branch-dependent through $`\delta g_k/M_k`$. $`\delta b`$ and $`\delta h_2`$ do not enter at order $`\gamma`$.

Class F (F0, with the Euclidean topology of the coefficient space $`P`$), lowest state (F2). $`\chi_0`$ is exact at each finite $`L`$. The made field is its term of order $`g`$ at fixed $`L`$, valid for $`\lvert g\rvert<\Delta_L/(2N_f\lVert\phi\rVert)`$. Large-distance forms hold for $`L\to\infty`$ at fixed distances.
- **(8.8)** For every member of class F, $`\chi_0(x,y)=\frac{2n}{\lvert X_f\rvert}\sum_q\cos(q\cdot d)S_L(q)`$, with $`S_L(q)=\langle w_L\vert\phi(h(k_L+q)-\epsilon_L)^{-1}\phi\vert w_L\rangle\ge0`$ for $`q\neq0`$. The made field is $`N(y)=n\bar\phi_L-g\chi_0(y,x_s)+O(g^2)`$.
- **(8.14)** If the made field is short range, $`S_{L,\rm e}(q)`$ is bounded uniformly in $`L`$ and in the grid momenta $`q\neq0`$.
- **(8.9)** On G1, $`S=\lvert F\rvert^2/(\epsilon_0(k_0+q)-\epsilon_0)+S_{\rm an}`$, with $`\lvert F(0)\rvert^2=\bar\phi^2`$. For $`k_0=0`$, the field is short range whenever the even part of $`S`$ is analytic at $`q=0`$.
- **(8.10)** On $`U`$ (G1 and $`\bar\phi\neq0`$), the made field is long range for every $`k_0`$. For $`L\to\infty`$ along sides with $`L\lvert k_L-k_0\rvert\to0`$ (all sides if $`k_0=0`$), at fixed $`y,y'`$: $`\chi_0(y,x_s)-\chi_0(y',x_s)=2n\bar\phi^2[\mathcal G_A(y-x_s)-\mathcal G_A(y'-x_s)]+R`$. This is linear in $`D=1`$, logarithmic in $`D=2`$ and $`1/\lvert d\rvert`$ in $`D=3`$. For $`r=1`$, every member of class F with $`\phi\neq0`$ is long range.
- **(8.15)** $`U\cap{}`$F is open and dense in class F. Its complement (G1 fails, or $`\bar\phi=0`$) is closed in class F with empty interior. Long range is therefore typical, and short range exceptional. On G1, short range requires $`\bar\phi=0`$.
- **(8.11)** Inside the complement, for members of G1 with $`k_0=0`$ and $`\bar\phi=0`$ (not a classification of the complement): in $`D=1`$ the field is short range. In $`D=2,3`$, $`\chi_0=-2n\sum C_{\mu\nu}\partial_\mu\partial_\nu\mathcal G_A+c_L+O(\lvert d\rvert^{-D-1})`$ as $`L\to\infty`$, a power law $`\lvert d\rvert^{-D}`$ (long range) unless $`C=cA`$ (for $`D=3`$: $`C=0`$).
- **(8.12)** On G1, long range follows from the condition that $`\Phi_x`$ carries the density of the conserved number of field objects, whose band is gapless: $`\bar\phi\neq0`$, in the M6-invariant form (8.12). This condition holds on the open dense set $`U`$. On G1, a sufficient condition for short range in every $`D`$ and for every $`k_0`$ is (Z): a conserved charge $`\sum_jZ^{(j)}`$ that $`\Phi_x`$ changes within the sector of the lowest state, with the other sectors gapped (then $`\bar\phi=0`$).
- **(8.13)** A short-range member of class F exists: $`r=2`$, $`h=(C_1+2Dt_f)\otimes\mathbb 1_2+\Delta\,\mathbb 1\otimes\lvert2\rangle\langle2\rvert`$, $`\phi=\sigma_1`$, $`\Delta,t_f>0`$. It has the exact form (8.13) and $`\lvert\chi_0\rvert\le C_\eta e^{-\eta\,\mathrm{dist}}`$ uniformly in $`L`$ for $`\cosh\eta<1+\Delta/(2Dt_f)`$. Controls: this member for the long-range statement (8.10); the members of $`U`$ for the short-range statements (8.11)–(8.12).

## Consistency checks

1. **Couplings (a), (c), (r) and dimensions.** (8.1) reproduces (5.3) for (a) and (c). Coupling (a) is $`\alpha=1`$, $`b=0`$, in $`\mathcal S_1`$. (8.4) gives $`a=-\tau^2\gamma N'+O(\gamma^2)`$, the first-order part of $`-\tau^2\gamma N'/\nu(x_0)`$, which is what (4.16) gives with (5.3). Coupling (c) is $`\alpha=1`$, $`b=\mathbb 1_N`$, in $`\mathcal S_2`$, with the same first-order fall. For (r), $`W_k/M_k=m\sigma_3/M_k`$ is level-dependent (not R3), in agreement with (5.5). (8.4) gives $`a=-\tau^2\gamma mN'/M_k+O(\gamma^2)`$, the first-order part of (5.5), and (8.3) reproduces (5.5) exactly for $`C_{\rm eff}`$. $`\gamma N`$ is dimensionless, and $`a`$ has the dimension of $`\tau^2`$. Passed.
2. **Class of 04-profile.** For $`r=1`$, $`\phi=1`$, $`h=C_1`$: $`k_0=0`$, $`\bar\phi=1`$, $`A=t_f\mathbb 1`$, and $`S_L(q)=1/(t_f\omega(q))`$ with $`S_L(0)=0`$. So (8.8) gives $`\chi_0=\frac{2n}{t_f}\Lambda^+`$, and the mutual cost $`-g_1g_2\chi_0`$ is (4.4), together with its sum rule $`\sum_y\chi_0=2nS_L(0)=0`$. (8.10) then gives $`2n\mathcal G_{\mathbb 1}/t_f`$. Passed.
3. **Short-range member against (4.20).** For (8.13), $`-g_1g_2\chi_0=-2ng_1g_2K_F^{-1}(x_1,x_2)`$ with $`K_F=C_1+(2Dt_f+\Delta)\mathbb 1`$. At $`n=1`$ this is the form of the leading term $`-2g_1g_2K^{-1}`$ of (4.20), with $`(\Delta+2t_f,t_f)`$ in place of $`(\Delta,J)`$, and $`\Delta>0`$ corresponds to $`\Delta>2J`$. The dimensions match: $`[\chi_0]=[\phi]^2/[\text{cost}]`$, the same as $`n\bar\phi^2\mathcal G_A`$. Passed.

## Open issues

- The members of class F in the complement of $`U`$ are not classified, as the question's dated note allows: degenerate, quartic or multiple minima (for $`r\ge2`$), $`\bar\phi=0`$ with $`k_0\neq0`$, and $`\bar\phi=0`$, $`C=cA`$ in $`D=2,3`$, where higher orders of (8.9) decide. (Z) is only sufficient.
- The made field is the finite-$`L`$ Taylor coefficient. Its convergence radius $`\Delta_L/(2N_f\lVert\phi\rVert)`$ shrinks as $`L^{-2}`$ on G1, and no statement uniform in $`L`$ beyond $`\chi_0`$ is derived.
- Item 1 is derived at first order in $`\gamma`$, at the band point $`p=0`$ and at first order in the gradients. At order $`\gamma^2`$, $`b`$ and $`h_2`$ enter the fall ((8.3) for $`C_{\rm eff}`$), but that order also needs the body's own change of the field, which is not treated. The band point $`p=\pi`$ is not treated. T3 (which profiles field states realize) is assumed for the field of 04-profile.
- "Exceptional" and "typical" refer to the Euclidean topology of the coefficient spaces of classes C and F. The language supplies no measure on descriptions.

## Code

- `code/v2/check_response.py` (role: check, item 2). One field object ($`N_f=1`$, $`n=1/\lvert X_f\rvert`$) of class F with $`r=2`$ and Bloch matrix $`h(k)=-2t\sum_\mu\cos k_\mu+\Delta\lvert2\rangle\langle2\rvert+\lambda\sin k_1\,\sigma_1`$, with $`t=1`$ and $`\Delta=1.5`$ ($`k_0=0`$). It computes $`\chi_0(x,x_s)`$ of (3.6) by full diagonalization of $`h`$ and compares it with (8.8), (8.10), (8.11) and (8.13). Members on rings $`L=40,80,160`$: long range ($`\lambda=0.5`$, $`\phi=\begin{pmatrix}1&0.3\\0.3&-0.5\end{pmatrix}`$, $`\bar\phi=1`$); $`\bar\phi=0`$ without a conserved sector ($`\lambda=0.5`$, $`\phi=\sigma_1`$); and the (Z) member (8.13) ($`\lambda=0`$, $`\phi=\sigma_1`$). On square tori $`L=20,32`$ (full diagonalization) and $`L=64`$ (through (8.8) only): the long-range member and the $`\bar\phi=0`$ member. It logs the maximal deviations over the distance windows quoted in Steps 10 and 11, against the lattice form of the leading term at the same $`L`$ and, for the $`\bar\phi=0`$ member, against its $`L\to\infty`$ value.
- Outputs:
  - `code/v2/output/check_log.txt`: all compared numbers;
  - `code/v2/output/chi_ring.csv`: $`\chi_0/(2n)`$ and $`\Omega(d)/(2n)`$ against $`d`$ on the rings, where $`\Omega(d)`$ is the max−min of $`\chi_0`$ over distances $`\ge d`$;
  - `code/v2/output/chi_torus.csv`: $`\chi_0/(2n)`$ along both axes of the tori, with the lattice form of the prediction;
  - `code/v2/output/decay.png`: $`\Omega(d)/(2n)`$ on the rings, and $`d^2(\chi_0(d)-\chi_0(\text{corner}))/(2n)`$ on the torus $`L=64`$.

## Methods used

- partial expectation (mean field) for a test body; level decomposition by functions of $`D`$
- local Bloch Hamiltonian; local $`\sigma_1`$ rotation; first-order gradient (semiclassical) band dynamics
- linear algebra of Pauli bases; dimension and codimension counting of linear subspaces
- Rayleigh–Schrödinger perturbation theory; second quantization for non-interacting identical objects
- Bloch decomposition; analytic perturbation of an isolated eigenvalue (convergence radius); Paley–Wiener (analyticity versus exponential decay)
- Fourier sum rule bounding the response by the decay; genericity in a coefficient space (implicit function theorem, Baire category theorem); Dirichlet simultaneous approximation
- Fourier transforms of homogeneous functions; anisotropic lattice Green functions
- numerical full diagonalization and FFT (check)
