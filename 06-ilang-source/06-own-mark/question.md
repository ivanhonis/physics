# Question: 06-own-mark

- **Subproject:** 06-ilang-source
- **Package:** 06-own-mark
- **Equation tags:** (6.k)
- **Created:** 2026-10-19

## Goal

Determine what the change of the field made by a body itself (its own mark) does to the body: the cost of its levels, the dependence of that cost on the plane-wave label (its inertia), and the spacings of its clock levels, at second order in its coupling to the field; and whether these changes are the same for all clock levels in proportion to their gaps. This is the first part of item 5 of the base problem. Every result is stated through quantities that the total contract fixes (M6): eigenvalues of the total contract in a sector of fixed total plane-wave label, their differences between levels, and their curvature in the label.

**Setting.**
- **Field.** The class of 04-profile on a ring of $`L`$ places: $`N_f\ge1`$ identical field objects ($`c=+1`$), no pair terms among them, own term $`C_1=-t_f\sum_x(\lvert x\rangle\langle x+1\rvert+\lvert x+1\rangle\langle x\rvert)`$, $`\Phi_x`$ the number of field objects at $`x`$, $`n:=N_f/L`$.
- **Body.** One Model D body $`b`$ (base problem, "Notation and conventions") on the same ring of position labels, with $`\tau>0`$, $`m>0`$, clock levels $`k`$ with half-gap $`M_k:=m+d_k`$, $`d_k:=\frac{2\pi k}{N\lambda_0}`$, coupled to the field by one of the two couplings of 02-what-a-body-presents with a coupling constant $`\gamma`$: (a) $`\gamma\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m\mathbb 1_N+D)\otimes\Phi_x`$; (c) the same plus $`\gamma`$ times the motion term with the factor $`\frac12(\Phi_x+\Phi_{x+1})`$ on each bond. Records at zeroth order ($`\kappa\to0`$); state what changes for $`\kappa>0`$ only if it is short.
- **Sectors.** The clock level $`k`$ is conserved, and so is the total plane-wave label $`P`$ of body and field (joint translation of the ring). For each $`k`$, branch $`\sigma`$ and $`P`$ near $`0`$, the *dressed level* $`E_{k,\sigma}(P)`$ is the eigenvalue of the total contract in the sector $`(k,P)`$ that is connected, as $`\gamma\to0`$, to the body in the branch start $`(p=P,\sigma,k)`$ with the field in its lowest state. Its existence and isolation are to be stated.
- **Invariant quantities** (to be shown invariant under every replacement of the listed terms that leaves $`C`$ unchanged): the dressed levels as eigenvalues of $`C`$; their differences between clock levels at fixed $`\sigma`$, $`P`$; their curvature $`E''_{k,\sigma}(0)`$ in $`P`$ and the curvature inertia $`1/E''_{k,\sigma}(0)`$.

