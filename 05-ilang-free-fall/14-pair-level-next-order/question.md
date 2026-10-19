# Question: 14-pair-level-next-order

- **Subproject:** 05-ilang-free-fall
- **Package:** 14-pair-level-next-order
- **Equation tags:** (14.k)
- **Created:** 2026-10-18

## Goal

Determine the bound level of the pair of 11-bound-pair, in the regime $`\mathsf R`$, one order beyond the leading order of that package: the level near total label $`0`$, its curvature, the expectation values of the rest terms of the parts, and the curvature inertia. No field acts in this package. It prepares the fall of the pair at the next order (criterion 9).

**Setting** (as in 11-bound-pair; quoted under "Inputs").
- Two Model D bodies $`b_1`$, $`b_2`$ of different types and one medium, with $`\langle\chi\vert X\vert\chi\rangle=0`$, so that the operator on the two bodies is $`C^{\rm D}_1+C^{\rm D}_2+U`$. Fixed clock levels $`k_1`$, $`k_2`$, with $`M_i:=M^{(i)}_{k_i}`$; the fibre contract $`H(P)`$ of (11.1), with a phase convention $`\eta`$.
- **Binding:** a diagonal on-site binding, $`U=\lvert0\rangle\langle0\rvert\otimes W_0`$ on the label separation $`r`$, $`W_0=\sum_{s_1,s_2}w_{s_1s_2}\lvert s_1s_2\rangle\langle s_1s_2\rvert`$ with four real numbers; the branch value $`1`$ of $`\sigma^{(i)}_3`$ is the upper branch.
- **Regime $`\mathsf R`$:** $`\tau_i=\epsilon\hat\tau_i`$, $`w_{s_1s_2}=\epsilon^2\hat w_{s_1s_2}`$, with fixed $`\hat\tau_i>0`$, $`\hat w_{s_1s_2}`$, $`M_i>0`$, and $`\epsilon\to0`$; $`\hat w_{11}\neq0`$, both signs. Notation of 11-bound-pair: $`a_i:=\tau_i^2/(4M_i)`$, $`a:=a_1+a_2`$, $`j(P)`$, $`w:=w_{11}`$, $`\varsigma:=\mathrm{sgn}w`$, $`u:=\lvert w\rvert/a`$, $`\Lambda:=1+\varsigma/\sqrt{1+u^2}`$, $`\mathfrak m_i:=M_i/\tau_i^2`$, $`\mathfrak m_b:=1/E_b''(0)`$.
- **The level:** $`E_b(P)`$ is the bound level at the band $`\mathcal B_{++}`$ of (11.12), the only one at a distance of order $`\epsilon^2`$ from that band for small $`\epsilon`$; $`\psi_P`$ its eigenvector.
- **"Next order":** each quantity below is asked through the order $`\epsilon^2`$ beyond the leading term that (11.12)–(11.16) give, at fixed hatted data (hence at a fixed $`u\in(0,\infty)`$): $`E_b(P)-(M_1+M_2)`$, $`E_b''(0)`$ and $`\langle\sigma^{(i)}_3\rangle_0-1`$ through order $`\epsilon^4`$ with a remainder $`O(\epsilon^6)`$; $`\mathfrak m_b`$ through relative order $`\epsilon^2`$. The constants of the remainders may depend on the hatted data; their uniformity in $`u`$ is not asked.

1. **Effective contract at the next order.** Determine the operator on the coefficient $`\psi(r)`$ of $`\lvert11\rangle`$ that replaces (11.11) through order $`\epsilon^4`$, with a remainder $`O(\epsilon^6)`$ in norm, for every $`P`$: every term with its coefficient as an explicit function of $`P`$, $`M_i`$, $`\tau_i`$ and the $`w_{s_1s_2}`$, and its range in $`r`$. State which of the four numbers $`w_{s_1s_2}`$ enter at this order.
2. **Level and derived quantities.** From item 1, for $`P`$ in a neighbourhood of $`0`$:
   - (a) $`E_b(P)`$ through order $`\epsilon^4`$, in closed form or as an explicit finite expression;
   - (b) $`E_{\rm bind}:=E_b(0)-(M_1+M_2)`$, $`E_b''(0)`$ and $`\langle\sigma^{(i)}_3\rangle_0`$ $`(i=1,2)`$ through order $`\epsilon^4`$, the last from (11.5);
   - (c) $`\mathfrak m_b`$ through relative order $`\epsilon^2`$.
