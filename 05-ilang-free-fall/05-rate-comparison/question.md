# Question: 05-rate-comparison

- **Subproject:** 05-ilang-free-fall
- **Package:** 05-rate-comparison
- **Equation tags:** (5.k)
- **Created:** 2026-10-10

## Goal

Determine when the relation between the rates of clocks at two places can be detected through readings, in the sense of 10-global-order of 04-ilang-time, extended from two parts to classes of places: for one body whose positions are connected by hopping, for a body that cannot move, for two bodies that are recorded by a common medium, and for the comparison of two runs used in 03-clock-and-fall. This is the part of criterion 2 that concerns the comparison of the rates at two places.

**Setting.**
- **Objects.** Finitely many objects $`o=1,\dots,n`$ of pairwise different types, each the only instance of its type, so $`\mathcal H_{\rm adm}=\mathcal H=\bigotimes_o\mathcal H_o`$; $`H_o`$ is the place set of the object $`o`$.
- **Contract.** $`C`$ is self-adjoint, independent of $`\lambda`$ and a sum of pair terms (A5).
- **Start.** A unit vector $`\Psi_0`$ at $`\lambda=0`$; only $`\lambda\ge0`$ is used.
- **Classes.** For every object $`o`$ the place set $`H_o`$ is divided into nonempty disjoint **blocks**. Every block is a **class** $`\ell`$, with its object $`o(\ell)`$ and its block $`B_\ell\subseteq H_{o(\ell)}`$. An object with one block is one class. A **place projector of the class $`\ell`$** is $`\Pi_S=\sum_{h\in S}\lvert h\rangle\langle h\rvert`$ on $`\mathcal H_{o(\ell)}`$, extended by the identity, for a set $`S\subseteq B_\ell`$.
- **Readings.** A **reading of the class $`\ell`$** is a partition of $`H_{o(\ell)}`$ in which the places outside $`B_\ell`$, if there are any, form one class, and $`B_\ell`$ is divided into classes in any way. It is applied directly at a stated value of $`\lambda`$ (A8), not represented by a record object.
- **Schedule.** A finite list of events $`e_j=(\ell_j,R_j,\lambda_j)`$: a class, a reading of that class, and a value $`\lambda_j\ge0`$. The readings are applied by (1.3) in the order of increasing $`\lambda_j`$, with the evolution (1.9) between them, as in (10.1). The statistics of the schedule is the joint distribution of its outcomes.
- **Re-timing.** A number $`a_\ell>0`$ for every class, and a contract $`C'`$ on the same objects (self-adjoint, independent of $`\lambda`$, a sum of pair terms). The re-timed schedule has the same events with $`\lambda_j`$ replaced by $`a_{\ell_j}\lambda_j`$.
- **Equivalence.** A re-timing $`((a_\ell),C')`$ is an **equivalence of $`C`$** if, for every start and every schedule, the statistics of the re-timed schedule under $`C'`$ equal the statistics of the original schedule under $`C`$.
- **Classes that are not read.** Unless an item says otherwise, events of every class may occur. If an item declares some classes **not read**, schedules contain no event of these classes, and no factor is assigned to them.
- **Detectable.** For a given $`C`$, the **relative factor** of two classes $`\ell,\ell'`$ is detectable if every equivalence of $`C`$ has $`a_\ell=a_{\ell'}`$.
- **Readings with one outcome per block.** A reading of an object with one outcome per block (for a body with the blocks of its positions: a position reading) is not a reading of one class. In a schedule it is represented by the readings "in the block or not" of all blocks at one value of $`\lambda`$; state why this gives the same statistics and the same state after the reading, and what a re-timing with different factors does to it.

