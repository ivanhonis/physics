# Question: 13-pair-fall

- **Subproject:** 05-ilang-free-fall
- **Package:** 13-pair-fall
- **Equation tags:** (13.k)
- **Created:** 2026-10-11

## Goal

Determine how a bound pair of two bodies of different types falls in a sharp and stationary field that acts on each part through its own pair term with the field: the first-order motion of the two parts from a bound level, the drift acceleration of the pair and the quantities that enter it, its dependence on the binding and on the clock levels of the parts, its comparison with the falls of the free parts, and its relation to the rates of the clocks of the parts. This is criterion 9.

**Setting.**
- **Objects.** Two bodies $`b_1`$, $`b_2`$, a recording medium $`c`$ and a field $`f`$, of four pairwise different types, one instance each.
- **Bodies.** For $`i=1,2`$ the body $`b_i`$ has the places $`(x_i,s_i,a_i)`$ of Model D and the Model D contract $`C^{\rm D}_i=A_i+B_i`$ with its own data: $`\tau_i>0`$, $`m_i>0`$, a clock with $`N_i\ge2`$ places, the tick parameter $`\lambda_{0,i}`$ and the clock operator $`D_i`$; $`d^{(i)}_k:=\frac{2\pi k}{N_i\lambda_{0,i}}`$ and $`M^{(i)}_k:=m_i+d^{(i)}_k`$. $`A_i`$ is the motion term and $`B_i=\sum_x\lvert x\rangle\langle x\rvert\otimes G_i`$ the rest and clock term of $`b_i`$, with $`G_i:=\sigma^{(i)}_3\otimes(m_i\mathbb 1_{N_i}+D_i)`$ on the branch label and the clock label of $`b_i`$. Both position labels run over the same chain $`\lvert x_i\rvert\le L`$, with $`x_i\in\mathbb Z`$ as the limit of long chains (A1). $`\hat x_i:=\sum_xx\,\lvert x\rangle\langle x\rvert`$ on the position label of $`b_i`$.
- **Records and common points.** One medium records both bodies through the same operator and with the same strength: $`C_{\rm rec}:=\kappa\,\hat x_1\otimes X+\kappa\,\hat x_2\otimes X`$ with $`\kappa>0`$ and $`X`$ self-adjoint on $`\mathcal H_c`$; the medium starts in $`\chi`$ with $`\sigma_X>0`$, and $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$. By (17.15) the position $`x`$ of either body has the record vector $`\kappa\,x\,e`$, and $`d_0:=\kappa\sigma_X`$ is the distance of neighbouring positions. By (16.11) the map $`x\mapsto x+s`$ from the positions of $`b_1`$ to those of $`b_2`$ is a correspondence for every integer $`s`$; the **label separation** is $`r:=x_1-x_2`$, and the choice $`s=0`$ is a convention of the labels.
- **Binding (the class $`\mathcal W`$).** One pair term between $`b_1`$ and $`b_2`$ (A5),
  ```math
  U=\sum_{x_1,x_2}\lvert x_1\rangle\langle x_1\rvert\otimes\lvert x_2\rangle\langle x_2\rvert\otimes W(x_1-x_2),
  ```
  where, for every integer $`r`$, $`W(r)`$ is a self-adjoint operator on the two branch labels, acting as the identity on the two clock labels, and $`W(r)=0`$ for $`\lvert r\rvert>R`$ with a finite range $`R\ge0`$. A **diagonal on-site binding** has $`W(r)=\delta_{r,0}\sum_{s_1,s_2}w_{s_1s_2}\,\lvert s_1s_2\rangle\langle s_1s_2\rvert`$ with four real numbers $`w_{s_1s_2}`$, $`s_i\in\{1,2\}`$. $`C_{\rm pair}:=C^{\rm D}_1+C^{\rm D}_2+U`$.
- **Field.** The field is coupled to each body by a lapse-type pair term on its rest and clock term:
  ```math
  C=C_{\rm pair}+C_{\rm rec}+\sum_{i=1,2}\theta_i\,\hat x_i\otimes G_i\otimes\Phi+C_f ,
  ```
  with real numbers $`\theta_1`$, $`\theta_2`$ and self-adjoint operators $`\Phi`$, $`C_f`$ on a finite-dimensional $`\mathcal H_f`$. The field starts in a state $`\varphi`$ with $`\Phi\varphi=\gamma\varphi`$ and $`C_f\varphi=e_f\varphi`$ (sharp and stationary; an assumption, A11). The **gradient of the part $`i`$** is $`g_i:=\gamma\theta_i`$, with $`\lvert g_i\rvert(L+1)<1`$. No term of $`C`$ contains the two bodies and the field together: by A5 a contract term holds between two objects, so in this class the binding carries no factor of the field. The **common gradient** is the case $`g_1=g_2=:g`$; the case $`g_1\neq g_2`$ is the control. The form of the coupling, the state of the field and the binding are assumptions of this package (M8).
