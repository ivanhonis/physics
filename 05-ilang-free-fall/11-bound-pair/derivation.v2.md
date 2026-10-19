# Bound pair of two Model D bodies: bound level, curvature, cost and clock rates

- **Subproject:** 05-ilang-free-fall
- **Package:** 11-bound-pair
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-11

## Changes from previous version

Changes against v1, caused by the issues I1–I5 of `verification.md` (external round 1). Steps 1, 3, 4, 5, 6, 8 and 9, the displays (11.1)–(11.3), (11.5)–(11.18) and (11.20), and the three consistency checks are kept word for word (one sentence is added to check 1).

- **I1 (Setup, Step 2, Result item 1).** The operator on the two bodies is now defined from the total contract and the start of the medium, (11.21), with the named assumption $`\langle\chi\vert X\vert\chi\rangle=0`$; every result refers to it. "What remains" in Step 2 now lists every replacement, not only those that keep the stated forms. The binding cost is defined as the distance from the band edge, (11.22).
  - **(11.4) restated.** It now has two columns, "computed from $`C_{\rm bod}`$" and "computed from the listed terms". Changed answers: $`M_i`$ as a listed coefficient: no. $`E_b(P)`$: yes as a total cost only (v1: no). $`E_b(P)-(M_1+M_2)`$: the literal expression is not well defined, (11.22) is (v1: yes). $`E_b(P)-E_b(0)`$, $`E_b''(0)`$, $`\langle\sigma^{(i)}_3\rangle_P`$: yes from $`C_{\rm bod}`$, in general no from the listed terms (v1: yes).
- **I2 (Setup, new Step 5a, Result).** The bullet "Simple level" of the Setup is replaced by "Multiplicity". Step 5a treats degenerate levels: (11.23) and (11.24). (11.5)–(11.9) are unchanged and are stated for simple levels; (11.9) is no longer claimed for a degenerate level.
- **I3 (Step 10, Result item 5, Open issues).**
  - **(11.19) restated.** $`\Gamma_i`$ is $`\langle\sigma^{(i)}_3\rangle_0`$ at the mean rest cost $`\bar M_i`$ (v1: at $`m_i`$), and the remainder is $`O(\delta_i^2(1+\lambda/\lambda_{0,i})^2)`$ (v1: $`O(\delta_i^2(1+g_0\lambda))`$, which was of first order). $`g_0`$ is now the isolation over the range of the levels.
  - New (11.25): the rate to first order in the level spacing. New (11.26): its form in $`\mathsf R`$.
  - **(11.20):** the display is unchanged; the $`M_i`$ of the part whose clock is read is now $`\bar M_i`$ (v1: $`m_i`$).
- **I4 (Step 7, "Other numbers").** $`w_{22}`$ enters $`E_b`$ at order $`\epsilon^6`$ (v1: $`\epsilon^4`$).
- **I5 (Step 7).** The display (11.13) is unchanged; it is now stated for $`j(P)\neq0`$, and the eigenvector at $`j(P)=0`$ is given.
- **Tags.** (11.1)–(11.20) are kept. New: (11.21)–(11.26). Withdrawn: none.
- **Code.** `code/v2/` contains the check of v1, unchanged, and checks of what is new.

## Response to verification

- **I1: Accepted and fixed** in the Setup ("Operator on the two bodies") and in Step 2: (11.21), the restated (11.4) and (11.22); Result item 1 follows. The literal expression $`E_b(P)-(M_1+M_2)`$ is declared not well defined.
- **I2: Accepted and fixed** in the Setup ("Multiplicity") and in the new Step 5a: (11.23) for the first derivatives, (11.24) in place of (11.9), with the list of what holds for every eigenvector and what holds for branch vectors.
- **I3: Accepted and fixed** in Step 10: (11.19) with the rate at the mean level and a remainder of second order on a stated range of $`\lambda`$, (11.25) for the rate to first order, (11.20) and (11.26) in $`\mathsf R`$.
- **I4: Accepted and fixed** in Step 7, "Other numbers": order $`\epsilon^6`$.
- **I5: Accepted and fixed** in Step 7, after (11.13): the eigenvector at $`j(P)=0`$.

## Setup and assumptions

- **Setting.** As in `question.md`: two Model D bodies $`b_1`$, $`b_2`$ of different types, one medium $`c`$, $`C=C_{\rm pair}+C_{\rm rec}`$, $`C_{\rm pair}=C^{\rm D}_1+C^{\rm D}_2+U`$, the binding $`U`$ of the class $`\mathcal W`$, fixed clock levels $`k_1,k_2`$ with $`M_i=M^{(i)}_{k_i}`$, the fibre contract $`H(P)`$, a bound level $`E_b(P)`$ with the eigenvector $`\psi_P`$, the curvature inertia $`\mathfrak m_b=1/E_b''(0)`$, $`\mathfrak m_i=M_i/\tau_i^2`$, and the regime $`\mathsf R`$ ($`\tau_i=\epsilon\hat\tau_i`$, $`w_{s_1s_2}=\epsilon^2\hat w_{s_1s_2}`$, $`\epsilon\to0`$). The bodies, the class $`\mathcal W`$, the diagonal on-site binding, $`\mathsf R`$ and every start are assumptions (M8, M9); a bound level is a distinguished set of states (A11). No field acts.
- **Operator on the two bodies.** The listed $`C_{\rm pair}`$ is a convention of the listing (A5, M6). Every result below refers to the operator $`C_{\rm bod}`$ of (11.21) in Step 2, which is defined by the total contract $`C`$ and the start $`\chi`$ of the medium alone. Assumption (M8): $`\langle\chi\vert X\vert\chi\rangle=0`$. Under it $`C_{\rm bod}=C^{\rm D}_1+C^{\rm D}_2+U`$, and from here on $`C_{\rm pair}`$, $`H(P)`$, $`E_b`$, $`\psi_P`$, $`\tau_i`$, $`M_i`$ and $`W`$ denote this operator, its fibres and its data.
- **Inputs used.**
  - (5.5), (5.6) of 04-ilang-time/05-moving-clock: on a plane wave $`\lvert p\rangle`$ and a level $`k`$ the Model D contract acts as $`-\tau\sin p\,\sigma_1+\mu_k\sigma_3`$, with the eigenvalues $`\pm\omega_k(p)`$, $`\omega_k=\sqrt{\mu_k^2+\tau^2\sin^2p}`$. (5.11) there: $`v_{\max}=\tau\kappa\sigma_X`$. (5.1), (5.21) there: $`P_N(a;\vartheta)`$ and $`q(a;\lambda)=P_N(a;\Gamma(p_0)\lambda/\lambda_0)+\mathcal R`$, with $`\Gamma(0)=1`$.
  - (6.7), (6.20) of 04-ilang-time/06-inertia-internal-energy: the gap $`2M_k`$, the upper branch is the eigenvector $`\lvert1\rangle`$ of $`\sigma_3`$, and $`1/\omega_k''(0)=M_k/\tau^2=I^{\rm lab}_k`$.
  - (17.15) of 03-ilang-space/17-motion and (16.11) of 03-ilang-space/16-common-space: the position of either body is $`\kappa\,\bar m_i\,e`$ with $`\bar m_i`$ the mean position label, and $`r=x_1-x_2`$ is the separation of corresponding points.
  - (21.2), (21.12), (21.15), (21.16) of 03-ilang-space/21-composite-body, as quoted in the question.
