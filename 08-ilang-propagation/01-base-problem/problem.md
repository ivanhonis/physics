# Base problem: 08-ilang-propagation

- **Subproject:** 08-ilang-propagation
- **Created:** 2026-10-24

## Research question

This subproject is the sixth stage of the research programme "Gravity in the description language Ilanguage" (group `gravity`). 03-ilang-space derived a space, 04-ilang-time a time and the kinematics of bodies that carry clocks, 05-ilang-free-fall the behaviour of such a body in a given field, 06-ilang-source the field that bodies make themselves, and 07-ilang-weight the weight, the inertia and the cost of bodies that make the field.

In 07 the field was a set of conserved hopping field objects without mutual terms (the field of 06-ilang-source/04-profile). With the full grip, the own mark of a body and a bond made through the field are weighed like the costs at leading order ((3.14) of 07-ilang-weight/03-weight-of-mark, (4.10)–(4.12) of 07-ilang-weight/04-weight-of-bond); with coupling (a) the rest term is not weighed and the bond is weighed more strongly than the level costs ((3.15), (4.13) there). The inertia of one body is its cost divided by the square of one speed at leading order, but not at the next order ((5.7), (5.8) of 07-ilang-weight/05-inertia-of-mark), and the binding cost of a pair enters its inertia twice ((7.8) of 07-ilang-weight/07-inertia-of-pair-full-grip). The field makes a long-range mark, but its long-range part forms only on $`\lambda\propto\lvert r\rvert^2/t_f`$, on no scale linear in $`\lvert r\rvert`$ ((8.10), (8.14) of 07-ilang-weight/08-field-speed). A weakly pinned field of oscillator cells forms its mark at its front, within a range set by the pinning ((8.15) there), and the speed of the field and the maximal speed of the bodies are independent parameters ((8.17) there).

This stage asks whether one field can weigh every cost, make a long-range mark and form that mark at a finite speed, all in one description, and what the field, the grip and the state must be for that. In such a field it asks whether the inertia of a body with its own mark follows its cost, in particular when the maximal speed of the bodies equals the speed of the field.

**Goal of the programme.** The programme has two questions, in this order.
- *First:* which structure of contracts and states is necessary and sufficient for space, time and gravity to be definable inside Ilanguage 1.b. The language allows many descriptions, and these notions appear only in some of them. A result is therefore a conditional statement: if a description has a stated structure, a stated behaviour follows; and, where a converse is proven, the behaviour is possible only with that structure.
- *Second:* how typical that structure is among the admissible descriptions, and whether anything in the language enforces it. This is asked once in every stage (item 6 below) and is otherwise left to later work.

**Question.** Inside the description language Ilanguage 1.b (quoted under "Physical setting and model"), with the space of 03-ilang-space, the time of 04-ilang-time, the behaviour of a body in a field of 05-ilang-free-fall, the field made by bodies of 06-ilang-source and the weight and inertia of 07-ilang-weight: for bodies that hold on to a common field by pair terms, without pair terms between them,
- how do the weight of a body, the weight of its own mark and the weight of a bond made through the field depend on the operator by which the body holds on to the field (its *grip*), and for which grips, field contracts and field states are the mark and the bond weighed like the rest cost;
- for which field contracts, and for which operators read by the bodies, does the long-range part of the made field form at a finite speed, and how is that speed related to the other speeds of the field and to the maximal speed of the bodies;
- a field whose contract leaves a change applied to all its cells alike free may have no lowest state once sources are present: what does a term on one cell of the field (an *anchor*) change, and can weighing, a long-range mark and its formation at a finite speed be had together in one eigenvector of the total contract;
- can they be had with finitely many places per object, and at which order;
- in such a field, does the inertia of a moving body with its own mark equal its cost divided by the square of one speed, and how does this depend on the ratio of the maximal speed of the bodies to the speed of the field, equality included?

Which grips, field contracts, field states and anchors give this and which do not, under which conditions and to which accuracy, and what cannot be obtained? The items are listed under "Success criteria".

**Working hypothesis.** As in 06-ilang-source and 07-ilang-weight: every body holds on to one common field by pair terms, there are no pair terms between bodies, and bonds between bodies are made through the field. New in this stage: the field may consist of cells, one at each place of a lattice, with pair terms between neighbouring cells, and the contract may contain an anchor. The hypothesis is a starting point, not an assumption. A proof that the properties above cannot be had together is a valid result.

