# Question: 10-global-order

- **Subproject:** 04-ilang-time
- **Package:** 10-global-order
- **Equation tags:** (10.k)
- **Created:** 2026-10-10

## Goal

Determine which features of the ordering parameter $`\lambda`$ can be detected through readings: its unit, its direction, and the relation between the values of $`\lambda`$ at which readings on different parts are made, in particular a common "now" (equal $`\lambda`$) and the order of two events. This is criterion 8.

**Setting.**
- **Objects and parts.** Finitely many objects of pairwise different types, each the only instance of its type, so $`\mathcal H_{\rm adm}=\mathcal H`$. The objects are divided into two nonempty disjoint parts $`\mathcal P_1`$, $`\mathcal P_2`$, and $`\mathcal H=\mathcal H_1\otimes\mathcal H_2`$.
- **Contract.** $`C`$ is self-adjoint, independent of $`\lambda`$ and a sum of pair terms (A5). The parts are **uncoupled** if $`C=C_1\otimes\mathbb 1+\mathbb 1\otimes C_2`$ with self-adjoint $`C_1`$, $`C_2`$; otherwise they are **coupled**.
- **Start.** A unit vector $`\Psi_0`$ at $`\lambda=0`$; only $`\lambda\ge0`$ is used (A9 restricted).
- **Readings.** Readings are applied at stated values of $`\lambda`$ (A8, first representation); no reading is represented by a record inside the description. A local reading on a part is a partition of the joint places of that part (A4).
- **Schedule.** A finite list of **events** $`e_k=(i_k,R_k,\lambda_k)`$, $`k=1,\dots,K`$: a part index $`i_k\in\{1,2\}`$, a local reading $`R_k`$ on $`\mathcal P_{i_k}`$, and a value $`\lambda_k\ge0`$. The readings are applied by (1.3) in the order of increasing $`\lambda_k`$, and between them the state evolves by (1.9). Events with equal $`\lambda`$ are applied in any order; state why the order does not matter. The **statistics** of the schedule is the joint distribution of its $`K`$ outcomes.
- **Re-timing.** Two numbers $`a_1,a_2>0`$ and a contract $`C'`$ on the same objects (self-adjoint, independent of $`\lambda`$, a sum of pair terms). The re-timed schedule has the same events with $`\lambda_k`$ replaced by $`a_{i_k}\lambda_k`$.
- **Equivalence.** A re-timing $`(a_1,a_2,C')`$ is an **equivalence of $`C`$** if, for every start $`\Psi_0`$ and every schedule, the statistics of the re-timed schedule under $`C'`$ equal the statistics of the original schedule under $`C`$.
- **Detectable.** For a given $`C`$:
  - the **unit of $`\lambda`$** is detectable if every equivalence of $`C`$ has $`a_1=a_2=1`$;
  - the **common now** is detectable if every equivalence of $`C`$ has $`a_1=a_2`$. (A re-timing with $`a_1\neq a_2`$ changes which events on different parts have equal $`\lambda`$, and reverses the order of some pairs of events on different parts.)

1. **Unit and origin.**
   - (a) Determine how the statistics of a schedule behave under the re-timing $`a_1=a_2=a`$, $`C'=C/a`$. Determine whether the unit of $`\lambda`$ is detectable, for any $`C`$.
   - (b) Let the start be an eigenvector of $`C`$. Determine how the statistics of a schedule change when all $`\lambda_k`$ are increased by the same amount, and how the statistics of a schedule with a single event depend on its $`\lambda`$.

2. **Direction.** Take a schedule with two events on different parts, with readings $`R`$ at $`\lambda_1`$ and $`R'`$ at $`\lambda_2>\lambda_1`$.
   - Determine, for every $`C`$ and every start, whether the marginal distribution of the outcome of $`R`$ depends on whether $`R'`$ is made, and whether the marginal distribution of the outcome of $`R'`$ depends on whether $`R`$ is made.
   - State what this implies for the detectability of the direction of increasing $`\lambda`$, and which element of the formalization (the laws, (1.1)–(1.11), A1–A9) fixes that direction.

3. **Uncoupled parts.**
   - (a) Determine a family of equivalences with $`a_1\neq a_2`$ that holds for every start, whether or not it is a product of states of the two parts.
   - (b) Determine whether the common now is detectable. For two events on different parts with $`\lambda_1<\lambda_2`$, determine whether an equivalence exists after which their values of $`\lambda`$ are equal, and one after which their order is reversed.

