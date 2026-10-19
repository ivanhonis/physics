# Question: 11-bound-pair

- **Subproject:** 05-ilang-free-fall
- **Package:** 11-bound-pair
- **Equation tags:** (11.k)
- **Created:** 2026-10-11

## Goal

Determine the properties of a bound pair of two bodies of different types that the fall of the pair will need: the bound level and its dependence on the total plane-wave label, the curvature of that dependence compared with the inertias of the parts and with the cost of the pair, the composition of the cost of the pair, and the rates of the clocks of the parts inside the pair. No field acts in this package. It prepares criterion 9.

**Setting.**
- **Objects.** Two bodies $`b_1`$, $`b_2`$ of different types and a recording medium $`c`$ of a third type, one instance each.
- **Bodies.** For $`i=1,2`$ the body $`b_i`$ has the places $`(x_i,s_i,a_i)`$ of Model D and the Model D contract $`C^{\rm D}_i=A_i+B_i`$ with its own data: $`\tau_i>0`$, $`m_i>0`$, a clock with $`N_i\ge2`$ places, the tick parameter $`\lambda_{0,i}`$ and the clock operator $`D_i`$; $`d^{(i)}_k:=\frac{2\pi k}{N_i\lambda_{0,i}}`$ and $`M^{(i)}_k:=m_i+d^{(i)}_k`$. $`A_i`$ is the motion term and $`B_i`$ the rest and clock term of $`b_i`$. Both position labels run over the same chain, $`x_i\in\mathbb Z`$ as the limit of long chains (A1). $`\hat x_i:=\sum_xx\,\lvert x\rangle\langle x\rvert`$ on the position label of $`b_i`$, and $`\sigma^{(i)}_3`$ is $`\sigma_3`$ on the branch label of $`b_i`$.
- **Records and common points.** One medium records both bodies through the same operator and with the same strength: $`C_{\rm rec}:=\kappa\,\hat x_1\otimes X+\kappa\,\hat x_2\otimes X`$ with $`\kappa>0`$ and $`X`$ self-adjoint on $`\mathcal H_c`$; the medium starts in $`\chi`$ with $`\sigma_X>0`$. By (17.15) the position $`x`$ of either body has the record vector $`\kappa\,x\,e`$. By (16.11) the map $`x\mapsto x+s`$ from the positions of $`b_1`$ to those of $`b_2`$ is then a correspondence for every integer $`s`$. The **label separation** is $`r:=x_1-x_2`$; a binding that depends on $`r`$ depends on the separation of corresponding points, and the choice $`s=0`$ among the correspondences is a convention of the labels.
- **Binding (the class $`\mathcal W`$).** The binding is one pair term between $`b_1`$ and $`b_2`$ (A5),
  ```math
  U=\sum_{x_1,x_2}\lvert x_1\rangle\langle x_1\rvert\otimes\lvert x_2\rangle\langle x_2\rvert\otimes W(x_1-x_2),
  ```
  where, for every integer $`r`$, $`W(r)`$ is a self-adjoint operator on the two branch labels ($`\mathbb C^2\otimes\mathbb C^2`$), acting as the identity on the two clock labels, and $`W(r)=0`$ for $`\lvert r\rvert>R`$ with a finite range $`R\ge0`$. An **on-site binding** has $`W(r)=\delta_{r,0}W_0`$. A **diagonal on-site binding** has $`W_0=\sum_{s_1,s_2}w_{s_1s_2}\,\lvert s_1s_2\rangle\langle s_1s_2\rvert`$ with four real numbers $`w_{s_1s_2}`$, $`s_i\in\{1,2\}`$.
