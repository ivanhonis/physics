# Limits of the level-independent fall: level superpositions, records, the operator under the factor

- **Subproject:** 05-ilang-free-fall
- **Package:** 07-limits
- **Version:** v2
- **Mode:** internal regeneration
- **Date:** 2026-10-11

## Changes from previous version

Internal regeneration after `review.v1.md` (I1 major, I2 minor). The equations (7.1)–(7.21) are unchanged and keep their tags; new results carry (7.23)–(7.26). Changed passages, in the order of the file:

1. **Header.** Version and mode.
2. **Step 3, last sentence (I2).** v1: "In $`\mathcal C_{\rm lev}`$ equality at one $`p_0`$ is one condition on $`(\tau_k,M_k,\tau_{k'},M_{k'})`$ and needs $`\tau_k\neq\tau_{k'}`$; equality at all $`p_0`$ holds iff ...". The first half fails for two levels with equal data. v2 states it for two levels with different data and treats equal data separately. Eq. (7.5) is unchanged.
3. **Step 5, part 2, last sentence (I1).** v1: "For a start that is not even a first-order term is not excluded." It is replaced by a pointer to the new parts 5–7. Eq. (7.9) and its proof, and parts 1, 3, 4 with (7.8), (7.10) and (E1)–(E3), are unchanged.
4. **Step 5, parts 5–7, new (I1).** The first order in the gradients of $`\lvert\Gamma_{kk'}\rvert`$ for a general start at rest (complex $`g`$, a label weight that is not even): the reflection relation (7.23), the first-order term (7.24), its leading part (7.25) as an order estimate with the conditions (F1)–(F3), the two classes of starts, and the case of a level-independent fall (7.26).
5. **Step 9, part 1, the sentence after (7.20) (I2).** v1 wrote the common value as $`-g\,w`$ and solved for $`u_k`$, which presumes $`g\neq0`$. v2 states the condition for every $`g`$, then the form for $`g\neq0`$, then the case $`g=0`$. Eq. (7.19), (7.20) are unchanged.
6. **Step 10, row "Superposition of levels" (I1).** The cell (ii) and the tag cell now state the class of starts for each order. This is the only tagged statement whose content changed: the table keeps its tag (7.22).
7. **Result.** Rewritten: every item states its class of starts, its range and the order of the limits, and says where it is an order estimate; the items (7.23)–(7.26) are added. Apart from the points 2–6 no statement is changed in content.
8. **Open issues.** The first item is replaced by two items (what remains open for (7.10) and for (7.24)–(7.26)).
9. **Methods used.** One keyword added.

Unchanged, word for word: "Setup and assumptions"; Steps 1, 2, 4, 6, 7, 8; Step 3 up to its last sentence; Step 5, parts 1, 3, 4 and part 2 up to its last sentence; Step 9, parts 2, 3 and part 1 up to (7.20); the other rows of the table; "Consistency checks"; the other open issues.

## Setup and assumptions

- **Setting (question.md, assumptions of this package, M8, M9).** One body $`b`$ of the class $`\mathcal C_{\rm lev}`$ with linear level profiles ($`M_k,G_k,\mathcal F_k,g_{\zeta,k},V_k,\tau_k`$), a medium $`c`$ with $`K_x=\kappa xX`$, no field object; $`\lambda\ge0`$; infinite chain as the limit of long chains. Starts: branch starts $`B_{k,\sigma}[g]`$ and level-superposed starts $`\Phi_\sigma[\alpha,g]`$, times $`\chi`$.
- **Inputs, as quoted.** (5.5), (5.6), (5.11) of 04-ilang-time/05-moving-clock; (8.1), (8.19), (8.20) of 04-ilang-time/08-maximal-speed; (17.15) of 03-ilang-space/17-motion; (3.2), (3.23), (3.36) of 03-clock-and-fall; (4.1), (4.2), (4.5), (4.7), (4.10), (4.11), (4.16), (4.17), (4.19)–(4.25) of 04-branch-fall.
- **Notation.** $`\sigma=\pm1`$; $`w_\xi:=\lVert Q_\xi\chi\rVert^2`$, $`\varepsilon_\xi:=\kappa(\xi-\langle X\rangle)`$, so $`\sum_\xi w_\xi\varepsilon_\xi=0`$, $`\sum_\xi w_\xi\varepsilon_\xi^2=\kappa^2\sigma_X^2`$, $`\sum_\xi w_\xi\varepsilon_\xi^3=\kappa^3\mu_3`$ with $`\mu_3:=\langle(X-\langle X\rangle)^3\rangle`$. Inside one level: $`\omega,\theta`$ of (5.6) of 04-ilang-time/05-moving-clock with $`\tau\to\tau_k`$, $`\mu_k\to M_k`$; a prime is $`\partial_p`$; $`\hat x=i\partial_p`$ on plane-wave amplitudes. $`\mathrm{Var}_\alpha(y):=\sum_k\lvert\alpha_k\rvert^2\bigl(y_k-\sum_j\lvert\alpha_j\rvert^2y_j\bigr)^2`$.
- **Facts used.** $`\langle\beta_{k,\sigma}\vert\sigma_3\vert\beta_{k,\sigma}\rangle=\sigma M_k/\omega_k`$, $`\langle\beta_{k,\sigma}\vert\sigma_1\vert\beta_{k,\sigma}\rangle=-\sigma\tau_k\sin p/\omega_k`$; $`\omega\omega'=\tfrac12\tau^2\sin2p`$, hence $`\omega''(0)=\tau^2/M`$ and, by two more derivatives, $`\omega'''=-\omega'(4+3\omega''/\omega)`$, $`\omega''''(0)=-\tfrac{\tau^2}{M}\bigl(4+\tfrac{3\tau^2}{M^2}\bigr)`$; $`\theta'=-\tau M\cos p/\omega^2`$, $`\lvert\theta'\rvert\le\tau/M`$.
- **Level offsets.** $`V_k\mathbb 1`$ commutes with $`C^{(k)}`$ and multiplies the level component $`k`$ by $`e^{-iV_k\lambda}`$. For a start in one level this is a common phase (1.2), so every result quoted from 04-branch-fall holds for any $`V_k`$. In a level-superposed start the offsets enter only the phases of the coherences (Step 5), never $`p_x`$ or $`\lvert\Gamma_{kk'}\rvert`$.
- **Regimes (A13).** "First order in the gradients" as in question.md. Record results: Taylor order in $`\kappa`$ at fixed $`\lambda`$, start and chain; the range on which a leading term dominates is stated with it. Statements marked *order estimate* are not bounds.

## Derivation

### Step 1. Item 1(a),(b): position statistics of a level-superposed start

1. *Exact mixture.* $`C=\sum_k\bigl(C^{(k)}\otimes\mathbb 1_c+\kappa\hat x\otimes X\bigr)\otimes\lvert f_k\rangle\langle f_k\rvert`$ is block-diagonal in the level, so $`\Psi(\lambda)=\sum_k\alpha_k\,\Psi^{(k)}(\lambda)\otimes\lvert f_k\rangle`$ with $`\Psi^{(k)}(\lambda)`$ the evolved position–branch–medium vector of $`B_{k,\sigma}[g]\otimes\chi`$. A reading of the position is a partition by $`x`$ (A4); it sums over the clock label, and $`\langle f_{k'}\vert f_k\rangle=\delta_{kk'}`$ removes all cross terms (witness rule (1.7) with the clock label as companion). Hence
```math
p_x(\lambda)=\sum_k\lvert\alpha_k\rvert^2\,p^{(k)}_x(\lambda),\qquad\bar x_{\rm lab}(\lambda)=\sum_k\lvert\alpha_k\rvert^2\,\bar x_k(\lambda),
\qquad\text{(7.1)}
```
with $`p^{(k)}_x`$, $`\bar x_k`$ those of $`B_{k,\sigma}[g]`$. **Exact** in the gradients and in $`\kappa`$, for every $`\lambda`$, chain, $`g`$, $`\alpha`$, $`\chi`$. It rests only on the conservation of the level and on the orthonormality of the $`\lvert f_k\rangle`$. Every reading of the position alone is that of the mixture of single-level starts with weights $`\lvert\alpha_k\rvert^2`$; the phases of $`\alpha`$ and the $`V_k`$ do not enter.
2. *Drift acceleration.* (7.1) is linear in the single-level quantities, so (4.10) and (4.11) apply term by term, in the same order of limits (first order in the gradients of all levels with $`\alpha_k\neq0`$ at fixed $`\lambda`$, start, chain; long chain; $`\Lambda\to\infty`$; $`\delta p\to0`$):
```math
\Bigl\lvert\overline{a^{(1)}}-\sum_k\lvert\alpha_k\rvert^2\langle a_{k,\sigma}\rangle_g\Bigr\rvert\le\sum_k\lvert\alpha_k\rvert^2\frac{2\tau_k}{M_k\Lambda}\mathsf b_k\Bigl(X_g+\frac{\tau_k}{2M_k}\Bigr),\qquad a_{\rm drift}[\alpha]=\sum_k\lvert\alpha_k\rvert^2\,a_{k,\sigma}(p_0).
\qquad\text{(7.2)}
```
Taking $`\alpha_k=\delta_{kk_0}`$ for each $`k_0`$: $`a_{\rm drift}[\alpha]`$ is the same for all $`\alpha`$ **iff** $`a_{k,\sigma}(p_0)`$ does not depend on $`k`$. At rest this is line 1 ($`\sigma=+`$) or line 2 ($`\sigma=-`$) of (4.19), unchanged: a superposition of levels adds and removes no condition.
3. *What position readings distinguish.* If $`a_{k,\sigma}(p_0)`$ is level-independent, position readings of $`\Phi_\sigma[\alpha,g]`$ show the drift of one level. If not, (i) the mean acceleration (7.2) depends on $`\lvert\alpha_k\rvert^2`$, and (ii) $`p_x`$ is a mixture of components that separate, so the variance of the position exceeds the weighted mean of the single-level variances by the between-level variance (7.3). A body in one level has neither.

