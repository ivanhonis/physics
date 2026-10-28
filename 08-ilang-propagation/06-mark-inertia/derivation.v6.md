# Inertia of a body with its own mark in a weakly pinned field of oscillator cells

- **Subproject:** 08-ilang-propagation
- **Package:** 06-mark-inertia
- **Version:** v6
- **Mode:** external regeneration
- **Date:** 2026-10-25

## Changes from previous version

- Step 8 (Odd part in $`\sigma`$, Heavy regime) and Result (6.10): the first relation of (6.10) is now stated for $`L\gg\ell\ge1`$. The other-branch term is given explicitly and bounded for every $`L`$, and its comparison with (iv) is shown to fail at finite $`L`$ when the uniform mode dominates. The heavy-regime part keeps every $`L`$ and $`\ell`$, now with this bound (verification I1).
- Step 6 (Rapidity identity) and Result (6.7): the relative error of the first relation of (6.7) is now $`O(\ell^{-1}\ln\ell)`$, from pairs with one soft and one lattice-order momentum (verification I2).
- Step 8 (Size of $`R`$): the heavy condition is stated as $`\varepsilon_kR\gg1+r^2`$. On the ring $`R_2=\Theta(\ln^2\ell/c_0\ell)`$, so the scale is $`c_0\ell/\ln\ell`$ for the linear grip and $`c_0\ell/\ln^2\ell`$ with a nonzero two-quantum part; the former is a sufficient condition for every grip (verification I3).
- Code: both scripts are copied unchanged from v5 and re-run into `code/v6/output/`; every number cited in Steps 3, 6, 7 and 10 is from this run.

## Response to verification

- I1: Accepted and fixed in Step 8 (Odd part in $`\sigma`$; Heavy regime) and Result (6.10). The other-branch term adds $`\sigma\langle\!\langle(1+\cos Q_1)^2\rangle\!\rangle/(4\varepsilon_k\langle\!\langle1/E\rangle\!\rangle)`$ to $`\rho`$; its smallness against (iv) needs $`\langle\!\langle1\rangle\!\rangle=O(c_0^2\langle\!\langle\sin^2Q_1/E^2\rangle\!\rangle)`$, which holds for $`L\gg\ell\ge1`$ but not when the uniform mode dominates at fixed $`L`$, as in the verifier's example ($`\rho_{k,-}-\rho^{\rm e}_k=-m_h/\varepsilon_k`$). The first relation is now restricted to $`L\gg\ell\ge1`$. The heavy part stays valid for every $`L`$: there the term is at most $`2\Omega_{\max}/\varepsilon_k\ll1\ll\varepsilon_kR`$.
- I2: Accepted and fixed in Step 6 (Rapidity identity) and Result (6.7): the error is now relative $`O(\ell^{-1}\ln\ell)`$. It is absorbed in $`O(\delta_\ell)`$, so (6.8) and (6.9) are unchanged.
- I3: Accepted and fixed in Step 8 (Size of $`R`$). The heavy condition is $`\varepsilon_kR\gg1+r^2`$. The scale $`c_0\ell/\ln\ell`$ is now given as the linear-grip scale and as a sufficient condition for every grip; with a nonzero two-quantum part the scale is $`c_0\ell/\ln^2\ell`$, up to grip-dependent constants.

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
  - Then $`L`$ large. By Poisson summation, a lattice sum differs from its value at $`L=\infty`$ by $`O(e^{-\kappa L})`$ if its summand is analytic in the strip $`\lvert\mathrm{Im}q_i\rvert<\kappa`$.
    - *Held-field sums* ($`G_0`$, $`w_0`$, $`J_2`$, $`\Gamma`$): the only singularities are the zeros of $`\Omega_q^2`$, at distance $`\simeq1/\ell`$. They need $`L\gg\ell`$.
    - *Dressed sums* ((6.3) and its $`P`$-derivatives): $`\omega`$ and $`\theta`$ are also singular at $`\lvert\mathrm{Im}q_1\rvert=\mathrm{arcsinh}(\varepsilon_k/\tau)`$, and the denominators vanish at complex $`q`$. At $`P=0`$ their smallest value on the real Brillouin zone is the isolation gap $`\Delta_k`$ of Step 3. Near a quadratic minimum, $`d(q)=\Delta_k+a_k(q_1-q_*)^2+\dots`$, the zeros lie at distance $`\simeq\sqrt{\Delta_k/a_k}`$ from the real axis. So $`\kappa_k\simeq\min\bigl(1/\ell,\ \mathrm{arcsinh}(\varepsilon_k/\tau),\ \sqrt{\Delta_k/a_k}\bigr)`$, and the finite-$`L`$ statements for a state need $`L\gg1/\kappa_k`$.
    - This control is not uniform as $`\Delta_k\to0`$. Statements at large $`L`$ are therefore made for gaps bounded below. In Step 10 the lower-branch findings ((a)–(e) and the grid findings of (6.14), (6.15)) are for $`\Delta_k>0.2\,m_h`$. The light levels (finding (f), Part G, and the light-level member of (6.14)) reach upper-branch gaps down to $`\Delta_k=0.022\,m_h`$; at that gap the torus values at $`L=128`$ and $`256`$ differ by $`0.067`$ (finding (f)). $`L`$-convergence is checked at the smallest gaps of both kinds (Part G for the lower branch, $`L=64`$ against $`128`$; finding (f) for the light levels).
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
- Second-order perturbation theory for an isolated level (Step 3) then gives (6.2) and (6.3); for an upper branch that is not isolated they define its formal coefficients (Step 3). The energy denominators are taken at $`F_0`$; the difference is $`O(\delta F^3)`$. Both expressions hold on both graphs and for every $`L`$.
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

Isolated means: separated, by a gap uniform in $`L`$, from all other states of the sector $`(k,P)`$, with any number of field quanta (question, note (a)).

**Spectrum of the sector at $`\delta F=0`$, $`P=0`$** (Step 1: energies $`E_f+\sigma'\omega(Q_n)+E_n`$).
- *Lower bound.* $`\Omega`$ is subadditive in the momentum: the map $`q\mapsto(2\lvert\sin\frac{q_i}2\rvert)_i`$ is componentwise subadditive, and $`\sqrt{m_h^2+x^2}`$ is increasing and subadditive. Hence a state with $`n\ge1`$ quanta and total momentum $`\mathbf Q`$ has $`E_n\ge\Omega_{\mathbf Q}\ge\Omega_{(Q_1,0,0)}`$. The states with $`n\ge1`$ quanta therefore lie at or above $`E_f+b_k`$ ($`\sigma'=-1`$) and $`E_f+m_h+\varepsilon_k`$ ($`\sigma'=+1`$), with $`b_k:=\min_q[\Omega_q-\omega_k(q_1)]`$. The minimum lies at $`q_2=q_3=0`$, so $`b_k`$ is the same function on both graphs, and $`b_k\le m_h-\varepsilon_k`$ (value at $`q=0`$).
- *Filling.* As $`L\to\infty`$, the lower-branch states with one quantum fill $`E_f+[b_k,\Omega_{\max}-\varepsilon_k]`$: $`q\mapsto\Omega_q-\omega_k(q_1)`$ is continuous on the connected Brillouin zone and equals $`\Omega_{\max}-\varepsilon_k`$ at $`q=(\pi,\dots,\pi)`$. States of $`n`$ pairs $`(q,q')`$ with $`q_1'=-q_1`$ fill $`E_f-\varepsilon_k+[2nm_h,2n\Omega_{\max}]`$. For $`\ell^2\ge3/(4D)`$, $`\Omega_{\max}\ge2m_h`$, so these intervals overlap, and the lower branch with $`n\ge1`$ quanta fills $`E_f+[b_k,\infty)`$.
- *Criterion.* The level $`E_f+\sigma\varepsilon_k`$ is isolated iff $`\sigma\varepsilon_k<b_k`$; otherwise it lies inside the continuum, or at its edge, as $`L\to\infty`$. The other zero-quantum level is at distance $`2\varepsilon_k`$. A strict gap persists for $`P`$ near 0 and small $`\delta F`$; the level is then analytic in $`P`$ and $`\delta F`$ (isolated eigenvalue of an analytic family).
- *Isolation gap.* $`\Delta_k:=b_k-\sigma\varepsilon_k>0`$ is the distance to the continuum. It is also the smallest denominator of (6.3) at $`P=0`$ (one quantum, own branch for $`\sigma=-1`$, other branch for $`\sigma=+1`$; two-quantum denominators are larger), so it sets a finite-size scale of its own (Setup, Limits).

