# Re-timings of classes of places: detectable relative factors of clock rates

- **Subproject:** 05-ilang-free-fall
- **Package:** 05-rate-comparison
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-10

## Changes from previous version

Local regeneration after the external round 2 (verification.r2.md, issues I1, I2, I3). All tags (5.1)–(5.25) are kept. Only (5.17) changes its content: (a) gets a condition of existence, and the last part of (b) is restated. Every passage that differs from v2 is listed here; all other text is that of v2.

- **Header, this section and "Response to verification":** version v3; the two sections are rewritten for this round.
- **Step 5, last sentence** (same kind of statement as I1). "Preserved by all equivalences only if ..." is now stated as a property of the events of a schedule, and a sentence is added: it is not a statement about an equality of statistics.
- **Step 9(a), "Rates from the two runs (exact)"** (I3). Added: the transformation of the rate holds where the rate exists, and the ratio is carried into itself wherever it is defined (both rates exist, $`r^{(2)}\neq0`$); a rule with (R) need not give such rates.
- **Step 9(b), "Rates from the two runs, wide starts (exact)", the sentences before the three statements** (I1). "Only if $`a_x`$ is constant on the support of the start" is replaced. Constancy of $`a_x`$ is necessary and sufficient for the mapping of the events to give one value of the parameter of $`C`$; for the clock statistics of one start it is sufficient, not necessary. The example of the verifier is given.
- **Step 9(b), statement 1** (I3). "The ratio of the two rates is exactly $`1`$" is replaced by: equal advances and equal rates for every rule, and the ratio $`1`$ wherever this common rate exists and is not zero; the dial and the rule $`\Theta\equiv0`$ are named.
- **Step 9(b), "Not proven", second sentence from the end** (I3). "Statement 1 holds for every rule" is replaced accordingly.
- **(5.17), tag kept** (I3). (a): "wherever the right side is defined" is added. (b): "under (5.13), for every rule: $`1`$" is replaced by a third line: equal rates for every rule, ratio $`1`$ wherever the common rate exists and is not zero.
- **Step 10(c), "Rates, arbitrary body contracts and starts", one sentence** (same kind of statement as I1). "Is not ... unless the rates are constant" is replaced by a sufficient condition.
- **Step 10(c), "Equal parameters of two types"** (I2). The first sentence now says which parameters get the ratio $`a_2/a_1`$; the list of preserved ratios is written in the form that needs no convention; a sentence states the normalization under which $`\tau^{(i)}\lambda_0^{(i)}`$ is preserved, and what happens under K2.
- **Result:** item 4 (I3) and the last sentence of item 3 (I2).
- **Consistency check 2:** the condition $`\eta_0\neq\eta_1`$, the rate of the dial in the flat description, and the example of I1 are added.
- **JSON twin:** the statements of (5.9) ("its events"), (5.17), (5.21), (5.25), check 2 and the response to the verification.

## Response to verification

- **I1:** Accepted and fixed in Step 9(b), "Rates from the two runs, wide starts (exact)". The same kind of statement is brought in line in Step 5 (last sentence) and in Step 10(c) ("Rates, arbitrary body contracts and starts"); check 2 contains the example.
- **I2:** Accepted and fixed in Step 10(c), "Equal parameters of two types", and in Result, item 3.
- **I3:** Accepted and fixed in Step 9(b), statement 1 and "Not proven", in (5.17), in Step 9(a), "Rates from the two runs (exact)", and in Result, item 4.

## Setup and assumptions

- **Setting** (question.md, "Goal"): objects $`o=1,\dots,n`$ of pairwise different types, $`\mathcal H=\bigotimes_o\mathcal H_o`$; $`C`$ self-adjoint, independent of $`\lambda`$, a sum of pair terms (A5); a start $`\Psi_0`$ at $`\lambda=0`$, only $`\lambda\ge0`$; classes $`\ell`$ with object $`o(\ell)`$ and block $`B_\ell`$; readings of a class, schedules, re-timings $`((a_\ell),C')`$ and equivalences as defined there. $`\mathcal R`$ is the set of read classes. "Detectable" is used only in the sense of the question: every equivalence of $`C`$ has $`a_\ell=a_{\ell'}`$.
- **Inputs.** From 04-ilang-time/10-global-order@v2: the statistics (10.1) of a schedule, $`P(s_1,\dots,s_K)=\lVert\Pi^{(K)}_{s_K}(\lambda_K)\cdots\Pi^{(1)}_{s_1}(\lambda_1)\Psi_0\rVert^2`$ with $`\lambda_1\le\dots\le\lambda_K`$ and $`Y(\lambda)=e^{iC\lambda}Ye^{-iC\lambda}`$. Its results for two parts, (10.5), (10.6), (10.7), (10.13)–(10.16), are not used as inputs: their analogues for classes are derived in Steps 1–4 and compared with them in check 1. From 03-clock-and-fall@v3: the class $`\mathcal C`$ and its notation, and (3.23), (3.24), (3.36), used only in Step 9.
- **Notation.** $`K=(h_1,\dots,h_n)`$ is a joint place, $`Y_{KK'}=\langle K\vert Y\vert K'\rangle`$, $`Y^{\rm d}`$ the diagonal part and $`Y^{\rm off}=Y-Y^{\rm d}`$. A pair $`K\neq K'`$ **touches** the class $`\ell`$ if, for $`o=o(\ell)`$, $`h_o\neq h'_o`$ and at least one of $`h_o,h'_o`$ lies in $`B_\ell`$. Every pair $`K\neq K'`$ touches at least one class. $`C^{\langle\ell\rangle}`$ is the part of $`C`$ on the pairs that touch $`\ell`$. $`\mathcal A_\ell`$ is the algebra of the operators that commute with all place projectors of $`\ell`$. The **transition graph** of $`C`$ has the joint places as vertices and an edge $`K - K'`$ whenever $`C_{KK'}\neq0`$, $`K\ne K'`$. For the evolved projectors under the two contracts, $`\Pi^{C}(\lambda)=e^{iC\lambda}\Pi e^{-iC\lambda}`$ and $`\Pi^{C'}(\lambda)=e^{iC'\lambda}\Pi e^{-iC'\lambda}`$.
- **M6.** Every condition below refers to the operator $`C`$, to the place basis (A2) and to the blocks. "Sum of pair terms" means membership in the real linear space $`\mathcal S`$ of such operators, not a property of a list. Restricting an operator of $`\mathcal S`$ entrywise to the diagonal, or to the pairs $`(K,K')`$ that touch classes of a given set only, gives an operator of $`\mathcal S`$: for a pair term on the objects $`(a,b)`$ the entries vanish unless $`h_o=h'_o`$ for $`o\neq a,b`$, so the restriction depends on $`(h_a,h'_a,h_b,h'_b)`$ only and is again a pair term on $`(a,b)`$. Rates (Step 9) are defined from reading statistics only.
- **Approximations.** Everything derived in this package is exact for finitely many places (A1). The quoted (3.23), (3.24), (3.36) carry the orders stated in Step 9 ("Orders"); they are used only to name the number that the two runs give in the description $`C`$. Contracts studied in Steps 6–10 are assumptions of the items (M8).
- **Assumption R** (Step 9): the mean advance $`\vartheta_W`$ of (3.36), quoted as "the mean advance of the clock distribution", is obtained from the clock statistics by a rule with the property (R) of Step 9. The rule itself is not quoted.

