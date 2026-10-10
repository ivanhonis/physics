# Question: 07-causal-order

- **Subproject:** 04-ilang-time
- **Package:** 07-causal-order
- **Equation tags:** (7.k)
- **Created:** 2026-10-10
- **Revised:** 2026-10-10 (item 4, last bullet: the question on generic chains is split, and its scope for $`n\ge3`$ is narrowed)

## Goal

Take readings as events. Determine when a reading on one object can change the statistics of a later reading on another object, given that the contracts couple neighbouring objects of a chain. Determine how this influence depends on the delay and on the distance along the chain, and whether the order of events it implies is sharp (a light cone) or only approximate. This is criterion 7. Whether the order of $`\lambda`$ itself can be detected is criterion 8 and not part of this package.

**Setting.**
- **Objects.** A chain of $`n\ge2`$ cells, objects $`1,\dots,n`$ of pairwise different types (each the only instance of its type), with place sets $`H_i`$, $`d_i\ge2`$.
- **Contracts.** $`C=\sum_{i=1}^nD_i+\sum_{i=1}^{n-1}J_i`$.
  - $`D_i`$ acts on cell $`i`$ alone (a single-object term, booked in a pair term by A5).
  - $`J_i`$ is a pair term on cells $`i`$ and $`i+1`$.
  - All are self-adjoint and extended by the identity. Write $`\lVert J\rVert:=\max_i\lVert J_i\rVert`$ (operator norm).
- **Events.** An event is a reading on one cell at a stated value of $`\lambda`$ (A8). A reading $`R`$ on cell $`i`$ is a partition of $`H_i`$, with projectors $`\Pi^{(i)}_r`$ extended by the identity. Between readings the state evolves by (1.9).
- **Outcome-averaged statistics.** For a reading $`R_i`$ on cell $`i`$ at $`\lambda_1`$ and a reading $`R_j`$ on cell $`j`$ at $`\lambda_2`$, consider two quantities:
  - $`P_j(r'\mid R_i)`$: the probability of outcome $`r'`$ of $`R_j`$, averaged over the outcomes of $`R_i`$ with their probabilities;
  - $`P_j(r')`$: the same probability without $`R_i`$.
- **Influence.** $`R_i`$ at $`\lambda_1`$ **influences** $`R_j`$ at $`\lambda_2`$ if $`P_j(\cdot\mid R_i)\neq P_j(\cdot)`$ for the given start. The size of the influence is $`\delta P:=\sum_{r'}\lvert P_j(r'\mid R_i)-P_j(r')\rvert`$.
- **Distance.** $`r:=\lvert i-j\rvert`$ is the distance along the chain.

1. **No influence without delay.** Determine whether $`R_i`$ at $`\lambda_1`$ can influence $`R_j`$ at $`\lambda_2`$ when $`\lambda_2=\lambda_1`$ and $`i\neq j`$, and when $`\lambda_2<\lambda_1`$.

2. **Order of the influence.** Let $`\lambda_2=\lambda_1+\delta`$ with $`\delta>0`$ and $`r\ge1`$.
   - Determine the lowest power of $`\delta`$ at which $`\delta P`$ can be nonzero, and its coefficient: an exact expression in the contract terms, the projectors and the state at $`\lambda_1`$.
   - Give an explicit example with qubit cells in which the coefficient is nonzero, for $`r=1`$ and for $`r=2`$.

3. **Bound.** Determine an upper bound on $`\delta P`$, valid for every start, every pair of readings and every $`\delta\ge0`$, in terms of $`r`$, $`\delta`$ and $`\lVert J\rVert`$ only. Determine whether the bound depends on the $`D_i`$.

4. **Sharpness and the order of events.**
   - Determine whether $`\delta P`$, as a function of $`\delta\ge0`$, can vanish on an interval $`(0,\varepsilon)`$ and be nonzero for some larger $`\delta`$.
   - Conclude whether the influence has a sharp boundary: no influence at all outside some cone in the plane of $`(r,\delta)`$.
   - From item 3, determine the set of $`(r,\delta)`$ in which $`\delta P`$ is below a given $`\epsilon>0`$ for every start, and the speed (cells per unit $`\lambda`$) at which its boundary moves for large $`r`$.
   - Define $`e_1\prec e_2`$ for two events if some reading at $`e_1`$ influences some reading at $`e_2`$ for some start. "Generic" below means: outside a set of measure zero in the real parameters of the pair terms.
     - Determine whether $`\prec`$ implies $`\lambda_1<\lambda_2`$.
     - **Generic pair terms, one prescribed delay.** For fixed cells $`i,j`$ and one fixed pair $`\lambda_1<\lambda_2`$, determine whether $`e_1\prec e_2`$ holds for generic pair terms.
     - **One fixed generic chain, all delays.** Determine whether one chain with generic pair terms has $`e_1\prec e_2`$ for every pair of events with $`\lambda_1<\lambda_2`$. Decide this for $`n=2`$. For $`n\ge3`$, determine what can be proven, and state exactly which statements remain undecided; a complete answer for $`n\ge3`$ is not required. Keep this statement apart from the one for a prescribed delay.
     - Determine whether $`\prec`$ is transitive: in general, and in the cases in which the previous sub-item is decided.

## Inputs

None. The package builds only on the base problem.

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5).
- Readings are applied at stated values of $`\lambda`$ (A8). The statistics compared are outcome averages; the outcome of $`R_i`$ is not used to select later statistics.
- $`n`$ is finite (A1). Statements for long chains are uniform in $`n`$; state where this is used.

## Scope

- In scope:
  - single-cell readings as events on a chain with nearest-neighbour pair contracts;
  - the outcome-averaged influence of one reading on one later reading;
  - the order of events this implies.
- Out of scope:
  - events defined by records (recording contracts), and sequences of more than two readings;
  - contract graphs other than a chain, except as remarks;
  - for $`n\ge3`$, a decision whether one fixed generic chain has influence at every positive delay: only what item 4 asks is required, and the rest may remain open;
  - the relation of the cells to the background of 03-ilang-space, and to its maximal speed;
  - whether the order of $`\lambda`$ is detectable (criterion 8);
  - any physical meaning of $`\lambda`$ (M1).

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: derive. A standard bound for nested commutators in the interaction picture may be used, stated.
- Item 4: short argument for sharpness and transitivity; derive the set and the speed.

## Expected result

- Item 1: a yes/no answer in each case.
- Item 2: a power of $`\delta`$, an exact coefficient, and two explicit examples.
- Item 3: an inequality and a yes/no answer.
- Item 4: a yes/no answer; a conclusion; a set and a speed; for $`\prec`$: a yes/no answer, a yes/no answer for a prescribed delay, for all delays a yes/no answer for $`n=2`$ and a statement of what is proven and what is undecided for $`n\ge3`$, and a yes/no answer on transitivity with its conditions.

Give every main result a tag $`(7.k)`$.

Consistency checks, at most three: for example $`J_i=0`$ for one link, $`n=2`$, and the limit $`\delta\to0`$.

## Code

None.
