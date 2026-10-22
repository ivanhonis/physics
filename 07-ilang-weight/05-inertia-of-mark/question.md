# Question: 05-inertia-of-mark

- **Subproject:** 07-ilang-weight
- **Package:** 05-inertia-of-mark
- **Equation tags:** (5.k)
- **Created:** 2026-10-21

## Goal

Determine, for one moving body with its own mark, how its inertia is related to its cost, for every level and both branches, for couplings (a), (c) and the full grip: whether the inertia is the cost divided by the square of one speed, and which speed; whether the ratio of weight to inertia is the same for all levels and both branches; and how these answers depend on the hopping amplitude of the field. This is item 3 of the base problem for a single body. Every result is stated through quantities that the total contract and the state fix (M6).

**Setting.**
- **Field.** $`N_f\ge1`$ identical field objects ($`c=+1`$) on a ring of $`L`$ places, no pair terms among them, own term $`C_1=-t_f\sum_x(\lvert x\rangle\langle x+1\rvert+\lvert x+1\rangle\langle x\rvert)`$, $`t_f>0`$, $`\Phi_x`$ the number of field objects at $`x`$, $`n:=N_f/L`$.
- **Body.** One Model D body (base problem, "Notation and conventions") with $`\tau>0`$, clock levels $`k`$ with half-gaps $`M_k`$, on the same ring of position labels, coupled to the field by one of three couplings of the base problem ("Couplings"), with a real constant $`\gamma`$: (a), (c), or the full grip in the form written there (own contract $`A`$ only; the rest and clock term only in the pair term $`\gamma\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m\mathbb 1_N+D)\otimes\Phi_x`$). Records at $`\kappa\to0`$.
- **State of the field** (assumption, M9): the lowest state adapted to the body. The highest state is out of scope.
- **Inertia:** $`1/E''_{k,\sigma}(0)`$, the inverse curvature in the total plane-wave label $`P`$ of the dressed level of the sector contract (6.1) of 06-ilang-source/06-own-mark (quoted below). For the full grip, state whether (6.1) applies unchanged.
- **Cost:** eigenvalue differences fixed by the total contract, as in the base problem ("Weight, inertia and cost"): the held-body cost (3.4) of 07-ilang-weight/03-weight-of-mark (quoted below), and the dressed level $`E_{k,\sigma}(0)`$ relative to the description without the body. State which of them enters each comparison.
- **Weight:** the place dependence of the held body's eigenvalue in the field of a distant held source $`g_sP_{x_s}`$ at first order in $`g_s`$, (3.12)–(3.13) of 07-ilang-weight/03-weight-of-mark (quoted below).

1. **Inertia of the full grip.** Determine $`E''_{k,\sigma}(0)`$ for the full grip, for every level and both branches, in a regime to be stated and named as an assumption (isolation of the dressed level, the order in $`\gamma`$ and in $`\tau`$). State the isolation condition in terms of $`t_f`$, $`L`$, $`N_f`$, $`\gamma`$, $`M_k`$ and $`\tau`$, and the branches and parameters for which it fails.
2. **Inertia against cost.** For each of the three couplings, determine whether there is one number $`v`$, the same for all levels and both branches, such that the inertia equals the cost divided by $`v^2`$. Use the level-difference form where M6 requires it: differences of inertia between levels and branches against the differences of cost. Answer at leading order and at the first order at which the answer changes, if it does. Identify $`v`$ by the parameters of the description, and state whether it is a group velocity of a band of the description, and of which band.
3. **Weight over inertia.** For each coupling, determine whether the product of the curvature $`E''_{k,\sigma}(0)`$ and the weight difference $`\Delta W_{k,\sigma}`$ between two places is the same for all levels and both branches. This product is the factor that sets the fall from rest in (7.7) of 06-ilang-source/07-dressed-fall (quoted below). Answer at leading order, and give the first order and the size of a level or branch dependence, if there is one. For the full grip, state whether (7.7) applies (its setting is couplings (a) and (c)).
4. **The hopping of the field.** State how the answers of items 1–3 depend on $`t_f`$ at fixed $`n`$, $`\gamma`$, $`M_k`$, $`\tau`$: the speed $`v`$, the isolation regime, and the order of the first level dependence. Include $`t_f`$ large and small against $`M_k`$ and $`\tau`$, and $`L\to\infty`$ at fixed $`n`$ where the regime allows it. The speed with which a change of the field spreads is item 4 of the base problem and is not asked here.

**Note (2026-10-21, after external round 2).** Two clarifications. (i) In item 2, for descriptions in which one speed holds through the first order at which it fails generically (isolated, tuned parameter values), only the criterion that locates them and the numerical findings are asked. Their behaviour at higher orders is out of scope: the base problem needs whether one speed holds in general, not for tuned exceptions. (ii) The mean position on the ring must be a well-defined observable for the starts used, for example a local chart away from the place where the labels close. The acceleration of item 3 refers to it.

## Inputs

