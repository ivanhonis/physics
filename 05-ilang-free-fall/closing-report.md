# Closing report: 05-ilang-free-fall

- **Subproject:** 05-ilang-free-fall. Clocks and free fall of a body in a field, inside Ilanguage 1.b, with the space of 03-ilang-space and the time of 04-ilang-time.
- **Date:** 2026-10-18.
- **State:** all 16 derivation packages (02–17) are verified, and every one has had at least one external verification round. For 02 and 14 the last round judged the current version correct. The current versions of the other packages answer their last external round, and only the main model reviewed those answers (section 6). The dependency graph passes `graphcheck`.
- **Scope of this report:** it summarizes the verified results against the success criteria of `01-base-problem/problem.md`, citing packages and tags. It adds no results. Interpretations are marked as such.
- **Status labels:**
  - **proven**: derived at the physicist-formal standard (every step justified, standard facts used without proof), reviewed by the main model and checked by an external AI referee. It is not a formal proof.
  - **conditional**: proven under stated assumptions, for a stated class of descriptions, or to a stated order;
  - **candidate**: numerical evidence only;
  - **open**: not settled.
- **Workflow:** the derivations, reviews and external checks are made by AI models in a human–AI research workflow.
- **Tags:** (2.k)–(17.k) are tags of this subproject. Results of 03-ilang-space and 04-ilang-time are cited with their package name.

## 1. Question and approach

The question: what happens to a body, and to the clock it carries, when a field object acts on it, inside Ilanguage 1.b? Does the clock rate depend on the place, does the body fall with an acceleration that does not depend on the body, how are the two tied, and under which contracts? Second, how special are the contracts that give this (M8–M10 of the base problem keep the two questions apart).

**Approach.**
- A field is an object (A10), coupled to the body by pair terms. A *lapse-type* term multiplies an operator $`G`$ of the body's internal labels by a field operator $`\Phi_x`$ at each position $`x`$. The field is *sharp* in a state where every $`\Phi_x`$ has a definite value $`N(x)`$, the lapse profile.
- The body is mostly Model D: position, branch and clock labels, a hopping term $`\propto\sigma_1`$ and a rest and clock term $`\sigma_3\otimes(m+D)`$. The body sees a position-dependent level block on each clock level $`k`$: rest term $`M_{x,k}`$, plain on-site cost $`V_{x,k}`$ and hopping $`\tau\zeta_{x,k}`$. With linear profiles, the gradients are $`G_k`$, $`\mathcal F_k`$ and $`g_{\zeta,k}`$.
- The *fall* is the drift acceleration of a start in one branch: the long-window average of the first-order acceleration, then the limit of a sharp plane-wave label. The *rate at a place* is the advance of the clock distribution of a wide start, per unit of $`\lambda`$. Two rates are compared as a ratio of two runs at equal $`\lambda`$ (A8).
- Universality (items 4–7) is tested level by level, branch by branch, against the speed of the body, for two types, for fields that are not sharp, and for bound pairs.

## 2. Answers at a glance