**Consequences.**
- *Lower branch.* $`b_k+\varepsilon_k=\min_q[\Omega_q-\tau^2\sin^2q_1/(\omega_k+\varepsilon_k)]`$ increases with $`\varepsilon_k`$, so the lower branch is isolated iff $`\varepsilon_k>\varepsilon_-(r)`$, for a threshold $`\varepsilon_-(r)\ge0`$. Since $`2(1-\cos q_1)\ge\sin^2q_1`$, $`\Omega_q>c_0\lvert\sin q_1\rvert`$, while $`\omega-\varepsilon_k=\tau^2\sin^2q_1/(\omega+\varepsilon_k)`$ is at most $`\tau\lvert\sin q_1\rvert`$ and at most $`\tau^2\lvert\sin q_1\rvert/2\varepsilon_k`$. Hence $`\varepsilon_-=0`$ for $`r\le1`$, and $`\tau^2\le2\varepsilon_kc_0`$ suffices.
- *Upper branch.* $`b_k-\varepsilon_k`$ decreases with $`\varepsilon_k`$, so the upper branch is isolated iff $`\varepsilon_k<\varepsilon_+(r)`$, and $`\varepsilon_+\le m_h/2`$ by $`b_k\le m_h-\varepsilon_k`$. By Cauchy–Schwarz, $`2\varepsilon_k+\tau\lvert\sin q_1\rvert\le\sqrt{(2\varepsilon_k/m_h)^2+r^2}\,\sqrt{m_h^2+c_0^2\sin^2q_1}`$, so $`(2\varepsilon_k/m_h)^2+r^2<1`$ suffices. In a weakly pinned field, $`m_h=c_0/\ell`$, only *light levels*, $`\varepsilon_k<c_0/2\ell`$, have an isolated upper branch.
- *Formal coefficients.* Where the upper branch is not isolated, (6.3) is still finite and analytic in $`P`$ near 0 if its denominators do not vanish. This is condition (U): $`q\mapsto\Omega_q-\varepsilon_k-\omega(q_1)`$ and, if $`F_2\ne0`$, $`(q,q')\mapsto\Omega_q+\Omega_{q'}-\varepsilon_k-\omega(q_1+q_1')`$ have no zero on the Brillouin zone (sufficient: $`\Omega_{\max}<\varepsilon_k`$, or $`\Omega_{\max}<2\varepsilon_k`$ if $`F_2=0`$). Under (U) we call (6.2), (6.3) and all quantities built from them at $`\sigma=+1`$ *formal coefficients*. They are not coefficients of an isolated eigenvalue, and they are not an answer to items 2 and 3.
```math
(k,\sigma)\ \text{isolated}\iff b_k>\sigma\varepsilon_k;\qquad\sigma=-1:\ \varepsilon_k>\varepsilon_-(r),\ \ \varepsilon_-=0\ \text{for}\ r\le1\ (\text{and }\Leftarrow\tau^2\le2\varepsilon_kc_0);\qquad\sigma=+1:\ \varepsilon_k<\varepsilon_+(r)\le\tfrac{m_h}2\ \ (\Leftarrow(2\varepsilon_k/m_h)^2+r^2<1).
\qquad\text{(6.4)}
```
$`\mathcal S`$ denotes the set of isolated states $`(k,\sigma)`$ of a description. Model D has $`N\ge2`$ levels, so for $`r\le1`$, $`\mathcal S`$ contains the lower branches of at least two levels. The thresholds are computed in `code/v6/output/torus_mark_inertia.txt` (Part D). At $`\ell=8`$: $`\varepsilon_+=m_h/2`$ for $`r\le0.5`$, $`\varepsilon_+=0.0620\,c_0`$ at $`r=0.75`$, $`0.0260\,c_0`$ at $`r=1`$, and $`\varepsilon_+=0`$ for $`r\ge1.25`$. Further, $`\varepsilon_-=0.117,\,0.346,\,0.985,\,2.877`$ (in units of $`c_0`$) at $`r=1.25,\,1.5,\,2,\,3`$.

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
Since $`C^{(1)}\ne0`$, $`I^{(1)}=C^{(1)}/v^2`$ forces $`v=\tau`$. A single $`v`$ for every isolated state therefore exists iff $`\rho_{k,\sigma}=1`$ on $`\mathcal S`$. For $`\lvert\delta_C\rvert<1`$, $`C^{\rm mark}\ne0`$ by (6.5), so $`\rho`$ has no vanishing denominator.

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

All these integrals converge in $`\mathcal A`$ and $`a`$, so the region $`\lvert q\rvert\gg1/\ell`$ enters only the corrections. For one quantum they are of relative order $`\ell^{-1}`$. In the two-quantum sums, pairs with one soft momentum ($`\lvert q\rvert\lesssim1/\ell`$) and one of lattice order deviate from the scaling form by a nonzero finite part per soft mode, and the sum over the soft partner adds a factor $`\ln\ell`$. Against the leading order $`\ell`$ this gives a relative $`O(\ell^{-1}\ln\ell)`$. For $`D=1`$:
```math
c_0^2\langle\!\langle Q^2/E^3\rangle\!\rangle=\tfrac12\langle\!\langle1/E\rangle\!\rangle\,[1+O(\ell^{-1}\ln\ell)],\qquad\langle\!\langle1/E\rangle\!\rangle=\frac{F_1^2G_0}2+2F_2^2J_2=\frac{\ell}{4c_0^2}\Bigl(F_1^2+\frac{F_2^2}{2c_0}\Bigr)[1+O(\ell^{-1}\ln\ell)] .
\qquad\text{(6.7)}
```

**Summing the terms.** Let $`\delta_\ell:=(1+r^2+c_0/\varepsilon_k+\tau^2/\varepsilon_kc_0)\ln^2\ell/\ell`$. Sum the four terms with the weights (6.1), keep (iv) explicitly, use (6.7), and use (6.5) with $`\lvert\delta_C\rvert=O(\tau^2R/\varepsilon)`$. This gives
```math
C^{\rm mark}_{k,\sigma}=-\frac{M_k^2\ell}{4c_0^2}\Bigl(F_1^2+\frac{F_2^2}{2c_0}\Bigr)[1+O(\delta_\ell)],\qquad\zeta=\frac{F_2^2}{2c_0}[1+O(\delta_\ell)],\qquad E^{(2)\prime\prime}_{k,\sigma}(0)=-\frac{2\tau^2}{\varepsilon_k^2}\,C^{\rm mark}_{k,\sigma}\Bigl[1-\frac{r^2}2-\sigma\varepsilon_kR+O(\delta_\ell)\Bigr] .
\qquad\text{(6.8)}
```
$`\delta_\ell\ll1`$ needs $`\varepsilon_k\gg c_0\ln^2\ell/\ell>m_h/2`$. In the range of (6.8) the upper branch is therefore never isolated (6.4), and its entries there are formal coefficients.

Code check (`code/v6/output/check_mark_inertia.txt`, part B), on rings with $`L=8\ell`$ at $`\ell=512`$:
- $`G_0\cdot2c_0^2/\ell=1.00067`$; the excess is the finite-$`L`$ term $`\approx2e^{-8}`$;
- $`J_2\cdot16c_0^3/\ell=0.99938`$;
- $`C^{\rm mark}(\tau)/C^{\rm mark}(0)`$ lies within $`3.1\times10^{-3}`$ of 1.

### Step 7. Inertia against cost on the ring

