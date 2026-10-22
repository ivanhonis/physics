# Question: 04-weight-of-bond

- **Subproject:** 07-ilang-weight
- **Package:** 04-weight-of-bond
- **Equation tags:** (4.k)
- **Created:** 2026-10-20

## Goal

Determine whether the cost of a bond that two bodies make through the field, without a pair term between them, is weighed in the field of a distant source in the same way as the costs of the bodies themselves. This is item 2 of the base problem, for bonds. Every result is stated through quantities that the total contract fixes (M6): eigenvalues of the total contract and their dependence on the places of held bodies.

**Setting.**
- **Field.** The class of 06-ilang-source/04-profile: $`N_f\ge1`$ identical field objects ($`c=+1`$), no pair terms among them, on a ring of $`L`$ places, a square torus or a cubic torus of side $`L`$; own term $`C_1=-t_f\sum_{\{x,y\}}(\lvert x\rangle\langle y\rvert+\lvert y\rangle\langle x\rvert)`$, $`t_f>0`$; $`\Phi_x`$ the number of field objects at $`x`$; $`n:=N_f/\lvert X_f\rvert`$. **State** (assumption, M9): the lowest state adapted to the bodies present, and the highest where it is mirrored.
- **Pair.** Two held Model D bodies (A15: $`\tau=0`$) at position labels $`x_1,x_2`$ with separation vector $`\mathbf r:=x_2-x_1`$, on levels $`k_1,k_2`$ and branches $`\sigma_1,\sigma_2`$ (half-gaps $`M^{(1)}_{k_1}`$, $`M^{(2)}_{k_2}`$), each coupled to the field by coupling (a) or by the full grip of the base problem ("Couplings"), with constants $`\gamma_1,\gamma_2`$. There is no pair term between them. The *place* of the pair is $`x_1`$ at fixed $`\mathbf r`$.
- **Source.** One held body at $`x_s`$, coupled by $`g_s\Phi_{x_s}`$, far from the pair; first order in $`g_s`$.
- **Quantities.** The eigenvalue $`E(x_1,\mathbf r)`$ of the total contract connected (as the couplings go to zero) to the bodies in their internal states with the field in its lowest state. Its dependence on $`\mathbf r`$ without the source is the *bond profile*; its dependence on $`x_1`$ at fixed $`\mathbf r`$ with the source present is the *weight of the pair*.

1. **Bond.** Determine the bond profile $`E(x_1,\mathbf r)-E(x_1,\mathbf r')`$ without the source, through second order in the couplings and in closed form on the ring, with its leading forms on the tori; state which part of it is fixed by the total contract.
2. **Weight of the pair.** Determine the weight of the pair at first order in $`g_s`$, through the lowest order in the couplings at which it depends on $`\mathbf r`$, on the three graphs, with its form for a distance from the source large against $`\lvert\mathbf r\rvert`$; for comparison, determine in the same way the weight of each body alone.
3. **Is the bond weighed?** For both couplings and the three graphs: determine the part of the weight of the pair that depends on $`\mathbf r`$, and compare it with the bond profile times the function of the place by which the weight of a single body follows its cost in item 2; give the ratio of the two (the bond is weighed like the costs of the bodies when it is one), its dependence on the levels, branches, couplings, dimension and distances, and the range in which a statement holds.

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

From 06-ilang-source/07-dressed-fall@v2. Setting there: coupling (a) or (c), one held body at $`x`$ with $`g_b:=\sigma\gamma M_k`$, a held source at $`x_s`$ on the ring; $`P_y:=\lvert y\rangle\langle y\rvert`$; $`W_{k,\sigma}(x)`$ the weight of the held body; $`G:=\Lambda^+`$, $`G_0:=G(x,x)`$, $`(G^2)`$ the square of the matrix $`G`$; $`R_W=O(g_s^2)+O(g_sg_b^3)`$.

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

Eq. (7.3) of 06-ilang-source/07-dressed-fall:

```math
W_{k,\sigma}(x)=\text{const}-\frac{2ng_sg_b}{t_f}G(x,x_s)+\frac{ng_sg_b^2}{t_f^2}\Bigl[2G_0\,G(x,x_s)+G(x,x_s)^2-\frac2L(G^2)(x,x_s)\Bigr]+R_W,
\qquad\text{(7.3)}
```

## Assumptions

- The setting under "Goal". The field class, the held bodies, the couplings and the field state are assumptions of the package (M8, M9).
- Standard mathematics applied to the stated operators may be used (perturbation theory for an isolated eigenvalue, Fourier analysis and lattice sums on the three graphs); state it with its conditions.

## Scope

- **Class.** Both couplings, every $`N_f\ge1`$, every pair of levels and branches, equal and unequal bodies, the three graph families, first order in $`g_s`$.
- **Control.** For each answer of item 3, a description of the class, or of a stated wider class, in which it fails, or a proof that there is none.
- Out of scope: moving bodies, bound levels of free bodies and the inertia of a pair (later packages); the weight of a single body beyond what item 3 needs for comparison (03-weight-of-mark).

## Depth

- Item 1: derive (needed by item 3).
- Item 2: derive (needed by item 3).
- Item 3: derive (needed by item 2 of the base problem: whether a bond made through the field is weighed like the costs of the bodies).

## Expected result

- Item 1: an expression for the bond profile on the ring and leading forms on the tori.
- Item 2: an expression for the weight of the pair and of each body alone, with the large-distance forms.
- Item 3: the ratio of item 3 as a function of the stated parameters, with its range; a yes/no answer for each coupling and graph.

Give every main result a tag $`(4.k)`$.

Consistency checks, at most three: for example $`\gamma_2\to0`$ (one body), $`\lvert\mathbf r\rvert\to`$ large (independent bodies), and the sum of the weight over all places.

## Code

Required: check: for $`N_f=1`$, items 1–3 against the exact lowest eigenvalue of one field object with three point terms (the two bodies and the source), on a ring, a square torus and a cubic torus of at least two sizes each, for both couplings and two choices of levels and branches, with the scaling of the deviation in the couplings and in the distances.