| # | Criterion | Status | Main packages and tags | Answer in one line |
|---|---|---|---|---|
| 1 | Field as an object | proven | 02 (2.3)–(2.6), (2.11), (2.16), (2.29) | In a sharp stationary field state the body evolves exactly by an effective contract with the profile as a position-dependent factor, its view stays pure, and a reduced admissible description exists; a field that is not sharp acts as a mixture of such evolutions. |
| 2 | Clock rate in a field | conditional | 03 (3.23), (3.24), (3.36); 05 (5.17), (5.19), (5.21); 06 (6.10), (6.13), (6.15) | The rate at a place is set by the factor on the clock term, $`\eta_x/\lambda_0`$ for a wide start; the ratio of two rates, from two runs at equal $`\lambda`$, is well defined, while the ratio of the parameters is not. |
| 3 | Free fall | conditional | 03 (3.15), (3.28); 04 (4.7), (4.11), (4.16), (4.17) | A body in one branch falls from rest with $`\frac{\tau^2}{M_k}(\sigma\mathcal F_k-G_k)`$, at first order in the gradients; the fall depends on the rest term, the level and the speed unless the gradients are tuned. |
| 4 | Universality of free fall | conditional | 04 (4.19), (4.20), (4.22), (4.23); 06 (6.17), (6.21); 17 (17.3) | The fall from rest is the same for all levels iff $`\frac{\tau_k^2}{M_k}(\mathcal F_k-G_k)`$ is; for both branches iff the field multiplies the whole rest and clock term and adds no plain gradient. A common clock response and a level-independent fall do not imply each other. |
| 5 | Clock rate and fall | conditional | 04 (4.24); 06 (6.23); 17 (17.7), (17.13) | Where the fall is level-independent and not zero, it equals $`-\frac{v_{\max}^2}{d_0}\frac{r(x+1)-r(x)}{r(x)}`$, with only the maximal speed, the distance and the two rates, at first order in the gradients. |
| 6 | Limits of universality | conditional | 04 (4.25); 07 (7.2), (7.4), (7.15), (7.19), (7.21), (7.22); 15 (15.10), (15.12), (15.13) | Exact only at rest and at first order: the lattice adds a level-dependent $`v^2`$ term, a clock in a superposition of levels falls with the mean, the records act at orders $`\kappa^2`$ and $`\kappa^3`$, a constant under the factor breaks universality, and a curved profile gives the local result only in a limit. |
| 7 | Bodies of different types | conditional | 08 (8.4), (8.8), (8.12), (8.14), (8.29) | Two types fall alike and their clocks respond alike per distance under separate conditions; with a level-independent fall, any two of "fall alike", "respond alike" and "common maximal speed" imply the third; equal falls need $`\langle X\rangle=0`$. |
| 8 | Fields that are not sharp | conditional | 09 (9.1), (9.6), (9.19); 10 (10.13), (10.34); 12 (12.4), (12.13), (12.22) | A static unsharp field acts as a mixture over its sectors; a field with its own contract gives the mean profile with level-dependent corrections; a changing field gives the same fall for all levels at every frequency iff the start has no position–label correlation. |
| 9 | Composite bodies | conditional | 11 (11.16), (11.17), (11.20); 13 (13.11), (13.13), (13.14), (13.34); 14 (14.11); 16 (16.6), (16.11), (16.13) | No: in this description a bound pair does not fall like its parts at any fixed binding, its fall depends on the clock levels, its inertia does not follow its cost, and its binding cost is not weighed like the rest cost; only the ordered wide-pair limit restores the agreement. |
| 10 | Typical or forced | conditional | 17 (17.3), (17.8), (17.10)–(17.12), (17.14) | In a five-parameter class of couplings the universal ones are exceptional (codimension 1 to 4) and are broken at first order by a deviation. They are selected by one requirement stated in the terms of the language, which the language does not enforce. |

The success line of the base problem (items 1–10, extended on 2026-10-11) is met: every item has a verified package. Item 9 is answered in the negative for the description studied, and item 10 is answered for a stated class of couplings of one body.

## 3. Results by criterion

### I. A body in a given field

**Field as an object** (criterion 1; 02-field-object).
- **Sharp stationary field.** The joint state is a product for all $`\lambda`$, both views are pure (2.4)–(2.5), and every schedule has the statistics of the effective generator $`C_{\rm red}`$ (2.3), (2.6). A reduced admissible description of the body and its other partners exists, with all its contracts given by (2.29); without other partners it exists only under the diagonality condition (2.31).
- **Which field states keep the view pure.** Under linear independence exactly the states of (2.11), with the state (2.12); otherwise (2.11) is sufficient.
- **A static field that is not sharp.** It acts as the mixture (2.16) of sector evolutions: readings cannot tell it from a sharp field with numbers drawn with the sector weights (2.17); the view is pure iff (2.19).
- **Well-defined quantities.** The effective generator up to a multiple of $`\mathbb 1`$, and the differences of on-site blocks between positions, are well defined. The values $`n_j`$ of the field, and the split of a block into body, medium and field parts, are not (item 4 of 02).

