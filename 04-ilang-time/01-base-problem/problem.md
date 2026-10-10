# Base problem: 04-ilang-time

- **Subproject:** 04-ilang-time
- **Created:** 2026-10-09

## Research question

This subproject is the second stage of the research programme "Gravity in the description language Ilanguage" (group `gravity`). The first stage, 03-ilang-space, derived a space. This stage asks for a time, and for the time-related structures that later stages on gravity need. Gravity itself is not part of this subproject.

**Question.** Can a physical time be derived inside the description language Ilanguage 1.b (quoted under "Physical setting and model") from the language's own elements alone, without importing any temporal notion, for bodies in the space derived in 03-ilang-space? Which of the features listed under "Success criteria" follow (clocks, time relative to the ordering parameter $`\lambda`$, comparison of clocks, proper time and moving clocks, inertia and internal energy, a common maximal speed, causal order), under which conditions, and which cannot be obtained?

**Working hypothesis.** Time is not a primitive of Ilanguage 1.b: $`\lambda`$ is only the ordering parameter of the evolution. If a physical time appears, it arises from structures the language already contains. The primary route is the clock: a part of the system whose readings change under its contracts, so that the evolution of other parts can be stated relative to its readings instead of $`\lambda`$. Readings (Law 1), the view (Law 2) and the contract system (Law 4) are further existing structures; they may be used alone or together with clocks.

Everything is derived within this subproject. No result is assumed beyond Ilanguage 1.b, the formalization fixed in this file, and the results of 03-ilang-space that a package quotes verbatim in its question, with a cross edge.

### Methodological constraint: no imported notions

- **M1.** No temporal notion is a primitive. None of the following may be assumed: a physical time, a duration, a physical rate, a clock, simultaneity, a causal order, a light cone, an arrow of time. Such a notion may appear only as a defined notion, built explicitly from the elements of Ilanguage 1.b. $`\lambda`$ is the ordering parameter of the evolution and nothing more: that a quantity depends on $`\lambda`$ does not make it a time.
- **M2.** Spatial notions come only from 03-ilang-space. Positions, distances, velocities and the maximal speed of bodies are those derived there, quoted verbatim in the questions that use them. No other spatial notion is imported; constraint M1 of 03-ilang-space continues to hold.
- **M3.** Mass is not imported. A notion of inertia or mass must be derived, for example from the cost, as in 03-ilang-space.
- **M4.** No physical theory that already contains time, a clock or a spacetime structure may be used as an input: for example special relativity, Lorentz transformations, a given physical clock model or a background spacetime. A description may use any contracts that the language allows; what they mean physically is derived, not assumed.
- **M5.** Standard mathematics may be used freely. Applying a mathematical notion (an order, a parametrization, a group, a limit) is not an import when the object it is applied to is built explicitly from Ilanguage elements.
- **M6.** Every derived structure must be well defined. It may not depend on the description labels of identical-type instances (Law 5), on the common phase of the state (1.2), or on any other convention of the description, for example the phase split in (1.6) or the pair term in which a single-object term is booked (A5).

## Physical setting and model

The model is Ilanguage 1.b. Its text is quoted below verbatim from the reference document of the subproject `00-ilanguage` (Ilanguage 1.b, version 1.b, 2026-10-09), with the reference document's equation tags $`(0.k)`$. Section 8 of the reference document (the absence of a copy constructor) is not quoted here; a package that needs it quotes it in its question. The formal forms that every package uses follow under "Formal form", with tags $`(1.k)`$. They are the same as in 03-ilang-space, so that results of the two subprojects can be combined in one description.

### Text of Ilanguage 1.b (verbatim)

This is a description language. It describes systems by means of object-oriented programming patterns.

The language does not say what a system means, and it prescribes no field of application. It fixes only which states and operations can form a valid description.

The language fixes a single formalism: the state is a complex weighting, evolution acts on it linearly, and the contract is an operator defined on the weighting (Section 5). The language does not derive this; it states it. Every further rule is formulated within this frame; the language attaches no meaning to the frame either.

