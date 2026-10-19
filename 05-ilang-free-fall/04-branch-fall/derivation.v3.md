# Fall of a branch start and level-independent fall

- **Subproject:** 05-ilang-free-fall
- **Package:** 04-branch-fall
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-10

## Changes from previous version

Trigger: `verification.md` (external round 1), issue I1 (minor): the estimate after (4.9) for the correction to an acceleration read off over a window omitted a term.

- **Step 3, paragraph after (4.9), rewritten.** The sentence "An acceleration read off (4.6) over a window ending at $`\lambda`$ therefore carries the correction $`O(\tau L^2\mathsf b'^2\lambda)`$" is withdrawn. Dividing (4.9) by the length of a window that starts at zero keeps both of its terms, and the term $`2\tau L^2\mathsf b'\lvert g_\zeta\rvert`$ does not vanish for a short window. The paragraph now defines the part $`r_L`$ of the velocity beyond first order and gives exact bounds.
- **New (4.30).** An exact bound for the acceleration beyond first order on the fixed chain, for all $`\lambda\ge0`$, derived separately with commutator norms that hold on open chains.
- **New (4.31).** The exact bounds for the correction to a window-averaged acceleration: for a window that starts at zero (from (4.9) and $`r_L(0)=0`$) and for a general window (from (4.30), and from (4.9) at the two ends). With them: the statement that the correction does not vanish for a short window, its exact value at $`\lambda=0`$ in an example, and the range in which the withdrawn estimate follows from (4.9).
- **Follow-up edits.** Result item 1 (one new bullet), Open issues (first item) and the JSON twin (two key results, two definitions, the first open issue, the response to the verification). Step 4 was checked: it contains no sentence that refers to this estimate, and it is unchanged.
- **Unchanged.** Every tagged statement of v2 keeps its tag and its wording, (4.1)–(4.29), (4.9) included. All other text is that of v2.

## Response to verification

- **I1: Accepted and fixed in Step 3** (paragraph after (4.9), new (4.30) and (4.31)), with follow-up edits in the Result (item 1) and in the Open issues (first item). The verifier's computation is confirmed: for $`G=\mathcal F=0`$ the operator $`i[C_1,\hat v_1]`$ is $`\tau^2g_\zeta^2\,\hat x`$ away from the end places, so the correction is present at $`\lambda=0`$ already. The term is retained for windows that start at zero, the endpoint bound is given for general windows, and a separate bound for the acceleration is derived. The bound of (4.31) for a window $`[0,\Lambda]`$ is at most $`4\tau L^2\mathsf b'^2\Lambda`$ if and only if $`\Lambda\,\mathsf b'\ge\lvert g_\zeta\rvert`$; this is the range in which the withdrawn estimate follows from (4.9).

## Setup and assumptions

- **Description (assumption, M8).** A body $`b`$ of the class $`\mathcal C_{\rm lev}`$ with linear level profiles and a medium $`c`$; total contract $`C=C_b\otimes\mathbb 1_c+\kappa\,\hat x\otimes X`$, $`\hat x=\sum_xx\,P_x`$. The single-object term $`C_b`$ is counted in the one pair term $`(b,c)`$ (A5); the position dependence is written into the body's contract (A10). Every control used below is a member of this class with the same medium, hence admissible (A1–A13). $`b`$ and $`c`$ are the only instances of their types, so no swap condition applies. $`\lambda\ge0`$.
- **Start (assumption, M9).** $`\phi_L\otimes\chi`$, with $`\phi_L`$ the branch start $`B_{k,\sigma}[g]`$ placed on the chain as in Step 1(iv). The start is a branch vector of the zeroth-order block and is not adapted to the gradients. A sharp-label limit is taken along a family of such starts (Step 4); where a result needs a class of families, the class is an assumption on the starts and is named in the statement.
- **Inputs, as quoted in question.md.** (5.5), (5.6), (5.11) of 04-ilang-time/05-moving-clock; (8.1), (8.19), (8.20) of 04-ilang-time/08-maximal-speed; (17.15) of 03-ilang-space/17-motion; (3.2), (3.5), (3.9), (3.15), (3.23), (3.26)–(3.28) of 03-clock-and-fall; (3.6) and (3.36) are quoted there as well and are not needed. Steps of those packages needed for $`\mathcal C_{\rm lev}`$ are rederived here.
- **Notation.** Inside one level the index $`k`$ is dropped: $`\tau,M,G,\mathcal F,g_\zeta,\omega,\theta`$. $`\mathsf b:=\lvert G\rvert+M\lvert g_\zeta\rvert+\lvert\mathcal F\rvert`$, $`\mathsf b':=\lvert G\rvert+\tau\lvert g_\zeta\rvert+\lvert\mathcal F\rvert`$. $`\xi_g(p):=-\mathrm{Im}(g^*g')`$, the position density of the start, $`\int\frac{\mathrm dp}{2\pi}\xi_g=\bar x_{\rm lab}(0)`$. $`X_g:=\bigl(\int\frac{\mathrm dp}{2\pi}\lvert g'\rvert^2\bigr)^{1/2}`$. A prime is $`\partial_p`$. $`\Xi_g`$, sharp-label families and the classes $`\mathcal K_1(x_c,\beta)`$, $`E`$, $`E_\infty`$: Step 4, (4.26).
- **Standard facts used.** First-order perturbation theory (Duhamel formula) for $`e^{-i(C_0+C_1)\lambda}`$; on plane-wave amplitudes $`\hat x=i\partial_p`$; Riemann–Lebesgue and stationary phase for $`\int e^{2i\omega\lambda}R\,\mathrm dp`$ with smooth $`R`$ and non-degenerate stationary points; weak convergence of measures; the zeros of an entire function that is not identically zero are isolated.

## Derivation

### Step 1. Reduction to one level block

**(i) Records.** With the spectral decomposition $`X=\sum_\xi\xi\,Q_\xi`$, $`C=\sum_\xi(C_b+\kappa\xi\hat x)\otimes Q_\xi`$, hence exactly

```math
p_x(\lambda)=\sum_\xi\lVert Q_\xi\chi\rVert^2\,p^{[\xi]}_x(\lambda),
\qquad\text{(4.1)}
```

where $`p^{[\xi]}`$ are the place weights of the body alone under $`C_b+\kappa\xi\hat x`$, that is with the plain gradients $`\mathcal F^{\rm body}_k-\kappa\xi`$. Expanding in $`\xi-\langle X\rangle`$, the linear term averages to zero. Therefore $`\bar x_{\rm lab}=\bar x_{\rm lab}[C_{\rm eff}]+O(\kappa^2\sigma_X^2)`$ at fixed $`\lambda`$, chain and start, with $`C_{\rm eff}=C_b+\kappa\langle X\rangle\hat x`$ of (8.19); the term of first order in $`\kappa`$ beyond $`C_{\rm eff}`$ vanishes exactly, and what is neglected is $`\tfrac12\kappa^2\sigma_X^2\,\partial_{\mathcal F}^2\bar x_{\rm lab}`$ plus higher central moments of $`X`$ (order estimate). From here on all profiles are those of $`C_{\rm eff}`$: $`\mathcal F_k=\mathcal F_k^{\rm body}-\kappa\langle X\rangle`$. $`C_{\rm eff}`$ is the same operator for every listing of the contract terms related by (8.1), place-dependent $`\alpha_h`$ included, and changes by a multiple of $`\mathbb 1`$ under $`Z`$ (8.20).

**(ii) Level block.** $`C_{\rm eff}`$ and the records conserve the level, so a start with the clock label in $`\lvert f_k\rangle`$ evolves by $`C^{(k)}`$. On the infinite chain $`\sum_xR_x=e^{-i\hat p}`$ and $`\sum_x(x+\tfrac12)R_x=\tfrac12\{\hat x,e^{-i\hat p}\}`$, so for the linear level profiles, exactly (this is (3.9) with $`\tau\to\tau_k`$, $`g_\zeta\to g_{\zeta,k}`$, $`\mathcal F\to\mathcal F_k`$),

```math
C^{(k)}=C_0+C_1,\quad C_0=-\tau\sin\hat p\,\sigma_1+M\sigma_3,\quad C_1=\tfrac12\{\hat x,B(\hat p)\},\quad B(p)=-g_\zeta\tau\sin p\,\sigma_1+G\sigma_3-\mathcal F .
\qquad\text{(4.2)}
```

**(iii) Velocity.** The records commute with $`\hat x`$, so $`\mathrm d\bar x_{\rm lab}/\mathrm d\lambda=\langle\hat v\otimes\mathbb 1_c\rangle`$ with $`\hat v=i[C^{(k)},\hat x]`$ on the level $`k`$. With $`\hat x=i\partial_p`$, $`i[F(\hat p),\hat x]=F'(\hat p)`$, and $`\partial_pB=g_\zeta V_0`$:

```math
\hat v=V_0(\hat p)+\hat v_1,\qquad V_0(p):=\partial_pC_0(p)=-\tau\cos p\,\sigma_1,\qquad \hat v_1=\tfrac{g_\zeta}{2}\{\hat x,V_0(\hat p)\}.
\qquad\text{(4.3)}
```

