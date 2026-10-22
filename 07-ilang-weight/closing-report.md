# Closing report: 07-ilang-weight

- **Subproject:** 07-ilang-weight. Weight, inertia and cost of bodies that make the field, inside Ilanguage 1.b, with the space of 03-ilang-space, the time of 04-ilang-time, the fall of 05-ilang-free-fall and the made field of 06-ilang-source.
- **Date:** 2026-10-22.
- **State:** all 7 derivation packages (02–08) are verified. Every one has had at least one external verification round, and 05–08 have had all three. The current version of each package answers its last external round, and only the main model reviewed those answers (section 6). The dependency graph passes `graphcheck`.
- **Scope of this report:** it summarizes the verified results against the success criteria of `01-base-problem/problem.md`, citing packages and tags. It adds no results. Interpretations are marked as such.
- **Status labels:**
  - **proven**: derived at the physicist-formal standard (every step justified, standard facts used without proof), reviewed by the main model and checked by an external AI referee. It is not a formal proof.
  - **conditional**: proven under stated assumptions, for a stated class of descriptions, or to a stated order;
  - **candidate**: numerical evidence only;
  - **open**: not settled.
- **Workflow:** the derivations, reviews and external checks are made by AI models in a human–AI research workflow.
- **Tags:** (2.k)–(8.k) are tags of this subproject. Results of other subprojects are cited with their package name.

## 1. Question and approach

The question: are bodies that make the field they fall in weighed and resistant to acceleration in proportion to their cost? 06-ilang-source found that a body's own mark lowers its cost and raises its inertia, but that the change of the inertia is not the change of the cost over $`\tau^2`$ ((6.12) of 06-ilang-source/06-own-mark). Here the questions are: how two free bodies move under the field they make; whether the own mark and a bond made through the field are weighed like the other costs; whether the inertia of a body, and of a bound pair, is its cost divided by the square of one speed; whether the ratio of weight to inertia is the same for all levels and for bound pairs; and how fast a change of the field spreads.

**Approach.**
- The field is $`N_f`$ conserved hopping field objects without mutual terms, on a ring (most packages) or a square or cubic torus. The bodies are Model D, with coupling (a) (pair term on the rest and clock term), (c) (on the whole body contract) or the full grip (the rest and clock term only in the pair term with the field).
- The field state is a named assumption (M9): the lowest state adapted to the bodies, in some results also the highest.
- Weight is the place dependence of an eigenvalue in the field of a distant held source; inertia is the inverse curvature of a level in the total plane-wave label of bodies and field; cost is a difference of eigenvalues fixed by the total contract (M6). A moving body is followed in a band regime: isolated band, motion terms small against the gaps.
- Tuned cancellations (a vanishing sum of inverse inertias, a vanishing sum of couplings) are excluded where they occur, by dated notes in the questions.

## 2. Answers at a glance

| # | Criterion | Status | Main packages and tags | Answer in one line |
|---|---|---|---|---|
| 1 | Two free bodies | conditional | 02 (2.1), (2.2), (2.4), (2.9), (2.12)–(2.19) | The total label of bodies and field is conserved, that of the bodies alone is not; action equals reaction exactly at every order; one charge per body holds only at second order; the accelerations from rest are in the inverse ratio of the inertias, with a deviation of relative order $`\gamma_1\gamma_2`$. |
| 2 | Weight against cost | conditional | 03 (3.12)–(3.16); 04 (4.7), (4.10)–(4.14), (4.17) | The weight of a held body is one function of the cost of its mark, for all levels. With the full grip the own mark and a bond through the field are weighed like the costs at leading order (ring with the midpoint, cubic torus at large distance; square torus only at very large distance); with coupling (a) the rest term is not weighed and the bond is over-weighed by $`(1+n\gamma)/(n\gamma)`$. |
| 3 | Inertia against cost | conditional | 05 (5.7)–(5.17); 06 (6.3), (6.8), (6.10), (6.14), (6.17); 07 (7.3), (7.5), (7.7), (7.8), (7.11), (7.12) | One body: inertia = cost$`/v^2`$ with one speed at leading order, for all levels; no single speed at the next order. Bound pair: the inertia exceeds the sum of the parts by a lattice factor $`1/\beta_0`$, the binding cost enters the inertia twice ($`2\Delta E/v^2`$ at equal speeds), and at leading order the pair falls more slowly than its parts. |
| 4 | The speed of the field | conditional | 08 (8.5)–(8.7), (8.10), (8.14)–(8.17) | The change of the field has a front of finite speed $`2t_f`$ along the axes, but the long-range part of the static mark forms only on $`\lambda\propto d^2/t_f`$, never on a scale linear in $`d`$; in a weakly pinned harmonic field the mark forms at the front. |
| 5 | Typical or forced | open | — | Not treated as an item; some packages give partial information (section 3). |

The success line of the base problem (items 1–3) is met: every item of the line has a verified package. Items 4 and 5 may remain open by the base problem; item 4 has a verified package, item 5 is open.

