# Re-timings of classes of places: which relative factors of clock rates are detectable

- **Subproject:** 05-ilang-free-fall
- **Package:** 05-rate-comparison
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-10

## Setup and assumptions

- **Setting** (question.md, "Goal"): objects $`o=1,\dots,n`$ of pairwise different types, $`\mathcal H=\bigotimes_o\mathcal H_o`$; $`C`$ self-adjoint, independent of $`\lambda`$, a sum of pair terms (A5); a start $`\Psi_0`$ at $`\lambda=0`$, only $`\lambda\ge0`$; classes $`\ell`$ with object $`o(\ell)`$ and block $`B_\ell`$; readings of a class, schedules, re-timings $`((a_\ell),C')`$ and equivalences as defined there. $`\mathcal R`$ is the set of read classes. "Detectable" is used only in the sense of the question: every equivalence of $`C`$ has $`a_\ell=a_{\ell'}`$.
- **Inputs.** From 04-ilang-time/10-global-order@v2: the statistics (10.1) of a schedule, $`P(s_1,\dots,s_K)=\lVert\Pi^{(K)}_{s_K}(\lambda_K)\cdots\Pi^{(1)}_{s_1}(\lambda_1)\Psi_0\rVert^2`$ with $`\lambda_1\le\dots\le\lambda_K`$ and $`Y(\lambda)=e^{iC\lambda}Ye^{-iC\lambda}`$. Its results for two parts, (10.5), (10.6), (10.7), (10.13)–(10.16), are not used as inputs: their analogues for classes are derived in Steps 1–4 and compared with them in check 1. From 03-clock-and-fall@v3: the class $`\mathcal C`$ and its notation, and (3.23), (3.24), (3.36), used only in Step 9.
- **Notation.** $`K=(h_1,\dots,h_n)`$ is a joint place, $`Y_{KK'}=\langle K\vert Y\vert K'\rangle`$, $`Y^{\rm d}`$ the diagonal part and $`Y^{\rm off}=Y-Y^{\rm d}`$. A pair $`K\neq K'`$ **touches** the class $`\ell`$ if, for $`o=o(\ell)`$, $`h_o\neq h'_o`$ and at least one of $`h_o,h'_o`$ lies in $`B_\ell`$. Every pair $`K\neq K'`$ touches at least one class. $`C^{\langle\ell\rangle}`$ is the part of $`C`$ on the pairs that touch $`\ell`$. $`\mathcal A_\ell`$ is the algebra of the operators that commute with all place projectors of $`\ell`$. The **transition graph** of $`C`$ has the joint places as vertices and an edge $`K - K'`$ whenever $`C_{KK'}\neq0`$, $`K\ne K'`$. For the evolved projectors under the two contracts, $`\Pi^{C}(\lambda)=e^{iC\lambda}\Pi e^{-iC\lambda}`$ and $`\Pi^{C'}(\lambda)=e^{iC'\lambda}\Pi e^{-iC'\lambda}`$.
- **M6.** Every condition below refers to the operator $`C`$, to the place basis (A2) and to the blocks. "Sum of pair terms" means membership in the real linear space $`\mathcal S`$ of such operators, not a property of a list. Restricting an operator of $`\mathcal S`$ entrywise to the diagonal, or to the pairs $`(K,K')`$ that touch classes of a given set only, gives an operator of $`\mathcal S`$: for a pair term on the objects $`(a,b)`$ the entries vanish unless $`h_o=h'_o`$ for $`o\neq a,b`$, so the restriction depends on $`(h_a,h'_a,h_b,h'_b)`$ only and is again a pair term on $`(a,b)`$.
- **No approximation** is made; all statements are exact for finitely many places (A1). Contracts studied in Steps 6–8 are assumptions of the items (M8).

## Derivation

### Step 1. Place projectors and touching

For $`S\subseteq B_\ell`$, $`o=o(\ell)`$, and any operator $`Y`$,

```math
\langle K\vert[Y,\Pi_S]\vert K'\rangle=Y_{KK'}\bigl(1_S(h'_o)-1_S(h_o)\bigr),\qquad\text{hence}\qquad Y\in\mathcal A_\ell\iff Y_{KK'}=0\ \text{on every pair that touches }\ell .
\qquad\text{(5.1)}
```

Proof of the equivalence: if the pair touches $`\ell`$ with, say, $`h_o\in B_\ell`$, take $`S=\{h_o\}`$; the bracket is $`-1`$. If it does not touch $`\ell`$, then $`h_o=h'_o`$ or both lie outside $`B_\ell`$, and the bracket is $`0`$ for every $`S\subseteq B_\ell`$. The class projectors of a reading of $`\ell`$ are projectors $`\Pi_S`$ and $`\mathbb 1-\Pi_{B_\ell}`$; every $`\Pi_S`$ occurs in some reading.

**(G)** The blocks of an object cover its places, so every $`\lvert h\rangle\langle h\rvert`$ is a place projector of a class, and $`\lvert K\rangle\langle K\rvert=\prod_o\lvert h_o\rangle\langle h_o\rvert`$. If every class is read, the place projectors of the read classes generate all operators that are diagonal in the joint places. If some class is not read, (G) fails and is not used.

### Step 2. Operator form of an equivalence (any $`\mathcal R`$)

```math
((a_\ell),C')\ \text{is an equivalence}\iff
\begin{cases}
\text{(I)}\ \ \Pi^{C'}(a_\ell\lambda)=\Pi^{C}(\lambda)\ \text{ for all }\lambda\ge0\text{ and all place projectors }\Pi\text{ of every }\ell\in\mathcal R,\\[2pt]
\text{(II)}\ \ [\Pi_1^{C}(\lambda),\Pi_2^{C}(\lambda')]=0\ \text{ for all }\lambda,\lambda'\text{ and all }\Pi_1\text{ of }\ell,\ \Pi_2\text{ of }\ell'\ \text{with }\ell,\ell'\in\mathcal R,\ a_\ell\neq a_{\ell'} .
\end{cases}
\qquad\text{(5.2)}
```

*Necessity.* (I): for a schedule with one event $`(\ell,R,\lambda)`$, (10.1) gives $`\langle\Psi_0\vert\Pi^{C'}(a_\ell\lambda)\vert\Psi_0\rangle=\langle\Psi_0\vert\Pi^{C}(\lambda)\vert\Psi_0\rangle`$ for every unit vector, so the two self-adjoint operators are equal. (II): let $`a_\ell>a_{\ell'}`$ and $`\lambda<\lambda'<(a_\ell/a_{\ell'})\lambda`$, so the re-timing reverses the order of the two events. With $`P=\Pi_1^{C}(\lambda)`$, $`Q=\Pi_2^{C}(\lambda')`$ and (I), the outcome probabilities are $`\langle\Psi_0\vert PQP\vert\Psi_0\rangle`$ before and $`\langle\Psi_0\vert QPQ\vert\Psi_0\rangle`$ after, for every start, so $`PQP=QPQ`$. Then $`PQP=PQPQ=QPQP`$ and $`(PQ-QP)^\dagger(PQ-QP)=QPQ-QPQP-PQPQ+PQP=QPQ-PQP=0`$, so $`[P,Q]=0`$ on an open set of $`(\lambda,\lambda')`$, and everywhere because the commutator is an entire function of $`(\lambda,\lambda')`$.

