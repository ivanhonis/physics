# Carried clock under a uniform gradient and two clocks between two meetings

- **Subproject:** 04-ilang-time
- **Package:** 09-proper-time
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-10

## Setup and assumptions

**Model.** The setting of question.md: bodies $`1`$, $`2`$ (types $`B_1\neq B_2`$) with places $`(x,s,a)`$, body contract $`C_{\rm D}=A+B`$, the gradient $`G=-\mathcal F\hat x`$ on body $`1`$ with $`\hat x:=\sum_xx\,P_x`$, the records $`\kappa xX`$, and the start $`\phi_1\otimes\phi_2\otimes\chi`$. Readings are applied at stated values of $`\lambda`$ (A8); $`\lambda\ge0`$.

**Inputs used.** From 05-moving-clock@v3: (5.1) $`P_N(a;\vartheta)`$; (5.5)–(5.6) $`C_k(p)`$, $`\omega_k`$, $`\beta_{k,\pm}`$, $`\theta_k`$; (5.11) $`v_{\max}=\tau\kappa\sigma_X`$; (5.20) the expansion of $`\omega_k`$ in $`j=k-\frac{N-1}2`$ with $`\bar\omega`$, $`\Gamma`$, $`\bar c`$, $`\bar\rho_k`$; (5.21), (5.22), (5.24), (5.25), (5.29); the notation $`d_k,\epsilon,\mu_k,\delta_k,w_k,\bar\mu,\bar w,\hat e`$. From 03-ilang-space/17-motion@v2: (17.15), $`\bar x=\kappa\,\bar x_{\rm lab}\,e`$. From 03-ilang-space/16-common-space@v2: (16.11), through the meeting condition $`t_\pi=0`$ of the question.

**New symbols.** $`p_\lambda:=p+\mathcal F\lambda`$; $`\theta_k':=\partial_p\theta_k=-\mu_k\tau\cos p/\omega_k^2`$; $`\Phi_k(p,\lambda):=\int_0^\lambda\omega_k(p_{\lambda'})\,\mathrm d\lambda'`$.

**Assumptions and their range.**
- **S1. Weak records.** Leading order in $`\kappa`$ at fixed $`\lambda`$ and fixed chain length. It is used in three places: (W1) the view of each body is that of its own contract, $`C_{\rm D}+G`$ or $`C_{\rm D}`$ (Steps 1–4); (W2) positions are $`\bar x_i=\kappa\,\bar x_{{\rm lab},i}\,e`$ in the background (17.15) with $`X\to\kappa X`$ (Steps 3, 6); (W3) the joint statistics of the two bodies factorize (Step 6). Corrections vanish with $`\kappa`$; (5.21) quotes them as $`O(\kappa)`$.
- **S2. Long chains.** For $`x\in\{-L,\dots,L\}`$ (open ends) and a start supported in $`\lvert x-x_0\rvert\le\ell_0`$, the limits are taken in the order: leading order in $`\kappa`$ (S1), then $`L\to\infty`$ at fixed $`\lambda`$, start and parameters, then the expansions below. The limit $`L\to\infty`$ exists: $`B`$ and $`G`$ are diagonal in $`x`$ and $`A`$ moves $`x`$ by one step with $`\lVert A\rVert\le\tau`$, so the Dyson series in $`A`$ bounds the amplitude beyond distance $`d`$ by $`\sum_{n\ge d}(\tau\lambda)^n/n!\le(e\tau\lambda/d)^d`$, for every $`\mathcal F`$; with $`d=L-\lvert x_0\rvert-\ell_0`$ this vanishes. On $`x\in\mathbb Z`$, $`\langle p\vert p'\rangle=2\pi\delta(p-p')`$.
- **S3. Starts.** $`\lvert\phi_i\rangle=\int\frac{\mathrm dp}{2\pi}g_i(p)\,\lvert p\rangle\otimes\beta_{0,+}(p)\otimes\lvert0\rangle`$ with $`\lvert0\rangle=N^{-1/2}\sum_k\lvert f_k\rangle`$ and $`\int\frac{\mathrm dp}{2\pi}\lvert g_i\rvert^2=1`$. The weight $`\lvert g_i\rvert^2/2\pi`$ has mean $`p_0\in(-\frac\pi2,0]`$ for body $`1`$ and $`0`$ for body $`2`$, and variance $`\delta p^2\ll1`$. For smooth $`f`$, $`\int\frac{\mathrm dp}{2\pi}\lvert g_i\rvert^2f=f(\text{mean})+r`$ with $`\lvert r\rvert\le\frac12\delta p^2\sup\lvert f''\rvert`$.
- **S4. Orders.** $`O(\epsilon^n)`$ and $`O(\delta p^2)`$ denote bounds $`K\epsilon^n`$, $`K\delta p^2`$ with $`K`$ depending only on $`N`$, $`\tau/m`$, $`\lambda/\lambda_0`$ and $`\mathcal F\lambda_0`$; they are uniform in $`p`$, $`p_0`$, $`k`$ and $`a`$. At these fixed quantities $`\mathcal F\lambda=\mathcal F\lambda_0\cdot\lambda/\lambda_0`$ is fixed, $`\mathcal F/m=\frac{N\epsilon}{2\pi}\mathcal F\lambda_0=O(\epsilon)`$ and $`m\lambda=\frac{2\pi}{N\epsilon}\frac\lambda{\lambda_0}=O(\epsilon^{-1})`$. No statement is made for $`\mathcal F\lambda\to\infty`$.

