# Inertia of a pair bound through a field of oscillator cells

- **Subproject:** 08-ilang-propagation
- **Package:** 07-bond-inertia
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-25

## Setup and assumptions

**Description (M8, M9, A15).** Ring of $`L`$ oscillator cells, contract $`H=\sum_x\tfrac12p_x^2+\tfrac{\kappa_h}2\sum_x(q_{x+1}-q_x)^2+\tfrac{m_h^2}2\sum_xq_x^2`$ plus the terms of the bodies, $`\Phi_x=q_x`$; $`c_0=\sqrt{\kappa_h}`$, $`\ell=c_0/m_h`$, $`\ell\gg1`$. Two Model D bodies of different types; the own contract of body $`i`$ is its motion term $`A_i`$ (strength $`\tau`$ for both, a condition, M7), its grip is $`\sum_x\lvert x\rangle\langle x\rvert\otimes S_i\otimes F(q_x)`$, $`S_i=\sigma_3\otimes(m_i\mathbb 1+D_i)`$, with the common grip $`F(q)=F_0+F_1q+F_2q^2`$, $`F_0>0`$, $`F_1\neq0`$ (a condition, M7). No pair term between the bodies. A body step is a field step ($`k=1`$ in (4.17)), so by (5.11) and (4.17) the maximal speed of each body is $`\tau`$ cells per unit $`\lambda`$ and equals the speed of the field iff $`r:=\tau/c_0=1`$. $`s:=4F_0F_2/F_1^2`$ labels the grip: $`s=1`$ is the square grip of (2.18), $`s=0`$ the linear grip.

**Quoted inputs.** (2.11) of 08-ilang-propagation/02-grip-weight: $`U(\mathbf r)=-\mu_1\mu_2\bigl[F_1^{2}G(\mathbf r)+4F_2^{2}J_2(\mathbf r)\bigr]+O(\mu^3)`$ in (G2), with $`G=(K^{-1})_{x+r,x}`$, $`J_2=\int_0^\infty\Gamma_r(t)^2dt`$, $`\Gamma_r(t)=\langle q_{x+r}e^{-(H-E_f)t}q_x\rangle`$; $`U`$ has the sign of $`-\mu_1\mu_2`$. (2.18) there: the static bond of held bodies is weighed like the rest cost, $`\rho_{{\rm bond},i}=m_{\mathbf r}`$, for every level and both branches iff the grip is square, at leading order in the grip. (4.17) of 04-formation, (5.11) of 04-ilang-time/05-moving-clock, and (6.7) of 04-ilang-time/06-inertia-internal-energy: $`M_k=m+d_k`$, gap $`2M_k`$, $`\omega_k''(0)=\tau^2/M_k`$.

**Notation.** Field modes $`q\in\frac{2\pi}L\mathbb Z_L`$, $`\omega_q^2=m_h^2+4\kappa_h\sin^2\frac q2`$ (the eigenvalues of $`K`$), $`w_0=\langle q_x^2\rangle=\frac1L\sum_q\frac1{2\omega_q}`$, $`\bar a=\langle F(q_x)\rangle=F_0+F_2w_0`$. Clock level $`k_i`$ and branch $`\sigma_i`$ of body $`i`$; $`\mu_i=\sigma_iM_{k_i}`$, $`\bar M_i=\bar aM_{k_i}`$, $`\lambda_{C,i}=\tau/\bar M_i`$ (the length, in cells, below which the band of body $`i`$ is not quadratic).

**Assumptions and regime.**
- (A) $`M\to\infty`$ first: the eigenvalues of $`C_M`$ plus the body terms below any fixed bound converge to those of $`H`$ plus the body terms (strong resolvent convergence of the compressions, standard), and every statement is about this limit. Then $`L\to\infty`$ for the separated reference (with $`L\gg\ell,a_b`$ for the bound level), then the regime limits below.
- (B) Orders: second order in $`\delta F=F_1q+F_2q^2`$ at fixed $`F_0`$ for the mutual term (Step 2), and leading order in $`|\Delta E|/\bar M_i`$ for $`D`$ (Steps 7–8). The neglected fourth-order terms of the elimination vanish for held bodies with $`F_2=0`$ (a linear term on a quadratic contract is removed exactly by a shift of $`q`$), so they enter only through the motion of the bodies and through $`F_2`$; they are smaller by the factors $`r^2|U(0)|/\bar M_i`$ (recoil of the virtual quanta) and $`u=2\max_iM_{k_i}|F_2|G(0)`$, both assumed $`\ll1`$. The single-body self-energies at second order change $`\bar M_i`$ and $`I_i`$ at relative order $`\delta F^2`$; they cancel from $`\Delta E`$ and $`D`$ at the order used (Step 7).
- (C) Slow bodies (continuum regime): the bound level has size $`a_b`$ with $`a_b\gg1`$ and $`a_b\gg\lambda_{C,i}`$; corrections are of relative order $`a_b^{-2}`$ and $`(\lambda_{C,i}/a_b)^2`$.
- (D) No Cherenkov denominators: $`r\min(1,\lambda_{C,i}/2)<1`$ for $`i=1,2`$ (Step 2), so that the elimination holds on the whole band.

## Derivation

### Step 1. Bodies at first order

The first-order part of the grip is $`\langle0\vert\delta F(q_x)\vert0\rangle=F_2w_0`$ in the lowest eigenvector $`\vert0\rangle`$ of the field; it is put into $`H_0`$, together with the motion terms and $`H`$. The clock label is conserved by every term, so $`S_i\to M_{k_i}\sigma_3`$. In plane waves $`\vert p\rangle=L^{-1/2}\sum_xe^{ipx}\vert x\rangle`$ the body contract is $`h_i(p)=\bar M_i\sigma_3-\tau\sin p\,\sigma_1`$, with bands $`\varepsilon_i^{\sigma}(p)=\sigma E_i(p)`$, $`E_i=\sqrt{\bar M_i^2+\tau^2\sin^2p}`$, eigenvectors $`u_+=(\cos\frac\theta2,-\sin\frac\theta2)`$, $`u_-=(\sin\frac\theta2,\cos\frac\theta2)`$, $`\tan\theta_i(p)=\tau\sin p/\bar M_i`$. Hence

