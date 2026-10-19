# Typical or forced: couplings and field contracts of the made field

- **Subproject:** 06-ilang-source
- **Package:** 08-typical-or-forced
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-19

## Setup and assumptions

**Item 1.** One Model D body ($`M_k=m+d_k>0`$, $`d_k=2\pi k/(N\lambda_0)`$ the $`N`$ distinct eigenvalues of $`D`$) is coupled to the field of 04-profile by $`\gamma\sum_xQ_x\otimes\Phi_x`$, with $`Q_x`$ in class C (question). A real function of $`D`$ is the list of its $`N`$ values, written $`f_k:=f(d_k)`$, so class C $`\cong\mathbb R^{5N}`$. The inputs are (5.3)–(5.5) of 05-made-field-scale, (17.11) of 05-ilang-free-fall/17-typical-or-forced and (4.16) of 05-ilang-free-fall/04-branch-fall, as quoted in the question. Assumptions:
- **T1 (test body).** As in 05-made-field-scale, the body evolves under the partial expectation of the total contract in the field state, $`C_{\rm eff}=C_{\rm D}+\gamma\sum_xN_\varphi(x)Q_x+E_\varphi`$. Its own change of the field is neglected (first order in $`\gamma`$, A15). $`C_{\rm eff}`$ is used as it stands: the local value $`\gamma N_\varphi(x_0)`$ is not expanded, and $`M_k+\gamma f_kN_\varphi(x_0)>0`$.
- **T2 (fall).** The fall is the acceleration of a branch start at rest at the band point $`p=0`$, at first order in the gradients of $`N_\varphi`$ (the regime of (4.16)).
- **T3 (field states).** "Every field state" includes states with $`N_\varphi(x+1)\neq N_\varphi(x)`$ at any $`x`$, and slowly varying profiles with any local value $`N_0`$ in an interval and any small slope $`N'\neq0`$ (product states of field objects placed at chosen sites, and their superpositions).

**Item 2.** Class F as in the question; $`\phi_x:=\lvert x\rangle\langle x\rvert\otimes\phi`$ on one object, $`\Phi_x=\sum_j\phi_x^{(j)}`$. Translation invariance and finite range give $`h=\sum_a\sum_x\lvert x+a\rangle\langle x\rvert\otimes h_a`$ with finitely many $`r\times r`$ blocks $`h_a`$, and Hermitian Bloch matrices $`h(k)=\sum_ae^{-ik\cdot a}h_a`$ (trigonometric polynomials), with eigenvalues $`\epsilon_0(k)\le\epsilon_1(k)\le\dots`$ and eigenvectors $`w_\ell(k)`$. The inputs are (3.6), (4.4) and (4.20), as quoted. Assumptions:
- **F1 (lowest band).** Over the continuous zone, $`\min_{k,\ell}\epsilon_\ell(k)=:\epsilon_0`$ is attained only at one $`k_0`$ and only by $`\ell=0`$, with $`\epsilon_0(k_0+q)-\epsilon_0=q^{\mathsf T}Aq+O(q^3)`$, $`A>0`$. Moreover $`k_0\in\frac{2\pi}{L}\mathbb Z^D`$ for the sides $`L`$ considered. Write $`w_0:=w_0(k_0)`$ and $`\bar\phi:=\langle w_0\vert\phi\vert w_0\rangle`$. Then $`u_0=\lvert X_f\rvert^{-1/2}\sum_xe^{ik_0\cdot x}\lvert x\rangle\otimes w_0`$ is the unique lowest eigenvector of $`h`$, as class F requires.
- **F2 (state, limit).** The field state is the lowest state (M9, named). $`L\to\infty`$ is taken at fixed $`r,h,\phi`$ and fixed density $`n=N_f/\lvert X_f\rvert`$. Since $`\chi_0/(2n)`$ does not depend on $`N_f`$ (8.8), the range criterion is a property of $`(h,\phi)`$. Distances are graph distances on $`X_f`$.

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

(i) At $`p=0`$, $`\partial_pE_{k,\sigma}=\sigma d_1\partial_pd_1/\lvert\mathbf d_k\rvert`$, which gives the velocity in (8.3). It vanishes for every level in every state iff $`h_1=0`$.

