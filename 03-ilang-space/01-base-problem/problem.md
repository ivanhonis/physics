# Base problem: 03-ilang-space

- **Subproject:** 03-ilang-space
- **Created:** 2026-10-07

## Research question

This subproject is the first stage of a larger research programme on gravity. Its aim is a space in which gravity can later be studied. Gravity itself is not part of this subproject.

**Question.** Can a space-like structure be derived inside the description language Ilanguage 1.b (rendered under "Physical setting and model") from the language's own elements alone, without importing any spatial notion? Which of the features that a later study of gravity needs follow (distance, dimension, locality, bodies, motion, localized cost, state-dependent geometry; see "Success criteria"; time is handed over to the time project), under which conditions, and which cannot be obtained?

**Working hypothesis.** Space is not a primitive of Ilanguage 1.b. If it appears, it arises from structures the language already contains. The primary route is the view: whole state $\to$ view of a part $\to$ space-like structure. The contract system $C$, the evolution it drives and the families of types are further existing structures; they may be used alone or together with the view.

Everything is derived within this subproject: no result is assumed beyond Ilanguage 1.b and the formalization fixed in this file.

### Methodological constraint: no imported notions

- **M1.** No spatial notion is a primitive. None of the following may be assumed: coordinates, distance, direction, orientation, dimension, neighbourhood, geometry, topology, a given spatial graph or lattice, a background space. Such a notion may appear only as a defined notion, built explicitly from the elements of Ilanguage 1.b.
- **M2.** Time and mass are not imported either. $\lambda$ is the ordering parameter of the evolution and nothing more. A notion of physical time (a clock, a duration, a physical rate) may not be assumed, and this subproject does not derive one (criterion 8). A mass-like notion must be derived, for example from the cost.
- **M3.** No physical model that already contains space (for example a field theory on a given space, or a collapse model) may be used as an input.
- **M4.** "Place" is the Ilanguage word for a possible value of an object. It is not a spatial location. A place may be related to a spatial notion only through an explicit derivation.
- **M5.** Standard mathematics may be used freely. Applying a mathematical notion (a metric, a graph, an order, a notion of dimension) is not an import when the object it is applied to is built explicitly from Ilanguage elements, for example from overlaps of states.
- **M6.** Every derived structure must be well defined. It may not depend on the description labels of identical-type instances (Law 5), on the common phase of the state (1.2), or on any other convention of the description, for example the phase split between $a_h$ and $\lvert E_h\rangle$ in (1.6).

## Physical setting and model

The model is Ilanguage 1.b, a description language. It describes systems with object-oriented programming patterns. The language does not say what a system means and prescribes no field of application; it fixes only which states and operations can form a valid description.

The language fixes a single formalism: the state is a complex weighting, evolution acts on it linearly, and the contract is an operator on the weighting (Section 5). The language states this frame; it does not derive it. Every further rule is formulated within this frame, and the language attaches no meaning to the frame either.

Each rule below is stated in the language's own terms, followed by its formal form. The formalization choices are listed under "Assumptions".

### 1. Object and state

An **object type** $T$ fixes the set of its possible values, in the language's word its **places** $H_T$, and the operations defined on them. A type has **instances** (objects). An instance is not the same as a state.

The state is not "0 or 1" but a weighting of the places:

$$
\lvert\psi\rangle=\sum_{h\in H_T}a_h\lvert h\rangle,\qquad a_h\in\mathbb C,\qquad \sum_h\lvert a_h\rvert^2=1 .
\tag{1.1}
$$

The weights are complex numbers, and their total length is fixed. Formally, $\lvert\psi\rangle$ is a unit vector of $\mathcal H_T=\mathbb C^{H_T}$, and the places $\lvert h\rangle$ form an orthonormal basis of it, the **place basis**.

**The common phase is not data.** Two weightings that differ only by a common complex factor of unit length,

$$
\lvert\psi\rangle\qquad\text{and}\qquad e^{i\varphi}\lvert\psi\rangle ,
\tag{1.2}
$$

