# Ilanguage 1.b — the rules

- **Version:** 1.b
- **Date:** 2026-10-09
- **Citing:** by section (introduction, §1–§9), law (Laws 1–5) and equation number (0.k).

---

This is a description language. It describes systems by means of object-oriented programming patterns.

The language does not say what a system means, and it prescribes no field of application. It fixes only which states and operations can form a valid description.

The language fixes a single formalism: the state is a complex weighting, evolution acts on it linearly, and the contract is an operator defined on the weighting (Section 5). The language does not derive this; it states it. Every further rule is formulated within this frame; the language attaches no meaning to the frame either.

---

## 1. Object and state

An **object type** specifies the set of possible values — in the language's terminology, the **places** — and the operations defined on them.

A type has **instances**. An instance is not the same as a state.

### The state is a weighting

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

### The common phase is not data

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

---

## 2. The operations

Two kinds of thing can happen to a state:

1. **evolution**
2. **reading**

### Evolution

Evolution rotates the weights, preserving their total length.

It is deterministic and reversible.

Its rule is given in Section 4.

### Reading

Reading yields a single value.

Its outcome is random, and it is not reversible.

The probability of the value obtained is given by the square of the length of the weight belonging to it.

After the reading, the weighting goes over to the part compatible with the value obtained: the weights of the incompatible places become zero, the weights of the compatible places stay unchanged relative to each other, and the total length is again one.

An immediately repeated reading therefore gives the same value.

### Law 1 — there is no getter without side effects

**Every reading is also a write.**

A reading does not only give information about the state; it also changes it.

---

## 3. Composition, ownership and view

### Composition

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

### Law 2 — the state is owned by the system, not by the instance

**The state is owned by the system, not by the instance.**

The joint state of several objects is a single weighting of the joint places. If it cannot be decomposed into a product of the states of the parts, the parts have no separate complete state; they have only a view.

### View

A **view** can still be assigned to a part.

The view is a read-only extract computed from the joint state.

It gives the statistics of every local reading that can be performed on the given part, but in general it does not contain enough information to restore the full joint state.

The view is not a separately stored state.

### The witness rule

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

---

## 4. The law of evolution

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

### Law 3 — evolution is termwise and preserves the total length

**Evolution acts with the same operation on every term of the weighting, and it preserves the total length.**

Because it is termwise, evolution is linear; because it preserves the total length, it is — for finitely many places — unitary, and therefore reversible.

Randomness is not part of evolution. Randomness appears only in reading.

---

## 5. The contract

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

### Consistency with Law 3

Since $`C`$ is self-adjoint, the cost is real for every $`\lvert\psi\rangle`$, and the evolution driven by $`C`$ is unitary: it preserves the total length and is reversible. The real cost and the total-length-preserving evolution come from the same definition; the engine of the contract cannot violate Law 3.

### Law 4 — the contract is judge and engine

**The same contract system that determines the cost of the state also drives the evolution of the state.**

The system has no separate behaviour independent of its contracts.

The contract system is itself the program that runs.

---

## 6. Identity

### Law 5 — the instance identifier is not data

Instances of the same type have no internal label.

“Which instance is which” is not part of the state of the system.

Swapping two instances of the same type is therefore not an operation on the system but another description of the same system.

The swap cannot change the statistics of any reading.

### The two families

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

---

## 7. The laws

| # | Law |
| - | --- |
| 1 | There is no getter without side effects: every reading is also a write. |
| 2 | The state is owned by the system, not by the instance. |
| 3 | Evolution is termwise, preserves the total length and is reversible. |
| 4 | The contract is judge and engine: the same $`C`$ evaluates and drives. |
| 5 | The instance identifier is not data. |

---

## 8. Consequence — there is no copy constructor

This is not a separate law.

It follows from the termwise nature of evolution.

### Claim

**No independent copy can be made of an unknown state.**

Suppose there is a copier which copies the pure places when placed next to the empty instance:

```math
\lvert 0\rangle\lvert\text{empty}\rangle \to \lvert 00\rangle ,
\qquad
\lvert 1\rangle\lvert\text{empty}\rangle \to \lvert 11\rangle .
\qquad\text{(0.15)}
```

If the state of the original instance is

```math
a\,\lvert 0\rangle + b\,\lvert 1\rangle ,
\qquad\text{(0.16)}
```

then by Law 3 the result of the copier must be

```math
a\,\lvert 00\rangle + b\,\lvert 11\rangle .
\qquad\text{(0.17)}
```

Two truly independent instances in the same state, by contrast:

```math
\bigl(a\,\lvert 0\rangle + b\,\lvert 1\rangle\bigr)\bigl(a\,\lvert 0\rangle + b\,\lvert 1\rangle\bigr)
= a^2\lvert 00\rangle + ab\,\lvert 01\rangle + ab\,\lvert 10\rangle + b^2\lvert 11\rangle .
\qquad\text{(0.18)}
```

The two results are not the same in general.

Hence there is no allowed evolution that independently copies an arbitrary unknown state.

Producing a known state is still allowed.

That is not copying but the creation of a known state.

---

## 9. The boundary of the language

Beyond this, Ilanguage 1.b does not say what the objects, places, contracts or states represent.

It assigns them no physical or other interpretation in advance.

The task of a description is to specify:

* which object types it uses,
* what places they have,
* which family each type belongs to (invariant or sign-changing under swap),
* what initial state it starts from,
* and what contracts hold between them.

Everything else is part of the given description, not of the language.