```math
\varepsilon_i(p)=\sigma_i\bar M_i+\frac{p^2}{2I_i}-\Bigl(\frac1{8I_i^3\tau^2}+\frac1{6I_i}\Bigr)p^4+O(p^6),\qquad I_i=\frac{\sigma_i\bar M_i}{\tau^2},\qquad \langle u_{\sigma}(p')\vert\sigma_3\vert u_\sigma(p)\rangle=\sigma\,c_i(p',p),\ \ c_i=\cos\tfrac{\theta_i(p)+\theta_i(p')}2 .
\qquad\text{(7.1)}
```

$`I_i`$ is the signed inertia; for $`\sigma_i=+`$ it is (6.7) with $`M_k\to\bar aM_k`$ at this order. The band has the same form near $`p=\pi`$ (the factor $`\sin p`$): every body has two minima of $`E_i`$, at $`p=0`$ and $`p=\pi`$. In (7.1) the $`p^4`$ term $`-1/(8I_i^3\tau^2)`$ is the relativistic part, $`-1/(6I_i)`$ the lattice part ($`\sin^2p=p^2-p^4/3`$). Near $`p=0`$ the velocity is $`v_i=\varepsilon_i'(p)=p/I_i`$ and $`c_i=1-\bar v_i^2/(2\tau^2)+O(v^4)`$, $`\bar v_i=(v_i+v_i')/2`$.

### Step 2. Elimination of the field: the mutual term

The modes $`q_x=\sum_q(2L\omega_q)^{-1/2}(b_qe^{iqx}+b_q^\dagger e^{-iqx})`$ diagonalize $`H`$ (standard). $`V=\sum_i\sum_x\lvert x\rangle\langle x\rvert\otimes M_{k_i}\sigma_3\otimes(\delta F(q_x)-F_2w_0)`$ has no component in the band space $`\mathcal P`$ (bodies in bands $`\sigma_1,\sigma_2`$, field in $`\vert0\rangle`$). The symmetric second-order effective contract on $`\mathcal P`$ (des Cloizeaux/Schrieffer–Wolff) is $`\langle f\vert H_{\rm eff}\vert i\rangle=\langle f\vert H_0\vert i\rangle+\frac12\sum_{n\notin\mathcal P}\langle f\vert V\vert n\rangle\langle n\vert V\vert i\rangle\bigl[(E_i-E_n)^{-1}+(E_f-E_n)^{-1}\bigr]`$. From $`\vert0\rangle`$, $`F_1q_x`$ creates one quantum and $`F_2(q_x^2-w_0)`$ two; the mixed products vanish (odd in $`q`$). Terms with both vertices on one body are the single-body self-energies; terms with one vertex on each body form the mutual term. For one vertex per body, body $`i`$ ends in its own band, so only same-band intermediate states enter. With the vertex amplitudes $`\mu_iF_1c_i/\sqrt{2L\omega_q}`$ (one quantum) and $`\mu_iF_2c_i/(L\sqrt{\omega_a\omega_b})`$ (two quanta, $`a\neq b`$; $`\sqrt2\mu_iF_2c_i/(2L\omega_a)`$ for $`a=b`$), and the two time orders, the mutual term is, for $`p_1'=p_1-q`$, $`p_2'=p_2+q`$, $`\Delta_1=\varepsilon_1(p_1)-\varepsilon_1(p_1')`$, $`\Delta_2=\varepsilon_2(p_2')-\varepsilon_2(p_2)`$:

```math
\langle p_1'p_2'\vert U\vert p_1p_2\rangle=-\frac{\mu_1\mu_2c_1c_2}{2L}\sum_{j=1,2}\Bigl[\frac{F_1^2}{\omega_q^2-\Delta_j^2}+\frac{F_2^2}{L}\sum_{a+b=q}\frac{\Omega_{ab}}{\omega_a\omega_b(\Omega_{ab}^2-\Delta_j^2)}\Bigr],\qquad \Omega_{ab}=\omega_a+\omega_b ,
\qquad\text{(7.2)}
```

with $`c_1=c_1(p_1',p_1)`$, $`c_2=c_2(p_2',p_2)`$. The effective joint contract in the sector $`P=p_1+p_2`$ is

```math
H_{\rm eff}(P)=\varepsilon_1(p_1)+\varepsilon_2(p_2)+U+O(\delta F^2\ \text{self-energies})+O(\delta F^4).
\qquad\text{(7.3)}
```

Code check (i) (`code/v1/check_mutual_term.py`, output `mutual_term_check.json`): on a ring of 16 cells, (7.2) agrees with second-order perturbation theory in the total contract restricted to at most two quanta, built in the position basis with numerically obtained spinors and both branches as intermediate states, to a relative deviation of at most $`3.9\times10^{-14}`$ over 32 matrix elements (four descriptions: a generic (G2) grip, the square grip and mixed branches at $`r=0.8`$, and the generic grip at $`r=1.3`$).

*No Cherenkov denominators.* $`\lvert E(p)-E(p')\rvert\le\tau\lvert\sin p-\sin p'\rvert\le2\tau\lvert\sin\frac q2\rvert`$ and $`\lvert E(p)-E(p')\rvert\le\frac{\tau^2}{2\bar M}\lvert\sin(p+p')\sin(p-p')\rvert\le\frac{\tau^2}{\bar M}\lvert\sin\frac q2\rvert`$, while $`\omega_q>2c_0\lvert\sin\frac q2\rvert`$ and $`\Omega_{ab}>2c_0\lvert\sin\frac{a+b}2\rvert`$. Hence $`\lvert\Delta_j\rvert<\omega_q,\Omega_{ab}`$ on the whole band under (D); the elimination is then valid for every label.

