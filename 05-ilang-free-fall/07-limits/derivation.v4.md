# Limits of the level-independent fall: level superpositions, records, the operator under the factor

- **Subproject:** 05-ilang-free-fall
- **Package:** 07-limits
- **Version:** v4
- **Mode:** external regeneration
- **Date:** 2026-10-11

## Changes from previous version

External regeneration after `verification.r2.md` (round 2 on v3, issues I1–I6, all accepted). Tags (7.1)–(7.34) are kept; new displays carry (7.35)–(7.46). No tag is withdrawn.

**Restated displays that keep their tag.**
- **(7.10):** formula unchanged; it is now the special case (E1) of the general second-order term (7.38), not a separate estimate.
- **(7.32):** restated. v3: an asserted size $`N_\perp`$ of the inter-branch part. Now: the size of everything that (7.38) neglects, each contribution with its calculation.
- **(7.15), (7.16):** formulas unchanged. They are now the answer for one stated order of limits (case A of (7.44)); (7.15) carries its near-rest regime (I6).
- **(7.17), (7.18):** the level speed bound $`c_k=\tau_kd_0`$ of (7.45) replaces "$`v_{\max,k}`$" (I5); (7.17) displays the omitted velocity orders (I6).
- **(7.33):** formula unchanged; the text after it no longer uses $`X_g\ge1/(2\delta p)`$, and the window condition is called sufficient (I3).
- **(7.34):** $`\varrho_{2,\rm rest}`$ unchanged; the third-order rest $`\varrho_{3,\rm rest}`$, which v3 gave in the text, is added to the display with its estimate.
- **(7.31):** inequality unchanged; its right side is named $`\epsilon_0`$. **(7.25):** formula unchanged; identified with $`\mathrm{Re}\epsilon_1`$ of (7.35), and $`\varpi_{kk'}`$, $`J_g`$ are now defined before it. **(7.29):** the status word of the bound is "bound".
- **(7.22):** rows "Superposition of levels" and "Records".

**Statements withdrawn (no tag):** the inequality $`X_g\ge1/(2\delta p)`$ and the lower bound on $`c_1[g]`$ built on it (I3); "the sharp-label limit can be combined with the long window *only* if $`X_g/\Lambda\to0`$" (I3); "$`v_{\max,k}=\tau_kd_0`$ by (5.11) of 04-ilang-time/05-moving-clock" (I5); "item 1(f) is resolved in part" and "items 2(c), (d) are resolved for the secular terms" (I1, I2).

**Changed passages.**
1. Setup: the convention for the effective blocks and the centred record term (I4); the scale $`p_c`$.
2. Step 1, part 1: the total contract is written with $`X-\langle X\rangle\mathbb 1`$ (I4).
3. Step 5: parts 1, 2 unchanged; part 3 (new) the exact expansion of $`\lvert\Gamma_{kk'}\rvert`$ to second order and the case distinction of the order, (7.35), (7.36); part 4 the first-order term (v3 parts 5, 6, unchanged in content); part 5 (new) narrow starts at rest, (7.37), (7.38), (7.10), (7.25), (7.32); part 6 (new) starts that are not narrow and pairs with equal data, (7.39); part 7 the level-independent fall, (7.26), (7.40). v3 part 8 ("resolved in part") is removed.
4. Step 7, part 4: the estimate of $`R_3`$ with its dependence on the spread; the false inequality removed.
5. Step 8: rewritten. Part 1 the exact acceleration for every start, (7.41); part 2 the two orders of limits, (7.44), with (7.15), (7.16), (7.33) for case A and (7.42), (7.43) for case B; part 3 level dependence in each case; part 4 the background form with (7.45), (7.17), (7.18), (7.34), (7.46).
6. Step 10, Result, Consistency checks (check 3 extended), Open issues, Methods used.

Unchanged in content: Steps 2, 3, 4, 6, 9; Step 1, parts 2, 3; Step 7, parts 1–3.

## Response to verification

- **I1: Accepted and fixed in Step 5, parts 3 and 5–7.** The expansion of $`\lvert\Gamma_{kk'}\rvert`$ to second order is given exactly for every smooth $`g`$, (7.35), with a complete case distinction of the order of the first deviation, (7.36). For narrow starts at rest of any shape the leading second-order term is derived, (7.38), with a lower bound that shows when it is different from zero; for pairs with equal data the second-order term is exact for every start, (7.39). Every contribution neglected in (7.38) is estimated by a calculation, (7.32).
- **I2: Accepted and fixed in Step 8.** The acceleration is taken from the complete coefficient (7.13): exactly for every smooth $`g`$, (7.41), and in the two orders of limits that do not commute, (7.44). The term quoted by the verifier is in (7.41), (7.42). The third order is exact at rest for a sharp label, (7.43). The level-independence conditions are stated for each case; the accuracy range of item 2(d) is (7.46).
- **I3: Accepted and fixed in Step 5, part 5, Step 7, part 4, and Step 8, parts 2 and 4.** The inequality with the boundary term, $`2\delta p\,X_g\ge\lvert1-\lvert g(p_0+\pi)\rvert^2\rvert`$, is derived and used; the window condition is sufficient, not necessary.
- **I4: Accepted and fixed in Setup and Step 1, part 1.** With effective blocks the total contract contains $`\kappa\hat x\otimes(X-\langle X\rangle\mathbb 1)`$; Steps 5–8 use this form.
- **I5: Accepted and fixed in Step 8, part 4.** The bound of one level, $`c_k=\tau_kd_0`$, is derived from the velocity operator, (7.45), and set against the row-sum bound of the complete body contract.
- **I6: Accepted and fixed in Step 8, parts 2 and 4.** The expansions in $`v`$ are expansions about $`p_0=0`$ with $`\lvert p_0\rvert\ll p_c`$; the exact $`p_0`$-dependent forms are kept, the value near $`p_0=\tfrac\pi2`$ is stated, and (7.17) shows the omitted orders.

## Setup and assumptions

- **Setting (question.md, assumptions of this package, M8, M9).** One body $`b`$ of the class $`\mathcal C_{\rm lev}`$ with linear level profiles ($`M_k,G_k,\mathcal F_k,g_{\zeta,k},V_k,\tau_k`$), a medium $`c`$ with $`K_x=\kappa xX`$, no field object; $`\lambda\ge0`$; infinite chain as the limit of long chains. Starts: branch starts $`B_{k,\sigma}[g]`$ and level-superposed starts $`\Phi_\sigma[\alpha,g]`$, times $`\chi`$.
- **Effective blocks and the record term.** The level blocks $`C^{(k)}`$ are those of the effective body contract (8.19) of 04-ilang-time/08-maximal-speed: $`\mathcal F_k=\mathcal F^{\rm body}_k-\kappa\langle X\rangle`$. The total contract is therefore $`C=\sum_k\bigl(C^{(k)}\otimes\mathbb 1_c+\kappa\hat x\otimes(X-\langle X\rangle\mathbb 1_c)\bigr)\otimes\lvert f_k\rangle\langle f_k\rvert`$; the mean record term is counted once, in $`C^{(k)}`$. In (4.1), $`p^{[\xi]}`$ belongs to the plain gradients $`\mathcal F^{\rm body}_k-\kappa\xi=\mathcal F_k-\varepsilon_\xi`$.
- **Inputs, as quoted.** (5.5), (5.6), (5.11) of 04-ilang-time/05-moving-clock; (8.1), (8.19), (8.20) of 04-ilang-time/08-maximal-speed; (17.15) of 03-ilang-space/17-motion; (3.2), (3.23), (3.36) of 03-clock-and-fall; (4.1), (4.2), (4.5), (4.7), (4.10), (4.11), (4.16), (4.17), (4.19)–(4.25) of 04-branch-fall.
- **Notation.** $`\sigma=\pm1`$; $`w_\xi:=\lVert Q_\xi\chi\rVert^2`$, $`\varepsilon_\xi:=\kappa(\xi-\langle X\rangle)`$, so $`\sum_\xi w_\xi\varepsilon_\xi=0`$, $`\sum_\xi w_\xi\varepsilon_\xi^2=\kappa^2\sigma_X^2`$, $`\sum_\xi w_\xi\varepsilon_\xi^3=\kappa^3\mu_3`$, $`\mu_3:=\langle(X-\langle X\rangle)^3\rangle`$. Inside one level: $`\omega,\theta`$ of (5.6) of 04-ilang-time/05-moving-clock with $`\tau\to\tau_k`$, $`\mu_k\to M_k`$; a prime is $`\partial_p`$; $`\hat x=i\partial_p`$ on plane-wave amplitudes. $`\nu_k:=\omega_k''(0)=\tau_k^2/M_k`$, $`t_k:=\tau_k^2/M_k^2`$, $`p_c:=\min(1,M_k/\tau_k)`$ (for a pair of levels the smaller value). $`\mathrm{Var}_\alpha(y):=\sum_k\lvert\alpha_k\rvert^2\bigl(y_k-\sum_j\lvert\alpha_j\rvert^2y_j\bigr)^2`$.
- **Facts used.** $`\langle\beta_{k,\sigma}\vert\sigma_3\vert\beta_{k,\sigma}\rangle=\sigma M_k/\omega_k`$, $`\langle\beta_{k,\sigma}\vert\sigma_1\vert\beta_{k,\sigma}\rangle=-\sigma\tau_k\sin p/\omega_k`$; $`\omega\omega'=\tfrac12\tau^2\sin2p`$, hence $`\omega''(0)=\tau^2/M`$, $`\omega'''=-\omega'(4+3\omega''/\omega)`$, $`\omega''''(0)=-\nu(4+3t)`$; $`\theta'=-\tau M\cos p/\omega^2`$, $`\lvert\theta'\rvert\le\tau/M`$; at $`p=0`$: $`\theta'=-\tau/M`$, $`\theta''=0`$, $`\theta'''=\tfrac\tau M(1+2t)`$, $`(\omega\theta')''=\tau(1+t)`$.
- **Level offsets.** $`V_k\mathbb 1`$ commutes with $`C^{(k)}`$ and multiplies the level component $`k`$ by $`e^{-iV_k\lambda}`$. For a start in one level this is a common phase (1.2), so every result quoted from 04-branch-fall holds for any $`V_k`$. In a level-superposed start the offsets enter only the phases of the coherences (Step 5), never $`p_x`$ or $`\lvert\Gamma_{kk'}\rvert`$.
- **Regimes (A13).** "First order in the gradients" as in question.md. Record results: Taylor order in $`\kappa`$ at fixed $`\lambda`$, start and chain; the range on which a term dominates is stated with it. Status words: *exact* (an identity), *bound* (an exact inequality), *order estimate* (not a bound; the calculation of its scaling is given with it).

## Derivation

### Step 1. Item 1(a),(b): position statistics of a level-superposed start

1. *Exact mixture.* The total contract of the Setup is block-diagonal in the level, so $`\Psi(\lambda)=\sum_k\alpha_k\,\Psi^{(k)}(\lambda)\otimes\lvert f_k\rangle`$ with $`\Psi^{(k)}(\lambda)`$ the evolved position–branch–medium vector of $`B_{k,\sigma}[g]\otimes\chi`$. A reading of the position is a partition by $`x`$ (A4); it sums over the clock label, and $`\langle f_{k'}\vert f_k\rangle=\delta_{kk'}`$ removes all cross terms (witness rule (1.7) with the clock label as companion). Hence
```math
p_x(\lambda)=\sum_k\lvert\alpha_k\rvert^2\,p^{(k)}_x(\lambda),\qquad\bar x_{\rm lab}(\lambda)=\sum_k\lvert\alpha_k\rvert^2\,\bar x_k(\lambda),
\qquad\text{(7.1)}
```
with $`p^{(k)}_x`$, $`\bar x_k`$ those of $`B_{k,\sigma}[g]`$. **Exact** in the gradients and in $`\kappa`$, for every $`\lambda`$, chain, $`g`$, $`\alpha`$, $`\chi`$. It rests only on the conservation of the level and on the orthonormality of the $`\lvert f_k\rangle`$; it does not depend on how the mean record term is assigned. Every reading of the position alone is that of the mixture of single-level starts with weights $`\lvert\alpha_k\rvert^2`$; the phases of $`\alpha`$ and the $`V_k`$ do not enter.
2. *Drift acceleration.* (7.1) is linear in the single-level quantities, so (4.10) and (4.11) apply term by term, in the same order of limits (first order in the gradients of all levels with $`\alpha_k\neq0`$ at fixed $`\lambda`$, start, chain; long chain; $`\Lambda\to\infty`$; $`\delta p\to0`$):
```math
\Bigl\lvert\overline{a^{(1)}}-\sum_k\lvert\alpha_k\rvert^2\langle a_{k,\sigma}\rangle_g\Bigr\rvert\le\sum_k\lvert\alpha_k\rvert^2\frac{2\tau_k}{M_k\Lambda}\mathsf b_k\Bigl(X_g+\frac{\tau_k}{2M_k}\Bigr),\qquad a_{\rm drift}[\alpha]=\sum_k\lvert\alpha_k\rvert^2\,a_{k,\sigma}(p_0).
\qquad\text{(7.2)}
```
Taking $`\alpha_k=\delta_{kk_0}`$ for each $`k_0`$: $`a_{\rm drift}[\alpha]`$ is the same for all $`\alpha`$ **iff** $`a_{k,\sigma}(p_0)`$ does not depend on $`k`$. At rest this is line 1 ($`\sigma=+`$) or line 2 ($`\sigma=-`$) of (4.19), unchanged: a superposition of levels adds and removes no condition.
3. *What position readings distinguish.* If $`a_{k,\sigma}(p_0)`$ is level-independent, the drift acceleration of $`\Phi_\sigma[\alpha,g]`$, in the limits of (7.2), is that of one level and carries no trace of $`\alpha`$; at finite spread and finite window the averages $`\langle a_{k,\sigma}\rangle_g`$, the bounded rests of (4.7) and, for $`p_0\neq0`$, the velocities of Step 3 can still depend on the level. If not, (i) the mean acceleration (7.2) depends on $`\lvert\alpha_k\rvert^2`$, and (ii) $`p_x`$ is a mixture of components that separate, so the variance of the position exceeds the weighted mean of the single-level variances by the between-level variance (7.3). A body in one level has neither.

### Step 2. Item 1(c): variance of the first-order displacements, start at rest

