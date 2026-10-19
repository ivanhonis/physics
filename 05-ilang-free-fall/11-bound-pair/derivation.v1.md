# Bound pair of two Model D bodies: bound level, curvature, cost and clock rates

- **Subproject:** 05-ilang-free-fall
- **Package:** 11-bound-pair
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-11

## Setup and assumptions

- **Setting.** As in `question.md`: two Model D bodies $`b_1`$, $`b_2`$ of different types, one medium $`c`$, $`C=C_{\rm pair}+C_{\rm rec}`$, $`C_{\rm pair}=C^{\rm D}_1+C^{\rm D}_2+U`$, the binding $`U`$ of the class $`\mathcal W`$, fixed clock levels $`k_1,k_2`$ with $`M_i=M^{(i)}_{k_i}`$, the fibre contract $`H(P)`$, a bound level $`E_b(P)`$ with the eigenvector $`\psi_P`$, the curvature inertia $`\mathfrak m_b=1/E_b''(0)`$, $`\mathfrak m_i=M_i/\tau_i^2`$, and the regime $`\mathsf R`$ ($`\tau_i=\epsilon\hat\tau_i`$, $`w_{s_1s_2}=\epsilon^2\hat w_{s_1s_2}`$, $`\epsilon\to0`$). The bodies, the class $`\mathcal W`$, the diagonal on-site binding, $`\mathsf R`$ and every start are assumptions (M8, M9); a bound level is a distinguished set of states (A11). No field acts.
- **Inputs used.**
  - (5.5), (5.6) of 04-ilang-time/05-moving-clock: on a plane wave $`\lvert p\rangle`$ and a level $`k`$ the Model D contract acts as $`-\tau\sin p\,\sigma_1+\mu_k\sigma_3`$, with the eigenvalues $`\pm\omega_k(p)`$, $`\omega_k=\sqrt{\mu_k^2+\tau^2\sin^2p}`$. (5.11) there: $`v_{\max}=\tau\kappa\sigma_X`$. (5.1), (5.21) there: $`P_N(a;\vartheta)`$ and $`q(a;\lambda)=P_N(a;\Gamma(p_0)\lambda/\lambda_0)+\mathcal R`$, with $`\Gamma(0)=1`$.
  - (6.7), (6.20) of 04-ilang-time/06-inertia-internal-energy: the gap $`2M_k`$, the upper branch is the eigenvector $`\lvert1\rangle`$ of $`\sigma_3`$, and $`1/\omega_k''(0)=M_k/\tau^2=I^{\rm lab}_k`$.
  - (17.15) of 03-ilang-space/17-motion and (16.11) of 03-ilang-space/16-common-space: the position of either body is $`\kappa\,\bar m_i\,e`$ with $`\bar m_i`$ the mean position label, and $`r=x_1-x_2`$ is the separation of corresponding points.
  - (21.2), (21.12), (21.15), (21.16) of 03-ilang-space/21-composite-body, as quoted in the question.
- **Notation.** $`\omega_i(p):=\sqrt{M_i^2+\tau_i^2\sin^2p}`$, $`\Omega_i:=\sqrt{M_i^2+\tau_i^2}`$. For item 3: $`a_i:=\tau_i^2/(4M_i)=1/(4\mathfrak m_i)`$, $`a:=a_1+a_2`$, $`j(P):=\sqrt{a_1^2+a_2^2+2a_1a_2\cos2P}`$ (so $`j(0)=a`$), $`w:=w_{11}`$, $`\varsigma:=\mathrm{sgn}w`$, $`u:=\lvert w\rvert/a=\lvert\hat w_{11}\rvert/\hat a`$ and $`\Lambda:=1+\varsigma/\sqrt{1+u^2}\in(0,2)`$. In $`\mathsf R`$ the quantities $`a_i,a,j,w`$ are of order $`\epsilon^2`$ and $`u,\Lambda`$ of order one.
- **Standard facts used.** Weyl's theorem (a finite-range change does not change the bands); exponential decay of the eigenvector of an isolated eigenvalue of a finite-range operator; analytic perturbation theory of an isolated eigenvalue (first and second order); degenerate perturbation theory for an isolated group of eigenvalues (Schrieffer–Wolff), valid for $`\tau_1+\tau_2+\max\lvert w_{s_1s_2}\rvert\ll2\min(M_1,M_2)`$.
- **Simple level.** A bound level is taken simple (multiplicity one), which is the case in Step 7. For a degenerate level, (11.5)–(11.9) hold for each analytic branch of the varied parameter with its eigenvector.
- **Status words.** *Exact*: an identity for every member of the stated class. *Leading order in $`\mathsf R`$*: the stated remainder is neglected.

## Derivation

### Step 1. Fibre contract and two-body bands (item 1a)

On the levels $`k_1,k_2`$ a vector with the label $`P`$ of the joint shift is $`\Psi(x_1,x_2)=e^{iP(\eta x_1+(1-\eta)x_2)}\psi(x_1-x_2)`$ with $`\psi(r)\in\mathbb C^2\otimes\mathbb C^2`$. The real number $`\eta`$ is the phase convention. Changing it is the unitary map $`\psi(r)\to e^{i(\eta-\eta')Pr}\psi(r)`$, so the spectrum and every $`\langle O\rangle_P`$ below are independent of it. With $`(A_i\Psi)(x_i)=\frac{\tau_i}2\bigl[-i\sigma_1\Psi(x_i-1)+i\sigma_1\Psi(x_i+1)\bigr]`$ and $`(S\psi)(r):=\psi(r-1)`$:

```math
H(P)=\underbrace{\tfrac{i\tau_1}{2}\,\sigma^{(1)}_1\bigl(e^{i\eta P}S^{\dagger}-e^{-i\eta P}S\bigr)}_{A_1}+\underbrace{\tfrac{i\tau_2}{2}\,\sigma^{(2)}_1\bigl(e^{i(1-\eta)P}S-e^{-i(1-\eta)P}S^{\dagger}\bigr)}_{A_2}+M_1\sigma^{(1)}_3+M_2\sigma^{(2)}_3+\underbrace{W(\hat r)}_{U}.
\qquad\text{(11.1)}
```

$`A_i`$, $`U`$, $`\sigma^{(i)}_3`$ denote from here on these fibres. On $`\psi(r)=e^{iqr}\beta`$ the part without $`W`$, $`H^0(P)`$, acts as $`h_P(q)=-\tau_1\sin p_1\,\sigma^{(1)}_1-\tau_2\sin p_2\,\sigma^{(2)}_1+M_1\sigma^{(1)}_3+M_2\sigma^{(2)}_3`$ with $`p_1=\eta P+q`$, $`p_2=(1-\eta)P-q`$, $`p_1+p_2=P`$: each body as in (5.5).