### Step 3. Held limit and time representation

With $`\frac1{\Omega-\Delta}+\frac1{\Omega+\Delta}=2\int_0^\infty e^{-\Omega t}\cosh(\Delta t)\,dt`$ and $`\frac1L\sum_qe^{iqr}e^{-\omega_qt}/(2\omega_q)=\Gamma_r(t)`$, (7.2) becomes, with $`r=x_1-x_2`$ and the transfer $`q`$ acting as $`-i\partial_r`$,

```math
U=-c_1c_2\int_0^\infty dt\ \tfrac12\textstyle\sum_j\cosh(\Delta_jt)\,W(r,t),\qquad W(r,t)=2\mu_1\mu_2\bigl[F_1^2\Gamma_r(t)+2F_2^2\Gamma_r(t)^2\bigr].
\qquad\text{(7.4)}
```

For held bodies ($`\tau=0`$: $`c_i=1`$, $`\Delta_j=0`$) it reduces to $`U(r)=-\int_0^\infty W\,dt=-\mu_1\mu_2[F_1^2G(r)+4F_2^2J_2(r)]`$, since $`\int_0^\infty\Gamma_r\,dt=G(r)/2`$: this is (2.11) in (G2), here without an $`O(\mu^3)`$ remainder at second order in $`\delta F`$. $`U(r)`$ below always denotes this static bond; it has the sign of $`-\mu_1\mu_2`$ at every $`r`$, as stated with (2.11) ($`\Gamma_r(t)>0`$).

### Step 4. The bond in motion (item 1)

In the sector $`P`$ write $`p_1=\frac{I_1}IP+k`$, $`p_2=\frac{I_2}IP-k`$, $`I=I_1+I_2`$, $`V=P/I`$, $`m_{\rm red}=I_1I_2/I`$; then $`\sum_ip_i^2/(2I_i)=P^2/(2I)+k^2/(2m_{\rm red})`$ exactly, and $`v_i=V+u_i`$ with $`u_1=k/I_1`$, $`u_2=-k/I_2`$. Near the band minimum (at $`0`$, and identically at $`\pi`$), Step 1 gives $`c_1c_2=1-(\bar v_1^2+\bar v_2^2)/(2\tau^2)`$, and $`\Delta_j=q\bar v_j`$ up to relative $`O(q^2,\lambda_C^2k^2)`$ (midpoint rule), so $`\cosh(\Delta_jt)=1+q^2\bar v_j^2t^2/2`$. Keeping in (7.4) the terms of second order in $`V`$, with $`q^2\to-\partial_r^2`$:
$`U_P=U(r)+V^2[-U(r)/\tau^2+R(r)]+(\text{odd in }k)+(\text{terms in }k\text{ only})`$, $`R(r)=\frac12\partial_r^2\int_0^\infty t^2W(r,t)\,dt`$.

*Identity for $`R`$.* For $`\ell\gg1`$ and $`L\to\infty`$ the relevant transfers are $`q\ll1`$, and $`\Gamma_r(t)=(2\pi)^{-2}\int dq\,d\nu\,e^{iqr+i\nu t}/(\nu^2+c_0^2q^2+m_h^2)`$ depends on $`(r,t)`$ only through $`t^2+r^2/c_0^2`$ (rotation of the integration variables $`(\nu,c_0q)`$; corrections $`O(q^2)`$ from $`\sin^2\frac q2=\frac{q^2}4-\frac{q^4}{48}`$). So $`W=w(t^2+\rho^2)`$, $`\rho=r/c_0`$. With $`\Psi(\rho)=\int_0^\infty t^2w\,dt`$: $`\Psi'(\rho)=\rho\int_0^\infty t\,\partial_tw\,dt=-\rho\int_0^\infty w\,dt=\rho U`$ (integration by parts; $`tw\to0`$ at both ends). Hence $`R=\Psi''/(2c_0^2)=(rU)'/(2c_0^2)`$, for both the one- and the two-quantum part, and

```math
U_P(r)=U(r)+\frac{P^2}{I^2}\Bigl[-\frac{U(r)}{\tau^2}+\frac{(rU(r))'}{2c_0^2}\Bigr]+O\bigl(V^4,\ V\cdot u,\ u^2\bigr),
\qquad\text{(7.5)}
```

with relative corrections $`O(\ell^{-2},a_b^{-2},\lambda_C^2/a_b^2)`$ to the $`V^2`$ term. The first bracket term is the reduction of the grip of a moving body (form factor), the second the motion of the field between the bodies (retardation). For the one-quantum part, dropping $`u`$, the kernel is $`1/(m_h^2+(c_0^2-V^2)q^2)`$, i.e. the static $`G`$ with $`c_0^2\to c_0^2-V^2`$. Below and above the pinning length, with $`U_G(r)=-\mu_1\mu_2F_1^2\ell e^{-|r|/\ell}/(2c_0^2)`$:

```math
U_{G,P}(r)\simeq\begin{cases}U_G(0)\Bigl[1-V^2\bigl(\tfrac1{\tau^2}-\tfrac1{2c_0^2}\bigr)\Bigr]+\dfrac{\mu_1\mu_2F_1^2}{2c_0^2}\,|r|\Bigl[1-V^2\bigl(\tfrac1{\tau^2}-\tfrac1{c_0^2}\bigr)\Bigr], & |r|\ll\ell,\\[2mm] U_G(r)\Bigl[1-\dfrac{V^2}{\tau^2}+\dfrac{V^2}{2c_0^2}\bigl(1-\tfrac{|r|}\ell\bigr)\Bigr], & |r|\gg\ell .\end{cases}
\qquad\text{(7.6)}
```

Below $`\ell`$ the constant and the slope of the bond change with $`P`$ by different factors; above $`\ell`$ the bond's range shrinks to $`\ell\sqrt{1-V^2/c_0^2}`$, so at fixed $`|r|\gg\ell`$ the moving bond is weaker by $`V^2|r|/(2c_0^2\ell)`$.