#### 1. Object and state

An **object type** specifies the set of possible values — in the language's terminology, the **places** — and the operations defined on them.

A type has **instances**. An instance is not the same as a state.

##### The state is a weighting

Let the smallest system be an object with two places, whose places are 0 and 1. The places are denoted $`\lvert 0\rangle`$ and $`\lvert 1\rangle`$.

The state is not “0 or 1” but a weighting:

```math
a\,\lvert 0\rangle + b\,\lvert 1\rangle .
\qquad\text{(0.1)}
```

On reading, one obtains 0 with probability $`|a|^2`$ and 1 with probability $`|b|^2`$.

The total length of the weights is fixed:

```math
|a|^2+|b|^2=1.
\qquad\text{(0.2)}
```

In general, if the places are denoted $`\lvert h\rangle`$, the state is

```math
\lvert\psi\rangle=\sum_h a_h\,\lvert h\rangle ,
\qquad
\sum_h |a_h|^2=1.
\qquad\text{(0.3)}
```

The weights are complex numbers.

##### The common phase is not data

Two weightings that differ only by a common complex factor of unit length,

```math
\lvert\psi\rangle
\qquad\text{and}\qquad
e^{i\varphi}\lvert\psi\rangle,
\qquad\text{(0.4)}
```

say the same for every reading.

They therefore mean the same state.

The weighting is the representation; the state is its content.

#### 2. The operations

Two kinds of thing can happen to a state:

1. **evolution**
2. **reading**

##### Evolution

Evolution rotates the weights, preserving their total length.

It is deterministic and reversible.

Its rule is given in Section 4.

##### Reading

Reading yields a single value.

Its outcome is random, and it is not reversible.

The probability of the value obtained is given by the square of the length of the weight belonging to it.

After the reading, the weighting goes over to the part compatible with the value obtained: the weights of the incompatible places become zero, the weights of the compatible places stay unchanged relative to each other, and the total length is again one.

An immediately repeated reading therefore gives the same value.

##### Law 1 — there is no getter without side effects

**Every reading is also a write.**

A reading does not only give information about the state; it also changes it.

#### 3. Composition, ownership and view

##### Composition

The composition of objects is the combination of their possibilities.

If one object has $`n`$ places and the other has $`m`$, then together they have

```math
n\cdot m
\qquad\text{(0.5)}
```

joint places. The joint places are denoted by writing the places of the members side by side: $`\lvert h_1\rangle\lvert h_2\rangle`$, briefly $`\lvert h_1 h_2\rangle`$.

The state of the composite system is a weighting of these joint places.

This is not the same as writing the states of the parts side by side.

Most joint states cannot be decomposed into a product of separate states of the members.

##### Law 2 — the state is owned by the system, not by the instance

**The state is owned by the system, not by the instance.**

The joint state of several objects is a single weighting of the joint places. If it cannot be decomposed into a product of the states of the parts, the parts have no separate complete state; they have only a view.

##### View

A **view** can still be assigned to a part.

The view is a read-only extract computed from the joint state.

It gives the statistics of every local reading that can be performed on the given part, but in general it does not contain enough information to restore the full joint state.

The view is not a separately stored state.

##### The witness rule

Computing the view is a single rule: the possibilities of the companion must be summed out.

The cross term between two places of the member remains to the extent that the companion is the same in the two branches. If the joint state is

```math
a\,\lvert 0\rangle\lvert E_0\rangle + b\,\lvert 1\rangle\lvert E_1\rangle ,
\qquad\text{(0.6)}
```

where $`\lvert E_0\rangle`$ and $`\lvert E_1\rangle`$ are the states of the companion in the two branches, then in the member's view the cross term between the two places is multiplied by the overlap

```math
\langle E_1 \vert E_0\rangle .
\qquad\text{(0.7)}
```

To the extent that the two states of the companion are distinguishable, to that extent the companion becomes a witness, and to that extent the cross term between the two branches decreases. If the two companion states are orthogonal, the cross term vanishes completely.

