# Inertia of a body with its own mark in a weakly pinned field of oscillator cells

- **Subproject:** 08-ilang-propagation
- **Package:** 06-mark-inertia
- **Version:** v2
- **Mode:** internal regeneration
- **Date:** 2026-10-25

## Changes from previous version

- New Step 10 and results (6.13)–(6.15): on the cubic torus, items 2 and 3 are now settled outside the large-$`\varepsilon_k`$ regime of (6.10), from the lattice sums of (6.3), which are evaluated numerically (`code/v2/torus_mark_inertia.py`); the size of $`\varepsilon_kR`$ where (U) holds is given (review I1).
- Step 8, "$`D=3`$ otherwise", and Step 9(b): now point to Step 10 (review I1).
- Step 9(a) and Result (6.11): for the linear grip, the first dependence on the level comes from $`I^{\rm mark}`$ at the next order, via (6.12) (review I2).
- Open issues: the item on the cubic torus is replaced by the limits of the numerical evaluation. Code: the v1 check is re-run unchanged in `code/v2/`, and the numbers of Steps 6 and 7 are cited from there.

## Setup and assumptions

- **Description** (assumptions, M8, M9, A11, A15), as in the question. Oscillator cells on the ring ($`D=1`$) or the cubic torus ($`D=3`$) of side $`L`$, $`\Phi_y=q_y`$, $`c_0=\sqrt{\kappa_h}`$, $`\ell=c_0/m_h`$. One Model D body with own contract $`A`$ only and the grip $`\sum_x\lvert x\rangle\langle x\rvert\otimes S\otimes F(q_{x\mathbf e_1})`$, $`S=\sigma_3\otimes(m\mathbb 1_N+D)`$, $`F=F_0+F_1q+F_2q^2`$, $`F_0>0`$, $`F_1\neq0`$; its chain runs over the cells $`x\mathbf e_1`$. State: the level $`E_{k,\sigma}(P)`$ connected to branch $`\sigma`$, clock level $`k`$, field in its lowest eigenvector. Speeds: $`v_{\max}=\tau`$ cells per unit $`\lambda`$ ((5.11) of 04-ilang-time/05-moving-clock with $`k=1`$), field speed $`c_0`$ ((4.17)), $`r:=\tau/c_0`$. The speeds are equal iff $`r=1`$, which is a condition on the description (M7).
- **Notation.** $`\varepsilon_k:=F_0M_k`$, with $`M_k`$ of (6.7) of 04-ilang-time/06-inertia-internal-energy, and $`\bar F:=F_0+F_2w_0`$. $`\omega_k(p):=\sqrt{\varepsilon_k^2+\tau^2\sin^2p}`$, $`\theta_k(p):=\arctan(\tau\sin p/\varepsilon_k)`$. Modes $`q\in(2\pi/L)\mathbb Z_L^D`$, $`\Omega_q^2:=m_h^2+2\kappa_h\sum_{i=1}^D(1-\cos q_i)`$, $`c_q^2:=1/(2L^D\Omega_q)`$, $`\Omega_{\max}:=\sqrt{m_h^2+4D\kappa_h}`$. Then the quantities of (2.6) are $`G_0=\sum_q2c_q^2/\Omega_q`$, $`w_0=\sum_qc_q^2`$, $`\Gamma(t)=\sum_qc_q^2e^{-\Omega_qt}`$ and $`J_2=\sum_{q,q'}c_q^2c_{q'}^2/(\Omega_q+\Omega_{q'})`$. The index $`k`$ is dropped where this is unambiguous. For a function $`f(E,Q)`$ we use the spectral sum of the grip and a ratio $`R`$ built from it:
```math
\langle\!\langle f\rangle\!\rangle:=F_1^2\sum_qc_q^2f(\Omega_q,q_1)+2F_2^2\sum_{q,q'}c_q^2c_{q'}^2f(\Omega_q+\Omega_{q'},q_1+q_1'),\qquad R:=\frac{\langle\!\langle\sin^2Q/E^2\rangle\!\rangle}{\langle\!\langle1/E\rangle\!\rangle}>0 .
\qquad\text{(6.1)}
```
- **Inputs** (as quoted in the question). From (2.6) of 08-ilang-propagation/02-grip-weight@v3, with $`\mu=\sigma M_k`$: $`C^{(1)}=\mu\langle F\rangle_0`$, $`C^{\rm mark}=-\frac{\mu^2G_0}{2D_\mu}(F_1^2+\zeta)`$, $`\zeta=\frac{4F_2^2J_2}{G_0}[1+O(\mu F_2G_0)]`$. From (2.8): $`W(x)-W(x')=\mu F_1\Delta\phi/D_\mu`$, with $`D_\mu=1+2\mu F_2G_0`$. Also (2.18) (the square grip $`4F_0F_2=F_1^2`$), (4.17), (5.11), and (6.7) of 04-ilang-time/06-inertia-internal-energy ($`\omega_k''(0)=\tau^2/M_k`$ for the bare body).
- **Order.** Expansion in $`\delta F`$ at fixed $`F_0`$, with $`F_1`$ and $`F_2`$ counted alike except in Step 9(b). It needs $`M_k\lvert F_2\rvert G_0\ll1`$ and $`M_kF_1^2G_0\ll F_0`$. On the ring $`G_0\propto\ell`$, so the statements at $`\ell\gg1`$ concern the coefficients; at fixed $`\delta F`$ they need $`M_k(F_1^2+F_2^2/2c_0)\,\ell\ll c_0^2F_0`$.
- **Limits.**
  - $`M\to\infty`$ first, at fixed $`L`$ and order by order in $`\delta F`$. The coefficients below are built from the lowest eigenvector of the field, its one- and two-quantum excitations and the matrix elements of $`q_0`$ and $`q_0^2`$, which are vectors and matrix elements with finitely many quanta. Those of $`C_M`$ tend to them as $`M\to\infty`$.
  - Then $`L\gg\ell`$. The lattice sums then differ from their values at $`L=\infty`$ by terms exponentially small in $`L/\ell`$ (Poisson summation: the summands are analytic in a strip of width of order $`1/\ell`$).
  - Then $`\ell\gg1`$, at fixed $`\tau`$, $`c_0`$ and $`\varepsilon_k`$.
- **Joint label.** At finite $`L`$ the allowed labels are $`P\in(2\pi/L)\mathbb Z_L`$. The expressions below are analytic in real $`P`$ and give the levels at these values. $`E''(0)`$ denotes the second derivative of this function.
- **Weights.** Those of (2.8), without corrections in $`\tau`$ (approximation allowed by the question).

## Derivation

### Step 1. Conserved labels and zeroth order

- **Clock level.** The clock operator $`D`$ (not the dimension) is diagonal in $`\lvert f_k\rangle`$, and every term of $`C`$ acts on the clock through $`\mathbb 1_N`$ or $`D`$. The clock level $`k`$ is therefore conserved, and $`S=M_k\sigma_3`$ in it.
- **Joint label and parity.** The joint translation (body $`x\to x+1`$, cells $`y\to y+\mathbf e_1`$) commutes with $`A`$, with the grip and with $`H`$, so $`P`$ is conserved. Reflect $`x\to-x`$ for the body and the cells together, and conjugate the branch by $`\sigma_3`$. This keeps $`A`$, $`S`$ and $`H`$ and maps $`P\to-P`$, so $`E_{k,\sigma}(P)`$ is even in $`P`$.
- **Body bands.** With $`\lvert p\rangle=L^{-1/2}\sum_xe^{ipx}\lvert x\rangle`$, $`A=\sum_p\lvert p\rangle\langle p\rvert\otimes(-\tau\sin p\,\sigma_1)`$. At $`\delta F=0`$, in level $`k`$, the body block is $`\omega(p)(\cos\theta_p\,\sigma_3-\sin\theta_p\,\sigma_1)`$. Its bands are $`\sigma\omega(p)`$, with eigenvectors $`u_+=(\cos\frac{\theta_p}2,-\sin\frac{\theta_p}2)`$ and $`u_-=(\sin\frac{\theta_p}2,\cos\frac{\theta_p}2)`$, and $`\omega''(0)=\tau^2/\varepsilon_k`$.
- **Field.** $`H=E_f+\sum_q\Omega_qa_q^\dagger a_q`$ and $`q_y=\sum_qc_q(a_qe^{iq\cdot y}+a_q^\dagger e^{-iq\cdot y})`$. The eigenvectors $`\lvert n\rangle`$ of $`H`$ have energies $`E_f+E_n`$ and momenta $`Q_n`$ along $`\mathbf e_1`$.
- **Unperturbed sector.** In the sector $`P`$ the eigenvectors at $`\delta F=0`$ are $`\lvert P-Q_n,\sigma'\rangle\lvert n\rangle`$, with energies $`\sigma'\omega(P-Q_n)+E_f+E_n`$.
- **Matrix elements of $`\sigma_3`$.** Multiplying out, with $`\vartheta=\frac12(\theta_p+\theta_{p'})`$: $`\lvert\langle u_\sigma(p')\vert\sigma_3\vert u_\sigma(p)\rangle\rvert^2=\cos^2\vartheta`$ and $`\lvert\langle u_{-\sigma}(p')\vert\sigma_3\vert u_\sigma(p)\rangle\rvert^2=\sin^2\vartheta`$.

