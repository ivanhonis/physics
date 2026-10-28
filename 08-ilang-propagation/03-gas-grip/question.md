# Question: 03-gas-grip

- **Subproject:** 08-ilang-propagation
- **Package:** 03-gas-grip
- **Equation tags:** (3.k)
- **Created:** 2026-10-24

## Goal

Determine which grips a body can have on the field of 06-ilang-source and 07-ilang-weight within pair terms, and, for those grips, whether the own mark and a bond made through the field are weighed like the first-order part of the cost. This is item 1 of the base problem for the field of identical objects. Every result is stated through quantities that the total contract and the state fix (M6).

**Setting.**
- **Field** (assumption, M8). The class of 06-ilang-source/04-profile: $`N_f\ge1`$ identical field objects ($`c=+1`$), no pair terms among them, on a ring ($`D=1`$), a square torus ($`D=2`$) or a cubic torus ($`D=3`$) of side $`L\ge3`$, $`\mathcal X=\lvert X_f\rvert=L^D`$; own term $`C_1=-t_f\sum_{\{x,y\}}(\lvert x\rangle\langle y\rvert+\lvert y\rangle\langle x\rvert)`$, $`t_f>0`$; $`\Phi_x`$ the number of field objects at $`x`$; $`n:=N_f/\mathcal X`$.
- **Bodies** (assumption, M8, A15). Held Model D bodies ($`\tau=0`$) in the eigenvector of $`S:=\sigma_3\otimes(m\mathbb 1_N+D)`$ with eigenvalue $`\sigma M_k`$, with the grip of the base problem, $`\sum_x\lvert x\rangle\langle x\rvert\otimes S\otimes F(\Phi_x)`$, $`F`$ a real function on the spectrum $`\{0,1,\dots,N_f\}`$ of $`\Phi_x`$, and no other rest and clock term. In 07-ilang-weight, coupling (a) is the grip $`F(\Phi)=1+\gamma\Phi`$ and the full grip is $`F(\Phi)=\gamma\Phi`$.
- **Source** (assumption, M8, A15). One held object at $`x_s`$ with the pair term $`g_s\Phi_{x_s}`$; first order in $`g_s`$.
- **State** (assumption, M9, A11). As in the quoted packages: the eigenvector of the total contract connected, as the couplings go to zero, to the bodies in their internal states and every field object in its lowest one-object state.
- **Cost, weight, bond and weighing ratios**: as defined in the quoted packages. The *first-order part* of the cost of a body is its part linear in the grip, as in (3.4) and (4.9) quoted below.

1. **Grips within pair terms.** Determine for which functions $`F`$ the grip term is a sum of pair terms (A5) between the body and single field objects, for $`N_f\ge2`$, and what changes for $`N_f=1`$.
2. **Weighing for these grips.** For the grips of item 1, determine for one held body the weight of its mark against its cost and against the weight of the first-order part of its cost, and for a pair bound through the field the weighing ratio of the bond, as functions of the parameters of the grip, for every level and both branches, at leading order and with the first breaking term, on the three graphs. Determine for which grips of item 1 (if any) the mark and the bond are weighed like the first-order part of the cost. Use the quoted results where they apply, and derive what they do not give.

**Note (2026-10-24, after the review of v2).** The setting of (4.12) quoted below omitted its conditions. The Result of 07-ilang-weight/04-weight-of-bond@v3 states for (4.12): on the ring $`\kappa^{\rm mid}`$ "is $`0`$ at leading order in η, for $`x_s`$ outside the arc between the bodies"; on the cubic torus the ratio is 1 "for $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d\ll L`$"; on the square torus "only for $`d`$ large against $`\lvert\mathbf r\rvert`$ times a logarithm of $`L`$". A result that uses (4.12) carries these conditions.

**Note (2026-10-24, after external round 1).** (a) The Result of 07-ilang-weight/04-weight-of-bond@v3 states for (4.10): "It holds for $`\ell(\mathbf r)\ne\ell(\mathbf r')`$, $`\Delta_{\mathbf e}\ell(\mathbf R)\ne0`$ and $`\eta K\ll1`$, including configurations with $`\rho_0=0`$." A result that uses (4.10) carries these conditions. (b) Item 2 asks the weight of a bond only for a source outside the pair: on the ring outside the arc between the bodies, on the tori at distances $`d`$ large against the separations, as in (4.12). The research needs the weight of a bond in the field of a distant source; a source between the bodies is out of scope.

## Inputs