### Step 5. Branches with a bound level

Near the minimum of the bands, $`H_{\rm eff}(0)=\sigma_1\bar M_1+\sigma_2\bar M_2+k^2/(2m_{\rm red})+U(r)`$ with $`U`$ of the sign of $`-\sigma_1\sigma_2`$ at every $`r`$ (Step 3). In one dimension a level splits off from the edge of the relative band iff the potential pulls toward that edge (standard), i.e. iff $`\sigma_1\sigma_2\,m_{\rm red}>0`$:

```math
\text{bound level near labels }0\iff\begin{cases}\sigma_1=\sigma_2=+: & \text{always; lowest level of the sector}\\ \sigma_1=-\sigma_2: & \text{iff the member in the branch }+\text{ has the larger }\bar M\ (I>0,\ m_{\rm red}<0);\ \text{highest level}\\ \sigma_1=\sigma_2=-: & \text{never}\end{cases}
\qquad\text{(7.7)}
```

For $`(-,-)`$ bound levels exist only near the labels $`\pm\pi/2`$, where the bands of the branch $`-`$ have their minima; there the continuum regime (C) does not hold, and they are out of scope. The extreme level of (7.7) comes in two copies, the pair near labels $`(0,0)`$ and near $`(\pi,\pi)`$; the mutual term couples them only through transfers $`q\approx\pi`$, with $`t\simeq\tilde U(\pi)|\phi(0)|^2`$, $`\tilde U(\pi)\simeq-\mu_1\mu_2F_1^2/(m_h^2+4c_0^2)`$, $`\phi`$ the relative wave function. The extreme level is the even combination, unique for $`t\neq0`$; $`|t|/|\Delta E|=O(1/(a_b\ell))`$ in the deep and $`O(\ell^{-2})`$ in the shallow regime, so $`\Delta E`$ and $`D`$ below are those of one copy up to these orders.

### Step 6. Binding regime and isolation

With $`L\to\infty`$ the separated pair has $`\sigma_1\bar M_1+\sigma_2\bar M_2`$, so $`\Delta E`$ is the eigenvalue of the relative contract. Two regimes, for $`\sigma_1=\sigma_2=+`$ (for the mixed case replace $`m_{\rm red}\to-|m_{\rm red}|`$; $`\Delta E>0`$):

```math
\begin{aligned}
&\text{deep }(1,\lambda_C\ll a_b\ll\ell): &&U\simeq U(0)+\lambda|r|,\ \ \lambda=\frac{\mu_1\mu_2F_1^2}{2c_0^2},\ \ a_b=(2m_{\rm red}\lambda)^{-1/3},\\
& &&\Delta E=U(0)+\alpha\Bigl(\frac{\lambda^2}{2m_{\rm red}}\Bigr)^{1/3},\ \ \langle T\rangle=\frac\alpha3\Bigl(\frac{\lambda^2}{2m_{\rm red}}\Bigr)^{1/3},\ \ U(0)=-\mu_1\mu_2\bigl[F_1^2G(0)+4F_2^2J_2(0)\bigr],\ G(0)\simeq\frac{\ell}{2c_0^2};\\
&\text{shallow }(a_b\gg\ell\gg1): &&U\to-g\,\delta_{r0},\ \ g=\mu_1\mu_2\Bigl[\frac{F_1^2}{m_h^2}+\frac{F_2^2}L\sum_q\frac1{2\omega_q^3}\Bigr],\ \ a_b=\frac1{m_{\rm red}g},\ \ \Delta E=-\frac{m_{\rm red}g^2}2=-\langle T\rangle .
\end{aligned}
\qquad\text{(7.8)}
```

Here $`\alpha=1.0188`$ is the first zero of $`-{\rm Ai}'(-x)`$ (even ground state of $`k^2/(2m)+\lambda|r|`$), $`\langle T\rangle=\langle k^2/(2m_{\rm red})\rangle`$, and $`g=-\sum_rU(r)`$ is exact on the ring ($`\sum_rG=1/m_h^2`$, $`\sum_r4J_2=\frac1L\sum_q\frac1{2\omega_q^3}`$). Corrections: deep, relative $`O(a_b/\ell)`$ to the Airy part (the $`r^2/\ell`$ term of $`G`$), and the two-quantum slope ($`\propto|r|\ln(\ell/|r|)`$), smaller than $`\lambda`$ by $`2F_2^2\ln(\ell/a_b)/(\pi F_1^2c_0)`$, is dropped; shallow, relative $`O(\ell/a_b)`$. In the deep regime $`\langle T\rangle/|\Delta E|=O(a_b/\ell)`$, since $`|U(0)|\simeq\lambda\ell`$.

*Isolation.* (i) From the relative continuum: by $`|\Delta E|`$ (shallow) or by $`|U(0)|`$ (deep); from the next relative level by $`\sim(\lambda^2/2m_{\rm red})^{1/3}`$ (deep) and from the other valley copy by $`2|t|`$. (ii) From the states with field quanta: for $`(+,+)`$ they lie at least $`m_h`$ above the bound level; for mixed branches (body 2 in $`-`$) the states reached by one vertex lie above the level iff $`\Delta E<\gamma:=\min_q[\omega_q-(E_2(q)-\bar M_2)]`$, and $`\gamma>0`$ under (D) by the bounds of Step 2; states reached only through two vertices give a width of order $`\delta F^4`$, beyond the order used. (iii) The expansion of $`1/E_b''`$ below needs $`|\Delta E|\ll|\sigma_1\bar M_1+\sigma_2\bar M_2|`$: automatic for $`(+,+)`$ by (B); for mixed branches it excludes the levels with $`\bar M_1\approx\bar M_2`$ (small $`I`$, large $`|m_{\rm red}|`$).