### Step 2. The level at second order

By Wick's theorem, $`q_y^2=w_0+{:}q_y^2{:}`$. The grip is therefore $`\bar F S+V'`$, with $`V'=\sum_x\lvert x\rangle\langle x\rvert\otimes S\otimes O_x`$ and $`O_x:=F_1q_x+F_2{:}q_x^2{:}`$. The term $`\bar FS`$ replaces $`\varepsilon_k`$ by $`M_k\bar F`$ exactly.
- $`O_x\lvert0\rangle`$ has only one- and two-quantum components, and $`\langle n\vert O_x\vert0\rangle=e^{-iQ_nx}\langle n\vert O_0\vert0\rangle`$. Hence $`\langle P-Q_n,\sigma';n\vert V'\vert P,\sigma;0\rangle=M_k\langle u_{\sigma'}(P-Q_n)\vert\sigma_3\vert u_\sigma(P)\rangle\langle n\vert O_0\vert0\rangle`$.
- The weights are $`\lvert\langle q\vert O_0\vert0\rangle\rvert^2=F_1^2c_q^2`$ for one quantum. The two-quantum states of a pair of modes carry $`2F_2^2c_q^2c_{q'}^2`$, summed over ordered pairs; this follows from $`\langle0\vert{:}q_0^2{:}\,e^{-(H-E_f)t}\,{:}q_0^2{:}\vert0\rangle=2\Gamma(t)^2`$.
- Second-order perturbation theory for the isolated level (Step 3) then gives (6.2) and (6.3). The energy denominators are taken at $`F_0`$; the difference is $`O(\delta F^3)`$. Both expressions hold on both graphs and for every $`L`$.
```math
E_{k,\sigma}(P)=E_f+\sigma\sqrt{M_k^2\bar F^2+\tau^2\sin^2P}+E^{(2)}_{k,\sigma}(P)+O(\delta F^3),
\qquad\text{(6.2)}
```
```math
E^{(2)}_{k,\sigma}(P)=-M_k^2\Bigl\langle\!\!\Bigl\langle\frac{\cos^2\vartheta}{E+\sigma[\omega(P-Q)-\omega(P)]}+\frac{\sin^2\vartheta}{E-\sigma[\omega(P-Q)+\omega(P)]}\Bigr\rangle\!\!\Bigr\rangle,\qquad\vartheta=\tfrac12[\theta(P)+\theta(P-Q)].
\qquad\text{(6.3)}
```
The first fraction has the intermediate body in its own branch, the second in the other branch.

### Step 3. Isolation and analyticity

**Branch $`\sigma=-1`$.**
- *Sufficient condition.* Since $`2(1-\cos q_1)\ge\sin^2q_1`$, $`\Omega_q^2\ge m_h^2+\kappa_h\sin^2q_1`$. If $`\tau^2\le2\varepsilon_kc_0`$, then $`\omega(q_1)-\varepsilon_k=\tau^2\sin^2q_1/(\omega+\varepsilon_k)\le\tau^2\lvert\sin q_1\rvert/2\varepsilon_k\le c_0\lvert\sin q_1\rvert<\Omega_q`$, because $`m_h>0`$.
- *Several quanta.* $`\Omega`$ is subadditive in the momentum. The map $`q\mapsto(2\lvert\sin\frac{q_i}2\rvert)_i`$ is componentwise subadditive, and $`\sqrt{m_h^2+x^2}`$ is increasing and subadditive. Hence a state with $`n\ge1`$ quanta and total momentum $`Q`$ has $`E_n\ge\Omega_Q`$.
- *Conclusion.* At $`\delta F=0`$, $`-\varepsilon_k`$ is the lowest level of the sector $`(k,P=0)`$, separated by a gap. It stays isolated for $`P`$ near 0 and small $`\delta F`$, and is therefore analytic in $`P`$ and $`\delta F`$ (isolated eigenvalue of an analytic family).

**Branch $`\sigma=+1`$.**
- *Own-branch denominators.* They exceed $`m_h-[\omega(P)-\varepsilon_k]>0`$ for $`P`$ near 0.
- *Other-branch denominators.* They are $`E_n-\omega(P-Q_n)-\omega(P)`$. Condition (U): the continuous functions $`q\mapsto\Omega_q-\varepsilon_k-\omega(q_1)`$ and, if $`F_2\ne0`$, $`(q,q')\mapsto\Omega_q+\Omega_{q'}-\varepsilon_k-\omega(q_1+q_1')`$ have no zero on the Brillouin zone. Under (U) these denominators are nonzero near $`P=0`$, uniformly in $`L`$. A sufficient condition is $`\Omega_{\max}<\varepsilon_k`$, or $`\Omega_{\max}<2\varepsilon_k`$ if $`F_2=0`$.
- *If one of these functions changes sign.* For $`L\to\infty`$ the level then lies inside a one- or two-quantum continuum of the other branch. It couples to that continuum with weight $`\sin^2\vartheta`$, which is nonzero on an open set ($`\tau>0`$), so it is not isolated at second order.
- *Several quanta.* States with three or more quanta of the other branch may be degenerate with the level; they enter at $`O(\delta F^4)`$.
```math
\sigma=-1:\ \ \Omega_q>\omega_k(q_1)-\varepsilon_k\ \forall q\ \ (\Leftarrow\ \tau^2\le2\varepsilon_kc_0);\qquad\sigma=+1:\ \ \text{(U)}\ \ (\Leftarrow\ \Omega_{\max}<\varepsilon_k,\ \text{or }\Omega_{\max}<2\varepsilon_k\text{ if }F_2=0).
\qquad\text{(6.4)}
```

### Step 4. Cost

At $`P=0`$ the zero-quantum term of (6.2) is exactly $`\sigma M_k\bar F`$, and $`\vartheta=-\theta(Q)/2`$. For the expansion in $`\tau^2`$, use $`\cos^2\vartheta=1-\tau^2\sin^2Q/4\varepsilon^2`$, $`\sin^2\vartheta=\tau^2\sin^2Q/4\varepsilon^2`$, $`\omega(Q)-\varepsilon=\tau^2\sin^2Q/2\varepsilon`$ and $`\omega(Q)+\varepsilon=2\varepsilon`$, each up to $`O(\tau^4)`$. Combining the three resulting terms of first order in $`\tau^2`$ gives
```math
C^{(1)}_{k,\sigma}=\sigma M_k\bar F,\qquad C^{\rm mark}_{k,\sigma}=E^{(2)}_{k,\sigma}(0)=-M_k^2\Bigl(\frac{F_1^2G_0}2+2F_2^2J_2\Bigr)(1+\delta_C),\qquad\delta_C=\tau^2\frac{\langle\!\langle\sin^2Q/[E^2(E-2\sigma\varepsilon_k)]\rangle\!\rangle}{\langle\!\langle1/E\rangle\!\rangle}+O(\tau^4).
\qquad\text{(6.5)}
```
The prefactor $`-M_k^2\langle\!\langle1/E\rangle\!\rangle`$ is the held mark, i.e. the second-order part of (2.6). It is strictly negative because $`F_1\ne0`$.

