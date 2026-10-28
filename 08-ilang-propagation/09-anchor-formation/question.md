# Question: 09-anchor-formation

- **Subproject:** 08-ilang-propagation
- **Package:** 09-anchor-formation
- **Equation tags:** (9.k)
- **Created:** 2026-10-26

## Goal

Determine, for the field of oscillator cells without pinning and with an anchor of 05-anchor, how the made field of a held source forms after the source term acts: its place-dependent part and its uniform part, against the distance and $`\lambda`$, and whether, in which order of the limits (size, distance to the anchor, distance from the source, $`\lambda`$) and at which speed, the long-range part forms within a $`\lambda`$ linear in the distance. Then determine whether, in one order of the limits, the long-range mark, its formation within a linear $`\lambda`$, and the weighing of 05-anchor hold together in the anchored field. This is the formation part of item 3 of the base problem, which 05-anchor left out. Every result is stated through quantities that the total contract and the start fix (M6).

**Setting.**
- **Field** (assumption, M8). As in 05-anchor: oscillator cells at the places of a ring ($`D=1`$) or a cubic torus ($`D=3`$) of side $`L`$, each cell an object of its own type with the places $`0,\dots,M-1`$; the contract is the compression $`C_M`$ of $`H=\sum_x\frac12p_x^2+\frac{\kappa_h}2\sum_{\langle xy\rangle}(q_x-q_y)^2`$, $`\kappa_h>0`$, without pinning, plus the anchor $`\frac{\kappa_a}2q_h^2`$, $`\kappa_a>0`$, on the cell at one place $`h`$, plus the source term; $`\Phi_x=q_x`$. $`M\to\infty`$ first, in the sense stated in 05-anchor (the ranges of the compressions grow with $`M`$; state how it is used for the evolution). $`K_a=\kappa_h\Delta+\kappa_aP_h`$ as in the inputs, and $`c_0:=\sqrt{\kappa_h}`$, the slope of the normal-mode frequency of $`\kappa_h\Delta`$ at small labels.
- **Source and start** (assumption, M8, M9, A11). A held object at $`x_s`$ coupled to its cell by $`g_sq_{x_s}`$. The contract is $`C_M+g_sq_{x_s}`$ at every $`\lambda\ge0`$ (the term is listed from the start; A5 admits no $`\lambda`$-dependent term); at $`\lambda=0`$ the state is the lowest eigenvector $`\Omega`$ of the contract without the source term (field and anchor). $`\lambda\ge0`$ only (A9). The made field is $`\delta a(x,\lambda)=\partial_{g_s}\langle q_x\rangle_\lambda`$ at $`g_s=0`$, and $`\delta a_{\rm st}(x)`$ is the same in the lowest eigenvector of the contract with the source, so that $`g_s\,\delta a_{\rm st}=\phi_a`$ of (5.11).
- **Parts of the made field.** As in (5.11), $`\delta a_{\rm st}`$ is a uniform shift plus a place-dependent part. For $`\lambda>0`$, state how the two parts are separated (for example by place differences of the made field, which remove any uniform part, and by the component along the lowest normal mode of $`K_a`$), and use the same separation for the static value.
- **Criteria.** (4.11) along an axis and (4.19) on a shell, applied to the place-dependent part (state the reference value and the place differences used); for the uniform part, a criterion stated before use. A criterion that the uniform part dominates is not a criterion for the place-dependent part.
- **Held body** (item 4 only; assumption, M8, A15). A held Model D body at $`x`$ with a grip of class (G2), in the block $`S\to\mu`$, as in 05-anchor; at first order in the grip its weight is $`W^{(1)}=\mu F_1\phi_a(x)`$ of (5.18).
- The results of 04-formation hold for translation-invariant fields with pinning ($`m_h>0`$). The anchored field is neither, so they are inputs for comparison and may be used only where you show that they apply.

