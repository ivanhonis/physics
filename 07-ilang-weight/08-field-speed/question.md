# Question: 08-field-speed

- **Subproject:** 07-ilang-weight
- **Package:** 08-field-speed
- **Equation tags:** (8.k)
- **Created:** 2026-10-21

## Goal

Determine, for the field class of the subproject, how a change of the field caused by a source spreads over the field places: whether it has a front with a finite speed, how long the made field takes to reach its static form at a given distance, whether the long-range part of the static mark forms at a finite speed, and how the speed compares with the speed of bodies. This is item 4 of the base problem for the field class used in 06-ilang-source and here, and the last clause of item 3 (the role of the speed with which a change of the field spreads). Every result is stated through quantities that the total contract and the state fix (M6).

**Setting.**
- **Field.** The class of 06-ilang-source/04-profile: $`N_f\ge1`$ identical field objects ($`c=+1`$) on a ring ($`D=1`$), a square torus ($`D=2`$) or a cubic torus ($`D=3`$) of side $`L`$, $`\lvert X_f\rvert=L^D`$ places, no pair terms among them, own term $`C_1=-t_f\sum_{\langle x,y\rangle}(\lvert x\rangle\langle y\rvert+\lvert y\rangle\langle x\rvert)`$ over nearest neighbours, $`t_f>0`$, $`\Phi_x`$ the number of field objects at $`x`$, $`n:=N_f/\lvert X_f\rvert`$.
- **Source.** A held body seen through its point coupling: the term $`g_s(\lambda)\Phi_{x_s}`$, with $`g_s(\lambda)=0`$ for $`\lambda<0`$. Two switchings, each an assumption: (i) sudden, $`g_s(\lambda)=g_s`$ for $`\lambda\ge0`$; (ii) gradual, $`g_s(\lambda)=g_sf(\lambda/T)`$ with a smooth $`f`$ rising from $`0`$ to $`1`$ over $`[0,1]`$, of duration $`T`$.
- **State** (assumption, M9, A11): at $`\lambda<0`$ the field is in its lowest state (no source). The language selects no relaxation; the field evolves by (1.9) of the base problem.
- **Made field.** $`\delta\rho(x,\lambda):=\langle\Phi_x\rangle_\lambda-n`$; the static mark: $`\delta\rho`$ in the lowest state with the source present. Results at first order in $`g_s`$ unless stated, with the regime named.
- **Distances** are counted in place labels (graph distance $`d`$ from $`x_s`$). Their relation to the distances of 03-ilang-space is out of scope.

1. **Front.** With a stated criterion for the arrival of the change at distance $`d`$ (for example the first $`\lambda`$ at which $`\lvert\delta\rho\rvert`$ there exceeds a fixed fraction of a stated reference), determine for the sudden switching whether the arrival time grows linearly in $`d`$ at large $`d`$, the speed if it does, and the size of the change ahead of the front.
2. **Formation of the static mark.** Determine on which scale of $`\lambda`$, as a function of $`d`$, $`D`$ and $`L`$, the made field at distance $`d`$ comes within a stated fraction of the static mark: (i) for the sudden switching, in a stated sense (for example its average over $`\lambda`$, since nothing relaxes); (ii) for the gradual switching, how large $`T`$ must be, as a function of $`d`$, $`D`$ and $`L`$, for the made field to follow the static mark to a stated accuracy.
3. **Long range and finite speed.** Determine whether, in this class, the long-range part of the static mark (the dependence on $`d`$ of (4.4) of 07-ilang-weight/04-weight-of-bond, quoted below) forms on a scale of $`\lambda`$ that grows linearly in $`d`$, or only on a longer one.
4. **Speeds.** Compare the speed of item 1, if it exists, with $`\tau`$, the largest group velocity of the motion term of a Model D body alone (base problem), both in place labels per unit $`\lambda`$. State the condition on $`t_f`$ and $`\tau`$ under which a body moves more slowly than the front.

**Note (2026-10-21, after external round 1).** The gradual switching (ii) is withdrawn: a contract that depends on $`\lambda`$ is excluded by A5 of the base problem, and this question should not have asked for it. Only the sudden switching (i) is asked, read as a fixed contract with the source present, started in the lowest state without the source. Item 2 (ii) is out of scope; item 2 asks only (i). Any control must have a well-defined lowest state with the source (a static mark).

**Note (2026-10-21, after external round 2).** Item 1 is asked along the lattice axes (and in $`D=1`$); in other directions only the absence of early arrival is asked. The base problem needs whether the field has a finite speed and its value, not its full dependence on direction. Statements at finite $`g_s`$ are asked relative to the first-order static reference (8.2) unless the remainder of the static mark itself is bounded.