- **Notation.** $`\omega_i(p):=\sqrt{M_i^2+\tau_i^2\sin^2p}`$, $`\Omega_i:=\sqrt{M_i^2+\tau_i^2}`$. For item 3: $`a_i:=\tau_i^2/(4M_i)=1/(4\mathfrak m_i)`$, $`a:=a_1+a_2`$, $`j(P):=\sqrt{a_1^2+a_2^2+2a_1a_2\cos2P}`$ (so $`j(0)=a`$), $`w:=w_{11}`$, $`\varsigma:=\mathrm{sgn}w`$, $`u:=\lvert w\rvert/a=\lvert\hat w_{11}\rvert/\hat a`$ and $`\Lambda:=1+\varsigma/\sqrt{1+u^2}\in(0,2)`$. In $`\mathsf R`$ the quantities $`a_i,a,j,w`$ are of order $`\epsilon^2`$ and $`u,\Lambda`$ of order one.
- **Standard facts used.** Weyl's theorem (a finite-range change does not change the bands); exponential decay of the eigenvector of an isolated eigenvalue of a finite-range operator; analytic perturbation theory of an isolated eigenvalue (first and second order); degenerate perturbation theory for an isolated group of eigenvalues (Schrieffer–Wolff), valid for $`\tau_1+\tau_2+\max\lvert w_{s_1s_2}\rvert\ll2\min(M_1,M_2)`$; Rellich's theorem (analytic branches of an isolated eigenvalue of finite multiplicity in one real parameter) with degenerate perturbation theory to second order.
- **Multiplicity.** A bound level lies outside the bands (11.2), which are the essential spectrum of $`H(P)`$, so its multiplicity $`n`$ is finite. The point $`\mathcal B_{\pm\mp}(0)=\{0\}`$ of equal data, of infinite multiplicity, belongs to the bands and is isolated at $`P=0`$ and $`P=\pi`$ only; it is not a bound level. Steps 3–5 treat a simple level ($`n=1`$), which is the case in Step 7. Step 5a treats $`n\ge2`$.
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
- **What remains.** With $`\delta U=0`$, (11.3) reads $`\delta C^{\rm D}_1=t-\alpha`$, $`\delta C^{\rm D}_2=-t-\beta`$, $`\delta C_{\rm rec}=\alpha+\beta`$, so $`\delta C_{\rm pair}=-(\alpha+\beta)=-\delta C_{\rm rec}`$, with every self-adjoint $`\alpha`$ on $`\mathcal H_{b_1}`$ and $`\beta`$ on $`\mathcal H_{b_2}`$ (A5: a single-object term may be listed in the pair term of the body with the medium).
  - Examples: a real constant; $`\alpha=h\,\sigma^{(1)}_3`$, after which the listed coefficient of $`\sigma^{(1)}_3`$ is $`M_1-h`$; a part of the motion term $`A_1`$; $`\alpha=g\,\hat x_1`$. None of them changes $`C`$, the evolution or the record vectors $`(K-\langle K\rangle)\chi`$.
  - The stated forms of the question select among them. For $`C_{\rm rec}`$ to stay a sum of record terms, $`\alpha=\sum_x\alpha_x\lvert x\rangle\langle x\rvert`$ with real numbers $`\alpha_x`$, and $`\beta`$ likewise. The fibres need $`C_{\rm pair}`$ to commute with the joint shift, which gives $`\alpha_x=c_1+gx`$, $`\beta_y=c_2-gy`$, and the one operator $`X`$ in both record terms gives $`g=0`$. Within the stated forms only real constants remain: $`\delta C^{\rm D}_1=t-c_1`$, $`\delta C^{\rm D}_2=-t-c_2`$, $`\delta C_{\rm pair}=-(c_1+c_2)`$.
  - M6 asks for invariance under every replacement (11.3), not only under these. So no quantity may be defined through the listed $`C_{\rm pair}`$. The conventions $`\eta`$ (Step 1) and the choice $`s`$ of the correspondence ($`r\to r+s`$ relabels $`W`$) change no quantity below.

**The operator on the two bodies.** Let $`\langle\chi\vert\,\cdot\,\vert\chi\rangle_c`$ be the partial expectation value over $`\mathcal H_c`$:

```math
C_{\rm bod}:=\langle\chi\vert C\vert\chi\rangle_c=\mathrm{Tr}_c\bigl[C\,(\mathbb 1\otimes\lvert\chi\rangle\langle\chi\rvert)\bigr]=C^{\rm D}_1+C^{\rm D}_2+U+\kappa\,\langle\chi\vert X\vert\chi\rangle\,(\hat x_1+\hat x_2).
\qquad\text{(11.21)}
```

The first two expressions use $`C`$ and $`\chi`$ only. So $`C_{\rm bod}`$ is the same operator on $`\mathcal H_{b_1}\otimes\mathcal H_{b_2}`$ in every listing; in a listing changed by $`\alpha,\beta`$ the listed pair term changes by $`-\alpha-\beta`$ and $`C_{\rm bod}`$ does not. The last expression is its value in the listing of the question.

- **Why this operator.** $`L(\phi\otimes\chi)=\langle\phi\vert C_{\rm bod}\vert\phi\rangle`$ is the total cost (1.8) of a product start. The view of $`\{b_1,b_2\}`$ of such a start evolves by $`C_{\rm bod}`$ up to second order in $`C-C_{\rm bod}\otimes\mathbb 1=\kappa(\hat x_1+\hat x_2)\otimes(X-\langle X\rangle)`$, because the mean of this operator in $`\chi`$ vanishes. This is the weak-record regime.
- **Assumption** $`\langle\chi\vert X\vert\chi\rangle=0`$ (M8). Then $`C_{\rm bod}`$ is the listed $`C_{\rm pair}`$ of the question and commutes with the joint shift. Without the assumption $`C_{\rm bod}`$ contains the uniform gradient $`\kappa\langle X\rangle(\hat x_1+\hat x_2)`$, which does not commute with the joint shift and is of order $`\kappa`$ on a fixed chain; the results below then hold at leading order in $`\kappa`$ only.
- **Data.** By the argument of the range condition, the split $`C_{\rm bod}=K_1\otimes\mathbb 1+\mathbb 1\otimes K_2+U`$ with $`U\in\mathcal W`$ is unique up to one real constant ($`K_1+t`$, $`K_2-t`$). So $`U`$, and $`K_1`$, $`K_2`$ up to a constant, are fixed by $`C`$ and $`\chi`$. $`\tau_i`$, the gaps $`2M^{(i)}_k`$ and the bands (11.2) are read from $`K_i`$, which is $`C^{\rm D}_i`$ up to the constant.

The seven quantities, under every replacement (11.3):

```math
\begin{array}{l|l|l}
& \text{computed from } C_{\rm bod} \text{ of (11.21)} & \text{computed from the listed terms}\\ \hline
W(r) & \text{yes, by the range condition (no without it)} & \text{yes, the same, if the listed } U\in\mathcal W\\
M_i & \text{yes as half the gap } 2M_i;\ \text{no as a cost of } b_i & \text{no (the listed coefficient of } \sigma^{(i)}_3)\\
E_b(P) & \text{yes as a total cost (1.8) only; no as a cost of the pair} & \text{no}\\
E_b(P)-(M_1+M_2) & \text{yes as } E_{\rm bind}(P) \text{ of (11.22)} & \text{no: the literal expression is not well defined}\\
E_b(P)-E_b(0),\ E_b''(0) & \text{yes} & \text{no (unchanged under constants only)}\\
\langle\sigma^{(i)}_3\rangle_P & \text{yes (for } n\ge2 \text{ it depends on the eigenvector)} & \text{no (unchanged under constants only)}
\end{array}
\qquad\text{(11.4)}
```