Inserting (6.8) into (6.6) gives (6.9). Since $`\varepsilon_kR+\delta_\ell=O(\ln^2\ell/\ell)`$, $`\rho_{k,\sigma}\to2-r^2`$ as $`\ell\to\infty`$. In this limit $`\mathcal S`$ consists of lower branches: those of all levels for $`r\le1`$, and of the levels with $`\varepsilon_k>\varepsilon_-(r)`$ otherwise (6.4). The statement on $`v`$ is for nonempty $`\mathcal S`$.
```math
\rho_{k,\sigma}=2-r^2-2\sigma\varepsilon_kR+O(\delta_\ell),\qquad\text{at leading order in }1/\ell:\ \ I^{\rm mark}_{k,-}=\frac{(2-r^2)\,C^{\rm mark}_{k,-}}{\tau^2}\ \Rightarrow\ \bigl[\exists\,v:\ I^{(1)}=C^{(1)}/v^2,\ I^{\rm mark}=C^{\rm mark}/v^2\ \text{on }\mathcal S\bigr]\iff r=1,\ v=\tau=c_0 .
\qquad\text{(6.9)}
```
- **First difference.** $`I^{\rm mark}-C^{\rm mark}/\tau^2=(1-r^2)C^{\rm mark}/\tau^2`$.
- **Mark alone, $`r\neq1`$.** For $`r<\sqrt2`$ the mark alone has $`v_{\rm mark}^2=\tau^2/(2-r^2)`$. At $`r=\sqrt2`$, $`I^{\rm mark}=0`$ at this order; for $`r>\sqrt2`$ it has the sign opposite to $`C^{\rm mark}`$.
- **Grip dependence.** The law holds for the $`F_1^2`$ part and the $`F_2^2`$ part separately. It is therefore independent of the grip, the linear grip ($`F_2=0`$) included.
- **Upper branch.** Its formal coefficients obey the same leading law.
- **Next order in $`1/\ell`$.** For the lower branch the term $`+2\varepsilon_kR`$ (from (iv)) grows with the level. The remainder $`O(\delta_\ell)`$ is of comparable order, and its difference between two levels is not controlled. So (6.9) does not decide whether two lower levels have different $`\rho`$ at finite $`\ell`$. They do at the tested members (code check below), and in the heavy regime of (6.10) for levels whose $`\varepsilon_k`$ differ by more than its relative remainder.
- **Code check** (part B, $`\ell=512`$, $`r=1`$). For the lower branch, the $`F_1^2`$ part gives $`\rho_{1,-}=1.056`$ and $`1.072`$ ($`M_k=3,4`$), and the $`F_2^2`$ part gives $`1.211`$ and $`1.275`$. With the term (iv) removed, the values are $`1.00919`$–$`1.00920`$ and $`1.021`$–$`1.023`$ for both levels (and for the formal upper-branch coefficients). For $`r=0.5`$ and $`1.5`$ the values approach $`2-r^2`$ in the same way.
- **Order of limits.** First $`L\gg\ell`$, then $`\ell\to\infty`$ at fixed $`\varepsilon_k/c_0`$ and $`r`$. Taking $`\varepsilon_k/c_0\to\infty`$ at fixed $`\ell`$ gives a different result (Step 8). Light levels ($`\varepsilon_k<m_h/2`$, the only ones with an isolated upper branch) lie outside this limit; they are treated in Step 10.

### Step 8. Heavy body: lower branch on both graphs

**Odd part in $`\sigma`$.** Let $`\Delta=\omega(P-Q)-\omega(P)`$ and $`\Sigma=\omega(P-Q)+\omega(P)`$. The part of (6.3) odd in $`\sigma`$ is $`-M_k^2\langle\!\langle-\cos^2\vartheta\,\Delta/(E^2-\Delta^2)+\sin^2\vartheta\,\Sigma/(E^2-\Sigma^2)\rangle\!\rangle`$. At $`P=0`$ its second derivative is dominated by $`\cos^2\vartheta\,\Delta''/E^2`$, with $`\Delta''(0)=\omega''(Q)-\omega''(0)=-2\tau^2\sin^2Q_1/\varepsilon\,[1+O(\tau^2/\varepsilon^2)]`$; this is the term (iv). The remaining odd terms are smaller:
- those with $`(\cos^2\vartheta)''\Delta`$ and $`(\cos^2\vartheta)'\Delta'`$, by $`\tau^2/\varepsilon^2`$;
- the one with $`\Delta\Delta'^2/E^2`$, by $`r^2\tau^2/\varepsilon^2`$;
- the other-branch term. With $`\vartheta'(0)=\frac{\tau}{2\varepsilon}(1+\cos Q_1)[1+O(\tau^2/\varepsilon^2)]`$ and $`\Sigma=2\varepsilon[1+O(\tau^2/\varepsilon^2)]`$, its odd part adds $`\sigma\langle\!\langle(1+\cos Q_1)^2\rangle\!\rangle/(4\varepsilon\langle\!\langle1/E\rangle\!\rangle)\,[1+O((\Omega_{\max}^2+\tau^2)/\varepsilon^2)]`$ to $`\rho`$. For every $`L`$ this is at most $`\langle\!\langle1\rangle\!\rangle/(\varepsilon\langle\!\langle1/E\rangle\!\rangle)\le2\Omega_{\max}/\varepsilon`$, since $`E\le2\Omega_{\max}`$. For $`L\gg\ell\ge1`$ the sums take their $`L=\infty`$ values, where $`\langle\!\langle1\rangle\!\rangle=O(c_0^2\langle\!\langle\sin^2Q_1/E^2\rangle\!\rangle)`$; the term is then smaller than (iv) by $`c_0^2/\varepsilon^2`$. This comparison is not uniform in $`L`$. At fixed $`L`$ and $`m_h\to0`$ the uniform mode $`q=0`$ dominates $`\langle\!\langle1\rangle\!\rangle`$ and $`\langle\!\langle1/E\rangle\!\rangle`$ but has $`\sin Q_1=0`$. Then $`R=O(m_h^2)`$, while this term gives $`\rho_{k,-}-\rho^{\rm e}_k=-m_h/\varepsilon_k+O(m_h^2)`$;
- the odd part of $`\delta_C`$ in $`C^{\rm mark}`$, by $`(1+r^2)\tau^2/\varepsilon^2`$, because the even part of $`\rho`$ is $`O(1+r^2)`$ for every $`L`$: (i) gives at most 2, and (iii) gives $`r^2`$ times a lattice ratio of order 1, using $`\omega'(Q)=\tau^2\sin2Q_1/2\varepsilon`$.

So, for $`L\gg\ell\ge1`$, the part of $`\rho_{k,\sigma}`$ odd in $`\sigma`$ is $`-2\sigma\varepsilon_kR[1+O((c_0^2+\tau^2(1+r^2))/\varepsilon_k^2)]`$, and the even part $`\rho^{\rm e}_k`$ (built from the lower branch and the formal upper coefficients) is $`O(1+r^2)`$. For the lower branch this gives the first part of (6.10). At finite $`L`$ the exact expressions (6.3) and (6.6) remain; only this estimate is restricted.

**Heavy regime.** If moreover $`\varepsilon_kR\gg1+r^2`$ and $`\tau^2\ll\varepsilon_kc_0`$, the term (iv), $`2\sigma\tau^2\sin^2Q_1/\varepsilon_kE^2\,[1+O(\tau^2/\varepsilon_kc_0)]`$, dominates $`\rho`$ itself, for every $`L`$. Indeed $`E\ge c_0\lvert\sin Q_1\rvert`$ (Step 3) and $`E\ge m_h`$ give $`R\le1/c_0`$ and $`R\le1/m_h`$, so $`\varepsilon_kR\gg1`$ implies $`\varepsilon_k\gg c_0+m_h`$. The other-branch term, at most $`2\Omega_{\max}/\varepsilon_k\ll1`$, is then inside the remainder. With (6.6) this gives the second part of (6.10). It holds on both graphs, for every $`L`$ and $`\ell`$, for an isolated lower branch (6.4); in the heavy regime it is isolated, since $`\tau^2\le2\varepsilon_kc_0`$.
```math
\rho_{k,-}=\rho^{\rm e}_k+2\varepsilon_kR\Bigl[1+O\Bigl(\frac{c_0^2+\tau^2(1+r^2)}{\varepsilon_k^2}\Bigr)\Bigr]\ \ (L\gg\ell\ge1),\ \ \rho^{\rm e}_k=O(1+r^2);\qquad\text{heavy: }\ I^{\rm mark}_{k,-}=I^{(1)}_{k,-}Y_k\Bigl[1+O\Bigl(\frac{1+r^2}{\varepsilon_kR},\frac{\tau^2}{\varepsilon_kc_0}\Bigr)\Bigr],\ \ Y_k:=2M_k^2\langle\!\langle\sin^2Q_1/E^2\rangle\!\rangle>0 .
\qquad\text{(6.10)}
```
**Consequences.**
- *Heavy regime.* $`\rho_{k,-}=2\varepsilon_kR\gg1`$ at leading order, for every grip. So no single $`v`$ exists at second order, at any $`r`$ ($`r=1`$ included) and at any finite $`\ell`$ and $`L`$. Moreover, at leading order $`\rho_{k,-}`$ is proportional to $`\varepsilon_k`$: two levels whose $`\varepsilon_k`$ differ by more than the relative remainder of (6.10) have different $`\rho_{k,-}`$.
- *Upper branch.* The same sums give the formal coefficient $`\rho_{k,+}=\rho^{\rm e}_k-2\varepsilon_kR[\dots]`$. For $`\varepsilon_k\gg c_0`$ the upper branch is not isolated (6.4).