### Step 7. The bound level near $`P=0`$

Take the expectation of the $`P^2`$ terms of $`H_{\rm eff}(P)`$ in the bound eigenvector $`\phi`$ of the relative contract $`k^2/(2m_{\rm red})+U`$ (first-order perturbation in $`P^2`$):
- *motion of the members:* the $`p^4`$ terms of (7.1) with $`p_i=I_iV+k_i`$ contain $`6I_i^2V^2k^2`$; with $`\langle k^2\rangle=2m_{\rm red}\langle T\rangle`$ they give $`-V^2[\frac3{2\tau^2}\langle T\rangle+2m_{\rm red}I\langle T\rangle]`$, the first from the relativistic, the second from the lattice part;
- *labels in the mutual term:* by (7.5), $`V^2\langle-U/\tau^2+(rU)'/(2c_0^2)\rangle`$;
- *terms odd in $`k`$* (from $`p_i^4`$, $`c_1c_2`$ and $`\Delta_j^2`$): zero at first order, since $`\phi`$ is real (the relative contract at $`V=0`$ is real in the position basis); at second order they are of relative order $`|\Delta E|/|\bar M_i|`$;
- *self-energies:* their $`p^2`$ parts renormalize $`I_i`$ in $`P^2/(2I)`$ exactly as for the bodies alone; their $`p^4`$ parts give $`O(\delta F^2\langle k^2\rangle)`$, of relative order $`\delta F^2`$.

With $`1/I_{\rm pair}=E_b''(0)=1/I+2I^{-2}[\dots]`$, at first order in $`|\Delta E|/\bar M`$:

```math
E_b(P)=E_b(0)+\frac{P^2}{2I_{\rm pair}}+O(P^4),\qquad I_{\rm pair}=I_1+I_2+D,\qquad D=\underbrace{\frac{3\langle T\rangle}{\tau^2}}_{\text{members}}+\underbrace{\frac{2\langle U\rangle}{\tau^2}-\frac{\langle(rU)'\rangle}{c_0^2}}_{\text{labels in }U}+\underbrace{4I_1I_2\langle T\rangle}_{\text{lattice}} .
\qquad\text{(7.9)}
```

The term $`2\langle U\rangle/\tau^2`$ is the form factor, $`-\langle(rU)'\rangle/c_0^2`$ the retardation. The first three parts are of order $`|\Delta E|/\tau^2`$ with relative corrections $`O(|\Delta E|/\bar M,(\lambda_C/a_b)^2,a_b^{-2},\ell^{-2},\delta F^2,u)`$; the lattice part is smaller than the members' part by $`4\bar M_1\bar M_2/(3\tau^2)=4/(3\lambda_{C,1}\lambda_{C,2})`$. Higher orders: $`I_{\rm pair}-I_1-I_2=D+D^2/I+\dots`$, the second term of relative order $`|\Delta E|/\bar M`$.

### Step 8. Virial form and the factor of $`\Delta E`$ (item 2)

For an eigenvector of $`k^2/(2m_{\rm red})+U(r)`$, $`2\langle T\rangle=\langle rU'\rangle`$ for either sign of $`m_{\rm red}`$ (virial theorem, from $`\langle[H,rk]\rangle=0`$), so $`\langle(rU)'\rangle=\langle U\rangle+2\langle T\rangle`$, and $`\Delta E=\langle T\rangle+\langle U\rangle`$ at leading order. Then (7.9) becomes

```math
D=\frac{(2-r^2)\,\Delta E+(1-r^2)\langle T\rangle}{\tau^2}+4I_1I_2\langle T\rangle .
\qquad\text{(7.10)}
```

In the two regimes of (7.8):

```math
\text{deep: }D=\frac{(2-r^2)\Delta E}{\tau^2}+O\Bigl(\bigl(1+\tfrac{1}{\lambda_{C,1}\lambda_{C,2}}\bigr)\tfrac{a_b}\ell\tfrac{|\Delta E|}{\tau^2}\Bigr);\qquad \text{shallow: }D=\Delta E\Bigl(\frac1{\tau^2}-4I_1I_2\Bigr)\Bigl[1+O\bigl(\tfrac\ell{a_b}\bigr)\Bigr]=\frac{\Delta E}{\tau^2}\Bigl(1-\frac{4\sigma_1\sigma_2}{\lambda_{C,1}\lambda_{C,2}}\Bigr)\Bigl[1+O\bigl(\tfrac\ell{a_b}\bigr)\Bigr].
\qquad\text{(7.11)}
```

In the shallow regime the retardation vanishes ($`rU`$ has zero derivative on average for a contact bond) and the form factor and the members' motion give $`(-3+4)\Delta E/\tau^2`$, for every $`r`$. In the deep regime $`\Delta E\simeq U(0)`$, the made field of each body at the other, and only the form factor ($`2U(0)/\tau^2`$) and the retardation ($`-U(0)/c_0^2`$) remain.

*One speed.* Write $`\rho:=\langle T\rangle/\Delta E`$; it runs from $`0^-`$ (deep) to $`-1`$ (shallow) and depends on $`F_1`$, $`\ell`$ and, through $`m_{\rm red}`$, on the levels. In the continuum part ($`\lambda_{C,i}\to\infty`$), (7.10) is $`D=\Delta E/v^2`$ with $`\tau^2/v^2=2-r^2+(1-r^2)\rho`$. Hence

```math
D=\frac{\Delta E}{v^2}\ \text{with one }v\text{ for every binding strength, level pair and grip}\iff r=1,\ \text{and then }v=\tau=c_0;\qquad \text{at }r=1:\ D=\frac{\Delta E}{\tau^2}+4I_1I_2\langle T\rangle .
\qquad\text{(7.12)}
```

