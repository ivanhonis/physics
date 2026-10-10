# Question: 02-clock

- **Subproject:** 04-ilang-time
- **Package:** 02-clock
- **Equation tags:** (2.k)
- **Created:** 2026-10-09

## Goal

Determine when a part of a system can serve as a clock, how its readings change with $`\lambda`$, how reading it affects it (Law 1), and what limits its resolution. The notions defined below are fixed for later packages. They mean only what their definitions say. A clock here indexes $`\lambda`$; whether its readings give a physical time is criterion 2 and not part of this package (M1).

**Setting.**
- **Objects.** The system consists of a part $`K`$, the clock part, and its companion $`R\neq\emptyset`$ (by A5, a single-object term of $`K`$ is booked into a pair term, which needs a second object). The joint places of $`K`$ are $`m,m'`$, those of $`R`$ are $`r,r'`$.
- **Contracts.** $`C=C_K\otimes\mathbb 1_R+\mathbb 1_K\otimes C_R+C_\partial`$, where $`C_K`$ collects the contract terms inside $`K`$ (single-object terms of $`K`$ included), $`C_R`$ those inside $`R`$, and $`C_\partial=\sum_nA_n\otimes B_n`$ the terms across the cut, with $`A_n=A_n^\dagger`$ on $`\mathcal H_K`$ and $`B_n=B_n^\dagger`$ on $`\mathcal H_R`$.
- **Readings on $`K`$.** A reading on $`K`$ is a local reading on $`K`$ (A4): a partition of the joint places of $`K`$ into classes $`S_r`$, with projectors $`\Pi_r`$. Its statistics at $`\lambda`$ in the evolution (1.9) without readings are $`p(r;\lambda):=\mathrm{Tr}\bigl(\Pi_r V_K(\lambda)\bigr)`$, where $`V_K(\lambda)`$ is the view (1.5) of $`K`$ in $`\lvert\Psi(\lambda)\rangle`$. Item 4 applies readings at stated values of $`\lambda`$ (A8).

**Definitions.**
- **Self-driven.** $`K`$ is self-driven if $`V_K(\lambda)=e^{-iC_K\lambda}V_K(0)\,e^{iC_K\lambda}`$ for every start and every $`\lambda`$.
- **Ticking.** A reading on $`K`$ ticks if $`p(r;\lambda)`$ depends on $`\lambda`$ for some outcome $`r`$.
- **Index.** The view of $`K`$ indexes $`\lambda`$ on a set $`\Lambda\subseteq\mathbb R`$ if $`\lambda\mapsto V_K(\lambda)`$ is injective on $`\Lambda`$.
- **Clock.** A clock is a self-driven part $`K`$ together with a reading on $`K`$ that ticks.
- **Uniform ring clock.** $`K`$ is a single object $`k`$ whose type has $`N\ge2`$ places, labelled $`m\in\mathbb Z_N`$, and there is $`\lambda_0>0`$ with $`e^{-iC_K\lambda_0}\lvert m\rangle=e^{i\theta_m}\lvert m+1\rangle`$ for every $`m`$ (indices mod $`N`$, real phases $`\theta_m`$). Its tick is $`\lambda_0`$. Its reading is the place reading, with one class per place.
- **Cost spread of the clock.** $`L_K:=\mathrm{Tr}\bigl(C_KV_K\bigr)`$ and $`\Delta C_K:=\bigl(\mathrm{Tr}(C_K^2V_K)-L_K^2\bigr)^{1/2}`$.

1. **Self-driven part.** Determine conditions on the contracts under which $`K`$ is self-driven, and whether they are also necessary. Determine whether the statistics of readings on a self-driven $`K`$ depend on the state of $`R`$ beyond $`V_K(0)`$.

2. **Ticking and index.** Let $`K`$ be self-driven, with $`C_K=\sum_iE_iP_i`$ (spectral decomposition, distinct $`E_i`$).
   - (a) Determine $`p(r;\lambda)`$ in terms of the $`E_i`$, the $`P_i`$, $`V_K(0)`$ and $`\Pi_r`$. Determine a necessary and sufficient condition, in terms of $`C_K`$ and $`V_K(0)`$ and the place basis of $`K`$, under which at least one reading on $`K`$ ticks.
   - (b) Determine the set of $`\lambda'`$ with $`V_K(\lambda')=V_K(\lambda)`$. Determine a necessary and sufficient condition under which the view of $`K`$ indexes $`\lambda`$ on all of $`\mathbb R`$, and otherwise the largest intervals on which it does.