**Clock rate in a field** (criterion 2; 03-clock-and-fall, 05-rate-comparison, 06-two-clocks).
- **Rate at a place.** In the class $`\mathcal C`$ (factors $`m_x`$, $`\eta_x`$, $`\zeta_x`$ on the rest, clock and hopping terms, plain cost $`V_x`$), a wide start at $`x_0`$ has the rate $`\eta_{x_0}/\lambda_0`$ (3.23). At finite width the rate is $`\frac{\eta_{x_0}}{\lambda_0}(1-\varsigma_W)`$, which depends on $`m`$ and $`\tau`$ at relative order $`\delta_W^2\tau^2/m^2`$ (3.36). The ratio of the rates at two places is $`\eta_{x_1}/\eta_{x_2}`$ in the wide-start approximation (3.24).
- **Comparison.** The ratio of the rates of two runs at equal $`\lambda`$ is the same in every equivalent description, for every start and rule, wherever it is defined; the ratio of the parameters is not (5.17). A comparison of two runs uses the order of $`\lambda`$ (A8). For two types, a common rescaling is detectable iff $`X`$ is not diagonal and both bodies hop ($`J_1,J_2\neq0`$) (5.19), and the transformation rule of the rates is exact (5.21).
- **Common response of all gaps.** In one level a response common to all gaps needs $`G_k=M_kg_{\zeta,k}`$ (6.10); in $`\mathcal C`$, $`g_m=g_\eta=g_\zeta`$ with any plain gradient (6.13). Its exact form is that the local contract at one place is a multiple of that at another, up to a constant (6.15).

**Free fall** (criterion 3; 03-clock-and-fall, 04-branch-fall).
- **A start in one branch.** At first order in the gradients the velocity has the coefficient $`\langle a_{k,\sigma}\rangle_g`$ of $`\lambda`$, with $`a_{k,\sigma}`$ in closed form (4.7). The drift acceleration (long window first, sharp label second) is $`a_{k,\sigma}(p_0)`$ (4.11). From rest it is $`a_{k,\sigma}(0)=\frac{\tau_k^2}{M_k}(\sigma\mathcal F_k-G_k)`$ (4.16), and in motion it has the expansion (4.17) in the drift velocity $`v`$.
- **A start that is not in one branch.** For the bare start of 03 the long-window limit at finite width exists, (3.27). The two limits (wide start, long window) do not commute when the rest term has a gradient (3.28); the secular acceleration is (3.15).

### II. Universality

**Universality of free fall** (criterion 4; 04-branch-fall, 06-two-clocks, 17-typical-or-forced).
- **From rest.** The fall is the same for all levels iff $`\frac{\tau_k^2}{M_k}(\mathcal F_k-G_k)`$ is, and on both branches with one value iff $`\mathcal F_k=0`$ and $`\frac{\tau_k^2G_k}{M_k}`$ is level-independent (4.19). In $`\mathcal C`$ this is $`\mathcal F=0`$, $`g_m=g_\eta`$: the field multiplies the whole rest and clock term, with the value $`-\tau^2g_\eta`$ (4.22).
- **In motion.** Through the order $`v^2`$, exactly, a level-independent fall exists in $`\mathcal C`$ only with zero fall for $`N\ge3`$ (4.23). At leading order in $`M_k/\tau`$ the condition is the same as from rest, and the level enters only through the lattice term $`2gM_k^2v^2/\tau^2`$ (4.20), (4.23).
- **Clocks and fall.** A common response of the clock to the place and a level-independent fall do not imply each other (6.17). For both branches with one value, the two sets of members coincide under the conditions of (6.21).
- **The wider class $`\mathcal C^+`$** (a level-dependent plain gradient added): the conditions and their codimensions are (17.3).