For $`\lvert r\rvert>R`$, $`H(P)`$ acts as $`H^0(P)`$, so an eigenvector that is bounded and not square-summable is there a combination of plane waves with real $`q`$. By (5.6) their eigenvalues are $`\sigma_1\omega_1(p_1)+\sigma_2\omega_2(p_2)`$, $`\sigma_i=\pm`$. By Weyl's theorem this set is the same for every $`W\in\mathcal W`$. With $`v=\sin^2q\in[0,1]`$ at $`P=0`$ and $`f(v):=\sqrt{M_1^2+\tau_1^2v}-\sqrt{M_2^2+\tau_2^2v}`$:

```math
\mathcal B_{\sigma_1\sigma_2}(P)=\bigl\{\sigma_1\omega_1(p_1)+\sigma_2\omega_2(P-p_1)\bigr\}_{p_1\in(-\pi,\pi]},\qquad \mathcal B_{++}(0)=[\,M_1+M_2,\ \Omega_1+\Omega_2\,],\quad \mathcal B_{+-}(0)=[\,\min f,\ \max f\,],\quad \mathcal B_{--}=-\mathcal B_{++},\quad \mathcal B_{-+}=-\mathcal B_{+-}.
\qquad\text{(11.2)}
```

- The extremes of $`f`$ are among $`f(0)=M_1-M_2`$, $`f(1)=\Omega_1-\Omega_2`$ and, if $`\tau_1\neq\tau_2`$ and $`v^{*}:=\frac{\tau_2^4M_1^2-\tau_1^4M_2^2}{\tau_1^2\tau_2^2(\tau_1^2-\tau_2^2)}\in(0,1)`$, the stationary value $`f(v^{*})=\mathrm{sgn}(\tau_1-\tau_2)\sqrt{(\tau_1^2-\tau_2^2)(\tau_2^2M_1^2-\tau_1^2M_2^2)}/(\tau_1\tau_2)`$.
- The edge $`M_1+M_2`$ is attained at $`q=0`$ and at $`q=\pi`$.
- Exceptional members: for equal data ($`M_1=M_2`$, $`\tau_1=\tau_2`$) $`\mathcal B_{\pm\mp}(0)=\{0\}`$, a point of infinite multiplicity that has square-summable eigenvectors; for $`\tau_i/M_i`$ of order one the bands can overlap. In $`\mathsf R`$ the four bands have widths $`O(\epsilon^2)`$ around $`\pm M_1\pm M_2`$.

### Step 2. Replacements and well-defined quantities (item 1b)

Expand a change of the four listed terms with zero sum in products of operators on $`b_1`$, $`b_2`$, $`c`$. A component that is non-trivial on two objects occurs in one listed term only and must vanish. Hence, as in (21.2) of 03-ilang-space/21-composite-body, with single-object operators in place of the numbers there (the terms here are not diagonal in the places): with $`T_1,\alpha`$ self-adjoint on $`\mathcal H_{b_1}`$ and $`T_2,\beta`$ on $`\mathcal H_{b_2}`$,

```math
\delta C^{\rm D}_1=T_1,\qquad \delta C^{\rm D}_2=T_2,\qquad \delta C_{\rm rec}=\alpha+\beta,\qquad \delta U=-(T_1+\alpha)-(T_2+\beta),
\qquad\text{(11.3)}
```

and inside $`C_{\rm rec}`$ an operator $`Z`$ on $`\mathcal H_c`$ can move between its two pair terms.

- **What the range condition fixes.** If $`U`$ and $`U+\delta U`$ are in $`\mathcal W`$, then $`\delta W(x_1-x_2)=-\theta_1(x_1)\otimes\mathbb 1-\mathbb 1\otimes\theta_2(x_2)`$ with $`\theta_i(x)`$ on the branch label of $`b_i`$, and $`\delta W=0`$ for $`\lvert x_1-x_2\rvert`$ beyond the larger range. Every $`x_1`$ has such $`x_2`$ and conversely, so $`\theta_1=t\,\mathbb 1`$, $`\theta_2=-t\,\mathbb 1`$ with one real $`t`$, and $`\delta U=0`$. The range condition fixes $`U`$ completely. Without it, single-object terms can be listed in $`U`$, for example $`W(r)\to W(r)+M_1\sigma^{(1)}_3`$ with $`B_1\to0`$.
- **What remains.** $`\delta C_{\rm pair}=-(\alpha+\beta)=-\delta C_{\rm rec}`$ and the constant $`t`$ between the two bodies. For $`C_{\rm rec}`$ to stay a sum of record terms, $`\alpha=\sum_x\alpha_x\lvert x\rangle\langle x\rvert`$ with real numbers $`\alpha_x`$, and $`\beta`$ likewise: place-dependent terms that move between a body and its records (M6). The fibres need $`C_{\rm pair}`$ to commute with the joint shift, which gives $`\alpha_x=c_1+gx`$, $`\beta_y=c_2-gy`$, and the one operator $`X`$ in both record terms gives $`g=0`$. Within the stated forms only real constants remain: $`\delta C^{\rm D}_1=t-c_1`$, $`\delta C^{\rm D}_2=-t-c_2`$, $`\delta C_{\rm pair}=-(c_1+c_2)`$. The conventions $`\eta`$ (Step 1) and the choice $`s`$ of the correspondence ($`r\to r+s`$ relabels $`W`$) change no quantity below.

```math
\begin{array}{ll}
W(r) & \text{yes, by the range condition (no without it)}\\
M_i & \text{yes as half the gap } 2M_i \text{ of (6.7), the coefficient of } \sigma^{(i)}_3;\ \text{no as a cost of } b_i \text{ (branch costs } \pm M_i+t-c_i)\\
E_b(P) & \text{no: } \delta E_b=-(c_1+c_2)\\
E_b(P)-(M_1+M_2) & \text{yes, as the distance from the edge of } \mathcal B_{++}(0),\ \text{which is } M_1+M_2 \text{ in the listed form and shifts with } E_b\\
E_b(P)-E_b(0),\ E_b''(0) & \text{yes}\\
\langle\sigma^{(i)}_3\rangle_P & \text{yes: a constant does not change } \psi_P
\end{array}
\qquad\text{(11.4)}
```

### Step 3. Derivatives with respect to the data (item 2a)

$`H(P)`$ is linear in $`M_i`$, in $`\tau_i`$ (through $`A_i`$) and in a factor $`\theta`$ of $`W`$, and these terms are bounded. For a simple isolated eigenvalue, first-order perturbation theory (Hellmann–Feynman) gives, for every $`W\in\mathcal W`$ and every $`P\in\mathcal P`$:

```math
\frac{\partial E_b}{\partial M_i}=\langle\sigma^{(i)}_3\rangle_P,\qquad
\tau_i\frac{\partial E_b}{\partial\tau_i}=\langle A_i\rangle_P,\qquad
\frac{\partial E_b}{\partial\theta}\Big|_{\theta=1}=\langle U\rangle_P\qquad(i=1,2).
\qquad\text{(11.5)}
```

$`H(P)`$ at the data $`(s\tau_i,sM_i,sW)`$ is $`s`$ times $`H(P)`$ at $`(\tau_i,M_i,W)`$, with the same eigenvectors. So $`E_b`$ is homogeneous of degree one in $`(\tau_1,\tau_2,M_1,M_2,\theta)`$, and Euler's relation with (11.5) reads

```math
E_b(P)=M_1\langle\sigma^{(1)}_3\rangle_P+M_2\langle\sigma^{(2)}_3\rangle_P+\langle A_1\rangle_P+\langle A_2\rangle_P+\langle U\rangle_P .
\qquad\text{(11.6)}
```

### Step 4. First derivative in $`P`$ and the velocities (item 2b)

Let $`V_i:=i[C_{\rm pair},\hat x_i]=i[A_i,\hat x_i]`$; $`B_i`$, $`U`$ and $`C_{\rm rec}`$ commute with $`\hat x_i`$, so $`\frac{\mathrm d}{\mathrm d\lambda}\langle\hat x_i\rangle=\langle V_i\rangle`$ holds for the full $`C`$. $`V_i`$ commutes with the joint shift, with the fibres $`V_1=-\frac{\tau_1}2\sigma^{(1)}_1(e^{i\eta P}S^\dagger+e^{-i\eta P}S)`$ and $`V_2=-\frac{\tau_2}2\sigma^{(2)}_1(e^{i(1-\eta)P}S+e^{-i(1-\eta)P}S^\dagger)`$ (on plane waves $`-\tau_i\cos p_i\,\sigma^{(i)}_1`$). From (11.1), $`\partial_PH=\eta V_1+(1-\eta)V_2`$ and $`V_1-V_2=i[H(P),\hat r]`$. The eigenvector $`\psi_P`$ decays exponentially, so $`\hat r\psi_P`$ is square-summable and $`\langle[H(P),\hat r]\rangle_P=0`$. With Hellmann–Feynman in $`P`$:

```math
E_b'(P)=\langle V_1\rangle_P=\langle V_2\rangle_P .
\qquad\text{(11.7)}
```

A state of the pair built from the bound level is $`\Phi=\int\mathrm dP\,g(P)\,\lvert P;\psi_P\rangle`$ with $`\int\lvert g\rvert^2=1`$. Under $`C_{\rm pair}`$, $`g(P)\to g(P)e^{-iE_b(P)\lambda}`$, and $`V_i`$ has no elements between different $`P`$. Hence for every $`\lambda`$, with $`P_0`$ the mean and $`\delta P`$ the width of $`\lvert g\rvert^2`$:

```math
\frac{\mathrm d\bar m_1}{\mathrm d\lambda}=\frac{\mathrm d\bar m_2}{\mathrm d\lambda}=\int\mathrm dP\,\lvert g(P)\rvert^2E_b'(P)=E_b'(P_0)+O(\delta P^2).
\qquad\text{(11.8)}
```

The two bodies have the same mean velocity: yes, exactly under $`C_{\rm pair}`$, for every $`W\in\mathcal W`$, every bound level and every $`g`$. By (17.15) both velocities are $`\kappa\,e\,\dot{\bar m}_i`$. The records change the state, and (11.8), at $`O(\kappa)`$ for fixed $`\lambda`$.

### Step 5. Second derivative in $`P`$ (item 2c)

From (11.1), $`\partial_P^2H=-\eta^2A_1-(1-\eta)^2A_2`$ (a lattice property: $`\partial_p^2\sin p=-\sin p`$). Second-order perturbation theory, with $`V_\eta:=\eta V_1+(1-\eta)V_2`$, $`Q_P:=\mathbb 1-\lvert\psi_P\rangle\langle\psi_P\rvert`$ and $`\mu`$ the spectral measure of $`H(P)`$ in the vector $`V_\eta\psi_P`$:

```math
E_b''(P)=-\eta^2\langle A_1\rangle_P-(1-\eta)^2\langle A_2\rangle_P-2\,\mathcal S_\eta(P),\qquad
\mathcal S_\eta(P):=\bigl\langle V_\eta\psi_P\big\vert Q_P\bigl(H(P)-E_b\bigr)^{-1}Q_P\big\vert V_\eta\psi_P\bigr\rangle=\int_{\mathrm{spec}H(P)\setminus\{E_b\}}\frac{\mathrm d\mu(E)}{E-E_b}.
\qquad\text{(11.9)}
```

The sum runs over the bands and the other bound levels. Each of the two parts depends on the convention $`\eta`$; their sum does not (M6).

### Step 6. Equation for the bound levels of a diagonal on-site binding (item 3a)

$`U=\lvert0\rangle\langle0\rvert\otimes W_0`$, with $`\lvert0\rangle`$ the place $`r=0`$. For $`E`$ outside the bands, $`(H^0+U-E)\psi=0`$ is equivalent to $`\psi=-(H^0-E)^{-1}\lvert0\rangle W_0\psi(0)`$, hence to $`[\mathbb 1_4+G\,W_0]\psi(0)=0`$ with $`G(E,P):=\langle0\rvert(H^0(P)-E)^{-1}\lvert0\rangle=\int\frac{\mathrm dq}{2\pi}(h_P(q)-E)^{-1}`$; a solution gives $`\psi(r)=-\int\frac{\mathrm dq}{2\pi}e^{iqr}(h_P(q)-E)^{-1}W_0\psi(0)`$, which is square-summable. The two parts of $`h_P(q)`$ commute, so $`(h_P(q)-E)^{-1}=\sum_{\sigma_1,\sigma_2}\Pi^{(1)}_{\sigma_1}\Pi^{(2)}_{\sigma_2}/(\sigma_1\omega_1+\sigma_2\omega_2-E)`$ with $`\Pi^{(i)}_\sigma=\frac12\bigl(\mathbb 1+\sigma(M_i\sigma^{(i)}_3-\tau_i\sin p_i\,\sigma^{(i)}_1)/\omega_i\bigr)`$ and $`\omega_i=\omega_i(p_i)`$. Under $`q\to q+\pi`$ both $`\sin p_i`$ change sign and the $`\omega_i`$ do not, so the terms with one factor $`\sin p_i`$ integrate to zero. $`G`$ has the diagonal elements $`G_{s_1s_2}`$ and the only other elements $`\langle11\vert G\vert22\rangle=\langle12\vert G\vert21\rangle=g_\times`$ (and their transposes). The bound levels of $`H(P)`$ are the solutions $`E`$ outside the bands of

