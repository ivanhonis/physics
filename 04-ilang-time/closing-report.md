# Closing report: 04-ilang-time

- **Subproject:** 04-ilang-time. Time inside Ilanguage 1.b, for bodies in the space of 03-ilang-space.
- **Date:** 2026-10-10.
- **State:** all 9 derivation packages (02–10) are verified, and every one has had at least one external verification round. The current versions of 05, 06 and 08 are regenerations that answer their last external round; only the main model reviewed them (section 6). The dependency graph passes `graphcheck`.
- **Scope of this report:** it summarizes the verified results against the success criteria of `01-base-problem/problem.md`, citing packages and tags. It adds no results. Interpretations are marked as such.
- **Status labels:**
  - **proven**: derived at the physicist-formal standard (every step justified, standard facts used without proof), reviewed by the main model and checked by an external AI referee. It is not a formal proof.
  - **conditional**: proven under stated assumptions, or for a stated class of models;
  - **candidate**: numerical evidence only;
  - **open**: not settled.
- **Workflow:** the derivations, reviews and external checks are made by AI models in a human–AI research workflow.
- **Tags:** (2.k)–(9.k) are tags of this subproject. Results of 03-ilang-space are cited with their package name.

## 1. Question and approach

The question: can a physical time be derived inside Ilanguage 1.b from the language's own elements, without importing any temporal notion (M1–M6), for bodies in the space of 03-ilang-space? Which time-related structures that a later study of gravity needs follow, and under which conditions?

**Approach.**
- The ordering parameter $`\lambda`$ of the evolution (1.9) is not treated as a time (M1). A *clock* is a part of the system whose reading statistics change with $`\lambda`$ under its contracts.
- *Time* is a relation between the readings of a clock and the rest of the system.
- A clock is then put on a body that moves in the space of 03-ilang-space. The body studied is **Model D**: places $`(x,s,a)`$ (position, branch, clock label) and the contract $`C_b=A+B`$ with a hopping term $`A\propto\sigma_1`$ and a rest and clock term $`B=\sigma_3\otimes(m\mathbb 1+D)`$, which anticommute (5.4). Bodies whose clock term commutes with the motion are treated for comparison.
- *Events* are readings at stated values of $`\lambda`$ (A8). What readings can detect of $`\lambda`$ itself is studied through re-timings: changes of the values of $`\lambda`$, together with a change of the contract, that leave all reading statistics unchanged.

## 2. Answers at a glance

