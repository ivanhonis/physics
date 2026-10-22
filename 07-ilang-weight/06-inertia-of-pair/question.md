# Question: 06-inertia-of-pair

- **Subproject:** 07-ilang-weight
- **Package:** 06-inertia-of-pair
- **Equation tags:** (6.k)
- **Created:** 2026-10-21

## Goal

Determine, for two moving bodies bound through the field they make, the inertia of the bound pair against the inertias of the two bodies and against the cost of the pair; whether it is the cost divided by the square of one speed; and whether the ratio of weight to inertia of the bound pair is the same as for each body alone. This is item 3 of the base problem for bound pairs, for couplings (a) and (c). Every result is stated through quantities that the total contract and the state fix (M6).

**Setting.**
- **Field.** $`N_f\ge1`$ identical field objects ($`c=+1`$) on a ring of $`L`$ places, no pair terms among them, own term $`C_1=-t_f\sum_x(\lvert x\rangle\langle x+1\rvert+\lvert x+1\rangle\langle x\rvert)`$, $`t_f>0`$, $`\Phi_x`$ the number of field objects at $`x`$, $`n:=N_f/L`$.
- **Bodies.** Two Model D bodies $`b_1,b_2`$ of different types (base problem, "Notation and conventions") on the same ring of position labels, with parameters $`\tau_i`$, $`m_i`$, clock levels $`k_i`$ with half-gaps $`M_i`$, branches $`\sigma_i`$, each coupled to the field by coupling (a) or (c) of the base problem with its own real constant $`\gamma_i`$, $`g_i:=\sigma_i\gamma_iM_i`$. There is no pair term between $`b_1`$ and $`b_2`$. Records at $`\kappa\to0`$.
- **State of the field** (assumption, M9): the lowest state adapted to the bodies. The highest state is out of scope.
- **Regime R** (assumption), as in 07-ilang-weight/02-two-free-bodies:
  - **R1** (isolated band). In each sector of the conserved labels, the $`\tau=0`$ group $`\mathcal G=\{e_{jl}\}`$, $`e_{jl}:=\lvert j\,\sigma_1k_1,\ l\,\sigma_2k_2\rangle\otimes\Omega_{jl}`$ ($`\Omega_{jl}`$ the lowest field state of the held problem with $`b_1`$ at $`j`$, $`b_2`$ at $`l`$), has distance $`\delta_1`$ from the $`\tau=0`$ levels reached by one motion term and $`\delta\le\delta_1`$ from all other $`\tau=0`$ levels, with $`\tau'\ll\delta_1`$ and $`\tau'^2/\delta_1\ll\delta`$, $`\tau':=\max_i\tau_i(1+\lvert\gamma_i\rvert N_f)`$ for (c) and $`\max_i\tau_i`$ for (a). Each body alone with the field satisfies the same with its own gaps.
  - **R2** (order). Order $`\tau_i^2`$ in the band contract.
  - A *binding regime* (the size of the mutual term against the hopping of the bodies in the band) is to be stated and named as an assumption.
- **Bound level.** A level of the band contract (2.10) of 07-ilang-weight/02-two-free-bodies (quoted below), in the sector of total plane-wave label $`P`$ of bodies and field (2.1) there, whose separation of the two bodies is localized on a scale small against $`L`$. Write it $`E_b(P)`$.
- **Inertia of the pair:** $`1/E_b''(0)`$, the inverse curvature in $`P`$ (continued in $`P`$ where needed; state how).
- **Weight:** the place dependence of an eigenvalue in the field of a distant held source $`g_sP_{x_s}`$ at first order in $`g_s`$.

