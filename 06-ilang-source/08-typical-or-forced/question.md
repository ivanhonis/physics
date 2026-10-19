# Question: 08-typical-or-forced

- **Subproject:** 06-ilang-source
- **Package:** 08-typical-or-forced
- **Equation tags:** (8.k)
- **Created:** 2026-10-19

## Goal

Determine how special the couplings and the field contracts are that give the results of items 3 and 4 of the base problem: the long-range made field (04-profile) and the made field as a common local scale (05-made-field-scale). This is item 8 of the base problem; the part on the field state (the sign as a condition on the state) is settled by 03-held-sources and is out of scope. Every result is stated through quantities that the total contract and the state fix (M6).

**Class C (couplings).** One Model D body (base problem, "Notation and conventions"; $`M_k:=m+d_k`$) coupled to a field of the class of 04-profile by a pair term linear in the $`\Phi_x`$, $`\gamma\sum_xQ_x\otimes\Phi_x`$, with
```math
Q_x=\Pi_x\bigl[\sigma_3\otimes f(D)+\mathbb 1_2\otimes g(D)+\sigma_1\otimes h_1(D)+\sigma_2\otimes h_2(D)\bigr]+\tfrac12\bigl(A_x+A_{x-1}\bigr)\bigl(\mathbb 1_2\otimes b(D)\bigr),
```
$`f,g,h_1,h_2,b`$ real functions on the spectrum of $`D`$ ($`\Pi_x`$, $`A_x`$ as under "Inputs"). Couplings (a) and (c) of 05-made-field-scale are $`f(D)=m\mathbb 1_N+D`$, $`g=h_1=h_2=0`$, with $`b=0`$ and $`b=1`$; the rest-only coupling of (5.5) is $`f=m\mathbb 1_N`$. The test body in a field state with expectations $`N_\varphi(x)`$, as in 05-made-field-scale.

**Class F (field contracts).** $`N_f\ge1`$ identical field objects ($`c=+1`$) without pair terms among them; each object has the places $`X_f\times\{1,\dots,r\}`$, $`X_f`$ a ring, square torus or cubic torus of side $`L`$, $`r\ge1`$ internal places per site; its own contract $`h`$ is Hermitian, invariant under the translations of $`X_f`$, of finite range, with a unique lowest eigenvector; the coupled operator is $`\Phi_x=\sum_j(\lvert x\rangle\langle x\rvert\otimes\phi)^{(j)}`$ with one Hermitian $`r\times r`$ matrix $`\phi`$; field state the lowest state. The class of 04-profile is $`r=1`$, $`\phi=1`$, $`h=C_1`$.

1. **Couplings.** In class C: determine the set of couplings for which, in every field state, the effective on-site blocks of the test body satisfy R3 at every place and the fall from rest at the band point $`p=0`$ is the same for all levels and both branches, and the subset for which in addition the hopping changes by the same local factor as the on-site blocks. State the dimension of these sets within class C (or the number of conditions), whether they are selected by a requirement that can be stated through the body's own contract (a condition on $`Q_x`$ written with the terms of $`C_{\rm D}`$), and how R3 and the level independence of the fall break at first order in a small deviation from them.
2. **Field contracts.** In class F: determine for which members the made field of one held source, at second order in its coupling (the response $`\chi_0`$ of (3.6) in the lowest state), is long range — its differences $`N(y)-N(y')`$ between places at graph distance at least $`d`$ from $`x_s`$ are not bounded by $`Ce^{-d/\xi}`$ uniformly in $`L`$ — and its leading form at large distance; whether long range holds on an open dense subset of class F or only on an exceptional one; and a condition on $`(h,\phi)`$ that can be stated through the contract (for example through a conserved quantity or the spectrum of $`h`$) and selects it. Give a member of class F with a short-range made field, or show that there is none.

**Note (2026-10-19, after external round 1).** Item 1 is asked at first order in $`\gamma`$ (Assumptions); a result kept exact in $`\gamma N_\varphi`$ may be added, distinguished from the first-order answer. In item 1, "the same for all levels and both branches" means equal values across levels and across the two branches. Item 2 is restricted: it asks for a subset of class F, open and dense in class F with a stated coefficient topology, on which the condition decides long or short range, and for the complement to be shown exceptional (closed with empty interior); a classification of the members inside that exceptional complement (for example degenerate or quartic band minima, or the cases left by the leading order of the response) is not asked. Reason: item 8 of the base problem needs whether long range is typical and what selects it, not a complete map of the exceptional members.

## Inputs

From 03-held-sources@v4 (this subproject). Setting there: a field object with contract $`C_f`$ (eigenvectors $`\varphi_n`$, eigenvalues $`e_n`$) and operators $`\Phi_x`$.

Eq. (3.6) of 03-held-sources:

```math
Q_n=\sum_{m:\,e_m\neq e_n}\frac{\lvert\varphi_m\rangle\langle\varphi_m\rvert}{e_m-e_n},\qquad
\chi_n(x,y)=\langle\varphi_n\vert\Phi_xQ_n\Phi_y+\Phi_yQ_n\Phi_x\vert\varphi_n\rangle
=\sum_{m:\,e_m\neq e_n}\frac{2\mathrm{Re}\bigl(\langle\varphi_n\vert\Phi_x\vert\varphi_m\rangle\langle\varphi_m\vert\Phi_y\vert\varphi_n\rangle\bigr)}{e_m-e_n}.
```

From 04-profile@v4 (this subproject). Setting there: the class of 04-profile ($`r=1`$, $`\phi=1`$, $`h=C_1=-t_f\sum_{\{x,y\}}(\lvert x\rangle\langle y\rvert+\lvert y\rangle\langle x\rvert)`$), two held sources $`g_i\Phi_{x_i}`$, lowest state, $`n=N_f/\lvert X_f\rvert`$; $`M`$ the mutual cost of the two sources.

Eq. (4.4) of 04-profile:

```math
M^{(2)}(x_1,x_2)=-\frac{2n\,g_1g_2}{t_f}\,\Lambda^+(x_1,x_2),\qquad \Lambda^+(x,y)=\frac1{\lvert X_f\rvert}\sum_{\mathbf k\neq0}\frac{e^{i\mathbf k\cdot(x-y)}}{\omega(\mathbf k)},\quad \omega(\mathbf k)=\sum_{\mu=1}^{D}4\sin^2\frac{k_\mu}2,\qquad \sum_{x_2\in X_f}M^{(2)}(x_1,x_2)=0,\qquad\text{(4.4)}
```

Setting of (4.20) (control field of 04-profile, outside class F): one field object with the places $`\{0,1\}^{X_f}`$ on an open chain, own term $`C^{\rm cell}_f=\Delta\sum_yn_y-J\sum_y(\sigma^+_y\sigma^-_{y+1}+\sigma^-_y\sigma^+_{y+1})`$, $`\Delta>2J>0`$, $`\Phi_x=\sigma^x_x`$, lowest state, $`d=x_2-x_1`$; $`K`$ the one-particle matrix of the own term.

Eq. (4.20) of 04-profile:

```math
\lvert M^{\rm cell}(d)\rvert\le\frac{3\gamma_\rho}{2}\,\frac{\lvert g_1g_2\rvert}{r_1r_2}\Bigl(\frac J\rho\Bigr)^{d},\qquad J<\rho<\frac\Delta2,\ \ \gamma_\rho=\Delta-2\rho,\ \ \lvert g_i\rvert<r_i,\ \ r_1+r_2=\frac{\gamma_\rho}2;\qquad M^{\rm cell}=-2g_1g_2K^{-1}(x_1,x_2)+O(g^4).\qquad\text{(4.20)}
```

From 05-made-field-scale@v3 (this subproject). Setting there: a test body coupled by (a) or (c) to the field in a state $`\varphi`$ with $`N_\varphi(x)=\langle\varphi\vert\Phi_x\vert\varphi\rangle`$, $`\nu(x)=1+\gamma N_\varphi(x)`$; $`\Pi_x=\lvert x\rangle\langle x\rvert\otimes\mathbb 1_2\otimes\mathbb 1_N`$, $`A_x`$ the bond $`(x,x+1)`$ of the motion term of Model D; $`B_{x,k}`$ the effective on-site block of level $`k`$ at $`x`$ (the level-$`k`$ on-site operator of the partial expectation of the total contract minus its field-independent scalar background), $`E_\varphi`$ a constant; $`\Delta N:=N_\varphi(x+1)-N_\varphi(x)`$; $`(r)`$ the rest-only coupling $`Q^{(r)}_x=\Pi_x\,\sigma_3\otimes m\mathbb 1_N`$; $`N'`$ the lattice slope.

Eq. (5.3) of 05-made-field-scale:

```math
\begin{aligned}
&B_{x,k}=M_{x,k}\sigma_3+V_{x,k}\mathbb 1_2,\qquad M_{x,k}=\nu(x)\,M_k,\qquad V_{x,k}=E_\varphi,\\
&\text{hopping on }(x,x+1):\ \tfrac{\tau_{x,x+1}}2(-i\sigma_1),\qquad \tau^{(a)}_{x,x+1}=\tau,\qquad \tau^{(c)}_{x,x+1}=\tau\,\tfrac12\bigl(\nu(x)+\nu(x+1)\bigr),
\end{aligned}
\qquad\text{(5.3)}
```

Eq. (5.4) of 05-made-field-scale:

```math
B_{x+1,k}-B_{x,k}=M_k\,\Gamma(x),\qquad \Gamma(x)=\gamma\bigl(N_\varphi(x+1)-N_\varphi(x)\bigr)\sigma_3 ;\qquad\text{for }\nu(x)\neq0:\ B_{x+1,k}-B_{x,k}=M_{x,k}\,\frac{\nu(x+1)-\nu(x)}{\nu(x)}\,\sigma_3 .
\qquad\text{(5.4)}
```

Eq. (5.5) of 05-made-field-scale:

```math
B^{(r)}_{x+1,k}-B^{(r)}_{x,k}=\gamma m\,\Delta N\,\sigma_3,\qquad a^{(r)}_{k,\sigma}(0)=-\tau^2\,\frac{\gamma m\,N'(x_0)}{M_k+\gamma mN_\varphi(x_0)} .
\qquad\text{(5.5)}
```

From 05-ilang-free-fall/17-typical-or-forced@v3. Setting there: one Model D body, linear level profiles $`M_{x,k}=M_k+G_kx`$, $`V_{x,k}=-\mathcal F_kx`$ with $`G_k=mg_m+d_kg_\eta`$, $`\mathcal F_k=\mathcal F+d_k\mathcal F_1`$; R3: with $`B_{x,k}:=M_{x,k}\sigma_3+V_{x,k}\mathbb 1_2`$ there is a level-independent operator $`\Gamma`$ on the branch label with $`B_{x+1,k}-B_{x,k}=M_k\Gamma`$ for every $`k`$; R3$`^+`$: $`E^+_{x+1,k}-E^+_{x,k}=\gamma_+M_k`$ with one real $`\gamma_+`$; the numbers $`\gamma`$, $`\phi`$ in (17.11) are the coefficients of $`\Gamma=\gamma\sigma_3-\phi\mathbb 1_2`$ there, not the coupling constant $`\gamma`$ of class C; $`\ell_+:=\mathcal F/m-g_m+g_\eta-\mathcal F_1`$; $`\mathcal U_4^{\pm}`$, $`\mathcal U_4^{+}`$, $`\mathcal U_5`$ the sets on which the fall from rest is level-independent on both branches, on the upper branch, and on which (4.24) holds with a nonzero fall.

Eq. (17.11) of 05-ilang-free-fall/17-typical-or-forced:

```math
\text{R3}\iff G_k=\gamma M_k,\ \mathcal F_k=\phi M_k\ \forall k\iff g_m=g_\eta=\gamma,\ \mathcal F_1=\phi,\ \mathcal F=m\phi\iff\boldsymbol g\in\mathcal U_4^{\pm};\qquad
\text{R3}^+\iff\ell_+=0\iff\boldsymbol g\in\mathcal U_4^{+},
```

From 05-ilang-free-fall/04-branch-fall@v3. Setting there: level blocks with linear level profiles $`M_{x,k}=M_k+G_kx`$, $`V_{x,k}=-\mathcal F_kx`$, hopping $`\tau_k\zeta_{x,k}`$; branch start at rest; first order in the gradients.

Eq. (4.16) of 05-ilang-free-fall/04-branch-fall:

```math
\boxed{\;a_{k,\sigma}(0)=\frac{\tau_k^2}{M_k}\,\bigl(\sigma\,\mathcal F_k-G_k\bigr)\;}
```

## Assumptions

- Classes C and F as under "Goal" are the classes studied (M8); the field state of item 1 is any state with expectations $`N_\varphi(x)`$, that of item 2 the lowest state (M9).
- Item 1 is at first order in $`\gamma`$ (test body); item 2 at second order in the source coupling.

## Scope

- **Class.** Item 1: class C, every field state, every place, every level, both branches. Item 2: class F, all three graph families, $`L\to\infty`$ at fixed $`r`$, $`h`$, $`\phi`$.
- **Control.** Item 2 asks for a short-range member of class F or a proof that there is none.
- Out of scope: the field state (03-held-sources); couplings nonlinear in $`\Phi_x`$ or not local; field objects with pair terms; orders beyond those stated.

## Depth

- Item 1: derive (needed by item 8 of the base problem: how special the couplings of item 4 are).
- Item 2: derive (needed by item 8 of the base problem: how special the field contracts of item 3 are).

## Expected result

- Item 1: a description of the sets by conditions on $`f,g,h_1,h_2,b`$, their dimension, a yes/no answer on the statable requirement with the requirement, and first-order breaking terms.
- Item 2: a condition on $`(h,\phi)`$ with the leading large-distance forms, a yes/no answer on typicality, and a short-range member or a proof that there is none.

Give every main result a tag $`(8.k)`$.

Consistency checks, at most three: for example couplings (a), (c) and (r) in item 1, the class of 04-profile in item 2.

## Code

Required: check: item 2, the response $`\chi_0(x,x_s)`$ of (3.6) for one object, for at least one long-range and one other member of class F with $`r=2`$ on rings of at least two sizes (and on one torus if cheap), and its decay with the distance.