### Step 5. Inertia: first-order part and mark

From (6.2), $`E''(0)=\sigma\tau^2/(M_k\bar F)+E^{(2)\prime\prime}(0)`$. The inverse of the first term is exactly linear in $`\delta F`$, and the second term is of second order. Expanding $`I=1/E''`$ gives (6.6), on both graphs and for every $`L`$, $`\ell`$ and $`r>0`$. At $`\tau=0`$ (held body) $`E''=0`$, and the inertia is not defined.
```math
I^{(1)}_{k,\sigma}=\frac{\sigma M_k\bar F}{\tau^2}=\frac{C^{(1)}_{k,\sigma}}{\tau^2},\qquad I^{\rm mark}_{k,\sigma}=-\frac{\varepsilon_k^2}{\tau^4}\,E^{(2)\prime\prime}_{k,\sigma}(0),\qquad\rho_{k,\sigma}:=\frac{\tau^2I^{\rm mark}_{k,\sigma}}{C^{\rm mark}_{k,\sigma}} .
\qquad\text{(6.6)}
```
Since $`C^{(1)}\ne0`$, $`I^{(1)}=C^{(1)}/v^2`$ forces $`v=\tau`$. A single $`v`$ for every level and both branches therefore exists iff $`\rho_{k,\sigma}=1`$ for all $`k,\sigma`$. For $`\lvert\delta_C\rvert<1`$, $`C^{\rm mark}\ne0`$ by (6.5), so $`\rho`$ has no vanishing denominator.

### Step 6. Ring, $`\ell\gg1`$: the scaling region

**Size of the sums.** On the ring $`Q=q`$. At $`L=\infty`$, $`G_0=1/(m_h\sqrt{m_h^2+4\kappa_h})`$, and $`\langle\!\langle1/E\rangle\!\rangle\propto\ell`$ is dominated by $`\lvert q\rvert\lesssim1/\ell`$, $`E\sim m_h`$. By contrast $`\langle\!\langle1\rangle\!\rangle`$ and $`\langle\!\langle\sin^2Q/E^2\rangle\!\rangle`$ grow at most like $`\ln^2\ell`$. Hence $`R=O(\ln^2\ell/c_0\ell)`$; its one-quantum part is $`\frac2\pi\frac{\ln\ell}{c_0\ell}[1+O(1/\ln\ell)]`$.

**Expansion of the own-branch fraction.** Let $`g=\cos^2\vartheta`$ and $`\mathcal D=E+\sigma[\omega(P-Q)-\omega(P)]`$. Then $`(g/\mathcal D)''=g''/\mathcal D-2g'\mathcal D'/\mathcal D^2+2g\mathcal D'^2/\mathcal D^3-g\mathcal D''/\mathcal D^2`$. At $`P=0`$:
- $`g''=-2\tau^2/\varepsilon^2\,[1+O(Q^2)]`$ and $`g'=O(\tau^2Q/\varepsilon^2)`$;
- $`\mathcal D'=-\sigma\omega'(Q)=-\sigma\tau^2Q/\varepsilon\,[1+O(Q^2)]`$;
- $`\mathcal D''=\sigma[\omega''(Q)-\omega''(0)]=-2\sigma\tau^2\sin^2Q/\varepsilon\,[1+O(\tau^2/\varepsilon^2)]`$;
- $`\mathcal D=E\,[1+O(\tau^2Q^2/\varepsilon E)]`$.

The four terms are therefore:
- (i) $`-2\tau^2/\varepsilon^2E`$;
- (ii) $`O(\tau^4Q^2/\varepsilon^3E^2)`$;
- (iii) $`2\tau^4Q^2/\varepsilon^2E^3`$;
- (iv) $`2\sigma\tau^2\sin^2Q/\varepsilon E^2`$.

In the scaling region, (ii), (iii) and (iv) are of relative size $`\tau^2/\varepsilon c_0\ell`$, $`r^2`$ and $`\varepsilon/c_0\ell`$ against (i). The other-branch fraction has $`\sin^2\vartheta=\tau^2(2P-Q)^2/4\varepsilon^2\,[1+\dots]`$ over $`-2\sigma\varepsilon+O(E)`$; it is of relative size $`O(c_0/\varepsilon\ell)`$.

**Rapidity identity.** In the scaling region $`\Omega_q=\sqrt{m_h^2+c_0^2q^2}\,[1+O(q^2)]`$. Substituting $`q=(m_h/c_0)\sinh\alpha`$ gives $`\sum_qc_q^2f\to\int d\alpha\,f/4\pi c_0`$, with $`E=m_h\cosh\alpha`$ and $`c_0Q=m_h\sinh\alpha`$. For pairs, put $`\alpha=\mathcal A+a`$ and $`\beta=\mathcal A-a`$. Then $`E=M_a\cosh\mathcal A`$ and $`c_0Q=M_a\sinh\mathcal A`$, with $`M_a=2m_h\cosh a`$ and $`d\alpha\,d\beta=2\,d\mathcal A\,da`$. In both cases $`\langle\!\langle f\rangle\!\rangle=\int d\nu(M)\int d\mathcal A\,f(M\cosh\mathcal A,M\sinh\mathcal A)`$, with a positive weight $`d\nu`$ independent of $`\mathcal A`$. Two integrals then give (6.7):
- $`\int d\mathcal A\,\sinh^2\!\mathcal A/\cosh^3\!\mathcal A=\pi/2=\frac12\int d\mathcal A/\cosh\mathcal A`$ gives the first relation;
- $`\int d\alpha/\cosh\alpha=\pi`$ and $`\iint d\alpha\,d\beta/(\cosh\alpha+\cosh\beta)=\pi^2`$ give $`G_0=\ell/2c_0^2`$ and $`J_2=\ell/16c_0^3`$ at leading order.

All these integrals converge in $`\mathcal A`$ and $`a`$, so the region $`\lvert q\rvert\gg1/\ell`$ enters only the corrections. For $`D=1`$:
```math
c_0^2\langle\!\langle Q^2/E^3\rangle\!\rangle=\tfrac12\langle\!\langle1/E\rangle\!\rangle\,[1+O(\ell^{-1})],\qquad\langle\!\langle1/E\rangle\!\rangle=\frac{F_1^2G_0}2+2F_2^2J_2=\frac{\ell}{4c_0^2}\Bigl(F_1^2+\frac{F_2^2}{2c_0}\Bigr)[1+O(\ell^{-1}\ln\ell)] .
\qquad\text{(6.7)}
```

**Summing the terms.** Let $`\delta_\ell:=(1+r^2+c_0/\varepsilon_k+\tau^2/\varepsilon_kc_0)\ln^2\ell/\ell`$. Sum the four terms with the weights (6.1), keep (iv) explicitly, use (6.7), and use (6.5) with $`\lvert\delta_C\rvert=O(\tau^2R/\varepsilon)`$. This gives
```math
C^{\rm mark}_{k,\sigma}=-\frac{M_k^2\ell}{4c_0^2}\Bigl(F_1^2+\frac{F_2^2}{2c_0}\Bigr)[1+O(\delta_\ell)],\qquad\zeta=\frac{F_2^2}{2c_0}[1+O(\delta_\ell)],\qquad E^{(2)\prime\prime}_{k,\sigma}(0)=-\frac{2\tau^2}{\varepsilon_k^2}\,C^{\rm mark}_{k,\sigma}\Bigl[1-\frac{r^2}2-\sigma\varepsilon_kR+O(\delta_\ell)\Bigr] .
\qquad\text{(6.8)}
```
Code check (`code/v2/output/check_mark_inertia.txt`, part B), on rings with $`L=8\ell`$ at $`\ell=512`$:
- $`G_0\cdot2c_0^2/\ell=1.00067`$; the excess is the finite-$`L`$ term $`\approx2e^{-8}`$;
- $`J_2\cdot16c_0^3/\ell=0.99938`$;
- $`C^{\rm mark}(\tau)/C^{\rm mark}(0)`$ lies within $`3.1\times10^{-3}`$ of 1.