## 3. Results by criterion

### I. Mutual motion

**Two free bodies** (criterion 1; 02-two-free-bodies).
- **Conserved quantities.** The joint translation of both bodies and all field objects commutes with the total contract, so the total plane-wave label of bodies and field is conserved (2.1). The label of the bodies alone is not: the field takes the recoil (2.2). For even $`L`$ a sublattice-branch label of each body is conserved as well (2.17).
- **Acting and acted upon.** For held bodies the eigenvalue depends on the positions only through the ring distance, is unchanged when the bodies exchange places, and the two forces are equal and opposite, exactly at every order in the couplings (2.3), (2.4). The mutual term is a product of one number per body and a function of the distance at second order, but not at third (2.9).
- **Mutual fall.** In a band regime, for the mean positions in a local chart (2.18), the accelerations from rest are $`-E''`$ of each dressed body times its envelope-weighted gradient of the held eigenvalue (2.12). For equal-width Gaussian starts the ratio of the mutual parts is minus the inverse ratio of the curvature inertias (2.13), with the inertias related to the rest costs by (2.14). The directions follow from the branches (2.15). The first deviation from the inertia ratio is of relative order $`\gamma_1\gamma_2`$, from each body's inertia being changed by the other's mark (2.16), (2.19).

### II. Weight, inertia and cost

**Weight against cost** (criterion 2; 03-weight-of-mark, 04-weight-of-bond).
- **Own mark.** The weight of a held body is exactly one function of the cost of its mark, for all levels, branches and both couplings (3.12), (3.13). With the full grip the weight is the cost times one place function at leading order, broken at the next order (3.14); only on the cubic torus does the break decay with the distance (3.16). With coupling (a) only the mark is weighed, not the rest term $`\sigma M_k`$ (3.15).
- **Bond through the field.** The bond is weighed by the same place function as the first-order costs, half at each body (4.7). With the full grip its weight per unit cost equals that of the costs at leading order: exactly on the ring with the midpoint as the pair's place, asymptotically on the cubic torus, and on the square torus only at distances large against the bond times $`\ln L`$ (4.10)–(4.12); at fixed places on the square torus the ratio diverges (4.17). With coupling (a) the bond is weighed $`(1+n\gamma_i)/(n\gamma_i)`$ times as strongly as the level costs (4.13). The highest field state mirrors the lowest (4.14).

**Inertia against cost, one body** (criterion 3; 05-inertia-of-mark).
- **Leading order.** For (a), (c) and the full grip, the inertia is the cost divided by $`v^2`$ with one speed for all levels and branches: $`v=\tau`$ for (a) and the full grip, $`v=\tau(1+\gamma n)`$ for (c) (5.7). The inertia is set by the branch-odd part of the cost (5.3).
- **Next order.** At order $`\gamma^2`$ there is no single speed. With the full grip the inertia misses the branch-even part of the mark, so level differences fail (5.8). For (c) one speed is excluded for every member of the class; for (a) it exists only on a set of parameters with empty interior, found numerically at isolated two-level ratios (5.9), (5.12).
- **Weight over inertia.** The factor that sets the fall from rest, $`E''\Delta W`$, is the same for all levels and branches at leading order; the first level and branch dependence is at relative order $`\gamma`$, with one coefficient for the three couplings, and at relative order $`\gamma^2`$ where that coefficient vanishes (5.10), (5.15)–(5.17). The fall law holds for the full grip as well, for the mean position in a chart (5.14).

**Inertia against cost, bound pair** (criterion 3; 06-inertia-of-pair for (a), (c); 07-inertia-of-pair-full-grip for the full grip). Results for the bound level made of bodies near rest, in a band regime, without tuned cancellations.
- **Inertia.** The inertia of the pair exceeds the sum of the inertias of its parts: $`1/E_b''-\mu_1-\mu_2=(\mu_1+\mu_2)(1-\beta_0)/\beta_0+D^{\rm mark}`$, with $`\beta_0<1`$ the bond overlap of the relative motion (6.8), (7.5). The first part comes from the lattice form of the bodies' bands together with the binding; it vanishes for weakly bound, wide pairs. The second part comes from each body's inertia being changed by the other's mark: the mutual term enters each body's inertia over its own speed squared, once per body (7.3); for (c) with the opposite sign (6.8).
- **Inertia against cost.** No universal identity "inertia difference = cost difference$`/c^2`$" holds, for any speed $`c\ge\min(c_1,c_2)`$ (6.10), (6.17), (7.7). In the regime where the mutual term dominates, with the full grip, the binding cost has inertia $`(\tau_1^{-2}+\tau_2^{-2})\Delta E`$, that is $`2\Delta E/v^2`$ at equal speeds, not $`\Delta E/v^2`$ (7.8).
- **Weight over inertia.** At leading order the weight of the bound level is the sum of the weights of its parts (6.12), and the pair's fall factor is $`\beta_0`$ times the inertia-weighted fall factor of its parts: the pair falls more slowly than its parts (6.14), (7.11). With the full grip, at the order of the mutual term, the bond is weighed by $`2\kappa_s`$ times the place function, against its inertia factor 2: on the ring, at equal speeds, the pair falls like its parts at this order only as the source's relative distance $`u\to0`$ ($`\kappa_s\to1`$); at finite $`u`$ the difference is proportional to $`1-\kappa_s`$ (7.10), (7.12). The fall law carries over to the bound level, for its centre of inertia, also with a fixed held source (6.13), (6.18), (7.14)–(7.17).
- **The hopping of the field.** The lattice parts fall as $`t_f^{-2/3}`$ and the mark parts as $`t_f^{-1}`$; no value of $`t_f`$ restores the proportions (6.15), (7.13).