### Step 2. Item 1(c): variance of the first-order displacements, start at rest

By (4.7) the first-order velocity of level $`k`$ is $`\lambda\langle a_{k,\sigma}\rangle_g+\rho_k(\lambda)`$ with $`\sup_{\lambda\ge0}\lvert\rho_k\rvert=:r_k<\infty`$; integrating, $`\bar x^{(1)}_k=\tfrac12\lambda^2\langle a_{k,\sigma}\rangle_g+O(\lambda)`$, the rest bounded by $`r_k\lambda`$. With $`r:=\max_kr_k`$ and $`\mathrm{Var}(A+B)-\mathrm{Var}(A)=2\mathrm{Cov}(A,B)+\mathrm{Var}(B)`$:
```math
D(\lambda):=\mathrm{Var}_\alpha\bigl(\bar x^{(1)}\bigr)=\frac{\lambda^4}{4}\mathrm{Var}_\alpha\bigl(\langle a_{\cdot,\sigma}\rangle_g\bigr)+E(\lambda),\quad\lvert E\rvert\le r\lambda^3\sqrt{\mathrm{Var}_\alpha(\langle a_{\cdot,\sigma}\rangle_g)}+r^2\lambda^2;\qquad\lim_{\delta p\to0}\mathrm{Var}_\alpha\bigl(\langle a_{\cdot,\sigma}\rangle_g\bigr)=\mathrm{Var}_\alpha\bigl(a_{\cdot,\sigma}(0)\bigr).
\qquad\text{(7.3)}
```
Order of limits: first order in the gradients at fixed $`\lambda`$, start, chain; long chain; the $`\lambda^4`$ part dominates for $`\lambda\gg r/\sqrt{\mathrm{Var}_\alpha}`$ at fixed $`g`$; then $`\delta p\to0`$, error $`\le\tfrac12\sup\lvert a''_{k,\sigma}\rvert\delta p^2`$ per level (4.11). $`D`$ is of second order in the gradients (a square of first-order displacements). For $`\lvert\alpha_k\rvert^2=1/N`$, with (4.25), $`M_k=m+d_k`$ and $`\mathcal V_N:=\frac1N\sum_kM_k^{-2}-\bigl(\frac1N\sum_kM_k^{-1}\bigr)^2>0`$ (for $`N=2`$: $`\mathcal V_2=\tfrac14\bigl(\tfrac1{M_0}-\tfrac1{M_1}\bigr)^2`$):
```math
\begin{array}{l|c|c|c|c|c}
\text{variant}&\text{(a)}&\text{(b1)}&\text{(b2)}&\text{(c)}&\text{(f)}\\\hline
\lim_{\delta p\to0}\ \lambda^4\text{-part of }D&0&\tfrac14\lambda^4\tau^4g^2m^2\,\mathcal V_N&\tfrac14\lambda^4\tau^4g^2m^2\,\mathcal V_N&0&\tfrac14\lambda^4\tau^4g^2c_{\rm f}^2\,\mathcal V_N
\end{array}
\qquad\text{(7.4)}
```
((b2): $`d_k/M_k=1-m/M_k`$; (f): both branches.) In (a), (c) the coefficient of $`\lambda^4`$ is $`O(\delta p^4)`$ at fixed $`g`$, by (4.11), and vanishes in the sharp-label limit; what remains is $`E`$. Control: (a) against (b1).

### Step 3. Item 1(d): velocities at $`p_0\neq0`$

By (4.5), exactly at zero gradients, the level component $`k`$ has the constant velocity
```math
v_k=\sigma\langle\omega_k'\rangle_g\ \xrightarrow{\ \delta p\to0\ }\ \sigma\,\omega_k'(p_0)=\sigma\,\frac{\tau_k^2\sin p_0\cos p_0}{\sqrt{M_k^2+\tau_k^2\sin^2p_0}};\qquad v_k=v_{k'}\ (\sin2p_0\neq0)\iff\frac{\tau_k^4}{M_k^2+\tau_k^2\sin^2p_0}=\frac{\tau_{k'}^4}{M_{k'}^2+\tau_{k'}^2\sin^2p_0}.
\qquad\text{(7.5)}
```
In the class $`\mathcal C`$ ($`\tau_k=\tau`$, $`M_k`$ strictly increasing) the velocities are strictly ordered for $`\sin2p_0\neq0`$: **no** start of this class with $`p_0\notin\{0,\pm\tfrac\pi2,\pi\}`$ has two level components with equal velocities; the components separate as $`\lvert v_k-v_{k'}\rvert\lambda`$ already at zeroth order in the gradients. In $`\mathcal C_{\rm lev}`$, for two levels with different data, $`(\tau_k,M_k)\neq(\tau_{k'},M_{k'})`$, equality at one $`p_0`$ with $`\sin2p_0\neq0`$ is one condition on $`(\tau_k,M_k,\tau_{k'},M_{k'})`$ and needs $`\tau_k\neq\tau_{k'}`$ (for $`\tau_k=\tau_{k'}`$ the condition of (7.5) reduces to $`M_k=M_{k'}`$). For two levels with equal data, $`\tau_k=\tau_{k'}`$ and $`M_k=M_{k'}`$, the velocities are equal at every $`p_0`$, and this is the only such case: equality at all $`p_0`$ holds iff $`\tau_k=\tau_{k'}`$ and $`M_k=M_{k'}`$ (compare the coefficients of $`\sin^2p_0`$).

### Step 4. Item 1(e): rate of the mean label

1. *Exact transport of the label weight.* On the infinite chain, (4.2) gives for the amplitudes $`c(p,\lambda)\in\mathbb C^2`$ of a level component $`i\partial_\lambda c=C_0(p)c+\tfrac i2\bigl(\partial_p(Bc)+B\partial_pc\bigr)`$. $`C_0`$ and $`B`$ are Hermitian, so $`\partial_\lambda(c^\dagger c)=\partial_p(c^\dagger Bc)`$. Multiplying by $`p`$ and integrating over the arc $`(p_0-\pi,p_0+\pi]`$ by parts, for a normalized component:
```math
\frac{\mathrm d\bar p_k}{\mathrm d\lambda}=-\int\frac{\mathrm dp}{2\pi}\,c^\dagger B_k\,c+\bigl(c^\dagger B_kc\bigr)(p_0+\pi)\qquad(\text{exact in the gradients}).
\qquad\text{(7.6)}
```
The last term is the weight crossing the cut, bounded by $`\lVert B_k\rVert\,\lVert c(p_0+\pi)\rVert^2`$.
2. *First order.* Insert the zeroth-order amplitudes $`c=g\,e^{-i(V_k+\sigma\omega_k)\lambda}\beta_{k,\sigma}`$ (the correction to $`c`$ contributes at second order). The integrand is $`\lambda`$-independent, so no window is needed. With the facts above and $`B_k=-g_{\zeta,k}\tau_k\sin p\,\sigma_1+G_k\sigma_3-\mathcal F_k`$:
```math
\frac{\mathrm d\bar p_k}{\mathrm d\lambda}\Big\vert_{1}=\langle\pi_{k,\sigma}\rangle_g-\lvert g(p_0+\pi)\rvert^2\pi_{k,\sigma}(p_0+\pi),\quad\pi_{k,\sigma}(p):=\mathcal F_k-\sigma\frac{G_kM_k+g_{\zeta,k}\tau_k^2\sin^2p}{\omega_k(p)};\qquad\lim_{\delta p\to0}=\pi_{k,\sigma}(0)=\mathcal F_k-\sigma G_k.
\qquad\text{(7.7)}
```
Order of limits: first order in the gradients at fixed $`\lambda`$, start; long chain; $`\delta p\to0`$ (which also removes the cut term). With (4.16), $`a_{k,\sigma}(0)=\sigma\,\omega_k''(0)\,\pi_{k,\sigma}(0)`$.
3. *Equivalences.* At rest the rate is the same for all levels **iff** $`\mathcal F_k-\sigma G_k`$ does not depend on $`k`$. Together with $`a_{k,\sigma}(0)=a\neq0`$ for all $`k`$ this holds **iff** in addition $`\tau_k^2/M_k`$ does not depend on $`k`$. In the class $`\mathcal C`$ the rate is level-independent iff $`g_\eta=0`$, and then $`a_{k,\sigma}(0)=\tau^2(\sigma\mathcal F-mg_m)/M_k`$ is level-independent only if it is zero: **no**, in $`\mathcal C`$ the two cannot hold together with $`a\neq0`$ (variant (a): $`\pi_{k,\sigma}(0)=-\sigma gM_k`$). In $`\mathcal C_{\rm lev}`$ they can, at the price $`\tau_k^2\propto M_k`$.

### Step 5. Item 1(f): clock readings and coherences