1. **Equivalences for classes.** Every class is read.
   - (a) Determine the necessary and sufficient conditions on $`((a_\ell),C')`$ for an equivalence of a general $`C`$, in terms of commutators of $`C`$ and $`C'`$ with the place projectors of the classes. State where the proof uses that the place projectors of the classes generate all operators that are diagonal in the joint places, and that $`C'`$ is a sum of pair terms.
   - (b) Determine conditions on the matrix elements of $`C`$ in the joint places under which two classes have equal factors in every equivalence: for two classes of one object, and for two classes of different objects.
   - (c) Let $`\mathcal G`$ be a set of classes and $`\alpha\neq\alpha'`$ two positive numbers. Determine the necessary and sufficient condition on $`C`$ for the existence of an equivalence with $`a_\ell=\alpha`$ for $`\ell\in\mathcal G`$ and $`a_\ell=\alpha'`$ for all other classes, and the contract $`C'`$ of such an equivalence. Determine how much freedom $`C'`$ has when all factors are equal.

2. **One body on a chain.** A body $`b`$ of the class $`\mathcal C`$ of 03-clock-and-fall (quoted under "Inputs", with arbitrary profiles $`m_x>0`$, $`\eta_x>0`$, $`\zeta_x\ge0`$, $`V_x`$) on a finite chain $`\lvert x\rvert\le L`$, and a medium $`c`$ with the records $`K_x=\kappa\,x\,X`$, $`\kappa>0`$, $`X`$ self-adjoint on $`\mathcal H_c`$ and not a multiple of $`\mathbb 1_c`$. The classes are the positions of the body (the block of $`x`$ consists of the places $`(x,s,a)`$) and the medium as one class.
   - (a) $`\tau>0`$ and $`\zeta_x>0`$ on every bond. Determine all equivalences when the medium is read, separately for an $`X`$ that is diagonal in the places of the medium and for one that is not. Determine which relative factors of positions are detectable when the medium is not read.
   - (b) No hopping, $`\tau=0`$. Determine the same. Determine whether an equivalence exists whose contract $`C'`$ is again of the class $`\mathcal C`$ with a clock profile that does not depend on the position.
   - (c) In (a) and in (b), with $`C`$ and $`C'`$ both written in the form of the class $`\mathcal C`$, determine which of the following are the same for $`C`$ and for the contract of every equivalence: $`\eta_x/\eta_y`$ for two positions; $`m_x/\eta_x`$; $`\tau\zeta_x/\eta_x`$; $`(V_x-V_y)/\eta_x`$; the tick $`\lambda_0/\eta_x`$.

3. **Two bodies and a common medium.** Two bodies $`b_1`$, $`b_2`$ of different types with arbitrary self-adjoint body contracts $`C_1`$, $`C_2`$, position labels $`x`$ with $`\hat x_i:=\sum_xx\,P^{(i)}_x`$, no contract between the bodies, and one medium $`c`$ that records both through the same operator: $`C=C_1+C_2+\kappa_1\,\hat x_1\otimes X+\kappa_2\,\hat x_2\otimes X`$, with $`\kappa_1,\kappa_2>0`$ and $`X`$ self-adjoint on $`\mathcal H_c`$. Each object is one class.
   - (a) All three objects are read. Determine the equivalences, and the conditions on $`X`$ and on $`C_1`$, $`C_2`$ under which the relative factor of the two bodies is detectable.
   - (b) The medium is not read. Determine whether an equivalence with $`a_1\neq a_2`$ exists, for every $`\kappa_1`$, $`\kappa_2`$ and $`X`$; if it does, give its contract.
   - (c) Let each body carry a clock. For a schedule that reads the clock label of $`b_1`$ at $`\lambda_1`$ and the clock label of $`b_2`$ at $`\lambda_2`$, determine how the pair $`(\lambda_1,\lambda_2)`$ and the parameters of the two body contracts change under an equivalence of (b). State what follows for a comparison of the two clocks that pairs their readings at equal $`\lambda`$, and for a statement that two types have equal parameters.