(ii) Let $`h_1=0`$. On level $`k`$, the rotation $`U=\sum_x\lvert x\rangle\langle x\rvert\otimes e^{-i\theta_k(x)\sigma_1/2}`$ takes $`\mu_k\sigma_3+\gamma Nh_{2,k}\sigma_2`$ to $`\tilde\mu_k\sigma_3`$ for a suitable angle $`\theta_k(x)`$, where $`\tilde\mu_k:=(\mu_k^2+\gamma^2N^2h_{2,k}^2)^{1/2}`$. $`U`$ commutes with $`\sigma_1`$ and with every position reading. It turns the bond operator $`-i\sigma_1`$ into $`-i\sigma_1\cos\frac{\delta\theta}2-\sin\frac{\delta\theta}2\,\mathbb 1_2`$, with $`\delta\theta=\theta_k(x+1)-\theta_k(x)`$. The change of the $`\sigma_1`$ part is of second order in the gradients. The branch-diagonal hop is of first order, and its variation in $`x`$ is of second order. At first order, the rotated blocks therefore have the form of (4.16), with $`G_k=\tilde\mu_k'`$, $`\mathcal F_k=-v_k'`$ and the local hopping $`\tau_k`$:
```math
v_{k,\sigma}(0)=-\frac{\sigma\,\tau_k\,\gamma N_0\,h_{1,k}}{\lvert\mathbf d_k(0)\rvert};\qquad h_1=0:\quad a_{k,\sigma}(0)=-\frac{\tau_k^2}{\tilde\mu_k}\bigl(\sigma v_k'+\tilde\mu_k'\bigr)\Big|_{x_0}.\qquad\text{(8.3)}
```

### Step 4. Level-independent fall: the set $`\mathcal S_1`$

On (8.2) with $`\eta_1=0`$ we have $`\tilde\mu_k=M_k\,s(N)`$, with $`s(N):=[(1+\gamma\alpha N)^2+(\gamma\eta_2N)^2]^{1/2}`$, and $`v_k'=\gamma\beta M_kN'`$. In (8.3) the factor $`M_k`$ cancels, which gives the fall in (8.4). The fraction there vanishes identically in $`N_0`$ for both $`\sigma`$ iff $`\alpha=\beta=\eta_2=0`$. Otherwise it is nonzero for some $`\sigma`$ on an open set of $`N_0`$. Level independence then requires $`(1+\gamma b_kN_0)^2`$ to be independent of $`k`$ on an interval, i.e. $`b_k=b_0`$ (polynomial identity in $`N_0`$). With (i):
```math
\begin{aligned}
&\mathcal S_1=\bigl\{h_1=0,\ (f,g,h_2)=(\alpha,\beta,\eta_2)(m\mathbb 1_N+D),\ (\alpha,\beta,\eta_2)\neq0,\ b=b_0\mathbb 1_N\bigr\},\qquad\mathcal S_1^0=\{f=g=h_1=h_2=0\},\\
&a_{k,\sigma}(0)=-\tau^2(1+\gamma b_0N_0)^2\,\gamma N'\,\frac{\sigma\beta\,s(N_0)+\alpha(1+\gamma\alpha N_0)+\gamma\eta_2^2N_0}{s(N_0)^2}\quad\text{on }\mathcal S_1;\qquad a_{k,\sigma}(0)=0\ \text{on }\mathcal S_1^0 .
\end{aligned}\qquad\text{(8.4)}
```

### Step 5. Pure local scale $`\mathcal S_2`$ and the requirement

"The hopping changes by the same local factor as the on-site blocks" means two things: $`B_{x,k}-E_\varphi=\nu(x)M_k\sigma_3`$ with one function $`\nu`$, and $`\tau_{x,x+1;k}=\tau\frac12(\nu(x)+\nu(x+1))`$. By (8.1), the first holds in every state iff $`W_k=\alpha M_k\sigma_3`$ (then $`\nu=1+\gamma\alpha N`$), and the second iff $`b_k=\alpha`$. Define the body's own contract at $`x`$, $`C_{{\rm D},x}:=\Pi_xB+\frac12(A_x+A_{x-1})`$, so that $`\sum_xC_{{\rm D},x}=C_{\rm D}`$. The two conditions select the couplings $`Q_x=\alpha C_{{\rm D},x}`$. Also, $`\sum_xQ_x=\mathbb 1_X\otimes W(D)+A\,b(D)`$; its place-diagonal and off-diagonal parts equal those of $`\alpha C_{\rm D}=\alpha A+\mathbb 1_X\otimes\alpha\sigma_3(m+D)`$ iff $`W=\alpha\sigma_3(m+D)`$ and $`b=\alpha`$. Hence
```math
\mathcal S_2=\{Q_x=\alpha\,C_{{\rm D},x},\ \alpha\neq0\}=\Bigl\{\textstyle\sum_xQ_x=\alpha\,C_{\rm D},\ \alpha\neq0\Bigr\},\qquad C_{\rm eff}=\sum_x\nu(x)\,C_{{\rm D},x}+E_\varphi,\qquad a(0)=-\tau^2\gamma\alpha N'\,\nu(x_0),\qquad\text{(8.5)}
```
with $`\mathcal S_2\subset\mathcal S_1`$ ($`\beta=\eta_2=0`$, $`b_0=\alpha`$; the fall follows from (8.4)). The conditions of the larger sets can also be written with the terms of $`C_{\rm D}`$:
- (8.2): the on-site part of $`Q_x`$ is $`W_*\,\lvert\Pi_xB\rvert`$, with one branch operator $`W_*`$ for all levels, where $`\lvert\Pi_xB\rvert=\Pi_x\otimes\mathbb 1_2\otimes(m+D)`$ is the modulus of the body's own on-site term;
- (8.4) adds two conditions: $`W_*`$ has no part along $`\sigma_1`$, the branch operator of the motion term; and the bond part of $`Q_x`$ is $`b_0`$ times the body's own motion term at $`x`$.