- **$`W(r)`$.** $`\delta U=0`$ in every replacement that keeps $`U\in\mathcal W`$. $`U`$ is the only element of $`\mathcal W`$ for which $`C_{\rm bod}-U`$ is a sum of single-object operators.
- **$`M_i`$.** Half the difference of the two eigenvalues of $`K_i`$ on the level $`k_i`$ at the plane-wave label $`0`$, (6.7). The listed coefficient of $`\sigma^{(i)}_3`$ changes under $`\alpha=h\,\sigma^{(i)}_3`$. The branch costs $`\pm M_i`$ of $`b_i`$ change by the constant $`t`$.
- **$`E_b(P)`$.** It is an eigenvalue of the fibre of $`C_{\rm bod}`$. For $`\Phi`$ of Step 4, $`L(\Phi\otimes\chi)=\int\lvert g\rvert^2E_b`$ is a total cost, which does not depend on the listing (A5). It is not a cost of the pair apart from the medium: which contract carries a constant or a single-object term is a convention, and the eigenvalue of the listed $`C_{\rm pair}`$ changes ($`\delta E_b=-(c_1+c_2)`$ under constants). Its zero enters no reading. Where a later step speaks of the cost of the pair, it means $`E_b`$ in this sense.
- **$`E_b(P)-(M_1+M_2)`$.** The literal expression is not well defined, with the listed coefficients and also with the half gaps and $`E_b`$ of the listed $`C_{\rm pair}`$: a constant $`c_1+c_2`$ listed in the record terms shifts this $`E_b`$ and no half gap. Well defined is the distance from the band edge:

```math
E_{\rm bind}(P):=E_b(P)-e_{++}(0),\qquad e_{++}(P):=\min\mathcal B_{++}(P),\qquad e_{++}(0)=M_1+M_2,\qquad E_{\rm bind}:=E_{\rm bind}(0).
\qquad\text{(11.22)}
```

  $`e_{++}(P)`$ is the least sum of the upper-branch costs of $`K_1`$ and $`K_2`$ with the total label $`P`$; the constant $`t`$ cancels in it. $`E_{\rm bind}(P)`$ is a difference of two total costs of the same $`C`$. It is also unchanged when a constant is added to $`C`$, which changes the weighting by a common phase (1.2) and no reading; $`E_b(P)`$ alone, and $`E_b(P)`$ minus the half gaps, are not. For the $`C`$ of the question the two forms coincide, because $`C_{\rm bod}`$ has no constant term: $`e_{++}(0)=M_1+M_2`$ by (11.2).
- **$`E_b(P)-E_b(0)`$, $`E_b''(0)`$.** Differences of total costs. Computed from the listed $`C_{\rm pair}`$ they change under $`\alpha=h\,\sigma^{(1)}_3`$ (in (11.12): $`M_1\to M_1-h`$).
- **$`\langle\sigma^{(i)}_3\rangle_P`$.** $`\sigma^{(i)}_3`$ is diagonal in the places of $`b_i`$: it is the reading of the branch label, (1.3), the probability of $`s_i=1`$ minus that of $`s_i=2`$. $`\psi_P`$ is an eigenvector of the fibre of $`C_{\rm bod}`$. With $`\psi_P`$ of the listed $`C_{\rm pair}`$ it changes under $`\alpha=h\,\sigma^{(1)}_3`$.

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

### Step 5a. Degenerate bound levels (items 2a–2c)

Let $`E_b`$ be an eigenvalue of $`H(P)`$ of multiplicity $`n\ge2`$ outside the bands, at given data and $`P`$. Let $`\mathcal E_b`$ be its eigenspace, $`\Pi_b`$ the projector on it, $`\bar Q:=\mathbb 1-\Pi_b`$ and $`\hat S:=\bar Q\,(H(P)-E_b)^{-1}\bar Q`$ the reduced resolvent, which is bounded. Every vector of $`\mathcal E_b`$ decays exponentially.

Let $`\xi`$ be one of the six real parameters $`M_1,M_2,\tau_1,\tau_2,\theta,P`$, the others fixed. $`H`$ is analytic in $`\xi`$, with $`\partial_{M_i}H=\sigma^{(i)}_3`$, $`\tau_i\partial_{\tau_i}H=A_i`$, $`\partial_\theta H=U`$, $`\partial_PH=V_\eta`$. By Rellich's theorem the eigenvalues near $`E_b`$ are $`n`$ analytic functions $`E^{(\nu)}(\xi)`$, the *branches of $`\xi`$*, with analytic orthonormal eigenvectors; at the given point these are the *branch vectors* $`\psi^{(\nu)}_\xi\in\mathcal E_b`$. A bound level that is differentiable in $`\xi`$ is one branch. First-order degenerate perturbation theory gives

```math
\Pi_b\,(\partial_\xi H)\,\Pi_b\;\psi^{(\nu)}_\xi=\partial_\xi E^{(\nu)}\;\psi^{(\nu)}_\xi ,\qquad
\langle\psi\vert\partial_\xi H\vert\psi\rangle=\sum_{\nu=1}^{n}\bigl\lvert\langle\psi^{(\nu)}_\xi\vert\psi\rangle\bigr\rvert^2\,\partial_\xi E^{(\nu)}\quad\text{for every unit vector }\psi\in\mathcal E_b .
\qquad\text{(11.23)}
```

- **For every eigenvector of the level** (every unit vector $`\psi\in\mathcal E_b`$):
  - (11.6), as the expectation value of (11.1) in an eigenvector;
  - $`\langle V_1\rangle=\langle V_2\rangle`$, and more: $`\Pi_bV_1\Pi_b=\Pi_bV_2\Pi_b`$, because $`\langle\psi\vert[H(P),\hat r]\vert\psi'\rangle=0`$ for $`\psi,\psi'\in\mathcal E_b`$;
  - the second relation of (11.23): each of the six expectation values is a mean of the $`n`$ branch derivatives. It is a derivative only if $`\psi`$ is an eigenvector of the matrix $`\Pi_b(\partial_\xi H)\Pi_b`$.
- **For the branch vectors of the parameter that is varied.** (11.5) holds for $`M_i`$, $`\tau_i`$, $`\theta`$ and (11.7) for $`P`$, each with the eigenvectors of its own matrix $`\Pi_b(\partial_\xi H)\Pi_b`$. The six matrices need not commute, so in general no eigenvector gives all the derivatives. If $`\xi`$ does not split the level (its $`n`$ branches coincide), its matrix is $`\partial_\xi E_b\,\Pi_b`$, and its identity holds for every eigenvector.
- **(11.8).** A state built from one branch of $`P`$ obeys (11.8). So does a state $`\Phi=\int\mathrm dP\sum_\nu g_\nu(P)\lvert P;\psi^{(\nu)}_P\rangle`$ built from a level that is $`n`$-fold on the support of the $`g_\nu`$, with $`\sum_\nu\lvert g_\nu\rvert^2`$ in place of $`\lvert g\rvert^2`$: the two bodies have the same mean velocity. Control: where two branches have different values, $`\langle\psi^{(\nu)}\vert(V_1-V_2)\vert\psi^{(\nu')}\rangle=i\bigl(E^{(\nu)}-E^{(\nu')}\bigr)\langle\psi^{(\nu)}\vert\hat r\vert\psi^{(\nu')}\rangle`$, and in a superposition of the two the mean velocities differ by a term that oscillates as $`e^{\pm i(E^{(\nu)}-E^{(\nu')})\lambda}`$. Such a state is built from two bound levels.
- **What replaces (11.9).** Second-order degenerate perturbation theory in $`P`$ gives, for a branch vector $`\psi^{(\nu)}_P`$ and with $`\langle\cdot\rangle_\nu`$ its expectation value:

```math
E^{(\nu)\prime\prime}(P)=-\eta^2\langle A_1\rangle_\nu-(1-\eta)^2\langle A_2\rangle_\nu-2\,\bigl\langle V_\eta\psi^{(\nu)}_P\big\vert\hat S\big\vert V_\eta\psi^{(\nu)}_P\bigr\rangle,\qquad \hat S=\bar Q\bigl(H(P)-E_b\bigr)^{-1}\bar Q .
\qquad\text{(11.24)}
```

  The sum over the rest of the spectrum leaves out the whole eigenspace $`\mathcal E_b`$. If several branches have the same first derivative, with $`\Pi'`$ the projector on their branch vectors, their second derivatives are the eigenvalues of $`\Pi'\bigl[\partial_P^2H-2V_\eta\hat SV_\eta\bigr]\Pi'`$, and their branch vectors are its eigenvectors. For $`n=1`$, (11.24) is (11.9). For $`n\ge2`$, (11.9) is not defined: $`Q_P(H(P)-E_b)^{-1}Q_P`$ does not exist on the rest of $`\mathcal E_b`$.
- **Members.** Degenerate levels exist in $`\mathcal W`$.
  - For a diagonal on-site binding, by (11.10) a root of $`F_-`$ can be placed on a root of $`F_+`$ by the choice of $`w_{12}`$, $`w_{21}`$. All six operators commute with $`\Xi`$ of Step 6, so the vectors with a definite $`\Xi`$ are branch vectors of every parameter.
  - For the on-site binding $`W_0=-G(E_0,P_0)^{-1}`$ on the span of $`\lvert11\rangle`$, $`\lvert22\rangle`$, with $`G`$ of Step 6 and $`E_0`$ outside the bands, $`\mathbb 1_4+GW_0`$ vanishes on that span, so $`E_0`$ is a twofold level of $`H(P_0)`$. For one such member the six matrices do not commute; this statement rests on the code (`code/v2/check_bound_pair.py`, set X).

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

The forms of $`\rho`$ and (11.13) are for $`j(P)\neq0`$. $`j(P)=0`$ occurs only for $`a_1=a_2`$ at $`P=\pm\frac\pi2`$. Then $`J=0`$, $`\alpha`$ is not defined and not needed, the chain has no hopping, and the eigenvector of the changed site is $`\psi_P(r)=\delta_{r,0}\lvert11\rangle`$ up to $`O(\epsilon)`$, with $`E_b=M_1+M_2+a+w+O(\epsilon^4)`$. These are the limits $`\rho\to0`$, $`\mathcal N_P\to1`$ of (11.13) and the value of (11.12) at $`j=0`$.

- **Existence and number.** The level (11.12) is at the distance $`\sqrt{w^2+j^2}-j`$ from the band, of order $`\epsilon^2`$, and the remainder of $`H_{\rm eff}`$ is $`O(\epsilon^4)`$ in norm. So for small $`\epsilon`$: $`H(P)`$ has a bound level at a distance of order $`\epsilon^2`$ from $`\mathcal B_{++}(P)`$ if and only if $`\hat w_{11}\neq0`$. It is then exactly one, simple, for every $`P\in(-\pi,\pi]`$: below the band for $`\hat w_{11}<0`$, above the band for $`\hat w_{11}>0`$.
- **What the order leaves out.** Every other point of the spectrum near $`M_1+M_2`$ lies within $`O(\epsilon^4)`$ of the band. For $`\hat w_{11}=0`$, and in the sector $`\Xi=-1`$ (the branches $`\lvert11\rangle`$ on odd $`r`$, where $`w_{12},w_{21}`$ act at order $`\epsilon^4`$), a bound level, if any, is at such a distance and is not seen at leading order.
- **Other numbers.** $`w_{22}`$ enters $`E_b`$ at order $`\epsilon^6`$. First-order perturbation theory in the number $`w_{22}`$ alone gives $`\partial E_b/\partial w_{22}=\lvert\langle22\vert\psi_P(0)\rangle\rvert^2`$; the branch $`\lvert22\rangle`$ needs two flips, so its amplitude is $`O(\epsilon^2)`$ and this derivative $`O(\epsilon^4)`$, and $`w_{22}=O(\epsilon^2)`$. (In $`F_+`$: the term $`w_{11}w_{22}g_\times^2`$ is $`O(\epsilon^4)`$ against a slope $`w_{11}\partial_EG_{11}`$ of order $`\epsilon^{-2}`$.) The $`O(\epsilon^4)`$ remainder of (11.12) has other sources. $`w_{12},w_{21}`$ do not enter this level at any order.

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

**(a)** Start: the clock label of the part $`i`$ in $`\lvert0\rangle=N_i^{-1/2}\sum_k\lvert f_k\rangle`$, the other part on its level $`k_j`$, the medium in $`\chi`$, and the positions and branches in $`\Phi`$ of Step 4, built from the bound eigenvectors of the levels $`(0,k_j)`$ with $`\lvert g\rvert^2`$ of width $`\delta P`$ around $`0`$. The levels are conserved, so the component on $`\lvert f_k\rangle`$ evolves with $`M_i\to m_i+d^{(i)}_k`$.

Let $`D_i:=d^{(i)}_{N_i-1}`$ be the spread of the levels of the clock, $`\bar d_i:=\frac1{N_i}\sum_kd^{(i)}_k=\frac{\pi(N_i-1)}{N_i\lambda_{0,i}}=\frac{D_i}2`$ their mean and $`\bar M_i:=m_i+\bar d_i`$ the mean rest cost. Let the bound level at $`P=0`$ be simple and at a distance of at least $`g_0`$ from the rest of the spectrum for all $`M_i\in[m_i,m_i+D_i]`$, and let $`\delta_i:=D_i/g_0`$. By analytic perturbation theory in $`M_i`$ ($`\partial_{M_i}H=\sigma^{(i)}_3`$ has norm one), $`E_b`$ and $`\psi_P`$ are analytic in $`M_i`$ on this range, with $`\lVert\partial_{M_i}\psi_P\rVert\le1/g_0`$, $`\lvert\partial^2_{M_i}E_b\rvert\le2/g_0`$ and $`\partial^n_{M_i}E_b=O(g_0^{1-n})`$. With (11.5), around the mean level:

```math
E^{[k]}_b(P)=\Bigl[E_b(P)+\bigl(d^{(i)}_k-\bar d_i\bigr)\langle\sigma^{(i)}_3\rangle_P+\tfrac12\bigl(d^{(i)}_k-\bar d_i\bigr)^2\,\partial^2_{M_i}E_b(P)\Bigr]_{M_i=\bar M_i}+O\bigl(D_i^3/g_0^2\bigr).
```

For a diagonal on-site binding $`\psi(r)\to\sigma^{(1)}_3\sigma^{(2)}_3\psi(-r)`$ maps $`H(P)`$ to $`H(-P)`$, so $`E_b`$ and $`\langle\sigma^{(i)}_3\rangle_P`$ are even in $`P`$: the pair is at rest by (11.8), and $`\langle\sigma^{(i)}_3\rangle_P=\langle\sigma^{(i)}_3\rangle_0+O(P^2)`$. The reading of the clock label of $`i`$ (the partition by $`a_i`$, (1.3)) has the statistics $`N_i^{-2}\sum_{k,k'}e^{2\pi i(k-k')a/N_i}\langle\Psi_{k'}(\lambda)\vert\Psi_k(\lambda)\rangle`$. Four contributions enter the overlaps.