4. **Two runs.** In 03-clock-and-fall the rates at two positions $`x_1`$, $`x_2`$ are taken from two runs of one description (starts $`S_{\rm clock}(x_1)`$ and $`S_{\rm clock}(x_2)`$), with the clock read at the same $`\lambda`$ in both, (3.24). Determine whether the wide-start ratio $`\eta_{x_1}/\eta_{x_2}`$ of (3.24) is the same in every description that is equivalent in the sense of item 2: (a) for $`\tau>0`$, (b) for $`\tau=0`$. State what the comparison of two runs relies on (A8), and whether it is a comparison of two events of one schedule.

## Inputs

From 10-global-order@v2 of 04-ilang-time. Setting there: finitely many objects of pairwise different types, divided into two nonempty disjoint parts $`\mathcal P_1`$, $`\mathcal P_2`$, $`\mathcal H=\mathcal H_1\otimes\mathcal H_2`$; $`C`$ self-adjoint, independent of $`\lambda`$ and a sum of pair terms; a start $`\Psi_0`$ at $`\lambda=0`$, only $`\lambda\ge0`$; readings applied at stated values of $`\lambda`$; a local reading on a part is a partition of the joint places of that part. Definitions fixed there:
- a **schedule** is a finite list of events $`e_k=(i_k,R_k,\lambda_k)`$ with a part index, a local reading on that part and a value of $`\lambda`$; its statistics is the joint distribution of the outcomes;
- a **re-timing** is $`(a_1,a_2,C')`$ with $`a_1,a_2>0`$ and a contract $`C'`$ of the same kind; it replaces $`\lambda_k`$ by $`a_{i_k}\lambda_k`$; it is an **equivalence of $`C`$** if, for every start and every schedule, the statistics of the re-timed schedule under $`C'`$ equal those of the original schedule under $`C`$; the **common now** is detectable if every equivalence has $`a_1=a_2`$;
- $`h,h'`$ are the joint places of $`\mathcal P_1`$ and $`r,r'`$ those of $`\mathcal P_2`$; $`X_{hr,h'r'}:=\langle hr\vert X\vert h'r'\rangle`$; a place projector of $`\mathcal P_1`$ is $`\Pi=\sum_{h\in S}\lvert h\rangle\langle h\rvert\otimes\mathbb 1`$, of $`\mathcal P_2`$ it is $`\Pi'=\mathbb 1\otimes\sum_{r\in S'}\lvert r\rangle\langle r\rvert`$; $`X(\lambda):=e^{iC\lambda}Xe^{-iC\lambda}`$;
- every operator is decomposed by the kind of transition, $`X=X^{\rm d}+X^{(1)}+X^{(2)}+X^{(12)}`$: the elements $`X_{hr,h'r'}`$ with ($`h=h'`$, $`r=r'`$), ($`h\neq h'`$, $`r=r'`$), ($`h=h'`$, $`r\neq r'`$), ($`h\neq h'`$, $`r\neq r'`$).

Eq. (10.1), with the events numbered so that $`\lambda_1\le\dots\le\lambda_K`$ and $`\Pi^{(k)}_{s_k}`$ the class projector of the outcome $`s_k`$ of $`R_k`$:

```math
P(s_1,\dots,s_K)=\bigl\lVert\Pi^{(K)}_{s_K}(\lambda_K)\cdots\Pi^{(1)}_{s_1}(\lambda_1)\,\Psi_0\bigr\rVert^2 .
```

Eq. (10.5): $`C`$ is **split** if there are self-adjoint $`F_1,F_2`$ with the following, for every place projector $`\Pi`$ of $`\mathcal P_1`$ and $`\Pi'`$ of $`\mathcal P_2`$; a split is a **pair-term split** if $`F_1`$ and $`F_2`$ are sums of pair terms:

```math
C=F_1+F_2,\qquad [F_1,F_2]=0,\qquad [F_1,\Pi']=0,\qquad [F_2,\Pi]=0
```

Eq. (10.6), for a split $`C`$; the second statement holds provided the split is a pair-term split:

```math
[\Pi(\lambda),\Pi'(\lambda')]=0,\qquad\bigl(a_1,\,a_2,\,F_1/a_1+F_2/a_2\bigr)\ \text{is an equivalence of } C\ \text{ for all } a_1,a_2>0 .
```