## Inputs

From 06-ilang-source/04-profile@v4. Setting there: the field class above with two held sources $`g_i\Phi_{x_i}`$; $`\Lambda`$ the graph Laplacian, $`\Lambda^+`$ its pseudo-inverse, $`\omega(\mathbf k)`$ the dispersion of one field object in units of $`t_f`$; $`M^{(2)}`$ the second-order mutual term of the two sources.

Eq. (4.4) of 06-ilang-source/04-profile:

```math
M^{(2)}(x_1,x_2)=-\frac{2n\,g_1g_2}{t_f}\,\Lambda^+(x_1,x_2),\qquad \Lambda^+(x,y)=\frac1{\lvert X_f\rvert}\sum_{\mathbf k\neq0}\frac{e^{i\mathbf k\cdot(x-y)}}{\omega(\mathbf k)},\quad \omega(\mathbf k)=\sum_{\mu=1}^{D}4\sin^2\frac{k_\mu}2,\qquad \sum_{x_2\in X_f}M^{(2)}(x_1,x_2)=0,\qquad\text{(4.4)}
```

From 07-ilang-weight/04-weight-of-bond@v3. Setting there: the same class; $`\ell(\mathbf r)=\Lambda^+(x,x+\mathbf r)`$; $`\gamma_E`$ Euler's constant.

Eq. (4.4) of 07-ilang-weight/04-weight-of-bond:

```math
\ell(0)-\ell(\mathbf r)=\begin{cases}\dfrac{\ln\lvert\mathbf r\rvert}{2\pi}+\dfrac{2\gamma_E+3\ln2}{4\pi}+O(\lvert\mathbf r\rvert^{-2})-\dfrac{\lvert\mathbf r\rvert^2}{4L^2}, & D=2,\\[2mm] G_0-\dfrac1{4\pi\lvert\mathbf r\rvert}+O(\lvert\mathbf r\rvert^{-3})-\dfrac{\lvert\mathbf r\rvert^2}{6L^3},\quad G_0=\Lambda^{-1}_{\mathbb Z^3}(0)=0.2527310, & D=3,\end{cases}\qquad\text{(4.4)}
```

## Assumptions

- The setting under "Goal". The field class, the source, the switchings and the start are assumptions of the package (M8, M9).
- Standard mathematics applied to the stated operators may be used (first-order time-dependent perturbation theory, Fourier analysis on tori, asymptotics of lattice sums and of Bessel-type integrals, bounds on the propagation of the one-object evolution); state it with its conditions.

## Scope

- **Class.** The field class above, $`N_f\ge1`$, $`D=1,2,3`$, every $`L`$ large enough for the stated regime, first order in $`g_s`$ (state where the answer needs more).
- **Control.** For the answers of items 1–3, a description of a stated wider class of field contracts (for example with pair terms among field objects, or field objects with more places) in which the answer differs, or a proof that there is none in that class.
- Out of scope: moving or shaken sources; the relation of place distances to 03-ilang-space; how typical the class is (item 5 of the base problem).

## Depth

- Item 1: derive (needed by item 4 of the base problem and by the closing report of the subproject: the speed of the field).
- Item 2: derive (needed by item 4 of the base problem: whether the made field forms at a finite speed).
- Item 3: derive in the class; the control at the depth of a short argument with a stated example (needed by item 4 of the base problem: long range and finite speed together, and by the choice of the field class of the next stage).
- Item 4: short argument (needed by item 3 of the base problem: the role of the speed of the field against the speed of bodies).

## Expected result

- Item 1: a yes/no answer on a finite front speed, with its value and the size of the change ahead of it.
- Item 2: the scales of $`\lambda`$ (sudden switching) and of $`T`$ (gradual switching) as functions of $`d`$, $`D`$, $`L`$.
- Item 3: a yes/no answer in the class, with a control.
- Item 4: the ratio of the two speeds and the condition.

Give every main result a tag $`(8.k)`$.

Consistency checks, at most three: for example the static limit against (4.4), the sum rule of (4.4) at every $`\lambda`$, and dimensions.

## Code

Required: check: for $`N_f=1`$ (the first-order response of $`N_f`$ objects is $`N_f`$ times that of one), on a ring with $`L\ge64`$ and on a cubic torus with $`L\ge16`$, items 1 and 2 against the exact evolution of one field object from its lowest state with the source switched on suddenly and gradually, at small $`g_s`$, with the scaling in $`d`$ fitted and stated.