For $`r\neq1`$ the speed depends on the binding: $`v=\tau/\sqrt{2-r^2}`$ in the deep regime ($`r<\sqrt2`$), $`v=\tau`$ in the shallow one; for $`r\ge\sqrt2`$ the deep leading term vanishes or changes sign and no real $`v`$ exists. At $`r=1`$ the lattice part breaks the equality by the relative amount $`4|\rho|/(\lambda_{C,1}\lambda_{C,2})`$, which is $`O(a_b/\ell)`$ small in the deep regime and $`O(\lambda_C^{-2})`$ in the shallow one. The grip enters (7.10) only through $`U`$, so the linear grip ($`F_2=0`$) obeys (7.10)–(7.12) unchanged; it is no control for item 2. Controls in the class: every $`r\neq1`$ (for example deep, $`r=\frac12`$: $`D=\frac74\Delta E/\tau^2`$), and $`\lambda_{C,i}=O(1)`$ at $`r=1`$ in the shallow regime (lattice part comparable to $`\Delta E/\tau^2`$). Cancellations, excluded: $`r=\sqrt2`$ in the deep regime (the leading term vanishes; $`D=[-\tau^{-2}+4I_1I_2]\langle T\rangle`$); $`\lambda_{C,1}\lambda_{C,2}=4`$ in the shallow regime (outside (C)); $`\bar M_1\approx\bar M_2`$ for mixed branches (Step 6 (iii)). For a common grip $`U`$ has no zero, so no separation is tuned away.

Code check (ii) (`code/v1/check_bound_pair.py`, output `bound_pair_check.json`): exact diagonalization of the effective contract (7.2)–(7.3) on a ring of 1024 cells ($`\tau=1`$, $`M_{k_1}=0.5`$, $`M_{k_2}=0.4`$, so $`\lambda_{C,1}\lambda_{C,2}\approx5`$; square and linear grip; $`r=0.5,1,1.4`$), for a deep ($`\ell=30`$, $`a_b\approx10`$, $`\rho\approx-0.12`$) and two shallower bound levels ($`\ell=30`$, $`a_b\approx93`$, $`\rho\approx-0.59`$; $`\ell=8`$, $`a_b\approx70`$, $`\rho\approx-0.81`$), branches $`(+,+)`$, and for $`(+,-)`$ with the linear grip. The curvature of the extreme level agrees with (7.10), with $`\Delta E`$ and $`\langle T\rangle`$ from the same eigenvector: $`|D_{\rm num}-D_{(7.10)}|\le0.18\,|\Delta E|/\tau^2`$ in the deep cases ($`\le0.072`$ for $`(+,+)`$ after removing the $`D^2/I`$ term of Step 7), where the expected corrections $`|\Delta E|/|\sigma_1\bar M_1+\sigma_2\bar M_2|+(\lambda_C/a_b)^2`$ are $`\approx0.11`$; $`\le0.014\,|\Delta E|/\tau^2`$ for $`\ell=30`$, $`a_b\approx93`$; $`\le0.021\,|\Delta E|/\tau^2`$ for $`\ell=8`$, where $`O(\ell^{-2})\approx0.016`$. $`E_b(P)-E_b(0)`$ agrees with $`P^2/(2I_{\rm pair})`$ to $`1\%`$ of the shift for $`(+,+)`$ and $`0.3\%`$ for $`(+,-)`$. For $`(+,+)`$ at $`r=1`$, $`D/(\Delta E/\tau^2)=0.88,\,0.53,\,0.34`$ in the three regimes ($`D`$ without the $`D^2/I`$ term) (formula $`0.90,\,0.53,\,0.35`$): the departure from $`1`$ is the lattice part of (7.12) at $`\lambda_C\approx2`$; at $`r=0.5`$ in the deep regime it is $`1.51`$ (formula $`1.57`$, $`2-r^2=1.75`$).

### Step 9. Fall of the pair (item 3)

A distant held source $`g_sq_{x_s}`$ translates the lowest eigenvector of the field by $`\langle q_x\rangle=\phi(x)=-g_sG(x-x_s)`$ (first order in $`g_s`$; quadratic contract), with unchanged fluctuations $`\tilde q`$. Over a pair of size $`a_b`$ much smaller than its distance to the source, $`\phi`$ is uniform up to its gradient (the midpoint factor $`m_{\mathbf r}\to1`$ of (2.18)), and the bodies hold $`F(\phi+\tilde q)`$: $`\bar a\to\bar a+F_1\phi`$, $`F_1\to F_1+2F_2\phi`$, $`F_2`$ unchanged. The weight of a cost $`E`$ is $`w=\partial E/\partial\phi`$ (the force is $`-w\nabla\phi`$). For a member, $`w_i=\mu_iF_1`$ and $`w_i/I_i=F_1\tau^2/\bar a`$ for every level and both branches. For the pair, $`w=w_1+w_2+\partial\Delta E/\partial\phi`$ and, by Hellmann–Feynman on $`k^2/(2m_{\rm red})+U`$ ($`m_{\rm red}\propto\bar a`$, $`U_G\propto F_1^2`$, $`U_J\propto F_2^2`$): $`\partial\Delta E/\partial\phi=\frac{F_1}{\bar a}(s\langle U\rangle-\langle T\rangle)`$, at leading order in the grip ($`U_J/U_G`$ and $`F_2w_0/F_0`$ dropped, the order of (2.18)). For $`s=1`$ the static part is (2.18): the held bond is weighed like the rest cost. With (7.10), at first order in $`\Delta E/\bar M`$:

```math
\frac{w_{\rm pair}/I_{\rm pair}}{w_i/I_i}-1=\frac{s\langle U\rangle-\langle T\rangle-\tau^2D}{\sigma_1\bar M_1+\sigma_2\bar M_2}=\frac{(s-2+r^2)\langle U\rangle-(4-2r^2+4\tau^2I_1I_2)\langle T\rangle}{\sigma_1\bar M_1+\sigma_2\bar M_2}.
\qquad\text{(7.13)}
```

Deep ($`\langle T\rangle/\langle U\rangle=O(a_b/\ell)`$) and shallow ($`\langle U\rangle=-2\langle T\rangle=2\Delta E`$):

