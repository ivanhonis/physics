# Grips within pair terms on the field of identical objects, and their weighing

- **Subproject:** 08-ilang-propagation
- **Package:** 03-gas-grip
- **Version:** v3
- **Mode:** internal regeneration
- **Date:** 2026-10-24

## Changes from previous version

- Setup, Inputs: the conditions of (4.12) from the dated note of question.md are added to the quoted (4.12) (review I1).
- Step 6, after (3.11): $`\kappa^{\rm mid}_{\rm ring}=0`$ is now stated at leading order in $`\eta`$ and for $`x_s`$ outside the arc between the bodies; the cubic-torus range is $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d\ll L`$; the square-torus range is the one stated with (4.12), $`d`$ large against $`\lvert\mathbf r\rvert`$ times a logarithm of $`L`$, replacing the range read off the $`O`$-bound (review I1).
- Step 6, "Mark and bond together": the same conditions are added to the cubic torus, the square torus and the ring (review I1).
- Result (3.11), Open issues (new item on the ring with $`x_s`$ between the bodies) and the twin follow.

## Setup and assumptions

**Description** (assumptions of the package, M8, M9, A11, A15, as fixed in question.md).
- *Field.* $`N_f\ge1`$ identical field objects ($`c=+1`$) without pair terms among them, each with the places $`X_f`$ of a ring ($`D=1`$), a square torus ($`D=2`$) or a cubic torus ($`D=3`$) of side $`L\ge3`$, $`\mathcal X=L^D`$. Own term of each object $`C_1=-t_f\sum_{\{x,y\}}(\lvert x\rangle\langle y\rvert+\lvert y\rangle\langle x\rvert)=t_f(\Lambda-2D\,\mathbb 1)`$, $`\Lambda`$ the graph Laplacian with the nonzero eigenvalues $`\lambda_k\ge\lambda_1>0`$. $`P^{(j)}_x`$ is the projector of field object $`j`$ on place $`x`$, $`\Phi_x=\sum_jP^{(j)}_x`$, $`n=N_f/\mathcal X`$; $`\Pi_f`$ projects onto the symmetric subspace of the field objects.
- *Body.* Held Model D ($`\tau=0`$). $`S=\sigma_3\otimes(m\mathbb 1_N+D)`$ has the eigenvalues $`\sigma M_k`$, $`\sigma=\pm1`$, $`M_k=m+2\pi k/(N\lambda_0)>0`$, all distinct. The grip term is
```math
G_F=\sum_x\lvert x\rangle\langle x\rvert\otimes S\otimes F(\Phi_x),
```
$`F`$ real on $`\{0,\dots,N_f\}`$, $`x`$ the field place of the body under the coupling map of the quoted packages; no other rest and clock term. Coupling (a) is $`F=1+\gamma\Phi`$, the full grip $`F=\gamma\Phi`$.
- *Source.* A held object at $`x_s`$, own eigenvalue $`c_s`$, pair term $`g_s\Phi_{x_s}`$; first order in $`g_s`$.
- *State.* The eigenvector of $`C`$ connected, as the couplings go to zero, to the bodies in eigenvectors of $`S`$ and every field object in its lowest one-object state.
- *Pair terms* (A5): operators acting on at most two objects, own terms included. "Sum of pair terms" means an operator identity on $`\mathcal H`$, or on $`\mathcal H_{\rm adm}`$ (both sides compressed by its projector $`\Pi`$).

**Inputs**, as quoted in question.md, with its notation ($`h_x`$, $`\varepsilon_0`$, $`\ell(y)=\Lambda^+(x,x+y)`$, $`\ell_0`$, $`\ell^{(j)}`$, $`r`$, $`r'`$, $`[f]`$, $`\delta N`$, $`\eta`$, $`T_2`$, $`\chi`$; for the bond $`\phi`$, $`\mathbf R`$, $`d`$, $`\Delta_{\mathbf e}`$, $`\Delta_{\mathbf r\mathbf r'}`$, $`W_b`$, $`K`$, $`\kappa`$, $`\rho_0`$). To avoid a clash with the grip function, the coefficients $`F,F_2,F_3`$ of (3.13)–(3.15) of 07-ilang-weight/03-weight-of-mark are written $`\Omega,\Omega_2,\Omega_3`$, and $`F_i`$ of (4.9) of 07-ilang-weight/04-weight-of-bond is written $`\mathcal F_i`$:
```math
\Omega:=-\frac{2g_s}{t_f}[\ell]=\frac{[\delta N]}{n}=\phi(x)-\phi(x').
```
- 07-ilang-weight/03-weight-of-mark@v2: (3.1) $`E_{k,\sigma}(x)=\theta\sigma M_k+c_s+N_f\varepsilon_0(x)`$; (3.4) $`\mathrm{Cost}_{k,\sigma}=\theta\sigma M_k+C^{\rm mark}_{k,\sigma}`$, $`C^{\rm mark}=N_f[\varepsilon_0(g_b)-\varepsilon_0(0)]=nt_f\eta(g_b)`$; (3.12)–(3.13) $`\Delta W_{k,\sigma}=\Omega C^{\rm mark}+\Omega_2(C^{\rm mark})^2+\Omega_3(C^{\rm mark})^3+O((C^{\rm mark})^4)+O(g_s^2)`$, $`\Omega_2=\frac{g_s}{nt_f^2}[\ell^2-\frac{2\ell^{(2)}}{\mathcal X}]`$; (3.14) full grip: $`\Delta W=\mathrm{Cost}\,\Omega\,[1+B^{\rm fg}]`$, $`B^{\rm fg}=-\frac\eta2[\ell(r)+\ell(r')-T_2]+O(\eta^2\ell^2)`$, $`\eta=\frac{\mathrm{Cost}}{nt_f}=\frac{g_b}{t_f}+O(g_b^2)`$; (3.15) coupling (a): $`\Delta W=\mathrm{Cost}\,F^{(a)}[1+B^{(a)}]`$, $`F^{(a)}=\frac{\gamma[\delta N]}{1+\gamma n}`$, $`B^{(a)}=-\frac{g_b}{2t_f}[\ell(r)+\ell(r')+\frac{2\ell_0}{1+\gamma n}-T_2]`$. Regime $`\chi=\lvert g_b\rvert\ell_0/t_f\ll1`$.
- 07-ilang-weight/04-weight-of-bond@v3: (4.2) bond cost $`B(\mathbf r)=-\frac{2ng_1g_2}{t_f}\ell(\mathbf r)`$; (4.9) $`\mathcal F_i=\phi`$ (full grip), $`\mathcal F_i=\frac{n\gamma_i}{1+n\gamma_i}\phi`$ (coupling (a)); (4.10) $`\rho_i=\frac{\Delta_{\mathbf e}\Delta_{\mathbf r\mathbf r'}W_b(x_1;\cdot)}{\Delta_{\mathbf r\mathbf r'}B\,\Delta_{\mathbf e}\mathcal F_i(x_1)}`$, $`\rho_i^{\rm fg}=\rho_0+O(\eta K)`$, $`\rho_0=1+\kappa`$; (4.12) $`\kappa^{\rm mid}_{D=3}=O(\frac{\lvert\mathbf r\rvert\lvert\mathbf r'\rvert}{d^2})`$, $`\kappa^{\rm mid}_{D=2}=O(\frac{\lvert\mathbf r'\rvert^2}{d^2}\ln\frac{L^2}{\lvert\mathbf r'\rvert d})`$, $`\kappa^{\rm mid}_{\rm ring}=0`$, with the conditions of the note of question.md: on the ring $`\kappa^{\rm mid}=0`$ at leading order in $`\eta`$ for $`x_s`$ outside the arc between the bodies; the ratio is 1 on the cubic torus for $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d\ll L`$, on the square torus only for $`d`$ large against $`\lvert\mathbf r\rvert`$ times a logarithm of $`L`$; (4.13) $`\rho_i^{(a)}=\frac{1+n\gamma_i}{n\gamma_i}\rho_i^{\rm fg}(1+O(\eta))`$. Regime $`\eta=\max_i\lvert g_i\rvert\ell_0/t_f<1/12`$, $`\gamma_i>0`$.

**Approximations.** First order in $`g_s`$; expansion in $`\chi`$ (mark) and $`\eta`$ (bond) at the orders stated with each result.

## Derivation

### Step 1. The grip as a sum of many-object terms

Newton's forward-difference formula on the finite set $`\{0,\dots,N_f\}`$ gives $`F(\nu)=\sum_{k=0}^{N_f}\binom\nu k\Delta^kF(0)`$ for every integer $`0\le\nu\le N_f`$, with $`\Delta^kF(0)=\sum_{i=0}^k(-1)^{k-i}\binom kiF(i)`$. The projectors $`P^{(j)}_x`$ commute and are diagonal in the joint places; on a joint place with $`\nu`$ objects at $`x`$, $`\Phi_x=\nu`$ and the elementary symmetric polynomial $`e_k(P^{(1)}_x,\dots,P^{(N_f)}_x)=\sum_{j_1<\dots<j_k}P^{(j_1)}_x\cdots P^{(j_k)}_x`$ equals $`\binom\nu k`$. Hence

```math
G_F=\sum_{k=0}^{N_f}\Delta^kF(0)\sum_x\lvert x\rangle\langle x\rvert\otimes S\otimes e_k\bigl(P^{(1)}_x,\dots,P^{(N_f)}_x\bigr),\qquad\text{(3.1)}
```

and its $`k`$-th term acts on the body and $`k`$ field objects together. If $`\Delta^kF(0)=0`$ for $`2\le k\le N_f`$, only the body term ($`k=0`$) and the pair terms ($`k=1`$) remain.

### Step 2. Only affine grips are sums of pair terms

Let $`N_f\ge2`$ and $`\Pi G_F\Pi=\Pi R\Pi`$, with $`R`$ a sum of pair terms between any objects of the description. On $`\mathcal H_{\rm adm}`$ the body is taken to be the only object of its type, so $`\Pi=\mathbb 1_b\otimes\Pi_f\otimes\Pi_O`$, $`O`$ the objects other than the body and the field; an identity on $`\mathcal H`$ implies this compressed one.

(a) Let $`e_\pm`$ be eigenvectors of $`S`$ with the eigenvalues $`\pm M_0=\pm m`$, and $`\mathcal D(X):=\langle x,e_+\rvert X\lvert x,e_+\rangle-\langle x,e_-\rvert X\lvert x,e_-\rangle`$ (partial matrix elements in the body places). $`\mathcal D`$ commutes with the compression by $`\Pi`$, and $`\mathcal D(G_F)=2M_0F(\Phi_x)`$. A term of $`R`$ that does not act on the body gives zero, a term on the body alone a number, a term of the body with field object $`j`$ an operator $`c_j`$ on object $`j`$, a term of the body with $`o\in O`$ an operator on $`o`$.
(b) The map $`X\mapsto\mathrm{Tr}_O(\Pi_OX\Pi_O)/\mathrm{Tr}\Pi_O`$ turns the last kind into numbers: $`2M_0\,\Pi_fF(\Phi_x)\Pi_f=\Pi_f\bigl(c_0+\sum_jc_j\bigr)\Pi_f`$, $`c_0`$ a number.
(c) Every permutation $`U`$ of the field objects has $`U\Pi_f=\Pi_f`$, so $`\Pi_f\sum_jc_j\Pi_f=\Pi_f\sum_j\bar c^{(j)}\Pi_f`$, with $`\bar c=N_f^{-1}\sum_ic_i`$ acting on object $`j`$.
(d) In the occupation basis $`\lvert\{n_y\}\rangle`$, $`\sum_yn_y=N_f`$, of the symmetric subspace the diagonal elements of $`\sum_j\bar c^{(j)}`$ are $`\sum_yn_y\bar c_{yy}`$ (standard), those of $`F(\Phi_x)`$ are $`F(n_x)`$. So $`2M_0F(n_x)=c_0+\sum_yn_y\bar c_{yy}`$ for every occupation.
(e) All objects at one place $`y\ne x`$: $`N_f\bar c_{yy}=2M_0F(0)-c_0`$, the same for every $`y\ne x`$. Then $`\nu`$ objects at $`x`$ and $`N_f-\nu`$ at one $`y\ne x`$: $`2M_0[F(\nu)-F(0)]=\nu(\bar c_{xx}-\bar c_{yy})`$ for $`0\le\nu\le N_f`$, so $`F`$ is affine.

With Step 1, for $`N_f\ge2`$:

```math
G_F\ \text{is a sum of pair terms}\iff\Delta^kF(0)=0\ \ (2\le k\le N_f)\iff F(\Phi)=\alpha+\beta\Phi,\qquad G_{\alpha,\beta}=\sum_{j=1}^{N_f}\sum_x\lvert x\rangle\langle x\rvert\otimes S\otimes\Bigl(\frac{\alpha}{N_f}\mathbb 1+\beta P^{(j)}_x\Bigr),\qquad\text{(3.2)}
```

with $`\alpha=F(0)`$, $`\beta=F(1)-F(0)`$. Since $`R`$ is arbitrary, adding, removing or moving listed pair terms (M6) does not make a grip with $`\Delta^kF(0)\ne0`$ for some $`k\ge2`$ a sum of pair terms. Control: $`F(\Phi)=\Phi^2`$ has $`\Delta^2F(0)=2`$; its term $`2\sum_x\lvert x\rangle\langle x\rvert\otimes S\otimes\sum_{i<j}P^{(i)}_xP^{(j)}_x`$ is a three-object term.

For $`N_f=1`$, $`\Phi_x=P_x`$ has the spectrum $`\{0,1\}`$, and every $`F`$ is affine there. For every $`N_f\ge1`$, $`G_{\alpha,\beta}`$ is the full grip $`\beta\Phi`$ together with the own term $`\alpha S`$ of the body (A5), so the two lists are one description (M6); coupling (a) is the full grip with the own term $`S`$. Two pairs $`(\alpha,\beta)\ne(\alpha',\beta')`$ give different $`C`$ on $`\mathcal H_{\rm adm}`$, since $`\Phi_x`$ takes the values $`0`$ and $`1`$ there:

```math
N_f=1:\ \ F(\Phi_x)=F(0)\,\mathbb 1+\bigl[F(1)-F(0)\bigr]\Phi_x\ \text{for every }F;\qquad N_f\ge1:\ \ G_{\alpha,\beta}=\alpha\sum_x\lvert x\rangle\langle x\rvert\otimes S+\beta\sum_x\lvert x\rangle\langle x\rvert\otimes S\otimes\Phi_x .\qquad\text{(3.3)}
```

### Step 3. Eigenvalue, cost and first-order part for an affine grip

All terms of the held body are $`S\otimes(\cdot)`$, so each eigenspace $`\sigma M_k`$ of $`S`$ is invariant, and $`G_{\alpha,\beta}`$ acts on it as $`\alpha\sigma M_k+g_b\Phi_x`$, $`g_b:=\sigma\beta M_k`$. On this sector $`C=\alpha\sigma M_k+c_s+\sum_jh_x^{(j)}`$, $`h_x=C_1+g_bP_x+g_sP_{x_s}`$ acting on object $`j`$. The lowest eigenvalue of $`h_x`$ is simple (Perron–Frobenius: connected graph, off-diagonal entries $`\le0`$), and the symmetric product of its eigenvectors is the stated state. As in (3.1), (3.4) of 07-ilang-weight/03-weight-of-mark, with $`\theta`$ replaced by $`\alpha`$:

```math
E_{k,\sigma}(x)=\alpha\sigma M_k+c_s+N_f\varepsilon_0(x),\qquad \mathrm{Cost}_{k,\sigma}=\alpha\sigma M_k+C^{\rm mark}_{k,\sigma},\qquad C^{\rm mark}_{k,\sigma}=N_f\bigl[\varepsilon_0(g_b)-\varepsilon_0(0)\bigr].\qquad\text{(3.4)}
```

$`\alpha`$ enters only through a constant that does not depend on the places; $`C^{\rm mark}`$ and every place dependence of $`E`$ are those of the full grip with $`\gamma=\beta`$.

The lowest eigenvector of $`C_1`$ is $`u=\mathcal X^{-1/2}\sum_y\lvert y\rangle`$, and $`C_1+2Dt_f=t_f\Lambda`$. Since $`\ell_0=\mathcal X^{-1}\sum_k\lambda_k^{-1}\ge(\mathcal X\lambda_1)^{-1}`$, $`\lvert g\rvert/\mathcal X\le\chi t_f\lambda_1`$, so for $`\chi\ll1`$ the shift stays far below the gap and the perturbation series of the simple eigenvalue applies: first order $`g\lvert u(x)\rvert^2=g/\mathcal X`$, second order $`-g^2\langle u\rvert P_x(t_f\Lambda)^+P_x\lvert u\rangle=-g^2\ell_0/(\mathcal Xt_f)`$, third order $`\frac{g^3}{\mathcal Xt_f^2}(\ell_0^2-\ell^{(2)}_0/\mathcal X)`$ with $`0\le\ell^{(2)}_0/\mathcal X\le\ell_0^2`$. With $`\chi_s:=g_b\ell_0/t_f`$ ($`\lvert\chi_s\rvert=\chi`$), $`C^{\rm mark}=ng_b[1-\chi_s+O(\chi^2)]`$. The parts of $`\mathrm{Cost}`$ and of $`\Delta W`$ linear in $`(\alpha,\beta)`$ follow from (3.4) and from (3.12)–(3.13) ($`\Omega C^{\rm mark}=\Omega ng_b+O(g_b^2)`$):

```math
\mathrm{Cost}^{(1)}_{k,\sigma}=\sigma M_k(\alpha+\beta n),\qquad \Delta W^{(1)}_{k,\sigma}=g_b[\delta N]=\mu\,\Omega\,\mathrm{Cost}^{(1)}_{k,\sigma},\qquad \mu:=\frac{\beta n}{\alpha+\beta n},\qquad C^{\rm self}_{k,\sigma}:=\mathrm{Cost}_{k,\sigma}-\mathrm{Cost}^{(1)}_{k,\sigma}=-ng_b\chi_s\bigl[1+O(\chi)\bigr].\qquad\text{(3.5)}
```

$`\mathrm{Cost}^{(1)}=\sigma M_kF(n)`$ is $`\sigma M_k\langle F(\Phi_x)\rangle`$ in the uncoupled field. The *mark fraction* $`\mu=ng_b/\mathrm{Cost}^{(1)}`$ does not depend on $`k`$ or $`\sigma`$, and $`\mu=1`$ iff $`\alpha=0`$. Excluded: $`\beta=0`$ (then $`g_b=0`$, no mark, $`\Delta W=0`$ for every level), $`\alpha+\beta n=0`$ ($`\mathrm{Cost}^{(1)}=0`$ for every level and both branches), and places with $`[\ell]=0`$ ($`\Omega=0`$).

### Step 4. Weight of the mark

By Step 3, $`\Delta W_{k,\sigma}`$ for $`(\alpha,\beta)`$ is that of the full grip with $`\gamma=\beta`$, which (3.14) of 07-ilang-weight/03-weight-of-mark gives as $`\Omega C^{\rm mark}(1+B^{\rm fg})`$, with $`\eta=C^{\rm mark}/(nt_f)`$; $`1+B^{\rm fg}:=\Delta W/(\Omega C^{\rm mark})`$. Inserting $`C^{\rm mark}=ng_b+C^{\rm self}=\mu\,\mathrm{Cost}^{(1)}+C^{\rm self}`$:

```math
\Delta W_{k,\sigma}=\Omega\,\bigl(1+B^{\rm fg}_{k,\sigma}\bigr)\bigl[\mu\,\mathrm{Cost}^{(1)}_{k,\sigma}+C^{\rm self}_{k,\sigma}\bigr].\qquad\text{(3.6)}
```

(3.6) is (3.14) of 07-ilang-weight/03-weight-of-mark rewritten with $`C^{\rm mark}=\mu\,\mathrm{Cost}^{(1)}+C^{\rm self}`$. At fixed $`\beta`$, $`\Delta W`$ does not depend on $`\alpha`$: the rest term $`\alpha\sigma M_k`$ is not weighed. The common factor of the two terms in (3.6) is an allocation, not the weight of the self-cost; that weight is derived in (3.13). Dividing by $`\mathrm{Cost}=\mathrm{Cost}^{(1)}+C^{\rm self}`$ with (3.5), $`\frac{\mu\mathrm{Cost}^{(1)}+C^{\rm self}}{\mathrm{Cost}^{(1)}+C^{\rm self}}=\mu\frac{1-\chi_s+O(\chi^2)}{1-\mu\chi_s+O(\mu\chi^2)}`$, so, with $`\epsilon:=(1+\lvert\mu\rvert)\chi+\lvert B^{\rm fg}\rvert`$,

```math
\Delta W_{k,\sigma}=\mathrm{Cost}_{k,\sigma}\,\mu\,\Omega\,\bigl[1+B^F_{k,\sigma}\bigr],\qquad B^F_{k,\sigma}=B^{\rm fg}_{k,\sigma}-(1-\mu)\chi_s+O(\epsilon^2)=-\frac{g_b}{2t_f}\Bigl[\ell(r)+\ell(r')+2(1-\mu)\ell_0-T_2\Bigr]+O(\eta^2\ell^2)+O(\epsilon^2),\qquad\text{(3.7)}
```

that is, the mark weighing ratio $`w_{k,\sigma}:=\frac{\Delta W_{k,\sigma}/\mathrm{Cost}_{k,\sigma}}{\Delta W^{(1)}_{k,\sigma}/\mathrm{Cost}^{(1)}_{k,\sigma}}=1+B^F_{k,\sigma}`$.

**Weight of the self-cost.** The weight of the first-order part is exactly $`\Delta W^{(1)}=\Omega ng_b`$ (3.5), so the weight that the self-cost carries is $`\Delta W-\Delta W^{(1)}`$. By (3.12)–(3.13) of 07-ilang-weight/03-weight-of-mark with $`C^{\rm mark}=ng_b+C^{\rm self}`$, $`C^{\rm self}=-ng_b^2\frac{\ell_0}{t_f}[1+O(\chi)]`$, it is $`\Omega C^{\rm self}+\Omega_2n^2g_b^2`$ up to terms with one more factor $`g_b/t_f`$ ($`\Omega_3n^3g_b^3`$, $`-2\chi_s\Omega_2n^2g_b^2`$, $`\Omega`$ times the cubic part of $`C^{\rm mark}`$); relative to $`\Omega C^{\rm self}`$ they are $`O(\chi)`$, their lattice-sum coefficients being of the size of $`\ell_0`$ on the three graphs (forms below). With $`[\ell^2]=[\ell]\,(\ell(r)+\ell(r'))`$, $`\Omega_2n^2g_b^2/(\Omega C^{\rm self})=\frac{[\ell^2]-2[\ell^{(2)}]/\mathcal X}{2\ell_0[\ell]}[1+O(\chi)]`$, and dividing by the weighing factor $`\mu\Omega`$ of the first-order part:

```math
w^{\rm self}_{k,\sigma}:=\frac{(\Delta W_{k,\sigma}-\Delta W^{(1)}_{k,\sigma})/C^{\rm self}_{k,\sigma}}{\Delta W^{(1)}_{k,\sigma}/\mathrm{Cost}^{(1)}_{k,\sigma}}=\frac{1+\zeta+O(\chi)}{\mu},\qquad \zeta:=\frac{\ell(r)+\ell(r')-T_2}{2\ell_0}.\qquad\text{(3.13)}
```

$`\zeta`$ depends on the graph and the two places, not on the grip, the level or the branch, and $`B^{\rm fg}=-\eta\ell_0\zeta+O(\eta^2\ell^2)`$. By definition $`B^F=(w^{\rm self}-1)\,C^{\rm self}/\mathrm{Cost}`$ exactly; with $`C^{\rm self}/\mathrm{Cost}=-\mu\chi_s[1+O(\epsilon)]`$ this is (3.7).

**$`\zeta`$ on the three graphs** (standard lattice sums). $`\ell^{(j)}(y)=\mathcal X^{-1}\sum_{k\ne0}\lambda_k^{-j}e^{ik\cdot y}`$, $`k\in\frac{2\pi}{L}\mathbb Z_L^D`$, $`\lambda_k=\sum_{i=1}^D(2-2\cos k_i)`$; $`\lvert y\rvert`$ is the length of the shortest representative.
- Ring: $`\ell(y)=\frac{L^2-1}{12L}-\frac{\varrho}{2L}`$, $`\varrho:=\lvert y\rvert(L-\lvert y\rvert)`$ (standard). Since $`\Lambda(\Lambda^+)^2=\Lambda^+`$, $`\ell^{(2)}`$ solves $`\Lambda\ell^{(2)}=\ell`$; the second difference of $`\varrho`$ is $`-2`$ and that of $`\varrho^2`$ is $`2L^2+2-12\varrho`$, so $`\ell^{(2)}=c-\frac{\varrho^2}{24L}-\frac{\varrho}{12L}`$, which also satisfies the equation at $`y=0`$, $`2[\ell^{(2)}(1)-\ell^{(2)}(0)]=-\ell_0`$. Hence $`T_2=\frac{\varrho+\varrho'+2}{6L}`$ exactly.
- Square torus, large $`L`$: $`\ell_0=\frac1{2\pi}\ln L+O(1)`$ and $`\ell_0-\ell(y)=\frac1{2\pi}\ln\lvert y\rvert+O(1)`$ for $`\lvert y\rvert\ge1`$ (potential kernel of the square lattice; the $`O(1)`$ includes the torus correction $`O(\lvert y\rvert^2/L^2)`$); $`\ell^{(2)}(0)-\ell^{(2)}(y)=\frac{\lvert y\rvert^2}{8\pi}\ln\frac{L}{\lvert y\rvert}+O(\lvert y\rvert^2)`$, so $`T_2=O(1)`$.
- Cubic torus: $`\ell_0=\ell_0^\infty+O(1/L)`$ with the finite $`\ell_0^\infty=(2\pi)^{-3}\int_{[-\pi,\pi]^3}\mathrm d^3k/\lambda(k)`$; $`\ell(y)=\frac1{4\pi\lvert y\rvert}+O(\lvert y\rvert^{-3})+O(1/L)`$; $`\ell^{(2)}(y)-\ell^{(2)}(0)=-\frac{\lvert y\rvert}{8\pi}+O(1)`$, so $`T_2=O(\lvert r\rvert\lvert r'\rvert/\mathcal X)=O(1/L)`$.

```math
\begin{aligned}\text{ring:}\quad&\zeta=1-\frac{2+4(\varrho+\varrho')}{L^2-1},\qquad\varrho=\lvert r\rvert(L-\lvert r\rvert),\ \ \varrho'=\lvert r'\rvert(L-\lvert r'\rvert)\qquad\text{(exact)};\\ \text{square torus:}\quad&\zeta=1-\frac{\ln(\lvert r\rvert\lvert r'\rvert)+O(1)}{4\pi\ell_0},\qquad 4\pi\ell_0=\ln L^2+O(1),\qquad \lvert r\rvert,\lvert r'\rvert\ge1;\\ \text{cubic torus:}\quad&\zeta=\frac{1}{8\pi\ell_0}\Bigl(\frac1{\lvert r\rvert}+\frac1{\lvert r'\rvert}\Bigr)+O\Bigl(\frac1{\lvert r\rvert^3}+\frac1{\lvert r'\rvert^3}+\frac1L\Bigr),\qquad \lvert r\rvert,\lvert r'\rvert\gg1.\end{aligned}\qquad\text{(3.14)}
```

So $`\zeta\to0`$ on the cubic torus as $`\min(\lvert r\rvert,\lvert r'\rvert)\to\infty`$. On the square torus $`\zeta\ll1`$ only where $`\ln\frac{L^2}{\lvert r\rvert\lvert r'\rvert}\ll\ln L`$ ($`\zeta=O(1/\ln L)`$ at distances of order $`L`$), and $`\zeta\to1`$ where $`\ln(\lvert r\rvert\lvert r'\rvert)/\ln L\to0`$. On the ring $`\zeta\ne0`$ at every pair of places ($`L^2-3`$ is not divisible by 4), $`\lvert\zeta\rvert\ll1`$ only near the curve $`4(\varrho+\varrho')=L^2`$, and $`\zeta=1-O((\lvert r\rvert+\lvert r'\rvert)/L)`$ for $`\lvert r\rvert,\lvert r'\rvert\ll L`$.

**Criterion.** By (3.13), $`\mu\,(w^{\rm self}-1)=1+\zeta-\mu+O(\chi)`$, with $`\mu`$ a constant of the grip and $`\zeta`$ a function of the places. Hence, at places with $`[\ell]\ne0`$:

```math
\text{(i)}\ \ w^{\rm self}_{k,\sigma}=1+O(\chi)\iff\mu=1+\zeta+O(\chi);\qquad\text{(ii)}\ \ \alpha=0:\ \ w^{\rm self}_{k,\sigma}=1+\zeta+O(\chi),\quad \Delta W_{k,\sigma}=\mathrm{Cost}_{k,\sigma}\,\Omega\,\bigl[1-\eta\ell_0\zeta+O(\eta^2\ell^2)\bigr].\qquad\text{(3.8)}
```

Where $`\zeta\to0`$, (i) is $`\mu=1`$, i.e. $`\alpha=F(0)=0`$; where $`\zeta\to1`$ (the ring for $`\lvert r\rvert,\lvert r'\rvert\ll L`$, the square torus for $`\ln(\lvert r\rvert\lvert r'\rvert)\ll\ln L`$) it is $`\mu=2`$, i.e. $`\alpha=-\beta n/2`$. By (3.14), at $`\alpha=0`$ the self-cost is weighed like the first-order part up to $`O(1/\min(\lvert r\rvert,\lvert r'\rvert))+O(\chi)`$ on the cubic torus; on the square torus only where $`\ln\frac{L^2}{\lvert r\rvert\lvert r'\rvert}\ll\ln L`$, up to $`O(1/\ln L)+O(\chi)`$ at distances of order $`L`$; on the ring only near the curve $`4(\varrho+\varrho')=L^2`$.

The leading factor $`\mu\Omega`$ of (3.7) is the same for all levels and both branches for every affine grip. Two bodies with grips $`(\alpha_i,\beta_i)`$ have the same leading factor iff $`\mu_1=\mu_2`$, i.e. $`\alpha_1\beta_2=\alpha_2\beta_1`$ (a condition, M7), which holds for all bodies with $`\alpha_i=0`$.

### Step 5. Level costs of one body

For two internal states $`a\ne a'`$ of one body, $`g_a\ne g_{a'}`$ (the $`M_k`$ are distinct and positive). The coefficients of $`\mathcal W`$ in (3.13) and of the series of $`C^{\rm mark}(g)`$ do not depend on the state, and $`\Omega_2n^2/(\Omega n)=-\frac1{2t_f}[\ell(r)+\ell(r')-T_2]`$. So $`\Delta W_a=\Omega n\,g_a[1-\frac{g_a}{t_f}(\ell_0+\frac12[\ell(r)+\ell(r')-T_2])]+O(\Omega ng_a\chi^2)`$ and $`\mathrm{Cost}_a=\frac{g_a}\beta(\alpha+\beta n)[1-\mu\frac{g_a\ell_0}{t_f}]+O(ng_a\chi^2)`$. The differences are proportional to $`g_a-g_{a'}`$, and their quotient gives

```math
\Delta W_a-\Delta W_{a'}=(\mathrm{Cost}_a-\mathrm{Cost}_{a'})\,\mu\,\Omega\Bigl[1-\frac{g_a+g_{a'}}{2t_f}\Bigl(\ell(r)+\ell(r')+2(1-\mu)\ell_0-T_2\Bigr)+O\bigl((1+\lvert\mu\rvert)^2\chi^2\bigr)\Bigr],\qquad\text{(3.9)}
```

with $`\chi`$ the larger of the two states. With $`\Omega=\phi(x)-\phi(x')`$ this is (4.9) of 07-ilang-weight/04-weight-of-bond with $`\mathcal F_i=\mu_i\phi`$, together with its relative remainder at first order. It involves only differences of costs of levels, which the total contract fixes (M6).

### Step 6. Weight of a bond

As in Step 3, the eigenvalue of the pair sector is $`\alpha_1\sigma_1M^{(1)}_{k_1}+\alpha_2\sigma_2M^{(2)}_{k_2}+c_s+N_f\varepsilon_0`$, $`\varepsilon_0`$ the lowest eigenvalue of $`C_1+g_1P_{x_1}+g_2P_{x_2}+g_sP_{x_s}`$, $`g_i=\sigma_i\beta_iM^{(i)}_{k_i}`$. The $`\alpha_i`$ add a constant that depends neither on $`x_1`$, nor on $`\mathbf r`$, nor on the source; so $`B(\mathbf r)`$ of (4.2), $`W_b`$ and the numerator of (4.10) are those of the full grips at the same $`g_1,g_2`$. The sector depends on the grips only through the $`g_i`$ and these constants, and every real $`g_i`$ is reached with $`\gamma_i>0`$ by the choice of $`\sigma_i`$; so (4.2), (4.10)–(4.12) hold for $`\beta_i`$ of either sign. With $`\mathcal F_i=\mu_i\phi`$ from (3.9) in the definition (4.10):

```math
\rho^F_i=\frac{\rho^{\rm fg}_i}{\mu_i}=\frac{\alpha_i+n\beta_i}{n\beta_i}\bigl[\rho_0+O(\eta K)\bigr],\qquad \rho^{{\rm mid},F}_i=\frac{\alpha_i+n\beta_i}{n\beta_i}\bigl[1+\kappa^{\rm mid}+O(\eta K)\bigr],\qquad\text{(3.10)}
```

with $`\kappa^{\rm mid}`$ of (4.12) on the three graphs. If the denominator uses the level factor of (3.9) with its remainder, the quotient changes by $`\bigl(1+\bar B^{\rm fg}_i\bigr)/\bigl(1+\bar B^F_i\bigr)=1+O\bigl((1+\lvert\mu_i\rvert)\eta\bigr)`$, the bracket of (3.9) at $`\mu_i=1`$ over that at $`\mu_i`$; this is the form of (4.13). The bond cost is weighed with $`\phi`$ times $`\rho^{\rm fg}_i`$, the first-order level costs of body $`i`$ with $`\mu_i\phi`$; for $`\rho^{\rm fg}_i\ne0`$:

```math
\text{(i)}\ \ \rho^F_i=\rho^{\rm fg}_i\iff\mu_i=1\iff\alpha_i=0;\qquad\text{(ii)}\ \ \alpha_i=0:\ \ \rho^{{\rm mid},F}_i-1=\kappa^{\rm mid}+O(\eta K).\qquad\text{(3.11)}
```

By (i), where $`\rho^{\rm fg}_i\to1`$ ($`\lvert\kappa\rvert`$, $`\eta K\ll1`$) the bond is weighed like the first-order level costs iff $`\alpha_i=0`$; for $`\alpha_i\ne0`$ it carries the extra factor $`1/\mu_i=1+\alpha_i/(n\beta_i)`$, the same at every separation, level and branch. By (4.12) with the conditions stated with it (note of question.md), the term $`\kappa^{\rm mid}`$ of (ii) is zero at leading order in $`\eta`$ on the ring for $`x_s`$ outside the arc between the bodies (for $`x_s`$ on that arc (4.12) gives no value); it is $`O(\lvert\mathbf r\rvert\lvert\mathbf r'\rvert/d^2)`$ on the cubic torus, small for $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d\ll L`$; and $`O(\frac{\lvert\mathbf r'\rvert^2}{d^2}\ln\frac{L^2}{\lvert\mathbf r'\rvert d})`$ on the square torus, small only for $`d`$ large against $`\lvert\mathbf r\rvert`$ times a logarithm of $`L`$.

**Mark and bond together.** Where $`\kappa^{\rm mid}`$ and $`\eta K`$ are small, the bond requires $`\mu_i=1`$ by (i), and then (3.8)(ii) leaves the self-cost of the mark with the factor $`1+\zeta`$. So both are weighed like the first-order part iff $`\alpha=0`$ and $`\zeta\ll1`$: on the cubic torus for $`1\ll\min(\lvert r\rvert,\lvert r'\rvert)`$ and $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d\ll L`$, by the grips $`F(\Phi)=\beta\Phi`$, $`\beta\ne0`$ of either sign; on the square torus by the same grips only where $`\ln\frac{L^2}{\lvert r\rvert\lvert r'\rvert}\ll\ln L`$ (up to $`O(1/\ln L)`$ at source distances of order $`L`$) and $`d`$ is large against $`\lvert\mathbf r\rvert`$ times a logarithm of $`L`$; on the ring, for $`x_s`$ outside the arc between the bodies, by no affine grip, except for pairs of places near the curve $`4(\varrho+\varrho')=L^2`$.

### Step 7. Control outside pair terms

$`F(\Phi)=\Phi^2`$ has $`F(0)=0`$ and, for $`N_f\ge2`$, is not a sum of pair terms (3.2). At first order in the grip the eigenvalue shift is $`\sigma M_k\langle\Phi_x^2\rangle`$ in the field state with the source, the product of $`N_f`$ copies of one vector $`\psi`$ with $`N_f\lvert\psi(y)\rvert^2=n+\delta N(y)`$. $`\Phi_x`$ is then binomial, $`\langle\Phi_x^2\rangle=N_fp+N_f(N_f-1)p^2`$, $`p=\lvert\psi(x)\rvert^2`$. With $`n':=(1-1/N_f)n`$:

```math
\mathrm{Cost}^{(1)}=\sigma M_k\,n(1+n'),\qquad \Delta W^{(1)}=\sigma M_k[\delta N](1+2n')+O(g_s^2),\qquad \frac{\Delta W^{(1)}}{\mathrm{Cost}^{(1)}}=\Omega\,\frac{1+2n'}{1+n'} .\qquad\text{(3.12)}
```

For $`N_f=1`$, $`n'=0`$ and the factor is 1, as it must be: $`\Phi_x^2=\Phi_x`$ is then the affine grip $`(0,1)`$ of (3.3), with $`\mu=1`$.

## Result

- **(3.1)** For every real $`F`$ on $`\{0,\dots,N_f\}`$ and every $`N_f\ge1`$, the grip term is the sum over $`k`$ of $`\Delta^kF(0)`$ times a term acting on the body and $`k`$ field objects together. Exact.
- **(3.2)** For $`N_f\ge2`$, $`G_F`$ is a sum of pair terms (on $`\mathcal H`$; on $`\mathcal H_{\rm adm}`$ when the body is the only object of its type) iff $`\Delta^kF(0)=0`$ for $`2\le k\le N_f`$, iff $`F(\Phi)=\alpha+\beta\Phi`$ on $`\{0,\dots,N_f\}`$; then $`G_{\alpha,\beta}`$ is a sum of $`N_f`$ pair terms between the body and single field objects. Adding or moving listed pair terms (M6) does not change this. Exact. Control: $`F=\Phi^2`$.
- **(3.3)** For $`N_f=1`$ every $`F`$ gives the pair term of the affine grip with $`\alpha=F(0)`$, $`\beta=F(1)-F(0)`$. For every $`N_f\ge1`$ the grips within pair terms are the affine grips $`(\alpha,\beta)`$, each the same description as the full grip $`\beta\Phi`$ with the own term $`\alpha S`$; different $`(\alpha,\beta)`$ give different $`C`$. Exact; a characterization, no control in the class.
- **(3.4)** For an affine grip, a held body and the stated state: $`E_{k,\sigma}=\alpha\sigma M_k+c_s+N_f\varepsilon_0(x)`$, $`\mathrm{Cost}_{k,\sigma}=\alpha\sigma M_k+C^{\rm mark}_{k,\sigma}`$, $`C^{\rm mark}`$ that of the full grip with $`\gamma=\beta`$, $`g_b=\sigma\beta M_k`$. Exact.
- **(3.5)** First-order part $`\mathrm{Cost}^{(1)}=\sigma M_k(\alpha+\beta n)`$, its weight $`\Delta W^{(1)}=\mu\Omega\,\mathrm{Cost}^{(1)}`$ (first order in $`g_s`$), mark fraction $`\mu=\beta n/(\alpha+\beta n)`$, the same for all levels and both branches, and self-cost $`C^{\rm self}=-ng_b\chi_s[1+O(\chi)]`$ for $`\chi\ll1`$. Excluded: $`\beta=0`$, $`\alpha+\beta n=0`$, $`[\ell]=0`$.
- **(3.6)** For every affine grip with $`\beta\ne0`$, $`\alpha+\beta n\ne0`$, every level and both branches, first order in $`g_s`$, regime $`\chi\ll1`$ of (3.14) of 07-ilang-weight/03-weight-of-mark: $`\Delta W=\Omega(1+B^{\rm fg})[\mu\,\mathrm{Cost}^{(1)}+C^{\rm self}]`$, a rewriting of that equation; at fixed $`\beta`$, $`\Delta W`$ does not depend on $`\alpha`$, so the rest term is not weighed. The common factor in front of $`C^{\rm self}`$ is an allocation, not the weight of the self-cost, which is (3.13). Control: (3.12).
- **(3.7)** Under the conditions of (3.6) and $`\lvert\mu\rvert\chi\ll1`$, on the three graphs: $`\Delta W=\mathrm{Cost}\,\mu\Omega[1+B^F]`$, and the mark weighing ratio is $`w=1+B^F`$, with the first breaking term $`B^F=-\frac{g_b}{2t_f}[\ell(r)+\ell(r')+2(1-\mu)\ell_0-T_2]`$ and remainder $`O(\eta^2\ell^2)+O(\epsilon^2)`$, $`\epsilon=(1+\lvert\mu\rvert)\chi+\lvert B^{\rm fg}\rvert`$.
- **(3.13)** Under the conditions of (3.6), at places with $`[\ell]\ne0`$: the self-cost carries the weight $`\Delta W-\Delta W^{(1)}`$, and its weighing ratio against the first-order part is $`w^{\rm self}=\mu^{-1}[1+\zeta+O(\chi)]`$, $`\zeta=(\ell(r)+\ell(r')-T_2)/(2\ell_0)`$; $`\zeta`$ is the same for every affine grip, level and branch, and $`B^F=(w^{\rm self}-1)C^{\rm self}/\mathrm{Cost}`$ exactly.
- **(3.14)** On the ring, exactly, $`\zeta=1-\frac{2+4(\varrho+\varrho')}{L^2-1}`$, $`\varrho=\lvert r\rvert(L-\lvert r\rvert)`$; on the square torus, large $`L`$, $`\zeta=1-\frac{\ln(\lvert r\rvert\lvert r'\rvert)+O(1)}{4\pi\ell_0}`$, $`4\pi\ell_0=\ln L^2+O(1)`$, for $`\lvert r\rvert,\lvert r'\rvert\ge1`$; on the cubic torus $`\zeta=\frac{1}{8\pi\ell_0}(\frac1{\lvert r\rvert}+\frac1{\lvert r'\rvert})+O(\lvert r\rvert^{-3}+\lvert r'\rvert^{-3}+L^{-1})`$ for $`\lvert r\rvert,\lvert r'\rvert\gg1`$. Thus $`\zeta\to0`$ on the cubic torus as $`\min(\lvert r\rvert,\lvert r'\rvert)\to\infty`$; on the square torus $`\zeta\ll1`$ only where $`\ln\frac{L^2}{\lvert r\rvert\lvert r'\rvert}\ll\ln L`$, and $`\zeta\to1`$ where $`\ln(\lvert r\rvert\lvert r'\rvert)/\ln L\to0`$; on the ring $`\zeta\ne0`$ at every pair of places, $`\lvert\zeta\rvert\ll1`$ only near the curve $`4(\varrho+\varrho')=L^2`$, and $`\zeta=1-O((\lvert r\rvert+\lvert r'\rvert)/L)`$ for $`\lvert r\rvert,\lvert r'\rvert\ll L`$.
- **(3.8)** Under the conditions of (3.13): (i) $`w^{\rm self}=1+O(\chi)`$ iff $`\mu=1+\zeta+O(\chi)`$; where $`\zeta\to0`$ this is $`\mu=1`$, i.e. $`\alpha=F(0)=0`$, and where $`\zeta\to1`$ (the ring for $`\lvert r\rvert,\lvert r'\rvert\ll L`$, the square torus for $`\ln(\lvert r\rvert\lvert r'\rvert)\ll\ln L`$) it is $`\mu=2`$, i.e. $`\alpha=-\beta n/2`$. (ii) For $`\alpha=0`$, every level and both branches: $`w^{\rm self}=1+\zeta+O(\chi)`$ and $`\Delta W=\mathrm{Cost}\,\Omega[1-\eta\ell_0\zeta+O(\eta^2\ell^2)]`$; the self-cost is weighed like the first-order part up to $`O(1/\min(\lvert r\rvert,\lvert r'\rvert))+O(\chi)`$ on the cubic torus, on the square torus only where $`\ln\frac{L^2}{\lvert r\rvert\lvert r'\rvert}\ll\ln L`$, up to $`O(1/\ln L)+O(\chi)`$ at distances of order $`L`$, and on the ring only near the curve $`4(\varrho+\varrho')=L^2`$. Two bodies have the same leading factor $`\mu\Omega`$ iff $`\alpha_1\beta_2=\alpha_2\beta_1`$ (a condition, M7). Control: coupling (a) for (i); the ring for (ii).
- **(3.9)** For two internal states of one body with an affine grip, at first order in $`g_s`$ and $`\chi\ll1`$, $`\lvert\mu\rvert\chi\ll1`$: the difference of weights is the difference of costs times $`\mu\Omega[1-\frac{g_a+g_{a'}}{2t_f}(\ell(r)+\ell(r')+2(1-\mu)\ell_0-T_2)+O((1+\lvert\mu\rvert)^2\chi^2)]`$; this is (4.9) of 07-ilang-weight/04-weight-of-bond with $`\mathcal F_i=\mu_i\phi`$.
- **(3.10)** For two held bodies with affine grips $`(\alpha_i,\beta_i)`$, $`\beta_i\ne0`$, $`\alpha_i+n\beta_i\ne0`$, either sign, every level and both branches, in the regime and on the three graphs of (4.10)–(4.12): $`\rho^F_i=\rho^{\rm fg}_i/\mu_i=\frac{\alpha_i+n\beta_i}{n\beta_i}[\rho_0+O(\eta K)]`$, and with the midpoint as the place of the pair $`\frac{\alpha_i+n\beta_i}{n\beta_i}[1+\kappa^{\rm mid}+O(\eta K)]`$, $`\kappa^{\rm mid}`$ of (4.12).
- **(3.11)** Under the conditions of (3.10) and $`\rho^{\rm fg}_i\ne0`$: (i) $`\rho^F_i=\rho^{\rm fg}_i`$ iff $`\alpha_i=0`$; where $`\lvert\kappa\rvert,\eta K\ll1`$ the bond is weighed like the first-order level costs iff $`\alpha_i=0`$, and for $`\alpha_i\ne0`$ it carries the extra factor $`1+\alpha_i/(n\beta_i)`$. (ii) For $`\alpha_i=0`$, $`\rho^{{\rm mid},F}_i-1=\kappa^{\rm mid}+O(\eta K)`$, with $`\kappa^{\rm mid}`$ of (4.12) under its conditions: zero at leading order in $`\eta`$ on the ring for $`x_s`$ outside the arc between the bodies; $`O(\lvert\mathbf r\rvert\lvert\mathbf r'\rvert/d^2)`$ on the cubic torus, small for $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d\ll L`$; $`O(\frac{\lvert\mathbf r'\rvert^2}{d^2}\ln\frac{L^2}{\lvert\mathbf r'\rvert d})`$ on the square torus, small only for $`d`$ large against $`\lvert\mathbf r\rvert`$ times a logarithm of $`L`$. Mark and bond together, where $`\kappa^{\rm mid}`$ and $`\eta K`$ are small: both are weighed like the first-order part iff $`\alpha=0`$ and $`\zeta\ll1`$, i.e. by $`F(\Phi)=\beta\Phi`$, $`\beta\ne0`$ of either sign, on the cubic torus for $`1\ll\min(\lvert r\rvert,\lvert r'\rvert)`$ and $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d\ll L`$; on the square torus by the same grips only where $`\ln\frac{L^2}{\lvert r\rvert\lvert r'\rvert}\ll\ln L`$ (up to $`O(1/\ln L)`$ at source distances of order $`L`$) and $`d`$ is large against $`\lvert\mathbf r\rvert`$ times a logarithm of $`L`$; on the ring, for $`x_s`$ outside the arc between the bodies, by no affine grip, except for pairs of places near the curve $`4(\varrho+\varrho')=L^2`$. Control: coupling (a); the ring.
- **(3.12)** Control outside pair terms: for $`F=\Phi^2`$ and $`N_f\ge2`$, first order in the grip and in $`g_s`$, the first-order part is weighed with $`\Omega(1+2n')/(1+n')`$, $`n'=(1-1/N_f)n`$, whose factor $`(1+2n')/(1+n')`$ lies strictly between 1 and 2 although $`F(0)=0`$.

## Consistency checks

1. Special grips: at $`\alpha=0`$, $`\mu=1`$ and (3.7), (3.9), (3.10) reduce to (3.14) of 07-ilang-weight/03-weight-of-mark and to (4.9), (4.10) of 07-ilang-weight/04-weight-of-bond for the full grip; at $`\alpha=1`$, $`\beta=\gamma`$, $`\mu\Omega=F^{(a)}`$, $`2(1-\mu)\ell_0=2\ell_0/(1+\gamma n)`$ gives $`B^F=B^{(a)}`$ of (3.15) exactly, $`\mu\phi`$ is (4.9) for coupling (a), and $`1/\mu`$ with the remainder factor of Step 6 is (4.13). Passed.
2. Dimensions: $`\alpha,\beta,\mu,\Omega,\chi,\zeta,T_2,B^F,w^{\rm self},\rho^F_i`$ are numbers ($`\ell^{(j)}`$ are entries of powers of the inverse of a graph Laplacian); $`g_b`$, $`\mathrm{Cost}`$, $`C^{\rm self}`$, $`\Delta W`$ and $`B(\mathbf r)`$ are costs ($`g_b^2\ell_0/t_f`$ and $`ng_1g_2\ell/t_f`$ included). Passed.
3. Ring $`L=3`$: $`\Lambda=3\cdot\mathbb 1-J`$ ($`J`$ the all-ones matrix) gives $`\Lambda^+=\frac13(\mathbb 1-J/3)`$, $`(\Lambda^+)^2=\frac19(\mathbb 1-J/3)`$; for $`\lvert r\rvert=0`$, $`\lvert r'\rvert=1`$: $`\ell_0=\frac29`$, $`\ell(1)=-\frac19`$, $`[\ell]=\frac13`$, $`[\ell^{(2)}]=\frac19`$, $`T_2=\frac29`$, $`\zeta=-\frac14`$, which (3.14) gives with $`\varrho=0`$, $`\varrho'=2`$. Passed.

## Open issues

- The size of $`O(\eta K)`$ of (4.10) on each graph is that of 07-ilang-weight/04-weight-of-bond; the $`O(\chi)`$ remainder of (3.13) and the $`O(1)`$ terms of (3.14) on the two tori are not evaluated.
- The bond criterion uses the midpoint as the place of the pair; with body 1 as the place its first breaking term is $`\kappa`$ of (4.10), on the ring $`\rho_0^{\rm ring}-1`$ of (4.12).
- On the ring with $`x_s`$ on the arc between the bodies, (4.12) gives no value of $`\kappa^{\rm mid}`$, and the joint criterion for mark and bond is not evaluated there.
- Grips outside pair terms ($`N_f\ge2`$, $`F`$ not affine) are characterized only by the first-order control (3.12); their marks and bonds are not studied.
- On $`\mathcal H_{\rm adm}`$, (3.2) assumes the body is the only object of its type; several identical bodies are treated only through the identity on $`\mathcal H`$.
- Grips with a different internal operator for each value of $`\Phi_x`$, field states other than the stated one, and fields of cells are outside the scope.

## Methods used

- Newton forward differences on a finite set; elementary symmetric polynomials of commuting projectors
- partial matrix elements and partial traces; symmetrization on the symmetric subspace, occupation basis
- Perron–Frobenius for the lowest one-object eigenvector; product eigenvectors of non-interacting identical objects
- Rayleigh–Schrödinger perturbation theory of a simple isolated eigenvalue; pseudo-inverse of the graph Laplacian
- lattice Green functions: exact sums on the ring (second-difference equation), large-distance forms on the square and cubic torus