3. **Uniform ring clock.**
   - (a) Determine all self-adjoint $`C_K`$ that make $`K`$ a uniform ring clock with tick $`\lambda_0`$, in terms of their eigenvalues and eigenvectors.
   - (b) For a self-driven uniform ring clock started at $`\lvert0\rangle`$, determine $`p(m;\lambda)`$ for every $`\lambda`$ and every member of the family of (a). Determine $`\Delta C_K`$ of this start over the family, and its minimum.

4. **Reading the clock (Law 1).** Let $`K`$ be a self-driven uniform ring clock with $`\theta_m=0`$, started at $`\lvert0\rangle`$ and read with the place reading at stated values of $`\lambda`$ (A8).
   - (a) For readings at $`\lambda_1`$ and at $`\lambda_2>\lambda_1>0`$, determine the joint distribution of the two outcomes, and the distribution of the second outcome when the first outcome is not recorded. Determine whether the first reading changes the distribution of the second outcome, and when.
   - (b) For readings at $`\lambda_j=j\lambda/n`$, $`j=1,\dots,n`$, with fixed $`\lambda>0`$, determine the probability that all $`n`$ outcomes equal $`0`$, and its limit as $`n\to\infty`$.

5. **Resolution.**
   - (a) Let $`K`$ be self-driven with $`V_K(0)`$ pure, $`V_K(\lambda)=\lvert\psi(\lambda)\rangle\langle\psi(\lambda)\rvert`$, and let $`\theta(\lambda,\lambda'):=\arccos\bigl\lvert\langle\psi(\lambda)\vert\psi(\lambda')\rangle\bigr\rvert\in[0,\pi/2]`$. Determine $`\lim_{\lambda'\to\lambda}\theta(\lambda,\lambda')/\lvert\lambda'-\lambda\rvert`$, and a lower bound, in terms of $`\Delta C_K`$, on the smallest $`\lvert\lambda'-\lambda\rvert>0`$ at which $`\psi(\lambda')`$ and $`\psi(\lambda)`$ are orthogonal. Orthogonality is necessary for a reading on $`K`$ to distinguish the two states with certainty.
   - (b) For the uniform ring clock of item 4, with the member of the family of minimal $`\Delta C_K`$: determine the smallest $`\lambda>0`$ at which $`\psi(\lambda)\perp\psi(0)`$, its ratio to the bound of (a), the limit of the ratio as $`N\to\infty`$, and the $`N`$ for which the bound is attained.

## Inputs

None. The package builds only on the base problem.

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5).
- Items 1–3 and 5 use the evolution (1.9) without readings. Item 4 applies readings at stated values of $`\lambda`$; between readings the state evolves by (1.9) (A8).

## Scope

- In scope:
  - one clock part and its own readings; the uniform ring clock;
  - readings applied at stated values of $`\lambda`$.
- Out of scope:
  - time as a relation between clock readings and other parts (criterion 2), and the comparison of clocks (criterion 3);
  - moving clocks, inertia and maximal speed (criteria 4–6);
  - events, records, and readings represented by recording contracts (criterion 7);
  - clocks that are not self-driven, beyond item 1;
  - any physical meaning of $`\lambda`$ (M1).

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: derive.
- Item 4: derive.
- Item 5(a): short argument; standard facts on unitary evolution may be used, stated.
- Item 5(b): derive.

## Expected result

- Item 1: a sufficient condition, whether it is necessary (with a counterexample if not), and a yes/no answer.
- Item 2: a closed form and an equivalence; a description of a set, an equivalence, and the intervals.
- Item 3: a characterization; closed forms, and a closed form with its minimum.
- Item 4: closed forms and a yes/no answer with a condition; a closed form and its limit.
- Item 5: a rate and an inequality; a closed form, a ratio, its limit, and the values of $`N`$.

Give every main result a tag $`(2.k)`$.

Consistency checks, at most three: for example $`N=2`$, a start whose view commutes with $`C_K`$, and the normalization of all distributions.

## Code

None.