1. **Bound levels.** Determine for which branches and signs of $`\gamma_1\gamma_2`$, and in which binding regime, bound levels exist, and give $`E_b(P)`$ for the lowest of them in the relative motion (or the highest, where the relative motion has negative inertia; state which). State the criterion of localization used.
2. **Inertia of the pair.** Determine $`1/E_b''(0)`$ at order $`\tau_i^2`$ and compare it with $`\mu_1+\mu_2`$ of (2.14): the difference at the leading order at which it is non-zero, if it is, and the terms of the band contract it comes from. State its dependence on the level of the relative motion.
3. **Inertia against cost.** Define the cost of the bound pair through eigenvalue differences fixed by the total contract (the pair level against the descriptions with one body and without bodies, as in (4.2) of 06-ilang-source/04-profile, quoted below). Determine whether the difference of item 2 equals the corresponding difference of cost divided by the square of the speed of (2.14) ($`\tau_i`$ for (a), $`\tau_i(1+\gamma_in)`$ for (c)). Treat equal speeds of the two bodies as a named condition, and also answer for unequal ones. Answer at leading order.
4. **Weight over inertia.** With the source at a distance large against the size of the pair, determine the weight of the bound level and the product of $`E_b''(0)`$ and its weight difference between two places of the pair. This product is the factor that sets the fall from rest in (7.7) of 06-ilang-source/07-dressed-fall (quoted below); state whether (7.7) carries over to the bound level. Compare the product with the same product for each body alone, and determine whether they are equal at leading order. If they differ, give the first order of the difference.
5. **The hopping of the field.** State how the answers of items 1–4 depend on $`t_f`$ at fixed $`n`$, $`\gamma_i`$, $`M_i`$, $`\tau_i`$, including the regime R and the binding regime.

**Note (2026-10-21, after external round 2).** Items 2–5 are asked only for the bound level selected in item 1: the lowest level of the relative motion where its inertia is positive, the highest where it is negative. This is the level made of bodies near rest that later packages compare with single bodies. Alternating extreme levels and excited levels of the relative motion are out of scope for items 2–5; item 1 may name them.

**Note (2026-10-21, after external round 3).** Two tuned cancellations are out of scope, because the base problem needs the general behaviour of a bound pair, not tuned exceptions. (i) All items are asked only where the relative hopping of the two bodies does not nearly cancel ($`\mu_1^{-1}+\mu_2^{-1}`$ not small against $`\max_i\lvert\mu_i^{-1}\rvert`$, with a stated hierarchy that keeps the omitted orders small against the retained relative dispersion). (ii) Item 4 is asked only where the first-order weights of the two bodies do not cancel ($`g_1+g_2`$ not small against $`\max_i\lvert g_i\rvert`$).

## Inputs

From 06-ilang-source/04-profile@v4. Setting there: held sources $`g_i\Phi_{x_i}`$ at $`x_1`$, $`x_2`$ on the field above; $`\varepsilon_0(g)`$ the lowest eigenvalue of the one-object contract with the sources; $`M`$ the mutual term.

Eq. (4.2) of 06-ilang-source/04-profile:

```math
E(g)=N_f\,\varepsilon_0(g),\qquad M=N_f\bigl[\varepsilon_0(g_1,g_2)-\varepsilon_0(g_1,0)-\varepsilon_0(0,g_2)+\varepsilon_0(0,0)\bigr].\qquad\text{(4.2)}
```

From 06-ilang-source/07-dressed-fall@v2. Setting there: one body with its own mark (coupling (a) or (c), constant $`\gamma`$, $`g_b:=\sigma\gamma M_k`$) and a held source $`g_s\Phi_{x_s}`$ on the ring; $`W_{k,\sigma}(x)`$ the weight of the held body ($`\tau=0`$) at $`x`$; in (7.7) a start with real envelope $`\phi_j`$ in an isolated band, the coefficient of $`\tau^2`$ at first order in $`g_s`$.

Eq. (7.7) of 06-ilang-source/07-dressed-fall:

```math
a_{k,\sigma}(0)=-E''_{k,\sigma}(0)\sum_j\phi_{j+1}\phi_{j-1}\,W'_{k,\sigma}(j)+O(g_s^2)+O(\tau^4\gamma g_s).
\qquad\text{(7.7)}
```