- **Contracts.** $`C_{\rm pair}:=C^{\rm D}_1+C^{\rm D}_2+U`$ on $`\mathcal H_{b_1}\otimes\mathcal H_{b_2}`$, and $`C=C_{\rm pair}+C_{\rm rec}`$. The two bodies, the class of bindings and every start are assumptions of this package (M8, M9).
- **Levels and fibres.** The clock levels of the two bodies are conserved. Fix levels $`k_1`$, $`k_2`$ and write $`M_i:=M^{(i)}_{k_i}`$; on these levels $`B_i`$ acts as $`M_i\sigma^{(i)}_3`$. On $`\mathbb Z`$, $`C_{\rm pair}`$ commutes with the joint shift $`(x_1,x_2)\mapsto(x_1+1,x_2+1)`$. For a **total plane-wave label** $`P\in(-\pi,\pi]`$, the **fibre contract** $`H(P)`$ is $`C_{\rm pair}`$ on the levels $`k_1`$, $`k_2`$ restricted to the plane waves of the joint shift with the label $`P`$, written as an operator on functions of $`r`$ with values in $`\mathbb C^2\otimes\mathbb C^2`$; the package fixes the convention for the phases.
- **Bound level.** A **bound level** on an interval $`\mathcal P\ni0`$ of total labels is a function $`E_b(P)`$, $`P\in\mathcal P`$, such that $`E_b(P)`$ is an eigenvalue of $`H(P)`$ with an eigenvector $`\psi_P`$ that is square-summable in $`r`$, and is isolated from the rest of the spectrum of $`H(P)`$. For an operator $`O`$ on the fibre, $`\langle O\rangle_P:=\langle\psi_P\vert O\vert\psi_P\rangle`$ with $`\lVert\psi_P\rVert=1`$. A bound level depends on $`k_1`$, $`k_2`$ through $`M_1`$, $`M_2`$.
- **Curvature inertia.** For a bound level with $`E_b''(0)\neq0`$, $`\mathfrak m_b:=1/E_b''(0)`$ (a prime is $`\partial_P`$). For one Model D body on the level $`k`$, (6.7) and (6.20) give $`1/\omega_k''(0)=M_k/\tau^2=I^{\rm lab}_k`$; $`\mathfrak m_i:=M_i/\tau_i^2`$ for the two parts. That $`\mathfrak m_b`$ is the inertia of the pair in a response is not assumed here and is not asked in this package.
- **Regime $`\mathsf R`$ (item 3).** Slow parts and a binding of the order of their motion: $`\tau_i=\epsilon\,\hat\tau_i`$ and $`w_{s_1s_2}=\epsilon^2\,\hat w_{s_1s_2}`$ with fixed $`\hat\tau_i>0`$, $`\hat w_{s_1s_2}`$, $`M_i`$, and $`\epsilon\to0`$. "Leading order" in $`\mathsf R`$ means the first order in $`\epsilon`$ at which the quantity differs from its value for the two parts at rest without a binding. Records: the weak-record regime, $`\kappa\to0`$ at fixed $`\lambda`$, chain and start; the items below concern $`C_{\rm pair}`$.

1. **Structure.**
   - (a) Give the fibre contract $`H(P)`$. Determine the part of its spectrum that belongs to eigenvectors that are not square-summable in $`r`$ (the two-body bands), from (5.6), and its edges at $`P=0`$.
   - (b) With (21.2): determine which replacements of the listed terms $`C^{\rm D}_1`$, $`C^{\rm D}_2`$, $`U`$, $`C_{\rm rec}`$ leave $`C`$ unchanged, and what the condition "$`W(r)=0`$ for $`\lvert r\rvert>R`$" fixes among them. Determine which of the following are well defined (M6): $`W(r)`$; $`M_i`$; $`E_b(P)`$; $`E_b(P)-(M_1+M_2)`$; $`E_b(P)-E_b(0)`$; $`E_b''(0)`$; $`\langle\sigma^{(i)}_3\rangle_P`$.

2. **Exact relations for a bound level.** For every binding of the class $`\mathcal W`$ and every bound level:
   - (a) Determine the derivatives of $`E_b(P)`$ with respect to $`M_1`$, $`M_2`$, $`\tau_1`$, $`\tau_2`$ and with respect to a common factor $`\theta`$ of the binding ($`W\to\theta W`$, at $`\theta=1`$), as expectation values $`\langle\cdot\rangle_P`$. Determine the relation among them that follows from the way $`H(P)`$ scales when all of $`\tau_i`$, $`M_i`$ and $`W`$ are multiplied by one number.
   - (b) Determine $`E_b'(P)`$ as an expectation value, and its relation to the rates of change of the mean position labels of the two bodies in a state of the pair built from the bound level with total labels near $`P`$. State whether the two bodies have the same mean velocity in such a state.
   - (c) Determine $`E_b''(P)`$ as the sum of an expectation value and of a sum over the rest of the spectrum of $`H(P)`$.

3. **Diagonal on-site binding.**
   - (a) Give the equation that determines the bound levels of $`H(P)`$ for a diagonal on-site binding, with every coefficient as an explicit sum or integral over the relative plane-wave label.
   - (b) In the regime $`\mathsf R`$, at leading order: determine the bound levels attached to the band in which both bodies are in their upper branch (the band whose edge at $`P=0`$ is $`M_1+M_2`$): the condition for their existence, their number, $`E_b(P)`$ in closed form for $`P`$ in a neighbourhood of $`0`$, and the eigenvector $`\psi_P`$ (its dependence on $`r`$ and on the branch labels at leading order). State which of the four numbers $`w_{s_1s_2}`$ enter at this order.
   - (c) From (b) and item 2, at leading order in $`\mathsf R`$: determine $`E_{\rm bind}:=E_b(0)-(M_1+M_2)`$, $`E_b''(0)`$, $`\langle\sigma^{(i)}_3\rangle_0`$, $`\langle A_i\rangle_0`$ and $`\langle U\rangle_0`$.
   - (d) Give the forms of (c) in the two limits of the binding within $`\mathsf R`$: a wide pair ($`\hat w\to0`$ in the combination that enters) and a tight pair (that combination large).

