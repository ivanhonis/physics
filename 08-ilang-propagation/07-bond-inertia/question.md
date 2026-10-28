# Question: 07-bond-inertia

- **Subproject:** 08-ilang-propagation
- **Package:** 07-bond-inertia
- **Equation tags:** (7.k)
- **Created:** 2026-10-25

## Goal

Determine, for two bodies bound through a field of oscillator cells by a common grip, how the cost of the bond that the field makes depends on the separation of the bodies and on the joint motion of the pair; whether, and with which factor, the cost of the bond enters the inertia of the bound pair; both as functions of the ratio of the maximal speed of the bodies to the speed of the field, equality included; and whether the pair then falls like its parts. This is the part of item 5 of the base problem on a pair bound through the field, on the ring, in a field for which items 1 and 2 hold (02-grip-weight, 04-formation). The anchor of item 3 is not used; the pinning is an assumption of the package. Every result is stated through quantities that the total contract and the state fix (M6).

**Setting.**
- **Field** (assumption, M8). Oscillator cells as in the base problem ("Field of cells") on a ring ($`D=1`$) of $`L`$ cells: the compression $`C_M=\Pi H\Pi`$ of
  ```math
  H=\sum_x\tfrac12p_x^2+\frac{\kappa_h}2\sum_{\langle xy\rangle}(q_x-q_y)^2+\frac{m_h^2}2\sum_xq_x^2,\qquad\kappa_h>0,\ m_h>0,
  ```
  plus the terms of the bodies; $`\Phi_x=q_x`$; $`M\to\infty`$ first, and state in which sense it is taken. The speed of the field is $`c_0=\sqrt{\kappa_h}`$, the speed with which the long-range part of its made field forms (04-formation); the pinning length is $`\ell=\sqrt{\kappa_h}/m_h`$.
- **Bodies** (assumption, M8, A15). Two Model D bodies (base problem) of two different types, $`i=1,2`$. The own contract of body $`i`$ is only its motion term $`A_i`$, of strength $`\tau_i=\tau>0`$ for both (equal maximal speeds, a condition, M7); its rest and clock term appears only in its grip on the field, $`\sum_x\lvert x\rangle\langle x\rvert\otimes S_i\otimes F(q_x)`$ with $`S_i:=\sigma_3\otimes(m_i\mathbb 1_{N_i}+D_i)`$ and a common grip $`F`$ of class (G2) (a condition, M7), $`F(q)=F_0+F_1q+F_2q^2`$, $`F_0>0`$, $`F_1\ne0`$. There is no pair term between the bodies. Internal states $`(k_i,\sigma_i)`$, with $`\mu_i:=\sigma_iM_{k_i}`$. The position labels of the bodies are identified with the cells, one step of a body being one step of the field ($`k=1`$ in (4.17) quoted below); the maximal speed of each body is then $`\tau`$ cells per unit $`\lambda`$ ((5.11)), and it equals the speed of the field iff $`\tau=c_0`$. Write $`r:=\tau/c_0`$.
- **Expansion.** $`F=F_0+\delta F`$ with $`\delta F(q)=F_1q+F_2q^2`$; orders are orders in $`\delta F`$ at fixed $`F_0`$. The part of the joint contract that the field makes between the bodies is of second order (one factor $`\delta F`$ from each body).
- **State** (assumption, M9, A11). In the sector of the joint label $`P`$ of both bodies and the field (the translations move all three), a bound level $`E_b(P)`$ of the joint contract: a level that does not exist without the field (base problem, "Own mark and bond made through the field"), connected, as $`\delta F`$ is switched on, to the levels of the two bodies in their internal states with the field in its lowest eigenvector. Determine for which branches $`\sigma_1,\sigma_2`$ such a level exists in the stated regime, and take the extreme bound level of the band where it is unique. State the binding regime (the size of the bound level against the lattice spacing and against $`\ell`$) and the isolation condition.
- **Definitions of this package.**
  - *Mutual term*: the part of the effective joint contract of the two bodies at second order in $`\delta F`$, after the field is eliminated, that depends on both bodies.
  - *Bond cost* $`\Delta E`$: $`E_b(0)`$ minus the levels at joint label $`0`$ of the two bodies each dressed alone at the same order (the separated pair; $`L\to\infty`$ first).
  - *Inertias*: $`I_{\rm pair}:=1/E''_b(0)`$; $`I_i:=1/E''_i(0)`$ for body $`i`$ dressed alone at the same order; the share of the bond $`D:=I_{\rm pair}-I_1-I_2`$.
  - *Weights* as in 02-grip-weight, at first order in a distant held source $`g_sq_{x_s}`$.