say the same for every reading, and therefore mean the same state. The weighting is the representation; the state is its content.

### 2. Operations

Two kinds of thing can happen to a state: **evolution** and **reading**.

**Evolution** rotates the weights while preserving their total length. It is deterministic and reversible. Its rule is given in Section 4.

**Reading** yields a single value. Its outcome is random, and it is not reversible. The probability of the value obtained is the squared length of the weight belonging to it. After the reading, the weighting settles on the part compatible with the value obtained: the incompatible places get weight zero, the compatible places keep their weights relative to each other, and the total length is again one. An immediately repeated reading therefore gives the same value.

Formally, a reading is a partition of the places (for a composite system, of the joint places; Section 3) into classes $S_r$, one for each outcome $r$. With $\Pi_r$ the orthogonal projector onto the span of the places in $S_r$:

$$
p(r)=\bigl\lVert\Pi_r\lvert\Psi\rangle\bigr\rVert^2,
\qquad
\lvert\Psi\rangle\;\longmapsto\;\frac{\Pi_r\lvert\Psi\rangle}{\bigl\lVert\Pi_r\lvert\Psi\rangle\bigr\rVert}.
\tag{1.3}
$$

**Law 1: there is no getter without side effects.** Every reading is also a write: it does not only give information about the state, it changes the state.

### 3. Composition, ownership and view

**Composition.** Composing objects combines their possibilities. If one object has $n$ places and another has $m$, together they have $n\cdot m$ joint places. A joint place is written by juxtaposing the members' places: $\lvert h_1\rangle\lvert h_2\rangle$, briefly $\lvert h_1h_2\rangle$. The state of the composite system is a weighting of these joint places. This is not the same as writing the parts' states side by side: most joint states cannot be factored into a product of separate states of the members.

Formally, a system of objects $1,\dots,N$ with types $T(1),\dots,T(N)$ has the joint space

$$
\mathcal H=\bigotimes_{a=1}^{N}\mathcal H_{T(a)},
\qquad
\lvert K\rangle=\lvert h_1h_2\cdots h_N\rangle=\lvert h_1\rangle\otimes\cdots\otimes\lvert h_N\rangle ,
\tag{1.4}
$$

and the joint places $\lvert K\rangle$ form its orthonormal place basis.

**Law 2: the system owns the state, not the instance.** The joint state of several objects is a single weighting of the joint places. If it cannot be factored into a product of states of the parts, the parts have no complete state of their own, only a view.

**View.** A view can still be assigned to a part. The view is a read-only extract computed from the joint state. It gives the statistics of every local reading that can be performed on that part, but in general it does not contain enough information to restore the full joint state. The view is not a separately stored state.

**The witness rule.** Computing the view is a single rule: the possibilities of the companion must be summed out. Of the cross term between two places of the member, as much remains as the companion is the same in the two branches. If the joint state is

$$
a\lvert0\rangle\lvert E_0\rangle+b\lvert1\rangle\lvert E_1\rangle ,
$$

where $\lvert E_0\rangle$ and $\lvert E_1\rangle$ are the states of the companion in the two branches, then in the member's view the cross term between the two places is multiplied by the overlap $\langle E_1\vert E_0\rangle$. To the extent that the two states of the companion are distinguishable, the companion becomes a witness, and to the same extent the cross term between the two branches decreases. If the two companion states are orthogonal, the cross term vanishes completely.

Formally, a **part** $A$ is a set of objects of the system, its **companion** $\bar A$ is the set of the remaining objects, and $\mathcal H=\mathcal H_A\otimes\mathcal H_{\bar A}$. The view of $A$ is the partial trace over the companion:

$$
V_A(\Psi)=\operatorname{Tr}_{\bar A}\lvert\Psi\rangle\langle\Psi\rvert .
\tag{1.5}
$$

Group the joint state by the joint places $h$ of $A$:

$$
\lvert\Psi\rangle=\sum_h a_h\,\lvert h\rangle\otimes\lvert E_h\rangle,
\qquad
\langle E_h\vert E_h\rangle=1\ \text{ whenever } a_h\neq0 .
\tag{1.6}
$$

