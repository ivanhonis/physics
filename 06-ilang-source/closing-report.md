# Closing report: 06-ilang-source

- **Subproject:** 06-ilang-source. Bodies as the source of the field, inside Ilanguage 1.b, with the space of 03-ilang-space, the time of 04-ilang-time and the fall of 05-ilang-free-fall.
- **Date:** 2026-10-19.
- **State:** all 7 derivation packages (02–08) are verified, and every one has had at least one external verification round. For 07 the last round judged the current version correct. The current versions of the other packages answer their last external round, and only the main model reviewed those answers (section 6). The dependency graph passes `graphcheck`.
- **Scope of this report:** it summarizes the verified results against the success criteria of `01-base-problem/problem.md`, citing packages and tags. It adds no results. Interpretations are marked as such.
- **Status labels:**
  - **proven**: derived at the physicist-formal standard (every step justified, standard facts used without proof), reviewed by the main model and checked by an external AI referee. It is not a formal proof.
  - **conditional**: proven under stated assumptions, for a stated class of descriptions, or to a stated order;
  - **candidate**: numerical evidence only;
  - **open**: not settled.
- **Workflow:** the derivations, reviews and external checks are made by AI models in a human–AI research workflow.
- **Tags:** (2.k)–(8.k) are tags of this subproject. Results of 03-ilang-space, 04-ilang-time and 05-ilang-free-fall are cited with their package name.

## 1. Question and approach

The question: can bodies make the field they fall in, inside Ilanguage 1.b? The stage 05-ilang-free-fall found that every positive result on the fall needs a common local scale on the whole internal contract of a body (R3 of 05-ilang-free-fall/17-typical-or-forced, (17.11)), and it took the field as given. Here the field is made by bodies. The questions: what a body presents to a field object; the sign and the profile of the field made by held sources; whether that field acts on another body as a common local scale; what a body's own field does to itself; and how special the couplings and field contracts are that give these results.

**Approach.**
- The field is one or several identical field objects (A10) without pair terms among them, with a coupled operator $`\Phi_x`$ at each place; in most packages a hopping field on a ring, square torus or cubic torus, with $`\Phi_x`$ the number of field objects at $`x`$.
- A body is Model D, coupled by a pair term $`\gamma\sum_xQ_x\otimes\Phi_x`$: (a) on its rest and clock term $`\sigma_3\otimes(m+D)`$, or (c) on its whole contract. A held body (A15) acts through the eigenvalue $`g`$ of its coupled operator.
- The field state is a named assumption (M9), mostly the lowest state adapted to the bodies present.
- **Lesson of the first wave.** For a pair term between a body and a field, "what a body presents" and "the mutual cost of two sources" depend on how the total contract is listed (M6). Fixed by the total contract are total costs, their dependence on the places of held bodies, their differences between states, eigenvalues of sectors, and accelerations. From 03 on, every result is stated through such quantities.

## 2. Answers at a glance

| # | Criterion | Status | Main packages and tags | Answer in one line |
|---|---|---|---|---|
| 1 | What a body presents | conditional | 02 (2.1), (2.3), (2.7), (2.9), (2.11)–(2.14) | At first order a body acts on the field through the expectation of its coupled operator; a branch start presents $`\gamma\sigma M_k^2/\omega_k`$ (a) or $`\gamma\sigma\omega_k`$ (c) and a pair the sum of its parts, but the per-body source is fixed only in a component split, while the generator of the field and additive changes between starts are fixed by the total contract. |
| 2 | Field of held sources | conditional | 03 (3.3), (3.6), (3.9), (3.14)–(3.16), (3.22), (3.26)–(3.28) | Held sources change the field by $`-g\chi_n`$; summed over all eigenvectors the mutual cost vanishes and the top of the spectrum mirrors the bottom, so the field contract alone never fixes the sign: attraction of like sources is a condition on the state (low end of the spectrum, or mixtures weighted towards it). |
| 3 | Profile | conditional | 04 (4.2), (4.4)–(4.7), (4.13), (4.15), (4.17), (4.19), (4.20); 08 (8.10), (8.15) | For conserved hopping objects in their lowest state the place dependence of the total cost is linear on a ring, logarithmic on a square torus and $`1/d`$ on a cubic torus; a gapped cell field is short range; the tie of field places to positions is the coupling map, which must be a scaled embedding. |
| 4 | The made field as a scale | conditional | 05 (5.1), (5.3)–(5.7), (5.15)–(5.17), (5.11)–(5.14), (5.16) | Yes, at first order in the test coupling: both couplings that multiply the whole rest and clock term make the field a common local scale (R3 at every place, every field state), with the clock ratio $`\nu(y)/\nu(x)`$, a fall from rest that does not depend on level or branch at the band point, and (4.24) with the local maximal speed; the rest-only coupling fails. |
| 5 | The body's own mark | conditional | 06 (6.2), (6.6)–(6.12); 07 (7.2), (7.6), (7.7)–(7.9) | The own mark lowers the cost and raises the inertia, rescales the clock commonly only at first order, and the inertia does not follow the cost; a body that makes a field falls universally in another one only at leading order: at relative order $`\gamma M_k/t_f`$ a level- and branch-dependent term appears. |
| 6 | Bonds through the field | open | — | Not treated. |
| 7 | A moving source | open | — | Not treated. |
| 8 | Typical or forced | conditional | 08 (8.2), (8.4)–(8.7), (8.8), (8.10), (8.12)–(8.15); 03 (3.14), (3.16) | The couplings that give a common local scale and a universal fall are exceptional (proper linear subspaces) and statable through the body's own contract, but not selected by the language; the long range of the made field is typical (open and dense in its class), selected by $`\Phi_x`$ carrying the density of the conserved number; the sign of the attraction is a condition on the state. |
| 9 | One medium | open | — | Not treated. |