### Step 6. Dimensions

Each set is described by linear conditions on $`(f,g,h_1,h_2,b)\in\mathbb R^{5N}`$:
```math
\dim\mathcal S_{\rm R3}=N+4,\qquad\dim\mathcal S_1=4\ (3\text{ for }\beta=0),\qquad\dim\mathcal S_1^0=N,\qquad\dim\mathcal S_2=1,\qquad\dim(\text{class C})=5N .\qquad\text{(8.6)}
```
Here $`\mathcal S_{\rm R3}`$ is the set (8.2). For $`N\ge2`$ the codimensions $`4N-4`$, $`5N-4`$, $`4N`$ and $`5N-1`$ are positive, so every set lies in a proper linear subspace.

### Step 7. Breaking at first order

Expand around $`P_0=\bigl((\alpha,\beta,0,0)(m+D),\,b_0\bigr)\in\mathcal S_1`$, which contains (a), (c) and $`\mathcal S_2`$. The deviation is $`(\delta f,\delta g,\delta h_1,\delta h_2,\delta b)`$. Write $`\nu_0:=1+\gamma\alpha N_0`$, $`\rho_0:=1+\gamma b_0N_0`$ and $`\delta W_k:=\delta f_k\sigma_3+\delta g_k\mathbb 1_2+\delta h_{1,k}\sigma_1+\delta h_{2,k}\sigma_2`$. The block difference follows exactly from (8.1). The rest velocity and the fall follow from (8.3) by expanding $`\mu_k=M_k\nu_0+\gamma N_0\delta f_k`$ and $`\tau_k^2=\tau^2(\rho_0^2+2\rho_0\gamma N_0\delta b_k)+\dots`$ ($`\delta h_2`$ enters $`\tilde\mu_k`$ only quadratically):
```math
\begin{aligned}
&B_{x+1,k}-B_{x,k}=M_k\,\gamma\Delta N(x)\,W_*+\gamma\Delta N(x)\,\delta W_k,\qquad v_{k,\sigma}(0)=-\sigma\tau\,\frac{\rho_0}{\nu_0}\,\gamma N_0\,\frac{\delta h_{1,k}}{M_k},\\
&a_{k,\sigma}(0)=-\tau^2\gamma N'\Bigl[\frac{\rho_0^2(\alpha+\sigma\beta)}{\nu_0}+\frac{\rho_0^2}{\nu_0^2}\,\frac{(1-\sigma\beta\gamma N_0)\,\delta f_k+\sigma\nu_0\,\delta g_k}{M_k}+\frac{2\rho_0\gamma N_0(\alpha+\sigma\beta)}{\nu_0}\,\delta b_k\Bigr].
\end{aligned}\qquad\text{(8.7)}
```

### Step 8. Response in class F

Without pair terms, $`C_f=\sum_jh^{(j)}`$. On the symmetric space ($`c=+1`$), its lowest state is $`\varphi_0=u_0^{\otimes N_f}`$, unique by F1. $`\Phi_x`$ is a sum of one-object operators, so $`\Phi_x\varphi_0`$ lies in the span of $`\varphi_0`$ and of the symmetrized states $`\varphi_{(n)}`$ with one object in an excited eigenvector $`u_n`$ of $`h`$. These have $`\langle\varphi_{(n)}\vert\Phi_x\vert\varphi_0\rangle=\sqrt{N_f}\langle u_n\vert\phi_x\vert u_0\rangle`$ and cost $`\epsilon_n-\epsilon_0>0`$. Inserted in (3.6), with Bloch eigenvectors $`u_{k\ell}=\lvert X_f\rvert^{-1/2}\sum_xe^{ik\cdot x}\lvert x\rangle\otimes w_\ell(k)`$ and $`\langle u_0\vert\phi_x\vert u_{k\ell}\rangle=\lvert X_f\rvert^{-1}e^{i(k-k_0)\cdot x}\langle w_0\vert\phi\vert w_\ell(k)\rangle`$, this gives, with $`q:=k-k_0`$ and $`d:=x-y`$:
```math
\chi_0(x,y)=\frac{2n}{\lvert X_f\rvert}\sum_{q}\cos(q\cdot d)\,S_L(q),\qquad S_L(q)=\sum_{\ell:\,(q,\ell)\neq(0,0)}\frac{\lvert\langle w_0\vert\phi\vert w_\ell(k_0+q)\rangle\rvert^2}{\epsilon_\ell(k_0+q)-\epsilon_0}=\bigl\langle w_0\big\vert\phi\,(h(k_0+q)-\epsilon_0)^{-1}\phi\big\vert w_0\bigr\rangle\ \ (q\neq0).\qquad\text{(8.8)}
```
The source $`g\Phi_{x_s}`$ moves the lowest state by $`-gQ_0\Phi_{x_s}\varphi_0`$ at first order. The made field is therefore $`N(y)=n\bar\phi-g\chi_0(y,x_s)+O(g^2)`$, where $`N_{\varphi_0}=N_f\langle u_0\vert\phi_y\vert u_0\rangle=n\bar\phi`$. The cross term of second-order perturbation theory gives the mutual cost of two sources, $`-g_1g_2\chi_0(x_1,x_2)`$. Summing (8.8) over $`y`$ gives $`\sum_y\chi_0(x,y)=2n\,S_L(0)`$. The code check confirms (8.8) against direct diagonalization (`check_log.txt`: deviation $`\le6\times10^{-12}`$ on rings and tori).