Statements marked **exact** hold without expansion (within S1, S2); all others are order estimates in the sense of S4.

## Derivation

### Step 1. The plane-wave label (item 1(a))

Since $`\hat x\lvert p\rangle=-i\partial_p\lvert p\rangle`$, $`e^{iq\hat x}\lvert p\rangle=\lvert p+q\rangle`$. Put $`\lvert\psi_1(\lambda)\rangle=e^{i\mathcal F\lambda\hat x}\lvert\tilde\psi(\lambda)\rangle`$. Then (1.9) with $`C_{\rm D}-\mathcal F\hat x`$ gives $`i\,\mathrm d\tilde\psi/\mathrm d\lambda=e^{-i\mathcal F\lambda\hat x}C_{\rm D}e^{i\mathcal F\lambda\hat x}\tilde\psi`$, and by (5.5) this operator acts on $`\lvert p\rangle\otimes\beta\otimes\lvert f_k\rangle`$ as $`C_k(p+\mathcal F\lambda)`$ on $`\beta`$. Hence, **exactly**,

```math
\lvert\psi_1(\lambda)\rangle=\int\frac{\mathrm dp}{2\pi}\,g_1(p)\,\lvert p+\mathcal F\lambda\rangle\otimes\frac1{\sqrt N}\sum_{k=0}^{N-1}\beta_k(p,\lambda)\otimes\lvert f_k\rangle,
\qquad
p(\lambda):=p_0+\mathcal F\lambda\ \ (\mathrm{mod}\ 2\pi),
\qquad\text{(9.1)}
```

```math
i\,\partial_\lambda\beta_k(p,\lambda)=C_k(p+\mathcal F\lambda)\,\beta_k(p,\lambda),\qquad\beta_k(p,0)=\beta_{0,+}(p).
\qquad\text{(9.2)}
```

The weight over the plane-wave label is translated rigidly by $`\mathcal F\lambda`$: its mean is $`p(\lambda)`$ and its variance stays $`\delta p^2`$, for every $`\mathcal F`$.

### Step 2. Following of the positive branch (item 1(a))

By (5.6), $`C_k=\omega_k(\cos\theta_k\,\sigma_3+\sin\theta_k\,\sigma_1)`$ and $`\partial_p\beta_{k,\pm}=\pm\frac12\theta_k'\beta_{k,\mp}`$; also $`\beta_{0,+}=\cos\delta_k\,\beta_{k,+}+\sin\delta_k\,\beta_{k,-}`$. Write $`\beta_k(p,\lambda)=c_{k+}\beta_{k,+}(p_\lambda)+c_{k-}\beta_{k,-}(p_\lambda)`$ and $`c_{k\pm}=e^{\mp i\Phi_k}\tilde c_{k\pm}`$. Then (9.2) is **exactly**

```math
\frac{\mathrm d\tilde c_{k+}}{\mathrm d\lambda}=2\nu_k\omega_k\,e^{2i\Phi_k}\,\tilde c_{k-},\qquad
\frac{\mathrm d\tilde c_{k-}}{\mathrm d\lambda}=-2\nu_k\omega_k\,e^{-2i\Phi_k}\,\tilde c_{k+},\qquad
\nu_k(p):=\frac{\mathcal F\,\theta_k'(p)}{4\,\omega_k(p)}=-\frac{\mathcal F\mu_k\tau\cos p}{4\,\omega_k^3(p)},
\qquad\text{(9.3)}
```

with $`\nu_k,\omega_k`$ taken at $`p_\lambda`$, $`\tilde c_{k+}(0)=\cos\delta_k(p)`$, $`\tilde c_{k-}(0)=\sin\delta_k(p)`$, and $`\lvert c_{k+}\rvert^2+\lvert c_{k-}\rvert^2=1`$. The coupling $`2\nu_k\omega_k`$ is half the rate of change of $`\theta_k`$; the gap between the branches is $`2\omega_k\ge2m`$. Their ratio is bounded by

```math
\lvert\nu_k(p)\rvert\le\eta:=\frac{\mathcal F\tau}{4m^2}=\frac\tau{4m}\cdot\frac{N\epsilon}{2\pi}\,\mathcal F\lambda_0,
\qquad\text{condition:}\quad\eta\ll1\iff\mathcal F\tau\ll4m^2 .
\qquad\text{(9.4)}
```

Since $`2\omega_ke^{-2i\Phi_k}=i\,\frac{\mathrm d}{\mathrm d\lambda}e^{-2i\Phi_k}`$, one integration by parts gives $`\tilde c_{k-}(\lambda)=\sin\delta_k(p)-\bigl[i\nu_ke^{-2i\Phi_k}\tilde c_{k+}\bigr]_0^\lambda+i\int_0^\lambda e^{-2i\Phi_k}\frac{\mathrm d}{\mathrm d\lambda'}(\nu_k\tilde c_{k+})\,\mathrm d\lambda'`$. In the last integral, $`\mathrm d\nu_k/\mathrm d\lambda=O(\eta\mathcal F)`$ multiplies an oscillating factor (a second integration by parts gives $`O(\eta\mathcal F/m)(1+\mathcal F\lambda)`$), and $`\lvert\nu_k\,\mathrm d\tilde c_{k+}/\mathrm d\lambda\rvert\le2\eta^2\omega_k\lvert\tilde c_{k-}\rvert`$ integrates to $`O(\eta^2m\lambda)\sup\lvert\tilde c_{k-}\rvert`$. By S4, $`\eta=O(\epsilon)`$ and $`\eta^2m\lambda=O(\epsilon)`$, and $`\lvert\delta_k\rvert\le\frac{d_k}2\sup\lvert\partial_\mu\theta\rvert\le\frac{k\epsilon}4`$ (from $`\lvert\partial_\mu\theta\rvert=\tau\lvert\sin p\rvert/\omega^2\le1/2\mu`$). Inserting the result into the first equation of (9.3), the term $`-i\nu_k(p_\lambda)e^{-2i\Phi_k}`$ gives the non-oscillating $`-2i\nu_k^2\omega_k`$, and the other terms oscillate. Hence