#### 4. The law of evolution

If an evolution turns the pure place $`\lvert h\rangle`$ into $`\lvert\Psi_h\rangle`$, then the state

```math
\sum_h a_h\,\lvert h\rangle
\qquad\text{(0.8)}
```

must become

```math
\sum_h a_h\,\lvert\Psi_h\rangle .
\qquad\text{(0.9)}
```

Evolution therefore does not choose how it acts depending on the result of the individual weightings; it carries the whole weighting over term by term.

##### Law 3 — evolution is termwise and preserves the total length

**Evolution acts with the same operation on every term of the weighting, and it preserves the total length.**

Because it is termwise, evolution is linear; because it preserves the total length, it is — for finitely many places — unitary, and therefore reversible.

Randomness is not part of evolution. Randomness appears only in reading.

#### 5. The contract

A **contract** can hold between two objects.

A contract assigns a real-valued **cost** to the joint state.

The total cost of the system is the sum of the costs of the contracts.

Let $`C`$ be the self-adjoint operator that describes the whole contract system:

```math
C=C^{\dagger}.
\qquad\text{(0.10)}
```

Then the cost of a state $`\lvert\psi\rangle`$ is

```math
L(\psi)=\langle\psi\vert C\vert\psi\rangle.
\qquad\text{(0.11)}
```

The contract, however, does not only evaluate the state.

The same $`C`$ also determines the evolution:

```math
i\,\frac{\mathrm d}{\mathrm d\lambda}\lvert\psi\rangle=C\,\lvert\psi\rangle.
\qquad\text{(0.12)}
```

Here $`\lambda`$ is the ordering parameter of the evolution. The language attaches no further meaning to it.

##### Consistency with Law 3

Since $`C`$ is self-adjoint, the cost is real for every $`\lvert\psi\rangle`$, and the evolution driven by $`C`$ is unitary: it preserves the total length and is reversible. The real cost and the total-length-preserving evolution come from the same definition; the engine of the contract cannot violate Law 3.

##### Law 4 — the contract is judge and engine

**The same contract system that determines the cost of the state also drives the evolution of the state.**

The system has no separate behaviour independent of its contracts.

The contract system is itself the program that runs.

#### 6. Identity

##### Law 5 — the instance identifier is not data

Instances of the same type have no internal label.

“Which instance is which” is not part of the state of the system.

Swapping two instances of the same type is therefore not an operation on the system but another description of the same system.

The swap cannot change the statistics of any reading.

##### The two families

Let $`P`$ be the swap.

Since the swap does not change the state, it can change the weighting at most by a common complex factor of unit length:

```math
P\,\lvert\psi\rangle = c\,\lvert\psi\rangle ,
\qquad
|c|=1 .
\qquad\text{(0.13)}
```

Since the swap does not change the state, it takes every allowed weighting into a common-phase version of that weighting. The swap acts termwise, and allowed states can be superposed: if two states had different factors, their sum would no longer go into a common-phase version of itself. Hence, within a type, $`c`$ cannot depend on the state.

Since swapping twice gives back the original description,

```math
P^2=\mathbb 1 ,
\qquad\text{(0.14)}
```

hence $`c^2=1`$, and $`c`$ can only be $`+1`$ or $`-1`$.

Objects of the same type thus belong to one of two families:

* invariant under swap ($`c=+1`$),
* sign-changing under swap ($`c=-1`$).

The family of a type cannot be derived; the description specifies it.

Beyond this, the language attaches no meaning to the two families.

#### 7. The laws

| # | Law |
| - | --- |
| 1 | There is no getter without side effects: every reading is also a write. |
| 2 | The state is owned by the system, not by the instance. |
| 3 | Evolution is termwise, preserves the total length and is reversible. |
| 4 | The contract is judge and engine: the same $`C`$ evaluates and drives. |
| 5 | The instance identifier is not data. |

#### 9. The boundary of the language

Beyond this, Ilanguage 1.b does not say what the objects, places, contracts or states represent.