1. **The made field after the source acts.** Determine $`\delta a(x,\lambda)`$ for every $`L`$ on both graphs ($`M\to\infty`$ first), and its split into the uniform part and the place-dependent part.
2. **Formation of the place-dependent part.** Determine its formation at distance $`\rho`$ from the source: for source and observation far from the anchor (distances to $`h`$ large against $`\rho`$), and for distances to $`h`$ comparable with $`\rho`$, where the image at the anchor enters; whether it forms within a $`\lambda`$ linear in $`\rho`$, and at which speed compared with $`c_0`$, the front and the largest slope of the normal-mode frequency; in the order $`L\to\infty`$ (or $`\lambda`$ below the wrap time), then $`\rho\to\infty`$ at fixed $`c_0\lambda/\rho`$, with the distances to $`h`$ in a stated relation to $`\rho`$.
3. **The uniform part.** Determine how the uniform part depends on $`\lambda`$: its scale in $`\lambda`$ against $`L`$, $`\kappa_a`$ and the distance of the source to the anchor; whether it reaches its static value of (5.11), and in which order of the limits ($`\lambda`$ against $`L`$).
4. **All three together.** From items 1–3, (5.15) and (5.18) with the weighing of 05-anchor quoted below: determine whether there is an order of the limits in which the long-range mark of two sources, the formation of the place-dependent part within a $`\lambda`$ linear in the distance, and that weighing hold together; state the order, or why there is none.

## Inputs

From 08-ilang-propagation/04-formation@v4 (same subproject). Setting there: class F, a translation-invariant field of finitely many objects on a torus $`X_f=\mathbb Z_L^D`$ with contract $`C_F`$, read operators $`A_x`$ and source operators $`B_x`$, the source at $`x_s=0`$; the contract is $`C_F+g_sB_0`$ at every $`\lambda\ge0`$, and at $`\lambda=0`$ the state is the nondegenerate lowest eigenvector $`\Omega`$ of $`C_F`$; $`\delta a(x,\lambda)=\partial_{g_s}\langle A_x\rangle_\lambda`$ at $`g_s=0`$, and $`\delta a_{\rm st}`$ the same in the lowest eigenvector of $`C_F+g_sB_0`$. The oscillator class: $`H=\frac12\sum_xp_x^2+\frac12\sum_{x,y}q_xK_{xy}q_y`$, $`A_x=B_x=q_x`$, $`K`$ of finite range and invariant under the translations and under the permutations and reflections of the axes, $`\hat K(\mathbf k)=m_h^2+\hat K_0(\mathbf k)`$ with $`\hat K_0(\mathbf k)=c_0^2\lvert\mathbf k\rvert^2+O(\lvert\mathbf k\rvert^4)`$ and $`m_h,c_0>0`$, a single soft point ($`\hat K_0(\mathbf k)>0`$ for $`\mathbf k\ne0`$), and finitely many caustic values with folds (its condition (d); the nearest-neighbour contract is a member); $`\Omega_{\mathbf k}=\hat K(\mathbf k)^{1/2}`$; $`M\to\infty`$ first.

Eq. (4.10), oscillator class, $`L\to\infty`$:

```math
u(x,\lambda):=\delta a(x,\lambda)-\delta a_{\rm st}(x)=\int_{[-\pi,\pi]^D}\frac{\mathrm d^D k}{(2\pi)^D}\,e^{i\mathbf k\cdot x}\,\frac{\cos\Omega_{\mathbf k}\lambda}{\Omega_{\mathbf k}^2}.
\qquad\text{(4.10)}
```

Eq. (4.11), the criterion along an axis (places $`\rho\mathbf e_1`$, $`\rho\in\mathbb N`$). Conditions stated with it: the made field at distance $`\rho`$ has formed to accuracy $`\varepsilon\in(0,1)`$ from $`\lambda_f`$ on if $`\lvert\Delta_D(\rho,\lambda)\rvert\le\varepsilon`$ for every $`\lambda\ge\lambda_f`$; $`\lambda_{\rm form}(\rho;\varepsilon)`$ is the least such $`\lambda_f`$; the first change arrives at $`\lambda_{\rm arr}(\rho;\eta)`$, the first $`\lambda`$ with $`\lvert\Delta_D+1\rvert\ge\eta\rho^{-1/2}`$ ($`\eta>0`$ fixed).