## Derivation

### Step 1. Place projectors and touching

For $`S\subseteq B_\ell`$, $`o=o(\ell)`$, and any operator $`Y`$,

```math
\langle K\vert[Y,\Pi_S]\vert K'\rangle=Y_{KK'}\bigl(1_S(h'_o)-1_S(h_o)\bigr),\qquad\text{hence}\qquad Y\in\mathcal A_\ell\iff Y_{KK'}=0\ \text{on every pair that touches }\ell .
\qquad\text{(5.1)}
```

Proof of the equivalence: if the pair touches $`\ell`$ with, say, $`h_o\in B_\ell`$, take $`S=\{h_o\}`$; the bracket is $`-1`$. If it does not touch $`\ell`$, then $`h_o=h'_o`$ or both lie outside $`B_\ell`$, and the bracket is $`0`$ for every $`S\subseteq B_\ell`$. The class projectors of a reading of $`\ell`$ are projectors $`\Pi_S`$ and $`\mathbb 1-\Pi_{B_\ell}`$; every $`\Pi_S`$ occurs in some reading.

**(G)** The blocks of an object cover its places, so every $`\lvert h\rangle\langle h\rvert`$ is a place projector of a class, and $`\lvert K\rangle\langle K\rvert=\prod_o\lvert h_o\rangle\langle h_o\rvert`$. If every class is read, the place projectors of the read classes generate all operators that are diagonal in the joint places. If some classes are not read, (G) is not guaranteed, and it is not assumed below. Exactly: on $`\mathcal H_o`$ the place projectors of the read classes of $`o`$, together with $`\mathbb 1`$, generate the diagonal operators that are constant on the places outside the read blocks. So (G) holds for the read classes iff every object has at most one place outside its read blocks; the projector of that place is $`\mathbb 1`$ minus the others.

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