1. **Bond: separation and motion.** At second order in $`\delta F`$, determine the mutual term of the two bodies as a function of their separation and of their labels. From it, determine how the bond's cost depends on the separation (its static limit to be compared with (2.11)) and on the joint label $`P`$ of the pair, below and above the pinning length.
2. **Bound pair.** In the binding regime, determine $`E_b(P)`$ near $`P=0`$, $`\Delta E`$, $`I_{\rm pair}`$, $`I_1`$, $`I_2`$ and $`D`$. Determine whether $`D=\Delta E/v^2`$ for one speed $`v`$, and which, as a function of $`r`$, equality included, and of the levels $`k_1,k_2`$; give the parts of $`D`$ (from the dependence of the mutual term on the labels, from the motion of the members, from the lattice) with their orders.
3. **Fall of the pair.** At leading order in the grip, from item 2 and the weighing of the bond in (2.18), determine whether the ratio of weight to inertia of the pair equals that of its members.

**Note (2026-10-25, after the review of v1).** Items 2 and 3 are asked for bound levels that are isolated eigenvalues of the full contract, with a gap to every sector of field excitations. Where a bound level is not isolated in this sense (for example when a member in the upper branch can reach its lower branch together with field quanta), its second-order coefficients may be given as formal coefficients, named as such, provided that no member can decay at the order computed (no resonance with one or two field quanta). State this condition and the range of parameters it allows.

**Note (2026-10-25, after the review of v2).** Items 2 and 3 concern bound levels whose members are near their rest levels (6.7): the label $`0`$ of each member, and on the ring its copy $`\pi`$ where the band has the same rest cost and curvature. Bound levels near other labels of the members, for example the $`(-,-)`$ levels near $`\pm\pi/2`$, are out of scope. Reason: item 5 of the base problem asks for the inertia of pairs whose members are at rest.

**Note (2026-10-25, after external round 1).**
- (a) Item 3 is asked for pairs whose extent is small against the length on which the made field of the distant held source varies over the pair. State this length on the pinned ring and the condition it puts on the binding regime.
- (b) The single body dressed alone is the subject of 06-mark-inertia; items 2 and 3 concern the share of the bond.
  - Item 2 needs the members only through $`D`$. Give $`I_i`$ at the order that $`D`$ needs, and state at which order the members' own second-order terms enter $`D`$.
  - Item 3 is asked for the contribution of the mutual term: compare the bond's weight with its share $`D`$ of the inertia, against the ratio of the members at first order in the grip. State what a comparison with the dressed members would further need.
- (c) In the deep regime, grips for which the two-quantum part of the bond is not small against its one-quantum part may be excluded; state the condition.

Reason: the share of the bond is what item 5 of the base problem needs from this package; the dressed single body is treated in 06-mark-inertia.

## Inputs

From 08-ilang-propagation/02-grip-weight@v3 (same subproject). Setting there: the same field and grips with held bodies ($`\tau=0`$) at separation $`\mathbf r`$ and a held source; $`\mu_i=\sigma_iM_{k_i}`$; $`K=\kappa_h\Delta+m_h^2\mathbb 1`$ with $`\Delta`$ the graph Laplacian, $`G(\mathbf r)=(K^{-1})_{x+\mathbf r,x}`$; $`a^{(i)}_n=\langle F^{(i)(n)}(q_x)\rangle`$, the $`n`$-th derivative of the grip of body $`i`$ averaged in the lowest eigenvector of the field; $`J_n(\mathbf r)=\int_0^\infty\Gamma_{\mathbf r}(t)^n\,dt`$ with $`\Gamma_{\mathbf r}(t)=\langle q_{x+\mathbf r}e^{-(H-E_f)t}q_x\rangle`$ ($`E_f`$ the lowest eigenvalue of the field); the bond $`U(\mathbf r)`$ is the part of the total cost of the two held bodies that depends on $`\mathbf r`$.

Eq. (2.11) of 08-ilang-propagation/02-grip-weight. Conditions stated with it in its Result: for two grips of the class at order $`\mu_1\mu_2`$; for a common grip $`U`$ has the sign of $`-\mu_1\mu_2`$, in (G2) exactly; for different grips $`U`$ can vanish at some separations.