| # | Criterion | Status | Main packages and tags | Answer in one line |
|---|---|---|---|---|
| 1 | Clock | proven | 02 (2.2), (2.6), (2.8), (2.9), (2.12)–(2.14), (2.18), (2.20)–(2.21) | A clock is a self-driven part with a reading that ticks; uniform ring clocks are classified; a reading resets the clock, frequent reading stops it, and the cost spread limits the resolution. |
| 2 | Time and $`\lambda`$ | conditional | 03 (3.2), (3.6), (3.9)–(3.12), (3.14), (3.16)–(3.19) | In a state without $`\lambda`$-dependence the rest evolves by its own contract, indexed by the clock reading; rates per $`\lambda`$ are rates per clock time, within the clock's bandwidth and for suitable clock–rest contracts. |
| 3 | Comparison of clocks | proven | 04 (4.3), (4.5), (4.9), (4.12), (4.14)–(4.16), (4.18) | Free clocks are compared by the ratio of their ticks; one joint reading synchronizes them up to the recorded offset; in an environment a clock stays uniform iff it is coupled through its own contract, and two clocks keep their rate ratio iff the coupling strengths are equal. |
| 4 | Proper time and moving clocks | conditional | 05 (5.2), (5.21)–(5.22), (5.25), (5.28)–(5.29), (5.33), (5.35); 09 (9.1), (9.11)–(9.16), (9.18)–(9.21) | For Model D a carried clock slows down with the body's drift speed, $`R=1+V^2/(2v_{\max}^2)`$ at small speed; its time along a path is the integral of $`\sqrt{1-V^2/v_{\max}^2}`$ up to lattice corrections; between two meetings the resting clock shows more. A clock that commutes with the motion is not affected. |
| 5 | Inertia and internal energy | conditional | 06 (6.4), (6.10), (6.13)–(6.17), (6.20), (6.22)–(6.23), (6.26); 08 (8.19), (8.24)–(8.25) | For Model D the averaged inertia is half the gap between the branches divided by $`v_{\max}^2`$, and the clock's cost adds to it like the rest term; the inverse inertia of 03-ilang-space vanishes for the same body at rest. For a clock that commutes with the motion the inertia does not depend on the clock. |
| 6 | Common maximal speed | proven | 08 (8.1), (8.3), (8.5)–(8.10), (8.13), (8.15), (8.17)–(8.18), (8.26) | No: the maximal speed belongs to a type, and the laws do not make it equal for two types. Equality is a condition on the description; it is equivalent to a common leading-order slowdown law and a common relation between inertia and rest gap. |
| 7 | Events and causal order | proven | 07 (7.1)–(7.2), (7.5), (7.12)–(7.14), (7.17), (7.19)–(7.21), (7.24)–(7.25) | Readings are events; an earlier reading can influence a later one, never one at equal or smaller $`\lambda`$. The influence at distance $`r`$ starts at order $`\delta^r`$ and obeys a bound with a finite speed, but there is no sharp cone: the order is only approximate. |
| 8 | Global order | conditional | 10 (10.2), (10.4), (10.7)–(10.8), (10.14), (10.16)–(10.20), (10.22) | The unit of $`\lambda`$ is never detectable; its direction is, wherever one reading can influence another. A common now of two parts is not detectable when they are uncoupled; for coupled parts it is detectable exactly when the contract has no split into commuting pieces that each leave the places of one part unchanged. On a chain the order of two events leaves a trace iff one can influence the other. |

The success line of the base problem (items 1–7) is met, and item 8 is answered as well. Items 2, 4 and 5 are answered with conditions that the derivations state; item 6 is answered in the negative, with the exact conditions; item 8 is answered for a defined notion of detectability (linear re-timings of two parts).

## 3. Results by criterion

### I. Clocks and time without $`\lambda`$

**Clock** (criterion 1; 02-clock).
- **Self-driven part.** The view of a part $`K`$ evolves under its own contract alone iff $`\mathrm{Tr}_R[C_\partial,X]=0`$ for all $`X`$ on the admissible space (2.2); when no two objects share a type this is $`C_\partial=\mathbb 1_K\otimes B`$ (2.1). Its statistics then depend on the rest only through its starting view (2.4).
- **Ticking.** Some reading statistic of $`K`$ depends on $`\lambda`$ iff some active gap of its contract has a nonzero place-diagonal component (2.6). A contract that is diagonal in the places never ticks.
- **Indexing.** The view distinguishes all values of $`\lambda`$ iff two active gaps have an irrational ratio; otherwise it distinguishes them only inside half-open intervals of one period (2.7)–(2.8).
- **Uniform ring clocks.** All contracts that move the place of an $`N`$-place clock by one step per tick $`\lambda_0`$ are (2.9). Equally spaced levels give the smallest cost spread (2.12); the place distribution of such a minimal clock is (2.13), a point mass exactly at the multiples of $`\lambda_0`$.
- **Reading (Law 1).** A place reading resets the view of the clock to the place read (2.14). An earlier reading, even unrecorded, changes the distribution of a later one except under the condition (2.23)–(2.24). Under $`n`$ equally spaced readings in a fixed interval the clock stays at its place with probability tending to 1 (2.18): a clock that is read often does not run.
- **Resolution.** The view moves at the angular rate $`\Delta C_K`$ (2.19); two views can be orthogonal only if $`\lvert\lambda'-\lambda\rvert\ge\pi/(2\Delta C_K)`$ (2.20). For the minimal ring clock the first orthogonal view is one tick later, and the ratio to the bound is $`\frac{2}{\sqrt3}\sqrt{1-N^{-2}}`$, attained only for $`N=2`$ (2.21).

