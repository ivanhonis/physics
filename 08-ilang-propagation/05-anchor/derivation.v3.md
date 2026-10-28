# Anchor for an unpinned field of oscillator cells: lowest eigenvector, long-range mark and weighing

- **Subproject:** 08-ilang-propagation
- **Package:** 05-anchor
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-25

## Changes from previous version

- Step 8, cubic torus: the limiting criterion for $`a_{\rm bond}`$ is now the exact one, $`N/(D-H)\to0`$ (image differences at the bodies over the direct-minus-image difference at the midpoint). It reduces to $`N/D\to0`$ only under $`H/D\to0`$, which families (A) and (B) supply. A new control, a pair far from a source next to the anchor, has $`N/D\to0`$ but $`a_{\rm bond}\not\to0`$; it is checked numerically (I1).
- Result 14, (5.27) in the twin: the unrestricted equivalence for $`a_{\rm bond}`$ is removed and the control is added (I1).
- Consistency check 1: the limit $`\kappa_a\to0`$ is separated from the criterion at $`\kappa_a=0`$. For linear grips the anchored lowest eigenvectors have no normalizable limit (I2).
- Code: `code/v3/check_anchor.py` gets the pair control of I1 (asymptotics.txt). The script was run again, and all numbers come from `code/v3/output/`.

## Response to verification

- I1: Accepted and fixed in Step 8 (cubic torus, after (5.27)) and in Result 14. With $`N:=\Delta g_h(x_1)+\Delta g_h(x_2)`$, $`D:=\Delta g_s(\bar x)`$, $`H:=\Delta g_h(\bar x)`$, the exact criterion is $`a_{\rm bond}\to0`$ iff $`N/(D-H)\to0`$. It is equivalent to $`N/D\to0`$ when also $`H/D\to0`$, not in general. Families (A) and (B) give $`H/D\to0`$, so their conclusions, (5.24) and the far-anchor theorem, are unchanged. The verifier's example ($`h=0`$, $`x_s=e_x`$, $`x_{1,2}=(n^3,\pm n^4,0)`$) is added as a control and checked on $`\mathbb Z^3`$ (asymptotics.txt). In it, $`N/D\to0`$, $`N/(D-H)\to1`$ and $`a_{\rm bond}\to-(c_\phi-g_\infty(e_x))/c_\phi`$.
- I2: Accepted and fixed in Consistency check 1. For $`F_2\ne0`$, the limit $`\kappa_a\to0`$ of (5.10) gives (5.5). For a linear grip, (5.10) holds at every $`\kappa_a>0`$, while at $`\kappa_a=0`$ Step 2 gives no lowest eigenvector. The anchored lowest eigenvectors lose their normalizable limit (mean shift $`-\mu F_1/\kappa_a`$, diverging spread of the uniform change), and their eigenvalue tends to $`-\infty`$. The criterion at $`\kappa_a=0`$ is that of Step 2, not the limit of (5.10).

## Setup and assumptions

**Description** (assumptions M8, M9, A11, A15; all from the question).
- *Field:* oscillator cells, one at each place $`x`$ of a ring ($`D=1`$) or cubic torus ($`D=3`$) of side $`L\ge3`$, $`n=L^D`$; contract the compression $`C_M=\Pi H\Pi`$ of $`H=\tfrac12p^{\rm T}p+\tfrac12q^{\rm T}\kappa_h\Delta q`$ ($`\Delta`$ the graph Laplacian, $`\kappa_h>0`$, no pinning), plus the terms below; $`\Phi_x=q_x`$. $`P_x:=e_xe_x^{\rm T}`$.
- *Anchor:* $`\tfrac{\kappa_a}2q_h^2`$, $`\kappa_a>0`$, at one place $`h`$.
- *Bodies:* held Model D bodies ($`\tau=0`$, no rest and clock term) at places $`x_i`$, in the eigenvector $`\lvert\sigma_i\rangle\lvert f_{k_i}\rangle`$ of $`S`$ with eigenvalue $`\mu_i=\sigma_iM_{k_i}`$, $`M_k=m+2\pi k/(N\lambda_0)>0`$; grip $`\sum_x\lvert x\rangle\langle x\rvert\otimes S\otimes F^{(i)}(q_x)`$, $`F^{(i)}=F^{(i)}_0+F^{(i)}_1q+F^{(i)}_2q^2`$, $`F^{(i)}_1\ne0`$ (class G2). Notation: $`\alpha_i:=2\mu_iF_2^{(i)}`$, and for $`F_0^{(i)}\ne0`$: $`\hat b_i:=F_1^{(i)}/(2F_0^{(i)})`$, $`\hat\beta_i:=2F_2^{(i)}/F_1^{(i)}`$. The square grip $`4F_0F_2=F_1^2`$ is $`\hat\beta=\hat b`$, i.e. $`F=F_0(1+\hat\beta q)^2`$.
- *Sources:* held objects coupled by $`g_sq_{x_s}`$.
- *State:* the total contract is diagonal in the place label of every held body and commutes with its $`S`$, so it is block diagonal in (place, $`\sigma_i`$, $`k_i`$). "Lowest eigenvector" means that of the block of the stated body labels (the reading of (2.5)); statements about the whole contract (all blocks) are marked as such.

**Inputs** (quoted in the question, from 08-ilang-propagation/02-grip-weight@v3, pinned field $`K=\kappa_h\Delta+m_h^2\mathbb 1`$, $`G_0=(K^{-1})_{xx}`$, $`w_0=\langle q_x^2\rangle`$):
- (2.5): a lowest eigenvector exists ($`M\to\infty`$) iff $`1+2\sigma M_kF_2G_0>0`$; otherwise the lowest eigenvalue of $`C_M\to-\infty`$.
- (2.18): for grips $`F^{(i)}=F^{(i)}(0)\Phi_i(\beta q)`$, at order $`\mu^2`$ and leading order in $`\beta`$: $`\rho_{{\rm mark},i}=1`$ and $`\rho_{{\rm bond},i}=m_{\mathbf r}`$ for every level and both branches iff $`2\Phi_i''(0)=\Phi_i'(0)^2`$ and $`\Phi_1'(0)=\Phi_2'(0)`$, i.e. square grips with a common $`\hat\beta`$.

**Definitions** (those of 02-grip-weight, applied with the anchor). *Cost* $`C`$: lowest eigenvalue with the body minus that without it, no sources. Replacing $`F\to sF`$: $`C(s)=sC^{(1)}+s^2C^{\rm mark}+O(s^3)`$. *Weight:* $`W(x)`$ is the $`g_s`$-linear part of the cost in the presence of the source, $`W^{(1)},W^{\rm mark}`$ its $`s`$ and $`s^2`$ coefficients; the weight is $`W(x)-W(x')`$. *Bond* $`B=C_{12}-C_1-C_2`$ (no sources) and its $`g_s`$-linear part $`W_{\rm bond}`$, both at order $`s^2`$. For two placements $`x,x'`$ of a body (or two placements of a pair related by a translation): $`\Delta f:=f(x)-f(x')`$, $`\bar f:=\tfrac12(f(x)+f(x'))`$, and
```math
\rho_{\rm mark}:=\frac{\Delta W^{\rm mark}}{\Delta W^{(1)}}\,\frac{\bar C^{(1)}}{\bar C^{\rm mark}},\qquad\rho_{{\rm bond},i}:=\frac{\Delta W_{\rm bond}}{\bar B}\,\frac{\bar C_i^{(1)}}{\Delta W_i^{(1)}},\qquad m_{\mathbf r}:=\frac{\Delta\phi_a(x_1)+\Delta\phi_a(x_2)}{2\Delta\phi_a(\bar x)},
```
where $`C_i^{(1)},W_i^{(1)}`$ belong to one body with the grip and level of body $`i`$ at the midpoint $`\bar x`$ of the pair (a place), and $`\phi_a`$ is the made field (5.11). With place-independent costs these are the ratios of 02-grip-weight; with an anchor the costs depend on the place and are taken as means over the two placements. *Mutual cost* of two sources: the part $`\propto g_1g_2`$ of the lowest eigenvalue.

**Regime.** Exact statements hold for every $`L\ge3`$, $`\kappa_h,\kappa_a>0`$, $`h`$, on both graphs; asymptotic statements on the cubic torus take $`L\to\infty`$ first at fixed places. Places are in lattice units (separations are cell separations, M2). Standard mathematics used: Gaussian lowest eigenvectors of quadratic contracts, min-max, Schur complements, Sherman–Morrison and the matrix determinant lemma, M-matrices, lattice Green functions and their asymptotics.

## Derivation

### Step 1. The contract of a block and the limit $`M\to\infty`$

In the block of the bodies, $`S\to\mu_i`$ and $`\lvert x\rangle\langle x\rvert\to\delta_{x,x_i}`$, so the total contract acts on the field as
```math
C_{\rm f}=\tfrac12p^{\rm T}p+\tfrac12q^{\rm T}Aq+b^{\rm T}q+c_0,\quad A=\kappa_h\Delta+\kappa_aP_h+\sum_i\alpha_iP_{x_i},\quad b=\sum_i\mu_iF_1^{(i)}e_{x_i}+\sum_sg_se_{x_s},\quad c_0=\sum_i\mu_iF_0^{(i)},\qquad\text{(5.1)}
```
with $`\kappa_a=0`$ without an anchor. For $`A>0`$ the uncompressed $`C_{\rm f}`$ has a simple isolated lowest eigenvalue with a Gaussian eigenvector (standard):
```math
E_0=c_0+\tfrac12{\rm Tr}\sqrt A-\tfrac12b^{\rm T}A^{-1}b,\qquad\langle q\rangle=-A^{-1}b,\qquad\langle q_xq_y\rangle-\langle q_x\rangle\langle q_y\rangle=\tfrac12(A^{-1/2})_{xy}.\qquad\text{(5.2)}
```
If $`A`$ has a negative eigenvalue, $`C_{\rm f}`$ is unbounded below. If $`A\ge0`$ has a kernel vector $`v`$, the contract along $`v`$ is $`\tfrac12p_v^2+(b\cdot v)q_v`$: unbounded below if $`b\cdot v\ne0`$, otherwise a free mode whose spectrum is continuous at its bottom, with no eigenvector there. *Sense of $`M\to\infty`$:* the ranges of $`\Pi`$ grow with $`M`$ and their union (finite superpositions of oscillator levels) is a core of the uncompressed contract (standard for quadratic operators). By min-max the lowest eigenvalue of $`C_M`$ does not increase with $`M`$ and tends to the bottom of the spectrum; if that is an isolated simple eigenvalue, the lowest eigenvectors of $`C_M`$ converge in norm to it (a unit vector with cost within $`\epsilon`$ of $`E_0`$ has overlap$`^2\ge1-\epsilon/\text{gap}`$). Hence
```math
\text{a lowest eigenvector exists }(M\to\infty)\iff A>0;\ \text{otherwise the lowest eigenvalue of }C_M\text{ tends to }-\infty\text{ or to the bottom of a continuum}.\qquad\text{(5.3)}
```

