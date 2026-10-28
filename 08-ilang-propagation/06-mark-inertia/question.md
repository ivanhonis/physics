# Question: 06-mark-inertia

- **Subproject:** 08-ilang-propagation
- **Package:** 06-mark-inertia
- **Equation tags:** (6.k)
- **Created:** 2026-10-25

## Goal

Determine the inertia of a moving body with its own mark against its cost, for a body that holds on to a field of oscillator cells with weak pinning by a grip of class (G2), for every level and both branches, as a function of the ratio of the maximal speed of the body to the speed of the field, equality included; and whether the ratio of weight to inertia is the same for every level and both branches. This is item 5 of the base problem for one body, in a field for which items 1 and 2 hold (02-grip-weight, 04-formation). The anchor of item 3 is not used; the pinning is an assumption of the package. Every result is stated through quantities that the total contract and the state fix (M6).

**Setting.**
- **Field** (assumption, M8). Oscillator cells as in the base problem ("Field of cells") on a ring ($`D=1`$) or a cubic torus ($`D=3`$) of side $`L`$: the compression $`C_M=\Pi H\Pi`$ of
  ```math
  H=\sum_x\tfrac12p_x^2+\frac{\kappa_h}2\sum_{\langle xy\rangle}(q_x-q_y)^2+\frac{m_h^2}2\sum_xq_x^2,\qquad\kappa_h>0,\ m_h>0,
  ```
  plus the terms of the body; $`\Phi_x=q_x`$; $`M\to\infty`$ first, and state in which sense it is taken. The speed of the field is $`c_0=\sqrt{\kappa_h}`$, the speed with which the long-range part of its made field forms (04-formation); the pinning length is $`\ell=\sqrt{\kappa_h}/m_h`$.
- **Body** (assumption, M8, A15). One Model D body (base problem) whose own contract is only its motion term $`A`$, $`\tau>0`$, and whose rest and clock term appears only in its grip on the field (the full-grip form of the base problem, "Couplings" and "Grip"): $`\sum_x\lvert x\rangle\langle x\rvert\otimes S\otimes F(q_x)`$, $`S:=\sigma_3\otimes(m\mathbb 1_N+D)`$, with $`F`$ of class (G2), $`F(q)=F_0+F_1q+F_2q^2`$, $`F_0>0`$, $`F_1\ne0`$. The position labels of the body are identified with the cells, one step of the body being one step of the field ($`k=1`$ in (4.17) quoted below); on the cubic torus the chain of the body runs along one lattice axis (assumption, M8). The maximal speed of the body is then $`\tau`$ cells per unit $`\lambda`$ ((5.11)), and the two speeds are equal iff $`\tau=c_0`$. Write $`r:=\tau/c_0`$.
- **Expansion.** $`F=F_0+\delta F`$ with $`\delta F(q)=F_1q+F_2q^2`$; orders are orders in $`\delta F`$ at fixed $`F_0`$. At zeroth order the body is a Model D body whose rest and clock term is $`F_0`$ times that of (6.7) quoted below.
- **State** (assumption, M9, A11). In the sector of the joint label $`P`$ of body and field (the translations move both), the level $`E_{k,\sigma}(P)`$ that is connected, as $`\delta F`$ is switched on, to the level of branch $`\sigma`$ and clock level $`k`$ with the field in its lowest eigenvector. State the condition under which it is isolated and analytic in $`P`$ and in $`\delta F`$.
- **Definitions of this package.**
  - *Cost*: $`\mathrm{Cost}_{k,\sigma}:=E_{k,\sigma}(0)`$ minus the lowest eigenvalue of the field alone. $`C^{(1)}_{k,\sigma}`$ is its part of zeroth and first order in $`\delta F`$, and the mark $`C^{\rm mark}_{k,\sigma}`$ is the rest, taken at second order.
  - *Inertia*: $`I_{k,\sigma}:=1/E''_{k,\sigma}(0)`$, the inverse curvature in the joint label (base problem, "Weight, inertia and cost"), split in the same way into $`I^{(1)}_{k,\sigma}`$ and $`I^{\rm mark}_{k,\sigma}`$.
  - *Weight*: the weight of the body in the field of a distant held source $`g_sq_{x_s}`$ at first order in $`g_s`$, as in 02-grip-weight. At leading order in $`\tau`$ it is that of the held body, (2.8) quoted below; state any correction that is used.