Eq. (10.7), for uncoupled parts, $`C=C_1\otimes\mathbb 1+\mathbb 1\otimes C_2`$, and every start:

```math
\Bigl(a_1,\,a_2,\,\tfrac1{a_1}C_1\otimes\mathbb 1+\tfrac1{a_2}\mathbb 1\otimes C_2\Bigr)\ \text{is an equivalence for all } a_1,a_2>0 .
```

Eq. (10.13), the first-order conditions from schedules with a single event; "(10.10)" in it is the condition $`[\,C-a_iC',\Pi\,]=0`$ for all place projectors $`\Pi`$ of $`\mathcal P_i`$, and $`C'^{\rm d}`$ is the diagonal part of $`C'`$:

```math
\text{(10.10) for both parts}\iff C'^{(1)}=\frac{C^{(1)}}{a_1},\quad C'^{(2)}=\frac{C^{(2)}}{a_2},\quad C'^{(12)}=\frac{C^{(12)}}{a_1}=\frac{C^{(12)}}{a_2};\qquad C'^{\rm d}\ \text{free (real diagonal)}.
```

Eq. (10.14), exact, for every $`C`$ and every re-timing $`(a_1,a_2,C')`$ with $`C'`$ a sum of pair terms:

```math
(a_1,a_2,C')\ \text{is an equivalence of } C\iff[\,C-a_iC',\Pi\,]=0\ \text{for all place projectors }\Pi\text{ of }\mathcal P_i\ (i=1,2)\ \text{ and }\ [C,C']=0 .
```

Eq. (10.15):

```math
(a,a,C')\ \text{is an equivalence of } C\iff C'=C/a+D,\ \ D\ \text{real diagonal in the joint places and a sum of pair terms (A5)},\ \ [C,D]=0 .
```

Eq. (10.16):

```math
C^{(12)}\neq0\quad\text{or}\quad[C^{(1)},C^{(2)}]\neq0\qquad\Longrightarrow\qquad\text{every equivalence has } a_1=a_2 :\ \text{the common now is detectable.}
```

From 03-clock-and-fall@v3 (this subproject). Setting there: one body $`b`$ of the class $`\mathcal C`$ and a medium $`c`$ with the records $`K_x=\kappa\,x\,X`$. The class $`\mathcal C`$: places $`(x,s,a)`$ as for Model D and, with real numbers $`m_x>0`$, $`\eta_x>0`$, $`\zeta_x>0`$ and $`V_x`$,
```math
C_b=A_\zeta+\sum_x\lvert x\rangle\langle x\rvert\otimes\Bigl[\sigma_3\otimes(m_x\mathbb 1_N+\eta_xD)+V_x\,\mathbb 1_2\otimes\mathbb 1_N\Bigr],\qquad A_\zeta=\frac\tau2\sum_x\zeta_x\Bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\Bigr)\otimes\mathbb 1_N ,
```
with the linear profiles $`m_x=m\,(1+g_mx)`$, $`\eta_x=1+g_\eta x`$, $`\zeta_x=1+g_\zeta(x+\tfrac12)`$, $`V_x=-\mathcal F\,x`$ on a chain $`\lvert x\rvert\le L`$. Notation fixed there:
- $`P_x:=\lvert x\rangle\langle x\rvert`$, $`R_x:=\lvert x+1\rangle\langle x\rvert`$, $`\hat x:=\sum_xx\,P_x`$, $`\mathsf M_x:=m_x\mathbb 1_N+\eta_xD`$, $`d_k:=\frac{2\pi k}{N\lambda_0}`$; $`C_{\rm eff}`$ is the effective body contract (8.19) of 04-ilang-time/08-maximal-speed, and all profiles are those of $`C_{\rm eff}`$;
- on the clock level $`k`$ (clock label in $`\lvert f_k\rangle`$; the level is conserved): $`M_{x,k}:=m_x+\eta_xd_k`$, the on-site block $`M_{x,k}\sigma_3+V_x\mathbb 1_2`$ and the hopping block $`T_x=-\tfrac{i\tau}2\zeta_x\sigma_1`$ from $`x`$ to $`x+1`$; for the linear profiles $`M_{x,k}=M_k+G_kx`$ with $`M_k:=m+d_k`$ and $`G_k:=m\,g_m+d_k\,g_\eta`$; $`\omega_k(p):=\sqrt{M_k^2+\tau^2\sin^2p}`$; $`b_1:=(\tau+M_k)\lvert g_\zeta\rvert+\lvert G_k\rvert+\lvert\mathcal F\rvert`$;
- $`\bar x_{\rm lab}(\lambda):=\sum_xx\,p_x(\lambda)`$ is the mean position label; the weak-record regime is the limit $`\kappa\to0`$ at fixed $`\lambda`$, chain and start; "first order in the gradients" is the first order jointly in $`g_m,g_\eta,g_\zeta,\mathcal F`$ at fixed $`\lambda`$, start and chain, followed by the limit of a long chain;
- the start $`S_k(x_0)`$: $`\phi=\phi_X\otimes\lvert1\rangle\otimes\lvert f_k\rangle`$ with $`\phi_X(x)=c_W\,w\bigl((x-x_0)/W\bigr)`$, $`w`$ real and smooth with support in $`[-1,1]`$ (a bare branch label $`s=1`$); the start $`S_{\rm clock}(x_0)`$: the same with the clock label in the place $`\lvert0\rangle`$;
- $`\tilde\phi_X(p):=\sum_xe^{-ipx}\phi_X(x)`$, $`\langle f\rangle_W:=\int_{-\pi}^{\pi}\frac{\mathrm dp}{2\pi}\lvert\tilde\phi_X(p)\rvert^2f(p)`$, and $`\delta_W^2:=\sum_x(\phi_X(x+1)-\phi_X(x))^2=O(W^{-2})`$.