**Clock rate and fall** (criterion 5; 04-branch-fall, 06-two-clocks, 17-typical-or-forced).
- In $`\mathcal C`$, if the fall from rest is level-independent with the value $`a\neq0`$, then $`\frac{\mathrm d^2\bar x}{\mathrm d\lambda^2}\big\vert_{\rm drift}=-\frac{v_{\max}^2}{d_0}\frac{r(x+1)-r(x)}{r(x)}\,\hat e`$ (4.24), for both branches. It contains neither $`m`$, $`N`$, $`\lambda_0`$, the level, nor the plain gradient, and $`\tau`$ only inside $`v_{\max}/d_0`$. A place-dependent rate does not imply a level-independent fall; the converse holds exactly when the common value is not zero.
- With other gaps of the body in place of the clock gap the relation holds under the conditions (6.24)–(6.25), (6.23).
- In $`\mathcal C^+`$, (4.24) holds on one level iff on all levels; its defect on level $`k`$ is (17.7), and the conversion from labels to the mean position carries over (17.13).

**Limits of universality** (criterion 6; 04-branch-fall, 07-limits, 15-curved-profile-fall).
- **Variants.** Table (4.25): the factor on the whole rest and clock term (with or without the hopping) gives a level-independent fall from rest on both branches; a factor on the rest term alone or on the clock term alone, a plain gradient, or a constant under the factor does not.
- **A clock in a superposition of levels.** It falls with the weighted mean of the level accelerations (7.2). The spread of the position grows as $`\frac14\lambda^4`$ times the variance of these accelerations, and vanishes in the universal variants (7.4).
- **The records.** Their effect enters at order $`\kappa^2`$ in motion and at order $`\kappa^3`$ at rest for a skewed record distribution (7.15), (7.16). It is level-independent only if $`\tau_k/M_k`$ (respectively $`\nu_k(4+3t_k)`$) is, which never holds in $`\mathcal C`$.
- **The zero of the cost.** With the on-site block $`(1+gx)[M_k\sigma_3+u_k\mathbb 1_2]`$ the fall from rest is (7.19). The constants $`u_k`$ are not well defined, while $`\mathcal F_U-gu_k`$ is (7.21). Which operator the field multiplies matters beyond its traceless part.
- **Orders.** Table (7.22).
- **Curved profiles.** With quadratic level profiles the curvature adds $`c_g+\lambda\langle b\omega'\rangle_g`$ to the non-oscillating acceleration, which grows linearly in $`\lambda`$ for a skewed start (15.9), (15.10). The local-slope value (4.16) is recovered exactly only in the limit (15.12): window before sharp label, even weight, $`\delta p^2W\to0`$. In the factor class the fall is level-independent only in that limit, because the hopping is not multiplied (15.13).

**Bodies of different types** (criterion 7; 08-two-types).
- Two types fall alike under (8.4)–(8.5), and their clocks respond alike per distance (RD) under (8.7). Neither implies the other. With level-independent falls and nonzero responses, any two of "fall alike", RD and "common maximal speed" imply the third (8.8).
- **In a common field.** The conditions are conditions on six numbers, and equal falls need $`\langle X\rangle=0`$ (8.12). The common couplings are $`\Theta_1=\Theta_2`$ for the fall and $`\theta_1/d_{0,1}=\theta_2/d_{0,2}`$ for the clocks (8.14).
- **Equivalent descriptions.** Whether a statement holds in every equivalent description depends on whether the medium is read and on whether $`X`$ is diagonal (8.29).

### III. Beyond a sharp field and a single body

**Fields that are not sharp** (criterion 8; 02-field-object, 09-unsharp-field, 10-field-own-contract, 12-changing-field).
- **Static field, not sharp.** It acts as the exact mixture over its sectors (9.1). The mean fall is (4.16) at the mean gradients (9.6), with a spread. In the lapse classes the fall is level-independent iff $`\langle X\rangle=0`$, and (4.24) holds for the means only under an additional covariance condition (9.19).
- **Field with its own contract and a gap.** At leading order the body sees the mean profile as a member of $`\mathcal C_{\rm lev}`$. At the next order a level-dependent on-site term appears (10.13). The mean clock rate can be zero or negative (10.33). For the members with a defined comparison ($`D_0\neq0`$) and $`N\ge3`$, (4.24) holds for all levels iff $`\gamma_1=0`$, $`g\gamma_0=0`$ and $`\langle X\rangle=0`$ (10.34).
- **Changing field.** At first order the body sees the generator $`C_{br}+\gamma(\lambda)B`$ (12.4). The response at the field frequency is the same for all levels iff the start has no position–label correlation, $`\chi=0`$ (12.13), with a resonance at $`\Omega=2M_k`$. The complete acceleration is level-independent iff $`\chi_k=0`$ on every level (12.22).