- **Linear term.** It gives the phases $`e^{-i(d_k-d_{k'})\Gamma_i\lambda}`$ with $`\Gamma_i:=\langle\sigma^{(i)}_3\rangle_0`$ at $`M_i=\bar M_i`$. With $`d^{(i)}_k=\frac{2\pi k}{N_i\lambda_{0,i}}`$ this is $`P_{N_i}`$ of (5.1) exactly.
- **Quadratic term.** It is a phase $`\beta_k`$ with $`\beta_k=\beta_{N_i-1-k}`$ and $`\lvert\beta_k\rvert\le\frac18D_i^2\,\lvert\partial^2_{M_i}E_b\rvert\,\lambda\le\frac\pi2\,\delta_i\,\lambda/\lambda_{0,i}`$. A phase that is even about the middle of the levels changes the statistics only at second order, because $`\sum_k\beta_ke^{ik\phi}`$ and $`\sum_ke^{ik\phi}`$ have the same phase $`e^{i(N_i-1)\phi/2}`$. This is why the level is expanded around $`\bar M_i`$.
- **Cubic term.** It is odd, enters at first order and is $`O(\delta_i^2\,\lambda/\lambda_{0,i})`$.
- **Eigenvector of the start.** The start has on every level the eigenvector of the level $`0`$, which differs from that of the level $`k`$ by at most $`d^{(i)}_k/g_0`$ in norm. This changes the overlaps by $`O(\delta_i^2)`$ for every $`\lambda`$.

In the form of (5.21):

```math
q_i(a;\lambda)=P_{N_i}\Bigl(a;\Gamma_i\frac{\lambda}{\lambda_{0,i}}\Bigr)+\mathcal R_i,\qquad \Gamma_i=\langle\sigma^{(i)}_3\rangle_0\Big\vert_{M_i=\bar M_i}=\frac{\partial E_b(0)}{\partial M_i}\Big\vert_{M_i=\bar M_i},\qquad \mathcal R_i=O\bigl(\delta_i^2(1+\lambda/\lambda_{0,i})^2\bigr)+O\bigl(\delta P^2(1+\lambda/\lambda_{0,i})\bigr)+O(\kappa).
\qquad\text{(11.19)}
```

Expanding $`\Gamma_i`$ around $`M_i=m_i`$, with $`Q_0`$ of (11.9) at $`P=0`$:

```math
\Gamma_i=\Gamma^{(0)}_i+\bar d_i\,\partial^2_{M_i}E_b(0)+O(\delta_i^2),\qquad \Gamma^{(0)}_i:=\langle\sigma^{(i)}_3\rangle_0\Big\vert_{M_i=m_i},\qquad \partial^2_{M_i}E_b(0)=\partial_{M_i}\langle\sigma^{(i)}_3\rangle_0=-2\,\bigl\langle\sigma^{(i)}_3\psi_0\big\vert Q_0\bigl(H(0)-E_b\bigr)^{-1}Q_0\big\vert\sigma^{(i)}_3\psi_0\bigr\rangle .
\qquad\text{(11.25)}
```

- **Rate and ratio.** The rate is $`\Gamma_i/\lambda_{0,i}`$. Its ratio to the rate $`1/\lambda_{0,i}`$ of the free part at rest ((5.21) with $`\Gamma(0)=1`$) is $`\Gamma_i\le1`$: the expectation value $`\langle\sigma^{(i)}_3\rangle_0`$ of item 2(a), taken at the mean rest cost $`\bar M_i`$ of the part $`i`$ and on the level $`k_j`$ of the other part. (11.25) is the rate to first order in the level spacing. Applied to one free body, with $`\omega_0(p_0)`$ at the rest cost $`\mu`$ in place of $`E_b`$, it gives $`\gamma\bigl[1+\frac{(N-1)\epsilon}2(1-\gamma^2)\bigr]`$ of (5.21), where $`\frac{(N-1)\epsilon}2=\bar d/m`$.
- **Two orders.** The level to first order in $`d^{(i)}_k`$ gives only $`\Gamma^{(0)}_i`$, the rate to zeroth order: the advance $`\Gamma_i\lambda/\lambda_{0,i}`$ is then wrong by $`\bar d_i\,\partial^2_{M_i}E_b\,\lambda/\lambda_{0,i}`$, which is of first order in $`\delta_i`$. The rate to first order in the level spacing needs the level to second order in $`d^{(i)}_k`$: a sum over the rest of the spectrum, as in (11.9).
- **Range of $`\lambda`$.** $`\mathcal R_i`$ is small for $`\delta_i\ll1`$ on $`0\le\lambda\ll\lambda_{0,i}/\delta_i`$, with $`\delta P^2\lambda/\lambda_{0,i}\ll1`$ and $`\kappa\to0`$ at fixed $`\lambda`$. On $`\lambda_{0,i}\lesssim\lambda\ll\lambda_{0,i}/\delta_i`$ the first-order term of (11.25) changes the statistics by more than $`\mathcal R_i`$. The condition $`\delta_i\ll1`$ is sufficient, not necessary (see (b)).

Class: every diagonal on-site binding and every bound level at $`P=0`$ that is simple for all $`M_i`$ in the range of the levels. Status: the rate to first order in the level spacing; the statistics up to the remainder $`\mathcal R_i`$, which is of second order.

**(b)** With (11.14), at leading order in $`\mathsf R`$ (remainder $`O(\epsilon^4)`$), with $`M_i=\bar M_i`$ and $`M_j=M^{(j)}_{k_j}`$:

```math
\Gamma_i=1-\frac{\tau_i^2}{4M_i^2}\,\Lambda,\qquad \Lambda=1+\frac{\varsigma}{\sqrt{1+u^2}},\qquad \frac{1-\Gamma_1}{1-\Gamma_2}=\frac{\tau_1^2/M_1^2}{\tau_2^2/M_2^2}.
\qquad\text{(11.20)}
```

To first order in the level spacing, with $`a_i`$, $`a`$, $`u`$, $`\Lambda`$ taken at $`M_i=m_i`$:

```math
\Gamma_i=1-\frac{\tau_i^2}{4m_i^2}\Bigl[\Lambda-\frac{\bar d_i}{m_i}\Bigl(2\Lambda+\varsigma\,\frac{a_i}{a}\,\frac{u^2}{(1+u^2)^{3/2}}\Bigr)\Bigr]+O\Bigl(\frac{a_i\,\bar d_i^{\,2}}{m_i^3}\Bigr)+O(\epsilon^4).
\qquad\text{(11.26)}
```

This is (11.25) with $`\partial^2_{M_i}E_b(0)=\frac{a_i}{M_i^2}\bigl[2\Lambda+\varsigma\frac{a_i}{a}\frac{u^2}{(1+u^2)^{3/2}}\bigr]`$, from (11.12) and $`\partial_{M_i}a=-a_i/M_i`$. In $`\mathsf R`$ the bounds through $`g_0=O(\epsilon^2)`$ are not sharp. By (11.12), (11.13) and the analyticity used in Step 8, $`E_b-M_1-M_2`$ and $`\psi_0`$ depend on $`M_i`$ on the scale $`M_i`$: $`\partial^n_{M_i}E_b=O(a_i/M_i^{\,n})`$ for $`n\ge2`$ and $`\lVert\partial_{M_i}\psi_0\rVert=O(1/M_i)`$. So $`\mathcal R_i`$ of (11.19) holds with $`\delta_i`$ replaced by $`D_i/M_i`$, also for $`D_i\gg g_0`$.