### Step 2. Without an anchor (item 1)

$`\Delta\ge0`$ with kernel the uniform vector $`\mathbf 1`$ (connected graph): the only free direction is the uniform change. Let the bodies sit at $`n`$ distinct places (bodies at one place add their $`\alpha`$), $`\mathcal A:={\rm diag}(\alpha_i)`$. *Kron reduction* (Schur complement): $`\min\{q^{\rm T}\kappa_h\Delta q:\ q_{x_i}=y_i\}=y^{\rm T}\mathcal L_ny`$, attained at the harmonic extension, with $`\mathcal L_n\ge0`$ the reduced Laplacian of the body places, kernel $`{\rm span}\{\mathbf 1\}`$; $`\mathcal L_1=0`$, $`\mathcal L_2=r_{12}^{-1}\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)`$ with $`r_{12}=r(x_1,x_2)`$ of (5.8). So $`q^{\rm T}A_0q\ge y^{\rm T}(\mathcal L_n+\mathcal A)y`$ with equality at the extension, and for $`y=0`$, $`q^{\rm T}A_0q=\kappa_hq^{\rm T}\Delta q>0`$ unless $`q=0`$:
```math
A_0>0\iff\mathcal L_n+\mathcal A>0.\qquad\text{(5.4)}
```
*Members.* With $`y=\mathbf 1`$: necessary $`\sum_i\mu_iF_2^{(i)}>0`$; sufficient: all $`\alpha_i\ge0`$, one $`>0`$. One body:
```math
\text{lowest eigenvector}\iff\mu F_2>0\iff\sigma={\rm sign}\,F_2\ (\text{every level }k);\quad\text{for }\sigma=-{\rm sign}\,F_2\text{ the lowest eigenvalue of }C_M\to-\infty.\qquad\text{(5.5)}
```
Two bodies (trace and determinant of a $`2\times2`$ matrix):
```math
A_0>0\iff\alpha_1+\alpha_2>0\ \text{and}\ \alpha_1\alpha_2+(\alpha_1+\alpha_2)/r_{12}>0.\qquad\text{(5.6)}
```
If all $`\alpha_i=0`$ (no bodies, or only linear grips), $`A_0=\kappa_h\Delta`$ and $`b\cdot\mathbf 1=\sum_i\mu_iF_1^{(i)}+\sum_sg_s`$: the lowest eigenvalue tends to $`-\infty`$ if this is $`\ne0`$; otherwise the uniform change is free and there is no lowest eigenvector. In particular the field alone has none, so the reference eigenvalue of the cost of a body does not exist. *Whole contract:* the block with $`\sigma_i=-{\rm sign}\,F_2^{(i)}`$ for every body has all $`\alpha_i\le0`$, so without an anchor the whole contract has no lowest eigenvector, for any bodies of (G2).
*A grip as anchor.* A body with $`\alpha=2\mu F_2>0`$ adds $`\tfrac\alpha2q_{x}^2`$: an anchor of strength $`\alpha`$ at its own place (and a source $`\mu F_1`$). For one such body, summing the components of $`(\kappa_h\Delta+\alpha P_x)v=e_y`$ gives $`\alpha v_x=1`$, so $`(A_0^{-1})_{xy}=1/\alpha`$ for every $`y`$, and its $`g_s`$-linear cost $`-\mu F_1g_s(A_0^{-1})_{xx_s}`$ is
```math
W(x)=-\frac{F_1g_s}{2F_2}\quad\text{for every }x,x_s:\qquad W(x)-W(x')=0.\qquad\text{(5.7)}
```
A body that anchors the field itself has no weight; and $`C(s)`$ has no lowest eigenvector for $`s\le0`$, so $`C^{(1)},C^{\rm mark}`$ do not exist.

### Step 3. The anchored Green function

$`K_a:=\kappa_h\Delta+\kappa_aP_h>0`$ ($`q^{\rm T}K_aq=0`$ forces $`q`$ uniform and $`q_h=0`$). Let $`g:=(\kappa_h\Delta)^+`$, $`g(x)=\frac1{\kappa_hL^D}\sum_{k\ne0}\frac{e^{ik\cdot x}}{\hat\Delta(k)}`$, $`\hat\Delta(k)=\sum_j(2-2\cos k_j)`$, $`k\in\frac{2\pi}L\mathbb Z_L^D`$, and $`r(x,y):=2[g(0)-g(x-y)]`$ (the resistance distance of the springs $`\kappa_h`$). For $`K_av=f`$, summing components gives $`\kappa_av_h=\sum_xf_x=:F`$; then $`\kappa_h\Delta v=f-Fe_h\perp\mathbf 1`$, so $`v=g*(f-Fe_h)+c\mathbf 1`$ with $`c`$ fixed by $`v_h=F/\kappa_a`$. For $`f=e_y`$:
```math
G_a(x,y):=(K_a^{-1})_{xy}=\frac1{\kappa_a}+g(x-y)-g(x-h)-g(y-h)+g(0)=\frac1{\kappa_a}+\frac12\bigl[r(x,h)+r(y,h)-r(x,y)\bigr],\qquad\text{(5.8)}
```
exact for every $`L`$, $`D`$, $`\kappa_h,\kappa_a>0`$, $`h`$. $`G_a(h,y)=1/\kappa_a`$ for all $`y`$; $`G_a>0`$ entrywise ($`K_a`$ is an irreducible M-matrix). *Ring:* $`g(x)=\frac1{\kappa_h}\bigl[\frac{L^2-1}{12L}-\frac{s(L-s)}{2L}\bigr]`$ ($`s`$ the ring distance; zero sum, $`\kappa_h\Delta g=\delta-\frac1L`$), so $`r=\frac{s(L-s)}{\kappa_hL}`$. *Cubic torus:* as $`L\to\infty`$ at fixed arguments, $`g\to g_\infty`$, the Green function of $`\kappa_h\Delta`$ on $`\mathbb Z^3`$, with $`g_\infty(0)=\gamma_3/\kappa_h`$, $`\gamma_3=0.2527310`$, and $`g_\infty(x)=\frac1{4\pi\kappa_h\lvert x\rvert}+O(\lvert x\rvert^{-3})`$ (asymptotics.txt). For $`\nu>0`$, Sherman–Morrison with $`\gamma_\nu:=(\kappa_h\Delta+\nu^2)^{-1}`$ gives
```math
R_{xy}(\nu):=\bigl[(K_a+\nu^2)^{-1}\bigr]_{xy}=\gamma_\nu(x-y)-\frac{\kappa_a\gamma_\nu(x-h)\gamma_\nu(y-h)}{1+\kappa_a\gamma_\nu(0)},\qquad R(0)=K_a^{-1};\qquad\text{(5.9)}
```
$`R_{xy}(\nu)>0`$, and $`R_{xx}(\nu)\le\min(\Gamma(x),\nu^{-2})`$ decreases in $`\nu`$.

### Step 4. With an anchor: existence, made field, field constants (item 2)

*Existence.* $`\min\{q^{\rm T}K_aq:\ q_{x_i}=y_i\}=y^{\rm T}\Gamma_n^{-1}y`$ with $`(\Gamma_n)_{ij}:=G_a(x_i,x_j)`$ (standard); as in Step 2,
```math
A>0\iff\Gamma_n^{-1}+\mathcal A>0;\qquad\text{one body: }1+2\mu F_2\Gamma(x)>0,\quad\Gamma(x):=G_a(x,x)=\frac1{\kappa_a}+r(x,h).\qquad\text{(5.10)}
```
It holds in every block with all $`\mu_iF_2^{(i)}\ge0`$ (linear grips, both branches; no bodies). For $`\mu F_2<0`$ it is $`2M_k\lvert F_2\rvert\Gamma(x)<1`$: (2.5) with $`G_0\to\Gamma(x)`$. On the ring $`\Gamma=\frac1{\kappa_a}+\frac{d(L-d)}{\kappa_hL}`$ ($`d`$ the ring distance to $`h`$): the branch $`\sigma=-{\rm sign}\,F_2`$ loses its lowest eigenvector once $`\frac{d(L-d)}{\kappa_hL}\ge\frac1{2M_k\lvert F_2\rvert}-\frac1{\kappa_a}`$. On the cubic torus $`\Gamma`$ is bounded uniformly in $`L`$ and tends to $`\Gamma_\infty-2g_\infty(x-h)<\Gamma_\infty:=\frac1{\kappa_a}+\frac{2\gamma_3}{\kappa_h}`$, so for $`L\to\infty`$ the condition holds at every place iff $`2M_k\lvert F_2\rvert\Gamma_\infty\le1`$. For the whole contract with one body the condition is needed for the highest level and the branch with $`\mu F_2<0`$.

*Two bodies.* $`\Gamma_n^{-1}+\mathcal A`$ ($`n=2`$) is positive iff its trace and determinant are. Multiplying both by $`\det\Gamma_n>0`$, with $`G_{12}:=G_a(x_1,x_2)`$:
```math
A>0\iff\bigl(1+\alpha_1\Gamma(x_1)\bigr)\bigl(1+\alpha_2\Gamma(x_2)\bigr)>\alpha_1\alpha_2G_{12}^2\ \text{and}\ \Gamma(x_1)+\Gamma(x_2)+(\alpha_1+\alpha_2)\bigl(\Gamma(x_1)\Gamma(x_2)-G_{12}^2\bigr)>0;\qquad\text{sufficient: }\bar a\,\bigl(\max_i\Gamma(x_i)+G_{12}\bigr)<1,\qquad\text{(5.26)}
```
with $`\bar a:=\max_i\max(0,-\alpha_i)`$. The sufficient condition holds because $`\Gamma_n^{-1}+\mathcal A\ge\lambda_{\max}(\Gamma_n)^{-1}-\bar a`$, and $`\lambda_{\max}(\Gamma_n)`$ is at most the largest row sum ($`G_{12}>0`$). Two bodies that each meet the one-body condition need not meet (5.26). For $`\alpha_1=\alpha_2=-a`$ and $`\Gamma(x_1)=\Gamma(x_2)=\Gamma`$, the pair needs $`a(\Gamma+G_{12})<1`$, while each body alone needs only $`a\Gamma<1`$. On the cubic torus far from the anchor, $`G_{12}\to c_\phi+g_\infty(\mathbf r)\ge c_\phi>0`$ ((5.13)), so the gap persists at every separation.