Everything is derived within this subproject. No result is assumed beyond Ilanguage 1.b, the formalization fixed in this file, and the results of 03-ilang-space, 04-ilang-time, 05-ilang-free-fall, 06-ilang-source and 07-ilang-weight that a package quotes verbatim in its question, with a cross edge.

### Methodological constraint: no imported notions

- **M1.** Temporal notions come only from 04-ilang-time and 05-ilang-free-fall: clocks, clock time, the rate of a carried clock, the rate of a clock at a place. They are quoted verbatim in the questions that use them. $`\lambda`$ is the ordering parameter of the evolution and nothing more.
- **M2.** Spatial notions come only from 03-ilang-space: positions, distances, velocities, the maximal speed. They are quoted verbatim in the questions that use them. The places of a field object, and the lattice places of the cells of a field, carry no distance of their own; a package that uses a separation of field places says how it is related to the distances of 03-ilang-space ((4.15) of 06-ilang-source/04-profile, (5.16) of 06-ilang-source/05-made-field-scale).
- **M3.** Mass, weight, charge and source are not imported. Inertia is the one derived in 04-ilang-time, 05-ilang-free-fall, 06-ilang-source and 07-ilang-weight, and weight the one derived in 06-ilang-source and 07-ilang-weight, each quoted where it is used. The weight, the inertia and the source strength of a body with its mark and of a bound pair must be derived from the contracts.
- **M4.** No theory of gravity or of fields may be used as an input: no Newtonian law, no Poisson or wave equation, no Green function of a field theory, no equivalence principle, no relation between mass and energy, no metric or curved spacetime, no redshift formula, no field equation. No theory of elastic media, of ordered magnets or of their waves may be used as an input, and no invariance of a field theory under a change of the observer. No theory that already contains time may be used as an input either. Such statements may appear only as results. Standard facts of linear algebra about the operators of a stated description (for example the inverse of a stated matrix) are mathematics (M5); so are expansions of stated operators, for example in the inverse number of places of a cell.
- **M5.** Standard mathematics may be used freely. Applying a mathematical notion is not an import when the object it is applied to is built explicitly from Ilanguage elements. A question may allow standard mathematics applied to its stated operators; it never allows a physical fact stated without derivation.
- **M6.** Every derived structure must be well defined. It may not depend on the description labels of identical-type instances (Law 5), on the common phase of the state (1.2), or on any other convention of the description. In particular it must be invariant under every replacement of the listed contract terms that leaves the total contract $`C`$ unchanged, place-dependent replacements included: for example, moving a term that is diagonal in the places of a body between the body's own term and its pair term with another object (A5). The cost of a single object is in general not well defined; gaps and differences of costs can be. Weight, inertia and cost are compared only through quantities that the total contract and the state fix: eigenvalues of sectors and their differences, the dependence of a total cost on the places of held bodies, curvatures in a conserved label, and accelerations.
- **M7.** Universality may not be put in. A statement that all bodies, all levels of a clock or all types behave alike, or that weight, inertia and cost agree for all bodies, must be derived, together with the conditions on the contracts under which it holds and the order to which it holds. Equal parameters of different types are conditions, and are named as such.
- **M8.** A description chosen for study (its objects, contracts and starts, for example Model D, a field contract, a coupling or a state of the field) is an assumption of the package, and is named as such. A result for a chosen description shows what the language allows, not what it implies. A statement that the language implies something must be proven for every admissible description of a stated class.
- **M9.** Class, control and start. Every package states the class of descriptions for which each of its results is derived. For each result it gives an admissible description in which the result fails (a control), or proves that there is none in the stated class. A result is derived either for every start of a stated class, or together with its dependence on the start. A distinguished state (an eigenvector, a lowest state, a product state, a branch) is an assumption and is named as such (A11).
- **M10.** The two questions of the programme are kept apart. No package may read a result of the first kind (what a structure gives) as an answer to the second (whether the language enforces the structure).

## Physical setting and model

