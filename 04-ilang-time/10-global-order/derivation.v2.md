# Detectability of λ through readings: unit, direction, common now, order

- **Subproject:** 04-ilang-time
- **Package:** 10-global-order
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-10

## Changes from previous version

- **Reason:** issue I1 of verification.md (round 1). The restriction that a contract is a sum of pair terms (A5) was not repeated in some characterizations; it matters when a part has more than one object.
- **Setup:** new bullet "Pair-term restriction (A5)"; the Setting bullet names the restriction.
- **Step 4:** the notion **pair-term split** is defined after (10.5). The sentence after (10.6) separates the commutation statement (no restriction) from the equivalence statement (pair-term split).
- **Step 6:** the theorem (10.14) names the class of $`C'`$; (10.15) requires $`D`$ to be a sum of pair terms; the exact criterion for the common now is "no pair-term split". "Not split" remains as a sufficient condition, exact when each part is one object.
- **Step 7, Result, Checks 1–2, Open issues:** the same qualification, and where it is automatic.
- **Wording only:** in Step 3 and in Open issues, "(split $`C`$)" became "(for example split $`C`$)", so that no equivalence is implied there.
- Nothing else changed: no proof, no example set, no bound. The tags (10.1)–(10.24) keep their meaning; there is no new tag.

## Response to verification

- **I1: Accepted and fixed** in Setup (bullet "Pair-term restriction"), Step 4 (pair-term split; sentence after (10.6)), Step 6 (theorem (10.14), (10.15), Consequences), Step 7 (last paragraph), Result (item 4), Consistency checks 1–2 and Open issues.
  - The exact criterion now reads: the common now is detectable iff $`C`$ has no split (10.5) whose components are sums of pair terms.
  - Every diagonal $`D`$ that parameterizes contracts is required to be a sum of pair terms.
  - With one object per part the restriction is empty, so the example sets (10.17)–(10.19) are unchanged.

## Setup and assumptions

- **Setting.** Exactly as in question.md: $`\mathcal H=\mathcal H_1\otimes\mathcal H_2`$, all objects of different types, $`C=C^\dagger`$ independent of $`\lambda`$ and a sum of pair terms (A5), start $`\Psi_0`$ at $`\lambda=0`$, only $`\lambda\ge0`$; schedules, re-timings $`(a_1,a_2,C')`$, equivalences and "detectable" as defined there.
- **Pair-term restriction (A5).** $`C`$ and every $`C'`$ of a re-timing are sums of pair terms. The operators of this form are a real linear space that contains $`\mathbb 1`$ and all single-object terms.
  - If each part is one object, every self-adjoint operator on $`\mathcal H`$ is one pair term: the restriction is empty.
  - If a part has more than one object, it is a real restriction: for example $`\sigma^z\otimes\sigma^z\otimes\sigma^z`$ on three two-place objects is real diagonal but not a sum of pair terms.
  - Every statement that describes the set of equivalences ((10.14), (10.15), the criterion of Step 6, Checks 1–2) is meant within this class and says so. The necessary conditions (10.9)–(10.13) and (10.16), and the commutation statement of (10.6), hold without it.
- **Notation.** $`h,h'`$ are the joint places of $`\mathcal P_1`$, $`r,r'`$ those of $`\mathcal P_2`$, and $`X_{hr,h'r'}:=\langle hr\vert X\vert h'r'\rangle`$. A **place projector of $`\mathcal P_1`$** is $`\Pi=\sum_{h\in S}\lvert h\rangle\langle h\rvert\otimes\mathbb 1`$ for a set $`S`$ of places; of $`\mathcal P_2`$, $`\Pi'=\mathbb 1\otimes\sum_{r\in S'}\lvert r\rangle\langle r\rvert`$. These are exactly the class projectors of local readings (A4); each occurs in some reading; all are diagonal in the joint place basis and commute with each other. $`X(\lambda):=e^{iC\lambda}Xe^{-iC\lambda}`$, and $`G_i:=C-a_iC'`$.
- **Standard facts.** (F0) A self-adjoint $`X`$ with $`\langle\Psi\vert X\vert\Psi\rangle=0`$ for all unit vectors is zero. (F1) For orthogonal projectors with $`\sum_s\Pi_s=\mathbb 1`$: $`X=\sum_s\Pi_sX\Pi_s`$ iff $`[X,\Pi_s]=0`$ for all $`s`$.
- **Well-definedness (M6).** "Uncoupled", the split (10.5), the components (10.13) and every condition below are properties of the operator $`C`$; none refers to the list of contract terms or to the booking of single-object terms. $`C_1,C_2`$ are fixed by $`C`$ up to $`(C_1+c\mathbb 1,\,C_2-c\mathbb 1)`$. Adding $`c\mathbb 1`$ to a contract changes no $`X(\lambda)`$, hence no statistics.
- **Exactness.** Items 1–4 and 5(a) use no approximation: every statement is exact and proven for the whole stated class. Item 5(b) is an inequality valid for every start.
- **Inputs** from 07-causal-order@v2, as quoted in question.md: (7.1), (7.2), (7.11), (7.12), (7.15). Abbreviation: $`\Sigma_r(\delta):=\sum_{k\ge r}(2\lVert J\rVert\delta)^k/k!`$.

## Derivation

### Step 1. Statistics of a schedule

