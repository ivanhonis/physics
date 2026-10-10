# Question: 08-maximal-speed

- **Subproject:** 04-ilang-time
- **Package:** 08-maximal-speed
- **Equation tags:** (8.k)
- **Created:** 2026-10-10

## Goal

Determine whether the maximal speed is the same for bodies of all types, the conditions under which it is, and what a common maximal speed means for the relations of 05-moving-clock and 06-inertia-internal-energy. This is criterion 6.

**Setting.** That of 03-ilang-space/16-common-space (two types recorded by one medium, quoted under "Inputs"), with a body contract for each of the two objects, as in 03-ilang-space/17-motion.
- **Objects.** $`a`$ of type $`A`$ with places $`h\in H_A`$, $`b`$ of type $`B`$ with places $`k\in H_B`$, and the medium $`c`$. The three types are pairwise different, and each object is the only instance of its type.
- **Contract.**
  ```math
  C=C_A\otimes\mathbb 1_b\otimes\mathbb 1_c+\mathbb 1_a\otimes C_B\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert_a\otimes\mathbb 1_b\otimes K^A_h+\sum_k\mathbb 1_a\otimes\lvert k\rangle\langle k\rvert_b\otimes K^B_k ,
  ```
  with $`C_A=\sum_{h,h'}t^A_{hh'}\lvert h\rangle\langle h'\rvert`$ and $`C_B=\sum_{k,k'}t^B_{kk'}\lvert k\rangle\langle k'\rvert`$ self-adjoint, and $`K^A_h`$, $`K^B_k`$ self-adjoint on $`\mathcal H_c`$. There is no contract between $`a`$ and $`b`$.
- **Start.** $`\lvert\phi\rangle_a\otimes\lvert\vartheta\rangle_b\otimes\lvert\chi\rangle_c`$.
- **Record vectors and distances.** $`u^A_h`$, $`u^B_k`$ and $`g`$ as in 16-common-space; $`d^a_0(h,h'):=\lVert u^A_h-u^A_{h'}\rVert`$ and $`d^b_0(k,k'):=\lVert u^B_k-u^B_{k'}\rVert`$, as in (16.8).
- **Positions and velocities.** With the place weights $`p^a_h(\lambda)`$ and $`p^b_k(\lambda)`$ of the views of $`a`$ and of $`b`$, the definitions of 17-motion are applied to each body:
  ```math
  \bar x_a(\lambda):=\sum_hp^a_h(\lambda)\,u^A_h,\quad v_a(\lambda):=\frac{\mathrm d\bar x_a}{\mathrm d\lambda},\qquad \bar x_b(\lambda):=\sum_kp^b_k(\lambda)\,u^B_k,\quad v_b(\lambda):=\frac{\mathrm d\bar x_b}{\mathrm d\lambda}.
  ```
- **Maximal speed of a type.** $`v^A_{\max}:=\varrho(a^A)`$, the largest eigenvalue of the matrix $`a^A_{hh'}:=\lvert t^A_{hh'}\rvert\,d^a_0(h,h')`$; likewise $`v^B_{\max}:=\varrho(a^B)`$ with $`a^B_{kk'}:=\lvert t^B_{kk'}\rvert\,d^b_0(k,k')`$. This is $`v_{\max}`$ of (17.7), built for each body from its own contract and its own records.

1. **Two bodies in one medium.**
   - (a) Determine all replacements of the diagonal entries $`t^A_{hh}`$, $`t^B_{kk}`$ and of the operators $`K^A_h`$, $`K^B_k`$ that leave $`C`$ unchanged. Determine how $`\bar x_a`$, $`\bar x_b`$, $`v_a`$, $`v_b`$, $`v^A_{\max}`$ and $`v^B_{\max}`$ change under them and under a change of the phase of $`\chi`$.
   - (b) Determine which of the following are well defined (M6): $`\lVert v_a\rVert`$, $`\lVert v_b\rVert`$, $`g(v_a,v_b)`$, $`\lVert v_a-v_b\rVert`$, $`\bar x_a-\bar x_b`$, and $`v^A_{\max}/v^B_{\max}`$.
   - (c) Determine whether $`\lVert v_a(\lambda)\rVert\le v^A_{\max}`$ holds in this setting for every product start and every $`\lambda\ge0`$. Determine whether $`v^A_{\max}`$ depends on $`C_B`$, on the $`K^B_k`$ or on $`\vartheta`$.

