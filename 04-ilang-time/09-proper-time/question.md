# Question: 09-proper-time

- **Subproject:** 04-ilang-time
- **Package:** 09-proper-time
- **Equation tags:** (9.k)
- **Created:** 2026-10-10

## Goal

Determine the time shown by a clock carried by a body whose motion changes, and compare two carried clocks between two meetings of their bodies. The motion is changed by a uniform cost gradient on one of the bodies. This is the part of criterion 4 that 05-moving-clock left open.

**Setting.** Model D of 05-moving-clock (items 2–4 there, quoted under "Inputs"), with two bodies.
- **Objects.** Two bodies, object $`1`$ of type $`B_1`$ and object $`2`$ of type $`B_2`$, and a medium $`c`$. The three types are pairwise different, and each object is the only instance of its type.
- **Places.** Each body has the places $`(x,s,a)`$ with $`x\in\mathbb Z`$ (position label), $`s\in\{1,2\}`$ (branch label) and $`a\in\mathbb Z_N`$, $`N\ge2`$ (clock label). $`x\in\mathbb Z`$ is the limit of long finite chains with the starts far from both ends (A1). State how the limit is taken.
- **Body contract.** On the places of one body,
  ```math
  C_{\rm D}=A+B,\qquad A=\frac\tau2\sum_x\Bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\Bigr)\otimes\mathbb 1_N,\qquad B=\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m\mathbb 1_N+D),
  ```
  with $`\tau>0`$, $`m>0`$, the Pauli matrices $`\sigma_1,\sigma_3`$ on the branch label, and $`D=\frac{2\pi}{N\lambda_0}\sum_{k=0}^{N-1}k\lvert f_k\rangle\langle f_k\rvert`$ on the clock label, where $`\lvert f_k\rangle=N^{-1/2}\sum_ae^{2\pi ika/N}\lvert a\rangle`$ and $`\lambda_0>0`$. Both bodies have the same $`\tau`$, $`m`$, $`N`$ and $`\lambda_0`$.
- **Gradient.** Let $`P_x:=\lvert x\rangle\langle x\rvert\otimes\mathbb 1_2\otimes\mathbb 1_N`$ on one body. Body $`1`$ has in addition the term $`G:=-\mathcal F\sum_xx\,P_x`$ with $`\mathcal F>0`$: a uniform gradient of its diagonal entries $`t_{hh}`$ along the position label. Body $`2`$ has no gradient.
- **Contract.**
  ```math
  C=(C_{\rm D}+G)\otimes\mathbb 1\otimes\mathbb 1_c+\mathbb 1\otimes C_{\rm D}\otimes\mathbb 1_c+\sum_x\kappa\,x\,\bigl(P_x\otimes\mathbb 1+\mathbb 1\otimes P_x\bigr)\otimes X ,
  ```
  with $`\kappa>0`$ and $`X`$ self-adjoint on $`\mathcal H_c`$, $`\sigma_X>0`$ as in (17.15), and $`\langle X\rangle=0`$. There is no contract between the two bodies. Both bodies have the records $`K_x=\kappa\,x\,X`$, so both have the record vectors $`u_x=\kappa\,x\,e`$ of (17.15) with $`X\to\kappa X`$.
- **Start.** $`\phi_1\otimes\phi_2\otimes\chi`$. Each $`\phi_i`$ is a start of item 3 of 05-moving-clock: concentrated near a plane-wave label, in the branch of positive eigenvalue, with the clock label in the place $`\lvert0\rangle`$. The label is $`p_0`$ with $`-\frac\pi2<p_0\le0`$ for body $`1`$, and $`0`$ for body $`2`$. The two starts have the same mean position label.
- **Readings.** The clock reading on body $`i`$ has one class per clock label, with statistics $`q_i(a;\lambda)`$. The joint reading of both clocks has one class per pair of clock labels, with statistics $`q_{12}(a_1,a_2;\lambda)`$. Readings are applied at stated values of $`\lambda`$ (A8).
- **Positions.** For each body, $`\bar x_i(\lambda):=\sum_hp^{(i)}_h(\lambda)\,u_h`$ as in 17-motion, with the place weights $`p^{(i)}_h`$ of the view of body $`i`$. The **displacement** is $`\Delta\bar x_i(\lambda):=\bar x_i(\lambda)-\bar x_i(0)`$.
- **Meeting.** In the description above, equal position labels of the two bodies carry equal record vectors, so by (16.11) the matching of equal position labels is a correspondence with $`t_\pi=0`$. The bodies **meet** at $`\lambda`$ if $`\bar x_2(\lambda)-\bar x_1(\lambda)=t_\pi`$, here $`\bar x_1(\lambda)=\bar x_2(\lambda)`$, to the order to which the displacements are determined in item 1. By the choice of the starts they meet at $`\lambda=0`$.