```math
\begin{aligned}
&F_+(E,P)\,F_-(E,P)=0,\qquad F_+:=(1+w_{11}G_{11})(1+w_{22}G_{22})-w_{11}w_{22}\,g_\times^2,\quad F_-:=(1+w_{12}G_{12})(1+w_{21}G_{21})-w_{12}w_{21}\,g_\times^2,\\
&G_{s_1s_2}=\int_{-\pi}^{\pi}\frac{\mathrm dq}{2\pi}\sum_{\sigma_1,\sigma_2=\pm}\frac{\bigl(1+(-1)^{s_1-1}\sigma_1\frac{M_1}{\omega_1}\bigr)\bigl(1+(-1)^{s_2-1}\sigma_2\frac{M_2}{\omega_2}\bigr)}{4\,(\sigma_1\omega_1+\sigma_2\omega_2-E)},\qquad
g_\times=\int_{-\pi}^{\pi}\frac{\mathrm dq}{2\pi}\sum_{\sigma_1,\sigma_2=\pm}\frac{\sigma_1\sigma_2\,\tau_1\tau_2\sin p_1\sin p_2}{4\,\omega_1\omega_2\,(\sigma_1\omega_1+\sigma_2\omega_2-E)} .
\end{aligned}
\qquad\text{(11.10)}
```

The multiplicity of a level is $`\dim\ker(\mathbb 1_4+GW_0)`$. The two factors belong to the two sectors of the exact symmetry $`\Xi:=(-1)^{\hat r}\sigma^{(1)}_3\sigma^{(2)}_3`$, $`[\Xi,H(P)]=0`$, which holds for every diagonal on-site binding because each $`A_i`$ changes $`r`$ by one and flips one branch. $`F_+`$ ($`\Xi=+1`$: equal branches on even $`r`$, different branches on odd $`r`$) contains only $`w_{11},w_{22}`$; $`F_-`$ ($`\Xi=-1`$) only $`w_{12},w_{21}`$. Class: every diagonal on-site binding, all data; exact.

### Step 7. Regime $`\mathsf R`$: the bound level at the band $`\mathcal B_{++}`$ (item 3b)

In $`\mathsf R`$, $`H(P)=H_0+\epsilon H_1+\epsilon^2H_2`$ with $`H_0=M_1\sigma^{(1)}_3+M_2\sigma^{(2)}_3`$, $`\epsilon H_1=A_1+A_2`$, $`\epsilon^2H_2=U`$. The eigenvalue $`M_1+M_2`$ of $`H_0`$ (projector $`\Pi`$ onto the branches $`\lvert11\rangle`$, all $`r`$) is separated from the other three by at least $`2\min(M_1,M_2)`$. All terms are bounded uniformly in $`r`$, so degenerate perturbation theory applies: the part of $`H(P)`$ with spectrum near $`M_1+M_2`$ is unitarily equivalent, by a unitary that differs from $`\mathbb 1`$ by $`O(\epsilon)`$, to

```math
H_{\rm eff}(P)=M_1+M_2+\Pi\,U\,\Pi+\Pi\Bigl(\frac{A_1^2}{2M_1}+\frac{A_2^2}{2M_2}\Bigr)\Pi+O(\epsilon^4)\quad\text{in norm}.
```

Here $`\Pi A_i\Pi=0`$; $`A_i`$ leads to the branch value $`M_1+M_2-2M_i`$ of $`H_0`$; $`\Pi A_1A_2\Pi=0`$; and the odd orders vanish because $`\sigma^{(1)}_3\sigma^{(2)}_3`$ maps $`H`$ at $`\epsilon`$ to $`H`$ at $`-\epsilon`$. With $`A_i^2=\tau_i^2\sin^2p_i=2M_ia_i(1-\cos2p_i)`$, on the coefficient $`\psi(r)`$ of $`\lvert11\rangle`$:

```math
(H_{\rm eff}\psi)(r)=\bigl(M_1+M_2+a+w\,\delta_{r,0}\bigr)\psi(r)-\tfrac12\bigl[J\,\psi(r+2)+J^{*}\psi(r-2)\bigr],\qquad J(P):=a_1e^{2i\eta P}+a_2e^{-2i(1-\eta)P}=j(P)\,e^{i\alpha(P)} .
\qquad\text{(11.11)}
```

Of the four numbers only $`w_{11}`$ enters. Even and odd $`r`$ decouple, and the binding acts on even $`r`$ only. With $`\psi(2n)=e^{-i\alpha n}\phi(n)`$ this is a chain with the hopping $`-\frac j2`$ and one changed site: its band is $`M_1+M_2+a+[-j,j]`$ (the band $`\mathcal B_{++}(P)`$ at this order), and for $`w\neq0`$ it has exactly one further eigenvector, $`\phi(n)\propto\rho^{\lvert n\rvert}`$ with $`\lvert\rho\rvert<1`$. The equations at $`n\neq0`$ and at $`n=0`$ are $`E-(M_1+M_2+a)=-\frac j2(\rho+\rho^{-1})`$ and $`\frac j2(\rho-\rho^{-1})=w`$, hence $`\rho=-\varsigma\bigl(\sqrt{w^2+j^2}-\lvert w\rvert\bigr)/j`$ and

```math
E_b(P)=M_1+M_2+a+\varsigma\sqrt{w^2+j(P)^2}+O(\epsilon^4),\qquad j(P)^2=a_1^2+a_2^2+2a_1a_2\cos2P ,
\qquad\text{(11.12)}
```

```math
\psi_P(r)=\mathcal N_P\,e^{-i\alpha(P)\,r/2}\,\rho(P)^{\lvert r\rvert/2}\,\lvert11\rangle\ \ (r\ \text{even}),\qquad \psi_P(r)=0\ \ (r\ \text{odd}),\qquad \mathcal N_P^2=\frac{\lvert w\rvert}{\sqrt{w^2+j^2}},\qquad\text{up to } O(\epsilon).
\qquad\text{(11.13)}
```

The $`O(\epsilon)`$ part is $`\bigl(\frac{A_1}{2M_1}+\frac{A_2}{2M_2}\bigr)\psi_P`$: the branches $`\lvert21\rangle`$, $`\lvert12\rangle`$ on odd $`r`$. The odd orders of $`E_b`$ vanish, so the remainder in (11.12) is $`O(\epsilon^4)`$ against terms of order $`\epsilon^2`$.