Number the events so that $`\lambda_1\le\dots\le\lambda_K`$; $`\Pi^{(k)}_{s_k}`$ is the class projector of the outcome $`s_k`$ of $`R_k`$. Applying (1.9) and (1.3) alternately and multiplying the conditional probabilities (the normalizations cancel):

```math
P(s_1,\dots,s_K)=\bigl\lVert\Pi^{(K)}_{s_K}(\lambda_K)\cdots\Pi^{(1)}_{s_1}(\lambda_1)\,\Psi_0\bigr\rVert^2 .
\qquad\text{(10.1)}
```

- **Equal $`\lambda`$.** Factors with the same $`\lambda`$ are $`e^{iC\lambda}(\cdot)e^{-iC\lambda}`$ of commuting place projectors, so they commute: the product, hence the statistics, does not depend on their order.
- **Comparison rule.** Two schedules, possibly under different contracts, have equal statistics for every start if every event has the same operator $`\Pi^{(k)}_{s}(\lambda_k)`$ in both and the two orders of the factors differ only by exchanges of commuting factors.

### Step 2. Unit and origin (item 1)

**(a)** For $`a_1=a_2=a`$, $`C'=C/a`$: $`e^{-iC'(a\lambda)}=e^{-iC\lambda}`$, so every factor of (10.1) is unchanged, and the order is unchanged because $`a>0`$. $`C/a`$ is a sum of pair terms. Hence the statistics of every schedule are identical, and

```math
(a,\,a,\,C/a)\ \text{is an equivalence of } C\quad\text{for every } C\text{ and every } a>0 .
\qquad\text{(10.2)}
```

Taking $`a\neq1`$: **the unit of $`\lambda`$ is not detectable, for any $`C`$** (no nondegeneracy condition; $`C=0`$ included).

**(b)** Increasing all $`\lambda_k`$ by $`\mu\ge0`$ replaces each factor of (10.1) by $`e^{iC\mu}\Pi^{(k)}_{s_k}(\lambda_k)e^{-iC\mu}`$, so for every start

```math
P_{\lambda+\mu}(s_1,\dots,s_K;\Psi_0)=P_{\lambda}(s_1,\dots,s_K;\,e^{-iC\mu}\Psi_0).
\qquad\text{(10.3)}
```

If $`C\Psi_0=c\Psi_0`$, then $`e^{-iC\mu}\Psi_0=e^{-ic\mu}\Psi_0`$ is the same state (1.2): **the statistics of every schedule are unchanged by a common shift**, and for a single event $`p(s)=\lVert\Pi_s\Psi_0\rVert^2`$ **does not depend on its $`\lambda`$**.

### Step 3. Direction (item 2)

$`R`$ on one part at $`\lambda_1`$ with projectors $`\Pi_s`$, $`R'`$ on the other part at $`\lambda_2>\lambda_1`$ with projectors $`\Pi'_t`$; $`\Psi_1:=e^{-iC\lambda_1}\Psi_0`$, $`\delta:=\lambda_2-\lambda_1`$, $`Q_t:=\Pi'_t(\delta)`$. By (10.1), $`P(s,t)=\lVert Q_t\Pi_s\Psi_1\rVert^2`$. Since the $`Q_t`$ are orthogonal projectors with $`\sum_tQ_t=\mathbb 1`$,

```math
\sum_tP(s,t)=\lVert\Pi_s\Psi_1\rVert^2,
\qquad
\sum_sP(s,t)-\lVert Q_t\Psi_1\rVert^2=\Delta_t:=\langle\Psi_1\vert\sum_s\Pi_s\,[Q_t,\Pi_s]\,\vert\Psi_1\rangle ,
\qquad\text{(10.4)}
```

where $`\lVert\Pi_s\Psi_1\rVert^2`$ and $`\lVert Q_t\Psi_1\rVert^2`$ are the distributions of the single-event schedules.

- **Marginal of $`R`$ (smaller $`\lambda`$):** it never depends on whether $`R'`$ is made — for every $`C`$, every start, every pair of readings. Exact.
- **Marginal of $`R'`$ (larger $`\lambda`$):** it changes by $`\Delta_t`$ when $`R`$ is made. For a given start it depends on $`R`$ iff $`\Delta_t\neq0`$ for some $`t`$. It is independent of $`R`$ for every start iff $`[Q_t,\Pi_s]=0`$ for all $`s,t`$ (F0, F1; $`\Psi_1`$ runs over all unit vectors with $`\Psi_0`$). This holds for all readings and all $`\lambda_1<\lambda_2`$ when $`C`$ is split (10.5), in particular for uncoupled parts, by the first statement of (10.6). It fails in example (i) with the place readings, where $`\Delta_t=\mp\tfrac12\sin(2g\delta)\,\langle\Psi_1\vert\sigma^x\otimes\sigma^y\vert\Psi_1\rangle`$ (Check 3).
- **Implication.** The effect of a reading is one-sided: it can reach the statistics of a reading at larger $`\lambda`$, never at smaller $`\lambda`$. Whenever some pair of readings on the two parts has $`\Delta\neq0`$, the direction of increasing $`\lambda`$ is detectable: of two events, the one whose marginal changes when the other is omitted has the larger $`\lambda`$. If no pair of readings on the two parts has $`\Delta\neq0`$ (for example split $`C`$), two events on different parts do not show the direction.
- **What fixes the direction.** Not the evolution (1.9) (Laws 3, 4), which is reversible. The direction is fixed by the state update of (1.3) (Law 1: a reading is a write and is not reversible) as applied in A8 and in the schedule: the written state is the one that evolves on to larger $`\lambda`$, the start being prescribed at the smallest $`\lambda`$ and nothing at the largest. In (10.1) this is the fact that the sum over the outcomes of the last factor gives $`\mathbb 1`$, while the sum over an earlier factor does not.

