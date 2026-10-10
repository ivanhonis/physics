# Causal order of single-cell readings on a contract chain

- **Subproject:** 04-ilang-time
- **Package:** 07-causal-order
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-10

## Changes from previous version

- **New Step 10** (tags (7.22)–(7.25)): the question "does one fixed generic chain have influence at every positive delay" is now treated on its own, separately from the fixed-delay statement (7.20). It is decided for $`n=2`$ (yes), reduced to blind delays for different cells when $`n\ge3`$, and the cases that remain undecided are named in Step 10 (d) and in the Result.
- **Step 9 (ii)**: (7.20) is labelled as a fixed-delay statement; the paragraph on a fixed $`C`$ now separates $`\mathcal I_{ij}=\emptyset`$ from $`\mathcal I_{ij}\neq\emptyset`$. **Step 9 (iii)** uses (7.25).
- **Step 6 (a)**: the one-class reading $`m=1`$ is treated separately. **Step 6 (c)** and Result item 3: leading-order attainment is attributed to the reading-dependent bound only.
- **Step 8**: the root $`\delta_\epsilon(r)`$ and the speed are stated for $`\lVert J\rVert>0`$; the case $`\lVert J\rVert=0`$ is added.
- Steps 1–5 and 7 are unchanged. Tags (7.1)–(7.21) keep their meaning; (7.22)–(7.25) are new. Checks 1 and 2 are extended to the new results.

## Response to verification

- **I1: Accepted.** Step 10 fixes the chain first and takes all delays at once. Result: yes for $`n=2`$, (7.25). For $`n\ge3`$ and different cells, (7.24) proves that a generic chain can fail only at blind delays (7.23); whether generic chains have blind delays, and the same-cell pairs for $`n\ge3`$, are not decided. Result item 4 marks the sub-item as incomplete for exactly these cases. The fixed-delay result (7.20) and the countable-delay remark are kept distinct in Step 9 (ii).
- **I2: Accepted and fixed in Step 9 (ii)**, paragraph "Fixed $`C`$": both alternatives of (7.14) are stated.
- **I3: Accepted and fixed in Step 6 (a)** ($`m=1`$ gives $`\delta P=0`$; (7.9) is stated for $`m\ge2`$) **and in Step 8** ($`\lVert J\rVert>0`$ for the root and the speed; $`\lVert J\rVert=0`$ treated separately).
- **I4: Accepted and fixed in Step 6 (c)** and Result item 3: only the bound with the factor $`1-1/m`$ is attained at leading order, for $`m=2`$.

## Setup and assumptions

- **Model** (setting of the question). Cells $`1,\dots,n`$ ($`n\ge2`$), each the only instance of its type, with place sets $`H_i`$, $`d_i\ge2`$, and $`C=\sum_{i=1}^nD_i+\sum_{i=1}^{n-1}J_i`$, where $`D_i`$ acts on cell $`i`$, $`J_i`$ on cells $`i,i+1`$, and $`\lVert J\rVert:=\max_i\lVert J_i\rVert`$. No two objects share a type, so (1.11) imposes nothing: $`\mathcal H_{\rm adm}=\mathcal H`$. Cells are distinguished by their types, not by labels (M6).
- **Readings.** $`R_i`$ on cell $`i`$ at $`\lambda_1`$ has outcomes $`s`$ and projectors $`\Pi_s:=\Pi^{(i)}_s`$ ($`m`$ classes). $`R_j`$ on cell $`j`$ at $`\lambda_2`$ has outcomes $`t`$ and projectors $`\Pi'_t:=\Pi^{(j)}_t`$. Here $`t`$ is the question's $`r'`$, renamed so that it does not clash with the distance $`r:=\lvert i-j\rvert`$. Readings are partitions of places (A4), so all reading projectors are diagonal in the joint place basis. The delay is $`\delta:=\lambda_2-\lambda_1`$.
- **Start** (A8, A9). The start is the state $`\Psi_0`$ at some $`\lambda_0\le\min(\lambda_1,\lambda_2)`$. Readings act in increasing order of $`\lambda`$, and (1.9) acts between them. For $`\lambda_1\le\lambda_2`$ let $`\Psi_1:=e^{-\mathrm iC(\lambda_1-\lambda_0)}\Psi_0`$. This map is a bijection of unit vectors, so "for every start" means "for every unit vector $`\Psi_1`$". Outcomes of probability $`0`$ contribute nothing to outcome averages.
- **Notation.** $`\mathrm i`$ is the imaginary unit; the letter $`i`$ always denotes a cell. $`\mathrm{ad}_XY:=[X,Y]`$, $`X(\delta):=e^{\mathrm iC\delta}Xe^{-\mathrm iC\delta}`$ and $`\mathcal M_i(X):=\sum_s\Pi_sX\Pi_s`$. The support of an operator is the set of cells on which it acts nontrivially. Operators with disjoint supports commute, and $`\mathrm{supp}[X,Y]\subseteq\mathrm{supp}X\cup\mathrm{supp}Y`$.
- **M6.** Every quantity below depends on $`\Psi_1`$ only through $`\lvert\Psi_1\rangle\langle\Psi_1\rvert`$. It depends on the contracts only through $`C`$, except where the split into $`D`$'s and $`J`$'s is used; there, independence of the split is shown.
- **Genericity** (Steps 9 and 10). "Generic" means: outside a set of Lebesgue measure zero (a null set) in the real parameter space of the contract terms. Step 10 makes this precise.
- **Inputs:** none; the package builds only on the base problem.

## Derivation

### Step 1. Outcome-averaged influence

Let $`\delta\ge0`$, $`U:=e^{-\mathrm iC\delta}`$ and $`Q_t:=\Pi'_t(\delta)=U^\dagger\Pi'_tU`$. By (1.3), outcome $`s`$ of $`R_i`$ occurs with probability $`\lVert\Pi_s\Psi_1\rVert^2`$ and leaves $`\Pi_s\Psi_1/\lVert\Pi_s\Psi_1\rVert`$. This state evolves by $`U`$, and $`R_j`$ then gives $`t`$ with probability $`\lVert\Pi'_tU\Pi_s\Psi_1\rVert^2/\lVert\Pi_s\Psi_1\rVert^2`$. Averaging over $`s`$ gives $`P_j(t\mid R_i)=\sum_s\lVert\Pi'_tU\Pi_s\Psi_1\rVert^2=\langle\Psi_1\vert\mathcal M_i(Q_t)\vert\Psi_1\rangle`$, while $`P_j(t)=\langle\Psi_1\vert Q_t\vert\Psi_1\rangle`$. Using $`\sum_s\Pi_s=\mathbb 1`$:

```math
\Delta_t:=P_j(t\mid R_i)-P_j(t)=\langle\Psi_1\vert\,\mathcal M_i(Q_t)-Q_t\,\vert\Psi_1\rangle,\qquad \mathcal M_i(X)-X=\sum_s\Pi_s\,[X,\Pi_s].
\qquad\text{(7.1)}
```

Hence $`\mathcal M_i(X)=X`$ if and only if $`[X,\Pi_s]=0`$ for all $`s`$: if $`\mathcal M_i(X)=X`$, then $`X`$ is block diagonal. Moreover $`\delta P=\sum_t\lvert\Delta_t\rvert`$ and $`\sum_t\Delta_t=0`$.

### Step 2. No influence without delay (item 1)

- **$`\lambda_2=\lambda_1`$.** Here $`Q_t=\Pi'_t`$. Both $`\Pi'_t`$ and $`\Pi_s`$ are diagonal in the joint place basis, so they commute, and $`\Delta_t=0`$ by (7.1). This holds for all $`i,j`$, including $`i=j`$. The order in which the two readings are applied does not matter.
- **$`\lambda_2<\lambda_1`$.** $`R_j`$ acts first, on the state $`\Psi_2`$ at $`\lambda_2`$. $`R_i`$ acts after the evolution $`U':=e^{-\mathrm iC(\lambda_1-\lambda_2)}`$. The joint probability of $`t`$ and then $`s`$ is $`\lVert\Pi_sU'\Pi'_t\Psi_2\rVert^2`$. Summed over $`s`$, it gives $`\lVert U'\Pi'_t\Psi_2\rVert^2=\lVert\Pi'_t\Psi_2\rVert^2=P_j(t)`$.

```math
P_j(\cdot\mid R_i)=P_j(\cdot)\qquad\text{whenever }\lambda_2\le\lambda_1,\ \text{for all cells } i,j,\ \text{all starts and all readings.}
\qquad\text{(7.2)}
```

### Step 3. Locality of nested commutators

Let $`i>j`$. Expand $`\mathrm{ad}_C^k\Pi'_t=\sum\mathrm{ad}_{X_k}\cdots\mathrm{ad}_{X_1}\Pi'_t`$ with every $`X_l\in\{D_1,\dots,D_n,J_1,\dots,J_{n-1}\}`$. After $`l`$ commutators, the support of a term lies in cells $`\le b_l`$, with $`b_0=j`$. A commutator with $`X_l`$ is nonzero only if $`\mathrm{supp}X_l`$ meets the current support. Among such terms, only $`X_l=J_{b_{l-1}}`$ reaches cell $`b_{l-1}+1`$. Hence $`b_l\le b_{l-1}+1`$, with equality only for $`X_l=J_{b_{l-1}}`$. A term that fails to commute with $`\Pi_s`$ needs $`b_k\ge i=j+r`$. Therefore

```math
[\mathrm{ad}_C^k\Pi'_t,\Pi_s]=0\ \ (k<r),\qquad [\mathrm{ad}_C^r\Pi'_t,\Pi_s]=[K_t,\Pi_s],\qquad K_t:=\mathrm{ad}_{J_{i-1}}\cdots\mathrm{ad}_{J_{j+1}}\mathrm{ad}_{J_j}\Pi'_t .
\qquad\text{(7.3)}
```

For $`i<j`$, the mirror argument gives $`K_t:=\mathrm{ad}_{J_i}\cdots\mathrm{ad}_{J_{j-2}}\mathrm{ad}_{J_{j-1}}\Pi'_t`$. Another booking (A5) replaces $`J_m`$ by $`J_m+D_m`$ or by $`J_m+D_{m+1}`$. This adds only terms with $`b_r<i`$, so $`[K_t,\Pi_s]`$ depends neither on the booking (M6) nor on the $`D`$'s.