The phase split between $a_h$ and $\lvert E_h\rangle$ is a convention. The matrix elements of the view are then

$$
\langle h\vert V_A\vert h'\rangle=a_h\,a_{h'}^{*}\,\langle E_{h'}\vert E_h\rangle .
\tag{1.7}
$$

This is the general form of the witness rule; the two-branch statement above is its special case.

### 4. The law of evolution

If an evolution turns the pure place $\lvert h\rangle$ into $\lvert\Psi_h\rangle$, then it necessarily turns the state $\sum_h a_h\lvert h\rangle$ into $\sum_h a_h\lvert\Psi_h\rangle$. Evolution therefore does not choose its action according to the individual weights; it carries the whole weighting over term by term.

**Law 3: evolution is termwise and preserves the total length.** Evolution acts on every term of the weighting with the same operation and preserves the total length. Because it is termwise, evolution is linear. Because it preserves the total length, it is unitary (for finitely many places) and hence reversible. Randomness is not part of evolution: it appears only in reading.

### 5. The contract

A **contract** can hold between two objects. A contract assigns a real-valued **cost** to the joint state. The total cost of the system is the sum of the costs of its contracts.

Let $C=C^{\dagger}$ be the self-adjoint operator describing the whole contract system. The cost of a state $\lvert\Psi\rangle$ is

$$
L(\Psi)=\langle\Psi\vert C\vert\Psi\rangle .
\tag{1.8}
$$

The contract does not only evaluate the state: the same $C$ also determines the evolution,

$$
i\,\frac{\mathrm d}{\mathrm d\lambda}\lvert\Psi\rangle=C\,\lvert\Psi\rangle,
\qquad\text{hence}\qquad
\lvert\Psi(\lambda)\rangle=e^{-iC\lambda}\lvert\Psi(0)\rangle .
\tag{1.9}
$$

Here $\lambda$ is the ordering parameter of the evolution. The language attaches no further meaning to it.

**Consistency with Law 3.** Since $C$ is self-adjoint, the cost is real for every state, and the evolution driven by $C$ is unitary: it preserves the total length and is reversible. The real cost and the length-preserving evolution come from the same definition; the engine of the contract cannot violate Law 3.

**Law 4: the contract is judge and engine.** The same contract system that determines the cost of the state also drives its evolution. The system has no behaviour independent of its contracts. The contract system is itself the program that runs.

Formally (Assumption A5),

$$
C=\sum_{\gamma}C_\gamma ,
\tag{1.10}
$$

where each contract $\gamma$ holds between two objects $a_\gamma\neq b_\gamma$. Each $C_\gamma$ is a self-adjoint operator on $\mathcal H_{T(a_\gamma)}\otimes\mathcal H_{T(b_\gamma)}$, extended by the identity to the other objects. The cost of a single contract is $\langle\Psi\vert C_\gamma\vert\Psi\rangle=\operatorname{Tr}\bigl(C_\gamma\,V_{\{a_\gamma,b_\gamma\}}(\Psi)\bigr)$.

### 6. Identity

**Law 5: the instance identifier is not data.** Instances of the same type have no internal label. "Which instance is which" is not part of the state of the system. Swapping two instances of the same type is therefore not an operation on the system but another description of the same system. A swap cannot change the statistics of any reading.

**The two families.** Let $P$ be the swap. Since the swap does not change the state, it can change the weighting at most by a common complex factor of unit length: $P\lvert\psi\rangle=c\lvert\psi\rangle$ with $\lvert c\rvert=1$. Since the swap does not change the state, it takes every allowed weighting into a common-phase version of itself. The swap acts termwise, and allowed states can be superposed. If two states had different factors, their sum would no longer go into a common-phase version of itself. Hence $c$ cannot depend on the state within a type. Swapping twice gives back the original description, so $P^2=\mathbb 1$, hence $c^2=1$, and $c$ can only be $+1$ or $-1$.

Objects of the same type therefore belong to one of two families: swap-invariant ($c=+1$) or sign-changing under swap ($c=-1$). The family of a type cannot be derived; the description gives it. Beyond this, the language attaches no meaning to the two families.

Formally (Assumption A6), for two objects $a\neq b$ of the same type $T$, the swap $P_{ab}$ exchanges the $a$-th and $b$-th entries of every joint place:

$$
P_{ab}\lvert\cdots h_a\cdots h_b\cdots\rangle=\lvert\cdots h_b\cdots h_a\cdots\rangle,
\qquad
P_{ab}\lvert\Psi\rangle=c_T\lvert\Psi\rangle,
\qquad
c_T\in\{+1,-1\}.
\tag{1.11}
$$

The second equation holds for every admissible state and every such pair. The admissible states form the subspace $\mathcal H_{\rm adm}\subseteq\mathcal H$.

### 7. The laws

| # | Law |
|---|---|
| 1 | There is no getter without side effects: every reading is also a write. |
| 2 | The system owns the state, not the instance. |
| 3 | Evolution is termwise, preserves the total length, and is reversible. |
| 4 | The contract is judge and engine: the same $C$ evaluates and drives. |
| 5 | The instance identifier is not data. |

### 8. Consequence: there is no copy constructor

This is not a separate law; it follows from the termwise nature of evolution. **An independent copy of an unknown state cannot be made.** Suppose a copier, placed next to an empty instance, copies the pure places: $\lvert0\rangle\lvert\text{empty}\rangle\to\lvert00\rangle$ and $\lvert1\rangle\lvert\text{empty}\rangle\to\lvert11\rangle$. If the original instance is in the state $a\lvert0\rangle+b\lvert1\rangle$, then by Law 3 the copier must produce $a\lvert00\rangle+b\lvert11\rangle$. Two truly independent instances in the same state would instead be in $\bigl(a\lvert0\rangle+b\lvert1\rangle\bigr)\bigl(a\lvert0\rangle+b\lvert1\rangle\bigr)=a^2\lvert00\rangle+ab\lvert01\rangle+ab\lvert10\rangle+b^2\lvert11\rangle$. The two results differ in general, so no allowed evolution copies an arbitrary unknown state independently. Producing a known state is still allowed: that is not copying but the creation of a known state.

### 9. The boundary of the language

Beyond this, Ilanguage 1.b does not say what the objects, places, contracts or states represent, and it assigns them no physical or other interpretation in advance. A description must specify:

- which object types it uses,
- what places they have,
- which family each type belongs to (swap-invariant or sign-changing),
- what initial state it starts from,
- and what contracts hold between the objects.

Everything else belongs to the given description, not to the language.

## Assumptions

Formalization choices for every package of this subproject, where the text of Ilanguage 1.b leaves room:

- **A1. Finiteness.** Every description has finitely many objects, and every type finitely many places. $\mathcal H$ is therefore finite-dimensional and the evolution is unitary. Families of descriptions of growing size and their limits may be studied; a package that takes a limit states it explicitly.
- **A2. Inner product.** $\mathcal H_T$ carries the standard inner product, in which the place basis is orthonormal. The place basis is part of the type, not a choice.
- **A3. Closed system, pure state.** The description lists all objects; nothing exists outside it. The state of the whole system is always a unit vector of $\mathcal H_{\rm adm}$, up to the common phase (1.2). Views are derived objects, not states.
- **A4. Readings.** A reading is a partition of the joint places, acting by (1.3). A local reading on a part $A$ is a reading whose classes depend only on the joint place of $A$.
- **A5. Contracts.** $C$ is a sum of contract terms between pairs of objects, (1.10). A term acting on a single object is included as $D\otimes\mathbb 1$ in a pair term (when the system has at least two objects). The list of contracts and the operators $C_\gamma$ belong to the description, and they do not depend on $\lambda$. Which pair term a single-object term is included in is a convention (M6): contract lists that differ only in this choice are the same description. The cost of a single contract is therefore defined only up to this choice; the total cost (1.8) does not depend on it. (Clarified on 2026-10-08, with the user.)
- **A6. Families.** (1.11) holds for every pair of objects of the same type.
- **A7. Parts and views.** A part is a set of objects, and its view is the partial trace (1.5). Whether, and how, a part consisting of identical-type instances can be specified without labels is a question for the packages (M6), not an assumption.

## Notation and conventions

- The inner product $\langle\phi\vert\psi\rangle$ is antilinear in the first argument and linear in the second. $z^{*}$ is the complex conjugate, $X^{\dagger}$ the adjoint, $\mathbb 1$ the identity, $\lVert\psi\rVert^2=\langle\psi\vert\psi\rangle$.
- Types $T$; place sets $H_T$ with $d_T=\lvert H_T\rvert$; places $h,h',k,\dots$; place basis $\lvert h\rangle$.
- Objects $a,b=1,\dots,N$. These are description labels, which by Law 5 are not data for identical-type instances. The type of object $a$ is $T(a)$.
- Joint places $K,K'$ and $\lvert K\rangle$ as in (1.4). The joint state is written $\lvert\Psi\rangle=\sum_K\Psi_K\lvert K\rangle$.
- Swap $P_{ab}$, family $c_T$, admissible subspace $\mathcal H_{\rm adm}$ (1.11).
- Contract system $C$, contract terms $C_\gamma$ (1.10), cost $L$ (1.8), evolution parameter $\lambda$, evolved state $\lvert\Psi(\lambda)\rangle$ (1.9).
- Part $A$ and companion $\bar A$. Joint places of $A$ are $h,h'$, those of $\bar A$ are $r,r'$. View $V_A$ (1.5); branch weights $a_h$ and branch states $\lvert E_h\rangle$ (1.6).
- Equation tags: $(1.k)$ in this file, $(P.k)$ in package $P$.

## Success criteria

The research question is answered when each item below has a verified package that does one of two things:
- it derives the item, together with the conditions under which it holds; or
- it proves that the item cannot be obtained within Ilanguage 1.b with the formalization of this file, and states what is missing.

The items define what a derived structure is measured against. They are not assumptions, and no item may be used as an input.

**I. Space at fixed $\lambda$**

1. **Points:** the entities that carry the space, defined from Ilanguage elements without labels.
2. **Distance:** a metric on the points.
3. **Neighbourhood and locality:** a notion of near points consistent with the distance, and whether the contract system couples only near points.
4. **Paths:** betweenness, and shortest paths (geodesics) in the derived space.
5. **Dimension:** a notion of dimension and the conditions that fix its value, and the conditions under which families of growing size give a continuum-like space.

**II. Bodies, motion and time**

6. **Body:** an entity that is localized in the derived space, persists under the evolution, and is specified without labels. It has a position, and two bodies have a distance.
7. **Background:** an identification of the points of the spaces obtained at different $\lambda$, and the conditions for a stable background, so that a body has a trajectory.
8. **Time:** handed over to the time project (decision of 2026-10-08, with the user). This subproject derives no clock. Its rates are rates with respect to $\lambda$. Its statements that depend only on the order of $\lambda$ need no clock, for example trajectories as ordered paths, causal order, boundedness of motion, and ratios of rates. If the time project derives a clock $\tau(\lambda)$, the rates convert with $\mathrm d\lambda/\mathrm d\tau$.
9. **Velocity and acceleration:** the rate of change of a body's position with respect to $\lambda$, whether the contract system implies a maximal propagation speed, and velocities relative to that maximal speed.

**III. Connection to gravity** (gravity itself is not part of this subproject)

10. **Localized cost:** the distribution of the cost (1.8) over the derived space, and the cost of a body as the analogue of mass.
11. **State-dependent geometry:** how the distance and the curvature change with the state. This is where later work can relate the geometry to the distribution of cost.
12. **Common space:** how the spaces derived from the views of different parts fit together: when they coincide, and otherwise which rule relates them.

The subproject succeeds when items 1–7 and 9–12 are derived; item 8 is handed over to the time project. A proven negative result for an item is a valid outcome: it identifies what Ilanguage 1.b lacks for that item.