### Step 4. Split contracts and uncoupled parts (item 3)

**Definition.** $`C`$ is **split** if there are self-adjoint $`F_1,F_2`$ with

```math
C=F_1+F_2,\qquad [F_1,F_2]=0,\qquad [F_1,\Pi']=0,\qquad [F_2,\Pi]=0
\qquad\text{(10.5)}
```

for every place projector $`\Pi`$ of $`\mathcal P_1`$ and $`\Pi'`$ of $`\mathcal P_2`$.

A split is a **pair-term split** if $`F_1`$ and $`F_2`$ are sums of pair terms (A5). Since $`F_1=C-F_2`$ and $`C`$ is a sum of pair terms, it suffices that $`F_2`$ is one. If each part is one object, every split is a pair-term split.

**Lemma.** Let $`C`$ be split, $`\lambda,\lambda'\ge0`$.
1. $`[F_1,F_2]=0`$ gives $`e^{iC\lambda}=e^{iF_1\lambda}e^{iF_2\lambda}`$; with $`[F_2,\Pi]=0`$ and $`[F_1,\Pi']=0`$: $`\Pi(\lambda)=e^{iF_1\lambda}\Pi e^{-iF_1\lambda}`$ and $`\Pi'(\lambda')=e^{iF_2\lambda'}\Pi'e^{-iF_2\lambda'}`$.
2. With $`W:=e^{iF_1\lambda}e^{iF_2\lambda'}`$, the same commutators give $`W\Pi W^\dagger=\Pi(\lambda)`$ and $`W\Pi'W^\dagger=\Pi'(\lambda')`$, so $`[\Pi(\lambda),\Pi'(\lambda')]=W[\Pi,\Pi']W^\dagger=0`$.
3. $`C':=F_1/a_1+F_2/a_2`$ is split with terms $`F_i/a_i`$; by item 1 an event on $`\mathcal P_i`$ at $`a_i\lambda`$ under $`C'`$ has the operator $`e^{iF_i\lambda}(\cdot)e^{-iF_i\lambda}`$, the same as at $`\lambda`$ under $`C`$.
4. A re-timing keeps the order of the events within each part ($`a_i>0`$) and can change only the relative order of events on different parts, whose operators commute (item 2). By the comparison rule of Step 1:

```math
[\Pi(\lambda),\Pi'(\lambda')]=0,\qquad\bigl(a_1,\,a_2,\,F_1/a_1+F_2/a_2\bigr)\ \text{is an equivalence of } C\ \text{ for all } a_1,a_2>0 .
\qquad\text{(10.6)}
```

The first statement holds for every split $`C`$. The second holds provided $`F_1/a_1+F_2/a_2=C/a_1+(1/a_2-1/a_1)F_2`$ is a sum of pair terms (A5): for $`a_1\neq a_2`$ this is the case iff the split is a pair-term split. It is automatic when each part is one object.

**(a) Uncoupled parts** are split with $`F_1=C_1\otimes\mathbb 1`$, $`F_2=\mathbb 1\otimes C_2`$. Hence, for every start (product or not; the proof is an operator identity):

```math
\Bigl(a_1,\,a_2,\,\tfrac1{a_1}C_1\otimes\mathbb 1+\tfrac1{a_2}\mathbb 1\otimes C_2\Bigr)\ \text{is an equivalence for all } a_1,a_2>0 .
\qquad\text{(10.7)}
```

- $`C'`$ is a sum of pair terms, that is, the split is a pair-term split: $`C_1\otimes\mathbb 1=d_2^{-1}\mathrm{Tr}_2C\otimes\mathbb 1-\text{const}`$ ($`d_2=\dim\mathcal H_2`$), and $`\mathrm{Tr}_2`$ maps each pair term of $`C`$ to a pair term inside $`\mathcal P_1`$, a single-object term or a constant (A5).
- M6: $`(C_1,C_2)\to(C_1+c,C_2-c)`$ changes $`C'`$ by $`c\,(1/a_1-1/a_2)\mathbb 1`$, which changes no statistics.

**(b)** (10.7) with $`a_1\neq a_2`$ exists for every uncoupled $`C`$: **the common now is not detectable for uncoupled parts.** For events $`e_1`$ on $`\mathcal P_i`$ and $`e_2`$ on $`\mathcal P_j`$, $`j\neq i`$, with $`\lambda_1<\lambda_2`$:

```math
a_i\lambda_1=a_j\lambda_2\iff\frac{a_i}{a_j}=\frac{\lambda_2}{\lambda_1},
\qquad
a_i\lambda_1>a_j\lambda_2\iff\frac{a_i}{a_j}>\frac{\lambda_2}{\lambda_1}.
\qquad\text{(10.8)}
```