```math
\tilde c_{k-}(\lambda)=\sin\delta_k(p)+i\nu_k(p)-i\nu_k(p_\lambda)\,e^{-2i\Phi_k}+O(\epsilon^2),\qquad
\tilde c_{k+}(\lambda)=1-i\,\Xi_k+O(\epsilon^2),\quad\Xi_k:=\int_0^\lambda2\nu_k^2\omega_k\,\mathrm d\lambda' .
\qquad\text{(9.5)}
```

Here $`\Xi_k\le2\eta^2\omega_k\lambda=O(\epsilon)`$ is a phase, and $`\Xi_k-\Xi_{k'}=O(N\epsilon\,\Xi_k)=O(\epsilon^2)`$.

**Answer to 1(a).** The label is $`p(\lambda)=p_0+\mathcal F\lambda`$ (exact). Under (9.4) the start stays in the branch of positive eigenvalue: the neglected weight of the negative branch of level $`k`$ is $`\lvert c_{k-}\rvert^2\le\bigl(\frac{k\epsilon}4+2\eta\bigr)^2+O(\epsilon^3)`$. The part $`\frac{k\epsilon}4`$ is present without a gradient (it is the mismatch $`\delta_k`$ of (5.24)); the gradient adds at most $`2\eta=\mathcal F\tau/2m^2`$ to the amplitude. With $`\mathcal F\lambda_0`$ fixed, (9.4) holds automatically for small $`\epsilon`$ and the neglected weight is of second order.

### Step 3. Displacement (item 1(b))

By W1 and W2, $`\bar x_{{\rm lab},1}=\langle\psi_1\vert\hat x\vert\psi_1\rangle`$ and $`\mathrm d\bar x_{{\rm lab},1}/\mathrm d\lambda=\langle i[A,\hat x]\rangle`$, because $`B`$ and $`G`$ commute with $`\hat x`$. On $`\lvert p\rangle\otimes\beta\otimes\lvert f_k\rangle`$, $`i[A,\hat x]`$ acts as $`\partial_pC_k=-\tau\cos p\,\sigma_1`$, with $`\langle\beta_{k,\pm}\vert\partial_pC_k\vert\beta_{k,\pm}\rangle=\pm w_k`$ and $`\langle\beta_{k,-}\vert\partial_pC_k\vert\beta_{k,+}\rangle=-\tau\cos p\cos\theta_k`$. With (9.1), **exactly**,

```math
\frac{\mathrm d\bar x_{{\rm lab},1}}{\mathrm d\lambda}=\int\frac{\mathrm dp}{2\pi}\lvert g_1\rvert^2\,\frac1N\sum_k\Bigl[\bigl(1-2\lvert c_{k-}\rvert^2\bigr)\,w_k(p_\lambda)-2\mathrm{Re}\bigl(c_{k+}^{*}c_{k-}\bigr)\,\tau\cos p_\lambda\cos\theta_k(p_\lambda)\Bigr],
\qquad\text{(9.6)}
```

which is (5.24) at $`\mathcal F=0`$. By (9.5), $`2\mathrm{Re}(c_{k+}^{*}c_{k-})=2\sin\delta_k(p)\cos2\Phi_k-2\nu_k(p)\sin2\Phi_k+O(\epsilon^2)`$: the co-rotating admixture $`-i\nu_k(p_\lambda)`$ is imaginary and drops out, so to first order the gradient adds no non-oscillating term to the velocity, only a second oscillating one.

- *Non-oscillating part.* $`\int_0^\lambda w_k(p_{\lambda'})\,\mathrm d\lambda'=[\omega_k(p_\lambda)-\omega_k(p)]/\mathcal F`$. By (5.20) and $`\sum_kj=0`$, $`\frac1N\sum_kw_k=\bar w+O\bigl(\frac{\tau^2}m(N\epsilon)^2\bigr)`$; the factor $`1-2\lvert c_{k-}\rvert^2`$ is $`1+O(\epsilon^2)`$; S3 replaces $`p`$ by $`p_0`$.
- *Oscillating part.* With $`2\omega_k\cos2\Phi_k=\frac{\mathrm d}{\mathrm d\lambda}\sin2\Phi_k`$ and $`a_k:=\tau\cos p_\lambda\cos\theta_k/2\omega_k`$, $`\lvert a_k\rvert\le\tau/2m`$, one integration by parts gives $`-\bigl[a_k\bigl(2\sin\delta_k\sin2\Phi_k+2\nu_k(p)\cos2\Phi_k\bigr)\bigr]_0^\lambda+O(\epsilon^2)`$.