It assigns them no physical or other interpretation in advance.

The task of a description is to specify:

* which object types it uses,
* what places they have,
* which family each type belongs to (invariant or sign-changing under swap),
* what initial state it starts from,
* and what contracts hold between them.

Everything else is part of the given description, not of the language.

### Formal form

Every package uses the following formal forms. The choices behind them are listed under "Assumptions".

**State.** An object type $`T`$ has the place set $`H_T`$. The space $`\mathcal H_T=\mathbb C^{H_T}`$ carries the standard inner product, and the places $`\lvert h\rangle`$ form its orthonormal **place basis**. A state of one object is

```math
\lvert\psi\rangle=\sum_{h\in H_T}a_h\lvert h\rangle,\qquad a_h\in\mathbb C,\qquad \sum_h\lvert a_h\rvert^2=1 ,
\qquad\text{(1.1)}
```

and two weightings that differ only by a common phase,

```math
\lvert\psi\rangle\qquad\text{and}\qquad e^{i\varphi}\lvert\psi\rangle ,
\qquad\text{(1.2)}
```

mean the same state.

**Reading.** A reading is a partition of the places (for a composite system, of the joint places) into classes $`S_r`$, one for each outcome $`r`$. With $`\Pi_r`$ the orthogonal projector onto the span of the places in $`S_r`$:

```math
p(r)=\bigl\lVert\Pi_r\lvert\Psi\rangle\bigr\rVert^2,
\qquad
\lvert\Psi\rangle\;\longmapsto\;\frac{\Pi_r\lvert\Psi\rangle}{\bigl\lVert\Pi_r\lvert\Psi\rangle\bigr\rVert}.
\qquad\text{(1.3)}
```

**Composition.** A system of objects $`1,\dots,N`$ with types $`T(1),\dots,T(N)`$ has the joint space

```math
\mathcal H=\bigotimes_{a=1}^{N}\mathcal H_{T(a)},
\qquad
\lvert K\rangle=\lvert h_1h_2\cdots h_N\rangle=\lvert h_1\rangle\otimes\cdots\otimes\lvert h_N\rangle ,
\qquad\text{(1.4)}
```

and the joint places $`\lvert K\rangle`$ form its orthonormal place basis.

**View.** A **part** $`A`$ is a set of objects of the system, its **companion** $`\bar A`$ is the set of the remaining objects, and $`\mathcal H=\mathcal H_A\otimes\mathcal H_{\bar A}`$. The view of $`A`$ is the partial trace over the companion:

```math
V_A(\Psi)=\mathrm{Tr}_{\bar A}\lvert\Psi\rangle\langle\Psi\rvert .
\qquad\text{(1.5)}
```

Group the joint state by the joint places $`h`$ of $`A`$:

```math
\lvert\Psi\rangle=\sum_h a_h\,\lvert h\rangle\otimes\lvert E_h\rangle,
\qquad
\langle E_h\vert E_h\rangle=1\ \text{ whenever } a_h\neq0 .
\qquad\text{(1.6)}
```

The phase split between $`a_h`$ and $`\lvert E_h\rangle`$ is a convention. The matrix elements of the view are then

```math
\langle h\vert V_A\vert h'\rangle=a_h\,a_{h'}^{*}\,\langle E_{h'}\vert E_h\rangle ,
\qquad\text{(1.7)}
```

the general form of the witness rule (0.6)–(0.7).

**Cost and evolution.** With the self-adjoint contract system $`C`$, the cost of a state and its evolution are

```math
L(\Psi)=\langle\Psi\vert C\vert\Psi\rangle ,
\qquad\text{(1.8)}
```

```math
i\,\frac{\mathrm d}{\mathrm d\lambda}\lvert\Psi\rangle=C\,\lvert\Psi\rangle,
\qquad\text{hence}\qquad
\lvert\Psi(\lambda)\rangle=e^{-iC\lambda}\lvert\Psi(0)\rangle .
\qquad\text{(1.9)}
```