### Step 9. Singular part and the short-range criterion

By F1, $`h(k)-\epsilon_0`$ is invertible for real $`k\neq k_0`$, so $`S`$ is real-analytic on the torus minus $`q=0`$. Near $`k_0`$, $`\epsilon_0(k)`$ is an isolated simple eigenvalue, and its spectral projector $`P_0(k)`$ is analytic:
```math
S(q)=\frac{\lvert F(q)\rvert^2}{\epsilon_0(k_0+q)-\epsilon_0}+S_{\rm an}(q),\qquad\lvert F(q)\rvert^2:=\langle w_0\vert\phi P_0(k_0+q)\phi\vert w_0\rangle,\quad\lvert F(0)\rvert^2=\bar\phi^2,\qquad\text{(8.9)}
```
with $`\lvert F\rvert^2`$ and $`S_{\rm an}`$ analytic. The set of $`q`$ is symmetric, so only the even part $`S_{\rm e}(q)=\frac12(S(q)+S(-q))`$ enters (8.8). Suppose $`S_{\rm e}`$ extends analytically to $`q=0`$. Then its Fourier coefficients decay exponentially in the graph distance (shift each $`q_\mu`$ into the strip of analyticity). The finite sum (8.8) is the sum of their periodic images plus a $`d`$-independent term of order $`\lvert X_f\rvert^{-1}`$. Hence the differences of $`\chi_0(\cdot,x_s)`$ beyond distance $`d`$ are bounded by $`Ce^{-d/\xi}`$ uniformly in $`L`$: the field is short range. Otherwise the leading non-analytic homogeneous term of $`S_{\rm e}`$ at $`q=0`$ fixes the large-distance form (Steps 10–11).

### Step 10. $`\bar\phi\neq0`$: Coulomb-type long range

Now $`S_{\rm e}(q)=\bar\phi^2/(q^{\mathsf T}Aq)+[\text{even terms of degree }0]+\dots`$, because the terms of degree $`-1`$ are odd. The Fourier integral of $`1/(q^{\mathsf T}Aq)`$ is the Green function $`\mathcal G_A`$ of $`-\nabla^{\mathsf T}A\nabla`$ (standard, up to a constant for $`D=1,2`$). An even function of degree $`0`$ gives $`O(\lvert d\rvert^{-D})`$ for $`d\neq0`$. In $`D=1`$, $`S-\bar\phi^2/(Aq^2)`$ is analytic up to an odd term. In the limit F2:
```math
\begin{aligned}
&\chi_0(y,x_s)-\chi_0(y',x_s)=2n\bar\phi^2\bigl[\mathcal G_A(y-x_s)-\mathcal G_A(y'-x_s)\bigr]+R,\\
&\mathcal G_A(d)=-\frac{\lvert d\rvert}{2A}\ (D=1),\qquad-\frac{\ln(d^{\mathsf T}A^{-1}d)}{4\pi\sqrt{\det A}}\ (D=2),\qquad\frac{1}{4\pi\sqrt{\det A}\,(d^{\mathsf T}A^{-1}d)^{1/2}}\ (D=3),
\end{aligned}\qquad\text{(8.10)}
```
with $`R=O(e^{-\min(\lvert d\rvert,\lvert d'\rvert)/\xi})`$ for $`D=1`$ and $`R=O(\lvert d\rvert^{-D}+\lvert d'\rvert^{-D})`$ for $`D=2,3`$, where $`d=y-x_s`$ and $`d'=y'-x_s`$. Along an axis, $`\mathcal G_A(d)-\mathcal G_A(2d)`$ is proportional to $`d`$, $`\ln2`$ and $`1/d`$ respectively, which is not exponentially small, so the field is long range. The made field is $`N(y)-N(y')=-g\times`$(8.10).

On F1, $`w_0`$ and therefore $`\bar\phi`$ depend continuously on $`(h_a,\phi)`$, and $`\phi\to\phi+\epsilon\mathbb 1_r`$ shifts $`\bar\phi`$ by $`\epsilon`$ at fixed $`h`$. Hence $`\{\bar\phi\neq0\}`$ is open and dense in F1.

The code check confirms (8.10). On the rings, the differences match the lattice form of $`\bar\phi^2/(q^{\mathsf T}Aq)`$ to $`5\times10^{-5}`$, and the oscillation $`\Omega(L/4)`$ grows $`\propto L`$. On the tori they match to within 2%.