**Size of $`R`$.** The heavy regime is defined by $`\varepsilon_kR\gg1+r^2`$ (with $`\tau^2\ll\varepsilon_kc_0`$); the scale of $`\varepsilon_k`$ this needs depends on the graph and the grip. Let $`R_1`$, $`R_2`$ be the ratio $`R`$ of the $`F_1^2`$ and the $`F_2^2`$ part; $`R`$ lies between them.
- On $`D=3`$ the sums are dominated by $`\lvert q\rvert\sim1`$, and $`R`$ tends to a finite limit of order $`1/c_0`$ as $`\ell\to\infty`$. The heavy regime is then $`\varepsilon_k\gg(1+r^2)c_0`$, up to a lattice number.
- On the ring ($`L\gg\ell`$), $`R_1=\frac2\pi\frac{\ln\ell}{c_0\ell}[1+O(1/\ln\ell)]`$ (Step 6). In the two-quantum numerator the soft pairs $`1/\ell\ll\lvert q\rvert,\lvert q'\rvert\ll1`$ contribute $`\propto\iint dq\,dq'/\lvert qq'\rvert\sim\ln^2\ell`$, with nonnegative summands, and Step 6 bounds it by $`O(\ln^2\ell)`$; so $`R_2=\Theta(\ln^2\ell/c_0\ell)`$. For the linear grip the heavy regime is therefore $`\varepsilon_k\gg(1+r^2)c_0\ell/\ln\ell`$. With a fixed nonzero two-quantum part ($`F_2\ne0`$ at fixed $`\xi=F_2^2/c_0F_1^2`$) it is reached already on the smaller scale $`(1+r^2)c_0\ell/\ln^2\ell`$, up to grip-dependent constants. Since $`R\ge\min(R_1,R_2)=R_1`$ at large $`\ell`$, $`\varepsilon_k\gg(1+r^2)c_0\ell/\ln\ell`$ suffices for every grip of (G2).

**$`D=3`$ otherwise.** The scaling argument of Step 6 fails on $`D=3`$. Outside the regime of (6.10), $`\rho`$ is given by the lattice sums of (6.3). They are evaluated in Step 10.

### Step 9. Weight over inertia

Let $`\Delta W_{k,\sigma}=\sigma M_kF_1\Delta\phi/(1+2\sigma M_kF_2G_0)`$ by (2.8), with $`\Delta\phi\ne0`$. Then $`E''\Delta W=\Delta W/I`$.

**(a) $`F_1`$ and $`F_2`$ counted alike.** $`E''(0)=\sigma\tau^2/(M_k\bar F)+O(\delta F^2)`$ and $`\Delta W=\sigma M_kF_1\Delta\phi(1-2\sigma M_kF_2G_0)+O(\delta F^3)`$. Hence, on both graphs and for every $`L`$, $`\ell`$ and $`r`$,
```math
E''_{k,\sigma}(0)\,\Delta W_{k,\sigma}=\frac{\tau^2F_1\Delta\phi}{F_0}\Bigl[1-\frac{F_2w_0}{F_0}-2\sigma M_kF_2G_0\Bigr]+O(\delta F^3).
\qquad\text{(6.11)}
```
In this counting the inertia of the mark enters only at $`O(\delta F^3)`$.
- **Linear grip.** For $`F_2=0`$ exactly, (6.11) is the same for every level and both branches, but only at this order. With $`F_2=0`$, $`\Delta W`$ is exactly $`\sigma M_kF_1\Delta\phi`$, and $`E''`$ is even in $`F_1`$. The first dependence on the level is therefore the term $`-I^{\rm mark}/I^{(1)}`$ of relative order $`F_1^2`$, i.e. (6.12) with $`F_2=0`$. On the ring, at leading order in $`1/\ell`$, it vanishes only at $`r=\sqrt2`$ (below). On the cubic torus it differs between any two isolated lower levels at the computed points (Step 10).

**(b) Grips of a fixed shape.** For grips $`F=F_0\Phi(\beta q)`$ of a fixed shape, as in (2.18), $`F_1=O(\beta)`$ and $`F_2=O(\beta^2)`$. The weight of the mark ($`\propto F_1F_2`$) and its inertia ($`\propto F_1^3`$ in $`E''\Delta W`$) are then of the same order $`\beta^3`$.
- $`E''`$ is even in $`F_1`$ (symmetry $`q\to-q`$, $`p\to-p`$ of $`H`$). Through relative order $`\beta^2`$ it therefore needs only the term $`F_2w_0`$ and the $`F_1^2`$ part of $`E^{(2)}`$; the $`F_2^2`$ part is $`O(\beta^4)`$.
- By (6.6), $`\sigma M_kE^{(2)\prime\prime}(0)=-\sigma M_k\tau^4I^{\rm mark}/\varepsilon_k^2=-(\tau^2/F_0)\,I^{\rm mark}/I^{(1)}`$ at this order. Hence, on both graphs and for every $`L`$ and $`\ell`$, with $`I^{\rm mark}`$ its $`F_1^2`$ part:
```math
E''_{k,\sigma}(0)\,\Delta W_{k,\sigma}=\frac{\tau^2F_1\Delta\phi}{F_0}\Bigl[1-\frac{F_2w_0}{F_0}-2\sigma M_kF_2G_0-\frac{I^{\rm mark}_{k,\sigma}}{I^{(1)}_{k,\sigma}}\Bigr][1+O(\beta^4)].
\qquad\text{(6.12)}
```
- **Ring, leading order in $`1/\ell`$.** By (6.9), $`I^{\rm mark}/I^{(1)}=(2-r^2)C^{\rm mark}/C^{(1)}=-(2-r^2)\sigma M_kF_1^2G_0/2F_0`$. The bracket is then $`1-F_2w_0/F_0-\sigma M_kG_0[2F_2-(2-r^2)F_1^2/2F_0]`$. If $`\mathcal S`$ (lower branches, Step 7) contains at least two levels, it is the same on $`\mathcal S`$ iff $`(2-r^2)F_1^2=4F_0F_2`$. The formal upper-branch coefficients obey the same condition. At $`r=1`$ this is the square grip of (2.18). The square grip satisfies it only at $`r=1`$, and the linear grip only at $`r=\sqrt2`$.
- **Heavy regime (both graphs, every finite $`\ell`$, lower branches).** By (6.10), with $`R_1`$ the ratio $`R`$ of the $`F_1^2`$ part, $`-I^{\rm mark}_{k,-}/I^{(1)}_{k,-}=-M_k^2F_1^2G_0R_1`$ at leading order. The bracket of (6.12) is then $`1-F_2w_0/F_0+2M_kF_2G_0-M_k^2F_1^2G_0R_1`$. This is a polynomial of degree two in $`M_k`$ with leading coefficient $`-F_1^2G_0R_1\neq0`$, while $`F_2`$ enters only through the terms of degree $`\le1`$. So, at this order, no grip of (G2) gives one value at three levels. For two levels $`a,b`$ exactly one grip does: $`F_0F_2/F_1^2=R_1(\varepsilon_a+\varepsilon_b)/2`$. The rest of the range on the cubic torus is treated in Step 10.

### Step 10. Cubic torus: items 2 and 3 from the lattice sums

**Two parts (exact).** Write (6.3) as $`E^{(2)}_{k,\sigma}(P)=-M_k^2[F_1^2S_1(P)+F_2^2S_2(P)]`$. Here $`S_1`$ and $`S_2`$ are its one- and two-quantum parts per unit $`F_1^2`$ and $`F_2^2`$; they depend only on $`\varepsilon_k`$, $`\tau`$, $`\sigma`$ and the field. Put $`S_i:=S_i(0)`$ and $`\rho_i:=-(\varepsilon_k^2/\tau^2)S_i''(0)/S_i`$, the ratio of (6.6) for part $`i`$. Define the grip ratios $`\xi:=F_2^2/(c_0F_1^2)`$ and $`y:=F_0F_2/F_1^2`$; $`y=\frac14`$ is the square grip and $`y=0`$ the linear grip. Finally put $`T_{k,\sigma}:=\rho_1S_1`$ and $`t_{k,\sigma}:=T_{k,\sigma}/G_0`$. Then (6.6) gives $`I^{\rm mark}/I^{(1)}=-\sigma M_kF_1^2T_{k,\sigma}/F_0`$ for the $`F_1^2`$ part, and with (6.12):
```math
\rho_{k,\sigma}=\frac{S_1\rho_1+\xi c_0S_2\rho_2}{S_1+\xi c_0S_2},\qquad\rho_{k,\sigma}=1\iff S_1(\rho_1-1)+\xi c_0S_2(\rho_2-1)=0,\qquad[\,\cdot\,]_{(6.12)}=1-\frac{F_2w_0}{F_0}-\sigma\frac{\varepsilon_kF_1^2G_0}{F_0^2}\,(2y-t_{k,\sigma}).
\qquad\text{(6.13)}
```
- *Singular cases.* Let $`S_1,S_2>0`$ (true at all computed points, finding (a) below). A grip of (G2), i.e. a finite $`\xi\ge0`$, gives $`\rho_{k,\sigma}=1`$ in exactly two cases:
  - $`\rho_1=1`$: then $`\xi=0`$, the linear grip, works (and every $`\xi`$ if also $`\rho_2=1`$);
  - $`(\rho_1-1)(\rho_2-1)<0`$: then exactly one grip works, $`\xi=\xi^*_{k,\sigma}:=S_1(1-\rho_1)/[c_0S_2(\rho_2-1)]>0`$.

  If $`\rho_2=1\ne\rho_1`$, then $`\rho_{k,\sigma}\to1`$ only as $`\xi\to\infty`$, i.e. $`F_1\to0`$, which (G2) excludes. In all other cases no grip works.