```math
\Delta\bar x_1(\lambda)=\kappa\sigma_X\,\Delta\bar x_{{\rm lab},1}(\lambda)\,\hat e,\qquad
\Delta\bar x_{{\rm lab},1}(\lambda)=\frac{\bar\omega(p_0+\mathcal F\lambda)-\bar\omega(p_0)}{\mathcal F}+\mathcal R_x,\qquad
\mathcal R_x=\frac{\tau^2\lambda}m\,O\bigl(\epsilon^2+\delta p^2\bigr),
\qquad\text{(9.7)}
```

with $`\bar\omega(p)=\sqrt{\bar\mu^2+\tau^2\sin^2p}`$ and $`\bar\mu=m\bigl(1+\frac{(N-1)\epsilon}2\bigr)`$. The leading term is $`\int_0^\lambda\bar w(p(\lambda'))\,\mathrm d\lambda'`$, of size up to $`\frac{\tau^2\lambda}{2\bar\mu}`$; the whole first order in $`\epsilon`$ sits in $`\bar\mu`$. The oscillating part of the velocity contributes

```math
\bigl\lvert\Delta\bar x^{\rm osc}_{{\rm lab},1}(\lambda)\bigr\rvert\le\frac\tau m\Bigl(\frac{(N-1)\epsilon}4+\frac{\mathcal F\tau}{2m^2}\Bigr)+O(\epsilon^2),
\qquad\text{(9.8)}
```

a bounded term of order $`\epsilon`$ in label units. Relative to $`\tau^2\lambda/m=O(\epsilon^{-1})`$ it is of order $`\epsilon^2`$: it contributes nothing to (9.7) at first order and is part of $`\mathcal R_x`$. The velocity of item 2, computed from (9.7), is

```math
V_1(\lambda)=\kappa\sigma_X\,\bar w\bigl(p(\lambda)\bigr)\,\hat e,\qquad
b(\lambda):=\frac{\lVert V_1(\lambda)\rVert}{v_{\max}}=\frac{\tau\,\lvert\sin p(\lambda)\cos p(\lambda)\rvert}{\bar\omega\bigl(p(\lambda)\bigr)} .
\qquad\text{(9.9)}
```

### Step 4. Clock reading and clock advance (items 1(c), 1(d))

With $`\langle a\vert f_k\rangle=N^{-1/2}e^{2\pi ika/N}`$, (9.1) and the orthogonality of plane waves give, **exactly** (W1),

```math
q_1(a;\lambda)=\int\frac{\mathrm dp}{2\pi}\lvert g_1\rvert^2\,\Bigl\lVert\frac1N\sum_{k}e^{2\pi ika/N}\beta_k(p,\lambda)\Bigr\rVert^2 .
\qquad\text{(9.10)}
```

1. *Spinors.* Let $`\bar\beta_\pm`$ be (5.6) with $`\mu_k\to\bar\mu`$ (angle $`\bar\theta`$) and $`\zeta_k:=(\bar\theta-\theta_k)/2`$, $`\lvert\zeta_k\rvert\le\lvert j\rvert\epsilon/4`$. The $`\bar\beta_-`$ component of $`\beta_k`$ is $`-c_{k+}\sin\zeta_k+c_{k-}\cos\zeta_k=O(\epsilon)`$; being orthogonal to $`\bar\beta_+`$, it adds $`O(\epsilon^2)`$ to the squared norm. The $`\bar\beta_+`$ component is $`c_{k+}+O(\epsilon^2)`$.
2. *Phases.* By (9.5), $`c_{k+}=e^{-i\Phi_k-i\Xi_k}(1+O(\epsilon^2))`$ and $`\Xi_k`$ is common to all $`k`$ up to $`O(\epsilon^2)`$. The squared norm is therefore $`\bigl\lvert\frac1N\sum_ke^{2\pi ika/N-i\Phi_k}\bigr\rvert^2+O(\epsilon^2)`$.
3. *Expansion in $`j`$.* Integrating (5.20) along $`p_{\lambda'}`$ and using $`m\epsilon=2\pi/N\lambda_0`$: $`\Phi_k=\bar\Phi+\frac{2\pi j}N\vartheta(p,\lambda)+\varphi_j+O(\epsilon^2)`$ with $`\vartheta(p,\lambda):=\frac1{\lambda_0}\int_0^\lambda\Gamma(p_{\lambda'})\,\mathrm d\lambda'`$ and $`\varphi_j:=\frac12(m\epsilon j)^2\int_0^\lambda\bar c\,\mathrm d\lambda'=O(\epsilon)`$, even in $`j`$. With $`u:=2\pi(a-\vartheta)/N`$, the sums $`S_n:=\sum_j\varphi_j^n\,e^{iuj}`$ are real ($`j\to-j`$), so $`\lvert S_0-iS_1\rvert^2=S_0^2+S_1^2`$: an even phase of first order changes the modulus only at second order. By (5.1) the squared norm is $`P_N(a;\vartheta(p,\lambda))+O(\epsilon^2)`$.
4. *Spread.* $`P_N`$ is a trigonometric polynomial in $`\vartheta`$ and $`\partial_p\vartheta`$, $`\partial_p^2\vartheta`$ are bounded by $`\frac\lambda{\lambda_0}\sup\lvert\Gamma'\rvert`$, $`\frac\lambda{\lambda_0}\sup\lvert\Gamma''\rvert`$; S3 replaces $`p`$ by $`p_0`$ with a remainder $`O(\delta p^2)`$.

