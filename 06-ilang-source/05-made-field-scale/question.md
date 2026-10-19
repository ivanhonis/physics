# Question: 05-made-field-scale

- **Subproject:** 06-ilang-source
- **Package:** 05-made-field-scale
- **Equation tags:** (5.k)
- **Created:** 2026-10-19

## Goal

Determine whether the field made by a held source acts on a test body as a common local scale: the effective contract of a test body in that field, whether its effective on-site blocks change from place to place in proportion to their gaps (the requirement R3 of 05-ilang-free-fall), the place dependence of its clock rate and of its fall from rest, and their dependence on the distance from the source. This is item 4 of the base problem. Every result is stated through quantities that the total contract and the state fix (M6): effective blocks and their differences between places, ratios of level spacings, accelerations.

**Setting.**
- **Field.** The class of 04-profile: $`N_f\ge1`$ identical field objects ($`c=+1`$), no pair terms among them, each with the places $`X_f`$ of a ring of $`L`$ places, a square torus or a cubic torus, own term $`C_1=-t_f\sum_{\{x,y\}}(\lvert x\rangle\langle y\rvert+\lvert y\rangle\langle x\rvert)`$, and $`\Phi_x`$ the number of field objects at $`x`$; $`n:=N_f/\lvert X_f\rvert`$.
- **Source.** One held body $`s`$ (A15) at the place $`x_s`$, in an eigenvector of its coupled operator with eigenvalue $`g_s`$, coupled by $`g_s\Phi_{x_s}`$. **State of the field** (an assumption, M9): the lowest state adapted to the source, as in 04-profile.
- **Test body.** A Model D body $`b`$ (base problem, "Notation and conventions"; $`M_k:=m+d_k`$ is the half-gap of level $`k`$), recorded by a medium with $`K_x=\kappa\,x\,X`$, whose position labels are the places of one line of the field graph (on the ring: all its places), coupled to the same field with a coupling constant $`\gamma`$, in one of the two forms of 02-what-a-body-presents: (a) $`\gamma\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m\mathbb 1_N+D)\otimes\Phi_x`$ (rest and clock term); (c) the same plus $`\gamma`$ times the motion term with the factor $`\frac12(\Phi_x+\Phi_{x+1})`$ on the bond $`(x,x+1)`$ (whole contract). *Test body*: its own change of the field is neglected at the order stated (A15); the order is to be stated.
- **R3** (05-ilang-free-fall/17-typical-or-forced, quoted under "Inputs"): with $`B_{x,k}:=M_{x,k}\sigma_3+V_{x,k}\mathbb 1_2`$ the effective on-site block of level $`k`$ at $`x`$, there is a level-independent operator $`\Gamma`$ on the branch label with $`B_{x+1,k}-B_{x,k}=M_k\Gamma`$ for every $`k`$. Here it is asked place by place: $`\Gamma`$ may depend on $`x`$.

1. **Effective contract of the test body.** For each coupling, at first order in $`\gamma`$ (with the remainder and its range in $`\lambda`$ stated): determine the operator by which the test body evolves in the field state of the setting, and its level blocks (on-site blocks and hopping) as functions of the place, in terms of the expectation $`\langle\Phi_x\rangle`$ in that state. State which part of the result is fixed by the total contract and the state, and which depends on the listing (M6; for example a place-independent shift of the blocks).
2. **Common local scale.** For each coupling: determine whether the effective on-site blocks of item 1 satisfy R3 at every place (with $`\Gamma(x)`$ allowed to depend on $`x`$), and whether the hopping of level $`k`$ changes from place to place by the same factor as the on-site blocks. Give a coupling of the same form (a pair term of the body with the $`\Phi_x`$) for which R3 fails.
3. **Clock rate and fall.** For each coupling, in the profile of item 1: determine the ratio of the level spacings of the upper on-site eigenvalues at two places (the clock-rate ratio of 05-ilang-free-fall), and the drift acceleration from rest of a branch start, for every level, in the approximation in which the profile is linear across the start (state the conditions of that approximation); determine whether the acceleration is the same for all levels and whether the relation (4.24) holds between it and the clock-rate ratio.
4. **Distance from the source.** With the made field of the setting at second order in the coupling of the source ((3.9) with the response of the lowest state, (4.4)): determine the acceleration of item 3 and the clock-rate ratio as functions of the place of the test body relative to the source, on the ring and, for the leading forms, on the square and the cubic torus; state their sign for $`g_s\gamma>0`$ and $`g_s\gamma<0`$ (towards or away from the source; slower or faster near it).