### Step 4. Order of the influence (item 2)

In finite dimension, $`Q_t=\sum_{k\ge0}\frac{(\mathrm i\delta)^k}{k!}\mathrm{ad}_C^k\Pi'_t`$ converges for every $`\delta`$. Inserting this series into (7.1) and using (7.3):

```math
\Delta_t=\Gamma_t\,\delta^r+O(\delta^{r+1}),\qquad
\Gamma_t=\frac{1}{r!}\langle\Psi_1\vert\,\mathcal M_i(\mathrm i^rK_t)-\mathrm i^rK_t\,\vert\Psi_1\rangle=\frac{1}{r!}\mathrm{Tr}\bigl[(\mathcal M_i(V)-V)\,\mathrm i^rK_t\bigr],
\qquad\text{(7.4)}
```

```math
\delta P=\delta^r\sum_t\lvert\Gamma_t\rvert+O(\delta^{r+1}).
\qquad\text{(7.5)}
```

- **Second form of (7.4).** $`V`$ is the view (1.5), at $`\lambda_1`$, of the part formed by the cells from $`j`$ to $`i`$. The second form holds because $`K_t`$ and $`\Pi_s`$ act inside this part and the partial trace commutes with $`\mathcal M_i`$.
- **Properties of $`\Gamma_t`$.** $`\Gamma_t`$ is real, because $`\mathrm i\,\mathrm{ad}_{J}`$ and $`\mathcal M_i`$ map self-adjoint operators to self-adjoint ones. Also $`\sum_t\Gamma_t=0`$, because $`\sum_t\Pi'_t=\mathbb 1`$ gives $`\sum_tK_t=0`$.
- **Role of the reading.** $`V-\mathcal M_i(V)=\sum_{s\neq s'}\Pi_sV\Pi_{s'}`$ is the part of the view between places of cell $`i`$ in different classes. At leading order, $`R_i`$ therefore acts only through the cross terms that it erases.
- **Answer.** The lowest possible power is $`\delta^r`$, with coefficient $`\sum_t\lvert\Gamma_t\rvert`$. It depends on $`J_j,\dots,J_{i-1}`$, on the projectors and on $`V`$, but not on the $`D_m`$. Step 5 shows that it can be nonzero.

### Step 5. Examples with qubit cells (item 2)

**Conventions.** The cells are qubits with places $`0,1`$. The Pauli matrices are written in the place basis: $`\sigma^z=\lvert0\rangle\langle0\rvert-\lvert1\rangle\langle1\rvert`$, $`\sigma^x=\lvert0\rangle\langle1\rvert+\lvert1\rangle\langle0\rvert`$, $`\sigma^y=-\mathrm i\lvert0\rangle\langle1\rvert+\mathrm i\lvert1\rangle\langle0\rvert`$, so that $`[\sigma^z,\sigma^x]=2\mathrm i\sigma^y`$. The states $`\lvert+\rangle=(\lvert0\rangle+\lvert1\rangle)/\sqrt2`$ and $`\lvert{+\mathrm i}\rangle=(\lvert0\rangle+\mathrm i\lvert1\rangle)/\sqrt2`$ satisfy $`\langle\sigma^x\rangle_+=1`$ and $`\langle\sigma^y\rangle_{+\mathrm i}=1`$.

**Family.** Take $`n=r+1`$, $`i=1`$, $`j=r+1`$, and place readings on both cells, so that $`\Pi'_{0,1}=(\mathbb 1\pm\sigma^z_{r+1})/2`$. The $`D_m`$ are arbitrary, $`g>0`$, and

```math
J_1=g\,\sigma^x_1\sigma^x_2,\qquad J_m=g\,\sigma^z_m\sigma^x_{m+1}\ \ (2\le m\le r),\qquad \lVert J\rVert=g.
\qquad\text{(7.6)}
```