From 07-ilang-weight/02-two-free-bodies@v3. Setting there: the setting above with regime R; $`\mathcal T`$ the joint translation of both bodies and all field objects, $`p_i`$, $`q_\alpha`$ the plane-wave labels of bodies and field objects; $`\mathcal U`$ the band transformation, $`\mathcal P_0`$ the projector on $`\mathcal G`$, $`H=\mathcal U^\dagger C\mathcal U`$; $`K_i`$ the second-order term of the motion term of $`b_i`$, which moves $`b_i`$ by $`0`$ or $`\pm2`$ places; $`\kappa(j,l)=\langle e_{j+1,l}\vert K_1\vert e_{j-1,l}\rangle=\bar\kappa+\delta\kappa(j,l)`$, $`\bar\kappa`$ the amplitude for $`b_1`$ alone with the field; $`\mu_i=1/E''_{k_i,\sigma_i}(0)`$ the inertia of body $`i`$ alone; $`R_i`$ half the difference of the $`\tau=0`$ eigenvalues of $`b_i`$ alone in its two branches (field lowest), $`R_i=M_i(1+\gamma_in)+O(\gamma_i^3)`$; in (2.16) upper sign (a), lower (c), $`M^{(2)}`$ the second-order part of $`M`$, $`\gamma_i\to\epsilon\gamma_i`$ the common scale.

Eq. (2.1) of 07-ilang-weight/02-two-free-bodies:

```math
[\mathcal T,C]=0,\qquad \mathcal T^L=\mathbb 1,\qquad \mathcal T=e^{-i\hat P},\quad P=p_1+p_2+\textstyle\sum_\alpha q_\alpha\in\tfrac{2\pi}{L}\mathbb Z_L , \qquad\text{(2.1)}
```

Eq. (2.3) of 07-ilang-weight/02-two-free-bodies:

```math
E(x_1,x_2)=\sigma_1M_1+\sigma_2M_2+N_f\,\varepsilon_0(x_1,x_2)=\mathrm{const}+M(x_1,x_2), \qquad\text{(2.3)}
```

Eq. (2.10) of 07-ilang-weight/02-two-free-bodies:

```math
H_{\rm eff}=\mathcal P_0H\mathcal P_0=W+K_1+K_2+O(\tau^4),\qquad W=\mathrm{diag}\,E(j,l)\ \text{of (2.3)}. \qquad\text{(2.10)}
```

Eq. (2.11) of 07-ilang-weight/02-two-free-bodies:

```math
E''_{k_1,\sigma_1}(0)=-\textstyle\sum_rr^2\bar\kappa_r=-8\bar\kappa , \qquad\text{(2.11)}
```

Eq. (2.14) of 07-ilang-weight/02-two-free-bodies:

```math
\mu_i=\sigma_i\frac{R_i}{\tau_i^2}+O(\gamma_i^2)\ \ \text{(a)},\qquad \mu_i=\sigma_i\frac{R_i}{\tau_i^2(1+\gamma_in)^2}+O(\gamma_i^2)\ \ \text{(c)}, \qquad\text{(2.14)}
```

Eq. (2.16) of 07-ilang-weight/02-two-free-bodies:

```math
\frac{\delta\kappa(j,l)}{\bar\kappa}=\mp\gamma_1\,\overline{\delta\rho}_l(j)+r_1(j,l),\qquad \overline{\delta\rho}_l(j):=\tfrac14[\delta\rho_l(j-1)+2\delta\rho_l(j)+\delta\rho_l(j+1)],\qquad \gamma_1\delta\rho_l(y)=\frac{\sigma_1M^{(2)}(y,l)}{M_1}+O(\gamma_1g_2^2),\qquad r_1=O(\epsilon^3), \qquad\text{(2.16)}
```

From 07-ilang-weight/04-weight-of-bond@v3. Setting there: held bodies ($`\tau_i=0`$) with point couplings $`g_i`$ at $`x_1`$, $`x_2=x_1+r`$ and a held source $`g_s`$ at $`x_s`$ on the field above (ring: $`\mathcal X=L`$); $`\ell=\Lambda^+`$, $`\ell^{(2)}=(\Lambda^+)^2`$, $`\ell_0=\ell(0)`$, $`\ell_{as}=\ell(x_a-x_s)`$; $`\eta=\max\lvert g_i\rvert\ell_0/t_f`$, $`\eta_i=\lvert g_i\rvert\ell_0/t_f`$; $`B`$ the bond function, $`\phi(x):=-\frac{2g_s}{t_f}\ell(x-x_s)`$; $`W_i`$ the weight of body $`i`$ alone, $`W_b`$ the bond part of the weight of the pair, $`W_{\rm pair}=W_1(x_1)+W_2(x_2)+W_b`$.

