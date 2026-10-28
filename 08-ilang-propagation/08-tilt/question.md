# Question: 08-tilt

- **Subproject:** 08-ilang-propagation
- **Package:** 08-tilt
- **Equation tags:** (8.k)
- **Created:** 2026-10-26

## Goal

Determine, for a field of exchange cells whose contract is unchanged by a common rotation of all cells: (1) whether a held term on one cell (a *push*) gives the lowest eigenvector an orientation that persists far from the push in a large field; (2) whether, at leading order in the inverse number of places, the small deviations from that orientation form the field of oscillator cells with a free uniform change and an anchor of 05-anchor, and which of its results carry over; (3) whether the mutual cost of two held sources has a long-range part, for sources that hold a fixed direction and for sources that enter only through terms unchanged by the common rotation. This is item 3 (the anchor) and item 4 (cells with finitely many places) of the base problem for exchange cells; the formation of the mark is the subject of 09-anchor-formation. Every result is stated through quantities that the total contract and the state fix (M6).

**Setting.**
- **Field** (assumption, M8). Exchange cells as in the base problem ("Field of cells"): one object with $`2S+1`$ places at each place $`x`$ of $`X_f`$, each object of its own type, with the matrices $`\mathbf S_x=(S^1_x,S^2_x,S^3_x)`$ of the irreducible representation of dimension $`2S+1`$ of $`\mathfrak{su}(2)`$. $`X_f`$ is a cubic torus ($`D=3`$, the main graph) or a ring ($`D=1`$) of even side $`L`$, so that its places split into two classes with signs $`\epsilon_x=\pm1`$ and every link joins the two classes. The contract is $`C_{\rm ex}=J\sum_{\langle xy\rangle}\mathbf S_x\cdot\mathbf S_y`$ with $`J>0`$, plus the terms of the push and of the sources below; $`J<0`$ enters only in item 1. The *common rotation* is $`U(\theta,\mathbf u)=\bigotimes_xe^{-i\theta\,\mathbf u\cdot\mathbf S_x}`$ for a unit vector $`\mathbf u`$; $`C_{\rm ex}`$ commutes with every $`U`$. Two neighbouring objects may form one cell (base problem); this is used only for the sources on two-object cells in item 3.
- **Push** (assumption, M8, A15; the anchor of the base problem for exchange cells). A held object coupled to the object at one place $`h`$, acting on it as $`-h_p\,\mathbf n\cdot\mathbf S_h`$, with $`h_p>0`$ and a fixed unit vector $`\mathbf n`$.
- **Direction sources** (assumption, M8, A15). Held objects, each acting on the object at a place $`x`$ as $`g\,\mathbf m\cdot\mathbf S_x`$ ($`g`$ real, $`\mathbf m`$ a fixed unit vector), or on a cell of two neighbouring objects $`x,x'`$ as $`g\,\mathbf m\cdot(\mathbf S_x-\mathbf S_{x'})`$ (a sum of two pair terms); transverse ($`\mathbf m\perp\mathbf n`$) or along the push ($`\mathbf m=\mathbf n`$).
- **Relation sources** (assumption, M8). (R1) A held object $`b`$ with $`2s_b+1`$ places ($`s_b\ge\frac12`$), of its own type, whose only term is $`g'\,\mathbf S_b\cdot\mathbf S_x`$ with the object at $`x`$: a pair term unchanged by the common rotation of the field and $`b`$ together. (R2) The description in which the term of one link $`\langle xy\rangle`$ has the coefficient $`J+\delta`$ instead of $`J`$. A held object cannot couple to an operator of two objects of the field without a term of three objects (A5). R1 and R2 are the sources unchanged by the common rotation that this package studies; other such pair terms (for example powers of $`\mathbf S_b\cdot\mathbf S_x`$) are out of scope.
- **State** (assumption, M9, A11). The lowest eigenvector of the stated total contract; it exists (A1). State its degeneracy where it matters.
- **Definitions.** The *staggered expectation* at $`x`$ is $`m(x)=\epsilon_x\langle\mathbf n\cdot\mathbf S_x\rangle`$ (for $`J<0`$ without $`\epsilon_x`$). The *mutual cost* of two sources is the part of the lowest eigenvalue that depends on both, at the lowest order in their strengths at which it does not vanish; name that order. It is *attractive* where it is negative and rises towards zero as the separation grows. Places are in lattice units (separations are cell separations, M2).