1. **Dressed level.** At second order in $`\delta F`$, in a stated regime of $`\tau`$ and $`c_0`$ against the isolation distance of the level, determine $`E_{k,\sigma}(P)`$ near $`P=0`$, $`\mathrm{Cost}_{k,\sigma}`$, $`C^{(1)}_{k,\sigma}`$ and $`C^{\rm mark}_{k,\sigma}`$ for every level and both branches, on both graphs, together with the isolation condition.
2. **Inertia against cost.** Determine $`I_{k,\sigma}`$, $`I^{(1)}_{k,\sigma}`$ and $`I^{\rm mark}_{k,\sigma}`$. Determine whether there is one speed $`v`$ with $`I^{(1)}_{k,\sigma}=C^{(1)}_{k,\sigma}/v^2`$ and $`I^{\rm mark}_{k,\sigma}=C^{\rm mark}_{k,\sigma}/v^2`$ for every level and both branches, and which; as a function of $`r`$, equality included, and of the grip. State the dependence on $`\ell`$ and on $`L`$, and the order of the limits.
3. **Weight over inertia.** Determine whether $`E''_{k,\sigma}(0)\,\Delta W_{k,\sigma}`$ is the same for every level and both branches at second order in $`\delta F`$, with the weights of (2.8), as a function of $`r`$ and of the grip.

**Note (2026-10-25, after external round 1).** (a) Items 2 and 3 are asked for the states that are isolated eigenvalues of the full contract, with a gap to every sector of field excitations. Where a level is not isolated in this sense (for example the upper branch, which states of the lower branch with several field quanta can reach), its second-order coefficients may be given as formal coefficients, named as such, and are not counted as an answer for an isolated state. (b) On the cubic torus, where the lattice sums have no closed form, items 2 and 3 are asked in this form: whether the property holds for every member of the class, where a member with stated numerical margins settles a negative answer; and for which members it holds on a stated grid of parameters, reported as a numerical finding. A proof of monotonicity or convexity between grid points is not asked; the research needs the answer for the class and the members found, not a complete classification.

## Inputs

From 08-ilang-propagation/02-grip-weight@v3 (same subproject). Setting there: the same field and grips with held bodies ($`\tau=0`$) and a held source $`g_sq_{x_s}`$, first order in $`g_s`$; $`\mu=\sigma M_k`$; $`K=\kappa_h\Delta+m_h^2\mathbb 1`$ with $`\Delta`$ the graph Laplacian, $`G(x)=(K^{-1})_{x+y,y}`$, $`G_0=G(0)`$, $`w_0=\langle q_x^2\rangle`$ in the lowest eigenvector of the field; $`D_\mu:=1+2\mu F_2G_0`$, positive where the lowest eigenvector exists ((2.5) there); $`Z(a):=\frac1{2\pi}\int_0^\infty\ln(1+a\,g(\nu))\,d\nu`$ with $`g(\nu)=[(K+\nu^2)^{-1}]_{xx}`$; $`\zeta\ge0`$ a zero-point term, $`\zeta=\frac{4F_2^2J_2}{G_0}[1+O(\mu F_2G_0)]`$, with $`J_2=\int_0^\infty\Gamma(t)^2\,dt`$ and $`\Gamma(t)=\langle q_xe^{-(H-E_f)t}q_x\rangle`$ ($`E_f`$ the lowest eigenvalue of the field); the made field $`\phi(x)=-g_sG(x-x_s)`$ and $`\Delta\phi=\phi(x)-\phi(x')`$; $`\Delta W^{(1)}`$, $`\Delta W^{\rm mark}`$ the weights of $`C^{(1)}`$ and $`C^{\rm mark}`$.

Eq. (2.6) of 08-ilang-propagation/02-grip-weight (for (G2), exactly, where the lowest eigenvector exists):

```math
\text{cost}=\mu F_0-\frac{\mu^2F_1^2G_0}{2D_\mu}+Z(2\mu F_2),\qquad
C^{(1)}=\mu(F_0+F_2w_0)=\mu\langle F\rangle_0,\qquad
C^{\rm mark}=-\frac{\mu^2G_0}{2D_\mu}\bigl(F_1^2+\zeta\bigr),
\qquad\text{(2.6)}
```

Eq. (2.8) of 08-ilang-propagation/02-grip-weight (for (G2), exactly; the zero-point part is not weighed):

```math
W(x)-W(x')=\frac{\mu F_1}{D_\mu}\Delta\phi,\qquad
\Delta W^{(1)}=\mu F_1\,\Delta\phi,\qquad
\Delta W^{\rm mark}=-\frac{2\mu^2F_1F_2G_0}{D_\mu}\Delta\phi .
\qquad\text{(2.8)}
```

