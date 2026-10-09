# Readings on the companion and the witness geometry of a part

- **Subproject:** 03-ilang-space
- **Package:** 09-measurability
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-08

## Setup and assumptions

- A description satisfying A1–A7 at fixed $\lambda$, an admissible unit vector $\lvert\Psi\rangle\in\mathcal H_{\rm adm}$, a part $A$ with nonempty companion $\bar A$, and $\mathcal H=\mathcal H_A\otimes\mathcal H_{\bar A}$ (A7). $H_A$ is the set of joint places $h$ of $A$.
- **Notation.** As fixed by the question, $r,s$ label the outcomes of readings. To avoid a clash, the joint places of $\bar A$ are written $k,k'$ here, not $r,r'$ as in the base problem and (2.1). So (2.1) reads $\lvert\psi_h\rangle=\sum_k\Psi_{hk}\lvert k\rangle$.
- **Reading on the companion.** The classes $S^{\bar A}_r$ partition the joint places of $\bar A$. $\Pi^{\bar A}_r$ is the projector onto their span, and $\Pi_r=\mathbb 1_A\otimes\Pi^{\bar A}_r$ (derived in Step 2). The reading is label-free: every swap of same-type objects of $\bar A$ maps each $S^{\bar A}_r$ onto itself.
- Only outcomes with $p(r)>0$ occur, and $\Psi_r$ is defined only for these outcomes. The quantities of the post-reading state are written $p^{(r)}_h$, $H_V(\Psi_r)$, $X_V(\Psi_r)$, $W_r$, $\alpha_r$, $\ell_r$.
- No evolution acts between readings (fixed $\lambda$). Each run yields one outcome, and the state becomes $\Psi_r$ (1.3), Law 1. "Averaged over outcomes" refers to the statistics of the outcomes over runs from the same $\Psi$. No mixed state is introduced (A3).
- Inputs: (1.3), (1.5), (1.11), A4, A7; (2.1), (2.2), (2.5), (2.11); (3.1), (3.5); (4.2), (4.3), (4.6), as quoted in question.md.

## Derivation

### Step 1. Grouping of the companion (item 1)

A joint place $K$ assigns a place of $T(a)$ to every object $a$. (1.4) writes this assignment as a tuple in the order $1,\dots,N$. Restriction $K\mapsto(h,k)=(K|_A,K|_{\bar A})$ is a bijection. The unitary $\lvert K\rangle\mapsto\lvert h\rangle\otimes\lvert k\rangle$, which maps the place basis onto the place basis, is what $\mathcal H=\mathcal H_A\otimes\mathcal H_{\bar A}$ means. With $\Psi_{hk}:=\Psi_K$, (2.1) and (2.2) give