```math
\Delta_3(\rho,\lambda)=\frac{\delta a(\rho\mathbf e_1,\lambda)}{\delta a_{\rm st}(\rho\mathbf e_1)}-1\ \ (D=3),\qquad
\Delta_1(\rho,\lambda)=\frac{\nabla\delta a(\rho,\lambda)}{\nabla\delta a_{\rm st}(\rho)}-1,\ \ \nabla v(\rho)=v(\rho+1)-v(\rho)\ \ (D=1);
\qquad\text{(4.11)}
```

Eqs. (4.12)–(4.14), oscillator class. Conditions stated with them in its Result: order of limits $`g_s\to0`$, $`M\to\infty`$, $`L\to\infty`$ (or $`\lambda`$ below the wrap time), then $`\rho\to\infty`$ along $`\mathbf e_1`$ at fixed $`w=c_0\lambda/\rho`$ and fixed $`\mu=m_h\rho/c_0`$, then $`\mu`$ small; (4.12) is the limit of $`\Delta_D`$ on the ring and on the cubic torus; (4.14) holds for every $`K`$ of the class, every $`\varepsilon\in(0,1)`$ and every $`\mu`$ with $`\mu e^\mu(1+\mu/2)<\varepsilon`$, on the ring and on the cubic torus: formation within a $`\lambda`$ linear in the distance at the formation speed $`c_0`$.

```math
\Delta_\infty(w,\mu)=\begin{cases}-1, & w<1,\\[2pt] e^{\mu}-1-\mu e^{\mu}\,I_\mu\bigl(\mu\sqrt{w^2-1}\bigr), & w>1,\end{cases}\qquad I_\mu(Y)=\int_0^Y\frac{J_1(y)\,\mathrm dy}{\sqrt{y^2+\mu^2}} .
\qquad\text{(4.12)}
```

```math
\Delta_\infty(w,\mu)=-1\ \ (w<1),\qquad \lvert\Delta_\infty(w,\mu)\rvert\le\mu e^{\mu}\bigl(1+\tfrac{\mu}{2}\bigr)\ \ (w>1).
\qquad\text{(4.13)}
```

```math
\lim_{\rho\to\infty}\frac{c_0\,\lambda_{\rm form}(\rho;\varepsilon)}{\rho}=1,\qquad \lambda_{\rm form}(\rho;\varepsilon)-\frac{\rho}{c_0}=O(\rho^{1/3})\ \ \text{once the caustic wakes }O(\rho^{-1/3})\text{ are below }\varepsilon-\mu e^\mu(1+\tfrac{\mu}{2}) ,
\qquad\text{(4.14)}
```

Eq. (4.19), the criterion on a shell (cubic torus). Conditions stated with it: $`\Phi\ge0`$ smooth on $`\mathbb R^3`$, not identically zero, supported in the shell $`1\le\lvert y\rvert\le2`$, $`\varphi_\ell(x)=\Phi(x/\ell)`$; the made field at distance $`\ell`$ has formed in the mean to accuracy $`\varepsilon\in(0,1)`$ from $`\lambda_f`$ on if (4.19) holds for every $`\lambda\ge\lambda_f`$; order $`g_s\to0`$, $`L\to\infty`$, then $`\ell\to\infty`$; this is not the arrival of a first change.

```math
\Bigl\lvert\sum_x\varphi_\ell(x)\bigl[\delta a(x,\lambda)-\delta a_{\rm st}(x)\bigr]\Bigr\rvert\ \le\ \varepsilon\,\Bigl\lvert\sum_x\varphi_\ell(x)\,\delta a_{\rm st}(x)\Bigr\rvert ;
\qquad\text{(4.19)}
```