### Step 7. Inertia against cost on the ring

Inserting (6.8) into (6.6) gives (6.9). Since $`\varepsilon_kR+\delta_\ell=O(\ln^2\ell/\ell)`$, $`\rho_{k,\sigma}\to2-r^2`$ as $`\ell\to\infty`$.
```math
\rho_{k,\sigma}=2-r^2-2\sigma\varepsilon_kR+O(\delta_\ell),\qquad\text{at leading order in }1/\ell:\ \ I^{\rm mark}_{k,\sigma}=\frac{(2-r^2)\,C^{\rm mark}_{k,\sigma}}{\tau^2}\ \Rightarrow\ \bigl[\exists\,v:\ I^{(1)}=C^{(1)}/v^2,\ I^{\rm mark}=C^{\rm mark}/v^2\ \forall k,\sigma\bigr]\iff r=1,\ v=\tau=c_0 .
\qquad\text{(6.9)}
```
- **First difference.** $`I^{\rm mark}-C^{\rm mark}/\tau^2=(1-r^2)C^{\rm mark}/\tau^2`$.
- **Mark alone, $`r\neq1`$.** For $`r<\sqrt2`$ the mark alone has $`v_{\rm mark}^2=\tau^2/(2-r^2)`$. At $`r=\sqrt2`$, $`I^{\rm mark}=0`$ at this order; for $`r>\sqrt2`$ it has the sign opposite to $`C^{\rm mark}`$.
- **Grip dependence.** The law holds for the $`F_1^2`$ part and the $`F_2^2`$ part separately. It is therefore independent of the grip, the linear grip ($`F_2=0`$) included.
- **Next order in $`1/\ell`$.** The term $`-2\sigma\varepsilon_kR`$ (from (iv)) is odd in $`\sigma`$ and grows with the level. By (6.10) it makes the two branches differ at every finite $`\ell`$ when $`\varepsilon_k\gg c_0,\ \tau\sqrt{1+r^2}`$.
- **Code check.** At $`\ell=512`$ and $`r=1`$, the $`F_1^2`$ part gives $`\rho=0.962`$ and $`1.056`$ ($`M_k=3`$, $`\sigma=\pm1`$). With the term (iv) removed, the values are $`1.00920`$ and $`1.00919`$ for both levels and both branches; for the $`F_2^2`$ part they are $`1.021`$–$`1.023`$. For $`r=0.5`$ and $`1.5`$ the values approach $`2-r^2`$ in the same way (part B).
- **Order of limits.** First $`L\gg\ell`$, then $`\ell\to\infty`$ at fixed $`\varepsilon_k/c_0`$ and $`r`$. Taking $`\varepsilon_k/c_0\to\infty`$ at fixed $`\ell`$ gives a different result (Step 8).

### Step 8. Branch asymmetry and heavy body: controls on both graphs

**Odd part in $`\sigma`$.** Let $`\Delta=\omega(P-Q)-\omega(P)`$ and $`\Sigma=\omega(P-Q)+\omega(P)`$. The part of (6.3) odd in $`\sigma`$ is $`-M_k^2\langle\!\langle-\cos^2\vartheta\,\Delta/(E^2-\Delta^2)+\sin^2\vartheta\,\Sigma/(E^2-\Sigma^2)\rangle\!\rangle`$. At $`P=0`$ its second derivative is dominated by $`\cos^2\vartheta\,\Delta''/E^2`$, with $`\Delta''(0)=\omega''(Q)-\omega''(0)=-2\tau^2\sin^2Q_1/\varepsilon\,[1+O(\tau^2/\varepsilon^2)]`$; this is the term (iv). The remaining odd terms are smaller:
- those with $`(\cos^2\vartheta)''\Delta`$ and $`(\cos^2\vartheta)'\Delta'`$, by $`\tau^2/\varepsilon^2`$;
- the one with $`\Delta\Delta'^2/E^2`$, by $`r^2\tau^2/\varepsilon^2`$;
- the other-branch term, by $`c_0^2/\varepsilon^2`$, since $`\langle\!\langle1\rangle\!\rangle=O(c_0^2\langle\!\langle\sin^2Q/E^2\rangle\!\rangle)`$;
- the odd part of $`\delta_C`$ in $`C^{\rm mark}`$, by $`(1+r^2)\tau^2/\varepsilon^2`$, because the even part of $`\rho`$ is $`O(1+r^2)`$: (i) gives at most 2, and (iii) gives $`r^2`$ times a lattice ratio of order 1, using $`\omega'(Q)=\tau^2\sin2Q_1/2\varepsilon`$.

**Heavy regime.** If moreover $`\varepsilon_kR\gg1+r^2`$ and $`\tau^2\ll\varepsilon_kc_0`$, the term (iv), $`2\sigma\tau^2\sin^2Q_1/\varepsilon_kE^2\,[1+O(\tau^2/\varepsilon_kc_0)]`$, dominates $`\rho`$ itself. With (6.6) this gives the second part of (6.10). Both parts hold on both graphs, for every $`L`$ and $`\ell`$, under (6.4).
```math
\rho_{k,+}-\rho_{k,-}=-4\varepsilon_kR\Bigl[1+O\Bigl(\frac{c_0^2+\tau^2(1+r^2)}{\varepsilon_k^2}\Bigr)\Bigr];\qquad\text{heavy: }\ I^{\rm mark}_{k,\sigma}=I^{(1)}_{k,\sigma}Y_k\Bigl[1+O\Bigl(\frac{1+r^2}{\varepsilon_kR},\frac{\tau^2}{\varepsilon_kc_0}\Bigr)\Bigr],\ \ Y_k:=2M_k^2\langle\!\langle\sin^2Q_1/E^2\rangle\!\rangle>0 .
\qquad\text{(6.10)}
```
**Consequences.**
- *Branch asymmetry.* $`R>0`$. For $`\varepsilon_k\gg c_0`$ and $`\varepsilon_k^2\gg\tau^2(1+r^2)`$ the two branches therefore have different $`\rho`$, so $`\rho_{k,\sigma}=1`$ cannot hold for both. At second order no single $`v`$ exists then, at any finite $`\ell`$ and $`L`$ and at any $`r`$ ($`r=1`$ included). On the ring this difference vanishes as $`\ell\to\infty`$, consistently with (6.9).
- *Heavy regime.* $`\rho_{k,\sigma}=-2\sigma\varepsilon_kR`$ at leading order, so $`\lvert\rho\rvert\gg1`$, and $`\rho`$ is proportional to $`\varepsilon_k`$, so it depends on the level.

**Size of $`R`$.** On $`D=3`$ the sums are dominated by $`\lvert q\rvert\sim1`$, and $`R`$ tends to a finite limit of order $`1/c_0`$ as $`\ell\to\infty`$. The heavy regime is then $`\varepsilon_k\gg c_0`$, up to a lattice number. On the ring it requires $`\varepsilon_k\gg c_0\ell/\ln\ell`$.

**$`D=3`$ otherwise.** The scaling argument of Step 6 fails on $`D=3`$. Outside the regime of (6.10), $`\rho`$ is given by the lattice sums of (6.3). They are evaluated in Step 10, which also gives the size of $`\varepsilon_kR`$ where (U) holds.

### Step 9. Weight over inertia

Let $`\Delta W_{k,\sigma}=\sigma M_kF_1\Delta\phi/(1+2\sigma M_kF_2G_0)`$ by (2.8), with $`\Delta\phi\ne0`$. Then $`E''\Delta W=\Delta W/I`$.

