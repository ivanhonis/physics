# Fall of a bound pair of two bodies in a sharp field

- **Subproject:** 05-ilang-free-fall
- **Package:** 13-pair-fall
- **Version:** v2
- **Mode:** internal regeneration
- **Date:** 2026-10-11

## Changes from previous version

Trigger: `review.v1.md` (three minor issues, I1–I3) and the three amendments of the question of 2026-10-11. Every sentence, display and tag (13.1)–(13.20) of v1 that is not listed here is kept word for word; no tag is renumbered or withdrawn. New tags: (13.21), (13.22). The amendment on $`C_{\rm bod}`$ (fixed up to an additive constant) needs no change: Step 2.3 states it.

- **Header.** Version and mode; this section is new.
- **I1 (derivatives of leading-order forms).**
  - Setup, bullet "Inputs": one sentence added at the end ("With (11.14) the question quotes ...").
  - Step 7.2: the sentence "The term of order $`\epsilon^2`$ follows from (13.17) by differentiation in the data; it assumes that the remainder of (11.20) stays $`O(\epsilon^4)`$ under one derivative in $`M_1,M_2`$, and it contains the gradient of the other part." is replaced by "The term of order $`\epsilon^2`$ contains the gradient of the other part. Both are derived as follows." and by four bullets with the new displays (13.21), (13.22). Why: $`\varrho_i`$ is a derivative of the rate in the data. It is now derived as such, from the second derivatives of (11.12) in $`M_1,M_2`$, with the statement of 11-bound-pair that the question now quotes with (11.14). The assumption is removed. The display (13.18) is unchanged.
  - Step 7.3: one bullet added at the end ("Derivatives used: ...").
  - Step 7.4: one sentence added at the end ("(13.20) is (13.19) for ...").
  - Result, item 4: the parenthesis is extended, "from (13.21), (13.22)" is added after "relative change (13.18)", and the sentence "The term of order $`\epsilon^2`$ in (13.18) rests on an assumption on the remainder of (11.20); (13.19) and (13.20) do not use it." is replaced by two sentences. Why: (13.19) and (13.20) do use the leading order of $`\varrho_i`$.
  - Open issues: the sentence "The $`\epsilon^2`$ term of (13.18) assumes a differentiable remainder of (11.20)." is removed from the fourth item; a seventh item is added (how the quoted statement is read).
- **I2 (exceptional members).**
  - JSON twin: key result (13.19) is stated with its condition and its exceptional members. The other key results were read against their displays; completed with a class, a condition, a remainder or an exceptional member: (13.2), (13.9), (13.10), (13.11), (13.13)–(13.18), (13.20). Unchanged: (13.1), (13.3), (13.7), (13.8), (13.12). Added: (13.21), (13.22).
  - Table of item 5, three cells changed: row 1, last column (the exceptional member $`u_*`$ added); row 3, third column ("for $`g_i\neq0`$:" added); row 3, last column (the exceptional members of Step 7.3 added, with the tag (13.19)). The other cells were read against (4.16), (13.13)–(13.16), (13.20) and are unchanged.
- **I3 (the other order of the limits).**
  - Step 5.3: the argument is kept; four bullets are added at its end ("Answer to item 2(c) as amended ..."). They state the result, add a sufficient condition for $`\mathsf f_i\neq0`$ (two lines, from (13.6)), and name two exceptional members that v1 covered by "in general".
  - Result, item 2(c): the sentence "In the other order the limit does not exist on the class in general." is replaced.
  - Open issues, second item: "The limit $`\delta P\to0`$ at a fixed window is only shown not to exist on the class in general; the quantity it defines on a subclass is not characterized." is restated as outside the scope of the question.
- **Code.** `code/v2/pair_fall_check.py` is the script of v1 with the paths changed and one table added (the derivative of the clock ratio in the data against (13.22), for I1). Changed sentences: the path in Step 4.4; in the section "Code" the bullets "File" and "Run", one sub-bullet added under "What it does", and the new bullet "Item 4". All numbers of v1 are reproduced.
- **Methods used.** Two keywords added.

## Setup and assumptions

- **Setting.** Objects, contract $`C`$, class $`\mathcal W`$, records, field, levels, bound level, packets, orders and the regime $`\mathsf R`$ are those of the question, used literally. Assumptions of the package (M8, A11): two Model D bodies, one medium with one operator and one strength, a binding of the class $`\mathcal W`$ without a factor of the field, the field coupled to the rest and clock terms only, the field start $`\varphi`$ sharp and stationary, and a packet of a bound level as the start (M9). Equal parameters of the two types are never assumed.
- **Inputs, as quoted in the question:** (11.1), (11.2), (11.5)–(11.9), (11.12)–(11.14), (11.16), (11.19)–(11.22) of 11-bound-pair; (8.10), (8.11) of 08-two-types; (2.1), (2.3) of 02-field-object; (4.7), (4.10), (4.11), (4.16), (4.24) of 04-branch-fall; (5.1), (5.5), (5.6), (5.11) of 04-ilang-time/05-moving-clock; (17.15) of 03-ilang-space/17-motion; (16.11) of 03-ilang-space/16-common-space. With (11.14) the question quotes the statement of Step 8 of 11-bound-pair on the differentiation of (11.12) in the data; it is used in Step 7.2.
- **Notation added here.**
  - The packet weight is written $`g(P)`$ and enters only through $`g`$, $`g'`$ and $`\langle F\rangle_g:=\int\mathrm dP\,\lvert g(P)\rvert^2F(P)`$. The common gradient ($`g`$ in the question) is written $`g_{\rm c}:=g_1=g_2`$.
  - $`\mathfrak h:=\ell^2(\mathbb Z)\otimes\mathbb C^2\otimes\mathbb C^2`$ is the fibre space; $`\lvert P;\psi\rangle(x_1,x_2)=(2\pi)^{-1/2}e^{iP(\eta x_1+(1-\eta)x_2)}\psi(x_1-x_2)`$, so that $`\langle P;\psi\vert P';\psi'\rangle=\delta(P-P')\langle\psi\vert\psi'\rangle`$ and $`\lVert\Phi_g\rVert=1`$.
  - $`\Gamma(P)>0`$ is the distance of $`E_b(P)`$ from the rest of the spectrum of $`H(P)`$; $`R_P:=Q_P(H(P)-E_b(P))^{-1}Q_P`$ with $`\lVert R_P\rVert=1/\Gamma(P)`$; $`\mathcal U_P(\lambda):=\mathbb 1-e^{-i(H(P)-E_b(P))\lambda}`$; $`I_g`$ as in (11.8); $`\Gamma_g:=\min_{I_g}\Gamma>0`$.
  - $`\mathsf b:=\lvert g_1\rvert M_1+\lvert g_2\rvert M_2+2\kappa\lvert\langle X\rangle\rvert`$, $`\mathsf d_\eta:=\lvert1-\eta\rvert\lvert g_1\rvert M_1+\lvert\eta\rvert\lvert g_2\rvert M_2+\lvert1-2\eta\rvert\kappa\lvert\langle X\rangle\rvert`$, $`\tau_{\min}:=\min(\tau_1,\tau_2)`$.
- **Standard facts used.**
  - F1 (first order in a term of the contract): $`e^{-i(H_0+\Delta)\lambda}=e^{-iH_0\lambda}-i\int_0^\lambda\mathrm ds\,e^{-iH_0(\lambda-s)}\Delta\,e^{-iH_0s}+O(\Delta^2)`$ at fixed $`\lambda`$.
  - F2 (isolated simple eigenvalue of an analytic family): $`E_b`$ and $`\psi_P`$ are analytic in $`P`$ and in the data, $`Q_P\psi_P'=-R_PV_\eta\psi_P`$, and $`\langle\psi_P\vert\psi_P'\rangle\in i\mathbb R`$.
  - F3: an eigenvector of $`H(P)`$ for an eigenvalue outside the bands (11.2) decays exponentially in $`\lvert r\rvert`$ (finite range of the hopping and of $`W`$), locally uniformly in $`P`$; hence $`\hat r\psi_P\in\mathfrak h`$.
  - F4 (long chain): at fixed $`\lambda`$ the first-order coefficients on the chain $`\lvert x_i\rvert\le L`$ converge for $`L\to\infty`$ to those of the infinite chain, because the hopping has range one and $`\Phi_g`$, $`\hat x_i\Phi_g`$ are square summable.
- **Approximations and their range.** First order in $`(g_1,g_2,\kappa\langle X\rangle)`$ at fixed $`\lambda`$ (the size of the second order is not estimated). Records at leading order in $`\kappa`$ with the convention of the question: the bodies evolve by $`C_{\rm bod}`$. Items 3 and 4 at leading order in $`\mathsf R`$ at fixed $`u`$; their remainders are not uniform in $`u`$.

## Derivation

### Step 1. Reduced contract (item 1a)

1. Every term of $`C`$ is the identity on $`\mathcal H_f`$, or $`\theta_i\,\hat x_i\otimes G_i\otimes\Phi`$, or $`C_f`$. With $`\Phi\varphi=\gamma\varphi`$ and $`C_f\varphi=e_f\varphi`$, for every $`\Psi\in\mathcal H_{b_1}\otimes\mathcal H_{b_2}\otimes\mathcal H_c`$ (the computation of (2.3) and (8.10); $`U`$ is carried along unchanged):

```math
C\,(\Psi\otimes\varphi)=\bigl((C_{\rm red}+e_f)\Psi\bigr)\otimes\varphi,\qquad C_{\rm red}=\sum_{i=1,2}\Bigl[A_i+\sum_xP^{(i)}_x\otimes(1+g_ix)\,G_i+\kappa\,\hat x_i\otimes X\Bigr]+U .
\qquad\text{(13.1)}
```