From 06-ilang-source/06-own-mark@v3. Setting there: one Model D body with coupling (a) or (c) and constant $`\gamma`$ on the ring field of the setting above, no source, lowest field state $`\Omega_f`$; $`Q_k=1`$ the projector on clock level $`k`$, $`\sigma=\pm`$ the branch; $`\omega_k(P)=(M_k^2+\tau^2\sin^2P)^{1/2}`$ the bare band and $`\tilde\omega_k`$ its mean-field value; $`\beta_\sigma(P)`$ the bare branch vector; $`\varepsilon_q=2t_f(1-\cos q)`$ the excitation energies of one field object; $`\hat V_q`$ the fluctuation vertex, $`M_k\sigma_3`$ for (a) and $`\frac12[C_k(P)+C_k(P-q)]`$ for (c); $`\Delta_{k,+}`$ the second-order own-mark cost at $`P=0`$ ((6.6) there); $`E_{\rm exc}`$ and $`Q`$ the energy and label of an excited field eigenstate.

Eq. (6.1) of 06-ilang-source/06-own-mark:

```math
C_k(P)=\hat C^{(0)}+e^{-iP}\hat C^{(+)}+e^{iP}\hat C^{(+)\dagger},\qquad\text{(6.1)}
```

Eq. (6.4) of 06-ilang-source/06-own-mark:

```math
\sigma\omega_k(P)\neq\sigma'\omega_k(P-Q)+E_{\rm exc}\quad\text{for every excited field eigenstate }(Q,E_{\rm exc})\text{ and }\sigma'=\pm\qquad\text{(6.4)}
```

Eq. (6.5) of 06-ilang-source/06-own-mark:

```math
E_{k,\sigma}(P)=\sigma\tilde\omega_k(P)-2t_fN_f+\gamma^2\frac nL\sum_{q\ne0}G_{k,\sigma}(P,q)+O(\gamma^3),\qquad G_{k,\sigma}=\langle\beta_\sigma(P)\vert\hat V_q\,(z_q-C_k(P-q))^{-1}\hat V_q\vert\beta_\sigma(P)\rangle,\qquad\text{(6.5)}
```

with $`z_q=\sigma\omega_k(P)-\varepsilon_q`$.

Eq. (6.10) of 06-ilang-source/06-own-mark:

```math
E''_{k,\sigma}(0)=\sigma\frac{\tau^2}{M_k}\times\begin{cases}1-\gamma n+\gamma^2n^2&\text{(a)}\\ 1+\gamma n&\text{(c)}\end{cases}+\Delta''_{k,\sigma}+O(\gamma^3),\qquad \Delta''_{k,\sigma}:=\gamma^2\frac nL\sum_{q\ne0}\partial_P^2G_{k,\sigma}(P,q)\big|_{P=0}.\qquad\text{(6.10)}
```

Eq. (6.12) of 06-ilang-source/06-own-mark, with $`\delta X:=X(\gamma)-X(0)`$:

```math
\delta\Bigl(\frac1{E''_{k,+}(0)}\Bigr)-\frac{\delta E_{k,+}(0)}{\tau^2}=\begin{cases}-\dfrac1{\tau^2}\Bigl[\dfrac{M_k^2}{\tau^2}\Delta''_{k,+}+\Delta_{k,+}\Bigr]&\text{(a)}\\[2mm] \dfrac{M_k}{\tau^2}(-2\gamma n+\gamma^2n^2)-\dfrac1{\tau^2}\Bigl[\dfrac{M_k^2}{\tau^2}\Delta''_{k,+}+\Delta_{k,+}\Bigr]&\text{(c)}\end{cases}\ +O(\gamma^3).\qquad\text{(6.12)}
```

From 07-ilang-weight/02-two-free-bodies@v3. Setting there: body $`i`$ of the setting above with coupling (a) or (c); $`\mu_i=1/E''_{k_i,\sigma_i}(0)`$; $`R_i`$ half the difference of the $`\tau=0`$ eigenvalues of $`b_i`$ alone in its two branches (field lowest), $`R_i=M_i(1+\gamma_in)+O(\gamma_i^3)`$.

Eq. (2.14) of 07-ilang-weight/02-two-free-bodies:

```math
\mu_i=\sigma_i\frac{R_i}{\tau_i^2}+O(\gamma_i^2)\ \ \text{(a)},\qquad \mu_i=\sigma_i\frac{R_i}{\tau_i^2(1+\gamma_in)^2}+O(\gamma_i^2)\ \ \text{(c)}, \qquad\text{(2.14)}
```