- If $`\lambda_1>0`$: both are solvable, and (10.7) is an equivalence for every pair $`(a_1,a_2)`$. So an equivalence making the two values of $`\lambda`$ equal exists, and one reversing their order exists.
- If $`\lambda_1=0`$: $`a_i\lambda_1=0<a_j\lambda_2`$ for every re-timing, so no equivalence of the defined class does either. The cause is the fixed origin of a linear re-timing, not a detectable order: by (10.6) the statistics do not depend on the relative order of events on different parts.

### Step 5. Single-event conditions (item 4a)

1. A single event $`(i,R,\lambda)`$ has $`p(s)=\langle\Psi_0\vert\Pi_s(\lambda)\vert\Psi_0\rangle`$. Equality with the re-timed schedule under $`C'`$ for every start, every reading and every $`\lambda\ge0`$ is, by (F0), equivalent to

```math
e^{iC\lambda}\,\Pi\,e^{-iC\lambda}=e^{ia_iC'\lambda}\,\Pi\,e^{-ia_iC'\lambda}\qquad\text{for all }\lambda\ge0\text{ and all place projectors }\Pi\text{ of }\mathcal P_i,\ i=1,2 .
\qquad\text{(10.9)}
```

2. Both sides are entire functions of $`\lambda`$, so (10.9) is equivalent to the equality of all Taylor coefficients at $`\lambda=0`$. At first and second order:

```math
[C,\Pi]=a_i\,[C',\Pi]\quad\Longleftrightarrow\quad[\,C-a_iC',\,\Pi\,]=0 ,
\qquad\text{(10.10)}
```

```math
[C,[C,\Pi]]=a_i^{2}\,[C',[C',\Pi]] .
\qquad\text{(10.11)}
```

3. Given (10.10), the right side of (10.11) is $`a_i[C',[C,\Pi]]=[C-G_i,[C,\Pi]]`$, so (10.11) $`\iff[G_i,[C,\Pi]]=0`$. By the Jacobi identity and (10.10), $`[G_i,[C,\Pi]]=[[G_i,C],\Pi]+[C,[G_i,\Pi]]=a_i[[C,C'],\Pi]`$. Hence, given (10.10):

```math
\text{(10.11)}\iff[[C,C'],\Pi]=0\ \ \text{for all place projectors of }\mathcal P_i;\qquad\text{for both parts together}\iff[C,C']=0 .
\qquad\text{(10.12)}
```

   Proof of the last step: commuting with all $`\lvert h\rangle\langle h\rvert\otimes\lvert r\rangle\langle r\rvert`$ means that $`[C,C']`$ is diagonal; and its diagonal vanishes by item 4 below.

4. **Matrix form.** Decompose every operator by the kind of transition, $`X=X^{\rm d}+X^{(1)}+X^{(2)}+X^{(12)}`$: the elements $`X_{hr,h'r'}`$ with ($`h=h'`$, $`r=r'`$), ($`h\neq h'`$, $`r=r'`$), ($`h=h'`$, $`r\neq r'`$), ($`h\neq h'`$, $`r\neq r'`$). Since $`[G_1,\Pi]=0`$ for all $`\Pi`$ of $`\mathcal P_1`$ iff $`(G_1)_{hr,h'r'}=0`$ for $`h\neq h'`$, and likewise for $`G_2`$:

```math
\text{(10.10) for both parts}\iff C'^{(1)}=\frac{C^{(1)}}{a_1},\quad C'^{(2)}=\frac{C^{(2)}}{a_2},\quad C'^{(12)}=\frac{C^{(12)}}{a_1}=\frac{C^{(12)}}{a_2};\qquad C'^{\rm d}\ \text{free (real diagonal)}.
\qquad\text{(10.13)}
```

   So off the diagonal $`C_{hr,h'r'}=\alpha\,C'_{hr,h'r'}`$ and $`C_{h'r',hr}=\alpha\,C'_{h'r',hr}`$ with the same real $`\alpha\in\{a_1,a_2\}`$, and $`\langle hr\vert[C,C']\vert hr\rangle=\sum_{h'r'}\bigl(C_{hr,h'r'}C'_{h'r',hr}-C'_{hr,h'r'}C_{h'r',hr}\bigr)=0`$.

### Step 6. All equivalences and the two sufficient conditions (item 4b)

**Theorem (exact, every $`C`$).** For a re-timing $`(a_1,a_2,C')`$, that is, $`a_1,a_2>0`$ and $`C'`$ self-adjoint, independent of $`\lambda`$ and a sum of pair terms (A5):

```math
(a_1,a_2,C')\ \text{is an equivalence of } C\iff[\,C-a_iC',\Pi\,]=0\ \text{for all place projectors }\Pi\text{ of }\mathcal P_i\ (i=1,2)\ \text{ and }\ [C,C']=0 .
\qquad\text{(10.14)}
```

- *Necessity:* (10.10) and (10.12), from single-event schedules.
- *Sufficiency:* $`[C,C']=0`$ gives $`[G_i,C]=0`$, so $`e^{ia_iC'\lambda}=e^{iC\lambda}e^{-iG_i\lambda}`$, and $`[G_i,\Pi]=0`$ gives (10.9): every event has the same operator in both schedules. If $`a_1=a_2`$ the order of the events is unchanged. If $`a_1\neq a_2`$, put $`F_1:=\frac{a_1}{a_1-a_2}G_2`$, $`F_2:=\frac{a_2}{a_2-a_1}G_1`$. Then $`F_1+F_2=C`$, $`F_1/a_1+F_2/a_2=C'`$, $`[F_1,F_2]\propto[G_2,G_1]=(a_2-a_1)[C,C']=0`$, and (10.10) gives the last two relations of (10.5). So $`C`$ is split, and by the first statement of (10.6) the operators of events on different parts commute. The comparison rule of Step 1 applies in both cases. The split is a pair-term split, because $`G_1`$ and $`G_2`$ are sums of pair terms.