- **The operator on the two bodies.** $`C_{\rm bod}`$ is the partial expectation of $`C-e_f`$ in $`\chi\otimes\varphi`$ over $`\mathcal H_c\otimes\mathcal H_f`$, an operator on $`\mathcal H_{b_1}\otimes\mathcal H_{b_2}`$ that is fixed by $`C`$ and the starts of the medium and of the field up to an additive constant (as (11.21), with the field included; the listed $`C_f`$, and with it $`e_f`$, is fixed only up to a constant). Every item refers to $`C_{\rm bod}`$, not to a listed term. In the listing above its part that is linear in the position labels consists of the terms with $`g_1`$, $`g_2`$ and $`\kappa\langle X\rangle`$; these three numbers are **the gradients**. Convention for the records, as in 04-branch-fall: at leading order in $`\kappa`$ the bodies evolve by $`C_{\rm bod}`$, and its term with $`\kappa\langle X\rangle`$ is one of the first-order gradients and is kept; $`\langle X\rangle=0`$ is a condition, to be named with every statement that needs it.
- **Levels, fibres and bound level.** The clock levels of the two bodies are conserved. Fix levels $`k_1`$, $`k_2`$ and write $`M_i:=M^{(i)}_{k_i}`$. With all gradients set to zero $`C_{\rm bod}`$ is $`C_{\rm pair}`$, with the fibre contract $`H(P)`$ of (11.1), $`P\in(-\pi,\pi]`$ the total plane-wave label and $`\eta`$ the phase convention. In this package a **bound level** is a function $`E_b(P)`$ on an open interval $`\mathcal P_0\ni0`$ such that, for every $`P\in\mathcal P_0`$, $`E_b(P)`$ is a simple eigenvalue of $`H(P)`$ outside the bands (11.2), with the normalized eigenvector $`\psi_P`$, chosen analytic in $`P`$; $`\langle O\rangle_P:=\langle\psi_P\vert O\vert\psi_P\rangle`$, and a prime is $`\partial_P`$.
- **Packets.** For $`g`$ of the class $`\mathcal G(\mathcal P_0)`$ of (11.8) (continuously differentiable with compact support in $`\mathcal P_0`$, $`\int\lvert g\rvert^2=1`$) the start of the two bodies is $`\Phi_g=\int\mathrm dP\,g(P)\,\lvert P;\psi_P\rangle`$ on the levels $`k_1`$, $`k_2`$; $`P_0:=\int P\,\lvert g\rvert^2`$ and $`\delta P^2:=\int(P-P_0)^2\lvert g\rvert^2`$. The packet is **concentrated at $`P_0`$** with the spread $`\delta P`$. A **sharp-total-label limit** is a limit along a sequence of such packets with $`\delta P\to0`$ at fixed $`P_0`$; the package names the class of sequences for which each limit is taken.
- **Quantities and orders.** $`\bar m_i(\lambda)`$ is the mean position label of the part $`i`$ (the expectation of $`\hat x_i`$ in the view of the two bodies). "First order in the gradients" means first order jointly in $`g_1`$, $`g_2`$ and $`\kappa\langle X\rangle`$, at fixed $`\lambda`$, fixed start and fixed chain, followed by the limit of a long chain. The **drift acceleration of the part $`i`$ at $`P_0`$** is the first-order acceleration of $`\bar m_i`$, averaged over a window $`[\lambda_1,\lambda_1+\Lambda]`$ with $`\Lambda\to\infty`$, followed by a sharp-total-label limit at $`P_0`$; this is the definition of (4.10), (4.11) for one body, taken over to the parts of the pair.
- **Regime $`\mathsf R`$ (items 3 and 4).** As in 11-bound-pair: $`\tau_i=\epsilon\,\hat\tau_i`$ and $`w_{s_1s_2}=\epsilon^2\,\hat w_{s_1s_2}`$ with fixed $`\hat\tau_i>0`$, $`\hat w_{s_1s_2}`$, $`M_i`$, and $`\epsilon\to0`$. With $`a_i:=\tau_i^2/(4M_i)`$, $`a:=a_1+a_2`$ and $`u:=\lvert w_{11}\rvert/a`$: the regime makes $`\tau_i/M_i`$ and $`\lvert w_{s_1s_2}\rvert/M_i`$ small; it does not make $`u`$ small or large. Results are asked at fixed hatted data, hence at a fixed $`u\in(0,\infty)`$. A wide-pair form ($`u\to0`$) or a tight-pair form ($`u\to\infty`$) is an ordered limit: first $`\epsilon\to0`$ at fixed $`u`$, then the limit in $`u`$ of the leading coefficient. The first order in the gradients is taken first, at fixed data; its coefficients are then evaluated at leading order in $`\mathsf R`$.