```math
U(\mathbf r)=-2\mu_1\mu_2S_{12}(\mathbf r)+O(\mu^3),\quad S_{12}(\mathbf r):=\sum_{n\ge1}\frac{a_n^{(1)}a_n^{(2)}J_n(\mathbf r)}{n!};\qquad \text{(G2): }U=-\mu_1\mu_2\bigl[F_1^{(1)}F_1^{(2)}G(\mathbf r)+4F_2^{(1)}F_2^{(2)}J_2(\mathbf r)\bigr]+O(\mu^3).
\qquad\text{(2.11)}
```

Eq. (2.18) of 08-ilang-propagation/02-grip-weight. Conditions stated with it in its Result: grips $`F^{(i)}(q)=F^{(i)}(0)\Phi_i(\beta q)`$ of a fixed smooth shape $`\Phi_i`$ with $`\Phi_i(0)=1`$, $`\Phi_i'(0)\ne0`$ and polynomially bounded derivatives; order $`\mu^2`$ and leading order in $`\beta`$, uniformly in the separation; it holds at every distance and separation, on all three graphs, and for all $`L,\kappa_h,m_h>0`$ with $`\varepsilon,u\ll1`$, where $`\varepsilon^2=\beta^2w_0`$, $`w_0=\langle q_x^2\rangle`$, and $`u=2\max_iM_{k_i}\lvert F_2^{(i)}\rvert G(0)`$ with $`F_2^{(i)}=F^{(i)}{}''(0)/2`$. In (G2) the square grip is $`4F_0F_2=F_1^2`$, i.e. $`F(q)=F_0(1+\hat\beta q)^2`$. $`\rho_{{\rm mark},i}`$ and $`\rho_{{\rm bond},i}`$ are the weighing ratios of the mark and of the bond against the first-order part of the cost (with the reference of a single body with the grip of body $`i`$ at the midpoint), and $`m_{\mathbf r}=(\Delta\phi_1+\Delta\phi_2)/(2\Delta\bar\phi)`$ is the midpoint factor, with $`\Delta\phi_j`$ the change of the made field at body $`j`$ and $`\Delta\bar\phi`$ that at the midpoint, between two placements of the pair.

```math
\rho_{{\rm mark},i}=1\ \text{and}\ \rho_{{\rm bond},i}=m_{\mathbf r}\ (i=1,2)\ \text{for every level and both branches}\iff 2\Phi_i''(0)=\Phi_i'(0)^2\ (i=1,2)\ \text{and}\ \Phi_1'(0)=\Phi_2'(0)\iff F^{(i)}(q)=F^{(i)}(0)(1+\hat\beta q)^2+O(q^3)\ \text{with a common}\ \hat\beta .
\qquad\text{(2.18)}
```

From 08-ilang-propagation/04-formation@v4 (same subproject). Setting there: the oscillator class with a single soft point (notes (c), (d) of its question), of which the nearest-neighbour contract is a member; a Model D body with motion term of strength $`\tau`$, recorded through the coupling map (4.15) of 06-ilang-source/04-profile, one step of the body being $`k`$ steps of the field (on the ring); $`v_{\rm form}`$ the formation speed $`c_0`$ in recorded units, and $`v_{\max}`$ the maximal speed (5.11) quoted below.

Eq. (4.17) of 08-ilang-propagation/04-formation:

```math
\frac{v_{\rm form}}{v_{\max}}=\frac{c_0}{k\,\tau},\qquad v_{\rm form}=v_{\max}\iff c_0=k\tau\quad(\text{nearest neighbour: }\sqrt{\kappa_h}=k\tau),
\qquad\text{(4.17)}
```