2. Hence $`e^{-iC\lambda}(\Psi\otimes\varphi)=e^{-ie_f\lambda}\,(e^{-iC_{\rm red}\lambda}\Psi)\otimes\varphi`$ for all $`\lambda`$: the view of $`\{b_1,b_2,c\}`$ is pure and evolves by $`C_{\rm red}`$ (exact, for this start of the field only).
3. $`C_{\rm red}`$ is the contract of an admissible description of $`b_1,b_2,c`$. It is self-adjoint and independent of $`\lambda`$; $`U`$ is a pair term of $`b_1,b_2`$; $`\kappa\,\hat x_i\otimes X`$ are pair terms of $`b_i,c`$; $`A_i+\sum_xP^{(i)}_x\otimes(1+g_ix)G_i`$ acts on one object and is included in a pair term (A5). Its position-dependent rest and clock term is then a property of the type of $`b_i`$ (A10).
4. A binding with a factor of the field needs a term on $`\mathcal H_{b_1}\otimes\mathcal H_{b_2}\otimes\mathcal H_f`$, for example $`\sum_{x_1,x_2}\lvert x_1\rangle\langle x_1\rvert\otimes\lvert x_2\rangle\langle x_2\rvert\otimes W(x_1-x_2)\otimes\Phi_{x_1x_2}`$, that is not a sum of pair terms. Decompose the operators of each object into $`\mathbb C\mathbb 1`$ and the traceless ones: a sum of pair terms has no component that is traceless on all three objects, while $`U'\otimes\Phi'`$ has one whenever $`U'\neq u_1\otimes\mathbb 1+\mathbb 1\otimes u_2`$ and $`\Phi'\notin\mathbb C\mathbb 1`$. Such a three-object term is not of the form (1.10).

### Step 2. The operator on the two bodies (item 1b)

1. The partial expectation of $`C-e_f`$ in $`\chi\otimes\varphi`$ is, by (13.1),

```math
C_{\rm bod}=C^{\rm D}_1+C^{\rm D}_2+U+\sum_{i=1,2}g_i\,\hat x_i\otimes G_i+\kappa\langle X\rangle\,(\hat x_1+\hat x_2).
\qquad\text{(13.2)}
```

2. $`[C_{\rm bod},D_i]=0`$, so the levels are conserved, and $`G_i=M_i\sigma^{(i)}_3`$ on the levels $`k_1,k_2`$. With $`\hat x_1=\hat X_\eta+(1-\eta)\hat r`$ and $`\hat x_2=\hat X_\eta-\eta\hat r`$ the gradient terms $`\Delta:=C_{\rm bod}-C_{\rm pair}`$ are

```math
\begin{aligned}
\Delta&=\hat X_\eta\,\mathcal K+\hat r\,\mathcal D_\eta,\qquad \mathcal K:=g_1M_1\sigma^{(1)}_3+g_2M_2\sigma^{(2)}_3+2\kappa\langle X\rangle,\\
\mathcal D_\eta&:=(1-\eta)\,g_1M_1\sigma^{(1)}_3-\eta\,g_2M_2\sigma^{(2)}_3+(1-2\eta)\,\kappa\langle X\rangle .
\end{aligned}
\qquad\text{(13.3)}
```

3. Well-definedness (M6). A replacement of the listed terms that leaves $`C`$ unchanged leaves $`\langle\chi\otimes\varphi\vert C\vert\chi\otimes\varphi\rangle`$ unchanged. It can change the listed $`C_f`$ by a multiple of $`\mathbb 1`$, hence $`e_f`$: $`C_{\rm bod}`$ is fixed by $`C`$, $`\chi`$, $`\varphi`$ up to an additive real constant, which drops out of everything below. Let $`b(x_1,x_2)`$ be the block of $`C_{\rm bod}`$ that is diagonal in both positions, an operator on the internal labels. For $`\lvert x_1-x_2\rvert>R`$ it is $`(1+g_1x_1)G_1+(1+g_2x_2)G_2+\kappa\langle X\rangle(x_1+x_2)`$ up to the constant. $`G_1`$ and $`G_2`$ are traceless and act on the labels of one body each, so the three parts are linearly independent: $`\kappa\langle X\rangle`$ is the normalized trace of $`b(x_1+1,x_2)-b(x_1,x_2)`$ (both arguments in that region), $`g_1G_1`$ is its traceless part, and $`G_1`$ is the traceless part of $`b(0,x_2)`$ on the labels of $`b_1`$; likewise for $`b_2`$.
   - $`g_1`$, $`g_2`$, $`\kappa\langle X\rangle`$: fixed by $`C_{\rm bod}`$, well defined, independent of $`\eta`$. They are the coefficients read from $`C_{\rm bod}`$. The listed numbers $`\gamma\theta_i`$ and $`\kappa\langle\chi\vert X\vert\chi\rangle`$ can change under a relisting such as $`X\to X-c`$, $`C^{\rm D}_i\to C^{\rm D}_i+\kappa c\,\hat x_i`$. Used: the label $`0`$ of the two types (A2) and the finite range of $`W`$.
   - The operator that multiplies the centre label, $`\mathcal K`$ (on all levels $`g_1G_1+g_2G_2+2\kappa\langle X\rangle`$): fixed by $`C_{\rm bod}`$, independent of $`\eta`$.
   - The operator that multiplies $`\hat r`$: fixed by $`C_{\rm bod}`$ once $`\eta`$ is given. It depends on the convention, $`\mathcal D_\eta=\mathcal D_0-\eta\,\mathcal K`$, and is independent of $`\eta`$ iff $`\mathcal K=0`$, i.e. (as $`M_i>0`$) iff all three gradients vanish.

### Step 3. First-order velocities from a bound level (item 2a)

Class: every $`W\in\mathcal W`$, all data, every bound level, every $`g\in\mathcal G(\mathcal P_0)`$, all gradients. On the levels $`k_1,k_2`$ write $`H_0:=C_{\rm pair}`$ and $`\Phi_g(\lambda):=e^{-iH_0\lambda}\Phi_g`$.

1. $`\Delta`$ is diagonal in the positions, so $`i[C_{\rm bod},\hat x_i]=V_i`$ and $`\mathrm d\bar m_i/\mathrm d\lambda=\langle V_i\rangle`$ in the evolved state, exactly. The first-order velocity $`v^{(1)}_i`$ is the part of this expectation that is linear in the gradients. By F1,

```math
v^{(1)}_i(\lambda)=2\,\mathrm{Re}\,\bigl\langle\Phi_g(\lambda)\big\vert V_i\big\vert\Phi^{(1)}(\lambda)\bigr\rangle,\qquad
\Phi^{(1)}(\lambda):=-i\int_0^\lambda\mathrm ds\;e^{-iH_0(\lambda-s)}\,\Delta\,\Phi_g(s),
\qquad\text{(13.4)}
```

and the same formula with $`V_i\to\hat r`$ gives the first-order change of $`\bar m_1-\bar m_2`$. On a finite chain all operators are bounded; the long-chain limit is F4, with (13.5).
2. In the fibres $`\Phi_g(s)`$ is $`g\,e^{-iE_bs}\psi_P`$, and $`\hat X_\eta`$ acts as $`i\partial_P`$ ($`g`$ has compact support in $`\mathcal P_0`$), so

```math
\Delta\,\Phi_g(s)\ \longleftrightarrow\ e^{-iE_b(P)s}\bigl[s\,E_b'\,g\,\mathcal K\psi_P+\xi_P\bigr],\qquad
\xi_P:=i\,g'\,\mathcal K\psi_P+i\,g\,\mathcal K\psi_P'+g\,\hat r\,\mathcal D_\eta\psi_P ,
\qquad\text{(13.5)}
```

a vector of $`\mathfrak h`$ with $`\int\mathrm dP\,\lVert\xi_P\rVert^2<\infty`$ (F2, F3, $`g\in C^1`$ with compact support).
3. Split (13.5) along $`\psi_P`$ and in $`Q_P\mathfrak h`$. On $`\psi_P`$ the propagator is $`e^{-iE_b(\lambda-s)}`$. On $`Q_P\mathfrak h`$, $`\int_0^\lambda\mathrm ds\,e^{-i(H-E_b)(\lambda-s)}=-iR_P\,\mathcal U_P(\lambda)`$ and $`\int_0^\lambda\mathrm ds\,s\,e^{-i(H-E_b)(\lambda-s)}=-i\lambda R_P+R_P^2\,\mathcal U_P(\lambda)`$.
4. Part along $`\psi_P`$. $`\langle V_i\rangle_P=E_b'`$ by (11.7), and $`\langle\mathcal K\rangle_P`$, $`\langle\hat r\mathcal D_\eta\rangle_P`$ are real. The terms with $`\lambda^2`$ and with $`\mathcal D_\eta`$ are imaginary and drop out. With $`2\,\mathrm{Re}\langle\psi_P\vert\mathcal K\vert\psi_P'\rangle=\partial_P\langle\mathcal K\rangle_P`$ the rest is $`\lambda\int\mathrm dP\,E_b'\,\partial_P\bigl(\lvert g\rvert^2\langle\mathcal K\rangle_P\bigr)=-\lambda\,\langle E_b''\langle\mathcal K\rangle\rangle_g`$ (partial integration).
5. Part in $`Q_P\mathfrak h`$. The term $`-i\lambda R_P`$ gives $`-\lambda\int\mathrm dP\,\lvert g\rvert^2E_b'\,2\,\mathrm{Re}\langle V_i\psi_P\vert R_P\vert\mathcal K\psi_P\rangle`$. Since $`V_1-V_2=i[H(P),\hat r]`$ and $`(H-E_b)\psi_P=0`$,

