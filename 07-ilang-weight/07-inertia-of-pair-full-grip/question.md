# Question: 07-inertia-of-pair-full-grip

- **Subproject:** 07-ilang-weight
- **Package:** 07-inertia-of-pair-full-grip
- **Equation tags:** (7.k)
- **Created:** 2026-10-21

## Goal

Determine, for two moving bodies with the full grip bound through the field they make, the inertia of the bound pair against the inertias of its bodies and against its cost, and the ratio of its weight to its inertia against that of each body alone. In particular, determine whether the cost of the binding contributes to the inertia and to the weight in the same proportion as the costs of the single bodies. This completes item 3 of the base problem for bound pairs, for the full grip. Every result is stated through quantities that the total contract and the state fix (M6).

**Setting.**
- **Field.** $`N_f\ge1`$ identical field objects ($`c=+1`$) on a ring of even length $`L\ge6`$, no pair terms among them, own term $`C_1=-t_f\sum_x(\lvert x\rangle\langle x+1\rvert+\lvert x+1\rangle\langle x\rvert)`$, $`t_f>0`$, $`\Phi_x`$ the number of field objects at $`x`$, $`n:=N_f/L`$.
- **Bodies.** Two Model D bodies $`b_1,b_2`$ of different types (base problem, "Notation and conventions") on the same ring of position labels, with parameters $`\tau_i`$, $`m_i`$, clock levels $`k_i`$ with half-gaps $`M_i`$, branches $`\sigma_i`$, each with the full grip of the base problem ("Couplings": own contract the motion term $`A`$ only; the rest and clock term only in the pair term $`\gamma_i\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m_i\mathbb 1_N+D_i)\otimes\Phi_x`$), with real constants $`\gamma_i\neq0`$, $`g_i:=\sigma_i\gamma_iM_i`$. There is no pair term between $`b_1`$ and $`b_2`$. Records at $`\kappa\to0`$.
- **State of the field** (assumption, M9): the lowest state adapted to the bodies.
- **Regime** (assumption, to be stated): the band regime of 07-ilang-weight/02-two-free-bodies (isolated group $`\mathcal G`$ of held levels, motion terms small against its distances to the other held levels, order $`\tau_i^2`$ in the band contract), with the distances of the full grip ((5.4) of 07-ilang-weight/05-inertia-of-mark, quoted below), and a binding regime.
- **Selected level**, as in 07-ilang-weight/06-inertia-of-pair: the bound level of the band contract at the edge of the relative band where both bodies are near rest (the lowest where the relative inertia is positive, the highest where it is negative), in the sector of total label $`P`$; $`E_b(P)`$ its eigenvalue.
- **Out of scope from the start** (tuned cases; the base problem needs the general behaviour): a near-cancellation of the relative hopping ($`\mu_1^{-1}+\mu_2^{-1}`$ small against $`\max_i\lvert\mu_i^{-1}\rvert`$); in item 4, a near-cancellation of the first-order weights ($`g_1+g_2`$ small against $`\max_i\lvert g_i\rvert`$); alternating extreme levels and excited levels of the relative motion. State the hierarchy that keeps the omitted orders small against the retained terms.
- **Positions.** Any mean position on the ring is a chart observable, well defined for the starts used (for example the centre of 07-ilang-weight/06-inertia-of-pair in a local chart away from the place where the labels close).

1. **Band contract and bound level.** Determine the band contract of the pair with the full grip, the regime in which it holds, and whether (6.1), (6.5), (6.6) of 07-ilang-weight/06-inertia-of-pair (quoted below, derived there for couplings (a) and (c)) hold for the full grip. Determine for which branches and signs the selected level is bound.
2. **Inertia of the pair.** Determine $`1/E_b''(0)`$ and compare it with $`\mu_1+\mu_2`$, the inertias of the bodies alone with the full grip ((5.3), (5.7) of 07-ilang-weight/05-inertia-of-mark): the difference at its leading order, and the dependence of each body's local inertia on the other body's mark, at the order of the mutual term.
3. **Inertia against cost.** With the cost of the bound pair defined through eigenvalue differences fixed by the total contract (as (6.9) of 07-ilang-weight/06-inertia-of-pair, against the descriptions with one body and without bodies), determine:
   - (i) whether the difference of item 2 equals the corresponding difference of cost divided by the square of the speed $`v`$ of (5.7) for the full grip, at leading order;
   - (ii) in a regime, to be stated, in which the part of the difference that comes from the lattice form of the bodies' bands is small against the part that comes from the mutual term, whether the contribution of the mutual term (the binding cost) to the inertia equals that cost divided by $`v^2`$, at its leading order.