Both clocks are slowed. They are not slowed by the same factor: $`\Lambda`$ is common, and the factors agree at this order if and only if $`\tau_1/M_1=\tau_2/M_2`$ (for example equal data). The third relation of (11.20) compares the two ratios at one pair $`(M_1,M_2)`$. The two readings are two starts, with the pairs $`(\bar M_1,M^{(2)}_{k_2})`$ and $`(M^{(1)}_{k_1},\bar M_2)`$, which changes the relation by relative terms of first order in $`d^{(i)}_k/M_i`$. For a wide pair with $`w_{11}<0`$, $`1-\Gamma_i=\frac{\tau_i^2}{8M_i^2}u^2`$; for a tight pair $`1-\Gamma_i=\frac{\tau_i^2}{4M_i^2}(1+\frac aw)`$. Without a binding $`\Gamma_i=1`$.

## Result

Classes, regimes and statuses. Every result refers to $`C_{\rm bod}`$ of (11.21), under the assumption $`\langle\chi\vert X\vert\chi\rangle=0`$. Items 1 and 2 hold for every $`W\in\mathcal W`$, all data, every bound level and every $`P\in\mathcal P`$; they are exact. For a simple level they are (11.5)–(11.9); for a degenerate level they hold in the form of Step 5a, (11.23) and (11.24). Item 3(a) and the control 4(d) are exact, for every diagonal on-site binding (4(d): no binding) and all data. Items 3(b)–(d), 4(a)–(c) and 5(b) hold for every diagonal on-site binding in $`\mathsf R`$ at leading order, with the remainders stated. Item 5(a) holds for every diagonal on-site binding and all data, for a bound level at $`P=0`$ that is simple over the range of the levels of the clock: the rate to first order in the level spacing, the statistics up to a remainder of second order.

1. **Structure.** $`H(P)`$ is (11.1), with the convention $`\eta`$. The two-body bands and their edges at $`P=0`$ are (11.2), for every $`W`$. The replacements are (11.3); the range condition fixes $`U`$, and every single-object term can still be listed in a body term or in a record term (within the stated forms: only constants). The operator to which the results refer is $`C_{\rm bod}`$ (11.21). The seven answers are (11.4).
   - Computed from the listed terms, only $`W(r)`$ is well defined.
   - Computed from $`C_{\rm bod}`$: $`W(r)`$ yes; $`M_i`$ yes as half the gap, no as a cost of $`b_i`$; $`E_b(P)`$ yes as a total cost (1.8) only; $`E_b(P)-E_b(0)`$, $`E_b''(0)`$ and $`\langle\sigma^{(i)}_3\rangle_P`$ yes.
   - The literal expression $`E_b(P)-(M_1+M_2)`$ is not well defined. Well defined is the distance $`E_{\rm bind}(P)`$ from the band edge (11.22), which equals it for the $`C`$ of the question when both are computed from $`C_{\rm bod}`$.
2. **Exact relations.** The five derivatives are (11.5) and the scaling relation is (11.6). $`E_b'(P)=\langle V_1\rangle_P=\langle V_2\rangle_P`$ (11.7), and both mean position labels move at the rate $`\int\lvert g\rvert^2E_b'`$ (11.8): the two bodies have the same mean velocity. $`E_b''(P)`$ is (11.9). For a degenerate level: (11.6), $`\langle V_1\rangle=\langle V_2\rangle`$ and the mean rule of (11.23) hold for every eigenvector; (11.5) and (11.7) hold for the branch vectors of the parameter that is varied (11.23); (11.24) replaces (11.9); a state built from one level has equal mean velocities of the two bodies.
3. **Diagonal on-site binding.** The equation is (11.10), exact for all data. In $`\mathsf R`$: a bound level at a distance of order $`\epsilon^2`$ from $`\mathcal B_{++}`$ exists iff $`\hat w_{11}\neq0`$, it is one, with $`E_b(P)`$ of (11.12) (remainder $`O(\epsilon^4)`$) and $`\psi_P`$ of (11.13) (up to $`O(\epsilon)`$; at $`j(P)=0`$ it is $`\delta_{r,0}\lvert11\rangle`$), from the effective contract (11.11); only $`w_{11}`$ enters ($`w_{22}`$ at order $`\epsilon^6`$). The five leading terms are (11.14), the limits (11.15).
4. **Curvature, inertias, cost.** $`\mathfrak m_b=\mathfrak m_1+\mathfrak m_2-4\mathfrak m_1\mathfrak m_2E_{\rm bind}`$ (11.16), relative remainder $`O(\epsilon^2)`$. For $`\tau_1=\tau_2`$, $`\tau^2\mathfrak m_b`$ differs from the cost of the pair and from $`\sum_iM_i\langle\sigma^{(i)}_3\rangle_0`$ at order $`\epsilon^0`$, by $`-\frac{4M_1M_2}{\tau^2}E_{\rm bind}`$ (11.17). The comparison with 03-ilang-space/21-composite-body is Step 9(c). The control without a binding is (11.18), exact.
5. **Clocks.** The statistics are (11.19), with the ratio $`\Gamma_i=\langle\sigma^{(i)}_3\rangle_0`$ at the mean rest cost $`\bar M_i`$. To first order in the level spacing the ratio is (11.25). The remainder is of second order in $`\delta_i`$ and small for $`\lambda\ll\lambda_{0,i}/\delta_i`$. In $`\mathsf R`$, $`\Gamma_i`$ is (11.20) at $`M_i=\bar M_i`$, and (11.26) to first order in the level spacing: the two clocks are not slowed by the same factor unless $`\tau_1/M_1=\tau_2/M_2`$.

Controls (M9). (11.5)–(11.9) are proven for every simple level of the class and (11.23), (11.24) for every degenerate one, so no member violates them. (11.9) fails for a degenerate level, and (11.19) with $`\Gamma^{(0)}_i`$ in place of $`\Gamma_i`$ fails at first order (sets X and the clock runs under "Code"). An operator read from the listed terms fails as the operator of the two bodies in a listing that differs by a single-object term (Step 2; the last check under "Code"). The leading-order results fail outside $`\mathsf R`$: for $`\tau_i/M_i`$ of order one the closed forms (11.14) are off by $`8`$ per cent ($`E_b''(0)`$) to $`23`$ per cent ($`\langle U\rangle_0`$) (set E under "Code"). Further controls: no binding (11.18), $`\tau_1\neq\tau_2`$ (Step 9d), wide against tight (11.15).

## Consistency checks

