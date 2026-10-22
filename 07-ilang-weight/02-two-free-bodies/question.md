# Question: 02-two-free-bodies

- **Subproject:** 07-ilang-weight
- **Package:** 02-two-free-bodies
- **Equation tags:** (2.k)
- **Created:** 2026-10-20

## Goal

Determine how two bodies move under the field they make, when there is no pair term between them: which quantities of bodies and field are conserved, how the strength with which one body acts on the other is related to the strength with which it is acted upon, and how the accelerations of the two bodies from rest are related to their inertias. This is item 1 of the base problem. Every result is stated through quantities that the total contract and the state fix (M6).

**Setting.**
- **Field.** The class of 06-ilang-source/04-profile on a ring of $`L`$ places: $`N_f\ge1`$ identical field objects ($`c=+1`$), no pair terms among them, own term $`C_1=-t_f\sum_x(\lvert x\rangle\langle x+1\rvert+\lvert x+1\rangle\langle x\rvert)`$, $`t_f>0`$, $`\Phi_x`$ the number of field objects at $`x`$, $`n:=N_f/L`$.
- **Bodies.** Two Model D bodies $`b_1,b_2`$ (base problem, "Notation and conventions") on the same ring of position labels, possibly of different types (parameters $`\tau_i`$, $`m_i`$, clock levels $`k_i`$ with half-gaps $`M_{k_i}^{(i)}`$), each coupled to the field by coupling (a) or (c) of the base problem with its own constant $`\gamma_i`$. There is no pair term between $`b_1`$ and $`b_2`$. Records at $`\kappa\to0`$.
- **Held bodies** (A15): the same bodies with $`\tau_i=0`$ at fixed position labels $`x_1,x_2`$.
- **State of the field** (assumption, M9): the lowest state adapted to the bodies present, and, where asked, the highest.

1. **Conserved quantities.** Determine the operators built from places that commute with the total contract (in particular a joint translation of both bodies and all field objects), and the quantity of bodies and field that is conserved with it. State what is conserved by the bodies alone, if anything.
2. **Acting and acted upon.** For the held bodies: determine the dependence of the eigenvalue of the total contract connected (as $`\gamma_1,\gamma_2\to0`$) to the bodies in their internal states with the field in its lowest state, on the two position labels; whether it depends on them only through their separation, and whether it is unchanged when the roles of the two bodies are exchanged (the strength with which $`b_1`$ acts on $`b_2`$ against the strength with which $`b_2`$ acts on $`b_1`$); at every order in the couplings, or to which order. Determine whether it is, at second order and at the next order, a product of one number for each body and one function of the separation.
3. **Mutual fall.** For the free bodies: in a regime to be stated and named as an assumption (band dynamics in isolated dressed levels; the order in $`\tau_i`$; the class of starts), determine the drift accelerations from rest of the mean positions of both bodies, at first order in the place dependence of item 2, and the ratio of the two accelerations; relate the ratio to the inertias of the dressed bodies (quoted (6.10) of 06-ilang-source/06-own-mark) and to their rest costs; state for which branches of the two bodies and for which field state (lowest, highest) they move towards each other, and the first order at which the ratio deviates from a ratio of inertias, if it does.

**Note (2026-10-20, after external round 1).** Two restrictions, with the reason that item 1 of the base problem needs the mutual motion and its relation to the inertias, not every symmetry case. (i) Item 3 is asked for two bodies of different types (distinguishable objects, Law 5 imposes no symmetry between them); bodies of one type are asked only in item 2, where the eigenvalue depends on the set of the two held bodies. (ii) The highest field state is asked for even $`L`$ only (through the mirror); odd $`L`$ is out of scope. The mean position on the ring is to be defined so that it is a well-defined observable for the starts and the range of $`\lambda`$ used (for example a local chart away from the place where the labels close).

## Inputs

From 06-ilang-source/04-profile@v4. Setting there: the field class of the setting above, held sources $`g_i\Phi_{x_i}`$ at $`x_1`$, $`x_2`$; $`h(g)`$ the one-object contract with the sources, $`\varepsilon_0(g)`$ its lowest eigenvalue; on the ring the one-object lowest eigenvector is uniform and the reduced resolvent is $`\Lambda^+/t_f`$, $`\Lambda^+`$ the pseudo-inverse of the ring Laplacian.

Eq. (4.2) of 06-ilang-source/04-profile:

```math
E(g)=N_f\,\varepsilon_0(g),\qquad M=N_f\bigl[\varepsilon_0(g_1,g_2)-\varepsilon_0(g_1,0)-\varepsilon_0(0,g_2)+\varepsilon_0(0,0)\bigr].\qquad\text{(4.2)}
```