**Coefficient.** For $`m\ge2`$, $`\mathrm i\,\mathrm{ad}_{J_m}`$ maps $`\sigma^z_{m+1}\sigma^y_{m+2}\cdots\sigma^y_{r+1}`$ to $`2g\,\sigma^z_m\sigma^y_{m+1}\cdots\sigma^y_{r+1}`$. Then $`\mathrm i\,\mathrm{ad}_{J_1}`$ maps $`\sigma^z_2\cdots`$ to $`2g\,\sigma^x_1\sigma^y_2\cdots`$. Hence $`\mathrm i^rK_0=-\mathrm i^rK_1=2^{r-1}g^r\,\sigma^x_1\sigma^y_2\cdots\sigma^y_{r+1}`$. $`\mathcal M_1`$ annihilates this operator, because $`\sum_s\Pi_s\sigma^x\Pi_s=0`$. With $`\Psi_1=\lvert+\rangle\otimes\lvert{+\mathrm i}\rangle^{\otimes r}`$, (7.4) and (7.5) give

```math
\Gamma_0=-\Gamma_1=-\frac{2^{r-1}g^r}{r!},\qquad \delta P=\frac{(2g\delta)^r}{r!}+O(\delta^{r+1})\qquad(r\ge1).
\qquad\text{(7.7)}
```

- **$`r=1`$.** Take $`n=2`$, $`J_1=g\sigma^x_1\sigma^x_2`$ and $`\Psi_1=\lvert+\rangle\lvert{+\mathrm i}\rangle`$. Then $`\delta P=2g\delta+O(\delta^2)`$. For $`D_1=D_2=0`$ the result is exact: $`\sigma^z_2`$ anticommutes with $`J_1`$, so $`Q_0=\tfrac12\bigl(\mathbb 1+\cos(2g\delta)\,\sigma^z_2+\sin(2g\delta)\,\sigma^x_1\sigma^y_2\bigr)`$, and

```math
\delta P=\lvert\sin(2g\delta)\rvert\qquad(n=2,\ D_1=D_2=0,\ J_1=g\sigma^x_1\sigma^x_2,\ \Psi_1=\lvert+\rangle\lvert{+\mathrm i}\rangle).
\qquad\text{(7.8)}
```

- **$`r=2`$.** Take $`n=3`$, $`J_1=g\sigma^x_1\sigma^x_2`$, $`J_2=g\sigma^z_2\sigma^x_3`$ and $`\Psi_1=\lvert+\rangle\lvert{+\mathrm i}\rangle\lvert{+\mathrm i}\rangle`$. Then $`\delta P=2g^2\delta^2+O(\delta^3)`$.

The power $`\delta^r`$ in (7.5) is thus attained for every $`r\ge1`$.

### Step 6. Bound (item 3)

**(a) Reduction.** Let $`\epsilon_t:=\mathrm{sgn}\Delta_t`$ and $`Z:=\sum_t\epsilon_t\Pi'_t`$, which acts on cell $`j`$ and has $`\lVert Z\rVert\le1`$. By linearity of (7.1), $`\delta P=\langle\Psi_1\vert\mathcal M_i(Z(\delta))-Z(\delta)\vert\Psi_1\rangle\le\lVert\mathcal M_i(Z(\delta))-Z(\delta)\rVert`$.

- **One class, $`m=1`$.** Then $`\Pi_1=\mathbb 1`$, $`\mathcal M_i`$ is the identity map and $`\delta P=0`$ for all $`\delta`$: a reading with one outcome influences nothing.
- **$`m\ge2`$.** Label the classes of $`R_i`$ by $`s=0,\dots,m-1`$, let $`\omega:=e^{2\pi\mathrm i/m}`$, and define $`W_k:=\sum_s\omega^{ks}\Pi_s`$. These are unitaries on cell $`i`$, with $`W_0=\mathbb 1`$. Since $`\frac1m\sum_k\omega^{k(s-s')}`$ is $`1`$ for $`s=s'`$ and $`0`$ otherwise, $`\mathcal M_i(X)=\frac1m\sum_kW_kXW_k^\dagger`$. Hence $`\mathcal M_i(X)-X=\frac1m\sum_{k=1}^{m-1}[W_k,X]W_k^\dagger`$, and

```math
\delta P\le\Bigl(1-\frac1m\Bigr)\max_{1\le k<m}\bigl\lVert[Z(\delta),W_k]\bigr\rVert\qquad(m\ge2).
\qquad\text{(7.9)}
```

**(b) Commutator bound** (Lieb–Robinson type). Let $`A`$ act on cell $`j`$ and $`B`$ on cell $`i=j+r>j`$.

- **Truncated evolutions.** For $`m\ge j`$, let $`C_{\le m}:=\sum_{l\le m}D_l+\sum_{l<m}J_l`$ be the terms inside cells $`1,\dots,m`$, so that $`C_{\le n}=C`$. Let $`A_m(\mu):=e^{\mathrm iC_{\le m}\mu}Ae^{-\mathrm iC_{\le m}\mu}`$; it is supported in cells $`\le m`$.
- **Duhamel step.** $`C_{\le m}-C_{\le m-1}=D_m+J_{m-1}`$, and $`D_m`$ commutes with $`A_{m-1}(\mu)`$. Hence $`\frac{\mathrm d}{\mathrm d\mu}\bigl[e^{\mathrm iC_{\le m}(\delta-\mu)}A_{m-1}(\mu)e^{-\mathrm iC_{\le m}(\delta-\mu)}\bigr]=-\mathrm i\,e^{\mathrm iC_{\le m}(\delta-\mu)}[J_{m-1},A_{m-1}(\mu)]e^{-\mathrm iC_{\le m}(\delta-\mu)}`$. Integrating over $`\mu\in[0,\delta]`$ gives

```math
\lVert A_m(\delta)-A_{m-1}(\delta)\rVert\le\int_0^\delta\beta_{m-1}(\mu)\,\mathrm d\mu,\qquad \beta_m(\mu):=\bigl\lVert[J_m,A_m(\mu)]\bigr\rVert .
\qquad\text{(7.10)}
```

- **Recursion.** $`J_m`$ commutes with $`A_{m-1}(\mu)`$, which lives on cells $`\le m-1`$. So for $`m>j`$, $`\beta_m(\mu)=\lVert[J_m,A_m(\mu)-A_{m-1}(\mu)]\rVert\le2\lVert J\rVert\int_0^\mu\beta_{m-1}`$, and $`\beta_j\le2\lVert J\rVert\lVert A\rVert`$. By induction, $`\beta_m(\mu)\le2\lVert J\rVert\lVert A\rVert(2\lVert J\rVert\mu)^{m-j}/(m-j)!`$. Then (7.10) gives $`\lVert A_m(\delta)-A_{m-1}(\delta)\rVert\le\lVert A\rVert(2\lVert J\rVert\delta)^{m-j}/(m-j)!`$.
- **Result.** $`[A_{i-1}(\delta),B]=0`$, and $`A(\delta)=A_n(\delta)=A_{i-1}(\delta)+\sum_{m=i}^n\bigl(A_m(\delta)-A_{m-1}(\delta)\bigr)`$. Therefore

```math
\bigl\lVert[A(\delta),B]\bigr\rVert\le2\lVert A\rVert\lVert B\rVert\sum_{k=r}^{\infty}\frac{(2\lVert J\rVert\delta)^k}{k!}\qquad(\delta\ge0,\ r\ge1).
\qquad\text{(7.11)}
```