```math
\begin{aligned}
R_PV_1\psi_P&=R_PV_\eta\psi_P+i(1-\eta)\,Q_P\hat r\psi_P,\qquad R_PV_2\psi_P=R_PV_\eta\psi_P-i\eta\,Q_P\hat r\psi_P,\\
2\,\mathrm{Re}\,\langle V_i\psi_P\vert R_P\vert\mathcal K\psi_P\rangle&=-\partial_P\langle\mathcal K\rangle_P\qquad(i=1,2).
\end{aligned}
\qquad\text{(13.6)}
```

The second line holds because $`\partial_P\langle\mathcal K\rangle_P=-2\,\mathrm{Re}\langle\mathcal K\psi_P\vert R_P\vert V_\eta\psi_P\rangle`$ (F2) and $`\langle Q_P\hat r\psi_P\vert\mathcal K\psi_P\rangle=\langle\hat r\mathcal K\rangle_P-\langle\hat r\rangle_P\langle\mathcal K\rangle_P`$ is real ($`[\hat r,\mathcal K]=0`$).
6. Result, for $`i=1,2`$ and every $`\lambda`$:

```math
\boxed{\;v^{(1)}_i(\lambda)=\lambda\,\langle\alpha\rangle_g+\rho_i(\lambda)\;},\qquad \alpha(P):=-E_b''(P)\,\langle\mathcal K\rangle_P+E_b'(P)\,\partial_P\langle\mathcal K\rangle_P ,
\qquad\text{(13.7)}
```

```math
\alpha=g_1\alpha_1+g_2\alpha_2+\kappa\langle X\rangle\,\alpha_X,\qquad
\alpha_i(P)=-M_i\bigl[E_b''\,\langle\sigma^{(i)}_3\rangle_P-E_b'\,\partial_P\langle\sigma^{(i)}_3\rangle_P\bigr],\qquad \alpha_X(P)=-2E_b''(P),
\qquad\text{(13.8)}
```

```math
\begin{aligned}
\rho_i(\lambda)&=-2\,\mathrm{Re}\int\mathrm dP\,\Bigl[i\lvert g\rvert^2E_b'\,\langle V_i\psi_P\vert R_P^2\,\mathcal U_P(\lambda)\vert\mathcal K\psi_P\rangle+g^{*}\langle V_i\psi_P\vert R_P\,\mathcal U_P(\lambda)\vert\xi_P\rangle\Bigr],\\
\lvert\rho_i(\lambda)\rvert&\le\tau_i\,\mathsf B_g,\qquad \mathsf B_g:=\frac4{\Gamma_g}\Bigl[\mathsf b\Bigl(\frac{\tau_{\min}}{\Gamma_g}+\lVert g'\rVert_2+\max_{I_g}\lVert\psi_P'\rVert\Bigr)+\mathsf d_\eta\max_{I_g}\lVert\hat r\psi_P\rVert\Bigr].
\end{aligned}
\qquad\text{(13.9)}
```

The bound uses $`\lVert V_i\rVert\le\tau_i`$, $`\lvert E_b'\rvert\le\tau_{\min}`$, $`\lVert\mathcal U_P\rVert\le2`$, $`\lVert\mathcal K\rVert\le\mathsf b`$, $`\lVert\mathcal D_\eta\rVert\le\mathsf d_\eta`$ and $`\int\lvert g\rvert\lvert g'\rvert\le\lVert g'\rVert_2`$.
7. Status. Both parts have the same coefficient $`\langle\alpha\rangle_g`$ of the growing part. The rests differ in general, and $`\rho_i(0)=0`$. The rest is bounded for all $`\lambda`$, in particular for all $`\lambda\ge0`$, under the conditions of the class alone: the level is isolated on the compact $`I_g\subset\mathcal P_0`$ ($`\Gamma_g>0`$) and $`g\in\mathcal G(\mathcal P_0)`$ ($`\lVert g'\rVert_2<\infty`$). $`\rho_i`$ does not depend on $`\eta`$ or on the phase of $`\psi_P`$; the single terms of the bound do. By (11.5) and F2, $`\langle\sigma^{(i)}_3\rangle_P=\partial E_b/\partial M_i`$ and $`\partial_P\langle\sigma^{(i)}_3\rangle_P=\partial E_b'/\partial M_i`$. Numerical check: section "Code".

### Step 4. Mean label separation (item 2b)

1. The computation of Step 3 with $`V_i\to\hat r`$ ($`\langle\hat r\rangle_P`$ is real; (13.6) is not used) gives, for every member of the class of item 2,

```math
\begin{aligned}
(\bar m_1-\bar m_2)^{(1)}(\lambda)&=\lambda\,\langle\beta\rangle_g+\sigma(\lambda),\qquad \lvert\sigma(\lambda)\rvert\le\max_{I_g}\lVert\hat r\psi_P\rVert\;\mathsf B_g,\\
\beta(P)&:=-\langle\mathcal K\rangle_P\,\partial_P\langle\hat r\rangle_P-2E_b'(P)\,\mathrm{Re}\,\langle\hat r\psi_P\vert R_P\vert\mathcal K\psi_P\rangle ,
\end{aligned}
\qquad\text{(13.10)}
```

where $`\sigma`$ is the first line of (13.9) with $`V_i\psi_P\to\hat r\psi_P`$. There is no term $`\propto\lambda^2`$: the first-order relative velocity $`\rho_1-\rho_2=\langle\beta\rangle_g+\dot\sigma`$ has no growing part. This holds alike for the common gradient and for $`g_1\neq g_2`$.
2. Bounded case (sufficient condition). Let $`W(-r)^{*}=W(r)`$ for all $`r`$ (complex conjugate of the matrix in the branch basis); every diagonal on-site binding has this property. The antiunitary $`(\Theta\psi)(r):=\psi(-r)^{*}`$ then commutes with $`H(P)`$ for every $`P`$ and $`\eta`$ ($`\Theta S\Theta^{-1}=S^\dagger`$ in (11.1)) and with $`\mathcal K`$, and $`\Theta\hat r\Theta^{-1}=-\hat r`$. For a simple level $`\Theta\psi_P=e^{i\phi}\psi_P`$, hence $`\langle\hat r\rangle_P=0`$ for all $`P`$ and $`\langle\hat r\psi_P\vert R_P\vert\mathcal K\psi_P\rangle\in i\mathbb R`$. So $`\beta\equiv0`$, and the first-order change of the separation is $`\sigma(\lambda)`$: bounded for all $`\lambda\ge0`$, for all values of the gradients.
3. Vanishing case (sufficient condition). Let $`\tau_1=\tau_2`$, $`M_1=M_2`$, $`W(-r)=\mathsf S\,W(r)\,\mathsf S`$ with $`\mathsf S`$ the exchange of the two branch labels, and $`g_1=g_2`$ (any $`\kappa\langle X\rangle`$). The exchange $`\Sigma`$ of the labels of the two bodies then commutes with $`C_{\rm bod}`$ and with the joint shift, $`\Sigma\Phi_g=\pm\Phi_g`$ (simple level) and $`\Sigma\hat r\Sigma=-\hat r`$. Hence $`\bar m_1-\bar m_2=0`$ for all $`\lambda`$, to all orders in the gradients.
4. Otherwise. For a binding without the property of 2, $`\beta\not\equiv0`$ in general, and the first-order separation grows linearly in $`\lambda`$: the internal structure of the level follows the first-order change $`-\lambda\langle\mathcal K\rangle_P`$ of the total label. This rests on a numerical control (`code/v2/pair_fall_check.py`, set S5), not on an analytic example. With the property of 2 and without the conditions of 3 the change is bounded and does not vanish in general (same file, sets S1–S4: it relaxes to a non-zero value).

### Step 5. Drift acceleration (items 2c, 2d)

1. The first-order acceleration is $`a^{(1)}_i=\mathrm dv^{(1)}_i/\mathrm d\lambda=\langle\alpha\rangle_g+\dot\rho_i(\lambda)`$; $`\dot\rho_i`$ is bounded, but neither small nor decaying in general. Its window average is a difference quotient of the velocity, exactly: $`\overline{a^{(1)}_i}=\langle\alpha\rangle_g+[\rho_i(\lambda_1+\Lambda)-\rho_i(\lambda_1)]/\Lambda`$, so $`\lvert\overline{a^{(1)}_i}-\langle\alpha\rangle_g\rvert\le2\tau_i\mathsf B_g/\Lambda`$ for all $`\lambda_1\ge0`$, $`\Lambda>0`$.
2. Sharp total label. Class of sequences $`\mathcal S(P_0,I)`$: packets of $`\mathcal G(\mathcal P_0)`$ with supports in one compact interval $`I\subset\mathcal P_0`$, mean $`P_0`$ and $`\delta P\to0`$. Taylor's formula with $`\int(P-P_0)\lvert g\rvert^2=0`$ gives $`\lvert\langle\alpha\rangle_g-\alpha(P_0)\rvert\le\frac12\max_I\lvert\alpha''\rvert\,\delta P^2`$. Hence, with the window first and the sharp label second, for both parts:

```math
\boxed{\;a^{\rm drift}(P_0):=\lim_{\delta P\to0}\,\lim_{\Lambda\to\infty}\overline{a^{(1)}_i}=g_1\,\alpha_1(P_0)+g_2\,\alpha_2(P_0)+\kappa\langle X\rangle\,\alpha_X(P_0)\;},\qquad \alpha_i=-M_i\Bigl[E_b''\,\frac{\partial E_b}{\partial M_i}-E_b'\,\frac{\partial E_b'}{\partial M_i}\Bigr],\quad\alpha_X=-2E_b'' .
\qquad\text{(13.11)}
```