- **Existence and number.** The level (11.12) is at the distance $`\sqrt{w^2+j^2}-j`$ from the band, of order $`\epsilon^2`$, and the remainder of $`H_{\rm eff}`$ is $`O(\epsilon^4)`$ in norm. So for small $`\epsilon`$: $`H(P)`$ has a bound level at a distance of order $`\epsilon^2`$ from $`\mathcal B_{++}(P)`$ if and only if $`\hat w_{11}\neq0`$. It is then exactly one, simple, for every $`P\in(-\pi,\pi]`$: below the band for $`\hat w_{11}<0`$, above the band for $`\hat w_{11}>0`$.
- **What the order leaves out.** Every other point of the spectrum near $`M_1+M_2`$ lies within $`O(\epsilon^4)`$ of the band. For $`\hat w_{11}=0`$, and in the sector $`\Xi=-1`$ (the branches $`\lvert11\rangle`$ on odd $`r`$, where $`w_{12},w_{21}`$ act at order $`\epsilon^4`$), a bound level, if any, is at such a distance and is not seen at leading order.
- **Other numbers.** $`w_{22}`$ enters $`E_b`$ at order $`\epsilon^4`$ (through $`g_\times`$ in $`F_+`$); $`w_{12},w_{21}`$ do not enter this level at any order.

### Step 8. Leading terms and the two limits (items 3c, 3d)

$`E_b`$ is analytic in the data with a remainder bounded uniformly near real data, so (11.12) can be differentiated and the remainders stay $`O(\epsilon^4)`$. From (11.5), (11.12), with $`(j^2)'(0)=0`$, $`(j^2)''(0)=-8a_1a_2`$, $`\partial_{M_i}a=-a_i/M_i`$, $`\tau_i\partial_{\tau_i}a=2a_i`$:

```math
E_{\rm bind}=a+\varsigma\sqrt{w^2+a^2},\quad E_b''(0)=-\varsigma\frac{4a_1a_2}{\sqrt{w^2+a^2}},\quad \langle\sigma^{(i)}_3\rangle_0=1-\frac{a_i}{M_i}\Lambda,\quad \langle A_i\rangle_0=2a_i\Lambda,\quad \langle U\rangle_0=\varsigma\frac{w^2}{\sqrt{w^2+a^2}},\qquad \Lambda=1+\frac{\varsigma\,a}{\sqrt{w^2+a^2}} .
\qquad\text{(11.14)}
```

Each is given up to $`O(\epsilon^4)`$; the terms shown (for $`\langle\sigma^{(i)}_3\rangle_0`$ the deviation from one) are of order $`\epsilon^2`$. The combination of the binding that enters is $`u=\lvert w_{11}\rvert/a`$. Limits within $`\mathsf R`$, with relative corrections $`O(u^2)`$ (wide) and $`O(u^{-2})`$ (tight):

```math
\begin{array}{l|ccc}
& \text{wide } (u\to0),\ w<0 & \text{wide } (u\to0),\ w>0 & \text{tight } (u\to\infty)\\ \hline
E_{\rm bind} & -\dfrac{w^2}{2a} & 2a+\dfrac{w^2}{2a} & w+a+\dfrac{a^2}{2w}\\
E_b''(0) & \dfrac{4a_1a_2}{a}\bigl(1-\tfrac{u^2}2\bigr) & -\dfrac{4a_1a_2}{a}\bigl(1-\tfrac{u^2}2\bigr) & -\dfrac{4a_1a_2}{w}\\
1-\langle\sigma^{(i)}_3\rangle_0 & \dfrac{a_i}{M_i}\dfrac{u^2}2 & \dfrac{2a_i}{M_i} & \dfrac{a_i}{M_i}\bigl(1+\tfrac aw\bigr)\\
\langle A_i\rangle_0 & a_iu^2 & 4a_i & 2a_i\bigl(1+\tfrac aw\bigr)\\
\langle U\rangle_0 & -\dfrac{w^2}{a} & \dfrac{w^2}{a} & w-\dfrac{a^2}{2w}
\end{array}
\qquad\text{(11.15)}
```

### Step 9. Curvature inertia, inertias of the parts and cost (item 4)

**(a)** With $`4a_1a_2/a=1/(\mathfrak m_1+\mathfrak m_2)`$, $`1/(4a_1a_2)=4\mathfrak m_1\mathfrak m_2`$ and $`\varsigma\sqrt{w^2+a^2}=E_{\rm bind}-a`$, (11.14) gives, at leading order in $`\mathsf R`$ (relative remainder $`O(\epsilon^2)`$), for both signs of $`w_{11}`$:

```math
\mathfrak m_b=-\varsigma\,(\mathfrak m_1+\mathfrak m_2)\sqrt{1+u^2}=\mathfrak m_1+\mathfrak m_2-4\,\mathfrak m_1\mathfrak m_2\,E_{\rm bind} .
\qquad\text{(11.16)}
```

The difference $`\mathfrak m_b-(\mathfrak m_1+\mathfrak m_2)`$ has the sign of $`-w_{11}`$, which is the sign of $`-E_{\rm bind}`$. For $`w_{11}<0`$ it is $`(\mathfrak m_1+\mathfrak m_2)(\sqrt{1+u^2}-1)>0`$, which grows from $`(\mathfrak m_1+\mathfrak m_2)u^2/2`$ (wide) to $`(\mathfrak m_1+\mathfrak m_2)u`$ (tight). For $`w_{11}>0`$, $`\mathfrak m_b<0`$ and the difference is $`-(\mathfrak m_1+\mathfrak m_2)(\sqrt{1+u^2}+1)`$. Through $`E_{\rm bind}`$ it is $`-4\mathfrak m_1\mathfrak m_2E_{\rm bind}`$, for a wide pair and for every $`u`$. All terms of (11.16) are of order $`\epsilon^{-2}`$.

**(b)** Let $`\tau_1=\tau_2=\tau`$, so $`\tau^2(\mathfrak m_1+\mathfrak m_2)=M_1+M_2`$ and $`4\tau^2\mathfrak m_1\mathfrak m_2=4M_1M_2/\tau^2`$. From (11.16) and (11.14):

```math
\tau^2\mathfrak m_b=M_1+M_2-\frac{4M_1M_2}{\tau^2}E_{\rm bind}+O(\epsilon^2),\qquad M_1+M_2+E_{\rm bind}=M_1+M_2+O(\epsilon^2),\qquad \sum_iM_i\langle\sigma^{(i)}_3\rangle_0=M_1+M_2-a\Lambda+O(\epsilon^4).
\qquad\text{(11.17)}
```

- $`\tau^2\mathfrak m_b`$ against the cost $`M_1+M_2+E_{\rm bind}`$: not at all. The leading difference is $`-\frac{4M_1M_2}{\tau^2}E_{\rm bind}=(M_1+M_2)\bigl(-\varsigma\sqrt{1+u^2}-1\bigr)`$, of order $`\epsilon^0`$, while the binding changes the cost by $`E_{\rm bind}=O(\epsilon^2)`$ with the opposite sign. The two agree only in the limit $`u\to0`$ with $`w_{11}<0`$, and exactly without a binding (d).
- $`\tau^2\mathfrak m_b`$ against $`\sum_iM_i\langle\sigma^{(i)}_3\rangle_0`$: not at all, with the same leading difference.
- The cost against $`\sum_iM_i\langle\sigma^{(i)}_3\rangle_0`$: they agree at order $`\epsilon^0`$ and differ at order $`\epsilon^2`$ by $`\langle A_1\rangle_0+\langle A_2\rangle_0+\langle U\rangle_0=2a\Lambda+\varsigma w^2/\sqrt{w^2+a^2}`$; this difference is exact by (11.6).