1. **Dimensions.** $`\tau_i`$, $`M_i`$, $`w`$, $`a_i`$, $`j`$, $`E_b`$, $`E_b''`$ are costs ($`P`$ and $`q`$ are numbers); $`u`$, $`\rho`$, $`\Lambda`$, $`\langle\sigma^{(i)}_3\rangle`$, $`\Gamma_i`$ are numbers; $`\mathfrak m`$ is an inverse cost, and so is $`\mathfrak m_1\mathfrak m_2E_{\rm bind}`$ in (11.16); $`\Gamma_i\lambda/\lambda_{0,i}`$ in (11.19) is a number. $`D_i`$, $`\bar d_i`$, $`g_0`$ are costs, $`\delta_i`$ and $`\bar d_i\,\partial^2_{M_i}E_b`$ in (11.25) are numbers. Passed.
2. **No binding.** For $`w\to0^-`$, (11.12) tends to $`M_1+M_2+a-j(P)`$, the lower edge of $`\mathcal B_{++}(P)`$ at this order, and (11.14) gives $`E_b''(0)\to4a_1a_2/a=1/(\mathfrak m_1+\mathfrak m_2)`$, which is (11.18), with $`\langle\sigma^{(i)}_3\rangle_0\to1`$, $`\langle A_i\rangle_0\to0`$, $`\langle U\rangle_0\to0`$, $`\Gamma_i\to1`$. Passed.
3. **Scaling relation on the closed form.** With (11.14) the right side of (11.6) at $`P=0`$ is $`M_1+M_2-a\Lambda+2a\Lambda+\varsigma\frac{w^2}{\sqrt{w^2+a^2}}=M_1+M_2+a+\varsigma\frac{a^2+w^2}{\sqrt{w^2+a^2}}=E_b(0)`$ of (11.12). Passed.

## Open issues

- Whether $`\mathfrak m_b`$ is the inertia of the pair in a response to a gradient is not derived here (not asked; (11.17) shows that it is not the cost divided by $`\tau^2`$).
- Outside the order asked in item 3(b): bound levels closer than $`O(\epsilon^4)`$ to the band (for $`\hat w_{11}=0`$, and in the sector $`\Xi=-1`$) are neither established nor excluded.
- The coefficients of the $`O(\epsilon^4)`$ remainders are not derived; the code only confirms their order.
- (11.19) is derived for a bound level that stays simple over the range of the levels of the clock. The condition $`D_i\ll g_0`$ is sufficient; in $`\mathsf R`$, where $`g_0`$ is of order $`\epsilon^2`$, it is replaced by $`D_i\ll M_i`$ (Step 10b). Item 5 for a level that is degenerate at some $`M_i`$ in that range is not derived.
- The results refer to $`C_{\rm bod}`$ under the assumption $`\langle\chi\vert X\vert\chi\rangle=0`$. Without it they hold at leading order in $`\kappa`$ only; the uniform gradient $`\kappa\langle X\rangle(\hat x_1+\hat x_2)`$ is a position-dependent term and is not treated (out of scope).
- $`E_b(P)`$ is well defined only as a total cost of the given $`C`$. Whether the zero of the total cost has any content (a constant in $`C`$ changes no reading) is not a question of this package.

## Code

`code/v2/check_bound_pair.py` (role: check; outputs `code/v2/output/check_bound_pair.txt`, a log, and `code/v2/output/check_bound_pair.json`, all numbers). Part 1 is the check of v1, unchanged; its log agrees line by line with `code/v1/output/check_bound_pair.txt`. Part 2 checks what is new in v2. The script builds $`H(P)`$ of (11.1) with $`\eta=\frac12`$ on $`r=-L,\dots,L`$ with open ends and diagonalizes it: densely, once per set and $`P`$ (all eigenvectors, needed for (11.9)), and with a banded shift-and-invert solver for the finite differences and the doubled range. The bound level is the eigenvector of largest weight on $`(r=0,\lvert11\rangle)`$. Derivatives of $`E_b`$ are five-point differences (step $`0.01`$ in $`P`$, relative step $`10^{-3}`$ in $`M_i`$, $`\tau_i`$, $`\theta`$). Nothing in the derivation rests on the code, except the one statement of Step 5a that is marked there.

**Part 1 (the check of v1).**

- **Range of $`r`$ and convergence.** $`L=120`$ ($`964`$ components). Convergence was checked in two ways: $`E_b`$ at $`L=240`$ differs by less than $`10^{-13}`$, and the weight of $`\psi_P`$ at $`\lvert r\rvert>60`$ is at most $`5\times10^{-8}`$ (set D) and below $`10^{-19}`$ otherwise. $`E_b`$ at $`\eta=0,0.3,1`$ and from the two solvers agrees to $`10^{-13}`$.
- **Parameter sets** ($`M_1,M_2;\ \tau_1,\tau_2;\ w_{11}`$; the other three $`w_{s_1s_2}`$ are non-zero and of the same order), each at $`P\in\{0,\pm0.15,\pm0.30\}`$: A $`(1,1;\ 0.1,0.1;\ -0.004)`$, equal data; B $`(1,1.7;\ 0.2,0.12;\ -0.01)`$; C $`(1,0.8;\ 0.1,0.15;\ +0.02)`$, level above the band; D $`(1.3,1;\ 0.15,0.2;\ -0.004)`$, wide; E $`(1,1.3;\ 1,0.8;\ -0.6)`$, $`\tau_i/M_i`$ of order one. In all sets the level is outside the bands and has $`\langle\Xi\rangle_P=+1`$ (`Gamma` in Part 1 of the output files; in Part 2 the keys `Gamma_...` are the ratios $`\Gamma_i`$).
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

**Part 2 (new in v2).**

- **I3, clock of a part: (11.19), (11.25), (11.26).** For each of the $`N_i`$ levels $`M_i=m_i+d^{(i)}_k`$ the matrix $`H(0)`$ is diagonalized, the eigenvector of the level $`0`$ is evolved on every level, and the exact statistics $`q_i(a;\lambda)`$ are formed (total label $`P=0`$ sharp, no records). They are compared with $`P_{N_i}(a;\Gamma\lambda/\lambda_{0,i})`$ at $`\lambda/\lambda_{0,i}=0.25,0.5,\dots,2N_i`$; the deviation is the largest $`\lvert q_i-P_{N_i}\rvert`$ over $`a`$ and $`\lambda`$. $`\Gamma_i`$ is $`\langle\sigma^{(i)}_3\rangle_0`$ at $`\bar M_i`$, $`\Gamma^{(0)}_i`$ the same at $`m_i`$ (the rate of v1), and (11.25) uses the sum over the rest of the spectrum.