- *Item 3 reduced.* By (6.13), the bracket of (6.12) is the same on $`\mathcal S`$ iff $`\sigma\varepsilon_k(2y-t_{k,\sigma})`$ is. Let $`\mathcal S`$ consist of lower branches, and put $`\varphi(\varepsilon):=\varepsilon\,t_{-}(\varepsilon)`$.
  - Two levels $`a\ne b`$ need exactly $`y=y_{ab}:=[\varphi(\varepsilon_b)-\varphi(\varepsilon_a)]/[2(\varepsilon_b-\varepsilon_a)]`$.
  - Three levels need the points $`(\varepsilon_k,\varphi(\varepsilon_k))`$ on one straight line.
  - The linear grip needs $`\varphi(\varepsilon_a)=\varphi(\varepsilon_b)`$.
- *Check on the ring.* At leading order in $`1/\ell`$, $`t=(2-r^2)/2`$ by (6.9), and (6.13) gives back the condition of Step 9(b).

**Isolated states.** The thresholds at $`\ell=8`$ are those of Step 3. The grid below has $`\varepsilon_k\ge0.1\,c_0>m_h/2`$, so there $`\mathcal S`$ consists of lower branches. They are evaluated where $`b_k+\varepsilon_k>0.2\,m_h`$. Light levels are treated at the end of this step.

**Evaluation** (`code/v6/output/torus_mark_inertia.txt`).
- *Setting.* Units $`c_0=F_0=1`$.
  - Part D: torus $`L=64`$, $`\ell=8`$; $`r\in\{0.1,0.25,0.5,0.75,1,1.25,1.5,2,3\}`$; 71 geometric values of $`\varepsilon_k\in[0.1,64]`$, refined to 81 equidistant points across each window.
  - Part D2: $`L=256`$, $`\ell=32`$; $`r\in\{0.1,0.5,1,1.5,2,3\}`$; 36 values.
- *Method.* $`S_1`$ is an exact mode sum and $`S_2`$ an FFT convolution (Code). $`S_i''(0)`$ is the analytic second $`P`$-derivative of the summands, so no finite-difference step enters. On $`L=12`$ the sums agree with brute-force sums to $`4\times10^{-14}`$ and $`2.5\times10^{-13}`$ (Part A). Exact diagonalisation with at most two quanta on the torus $`L=4`$ reproduces the second-order coefficients of the cost and of $`E''(0)`$ from (6.2), (6.3) to $`3.8\times10^{-9}`$ (Part E).
- *Curvature and finite size at the smallest gaps* (Part G). The test points are the light levels at $`f=0.9`$ (gaps down to $`0.022\,m_h`$) and the lower-branch grid points nearest their threshold (gaps $`0.279`$–$`0.455\,m_h`$ at $`\ell=8`$, $`m_h`$ at $`\ell=32`$).
  - Richardson differences approach the analytic $`\rho_1`$, asymptotically like $`h^4`$. At the step $`h_0`$ of v3 they deviate by up to $`15`$ (ring) and $`0.11`$ (torus) at the light levels and by $`8\times10^{-3}`$ at the lower-branch points; at $`h_0/4`$, by $`0.019`$, $`1.5\times10^{-4}`$ and $`3\times10^{-5}`$. For $`\rho_2`$ the deviation is at most $`6\times10^{-6}`$.
  - At the lower-branch points, $`L=64`$ and $`L=128`$ ($`\ell=8`$) give $`\rho_i`$ within $`1.6\times10^{-4}`$.
- *Change with $`\ell`$* (Parts B, B2; $`L=8\ell`$ throughout), over the points of Part C, from $`(L,\ell)=(64,8)`$ to $`(256,32)`$:
  - for $`\varepsilon_k\le4c_0`$, $`\rho_1`$, $`\rho_2`$ and $`t`$ change by at most $`0.093`$, $`0.012`$ and $`0.058`$;
  - above, by at most $`2.7\%`$, $`0.8\%`$ and $`2.8\%`$;
  - nearer the lower threshold the change is larger: at $`r=3`$, $`\varepsilon_k=4c_0`$, $`\rho_{1,-}=1.95`$, $`1.71`$, $`1.61`$ at $`\ell=8`$, $`16`$, $`32`$.

**Findings at the computed points** (numerical: grid, refinement and roots; nothing is claimed between computed points).
- (a) At every computed point, $`S_i(0)`$ is at least its held value, so $`S_1,S_2>0`$.
- (b) $`\rho_{1,-}`$ and $`\rho_{2,-}`$ increase along the grid at every $`r`$. At $`r=1`$, $`\ell=8`$, they go from $`0.28`$ and $`0.06`$ at $`\varepsilon_k=0.1\,c_0`$ to $`30.6`$ and $`16.8`$ at $`64\,c_0`$.
- (c) *Windows.* By (6.13), a finite grip with $`\rho_{k,-}=1`$ needs $`\rho_{1,-}=1`$ or $`(\rho_{1,-}-1)(\rho_{2,-}-1)<0`$.
  - *Roots.* In each grid interval where $`\rho_{i,-}-1`$ changes sign, the root of $`\rho_{i,-}(\varepsilon)=1`$ is found by Brent's method on the lattice sums. Its estimated numerical error is below $`2\times10^{-10}`$: residual over slope, and for $`\rho_2`$ also the binning error, estimated from a lattice with half the energy step.
  - *Windows.* The windows are the intervals between consecutive roots (or the edge of the computed range) on which $`(\rho_{1,-}-1)(\rho_{2,-}-1)<0`$. At every computed point, grid and refinement (98–152 points per $`r`$), a finite grip exists iff the point lies in a window. Values in units of $`c_0`$, at $`\ell=8`$ with $`\ell=32`$ in brackets.
  - For $`r\le2`$ the window runs from the root of $`\rho_{1,-}=1`$, attained by the linear grip, to the root of $`\rho_{2,-}=1`$, not attained ($`\xi^*\to\infty`$):
    - $`r=0.1`$: $`[0.9721,2.6683)`$ $`([0.9274,2.6406))`$;
    - $`r=1`$: $`[0.9123,2.6119)`$ $`([0.8957,2.5838))`$;
    - $`r=1.5`$: $`[0.8447,2.5342)`$ $`([0.8909,2.5053))`$;
    - $`r=2`$: $`[1.3385,2.4089)`$ $`([1.4187,2.3785))`$.

    $`\xi^*_{k,-}`$ increases along the refined grid. The refined point $`\varepsilon=1.434`$ ($`\ell=32`$, $`r=2`$, $`\xi^*=0.5056`$) lies inside its window.
  - At $`r=3`$, $`\rho_{2,-}>1`$ at all computed points. The window runs from the edge of the computed range, $`3.043`$ ($`3.337`$), to the root of $`\rho_{1,-}=1`$ at $`3.5649`$ ($`3.6997`$), which the linear grip attains. $`\xi^*`$ decreases along it.
- (d) $`\varphi`$ increases along the grid at every $`r`$. Its discrete second differences are positive at all grid points for $`r\le1`$. For $`r\ge1.25`$ they are negative in a band just above the lower threshold: $`[0.174,0.209]`$ at $`r=1.25`$, $`[0.438,0.634]`$ ($`[0.527,0.634]`$) at $`r=1.5`$, $`[1.209,1.749]`$ ($`[1.326,1.595]`$) at $`r=2`$, and $`[3.337,4.827]`$ ($`[4.014,4.827]`$) at $`r=3`$.
- (e) *Large $`\varepsilon_k`$.* $`R_1=0.232/c_0`$ ($`0.229/c_0`$ at $`\ell=32`$). At $`\varepsilon_k=64\,c_0`$, $`\rho_{1,-}-2\varepsilon_kR_1=0.75`$–$`0.88`$ ($`0.58`$–$`0.91`$) and $`\rho_{1,-}/(2\varepsilon_kR_1)=1.025`$–$`1.030`$ ($`1.020`$–$`1.031`$), as (6.10) describes.
- (f) *Light levels* (Part F): $`\ell=8`$, $`\varepsilon_k=f\varepsilon_+(r)`$ with $`f\in\{0.3,0.5,0.7,0.9\}`$ and $`r\in\{0.25,0.5,0.75,1\}`$, so both branches are isolated.
  - On the ring ($`L=2048`$; $`L=4096`$ for the $`F_1^2`$ part, the same to four digits), $`\rho_{1,+}\in[-65.2,-0.52]`$, $`\rho_{2,+}\in[-0.85,-0.13]`$, and $`\rho_{1,-},\rho_{2,-}\in[0.1065,0.7715]`$.
  - On the torus ($`L=128`$, $`256`$), $`\rho_{i,+}\in[-1.277,-0.0049]`$ and $`\rho_{i,-}\in[0.0049,0.1473]`$. The two sizes agree to $`0.003`$, except at $`r=1`$, $`f=0.9`$ (gap $`0.022\,m_h`$), where $`\rho_{1,+}=-1.277`$ and $`-1.210`$.
  - So at every light-level point both parts of both branches have $`\rho_i<1`$, and by (6.13) no grip gives $`\rho=1`$ for either branch.