**Consequences.**
- For $`a_1=a_2=a`$, (10.10) for both parts says that $`C-aC'`$ is diagonal. Since $`C`$ is a sum of pair terms, $`C'=C/a+D`$ is one iff $`D`$ is:

```math
(a,a,C')\ \text{is an equivalence of } C\iff C'=C/a+D,\ \ D\ \text{real diagonal in the joint places and a sum of pair terms (A5)},\ \ [C,D]=0 .
\qquad\text{(10.15)}
```

  If each part is one object, every real diagonal $`D`$ is a sum of pair terms.
- An equivalence with $`a_1\neq a_2`$ exists iff $`C`$ has a pair-term split; then $`C'=C/a_1+(1/a_2-1/a_1)F_2`$. "Only if": the sufficiency proof above constructs the split. "If": (10.6). Hence the exact criterion:
  - **the common now is detectable iff $`C`$ has no pair-term split.**
  - "$`C`$ is not split" is sufficient for a detectable common now, and so are the conditions (10.16) below. It is the exact criterion when each part is one object, where every split is a pair-term split.
  - If a part has more than one object, a split whose components are not sums of pair terms gives no equivalence: "split" alone then does not show that the common now is undetectable.

**Sufficient condition for $`a_1=a_2`$ in every equivalence.**

```math
C^{(12)}\neq0\quad\text{or}\quad[C^{(1)},C^{(2)}]\neq0\qquad\Longrightarrow\qquad\text{every equivalence has } a_1=a_2 :\ \text{the common now is detectable.}
\qquad\text{(10.16)}
```

- If $`C^{(12)}\neq0`$: (10.13) gives $`(a_1-a_2)\,C'^{(12)}=0`$ with $`C'^{(12)}\neq0`$.
- If $`C^{(12)}=0`$: by (10.13), $`C'=C'^{\rm d}+C^{(1)}/a_1+C^{(2)}/a_2`$, and
  $`[C,C']=[C^{(1)},C'^{\rm d}-C^{\rm d}/a_1]+[C^{(2)},C'^{\rm d}-C^{\rm d}/a_2]+(1/a_2-1/a_1)[C^{(1)},C^{(2)}]`$. The three terms contain only transitions of kind (1), (2), (12) respectively, so by (10.14) each vanishes; the third gives $`a_1=a_2`$.
- In words: the contract changes the places of both parts in one step, or its place-changing terms of the two parts do not commute. The condition is sufficient, not necessary. It uses only necessary conditions on $`C'`$, so it holds for any number of objects.

**Sufficient condition for an equivalence with $`a_1\neq a_2`$ although the parts are coupled.** $`C`$ is coupled and has a pair-term split: then (10.6). A class that is always of this kind: $`C`$ commutes with every place projector of one part, say $`\mathcal P_2`$ (the places of $`\mathcal P_2`$ are conserved), $`C=\sum_rC_r\otimes\lvert r\rangle\langle r\rvert`$. Then $`F_1=C`$, $`F_2=0`$ is a pair-term split, and $`(a_1,a_2,C/a_1)`$ is an equivalence for all $`a_1,a_2>0`$. The parts are coupled iff $`C_r-C_{r'}\notin\mathbb R\,\mathbb 1`$ for some $`r,r'`$ (taking the $`(r,r)`$ block of $`C=C_1\otimes\mathbb 1+\mathbb 1\otimes C_2`$ gives $`C_r=C_1+(C_2)_{rr}\mathbb 1`$, and conversely).

### Step 7. The three examples (item 4c)

Each part is one object with places $`\lvert1\rangle,\lvert2\rangle`$, $`\sigma^z=\lvert1\rangle\langle1\rvert-\lvert2\rangle\langle2\rvert`$, $`\sigma^x=\lvert1\rangle\langle2\rvert+\lvert2\rangle\langle1\rvert`$; every self-adjoint $`C'`$ is one pair term. $`D=\sum d_{hr}\lvert hr\rangle\langle hr\rvert`$ is real diagonal, and $`[C,D]_{hr,h'r'}=C_{hr,h'r'}(d_{h'r'}-d_{hr})`$. In (ii), $`h`$ is the coupling constant. All three sets are exact, by (10.14).

**(i) $`C=g\,\sigma^x\otimes\sigma^x`$.** $`C=C^{(12)}\neq0`$, so $`a_1=a_2=a`$ by (10.16). By (10.15), $`C'=C/a+D`$ with $`[C,D]=0`$, i.e. $`d_{11}=d_{22}`$ and $`d_{12}=d_{21}`$:

```math
\mathcal E_{\rm(i)}=\bigl\{(a,\,a,\,C/a+c\,\mathbb 1+\mu\,\sigma^z\otimes\sigma^z):\ a>0,\ c,\mu\in\mathbb R\bigr\};\qquad\text{common now detectable.}
\qquad\text{(10.17)}
```

