# Closing report: 03-ilang-space

- **Subproject:** 03-ilang-space. Space inside Ilanguage 1.b, route P: space from the view.
- **Date:** 2026-10-09. **Revised:** 2026-10-09, after an external critical review of the published material (section 6).
- **State:** all 23 derivation packages (02–24) are verified, and every one has had at least one external verification round. The current versions of 14–24 are regenerations that answer the last external round; only the main model reviewed them (section 6). The dependency graph passes `graphcheck`.
- **Scope of this report:** it summarizes the verified results against the success criteria of `01-base-problem/problem.md`, citing packages and tags. It adds no results. Interpretations are marked as such.
- **Status labels:**
  - **proven**: derived at the physicist-formal standard (every step justified, standard facts used without proof), reviewed by the main model and checked by an external AI referee. It is not a formal proof.
  - **conditional**: proven under stated assumptions;
  - **candidate**: numerical evidence only;
  - **open**: not settled.
- **Workflow:** the derivations, reviews and external checks are made by AI models in a human–AI research workflow.

## 1. Question and approach

The question: can a space-like structure be derived inside Ilanguage 1.b from the language's own elements, without importing any spatial notion (M1–M6)? Which of the features needed for a later study of gravity follow, and under which conditions?

**Approach (route P).**
- The points of space are the places of an object (a *probe* or a *body*), as distinguished by the rest of the system.
- The distance between two places measures how differently the companion *witnesses* them in the view (1.5)–(1.7).
- Space appears as soon as a contract *records* the probe's place in a medium. All further structure is built on this: neighbours, chains, dimension, bodies, motion, cost, curvature and continuum limits.

## 2. Answers at a glance

| # | Criterion | Status | Main packages and tags | Answer in one line |
|---|---|---|---|---|
| 1 | Points | proven | 03 (3.1)–(3.4) | Points are classes of places whose companion branch states coincide ($`W=1`$); they are label-free. |
| 2 | Distance | proven | 03 (3.5), (3.12)–(3.13); 05 (5.10)–(5.11) | The witness angle $`\alpha=\arccos\sqrt W`$ (Fubini–Study) is a metric, unique up to scale under additivity. At small $`\lambda`$ it is Euclidean: $`\alpha\approx\lambda\lVert u_h-u_{h'}\rVert`$. |
| 3 | Neighbourhood, locality | proven / conditional | 04 (4.1)–(4.7); 08 (8.15)–(8.16); 11 (11.3)–(11.11) | Neighbours follow the relative-neighbourhood rule. From a product start, edges need contracts across the cut. Influence spreads one cell per order of $`\lambda`$ (perturbative light cone). |
| 4 | Paths, geodesics | conditional + candidate | 22 (22.5)–(22.11), (22.27), (22.29), (22.32)–(22.36); 23 (23.9) | The Euclidean limit has unique straight geodesics. On the spherical limits geodesics are great-circle arcs, unique except for antipodal pairs, and some caps are not length spaces. Fixed periodic chain geometries are polygonal (anisotropic, non-unique geodesics). Random local arrangements are numerically compatible with isotropy. |
| 5 | Dimension, continuum | proven / conditional | 05 (5.14); 07 (7.7); 14 (14.4)–(14.16); 22 (22.6), (22.13), (22.18), (22.22), (22.27), (22.36) | The dimension is the record capacity of the medium, fixed by the description. Continuum limits exist for the studied families, except for the compact window family, which collapses. |
| 6 | Body | proven | 15 (15.3)–(15.7), (15.20)–(15.21) | Localized, persistent, label-free bodies exist, with positions and a two-body distance. |
| 7 | Background across $`\lambda`$ | proven | 24 (24.3)–(24.11), (24.18), (24.24), (24.28) | Points are identified through places. Generic points never split; some coincide at isolated $`\lambda`$ and separate again after. The neighbour structure (not the metric) is stable below $`\lambda_*>0`$, with $`\lambda_*\sim1/\text{size}`$ for linear records and size-independent for local windows. |
| 8 | Time | handed over | — | Handed to the time project. All rates here are per $`\lambda`$. |
| 9 | Velocity, acceleration | proven | 17 (17.4)–(17.7), (17.20); 20 (20.7) | Currents, velocity and a contract-implied maximal speed $`v_{\max}`$; an exact acceleration identity. |
| 10 | Localized cost, mass | proven | 20 (20.2)–(20.5), (20.10); 21 (21.10), (21.16) | A region's cost changes only through the contracts across its boundary. The inverse inertia is fixed by the edge (motion) costs and can vanish. On the chain, binding raises the inertia by $`\lvert E_{\rm bind}\rvert/v_{\max}^2`$, opposite in sign to the relativistic mass defect. |
| 11 | State-dependent geometry | proven / conditional | 06 (6.9)–(6.13); 08 (8.10)–(8.16); 18 (18.4)–(18.16); 19 (19.1)–(19.20) | Bodies change the geometry only through non-commuting records, locally. Curvature has three sources. A mediated influence exists but is not sourced by cost. |
| 12 | Common space | proven | 12 (12.12)–(12.15); 16 (16.5), (16.8)–(16.13), (16.17) | Identical probes share one background. Two types share points, in the sense of the correspondence of 16, only if their record clouds are translates; otherwise only displacements compare. |