4. **Coupled parts.**
   - (a) For an equivalence $`(a_1,a_2,C')`$ of a general $`C`$, determine the conditions that follow from schedules with a single event, at first and at second order in $`\lambda`$. Express them through commutators of $`C`$ and $`C'`$ with the place projectors of the two parts.
   - (b) Determine a sufficient condition on $`C`$ under which every equivalence has $`a_1=a_2`$. Determine a sufficient condition under which an equivalence with $`a_1\neq a_2`$ exists although the parts are coupled.
   - (c) For each of the following three contracts, determine all equivalences, and whether the common now is detectable. Each part is one object with two places; $`\sigma^x`$, $`\sigma^z`$ are the Pauli matrices in the place basis, with $`\sigma^z`$ diagonal, and $`g,h,t,\kappa>0`$.
     - (i) $`C=g\,\sigma^x\otimes\sigma^x`$.
     - (ii) $`C=g\,\sigma^z\otimes\sigma^z+h\,\sigma^x\otimes\mathbb 1`$.
     - (iii) $`C=t\,\sigma^x\otimes\mathbb 1+\lvert2\rangle\langle2\rvert\otimes\kappa\,\sigma^x`$, where $`\lvert2\rangle`$ is the second place of $`\mathcal P_1`$: a body with two places and a hopping term, whose place is recorded by a medium.

5. **The order of two events on a chain.** Setting of 07-causal-order (quoted under "Inputs"): a chain of $`n`$ cells, a reading $`R_i`$ on cell $`i`$ at $`\lambda_1`$ with projectors $`\Pi_s`$ and a reading $`R_j`$ on cell $`j`$ at $`\lambda_2=\lambda_1+\delta`$, $`\delta\ge0`$, with projectors $`\Pi'_t`$; $`r=\lvert i-j\rvert\ge1`$, $`\Psi_1`$ is the state at $`\lambda_1`$ and $`Q_t=\Pi'_t(\delta)`$. The joint statistics are $`P(s,t)=\lVert Q_t\Pi_s\Psi_1\rVert^2`$. Define the **order-exchanged statistics** $`\tilde P(s,t):=\lVert\Pi_sQ_t\Psi_1\rVert^2`$: the two readings, both carried to $`\lambda_1`$ by the evolution, applied in the opposite order.
   - (a) Determine the necessary and sufficient condition under which $`P=\tilde P`$ for every start. Determine its relation to the influence (7.1) of $`R_i`$ on $`R_j`$.
   - (b) Determine an upper bound on $`\sum_{s,t}\lvert P(s,t)-\tilde P(s,t)\rvert`$, valid for every start, in terms of $`r`$, $`\delta`$, $`\lVert J\rVert`$ and the numbers of classes of the two readings. Determine the set of $`(r,\delta)`$ on which this bound is below a given $`\epsilon>0`$, and compare it with (7.15).
   - (c) State what (a) and (b) imply for the detectability of the order of two events on different cells: at equal $`\lambda`$, at a small delay over a large distance, and in general.

## Inputs

From 07-causal-order@v2 (this subproject). Setting there: a chain of $`n\ge2`$ cells, objects $`1,\dots,n`$ of pairwise different types, with $`C=\sum_{i=1}^nD_i+\sum_{i=1}^{n-1}J_i`$, where $`D_i`$ acts on cell $`i`$ alone, $`J_i`$ is a pair term on cells $`i`$ and $`i+1`$, and $`\lVert J\rVert:=\max_i\lVert J_i\rVert`$. Notation fixed there:
- a reading $`R_i`$ on cell $`i`$ at $`\lambda_1`$ with outcomes $`s`$ and projectors $`\Pi_s`$ ($`m`$ classes), a reading $`R_j`$ on cell $`j`$ at $`\lambda_2`$ with outcomes $`t`$ and projectors $`\Pi'_t`$; all extended by the identity;
- $`\delta:=\lambda_2-\lambda_1`$, $`r:=\lvert i-j\rvert`$, $`\Psi_1`$ the state at $`\lambda_1`$;
- $`X(\delta):=e^{iC\delta}Xe^{-iC\delta}`$, $`Q_t:=\Pi'_t(\delta)`$ and $`\mathcal M_i(X):=\sum_s\Pi_sX\Pi_s`$;
- $`P_j(t\mid R_i)`$ is the probability of the outcome $`t`$ of $`R_j`$ averaged over the outcomes of $`R_i`$, and $`P_j(t)`$ the same probability without $`R_i`$; $`R_i`$ **influences** $`R_j`$ if $`P_j(\cdot\mid R_i)\neq P_j(\cdot)`$, and $`\delta P:=\sum_t\lvert P_j(t\mid R_i)-P_j(t)\rvert`$.