Checked against $`\lambda_{\min}(A)`$, on two sizes of each graph (existence.txt):
- one body: three grips, two levels, both branches, three distances, with (5.5) and (5.6);
- random pairs of bodies: (5.10) and (5.26) agree with $`\lambda_{\min}(A)`$ in 40/40 cases;
- for each lattice, a pair with $`\alpha_1=\alpha_2=-a`$ and $`1/\lambda_{\max}(\Gamma_n)<a<1/\max_i\Gamma(x_i)`$: each body alone has a lowest eigenvector, but the pair has $`\lambda_{\min}(A)<0`$, as (5.26) predicts.

*Made field.* Without bodies, (5.2) with $`b=g_se_{x_s}`$:
```math
\phi_a(x):=\langle q_x\rangle=-g_sG_a(x,x_s)=-g_s\Bigl[\frac1{\kappa_a}+\frac{r(x_s,h)}2\Bigr]-\frac{g_s}2\bigl[r(x,h)-r(x,x_s)\bigr].\qquad\text{(5.11)}
```
It is a uniform shift (the anchored cell moves by $`-g_s/\kappa_a`$, plus half the resistance from source to anchor) plus a place-dependent part. Cubic torus, $`L\to\infty`$, with $`c_\phi:=\frac1{\kappa_a}+\frac{\gamma_3}{\kappa_h}`$: $`\phi_a(x)=-g_s\bigl[c_\phi-g_\infty(x_s-h)\bigr]-g_s\bigl[g_\infty(x-x_s)-g_\infty(x-h)\bigr]`$: the source and an image of opposite sign at the anchor, over a nonzero constant. Line (ring, $`L\to\infty`$): $`\phi_a=-g_s[\frac1{\kappa_a}+\frac{\min(d_x,d_s)}{\kappa_h}]`$ for $`x,x_s`$ on one side of $`h`$, $`-g_s/\kappa_a`$ on opposite sides.

*Field constants.* With $`K_au_a=\omega_a^2u_a`$ orthonormal, $`\frac1{2\sqrt\lambda}=\frac1\pi\int_0^\infty\frac{d\nu}{\lambda+\nu^2}`$ and $`\frac1{\omega_a\omega_b(\omega_a+\omega_b)}=\frac2\pi\int_0^\infty\frac{d\nu}{(\omega_a^2+\nu^2)(\omega_b^2+\nu^2)}`$, the constants that enter (Steps 6–7) are $`\Gamma(x)`$ (analogue of $`G_0`$), $`G_a(x,y)`$ (of $`G(x-y)`$) and
```math
w(x):=\langle q_x^2\rangle=\tfrac12(K_a^{-1/2})_{xx}=\frac1\pi\int_0^\infty R_{xx}(\nu)\,d\nu,\qquad\Sigma(x,y):=\sum_{a,b}\frac{u_a(x)u_a(y)u_b(x)u_b(y)}{\omega_a\omega_b(\omega_a+\omega_b)}=\frac2\pi\int_0^\infty R_{xy}(\nu)^2d\nu,\qquad\text{(5.12)}
```
the analogue of $`w_0`$ and the static correlation of $`q_x^2,q_y^2`$ (a term $`\epsilon q_y^2`$ changes $`w(x)`$ by $`-\epsilon\Sigma(x,y)`$). Against the distance $`d`$ to $`h`$ ($`x-y`$ fixed):
```math
\begin{aligned}&\text{line }(L\to\infty):&&\Gamma=\tfrac1{\kappa_a}+\tfrac d{\kappa_h},\quad w=\tfrac{\ln d}{2\pi\sqrt{\kappa_h}}+O(1),\quad\Sigma(x,x)=\tfrac{2\ln2}{\pi\kappa_h^{3/2}}\,d\,(1+o(1));\\&\text{cubic }(L\to\infty):&&\Gamma=\Gamma_\infty-2g_\infty(x-h),\quad G_a(x,y)\xrightarrow{d\to\infty}c_\phi+g_\infty(x-y),\quad w-w_\infty,\ \Sigma-\Sigma_\infty=O(d^{-3}),\end{aligned}\qquad\text{(5.13)}
```
with $`w_\infty,\Sigma_\infty(x-y)`$ the values (5.12) of the unanchored infinite lattice. *Line:* the anchor term of (5.9) makes $`R_{xx}(\nu)\simeq\frac{1-e^{-2\nu d/\sqrt{\kappa_h}}}{2\nu\sqrt{\kappa_h}}`$ for $`d\gg1`$ (up to $`O(1/d)`$ relative terms from $`\kappa_a`$); $`\frac1\pi\int`$ gives the logarithm, and $`\frac2\pi\int`$ gives $`\frac{d}{\pi\kappa_h^{3/2}}\int_0^\infty\frac{(1-e^{-t})^2}{t^2}dt=\frac{2\ln2\,d}{\pi\kappa_h^{3/2}}`$. From (5.9) on $`\mathbb Z`$ at $`\kappa_h=1`$, $`\kappa_a=0.7`$: $`w(10d)-w(d)=0.3485,0.3645,0.3663`$ for $`d=10,100,1000`$ against $`\frac{\ln10}{2\pi}=0.3665`$, and $`\Sigma/d=0.4895,0.4463,0.4418,0.4413`$ for $`d=10,\dots,10^4`$ against $`\frac{2\ln2}\pi=0.4413`$ (asymptotics.txt). *Cubic:* for each $`\nu>0`$ the torus resolvent tends to (5.9) on $`\mathbb Z^3`$, dominated by $`\min(\Gamma_{\max},\nu^{-2})`$, so (5.12) converges; the anchor term is $`O(e^{-2\nu d/\sqrt{\kappa_h}}/d^2)`$, whose $`\nu`$-integral is $`O(d^{-3})`$. At $`\nu=0`$ the zero mode of $`\Delta`$ keeps the anchor at every distance: $`\Gamma\to\frac1{\kappa_a}+\frac{2\gamma_3}{\kappa_h}`$, not the unanchored $`g_\infty(0)=\gamma_3/\kappa_h`$. The constants $`w,\Sigma`$ forget a distant anchor; $`\Gamma,G_a`$ do not.

### Step 5. Mutual cost of two sources (item 3)

By (5.2) with $`A=K_a`$, $`b=g_1e_{x_1}+g_2e_{x_2}`$:
```math
\mathcal E_{12}=-g_1g_2\,G_a(x_1,x_2)=-g_1g_2\Bigl[\frac1{\kappa_a}+g(x_1-x_2)-g(x_1-h)-g(x_2-h)+g(0)\Bigr],\qquad\text{(5.14)}
```
exact on both graphs for every $`L`$ (with held bodies, $`G_a\to(A^{-1})_{x_1x_2}`$); it is the constant $`-g_1g_2/\kappa_a`$ if one source sits at the anchor. Checked against the exact eigenvalue to 10 digits on rings $`L=64,256`$ and tori $`L=16,32`$ (mutual_cost.txt). *Cubic torus, $`L\to\infty`$ first*, all of $`\lvert x_1-x_2\rvert,\lvert x_1-h\rvert,\lvert x_2-h\rvert\ge\ell\gg1`$:
```math
\mathcal E_{12}=-g_1g_2\,c_\phi-\frac{g_1g_2}{4\pi\kappa_h}\Bigl[\frac1{\lvert x_1-x_2\rvert}-\frac1{\lvert x_1-h\rvert}-\frac1{\lvert x_2-h\rvert}\Bigr]+O(\ell^{-3}).\qquad\text{(5.15)}
```
With $`\mathbf r=x_2-x_1`$, midpoint $`X`$, $`D_X=\lvert X-h\rvert`$:
- *(a) $`L\to\infty`$, then $`D_X\to\infty`$ at fixed $`\mathbf r`$, then $`\lvert\mathbf r\rvert\to\infty`$:* $`\mathcal E_{12}\to-g_1g_2[c_\phi+g_\infty(\mathbf r)]`$, a fall as $`-\frac{g_1g_2}{4\pi\kappa_h\lvert\mathbf r\rvert}`$, the coefficient of the field without an anchor. Uniformly for $`1\ll\lvert\mathbf r\rvert\ll D_X`$ (the dipole parts of the two anchor terms cancel): $`\mathcal E_{12}=-g_1g_2[c_\phi-\frac1{2\pi\kappa_hD_X}]-\frac{g_1g_2}{4\pi\kappa_h\lvert\mathbf r\rvert}[1+O(\lvert\mathbf r\rvert^3/D_X^3)+O(\lvert\mathbf r\rvert^{-2})]`$.
- *(b) $`L\to\infty`$, then $`\lvert\mathbf r\rvert\to\infty`$ with $`x_1`$ fixed:* $`\mathcal E_{12}=-g_1g_2[c_\phi-g_\infty(x_1-h)]-\frac{g_1g_2}{4\pi\kappa_h}\frac{\hat{\mathbf r}\cdot(x_1-h)}{\lvert\mathbf r\rvert^2}+O(\lvert\mathbf r\rvert^{-3})`$: a fall as $`\lvert\mathbf r\rvert^{-2}`$ or faster, no long-range mark; no place dependence at all for $`x_1=h`$.
- *(c) $`L\to\infty`$, then $`\lvert\mathbf r\rvert\to\infty`$ at fixed $`X`$:* $`\lvert x_i-h\rvert=\frac{\lvert\mathbf r\rvert}2(1+O(D_X/\lvert\mathbf r\rvert))`$ and $`\mathcal E_{12}=-g_1g_2c_\phi+\frac{3g_1g_2}{4\pi\kappa_h\lvert\mathbf r\rvert}[1+O(D_X^2/\lvert\mathbf r\rvert^2)+O(\lvert\mathbf r\rvert^{-2})]`$: a fall as the inverse separation with $`-3`$ times the coefficient of (a).
- *$`L`$ not first:* (5.14) is a bounded function on the torus; the forms above need $`\lvert\mathbf r\rvert,D_X\ll L`$.

