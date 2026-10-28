# Question: 04-formation

- **Subproject:** 08-ilang-propagation
- **Package:** 04-formation
- **Equation tags:** (4.k)
- **Created:** 2026-10-24

## Goal

Determine how fast the long-range part of a made field can form after a held source is switched on; for which fields and read operators it can form within a $`\lambda`$ that grows linearly in the distance, and for which it cannot; and how the speed of its formation is related to the speeds of the field and to the maximal speed of a body. This is item 2 of the base problem. Every result is stated through quantities that the total contract and the state fix (M6).

**Setting.**
- **Class F** (assumption, M8). A field of finitely many objects with finitely many places each (A1) on a torus $`X_f`$ (a ring, a square torus or a cubic torus of side $`L`$), whose contract $`C_F`$ is a sum of pair terms (A5) of finite range and is invariant under the translations of $`X_f`$. $`A_x`$ (the operator read by a body at $`x`$) and $`B_x`$ (the operator to which the source is coupled) are the translates of one self-adjoint operator each, acting on the objects near $`x`$. A stated limit of such fields (for example the oscillator cells of the base problem as $`M\to\infty`$) may be used; it is then named.
- **Source and start** (assumption, M8, M9, A11). The contract contains the source term $`g_sB_{x_s}`$, $`g_s`$ real, at every $`\lambda`$ (A5). At $`\lambda=0`$ the field is in the lowest eigenvector $`\Omega`$ of $`C_F`$, assumed nondegenerate; $`\lambda\ge0`$ (A9). First order in $`g_s`$: the limit $`g_s\to0`$ of the coefficient is taken first.
- **Made field.** $`\delta a(x,\lambda)`$, the first-order change of $`\langle A_x\rangle_\lambda`$; the static mark $`\delta a_{\rm st}(x)`$, the same quantity in the lowest eigenvector of $`C_F+g_sB_{x_s}`$; their label components $`\delta a_{\mathbf q}(\lambda)`$, $`\delta a^{\rm st}_{\mathbf q}`$ (Fourier series on $`X_f`$).
- **Formation.** A package criterion for "the made field at distance $`\lvert r\rvert`$ has formed", stated before use and distinct from the arrival of the first change; for the field of 06-ilang-source the criterion of (8.10) quoted below.

**Note (2026-10-24, after the review of v1).** Two restrictions, because the research needs neither case. (a) In item 2 a source coupled to another operator is asked for source operators $`B`$ whose own static self-response is at most long-range, $`\chi_B(\mathbf q)\le s_B/\lvert\mathbf q\rvert^2`$ (a held body or a local source); sources with a stronger self-response are out of scope. (b) Item 3 is asked on the ring and on the cubic torus; the square torus is out of scope (the long-range mark of the base problem is defined on the cubic torus, and the ring is the control).

**Note (2026-10-24, after external round 1).** Two restrictions of item 3, because the research needs the field of the base problem and one control, and a clarification. (c) The class of item 3 contains only contracts with a single soft point: $`\hat K(\mathbf k)-m_h^2>0`$ for every $`\mathbf k\ne0`$; contracts with further soft points are out of scope. (d) Item 3 is asked for the members of this class for which the part of the made field from labels away from $`\mathbf k=0`$ obeys stationary-phase estimates with folds as the only degenerate points: finitely many caustic values of $`\rho/\lambda`$; at each degenerate stationary point of the phase $`\rho k_1\pm\lambda\hat K(\mathbf k)^{1/2}`$ a single degenerate direction, with a nonzero third derivative along it; and nondegenerate critical points of $`\hat K^{1/2}`$ away from $`\mathbf k=0`$. The other members are out of scope. Determine whether the nearest-neighbour contract is a member; the control of item 3 is to be a member. (e) In the section "Code", "the same criterion" of (ii) is the criterion of (8.10) quoted under "Inputs", in both dimensions.

