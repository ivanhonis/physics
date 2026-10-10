# Question: 04-clock-comparison

- **Subproject:** 04-ilang-time
- **Package:** 04-clock-comparison
- **Equation tags:** (4.k)
- **Created:** 2026-10-10

## Goal

Determine how the readings of two clocks compare:
- their joint statistics;
- the ratio of their rates, expressed through readings;
- when two clocks agree, and how readings can synchronize them;
- how a contract with an environment changes the rate of a clock, for one clock and for two clocks of different types.

This is criterion 3. Time as a relation between a clock and the rest of a system is criterion 2 and not part of this package.

**Setting.**
- **Objects.** Two clock objects $`K_1`$ and $`K_2`$, each a part of its own; the rest of the system; and, in item 3, an environment part $`E`$. No two objects of the system have the same type, so every partition of joint places is an admissible reading.
- **Clocks.** $`K_i`$ has $`N_i\ge2`$ places $`m_i\in\mathbb Z_{N_i}`$, a tick $`\lambda_{0i}>0`$, and the contract
  ```math
  C_{K_i}=\frac{2\pi}{N_i\lambda_{0i}}\sum_{k=0}^{N_i-1}k\,\lvert f^{(i)}_k\rangle\langle f^{(i)}_k\rvert,\qquad \lvert f^{(i)}_k\rangle=\frac1{\sqrt{N_i}}\sum_{m\in\mathbb Z_{N_i}}e^{2\pi ikm/N_i}\lvert m\rangle .
  ```
  By (2.9) and (2.12) of 02-clock, quoted under "Inputs", each is a uniform ring clock with $`\theta_m=0`$ and minimal cost spread (the case $`\alpha_m=0`$, $`\varepsilon=0`$, $`\ell_k=k`$); call such a clock a **minimal ring clock**. Its reading is the place reading.
- **Free clocks (items 1–2).** No contract term acts across $`K_1`$, $`K_2`$ and the rest, so each clock is self-driven by (2.1). The start is $`\lvert0\rangle\otimes\lvert0\rangle\otimes\chi`$, with $`\chi`$ a state of the rest.
- **Joint reading.** The place reading on $`K_1\cup K_2`$, with one class per joint place $`(m_1,m_2)`$, applied at a stated value of $`\lambda`$ (A8).

1. **Joint readings of two free clocks.**
   - (a) Determine the joint distribution of $`(m_1,m_2)`$ at $`\lambda`$.
   - (b) Determine the set of $`\lambda>0`$ at which both readings are certain, and the readings there. Determine a necessary and sufficient condition on $`\lambda_{01}`$ and $`\lambda_{02}`$ under which this set is nonempty.
   - (c) At $`\lambda=n\lambda_{01}`$, $`n\in\mathbb Z`$, the reading of $`K_1`$ is certain. Determine the distribution of the reading of $`K_2`$ there, and its places of maximal probability, as functions of $`n`$, $`\lambda_{01}/\lambda_{02}`$ and $`N_2`$.

2. **Identical clocks.** Let $`N_1=N_2=N`$ and $`\lambda_{01}=\lambda_{02}=\lambda_0`$.
   - (a) Determine the probability that the two readings coincide ($`m_1=m_2`$) as a function of $`\lambda`$, its minimum over $`\lambda`$, and the set of $`\lambda`$ at which it equals $`1`$.
   - (b) A joint reading at $`\lambda_s`$ gives $`(m_1,m_2)`$. For a second joint reading at $`\lambda>\lambda_s`$, determine the joint distribution of its outcomes, and the probability that $`m_2-m_1`$ (mod $`N`$) is the same as at $`\lambda_s`$.

3. **A clock in an environment.** Let $`C=C_{K_1}\otimes\mathbb 1_E+\mathbb 1_{K_1}\otimes C_E+A\otimes B`$, with $`A=A^\dagger`$ on $`\mathcal H_{K_1}`$, $`B=B^\dagger`$ on $`\mathcal H_E`$ and $`[B,C_E]=0`$; the contracts of $`K_2`$ and of the rest are omitted. The start is $`\lvert0\rangle\otimes\lvert b\rangle`$, where $`\lvert b\rangle`$ is a common eigenvector of $`B`$ and $`C_E`$ with $`B\lvert b\rangle=b\lvert b\rangle`$.
   - (a) Determine the view of $`K_1`$ for every $`\lambda`$. Determine whether $`K_1`$ is self-driven in the sense of 02-clock.
   - (b) Let $`\mathfrak B\subset\mathbb R`$ have at least two elements. Determine all $`A`$ for which $`C_{K_1}+bA`$ is, for every $`b\in\mathfrak B`$, the contract of a minimal ring clock with $`N_1`$ places and some tick $`\lambda_{01}(b)>0`$. Determine $`\lambda_{01}(b)`$.
   - (c) Let both clocks be coupled to the same environment: $`C=C_{K_1}+C_{K_2}+C_E+A_1\otimes B+A_2\otimes B`$, each term extended by the identity, with $`A_i`$ of the form found in (b) for $`K_i`$, and the start $`\lvert0\rangle\otimes\lvert0\rangle\otimes\lvert b\rangle`$. Determine a necessary and sufficient condition under which the ratio $`\lambda_{01}(b)/\lambda_{02}(b)`$ is the same for all $`b\in\mathfrak B`$.