**(ii) $`C=g\,\sigma^z\otimes\sigma^z+h\,\sigma^x\otimes\mathbb 1`$.** $`C^{\rm d}=g\,\sigma^z\otimes\sigma^z`$, $`C^{(1)}=h\,\sigma^x\otimes\mathbb 1`$, $`C^{(2)}=C^{(12)}=0`$. By (10.13), $`C'=C^{(1)}/a_1+C'^{\rm d}`$, with no condition on $`a_2`$. Then $`[C,C']=[C^{(1)},E]`$ with $`E:=C'^{\rm d}-C^{\rm d}/a_1`$, which vanishes iff $`e_{1r}=e_{2r}`$, i.e. $`E=c\,\mathbb 1+\mu\,\mathbb 1\otimes\sigma^z`$:

```math
\mathcal E_{\rm(ii)}=\bigl\{(a_1,\,a_2,\,C/a_1+c\,\mathbb 1+\mu\,\mathbb 1\otimes\sigma^z):\ a_1,a_2>0,\ c,\mu\in\mathbb R\bigr\};\qquad\text{common now not detectable.}
\qquad\text{(10.18)}
```

The parts are coupled ($`g\neq0`$), and the places of $`\mathcal P_2`$ are conserved: the second sufficient condition of Step 6.

**(iii) $`C=t\,\sigma^x\otimes\mathbb 1+\kappa\,\lvert2\rangle\langle2\rvert\otimes\sigma^x`$.** $`C^{(1)}=t\,\sigma^x\otimes\mathbb 1`$, $`C^{(2)}=\kappa\,\lvert2\rangle\langle2\rvert\otimes\sigma^x`$, $`C^{\rm d}=C^{(12)}=0`$, and $`[C^{(1)},C^{(2)}]=t\kappa\,(\lvert1\rangle\langle2\rvert-\lvert2\rangle\langle1\rvert)\otimes\sigma^x\neq0`$, so $`a_1=a_2=a`$ by (10.16). By (10.15), $`C'=C/a+D`$ with $`[C,D]=0`$: $`d_{1r}=d_{2r}`$ (from $`t`$) and $`d_{21}=d_{22}`$ (from $`\kappa`$), so $`D=c\,\mathbb 1`$:

```math
\mathcal E_{\rm(iii)}=\bigl\{(a,\,a,\,C/a+c\,\mathbb 1):\ a>0,\ c\in\mathbb R\bigr\};\qquad\text{common now detectable.}
\qquad\text{(10.19)}
```

**Without $`g,h,t,\kappa>0`$.** If a constant vanishes, the contract is diagonal ((i) $`g=0`$, (ii) $`h=0`$), uncoupled ((ii) $`g=0`$, (iii) $`\kappa=0`$) or conserves the places of $`\mathcal P_1`$ ((iii) $`t=0`$). Each of these is split, with a pair-term split because each part is one object, and the common now is not detectable.

### Step 8. The order of two events on a chain (item 5)

With $`c_{st}:=[Q_t,\Pi_s]`$: $`P(s,t)=\langle\Psi_1\vert\Pi_sQ_t\Pi_s\vert\Psi_1\rangle`$ and $`\tilde P(s,t)=\langle\Psi_1\vert Q_t\Pi_sQ_t\vert\Psi_1\rangle`$.

**(a)** By (F0) ($`\Psi_1`$ runs over all unit vectors), $`P=\tilde P`$ for every start iff $`\Pi_sQ_t\Pi_s=Q_t\Pi_sQ_t=:T`$ for all $`s,t`$. Then $`T=TQ_t=T\Pi_s`$, so $`c_{st}^\dagger c_{st}=-(Q_t\Pi_s-\Pi_sQ_t)^2=-(TQ_t-\Pi_sQ_t\Pi_s-Q_t\Pi_sQ_t+T\Pi_s)=0`$; the converse is evident. By (7.1) with (F0), (F1), $`R_i`$ influences $`R_j`$ for no start iff $`\mathcal M_i(Q_t)=Q_t`$ for all $`t`$ iff $`[Q_t,\Pi_s]=0`$ for all $`s,t`$. Hence

```math
P=\tilde P\ \text{for every start}\iff[Q_t,\Pi_s]=0\ \text{for all }s,t\iff R_i\text{ influences }R_j\text{ for no start.}
\qquad\text{(10.20)}
```

For a single start only one direction holds: $`\sum_s\tilde P(s,t)=\lVert Q_t\Psi_1\rVert^2=P_j(t)`$ and $`\sum_sP(s,t)=P_j(t\mid R_i)`$, so

```math
\sum_s\bigl(P(s,t)-\tilde P(s,t)\bigr)=\Delta_t,\qquad\delta P\le\sum_{s,t}\bigl\lvert P(s,t)-\tilde P(s,t)\bigr\rvert .
\qquad\text{(10.21)}
```

$`P=\tilde P`$ implies no influence for that start; the converse fails (Check 3).