**Item 2.** By (6.6) a single $`v`$ must be $`\tau`$, and it needs $`\rho_{k,\sigma}=1`$ on $`\mathcal S`$ with one common grip. By (6.13) each isolated state then needs $`\rho_1=1`$ or $`(\rho_1-1)(\rho_2-1)<0`$.
- *Negative for the class, by members with margins.* Take $`r=1`$, where $`\mathcal S`$ contains the lower branches of all levels (6.4).
  - A description with a level at $`\varepsilon_k=4c_0`$: $`\rho_{1,-}=2.6235`$ and $`\rho_{2,-}=1.4061`$ at $`\ell=8`$ ($`2.6102`$ and $`1.4175`$ at $`\ell=32`$). So $`\rho_{k,-}\ge1.40`$ for every grip.
  - Two levels at $`1.2\,c_0`$ and $`2\,c_0`$, both in the window, need $`\xi^*=1.96`$ and $`16.40`$ ($`2.105`$ and $`17.38`$ at $`\ell=32`$).
  - Any description with a light level at a point of (f).
- *Members found on the grid.* One $`v`$ exists exactly when $`\mathcal S`$ is the lower branch of a single level with $`\varepsilon_k`$ in the window of (c) and $`\xi=\xi^*_{k,-}`$; then $`v=\tau`$.
  - Since $`N\ge2`$, this requires $`r>1`$ with all other levels at or below $`\varepsilon_-(r)`$; for $`r\ge1.25`$ there are no light levels.
  - For $`r\le1`$, $`\mathcal S`$ contains at least two lower levels. On the refined grid distinct points of the window have distinct $`\xi^*`$, and outside it no grip works, so no member with its levels on the grid has one $`v`$.
```math
D=3,\ \text{grid of Step 10}:\ \ \bigl[\exists\,v:\ I^{(1)}=C^{(1)}/v^2,\ I^{\rm mark}=C^{\rm mark}/v^2\ \text{on }\mathcal S\bigr]\iff\mathcal S=\{(k,-)\},\ \varepsilon_k\ \text{in the window},\ \xi=\xi^*_{k,-}\ (\text{then }v=\tau);\qquad r=1,\ \varepsilon_k=4c_0:\ \rho_{k,-}\ge1.40\ \text{for every grip}.
\qquad\text{(6.14)}
```
- The first difference is $`I^{\rm mark}-C^{\rm mark}/\tau^2=(\rho_{k,\sigma}-1)\,C^{\rm mark}/\tau^2`$.
- Order of limits: $`L\gg\ell`$, then $`\ell`$ large. Unlike on the ring, the sums have finite limits as $`\ell\to\infty`$; the findings are stated at $`\ell=8`$ and $`\ell=32`$.

**Item 3** ($`\mathcal S`$ without light levels; with them it is not evaluated).
- *Negative for the class, by a member with margins.* Take $`r=1`$ and the levels $`\varepsilon_k=(1,2,3)\,c_0`$: Model D with $`m=d_1=c_0/F_0`$, $`N=3`$, all three lower branches isolated. Then $`y_{12}=0.563`$ and $`y_{23}=0.804`$ at $`\ell=8`$ ($`0.561`$ and $`0.798`$ at $`\ell=32`$), so no grip of (G2) works.
- *Linear grip.* By (d), $`y_{ab}>0`$ for any two grid levels, so $`y=0`$ fails for any two isolated lower levels on the grid.
- *Members found on the grid.*
  - If $`\mathcal S`$ has two lower levels, exactly one grip works, $`y=y_{ab}`$. It depends on the levels and on $`r`$: at $`r=1`$, $`y_{ab}=0.25,0.37,0.56,0.92,1.62`$ for $`(\varepsilon_a,\varepsilon_b)/c_0=(0.25,0.5),(0.5,1),(1,2),(2,4),(4,8)`$, and $`0.26,0.37,0.56,0.91,1.605`$ at $`\ell=32`$ (direct evaluation at these levels).
  - If $`\mathcal S`$ has three or more lower levels at grid points where $`\varphi`$ has positive discrete second differences (all grid points for $`r\le1`$), no grip works, since the chord slopes of $`\varphi`$ then increase.
  - The square grip, which gives (6.12) on the ring at $`r=1`$, works only for pairs with $`y_{ab}=\frac14`$; it is not singled out.
```math
D=3:\ \ E''_{k,\sigma}(0)\,\Delta W_{k,\sigma}\ \text{the same on }\mathcal S\iff\sigma\varepsilon_k(2y-t_{k,\sigma})\ \text{the same on }\mathcal S;\qquad r=1,\ \varepsilon_k=(1,2,3)\,c_0:\ y_{12}=0.563\ne y_{23}=0.804\ \Rightarrow\ \text{no grip of (G2)} .
\qquad\text{(6.15)}
```

## Result

- **(6.2), (6.3)** [formula]. Class: ring and cubic torus, every $`L`$, $`M\to\infty`$ first, every isolated state (6.4), $`P`$ near 0. The level is $`E_f+\sigma\sqrt{M_k^2\bar F^2+\tau^2\sin^2P}+E^{(2)}_{k,\sigma}(P)`$ up to $`O(\delta F^3)`$, with $`E^{(2)}`$ the spectral sum (6.3) over one- and two-quantum states; it is even in $`P`$. For an upper branch that is not isolated, under (U), the same expressions are its formal coefficients.
- **(6.4)** [criterion]. Both graphs, $`\ell^2\ge3/(4D)`$, $`L\to\infty`$, $`\delta F\to0`$. $`(k,\sigma)`$ is separated by a gap from every sector of field excitations, and then analytic in $`P`$ near 0 and in $`\delta F`$, iff $`b_k=\min_q[\Omega_q-\omega_k(q_1)]>\sigma\varepsilon_k`$.
  - Lower branch: iff $`\varepsilon_k>\varepsilon_-(r)`$; $`\varepsilon_-=0`$ for $`r\le1`$, and $`\tau^2\le2\varepsilon_kc_0`$ suffices.
  - Upper branch: iff $`\varepsilon_k<\varepsilon_+(r)\le m_h/2`$, so only for light levels; $`(2\varepsilon_k/m_h)^2+r^2<1`$ suffices.
  - Otherwise the upper-branch coefficients are formal, finite under (U).