**Time and $`\lambda`$** (criterion 2; 03-relational-time).
- **States without $`\lambda`$.** All reading statistics are independent of $`\lambda`$ iff the place-diagonal of every Bohr component of the state vanishes (3.2). Eigenvectors of the total contract are of this kind, but not the only ones (3.3).
- **Relational evolution.** Let the clock be a minimal ring clock without a contract to the rest $`R`$, and the state an eigenvector with eigenvalue $`E`$. The components of the state along the clock places obey $`\Phi(m+1)=e^{-i(C_R-E)\lambda_0}\Phi(m)`$ (3.6): from one clock reading to the next, the rest evolves by its own contract for one tick. The statistics of $`R`$ conditional on the reading $`m`$ are those of $`R`$ alone at $`\lambda=m\lambda_0`$ (3.12).
- **Bandwidth.** Such an eigenvector through a given state $`\chi`$ of the rest exists iff the levels of $`C_R`$ present in $`\chi`$ fit into a window of $`N`$ levels with spacing $`2\pi/(N\lambda_0)`$ (3.9); it is then unique, and the clock places are equally likely (3.10)–(3.11). A finite clock times only a system of finite bandwidth.
- **Clock time.** With $`\tau_m=m\lambda_0`$ modulo $`N\lambda_0`$ (3.17), rates with respect to $`\lambda`$, such as those of 03-ilang-space, are rates with respect to $`\tau`$ with factor one, up to an error bounded by $`\lambda_0w_\chi^2/2`$ (3.18). The time is cyclic and has the resolution of one tick.
- **Contracts between clock and rest.** The relation does not hold for every such contract (counterexample (3.16)); a sufficient condition is (3.14), realized by (3.15). The split of the contract into clock, rest and crossing part is fixed without conventions by (3.19).
- **Readings.** The outcome of the clock reading can change the statistics of the rest; it does so iff the joint place distribution is not a product (3.4)–(3.5).

**Comparison of clocks** (criterion 3; 04-clock-comparison).
- **Rates.** Two free minimal clocks have independent readings (4.3). The ratio of their rates is $`\rho=\lambda_{01}/\lambda_{02}`$. Both readings are certain at common values of $`\lambda`$ iff $`\rho`$ is rational (4.4)–(4.6); otherwise the second clock, read at the ticks of the first, is distributed around the nearest place (4.7)–(4.8).
- **Agreement.** Two identical clocks show the same place with the probability (4.9), which is 1 exactly at the multiples of the tick and never below $`(N^2+2)/(3N^2)`$ (4.10).
- **Synchronization.** After one joint reading, two identical clocks keep the recorded offset with the same probability function; it equals 1 exactly at the later multiples of the tick (4.11)–(4.12).
- **A clock in an environment.** With a contract $`A\otimes B`$ between clock and environment, in an eigenvector of $`B`$ with eigenvalue $`b`$ the clock evolves under $`C_K+bA`$ (4.13); it is self-driven iff $`B=0`$ or $`A\propto\mathbb 1`$ (4.14).
- **Lapse form.** The clock remains a minimal ring clock for every such $`b`$ iff $`A=\gamma C_K`$, a multiple of its own contract; its tick is then $`\lambda_0/(1+\gamma b)`$ (4.15)–(4.16).
- **Common coupling.** In a common environment the rate ratio of two such clocks is $`\rho(1+\gamma_2b)/(1+\gamma_1b)`$; it does not depend on the environment iff $`\gamma_1=\gamma_2`$ (4.17)–(4.18).

### II. Clocks in motion, inertia, maximal speed