2. **Are the maximal speeds of two types equal?**
   - (a) **Chain types.** Each type is a chain as in (17.20): type $`A`$ with hopping $`t_A>0`$ and records $`K^A_{h_m}=m\,X_A`$, type $`B`$ with $`t_B>0`$ and $`K^B_{k_n}=n\,X_B`$, where $`X_A`$, $`X_B`$ are self-adjoint on $`\mathcal H_c`$ with $`\sigma_{X_A},\sigma_{X_B}>0`$. Determine $`v^A_{\max}`$ and $`v^B_{\max}`$, and the necessary and sufficient condition for $`v^A_{\max}=v^B_{\max}`$.
   - (b) **Model D types.** Each type is a Model D body of 05-moving-clock (quoted under "Inputs"), with its own parameters: $`\tau_A`$, $`m_A`$, $`N_A`$, $`\lambda_{0A}`$, $`\kappa_A`$, $`X_A`$ for type $`A`$, and $`\tau_B`$, $`m_B`$, $`N_B`$, $`\lambda_{0B}`$, $`\kappa_B`$, $`X_B`$ for type $`B`$. Determine $`v^A_{\max}`$ and $`v^B_{\max}`$, and the necessary and sufficient condition for $`v^A_{\max}=v^B_{\max}`$.
   - (c) Determine whether Laws 1–5 of Ilanguage 1.b and A1–A9 imply $`v^A_{\max}=v^B_{\max}`$ for two types recorded by one medium.
   - (d) **Common points.** In (a) and in (b), let the two chains have the same finite number of positions, and let a correspondence with $`D_A=X_A`$ and $`D_B=X_B`$ exist (16.13). Determine what this implies for the records of the two types, and the condition for $`v^A_{\max}=v^B_{\max}`$ in that case.

3. **What a common maximal speed means.** Two Model D types as in item 2(b), in the weak-record regime for both bodies.
   - (a) State why, in this regime, the results of 05-moving-clock and of 06-inertia-internal-energy quoted below apply to each of the two bodies in the presence of the other.
   - (b) **Moving clocks.** Let each body carry its clock as in item 3 of 05-moving-clock, and let $`\bar v_a`$, $`\bar v_b`$ be the drift velocities (5.25) of the two clock-carrying starts, and $`R_A`$, $`R_B`$ their tick ratios (5.22). For $`\lVert\bar v_a\rVert=\lVert\bar v_b\rVert`$, determine $`R_A-R_B`$ to leading order for small plane-wave labels. Determine the necessary and sufficient condition on the parameters of the two types under which, to this order, the tick ratio is the same function of the drift speed for both types. Determine whether, under this condition, the relations (5.29) of the two types agree as well.
   - (c) **Inertia.** For each type and each clock level, express the background inertia (6.20) through the rest cost (6.7) and the maximal speed of the type. Determine the necessary and sufficient condition under which the relation between background inertia and rest cost is the same for both types.
   - (d) Determine how the conditions of (b) and (c) are related to $`v^A_{\max}=v^B_{\max}`$.

## Inputs