**(c)** Comparison with (21.15), (21.16) of 03-ilang-space/21-composite-body, in label units ($`\mathfrak m\leftrightarrow\sigma_X^2I`$).
- Common: the same function, $`\mathfrak m_b/(\mathfrak m_1+\mathfrak m_2)=\sqrt{1+u^2}`$ against $`I_c/2I_1=\sqrt{1+U^2/16t^2}`$, where in both cases the binding is divided by the half-width of the two-body band at total label zero ($`a`$ here, $`4t`$ there); an attractive binding raises the inertia, and the excess is linear in $`E_{\rm bind}`$ for every strength.
- Different, the coefficient: there $`I_c-2I_1=-E_{\rm bind}/v_{\max}^2`$, which is $`-\mathfrak m_1\mathfrak m_2E_{\rm bind}`$; here $`-4\mathfrak m_1\mathfrak m_2E_{\rm bind}`$. The factor $`4`$ arises because the upper branch moves by two labels per step (11.11), so $`a=\frac14(1/\mathfrak m_1+1/\mathfrak m_2)`$. With (5.11) the coefficient here is $`4M_1M_2/\tau^4`$ for $`\tau_1=\tau_2`$: it contains the rest costs and is not $`1/v_{\max}^2`$.
- Different, the cost: there, without rest terms, $`I_cv_{\max}^2=\sqrt{U^2+16t^2}=-E_{\min}(t,U)`$ by (21.12), for every $`U`$. Here a rest cost exists, and by (11.17) $`\tau^2\mathfrak m_b`$ does not follow the cost of the pair.
- Different, the notion: (21.15) is an inertia from a response; $`\mathfrak m_b`$ is a curvature.

**(d) Control, no binding.** For $`W=0`$ there is no bound level; the lower edge of $`\mathcal B_{++}(P)`$ is $`e(P)=\min_{p_1}[\omega_1(p_1)+\omega_2(P-p_1)]`$. At the minimum $`\omega_1'(p_1)=\omega_2'(p_2)`$, and for a minimum over a split of $`P`$ the inverse curvatures add. With (6.7), exactly and for all data:

```math
\frac1{e''(0)}=\mathfrak m_1+\mathfrak m_2=\frac{M_1}{\tau_1^2}+\frac{M_2}{\tau_2^2},\qquad e(0)=M_1+M_2,\qquad \langle\sigma^{(i)}_3\rangle=1 .
\qquad\text{(11.18)}
```

For $`\tau_1=\tau_2=\tau`$ the three quantities of (b) agree exactly: $`\tau^2/e''(0)=M_1+M_2`$. For $`\tau_1\neq\tau_2`$ they do not: $`\tau_1^2/e''(0)-(M_1+M_2)=M_2(\tau_1^2/\tau_2^2-1)\neq0`$, and the ratio $`1/[e''(0)(M_1+M_2)]`$ lies strictly between $`\tau_1^{-2}`$ and $`\tau_2^{-2}`$ and depends on $`M_1/M_2`$, hence on the clock levels. So the difference in (b) is caused by the binding, and for $`\tau_1\neq\tau_2`$ the comparison with a cost fails already without one. (11.16) holds for $`\tau_1\neq\tau_2`$ unchanged.

### Step 10. Clocks of the parts (item 5)

**(a)** Start: the clock label of the part $`i`$ in $`\lvert0\rangle=N_i^{-1/2}\sum_k\lvert f_k\rangle`$, the other part on its level $`k_j`$, the medium in $`\chi`$, and the positions and branches in $`\Phi`$ of Step 4, built from the bound eigenvectors of the levels $`(0,k_j)`$ with $`\lvert g\rvert^2`$ of width $`\delta P`$ around $`0`$. The levels are conserved, so the component on $`\lvert f_k\rangle`$ evolves with $`M_i\to m_i+d^{(i)}_k`$. Let $`g_0`$ be the distance of $`E_b(0)`$ from the rest of the spectrum and $`\delta_i:=d^{(i)}_{N_i-1}/g_0`$. By (11.5) and perturbation theory in $`d^{(i)}_k`$, the bound eigenvector changes by $`O(\delta_i)`$ and $`E^{[k]}_b(P)=E^{[0]}_b(P)+d^{(i)}_k\langle\sigma^{(i)}_3\rangle_P+O\bigl((d^{(i)}_k)^2/g_0\bigr)`$. For a diagonal on-site binding $`\psi(r)\to\sigma^{(1)}_3\sigma^{(2)}_3\psi(-r)`$ maps $`H(P)`$ to $`H(-P)`$, so $`E_b`$ and $`\langle\sigma^{(i)}_3\rangle_P`$ are even in $`P`$: the pair is at rest by (11.8), and $`\langle\sigma^{(i)}_3\rangle_P=\langle\sigma^{(i)}_3\rangle_0+O(P^2)`$. The reading of the clock label of $`i`$ (the partition by $`a_i`$, (1.3)) has the statistics $`N_i^{-2}\sum_{k,k'}e^{2\pi i(k-k')a/N_i}\langle\Psi_{k'}(\lambda)\vert\Psi_k(\lambda)\rangle`$ with $`\langle\Psi_{k'}\vert\Psi_k\rangle=e^{-i(d_k-d_{k'})\langle\sigma_3^{(i)}\rangle_0\lambda}`$ up to the remainders. With $`d^{(i)}_k=\frac{2\pi k}{N_i\lambda_{0,i}}`$ and (5.1), in the form of (5.21):

```math
q_i(a;\lambda)=P_{N_i}\Bigl(a;\Gamma_i\frac{\lambda}{\lambda_{0,i}}\Bigr)+\mathcal R_i,\qquad \Gamma_i=\langle\sigma^{(i)}_3\rangle_0=\frac{\partial E_b(0)}{\partial M_i},\qquad \mathcal R_i=O\bigl(\delta_i^2(1+g_0\lambda)\bigr)+O\bigl(\delta P^2(1+\lambda/\lambda_{0,i})\bigr)+O(\kappa).
\qquad\text{(11.19)}
```