Here $`E_b'=\langle V_i\rangle_P`$ (11.7), $`\partial E_b/\partial M_i=\langle\sigma^{(i)}_3\rangle_P`$ (11.5), and $`E_b''=-\eta^2\langle A_1\rangle_P-(1-\eta)^2\langle A_2\rangle_P-2\mathcal S_\eta(P)`$ (11.9).
3. The other order. At a fixed window the limit $`\delta P\to0`$ does not exist on $`\mathcal S(P_0,I)`$ in general. The joint shift by $`n`$ labels, $`g\to g\,e^{-inP}`$, maps the class to itself with the same $`\lvert g\rvert^2`$. In (13.9) only the term with $`g'`$ changes: $`\rho_i\to\rho_i-2n\,\mathrm{Re}\langle F_{i,\lambda}\rangle_g`$ with $`F_{i,\lambda}(P):=\langle V_i\psi_P\vert R_P\,\mathcal U_P(\lambda)\vert\mathcal K\psi_P\rangle`$. The window averages of a sequence and of its shifted copy therefore differ by $`-\frac{2n}{\Lambda}\mathrm{Re}\langle F_{i,\lambda_1+\Lambda}-F_{i,\lambda_1}\rangle_g`$, which tends to $`-2n\,\mathsf f_i/\Lambda`$ with $`\mathsf f_i:=\mathrm{Re}\bigl[F_{i,\lambda_1+\Lambda}(P_0)-F_{i,\lambda_1}(P_0)\bigr]`$. For $`\mathsf f_i\neq0`$ two sequences that differ by a fixed shift have different limits, and a sequence shifted by $`n\to\infty`$ has none. On a subclass on which the limit exists it defines the window average of the first-order acceleration of a start with a sharp total label. That quantity depends on the window, on the part and on the place of the packet, so it is not a property of the level; whether it tends to $`\alpha(P_0)`$ for $`\Lambda\to\infty`$ is not derived.
   - Answer to item 2(c) as amended. On $`\mathcal S(P_0,I)`$ the two limits do not commute in general. With the window first, both limits exist for every sequence of the class and give (13.11) (items 1 and 2). With the sharp total label first, the limit at a fixed window fails to exist for some sequences of the class, under the condition of the next bullet.
   - What is shown for the other order. For a window with $`\mathsf f_i\neq0`$ the limit $`\delta P\to0`$ does not exist on the class; on a subclass on which it exists, its value depends on the place of the packet (the shift $`n`$). A sufficient condition for windows $`[0,\Lambda]`$ with $`\mathsf f_i\neq0`$ and arbitrarily large $`\Lambda`$ is $`\partial_P\langle\mathcal K\rangle_{P_0}\neq0`$: for $`\lambda_1=0`$, $`\mathsf f_i=\mathrm{Re}\,F_{i,\Lambda}(P_0)`$; the mean of $`e^{-i(H(P_0)-E_b(P_0))\Lambda}`$ over $`\Lambda\in[0,T]`$ tends to zero on $`Q_{P_0}\mathfrak h`$ for $`T\to\infty`$ (mean ergodic theorem, simple level), so the mean of $`\mathsf f_i`$ tends to $`\mathrm{Re}\langle V_i\psi_{P_0}\vert R_{P_0}\vert\mathcal K\psi_{P_0}\rangle=-\tfrac12\partial_P\langle\mathcal K\rangle_{P_0}`$ by (13.6).
   - Exceptional members, for which nothing is shown: windows with $`\mathsf f_i=0`$. This is every window if $`g_1=g_2=0`$ (then $`R_P\mathcal K\psi_P=0`$), and every window at $`P_0=0`$ if $`\mathcal R`$ of Step 6.1 commutes with $`H(0)`$: then $`\mathcal R\psi_0=\pm\psi_0`$, $`\mathcal RV_i(0)\mathcal R^{-1}=-V_i(0)`$ and $`[\mathcal R,\mathcal K]=0`$ give $`F_{i,\lambda}(0)=0`$. The second case contains every diagonal on-site binding, hence the levels of items 3 and 4.
   - The evaluation of the other order is not asked (item 2(c) of the question) and is not given.
4. What multiplies the gradients. $`E_b''(P_0)`$ multiplies all three, but it is the whole coefficient only for $`\kappa\langle X\rangle`$: $`\alpha_X=-2E_b''`$, exactly, on the whole class. For $`g_i`$ it is weighted by $`M_i\,\partial E_b/\partial M_i=M_i\langle\sigma^{(i)}_3\rangle_{P_0}`$, and for $`E_b'(P_0)\neq0`$ the term $`M_iE_b'\,\partial E_b'/\partial M_i`$ enters in addition. Exceptional members:
   - $`E_b''(P_0)=0`$: $`\alpha_X=0`$, $`\alpha_i=M_iE_b'\,\partial E_b'/\partial M_i`$; at $`P_0=0`$ the inertia $`\mathfrak m_b`$ is not defined.
   - $`E_b'(P_0)=0`$: $`\alpha_i=-M_iE_b''\langle\sigma^{(i)}_3\rangle_{P_0}`$; at $`P_0=0`$ then $`a^{\rm drift}(0)=-\langle\mathcal K\rangle_0/\mathfrak m_b`$. The class does not imply $`E_b'(0)=0`$; a sufficient condition is $`W(-r)=\sigma^{(1)}_3\sigma^{(2)}_3W(r)\sigma^{(1)}_3\sigma^{(2)}_3`$ together with a level that the map $`P\to-P`$ takes to itself.
   - $`\langle\sigma^{(i)}_3\rangle_{P_0}=0`$: the first term of $`\alpha_i`$ vanishes.
5. Common gradient (item 2d). With (11.6),

```math
\alpha_1+\alpha_2=-E_b''\,\mathcal M_P+E_b'\,\mathcal M_P',\qquad
\mathcal M_P:=M_1\langle\sigma^{(1)}_3\rangle_P+M_2\langle\sigma^{(2)}_3\rangle_P=E_b(P)-\langle A_1\rangle_P-\langle A_2\rangle_P-\langle U\rangle_P .
\qquad\text{(13.12)}
```

The coefficient of $`g_{\rm c}`$ is built from the two rest terms of the scaling relation only. The motion terms $`\langle A_i\rangle_P`$ and the binding term $`\langle U\rangle_P`$, which the field does not multiply, do not enter; $`\mathcal M_P=E_b(P)`$ iff $`\langle A_1\rangle_P+\langle A_2\rangle_P+\langle U\rangle_P=0`$.

### Step 6. Diagonal on-site binding in the regime $`\mathsf R`$ (item 3)

Class: every diagonal on-site binding with $`\hat w_{11}\neq0`$, the level (11.12), fixed hatted data, $`P_0=0`$.

1. At rest. $`(\mathcal R\psi)(r):=\sigma^{(1)}_3\sigma^{(2)}_3\psi(-r)`$ gives $`\mathcal RH(P)\mathcal R^{-1}=H(-P)`$ for a diagonal on-site binding, and by (11.12) the level near $`\mathcal B_{++}`$ is the only one for small $`\epsilon`$. So $`E_b(-P)=E_b(P)`$ and $`E_b'(0)=0`$, exactly. By (11.8), without gradients $`\mathrm d\bar m_i/\mathrm d\lambda=\langle E_b'\rangle_g=O(\delta P^2)`$ for all $`\lambda`$ (zero for even $`\lvert g\rvert^2`$): the pair is at rest in the sharp-total-label limit.
2. Closed form. (13.11) at $`P_0=0`$ is $`a_{\rm pair}:=a^{\rm drift}(0)=-E_b''(0)\bigl[g_1M_1\langle\sigma^{(1)}_3\rangle_0+g_2M_2\langle\sigma^{(2)}_3\rangle_0+2\kappa\langle X\rangle\bigr]`$, exactly. With (11.14) and (11.16):

```math
\boxed{\;a_{\rm pair}=\frac{\varsigma}{\sqrt{1+u^2}}\;\frac{g_1M_1(1+r_1)+g_2M_2(1+r_2)+2\kappa\langle X\rangle(1+r_X)}{\mathfrak m_1+\mathfrak m_2}\;},\qquad r_1,r_2,r_X=O(\epsilon^2)\ \text{at fixed }u .
\qquad\text{(13.13)}
```

Equivalently $`a_{\rm pair}=-(g_1M_1+g_2M_2+2\kappa\langle X\rangle)/\mathfrak m_b`$. Since $`\mathfrak m_ia^{(i)}=-(g_iM_i+\kappa\langle X\rangle)`$, at leading order $`a_{\rm pair}=-\varsigma(1+u^2)^{-1/2}\,\bar a`$ with the inertia-weighted mean $`\bar a:=(\mathfrak m_1a^{(1)}+\mathfrak m_2a^{(2)})/(\mathfrak m_1+\mathfrak m_2)`$ of the free falls. Each coefficient is of order $`\epsilon^2`$; the remainders are not uniform in $`u`$.
3. Ordered limits of the leading coefficient (first $`\epsilon\to0`$ at fixed $`u`$, then $`u`$):

```math
u\to0:\ \ a_{\rm pair}\to-\varsigma\,\bar a\,\bigl[1-\tfrac12u^2+O(u^4)\bigr];\qquad
u\to\infty:\ \ a_{\rm pair}\to-\varsigma\,\frac{\bar a}{u}\,\bigl[1+O(u^{-2})\bigr]\to0 .
\qquad\text{(13.14)}
```

