# Question: 04-profile

- **Subproject:** 06-ilang-source
- **Package:** 04-profile
- **Equation tags:** (4.k)
- **Created:** 2026-10-19

## Goal

For a stated class of field objects, determine how the mutual cost of two held sources depends on their distance and on the structure of the field (its places, its contract, its number of field objects and the dimension of its graph), which field contracts give a long-range dependence, and what ties the places of the field to the positions of the bodies. This is item 3 of the base problem.

**Setting.**
- **Field.** $`N_f\ge1`$ identical field objects of one type, invariant under swap ($`c=+1`$), with no pair terms among them. Each has the places $`X_f`$ of a finite connected graph $`\Gamma`$ and the own term $`C_1=-t_f\sum_{\{x,y\}\in E(\Gamma)}\bigl(\lvert x\rangle\langle y\rvert+\lvert y\rangle\langle x\rvert\bigr)`$, $`t_f>0`$. The field operator at the place $`x`$ is the number of field objects at $`x`$, $`\Phi_x=\sum_{j=1}^{N_f}\lvert x\rangle\langle x\rvert_j`$. The graphs studied: a ring of $`L`$ places, a square torus $`L\times L`$, a cubic torus $`L\times L\times L`$, nearest-neighbour edges.
- **Sources.** Two held bodies (A15) at field places $`x_1\neq x_2`$, in eigenvectors of their coupled operators with eigenvalues $`g_1`$, $`g_2`$, coupled by $`g_i\Phi_{x_i}`$; no other contracts.
- **State of the field** (an assumption, M9): the eigenvector of the field contract with the sources that is connected to the lowest eigenvector of the field contract without them (the *lowest state*). Control state: the one connected to the highest eigenvector.
- **Distance.** $`d`$ is the graph distance in $`\Gamma`$; on the tori, $`\mathbf d=x_1-x_2`$ is the difference vector.
- **Mutual cost** as in 03-held-sources: the part of the field cost that depends on both $`g_1`$ and $`g_2`$.

1. **Mutual cost at second order.** In the lowest state, through second order in $`(g_1,g_2)`$: determine the mutual cost as a function of $`x_1`$, $`x_2`$ in terms of the single-object contract on $`\Gamma`$; give its closed form on the ring as a function of $`d`$ and $`L`$, and its form on the square and the cubic torus for $`1\ll\lvert\mathbf d\rvert\ll L`$; state its dependence on $`N_f`$, $`t_f`$, $`L`$, and at fixed density $`n:=N_f/\lvert X_f\rvert`$; state its sign for $`g_1g_2>0`$.
2. **Range.** Determine the range of $`g_i`$, $`t_f`$, $`L`$ and $`n`$ in which the second-order form holds to a stated relative accuracy, and, for one field object on the ring, the exact lowest eigenvalue with the two sources as a function of $`d`$, against the second-order form.
3. **Control state and control field.** Determine the mutual cost in the highest state. Give a field contract of a different kind within A1 (for example cells with one gapped degree of freedom per place, coupled to their neighbours) whose mutual cost in its lowest state falls off faster than any power of $`d`$, with its decay length.
4. **Field places and body positions.** Let the bodies be recorded on a chain as in (17.15), and let the coupling map the position label $`m`$ of a body to the field place $`\pi(m)`$ of a ring. Determine the condition on $`\pi`$ under which the mutual cost is the same function of the distance $`d_0`$ of 03-ilang-space as of the graph distance (up to a constant factor), and give a map that fails it.

## Inputs

From 03-ilang-space/17-motion@v2. Setting there: $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$; the start is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, $`\lvert u_h\rangle:=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$, $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$; with $`p_h(\lambda)`$ the place weights of the view of $`b`$, $`\bar x(\lambda):=\sum_hp_h(\lambda)\,u_h`$.

Eq. (17.15) of 03-ilang-space/17-motion, for the chain $`h_m`$, $`m\in\mathbb Z`$, with $`K_{h_m}=m\,X`$, $`X`$ self-adjoint on $`\mathcal H_c`$, $`\sigma_X:=(\langle X^2\rangle-\langle X\rangle^2)^{1/2}>0`$ and $`e:=(X-\langle X\rangle)\chi`$, so that $`\lVert e\rVert=\sigma_X`$ and $`u_{h_m}=m\,e`$:

```math
d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X,\qquad \bar x=\bar m\,e,\quad \bar m:=\sum_mm\,p_{h_m},\qquad s^2=\sigma_X^2\sum_m(m-\bar m)^2p_{h_m} .
```

## Assumptions

- The setting under "Goal". The field type, its contract, the graphs, the held bodies, the coupling map and the lowest and highest states are assumptions of the package (M8, M9).
- Standard perturbation theory for an isolated eigenvalue, standard facts on the spectra of graph matrices and on lattice sums, and standard asymptotic expansions may be used with their conditions stated. No field equation or Green function of a field theory is an input (M4); whatever is needed is derived for the stated matrices.

## Scope

- **Class.** Items 1–2: every $`N_f\ge1`$, $`t_f>0`$, the three graph families, every $`x_1\neq x_2`$. Item 3: the highest state, and one field of another kind. Item 4: bodies on a chain and a ring field.
- **Control.** Item 3 (highest state; a field with short range); item 4 (a map that fails).
- Out of scope: what a body presents (02-what-a-body-presents); the general sum rules over all states (03-held-sources); moving sources; the fall of a test body; records of more than one dimension.

## Depth

- Item 1: derive (needed by item 4 of the base problem, the made field as a scale, and by item 8).
- Item 2: short argument (needed by every later package that uses the second-order form).
- Item 3: short argument (needed by item 8 of the base problem).
- Item 4: short argument (needed by item 3 of the base problem: what ties the field to the positions).

## Expected result

- Item 1: an expression in the single-object contract; a closed form on the ring; leading forms on the two tori; dependences and a sign.
- Item 2: inequalities; an exact eigenvalue equation or closed form.
- Item 3: a mutual cost in the highest state; a field with its decay length.
- Item 4: a condition on the map; a counterexample.

Give every main result a tag $`(4.k)`$.

Consistency checks, at most three: for example $`g_2=0`$, the ring with $`L=2`$ or $`3`$, and the sum over the two ends of the spectrum.

## Code

Required: check: (i) the second-order mutual cost computed numerically from the single-object contract against the closed form on rings of at least two sizes, and against the leading forms on square and cubic tori (at least two sizes each, with the range of $`\lvert\mathbf d\rvert`$ used and the size of the deviation); (ii) for one field object on a ring, the exact lowest eigenvalue with the two sources against the second-order form, at several values of $`g_i L/t_f`$; (iii) the decay of the control field of item 3 on a chain of stated length.