```math
q_1(a;\lambda)=P_N\bigl(a;\vartheta_1(\lambda)\bigr)+\mathcal R_1,\qquad\mathcal R_1=O(\epsilon^2)+O(\delta p^2)+O(\kappa),
\qquad\text{(9.11)}
```

```math
\vartheta_1(\lambda):=\frac1{\lambda_0}\int_0^\lambda\Gamma\bigl(p_0+\mathcal F\lambda'\bigr)\,\mathrm d\lambda'=\frac{\mathcal I(p_0+\mathcal F\lambda)-\mathcal I(p_0)}{\mathcal F\lambda_0},\qquad
\mathcal I(\varphi):=\int_0^\varphi\frac{\bar\mu\,\mathrm dp}{\sqrt{\bar\mu^2+\tau^2\sin^2p}} .
\qquad\text{(9.12)}
```

$`\mathcal I(\varphi)=F(\varphi\mid-\tau^2/\bar\mu^2)`$ is the incomplete elliptic integral of the first kind; it is odd, and $`\mathcal I(\varphi+\pi)=\mathcal I(\varphi)+2\mathcal K`$ with $`\mathcal K:=\mathcal I(\pi/2)`$.

**Answer to 1(c).** Yes: $`q_1`$ has the form of (5.21) with $`\Gamma(p_0)\lambda/\lambda_0`$ replaced by the clock advance $`\vartheta_1(\lambda)`$ of (9.12).

**Answer to 1(d).** No. From (9.12),

```math
\lambda_0\,\frac{\mathrm d\vartheta_1}{\mathrm d\lambda}=\Gamma\bigl(p(\lambda)\bigr)=\frac{\bar\mu}{\sqrt{\bar\mu^2+\tau^2\sin^2p(\lambda)}} ,
\qquad\text{(9.13)}
```

the function $`\Gamma`$ of (5.21) at the label $`p(\lambda)`$; $`\mathcal F`$ enters only through $`p(\lambda)`$. Explicit dependence on $`\mathcal F`$ lies in $`\mathcal R_1`$. One such term is identified (order estimate): the part of $`\Xi_k`$ linear in $`j`$ shifts the rate by $`\partial_\mu(2\nu^2\omega)\vert_{\bar\mu}=O(\eta^2)`$, of second order.

### Step 5. Rate along the path (item 2)

Write $`\Gamma`$ for (9.13) and $`p=p(\lambda)`$. From (9.9), $`b^2=\tau^2\sin^2p\,(1-\sin^2p)/\bar\omega^2`$, and $`\tau^2\sin^2p/\bar\omega^2=1-\Gamma^2`$. Both forms below are **exact** identities between the expressions (9.9) and (9.13), so they hold to the orders of items 1(b) and 1(c), for all labels:

```math
\Bigl(\lambda_0\frac{\mathrm d\vartheta_1}{\mathrm d\lambda}\Bigr)^2\Bigl(1+\frac{\tau^2}{\bar\mu^2}\sin^4p(\lambda)\Bigr)=1-\frac{\lVert V_1\rVert^2}{v_{\max}^2},
\qquad\text{equivalently}\qquad
\frac{\lVert V_1\rVert^2}{v_{\max}^2}=\bigl(1-\Gamma^2\bigr)\Bigl[1-\frac{\bar\mu^2}{\tau^2}\,\frac{1-\Gamma^2}{\Gamma^2}\Bigr].
\qquad\text{(9.14)}
```

The first form is (5.29) with $`R=1/\Gamma`$ at the label $`p(\lambda)`$. The second contains no label: the speed is a function of the rate. Conversely the rate is a function of the speed only where $`b`$ is monotonic in $`\lvert\sin p\rvert`$, i.e. for $`\sin^2p\le\bar\mu/(\bar\mu+\sqrt{\bar\mu^2+\tau^2})`$, where $`b`$ rises to its largest value $`b_*=(\sqrt{\bar\mu^2+\tau^2}-\bar\mu)/\tau<1`$. For small labels, since $`1-\frac x2\le(1+x)^{-1/2}\le1`$,

```math
\lambda_0\frac{\mathrm d\vartheta_1}{\mathrm d\lambda}=\sqrt{1-\frac{\lVert V_1(\lambda)\rVert^2}{v_{\max}^2}}\;\bigl(1+\rho(\lambda)\bigr),\qquad-\frac{\tau^2}{2\bar\mu^2}\sin^4p(\lambda)\le\rho(\lambda)\le0 .
\qquad\text{(9.15)}
```

The bound on $`\rho`$ is exact. The deviation of the rate from $`1`$ is $`\frac{\tau^2}{2\bar\mu^2}p^2+O(p^4)`$, so $`\rho`$ is smaller by a factor of order $`p^2`$. At fixed $`\tau/\bar\mu`$ the leading order is equally $`1-\frac12b^2`$; the square root is the more accurate form, and the only one that stays valid when $`\tau p/\bar\mu`$ is not small (it then needs only $`\tau^2p^4/\bar\mu^2\ll1`$). Integrating (9.15), with $`\bar\rho`$ a weighted mean of $`\rho`$:

```math
\vartheta_1(\lambda)=\frac{1+\bar\rho}{\lambda_0}\int_0^\lambda\sqrt{1-\frac{\lVert V_1(\lambda')\rVert^2}{v_{\max}^2}}\;\mathrm d\lambda',\qquad
-\frac{\tau^2}{2\bar\mu^2}\max_{0\le\lambda'\le\lambda}\sin^4p(\lambda')\le\bar\rho\le0 .
\qquad\text{(9.16)}
```