By (4.7) the first-order velocity of level $`k`$ is $`\lambda\langle a_{k,\sigma}\rangle_g+\rho_k(\lambda)`$ with $`\sup_{\lambda\ge0}\lvert\rho_k\rvert=:r_k<\infty`$; integrating, $`\bar x^{(1)}_k=\tfrac12\lambda^2\langle a_{k,\sigma}\rangle_g+O(\lambda)`$, the rest bounded by $`r_k\lambda`$. With $`r:=\max_kr_k`$ and $`\mathrm{Var}(A+B)-\mathrm{Var}(A)=2\mathrm{Cov}(A,B)+\mathrm{Var}(B)`$:
```math
D(\lambda):=\mathrm{Var}_\alpha\bigl(\bar x^{(1)}\bigr)=\frac{\lambda^4}{4}\mathrm{Var}_\alpha\bigl(\langle a_{\cdot,\sigma}\rangle_g\bigr)+E(\lambda),\quad\lvert E\rvert\le r\lambda^3\sqrt{\mathrm{Var}_\alpha(\langle a_{\cdot,\sigma}\rangle_g)}+r^2\lambda^2;\qquad\lim_{\delta p\to0}\mathrm{Var}_\alpha\bigl(\langle a_{\cdot,\sigma}\rangle_g\bigr)=\mathrm{Var}_\alpha\bigl(a_{\cdot,\sigma}(0)\bigr).
\qquad\text{(7.3)}
```
Order of limits: first order in the gradients at fixed $`\lambda`$, start, chain; long chain; the $`\lambda^4`$ part dominates for $`\lambda\gg r/\sqrt{\mathrm{Var}_\alpha}`$ at fixed $`g`$. The limit $`\delta p\to0`$ in (7.3) is a limit of the **coefficient** of $`\lambda^4`$, for every sequence of starts at rest with $`\delta p\to0`$; it uses only the mean $`0`$ and the variance $`\delta p^2`$ of the label weight (error $`\le\tfrac12\sup\lvert a''_{k,\sigma}\rvert\delta p^2`$ per level, (4.11)). It is not a limit of $`D`$ at fixed $`\lambda`$: $`r`$ depends on $`g`$. $`D`$ is of second order in the gradients. For $`\lvert\alpha_k\rvert^2=1/N`$, with (4.25), $`M_k=m+d_k`$ and $`\mathcal V_N:=\frac1N\sum_kM_k^{-2}-\bigl(\frac1N\sum_kM_k^{-1}\bigr)^2>0`$ (for $`N=2`$: $`\mathcal V_2=\tfrac14\bigl(\tfrac1{M_0}-\tfrac1{M_1}\bigr)^2`$):
```math
\begin{array}{l|c|c|c|c|c}
\text{variant}&\text{(a)}&\text{(b1)}&\text{(b2)}&\text{(c)}&\text{(f)}\\\hline
\lim_{\delta p\to0}\ \lambda^4\text{-part of }D&0&\tfrac14\lambda^4\tau^4g^2m^2\,\mathcal V_N&\tfrac14\lambda^4\tau^4g^2m^2\,\mathcal V_N&0&\tfrac14\lambda^4\tau^4g^2c_{\rm f}^2\,\mathcal V_N
\end{array}
\qquad\text{(7.4)}
```
((b2): $`d_k/M_k=1-m/M_k`$; (f): both branches.) In (a), (c) the coefficient of $`\lambda^4`$ is, by (4.11), at most $`\tfrac1{16}\max_k\sup_p\lvert a''_{k,\sigma}\rvert^2\,\delta p^4`$ for every start at rest, and vanishes in the sharp-label limit; what remains is $`E`$. Control: (a) against (b1).

### Step 3. Item 1(d): velocities at $`p_0\neq0`$