The results of this part for Model D hold in the *weak-record regime* (leading order in the record strength $`\kappa`$ at fixed $`\lambda`$; positions are measured in the background of 03-ilang-space), for starts concentrated near one plane-wave label $`p_0`$ in the branch of positive eigenvalue, and to first order in $`\epsilon=2\pi/(N\lambda_0m)`$, the level spacing of the clock relative to the rest term, on the scale of a tick. Remainders are stated in the packages.

**Moving clocks** (criterion 4, first part; 05-moving-clock).
- **A clock that commutes with the motion.** If the body contract is a sum of a position part and a clock part, the clock statistics do not depend on the motion, on the start of the position, or on the records, exactly (5.2).
- **Model D.** $`AB+BA=0`$ (5.4); for each clock level $`d_k`$ the eigenvalues are $`\pm\sqrt{(m+d_k)^2+\tau^2\sin^2p}`$ (5.6). The velocity of a start in one level is (5.9), its largest value (5.10); the bound (17.7) of 03-ilang-space/17-motion is $`v_{\max}=\tau\kappa\sigma_X`$, strictly larger (5.11).
- **The carried clock.** Its reading distribution is that of the clock at rest with $`\lambda`$ replaced by $`\Gamma(p_0)\lambda`$, where $`\Gamma=\bar\mu/\sqrt{\bar\mu^2+\tau^2\sin^2p_0}\le1`$ and $`\bar\mu=m+\langle0\vert D\vert0\rangle`$ is the rest term plus the mean clock cost (5.20)–(5.21). The tick is $`\lambda_0/\Gamma`$ (5.22). Beyond first order the reading at the tick is not exactly certain (5.23).
- **Rate and velocity.** For the *drift velocity* $`\bar v`$ of the clock-carrying start (its mean velocity over a tick or longer, (5.25)), the tick ratio $`R=1/\Gamma`$ obeys $`R=1+\lVert\bar v\rVert^2/(2v_{\max}^2)+O(p_0^4)`$ (5.28) and $`R^2(1-\lVert\bar v\rVert^2/v_{\max}^2)=1+(\tau/\bar\mu)^2\sin^4p_0`$ (5.29); the exact relation on the chain is two-valued (5.26)–(5.27). The bound $`v_{\max}`$ is never reached.
- **Which velocity.** The coefficient $`\frac12`$ in units of $`v_{\max}`$ holds to first order in $`\epsilon`$ for the drift velocity only. Expressed through the velocity of a start in one clock level it is $`\frac12\mu_k^2/\bar\mu^2`$ (5.33), and through the instantaneous velocity of the clock-carrying start it oscillates with $`\lambda`$ (5.30), (5.35). At zeroth order in $`\epsilon`$ all three agree.

**Proper time and two clocks** (criterion 4, second part; 09-proper-time).
- **A uniform gradient.** Under a uniform cost gradient $`-\mathcal Fx`$ on the body, the plane-wave label moves as $`p_0+\mathcal F\lambda`$ exactly (9.1); the start stays in its branch if $`\mathcal F\tau\ll4m^2`$ (9.4), (9.25). The displacement is (9.7).
- **Clock advance.** The reading distribution keeps its form with the advance $`\vartheta(\lambda)=\frac1{\lambda_0}\int_0^\lambda\Gamma(p_0+\mathcal F\lambda')\,\mathrm d\lambda'`$ (9.11)–(9.12). To this order the gradient enters the rate only through the label at $`\lambda`$ (9.13).
- **Rate along the path.** With the velocity $`V`$ computed from the displacement, $`\lambda_0\,\mathrm d\vartheta/\mathrm d\lambda=\sqrt{1-\lVert V\rVert^2/v_{\max}^2}\,(1+\rho)`$ with $`-\tau^2\sin^4p/(2\bar\mu^2)\le\rho\le0`$ (9.14)–(9.15); for small labels the advance is the integral of $`\sqrt{1-\lVert V\rVert^2/v_{\max}^2}`$ along the path (9.16). The rate is a function of the speed only on each of two branches of the relation (9.24).
- **Two clocks between two meetings.** For two bodies of different types with equal parameters, one under the gradient and one at rest, the joint readings are independent (9.17). They meet again at the values (9.18). The ratio of the advances at the first meeting is $`\frac1{\lvert p_0\rvert}\int_0^{\lvert p_0\rvert}\Gamma`$, independent of the gradient (9.19). The clock of the resting body has advanced more at every $`\lambda>0`$, hence at every meeting (9.20); for small $`p_0`$ the ratio is $`1-\frac12\langle\lVert V\rVert^2/v_{\max}^2\rangle`$ (9.21). Both readings are certain iff both advances are integers (9.22).