1. **A carried clock under a uniform gradient.** Consider body $`1`$.
   - (a) Determine how the plane-wave label of the start changes with $`\lambda`$. State the condition on $`\mathcal F`$ under which the start stays in the branch of positive eigenvalue, and the size of what is neglected.
   - (b) Determine the displacement $`\Delta\bar x_1(\lambda)`$ to first order in $`\epsilon`$ relative to its leading term (the orders are defined under "Assumptions"). State what the oscillating part of the velocity (5.24) contributes to it.
   - (c) Determine $`q_1(a;\lambda)`$ to first order in $`\epsilon`$ and to leading order in the spread of the start. Determine whether it has the form of (5.21) with $`\Gamma(p_0)\lambda/\lambda_0`$ replaced by a function $`\vartheta_1(\lambda)`$. If it has, determine $`\vartheta_1`$, the **clock advance**; if not, determine what replaces it.
   - (d) Determine whether, to this order, $`\mathcal F`$ enters $`\mathrm d\vartheta_1/\mathrm d\lambda`$ otherwise than through the plane-wave label at $`\lambda`$.

2. **Rate along the path.** Let $`V_1(\lambda):=\mathrm d\Delta\bar x_1/\mathrm d\lambda`$, computed from the expression of item 1(b).
   - Determine the relation between $`\lambda_0\,\mathrm d\vartheta_1/\mathrm d\lambda`$ and $`\lVert V_1(\lambda)\rVert/v_{\max}`$, with $`v_{\max}`$ of (5.11), in two forms: without an expansion in the plane-wave label, to the orders in $`\epsilon`$ of items 1(b) and 1(c); and to leading order for small plane-wave labels.
   - Express $`\vartheta_1(\lambda)`$ as a functional of the path $`\lambda'\mapsto V_1(\lambda')`$, $`0\le\lambda'\le\lambda`$, to leading order for small plane-wave labels.

3. **Two clocks between two meetings.**
   - (a) Determine $`q_{12}(a_1,a_2;\lambda)`$ in terms of $`q_1`$ and $`q_2`$, and the clock advance $`\vartheta_2(\lambda)`$ of body $`2`$.
   - (b) Determine all $`\lambda>0`$ at which the bodies meet, and the first of them, $`\lambda_R`$.
   - (c) Determine $`\vartheta_1(\lambda_R)`$, $`\vartheta_2(\lambda_R)`$ and their ratio as functions of $`p_0`$, $`\mathcal F\lambda_0`$ and the parameters of the bodies.
   - (d) Determine which of the two clocks has advanced more at $`\lambda_R`$, for all admissible $`p_0`$ and $`\mathcal F`$, and when the advances are equal. Determine whether the same holds at every later meeting.
   - (e) Determine the deviation of the ratio of item (c) from $`1`$ to leading order for small $`\lvert p_0\rvert`$, and express it through the mean of $`\lVert V_1\rVert^2/v_{\max}^2`$ over $`[0,\lambda_R]`$.
   - (f) Determine the conditions under which both clock readings at $`\lambda_R`$ are certain to the order of item 1(c), and what the two readings then show.

## Inputs

From 05-moving-clock@v3 (this subproject). Setting there: one body with the places and the contract $`C_b=C_{\rm D}`$ above, the records $`K_x=\kappa xX`$, and the start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$. Notation fixed there:
- $`d_k:=\frac{2\pi k}{N\lambda_0}`$, $`\epsilon:=\frac{2\pi}{N\lambda_0m}`$, so $`d_k=km\epsilon`$;
- the plane waves $`\lvert p\rangle=\sum_xe^{ipx}\lvert x\rangle`$, $`p\in(-\pi,\pi]`$;
- $`\hat e:=e/\sigma_X`$, with $`e`$ of (17.15);
- $`\gamma:=m/\omega_0(p_0)`$;
- the label velocity $`w_k(p):=\partial_p\omega_k(p)`$ of the positive branch of level $`k`$;
- $`\bar x_{\rm lab}:=\sum_xx\,P(x;\lambda)`$, the mean position label, with $`\bar x=\kappa\,\bar x_{\rm lab}\,e`$.

Eq. (5.1), the reading distribution (2.13) of the minimal ring clock of 02-clock started at $`\lvert0\rangle`$, as a function of the advance $`\vartheta`$:

```math
P_N(a;\vartheta):=\Bigl\lvert\frac1N\sum_{k=0}^{N-1}e^{2\pi ik(a-\vartheta)/N}\Bigr\rvert^2=\frac{\sin^2(\pi\vartheta)}{N^2\sin^2\bigl(\pi(\vartheta-a)/N\bigr)},\qquad p(a;\lambda)=P_N(a;\lambda/\lambda_0)\ \text{in (2.13)}.
```

Eq. (5.5):

```math
C_b\bigl(\lvert p\rangle\otimes\beta\otimes\lvert f_k\rangle\bigr)=\lvert p\rangle\otimes C_k(p)\beta\otimes\lvert f_k\rangle,\qquad C_k(p):=-\tau\sin p\,\sigma_1+\mu_k\sigma_3,\qquad\mu_k:=m+d_k .
```

Eq. (5.6), the eigenvalues $`\pm\omega_k(p)`$ and the real eigenvectors $`\lvert p\rangle\otimes\beta_{k,\pm}(p)\otimes\lvert f_k\rangle`$ of $`C_b`$:

```math
\omega_k(p)=\sqrt{\mu_k^2+\tau^2\sin^2p},\quad
\beta_{k,+}=\begin{pmatrix}\cos\frac{\theta_k}2\\ \sin\frac{\theta_k}2\end{pmatrix},\quad
\beta_{k,-}=\begin{pmatrix}-\sin\frac{\theta_k}2\\ \cos\frac{\theta_k}2\end{pmatrix},\quad
\tan\theta_k(p)=-\frac{\tau\sin p}{\mu_k},\ \ \lvert\theta_k\rvert<\frac\pi2 .
```

Eq. (5.11), the bound (17.7) for this $`C_b`$:

```math
v_{\max}=\tau\,\kappa\sigma_X=\max_h\sum_{h'}\lvert t_{hh'}\rvert\,d_0(h,h') .
```

Eq. (5.20), with $`\bar d:=\frac1N\sum_kd_k=\frac{N-1}2m\epsilon=\langle0\vert D\vert0\rangle`$, $`\bar\mu:=m+\bar d`$ and $`j:=k-\frac{N-1}2`$:

```math
\omega_k=\bar\omega+\Gamma\,m\epsilon j+\tfrac12\bar c\,(m\epsilon j)^2+\bar\rho_k,\qquad
\bar\omega(p):=\sqrt{\bar\mu^2+\tau^2\sin^2p},\quad\Gamma(p):=\frac{\bar\mu}{\bar\omega(p)},\quad\bar c:=\frac{\tau^2\sin^2p}{\bar\omega^3}\le\frac1m,\quad\lvert\bar\rho_k\rvert\le\frac{(m\epsilon\lvert j\rvert)^3}{6m^2}.
```

Eq. (5.21), for the start of item 3 there (concentrated near $`p_0`$, spinor of the positive branch of level $`0`$, clock label in $`\lvert0\rangle`$), in the weak-record regime. The remainder is $`\mathcal R=O\bigl((N\epsilon)^2(1+\lambda/\lambda_0)^2\bigr)+O(\delta p^2)+O(\kappa)`$, with $`\delta p`$ the spread of the start:

```math
q(a;\lambda)=P_N\Bigl(a;\Gamma(p_0)\frac{\lambda}{\lambda_0}\Bigr)+\mathcal R,\qquad
\Gamma(p_0)=\frac{\bar\mu}{\sqrt{\bar\mu^2+\tau^2\sin^2p_0}}=\gamma\Bigl[1+\frac{(N-1)\epsilon}2\bigl(1-\gamma^2\bigr)\Bigr]+O\bigl((N\epsilon)^2\bigr),\quad\gamma:=\frac m{\omega_0(p_0)} .
```

Eq. (5.22), the tick of the first-order distribution (5.21) and its ratio to the tick at $`p_0=0`$, with $`\omega:=\omega_0(p_0)`$:

```math
\lambda_0(p_0)=\frac{\lambda_0}{\Gamma(p_0)},\qquad
R(p_0):=\frac{\lambda_0(p_0)}{\lambda_0(0)}=\frac{\bar\omega(p_0)}{\bar\mu}=\sqrt{1+\frac{\tau^2}{\bar\mu^2}\sin^2p_0}=\frac\omega m\Bigl[1-\frac{(N-1)\epsilon}2\,\frac{\tau^2\sin^2p_0}{\omega^2}\Bigr]+O\bigl((N\epsilon)^2\bigr)\ \ge1 .
```

Eq. (5.24), the label velocity of the same start, exactly in the weak-record regime, with $`\delta_k:=(\theta_0-\theta_k)/2`$ and $`g`$ the plane-wave amplitude of the start:

```math
\frac{\mathrm d\bar x_{\rm lab}}{\mathrm d\lambda}=\int\frac{\mathrm dp}{2\pi}\lvert g\rvert^2\,\frac1N\sum_{k=0}^{N-1}\Bigl[\cos2\delta_k\,w_k-\sin2\delta_k\,\tau\cos p\,\cos\theta_k\,\cos(2\omega_k\lambda)\Bigr].
```

Eq. (5.25), the mean of $`v`$ over $`[0,\lambda]`$ with $`\lambda`$ of the order of the tick, to first order in $`\epsilon`$:

```math
\bar v:=\frac{\bar x(\lambda)-\bar x(0)}{\lambda}=\kappa\sigma_X\,\bar w(p_0)\,\hat e+\mathcal R_v,\qquad\bar w(p):=w(p;\bar\mu)=\frac{\tau^2\sin p\cos p}{\sqrt{\bar\mu^2+\tau^2\sin^2p}} .
```

Eq. (5.29), with $`\lVert\bar v\rVert`$ of (5.25) and $`R`$ of (5.22):

```math
R^2\Bigl(1-\frac{\lVert\bar v\rVert^2}{v_{\max}^2}\Bigr)=1+\frac{\tau^2}{\bar\mu^2}\sin^4p_0 .
```