The model is Ilanguage 1.b. Its text is quoted below verbatim from the reference document of the subproject `00-ilanguage` (Ilanguage 1.b, version 1.b, 2026-10-09), with the reference document's equation tags $`(0.k)`$. Section 8 of the reference document (the absence of a copy constructor) is not quoted here; a package that needs it quotes it in its question. The formal forms that every package uses follow under "Formal form", with tags $`(1.k)`$. They are the same as in 03-ilang-space, 04-ilang-time, 05-ilang-free-fall, 06-ilang-source and 07-ilang-weight, so that results of the six subprojects can be combined in one description.

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

Formalization choices for every package of this subproject, where the text of Ilanguage 1.b leaves room. A1–A15 are the choices of 07-ilang-weight and 06-ilang-source (A1–A13 those of 05-ilang-free-fall, A1–A9 those of 04-ilang-time, A1–A7 those of 03-ilang-space), unchanged.

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
  - A comparison of readings taken at equal $`\lambda`$ uses the order of $`\lambda`$. A package that relies on it says so.
  - A reading may also be represented inside the description, by a contract that writes the read value into a record object that is read later.
  - Each question states which representation it uses.
- **A9. Range of $`\lambda`$.** $`\lambda`$ ranges over $`\mathbb R`$. A package that restricts it, for example to $`\lambda\ge0`$, says so.
- **A10. Fields are objects.** Whatever acts on a body is an object of the description, with its own type, places and contracts, coupled to the body by pair terms (A5). No contract depends on the state (Law 3). A term of the body's own contract that depends on the body's position is an admissible description as well; it is then a property of the body's type, and a package that uses it says so.
- **A11. No preferred state.** The language selects no state of a field or of a medium: there is no rule that picks a lowest state, and no relaxation. A package that needs a field or a medium in a particular state states it, and determines or delimits what happens in other states.
- **A12. Bodies, positions and clocks.** A body is an object recorded by a medium as in 03-ilang-space; its positions, distances and velocities are those defined there. A clock is carried by a body as in 04-ilang-time: the places of the body carry a clock label. The standard body of this subproject is Model D (see "Notation and conventions"). A package may use other bodies, and then defines them.
- **A13. Regimes and orders.** A package states the regime in which it works and the order of every approximation: the strength of the records, the level spacing of the clock, the variation of the field over the body, the size of the plane-wave label, the width of the start. Every statement of universality carries the order to which it holds, and every error term the range on which it holds.
- **A14. Local readings.** A reading of a part is local (A4) unless a package states otherwise and gives the reason. A reading whose classes are not local to one part can fix a common now of parts without a contract between them; no result of this subproject uses one unless its question says so.
- **A15. Held bodies and test bodies.** A body without a motion term, at a fixed position label, is an admissible description (a *held* body); a body whose own change of the field is neglected is a *test body*, and the order of the neglect is stated. Both are choices of the package (M8), not properties of the language.

## Notation and conventions