**(a) $`F_1`$ and $`F_2`$ counted alike.** $`E''(0)=\sigma\tau^2/(M_k\bar F)+O(\delta F^2)`$ and $`\Delta W=\sigma M_kF_1\Delta\phi(1-2\sigma M_kF_2G_0)+O(\delta F^3)`$. Hence, on both graphs and for every $`L`$, $`\ell`$ and $`r`$,
```math
E''_{k,\sigma}(0)\,\Delta W_{k,\sigma}=\frac{\tau^2F_1\Delta\phi}{F_0}\Bigl[1-\frac{F_2w_0}{F_0}-2\sigma M_kF_2G_0\Bigr]+O(\delta F^3).
\qquad\text{(6.11)}
```
In this counting the inertia of the mark enters only at $`O(\delta F^3)`$.
- **Linear grip.** For $`F_2=0`$ exactly, (6.11) is the same for every level and both branches, but only at this order. With $`F_2=0`$, $`\Delta W`$ is exactly $`\sigma M_kF_1\Delta\phi`$, and $`E''`$ is even in $`F_1`$. The first dependence on the level is therefore the term $`-I^{\rm mark}/I^{(1)}`$ of relative order $`F_1^2`$, i.e. (6.12) with $`F_2=0`$. On the ring, at leading order in $`1/\ell`$, it vanishes only at $`r=\sqrt2`$ (below). On the cubic torus it does not vanish once two lower levels are isolated, at any computed $`r`$ (Step 10).

**(b) Grips of a fixed shape.** For grips $`F=F_0\Phi(\beta q)`$ of a fixed shape, as in (2.18), $`F_1=O(\beta)`$ and $`F_2=O(\beta^2)`$. The weight of the mark ($`\propto F_1F_2`$) and its inertia ($`\propto F_1^3`$ in $`E''\Delta W`$) are then of the same order $`\beta^3`$.
- $`E''`$ is even in $`F_1`$ (symmetry $`q\to-q`$, $`p\to-p`$ of $`H`$). Through relative order $`\beta^2`$ it therefore needs only the term $`F_2w_0`$ and the $`F_1^2`$ part of $`E^{(2)}`$; the $`F_2^2`$ part is $`O(\beta^4)`$.
- By (6.6), $`\sigma M_kE^{(2)\prime\prime}(0)=-\sigma M_k\tau^4I^{\rm mark}/\varepsilon_k^2=-(\tau^2/F_0)\,I^{\rm mark}/I^{(1)}`$ at this order. Hence, on both graphs and for every $`L`$ and $`\ell`$, with $`I^{\rm mark}`$ its $`F_1^2`$ part:
```math
E''_{k,\sigma}(0)\,\Delta W_{k,\sigma}=\frac{\tau^2F_1\Delta\phi}{F_0}\Bigl[1-\frac{F_2w_0}{F_0}-2\sigma M_kF_2G_0-\frac{I^{\rm mark}_{k,\sigma}}{I^{(1)}_{k,\sigma}}\Bigr][1+O(\beta^4)].
\qquad\text{(6.12)}
```
- **Ring, leading order in $`1/\ell`$.** By (6.9), $`I^{\rm mark}/I^{(1)}=(2-r^2)C^{\rm mark}/C^{(1)}=-(2-r^2)\sigma M_kF_1^2G_0/2F_0`$. The bracket is then the same for every level and both branches iff $`(2-r^2)F_1^2=4F_0F_2`$. At $`r=1`$ this is the square grip of (2.18). The square grip satisfies it only at $`r=1`$, and the linear grip only at $`r=\sqrt2`$.
- **$`\varepsilon_k\gg c_0,\ \tau\sqrt{1+r^2}`$ (both graphs, every finite $`\ell`$).** By (6.10), the part of $`-I^{\rm mark}/I^{(1)}`$ even in $`\sigma`$ is $`-M_k^2G_0F_1^2R\,[1+O((c_0^2+\tau^2(1+r^2))/\varepsilon_k^2)]`$, with $`R`$ of the $`F_1^2`$ part. All $`F_2`$ terms are odd in $`\sigma`$ or independent of the level. Take two levels whose values of $`M_k^2`$ differ by a relative amount larger than this error. Then no grip of (G2) makes the bracket the same for every level and both branches; this includes the heavy regime. The rest of the range on the cubic torus is treated in Step 10.

### Step 10. Cubic torus: items 2 and 3 from the lattice sums

**Two parts.** Write (6.3) as $`E^{(2)}_{k,\sigma}(P)=-M_k^2[F_1^2S_1(P)+F_2^2S_2(P)]`$. Here $`S_1`$ and $`S_2`$ are its one- and two-quantum parts per unit $`F_1^2`$ and $`F_2^2`$; they depend only on $`\varepsilon_k`$, $`\tau`$, $`\sigma`$ and the field. Put $`S_i:=S_i(0)`$ and $`\rho_i:=-(\varepsilon_k^2/\tau^2)S_i''(0)/S_i`$, the ratio of (6.6) for part $`i`$. Define the grip ratios $`\xi:=F_2^2/(c_0F_1^2)`$ and $`y:=F_0F_2/F_1^2`$; $`y=\frac14`$ is the square grip and $`y=0`$ the linear grip. Finally put $`T_{k,\sigma}:=\rho_1S_1`$ and $`t_{k,\sigma}:=T_{k,\sigma}/G_0`$. Then (6.6) gives $`I^{\rm mark}/I^{(1)}=-\sigma M_kF_1^2T_{k,\sigma}/F_0`$ for the $`F_1^2`$ part, and with (6.12):
```math
\rho_{k,\sigma}=\frac{S_1\rho_1+\xi c_0S_2\rho_2}{S_1+\xi c_0S_2},\qquad\rho_{k,\sigma}=1\iff\xi=\xi^*_{k,\sigma}:=\frac{S_1(1-\rho_1)}{c_0S_2(\rho_2-1)}\ge0,\qquad[\,\cdot\,]_{(6.12)}=1-\frac{F_2w_0}{F_0}-\sigma\frac{\varepsilon_kF_1^2G_0}{F_0^2}\,(2y-t_{k,\sigma}).
\qquad\text{(6.13)}
```
- Where $`S_1,S_2>0`$ (all computed points: each is at least $`0.55`$ times its held value, Part D), $`\rho`$ is a mean of $`\rho_1`$ and $`\rho_2`$ with positive weights. Hence some grip gives $`\rho_{k,\sigma}=1`$ iff 1 lies between $`\rho_1`$ and $`\rho_2`$.
- Check on the ring: at leading order in $`1/\ell`$, $`t=(2-r^2)/2`$ by (6.9), and (6.13) gives back the condition of Step 9(b).

**Isolated states.** The quantity $`\min_q[\Omega_q-\omega_k(q_1)+\varepsilon_k]`$ of (6.4) increases with $`\varepsilon_k`$, since $`\omega_k(q_1)-\varepsilon_k=\tau^2\sin^2q_1/(\omega_k+\varepsilon_k)`$. In (U), the maxima of $`\Omega_q-\omega_k(q_1)`$ and of $`\Omega_q+\Omega_{q'}-\omega_k(q_1+q_1')`$ lie at $`q=q'=(\pi,\pi,\pi)`$, where $`\omega_k=\varepsilon_k`$. For $`2\varepsilon_k>m_h`$ the functions of (U) are negative at $`q=0`$. So, as $`L\to\infty`$, (U) holds iff $`\Omega_{\max}<2\varepsilon_k`$ for $`F_2=0`$, and iff $`\Omega_{\max}<\varepsilon_k`$ otherwise, with $`\Omega_{\max}\approx2\sqrt3\,c_0`$. The set $`\mathcal S`$ of isolated states $`(k,\sigma)`$ is therefore made of the lower branches of all levels above one threshold, together with the upper branches of all levels above another.

**Evaluation** (`code/v2/output/torus_mark_inertia.txt`).
- *Setting.* Units $`c_0=F_0=1`$. Torus $`L=64`$, $`\ell=8`$. Values $`r\in\{0.1,0.25,0.5,0.75,1,1.25,1.5,2,3\}`$ and 71 values of $`\varepsilon_k\in[0.1,64]`$. Lower branches are taken where their gap exceeds $`m_h/2`$, upper branches where (U) holds with a margin of $`0.1`$.
- *Method.* $`S_1`$ is an exact mode sum. $`S_2`$ is summed from histograms of pair energies, with the exact moments in each bin; this agrees with brute-force pair sums on $`L=12`$ to $`4\times10^{-10}`$ (Part A). Exact diagonalisation with at most two quanta on the torus $`L=4`$ reproduces the second-order coefficients of $`\mathrm{Cost}`$ and $`E''(0)`$ from (6.2), (6.3) to $`9\times10^{-9}`$, for both branches (Part E).
- *Convergence in $`L`$* (Part B). At $`\ell=8`$, $`L=48`$ and $`L=64`$ give the same $`\rho_i`$ to $`6\times10^{-4}`$.
- *Convergence in $`\ell`$* (Part B2), over the points of Part C. From $`\ell=8`$ to $`\ell=32`$ ($`L=256`$), $`\rho_1`$ and $`t`$ change by at most $`0.093`$ and $`0.058`$ for $`\varepsilon_k\le4c_0`$, and by at most $`3.4\%`$ above. From $`\ell=6`$ to $`\ell=8`$, $`\rho_2`$ changes by at most $`0.008`$ and $`1.2\%`$ respectively.
- *Check at $`\ell=32`$* (Part D2). The tests of Part D on the $`F_1^2`$ part are repeated at $`\ell=32`$, $`L=256`$, with the same outcomes.