- **(6.5)** [formula]. Same class. $`C^{(1)}_{k,\sigma}=\sigma M_k\bar F`$ for every $`\tau`$. $`C^{\rm mark}_{k,\sigma}=E^{(2)}_{k,\sigma}(0)=-M_k^2(F_1^2G_0/2+2F_2^2J_2)(1+\delta_C)`$, with $`\delta_C`$ as in (6.5) at first order in $`\tau^2`$. The held mark is strictly negative.
- **(6.6)** [theorem]. Same class, $`\tau>0`$, exact at its order: $`I^{(1)}_{k,\sigma}=C^{(1)}_{k,\sigma}/\tau^2`$ for every isolated state and every $`r`$; $`I^{\rm mark}=-\varepsilon_k^2E^{(2)\prime\prime}(0)/\tau^4`$. A single $`v`$ for all isolated states exists iff $`\rho_{k,\sigma}=1`$ on $`\mathcal S`$, and then $`v=\tau`$.
- **(6.7)** [formula]. Ring, $`L\gg\ell`$: $`c_0^2\langle\!\langle Q^2/E^3\rangle\!\rangle=\frac12\langle\!\langle1/E\rangle\!\rangle[1+O(\ell^{-1}\ln\ell)]`$ and $`\langle\!\langle1/E\rangle\!\rangle=\frac{\ell}{4c_0^2}(F_1^2+F_2^2/2c_0)[1+O(\ln\ell/\ell)]`$.
- **(6.8)** [formula]. Ring, $`L\gg\ell`$, under (6.4) (for $`\sigma=+1`$: formal coefficients, since the upper branch is not isolated where $`\delta_\ell\ll1`$), up to relative $`O(\delta_\ell)`$: $`C^{\rm mark}_{k,\sigma}=-\frac{M_k^2\ell}{4c_0^2}(F_1^2+\frac{F_2^2}{2c_0})`$, $`\zeta=F_2^2/2c_0`$, and $`E^{(2)\prime\prime}(0)=-\frac{2\tau^2}{\varepsilon_k^2}C^{\rm mark}[1-\frac{r^2}2-\sigma\varepsilon_kR]`$, with $`R=O(\ln^2\ell/c_0\ell)`$.
- **(6.9)** [theorem]. Ring, $`L\gg\ell`$, every (G2) grip, every $`r>0`$, isolated lower branches (all levels for $`r\le1`$, levels with $`\varepsilon_k>\varepsilon_-(r)`$ otherwise). $`\rho_{k,-}=2-r^2+2\varepsilon_kR+O(\delta_\ell)`$, with $`\varepsilon_kR=O((\varepsilon_k/c_0)\ln^2\ell/\ell)`$. At leading order in $`1/\ell`$ (first $`L\to\infty`$, then $`\ell\to\infty`$ at fixed $`\varepsilon_k/c_0`$ and $`r`$, where $`\mathcal S`$ contains only lower branches), $`I^{\rm mark}_{k,-}=(2-r^2)C^{\rm mark}_{k,-}/\tau^2`$. Hence, for nonempty $`\mathcal S`$, one $`v`$ with $`I^{(1)}=C^{(1)}/v^2`$ and $`I^{\rm mark}=C^{\rm mark}/v^2`$ on $`\mathcal S`$ exists iff $`r=1`$, and then $`v=\tau=c_0`$. The first difference is $`(1-r^2)C^{\rm mark}/\tau^2`$. The formal upper-branch coefficients obey the same leading law.
- **(6.10)** [negative]. Both graphs, isolated lower branch with $`\varepsilon_k\gg c_0`$ and $`\varepsilon_k^2\gg\tau^2(1+r^2)`$. For $`L\gg\ell\ge1`$: $`\rho_{k,-}=\rho^{\rm e}_k+2\varepsilon_kR\,[1+O((c_0^2+\tau^2(1+r^2))/\varepsilon_k^2)]`$, with $`\rho^{\rm e}_k=O(1+r^2)`$; this estimate is not uniform at finite $`L`$ (uniform mode, Step 8). In the heavy regime (additionally $`\varepsilon_kR\gg1+r^2`$ and $`\tau^2\ll\varepsilon_kc_0`$), for every $`L`$ and $`\ell`$: $`I^{\rm mark}_{k,-}=I^{(1)}_{k,-}Y_k`$ and $`\rho_{k,-}=2\varepsilon_kR\gg1`$ at leading order. So no single $`v`$ exists at second order, at any $`r`$ ($`r=1`$ included) and at any finite $`\ell`$ and $`L`$. At leading order $`\rho_{k,-}\propto\varepsilon_k`$, so levels whose $`\varepsilon_k`$ differ by more than the relative remainder have different $`\rho_{k,-}`$.
- **(6.11)** [criterion]. Both graphs, every $`L`$, $`\ell`$, $`r`$, isolated states, at second order in $`\delta F`$ with $`F_1`$ and $`F_2`$ counted alike, with the weights (2.8): $`E''\Delta W=\frac{\tau^2F_1\Delta\phi}{F_0}[1-F_2w_0/F_0-2\sigma M_kF_2G_0]`$. At this order it is the same on $`\mathcal S`$ (with at least two states) iff $`F_2=0`$, independently of $`r`$. For $`F_2=0`$ the first dependence on the level comes from $`I^{\rm mark}`$ at relative order $`F_1^2`$, given by (6.12) with $`F_2=0`$. On the ring, at leading order in $`1/\ell`$, it vanishes only at $`r=\sqrt2`$. On the cubic torus it differs between any two isolated lower levels at the computed points (6.15).
- **(6.12)** [criterion]. Grips of fixed shape through relative order $`\beta^2`$, weights (2.8), both graphs, every $`L`$ and $`\ell`$, isolated states: $`E''\Delta W=\frac{\tau^2F_1\Delta\phi}{F_0}[1-F_2w_0/F_0-2\sigma M_kF_2G_0-I^{\rm mark}/I^{(1)}]`$.
  - Ring ($`L\gg\ell`$, leading order in $`1/\ell`$), $`\mathcal S`$ with at least two levels: the same on $`\mathcal S`$ iff $`(2-r^2)F_1^2=4F_0F_2`$. At $`r=1`$ this holds iff the grip is the square grip; for the linear grip it holds only at $`r=\sqrt2`$.
  - Heavy regime of (6.10), lower branches, at leading order: the bracket is a polynomial of degree two in $`M_k`$ with leading coefficient $`-F_1^2G_0R_1\ne0`$. No grip of (G2) makes it the same for three levels; for two levels $`a,b`$ exactly one grip does, $`F_0F_2/F_1^2=R_1(\varepsilon_a+\varepsilon_b)/2`$.
- **(6.13)** [formula]. Both graphs, every $`L`$ and $`\ell`$, isolated states. $`\rho_{k,\sigma}`$ is the mean of $`\rho_1,\rho_2`$ with weights $`S_1`$, $`\xi c_0S_2`$, and $`\rho_{k,\sigma}=1`$ iff $`S_1(\rho_1-1)+\xi c_0S_2(\rho_2-1)=0`$. For $`S_1,S_2>0`$ a grip of (G2) achieves this iff $`\rho_1=1`$ (with $`\xi=0`$, the linear grip; every $`\xi`$ if also $`\rho_2=1`$) or $`(\rho_1-1)(\rho_2-1)<0`$ (exactly one $`\xi=\xi^*_{k,\sigma}>0`$). If $`\rho_2=1\ne\rho_1`$ no grip does. The bracket of (6.12) is $`1-F_2w_0/F_0-\sigma(\varepsilon_kF_1^2G_0/F_0^2)(2y-t_{k,\sigma})`$.
- **(6.14)** [negative]. Cubic torus, every grip of (G2), isolated states. A single $`v`$ on $`\mathcal S`$ requires $`\rho_{k,\sigma}=1`$ on $`\mathcal S`$ with one grip, and then $`v=\tau`$ (exact).
  - Negative for the class, by members with margins at $`r=1`$: a level at $`\varepsilon_k=4c_0`$ has $`\rho_{k,-}\ge1.40`$ for every grip ($`\ell=8`$ and $`32`$, both parts). Two levels at $`1.2\,c_0`$ and $`2\,c_0`$ need different $`\xi^*`$. A light level at the points of Part F has $`\rho<1`$ for both branches and every grip.
  - Numerical finding at the computed points (grid and refinement; $`L=8\ell`$, $`\ell=8`$ and $`32`$, $`r\in[0.1,3]`$, $`\varepsilon_k/c_0\in[0.1,64]`$ with lower gap $`>0.2\,m_h`$, where $`\mathcal S`$ has only lower branches): one $`v`$ exists exactly when $`\mathcal S`$ is the lower branch of a single level, with $`\varepsilon_k`$ in the window of Step 10 (c) and $`\xi=\xi^*_{k,-}`$. The window ends are roots of $`\rho_{1,-}=1`$ and $`\rho_{2,-}=1`$, found to within $`2\times10^{-10}`$. At $`r=1`$, $`\ell=8`$ the window is $`[0.9123,2.6119)\,c_0`$; its lower end is attained by the linear grip, its upper end is not. This requires $`r>1`$. For the computed $`r\le1`$ ($`r=1`$ included) no member with its levels on the grid has one $`v`$.
  - The first difference is $`(\rho_{k,\sigma}-1)C^{\rm mark}/\tau^2`$.
- **(6.15)** [criterion]. Cubic torus, isolated states without light levels, relative order $`\beta^2`$, weights (2.8). $`E''\Delta W`$ is the same on $`\mathcal S`$ iff $`\sigma\varepsilon_k(2y-t_{k,\sigma})`$ is (exact); for lower branches, two levels need $`y=y_{ab}`$ and three need $`(\varepsilon_k,\varphi(\varepsilon_k))`$ collinear.
  - Negative for the class, by a member with margins: at $`r=1`$ the levels $`(1,2,3)\,c_0`$ give $`y_{12}=0.563\ne y_{23}=0.804`$ ($`0.561\ne0.798`$ at $`\ell=32`$), so no grip works.
  - Numerical finding at the grid points of (6.14): with two lower levels exactly one grip works, $`y=y_{ab}`$, depending on the levels and on $`r`$. With three or more lower levels where $`\varphi`$ is discretely convex (all grid points for $`r\le1`$) no grip works. The linear grip fails for any two lower levels, and the square grip is not singled out.

## Consistency checks

