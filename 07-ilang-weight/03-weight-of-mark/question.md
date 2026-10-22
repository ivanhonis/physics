# Question: 03-weight-of-mark

- **Subproject:** 07-ilang-weight
- **Package:** 03-weight-of-mark
- **Equation tags:** (3.k)
- **Created:** 2026-10-20

## Goal

Determine whether a body with its own mark is weighed in the field of a distant source in proportion to its cost, for every clock level and both branches, and how this depends on the coupling and on the dimension of the field graph. This is item 2 of the base problem, for one body. Every result is stated through quantities that the total contract fixes (M6): eigenvalues of the total contract, their differences between descriptions and between places of held bodies.

**Setting.**
- **Field.** The class of 06-ilang-source/04-profile: $`N_f\ge1`$ identical field objects ($`c=+1`$), no pair terms among them, on a ring of $`L`$ places, a square torus or a cubic torus of side $`L`$; own term $`C_1=-t_f\sum_{\{x,y\}}(\lvert x\rangle\langle y\rvert+\lvert y\rangle\langle x\rvert)`$, $`t_f>0`$; $`\Phi_x`$ the number of field objects at $`x`$; $`n:=N_f/\lvert X_f\rvert`$. **State** (assumption, M9): the lowest state adapted to the bodies present, and the highest where it is mirrored.
- **Body.** One held Model D body (A15: $`\tau=0`$, position label $`x`$, clock level $`k`$, branch $`\sigma`$, half-gap $`M_k`$), coupled to the field by one of two couplings of the base problem ("Couplings"): coupling (a) (equal to (c) at $`\tau=0`$), and the full grip, in which the rest and clock term appears only in the pair term with the field. Coupling constant $`\gamma`$.
- **Source.** One held body at $`x_s`$, in an eigenvector of its coupled operator with eigenvalue $`g_s`$, coupled by $`g_s\Phi_{x_s}`$; first order in $`g_s`$.
- **Cost of the body** (definition of this package): the difference between the eigenvalue of the total contract connected (as the couplings go to zero) to the body in its internal state with the field in its lowest state, and the lowest eigenvalue of the description without the body, both without the source. **Weight**: the dependence of that eigenvalue on the place $`x`$ of the held body with the source present, as in (7.2) of 06-ilang-source/07-dressed-fall.

1. **Cost.** For both couplings: determine the cost of the body with its mark as a function of $`M_k`$, $`\sigma`$, $`\gamma`$, $`N_f`$, $`t_f`$ and the size, exactly where the one-object reduction of (4.2) applies, and its expansion through second order in $`\gamma`$; state which part of it is fixed by the total contract.
2. **Weight.** For both couplings: determine $`W_{k,\sigma}(x)-W_{k,\sigma}(x')`$ at first order in $`g_s`$, exactly in $`\gamma`$ where the reduction applies and through second order in $`\gamma`$ in closed form, on the ring, the square torus and the cubic torus; give the forms at large distance from the source.
3. **Weight against cost.** For both couplings and the three graphs: determine whether the weight difference equals the cost of the body times one function of the two places that is the same for all levels and both branches; at which order in $`\gamma`$ and in which range of distances it holds; if it does not, the first term that breaks it, its parameter and its dependence on the distance. Make the same comparison for the differences between two levels or two branches of the body (weight differences against cost differences), which the total contract fixes even where the cost of a single body is not fixed (M6).

## Inputs

From 06-ilang-source/04-profile@v4. Setting there: the field class of the setting above, held sources $`g_i\Phi_{x_i}`$ at $`x_1`$, $`x_2`$ at graph distance $`d`$; $`h(g)`$ the one-object contract with the sources, $`\varepsilon_0(g)`$ its lowest eigenvalue; $`\ell:=\Lambda^+`$ the pseudo-inverse of the graph Laplacian, $`\ell_d`$ its value at distance $`d`$, $`\ell^{(2)}:=(\Lambda^+)^2`$; lowest state.

Eq. (4.2) of 06-ilang-source/04-profile:

```math
E(g)=N_f\,\varepsilon_0(g),\qquad M=N_f\bigl[\varepsilon_0(g_1,g_2)-\varepsilon_0(g_1,0)-\varepsilon_0(0,g_2)+\varepsilon_0(0,0)\bigr].\qquad\text{(4.2)}
```

Eq. (4.4) of 06-ilang-source/04-profile:

```math
M^{(2)}(x_1,x_2)=-\frac{2n\,g_1g_2}{t_f}\,\Lambda^+(x_1,x_2),\qquad \Lambda^+(x,y)=\frac1{\lvert X_f\rvert}\sum_{\mathbf k\neq0}\frac{e^{i\mathbf k\cdot(x-y)}}{\omega(\mathbf k)},\quad \omega(\mathbf k)=\sum_{\mu=1}^{D}4\sin^2\frac{k_\mu}2,\qquad \sum_{x_2\in X_f}M^{(2)}(x_1,x_2)=0,\qquad\text{(4.4)}
```