Eq. (3.36), for the start $`S_{\rm clock}(x_0)`$ at zeroth order in the gradients and to first order in the level spacing, with the local parameters $`\tau^0:=\tau(1+g_\zeta x_0)`$, $`m^0:=m_{x_0}`$, $`\eta^0:=\eta_{x_0}`$, $`\bar\mu:=m^0+\eta^0\frac{\pi(N-1)}{N\lambda_0}`$ and $`\Gamma(p):=\bar\mu/\sqrt{\bar\mu^2+\tau^{0\,2}\sin^2p}`$; $`\vartheta_W`$ is the mean advance of the clock distribution, $`r_W`$ the rate at finite $`W`$:

```math
\vartheta_W(\lambda):=\Bigl\langle\tfrac{1+\Gamma}2\Gamma-\tfrac{1-\Gamma}2\Gamma\Bigr\rangle_W\frac{\eta^0\lambda}{\lambda_0}=(1-\varsigma_W)\frac{\eta^0\lambda}{\lambda_0},\qquad r_W(x_0):=\frac{\mathrm d\vartheta_W}{\mathrm d\lambda}=\frac{\eta^0}{\lambda_0}\,(1-\varsigma_W),\qquad\varsigma_W(x_0):=\Bigl\langle\frac{\tau^{0\,2}\sin^2p}{\bar\mu^2+\tau^{0\,2}\sin^2p}\Bigr\rangle_W,
```

Eq. (3.23), the rate at $`x_0`$ (its wide-start form and its form at finite $`W`$), with $`E^{\pm}_{x,k}:=V_x\pm M_{x,k}`$:

```math
\text{rate at }x_0:=\lim_{W\to\infty}r_W(x_0)=\frac{\eta_{x_0}}{\lambda_0}=\frac{N}{2\pi}\bigl(E^+_{x_0,k+1}-E^+_{x_0,k}\bigr),\ \ \text{tick }\frac{\lambda_0}{\eta_{x_0}};\qquad\text{at finite }W:\ \ r_W=\frac{\eta_{x_0}}{\lambda_0}(1-\varsigma_W),\ \ \text{tick }\frac{\lambda_0}{\eta_{x_0}(1-\varsigma_W)},\ \ \Bigl\lvert r_W-\frac{\eta_{x_0}}{\lambda_0}\Bigr\rvert\le\frac{\eta_{x_0}}{\lambda_0}\,\delta_W^2\frac{\tau^{0\,2}}{m_{x_0}^2}.
```

