# Causal order of single-cell readings on a contract chain

- **Subproject:** 04-ilang-time
- **Package:** 07-causal-order
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-10

## Setup and assumptions

- **Model** (setting of the question). Cells $`1,\dots,n`$ ($`n\ge2`$), each the only instance of its type, with place sets $`H_i`$, $`d_i\ge2`$, and $`C=\sum_{i=1}^nD_i+\sum_{i=1}^{n-1}J_i`$, where $`D_i`$ acts on cell $`i`$, $`J_i`$ on cells $`i,i+1`$, and $`\lVert J\rVert:=\max_i\lVert J_i\rVert`$. No two objects share a type, so (1.11) imposes nothing: $`\mathcal H_{\rm adm}=\mathcal H`$. Cells are distinguished by their types, not by labels (M6).
- **Readings.** $`R_i`$ on cell $`i`$ at $`\lambda_1`$ has outcomes $`s`$ and projectors $`\Pi_s:=\Pi^{(i)}_s`$ ($`m`$ classes). $`R_j`$ on cell $`j`$ at $`\lambda_2`$ has outcomes $`t`$ and projectors $`\Pi'_t:=\Pi^{(j)}_t`$. Here $`t`$ is the question's $`r'`$, renamed so that it does not clash with the distance $`r:=\lvert i-j\rvert`$. Readings are partitions of places (A4), so all reading projectors are diagonal in the joint place basis. The delay is $`\delta:=\lambda_2-\lambda_1`$.
- **Start** (A8, A9). The start is the state $`\Psi_0`$ at some $`\lambda_0\le\min(\lambda_1,\lambda_2)`$. Readings act in increasing order of $`\lambda`$, and (1.9) acts between them. For $`\lambda_1\le\lambda_2`$ let $`\Psi_1:=e^{-\mathrm iC(\lambda_1-\lambda_0)}\Psi_0`$. This map is a bijection of unit vectors, so "for every start" means "for every unit vector $`\Psi_1`$". Outcomes of probability $`0`$ contribute nothing to outcome averages.
- **Notation.** $`\mathrm i`$ is the imaginary unit; the letter $`i`$ always denotes a cell. $`\mathrm{ad}_XY:=[X,Y]`$, $`X(\delta):=e^{\mathrm iC\delta}Xe^{-\mathrm iC\delta}`$ and $`\mathcal M_i(X):=\sum_s\Pi_sX\Pi_s`$. The support of an operator is the set of cells on which it acts nontrivially. Operators with disjoint supports commute, and $`\mathrm{supp}[X,Y]\subseteq\mathrm{supp}X\cup\mathrm{supp}Y`$.
- **M6.** Every quantity below depends on $`\Psi_1`$ only through $`\lvert\Psi_1\rangle\langle\Psi_1\rvert`$. It depends on the contracts only through $`C`$, except where the split into $`D`$'s and $`J`$'s is used; there, independence of the split is shown.
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

Label the classes of $`R_i`$ by $`s=0,\dots,m-1`$, let $`\omega:=e^{2\pi\mathrm i/m}`$, and define $`W_k:=\sum_s\omega^{ks}\Pi_s`$. These are unitaries on cell $`i`$, with $`W_0=\mathbb 1`$. Since $`\frac1m\sum_k\omega^{k(s-s')}`$ is $`1`$ for $`s=s'`$ and $`0`$ otherwise, $`\mathcal M_i(X)=\frac1m\sum_kW_kXW_k^\dagger`$. Hence $`\mathcal M_i(X)-X=\frac1m\sum_{k=1}^{m-1}[W_k,X]W_k^\dagger`$, and

```math
\delta P\le\Bigl(1-\frac1m\Bigr)\max_{1\le k<m}\bigl\lVert[Z(\delta),W_k]\bigr\rVert .
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

- **Validity.** (7.12) holds for every start, every pair of readings and every $`\delta\ge0`$; trivially, also $`\delta P\le2`$.
- **Dependence on the $`D_i`$.** The bound does not depend on the $`D_i`$.
- **Booking (M6).** (7.12) holds for every split of $`C`$ into single-cell and pair terms, so it holds with the smallest $`\lVert J\rVert`$ over all splits. That value does not depend on the booking.
- **Leading order.** The bound is attained at leading order. For $`m=2`$, its first term is $`(2\lVert J\rVert\delta)^r/r!`$, which equals (7.7).

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

Here $`\delta_\epsilon(r)`$ is the unique root of $`2\sum_{k\ge r}(2\lVert J\rVert\delta)^k/k!=\epsilon`$. The left side increases strictly in $`\delta`$, from $`0`$ to $`\infty`$, and decreases in $`r`$; hence $`\delta_\epsilon(r)`$ increases with $`r`$.

**Explicit inner cone.** Let $`v>2e\lVert J\rVert`$ and $`u:=2\lVert J\rVert/v<1/e`$. For $`\delta\le r/v`$, $`x:=2\lVert J\rVert\delta\le ur`$, so the terms $`x^k/k!`$ with $`k\ge r`$ decrease with ratio $`\le u`$. Using $`r!\ge(r/e)^r`$, $`\sum_{k\ge r}x^k/k!\le x^r/(r!(1-u))\le(eu)^r/(1-u)`$. Hence

```math
\delta P\le\frac{2}{1-2\lVert J\rVert/v}\Bigl(\frac{2e\lVert J\rVert}{v}\Bigr)^{r}\qquad\text{for all starts, readings and } 0\le\delta\le r/v ,
\qquad\text{(7.16)}
```

which is exponentially small in $`r`$.

**Outside.** Conversely, let $`v<2e\lVert J\rVert`$ and $`\delta=r/v`$. Using $`r!\le e\sqrt r\,(r/e)^r`$, the bound is at least $`2(2\lVert J\rVert\delta)^r/r!\ge\frac{2}{e\sqrt r}\bigl(\frac{2e\lVert J\rVert}{v}\bigr)^r\to\infty`$. So $`(r,r/v)\notin\mathcal S_\epsilon`$ for large $`r`$.

**Speed.** Together, for every $`\epsilon>0`$ the boundary moves at

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

**(ii) Pairs with $`\lambda_1<\lambda_2`$.**

- **Criterion.** By (7.1) and Step 1, influence occurs for some start if and only if some $`\mathcal M_i(Q_t)-Q_t\neq0`$; for $`\Psi_1`$ one takes an eigenvector of this self-adjoint operator for a nonzero eigenvalue. Equivalently, some $`Q_t`$ fails to commute with some $`\Pi_s`$. Coarse projectors are sums of place projectors $`p_h`$, so it suffices to test place readings. Hence $`e_1\prec e_2`$ if and only if $`F_\delta(C):=\sum_{h,h'}\lVert[\,p^{(j)}_{h'}(\delta),\,p^{(i)}_h\,]\rVert_{2}^{2}>0`$, with $`\lVert\cdot\rVert_2`$ the Hilbert–Schmidt norm.
- **Analyticity in the contract terms.** $`F_\delta`$ is real-analytic in the real parameters of $`(D_1,\dots,D_n,J_1,\dots,J_{n-1})`$. By A5 the $`D`$'s are booked in pair terms, so these are the parameters of the pair terms. Also $`F_\delta(C)=F_1(\delta C)`$.
- **$`F_\delta\not\equiv0`$, case $`r\ge1`$.** Place the chain (7.6) on the cells between $`i`$ and $`j`$, mirrored if $`i>j`$. For $`d>2`$ it acts on places $`0,1`$; all other terms are $`0`$. Then $`F_{\delta'}>0`$ for small $`\delta'`$ by (7.7), and rescaling $`C`$ by $`\delta'/\delta`$ gives $`F_\delta>0`$.
- **$`F_\delta\not\equiv0`$, case $`r=0`$.** Take $`D_i=g\sigma^x_i`$ and all other terms zero. Then $`p^{(i)}_0(\delta)`$ fails to commute with $`p^{(i)}_0`$ unless $`\sin(2g\delta)=0`$.
- **Generic statement.** The zero set of a nonzero real-analytic function has measure zero. Hence:

```math
\text{for fixed } i,j \text{ and } \lambda_1<\lambda_2:\ \ e_1\prec e_2\ \text{for all contract terms outside a closed set of measure zero.}
\qquad\text{(7.20)}
```

- **Fixed $`C`$.** For a fixed $`C`$, the pairs with $`\lambda_1<\lambda_2`$ but $`e_1\nprec e_2`$ are those with $`\lambda_2-\lambda_1\in E_{ij}`$ of (7.14). There are none for $`0<\lambda_2-\lambda_1<\delta_0`$, and they form a discrete set otherwise. For generic $`C`$, outside a countable union of null sets, there are none at rational delays.
- **Exceptional delays exist.** They do not vanish for every $`C`$. For $`n=2`$, $`D=0`$ and $`J_1=g\sigma^x_1\sigma^x_2`$, the evolution $`e^{-\mathrm iC\pi/(2g)}=-\mathrm i\sigma^x_1\sigma^x_2`$ is a product of single-cell unitaries. Every $`p_h(\pi/(2g))`$ is then a place projector of its own cell, so no reading influences any other at delay $`\pi/(2g)`$.

**(iii) Transitivity.** In the same chain, by (7.8) at $`2g\delta=\pi/2`$ and by the $`1\leftrightarrow2`$ symmetry of $`C`$ (start $`\lvert{+\mathrm i}\rangle\lvert+\rangle`$ for the second relation), together with (ii):

```math
e_1=(1,0)\prec e_2=\bigl(2,\tfrac{\pi}{4g}\bigr)\prec e_3=\bigl(1,\tfrac{\pi}{2g}\bigr),\qquad e_1\nprec e_3\qquad(n=2,\ D=0,\ J_1=g\sigma^x_1\sigma^x_2).
\qquad\text{(7.21)}
```

So $`\prec`$ is not transitive in general. If all $`\mathcal I_{ij}\neq\emptyset`$ and all $`E_{ij}=\emptyset`$, then (7.14) and (7.19) give $`e_1\prec e_2\Leftrightarrow\lambda_1<\lambda_2`$, which is transitive. For generic $`C`$, a triple can violate transitivity only if $`\lambda_3-\lambda_1`$ lies in the discrete set $`E_{ik}`$.

## Result

1. **Item 1.** $`R_i`$ cannot influence $`R_j`$ when $`\lambda_2=\lambda_1`$, $`i\neq j`$ (no), nor when $`\lambda_2<\lambda_1`$ (no): (7.2). The equal-$`\lambda`$ statement holds even for $`i=j`$.
2. **Item 2.**
   - The influence is $`\Delta_t=\langle\Psi_1\vert\mathcal M_i(Q_t)-Q_t\vert\Psi_1\rangle`$ (7.1).
   - The lowest power is $`\delta^r`$. The exact coefficient $`\Gamma_t`$ of (7.4) is built from the nested commutator $`K_t`$ of the links between the cells (7.3), the projectors and the view of the cells between; $`\delta P`$ is given by (7.5). The $`D_i`$ do not enter.
   - Nonzero examples exist for every $`r\ge1`$, (7.6)–(7.7), including $`r=1`$ (exactly $`\delta P=\lvert\sin 2g\delta\rvert`$, (7.8)) and $`r=2`$ ($`\delta P=2g^2\delta^2+O(\delta^3)`$).
3. **Item 3.** The bound is (7.12), $`\delta P\le2\sum_{k\ge r}(2\lVert J\rVert\delta)^k/k!`$, obtained from the chain Lieb–Robinson bound (7.11). It is uniform in $`n`$, attained at leading order, and does not depend on the $`D_i`$.
4. **Item 4.**
   - No: $`\delta P`$ cannot vanish on $`(0,\varepsilon)`$ and be nonzero later (7.13).
   - Hence there is no sharp cone: influence at some delay implies influence at all delays except a discrete set, in particular at arbitrarily small ones (7.14). The order is sharp only at $`\delta=0`$.
   - Below $`\epsilon`$ for every start: the set $`\mathcal S_\epsilon`$ (7.15), with explicit inner cone (7.16). Its boundary moves at $`v_{\rm LR}=2e\lVert J\rVert`$ cells per unit $`\lambda`$ (7.17).
   - For $`\prec`$ (7.18):
     - $`\prec`$ implies $`\lambda_1<\lambda_2`$: yes (7.19).
     - $`\prec`$ holds for every pair with $`\lambda_1<\lambda_2`$ only with conditions. For generic contract terms it holds at every prescribed delay (7.20) and at all small delays. It is not true for every $`C`$ at every delay, since exceptional delays exist (Step 9 (ii)).
     - $`\prec`$ is not transitive in general (7.21); it is transitive when no exceptional delays exist.

## Consistency checks

1. **Cut link** ($`J_m=0`$ for some $`j\le m<i`$). Then $`C=C_L+C_R`$ with commuting parts on cells $`\le m`$ and $`\ge m+1`$. So $`Q_t`$ stays in cells $`\le m<i`$, and $`\delta P\equiv0`$ exactly. This agrees with $`K_t=0`$ in (7.4), with $`\beta_m\equiv0`$ in the recursion behind (7.11), which forces every later term to vanish, and with $`\mathcal I_{ij}=\emptyset`$ in (7.14). Passed.
2. **$`n=2`$, exact solution (7.8).** The expansion of $`\lvert\sin2g\delta\rvert`$ begins with $`2g\delta`$, which agrees with (7.7) for $`r=1`$. The bound (7.12) with $`m=2`$ gives $`e^{2g\delta}-1\ge2g\delta\ge\lvert\sin2g\delta\rvert`$. The zeros $`\delta=k\pi/(2g)`$ are isolated, as (7.13)–(7.14) require. Passed.
3. **$`\delta\to0`$ and dimensions.** (7.5) and (7.12) give $`\delta P\to0`$ as $`\delta\to0`$, continuous with (7.2), and $`\sum_t\Gamma_t=0`$ preserves normalization. In (1.9), $`C\lambda`$ is dimensionless, so $`\lVert J\rVert\delta`$ in (7.11)–(7.16) is dimensionless and $`v_{\rm LR}`$ has the dimension of $`\lVert J\rVert`$, i.e. cells per unit $`\lambda`$. Passed.

## Open issues

- It is not decided whether $`E_{ij}=\emptyset`$ for generic contract terms; a dimension count suggests yes. If so, $`\prec`$ would coincide with the order of $`\lambda`$ and would be transitive.
- $`v_{\rm LR}=2e\lVert J\rVert`$ is the speed of the bound's $`\epsilon`$-boundary. The actual front speed of a given chain, for example (7.6), may be lower and is not determined; the bound is shown to be tight only at leading order.
- Out of scope: events defined by records, sequences of more than two readings, other contract graphs, the relation to the maximal speed of 03-ilang-space, and whether the order of $`\lambda`$ is detectable (criterion 8).

## Methods used

- Heisenberg picture; outcome-averaged reading as the dephasing map $`\mathcal M_i`$
- Nested-commutator (Taylor) expansion; support counting on a chain
- Duhamel formula; truncated evolutions; Grönwall-type iteration (Lieb–Robinson bound)
- Twirling over phase unitaries
- Real-analyticity and the identity theorem; measure-zero zero sets of analytic functions
- Stirling bounds; Pauli algebra