### Step 11. $`\bar\phi=0`$

Then $`\lvert F(q)\rvert^2=q^{\mathsf T}Cq+O(q^3)`$, with $`C:=\frac12\nabla_q\nabla_q^{\mathsf T}\lvert F\rvert^2\big|_0\ge0`$. In a smooth gauge $`F(q)=\mathbf c\cdot q+O(q^2)`$, so $`C=\mathrm{Re}\,\mathbf c\,\mathrm{Re}\,\mathbf c^{\mathsf T}+\mathrm{Im}\,\mathbf c\,\mathrm{Im}\,\mathbf c^{\mathsf T}`$ has rank $`\le2`$.

For $`D=1`$, write $`\lvert F\rvert^2=q^2v(q)`$ and $`\epsilon_0(k_0+q)-\epsilon_0=q^2u(q)`$ with $`v,u`$ analytic and $`u(0)=A>0`$. Then $`S`$ is analytic at $`0`$ and the field is short range (Step 9).

For $`D=2,3`$, the leading term of $`S_{\rm e}`$ is $`q^{\mathsf T}Cq/q^{\mathsf T}Aq`$, of degree 0; the next even term has degree 2. With $`q_\mu q_\nu\leftrightarrow-\partial_\mu\partial_\nu`$:
```math
\bar\phi=0,\ D=2,3:\qquad\chi_0(y,x_s)=-2n\sum_{\mu,\nu}C_{\mu\nu}\,\partial_\mu\partial_\nu\mathcal G_A(y-x_s)+c_L+O(\lvert y-x_s\rvert^{-D-1}),\qquad\text{(8.11)}
```
where $`c_L`$ does not depend on $`y`$. The leading term is homogeneous of degree $`-D`$. It vanishes for all $`d\neq0`$ iff $`q^{\mathsf T}Cq/q^{\mathsf T}Aq`$ is constant, i.e. $`C=cA`$; for $`D=3`$ the rank bound then forces $`C=0`$.

The code check confirms both cases. For the 1D member with $`\bar\phi=0`$ and no conserved sector, $`\lvert\chi_0(d)-\chi_0(L/2)\rvert`$ decays at rate $`1.03749`$, which equals the distance of the nearest complex zero of $`\det(h(k)-\epsilon_0)`$ from the real axis. For the 2D member of the same construction, $`d^2(\chi_0(d)-\chi_0(\text{corner}))/(2n)`$ is about $`-0.020`$ along axis 1 and $`+0.024`$ to $`+0.026`$ along axis 2 at $`d=8,10`$. This matches the lattice form of (8.11) to within 5% and the $`L\to\infty`$ values $`-0.0194`$ and $`+0.0233`$.

### Step 12. Conditions stated through the contract

(i) **Long range.** Every member of class F conserves the number of field objects, $`\sum_xn_x=N_f`$ with $`n_x:=\sum_j(\lvert x\rangle\langle x\rvert\otimes\mathbb 1_r)^{(j)}`$. This number is carried by a band that becomes gapless as $`L\to\infty`$ (F1). By Step 10 the Coulomb-type long range is present iff $`\Phi_x`$ carries the density of this conserved number in the lowest state:
```math
\bar\phi=\frac{\langle\varphi_0\vert\Phi_x\vert\varphi_0\rangle}{\langle\varphi_0\vert n_x\vert\varphi_0\rangle}\neq0\iff\lim_{q\to0}\frac{\lvert X_f\rvert}{\sqrt{N_f}}\,\bigl\lvert\langle\varphi_{q}\vert\Phi_x\vert\varphi_0\rangle\bigr\rvert=\lvert\bar\phi\rvert\neq0,\qquad\text{(8.12)}
```
where $`\varphi_q`$ is the lowest-band one-object excitation at momentum $`k_0+q`$; the right-hand form follows from $`\lvert\langle u_q\vert\phi_x\vert u_0\rangle\rvert=\lvert X_f\rvert^{-1}\lvert F(q)\rvert`$. The right-hand form does not change under $`\Phi_x\to\Phi_x+c\mathbb 1`$ (M6).

(ii) **Short range, sufficient condition (Z).** Suppose there is a Hermitian $`Z`$ on $`\mathbb C^r`$ with $`[h,\mathbb 1\otimes Z]=0`$, so that the charge $`\sum_jZ^{(j)}`$ is conserved by $`C_f`$. Suppose further that $`w_0`$ lies in an eigenspace of $`Z`$ with projector $`P_Z`$, and $`P_Z\phi P_Z=0`$ ($`\Phi_x`$ changes the charge). Then $`[h(k),Z]=0`$, by continuity $`w_0(k)\in P_Z`$ near $`k_0`$, and $`\phi w_0\in(1-P_Z)`$. Hence $`S(q)=\langle w_0\vert\phi(1-P_Z)(h(k_0+q)-\epsilon_0)^{-1}(1-P_Z)\phi\vert w_0\rangle`$. By F1, the bands of $`h(k)`$ on $`(1-P_Z)`$ stay above $`\epsilon_0`$ on the whole zone. So $`S`$ is analytic on the torus, and the field is short range in every $`D`$.