For $`i<j`$, the same bound follows with $`C_{\ge m}`$, the terms inside cells $`m,\dots,n`$. The bound (7.11) is uniform in $`n`$: the finite sum over $`m`$ is bounded by the series. No $`D_l`$ enters it, since the $`D`$'s appear only inside unitary conjugations, which preserve norms.

**(c) Bound on $`\delta P`$.** Inserting (7.11) with $`A=Z`$ and $`B=W_k`$ into (7.9), and using $`(r+l)!\ge r!\,l!`$ for the last step:

```math
\delta P\le2\Bigl(1-\frac1m\Bigr)\sum_{k\ge r}\frac{(2\lVert J\rVert\delta)^k}{k!}\le2\sum_{k\ge r}\frac{(2\lVert J\rVert\delta)^k}{k!}\le\frac{2\,(2\lVert J\rVert\delta)^r}{r!}\,e^{2\lVert J\rVert\delta}.
\qquad\text{(7.12)}
```

- **Validity.** (7.12) holds for every start, every pair of readings and every $`\delta\ge0`$, with $`r\ge1`$. For $`m=1`$ its first member is $`0`$, in agreement with (a). Trivially, also $`\delta P\le2`$.
- **Dependence on the $`D_i`$.** The bound does not depend on the $`D_i`$.
- **Booking (M6).** (7.12) holds for every split of $`C`$ into single-cell and pair terms, so it holds with the smallest $`\lVert J\rVert`$ over all splits. That value does not depend on the booking.
- **Leading order.** Only the first, reading-dependent member of (7.12) is attained at leading order, and this is shown for $`m=2`$: its first term is then $`(2\lVert J\rVert\delta)^r/r!`$, which equals (7.7). The second and third members, which do not depend on the reading, are not attained: their leading coefficient $`2(2\lVert J\rVert)^r/r!`$ exceeds that of the first member for every finite $`m`$.

### Step 7. Sharpness (item 4)

**Analyticity.** Write the spectral decomposition $`C=\sum_ac_aP_a`$. Then $`\Delta_t(\delta)=\sum_{a,b}e^{\mathrm i(c_a-c_b)\delta}\langle\Psi_1\vert(\mathcal M_i-\mathrm{id})(P_a\Pi'_tP_b)\vert\Psi_1\rangle`$ is an entire function of $`\delta`$ (A1). If $`\delta P=0`$ on $`(0,\varepsilon)`$, every $`\Delta_t`$ vanishes on an interval, hence identically by the identity theorem:

```math
\delta P=0\ \text{on}\ (0,\varepsilon)\ \Longrightarrow\ \delta P=0\ \text{for all}\ \delta\ge0 .
\qquad\text{(7.13)}
```

So $`\delta P`$ cannot vanish on $`(0,\varepsilon)`$ and be nonzero at a larger $`\delta`$. For a fixed start and fixed readings, either $`\delta P\equiv0`$, or the zeros of $`\delta P`$ in $`(0,\infty)`$ are isolated and $`\delta P\simeq c\,\delta^q`$ near $`0`$, with $`c>0`$ and $`q\ge r`$.

**Delay sets.** Let $`\mathcal I_{ij}`$ be the set of $`\delta>0`$ for which some start and some readings give $`\delta P>0`$. Its complement in $`(0,\infty)`$ is contained in the zero set of one $`\delta P\not\equiv0`$. Hence, for $`r\ge0`$:

```math
\mathcal I_{ij}=\emptyset\quad\text{or}\quad \mathcal I_{ij}=(0,\infty)\setminus E_{ij},\ \ E_{ij}\ \text{discrete in }[0,\infty),\ \ E_{ij}\cap(0,\delta_0)=\emptyset\ \text{for some}\ \delta_0>0 .
\qquad\text{(7.14)}
```

**Conclusion: no sharp boundary.** By (7.7), for every $`r\ge1`$ there are chains with $`\mathcal I_{ij}\supseteq(0,\delta_0)`$. So no cone $`\{\delta\ge r/v\}`$ with finite $`v`$ contains all influence. The only sharp boundary is $`\delta=0`$, from (7.2). In the distance $`r`$ the order is approximate: influence outside the cone of Step 8 is small, but it is not zero.

### Step 8. Region of small influence and its speed (item 4)

**The set.** By (7.12), $`\delta P<\epsilon`$ for every start and every pair of readings on

```math
\mathcal S_\epsilon:=\Bigl\{(r,\delta):\ r\ge1,\ \delta\ge0,\ 2\sum_{k\ge r}\frac{(2\lVert J\rVert\delta)^k}{k!}<\epsilon\Bigr\}=\bigl\{(r,\delta):\ 0\le\delta<\delta_\epsilon(r)\bigr\}.
\qquad\text{(7.15)}
```

- **$`\lVert J\rVert>0`$.** $`\delta_\epsilon(r)`$ is the unique root of $`2\sum_{k\ge r}(2\lVert J\rVert\delta)^k/k!=\epsilon`$. The left side increases strictly in $`\delta`$, from $`0`$ to $`\infty`$, and decreases in $`r`$; hence $`\delta_\epsilon(r)`$ increases with $`r`$.
- **$`\lVert J\rVert=0`$** (in some booking: $`C`$ is a sum of single-cell terms). Then (7.12) gives $`\delta P\equiv0`$ for all $`r\ge1`$. $`\mathcal S_\epsilon`$ is the whole domain, $`\delta_\epsilon(r)=\infty`$, and there is no boundary and no speed.

**Explicit inner cone.** Let $`v>2e\lVert J\rVert`$ and $`u:=2\lVert J\rVert/v<1/e`$. For $`\delta\le r/v`$, $`x:=2\lVert J\rVert\delta\le ur`$, so the terms $`x^k/k!`$ with $`k\ge r`$ decrease with ratio $`\le u`$. Using $`r!\ge(r/e)^r`$, $`\sum_{k\ge r}x^k/k!\le x^r/(r!(1-u))\le(eu)^r/(1-u)`$. Hence

```math
\delta P\le\frac{2}{1-2\lVert J\rVert/v}\Bigl(\frac{2e\lVert J\rVert}{v}\Bigr)^{r}\qquad\text{for all starts, readings and } 0\le\delta\le r/v ,
\qquad\text{(7.16)}
```

which is exponentially small in $`r`$.

**Outside** ($`\lVert J\rVert>0`$). Conversely, let $`v<2e\lVert J\rVert`$ and $`\delta=r/v`$. Using $`r!\le e\sqrt r\,(r/e)^r`$, the bound is at least $`2(2\lVert J\rVert\delta)^r/r!\ge\frac{2}{e\sqrt r}\bigl(\frac{2e\lVert J\rVert}{v}\bigr)^r\to\infty`$. So $`(r,r/v)\notin\mathcal S_\epsilon`$ for large $`r`$.

**Speed** ($`\lVert J\rVert>0`$). Together, for every $`\epsilon>0`$ the boundary moves at

```math
\lim_{r\to\infty}\frac{r}{\delta_\epsilon(r)}=v_{\rm LR}:=2e\lVert J\rVert\quad\text{cells per unit }\lambda .
\qquad\text{(7.17)}
```

This speed is independent of $`\epsilon`$, of $`n`$ (uniformity of (7.11)) and of the $`D_i`$.

### Step 9. The order of events (item 4)