**Note (2026-10-19, after external round 1).** In item 4, "place relative to the source" and "towards or away from the source" are positions in the field graph (graph coordinates, graph separation). The record contract $`K_x=\kappa\,x\,X`$ fixes a recorded geometry only along the test body's line; where graph separation and recorded distance coincide, and where they do not (for example the closing bond of the ring, the transverse separation on the tori), is to be stated.

## Inputs

From 02-what-a-body-presents@v3 (this subproject). Setting there: the two couplings (a), (c) above; $`\Pi_x:=\lvert x\rangle\langle x\rvert\otimes\mathbb 1_2\otimes\mathbb 1_N`$, $`O:=\sigma_3\otimes(m\mathbb 1_N+D)`$, $`A_x`$ the bond $`(x,x+1)`$ of the motion term of Model D, $`A=\sum_xA_x`$, $`B=\sum_x\Pi_xO`$.

Eq. (2.1) of 02-what-a-body-presents:

```math
C_{bf}=\gamma\sum_xQ_x\otimes\Phi_x,\qquad Q^{(a)}_x=\Pi_xO,\qquad Q^{(c)}_x=\Pi_xO+\tfrac12\bigl(A_x+A_{x-1}\bigr). \qquad\text{(2.1)}
```

From 03-held-sources@v4 (this subproject). Setting there: a field object with contract $`C_f`$ (eigenvectors $`\varphi_n`$, eigenvalues $`e_n`$) and operators $`\Phi_x`$; held sources $`g_i\Phi_{x_i}`$, $`V:=g_1\Phi_{x_1}+g_2\Phi_{x_2}`$, $`v`$ its size, $`\Delta_n`$ the gap of $`e_n`$, $`\bar\Phi_n(y):=\langle\varphi_n\vert\Phi_y\vert\varphi_n\rangle`$; $`\varphi_n(g)`$ the adapted eigenvector.

Eq. (3.6) of 03-held-sources:

```math
Q_n=\sum_{m:\,e_m\neq e_n}\frac{\lvert\varphi_m\rangle\langle\varphi_m\rvert}{e_m-e_n},\qquad
\chi_n(x,y)=\langle\varphi_n\vert\Phi_xQ_n\Phi_y+\Phi_yQ_n\Phi_x\vert\varphi_n\rangle
=\sum_{m:\,e_m\neq e_n}\frac{2\mathrm{Re}\bigl(\langle\varphi_n\vert\Phi_x\vert\varphi_m\rangle\langle\varphi_m\vert\Phi_y\vert\varphi_n\rangle\bigr)}{e_m-e_n}.
```

Eq. (3.9) of 03-held-sources:

```math
\langle\varphi_n(g)\vert\Phi_y\vert\varphi_n(g)\rangle=\bar\Phi_n(y)+\delta N_n^{(1)}(y)+\delta N_n^{(2)}(y)+O\Bigl(\frac{\lVert\Phi_y\rVert v^2}{\Delta_n^2}\Bigr),\qquad \delta N_n^{(i)}(y)=-g_i\,\chi_n(y,x_i).
```

From 04-profile@v4 (this subproject). Setting there: the field class of the setting above, two held sources, lowest state; $`\Lambda`$ the graph Laplacian, $`\Lambda^+`$ its pseudo-inverse; on the three graph families the single-object lowest eigenvector is uniform and the reduced resolvent is $`\Lambda^+/t_f`$.

Eq. (4.4) of 04-profile:

```math
M^{(2)}(x_1,x_2)=-\frac{2n\,g_1g_2}{t_f}\,\Lambda^+(x_1,x_2),\qquad \Lambda^+(x,y)=\frac1{\lvert X_f\rvert}\sum_{\mathbf k\neq0}\frac{e^{i\mathbf k\cdot(x-y)}}{\omega(\mathbf k)},\quad \omega(\mathbf k)=\sum_{\mu=1}^{D}4\sin^2\frac{k_\mu}2,\qquad \sum_{x_2\in X_f}M^{(2)}(x_1,x_2)=0,\qquad\text{(4.4)}
```