**(iv) Finite chain and long-chain limit.** The position amplitudes $`\phi(x)`$ of $`B_{k,\sigma}[g]`$ decay faster than any power of $`\lvert x\rvert`$ ($`g\beta_{k,\sigma}`$ is smooth and periodic). On the chain $`\lvert x\rvert\le L`$ (open ends, hopping terms $`x=-L,\dots,L-1`$) the start is $`\phi_L:=\mathbb 1_{\lvert x\rvert\le L}\phi/\lVert\mathbb 1_{\lvert x\rvert\le L}\phi\rVert`$. The velocity $`v_L(\lambda)`$ is an entire function of the gradients; $`v_L^{(0)}`$ is its value and $`v_L^{(1)}`$ its differential at zero gradients, a linear form in $`(G,\mathcal F,g_\zeta)`$. By the finite-propagation estimate $`\lvert\langle x\rvert e^{-iC_0s}\lvert y\rangle\rvert\le e^{(\tau+M)s}\,((\tau+M)s)^{\lvert x-y\rvert}/\lvert x-y\rvert!`$ and the decay of $`\phi`$, the Duhamel expressions of Step 3 on the finite chain converge to those on the infinite chain: $`v^{(j)}_L(\lambda)\to v^{(j)}(\lambda)`$, $`j=0,1`$, for $`L\to\infty`$ at fixed $`\lambda`$ and $`g`$, faster than any power of $`1/L`$, not uniformly in $`\lambda`$. All formulas below are these limits.

### Step 2. Branch basis

Write a two-component amplitude as $`\sum_{\sigma}c_\sigma(p)\beta_{k,\sigma}(p)`$ and let $`\rho_1,\rho_2,\rho_3`$ be the Pauli matrices on $`(c_+,c_-)`$. The $`\beta_{k,\pm}`$ of (5.6) are real, $`\beta_+'=\tfrac{\theta'}2\beta_-`$, $`\beta_-'=-\tfrac{\theta'}2\beta_+`$, and $`\langle\beta_\pm\rvert\vec\sigma\lvert\beta_\pm\rangle=\pm(\sin\theta,0,\cos\theta)`$, $`\langle\beta_+\rvert\sigma_1\lvert\beta_-\rangle=\cos\theta`$, $`\langle\beta_+\rvert\sigma_3\lvert\beta_-\rangle=-\sin\theta`$, with $`\cos\theta=M/\omega`$, $`\sin\theta=-\tau\sin p/\omega`$. Hence, exactly,

```math
\hat x=i\partial_p+\tfrac{\theta'}2\rho_2,\qquad C_0=\omega\rho_3,\qquad V_0=\omega'\rho_3+u\,\rho_1,\qquad B=-\mathcal F+B_\parallel\rho_3+B_\perp\rho_1,
\qquad\text{(4.4)}
```

```math
\omega'=\frac{\tau^2\sin p\cos p}{\omega},\quad \theta'=-\frac{\tau M\cos p}{\omega^2},\quad u=\omega\theta',\quad B_\parallel=\frac{g_\zeta\tau^2\sin^2p+GM}{\omega},\quad B_\perp=\frac{\tau\sin p\,(G-g_\zeta M)}{\omega},
```

and, since $`\rho_2`$ anticommutes with $`\rho_1,\rho_3`$, $`C_1=\tfrac12\{i\partial_p,-\mathcal F+B_\parallel\rho_3\}+C_1^{\rm od}`$ with the branch-changing part $`C_1^{\rm od}=\tfrac12\{i\partial_p,B_\perp\}\rho_1-\tfrac{\theta'}2\mathcal F\rho_2`$. Differentiating $`B_\parallel=\langle\beta_+\rvert B\lvert\beta_+\rangle+\mathcal F`$ gives the identity $`B_\parallel'=g_\zeta\omega'+\theta'B_\perp`$.

### Step 3. Velocity of a branch start to first order (item 1a)

The start is $`c(0)=g\,e_\sigma`$. By the Duhamel formula, $`\psi=\psi_0+\psi_1+O(2)`$ with $`\psi_0(\lambda)=g\,e^{-i\sigma\omega\lambda}e_\sigma`$, $`\psi_1(\lambda)=-i\int_0^\lambda\mathrm ds\,e^{-iC_0(\lambda-s)}C_1\psi_0(s)`$, and $`v^{(0)}=\langle\psi_0\rvert V_0\lvert\psi_0\rangle`$, $`v^{(1)}=\langle\psi_0\rvert\hat v_1\lvert\psi_0\rangle+2\mathrm{Re}\langle\psi_0\rvert V_0\lvert\psi_1\rangle`$.

1. Zeroth order, exactly and for all $`\lambda`$ (only $`\omega'\rho_3`$ has a diagonal element):
```math
v^{(0)}(\lambda)=\sigma\,\langle\omega_k'\rangle_g\qquad(\text{constant in }\lambda).
\qquad\text{(4.5)}
```
2. With $`i\partial_p(e^{-i\sigma\omega s}g)=e^{-i\sigma\omega s}(ig'+\sigma\omega'sg)`$: $`\langle\psi_0\rvert\hat v_1\lvert\psi_0\rangle=g_\zeta\bigl[\lambda\langle\omega'^2\rangle_g+\sigma\int\frac{\mathrm dp}{2\pi}\omega'\xi_g\bigr]`$.
3. Same-branch part of $`\psi_1`$, with $`b_\sigma:=-\mathcal F+\sigma B_\parallel`$: $`\psi_1^{\sigma}=-ie^{-i\sigma\omega\lambda}\bigl[\lambda(ib_\sigma g'+\tfrac i2b_\sigma'g)+\tfrac{\lambda^2}2\sigma\omega'b_\sigma g\bigr]`$. Its contribution is $`2\sigma\mathrm{Re}\langle\psi_0\rvert\omega'\lvert\psi_1^\sigma\rangle=\sigma\lambda\int\frac{\mathrm dp}{2\pi}\omega'(b_\sigma\lvert g\rvert^2)'=-\sigma\lambda\langle\omega''b_\sigma\rangle_g`$; the $`\lambda^2`$ term is imaginary and drops out.
4. Other-branch part: $`\psi_1^{-\sigma}=-ie^{i\sigma\omega\lambda}\int_0^\lambda\mathrm ds\,e^{-2i\sigma\omega s}\bigl[q+\sigma\omega'B_\perp g\,s\bigr]`$, $`q:=iB_\perp g'+\tfrac i2(B_\perp'-\sigma\theta'\mathcal F)g`$. With $`\int_0^\lambda e^{-2i\sigma\omega s}\mathrm ds=\frac{1-e^{-2i\sigma\omega\lambda}}{2i\sigma\omega}`$ and $`\int_0^\lambda s\,e^{-2i\sigma\omega s}\mathrm ds=\frac{i\sigma\lambda e^{-2i\sigma\omega\lambda}}{2\omega}-\frac{1-e^{-2i\sigma\omega\lambda}}{4\omega^2}`$, the contribution is $`2\mathrm{Re}\langle\psi_0\rvert u\lvert\psi_1^{-\sigma}\rangle=\lambda\langle\theta'\omega'B_\perp\rangle_g+\sigma\mathrm{Re}\int\frac{\mathrm dp}{2\pi}(e^{2i\sigma\omega\lambda}-1)R_\sigma`$. The term $`s\,e^{-2i\sigma\omega s}`$ meets the phase $`e^{2i\sigma\omega\lambda}`$ of $`\langle\psi_0\rvert\cdots e^{i\sigma\omega\lambda}`$ and gives a part that is linear in $`\lambda`$ and does not oscillate.

Adding 2–4 and using $`B_\parallel'=g_\zeta\omega'+\theta'B_\perp`$, exactly for all $`\lambda\ge0`$ and every smooth $`g`$:

```math
v^{(1)}(\lambda)=\lambda\,\langle a_{k,\sigma}\rangle_g+\rho(\lambda),\qquad
\rho(\lambda)=\underbrace{\sigma\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\,B_\parallel'\,\xi_g}_{=:\rho_\infty}+\sigma\mathrm{Re}\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\,e^{2i\sigma\omega\lambda}R_\sigma(p),
\qquad\text{(4.6)}
```

```math
R_\sigma:=-i\theta'\Bigl[B_\perp\,g^*g'+\tfrac12\bigl(\omega(B_\perp/\omega)'-\sigma\theta'\mathcal F\bigr)\lvert g\rvert^2\Bigr],
```

with the coefficient $`a_{k,\sigma}=g_\zeta\omega'^2+\theta'\omega'B_\perp-\sigma\omega''b_\sigma=\omega'B_\parallel'-\omega''B_\parallel+\sigma\mathcal F\omega''`$. With $`\omega\omega'=\tau^2\sin p\cos p`$, $`\omega'^2+\omega\omega''=\tau^2\cos2p`$ and $`\omega''=\tau^2(M^2\cos2p-\tau^2\sin^4p)/\omega^3`$:

```math
\boxed{\;a_{k,\sigma}(p)=\frac{g_{\zeta,k}\tau_k^4\sin^2p-G_kM_k\tau_k^2\cos2p}{\omega_k^2}+\sigma\,\mathcal F_k\,\frac{\tau_k^2\bigl(M_k^2\cos2p-\tau_k^2\sin^4p\bigr)}{\omega_k^3}\;},\qquad\lvert a_{k,\sigma}(p)\rvert\le\frac{\tau_k^2}{M_k}\,\mathsf b_k .
\qquad\text{(4.7)}
```

**The rest $`\rho`$.** It is bounded for all $`\lambda\ge0`$: with $`\lvert\theta'\rvert\le\tau/M`$, $`\lvert\omega'\rvert\le\tau`$, $`\lvert B_\perp\rvert\le\lvert G-g_\zeta M\rvert`$, $`\lvert\omega(B_\perp/\omega)'\rvert\le\frac\tau M\lvert G-g_\zeta M\rvert`$, $`\lvert\xi_g\rvert\le\lvert g\rvert\lvert g'\rvert`$ and the Cauchy–Schwarz inequality,