| set, part, $`N_i`$ | $`D_i`$ | $`D_i/g_0`$ | $`\Gamma^{(0)}_i`$ | $`\Gamma_i`$ | (11.25) | deviation with $`\Gamma_i`$ | deviation with $`\Gamma^{(0)}_i`$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E, 1, 4 | 0.06 | 0.21 | 0.856470 | 0.862190 | 0.862334 | $`9.5\times10^{-4}`$ | $`7.1\times10^{-2}`$ |
| E, 1, 4 | 0.03 | 0.10 | 0.856470 | 0.859366 | 0.859402 | $`2.5\times10^{-4}`$ | $`3.6\times10^{-2}`$ |
| E, 1, 4 | 0.015 | 0.05 | 0.856470 | 0.857927 | 0.857936 | $`6.1\times10^{-5}`$ | $`1.8\times10^{-2}`$ |
| B, 1, 4 | 0.10 | 27.9 | 0.9977124 | 0.9978094 | 0.9978119 | $`4.7\times10^{-4}`$ | $`1.4\times10^{-3}`$ |
| B, 1, 4 | 0.05 | 13.9 | 0.9977124 | 0.9977615 | 0.9977621 | $`1.3\times10^{-4}`$ | $`5.9\times10^{-4}`$ |
| B, 1, 4 | 0.025 | 7.0 | 0.9977124 | 0.9977371 | 0.9977373 | $`3.3\times10^{-5}`$ | $`3.0\times10^{-4}`$ |
| B, 2, 5 | 0.10 | 27.9 | 0.9997133 | 0.9997276 | 0.9997282 | $`7.3\times10^{-6}`$ | $`2.2\times10^{-4}`$ |
| B, 2, 5 | 0.05 | 13.9 | 0.9997133 | 0.9997206 | 0.9997208 | $`1.9\times10^{-6}`$ | $`1.1\times10^{-4}`$ |
| B, 2, 5 | 0.025 | 7.0 | 0.9997133 | 0.9997170 | 0.9997170 | $`4.9\times10^{-7}`$ | $`5.7\times10^{-5}`$ |

  Each halving of the spread at fixed $`\lambda/\lambda_{0,i}`$ divides the deviation with $`\Gamma_i`$ by $`3.6`$ to $`4.1`$ (second order) and the deviation with $`\Gamma^{(0)}_i`$ by $`1.9`$ to $`2.4`$ (first order). A least-squares fit of the rate gives $`0.862146`$ (E, $`D_i=0.06`$) and $`0.9977620`$ (B, part 1, $`D_i=0.05`$). In set B the spread is far above $`g_0=0.0036`$ and the remainder is small all the same, as stated in Step 10(b) with $`D_i/M_i`$. In $`\mathsf R`$ (set B): $`\partial^2_{M_i}E_b(0)`$ is $`1.990\times10^{-3}`$ against $`1.996\times10^{-3}`$ from (11.26) (part 1) and $`2.976\times10^{-4}`$ against $`2.952\times10^{-4}`$ (part 2); (11.20) at $`\bar M_1`$ gives $`0.9978101`$ against $`0.9978094`$ ($`D_1=0.10`$).
- **I4, order of $`w_{22}`$** (set B scaled as above, $`\epsilon'=2,1,\frac12,\frac14`$): $`E_b`$ with $`w_{22}`$ minus $`E_b`$ with $`w_{22}=0`$ is $`2.9\times10^{-7}`$, $`4.4\times10^{-9}`$, $`6.9\times10^{-11}`$, $`1.1\times10^{-12}`$. Each halving divides it by $`64.5`$, $`64.1`$, $`64.2`$ (order $`\epsilon^6`$) and the weight $`\lvert\langle22\vert\psi_0(0)\rangle\rvert^2`$ by $`16.1`$, $`16.0`$, $`16.0`$ (order $`\epsilon^4`$); the difference agrees with $`w_{22}\lvert\langle22\vert\psi_0(0)\rangle\rvert^2`$ to four digits or better for $`\epsilon'\ge\frac12`$, and to two digits at $`\epsilon'=\frac14`$, where it is near the rounding error.
- **I5, $`j(P)=0`$** (set A, $`a_1=a_2`$, at $`P=\frac\pi2`$, $`\epsilon'=1,\frac12,\frac14`$): $`E_b-(M_1+M_2+a+w_{11})`$ is $`6.2\times10^{-7}`$, $`3.9\times10^{-8}`$, $`2.4\times10^{-9}`$ (ratios $`16.0`$); one minus the weight on $`(r=0,\lvert11\rangle)`$ is $`2.5\times10^{-3}`$, $`6.2\times10^{-4}`$, $`1.6\times10^{-4}`$ (ratios $`4.0`$, the $`O(\epsilon)`$ part of the eigenvector); the weight of $`\lvert11\rangle`$ at $`r\neq0`$ is $`3\times10^{-7}`$ at $`\epsilon'=1`$.
- **I2, twofold levels: (11.23), (11.24)** (set X: $`M=(1,0.7)`$, $`\tau=(0.5,0.35)`$, $`E_0=1`$, the on-site binding $`W_0=-G(E_0,P_0)^{-1}`$ on the span of $`\lvert11\rangle`$, $`\lvert22\rangle`$, which is not diagonal, with $`w_{12}=0.15`$, $`w_{21}=-0.10`$; at $`P_0=0.3`$ and at $`P_0=0`$). The two eigenvalues at $`E_0`$ differ by less than $`4\times10^{-15}`$ and are $`0.54`$ away from the next one.
  - (11.23): the eigenvalues of $`\Pi_b(\partial_\xi H)\Pi_b`$ against the slopes of the two branches (five-point differences, the branches followed by their overlap with the branch vectors): below $`10^{-11}`$ for $`M_i`$, $`\tau_i`$, $`\theta`$ and $`3\times10^{-10}`$ for $`P`$.
  - (11.24) against the second differences of the branches: below $`5\times10^{-10}`$. At $`P_0=0`$ both first derivatives in $`P`$ vanish, the branch vectors come from the second-order matrix, and $`E''=-0.1063`$ and $`+0.1929`$.
  - (11.9) with $`Q_P`$: at $`P_0=0.3`$ the term of the other vector of the level is $`6.5\times10^{-4}`$ divided by $`2\times10^{-15}`$.
  - Every eigenvector (five random vectors of the level): the residual of (11.6) is $`2\times10^{-15}`$, $`\langle V_1\rangle-\langle V_2\rangle`$ is $`10^{-16}`$, and $`\lVert\Pi_b(V_1-V_2)\Pi_b\rVert`$ is $`2\times10^{-16}`$.
  - The six matrices do not commute: at $`P_0=0.3`$ the first branch vector of $`M_1`$ has the squared overlap $`0.28`$ with that of $`\tau_1`$ and $`0.51`$ with that of $`P`$. In the branch vectors of $`M_1`$, $`\langle U\rangle`$ is $`+2.0135`$ and $`-0.7226`$, against the slopes $`+2.0170`$ and $`-0.7261`$ of the branches of $`\theta`$.
- **I1, the operator (11.21)** (a small system given in the places: two bodies with a branch label on an open chain of four positions, a medium with three places, a random $`X`$ and $`\chi`$, $`\lambda=3`$). Listing B lists $`h\,\sigma^{(1)}_3`$, a constant and a part of the motion term of $`b_2`$ in the record terms. $`C_{\rm bod}`$ of the two listings agrees to $`10^{-15}`$, while the listed pair term of B differs from it by $`2.6`$ in norm. The view of the two bodies against the evolution by $`C_{\rm bod}`$: $`4.1\times10^{-2}`$, $`1.05\times10^{-2}`$, $`2.6\times10^{-3}`$ for $`\kappa=0.04,0.02,0.01`$ (ratios $`3.9`$, $`4.0`$: second order). With a medium that is not centred, $`C_{\rm bod}`$ minus the listed $`C_{\rm pair}`$ is the gradient of (11.21) to $`10^{-15}`$, and the view against the evolution by the listed $`C_{\rm pair}`$ is $`0.153`$, $`0.074`$, $`0.037`$ (ratios $`2.05`$, $`2.01`$: first order).

No check failed and no step of the derivation was changed after a check.

## Methods used

- Fibre decomposition of a shift-invariant two-body contract (total plane-wave label)
- Weyl's theorem on the essential spectrum
- Hellmann–Feynman theorem; second-order perturbation theory; Euler's relation for homogeneous functions
- Rellich's theorem; degenerate perturbation theory to second order (reduced resolvent)
- Partial expectation value of the contract in the start of the medium; unique split into single-object terms and a finite-range pair term
- Resolvent (Green function) equation for a rank-four on-site change
- Degenerate perturbation theory (Schrieffer–Wolff) and the one-defect chain
- Commutator identity for the relative coordinate in a bound state
- Taylor expansion of the level around the mean clock level; cancellation of an even phase in the reading statistics
- Numerical diagonalization, finite differences (check)
