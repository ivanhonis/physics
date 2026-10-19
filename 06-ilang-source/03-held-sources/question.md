# Question: 03-held-sources

- **Subproject:** 06-ilang-source
- **Package:** 03-held-sources
- **Equation tags:** (3.k)
- **Created:** 2026-10-19

## Goal

For one and two held bodies coupled to one field object, determine how the field and its cost change, the mutual cost of two sources and its sign, as functions of the field contract and of the state of the field, and which part of the sign is a condition on the state. This is item 2 of the base problem.

**Setting.**
- **Objects.** A field object $`f`$ of any finite type, with a self-adjoint contract $`C_f`$ on $`\mathcal H_f`$ and self-adjoint operators $`\Phi_x`$ on $`\mathcal H_f`$, one for each $`x`$ of a finite set $`X_f`$ of field places. Two held bodies $`b_1`$, $`b_2`$ (A15) of any types: body $`b_i`$ is at a fixed place $`x_i\in X_f`$, $`x_1\neq x_2`$, and is coupled to $`f`$ by the pair term $`G_i\otimes\Phi_{x_i}`$ with a self-adjoint operator $`G_i`$ on $`\mathcal H_{b_i}`$. The bodies have no other contracts. Each object is the only instance of its type. Every element of the setting is an assumption of the package (M8).
- **States.** The bodies start in eigenvectors of $`G_i`$ with eigenvalues $`g_i`$; the field starts in a state $`\varphi`$. The states of $`f`$ studied are named in each item; the language selects none (A11).
- **Field cost with sources.** $`E(\varphi;g_1,g_2)`$ denotes the cost (1.8) of the field part in the state named, and, for an eigenvector $`\varphi_n`$ of $`C_f`$ with eigenvalue $`e_n`$, $`E_n(g_1,g_2)`$ the eigenvalue of the field contract with the sources that is continuously connected to $`e_n`$.
- **Mutual cost.** The part of $`E_n(g_1,g_2)`$ that depends on both $`g_1`$ and $`g_2`$; its *sign* for $`g_1g_2>0`$ decides whether two like sources have a lower cost close together or far apart.

1. **Reduction.** Determine the evolution of the field under the full contract for the starts of the setting, and the operator by which it evolves; state for which starts it is exact.
2. **One eigenvector.** For a non-degenerate eigenvector $`\varphi_n`$ of $`C_f`$: determine $`E_n(g_1,g_2)`$ through second order in $`(g_1,g_2)`$, with the self terms of each source and the mutual term written through a response function of $`\varphi_n`$; give the response function and state its symmetry. Determine how the result changes for a degenerate eigenvector.
3. **All states.** Determine the sum of the mutual term over all eigenvectors of $`C_f`$, and over the eigenvectors in an invariant subspace of $`C_f`$ and of all $`\Phi_x`$. Determine the relation between the mutual terms of the eigenvectors at the two ends of the spectrum when a unitary maps $`C_f`$ to $`-C_f`$ and each $`\Phi_x`$ to $`\pm\Phi_x`$. Determine what can be said about the sign of the mutual term for mixtures of eigenvectors with weights that decrease (or increase) with $`e_n`$.
4. **Sharp and responding.** Determine the response function in a state in which all $`\Phi_x`$ are sharp (A10, base problem notation), and the relation between the mutual term of two sources and the self term of one; state whether a field state can be sharp at the places of the bodies and respond to them at the same time.
5. **Sign as a condition on the state.** From items 2–4: state which part of the sign of the mutual term is fixed by $`C_f`$ and the $`\Phi_x`$ alone, and which part is a condition on the state of the field. Give, for one explicit small field (for example a field with three places), a state in which like sources have a lower cost close together and a state in which they have a higher one.

## Inputs

None. The package builds on the base problem only.

## Assumptions

- The setting under "Goal". Held bodies, the pair terms $`G_i\otimes\Phi_{x_i}`$ and every state of the field are assumptions of the package (M8, M9).
- Standard perturbation theory for an isolated eigenvalue of a self-adjoint operator, and standard facts on spectra of finite self-adjoint matrices, may be used with their conditions stated.

## Scope

- **Class.** Every finite field type, every self-adjoint $`C_f`$ and $`\Phi_x`$, every pair of held bodies with $`x_1\neq x_2`$; items 2–4 for every eigenvector or mixture named there.
- **Control.** Item 5 asks for a state with each sign; item 4 for a state that does not respond.
- Out of scope: moving bodies, what a moving body presents (02-what-a-body-presents), the dependence on the distance for a particular field (04-profile), the fall of a test body, orders above the second except in item 1 and item 4.

## Depth

- Item 1: short argument (needed by items 2–5).
- Item 2: derive (needed by 04-profile and item 4 of the base problem).
- Item 3: derive (needed by item 5 and item 8 of the base problem).
- Item 4: short argument (needed by item 5 of the base problem, the body's own mark).
- Item 5: short argument (the answer to item 2 of the base problem on the sign).

## Expected result

- Item 1: an operator on $`\mathcal H_f`$ and a condition.
- Item 2: an expansion with a response function; its change for a degenerate eigenvector.
- Item 3: a sum rule; a relation between two eigenvectors; a statement on the sign for ordered mixtures.
- Item 4: a value of the response; an inequality or identity between mutual and self terms; a yes/no answer.
- Item 5: a statement separating the two parts; two explicit states.

Give every main result a tag $`(3.k)`$.

Consistency checks, at most three: for example $`g_2=0`$, a field with two places, and a field whose $`\Phi_x`$ commute with $`C_f`$.

## Code

None.