Eq. (4.4) of 06-ilang-source/04-profile:

```math
M^{(2)}(x_1,x_2)=-\frac{2n\,g_1g_2}{t_f}\,\Lambda^+(x_1,x_2),\qquad \Lambda^+(x,y)=\frac1{\lvert X_f\rvert}\sum_{\mathbf k\neq0}\frac{e^{i\mathbf k\cdot(x-y)}}{\omega(\mathbf k)},\quad \omega(\mathbf k)=\sum_{\mu=1}^{D}4\sin^2\frac{k_\mu}2,\qquad \sum_{x_2\in X_f}M^{(2)}(x_1,x_2)=0,\qquad\text{(4.4)}
```

From 06-ilang-source/06-own-mark@v3. Setting there: one body of the setting above with coupling (a) or (c) and constant $`\gamma`$, no source; $`E_{k,\sigma}(P)`$ the dressed level (eigenvalue of the total contract in the sector of clock level $`k`$ and total plane-wave label $`P`$ of body and field, connected to the branch start $`(P,\sigma,k)`$ with the field in its lowest state); $`G_{k,\sigma}(P,q)`$ the second-order kernel of that package; isolation condition (6.4) there.

Eq. (6.10) of 06-ilang-source/06-own-mark:

```math
E''_{k,\sigma}(0)=\sigma\frac{\tau^2}{M_k}\times\begin{cases}1-\gamma n+\gamma^2n^2&\text{(a)}\\ 1+\gamma n&\text{(c)}\end{cases}+\Delta''_{k,\sigma}+O(\gamma^3),\qquad \Delta''_{k,\sigma}:=\gamma^2\frac nL\sum_{q\ne0}\partial_P^2G_{k,\sigma}(P,q)\big|_{P=0}.\qquad\text{(6.10)}
```

From 06-ilang-source/07-dressed-fall@v2. Setting there: one body with its own mark (coupling (a) or (c), constant $`\gamma`$, $`g_b:=\sigma\gamma M_k`$) and a held source $`g_s\Phi_{x_s}`$ on the ring; $`W_{k,\sigma}(x)`$ the weight of the held body ($`\tau=0`$) at $`x`$; $`P_y:=\lvert y\rangle\langle y\rvert`$; in (7.7) a start with real envelope $`\phi_j`$ in an isolated band, the coefficient of $`\tau^2`$ at first order in $`g_s`$.

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

Eq. (7.7) of 06-ilang-source/07-dressed-fall:

```math
a_{k,\sigma}(0)=-E''_{k,\sigma}(0)\sum_j\phi_{j+1}\phi_{j-1}\,W'_{k,\sigma}(j)+O(g_s^2)+O(\tau^4\gamma g_s).
\qquad\text{(7.7)}
```

## Assumptions

- The setting under "Goal". The field class, the bodies, their couplings, the field state and the regime of item 3 are assumptions of the package (M8, M9).
- Standard mathematics applied to the stated operators may be used (perturbation theory for an isolated eigenvalue, Fourier analysis on the ring); state it with its conditions.

## Scope

- **Class.** Both couplings, $`N_f\ge1`$, $`L\ge5`$, every pair of levels and branches; item 3 in the stated regime.
- **Control.** For each answer of items 2 and 3, a description of the class, or of a stated wider class, in which it fails, or a proof that there is none.
- Out of scope: the tori; bound pairs (04-weight-of-bond and later packages); the inertia of a bound pair; moving sources beyond the two bodies.

## Depth

- Item 1: derive (needed by items 2–3 and by item 1 of the base problem).
- Item 2: derive (needed by item 1 of the base problem: acting and acted upon).
- Item 3: derive (needed by item 1 of the base problem: accelerations against inertias).

## Expected result

- Item 1: a list of conserved quantities with the operators that give them.
- Item 2: a statement on the dependence on the positions, a yes/no answer on the exchange symmetry with its order, and a yes/no answer on the product form at each order.
- Item 3: expressions for the two accelerations and their ratio, with the regime; the branch and state conditions; the first order of a deviation, if any.

Give every main result a tag $`(2.k)`$.

Consistency checks, at most three: for example a held body against (7.2), $`\gamma_2\to0`$ (test body), and equal bodies.

## Code

Required: check: for $`N_f=1`$ on a ring of at least two sizes, item 2 against the exact lowest eigenvalue with two held point terms for unequal bodies, and item 3 against a joint evolution of two bodies and the field object from rest (accelerations and their ratio) for at least two pairs of parameters, with the deviation stated.