**Note (2026-10-24, after external round 2).** (f) Item 2 is asked for $`B=A`$, too, only under the bound of note (a), $`\chi_A(\mathbf q)\le s_A/\lvert\mathbf q\rvert^2`$. In item 2 the constants $`s_A`$, $`s_B`$ and the norms of the local terms of $`C_F`$ and of $`A_0`$ are to be bounded uniformly in $`L`$. Cases without these bounds are out of scope, because the research needs held bodies and local sources on fields whose local terms do not change with $`L`$.

1. **A bound on formation.** For the class F: determine an upper bound on $`\lvert\delta a_{\mathbf q}(\lambda)\rvert`$, valid for every $`\lambda\ge0`$, in terms of $`\lambda`$ and of quantities fixed by $`C_F`$, $`A`$, $`B`$ and $`\Omega`$, to be compared with $`\lvert\delta a^{\rm st}_{\mathbf q}\rvert`$; state its conditions.
2. **Read operators that are conserved densities.** Let $`A_x`$ be the density of a conserved number of the field: the number commutes with $`C_F`$, and the terms that move it have finite range. Determine whether a static place dependence $`\delta a_{\rm st}`$ that falls as the inverse of the distance on the cubic torus (the long-range mark of the base problem) can form within a $`\lambda`$ that grows linearly in the distance, for $`B=A`$ and for a source coupled to another operator, fields of several kinds of objects included.
3. **Oscillator cells.** For oscillator cells (base problem, "Field of cells") with the contract $`H=\tfrac12\sum_xp_x^2+\tfrac12\sum_{x,y}q_xK_{xy}q_y`$, and $`A_x=B_x=q_x`$, in the limit $`M\to\infty`$ taken first. The class: $`K`$ of finite range, invariant under the translations and under the permutations and reflections of the lattice axes, with Fourier transform $`\hat K(\mathbf k)=m_h^2+c_0^2\lvert\mathbf k\rvert^2+O(\lvert\mathbf k\rvert^4)`$, $`m_h>0`$, $`c_0>0`$, and positive (it contains the nearest-neighbour contract of the base problem). Determine, with a stated criterion, whether the long-range part of the made field forms within a $`\lambda`$ linear in the distance along the lattice axes, at distances large against the lattice spacing and small against the pinning length $`c_0/m_h`$, and at which speed; and the relation of this speed to $`c_0`$, to the largest slope of the normal-mode frequencies $`\hat K(\mathbf k)^{1/2}`$ and to the speed of the front.
4. **Speeds of bodies and field.** Compare the formation speed of item 3 with the maximal speed (5.11) of a Model D body coupled to the field through a coupling map of the form (4.15) (on the ring; along a lattice axis of the tori as a stated assumption, M8); state the condition on the parameters under which the two are equal.

## Inputs

From 07-ilang-weight/08-field-speed@v4. Setting there for (8.10) and (8.14): the field of 06-ilang-source/04-profile ($`N_f\ge1`$ identical field objects, no pair terms among them, own term $`C_1=-t_fA`$ with $`A`$ the nearest-neighbour adjacency of $`\mathbb Z_L^D`$, $`\Phi_x`$ the number of field objects at $`x`$, $`n=N_f/\lvert X_f\rvert`$); source $`g_s\Phi_{x_s}`$ in the contract at every $`\lambda`$, start in the lowest state without the source; made field $`\delta\rho(x,\lambda)=\langle\Phi_x\rangle_\lambda-n`$ and its static value $`\delta\rho_{\rm st}`$; first order in $`g_s`$, then $`L\to\infty`$ (or $`\lambda`$ below the wrap time). **Criterion** there: the long-range part at distance $`\lvert r\rvert`$ is formed to accuracy $`\varepsilon`$ from $`\lambda_f`$ on if $`\lvert1-\partial_{\lvert r\rvert}\delta\rho/\partial_{\lvert r\rvert}\delta\rho_{\rm st}\rvert\le\varepsilon`$ for every $`\lambda\ge\lambda_f`$, with $`\delta\rho_{\rm st}`$ replaced by its long-range part, applied in the pointwise scaling-limit sense at fixed $`\zeta=\lvert r\rvert^2/(4t_f\lambda)`$; $`\zeta^*`$ is a fixed value at which the bound fails.