**(b)**
1. $`Q_t\Pi_s=\Pi_sQ_t+c_{st}`$ gives $`\Pi_sQ_t\Pi_s-Q_t\Pi_sQ_t=\Pi_sc_{st}-c_{st}Q_t`$, so $`\lvert P-\tilde P\rvert(s,t)\le\lVert c_{st}\rVert\,\bigl(\lVert\Pi_s\Psi_1\rVert+\lVert Q_t\Psi_1\rVert\bigr)`$.
2. $`c_{st}=[A(\delta),B]`$ with $`A=\Pi'_t-\tfrac12\mathbb 1`$ on cell $`j`$ and $`B=\Pi_s-\tfrac12\mathbb 1`$ on cell $`i`$, $`\lVert A\rVert,\lVert B\rVert\le\tfrac12`$; by (7.11), $`\lVert c_{st}\rVert\le\tfrac12\Sigma_r(\delta)`$.
3. $`\sum_s\lVert\Pi_s\Psi_1\rVert^2=1`$ and the Cauchy–Schwarz inequality give $`\sum_s\lVert\Pi_s\Psi_1\rVert\le\sqrt m`$; likewise $`\sum_t\lVert Q_t\Psi_1\rVert\le\sqrt{m'}`$, with $`m'`$ the number of classes of $`R_j`$.
4. Summing over the $`m\,m'`$ pairs, and using the last bound of (7.12): for every start, $`\delta\ge0`$, $`r\ge1`$,

```math
\sum_{s,t}\bigl\lvert P(s,t)-\tilde P(s,t)\bigr\rvert\le\Theta_{mm'}\,\Sigma_r(\delta)\le\Theta_{mm'}\,\frac{(2\lVert J\rVert\delta)^r}{r!}\,e^{2\lVert J\rVert\delta},
\qquad\Theta_{mm'}:=\tfrac12\sqrt{m\,m'}\,\bigl(\sqrt m+\sqrt{m'}\bigr).
\qquad\text{(10.22)}
```

5. The set on which this bound is below $`\epsilon`$, in the notation of (7.15):

```math
\tilde{\mathcal S}_\epsilon:=\bigl\{(r,\delta):\ r\ge1,\ \delta\ge0,\ \Theta_{mm'}\Sigma_r(\delta)<\epsilon\bigr\}=\mathcal S_{2\epsilon/\Theta_{mm'}}=\bigl\{(r,\delta):\ 0\le\delta<\delta_{2\epsilon/\Theta_{mm'}}(r)\bigr\}
\qquad\text{(10.23)}
```

   (last form for $`\lVert J\rVert>0`$; for $`\lVert J\rVert=0`$ it is all $`(r,\delta)`$ and $`P=\tilde P`$).
6. Comparison with (7.15): the same family of regions, with $`\epsilon`$ replaced by $`2\epsilon/\Theta_{mm'}`$. For $`m,m'\ge2`$, $`\Theta_{mm'}\ge2\sqrt2>2`$, so $`\tilde{\mathcal S}_\epsilon\subseteq\mathcal S_\epsilon`$, as (10.21) requires. If $`m=1`$ or $`m'=1`$, a projector is $`\mathbb 1`$ and $`P=\tilde P`$.
7. An explicit part of the set: for $`2\lVert J\rVert\delta\le r/e^2`$, the last bound of (7.12) and $`r!\ge(r/e)^r`$ give $`\Sigma_r(\delta)\le e^{-r}e^{r/e^2}`$, so

```math
\delta\le\frac{r}{2e^2\lVert J\rVert}\ \Longrightarrow\ \sum_{s,t}\lvert P-\tilde P\rvert\le\Theta_{mm'}\,e^{-(1-e^{-2})\,r};\qquad(r,\delta)\in\tilde{\mathcal S}_\epsilon\ \text{ if also }\ r>\frac{\ln(\Theta_{mm'}/\epsilon)}{1-e^{-2}} .
\qquad\text{(10.24)}
```

**(c)**
- **Equal $`\lambda`$** ($`\delta=0`$): $`Q_t=\Pi'_t`$ commutes with $`\Pi_s`$, so $`P=\tilde P`$ exactly, for every start and every pair of readings on different cells (consistent with (7.2)). The order of two events at equal $`\lambda`$ is not detectable.
- **Small delay over a large distance** ($`(r,\delta)\in\tilde{\mathcal S}_\epsilon`$, e.g. (10.24)): the statistics differ from the order-exchanged ones by less than $`\epsilon`$ for every start. The order is undetectable to accuracy $`\epsilon`$, but for $`\delta>0`$ in general not exactly.
- **In general:** by (10.20) the order of the two events is detectable for some start iff $`R_i`$ can influence $`R_j`$, and its statistical trace is at most (10.22). The order given by $`\lambda`$ is therefore detectable only where an influence is possible; elsewhere it is carried by the labels $`\lambda_k`$ alone. The boundary $`\delta_{2\epsilon/\Theta}(r)`$ depends on $`\epsilon`$: the detectable order is not sharp.

## Result