- The inner product $`\langle\phi\vert\psi\rangle`$ is antilinear in the first argument and linear in the second. $`z^{*}`$ is the complex conjugate, $`X^{\dagger}`$ the adjoint, $`\mathbb 1`$ the identity, $`\lVert\psi\rVert^2=\langle\psi\vert\psi\rangle`$.
- Types $`T`$; place sets $`H_T`$ with $`d_T=\lvert H_T\rvert`$; places $`h,h',k,\dots`$; place basis $`\lvert h\rangle`$.
- Objects $`a,b=1,\dots,N`$. These are description labels, which by Law 5 are not data for identical-type instances. The type of object $`a`$ is $`T(a)`$.
- Joint places $`K,K'`$ and $`\lvert K\rangle`$ as in (1.4). The joint state is written $`\lvert\Psi\rangle=\sum_K\Psi_K\lvert K\rangle`$.
- Swap $`P_{ab}`$, family $`c_T`$, admissible subspace $`\mathcal H_{\rm adm}`$ (1.11).
- Contract system $`C`$, contract terms $`C_\gamma`$ (1.10), cost $`L`$ (1.8), evolution parameter $`\lambda`$, evolved state $`\lvert\Psi(\lambda)\rangle`$ (1.9).
- Part $`A`$ and companion $`\bar A`$. Joint places of $`A`$ are $`h,h'`$, those of $`\bar A`$ are $`r,r'`$. View $`V_A`$ (1.5); branch weights $`a_h`$ and branch states $`\lvert E_h\rangle`$ (1.6).
- Rates with respect to $`\lambda`$ are written $`\mathrm d/\mathrm d\lambda`$. The unit of $`\lambda`$ is a convention of the description, so rates of clocks are compared as ratios. A package that compares clocks at different places states the procedure.
- **Model D** (notation only; it is the body studied in 04-ilang-time, and results about it are quoted in the questions, with cross edges). A body with places $`(x,s,a)`$: a position label $`x`$ on a chain, a branch label $`s\in\{1,2\}`$ and a clock label $`a\in\mathbb Z_N`$, $`N\ge2`$, with the body contract
  ```math
  C_{\rm D}=A+B,\qquad A=\frac\tau2\sum_x\Bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\Bigr)\otimes\mathbb 1_N,\qquad B=\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m\mathbb 1_N+D),
  ```
  where $`\tau>0`$, $`m>0`$, $`\sigma_1,\sigma_3`$ are the Pauli matrices on the branch label, and $`D=\frac{2\pi}{N\lambda_0}\sum_{k=0}^{N-1}k\lvert f_k\rangle\langle f_k\rvert`$ with $`\lvert f_k\rangle=N^{-1/2}\sum_ae^{2\pi ika/N}\lvert a\rangle`$ and $`\lambda_0>0`$ acts on the clock label. $`A`$ is the *motion term*, $`B`$ the *rest and clock term*. The body is recorded by a medium $`c`$ through $`\sum_x\lvert x\rangle\langle x\rvert\otimes K_x`$ with $`K_x=\kappa\,x\,X`$, $`\kappa>0`$, $`X`$ self-adjoint on $`\mathcal H_c`$. A chain on $`\mathbb Z`$ is the limit of long finite chains (A1).