To leading order for small labels on the whole path ($`\lvert p_0\rvert\ll1`$ and $`\lvert p_0+\mathcal F\lambda\rvert\ll1`$), $`\bar\rho\to0`$ and $`\vartheta_1`$ is a functional of the path $`V_1`$ alone.

### Step 6. Joint reading and meetings (items 3(a), 3(b))

*3(a).* At leading order in $`\kappa`$ (W3), $`C=(C_{\rm D}+G)\otimes\mathbb 1\otimes\mathbb 1_c+\mathbb 1\otimes C_{\rm D}\otimes\mathbb 1_c`$ is a sum of commuting terms on different factors. The product start evolves into $`\psi_1(\lambda)\otimes\psi_2(\lambda)\otimes\chi`$, and the class of $`(a_1,a_2)`$ has the projector $`\Pi_{a_1}\otimes\Pi_{a_2}\otimes\mathbb 1_c`$. The types are pairwise different, so (1.11) imposes nothing. Body $`2`$ is the case $`\mathcal F=0`$, $`p_0=0`$ of Steps 1–4, i.e. (5.21) with $`\Gamma(0)=1`$:

```math
q_{12}(a_1,a_2;\lambda)=q_1(a_1;\lambda)\,q_2(a_2;\lambda)+O(\kappa),\qquad
q_2(a;\lambda)=P_N\bigl(a;\vartheta_2(\lambda)\bigr)+\mathcal R_1,\qquad\vartheta_2(\lambda)=\frac\lambda{\lambda_0} .
\qquad\text{(9.17)}
```

The factorization is exact at $`\kappa=0`$.

*3(b).* For body $`2`$, (5.25) gives $`\Delta\bar x_{{\rm lab},2}=\bar w(0)\lambda+\mathcal R_x=\mathcal R_x`$: no displacement to the order of (9.7). The starts have equal mean labels and $`t_\pi=0`$, so by W2 the bodies meet iff the leading term of (9.7) vanishes, $`\sin^2(p_0+\mathcal F\lambda)=\sin^2p_0`$:

```math
\mathcal F\lambda\in\{\,n\pi:\ n\ge1\,\}\ \cup\ \{\,2\lvert p_0\rvert+n\pi:\ n\ge0\,\}\setminus\{0\},\qquad
\lambda_R=\frac{2\lvert p_0\rvert}{\mathcal F}\ \ (p_0<0),\qquad\lambda_R=\frac\pi{\mathcal F}\ \ (p_0=0).
\qquad\text{(9.18)}
```

For $`p_0<0`$, body $`1`$ leaves towards decreasing labels ($`\bar w(p_0)<0`$), stops at $`\lambda_R/2`$ where $`p=0`$, at the displacement $`-[\bar\omega(p_0)-\bar\mu]/\mathcal F`$, and returns with label $`\lvert p_0\rvert`$. The meetings with $`n\ge1`$ lie after the label has passed $`\pi/2`$; the label motion has period $`\pi/\mathcal F`$ in $`\lambda`$. For $`p_0=0`$ the two families coincide. Because of $`\mathcal R_x`$, $`\lambda_R`$ for $`p_0<0`$ is determined up to the relative shift $`\frac{\bar\omega(p_0)}{m\lvert\sin p_0\cos p_0\rvert}\,O(\epsilon^2+\delta p^2)`$, which is not uniform for $`p_0\to0^-`$.

### Step 7. Advances at the meetings (items 3(c)–3(e))

*3(c).* Insert (9.18) into (9.12) and (9.17), with $`\mathcal I`$ odd. For $`p_0<0`$:

```math
\vartheta_2(\lambda_R)=\frac{2\lvert p_0\rvert}{\mathcal F\lambda_0},\qquad
\vartheta_1(\lambda_R)=\frac{2\,\mathcal I(\lvert p_0\rvert)}{\mathcal F\lambda_0},\qquad
\frac{\vartheta_1(\lambda_R)}{\vartheta_2(\lambda_R)}=\frac{\mathcal I(\lvert p_0\rvert)}{\lvert p_0\rvert}=\frac1{\lvert p_0\rvert}\int_0^{\lvert p_0\rvert}\frac{\bar\mu\,\mathrm dp}{\sqrt{\bar\mu^2+\tau^2\sin^2p}} .
\qquad\text{(9.19)}
```

For $`p_0=0`$: $`\vartheta_2(\lambda_R)=\pi/\mathcal F\lambda_0`$, $`\vartheta_1(\lambda_R)=2\mathcal K/\mathcal F\lambda_0`$, ratio $`2\mathcal K/\pi`$. The ratio does not depend on $`\mathcal F`$; it depends on $`p_0`$ and on $`\tau/\bar\mu`$, with $`\bar\mu=m\bigl(1+\frac{(N-1)\epsilon}2\bigr)`$.

*3(d).* $`\Gamma(p)\le1`$ with equality only at $`\sin p=0`$, and $`p(\lambda')`$ is not constant because $`\mathcal F>0`$. By (9.12) and (9.17), for all $`p_0\in(-\frac\pi2,0]`$, $`\mathcal F>0`$, $`\tau>0`$:

```math
\vartheta_1(\lambda)<\vartheta_2(\lambda)\quad\text{for every }\lambda>0,\qquad
\frac{2\mathcal K}\pi\le\frac{\vartheta_1}{\vartheta_2}\Big\vert_{\text{meeting}}<1 .
\qquad\text{(9.20)}
```

The clock of body $`2`$, the body without gradient, has advanced more at $`\lambda_R`$, and the advances are never equal at $`\lambda>0`$. The ratio tends to $`1`$ only for $`p_0\to0^-`$, where $`\lambda_R\to0`$, or for $`\tau/\bar\mu\to0`$. The same holds at every later meeting: there the ratio is $`2\mathcal K/\pi`$ (at $`\mathcal F\lambda=n\pi`$) or $`\frac{2\mathcal I(\lvert p_0\rvert)+2n\mathcal K}{2\lvert p_0\rvert+n\pi}`$. The lower bound follows because $`\Gamma`$ decreases on $`[0,\frac\pi2]`$, so its running mean $`\mathcal I(\varphi)/\varphi`$ decreases to $`2\mathcal K/\pi`$. At $`p_0=0`$ the first meeting is the full period and the ratio jumps to $`2\mathcal K/\pi`$. These are statements about the advances (9.12); for the distributions they hold where $`\vartheta_2-\vartheta_1`$ exceeds the remainders of (9.11).

*3(e).* With $`\Gamma=1-\frac{\tau^2}{2\bar\mu^2}p^2+O(p^4)`$ and, from (9.9), $`b^2=\frac{\tau^2}{\bar\mu^2}p^2+O(p^4)`$, and $`\mathrm d\lambda=\mathrm dp/\mathcal F`$:

```math
\frac{\vartheta_1(\lambda_R)}{\vartheta_2(\lambda_R)}=1-\frac{\tau^2p_0^2}{6\bar\mu^2}+O(p_0^4)=1-\frac12\Bigl\langle\frac{\lVert V_1\rVert^2}{v_{\max}^2}\Bigr\rangle+O(p_0^4),\qquad
\Bigl\langle\frac{\lVert V_1\rVert^2}{v_{\max}^2}\Bigr\rangle:=\frac1{\lambda_R}\int_0^{\lambda_R}b^2\,\mathrm d\lambda=\frac{\tau^2p_0^2}{3\bar\mu^2}+O(p_0^4).
\qquad\text{(9.21)}
```

Each $`O(p_0^4)`$ is bounded by a multiple of $`\frac{\tau^2}{\bar\mu^2}\bigl(1+\frac{\tau^2}{\bar\mu^2}\bigr)p_0^4`$; in the second form it equals $`-\bigl(\frac{\tau^2}{10\bar\mu^2}+\frac{\tau^4}{40\bar\mu^4}\bigr)p_0^4`$ to this order.

### Step 8. Certain readings at the first meeting (item 3(f))

By (5.1), $`P_N(a;\vartheta)=\delta_{a,\,\vartheta\bmod N}`$ if $`\vartheta\in\mathbb Z`$, and $`P_N(a;\vartheta)>0`$ for every $`a`$ otherwise. Both readings at $`\lambda_R`$ are therefore certain, up to $`\mathcal R_1`$, iff both advances are integers. Since $`0<\vartheta_1<\vartheta_2`$ by (9.20), for $`p_0<0`$:

```math
\mathcal F\lambda_0=\frac{2\lvert p_0\rvert}{n_2},\qquad\frac{\mathcal I(\lvert p_0\rvert)}{\lvert p_0\rvert}=\frac{n_1}{n_2},\qquad n_1,n_2\in\mathbb N,\ 1\le n_1<n_2
\quad\Longrightarrow\quad
q_{12}(a_1,a_2;\lambda_R)=\delta_{a_1,\,n_1\bmod N}\,\delta_{a_2,\,n_2\bmod N}+O(\mathcal R_1).
\qquad\text{(9.22)}
```

Clock $`2`$ shows $`n_2\bmod N`$ and clock $`1`$ shows $`n_1\bmod N`$; they differ iff $`N\nmid(n_2-n_1)`$. For $`p_0=0`$ the conditions are $`\mathcal F\lambda_0=\pi/n_2`$ and $`2\mathcal K/\pi=n_1/n_2`$, a condition on $`\tau/\bar\mu`$. Since $`\mathcal I(\varphi)/\varphi`$ decreases strictly from $`1`$ to $`2\mathcal K/\pi`$ on $`(0,\frac\pi2]`$, every pair with $`2\mathcal K/\pi<n_1/n_2<1`$ fixes exactly one $`p_0\in(-\frac\pi2,0)`$ and then $`\mathcal F\lambda_0`$. Because $`P_N(n;n+\delta)=1-O(\delta^2)`$, the conditions need to hold only up to $`O(\epsilon)`$.

## Result

Exact within S1, S2: (9.1), the identities (9.14), the bounds of (9.15) and (9.16), and the factorization in (9.17) at $`\kappa=0`$. Order estimates in the sense of S4: (9.4), (9.7), (9.8), (9.11), (9.21). The statements (9.13), (9.18)–(9.20), (9.22) are exact properties of the first-order expressions (9.7) and (9.12).