An event is a pair $`e=(i,\lambda)`$ of a cell and a value of $`\lambda`$, at which a reading is applied. Following the question,

```math
(i,\lambda_1)\prec(j,\lambda_2)\ :\Longleftrightarrow\ \text{some reading at }(i,\lambda_1)\text{ influences some reading at }(j,\lambda_2)\text{ for some start.}
\qquad\text{(7.18)}
```

**(i) Order in $`\lambda`$.** By (7.2):

```math
e_1\prec e_2\ \Longrightarrow\ \lambda_1<\lambda_2 .
\qquad\text{(7.19)}
```

**(ii) Pairs with $`\lambda_1<\lambda_2`$: one prescribed delay.**

- **Criterion.** By (7.1) and Step 1, influence occurs for some start if and only if some $`\mathcal M_i(Q_t)-Q_t\neq0`$; for $`\Psi_1`$ one takes an eigenvector of this self-adjoint operator for a nonzero eigenvalue. Equivalently, some $`Q_t`$ fails to commute with some $`\Pi_s`$. Coarse projectors are sums of place projectors $`p_h`$, so it suffices to test place readings. Hence $`e_1\prec e_2`$ if and only if $`F_\delta(C):=\sum_{h,h'}\lVert[\,p^{(j)}_{h'}(\delta),\,p^{(i)}_h\,]\rVert_{2}^{2}>0`$, with $`\lVert\cdot\rVert_2`$ the Hilbert–Schmidt norm.
- **Analyticity in the contract terms.** $`F_\delta`$ is real-analytic in the real parameters of $`(D_1,\dots,D_n,J_1,\dots,J_{n-1})`$. By A5 the $`D`$'s are booked in pair terms, so these are the parameters of the pair terms. Also $`F_\delta(C)=F_1(\delta C)`$.
- **$`F_\delta\not\equiv0`$, case $`r\ge1`$.** Place the chain (7.6) on the cells between $`i`$ and $`j`$, mirrored if $`i>j`$. For $`d>2`$ it acts on places $`0,1`$; all other terms are $`0`$. Then $`F_{\delta'}>0`$ for small $`\delta'`$ by (7.7), and rescaling $`C`$ by $`\delta'/\delta`$ gives $`F_\delta>0`$.
- **$`F_\delta\not\equiv0`$, case $`r=0`$.** Take $`D_i=g\sigma^x_i`$ and all other terms zero. Then $`p^{(i)}_0(\delta)`$ fails to commute with $`p^{(i)}_0`$ unless $`\sin(2g\delta)=0`$.
- **Fixed-delay statement.** The zero set of a nonzero real-analytic function has measure zero. Hence:

```math
\text{for fixed } i,j \text{ and } \lambda_1<\lambda_2:\ \ e_1\prec e_2\ \text{for all contract terms outside a closed set of measure zero.}
\qquad\text{(7.20)}
```

- **What (7.20) does not say.** Its null set depends on $`i`$, $`j`$ and $`\delta`$. It does not state that one generic chain has influence at all delays. A countable union of null sets is null, so a generic chain has no exceptional delay in any prescribed countable set, for example at rational delays; in particular $`\mathcal I_{ij}\neq\emptyset`$ for all $`i,j`$ for a generic chain. All real delays at once are the subject of Step 10.
- **Fixed $`C`$.** By (7.14) there are two cases for each pair of cells.
  - $`\mathcal I_{ij}=\emptyset`$: then $`e_1\nprec e_2`$ at every delay. Example: a cut link between $`i\neq j`$ (check 1).
  - $`\mathcal I_{ij}\neq\emptyset`$: the pairs with $`\lambda_1<\lambda_2`$ but $`e_1\nprec e_2`$ are those with $`\lambda_2-\lambda_1\in E_{ij}`$. There are none for $`0<\lambda_2-\lambda_1<\delta_0`$, and they form a discrete set otherwise.
- **Exceptional delays exist.** For $`n=2`$, $`D=0`$ and $`J_1=g\sigma^x_1\sigma^x_2`$, the evolution $`e^{-\mathrm iC\pi/(2g)}=-\mathrm i\sigma^x_1\sigma^x_2`$ is a product of single-cell unitaries. Every $`p_h(\pi/(2g))`$ is then a place projector of its own cell, so no reading influences any other at delay $`\pi/(2g)`$.

**(iii) Transitivity.** In the same chain, by (7.8) at $`2g\delta=\pi/2`$ and by the $`1\leftrightarrow2`$ symmetry of $`C`$ (start $`\lvert{+\mathrm i}\rangle\lvert+\rangle`$ for the second relation), together with (ii):

```math
e_1=(1,0)\prec e_2=\bigl(2,\tfrac{\pi}{4g}\bigr)\prec e_3=\bigl(1,\tfrac{\pi}{2g}\bigr),\qquad e_1\nprec e_3\qquad(n=2,\ D=0,\ J_1=g\sigma^x_1\sigma^x_2).
\qquad\text{(7.21)}
```

So $`\prec`$ is not transitive in general. If all $`\mathcal I_{ij}\neq\emptyset`$ and all $`E_{ij}=\emptyset`$, then (7.14) and (7.19) give $`e_1\prec e_2\Leftrightarrow\lambda_1<\lambda_2`$, which is transitive; by (7.25) this is the generic case for $`n=2`$. If all $`\mathcal I_{ij}\neq\emptyset`$, a triple can violate transitivity only if $`\lambda_3-\lambda_1`$ lies in the discrete set $`E_{ik}`$.

### Step 10. One fixed chain and all delays (item 4)

Here the chain is fixed first and all delays $`\delta>0`$ are taken at once. Uncountably many delays cannot be handled by a union of the null sets of (7.20).

**Setting.**
- $`\mathcal P:=\sum_{m=1}^{n-1}\mathrm{Herm}(\mathcal H_m\otimes\mathcal H_{m+1})\otimes\mathbb 1`$ is the real vector space of all $`C`$ of the chain form, with the Lebesgue measure $`\mathrm{vol}`$ of the Hilbert–Schmidt inner product. **Generic** means: outside a null set of $`\mathcal P`$. The map $`(J_1,\dots,J_{n-1})\mapsto C`$, with the $`D`$'s booked by A5, is linear and onto, so a null set of $`\mathcal P`$ is a null set of pair terms. The sets below depend on $`C`$ only (M6).
- $`\mathcal O_k`$ is the algebra of all operators on cell $`k`$, extended by the identity. $`\mathcal D_k\subset\mathcal O_k`$ is the span of the place projectors $`p^{(k)}_h`$. $`U_\delta:=e^{-\mathrm iC\delta}`$.
- A set has **codimension $`\ge2`$** in a manifold if it lies in a countable union of submanifolds of codimension $`\ge2`$.

By the criterion of Step 9 (ii), $`(i,\lambda_1)\nprec(j,\lambda_1+\delta)`$ if and only if $`[U_\delta^\dagger\mathcal D_jU_\delta,\mathcal D_i]=0`$. The chains with an exceptional delay are

```math
\mathcal X_{ij}:=\bigl\{C\in\mathcal P:\ [U_\delta^\dagger\mathcal D_jU_\delta,\mathcal D_i]=0\ \text{for some }\delta>0\bigr\},\qquad \mathcal X:=\bigcup_{i,j=1}^{n}\mathcal X_{ij}.
\qquad\text{(7.22)}
```