The success line of the base problem ("items 1–7 and 9–12 are derived; item 8 is handed over") is met. Several items are answered with conditions or with negative results that name what is missing (section 5).

## 3. Results by criterion

### I. Space at fixed $`\lambda`$

**Points and distance** (criteria 1–2).
- The view of a part is the Gram matrix of the companion's branch states (2.2). It is fixed by the witness weights $`W(h,h')=\lvert\langle E_{h'}\vert E_h\rangle\rvert^2`$ and their cyclic products, up to local phases (2.10)–(2.13).
- Points are the classes $`W=1`$ (3.1)–(3.2). They do not depend on labels (3.3)–(3.4).
- $`\alpha=\arccos\sqrt W`$ is a metric (3.5). Every triangle with sides in $`[0,\pi/2]`$ is realizable under condition (R) (3.6)–(3.8). Additivity on aligned triples forces $`\alpha`$ up to scale (3.12)–(3.13).
- A recording contract $`\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$ gives $`W`$ (5.6), independent of the probe's weights. At small $`\lambda`$, $`\alpha/\lambda\to d_0=\lVert u_h-u_{h'}\rVert`$ with record vectors $`u_h=(K_h-\langle K_h\rangle)\chi`$ (5.10). The background is a subset of a Euclidean space (5.11).

**Neighbourhood and locality** (criterion 3).
- Related points have $`W>0`$ (4.1)–(4.2). Neighbours are related pairs with no third point that overlaps more strongly with both (4.3); the rule does not depend on the metric transform (4.4).
- The chain distance $`\ell`$ (4.6)–(4.7) extends $`\alpha`$ beyond its saturation at $`\pi/2`$.
- Without contracts across the cut, a product start never acquires a geometry: it stays a product, with one point and no edge (11.3). From any start, the view then evolves only under the part's own contracts, with a $`\lambda`$-independent spectrum (11.4): no geometry is created through the cut, but a correlated start can carry one. At small $`\lambda`$ the boundary contracts alone fix $`d_0`$ and the edges (11.6)–(11.11). A nonempty boundary is not sufficient (11.16).
- In a medium of cells with link contracts, a body changes $`W`$ at the earliest at order $`\lambda^{3+r}`$, $`r`$ links away (8.15)–(8.16). This is a perturbative light cone, not a Lieb–Robinson bound.

**Dimension** (criterion 5, first part).
- $`\dim_0`$ is the affine rank of the record vectors, at most $`\min(n-1,2d_c-2)`$ (5.14).
- Generic records give $`\dim_0=\min(n-1,2(d_c-1))`$, or $`\min(n-1,d_c-1)`$ for real ones (7.7), (7.11).
- Independent channels add up (14.4)–(14.7). A generic 3D background needs total capacity 3, with minimal medium dimension 4 (14.15)–(14.16).
- **The language does not select 3; the description does.**
- The loop data are the Kähler form of the record geometry: $`\Phi=-\lambda^2\sum\omega(u_j,u_{j+1})`$ (10.8)–(10.14). The $`\lambda^2`$ term vanishes for commuting or real records; for real records the loop data are odd in $`\lambda`$ (10.15).

**Paths, continuum, isotropy** (criteria 4–5).
- **Direct distances.**
  - $`d_0`$ on a dense square family converges to the Euclidean square, with unique straight geodesics (22.5)–(22.6).
  - At fixed $`\lambda`$, a qubit medium gives a cap of the round sphere of radius 1/2 (curvature 4), or the whole $`\mathbb{CP}^1`$ (22.12)–(22.13). It is a length space iff $`\lambda r_0\le\pi/4`$ or $`\lambda r_0\ge\pi/2`$. Its geodesics are great-circle arcs, unique except for antipodal pairs.
- **Chain distance on regular arrangements.** On a square family, the chain distance is the $`\ell^1`$ (taxicab) norm, even where $`d_0`$ is Euclidean: box betweenness, binomially many shortest chains, $`\max\ell_0/d_0=\sqrt2`$ (22.7)–(22.11).
- **Compact window records** collapse. This is shown for the window family of 22, not for every compact local record. Saturation ties make distant places neighbours, the diameter stays bounded, and there is no continuum limit for any scaling (22.14)–(22.18), with exact $`\ell`$ and diameter for every size (22.16)–(22.17), (22.30)–(22.31).
- **Quasi-local records** (exponential tails) give continuum limits of dimension 1 and 2 (22.22), (22.27). The neighbour decisions for far pairs rest on margins $`\sim q^{r/2}`$ (22.23).
- **Periodic arrangements.** A fixed periodic pattern always gives a polygonal norm, never an isotropic one (22.29) (conditional on (F1)–(F3)). The same holds for patterns of bounded complexity under (F4) (22.32).
  - An isotropic limit is possible with periodic patterns of growing complexity. In the explicit Crofton construction the records are non-local half-plane indicators: $`\cos\alpha=(\cos\lambda)^{d_G}`$, $`\ell=\lambda d_G`$, and the limit is Euclidean (22.33)–(22.36).
- **Random local arrangements** (code package 23, precommitted).
  - The large-scale chain distance is compatible with isotropy to within 0.4%: $`\bar B_{128}=0.9995\pm0.0021`$, "isotropy supported" (23.9). The periodic control gives $`B=1.30`$ (23.8). This is evidence from finite samples, not a continuum theorem. Status: **candidate**.
  - Robustness was classified "intermediate" (23.10). Non-local admixtures of size $`\varepsilon`$ create long edges: the shortest long edge was at $`r=66`$ for $`\varepsilon=10^{-4}`$ and at $`r=46`$ for $`\varepsilon=10^{-2}`$. These are observations for one realization and one perturbation; 23 states no general locality condition.

### II. Bodies, motion, background

**Bodies** (criterion 6).
- A localized body stays localized and uncorrelated; its position is $`[\beta]_0`$ (15.3)–(15.4).
- Two bodies of one type give an exact product state, with a well-defined distance $`D=\lVert u_{\beta_1}-u_{\beta_2}\rVert`$ (15.5)–(15.7).
- The medium records only the sum of the bodies' record vectors (15.11)–(15.13). With linear records the separation is never recorded (15.15)–(15.16); local windows record it (15.17)–(15.19), except at revivals (15.21)–(15.22).

**Motion and velocity** (criterion 9).
- The currents are $`J=2\mathrm{Im}[t\,(V_b)_{h'h}]`$ (17.4), bounded by the witness weight (17.5).
- The velocity is (17.6). The maximal speed is $`v_{\max}=\varrho(\lvert t\rvert d_0)\le\max_h\sum\lvert t\rvert d_0`$ (17.7); on the chain, $`v_{\max}=2t\sigma_X`$ (17.20).
- Records slow hops in proportion to their background length (Zeno-like) (17.10).
- Linear records act as a random uniform force (17.18)–(17.22). A body's spread stays bounded (Bloch oscillation, Wannier–Stark localization) iff the medium state has no component in the kernel of the record generator $`X`$ (17.23); otherwise the spread grows without bound.
- The acceleration obeys an exact identity (20.7).

**Background across $`\lambda`$** (criterion 7).
- For two places, $`W(\lambda)=1`$ either for all $`\lambda`$ or on a discrete set (24.3)–(24.4). Off a discrete set the points are the generic ones. At isolated $`\lambda`$ some generic points coincide and separate again after; a generic point never splits (24.5)–(24.6).
- The neighbour graph changes only on a discrete set (24.8). The stability scale $`\lambda_*`$ is positive (24.9). Trajectories are analytic for all $`\lambda`$ and continue across mergers (24.10)–(24.11).
- Linear records on a qubit: the line closes into a circle at $`\lambda_*=\pi/(\lfloor3n/2\rfloor-1)`$ (24.18)–(24.20).
- General linear records: $`\lambda_*=\Theta(1/n)`$ (24.24).
- Local windows: $`\lambda_*=\pi/2`$, independent of size (24.28).

### III. Connection to gravity

**State-dependent geometry and curvature** (criterion 11).
- **A body changes a probe's geometry.**
  - It does so only through records that do not commute with the probe's (6.7), (6.9)–(6.13); the effect first appears at $`\lambda^3`$.
  - In a cell medium it does so locally, at $`\lambda^{3+r}`$ for $`r`$ links between them (8.15)–(8.16).
  - In the qubit example the sign follows the record strength, not the cost (6.14)–(6.15).
- **The background metric** is the Fubini–Study pullback (19.1)–(19.2). Its leading curvature is the Gauss curvature of the record surface (19.8)–(19.10).
- **Curvature has three sources:**
  - the shape of the record map (medium state);
  - finite $`\lambda`$ (e.g. curvature 4 for a qubit medium) (19.16)–(19.17);
  - bodies, only through non-uniform effects (19.13)–(19.15).
- **Mediated influence on motion.**
  - One body influences another's motion through the medium only via commutators, and the influence is independent of the source's cost (18.4), (18.12).
  - With linear records it is even in the source strength, and the directed drift appears only at $`\lambda^8`$ (18.13)–(18.16).

**Cost and mass** (criterion 10).
- **Distribution of the cost.**
  - The cost splits exactly into site costs and edge costs, free of conventions (20.2).
  - Only the edge costs and the differences of site costs per unit weight are fixed by readings (20.3)–(20.4).
  - The cost of a region changes only through the contracts across its boundary (20.5). This is conservation region by region along the contracts; it is locality in the derived space only where the contract graph matches the neighbour graph.
- **Inertia.**
  - The inverse inertia is the initial response to a uniform cost gradient. It is minus the edge cost, weighted by the background edge vectors: $`\mu=-\sum_EL_{hh'}\Delta\otimes\Delta`$ (20.10). It depends on the state and can vanish. The site costs give only the force.
  - A localized body has no instantaneous response (20.11).
- **Composite bodies.**
  - The inertia of a composite comes from its parts' edge costs: $`\mu_c=\tfrac14(\mu_1+\mu_2)`$ (21.10).
  - On the chain, binding raises the inertia by exactly $`\lvert E_{\rm bind}\rvert/v_{\max}^2`$ (21.16): the bound pair is heavier than its parts, an effective band-mass effect of the lattice.
    - The size has the form $`\lvert E_{\rm bind}\rvert/v_{\max}^2`$, but the sign is opposite to the relativistic mass defect, where binding lowers the mass.
    - No relativistic identification is derived, and the result is shown for the 1D chain only.
  - The absolute version $`I\,v_{\max}^2=-E_{\min}`$ (21.17) depends on the cost zero, which no reading fixes.
- **Inertial versus active mass.** Inertia is tied to a part of the cost (20.10), but the mediated influence is not sourced by the cost (18.12). In the static recording media studied here, inertial and active mass therefore do not coincide.

**Common space** (criterion 12).
- Identical probes see the same background, provided the contracts respect Law 5 (12.4), (12.12)–(12.15).
- For two types, the split of medium-only terms is a convention (16.3)–(16.4). The well-defined quantities are the functions of $`u^A_h+u^B_k`$ (16.5).
- A common set of points exists iff the record clouds are translates; the correspondence is then unique (16.11)–(16.13).
- The centred cross distance is fixed (16.17). The raw cross-type distance is not (16.6), (21.3).

## 4. Cross-cutting findings (interpretation)

1. **A space-like structure is derivable without importing spatial notions.** The view, together with a recording contract, gives points, a Fubini–Study metric, a Euclidean small-$`\lambda`$ geometry, neighbours, chains, bodies, motion, cost densities and curvature. All of these are built from the language's elements; the quantum formalism of Ilanguage 1.b is the starting point, not an import.
2. **The language does not select the geometry; the description does.** This holds for the dimension (14), the isotropy (22, 23) and the medium's capacity. Ilanguage 1.b provides the mechanism, not the values.
3. **Linear, lattice-like records are too rigid.** Their geometry is clean, but:
   - they give no separation sensing (15);
   - they give no transport unless the medium state has a component in the kernel of the record generator (17.23);
   - mediated effects are even and origin-dependent (18);
   - the stability scale shrinks with size (24).
4. **Local records are necessary but delicate.**
   - Large distances need chains, and the compact window family collapses (22).
   - Quasi-local records give continua (22). In the random run, small non-local admixtures created long edges, and robustness was only intermediate (23).
   - Fixed periodic arrangements are anisotropic (22.29); random ones are numerically compatible with isotropy (23.9, candidate).
5. **Gravity-like behaviour does not arise in the static recording media studied here.** The mediated influence is not cost-sourced (18.12), and inertial and active mass differ (20, 21 versus 18). This is a negative result for these model families, not an impossibility theorem. Media with their own dynamics (links, local records) are the natural next step.

## 5. What is missing, and open problems

- **Negative or conditional results**, naming what Ilanguage 1.b with the formalization of `problem.md` lacks:
  - a cost-sourced, directed mediated interaction in static recording media (18);
  - a canonical zero of the cost, so that only cost differences are physical (20.3), (21.17);
  - isotropy from a fixed periodic local description (22.29);
  - scale-free stability of linear-record backgrounds (24.24).
- **Open:**
  - one contract system that gives the geometry, bodies, local motion and a stable continuum limit together (the examples here show these properties separately);
  - an operational procedure that reconstructs the distances from admissible preparations and readings;
  - isotropy of local records in 3D;
  - the binding–inertia relation (21.16) beyond the 1D chain, and its physical reading;
  - $`\Lambda_N`$ in closed form for general records (24.30 is implicit);
  - media with internal dynamics as the source of gravity-like effects;
  - the time project's clock $`\tau(\lambda)`$, needed to convert all rates;
  - the interface with the gravity programme's $`K_{\rm rel}`$.

## 6. Quality record

**External verification** (an independent external referee model saw only the referee prompt, the base problem, the question without "Expected result", the derivation and its code):
- correct: 02, 03, 04, 07, 08, 09;
- minor issues, recorded without regeneration: 05, 06, 10, 11, 12, 13;
- fixed by external regeneration: 14, 16, 17, 19, 20, 21, 23, 24 (one round each);
- 15, 18 and 22 needed two rounds (major issues in the first round, fixed; 22 also in the second).

**Not externally re-checked.** The current versions of 14–24 (v2 or v3) answer the last external round. The main model reviewed them; no external round has seen them.

**Known minor issues, not fixed.** The referee found these in the current versions. They were accepted as minor and left without regeneration; details are in each package's verification file.
- 05 (I1): the line has dimension 1 only with at least two places; a single point has dimension 0.
- 06 (I1): the angle expansion needs a quantitative validity condition when $`d_0`$ is small; $`\lambda\lVert K\rVert\ll1`$ alone is not enough.
- 10:
  - (I1) the geometric form of the saturation condition needs a nondegeneracy qualification;
  - (I2) consistency check 3 states the leading-order saturation as an exact phase equality.
- 11:
  - (I1) regrouping local terms changes the fixed cut notation;
  - (I2) the full ordering of distances need not be preserved;
  - (I3) the restriction on when item 2 is informative is too strong;
  - (I4) scaling with a negative factor needs $`\lvert s\rvert`$.
- 12:
  - (I1) a nonunique decomposition is not automatically a convention of the description;
  - (I2) nonconstant record differences need not produce unequal distances.
- 13:
  - (I1) cell typing and admissibility under Law 5 are not specified;
  - (I2) the cited T2 and T3 outputs are compact summaries, not raw data.

**Main-model errors found by the referee and recorded as lessons:**
- accepting an unanswered requested item as an "open issue" (18, 22);
- an imprecise question that did not fix what is held constant across a family (22);
- a miscalibrated precommitted tolerance (13, T3(a)).

**Revision after an external critical review (2026-10-09).** A critical review of the published material reproduced the numerical runs of 13 and 23 and found no error in the derivations. It found statements in this report that went beyond them, and these are now corrected:
- the binding result (21.16) was read as an analogue of the relativistic mass defect, but its sign is opposite;
- a $`\ln(1/\varepsilon)`$ cut-off was read into 23, which 23 v2 explicitly does not claim;
- several summaries lacked conditions that the derivations state:
  - geodesics on the spherical limits;
  - fixed versus growing periodic patterns;
  - the numerical status of isotropy;
  - the kernel condition for transport;
  - the product start for the cut boundary;
  - the merging of points;
  - the window family;
  - the meaning of the inverse inertia.

## Appendix A. Package index

| Package | Topic | Version | External rounds |
|---|---|---|---|
| 02 | view content | v1 | 1 |
| 03 | witness distance | v1 | 1 |
| 04 | neighbours | v1 | 1 |
| 05 | recording contract | v1 | 1 |
| 06 | body in medium | v1 | 1 |
| 07 | random records | v1 | 1 |
| 08 | cell medium | v1 | 1 |
| 09 | measurability | v1 | 1 |
| 10 | loop data | v1 | 1 |
| 11 | cut boundary | v1 | 1 |
| 12 | identical probes | v1 | 1 |
| 13 | numerical run (code) | v1 | 1 |
| 14 | dimension | v2 | 1 |
| 15 | bodies | v3 | 2 |
| 16 | common space | v2 | 1 |
| 17 | motion | v2 | 1 |
| 18 | mediated effect | v3 | 2 |
| 19 | curvature | v2 | 1 |
| 20 | cost and mass | v2 | 1 |
| 21 | composite body | v2 | 1 |
| 22 | large-scale geometry | v3 | 2 |
| 23 | random arrangements (code) | v2 | 1 |
| 24 | background stability | v2 | 1 |