The success line of the base problem (items 1–5 and 8) is met: every item of the line has a verified package. Items 6, 7 and 9 remain open, as the base problem allows.

## 3. Results by criterion

### I. A body that makes the field

**What a body presents** (criterion 1; 02-what-a-body-presents).
- **The coupling.** Both couplings are $`\gamma\sum_xQ_x\otimes\Phi_x`$ with $`Q^{(a)}_x=\Pi_xO`$, $`Q^{(c)}_x=\Pi_xO+\frac12(A_x+A_{x-1})`$ (2.1). At first order in $`\gamma`$ the field evolves by a generator $`C_f+\sum_xs_x\Phi_x`$, with the source field $`s_x=\gamma\langle Q_x\rangle`$ of the body's own evolution (2.3).
- **Branch starts, pairs.** A branch start on level $`k`$ presents $`\gamma\sigma M_k^2/\omega_k(p)`$ under (a) and $`\gamma\sigma\omega_k(p)`$ under (c) (2.7). A pair in an eigenvector of its contract presents the sum over its parts in the joint state; the binding term adds no term of its own (2.9), and a control with a branch-changing binding differs (2.10).
- **What is well defined.** The replacements that leave the total contract unchanged are exactly the moves of single-object operators (2.11). The component listing and its generator are fixed by the total contract (2.12). The per-body source, its total and the ratios between bodies are not; they are fixed only in the component split, and additive changes between starts are fixed (2.14). The zero of the body operator is a convention iff the traceless parts of all $`\Phi_x`$ are equal (2.13).

**Field of held sources** (criterion 2; 03-held-sources).
- **Exact reduction.** For a body start in one joint eigenspace of the coupled operators, the bodies stay in their start and the field evolves by $`C_f+g_1\Phi_{x_1}+g_2\Phi_{x_2}`$, exactly (3.3). A field start that does not depend on the sources carries no mutual cost (3.5).
- **Response.** With the response $`\chi_n`$ (3.6), source $`i`$ changes the field by $`-g_i\chi_n(y,x_i)`$ in the adapted eigenvector (3.9).
- **Sign.** Summed over all eigenvectors the mutual part vanishes (3.14); a symmetry that reverses the contract mirrors the top of the spectrum onto the bottom (3.15); mixtures with weights decreasing in the cost have a positive semidefinite response (3.16). For every field and two places, either all level responses vanish or both signs occur (3.22): the field contract and $`\Phi_x`$ alone never fix the sign of the mutual cost of like sources.
- **Invariant form.** The sector operators and their ordered eigenvalues are fixed by the total contract, and the invariant mutual cost of a change of both sources satisfies an exact sum rule (3.26), with second-order value (3.27). The family of configurations fixes the zeros of the coupled operators (3.28).