Eq. (7.1):

```math
\Delta_t:=P_j(t\mid R_i)-P_j(t)=\langle\Psi_1\vert\,\mathcal M_i(Q_t)-Q_t\,\vert\Psi_1\rangle,\qquad \mathcal M_i(X)-X=\sum_s\Pi_s\,[X,\Pi_s].
```

Eq. (7.2):

```math
P_j(\cdot\mid R_i)=P_j(\cdot)\qquad\text{whenever }\lambda_2\le\lambda_1,\ \text{for all cells } i,j,\ \text{all starts and all readings.}
```

Eq. (7.11), for an operator $`A`$ on cell $`j`$ and an operator $`B`$ on cell $`i`$ at distance $`r`$, uniform in $`n`$ and independent of the $`D_l`$:

```math
\bigl\lVert[A(\delta),B]\bigr\rVert\le2\lVert A\rVert\lVert B\rVert\sum_{k=r}^{\infty}\frac{(2\lVert J\rVert\delta)^k}{k!}\qquad(\delta\ge0,\ r\ge1).
```

Eq. (7.12), for every start, every pair of readings and every $`\delta\ge0`$:

```math
\delta P\le2\Bigl(1-\frac1m\Bigr)\sum_{k\ge r}\frac{(2\lVert J\rVert\delta)^k}{k!}\le2\sum_{k\ge r}\frac{(2\lVert J\rVert\delta)^k}{k!}\le\frac{2\,(2\lVert J\rVert\delta)^r}{r!}\,e^{2\lVert J\rVert\delta}.
```

Eq. (7.15), the region in which $`\delta P<\epsilon`$ is guaranteed; for $`\lVert J\rVert>0`$, $`\delta_\epsilon(r)`$ is the root of $`2\sum_{k\ge r}(2\lVert J\rVert\delta)^k/k!=\epsilon`$:

```math
\mathcal S_\epsilon:=\Bigl\{(r,\delta):\ r\ge1,\ \delta\ge0,\ 2\sum_{k\ge r}\frac{(2\lVert J\rVert\delta)^k}{k!}<\epsilon\Bigr\}=\bigl\{(r,\delta):\ 0\le\delta<\delta_\epsilon(r)\bigr\}.
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5).
- No two objects have the same type, so every partition of joint places is an admissible reading and every state after a reading is admissible.
- Equivalences are required for every start and every schedule. "Detectable" is meant in this sense: with respect to re-timings by constant factors $`a_1,a_2`$ and an arbitrary contract $`C'`$ of the allowed form.

## Scope

- In scope:
  - the behaviour of reading statistics under re-timings of the two parts;
  - the unit, the direction and the common now of $`\lambda`$;
  - uncoupled parts in general, coupled parts through general conditions and the three examples;
  - the order of two events on a chain, through the order-exchanged statistics.
- Out of scope:
  - re-timings that are not linear in $`\lambda`$, more than two parts, and re-timings that depend on the position;
  - readings represented by records inside the description, and events defined by the readings of clocks;
  - a complete classification of the coupled contracts for which the common now is detectable;
  - bodies of the Model D type and their motion (05, 09);
  - any physical meaning of $`\lambda`$ beyond the definitions (M1); no theory that contains time may be used as an input (M4).

## Depth

- Item 1: short argument.
- Item 2: short argument.
- Item 3: derive.
- Item 4: derive.
- Item 5: short argument for (a) and (c); derive (b).

## Expected result

- Item 1: a statement and a yes/no answer; two statements.
- Item 2: two yes/no answers with conditions; a statement.
- Item 3: a family of equivalences; a yes/no answer and two yes/no answers.
- Item 4: conditions in closed form; two sufficient conditions; for each example the set of equivalences and a yes/no answer.
- Item 5: an equivalence of conditions; an inequality and a set; a statement.

Give every main result a tag $`(10.k)`$.

Consistency checks, at most three: for example $`C=0`$, a contract that is diagonal in the places, and example (i) against the exact evolution of two cells.

## Code

None.