*Sufficiency.* By (I) every factor of (10.1) for the re-timed schedule under $`C'`$ is the same operator as for the original schedule under $`C`$ (also for $`\mathbb 1-\Pi_{B_\ell}`$). The order of two factors can differ only if their classes have different factors, or at a tie. Tied factors commute (two diagonal projectors conjugated by one unitary); the others commute by (II). A reordering by exchanges of commuting neighbours does not change the product. $`\blacksquare`$

(5.2) uses neither (G) nor A5, and no projector of a class that is not read.

### Step 3. Commutator form

```math
\begin{aligned}
&\text{(N)}\ \ \text{equivalence}\ \Longrightarrow\ \text{(i)}\ [\,C-a_\ell C',\Pi\,]=0\ \text{ and }\ \text{(ii}'\text{)}\ [[C,C'],\Pi]=0\ \text{ for all place projectors }\Pi\text{ of every }\ell\in\mathcal R;\\
&\text{(S)}\ \ \text{(i) for every }\ell\in\mathcal R\ \text{ and }\ \text{(ii)}\ [C,C']=0\ \Longrightarrow\ \text{equivalence};\\
&\text{every class read:}\qquad\text{equivalence}\iff\text{(i) for every class and (ii)} .
\end{aligned}
\qquad\text{(5.3)}
```

*(N).* Both sides of (I) are entire in $`\lambda`$; equality on $`\lambda\ge0`$ gives equal derivatives at $`0`$. First order: $`[C,\Pi]=a_\ell[C',\Pi]`$, which is (i). Second order: $`[C,[C,\Pi]]=a_\ell^2[C',[C',\Pi]]`$; inserting (i) on both sides gives $`[C,[C',\Pi]]=[C',[C,\Pi]]`$, and by the Jacobi identity the difference of the two sides is $`[[C,C'],\Pi]`$. Only single-event schedules of read classes are used.

*(S).* Let $`E_\ell:=C-a_\ell C'`$. By (ii), $`[C,E_\ell]=0`$, so $`e^{ia_\ell C'\lambda}=e^{iC\lambda}e^{-iE_\ell\lambda}`$, and by (i) $`e^{-iE_\ell\lambda}`$ commutes with $`\Pi`$: this is (I). For $`a_\ell\neq a_{\ell'}`$ put $`F_{\ell}:=-\frac{a_\ell}{a_{\ell'}-a_\ell}E_{\ell'}`$ and $`F_{\ell'}:=\frac{a_{\ell'}}{a_{\ell'}-a_\ell}E_\ell`$. Then $`C=F_\ell+F_{\ell'}`$, $`[F_\ell,F_{\ell'}]=0`$, $`F_\ell\in\mathcal A_{\ell'}`$, $`F_{\ell'}\in\mathcal A_\ell`$, hence $`\Pi_1^{C}(\lambda)=e^{iF_\ell\lambda}\Pi_1e^{-iF_\ell\lambda}`$, $`\Pi_2^{C}(\lambda')=e^{iF_{\ell'}\lambda'}\Pi_2e^{-iF_{\ell'}\lambda'}`$, and their product is $`e^{iF_\ell\lambda}e^{iF_{\ell'}\lambda'}\Pi_1\Pi_2e^{-iF_{\ell'}\lambda'}e^{-iF_\ell\lambda}`$, symmetric in the two because $`[\Pi_1,\Pi_2]=0`$: this is (II). Then (5.2) applies. Only projectors of read classes are used.

