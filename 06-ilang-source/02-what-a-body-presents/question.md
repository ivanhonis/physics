# Question: 02-what-a-body-presents

- **Subproject:** 06-ilang-source
- **Package:** 02-what-a-body-presents
- **Equation tags:** (2.k)
- **Created:** 2026-10-19

## Goal

Determine what a body presents to a field object that it is coupled to: the term through which the state of the body enters the evolution of the field, for a body at rest, a moving body, a body on one clock level and a bound pair, for two kinds of coupling; and which of these quantities are well defined. This is item 1 of the base problem.

**Setting.**
- **Objects.** A body $`b`$ of Model D type (base problem, "Notation and conventions"), a recording medium $`c`$ with $`K_x=\kappa\,x\,X`$, and a field object $`f`$ of any finite type with a self-adjoint contract $`C_f`$ and self-adjoint operators $`\Phi_x`$ on $`\mathcal H_f`$, one for each position label $`x`$ of the body. Each object is the only instance of its type.
- **Two couplings** (each an assumption of the package, M8), with a real coupling constant $`\gamma`$:
  - (a) on the rest and clock term: $`C_{bf}^{(a)}=\gamma\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m\mathbb 1_N+D)\otimes\Phi_x`$;
  - (c) on the whole body contract: $`C_{bf}^{(c)}=C_{bf}^{(a)}+\gamma\,\frac\tau2\sum_x\bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\bigr)\otimes\mathbb 1_N\otimes\tfrac12(\Phi_x+\Phi_{x+1})`$.
- **Total contract.** $`C=C_{\rm D}+C_{bc}+C_f+C_{bf}`$, with $`C_{bc}=\sum_x\lvert x\rangle\langle x\rvert\otimes K_x`$.
- **Source.** For a state $`\Psi`$ of the whole system, the *source field* of the body is the family of numbers or operators through which the body enters the evolution of the view of $`f`$ at first order in $`\gamma`$; the package determines it and states the remainder.
- **Bound pair.** Two Model D bodies $`b_1`$, $`b_2`$ of different types, each coupled to $`f`$ by (a) or (c) with its own $`\gamma_i`$, and a binding pair term $`U`$ between them that is diagonal in both position labels, as in 05-ilang-free-fall (no factor of the field on $`U`$).

1. **The source at first order.** For a product start $`\Psi_b\otimes\chi\otimes\varphi`$ and for each coupling: determine the generator of the view of $`f`$ to first order in $`\gamma`$ at fixed $`\lambda`$, and the source field (its value at each field operator $`\Phi_x`$), with the remainder; state for which starts the first-order generator is a contract of $`f`$ alone (independent of $`\lambda`$).
2. **Evaluation.** For a branch start of Model D (plane-wave label $`p`$, branch $`\sigma`$, clock level $`k`$, quoted under "Inputs") at zeroth order in the coupling and in the records: determine the total source $`\sum_x`$ of the source field and its dependence on $`p`$, $`\sigma`$ and $`k`$, for (a) and for (c); give its relation to the cost of the start and to the half-gap $`M_k`$.
3. **Bound pair.** For a bound pair in an eigenvector of its pair contract on fixed clock levels: determine the total source, as a combination of expectation values of the terms of the pair contract, for (a) and for (c), and its relation to the cost of the pair and to the sum of the sources of the parts; state what the binding term contributes.
4. **Well-definedness (M6).** Determine which replacements of the listed terms leave $`C`$ unchanged when a body–field pair term is present (including moving a constant or an operator of one object between the body's own term, the medium term and the field term), and which of the following are well defined: the source field; its total; its value relative to that of another body; the zero of the body operator of the coupling (a constant added to $`\sigma_3\otimes(m\mathbb 1_N+D)`$ in (a)).

## Inputs

From 05-moving-clock@v3 of 04-ilang-time. Setting there: one Model D body with the contract $`C_b=C_{\rm D}`$ of the base problem, the records $`K_x=\kappa xX`$ and the start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`d_k:=\frac{2\pi k}{N\lambda_0}`$; the plane waves $`\lvert p\rangle=\sum_xe^{ipx}\lvert x\rangle`$, $`p\in(-\pi,\pi]`$.

Eq. (5.5) of 04-ilang-time/05-moving-clock:

```math
C_b\bigl(\lvert p\rangle\otimes\beta\otimes\lvert f_k\rangle\bigr)=\lvert p\rangle\otimes C_k(p)\beta\otimes\lvert f_k\rangle,\qquad C_k(p):=-\tau\sin p\,\sigma_1+\mu_k\sigma_3,\qquad\mu_k:=m+d_k .
```

Eq. (5.6) of 04-ilang-time/05-moving-clock, the eigenvalues $`\pm\omega_k(p)`$ and the real eigenvectors $`\lvert p\rangle\otimes\beta_{k,\pm}(p)\otimes\lvert f_k\rangle`$ of $`C_b`$:

```math
\omega_k(p)=\sqrt{\mu_k^2+\tau^2\sin^2p},\quad
\beta_{k,+}=\begin{pmatrix}\cos\frac{\theta_k}2\\ \sin\frac{\theta_k}2\end{pmatrix},\quad
\beta_{k,-}=\begin{pmatrix}-\sin\frac{\theta_k}2\\ \cos\frac{\theta_k}2\end{pmatrix},\quad
\tan\theta_k(p)=-\frac{\tau\sin p}{\mu_k},\ \ \lvert\theta_k\rvert<\frac\pi2 .
```

## Assumptions

- The setting under "Goal". The body, the two couplings, the binding and every start are assumptions of the package (M8, M9); the field object is of any finite type.
- Standard first-order perturbation theory in a term of the contract, at fixed $`\lambda`$, may be used with its conditions stated.

## Scope

- **Class.** Item 1: every finite field type, every $`C_f`$, $`\Phi_x`$, every product start. Item 2: branch starts of Model D. Item 3: every binding diagonal in both positions, every eigenvector of the pair contract on fixed levels. Item 4: the whole setting.
- **Control.** For item 1, a start for which the first-order generator of $`f`$ depends on $`\lambda`$; for item 3, a pair for which the total source differs from the sum of what its parts present when free.
- Out of scope: the response of the field (03-held-sources), its profile (04-profile), second order in $`\gamma`$, the fall of the body.

## Depth

- Item 1: derive (needed by items 2–4 and by every later package of this subproject).
- Item 2: short argument (needed by item 4 of the base problem, the made field as a scale).
- Item 3: short argument (needed by item 6 of the base problem, bonds through the field).
- Item 4: derive (needed by items 1 and 8 of the base problem).

## Expected result

- Item 1: a generator with a remainder; a condition on the start.
- Item 2: a closed form for each coupling, with its dependence on $`p`$, $`\sigma`$, $`k`$.
- Item 3: an expression in expectation values for each coupling; a statement on the binding term.
- Item 4: a list of replacements and yes/no answers.

Give every main result a tag $`(2.k)`$.

Consistency checks, at most three: for example $`\gamma\to0`$, $`\tau\to0`$ (a body without motion), and the sum over both branches.

## Code

None.