```math
\lvert\rho(\lambda)\rvert\le\frac{\tau}{M}\,\mathsf b\,\Bigl(3X_g+\frac{\tau}{2M}\Bigr),\qquad\lvert\rho(\lambda)-\rho_\infty\rvert\le\frac{\tau}{M}\,\mathsf b\,\Bigl(X_g+\frac{\tau}{2M}\Bigr)\qquad(\text{exact, all }\lambda\ge0),
\qquad\text{(4.8)}
```

where $`X_g\le(\sum_xx^2p_x(0))^{1/2}`$ because $`\lVert\hat x\psi\rVert^2=X_g^2+\tfrac14\langle\theta'^2\rangle_g`$. It does not grow: no power of $`\lambda`$ multiplies the oscillating integral, since a branch start has no zeroth-order amplitude in the other branch. For $`\lambda\to\infty`$, $`\rho(\lambda)\to\rho_\infty`$ with $`\rho(\lambda)-\rho_\infty=O(\lambda^{-1/2})`$ (order estimate, constant depending on $`g`$): the phase $`2\omega\lambda`$ is stationary only at $`p\in\{0,\pm\tfrac\pi2,\pi\}`$, where $`\omega''\neq0`$, and labels with different $`\omega(p)`$ dephase. $`\rho_\infty`$ is the change of the velocity $`\sigma\omega'`$ due to the local parameters at the position of the start; it shifts by $`\sigma x_c\langle B_\parallel'\rangle_g`$ when the start is translated by $`x_c`$.

**Beyond first order (fixed chain).** On the chain $`\lvert x\rvert\le L`$, $`\lVert C_1\rVert\le L\,\mathsf b'`$, $`\lVert V_0\rVert\le\tau`$, $`\lVert\hat v_1\rVert\le\tau\lvert g_\zeta\rvert L`$ (open ends included) and $`\lVert\psi-\psi_0\rVert\le\lambda\lVert C_1\rVert`$, $`\lVert\psi-\psi_0-\psi_1\rVert\le\tfrac12\lambda^2\lVert C_1\rVert^2`$, so

```math
\bigl\lvert v_L(\lambda)-v_L^{(0)}(\lambda)-v_L^{(1)}(\lambda)\bigr\rvert\le2\tau L^2\,\mathsf b'\,\bigl(\lambda^2\mathsf b'+\lambda\lvert g_\zeta\rvert\bigr)\qquad(\text{exact, all }\lambda\ge0).
\qquad\text{(4.9)}
```

This bound grows with $`\lambda`$ and with $`L`$. It contains a term that is linear in $`\lambda`$, so the correction to an acceleration that follows from it does not vanish for a short window. Let $`r_L(\lambda):=v_L(\lambda)-v_L^{(0)}(\lambda)-v_L^{(1)}(\lambda)`$ be the part of the velocity beyond first order. $`r_L(0)=0`$ exactly, because $`\hat v`$ is of first degree in the gradients and $`\psi_1(0)=0`$. The part of the acceleration beyond first order is $`\mathrm dr_L/\mathrm d\lambda`$, and that of the acceleration averaged over a window $`[\lambda_1,\lambda_1+\Lambda]`$ is $`\bigl(r_L(\lambda_1+\Lambda)-r_L(\lambda_1)\bigr)/\Lambda`$.

**Acceleration beyond first order (fixed chain).** $`\mathrm dv_L/\mathrm d\lambda=\langle\psi\rvert\hat a\lvert\psi\rangle`$ with $`\hat a:=i[C^{(k)},\hat v]=\hat a_0+\hat a_1+\hat a_2`$, where $`\hat a_0:=i[C_0,V_0]`$, $`\hat a_1:=i[C_0,\hat v_1]+i[C_1,V_0]`$ and $`\hat a_2:=i[C_1,\hat v_1]`$ are of degree $`0`$, $`1`$, $`2`$ in the gradients. $`v_L`$ is entire in the gradients, so the derivative of each order is the order of the derivative, and

```math
\frac{\mathrm dr_L}{\mathrm d\lambda}=\langle\psi\rvert\hat a_2\lvert\psi\rangle+\Bigl(\langle\psi\rvert\hat a_1\lvert\psi\rangle-\langle\psi_0\rvert\hat a_1\lvert\psi_0\rangle\Bigr)+\Bigl(\langle\psi\rvert\hat a_0\lvert\psi\rangle-\langle\psi_0\rvert\hat a_0\lvert\psi_0\rangle-2\mathrm{Re}\langle\psi_0\rvert\hat a_0\lvert\psi_1\rangle\Bigr).
```

With $`\lVert[A,B]\rVert\le2\lVert A\rVert\lVert B\rVert`$, $`\lVert C_0\rVert\le\tau+M`$ and the norms above (open ends included): $`\lVert\hat a_0\rVert\le2\tau(\tau+M)`$, $`\lVert\hat a_1\rVert\le2\tau L\bigl(\mathsf b'+(\tau+M)\lvert g_\zeta\rvert\bigr)`$, $`\lVert\hat a_2\rVert\le2\tau L^2\mathsf b'\lvert g_\zeta\rvert`$. The three terms are bounded by $`\lVert\hat a_2\rVert`$, $`2\lVert\hat a_1\rVert\lambda\lVert C_1\rVert`$ and $`2\lVert\hat a_0\rVert\lambda^2\lVert C_1\rVert^2`$, so

```math
\Bigl\lvert\frac{\mathrm dr_L}{\mathrm d\lambda}(\lambda)\Bigr\rvert\le\mathcal R_L(\lambda):=2\tau L^2\,\mathsf b'\,\Bigl[\lvert g_\zeta\rvert+2\lambda\bigl(\mathsf b'+(\tau+M)\lvert g_\zeta\rvert\bigr)+2(\tau+M)\,\lambda^2\,\mathsf b'\Bigr]\qquad(\text{exact, all }\lambda\ge0).
\qquad\text{(4.30)}
```

**Correction to an acceleration read off over a window.** For a window that starts at zero, from (4.9) and $`r_L(0)=0`$. For a general window, from (4.30), which increases with $`\lambda`$, and from (4.9) at the two ends:

```math
\begin{aligned}
\text{window }[0,\Lambda]:\quad&\Bigl\lvert\frac{r_L(\Lambda)}{\Lambda}\Bigr\rvert\le2\tau L^2\,\mathsf b'\,\bigl(\Lambda\,\mathsf b'+\lvert g_\zeta\rvert\bigr),\\
\text{window }[\lambda_1,\lambda_2],\ \lambda_2=\lambda_1+\Lambda:\quad&\Bigl\lvert\frac{r_L(\lambda_2)-r_L(\lambda_1)}{\Lambda}\Bigr\rvert\le\min\Bigl\{\mathcal R_L(\lambda_2),\ \frac{2\tau L^2\,\mathsf b'}{\Lambda}\bigl[(\lambda_1^2+\lambda_2^2)\,\mathsf b'+(\lambda_1+\lambda_2)\lvert g_\zeta\rvert\bigr]\Bigr\}\\
&(\text{exact, all }\lambda_1\ge0,\ \Lambda>0).
\end{aligned}
\qquad\text{(4.31)}
```

Both bounds are of second degree in the gradients and bound everything beyond first order. They are not uniform in $`L`$. Neither vanishes for a short window: for $`\Lambda\to0`$ the first tends to $`2\tau L^2\mathsf b'\lvert g_\zeta\rvert`$ and the second to $`\mathcal R_L(\lambda_1)\ge2\tau L^2\mathsf b'\lvert g_\zeta\rvert`$. A bound that vanishes for $`\Lambda\to0`$ is obtained only if $`g_\zeta=0`$ and the window starts at zero (then it is $`2\tau L^2\mathsf b'^2\Lambda`$), or if all gradients vanish. For a window $`[0,\Lambda]`$ the bound is at most $`4\tau L^2\mathsf b'^2\Lambda`$ if and only if $`\Lambda\,\mathsf b'\ge\lvert g_\zeta\rvert`$.

The term that is constant in the window is not an artefact of the bounds. At $`\lambda=0`$, exactly, $`\mathrm dr_L/\mathrm d\lambda=\langle\phi_L\rvert\hat a_2\lvert\phi_L\rangle`$. For $`G=\mathcal F=0`$, $`C_1=-\tfrac{i\tau g_\zeta}2\sum_xc_x(R_x-R_x^\dagger)\,\sigma_1`$ and $`\hat v_1=-\tfrac{\tau g_\zeta}2\sum_xc_x(R_x+R_x^\dagger)\,\sigma_1`$ with $`c_x=x+\tfrac12`$, and $`\bigl[\sum_xc_x(R_x-R_x^\dagger),\sum_yc_y(R_y+R_y^\dagger)\bigr]=2\sum_x(c_{x-1}^2-c_x^2)P_x=-4\hat x`$ apart from the two end places. Hence $`\hat a_2=\tau^2g_\zeta^2\,\hat x`$ apart from the end places, whose weights in $`\phi_L`$ decay faster than any power of $`1/L`$, and

```math
G=\mathcal F=0:\qquad\frac{\mathrm dr_L}{\mathrm d\lambda}(0)\ \xrightarrow[L\to\infty]{}\ \tau^2g_\zeta^2\,\bar x_{\rm lab}(0),
```

which is not zero for $`g_\zeta\neq0`$ and a start with $`\bar x_{\rm lab}(0)\neq0`$, for example a start translated by $`x_c\neq0`$. The second order in the gradients is outside the scope; (4.6)–(4.8) are statements about the first-order coefficient in the stated order of limits.

### Step 4. Long window and sharp label (item 1b)

The first-order acceleration is $`a^{(1)}(\lambda):=\mathrm dv^{(1)}/\mathrm d\lambda=\langle a_{k,\sigma}\rangle_g+\rho'(\lambda)`$.

