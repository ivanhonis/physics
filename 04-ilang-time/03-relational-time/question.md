# Question: 03-relational-time

- **Subproject:** 04-ilang-time
- **Package:** 03-relational-time
- **Equation tags:** (3.k)
- **Created:** 2026-10-10

## Goal

Determine whether, and under which conditions, the evolution of the rest of a system can be stated relative to the readings of a clock instead of $`\lambda`$, starting from a global state whose reading statistics do not depend on $`\lambda`$ at all. Determine how rates with respect to $`\lambda`$ then convert to rates with respect to the clock. This is criterion 2. Comparing two clocks is criterion 3 and not part of this package.

**Setting.**
- **Objects.** A clock part $`K`$, consisting of one object (the clock object), and its companion $`R\neq\emptyset`$. No object of $`R`$ has the type of the clock object, so a reading on $`K`$ keeps every state admissible (A3, A6).
- **Contracts.** $`C=C_K\otimes\mathbb 1_R+\mathbb 1_K\otimes C_R+C_\partial`$, as in 02-clock: $`C_K`$ acts on the clock object, $`C_R`$ on $`R`$, and $`C_\partial=\sum_nA_n\otimes B_n`$ collects the terms across the cut.
- **Clock.** The clock object has $`N\ge2`$ places $`m\in\mathbb Z_N`$, and
  ```math
  C_K=\frac{2\pi}{N\lambda_0}\sum_{k=0}^{N-1}k\,\lvert f_k\rangle\langle f_k\rvert,\qquad \lvert f_k\rangle=\frac1{\sqrt N}\sum_{m\in\mathbb Z_N}e^{2\pi ikm/N}\lvert m\rangle ,
  ```
  with $`\lambda_0>0`$. By (2.9) and (2.12) of 02-clock, quoted under "Inputs", this is a uniform ring clock with tick $`\lambda_0`$ and $`\theta_m=0`$ (the case $`\alpha_m=0`$, $`\varepsilon=0`$, $`\ell_k=k`$), and of minimal cost spread. Its reading is the place reading.
- **Conditional states.** For a state $`\Psi`$ of the whole system and a clock place $`m`$, let $`\Phi(m):=\bigl(\langle m\rvert\otimes\mathbb 1_R\bigr)\Psi\in\mathcal H_R`$. By (1.3), a place reading on $`K`$ gives $`m`$ with probability $`\lVert\Phi(m)\rVert^2`$ and leaves the state $`\lvert m\rangle\otimes\Phi(m)/\lVert\Phi(m)\rVert`$.
- **Notation.** $`C_R=\sum_se_sQ_s`$ is the spectral decomposition of $`C_R`$, with distinct $`e_s`$.

1. **States without $`\lambda`$-dependence.** Determine a necessary and sufficient condition on the start $`\Psi(0)`$ under which the statistics of every reading, on any part and at any stated $`\lambda`$ (without earlier readings), do not depend on $`\lambda`$. For such starts, determine whether the outcome $`m`$ of a place reading on $`K`$ can change the statistics of a reading on $`R`$ performed right after it.

2. **Conditional states of an eigenstate.** Let $`C_\partial=0`$, and let $`\Psi`$ be an eigenvector of $`C`$ with eigenvalue $`E`$.
   - (a) Determine the relation between $`\Phi(m+1)`$ and $`\Phi(m)`$ for every $`m`$, in terms of $`C_R`$, $`\lambda_0`$ and $`E`$.
   - (b) Determine which components $`Q_s\Phi(m)`$ can be nonzero, as a condition on $`e_s`$, $`E`$, $`N`$ and $`\lambda_0`$. For a given unit vector $`\chi\in\mathcal H_R`$, determine a necessary and sufficient condition under which some eigenvector $`\Psi`$ of $`C`$ with eigenvalue $`E`$ has $`\Phi(0)\propto\chi`$. In that case, determine $`\Psi`$, all $`\Phi(m)`$, and the probabilities of the clock places.
   - (c) For the case of (b), compare the statistics of any reading on $`R`$ in the state $`\Phi(m)/\lVert\Phi(m)\rVert`$ with the statistics of the same reading in $`e^{-iC_R\lambda}\chi`$. Determine the values of $`\lambda`$ at which they coincide for every reading on $`R`$.