With (7.19): $`C\notin\mathcal X`$ if and only if $`e_1\prec e_2\Leftrightarrow\lambda_1<\lambda_2`$ for all events. The question is whether $`\mathcal X`$ is null. A delay is **blind** for $`(i,j)`$ if nothing on cell $`i`$ influences anything on cell $`j`$, whatever the place bases:

```math
\Lambda^{ij}_C:=\bigl\{\delta>0:\ [U_\delta^\dagger\mathcal O_jU_\delta,\mathcal O_i]=0\bigr\},\qquad \mathcal X^{\rm bl}_{ij}:=\{C\in\mathcal P:\ \Lambda^{ij}_C\neq\emptyset\}\subseteq\mathcal X_{ij}.
\qquad\text{(7.23)}
```

$`\Lambda^{ij}_C`$ is closed in $`(0,\infty)`$. All sets of chains used below are projections of countable unions of compact sets, hence measurable.

**(a) Three tools.**

- **T1 (rotation).** Let $`\mathcal G`$ be a compact group of unitaries with $`W\mathcal PW^\dagger=\mathcal P`$. Conjugation preserves the Hilbert–Schmidt norm, hence $`\mathrm{vol}`$. By Tonelli's theorem, $`\mathrm{vol}(\mathcal Y)=\int_{\mathcal P}\mathrm dC\,\mathrm{Haar}\{W\in\mathcal G:\ WCW^\dagger\in\mathcal Y\}`$ for every measurable $`\mathcal Y\subseteq\mathcal P`$. So $`\mathcal Y`$ is null if this Haar measure vanishes for almost every $`C`$.
- **T2 (one-parameter union).** Let $`I\subseteq(0,\infty)`$ be open, and let $`\Phi\ge0`$ be real-analytic on $`I\times\mathcal G`$ such that $`\{W:\Phi(\delta,W)=0\}`$ has codimension $`\ge2`$ in $`\mathcal G`$ for every $`\delta\in I`$. Then $`\{W:\ \Phi(\delta,W)=0\text{ for some }\delta\in I\}`$ is Haar-null. Reason: the zero set of $`\Phi`$ is a countable union of submanifolds $`S`$ (stratification of analytic sets). By the rank theorem, $`S`$ has fibres over $`\delta`$ of dimension $`\ge\dim S-1`$, and they lie in a set of dimension $`\le\dim\mathcal G-2`$. So $`\dim S\le\dim\mathcal G-1`$, and the projection of $`S`$ to $`\mathcal G`$ is null (Sard).
- **T3 (bases inside a subalgebra).** Let $`\mathcal S\subsetneq M_d`$ be a unital $`*`$-subalgebra. The $`W\in U(d)`$ with $`W^\dagger\lvert h\rangle\langle h\rvert W\in\mathcal S`$ for all $`h`$ form a set of codimension $`\ge2`$. Reason: $`\mathcal S\cong\bigoplus_kM_{m_k}\otimes\mathbb 1_{r_k}`$ (structure theorem). It contains $`d`$ orthogonal rank-one projectors only if all $`r_k=1`$, that is, $`\mathcal S=\bigoplus_kM(V_k)`$ for an orthogonal decomposition $`\mathbb C^d=\bigoplus_kV_k`$ with at least two blocks. The bases adapted to it form a set of dimension $`\sum_km_k^2\le(d-1)^2+1\le d^2-2`$.

**(b) Different cells, every $`n`$.** Let $`i\neq j`$ and $`\mathcal G=\{W_i\otimes W_j\}\cong U(d_i)\times U(d_j)`$, acting on cells $`i,j`$. It preserves $`\mathcal P`$ and the algebras $`\mathcal O_k`$, so $`\Lambda^{ij}_{WCW^\dagger}=\Lambda^{ij}_C`$. Since $`e^{-\mathrm iWCW^\dagger\delta}=WU_\delta W^\dagger`$, the chain $`WCW^\dagger`$ has no influence from $`i`$ to $`j`$ at delay $`\delta`$ if and only if $`[U_\delta^\dagger\mathcal A_jU_\delta,\mathcal A_i]=0`$ with $`\mathcal A_k:=W_k^\dagger\mathcal D_kW_k`$. Rotating the contracts is the same as rotating the place bases of cells $`i`$ and $`j`$. Fix $`\delta\notin\Lambda^{ij}_C`$ and write $`U=U_\delta`$.

- For fixed $`W_i`$, $`\mathcal S:=\{a\in\mathcal O_j:\ [U^\dagger aU,\mathcal A_i]=0\}`$ is a unital $`*`$-subalgebra of $`\mathcal O_j\cong M_{d_j}`$, and $`W`$ is bad if and only if $`W_j^\dagger p^{(j)}_hW_j\in\mathcal S`$ for all $`h`$. By T3 the bad $`W_j`$ have codimension $`\ge2`$ in $`U(d_j)`$, unless $`\mathcal S=\mathcal O_j`$.
- $`\mathcal S=\mathcal O_j`$ if and only if $`\mathcal A_i\subseteq\mathcal S':=\{b\in\mathcal O_i:\ [U^\dagger\mathcal O_jU,b]=0\}`$. This is a unital $`*`$-subalgebra of $`\mathcal O_i`$, and it is proper because $`\delta`$ is not blind. By T3 such $`W_i`$ have codimension $`\ge2`$ in $`U(d_i)`$.

So at every delay that is not blind, the bad $`W`$ have codimension $`\ge2`$ in $`\mathcal G`$. T2 with $`I=(0,\infty)\setminus\Lambda^{ij}_C`$ and $`\Phi(\delta,W)=F_\delta(WCW^\dagger)`$, followed by T1, gives

```math
\mathrm{vol}\bigl\{C\in\mathcal P:\ [U_\delta^\dagger\mathcal D_jU_\delta,\mathcal D_i]=0\ \text{for some }\delta>0\text{ with }\delta\notin\Lambda^{ij}_C\bigr\}=0\qquad(i\neq j,\ n\ge2).
\qquad\text{(7.24)}
```

For a generic chain, a positive delay without influence between two different cells is therefore a blind delay. In particular $`\mathcal X_{ij}\setminus\mathcal X^{\rm bl}_{ij}`$ is null.

**(c) Two cells, $`n=2`$.** Now $`\mathcal P=\mathrm{Herm}(\mathcal H)`$, $`N:=d_1d_2\ge4`$, and T1 applies with $`\mathcal G=U(N)`$. Let (G) be the property: the eigenvalues $`c_a`$ of $`C`$ are simple, and no two gaps $`c_a-c_b`$, $`c_{a'}-c_{b'}`$ with $`\{a,b\}\neq\{a',b'\}`$ have a rational ratio. (G) holds for almost every $`C`$ (it excludes countably many hyperplanes of spectra) and is invariant under conjugation. Under (G), at most one pair of the numbers $`e^{-\mathrm ic_a\delta}`$ coincides at any $`\delta>0`$, so $`U_\delta`$ has at least $`N-1\ge3`$ distinct eigenvalues.