**Composite bodies** (criterion 9; 11-bound-pair, 13-pair-fall, 14-pair-level-next-order, 16-pair-fall-next-order). Two Model D bodies with a diagonal on-site binding, in the regime of slow parts with a binding of the order of their motion (small $`\epsilon`$, fixed $`u`$), at first order in the gradients. The field multiplies the rest and clock terms of the parts, not the binding: a binding with a field factor needs a term on three objects (13-pair-fall, Step 1.4).
- **The bound level.** Its curvature inertia is $`\mathfrak m_b=\mathfrak m_1+\mathfrak m_2-4\mathfrak m_1\mathfrak m_2E_{\rm bind}`$ at leading order (11.16). It is not the cost of the pair divided by $`\tau^2`$ (11.17). The clocks of the parts are slowed by factors that differ unless $`\tau_1/M_1=\tau_2/M_2`$ (11.20).
- **Fall of the pair.** Exactly, $`a_{\rm pair}=-\langle\mathcal K\rangle_0/\mathfrak m_b`$, with weight $`\langle\mathcal K\rangle_0`$ from the rest terms only (13.11). At leading order this is $`-\mathrm{sgn}(w_{11})(1+u^2)^{-1/2}`$ times the inertia-weighted mean $`\bar a`$ of the free falls (13.13).
- **Comparison with the parts at leading order.** The pair falls like its parts at no fixed binding. Agreement holds only in the ordered wide-pair limit for an attractive binding (13.14), (13.34). Its fall depends on the clock levels (13.16).
- **Next order.** With the exact binding cost, $`\mathfrak m_b=\mathfrak m_1+\mathfrak m_2-4\mathfrak m_1\mathfrak m_2E_{\rm bind}`$ fails at relative order $`\epsilon^2`$ (14.11). The weight per unit gradient counts the rest costs with factor 1 and the binding cost with factor $`-\mathrm{sgn}(w_{11})/\sqrt{1+u^2}`$, not 1 (16.6). Through relative order $`\epsilon^2`$ the pair against its parts is (16.11), with the wide-pair coefficient (16.13).

### IV. How special the structure is

**Typical or forced** (criterion 10; 17-typical-or-forced). The class $`\mathcal C^+`$: one Model D body, a sharp field with a linear profile, couplings $`\sigma_3\otimes(\alpha_0+\alpha_1D)+\mathbb 1_2\otimes(\beta_0+\beta_1D)`$ and an optional factor on the hopping; five gradients. First order in the gradients.
- **Exceptional.** The sets of couplings that give items 4 and 5 have empty interior and codimension 1 to 4 (17.3), (17.5), (17.7), (17.12).
- **Not robust.** A deviation at distance $`\delta`$ from the upper-branch set breaks the level independence and (4.24) at first order in $`\delta`$ (17.8).
- **Requirements.** "The field multiplies the body's own rest and clock term as listed" (R1), and its traceless form (R2, with or without a common factor), are not well defined: a relisting of single-object terms that leaves the total contract unchanged changes their verdict (17.10), (17.14). A requirement stated on the effective blocks is well defined and equivalent to universality from rest on both branches (17.11). It says that the change of each level's on-site block from one place to the next is that level's half-gap times one level-independent operator.
- **Not forced.** Every coupling of $`\mathcal C^+`$ is an admissible description, so the language does not enforce that requirement (17.12).

## 4. Cross-cutting findings (interpretation)