1. **Tilt by a push.** (a) For the field alone (no push, no sources), on both graphs: determine whether the lowest eigenvector is unique and whether it is unchanged by the common rotation; the same for $`J<0`$. (b) With the push: determine $`m(x)`$ at distance $`R`$ from $`h`$ in the lowest eigenvector, in the order $`L\to\infty`$, then $`R\to\infty`$, then $`h_p\to0`$, and in the order $`h_p\to0`$ at fixed $`L`$, then $`L\to\infty`$; at leading order in $`1/S`$ and at the first correction, on the cubic torus and on the ring; and for $`J<0`$. For $`S=\frac12`$, determine what exact diagonalization on the clusters of "Code" decides; an undecided answer is admissible if it is stated with its sizes.
2. **Small deviations.** At leading order in $`1/S`$ about the orientation $`\mathbf n`$, determine whether the total contract with the push and with transverse direction sources is, after an identification of operators and constants that you state, a field of oscillator cells of the class of 05-anchor (no pinning, an anchor, held sources); state how many copies, in which limit, and the conditions under which the deviations stay small. Give the identification of $`\kappa_h`$, $`\kappa_a`$, $`g_s`$ and of the read operator $`q_x`$. Then determine which of the quoted results of 05-anchor hold for exchange cells at this order under this identification, and where the boundedness of the common rotation (finitely many places, A1) or the next order in $`1/S`$ changes them.
3. **Long range for two kinds of sources.** On the cubic torus, in the lowest eigenvector with the push, in the order $`L\to\infty`$, then the distances of both sources to $`h`$ to infinity at fixed separation $`r`$, then $`r\to\infty`$: determine the mutual cost of two sources at large $`r`$, its law of decay in $`r`$ and its sign, (a) for direction sources, transverse and along $`\mathbf n`$, on single objects and on two-object cells; (b) for relation sources R1 and R2; each at the lowest order in $`1/S`$ and in the strengths at which it does not vanish. (c) Without a push: determine whether two sources of each kind fix the orientation of the lowest eigenvector themselves, and what that changes in (a) and (b).

## Inputs

From 08-ilang-propagation/05-anchor@v3 (same subproject). Setting there: oscillator cells on a ring or a cubic torus of side $`L\ge3`$ without pinning, $`H=\sum_x\frac12p_x^2+\frac{\kappa_h}2\sum_{\langle xy\rangle}(q_x-q_y)^2`$, $`\Phi_x=q_x`$, the compression $`C_M`$ with $`M\to\infty`$ first; the anchor $`\frac{\kappa_a}2q_h^2`$; held Model D bodies at places $`x_i`$ with grips $`F^{(i)}(q)=F_0^{(i)}+F_1^{(i)}q+F_2^{(i)}q^2`$ (class (G2)), in the block where $`S\to\mu_i=\sigma_iM_{k_i}`$, with $`\alpha_i:=2\mu_iF_2^{(i)}`$; held sources $`g_sq_{x_s}`$. In the block of the bodies the contract acts on the field as $`C_{\rm f}=\frac12p^{\rm T}p+\frac12q^{\rm T}Aq+b^{\rm T}q+c_0`$ with $`A=\kappa_h\Delta+\kappa_aP_h+\sum_i\alpha_iP_{x_i}`$ and $`b=\sum_i\mu_iF_1^{(i)}e_{x_i}+\sum_sg_se_{x_s}`$, $`\kappa_a=0`$ without an anchor; $`A_0`$ is $`A`$ with $`\kappa_a=0`$. $`\Delta`$ is the graph Laplacian, $`P_x`$ the projector onto the cell $`x`$, $`\mathcal L_n`$ the reduced Laplacian of the $`n`$ body places (Kron reduction), $`\mathcal A={\rm diag}(\alpha_i)`$, $`K_a=\kappa_h\Delta+\kappa_aP_h`$. $`g:=(\kappa_h\Delta)^+`$, $`r(x,y):=2[g(0)-g(x-y)]`$ (the resistance distance of the springs $`\kappa_h`$), $`r_{12}=r(x_1,x_2)`$, $`\Gamma_n`$ the matrix $`(G_a(x_i,x_j))`$. On the cubic torus as $`L\to\infty`$, $`g\to g_\infty`$ with $`g_\infty(0)=\gamma_3/\kappa_h`$, $`\gamma_3=0.2527310`$, $`g_\infty(x)=\frac1{4\pi\kappa_h\lvert x\rvert}+O(\lvert x\rvert^{-3})`$; $`c_\phi:=\frac1{\kappa_a}+\frac{\gamma_3}{\kappa_h}`$. The mutual cost of two sources is the part $`\propto g_1g_2`$ of the lowest eigenvalue.