- **No blind delays.** For $`n=2`$ the commutant of $`\mathcal O_1`$ is $`\mathcal O_2`$. So $`[U^\dagger\mathcal O_2U,\mathcal O_1]=0`$ gives $`U^\dagger\mathcal O_2U=\mathcal O_2`$ (equal dimensions), then $`U^\dagger\mathcal O_1U=\mathcal O_1`$ (commutants), and $`U=u_1\otimes u_2`$ because automorphisms of full matrix algebras are inner. Hence $`\delta`$ is blind for $`VCV^\dagger`$ if and only if $`VZV^\dagger`$ is a product unitary, with $`Z=U_\delta`$. Let $`Z`$ be any non-scalar unitary with eigenvalues $`z_a`$.
  - $`V\mapsto VZV^\dagger`$ is a fibration of $`U(N)`$ over the conjugacy class of $`Z`$, of dimension $`\#\{(a,b):z_a\neq z_b\}`$ (ordered pairs).
  - A product unitary in this class has factors with eigenvalues $`\alpha_k`$ ($`k\le d_1`$) and $`\beta_l`$ ($`l\le d_2`$) such that $`\{\alpha_k\beta_l\}=\{z_a\}`$ as multisets. Up to $`(\alpha,\beta)\to(\tau\alpha,\beta/\tau)`$ there are finitely many such $`(\alpha,\beta)`$. For each, the product unitaries form a set of dimension $`\le n_\alpha+n_\beta`$, with $`n_\alpha:=\#\{(k,k'):\alpha_k\neq\alpha_{k'}\}`$ and $`n_\beta`$ likewise.
  - The class has dimension $`\#\{(kl,k'l'):\alpha_k\beta_l\neq\alpha_{k'}\beta_{l'}\}\ge d_2n_\alpha+d_1n_\beta`$ (pairs with $`l=l'`$, and pairs with $`k=k'`$). So the codimension is $`\ge(d_2-1)n_\alpha+(d_1-1)n_\beta\ge n_\alpha+n_\beta\ge2`$, since $`n_\alpha+n_\beta`$ is even and nonzero for non-scalar $`Z`$.

  So under (G) the bad $`V`$ have codimension $`\ge2`$ at every $`\delta>0`$. By T2 and T1, $`\mathcal X^{\rm bl}_{12}=\mathcal X^{\rm bl}_{21}`$ is null, and by (7.24) $`\mathcal X_{12}`$ and $`\mathcal X_{21}`$ are null.
- **Same cell.** Let $`i=j=1`$; cell $`2`$ is alike with $`d_1\leftrightarrow d_2`$. The chain $`VCV^\dagger`$ has no influence at delay $`\delta`$ if and only if $`[Z^\dagger q_hZ,q_{h'}]=0`$ for all $`h,h'`$, where $`Z=U_\delta`$ and $`q_h:=V^\dagger p^{(1)}_hV`$ projects on $`E_h:=V^\dagger(\lvert h\rangle\otimes\mathcal H_2)`$, of dimension $`d_2`$. Fix one $`h`$. Commuting projectors and $`\sum_{h'}Z^\dagger q_{h'}Z=\mathbb 1`$ give $`E_h=\bigoplus_{h'}\bigl(E_h\cap Z^\dagger E_{h'}\bigr)`$. So $`E:=E_h`$ satisfies (α) or (β):
  - (α) some unit vector $`f\in E`$ has $`Zf\in E_{h'}`$ with $`h'\neq h`$, hence $`Zf\perp E`$;
  - (β) $`ZE=E`$.

  Let $`Z`$ have at least three distinct eigenvalues $`\zeta`$, with eigenprojectors $`\Pi_\zeta`$ and multiplicities $`\mu_\zeta`$. Both sets have codimension $`\ge2`$ in the Grassmannian $`\mathrm{Gr}(d_2,N)`$, of real dimension $`2d_2(N-d_2)`$:
  - (α): $`\langle f\vert Z\vert f\rangle=\sum_\zeta\zeta\,\lVert\Pi_\zeta f\rVert^2=0`$. Three distinct points of the unit circle are not collinear, so these are two independent real conditions on the weights $`\lVert\Pi_\zeta f\rVert^2`$ when at least three weights are nonzero; otherwise $`f`$ lies in the sum of two eigenspaces, a proper subspace. Such $`[f]`$ thus have real dimension $`\le2N-4`$. Given $`f`$, $`E=\mathbb Cf\oplus E'`$ with $`E'\subseteq\{f,Zf\}^\perp`$, a Grassmannian of real dimension $`2(d_2-1)(N-d_2-1)`$. The total is $`\le2N-4+2(d_2-1)(N-d_2-1)=2d_2(N-d_2)-2`$.
  - (β): $`E=\bigoplus_\zeta(E\cap\mathrm{ran}\Pi_\zeta)`$ with dimensions $`k_\zeta`$, $`\sum_\zeta k_\zeta=d_2`$. These $`E`$ have dimension $`2\sum_\zeta k_\zeta(\mu_\zeta-k_\zeta)`$. It is smaller than $`2d_2(N-d_2)=2\sum_{\zeta,\zeta'}k_\zeta(\mu_{\zeta'}-k_{\zeta'})`$ by the even number $`2\sum_{\zeta\neq\zeta'}k_\zeta(\mu_{\zeta'}-k_{\zeta'})`$, which is positive because $`0<d_2<N`$ and $`Z`$ has more than one eigenvalue.

  $`V\mapsto E_h`$ is a fibration of $`U(N)`$ over $`\mathrm{Gr}(d_2,N)`$. So under (G) the bad $`V`$ have codimension $`\ge2`$ at every $`\delta>0`$. By T2 and T1, $`\mathcal X_{11}`$ and $`\mathcal X_{22}`$ are null.

Together:

```math
n=2:\qquad \mathrm{vol}(\mathcal X)=0,\quad\text{that is, for almost every }C:\quad e_1\prec e_2\iff\lambda_1<\lambda_2\ \ \text{for all events.}
\qquad\text{(7.25)}
```

**(d) Longer chains, $`n\ge3`$: what is decided and what is not.**

- **Decided.** (7.24): between different cells, a generic chain has no exceptional delay other than blind delays. Step 9 (ii): for a generic chain every $`\mathcal I_{ij}\neq\emptyset`$, every $`E_{ij}`$ is discrete, and no exceptional delay lies in a prescribed countable set.
- **Undecided (U1).** Whether $`\mathrm{vol}(\mathcal X^{\rm bl}_{ij})=0`$ for $`i\neq j`$, that is, whether a generic chain with $`n\ge3`$ has no blind delay. Blind delays are invariant under all products of single-cell unitaries, so (b) cannot remove them. The proof of (c) conjugates by all of $`U(N)`$, which varies the eigenvectors of $`C`$ at fixed spectrum; for $`n\ge3`$ this does not preserve $`\mathcal P`$.
- **Undecided (U2).** Whether $`\mathrm{vol}(\mathcal X_{ii})=0`$ for $`n\ge3`$ (two readings on the same cell). Here only the one place basis of cell $`i`$ can be rotated, and the bad bases can have codimension $`1`$: for a qubit cell on which $`U_\delta`$ acts as a rotation by $`\pi`$, they form a curve. T2 then does not apply unless such delays are excluded.
- A count of conditions against parameters suggests that both sets are null. A count is not a proof; no chain with $`n\ge3`$ is claimed to be free of exceptional delays.