1. *Formula.* The reading of the clock label is the partition by $`a`$; with $`\langle a\vert f_k\rangle=N^{-1/2}e^{2\pi ika/N}`$ and $`\Psi=\sum_k\psi_k\otimes\lvert f_k\rangle`$:
```math
P(a;\lambda)=\frac1N\sum_{k,k'}\alpha_{k'}^{*}\alpha_k\,\Gamma_{kk'}(\lambda)\,e^{2\pi i(k-k')a/N},\qquad\Gamma_{kk}=1,\quad\Gamma_{k'k}=\Gamma_{kk'}^{*},\quad\lvert\Gamma_{kk'}\rvert\le1.
\qquad\text{(7.8)}
```
This is exact if $`\psi_k`$ includes the medium, and then $`\Gamma_{kk'}=\sum_\xi w_\xi\Gamma^{[\xi]}_{kk'}`$ as in (4.1). At leading order in $`\kappa`$ ($`\kappa\to0`$ at fixed $`\lambda`$, chain, start) $`\Gamma_{kk'}`$ is that of the effective body contract, used below.
2. *Zero gradients, and the order of the first deviation.* From (5.6) of 04-ilang-time/05-moving-clock, $`\langle\beta_{k',\sigma}\vert\beta_{k,\sigma}\rangle=\cos\tfrac{\theta_k-\theta_{k'}}2`$, so
```math
\Gamma^{(0)}_{kk'}(\lambda)=e^{-i(V_k-V_{k'})\lambda}\Bigl\langle\cos\tfrac{\theta_k-\theta_{k'}}2\,e^{-i\sigma(\omega_k-\omega_{k'})\lambda}\Bigr\rangle_g;\qquad g(-p)=g(p)\ \Longrightarrow\ \Gamma_{kk'}[\text{gradients}]=\Gamma_{kk'}[-\text{gradients}]\ \ \text{exactly}.
\qquad\text{(7.9)}
```
Proof of the second statement: let $`\mathsf P`$ be the reflection $`x\to-x`$ times $`\sigma_3`$. By (4.2), $`\mathsf PC_0\mathsf P^{-1}=C_0`$ and $`\mathsf PC_1\mathsf P^{-1}=-C_1`$ in every level; $`\sigma_3\beta_{k,\sigma}(-p)=\sigma\beta_{k,\sigma}(p)`$ gives $`\mathsf PB_{k,\sigma}[g]=\sigma B_{k,\sigma}[g]`$ for even $`g`$, with the same sign in both levels; $`\mathsf P`$ is unitary. Hence for a start at rest with even $`g`$ the deviation of $`\Gamma_{kk'}`$, and of $`\lvert\Gamma_{kk'}\rvert`$, starts at **second order** in the gradients. For a start at rest that is not even, the first order is determined in parts 5–7.
3. *Leading term (order estimate).* Conditions: (E1) $`\lvert g\rvert^2\propto e^{-p^2/2\delta p^2}`$, $`g`$ real, $`\delta p\ll\min(1,M_k/\tau_k)`$, so the spread of the start in the position label is $`\delta x=1/(2\delta p)`$; (E2) inside the branch $`\sigma`$, at first order, the level component is transported by (7.7): $`c_k(p,\lambda)\simeq g(p-\pi_k\lambda)\,e^{-i\int_0^\lambda E_k(p-\pi_ks)\mathrm ds}\beta_{k,\sigma}`$, $`E_k=V_k+\sigma\omega_k`$, $`\pi_k:=\pi_{k,\sigma}(0)`$; the neglected inter-branch part gives a second-order term bounded in $`\lambda`$, negligible for $`\lambda\gg\tau_k/M_k^2`$; (E3) $`\lvert\pi_k\rvert\lambda\ll M_k/\tau_k`$ and $`\lvert\omega_k''-\omega_{k'}''\rvert\lambda\,\delta p^2\ll1`$, with $`\omega_k'':=\omega_k''(0)=\tau_k^2/M_k`$. Then the overlap is a Gaussian integral: the product $`g(p-\pi_{k'}\lambda)g(p-\pi_k\lambda)`$ gives $`e^{-(\pi_k-\pi_{k'})^2\lambda^2/8\delta p^2}`$, and the phase linear in $`p`$ about the common centre gives a relative position shift $`\Delta X=\tfrac12\lambda^2\sigma(\omega_{k'}''\pi_k-\omega_k''\pi_{k'})`$ and the factor $`e^{-\delta p^2\Delta X^2/2}`$:
```math
1-\frac{\lvert\Gamma_{kk'}\rvert}{\lvert\Gamma^{(0)}_{kk'}\rvert}\simeq\frac{\delta x^2}2\,(\pi_k-\pi_{k'})^2\lambda^2+\frac{\lambda^4}{32\,\delta x^2}\Bigl(\frac{\tau_{k'}^2}{M_{k'}}\pi_k-\frac{\tau_k^2}{M_k}\pi_{k'}\Bigr)^2,\qquad\pi_k=\mathcal F_k-\sigma G_k.
\qquad\text{(7.10)}
```
4. *Level-independent fall.* With $`a_{k,\sigma}(0)=\sigma\omega_k''\pi_k=a`$ for all $`k`$: $`\pi_k-\pi_{k'}=\sigma a\bigl(\tfrac{M_k}{\tau_k^2}-\tfrac{M_{k'}}{\tau_{k'}^2}\bigr)`$. The deviation (7.10) vanishes iff $`a=0`$ or $`\tau_k^2/M_k=\tau_{k'}^2/M_{k'}`$. So **no**: in the class $`\mathcal C`$ with $`a\neq0`$ it does not vanish. Variants (a), (c): $`1-\lvert\Gamma\rvert/\lvert\Gamma^{(0)}\rvert\simeq\tfrac12\delta x^2g^2(d_k-d_{k'})^2\lambda^2+\tfrac{\lambda^4\tau^4g^2}{32\delta x^2}\bigl(\tfrac{M_k}{M_{k'}}-\tfrac{M_{k'}}{M_k}\bigr)^2`$. In $`\mathcal C`$, $`\pi_k-\pi_{k'}=-\sigma g_\eta(d_k-d_{k'})`$ is, by (3.23), $`-\sigma\tfrac{2\pi(k-k')}{N}\bigl(r(x+1)-r(x)\bigr)`$: the $`\lambda^2`$ term is the difference of the clock rates across the spread $`\delta x`$.
5. *Reflection relation for every start.* Let $`g^-(p):=g(-p)`$. The proof of (7.9) uses that $`g`$ is even only in its last step; for every smooth $`g`$ it gives $`\mathsf PB_{k,\sigma}[g]=\sigma B_{k,\sigma}[g^-]`$, with the same sign in both levels. Hence, exactly, for the coherence of the effective body contract, every member of $`\mathcal C_{\rm lev}`$ with linear level profiles, both branches, every $`p_0`$ and every $`\lambda`$:
```math
\Gamma_{kk'}\bigl[g;\,\text{gradients}\bigr]=\Gamma_{kk'}\bigl[g^-;\,-\text{gradients}\bigr].
\qquad\text{(7.23)}
```
The first-order term of $`\Gamma_{kk'}`$, and of $`\lvert\Gamma_{kk'}\rvert`$, is therefore odd under $`g\to g^-`$. It vanishes for every start of **definite parity**, $`g^-=\pm g`$ (an odd $`g`$ is a start at rest as well); for other starts (7.23) does not exclude it. Independently of the start: if $`(\tau_k,M_k)=(\tau_{k'},M_{k'})`$, then $`\lvert\Gamma^{(0)}_{kk'}\rvert=1`$ by (7.9), the largest value that (7.8) allows for any gradients, so $`\lvert\Gamma_{kk'}\rvert`$ has no first-order term for any $`g`$.
6. *First-order term for a general $`g`$.* Class: every smooth complex $`g`$. Limits: first order in the gradients of the levels $`k`$, $`k'`$ at fixed $`\lambda`$ and start, infinite chain, leading order in $`\kappa`$. Notation: $`(\cdot)_1`$ is the first-order term in the gradients; $`\rho:=\lvert g\rvert^2`$; $`j:=\mathrm{Im}(g^{*}g')`$, so that $`-j/\rho`$ is the position label carried by the label component $`p`$ of the start ($`\langle\hat x\rangle=-\int\frac{\mathrm dp}{2\pi}j`$); $`F:=\cos\tfrac{\theta_k-\theta_{k'}}2`$; $`\Delta\omega:=\omega_k-\omega_{k'}`$; $`\pi_k:=\pi_{k,\sigma}(p)`$ of (7.7). In the interaction picture, $`c_k=e^{-i(V_k+C^{(k)}_0)\lambda}\tilde c_k`$, first-order perturbation theory in $`C_1`$ of (4.2), with $`\langle\beta_{k,\sigma}\vert B_k\vert\beta_{k,\sigma}\rangle=-\pi_k`$ and real $`\beta_{k,\sigma}`$, gives $`\tilde c_k=(g+a_k)\beta_{k,\sigma}+a_{k,\perp}\beta_{k,-\sigma}`$ with, exactly, $`a_k=-\lambda\bigl(\pi_kg'+\tfrac12\pi_k'g\bigr)+\tfrac{i\sigma}2\lambda^2\omega_k'\pi_k\,g`$ (the first order of the transport (E2); it conserves the norm and reproduces (7.7)). $`a_{k,\perp}`$ contains $`\int_0^\lambda e^{-2i\sigma\omega_ks}\mathrm ds`$ and $`\omega_k'\int_0^\lambda s\,e^{-2i\sigma\omega_ks}\mathrm ds`$, so it is bounded in $`\lambda`$ up to a part $`\propto\lambda\,\omega_k'/\omega_k`$. Inserting in $`\Gamma_{kk'}=\int\frac{\mathrm dp}{2\pi}c_{k'}^\dagger c_k`$ and integrating the term with $`\rho'`$ by parts on the circle:
```math
\Gamma^{(1)}_{kk'}=e^{-i(V_k-V_{k'})\lambda}\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\,e^{-i\sigma\Delta\omega\lambda}\Bigl\{\rho\Bigl[\tfrac\lambda2(\pi_k+\pi_{k'})F'+\tfrac{i\sigma}2\lambda^2\bigl(\omega_{k'}'\pi_k-\omega_k'\pi_{k'}\bigr)F\Bigr]-i\lambda(\pi_k-\pi_{k'})F\,j\Bigr\}+\Gamma^{(1),\perp}_{kk'},\qquad\Bigl(\frac{\lvert\Gamma_{kk'}\rvert}{\lvert\Gamma^{(0)}_{kk'}\rvert}\Bigr)_{1}=\mathrm{Re}\frac{\Gamma^{(1)}_{kk'}}{\Gamma^{(0)}_{kk'}}.
\qquad\text{(7.24)}
```
The displayed integral is the part inside the branch $`\sigma`$; it is exact, for every smooth $`g`$, every $`p_0`$ and every $`\lambda\ge0`$. It vanishes for $`k=k'`$, and for $`g^-=\pm g`$ ($`\rho`$ even, $`j`$ odd, $`F`$, $`\Delta\omega`$, $`\pi_k`$ even), as (7.23) demands. $`\Gamma^{(1),\perp}_{kk'}`$ is the inter-branch part: each of its terms carries the overlap $`\langle\beta_{k',\sigma}\vert\beta_{k,-\sigma}\rangle=-\sigma\sin\tfrac{\theta_k-\theta_{k'}}2`$ and one factor $`a_{k,\perp}`$ or $`a_{k',\perp}`$; it is estimated in (F3).
7. *Leading part for a start at rest (order estimate), the two classes, and a level-independent fall.* Conditions: (F1) a start at rest (label weight with the mean $`0`$ and the variance $`\delta p^2`$ on the arc $`(-\pi,\pi]`$), $`g`$ smooth and complex, in general neither even nor real, with $`\delta p\ll\min(1,M_k/\tau_k,M_{k'}/\tau_{k'})`$ and $`\langle\lvert p\rvert^n\rangle_g=O(\delta p^n)`$ for $`n\le6`$; (F2) $`\lvert\Delta\nu_{kk'}\rvert\,\lambda\,\delta p^2\ll1`$, with $`\nu_k:=\omega_k''(0)=\tau_k^2/M_k`$ and $`\Delta\nu_{kk'}:=\nu_k-\nu_{k'}`$, so that $`\Gamma^{(0)}_{kk'}\neq0`$ and $`\lvert\Gamma^{(0)}_{kk'}\rvert`$ is close to $`1`$. Order of limits: the first order is a Taylor coefficient at fixed $`\lambda`$ and start (no condition on $`\pi_k\lambda`$), long chain, leading order in $`\kappa`$; then the expansion in $`\delta p`$ at fixed $`\lambda`$ within (F2). With $`\Delta\omega=\Delta\omega(0)+\tfrac12\Delta\nu\,p^2+\dots`$ in (7.24), a real weight $`h`$ gives $`\mathrm{Im}\bigl[\int Fe^{-i\sigma\Delta\omega\lambda}h\big/\int Fe^{-i\sigma\Delta\omega\lambda}\rho\bigr]=-\tfrac\sigma2\lambda\,\Delta\nu\int\frac{\mathrm dp}{2\pi}(p^2-\delta p^2)h`$ at leading order. Applied to the two terms of (7.24) with the factor $`i`$ ($`h=\rho\,(\omega_{k'}'\pi_k-\omega_k'\pi_{k'})\simeq\rho\,\varpi_{kk'}p`$ and $`h=(\pi_k-\pi_{k'})j`$), with $`\pi_k:=\pi_{k,\sigma}(0)=\mathcal F_k-\sigma G_k`$ from here on:
```math
\Bigl(\frac{\lvert\Gamma_{kk'}\rvert}{\lvert\Gamma^{(0)}_{kk'}\rvert}\Bigr)_{1}\simeq\Delta\nu_{kk'}\Bigl[\tfrac14\lambda^3\,\varpi_{kk'}\,\langle p^3\rangle_g-\tfrac\sigma2\lambda^2\,(\pi_k-\pi_{k'})\,J_g\Bigr],\qquad\varpi_{kk'}:=\nu_{k'}\pi_k-\nu_k\pi_{k'},\quad J_g:=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\,(p^2-\delta p^2)\,\mathrm{Im}\bigl(g^{*}g'\bigr).
\qquad\text{(7.25)}
```
   - *The start enters through two numbers.* $`\langle p^3\rangle_g`$ is the third moment of the label weight (its skewness times $`\delta p^3`$). $`J_g`$ is minus the covariance, in the start, of $`p^2`$ with the position label: $`J_g=0`$ for real $`g`$, and $`J_g=3c\mathrm{Var}_g(p^2)`$ for $`g=\lvert g\rvert e^{icp^3}`$; a shift of the start in the position does not change it. $`\varpi_{kk'}`$ is the bracket of (7.10). The sign of (7.25) is not fixed: $`\lvert\Gamma_{kk'}\rvert`$ can rise or fall at first order, which is possible only because $`\lvert\Gamma^{(0)}_{kk'}\rvert<1`$ (factor $`\Delta\nu_{kk'}`$).
   - *(F3) Remainder (order estimate; $`\tau/M`$, $`\nu`$, $`\mathsf b`$ are the larger of the two levels' values).* Corrections to the two terms of (7.25) that are smaller than their largest possible sizes, $`\lambda^3\lvert\Delta\nu\rvert\,\nu\,\mathsf b\,\delta p^3`$ and $`\lambda^2\lvert\Delta\nu\rvert\,\mathsf b\,\delta p^2X_g`$ (from $`\lvert J_g\rvert\le\sqrt{\mathrm{Var}_g(p^2)}\,X_g`$), by the factors $`O\bigl(\delta p^2(1+\tau^2/M^2)\bigr)+O\bigl((\Delta\nu\,\lambda\,\delta p^2)^2\bigr)`$; the term of (7.24) with $`F'`$, $`O\bigl(\lambda\,\mathsf b\,\tfrac{\tau^2}{M^2}(1+\tfrac{\tau^2}{M^2})\,\delta p^3\bigr)`$; and $`\Gamma^{(1),\perp}_{kk'}=O\bigl(\tfrac{\tau^2\mathsf b}{M^3}\,\delta p^2X_g\bigr)+O\bigl(\lambda\,\tfrac{\tau^4\mathsf b}{M^4}\,\delta p^3\bigr)`$. So (7.25) is the part of the first-order term that grows fastest with $`\lambda`$. For level data that differ by relative amounts of order one, and $`\langle p^3\rangle_g\sim\delta p^3`$ or $`J_g\sim\delta p^2X_g`$, it exceeds the remainder for $`1/M+1/\tau\ll\lambda\ll1/(\lvert\Delta\nu\rvert\,\delta p^2)`$. No bound on the remainder is derived.
   - *Class with a first deviation of second order.* Starts of definite parity, $`g(-p)=\pm g(p)`$, for all level data and all $`\lambda`$; and every start for a pair of levels with equal $`(\tau,M)`$. Both statements are exact (part 5). For the starts (E1) the leading term is (7.10).
   - *Class with a first deviation of first order.* Starts at rest that are not of definite parity, for a pair of levels with $`\Delta\nu_{kk'}\neq0`$ and with $`\varpi_{kk'}\langle p^3\rangle_g\neq0`$ or $`(\pi_k-\pi_{k'})J_g\neq0`$: the leading part is (7.25). A real $`g`$ with a skewed label weight suffices. Order estimate: (7.25) exceeds second-order terms of the size of (7.10) where $`\lvert\varpi_{kk'}\rvert\lambda\,\delta p^2\ll\lvert\Delta\nu\,\langle p^3\rangle_g\rvert`$, respectively $`\lvert\pi_k-\pi_{k'}\rvert\,\delta x^2\ll\lvert\Delta\nu\,J_g\rvert`$. For a start that is not of definite parity with $`\langle p^3\rangle_g=J_g=0`$, and for a pair with $`\Delta\nu_{kk'}=0`$ and unequal data, the first-order term is at most of the size of the remainder (F3); whether it vanishes is not determined.
   - *Level-independent fall.* With $`a_{k,\sigma}(0)=\sigma\nu_k\pi_k=a`$ for all $`k`$: $`\pi_k=\sigma a/\nu_k`$, and (7.25) becomes
```math
\Bigl(\frac{\lvert\Gamma_{kk'}\rvert}{\lvert\Gamma^{(0)}_{kk'}\rvert}\Bigr)_{1}\simeq\frac{a\,\Delta\nu_{kk'}^2}{\nu_k\,\nu_{k'}}\Bigl[\tfrac12\lambda^2J_g-\tfrac\sigma4\lambda^3\,(\nu_k+\nu_{k'})\,\langle p^3\rangle_g\Bigr].
\qquad\text{(7.26)}
```
   For a start with $`J_g\neq0`$ or $`\langle p^3\rangle_g\neq0`$ it vanishes for all $`\lambda`$ iff $`a=0`$ or $`\nu_k=\nu_{k'}`$, the condition of part 4. So **no**: a level-independent fall with $`a\neq0`$ does not remove the first-order term, and in the class $`\mathcal C`$ ($`\tau_k=\tau`$, $`M_k`$ distinct) it never does. Variants (a), (c): $`a=-\tau^2g`$, $`\tfrac{\Delta\nu^2}{\nu_k\nu_{k'}}=\tfrac{(d_k-d_{k'})^2}{M_kM_{k'}}`$, $`\nu_k+\nu_{k'}=\tau^2\tfrac{M_k+M_{k'}}{M_kM_{k'}}`$. (7.26) has the class, the range and the status (order estimate) of (7.25).

### Step 6. Item 2(a): records at first order

In (4.1), $`p^{[\xi]}`$ belongs to the level profiles of the effective body contract with $`\mathcal F_k\to\mathcal F_k-\varepsilon_\xi`$. The zeroth-order velocity (4.5) does not depend on $`\xi`$; the first-order velocity is linear in $`(G_k,\mathcal F_k-\varepsilon_\xi,g_{\zeta,k})`$. Averaging with $`w_\xi`$ and $`\sum_\xi w_\xi\varepsilon_\xi=0`$:
```math
v^{(1)}\bigl[G_k,\mathcal F_k,g_{\zeta,k};\chi\bigr]=\sum_\xi w_\xi\Bigl(v^{(1)}[G_k,\mathcal F_k,g_{\zeta,k}]-\varepsilon_\xi\,\partial_{\mathcal F_k}v^{(1)}\Bigr)=v^{(1)}[G_k,\mathcal F_k,g_{\zeta,k}].
\qquad\text{(7.11)}
```
**No change**: (4.7), (4.16), (4.19) hold at first order jointly in $`G_k,\mathcal F_k,g_{\zeta,k},\kappa(\xi-\langle X\rangle)`$ for every $`\chi`$, sharp $`X`$ or not. The reason is linearity and the vanishing mean of $`\xi-\langle X\rangle`$, which is what counting $`\kappa\langle X\rangle`$ in $`V_{x,k}`$ achieves.

### Step 7. Item 2(b): mean velocity to second and third order in $`\kappa`$

All gradients of the effective body contract vanish; fix $`\xi`$, a level and $`\varepsilon:=\varepsilon_\xi`$. The level block is $`C_0(\hat p)+\varepsilon\hat x`$ plus a constant.
1. *Exact reduction.* $`e^{i\varepsilon\hat x\lambda}f(\hat p)e^{-i\varepsilon\hat x\lambda}=f(\hat p-\varepsilon\lambda)`$, so $`e^{-i(C_0+\varepsilon\hat x)\lambda}=e^{-i\varepsilon\hat x\lambda}W(\lambda)`$ with $`W`$ acting at each $`p`$ as the solution of $`i\partial_s\psi=C_0(q(s))\psi`$, $`q(s):=p-\varepsilon s`$, $`\psi(0)=\beta_\sigma(p)`$. The velocity operator is $`i[C,\hat x]=C_0'(\hat p)`$ (the records commute with $`\hat x`$), so $`v^{[\xi]}(\lambda)=\langle\,\psi^\dagger C_0'(q(\lambda))\psi\,\rangle_g`$.
2. *Bloch form.* $`C_0(q)=\omega(q)\,\mathbf n\cdot\boldsymbol\sigma`$ with $`\mathbf n=(\sin\theta,0,\cos\theta)`$, $`\mathbf e_\theta=\partial_\theta\mathbf n`$, $`\mathbf e_y=\mathbf n\times\mathbf e_\theta`$. For $`\mathbf S=\psi^\dagger\boldsymbol\sigma\psi=S_n\mathbf n+S_\theta\mathbf e_\theta+S_y\mathbf e_y`$, $`\dot{\mathbf S}=2\omega\,\mathbf n\times\mathbf S`$ and $`\dot{\mathbf n}=-\varepsilon\theta'\mathbf e_\theta`$ give, with all functions at $`q(s)`$,
```math
\dot S_n=-\varepsilon\theta'S_\theta,\quad\dot S_\theta=\varepsilon\theta'S_n-2\omega S_y,\quad\dot S_y=2\omega S_\theta,\quad\mathbf S(0)=\sigma\mathbf n;\qquad v_p=\omega'(q)S_n+\omega(q)\theta'(q)S_\theta .
\qquad\text{(7.12)}
```
3. *Solution to second order.* For $`z=S_\theta+iS_y`$: $`z(\lambda)=\varepsilon\int_0^\lambda\theta'S_n\,e^{i(\varphi(\lambda)-\varphi(s))}\mathrm ds`$, $`\varphi(s)=2\int_0^s\omega(q)`$. One integration by parts and $`\varphi(\lambda)=2\omega\lambda-\varepsilon\omega'\lambda^2+O(\varepsilon^2)`$ give, with all functions now at $`p`$: $`S_\theta=\tfrac{\varepsilon\sigma\theta'}{2\omega}\sin2\omega\lambda-\varepsilon^2\sigma\bigl[\tfrac{\theta'\omega'}{2\omega}\lambda^2\cos2\omega\lambda+\tfrac1{4\omega}(\theta'/\omega)'(1-\cos2\omega\lambda)\bigr]`$ and $`S_n=\sigma-\varepsilon^2\sigma\tfrac{\theta'^2}{4\omega^2}(1-\cos2\omega\lambda)`$. Expanding $`\omega'(q),(\omega\theta')(q)`$ about $`p`$: $`v_p=\sigma\omega'+\varepsilon\sigma\bigl[-\lambda\omega''+\tfrac12\theta'^2\sin2\omega\lambda\bigr]+\varepsilon^2v_2+O(\varepsilon^3)`$,
```math
v_2(p,\lambda)=\sigma\Bigl[\tfrac12\lambda^2\omega'''-\tfrac{\theta'\theta''}{4\omega}(1-\cos2\omega\lambda)-\tfrac{\lambda}{2\omega}\theta'(\omega\theta')'\sin2\omega\lambda-\tfrac12\lambda^2\theta'^2\omega'\cos2\omega\lambda\Bigr].
\qquad\text{(7.13)}
```
The first-order term agrees with (4.7) for $`\mathcal F=-\varepsilon`$ ($`a=\sigma\mathcal F\omega''`$, bounded rest) and averages to zero over $`\xi`$ (Step 6).
4. *Average over $`\xi`$ and $`g`$.* The $`\lambda^2\cos`$ term carries the factor $`\omega'`$: $`\langle\theta'^2\omega'\cos2\omega\lambda\rangle_g=-\tfrac1{2\lambda}\int\tfrac{\mathrm dp}{2\pi}(\lvert g\rvert^2\theta'^2)'\sin2\omega\lambda`$ (integration by parts on the circle). With $`\int\tfrac{\mathrm dp}{2\pi}\lvert(\lvert g\rvert^2)'\rvert\le2X_g`$ and $`\lvert\theta'\rvert\le\tau/M`$:
```math
\begin{aligned}
v(\lambda)&=\sigma\langle\omega_k'\rangle_g+\kappa^2\sigma_X^2\Bigl[\tfrac12\lambda^2\sigma\langle\omega_k'''\rangle_g+R_2(\lambda)\Bigr]+\kappa^3\mu_3\Bigl[-\tfrac16\lambda^3\sigma\langle\omega_k''''\rangle_g+R_3(\lambda)\Bigr]+O(\kappa^4),\\
\lvert R_2(\lambda)\rvert&\le\lambda\Bigl[\tfrac{\tau_k^2}{2M_k^2}X_g+\tfrac14\sup\lvert(\theta'^2)'\rvert+\tfrac12\sup\bigl\lvert\tfrac{\theta'(\omega\theta')'}{\omega}\bigr\rvert\Bigr]+\tfrac12\sup\bigl\lvert\tfrac{\theta'\theta''}{\omega}\bigr\rvert\ \ (\text{exact}),\qquad R_3(\lambda)=O(\lambda^{5/2})\ \ (\text{order estimate}).
\end{aligned}
\qquad\text{(7.14)}
```
The third-order secular term is the $`\varepsilon^3`$ coefficient of the adiabatic part $`\sigma\omega'(p-\varepsilon\lambda)`$ of (7.12). $`R_3`$ consists of terms oscillating at $`2\omega_k(p)`$ with amplitudes up to $`\lambda^4\theta'^2\omega'^2`$ and $`\lambda^3\theta'^2\omega''`$ (from the expansion of $`\varphi`$), reduced to $`O(\lambda^{5/2})`$ by integration by parts and stationary phase at $`\omega_k'=0`$, and of non-oscillating terms $`O(\lambda)`$. Range: fixed smooth $`g`$, chain and $`\lambda`$, $`\kappa\to0`$; the leading parts dominate for $`\lambda\gg X_g\tau_k^2/(M_k^2\lvert\langle\omega_k'''\rangle_g\rvert)`$ within $`\kappa\lvert\xi-\langle X\rangle\rvert\lambda\ll\min(1,M_k/\tau_k)`$ on the support of $`w_\xi`$. The bound on $`R_2`$ is not uniform in $`\delta p\to0`$ ($`X_g\ge1/(2\delta p)`$): for a sharp label the oscillating terms of (7.13) are removed by a window average instead, with relative size $`O(1/(M_k\Lambda))`$ (order estimate). Controls: a sharp $`X`$ gives $`\sigma_X=\mu_3=0`$ and no term; a symmetric distribution of $`X`$ gives $`\mu_3=0`$.

### Step 8. Item 2(c),(d): change of the acceleration

1. *Closed form.* For a sharp label $`p_0`$ (order: $`\kappa`$-expansion at fixed $`\lambda`$; window average; $`\delta p\to0`$), the $`\lambda`$-derivative of the secular parts of (7.14), with $`v=\sigma\omega_k'(p_0)`$ of (4.17) and $`\omega'''=-\omega'(4+3\omega''/\omega)`$:
```math
\delta a^{(2)}_{k,\sigma}=\kappa^2\sigma_X^2\,\lambda\,\sigma\,\omega_k'''(p_0)=-\kappa^2\sigma_X^2\,\lambda\,v\Bigl(4+\frac{3\,\omega_k''(p_0)}{\omega_k(p_0)}\Bigr)=-\kappa^2\sigma_X^2\,\lambda\Bigl(4+\frac{3\tau_k^2}{M_k^2}\Bigr)v+O(v^3).
\qquad\text{(7.15)}
```
It vanishes at rest, is of first order in $`v`$, opposes $`v`$, grows linearly in $`\lambda`$, and at given $`v`$ is the same in both branches. The third-order term does not vanish at rest:
```math
\delta a^{(3)}_{k,\sigma}=-\tfrac12\kappa^3\mu_3\,\lambda^2\,\sigma\,\omega_k''''(p_0),\qquad\delta a^{(3)}_{k,\sigma}\big\vert_{p_0=0}=\frac{\sigma}{2}\,\kappa^3\mu_3\,\lambda^2\,\frac{\tau_k^2}{M_k}\Bigl(4+\frac{3\tau_k^2}{M_k^2}\Bigr).
\qquad\text{(7.16)}
```
It is odd in the branch and present only for a skewed distribution of $`X`$.
2. *Level dependence.* (7.15) is the same for all levels at leading order in $`v`$ **iff** $`\tau_k/M_k`$ does not depend on $`k`$, and as a function of $`p_0`$ iff $`(\tau_k,M_k)`$ do not ($`\omega_k-\omega_{k'}`$ constant forces equal data, as in Step 3). (7.16) at rest is level-independent iff $`\tfrac{\tau_k^2}{M_k}(4+\tfrac{3\tau_k^2}{M_k^2})`$ is. In the class $`\mathcal C`$ ($`\tau_k=\tau`$, $`M_k`$ distinct): **no** in both cases; for $`M_k\ll\tau`$ the terms scale as $`M_k^{-2}`$ and $`M_k^{-3}`$.
3. *Background form (item 2(d)).* With $`d_0=\kappa\sigma_X`$, $`v_{\max,k}:=\tau_kd_0`$ ((5.11) of 04-ilang-time/05-moving-clock with $`\tau\to\tau_k`$; $`=v_{\max}`$ in $`\mathcal C`$), $`\hat e`$ and $`\bar x=d_0\bar x_{\rm lab}\hat e`$ of (17.15) of 03-ilang-space/17-motion, $`u:=d_0v`$ and $`\gamma_X:=\mu_3/\sigma_X^3`$:
```math
\delta\frac{\mathrm d^2\bar x}{\mathrm d\lambda^2}=\Bigl[-\lambda\Bigl(4d_0^2+\frac{3v_{\max,k}^2}{M_k^2}\Bigr)u+\frac{\sigma\gamma_X}{2}\,\lambda^2\,\frac{v_{\max,k}^2}{M_k}\Bigl(4d_0^2+\frac{3v_{\max,k}^2}{M_k^2}\Bigr)\Bigr]\hat e,\qquad d_0\,a_{k,\sigma}(0)=\frac{v_{\max,k}^2}{d_0M_k}\bigl(\sigma\mathcal F_k-G_k\bigr).
\qquad\text{(7.17)}
```
The record terms are smaller than the drift acceleration (4.7) at rest where
```math
\varrho_2:=\frac{\lambda\lvert u\rvert M_k}{d_0\,\tau_k^2\lvert\sigma\mathcal F_k-G_k\rvert}\Bigl(4d_0^2+\frac{3v_{\max,k}^2}{M_k^2}\Bigr)<1\quad\text{and}\quad\varrho_3:=\frac{\lvert\gamma_X\rvert d_0\lambda^2}{2\lvert\sigma\mathcal F_k-G_k\rvert}\Bigl(4d_0^2+\frac{3v_{\max,k}^2}{M_k^2}\Bigr)<1,
\qquad\text{(7.18)}
```
that is $`\lambda<\lambda_2\propto\lvert\sigma\mathcal F_k-G_k\rvert/(\kappa^2\lvert v\rvert)`$ and $`\lambda<\lambda_3\propto(\lvert\sigma\mathcal F_k-G_k\rvert/\kappa^3)^{1/2}`$. Order estimate for a fall from rest ($`\lvert v\rvert\le\lvert a\rvert\lambda`$; this mixes $`\kappa^2`$ with a gradient and is outside the derived orders): $`\varrho_2\lesssim\lambda^2(4d_0^2+3v_{\max,k}^2/M_k^2)`$, independent of the gradients. Both ratios are level-dependent at their own order. So "weak records" must mean $`\varrho_2,\varrho_3\le\delta_{\rm acc}`$ for every level involved, on the whole range of $`\lambda`$ and of $`v`$ observed, for the fall to be level-independent to the relative accuracy $`\delta_{\rm acc}`$: a joint condition $`\kappa^2\lambda\lvert v\rvert\ll`$ gradient and $`\kappa^3\lvert\mu_3\rvert\lambda^2\ll`$ gradient, not uniform in $`\lambda`$ and violated if the gradients are sent to zero at fixed $`\kappa`$.

### Step 9. Item 3: the operator under the factor

1. *Fall from rest.* $`(1+gx)[M_k\sigma_3+u_k]-\mathcal F_Ux=M_k\sigma_3+gM_kx\,\sigma_3+u_k-(\mathcal F_U-gu_k)x`$, a linear level profile with $`G_k=gM_k`$, $`\mathcal F_k=\mathcal F_U-gu_k`$, $`V_k=u_k`$. The hopping factors do not enter (4.16):
```math
a_{k,\pm}(0)=-g\,\tau_k^2\pm\frac{\tau_k^2}{M_k}\bigl(\mathcal F_U-g\,u_k\bigr).
\qquad\text{(7.19)}
```
```math
\begin{aligned}
\text{upper: }&\tau_k^2\Bigl[\tfrac{\mathcal F_U-gu_k}{M_k}-g\Bigr]=a_+\ \forall k;\qquad\text{lower: }\tau_k^2\Bigl[-\tfrac{\mathcal F_U-gu_k}{M_k}-g\Bigr]=a_-\ \forall k;\\
\text{both, }a_+=a_-=a:\ &g\,u_k=\mathcal F_U\ \text{ and }\ g\,\tau_k^2=-a\quad\forall k.
\end{aligned}
\qquad\text{(7.20)}
```
(Sum and difference of the two lines give the third.) For $`\tau_k=\tau`$ the upper and the lower condition coincide, for every $`g`$: $`(\mathcal F_U-gu_k)/M_k=:y_U`$ independent of $`k`$, and then $`a_\pm=\tau^2(-g\pm y_U)`$; one value iff $`y_U=0`$. For $`g\neq0`$, with $`y_U=:-g\,w`$, this is $`u_k=u_*+wM_k`$ with $`gu_*=\mathcal F_U`$, and $`a_\pm=-\tau^2g(1\pm w)`$; one value iff $`w=0`$. For $`g=0`$ the numbers $`u_k`$ drop out and the condition is on $`\mathcal F_U/M_k`$ alone: it holds iff $`\mathcal F_U=0`$ (then $`a_\pm=0`$) or all $`M_k`$ are equal (then $`a_\pm=\pm\tau^2\mathcal F_U/M_k`$; one value iff $`\mathcal F_U=0`$).
2. *Well-defined statements (M6).* By (8.1) and (8.20) of 04-ilang-time/08-maximal-speed the effective body contract is defined modulo $`c\,\mathbb 1`$ with one real $`c`$ for all $`x`$, branches and levels (a level-dependent constant is not diagonal in the places and is not a replacement of (8.1)). In the parametrization of item 3,
```math
C_{\rm eff}\mapsto C_{\rm eff}+c\,\mathbb 1\iff(u_k,\mathcal F_U)\mapsto(u_k+c,\ \mathcal F_U+g\,c);\qquad\text{invariants: }g,\ M_k,\ u_k-u_{k'},\ \mathcal F_k=\mathcal F_U-g\,u_k .
\qquad\text{(7.21)}
```
Hence: $`u_k`$ — **not** well defined; $`u_k-u_{k'}`$ — **well defined**; "$`u_k=0`$ for all $`k`$" — **not** well defined (well defined are "$`u_k`$ is the same for all $`k`$" and "$`\mathcal F_U=gu_k`$ for all $`k`$"); "$`u_k\propto M_k`$" — **not** well defined (well defined is "$`u_k`$ is affine in $`M_k`$", with the slope $`w`$ and $`\mathcal F_U-gu_*`$). The conditions (7.20) contain only invariants.
3. *Evaluations.* $`u_k=uM_k`$: $`a_{k,\sigma}(0)=-\tau_k^2g(1+\sigma u)+\sigma\tau_k^2\mathcal F_U/M_k`$; for $`\tau_k=\tau`$ and distinct $`M_k`$ it is level-independent iff $`\mathcal F_U=0`$, with the branch-dependent value $`-\tau^2g(1+\sigma u)`$. Class $`\mathcal C`$, variant (f) with a plain gradient ($`u_k=c_{\rm f}`$): $`a_{k,\sigma}(0)=-\tau^2g+\sigma\tau^2(\mathcal F_U-gc_{\rm f})/M_k`$, level-independent iff $`\mathcal F_U=gc_{\rm f}`$, then $`-\tau^2g`$ in both branches; $`\mathcal F_U=0`$ reproduces row (f) of (4.25). Control: $`\mathcal F_U-gu_k=0`$ (e.g. $`u_k=0`$, $`\mathcal F_U=0`$) against $`u_k=c_{\rm f}\neq0`$, $`\mathcal F_U=0`$.

### Step 10. Item 4: table of orders

Orders are those of the leading deviation; "grad" is the joint order in the gradients, the entries on $`M_k/\tau_k`$ are relative to the fall. (i): the fall is the same for all levels; (ii): the relation (4.24), a statement at rest in the class $`\mathcal C`$.

| Source | (i) level-independent fall | (ii) relation (4.24) | Tags |
|---|---|---|---|
| Lattice | grad$`^1`$, $`v^2`$, relative $`(M_k/\tau_k)^2`$, $`\kappa^0`$, $`\lambda^0`$: $`c_{2,k,+}-c_{2,k',+}=-2a_0\bigl(\tfrac{M_k^2}{\tau_k^4}-\tfrac{M_{k'}^2}{\tau_{k'}^4}\bigr)`$; none at $`v=0`$ | none at $`v=0`$; at $`v\neq0`$ level-dependent at grad$`^1`$, $`v^2`$, $`(M_k/\tau)^2`$ | (4.20), (4.21), (4.23), (4.25) |
| Drift velocity | grad$`^1`$, $`v^2`$, $`(M_k/\tau_k)^0`$ unless $`c^{(0)}_{2,k}`$ is level-independent; in $`\mathcal C`$ only for $`\mathcal F=0`$, $`g_m=g_\eta`$; $`O(v^4)`$ an order estimate | the acceleration is $`a(0)+c_2v^2`$: grad$`^1`$, relative $`c_2v^2/a(0)`$ (variant (a): $`-\ell_kv^2/\tau^2`$), $`\kappa^0`$, $`\lambda^0`$ | (4.17), (4.20), (4.21), (4.23) |
| Superposition of levels | no new condition; if the fall is level-dependent: mean acceleration $`\alpha`$-dependent at grad$`^1`$; between-level variance grad$`^2`$, $`\lambda^4`$; at $`p_0\neq0`$ separation at grad$`^0`$, $`v^1`$, $`\lambda^1`$ | position side unchanged (exact mixture); label rates level-dependent at grad$`^1`$; $`\lvert\Gamma_{kk'}\rvert`$: for starts of definite parity, $`g(-p)=\pm g(p)`$, no grad$`^1`$ term (exact), and for the starts (E1) grad$`^2`$ with $`\lambda^2\delta x^2`$ and $`\lambda^4/\delta x^2`$ (order estimate, range (E3)); for starts at rest that are not of definite parity grad$`^1`$ with $`\lambda^3\Delta\nu_{kk'}\langle p^3\rangle_g`$ and $`\lambda^2\Delta\nu_{kk'}J_g`$ (order estimate, range (F1)–(F3)); in both classes also for a level-independent fall with $`a\neq0`$, unless $`\tau_k^2/M_k=\tau_{k'}^2/M_{k'}`$ | (7.1)–(7.5), (7.7), (7.9), (7.10), (7.23)–(7.26) |
| Records | $`\kappa^1`$: none; $`\kappa^2\sigma_X^2`$: grad$`^0`$, $`v^1`$, $`\lambda^1`$, factor $`4+3\tau_k^2/M_k^2`$; $`\kappa^3\mu_3`$: grad$`^0`$, $`v^0`$, $`\lambda^2`$, factor $`\tfrac{\tau_k^2}{M_k}(4+\tfrac{3\tau_k^2}{M_k^2})`$ | the same terms add to the left side; negligible on the range (7.18) | (7.11), (7.14)–(7.18) |
| Operator under the factor | grad$`^1`$, $`v^0`$, $`\kappa^0`$, $`\lambda^0`$, relative $`(\mathcal F_U-gu_k)/(gM_k)`$: the same order as the fall, no small parameter | in $`\mathcal C`$ the hypothesis holds iff $`\mathcal F_U=gc_{\rm f}`$; then unchanged | (7.19)–(7.21), (4.25) row (f) |
| Plain gradient | grad$`^1`$, $`v^0`$: $`\sigma\tau_k^2\mathcal F_k/M_k`$, level-dependent and odd in the branch; in $`\mathcal C`$ admissible at rest only for $`\mathcal F=\pm m(g_m-g_\eta)`$, through $`v^2`$ only $`\mathcal F=0`$ (leading order in $`M_k/\tau`$) | the hypothesis fixes $`\mathcal F=m(g_m-g_\eta)`$; any other $`\mathcal F`$ breaks it at grad$`^1`$, $`v^0`$ | (4.16), (4.19), (4.22), (4.23), (4.25) row (d) |
```math
\text{(the table above is the result of item 4)}
\qquad\text{(7.22)}
```

## Result

Common class, unless an item restricts it: a body of $`\mathcal C_{\rm lev}`$ with linear level profiles, both branches $`\sigma`$, every level, $`\lambda\ge0`$, the infinite chain as the limit of long chains. "First order" is the first order in the gradients at fixed $`\lambda`$, start and chain, followed by the long chain. "Leading order in $`\kappa`$" is $`\kappa\to0`$ at fixed $`\lambda`$, chain and start (the effective body contract). An *order estimate* is not a bound.

**Item 1, starts $`\Phi_\sigma[\alpha,g]`$.**
- **(7.1)** Exact in the gradients and in $`\kappa`$; every $`\alpha`$, smooth $`g`$, $`\chi`$, $`\lambda`$ and chain. $`p_x=\sum_k\lvert\alpha_k\rvert^2p^{(k)}_x`$ and $`\bar x_{\rm lab}=\sum_k\lvert\alpha_k\rvert^2\bar x_k`$. It rests on the conservation of the level and the orthonormality of the $`\lvert f_k\rangle`$.
- **(7.2)** Every $`\alpha`$ and every smooth $`g`$ concentrated at $`p_0`$; first order, long chain, $`\Lambda\to\infty`$, then $`\delta p\to0`$; leading order in $`\kappa`$. Drift acceleration $`\sum_k\lvert\alpha_k\rvert^2a_{k,\sigma}(p_0)`$, with the exact bound of (7.2) for every window $`\Lambda>0`$. It is the same for all $`\alpha`$ iff $`a_{k,\sigma}(p_0)`$ is level-independent; at rest this is line 1 or 2 of (4.19), with no new condition.
- **(7.3), (7.4)** Starts at rest; first order, long chain; fixed smooth $`g`$. $`D=\tfrac14\lambda^4\mathrm{Var}_\alpha(\langle a_{\cdot,\sigma}\rangle_g)+E`$, with the exact bound on $`E`$ for all $`\lambda\ge0`$; the $`\lambda^4`$ part dominates for $`\lambda\gg r/\sqrt{\mathrm{Var}_\alpha}`$; its coefficient tends to $`\tfrac14\mathrm{Var}_\alpha(a_{\cdot,\sigma}(0))`$ for $`\delta p\to0`$, taken last. (7.4), class $`\mathcal C`$ with $`\lvert\alpha_k\rvert^2=1/N`$: zero for (a), (c); $`\tfrac14\lambda^4\tau^4g^2m^2\mathcal V_N`$ for (b1), (b2); $`\tfrac14\lambda^4\tau^4g^2c_{\rm f}^2\mathcal V_N`$ for (f).
- **(7.5)** Zero gradients, exact; $`\delta p\to0`$. Velocities $`\sigma\omega_k'(p_0)`$. In $`\mathcal C`$ no two levels have equal velocities for $`\sin2p_0\neq0`$. In $`\mathcal C_{\rm lev}`$ two levels with different data have equal velocities at one such $`p_0`$ under one condition, which needs $`\tau_k\neq\tau_{k'}`$; at all $`p_0`$ iff the data are equal.
- **(7.6), (7.7)** (7.6): exact in the gradients, any normalized level component. (7.7): starts at rest; first order at fixed $`\lambda`$ and start, long chain, then $`\delta p\to0`$; no window. Rate of the mean label $`\mathcal F_k-\sigma G_k`$. Level-independent iff $`\mathcal F_k-\sigma G_k`$ is; together with a level-independent drift acceleration $`a\neq0`$ iff also $`\tau_k^2/M_k`$ is level-independent; impossible in $`\mathcal C`$.
- **(7.8), (7.9)** (7.8): clock-label statistics through $`\alpha`$ and $`\Gamma_{kk'}`$, exact with the medium in the level components; at leading order in $`\kappa`$ the $`\Gamma_{kk'}`$ of the effective body contract. (7.9): the zero-gradient coherence, exact for every smooth $`g`$; for even $`g`$, $`\Gamma_{kk'}`$ is exactly even in the gradients.
- **(7.23)** Exact; every smooth $`g`$, every $`p_0`$ and $`\lambda`$; effective body contract. $`\Gamma_{kk'}[g;\text{gradients}]=\Gamma_{kk'}[g^-;-\text{gradients}]`$. **The first deviation of $`\lvert\Gamma_{kk'}\rvert`$ is of second order** for every start of definite parity, $`g(-p)=\pm g(p)`$, and for every start if $`(\tau_k,M_k)=(\tau_{k'},M_{k'})`$.
- **(7.10)** Order estimate. Class: real Gaussian starts at rest (E1), $`\delta p\ll\min(1,M_k/\tau_k)`$. Range (E3): $`\lvert\pi_k\rvert\lambda\ll M_k/\tau_k`$, $`\lvert\nu_k-\nu_{k'}\rvert\lambda\,\delta p^2\ll1`$, and $`\lambda\gg\tau_k/M_k^2`$. Second order in the gradients at fixed $`\lambda`$ and start; leading order in $`\kappa`$. $`1-\lvert\Gamma_{kk'}\rvert/\lvert\Gamma^{(0)}_{kk'}\rvert\simeq\tfrac12\delta x^2(\pi_k-\pi_{k'})^2\lambda^2+\tfrac{\lambda^4}{32\delta x^2}\varpi_{kk'}^2`$. With a level-independent fall $`a`$ it vanishes iff $`a=0`$ or $`\tau_k^2/M_k=\tau_{k'}^2/M_{k'}`$.
- **(7.24)** Every smooth complex $`g`$; first order at fixed $`\lambda`$ and start; leading order in $`\kappa`$. The first-order term of $`\Gamma_{kk'}`$: its part inside the branch is exact, its inter-branch part is estimated (F3).
- **(7.25)** Order estimate. Class (F1): starts at rest with a smooth complex $`g`$ that need not be even or real, $`\delta p\ll\min(1,M_k/\tau_k,M_{k'}/\tau_{k'})`$. Range (F2): $`\lvert\Delta\nu_{kk'}\rvert\lambda\,\delta p^2\ll1`$; it exceeds the remainder (F3) for $`1/M+1/\tau\ll\lambda`$ when the level data differ by relative amounts of order one. Limits: first order at fixed $`\lambda`$ and start, long chain, leading order in $`\kappa`$, then leading order in $`\delta p`$. **The first deviation of $`\lvert\Gamma_{kk'}\rvert`$ is of first order** for starts that are not of definite parity, with the fastest-growing part $`\Delta\nu_{kk'}\bigl[\tfrac14\lambda^3\varpi_{kk'}\langle p^3\rangle_g-\tfrac\sigma2\lambda^2(\pi_k-\pi_{k'})J_g\bigr]`$; it needs $`\Delta\nu_{kk'}\neq0`$ and a skewed label weight or $`J_g\neq0`$.
- **(7.26)** Same class, range and status as (7.25). A level-independent fall $`a\neq0`$ does not remove the first-order term unless $`\tau_k^2/M_k=\tau_{k'}^2/M_{k'}`$; in $`\mathcal C`$ it never does.

**Item 2, branch starts $`B_{k,\sigma}[g]`$.**
- **(7.11)** Every smooth $`g`$ and every $`\chi`$; first order jointly in $`G_k`$, $`\mathcal F_k`$, $`g_{\zeta,k}`$ and $`\kappa(\xi-\langle X\rangle)`$. The first-order velocity does not change when $`X`$ is not sharp; (4.7), (4.16), (4.19) are unchanged.
- **(7.13), (7.14)** Zero gradients of the effective body contract; every smooth $`g`$ and every $`\chi`$ with finite moments of $`X`$; Taylor expansion in $`\kappa`$ at fixed $`\lambda`$, start and chain. $`v=\sigma\langle\omega_k'\rangle_g+\kappa^2\sigma_X^2\bigl[\tfrac12\lambda^2\sigma\langle\omega_k'''\rangle_g+R_2\bigr]+\kappa^3\mu_3\bigl[-\tfrac16\lambda^3\sigma\langle\omega_k''''\rangle_g+R_3\bigr]+O(\kappa^4)`$. The bound on $`R_2`$ is exact, linear in $`\lambda`$, for all $`\lambda\ge0`$ at fixed $`g`$, and not uniform for $`\delta p\to0`$; $`R_3=O(\lambda^{5/2})`$ is an order estimate. The leading parts dominate for $`\lambda\gg X_g\tau_k^2/(M_k^2\lvert\langle\omega_k'''\rangle_g\rvert)`$ within $`\kappa\lvert\xi-\langle X\rangle\rvert\lambda\ll\min(1,M_k/\tau_k)`$.
- **(7.15), (7.16)** Sharp label $`p_0`$: expansion in $`\kappa`$ at fixed $`\lambda`$, window average (its suppression of the oscillating terms is an order estimate), then $`\delta p\to0`$. $`\delta a^{(2)}_{k,\sigma}=-\kappa^2\sigma_X^2\lambda\,v\,(4+3\omega_k''/\omega_k)`$: zero at rest, of first order in $`v`$, the same in both branches at given $`v`$. $`\delta a^{(3)}_{k,\sigma}`$ at rest is $`\tfrac\sigma2\kappa^3\mu_3\lambda^2\tfrac{\tau_k^2}{M_k}(4+\tfrac{3\tau_k^2}{M_k^2})`$: odd in the branch, only for a skewed $`X`$. Level-independent iff $`\tau_k/M_k`$, respectively $`\tfrac{\tau_k^2}{M_k}(4+\tfrac{3\tau_k^2}{M_k^2})`$, is; not in $`\mathcal C`$.
- **(7.17), (7.18)** The same terms in the background of (17.15) of 03-ilang-space/17-motion, with $`d_0=\kappa\sigma_X`$ and $`v_{\max,k}=\tau_kd_0`$ from (5.11) of 04-ilang-time/05-moving-clock. They are smaller than the drift acceleration (4.7) at rest where $`\varrho_2<1`$ and $`\varrho_3<1`$. "Weak records" has to mean $`\varrho_2,\varrho_3\le\delta_{\rm acc}`$ for every level on the whole observed range of $`\lambda`$ and $`v`$.

**Item 3, on-site block $`(1+gx)[M_k\sigma_3+u_k\mathbb 1_2]-\mathcal F_Ux\,\mathbb 1_2`$, any $`\tau_k`$ and $`g_{\zeta,k}`$; branch starts at rest; drift acceleration (first order, long window, sharp label), leading order in $`\kappa`$.**
- **(7.19), (7.20)** $`a_{k,\pm}(0)=-g\tau_k^2\pm\tfrac{\tau_k^2}{M_k}(\mathcal F_U-gu_k)`$, and the three equivalences; one value in both branches iff $`gu_k=\mathcal F_U`$ and $`g\tau_k^2=-a`$ for all $`k`$.
- **(7.21)** Well defined: $`g`$, $`M_k`$, $`u_k-u_{k'}`$, $`\mathcal F_U-gu_k`$. Not well defined: $`u_k`$, "$`u_k=0`$ for all $`k`$", "$`u_k\propto M_k`$".

**Item 4.** **(7.22)** the table of orders, with the class of starts in the row on the superposition of levels.

## Consistency checks

1. **Dimensions.** With costs and $`\tau,M,G,\mathcal F,\kappa\sigma_X`$ in units of $`1/\lambda`$ and labels dimensionless: (7.15) is $`\lambda^{-2}\cdot\lambda\cdot\lambda^{-1}=\lambda^{-2}`$, (7.16) is $`\lambda^{-3}\lambda^2\lambda^{-1}=\lambda^{-2}`$, as (4.16); both terms of (7.10) and $`\varrho_2,\varrho_3`$ are dimensionless; (7.3) is dimensionless (labels squared). Passed.
2. **One level and a sharp $`X`$.** $`\alpha_k=\delta_{kk_0}`$: (7.1), (7.2) reduce to the single-level start, $`D=0`$ in (7.3), and (7.8) gives $`P(a)=1/N`$, the uniform clock-label statistics of $`\lvert f_{k_0}\rangle`$. Sharp $`X`$: $`w_\xi=\delta_{\xi\xi_0}`$, $`\varepsilon_\xi=0`$, so (7.11) is trivial and (7.14)–(7.17) reduce to (4.5). Passed.
3. **Short-$`\lambda`$ expansion of (7.13).** Directly, the $`\varepsilon^2`$ term of $`v_p`$ at small $`\lambda`$ is $`\tfrac12\lambda^2\varepsilon^2\langle\beta_\sigma\vert C_0'''\vert\beta_\sigma\rangle=\tfrac12\lambda^2\varepsilon^2\sigma(\omega'''-3\omega'\theta'^2-3\omega\theta'\theta'')`$ (double commutator with $`\varepsilon\hat x`$; $`\mathbf n`$-component of $`(\omega\mathbf n)'''`$). Expanding (7.13) to $`\lambda^2`$ gives $`\sigma\lambda^2[\tfrac12\omega'''-\tfrac12\omega\theta'\theta''-\theta'(\omega\theta')'-\tfrac12\theta'^2\omega']`$, the same. Also, with zero gradients except $`\mathcal F`$, (7.7) and (4.16) agree with $`a=\sigma\omega''(0)\,\mathrm d\bar p/\mathrm d\lambda`$. Passed.

## Open issues

- The coefficients of (7.10) are an order estimate under (E1)–(E3) (Gaussian even start, within-branch transport, equal spreading); a bound, and the second-order term for other starts of definite parity, are not derived.
- (7.25) and (7.26) are order estimates under (F1)–(F3): the remainder is estimated, not bounded. For a start at rest that is not of definite parity with $`\langle p^3\rangle_g=J_g=0`$, and for a pair of levels with $`\Delta\nu_{kk'}=0`$ and unequal data, the first-order term of $`\lvert\Gamma_{kk'}\rvert`$ is at most of the size of the remainder (F3); whether it vanishes is not determined. Outside (F2), $`\lvert\Delta\nu_{kk'}\rvert\lambda\,\delta p^2\gtrsim1`$, only (7.24) is available. The second-order term of a start that is not of definite parity is not derived.
- $`R_3=O(\lambda^{5/2})`$ in (7.14) and the window suppression $`O(1/(M_k\Lambda))`$ of the oscillating terms for a sharp label are order estimates; only $`R_2`$ has an exact bound, and it is not uniform in $`\delta p\to0`$.
- The estimate $`\varrho_2\lesssim\lambda^2(4d_0^2+3v_{\max,k}^2/M_k^2)`$ for a fall from rest mixes $`\kappa^2`$ with a gradient (third order, out of scope) and is not derived.
- (7.17) uses $`v_{\max,k}=\tau_kd_0`$ for level-dependent $`\tau_k`$; the quoted bound (5.11) of 04-ilang-time/05-moving-clock is stated for one $`\tau`$.
- The effect of an operator under the factor on the relation (4.24) outside the class $`\mathcal C`$ (for example $`u_k=u_*+wM_k`$ with $`w\neq0`$) needs the clock rate of that body, which is not among the quoted inputs.

## Methods used

- Block decomposition by a conserved label; witness rule for the clock label
- First-order perturbation theory in the gradients; linearity of mixtures
- Continuity equation for the plane-wave label weight
- Reflection symmetry (parity) argument for the order of a deviation
- Interaction-picture first-order perturbation theory for the overlap of two level components; moment expansion of an oscillating average
- Gaussian overlap of displaced wave packets (order estimate)
- Exact reduction to a driven two-level problem; Bloch equations; adiabatic expansion with integration by parts
- Stationary phase and Riemann–Lebesgue estimates for oscillating averages
- Invariance under replacements of contract terms (well-definedness)