From 08-ilang-propagation/05-anchor@v3 (same subproject). Setting there: the field of "Setting" above with held bodies and held sources; $`\Delta`$ the graph Laplacian, $`P_x`$ the projector onto the cell $`x`$, $`K_a=\kappa_h\Delta+\kappa_aP_h`$; $`g:=(\kappa_h\Delta)^+`$, $`r(x,y):=2[g(0)-g(x-y)]`$, and $`\gamma_\nu:=(\kappa_h\Delta+\nu^2)^{-1}`$ for $`\nu>0`$. On the cubic torus as $`L\to\infty`$, $`g\to g_\infty`$ with $`g_\infty(0)=\gamma_3/\kappa_h`$, $`\gamma_3=0.2527310`$, $`g_\infty(x)=\frac1{4\pi\kappa_h\lvert x\rvert}+O(\lvert x\rvert^{-3})`$; $`c_\phi:=\frac1{\kappa_a}+\frac{\gamma_3}{\kappa_h}`$. $`\Gamma(x):=G_a(x,x)`$, $`w(x):=\langle q_x^2\rangle=\frac12(K_a^{-1/2})_{xx}`$, and $`\Sigma(x,y)`$ the static correlation of $`q_x^2,q_y^2`$ (a term $`\epsilon q_y^2`$ changes $`w(x)`$ by $`-\epsilon\Sigma(x,y)`$). A held body has $`\mu=\sigma M_k`$ and a grip $`F(q)=F_0+F_1q+F_2q^2`$; the mutual cost of two sources is the part $`\propto g_1g_2`$ of the lowest eigenvalue.

Eq. (5.8), exact for every $`L`$ on both graphs, with $`G_a(h,\cdot)=1/\kappa_a`$; on the ring $`r=\frac{s(L-s)}{\kappa_hL}`$:

```math
G_a(x,y):=(K_a^{-1})_{xy}=\frac1{\kappa_a}+g(x-y)-g(x-h)-g(y-h)+g(0)=\frac1{\kappa_a}+\frac12\bigl[r(x,h)+r(y,h)-r(x,y)\bigr],
\qquad\text{(5.8)}
```

Eq. (5.9), the resolvent, for $`\nu>0`$ ($`R_{xy}(\nu)>0`$):

```math
R_{xy}(\nu):=\bigl[(K_a+\nu^2)^{-1}\bigr]_{xy}=\gamma_\nu(x-y)-\frac{\kappa_a\gamma_\nu(x-h)\gamma_\nu(y-h)}{1+\kappa_a\gamma_\nu(0)},\qquad R(0)=K_a^{-1};
\qquad\text{(5.9)}
```

Eq. (5.11), the static made field, first order in $`g_s`$. Conditions stated with it in its Result: a uniform shift plus a place-dependent part; on the cubic torus as $`L\to\infty`$, the source plus an opposite image at the anchor over the constant $`-g_s[c_\phi-g_\infty(x_s-h)]`$; on the line, $`-g_s[\frac1{\kappa_a}+\frac{\min(d_x,d_s)}{\kappa_h}]`$ on one side of $`h`$ and $`-g_s/\kappa_a`$ across.

```math
\phi_a(x):=\langle q_x\rangle=-g_sG_a(x,x_s)=-g_s\Bigl[\frac1{\kappa_a}+\frac{r(x_s,h)}2\Bigr]-\frac{g_s}2\bigl[r(x,h)-r(x,x_s)\bigr].
\qquad\text{(5.11)}
```