**Inertia and internal energy** (criterion 5; 06-inertia-internal-energy, 08-maximal-speed).
- **The inverse inertia of 03-ilang-space with internal labels.** The response at $`\lambda=0`$ to a uniform cost gradient, (20.10) of 03-ilang-space/20-cost-and-mass, involves only the edges between different points (6.3). For a body whose hopping does not act on the internal labels it depends neither on the internal state nor on the on-site terms (6.4).
- **Model D at $`\lambda=0`$.** For a start in the branch label $`s=1`$ and one clock level this inverse inertia vanishes, for every position state (6.10).
- **Averaged response.** For a start at rest (label $`0`$) in the positive branch with clock level $`k`$, the acceleration builds up as $`\sin^2(M_k\lambda)`$ (6.13), with $`M_k=m+d_k`$. Its average over intervals that are long compared with the inverse gap, and short enough for the first-order treatment, is $`\mu_{\rm av}(k)F`$ with $`\mu_{\rm av}(k)=\frac{\tau^2}{M_k}\kappa^2\,e\,g(e,\cdot)`$ (6.14)–(6.15), with the exact bound (6.26) on the error. In background units the inertia is $`I_k=M_k/(\tau^2\kappa^2\sigma_X^2)=M_k/v_{\max}^2`$ (6.20), (8.16): it is proportional to $`M_k`$, and the clock cost $`d_k`$ adds to it with the same coefficient as $`m`$ (6.16).
- **Convention-independent form.** The rest cost of one type is defined only up to a constant of the description; the gap between the branches $`\Delta_k`$ and cost differences are well defined (8.24). In every description $`\Delta_k=2I_kv_{\max}^2`$ and $`E_k-E_{k'}=(I_k-I_{k'})v_{\max}^2`$ (8.25).
- **Bodies with scalar hopping.** If the on-site terms are the same at every position, the averaged and the instantaneous inverse inertia coincide and do not depend on the clock (6.17). With position-dependent on-site terms there is no general relation; Model D is the direct sum of two such bodies with a staggered on-site term (6.22). The dividing line is whether the term that carries the clock commutes with the velocity (6.23).

**Common maximal speed** (criterion 6; 08-maximal-speed).
- **Comparing two types.** For two bodies of different types recorded by one medium, the velocities, their norms and inner products and the ratio of the maximal speeds are well defined; the difference of the positions is not (8.1)–(8.3). The bound $`\lVert v_a\rVert\le v^A_{\max}`$ holds for each body in the presence of the other, and $`v^A_{\max}`$ depends only on the body's own hopping, its own records and the start of the medium (8.5)–(8.6).
- **Values.** $`v_{\max}=2t\sigma_X`$ for a chain type and $`\tau\kappa\sigma_X`$ for a Model D type (8.7); they are equal for two types iff these products are equal (8.8).
- **Not forced.** Laws 1–5 and A1–A9 do not imply equal maximal speeds; every ratio occurs in admissible descriptions (8.9).
- **Common points.** If the points of the two types coincide (a full correspondence of 03-ilang-space/16-common-space), the distances of neighbouring points agree and the condition reduces to equal hopping (8.10).
- **What a common maximal speed means.** For two Model D types, the tick ratio is the same function of the drift speed to leading order iff $`v^A_{\max}=v^B_{\max}`$ (8.12)–(8.13); beyond that order the relations (5.29) agree only if also $`\bar\mu/\tau`$ agrees (8.15). The relation between inertia and branch gap is the same iff $`v^A_{\max}=v^B_{\max}`$ (8.17), (8.26). All these conditions are one condition (8.18).