### III. The field

**The speed of the field** (criterion 4; 08-field-speed). For the field class above, a held source switched on in the lowest state without it.
- **Front.** Ahead of $`2t_f\lambda=\rho`$ the change is exponentially small, at every order in the source (8.5). Along the lattice axes it arrives at $`\lambda=\rho/(2t_f)`$ up to $`O(\rho^{1/3}(\ln\rho)^{2/3})`$: the front speed is $`2t_f`$ (8.6), (8.7). In other directions only the absence of earlier arrival is derived.
- **Formation of the mark.** Behind the front the long-range part of the static mark forms on $`\lambda=|r|^2/(4t_f\zeta_D(\varepsilon))`$ (8.10), and on no scale linear in $`|r|`$ (8.14). On the torus only the average over $`\lambda`$ converges to the static mark (8.11).
- **Controls.** In a pinned harmonic field (field objects with pair terms) the mark forms at the front, linearly in the distance, as long as the pinning is weak on the scale of the distance ($`m_Y\rho\ll1`$) (8.15). A field with hopping of unbounded range has no finite front speed (8.16).
- **Speeds.** The front speed compared with a body's: $`v_f/\tau=2t_f/\tau`$; $`\tau<2t_f`$ keeps every velocity of a Model D body below the front (8.17).

### IV. How special the structure is

**Typical or forced** (criterion 5). Not treated as an item. Partial information: the descriptions with one speed at order $`\gamma^2`$ for coupling (a) form a set with empty interior (5.12); the bond is weighed like the costs only with the full grip (4.13); the formation of the mark at a finite speed needs a field outside the class used here (8.14), (8.15).

## 4. What it means (interpretation, not a result)

- **Leading order.** A single body that makes the field is weighed and resists acceleration in proportion to its cost, with one speed, for all levels (5.7), (5.10). Together with the results of 05-ilang-free-fall and 06-ilang-source, this gives a Newton-like behaviour at leading order, under the stated conditions.
- **Where it stops.** Every cost beyond the rest cost enters weight and inertia differently. The own mark: weight follows the whole mark, inertia only its branch-odd part (5.3), (5.8). The binding of a pair: its inertia contains the lattice part and the mutual term twice (6.8), (7.8), while its weight contains the mutual term with the place factor $`2\kappa_s`$ (7.10). In these descriptions the inertia comes from the bodies' own motion terms and the weight from their coupling to the field density; the two agree at leading order because both are proportional to the rest cost.
- **The field.** The field used here makes a long-range mark, but the mark forms diffusively, on $`d^2/t_f`$ (8.10), (8.14). A field whose mark forms at its front exists in a wider class (8.15); whether such a field also weighs every cost, and whether its speed can be tied to the bodies' speed, is not settled here.

## 5. Open points

- **Criterion 5** (typical or forced) is open.
- **Tori for the bound pair.** The pair results are derived on the ring; the place factor $`\kappa_s`$ is a property of the ring (7.9), (7.12). The weight of a moving bound pair on the tori is not treated.
- **Higher orders and tuned cases.** The orders beyond those stated, the tuned cancellations excluded by the dated notes, alternating and excited relative levels, and the highest field state for the pair are not treated.
- **Field speed.** Off the lattice axes only a lower bound on the arrival time is derived (8.7); the formation results are pointwise scaling limits (8.10).
- **Numbers.** The code checks use $`N_f=1`$; where the full space is too large, the checks use the band contract and are labelled so (07-inertia-of-pair-full-grip).

## 6. Verification state

| Package | Version | External rounds | Last external verdict | Current version checked by |
|---|---|---|---|---|
| 02-two-free-bodies | v3 | 2 | minor issues | main model |
| 03-weight-of-mark | v2 | 1 | minor issues | main model |
| 04-weight-of-bond | v3 | 2 | minor issues | main model |
| 05-inertia-of-mark | v4 | 3 | minor issues | main model |
| 06-inertia-of-pair | v4 | 3 | major errors | main model |
| 07-inertia-of-pair-full-grip | v4 | 3 | major errors | main model |
| 08-field-speed | v4 | 3 | minor issues | main model |

For 06 and 07 the last external round found major errors in the previous version. The current versions answer them, in part by restrictions of the questions recorded as dated notes, and rest on the main model's review alone.