- **1(a)** (9.1): $`p(\lambda)=p_0+\mathcal F\lambda`$, exact. (9.4): condition $`\eta=\mathcal F\tau/4m^2\ll1`$; neglected negative-branch weight at most $`(k\epsilon/4+2\eta)^2+O(\epsilon^3)`$.
- **1(b)** (9.7): $`\Delta\bar x_1=\kappa\sigma_X\hat e\,[\bar\omega(p_0+\mathcal F\lambda)-\bar\omega(p_0)]/\mathcal F`$, relative remainder $`O(\epsilon^2+\delta p^2)`$. (9.8): the oscillating velocity contributes a bounded term of relative order $`\epsilon^2`$. (9.9): $`V_1`$ and $`b=\lVert V_1\rVert/v_{\max}`$.
- **1(c)** (9.11), (9.12): $`q_1=P_N(a;\vartheta_1(\lambda))+\mathcal R_1`$ with $`\vartheta_1=[\mathcal I(p_0+\mathcal F\lambda)-\mathcal I(p_0)]/\mathcal F\lambda_0`$; yes, of the form (5.21).
- **1(d)** (9.13): $`\lambda_0\,\mathrm d\vartheta_1/\mathrm d\lambda=\Gamma(p(\lambda))`$; no other dependence on $`\mathcal F`$ to first order.
- **2** (9.14): relation without expansion in the label. (9.15): $`\lambda_0\,\mathrm d\vartheta_1/\mathrm d\lambda=\sqrt{1-\lVert V_1\rVert^2/v_{\max}^2}\,(1+\rho)`$. (9.16): $`\vartheta_1`$ as a functional of the path.
- **3(a)** (9.17): $`q_{12}=q_1q_2`$, $`\vartheta_2=\lambda/\lambda_0`$. **3(b)** (9.18): all meetings and $`\lambda_R`$. **3(c)** (9.19): advances and ratio at $`\lambda_R`$. **3(d)** (9.20): $`\vartheta_1<\vartheta_2`$ at every $`\lambda>0`$, hence at every meeting; never equal. **3(e)** (9.21): ratio $`=1-\frac12\langle\lVert V_1\rVert^2/v_{\max}^2\rangle+O(p_0^4)`$. **3(f)** (9.22): integer advances; readings $`n_1\bmod N`$ and $`n_2\bmod N`$ with $`n_1<n_2`$.

## Consistency checks

1. **Dimensions.** $`x`$, $`p`$, $`a`$ are pure numbers; $`\tau,m,\mathcal F,\omega_k,\bar\mu`$ and $`\kappa\sigma_X`$ have the dimension $`[\lambda]^{-1}`$. Then $`\mathcal F\lambda`$, $`\eta`$, $`\nu_k`$, $`\Xi_k`$, $`\vartheta_i`$, $`b`$ and $`\Delta\bar x_{\rm lab}`$ in (9.7) are pure numbers, and $`V_1`$ and $`v_{\max}=\tau\kappa\sigma_X`$ both have $`[\lambda]^{-2}`$.
2. **$`\mathcal F\to0`$ at fixed $`\lambda`$.** $`p(\lambda)\to p_0`$; $`\nu_k\to0`$ and $`\Phi_k\to\omega_k\lambda`$, so (9.3) gives $`\tilde c_{k+}=\cos\delta_k`$, $`\tilde c_{k-}=\sin\delta_k`$ and (9.6) becomes (5.24) exactly; (9.7) $`\to\bar w(p_0)\lambda`$, which is (5.25); (9.12) $`\to\Gamma(p_0)\lambda/\lambda_0`$, which is (5.21); (9.14) becomes (5.29).
3. **$`\tau\to0`$.** Then $`A=0`$, $`[B,G]=0`$ and $`\beta_{0,+}=(1,0)^{\rm T}`$, so each clock label evolves by $`e^{-i(m+D)\lambda}\lvert0\rangle`$ and $`q_i=P_N(a;\lambda/\lambda_0)`$ exactly, for every $`\mathcal F`$. Accordingly $`\Gamma\equiv1`$, $`\vartheta_1=\vartheta_2`$, (9.7) $`\to0`$, the ratio (9.19) $`\to1`$ and the deviation in (9.21) vanishes as $`\tau^2`$.

## Open issues

- The remainders $`\mathcal R_x`$, $`\mathcal R_1`$ are order estimates at fixed $`\mathcal F\lambda`$; their constants were not computed. Nothing is claimed for $`\mathcal F\lambda\to\infty`$ (many periods of the label), where transfer to the negative branch may accumulate.
- The explicit dependence of the rate on $`\mathcal F`$ at second order ($`O(\eta^2)`$) is identified in Step 4 but not derived in full.
- A meeting is an equality of the mean positions only. $`\lambda_R`$ is determined up to the shift stated in Step 6, which is not uniform for $`p_0\to0^-`$; the first meeting changes discontinuously between $`p_0\to0^-`$ and $`p_0=0`$.
- Corrections in $`\kappa`$, including any influence of one body on the other through the medium, are out of scope; the results assume the order of limits of S2.
- At fixed $`\tau/\bar\mu`$ the small-label result (9.15) does not distinguish the square root from $`1-\frac12b^2`$ at leading order; the exact relation is (9.14).

## Methods used

- Translation of the plane-wave label by a uniform gradient (interaction picture with respect to $`G`$)
- Adiabatic following in a two-branch system; integration by parts of oscillating integrals
- Rate of change of a mean value from a commutator
- Expansion of the level frequencies about the mean level; symmetry of an even phase
- Taylor expansion about the mean of a concentrated weight
- Incomplete elliptic integral of the first kind; monotonicity of running means