Eq. (5.3) (criterion; the class above, the block of the stated body labels):

```math
\text{a lowest eigenvector exists }(M\to\infty)\iff A>0;\ \text{otherwise the lowest eigenvalue of }C_M\text{ tends to }-\infty\text{ or to the bottom of a continuum}.
\qquad\text{(5.3)}
```

Eqs. (5.4)–(5.6) (criterion without an anchor). Conditions stated with them in its Result: necessary $`\sum_i\mu_iF_2^{(i)}>0`$; (5.5) is one body with $`F_2\ne0`$, (5.6) two bodies; if no body has $`F_2\ne0`$ there is no lowest eigenvector ($`-\infty`$ if $`\sum_i\mu_iF_1^{(i)}+\sum_sg_s\ne0`$, a free uniform change otherwise); the field alone has none, so the cost of a body is undefined; the whole contract (all blocks) has none, for any bodies of (G2).

```math
A_0>0\iff\mathcal L_n+\mathcal A>0.
\qquad\text{(5.4)}
```

```math
\text{lowest eigenvector}\iff\mu F_2>0\iff\sigma={\rm sign}\,F_2\ (\text{every level }k);\quad\text{for }\sigma=-{\rm sign}\,F_2\text{ the lowest eigenvalue of }C_M\to-\infty.
\qquad\text{(5.5)}
```

```math
A_0>0\iff\alpha_1+\alpha_2>0\ \text{and}\ \alpha_1\alpha_2+(\alpha_1+\alpha_2)/r_{12}>0.
\qquad\text{(5.6)}
```

Eq. (5.7) (negative). Conditions stated with it in its Result: a body with $`\mu F_2>0`$ (branch $`\sigma={\rm sign}\,F_2`$, every level), no anchor, acts as an anchor of strength $`2\mu F_2`$ at its own place; alone, its $`g_s`$-linear cost is the same at every place (no weight), and its cost has no expansion in $`s`$.

```math
W(x)=-\frac{F_1g_s}{2F_2}\quad\text{for every }x,x_s:\qquad W(x)-W(x')=0.
\qquad\text{(5.7)}
```

Eq. (5.8), exact for every $`L`$ on both graphs, with $`G_a(h,\cdot)=1/\kappa_a`$; on the ring $`r=\frac{s(L-s)}{\kappa_hL}`$:

```math
G_a(x,y):=(K_a^{-1})_{xy}=\frac1{\kappa_a}+g(x-y)-g(x-h)-g(y-h)+g(0)=\frac1{\kappa_a}+\frac12\bigl[r(x,h)+r(y,h)-r(x,y)\bigr],
\qquad\text{(5.8)}
```

Eq. (5.10) (criterion with the anchor). Conditions stated with it in its Result: it holds whenever all $`\mu_iF_2^{(i)}\ge0`$; for $`\mu F_2<0`$ it fails on the ring once $`\frac{d(L-d)}{\kappa_hL}\ge\frac1{2M_k\lvert F_2\rvert}-\frac1{\kappa_a}`$, and on the cubic torus ($`L\to\infty`$) it holds at every place iff $`2M_k\lvert F_2\rvert\Gamma_\infty\le1`$, $`\Gamma_\infty=\frac1{\kappa_a}+\frac{2\gamma_3}{\kappa_h}`$.

```math
A>0\iff\Gamma_n^{-1}+\mathcal A>0;\qquad\text{one body: }1+2\mu F_2\Gamma(x)>0,\quad\Gamma(x):=G_a(x,x)=\frac1{\kappa_a}+r(x,h).
\qquad\text{(5.10)}
```