Eq. (4.3) of 07-ilang-weight/04-weight-of-bond:

```math
\ell(r)=\frac{L^2-1}{12L}-\frac{r(L-r)}{2L},\qquad E(r)-E(r')=\frac{ng_1g_2}{t_fL}\big[r(L-r)-r'(L-r')\big]+O\Big(n\lvert g_1g_2\rvert\frac{\ell_0}{t_f}\,\eta\Big).\qquad\text{(4.3)}
```

Eq. (4.5) of 07-ilang-weight/04-weight-of-bond:

```math
W_i(x)=ng_i\,\phi(x)+\frac{ng_sg_i^2}{t_f^2}\Big[2\ell_0\,\ell(x-x_s)+\ell(x-x_s)^2-\frac2{\mathcal X}\,\ell^{(2)}(x-x_s)\Big]+O\big(n\lvert g_s\rvert\eta_i^3\big),\qquad\text{(4.5)}
```

Eq. (4.7) of 07-ilang-weight/04-weight-of-bond:

```math
W_b(x_1;\mathbf r)=\tfrac12B(\mathbf r)\big[\phi(x_1)+\phi(x_2)\big]+\frac{ng_1g_2}{2g_s}\,\phi(x_1)\phi(x_2)-\frac{2ng_sg_1g_2}{t_f^2\mathcal X}\big[\ell^{(2)}_{1s}+\ell^{(2)}_{2s}\big].\qquad\text{(4.7)}
```

## Assumptions

- The setting under "Goal". The field, the bodies, their couplings, the field state, regime R and the binding regime are assumptions of the package (M8, M9).
- Standard mathematics applied to the stated operators may be used (perturbation theory for isolated eigenvalues, spectral theory of the band contract on the ring, Fourier analysis); state it with its conditions.

## Scope

- **Class.** Couplings (a) and (c) (each body with its own coupling), $`N_f\ge1`$, even $`L\ge6`$, the branch combinations and signs for which item 1 finds bound levels; regime R and the stated binding regime.
- **Control.** For each answer of items 2–4, a description of the class, or of a stated wider class, in which it fails, or a proof that there is none.
- Out of scope: the full grip (a later package, after 05-inertia-of-mark); the tori; the highest field state; bodies of one type; the speed of a front of the field (item 4 of the base problem).

## Depth

- Item 1: derive (needed by items 2–4).
- Item 2: derive (needed by item 3 of the base problem: the inertia of a bound pair).
- Item 3: derive (needed by item 3 of the base problem: inertia against cost).
- Item 4: derive (needed by item 3 of the base problem: weight over inertia for bound pairs against a single body).
- Item 5: short argument (needed by item 3 of the base problem: the role of the field).

## Expected result

- Item 1: the existence condition and an expression for $`E_b(P)`$ at the stated order.
- Item 2: an expression for the difference $`1/E_b''(0)-\mu_1-\mu_2`$ at its leading order, with its sources.
- Item 3: a yes/no answer at leading order, for equal and unequal speeds.
- Item 4: a yes/no answer at leading order, with the first order of a difference.
- Item 5: statements of the dependence on $`t_f`$.

Give every main result a tag $`(6.k)`$.

Consistency checks, at most three: for example $`\gamma_2\to0`$ (no binding), dimensions, and a limit of the binding regime.

## Code

Required: check: for $`N_f=1`$ on a ring of at least two even sizes, for both couplings and at least two parameter sets, item 2 against the curvature in $`P`$ of the exact bound level of two bodies and the field object (the sector contract continued in $`P`$), and item 4 for at least one case against exact eigenvalues with a held source.