From 07-ilang-weight/03-weight-of-mark@v2. Setting there: one held body at $`x`$ with coupling (a) ($`\theta=1`$) or the full grip ($`\theta=0`$), constant $`\gamma`$, $`g_b:=\sigma\gamma M_k`$; $`h_x=C_1+g_bP_x+g_sP_{x_s}`$ the one-object contract, $`\varepsilon_0(g)`$ the lowest eigenvalue of $`C_1+gP_x`$, $`c_s`$ the source's own eigenvalue; $`\ell(y):=\Lambda^+(x,x+y)`$ with $`\Lambda`$ the graph Laplacian, $`\ell_0:=\ell(0)`$, $`\ell^{(j)}:=(\Lambda^+)^j`$ in the same way; $`r:=x_s-x`$, $`r':=x_s-x'`$, $`[f]:=f(r)-f(r')`$; $`\delta N(x)=-\frac{2ng_s}{t_f}\ell(r)`$ the first-order made field of the source; $`\Delta W_{k,\sigma}:=W_{k,\sigma}(x)-W_{k,\sigma}(x')`$; $`\eta(g)=\mathcal X\delta(g)/t_f`$ with $`\delta`$ the shift of the lowest one-object eigenvalue; $`\Theta_D(x):=\frac{ng_s}{t_f^2}\bigl[\ell(r)^2+2\ell_0\ell(r)-\frac{2\ell^{(2)}(r)}{\lvert X_f\rvert}\bigr]`$ and $`T_2:=2[\ell^{(2)}]/(\lvert X_f\rvert[\ell])`$; regime $`\chi:=\lvert g_b\rvert\ell_0/t_f\ll1`$, and for (3.15) also $`\gamma\ne0`$, $`1+\gamma n\ne0`$, $`\lvert\gamma n\rvert\chi\ll\lvert1+\gamma n\rvert`$, for pairs of places with $`F\ne0`$.

Eq. (3.1) of 07-ilang-weight/03-weight-of-mark:

```math
E_{k,\sigma}(x)=\theta\sigma M_k+c_s+N_f\,\varepsilon_0(x),\qquad \varepsilon_0(x)=\min\mathrm{spec}h_x .\qquad\text{(3.1)}
```

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

Eq. (3.14) of 07-ilang-weight/03-weight-of-mark (full grip):

```math
\Delta W_{k,\sigma}=\mathrm{Cost}_{k,\sigma}F\bigl[1+B^{\rm fg}_{k,\sigma}\bigr],\qquad B^{\rm fg}_{k,\sigma}=-\frac{\eta}2\Bigl[\ell(r)+\ell(r')-\frac{2[\ell^{(2)}]}{\lvert X_f\rvert[\ell]}\Bigr]+O(\eta^2\ell^2),\quad \eta=\frac{\mathrm{Cost}_{k,\sigma}}{nt_f}=\frac{g_b}{t_f}+O(g_b^2).\qquad\text{(3.14)}
```

Eq. (3.15) of 07-ilang-weight/03-weight-of-mark (coupling (a)):

```math
\Delta W_{k,\sigma}=\mathrm{Cost}_{k,\sigma}F^{(a)}\bigl[1+B^{(a)}_{k,\sigma}\bigr],\quad F^{(a)}:=\frac{\gamma[\delta N]}{1+\gamma n},\quad B^{(a)}_{k,\sigma}=\frac{g_b[\Theta^{(a)}_D]}{[\delta N]}=-\frac{g_b}{2t_f}\Bigl[\ell(r)+\ell(r')+\frac{2\ell_0}{1+\gamma n}-T_2\Bigr],\quad \Theta^{(a)}_D:=\Theta_D+\frac{\gamma n}{1+\gamma n}\,\frac{\ell_0}{t_f}\,\delta N,\qquad\text{(3.15)}
```

From 07-ilang-weight/04-weight-of-bond@v3. Setting there: two held bodies at $`x_1`$ and $`x_2=x_1+\mathbf r`$, each with coupling (a) or the full grip and constant $`\gamma_i>0`$, $`g_i:=\sigma_i\gamma_iM^{(i)}_{k_i}`$, no pair term between them; $`E(x_1,\mathbf r)`$ the eigenvalue of the pair without the source; $`\ell`$, $`\ell^{(2)}`$ as above, $`\ell_{as}:=\ell(x_a-x_s)`$, $`\ell^{(2)}_{as}`$ likewise; $`\phi(x)=-\frac{2g_s}{t_f}\ell(x-x_s)`$; $`\mathbf R:=x_1-x_s`$, $`d`$ the length of its shortest representative; $`\eta:=\max(\lvert g_1\rvert,\lvert g_2\rvert)\ell_0/t_f<1/12`$; $`\Delta\mathcal C_i`$ the difference of the costs of body $`i`$ alone between two of its internal states, $`\Delta W_i`$ the corresponding difference of weights, $`\epsilon_F`$ the relative remainder stated there; $`W_b(x_1;\mathbf r)`$ the part of the weight of the pair beyond the weights of the bodies at their own places, $`S:=\ell(\mathbf r)(\ell_{1s}+\ell_{2s})+\ell_{1s}\ell_{2s}-(\ell^{(2)}_{1s}+\ell^{(2)}_{2s})/\mathcal X`$, $`\delta S:=(\ell(\mathbf r)+\ell_{1s})(\ell_{2s}-\ell_{1s})-(\ell^{(2)}_{2s}-\ell^{(2)}_{1s})/\mathcal X`$; $`\Delta_{\mathbf e}`$ a unit step of the pair as a whole, $`\Delta_{\mathbf r\mathbf r'}`$ the change $`\mathbf r\to\mathbf r'`$; $`K`$ the place-dependent quotient defined there; "mid" refers to the midpoint of the pair as its place; on the ring $`u=(d_1+\frac12)/L`$, $`v=(r-\frac12)/L`$, $`w=u+v`$.

Eq. (4.2) of 07-ilang-weight/04-weight-of-bond:

```math
E(x_1,\mathbf r)-E(x_1,\mathbf r')=B(\mathbf r)-B(\mathbf r')+O\Big(n\lvert g_1g_2\rvert\frac{\ell_0}{t_f}\,\eta\Big),\qquad B(\mathbf r):=-\frac{2ng_1g_2}{t_f}\,\ell(\mathbf r).\qquad\text{(4.2)}
```

Eq. (4.9) of 07-ilang-weight/04-weight-of-bond:

```math
\Delta W_i(x)-\Delta W_i(x')=\Delta\mathcal C_i\,\big[F_i(x)-F_i(x')\big]\big(1+\epsilon_F\big),\qquad F_i=\phi\ \ \text{(full grip)},\qquad F_i=\frac{n\gamma_i}{1+n\gamma_i}\,\phi\ \ \text{(coupling (a))},\qquad\text{(4.9)}
```

Eq. (4.10) of 07-ilang-weight/04-weight-of-bond:

```math
\rho_i:=\frac{\Delta_{\mathbf e}\Delta_{\mathbf r\mathbf r'}W_b(x_1;\cdot)}{\Delta_{\mathbf r\mathbf r'}B\;\Delta_{\mathbf e}F_i(x_1)},\qquad \rho_i^{\rm fg}=\rho_0+O(\eta K),\qquad \rho_0=\frac{\Delta_{\mathbf e}\Delta_{\mathbf r\mathbf r'}S}{2\,\Delta_{\mathbf r\mathbf r'}\ell\;\Delta_{\mathbf e}\ell(\mathbf R)}=1+\kappa,\qquad \kappa=\frac{\Delta_{\mathbf e}\Delta_{\mathbf r\mathbf r'}\delta S}{2\,\Delta_{\mathbf r\mathbf r'}\ell\;\Delta_{\mathbf e}\ell(\mathbf R)} .\qquad\text{(4.10)}
```

Eq. (4.12) of 07-ilang-weight/04-weight-of-bond:

```math
\kappa^{\rm mid}_{D=3}=O\Big(\frac{\lvert\mathbf r\rvert\lvert\mathbf r'\rvert}{d^2}\Big),\qquad \kappa^{\rm mid}_{D=2}=O\Big(\frac{\lvert\mathbf r'\rvert^2}{d^2}\ln\frac{L^2}{\lvert\mathbf r'\rvert d}\Big),\qquad \kappa^{\rm mid}_{\rm ring}=0,\qquad \rho_0^{\rm ring}=\frac{2(1-w)(1-2w)}{(1-2u)(1-2v)}.\qquad\text{(4.12)}
```

Eq. (4.13) of 07-ilang-weight/04-weight-of-bond:

```math
\rho_i^{(a)}=\frac{1+n\gamma_i}{n\gamma_i}\,\rho_i^{\rm fg}\,\big(1+O(\eta)\big),\qquad \rho_i^{{\rm mid},(a)}=\frac{1+n\gamma_i}{n\gamma_i}\,\rho_i^{\rm mid,fg}\,\big(1+O(\eta)\big).\qquad\text{(4.13)}
```

## Assumptions

- The setting under "Goal". The field class, the bodies, the grips, the source and the field state are assumptions of the package (M8, M9).
- The regimes of the quoted results; state the regime of every result.
- Standard mathematics applied to the stated operators may be used (operators on symmetric tensor products, polynomial interpolation on a finite set, perturbation theory for an isolated eigenvalue); state it with its conditions.

## Scope

- **Class.** Item 1: every real function $`F`$ on $`\{0,\dots,N_f\}`$ and every $`N_f\ge1`$. Item 2: every grip of item 1, every level and both branches, the three graphs, at the orders of the quoted results.
- **Cancellations.** Name the grips and internal states at which a cost, a first-order part or a denominator of a weighing ratio vanishes, and exclude them explicitly.
- **Control.** For each answer of item 2, a grip of item 1, or a description of a stated wider class, in which it fails, or a proof that there is none.
- Out of scope: field states other than the stated one; moving bodies and inertia; fields of cells (02-grip-weight).

## Depth

- Item 1: derive (needed by item 1 of the base problem: the grips admissible on this field; and by item 6).
- Item 2: derive where the quoted results do not suffice, short argument where they do (needed by item 1 of the base problem).

## Expected result

- Item 1: a characterization of the functions $`F`$, with the case $`N_f=1`$.
- Item 2: the weighing ratios of the mark and the bond as functions of the grip parameters, with the order and the range of distances, and the set of grips (possibly empty) for which they are those of the first-order part.

Give every main result a tag $`(3.k)`$.

Consistency checks, at most three: for example the two grips treated in 07-ilang-weight, and dimensions.

## Code

None.