### III. Events and order

**Events and causal order** (criterion 7; 07-causal-order). Setting: a chain of $`n`$ cells of different types with single-cell terms and pair terms $`J_i`$ between neighbours; an event is a reading on one cell at a stated $`\lambda`$; the influence $`\delta P`$ of a reading on a later one is the change of the outcome-averaged statistics (7.1).
- **No influence without delay.** A reading does not influence a reading at an equal or smaller $`\lambda`$ (7.2).
- **Order of the influence.** At distance $`r`$ along the chain the influence starts at order $`\delta^r`$ in the delay, with a coefficient given by the nested commutator of the pair terms between the two cells (7.3)–(7.5); it is attained in explicit examples (7.6)–(7.8).
- **Bound.** $`\delta P\le2\sum_{k\ge r}(2\lVert J\rVert\delta)^k/k!`$ for every start and every pair of readings, independent of the single-cell terms (7.12).
- **No sharp cone.** $`\delta P`$ is analytic in the delay: if it vanishes on an interval it vanishes for all delays (7.13)–(7.14). The region in which the bound is below a given $`\epsilon`$ has a boundary that moves at $`2e\lVert J\rVert`$ cells per unit $`\lambda`$ (7.15)–(7.17). This is the speed of the bound, not a derived propagation speed.
- **The order of events.** With $`e_1\prec e_2`$ if some reading at $`e_1`$ influences some reading at $`e_2`$ for some start (7.18): $`e_1\prec e_2`$ implies $`\lambda_1<\lambda_2`$ (7.19). For a prescribed delay the converse holds for almost all pair terms (7.20). For one fixed chain and all delays it holds for almost every chain when $`n=2`$ (7.25); for $`n\ge3`$ exceptional delays of a generic chain between different cells can only be blind delays (7.24), and two statements remain undecided (section 5). $`\prec`$ is not transitive in general (7.21).

**Global order** (criterion 8; 10-global-order). Setting: two parts of the system; a schedule of events (part, reading, $`\lambda`$) with readings applied in the order of $`\lambda`$; a *re-timing* multiplies the $`\lambda`$ of the events on part $`i`$ by $`a_i>0`$ and replaces the contract by another one; it is an *equivalence* if all joint statistics agree for every start and every schedule. A feature is *detectable* if no equivalence changes it.
- **Unit.** $`(a,a,C/a)`$ is an equivalence for every contract: the unit of $`\lambda`$ is never detectable (10.2). For a start that is an eigenvector of the contract, a common shift of all events changes nothing, and a single reading does not depend on its $`\lambda`$ (10.3).
- **Direction.** Of two readings, the marginal statistics of the one at the smaller $`\lambda`$ never depend on the other; those of the one at the larger $`\lambda`$ do whenever there is an influence (10.4). The direction of increasing $`\lambda`$ is therefore detectable wherever an influence exists. It is fixed by the reading rule (1.3) (Law 1: a reading is a write) as applied in A8, not by the evolution (1.9).
- **Uncoupled parts.** $`(a_1,a_2,C_1/a_1+C_2/a_2)`$ is an equivalence for all $`a_1,a_2`$ and every start, entangled or not (10.7): the common now is not detectable. Two events on different parts can be given equal values of $`\lambda`$, or the opposite order, by an equivalence, unless the earlier one is at $`\lambda=0`$ (10.8).
- **Coupled parts.** A re-timing is an equivalence iff $`C-a_iC'`$ commutes with the place projectors of part $`i`$, for both parts, and $`[C,C']=0`$ (10.14). An equivalence with $`a_1\neq a_2`$ exists iff the contract is a sum of two commuting pieces, each of which leaves the places of one of the parts unchanged, both sums of pair terms (10.5), (10.14); the common now is detectable iff no such split exists. It is detectable in particular if the contract changes the places of both parts in one step, or if its place-changing terms of the two parts do not commute (10.16).
- **Examples** (two cells with two places). The common now is detectable for $`g\,\sigma^x\otimes\sigma^x`$ (10.17) and for a hopping body whose place is recorded by a medium (10.19). It is not detectable for $`g\,\sigma^z\otimes\sigma^z+h\,\sigma^x\otimes\mathbb 1`$, although the parts are coupled: the places of the second part are conserved (10.18).
- **The order of two events on a chain.** Compare the joint statistics of two readings with the statistics in which the two readings, carried to one value of $`\lambda`$, are applied in the opposite order. The two agree for every start iff the earlier reading cannot influence the later one (10.20). Their difference is bounded by $`\Theta\sum_{k\ge r}(2\lVert J\rVert\delta)^k/k!`$ at distance $`r`$ and delay $`\delta`$ (10.22): at equal $`\lambda`$ the order leaves no trace, and at a small delay over a large distance only an exponentially small one (10.23)–(10.24).