**Profile** (criterion 3; 04-profile; 08-typical-or-forced).
- **Lowest state.** For $`N_f`$ conserved hopping objects without mutual terms, the lowest state is a product, $`E=N_f\varepsilon_0(g)`$, exactly (4.2). The second-order mutual cost is $`-(2ng_1g_2/t_f)\Lambda^+(x_1,x_2)`$ (4.4); in invariant form it is the place dependence of the total cost (4.17).
- **Distance.** Ring: $`\propto d(L-d)-(L^2-1)/6`$ (4.5); square torus: logarithmic (4.6); cubic torus: $`1/d`$ (4.7). The higher orders are bounded explicitly (4.19). For like sources the total cost decreases as the sources approach in the lowest state, and increases in the highest state (4.13).
- **Short range.** A gapped cell field decays at least exponentially at all orders (4.20).
- **Field places and positions.** The mutual cost is the same function of the recorded distance as of the graph distance iff the coupling map is a scaled embedding (4.15); wrapping a longer chain onto the ring fails (4.16).

### II. The common local scale

**The made field as a scale** (criterion 4; 05-made-field-scale).
- **Effective contract.** A test body evolves by the partial expectation $`\bar C_\varphi`$ of the total contract in the field state (5.1). Its view of body and medium has no first-order error; the remainder is second order in $`\gamma`$ (5.15).
- **R3.** The level blocks are $`\nu(x)M_k\sigma_3`$ with $`\nu=1+\gamma N_\varphi`$, the hopping is $`\tau`$ for (a) and $`\tau\frac12(\nu(x)+\nu(x+1))`$ for (c) (5.3). R3 holds at every place in every field state, $`\Gamma(x)=\gamma\Delta N\sigma_3`$ (5.4). The rest-only coupling fails R3 and gives a level-dependent fall (5.5).
- **Clock and fall.** The clock ratio is $`r(y)/r(x)=\nu(y)/\nu(x)`$ for every pair of levels (5.6). The fall from rest at the band point $`p=0`$ is $`-\tau_{\rm loc}^2\gamma N'/\nu`$ for all levels and both branches, and (4.24) of 05-ilang-free-fall/04-branch-fall holds with the local maximal speed up to a curvature term (5.7). A start of finite momentum width falls with a relative correction $`\epsilon_k\le c_k\overline{\sin^2p}`$ that depends on the level in general (5.17).
- **Distance from the source.** In the lowest adapted state the made field is (5.8). The clock ratio and the fall in graph coordinates are (5.11)–(5.14): for $`g_s\gamma>0`$ the clock is slower nearer the source and the fall points towards it; for $`g_s\gamma<0`$ both reverse. Graph separation and recorded distance coincide on the test body's line iff the label separation is at most half the ring (5.16).

**The body's own mark** (criterion 5; 06-own-mark, 07-dressed-fall).
- **Dressed levels.** For (a) and (c) every clock level is dressed like a clockless body with rest parameter $`M_k`$, exactly (6.2). The own mark lowers the cost (6.6); for a held body it is $`-\gamma^2M_k^2N_f(L^2-1)/(12t_fL^2)`$ (6.7).
- **Clock.** The spacings are rescaled by the common factor $`1+\gamma n`$ at first order; at second order the change decreases with the level, so it is not a common rescaling (6.8), (6.9).
- **Inertia against cost.** The curvature is (6.10), (6.11). The change of the inertia is not the change of the cost divided by $`\tau^2`$: for (a) at second order, for (c) already at first order (6.12). Controls: $`\tau\to0`$ and the rest-only coupling (6.13), (6.14).
- **Weight.** A held body's weight in the field of another source is exactly a one-object eigenvalue (7.2). At first order in $`\gamma`$ it is $`\sigma M_k`$ times one function of the place; at second order its shape changes with $`\sigma M_k`$, so it does not factorize (7.6).
- **Fall.** In the regime of a heavy body and band dynamics, the drift acceleration is the projected lattice expression (7.7), (7.8). It is the same for all levels and both branches at leading order; at relative order $`\gamma M_k/t_f`$ a level- and branch-dependent term appears, odd in the branch, for every member of the class (7.9).

### IV. How special the structure is

**Typical or forced** (criterion 8; 08-typical-or-forced; 03-held-sources).
- **Couplings** (a class of $`5N`$ local linear couplings $`Q_x`$, test body, first order in $`\gamma`$). R3 at every place iff the on-site part of $`Q_x`$ is one branch operator times $`(m+D)`$ (8.2). A fall from rest that is equal across levels and branches adds rest at $`p=0`$ and no scalar part (8.4); the pure local scale, with the hopping scaled by the same factor, is $`\sum_xQ_x=\alpha C_{\rm D}`$ (8.5). These sets have dimensions $`N+4`$, $`N+2`$ and $`1`$ in $`5N`$: exceptional (8.6). A deviation breaks them at first order (8.7). They are statable through the body's own contract, but every coupling of the class is admissible, so the language does not select them (8.6).
- **Field contracts** (translation-invariant multi-band fields, coupled operator $`\lvert x\rangle\langle x\rvert\otimes\phi`$, lowest state). The response has the Bloch form (8.8). A short-range field needs a uniformly bounded response (8.14). Long range of Coulomb type holds wherever $`\Phi_x`$ carries the density of the conserved number of field objects (8.10), (8.12), and this set is open and dense in the class (8.15): long range is typical. A conserved charge that $`\Phi_x`$ changes gives short range, with an explicit member (8.13).
- **States.** The sign of the attraction is selected by the state, not by the contract (3.14)–(3.16), (3.22).