So the coefficient of the unanchored field is obtained when $`\lvert\mathbf r\rvert/D_X\to0`$ after $`L\to\infty`$, and not in the orders (b), (c). On $`\mathbb Z^3`$ the coefficient of $`-\frac{g_1g_2}{4\pi\kappa_h\lvert\mathbf r\rvert}`$ between consecutive separations is $`+1.03,+1.00`$ for $`D_X=40`$, $`\lvert\mathbf r\rvert=4\to8\to16`$ (a), and $`-3.14,-3.03,-3.01`$ for $`X=h`$, $`\lvert\mathbf r\rvert=8\to16\to32\to64`$ (c); for $`x_1-h=3\hat e_x`$, $`4\pi\kappa_h\lvert\mathbf r\rvert^2[\mathcal E_{12}-\mathcal E_{12}(\infty)]=-2.20,-2.53,-2.74,-2.87`$ for $`\lvert\mathbf r\rvert=8,\dots,64`$, approaching $`-\hat{\mathbf r}\cdot(x_1-h)=-3`$ (b) (asymptotics.txt). On the torus $`L=32`$ with $`D_X=6`$ it runs from $`+1.08`$ ($`\lvert\mathbf r\rvert=2\to4`$) through $`\approx0`$ to $`-1.11`$ ($`12\to16`$), the crossover from (a) to (c); with one source at $`h`$, $`\mathcal E_{12}=-1/\kappa_a`$ to 11 digits (mutual_cost.txt). *Ring (control):* from $`r=\frac{s(L-s)}{\kappa_hL}`$,
```math
\mathcal E_{12}=-g_1g_2\Bigl[\frac1{\kappa_a}+\frac{d_1(L-d_1)+d_2(L-d_2)-s(L-s)}{2\kappa_hL}\Bigr]\xrightarrow{L\to\infty}\begin{cases}-g_1g_2\bigl[\frac1{\kappa_a}+\frac{\min(d_1,d_2)}{\kappa_h}\bigr]&\text{one side of }h,\\-g_1g_2/\kappa_a&\text{opposite sides}.\end{cases}\qquad\text{(5.16)}
```
It is a quadratic polynomial in the distances at finite $`L`$, independent of the separation at fixed distance of the nearer source for $`L\to\infty`$, and grows with that distance: no part falls as the inverse separation in any order of the limits.

### Step 6. Cost and weight of one body (item 4)

One body at $`x`$: $`A=K_a+\alpha P_x`$. Determinant lemma, $`\det(A+\nu^2)/\det(K_a+\nu^2)=1+\alpha R_{xx}(\nu)`$, with $`\int_0^\infty\ln\frac{\lambda'+\nu^2}{\lambda+\nu^2}d\nu=\pi(\sqrt{\lambda'}-\sqrt\lambda)`$, gives $`\tfrac12{\rm Tr}(\sqrt A-\sqrt{K_a})=\frac1{2\pi}\int_0^\infty\ln(1+\alpha R_{xx})d\nu`$; Sherman–Morrison gives $`(A^{-1})_{xy}=G_a(x,y)/(1+\alpha\Gamma(x))`$. By (5.2), the cost and its $`g_s`$-linear part with a source (the trace does not depend on $`g_s`$) are, under (5.10),
```math
C(x)=\mu F_0+\frac1{2\pi}\int_0^\infty\ln\bigl(1+2\mu F_2R_{xx}(\nu)\bigr)d\nu-\frac{\mu^2F_1^2\,\Gamma(x)}{2\bigl(1+2\mu F_2\Gamma(x)\bigr)},\qquad W(x)=\frac{\mu F_1\,\phi_a(x)}{1+2\mu F_2\Gamma(x)}.\qquad\text{(5.17)}
```
Expanding in $`s`$ with (5.12):
```math
C^{(1)}=\mu\bigl(F_0+F_2w(x)\bigr),\quad C^{\rm mark}=-\frac{\mu^2}2\bigl(F_1^2\Gamma(x)+F_2^2\Sigma(x,x)\bigr),\quad W^{(1)}=\mu F_1\phi_a(x),\quad W^{\rm mark}=-2\mu^2F_1F_2\,\Gamma(x)\,\phi_a(x).\qquad\text{(5.18)}
```
All four are fixed by eigenvalues of blocks (M6). At leading order in the grip scale ($`\hat\beta\hat bw,\ \hat\beta^2\Sigma/\Gamma\ll1`$) they give, at every place, $`W^{(1)}=2\hat b\,C^{(1)}\phi_a`$ and $`W^{\rm mark}=2\hat\beta\,C^{\rm mark}\phi_a`$: each component's $`g_s`$-linear part is its own cost times the field at the body, with equal factors iff the grip is square. Beyond order $`s^2`$, (5.17) carries $`u(x):=2M_k\lvert F_2\rvert\Gamma(x)`$ and depends on the level.

### Step 7. Bond (item 4)

Two bodies at $`x_1\ne x_2`$, $`G_{12}:=G_a(x_1,x_2)`$, $`\Sigma_{12}:=\Sigma(x_1,x_2)`$. The $`2\times2`$ determinant lemma gives the trace part $`\frac1{2\pi}\int\ln[(1+\alpha_1R_{11})(1+\alpha_2R_{22})-\alpha_1\alpha_2R_{12}^2]d\nu`$, whose part depending on both bodies is $`-\frac{\alpha_1\alpha_2}{2\pi}\int R_{12}^2d\nu=-\frac{\alpha_1\alpha_2}4\Sigma_{12}`$ at order $`s^2`$. In $`-\frac12b^{\rm T}A^{-1}b`$, $`A^{-1}=K_a^{-1}-\sum_i\alpha_iK_a^{-1}P_{x_i}K_a^{-1}+O(\alpha^2)`$. At order $`s^2`$ and first order in $`g_s`$:
```math
B=-\mu_1\mu_2\bigl[F_1^{(1)}F_1^{(2)}G_{12}+F_2^{(1)}F_2^{(2)}\Sigma_{12}\bigr],\qquad W_{\rm bond}=-2\mu_1\mu_2G_{12}\bigl[F_1^{(1)}F_2^{(2)}\phi_a(x_2)+F_2^{(1)}F_1^{(2)}\phi_a(x_1)\bigr],\qquad\text{(5.19)}
```
i.e. $`W_{\rm bond}=-\mu_1\mu_2F_1^{(1)}F_1^{(2)}G_{12}\Psi`$ with $`\Psi:=\hat\beta_1\phi_a(x_1)+\hat\beta_2\phi_a(x_2)`$.

### Step 8. Weighing ratios, conditions and orders (item 4)

From (5.18), (5.19) and $`\Delta(fg)=\bar f\Delta g+\bar g\Delta f`$:
```math
\rho_{\rm mark}=\frac{4F_2(F_0+F_2\bar w)\,\bar\Gamma}{F_1^2\bar\Gamma+F_2^2\bar\Sigma}\,(1+a_{\rm mark}),\qquad a_{\rm mark}:=\frac{\bar\phi_a\,\Delta\Gamma}{\bar\Gamma\,\Delta\phi_a},\qquad\text{(5.20)}
```
```math
\rho_{{\rm bond},i}=\frac{\bar G_{12}\,\Delta\Psi+\bar\Psi\,\Delta G_{12}}{\bar G_{12}+\frac14\hat\beta_1\hat\beta_2\bar\Sigma_{12}}\cdot\frac{1+\hat\beta_i\hat b_i\,\bar w(\bar x)}{2\hat b_i\,\Delta\phi_a(\bar x)},\qquad\text{(5.21)}
```
($`\bar w,\bar\Sigma,\bar\Gamma`$ at the body places; for $`F_0^{(i)}=0`$ replace $`\frac{2\hat b_i}{1+\hat\beta_i\hat b_i\bar w}`$ by $`\frac{F_1^{(i)}}{F_0^{(i)}+F_2^{(i)}\bar w}`$). Both are exact at order $`s^2`$ for (G2) and independent of $`\mu`$: the same for every level and both branches.

*Coefficients and states.* For $`\lvert s\rvert`$ small, $`A(s)=K_a+s\mathcal A>0`$ for every grip, level and branch. So the $`s`$-coefficients of Steps 6–8 belong to an existing lowest eigenvector of the contract with $`F\to sF`$, and (5.20), (5.21) are defined for every member. They describe the lowest eigenvector of the stated contract ($`s=1`$) iff (5.10) holds at $`s=1`$ ((5.26) for a pair); then $`A(s)=(1-s)K_a+sA(1)>0`$ on all of $`[0,1]`$. $`A`$ increases with every $`\alpha_i`$, so a statement for every level up to $`k_i`$ and both branches needs (5.10) or (5.26) at $`\alpha_i=-2M_{k_i}\lvert F_2^{(i)}\rvert`$. Every statement below about the lowest eigenvector of the stated contract carries this condition.

*Numerical check* against the exact eigenvalue (weighing.txt; rings $`L=32,64`$ and tori $`L=8,12`$, three distances each, two levels, both branches):
- $`C^{(1)},C^{\rm mark},W^{(1)},W^{\rm mark}`$ agree with (5.18) to $`3\times10^{-6}`$ relative.
- $`\rho_{\rm mark}`$ agrees with (5.20) to $`4\times10^{-6}`$ relative for square, non-square, $`8F_0F_2=F_1^2`$ and linear grips. The linear grip gives $`\rho_{\rm mark}=0`$ within $`10^{-12}`$.
- $`B`$ and $`W_{\rm bond}`$ agree with (5.19) to $`9\times10^{-5}`$, and $`\rho_{{\rm bond},i}`$ with (5.21) to $`1.4\times10^{-4}`$ relative. This covers common square grips (five level and branch combinations), and common non-square, common $`8F_0F_2=F_1^2`$, common linear grips and a mixed (square, non-square) pair (two combinations each, giving each body both levels and both branches). The linear pair gives $`\rho_{{\rm bond},i}=0`$ within $`10^{-8}`$.
- The largest deviations come from the truncation of the $`s`$-stencil, largest on the ring at large $`\Gamma`$. Levels and branches agree within this accuracy.
- At $`s=1`$, $`\lambda_{\min}`$ of every pair block (156 cases) agrees with (5.26). On the tori every block of the check exists. On the rings some blocks do not exist at $`s=1`$, and there the ratios are formal coefficients only:
  - single blocks of the square grip with $`\sigma=-1`$: the upper level at $`d=2`$, both levels at $`d=5,10`$;
  - the single block of the grip $`8F_0F_2=F_1^2`$ with $`\sigma=-1`$, $`k=1`$, at $`d=10`$;
  - 22 of the 78 pair blocks, each containing a square-grip body with $`\sigma=-1`$.

*Excluded members:*
- $`\Delta\phi_a=0`$ (then $`\Delta W^{(1)}=0`$; on the line, (5.28) with $`\Delta m=0`$);
- $`\Delta\phi_a(\bar x)=0`$;
- $`F_0+F_2\bar w=0`$;
- $`\bar G_{12}+\frac14\hat\beta_1\hat\beta_2\bar\Sigma_{12}=0`$ (possible only for $`\hat\beta_1\hat\beta_2<0`$ outside $`\varepsilon\ll1`$).

$`\bar C^{\rm mark}\ne0`$ always ($`\Gamma,\Sigma>0`$).