3. **Inertia against the binding cost.** Determine whether the relation (11.16), $`\mathfrak m_b=\mathfrak m_1+\mathfrak m_2-4\mathfrak m_1\mathfrak m_2E_{\rm bind}`$, holds at relative order $`\epsilon^2`$ when $`E_{\rm bind}`$ of item 2(b) is inserted. If not, give the leading difference.
4. **Wide pair.** For $`w_{11}<0`$, give the leading term in $`u`$, as $`u\to0`$, of each coefficient of order $`\epsilon^4`$ in item 2(b) and of the relative correction of order $`\epsilon^2`$ in item 2(c), as an ordered limit (first $`\epsilon\to0`$ at fixed $`u`$, then $`u\to0`$ in the coefficient).

## Inputs

From 11-bound-pair@v3 (this subproject). Setting there: as under "Goal"; the results refer to the operator on the two bodies under $`\langle\chi\vert X\vert\chi\rangle=0`$. On the levels $`k_1`$, $`k_2`$ a vector with the label $`P`$ of the joint shift is $`\Psi(x_1,x_2)=e^{iP(\eta x_1+(1-\eta)x_2)}\psi(x_1-x_2)`$ with $`\psi(r)\in\mathbb C^2\otimes\mathbb C^2`$; $`(S\psi)(r):=\psi(r-1)`$; $`A_i`$, $`U`$, $`\sigma^{(i)}_3`$ also denote the fibres of these operators; $`\omega_i(p):=\sqrt{M_i^2+\tau_i^2\sin^2p}`$, $`p_1+p_2=P`$; "leading order in $`\mathsf R`$" is taken at fixed hatted data.

Eq. (11.1) of 11-bound-pair, the fibre contract:

```math
H(P)=\underbrace{\tfrac{i\tau_1}{2}\,\sigma^{(1)}_1\bigl(e^{i\eta P}S^{\dagger}-e^{-i\eta P}S\bigr)}_{A_1}+\underbrace{\tfrac{i\tau_2}{2}\,\sigma^{(2)}_1\bigl(e^{i(1-\eta)P}S-e^{-i(1-\eta)P}S^{\dagger}\bigr)}_{A_2}+M_1\sigma^{(1)}_3+M_2\sigma^{(2)}_3+\underbrace{W(\hat r)}_{U}.
```

Eq. (11.5) of 11-bound-pair, for every simple isolated bound level and every $`P`$ of its interval:

```math
\frac{\partial E_b}{\partial M_i}=\langle\sigma^{(i)}_3\rangle_P,\qquad
\tau_i\frac{\partial E_b}{\partial\tau_i}=\langle A_i\rangle_P,\qquad
\frac{\partial E_b}{\partial\theta}\Big|_{\theta=1}=\langle U\rangle_P\qquad(i=1,2).
```

Step 7 of 11-bound-pair, the reduction at leading order (untagged display there). In $`\mathsf R`$, $`H(P)=H_0+\epsilon H_1+\epsilon^2H_2`$ with $`H_0=M_1\sigma^{(1)}_3+M_2\sigma^{(2)}_3`$, $`\epsilon H_1=A_1+A_2`$, $`\epsilon^2H_2=U`$; $`\Pi`$ is the projector onto the branches $`\lvert11\rangle`$ (all $`r`$); the part of $`H(P)`$ with spectrum near $`M_1+M_2`$ is unitarily equivalent, by a unitary that differs from $`\mathbb 1`$ by $`O(\epsilon)`$, to

```math
H_{\rm eff}(P)=M_1+M_2+\Pi\,U\,\Pi+\Pi\Bigl(\frac{A_1^2}{2M_1}+\frac{A_2^2}{2M_2}\Bigr)\Pi+O(\epsilon^4)\quad\text{in norm}.
```

Eq. (11.11) of 11-bound-pair, on the coefficient $`\psi(r)`$ of $`\lvert11\rangle`$, with $`a_i=\tau_i^2/(4M_i)`$:

```math
(H_{\rm eff}\psi)(r)=\bigl(M_1+M_2+a+w\,\delta_{r,0}\bigr)\psi(r)-\tfrac12\bigl[J\,\psi(r+2)+J^{*}\psi(r-2)\bigr],\qquad J(P):=a_1e^{2i\eta P}+a_2e^{-2i(1-\eta)P}=j(P)\,e^{i\alpha(P)} .
```

Eq. (11.12) of 11-bound-pair, the level for $`\hat w_{11}\neq0`$:

```math
E_b(P)=M_1+M_2+a+\varsigma\sqrt{w^2+j(P)^2}+O(\epsilon^4),\qquad j(P)^2=a_1^2+a_2^2+2a_1a_2\cos2P ,
```

Eq. (11.13) of 11-bound-pair, the eigenvector, with $`\rho=-\varsigma\bigl(\sqrt{w^2+j^2}-\lvert w\rvert\bigr)/j`$:

```math
\psi_P(r)=\mathcal N_P\,e^{-i\alpha(P)\,r/2}\,\rho(P)^{\lvert r\rvert/2}\,\lvert11\rangle\ \ (r\ \text{even}),\qquad \psi_P(r)=0\ \ (r\ \text{odd}),\qquad \mathcal N_P^2=\frac{\lvert w\rvert}{\sqrt{w^2+j^2}},\qquad\text{up to } O(\epsilon).
```

Eq. (11.14) of 11-bound-pair, each up to $`O(\epsilon^4)`$:

```math
E_{\rm bind}=a+\varsigma\sqrt{w^2+a^2},\quad E_b''(0)=-\varsigma\frac{4a_1a_2}{\sqrt{w^2+a^2}},\quad \langle\sigma^{(i)}_3\rangle_0=1-\frac{a_i}{M_i}\Lambda,\quad \langle A_i\rangle_0=2a_i\Lambda,\quad \langle U\rangle_0=\varsigma\frac{w^2}{\sqrt{w^2+a^2}},\qquad \Lambda=1+\frac{\varsigma\,a}{\sqrt{w^2+a^2}} .
```

Eq. (11.16) of 11-bound-pair, at leading order in $`\mathsf R`$ (relative remainder $`O(\epsilon^2)`$), for both signs of $`w_{11}`$:

```math
\mathfrak m_b=-\varsigma\,(\mathfrak m_1+\mathfrak m_2)\sqrt{1+u^2}=\mathfrak m_1+\mathfrak m_2-4\,\mathfrak m_1\mathfrak m_2\,E_{\rm bind} .
```

Statements of Step 7 of 11-bound-pair: the odd orders of $`E_b`$ in $`\epsilon`$ vanish ($`\sigma^{(1)}_3\sigma^{(2)}_3`$ maps $`H`$ at $`\epsilon`$ to $`H`$ at $`-\epsilon`$); $`w_{22}`$ enters $`E_b`$ at order $`\epsilon^6`$, and $`w_{12}`$, $`w_{21}`$ do not enter this level at any order; the $`O(\epsilon)`$ part of the eigenvector is $`\bigl(\frac{A_1}{2M_1}+\frac{A_2}{2M_2}\bigr)\psi_P`$.

## Assumptions

- The setting under "Goal": the two bodies, the diagonal on-site binding, the regime $`\mathsf R`$ and the bound level are assumptions of this package (M8, M9); equal parameters of the two types are never assumed (M7).
- Standard degenerate perturbation theory for an isolated group of eigenvalues (Schrieffer–Wolff) to fourth order, and standard perturbation theory for an isolated eigenvalue, may be used with their conditions stated.

## Scope

- **Class.** Every diagonal on-site binding with $`\hat w_{11}\neq0`$ (both signs), all hatted data, the level (11.12), at fixed hatted data; item 1 for every $`P`$, items 2–3 for $`P`$ near $`0`$, item 4 for $`w_{11}<0`$.
- **Control.** Item 3: the relation (11.16) with the exact binding cost is the member whose failure or validity is to be determined.
- Out of scope: the tight-pair limit; joint limits in $`\epsilon`$ and $`u`$; any field; the clocks of the parts beyond $`\langle\sigma^{(i)}_3\rangle_0`$; other bands and other bound levels; bindings other than diagonal on-site ones.

## Depth

- Item 1: derive (needed by item 2).
- Item 2: derive (needed by the fall of the pair at the next order, criterion 9).
- Item 3: short argument (needed by the comparison of weight and inertia in the fall at the next order, criterion 9).
- Item 4: short argument (the fall at the next order compares the wide pair with its parts).

## Expected result

- Item 1: an operator on $`\psi(r)`$ with explicit coefficients, and a list of the $`w_{s_1s_2}`$ that enter.
- Item 2: a closed form or explicit finite expression; four coefficients of order $`\epsilon^4`$; a relative correction.
- Item 3: a yes/no answer, with the leading difference if no.
- Item 4: leading terms in $`u`$.

Give every main result a tag $`(14.k)`$.

Consistency checks, at most three: for example no binding in the ordered limit $`u\to0`$, the scaling relation (11.6) on the result, and equal data of the two bodies.

## Code

Required: check: a numerical diagonalization of $`H(P)`$ of (11.1) on a finite range of $`r`$, for a diagonal on-site binding, at no fewer than three values of $`\epsilon`$ for each of at least three hatted data sets (one with $`\tau_1\neq\tau_2`$ and $`M_1\neq M_2`$; both signs of $`w_{11}`$; one with $`u\le0.3`$). Compare $`E_{\rm bind}`$, $`E_b''(0)`$ (by finite differences in $`P`$) and $`\langle\sigma^{(i)}_3\rangle_0`$ with item 2(b): report the deviation from the leading forms (11.14) and from the next-order forms, and its scaling with $`\epsilon`$. State the range of $`r`$, the step of the finite differences, and how convergence was checked.