1. **Dressed level.** For each coupling, through second order in $`\gamma`$ at fixed $`L`$, $`N_f`$, $`t_f`$, $`\tau`$, $`m`$: determine $`E_{k,\sigma}(P)`$ for $`P`$ near $`0`$, with the condition under which the dressed level is isolated (in particular when the field's excitations reach the gap $`2M_k`$ between the branches); give the second-order shift (the cost of the own mark) at $`P=0`$ and its dependence on $`k`$, $`\sigma`$, $`N_f`$, $`L`$, $`t_f`$.
2. **Clock spacings.** Determine the differences $`E_{k+1,+}(0)-E_{k,+}(0)`$ through second order in $`\gamma`$, and whether the second-order change of each spacing is proportional to the unperturbed spacing with one factor for all $`k`$ (a common rescaling of the clock by the own mark), for each coupling.
3. **Inertia.** Determine $`E''_{k,\sigma}(0)`$ through second order in $`\gamma`$, and compare the curvature inertia with $`M_k/\tau^2`$ (the inertia without the mark, (6.7) of 04-ilang-time/06-inertia-internal-energy) and with the dressed cost $`E_{k,+}(0)`$ divided by $`\tau^2`$: state whether the change of the inertia equals the change of the cost divided by $`\tau^2`$, and whether it is the same function of $`M_k`$ for all levels.
4. **Control.** A body without motion term ($`\tau\to0`$) and a body whose coupling multiplies its rest term only ($`\sigma_3\otimes m\mathbb 1_N`$ in place of $`\sigma_3\otimes(m\mathbb 1_N+D)`$): the answers of items 2 and 3 for them.

**Note (2026-10-19, after the review of v1).** Items 2 and 3 are restricted: for the negative answers ("not a common rescaling", "the change of the inertia is not the change of the cost divided by $`\tau^2`$") a stated parameter region in which they hold, inside the isolation condition, suffices; a classification of all parameters is not asked. Reason: item 5 of the base problem needs only whether the own mark preserves the common scale and the tie of inertia to cost in general, not the full parameter map.

## Inputs

From 05-moving-clock@v3 of 04-ilang-time. Setting there: one Model D body with the contract $`C_b=C_{\rm D}`$ of the base problem; $`d_k:=\frac{2\pi k}{N\lambda_0}`$; the plane waves $`\lvert p\rangle=\sum_xe^{ipx}\lvert x\rangle`$, $`p\in(-\pi,\pi]`$.

Eq. (5.5) of 04-ilang-time/05-moving-clock:

```math
C_b\bigl(\lvert p\rangle\otimes\beta\otimes\lvert f_k\rangle\bigr)=\lvert p\rangle\otimes C_k(p)\beta\otimes\lvert f_k\rangle,\qquad C_k(p):=-\tau\sin p\,\sigma_1+\mu_k\sigma_3,\qquad\mu_k:=m+d_k .
```

Eq. (5.6) of 04-ilang-time/05-moving-clock, the eigenvalues $`\pm\omega_k(p)`$ and the real eigenvectors $`\lvert p\rangle\otimes\beta_{k,\pm}(p)\otimes\lvert f_k\rangle`$ of $`C_b`$:

```math
\omega_k(p)=\sqrt{\mu_k^2+\tau^2\sin^2p},\quad
\beta_{k,+}=\begin{pmatrix}\cos\frac{\theta_k}2\\ \sin\frac{\theta_k}2\end{pmatrix},\quad
\beta_{k,-}=\begin{pmatrix}-\sin\frac{\theta_k}2\\ \cos\frac{\theta_k}2\end{pmatrix},\quad
\tan\theta_k(p)=-\frac{\tau\sin p}{\mu_k},\ \ \lvert\theta_k\rvert<\frac\pi2 .
```

From 06-inertia-internal-energy@v3 of 04-ilang-time. Setting there: one Model D body; on the clock level $`k`$ the contract acts on plane waves as $`C_k(p)=-\tau\sin p\,\sigma_1+M_k\sigma_3`$.

Eq. (6.7) of 04-ilang-time/06-inertia-internal-energy:

```math
M_k:=m+d_k=m+\frac{2\pi k}{N\lambda_0}\ \ (\text{rest cost of level }k,\ \text{eigenvector }\lvert1\rangle),\qquad\text{gap }2M_k,\qquad \omega_k''(0)=\frac{\tau^2}{M_k}.
```

From 04-profile@v4 (this subproject). Setting there: the field class of the setting above, held sources $`g_i\Phi_{x_i}`$; $`h(g)`$ the single-object contract with the sources, $`\varepsilon_0(g)`$ its lowest eigenvalue.

Eq. (4.2) of 04-profile:

```math
E(g)=N_f\,\varepsilon_0(g),\qquad M=N_f\bigl[\varepsilon_0(g_1,g_2)-\varepsilon_0(g_1,0)-\varepsilon_0(0,g_2)+\varepsilon_0(0,0)\bigr].\qquad\text{(4.2)}
```

## Assumptions

- The setting under "Goal". The field class, the body, its couplings and the dressed levels are assumptions of the package (M8, M9); the language selects no state (A11), and the dressed level is a named eigenvector of the total contract.
- Standard perturbation theory for an isolated eigenvalue may be used with its conditions stated.

## Scope

- **Class.** Both couplings, every $`N_f\ge1`$, $`L\ge3`$, every level $`k`$, both branches, $`P`$ near $`0`$.
- **Control.** Item 4.
- Out of scope: the fall of the dressed body in a field made by another source (a later package); a test body in the field of a source (05-made-field-scale); orders above the second in $`\gamma`$, except where an exact statement is short; more than one body.

## Depth

- Item 1: derive (needed by items 2–3 and by item 5 of the base problem).
- Item 2: derive (needed by item 5 of the base problem: the clock of a body that makes a field).
- Item 3: derive (needed by item 5 of the base problem: the inertia of a body that makes a field, against its cost).
- Item 4: short argument (control).

## Expected result

- Item 1: an expression for the dressed level through second order, an isolation condition, and the dependences of the shift.
- Item 2: an expression for the spacings and a yes/no answer for each coupling.
- Item 3: an expression for the curvature and two yes/no answers for each coupling.
- Item 4: the answers of items 2–3 for the two controls.

Give every main result a tag $`(6.k)`$.

Consistency checks, at most three: for example $`\gamma\to0`$, $`N_f\to`$ large at fixed $`n`$, and the sum rule over the branches.

## Code

Required: check: exact diagonalization of the total contract in the sectors $`(k,P)`$ for one field object ($`N_f=1`$) on rings of at least two sizes, for both couplings and at least two clock levels; compare the dressed levels, the clock spacings and the curvature at $`P=0`$ (by finite differences in $`P`$ over the allowed labels, or by an exact derivative) with items 1–3 at several values of $`\gamma`$, and report the scaling of the deviation with $`\gamma`$.