- **Item 1.** (10.2): $`(a,a,C/a)`$ is an equivalence for every $`C`$; the unit of $`\lambda`$ is never detectable. (10.3): for an eigenvector start, a common shift changes no statistics, and a single-event schedule does not depend on its $`\lambda`$.
- **Item 2.** (10.4): the marginal at the smaller $`\lambda`$ never depends on the later reading; the marginal at the larger $`\lambda`$ changes by $`\Delta_t`$, which vanishes for every start iff $`[Q_t,\Pi_s]=0`$. The direction is detectable wherever $`\Delta\neq0`$; it is fixed by the state update (1.3) (Law 1) as applied in A8, not by (1.9).
- **Item 3.** (10.5)–(10.7): the family $`(a_1,a_2,C_1/a_1\otimes\mathbb 1+\mathbb 1\otimes C_2/a_2)`$ for every start; the common now is not detectable; by (10.8) equal values and a reversed order are reachable iff $`\lambda_1>0`$.
- **Item 4.**
  - (10.9)–(10.13): the single-event conditions.
  - (10.14): all equivalences of a general $`C`$, among the contracts $`C'`$ that are sums of pair terms (A5). (10.15): those with $`a_1=a_2`$, with $`D`$ real diagonal and a sum of pair terms.
  - Exact criterion (Step 6): the common now is detectable iff $`C`$ has no pair-term split, that is, no split (10.5) whose components are sums of pair terms. If each part is one object, the pair-term conditions are automatic and the criterion is "$`C`$ is not split".
  - (10.16) and the pair-term split: the two sufficient conditions; (10.16) holds for any number of objects.
  - (10.17)–(10.19): the examples (each part one object), with the common now detectable in (i) and (iii), not in (ii).
- **Item 5.** (10.20), (10.21): $`P=\tilde P`$ for every start iff all $`[Q_t,\Pi_s]=0`$ iff no influence for any start; (10.22): the bound; (10.23), (10.24): the set; item (c) in Step 8.

## Consistency checks

1. **Dimensions and $`C=0`$.** $`C\lambda`$ is dimensionless, $`a_i`$ are pure numbers, so $`C/a`$, $`F_i/a_i`$ and $`\lVert J\rVert\delta`$ have the right dimensions. For $`C=0`$, (10.14) gives $`[C',\Pi]=0`$ for all place projectors: the equivalences are all $`(a_1,a_2,D)`$ with $`D`$ real diagonal and a sum of pair terms (A5); if each part is one object, every real diagonal $`D`$. Directly: under a diagonal contract every place projector is constant, so the statistics do not depend on any $`\lambda_k`$. Passed.
2. **Contract diagonal in the places**, e.g. $`C=g\,\sigma^z\otimes\sigma^z`$ (coupled). (10.14) again gives all $`(a_1,a_2,D)`$, $`D`$ real diagonal and a sum of pair terms (A5); in the example each part is one object, so every real diagonal $`D`$. The common now is not detectable although the parts are coupled, in agreement with the pair-term split $`F_1=C`$, $`F_2=0`$ and with (10.1), where all factors are constant and commute. Also $`c_{st}=0`$ while (10.22) is positive: the bound is not tight, as allowed. Passed.
3. **Example (i) against the exact evolution of two cells** ($`n=2`$, $`r=1`$, $`\lVert J\rVert=g`$, place readings). $`C`$ anticommutes with $`\mathbb 1\otimes\sigma^z`$, so $`(\mathbb 1\otimes\sigma^z)(\delta)=\cos(2g\delta)\,\mathbb 1\otimes\sigma^z+\sin(2g\delta)\,\sigma^x\otimes\sigma^y`$.
   - $`\mathcal M(Q_\pm)-Q_\pm=\mp\tfrac12\sin(2g\delta)\,\sigma^x\otimes\sigma^y`$: the value of $`\Delta_t`$ used in Step 3; $`\lVert c_{st}\rVert=\tfrac12\lvert\sin2g\delta\rvert\le\tfrac12(e^{2g\delta}-1)`$, as in Step 8(b).
   - $`\Psi_1=\lvert11\rangle`$: $`P=(\cos^2,\sin^2,0,0)`$ and $`\tilde P=(\cos^4,\sin^4,\sin^2\cos^2,\sin^2\cos^2)`$ for $`(s,t)=(1,1),(1,2),(2,1),(2,2)`$, argument $`g\delta`$. So $`\sum\lvert P-\tilde P\rvert=\sin^2(2g\delta)\le2\sqrt2\,(e^{2g\delta}-1)`$, and $`\Delta_t=0`$ although $`P\neq\tilde P`$.
   - Under $`C'=C/a+\mu\,\sigma^z\otimes\sigma^z`$ at $`a\delta`$ the same operator results, because $`\sigma^z\otimes\sigma^z`$ commutes with $`C`$ and with $`\mathbb 1\otimes\sigma^z`$: agreement with (10.17). Passed.

## Open issues

- The exact criterion for a detectable common now is the absence of a pair-term split (Step 6). It is not turned into an explicit classification of the coupled contracts (out of scope). "Not split" is the exact criterion only when each part is one object; for a part with more than one object it is sufficient, and whether a contract exists that is split but has no pair-term split was not examined.
- Item 2 treats two events on different parts. Whether the direction can be detected when no reading on one part influences a reading on the other (for example split $`C`$) was not examined; (10.4) itself holds for any two readings.
- $`\tilde P`$ is the comparator defined in the question, not the statistics of a schedule; item 5(c) refers to this notion. The constant $`\Theta_{mm'}`$ in (10.22) is not optimized.
- Re-timings that are not linear, more than two parts and readings represented by records are out of scope.

## Methods used

- Heisenberg form of sequential reading statistics
- Operator identities from quadratic forms (polarization)
- Taylor expansion of conjugations, nested commutators, Jacobi identity
- Decomposition of an operator by transition type in the place basis
- Commuting splits of a self-adjoint operator
- Pauli algebra for two two-place objects
- Commutator bound (7.11) with Cauchy–Schwarz inequality