$$
(V_A)_{hh'}=\langle\psi_{h'}\vert\psi_h\rangle=\sum_k\Psi_{hk}\,\Psi_{h'k}^{*}.
\tag{9.1}
$$

This is a finite sum over the set of all assignments $k$ of places to the objects of $\bar A$. Neither this set nor the summand refers to an order or a grouping of $\bar A$:
- A grouping $\bar A=B_1\cup\dots\cup B_m$ into disjoint subsets writes $k=(k_{B_1},\dots,k_{B_m})$ and $\mathcal H_{\bar A}=\bigotimes_j\mathcal H_{B_j}$. The iterated partial trace $\operatorname{Tr}_{B_1}\circ\cdots\circ\operatorname{Tr}_{B_m}$, taken in any order, is (9.1) written as an iterated finite sum.
- Reordering the factors of $\bar A$ relabels $k$ by a bijection of the summation set.

A common phase (1.2) cancels in (9.1). Hence $V_A$ depends only on the state $\Psi$ and on the set $A$. The other structures are functions of $V_A$ alone:
- $p_h$, $H_V$ and $W$, by (2.2) and (2.11);
- $\approx$, $X_V$ and $\alpha$, by (3.1) and (3.5);
- $\sim$, from $\alpha$ alone (4.3);
- $\ell$, from $\alpha$ and $\sim$ (4.6).

So none of them depends on how the companion is grouped or ordered.

### Step 2. The lifted reading

By A4, with $A$ and $\bar A$ exchanged, the class of $K=(h,k)$ is fixed by $k$, so $S_r=H_A\times S^{\bar A}_r$. Its projector is

$$
\Pi_r=\sum_{h\in H_A}\sum_{k\in S^{\bar A}_r}\lvert h\rangle\langle h\rvert\otimes\lvert k\rangle\langle k\rvert=\mathbb 1_A\otimes\Pi^{\bar A}_r,
\qquad
\Pi^{\bar A}_r\Pi^{\bar A}_s=\delta_{rs}\Pi^{\bar A}_r,
\qquad
\sum_r\Pi^{\bar A}_r=\mathbb 1_{\bar A}.
\tag{9.2}
$$

The last two relations hold because the classes are disjoint and cover all joint places of $\bar A$, and because the place basis is orthonormal and complete (A2).

### Step 3. Outcome probability, post-reading state, branch vectors, view (item 2)

**(a) Probability.** Applying (9.2) to (2.1) gives $\Pi_r\lvert\Psi\rangle=\sum_h\lvert h\rangle\otimes\Pi^{\bar A}_r\lvert\psi_h\rangle$. The $\lvert h\rangle$ are orthonormal and $(\Pi^{\bar A}_r)^\dagger\Pi^{\bar A}_r=\Pi^{\bar A}_r$, so

$$
p(r)=\bigl\lVert\Pi_r\lvert\Psi\rangle\bigr\rVert^2=\sum_h\langle\psi_h\vert\Pi^{\bar A}_r\vert\psi_h\rangle=\sum_h\bigl\lVert\Pi^{\bar A}_r\lvert\psi_h\rangle\bigr\rVert^2 .
\tag{9.3}
$$

By (9.2) and (2.1), $\sum_rp(r)=\sum_h\lVert\psi_h\rVert^2=1$.

**(b) State.** By (1.3), for $p(r)>0$,

$$
\lvert\Psi_r\rangle=\frac{\Pi_r\lvert\Psi\rangle}{\sqrt{p(r)}}=\sum_h\lvert h\rangle\otimes\frac{\Pi^{\bar A}_r\lvert\psi_h\rangle}{\sqrt{p(r)}} .
\tag{9.4}
$$

**(c) Branch vectors.** Apply the definition (2.1) to $\Psi_r$, using $(\langle h\rvert\otimes\mathbb 1_{\bar A})(\lvert h'\rangle\otimes\lvert\phi\rangle)=\delta_{hh'}\lvert\phi\rangle$:

$$
\lvert\psi^{(r)}_h\rangle=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi_r\rangle=\frac{\Pi^{\bar A}_r\lvert\psi_h\rangle}{\sqrt{p(r)}} .
\tag{9.5}
$$

**(d) View.** By (2.2) for $\Psi_r$ and (9.5), again with $(\Pi^{\bar A}_r)^\dagger\Pi^{\bar A}_r=\Pi^{\bar A}_r$:

$$
\bigl(V_A(\Psi_r)\bigr)_{hh'}=\langle\psi^{(r)}_{h'}\vert\psi^{(r)}_h\rangle=\frac{\langle\psi_{h'}\vert\Pi^{\bar A}_r\vert\psi_h\rangle}{p(r)},
\qquad\text{i.e.}\qquad
V_A(\Psi_r)=\frac{\operatorname{Tr}_{\bar A}\bigl(\Pi_r\lvert\Psi\rangle\langle\Psi\rvert\bigr)}{p(r)} .
\tag{9.6}
$$

**(e) Admissibility.** Let $a\neq b$ with $T(a)=T(b)=T$. If $P_{ab}\Pi_r=\Pi_rP_{ab}$, then (1.11) for $\Psi$ gives $P_{ab}\lvert\Psi_r\rangle=\Pi_rP_{ab}\lvert\Psi\rangle/\sqrt{p(r)}=c_T\lvert\Psi_r\rangle$. Since $P_{ab}$ permutes the joint places, $P_{ab}\Pi_rP_{ab}^{-1}$ is the projector onto the span of $P_{ab}(S_r)$. Commutation therefore holds iff $P_{ab}(S_r)=S_r$. There are three cases:
- $a,b\in A$: $P_{ab}=P^A_{ab}\otimes\mathbb 1_{\bar A}$ commutes with $\mathbb 1_A\otimes\Pi^{\bar A}_r$.
- $a,b\in\bar A$: $P_{ab}=\mathbb 1_A\otimes P^{\bar A}_{ab}$. Label-freeness gives $P^{\bar A}_{ab}(S^{\bar A}_r)=S^{\bar A}_r$, so the two commute.
- $a\in A$, $b\in\bar A$: $P_{ab}$ replaces the place of $b$ in $k$ by $h_a$, which ranges over all of $H_T$. So $P_{ab}(S_r)=S_r$ for all $r$ iff the class of $k$ does not depend on the place of $b$.

Hence, for a label-free reading on $\bar A$,

$$
\Pi_r\ \text{commutes with every swap}
\iff
\text{(C): the class of } k \text{ does not depend on the places of the objects of } \bar A \text{ whose type occurs in } A .
\tag{9.7}
$$

Under (C), $\lvert\Psi_r\rangle\in\mathcal H_{\rm adm}$ for every outcome. (C) holds automatically when no type has objects on both sides of the cut.

**Without (C), admissibility can fail.** Take $N=2$ and one type $T$ with $H_T=\{0,1\}$. Let $A=\{1\}$, $\bar A=\{2\}$, and $\lvert\Psi\rangle=(\lvert01\rangle+c_T\lvert10\rangle)/\sqrt2$, which satisfies (1.11). Read the place of object 2. This reading is label-free, vacuously, since $\bar A$ has a single object. The outcome "place 0" gives $\lvert\Psi_r\rangle=c_T\lvert10\rangle$, and $P_{12}\lvert\Psi_r\rangle=c_T\lvert01\rangle\perp\lvert\Psi_r\rangle$, so $\Psi_r$ is not admissible. In this example the cut separates two same-type instances, so $A$ is itself specified by a description label (M6, A7).

### Step 4. No signalling on average (item 3)

For an outcome with $p(r)=0$, (9.3) gives $\Pi^{\bar A}_r\lvert\psi_h\rangle=0$ for all $h$, so the sum may run over all classes. Then (9.6) and (9.2) give

$$
\sum_rp(r)\,V_A(\Psi_r)=\sum_{h,h'}\Bigl\langle\psi_{h'}\Big\vert\sum_r\Pi^{\bar A}_r\Big\vert\psi_h\Bigr\rangle\lvert h\rangle\langle h'\rvert=V_A(\Psi).
\tag{9.8}
$$

Take a local reading on $A$ with classes $S^A_s$ and projectors $\Pi^A_s$. If the distant reading is made and yields $r$, the state is $\Psi_r$. By (2.5) for $\Psi_r$, the local reading then yields $s$ with probability $p(s\vert r)=\operatorname{Tr}\bigl(\Pi^A_sV_A(\Psi_r)\bigr)$. The outcome $r$ itself occurs with probability $p(r)$. By linearity of the trace and (9.8), the frequency of $s$ over runs is

$$
\sum_rp(r)\,p(s\vert r)=\operatorname{Tr}\Bigl(\Pi^A_s\sum_rp(r)V_A(\Psi_r)\Bigr)=\operatorname{Tr}\bigl(\Pi^A_sV_A(\Psi)\bigr)=p(s).
\tag{9.9}
$$

The right side is (2.5) without the distant reading. So the statistics of $s$ depend neither on whether the distant reading was made nor on which reading was chosen. Neither label-freeness nor (C) enters (9.8) and (9.9); they matter only for the admissibility of $\Psi_r$.

### Step 5. The witness geometry after one outcome (item 4)

By (2.2) and (9.6), $p^{(r)}_h=\langle\psi_h\vert\Pi^{\bar A}_r\vert\psi_h\rangle/p(r)$, so

$$
H_V(\Psi_r)=\bigl\{h:\ \Pi^{\bar A}_r\lvert\psi_h\rangle\neq0\bigr\}\subseteq H_V .
\tag{9.10}
$$

For $h,h'\in H_V(\Psi_r)$, apply (2.11) to $\Psi_r$ with (9.6). The factor $p(r)$ cancels:

$$
W_r(h,h')=\frac{\bigl\lvert\langle\psi_{h'}\vert\Pi^{\bar A}_r\vert\psi_h\rangle\bigr\rvert^2}{\langle\psi_h\vert\Pi^{\bar A}_r\vert\psi_h\rangle\,\langle\psi_{h'}\vert\Pi^{\bar A}_r\vert\psi_{h'}\rangle}
=\bigl\lvert\langle e^{(r)}_{h'}\vert e^{(r)}_h\rangle\bigr\rvert^2,
\qquad
\lvert e^{(r)}_h\rangle:=\frac{\Pi^{\bar A}_r\lvert\psi_h\rangle}{\lVert\Pi^{\bar A}_r\psi_h\rVert},
\tag{9.11}
$$

and $\cos\alpha_r=\sqrt{W_r}$ by (3.5). The $\lvert\psi_h\rangle$ may be replaced by the $\lvert E_h\rangle$, since the factor $p_hp_{h'}$ and the phase convention cancel. By Cauchy–Schwarz, $0\le W_r\le1$, with $W_r(h,h')=1$ iff $\Pi^{\bar A}_r\lvert\psi_{h'}\rangle\parallel\Pi^{\bar A}_r\lvert\psi_h\rangle$.

**Points are never split.** Suppose $h\approx h'$ in $\Psi$. Then (3.1) gives $\lvert\psi_{h'}\rangle\langle\psi_{h'}\rvert/p_{h'}=\lvert\psi_h\rangle\langle\psi_h\rvert/p_h$, so $\lvert\psi_{h'}\rangle=c\lvert\psi_h\rangle$ with $c\neq0$, and hence $\Pi^{\bar A}_r\lvert\psi_{h'}\rangle=c\,\Pi^{\bar A}_r\lvert\psi_h\rangle$. So either both places are absent from $\Psi_r$, or both are present with $W_r(h,h')=1$. Hence the map

$$
x\ \longmapsto\ \text{the point of } X_V(\Psi_r) \text{ that contains } x,
\qquad
\bigl\{x\in X_V:\ \Pi^{\bar A}_r\lvert\psi_h\rangle\neq0 \text{ for } h\in x\bigr\}\ \to\ X_V(\Psi_r),
\tag{9.12}
$$

is well defined. It is surjective by (9.10). For a given outcome, a reading on the companion can remove points and merge points, but it never splits a point. $W_r$ can be larger or smaller than $W$; Step 6 shows both.

### Step 6. Example (item 4)

Take two objects of different types: object 1 with places $\{0,1\}$ and object 2 with places $\{k_1,k_2,k_3\}$. Let $A=\{1\}$ and $\bar A=\{2\}$. Since there is no same-type pair, (1.11) is void and $\mathcal H_{\rm adm}=\mathcal H$. Every reading is label-free and (C) holds. The contract system is arbitrary; it plays no role at fixed $\lambda$. Choose

$$
\lvert\Psi\rangle=\tfrac12\bigl(\lvert0\rangle\otimes(\lvert k_1\rangle+\lvert k_2\rangle)+\lvert1\rangle\otimes(\lvert k_1\rangle+\lvert k_3\rangle)\bigr),
\qquad
V_A(\Psi)=\frac14\begin{pmatrix}2&1\\1&2\end{pmatrix},
\qquad
W(0,1)=\tfrac14,\quad \alpha=\tfrac{\pi}{3}.
\tag{9.13}
$$

Here $\lvert\psi_0\rangle=(\lvert k_1\rangle+\lvert k_2\rangle)/2$ and $\lvert\psi_1\rangle=(\lvert k_1\rangle+\lvert k_3\rangle)/2$, so $p_0=p_1=\tfrac12$ and $\langle\psi_1\vert\psi_0\rangle=\tfrac14$, which gives (2.2) and (2.11). The two points $x_0=\{0\}$ and $x_1=\{1\}$ are distinct. Since $\alpha$ is a metric (3.5), every chain sum in (4.6) is at least $\alpha$, so $\ell(x_0,x_1)\ge\pi/3$.

The reading has the classes $S^{\bar A}_1=\{k_1\}$ and $S^{\bar A}_2=\{k_2,k_3\}$.

**Outcome 1.** $\Pi^{\bar A}_1\lvert\psi_0\rangle=\Pi^{\bar A}_1\lvert\psi_1\rangle=\lvert k_1\rangle/2$. By (9.3)–(9.6) and (9.11):

$$
p(1)=\tfrac12,\qquad
\lvert\Psi_1\rangle=\tfrac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)\otimes\lvert k_1\rangle,\qquad
V_A(\Psi_1)=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
W_1(0,1)=1 .
\tag{9.14}
$$

So $0\approx1$. The two points merge into one, $\alpha_1=0$ and $\ell_1=0$ (chain of length zero), compared with $\ell\ge\pi/3$ before.

**Outcome 2.** $\Pi^{\bar A}_2\lvert\psi_0\rangle=\lvert k_2\rangle/2$ and $\Pi^{\bar A}_2\lvert\psi_1\rangle=\lvert k_3\rangle/2$, so

$$
p(2)=\tfrac12,\qquad
\lvert\Psi_2\rangle=\tfrac{1}{\sqrt2}\bigl(\lvert0\rangle\lvert k_2\rangle+\lvert1\rangle\lvert k_3\rangle\bigr),\qquad
V_A(\Psi_2)=\frac12\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
W_2(0,1)=0 .
\tag{9.15}
$$

So $\alpha_2=\pi/2$. By (4.2) the two points are no longer related, and $\ell_2\ge\pi/2$.

**Average.** By (9.14) and (9.15),

$$
p(1)V_A(\Psi_1)+p(2)V_A(\Psi_2)=\frac14\begin{pmatrix}1&1\\1&1\end{pmatrix}+\frac14\begin{pmatrix}1&0\\0&1\end{pmatrix}=\frac14\begin{pmatrix}2&1\\1&2\end{pmatrix}=V_A(\Psi),
\tag{9.16}
$$

as (9.8) requires. In this example even each single outcome leaves $p^{(r)}_h=\tfrac12$ unchanged. By (2.5), no local reading on $A$ registers the change of $W$, $\alpha$ or $\ell$.

### Step 7. The factorized case (item 5)

Let $\bar A=\bar A_1\cup\bar A_2$ be disjoint, with $\lvert\Psi\rangle=\lvert\Psi_{A\bar A_1}\rangle\otimes\lvert\Omega_{\bar A_2}\rangle$; this grouping is allowed by Step 1. Both factors may be taken as unit vectors. Then $\lvert\psi_h\rangle=\lvert\phi_h\rangle\otimes\lvert\Omega\rangle$, where $\lvert\phi_h\rangle:=(\langle h\rvert\otimes\mathbb 1_{\bar A_1})\lvert\Psi_{A\bar A_1}\rangle$ and $\sum_h\lVert\phi_h\rVert^2=1$. A reading on $\bar A_2$ alone has classes that depend only on $k_{\bar A_2}$. As in (9.2), $\Pi^{\bar A}_r=\mathbb 1_{\bar A_1}\otimes\Pi^{\bar A_2}_r$, hence $\langle\psi_{h'}\vert\Pi^{\bar A}_r\vert\psi_h\rangle=\langle\phi_{h'}\vert\phi_h\rangle\,\omega_r$ with $\omega_r:=\langle\Omega\vert\Pi^{\bar A_2}_r\vert\Omega\rangle$. Then (9.3) and (9.6) give

$$
p(r)=\omega_r,\qquad
\bigl(V_A(\Psi_r)\bigr)_{hh'}=\langle\phi_{h'}\vert\phi_h\rangle=\langle\psi_{h'}\vert\psi_h\rangle=\bigl(V_A(\Psi)\bigr)_{hh'}
\quad\text{for every outcome with } p(r)>0 .
\tag{9.17}
$$

By Step 1, $X_V$, $\alpha$, $\sim$ and $\ell$ are unchanged as well. The argument holds for every partition of the joint places of $\bar A_2$; label-freeness is not used.

## Result

- **Cut and grouping (9.1).** $V_A$, and with it $X_V$, $\alpha$, $\sim$ and $\ell$, depend only on $\Psi$ and the set $A$. A distant choice of how the companion is grouped or ordered cannot change a local distance.
- **State update.** $p(r)=\sum_h\langle\psi_h\vert\Pi^{\bar A}_r\vert\psi_h\rangle$ (9.3); $\lvert\Psi_r\rangle=\Pi_r\lvert\Psi\rangle/\sqrt{p(r)}$ (9.4); $\lvert\psi^{(r)}_h\rangle=\Pi^{\bar A}_r\lvert\psi_h\rangle/\sqrt{p(r)}$ (9.5); $(V_A(\Psi_r))_{hh'}=\langle\psi_{h'}\vert\Pi^{\bar A}_r\vert\psi_h\rangle/p(r)$ (9.6). $\Psi_r$ is admissible under condition (C) of (9.7), which is exactly the condition that $\Pi_r$ commutes with every swap. Without (C) it can fail (Step 3e).
- **No signalling on average.** $\sum_rp(r)V_A(\Psi_r)=V_A(\Psi)$ (9.8). Hence the outcome-averaged statistics of every local reading on $A$ equal those without the distant reading, whichever reading is chosen (9.9).
- **One outcome.** $W_r$ is given by (9.11). Points can be removed or merged but are never split (9.12). For a single outcome a distant reading can change $X_V$, $W$, $\alpha$ and $\ell$: in (9.13)–(9.16) one outcome merges two points ($\alpha:\pi/3\to0$), the other separates them ($\alpha:\pi/3\to\pi/2$), and the average view is unchanged.
- **Factorized companion.** A reading on a factor $\bar A_2$ with $\Psi=\Psi_{A\bar A_1}\otimes\Omega_{\bar A_2}$ leaves $V_A$, and hence the whole witness geometry, unchanged for every outcome (9.17).

## Consistency checks

1. **Trivial reading.** A single class gives $\Pi^{\bar A}_1=\mathbb 1_{\bar A}$. Then (9.3) gives $p(1)=1$, (9.4) gives $\Psi_1=\Psi$, (9.6) gives $V_A(\Psi_1)=V_A(\Psi)$, and (9.11) reduces to (2.11).
2. **Perfect record.** Suppose that for each $r$ at most one place $h_r$ has $\Pi^{\bar A}_r\lvert\psi_{h_r}\rangle\neq0$. By (9.2) this implies $\langle\psi_{h'}\vert\psi_h\rangle=0$ for $h\neq h'$. By (9.10), $H_V(\Psi_r)=\{h_r\}$, a single point, and (9.6) gives $V_A(\Psi_r)=\lvert h_r\rangle\langle h_r\rvert$. Then $\sum_rp(r)V_A(\Psi_r)=\sum_h\bigl(\sum_r\lVert\Pi^{\bar A}_r\psi_h\rVert^2\bigr)\lvert h\rangle\langle h\rvert=\sum_hp_h\lvert h\rangle\langle h\rvert=V_A(\Psi)$, in agreement with (9.8).
3. **Example average.** (9.16) is computed directly from the post-reading views (9.14) and (9.15), and it reproduces $V_A(\Psi)$ of (9.13), as (9.8) requires.

## Open issues

- **Discrepancy with the expected result (item 2).** $\Pi_r$ does not commute with every swap for every label-free reading on $\bar A$. Commutation, and with it admissibility, holds exactly under (C) (9.7), in particular when no type has objects on both sides of the cut. The counterexample in Step 3e uses a cut that separates same-type instances. Whether such parts are legitimate is the open question of A7/M6.
- **Values of $\ell$ in the example.** (4.3) is quoted only as "defined from $\alpha$ alone". The example therefore uses only $\ell\ge\alpha$ (triangle inequality) and $\ell(x,x)=0$. The exact values of $\ell$ in the two-point spaces (9.13) and (9.15), either $\alpha$ or $+\infty$, depend on (4.3).
- **Notation.** Here $r$ labels outcomes and $k$ labels the joint places of $\bar A$. Later packages that combine (2.1) with readings should keep this convention.

## Methods used

- Partial trace as a finite sum over companion joint places; iterated partial traces
- Orthogonal projectors of a partition, completeness relation
- Projective state update (1.3), sequential readings, law of total probability
- Commutation of permutation operators with diagonal projectors
- Cauchy–Schwarz inequality; triangle inequality for the metric $\alpha$
- Explicit finite-dimensional example