*Controlled regime.* For $`F_0^{(i)}\ne0`$, let
```math
\varepsilon^2:=\max_i\Bigl(\frac{\lvert F_2^{(i)}\rvert}{\lvert F_0^{(i)}\rvert}\bar w,\ \hat\beta_i^2\frac{\bar\Sigma}{\bar\Gamma},\ \lvert\hat\beta_1\hat\beta_2\rvert\frac{\bar\Sigma_{12}}{\bar G_{12}}\Bigr)\ll1 .
```
Every entry is nonnegative, $`\lvert F_2\rvert/\lvert F_0\rvert=\lvert\hat\beta\hat b\rvert`$, and each $`\bar w`$ is taken at the places where it enters. Then the factors $`1+\hat\beta\hat b\bar w`$, $`1+\frac14\hat\beta^2\bar\Sigma/\bar\Gamma`$ and $`1+\frac14\hat\beta_1\hat\beta_2\bar\Sigma_{12}/\bar G_{12}`$ of (5.20), (5.21) are $`1+O(\varepsilon^2)`$; the rest of (5.20), (5.21) is exact. With $`\phi_j:=\phi_a(x_j)`$ and $`\bar\phi:=\phi_a(\bar x)`$:
```math
\rho_{\rm mark}=\frac{\hat\beta}{\hat b}(1+a_{\rm mark})\bigl(1+O(\varepsilon^2)\bigr),\qquad\rho_{{\rm bond},i}=\Bigl[\frac{\hat\beta_1\Delta\phi_1+\hat\beta_2\Delta\phi_2}{2\hat b_i\,\Delta\bar\phi}+\frac{(\hat\beta_1\bar\phi_1+\hat\beta_2\bar\phi_2)\,\Delta G_{12}}{2\hat b_i\,\bar G_{12}\,\Delta\bar\phi}\Bigr]\bigl(1+O(\varepsilon^2)\bigr).\qquad\text{(5.22)}
```
*Grips with $`F_0=0`$* ($`\hat b`$ undefined). (5.20), (5.21) give exactly
```math
\rho_{\rm mark}=\frac{\hat\beta^2\bar w\,(1+a_{\rm mark})}{1+\hat\beta^2\bar\Sigma/(4\bar\Gamma)},\qquad\rho_{{\rm bond},i}=\frac{\hat\beta_i\bar w(\bar x)}2\cdot\frac{\bar G_{12}\Delta\Psi+\bar\Psi\Delta G_{12}}{(\bar G_{12}+\frac14\hat\beta_1\hat\beta_2\bar\Sigma_{12})\,\Delta\bar\phi}.
```
In their weak-grip regime $`\eta_0^2:=\max_j(\hat\beta_j^2\bar w,\hat\beta_j^2\bar\Sigma/\bar\Gamma,\lvert\hat\beta_1\hat\beta_2\rvert\bar\Sigma_{12}/\bar G_{12})\ll1`$:
- $`\rho_{\rm mark}=\hat\beta^2\bar w(1+a_{\rm mark})(1+O(\eta_0^2))`$;
- $`\rho_{{\rm bond},i}=\frac{\hat\beta_i\bar w(\bar x)}2\bigl[\frac{\hat\beta_1\Delta\phi_1+\hat\beta_2\Delta\phi_2}{\Delta\bar\phi}+\frac{(\hat\beta_1\bar\phi_1+\hat\beta_2\bar\phi_2)\Delta G_{12}}{\bar G_{12}\Delta\bar\phi}\bigr](1+O(\eta_0^2))`$.

Both carry a factor $`O(\eta_0^2)`$, so at a fixed placement they vanish as $`\eta_0\to0`$. The first-order cost is then only $`\mu F_2w`$, and neither the mark nor a bond is weighed like it. Outside this regime there is no small parameter, and only (5.20), (5.21) apply.

For common square grips, $`\rho_{\rm mark}=(1+a_{\rm mark})(1+O(\varepsilon^2))`$ and $`\rho_{{\rm bond},i}=(m_{\mathbf r}+a_{\rm bond})(1+O(\varepsilon^2))`$, with $`a_{\rm bond}:=\frac{(\bar\phi_1+\bar\phi_2)\Delta G_{12}}{2\bar G_{12}\Delta\bar\phi}`$. For placements with $`\Delta\Gamma=\Delta G_{12}=0`$, (5.22) has the form of the pinned case and gives the conditions of (2.18) with $`G_0\to\Gamma`$, $`w_0\to w`$. In general the terms $`a`$ are the place dependence of the costs ($`\Delta\Gamma`$, $`\Delta G_{12}`$) times the uniform part of $`\phi_a`$ (5.11); the place-wise relations of Step 6 are not affected.

*Direct and image differences.* Let $`\Delta g_h:=g(x-h)-g(x'-h)`$ and $`\Delta g_s:=g(x-x_s)-g(x'-x_s)`$. By (5.8), (5.10), (5.11), exactly for every $`L`$ on both graphs, $`\Delta\Gamma=-2\Delta g_h`$ and $`\Delta\phi_a=-g_s(\Delta g_s-\Delta g_h)`$. For a pair translated by $`\delta`$, $`\Delta G_{12}=-[\Delta g_h(x_1)+\Delta g_h(x_2)]`$ and $`\Delta\bar\phi=-g_s[\Delta g_s(\bar x)-\Delta g_h(\bar x)]`$. Hence
```math
a_{\rm mark}=\frac{2\bar\phi_a}{g_s\bar\Gamma}\,\frac{\Delta g_h}{\Delta g_s-\Delta g_h},\qquad a_{\rm bond}=\frac{\bar\phi_1+\bar\phi_2}{2g_s\bar G_{12}}\,\frac{\Delta g_h(x_1)+\Delta g_h(x_2)}{\Delta g_s(\bar x)-\Delta g_h(\bar x)}.\qquad\text{(5.27)}
```
On the cubic torus both prefactors are bounded away from $`0`$ and $`\infty`$, uniformly in $`L`$ and in the places:
- $`G_a\ge1/\kappa_a`$ by the triangle inequality for $`r`$ in (5.8), so $`-\phi_a/g_s\ge1/\kappa_a`$ and $`\Gamma,G_{12}\ge1/\kappa_a`$;
- $`G_a(x,y)\le\sqrt{\Gamma(x)\Gamma(y)}`$, and $`\Gamma`$ is bounded uniformly in $`L`$ for $`D=3`$.

So after $`L\to\infty`$, with $`N:=\Delta g_h(x_1)+\Delta g_h(x_2)`$, $`D:=\Delta g_s(\bar x)`$ and $`H:=\Delta g_h(\bar x)`$:
- $`a_{\rm mark}\to0`$ iff $`\Delta g_h/(\Delta g_s-\Delta g_h)\to0`$, i.e. iff $`\Delta g_h/\Delta g_s\to0`$ with $`\Delta g_s\ne0`$ (for $`t:=\Delta g_h/\Delta g_s`$ the ratio is $`t/(1-t)`$);
- $`a_{\rm bond}\to0`$ iff $`N/(D-H)\to0`$. Here the numerator is not the image difference $`H`$ of the denominator. So this is equivalent to $`N/D\to0`$ when also $`H/D\to0`$ (then $`N/(D-H)=(N/D)/(1-H/D)`$), but not in general (pair control below).

Distance from the anchor alone does not suffice. Two sufficient families, both with $`\Delta g_h/\Delta g_s\to0`$, $`H/D\to0`$ and $`N/D\to0`$:
- *(A) Fixed relative placement.* Fix $`x-x_s`$ and $`x'-x_s`$ (for a pair, $`x_j-x_s`$ in both placements) with $`\Delta g_s\ne0`$ (resp. $`\Delta g_s(\bar x)\ne0`$), and move the configuration away from $`h`$ to distance $`d`$. Then $`\Delta g_h=O(\lvert\delta\rvert d^{-2})`$, so $`a_{\rm mark},a_{\rm bond}=O(d^{-2})`$.
- *(B) Non-cancellation.* Let $`y:=\frac12(x+x')`$ be the center of the comparison; for a pair of size $`\lvert\mathbf r\rvert\ll R`$, $`y`$ is the center of its two midpoints. Let $`d:=\lvert y-h\rvert`$, $`R:=\lvert y-x_s\rvert`$, $`\hat e_h:=(y-h)/d`$, $`\hat e_s:=(y-x_s)/R`$ and $`\delta:=x-x'`$. Require $`\lvert\delta\cdot\hat e_s\rvert\ge c\lvert\delta\rvert`$ with a fixed $`c\in(0,1]`$, and $`1\ll R`$, $`\lvert\delta\rvert\ll R\ll d`$.

In (B), the centered expansion of $`g_\infty(x)=\frac1{4\pi\kappa_h\lvert x\rvert}+O(\lvert x\rvert^{-3})`$ gives:
- $`\Delta g_s=-\frac{\delta\cdot\hat e_s}{4\pi\kappa_hR^2}\bigl[1+O(\frac{\lvert\delta\rvert^2+1}{cR^2})\bigr]`$;
- $`\Delta g_h=-\frac{\delta\cdot\hat e_h}{4\pi\kappa_hd^2}+O(\lvert\delta\rvert(\lvert\delta\rvert^2+1)d^{-4})`$, and $`\Delta g_h(x_1)+\Delta g_h(x_2)=2\Delta g_h(y)+O(\lvert\delta\rvert(\lvert\mathbf r\rvert^2+\lvert\delta\rvert^2+1)d^{-4})`$;
- $`-\bar\phi_a/g_s=c_\phi+O(R^{-1})`$, $`\bar\Gamma=\Gamma_\infty+O(d^{-1})`$, $`\bar G_{12}=c_\phi+g_\infty(\mathbf r)+O(d^{-1})`$.

With $`\eta:=R^{-1}+\frac{\lvert\delta\rvert^2+1}{cR^2}+\frac{R^2}{cd^2}`$, (5.27) gives
```math
a_{\rm mark}=-\frac{2c_\phi}{\Gamma_\infty}\,\frac{R^2}{d^2}\,\frac{\delta\cdot\hat e_h}{\delta\cdot\hat e_s}+O\Bigl(\frac{R^2\eta}{cd^2}\Bigr),\qquad\frac{2c_\phi}{\Gamma_\infty}\in(1,2),\qquad\text{(5.23)}
```
```math
a_{\rm bond}=-\frac{2c_\phi}{c_\phi+g_\infty(\mathbf r)}\,\frac{R^2}{d^2}\,\frac{\delta\cdot\hat e_h}{\delta\cdot\hat e_s}+O\Bigl(\frac{R^2\eta}{cd^2}\Bigr),\qquad\text{(5.24)}
```
so both are $`O(R^2/(cd^2))`$. $`\kappa_a`$ enters only through $`c_\phi`$ and $`\Gamma_\infty`$; $`2c_\phi/\Gamma_\infty`$ runs from 2 ($`\kappa_a\to0`$) to 1 ($`\kappa_a\to\infty`$).