Eq. (3.24), the ratio of the rates at two positions, taken from two runs with the starts $`S_{\rm clock}(x_1)`$, $`S_{\rm clock}(x_2)`$ (same $`w`$ and $`W`$) and the clock read at the same $`\lambda`$ in both; $`\varkappa_i:=\tau^0(x_i)/\bar\mu(x_i)`$; the variants (a), (b2), (c) have $`g_\eta=g`$ and the variants (b1), (d) have $`g_\eta=0`$:

```math
\frac{r_W(x_1)}{r_W(x_2)}=\frac{\eta_{x_1}}{\eta_{x_2}}\cdot\frac{1-\varsigma_W(x_1)}{1-\varsigma_W(x_2)}\ \xrightarrow[W\to\infty]{}\ \frac{\eta_{x_1}}{\eta_{x_2}}=\frac{1+g_\eta x_1}{1+g_\eta x_2}:\quad\text{(a), (b2), (c)}:\ \frac{1+gx_1}{1+gx_2};\quad\text{(b1), (d)}:\ 1;\qquad\Bigl\lvert\frac{1-\varsigma_W(x_1)}{1-\varsigma_W(x_2)}-1\Bigr\rvert\le\delta_W^2\,\lvert\varkappa_1^2-\varkappa_2^2\rvert\,(1+\varkappa_2^2).
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5).
- No two objects have the same type, so every partition of joint places is an admissible reading and every state after a reading is admissible.
- Equivalences are required for every start and every schedule of the stated kind. "Detectable" is meant in this sense: with respect to re-timings by constant factors of the classes and an arbitrary contract $`C'`$ of the allowed form.
- The division of the places into blocks is part of the setting of each item (M8).

## Scope

- **Class.** Item 1: every contract of the stated kind and every division into blocks. Item 2: every member of $`\mathcal C`$ on a finite chain, every $`\kappa>0`$ and every $`X`$ of the stated kind. Item 3: all body contracts $`C_1`$, $`C_2`$, all $`\kappa_1,\kappa_2>0`$ and all $`X`$.
- **Controls.** The body without hopping against the body with hopping (item 2); the medium read against not read, and $`X`$ diagonal in the places of the medium against not diagonal (items 2 and 3).
- In scope:
  - equivalences under re-timings of classes of places, and the detectable relative factors;
  - one body on a chain with and without hopping;
  - two bodies with a common recording medium;
  - the status of the comparison of two runs.
- Out of scope:
  - re-timings that are not linear in $`\lambda`$;
  - instances of one type (Law 5), and readings whose classes are not local to one object;
  - a protocol that compares two clocks by carrying one of them, or by a signal (a later package);
  - the motion and the fall of the body (03-clock-and-fall, 04-branch-fall);
  - any physical meaning of $`\lambda`$ beyond the definitions (M1); no theory that contains time may be used as an input (M4).

## Depth

- Item 1: derive.
- Item 2: derive.
- Item 3: derive.
- Item 4: short argument.

## Expected result

- Item 1: an equivalence of conditions; conditions on matrix elements; an equivalence with a contract and a description of the remaining freedom.
- Item 2: for each case the set of equivalences and a list of detectable relative factors; a yes/no answer; a table of yes/no answers.
- Item 3: a set of equivalences with conditions; a yes/no answer with a contract; a transformation rule and two statements.
- Item 4: two yes/no answers and a statement.

Give every main result a tag $`(5.k)`$.

Consistency checks, at most three: for example two classes that are two objects against (10.14), a chain of two positions with a clock of two places, and $`C`$ diagonal in the joint places.

## Code

None.