## 4. Cross-cutting findings (interpretation)

1. **Time is relational, and $`\lambda`$ is detectable only as far as the parts are coupled.** The unit of $`\lambda`$ is a convention (10.2), and between uncoupled parts so is a common now (10.7). What is defined is the relation between the readings of a clock and the rest (3.6), (3.12), and between two clocks (4.5), (9.19). The order of $`\lambda`$ shows in the statistics only where one reading can influence another (10.4), (10.20). This is an interpretation of the cited results, not an additional result.
2. **For Model D bodies the kinematics has the form known from special relativity, with the maximal speed of 03-ilang-space in the place of the speed of light.** Moving clocks slow down (5.28), the clock time along a path is the integral of $`\sqrt{1-V^2/v_{\max}^2}`$ (9.15)–(9.16), the resting clock shows more between two meetings (9.20), and the inertia is the half-gap divided by $`v_{\max}^2`$ (6.20), (8.25). No relativistic theory was used as an input (M4), and no identification with it is derived: the relations hold for one model on a chain, to the stated orders, and have lattice corrections ((5.29), (8.14), (9.15)).
3. **The language allows this kinematics; it does not force it.** Three things are conditions on the description, not consequences of the laws: the structure of the body (a clock term that commutes with the motion gives none of these effects, (5.2), (6.17)), a common coupling of clocks to an environment (4.18), and a common maximal speed (8.9). As in 03-ilang-space, Ilanguage 1.b provides the mechanism, not the values.
4. **Only differences of costs are physical.** The relation between inertia and internal cost is well defined for the gap and for differences between levels (8.25), not for the rest cost itself (8.24). This agrees with the absence of a canonical zero of the cost in 03-ilang-space ((20.3), (21.17) there).
5. **The inverse inertia of 03-ilang-space is an instantaneous response.** For branch-type bodies it misses the inertia (6.10) against (6.15). Results of 03-ilang-space that rest on it, such as the effect of binding on the inertia ((21.16) there), are statements about bodies with scalar hopping and about that response.
6. **The causal order is approximate.** There are two different speeds in the results: the maximal speed of a body, set by its hopping and its records (5.11), and the speed of the influence bound, set by the pair terms of a chain of cells (7.17). Their relation is not derived.

## 5. What is missing, and open problems