- **Field and lapse-type coupling** (notation only). A field is an object $`f`$ (A10). A *lapse-type* pair term between a body and a field has the form $`\sum_x\lvert x\rangle\langle x\rvert\otimes G\otimes\Phi_x`$, where $`G`$ is a self-adjoint operator on the internal labels of the body (branch and clock) and the $`\Phi_x`$ are self-adjoint operators on $`\mathcal H_f`$; a package may also let the motion term carry such factors. The field is *sharp* in a state $`\varphi`$ if $`\Phi_x\varphi=N(x)\varphi`$ for all $`x`$, with real numbers $`N(x)`$, the *lapse profile*. Which operator $`G`$ is, and what a body sees when the field is or is not sharp, are questions for the packages.
- Equation tags: $`(1.k)`$ in this file, $`(P.k)`$ in package $`P`$ of this subproject, $`(0.k)`$ in the reference document Ilanguage 1.b. A result of 03-ilang-space, 04-ilang-time, 05-ilang-free-fall, 06-ilang-source or 07-ilang-weight is cited with its qualified package name, for example "(17.7) of 03-ilang-space/17-motion", "(5.21) of 04-ilang-time/05-moving-clock", "(17.11) of 05-ilang-free-fall/17-typical-or-forced", "(7.2) of 06-ilang-source/07-dressed-fall" or "(8.15) of 07-ilang-weight/08-field-speed". The five subprojects use the same tag numbers for different results.
- **Source** (notation only). A body $`b`$ coupled to a field $`f`$ by a lapse-type pair term $`\sum_x\lvert x\rangle\langle x\rvert\otimes G\otimes\Phi_x`$ changes the state of $`f`$ unless the state of $`f`$ is sharp. What a body presents to the field (its *source*), whether it is $`\langle G\rangle`$ of some state and whether it is well defined, are questions for the packages. A *held* body is a body without a motion term at a fixed position label; it is a choice of the description (A15). A *test body* is a body whose own change of the field is neglected at a stated order.
- **Common local scale** (notation only). As in 05-ilang-free-fall: at each position the effective on-site block of every level of a body changes from one place to the next by the half-gap of that level times one operator that is the same for all levels ((17.11) of 05-ilang-free-fall/17-typical-or-forced, quoted in the questions that use it). For a field made by a held source and a test body this was studied in 06-ilang-source (item 4 there), and for a body with its own mark and for bonds made through the field in 07-ilang-weight (items 2 and 3 there).
- **Couplings** (notation only). The couplings of 06-ilang-source: (a) the pair term $`\gamma\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m\mathbb 1_N+D)\otimes\Phi_x`$ added to the body contract $`C_{\rm D}`$; (c) the same plus $`\gamma`$ times the motion term with the factor $`\frac12(\Phi_x+\Phi_{x+1})`$ on each bond. A package may also study a *full grip*: a body whose own contract is only the motion term $`A`$, and whose rest and clock term appears only in its pair term with the field, $`\gamma\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m\mathbb 1_N+D)\otimes\Phi_x`$, or the corresponding form of (c). Which of these are different descriptions, and which differ only by a replacement of listed terms (M6), is a question for the packages.
- **Own mark and bond made through the field** (notation only). The *own mark* of a body is the change of the field that the body makes itself, as in 06-ilang-source/06-own-mark. Two bodies are *bound through the field* if there is no pair term between them and their joint contract with the field has a bound level that does not exist without the field.
- **Weight, inertia and cost** (notation only). The *cost* of a body with its mark, or of a bound pair, is given by eigenvalues of the total contract in a sector and their differences (between levels, between configurations, between descriptions with and without a coupling), as in 06-ilang-source/06-own-mark. Its *inertia* is the inverse curvature of such an eigenvalue in a conserved label of joint motion ((6.10) of 06-ilang-source/06-own-mark), or the averaged response of 04-ilang-time; its *weight* is the dependence of such an eigenvalue on the place of the held body or held pair in the field of a distant held source ((7.2) of 06-ilang-source/07-dressed-fall), or the coefficient of the gradient of the made field in the force on body and field. A package states which form it uses and shows that it is well defined (M6).
- **Speed of the field** (notation only). The speed with which a change of the field caused by a source (switched on, moved or shaken) spreads over the places of the field, defined in a package by a stated criterion for the front. The *formation* of the long-range part of the made field, the approach of the made field at a given distance to its static value by a stated criterion, is distinct from the arrival of the first change ((8.10), (8.14) of 07-ilang-weight/08-field-speed); a package that uses a formation speed states its criterion.
- **Field of cells** (notation only). A field made of objects called *cells*, one at each place $`x`$ of a lattice (a ring, a square or a cubic torus), with pair terms between cells at neighbouring places and terms on single cells (A5). The operator $`\Phi_x`$ of a lapse-type pair term is then an operator of the cell at $`x`$. Each cell is an object of its own type, so (1.11) imposes no condition between cells, as in the control of 07-ilang-weight/08-field-speed; a cell may also consist of two objects. Examples that a package may use:
  - *oscillator cells:* each cell has the places $`0,\dots,M-1`$, read as the $`M`$ lowest levels of an oscillator with operators $`q_x,p_x`$, and the contract is the compression $`C_M=\Pi H\Pi`$ of $`H=\sum_x\tfrac12p_x^2+\frac{\kappa_h}2\sum_{\langle xy\rangle}(q_x-q_y)^2+\frac{m_h^2}2\sum_xq_x^2`$, $`\Pi`$ the projector onto the levels below $`M`$ of every cell, with $`\Phi_x=q_x`$ (as in the control (8.15) of 07-ilang-weight/08-field-speed, where $`m_h>0`$);
  - *exchange cells:* objects with $`2S+1`$ places, one at each place of a lattice, with the contract $`J\sum_{\langle xy\rangle}\mathbf S_x\cdot\mathbf S_y`$ between objects at neighbouring places, where $`S^1,S^2,S^3`$ are the matrices of the irreducible representation of dimension $`2S+1`$ of $`\mathfrak{su}(2)`$; a cell is one such object or two neighbouring ones.

  A cell with infinitely many places is not an object of a description (A1). A statement about the uncompressed $`H`$ is a statement about the limit $`M\to\infty`$, and a statement about cells with many places is a statement about the limit $`S\to\infty`$; a package that uses either states the limit and the order of all limits it takes.