Eq. (5.15), the mutual cost of two sources. Conditions stated with it in its Result: cubic torus, $`L\to\infty`$ first, all of $`\lvert x_1-x_2\rvert,\lvert x_1-h\rvert,\lvert x_2-h\rvert\ge\ell\gg1`$. With $`\mathbf r=x_2-x_1`$, midpoint $`X`$ and $`D_X=\lvert X-h\rvert`$: the separation dependence is $`-\frac{g_1g_2}{4\pi\kappa_h\lvert\mathbf r\rvert}`$ when $`\lvert\mathbf r\rvert/D_X\to0`$ (order (a)); with one source at a fixed place it falls as $`\lvert\mathbf r\rvert^{-2}`$ or faster (order (b)); at fixed midpoint it is $`+\frac{3g_1g_2}{4\pi\kappa_h\lvert\mathbf r\rvert}`$ (order (c)); $`L\to\infty`$ must come before both other limits.

```math
\mathcal E_{12}=-g_1g_2\,c_\phi-\frac{g_1g_2}{4\pi\kappa_h}\Bigl[\frac1{\lvert x_1-x_2\rvert}-\frac1{\lvert x_1-h\rvert}-\frac1{\lvert x_2-h\rvert}\Bigr]+O(\ell^{-3}).
\qquad\text{(5.15)}
```

Eq. (5.18), one held body under (5.10) of 05-anchor ($`1+2\mu F_2\Gamma(x)>0`$), at order $`s`$ and $`s^2`$ of the grip $`F\to sF`$:

```math
C^{(1)}=\mu\bigl(F_0+F_2w(x)\bigr),\quad C^{\rm mark}=-\frac{\mu^2}2\bigl(F_1^2\Gamma(x)+F_2^2\Sigma(x,x)\bigr),\quad W^{(1)}=\mu F_1\phi_a(x),\quad W^{\rm mark}=-2\mu^2F_1F_2\,\Gamma(x)\,\phi_a(x).
\qquad\text{(5.18)}
```

The weighing of 05-anchor (its Result, item 14; quoted in words). Two families of comparisons: (A) fixed placements relative to the source, with a nonzero source-induced difference $`\Delta g_s`$, moved away from $`h`$ to distance $`d`$; (B) the center $`y`$ of the comparison at distance $`d`$ from $`h`$ and $`R`$ from $`x_s`$, with the comparison vector $`\delta`$ satisfying $`\lvert\delta\cdot\hat e_s\rvert\ge c\lvert\delta\rvert`$, $`\hat e_s=(y-x_s)/R`$, $`c\in(0,1]`$ fixed, and $`1\ll R`$, $`\lvert\delta\rvert\ll R\ll d`$. In the order $`L\to\infty`$, then $`d\to\infty`$, within (A), or within (B) with $`R/d\to0`$ at fixed $`c`$, in its controlled regime: $`\rho_{\rm mark}=1`$ and $`\rho_{{\rm bond},i}=m_{\mathbf r}`$ for every level and both branches, at order $`\mu^2`$ and leading order in the grip, iff the grips are square with a common $`\hat\beta`$; in the lowest eigenvector of the stated contract iff in addition (5.10) holds for one body ((5.26) there for a pair). At the mirror placement no grip gives $`\rho_{\rm mark}=1`$, so no grip weighs at every comparison.

## Assumptions

- The setting under "Goal". The field, the anchor, the source, the start and the held body are assumptions of the package (M8, M9).
- Standard mathematics applied to the stated operators may be used: the closed linear equations of the means of a quadratic contract with a linear term; normal modes of $`K_a`$, rank-one updates (Sherman–Morrison) and resolvents; Laplace and Fourier transforms; lattice Green functions on tori and their asymptotics; stationary phase uniform in a parameter. State each with its conditions.

## Scope