Eq. (8.10) of 07-ilang-weight/08-field-speed:

```math
\lambda_{\rm form}(|r|;\varepsilon)=\frac{|r|^2}{4t_f\,\zeta_D(\varepsilon)},\qquad \zeta_1=\frac{\pi\varepsilon^2}2\bigl(1+O(\varepsilon^2)\bigr),\quad \zeta_2=\sqrt{2\varepsilon}\bigl(1+O(\varepsilon)\bigr),\quad \zeta_3=\Bigl(\frac{3\sqrt{2\pi}\,\varepsilon}4\Bigr)^{2/3}\bigl(1+O(\varepsilon^{2/3})\bigr),\qquad\text{(8.10)}
```

Eq. (8.14) of 07-ilang-weight/08-field-speed:

```math
\text{in the class, at first order, for every fixed }\beta>0\text{ and }\varepsilon<1:\quad \lambda_{\rm form}(|r|;\varepsilon)>\frac{|r|^2}{4t_f\zeta^*}>\frac{\beta|r|}{t_f}\ \text{ for all large }|r|.\qquad\text{(8.14)}
```

Setting there for (8.15): oscillator cells on the cubic torus, one object of its own type per place with the places $`0,\dots,M-1`$, the contract the compression $`C_M=\Pi H\Pi`$ of $`H=\sum_x\tfrac12p_x^2+\frac{\kappa_h}2\sum_{\langle xy\rangle}(q_x-q_y)^2+\frac{m_h^2}2\sum_xq_x^2+g_sq_{x_s}`$, $`\kappa_h,m_h>0`$; start in the lowest state of $`C_M`$ at $`g_s=0`$; made field $`\langle q_x\rangle_\lambda`$, static mark $`\langle q\rangle_{\rm st}`$; $`m_Y=m_h/\sqrt{\kappa_h}`$; order of limits $`M\to\infty`$, $`L\to\infty`$, then $`\rho\to\infty`$ along an axis, $`r=\rho\mathbf e_1`$, at fixed $`c`$ and $`m_Y\rho`$; the front window $`\lvert\sqrt{\kappa_h}\lambda-\rho\rvert=O(\rho^{1/3})`$ excluded.

Eq. (8.15) of 07-ilang-weight/08-field-speed:

```math
\Bigl|\frac{\langle q\rangle(\rho\mathbf e_1,\lambda)}{\langle q\rangle_{\rm st}(\rho\mathbf e_1)}-1\Bigr|\le8.4\,m_Y\rho+o(1)\qquad\Bigl(c=\frac{\sqrt{\kappa_h}\lambda}\rho>1\ \text{fixed},\ m_Y\rho\le1\Bigr),\qquad o(1)=O(\rho^{-1/2})\ \text{for}\ 1<c<2.\qquad\text{(8.15)}
```