**Findings** (Parts C, D, D2).
- (a) *Upper branch:* $`\rho_{1,+}\le0.61`$ and $`\rho_{2,+}\le0.44`$ (at $`\ell=32`$, $`\rho_{1,+}\le0.63`$).
- (b) *Lower branch.*
  - $`\rho_{1,-}`$ and $`\rho_{2,-}`$ increase strictly with $`\varepsilon_k`$ at every $`r`$. At $`r=1`$ they go from $`0.28`$ and $`0.06`$ at $`\varepsilon_k=0.1\,c_0`$ to $`30.6`$ and $`16.8`$ at $`64\,c_0`$.
  - Hence $`\xi^*_{k,-}\ge0`$ only in a window of $`\varepsilon_k`$: $`[0.99,2.66]\,c_0`$ at $`r=0.1`$, $`[0.93,2.61]\,c_0`$ at $`r=1`$, $`[1.34,2.39]\,c_0`$ at $`r=2`$, and $`[3.34,3.56]\,c_0`$ at $`r=3`$, whose lower end is the edge of the computed range.
  - Across the window $`\xi^*_{k,-}`$ is strictly monotone: increasing for $`r\le2`$, decreasing at $`r=3`$.
  - At $`\ell=32`$ the lower end of the window moves by at most $`0.11\,c_0`$ for $`r\le2`$, and by $`0.3\,c_0`$ at $`r=3`$.
- (c) *Both branches of one level:* for every grip, $`\rho_{k,-}-\rho_{k,+}\ge0.85`$ for $`r\le2`$, and $`\ge0.44`$ at $`r=3`$. For $`r\le2`$ the ratio $`(\rho_{1,-}-\rho_{1,+})/(4\varepsilon_kR_1)`$ is $`0.54`$–$`0.74`$ at $`\varepsilon_k=1.92\,c_0`$ (edge of (U)), and $`0.9997`$ at $`64\,c_0`$, as (6.10) predicts.
- (d) *Size of $`\varepsilon_kR`$:* $`R_1=0.232/c_0`$ and $`R_2=0.127/c_0`$ ($`R_1=0.229/c_0`$ at $`\ell=32`$).
  - At the edge of (U), $`\varepsilon_kR_1=0.40`$ for $`F_2=0`$ ($`\varepsilon_k=\Omega_{\max}/2`$). For $`F_2\ne0`$ ($`\varepsilon_k=\Omega_{\max}`$), $`\varepsilon_kR_1=0.80`$ and $`\varepsilon_kR_2=0.44`$.
  - Where (U) begins, $`\varepsilon_kR<1`$, so the heavy regime of (6.10) is not reached there, and the corrections to the first part of (6.10) are of order one.
- (e) *Item 3 functions.*
  - $`\varphi(\varepsilon):=\varepsilon\,t_{-}(\varepsilon)`$ increases strictly. It is strictly convex for $`r\le1.25`$. For $`r\ge1.5`$ it is strictly convex except in a band just above the edge of isolation of the lower branch: $`\varepsilon\in[0.48,0.63]`$ at $`r=1.5`$, $`[1.33,1.75]`$ at $`r=2`$, and $`[3.66,4.83]`$ at $`r=3`$ (narrower at $`\ell=32`$).
  - $`\psi(\varepsilon):=\varepsilon(t_--t_+)`$ increases strictly.
  - $`y_{\rm b}:=(t_++t_-)/4`$ lies in $`[0.22,0.28]`$ for $`r\le2`$, and changes sign at $`r=3`$.
- (f) *Dependence on $`r`$* (Part D). For $`\varepsilon_k\ge2c_0`$, $`\rho_{1,-}`$ and $`\rho_{2,-}`$ change by at most $`0.08`$ between $`r=0.25`$ and $`r=2`$; $`\rho_{1,+}`$ changes by up to $`0.32`$, near the edge of (U). Without a scaling region there is no counterpart of the term $`-r^2`$ of (6.9).

**Item 2.** By (6.6), a single $`v`$ must be $`\tau`$, and it needs $`\rho_{k,\sigma}=1`$ on all of $`\mathcal S`$.
- By (a), no grip gives this on an isolated upper branch.
- By (b), two isolated lower levels would need two different values of $`\xi^*`$.

Hence, for nonempty $`\mathcal S`$:
```math
D=3:\ \ \bigl[\exists\,v:\ I^{(1)}=C^{(1)}/v^2,\ I^{\rm mark}=C^{\rm mark}/v^2\ \text{on }\mathcal S\bigr]\iff\mathcal S=\{(k,-)\},\ \varepsilon_k\ \text{in the window of (b)},\ \xi=\xi^*_{k,-};\ \ \text{then }v=\tau .
\qquad\text{(6.14)}
```
- In particular, once two states are isolated, no grip and no computed $`r`$ ($`r=1`$ included) give one $`v`$.
- The first difference is $`I^{\rm mark}-C^{\rm mark}/\tau^2=(\rho_{k,\sigma}-1)\,C^{\rm mark}/\tau^2`$. For example, at $`r=1`$ and $`\varepsilon_k=4c_0`$: $`\rho_{1,-}=2.62`$, $`\rho_{2,-}=1.41`$, $`\rho_{1,+}=-0.83`$, $`\rho_{2,+}=0.16`$.
- Order of limits: $`L\gg\ell`$, then $`\ell\to\infty`$. Unlike on the ring, the sums have finite limits.

**Item 3.** By (6.13), the bracket of (6.12) is the same on $`\mathcal S`$ iff $`\sigma\varepsilon_k(2y-t_{k,\sigma})`$ is the same for all $`(k,\sigma)\in\mathcal S`$.
- *Both branches of a level $`a`$.* Adding the two conditions gives $`y=y_{\rm b}(\varepsilon_a)`$, and the common value is then $`\psi(\varepsilon_a)/2`$. For two such levels this needs $`\psi(\varepsilon_a)=\psi(\varepsilon_b)`$, which (e) excludes.
- *Lower branches of levels $`a\ne b`$.*
  - They give $`y=y_{ab}:=[\varphi(\varepsilon_b)-\varphi(\varepsilon_a)]/[2(\varepsilon_b-\varepsilon_a)]`$, which depends on the levels.
  - At $`r=1`$, $`y_{ab}=0.25,0.37,0.56,0.92,1.62`$ for $`(\varepsilon_a,\varepsilon_b)/c_0=(0.25,0.5),(0.5,1),(1,2),(2,4),(4,8)`$; at $`\ell=32`$ the values are $`0.26,0.37,0.56,0.91,1.60`$.
  - Three lower levels would have to lie on one straight line on the graph of $`\varphi`$, which strict convexity excludes.
- *Linear grip* ($`y=0`$).
  - Since $`\varphi`$ is increasing, $`y_{ab}>0`$, so the linear grip fails for any two lower levels.
  - Since $`y_{\rm b}>0`$ for $`r\le2`$, it also fails for both branches of one level.
```math
D=3:\ \ E''_{k,\sigma}(0)\,\Delta W_{k,\sigma}\ \text{the same on }\mathcal S\iff\sigma\varepsilon_k\,(2y-t_{k,\sigma})\ \text{the same on }\mathcal S;\ \ \text{no grip of (G2) if }\mathcal S\ \text{has both branches of two levels, or three lower levels where }\varphi\ \text{is strictly convex} .
\qquad\text{(6.15)}
```
If $`\mathcal S`$ has two states, exactly one value of $`y`$ works, and it depends on the levels and on $`r`$. The square grip, which gives (6.12) on the ring at $`r=1`$, is not singled out here.