*Every class read.* By (5.1), (i) for all classes says: on every pair $`K\neq K'`$, $`C_{KK'}=a_\ell C'_{KK'}`$ for every class $`\ell`$ that the pair touches. By (G) and (ii'), $`[C,C']`$ is diagonal. Its diagonal is $`\sum_{K'}(C_{KK'}C'_{K'K}-C'_{KK'}C_{K'K})`$, and each term with $`K'\neq K`$ vanishes because $`C'_{KK'}`$ and $`C'_{K'K}`$ are $`C_{KK'}`$ and $`C_{K'K}`$ divided by the same number. Hence (ii). $`\blacksquare`$

**Hypotheses.** (G) is used in one place only: (ii') $`\Rightarrow`$ (ii), and it needs (i) for all classes. A5 for $`C'`$ is used in no implication of (5.2), (5.3); it is the admissibility condition in the definition of a re-timing and must be imposed on the solution $`C'`$ (condition (E4) below). For $`n=2`$ every self-adjoint operator is one pair term and A5 is empty. If some classes are not read, what is proven is (5.2), (N) and (S); between (N) and (S) a gap remains in general.

### Step 4. Matrix elements, equal factors, splits (every class read)

Let $`\alpha_1,\dots,\alpha_q`$ be the distinct values of the factors and $`\mathcal G_i`$ the set of classes with $`a_\ell=\alpha_i`$. By (5.1) and (5.3)(i): if $`C_{KK'}\neq0`$, all classes touched by $`(K,K')`$ have one factor; if $`C_{KK'}=0`$ then $`C'_{KK'}=0`$. Let $`C^{[i]}`$ be the part of $`C^{\rm off}`$ on the pairs that touch classes of $`\mathcal G_i`$ only (for two groups $`\mathcal G`$, $`\bar{\mathcal G}`$ these parts are written $`C^{[\mathcal G]}`$, $`C^{[\bar{\mathcal G}]}`$). Then (i) is equivalent to (E1) together with $`C'^{\rm off}=\sum_iC^{[i]}/\alpha_i`$. A product of an entry of $`C^{[i]}`$ and an entry of $`C^{[i']}`$, $`i\neq i'`$, changes disjoint sets of objects (an object changed by both would have a place in blocks of both groups), so $`[C^{[i]},C^{[i']}]`$ lives on pairs touching exactly the groups $`i`$ and $`i'`$, while $`[C^{\rm d},C^{[i]}]`$ and $`[C'^{\rm d},C^{[i]}]`$ live on pairs touching the group $`i`$ only. These sets of entries are disjoint, so (ii) splits into (E2) and (E3):

```math
((a_\ell),C')\ \text{equivalence}\iff
\begin{cases}
\text{(E1)}\ \text{every }C_{KK'}\neq0,\ K\neq K',\ \text{touches classes of one group only: }C=C^{\rm d}+\sum_iC^{[i]};\\
\text{(E2)}\ [C^{[i]},C^{[i']}]=0\ \text{for }i\neq i';\\
\text{(E3)}\ C'=C'^{\rm d}+\sum_iC^{[i]}/\alpha_i,\ \ C'^{\rm d}\ \text{real diagonal with }[\,C^{\rm d}-\alpha_iC'^{\rm d},C^{[i]}\,]=0\ \text{for all }i;\\
\text{(E4)}\ C'^{\rm d}\in\mathcal S\ \ (\text{A5; then }C'\in\mathcal S\text{ by the remark under M6}).
\end{cases}
\qquad\text{(5.4)}
```

**Freedom at given factors, 1(c) second part.** If $`((a_\ell),C')`$ and $`((a_\ell),C'')`$ are equivalences, (i) gives $`C''-C'\in\bigcap_\ell\mathcal A_\ell`$, which is diagonal by (G), and (E3) gives $`[C''-C',C^{[i]}]=0`$. Conversely such a term may be added. So

```math
C'\ \text{is unique up to}\ C'\to C'+D,\quad D\ \text{real diagonal},\ D\in\mathcal S,\ [C,D]=0;\qquad a_\ell=\alpha\ \text{for all }\ell:\quad C'=\frac C\alpha+D .
\qquad\text{(5.5)}
```

$`[C,D]=0`$ means that $`D`$ is constant on each connected component of the transition graph of $`C`$. If the graph is connected, $`C'=C/\alpha+d\,\mathbb 1`$: the freedom is the number $`d`$.

**Equal factors, 1(b).** Each of the following conditions on the entries of $`C`$ implies $`a_\ell=a_{\ell'}`$ in every equivalence:

```math
\begin{aligned}
&\text{(T1)}\ \text{some }C_{KK'}\neq0\text{ touches both }\ell\text{ and }\ell';\qquad\text{(T2)}\ \ell,\ell'\text{ are joined by a chain of classes, consecutive ones related by (T1)};\\
&\text{(T3)}\ \text{no entry touches both, and }\langle K\vert[C^{\langle\ell\rangle},C^{\langle\ell'\rangle}]\vert K'\rangle\neq0\text{ for some pair }(K,K')\text{ that touches both}.
\end{aligned}
\qquad\text{(5.6)}
```

(T1), (T2) follow from (E1) and hold also when only $`\ell,\ell'`$ and the classes of the chain are read ((N)(i)). (T3): if $`a_\ell\neq a_{\ell'}`$, write $`C^{[i]}=C^{\langle\ell\rangle}+G`$, $`C^{[i']}=C^{\langle\ell'\rangle}+G'`$ for their groups; $`C^{\langle\ell\rangle},G,G'\in\mathcal A_{\ell'}`$ and $`C^{\langle\ell'\rangle},G,G'\in\mathcal A_\ell`$, so by (5.1) all terms of $`[C^{[i]},C^{[i']}]`$ except $`[C^{\langle\ell\rangle},C^{\langle\ell'\rangle}]`$ vanish on pairs touching both, and (E2) contradicts (T3).
- *Two classes of one object $`o`$:* (T1) reads $`C_{KK'}\neq0`$ with $`h_o\in B_\ell`$, $`h'_o\in B_{\ell'}`$ (a hop between the blocks, whatever the other objects do). (T3) adds nothing to (T2): a two-step path from $`B_\ell`$ to $`B_{\ell'}`$ passes through a third block linked to both.
- *Two classes of different objects $`o\neq o'`$:* (T1) reads $`C_{KK'}\neq0`$ with $`h_o\neq h'_o`$, $`h_{o'}\neq h'_{o'}`$, one of $`h_o,h'_o`$ in $`B_\ell`$ and one of $`h_{o'},h'_{o'}`$ in $`B_{\ell'}`$ (a joint transition); (T3) is the non-commutativity of the separate transitions.
- These conditions are sufficient, not necessary: the diagonal condition (E3) can fail as well. The exact statement is: $`a_\ell=a_{\ell'}`$ in every equivalence iff no division of the classes into groups that separates $`\ell`$ from $`\ell'`$ satisfies (E1)–(E4).

**Two values, 1(c).** For $`q=2`$, $`\mathcal G_1=\mathcal G`$, $`\mathcal G_2=\bar{\mathcal G}`$ (the other classes), put $`D_{\mathcal G}:=\frac{\alpha}{\alpha-\alpha'}(C^{\rm d}-\alpha'C'^{\rm d})`$, $`F_{\mathcal G}:=C^{[\mathcal G]}+D_{\mathcal G}`$, $`F_{\bar{\mathcal G}}:=C-F_{\mathcal G}`$. Then (5.4) becomes: an equivalence with $`a_\ell=\alpha`$ on $`\mathcal G`$ and $`a_\ell=\alpha'\neq\alpha`$ elsewhere exists iff $`C`$ has a **pair-term split along $`\mathcal G`$**,

```math
C=F_{\mathcal G}+F_{\bar{\mathcal G}},\quad[F_{\mathcal G},F_{\bar{\mathcal G}}]=0,\quad F_{\mathcal G}\in\bigcap_{\ell\notin\mathcal G}\mathcal A_\ell,\quad F_{\bar{\mathcal G}}\in\bigcap_{\ell\in\mathcal G}\mathcal A_\ell,\quad F_{\mathcal G},F_{\bar{\mathcal G}}\in\mathcal S;\qquad C'=\frac{F_{\mathcal G}}{\alpha}+\frac{F_{\bar{\mathcal G}}}{\alpha'}\ (+D\text{ of (5.5)}).
\qquad\text{(5.7)}
```

In entries: (S1) no $`C_{KK'}\neq0`$ touches a class of $`\mathcal G`$ and a class outside it; (S2) $`[C^{[\mathcal G]},C^{[\bar{\mathcal G}]}]=0`$; (S3) $`C^{\rm d}=D_{\mathcal G}+D_{\bar{\mathcal G}}`$ with real diagonal $`D_{\mathcal G}`$ constant along the edges of $`C^{[\bar{\mathcal G}]}`$ and $`D_{\bar{\mathcal G}}`$ constant along the edges of $`C^{[\mathcal G]}`$; (S4) $`D_{\mathcal G}\in\mathcal S`$. Proof: "$`\Leftarrow`$": $`C-\alpha C'=(1-\alpha/\alpha')F_{\bar{\mathcal G}}`$ and $`C-\alpha'C'=(1-\alpha'/\alpha)F_{\mathcal G}`$ give (i), and $`[C,C']=0`$; $`C'`$ is self-adjoint, independent of $`\lambda`$ and in $`\mathcal S`$. "$`\Rightarrow`$": (E1)–(E3) give (S1)–(S3) with the $`D_{\mathcal G}`$ above, and $`F_{\mathcal G}=\frac{\alpha\alpha'}{\alpha'-\alpha}(C'-C/\alpha')\in\mathcal S`$. The condition does not depend on the values $`\alpha\neq\alpha'`$. A5 enters through (S4) only, and is empty for $`n=2`$.

**Several groups (sufficient, any $`\mathcal R`$).** If $`C=\sum_iF_i`$ with self-adjoint $`F_i\in\mathcal S`$, $`[F_i,F_j]=0`$, and $`F_i\in\mathcal A_\ell`$ for every read class $`\ell\notin\mathcal G_i`$, then

```math
\Bigl(a_\ell=\alpha_i\ \text{for }\ell\in\mathcal G_i,\ \ C'=\sum_i\frac{F_i}{\alpha_i}\Bigr)\ \text{is an equivalence for all }\alpha_i>0,
\qquad\text{(5.8)}
```

because $`C-\alpha_iC'=\sum_{j\neq i}(1-\alpha_i/\alpha_j)F_j`$ gives (i) for the read classes of $`\mathcal G_i`$, and $`[C,C']=0`$; then (5.3)(S). A group may consist of classes that are not read.

### Step 5. Readings with one outcome per block

Let the blocks of an object be $`B_1,\dots,B_q`$, $`Q_i:=\Pi_{B_i}`$. The readings "in $`B_i`$ or not" have the class projectors $`Q_i`$, $`\mathbb 1-Q_i`$, which commute, with $`Q_iQ_j=0`$ ($`i\neq j`$) and $`\sum_iQ_i=\mathbb 1`$. Applied at one $`\lambda`$, the product of the class projectors of an outcome string is

```math
Q_i\prod_{j\neq i}(\mathbb 1-Q_j)=Q_i\ \ \text{(exactly one "in", at }i),\qquad 0\ \ \text{otherwise (also for no "in":}\ \prod_j(\mathbb 1-Q_j)=\mathbb 1-\textstyle\sum_jQ_j=0).
\qquad\text{(5.9)}
```

So the outcome strings with nonzero probability correspond one to one to the blocks, with probability $`\lVert Q_i\Psi\rVert^2`$ and state $`Q_i\Psi/\lVert Q_i\Psi\rVert`$ after the readings: the same as for the reading with one outcome per block, by (1.3). A re-timing moves the reading of the block $`i`$ to $`a_i\lambda`$. If the factors of the blocks are equal, the readings stay at one value of the parameter. If they differ, the re-timed schedule contains $`q`$ yes/no readings at up to $`q`$ different values; in an equivalence its statistics is unchanged by definition (by (5.2) the evolved projectors are the same operators and commute), but in the re-timed description it is not a reading of the object at one value of $`\lambda`$. "Reading the block label at one $`\lambda`$" is therefore preserved by all equivalences only if all relative factors of the blocks are detectable.

### Step 6. One body on a chain: the entries of $`C`$ (item 2)

Assumption of the item (M8): $`C=C_b\otimes\mathbb 1_c+\kappa\,\hat x\otimes X`$ with $`C_b\in\mathcal C`$ on the chain $`\lvert x\rvert\le L`$, $`L\ge1`$; the medium has no contract of its own. There are two objects, so every self-adjoint operator on $`\mathcal H_b\otimes\mathcal H_c`$ is one pair term: $`\mathcal S`$ is everything, and (E4), (S4) are empty. Every contract constructed in Steps 6–8 is self-adjoint, independent of $`\lambda`$ and a pair term between $`b`$ and $`c`$. From here on the diagonal term of (5.5) is written $`\Delta`$, because $`D`$ is the clock operator of the class $`\mathcal C`$. Joint places are $`(x,s,a;r)`$ with $`r\in H_c`$. The entries of $`C`$ are:
- *hopping:* $`(x,s,a;r)\leftrightarrow(x+1,\bar s,a;r)`$ with modulus $`\tau\zeta_x/2`$; it touches the classes $`x`$ and $`x+1`$;
- *clock:* $`(x,s,a;r)\leftrightarrow(x,s,a';r)`$, $`a\neq a'`$, with value $`\pm\eta_xD_{aa'}`$, $`D_{aa'}=\frac{2\pi}{N\lambda_0}\bigl(e^{2\pi i(a-a')/N}-1\bigr)^{-1}\neq0`$ (from $`\sum_{k=0}^{N-1}k\,\omega^k=N/(\omega-1)`$ for $`\omega^N=1`$, $`\omega\neq1`$); it touches $`x`$ only;
- *medium:* $`(x,s,a;r)\leftrightarrow(x,s,a;r')`$ with value $`\kappa\,x\,X_{rr'}`$; it touches $`c`$ only, and is absent at $`x=0`$;
- *diagonal:* $`\pm\bigl(m_x+\eta_x\tfrac{\pi(N-1)}{N\lambda_0}\bigr)+V_x+\kappa\,x\,X_{rr}`$.

Two facts are used below. With $`\Sigma:=(-1)^{\hat x}\sigma_3\otimes\mathbb 1_N`$ and $`\Pi_\pm:=\tfrac12(\mathbb 1\pm\Sigma)`$, and with $`\gamma`$ running over the connected components of the graph of $`X`$ on $`H_c`$ (edge $`r - r'`$ iff $`X_{rr'}\neq0`$; projectors $`\Pi_\gamma`$; for a diagonal $`X`$ every place is a component):

```math
[\Sigma,C]=0\ \ (\Sigma\text{ is diagonal; }(-1)^{\hat x}\text{ and }\sigma_3\text{ each anticommute with the hopping}),\qquad[A_\zeta,\hat x]=\frac{i\tau}2\sum_x\zeta_x\bigl(R_x+R_x^\dagger\bigr)\otimes\sigma_1\otimes\mathbb 1_N .
\qquad\text{(5.10)}
```

The second follows from $`[R_x,\hat x]=-R_x`$.

### Step 7. Equivalences for the body on a chain (items 2(a), 2(b))

**(a) $`\tau>0`$, $`\zeta_x>0`$ on every bond.**
- *Positions.* The hopping entry on the bond $`(x,x+1)`$ is nonzero and touches $`x`$ and $`x+1`$: by (T1), (T2) all positions have one factor $`a_b`$. This uses (N)(i) for the position classes only, so it holds whether the medium is read or not: **every relative factor of two positions is detectable**, in both cases.
- *Body and medium, medium read.* $`C^{[b]}=A_\zeta+(\text{clock entries})`$, $`C^{[c]}=\kappa\,\hat x\otimes X^{\rm off}`$, and by (5.10) $`[C^{[b]},C^{[c]}]=\kappa[A_\zeta,\hat x]\otimes X^{\rm off}`$, which is nonzero iff $`X^{\rm off}\neq0`$. If $`X`$ is not diagonal, (E2) excludes $`a_c\neq a_b`$. If $`X`$ is diagonal, no entry touches $`c`$, (E2) and (E3) are empty for the group $`\{c\}`$, and $`a_c`$ is free.
- *The term $`\Delta`$.* The hopping and clock edges join exactly the body places with equal $`\Sigma`$; each of the two sets contains places with $`x\neq0`$, where the medium edges join the places of one $`\gamma`$. The components of the transition graph are the pairs $`(\epsilon,\gamma)`$.

```math
\text{(a):}\quad a_x=a_b\ \ \forall x;\qquad a_c=a_b\ \text{ if }X\text{ is not diagonal},\quad a_c>0\ \text{free if }X\text{ is diagonal};\qquad C'=\frac C{a_b}+\Delta,\quad\Delta=\sum_{\epsilon=\pm}\sum_\gamma d_{\epsilon\gamma}\,\Pi_\epsilon\otimes\Pi_\gamma,\ \ d_{\epsilon\gamma}\in\mathbb R .
\qquad\text{(5.11)}
```

These are all equivalences when the medium is read, by (5.4), (5.5). The relative factor of a position and the medium is detectable iff $`X`$ is not diagonal in the places of the medium.
- *Medium not read: what is proven.* By (N): $`a_x=a_b`$ and $`C'=C/a_b+Z`$ with $`Z=\sum_h\lvert h\rangle\langle h\rvert\otimes Z_h`$ ($`h`$ the places of the body, $`Z_h`$ self-adjoint on $`\mathcal H_c`$) and $`[[C,Z],\Pi]=0`$ for the place projectors of the body. By (S): $`[C,Z]=0`$ suffices; in particular the contracts of (5.11) are equivalences. The exact set between the two is not determined here; the detectable relative factors of positions do not depend on it.

**(b) $`\tau=0`$.** Now

```math
C=\sum_xF_x+F_c,\qquad F_x:=P_x\otimes\bigl(\sigma_3\otimes\mathsf M_x+V_x\,\mathbb 1\bigr)\otimes\mathbb 1_c,\qquad F_c:=\kappa\,\hat x\otimes X,
```

all terms commute with each other, $`F_x\in\mathcal A_y`$ for $`y\neq x`$ and $`F_x\in\mathcal A_c`$, and $`F_c\in\mathcal A_x`$ for all $`x`$. By (5.8) with every class as its own group, and by (5.5) (clock edges join all $`a`$ at fixed $`(x,s,r)`$; medium edges join the places of one $`\gamma`$ when $`x\neq0`$):

```math
\text{(b):}\quad\text{all }a_x>0,\ a_c>0\ \text{ occur};\qquad C'=\sum_x\frac{F_x}{a_x}+\frac{F_c}{a_c}+\Delta,\quad\Delta=\sum_{x,s}P_x\otimes\lvert s\rangle\langle s\rvert\otimes\mathbb 1_N\otimes\Delta_{x,s},\ \ \Delta_{x,s}\ \text{real diagonal},\ [\Delta_{x,s},x\,X]=0 .
\qquad\text{(5.12)}
```

This is the complete set when the medium is read, for $`X`$ diagonal and for $`X`$ not diagonal (for a diagonal $`X`$ the term $`F_c`$ is itself of the form $`\Delta`$, and $`a_c`$ drops out). **No relative factor is detectable**: not of two positions, and not of a position and the medium. When the medium is not read, (5.8) applies with the group $`\{c\}`$ not read, so the contracts of (5.12) remain equivalences and no relative factor of two positions is detectable.

*An equivalent contract of the class $`\mathcal C`$ with a flat clock profile exists:* take $`a_x=\eta_x`$, $`a_c=1`$, $`\Delta=0`$ in (5.12),

```math
C'=\sum_xP_x\otimes\Bigl[\sigma_3\otimes\Bigl(\frac{m_x}{\eta_x}\mathbb 1_N+D\Bigr)+\frac{V_x}{\eta_x}\mathbb 1\Bigr]\otimes\mathbb 1_c+\kappa\,\hat x\otimes X:\qquad\tau'=0,\ \ m'_x=\frac{m_x}{\eta_x}>0,\ \ \eta'_x=1,\ \ V'_x=\frac{V_x}{\eta_x},\ \ \lambda'_0=\lambda_0,\ \ K'_x=K_x .
\qquad\text{(5.13)}
```

**Control (M9).** The two cases are controls of each other: with hopping on every bond no equivalence separates two positions; without hopping every assignment of factors occurs. If $`\zeta_x=0`$ on some bonds only, the same arguments give one factor for each segment of the chain joined by hopping (not asked; stated without the list of $`\Delta`$).

### Step 8. Parameters of the class form (item 2(c))

**What the operator fixes (M6).** An operator of the form $`C=C_b\otimes\mathbb 1_c+\kappa\,\hat x\otimes X`$ with $`C_b\in\mathcal C`$ fixes $`\tau\zeta_x`$, $`\eta_x/\lambda_0`$, $`m_x`$, and the pair $`(\kappa X,V_x)`$ up to $`\kappa X\to\kappa X+\beta\,\mathbb 1`$, $`V_x\to V_x-\beta\,x`$ (a term diagonal in the places of the body, moved between the body term and the pair term). Two conventions are therefore needed to write the parameters:
- **K1:** the multiple of $`\mathbb 1_c`$ in $`X`$, for example $`\mathrm{Tr}X=0`$. Then $`C_b=\mathrm{Tr}_cC/d_c`$ is fixed by $`C`$, with $`V_x=\frac1{2N}\mathrm{Tr}\langle x\vert C_b\vert x\rangle`$, $`\mathsf M_x=\frac12\mathrm{Tr}_s\bigl(\sigma_3\langle x\vert C_b\vert x\rangle\bigr)`$, $`m_x`$ its lowest eigenvalue and $`2\pi\eta_x/(N\lambda_0)`$ its level spacing. Without K1 only $`V_x-V_y`$ modulo $`\beta\,(x-y)`$ is a property of $`C`$.
- **K2:** how $`\eta_x/\lambda_0`$ is divided into $`\eta_x`$ and $`\lambda_0`$. Here: $`\lambda'_0=\lambda_0`$, that is, $`C`$ and $`C'`$ are written with the same clock operator $`D`$.

So $`\eta_x/\eta_y`$ and the tick $`t_x:=\lambda_0/\eta_x`$ are properties of $`C`$ alone, as are $`m_xt_x`$ and $`\tau\zeta_xt_x`$; $`m_x/\eta_x`$ and $`\tau\zeta_x/\eta_x`$ need K2; $`(V_x-V_y)/\eta_x`$ needs K1 and K2.

**Equivalences whose contract has the class form.** Write $`\Delta=\mathbb 1\otimes Y_0+\Sigma\otimes Y_1`$ in (5.11), with $`Y_0,Y_1`$ real combinations of the $`\Pi_\gamma`$, and let a tilde denote the part that is traceless on $`\mathcal H_c`$. The class form $`C'=C'_b\otimes\mathbb 1_c+\kappa'\hat x\otimes X'`$ requires $`\frac\kappa{a_b}\hat x\otimes\tilde X+\mathbb 1\otimes\tilde Y_0+\Sigma\otimes\tilde Y_1=\kappa'\hat x\otimes\tilde X'`$. Since $`\hat x`$, $`\mathbb 1`$, $`\Sigma`$ are linearly independent on $`\mathcal H_b`$ and $`\tilde X\neq0`$: $`\tilde Y_0=\tilde Y_1=0`$, so $`\Delta=y_0\mathbb 1+y_1\Sigma`$. The same argument in (5.12), with $`\Delta=\sum_xP_x\otimes(\mathbb 1\otimes Y_{0,x}+\sigma_3\otimes Y_{1,x})`$, gives $`\tilde Y_{1,x}=0`$ and $`\tilde Y_{0,x}=x\,\tilde Y`$. Hence

```math
\text{(a):}\quad\tau'\zeta'_x=\frac{\tau\zeta_x}{a_b},\quad\frac{\eta'_x}{\lambda'_0}=\frac{\eta_x}{a_b\lambda_0},\quad m'_x=\frac{m_x}{a_b}+(-1)^xy_1,\quad V'_x=\frac{V_x}{a_b}+y_0-\beta x,\quad\kappa'X'=\frac{\kappa X}{a_b}+\beta\,\mathbb 1,
\qquad\text{(5.14)}
```

```math
\text{(b):}\quad\tau'\zeta'_x=0,\quad\frac{\eta'_x}{\lambda'_0}=\frac{\eta_x}{a_x\lambda_0},\quad m'_x=\frac{m_x}{a_x}+y_{1,x},\quad V'_x=\frac{V_x}{a_x}+y_{0,x},\quad\kappa'X'=\frac{\kappa X}{a_c}+\tilde Y+\beta\,\mathbb 1,\ \ \tilde Y\ \text{real diagonal},\ [\tilde Y,X]=0,
\qquad\text{(5.15)}
```

with arbitrary real $`y_0,y_1,\beta`$, $`y_{0,x},y_{1,x}`$ subject to $`m'_x>0`$ (and $`X'`$ not a multiple of $`\mathbb 1_c`$); $`\beta=0`$ when $`C`$ and $`C'`$ use the same K1. Every contract in (5.14), (5.15) is of the class $`\mathcal C`$ with the records $`\kappa'xX'`$, and is an equivalence by (5.11), (5.12). The term $`y_1\Sigma`$ adds a different constant on the two components $`\Sigma=\pm1`$, which no place projector connects; it changes $`m_x`$ by a staggered amount.

**Answer, under K1 and K2 for both contracts** ("same" means: equal for $`C`$ and for the contract of every equivalence of the class form):

```math
\begin{array}{l|l|l}
\text{quantity} & \text{(a) }\tau>0 & \text{(b) }\tau=0\\\hline
\eta_x/\eta_y & \text{same (no convention needed)} & \text{not the same: multiplied by }a_y/a_x,\ \text{any positive value}\\
m_x/\eta_x & \text{not the same: }+(-1)^xa_by_1/\eta_x & \text{not the same: }+a_xy_{1,x}/\eta_x\\
\tau\zeta_x/\eta_x & \text{same} & \text{same, trivially: both are }0\\
(V_x-V_y)/\eta_x & \text{same} & \text{not the same: }V'_x-V'_y\ \text{is arbitrary}\\
\text{tick }\lambda_0/\eta_x & \text{not the same: multiplied by }a_b;\ \text{ratios of ticks same} & \text{not the same: multiplied by }a_x;\ \text{ratios not the same}
\end{array}
\qquad\text{(5.16)}
```

Additions. In (a), $`m_x/\eta_x`$ is the same exactly for the equivalences with $`y_1=0`$; what is the same for every equivalence is $`(m_x+m_y)/\eta_z`$ for $`x-y`$ odd and $`(m_x-m_y)/\eta_z`$ for $`x-y`$ even. With another K2 (for example $`\eta'_{x_*}=\eta_{x_*}`$ at a reference position, so $`\lambda'_0=a_b\lambda_0`$) the entries "same" of rows 2–4 in (a) become "multiplied by $`1/a_b`$"; free of K2 are the products with the tick, $`\tau\zeta_xt_x`$ and $`(V_x-V_y)t_x`$. Without a common K1, row 4 in (a) fails by $`-a_b\beta(x-y)/\eta_x`$.

### Step 9. Two runs (item 4)

**What the comparison is (A8).** Two runs are two applications of one description (the same objects and the same $`C`$) with two starts, $`S_{\rm clock}(x_1)`$ and $`S_{\rm clock}(x_2)`$, each with its own schedule of one event: the reading of the clock label at $`\lambda`$. There is no joint state and no joint distribution of the two outcomes. It is therefore **not a comparison of two events of one schedule**, and it does not use the order of $`\lambda`$ within one evolution (A8, third bullet). It relies on two elements of the setting: the value of $`\lambda`$ at which a reading is applied, counted from the start in both runs (A8, second bullet), and the use of one contract $`C`$ in both runs, which fixes the unit of $`\lambda`$ across the runs. Equivalences act on it run by run, because each run is a start with a schedule.

**The clock reading.** The reading of the clock label is not a reading of one class. For one event its statistics is $`p_\lambda(a)=\sum_x\lVert\Pi_{x,a}e^{-iC\lambda}\Psi_0\rVert^2`$ with the place projectors $`\Pi_{x,a}=P_x\otimes\mathbb 1_2\otimes\lvert a\rangle\langle a\rvert`$ of the classes $`x`$, and by (5.2)(I) each term equals $`\lVert\Pi_{x,a}e^{-iC'a_x\lambda}\Psi_0\rVert^2`$ in every equivalence, whether the medium is read or not. The rates $`r_W`$ of (3.36), (3.23) are functionals of $`\lambda\mapsto p_\lambda`$.
- **(a) $`\tau>0`$: yes.** All $`a_x=a_b`$, so $`p^{C}_\lambda=p^{C'}_{a_b\lambda}`$ for every start, and both runs have $`r'_W=r_W/a_b`$.
- **(b) $`\tau=0`$: no.** $`P_x`$ commutes with $`C`$, a start in the block $`x_i`$ stays there, and $`p^{C}_\lambda=p^{C'}_{a_{x_i}\lambda}`$: equal $`\lambda`$ in the two runs under $`C`$ is $`a_{x_1}\lambda`$ and $`a_{x_2}\lambda`$ under $`C'`$.

```math
\text{(a):}\ \ \frac{r'_W(x_1)}{r'_W(x_2)}=\frac{r_W(x_1)}{r_W(x_2)}\ \text{ for every }W,\quad\frac{\eta'_{x_1}}{\eta'_{x_2}}=\frac{\eta_{x_1}}{\eta_{x_2}};\qquad\text{(b):}\ \ \frac{\eta'_{x_1}}{\eta'_{x_2}}=\frac{\eta_{x_1}}{\eta_{x_2}}\cdot\frac{a_{x_2}}{a_{x_1}}\ \ (\text{any positive number; }1\text{ for (5.13)}).
\qquad\text{(5.17)}
```

The parameter forms follow from (5.14), (5.15). In (a) the wide-start ratio of (3.24) is the same in every equivalent description, although it is not a statistic of one schedule; in (b) it is a property of the chosen description only.

### Step 10. Two bodies and a common medium (item 3)

Assumption of the item (M8): $`C=C_1+C_2+\kappa_1\hat x_1\otimes X+\kappa_2\hat x_2\otimes X`$, three objects, each one class; $`\hat x_i`$ is diagonal in the places of $`b_i`$. Now $`n=3`$ and A5 is a real condition. Put $`F_i:=C_i+\kappa_i\hat x_i\otimes X`$ (a pair term between $`b_i`$ and $`c`$) and $`J_i:=[C_i,\hat x_i]`$ ($`J_i\neq0`$ iff $`C_i`$ has an entry between places with different position labels). The entries of $`C`$ are $`C^{\langle i\rangle}=C_i^{\rm off}`$, touching $`b_i`$ only, and $`C^{\langle c\rangle}=(\kappa_1\hat x_1+\kappa_2\hat x_2)\otimes X^{\rm off}`$, touching $`c`$ only; (E1) holds for every grouping. Further

```math
[C^{\langle1\rangle},C^{\langle2\rangle}]=0,\qquad[C^{\langle i\rangle},C^{\langle c\rangle}]=\kappa_i\,J_i\otimes X^{\rm off},\qquad[F_1,F_2]=\kappa_1\kappa_2\,\hat x_1\hat x_2\otimes[X,X]=0\ \text{ for every }X .
\qquad\text{(5.18)}
```

**(a) All three read.** By (E2) and (5.18), $`a_i\neq a_c`$ requires $`J_i\otimes X^{\rm off}=0`$. In each remaining case (5.8) gives an equivalence and (5.5) the complete set; $`\Delta`$ is real diagonal with $`[C,\Delta]=0`$ and $`\Delta\in\mathcal S`$:

```math
\begin{array}{l|l|l}
\text{case} & \text{factors} & C'\\\hline
X\text{ diagonal} & a_1,a_2,a_c\ \text{free} & F_1/a_1+F_2/a_2+\Delta\\
X\text{ not diagonal},\ J_1\neq0,\ J_2\neq0 & a_1=a_2=a_c=\alpha & C/\alpha+\Delta\\
X\text{ not diagonal},\ J_1=0,\ J_2\neq0 & a_2=a_c,\ a_1\ \text{free} & C_1/a_1+(C-C_1)/a_c+\Delta\\
X\text{ not diagonal},\ J_1\neq0,\ J_2=0 & a_1=a_c,\ a_2\ \text{free} & C_2/a_2+(C-C_2)/a_c+\Delta\\
X\text{ not diagonal},\ J_1=J_2=0 & a_1,a_2,a_c\ \text{free} & C_1/a_1+C_2/a_2+(\kappa_1\hat x_1+\kappa_2\hat x_2)\otimes X/a_c+\Delta
\end{array}
\qquad\text{(5.19)}
```

Hypotheses of (5.8) in the rows: row 1, $`F_1\in\mathcal A_{b_2}\cap\mathcal A_c`$, $`F_2\in\mathcal A_{b_1}\cap\mathcal A_c`$ and (5.18); row 3, $`[C_1,C-C_1]=\kappa_1J_1\otimes X=0`$, $`C_1\in\mathcal A_{b_2}\cap\mathcal A_c`$, $`C-C_1\in\mathcal A_{b_1}`$; row 5, three commuting terms. Every $`C'`$ is self-adjoint, independent of $`\lambda`$ and a sum of pair terms between a body and the medium (a single-object term $`C_i/a_i`$ is included in one of them, A5). So (E4) removes no assignment of factors here; it restricts $`\Delta`$. **The relative factor of the two bodies is detectable iff $`X`$ is not diagonal in the places of the medium and $`J_1\neq0`$ and $`J_2\neq0`$.** Both directions: if all three hold, (E2) forces $`a_1=a_c=a_2`$; if one fails, rows 1, 3, 4, 5 give equivalences with $`a_1\neq a_2`$.

**(b) The medium is not read.** By (5.18) and (5.8) with the groups $`\{b_1\}`$, $`\{b_2\}`$ ($`F_1\in\mathcal A_{b_2}`$, $`F_2\in\mathcal A_{b_1}`$; nothing is required for the class $`c`$, which is not read):

```math
\Bigl(a_1,\ a_2;\ \ C'=\frac{C_1}{a_1}+\frac{C_2}{a_2}+\frac{\kappa_1}{a_1}\hat x_1\otimes X+\frac{\kappa_2}{a_2}\hat x_2\otimes X\Bigr)\ \text{is an equivalence for all }a_1,a_2>0,\ \text{for every }C_1,C_2,\ \kappa_1,\kappa_2>0\ \text{and }X .
\qquad\text{(5.20)}
```

So **an equivalence with $`a_1\neq a_2`$ always exists**; the relative factor of the two bodies is not detectable when the medium is not read. $`C'`$ is self-adjoint, independent of $`\lambda`$, a sum of the two pair terms $`F_i/a_i`$, and again of the form of the item, with $`C'_i=C_i/a_i`$, $`\kappa'_i=\kappa_i/a_i`$ and the same $`X`$. The control is row 2 of (5.19).

**(c) Two clocks.** Each body is one class, so the reading of the clock label of $`b_i`$ is a reading of the class $`b_i`$. For the schedule with the events $`(b_1,\text{clock},\lambda_1)`$, $`(b_2,\text{clock},\lambda_2)`$, outcomes $`j_1,j_2`$, every start and the equivalence (5.20):

```math
P_C(j_1,j_2;\lambda_1,\lambda_2)=P_{C'}(j_1,j_2;a_1\lambda_1,a_2\lambda_2):\qquad(\lambda_1,\lambda_2)\mapsto(a_1\lambda_1,a_2\lambda_2),\qquad C_i\mapsto\frac{C_i}{a_i},\quad\kappa_i\mapsto\frac{\kappa_i}{a_i} .
\qquad\text{(5.21)}
```

Every parameter that enters $`C_i`$ linearly (for a body of the class $`\mathcal C`$: $`\tau\zeta_x`$, $`m_x`$, $`V_x`$, $`\eta_x/\lambda_0`$) and $`\kappa_i`$ are divided by $`a_i`$; the tick of the clock of $`b_i`$ and every value of $`\lambda`$ at which $`b_i`$ is read are multiplied by $`a_i`$; ratios of two such parameters of one body do not change.
- *Pairing at equal $`\lambda`$.* The pairs $`(\lambda,\lambda)`$ of $`C`$ are the pairs $`(a_1\lambda,a_2\lambda)`$ of $`C'`$, and the pairs $`(\lambda',\lambda')`$ of $`C'`$ are the pairs $`(\lambda'/a_1,\lambda'/a_2)`$ of $`C`$. The rates with respect to $`\lambda`$ become $`r_i/a_i`$, so a comparison that pairs the readings at equal $`\lambda`$ gives the ratio $`r_1/r_2`$ in $`C`$ and $`(r_1/r_2)(a_2/a_1)`$ in $`C'`$: every positive number occurs in some equivalent description. With the medium not read, this ratio is not a function of the statistics of schedules; it relies on the order of $`\lambda`$ across the two objects (A8) and on the description chosen in the class of equivalent ones. It is the same in every equivalent description exactly in row 2 of (5.19).
- *Equal parameters of two types.* If the two types have equal parameters in $`C`$, they have parameters in the ratio $`a_2/a_1`$ in $`C'`$. With the medium not read, the statistics of schedules cannot distinguish "equal" from "proportional by one common factor": preserved by (5.20) are the ratios within one type ($`m^{(i)}/\tau^{(i)}`$, $`\kappa_i/\tau^{(i)}`$, $`\tau^{(i)}\lambda_0^{(i)}`$, ...), and with them the statement that the parameters of one type are a common multiple of those of the other. A condition "equal parameters" (M7) then has content only relative to the pairing of $`\lambda`$. In row 2 of (5.19) every equivalence has one factor $`\alpha`$, and equality of two such parameters is preserved up to the terms $`\Delta`$.

## Result

Class of every result: all contracts, blocks, starts and schedules of the stated item; controls are named in Steps 7 and 10.
- **Item 1(a):** (5.2) exact operator form for any set of read classes; (5.3) commutator form: equivalence $`\iff`$ $`[C-a_\ell C',\Pi]=0`$ for all place projectors of all classes and $`[C,C']=0`$, when every class is read; necessary and sufficient parts separately otherwise. (G) is used only for $`[C,C']=0`$; A5 only as admissibility of $`C'`$, (E4).
- **Item 1(b):** (5.4) entry form (E1)–(E4); (5.6) conditions (T1)–(T3) for equal factors, for one object and for two objects.
- **Item 1(c):** (5.7) two values exist iff $`C`$ has a pair-term split along $`\mathcal G`$, with $`C'=F_{\mathcal G}/\alpha+F_{\bar{\mathcal G}}/\alpha'`$; (5.5) at equal factors $`C'=C/\alpha+D`$, $`D`$ real diagonal, a sum of pair terms, constant on the components of the transition graph; (5.8) sufficient form for several groups; (5.9) readings with one outcome per block.
- **Item 2:** (5.11) with hopping: one factor for all positions (medium read or not), medium tied iff $`X`$ is not diagonal; (5.12) without hopping: all factors free, nothing detectable; (5.13) yes, a flat clock profile within $`\mathcal C`$; (5.14)–(5.16) parameters and the table, under K1, K2.
- **Item 3:** (5.19) all equivalences and the criterion: detectable iff $`X`$ not diagonal, $`J_1\neq0`$, $`J_2\neq0`$; (5.20) yes, with the contract; (5.21) the transformation rule and the two statements.
- **Item 4:** (5.17): (a) yes, (b) no; the comparison of two runs is not a comparison of two events of one schedule and relies on $`\lambda`$ as part of the setting with one $`C`$ in both runs.

## Consistency checks

1. **Two objects, each one class, against 10-global-order.** The pairs touching both classes are the transitions of kind (12), and $`C^{\langle1\rangle}=C^{(1)}+C^{(12)}`$. Then (5.3) is (10.14); (E1), (E3) give (10.13); (5.5) is (10.15); (T1) and (T3) are the two conditions of (10.16); (5.7) is (10.5), (10.6); (5.8) with $`F_i=C_i`$ is (10.7). Units: the $`a_\ell`$ are numbers, and every formula for $`C'`$ is of degree $`1`$ in $`C`$ and $`-1`$ in the factors, so $`C'a_\ell\lambda`$ is a pure number like $`C\lambda`$. Passed.
2. **Chain of two positions $`x\in\{0,1\}`$, clock with $`N=2`$, medium with two places** (Steps 6–8 do not use the shape of the chain). $`D=\frac{\pi}{2\lambda_0}\bigl(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\bigr)`$, so $`D_{01}\neq0`$ as in Step 6. *With hopping,* $`\theta:=\tau\zeta_0>0`$: from a start in the block $`0`$, $`p(\text{in block }1)=(\theta\lambda/2)^2+O(\lambda^3)`$. For a contract whose hopping entry is $`\theta/(2a_h)`$, the reading of the block $`1`$ at $`a_1\lambda`$ gives $`(\theta a_1\lambda/2a_h)^2`$ and the reading "not in the block $`0`$" at $`a_0\lambda`$ gives $`(\theta a_0\lambda/2a_h)^2`$: equality forces $`a_0=a_1=a_h`$, as (T1). On a clock level $`k`$, the component $`\Sigma=+1`$ ($`\lvert0,1\rangle,\lvert1,2\rangle`$) has the block $`\bigl(\begin{smallmatrix}V_0+M_{0,k}&i\theta/2\\-i\theta/2&V_1-M_{1,k}\end{smallmatrix}\bigr)`$ and $`\Sigma=-1`$ ($`\lvert0,2\rangle,\lvert1,1\rangle`$) has $`\bigl(\begin{smallmatrix}V_0-M_{0,k}&i\theta/2\\-i\theta/2&V_1+M_{1,k}\end{smallmatrix}\bigr)`$; adding $`\pm y_1`$ to them is $`m_0\to m_0+y_1`$, $`m_1\to m_1-y_1`$, as (5.14). With $`X=\sigma_1`$, $`[A_\zeta,\hat x]\otimes X\neq0`$ and $`a_c=a_b`$; with $`X=\sigma_3`$ the place projectors of $`c`$ commute with $`C`$ and $`a_c`$ is free, as (5.11). *Without hopping:* from $`\lvert x,s\rangle\otimes\lvert a=0\rangle`$, $`p_\lambda(a=1)=\sin^2\bigl(\pi\eta_x\lambda/2\lambda_0\bigr)`$, independent of $`m_x,V_x,\kappa,X`$; under (5.12) at $`a_x\lambda`$ it is $`\sin^2\bigl(\pi(\eta_x/a_x)(a_x\lambda)/2\lambda_0\bigr)`$, the same. The two-run ratio at equal $`\lambda`$ is $`\eta_0/\eta_1`$ under $`C`$ and $`1`$ under (5.13), as (5.17)(b). Passed.
3. **$`C`$ diagonal in the joint places.** There are no off-diagonal entries, so (E1)–(E3) hold for every grouping and every real diagonal $`C'\in\mathcal S`$, and a non-diagonal $`C'`$ violates (i). Directly: every place projector commutes with $`C`$ and $`C'`$, the statistics of every schedule does not depend on any $`\lambda_j`$, and no relative factor is detectable. Passed.

## Open issues

- When some classes are not read, the exact set of equivalences lies between (N) and (S) of (5.3); (5.2) is exact but is not reduced to commutators. This leaves open the complete list of contracts in item 2(a) with the medium not read; the detectability answers do not depend on it.
- (T1)–(T3) are sufficient, not necessary. The exact criterion is the absence of a separating grouping in (5.4). For three or more objects the A5 condition (E4), (S4) on the diagonal part is not reduced to a condition on entries.
- For several groups, (5.8) is proven as sufficient only; whether every equivalence with three or more distinct factors comes from such a sum is not decided.
- Item 4(b) is shown for starts inside one block. For a start spread over several positions at $`\tau=0`$, the clock reading at one $`\lambda`$ is not mapped to a clock reading at one value of the parameter in the equivalent description.
- The answers of item 2(c) depend on the conventions K1, K2 as stated in (5.16).
- Out of scope and not treated: re-timings that are not linear in $`\lambda`$, instances of one type, readings not local to one object, comparison by transport or by a signal.

## Methods used

- Evolved projectors for sequences of readings (Heisenberg form of (10.1))
- Power series in $`\lambda`$ and analyticity; Jacobi identity
- Commutants of place projectors; entrywise analysis of operators in the place basis
- Commuting splits of the contract; connected components of the transition graph
- Linear independence and partial trace for reading parameters off an operator