The rate is $`\Gamma_i/\lambda_{0,i}`$. Its ratio to the rate $`1/\lambda_{0,i}`$ of the free part at rest ((5.21) with $`\Gamma(0)=1`$) is $`\Gamma_i=\langle\sigma^{(i)}_3\rangle_0\le1`$, taken on the levels $`(0,k_j)`$. Class: every diagonal on-site binding and every simple bound level at $`P=0`$; status: first order in the level spacing, remainder $`\mathcal R_i`$.

**(b)** With (11.14), at leading order in $`\mathsf R`$ (remainder $`O(\epsilon^4)`$), with $`M_i=m_i`$ and $`M_j=M^{(j)}_{k_j}`$:

```math
\Gamma_i=1-\frac{\tau_i^2}{4M_i^2}\,\Lambda,\qquad \Lambda=1+\frac{\varsigma}{\sqrt{1+u^2}},\qquad \frac{1-\Gamma_1}{1-\Gamma_2}=\frac{\tau_1^2/M_1^2}{\tau_2^2/M_2^2}.
\qquad\text{(11.20)}
```

Both clocks are slowed. They are not slowed by the same factor: $`\Lambda`$ is common, and the factors agree at this order if and only if $`\tau_1/M_1=\tau_2/M_2`$ (for example equal data). For a wide pair with $`w_{11}<0`$, $`1-\Gamma_i=\frac{\tau_i^2}{8M_i^2}u^2`$; for a tight pair $`1-\Gamma_i=\frac{\tau_i^2}{4M_i^2}(1+\frac aw)`$. Without a binding $`\Gamma_i=1`$.

## Result

Classes, regimes and statuses. Items 1 and 2 hold for every $`W\in\mathcal W`$, all data, every simple bound level and every $`P\in\mathcal P`$; they are exact. Item 3(a) and the control 4(d) are exact, for every diagonal on-site binding (4(d): no binding) and all data. Items 3(b)–(d), 4(a)–(c) and 5(b) hold for every diagonal on-site binding in $`\mathsf R`$ at leading order, with the remainders stated. Item 5(a) holds for every diagonal on-site binding and all data, at first order in the level spacing of the clock.

1. **Structure.** $`H(P)`$ is (11.1), with the convention $`\eta`$. The two-body bands and their edges at $`P=0`$ are (11.2), for every $`W`$. The replacements are (11.3); the range condition fixes $`U`$, and only constants remain. The seven answers are (11.4): $`E_b(P)`$ alone is not well defined, the other six are (for $`M_i`$: as half the gap).
2. **Exact relations.** The five derivatives are (11.5) and the scaling relation is (11.6). $`E_b'(P)=\langle V_1\rangle_P=\langle V_2\rangle_P`$ (11.7), and both mean position labels move at the rate $`\int\lvert g\rvert^2E_b'`$ (11.8): the two bodies have the same mean velocity. $`E_b''(P)`$ is (11.9).
3. **Diagonal on-site binding.** The equation is (11.10), exact for all data. In $`\mathsf R`$: a bound level at a distance of order $`\epsilon^2`$ from $`\mathcal B_{++}`$ exists iff $`\hat w_{11}\neq0`$, it is one, with $`E_b(P)`$ of (11.12) (remainder $`O(\epsilon^4)`$) and $`\psi_P`$ of (11.13) (up to $`O(\epsilon)`$), from the effective contract (11.11); only $`w_{11}`$ enters. The five leading terms are (11.14), the limits (11.15).
4. **Curvature, inertias, cost.** $`\mathfrak m_b=\mathfrak m_1+\mathfrak m_2-4\mathfrak m_1\mathfrak m_2E_{\rm bind}`$ (11.16), relative remainder $`O(\epsilon^2)`$. For $`\tau_1=\tau_2`$, $`\tau^2\mathfrak m_b`$ differs from the cost of the pair and from $`\sum_iM_i\langle\sigma^{(i)}_3\rangle_0`$ at order $`\epsilon^0`$, by $`-\frac{4M_1M_2}{\tau^2}E_{\rm bind}`$ (11.17). The comparison with 03-ilang-space/21-composite-body is Step 9(c). The control without a binding is (11.18), exact.
5. **Clocks.** The statistics are (11.19) with the ratio $`\Gamma_i=\langle\sigma^{(i)}_3\rangle_0`$. In $`\mathsf R`$, $`\Gamma_i`$ is (11.20): the two clocks are not slowed by the same factor unless $`\tau_1/M_1=\tau_2/M_2`$.

Controls (M9). (11.5)–(11.9) are proven for the whole class, so no member violates them. The leading-order results fail outside $`\mathsf R`$: for $`\tau_i/M_i`$ of order one the closed forms (11.14) are off by $`8`$ per cent ($`E_b''(0)`$) to $`23`$ per cent ($`\langle U\rangle_0`$) (set E under "Code"). Further controls: no binding (11.18), $`\tau_1\neq\tau_2`$ (Step 9d), wide against tight (11.15).

## Consistency checks

1. **Dimensions.** $`\tau_i`$, $`M_i`$, $`w`$, $`a_i`$, $`j`$, $`E_b`$, $`E_b''`$ are costs ($`P`$ and $`q`$ are numbers); $`u`$, $`\rho`$, $`\Lambda`$, $`\langle\sigma^{(i)}_3\rangle`$, $`\Gamma_i`$ are numbers; $`\mathfrak m`$ is an inverse cost, and so is $`\mathfrak m_1\mathfrak m_2E_{\rm bind}`$ in (11.16); $`\Gamma_i\lambda/\lambda_{0,i}`$ in (11.19) is a number. Passed.
2. **No binding.** For $`w\to0^-`$, (11.12) tends to $`M_1+M_2+a-j(P)`$, the lower edge of $`\mathcal B_{++}(P)`$ at this order, and (11.14) gives $`E_b''(0)\to4a_1a_2/a=1/(\mathfrak m_1+\mathfrak m_2)`$, which is (11.18), with $`\langle\sigma^{(i)}_3\rangle_0\to1`$, $`\langle A_i\rangle_0\to0`$, $`\langle U\rangle_0\to0`$, $`\Gamma_i\to1`$. Passed.
3. **Scaling relation on the closed form.** With (11.14) the right side of (11.6) at $`P=0`$ is $`M_1+M_2-a\Lambda+2a\Lambda+\varsigma\frac{w^2}{\sqrt{w^2+a^2}}=M_1+M_2+a+\varsigma\frac{a^2+w^2}{\sqrt{w^2+a^2}}=E_b(0)`$ of (11.12). Passed.

## Open issues

- Whether $`\mathfrak m_b`$ is the inertia of the pair in a response to a gradient is not derived here (not asked; (11.17) shows that it is not the cost divided by $`\tau^2`$).
- Outside the order asked in item 3(b): bound levels closer than $`O(\epsilon^4)`$ to the band (for $`\hat w_{11}=0`$, and in the sector $`\Xi=-1`$) are neither established nor excluded.
- The coefficients of the $`O(\epsilon^4)`$ remainders are not derived; the code only confirms their order.
- (11.19) is of first order in the level spacing and needs $`d^{(i)}_{N_i-1}\ll g_0`$; in $`\mathsf R`$ the isolation $`g_0`$ is of order $`\epsilon^2`$.