Eq. (5.11) (made field without bodies, first order in $`g_s`$). Conditions stated with it in its Result: a uniform shift plus a place-dependent part; on the cubic torus as $`L\to\infty`$, the source plus an opposite image at the anchor over the constant $`-g_s[c_\phi-g_\infty(x_s-h)]`$; on the line, $`-g_s[\frac1{\kappa_a}+\frac{\min(d_x,d_s)}{\kappa_h}]`$ on one side of $`h`$ and $`-g_s/\kappa_a`$ across.

```math
\phi_a(x):=\langle q_x\rangle=-g_sG_a(x,x_s)=-g_s\Bigl[\frac1{\kappa_a}+\frac{r(x_s,h)}2\Bigr]-\frac{g_s}2\bigl[r(x,h)-r(x,x_s)\bigr].
\qquad\text{(5.11)}
```

Eqs. (5.14), (5.15) (mutual cost of two sources). Conditions stated with them in its Result: (5.14) is exact on both graphs for every $`L`$, and constant if one source sits at $`h`$; (5.15) holds on the cubic torus with $`L\to\infty`$ first and all of $`\lvert x_1-x_2\rvert,\lvert x_1-h\rvert,\lvert x_2-h\rvert\ge\ell\gg1`$. With $`\mathbf r=x_2-x_1`$, midpoint $`X`$ and $`D_X=\lvert X-h\rvert`$: the separation dependence is $`-\frac{g_1g_2}{4\pi\kappa_h\lvert\mathbf r\rvert}`$, the coefficient of the field without an anchor, when $`\lvert\mathbf r\rvert/D_X\to0`$ (order (a)); with one source at a fixed place it falls as $`\lvert\mathbf r\rvert^{-2}`$ or faster (order (b)); at fixed midpoint it is $`+\frac{3g_1g_2}{4\pi\kappa_h\lvert\mathbf r\rvert}`$ (order (c)); $`L\to\infty`$ must come before both other limits.

```math
\mathcal E_{12}=-g_1g_2\,G_a(x_1,x_2)=-g_1g_2\Bigl[\frac1{\kappa_a}+g(x_1-x_2)-g(x_1-h)-g(x_2-h)+g(0)\Bigr],
\qquad\text{(5.14)}
```

```math
\mathcal E_{12}=-g_1g_2\,c_\phi-\frac{g_1g_2}{4\pi\kappa_h}\Bigl[\frac1{\lvert x_1-x_2\rvert}-\frac1{\lvert x_1-h\rvert}-\frac1{\lvert x_2-h\rvert}\Bigr]+O(\ell^{-3}).
\qquad\text{(5.15)}
```

## Assumptions

- The setting under "Goal". The field, the push, the sources and the state are assumptions of the package (M8, M9).
- Standard mathematics applied to the stated operators may be used: the representation theory of $`\mathfrak{su}(2)`$ and the decomposition into sectors of total spin; Perron–Frobenius arguments for the stated matrices; exact representations of the spin matrices by oscillator operators and their expansion in $`1/S`$ (base problem, M4: expansions of stated operators in the inverse number of places are mathematics); quadratic forms, their normal modes and lowest eigenvectors; lattice Green functions on tori and their asymptotics; exact diagonalization. State each with its conditions. No result of a theory of ordered media or of their waves is an input (M4); every statement about the exchange cells is derived from the stated operators.

## Scope