For $`w_{11}<0`$ the wide pair falls with $`\bar a`$: the sum of the weights $`g_iM_i+\kappa\langle X\rangle`$ over the sum of the inertias. For $`w_{11}>0`$ the level lies above the band, $`\mathfrak m_b<0`$, and the pair accelerates opposite to $`\bar a`$ at every $`u`$; by (4.7) its wide form $`-\bar a`$ is, at leading order, the same mean of the drift accelerations of the free parts at $`p=\pi/2`$ instead of at rest. A tight pair does not fall at this order: its inertia grows like $`u`$, its weight does not.
4. Ratios for $`\langle X\rangle=0`$ (item 3b), where $`a^{(i)}=-\tau_i^2g_i`$ and $`g_i\neq0`$:

```math
\frac{a_{\rm pair}}{a^{(i)}}=-\frac{\varsigma}{\sqrt{1+u^2}}\cdot\frac{g_1M_1+g_2M_2}{g_i\,\tau_i^2\,(\mathfrak m_1+\mathfrak m_2)}\,\bigl(1+O(\epsilon^2)\bigr),\qquad
\tau_{\rm p}^2:=\frac{M_1+M_2}{M_1/\tau_1^2+M_2/\tau_2^2}.
\qquad\text{(13.15)}
```

   - Common gradient, $`\tau_1=\tau_2`$ (the free parts fall alike): both ratios are $`-\varsigma/\sqrt{1+u^2}`$. For $`w_{11}<0`$ this is $`<1`$ at every fixed $`u`$. The pair falls like its parts neither exactly nor to any order in $`\epsilon`$ (the difference is of order $`\epsilon^0`$), but only in the ordered wide-pair limit, with the leading difference $`-\tfrac12u^2`$. For $`w_{11}>0`$: not at all (ratio $`\to-1`$).
   - Common gradient, $`\tau_1\neq\tau_2`$ (the free parts differ, $`a^{(1)}/a^{(2)}=\tau_1^2/\tau_2^2`$): the ratios are $`-\varsigma(1+u^2)^{-1/2}\tau_{\rm p}^2/\tau_i^2`$, with $`\tau_{\rm p}^2`$ strictly between $`\tau_1^2`$ and $`\tau_2^2`$. The pair falls like its parts at no $`u`$ and in no limit. In the wide limit ($`w_{11}<0`$) the ratio differs from $`1`$ by $`M_j(\tau_j^2-\tau_i^2)/(M_i\tau_j^2+M_j\tau_i^2)`$, $`j\neq i`$. Exceptional: for the part with the smaller $`\tau_i`$ and $`w_{11}<0`$ the ratio is $`1`$ at the single value $`u_*=(\tau_{\rm p}^4/\tau_i^4-1)^{1/2}`$.
   - $`g_1\neq g_2`$: $`a_{\rm pair}=-\varsigma(1+u^2)^{-1/2}\bar a`$. If $`\tau_1^2g_1=\tau_2^2g_2`$ the free parts fall alike and the first case applies. Otherwise not at all: in the wide limit ($`w_{11}<0`$) $`a_{\rm pair}-a^{(1)}\to\mathfrak m_2(a^{(2)}-a^{(1)})/(\mathfrak m_1+\mathfrak m_2)`$. Exceptional: $`g_1M_1+g_2M_2=0`$ (no fall at this order).
5. Clock levels (item 3c). With $`u=4\lvert w\rvert\mathfrak m_1\mathfrak m_2/(\mathfrak m_1+\mathfrak m_2)`$, (13.13) reads

```math
a_{\rm pair}=\varsigma\,\frac{g_1M_1+g_2M_2+2\kappa\langle X\rangle}{\sqrt{(\mathfrak m_1+\mathfrak m_2)^2+16\,w^2\,\mathfrak m_1^2\mathfrak m_2^2}}\,\bigl(1+O(\epsilon^2)\bigr),\qquad \mathfrak m_i=\frac{M^{(i)}_{k_i}}{\tau_i^2}.
\qquad\text{(13.16)}
```

   - Claim: the leading coefficient is the same for all $`N_1N_2`$ pairs of levels iff $`g_1=g_2=0`$ and $`\kappa\langle X\rangle=0`$. Proof: call the numerator $`\mathsf N`$ and the root $`h`$. If $`\mathsf N=\varsigma c\,h`$ on four pairs $`\{M_1,M_1'\}\times\{M_2,M_2'\}`$ ($`N_i\ge2`$), take the mixed second difference. It is $`0`$ for $`\mathsf N`$ and strictly positive for $`h`$, because $`4h^3\,\partial_{\mathfrak m_1}\partial_{\mathfrak m_2}h=4q\bigl[(\mathfrak m_1+\mathfrak m_2)^2+(1+q)\mathfrak m_1\mathfrak m_2\bigr]>0`$ with $`q:=16w^2\mathfrak m_1\mathfrak m_2`$. So $`c=0`$, $`\mathsf N=0`$ on the four pairs, and all three gradients vanish.
   - Hence: for $`\langle X\rangle=0`$ iff $`g_1=g_2=0`$ (no fall); for $`\langle X\rangle\neq0`$ never.
   - Leading dependence: $`\partial\ln a_{\rm pair}/\partial\ln M_i=g_iM_i/\mathsf N-\mathfrak m_i/(\mathfrak m_1+\mathfrak m_2)-\frac{u^2}{1+u^2}\frac{a_i}{a}`$. For the common gradient with $`\tau_1=\tau_2=\tau`$ and $`\langle X\rangle=0`$ only the last term remains: $`a_{\rm pair}=\varsigma g_{\rm c}\tau^2/\sqrt{1+u^2}`$ with $`u=\frac{4\lvert w\rvert}{\tau^2}\frac{M_1M_2}{M_1+M_2}`$.
   - In the ordered wide-pair limit the leading coefficient $`\varsigma\mathsf N/(\mathfrak m_1+\mathfrak m_2)`$ is the same for all levels iff $`\langle X\rangle=0`$ and $`\tau_1^2g_1=\tau_2^2g_2`$ (two affine functions of $`M_1,M_2`$ that agree on the four pairs).
   - Comparison: a free part falls alike on all levels iff $`\langle X\rangle=0`$ (4.16). The pair does not, at any fixed $`u`$, because the binding $`w`$ does not scale with the levels while $`a`$ does.
6. $`\langle X\rangle\neq0`$ (item 3d). It adds $`-2\kappa\langle X\rangle E_b''(P_0)`$ to the drift acceleration, exactly and on the whole class of item 2 (13.8). At $`P_0=0`$ this is $`-2\kappa\langle X\rangle/\mathfrak m_b`$, in $`\mathsf R`$ equal to $`\frac{\varsigma}{\sqrt{1+u^2}}\frac{2\kappa\langle X\rangle}{\mathfrak m_1+\mathfrak m_2}`$. For a free part it adds $`-\kappa\langle X\rangle/\mathfrak m_i`$ (4.16). In both cases the plain gradient enters as the sum of the plain gradients over the curvature inertia, without a factor $`\langle\sigma_3\rangle`$, and it makes the fall depend on the levels. For the pair it is in addition reduced by $`(1+u^2)^{-1/2}`$ against the inertia-weighted mean, and reversed for $`w_{11}>0`$.

### Step 7. Fall and the clocks of the parts (item 4)

Class as in Step 6, with $`\langle X\rangle=0`$.

1. Rate (item 4a). At the label $`x_0`$ put $`n_i:=1+g_ix_0>0`$. The operator $`(1+g_ix_0)G_i`$ is the rest and clock operator of Model D with $`m_i\to n_im_i`$ and $`\lambda_{0,i}\to\lambda_{0,i}/n_i`$, hence $`M^{(i)}_k\to n_iM^{(i)}_k`$ and $`\bar M_i\to n_i\bar M_i`$. The zeroth order in the gradients is the pair without gradients and with these data. It is invariant under the joint shift, so (11.19) applies to a packet placed at $`x_0`$: the reading of the clock label of the part $`i`$ is $`P_{N_i}(a;\vartheta_i)+\mathcal R_i`$ with the advance $`\vartheta_i=\Gamma_i(x_0)\,n_i\lambda/\lambda_{0,i}`$. The rate is $`\mathrm d\vartheta_i/\mathrm d\lambda`$. With (11.20):

```math
\begin{aligned}
r_i(x_0)&=\frac{1+g_ix_0}{\lambda_{0,i}}\;\Gamma_i(x_0),\qquad \Gamma_i(x_0)=1-\frac{\tau_i^2}{4\,n_i^2\bar M_i^2}\,\Lambda(x_0)+O(\epsilon^4),\\
\Lambda(x_0)&=1+\frac{\varsigma}{\sqrt{1+u(x_0)^2}},\qquad u(x_0)=\frac{\lvert w\rvert}{a_1/n_1+a_2/n_2}
\end{aligned}
\qquad\text{(13.17)}
```

($`a_i`$ with $`\bar M_i`$ for the part that is read and $`M_j`$ for the other part).
   - Conditions, from (11.19): the clock of the part $`i`$ starts in $`\lvert0\rangle`$; the other part is on its level; the positions and branches are in a packet of the bound level of the data at $`x_0`$ with mean total label $`0`$ and spread $`\delta P`$; leading order in $`\kappa`$.
   - Range of $`\lambda`$: $`\mathcal R_i`$ is small for $`\lambda\ll\lambda_{0,i}/\delta_i`$ (in $`\mathsf R`$ with $`\delta_i\to D_i/M_i`$) and $`\delta P^2(1+\lambda/\lambda_{0,i})\ll1`$.
   - As a statement on the pair in the field, (13.17) is the zeroth order in $`(\lvert g_1\rvert+\lvert g_2\rvert)\,s`$, where $`s\gtrsim1/(2\delta P)`$ is the width of the packet in labels. The first-order corrections to the reading are not derived here.
