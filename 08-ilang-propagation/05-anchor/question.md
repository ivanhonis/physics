# Question: 05-anchor

- **Subproject:** 08-ilang-propagation
- **Package:** 05-anchor
- **Equation tags:** (5.k)
- **Created:** 2026-10-25

## Goal

Determine, for a field of oscillator cells whose contract leaves a change applied to all cells alike free, whether the total contract with held bodies and held sources has a lowest eigenvector; what an anchor changes; and, in the lowest eigenvector of a contract with an anchor, whether the mutual cost of two held sources has a long-range part and for which grips a held body weighs its own mark and a bond like the first-order part of its cost, in which order of the limits (size, distance to the anchor, separation). This is item 3 of the base problem without the formation of the mark, which is a later package. Every result is stated through quantities that the total contract and the state fix (M6).

**Setting.**
- **Field** (assumption, M8). Oscillator cells as in the base problem ("Field of cells"): one cell at each place $`x`$ of $`X_f`$, a ring ($`D=1`$) or a cubic torus ($`D=3`$) of side $`L`$, $`\lvert X_f\rvert=L^D`$, each cell an object of its own type with the places $`0,\dots,M-1`$; the contract is the compression $`C_M=\Pi H\Pi`$ of
  ```math
  H=\sum_x\tfrac12p_x^2+\frac{\kappa_h}2\sum_{\langle xy\rangle}(q_x-q_y)^2,\qquad\kappa_h>0,
  ```
  plus the terms of the anchor, the bodies and the sources below; $`\Phi_x=q_x`$. There is no pinning ($`m_h=0`$): $`H`$ is unchanged by the change $`q_x\to q_x+c`$ of all cells alike. Statements about the uncompressed contract are statements about the limit $`M\to\infty`$, taken first; state in which sense it is taken.
- **Anchor** (assumption, M8, A15; base problem, "Anchor"). The term $`\frac{\kappa_a}2q_h^2`$, $`\kappa_a>0`$, on the cell at one place $`h`$ (a term on one cell, A5). Descriptions without an anchor are asked in item 1.
- **Bodies** (assumption, M8, A15). Held Model D bodies ($`\tau=0`$), each at a position label identified with one cell (separations are cell separations; their relation to the distances of 03-ilang-space is out of scope, M2), in the eigenvector $`\lvert\sigma\rangle\lvert f_k\rangle`$ of $`S:=\sigma_3\otimes(m\mathbb 1_N+D)`$ with eigenvalue $`\mu:=\sigma M_k`$. A body has no rest and clock term of its own; it holds on to the field by the grip $`\sum_x\lvert x\rangle\langle x\rvert\otimes S\otimes F(q_x)`$ with $`F`$ of class (G2): $`F(q)=F_0+F_1q+F_2q^2`$, real coefficients, $`F_1\ne0`$. Two bodies may carry different grips of the class.
- **Sources** (assumption, M8, A15). Held objects at places $`x_s`$, each coupled to the cell there by $`g_sq_{x_s}`$, $`g_s`$ real: first order in $`g_s`$ for weights; for the mutual cost of two sources, the term proportional to $`g_sg_s'`$.
- **State** (assumption, M9, A11). The lowest eigenvector of the total contract in the limit $`M\to\infty`$, where it exists.
- **Definitions** as in 02-grip-weight (quoted under "Inputs"), applied to the description with the anchor: the cost of a body (the lowest eigenvalue with the body minus that without it, both without sources), its first-order part $`C^{(1)}`$ and its mark $`C^{\rm mark}`$ (replace $`F`$ by $`sF`$ and expand in $`s`$), the weight $`W(x)-W(x')`$ at first order in $`g_s`$, the bond of two bodies and its weight, $`\rho_{\rm mark}`$, $`\rho_{{\rm bond},i}`$ with the reference of a single body with the grip of body $`i`$ at the midpoint of the pair, and the midpoint factor $`m_{\mathbf r}`$. With an anchor these quantities may depend on the places relative to $`h`$; state how. The *mutual cost* of two held sources is the part of the lowest eigenvalue with both sources that depends on both of them.