1. **Reduced contract and well-defined data.**
   - (a) Determine the generator by which the two bodies and the medium evolve when the field starts in $`\varphi`$ (the form that (8.10) takes when the binding is present), and state whether it is the contract of an admissible description of $`b_1`$, $`b_2`$ and $`c`$ (A5). State which kind of term would be needed for the binding to carry a factor of the field.
   - (b) Determine $`C_{\rm bod}`$. On the levels $`k_1`$, $`k_2`$ write its gradient terms with the centre label $`\hat X_\eta:=\eta\,\hat x_1+(1-\eta)\,\hat x_2`$ of the convention $`\eta`$ of (11.1) and the label separation $`\hat r`$. State which of the following are fixed by $`C_{\rm bod}`$ and hence well defined (M6) under every replacement of the listed terms that leaves $`C`$ unchanged: $`g_1`$; $`g_2`$; $`\kappa\langle X\rangle`$; the operator that multiplies the centre label; the operator that multiplies $`\hat r`$. State which of them depend on the convention $`\eta`$. (The split of $`g_i`$ into $`\gamma`$ and $`\theta_i`$, and into a part of the field and a part of a body's own contract, is not asked.)

2. **First-order motion from a bound level (exact relations).** For every binding of the class $`\mathcal W`$, all data of the two bodies, every bound level in the sense of the setting, every packet of the class $`\mathcal G(\mathcal P_0)`$, and all values of the three gradients:
   - (a) Determine the first-order velocities of $`\bar m_1`$ and $`\bar m_2`$ as functions of $`\lambda`$: the part that grows linearly in $`\lambda`$, with its coefficient as an average over $`\lvert g\rvert^2`$ of a function of $`P`$ built from $`E_b`$, its derivatives and expectation values $`\langle\cdot\rangle_P`$; and the rest, with a bound or an order estimate and the conditions under which it stays bounded for all $`\lambda\ge0`$. State whether the two parts have the same coefficient.
   - (b) Determine the first-order change of the mean label separation $`\bar m_1-\bar m_2`$: whether it grows with $`\lambda`$, stays bounded or vanishes, for the common gradient and for $`g_1\neq g_2`$.
   - (c) Determine the drift acceleration of the two parts at $`P_0`$, with the class of sequences for which the limits of its definition exist (the window average first, then the sharp total label). State whether the two limits commute on that class, with what is shown for the other order; the evaluation of the other order is not asked. (Amended on 2026-10-11, after the first version: the first form of this item asked for both orders, each with the quantity it defines.) (Clarified on 2026-10-11, after the first external round: a determination is asked for the members of the class of item 2, the bound levels of items 3 and 4 at $`P_0=0`$ included: for which members the other order exists on the class of sequences and agrees with the defining order, and for which it does not. A sufficient condition for one of the two cases does not answer the item for the members it leaves open; a member that stays open is named with the reason.) (Restricted on 2026-10-11, after the second external round; this replaces the clarification before it. The determination, exists and agrees or does not exist, is asked for two groups: the members with $`g_1=g_2=0`$, and the bound levels of items 3 and 4 at $`P_0=0`$. For the other members of the class of item 2 three things are asked: the necessary and sufficient condition under which the limit of the sharp total label exists at a fixed window for every sequence of the class; a necessary condition and a sufficient condition for the existence of the other order, each named as necessary or as sufficient; and whether a member that satisfies the necessary condition without the sufficient one is shown to exist, is excluded, or neither. A classification of the members between the two conditions is not asked: the drift acceleration is defined by the order named first, and nothing in this package uses the other order.) Write it as a sum in which each of $`g_1`$, $`g_2`$ and $`\kappa\langle X\rangle`$ is multiplied by a coefficient, and determine each coefficient through $`E_b`$ and the expectation values of (11.5), (11.7) and (11.9). State whether $`E_b''(P_0)`$, the inverse of the curvature inertia of (11.16) at $`P_0=0`$, is the only property of the level that multiplies all three gradients, or what else enters.
   - (d) For the common gradient, state the relation between the coefficient of $`g`$ and the terms of the scaling relation (11.6).

3. **Diagonal on-site binding in the regime $`\mathsf R`$.** For the bound level (11.12) with $`\hat w_{11}\neq0`$, both signs of $`w_{11}`$, packets concentrated at $`P_0=0`$ (state why such a pair is at rest), at leading order in $`\mathsf R`$ and at a fixed $`u`$:
   - (a) Evaluate the drift acceleration of the pair from rest for general $`g_1`$, $`g_2`$ and $`\langle X\rangle`$, in closed form, with its remainder. Give its wide-pair and tight-pair forms as ordered limits.
   - (b) By (4.16) with the gradients (8.11), the free part $`i`$ on its level $`k_i`$, in the upper branch and from rest, has in the same field the drift acceleration $`a^{(i)}:=-\tau_i^2\,g_i-\tau_i^2\,\kappa\langle X\rangle/M_i`$ in position labels. For $`\langle X\rangle=0`$ determine the ratios of the drift acceleration of the pair to $`a^{(1)}`$ and to $`a^{(2)}`$ in three cases: the common gradient with $`\tau_1=\tau_2`$ (the free parts then have equal drift accelerations); the common gradient with $`\tau_1\neq\tau_2`$; and $`g_1\neq g_2`$. For each case state whether the pair falls like its parts exactly, to a stated order in $`\epsilon`$, in an ordered limit of $`u`$, or not at all, and give the leading difference.
   - (c) Determine whether the drift acceleration of the pair from rest is the same for all pairs of clock levels $`(k_1,k_2)`$: the necessary and sufficient condition at this order, for $`\langle X\rangle=0`$ and for $`\langle X\rangle\neq0`$, and the leading dependence on $`M_1`$, $`M_2`$ where it is not. Compare with the free parts, for which (4.16) gives a drift acceleration from rest that is the same for all levels if and only if $`\langle X\rangle=0`$.
   - (d) Determine the effect of $`\langle X\rangle\neq0`$ on the drift acceleration of the pair, compared with its effect on the free parts.

4. **Fall and the clocks of the parts.** For the bound levels of item 3 and $`\langle X\rangle=0`$:
   - (a) At a position label $`x_0`$ the rest and clock term of the part $`i`$ carries the factor $`1+g_i\,x_0`$. Determine the rate of the clock of the part $`i`$ (the reading of its clock label, as in (11.19)) for a pair at rest whose packet is concentrated in position around the label $`x_0`$, at zeroth order in the gradients (with the data of the two parts at $`x_0`$) and at leading order in $`\mathsf R`$; state the conditions on the packet and the range of $`\lambda`$. Determine its relative change per label at $`x_0=0`$, $`\varrho_i:=\bigl[\text{rate at }x_0=1\text{ minus rate at }x_0=0\bigr]/\text{rate at }x_0=0`$, to first order in the gradients.
   - (b) For $`i=1,2`$ determine the number $`\mathsf w_i^2:=-(\text{drift acceleration of the pair from rest})/\varrho_i`$, where $`\varrho_i\neq0`$. State whether it equals $`\tau_i^2`$ (the square of the bound (5.11) of the part $`i`$ in position labels per unit of $`\lambda`$), whether it is the same for $`i=1`$ and $`i=2`$, and whether it contains data of the pair (the binding, the clock levels). For the free part $`i`$ the relation (4.24) reads $`a^{(i)}=-\tau_i^2\,g_i`$ with the relative change $`g_i`$ of its clock rate.
   - (c) For the case in which the free parts fall alike and each obeys (4.24) with one speed (common gradient, $`\tau_1=\tau_2=\tau`$): state whether the pair obeys the relation of the form (4.24) with the speed $`\tau d_0`$ and the clock of a part, exactly, to a stated order in $`\epsilon`$, in an ordered limit of $`u`$, or not at all, and give the leading deviation.

5. **Summary.** State in a table, for each of: the drift acceleration from rest; its independence of the clock levels; the number that ties it to the relative change of a clock rate: the result for a free part, the result for the bound pair, and the condition under which the pair agrees with its parts, with the tags of the results used.

## Inputs

From 11-bound-pair@v3 (this subproject). Setting there: the two bodies, the medium, the binding and $`C_{\rm pair}`$ as under "Goal", with no field and under the assumption $`\langle\chi\vert X\vert\chi\rangle=0`$. Notation there:
- on the levels $`k_1`$, $`k_2`$ a vector with the label $`P`$ of the joint shift is $`\Psi(x_1,x_2)=e^{iP(\eta x_1+(1-\eta)x_2)}\psi(x_1-x_2)`$ with $`\psi(r)\in\mathbb C^2\otimes\mathbb C^2`$ and a real number $`\eta`$ (the phase convention; the spectrum and every $`\langle O\rangle_P`$ are independent of it); $`(S\psi)(r):=\psi(r-1)`$; $`A_i`$, $`U`$, $`\sigma^{(i)}_3`$ also denote the fibres of these operators;
- $`V_i:=i[C_{\rm pair},\hat x_i]`$, with the fibres $`V_1=-\frac{\tau_1}2\sigma^{(1)}_1(e^{i\eta P}S^\dagger+e^{-i\eta P}S)`$ and $`V_2=-\frac{\tau_2}2\sigma^{(2)}_1(e^{i(1-\eta)P}S+e^{-i(1-\eta)P}S^\dagger)`$; $`V_\eta:=\eta V_1+(1-\eta)V_2=\partial_PH`$; $`Q_P:=\mathbb 1-\lvert\psi_P\rangle\langle\psi_P\rvert`$; on the fibres $`\eta\hat x_1+(1-\eta)\hat x_2`$ acts as $`i\partial_P`$ and $`\hat x_1-\hat x_2`$ as $`\hat r`$;
- $`\omega_i(p):=\sqrt{M_i^2+\tau_i^2\sin^2p}`$, $`\Omega_i:=\sqrt{M_i^2+\tau_i^2}`$, $`p_1+p_2=P`$; $`\mathfrak m_i:=M_i/\tau_i^2`$ and, for a bound level with $`E_b''(0)\neq0`$, the curvature inertia $`\mathfrak m_b:=1/E_b''(0)`$;
- for the diagonal on-site binding in the regime $`\mathsf R`$: $`a_i:=\tau_i^2/(4M_i)=1/(4\mathfrak m_i)`$, $`a:=a_1+a_2`$, $`j(P):=\sqrt{a_1^2+a_2^2+2a_1a_2\cos2P}`$, $`J(P):=a_1e^{2i\eta P}+a_2e^{-2i(1-\eta)P}=j(P)e^{i\alpha(P)}`$, $`w:=w_{11}`$, $`\varsigma:=\mathrm{sgn}w`$, $`u:=\lvert w\rvert/a`$, $`\Lambda:=1+\varsigma/\sqrt{1+u^2}`$;
- "leading order in $`\mathsf R`$" is taken at fixed hatted data; a wide-pair or tight-pair form is an ordered limit (first $`\epsilon\to0`$ at fixed $`u`$).

Eq. (11.1) of 11-bound-pair, the fibre contract:

```math
H(P)=\underbrace{\tfrac{i\tau_1}{2}\,\sigma^{(1)}_1\bigl(e^{i\eta P}S^{\dagger}-e^{-i\eta P}S\bigr)}_{A_1}+\underbrace{\tfrac{i\tau_2}{2}\,\sigma^{(2)}_1\bigl(e^{i(1-\eta)P}S-e^{-i(1-\eta)P}S^{\dagger}\bigr)}_{A_2}+M_1\sigma^{(1)}_3+M_2\sigma^{(2)}_3+\underbrace{W(\hat r)}_{U}.
```

Eq. (11.2) of 11-bound-pair, the two-body bands (the essential spectrum of $`H(P)`$, the same for every $`W\in\mathcal W`$), with $`f(v):=\sqrt{M_1^2+\tau_1^2v}-\sqrt{M_2^2+\tau_2^2v}`$ on $`v\in[0,1]`$:

```math
\mathcal B_{\sigma_1\sigma_2}(P)=\bigl\{\sigma_1\omega_1(p_1)+\sigma_2\omega_2(P-p_1)\bigr\}_{p_1\in(-\pi,\pi]},\qquad \mathcal B_{++}(0)=[\,M_1+M_2,\ \Omega_1+\Omega_2\,],\quad \mathcal B_{+-}(0)=[\,\min f,\ \max f\,],\quad \mathcal B_{--}=-\mathcal B_{++},\quad \mathcal B_{-+}=-\mathcal B_{+-}.
```

Eq. (11.21) of 11-bound-pair, the operator on the two bodies, defined by the total contract and the start of the medium; the view of the two bodies evolves by it up to second order in the record term:

```math
C_{\rm bod}:=\langle\chi\vert C\vert\chi\rangle_c=\mathrm{Tr}_c\bigl[C\,(\mathbb 1\otimes\lvert\chi\rangle\langle\chi\rvert)\bigr]=C^{\rm D}_1+C^{\rm D}_2+U+\kappa\,\langle\chi\vert X\vert\chi\rangle\,(\hat x_1+\hat x_2).
```

Eq. (11.22) of 11-bound-pair, the distance of the bound level from the band edge:

```math
E_{\rm bind}(P):=E_b(P)-e_{++}(0),\qquad e_{++}(P):=\min\mathcal B_{++}(P),\qquad e_{++}(0)=M_1+M_2\ \ (\text{for the } C \text{ of the question}),\qquad E_{\rm bind}:=E_{\rm bind}(0).
```

Eq. (11.5) of 11-bound-pair, for every $`W\in\mathcal W`$, every simple bound level outside the bands and every $`P`$ of its interval, with $`\theta`$ a common factor of the binding ($`W\to\theta W`$; this $`\theta`$ is not the $`\theta_i`$ of this question):

```math
\frac{\partial E_b}{\partial M_i}=\langle\sigma^{(i)}_3\rangle_P,\qquad
\tau_i\frac{\partial E_b}{\partial\tau_i}=\langle A_i\rangle_P,\qquad
\frac{\partial E_b}{\partial\theta}\Big|_{\theta=1}=\langle U\rangle_P\qquad(i=1,2).
```

Eq. (11.6) of 11-bound-pair, the scaling relation, same class:

```math
E_b(P)=M_1\langle\sigma^{(1)}_3\rangle_P+M_2\langle\sigma^{(2)}_3\rangle_P+\langle A_1\rangle_P+\langle A_2\rangle_P+\langle U\rangle_P .
```

Eq. (11.7) of 11-bound-pair, same class:

```math
E_b'(P)=\langle V_1\rangle_P=\langle V_2\rangle_P .
```

Eq. (11.8) of 11-bound-pair, for $`g\in\mathcal G(\mathcal P_0)`$ and every $`\lambda`$, under $`C_{\rm pair}`$ (no gradients); the mean position labels of the two bodies exist for $`g`$ of this class, and $`I_g`$ is the smallest closed interval that contains the support of $`g`$:

```math
\frac{\mathrm d\bar m_1}{\mathrm d\lambda}=\frac{\mathrm d\bar m_2}{\mathrm d\lambda}=\int\mathrm dP\,\lvert g(P)\rvert^2E_b'(P)=E_b'(P_0)+O(\delta P^2)\qquad\text{for } g\in\mathcal G(\mathcal P_0)\ \text{and every }\lambda,\qquad \bigl\lvert O(\delta P^2)\bigr\rvert\le\tfrac12\max_{I_g}\lvert E_b'''\rvert\;\delta P^2 .
```

Eq. (11.9) of 11-bound-pair, for a simple bound level; $`\mu`$ is the spectral measure of $`H(P)`$ in the vector $`V_\eta\psi_P`$, and each of the two parts depends on the convention $`\eta`$ while their sum does not:

```math
E_b''(P)=-\eta^2\langle A_1\rangle_P-(1-\eta)^2\langle A_2\rangle_P-2\,\mathcal S_\eta(P),\qquad
\mathcal S_\eta(P):=\bigl\langle V_\eta\psi_P\big\vert Q_P\bigl(H(P)-E_b\bigr)^{-1}Q_P\big\vert V_\eta\psi_P\bigr\rangle=\int_{\mathrm{spec}H(P)\setminus\{E_b\}}\frac{\mathrm d\mu(E)}{E-E_b}.
```

Eq. (11.11) of 11-bound-pair, with the statement of its Step 7 from which (11.12) and (11.13) follow, for every diagonal on-site binding in the regime $`\mathsf R`$ (added to the quoted inputs on 2026-10-11, after the first external round). There $`H(P)=H_0+\epsilon H_1+\epsilon^2H_2`$ with $`H_0=M_1\sigma^{(1)}_3+M_2\sigma^{(2)}_3`$, $`\epsilon H_1=A_1+A_2`$, $`\epsilon^2H_2=U`$, and $`\Pi`$ is the projector onto the branches $`\lvert11\rangle`$, all $`r`$, the eigenvalue $`M_1+M_2`$ of $`H_0`$, which is separated from the other three by at least $`2\min(M_1,M_2)`$. "All terms are bounded uniformly in $`r`$, so degenerate perturbation theory applies: the part of $`H(P)`$ with spectrum near $`M_1+M_2`$ is unitarily equivalent, by a unitary that differs from $`\mathbb 1`$ by $`O(\epsilon)`$, to"

```math
H_{\rm eff}(P)=M_1+M_2+\Pi\,U\,\Pi+\Pi\Bigl(\frac{A_1^2}{2M_1}+\frac{A_2^2}{2M_2}\Bigr)\Pi+O(\epsilon^4)\quad\text{in norm}.
```

On the coefficient $`\psi(r)`$ of $`\lvert11\rangle`$:

```math
(H_{\rm eff}\psi)(r)=\bigl(M_1+M_2+a+w\,\delta_{r,0}\bigr)\psi(r)-\tfrac12\bigl[J\,\psi(r+2)+J^{*}\psi(r-2)\bigr],\qquad J(P):=a_1e^{2i\eta P}+a_2e^{-2i(1-\eta)P}=j(P)\,e^{i\alpha(P)} .
```

Eq. (11.12) of 11-bound-pair, for every diagonal on-site binding in the regime $`\mathsf R`$ and every $`P`$: for small $`\epsilon`$ at fixed hatted data, $`H(P)`$ has a bound level at a distance of order $`\epsilon^2`$ from the band $`\mathcal B_{++}(P)`$ if and only if $`\hat w_{11}\neq0`$; it is then exactly one, simple, below the band for $`w_{11}<0`$ and above it for $`w_{11}>0`$, and of the four numbers $`w_{s_1s_2}`$ only $`w_{11}`$ enters it at this order:

```math
E_b(P)=M_1+M_2+a+\varsigma\sqrt{w^2+j(P)^2}+O(\epsilon^4),\qquad j(P)^2=a_1^2+a_2^2+2a_1a_2\cos2P ,
```

Eq. (11.13) of 11-bound-pair, its eigenvector for $`j(P)\neq0`$, up to $`O(\epsilon)`$ (the $`O(\epsilon)`$ part is $`\bigl(\frac{A_1}{2M_1}+\frac{A_2}{2M_2}\bigr)\psi_P`$, on the branches $`\lvert21\rangle`$, $`\lvert12\rangle`$ at odd $`r`$), with $`\rho=-\varsigma\bigl(\sqrt{w^2+j^2}-\lvert w\rvert\bigr)/j`$:

```math
\psi_P(r)=\mathcal N_P\,e^{-i\alpha(P)\,r/2}\,\rho(P)^{\lvert r\rvert/2}\,\lvert11\rangle\ \ (r\ \text{even}),\qquad \psi_P(r)=0\ \ (r\ \text{odd}),\qquad \mathcal N_P^2=\frac{\lvert w\rvert}{\sqrt{w^2+j^2}},\qquad\text{up to } O(\epsilon).
```

Eq. (11.14) of 11-bound-pair, at $`P=0`$, each up to $`O(\epsilon^4)`$ against terms of order $`\epsilon^2`$, at fixed hatted data. It is obtained from (11.5) and (11.12) by differentiation in the data, with the statement of its Step 8: "$`E_b`$ is analytic in the data with a remainder bounded uniformly near real data, so (11.12) can be differentiated and the remainders stay $`O(\epsilon^4)`$." (This sentence was added to the quoted inputs on 2026-10-11, after the first version.)

```math
E_{\rm bind}=a+\varsigma\sqrt{w^2+a^2},\quad E_b''(0)=-\varsigma\frac{4a_1a_2}{\sqrt{w^2+a^2}},\quad \langle\sigma^{(i)}_3\rangle_0=1-\frac{a_i}{M_i}\Lambda,\quad \langle A_i\rangle_0=2a_i\Lambda,\quad \langle U\rangle_0=\varsigma\frac{w^2}{\sqrt{w^2+a^2}},\qquad \Lambda=1+\frac{\varsigma\,a}{\sqrt{w^2+a^2}} .
```

Eq. (11.16) of 11-bound-pair, at leading order in $`\mathsf R`$ (relative remainder $`O(\epsilon^2)`$ at every fixed $`u`$), for both signs of $`w_{11}`$:

```math
\mathfrak m_b=-\varsigma\,(\mathfrak m_1+\mathfrak m_2)\sqrt{1+u^2}=\mathfrak m_1+\mathfrak m_2-4\,\mathfrak m_1\mathfrak m_2\,E_{\rm bind} .
```

Eq. (11.19) of 11-bound-pair, the statistics of a reading of the clock label of the part $`i`$ for a pair in a bound level at $`P=0`$ with no field: the clock label of the part $`i`$ starts in the place $`\lvert0\rangle`$, the other part is on its level, and the positions and branches are in a packet of total labels of mean $`0`$ and spread $`\delta P`$. $`P_N`$ is the reading distribution (5.1), $`\bar M_i:=m_i+\bar d_i`$ with $`\bar d_i:=\frac{\pi(N_i-1)}{N_i\lambda_{0,i}}`$ is the mean rest cost of the part $`i`$, $`D_i:=d^{(i)}_{N_i-1}`$ is here the spread of its levels, $`g_0`$ the distance of the bound level from the rest of the spectrum over the range $`[m_i,m_i+D_i]`$ of $`M_i`$, and $`\delta_i:=D_i/g_0`$; the remainder is small for $`\lambda\ll\lambda_{0,i}/\delta_i`$, and in $`\mathsf R`$ it holds with $`\delta_i`$ replaced by $`D_i/M_i`$:

```math
q_i(a;\lambda)=P_{N_i}\Bigl(a;\Gamma_i\frac{\lambda}{\lambda_{0,i}}\Bigr)+\mathcal R_i,\qquad \Gamma_i=\langle\sigma^{(i)}_3\rangle_0\Big\vert_{M_i=\bar M_i}=\frac{\partial E_b(0)}{\partial M_i}\Big\vert_{M_i=\bar M_i},\qquad \mathcal R_i=O\bigl(\delta_i^2(1+\lambda/\lambda_{0,i})^2\bigr)+O\bigl(\delta P^2(1+\lambda/\lambda_{0,i})\bigr)+O(\kappa).
```

Eq. (11.20) of 11-bound-pair, at leading order in $`\mathsf R`$ (remainder $`O(\epsilon^4)`$, fixed $`u`$), with $`M_i=\bar M_i`$ for the part whose clock is read and $`M_j=M^{(j)}_{k_j}`$ for the other part:

```math
\Gamma_i=1-\frac{\tau_i^2}{4M_i^2}\,\Lambda,\qquad \Lambda=1+\frac{\varsigma}{\sqrt{1+u^2}},\qquad \frac{1-\Gamma_1}{1-\Gamma_2}=\frac{\tau_1^2/M_1^2}{\tau_2^2/M_2^2}.
```

Statements of Step 10 of 11-bound-pair that accompany (11.19) and (11.20), for the same class, in the regime $`\mathsf R`$ (added to the quoted inputs on 2026-10-11, after the first external round). They state how that package reads the statement of its Step 8 that is quoted with (11.14):
- "$`\partial^2_{M_i}E_b(0)=\frac{a_i}{M_i^2}\bigl[2\Lambda+\varsigma\frac{a_i}{a}\frac{u^2}{(1+u^2)^{3/2}}\bigr]`$, from (11.12) and $`\partial_{M_i}a=-a_i/M_i`$."
- "By (11.12), (11.13) and the analyticity used in Step 8, $`E_b-M_1-M_2`$ and $`\psi_0`$ depend on $`M_i`$ on the scale $`M_i`$: $`\partial^n_{M_i}E_b=O(a_i/M_i^{\,n})`$ for $`n\ge2`$ and $`\lVert\partial_{M_i}\psi_0\rVert=O(1/M_i)`$."
- "(11.26) and these bounds are for fixed hatted data, hence a fixed $`u\in(0,\infty)`$; their constants are not bounded here for $`u\to0`$ or $`u\to\infty`$." ((11.26) is the clock ratio $`\Gamma_i`$ to first order in the level spacing; it is not used here.)

From 08-two-types@v5 (this subproject). Setting of its item 5: two Model D bodies of different types with no term between them, one medium with the records $`\kappa_i\,\hat x_i\otimes X`$, and a field $`f`$ coupled to both bodies by $`\sum_iB_i\otimes\Phi`$ with $`B_i:=\theta_i\,\hat x_i\otimes\sigma_3\otimes(m_i\mathbb 1_{N_i}+D_i)`$; the field starts in $`\varphi`$ with $`\Phi\varphi=\gamma\varphi`$ and $`C_f\varphi=e_f\varphi`$; $`P^{(i)}_x:=\lvert x\rangle\langle x\rvert`$ on the position label of $`b_i`$.

Eq. (8.10) of 08-two-types, for every $`\Psi\in\mathcal H_{b_1}\otimes\mathcal H_{b_2}\otimes\mathcal H_c`$:

```math
C\,(\Psi\otimes\varphi)=\bigl((C_{\rm red}+e_f)\Psi\bigr)\otimes\varphi,\qquad C_{\rm red}=\sum_{i=1,2}\Bigl[A_i+\sum_xP^{(i)}_x\otimes(1+\gamma\theta_ix)\,\sigma_3\otimes\bigl(m_i\mathbb 1_{N_i}+D_i\bigr)+\kappa_i\,\hat x_i\otimes X\Bigr],
```

Eq. (8.11) of 08-two-types, the gradients of the effective body contract of the type $`i`$ in the notation of 04-branch-fall below ($`M_{x,k}=m_x+\eta_xd_k`$ with $`m_x=m_i(1+g_{m,i}x)`$, $`\eta_x=1+g_{\eta,i}x`$, so that $`G_k=g_iM^{(i)}_k`$ for $`g_{m,i}=g_{\eta,i}=g_i`$):

```math
g_{m,i}=g_{\eta,i}=\gamma\theta_i,\qquad g_{\zeta,i}=0,\qquad\mathcal F_i=-\kappa_i\langle X\rangle;\qquad\text{class }\mathcal C\iff\lvert\gamma\rvert\,L\,\max(\lvert\theta_1\rvert,\lvert\theta_2\rvert)<1 .
```

From 02-field-object@v2 (this subproject). Setting there: a body $`b`$, a field $`f`$ and a set $`r`$ of further objects (possibly empty), of pairwise different types, $`\mathcal H=\mathcal H_{br}\otimes\mathcal H_f`$ with $`\mathcal H_{br}:=\mathcal H_b\otimes\mathcal H_r`$; $`C_{br}`$ is a sum of pair terms among $`b`$ and the objects of $`r`$, $`C_f`$ is self-adjoint on $`\mathcal H_f`$, and $`B_j`$ (on $`\mathcal H_b`$), $`\Phi_j`$ (on $`\mathcal H_f`$), $`j\in J`$, are finite families of self-adjoint operators; $`B_j`$ also denotes $`B_j\otimes\mathbb 1_r`$. The start is $`\Psi_0=\Psi_{br}\otimes\varphi`$ and $`\lambda\ge0`$; $`V(\lambda)`$ is the view of $`\{b\}\cup r`$. A field state $`\varphi`$ is **sharp** if $`\Phi_j\varphi=n_j\varphi`$ for all $`j`$, with real numbers $`n_j`$. A **schedule** consists of readings with projectors $`\Pi_i\otimes\mathbb 1_f`$ at $`0\le\lambda_1\le\dots\le\lambda_k`$, where $`\Pi_i`$ is diagonal in the joint places of $`b`$ and $`r`$; $`p(r_1,\dots,r_k)`$ is the joint distribution of its outcomes.

Eq. (2.1) of 02-field-object, the contract:

```math
C=C_{br}\otimes\mathbb 1_f+\sum_{j\in J}B_j\otimes\mathbb 1_r\otimes\Phi_j+\mathbb 1_{br}\otimes C_f
```

Eq. (2.3) of 02-field-object, for a field state with $`\Phi_j\varphi=n_j\varphi`$ and $`C_f\varphi=e_f\varphi`$ (sharp and stationary), and every $`\Psi\in\mathcal H_{br}`$:

```math
C\,(\Psi\otimes\varphi)=\bigl((C_{\rm red}+e_f)\Psi\bigr)\otimes\varphi,\qquad C_{\rm red}:=C_{br}+\sum_{j\in J}n_j\,B_j\otimes\mathbb 1_r .
```

From 04-branch-fall@v3 (this subproject). Setting there: one body with the places of Model D and a conserved clock level, whose level blocks are $`C^{(k)}=\frac{\tau_k}2\sum_x\zeta_{x,k}\bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\bigr)+\sum_x\lvert x\rangle\langle x\rvert\otimes\bigl(M_{x,k}\sigma_3+V_{x,k}\mathbb 1_2\bigr)`$ with the linear level profiles $`M_{x,k}=M_k+G_kx`$, $`V_{x,k}=-\mathcal F_kx`$, $`\zeta_{x,k}=1+g_{\zeta,k}(x+\tfrac12)`$; a medium with the records $`K_x=\kappa\,x\,X`$, whose mean $`\kappa\,x\,\langle X\rangle`$ is counted in $`V_{x,k}`$ (the effective body contract; at leading order in $`\kappa`$ the body evolves by it). With all gradients of the level $`k`$ set to zero the level block is $`-\tau_k\sin\hat p\,\sigma_1+M_k\sigma_3`$, with the eigenvalues $`\pm\omega_k(p)`$, $`\omega_k(p):=\sqrt{M_k^2+\tau_k^2\sin^2p}`$, and the eigenvectors $`\beta_{k,\pm}(p)`$ of (5.6) of 04-ilang-time/05-moving-clock with $`\tau\to\tau_k`$, $`\mu_k\to M_k`$. For a level $`k`$, a branch $`\sigma\in\{+,-\}`$ and a smooth $`2\pi`$-periodic $`g`$ with $`\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g\rvert^2=1`$, the **branch start** $`B_{k,\sigma}[g]`$ is $`\lvert\phi\rangle=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\,g(p)\,\lvert p\rangle\otimes\beta_{k,\sigma}(p)\otimes\lvert f_k\rangle`$ on the infinite chain, and $`\langle F\rangle_g:=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert g(p)\rvert^2F(p)`$; it is concentrated at $`p_0`$ with the spread $`\delta p`$ if the weight $`\lvert g\rvert^2\frac{\mathrm dp}{2\pi}`$ has the mean $`p_0`$ and the variance $`\delta p^2`$ on the arc $`(p_0-\pi,p_0+\pi]`$, and at rest if $`p_0=0`$. "First order in the gradients" there: first order in $`G_k`$, $`\mathcal F_k`$, $`g_{\zeta,k}`$ of the level $`k`$, at fixed $`\lambda`$, start and chain, followed by the limit of a long chain; records at leading order in $`\kappa`$. $`\bar x_{\rm lab}`$ is the mean position label. Inside one level the index $`k`$ is dropped: $`\tau,M,G,\mathcal F,g_\zeta,\omega`$; a prime is $`\partial_p`$; $`\mathsf b:=\lvert G\rvert+M\lvert g_\zeta\rvert+\lvert\mathcal F\rvert`$; $`X_g:=\bigl(\int\frac{\mathrm dp}{2\pi}\lvert g'\rvert^2\bigr)^{1/2}`$. Model D is the member $`\tau_k=\tau`$, $`M_k=m+d_k`$ with all gradients zero.

Eq. (4.7) of 04-branch-fall. The first-order velocity of $`B_{k,\sigma}[g]`$ is $`\lambda\,\langle a_{k,\sigma}\rangle_g`$ plus a rest that is bounded for all $`\lambda\ge0`$, with the coefficient

```math
\boxed{\;a_{k,\sigma}(p)=\frac{g_{\zeta,k}\tau_k^4\sin^2p-G_kM_k\tau_k^2\cos2p}{\omega_k^2}+\sigma\,\mathcal F_k\,\frac{\tau_k^2\bigl(M_k^2\cos2p-\tau_k^2\sin^4p\bigr)}{\omega_k^3}\;},\qquad\lvert a_{k,\sigma}(p)\rvert\le\frac{\tau_k^2}{M_k}\,\mathsf b_k .
```

Eq. (4.10) of 04-branch-fall, with $`a^{(1)}(\lambda)`$ the first-order acceleration of $`\bar x_{\rm lab}`$ and $`\overline{a^{(1)}}`$ its average over a window $`[\lambda_1,\lambda_1+\Lambda]`$, for all $`\lambda_1\ge0`$, $`\Lambda>0`$ and every smooth $`g`$:

```math
\Bigl\lvert\overline{a^{(1)}}-\langle a_{k,\sigma}\rangle_g\Bigr\rvert\le\frac{2\tau}{M\Lambda}\,\mathsf b\,\Bigl(X_g+\frac{\tau}{2M}\Bigr)\ \ (\text{exact}),\qquad\lim_{\Lambda\to\infty}\overline{a^{(1)}}=\langle a_{k,\sigma}\rangle_g .
```

Eq. (4.11) of 04-branch-fall, for every sequence of branch starts concentrated at $`p_0`$ with $`\delta p\to0`$:

```math
\bigl\lvert\langle a_{k,\sigma}\rangle_g-a_{k,\sigma}(p_0)\bigr\rvert\le\tfrac12\sup_p\lvert a_{k,\sigma}''\rvert\,\delta p^2\ \ (\text{exact}),\qquad\text{drift acceleration}=\lim_{\delta p\to0}\lim_{\Lambda\to\infty}\overline{a^{(1)}}=a_{k,\sigma}(p_0).
```

Eq. (4.16) of 04-branch-fall, the drift acceleration at rest:

```math
\boxed{\;a_{k,\sigma}(0)=\frac{\tau_k^2}{M_k}\,\bigl(\sigma\,\mathcal F_k-G_k\bigr)\;}
```

Eq. (4.24) of 04-branch-fall, for the class $`\mathcal C`$ under the hypothesis $`a_{k,+}(0)=a\neq0`$ for all $`k`$, at first order in the gradients and at leading order in $`\kappa`$. Here $`r(x)=\eta_x/\lambda_0`$ is the rate (3.23) in its wide-start form, $`d_0:=\kappa\sigma_X`$ is the distance of neighbouring positions in the background of (17.15), $`\bar x=d_0\,\bar x_{\rm lab}\,\hat e`$ with $`\hat e:=e/\sigma_X`$, and $`v_{\max}=\tau d_0`$ is the bound (5.11) of 04-ilang-time/05-moving-clock:

```math
\boxed{\;\frac{\mathrm d^2\bar x}{\mathrm d\lambda^2}\Big\vert_{\rm drift}=d_0\,a_{k,+}(0)\,\hat e=-\,\frac{v_{\max}^2}{d_0}\;\frac{r(x+1)-r(x)}{r(x)}\;\hat e\;}
```

From 05-moving-clock@v3 of 04-ilang-time. Setting there: one Model D body with the contract $`C_b=C_{\rm D}`$ of the base problem, the records $`K_x=\kappa xX`$ and the start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`d_k:=\frac{2\pi k}{N\lambda_0}`$; the plane waves $`\lvert p\rangle=\sum_xe^{ipx}\lvert x\rangle`$, $`p\in(-\pi,\pi]`$.

Eq. (5.5) of 04-ilang-time/05-moving-clock:

```math
C_b\bigl(\lvert p\rangle\otimes\beta\otimes\lvert f_k\rangle\bigr)=\lvert p\rangle\otimes C_k(p)\beta\otimes\lvert f_k\rangle,\qquad C_k(p):=-\tau\sin p\,\sigma_1+\mu_k\sigma_3,\qquad\mu_k:=m+d_k .
```

Eq. (5.6) of 04-ilang-time/05-moving-clock, the eigenvalues $`\pm\omega_k(p)`$ and the real eigenvectors $`\lvert p\rangle\otimes\beta_{k,\pm}(p)\otimes\lvert f_k\rangle`$ of $`C_b`$:

```math
\omega_k(p)=\sqrt{\mu_k^2+\tau^2\sin^2p},\quad
\beta_{k,+}=\begin{pmatrix}\cos\frac{\theta_k}2\\ \sin\frac{\theta_k}2\end{pmatrix},\quad
\beta_{k,-}=\begin{pmatrix}-\sin\frac{\theta_k}2\\ \cos\frac{\theta_k}2\end{pmatrix},\quad
\tan\theta_k(p)=-\frac{\tau\sin p}{\mu_k},\ \ \lvert\theta_k\rvert<\frac\pi2 .
```

Eq. (5.11) of 04-ilang-time/05-moving-clock, the bound (17.7) of 03-ilang-space/17-motion for this $`C_b`$ (the maximal speed):

```math
v_{\max}=\tau\,\kappa\sigma_X=\max_h\sum_{h'}\lvert t_{hh'}\rvert\,d_0(h,h') .
```

Eq. (5.1) of 04-ilang-time/05-moving-clock, the reading distribution of a ring clock with $`N`$ places as a function of the advance $`\vartheta`$; (2.13) there is the reading distribution $`p(a;\lambda)`$ of the ring clock with the tick $`\lambda_0`$ of 04-ilang-time/02-clock, started in the place $`\lvert0\rangle`$:

```math
P_N(a;\vartheta):=\Bigl\lvert\frac1N\sum_{k=0}^{N-1}e^{2\pi ik(a-\vartheta)/N}\Bigr\rvert^2=\frac{\sin^2(\pi\vartheta)}{N^2\sin^2\bigl(\pi(\vartheta-a)/N\bigr)},\qquad p(a;\lambda)=P_N(a;\lambda/\lambda_0)\ \text{in (2.13)}.
```

From 03-ilang-space/17-motion@v2. Setting there: $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$; the start is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, $`\lvert u_h\rangle:=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$, $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$; with $`p_h(\lambda)`$ the place weights of the view of $`b`$, $`\bar x(\lambda):=\sum_hp_h(\lambda)\,u_h`$.

Eq. (17.15) of 03-ilang-space/17-motion, for the chain $`h_m`$, $`m\in\mathbb Z`$, with $`K_{h_m}=m\,X`$, $`X`$ self-adjoint on $`\mathcal H_c`$, $`\sigma_X:=(\langle X^2\rangle-\langle X\rangle^2)^{1/2}>0`$ and $`e:=(X-\langle X\rangle)\chi`$, so that $`\lVert e\rVert=\sigma_X`$ and $`u_{h_m}=m\,e`$:

```math
d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X,\qquad \bar x=\bar m\,e,\quad \bar m:=\sum_mm\,p_{h_m},\qquad s^2=\sigma_X^2\sum_m(m-\bar m)^2p_{h_m} .
```

From 16-common-space@v2 of 03-ilang-space. Setting there: two objects $`a`$, $`b`$ of different types (places $`h`$, $`k`$) and a medium $`c`$, with $`C=\sum_h\lvert h\rangle\langle h\rvert_a\otimes\mathbb 1_b\otimes K^A_h+\sum_k\mathbb 1_a\otimes\lvert k\rangle\langle k\rvert_b\otimes K^B_k`$ and a product start with the medium in $`\chi`$; $`u^A_h:=(K^A_h-\langle K^A_h\rangle)\chi`$, $`u^B_k:=(K^B_k-\langle K^B_k\rangle)\chi`$ are the record vectors, and $`\mathcal N:=\{v\in\mathcal H_c:\langle\chi\vert v\rangle=0\}`$. $`X_A`$ and $`X_B`$ are the sets of leading-order points of the views of $`\{a\}`$ and of $`\{b\}`$ (places with equal record vectors form one point). A **correspondence** is a bijection $`\pi:D_A\to D_B`$ between subsets $`D_A\subseteq X_A`$, $`D_B\subseteq X_B`$ with $`\lvert D_A\rvert\ge2`$ such that, at leading order, the medium does not witness which object stands at which of two matched points.

Eq. (16.11) of 03-ilang-space/16-common-space: $`\pi`$ is a correspondence if and only if

```math
u^A_x-u^A_{x'}=u^B_{\pi(x)}-u^B_{\pi(x')}\ \ \forall x,x'\in D_A
\iff
\exists\,t_\pi\in\mathcal N:\ u^B_{\pi(x)}=u^A_x+t_\pi\ \ \forall x\in D_A .
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- The four types are pairwise different and each has one instance, so no swap condition applies.
- The two Model D bodies, the common medium with one operator and one strength, the class $`\mathcal W`$ of bindings, the coupling of the field to the rest and clock term of each part, the sharp and stationary state of the field, the diagonal on-site binding and the regime $`\mathsf R`$ are assumptions of this package (M8, A11). Equal parameters of the two types are never assumed (M7); where a result needs $`\tau_1=\tau_2`$ or $`g_1=g_2`$, the package says so.
- A bound level and a packet built from it are distinguished starts (M9, A11): the results state what holds for a pair in a bound level, not that a pair is in one. The parts are not started in branch starts of their own.
- Standard first-order perturbation theory in a term of the contract, standard perturbation theory for an isolated simple eigenvalue, and standard facts on packets and on the averaging of oscillating terms may be used; state them with their conditions.
- Every limit is stated with its order: the first order in the gradients, the long chain, the window, the sharp total label, and $`\epsilon\to0`$ at fixed $`u`$ before any limit in $`u`$. Where two of them do not commute, this is stated, and each reported quantity carries the order that defines it. A statement about a rate of change is derived for that rate; it is not inferred from a bound or an estimate of the quantity whose derivative it is. A range of $`\lambda`$ is stated per quantity.
- Every statement with "all", "iff", "only" or "well defined" is stated with its exceptional members (no binding, equal data of the two bodies, $`E_b''(P_0)=0`$, a vanishing coefficient of a gradient, $`\varrho_i=0`$, a level close to the band) and for the class in which it is derived; a condition that is only sufficient is called sufficient. An expansion names its parameter, which is one of the small numbers of the stated regime.