4. **Curvature, inertias and cost.** At leading order in $`\mathsf R`$, for the bound levels of item 3:
   - (a) Compare $`\mathfrak m_b`$ with $`\mathfrak m_1+\mathfrak m_2`$: the sign of the difference and its size as a function of the binding; for a wide pair express the difference through $`E_{\rm bind}`$.
   - (b) For $`\tau_1=\tau_2=\tau`$: compare $`\tau^2\mathfrak m_b`$ with $`M_1+M_2+E_{\rm bind}`$ and with $`M_1\langle\sigma^{(1)}_3\rangle_0+M_2\langle\sigma^{(2)}_3\rangle_0`$. For each pair of quantities determine whether they agree exactly, to a stated order, or not at all, and give the leading difference.
   - (c) Compare with (21.15) and (21.16) of 03-ilang-space/21-composite-body, which concern a pair without rest terms: state what is common and what is different.
   - (d) Control: the same comparison for $`\tau_1\neq\tau_2`$ without a binding (two free parts with one total label).

5. **Clocks of the parts.** Let the pair be in a bound level at $`P=0`$ (a start built from the bound eigenvectors with total labels concentrated at $`0`$), and let the clock label of the part $`i`$ be in the place $`\lvert0\rangle`$, the other part in one level.
   - (a) Determine the statistics of a reading of the clock label of the part $`i`$ to first order in the level spacing of its clock, in the form of (5.21), and its rate. Express the rate through an expectation value of item 2, and give its ratio to the rate $`1/\lambda_{0,i}`$ of the free part at rest.
   - (b) Evaluate the ratio for the bound levels of item 3 at leading order in $`\mathsf R`$, and state whether the clocks of the two parts are slowed by the same factor.

## Inputs

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

Eq. (5.21) of 04-ilang-time/05-moving-clock, the statistics $`q(a;\lambda)`$ of a reading of the clock label of a Model D body whose start is concentrated near $`p_0`$ with the spinor of the positive branch of the level $`0`$ and the clock label in $`\lvert0\rangle`$, in the weak-record regime; $`\epsilon:=\frac{2\pi}{N\lambda_0m}`$, $`\bar\mu:=m+\frac{\pi(N-1)}{N\lambda_0}`$, $`\omega_0(p):=\sqrt{m^2+\tau^2\sin^2p}`$, and the remainder is $`\mathcal R=O\bigl((N\epsilon)^2(1+\lambda/\lambda_0)^2\bigr)+O(\delta p^2)+O(\kappa)`$, with $`\delta p`$ the spread of the start:

```math
q(a;\lambda)=P_N\Bigl(a;\Gamma(p_0)\frac{\lambda}{\lambda_0}\Bigr)+\mathcal R,\qquad
\Gamma(p_0)=\frac{\bar\mu}{\sqrt{\bar\mu^2+\tau^2\sin^2p_0}}=\gamma\Bigl[1+\frac{(N-1)\epsilon}2\bigl(1-\gamma^2\bigr)\Bigr]+O\bigl((N\epsilon)^2\bigr),\quad\gamma:=\frac m{\omega_0(p_0)} .
```

From 06-inertia-internal-energy@v3 of 04-ilang-time. Setting there: one Model D body with the records $`K_x=\kappa\,x\,X`$; on the clock level $`k`$ the contract acts as $`C_k(p)=-\tau\sin p\,\sigma_1+M_k\sigma_3`$ with the eigenvalues $`\pm\omega_k(p)`$, $`\omega_k(p)=\sqrt{M_k^2+\tau^2\sin^2p}`$.

Eq. (6.7) of 04-ilang-time/06-inertia-internal-energy:

```math
M_k:=m+d_k=m+\frac{2\pi k}{N\lambda_0}\ \ (\text{rest cost of level }k,\ \text{eigenvector }\lvert1\rangle),\qquad\text{gap }2M_k,\qquad \omega_k''(0)=\frac{\tau^2}{M_k}.
```