**Families of starts.** A *sharp-label family at $`p_0`$* is a sequence of branch starts $`B_{k,\sigma}[g]`$, all concentrated at $`p_0`$, with $`\delta p\to0`$; nothing else is assumed. For it $`\lvert g\rvert^2\frac{\mathrm dp}{2\pi}\to\delta_{p_0}`$ weakly (Chebyshev's inequality), so $`\langle F\rangle_g\to F(p_0)`$ for every continuous periodic $`F`$. The start enters (4.6) also through $`\xi_g`$, which $`\delta p\to0`$ does not fix. For smooth periodic $`F`$ let

```math
\Xi_g[F]:=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\,\xi_g(p)\,F(p),\qquad
\mathcal K_1(x_c,\beta):\ \text{sharp-label families with}\ \ \Xi_g[F]\ \xrightarrow[\delta p\to0]{}\ x_c\,F(p_0)+\beta\,F'(p_0)\ \ \text{for every smooth periodic }F .
\qquad\text{(4.26)}
```

Here $`x_c,\beta\in\mathbb R`$, and necessarily $`x_c=\lim\bar x_{\rm lab}(0)`$, $`\beta=\lim\Xi_g[\sin(p-p_0)]`$. A family of $`\mathcal K_1(x_c,0)`$ is *centred at $`x_c`$*. The class is a property of the starts, not of the contract (M9). Examples: for $`x_c\in\mathbb Z`$, $`\mu\in\mathbb R`$ and real $`\gamma`$, $`g=e^{-ipx_c}e^{-i\mu(1-\cos(p-p_0))}\gamma`$ has $`\xi_g=\bigl(x_c+\mu\sin(p-p_0)\bigr)\lvert g\rvert^2`$. With $`\mu=0`$ and any real $`\gamma`$ of spread $`\delta p\to0`$ the family is centred at $`x_c`$. The family $`E(x_c,\mu)`$ has $`\gamma(p_0+y)=(2\pi/\epsilon)^{1/2}\Gamma_0(y/\epsilon)`$ for $`\lvert y\rvert\le\pi`$, with a fixed real, smooth, even $`\Gamma_0`$ supported in $`[-1,1]`$, $`\int\Gamma_0^2=1`$, and $`\epsilon\to0`$; then $`\delta p\propto\epsilon`$ and, by Taylor expansion, $`\Xi_g[F]=x_c\langle F\rangle_g+\mu\,\delta p^2\bigl[F'(p_0)+O(\delta p^2)\bigr]`$. So $`E`$ with $`\mu\,\delta p^2\to\beta`$ belongs to $`\mathcal K_1(x_c,\beta)`$, and for $`E`$ with $`\mu\,\delta p^2\to\infty`$, called $`E_\infty`$, $`\Xi_g[F]`$ diverges whenever $`F'(p_0)\neq0`$.

1. **Long window at fixed $`g`$.** $`\overline{a^{(1)}}=\bigl[v^{(1)}(\lambda_1+\Lambda)-v^{(1)}(\lambda_1)\bigr]/\Lambda`$, so by (4.6), (4.8), for all $`\lambda_1\ge0`$, $`\Lambda>0`$:
```math
\Bigl\lvert\overline{a^{(1)}}-\langle a_{k,\sigma}\rangle_g\Bigr\rvert\le\frac{2\tau}{M\Lambda}\,\mathsf b\,\Bigl(X_g+\frac{\tau}{2M}\Bigr)\ \ (\text{exact}),\qquad\lim_{\Lambda\to\infty}\overline{a^{(1)}}=\langle a_{k,\sigma}\rangle_g .
\qquad\text{(4.10)}
```
2. **Then sharp label (every sharp-label family; no class is needed).** On the arc $`(p_0-\pi,p_0+\pi]`$ the weight has mean $`p_0`$, so the linear Taylor term of $`a_{k,\sigma}`$ averages to zero:
```math
\bigl\lvert\langle a_{k,\sigma}\rangle_g-a_{k,\sigma}(p_0)\bigr\rvert\le\tfrac12\sup_p\lvert a_{k,\sigma}''\rvert\,\delta p^2\ \ (\text{exact}),\qquad\text{drift acceleration}=\lim_{\delta p\to0}\lim_{\Lambda\to\infty}\overline{a^{(1)}}=a_{k,\sigma}(p_0).
\qquad\text{(4.11)}
```
3. **Sharp label at fixed $`\lambda`$.** With $`g^*g'=\tfrac12(\lvert g\rvert^2)'-i\xi_g`$ and one integration by parts in (4.6), exactly,
```math
v^{(1)}(\lambda)=\Bigl\langle a_{k,\sigma}\lambda-\lambda\,n_k\cos(2\omega\lambda)-\tfrac12\bigl(\tfrac{u'}{\omega}B_\perp+\sigma\theta'^2\mathcal F\bigr)\sin(2\omega\lambda)\Bigr\rangle_g+\sigma\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\,\xi_g\bigl[B_\parallel'-\theta'B_\perp\cos(2\omega\lambda)\bigr],
\qquad\text{(4.12)}
```
```math
n_k(p):=\omega'\theta'B_\perp=-\frac{\tau^4M\,(G-g_\zeta M)\,\sin^2(2p)}{4\,\omega^4}.
```
Differentiating in $`\lambda`$, with $`A_\sigma:=(u'+\theta'\omega')B_\perp+\sigma\omega\theta'^2\mathcal F`$ and $`w:=2\omega\theta'B_\perp=-\tau^2M(G-g_\zeta M)\sin2p/\omega^2`$ (so $`\omega'w=2\omega n_k`$):
```math
\begin{aligned}
&a^{(1)}(\lambda)=\Bigl\langle a_{k,\sigma}-A_\sigma\cos(2\omega\lambda)+\omega'w\,\lambda\sin(2\omega\lambda)\Bigr\rangle_g+\sigma\,\Xi_g\bigl[w\sin(2\omega\lambda)\bigr]\qquad(\text{exact, every smooth }g,\ \text{all }\lambda\ge0);\\
&\text{every sharp-label family:}\quad\lim_{\delta p\to0}a^{(1)}(\lambda)\ \text{exists}\iff\lim_{\delta p\to0}\Xi_g\bigl[w\sin(2\omega\lambda)\bigr]\ \text{exists}.
\end{aligned}
\qquad\text{(4.27)}
```
The second line holds in both directions because the average $`\langle\cdot\rangle_g`$ converges to the value of its argument at $`p_0`$ for every sharp-label family; the limit is then that value plus $`\sigma\lim\Xi_g[w\sin(2\omega\lambda)]`$. Evaluating $`\Xi_g`$ by (4.26), and using $`w\equiv0`$, $`A_\sigma=\sigma\omega\theta'^2\mathcal F`$ for $`G=g_\zeta M`$:
```math
\begin{aligned}
\text{families of }\mathcal K_1(x_c,\beta):\quad a^{(1)}_{\rm sharp}(\lambda)&=\Bigl[a_{k,\sigma}-A_\sigma\cos(2\omega\lambda)+w\,(\omega'\lambda+\sigma x_c)\sin(2\omega\lambda)+\sigma\beta\bigl(w'\sin(2\omega\lambda)+2\omega'w\,\lambda\cos(2\omega\lambda)\bigr)\Bigr]_{p=p_0},\\
G_k=g_{\zeta,k}M_k,\ \text{every sharp-label family}:\quad a^{(1)}_{\rm sharp}(\lambda)&=\Bigl[a_{k,\sigma}-\sigma\,\omega\,\theta'^2\mathcal F\cos(2\omega\lambda)\Bigr]_{p=p_0}.
\end{aligned}
\qquad\text{(4.13)}
```
For centred families ($`\beta=0`$) the first line is $`\bigl[a_{k,\sigma}-A_\sigma\cos(2\omega\lambda)+2\omega\theta'B_\perp(\omega'\lambda+\sigma x_c)\sin(2\omega\lambda)\bigr]_{p_0}`$. Already within $`\mathcal K_1`$ the limit depends on the family through $`\beta`$, also at rest if $`G_k\neq g_{\zeta,k}M_k`$ (there $`w=0`$ and $`w'\neq0`$). Outside these classes it need not exist: for $`G_k\neq g_{\zeta,k}M_k`$ and the family $`E_\infty`$ it does not exist, at every $`p_0`$ and for all $`\lambda`$ outside a discrete set. Indeed $`\partial_p\bigl(w\sin(2\omega\lambda)\bigr)_{p_0}=w'\sin(2\omega\lambda)+2\omega'w\,\lambda\cos(2\omega\lambda)`$ is an entire function of $`\lambda`$ that is not identically zero, since $`\omega'w=2\omega n_k\neq0`$ for $`\sin2p_0\neq0`$, and $`w'(p_0)=-2\tau^2M(G-g_\zeta M)\cos(2p_0)/\omega^2\neq0`$ for $`\sin2p_0=0`$ (rest included). For other families outside $`\mathcal K_1`$ only (4.27) is established.
4. **The two orders.** Let $`\lambda_2:=\lambda_1+\Lambda`$, $`[f]_{\lambda_1}^{\lambda_2}:=f(\lambda_2)-f(\lambda_1)`$, $`h:=\theta'B_\perp=w/2\omega`$, $`S_\sigma:=\tfrac{u'}{\omega}B_\perp+\sigma\theta'^2\mathcal F`$. From (4.12), in which the term $`\Xi_g[B_\parallel']`$ cancels, exactly for every smooth $`g`$:
```math
\overline{a^{(1)}}=\Bigl\langle a_{k,\sigma}-\frac{n_k}{\Lambda}\bigl[\lambda\cos(2\omega\lambda)\bigr]_{\lambda_1}^{\lambda_2}-\frac{S_\sigma}{2\Lambda}\bigl[\sin(2\omega\lambda)\bigr]_{\lambda_1}^{\lambda_2}\Bigr\rangle_g-\frac{\sigma}{\Lambda}\,\Xi_g\Bigl[h\,\bigl[\cos(2\omega\lambda)\bigr]_{\lambda_1}^{\lambda_2}\Bigr].
\qquad\text{(4.28)}
```
For a family of $`\mathcal K_1(x_c,\beta)`$, with $`\partial_p\bigl(h\cos(2\omega\lambda)\bigr)=h'\cos(2\omega\lambda)-2n_k\lambda\sin(2\omega\lambda)`$, $`\phi_j:=2\omega(p_0)\lambda_j`$ and all functions taken at $`p_0`$:
```math
\lim_{\delta p\to0}\overline{a^{(1)}}=a_{k,\sigma}-n_k\bigl[\cos\phi_2-2\sigma\beta\sin\phi_2\bigr]+\frac{R}{\Lambda},\qquad\lvert R\rvert\le2\lvert n_k\rvert\lambda_1(1+2\lvert\beta\rvert)+\lvert S_\sigma\rvert+2\lvert x_ch+\beta h'\rvert\quad(\text{exact}).
```
If $`n_k(p_0)=0`$ this tends to $`a_{k,\sigma}(p_0)`$ for $`\Lambda\to\infty`$. If $`n_k(p_0)\neq0`$ it has no limit, because $`\cos\phi_2-2\sigma\beta\sin\phi_2=\sqrt{1+4\beta^2}\cos(\phi_2+\phi_\beta)`$ and $`\omega(p_0)>0`$. Hence
```math
\text{families of }\mathcal K_1(x_c,\beta),\ \text{every }x_c,\beta:\qquad\lim_{\Lambda\to\infty}\lim_{\delta p\to0}\overline{a^{(1)}}\ \text{exists}\iff n_k(p_0)=0\iff(G_k-g_{\zeta,k}M_k)\sin^2(2p_0)=0,\ \text{and then equals }a_{k,\sigma}(p_0).
\qquad\text{(4.14)}
```
The limits commute when both orders exist and agree; the order "long window first" exists for every sharp-label family and gives $`a_{k,\sigma}(p_0)`$ (4.11). For all sharp-label families:
```math
\begin{array}{l|l|l|l|l}
\text{level data}&\text{label }p_0&\text{sharp-label family}&\lim_{\Lambda\to\infty}\lim_{\delta p\to0}\overline{a^{(1)}}&\text{commute}\\\hline
G_k=g_{\zeta,k}M_k&\text{every }p_0&\text{every family}&a_{k,\sigma}(p_0)&\text{yes}\\
G_k\neq g_{\zeta,k}M_k&\sin2p_0=0:\ \text{rest},\ \pm\tfrac\pi2,\ \pi&\mathcal K_1(x_c,\beta),\ \text{every }x_c,\beta&a_{k,\sigma}(p_0)&\text{yes}\\
G_k\neq g_{\zeta,k}M_k&\sin2p_0\neq0&\mathcal K_1(x_c,\beta),\ \text{every }x_c,\beta&\text{none: }\limsup,\liminf=a_{k,\sigma}(p_0)\pm\lvert n_k(p_0)\rvert\sqrt{1+4\beta^2}&\text{no}\\
G_k\neq g_{\zeta,k}M_k&\text{every }p_0,\ \text{rest included}&E_\infty&\text{none: the inner limit does not exist}&\text{no}\\
G_k\neq g_{\zeta,k}M_k&\text{every }p_0&\text{any other family}&\text{exists iff (4.28) converges for }\delta p\to0\text{, then for }\Lambda\to\infty&\text{not determined}
\end{array}
\qquad\text{(4.29)}
```
Proofs of the rows. Row 1: $`n_k\equiv h\equiv0`$, so (4.28) is an average $`\langle\cdot\rangle_g`$, which converges for every sharp-label family to $`a_{k,\sigma}(p_0)-\frac{\sigma\theta'^2\mathcal F}{2\Lambda}[\sin(2\omega\lambda)]_{\lambda_1}^{\lambda_2}`$ at $`p_0`$. Rows 2, 3: (4.14); in row 3 what converges is the window average minus the explicit term $`-n_k[\cos\phi_2-2\sigma\beta\sin\phi_2]`$. Row 4: at fixed $`\lambda_1`$, $`\partial_p\bigl(h[\cos(2\omega\lambda)]_{\lambda_1}^{\lambda_2}\bigr)_{p_0}=\bigl[h'\cos(2\omega\lambda)-2n_k\lambda\sin(2\omega\lambda)\bigr]_{\lambda_1}^{\lambda_2}`$ is an entire function of $`\lambda_2`$ that is not identically zero ($`n_k(p_0)\neq0`$, or $`h'(p_0)=-\tau^2M(G-g_\zeta M)\cos(2p_0)/\omega^3\neq0`$ for $`\sin2p_0=0`$), so for all $`\Lambda`$ outside a discrete set $`\Xi_g[\cdot]`$ in (4.28) diverges while the average converges. Row 5: nothing beyond (4.28) is proven.

The reason for the rows "no" in $`\mathcal K_1`$ is that the term $`\lambda\,n_k\cos(2\omega\lambda)`$ of (4.12) dephases only at fixed $`g`$; the bound (4.10) contains $`X_g`$, which diverges for $`\delta p\to0`$. Near rest $`n_k=-(G/M-g_\zeta)v^2+O(v^4)`$ in the variable $`v`$ of Step 6.

### Step 5. Comparison with the bare start $`S_k`$ (item 1c)

At $`p_0=0`$: $`\omega'=B_\perp=B_\parallel'=h=n_k=0`$, $`\theta'=-\tau/M`$, $`A_\sigma=\sigma\tau^2\mathcal F/M`$, $`S_\sigma=\sigma\tau^2\mathcal F/M^2`$, $`h'=-\tau^2(G-g_\zeta M)/M^2`$, $`B_\parallel''=g_\zeta\omega''+h'=\tau^2(2g_\zeta M-G)/M^2`$. Integrating (4.12) over $`[0,\lambda]`$ at fixed $`g`$ and then taking the limit with (4.26), for sharp-label families at rest of the class $`\mathcal K_1(x_c,\beta)`$, every $`x_c`$:

```math
\bar x^{(1)}_{\rm lab}(\lambda)-\bar x_{\rm lab}(0)\ \xrightarrow[\delta p\to0]{}\ \tfrac12\,a_{k,\sigma}(0)\,\lambda^2-\sigma\,\frac{\tau^2\mathcal F}{2M^3}\sin^2(M\lambda)+\sigma\beta\,\frac{\tau^2}{M^2}\Bigl[(2g_\zeta M-G)\,\lambda+(G-g_\zeta M)\,\frac{\sin(2M\lambda)}{2M}\Bigr].
\qquad\text{(4.15)}
```

For centred families ($`\beta=0`$) the right side is $`\tfrac12a_{k,\sigma}(0)\lambda^2-\sigma\frac{\tau^2\mathcal F}{2M^3}\sin^2(M\lambda)`$. Against (3.15) and (3.26), for $`\sigma=+`$:
- the secular term is unchanged at rest, $`a_{k,+}(0)=a_{\rm sec}`$ (every $`g`$); for all labels $`a_{\rm sec}(p)`$ of (3.26) is replaced by $`a_{k,\sigma}(p)`$, and $`a_{\rm sec}(p)=\sum_\sigma w_\sigma a_{k,\sigma}(p)`$ with the branch weights $`w_\pm=\tfrac12(1\pm M/\omega)`$ of the bare label (these are not the function $`w`$ of Step 4; checked term by term with $`\sum_\sigma w_\sigma=1`$, $`\sum_\sigma\sigma w_\sigma=M/\omega`$);
- the term $`\frac{\tau^2G}{2M^2}\lambda\sin(2M\lambda)`$ of (3.15) is absent for every family of $`\mathcal K_1`$ at rest: in (3.26) the term $`\lambda^2A_2`$ is absent and $`A_1`$ is replaced by $`-n_k`$ (every $`g`$, (4.12)), which vanishes at $`p=0`$, whereas $`A_1(0)=\tau^2G/M`$ for $`S_k`$;
- in the term $`\sin^2(M\lambda)`$ the coefficient $`Mg_\zeta-\mathcal F-G`$ is replaced by $`-\mathcal F`$ ($`A_0`$ at $`p=0`$ keeps only its $`\mathcal F`$ part), and $`\langle\nu_0\rangle_W`$ is replaced by $`\rho_\infty`$. For centred families no $`G`$ or $`g_\zeta`$ remains in the oscillation; for $`\beta\neq0`$ the last term of (4.15) adds a constant velocity and an oscillation $`\sin(2M\lambda)`$ that contain them;
- the second limit of (3.28), which does not exist for $`S_k`$ if $`G_k\neq0`$, exists and equals the first for every family of $`\mathcal K_1`$ at rest, and for every sharp-label family if $`G_k=g_{\zeta,k}M_k`$ ((4.14), (4.29)); for $`E_\infty`$ and $`G_k\neq g_{\zeta,k}M_k`$ it does not exist.

Why: the bare label is $`\lvert1\rangle=\cos\tfrac\theta2\,\beta_+-\sin\tfrac\theta2\,\beta_-`$, with the amplitude $`-\sin\tfrac\theta2=\tfrac{\tau p}{2M}+O(p^3)`$ in the lower branch. It vanishes at $`p=0`$, but $`\hat x=i\partial_p`$ in $`C_1`$ and $`\hat v_1`$ differentiates it, so the zeroth-order coherence between the branches contributes at order one for $`W\to\infty`$; with $`G\neq0`$ the beat frequency $`2M_{x,k}`$ varies along the start, which gives $`\lambda\sin(2M\lambda)`$. A branch start has no such coherence. Its branches are mixed only at first order by $`C_1^{\rm od}`$ (Step 2), whose $`G`$ and $`g_\zeta`$ part is proportional to $`B_\perp`$ and vanishes at $`p=0`$ (for $`\beta\neq0`$ its $`p`$-derivative at $`p=0`$ enters, with the weight $`\beta`$); the part $`-\tfrac{\theta'}2\mathcal F\rho_2`$ remains, because the start is not adapted to the gradient $`\mathcal F`$, and it is the same for both starts.

### Step 6. Rest and motion (item 2)

**(a)** The drift acceleration is (4.7) at $`p=p_0`$, for every $`p_0`$; it has the period $`\pi`$ in $`p_0`$. At rest:

```math
\boxed{\;a_{k,\sigma}(0)=\frac{\tau_k^2}{M_k}\,\bigl(\sigma\,\mathcal F_k-G_k\bigr)\;}
\qquad\text{(4.16)}
```

**(b)** $`v:=\sigma\omega_k'(p_0)`$ is the sharp-label limit of (4.5): the velocity of the branch start at zero gradients, in position labels per unit of $`\lambda`$, $`\lvert v\rvert<\tau_k`$. $`a_{k,\sigma}`$ is even and $`v`$ is odd in $`p_0`$, and $`v=\sigma\frac{\tau^2}{M}p_0\,(1+O(p_0^2))`$ is invertible near $`p_0=0`$; on this branch of $`p_0(v)`$, which contains rest, $`a_{k,\sigma}`$ is a smooth function of $`v^2`$ and $`p_0^2=\frac{M^2}{\tau^4}v^2+O(v^4)`$. Expanding (4.7) with $`\cos2p=1-2p^2`$, $`\omega^{-2}=M^{-2}(1-\tau^2p^2/M^2)`$, $`\omega^{-3}=M^{-3}(1-\tfrac{3\tau^2p^2}{2M^2})`$:

```math
a_{k,\sigma}=\frac{\tau^2}{M}(\sigma\mathcal F-G)+c_{2,k,\sigma}\,v^2+O(v^4),\qquad
c_{2,k,\sigma}=g_\zeta+\frac GM\Bigl(1+\frac{2M^2}{\tau^2}\Bigr)-\sigma\,\frac{\mathcal F}{M}\Bigl(\frac32+\frac{2M^2}{\tau^2}\Bigr).
\qquad\text{(4.17)}
```

| gradient | value at $`v=0`$ | coefficient of $`v^2`$ |
| --- | --- | --- |
| $`g_{\zeta,k}`$ | $`0`$ | $`g_{\zeta,k}`$ |
| $`G_k`$ | $`-\tau_k^2G_k/M_k`$ | $`\frac{G_k}{M_k}\bigl(1+\frac{2M_k^2}{\tau_k^2}\bigr)`$ |
| $`\mathcal F_k`$ | $`\sigma\,\tau_k^2\mathcal F_k/M_k`$ | $`-\sigma\frac{\mathcal F_k}{M_k}\bigl(\frac32+\frac{2M_k^2}{\tau_k^2}\bigr)`$ |

The two table columns are exact; $`O(v^4)`$ is an order estimate for $`v\to0`$ at fixed level data. The terms $`2M^2/\tau^2`$ come from $`\cos2p=1-2p^2`$, that is from the lattice.

**(c)** In the manner of (3.2), for the level $`k`$ of $`C_{\rm eff}`$: $`E^\pm_{x,k}=V_{x,k}\pm M_{x,k}`$ (modulo a common constant), gap $`\Delta_{x,k}=2M_{x,k}`$, norm of the hopping block $`t_{x,k}=\tfrac12\tau_k\zeta_{x,k}`$. For the linear profiles the differences $`\delta E^\pm_k=\pm G_k-\mathcal F_k`$, $`\delta\Delta_k=2G_k`$, $`\delta t_k=\tfrac12\tau_kg_{\zeta,k}`$ do not depend on $`x`$; the reference values are $`\Delta_k:=\Delta_{0,k}=2M_k`$ and $`\bar t_k:=\tfrac12(t_{0,k}+t_{-1,k})=\tfrac12\tau_k`$. Then

```math
a_{k,\sigma}(0)=-\sigma\,\frac{8\,\bar t_k^{\,2}}{\Delta_k}\,\delta E^{\sigma}_k,\qquad
c_{2,k,\sigma}=\frac{\delta t_k}{\bar t_k}+\frac{\delta\Delta_k}{\Delta_k}\Bigl(1+\frac{\Delta_k^2}{8\bar t_k^{\,2}}\Bigr)+\sigma\,\frac{\delta E^+_k+\delta E^-_k}{\Delta_k}\Bigl(\frac32+\frac{\Delta_k^2}{8\bar t_k^{\,2}}\Bigr).
\qquad\text{(4.18)}
```

These are functions of $`C_{\rm eff}`$ modulo $`\mathbb 1`$. They are invariant under every replacement (8.1), place-dependent $`\alpha_h`$ included (which leave $`C_{\rm eff}`$ unchanged), under $`Z`$ (which shifts $`C_{\rm eff}`$ by a multiple of $`\mathbb 1`$, (8.20)), and under the common phases of $`\chi`$ and of the state. The values $`E^\pm_{x,k}`$ and $`V_{x,k}`$ themselves are not invariant. The reference values belong to the origin $`x=0`$ of the linear profiles; moving the origin changes (4.18) at second order in the gradients.

### Step 7. Level-independent fall (item 3)

(4.16) and (4.17) hold for every member of $`\mathcal C_{\rm lev}`$ with linear level profiles, every $`N\ge2`$ and all admissible level data. Each statement below is an equality between these numbers, so both directions follow from (4.16), (4.17) alone; (b) also uses that a smooth function of $`v^2`$ fixes its Taylor coefficients.

**(a) From rest.**

```math
\begin{aligned}
a_{k,+}(0)=a_+\ \forall k&\iff\frac{\tau_k^2}{M_k}(\mathcal F_k-G_k)=a_+\ \forall k,\qquad
a_{k,-}(0)=a_-\ \forall k\iff\frac{\tau_k^2}{M_k}(\mathcal F_k+G_k)=-a_-\ \forall k,\\
\text{both, with }a_+=a_-=a&\iff\mathcal F_k=0\ \text{ and }\ \frac{\tau_k^2G_k}{M_k}=-a\quad\forall k .
\end{aligned}
\qquad\text{(4.19)}
```

Both without equal values: $`\tau_k^2\mathcal F_k/M_k=\tfrac12(a_+-a_-)`$ and $`\tau_k^2G_k/M_k=-\tfrac12(a_++a_-)`$ for all $`k`$. In well-defined terms the first condition is that $`\bar t_k^{\,2}\,\delta E^+_k/\Delta_k`$ does not depend on $`k`$, and $`\mathcal F_k=0`$ is $`\delta E^+_k+\delta E^-_k=0`$, the term $`\kappa\langle X\rangle`$ of the records included.

**(b) In motion (upper branch).** $`a_{k,+}`$ is the same function of $`v`$ through the order $`v^2`$ for all $`k`$ if and only if (i) $`\frac{\tau_k^2}{M_k}(\mathcal F_k-G_k)=a_0`$ for all $`k`$ and (ii) $`c_{2,k,+}`$ does not depend on $`k`$. With (i) inserted in (4.17), exactly,

```math
c_{2,k,+}=g_{\zeta,k}-\frac{\mathcal F_k}{2M_k}-\frac{a_0}{\tau_k^2}\Bigl(1+\frac{2M_k^2}{\tau_k^2}\Bigr)\quad\text{independent of }k .
\qquad\text{(4.20)}
```

In the regime $`M_k\ll\tau_k`$: $`c_{2,k,+}=c^{(0)}_{2,k}+\frac{2M_k}{\tau_k^2}(G_k-\mathcal F_k)`$ with $`c^{(0)}_{2,k}:=g_{\zeta,k}+\frac{G_k}{M_k}-\frac{3\mathcal F_k}{2M_k}`$. To leading order the condition is (i), which is unchanged, together with

```math
c^{(0)}_{2,k}=g_{\zeta,k}-\frac{\mathcal F_k}{2M_k}-\frac{a_0}{\tau_k^2}\quad\text{independent of }k;\qquad\text{then exactly}\quad c_{2,k,+}-c_{2,k',+}=-2a_0\Bigl(\frac{M_k^2}{\tau_k^4}-\frac{M_{k'}^2}{\tau_{k'}^4}\Bigr).
\qquad\text{(4.21)}
```

The dropped terms are the lattice terms $`\frac{2M_k}{\tau_k^2}(G_k-\mathcal F_k)=-2a_0M_k^2/\tau_k^4`$, of relative order $`M_k^2/\tau_k^2`$. For the lower branch replace $`\mathcal F_k\to-\mathcal F_k`$.

**(c) The class $`\mathcal C`$** ($`\tau_k=\tau`$, $`M_k=m+d_k`$, $`G_k=mg_m+d_kg_\eta`$, $`\mathcal F_k=\mathcal F`$, $`g_{\zeta,k}=g_\zeta`$). Here $`a_{k,\pm}(0)=-\tau^2\bigl[g_\eta+\frac{m(g_m-g_\eta)\mp\mathcal F}{m+d_k}\bigr]`$, the $`d_k`$ are distinct and $`d\mapsto1/(m+d)`$ is injective. For every $`N\ge2`$:

```math
a_{k,+}(0)\ \text{level-independent}\iff\mathcal F=m(g_m-g_\eta);\qquad a_{k,-}(0)\ \text{level-independent}\iff\mathcal F=-m(g_m-g_\eta);\qquad\text{value }-\tau^2g_\eta\text{ in each case};
\qquad\text{(4.22)}
```

both hold if and only if $`\mathcal F=0`$ and $`g_m=g_\eta`$, and then the two values are equal automatically. Through the order $`v^2`$ (upper branch): (i) gives $`\mathcal F=m(g_m-g_\eta)`$, $`a_0=-\tau^2g_\eta`$, and (4.20) requires $`h(M_k):=-\frac{\mathcal F}{2M_k}+\frac{2g_\eta}{\tau^2}M_k^2`$ to be the same for all $`k`$.

```math
\begin{aligned}
N=2:&\quad\mathcal F=m(g_m-g_\eta)=-\frac{4g_\eta}{\tau^2}\,m\Bigl(m+\frac{\pi}{\lambda_0}\Bigr)\Bigl(2m+\frac{\pi}{\lambda_0}\Bigr),\quad g_\eta,\ g_\zeta\ \text{free};\\
N\ge3:&\quad g_m=g_\eta=0,\ \mathcal F=0,\quad g_\zeta\ \text{free}\quad(\text{so }a_0=0);\\
M_k\ll\tau,\ \text{leading order, every }N\ge2:&\quad\mathcal F=0,\ g_m=g_\eta=:g,\quad g_\zeta\ \text{free}.
\end{aligned}
\qquad\text{(4.23)}
```

Proofs. $`N=2`$: $`h(M_0)=h(M_1)`$ is $`\mathcal F=-\frac{4g_\eta}{\tau^2}M_0M_1(M_0+M_1)`$. $`N\ge3`$: $`h(M)=c`$ is the cubic $`\frac{2g_\eta}{\tau^2}M^3-cM-\tfrac12\mathcal F=0`$, whose roots sum to zero, so it cannot have three distinct positive roots unless it vanishes identically. Leading order: $`g_\zeta+g_\eta-\frac{\mathcal F}{2M_k}`$ is level-independent if and only if $`\mathcal F=0`$. In the last case $`a_{k,\pm}=-\tau^2g+\bigl[g_\zeta+g\bigl(1+\frac{2M_k^2}{\tau^2}\bigr)\bigr]v^2+O(v^4)`$: the level enters only through the lattice term $`2gM_k^2v^2/\tau^2`$. Exactly, for $`N\ge3`$, a fall that is level-independent through the order $`v^2`$ exists in $`\mathcal C`$ only with $`a_0=0`$. (In this step $`h`$ is the function just defined, not $`\theta'B_\perp`$ of Step 4.)

### Step 8. Clock rate and fall in the class $`\mathcal C`$ (item 4)

The rate (3.23) in its wide-start form is $`r(x)=\eta_x/\lambda_0=\frac N{2\pi}(E^+_{x,k+1}-E^+_{x,k})`$ with $`\eta_x=1+g_\eta x`$; it depends on the place if and only if $`g_\eta\neq0`$.

**(a)** A place-dependent rate does not imply a level-independent fall: in the variant (b2) ($`g_\eta=g\neq0`$, the others zero) $`a_{k,+}(0)=-\tau^2g\,d_k/(m+d_k)`$, which is zero for $`k=0`$ and not for $`k\ge1`$. Conversely, by (4.22) a level-independent $`a_{k,+}(0)`$ has the value $`-\tau^2g_\eta`$. So the converse holds exactly when the common value is not zero; it fails when the value is zero, for example Model D, or $`g_\eta=0`$ with $`\mathcal F=m\,g_m\neq0`$ (level-independent, no fall from rest, uniform rate).

**(b)** Let $`a_{k,+}(0)=a\neq0`$ for all $`k`$. By (4.22), $`a=-\tau^2g_\eta`$, and $`g_\eta=\frac{r(x+1)-r(x)}{r(x)}`$ at $`x=0`$ (for other $`x`$ the ratio is $`g_\eta+O(g_\eta^2x)`$). In the background of (17.15) with $`K_x=\kappa xX`$: $`u_x=\kappa x\,e`$, the distance of neighbouring positions is $`d_0:=\kappa\sigma_X`$, $`\bar x=d_0\,\bar x_{\rm lab}\,\hat e`$ with $`\hat e:=e/\sigma_X`$, and (5.11) reads $`v_{\max}=\tau d_0`$. Hence, at first order in the gradients,

```math
\boxed{\;\frac{\mathrm d^2\bar x}{\mathrm d\lambda^2}\Big\vert_{\rm drift}=d_0\,a_{k,+}(0)\,\hat e=-\,\frac{v_{\max}^2}{d_0}\;\frac{r(x+1)-r(x)}{r(x)}\;\hat e\;}
\qquad\text{(4.24)}
```

The relation contains $`v_{\max}`$, $`d_0`$ and the two rates only. $`m`$: no. $`N`$: no. $`\lambda_0`$: no (it cancels in the ratio). $`\tau`$: only inside $`v_{\max}/d_0`$. The level $`k`$: no. The plain gradient $`\mathcal F`$: no; it is fixed by the hypothesis, $`\mathcal F=m(g_m-g_\eta)`$, and $`m`$, $`g_m`$ enter this condition, not the relation. Accuracy: first order in the gradients with the ratio taken at the origin of the profiles; leading order in $`\kappa`$ (both sides are proportional to $`d_0`$; corrections as in Step 1(i)); $`v_{\max}=\tau d_0`$ is the bound (5.11) of the zeroth-order contract, and for $`g_\zeta\neq0`$ its form (17.7) gives $`\tau d_0\max_x\tfrac12(\zeta_x+\zeta_{x-1})`$, a difference of second order in (4.24).

**(c)** Lower branch: $`a_{k,-}(0)=a\neq0`$ for all $`k`$ if and only if $`\mathcal F=-m(g_m-g_\eta)`$ and $`g_\eta\neq0`$, with $`a=-\tau^2g_\eta`$. The relation (4.24) and the list of answers are the same, with the same rate (3.23). The level spacings of the lower on-site eigenvalues are $`E^-_{x,k+1}-E^-_{x,k}=-\frac{2\pi}N\frac{\eta_x}{\lambda_0}`$, of opposite sign and with the same ratio between neighbouring positions. The hypotheses of (b) and (c) differ in the sign of $`\mathcal F`$; they hold together only for $`\mathcal F=0`$, $`g_m=g_\eta`$.

**(d)** $`r(x)`$ and $`r(x+1)`$ are the rates (3.23) of two runs of the same description, with the starts $`S_{\rm clock}(x)`$ and $`S_{\rm clock}(x+1)`$. Each is the advance of the clock distribution per unit of $`\lambda`$, taken from readings of the clock label applied at stated values of $`\lambda`$. Comparing them relies on A8 (readings at stated $`\lambda`$, comparison at equal $`\lambda`$ through the order of $`\lambda`$) and on the contract being the same in both runs; $`\lambda`$ is not a time (M1). Only the ratio enters. It does not depend on the unit of $`\lambda`$ and equals a ratio of level spacings of $`C_{\rm eff}`$, $`\frac{r(x+1)}{r(x)}=\frac{E^+_{x+1,k+1}-E^+_{x+1,k}}{E^+_{x,k+1}-E^+_{x,k}}`$, which is well defined (M6). The acceleration is the second $`\lambda`$-derivative of $`\bar x_{\rm lab}`$, from readings of the position at stated $`\lambda`$ (A8). This is not a comparison of two clocks inside one description. No meaning beyond these definitions is attached to (4.24).

### Step 9. Variants (item 5)

From (4.16), (4.17) with $`\tau_k=\tau`$, $`M_k=m+d_k`$ and $`\ell_k:=1+2M_k^2/\tau^2`$. "Same for all levels" is meant for every $`N\ge2`$ and $`g\neq0`$ (in (f) also $`c_{\rm f}\neq0`$).

```math
\begin{array}{l|c|c|c|c|c|c}
\text{variant}&a_{k,+}(0)&a_{k,-}(0)&c_{2,k,\sigma}&\text{rest, upper}&\text{rest, lower}&\text{through }v^2\\\hline
\text{(a)}&-\tau^2g&-\tau^2g&g\,\ell_k&\text{yes}&\text{yes}&\text{exactly no; leading order in }M_k/\tau\text{ yes}\\
\text{(b1)}&-\tau^2\frac{mg}{M_k}&-\tau^2\frac{mg}{M_k}&\frac{mg}{M_k}\ell_k&\text{no}&\text{no}&\text{no}\\
\text{(b2)}&-\tau^2\frac{d_kg}{M_k}&-\tau^2\frac{d_kg}{M_k}&\frac{d_kg}{M_k}\ell_k&\text{no}&\text{no}&\text{no}\\
\text{(c)}&-\tau^2g&-\tau^2g&g\,(1+\ell_k)&\text{yes}&\text{yes}&\text{exactly no; leading order in }M_k/\tau\text{ yes}\\
\text{(d)}&+\frac{\tau^2\mathcal F}{M_k}&-\frac{\tau^2\mathcal F}{M_k}&-\sigma\frac{\mathcal F}{M_k}\bigl(\tfrac12+\ell_k\bigr)&\text{no}&\text{no}&\text{no}\\
\text{(f)}&-\tau^2g\bigl(1+\frac{c_{\rm f}}{M_k}\bigr)&-\tau^2g\bigl(1-\frac{c_{\rm f}}{M_k}\bigr)&g\,\ell_k+\sigma\frac{c_{\rm f}g}{M_k}\bigl(\tfrac12+\ell_k\bigr)&\text{no}&\text{no}&\text{no}
\end{array}
\qquad\text{(4.25)}
```

In (a) and (c) the only level dependence is the lattice term $`2gM_k^2v^2/\tau^2`$; at leading order in $`M_k/\tau`$, $`a=-\tau^2g+g\,v^2`$ in (a) and $`a=-\tau^2g+2g\,v^2`$ in (c). In (f) the number $`c_{\rm f}`$ enters only through the well-defined gradient $`\delta E^+_k+\delta E^-_k=2c_{\rm f}g`$: a factor $`1+gx`$ on the on-site block gives a level-independent fall only if it multiplies the traceless part alone, so the zero of the cost under the factor matters.

## Result

For every member of $`\mathcal C_{\rm lev}`$ with linear level profiles, every level $`k`$, both branches and every smooth $`g`$; first order in the gradients at fixed $`\lambda`$, start and chain, then a long chain; records at leading order ($`O(\kappa^2\sigma_X^2)`$ neglected, Step 1). Sharp-label limits are taken along sharp-label families, and the class of families is named with each statement (4.26).

1. **Drift.**
   - Every smooth $`g`$: $`v^{(0)}=\sigma\langle\omega_k'\rangle_g`$ (4.5). $`v^{(1)}(\lambda)=\lambda\langle a_{k,\sigma}\rangle_g+\rho(\lambda)`$ (4.6), with the coefficient (4.7) exact and the rest bounded for all $`\lambda\ge0`$ by (4.8), converging to $`\rho_\infty`$ like $`\lambda^{-1/2}`$. Long window: $`\langle a_{k,\sigma}\rangle_g`$ (4.10). Fixed-chain remainder: (4.9).
   - Beyond first order, on the fixed chain $`\lvert x\rvert\le L`$ (exact bounds of second degree in the gradients, not uniform in $`L`$): the acceleration is bounded by (4.30) for all $`\lambda\ge0`$, and the correction to an acceleration read off over a window by (4.31), for a window that starts at zero and for every window $`[\lambda_1,\lambda_1+\Lambda]`$. This correction does not vanish for a short window: the bounds tend to $`\mathcal R_L(\lambda_1)\ge2\tau L^2\mathsf b'\lvert g_{\zeta}\rvert`$, and at $`\lambda=0`$ the correction itself is $`\tau^2g_{\zeta}^2\,\bar x_{\rm lab}(0)`$ for $`G=\mathcal F=0`$ and a long chain.
   - Every sharp-label family: the drift acceleration (long window, then sharp label) exists for every $`p_0`$ and is $`a_{k,\sigma}(p_0)`$ (4.11).
   - Sharp label at fixed $`\lambda`$: for every sharp-label family the limit exists if and only if $`\Xi_g[w\sin(2\omega\lambda)]`$ converges (4.27). It is (4.13) for the families of $`\mathcal K_1(x_c,\beta)`$, which contain the centred families ($`\beta=0`$), and for every sharp-label family if $`G_k=g_{\zeta,k}M_k`$. For $`G_k\neq g_{\zeta,k}M_k`$ it does not exist for the family $`E_\infty`$, at rest included.
   - Commutation, (4.14) and table (4.29): for the families of $`\mathcal K_1(x_c,\beta)`$ the limits commute if and only if $`(G_k-g_{\zeta,k}M_k)\sin^2(2p_0)=0`$, in particular at rest. If $`G_k=g_{\zeta,k}M_k`$ they commute for every sharp-label family and every $`p_0`$. If $`G_k\neq g_{\zeta,k}M_k`$ they do not commute for $`E_\infty`$ at any $`p_0`$, rest included, and for other families outside $`\mathcal K_1`$ this is not determined beyond (4.28).
   - Against $`S_k`$: (4.15), for sharp-label families of $`\mathcal K_1(x_c,\beta)`$ at rest, and Step 5.
2. **Rest and motion.** Closed form (4.7); at rest (4.16); expansion in $`v`$ and its coefficients (4.17); well-defined form (4.18).
3. **Level-independent fall.** From rest (4.19); through $`v^2`$ exactly (4.20) and for $`M_k\ll\tau_k`$ (4.21); in the class $`\mathcal C`$ (4.22), (4.23).
4. **Clock rate and fall in $`\mathcal C`$.** A place-dependent rate does not imply a level-independent fall; the converse holds exactly when the common acceleration is not zero. Then (4.24), for both branches, without $`m`$, $`N`$, $`\lambda_0`$, $`k`$, $`\mathcal F`$ and with $`\tau`$ only inside $`v_{\max}/d_0`$. The comparison of the rates relies on A8 (Step 8(d)).
5. **Variants.** Table (4.25).

Controls (M9): the lower branch ((4.16): sign of $`\mathcal F_k`$); the bare start (Step 5); the family $`E_\infty`$, a class of starts for which the sharp-label limit at fixed $`\lambda`$ and the commutation at rest fail; the variants (b1), (b2), (d), (f), where the fall depends on the level.

## Consistency checks

1. **Dimensions and zero gradients.** With $`\tau,M,G,\mathcal F`$ in units of $`1/\lambda`$ and $`g_\zeta`$, $`x`$, $`p`$ pure numbers: $`a_{k,\sigma}\sim\tau^2\mathsf b/M\sim\lambda^{-2}`$, $`c_2v^2\sim\lambda^{-2}`$, and (4.24) is a distance per $`\lambda^2`$ on both sides. With all gradients zero, $`v^{(1)}=0`$ and $`v=\sigma\langle\omega'\rangle_g`$ is constant, as it must be for eigenvectors of $`C_0`$. Passed.
2. **Upper branch at rest against 03-clock-and-fall, and (4.13) against (4.15).** $`a_{k,+}(0)=\frac{\tau^2}{M_k}(\mathcal F-G_k)`$ equals $`a_{\rm sec}`$ of (3.15) and (3.28); for all $`p`$, $`\sum_\sigma w_\sigma a_{k,\sigma}(p)`$ reproduces $`a_{\rm sec}(p)`$ of (3.26), which was derived there for another start; the $`\mathcal F`$ oscillation of (4.15) equals that of (3.15). The second $`\lambda`$-derivative of (4.15) is $`a_{k,\sigma}(0)-\sigma\frac{\tau^2\mathcal F}{M}\cos(2M\lambda)-2\sigma\beta\frac{\tau^2}{M}(G-g_\zeta M)\sin(2M\lambda)`$, which is (4.13) at $`p_0=0`$ with $`w'(0)=-2\tau^2(G-g_\zeta M)/M`$; its first derivative at $`\lambda=0`$, $`\sigma\beta g_\zeta\tau^2/M`$, equals $`\langle\psi_0\rvert\hat v_1\lvert\psi_0\rangle=\sigma g_\zeta\Xi_g[\omega']`$ of Step 3. Passed.
3. **Symmetry and $`\tau_k\to0`$.** $`\sigma_2C^{(k)}[G,\mathcal F,g_\zeta]\sigma_2=-C^{(k)}[G,-\mathcal F,g_\zeta]`$ and $`\sigma_2\beta_{k,+}=i\beta_{k,-}`$, so the upper branch at $`\lambda`$ is the lower branch with $`\mathcal F\to-\mathcal F`$ at $`-\lambda`$; the coefficient of $`\lambda^2`$ is even in $`\lambda`$, hence $`a_{k,+}[G,\mathcal F,g_\zeta]=a_{k,-}[G,-\mathcal F,g_\zeta]`$, as in (4.7). For $`\tau_k\to0`$, $`a_{k,\sigma}\to0`$ and $`v\to0`$: no hopping, no motion. Passed.

## Open issues

- The second order in the gradients is not derived, only bounded: the bounds (4.9), (4.30) and (4.31) are not uniform in $`L`$ and grow with $`\lambda`$, and (4.30), (4.31) do not vanish for a short window. So (4.7) is an acceleration of the first-order coefficient, not a statement about long falls.
- For $`G_k\neq g_{\zeta,k}M_k`$ and sharp-label families outside $`\mathcal K_1(x_c,\beta)`$, other than $`E_\infty`$, the sharp-label limit at fixed $`\lambda`$ is known only through the criterion (4.27), and whether the two limits commute is not determined (last row of (4.29)). The drift acceleration (4.11) is not affected.
- The constants in $`O(v^4)`$ of (4.17), in $`\sup\lvert a_{k,\sigma}''\rvert`$ of (4.11) and in the $`\lambda^{-1/2}`$ decay of $`\rho-\rho_\infty`$ are not made explicit.
- Item 4 uses the rate (3.23) in its wide-start form, defined at zeroth order in the gradients; the comparison of two clocks inside one description is left to 05-rate-comparison.
- Records beyond leading order in $`\kappa`$, and starts in a superposition of levels or branches, are outside the scope.

## Methods used

- First-order perturbation theory in a term of the contract (Duhamel formula)
- Plane-wave representation, $`\hat x=i\partial_p`$, branch (eigenvector) basis of a two-level block
- Separation of secular and oscillating terms; integration by parts
- Riemann–Lebesgue lemma and stationary phase
- Weak convergence of the label weight; limit functionals of families of starts; zeros of entire functions
- Operator-norm and Cauchy–Schwarz bounds; finite-propagation estimate
- Spectral decomposition of the record operator; effective body contract
- Taylor expansion in the drift velocity; injectivity and root-sum arguments for the level conditions