## Result

1. **Item 1.** $`R_i`$ cannot influence $`R_j`$ when $`\lambda_2=\lambda_1`$, $`i\neq j`$ (no), nor when $`\lambda_2<\lambda_1`$ (no): (7.2). The equal-$`\lambda`$ statement holds even for $`i=j`$.
2. **Item 2.**
   - The influence is $`\Delta_t=\langle\Psi_1\vert\mathcal M_i(Q_t)-Q_t\vert\Psi_1\rangle`$ (7.1).
   - The lowest power is $`\delta^r`$. The exact coefficient $`\Gamma_t`$ of (7.4) is built from the nested commutator $`K_t`$ of the links between the cells (7.3), the projectors and the view of the cells between; $`\delta P`$ is given by (7.5). The $`D_i`$ do not enter.
   - Nonzero examples exist for every $`r\ge1`$, (7.6)–(7.7), including $`r=1`$ (exactly $`\delta P=\lvert\sin 2g\delta\rvert`$, (7.8)) and $`r=2`$ ($`\delta P=2g^2\delta^2+O(\delta^3)`$).
3. **Item 3.** The bound is (7.12): $`\delta P\le2(1-\tfrac1m)\sum_{k\ge r}(2\lVert J\rVert\delta)^k/k!\le2\sum_{k\ge r}(2\lVert J\rVert\delta)^k/k!`$, obtained from the chain Lieb–Robinson bound (7.11). It is uniform in $`n`$ and does not depend on the $`D_i`$. Only the first form, with the number $`m`$ of classes of $`R_i`$, is attained at leading order (for $`m=2`$, by (7.7)); the reading-independent second form is not.
4. **Item 4.**
   - No: $`\delta P`$ cannot vanish on $`(0,\varepsilon)`$ and be nonzero later (7.13).
   - Hence there is no sharp cone: influence at some delay implies influence at all delays except a discrete set, in particular at arbitrarily small ones (7.14). The order is sharp only at $`\delta=0`$.
   - Below $`\epsilon`$ for every start: the set $`\mathcal S_\epsilon`$ (7.15), with explicit inner cone (7.16). For $`\lVert J\rVert>0`$ its boundary moves at $`v_{\rm LR}=2e\lVert J\rVert`$ cells per unit $`\lambda`$ (7.17); for $`\lVert J\rVert=0`$ there is no influence between different cells and no boundary.
   - For $`\prec`$ (7.18):
     - $`\prec`$ implies $`\lambda_1<\lambda_2`$: yes (7.19).
     - Does $`\prec`$ hold for every pair with $`\lambda_1<\lambda_2`$ when the pair terms are generic? Two statements must be kept apart.
       - **One prescribed delay:** yes, outside a null set of contract terms that depends on the delay (7.20).
       - **One fixed generic chain, all delays** (exceptional set $`\mathcal X`$, (7.22)):
         - $`n=2`$: **yes**. For almost every $`C`$, $`e_1\prec e_2\Leftrightarrow\lambda_1<\lambda_2`$ for all events (7.25).
         - $`n\ge3`$, different cells: **partly decided**. A generic chain can fail only at blind delays (7.23), (7.24). Whether a generic chain has blind delays is **not decided** (U1).
         - $`n\ge3`$, same cell: **not decided** (U2).
       - It does not hold for every chain: (7.21), and chains with a cut link.

       For $`n\ge3`$ this sub-item is therefore incomplete.
     - $`\prec`$ is not transitive in general (7.21). It is transitive whenever $`C\notin\mathcal X`$, which is the generic case for $`n=2`$ (7.25).

## Consistency checks

1. **Cut link** ($`J_m=0`$ for some $`j\le m<i`$). Then $`C=C_L+C_R`$ with commuting parts on cells $`\le m`$ and $`\ge m+1`$. So $`Q_t`$ stays in cells $`\le m<i`$, and $`\delta P\equiv0`$ exactly. This agrees with $`K_t=0`$ in (7.4), with $`\beta_m\equiv0`$ in the recursion behind (7.11), which forces every later term to vanish, and with $`\mathcal I_{ij}=\emptyset`$ in (7.14). Every delay is then blind, $`\Lambda^{ij}_C=(0,\infty)`$, as (7.24) requires of exceptional delays between different cells. Passed.
2. **$`n=2`$, exact solution (7.8).** The expansion of $`\lvert\sin2g\delta\rvert`$ begins with $`2g\delta`$, which agrees with (7.7) for $`r=1`$. The first member of (7.12) with $`m=2`$ gives $`e^{2g\delta}-1\ge2g\delta\ge\lvert\sin2g\delta\rvert`$. The zeros $`\delta=k\pi/(2g)`$ are isolated, as (7.13)–(7.14) require. This chain has the double eigenvalues $`\pm g`$, so it violates (G), and at $`\delta=\pi/(2g)`$ its evolution is a product unitary with only two eigenvalues: the delay is blind, and the chain lies in the null set $`\mathcal X`$ that (7.25) allows. Passed.
3. **$`\delta\to0`$ and dimensions.** (7.5) and (7.12) give $`\delta P\to0`$ as $`\delta\to0`$, continuous with (7.2), and $`\sum_t\Gamma_t=0`$ preserves normalization. In (1.9), $`C\lambda`$ is dimensionless, so $`\lVert J\rVert\delta`$ in (7.11)–(7.16) is dimensionless and $`v_{\rm LR}`$ has the dimension of $`\lVert J\rVert`$, i.e. cells per unit $`\lambda`$. Passed.

## Open issues

- **U1** ($`n\ge3`$, different cells): it is not decided whether a generic chain has no blind delay, i.e. whether $`\mathcal X^{\rm bl}_{ij}`$ of (7.23) is null. If it is, (7.24) gives $`\mathrm{vol}(\mathcal X_{ij})=0`$ for $`i\neq j`$.
- **U2** ($`n\ge3`$, same cell): it is not decided whether $`\mathcal X_{ii}`$ is null. If U1 and U2 both hold, (7.25) extends to every $`n`$, and $`\prec`$ is then generically the order of $`\lambda`$ and transitive.
- $`v_{\rm LR}=2e\lVert J\rVert`$ is the speed of the bound's $`\epsilon`$-boundary. The actual front speed of a given chain, for example (7.6), may be lower and is not determined; attainment of the bound is shown only at leading order, for $`m=2`$.
- Out of scope: events defined by records, sequences of more than two readings, other contract graphs, the relation to the maximal speed of 03-ilang-space, and whether the order of $`\lambda`$ is detectable (criterion 8).

## Methods used

- Heisenberg picture; outcome-averaged reading as the dephasing map $`\mathcal M_i`$
- Nested-commutator (Taylor) expansion; support counting on a chain
- Duhamel formula; truncated evolutions; Grönwall-type iteration (Lieb–Robinson bound)
- Twirling over phase unitaries
- Real-analyticity and the identity theorem; measure-zero zero sets of analytic functions
- Invariance of Lebesgue measure under conjugation, Tonelli's theorem, Haar measure
- Structure theorem of finite-dimensional $`*`$-algebras, commutants; dimension counts on conjugacy classes and Grassmannians; stratification of analytic sets and Sard's theorem
- Stirling bounds; Pauli algebra