4. **Weight over inertia.** With the source at a distance large against the size of the pair, determine the weight of the selected level through the order of the mutual term, including the weight of the bond ((4.7) of 07-ilang-weight/04-weight-of-bond, quoted below), and the factor that sets the fall from rest, $`E_b''(0)`$ times the weight difference. Compare it with the same factor for each body alone ((5.14) of 07-ilang-weight/05-inertia-of-mark). Determine whether they are equal at leading order, and at the order of the mutual term in the regime of item 3 (ii): whether the binding cost is weighed in the same proportion as it contributes to the inertia.
5. **The hopping of the field.** State how the answers of items 2–4 depend on $`t_f`$ at fixed $`n`$, $`\gamma_i`$, $`M_i`$, $`\tau_i`$, at leading order.

## Inputs

From 07-ilang-weight/02-two-free-bodies@v3. Setting there: two bodies on the ring field above (couplings (a), (c) there); $`\mathcal T`$ the joint translation of both bodies and all field objects, $`p_i`$, $`q_\alpha`$ the plane-wave labels of bodies and field objects; $`\mathcal U`$ the band transformation, $`\mathcal P_0`$ the projector on the group $`\mathcal G=\{e_{jl}\}`$ of held levels ($`b_1`$ at $`j`$, $`b_2`$ at $`l`$, field in the lowest held state), $`H=\mathcal U^\dagger C\mathcal U`$; $`E(j,l)`$ the held-pair eigenvalue; $`K_i`$ the second-order term of the motion term of $`b_i`$, moving $`b_i`$ by $`0`$ or $`\pm2`$ places.

Eq. (2.1) of 07-ilang-weight/02-two-free-bodies:

```math
[\mathcal T,C]=0,\qquad \mathcal T^L=\mathbb 1,\qquad \mathcal T=e^{-i\hat P},\quad P=p_1+p_2+\textstyle\sum_\alpha q_\alpha\in\tfrac{2\pi}{L}\mathbb Z_L , \qquad\text{(2.1)}
```

Eq. (2.10) of 07-ilang-weight/02-two-free-bodies:

```math
H_{\rm eff}=\mathcal P_0H\mathcal P_0=W+K_1+K_2+O(\tau^4),\qquad W=\mathrm{diag}\,E(j,l)\ \text{of (2.3)}. \qquad\text{(2.10)}
```

From 06-ilang-source/04-profile@v4. Setting there: held sources $`g_i\Phi_{x_i}`$ at $`x_1,x_2`$ on the field above; $`\varepsilon_0(g)`$ the lowest one-object eigenvalue with the sources; $`M`$ the mutual term.

Eq. (4.2) of 06-ilang-source/04-profile:

```math
E(g)=N_f\,\varepsilon_0(g),\qquad M=N_f\bigl[\varepsilon_0(g_1,g_2)-\varepsilon_0(g_1,0)-\varepsilon_0(0,g_2)+\varepsilon_0(0,0)\bigr].\qquad\text{(4.2)}
```

From 07-ilang-weight/04-weight-of-bond@v3. Setting there: held bodies with point couplings $`g_i`$ at $`x_1`$, $`x_2=x_1+\mathbf r`$ and a held source $`g_s`$ at $`x_s`$ on the field above (ring: $`\mathcal X=L`$); $`\ell=\Lambda^+`$, $`\ell^{(2)}=(\Lambda^+)^2`$, $`\ell_0=\ell(0)`$, $`\ell_{as}=\ell(x_a-x_s)`$; $`\eta=\max\lvert g_i\rvert\ell_0/t_f`$, $`\eta_i=\lvert g_i\rvert\ell_0/t_f`$; $`\phi(x):=-\frac{2g_s}{t_f}\ell(x-x_s)`$; $`W_i`$ the weight of body $`i`$ alone, $`W_b`$ the bond part of the weight of the pair.

Eq. (4.2) of 07-ilang-weight/04-weight-of-bond:

```math
E(x_1,\mathbf r)-E(x_1,\mathbf r')=B(\mathbf r)-B(\mathbf r')+O\Big(n\lvert g_1g_2\rvert\frac{\ell_0}{t_f}\,\eta\Big),\qquad B(\mathbf r):=-\frac{2ng_1g_2}{t_f}\,\ell(\mathbf r).\qquad\text{(4.2)}
```

Eq. (4.5) of 07-ilang-weight/04-weight-of-bond:

```math
W_i(x)=ng_i\,\phi(x)+\frac{ng_sg_i^2}{t_f^2}\Big[2\ell_0\,\ell(x-x_s)+\ell(x-x_s)^2-\frac2{\mathcal X}\,\ell^{(2)}(x-x_s)\Big]+O\big(n\lvert g_s\rvert\eta_i^3\big),\qquad\text{(4.5)}
```

Eq. (4.7) of 07-ilang-weight/04-weight-of-bond:

```math
W_b(x_1;\mathbf r)=\tfrac12B(\mathbf r)\big[\phi(x_1)+\phi(x_2)\big]+\frac{ng_1g_2}{2g_s}\,\phi(x_1)\phi(x_2)-\frac{2ng_sg_1g_2}{t_f^2\mathcal X}\big[\ell^{(2)}_{1s}+\ell^{(2)}_{2s}\big].\qquad\text{(4.7)}
```

From 07-ilang-weight/05-inertia-of-mark@v4. Setting there: one body on the ring field above with coupling (a), (c) or the full grip (FG), $`\theta=1`$ for (a), (c) and $`0`$ for FG, $`g_\sigma=\sigma\gamma M_k`$; the sector contract $`C_k(P)=\hat C^{(0)}+e^{-iP}\hat C^{(+)}+e^{iP}\hat C^{(+)\dagger}`$ in relative field coordinates, $`T_\pm`$ shifting all relative places by $`\pm1`$, $`\Phi_0`$ the number of field objects at the body; $`\mathrm{Cost}_{k,\sigma}`$ the held cost; $`\Omega_\sigma`$ the held field state of branch $`\sigma`$, $`R_k`$ and $`C^{\rm ev}_k`$ the branch-odd and branch-even parts of the cost, $`a_{k,\sigma}=\langle\Omega_{-\sigma}\vert K\vert\Omega_\sigma\rangle`$, $`J^{\rm exc}`$ the part of the curvature amplitude from excited field states; $`\mu_{k,\sigma}=1/E''_{k,\sigma}(0)`$; $`\varepsilon_1`$ the first excitation energy of one field object; $`d_{k,\sigma}`$ the distance of the held level from the rest of the held spectrum; in (5.14), $`a_{k,\sigma}(0)`$ the acceleration from rest of the mean position in a chart cut at a bond, $`\phi_j`$ the real envelope of the start in the dressed band, $`W`$ the held weight in the field of a held source $`g_s`$, $`d_s`$ the distance of the held band with the source, $`p_c`$ the weight of the start near the cut.

Eq. (5.1) of 07-ilang-weight/05-inertia-of-mark:

```math
\hat C^{(0)}=\sum_{\sigma=\pm}\lvert\sigma\rangle\langle\sigma\rvert\otimes\hat C^{(0)}_\sigma,\quad \hat C^{(0)}_\sigma=\theta\sigma M_k+C_1+g_\sigma\Phi_0,\qquad \hat C^{(+)}=\frac\tau2(-i\sigma_1)\otimes K,\quad K=\begin{cases}T_-&\text{(a), FG}\\ T_-\bigl(1+\frac\gamma2(\Phi_0+\Phi_1)\bigr)&\text{(c)}\end{cases}
\qquad\text{(5.1)}
```

Eq. (5.3) of 07-ilang-weight/05-inertia-of-mark:

```math
\mathrm{Cost}_{k,\sigma}=\sigma R_k+C^{\rm ev}_k,\qquad J_{k,\sigma}=\frac{a_{k,\sigma}^2}{2\sigma R_k}+J^{\rm exc}_{k,\sigma},\qquad \mu_{k,\sigma}=\frac{\sigma R_k}{\tau^2\bigl(a^2_{k,\sigma}+2\sigma R_kJ^{\rm exc}_{k,\sigma}\bigr)}\quad\text{at order }\tau^{-2},\qquad\text{(5.3)}
```

Eq. (5.4) of 07-ilang-weight/05-inertia-of-mark:

```math
\tau<\tfrac12d_{k,\sigma},\qquad d_{k,\sigma}\simeq\begin{cases}\min\bigl(2n|\gamma|M_k,\ \varepsilon_1\bigr),&\sigma\gamma<0,\\ \min\bigl(2n|\gamma|M_k,\ \varepsilon_1-2n|\gamma|M_k\bigr),&\sigma\gamma>0,\ 2n|\gamma|M_k<\varepsilon_1,\end{cases}\qquad \varepsilon_1=2t_f\Bigl(1-\cos\frac{2\pi}L\Bigr).\qquad\text{(5.4)}
```

Eq. (5.7) of 07-ilang-weight/05-inertia-of-mark:

```math
\mu_{k,\sigma}=\frac{\mathrm{Cost}_{k,\sigma}}{v^2}+O(\gamma^2)\ \text{ for every }k,\sigma,\qquad v=\tau\ \text{ (a), FG},\qquad v=\tau(1+\gamma n)\ \text{ (c)}.\qquad\text{(5.7)}
```

Eq. (5.14) of 07-ilang-weight/05-inertia-of-mark:

```math
a_{k,\sigma}(0)=-E''_{k,\sigma}(0)\sum_j\phi_{j+1}\phi_{j-1}W'_{k,\sigma}(j)+\epsilon_{\rm cut}+O\Bigl(\frac{\tau^2N_f^2g_s^2}{d_s^2}\Bigr)+O\Bigl(\frac{\tau^4N_f|g_s|}{d_s^3}\Bigr),\qquad |\epsilon_{\rm cut}|\le L\tau(\tau+N_f|g|)\,p_c,\qquad\text{(5.14)}
```

From 07-ilang-weight/06-inertia-of-pair@v4. Setting there: two bodies with couplings (a) or (c) in the band regime; $`\psi(j,l)=e^{iPj}g(l-j)`$ in the sector $`P`$, $`r=l-j`$; $`\kappa_1(\rho)`$, $`\kappa_2(\rho)`$ the hop amplitudes of $`K_1`$, $`K_2`$ across the relative bond $`\rho`$, $`d_i`$ the diagonal of $`K_i`$, $`U=E+d_1+d_2`$; $`\bar\kappa_i`$ the amplitudes of each body alone, $`\bar t_0=\bar\kappa_1+\bar\kappa_2`$, $`\mu_i=-1/(8\bar\kappa_i)`$; $`f_0`$ the real eigenvector of $`h_0`$ for the selected level; $`\tilde\Phi`$ the flux of the relative ring and $`\epsilon_0`$ the level as a function of bond magnitudes and flux; $`\rho_L`$ the ring remainder, $`E''_{\rm line}=\sum_\rho b_0/m`$; $`s_c=+1`$ for (a), $`-1`$ for (c), $`c_i`$ the speeds of (5.7) for (a), (c), $`\bar M^{(2)}(\rho)=\frac14[M^{(2)}(\rho-1)+2M^{(2)}(\rho)+M^{(2)}(\rho+1)]`$ with $`M^{(2)}`$ the second-order part of $`M`$; $`E_i(0)`$ the band level of $`b_i`$ alone at $`P=0`$, $`E_\varnothing`$ the lowest level of the field alone, $`\Delta E_0=E_b(0)-E_1(0)-E_2(0)+E_\varnothing`$; $`V`$ the relative potential; in (6.13), $`\hat Y`$ the centre conjugate to $`P`$, $`\varphi_X`$ the real envelope of the start, $`W_{\rm pair}`$ the held-pair weight, $`W'_0`$ the central difference of the weight of the bound level, $`\partial_i`$ the central difference in $`x_i`$.

Eq. (6.1) of 07-ilang-weight/06-inertia-of-pair:

```math
(h_Pg)(r)=U(r)g(r)+t(r+1;P)\,g(r+2)+t(r-1;P)^*g(r-2),\qquad t(\rho;P):=\kappa_1(\rho)e^{-2iP}+\kappa_2(\rho),\qquad U:=E+d_1+d_2. \qquad\text{(6.1)}
```

Eq. (6.5) of 07-ilang-weight/06-inertia-of-pair:

```math
b_0(\rho):=f_0(\rho-1)f_0(\rho+1),\qquad\beta_0:=\sum_\rho b_0(\rho),\qquad m(\rho):=-\frac1{8\kappa_1(\rho)}-\frac1{8\kappa_2(\rho)}. \qquad\text{(6.5)}
```

Eq. (6.6) of 07-ilang-weight/06-inertia-of-pair:

```math
E_b''(0)=\sum_\rho\frac{b_0(\rho)}{m(\rho)}+\tilde\Phi'(0)^2\,\partial_{\tilde\Phi}^2\epsilon_0,\qquad\tilde\Phi'(0)\simeq-\frac{L\mu_2}{\mu_1+\mu_2}. \qquad\text{(6.6)}
```

Eq. (6.8) of 07-ilang-weight/06-inertia-of-pair:

```math
D_0:=\frac1{E_b''(0)}-\mu_1-\mu_2=\underbrace{(\mu_1+\mu_2)\frac{1-\beta_0}{\beta_0}}_{D^{\rm lat}_0}+\underbrace{\frac{s_c}{\beta_0^2}\Big(\frac1{c_1^2}+\frac1{c_2^2}\Big)\sum_\rho b_0(\rho)\bar M^{(2)}(\rho)}_{D^{\rm mark}_0}-\frac{\rho_L}{E''_{\rm line}}+O\Big(\frac{\varepsilon^3(\lvert\mu_1\rvert+\lvert\mu_2\rvert)}{\beta_0},\frac{\bar x^2\lvert m_0\rvert}{\beta_0},\frac{\rho_L^2}{E''_{\rm line}}\Big). \qquad\text{(6.8)}
```

Eq. (6.9) of 07-ilang-weight/06-inertia-of-pair:

```math
\Delta E_0=\langle M\rangle_0+K_0+O(\varepsilon^2\lvert\bar\kappa\rvert),\qquad K_0:=2\bar t_0(\beta_0-1),\qquad\langle M\rangle_0=\sum_rf_0(r)^2M(r)=M(0)+\langle V\rangle_0+O\big(n\lvert g_1g_2\rvert\ell_0\eta/t_f\big). \qquad\text{(6.9)}
```

Eq. (6.13) of 07-ilang-weight/06-inertia-of-pair:

```math
a_0(0)=-\sum_X\varphi_X^2\sum_\rho\frac{b_0(\rho)}{m(\rho)}\,(\partial_1+\partial_2)W_{\rm pair}\big\vert_{X,\rho}\big[1+O(w^{-2})\big]=-E''_{\rm line}\sum_X\varphi_X^2\,W'_0(X)\big[1+O(w^{-2})\big]+O(\varepsilon^2g_sE''_{\rm line})+O(g_s^2)+O(\tau^4\gamma g_s), \qquad\text{(6.13)}
```

## Assumptions

- The setting under "Goal". The field, the bodies, the full grip, the field state, the band regime and the binding regime are assumptions of the package (M8, M9).
- Standard mathematics applied to the stated operators may be used (perturbation theory for isolated eigenvalues, spectral theory of the band contract on the ring, Fourier analysis); state it with its conditions.

## Scope

- **Class.** The full grip for both bodies, $`N_f\ge1`$, even $`L\ge6`$, the branch combinations and signs for which item 1 finds the selected level bound, in the stated regimes, without the tuned cases named under "Goal".
- **Control.** For each answer of items 2–4, a description of the class, or of a stated wider class, in which it fails, or a proof that there is none.
- Out of scope: couplings (a), (c) (done in 07-ilang-weight/06-inertia-of-pair); the tori; the highest field state; bodies of one type; the speed of a front of the field (08-field-speed).

## Depth

- Item 1: derive the full-grip band contract and the regime; short argument for the carry-over of (6.1), (6.5), (6.6) (needed by items 2–4).
- Item 2: derive (needed by item 3 of the base problem: the inertia of a bound pair).
- Item 3: derive (needed by item 3 of the base problem: inertia against cost, and whether the binding cost has inertia in proportion to it).
- Item 4: derive (needed by item 3 of the base problem: weight over inertia for bound pairs against a single body).
- Item 5: short argument (needed by item 3 of the base problem: the role of the field).

## Expected result

- Item 1: the band contract, the regime, and the condition under which the selected level is bound.
- Item 2: an expression for $`1/E_b''(0)-\mu_1-\mu_2`$ at its leading order and the mark part, with their sources.
- Item 3: yes/no answers for (i) and (ii), with the orders and the regime of (ii).
- Item 4: yes/no answers at leading order and at the order of the mutual term in the regime of item 3 (ii), with the first order of a difference.
- Item 5: statements of the dependence on $`t_f`$.

Give every main result a tag $`(7.k)`$.

Consistency checks, at most three: for example $`\gamma_2\to0`$ (no binding), the single-body limit against (5.7), and dimensions.

## Code

**Note (2026-10-22, after external round 3).** An exact check of the full laboratory contract with a held source is feasible only at small rings (its dimension grows as $`2L^3`$), while the regime of item 3 (ii) needs large rings. So item 4 is checked against exact eigenvalues with the held source at the sizes the full space allows, and in the regime of item 3 (ii) against the band contract in laboratory coordinates with the held source, each labelled as such. Statements in the narrow-pair regime may be restricted to one parity class of the relative position, stated as such.

Required: check: for $`N_f=1`$ on a ring of at least two even sizes, for at least two parameter sets, item 2 against the curvature in $`P`$ of the exact bound level of two full-grip bodies and the field object (the sector contract continued in $`P`$), and item 4 for at least one case against exact eigenvalues with a held source, including a case in the regime of item 3 (ii).