## Scope

- **Class.** Items 1 and 2: every binding of the class $`\mathcal W`$, all data of the two bodies, every bound level in the sense of the setting (simple, outside the bands, on an open interval $`\mathcal P_0\ni0`$), every packet of the class $`\mathcal G(\mathcal P_0)`$, all values of $`g_1`$, $`g_2`$, $`\kappa\langle X\rangle`$. Items 3 and 4: every diagonal on-site binding with $`\hat w_{11}\neq0`$, the bound level (11.12), the regime $`\mathsf R`$ at fixed hatted data, packets concentrated at $`P_0=0`$. Item 5: the classes of the results it cites.
- **Controls.** The common gradient against $`g_1\neq g_2`$; $`\tau_1=\tau_2`$ against $`\tau_1\neq\tau_2`$; a wide pair against a tight pair; $`w_{11}<0`$ against $`w_{11}>0`$; $`\langle X\rangle=0`$ against $`\langle X\rangle\neq0`$; the free parts in the same field.
- In scope:
  - the first-order motion of the two parts of a pair that starts in a bound level, in a sharp and stationary field with linear profile;
  - the drift acceleration of the pair, the quantities that enter it, and its comparison with the falls of the free parts;
  - its dependence on the clock levels of the parts and on the binding;
  - the number that ties it to the relative change of the clock rate of a part.