3. **Crossing contracts.** Let $`C_\partial\neq0`$. Determine whether a relation $`\Phi(m+1)=U\,\Phi(m)`$, with one unitary $`U`$ on $`\mathcal H_R`$ independent of $`m`$, holds for every eigenvector of $`C`$. Give a sufficient condition on $`C_\partial`$ under which it does, with $`U`$, and an example of a crossing contract for which it does not.

4. **Rates.** From items 2 and 3, determine how the rate of change of the statistics of a reading on $`R`$ with respect to $`\lambda`$, under the evolution of $`R`$ alone, converts to its rate of change with respect to the clock reading. State the conditions under which this conversion holds.

## Inputs

From 02-clock@v2. Setting and notation fixed there:
- a uniform ring clock is a single object with $`N\ge2`$ places $`m\in\mathbb Z_N`$, with $`e^{-iC_K\lambda_0}\lvert m\rangle=e^{i\theta_m}\lvert m+1\rangle`$ for every $`m`$, where $`\lambda_0>0`$ is its tick;
- $`S\lvert m\rangle=\lvert m+1\rangle`$ is the shift, and $`\lvert f_k\rangle=N^{-1/2}\sum_me^{2\pi ikm/N}\lvert m\rangle`$;
- $`\Delta C_K`$ is the spread of $`C_K`$ in the view of $`K`$.

Eq. (2.9), "where the $`\alpha_m`$ and $`\varepsilon`$ are arbitrary reals. The phases are then $`\theta_m=\alpha_{m+1}-\alpha_m-\varepsilon\lambda_0`$ (mod $`2\pi`$, with $`\alpha_N:=\alpha_0`$). If $`\theta_m=0`$ for all $`m`$, then $`e^{-iC_K\lambda_0}=S`$. The same argument applied to $`S`$, whose eigenvalues $`e^{-2\pi ik/N}`$ on $`\lvert f_k\rangle`$ are distinct, gives exactly $`C_K=\sum_k\frac{2\pi\ell_k}{N\lambda_0}\lvert f_k\rangle\langle f_k\rvert`$ with $`\ell_k\equiv k`$."

```math
C_K=\sum_{k\in\mathbb Z_N}E_k\lvert v_k\rangle\langle v_k\rvert,\quad
\lvert v_k\rangle=\frac{1}{\sqrt N}\sum_{m}e^{2\pi ikm/N}e^{i\alpha_m}\lvert m\rangle,\quad
E_k=\varepsilon+\frac{2\pi\ell_k}{N\lambda_0},\quad \ell_k\in\mathbb Z,\ \ell_k\equiv k\ (\mathrm{mod}\ N),
```

Eq. (2.12), for the start $`\lvert0\rangle`$:

```math
\min\Delta C_K=\frac{2\pi}{\lambda_0}\sqrt{\frac{N^2-1}{12N^2}},\quad\text{attained iff } \{\ell_k\}=\{c,c+1,\dots,c+N-1\},\ c\in\mathbb Z .
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\in\mathbb R`$ (A9).
- Readings are applied at stated values of $`\lambda`$ (A8). In item 1 they serve only to show that the value of $`\lambda`$ does not matter. Items 2–4 use readings on the eigenstate $`\Psi`$, which needs no value of $`\lambda`$.

## Scope

- In scope:
  - one clock of the form above and the rest $`R`$, a general finite system;
  - eigenstates of $`C`$ and their conditional states;
  - crossing contracts only as far as item 3 needs them.
- Out of scope:
  - comparison of clocks (criterion 3), moving clocks and inertia (criteria 4–5);
  - clocks of other forms, and clocks whose type also occurs in $`R`$;
  - events and causal order (criterion 7), and whether the order of $`\lambda`$ is detectable (criterion 8);
  - any physical meaning of $`\lambda`$ beyond the definitions (M1).

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: short argument for the sufficient condition; derive the counterexample.
- Item 4: short argument.

## Expected result

- Item 1: an equivalence; a yes/no answer.
- Item 2: an identity; a condition, an equivalence and closed forms; a set of values of $`\lambda`$.
- Item 3: a yes/no answer, a sufficient condition with $`U`$, and an explicit counterexample.
- Item 4: a conversion rule and its conditions.

Give every main result a tag $`(3.k)`$.

Consistency checks, at most three: for example $`N=2`$, an $`R`$ whose state is an eigenvector of $`C_R`$, and the normalization of the place probabilities.

## Code

None.