1. **Without an anchor.** Determine whether the total contract of the field with held bodies of class (G2) and held sources has a lowest eigenvector ($`M\to\infty`$), and the condition. Say whether the grips of the bodies can act as an anchor, and for which grips, levels and branches.
2. **With an anchor.** Determine the condition for a lowest eigenvector with the anchor and with held bodies; the made field of a held source (the shift of the field in the lowest eigenvector, first order in $`g_s`$) as a function of the places of the source, of the observation and of the anchor; and the field constants that enter the cost and the weight (the analogues of $`G_0`$, of $`w_0=\langle q_x^2\rangle`$ and of the static correlations of 02-grip-weight) as functions of the distance to the anchor, on both graphs.
3. **Long-range mark.** Determine the mutual cost of two held sources in the anchored lowest eigenvector on the cubic torus, and in which order of the limits $`L\to\infty`$, distance of the sources to the anchor $`\to\infty`$ and separation of the sources $`\to\infty`$ it falls as the inverse of the separation (base problem, "Long-range mark"); give the same for the ring.
4. **Weighing with an anchor.** For held bodies of class (G2) in the anchored lowest eigenvector: determine the cost, $`C^{(1)}`$, $`C^{\rm mark}`$, their weights, the bond and its weight, $`\rho_{\rm mark}`$ and $`\rho_{{\rm bond},i}`$. Determine for which grips $`\rho_{\rm mark}=1`$ and $`\rho_{{\rm bond},i}=m_{\mathbf r}`$ for every level and both branches, at which order in the grip, and how this depends on the distances to the anchor and on the order of the limits; where they differ, the first deviation and its parameter.

## Inputs

From 08-ilang-propagation/02-grip-weight@v3 (same subproject). Setting there: the same oscillator cells, held bodies, grips, source and definitions, but with pinning, $`H+\frac{m_h^2}2\sum_xq_x^2`$ with $`m_h>0`$, and without an anchor; $`K:=\kappa_h\Delta+m_h^2\mathbb 1`$ with $`\Delta`$ the graph Laplacian, $`G(x):=(K^{-1})_{x+y,y}`$, $`G_0:=G(0)`$, $`\mu=\sigma M_k`$.

Eq. (2.5) of 08-ilang-propagation/02-grip-weight (for (G2)):

```math
\text{a lowest eigenvector exists }(M\to\infty)\iff 1+2\sigma M_kF_2G_0>0;\ \text{otherwise the lowest eigenvalue of }C_M\to-\infty .
\qquad\text{(2.5)}
```

Eq. (2.18) of 08-ilang-propagation/02-grip-weight. Conditions stated with it in its Result: grips $`F^{(i)}(q)=F^{(i)}(0)\Phi_i(\beta q)`$ of a fixed smooth shape $`\Phi_i`$ with $`\Phi_i(0)=1`$, $`\Phi_i'(0)\ne0`$ and polynomially bounded derivatives; order $`\mu^2`$ and leading order in $`\beta`$, uniformly in the separation; it holds at every distance and separation, on all three graphs, and for all $`L,\kappa_h,m_h>0`$ with $`\varepsilon,u\ll1`$, where $`\varepsilon^2=\beta^2w_0`$, $`w_0=\langle q_x^2\rangle`$ in the lowest eigenvector of the field, and $`u=2\max_iM_{k_i}\lvert F_2^{(i)}\rvert G_0`$ with $`F_2^{(i)}=F^{(i)}{}''(0)/2`$. In (G2) the square grip is $`4F_0F_2=F_1^2`$, i.e. $`F(q)=F_0(1+\hat\beta q)^2`$. $`m_{\mathbf r}=(\Delta\phi_1+\Delta\phi_2)/(2\Delta\bar\phi)`$ is the midpoint factor, with $`\Delta\phi_j`$ the change of the made field $`\phi(x)=-g_sG(x-x_s)`$ at body $`j`$, and $`\Delta\bar\phi`$ that at the midpoint, between two placements of the pair.