**Hypotheses.** (G) is used in one place only: (ii') $`\Rightarrow`$ (ii), and that step also needs (i) on every pair $`K\neq K'`$. A5 for $`C'`$ is used in no implication of (5.2), (5.3); it is the admissibility condition in the definition of a re-timing and must be imposed on the solution $`C'`$ (condition (E4) below). For $`n=2`$ every self-adjoint operator is one pair term and A5 is empty. If some classes are not read but (G) holds for the read classes (Step 1), every pair $`K\neq K'`$ touches a read class (of two different places of an object at least one lies in a read block), the proof above applies with "class" replaced by "read class", and an equivalence is the same as (i) for every read class together with (ii). If (G) does not hold for the read classes, what is proven is (5.2), (N) and (S); between (N) and (S) a gap remains in general.

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

So the outcome strings with nonzero probability correspond one to one to the blocks, with probability $`\lVert Q_i\Psi\rVert^2`$ and state $`Q_i\Psi/\lVert Q_i\Psi\rVert`$ after the readings: the same as for the reading with one outcome per block, by (1.3). A re-timing moves the reading of the block $`i`$ to $`a_i\lambda`$. If the factors of the blocks are equal, the readings stay at one value of the parameter. If they differ, the re-timed schedule contains $`q`$ yes/no readings at up to $`q`$ different values; in an equivalence its statistics is unchanged by definition (by (5.2) the evolved projectors are the same operators and commute), but in the re-timed description it is not a reading of the object at one value of $`\lambda`$. "Reading the block label at one $`\lambda`$", as a property of the events of a schedule, is therefore preserved by all equivalences only if all relative factors of the blocks are detectable. This concerns the mapping of the events, not the statistics: the statistics of the $`q`$ readings at different values can still be that of a reading at one value under $`C'`$ (Step 7(b), where the $`Q_i`$ commute with $`C'`$).

### Step 6. One body on a chain: the entries of $`C`$ (item 2)

Assumption of the item (M8): $`C=C_b\otimes\mathbb 1_c+\kappa\,\hat x\otimes X`$ with $`C_b\in\mathcal C`$ on the chain $`\lvert x\rvert\le L`$, $`L\ge1`$; the medium has no contract of its own. There are two objects, so every self-adjoint operator on $`\mathcal H_b\otimes\mathcal H_c`$ is one pair term: $`\mathcal S`$ is everything, and (E4), (S4) are empty. Every contract constructed in Steps 6–9 is self-adjoint, independent of $`\lambda`$ and a pair term between $`b`$ and $`c`$. From here on the diagonal term of (5.5) is written $`\Delta`$, because $`D`$ is the clock operator of the class $`\mathcal C`$. Joint places are $`(x,s,a;r)`$ with $`r\in H_c`$. The entries of $`C`$ are:
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

So $`\eta_x/\eta_y`$ and the tick parameter $`t_x:=\lambda_0/\eta_x`$ are properties of $`C`$ alone, as are $`m_xt_x`$ and $`\tau\zeta_xt_x`$; $`m_x/\eta_x`$ and $`\tau\zeta_x/\eta_x`$ need K2; $`(V_x-V_y)/\eta_x`$ needs K1 and K2.

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

Additions. In (a), $`m_x/\eta_x`$ is the same exactly for the equivalences with $`y_1=0`$; what is the same for every equivalence is $`(m_x+m_y)/\eta_z`$ for $`x-y`$ odd and $`(m_x-m_y)/\eta_z`$ for $`x-y`$ even. With another K2 (for example $`\eta'_{x_*}=\eta_{x_*}`$ at a reference position, so $`\lambda'_0=a_b\lambda_0`$) the entries "same" of rows 2–4 in (a) become "multiplied by $`1/a_b`$"; free of K2 are the products with the tick, $`\tau\zeta_xt_x`$ and $`(V_x-V_y)t_x`$. Without a common K1, row 4 in (a) fails by $`-a_b\beta(x-y)/\eta_x`$. The table is about the parameters of the contracts; rates taken from readings are the subject of Step 9.

### Step 9. Rates from the reading statistics; two runs (item 4)

In Steps 9 and 10 the clock label is written $`j\in\mathbb Z_N`$, to keep it apart from the factors $`a_x`$.

**Rate (definition, for Steps 9 and 10).** For a body with a clock label, a contract $`C`$ and a start $`\Psi_0`$, let $`\Pi_j`$ be the projector onto the places of the body with clock label $`j`$, and $`D`$ the clock operator of Model D:

```math
p_\lambda(j):=\bigl\lVert\Pi_j\,e^{-iC\lambda}\Psi_0\bigr\rVert^2,\qquad
\pi_u(j):=\bigl\lvert\langle j\vert e^{-iDu\lambda_0}\vert0\rangle\bigr\rvert^2=\frac{\sin^2\pi(j-u)}{N^2\sin^2\bigl(\pi(j-u)/N\bigr)},\qquad
\text{uniform clock, rate }r>0\text{ on }[0,\Lambda]:\ \ p_\lambda=\pi_{r\lambda}\ \ (0\le\lambda\le\Lambda,\ r\Lambda\le1).
\qquad\text{(5.22)}
```

- $`p_\lambda`$ is the statistics of the single reading of the clock label at $`\lambda`$ (the **clock statistics**). It depends on $`C`$, on the start and on $`\lambda`$.
- $`\pi_u`$ (the **dial**) follows from $`\lvert f_k\rangle`$ and $`d_k`$; it depends on $`N`$ and $`u`$ only, $`\pi_u(j)=1`$ for $`j-u\in N\mathbb Z`$, and $`u\mapsto\pi_u`$ is injective on $`0\le u\le1`$ because $`\pi_u(0)`$ decreases strictly from $`1`$ to $`0`$ there ($`t\cot t`$ is decreasing on $`(0,\pi)`$).
- For a **uniform clock** the advance $`\vartheta(\lambda)=r\lambda`$ is read from $`p_\lambda`$ by the dial, and the rate $`r`$ is a number: it does not depend on $`\lambda`$ on the range. Whether a contract gives a uniform clock depends on the start.
- In general an **advance** is a function $`\vartheta(\lambda)=\Theta\bigl[(p_\mu)_{0\le\mu\le\lambda}\bigr]`$ with a rule $`\Theta`$ that has the property **(R)**: the family $`\mu\mapsto p_{\mu/\alpha}`$ on $`[0,\alpha\lambda]`$ gets the same value as $`\mu\mapsto p_\mu`$ on $`[0,\lambda]`$, for every $`\alpha>0`$. A function of $`p_\lambda`$ alone has (R); the dial reading is one. The **rate** is $`r(\lambda;\Psi_0,C):=\mathrm d\vartheta/\mathrm d\lambda`$ where the derivative exists. It depends on the start and on $`\lambda`$, and it is a number only for the starts and on the ranges of $`\lambda`$ on which it is constant.

**Transformation.** For one start, two contracts and a number $`\alpha>0`$:

```math
p^{C'}_{\alpha\lambda}=p^{C}_\lambda\ \ \forall\lambda\ge0\quad\Longrightarrow\quad\vartheta^{C'}(\lambda')=\vartheta^{C}\Bigl(\frac{\lambda'}\alpha\Bigr),\qquad r^{C'}(\lambda')=\frac1\alpha\,r^{C}\Bigl(\frac{\lambda'}\alpha\Bigr);\qquad\text{uniform, rate }r\text{ on }[0,\Lambda]\ \longmapsto\ \text{uniform, rate }\frac r\alpha\text{ on }[0,\alpha\Lambda].
\qquad\text{(5.23)}
```

Proof: the family of $`C'`$ is $`\mu\mapsto p^{C}_{\mu/\alpha}`$, so (R) gives the first equation and the chain rule the second; for a uniform clock $`p^{C'}_{\lambda'}=\pi_{(r/\alpha)\lambda'}`$ on $`0\le\lambda'\le\alpha\Lambda`$. (5.23) is exact, for every contract and every start for which the hypothesis holds.

**What the comparison is (A8).** Two runs are two applications of one description (the same objects and the same $`C`$) with two starts, $`S_{\rm clock}(x_1)\otimes\chi`$ and $`S_{\rm clock}(x_2)\otimes\chi`$ ($`\chi`$ any unit vector of $`\mathcal H_c`$; the results below hold for every $`\chi`$), each with its own schedule of one event: the reading of the clock label at $`\lambda`$. There is no joint state and no joint distribution of the two outcomes, so it is **not a comparison of two events of one schedule**. It relies on A8 in two ways. The value of $`\lambda`$ at which each reading is applied is part of the setting and is not a time; here it is counted from the start of each run, with one contract $`C`$ in both runs. And the comparison pairs readings taken at equal $`\lambda`$ in the two runs: by A8, "a comparison of readings taken at equal $`\lambda`$ uses the order of $`\lambda`$", and a package that relies on it says so. This comparison relies on it. Equivalences act on it run by run, because each run is a start with a schedule.

**The clock reading and the classes.** The reading of the clock label is not a reading of one class. With the place projectors $`\Pi_{x,j}=P_x\otimes\mathbb 1_2\otimes\lvert j\rangle\langle j\rvert`$ of the classes $`x`$, for every start and every equivalence (medium read or not), by (5.2)(I):

```math
\begin{aligned}
&q_\lambda(x,j):=\bigl\lVert\Pi_{x,j}e^{-iC\lambda}\Psi_0\bigr\rVert^2,\qquad p_\lambda(j)=\sum_xq_\lambda(x,j),\qquad q^{C}_\lambda(x,j)=q^{C'}_{a_x\lambda}(x,j);\\
&\tau=0,\ \Psi_0=S_{\rm clock}(x_i)\otimes\chi:\qquad q^{C}_\lambda(x,j)=\phi^{(i)}_X(x)^2\,\pi_{\eta_x\lambda/\lambda_0}(j),\qquad p^{C'}_{\lambda'}(j)=\sum_x\phi^{(i)}_X(x)^2\,\pi_{\eta_x\lambda'/(a_x\lambda_0)}(j).
\end{aligned}
\qquad\text{(5.24)}
```

Here $`\phi^{(i)}_X(x)=c_W\,w((x-x_i)/W)`$, with $`\lvert x_i\rvert+W\le L`$. Proof of the second line: at $`\tau=0`$, $`P_x`$ commutes with $`C`$, and with $`\sigma_3\lvert1\rangle=\lvert1\rangle`$ the component at $`x`$ evolves into $`\phi^{(i)}_X(x)\,e^{-i(m_x+V_x)\lambda}\lvert x\rangle\lvert1\rangle\,e^{-i\eta_xD\lambda}\lvert0\rangle\otimes e^{-i\kappa xX\lambda}\chi`$, which gives $`q^{C}_\lambda`$; the formula for $`p^{C'}_{\lambda'}`$ then follows from the first line. The clock statistics of a wide start at $`\tau=0`$ is therefore a mixture, over the occupied positions, of uniform clocks with the rates $`\eta_x/\lambda_0`$; it does not depend on $`m_x`$, $`V_x`$, $`\kappa`$, $`X`$, $`\chi`$.

**(a) $`\tau>0`$, $`\zeta_x>0`$ on every bond: yes.**
- *Parameters (exact).* By (N)(i), every equivalence has $`C'=C/a_b+Z`$ with $`Z`$ diagonal in the places of the body, medium read or not. If $`C'`$ has the class form, its clock entries give $`\eta'_x/\lambda'_0=\eta_x/(a_b\lambda_0)`$ as in (5.14), so $`\eta'_{x_1}/\eta'_{x_2}=\eta_{x_1}/\eta_{x_2}`$.
- *Rates from the two runs (exact).* All $`a_x=a_b`$ (Step 7), so (5.24) gives $`p^{C}_\lambda=p^{C'}_{a_b\lambda}`$ for every start, the wide starts included. By (5.23), for every rule with (R), the rate of run $`i`$ obeys $`r'^{(i)}(\lambda')=r^{(i)}(\lambda'/a_b)/a_b`$ with the same $`a_b`$ in both runs, wherever $`r^{(i)}(\lambda'/a_b)`$ exists. Readings at equal $`\lambda`$ in the two runs under $`C`$ are readings at equal $`a_b\lambda`$ under $`C'`$, and the ratio of the two rates, as a function of the common value of the parameter, is carried into itself, (5.17)(a), wherever it is defined: where both rates exist and $`r^{(2)}\neq0`$. A rule with (R) need not give such rates (statement 1 of (b)). This holds for every $`W`$ and uses no approximation.
- *Consequence.* Under Assumption R the ratio $`r_W(x_1)/r_W(x_2)`$ of (3.24) is the same number in $`C`$ and in every equivalent description, for every $`W`$ and in the limit $`W\to\infty`$, to whatever order it is constant in $`\lambda`$. The contracts of (5.14) with the linear profiles of (3.24) are those with $`y_0=y_1=0`$; written with $`\eta'_0=1`$ (so $`\lambda'_0=a_b\lambda_0`$) they have $`\tau'=\tau/a_b`$, $`m'=m/a_b`$, $`\mathcal F'=\mathcal F/a_b+\beta`$ and the same $`g_m,g_\eta,g_\zeta`$, hence $`\varkappa'_i=\varkappa_i`$ and $`\varsigma'_W=\varsigma_W`$: every term of (3.24) is the same, in agreement with the exact statement.

**(b) $`\tau=0`$: no.**
- *Parameters (exact).* By (5.15), $`\eta'_{x_1}/\eta'_{x_2}=(\eta_{x_1}/\eta_{x_2})(a_{x_2}/a_{x_1})`$: every positive number occurs, by (5.12); it is $`1`$ for (5.13). This holds with the medium read or not.
- *Rates from the two runs, wide starts (exact).* By (5.24), a reading of the clock at one $`\lambda'`$ under $`C'`$ collects the contributions of the positions at the values $`\lambda'/a_x`$ of the parameter of $`C`$: $`p^{C'}_{\lambda'}(j)=\sum_xq^{C}_{\lambda'/a_x}(x,j)`$. For $`\lambda'>0`$ these are one value iff $`a_x`$ is constant on the support of the start. So the mapping of the events by the factors carries the reading into a clock reading at one $`\lambda`$ of $`C`$ iff $`a_x=\alpha`$ there, and then $`p^{C'}_{\lambda'}=p^{C}_{\lambda'/\alpha}`$. This is a statement about the mapping of the events, not about the clock statistics of one start: for $`p^{C'}_{\lambda'}`$ to be a clock statistics of $`C`$ at one $`\lambda`$, constancy of $`a_x`$ is sufficient, not necessary. Example: a start of the same form with equal weights on two positions, $`\eta_0=1`$, $`\eta_1=2`$, $`a_0=\tfrac12`$, $`a_1=2`$ gives $`p^{C'}_{\lambda'}=\tfrac12\pi_{2\lambda'/\lambda_0}+\tfrac12\pi_{\lambda'/\lambda_0}=p^{C}_{\lambda'}`$ although the factors differ. Nothing below uses the necessity. Three statements follow, for every $`W`$.
  1. *Uniform runs.* If $`\eta_x/a_x`$ has one value $`b_i`$ on the support of run $`i`$, then $`p^{C'}_{\lambda'}=\pi_{b_i\lambda'/\lambda_0}`$: run $`i`$ is a uniform clock with the rate $`b_i/\lambda_0`$ on $`[0,\lambda_0/b_i]`$. In the flat description (5.13), $`b_1=b_2=1`$: the two runs have the same clock statistics at every $`\lambda'`$, so every rule gives the same advance in both, and the same rate wherever it exists. The ratio of the two rates is exactly $`1`$ wherever this common rate exists and is not zero, for every $`W`$ and in the limit $`W\to\infty`$. For the dial the common rate is $`1/\lambda_0`$ on $`[0,\lambda_0]`$, and the ratio is $`1`$. The property (R) alone does not give a nonzero rate: the rule $`\Theta\equiv0`$ has (R) and gives two zero rates, whose ratio is not defined.
  2. *Position-resolved mean advance.* Let $`w_x(\lambda):=\sum_jq_\lambda(x,j)`$, let $`u_x(\lambda)\in[0,1]`$ be the dial value of $`q_\lambda(x,\cdot)/w_x`$, and $`\vartheta_{\rm pos}:=\sum_xw_xu_x`$, $`r_{\rm pos}:=\mathrm d\vartheta_{\rm pos}/\mathrm d\lambda`$. This rule reads the position and the clock label at one $`\lambda`$ (Step 5); it is the weighted mean of the advances of the components, the form that $`\vartheta_W`$ has in (3.36). With $`\mathsf E_i[f]:=\sum_x\phi^{(i)}_X(x)^2f_x`$, (5.24) gives $`r_{\rm pos}(x_i)=\mathsf E_i[\eta]/\lambda_0`$ under $`C`$ and $`r'_{\rm pos}(x_i)=\mathsf E_i[\eta/a]/\lambda_0`$ under $`C'`$, constant in the parameter while all $`u_x\le1`$. For the linear profile $`\mathsf E_i[\eta]=\eta_{x_i}+g_\eta W\bar\xi_W`$ with $`\bar\xi_W:=\sum_x\frac{x-x_i}W\phi^{(i)}_X(x)^2\in[-1,1]`$, the same in both runs; $`\bar\xi_W=0`$ for an even $`w`$, and then the ratio under $`C`$ is exactly $`\eta_{x_1}/\eta_{x_2}`$.
  3. *Every positive number.* For $`x_1\neq x_2`$ the supports of the two starts are translates of one finite set, so each contains a position outside the other. Put $`\eta_x/a_x=1`$ at such a position of run 1 and $`\varepsilon`$ elsewhere: the ratio $`\mathsf E_1[\eta/a]/\mathsf E_2[\eta/a]`$ tends to $`\infty`$ as $`\varepsilon\to0`$, and to $`0`$ with the runs exchanged; it is continuous on the connected set of positive profiles, so it takes every positive value.
- *Not proven.* The value that a rule using $`p_\lambda`$ alone assigns to a mixture in which $`\eta_x/a_x`$ varies over the support. Under $`C`$ it is the value of (3.24), to the orders below. The answer does not depend on it: by statement 1 the two rates are equal in the flat description for every rule, with the ratio $`1`$ for every rule whose rate there exists and is not zero (the dial is one), and by (5.15) with $`a_x=\eta_x`$, $`y_{1,x}=m-m_x/\eta_x`$, $`y_{0,x}=-V_x/\eta_x`$ there is an equivalent contract with $`\tau'=0`$, $`m'_x=m`$, $`\eta'_x=1`$, $`V'_x=0`$ and the same records, which has linear profiles with $`g'_m=g'_\eta=\mathcal F'=0`$, so that (3.24) applies to it and gives $`1`$.

```math
\begin{aligned}
&\text{(a)}\ \ \rho^{C'}(\lambda')=\rho^{C}\Bigl(\frac{\lambda'}{a_b}\Bigr),\quad\rho(\lambda):=\frac{r^{(1)}(\lambda)}{r^{(2)}(\lambda)},\quad\text{for every start and every rule with (R), wherever the right side is defined};\qquad\frac{\eta'_{x_1}}{\eta'_{x_2}}=\frac{\eta_{x_1}}{\eta_{x_2}};\\
&\text{(b)}\ \ \frac{\eta'_{x_1}}{\eta'_{x_2}}=\frac{\eta_{x_1}}{\eta_{x_2}}\cdot\frac{a_{x_2}}{a_{x_1}},\qquad\frac{r'_{\rm pos}(x_1)}{r'_{\rm pos}(x_2)}=\frac{\mathsf E_1[\eta/a]}{\mathsf E_2[\eta/a]}\quad\Bigl(\text{under }C:\ \frac{\mathsf E_1[\eta]}{\mathsf E_2[\eta]}\Bigr);\\
&\phantom{\text{(b)}\ \ }\text{under (5.13), for every rule: }r'^{(1)}=r'^{(2)}\ \text{wherever one of them exists, and }\frac{r'^{(1)}}{r'^{(2)}}=1\ \text{wherever this common rate exists and is not zero}.
\end{aligned}
\qquad\text{(5.17)}
```

**Orders.** The quoted formulas hold for the linear profiles of $`C_{\rm eff}`$ and carry: (3.36) the zeroth order in the gradients (the profiles enter through their values at $`x_0`$) and the first order in the level spacing; (3.23) and (3.24) in addition the limit $`W\to\infty`$, with the finite-$`W`$ corrections bounded by $`\delta_W^2\tau^{0\,2}/m_{x_0}^2`$ (relative, for the rate) and $`\delta_W^2\lvert\varkappa_1^2-\varkappa_2^2\rvert(1+\varkappa_2^2)`$ (for the ratio), $`\delta_W^2=O(W^{-2})`$. The statement "the two runs give $`\eta_{x_1}/\eta_{x_2}`$" holds to these orders. At $`\tau=0`$, $`\varsigma_W=0`$ and statement 2 shows the term that the zeroth order drops: $`g_\eta W\bar\xi_W`$. The transformations (5.14), (5.15), (5.23), (5.24) and (5.17) are exact.

**Summary of item 4.** In (a) the wide-start ratio of (3.24) is the same in every equivalent description, as a parameter ratio and as the ratio taken from the two runs, although it is not a statistic of one schedule. In (b) it is a property of the chosen description only.

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

This is exact, for arbitrary $`C_1`$, $`C_2`$ and every start. Every parameter that enters $`C_i`$ linearly (for a body of the class $`\mathcal C`$: $`\tau\zeta_x`$, $`m_x`$, $`V_x`$, $`\eta_x/\lambda_0`$) and $`\kappa_i`$ are divided by $`a_i`$; the tick parameter $`\lambda_0/\eta_x`$ of $`b_i`$ and every value of $`\lambda`$ at which $`b_i`$ is read are multiplied by $`a_i`$; ratios of two such parameters of one body do not change.

*Rates, arbitrary body contracts and starts.* Let $`p^{(i)}_\lambda`$ be the clock statistics (5.22) of $`b_i`$ (the statistics of (5.21) for one event) and $`r_i(\lambda;\Psi_0,C)`$ a rate of $`b_i`$ for a rule with (R). For every equivalence with the factors $`a_1,a_2`$ of the bodies, the medium read or not, (5.2)(I) gives $`p^{(i),C'}_{a_i\lambda}=p^{(i),C}_\lambda`$ for every start, and (5.23) gives

```math
r_i^{C'}(\lambda')=\frac1{a_i}\,r_i^{C}\Bigl(\frac{\lambda'}{a_i}\Bigr),\qquad\frac{r_1^{C'}(\lambda')}{r_2^{C'}(\lambda')}=\frac{a_2}{a_1}\cdot\frac{r_1^{C}(\lambda'/a_1)}{r_2^{C}(\lambda'/a_2)};\qquad\text{two uniform clocks, rates }r_1,r_2\text{ on }[0,\Lambda]:\ \ \frac{r'_1}{r'_2}=\frac{r_1}{r_2}\cdot\frac{a_2}{a_1}\ \text{ on }0<\lambda'\le\min(a_1,a_2)\Lambda,
\qquad\text{(5.25)}
```

wherever the rates exist and the denominators do not vanish. The pairs $`(\lambda,\lambda)`$ of $`C`$ are the pairs $`(a_1\lambda,a_2\lambda)`$ of $`C'`$, and the pairs $`(\lambda',\lambda')`$ of $`C'`$ are the pairs $`(\lambda'/a_1,\lambda'/a_2)`$ of $`C`$: a pairing at equal $`\lambda`$ is carried into a pairing at equal values of the parameter iff $`a_1=a_2`$, and then $`r_1^{C'}(\lambda')/r_2^{C'}(\lambda')=r_1^{C}(\lambda'/\alpha)/r_2^{C}(\lambda'/\alpha)`$ with $`\alpha=a_1=a_2`$. Nothing more holds in this generality. For $`a_1\neq a_2`$ the right side of (5.25) contains the rates of $`C`$ at the two different values $`\lambda'/a_1\neq\lambda'/a_2`$; it is $`a_2/a_1`$ times the ratio taken at equal $`\lambda`$ under $`C`$ if the rates are constant (sufficient, not necessary), and for rates that depend on $`\lambda`$ it need not be. And a rate need not exist: if $`C_i`$ is diagonal in the clock label, $`\Pi_j`$ commutes with $`C`$, $`p^{(i)}_\lambda`$ does not depend on $`\lambda`$, every advance is constant and no ratio is defined. So for arbitrary body contracts and starts neither "the ratio becomes $`(r_1/r_2)(a_2/a_1)`$" nor "every positive number occurs" holds.

*Two uniform clocks.* The class: contracts of the item together with a start for which both clocks are uniform, with rates $`r_1,r_2>0`$ on $`[0,\Lambda]`$. It has members for every $`\kappa_1,\kappa_2,X`$ and in every row of (5.19): the **uncoupled clocks** $`C_i=A_i\otimes\mathbb 1_{N_i}+\mathbb 1\otimes\eta_iD_i`$, with $`A_i`$ self-adjoint on the other labels of $`b_i`$, $`\eta_i>0`$ and $`D_i`$ the clock operator with $`N_i`$ and $`\lambda_{0,i}`$, and a start $`\chi\otimes\lvert0\rangle\otimes\lvert0\rangle`$ with the two clock labels in the place $`0`$ and $`\chi`$ any unit vector of the other labels and the medium. $`\eta_iD_i`$ commutes with the rest of $`C`$, so $`p^{(i)}_\lambda=\pi_{\eta_i\lambda/\lambda_{0,i}}`$: the rate is $`\eta_i/\lambda_{0,i}`$ on $`[0,\lambda_{0,i}/\eta_i]`$, and $`J_i=[A_i,\hat x_i]\otimes\mathbb 1`$ vanishes or not with the choice of $`A_i`$. The same contracts with a clock label started in a level $`\lvert f_k\rangle`$ give $`p^{(i)}_\lambda(j)=1/N_i`$ for all $`\lambda`$: no rate. For the class, by (5.25), the rates become $`r_i/a_i`$ and the ratio at equal values of the parameter becomes $`(r_1/r_2)(a_2/a_1)`$. Hence:
- *Medium not read.* By (5.20) every $`a_2/a_1>0`$ occurs, so the ratio of the two rates at equal $`\lambda`$ takes every positive value in the equivalent descriptions. It is not the same in them; it is fixed only together with the pairing of the two readings at equal $`\lambda`$, which uses the order of $`\lambda`$ (A8), and with the description chosen.
- *All three read.* The ratio is the same in every equivalent description iff every equivalence has $`a_1=a_2`$, that is, iff $`C`$ is in row 2 of (5.19). In row 2 both rates are divided by $`\alpha`$; in rows 1, 3, 4, 5 an equivalence with $`a_1\neq a_2`$ multiplies the ratio by $`a_2/a_1\neq1`$.

*Equal parameters of two types.* If the two types have equal parameters in $`C`$, then in $`C'`$ of (5.20) those that enter $`C_i`$ linearly, and $`\kappa_i`$, are in the ratio $`a_2/a_1`$, and the tick parameters in the ratio $`a_1/a_2`$. With the medium not read, the statistics of schedules cannot distinguish "equal" from "proportional by one common factor": preserved by (5.20) are the ratios of two such parameters within one type and their products with the tick parameter, which need no convention (for a body of the class $`\mathcal C`$: $`m^{(i)}_x/(\tau^{(i)}\zeta^{(i)}_y)`$, $`\kappa_i/(\tau^{(i)}\zeta^{(i)}_y)`$, $`\tau^{(i)}\zeta^{(i)}_y\lambda_0^{(i)}/\eta^{(i)}_x`$, ...), and with them the statement that the parameters of one type are a common multiple of those of the other. A product such as $`\tau^{(i)}\lambda_0^{(i)}`$ depends on the normalization in which the contract is written. It is preserved when the clock coefficient and the hopping profile are held fixed, $`\eta'_x=\eta_x`$ and $`\zeta'_x=\zeta_x`$, hence $`\lambda'^{(i)}_0=a_i\lambda^{(i)}_0`$ and $`\tau'^{(i)}=\tau^{(i)}/a_i`$; this is the case of Model D, where $`\eta_x=\zeta_x=1`$, and then $`m^{(i)}/\tau^{(i)}`$, $`\kappa_i/\tau^{(i)}`$ and $`\tau^{(i)}\lambda_0^{(i)}`$ are preserved. Under K2 of Step 8 with the same hopping profile ($`\lambda'_0=\lambda_0`$, $`\eta'_x=\eta_x/a_i`$, $`\zeta'_x=\zeta_x`$) the product $`\tau^{(i)}\lambda_0^{(i)}`$ is divided by $`a_i`$. A condition "equal parameters" (M7) then has content only relative to the pairing of $`\lambda`$. In row 2 of (5.19) every equivalence has one factor $`\alpha`$, and equality of two such parameters is preserved up to the terms $`\Delta`$.

## Result

Class of every result: all contracts, blocks, starts and schedules of the stated item, unless a narrower class is named. Controls are named in Steps 7 and 10.
- **Item 1(a):** (5.2) exact operator form for any set of read classes; (5.3) commutator form: equivalence $`\iff`$ $`[C-a_\ell C',\Pi]=0`$ for all place projectors of all classes and $`[C,C']=0`$, when every class is read, and also when (G) holds for the read classes (every object has at most one place outside its read blocks); necessary and sufficient parts separately otherwise. (G) is used only for $`[C,C']=0`$; A5 only as admissibility of $`C'`$, (E4).
- **Item 1(b):** (5.4) entry form (E1)–(E4); (5.6) conditions (T1)–(T3) for equal factors, for one object and for two objects.
- **Item 1(c):** (5.7) two values exist iff $`C`$ has a pair-term split along $`\mathcal G`$, with $`C'=F_{\mathcal G}/\alpha+F_{\bar{\mathcal G}}/\alpha'`$; (5.5) at equal factors $`C'=C/\alpha+D`$, $`D`$ real diagonal, a sum of pair terms, constant on the components of the transition graph; (5.8) sufficient form for several groups; (5.9) readings with one outcome per block.
- **Item 2:** (5.11) with hopping: one factor for all positions (medium read or not), medium tied iff $`X`$ is not diagonal; (5.12) without hopping: all factors free, nothing detectable; (5.13) yes, a flat clock profile within $`\mathcal C`$; (5.14)–(5.16) parameters and the table, under K1, K2.
- **Rates:** (5.22) clock statistics, dial, uniform clock, advance rule with (R), rate $`r(\lambda;\Psi_0,C)`$; (5.23) $`r^{C'}(\lambda')=r^{C}(\lambda'/\alpha)/\alpha`$, exact.
- **Item 4:** (5.24) exact statistics of the wide starts; (5.17): (a) yes, exactly, for every start, every $`W`$ and every rule with (R), wherever the ratio of the two rates is defined (both rates exist and the denominator is not zero), and for the parameter ratio; (b) no: the parameter ratio is multiplied by $`a_{x_2}/a_{x_1}`$; in the flat description (5.13) the two runs with the wide starts have the same clock statistics, hence equal advances and equal rates for every rule, and the ratio $`1`$ wherever this common rate exists and is not zero (for the dial it is $`1/\lambda_0`$); the position-resolved mean advance gives $`\mathsf E_1[\eta/a]/\mathsf E_2[\eta/a]`$, any positive number. The identification of the two-run ratio under $`C`$ with $`\eta_{x_1}/\eta_{x_2}`$ carries the orders of (3.23), (3.24), (3.36). The comparison of two runs is not a comparison of two events of one schedule; it pairs readings taken at equal $`\lambda`$, counted from the two starts with one $`C`$, and so uses the order of $`\lambda`$ (A8).
- **Item 3:** (5.19) all equivalences and the criterion: detectable iff $`X`$ not diagonal, $`J_1\neq0`$, $`J_2\neq0`$; (5.20) yes, with the contract; (5.21) the exact transformation rule, for arbitrary body contracts and every start; (5.25) the rates with their arguments. For two uniform clocks the ratio of the rates at equal $`\lambda`$ becomes $`(r_1/r_2)(a_2/a_1)`$: every positive number with the medium not read, and the same in every equivalent description iff row 2 of (5.19) with all three read. For arbitrary body contracts and starts only (5.21) and (5.25) hold. Equal parameters of two types that enter the body contracts linearly, and equal $`\kappa_i`$, become parameters in the ratio $`a_2/a_1`$ (tick parameters: $`a_1/a_2`$); preserved without a convention are the ratios of such parameters within one type and their products with the tick parameter, such as $`\tau\zeta_y\lambda_0/\eta_x`$, while $`\tau\lambda_0`$ depends on the normalization of the clock: it is preserved with the clock coefficient held fixed (Model D) and divided by $`a_i`$ under K2.

## Consistency checks

1. **Two objects, each one class, against 10-global-order.** The pairs touching both classes are the transitions of kind (12), and $`C^{\langle1\rangle}=C^{(1)}+C^{(12)}`$. Then (5.3) is (10.14); (E1), (E3) give (10.13); (5.5) is (10.15); (T1) and (T3) are the two conditions of (10.16); (5.7) is (10.5), (10.6); (5.8) with $`F_i=C_i`$ is (10.7). Units: the $`a_\ell`$ are numbers, and every formula for $`C'`$ is of degree $`1`$ in $`C`$ and $`-1`$ in the factors, so $`C'a_\ell\lambda`$ is a pure number like $`C\lambda`$; a rate has the unit of $`1/\lambda`$, and $`r^{C'}\lambda'=r^{C}\lambda`$ in (5.23). Passed.
2. **Chain of two positions $`x\in\{0,1\}`$, clock with $`N=2`$, medium with two places** (Steps 6–9 do not use the shape of the chain). $`D=\frac{\pi}{2\lambda_0}\bigl(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\bigr)`$, so $`D_{01}\neq0`$ as in Step 6, and the dial is $`\pi_u=(\cos^2\frac{\pi u}2,\sin^2\frac{\pi u}2)`$, injective on $`[0,1]`$ as in (5.22). *With hopping,* $`\theta:=\tau\zeta_0>0`$: from a start in the block $`0`$, $`p(\text{in block }1)=(\theta\lambda/2)^2+O(\lambda^3)`$. For a contract whose hopping entry is $`\theta/(2a_h)`$, the reading of the block $`1`$ at $`a_1\lambda`$ gives $`(\theta a_1\lambda/2a_h)^2`$ and the reading "not in the block $`0`$" at $`a_0\lambda`$ gives $`(\theta a_0\lambda/2a_h)^2`$: equality forces $`a_0=a_1=a_h`$, as (T1). On a clock level $`k`$, the component $`\Sigma=+1`$ ($`\lvert0,1\rangle,\lvert1,2\rangle`$) has the block $`\bigl(\begin{smallmatrix}V_0+M_{0,k}&i\theta/2\\-i\theta/2&V_1-M_{1,k}\end{smallmatrix}\bigr)`$ and $`\Sigma=-1`$ ($`\lvert0,2\rangle,\lvert1,1\rangle`$) has $`\bigl(\begin{smallmatrix}V_0-M_{0,k}&i\theta/2\\-i\theta/2&V_1+M_{1,k}\end{smallmatrix}\bigr)`$; adding $`\pm y_1`$ to them is $`m_0\to m_0+y_1`$, $`m_1\to m_1-y_1`$, as (5.14). With $`X=\sigma_1`$, $`[A_\zeta,\hat x]\otimes X\neq0`$ and $`a_c=a_b`$; with $`X=\sigma_3`$ the place projectors of $`c`$ commute with $`C`$ and $`a_c`$ is free, as (5.11). *Without hopping,* from a start with the weights $`w_0,w_1`$ on the two positions, $`s=1`$ and the clock in the place $`0`$: $`p_\lambda(1)=w_0\sin^2\frac{\pi\eta_0\lambda}{2\lambda_0}+w_1\sin^2\frac{\pi\eta_1\lambda}{2\lambda_0}`$, independent of $`m_x,V_x,\kappa,X`$, as (5.24). Under (5.13) it is $`\sin^2\frac{\pi\lambda'}{2\lambda_0}`$ for all weights: two runs with different weights have different clock statistics under $`C`$ (for $`\eta_0\neq\eta_1`$) and the same under $`C'`$, the dial gives the common rate $`1/\lambda_0\neq0`$ in both, and the position-resolved ratio changes from $`(w_0\eta_0+w_1\eta_1)/(w'_0\eta_0+w'_1\eta_1)`$ to $`1`$, as (5.17)(b). With $`w_0=w_1=\tfrac12`$, $`\eta_0=1`$, $`\eta_1=2`$, $`a_0=\tfrac12`$, $`a_1=2`$: $`p^{C'}_{\lambda'}(1)=\tfrac12\sin^2\frac{\pi\lambda'}{\lambda_0}+\tfrac12\sin^2\frac{\pi\lambda'}{2\lambda_0}=p^{C}_{\lambda'}(1)`$ although $`a_0\neq a_1`$, the example of Step 9(b). Passed.
3. **$`C`$ diagonal in the joint places.** There are no off-diagonal entries, so (E1)–(E3) hold for every grouping and every real diagonal $`C'\in\mathcal S`$, and a non-diagonal $`C'`$ violates (i). Directly: every place projector commutes with $`C`$ and $`C'`$, the statistics of every schedule does not depend on any $`\lambda_j`$, no relative factor is detectable, and no clock has a rate (the case without a rate in Step 10(c)). Passed.

## Open issues

- When some classes are not read and (G) does not hold for the read classes, the exact set of equivalences lies between (N) and (S) of (5.3); (5.2) is exact but is not reduced to commutators. This leaves open the complete list of contracts in item 2(a) with the medium not read; the detectability answers and (5.17) do not depend on it.
- (T1)–(T3) are sufficient, not necessary. The exact criterion is the absence of a separating grouping in (5.4). For three or more objects the A5 condition (E4), (S4) on the diagonal part is not reduced to a condition on entries.
- For several groups, (5.8) is proven as sufficient only; whether every equivalence with three or more distinct factors comes from such a sum is not decided.
- The rule by which 03-clock-and-fall obtains the mean advance $`\vartheta_W`$ from the clock statistics is not quoted in the question. Assumption R (the rule has the property (R)) is used for the statement about $`r_W`$ in Step 9(a). The exact results of Step 9(b) use the dial and the position-resolved mean advance defined here.
- The answers of item 2(c) depend on the conventions K1, K2 as stated in (5.16).
- Out of scope and not treated: re-timings that are not linear in $`\lambda`$, instances of one type, readings not local to one object, comparison by transport or by a signal.

## Methods used

- Evolved projectors for sequences of readings (Heisenberg form of (10.1))
- Power series in $`\lambda`$ and analyticity; Jacobi identity
- Commutants of place projectors; entrywise analysis of operators in the place basis
- Commuting splits of the contract; connected components of the transition graph
- Linear independence and partial trace for reading parameters off an operator
- Covariance of reading statistics under a rescaling of the evolution parameter; mixtures over a conserved label
