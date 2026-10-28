# Question: 02-grip-weight

- **Subproject:** 08-ilang-propagation
- **Package:** 02-grip-weight
- **Equation tags:** (2.k)
- **Created:** 2026-10-24

## Goal

Determine how the weight of a held body, of its own mark and of a bond made through the field depends on the grip function, for a field of oscillator cells, and for which grips the mark and the bond are weighed like the first-order part of the cost. This is item 1 of the base problem for a field of cells. Every result is stated through quantities that the total contract and the state fix (M6).

**Setting.**
- **Field** (assumption, M8). Oscillator cells as in the base problem ("Field of cells"): one cell at each place $`x`$ of $`X_f`$, a ring ($`D=1`$), a square torus ($`D=2`$) or a cubic torus ($`D=3`$) of side $`L`$, $`\lvert X_f\rvert=L^D`$, each cell an object of its own type with the places $`0,\dots,M-1`$; the contract is the compression $`C_M=\Pi H\Pi`$ of
  ```math
  H=\sum_x\tfrac12p_x^2+\frac{\kappa_h}2\sum_{\langle xy\rangle}(q_x-q_y)^2+\frac{m_h^2}2\sum_xq_x^2,\qquad\kappa_h>0,\ m_h>0,
  ```
  plus the terms of the bodies and the source below; $`\Phi_x=q_x`$. Statements about the uncompressed contract are statements about the limit $`M\to\infty`$, taken first; state in which sense it is taken.
- **Bodies** (assumption, M8, A15). Held Model D bodies ($`\tau=0`$), each at a position label identified with one cell (the separations used are cell separations; their relation to the distances of 03-ilang-space is out of scope, M2), in the eigenvector $`\lvert\sigma\rangle\lvert f_k\rangle`$ of $`S:=\sigma_3\otimes(m\mathbb 1_N+D)`$ with eigenvalue $`\sigma M_k`$. A body has no rest and clock term of its own; it holds on to the field by the grip of the base problem, $`\sum_x\lvert x\rangle\langle x\rvert\otimes S\otimes F(q_x)`$, with a real grip function $`F`$. Two classes of grips:
  - (G2) $`F(q)=F_0+F_1q+F_2q^2`$ with real $`F_0,F_1,F_2`$, $`F_1\ne0`$: the total contract stays quadratic in the $`q`$'s;
  - (G) a real function $`F`$, smooth at $`q=0`$, with $`F'(0)\ne0`$, written $`F(q)=F(0)+\theta f(q)`$ with $`f(0)=0`$, $`f'(0)=1`$, studied through the lowest orders in $`\theta`$ at which the mark and its weight appear.
- **Source** (assumption, M8, A15). One held object at $`x_s`$ coupled to the cell there by the pair term $`g_sq_{x_s}`$, $`g_s`$ real; first order in $`g_s`$.
- **State** (assumption, M9, A11). For (G2): the lowest eigenvector of the total contract, in the limit $`M\to\infty`$, where it exists; state the condition on the grip under which it exists. For (G): the eigenvalue of $`C_M`$ connected, as $`\theta\to0`$, to the lowest eigenvalue at $`\theta=0`$; its Taylor coefficients in $`\theta`$, each taken in the limit $`M\to\infty`$; state where this eigenvalue is the lowest one.
- **Definitions of this package.**
  - *Cost* of a body: the lowest eigenvalue of the description with the body (in its internal state $`(k,\sigma)`$) minus that without the body, both without the source.
  - *First-order part* $`C^{(1)}`$ and *mark* $`C^{\rm mark}`$: replace $`F`$ by $`sF`$ and expand the cost in $`s`$; $`C^{(1)}`$ is the term linear in $`s`$, at $`s=1`$, and $`C^{\rm mark}`$ is the cost minus $`C^{(1)}`$.
  - *Weight*: the dependence of the same eigenvalue, with the source present, on the place $`x`$ of the held body, $`W(x)-W(x')`$, as in the base problem. The weights of $`C^{(1)}`$ and of $`C^{\rm mark}`$ are defined by the same expansion in $`s`$, with the source present.
  - *Bond*: for two held bodies at $`x_1`$ and $`x_2=x_1+\mathbf r`$ with grips of the same class and no pair term between them, the part of their total cost that depends on $`\mathbf r`$, without the source; its weight is the dependence of that part on a common shift of both bodies with the source present.
  - *Weighing ratios*: $`\rho_{\rm mark}`$, the weight of the mark per unit of mark divided by the weight of $`C^{(1)}`$ per unit of $`C^{(1)}`$; and $`\rho_{\rm bond}`$, the weight of the bond per unit of bond profile divided by the same quantity for $`C^{(1)}`$, referred to the midpoint of the pair. Where a ratio has a vanishing denominator, say so.