```math
\text{deep: the pair falls like its members}\iff s=2-r^2\ \ (\text{square grip: }r=1;\ \text{linear grip: }r=\sqrt2);\qquad \text{shallow: }\iff s=-2\tau^2I_1I_2\ \ (\to0:\ \text{linear grip, every }r),
\qquad\text{(7.14)}
```

each at leading order in $`a_b/\ell`$ (deep) or $`\ell/a_b`$ (shallow).

For the square grip in the shallow regime the binding cost is weighed three times ($`\partial\Delta E/\partial\phi=3\frac{F_1}{\bar a}\Delta E`$) but enters the inertia once, so the ratio differs by $`(2+4\tau^2I_1I_2)\Delta E/(\bar M_1+\bar M_2)`$ at every $`r`$ ($`2\Delta E/(\bar M_1+\bar M_2)`$ in the continuum part). The answer to item 3 is therefore no in general: with the square grip, which weighs the held mark and bond (2.18), the pair falls like its members only at $`r=1`$ and in the deep regime; the remainder there is $`-(2+4\tau^2I_1I_2)\langle T\rangle/(\bar M_1+\bar M_2)=O\bigl(\frac{a_b}\ell\frac{|\Delta E|}{\bar M}\bigr)`$.

## Result

Class for all items: the description of "Setup" (common grip of (G2) with $`F_0>0`$, $`F_1\neq0`$, every pair of levels, ring with $`m_h>0`$, $`\ell\gg1`$, $`L\gg\ell,a_b`$), $`M\to\infty`$ first, then $`L\to\infty`$, then the regime limits; second order in $`\delta F`$ for the mutual term, with fourth-order terms and self-energies negligible as in (B); continuum regime (C) and no Cherenkov denominators (D).

- **(7.1)** (definition) Bands $`\varepsilon_i=\sigma_iE_i(p)`$ of the bodies at first order, signed inertias $`I_i=\sigma_i\bar aM_{k_i}/\tau^2`$, form factor $`\sigma_ic_i`$ of the grip between band states; minima of $`E_i`$ at $`p=0`$ and $`p=\pi`$.
- **(7.2)** (formula) The mutual term between two-body states of labels $`(p_1,p_2)\to(p_1-q,p_2+q)`$, one- and two-quantum exchange with the form factors $`c_1c_2`$ and the energy transfers $`\Delta_1,\Delta_2`$, for every label under (D).
- **(7.3)** (formula) The effective joint contract in the sector $`P`$: the bands of the two bodies plus the mutual term, up to the single-body self-energies and $`O(\delta F^4)`$.
- **(7.4)** (formula) Time representation of (7.2); for held bodies it is the static bond (2.11) in (G2), with the sign of $`-\mu_1\mu_2`$ at every separation.
- **(7.5)** (formula) The bond of a pair moving with $`V=P/I`$: $`U+V^2[-U/\tau^2+(rU)'/(2c_0^2)]`$, at second order in the velocities, for $`\ell\gg1`$, with relative corrections $`O(\ell^{-2},a_b^{-2},\lambda_C^2/a_b^2)`$.
- **(7.6)** (formula) The one-quantum part of the moving bond, at second order in $`V`$: below the pinning length its constant and its slope change with $`P`$ by the factors $`1-V^2(\tau^{-2}-\frac12c_0^{-2})`$ and $`1-V^2(\tau^{-2}-c_0^{-2})`$; above it the bond has the range $`\ell\sqrt{1-V^2/c_0^2}`$.
- **(7.7)** (criterion) A bound level near labels $`0`$ exists for $`(+,+)`$ (lowest level of the sector), for mixed branches iff the member in the branch $`+`$ has the larger $`\bar M`$ (highest level), never for $`(-,-)`$; it comes in two valley copies, and the extreme level is their even combination, unique for $`t\neq0`$.
- **(7.8)** (formula) $`\Delta E`$, $`\langle T\rangle`$, $`a_b`$ in the deep regime $`1,\lambda_C\ll a_b\ll\ell`$ (Airy, relative corrections $`O(a_b/\ell)`$) and the shallow regime $`a_b\gg\ell`$ (contact bond, $`O(\ell/a_b)`$), with the isolation conditions of Step 6.
- **(7.9)** (formula) $`E_b(P)=E_b(0)+P^2/(2I_{\rm pair})+O(P^4)`$, $`I_{\rm pair}=I_1+I_2+D`$, with $`D`$ the sum of the members' part $`3\langle T\rangle/\tau^2`$, the labels' part $`2\langle U\rangle/\tau^2-\langle(rU)'\rangle/c_0^2`$ and the lattice part $`4I_1I_2\langle T\rangle`$, at first order in $`|\Delta E|/\bar M`$, relative corrections $`O(|\Delta E|/\bar M,(\lambda_C/a_b)^2,a_b^{-2},\ell^{-2},\delta F^2,u)`$.
- **(7.10)** (formula) $`D=[(2-r^2)\Delta E+(1-r^2)\langle T\rangle]/\tau^2+4I_1I_2\langle T\rangle`$, same class and order.
- **(7.11)** (formula) Deep: $`D=(2-r^2)\Delta E/\tau^2+O((1+\lambda_{C,1}^{-1}\lambda_{C,2}^{-1})\frac{a_b}\ell\frac{|\Delta E|}{\tau^2})`$; shallow: $`D=\Delta E(\tau^{-2}-4I_1I_2)[1+O(\ell/a_b)]`$, for every $`r>0`$ allowed by (D).
- **(7.12)** (criterion) $`D=\Delta E/v^2`$ with one speed for every binding strength, pair of levels and grip of the class iff $`r=1`$, then $`v=\tau=c_0`$, up to the lattice part $`4I_1I_2\langle T\rangle`$ (relative $`4|\langle T\rangle/\Delta E|/(\lambda_{C,1}\lambda_{C,2})`$); for $`r\neq1`$ the speed depends on the binding, from $`\tau/\sqrt{2-r^2}`$ (deep, $`r<\sqrt2`$) to $`\tau`$ (shallow), and no real speed exists in the deep regime for $`r\ge\sqrt2`$. Excluded cancellations: $`r=\sqrt2`$ (deep), $`\lambda_{C,1}\lambda_{C,2}=4`$ (shallow), $`\bar M_1\approx\bar M_2`$ (mixed branches).
- **(7.13)** (formula) Relative difference of weight over inertia between the pair and its members, at leading order in the grip and first order in $`\Delta E/\bar M`$, for a pair small against its distance to a distant held source.
- **(7.14)** (criterion) The pair falls like its members iff $`s=4F_0F_2/F_1^2=2-r^2`$ in the deep regime, at leading order in $`a_b/\ell`$ (square grip: iff $`r=1`$), and iff $`s=-2\tau^2I_1I_2\to0`$ in the shallow regime, at leading order in $`\ell/a_b`$ (linear grip, every $`r`$); with the square grip the answer to item 3 is no except at $`r=1`$ in the deep regime, with remainder $`O(\frac{a_b}\ell\frac{|\Delta E|}{\bar M})`$.