From 05-ilang-free-fall/17-typical-or-forced@v3. Setting there: one Model D body, linear level profiles $`M_{x,k}=M_k+G_kx`$, $`V_{x,k}=-\mathcal F_kx`$ with $`G_k=mg_m+d_kg_\eta`$, $`\mathcal F_k=\mathcal F+d_k\mathcal F_1`$; R3 and R3$`^+`$ as under "Goal" (R3$`^+`$: $`E^+_{x+1,k}-E^+_{x,k}=\gamma_+M_k`$ with one real $`\gamma_+`$); the numbers $`\gamma`$, $`\phi`$ in (17.11) are the coefficients of $`\Gamma=\gamma\sigma_3-\phi\mathbb 1_2`$ there, not the coupling constant $`\gamma`$ of the setting above; $`\ell_+:=\mathcal F/m-g_m+g_\eta-\mathcal F_1`$; $`\mathcal U_4^{\pm}`$, $`\mathcal U_4^{+}`$, $`\mathcal U_5`$ the sets on which the fall from rest is level-independent on both branches, on the upper branch, and on which (4.24) holds with a nonzero fall.

Eq. (17.11) of 05-ilang-free-fall/17-typical-or-forced:

```math
\text{R3}\iff G_k=\gamma M_k,\ \mathcal F_k=\phi M_k\ \forall k\iff g_m=g_\eta=\gamma,\ \mathcal F_1=\phi,\ \mathcal F=m\phi\iff\boldsymbol g\in\mathcal U_4^{\pm};\qquad
\text{R3}^+\iff\ell_+=0\iff\boldsymbol g\in\mathcal U_4^{+},
```

From 05-ilang-free-fall/04-branch-fall@v3. Setting there: level blocks with linear level profiles $`M_{x,k}=M_k+G_kx`$, $`V_{x,k}=-\mathcal F_kx`$, hopping $`\tau_k\zeta_{x,k}`$; branch start at rest; first order in the gradients; in the background of (17.15) of 03-ilang-space/17-motion, $`d_0=\kappa\sigma_X`$, $`v_{\max}=\tau d_0`$, $`\hat e`$ the direction of the record vectors; $`r(x)`$ the clock rate at $`x`$.

Eq. (4.16) of 05-ilang-free-fall/04-branch-fall:

```math
\boxed{\;a_{k,\sigma}(0)=\frac{\tau_k^2}{M_k}\,\bigl(\sigma\,\mathcal F_k-G_k\bigr)\;}
```

Eq. (4.24) of 05-ilang-free-fall/04-branch-fall:

```math
\boxed{\;\frac{\mathrm d^2\bar x}{\mathrm d\lambda^2}\Big\vert_{\rm drift}=d_0\,a_{k,+}(0)\,\hat e=-\,\frac{v_{\max}^2}{d_0}\;\frac{r(x+1)-r(x)}{r(x)}\;\hat e\;}
```

## Assumptions

- The setting under "Goal". The field class, the held source, the lowest adapted state, the test body, its two couplings and its starts are assumptions of the package (M8, M9).
- The test body neglects its own change of the field at the order stated (A15); its own mark is item 5 of the base problem (06-own-mark), out of scope here.

## Scope

- **Class.** Items 1–3: both couplings, every field state in which $`\langle\Phi_x\rangle`$ is defined, then the lowest adapted state; item 4: the made field at second order in $`g_s`$ on the three graph families.
- **Control.** Item 2 asks for a coupling for which R3 fails.
- Out of scope: the test body's own mark; second order in $`\gamma`$; motion of the source; fields in other states except where named; profiles of the made field beyond the local-slope approximation in item 3 (state where that approximation fails).

## Depth

- Item 1: derive (needed by items 2–4 and by 06-own-mark).
- Item 2: derive (the answer to item 4 of the base problem: is the made field a common local scale).
- Item 3: short argument (needed by item 4 of the base problem: clock rate and fall in the made field).
- Item 4: short argument (needed by items 3 and 4 of the base problem: sign and distance of the fall towards a source).

## Expected result

- Item 1: an effective operator with its level blocks, a remainder, and a statement on what is fixed by $`C`$ and the state.
- Item 2: two yes/no answers for each coupling, with $`\Gamma(x)`$ where it exists; a control.
- Item 3: a ratio of spacings and an acceleration for each coupling; yes/no answers on level independence and on (4.24), with conditions.
- Item 4: functions of the place on the ring and leading forms on the tori; signs.

Give every main result a tag $`(5.k)`$.

Consistency checks, at most three: for example $`g_s=0`$, $`\gamma=0`$, and a field state in which all $`\Phi_x`$ are sharp (05-ilang-free-fall's sharp field).

## Code

None.