1. Held limit $`\tau\to0`$: $`\theta=0`$ and $`\omega=\varepsilon_k`$, so $`E^{(2)}(0)=-M_k^2(F_1^2G_0/2+2F_2^2J_2)`$. This is the second-order part of $`C^{\rm mark}`$ in (2.6), with $`\mu^2=M_k^2`$, $`D_\mu=1+O(\delta F)`$ and $`\zeta=4F_2^2J_2/G_0`$.
2. Bare body ($`\delta F=0`$, $`F_0=1`$): $`E''(0)=\sigma\tau^2/M_k`$, which is $`\omega_k''(0)`$ of (6.7) of 04-ilang-time/06-inertia-internal-energy (mirrored for $`\sigma=-1`$).
3. Dimensions:
   - $`[\tau]=[c_0]=[m_h]=[M_k]=`$ cost, $`[q^2]=`$ cost$`^{-1}`$, $`[F_1^2]=[F_2^2/c_0]=`$ cost, $`[G_0]=`$ cost$`^{-2}`$;
   - $`C^{\rm mark}`$ is a cost, $`I`$ and $`C/\tau^2`$ are cost$`^{-1}`$, $`r`$ is dimensionless;
   - $`E''\Delta W`$ and $`\tau^2F_1\Delta\phi/F_0`$ are cost$`^2`$.

## Open issues

- Cubic torus: the findings of (6.14) and (6.15) hold at the grid points of Step 10 ($`L=64`$, $`\ell=8`$ and $`L=256`$, $`\ell=32`$; $`r\in[0.1,3]`$; $`\varepsilon_k/c_0\in[0.1,64]`$; lower branch at least $`0.2\,m_h`$ above its threshold; light levels at the points of Part F). Nothing is claimed between grid points, for $`r>3`$, closer to the lower threshold, or in the limit $`\ell\to\infty`$. Near the threshold the values still change with $`\ell`$.
- Light levels: item 3 is not evaluated for descriptions with a light level, and item 2 only at the points of Part F ($`\ell=8`$).
- Finite size near threshold: the control of the dressed sums in $`L`$ is not uniform as the isolation gap $`\Delta_k\to0`$ (Setup, Limits). Lower branches with $`\Delta_k\le0.2\,m_h`$ are not evaluated. At the light level nearest its boundary ($`\Delta_k=0.022\,m_h`$), the torus values at $`L=128`$ and $`256`$ still differ by $`0.067`$.
- Upper branch outside $`\mathcal S`$: only its formal coefficients are given. How the embedded level behaves beyond second order (its decay into the continuum) is not computed.
- The weight of the moving body is taken from (2.8) without corrections in $`\tau`$; (6.11) and (6.12) rest on this.
- On the ring the expansion parameter grows like $`\ell`$, so (6.8)–(6.12) need $`\delta F`$ to shrink as $`\ell`$ grows. The regime $`M_kF_1^2G_0\sim F_0`$ is open.

## Code

- `code/v6/check_mark_inertia.py` (role: check). It is the v1 script, unchanged, run again; its output `code/v6/output/check_mark_inertia.txt` is identical to that of v1–v5.
- **Part A** (the check required by the question).
  - *Setting.* Ring of $`L=32`$ cells, $`c_0=1`$, $`m_h=0.25`$, $`F_0=1`$. A square grip ($`F_1=0.3`$, $`F_2=0.0225`$) and another grip ($`F_1=0.3`$, $`F_2=-0.15`$); levels $`M_k=3,4`$; both branches; $`r=0.5,1,1.5`$.
  - *Independent computation.* Exact diagonalisation of the total contract restricted to states with at most two field quanta, in the sector $`P`$ (dimension 1122). $`E''(0)`$ is the exact second derivative of the eigenvalue, from the eigen-decomposition. The coefficient of $`s^2`$ is fitted from $`\delta F\to s\,\delta F`$ with $`s=\pm0.01,\pm0.02,\pm0.04`$.
  - *Formula side.* (6.2), (6.3), (6.5) are evaluated as lattice sums.
  - *Results.* The second-order coefficients of $`\mathrm{Cost}_{k,\sigma}`$ and $`E''_{k,\sigma}(0)`$ agree to a maximal relative deviation of $`2.26\times10^{-7}`$. The first-order coefficients agree to $`\le2.6\times10^{-8}`$ absolute. The zeroth order reproduces $`\sigma F_0M_k`$ and $`\sigma\tau^2/F_0M_k`$.
  - At these parameters ($`\varepsilon_k\ge3>m_h/2`$) the upper branch is not isolated (6.4). Its rows are formal coefficients, which the restricted diagonalisation reproduces as well; the lower-branch rows are those of isolated states.
- **Part B.** Formula (6.3) on rings with $`L=8\ell`$, $`\ell=16,\dots,512`$. It reports $`\rho`$ of the $`F_1^2`$ and $`F_2^2`$ parts against $`2-r^2`$, the same values without the term (iv), the held sums against (6.7), and $`C^{\rm mark}(\tau)/C^{\rm mark}(0)`$; the $`\sigma=+1`$ rows are formal coefficients. These are the numbers quoted in Steps 6 and 7.
- `code/v6/torus_mark_inertia.py` (role: computation). It is the v4 script, unchanged, run again; its output `code/v6/output/torus_mark_inertia.txt` is identical to that of v4 and v5.
  - It evaluates the lattice sums of (6.3) for the $`F_1^2`$ and $`F_2^2`$ parts separately (units $`c_0=F_0=1`$, $`\varepsilon_k=M_k`$), at isolated states only, except in Part E.
  - Two-quantum sums: the one-quantum energies of each $`q_1`$ are binned with linear weights (step $`10^{-3}`$). The pair distribution per total $`q_1`$ is their convolution, computed by FFT, and the binning variance is removed to second order.
  - $`S_i''(0)`$: analytic second derivative in $`P`$ of each summand (of $`\cos^2\vartheta`$, $`\sin^2\vartheta`$ and the denominators, through $`\omega'`$, $`\omega''`$, $`\theta'`$, $`\theta''`$), summed with the same weights.
  - Crossings $`\rho_{i,-}=1`$: Brent's method in each sign-changing grid interval; error estimate from the residual, the slope, and for $`\rho_2`$ a lattice with energy step $`5\times10^{-4}`$. The windows are built from the roots and checked against all computed points.
  - Thresholds $`\varepsilon_\pm(r)`$ from $`b_k`$ at $`L=\infty`$.
  - *Part A:* mode-class and pair sums against brute-force sums on $`L=12`$.
  - *Parts B, B2:* convergence in $`L`$ and $`\ell`$, both parts, up to $`(L,\ell)=(256,32)`$.
  - *Part C:* table of $`S_i(0)`$ relative to the held value, $`\rho_1`$, $`\rho_2`$, $`t`$ and $`\xi^*`$ on $`L=64`$, $`\ell=8`$.
  - *Part D:* fine grid in $`\varepsilon_k`$ for nine values of $`r`$ on $`L=64`$, $`\ell=8`$. It gives the thresholds, monotonicity of $`\rho_{i,-}`$ at the grid points, the crossings $`\rho_{i,-}=1`$, the points with a finite $`\xi^*_{k,-}`$, monotonicity and discrete convexity of $`\varphi`$, $`y_{ab}`$, and the members with margins.
  - *Part D2:* Part D on $`L=256`$, $`\ell=32`$, both parts.
  - *Part E:* exact diagonalisation of the contract restricted to at most two field quanta on the torus $`L=4`$ (dimension 4290), against (6.2), (6.3) for both branches ($`\sigma=+1`$ formal).
  - *Part F:* light levels on the ring ($`L=2048`$, $`4096`$) and the torus ($`L=128`$, $`256`$), $`\ell=8`$.
  - *Part G:* at the light levels with $`f=0.9`$ and the lower-branch grid points nearest threshold, the analytic $`\rho_i`$ against Richardson differences with steps $`h_0=\min(10^{-2},0.05\,\varepsilon_k/\tau)`$, $`h_0/2`$, $`h_0/4`$, and $`L=64`$ against $`L=128`$ at $`\ell=8`$.
  These are the numbers quoted in Steps 3 and 10.

## Methods used

- Rayleigh–Schrödinger perturbation theory for an isolated eigenvalue in a sector of a conserved label; analyticity of isolated eigenvalues
- Fourier analysis on ring and torus; normal modes and Wick's theorem for the oscillator field
- Asymptotics of lattice sums dominated by a scaling region; rapidity substitution; Poisson summation
- Exact diagonalisation in a truncated Fock space; second derivative of an eigenvalue from its eigen-decomposition (code check)
- Spectrum of a sector: continuum edges from the subadditivity of the field dispersion; isolation by a uniform gap
- Numerical lattice sums on the cubic torus: FFT convolution of linearly binned energies with a variance correction, analytic differentiation of the summands in $`P`$ (checked against Richardson finite differences), Brent root-finding, convergence in $`L`$ and $`\ell`$; monotonicity and convexity at grid points
- Finite-size errors from the analyticity strip of the summands (Poisson summation), including the zeros of the energy denominators