### Step 13. A short-range member

Take $`r=2`$, $`h=(C_1+2Dt_f)\otimes\mathbb 1_2+\Delta\,\mathbb 1\otimes\lvert2\rangle\langle2\rvert`$ with $`t_f,\Delta>0`$, and $`\phi=\sigma_1`$; (Z) holds with $`Z=\sigma_3`$. Then $`h(k)=\mathrm{diag}(t_f\omega(k),\,t_f\omega(k)+\Delta)`$, $`k_0=0`$, $`w_0=\lvert1\rangle`$, and F1 holds with $`A=t_f\mathbb 1`$. Moreover $`S_L(q)=1/(t_f\omega(q)+\Delta)`$ for every $`q`$, including $`q=0`$. The 1D lattice sum is standard:
```math
\chi_0(x,y)=\frac{2n}{\lvert X_f\rvert}\sum_q\frac{\cos(q\cdot d)}{t_f\omega(q)+\Delta};\qquad D=1:\ \chi_0=\frac{n}{t_f\sinh\kappa}\,\frac{\cosh\kappa(\frac L2-d)}{\sinh\frac{\kappa L}2},\quad\cosh\kappa=1+\frac{\Delta}{2t_f},\ 0\le d\le L.\qquad\text{(8.13)}
```
For every $`D`$, shifting each $`q_\mu`$ by $`\pm i\eta`$ with $`\cosh\eta<1+\Delta/(2Dt_f)`$ keeps $`\mathrm{Re}(t_f\omega+\Delta)>0`$. Hence $`\lvert\chi_0(x,y)\rvert\le C_\eta e^{-\eta\,\mathrm{dist}(x,y)}`$ uniformly in $`L`$. The code check confirms the 1D form to $`2\times10^{-13}`$.

## Result

Class C, test body (T1), every field state (T3); the fall at first order in the gradients (T2), exact in the local value $`\gamma N_\varphi(x_0)`$.
- **(8.1)** The effective level-$`k`$ blocks are $`B_{x,k}=M_k\sigma_3+\gamma N(x)W_k+E_\varphi`$ and $`\tau_{x,x+1;k}=\tau(1+\gamma b_k\bar N_x)`$.
- **(8.2)** R3 holds at every place in every field state iff $`(f,g,h_1,h_2)=(\alpha,\beta,\eta_1,\eta_2)(m\mathbb 1_N+D)`$, with $`b`$ free; then $`\Gamma(x)=\gamma\Delta N(x)W_*`$.
- **(8.3)** The start at $`p=0`$ has velocity $`v_{k,\sigma}(0)=-\sigma\tau_k\gamma N_0h_{1,k}/\lvert\mathbf d_k(0)\rvert`$, so it is at rest in every state iff $`h_1=0`$. For $`h_1=0`$ the fall is $`a_{k,\sigma}(0)=-\tau_k^2(\sigma v_k'+\tilde\mu_k')/\tilde\mu_k`$.
- **(8.4)** The couplings with R3 at every place and a fall from rest at $`p=0`$ that is level-independent on both branches in every field state form $`\mathcal S_1\cup\mathcal S_1^0`$. Here $`\mathcal S_1`$ is given by $`h_1=0`$, $`(f,g,h_2)=(\alpha,\beta,\eta_2)(m+D)\neq0`$ and $`b=b_0\mathbb 1_N`$, with the fall of (8.4). On $`\mathcal S_1^0`$ ($`f=g=h_1=h_2=0`$) the fall vanishes. The two branches fall alike iff $`\beta=0`$. Control: the rest-only coupling (r) lies outside $`\mathcal S_1`$.
- **(8.5)** The subset on which, in addition, the on-site blocks scale by one local factor $`\nu`$ and the hopping by $`\frac12(\nu(x)+\nu(x+1))`$ is $`\mathcal S_2=\{Q_x=\alpha C_{{\rm D},x}\}=\{\sum_xQ_x=\alpha C_{\rm D}\}`$, $`\alpha\neq0`$. On $`\mathcal S_2`$, $`C_{\rm eff}=\sum_x\nu(x)C_{{\rm D},x}+E_\varphi`$ and $`a(0)=-\tau^2\gamma\alpha N'\nu(x_0)`$. Coupling (a) lies in $`\mathcal S_1`$ but not in $`\mathcal S_2`$; coupling (c) lies in $`\mathcal S_2`$. The sets (8.2), $`\mathcal S_1`$ and $`\mathcal S_2`$ are selected by requirements written with the terms of $`C_{\rm D}`$ (Step 5); for $`\mathcal S_2`$ the requirement is that a uniform field rescales the body's own contract.
- **(8.6)** $`\dim\mathcal S_{\rm R3}=N+4`$, $`\dim\mathcal S_1=4`$ (3 with $`\beta=0`$), $`\dim\mathcal S_1^0=N`$, $`\dim\mathcal S_2=1`$, inside $`\dim(\text{class C})=5N`$. For $`N\ge2`$ every set lies in a proper linear subspace, so each is nowhere dense and of measure zero: exceptional, not typical. Every member of class C is admissible, so within class C the language does not select these couplings (M10).
- **(8.7)** At first order in a deviation from $`P_0\in\mathcal S_1`$ (with $`\eta_2=0`$), R3 breaks by $`\gamma\Delta N(x)\,\delta W_k`$; this defect is exact and is absent iff $`\delta W_k/M_k`$ is level-independent. The rest at $`p=0`$ breaks by $`v_{k,\sigma}(0)\propto\sigma\gamma N_0\delta h_{1,k}/M_k`$. The fall breaks through $`\delta f_k/M_k`$ and $`\delta g_k/M_k`$ (order $`\gamma N'`$) and through $`\delta b_k`$ (order $`\gamma^2N_0N'`$). $`\delta h_2`$ enters the fall only at second order.