- Out of scope:
  - a field that is not sharp, a field with its own contract acting on the pair, a field that changes with $`\lambda`$, and a field that responds to the bodies;
  - a factor of the field on the binding or on the motion terms; a binding that acts on the clock labels; more than two bodies; instances of one type (Law 5);
  - degenerate bound levels and the flat values of 11-bound-pair; bound levels attached to the other bands; a joint limit of $`\epsilon`$ and $`u`$;
  - the second order in the gradients, a level profile that is not linear, the fall of a moving pair beyond what item 2 contains, and records beyond leading order in $`\kappa`$;
  - any physical meaning beyond the definitions (M1–M4); no theory of gravity, no theory that contains time and no theory of bound states of a named physical system may be used as an input.

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: derive.
- Item 4: short argument.
- Item 5: standard (a table of results with their tags).

## Expected result

- Item 1: a generator with a yes/no answer and a statement; an operator, its gradient terms in two labels, and five answers with a statement on the convention.
- Item 2: two first-order velocities, each with a growing part, a coefficient and a rest; a statement on the separation; a drift acceleration as a sum of three terms with their coefficients, the limits and a statement; a relation.
- Item 3: a closed form with a remainder and two limiting forms; ratios in three cases, each with an answer and a leading difference; a condition with a leading dependence; a comparison.
- Item 4: a rate with its conditions and a relative change; two numbers with three answers; an answer with a leading deviation.
- Item 5: a table.

Give every main result a tag $`(13.k)`$.

Consistency checks, at most three: for example the limit of no binding against the free parts, the common gradient against the scaling relation (11.6), and dimensions.

## Code

Required: check: a numerical evolution of a packet of the pair, built from the bound level of a diagonal on-site binding, on a finite chain with small gradients, with the first order taken by a symmetric difference in the gradients. At least four parameter sets: three with $`\tau_i/M_i\le0.2`$, among them one with $`\tau_1\neq\tau_2`$ and $`M_1\neq M_2`$ and one with $`w_{11}>0`$, and one with $`\tau_i/M_i`$ of order one; each with the common gradient, with $`g_1\neq g_2`$, and with a plain gradient in the place of $`\kappa\langle X\rangle`$. Compare with the derivation: the coefficient of the linear growth of the first-order velocities of both parts with item 2 (for all sets, to numerical accuracy, with the coefficients of item 2 obtained from the numerical bound level), and with the closed form of item 3 (for the sets in the regime $`\mathsf R`$, with the size of the deviation against the next order in $`\epsilon`$); the first-order change of the mean label separation with item 2(b). State the chain, the range of the label separation, the width of the packet and the range of $`\lambda`$ used, and how the convergence in them was checked.