**Note (2026-10-24, after external round 1).**
- (a) Class (G) is restricted to grips of a fixed shape on the scale of the field's fluctuations: $`F(q)=F(0)\,\Phi(\beta q)`$ with $`F(0)\ne0`$, $`\Phi(0)=1`$, $`\Phi'(0)\ne0`$, or $`F(q)=F(0)+\theta f(q)`$, where $`\Phi`$ and $`f`$ are smooth and every derivative of them is bounded by a polynomial. Results are expansions in $`\beta`$ (resp. $`\theta`$) at fixed $`\Phi`$ (resp. $`f`$). Grips outside this class are out of scope.
- (b) The reference of $`\rho_{\rm bond}`$ is the weight of $`C^{(1)}`$ per unit of $`C^{(1)}`$ of a single body at the midpoint of the pair with the grip of body $`i`$; this gives one ratio $`\rho_{{\rm bond},i}`$ per body, as in 07-ilang-weight/04-weight-of-bond. The two coincide for a common grip. With this reference, pairs whose first-order costs cancel need not be excluded. The two bodies may have different grips of the class.
- (c) For members whose mark weight vanishes at the lowest order (for example shapes odd about zero), state this and the lowest order at which a nonzero weight can appear; its value at that order is not asked.

1. **Cost and mark.** For (G2) exactly, and for (G) through the lowest order in $`\theta`$ at which $`C^{\rm mark}`$ appears: determine the cost, $`C^{(1)}`$ and $`C^{\rm mark}`$ of a held body as functions of $`k`$, $`\sigma`$, the grip and the field parameters ($`\kappa_h`$, $`m_h`$, $`L`$, $`D`$), and state which part is fixed by the total contract.
2. **Weight.** At first order in $`g_s`$: determine $`W(x)-W(x')`$ for both classes, split into the weights of $`C^{(1)}`$ and of $`C^{\rm mark}`$, on the three graphs, with their forms at distances from the source large against the lattice spacing, both below and above the pinning length $`\sqrt{\kappa_h}/m_h`$.
3. **Bond.** For two held bodies with grips of either class: determine the bond profile and its weight, referred to the midpoint, at first order in $`g_s`$ and through the lowest order in the grip at which the bond and its weight appear; say how the weight changes if another place of the pair is used.
4. **Which grips weigh.** Determine for which grips (and for which $`\kappa_h`$, $`m_h`$, $`L`$, $`D`$) $`\rho_{\rm mark}=1`$ and $`\rho_{\rm bond}=1`$ for every level and both branches, at which order in the grip and for which distances; where they are not 1, the first deviation, its parameter and its dependence on the distance.

## Inputs

None. The package builds only on the base problem (its notation "Model D", "Field of cells", "Grip", "Weight, inertia and cost").

## Assumptions

- The setting under "Goal". The field class, the bodies, the grips, the source and the field state are assumptions of the package (M8, M9).
- Standard mathematics applied to the stated operators may be used (quadratic forms and their lowest eigenvectors, Gaussian expectation values, perturbation theory for an isolated eigenvalue, compressions and min-max, Fourier analysis and lattice sums on the three graphs); state it with its conditions.

## Scope

- **Class.** Both grip classes, every level and both branches, the three graph families, every $`L`$ and $`m_h>0`$ in a stated regime; first order in $`g_s`$; the full grip dependence for (G2) where the lowest eigenvector exists.
- **Order of limits.** $`M\to\infty`$ first, then the size, then the distances, unless a result states another order; say how the results depend on $`m_h`$ and whether they have a limit as $`m_h\to0`$ at fixed $`L`$ and as $`L\to\infty`$.
- **Cancellations.** Name the members of the class at which a denominator of a weighing ratio vanishes (for example a body whose $`C^{(1)}`$ vanishes, or a pair whose first-order costs cancel) and exclude them explicitly.
- **Control.** For each answer of item 4, a description of the class, or of a stated wider class, in which it fails, or a proof that there is none. The linear grip ($`F_2=0`$ in (G2)) is one member to treat explicitly.
- **Other states** (A11). For one stated eigenvector of the field other than the lowest, say whether the answers of item 4 change.
- Out of scope: moving bodies and inertia; the speed with which the made field forms (04-formation); fields of identical objects (03-gas-grip); fields without pinning ($`m_h=0`$) and anchors (a later package).

## Depth

- Item 1: derive (needed by items 2–4).
- Item 2: derive (needed by item 4).
- Item 3: derive (needed by item 4).
- Item 4: derive (needed by item 1 of the base problem and by the later package on anchors, item 3 of the base problem).
- Other states: short argument (needed by item 1 of the base problem, A11).

## Expected result

- Item 1: expressions for the cost, $`C^{(1)}`$ and $`C^{\rm mark}`$, exact for (G2) and as an expansion for (G), with the existence condition.
- Item 2: expressions for the weights on the three graphs, with large-distance forms.
- Item 3: expressions for the bond profile and its weight.
- Item 4: conditions on the grip and the field parameters, with the order and the range of distances; the first deviation otherwise.

Give every main result a tag $`(2.k)`$.

Consistency checks, at most three: for example the limit of a linear grip, the sum of the weight over all places, and dimensions.

## Code

Required: check: (i) for (G2) grips, on a ring and on a cubic torus of two sizes each, $`\rho_{\rm mark}`$ and $`\rho_{\rm bond}`$ of item 4 against the exact lowest eigenvalue of the uncompressed quadratic total contract, for two levels and both branches and at least three distances; (ii) on a ring of three cells, the lowest eigenvalue of the compression $`C_M`$ for increasing $`M`$ against the uncompressed value, for one grip of each class.