*Numbers.* On $`\mathbb Z^3`$ with collinear placements ($`c=1`$; $`R'=3,6`$, $`d=8,\dots,64`$; asymptotics.txt), at $`R'=3`$ $`a_{\rm mark}`$ falls from $`0.24`$ to $`4.6\times10^{-3}`$ and $`a_{\rm bond}`$ from $`0.25`$ to $`5.2\times10^{-3}`$. Their ratios to the leading terms of (5.23), (5.24) reach $`0.91`$ ($`R'=3`$) and $`0.97`$ ($`R'=6`$) at $`d=64`$, within the $`O(\eta)`$ correction. On the tori of the check ($`R'=1`$, $`d=1,2,3`$), $`a_{\rm mark}=0.92,0.47,0.23`$ at $`L=12`$ (weighing.txt).

*Control: the mirror placement* $`h=0`$, $`x=(d,0,0)`$, $`x'=(d+2,0,0)`$, $`x_s=(d+1,R,0)`$. Here $`\Delta g_s=0`$ by reflection, while $`\Delta\phi_a=g_s\Delta g_h\ne0`$, so it is not an excluded member. (5.27) gives $`a_{\rm mark}=-2\bar\phi_a/(g_s\bar\Gamma)\to2[c_\phi+g_\infty((1,R,0))]/\Gamma_\infty`$ as $`d\to\infty`$. The placement has $`\delta\cdot\hat e_s=0`$, so it lies outside (B). On $`\mathbb Z^3`$ ($`R=3`$), $`a_{\rm mark}=1.7634,1.7640,1.7645,1.7647`$ for $`d=8,16,32,64`$, against the limit $`1.7650`$; for $`R=6`$ the limit is $`1.7523`$ (asymptotics.txt). At leading order in $`\varepsilon`$, common square grips there give $`\rho_{\rm mark}\to2.77`$, not 1. Hence, at leading order in $`\varepsilon`$, no grip gives $`\rho_{\rm mark}=1`$ at every comparison: $`a_{\rm mark}`$ tends to 0 in (A) and not at the mirror placement.

*Control: a pair far from a source next to the anchor.* $`h=0`$, $`x_s=e_x`$, $`x_{1,2}=(d,\pm t,0)`$ translated by $`e_x`$, with $`d=n^3`$, $`t=n^4`$, $`n\to\infty`$, so $`\bar x=(d,0,0)`$. With $`A_*:=1/(4\pi\kappa_h)`$ and $`g_\infty`$ of Step 3: $`D\simeq A_*d^{-2}`$, $`D-H`$ is the second difference of $`g_\infty`$ along $`e_x`$ at $`\bar x`$, $`\simeq2A_*d^{-3}`$, and $`N\simeq2A_*d\,t^{-3}=2A_*d^{-3}`$. So $`N/D\to0`$ and $`H/D\to1`$, but $`N/(D-H)\to1`$. As $`t\to\infty`$, $`\bar\phi_j\to-g_s[c_\phi-g_\infty(e_x)]`$ and $`\bar G_{12}\to c_\phi`$, so (5.27) gives $`a_{\rm bond}\to-[c_\phi-g_\infty(e_x)]/c_\phi\ne0`$, while $`m_{\mathbf r}\simeq-d^3/(2t^3)\to0`$. Here $`\Delta\bar\phi=-g_s(D-H)\ne0`$, and (5.26) holds for weak enough grips ($`\Gamma`$ and $`G_{12}`$ are bounded), so this is not an excluded member. The placement lies outside (A) (the $`x_j-x_s`$ are not fixed) and outside (B) ($`\lvert\mathbf r\rvert\gg R\simeq d`$). On $`\mathbb Z^3`$ for $`n=2,\dots,6`$ (asymptotics.txt): $`N/(D-H)=0.703,0.862,0.918,0.946,0.962`$ and $`a_{\rm bond}=-0.669,-0.819,-0.872,-0.898,-0.913`$, against the limit $`-0.9488`$. Over the same range $`N/D`$ falls from $`0.16`$ to $`8.9\times10^{-3}`$, and $`\lvert m_{\mathbf r}\rvert`$ from $`0.017`$ to $`0.0020`$ ($`m_{\mathbf r}<0`$). For common square grips, at leading order in $`\varepsilon`$, $`\rho_{{\rm bond},i}-m_{\mathbf r}=a_{\rm bond}`$ does not vanish there.

*Far from the anchor.* Take the order $`L\to\infty`$, then $`d\to\infty`$, within (A), or within (B) with $`R/d\to0`$ at fixed $`c`$. In the controlled regime ($`\varepsilon\to0`$ for $`F_0^{(i)}\ne0`$; grips with $`F_0=0`$ fail there), (5.22) reduces to the form of (2.18): $`\rho_{\rm mark}=1`$ and $`\rho_{{\rm bond},i}=m_{\mathbf r}`$, for every level and both branches, at order $`\mu^2`$ and leading order in the grip, iff the grips are square with a common $`\hat\beta`$. They then hold in the lowest eigenvector of the stated contract iff (5.10) holds for one body, and (5.26) for the pair, at $`\alpha_i=-2M_{k_i}\lvert F_2^{(i)}\rvert`$. For a pair this is stronger than the one-body conditions $`2M_{k_i}\lvert F_2^{(i)}\rvert\Gamma(x_i)<1`$. Far from the anchor, with equal $`\alpha_i=-a`$, it reads $`a(\Gamma_\infty+c_\phi+g_\infty(\mathbf r))<1`$. The first deviations are:
- at order $`\hat\beta^0`$: $`a_{\rm mark},a_{\rm bond}`$, of order $`d^{-2}`$ in (A) and $`R^2/(cd^2)`$ in (B);
- at the next order in the grip, for $`a=0`$: $`\rho_{\rm mark}-1=\hat\beta^2(\bar w-\frac{\bar\Sigma}{4\bar\Gamma})+O(\hat\beta^4)`$ and $`\rho_{{\rm bond},i}-m_{\mathbf r}=m_{\mathbf r}\hat\beta^2(\bar w(\bar x)-\frac{\bar\Sigma_{12}}{4\bar G_{12}})+O(\hat\beta^4)`$.

*Line (ring, $`L\to\infty`$ first).* Let $`d_x`$ be the distance of $`x`$ to $`h`$, and $`m_x:=\min(d_x,d_s)`$ for $`x`$ on the side of the source ($`m_x:=0`$ on the other side). Then (5.11), (5.13) give $`\phi_a(x)=-g_s(\frac1{\kappa_a}+\frac{m_x}{\kappa_h})`$ and $`\Gamma(x)=\frac1{\kappa_a}+\frac{d_x}{\kappa_h}`$. Also $`G_{12}=\frac1{\kappa_a}+\frac{\min(d_1,d_2)}{\kappa_h}`$ for two places on one side of $`h`$, and $`\frac1{\kappa_a}`$ across. Every comparison with $`\Delta m\ne0`$ ($`\Delta m=0`$ is the excluded $`\Delta\phi_a=0`$) has
```math
a_{\rm mark}=\frac{(\kappa_h/\kappa_a+\bar m)\,\Delta d}{(\kappa_h/\kappa_a+\bar d)\,\Delta m}.\qquad\text{(5.28)}
```
- *Both placements between the anchor and the source* ($`m=d`$ at both): $`a_{\rm mark}=1`$ exactly.
- *Straddling the source* ($`d_{x'}<d_s<d_x`$): $`a_{\rm mark}-1=\frac{vP}{u(P+(u+v)/2)}>0`$, with $`P:=\kappa_h/\kappa_a+d_{x'}`$, $`u:=d_s-d_{x'}`$, $`v:=d_x-d_s`$. Far from the anchor it tends to $`\Delta d/\Delta m-1`$; for example $`x=x_s+1`$, $`x'=x_s-1`$ gives $`a_{\rm mark}\to2`$.
- *Across the anchor* ($`x'`$ on the other side, $`m_{x'}=0<m_x`$): $`a_{\rm mark}`$ has the sign of $`d_x-d_{x'}`$.

The ring closed forms at $`L=4096`$ reproduce (5.28) in all three cases to $`3\times10^{-3}`$, the size of the finite-$`L`$ corrections (asymptotics.txt). For example, $`x=21`$, $`x'=19`$, $`x_s=20`$ gives $`1.9531`$ against $`1.9533`$. At leading order in $`\varepsilon`$, the grip with $`\rho_{\rm mark}=1`$, $`\hat\beta/\hat b=1/(1+a_{\rm mark})`$, therefore depends on the comparison, and no grip gives $`\rho_{\rm mark}=1`$ at every comparison on the line. A pair outside the range below needs (5.21) with the piecewise $`\phi_a`$ and $`G_{12}`$.

For comparisons in which both placements, and both bodies of a pair in both placements, lie between the anchor and the source on its side, $`\phi_a=-g_s\Gamma`$ and $`G_{12}=\Gamma(x_{\rm near})`$, so $`a_{\rm mark}=1`$ exactly and
```math
\rho_{\rm mark}=\frac{2\hat\beta}{\hat b}\bigl(1+O(\varepsilon^2)\bigr),\qquad\rho_{{\rm bond},i}=\Bigl[\frac{\hat\beta_1+\hat\beta_2}{\hat b_i}+\frac{\hat\beta_{\rm far}\,s}{2\hat b_i(\kappa_h/\kappa_a+\bar d_{\rm near})}\Bigr]\bigl(1+O(\varepsilon^2)\bigr),\qquad m_{\mathbf r}=1,\qquad\text{(5.25)}
```
with $`s`$ the separation, $`d_{\rm near}`$ the distance of the nearer body to $`h`$, and $`\hat\beta_{\rm far}`$ the grip of the farther body. In this range:
- square grips give $`\rho_{\rm mark}=2`$;
- $`\rho_{\rm mark}=1`$ at every such comparison iff $`8F_0F_2=F_1^2`$ ($`\hat\beta=\hat b/2`$);
- with a common such grip, $`\rho_{{\rm bond},i}=1+\frac{s}{4(\kappa_h/\kappa_a+\bar d_{\rm near})}`$, which tends to $`m_{\mathbf r}`$ only as $`d_{\rm near}/s\to\infty`$.

All three hold at leading order in $`\varepsilon`$, which here contains $`\lvert F_2/F_0\rvert\bar w\propto\ln d`$. On rings with $`d=10`$, $`R'=3`$: $`a_{\rm mark}=0.53,0.81,0.96,0.990,0.9975`$ for $`L=32,64,256,1024,4096`$ (asymptotics.txt); on the rings of the check the grip $`8F_0F_2=F_1^2`$ gives $`\rho_{\rm mark}=1.008`$ ($`L=32`$, $`d=2`$, $`a_{\rm mark}=0.96`$) and $`0.937`$ ($`L=64`$, $`d=10`$, $`a_{\rm mark}=0.81`$) (weighing.txt).