## Result

- **(6.2), (6.3)** [formula]. Class: ring and cubic torus, every $`L`$, $`M\to\infty`$ first, every level and both branches under (6.4), $`P`$ near 0. The level is $`E_f+\sigma\sqrt{M_k^2\bar F^2+\tau^2\sin^2P}+E^{(2)}_{k,\sigma}(P)`$ up to $`O(\delta F^3)`$, with $`E^{(2)}`$ the spectral sum (6.3) over one- and two-quantum states; it is even in $`P`$.
- **(6.4)** [criterion]. $`\sigma=-1`$: under $`\Omega_q>\omega_k(q_1)-\varepsilon_k`$ for all $`q`$ (implied by $`\tau^2\le2\varepsilon_kc_0`$), the level is isolated and analytic in $`P`$ and $`\delta F`$. $`\sigma=+1`$: under (U) (implied by $`\Omega_{\max}<\varepsilon_k`$, or by $`\Omega_{\max}<2\varepsilon_k`$ for $`F_2=0`$), the second-order coefficients are analytic in $`P`$ near 0. If a function of (U) changes sign, the level is not isolated at second order as $`L\to\infty`$.
- **(6.5)** [formula]. Same class. $`C^{(1)}_{k,\sigma}=\sigma M_k\bar F`$ for every $`\tau`$. $`C^{\rm mark}_{k,\sigma}=E^{(2)}_{k,\sigma}(0)=-M_k^2(F_1^2G_0/2+2F_2^2J_2)(1+\delta_C)`$, with $`\delta_C`$ as in (6.5) at first order in $`\tau^2`$. The held mark is strictly negative.
- **(6.6)** [theorem]. Same class, $`\tau>0`$, exact at its order: $`I^{(1)}_{k,\sigma}=C^{(1)}_{k,\sigma}/\tau^2`$ for every level, both branches and every $`r`$; $`I^{\rm mark}=-\varepsilon_k^2E^{(2)\prime\prime}(0)/\tau^4`$. A single $`v`$ exists iff $`\rho_{k,\sigma}=1`$ for all $`k,\sigma`$, and then $`v=\tau`$.
- **(6.7)** [formula]. Ring, $`L\gg\ell`$: $`c_0^2\langle\!\langle Q^2/E^3\rangle\!\rangle=\frac12\langle\!\langle1/E\rangle\!\rangle[1+O(1/\ell)]`$ and $`\langle\!\langle1/E\rangle\!\rangle=\frac{\ell}{4c_0^2}(F_1^2+F_2^2/2c_0)[1+O(\ln\ell/\ell)]`$.
- **(6.8)** [formula]. Ring, $`L\gg\ell`$, under (6.4), up to relative $`O(\delta_\ell)`$: $`C^{\rm mark}_{k,\sigma}=-\frac{M_k^2\ell}{4c_0^2}(F_1^2+\frac{F_2^2}{2c_0})`$, $`\zeta=F_2^2/2c_0`$, and $`E^{(2)\prime\prime}(0)=-\frac{2\tau^2}{\varepsilon_k^2}C^{\rm mark}[1-\frac{r^2}2-\sigma\varepsilon_kR]`$, with $`R=O(\ln^2\ell/c_0\ell)`$.
- **(6.9)** [theorem]. Ring, $`L\gg\ell`$, every (G2) grip, every level and both branches under (6.4), every $`r>0`$. $`\rho_{k,\sigma}=2-r^2-2\sigma\varepsilon_kR+O(\delta_\ell)`$, with $`\varepsilon_kR=O((\varepsilon_k/c_0)\ln^2\ell/\ell)`$. At leading order in $`1/\ell`$, $`I^{\rm mark}=(2-r^2)C^{\rm mark}/\tau^2`$. Hence one $`v`$ with $`I^{(1)}=C^{(1)}/v^2`$ and $`I^{\rm mark}=C^{\rm mark}/v^2`$ for every level and both branches exists iff $`r=1`$, and then $`v=\tau=c_0`$. The first difference is $`(1-r^2)C^{\rm mark}/\tau^2`$.
- **(6.10)** [negative]. Both graphs, every $`L`$ and $`\ell`$, under (6.4).
  - $`\rho_{k,+}-\rho_{k,-}=-4\varepsilon_kR\,[1+O((c_0^2+\tau^2(1+r^2))/\varepsilon_k^2)]`$. For $`\varepsilon_k\gg c_0`$ and $`\varepsilon_k^2\gg\tau^2(1+r^2)`$, no single $`v`$ exists at second order, at any $`r`$ ($`r=1`$ included) and at any finite $`\ell`$.
  - In the heavy regime (additionally $`\varepsilon_kR\gg1+r^2`$ and $`\tau^2\ll\varepsilon_kc_0`$): $`I^{\rm mark}=I^{(1)}Y_k`$ and $`\rho_{k,\sigma}=-2\sigma\varepsilon_kR`$ at leading order.
- **(6.11)** [criterion]. Both graphs, every $`L`$, $`\ell`$, $`r`$, at second order in $`\delta F`$ with $`F_1`$ and $`F_2`$ counted alike, with the weights (2.8): $`E''\Delta W=\frac{\tau^2F_1\Delta\phi}{F_0}[1-F_2w_0/F_0-2\sigma M_kF_2G_0]`$. At this order it is the same for every level and both branches iff $`F_2=0`$, independently of $`r`$. For $`F_2=0`$ the first dependence on the level comes from $`I^{\rm mark}`$ at relative order $`F_1^2`$, given by (6.12) with $`F_2=0`$. On the ring, at leading order in $`1/\ell`$, it vanishes only at $`r=\sqrt2`$. On the cubic torus it does not vanish once two lower levels are isolated, at any computed $`r`$, by (6.15).
- **(6.12)** [criterion]. Grips of fixed shape through relative order $`\beta^2`$, weights (2.8), both graphs, every $`L`$ and $`\ell`$: $`E''\Delta W=\frac{\tau^2F_1\Delta\phi}{F_0}[1-F_2w_0/F_0-2\sigma M_kF_2G_0-I^{\rm mark}/I^{(1)}]`$.
  - On the ring ($`L\gg\ell`$, leading order in $`1/\ell`$) it is the same for every level and both branches iff $`(2-r^2)F_1^2=4F_0F_2`$. At $`r=1`$ this holds iff the grip is the square grip; for the linear grip it holds only at $`r=\sqrt2`$.
  - For $`\varepsilon_k\gg c_0,\ \tau\sqrt{1+r^2}`$, with levels whose $`M_k^2`$ differ by more than the relative error of (6.10), no grip of (G2) gives this at any finite $`\ell`$, on either graph.
- **(6.13)** [formula]. Both graphs, every $`L`$ and $`\ell`$, under (6.4). $`\rho_{k,\sigma}`$ is the mean of $`\rho_1,\rho_2`$ with weights $`S_1`$, $`\xi c_0S_2`$, and $`\rho_{k,\sigma}=1`$ iff $`\xi=\xi^*_{k,\sigma}\ge0`$. The bracket of (6.12) is $`1-F_2w_0/F_0-\sigma(\varepsilon_kF_1^2G_0/F_0^2)(2y-t_{k,\sigma})`$.
- **(6.14)** [negative]. Cubic torus, $`L=64`$, $`\ell=8`$ (with the convergence check of Step 10), every grip of (G2), $`r\in[0.1,3]`$, $`\varepsilon_k/c_0\in[0.1,64]`$ on the computed grid. $`\mathcal S`$ is the nonempty set of isolated states: lower branches where the minimum of (6.4) exceeds $`m_h/2`$, upper branches where $`\Omega_{\max}<2\varepsilon_k`$ ($`F_2=0`$) or $`\Omega_{\max}<\varepsilon_k`$ ($`F_2\neq0`$).
  - One $`v`$ with $`I^{(1)}=C^{(1)}/v^2`$ and $`I^{\rm mark}=C^{\rm mark}/v^2`$ on all of $`\mathcal S`$ exists iff $`\mathcal S`$ is the lower branch of a single level, with $`\varepsilon_k`$ in a window and $`\xi=\xi^*_{k,-}`$; then $`v=\tau`$. The window is about $`[0.93,2.61]\,c_0`$ at $`r=1`$.
  - In particular, no grip and no computed $`r`$ ($`r=1`$ included) give one $`v`$ once two states are isolated: $`\rho_{k,+}<1`$ for every grip, and $`\xi^*_{k,-}`$ is strictly monotone in $`\varepsilon_k`$.
  - The first difference is $`(\rho_{k,\sigma}-1)C^{\rm mark}/\tau^2`$. Where (U) begins, $`\varepsilon_kR\le0.80`$ (Step 10 (d)).