**Contracts** (Assumption A5).

```math
C=\sum_{\gamma}C_\gamma ,
\qquad\text{(1.10)}
```

where each contract $`\gamma`$ holds between two objects $`a_\gamma\neq b_\gamma`$. Each $`C_\gamma`$ is a self-adjoint operator on $`\mathcal H_{T(a_\gamma)}\otimes\mathcal H_{T(b_\gamma)}`$, extended by the identity to the other objects. The cost of a single contract is $`\langle\Psi\vert C_\gamma\vert\Psi\rangle=\mathrm{Tr}\bigl(C_\gamma\,V_{\{a_\gamma,b_\gamma\}}(\Psi)\bigr)`$.

**Families** (Assumption A6). For two objects $`a\neq b`$ of the same type $`T`$, the swap $`P_{ab}`$ exchanges the $`a`$-th and $`b`$-th entries of every joint place:

```math
P_{ab}\lvert\cdots h_a\cdots h_b\cdots\rangle=\lvert\cdots h_b\cdots h_a\cdots\rangle,
\qquad
P_{ab}\lvert\Psi\rangle=c_T\lvert\Psi\rangle,
\qquad
c_T\in\{+1,-1\}.
\qquad\text{(1.11)}
```

The second equation holds for every admissible state and every such pair. The admissible states form the subspace $`\mathcal H_{\rm adm}\subseteq\mathcal H`$.

## Assumptions

Formalization choices for every package of this subproject, where the text of Ilanguage 1.b leaves room. A1–A7 are the choices of 03-ilang-space, unchanged.

- **A1. Finiteness.** Every description has finitely many objects, and every type finitely many places. $`\mathcal H`$ is therefore finite-dimensional and the evolution is unitary. Families of descriptions of growing size and their limits may be studied; a package that takes a limit states it explicitly.
- **A2. Inner product.** $`\mathcal H_T`$ carries the standard inner product, in which the place basis is orthonormal. The place basis is part of the type, not a choice.
- **A3. Closed system, pure state.** The description lists all objects; nothing exists outside it. The state of the whole system is always a unit vector of $`\mathcal H_{\rm adm}`$, up to the common phase (1.2). Views are derived objects, not states.
- **A4. Readings.** A reading is a partition of the joint places, acting by (1.3). A local reading on a part $`A`$ is a reading whose classes depend only on the joint place of $`A`$.
- **A5. Contracts.** $`C`$ is a sum of contract terms between pairs of objects, (1.10). A term acting on a single object is included as $`D\otimes\mathbb 1`$ in a pair term (when the system has at least two objects). The list of contracts and the operators $`C_\gamma`$ belong to the description, and they do not depend on $`\lambda`$. Which pair term a single-object term is included in is a convention (M6): contract lists that differ only in this choice are the same description. The cost of a single contract is therefore defined only up to this choice; the total cost (1.8) does not depend on it.
- **A6. Families.** (1.11) holds for every pair of objects of the same type.
- **A7. Parts and views.** A part is a set of objects, and its view is the partial trace (1.5). Whether, and how, a part consisting of identical-type instances can be specified without labels is a question for the packages (M6), not an assumption.
- **A8. Readings and $`\lambda`$.**
  - A package may apply a reading (1.3) at a stated value of $`\lambda`$. Between readings, the state evolves by (1.9).
  - The value of $`\lambda`$ at which a reading is applied is part of the package's setting; it is not a time (M1).
  - A comparison of readings taken at equal $`\lambda`$ uses the order of $`\lambda`$. Whether that order can itself be detected is criterion 8.
  - A reading may also be represented inside the description, by a contract that writes the read value into a record object that is read later.
  - Each question states which representation it uses.
- **A9. Range of $`\lambda`$.** $`\lambda`$ ranges over $`\mathbb R`$. A package that restricts it, for example to $`\lambda\ge0`$, says so.

## Notation and conventions