From 04-ilang-time/05-moving-clock@v3. Setting there: a Model D body with motion term of strength $`\tau`$, recorded by a medium through $`K_x=\kappa\,x\,X`$, $`\sigma_X`$ the spread of $`X`$ in the medium's start, so that $`d_0(h,h')=\kappa\sigma_X\lvert x-x'\rvert`$; $`t_{hh'}`$ the hopping amplitudes of the body's contract; $`v_{\max}`$ the bound on the speed of the mean position of every state, (17.7) of 03-ilang-space/17-motion.

Eq. (5.11) of 04-ilang-time/05-moving-clock:

```math
v_{\max}=\tau\,\kappa\sigma_X=\max_h\sum_{h'}\lvert t_{hh'}\rvert\,d_0(h,h') .
\qquad\text{(5.11)}
```

From 04-ilang-time/06-inertia-internal-energy@v3. Setting there: the Model D body of the base problem with its own rest and clock term, eigenvector $`\lvert1\rangle`$ of the branch label the positive branch, and $`\omega_k(p)`$ the band of clock level $`k`$ in the label $`p`$.

Eq. (6.7) of 04-ilang-time/06-inertia-internal-energy:

```math
M_k:=m+d_k=m+\frac{2\pi k}{N\lambda_0}\ \ (\text{rest cost of level }k,\ \text{eigenvector }\lvert1\rangle),\qquad\text{gap }2M_k,\qquad \omega_k''(0)=\frac{\tau^2}{M_k}.
\qquad\text{(6.7)}
```

## Assumptions

- The setting under "Goal". The field, the bodies, the common grip, the equal motion strengths and the state are assumptions of the package (M8, M9); the equal parameters of the two types are conditions (M7).
- Standard mathematics applied to the stated operators may be used (perturbation theory for isolated eigenvalues in a sector of a conserved label, elimination of the field at second order (an effective contract in the band of the bodies), two-body bound levels on a chain and their dependence on the joint label, Gaussian expectation values, lattice Green functions on the ring); state it with its conditions.

## Scope

- **Class.** Every common grip of (G2) with $`F_0>0`$, $`F_1\ne0`$ (the square grip $`4F_0F_2=F_1^2`$ of (2.18) is one member), every pair of levels $`k_1,k_2`$, the branches for which a bound level exists, the ring with $`m_h>0`$ and $`\ell\gg1`$, every $`L`$ in a stated regime; second order in $`\delta F`$ for the mutual term; every ratio $`r>0`$, equality included, within the stated regime of $`\tau`$ and $`c_0`$.
- **Branches.** By (2.11) the static mutual cost has the sign of $`-\mu_1\mu_2`$; say, with a short argument, for which branches $`\sigma_1,\sigma_2`$ a bound level exists, which level of the band it is, and treat those cases; the others are out of scope.
- **Order of limits.** $`M\to\infty`$ first, then $`L\to\infty`$ for the separated reference, then the limits of the binding regime; state each order used.
- **Cancellations.** Name the members at which $`\Delta E`$, the binding, or a denominator of a ratio vanishes (for example tuned grips at which the mutual term vanishes at some separation, or levels at which the sum of the members' inverse inertias is small), and exclude them explicitly.
- **Control.** For the answer of item 2, a member of the class, or of a stated wider class, in which it fails, or a proof that there is none. The linear grip ($`F_2=0`$) is one member to treat explicitly.
- Out of scope: the cubic torus (a later package if needed); one body alone beyond what $`I_i`$ needs (06-mark-inertia, a separate package); held pairs (02-grip-weight); the anchor (05-anchor); cells with finitely many places; moving sources; pair terms between the bodies.

## Depth

- Item 1: derive (needed by item 2).
- Item 2: derive (needed by item 5 of the base problem: the inertia of a pair bound through the field against its cost at a common speed).
- Item 3: short argument (needed by item 5 of the base problem: weight over inertia for a bound pair).

## Expected result

- Item 1: an expression for the mutual term, and the dependence of the bond's cost on the separation and on the joint label.
- Item 2: expressions for $`\Delta E`$, $`I_{\rm pair}`$ and $`D`$; the factor with which $`\Delta E`$ enters $`D`$, as a function of $`r`$, or the statement that no single speed gives it, with its parts.
- Item 3: a yes/no answer with its conditions.

Give every main result a tag $`(7.k)`$.

Consistency checks, at most three: for example the held limit $`\tau\to0`$ of the mutual term against (2.11), the bare bodies against (6.7), and dimensions.

## Code

Required: check: (i) on a ring of at least 16 cells, the matrix elements of the mutual term of item 1 between two-body states of given labels, against second-order perturbation theory in the total contract restricted to states with at most two field quanta; (ii) on a ring of at least 64 cells, for one square grip and one other grip of (G2), at least three values of $`r`$ including $`r=1`$ and two binding strengths, the bound level $`E_b(P)`$ for several $`P`$ near $`0`$ and its curvature, from the exact diagonalization of the effective joint contract of item 1 in the sector $`P`$, against the formulas of item 2.