From 07-ilang-weight/03-weight-of-mark@v2. Setting there: a held body ($`\tau=0`$) at $`x`$ with coupling (a) or the full grip (at $`\tau=0`$ couplings (a) and (c) coincide), $`\theta=1`$ for (a) and $`0`$ for the full grip, $`g_b=\sigma\gamma M_k`$, $`\varepsilon_0(g)`$ the lowest eigenvalue of $`C_1+gP_x`$, $`\eta(g_b)`$ its scaled shift, $`\ell=\Lambda^+`$ the pseudo-inverse of the graph Laplacian, $`\ell^{(2)}=(\Lambda^+)^2`$, $`[\cdot]`$ the difference between the places $`x`$ and $`x'`$ of a function of $`r=x_s-x`$, $`\lvert X_f\rvert=L`$ on the ring, $`\delta N`$ the first-order change of the field density made by the source; a held source $`g_sP_{x_s}`$ for the weight.

Eq. (3.4) of 07-ilang-weight/03-weight-of-mark:

```math
\mathrm{Cost}_{k,\sigma}=\theta\sigma M_k+C^{\rm mark}_{k,\sigma},\qquad C^{\rm mark}_{k,\sigma}:=N_f\bigl[\varepsilon_0(g_b)-\varepsilon_0(0)\bigr]=n\,t_f\,\eta(g_b),\qquad\text{(3.4)}
```

Eq. (3.12) of 07-ilang-weight/03-weight-of-mark:

```math
\Delta W_{k,\sigma}=\mathcal W_{x,x'}\bigl(C^{\rm mark}_{k,\sigma}\bigr)+O(g_s^2),\qquad\text{(3.12)}
```

Eq. (3.13) of 07-ilang-weight/03-weight-of-mark:

```math
\mathcal W(C)=FC+F_2C^2+F_3C^3+O(C^4),\qquad F=-\frac{2g_s}{t_f}[\ell]=\frac{[\delta N]}n,\quad F_2=\frac{g_s}{nt_f^2}\Bigl[\ell^2-\frac{2\ell^{(2)}}{\lvert X_f\rvert}\Bigr],\quad F_3=\frac{2g_s}{n^2t_f^3\lvert X_f\rvert}\Bigl[\ell\,\ell^{(2)}+\ell^{(2)}_0\ell-\frac{\ell^{(3)}}{\lvert X_f\rvert}\Bigr].\qquad\text{(3.13)}
```

From 06-ilang-source/07-dressed-fall@v2. Setting there: one body with its own mark (coupling (a) or (c), constant $`\gamma`$, $`g_b:=\sigma\gamma M_k`$) and a held source $`g_s\Phi_{x_s}`$ on the ring; $`W_{k,\sigma}(x)`$ the weight of the held body ($`\tau=0`$) at $`x`$; in (7.7) a start with real envelope $`\phi_j`$ in an isolated band, the coefficient of $`\tau^2`$ at first order in $`g_s`$.

Eq. (7.7) of 06-ilang-source/07-dressed-fall:

```math
a_{k,\sigma}(0)=-E''_{k,\sigma}(0)\sum_j\phi_{j+1}\phi_{j-1}\,W'_{k,\sigma}(j)+O(g_s^2)+O(\tau^4\gamma g_s).
\qquad\text{(7.7)}
```

## Assumptions

- The setting under "Goal". The field, the body, the couplings, the field state and the regime of item 1 are assumptions of the package (M8, M9).
- Standard mathematics applied to the stated operators may be used (perturbation theory for an isolated eigenvalue, Fourier analysis on the ring); state it with its conditions.

## Scope

- **Class.** The three couplings, $`N_f\ge1`$, $`L\ge5`$, every level and both branches, in the stated regime.
- **Control.** For each answer of items 2 and 3, a description of the class, or of a stated wider class, in which it fails, or a proof that there is none.
- Out of scope: the tori; the highest field state; the full grip in the form of (c); bound pairs (06-inertia-of-pair and later packages); the speed of a front of the field (item 4 of the base problem).

## Depth

- Item 1: derive (needed by items 2–3 and by the later package on a bound pair with the full grip).
- Item 2: derive for the full grip; short argument from the quoted (2.14), (6.10), (6.12) for (a) and (c) where they settle the answer, derive beyond (needed by item 3 of the base problem: inertia against cost).
- Item 3: derive (needed by item 3 of the base problem: weight over inertia, and by 06-inertia-of-pair as the single-body comparison).
- Item 4: short argument (needed by item 3 of the base problem: the role of the field).

## Expected result

- Item 1: an expression for $`E''_{k,\sigma}(0)`$ through the stated order, with the isolation condition.
- Item 2: for each coupling, a yes/no answer at leading order and at the next order, with the expression for $`v`$ where it exists.
- Item 3: for each coupling, a yes/no answer at leading order, with the order and size of the first level or branch dependence.
- Item 4: statements of the dependence on $`t_f`$ and $`L`$.

Give every main result a tag $`(5.k)`$.

Consistency checks, at most three: for example $`\gamma\to0`$ for (a) and (c) against (6.10), the full grip at mean field against a body with a rest term, and dimensions.

## Code

Required: check: for $`N_f=1`$ on a ring of at least two sizes, item 1 against the curvature of the exact dressed level of the full grip (the sector contract continued in $`P`$), for at least two levels and both branches where the level is isolated, and the ratios of items 2 and 3 against the same exact data.