- The inner product $`\langle\phi\vert\psi\rangle`$ is antilinear in the first argument and linear in the second. $`z^{*}`$ is the complex conjugate, $`X^{\dagger}`$ the adjoint, $`\mathbb 1`$ the identity, $`\lVert\psi\rVert^2=\langle\psi\vert\psi\rangle`$.
- Types $`T`$; place sets $`H_T`$ with $`d_T=\lvert H_T\rvert`$; places $`h,h',k,\dots`$; place basis $`\lvert h\rangle`$.
- Objects $`a,b=1,\dots,N`$. These are description labels, which by Law 5 are not data for identical-type instances. The type of object $`a`$ is $`T(a)`$.
- Joint places $`K,K'`$ and $`\lvert K\rangle`$ as in (1.4). The joint state is written $`\lvert\Psi\rangle=\sum_K\Psi_K\lvert K\rangle`$.
- Swap $`P_{ab}`$, family $`c_T`$, admissible subspace $`\mathcal H_{\rm adm}`$ (1.11).
- Contract system $`C`$, contract terms $`C_\gamma`$ (1.10), cost $`L`$ (1.8), evolution parameter $`\lambda`$, evolved state $`\lvert\Psi(\lambda)\rangle`$ (1.9).
- Part $`A`$ and companion $`\bar A`$. Joint places of $`A`$ are $`h,h'`$, those of $`\bar A`$ are $`r,r'`$. View $`V_A`$ (1.5); branch weights $`a_h`$ and branch states $`\lvert E_h\rangle`$ (1.6).
- Rates with respect to $`\lambda`$ are written $`\mathrm d/\mathrm d\lambda`$. A physical time, once a package defines one, gets its own symbol (for example $`\tau`$). It is never identified with $`\lambda`$ by notation alone.
- Equation tags: $`(1.k)`$ in this file, $`(P.k)`$ in package $`P`$ of this subproject, $`(0.k)`$ in the reference document Ilanguage 1.b. A result of 03-ilang-space is cited with its qualified package name, for example "(17.7) of 03-ilang-space/17-motion".

## Success criteria

The research question is answered when each item below has a verified package that does one of two things:
- it derives the item, together with the conditions under which it holds; or
- it proves that the item cannot be obtained within Ilanguage 1.b with the formalization of this file, and states what is missing.

The items define what a derived structure is measured against. They are not assumptions, and no item may be used as an input.

**I. Clocks and time**

1. **Clock:** an entity, defined from Ilanguage elements, whose readings change with $`\lambda`$ under its contracts, so that its readings can index the evolution of other parts; how such a clock is read (Law 1), and what limits its resolution.
2. **Time and $`\lambda`$:** a notion of physical time built from clock readings, and its relation to $`\lambda`$; the conditions under which the evolution of other parts can be stated relative to a clock instead of $`\lambda`$; how rates with respect to $`\lambda`$, such as those of 03-ilang-space, convert to rates with respect to this time.
3. **Comparison of clocks:** the comparison of the rates of two clocks, their synchronization, and the conditions under which two clocks agree.

**II. Bodies in time**

4. **Proper time and moving clocks:** the time shown by a clock carried by a body, and how its rate depends on the body's motion in the derived space, including the relation to the maximal speed of 03-ilang-space; the comparison of two such clocks whose bodies move differently between two meetings.
5. **Inertia and internal energy:** whether, and how, the inertia of a body depends on its internal cost (for example the cost of the clock it carries), compared with the inertia derived in 03-ilang-space.
6. **Common maximal speed:** whether the maximal speed is the same for bodies of all types, and the conditions under which it is.

**III. Order**

7. **Events and causal order:** events defined from Ilanguage elements (for example readings or records), an order of events implied by the contracts, and whether this order is sharp or only approximate.
8. **Global order:** whether the order given by $`\lambda`$, and a global "now" at fixed $`\lambda`$, can be detected through readings.

The subproject succeeds when items 1–7 are derived; item 8 may remain open. A proven negative result for an item is a valid outcome: it identifies what Ilanguage 1.b lacks for that item.