- **Limits of the answer to criterion 8:** detectability is defined with respect to re-timings by constant factors of two parts, with readings at stated values of $`\lambda`$. Re-timings that are not linear or that depend on the position, more than two parts, and events defined by records or by the readings of clocks are not treated. The contracts with a detectable common now are characterized by (10.14) but not classified explicitly.
- **Open mathematical statements** (07, Step 10): for $`n\ge3`$ cells, whether a generic chain has no blind delay, and whether two readings on the same cell always influence each other at every positive delay for a generic chain. If both hold, $`\prec`$ is generically the order of $`\lambda`$ for every $`n`$.
- **Limits of the Model D results:**
  - they hold in the weak-record regime; beyond it the records act on the body (random force and loss of coherence, noted in 05, 06, 08) and this is not derived here;
  - they are of first order in the level spacing of the clock; at second order the tick is not sharply defined (5.23);
  - the inertia of a clock that ticks (a superposition of levels) is not derived (06);
  - nothing is derived for many periods of the label under a gradient (09), or for transitions between the branches.
- **Model dependence:** how special Model D is among the allowed bodies, and whether the same laws hold in two or three dimensions, is not known.
- **Not forced by the language:** a mechanism that would give all types the same maximal speed (8.9), or all clocks the same coupling (4.18).
- **Composite bodies:** the inertia of bound bodies of the Model D type, and the fate of (21.16) of 03-ilang-space/21-composite-body for them.
- **Readings:** sequences of joint readings of different clocks, and the count of turns of a cyclic clock (04).
- **Speeds:** the relation between the maximal speed of bodies and the speed of the influence bound (7.17); the actual speed of the front of a body.
- **Handed to the gravity stage:** the behaviour of a body and its clock when a field object multiplies the body's rest and clock term (the lapse form (4.15) for a body), and whether the fall is then independent of the body.

## 6. Quality record

**External verification** (an independent external referee model saw only the referee prompt, the base problem, the question without "Expected result", the derivation and its code):
- minor issues, recorded without regeneration: 02;
- minor issues, fixed by an external regeneration: 03, 04, 09, 10 (one round each);
- major issues in the first round, fixed: 05, 06, 07, 08;
- second round: major issues again in 05 and 06, fixed in v3; minor issues in 08, fixed in v3; 07 judged correct.

**Not externally re-checked.** The current versions of 03, 04, 05, 06, 08, 09 and 10 answer their last external round. The main model reviewed them; no external round has seen them. For 05 v3 and 06 v3 the last changes were substantive (the relation between rate and velocity in 05; the error bound of the average in 06). For 08 v3 they were corrections of wording in a version the referee had confirmed.

**Revised question.** The last sub-item of item 4 of 07 originally asked, for every $`n`$, whether one chain with generic pair terms has influence at every positive delay. Two versions decided this for $`n=2`$ only. On the user's decision the sub-item was narrowed on 2026-10-10: decide $`n=2`$; for $`n\ge3`$ state what is proven and what remains undecided. The first external round judged v1 against the original wording, the second judged v2 against the revised one.

**Known minor issues, not fixed.** 02: (I1) the statements on which readings exist need qualifications on admissibility and label independence when objects of the clock's type lie on both sides of the cut; (I2) the Result line of (2.8) omits the case of a stationary view, which indexes nothing (the derivation step is correct).

**Main-model errors found by the referee and recorded as lessons.** In each case the main model had accepted the version:
- a requested item answered at a lower order than asked (05 v1), for a narrower class than asked (06 v1), or left open (07 v1);
- a quantity named by the question replaced by another one (05 v2: the velocity in the rate–velocity relation);
- an error estimate that does not hold on the whole range for which it was stated (06 v2);
- a claim of convention independence tested only against uniform rebookings (08 v1).

## Appendix A. Package index

| Package | Topic | Version | External rounds |
|---|---|---|---|
| 02 | clock | v2 | 1 |
| 03 | relational time | v2 | 1 |
| 04 | clock comparison | v2 | 1 |
| 05 | moving clock | v3 | 2 |
| 06 | inertia and internal energy | v3 | 2 |
| 07 | causal order | v2 | 2 |
| 08 | maximal speed | v3 | 2 |
| 09 | proper time | v2 | 1 |
| 10 | global order | v2 | 1 |