2. Relative change per label, to first order in the gradients ($`\varrho_i=\partial_{x_0}\ln r_i`$ at $`x_0=0`$):

```math
\varrho_i=g_i+\frac{\tau_i^2}{4\bar M_i^2}\Bigl[2\Lambda\,g_i+\frac{\varsigma\,u^2}{(1+u^2)^{3/2}}\,\frac{g_1a_1+g_2a_2}{a}\Bigr]+O(\epsilon^4)\,(\lvert g_1\rvert+\lvert g_2\rvert) .
\qquad\text{(13.18)}
```

At leading order $`\varrho_i=g_i`$, as for the free part. The term of order $`\epsilon^2`$ contains the gradient of the other part. Both are derived as follows.
   - Derivative used. $`\Gamma_i=\partial E_b(0)/\partial M_i`$, exactly, by (11.19) with (11.5), and at the label $`x_0`$ the data are $`n_1M_1`$, $`n_2M_2`$ with $`\tau_1`$, $`\tau_2`$ and $`W`$ unchanged (item 1). The rate is $`r_i=n_i\Gamma_i/\lambda_{0,i}`$, so its change with $`x_0`$ is the derivative of a known function of the data, not of an estimate. To first order in the gradients, without the expansion in $`\mathsf R`$ (with $`M_i=\bar M_i`$ for the part that is read, as in (13.17)):

```math
\varrho_i=g_i+\frac1{\Gamma_i}\sum_{j=1,2}g_j\,M_j\,\frac{\partial^2E_b(0)}{\partial M_j\,\partial M_i} .
\qquad\text{(13.21)}
```

   This uses the second derivatives of the level at $`P=0`$ in the rest costs $`M_1`$, $`M_2`$: one derivative in the data more than (11.14) and (11.20). A derivative of the remainder of (11.20) is thereby reduced to (11.12): that remainder is $`\partial/\partial M_i`$ of the remainder of (11.12).
   - Regime $`\mathsf R`$. (11.12) at $`P=0`$ is $`E_b(0)=M_1+M_2+\mathsf e(a)+\mathcal E`$ with $`\mathsf e(a):=a+\varsigma\sqrt{w^2+a^2}`$ and the remainder $`\mathcal E=O(\epsilon^4)`$. With $`\partial a/\partial M_j=-a_j/M_j`$, $`\mathsf e'=\Lambda`$ and $`\mathsf e''=\varsigma u^2/\bigl(a(1+u^2)^{3/2}\bigr)`$, for $`i,j=1,2`$:

```math
\frac{\partial^2E_b(0)}{\partial M_j\,\partial M_i}=\delta_{ij}\,\frac{2a_i}{M_i^2}\,\Lambda+\frac{a_i\,a_j}{M_iM_j}\cdot\frac{\varsigma\,u^2}{a\,(1+u^2)^{3/2}}+\frac{\partial^2\mathcal E}{\partial M_j\,\partial M_i},\qquad \frac{\partial^2\mathcal E}{\partial M_j\,\partial M_i}=O(\epsilon^4)\ \text{at fixed }u .
\qquad\text{(13.22)}
```

   The two explicit terms are of order $`\epsilon^2`$.
   - Remainder of (13.22). The statement of Step 8 of 11-bound-pair, quoted with (11.14): "$`E_b`$ is analytic in the data with a remainder bounded uniformly near real data, so (11.12) can be differentiated and the remainders stay $`O(\epsilon^4)`$." It is read here as: $`\mathcal E`$ is analytic in the data and $`\lvert\mathcal E\rvert\le c\,\epsilon^4`$ on a complex neighbourhood of the real data whose size does not depend on $`\epsilon`$. $`M_1`$ and $`M_2`$ are data that are fixed in $`\mathsf R`$, so Cauchy's estimate on a polydisc of radius $`\delta`$ in $`(M_1,M_2)`$ inside that neighbourhood gives $`\lvert\partial_{M_j}\partial_{M_i}\mathcal E\rvert\le2c\,\epsilon^4/\delta^2`$. In 11-bound-pair the statement serves the first derivatives in the data that give (11.14); for the second derivatives used here it is its premise that carries the estimate.
   - Result. Insert (13.22) in (13.21), with $`1/\Gamma_i=1+O(\epsilon^2)`$ by (11.20) and $`a_i/M_i=\tau_i^2/(4\bar M_i^2)`$ for the part that is read: this is (13.18). Its leading order, $`\varrho_i=g_i+O(\epsilon^2)(\lvert g_1\rvert+\lvert g_2\rvert)`$, uses only that the second derivatives (13.22) are of order $`\epsilon^2`$; its term of order $`\epsilon^2`$ uses their values, with the remainder $`O(\epsilon^4)`$. No assumption on a remainder is made. Numerical check of (13.22) and of the term of order $`\epsilon^2`$: section "Code".
3. The number $`\mathsf w_i^2`$ (item 4b), for $`g_i\neq0`$ (then $`\varrho_i\neq0`$ for small $`\epsilon`$):

```math
\mathsf w_i^2:=-\frac{a_{\rm pair}}{\varrho_i}=-\frac{\varsigma}{\sqrt{1+u^2}}\cdot\frac{g_1M_1+g_2M_2}{g_i\,(\mathfrak m_1+\mathfrak m_2)}\,\bigl(1+O(\epsilon^2)\bigr)\qquad\Bigl[\,=-\frac{\varsigma\,\tau_{\rm p}^2}{\sqrt{1+u^2}}\,\bigl(1+O(\epsilon^2)\bigr)\ \text{for } g_1=g_2\Bigr].
\qquad\text{(13.19)}
```

   - Equal to $`\tau_i^2`$: no. For the common gradient $`\mathsf w_i^2/\tau_i^2=-\varsigma(1+u^2)^{-1/2}\tau_{\rm p}^2/\tau_i^2`$, which is $`\neq1`$ except at $`u_*`$ of Step 6 for one part; for $`w_{11}>0`$ it is negative. For $`g_1\neq g_2`$ equality holds only for one special value of $`g_1/g_2`$ at given $`u`$.
   - The same for $`i=1,2`$: $`\mathsf w_1^2/\mathsf w_2^2=\varrho_2/\varrho_1`$ (exact), which is $`g_2/g_1`$ at leading order. So: the same at leading order iff $`g_1=g_2`$; and then, by (13.18), not at relative order $`\epsilon^2`$ unless $`\tau_1/\bar M_1=\tau_2/\bar M_2`$.
   - Data of the pair: yes. It contains the binding ($`\varsigma`$, $`u`$) and the clock levels (through $`u`$, and through $`\tau_{\rm p}`$ if $`\tau_1\neq\tau_2`$).
   - Exceptional: for $`g_i=0\neq g_j`$, $`\varrho_i=O(\epsilon^2)g_j`$; (13.19) does not apply, and $`\mathsf w_i^2`$ follows from (13.13) and (13.18).
   - Derivatives used: (13.19) is (13.13) divided by (13.18). (13.13) uses (11.14) and (11.16): the first derivatives of (11.12) in $`M_i`$, and $`E_b''(0)`$. Of (13.18) only the leading order $`\varrho_i=g_i+O(\epsilon^2)(\lvert g_1\rvert+\lvert g_2\rvert)`$ enters, hence the second derivatives (13.22) only through their order $`\epsilon^2`$, not through their values. The factor $`1+O(\epsilon^2)`$ holds at a fixed ratio $`g_1:g_2`$ with $`g_i\neq0`$ and $`g_1M_1+g_2M_2\neq0`$. For $`g_1M_1+g_2M_2=0`$ the leading term vanishes (no fall at this order, Step 6.4); then $`\mathsf w_i^2=O(\epsilon^4)`$ by (13.13), and its value is not determined here.
4. Free parts alike with one speed (item 4c): $`g_1=g_2=g_{\rm c}`$ and $`\tau_1=\tau_2=\tau`$, so that $`a^{(i)}=-\tau^2g_{\rm c}`$ is (4.24) with $`v_{\max}=\tau d_0`$. Both parts of the pair have the drift acceleration $`a_{\rm pair}`$, and $`\bar x=d_0\,\bar m\,\hat e`$ for both (17.15). Hence

```math
\frac{\mathrm d^2\bar x}{\mathrm d\lambda^2}\Big\vert_{\rm drift}=-\,\frac{\mathsf w^2}{\tau^2}\;\frac{v_{\max}^2}{d_0}\;\varrho_i\;\hat e,\qquad \frac{\mathsf w^2}{\tau^2}=-\frac{\varsigma}{\sqrt{1+u^2}}\,\bigl(1+O(\epsilon^2)\bigr).
\qquad\text{(13.20)}
```

The pair obeys a relation of the form (4.24) in which $`v_{\max}^2`$ is replaced by $`-\varsigma\,v_{\max}^2/\sqrt{1+u^2}`$. With the speed $`\tau d_0`$ itself it holds neither exactly nor to any order in $`\epsilon`$ at fixed $`u`$. For $`w_{11}<0`$ it holds only in the ordered wide-pair limit, with the leading deviation $`\mathsf w^2/\tau^2-1=-\tfrac12u^2+O(u^4)`$; for $`w_{11}>0`$ not at all ($`\mathsf w^2/\tau^2\to-1`$). (13.20) is (13.19) for $`g_1=g_2=g_{\rm c}\neq0`$ and $`\tau_1=\tau_2`$, so it uses the same derivatives: (11.14), (11.16), and of (13.22) only the order $`\epsilon^2`$.