## Inputs

From 02-clock@v2. Setting and notation fixed there:
- a part $`K`$ with companion $`R`$, and $`C=C_K\otimes\mathbb 1_R+\mathbb 1_K\otimes C_R+C_\partial`$ with $`C_\partial=\sum_nA_n\otimes B_n`$ the terms across the cut;
- $`K`$ is self-driven if $`V_K(\lambda)=e^{-iC_K\lambda}V_K(0)e^{iC_K\lambda}`$ for every start and every $`\lambda`$;
- a uniform ring clock is a single object with $`N\ge2`$ places $`m\in\mathbb Z_N`$, with $`e^{-iC_K\lambda_0}\lvert m\rangle=e^{i\theta_m}\lvert m+1\rangle`$ for every $`m`$, where $`\lambda_0>0`$ is its tick;
- $`S\lvert m\rangle=\lvert m+1\rangle`$, $`\lvert f_k\rangle=N^{-1/2}\sum_me^{2\pi ikm/N}\lvert m\rangle`$, $`V_0:=V_K(0)`$, and $`\Delta C_K`$ is the spread of $`C_K`$ in the view of $`K`$.

Eq. (2.1), a sufficient condition for $`K`$ to be self-driven:

```math
C_\partial=\mathbb 1_K\otimes B,\qquad B=B^\dagger\ \text{on}\ \mathcal H_R\quad(\text{in particular } C_\partial=0).
```

Eq. (2.4), for a self-driven $`K`$ and a reading on $`K`$ with projectors $`\Pi_r`$:

```math
p(r;\lambda)=\mathrm{Tr}\bigl(\Pi_r\,e^{-iC_K\lambda}V_0\,e^{iC_K\lambda}\bigr),
```

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

Eq. (2.13), the place-reading distribution of a self-driven uniform ring clock of a minimal member, started at $`\lvert0\rangle`$:

```math
p(m;\lambda)=\frac{\sin^2(\pi\lambda/\lambda_0)}{N^2\sin^2\bigl(\pi(\lambda/\lambda_0-m)/N\bigr)}\qquad(\text{value }1\text{ where the denominator vanishes}).
```

Eq. (2.14), under the condition that the state after a reading is admissible (it holds when no object of $`R`$ has the type of the clock object): "A place reading with outcome $`m`$ acts by $`\Pi_m\otimes\mathbb 1_R`$ (1.3). The partial-trace rules give the new view"

```math
V_K\ \longmapsto\ \frac{\Pi_mV_K\Pi_m}{\mathrm{Tr}(\Pi_mV_K)}=\lvert m\rangle\langle m\rvert .
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5).
- Readings are applied at stated values of $`\lambda`$ (A8). Comparing readings taken at equal $`\lambda`$ uses the order of $`\lambda`$; whether that order is detectable is criterion 8 and not part of this package.

## Scope

- In scope:
  - two minimal ring clocks, free (items 1–2) or coupled to one environment part through one contract each (item 3);
  - environment states that are common eigenvectors of $`B`$ and $`C_E`$.
- Out of scope:
  - time as a relation between a clock and the rest (criterion 2);
  - environment states that are superpositions of eigenvectors of $`B`$;
  - contracts between the two clocks, and clocks of other forms;
  - moving clocks, inertia and maximal speed (criteria 4–6);
  - any physical meaning of $`\lambda`$, $`A`$ or $`B`$ beyond the definitions (M1).

## Depth

- Item 1: (a) short argument; (b) and (c) derive.
- Item 2: (a) derive; (b) short argument.
- Item 3: (a) short argument; (b) derive; (c) short argument.

## Expected result

- Item 1: a closed form; a set, the readings there, and an equivalence; a closed form and the places of maximal probability.
- Item 2: a closed form, its minimum, and a set; a closed form and a probability.
- Item 3: a closed form and a yes/no answer; a characterization and a closed form; an equivalence.

Give every main result a tag $`(4.k)`$.

Consistency checks, at most three: for example $`N_1=N_2=2`$, $`\lambda_{01}=\lambda_{02}`$, and $`b=0`$.

## Code

None.