- **Class.** Exchange cells with every $`S\ge\frac12`$: the leading orders in $`1/S`$ as $`S\to\infty`$, and $`S=\frac12`$ as the smallest cells. $`J>0`$ on the cubic torus (main) and on the ring; $`J<0`$ in item 1 only. Every $`h_p>0`$ and every place $`h`$. The sources of "Setting", with strengths small against $`JS`$; state the small numbers and what they do and do not make small.
- **Orders of limits.** State every order used, and say which results depend on it. Item 1(b): the two orders named there. Item 3: the order named there; where another order changes the answer, say so. State whether the expansion in $`1/S`$ is taken at fixed $`L`$, and whether its coefficients are uniform in $`L`$ and in the distances.
- **Cancellations.** Name the members at which a leading coefficient of item 3 vanishes (for example a source at the push, sources on the same cell, a vanishing component of $`\mathbf m`$), and exclude them explicitly.
- **Control.** For items 1(b) and 3, a member of the class or of a stated wider class in which the answer fails, or a proof that there is none. The ring is one member to treat in item 1(b).
- **Note (2026-10-26, after external round 1).** For R1, item 3(b) asks whether the mutual cost has a part that falls as $`1/r`$, and its leading law of decay and sign at $`r\to\infty`$ last; its coefficient, and the regime $`r\ll\ell_b`$, are asked only where a controlled derivation gives them, and are otherwise stated as estimates. For R2, the sign is asked for every pair of link orientations with the separation along an axis, together with the members at which the leading coefficient vanishes. Reason: the next stage needs to know which held objects have a long-range mutual cost; the coefficient of a faster decay is not used.
- **Note (2026-10-26, after external round 3).** In item 3(c), for direction sources that are not parallel and nearly cancel each other (where $`SJ\lvert\mathbf h_{\rm eff}\rvert`$ is not large against $`\gamma_3\lvert\mathbf h_i\rvert^2`$), the item asks only the cost of the orientation and what its minimum gives where it is computed; a full classification of that corner is not asked. Reason: the next stage uses items 3(a), 3(b) and the cases of 3(c) away from this corner.
- **Note (2026-10-26, after the review of v5).** In item 2, the identification for dynamics (a field with the kinetic term of 05-anchor, the limit in which it holds and its range) is asked on the cubic torus only; on the ring, item 2 asks the static identification and its conditions. Reason: the ring is the control of item 1(b), and the carry-over of 09-anchor-formation to exchange cells is needed on the cubic torus, the main graph.
- Out of scope: moving bodies and inertia; the weighing of a held body's own mark and of bonds (a later package on the grip and the number of places); the formation of the mark (09-anchor-formation); the square torus; pushes other than the stated term (but state how the results depend on $`h_p`$); cells of more than two objects; where the lattice itself comes from.

## Depth

- Item 1(a): standard or short argument (needed by items 1(b) and 3(c)).
- Item 1(b): derive (needed by item 3 of the base problem, the anchor as a push, and by item 4, cells with finitely many places).
- Item 2: derive for the identification, short argument for the carry-over (needed by item 4 of the base problem, and to carry 09-anchor-formation over to exchange cells).
- Item 3(a): short argument from item 2 where it applies, derive otherwise; item 3(b): derive; item 3(c): short argument (needed by item 3 of the base problem, a long-range mark with a free uniform change, and by the choice of the next stage: which held objects can have a long-range mutual cost in a field unchanged by a common rotation).

## Expected result

- Item 1(a): uniqueness and the behaviour under the common rotation, for both signs of $`J`$.
- Item 1(b): $`m(x)`$ far from the push as a function of $`S`$, $`h_p`$ and the graph, in each order of limits, at the stated orders in $`1/S`$; for $`S=\frac12`$, what the computed clusters decide.
- Item 2: an identification with its conditions, or the statement that there is none; the results of 05-anchor that hold, and the changes for those that do not.
- Item 3: for each kind of source, the law of decay of the mutual cost in $`r`$ with its coefficient and sign at the stated order, and the order of limits; the members with a vanishing coefficient.

Give every main result a tag $`(8.k)`$.

Consistency checks, at most three: for example the limit $`S\to\infty`$ of item 1(b) against the product state with orientation $`\mathbf n`$, the identification of item 2 against (5.15), and dimensions.

## Code

Required: check: (i) exact diagonalization of cells with $`S=\frac12`$ (and $`S=1`$ where feasible), $`J>0`$ and a push on one object, on rings of at least three even sizes up to at least 16 objects and on one periodic three-dimensional cluster of at least 16 objects (state its links): $`m(x)`$ at the largest distance from the push against $`h_p`$ and the size (item 1(b)); (ii) at leading order in $`1/S`$, on cubic tori of two sizes: the first correction to $`m(x)`$ far from the push (item 1(b)), and the mutual cost of item 3 for each kind of source at four or more separations.