- **(6.15)** [criterion]. Same setting as (6.14). $`E''\Delta W`$ (to relative order $`\beta^2`$, weights (2.8)) is the same on $`\mathcal S`$ iff $`\sigma\varepsilon_k(2y-t_{k,\sigma})`$ is the same on $`\mathcal S`$.
  - No grip of (G2) achieves this if $`\mathcal S`$ contains both branches of two levels, or three lower levels in the range where $`\varphi`$ is strictly convex (all computed $`\varepsilon_k`$ for $`r\le1.25`$).
  - If $`\mathcal S`$ has two states, exactly one value of $`y`$ works, and it depends on the levels and on $`r`$.
  - The linear grip fails for any two lower levels, and for both branches of one level when $`r\le2`$. The square grip is not singled out.

## Consistency checks

1. Held limit $`\tau\to0`$: $`\theta=0`$ and $`\omega=\varepsilon_k`$, so $`E^{(2)}(0)=-M_k^2(F_1^2G_0/2+2F_2^2J_2)`$. This is the second-order part of $`C^{\rm mark}`$ in (2.6), with $`\mu^2=M_k^2`$, $`D_\mu=1+O(\delta F)`$ and $`\zeta=4F_2^2J_2/G_0`$.
2. Bare body ($`\delta F=0`$, $`F_0=1`$): $`E''(0)=\sigma\tau^2/M_k`$, which is $`\omega_k''(0)`$ of (6.7) of 04-ilang-time/06-inertia-internal-energy (mirrored for $`\sigma=-1`$).
3. Dimensions:
   - $`[\tau]=[c_0]=[m_h]=[M_k]=`$ cost, $`[q^2]=`$ cost$`^{-1}`$, $`[F_1^2]=[F_2^2/c_0]=`$ cost, $`[G_0]=`$ cost$`^{-2}`$;
   - $`C^{\rm mark}`$ is a cost, $`I`$ and $`C/\tau^2`$ are cost$`^{-1}`$, $`r`$ is dimensionless;
   - $`E''\Delta W`$ and $`\tau^2F_1\Delta\phi/F_0`$ are cost$`^2`$.

## Open issues

- Cubic torus: (6.14) and (6.15) rest on lattice sums evaluated on a grid ($`r\in[0.1,3]`$, $`\varepsilon_k/c_0\in[0.1,64]`$, $`L=64`$, $`\ell=8`$, with the convergence check of Step 10). Between the grid points they rest on the monotonicity and convexity found on the grid, and above $`64c_0`$ on (6.10). No points were computed in the band where the gap of the lower branch is below $`m_h/2`$, or for $`r>3`$.
- Branch $`\sigma=+1`$ beyond second order: lower-branch states with three or more quanta can be degenerate with the level. Whether the exact level is isolated as $`L\to\infty`$ is not settled.
- The weight of the moving body is taken from (2.8) without corrections in $`\tau`$; (6.11) and (6.12) rest on this.
- On the ring the expansion parameter grows like $`\ell`$, so (6.8)–(6.12) need $`\delta F`$ to shrink as $`\ell`$ grows. The regime $`M_kF_1^2G_0\sim F_0`$ is open.

## Code

- `code/v2/check_mark_inertia.py` (role: check). It is the v1 script, unchanged, run again; its output `code/v2/output/check_mark_inertia.txt` is identical to that of v1.
- **Part A** (the check required by the question).
  - *Setting.* Ring of $`L=32`$ cells, $`c_0=1`$, $`m_h=0.25`$, $`F_0=1`$. A square grip ($`F_1=0.3`$, $`F_2=0.0225`$) and another grip ($`F_1=0.3`$, $`F_2=-0.15`$); levels $`M_k=3,4`$; both branches; $`r=0.5,1,1.5`$.
  - *Independent computation.* Exact diagonalisation of the total contract restricted to states with at most two field quanta, in the sector $`P`$ (dimension 1122). $`E''(0)`$ is the exact second derivative of the eigenvalue, from the eigen-decomposition. The coefficient of $`s^2`$ is fitted from $`\delta F\to s\,\delta F`$ with $`s=\pm0.01,\pm0.02,\pm0.04`$.
  - *Formula side.* (6.2), (6.3), (6.5) are evaluated as lattice sums.
  - *Results.* The second-order coefficients of $`\mathrm{Cost}_{k,\sigma}`$ and $`E''_{k,\sigma}(0)`$ agree to a maximal relative deviation of $`2.26\times10^{-7}`$. The first-order coefficients agree to $`\le2.6\times10^{-8}`$ absolute. The zeroth order reproduces $`\sigma F_0M_k`$ and $`\sigma\tau^2/F_0M_k`$.
- **Part B.** Formula (6.3) on rings with $`L=8\ell`$, $`\ell=16,\dots,512`$. It reports $`\rho`$ of the $`F_1^2`$ and $`F_2^2`$ parts against $`2-r^2`$, the same values without the term (iv), the held sums against (6.7), and $`C^{\rm mark}(\tau)/C^{\rm mark}(0)`$. These are the numbers quoted in Steps 6 and 7.
- `code/v2/torus_mark_inertia.py` (role: computation). Output: `code/v2/output/torus_mark_inertia.txt`. It evaluates the lattice sums of (6.3) on the cubic torus, for the $`F_1^2`$ and $`F_2^2`$ parts separately (units $`c_0=F_0=1`$, $`\varepsilon_k=M_k`$). The two-quantum sums use histograms of pair energies per total $`q_1`$, with the exact zeroth to second moments in each bin.
  - *Part A:* mode-class and histogram sums against brute-force sums on $`L=12`$.
  - *Parts B, B2:* convergence in $`L`$ and $`\ell`$.
  - *Part C:* table of $`S_i(0)`$ relative to the held value, $`\rho_1`$, $`\rho_2`$, $`t`$ and $`\xi^*`$ on $`L=64`$, $`\ell=8`$.
  - *Part D:* fine grid in $`\varepsilon_k`$ for nine values of $`r`$: monotonicity of $`\rho_{i,-}`$, window and monotonicity of $`\xi^*_{k,-}`$, bounds on $`\rho_{i,+}`$, monotonicity and convexity of $`\varphi`$, monotonicity of $`\psi`$, $`y_{\rm b}`$, $`y_{ab}`$, and the dependence on $`r`$.
  - *Part D2:* the $`F_1^2`$ tests of Part D repeated at $`\ell=32`$, $`L=256`$.
  - *Part E:* exact diagonalisation of the contract restricted to at most two field quanta on the torus $`L=4`$ (dimension 4290), against (6.2), (6.3) for both branches.
  These are the numbers quoted in Step 10.

## Methods used

- Rayleigh–Schrödinger perturbation theory for an isolated eigenvalue in a sector of a conserved label; analyticity of isolated eigenvalues
- Fourier analysis on ring and torus; normal modes and Wick's theorem for the oscillator field
- Asymptotics of lattice sums dominated by a scaling region; rapidity substitution; Poisson summation
- Exact diagonalisation in a truncated Fock space; second derivative of an eigenvalue from its eigen-decomposition (code check)
- Numerical lattice sums on the cubic torus: pair-energy histograms with exact bin moments, Richardson-extrapolated finite differences in $`P`$, convergence in $`L`$ and $`\ell`$; monotonicity and convexity tests on a grid