Class F under F1, lowest state (F2); $`\chi_0`$ is exact at finite $`L`$, the made field is of first order in the source coupling $`g`$, and the large-distance forms hold as $`L\to\infty`$ at fixed $`n`$.
- **(8.8)** $`\chi_0(x,y)=\frac{2n}{\lvert X_f\rvert}\sum_q\cos(q\cdot d)S_L(q)`$, with $`S_L(q)=\langle w_0\vert\phi(h(k_0+q)-\epsilon_0)^{-1}\phi\vert w_0\rangle`$ for $`q\neq0`$. The made field is $`N(y)=n\bar\phi-g\chi_0(y,x_s)+O(g^2)`$.
- **(8.9)** $`S=\lvert F\rvert^2/(\epsilon_0(k_0+q)-\epsilon_0)+S_{\rm an}`$, and the field is short range whenever the even part of $`S`$ is analytic at $`q=0`$.
- **(8.10)** If $`\bar\phi\neq0`$, the field is long range: $`\chi_0(y,x_s)-\chi_0(y',x_s)=2n\bar\phi^2[\mathcal G_A(y-x_s)-\mathcal G_A(y'-x_s)]+R`$, which is linear in $`D=1`$, logarithmic in $`D=2`$ and $`1/\lvert d\rvert`$ in $`D=3`$. $`\{\bar\phi\neq0\}`$ is open and dense in F1, so long range is typical. For $`r=1`$ every member with $`\phi\neq0`$ is long range.
- **(8.11)** If $`\bar\phi=0`$: in $`D=1`$ the field is short range. In $`D=2,3`$, $`\chi_0=-2n\sum C_{\mu\nu}\partial_\mu\partial_\nu\mathcal G_A+c_L+O(\lvert d\rvert^{-D-1})`$, a power law $`\lvert d\rvert^{-D}`$ (long range) unless $`C=cA`$ (for $`D=3`$: $`C=0`$). Short range is therefore confined to the closed set $`\{\bar\phi=0\}`$, which has empty interior: in $`D=1`$ it fills this set, and in $`D=2,3`$ it requires in addition $`C=cA`$.
- **(8.12)** The condition that selects the Coulomb-type long range is that $`\Phi_x`$ carries the density of the conserved number of field objects, whose band is gapless: $`\bar\phi\neq0`$, in the M6-invariant form (8.12). A sufficient condition for short range in every $`D`$ is (Z): a conserved charge $`\sum_jZ^{(j)}`$ that $`\Phi_x`$ changes within the sector of the lowest state, with the other sectors gapped.
- **(8.13)** A short-range member of class F exists: $`r=2`$, $`h=(C_1+2Dt_f)\otimes\mathbb 1_2+\Delta\,\mathbb 1\otimes\lvert2\rangle\langle2\rvert`$, $`\phi=\sigma_1`$, $`\Delta,t_f>0`$. It has the exact form (8.13) and $`\lvert\chi_0\rvert\le C_\eta e^{-\eta\,\mathrm{dist}}`$ uniformly in $`L`$ for $`\cosh\eta<1+\Delta/(2Dt_f)`$. Controls: this member for the long-range statement (8.10); the members with $`\bar\phi\neq0`$ for the short-range statements (8.11)–(8.12).

## Consistency checks