From 04-ilang-time/05-moving-clock@v3. Setting there: a Model D body with motion term of strength $`\tau`$, recorded by a medium through $`K_x=\kappa\,x\,X`$, $`\sigma_X`$ the spread of $`X`$ in the medium's start, so that $`d_0(h,h')=\kappa\sigma_X\lvert x-x'\rvert`$; $`t_{hh'}`$ the hopping amplitudes of the body's contract; $`v_{\max}`$ the bound on the speed of the mean position of every state, (17.7) of 03-ilang-space/17-motion.

Eq. (5.11) of 04-ilang-time/05-moving-clock:

```math
v_{\max}=\tau\,\kappa\sigma_X=\max_h\sum_{h'}\lvert t_{hh'}\rvert\,d_0(h,h') .
\qquad\text{(5.11)}
```

From 06-ilang-source/04-profile@v4. Setting there: a body coupled to a field on a ring of $`L`$ places by $`\sum_m\lvert h_m\rangle\langle h_m\rvert\otimes G\otimes\Phi_{\pi(m)}`$, with $`\pi`$ a map from the body's chain labels to ring places (assumption); $`S=\{m_0,\dots,m_0+K\}`$ the positions used, $`K\ge1`$; $`d_\Gamma`$ the ring distance; the requirement that the mutual cost of two held bodies be a function of their recorded distance $`d_0=\lvert m-m'\rvert\sigma_X`$ up to a scale, with $`k`$ the resulting positive integer.

Eq. (4.15) of 06-ilang-source/04-profile:

```math
d_\Gamma\bigl(\pi(m),\pi(m')\bigr)=k\lvert m-m'\rvert\ \ \forall m,m'\in S\iff \pi(m)=\pi(m_0)+s\,k\,(m-m_0)\bmod L,\ s=\pm1,\ kK\le\lfloor L/2\rfloor,\qquad\text{(4.15)}
```

## Assumptions

- The setting under "Goal". The field classes, the source, the start and the coupling map are assumptions of the package (M8, M9).
- Standard mathematics applied to the stated operators may be used (spectral representations of first-order responses, Fourier analysis on tori, inequalities for sums over a spectrum, stationary phase and lattice asymptotics, compressions and min-max); state it with its conditions.

## Scope

- **Class.** Items 1 and 2: the class F, every $`D`$, every $`L`$ large enough for the stated regime, and the stated limits; item 3: the oscillator class above; first order in $`g_s`$ throughout.
- **Order of limits.** $`g_s\to0`$ first, then $`M\to\infty`$ where it applies, then $`L\to\infty`$ (or $`\lambda`$ below the wrap time), then the distance along a stated path; state it at every result.
- **Control.** For item 2, a member of the class F or of a stated limit in which a long-range part forms within a $`\lambda`$ linear in the distance, or a proof that there is none. For item 3, a member of the class in which $`c_0`$ and the largest slope of $`\hat K^{1/2}`$ differ.
- **Other states** (A11). For items 1 and 2, say whether the results hold for the highest eigenvector as well.
- Out of scope: moving sources; weighing (02-grip-weight, 03-gas-grip); fields without pinning and anchors (a later package); the relation of field places to the distances of 03-ilang-space beyond item 4.

## Depth

- Item 1: derive (needed by item 2 and by item 2 of the base problem).
- Item 2: derive; the control at the depth of a short argument with a stated example (needed by item 2 of the base problem: for which read operators formation at a finite speed is excluded; and by the later package on anchors, item 3).
- Item 3: derive (needed by item 2 of the base problem and by items 3 and 5: the formation speed of the field used there).
- Item 4: short argument (needed by item 2 of the base problem and by item 5: the condition for a common speed).

## Expected result

- Item 1: an inequality with its conditions.
- Item 2: a yes/no answer with its conditions, and a control.
- Item 3: a yes/no answer in the class; where yes, the formation speed as a function of $`K`$, its relation to the other speeds, and the range of distances.
- Item 4: the ratio of the speeds and the condition for equality.

Give every main result a tag $`(4.k)`$.

Consistency checks, at most three: for example (8.10) and (8.15) as special cases, and dimensions.

## Code

Required: check: (i) item 3 on a ring with $`L\ge256`$ and on a cubic torus with $`L\ge48`$, for the nearest-neighbour $`K`$ and for one $`K`$ of the class whose $`c_0`$ differs from the largest slope of $`\hat K^{1/2}`$, at three or more distances: the formation $`\lambda`$ against the distance with the stated criterion; (ii) the field of 06-ilang-source (one field object suffices at first order) with the same criterion, for item 2.