## Result

Every statement is at first order in $`(g_1,g_2,\kappa\langle X\rangle)`$ at fixed $`\lambda`$, followed by the long chain, with the records at leading order in $`\kappa`$. "Derived" means derived here from the quoted inputs and standard facts.

- **Item 1** (class: the contract $`C`$ of the question and the field start $`\varphi`$; exact; derived).
  - The two bodies and the medium evolve by $`C_{\rm red}`$ (13.1). It is the contract of an admissible description of $`b_1,b_2,c`$: yes. A binding with a factor of the field would need a term on three objects, which (1.10) does not contain.
  - $`C_{\rm bod}`$ is (13.2), fixed by $`C,\chi,\varphi`$ up to an additive constant; its gradient terms are (13.3).
  - Fixed by $`C_{\rm bod}`$ and well defined: $`g_1`$ yes; $`g_2`$ yes; $`\kappa\langle X\rangle`$ yes; the operator $`\mathcal K`$ at the centre label yes; the operator $`\mathcal D_\eta`$ at $`\hat r`$ yes, for given $`\eta`$. Only $`\mathcal D_\eta`$ (with the centre label itself) depends on $`\eta`$, unless all gradients vanish.
- **Item 2** (class: every $`W\in\mathcal W`$, all data, every bound level, every $`g\in\mathcal G(\mathcal P_0)`$, all gradients; exact relations at first order; derived).
  - (a) $`v^{(1)}_i=\lambda\langle\alpha\rangle_g+\rho_i(\lambda)`$ (13.7), (13.8), with the same coefficient for both parts, and $`\lvert\rho_i\rvert\le\tau_i\mathsf B_g`$ for all $`\lambda`$ (13.9).
  - (b) $`(\bar m_1-\bar m_2)^{(1)}=\lambda\langle\beta\rangle_g+\sigma(\lambda)`$ with bounded $`\sigma`$ (13.10). There is never a term $`\propto\lambda^2`$. It stays bounded if $`W(-r)^{*}=W(r)`$ (all diagonal on-site bindings); it is zero under the sufficient condition of Step 4.3; otherwise it grows linearly in general (numerical control only). The answer is the same for the common gradient and for $`g_1\neq g_2`$, except that the vanishing case needs $`g_1=g_2`$.
  - (c) $`a^{\rm drift}(P_0)=g_1\alpha_1+g_2\alpha_2+\kappa\langle X\rangle\alpha_X`$ at $`P_0`$ (13.11): window average first, then $`\delta P\to0`$ on $`\mathcal S(P_0,I)`$. The two limits do not commute on this class in general: in the other order the limit at a fixed window does not exist on the class for a window with $`\mathsf f_i\neq0`$ (in particular for $`\partial_P\langle\mathcal K\rangle_{P_0}\neq0`$), and where it exists it depends on the place of the packet; nothing is shown for $`\mathsf f_i=0`$, which includes $`g_1=g_2=0`$ and the levels of items 3 and 4 at $`P_0=0`$ (Step 5.3); the evaluation of that order is not asked. $`E_b''(P_0)`$ is not the only property of the level: $`\partial E_b/\partial M_i`$, $`E_b'`$ and $`\partial E_b'/\partial M_i`$ enter the coefficients of $`g_i`$.
  - (d) The coefficient of the common gradient contains only the rest terms $`\mathcal M_P`$ of (11.6), not its motion and binding terms (13.12).
- **Item 3** (class: diagonal on-site binding, $`\hat w_{11}\neq0`$, level (11.12), $`P_0=0`$; leading order in $`\mathsf R`$ at fixed $`u`$, then limits in $`u`$; derived from (11.14), (11.16)). Closed form (13.13), limits (13.14), ratios (13.15), levels (13.16). The pair falls like its parts only for $`w_{11}<0`$, for free parts that fall alike, and in the ordered wide-pair limit. Its fall is the same for all pairs of levels only if all gradients vanish.
- **Item 4** (same class, $`\langle X\rangle=0`$; derived from (11.19), (11.20), and from (11.12) with the statement on its differentiation that is quoted with (11.14)). Rate (13.17), relative change (13.18) from (13.21), (13.22), number $`\mathsf w_i^2`$ (13.19), relation (13.20). No assumption on a remainder is used: (13.18) rests on the second derivatives of (11.12) in $`M_1,M_2`$ at $`P=0`$, with remainders $`O(\epsilon^4)`$ at fixed $`u`$. Its term of order $`\epsilon^2`$ uses their values (13.22); its leading order $`\varrho_i=g_i`$, and with it the factors $`1+O(\epsilon^2)`$ of (13.19) and (13.20), uses only that they are of order $`\epsilon^2`$.
- **Item 5.**

| | Free part $`i`$ (upper branch, at rest) | Bound pair (level (11.12), $`P_0=0`$, leading order in $`\mathsf R`$) | Pair agrees with its parts |
|---|---|---|---|
| Drift acceleration from rest | $`a^{(i)}=-(g_iM_i+\kappa\langle X\rangle)/\mathfrak m_i`$; (4.16), (8.11) | $`a_{\rm pair}=-\varsigma(1+u^2)^{-1/2}\,\bar a`$; (13.11), (13.13) | at no fixed $`u`$ with a non-zero fall; in the ordered limit $`u\to0`$ iff $`a^{(1)}=a^{(2)}`$ and $`w_{11}<0`$; exceptional (common gradient, $`\tau_1\neq\tau_2`$, $`\langle X\rangle=0`$, $`w_{11}<0`$): equal to the fall of the part with the smaller $`\tau_i`$ at the single value $`u_*`$; (13.14), (13.15) |
| Independent of the clock levels | iff $`\langle X\rangle=0`$; (4.16) | iff $`g_1=g_2=0`$ and $`\langle X\rangle=0`$; (13.16) | at no fixed $`u`$ with a non-zero fall; in the ordered limit $`u\to0`$ iff $`\langle X\rangle=0`$ and $`\tau_1^2g_1=\tau_2^2g_2`$; (13.16) |
| Number that ties it to the relative change of a clock rate ($`\langle X\rangle=0`$) | $`\tau_i^2`$, from $`a^{(i)}=-\tau_i^2g_i`$; (4.24) | for $`g_i\neq0`$: $`\mathsf w_i^2=-\varsigma(1+u^2)^{-1/2}(g_1M_1+g_2M_2)/(g_i(\mathfrak m_1+\mathfrak m_2))`$; (13.18), (13.19) | for $`g_1=g_2`$, $`\tau_1=\tau_2`$: $`\mathsf w^2/\tau^2=-\varsigma(1+u^2)^{-1/2}`$, equal to $`1`$ only for $`w_{11}<0`$ in the ordered limit $`u\to0`$; otherwise $`\mathsf w_i^2=\tau_i^2`$ only at $`u_*`$ (common gradient, one part) or at one value of $`g_1/g_2`$ for given $`u`$ ($`g_1\neq g_2`$); (13.19), (13.20) |

## Consistency checks

1. **One body, and no binding.** (13.8) applied to one free body on a level ($`E=\sigma\omega`$, $`\langle\sigma_3\rangle=\partial E/\partial M=\sigma M/\omega`$, $`\mathcal K=G\sigma_3-\mathcal F`$) gives $`\alpha=-GM(\omega\omega')'/\omega^2+\sigma\mathcal F\omega''=-GM\tau^2\cos2p/\omega^2+\sigma\mathcal F\tau^2(M^2\cos2p-\tau^2\sin^4p)/\omega^3`$. This is (4.7) with $`g_\zeta=0`$, for all $`p`$ and both branches. In the pair, the ordered limit of no binding ($`u\to0`$, $`w_{11}<0`$) of (13.13) is $`\bar a`$, equal to $`a^{(1)}=a^{(2)}`$ when the free parts fall alike. Passed.
2. **Common gradient against (11.6).** With (11.14) at $`P=0`$: $`\mathcal M_0=M_1+M_2-a\Lambda`$ from $`\langle\sigma^{(i)}_3\rangle_0`$, and $`E_b-\langle A_1\rangle_0-\langle A_2\rangle_0-\langle U\rangle_0=M_1+M_2+a+\varsigma\sqrt{w^2+a^2}-2a\Lambda-\varsigma w^2/\sqrt{w^2+a^2}=M_1+M_2-a\Lambda`$. Passed, in agreement with (13.12).
3. **Dimensions.** Labels and $`P`$ are pure numbers and costs are $`1/\lambda`$. $`g_i`$ is per label, $`\kappa\langle X\rangle`$ a cost per label, $`E_b''`$ and $`1/\mathfrak m`$ are costs. (13.8), (13.13): cost$`^2`$, i.e. labels$`/\lambda^2`$. (13.10): $`\beta`$ is a cost, i.e. labels$`/\lambda`$. (13.17): $`1/\lambda`$. (13.19): $`\mathsf w_i^2`$ is a cost$`^2`$, like $`\tau_i^2`$. Passed.

## Open issues