From 03-ilang-space/16-common-space@v2. Setting there: objects $`a`$ (type $`A`$, places $`h`$), $`b`$ (type $`B`$, places $`k`$) and the medium $`c`$, of pairwise different types, each the only instance of its type; $`C=\sum_h\lvert h\rangle\langle h\rvert_a\otimes\mathbb 1_b\otimes K^A_h+\sum_k\mathbb 1_a\otimes\lvert k\rangle\langle k\rvert_b\otimes K^B_k`$; start $`\lvert\phi\rangle_a\otimes\lvert\vartheta\rangle_b\otimes\lvert\chi\rangle_c`$ with all $`\phi_h\neq0`$, $`\vartheta_k\neq0`$. Notation fixed there:
- $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, $`\lvert u^A_h\rangle:=(K^A_h-\langle K^A_h\rangle)\lvert\chi\rangle`$, $`\lvert u^B_k\rangle:=(K^B_k-\langle K^B_k\rangle)\lvert\chi\rangle`$, $`g(v,w):=\mathrm{Re}\langle v\vert w\rangle`$, $`\mathcal N:=\{v\in\mathcal H_c:\langle\chi\vert v\rangle=0\}`$;
- $`X_A`$ and $`X_B`$ are the sets of leading-order points of the views of $`\{a\}`$ and $`\{b\}`$ (places with $`d_0=0`$ form one point), with record vectors $`u^A_x`$, $`u^B_y`$; $`U_A:=\{u^A_h\}`$ and $`U_B:=\{u^B_k\}`$ are the sets of record vectors;
- a **correspondence** is a bijection $`\pi:D_A\to D_B`$ between subsets $`D_A\subseteq X_A`$, $`D_B\subseteq X_B`$ with $`\lvert D_A\rvert\ge2`$ such that, for all $`x,x'\in D_A`$, the joint places $`(h,k')`$ and $`(h',k)`$ have $`d_0=0`$ in the view of $`\{a,b\}`$, where $`h\in x`$, $`h'\in x'`$, $`k\in\pi(x)`$, $`k'\in\pi(x')`$.

Eq. (16.3), all replacements of the $`K`$'s that leave the $`C`$ of that setting unchanged:

```math
K'^A_h=K^A_h+Z,\qquad K'^B_k=K^B_k-Z,\qquad Z=Z^\dagger\ \text{on }\mathcal H_c\ \text{arbitrary.}
```

Eq. (16.4), with the possible shifts being exactly the vectors $`z\in\mathcal N`$; under a change of the phase of $`\chi`$, every record vector is multiplied by the same phase factor:

```math
u^A_h\mapsto u^A_h+z,\qquad u^B_k\mapsto u^B_k-z,\qquad \lvert z\rangle=(Z-\langle Z\rangle)\lvert\chi\rangle .
```

Eq. (16.8), the leading-order distances of the views of $`\{a\}`$ and of $`\{b\}`$:

```math
d_0^{a}(h,h')=\lVert u^A_h-u^A_{h'}\rVert,\qquad d_0^{b}(k,k')=\lVert u^B_k-u^B_{k'}\rVert,
```

Eq. (16.11), "Hence $`\pi`$ is a correspondence iff"

```math
u^A_x-u^A_{x'}=u^B_{\pi(x)}-u^B_{\pi(x')}\ \ \forall x,x'\in D_A
\iff
\exists\,t_\pi\in\mathcal N:\ u^B_{\pi(x)}=u^A_x+t_\pi\ \ \forall x\in D_A .
```

Eq. (16.13), with the centroids $`\bar u^A:=\lvert X_A\rvert^{-1}\sum_{x\in X_A}u^A_x`$ and $`\bar u^B:=\lvert X_B\rvert^{-1}\sum_{y\in X_B}u^B_y`$: a correspondence with $`D_A=X_A`$ and $`D_B=X_B`$ exists iff

```math
\lvert X_A\rvert\ge2\ \text{ and }\ U_B=U_A+t\ \text{for some }t\in\mathcal N
\iff
\lvert X_A\rvert=\lvert X_B\rvert\ge2\ \text{ and }\ U_A-\bar u^A=U_B-\bar u^B ,
```

"and it is then **unique**."