Eq. (4.8) of 06-ilang-source/04-profile (third order, vertex-transitive graph, lowest state):

```math
M^{(3)}=\frac{N_f\,g_1g_2(g_1+g_2)}{\lvert X_f\rvert\,t_f^2}\Bigl[2\ell_0\ell_d+\ell_d^2-\frac{\ell^{(2)}_0+2\ell^{(2)}_d}{\lvert X_f\rvert}\Bigr].\qquad\text{(4.8)}
```

From 06-ilang-source/06-own-mark@v3. Setting there: one body with coupling (a) or (c) on the ring, no source; $`\varepsilon_0(g)`$ the lowest eigenvalue of one field object with a held point term $`g`$ at the body's place; $`S_0=\sum_{q\ne0}\varepsilon_q^{-1}=(L^2-1)/(12t_f)`$.

Eq. (6.7) of 06-ilang-source/06-own-mark:

```math
E_{k,\sigma}(P)\big|_{\tau=0}=\sigma M_k+N_f\,\varepsilon_0(\sigma\gamma M_k)\ \ \text{for all }P\ \text{and all }\gamma,\qquad N_f\varepsilon_0(g)=-2t_fN_f+gn-g^2\tfrac nLS_0+O(g^3).\qquad\text{(6.7)}
```

From 06-ilang-source/07-dressed-fall@v2. Setting there: coupling (a) or (c), held body at $`x`$ with $`g_b:=\sigma\gamma M_k`$, held source at $`x_s`$ on the ring; $`P_y:=\lvert y\rangle\langle y\rvert`$; $`G:=\Lambda^+`$, $`G_0:=G(x,x)`$; $`r`$ the distance of $`x`$ from $`x_s`$, $`u:=r(L-r)`$; $`\delta N(x):=-\frac{2ng_s}{t_f}\Lambda^+(x,x_s)`$ the first-order made field of the source; $`R_W=O(g_s^2)+O(g_sg_b^3)`$.

Eq. (7.1) of 06-ilang-source/07-dressed-fall:

```math
h_x:=C_1+g_bP_x+g_sP_{x_s}.
\qquad\text{(7.1)}
```

Eq. (7.2) of 06-ilang-source/07-dressed-fall:

```math
W_{k,\sigma}(x)-W_{k,\sigma}(x')=N_f\bigl[\varepsilon_0(x)-\varepsilon_0(x')\bigr],\qquad \varepsilon_0(x)=\min\mathrm{spec}h_x .
\qquad\text{(7.2)}
```

Eq. (7.6) of 06-ilang-source/07-dressed-fall:

```math
W_{k,\sigma}(x)-W_{k,\sigma}(x')=\sigma M_k\,\gamma\bigl[\delta N(x)-\delta N(x')\bigr]+M_k^2\gamma^2\bigl[\Theta(x)-\Theta(x')\bigr]+R_W,\qquad \Theta:=\frac{ng_s}{3L^2t_f^2}\Bigl(u^2-\frac{L^2-2}{2}\,u\Bigr).
\qquad\text{(7.6)}
```

## Assumptions

- The setting under "Goal". The field class, the held bodies, the couplings and the field state are assumptions of the package (M8, M9).
- Standard mathematics applied to the stated operators may be used (perturbation theory for an isolated eigenvalue, Fourier analysis and lattice sums on the three graphs); state it with its conditions.

## Scope

- **Class.** Both couplings, every $`N_f\ge1`$, every level and both branches, the three graph families, first order in $`g_s`$; the full $`\gamma`$ dependence where the one-object reduction gives it.
- **Control.** For each answer of item 3, a description of the class, or of a stated wider class, in which it fails, or a proof that there is none.
- Out of scope: moving bodies and inertia (later packages); bonds (04-weight-of-bond); field objects with pair terms among them.

## Depth

- Item 1: derive (needed by item 3).
- Item 2: derive (needed by item 3).
- Item 3: derive (needed by item 2 of the base problem: the weight of a body with its own mark against its cost).

## Expected result

- Item 1: an expression for the cost of the body, exact and expanded, for both couplings.
- Item 2: expressions for the weight difference on the three graphs, with large-distance forms.
- Item 3: a yes/no answer for each coupling and graph, with the order and the range of distances; the first breaking term otherwise.

Give every main result a tag $`(3.k)`$.

Consistency checks, at most three: for example the comparison with (7.6) on the ring for coupling (a), $`\gamma\to0`$, and the sum of the weight over all places.

## Code

Required: check: for $`N_f=1`$, the weight and the cost of item 1–3 against the exact lowest eigenvalue of one field object with the point terms of the body and the source, on a ring, a square torus and a cubic torus of at least two sizes each, for both couplings and two levels and both branches, with the scaling of the deviation in $`\gamma`$ and in the distance.