## Consistency checks

1. **Held limit.** For $`\tau\to0`$, $`c_i\to1`$ and $`\Delta_j\to0`$, and (7.2)/(7.4) give $`-\mu_1\mu_2[F_1^2G+4F_2^2J_2]`$, which is (2.11) in (G2) (Step 3). Passed.
2. **Bare bodies.** At first order, (7.1) gives $`\varepsilon_i''(0)=\tau^2/(\bar aM_{k_i})`$ for $`\sigma_i=+`$, which is (6.7) with the rest cost $`M_k\to\bar aM_k`$ of the grip ($`\bar a=F_0`$ for $`\delta F=0`$). Passed.
3. **Dimensions.** With $`[\text{cost}]=\lambda^{-1}`$: $`[\mu_i]=[\bar M_i]=[\text{cost}]`$, $`F`$ dimensionless, $`[q]=[\text{cost}]^{-1/2}`$, $`[\kappa_h]=[\text{cost}]^2`$, $`[c_0]=[\tau]=[\text{cost}]`$ (cells per unit $`\lambda`$), $`[F_1^2]=[\text{cost}]`$, $`[F_2^2]=[\text{cost}]^2`$, $`[G]=[\text{cost}]^{-2}`$, $`[J_2]=[\text{cost}]^{-3}`$: $`[U]=[\text{cost}]`$; $`[I_i]=[D]=[\text{cost}]^{-1}`$, and each term of (7.9) and (7.10) is $`[\text{cost}]/[\text{cost}]^2`$ or $`[\text{cost}]^{-2}[\text{cost}]`$. Passed.

## Open issues

- The fourth-order terms of the elimination and the single-body self-energies are not computed; they are argued to be of relative order $`r^2|U(0)|/\bar M`$, $`u`$ and $`\delta F^2`$ (assumption (B)), and the code checks only the second-order effective contract.
- The mixed-branch bound level is treated by the same formulas, with the extra isolation condition $`\Delta E<\gamma`$ and the exclusion $`\bar M_1\approx\bar M_2`$; its width from two-vertex processes (order $`\delta F^4`$) is not computed.
- The $`(-,-)`$ bound levels near the labels $`\pm\pi/2`$ and every bound level outside the continuum regime (C) are not treated.
- Item 3 uses a locally uniform made field ($`m_{\mathbf r}\to1`$); the corrections of the gradient over the pair, of relative order $`(a_b/d)^2`$ for a source at distance $`d`$, are not computed.
- Only the ring; the cubic torus (where the static bond falls as $`1/|r|`$) is a later package.

## Code

- `code/v1/check_mutual_term.py` (role: check). Builds the total contract on a ring of 16 cells in the position basis of the two bodies and the occupation basis of the field modes with at most two quanta, computes the symmetric second-order effective contract by summing over all intermediate states (both branches), keeps the part with one vertex on each body, and compares it with (7.2) for 8 label triples in four descriptions. Output: `code/v1/output/mutual_term_check.json` (maximal relative deviation $`3.9\times10^{-14}`$).
- `code/v1/check_bound_pair.py` (role: check). Diagonalizes the effective joint contract (7.2)–(7.3) (without self-energies) on a ring of $`L=1024`$ cells in the sector $`P`$, for $`P=0,h,2h,3h`$ with $`h=0.015|I|\tau`$ (labels $`p_{1,2}=\frac{I_{1,2}}IP\pm k`$), takes the extreme level (lowest for $`(+,+)`$, highest for $`(+,-)`$), fits $`E_b(P)-E_b(0)=aP^2+bP^4+cP^6`$, and compares $`D=1/(2a)-I_1-I_2`$ and $`E_b(P)`$ with (7.9)–(7.10), using $`\Delta E`$ and $`\langle T\rangle`$ (relative label measured from the nearest valley) from the same eigenvector; it also records the regime estimates (7.8), (7.11), the valley splitting and the largest $`|\Delta_j|/\omega_q`$, $`|\Delta_j|/\Omega_{ab}`$ (at most $`0.93`$). Parameters and results are listed in Step 8. Output: `code/v1/output/bound_pair_check.json`.

## Methods used

- Plane-wave and normal-mode diagonalization of quadratic contracts
- Symmetric second-order effective contract (Schrieffer–Wolff/des Cloizeaux)
- Laplace (time) representation of energy denominators; Euclidean isotropy of the continuum propagator
- Expansion in the velocities of the bodies (form factors, retardation)
- Two-body bound levels on a chain: Airy (linear bond) and contact limits; virial theorem
- First-order perturbation theory in the joint label; Hellmann–Feynman theorem
- Exact diagonalization and polynomial fit (code checks)