1. **Universality of free fall is a structure, not a consequence of the laws.** A body falls the same way on all its clock levels when the field scales each level's internal block in proportion to its gap (17.11); in $`\mathcal C`$, when it multiplies the whole rest and clock term (4.22). Ilanguage 1.b allows this, but does not enforce it, and among the couplings of $`\mathcal C^+`$ it is exceptional (17.12). This is the answer of this stage to the second question of the programme, for one body. It is an interpretation of the cited results, not an additional result.
2. **Where it holds, the fall is tied to the clock rates.** The relation (4.24) has the form of a relation between an acceleration and the relative gradient of clock rates, with the square of the maximal speed of 03-ilang-space as the factor. No theory of gravity was used as an input (M4), and no identification with one is derived: the relation holds at first order in the gradients, on a chain, for the stated class.
3. **"Which operator the field multiplies" is not fixed by a listing.** A constant under the factor changes the fall (4.25), (7.21), and the natural requirement on the listed term is not well defined (17.10). What is well defined is stated on effective blocks and their differences. This continues the finding of 04-ilang-time that only differences of costs are physical.
4. **Composite bodies break universality in this description.** The bound pair's inertia is not its cost over $`\tau^2`$ (11.17), (14.11), and its binding cost is not weighed like its rest cost (16.6). Only the ordered wide-pair limit restores the agreement with the parts (13.14), (16.12). In this description the equality of fall of composite and simple bodies is therefore a property of a limit, not of the language.
5. **Results hold in ordered limits.** The fall is defined by a long window followed by a sharp label (4.11). At finite width, curvature (15.13), superpositions (7.4), records (7.15) and unsharp or changing fields (9.6), (12.13) all add level dependence. Universality is exact only in these limits and at first order in the gradients.

## 5. What is missing, and open problems

- **The source of the field.** How a body makes the field it falls in, the sign of a mediated interaction and the profile are not treated. They are the next stage.
- **Beyond $`\mathcal C^+`$.** Item 10 is answered for one body and one class of couplings. Couplings that mix branches or levels, fields that are not sharp, two types and composite bodies are not included in the classification, and whether a requirement outside $`\mathcal C^+`$ selects the universal set is open (17).
- **Orders and limits.** Second order in the gradients, long falls, joint limits in $`\epsilon`$ and $`u`$ for the pair (13, 14, 16), the finite-width rate in $`\mathcal C^+`$ (17.6), and stability of the through-$`v^2`$ sets (17) are not derived.
- **Composite bodies.** Only a direct on-site binding of two bodies is treated. Bindings through a medium that is also the field, more than two parts, and the clock of a moving pair are open.
- **Model dependence and dimension.** Model D on a chain is the body studied throughout; other bodies and two or three dimensions are not treated.
- **Formalization.** Readings whose classes are not local to one part (A4) are admitted by the base problem; which readings are primitive should be settled before interacting bodies are read jointly.

## 6. Quality record

**External verification** (an independent external referee model saw only the referee prompt, the base problem, the question without "Expected result", the derivation and its code):
- one round, minor issues, fixed by a regeneration: 04, 06, 09, 15, 16;
- major issues in the first round, minor issues or none in the second, fixed: 02 (second round correct), 03, 05, 08, 11, 12, 14 (second round correct), 17;
- major issues in two rounds: 07 (v4 answered the second round, and v5 fixed an error that the main model's review of v4 found); 10 and 13 (third round minor issues, fixed).

**Not externally re-checked.** The current versions of 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 15, 16 and 17 answer their last external round, and only the main model reviewed those answers. For 07 v5, 10 v6 and 13 v6 these answers included substantive changes. For the others they were corrections of conditions, ranges and wording in versions whose formulas the referee had confirmed.

**Revised questions.**
- 10: item 4(c) was restricted to cells with linear level profiles (2026-10-11).
- 13: item 2(c) was restricted to the members the programme needs (2026-10-11; confirmed by the user on 2026-10-18).
- 16: the notation of 11-bound-pair was added to the question after its first external round, which found it missing (2026-10-18). Its item 4 was restricted from the start to the data on which the leading coefficient does not vanish.

**Known minor issues, not fixed.** None recorded.