From 03-ilang-space/17-motion@v2. Setting there: one body $`b`$ and a medium $`c`$, $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, $`C_b=\sum_{h,h'}t_{hh'}\lvert h\rangle\langle h'\rvert`$ with $`t_{hh'}=t_{h'h}^*`$; the hopping graph joins $`h\neq h'`$ iff $`t_{hh'}\neq0`$, and $`E`$ is its set of edges; the start is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`\lvert u_h\rangle:=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$, $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$; $`V_b`$ is the view of $`b`$ and $`\lvert\psi_h\rangle:=(\langle h\rvert\otimes\mathbb 1)\lvert\Psi\rangle`$, so that $`(V_b)_{h'h}=\langle\psi_h\vert\psi_{h'}\rangle`$ and $`p_h=\lVert\psi_h\rVert^2`$. Definitions fixed there, with $`p_h(\lambda)`$ the place weights of the view of $`b`$:

```math
\bar x(\lambda):=\sum_hp_h(\lambda)\,u_h,\qquad v(\lambda):=\frac{\mathrm d\bar x}{\mathrm d\lambda}.
```

Eq. (17.4), the currents:

```math
\frac{\mathrm dp_h}{\mathrm d\lambda}=\sum_{h'}J_{h'\to h},\qquad J_{h'\to h}(\lambda):=2\mathrm{Im}\bigl[t_{hh'}\,(V_b(\lambda))_{h'h}\bigr]=-J_{h\to h'} .
```

Eq. (17.7), with $`W`$ the witness weight of the view of $`b`$, $`q_h:=\sqrt{p_h}`$, and $`a_{hh'}:=\lvert t_{hh'}\rvert d_0(h,h')`$ with largest eigenvalue $`\varrho(a)`$; in the setting of 17 the bound holds for every start and every $`\lambda`$:

```math
\lVert v(\lambda)\rVert\le\sum_{\{h,h'\}\in E}2\lvert t_{hh'}\rvert d_0(h,h')\sqrt{W(h,h';\lambda)p_hp_{h'}}\le\sum_{h,h'}a_{hh'}q_hq_{h'}\le v_{\max}:=\varrho(a)\le\max_h\sum_{h'}\lvert t_{hh'}\rvert\,d_0(h,h') .
```

Eq. (17.15), for the chain $`h_m`$, $`m\in\mathbb Z`$, with $`K_{h_m}=m\,X`$, $`X`$ self-adjoint on $`\mathcal H_c`$, $`\sigma_X:=(\langle X^2\rangle-\langle X\rangle^2)^{1/2}>0`$ and $`e:=(X-\langle X\rangle)\chi`$, so that $`\lVert e\rVert=\sigma_X`$ and $`u_{h_m}=m\,e`$:

```math
d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X,\qquad \bar x=\bar m\,e,\quad \bar m:=\sum_mm\,p_{h_m},\qquad s^2=\sigma_X^2\sum_m(m-\bar m)^2p_{h_m} .
```

Eq. (17.20), the bound (17.7) for the chain with $`C_b=t\sum_m(\lvert h_m\rangle\langle h_{m+1}\rvert+\lvert h_{m+1}\rangle\langle h_m\rvert)`$, $`t>0`$:

```math
v_{\max}=2t\,\sigma_X .
```

From 05-moving-clock@v3 (this subproject). **Model D**: one body with places $`(x,s,a)`$, $`x\in\mathbb Z`$ (position label, as the limit of long finite chains), $`s\in\{1,2\}`$ (branch label), $`a\in\mathbb Z_N`$ (clock label), with the contract
```math
C_b=A+B,\qquad A=\frac\tau2\sum_x\Bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\Bigr)\otimes\mathbb 1_N,\qquad B=\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m\mathbb 1_N+D),
```
$`\tau>0`$, $`m>0`$, $`D=\frac{2\pi}{N\lambda_0}\sum_{k=0}^{N-1}k\lvert f_k\rangle\langle f_k\rvert`$ with $`\lvert f_k\rangle=N^{-1/2}\sum_ae^{2\pi ika/N}\lvert a\rangle`$ and eigenvalues $`d_k=\frac{2\pi k}{N\lambda_0}`$, and the records $`K_x=\kappa\,x\,X`$, $`\kappa>0`$, $`X`$ as in (17.15). Notation fixed there:
- $`\mu_k:=m+d_k`$, $`\epsilon:=\frac{2\pi}{N\lambda_0m}`$, $`\hat e:=e/\sigma_X`$;
- the plane-wave label $`p_0`$ near which a start is concentrated;
- $`\bar\mu:=m+\langle0\vert D\vert0\rangle=m+\frac{\pi(N-1)}{N\lambda_0}`$, $`\bar\omega(p):=\sqrt{\bar\mu^2+\tau^2\sin^2p}`$, $`\Gamma(p):=\bar\mu/\bar\omega(p)`$, $`\bar W:=\sqrt{\bar\mu^2+\tau^2}`$;
- the **weak-record regime**: leading order in $`\kappa`$ at fixed $`\lambda`$; the view of the body is then that of $`C_b`$ alone, and positions are measured in the background (17.15);
- the **clock-carrying start** (item 3 there): concentrated near $`p_0`$, in the branch of positive eigenvalue, with the clock label in the place $`\lvert0\rangle`$.

Eq. (5.11), the bound (17.7) for this $`C_b`$:

```math
v_{\max}=\tau\,\kappa\sigma_X=\max_h\sum_{h'}\lvert t_{hh'}\rvert\,d_0(h,h') .
```

Eq. (5.22), the tick of the clock-carrying start and its ratio to the tick at $`p_0=0`$, to first order in $`\epsilon`$, with $`\omega:=\sqrt{m^2+\tau^2\sin^2p_0}`$:

```math
\lambda_0(p_0)=\frac{\lambda_0}{\Gamma(p_0)},\qquad
R(p_0):=\frac{\lambda_0(p_0)}{\lambda_0(0)}=\frac{\bar\omega(p_0)}{\bar\mu}=\sqrt{1+\frac{\tau^2}{\bar\mu^2}\sin^2p_0}=\frac\omega m\Bigl[1-\frac{(N-1)\epsilon}2\,\frac{\tau^2\sin^2p_0}{\omega^2}\Bigr]+O\bigl((N\epsilon)^2\bigr)\ \ge1 .
```

Eq. (5.25), the drift velocity of the clock-carrying start: the mean of $`v`$ over $`[0,\lambda]`$ with $`\lambda`$ a tick or longer, to first order in $`\epsilon`$:

```math
\bar v:=\frac{\bar x(\lambda)-\bar x(0)}{\lambda}=\kappa\sigma_X\,\bar w(p_0)\,\hat e+\mathcal R_v,\qquad\bar w(p):=w(p;\bar\mu)=\frac{\tau^2\sin p\cos p}{\sqrt{\bar\mu^2+\tau^2\sin^2p}} .
```

Eq. (5.28), for the drift velocity $`\bar v`$ of (5.25) and small $`p_0`$, with $`v_{\rm top}:=\kappa\sigma_X(\bar W-\bar\mu)`$:

```math
R=1+\frac{\lVert\bar v\rVert^2}{2v_{\max}^2}+O(p_0^4)=1+\frac{\bar W-\bar\mu}{2(\bar W+\bar\mu)}\,\frac{\lVert\bar v\rVert^2}{v_{\rm top}^2}+O(p_0^4).
```

Eq. (5.29), for the drift velocity $`\bar v`$ of (5.25):

```math
R^2\Bigl(1-\frac{\lVert\bar v\rVert^2}{v_{\max}^2}\Bigr)=1+\frac{\tau^2}{\bar\mu^2}\sin^4p_0 .
```

The relations (5.28) and (5.29) hold up to terms of second order in $`\epsilon`$, $`O(\delta p^2)`$ in the spread $`\delta p`$ of the start, and $`O(\kappa)`$.

From 06-inertia-internal-energy@v3 (this subproject). Setting there: one Model D body as above, with a uniform cost gradient added through its diagonal entries $`t_{hh}`$, with force $`F\in\mathcal H_c`$; the start is concentrated near the plane-wave label $`0`$, in the branch of positive eigenvalue, with clock level $`k`$ (clock label in $`\lvert f_k\rangle`$); weak-record regime. Notation fixed there:
- the acceleration $`a:=\mathrm d^2\bar x/\mathrm d\lambda^2`$, and $`\mathcal F:=\kappa\,g(e,F)`$, the force on the position label;
- the **averaged inverse inertia** $`\mu_{\rm av}(k)`$: the coefficient of $`F`$ in the average of $`a(\lambda)`$ over $`\lambda`$-intervals that are long compared with the inverse of the gap between the two branches, at first order in $`F`$ and leading order in $`\kappa`$;
- $`n:=e/\sigma_X`$ and $`d_1:=\kappa\sigma_X`$, the background distance of neighbouring points; $`\bar m`$ is the mean position label.

Eq. (6.7), the rest cost of clock level $`k`$: the positive eigenvalue of $`C_b`$ on the plane wave with label $`0`$ and clock level $`k`$:

```math
M_k:=m+d_k=m+\frac{2\pi k}{N\lambda_0}\ \ (\text{rest cost of level }k,\ \text{eigenvector }\lvert1\rangle),\qquad\text{gap }2M_k,\qquad \omega_k''(0)=\frac{\tau^2}{M_k}.
```

Eq. (6.15):

```math
\mu_{\rm av}(k)=\frac{\tau^2}{M_k}\,\kappa^2\,e\,g(e,\cdot\,)=\frac{\tau^2}{m+d_k}\,\kappa^2\,e\,g(e,\cdot\,).
```

Eq. (6.16):

```math
M_k\,\mu_{\rm av}(k)=\tau^2\kappa^2\,e\,g(e,\cdot\,)\ \ \text{for every }k,\qquad \frac{M_k}{\tau^2}=\frac{m}{\tau^2}+\frac{2\pi k}{N\lambda_0\,\tau^2}.
```

Eq. (6.20), the background inertia $`I_k`$ and the label inertia $`I_k^{\rm lab}`$:

```math
\mu_{\rm av}(k)=\frac{1}{I_k}\,n\,g(n,\cdot\,),\qquad
I_k:=\frac{M_k}{\tau^2\kappa^2\sigma_X^2}=\frac{I_k^{\rm lab}}{d_1^{\,2}},\qquad
I_k^{\rm lab}:=\frac{M_k}{\tau^2}\quad\bigl(\overline{\ddot{\bar m}}=\mathcal F/I_k^{\rm lab}\bigr).
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- No object other than $`a`$ has the type of $`a`$, none other than $`b`$ the type of $`b`$, and $`c`$ is the only instance of its type.
- Chains on $`\mathbb Z`$ are limits of long finite chains (A1), as in the quoted packages; item 2(d) uses finite chains.
- Item 3 uses the weak-record regime of 05-moving-clock and 06-inertia-internal-energy for both bodies, and their orders of approximation. State every place where they are used.

## Scope

- In scope:
  - two bodies of different types recorded by one medium, each with its own body contract;
  - which comparisons of their velocities and maximal speeds are well defined;
  - the maximal speeds of chain types and of Model D types, and the conditions for their equality;
  - the consequences for the tick ratio and for the inertia of Model D types.
- Out of scope:
  - contracts between the two bodies, several media, and identical instances (Law 5);
  - the speed of the influence between readings (07-causal-order) and its relation to the maximal speed;
  - any mechanism that would select the parameters of the types;
  - effects of the records beyond leading order in $`\kappa`$;
  - any physical meaning of $`\lambda`$ beyond the definitions (M1); no relation of special relativity may be used as an input (M4).

## Depth

- Item 1: derive.
- Item 2: short argument.
- Item 3: short argument.

## Expected result

- Item 1: the general form of the replacements and the transformation of each quantity; a list of well-defined quantities; two yes/no answers with reasons.
- Item 2: closed forms and an equivalence, for each family; a yes/no answer with a reason; a condition.
- Item 3: a reason; a leading-order expression, an equivalence and a yes/no answer; a closed form and an equivalence; a statement of the relation.

Give every main result a tag $`(8.k)`$.

Consistency checks, at most three: for example equal parameters of the two types, the exchange of $`a`$ and $`b`$, and a common rescaling of $`\kappa`$ and $`X`$ that leaves the records unchanged.

## Code

None.