*Controls.*
- Linear grip ($`F_2=0`$): $`W^{\rm mark}=W_{\rm bond}=0`$ while $`C^{\rm mark},B\ne0`$, so $`\rho_{\rm mark}=\rho_{{\rm bond},i}=0`$ at every place, on both graphs.
- Grips with $`F_0=0`$: $`\rho_{\rm mark},\rho_{{\rm bond},i}=O(\eta_0^2)`$ in their weak-grip regime.
- Square grips, cubic torus: placements with $`d\sim R`$ ($`a=O(1)`$), the mirror placement at every $`d`$, and the pair far from a source next to the anchor ($`a_{\rm bond}\not\to0`$).
- Square grips, line: $`\rho_{\rm mark}=2`$ between the anchor and the source, $`\rho_{\rm mark}>2`$ straddling the source.

## Result

Class: oscillator cells on a ring or cubic torus of side $`L\ge3`$ without pinning, held Model D bodies with grips of class (G2) in a stated eigenvector of $`S`$, held sources; the block of the stated body labels; $`M\to\infty`$ first, in the sense of (5.3).

1. **(5.3)** *Criterion.* A lowest eigenvector exists iff $`A>0`$ in (5.1); otherwise the lowest eigenvalue of $`C_M`$ tends to $`-\infty`$ or to the bottom of a continuum.
2. **(5.4)–(5.6)** *Criterion, item 1 (no anchor).* A lowest eigenvector exists iff $`\mathcal L_n+\mathcal A>0`$; necessary: $`\sum_i\mu_iF_2^{(i)}>0`$. One body with $`F_2\ne0`$: iff $`\sigma={\rm sign}\,F_2`$, every level (otherwise the eigenvalue tends to $`-\infty`$). Two bodies: iff $`\alpha_1+\alpha_2>0`$ and $`\alpha_1\alpha_2+(\alpha_1+\alpha_2)/r_{12}>0`$. If no body has $`F_2\ne0`$ there is none ($`-\infty`$ if $`\sum_i\mu_iF_1^{(i)}+\sum_sg_s\ne0`$, a free uniform change otherwise); the field alone has none, so the cost of a body is undefined. The whole contract (all blocks) has none, for any bodies of (G2).
3. **(5.7)** *Negative.* A body with $`\mu F_2>0`$ (branch $`\sigma={\rm sign}\,F_2`$, every level) acts as an anchor of strength $`2\mu F_2`$ at its own place; alone, its $`g_s`$-linear cost is $`-F_1g_s/(2F_2)`$ at every place (no weight), and its cost has no expansion in $`s`$.
4. **(5.8), (5.9)** *Formula.* $`G_a(x,y)=\frac1{\kappa_a}+\frac12[r(x,h)+r(y,h)-r(x,y)]`$, exact for every $`L`$ on both graphs, with $`G_a(h,\cdot)=1/\kappa_a`$, ring $`r=\frac{s(L-s)}{\kappa_hL}`$; the resolvent (5.9).
5. **(5.10)** *Criterion, item 2.* With the anchor, a lowest eigenvector exists iff $`\Gamma_n^{-1}+\mathcal A>0`$; one body: iff $`1+2\mu F_2\Gamma(x)>0`$, $`\Gamma(x)=\frac1{\kappa_a}+r(x,h)`$, i.e. (2.5) with $`G_0\to\Gamma(x)`$. It holds whenever all $`\mu_iF_2^{(i)}\ge0`$. For $`\mu F_2<0`$ it fails on the ring once $`\frac{d(L-d)}{\kappa_hL}\ge\frac1{2M_k\lvert F_2\rvert}-\frac1{\kappa_a}`$, and on the cubic torus ($`L\to\infty`$) it holds at every place iff $`2M_k\lvert F_2\rvert\Gamma_\infty\le1`$, $`\Gamma_\infty=\frac1{\kappa_a}+\frac{2\gamma_3}{\kappa_h}`$.
   - **(5.26)** *Criterion.* Two bodies: a lowest eigenvector exists iff $`(1+\alpha_1\Gamma(x_1))(1+\alpha_2\Gamma(x_2))>\alpha_1\alpha_2G_{12}^2`$ and $`\Gamma(x_1)+\Gamma(x_2)+(\alpha_1+\alpha_2)(\Gamma(x_1)\Gamma(x_2)-G_{12}^2)>0`$. Sufficient: $`\bar a(\max_i\Gamma(x_i)+G_{12})<1`$. Two bodies that each meet the one-body condition need not meet it. With $`\alpha_1=\alpha_2=-a`$ and equal $`\Gamma`$, the pair needs $`a(\Gamma+G_{12})<1`$, each body alone only $`a\Gamma<1`$; on the cubic torus far from the anchor, $`G_{12}\to c_\phi+g_\infty(\mathbf r)\ge c_\phi`$ at every separation.
6. **(5.11)** *Formula.* Made field $`\phi_a(x)=-g_sG_a(x,x_s)`$: a uniform shift $`-g_s[\frac1{\kappa_a}+\frac12r(x_s,h)]`$ plus $`-\frac{g_s}2[r(x,h)-r(x,x_s)]`$. Cubic, $`L\to\infty`$: source plus an opposite image at the anchor, over the constant $`-g_s[c_\phi-g_\infty(x_s-h)]`$. Line: $`-g_s[\frac1{\kappa_a}+\frac{\min(d_x,d_s)}{\kappa_h}]`$ on one side of $`h`$, $`-g_s/\kappa_a`$ across.
7. **(5.12), (5.13)** *Formula.* Field constants $`\Gamma`$, $`G_a`$, $`w`$, $`\Sigma`$. Line ($`L\to\infty`$): $`\Gamma=\frac1{\kappa_a}+\frac d{\kappa_h}`$, $`w=\frac{\ln d}{2\pi\sqrt{\kappa_h}}+O(1)`$, $`\Sigma(x,x)=\frac{2\ln2}{\pi\kappa_h^{3/2}}d(1+o(1))`$. Cubic ($`L\to\infty`$, then $`d\to\infty`$): $`\Gamma\to\Gamma_\infty`$ and $`G_a(x,y)\to c_\phi+g_\infty(x-y)`$, which differ from the unanchored values; $`w,\Sigma`$ tend to the unanchored values with corrections $`O(d^{-3})`$.
8. **(5.14), (5.15)** *Formula and theorem, item 3.* $`\mathcal E_{12}=-g_1g_2G_a(x_1,x_2)`$, exact; constant if one source is at $`h`$. Cubic torus, $`L\to\infty`$ first: the image form (5.15), error $`O(\ell^{-3})`$. The separation dependence is $`-\frac{g_1g_2}{4\pi\kappa_h\lvert\mathbf r\rvert}`$, the coefficient of the unanchored field, when $`\lvert\mathbf r\rvert/D_X\to0`$ (order (a); uniformly for $`1\ll\lvert\mathbf r\rvert\ll D_X`$ with relative error $`O(\lvert\mathbf r\rvert^3/D_X^3)+O(\lvert\mathbf r\rvert^{-2})`$). With one source at a fixed place it falls as $`\lvert\mathbf r\rvert^{-2}`$ or faster (order (b)). At fixed midpoint it is $`+\frac{3g_1g_2}{4\pi\kappa_h\lvert\mathbf r\rvert}`$ (order (c)). $`L\to\infty`$ must come before both other limits.
9. **(5.16)** *Negative (control).* On the ring the mutual cost is a quadratic polynomial in the distances, for $`L\to\infty`$ independent of the separation at fixed distance of the nearer source: it falls as the inverse separation in no order of the limits.
10. **(5.17), (5.18)** *Formula, item 4.* Exact cost and $`g_s`$-linear cost of one body under (5.10). At order $`s`$ and $`s^2`$: $`C^{(1)}=\mu(F_0+F_2w)`$, $`C^{\rm mark}=-\frac{\mu^2}2(F_1^2\Gamma+F_2^2\Sigma)`$, $`W^{(1)}=\mu F_1\phi_a`$, $`W^{\rm mark}=-2\mu^2F_1F_2\Gamma\phi_a`$, at the body's place. At leading order in the grip, at every place: $`W^{(1)}=2\hat bC^{(1)}\phi_a`$ and $`W^{\rm mark}=2\hat\beta C^{\rm mark}\phi_a`$.
11. **(5.19)** *Formula.* Bond and its weight at order $`s^2`$ and first order in $`g_s`$: $`B=-\mu_1\mu_2[F_1^{(1)}F_1^{(2)}G_{12}+F_2^{(1)}F_2^{(2)}\Sigma_{12}]`$, $`W_{\rm bond}=-\mu_1\mu_2F_1^{(1)}F_1^{(2)}G_{12}\Psi`$.
12. **(5.20), (5.21)** *Formula.* $`\rho_{\rm mark}`$ and $`\rho_{{\rm bond},i}`$, exact at order $`s^2`$, independent of level and branch, with the excluded members of Step 8. As $`s`$-coefficients they are defined for every member. They refer to the lowest eigenvector of the stated contract iff (5.10) holds at $`s=1`$ ((5.26) for a pair), at $`\alpha_i=-2M_{k_i}\lvert F_2^{(i)}\rvert`$ when every level up to $`k_i`$ and both branches are claimed.
13. **(5.22)** *Criterion.* In the controlled regime, $`F_0^{(i)}\ne0`$ and $`\varepsilon^2:=\max_i(\lvert F_2^{(i)}\rvert\bar w/\lvert F_0^{(i)}\rvert,\hat\beta_i^2\bar\Sigma/\bar\Gamma,\lvert\hat\beta_1\hat\beta_2\rvert\bar\Sigma_{12}/\bar G_{12})\ll1`$: $`\rho_{\rm mark}=\frac{\hat\beta}{\hat b}(1+a_{\rm mark})(1+O(\varepsilon^2))`$, and $`\rho_{{\rm bond},i}`$ is the bracket of (5.22) times $`1+O(\varepsilon^2)`$. For placements with $`\Delta\Gamma=\Delta G_{12}=0`$ these are the conditions of (2.18) with $`G_0\to\Gamma`$, $`w_0\to w`$. Grips with $`F_0=0`$ give $`\rho_{\rm mark},\rho_{{\rm bond},i}=O(\eta_0^2)`$ in their weak-grip regime $`\eta_0\ll1`$: they do not weigh.
14. **(5.27), (5.23), (5.24)** *Formula and theorem.* Exactly, $`a_{\rm mark}`$ is the image difference $`\Delta g_h`$ over $`\Delta g_s-\Delta g_h`$ at the body, and $`a_{\rm bond}`$ is $`N=\Delta g_h(x_1)+\Delta g_h(x_2)`$ over $`D-H=\Delta g_s(\bar x)-\Delta g_h(\bar x)`$ at the midpoint, each times a prefactor bounded away from 0 and $`\infty`$ on the cubic torus. After $`L\to\infty`$, $`a_{\rm mark}\to0`$ iff $`\Delta g_h/\Delta g_s\to0`$ (with $`\Delta g_s\ne0`$), and $`a_{\rm bond}\to0`$ iff $`N/(D-H)\to0`$; the latter is equivalent to $`N/D\to0`$ when also $`H/D\to0`$, not in general. Distance from the anchor alone does not suffice. Two sufficient families, both with $`H/D\to0`$:
    - (A) fixed relative placement with $`\Delta g_s\ne0`$: $`a=O(d^{-2})`$;
    - (B) non-cancellation $`\lvert\delta\cdot\hat e_s\rvert\ge c\lvert\delta\rvert`$ at the center of the comparison, $`1\ll R`$, $`\lvert\delta\rvert\ll R\ll d`$: (5.23), (5.24), with $`a=O(R^2/(cd^2))`$.

    Take the order $`L\to\infty`$, then $`d\to\infty`$, within (A), or within (B) with $`R/d\to0`$ at fixed $`c`$, in the controlled regime. Then $`\rho_{\rm mark}=1`$ and $`\rho_{{\rm bond},i}=m_{\mathbf r}`$, for every level and both branches, at order $`\mu^2`$ and leading order in the grip, iff the grips are square with a common $`\hat\beta`$. They hold in the lowest eigenvector of the stated contract iff in addition (5.10) holds for one body, and (5.26) for the pair, at $`\alpha_i=-2M_{k_i}\lvert F_2^{(i)}\rvert`$; for a pair this is stronger than the one-body conditions. The first deviations are $`a_{\rm mark},a_{\rm bond}`$ and, at the next order in the grip, $`\hat\beta^2(\bar w-\frac{\bar\Sigma}{4\bar\Gamma})`$ and $`m_{\mathbf r}\hat\beta^2(\bar w(\bar x)-\frac{\bar\Sigma_{12}}{4\bar G_{12}})`$. *Controls:* at the mirror placement ($`\Delta g_s=0`$), $`a_{\rm mark}\to2[c_\phi+g_\infty((1,R,0))]/\Gamma_\infty\ne0`$ at every $`d`$. The pair with $`x_s-h=e_x`$, $`x_{1,2}-h=(n^3,\pm n^4,0)`$ has $`N/D\to0`$ but $`a_{\rm bond}\to-[c_\phi-g_\infty(e_x)]/c_\phi\ne0`$ as $`n\to\infty`$. At leading order in $`\varepsilon`$, no grip gives $`\rho_{\rm mark}=1`$ at every comparison.