From 03-ilang-space/17-motion@v2. Setting there: $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, $`C_b=\sum_{h,h'}t_{hh'}\lvert h\rangle\langle h'\rvert`$ with $`t_{hh'}=t_{h'h}^*`$; the start is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, $`\lvert u_h\rangle:=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$, $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$. Definitions fixed there, with $`p_h(\lambda)`$ the place weights of the view of $`b`$:

```math
\bar x(\lambda):=\sum_hp_h(\lambda)\,u_h,\qquad v(\lambda):=\frac{\mathrm d\bar x}{\mathrm d\lambda}.
```

Eq. (17.7), with $`W`$ the witness weight of the view of $`b`$, $`q_h:=\sqrt{p_h}`$, and $`a_{hh'}:=\lvert t_{hh'}\rvert d_0(h,h')`$ with largest eigenvalue $`\varrho(a)`$; the bound holds for every start and every $`\lambda`$:

```math
\lVert v(\lambda)\rVert\le\sum_{\{h,h'\}\in E}2\lvert t_{hh'}\rvert d_0(h,h')\sqrt{W(h,h';\lambda)p_hp_{h'}}\le\sum_{h,h'}a_{hh'}q_hq_{h'}\le v_{\max}:=\varrho(a)\le\max_h\sum_{h'}\lvert t_{hh'}\rvert\,d_0(h,h') .
```

Eq. (17.15), for the chain $`h_m`$, $`m\in\mathbb Z`$, with $`K_{h_m}=m\,X`$, $`X`$ self-adjoint on $`\mathcal H_c`$, $`\sigma_X:=(\langle X^2\rangle-\langle X\rangle^2)^{1/2}>0`$ and $`e:=(X-\langle X\rangle)\chi`$, so that $`\lVert e\rVert=\sigma_X`$ and $`u_{h_m}=m\,e`$:

```math
d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X,\qquad \bar x=\bar m\,e,\quad \bar m:=\sum_mm\,p_{h_m},\qquad s^2=\sigma_X^2\sum_m(m-\bar m)^2p_{h_m} .
```

From 03-ilang-space/16-common-space@v2. Setting there: objects $`a`$ (type $`A`$, places $`h`$), $`b`$ (type $`B`$, places $`k`$) and the medium $`c`$, of pairwise different types, each the only instance of its type; $`C=\sum_h\lvert h\rangle\langle h\rvert_a\otimes\mathbb 1_b\otimes K^A_h+\sum_k\mathbb 1_a\otimes\lvert k\rangle\langle k\rvert_b\otimes K^B_k`$; start $`\lvert\phi\rangle_a\otimes\lvert\vartheta\rangle_b\otimes\lvert\chi\rangle_c`$ with all $`\phi_h\neq0`$, $`\vartheta_k\neq0`$. Notation fixed there:
- $`\lvert u^A_h\rangle:=(K^A_h-\langle K^A_h\rangle)\lvert\chi\rangle`$, $`\lvert u^B_k\rangle:=(K^B_k-\langle K^B_k\rangle)\lvert\chi\rangle`$, $`g(v,w):=\mathrm{Re}\langle v\vert w\rangle`$, $`\mathcal N:=\{v\in\mathcal H_c:\langle\chi\vert v\rangle=0\}`$;
- $`X_A`$ and $`X_B`$ are the sets of leading-order points of the views of $`\{a\}`$ and $`\{b\}`$ (places with $`d_0=0`$ form one point), with record vectors $`u^A_x`$, $`u^B_y`$;
- a **correspondence** is a bijection $`\pi:D_A\to D_B`$ between subsets $`D_A\subseteq X_A`$, $`D_B\subseteq X_B`$ with $`\lvert D_A\rvert\ge2`$ such that, for all $`x,x'\in D_A`$, the joint places $`(h,k')`$ and $`(h',k)`$ have $`d_0=0`$ in the view of $`\{a,b\}`$, where $`h\in x`$, $`h'\in x'`$, $`k\in\pi(x)`$, $`k'\in\pi(x')`$.

Here body $`1`$ is the object $`a`$ and body $`2`$ is the object $`b`$.

Eq. (16.3), all replacements of the $`K`$'s that leave $`C`$ unchanged:

```math
K'^A_h=K^A_h+Z,\qquad K'^B_k=K^B_k-Z,\qquad Z=Z^\dagger\ \text{on }\mathcal H_c\ \text{arbitrary.}
```

Eq. (16.4), with the possible shifts being exactly the vectors $`z\in\mathcal N`$:

```math
u^A_h\mapsto u^A_h+z,\qquad u^B_k\mapsto u^B_k-z,\qquad \lvert z\rangle=(Z-\langle Z\rangle)\lvert\chi\rangle .
```

Eq. (16.11), "Hence $`\pi`$ is a correspondence iff"

```math
u^A_x-u^A_{x'}=u^B_{\pi(x)}-u^B_{\pi(x')}\ \ \forall x,x'\in D_A
\iff
\exists\,t_\pi\in\mathcal N:\ u^B_{\pi(x)}=u^A_x+t_\pi\ \ \forall x\in D_A .
```

"Under (16.4), $`t_\pi\mapsto t_\pi-2z`$".

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- **Weak records.** As in 05-moving-clock: work to leading order in $`\kappa`$ at fixed $`\lambda`$. The view of each body is then that of its own contract alone ($`C_{\rm D}+G`$ for body $`1`$, $`C_{\rm D}`$ for body $`2`$), and positions are measured in the background (17.15). State every place where this is used.
- **Starts.** As in 05-moving-clock: the weight of the start over the plane-wave label has mean $`p_0`$ (respectively $`0`$) and variance $`\delta p^2\ll1`$. "Leading order in the spread" means a remainder $`O(\delta p^2)`$.
- **Orders in $`\epsilon`$.** "To first order in $`\epsilon`$" means: at fixed $`N`$, $`\tau/m`$, $`p_0`$, $`\lambda/\lambda_0`$ and $`\mathcal F\lambda_0`$, with a remainder of relative order $`\epsilon^2`$. With $`\mathcal F\lambda_0`$ fixed, $`\mathcal F/m=\frac{N\epsilon}{2\pi}\mathcal F\lambda_0`$ is itself of first order.
- Standard facts on the motion of a plane-wave label under a uniform gradient, and on the adiabatic following of a branch separated from the other by a gap, may be used; state them with their conditions.

## Scope

- In scope:
  - one Model D body with a uniform gradient: label, displacement and clock reading;
  - the clock advance as a function of $`\lambda`$ and of the path;
  - two bodies with equal parameters, one with a gradient and one at rest, between two meetings.
- Out of scope:
  - two instances of the same type (Law 5), and bodies with different parameters (criterion 6, a separate package);
  - gradients that depend on $`\lambda`$, on the branch label or on the clock label;
  - transitions to the branch of negative eigenvalue, beyond the condition of item 1(a);
  - effects of the records beyond leading order in $`\kappa`$, and any effect of one body on the other through the medium;
  - any physical meaning of $`\lambda`$ beyond the definitions (M1); no relation of special relativity may be used as an input (M4).

## Depth

- Item 1: derive.
- Item 2: short argument.
- Item 3: derive; item 3(a): short argument.

## Expected result

- Item 1: a closed form for the label; a condition; a closed form for the displacement to the stated order; a distribution to the stated order with its remainder, and a yes/no answer with a function; a yes/no answer.
- Item 2: a relation in the two stated forms; a functional of the path.
- Item 3: a closed form; a set of values of $`\lambda`$; closed forms or one-dimensional integrals; an inequality with its case of equality, and a yes/no answer; a leading-order expression; conditions and two values.

Give every main result a tag $`(9.k)`$.

Consistency checks, at most three: for example $`\mathcal F\to0`$ at fixed $`\lambda`$, $`p_0=0`$, and $`\tau\to0`$.

## Code

None.