- **Grip** (notation only). The operator by which a body holds on to a field: a lapse-type pair term $`\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m\mathbb 1_N+D)\otimes F(\Phi_x)`$ with a real function $`F`$, the *grip function*. The full grip of 07-ilang-weight is the case of a body whose own contract is only the motion term $`A`$, with $`F`$ linear. For a field of cells, $`F(\Phi_x)`$ acts on one cell, so the term is a pair term. For the field of 06-ilang-source/04-profile, where $`\Phi_x`$ is an occupation summed over the field objects, a package that uses an $`F`$ that is not linear shows that its term is a sum of pair terms (A5). Which grips are different descriptions, and which differ only by a replacement of listed terms (M6), is a question for the packages.
- **Anchor** (notation only). A term of the contract that acts on the cell at one place $`h`$ of the field only, for example the pair term of a held object coupled to that cell. It singles out one place of the field. It is a choice of the description (M8, A15), and a package that uses it states it.
- **Long-range mark** (notation only). A place dependence of the total cost of two held sources that falls, at large separation on the cubic torus, as the inverse of the separation, as in (4.7) of 06-ilang-source/04-profile, up to its coefficient. A package that uses a weaker notion, for example "not exponentially bounded" as in 06-ilang-source/08-typical-or-forced, says so.
- **Speeds** (notation only). The maximal speed of a body is that of 03-ilang-space ((17.7) of 03-ilang-space/17-motion; for Model D, (5.11) of 04-ilang-time/05-moving-clock). The speeds of a field (the speed of its front, the largest slope of its spectrum in the plane-wave label, its slope at small labels, the formation speed of its long-range part) are defined in the packages that use them. The places of the field and the positions of the bodies are related by the coupling map ((4.15) of 06-ilang-source/04-profile), so a comparison of a speed of the field with the maximal speed of a body states that map. Equality of the two speeds is a condition on the description (M7), named as such.

## Success criteria

The research question is answered when each item below has a verified package that does one of two things:
- it derives the item, together with the conditions under which it holds and the order to which it holds; or
- it proves that the item cannot be obtained within Ilanguage 1.b with the formalization of this file, and states what is missing.

The items define what a derived structure is measured against. They are not assumptions, and no item may be used as an input.

**I. Weighing and the grip**

1. **Which grips weigh:** for a held body with a grip on a field in a stated eigenvector, near a distant held source: how its weight, the weight of its own mark and the weight of a pair bound through the field depend on the grip function; for which grips, field contracts and field states the mark and the bond are weighed like the rest cost, for every level and both branches, and to which order; for a field of cells and for the field of 06-ilang-source and 07-ilang-weight.

**II. Formation at a finite speed**

2. **Formation of the long-range part:** after a held source is switched on, how the long-range part of the made field forms against the distance; for which field contracts and which operators read by the bodies it forms at a finite speed, and for which it cannot; and how its formation speed is related to the other speeds of the field and to the maximal speed of the bodies.

**III. One field with all three**

3. **A free uniform change and an anchor:** for a field of cells whose contract leaves a change applied to all cells alike free (for oscillator cells, in the limit $`M\to\infty`$): whether the total contract with held sources has a lowest eigenvector; what an anchor changes; and whether weighing as in item 1, a long-range mark, and its formation at a finite speed as in item 2 hold together in the lowest eigenvector of a contract with an anchor, and in which order of the limits (size, distance to the anchor, separation of the bodies).
4. **Finitely many places:** whether item 3 holds for cells with finitely many places (A1), at every number of places of a cell or in the limit of many places, and how the grip that gives item 1 depends on the number of places; with the smallest cells as a control.

**IV. Inertia**

5. **Inertia at a common speed:** in a field for which items 1–3 hold: the inertia of a moving body with its own mark against its cost, for every level and both branches, as a function of the ratio of the maximal speed of the body to the speed of the field, equality included; whether the ratio of weight to inertia is the same for all levels; and, if reached, the same for a pair bound through the field.

**V. How special the structure is**

6. **Typical or forced:** among the grips, field contracts, field states and anchors of a stated class, how special those are that give items 1–3 and 5: whether they are typical, exceptional, or selected by a requirement that can be stated in the terms of the language.

The subproject succeeds when items 1–4 are settled. Items 5 and 6 may remain open. A proven negative result for an item is a valid outcome: it identifies what Ilanguage 1.b lacks for that item.