## 4. Cross-cutting findings (interpretation)

1. **The made field can be the common local scale.** The requirement found in 05-ilang-free-fall, that the field scale each level's internal block in proportion to its gap, is met by the field that held sources make, for both couplings that multiply the whole rest and clock term (5.4). The clock rate and the fall are then tied as in 05-ilang-free-fall (5.7). This is an interpretation of the cited results, not an additional result.
2. **Attraction is a property of the state.** No field contract fixes the sign of the mutual cost of like sources (3.22); the lowest state attracts, the highest repels (3.15), (4.13). The language selects no state (A11), so the attraction found here rests on a named state.
3. **Long range is typical, the scale is not.** In the classes studied, the long range of the made field follows from a conserved number carried by a gapless band and holds on an open dense set (8.15); the couplings that make it a common scale are an exceptional linear set (8.6). The first is close to forced, the second is a structure the language allows but does not select.
4. **A body that makes a field does not fall exactly universally.** Its own mark changes its weight and its inertia in different ways (6.12), (7.6), and its fall depends on the level at relative order $`\gamma M_k/t_f`$ (7.9). Universality holds for a test body, and for a source only at leading order.
5. **Only total costs and their differences are physical.** The split of a cost into "what a body presents" and "mutual cost" depends on the listing (2.14), (4.1). This continues the finding of 04-ilang-time and 05-ilang-free-fall that only differences of costs, and quantities built from them, are well defined.

## 5. What is missing, and open problems

- **Items 6, 7 and 9.** Bonds through the field, a moving source and the speed of a change of the field, and one medium for records and field are not treated.
- **Relaxation.** What brings the field into an adapted state is open (A11); the results rest on the named lowest state.
- **Orders and regimes.** The test body is at first order in its coupling (05); the own mark at second order (06); the fall of a source at the coefficient of $`\tau^2`$, first order in the source and relative order $`\gamma`$ (07). Uniform-in-$`L`$ perturbative regimes are not derived for the made field (08, (8.8)).
- **Classes.** The fields are conserved objects without mutual terms; field objects with $`c=-1`$ or with pair terms are not treated. Inside the exceptional complement of (8.15), degenerate or quartic band minima and the cases left by the leading order of the response are not classified.
- **Geometry.** Graph separation and recorded distance coincide only on part of a line (5.16); a record of the transverse separation on the tori is not part of the setting.

## 6. Quality record

**External verification** (an independent external referee model saw only the referee prompt, the base problem, the question without "Expected result", the derivation and its code):
- one round, minor issues, fixed by a regeneration: 06;
- major issues in the first round, minor issues or none in the second: 02, 03, 04 (round 1 on v2, after a review of the main model on v1), 05, 08, fixed by a regeneration; 07 (second round correct).

**Not externally re-checked.** The current versions of 02, 03, 04, 05, 06 and 08 answer their last external round, and only the main model reviewed those answers. These answers were corrections of conditions, ranges, normalizations and wording, in versions whose formulas the referee had confirmed. Two of them added content: in 06 v3 the second-order curvature of the rest-only controls (6.14), and in 08 v3 the restriction of the large-distance profile to stated sizes with the near-tie obstruction (8.10).

**Revised questions.**
- 05: a note on item 4 states that "place relative to the source" means graph coordinates, and asks where they coincide with the recorded geometry (2026-10-19, after the first external round).
- 06: items 2 and 3 were restricted: a stated parameter region suffices for the negative answers (2026-10-19, after the review of v1).
- 07: the isolation condition of 06-own-mark, first cited in words, was quoted (2026-10-19, after the first external round).
- 08: item 1 was fixed at first order in the coupling with equal falls across branches, and item 2 was restricted to an open dense subset of its class, without a classification of the exceptional members (2026-10-19, after the first external round).

**Known minor issues, not fixed.** None recorded.