1. **Couplings (a), (c), (r) and dimensions.** (8.1) reproduces (5.3) for (a) and (c). Coupling (a) is $`\alpha=1`$, $`b_0=0`$; (8.4) gives $`a=-\tau^2\gamma N'/\nu(x_0)`$, which is also what (4.16) gives with (5.3). Coupling (c) is $`\alpha=b_0=1\in\mathcal S_2`$, with $`a=-\tau^2\gamma N'\nu(x_0)`$. For (r), $`W_k/M_k=m\sigma_3/M_k`$ is level-dependent (not R3), in agreement with (5.5), and (8.3) gives exactly $`a=-\tau^2\gamma mN'/(M_k+\gamma mN_0)`$, which is (5.5). $`\gamma N`$ is dimensionless, and $`a`$ has the dimension of $`\tau^2`$. Passed.
2. **Class of 04-profile.** For $`r=1`$, $`\phi=1`$, $`h=C_1`$: $`k_0=0`$, $`\bar\phi=1`$, $`A=t_f\mathbb 1`$, and $`S_L(q)=1/(t_f\omega(q))`$ with $`S_L(0)=0`$. So (8.8) gives $`\chi_0=\frac{2n}{t_f}\Lambda^+`$, and the mutual cost $`-g_1g_2\chi_0`$ is (4.4), together with its sum rule $`\sum_y\chi_0=2nS_L(0)=0`$. (8.10) then gives $`2n\mathcal G_{\mathbb 1}/t_f`$. Passed.
3. **Short-range member against (4.20).** For (8.13), $`-g_1g_2\chi_0=-2ng_1g_2K_F^{-1}(x_1,x_2)`$ with $`K_F=C_1+(2Dt_f+\Delta)\mathbb 1`$. At $`n=1`$ this is the form of the leading term $`-2g_1g_2K^{-1}`$ of (4.20), with $`(\Delta+2t_f,t_f)`$ in place of $`(\Delta,J)`$, and $`\Delta>0`$ corresponds to $`\Delta>2J`$. The dimensions match: $`[\chi_0]=[\phi]^2/[\text{cost}]`$, the same as $`n\bar\phi^2\mathcal G_A`$. Passed.

## Open issues

- Members of class F outside F1 are not treated: a minimum at a momentum incommensurate with $`L`$, a degenerate or quartic minimum, several minimizers. A quartic minimum with $`\bar\phi=0`$ could be long range even in $`D=1`$.
- In $`D=2,3`$, short range on $`\{\bar\phi=0,\ C=cA\}`$ is decided by higher orders of (8.9), which are not characterized here; (Z) is sufficient only.
- Item 1 is derived at the band point $`p=0`$ and at first order in the gradients. The second-order effects of $`h_1,h_2`$ and the band point $`p=\pi`$ are not treated. T3 (which profiles field states realize) is assumed for the field of 04-profile.
- "Exceptional" and "typical" refer to the natural parametrizations of classes C and F (coefficients $`f_k,\dots`$; blocks $`h_a`$, $`\phi`$). The language supplies no measure on descriptions.

## Code

- `code/v1/check_response.py` (role: check, item 2). One field object ($`N_f=1`$, $`n=1/\lvert X_f\rvert`$) of class F with $`r=2`$ and Bloch matrix $`h(k)=-2t\sum_\mu\cos k_\mu+\Delta\lvert2\rangle\langle2\rvert+\lambda\sin k_1\,\sigma_1`$, with $`t=1`$ and $`\Delta=1.5`$. It computes $`\chi_0(x,x_s)`$ of (3.6) by full diagonalization of $`h`$ and compares it with (8.8), (8.10), (8.11) and (8.13). Members on rings $`L=40,80,160`$: long range ($`\lambda=0.5`$, $`\phi=\begin{pmatrix}1&0.3\\0.3&-0.5\end{pmatrix}`$, $`\bar\phi=1`$); $`\bar\phi=0`$ without a conserved sector ($`\lambda=0.5`$, $`\phi=\sigma_1`$); and the (Z) member (8.13) ($`\lambda=0`$, $`\phi=\sigma_1`$). On square tori $`L=20,32`$: the long-range member and the $`\bar\phi=0`$ member.
- Outputs:
  - `code/v1/output/check_log.txt`: all compared numbers;
  - `code/v1/output/chi_ring.csv`: $`\chi_0/(2n)`$ and $`\Omega(d)/(2n)`$ against $`d`$ on the rings, where $`\Omega(d)`$ is the max−min of $`\chi_0`$ over distances $`\ge d`$;
  - `code/v1/output/chi_torus.csv`: $`\chi_0/(2n)`$ along both axes of the tori, with the lattice form of the prediction;
  - `code/v1/output/decay.png`: $`\Omega(d)/(2n)`$ on the rings, and $`d^2(\chi_0(d)-\chi_0(\text{corner}))/(2n)`$ on the torus.

## Methods used

- partial expectation (mean field) for a test body; level decomposition by functions of $`D`$
- local Bloch Hamiltonian; local $`\sigma_1`$ rotation; first-order gradient (semiclassical) band dynamics
- linear algebra of Pauli bases; dimension and codimension counting of linear subspaces
- Rayleigh–Schrödinger perturbation theory; second quantization for non-interacting identical objects
- Bloch decomposition; analytic perturbation of an isolated eigenvalue; Paley–Wiener (analyticity versus exponential decay)
- Fourier transforms of homogeneous functions; anisotropic lattice Green functions
- numerical full diagonalization and FFT (check)