- The second order in the gradients, and the range of $`\lambda`$ over which the first order describes the motion, are not estimated (out of scope); (13.9) and (13.10) bound first-order terms only.
- Outside the scope of the question (item 2(c) as amended): the evaluation of the limits in the other order, with the sharp total label first. Not decided here: whether that order exists for the exceptional members of Step 5.3 ($`\mathsf f_i=0`$), among them the levels of items 3 and 4 at $`P_0=0`$.
- A binding of $`\mathcal W`$ with $`\beta\not\equiv0`$ is exhibited numerically (set S5), not analytically.
- The relative remainders $`O(\epsilon^2)`$ of (13.13)–(13.20) are not determined (numerically up to 4 % at $`\tau_i/M_i=0.2`$) and are not uniform in $`u`$.
- The first-order corrections to the clock reading of a pair in the field (the gradient across the packet) are not derived.
- The results hold for a binding and for motion terms without a factor of the field, the class of the question. Whether another admissible coupling makes the pair fall like its parts is outside this package.
- The remainder of (13.22) rests on the reading of the quoted statement of 11-bound-pair that is given in Step 7.2: a complex neighbourhood of the real data, $`M_1`$ and $`M_2`$ included, whose size does not depend on $`\epsilon`$. That statement is worded for the differentiation that gives (11.14); the second derivatives in $`M_1,M_2`$ follow from its premise, not from its wording. The numerical check finds the order $`\epsilon^4`$ for three sets (section "Code", item 4).

## Code

- **File:** `code/v2/pair_fall_check.py`, role: check. Outputs: `code/v2/output/summary.txt` (all numbers below), `code/v2/output/results.json`, `code/v2/output/first_order_motion.png`. It is the script of v1 with the paths changed and one table added (item 4 below); the evolution, its parameters and its numbers are those of v1.
- **What it does.**
  - It builds the fibre contract (11.1) on $`\lvert r\rvert\le48`$, finds the bound level attached to $`\mathcal B_{++}`$ on a grid of 161 values of $`P`$, and computes $`\alpha`$ (13.8) and $`\beta`$ (13.10) from it ($`E_b''`$ by (11.9); the reduced resolvent by full diagonalization).
  - It builds $`\Phi_g`$ with $`g\propto\cos^4\bigl(\pi(P-P_0)/(2P_c)\bigr)`$ on the chain $`\lvert x_i\rvert\le60`$ (121 sites, dimension 58564), evolves it by $`C_{\rm bod}`$ (13.2) with small gradients of both signs (Chebyshev expansion), and takes the symmetric difference.
  - The slope of a first-order quantity is its mean rate over $`[0,\lambda_{\max}]`$ with the weight $`\propto\sin^4(\pi\lambda/\lambda_{\max})`$. The sampling step is chosen so that no multiple of $`2\pi/\text{step}`$ lies near a frequency $`\lvert E_n(P)-E_b(P)\rvert`$ of the rest.
  - From the numerical level at $`P=0`$ (fibre $`\lvert r\rvert\le64`$) it computes the clock ratio $`\Gamma_i=\langle\sigma^{(i)}_3\rangle_0`$ and its derivative in the data, $`T_{ij}:=M_j\,\partial\Gamma_i/\partial M_j=M_j\,\partial^2E_b(0)/\partial M_j\partial M_i=-2M_j\,\mathrm{Re}\langle\sigma^{(i)}_3\psi_0\vert R_0\vert\sigma^{(j)}_3\psi_0\rangle`$, and compares them with (11.20), with (13.22) and, through (13.21), with (13.18).
- **Sets.** Each with the common gradient, with $`g_1`$ only ($`g_2=0`$), and with a plain gradient in the place of $`\kappa\langle X\rangle`$.
  - S1: $`\tau_i=0.2`$, $`M_i=1`$, $`w_{11}=-0.02`$ ($`u=1.00`$). S2: $`\tau=(0.20,0.18)`$, $`M=(1,1.25)`$, $`w_{11}=-0.02`$ ($`u=1.21`$). S3: $`\tau=(0.20,0.17)`$, $`M=(1,0.9)`$, $`w_{11}=+0.022`$ ($`u=1.22`$). S4: $`\tau=(1,0.8)`$, $`M=(1,1.2)`$, $`w_{11}=-0.9`$. In all four the other $`w_{s_1s_2}`$ are non-zero, $`P_0=0`$ and $`P_c=0.5`$ ($`\delta P=0.106`$).
  - S5 (control): the data of S4 with a binding of range 1 that is neither diagonal nor symmetric, $`P_0=0.2`$, $`P_c=0.4`$ ($`\delta P=0.085`$).
  - Range: $`\lambda\le3000`$ (S1–S3), $`200`$ (S4), $`400`$ (S5). Gradients: $`5\cdot10^{-7}`$ (S1–S3), $`2\cdot10^{-6}`$ (S4, S5).
- **Item 2a.** The slopes of $`v^{(1)}_1`$ and $`v^{(1)}_2`$ agree with $`\langle\alpha\rangle_g`$ of (13.7), in all three configurations, to a relative $`2\cdot10^{-5}`$ (S1), $`1.3\cdot10^{-5}`$ (S2), $`6\cdot10^{-6}`$ (S3), $`4\cdot10^{-7}`$ (S4), $`3\cdot10^{-5}`$ (S5). The rest stays bounded, at most 3 % of the linear part at $`\lambda_{\max}`$.
- **Item 2b.** For S1–S4 the first-order separation stays bounded and relaxes to a constant (slope times $`\lambda_{\max}`$ below 0.5 % of its maximum). For S1 with the common and the plain gradient it is zero within the noise of the difference ($`3\cdot10^{-8}`$ against $`270`$ for $`g_1`$ only), as in Step 4.3. For S5 it grows linearly: slopes $`-0.08662`$, $`-0.02819`$, $`-0.07457`$ against $`\langle\beta\rangle_g=-0.08651`$, $`-0.02813`$, $`-0.07444`$; with $`\lambda\le600`$ the second slope is $`-0.028139`$.
- **Item 3.** The coefficients of (13.13) deviate from those of the numerical level at $`P_0=0`$ by $`-5\cdot10^{-4}`$ to $`+2.5\cdot10^{-3}`$ (S1), up to $`2.9\cdot10^{-3}`$ (S2), and $`-2.2\cdot10^{-2}`$ to $`-3.8\cdot10^{-2}`$ (S3), against $`(\tau_i/M_i)^2\le0.04`$. With $`\tau\to s\tau`$, $`w\to s^2w`$ and $`s=1,\tfrac12,\tfrac14`$ the deviations fall by factors $`3.8`$ to $`4.5`$ per step. The slopes of the evolution agree, to the same deviations, with (13.13) averaged over the packet through (11.12).
- **Item 4 (the derivative of the clock ratio in the data; I1).** Sets S1–S3 and their scalings $`\tau\to s\tau`$, $`w\to s^2w`$, $`s=1,\tfrac12,\tfrac14`$.
  - The four numbers $`T_{ij}`$ deviate from (13.22) by a relative $`5.4\cdot10^{-3}`$ to $`1.1\cdot10^{-2}`$ (S1, S2) and $`-2.7\cdot10^{-2}`$ to $`-7.0\cdot10^{-2}`$ (S3) at $`s=1`$. Per step in $`s`$ the relative deviations fall by factors $`3.8`$ to $`4.0`$ and the absolute ones by $`15`$ to $`16`$: the remainder of (13.22) is of order $`\epsilon^4`$, as Step 7.2 states.
  - $`\varrho_i-g_i`$ from (13.21), for the common gradient, $`g_1`$ only and $`g_2`$ only, deviates from the term of order $`\epsilon^2`$ of (13.18) by up to $`1.6\cdot10^{-2}`$ (S1, S2) and $`5.5\cdot10^{-2}`$ (S3) at $`s=1`$, with factors $`3.9`$ to $`4.0`$ per step.
  - $`1-\Gamma_i`$ deviates from (11.20) by $`7\cdot10^{-3}`$ to $`9\cdot10^{-3}`$ (S1, S2) and $`-4\cdot10^{-2}`$ (S3) at $`s=1`$, with factors $`3.9`$ to $`4.0`$ per step.
  - Checks: a symmetric difference of $`\Gamma_i`$ in $`M_j`$ (relative step $`10^{-4}`$) agrees with the resolvent form to $`7\cdot10^{-8}`$; fibre range $`48`$ against $`64`$: $`5\cdot10^{-12}`$.
- **Convergence** (configuration $`g_1`$ only; relative change of the slopes).
  - Chain: $`45`$ against $`60`$: $`3\cdot10^{-7}`$ (S1), $`5\cdot10^{-8}`$ (S4); $`75`$ against $`60`$: $`1.5\cdot10^{-6}`$ (S5).
  - Gradient doubled: $`2\cdot10^{-6}`$. Other sampling step: below $`10^{-6}`$. Fibre range $`48`$ against $`64`$: $`10^{-13}`$ in $`\alpha`$.
  - Narrower packet ($`P_c=0.35`$): the same agreement with its own $`\langle\alpha\rangle_g`$.
  - Range of $`\lambda`$: on half of the range the slopes deviate by up to $`1.2\cdot10^{-2}`$; the full range reduces this to the values of item 2a.
- **Run.** Once, in the foreground: 414 s. No package was installed.

## Methods used

- Reduction of a contract on an eigenstate of the field operators; partial expectation
- Fibre decomposition under the joint shift of two bodies
- First-order perturbation theory in a term of the contract (Duhamel formula)
- Perturbation theory of an isolated simple eigenvalue; reduced resolvent
- Commutator identities for velocity operators; Hellmann–Feynman relations
- Antiunitary and exchange symmetries of the fibre contract
- Window averaging of bounded oscillating terms; packets with a sharp total label
- Leading-order expansion in a scaling regime with ordered limits
- Mixed second differences (strict supermodularity) for a uniqueness argument
- Numerical evolution by a Chebyshev expansion with a symmetric difference in the gradients
- Second derivatives of an eigenvalue in the data; Cauchy estimate for the derivatives of an analytic remainder
- Mean ergodic theorem for the time average of a unitary group