By (4.5), exactly at zero gradients and for every smooth $`g`$ of any width, the level component $`k`$ has the constant velocity $`v_k=\sigma\langle\omega_k'\rangle_g`$. For a start concentrated at $`p_0`$ with the spread $`\delta p`$, Taylor's formula for $`\omega_k'`$ on the arc $`(p_0-\pi,p_0+\pi]`$ gives, using only the mean $`p_0`$ and the variance $`\delta p^2`$ of the label weight,
```math
\bigl\lvert v_k-\sigma\,\omega_k'(p_0)\bigr\rvert\le\tfrac12\sup_p\lvert\omega_k'''\rvert\,\delta p^2\ \ (\text{exact}),\qquad v_k\neq v_{k'}\ \ \text{whenever}\ \ \delta p^2<\delta p_{*}^2:=\frac{2\,\lvert\omega_k'(p_0)-\omega_{k'}'(p_0)\rvert}{\sup_p\lvert\omega_k'''\rvert+\sup_p\lvert\omega_{k'}'''\rvert}.
\qquad\text{(7.27)}
```
Hence, for every sequence of starts concentrated at $`p_0`$ with $`\delta p\to0`$,
```math
\lim_{\delta p\to0}v_k=\sigma\,\omega_k'(p_0)=\sigma\,\frac{\tau_k^2\sin p_0\cos p_0}{\sqrt{M_k^2+\tau_k^2\sin^2p_0}};\qquad\omega_k'(p_0)=\omega_{k'}'(p_0)\ (\sin2p_0\neq0)\iff\frac{\tau_k^4}{M_k^2+\tau_k^2\sin^2p_0}=\frac{\tau_{k'}^4}{M_{k'}^2+\tau_{k'}^2\sin^2p_0}.
\qquad\text{(7.5)}
```
*Can a start of this class have level components with equal velocities?*
- *Starts of finite width:* **yes**, in every member of $`\mathcal C_{\rm lev}`$, the class $`\mathcal C`$ included. Example: $`\lvert g(p)\rvert^2=1+\epsilon\cos(p-p_0)`$, $`0<\lvert\epsilon\rvert<1`$, is normalized and has the mean $`p_0`$ on the arc. Every $`\omega_k'`$ has the period $`\pi`$ and the mean zero, so it contains only even harmonics and $`\langle\omega_k'\rangle_g=0`$: all level components have the velocity zero, also for $`\sin2p_0\neq0`$. The spread of this start is of order one ($`\delta p^2=\pi^2/3-2\epsilon`$).
- *Sharp label, class $`\mathcal C`$* ($`\tau_k=\tau`$, $`M_k`$ strictly increasing): the sharp-label velocities $`\sigma\omega_k'(p_0)`$ are strictly ordered for $`\sin2p_0\neq0`$. So **no** in the following sense: for $`p_0\notin\{0,\pm\tfrac\pi2,\pi\}`$ and two levels $`k\neq k'`$, no start concentrated at $`p_0`$ with $`\delta p<\delta p_*`$ of (7.27) has equal velocities in these levels; the components then separate as $`\lvert v_k-v_{k'}\rvert\lambda`$ already at zeroth order in the gradients.
- *Sharp label, $`\mathcal C_{\rm lev}`$:* for two levels with different data, $`(\tau_k,M_k)\neq(\tau_{k'},M_{k'})`$, equality of the sharp-label velocities at one $`p_0`$ with $`\sin2p_0\neq0`$ is one condition on $`(\tau_k,M_k,\tau_{k'},M_{k'})`$ and needs $`\tau_k\neq\tau_{k'}`$ (for $`\tau_k=\tau_{k'}`$ the condition of (7.5) reduces to $`M_k=M_{k'}`$). For two levels with equal data the velocities are equal for every $`g`$, and equality at all $`p_0`$ holds iff the data are equal (compare the coefficients of $`\sin^2p_0`$).

### Step 4. Item 1(e): rate of the mean label

1. *Exact transport of the label weight.* On the infinite chain, (4.2) gives for the amplitudes $`c(p,\lambda)\in\mathbb C^2`$ of a level component $`i\partial_\lambda c=C_0(p)c+\tfrac i2\bigl(\partial_p(Bc)+B\partial_pc\bigr)`$. $`C_0`$ and $`B`$ are Hermitian, so $`\partial_\lambda(c^\dagger c)=\partial_p(c^\dagger Bc)`$. Multiplying by $`p`$ and integrating over the arc $`(p_0-\pi,p_0+\pi]`$ by parts, for a normalized component:
```math
\frac{\mathrm d\bar p_k}{\mathrm d\lambda}=-\int\frac{\mathrm dp}{2\pi}\,c^\dagger B_k\,c+\bigl(c^\dagger B_kc\bigr)(p_0+\pi)\qquad(\text{exact in the gradients}).
\qquad\text{(7.6)}
```
The last term is the weight crossing the cut, bounded by $`\lVert B_k\rVert\,\lVert c(p_0+\pi)\rVert^2`$.
2. *First order.* Insert the zeroth-order amplitudes $`c=g\,e^{-i(V_k+\sigma\omega_k)\lambda}\beta_{k,\sigma}`$ (the correction to $`c`$ contributes at second order). The integrand is $`\lambda`$-independent, so no window is needed. With the facts above and $`B_k=-g_{\zeta,k}\tau_k\sin p\,\sigma_1+G_k\sigma_3-\mathcal F_k`$, for every smooth $`g`$:
```math
\frac{\mathrm d\bar p_k}{\mathrm d\lambda}\Big\vert_{1}=\langle\pi_{k,\sigma}\rangle_g-\lvert g(p_0+\pi)\rvert^2\pi_{k,\sigma}(p_0+\pi),\quad\pi_{k,\sigma}(p):=\mathcal F_k-\sigma\frac{G_kM_k+g_{\zeta,k}\tau_k^2\sin^2p}{\omega_k(p)};\qquad\lim_{\substack{\delta p\to0\\ \lvert g(\pi)\rvert^2\to0}}=\pi_{k,\sigma}(0)=\mathcal F_k-\sigma G_k\ \ (p_0=0).
\qquad\text{(7.7)}
```
The weight at the cut does not vanish with the spread: the variance controls the integrated weight, not the value $`\lvert g(p_0+\pi)\rvert^2`$, which can be any number $`\ge0`$. For a start at rest, $`\pi_{k,\sigma}(\pi)=\pi_{k,\sigma}(0)`$ and Taylor's formula for $`\pi_{k,\sigma}`$ give, using only the mean $`0`$ and the variance $`\delta p^2`$:
```math
\Bigl\lvert\frac{\mathrm d\bar p_k}{\mathrm d\lambda}\Big\vert_{1}-\bigl(1-\lvert g(\pi)\rvert^2\bigr)\bigl(\mathcal F_k-\sigma G_k\bigr)\Bigr\rvert\le\tfrac12\sup_p\lvert\pi_{k,\sigma}''\rvert\,\delta p^2\qquad(\text{exact, every start at rest}).
\qquad\text{(7.28)}
```
Order of limits: first order in the gradients at fixed $`\lambda`$ and start; long chain; then a sequence of starts at rest with $`\delta p\to0`$ and $`\lvert g(\pi)\rvert^2\to c_{\rm cut}\in[0,\infty)`$. The limiting rate is $`(1-c_{\rm cut})(\mathcal F_k-\sigma G_k)`$; it is $`\mathcal F_k-\sigma G_k`$ **only for $`c_{\rm cut}=0`$**. The factor $`1-c_{\rm cut}`$ is the same for all levels, because $`\Phi_\sigma[\alpha,g]`$ has the same $`g`$ in every level. With (4.16), $`a_{k,\sigma}(0)=\sigma\,\nu_k\,\pi_{k,\sigma}(0)`$ for every start; the drift acceleration (4.11) has no cut term.
3. *Equivalences.* For sequences of starts at rest with $`\delta p\to0`$ and $`c_{\rm cut}\neq1`$: the limiting rate is the same for all levels **iff** $`\mathcal F_k-\sigma G_k`$ does not depend on $`k`$. Together with $`a_{k,\sigma}(0)=a\neq0`$ for all $`k`$ this holds **iff** in addition $`\tau_k^2/M_k`$ does not depend on $`k`$. In the class $`\mathcal C`$ the limiting rate is level-independent iff $`g_\eta=0`$, and then $`a_{k,\sigma}(0)=\tau^2(\sigma\mathcal F-mg_m)/M_k`$ is level-independent only if it is zero: **no**, in $`\mathcal C`$ the two cannot hold together with $`a\neq0`$ (variant (a): $`\pi_{k,\sigma}(0)=-\sigma gM_k`$). In $`\mathcal C_{\rm lev}`$ they can, at the price $`\tau_k^2\propto M_k`$. For sequences with $`c_{\rm cut}=1`$ the limiting rate of the arc mean is zero in every level, whatever the gradients, and then holds trivially together with any level-independent $`a`$.

### Step 5. Item 1(f): clock readings and coherences

1. *Formula.* The reading of the clock label is the partition by $`a`$; with $`\langle a\vert f_k\rangle=N^{-1/2}e^{2\pi ika/N}`$ and $`\Psi=\sum_k\psi_k\otimes\lvert f_k\rangle`$:
```math
P(a;\lambda)=\frac1N\sum_{k,k'}\alpha_{k'}^{*}\alpha_k\,\Gamma_{kk'}(\lambda)\,e^{2\pi i(k-k')a/N},\qquad\Gamma_{kk}=1,\quad\Gamma_{k'k}=\Gamma_{kk'}^{*},\quad\lvert\Gamma_{kk'}\rvert\le1.
\qquad\text{(7.8)}
```
This is exact if $`\psi_k`$ includes the medium, and then $`\Gamma_{kk'}=\sum_\xi w_\xi\Gamma^{[\xi]}_{kk'}`$ as in (4.1) (plain gradients $`\mathcal F_k-\varepsilon_\xi`$ in every level). At leading order in $`\kappa`$ ($`\kappa\to0`$ at fixed $`\lambda`$, chain, start) $`\Gamma_{kk'}`$ is that of the effective body contract, used below.
2. *Zero gradients.* From (5.6) of 04-ilang-time/05-moving-clock, $`\langle\beta_{k',\sigma}\vert\beta_{k,\sigma}\rangle=\cos\tfrac{\theta_k-\theta_{k'}}2=:F`$, so
```math
\Gamma^{(0)}_{kk'}(\lambda)=e^{-i(V_k-V_{k'})\lambda}\Bigl\langle\cos\tfrac{\theta_k-\theta_{k'}}2\,e^{-i\sigma(\omega_k-\omega_{k'})\lambda}\Bigr\rangle_g;\qquad g(-p)=g(p)\ \Longrightarrow\ \Gamma_{kk'}[\text{gradients}]=\Gamma_{kk'}[-\text{gradients}]\ \ \text{exactly}.
\qquad\text{(7.9)}
```
Proof of the second statement: let $`\mathsf P`$ be the reflection $`x\to-x`$ times $`\sigma_3`$. By (4.2), $`\mathsf PC_0\mathsf P^{-1}=C_0`$ and $`\mathsf PC_1\mathsf P^{-1}=-C_1`$ in every level; $`\sigma_3\beta_{k,\sigma}(-p)=\sigma\beta_{k,\sigma}(p)`$ gives $`\mathsf PB_{k,\sigma}[g]=\sigma B_{k,\sigma}[g^-]`$ with $`g^-(p):=g(-p)`$, the same sign in both levels; $`\mathsf P`$ is unitary. For every smooth $`g`$, every $`p_0`$ and $`\lambda`$, exactly:
```math
\Gamma_{kk'}\bigl[g;\,\text{gradients}\bigr]=\Gamma_{kk'}\bigl[g^-;\,-\text{gradients}\bigr].
\qquad\text{(7.23)}
```
Hence for every start of **definite parity**, $`g^-=\pm g`$ (both are starts at rest), $`\lvert\Gamma_{kk'}\rvert`$ is exactly even in the gradients.
3. *Exact expansion of $`\lvert\Gamma_{kk'}\rvert`$ to second order.* Class: every smooth $`g`$, every $`p_0`$, every $`\lambda\ge0`$; effective body contract; Taylor expansion in the gradients of the two levels at fixed $`\lambda`$ and start, infinite chain. Let $`\varphi_k:=B_{k,\sigma}[g]`$ (position and branch labels), $`U_{0k}(\lambda):=e^{-iC_0^{(k)}\lambda}`$, $`D_k:=U_{0k}^\dagger e^{-iC^{(k)}\lambda}`$ with $`C^{(k)}`$ without $`V_k`$, $`Z:=U_{0k'}^\dagger U_{0k}`$, and
```math
\Omega_k:=\int_0^\lambda U_{0k}(s)^\dagger C_1^{(k)}U_{0k}(s)\,\mathrm ds,\qquad\Theta_1:=\Omega_k-Z^\dagger\Omega_{k'}Z,\qquad e^{-i(\Theta_1+\Theta_2+\dots)}:=\bigl(Z^\dagger D_{k'}^\dagger Z\bigr)D_k ,
```
with $`\Theta_n`$ self-adjoint of order $`n`$ (the right side is unitary; $`D_k=\exp[-i\Omega_k-\tfrac12\int_0^\lambda\!\mathrm ds\int_0^s\!\mathrm ds'\,[\tilde C_1(s),\tilde C_1(s')]+\dots]`$, and $`\Theta_2`$ follows by the Baker–Campbell–Hausdorff formula). Then $`\Gamma_{kk'}=e^{-i(V_k-V_{k'})\lambda}\langle Z^\dagger\varphi_{k'}\vert e^{-i\Theta}\vert\varphi_k\rangle`$. Split $`Z^\dagger\varphi_{k'}=\gamma_0^{*}\varphi_k+\chi_\perp`$ with $`\gamma_0:=\langle\varphi_{k'}\vert Z\vert\varphi_k\rangle=e^{i(V_k-V_{k'})\lambda}\Gamma^{(0)}_{kk'}`$, $`\chi_\perp\perp\varphi_k`$, $`\lVert\chi_\perp\rVert^2=1-\lvert\Gamma^{(0)}_{kk'}\rvert^2`$. With $`\langle\cdot\rangle:=\langle\varphi_k\vert\cdot\vert\varphi_k\rangle`$, $`\delta\Theta_1:=\Theta_1-\langle\Theta_1\rangle`$, and $`\lvert1+z_1+z_2\rvert=1+\mathrm{Re}z_1+\mathrm{Re}z_2+\tfrac12(\mathrm{Im}z_1)^2+O(3)`$, the terms with $`\langle\Theta_1\rangle`$ and $`\langle\Theta_2\rangle`$ cancel (they are phases), and where $`\Gamma^{(0)}_{kk'}(\lambda)\neq0`$:
```math
\begin{aligned}
\frac{\lvert\Gamma_{kk'}\rvert}{\lvert\Gamma^{(0)}_{kk'}\rvert}&=1+\mathrm{Re}\epsilon_1+Q_2+O(\text{grad}^3),\qquad Q_2:=-\tfrac12\mathcal V+\tfrac12(\mathrm{Im}\epsilon_1)^2+\mathrm{Re}\epsilon_2,\qquad\mathcal V:=\bigl\lVert\delta\Theta_1\varphi_k\bigr\rVert^2,\\
\epsilon_1&:=-\frac{i}{\gamma_0}\langle\chi_\perp\vert\Theta_1\varphi_k\rangle,\qquad\epsilon_2:=-\frac{1}{\gamma_0}\bigl\langle\chi_\perp\big\vert\bigl(i\Theta_2+\tfrac12\delta\Theta_1^2\bigr)\varphi_k\bigr\rangle,\qquad\lvert\epsilon_1\rvert\le\eta_0\,\mathcal V^{1/2},\quad\eta_0:=\frac{\sqrt{1-\lvert\Gamma^{(0)}_{kk'}\rvert^2}}{\lvert\Gamma^{(0)}_{kk'}\rvert}.
\end{aligned}
\qquad\text{(7.35)}
```
(7.35) is exact; the bound is the Cauchy–Schwarz inequality with $`\chi_\perp\perp\varphi_k`$; likewise $`\lvert\epsilon_2\rvert\le\eta_0\bigl(\mathrm{Var}(\Theta_2)^{1/2}+\tfrac12\lVert\delta\Theta_1^2\varphi_k\rVert\bigr)`$. $`\mathrm{Re}\epsilon_1=\mathrm{Re}(\Gamma^{(1)}_{kk'}/\Gamma^{(0)}_{kk'})`$ is the first-order term, given in closed form in part 4. The first-order term is bounded by $`\eta_0\mathcal V^{1/2}`$: it exists only because $`\lvert\Gamma^{(0)}_{kk'}\rvert<1`$. **The order of the first deviation**, for a pair $`k\neq k'`$ and a given $`\lambda`$, is therefore, exactly:
```math
\begin{array}{l|l|l}
\text{case}&\text{defining condition}&\text{first deviation of }\lvert\Gamma_{kk'}\rvert\\\hline
\text{(O0)}&(\tau,M,G,\mathcal F,g_\zeta)\text{ equal in the two levels}&\text{none, at any order: }\lvert\Gamma_{kk'}\rvert=1\\
\text{(OZ)}&\Gamma^{(0)}_{kk'}(\lambda)=0&\lvert\Gamma_{kk'}\rvert=\lvert\Gamma^{(1)}_{kk'}\rvert+O(\text{grad}^2)\text{: degree one, not linear}\\
\text{(O1)}&\Gamma^{(0)}_{kk'}\neq0,\ \mathrm{Re}\epsilon_1\neq0&\text{first order, the term }\mathrm{Re}\epsilon_1\text{ of (7.24)}\\
\text{(O2)}&\Gamma^{(0)}_{kk'}\neq0,\ \mathrm{Re}\epsilon_1=0,\ Q_2\neq0&\text{second order, the term }Q_2\text{ of (7.35)}\\
\text{(O3)}&\Gamma^{(0)}_{kk'}\neq0,\ \mathrm{Re}\epsilon_1=Q_2=0&\text{third order or higher (out of scope)}
\end{array}
\qquad\text{(7.36)}
```
(O0): the two level blocks differ by a constant. Sufficient for $`\mathrm{Re}\epsilon_1=0`$ at all $`\lambda`$: definite parity (7.23), or equal data $`(\tau_k,M_k)=(\tau_{k'},M_{k'})`$ (then $`\eta_0=0`$). Parts 5 and 6 determine in which of (O1)–(O3) a start at rest lies and give the leading term.
4. *First-order term for every $`g`$ (exact).* Notation: $`\rho:=\lvert g\rvert^2`$; $`j:=\mathrm{Im}(g^{*}g')`$ ($`\langle\hat x\rangle_g=-\int\frac{\mathrm dp}{2\pi}j`$); $`\Delta\omega:=\omega_k-\omega_{k'}`$; $`\pi_k:=\pi_{k,\sigma}(p)`$ of (7.7); $`\lVert f\rVert^2:=\int\frac{\mathrm dp}{2\pi}\lvert f\rvert^2`$. First-order perturbation theory in $`C_1`$ of (4.2), with $`C_1\psi=\tfrac i2(B_k'\psi+2B_k\psi')`$, $`\beta_{k,\sigma}'=\tfrac\sigma2\theta_k'\beta_{k,-\sigma}`$, $`\langle\beta_{k,\sigma}\vert B_k\vert\beta_{k,\sigma}\rangle=-\pi_k`$, gives $`-i\Omega_k\varphi_k=a_k\beta_{k,\sigma}+a_{k,\perp}\beta_{k,-\sigma}`$ with $`a_k=-\lambda\bigl(\pi_kg'+\tfrac12\pi_k'g\bigr)+\tfrac{i\sigma}2\lambda^2\omega_k'\pi_k\,g`$ (the transport of Step 4; it conserves the norm) and the inter-branch amplitude
```math
\begin{aligned}
a_{k,\perp}&=\tfrac12\bigl(b_{0,k}\,g+2\,b_{\perp,k}\,g'\bigr)I_{0,k}-i\sigma\,\omega_k'\,b_{\perp,k}\,g\,I_{1,k},\qquad I_{n,k}:=\int_0^\lambda s^n e^{-2i\sigma\omega_ks}\,\mathrm ds,\quad I_{1,k}=\tfrac{i\sigma}{2\omega_k}\bigl(\lambda e^{-2i\sigma\omega_k\lambda}-I_{0,k}\bigr),\\
b_{\perp,k}&:=\langle\beta_{k,-\sigma}\vert B_k\vert\beta_{k,\sigma}\rangle=\frac{\tau_k\sin p}{\omega_k}\bigl(G_k-M_kg_{\zeta,k}\bigr),\qquad b_{0,k}:=-g_{\zeta,k}\tau_k\cos p\,\frac{M_k}{\omega_k}-\sigma\,\theta_k'\,\pi_{k,-\sigma},\\
\lVert a_{k,\perp}\rVert&\le A_{k,\perp}(\lambda):=\frac{\tau_k\mathsf b_k}{2M_k^2}\Bigl(2+\frac{\tau_k}{M_k}+2\lVert\sin p\;g'\rVert\Bigr)+\frac{\tau_k^3\mathsf b_k}{2M_k^3}\Bigl(\lambda+\frac1{M_k}\Bigr)\langle\sin^4p\rangle_g^{1/2}\qquad(\text{bound}).
\end{aligned}
\qquad\text{(7.29)}
```
(The bound uses $`\lvert I_{0,k}\rvert\le1/\omega_k`$, $`\lvert I_{1,k}\rvert\le\lambda/(2\omega_k)+1/(2\omega_k^2)`$, $`\omega_k\ge M_k`$, $`\lvert b_{\perp,k}\rvert\le\tfrac{\tau_k}{M_k}\mathsf b_k\lvert\sin p\rvert`$, $`\lvert\omega_k'b_{\perp,k}\rvert\le\tfrac{\tau_k^3}{M_k^2}\mathsf b_k\sin^2p`$, $`\lvert b_{0,k}\rvert\le\tfrac{\tau_k}{M_k}\mathsf b_k(2+\tfrac{\tau_k}{M_k})`$.) Inserting in $`\Gamma_{kk'}=\int\frac{\mathrm dp}{2\pi}c_{k'}^\dagger c_k`$ and integrating the term with $`\rho'`$ by parts on the circle:
```math
\Gamma^{(1)}_{kk'}=e^{-i(V_k-V_{k'})\lambda}\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\,e^{-i\sigma\Delta\omega\lambda}\Bigl\{\rho\Bigl[\tfrac\lambda2(\pi_k+\pi_{k'})F'+\tfrac{i\sigma}2\lambda^2\bigl(\omega_{k'}'\pi_k-\omega_k'\pi_{k'}\bigr)F\Bigr]-i\lambda(\pi_k-\pi_{k'})F\,j\Bigr\}+\Gamma^{(1),\perp}_{kk'},\qquad\Bigl(\frac{\lvert\Gamma_{kk'}\rvert}{\lvert\Gamma^{(0)}_{kk'}\rvert}\Bigr)_{1}=\mathrm{Re}\frac{\Gamma^{(1)}_{kk'}}{\Gamma^{(0)}_{kk'}}\ \ \text{where }\Gamma^{(0)}_{kk'}(\lambda)\neq0.
\qquad\text{(7.24)}
```
With $`\langle\beta_{k',\sigma}\vert\beta_{k,-\sigma}\rangle=-\sigma\sin\tfrac{\theta_k-\theta_{k'}}2=-\langle\beta_{k',-\sigma}\vert\beta_{k,\sigma}\rangle`$ the inter-branch part is
```math
\Gamma^{(1),\perp}_{kk'}=-\sigma\,e^{-i(V_k-V_{k'})\lambda}\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\,\sin\tfrac{\theta_k-\theta_{k'}}2\Bigl[g^{*}a_{k,\perp}\,e^{i\sigma(\omega_k+\omega_{k'})\lambda}-a_{k',\perp}^{*}\,g\,e^{-i\sigma(\omega_k+\omega_{k'})\lambda}\Bigr],\qquad\bigl\lvert\Gamma^{(1),\perp}_{kk'}\bigr\rvert\le\tfrac12\Bigl(\frac{\tau_k}{M_k}+\frac{\tau_{k'}}{M_{k'}}\Bigr)\langle\sin^2p\rangle_g^{1/2}\bigl(A_{k,\perp}+A_{k',\perp}\bigr).
\qquad\text{(7.30)}
```
(7.24) with (7.29), (7.30) is the complete first-order term, exact for every smooth $`g`$, $`p_0`$ and $`\lambda\ge0`$. A sufficient condition for $`\Gamma^{(0)}_{kk'}\neq0`$, for a start at rest, from $`F\cos y\ge F-(1-\cos y)`$, $`1-\cos y\le\lvert y\rvert`$, $`1-F\le\tfrac18(\theta_k-\theta_{k'})^2`$ and Taylor's formula for $`\Delta\omega`$ (mean $`0`$ and variance $`\delta p^2`$ only):
```math
1-\bigl\lvert\Gamma^{(0)}_{kk'}(\lambda)\bigr\rvert\le\epsilon_0(\lambda):=\Bigl[\tfrac12\lambda\sup_p\lvert\omega_k''-\omega_{k'}''\rvert+\tfrac18\Bigl(\frac{\tau_k}{M_k}+\frac{\tau_{k'}}{M_{k'}}\Bigr)^2\Bigr]\delta p^2\qquad(\text{bound, every start at rest}),
\qquad\text{(7.31)}
```
so $`\Gamma^{(0)}_{kk'}\neq0`$ wherever $`\epsilon_0<1`$, and then $`\eta_0\le\sqrt{2\epsilon_0}/(1-\epsilon_0)`$.
5. *Narrow starts at rest: the leading terms.* **Class (N):** starts at rest with a smooth complex $`g`$ of any shape, along a sequence with $`\delta p\to0`$, $`\delta p\ll p_c`$, moments $`\langle\lvert p\rvert^n\rangle_g=O(\delta p^n)`$ for $`n\le6`$, $`\lVert(\hat x-\bar x_g)^2g\rVert=O(\delta x_g^2)`$ and $`\lvert g(\pi)\rvert^2\to c_{\rm cut}\neq1`$; **range (N2):** $`\epsilon_0(\lambda)\ll1`$ (in particular $`\lvert\Delta\nu_{kk'}\rvert\lambda\,\delta p^2\ll1`$, $`\Delta\nu_{kk'}:=\nu_k-\nu_{k'}`$). The start enters through $`\bar x_g:=\langle g\vert\hat x\vert g\rangle`$, $`\delta x_g^2:=X_g^2-\bar x_g^2`$ (the **spread of the start in the position**; the position variance of the level component is $`\delta x_g^2+\tfrac14\langle\theta_k'^2\rangle_g`$, with a level-dependent addition $`\le t_k/4`$), $`C_g:=-\int\frac{\mathrm dp}{2\pi}\,p\,j`$ (the covariance of position and label), $`\langle p^3\rangle_g`$ and $`J_g:=\int\frac{\mathrm dp}{2\pi}(p^2-\delta p^2)\,j`$. With $`u=(\hat x-\bar x_g)g`$, $`w=pg`$ and one integration by parts on the arc, $`\mathrm{Im}\langle u\vert w\rangle=\tfrac12(1-\lvert g(\pi)\rvert^2)`$ and $`\mathrm{Re}\langle u\vert w\rangle=C_g`$, so
```math
\delta x_g^2\,\delta p^2\ \ge\ C_g^2+\tfrac14\bigl(1-\lvert g(\pi)\rvert^2\bigr)^2,\qquad\text{in particular}\quad2\,\delta p\,X_g\ge2\,\delta p\,\delta x_g\ge\bigl\lvert1-\lvert g(\pi)\rvert^2\bigr\rvert\qquad(\text{bound, every start at rest}).
\qquad\text{(7.37)}
```
(For $`g=1`$ both sides vanish.) *Local form.* On the label weight, $`\pi_{k,\sigma}(p)=\pi_k+O(\mathsf b\,p^2/p_c^2)`$ with $`\pi_k:=\mathcal F_k-\sigma G_k`$ from here on, $`\omega_k'=\nu_kp\,(1+O(p^2/p_c^2))`$, $`F=1-O(p^2/p_c^2)`$. To leading order the branch part of part 4 is $`\Omega_k=-\pi_k(\lambda\hat x+\tfrac12\sigma\nu_k\lambda^2\hat p)`$ and $`Z=e^{-\frac i2\sigma\Delta\nu\lambda\hat p^2}`$ up to a phase, operators on $`g`$ with $`[\hat x,\hat p]=i`$. Then $`Z^\dagger\hat xZ=\hat x+\sigma\Delta\nu\lambda\hat p`$ and
```math
\Theta_1=-\bigl(K_{kk'}+\tfrac12\sigma\lambda^2\Delta\nu_{kk'}(\pi_k-\pi_{k'})\,\hat p\bigr),\qquad K_{kk'}:=\lambda\,(\pi_k-\pi_{k'})\,\hat x+\tfrac12\sigma\lambda^2\,\varpi_{kk'}\,\hat p,\qquad\varpi_{kk'}:=\nu_{k'}\pi_k-\nu_k\pi_{k'} ,
```
and $`\Theta_2`$ is a number (commutators of operators linear in $`\hat x,\hat p`$). $`K_{kk'}`$ is the generator of the relative displacement of the two level components: $`\lambda(\pi_k-\pi_{k'})`$ in the label and $`\tfrac12\sigma\lambda^2\varpi_{kk'}`$ in the position at the common label. By (7.35), with $`\mathrm{Var}_g(a\hat x+b\hat p)=a^2\delta x_g^2+2abC_g+b^2\delta p^2`$ and (7.37):
```math
\boxed{\;Q_2\simeq-\tfrac12\mathrm{Var}_g(K_{kk'})=-\Bigl[\tfrac12\lambda^2(\pi_k-\pi_{k'})^2\,\delta x_g^2+\tfrac12\sigma\lambda^3(\pi_k-\pi_{k'})\,\varpi_{kk'}\,C_g+\tfrac18\lambda^4\varpi_{kk'}^2\,\delta p^2\Bigr]\;},\qquad\mathrm{Var}_g(K_{kk'})\ge\bigl(1-\lvert g(\pi)\rvert^2\bigr)^2\max\Bigl\{\frac{\lambda^2(\pi_k-\pi_{k'})^2}{4\,\delta p^2},\ \frac{\lambda^4\varpi_{kk'}^2}{16\,\delta x_g^2}\Bigr\}.
\qquad\text{(7.38)}
```
The lower bound is exact. So for the class (N) the second-order term is **different from zero iff $`(\pi_k-\pi_{k'},\varpi_{kk'})\neq(0,0)`$**, for every shape of $`g`$, starts of definite parity included. It depends on $`\lambda`$ as $`\lambda^2`$, $`\lambda^3`$, $`\lambda^4`$; on the level data through $`\pi_k-\pi_{k'}`$ and $`\varpi_{kk'}`$; on the start through $`\delta x_g^2`$, $`C_g`$ and $`\delta p^2`$: the $`\lambda^2`$ term grows with the spread in the position, the $`\lambda^4`$ term falls with it ($`\delta p\ge\lvert1-c_{\rm cut}\rvert/(2\delta x_g)`$). For the real Gaussian starts (E1), $`\lvert g\rvert^2\propto e^{-p^2/2\delta p^2}`$, $`g`$ real: $`C_g=0`$, $`\delta p=1/(2\delta x)`$, and (7.38) is
```math
1-\frac{\lvert\Gamma_{kk'}\rvert}{\lvert\Gamma^{(0)}_{kk'}\rvert}\simeq\frac{\delta x^2}2\,(\pi_k-\pi_{k'})^2\lambda^2+\frac{\lambda^4}{32\,\delta x^2}\Bigl(\frac{\tau_{k'}^2}{M_{k'}}\pi_k-\frac{\tau_k^2}{M_k}\pi_{k'}\Bigr)^2,\qquad\pi_k=\mathcal F_k-\sigma G_k.
\qquad\text{(7.10)}
```
*First-order term.* In (7.35), $`\chi_\perp\neq0`$ only through $`Z\neq1`$. Expanding (7.24) with $`\Delta\omega=\Delta\omega(0)+\tfrac12\Delta\nu\,p^2+\dots`$: a real weight $`h`$ gives $`\mathrm{Im}\bigl[\int Fe^{-i\sigma\Delta\omega\lambda}h\big/\int Fe^{-i\sigma\Delta\omega\lambda}\rho\bigr]=-\tfrac\sigma2\lambda\Delta\nu\int\frac{\mathrm dp}{2\pi}(p^2-\delta p^2)h`$ at leading order; with $`h=\rho\,\varpi_{kk'}p`$ and $`h=(\pi_k-\pi_{k'})j`$:
```math
\mathrm{Re}\epsilon_1=\Bigl(\frac{\lvert\Gamma_{kk'}\rvert}{\lvert\Gamma^{(0)}_{kk'}\rvert}\Bigr)_{1}\simeq\Delta\nu_{kk'}\Bigl[\tfrac14\lambda^3\,\varpi_{kk'}\,\langle p^3\rangle_g-\tfrac\sigma2\lambda^2\,(\pi_k-\pi_{k'})\,J_g\Bigr]
\qquad\text{(7.25)}
```
(the same follows from $`\Theta_1`$ above: $`\mathrm{Re}\epsilon_1=\tfrac12\sigma\Delta\nu\lambda\,\mathrm{Cov}_g(K_{kk'},\hat p^2)`$). $`J_g=0`$ for real $`g`$; $`\langle p^3\rangle_g=J_g=0`$ for definite parity. Its sign is not fixed. So, in (N), (N2): **(O1)** iff the bracket of (7.25) and $`\Delta\nu_{kk'}`$ are different from zero (a real $`g`$ with a skewed label weight suffices); otherwise **(O2)** iff $`(\pi_k-\pi_{k'},\varpi_{kk'})\neq(0,0)`$. To second order the deviation is $`1-\lvert\Gamma_{kk'}\rvert/\lvert\Gamma^{(0)}_{kk'}\rvert\simeq-(7.25)+\tfrac12\mathrm{Var}_g(K_{kk'})`$; the first-order term is the larger one where $`\mathrm{Var}_g(K_{kk'})^{1/2}\ll\lvert\Delta\nu\rvert\lambda\,\delta p^2`$ times the skewness of the start.
   *What (7.38) and (7.25) neglect (order estimates; $`\tau/M`$, $`\nu`$, $`\mathsf b`$ the larger of the two levels' values; $`\mathcal V_{\max}:=\mathsf b^2(\lambda^2X_g^2+\nu^2\lambda^4\delta p^2)`$ is the largest size of $`\mathrm{Var}_g(K)`$).* (i) *Local form.* The Taylor remainders of $`\pi_{k,\sigma}`$, $`\omega_k'`$, $`F`$ change $`\Theta_1\varphi_k`$ by a vector of norm $`O(\delta p^2/p_c^2)\,\mathcal V_{\max}^{1/2}`$ (moments $`n\le6`$). (ii) *The term $`\tfrac12\sigma\lambda^2\Delta\nu(\pi_k-\pi_{k'})\hat p`$ of $`\Theta_1`$* changes $`\mathcal V^{1/2}`$ by at most $`\tfrac12\lambda^2\lvert\Delta\nu(\pi_k-\pi_{k'})\rvert\delta p\le\lvert\Delta\nu\rvert\lambda\,\delta p^2\mathrm{Var}_g(K)^{1/2}/\lvert1-c_{\rm cut}\rvert`$, by (7.38). (iii) *Inter-branch components of $`\Theta_1\varphi_k`$*, orthogonal to the branch part, so they add to $`\mathcal V`$ in squares: $`ia_{k,\perp}`$ and its counterpart of $`k'`$, of norm $`\le A_{k,\perp}+A_{k',\perp}`$ (bound (7.29)); and the part of $`\varphi_k`$ outside the branch $`\sigma`$ of the level $`k'`$, of norm $`\le\tfrac12(\tfrac{\tau_k}{M_k}+\tfrac{\tau_{k'}}{M_{k'}})\langle\sin^2p\rangle_g^{1/2}\le\tfrac\tau M\delta p`$, on which $`\Omega_{k'}`$ acts as on a start of the other branch: $`O\bigl(\tfrac\tau M\mathsf b\,\lambda\,(\delta p\,X_g+1+\nu\lambda\,\delta p^2)\bigr)`$. (iv) *The terms with $`\chi_\perp`$:* $`\tfrac12(\mathrm{Im}\epsilon_1)^2\le\tfrac12\eta_0^2\mathcal V`$; $`\tfrac12\eta_0\lVert\delta\Theta_1^2\varphi_k\rVert=O(\eta_0\mathcal V_{\max})`$ (fourth moments); and $`\eta_0\mathrm{Var}(\Theta_2)^{1/2}`$, where only the operator part of $`\Theta_2`$ counts: from the $`p`$-dependence inside the branch, $`\Theta_2\ni-\tfrac\sigma{12}\lambda^3\pi_k(\omega_k'\pi_k)'`$ (double integral of $`[\tilde C_1(s),\tilde C_1(s')]=i\sigma(s'-s)\pi_k(\omega_k'\pi_k)'`$), with the fluctuation $`O(\lambda^3\nu\mathsf b^2\delta p^2/p_c^2)`$; and from the second-order inter-branch term $`-\sigma\lambda\,(C_1)_{\sigma,-\sigma}(C_1)_{-\sigma,\sigma}/(2\omega_k)`$, $`(C_1)_{-\sigma,\sigma}=\tfrac i2(b_{0,k}+2b_{\perp,k}\partial_p)`$, with the fluctuation $`O\bigl(\lambda\tfrac{\tau^2\mathsf b^2}{M^3}(1+\delta pX_g)^2\bigr)`$. Together:
```math
\bigl\lvert Q_2+\tfrac12\mathrm{Var}_g(K_{kk'})\bigr\rvert\lesssim\mathcal V_{\max}\Bigl[\frac{\delta p^2}{p_c^2}+\lvert\Delta\nu\rvert\lambda\,\delta p^2+\eta_0\Bigr]+\bigl(A_{k,\perp}+A_{k',\perp}\bigr)^2+\frac{\tau^2\mathsf b^2}{M^2}\lambda^2\bigl(1+\delta pX_g+\nu\lambda\,\delta p^2\bigr)^2+\eta_0\,\lambda\,\mathsf b^2\Bigl[\frac{\nu\lambda^2\delta p^2}{p_c^2}+\frac{\tau^2}{M^3}(1+\delta pX_g)^2\Bigr].
\qquad\text{(7.32)}
```
(7.38) is the leading second-order term where the right side of (7.32) is small against $`\tfrac12\mathrm{Var}_g(K_{kk'})`$. If the gradients and the data of the two levels differ by relative amounts of order one ($`\mathrm{Var}_g(K)\sim\mathcal V_{\max}`$) and $`\delta pX_g=O(1)`$, this is the range (N2) with $`\lambda\gg\tau\,\delta p/M^2`$ (from $`A_\perp^2\sim\tau^2\mathsf b^2/M^4\ll\mathsf b^2\lambda^2/\delta p^2`$; the other terms are then small by $`\delta p\ll p_c`$ and $`\eta_0\ll1`$). For (7.25): the Taylor remainders change its two terms by relative $`O(\delta p^2/p_c^2)`$; the next order of $`e^{-i\sigma\Delta\omega\lambda}`$ is real and enters at relative $`O((\Delta\nu\lambda\delta p^2)^2)`$; the term of (7.24) with $`F'\simeq-\tfrac14(\theta_k'-\theta_{k'}')^2p`$ is $`O(\lambda\mathsf b\,t(1+t)\delta p^3)`$; and $`\lvert\Gamma^{(1),\perp}_{kk'}\rvert`$ has the bound (7.30), with the growing part $`O(\lambda\tfrac{\tau^4\mathsf b}{M^4}\delta p^3)`$. If $`\pi_k-\pi_{k'}`$, $`\varpi_{kk'}`$ are small against $`\mathsf b`$, $`\nu\mathsf b`$, the ranges shrink accordingly; for $`\pi_k=\pi_{k'}`$, $`\varpi_{kk'}=0`$ the leading terms vanish and the deviation is of higher order in $`\delta p`$, given by (7.35).
6. *Starts at rest that are not narrow, and pairs with equal data.* For every start at rest outside (N), (N2) (fixed $`g`$ of any width, or $`\epsilon_0\gtrsim1`$) the order is given by (7.36) and the terms by (7.24) and (7.35), exactly; no further reduction to moments exists, because the whole functions $`\rho`$, $`j`$ enter. Their dependence on $`\lambda`$: $`\Theta_1\varphi_k`$ is a sum of vectors of the form $`\lambda^n\times(\text{bounded in }\lambda)`$, $`n\le2`$, by (7.29), so $`\mathrm{Re}\epsilon_1`$ grows at most as $`\lambda^2`$ and $`\mathcal V`$ at most as $`\lambda^4`$, as long as $`\Gamma^{(0)}_{kk'}`$ stays away from zero; at a zero, (OZ) applies. On the spread in the position: through $`j`$ and $`g'`$, at most linearly in $`X_g`$ per factor $`\Theta_1`$. For a pair with **equal data**, $`(\tau_k,M_k)=(\tau_{k'},M_{k'})`$, and every smooth $`g`$, every $`p_0`$ and $`\lambda`$: $`Z=\mathbb 1`$, $`\varphi_k=\varphi_{k'}`$, $`\chi_\perp=0`$, and (7.35) is, exactly,
```math
\lvert\Gamma_{kk'}\rvert=1-\tfrac12\Bigl[\lVert\Delta a\rVert^2+\lVert\Delta a_\perp\rVert^2-\lvert\langle g\vert\Delta a\rangle\rvert^2\Bigr]+O(\text{grad}^3),\qquad\Delta a:=a_k-a_{k'},\quad\Delta a_\perp:=a_{k,\perp}-a_{k',\perp}\ \ \text{of (7.29)},
\qquad\text{(7.39)}
```
which are (7.29) with the differences of the gradients. The bracket is the variance of $`\Omega_k-\Omega_{k'}`$ in the start: (O2) unless the start is an eigenvector of $`\Omega_k-\Omega_{k'}`$, and (O0) if the gradients are equal as well.
7. *Level-independent fall.* Let $`a_{k,\sigma}(0)=\sigma\nu_k\pi_k=a`$ for all $`k`$. Then $`\pi_k-\pi_{k'}=-\sigma a\Delta\nu_{kk'}/(\nu_k\nu_{k'})`$, $`\varpi_{kk'}=-\sigma a\Delta\nu_{kk'}(\nu_k+\nu_{k'})/(\nu_k\nu_{k'})`$, and (7.25), (7.38) become, in the class (N), range (N2), with the status of (7.25), (7.38):
```math
\Bigl(\frac{\lvert\Gamma_{kk'}\rvert}{\lvert\Gamma^{(0)}_{kk'}\rvert}\Bigr)_{1}\simeq\frac{a\,\Delta\nu_{kk'}^2}{\nu_k\,\nu_{k'}}\Bigl[\tfrac12\lambda^2J_g-\tfrac\sigma4\lambda^3\,(\nu_k+\nu_{k'})\,\langle p^3\rangle_g\Bigr],
\qquad\text{(7.26)}
```
```math
Q_2\simeq-\frac{a^2\,\Delta\nu_{kk'}^2}{2\,\nu_k^2\,\nu_{k'}^2}\Bigl[\lambda^2\delta x_g^2+\sigma\lambda^3(\nu_k+\nu_{k'})\,C_g+\tfrac14\lambda^4(\nu_k+\nu_{k'})^2\delta p^2\Bigr]\ \le\ -\frac{a^2\,\Delta\nu_{kk'}^2\,(1-\lvert g(\pi)\rvert^2)^2\,\lambda^2}{8\,\nu_k^2\,\nu_{k'}^2\,\delta p^2}.
\qquad\text{(7.40)}
```
**Does the deviation vanish when the fall is the same for all levels? No**, with this case distinction:
   - *(N), (N2), $`a\neq0`$, $`\nu_k\neq\nu_{k'}`$:* it does not vanish; $`Q_2<0`$ by the bound of (7.40) for every shape of $`g`$, and the first-order term (7.26) is present in addition if $`J_g\neq0`$ or $`\langle p^3\rangle_g\neq0`$. In the class $`\mathcal C`$ ($`\tau_k=\tau`$, $`M_k`$ distinct) this is every pair of levels: with $`a=-\tau^2g`$, $`a\Delta\nu/(\nu_k\nu_{k'})=g(d_k-d_{k'})`$, $`\nu_k+\nu_{k'}=\tau^2\tfrac{M_k+M_{k'}}{M_kM_{k'}}`$; the $`\lambda^2`$ term is $`\tfrac12\delta x_g^2g^2(d_k-d_{k'})^2\lambda^2`$, and by (3.23) $`g_\eta(d_k-d_{k'})=\tfrac{2\pi(k-k')}{N}\bigl(r(x+1)-r(x)\bigr)`$: it is the difference of the clock rates across the spread of the start.
   - *(N), (N2), $`a=0`$ or $`\nu_k=\nu_{k'}`$:* the leading terms (7.26), (7.40) vanish ($`\pi_k=\pi_{k'}`$, $`\varpi_{kk'}=0`$). The deviation itself vanishes only in case (O0); otherwise it is of higher order in $`\delta p`$ and given by (7.35) (for equal data by (7.39), with $`\Delta a\neq0`$ as soon as $`\pi_{k,\sigma}(p)\neq\pi_{k',\sigma}(p)`$ on the label weight).
   - *Starts at rest outside (N), (N2):* (7.36) with (7.24), (7.35); a level-independent fall is one condition on the gradients at $`p=0`$ and makes neither $`\mathrm{Re}\epsilon_1`$ nor $`\mathcal V`$ vanish unless (O0) holds or the start is an eigenvector of $`\Theta_1`$.

### Step 6. Item 2(a): records at first order

By the Setup, $`p^{[\xi]}`$ of (4.1) belongs to the effective level profiles with $`\mathcal F_k\to\mathcal F_k-\varepsilon_\xi`$. The zeroth-order velocity (4.5) does not depend on $`\xi`$; the first-order velocity is linear in $`(G_k,\mathcal F_k-\varepsilon_\xi,g_{\zeta,k})`$. Averaging with $`w_\xi`$ and $`\sum_\xi w_\xi\varepsilon_\xi=0`$:
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
3. *Solution to second order.* For $`z=S_\theta+iS_y`$: $`z(\lambda)=\varepsilon\int_0^\lambda\theta'S_n\,e^{i(\varphi(\lambda)-\varphi(s))}\mathrm ds`$, $`\varphi(s)=2\int_0^s\omega(q)`$. One integration by parts and $`\varphi(\lambda)=2\omega\lambda-\varepsilon\omega'\lambda^2+\tfrac13\varepsilon^2\omega''\lambda^3+O(\varepsilon^3)`$ give, with all functions now at $`p`$: $`S_\theta=\tfrac{\varepsilon\sigma\theta'}{2\omega}\sin2\omega\lambda-\varepsilon^2\sigma\bigl[\tfrac{\theta'\omega'}{2\omega}\lambda^2\cos2\omega\lambda+\tfrac1{4\omega}(\theta'/\omega)'(1-\cos2\omega\lambda)\bigr]`$ and $`S_n=\sigma-\varepsilon^2\sigma\tfrac{\theta'^2}{4\omega^2}(1-\cos2\omega\lambda)`$. Expanding $`\omega'(q),(\omega\theta')(q)`$ about $`p`$: $`v_p=\sigma\omega'+\varepsilon\sigma\bigl[-\lambda\omega''+\tfrac12\theta'^2\sin2\omega\lambda\bigr]+\varepsilon^2v_2+\varepsilon^3v_3+O(\varepsilon^4)`$,
```math
v_2(p,\lambda)=\sigma\Bigl[\tfrac12\lambda^2\omega'''-\tfrac{\theta'\theta''}{4\omega}(1-\cos2\omega\lambda)-\tfrac{\lambda}{2\omega}\theta'(\omega\theta')'\sin2\omega\lambda-\tfrac12\lambda^2\theta'^2\omega'\cos2\omega\lambda\Bigr].
\qquad\text{(7.13)}
```
The first-order term agrees with (4.7) for $`\mathcal F=-\varepsilon`$ and averages to zero over $`\xi`$ (Step 6). The terms of $`v_2`$, $`v_3`$ with the highest powers of $`\lambda`$ and an oscillating factor come from the phase of the first-order oscillation, $`\tfrac12\varepsilon\sigma\theta'^2\sin\varphi(\lambda)`$: $`-\tfrac12\lambda^2\theta'^2\omega'\cos2\omega\lambda`$ in $`v_2`$, and in $`v_3`$
```math
v_3(p,\lambda)=\sigma\Bigl[-\tfrac16\lambda^3\omega''''-\tfrac14\lambda^4\theta'^2\omega'^2\sin2\omega\lambda+\tfrac16\lambda^3\theta'^2\omega''\cos2\omega\lambda+\lambda^3\omega'\,(\dots)+O(\lambda^2)\Bigr],
```
where $`(\dots)`$ is smooth in $`p`$ times oscillating factors, and the only terms without an oscillating factor are $`-\tfrac16\lambda^3\omega''''`$ and one linear in $`\lambda`$ (the adiabatic series in $`p-\varepsilon\lambda`$). The Taylor expansion in $`\varepsilon`$ at a fixed label needs $`\lvert\varepsilon\rvert\lambda\ll p_c`$, $`\lvert\varepsilon\,\omega'\rvert\lambda^2\ll1`$ and $`\varepsilon^2\nu\lambda^3\ll1`$; beyond, the oscillating terms sum to $`\tfrac12\varepsilon\sigma\theta'^2\sin\varphi(\lambda)`$, bounded by $`\tfrac12\lvert\varepsilon\rvert t`$.
4. *Average over $`\xi`$ and $`g`$.* The $`\lambda^2\cos`$ term carries the factor $`\omega'`$: $`\langle\theta'^2\omega'\cos2\omega\lambda\rangle_g=-\tfrac1{2\lambda}\int\tfrac{\mathrm dp}{2\pi}(\lvert g\rvert^2\theta'^2)'\sin2\omega\lambda`$ (integration by parts on the circle). With $`\int\tfrac{\mathrm dp}{2\pi}\lvert(\lvert g\rvert^2)'\rvert\le2X_g`$ and $`\lvert\theta'\rvert\le\tau/M`$:
```math
\begin{aligned}
v(\lambda)&=\sigma\langle\omega_k'\rangle_g+\kappa^2\sigma_X^2\Bigl[\tfrac12\lambda^2\sigma\langle\omega_k'''\rangle_g+R_2(\lambda)\Bigr]+\kappa^3\mu_3\Bigl[-\tfrac16\lambda^3\sigma\langle\omega_k''''\rangle_g+R_3(\lambda)\Bigr]+O(\kappa^4),\\
\lvert R_2(\lambda)\rvert&\le\lambda\Bigl[\tfrac{\tau_k^2}{2M_k^2}X_g+\tfrac14\sup\lvert(\theta'^2)'\rvert+\tfrac12\sup\bigl\lvert\tfrac{\theta'(\omega\theta')'}{\omega}\bigr\rvert\Bigr]+\tfrac12\sup\bigl\lvert\tfrac{\theta'\theta''}{\omega}\bigr\rvert\ \ (\text{bound}),\qquad R_3(\lambda)=O(\lambda^{5/2})\ \ (\text{order estimate}).
\end{aligned}
\qquad\text{(7.14)}
```
The fastest-growing parts are the coefficients of the adiabatic term $`\sigma\omega'(p-\varepsilon\lambda)`$; their coefficients are exact. *Estimate of $`R_3`$ (order estimate at fixed smooth $`g`$).* Let $`\mathcal D_k:=\lambda\bigl(\lvert\omega_k'(p_0)\rvert\delta p+\lvert\omega_k''(p_0)\rvert\delta p^2\bigr)`$ be the **dephasing parameter**: the spread of the phase $`2\omega_k\lambda`$ over the label weight. In $`\langle v_3\rangle_g`$, each factor $`\omega'`$ of an oscillating term is removed by one integration by parts ($`\omega'e^{2i\omega\lambda}=\partial_pe^{2i\omega\lambda}/(2i\lambda)`$), which gains $`1/\lambda`$ and puts a derivative on $`\lvert g\rvert^2\theta'^2`$; an oscillating integral without a factor $`\omega'`$ over a weight of height $`\sim1/\delta p`$ is $`O(\mathcal D_k^{-1/2})`$ (stationary phase at the nondegenerate points $`p\in\{0,\pm\tfrac\pi2,\pi\}`$ of $`\omega_k`$; $`O(\mathcal D_k^{-1})`$ away from them). The $`\lambda^4\omega'^2`$ term gives $`-\tfrac{\sigma\lambda^3}{8}\int\tfrac{\mathrm dp}{2\pi}\lvert g\rvert^2\theta'^2\omega''\cos2\omega\lambda`$ plus terms smaller by $`1/\mathcal D_k`$; with the $`\lambda^3\theta'^2\omega''`$ term: $`R_3=O\bigl(t_k\nu_k\lambda^3\mathcal D_k^{-1/2}\bigr)`$, that is $`O(\lambda^{5/2}t_k\nu_k^{1/2}/\delta p)`$ at rest, for $`\mathcal D_k\gg1`$; for $`\mathcal D_k\lesssim1`$ the oscillating terms are not suppressed, and $`R_3`$ is of the order of the fastest-growing part (relative amplitude $`t_k/(4+3t_k)<\tfrac13`$ at rest, (7.43)). The bound on $`R_2`$ holds for all $`\lambda\ge0`$; it contains $`X_g`$ and is therefore not uniform in the spread ($`X_g\ge\lvert1-\lvert g(p_0+\pi)\rvert^2\rvert/(2\delta p)`$, (7.37) with the cut at $`p_0+\pi`$). Range: fixed smooth $`g`$, chain and $`\lambda`$, $`\kappa\to0`$, with the conditions of part 3 on the support of $`w_\xi`$. Controls: a sharp $`X`$ gives $`\sigma_X=\mu_3=0`$ and no term; a symmetric distribution of $`X`$ gives $`\mu_3=0`$.

### Step 8. Item 2(c),(d): change of the acceleration

1. *Exact acceleration for every start.* The change of the acceleration of $`\bar x_{\rm lab}`$ at the orders $`\kappa^2`$, $`\kappa^3`$ is $`\kappa^2\sigma_X^2\,a_2[g](\lambda)+\kappa^3\mu_3\,a_3[g](\lambda)`$ with $`a_n[g]:=\tfrac{\mathrm d}{\mathrm d\lambda}\langle v_n\rangle_g=\langle\partial_\lambda v_n\rangle_g`$. From the complete coefficient (7.13), exactly, for every smooth $`g`$ and $`\lambda\ge0`$:
```math
\partial_\lambda v_2(p,\lambda)=\sigma\Bigl[\lambda\,\omega'''+\lambda^2\,\omega\,\omega'\theta'^2\sin2\omega\lambda-\lambda\,\theta'\bigl(2\omega'\theta'+\omega\theta''\bigr)\cos2\omega\lambda-\frac{\theta'}{2\omega}\bigl(2\omega\theta''+\omega'\theta'\bigr)\sin2\omega\lambda\Bigr].
\qquad\text{(7.41)}
```
Pointwise in $`p`$ the second term grows faster than the first, and it oscillates at the level-dependent rate $`2\omega_k(p)`$. What the acceleration "for a sharp label" is depends on the order in which $`\delta p\to0`$ and the growth of $`\lambda`$ are taken; the two orders do not commute. They are separated by $`\mathcal D_k`$ of Step 7.
2. *The two orders of limits.*
```math
\begin{array}{l|l|l|l}
\text{case}&\text{defining condition}&\text{order }\kappa^2&\text{order }\kappa^3\text{ at rest}\\\hline
\text{A (dephased)}&\text{fixed smooth }g;\ \mathcal D_k\to\infty\ \text{or a long window, (7.33); then }\delta p\to0\text{ in the coefficient}&\text{(7.15)}&\text{(7.16)}\\
\text{B (coherent)}&\delta p\to0\text{ at fixed }\lambda\text{ or fixed window }(\mathcal D_k\to0)&\kappa^2\sigma_X^2\,\partial_\lambda v_2(p_0,\lambda),\ \text{(7.41), (7.42)}&\text{(7.43)}\\
\text{between}&\text{every smooth }g,\ \text{every }\lambda&\kappa^2\sigma_X^2\langle\partial_\lambda v_2\rangle_g,\ \text{(7.41), exact}&\kappa^3\mu_3\langle\partial_\lambda v_3\rangle_g
\end{array}
\qquad\text{(7.44)}
```
Case A is the order of limits of the drift acceleration (4.10), (4.11) (window at fixed $`g`$, then the sharp label).

   *Case A.* Write $`\langle v_n\rangle_g=s_n\lambda^n+R_n`$ with $`s_2=\tfrac\sigma2\langle\omega_k'''\rangle_g`$, $`s_3=-\tfrac\sigma6\langle\omega_k''''\rangle_g`$. For the average over a window $`[\lambda_1,\lambda_1+\Lambda]`$, $`\overline{a_n}:=(\langle v_n\rangle_g(\lambda_1+\Lambda)-\langle v_n\rangle_g(\lambda_1))/\Lambda`$, with the midpoint $`\bar\lambda:=\lambda_1+\tfrac\Lambda2`$, $`c_1[g]`$ the square bracket of the bound on $`R_2`$ in (7.14) and $`c_0:=\tfrac12\sup\lvert\theta'\theta''/\omega\rvert`$:
```math
\bigl\lvert\overline{a_2}-2s_2\,\bar\lambda\bigr\rvert\le\frac{2c_1[g]\,\bar\lambda+2c_0}{\Lambda}\ \ (\text{bound; every smooth }g,\ \lambda_1\ge0,\ \Lambda>0),\qquad\overline{a_3}=3s_3\Bigl(\bar\lambda^2+\frac{\Lambda^2}{12}\Bigr)+\frac{R_3(\lambda_1+\Lambda)-R_3(\lambda_1)}{\Lambda}.
\qquad\text{(7.33)}
```
A window $`\Lambda\gg c_1[g]/\lvert\langle\omega_k'''\rangle_g\rvert`$ is **sufficient** for the first term to dominate $`\overline{a_2}`$; a sequence of starts and windows with $`\delta p\to0`$ and $`c_1[g]/\Lambda\to0`$ is sufficient to combine the two limits (not shown to be necessary). Without a window: the oscillating terms of (7.41) are averages of a smooth weight of width $`\delta p`$ against $`e^{2i\omega_k\lambda}`$; for $`p_0`$ away from the stationary points of $`\omega_k`$, repeated integration by parts makes them $`O(\lambda^2\nu_k^2\lvert p_0\rvert\,\mathcal D_k^{-n})`$ for every $`n`$, with constants that depend on $`g`$, so $`a_2[g](\lambda)/\lambda\to2s_2`$ for $`\lambda\to\infty`$ at fixed $`g`$ (order estimate). The coefficients have the sharp-label limits $`\langle\omega_k'''\rangle_g\to\omega_k'''(p_0)`$, $`\langle\omega_k''''\rangle_g\to\omega_k''''(p_0)`$ (mean and variance only; errors $`\le\tfrac12\sup\lvert\omega_k^{(5)}\rvert\delta p^2`$, $`\le\tfrac12\sup\lvert\omega_k^{(6)}\rvert\delta p^2`$). With $`v=\sigma\omega_k'(p_0)`$ of (4.17) and $`\omega'''=-\omega'(4+3\omega''/\omega)`$, for every $`p_0`$ and, in the last form, **near rest** ($`\lvert p_0\rvert\ll p_c`$, where $`v=\sigma\nu_kp_0(1+O(p_0^2/p_c^2))`$):
```math
\delta a^{(2)}_{k,\sigma}=\kappa^2\sigma_X^2\,\lambda\,\sigma\,\omega_k'''(p_0)=-\kappa^2\sigma_X^2\,\lambda\,v\Bigl(4+\frac{3\,\omega_k''(p_0)}{\omega_k(p_0)}\Bigr)=-\kappa^2\sigma_X^2\,\lambda\Bigl(4+\frac{3\tau_k^2}{M_k^2}\Bigr)v\,\Bigl(1+O\bigl(p_0^2/p_c^2\bigr)\Bigr).
\qquad\text{(7.15)}
```
It vanishes at rest, is of first order in $`v`$, opposes $`v`$, grows linearly in $`\lambda`$, and at given $`v`$ is the same in both branches. Small $`v`$ alone does not give the last form: near $`p_0=\tfrac\pi2`$ the velocity is small as well, and the bracket of the middle form tends to $`4-3\tau_k^2/(M_k^2+\tau_k^2)`$; near $`p_0=\pi`$ it is as near $`0`$. The third-order term does not vanish at rest:
```math
\delta a^{(3)}_{k,\sigma}=-\tfrac12\kappa^3\mu_3\,\lambda^2\,\sigma\,\omega_k''''(p_0),\qquad\delta a^{(3)}_{k,\sigma}\big\vert_{p_0=0}=\frac{\sigma}{2}\,\kappa^3\mu_3\,\lambda^2\,\frac{\tau_k^2}{M_k}\Bigl(4+\frac{3\tau_k^2}{M_k^2}\Bigr),
\qquad\text{(7.16)}
```
of zeroth order in $`v`$ (relative corrections $`O(p_0^2/p_c^2)`$ near rest), odd in the branch, present only for a skewed distribution of $`X`$; that it is the fastest-growing part rests on the estimate of $`R_3`$.

   *Case B.* Taylor's formula in $`p`$ (mean and variance of the label weight) gives $`a_2[g](\lambda)\to\partial_\lambda v_2(p_0,\lambda)`$ for $`\delta p\to0`$ at fixed $`\lambda`$. Exactly zero at rest (every term of (7.13) vanishes at $`p=0`$: $`\omega'=\theta''=(\omega\theta')'=0`$). Near rest, expanding the coefficients of (7.41) with the facts of the Setup ($`\omega=\omega_k(p_0)`$ in the trigonometric functions):
```math
\delta a^{(2)}_{k,\sigma}\Big\vert_{\rm B}=\kappa^2\sigma_X^2\,v\Bigl[-(4+3t_k)\lambda+\lambda\cos2\omega\lambda+\nu_k\lambda^2\sin2\omega\lambda+\frac{2+3t_k}{2M_k}\sin2\omega\lambda\Bigr]\Bigl(1+O\bigl(p_0^2/p_c^2\bigr)\Bigr);\qquad\Bigl\lvert\overline{a_2}(p_0)-\sigma\omega'''\bar\lambda\Bigr\rvert\le\frac1\Lambda\Bigl[\theta'^2\lvert\omega'\rvert\Bigl(\bar\lambda^2+\frac{\Lambda^2}4\Bigr)+\frac{\lvert\theta'(\omega\theta')'\rvert}{\omega}\bar\lambda+\frac{\lvert\theta'\theta''\rvert}{2\omega}\Bigr].
\qquad\text{(7.42)}
```
The second statement is an exact bound for the window average at a sharp label, every $`p_0`$ (the three oscillating terms of (7.13) at the two ends of the window). So in case B the change of the acceleration is still zero at rest and of first order in $`v`$, but it is not (7.15): the oscillating term $`\nu_k\lambda^2\sin2\omega\lambda`$ exceeds the secular one for $`\nu_k\lambda>4+3t_k`$, and in a window average its relative size is up to $`t_k(\bar\lambda/\Lambda+\Lambda/4\bar\lambda)/(4+3t_k)`$, which no choice of the window makes small unless $`t_k\ll1`$. At third order and at rest, the Bloch equations (7.12) at $`p=0`$ ($`q=-\varepsilon s`$, $`\varphi(\lambda)-\varphi(s)=2M(\lambda-s)+\tfrac13\nu\varepsilon^2(\lambda^3-s^3)`$, $`z`$ to the order $`\varepsilon^3`$ by elementary integrals) give, exactly:
```math
\begin{aligned}
v_3(0,\lambda)&=\sigma\Bigl\{\frac{\nu_k}{6}\lambda^3\bigl[(4+3t_k)+t_k\cos2M_k\lambda\bigr]-\frac{t_k(1+t_k)}4\lambda^2\sin2M_k\lambda-\frac{t_k}{4M_k}\lambda\bigl[(1+2t_k)+\tfrac12t_k\cos2M_k\lambda\bigr]+\frac{t_k(2+5t_k)}{16M_k^2}\sin2M_k\lambda\Bigr\},\\
\partial_\lambda v_3(0,\lambda)&=\sigma\Bigl\{\frac{\nu_k}{2}\lambda^2\bigl[(4+3t_k)-\cos2M_k\lambda\bigr]-\frac{\tau_k^2t_k}{3}\lambda^3\sin2M_k\lambda-\frac{t_k(2+t_k)}4\lambda\sin2M_k\lambda-\frac{t_k(1+2t_k)}{4M_k}\bigl(1-\cos2M_k\lambda\bigr)\Bigr\}.
\end{aligned}
\qquad\text{(7.43)}
```
$`\delta a^{(3)}_{k,\sigma}\vert_{\rm B}=\kappa^3\mu_3\,\partial_\lambda v_3(0,\lambda)`$ at rest: its non-oscillating part is (7.16), and it has in addition an oscillating part that grows as $`\lambda^3`$. For $`p_0\neq0`$ the highest power is $`-\tfrac12\sigma\lambda^4\omega\,\theta'^2\omega'^2\cos2\omega\lambda`$ (Step 7, part 3), small against (7.43) for $`\lvert\omega_k'(p_0)\rvert\lambda\ll1`$.
3. *Level and branch dependence.* Branch: at given $`v`$ the second-order terms (7.15), (7.42) are the same in both branches; the third-order terms (7.16), (7.43) are odd in $`\sigma`$. Level:
   - *Case A.* (7.15) is the same for all levels at leading order in $`v`$ near rest **iff** $`\tau_k/M_k`$ does not depend on $`k`$, and as a function of $`p_0`$ iff $`(\tau_k,M_k)`$ do not ($`\omega_k-\omega_{k'}`$ constant forces equal data). (7.16) at rest is level-independent iff $`\nu_k(4+3t_k)`$ is.
   - *Case B.* (7.42) and (7.43) are the same for all levels, for all $`\lambda`$, **iff** $`(\tau_k,M_k)`$ do not depend on $`k`$: the oscillation rate $`2M_k`$ has to be common, and then $`t_k`$. A common $`\tau_k/M_k`$, which suffices in case A, does not suffice here.
   - In the class $`\mathcal C`$ ($`\tau_k=\tau`$, $`M_k`$ distinct): **no** in both cases; for $`M_k\ll\tau`$ the case-A terms scale as $`M_k^{-2}`$ and $`M_k^{-3}`$.
4. *Background form and the weak-record regime (item 2(d)).* *The speed bound of one level.* In the level $`k`$ the velocity operator is $`i[C^{(k)}+\varepsilon\hat x,\hat x]=-\tau_k\cos\hat p\,\sigma_1`$ at zero gradients (with gradients, the same with the factors $`\zeta_{x,k}`$), of norm $`\tau_k`$. With $`d_0=\kappa\sigma_X`$, $`\hat e`$ and $`\bar x=d_0\bar x_{\rm lab}\hat e`$ of (17.15) of 03-ilang-space/17-motion:
```math
\Bigl\lVert\frac{\mathrm d\bar x}{\mathrm d\lambda}\Bigr\rVert\le c_k:=\tau_k\,d_0\ \ \text{for every state in the level }k;\qquad c_k\le d_0\max_j\tau_j\le v^{\rm full}_{\max}:=d_0\sum_{n\in\mathbb Z_N}\Bigl\lvert\frac1N\sum_j\tau_je^{2\pi ijn/N}\Bigr\rvert .
\qquad\text{(7.45)}
```
$`c_k`$ is a bound for one conserved level, derived here. $`v^{\rm full}_{\max}`$ is the row-sum expression of (5.11) of 04-ilang-time/05-moving-clock for the complete body contract in the place basis $`(x,s,a)`$, where the hopping contains $`\sum_j\tau_j\lvert f_j\rangle\langle f_j\rvert`$, not diagonal in the clock places (row sum of a circulant matrix; it is at least the largest eigenvalue). The two are different statements; they coincide, $`c_k=v_{\max}=\tau d_0`$, iff the $`\tau_j`$ are equal, as in the class $`\mathcal C`$. For $`\Phi_\sigma[\alpha,g]`$ the bound is $`\sum_k\lvert\alpha_k\rvert^2c_k`$, by (7.1). With $`u:=d_0v`$ and $`\gamma_X:=\mu_3/\sigma_X^3`$, the case-A terms (7.15), (7.16) near rest are
```math
\delta\frac{\mathrm d^2\bar x}{\mathrm d\lambda^2}=\Bigl[-\lambda\Bigl(4d_0^2+\frac{3c_k^2}{M_k^2}\Bigr)u+\frac{\sigma\gamma_X}{2}\,\lambda^2\,\frac{c_k^2}{M_k}\Bigl(4d_0^2+\frac{3c_k^2}{M_k^2}\Bigr)\Bigr]\Bigl(1+O\bigl(p_0^2/p_c^2\bigr)\Bigr)\hat e,\qquad d_0\,a_{k,\sigma}(0)=\frac{c_k^2}{d_0M_k}\bigl(\sigma\mathcal F_k-G_k\bigr),
\qquad\text{(7.17)}
```
with $`p_0^2/p_c^2=v^2/(\nu_kp_c)^2`$ to this order. They are smaller than the drift acceleration (4.7) at rest where
```math
\varrho_2:=\frac{\lambda\lvert u\rvert M_k}{d_0\,\tau_k^2\lvert\sigma\mathcal F_k-G_k\rvert}\Bigl(4d_0^2+\frac{3c_k^2}{M_k^2}\Bigr)<1\quad\text{and}\quad\varrho_3:=\frac{\lvert\gamma_X\rvert d_0\lambda^2}{2\lvert\sigma\mathcal F_k-G_k\rvert}\Bigl(4d_0^2+\frac{3c_k^2}{M_k^2}\Bigr)<1,
\qquad\text{(7.18)}
```
that is $`\lambda<\lambda_2:=\nu_k\lvert\sigma\mathcal F_k-G_k\rvert/(\kappa^2\sigma_X^2(4+3t_k)\lvert v\rvert)`$ and $`\lambda<\lambda_3:=\bigl(2\lvert\sigma\mathcal F_k-G_k\rvert/(\kappa^3\lvert\mu_3\rvert(4+3t_k))\bigr)^{1/2}`$. The rests of the window averages (7.33), relative to the drift acceleration, are
```math
\varrho_{2,\rm rest}:=\kappa^2\sigma_X^2\,\frac{2c_1[g]\,\bar\lambda+2c_0}{\Lambda}\cdot\frac{M_k}{\tau_k^2\,\lvert\sigma\mathcal F_k-G_k\rvert}\ \ (\text{bound}),\qquad\varrho_{3,\rm rest}:=\frac{\kappa^3\lvert\mu_3\rvert\,\lvert R_3(\lambda_1+\Lambda)-R_3(\lambda_1)\rvert}{\Lambda\,\nu_k\lvert\sigma\mathcal F_k-G_k\rvert}=O\Bigl(\frac{\kappa^3\lvert\mu_3\rvert\,t_k\,\bar\lambda^3}{\Lambda\,\mathcal D_k^{1/2}\lvert\sigma\mathcal F_k-G_k\rvert}\Bigr).
\qquad\text{(7.34)}
```
*The accuracy range.* At the orders retained by the question (first order in the gradients at $`\kappa^0`$; $`\kappa^2`$ and $`\kappa^3`$ at zero gradients), the window-averaged acceleration of the level $`k`$ for a fixed smooth $`g`$ near rest is the drift term of (4.10) plus $`\kappa^2\sigma_X^2\overline{a_2}+\kappa^3\mu_3\overline{a_3}`$. Since $`\lambda_1\ge0`$ gives $`\Lambda\le2\bar\lambda`$, (7.33) yields: if, at $`\lambda=\bar\lambda`$ and for every level with $`\alpha_k\neq0`$,
```math
\varrho_2+\varrho_{2,\rm rest}+\tfrac43\varrho_3+\varrho_{3,\rm rest}\le\delta_{\rm acc},
\qquad\text{(7.46)}
```
then the record terms change the window-averaged acceleration of each level by at most $`\delta_{\rm acc}`$ times its drift acceleration, and two levels with the same drift acceleration fall alike to the relative accuracy $`2\delta_{\rm acc}`$. (7.46) is sufficient at the retained orders ($`\varrho_2,\varrho_{2,\rm rest}`$ controlled by bounds, $`\varrho_{3,\rm rest}`$ by the estimate of $`R_3`$); terms that mix $`\kappa`$ with the gradients, $`\kappa^4`$ and the second order in the gradients are outside the scope of the question and not part of the statement. It is also necessary up to factors of order one when the record terms of the levels differ by relative amounts of order one (class $`\mathcal C`$ with $`M_k`$ not close): then $`\lvert\delta a_k-\delta a_{k'}\rvert\sim\lvert\delta a_k\rvert`$. Asking each of the four terms to be $`\le\delta_{\rm acc}/4`$ gives the range
   - in $`\lambda`$: $`\bar\lambda\le\tfrac14\delta_{\rm acc}\lambda_2`$ and $`\bar\lambda\le(\tfrac3{16}\delta_{\rm acc})^{1/2}\lambda_3`$, with a window $`\Lambda\ge4\kappa^2\sigma_X^2(2c_1[g]\bar\lambda+2c_0)/(\delta_{\rm acc}\nu_k\lvert\sigma\mathcal F_k-G_k\rvert)`$, which exists inside $`\Lambda\le2\bar\lambda`$ only if $`4\kappa^2\sigma_X^2c_1[g]\le\delta_{\rm acc}\nu_k\lvert\sigma\mathcal F_k-G_k\rvert`$ (a condition on the spread of the start, through $`X_g`$), and $`\mathcal D_k\gg1`$;
   - in $`\kappa`$, at fixed $`\bar\lambda`$ and $`v`$: $`\kappa^2\le\delta_{\rm acc}\nu_k\lvert\sigma\mathcal F_k-G_k\rvert/(4\sigma_X^2(4+3t_k)\lvert v\rvert\bar\lambda)`$ and $`\kappa^3\le3\delta_{\rm acc}\lvert\sigma\mathcal F_k-G_k\rvert/(8\lvert\mu_3\rvert(4+3t_k)\bar\lambda^2)`$;
   - in the gradients: $`\lvert\sigma\mathcal F_k-G_k\rvert\ge\tfrac4{\delta_{\rm acc}}\max\bigl\{\kappa^2\sigma_X^2(4+3t_k)\lvert v\rvert\bar\lambda/\nu_k,\ \tfrac23\kappa^3\lvert\mu_3\rvert(4+3t_k)\bar\lambda^2\bigr\}`$.

   For a sharp label without dephasing (case B) the same comparison uses (7.42), (7.43): at rest the second-order term is zero, and the third-order term needs in addition $`\kappa^3\lvert\mu_3\rvert\,\tfrac13\tau_k^2t_k\lambda^3\le\delta_{\rm acc}\nu_k\lvert\sigma\mathcal F_k-G_k\rvert`$. So **"weak records" has to mean** (7.46) for every level involved, on the whole range of $`\lambda`$, windows and $`v`$ observed: a joint condition on $`\kappa^2\lambda\lvert v\rvert`$, $`\kappa^3\lvert\mu_3\rvert\lambda^2`$ and the gradients. It is not uniform in $`\lambda`$, it depends on the start (through $`X_g`$ and $`\mathcal D_k`$), and it fails if the gradients are sent to zero at fixed $`\kappa`$; "$`\kappa\to0`$ at fixed $`\lambda`$, chain and start" satisfies it for every $`\delta_{\rm acc}>0`$.

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

Orders are those of the leading deviation; "grad" is the joint order in the gradients; the entries on $`M_k/\tau_k`$ are relative to the fall; orders in $`v`$ are orders near rest ($`\lvert p_0\rvert\ll p_c`$). (i): the fall is the same for all levels; (ii): the relation (4.24), a statement at rest in the class $`\mathcal C`$.

| Source | (i) level-independent fall | (ii) relation (4.24) | Tags |
|---|---|---|---|
| Lattice | grad$`^1`$, $`v^2`$, relative $`(M_k/\tau_k)^2`$, $`\kappa^0`$, $`\lambda^0`$: $`c_{2,k,+}-c_{2,k',+}=-2a_0\bigl(\tfrac{M_k^2}{\tau_k^4}-\tfrac{M_{k'}^2}{\tau_{k'}^4}\bigr)`$; none at $`v=0`$ | none at $`v=0`$; at $`v\neq0`$ level-dependent at grad$`^1`$, $`v^2`$, $`(M_k/\tau)^2`$ | (4.20), (4.21), (4.23), (4.25) |
| Drift velocity | grad$`^1`$, $`v^2`$, $`(M_k/\tau_k)^0`$ unless $`c^{(0)}_{2,k}`$ is level-independent; in $`\mathcal C`$ only for $`\mathcal F=0`$, $`g_m=g_\eta`$; $`O(v^4)`$ an order estimate | the acceleration is $`a(0)+c_2v^2`$: grad$`^1`$, relative $`c_2v^2/a(0)`$ (variant (a): $`-\ell_kv^2/\tau^2`$), $`\kappa^0`$, $`\lambda^0`$ | (4.17), (4.20), (4.21), (4.23) |
| Superposition of levels | no new condition (limits of (7.2)); if the fall is level-dependent: mean acceleration $`\alpha`$-dependent at grad$`^1`$; between-level variance grad$`^2`$, $`\lambda^4`$ (coefficient in the sharp-label limit); at $`p_0\neq0`$ separation at grad$`^0`$, $`v^1`$, $`\lambda^1`$ for $`\delta p<\delta p_*`$ of (7.27) | position side unchanged (exact mixture); label rates level-dependent at grad$`^1`$ (sequences with $`c_{\rm cut}\neq1`$, (7.28)); $`\lvert\Gamma_{kk'}\rvert`$, order by (7.36): grad$`^1`$ iff $`\mathrm{Re}\epsilon_1\neq0`$, for narrow starts at rest $`\Delta\nu_{kk'}[\lambda^3\varpi_{kk'}\langle p^3\rangle_g,\ \lambda^2(\pi_k-\pi_{k'})J_g]`$; grad$`^2`$ always present for narrow starts with $`(\pi_k-\pi_{k'},\varpi_{kk'})\neq0`$: $`\lambda^2\delta x_g^2`$, $`\lambda^3C_g`$, $`\lambda^4\delta p^2`$, and the only order for definite parity or equal data; both also for a level-independent fall $`a\neq0`$ unless $`\nu_k=\nu_{k'}`$ | (7.1)–(7.5), (7.27), (7.7), (7.28), (7.8), (7.9), (7.23)–(7.26), (7.29)–(7.32), (7.35)–(7.40) |
| Records | $`\kappa^1`$: none. $`\kappa^2\sigma_X^2`$: grad$`^0`$, zero at $`v=0`$, $`v^1`$; case A: $`\lambda^1`$, factor $`4+3t_k`$, level-independent iff $`\tau_k/M_k`$ is; case B: in addition oscillating terms up to $`\nu_k\lambda^2`$ at the rate $`2\omega_k`$, level-independent iff $`(\tau_k,M_k)`$ are. $`\kappa^3\mu_3`$: grad$`^0`$, $`v^0`$; case A: $`\lambda^2`$, factor $`\nu_k(4+3t_k)`$; case B: in addition oscillating terms up to $`\tfrac13\tau_k^2t_k\lambda^3`$ | the same terms add to the left side; below the relative accuracy $`\delta_{\rm acc}`$ on the range (7.46) | (7.11), (7.13)–(7.18), (7.33), (7.34), (7.41)–(7.46) |
| Operator under the factor | grad$`^1`$, $`v^0`$, $`\kappa^0`$, $`\lambda^0`$, relative $`(\mathcal F_U-gu_k)/(gM_k)`$: the same order as the fall, no small parameter | in $`\mathcal C`$ the hypothesis holds iff $`\mathcal F_U=gc_{\rm f}`$; then unchanged | (7.19)–(7.21), (4.25) row (f) |
| Plain gradient | grad$`^1`$, $`v^0`$: $`\sigma\tau_k^2\mathcal F_k/M_k`$, level-dependent and odd in the branch; in $`\mathcal C`$ admissible at rest only for $`\mathcal F=\pm m(g_m-g_\eta)`$, through $`v^2`$ only $`\mathcal F=0`$ (leading order in $`M_k/\tau`$) | the hypothesis fixes $`\mathcal F=m(g_m-g_\eta)`$; any other $`\mathcal F`$ breaks it at grad$`^1`$, $`v^0`$ | (4.16), (4.19), (4.22), (4.23), (4.25) row (d) |
```math
\text{(the table above is the result of item 4)}
\qquad\text{(7.22)}
```

## Result

Common class, unless an item restricts it: a body of $`\mathcal C_{\rm lev}`$ with linear level profiles, both branches $`\sigma`$, every level, $`\lambda\ge0`$, the infinite chain as the limit of long chains. "First order" is the first order in the gradients at fixed $`\lambda`$, start and chain, followed by the long chain. "Leading order in $`\kappa`$" is $`\kappa\to0`$ at fixed $`\lambda`$, chain and start (the effective body contract). A *sharp-label limit* is a limit along a sequence of starts concentrated at $`p_0`$ with $`\delta p\to0`$; where nothing else is said it uses only the mean and the variance of the label weight.

**Item 1, starts $`\Phi_\sigma[\alpha,g]`$.**
- **(7.1)** Exact in the gradients and in $`\kappa`$; every $`\alpha`$, smooth $`g`$, $`\chi`$, $`\lambda`$, chain. $`p_x=\sum_k\lvert\alpha_k\rvert^2p^{(k)}_x`$, $`\bar x_{\rm lab}=\sum_k\lvert\alpha_k\rvert^2\bar x_k`$; rests on the conservation of the level and the orthonormality of the $`\lvert f_k\rangle`$.
- **(7.2)** Every $`\alpha`$, every smooth $`g`$ concentrated at $`p_0`$. Limits: first order, long chain, $`\Lambda\to\infty`$ at fixed $`g`$, then sharp label; leading order in $`\kappa`$. Drift acceleration $`\sum_k\lvert\alpha_k\rvert^2a_{k,\sigma}(p_0)`$ (the bound is exact for every $`\Lambda>0`$). The same for all $`\alpha`$ iff $`a_{k,\sigma}(p_0)`$ is level-independent; at rest line 1 or 2 of (4.19), no new condition.
- **(7.3), (7.4)** Starts at rest, fixed smooth $`g`$; first order, long chain. $`D=\tfrac14\lambda^4\mathrm{Var}_\alpha(\langle a_{\cdot,\sigma}\rangle_g)+E`$ with a bound on $`E`$; the sharp-label limit is taken on the coefficient of $`\lambda^4`$, which tends to $`\tfrac14\mathrm{Var}_\alpha(a_{\cdot,\sigma}(0))`$. (7.4), class $`\mathcal C`$, $`\lvert\alpha_k\rvert^2=1/N`$: zero for (a), (c); $`\tfrac14\lambda^4\tau^4g^2m^2\mathcal V_N`$ for (b1), (b2); $`\tfrac14\lambda^4\tau^4g^2c_{\rm f}^2\mathcal V_N`$ for (f).
- **(7.5), (7.27)** Zero gradients. Exact, every smooth $`g`$: $`v_k=\sigma\langle\omega_k'\rangle_g`$; bound (7.27); sharp-label velocities (7.5). Item 1(d): a start of finite width can have equal velocities in all levels (example, every member of $`\mathcal C_{\rm lev}`$); in $`\mathcal C`$, for $`\sin2p_0\neq0`$, no start with $`\delta p<\delta p_*`$ has equal velocities in two levels; in $`\mathcal C_{\rm lev}`$ equality at one such $`p_0`$ is one condition and needs $`\tau_k\neq\tau_{k'}`$, at all $`p_0`$ iff the data are equal.
- **(7.6), (7.7), (7.28)** (7.6) exact in the gradients. (7.7) first order, every smooth $`g`$, no window. (7.28) bound, every start at rest. For sequences of starts at rest with $`\delta p\to0`$, $`\lvert g(\pi)\rvert^2\to c_{\rm cut}`$: limiting rate $`(1-c_{\rm cut})(\mathcal F_k-\sigma G_k)`$. For $`c_{\rm cut}\neq1`$: level-independent iff $`\mathcal F_k-\sigma G_k`$ is; together with a level-independent drift acceleration $`a\neq0`$ iff also $`\tau_k^2/M_k`$ is; impossible in $`\mathcal C`$. For $`c_{\rm cut}=1`$ the limiting rate is zero in every level.
- **(7.8), (7.9), (7.23)** (7.8) exact with the medium in the level components; at leading order in $`\kappa`$ the $`\Gamma_{kk'}`$ of the effective body contract. (7.9) exact, every smooth $`g`$. (7.23) exact, every $`g`$, $`p_0`$, $`\lambda`$: $`\Gamma_{kk'}[g;\text{grad}]=\Gamma_{kk'}[g^-;-\text{grad}]`$.
- **(7.35), (7.36)** Exact Taylor expansion in the gradients at fixed $`\lambda`$ and start; every smooth $`g`$, $`p_0`$, $`\lambda`$ with $`\Gamma^{(0)}_{kk'}\neq0`$; leading order in $`\kappa`$. $`\lvert\Gamma_{kk'}\rvert/\lvert\Gamma^{(0)}_{kk'}\rvert=1+\mathrm{Re}\epsilon_1+Q_2+O(\text{grad}^3)`$, $`Q_2=-\tfrac12\mathcal V+\tfrac12(\mathrm{Im}\epsilon_1)^2+\mathrm{Re}\epsilon_2`$; bound $`\lvert\epsilon_1\rvert\le\eta_0\mathcal V^{1/2}`$. **Order of the first deviation**, complete by (7.36): none (equal blocks); degree one at a zero of $`\Gamma^{(0)}_{kk'}`$; first order iff $`\mathrm{Re}\epsilon_1\neq0`$; second order iff $`\mathrm{Re}\epsilon_1=0\neq Q_2`$; otherwise third or higher. Starts of definite parity and pairs with equal data have $`\mathrm{Re}\epsilon_1=0`$ (exact).
- **(7.24), (7.29), (7.30), (7.31)** Exact, every smooth complex $`g`$, $`p_0`$, $`\lambda\ge0`$: the complete first-order term $`\Gamma^{(1)}_{kk'}`$, branch part and inter-branch part, with the bounds $`A_{k,\perp}`$ and (7.30). (7.31): bound, every start at rest; $`\Gamma^{(0)}_{kk'}\neq0`$ where $`\epsilon_0<1`$.
- **(7.37)** Bound, every start at rest: $`\delta x_g^2\delta p^2\ge C_g^2+\tfrac14(1-\lvert g(\pi)\rvert^2)^2`$, hence $`2\delta pX_g\ge\lvert1-\lvert g(\pi)\rvert^2\rvert`$.
- **(7.38), (7.10), (7.25), (7.32)** Class (N): narrow starts at rest of any shape (smooth complex $`g`$, $`\delta p\ll p_c`$, moment conditions, $`c_{\rm cut}\neq1`$); range (N2): $`\epsilon_0\ll1`$. Status: leading terms, order estimates; the coefficients are exact in the local form, the lower bound of (7.38) is exact, and (7.32) gives the size of every neglected contribution with its calculation. Second order: $`Q_2\simeq-\tfrac12\mathrm{Var}_g(K_{kk'})`$, different from zero iff $`(\pi_k-\pi_{k'},\varpi_{kk'})\neq(0,0)`$; dependence $`\lambda^2\delta x_g^2`$, $`\lambda^3C_g`$, $`\lambda^4\delta p^2`$; (7.10) is the real Gaussian case. First order: (7.25), present iff $`\Delta\nu_{kk'}\neq0`$ and its bracket is not zero. Where (7.38) leads, for data that differ by order one: (N2) with $`\lambda\gg\tau\delta p/M^2`$.
- **(7.39)** Exact through second order; pairs with equal $`(\tau,M)`$, every smooth $`g`$, $`p_0`$, $`\lambda`$: $`1-\lvert\Gamma_{kk'}\rvert=\tfrac12\mathrm{Var}(\Omega_k-\Omega_{k'})`$. Starts at rest that are not narrow, with unequal data: (7.36), (7.24), (7.35), exact; growth at most $`\lambda^2`$ (first order) and $`\lambda^4`$ (second order).
- **(7.26), (7.40)** Class (N), range (N2), status of (7.25), (7.38). With a level-independent fall $`a`$: the deviation **does not vanish** for $`a\neq0`$ and $`\nu_k\neq\nu_{k'}`$ ($`Q_2<0`$ by an exact lower bound, for every shape of $`g`$); in $`\mathcal C`$ this is every pair. For $`a=0`$ or $`\nu_k=\nu_{k'}`$ the leading terms vanish; the deviation vanishes identically only for equal blocks.

**Item 2, branch starts $`B_{k,\sigma}[g]`$.**
- **(7.11)** Exact at this order; every smooth $`g`$, every $`\chi`$; first order jointly in $`G_k`$, $`\mathcal F_k`$, $`g_{\zeta,k}`$, $`\kappa(\xi-\langle X\rangle)`$: no change of the first-order velocity, nor of (4.7), (4.16), (4.19).
- **(7.13), (7.14)** Zero gradients; every fixed smooth $`g`$, every $`\chi`$ with finite moments of $`X`$; Taylor expansion in $`\kappa`$ at fixed $`\lambda`$, start, chain. (7.13) exact pointwise in $`p`$. Fastest-growing parts $`\tfrac12\lambda^2\sigma\langle\omega_k'''\rangle_g`$ and $`-\tfrac16\lambda^3\sigma\langle\omega_k''''\rangle_g`$, coefficients exact. $`R_2`$: bound, linear in $`\lambda`$. $`R_3=O(t_k\nu_k\lambda^3\mathcal D_k^{-1/2})`$: order estimate for $`\mathcal D_k\gg1`$, with its calculation.
- **(7.41), (7.44)** Exact, every smooth $`g`$, every $`\lambda`$: the change of the acceleration at order $`\kappa^2`$ is $`\kappa^2\sigma_X^2\langle\partial_\lambda v_2\rangle_g`$. The sharp-label limit and the growth of $`\lambda`$ do not commute; (7.44) lists the cases with their defining conditions.
- **(7.15), (7.16), (7.33)** Case A (fixed smooth $`g`$, long window or $`\mathcal D_k\to\infty`$, then sharp label in the coefficient; the order of limits of the drift acceleration). (7.33): bound at order $`\kappa^2`$, identity at order $`\kappa^3`$. $`\delta a^{(2)}=-\kappa^2\sigma_X^2\lambda v(4+3\omega_k''/\omega_k)`$, exact coefficient for every $`p_0`$: zero at rest, first order in $`v`$, same in both branches; near rest ($`\lvert p_0\rvert\ll p_c`$) the factor is $`4+3t_k`$. $`\delta a^{(3)}`$ at rest $`=\tfrac\sigma2\kappa^3\mu_3\lambda^2\nu_k(4+3t_k)`$: zeroth order in $`v`$, odd in the branch, skewed $`X`$ only. Level-independent iff $`\tau_k/M_k`$, respectively $`\nu_k(4+3t_k)`$, is; not in $`\mathcal C`$.
- **(7.42), (7.43)** Case B (sharp label at fixed $`\lambda`$ or fixed window). Exact: $`\kappa^2\sigma_X^2\partial_\lambda v_2(p_0,\lambda)`$, zero at rest, first order in $`v`$, with oscillating terms up to $`\nu_k\lambda^2`$; exact bound for the window average; exact third-order velocity and acceleration at rest (7.43), with an oscillating part $`\propto\lambda^3`$. Level-independent iff $`(\tau_k,M_k)`$ are; not in $`\mathcal C`$.
- **(7.45)** Bound: $`\lVert\mathrm d\bar x/\mathrm d\lambda\rVert\le c_k=\tau_kd_0`$ in the level $`k`$; it equals the bound (5.11) of 04-ilang-time/05-moving-clock iff the $`\tau_k`$ are equal.
- **(7.17), (7.18), (7.34), (7.46)** Case A, near rest, background of (17.15) of 03-ilang-space/17-motion. The record terms are smaller than the drift acceleration for $`\varrho_2,\varrho_3<1`$. **Weak records** has to mean (7.46) for every level involved: then the fall is level-independent to the relative accuracy $`2\delta_{\rm acc}`$ at the retained orders; sufficient (bounds at order $`\kappa^2`$, estimate of $`R_3`$ at order $`\kappa^3`$), with the ranges in $`\lambda`$, $`\kappa`$ and the gradients of Step 8, part 4; not uniform in $`\lambda`$ and violated for gradients $`\to0`$ at fixed $`\kappa`$.

**Item 3, on-site block $`(1+gx)[M_k\sigma_3+u_k\mathbb 1_2]-\mathcal F_Ux\,\mathbb 1_2`$, any $`\tau_k`$, $`g_{\zeta,k}`$; drift acceleration from rest, leading order in $`\kappa`$.**
- **(7.19), (7.20)** Exact in these limits. $`a_{k,\pm}(0)=-g\tau_k^2\pm\tfrac{\tau_k^2}{M_k}(\mathcal F_U-gu_k)`$ and the three equivalences; one value in both branches iff $`gu_k=\mathcal F_U`$ and $`g\tau_k^2=-a`$ for all $`k`$.
- **(7.21)** Exact. Well defined: $`g`$, $`M_k`$, $`u_k-u_{k'}`$, $`\mathcal F_U-gu_k`$. Not well defined: $`u_k`$, "$`u_k=0`$ for all $`k`$", "$`u_k\propto M_k`$".

**Item 4.** **(7.22)** the table of orders.

## Consistency checks

1. **Dimensions.** With costs and $`\tau,M,G,\mathcal F,\kappa\sigma_X`$ in units of $`1/\lambda`$ and labels dimensionless: (7.15) is $`\lambda^{-2}\cdot\lambda\cdot\lambda^{-1}=\lambda^{-2}`$; (7.16) and each term of (7.43) times $`\kappa^3\mu_3`$ are $`\lambda^{-2}`$, as (4.16); every term of (7.38), (7.40) and the ratios of (7.18), (7.34) are dimensionless. Passed.
2. **One level, a sharp $`X`$, a plain gradient only, a Gaussian start.** $`\alpha_k=\delta_{kk_0}`$: (7.1), (7.2) reduce to the single-level start, $`D=0`$, and (7.8) gives $`P(a)=1/N`$. Sharp $`X`$: $`\varepsilon_\xi=0`$, (7.11) is trivial and (7.14)–(7.17), (7.41)–(7.43) give no term. Plain gradient only: the transport of Step 4 is a rigid shift at the rate $`\mathcal F_k`$, and (7.29) gives $`b_{\perp,k}=0`$ and $`S_\theta=-\tfrac{\sigma\theta'\mathcal F}{2\omega}\sin2\omega\lambda`$, the first-order term of Step 7 with $`\mathcal F=-\varepsilon`$. Real Gaussian start: (7.38) with $`C_g=0`$, $`\delta p=1/(2\delta x)`$ is (7.10); and $`\mathrm{Re}\epsilon_1=\tfrac12\sigma\Delta\nu\lambda\mathrm{Cov}_g(K,\hat p^2)`$ from $`\Theta_1`$ reproduces (7.25), which was obtained from (7.24). Passed.
3. **Short-$`\lambda`$ expansions.** (7.13): the $`\varepsilon^2`$ term of $`v_p`$ at small $`\lambda`$ is $`\tfrac12\lambda^2\sigma(\omega'''-3\omega'\theta'^2-3\omega\theta'\theta'')`$ (double commutator with $`\varepsilon\hat x`$), and (7.13) expanded to $`\lambda^2`$ gives the same; near rest this is $`-\tfrac12\lambda^2v`$, and (7.42) at small $`\lambda`$ gives $`-\lambda v`$ ($`-4-3t+1+2+3t=-1`$), its derivative. (7.43): at $`p=0`$ the $`\varepsilon^3`$ term of the velocity has no term in $`\lambda`$ and none in $`\lambda^3`$ ($`\langle C_0''''\rangle=0`$ at $`p=0`$); in (7.43) the coefficients of $`\lambda`$, $`-\tfrac{t}{4M}(1+\tfrac52t)+\tfrac{t(2+5t)}{8M}`$, and of $`\lambda^3`$, $`tM[\tfrac23(1+t)-\tfrac12(1+t)+\tfrac t4-\tfrac{2+5t}{12}]`$, both vanish, and so does the coefficient of $`\lambda^2`$ in $`\partial_\lambda v_3`$. Passed.

## Open issues

- The third order in the gradients of $`\lvert\Gamma_{kk'}\rvert`$ (case (O3) of (7.36)) is outside the scope and not derived.
- (7.32) and the remainder of (7.25) are order estimates with their calculations; no constants and no bounds are derived for them, apart from (7.29), (7.30), (7.31), (7.37).
- $`R_3`$ in (7.14) is an order estimate without a constant; for $`p_0\neq0`$ in case B only the term of $`v_3`$ with the highest power of $`\lambda`$ is given.
- Terms that mix $`\kappa`$ with the gradients, the order $`\kappa^4`$ and the second order in the gradients of the acceleration are outside the scope; (7.46) is a statement at the retained orders.
- (7.3): the constant $`r`$ of the bound on $`E`$ depends on $`g`$; nothing is stated on $`D`$ at fixed $`\lambda`$ in the sharp-label limit.
- The effect of an operator under the factor on the relation (4.24) outside the class $`\mathcal C`$ needs the clock rate of that body, which is not among the quoted inputs.

## Methods used

- Block decomposition by a conserved label; witness rule for the clock label
- First-order perturbation theory in the gradients; linearity of mixtures
- Continuity equation for the plane-wave label weight, with the boundary term at the cut of the arc
- Taylor's formula with the mean and the variance of the label weight for sharp-label limits
- Reflection symmetry (parity) argument for the order of a deviation
- Interaction picture, Magnus and Baker–Campbell–Hausdorff expansion of a product of unitaries; variance formula for the modulus of an overlap; Cauchy–Schwarz bounds
- Local (quadratic) form of the branch dynamics; Weyl displacement operators; uncertainty inequality with covariance and boundary term
- Exact reduction to a driven two-level problem; Bloch equations; adiabatic expansion with integration by parts
- Window averages; stationary phase and non-stationary phase estimates; dephasing parameter
- Operator norm of the velocity operator; row-sum bound of a circulant matrix
- Invariance under replacements of contract terms (well-definedness)