Eq. (2.18) of 08-ilang-propagation/02-grip-weight. Conditions stated with it in its Result: grips $`F^{(i)}(q)=F^{(i)}(0)\Phi_i(\beta q)`$ of a fixed smooth shape $`\Phi_i`$ with $`\Phi_i(0)=1`$, $`\Phi_i'(0)\ne0`$ and polynomially bounded derivatives; order $`\mu^2`$ and leading order in $`\beta`$, uniformly in the separation; it holds at every distance and separation, on all three graphs, and for all $`L,\kappa_h,m_h>0`$ with $`\varepsilon,u\ll1`$, where $`\varepsilon^2=\beta^2w_0`$ and $`u=2\max_iM_{k_i}\lvert F_2^{(i)}\rvert G_0`$ with $`F_2^{(i)}=F^{(i)}{}''(0)/2`$. In (G2) the square grip is $`4F_0F_2=F_1^2`$, i.e. $`F(q)=F_0(1+\hat\beta q)^2`$; $`m_{\mathbf r}`$ is the midpoint factor of a pair.

```math
\rho_{{\rm mark},i}=1\ \text{and}\ \rho_{{\rm bond},i}=m_{\mathbf r}\ (i=1,2)\ \text{for every level and both branches}\iff 2\Phi_i''(0)=\Phi_i'(0)^2\ (i=1,2)\ \text{and}\ \Phi_1'(0)=\Phi_2'(0)\iff F^{(i)}(q)=F^{(i)}(0)(1+\hat\beta q)^2+O(q^3)\ \text{with a common}\ \hat\beta .
\qquad\text{(2.18)}
```

From 08-ilang-propagation/04-formation@v4 (same subproject). Setting there: the oscillator class with a single soft point (notes (c), (d) of its question), of which the nearest-neighbour contract is a member; a Model D body with motion term of strength $`\tau`$, recorded through the coupling map (4.15) of 06-ilang-source/04-profile, one step of the body being $`k`$ steps of the field (on the ring; along a lattice axis of the tori as a stated assumption); $`v_{\rm form}`$ the formation speed $`c_0`$ in recorded units, and $`v_{\max}`$ the maximal speed (5.11) quoted below.

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

- The setting under "Goal". The field, the body, the grips and the state are assumptions of the package (M8, M9).
- Standard mathematics applied to the stated operators may be used (perturbation theory for an isolated eigenvalue in a sector of a conserved label and its analytic dependence on the label, Gaussian expectation values, Fourier analysis and lattice sums on the two graphs, compressions); state it with its conditions.

## Scope

- **Class.** Every grip of (G2) with $`F_0>0`$, $`F_1\ne0`$ (the square grip $`4F_0F_2=F_1^2`$ of (2.18) is one member), every level and both branches where the level is isolated, the ring and the cubic torus, $`m_h>0`$ with $`\ell\gg1`$, every $`L`$ in a stated regime; second order in $`\delta F`$; every ratio $`r>0`$, equality included, within the stated regime of $`\tau`$ and $`c_0`$.
- **Order of limits.** $`M\to\infty`$ first, then $`L\to\infty`$ (or a stated large $`L`$), then the dependence on $`\ell`$; state each order used.
- **Cancellations.** Name the members at which a ratio of inertia to cost has a vanishing denominator (for example a vanishing $`C^{\rm mark}`$ at second order) and exclude them explicitly.
- **Control.** For the answers of items 2 and 3, a member of the class, or of a stated wider class, in which the answer fails, or a proof that there is none. The linear grip ($`F_2=0`$) is one member to treat explicitly.
- Out of scope: two bodies and bound pairs (07-bond-inertia, a separate package); the anchor (05-anchor); cells with finitely many places; moving sources; the square torus.

## Depth

- Item 1: derive (needed by items 2 and 3).
- Item 2: derive (needed by item 5 of the base problem: inertia against cost at a common speed).
- Item 3: derive (needed by item 5 of the base problem: weight over inertia for every level).

## Expected result

- Item 1: expressions for $`E_{k,\sigma}(P)`$ near $`P=0`$ and for the cost and its parts at second order, with the isolation condition.
- Item 2: expressions for the inertia and its parts; the speed $`v`$ as a function of $`r`$ and of the grip, or the statement that no single $`v`$ exists, with the first difference.
- Item 3: a yes/no answer with its conditions, and the first dependence on the level otherwise.

Give every main result a tag $`(6.k)`$.

Consistency checks, at most three: for example the held limit $`\tau\to0`$ against (2.6), the bare body against (6.7), and dimensions.

## Code

Required: check: on a ring of at least 32 cells, for one square grip and one other grip of (G2), two levels, both branches and at least three values of $`r`$ including $`r=1`$: $`\mathrm{Cost}_{k,\sigma}`$ and $`E''_{k,\sigma}(0)`$ at second order in $`\delta F`$ against an independent computation, the levels of the total contract restricted to states with at most two field quanta (exact at second order in $`\delta F`$) in the sectors $`P`$ near $`0`$, with the second-order coefficient extracted from several small values of $`\delta F`$.