- **Class.** The nearest-neighbour oscillator cells of "Setting" without pinning, with the anchor, every $`\kappa_h,\kappa_a>0`$, every anchor place $`h`$ and every source place $`x_s`$, the ring and the cubic torus, every $`L`$ in a stated regime; first order in $`g_s`$.
- **Orders of limits.** $`M\to\infty`$ first. State every other order (size, $`\lambda`$, distance to the anchor, distance from the source), and say which results depend on it; in particular, state the results both for $`L\to\infty`$ before $`\lambda\to\infty`$ and for $`\lambda`$ growing with $`L`$, where they differ.
- **Cancellations.** Name the members at which a reference value of a criterion vanishes or the place-dependent part is not dominated by its long-range part (for example the source at the anchor, an observation place at the anchor, places where the source and image terms cancel), and exclude them explicitly.
- **Control.** For item 2, a member of the class or of a stated wider class in which the place-dependent part does not form within a $`\lambda`$ linear in the distance, or a proof that there is none. The ring is one member to treat.
- **Note (2026-10-26, after external round 1).** (a) Item 2 with the shell criterion (4.19) may be restricted to weights $`\Phi`$ that depend only on $`\lvert y\rvert`$; say so where it is used. (b) Condition (d) of 04-formation concerns the phases $`\rho k_1\pm\lambda\Omega_{\mathbf k}`$ of formation along an axis, at $`m_h\to0`$; its Result (4.14) states that the nearest-neighbour contract is a member, with no caustic values in $`D=1`$ and the caustic values $`w=1+\sqrt2`$ and $`\sqrt2+\sqrt3`$ in $`D=3`$. (c) Item 4 asks whether the three statements hold in one order of the limits as properties of the stated description: the long-range mark and the weighing as properties of the lowest eigenvectors of the contracts with the sources and bodies, the formation as a property of the evolution from $`\Omega`$. Whether a weighing is realized in the evolving state is not asked. Reason: the next stage needs the order of limits in which the three properties are available together; a weighing in a state that does not relax is a separate question.
- **Note (2026-10-26, after external round 2).** On the cubic torus, the single anchor strength $`\kappa_a=\kappa_h/\gamma_3`$, at which the localized mode reaches the edge of the band, may be excluded from the positive formation statements and from the asymptotics of the image; state the exclusion and what still holds there (the statements that no formation occurs are asked for every $`\kappa_a`$). Reason: it is one marginal value of the anchor, and no later package uses it.
- Out of scope: held bodies other than at first order in the grip (item 4 only); moving bodies and inertia; exchange cells (08-tilt carries the result over); the square torus; anchors other than $`\frac{\kappa_a}2q_h^2`$ (but state how the results depend on $`\kappa_a`$).

## Depth

- Item 1: derive (needed by items 2 and 3, and by item 3 of the base problem).
- Item 2: derive (needed by item 3 of the base problem: formation at a finite speed with an anchor).
- Item 3: derive (needed by item 3 of the base problem, and by the weighing with an anchor, whose static quantities contain the uniform part).
- Item 4: short argument (needed by item 3 of the base problem: weighing, a long-range mark and formation together).

## Expected result

- Item 1: an expression for the made field at every $`\lambda\ge0`$, and the split into its two parts.
- Item 2: the formation $`\lambda`$ of the place-dependent part as a function of $`\rho`$ and of the distances to the anchor, with its speed and the order of limits, or the statement that it does not form within a linear $`\lambda`$.
- Item 3: the scale in $`\lambda`$ of the uniform part as a function of $`L`$, $`\kappa_a`$ and the distance of the source to the anchor, and the orders of limits in which it reaches its static value.
- Item 4: an order of limits in which the three hold together, or the reason why there is none.

Give every main result a tag $`(9.k)`$.

Consistency checks, at most three: for example the limit $`\kappa_a\to\infty`$, the comparison of item 2 with (4.14) at small $`m_h`$ where the two settings can be compared, and dimensions.

## Code

Required: check: on a ring and on a cubic torus of two sizes each, with the anchor, against the exact solution of the linear equations of the means of the quadratic contract ($`M\to\infty`$): (i) the made field of item 1 at three places, with the anchor at two distances from the source; (ii) the formation of the place-dependent part at four or more distances (item 2); (iii) the scale in $`\lambda`$ of the uniform part at three or more sizes at fixed $`\kappa_a`$ (item 3).