Eq. (6.20) of 04-ilang-time/06-inertia-internal-energy. For a uniform gradient $`F`$ added to the contract, at first order in $`F`$, at leading order in $`\kappa`$ and averaged over a long interval, the acceleration of the body on the level $`k`$ in the positive branch at rest is $`\mu_{\rm av}(k)F`$; with $`n:=e/\sigma_X`$, $`d_1:=\kappa\sigma_X`$, $`\bar m`$ the mean position label and $`\mathcal F=d_1\,g(n,F)`$ the gradient per label ($`g`$ is the real inner product of the record vectors):

```math
\mu_{\rm av}(k)=\frac{1}{I_k}\,n\,g(n,\cdot\,),\qquad
I_k:=\frac{M_k}{\tau^2\kappa^2\sigma_X^2}=\frac{I_k^{\rm lab}}{d_1^{\,2}},\qquad
I_k^{\rm lab}:=\frac{M_k}{\tau^2}\quad\bigl(\overline{\ddot{\bar m}}=\mathcal F/I_k^{\rm lab}\bigr).
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

From 21-composite-body@v2 of 03-ilang-space. Setting there: two bodies $`b_1`$, $`b_2`$ of different types (places $`h`$, $`k`$) and a medium $`c`$, with $`C=C_1+C_2+\sum_h\lvert h\rangle\langle h\rvert\otimes K^{(1)}_h+\sum_k\lvert k\rangle\langle k\rvert\otimes K^{(2)}_k+W`$, where $`C_1=\sum_{h,h'}t^{(1)}_{hh'}\lvert h\rangle\langle h'\rvert`$ and $`C_2=\sum_{k,k'}t^{(2)}_{kk'}\lvert k\rangle\langle k'\rvert`$ with Hermitian matrices $`t^{(i)}`$, the $`K^{(i)}`$ are self-adjoint on $`\mathcal H_c`$, and the binding is $`W=\sum_{h,k}W_{hk}\,\lvert h\rangle\langle h\rvert\otimes\lvert k\rangle\langle k\rvert`$ with real $`W_{hk}`$; $`C_{\rm body}:=C_1\otimes\mathbb 1+\mathbb 1\otimes C_2+W`$.

Eq. (21.2) of 03-ilang-space/21-composite-body, the general change of the data $`(t^{(1)},t^{(2)},K^{(1)},K^{(2)},W)`$ of this form that leaves $`C`$ unchanged, with $`Z`$ self-adjoint on $`\mathcal H_c`$ and real numbers $`\alpha_h`$, $`\beta_k`$, $`\tau_h`$, $`\tau'_k`$ (these $`\tau_h`$, $`\tau'_k`$ are not the $`\tau_i`$ of this question):

```math
\delta K^{(1)}_h=Z+\alpha_h,\quad \delta K^{(2)}_k=-Z+\beta_k,\quad \delta t^{(1)}_{hh}=\tau_h,\quad \delta t^{(2)}_{kk}=\tau'_k,\quad \delta W_{hk}=-(\tau_h+\alpha_h)-(\tau'_k+\beta_k),
```

The example there: both bodies on the chain $`m\in\mathbb Z`$ with the same hopping, $`C_1=t\sum_m\bigl(\lvert h_m\rangle\langle h_{m+1}\rvert+\lvert h_{m+1}\rangle\langle h_m\rvert\bigr)`$ with $`t>0`$ and $`C_2`$ likewise, no on-site terms, the records $`K^{(1)}_{h_m}=K^{(2)}_{k_m}=m\,X`$, and the on-site binding $`W=U\sum_m\lvert h_m\rangle\langle h_m\rvert\otimes\lvert k_m\rangle\langle k_m\rvert`$ with $`U<0`$; $`K`$ is the total quasi-momentum.

Eq. (21.12) of 03-ilang-space/21-composite-body, the bound state of the example and the spectrum of $`C_{\rm body}`$:

```math
E_b(K)=-\sqrt{U^2+16t^2\cos^2\tfrac K2},\qquad \mathrm{spec}C_{\rm body}=[-4t,4t]\cup\bigl[-\sqrt{U^2+16t^2},\,-\lvert U\rvert\bigr],\qquad E_{\min}(t,U)=-\sqrt{U^2+16t^2}.
```

Eq. (21.15) of 03-ilang-space/21-composite-body. $`I_c`$ is the scalar inertia of the pair, from its response at $`\lambda=0`$ to a uniform gradient along sequences of starts whose cost tends to $`E_{\min}(t,U)`$; $`I_1`$ is the same for one body alone:

```math
I_c(t,U,\sigma_X)=\frac{\sqrt{U^2+16t^2}}{4t^2\sigma_X^2},\qquad I_1=\frac{1}{2t\sigma_X^2},\qquad I_c(t,0,\sigma_X)=\frac{1}{t\sigma_X^2}=2I_1,\qquad \frac{I_c}{2I_1}=\sqrt{1+\frac{U^2}{16t^2}} .
```

Eq. (21.16) of 03-ilang-space/21-composite-body, with $`E_{\rm bind}:=E_{\min}(t,U)-E_{\min}(t,0)=4t-\sqrt{U^2+16t^2}<0`$ and $`v_{\max}=2t\sigma_X`$ the bound of 03-ilang-space/17-motion for one body of the example:

```math
I_c-2I_1=\frac{\sqrt{U^2+16t^2}-4t}{4t^2\sigma_X^2}=-\frac{E_{\rm bind}}{v_{\max}^2},
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- The three types are pairwise different and each has one instance, so no swap condition applies.
- The two Model D bodies, the common medium with one operator and one strength, the class $`\mathcal W`$ of bindings, the diagonal on-site binding and the regime $`\mathsf R`$ are assumptions of this package (M8). Equal parameters of the two types are never assumed (M7); where a result needs $`\tau_1=\tau_2`$, the package says so.
- A bound level is a distinguished set of states (M9, A11): the results state what holds for a pair in a bound level, not that a pair is in one.
- Standard facts on the spectrum of a self-adjoint operator that is a finite-range change of an operator with bands, and standard perturbation theory for an isolated eigenvalue, may be used; state them with their conditions.
- Every statement with "all", "iff" or "well defined" is stated with its exceptional members (no binding, equal data of the two bodies, a level that merges with a band); a condition that is only sufficient is called sufficient.