15. **(5.28), (5.25)** *Formula, criterion and negative.* Line ($`L\to\infty`$ first): every comparison with $`\Delta m\ne0`$ has $`a_{\rm mark}=\frac{(\kappa_h/\kappa_a+\bar m)\Delta d}{(\kappa_h/\kappa_a+\bar d)\Delta m}`$. This equals 1 between the anchor and the source, is $`>1`$ straddling the source, and has the sign of $`d_x-d_{x'}`$ across the anchor. At leading order in $`\varepsilon`$, no grip gives $`\rho_{\rm mark}=1`$ at every comparison. For comparisons with both placements (both bodies of a pair in both placements) between the anchor and the source, at leading order in $`\varepsilon`$:
    - square grips give $`\rho_{\rm mark}=2`$;
    - $`\rho_{\rm mark}=1`$ iff $`8F_0F_2=F_1^2`$;
    - with that common grip, $`\rho_{{\rm bond},i}=1+\frac{s}{4(\kappa_h/\kappa_a+\bar d_{\rm near})}`$, which tends to $`m_{\mathbf r}=1`$ only for $`d_{\rm near}/s\to\infty`$.
16. *Control.* Linear grip: $`\rho_{\rm mark}=\rho_{{\rm bond},i}=0`$ at every place, every $`L`$, on both graphs. Grips with $`F_0=0`$: both ratios are $`O(\eta_0^2)`$ in their weak-grip regime.

## Consistency checks

1. *Limits of the anchor strength.* $`\kappa_a\to\infty`$: (5.8) becomes $`g(x-y)-g(x-h)-g(y-h)+g(0)`$, which vanishes for $`x=h`$: the cell at $`h`$ is held at $`q_h=0`$, and $`\phi_a(h)=-g_s/\kappa_a\to0`$. $`\kappa_a\to0`$ through positive values: $`\Gamma=\frac1{\kappa_a}+r(x,h)\to\infty`$. For $`F_2\ne0`$, (5.10) holds for all small $`\kappa_a`$ iff $`\mu F_2>0`$, the criterion (5.5) without an anchor. For a linear grip ($`F_2=0`$), (5.10) holds at every $`\kappa_a>0`$, while at $`\kappa_a=0`$ Step 2 gives no lowest eigenvector ($`b\cdot\mathbf 1=\mu F_1\ne0`$). The anchored lowest eigenvectors have no normalizable limit: their mean shift is $`\langle q_y\rangle=-\mu F_1G_a(y,x)=-\mu F_1/\kappa_a+O(1)`$, and the variance $`\frac12(K_a^{-1/2})_{yy}`$ diverges, because the lowest eigenvalue of $`K_a`$ is at most $`\kappa_a/L^D`$, with an eigenvector tending to the uniform one. Their eigenvalue $`c_0+\frac12{\rm Tr}\sqrt{K_a}-\frac12\mu^2F_1^2\Gamma(x)\to-\infty`$, as Step 2 states for $`\kappa_a=0`$. So the criterion at $`\kappa_a=0`$ is that of Step 2, not the limit of (5.10). Passed.
2. *Comparison with 02-grip-weight.* (5.10) is (2.5) with $`G_0\to\Gamma(x)`$; for $`a_{\rm mark}=a_{\rm bond}=0`$ (placements with $`\Delta\Gamma=\Delta G_{12}=0`$, or the far-anchor limit of the families (A), (B) of Step 8 on the cubic torus) (5.22) gives exactly the conditions of (2.18). Passed.
3. *Dimensions.* $`[p]^2=`$ cost $`E`$, $`[q]^2=E^{-1}`$; $`[\kappa_h]=[\kappa_a]=E^2`$, $`[G_a]=[\Gamma]=E^{-2}`$, $`[g_s]=E^{3/2}`$, $`[\mu]=E`$, $`[F_1]=E^{1/2}`$, $`[F_2]=E`$, $`[\Sigma]=E^{-3}`$: $`g_1g_2G_a`$, $`\mu^2F_1^2\Gamma`$, $`\mu F_2w`$ are costs; $`\mu F_2\Gamma`$, $`a_{\rm mark}`$, $`\hat\beta^2w`$, $`\hat\beta^2\Sigma/\Gamma`$ are pure numbers; $`\ln d/\sqrt{\kappa_h}`$ and $`d/\kappa_h^{3/2}`$ have the units of $`w`$ and $`\Sigma`$. Passed.

## Open issues

- The ratios use differences between placements with means of the place-dependent costs (the definitions of 02-grip-weight extended). The anchor terms $`a_{\rm mark},a_{\rm bond}`$ come from that extension, while the place-wise relation of Step 6 holds at every place. Which notion of weighing the programme adopts with an anchor is a choice for the main model.
- Finite-$`L`$ corrections to (5.15) are not derived in closed form (only $`L\to\infty`$ first; the tori of the check show them).
- $`w_\infty`$ and $`\Sigma_\infty`$ are not evaluated; the $`O(1)`$ and $`o(1)`$ terms of (5.13) on the line are not derived.
- Out of scope: formation of the mark with an anchor, moving bodies and inertia, cells with finitely many places, other anchors, typicality (item 6).

## Code

- `code/v3/check_anchor.py` (role: check). It computes the exact lowest eigenvalue (5.2) of the uncompressed quadratic contract and compares it with the closed forms.
  - Method: dense linear algebra ($`\frac12{\rm Tr}\sqrt A`$ from all eigenvalues) or sparse linear algebra. The Green function $`g`$ is computed independently by FFT, and $`g_\infty`$ by a Bessel integral. Small differences of $`g_\infty`$ (the pair control of (5.27)) come from one Bessel integral of the combined integrand.
  - Parameters: $`\kappa_h=1`$, $`\kappa_a=0.7`$, $`M_k\in\{1,1.5\}`$. The $`s`$-coefficients come from a five-point stencil (step 0.01). The $`g_s`$-linear part is exact (antisymmetric part in $`g_s=\pm1`$).

  Outputs:
  - `code/v3/output/existence.txt`: (i) $`\lambda_{\min}(A)`$ against (5.5), (5.6) and (5.10), and against (5.10), (5.26) for random pairs. For each lattice, a pair whose bodies meet the one-body condition while the pair violates (5.26). Rings $`L=32,64`$, tori $`L=8,12`$.
  - `code/v3/output/mutual_cost.txt`: (ii) $`\mathcal E_{12}`$ against (5.14), (5.15), (5.16) versus the separation, at midpoint distances 0 and 6 from the anchor. Rings $`L=64,256`$, tori $`L=16,32`$.
  - `code/v3/output/weighing.txt`: (iii) $`C^{(1)},C^{\rm mark},W^{(1)},W^{\rm mark}`$ against (5.18), and $`\rho_{\rm mark}`$ against (5.20), with the leading form (5.22), for square, non-square, $`8F_0F_2=F_1^2`$ and linear grips. Bonds $`B`$, $`W_{\rm bond}`$ against (5.19), and $`\rho_{{\rm bond},i}`$ against (5.21) and (5.22), for common square grips (five level and branch combinations), common non-square, $`8F_0F_2=F_1^2`$ and linear grips, and a mixed (square, non-square) pair (two combinations each). Existence at $`s=1`$ by (5.10), and for pairs $`\lambda_{\min}`$ against (5.26). Two levels, both branches, three distances; rings $`L=32,64`$, tori $`L=8,12`$; maximal deviations per lattice.
  - `code/v3/output/asymptotics.txt`: $`\gamma_3`$ and $`g_\infty`$; the orders of (5.15) on $`\mathbb Z^3`$; (5.23), (5.24) for collinear placements; the mirror placement of (5.27); the pair control of (5.27) ($`N/D`$, $`H/D`$, $`N/(D-H)`$, $`m_{\mathbf r}`$, $`a_{\rm bond}`$ for $`n=2,\dots,6`$); the line limit $`a_{\rm mark}\to1`$; (5.28) against the ring closed forms; (5.13) on the line.

## Methods used

- Gaussian lowest eigenvector of a quadratic contract; min-max and compressions
- Schur complement (Kron reduction), constrained quadratic minimum
- Pseudo-inverse of the graph Laplacian, resistance distance, M-matrices
- Sherman–Morrison formula and matrix determinant lemma; resolvent integral representations
- Lattice Green functions on tori and $`\mathbb Z^3`$ and their asymptotics; image form
- Perturbative expansion in the grip strength; numerical linear algebra (check)