```math
\rho_{{\rm mark},i}=1\ \text{and}\ \rho_{{\rm bond},i}=m_{\mathbf r}\ (i=1,2)\ \text{for every level and both branches}\iff 2\Phi_i''(0)=\Phi_i'(0)^2\ (i=1,2)\ \text{and}\ \Phi_1'(0)=\Phi_2'(0)\iff F^{(i)}(q)=F^{(i)}(0)(1+\hat\beta q)^2+O(q^3)\ \text{with a common}\ \hat\beta .
\qquad\text{(2.18)}
```

## Assumptions

- The setting under "Goal". The field, the anchor, the bodies, the grips, the sources and the field state are assumptions of the package (M8, M9).
- Standard mathematics applied to the stated operators may be used (quadratic forms and their lowest eigenvectors, Gaussian expectation values, rank-one updates such as Sherman–Morrison and the matrix determinant lemma, compressions and min-max, lattice Green functions on tori and their asymptotics); state it with its conditions.

## Scope

- **Class.** Every grip of (G2), several bodies with different grips included, every level and both branches, every $`\kappa_a>0`$ and every anchor place $`h`$, the ring and the cubic torus, every $`L`$ in a stated regime; first order in $`g_s`$ for weights, the term $`g_sg_s'`$ for the mutual cost of two sources.
- **Order of limits.** $`M\to\infty`$ first; then the size, the distance to the anchor and the separation, in each order that items 3 and 4 ask or use; state every order, and say which results depend on it.
- **Cancellations.** Name the members at which a denominator of a weighing ratio vanishes (as in 02-grip-weight: a vanishing $`C^{(1)}`$ or $`\partial_cC^{(1)}`$, a vanishing $`\Delta\bar\phi`$, a vanishing bond) and exclude them explicitly.
- **Control.** For items 3 and 4, a description of the class, or of a stated wider class, in which the answer fails, or a proof that there is none. The ring is one control for item 3; the linear grip ($`F_2=0`$) is one member to treat explicitly in item 4.
- Out of scope: moving bodies and inertia; the formation of the mark and its speed with an anchor (a later package); cells with finitely many places (item 4 of the base problem); anchors other than $`\frac{\kappa_a}2q_h^2`$ (but state how the results depend on $`\kappa_a`$ and what $`\kappa_a\to\infty`$ gives); the square torus.

## Depth

- Item 1: derive (needed by item 3 of the base problem: the free uniform change).
- Item 2: derive (needed by items 3 and 4, and by the later package on formation with an anchor).
- Item 3: derive (needed by item 3 of the base problem: a long-range mark in the lowest eigenvector with an anchor).
- Item 4: derive (needed by item 3 of the base problem, and by item 4: the grip that weighs).

## Expected result

- Item 1: a condition for the existence of a lowest eigenvector, with the members that meet it.
- Item 2: the existence condition with the anchor; expressions for the made field and for the field constants, with their dependence on the distance to the anchor.
- Item 3: the place dependence of the mutual cost of two sources, with the order of limits in which it is the inverse of the separation, or the statement that it is not.
- Item 4: conditions on the grip, with the order in the grip, the dependence on the distances to the anchor and the order of limits; the first deviation otherwise.

Give every main result a tag $`(5.k)`$.

Consistency checks, at most three: for example the limit $`\kappa_a\to\infty`$, the comparison of item 4 with (2.18) where the two settings can be compared, and dimensions.

## Code

Required: check: on a ring and on a cubic torus of two sizes each, with an anchor, against the exact lowest eigenvalue of the uncompressed quadratic total contract: (i) the existence conditions of items 1 and 2 for at least two grips; (ii) the mutual cost of two held sources against the separation, at two distances of the pair from the anchor; (iii) $`\rho_{\rm mark}`$ and $`\rho_{{\rm bond},i}`$ of item 4 for two levels and both branches, at three distances from the anchor.