## Scope

- **Class.** Items 1 and 2: every binding of the class $`\mathcal W`$, all data of the two bodies, every bound level, every $`P`$ in its interval. Items 3–5: every diagonal on-site binding; item 3(a) for all data, the other parts in the regime $`\mathsf R`$.
- **Controls.** No binding ($`W=0`$) against a binding; $`\tau_1=\tau_2`$ against $`\tau_1\neq\tau_2`$ (item 4); a wide pair against a tight pair.
- In scope:
  - the bound levels of the pair and their dependence on the total label;
  - exact relations between a bound level, its derivatives and expectation values of the terms of the contract;
  - the comparison of the curvature inertia with the inertias of the parts and with the cost of the pair;
  - the rates of the clocks of the parts in a bound level at rest.
- Out of scope:
  - any field and any position-dependent factor (the next package), and the response of the pair to a gradient;
  - bindings that act on the clock labels, bindings of infinite range, more than two bodies, and instances of one type (Law 5);
  - bound levels attached to the other bands, beyond what item 3(a) contains;
  - the clock of a moving pair, and records beyond leading order in $`\kappa`$;
  - any physical meaning beyond the definitions (M1–M4); no theory of gravity, no theory that contains time and no theory of bound states of a named physical system may be used as an input.

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: derive.
- Item 4: short argument.
- Item 5: short argument.

## Expected result

- Item 1: an operator with a set and its edges; a list of replacements with seven yes/no answers.
- Item 2: five expectation values and a relation; an expectation value with a relation and a yes/no answer; a formula.
- Item 3: an equation with explicit coefficients; a condition, a number, a closed form and an eigenvector; five leading terms; two limiting forms.
- Item 4: a sign with a function and an expression; two comparisons, each with an answer and a leading difference; a statement; a control.
- Item 5: a distribution with a rate and a ratio; an evaluation with a yes/no answer.

Give every main result a tag $`(11.k)`$.

Consistency checks, at most three: for example no binding ($`W=0`$), the relation of item 2(a) from the scaling evaluated on the closed form of item 3(b), and equal data of the two bodies.

## Code

Required: check: a numerical diagonalization of the fibre contract $`H(P)`$ on a finite range of $`r`$, for a diagonal on-site binding and at least four parameter sets (three with $`\tau_i/M_i\le0.2`$, among them one with $`\tau_1\neq\tau_2`$ and $`M_1\neq M_2`$, and one with $`\tau_i/M_i`$ of order one), each for several values of $`P`$ near $`0`$. Compare with the derivation: the bound level $`E_b(P)`$ and $`E_b''(0)`$ with the closed forms of item 3 (for the sets in the regime $`\mathsf R`$, with the size of the deviation against the next order in $`\epsilon`$), and the relations of item 2(a) and 2(b) between derivatives of $`E_b`$ and expectation values (for all sets, to numerical accuracy). State the range of $`r`$ used and how the convergence in it was checked.