## Code

`code/v1/check_bound_pair.py` (role: check; outputs `code/v1/output/check_bound_pair.txt`, a log, and `code/v1/output/check_bound_pair.json`, all numbers). It builds $`H(P)`$ of (11.1) with $`\eta=\frac12`$ on $`r=-L,\dots,L`$ with open ends and diagonalizes it: densely, once per set and $`P`$ (all eigenvectors, needed for (11.9)), and with a banded shift-and-invert solver for the finite differences and the doubled range. The bound level is the eigenvector of largest weight on $`(r=0,\lvert11\rangle)`$. Derivatives of $`E_b`$ are five-point differences (step $`0.01`$ in $`P`$, relative step $`10^{-3}`$ in $`M_i`$, $`\tau_i`$, $`\theta`$). Nothing in the derivation rests on the code.

- **Range of $`r`$ and convergence.** $`L=120`$ ($`964`$ components). Convergence was checked in two ways: $`E_b`$ at $`L=240`$ differs by less than $`10^{-13}`$, and the weight of $`\psi_P`$ at $`\lvert r\rvert>60`$ is at most $`5\times10^{-8}`$ (set D) and below $`10^{-19}`$ otherwise. $`E_b`$ at $`\eta=0,0.3,1`$ and from the two solvers agrees to $`10^{-13}`$.
- **Parameter sets** ($`M_1,M_2;\ \tau_1,\tau_2;\ w_{11}`$; the other three $`w_{s_1s_2}`$ are non-zero and of the same order), each at $`P\in\{0,\pm0.15,\pm0.30\}`$: A $`(1,1;\ 0.1,0.1;\ -0.004)`$, equal data; B $`(1,1.7;\ 0.2,0.12;\ -0.01)`$; C $`(1,0.8;\ 0.1,0.15;\ +0.02)`$, level above the band; D $`(1.3,1;\ 0.15,0.2;\ -0.004)`$, wide; E $`(1,1.3;\ 1,0.8;\ -0.6)`$, $`\tau_i/M_i`$ of order one. In all sets the level is outside the bands and has $`\langle\Xi\rangle_P=+1`$ (`Gamma` in the output files).
- **Exact relations, all five sets and all $`P`$** (largest absolute deviation): (11.5) derivatives against expectation values, below $`10^{-10}`$; (11.6), below $`10^{-14}`$; (11.7) $`E_b'`$ against $`\langle V_1\rangle_P`$ and $`\langle V_2\rangle_P`$, below $`2\times10^{-10}`$ (below $`10^{-11}`$ in A–D), and $`\langle V_1\rangle_P-\langle V_2\rangle_P`$ below $`10^{-15}`$; (11.9) against the difference quotient, below $`10^{-9}`$; (11.10): the coefficients against a direct inversion of $`h_P(q)-E`$, relative deviation below $`10^{-12}`$, and the root of $`F_+`$ against $`E_b`$, below $`10^{-14}`$. These are the sizes of the rounding and truncation errors of the differences.
- **Closed forms, sets in $`\mathsf R`$.**

| set | $`\max_i\tau_i/M_i`$ | $`u`$ | $`\max_P\lvert E_b-(11.12)\rvert`$ | the same over $`(\max\tau_i/M_i)^4`$ | rel. deviation of $`E_b''(0)`$ | the same over $`(\max\tau_i/M_i)^2`$ |
| --- | --- | --- | --- | --- | --- | --- |
| A | 0.10 | 0.80 | $`2.1\times10^{-6}`$ | 0.021 | $`3.2\times10^{-4}`$ | 0.032 |
| B | 0.20 | 0.83 | $`8.3\times10^{-6}`$ | 0.005 | $`5.4\times10^{-4}`$ | 0.014 |
| C | 0.19 | 2.10 | $`2.0\times10^{-4}`$ | 0.164 | $`1.7\times10^{-2}`$ | 0.47 |
| D | 0.20 | 0.28 | $`7.7\times10^{-7}`$ | 0.0005 | $`3.6\times10^{-5}`$ | 0.001 |
| E (control) | 1.0 | 1.61 | $`4.6\times10^{-2}`$ | 0.046 | $`7.7\times10^{-2}`$ | 0.077 |

  The expectation values of (11.14) agree with the numerical ones to $`2.1\times10^{-5}`$ (A, B, D) and $`5.3\times10^{-4}`$ (C), a fraction of $`(\tau_i/M_i)^2`$ of their leading terms. (11.16), $`\mathfrak m_b-(\mathfrak m_1+\mathfrak m_2)`$ against $`-4\mathfrak m_1\mathfrak m_2E_{\rm bind}`$ with the numerical $`E_{\rm bind}`$: A $`56.043`$ against $`56.045`$; B $`42.321`$ against $`42.326`$; C $`-455.96`$ against $`-447.76`$ ($`\mathfrak m_b<0`$); D $`3.169`$ against $`3.161`$.
- **Next order in $`\epsilon`$** (set B with $`\tau_i\to\epsilon'\tau_i`$, $`w_{s_1s_2}\to\epsilon'^2w_{s_1s_2}`$, $`\epsilon'=1,\frac12,\frac14,\frac18`$): each halving of $`\epsilon'`$ divides $`E_b-(11.12)`$ by $`16.00`$ (at $`P=0`$ and at $`P=0.3`$), $`\langle\sigma^{(i)}_3\rangle_0-(11.14)`$ by $`15.6`$ to $`16.0`$, and the relative deviation of $`E_b''(0)`$ by $`3.97`$ to $`4.00`$. The remainders are of order $`\epsilon^4`$, and of relative order $`\epsilon^2`$ for $`E_b''(0)`$, as stated.
- **Control E.** Outside $`\mathsf R`$ the exact relations hold as above, while $`E_{\rm bind}=-0.288`$ against $`-0.333`$ from (11.14) and $`E_b''(0)`$ is off by $`7.7`$ per cent.

No check failed and no step of the derivation was changed after a check.

## Methods used

- Fibre decomposition of a shift-invariant two-body contract (total plane-wave label)
- Weyl's theorem on the essential spectrum
- Hellmann–Feynman theorem; second-order perturbation theory; Euler's relation for homogeneous functions
- Resolvent (Green function) equation for a rank-four on-site change
- Degenerate perturbation theory (Schrieffer–Wolff) and the one-defect chain
- Commutator identity for the relative coordinate in a bound state
- Numerical diagonalization, finite differences (check)
