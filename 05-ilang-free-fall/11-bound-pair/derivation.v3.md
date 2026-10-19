# Bound pair of two Model D bodies: bound level, curvature, cost and clock rates

- **Subproject:** 05-ilang-free-fall
- **Package:** 11-bound-pair
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-11

## Changes from previous version

Changes against v2, caused by the issues I1–I4 of `verification.r2.md` (external round 2). Everything that these issues do not touch is kept word for word: the steps, the tags (11.1)–(11.26), the displays (three are restated with a condition), the three consistency checks (one parenthesis is added to check 2).

- **I1 (Step 2, Result item 1).** Three questions on the expression $`E_b(P)-(M_1+M_2)`$ are kept apart: (i) formed from the listed terms: no; (ii) formed from $`C_{\rm bod}`$, under every replacement (11.3) at fixed $`C`$: yes, and it is then (11.22); (iii) a constant added to $`C`$: not a replacement, it changes the expression (ii) and not (11.22).
  - **(11.4) restated**: the row of this expression. From $`C_{\rm bod}`$: "yes" (v2: "yes as $`E_{\rm bind}(P)`$"); from the listed terms: "no" (v2 added "the literal expression is not well defined", without saying from which quantities).
  - **(11.22) restated**: the equality $`e_{++}(0)=M_1+M_2`$ carries its condition (the $`C`$ of the question).
- **I2 (Setup, new Step 1a, Step 6, Result, Open issues).** The claim of v2 that every bound level lies outside the bands is withdrawn: it does not follow from the definition, and it is false for a member that is given. New (11.27): a band is a single point iff the data are equal and $`P\in\{0,\pi\}`$. So a bound level lies outside the bands, with finite multiplicity, at every $`P`$ of its interval except possibly such a point with the value $`0`$; new (11.28) bounds the level near such a point. Steps 3–5a are unchanged; their class is now stated.
- **I3 (Steps 8, 9, 10, Result).** Every wide-pair and tight-pair form is stated as an ordered limit: first $`\epsilon\to0`$ at fixed $`u`$, then $`u\to0`$ or $`u\to\infty`$ in the leading coefficient. New (11.30): sufficient inequalities for a joint range, for the level $`E_b(P)`$ only. For the other quantities no joint limit is derived.
- **I4 (Steps 4, 5a, 10, Result).** The class $`\mathcal G(\mathcal P_0)`$ of packets is defined. **(11.8) restated** with this class and a bound on its remainder. New (11.29): the statement that holds for every normalized $`g`$ (expectation values of the velocity operators). Steps 5a and 10 name their class of $`g`$.
- **Tags.** (11.1)–(11.26) are kept. New: (11.27)–(11.30). Withdrawn: none.
- **Code.** `code/v3/check_bound_pair.py` is the script of v2 with the output folder of v3 (Parts 1 and 2, same log) and a new Part 3 for I2 and I3.

## Response to verification

- **I1: Accepted and fixed** in Step 2: the row of (11.4), the bullet "$`E_b(P)-(M_1+M_2)`$" with the three questions (i)–(iii), and (11.22) with its text; Result item 1 follows.
- **I2: Accepted and fixed** in the Setup ("Multiplicity and location") and in the new Step 1a: (11.27), (11.28), a member with a flat value, and the list of what is proven where. The claim of v2 is not proven; it is withdrawn. What remains open is named in "Open issues".
- **I3: Accepted and fixed** in Step 8 ("Order of the limits", "Joint range", (11.30)), with the order of the limits stated after (11.16), (11.17), (11.20) and (11.26) and in the Result.
- **I4: Accepted and fixed** in Step 4 (the class $`\mathcal G(\mathcal P_0)`$, (11.29), the restated (11.8)), in Step 5a and in Step 10(a).

## Setup and assumptions

- **Setting.** As in `question.md`: two Model D bodies $`b_1`$, $`b_2`$ of different types, one medium $`c`$, $`C=C_{\rm pair}+C_{\rm rec}`$, $`C_{\rm pair}=C^{\rm D}_1+C^{\rm D}_2+U`$, the binding $`U`$ of the class $`\mathcal W`$, fixed clock levels $`k_1,k_2`$ with $`M_i=M^{(i)}_{k_i}`$, the fibre contract $`H(P)`$, a bound level $`E_b(P)`$ with the eigenvector $`\psi_P`$, the curvature inertia $`\mathfrak m_b=1/E_b''(0)`$, $`\mathfrak m_i=M_i/\tau_i^2`$, and the regime $`\mathsf R`$ ($`\tau_i=\epsilon\hat\tau_i`$, $`w_{s_1s_2}=\epsilon^2\hat w_{s_1s_2}`$, $`\epsilon\to0`$). The bodies, the class $`\mathcal W`$, the diagonal on-site binding, $`\mathsf R`$ and every start are assumptions (M8, M9); a bound level is a distinguished set of states (A11). No field acts.
- **Operator on the two bodies.** The listed $`C_{\rm pair}`$ is a convention of the listing (A5, M6). Every result below refers to the operator $`C_{\rm bod}`$ of (11.21) in Step 2, which is defined by the total contract $`C`$ and the start $`\chi`$ of the medium alone. Assumption (M8): $`\langle\chi\vert X\vert\chi\rangle=0`$. Under it $`C_{\rm bod}=C^{\rm D}_1+C^{\rm D}_2+U`$, and from here on $`C_{\rm pair}`$, $`H(P)`$, $`E_b`$, $`\psi_P`$, $`\tau_i`$, $`M_i`$ and $`W`$ denote this operator, its fibres and its data.
- **Inputs used.**
  - (5.5), (5.6) of 04-ilang-time/05-moving-clock: on a plane wave $`\lvert p\rangle`$ and a level $`k`$ the Model D contract acts as $`-\tau\sin p\,\sigma_1+\mu_k\sigma_3`$, with the eigenvalues $`\pm\omega_k(p)`$, $`\omega_k=\sqrt{\mu_k^2+\tau^2\sin^2p}`$. (5.11) there: $`v_{\max}=\tau\kappa\sigma_X`$. (5.1), (5.21) there: $`P_N(a;\vartheta)`$ and $`q(a;\lambda)=P_N(a;\Gamma(p_0)\lambda/\lambda_0)+\mathcal R`$, with $`\Gamma(0)=1`$.
  - (6.7), (6.20) of 04-ilang-time/06-inertia-internal-energy: the gap $`2M_k`$, the upper branch is the eigenvector $`\lvert1\rangle`$ of $`\sigma_3`$, and $`1/\omega_k''(0)=M_k/\tau^2=I^{\rm lab}_k`$.
  - (17.15) of 03-ilang-space/17-motion and (16.11) of 03-ilang-space/16-common-space: the position of either body is $`\kappa\,\bar m_i\,e`$ with $`\bar m_i`$ the mean position label, and $`r=x_1-x_2`$ is the separation of corresponding points.
  - (21.2), (21.12), (21.15), (21.16) of 03-ilang-space/21-composite-body, as quoted in the question.
- **Notation.** $`\omega_i(p):=\sqrt{M_i^2+\tau_i^2\sin^2p}`$, $`\Omega_i:=\sqrt{M_i^2+\tau_i^2}`$. For item 3: $`a_i:=\tau_i^2/(4M_i)=1/(4\mathfrak m_i)`$, $`a:=a_1+a_2`$, $`j(P):=\sqrt{a_1^2+a_2^2+2a_1a_2\cos2P}`$ (so $`j(0)=a`$), $`w:=w_{11}`$, $`\varsigma:=\mathrm{sgn}w`$, $`u:=\lvert w\rvert/a=\lvert\hat w_{11}\rvert/\hat a`$ and $`\Lambda:=1+\varsigma/\sqrt{1+u^2}\in(0,2)`$. In $`\mathsf R`$ the quantities $`a_i,a,j,w`$ are of order $`\epsilon^2`$ and $`u,\Lambda`$ of order one.
- **Standard facts used.** Weyl's theorem (a finite-range change does not change the bands); exponential decay of the eigenvector of an isolated eigenvalue of a finite-range operator; analytic perturbation theory of an isolated eigenvalue (first and second order); degenerate perturbation theory for an isolated group of eigenvalues (Schrieffer–Wolff), valid for $`\tau_1+\tau_2+\max\lvert w_{s_1s_2}\rvert\ll2\min(M_1,M_2)`$; Rellich's theorem (analytic branches of an isolated eigenvalue of finite multiplicity in one real parameter) with degenerate perturbation theory to second order. Added in v3: an isolated point of the spectrum outside the essential spectrum is an eigenvalue of finite multiplicity; a simple eigenvalue at the distance $`g`$ from the rest of the spectrum stays simple, and moves by at most $`\varrho`$, under a self-adjoint change of norm $`\varrho<g/2`$.
- **Multiplicity and location.** By Step 1a, at every $`P\in\mathcal P`$ a bound level lies outside the bands (11.2), which are the essential spectrum of $`H(P)`$, and has a finite multiplicity $`n`$, with one possible exception: for equal data ($`M_1=M_2`$, $`\tau_1=\tau_2`$) at $`P\in\{0,\pi\}`$ the value $`0`$, the point $`\mathcal B_{\pm\mp}=\{0\}`$ of infinite multiplicity (a *flat value*). The definition of the question does not exclude this value, and a member with it exists (Step 1a). Steps 3–5a are derived at the points of $`\mathcal P`$ where the level lies outside the bands; Step 1a says what holds at a flat value. Steps 3–5 treat a simple level ($`n=1`$), which is the case in Step 7. Step 5a treats $`n\ge2`$.
- **Status words.** *Exact*: an identity for every member of the stated class. *Leading order in $`\mathsf R`$*: the stated remainder is neglected, at fixed hatted data. *Ordered limit*: first $`\epsilon\to0`$ at fixed hatted data, then a limit in $`u`$ of the leading coefficient (Step 8).

## Derivation

### Step 1. Fibre contract and two-body bands (item 1a)

On the levels $`k_1,k_2`$ a vector with the label $`P`$ of the joint shift is $`\Psi(x_1,x_2)=e^{iP(\eta x_1+(1-\eta)x_2)}\psi(x_1-x_2)`$ with $`\psi(r)\in\mathbb C^2\otimes\mathbb C^2`$. The real number $`\eta`$ is the phase convention. Changing it is the unitary map $`\psi(r)\to e^{i(\eta-\eta')Pr}\psi(r)`$, so the spectrum and every $`\langle O\rangle_P`$ below are independent of it. With $`(A_i\Psi)(x_i)=\frac{\tau_i}2\bigl[-i\sigma_1\Psi(x_i-1)+i\sigma_1\Psi(x_i+1)\bigr]`$ and $`(S\psi)(r):=\psi(r-1)`$:

```math
H(P)=\underbrace{\tfrac{i\tau_1}{2}\,\sigma^{(1)}_1\bigl(e^{i\eta P}S^{\dagger}-e^{-i\eta P}S\bigr)}_{A_1}+\underbrace{\tfrac{i\tau_2}{2}\,\sigma^{(2)}_1\bigl(e^{i(1-\eta)P}S-e^{-i(1-\eta)P}S^{\dagger}\bigr)}_{A_2}+M_1\sigma^{(1)}_3+M_2\sigma^{(2)}_3+\underbrace{W(\hat r)}_{U}.
\qquad\text{(11.1)}
```

$`A_i`$, $`U`$, $`\sigma^{(i)}_3`$ denote from here on these fibres. On $`\psi(r)=e^{iqr}\beta`$ the part without $`W`$, $`H^0(P)`$, acts as $`h_P(q)=-\tau_1\sin p_1\,\sigma^{(1)}_1-\tau_2\sin p_2\,\sigma^{(2)}_1+M_1\sigma^{(1)}_3+M_2\sigma^{(2)}_3`$ with $`p_1=\eta P+q`$, $`p_2=(1-\eta)P-q`$, $`p_1+p_2=P`$: each body as in (5.5).

For $`\lvert r\rvert>R`$, $`H(P)`$ acts as $`H^0(P)`$, so an eigenvector that is bounded and not square-summable is there a combination of plane waves with real $`q`$. By (5.6) their eigenvalues are $`\sigma_1\omega_1(p_1)+\sigma_2\omega_2(p_2)`$, $`\sigma_i=\pm`$. By Weyl's theorem this set is the same for every $`W\in\mathcal W`$. With $`v=\sin^2q\in[0,1]`$ at $`P=0`$ and $`f(v):=\sqrt{M_1^2+\tau_1^2v}-\sqrt{M_2^2+\tau_2^2v}`$:

```math
\mathcal B_{\sigma_1\sigma_2}(P)=\bigl\{\sigma_1\omega_1(p_1)+\sigma_2\omega_2(P-p_1)\bigr\}_{p_1\in(-\pi,\pi]},\qquad \mathcal B_{++}(0)=[\,M_1+M_2,\ \Omega_1+\Omega_2\,],\quad \mathcal B_{+-}(0)=[\,\min f,\ \max f\,],\quad \mathcal B_{--}=-\mathcal B_{++},\quad \mathcal B_{-+}=-\mathcal B_{+-}.
\qquad\text{(11.2)}
```

- The extremes of $`f`$ are among $`f(0)=M_1-M_2`$, $`f(1)=\Omega_1-\Omega_2`$ and, if $`\tau_1\neq\tau_2`$ and $`v^{*}:=\frac{\tau_2^4M_1^2-\tau_1^4M_2^2}{\tau_1^2\tau_2^2(\tau_1^2-\tau_2^2)}\in(0,1)`$, the stationary value $`f(v^{*})=\mathrm{sgn}(\tau_1-\tau_2)\sqrt{(\tau_1^2-\tau_2^2)(\tau_2^2M_1^2-\tau_1^2M_2^2)}/(\tau_1\tau_2)`$.
- The edge $`M_1+M_2`$ is attained at $`q=0`$ and at $`q=\pi`$.
- Exceptional members: for equal data ($`M_1=M_2`$, $`\tau_1=\tau_2`$) $`\mathcal B_{\pm\mp}(0)=\{0\}`$, a point of infinite multiplicity that has square-summable eigenvectors; for $`\tau_i/M_i`$ of order one the bands can overlap. In $`\mathsf R`$ the four bands have widths $`O(\epsilon^2)`$ around $`\pm M_1\pm M_2`$.

### Step 1a. Where a bound level lies, and its multiplicity (class of items 1 and 2)

The definition of the question is pointwise in $`P`$: $`E_b(P)`$ is an eigenvalue of $`H(P)`$ with a square-summable eigenvector, isolated from the rest of the spectrum of $`H(P)`$. It does not say that $`E_b(P)`$ lies outside the bands, and it does not ask for continuity in $`P`$. The interval $`\mathcal P`$ is taken of positive length.

**Flat bands.** The essential spectrum of $`H(P)`$ is the union of the four bands (11.2) (Weyl). Each band is the range of a continuous function of $`p_1`$ on the circle: a closed interval of positive length or a single point, and every point of an interval of positive length is a limit of other points of it. So an isolated point of the spectrum lies either outside the bands, where it is an eigenvalue of finite multiplicity, or in a band that is a single point. Let $`\sigma_1\omega_1(p_1)+\sigma_2\omega_2(P-p_1)=c`$ for all $`p_1`$.
- If $`c\neq0`$: squaring $`\sigma_2\omega_2=c-\sigma_1\omega_1`$ gives $`\omega_1(p_1)=\sigma_1\bigl[c^2+\omega_1(p_1)^2-\omega_2(P-p_1)^2\bigr]/(2c)`$, a trigonometric polynomial $`T`$ of degree at most one in $`e^{2ip_1}`$. Then $`T^2`$ has the degree $`0`$ or $`2`$, while $`\omega_1^2=M_1^2+\frac{\tau_1^2}2(1-\cos2p_1)`$ has the degree one ($`\tau_1>0`$). This is impossible.
- If $`c=0`$: $`\sigma_1=-\sigma_2`$ and $`\omega_1(p_1)^2=\omega_2(P-p_1)^2`$ for all $`p_1`$. The coefficients of $`\sin2p_1`$, $`\cos2p_1`$ and $`1`$ give $`\tau_2^2\sin2P=0`$, $`\tau_1^2=\tau_2^2\cos2P`$ and $`M_1^2+\frac{\tau_1^2}2=M_2^2+\frac{\tau_2^2}2`$.

Hence, for all data and every $`P`$:

```math
\text{a band of (11.2) is a single point}\iff M_1=M_2,\ \ \tau_1=\tau_2\ \ \text{and}\ \ P\in\{0,\pi\};\qquad\text{then}\quad \mathcal B_{+-}(P)=\mathcal B_{-+}(P)=\{0\}.
\qquad\text{(11.27)}
```

**What the definition gives.** Let $`E_b`$ be a bound level on $`\mathcal P`$.
- **Rule.** At every $`P\in\mathcal P`$ at which $`E_b(P)`$ is not the single point of a band, $`E_b(P)`$ lies outside the bands and has a finite multiplicity $`n(P)`$. By (11.27) this is every $`P\in\mathcal P`$ with one possible exception: for equal data, a point $`P_*\in\{0,\pi\}\cap\mathcal P`$ with $`E_b(P_*)=0`$, a *flat value*. There the multiplicity is infinite.
- **The pointwise conditions do not exclude a flat value.** For equal data and every $`W\in\mathcal W`$, $`0`$ is an eigenvalue of $`H(P_*)`$ with square-summable eigenvectors, isolated from the rest of the spectrum: $`U`$ has finite rank, so it vanishes on a subspace of finite codimension of the kernel of $`H^0(P_*)`$, and only finitely many eigenvalues lie in the gap around $`0`$.
- **What the interval adds.** For equal data write $`M`$, $`\tau`$, $`\omega`$ and $`\Omega=\sqrt{M^2+\tau^2}`$. The two mixed bands are $`[-\Delta(P),\Delta(P)]`$ with $`\Delta(P)=\max_{p_1}[\omega(p_1)-\omega(P-p_1)]`$, because $`p_1\to P-p_1`$ changes the sign. With $`x:=P-P_*`$ and $`p_1=q+\frac x2`$ ($`\omega`$ is even and has the period $`\pi`$), $`\omega(p_1)-\omega(P-p_1)=\omega(q+\frac x2)-\omega(q-\frac x2)=x\,\omega'(q)+O(x^3)`$, and $`\max_p\lvert\omega'(p)\rvert=\max_p\tau^2\lvert\sin p\cos p\rvert/\omega(p)=\Omega-M`$, attained at $`\sin^2p=M/(\Omega+M)`$. At every other point of $`\mathcal P`$ the level lies outside these bands, so:

```math
E_b(P_*)=0\ \Longrightarrow\ \lvert E_b(P)-E_b(P_*)\rvert>\Delta(P)\ \ \text{for every }P\in\mathcal P\setminus\{0,\pi\},\qquad \Delta(P)=(\Omega-M)\,\lvert P-P_*\rvert+O\bigl(\lvert P-P_*\rvert^3\bigr)\ \ (P\to P_*).
\qquad\text{(11.28)}
```

  Consequences. A bound level that is differentiable at $`P_*`$ with $`\lvert E_b'(P_*)\rvert<\Omega-M`$, in particular with $`E_b'(P_*)=0`$, has no flat value at $`P_*`$: it lies outside the bands there as well. A bound level with a flat value at an interior point $`P_*`$ of $`\mathcal P`$ that is even about $`P_*`$ is not differentiable at $`P_*`$.
- **A continuous member with a flat value.** Equal data and the on-site binding $`W(r)=\delta_{r,0}\,w\,\lvert v\rangle\langle v\rvert`$ with $`v:=(\lvert11\rangle-\lvert22\rangle)/\sqrt2`$ and $`w>0`$. It belongs to $`\mathcal W`$ and is not diagonal. By the first lines of Step 6, which hold for every on-site binding, the eigenvalues outside the bands are the roots of $`1+w\,g_v(E,P)=0`$ with $`g_v:=\langle v\vert G(E,P)\vert v\rangle`$, and they are simple.
  - $`P=0`$. With $`n_1:=(M\sigma^{(1)}_3-\tau\sin q\,\sigma^{(1)}_1)/\omega`$ and $`n_2:=(M\sigma^{(2)}_3+\tau\sin q\,\sigma^{(2)}_1)/\omega`$, $`h_0(q)=\omega\,(n_1+n_2)`$, and its kernel is the eigenspace $`n_1n_2=-1`$. From $`\sigma^{(1)}_3\sigma^{(2)}_3v=v`$, $`\sigma^{(1)}_1\sigma^{(2)}_1v=-v`$ and $`(\sigma^{(1)}_3\sigma^{(2)}_1-\sigma^{(1)}_1\sigma^{(2)}_3)v=0`$ follows $`n_1n_2v=v`$ for every $`q`$. So $`U`$ vanishes on the kernel of $`H^0(0)`$, and $`0`$ is an eigenvalue of $`H(0)`$ of infinite multiplicity. On $`v`$ the branches $`++`$ and $`--`$ have the weight $`\frac12`$ each, so $`g_v(E,0)=\int\frac{\mathrm dq}{2\pi}\frac{E}{4\omega^2-E^2}`$ for $`\lvert E\rvert<2M`$, and $`1+w\,g_v(E,0)`$ has no root near $`E=0`$: the value $`0`$ is isolated.
  - $`P\neq0`$, small. On the gap above the mixed bands $`g_v(\cdot,P)`$ increases with $`E`$ ($`\partial_EG=\int\frac{\mathrm dq}{2\pi}(h_P-E)^{-2}>0`$). For $`E\downarrow\Delta(P)`$ it tends to $`-\infty`$: the branch $`\omega_1-\omega_2`$ has its maximum $`\Delta(P)`$ at some $`q^*`$, where $`\Delta-(\omega_1-\omega_2)\le c\,(q-q^*)^2`$, and the weight of $`v`$ in this branch is $`\frac12(\sqrt\alpha\mp\sqrt\beta)^2`$ with $`\alpha,\beta=\frac14(1\pm\frac M{\omega_1})(1\mp\frac M{\omega_2})`$, which vanishes only where $`\omega_1=\omega_2`$. For a fixed $`E_1\in(0,2M)`$, $`g_v(E_1,P)\to g_v(E_1,0)>0`$ as $`P\to0`$. So for every small $`P\neq0`$ there is exactly one root $`E_b(P)\in(\Delta(P),E_1)`$: a simple eigenvalue outside the bands, and $`E_b(P)\to0`$ as $`P\to0`$.
  - The function equal to this root for $`0<\lvert P\rvert<P_1`$ and to $`0`$ at $`P=0`$ is continuous and meets the definition of the question on $`\mathcal P=(-P_1,P_1)`$. Its value at $`P=0`$ lies in the bands and has infinite multiplicity. The map $`\psi(r)\to\sigma^{(1)}_3\sigma^{(2)}_3\psi(-r)`$ takes $`H(P)`$ to $`H(-P)`$ for this binding, so $`E_b`$ is even, and by (11.28) $`E_b(P)>(\Omega-M)\lvert P\rvert+O(\lvert P\rvert^3)`$ on both sides: $`E_b'(0)`$ does not exist. Part 3 of the code finds this eigenvalue (see "Code").
- **What is proven where.**
  - Steps 3–5a use an isolated eigenvalue of finite multiplicity. They hold at every $`P\in\mathcal P`$ at which the level lies outside the bands: by the rule, at every $`P\in\mathcal P`$ except a flat value.
  - At a flat value: (11.6) holds for every square-summable eigenvector, as the expectation value of (11.1). (11.5), (11.7), (11.9), (11.23) and (11.24) are not derived there. A derivative with respect to $`M_i`$ or $`\tau_i`$ of one body is not defined there: by (11.27) such a change turns the point into an interval of the bands. In the member above (11.7) has no meaning at $`P=0`$.
  - Steps 6–10 are not affected: a root of (11.10) lies outside the bands, the level of Step 7 is near $`M_1+M_2\neq0`$, and Step 10 assumes a simple level.
  - Open: whether a bound level can have a flat value and be differentiable at $`P_*`$. By (11.28) it would have $`\lvert E_b'(P_*)\rvert\ge\Omega-M`$ and would lie above the mixed bands on one side of $`P_*`$ and below them on the other.

### Step 2. Replacements and well-defined quantities (item 1b)

Expand a change of the four listed terms with zero sum in products of operators on $`b_1`$, $`b_2`$, $`c`$. A component that is non-trivial on two objects occurs in one listed term only and must vanish. Hence, as in (21.2) of 03-ilang-space/21-composite-body, with single-object operators in place of the numbers there (the terms here are not diagonal in the places): with $`T_1,\alpha`$ self-adjoint on $`\mathcal H_{b_1}`$ and $`T_2,\beta`$ on $`\mathcal H_{b_2}`$,

```math
\delta C^{\rm D}_1=T_1,\qquad \delta C^{\rm D}_2=T_2,\qquad \delta C_{\rm rec}=\alpha+\beta,\qquad \delta U=-(T_1+\alpha)-(T_2+\beta),
\qquad\text{(11.3)}
```

and inside $`C_{\rm rec}`$ an operator $`Z`$ on $`\mathcal H_c`$ can move between its two pair terms.

- **What the range condition fixes.** If $`U`$ and $`U+\delta U`$ are in $`\mathcal W`$, then $`\delta W(x_1-x_2)=-\theta_1(x_1)\otimes\mathbb 1-\mathbb 1\otimes\theta_2(x_2)`$ with $`\theta_i(x)`$ on the branch label of $`b_i`$, and $`\delta W=0`$ for $`\lvert x_1-x_2\rvert`$ beyond the larger range. Every $`x_1`$ has such $`x_2`$ and conversely, so $`\theta_1=t\,\mathbb 1`$, $`\theta_2=-t\,\mathbb 1`$ with one real $`t`$, and $`\delta U=0`$. The range condition fixes $`U`$ completely. Without it, single-object terms can be listed in $`U`$, for example $`W(r)\to W(r)+M_1\sigma^{(1)}_3`$ with $`B_1\to0`$.
- **What remains.** With $`\delta U=0`$, (11.3) reads $`\delta C^{\rm D}_1=t-\alpha`$, $`\delta C^{\rm D}_2=-t-\beta`$, $`\delta C_{\rm rec}=\alpha+\beta`$, so $`\delta C_{\rm pair}=-(\alpha+\beta)=-\delta C_{\rm rec}`$, with every self-adjoint $`\alpha`$ on $`\mathcal H_{b_1}`$ and $`\beta`$ on $`\mathcal H_{b_2}`$ (A5: a single-object term may be listed in the pair term of the body with the medium).
  - Examples: a real constant; $`\alpha=h\,\sigma^{(1)}_3`$, after which the listed coefficient of $`\sigma^{(1)}_3`$ is $`M_1-h`$; a part of the motion term $`A_1`$; $`\alpha=g\,\hat x_1`$. None of them changes $`C`$, the evolution or the record vectors $`(K-\langle K\rangle)\chi`$.
  - The stated forms of the question select among them. For $`C_{\rm rec}`$ to stay a sum of record terms, $`\alpha=\sum_x\alpha_x\lvert x\rangle\langle x\rvert`$ with real numbers $`\alpha_x`$, and $`\beta`$ likewise. The fibres need $`C_{\rm pair}`$ to commute with the joint shift, which gives $`\alpha_x=c_1+gx`$, $`\beta_y=c_2-gy`$, and the one operator $`X`$ in both record terms gives $`g=0`$. Within the stated forms only real constants remain: $`\delta C^{\rm D}_1=t-c_1`$, $`\delta C^{\rm D}_2=-t-c_2`$, $`\delta C_{\rm pair}=-(c_1+c_2)`$.
  - M6 asks for invariance under every replacement (11.3), not only under these. So no quantity may be defined through the listed $`C_{\rm pair}`$. The conventions $`\eta`$ (Step 1) and the choice $`s`$ of the correspondence ($`r\to r+s`$ relabels $`W`$) change no quantity below.

**The operator on the two bodies.** Let $`\langle\chi\vert\,\cdot\,\vert\chi\rangle_c`$ be the partial expectation value over $`\mathcal H_c`$:

```math
C_{\rm bod}:=\langle\chi\vert C\vert\chi\rangle_c=\mathrm{Tr}_c\bigl[C\,(\mathbb 1\otimes\lvert\chi\rangle\langle\chi\rvert)\bigr]=C^{\rm D}_1+C^{\rm D}_2+U+\kappa\,\langle\chi\vert X\vert\chi\rangle\,(\hat x_1+\hat x_2).
\qquad\text{(11.21)}
```

The first two expressions use $`C`$ and $`\chi`$ only. So $`C_{\rm bod}`$ is the same operator on $`\mathcal H_{b_1}\otimes\mathcal H_{b_2}`$ in every listing; in a listing changed by $`\alpha,\beta`$ the listed pair term changes by $`-\alpha-\beta`$ and $`C_{\rm bod}`$ does not. The last expression is its value in the listing of the question.

- **Why this operator.** $`L(\phi\otimes\chi)=\langle\phi\vert C_{\rm bod}\vert\phi\rangle`$ is the total cost (1.8) of a product start. The view of $`\{b_1,b_2\}`$ of such a start evolves by $`C_{\rm bod}`$ up to second order in $`C-C_{\rm bod}\otimes\mathbb 1=\kappa(\hat x_1+\hat x_2)\otimes(X-\langle X\rangle)`$, because the mean of this operator in $`\chi`$ vanishes. This is the weak-record regime.
- **Assumption** $`\langle\chi\vert X\vert\chi\rangle=0`$ (M8). Then $`C_{\rm bod}`$ is the listed $`C_{\rm pair}`$ of the question and commutes with the joint shift. Without the assumption $`C_{\rm bod}`$ contains the uniform gradient $`\kappa\langle X\rangle(\hat x_1+\hat x_2)`$, which does not commute with the joint shift and is of order $`\kappa`$ on a fixed chain; the results below then hold at leading order in $`\kappa`$ only.
- **Data.** By the argument of the range condition, the split $`C_{\rm bod}=K_1\otimes\mathbb 1+\mathbb 1\otimes K_2+U`$ with $`U\in\mathcal W`$ is unique up to one real constant ($`K_1+t`$, $`K_2-t`$). So $`U`$, and $`K_1`$, $`K_2`$ up to a constant, are fixed by $`C`$ and $`\chi`$. $`\tau_i`$, the gaps $`2M^{(i)}_k`$ and the bands (11.2) are read from $`K_i`$, which is $`C^{\rm D}_i`$ up to the constant.

The seven quantities, under every replacement (11.3):

```math
\begin{array}{l|l|l}
& \text{computed from } C_{\rm bod} \text{ of (11.21)} & \text{computed from the listed terms}\\ \hline
W(r) & \text{yes, by the range condition (no without it)} & \text{yes, the same, if the listed } U\in\mathcal W\\
M_i & \text{yes as half the gap } 2M_i;\ \text{no as a cost of } b_i & \text{no (the listed coefficient of } \sigma^{(i)}_3)\\
E_b(P) & \text{yes as a total cost (1.8) only; no as a cost of the pair} & \text{no}\\
E_b(P)-(M_1+M_2) & \text{yes (eigenvalue of the fibre and half gaps of } C_{\rm bod});\ \text{it is } E_{\rm bind}(P) \text{ of (11.22)} & \text{no (listed pair contract, listed coefficients)}\\
E_b(P)-E_b(0),\ E_b''(0) & \text{yes} & \text{no (unchanged under constants only)}\\
\langle\sigma^{(i)}_3\rangle_P & \text{yes (for } n\ge2 \text{ it depends on the eigenvector)} & \text{no (unchanged under constants only)}
\end{array}
\qquad\text{(11.4)}
```

- **$`W(r)`$.** $`\delta U=0`$ in every replacement that keeps $`U\in\mathcal W`$. $`U`$ is the only element of $`\mathcal W`$ for which $`C_{\rm bod}-U`$ is a sum of single-object operators.
- **$`M_i`$.** Half the difference of the two eigenvalues of $`K_i`$ on the level $`k_i`$ at the plane-wave label $`0`$, (6.7). The listed coefficient of $`\sigma^{(i)}_3`$ changes under $`\alpha=h\,\sigma^{(i)}_3`$. The branch costs $`\pm M_i`$ of $`b_i`$ change by the constant $`t`$.
- **$`E_b(P)`$.** It is an eigenvalue of the fibre of $`C_{\rm bod}`$. For $`\Phi`$ of Step 4, $`L(\Phi\otimes\chi)=\int\lvert g\rvert^2E_b`$ is a total cost, which does not depend on the listing (A5). It is not a cost of the pair apart from the medium: which contract carries a constant or a single-object term is a convention, and the eigenvalue of the listed $`C_{\rm pair}`$ changes ($`\delta E_b=-(c_1+c_2)`$ under constants). Its zero enters no reading. Where a later step speaks of the cost of the pair, it means $`E_b`$ in this sense.
- **$`E_b(P)-(M_1+M_2)`$.** Three questions, each with its own answer.
  - (i) *Formed from the listed terms*: the eigenvalue $`E^{\rm list}_b(P)`$ of the fibre of the listed pair contract, minus the listed coefficients of $`\sigma^{(1)}_3`$ and $`\sigma^{(2)}_3`$. This expression is not invariant under (11.3), so it is not well defined: constants $`c_1+c_2`$ listed in the record terms shift $`E^{\rm list}_b`$ by $`-(c_1+c_2)`$ and no coefficient, and $`\alpha=h\,\sigma^{(1)}_3`$ replaces $`M_1`$ by $`M_1-h`$ in both. The same holds with the half gaps of the listed pair contract in place of the listed coefficients: the constants shift $`E^{\rm list}_b`$ and no half gap.
  - (ii) *Formed from $`C_{\rm bod}`$*: the eigenvalue $`E_b(P)`$ of its fibre, minus the half gaps $`M_1`$, $`M_2`$ of $`K_1`$, $`K_2`$. A replacement (11.3) leaves $`C`$ unchanged, and $`C_{\rm bod}`$, $`K_1+K_2`$ and the gaps are fixed by $`C`$ and $`\chi`$. So this expression is invariant under every replacement (11.3): it is well defined. For the $`C`$ of the question it is the distance $`E_{\rm bind}(P)`$ of the level from the band edge, (11.22) below.
  - (iii) *A constant added to the total contract*, $`C\to C+c\,\mathbb 1`$. This is not a replacement (11.3): it changes $`C`$. It multiplies the weighting by the common phase $`e^{-ic\lambda}`$ (1.2), changes no reading, and changes the cost (1.8) of every state by $`c`$. Then $`C_{\rm bod}\to C_{\rm bod}+c`$, $`E_b(P)\to E_b(P)+c`$ and $`e_{++}(P)\to e_{++}(P)+c`$, and the half gaps do not change. So the expression (ii) changes by $`c`$, and $`E_{\rm bind}(P)`$ of (11.22) does not; for $`C+c`$, $`e_{++}(0)=M_1+M_2+c`$. The form (11.22) is invariant under (11.3) and under the constant; the expression (ii) is invariant under (11.3) only, and so is $`E_b(P)`$ alone.

  The distance from the band edge:

```math
E_{\rm bind}(P):=E_b(P)-e_{++}(0),\qquad e_{++}(P):=\min\mathcal B_{++}(P),\qquad e_{++}(0)=M_1+M_2\ \ (\text{for the } C \text{ of the question}),\qquad E_{\rm bind}:=E_{\rm bind}(0).
\qquad\text{(11.22)}
```

  $`e_{++}(P)`$ is the least sum of the upper-branch costs of $`K_1`$ and $`K_2`$ with the total label $`P`$; the constant $`t`$ cancels in it. $`E_{\rm bind}(P)`$ is a difference of two total costs of the same $`C`$. For the $`C`$ of the question $`C_{\rm bod}`$ has no constant term, so $`e_{++}(0)=M_1+M_2`$ by (11.2), and the expression (ii) equals $`E_{\rm bind}(P)`$.
- **$`E_b(P)-E_b(0)`$, $`E_b''(0)`$.** Differences of total costs. Computed from the listed $`C_{\rm pair}`$ they change under $`\alpha=h\,\sigma^{(1)}_3`$ (in (11.12): $`M_1\to M_1-h`$).
- **$`\langle\sigma^{(i)}_3\rangle_P`$.** $`\sigma^{(i)}_3`$ is diagonal in the places of $`b_i`$: it is the reading of the branch label, (1.3), the probability of $`s_i=1`$ minus that of $`s_i=2`$. $`\psi_P`$ is an eigenvector of the fibre of $`C_{\rm bod}`$. With $`\psi_P`$ of the listed $`C_{\rm pair}`$ it changes under $`\alpha=h\,\sigma^{(1)}_3`$.

### Step 3. Derivatives with respect to the data (item 2a)

$`H(P)`$ is linear in $`M_i`$, in $`\tau_i`$ (through $`A_i`$) and in a factor $`\theta`$ of $`W`$, and these terms are bounded. For a simple isolated eigenvalue, first-order perturbation theory (Hellmann–Feynman) gives, for every $`W\in\mathcal W`$ and every $`P\in\mathcal P`$:

```math
\frac{\partial E_b}{\partial M_i}=\langle\sigma^{(i)}_3\rangle_P,\qquad
\tau_i\frac{\partial E_b}{\partial\tau_i}=\langle A_i\rangle_P,\qquad
\frac{\partial E_b}{\partial\theta}\Big|_{\theta=1}=\langle U\rangle_P\qquad(i=1,2).
\qquad\text{(11.5)}
```

$`H(P)`$ at the data $`(s\tau_i,sM_i,sW)`$ is $`s`$ times $`H(P)`$ at $`(\tau_i,M_i,W)`$, with the same eigenvectors. So $`E_b`$ is homogeneous of degree one in $`(\tau_1,\tau_2,M_1,M_2,\theta)`$, and Euler's relation with (11.5) reads

```math
E_b(P)=M_1\langle\sigma^{(1)}_3\rangle_P+M_2\langle\sigma^{(2)}_3\rangle_P+\langle A_1\rangle_P+\langle A_2\rangle_P+\langle U\rangle_P .
\qquad\text{(11.6)}
```

### Step 4. First derivative in $`P`$ and the velocities (item 2b)

Let $`V_i:=i[C_{\rm pair},\hat x_i]=i[A_i,\hat x_i]`$; $`B_i`$, $`U`$ and $`C_{\rm rec}`$ commute with $`\hat x_i`$, so $`\frac{\mathrm d}{\mathrm d\lambda}\langle\hat x_i\rangle=\langle V_i\rangle`$ holds for the full $`C`$. $`V_i`$ commutes with the joint shift, with the fibres $`V_1=-\frac{\tau_1}2\sigma^{(1)}_1(e^{i\eta P}S^\dagger+e^{-i\eta P}S)`$ and $`V_2=-\frac{\tau_2}2\sigma^{(2)}_1(e^{i(1-\eta)P}S+e^{-i(1-\eta)P}S^\dagger)`$ (on plane waves $`-\tau_i\cos p_i\,\sigma^{(i)}_1`$). From (11.1), $`\partial_PH=\eta V_1+(1-\eta)V_2`$ and $`V_1-V_2=i[H(P),\hat r]`$. The eigenvector $`\psi_P`$ decays exponentially, so $`\hat r\psi_P`$ is square-summable and $`\langle[H(P),\hat r]\rangle_P=0`$. With Hellmann–Feynman in $`P`$:

```math
E_b'(P)=\langle V_1\rangle_P=\langle V_2\rangle_P .
\qquad\text{(11.7)}
```

**Packets and the class of $`g`$.** Let $`\mathcal P_0\subseteq\mathcal P`$ be an open interval on which the bound level is simple and lies outside the bands (Step 1a). On $`\mathcal P_0`$, $`E_b`$ is analytic and $`\psi_P`$ can be chosen analytic in $`P`$ (analytic perturbation theory), and $`\lVert\hat r\psi_P\rVert`$ and $`\lVert\partial_P\psi_P\rVert`$ are bounded on every compact subset. A state of the pair built from the bound level is $`\Phi=\int\mathrm dP\,g(P)\,\lvert P;\psi_P\rangle`$ with $`g`$ supported in $`\mathcal P_0`$ and $`\int\lvert g\rvert^2=1`$. Under $`C_{\rm pair}`$, $`g(P)\to g(P)e^{-iE_b(P)\lambda}`$, and $`V_i`$ has no elements between different $`P`$.

- **Every normalized $`g`$ supported in $`\mathcal P_0`$.** $`V_i`$ is bounded, so its expectation value exists, and by (11.7), for every $`\lambda`$:

```math
\langle\Phi(\lambda)\vert V_1\vert\Phi(\lambda)\rangle=\langle\Phi(\lambda)\vert V_2\vert\Phi(\lambda)\rangle=\int\mathrm dP\,\lvert g(P)\rvert^2E_b'(P).
\qquad\text{(11.29)}
```

  This says nothing on mean position labels: on the infinite chain they need not exist. Example: for $`g`$ constant on a subinterval of $`\mathcal P_0`$ and zero outside (a sharp cutoff), $`\lvert\Phi\rvert^2`$ summed over $`r`$ falls off as the inverse square of the centre label $`\eta x_1+(1-\eta)x_2`$, and $`\sum\lvert x_i\rvert\,\lvert\Phi\rvert^2`$ diverges.
- **The class $`\mathcal G(\mathcal P_0)`$** (sufficient): $`g`$ continuously differentiable with compact support in $`\mathcal P_0`$, and $`\int\lvert g\rvert^2=1`$. On the fibres $`\eta\hat x_1+(1-\eta)\hat x_2`$ acts as $`i\partial_P`$ and $`\hat x_1-\hat x_2`$ as $`\hat r`$, so $`\hat x_i\Phi(\lambda)`$ is square-summable for every $`\lambda`$ ($`g\,e^{-iE_b\lambda}`$ belongs to the class again). Then the mean position labels $`\bar m_i(\lambda)=\langle\Phi(\lambda)\vert\hat x_i\vert\Phi(\lambda)\rangle`$ exist and are differentiable with $`\dot{\bar m}_i=\langle V_i\rangle`$, and (11.29) gives the first two equalities below. Let $`P_0:=\int P\,\lvert g\rvert^2`$, $`\delta P^2:=\int(P-P_0)^2\lvert g\rvert^2`$, and let $`I_g\subset\mathcal P_0`$ be the smallest closed interval that contains the support of $`g`$. Taylor's formula for $`E_b'`$ around $`P_0`$ on $`I_g`$ gives the third equality:

```math
\frac{\mathrm d\bar m_1}{\mathrm d\lambda}=\frac{\mathrm d\bar m_2}{\mathrm d\lambda}=\int\mathrm dP\,\lvert g(P)\rvert^2E_b'(P)=E_b'(P_0)+O(\delta P^2)\qquad\text{for } g\in\mathcal G(\mathcal P_0)\ \text{and every }\lambda,\qquad \bigl\lvert O(\delta P^2)\bigr\rvert\le\tfrac12\max_{I_g}\lvert E_b'''\rvert\;\delta P^2 .
\qquad\text{(11.8)}
```

The two bodies have the same mean velocity: yes, exactly under $`C_{\rm pair}`$, for every $`W\in\mathcal W`$, every bound level and every such $`\mathcal P_0`$, in two senses. For every normalized $`g`$ supported in $`\mathcal P_0`$ the two velocity operators have the same expectation value (11.29). For $`g\in\mathcal G(\mathcal P_0)`$ the two mean position labels exist and change at the same rate (11.8), so $`\bar m_1-\bar m_2`$ is constant. By (17.15) both velocities are $`\kappa\,e\,\dot{\bar m}_i`$. The records change the state, and (11.8), at $`O(\kappa)`$ for fixed $`\lambda`$ and a fixed $`g\in\mathcal G(\mathcal P_0)`$.

### Step 5. Second derivative in $`P`$ (item 2c)

From (11.1), $`\partial_P^2H=-\eta^2A_1-(1-\eta)^2A_2`$ (a lattice property: $`\partial_p^2\sin p=-\sin p`$). Second-order perturbation theory, with $`V_\eta:=\eta V_1+(1-\eta)V_2`$, $`Q_P:=\mathbb 1-\lvert\psi_P\rangle\langle\psi_P\rvert`$ and $`\mu`$ the spectral measure of $`H(P)`$ in the vector $`V_\eta\psi_P`$:

```math
E_b''(P)=-\eta^2\langle A_1\rangle_P-(1-\eta)^2\langle A_2\rangle_P-2\,\mathcal S_\eta(P),\qquad
\mathcal S_\eta(P):=\bigl\langle V_\eta\psi_P\big\vert Q_P\bigl(H(P)-E_b\bigr)^{-1}Q_P\big\vert V_\eta\psi_P\bigr\rangle=\int_{\mathrm{spec}H(P)\setminus\{E_b\}}\frac{\mathrm d\mu(E)}{E-E_b}.
\qquad\text{(11.9)}
```

The sum runs over the bands and the other bound levels. Each of the two parts depends on the convention $`\eta`$; their sum does not (M6).

### Step 5a. Degenerate bound levels (items 2a–2c)

Let $`E_b`$ be an eigenvalue of $`H(P)`$ of multiplicity $`n\ge2`$ outside the bands, at given data and $`P`$. Let $`\mathcal E_b`$ be its eigenspace, $`\Pi_b`$ the projector on it, $`\bar Q:=\mathbb 1-\Pi_b`$ and $`\hat S:=\bar Q\,(H(P)-E_b)^{-1}\bar Q`$ the reduced resolvent, which is bounded. Every vector of $`\mathcal E_b`$ decays exponentially.

Let $`\xi`$ be one of the six real parameters $`M_1,M_2,\tau_1,\tau_2,\theta,P`$, the others fixed. $`H`$ is analytic in $`\xi`$, with $`\partial_{M_i}H=\sigma^{(i)}_3`$, $`\tau_i\partial_{\tau_i}H=A_i`$, $`\partial_\theta H=U`$, $`\partial_PH=V_\eta`$. By Rellich's theorem the eigenvalues near $`E_b`$ are $`n`$ analytic functions $`E^{(\nu)}(\xi)`$, the *branches of $`\xi`$*, with analytic orthonormal eigenvectors; at the given point these are the *branch vectors* $`\psi^{(\nu)}_\xi\in\mathcal E_b`$. A bound level that is differentiable in $`\xi`$ is one branch. First-order degenerate perturbation theory gives

```math
\Pi_b\,(\partial_\xi H)\,\Pi_b\;\psi^{(\nu)}_\xi=\partial_\xi E^{(\nu)}\;\psi^{(\nu)}_\xi ,\qquad
\langle\psi\vert\partial_\xi H\vert\psi\rangle=\sum_{\nu=1}^{n}\bigl\lvert\langle\psi^{(\nu)}_\xi\vert\psi\rangle\bigr\rvert^2\,\partial_\xi E^{(\nu)}\quad\text{for every unit vector }\psi\in\mathcal E_b .
\qquad\text{(11.23)}
```

- **For every eigenvector of the level** (every unit vector $`\psi\in\mathcal E_b`$):
  - (11.6), as the expectation value of (11.1) in an eigenvector;
  - $`\langle V_1\rangle=\langle V_2\rangle`$, and more: $`\Pi_bV_1\Pi_b=\Pi_bV_2\Pi_b`$, because $`\langle\psi\vert[H(P),\hat r]\vert\psi'\rangle=0`$ for $`\psi,\psi'\in\mathcal E_b`$;
  - the second relation of (11.23): each of the six expectation values is a mean of the $`n`$ branch derivatives. It is a derivative only if $`\psi`$ is an eigenvector of the matrix $`\Pi_b(\partial_\xi H)\Pi_b`$.
- **For the branch vectors of the parameter that is varied.** (11.5) holds for $`M_i`$, $`\tau_i`$, $`\theta`$ and (11.7) for $`P`$, each with the eigenvectors of its own matrix $`\Pi_b(\partial_\xi H)\Pi_b`$. The six matrices need not commute, so in general no eigenvector gives all the derivatives. If $`\xi`$ does not split the level (its $`n`$ branches coincide), its matrix is $`\partial_\xi E_b\,\Pi_b`$, and its identity holds for every eigenvector.
- **(11.8) and (11.29).** Let $`\mathcal P_0\subseteq\mathcal P`$ be an open interval on which the level lies outside the bands, with the branch vectors chosen analytic in $`P`$ (Rellich). A state built from one branch of $`P`$ obeys (11.29) for every normalized $`g`$ supported in $`\mathcal P_0`$, and (11.8) for $`g\in\mathcal G(\mathcal P_0)`$. So does a state $`\Phi=\int\mathrm dP\sum_\nu g_\nu(P)\lvert P;\psi^{(\nu)}_P\rangle`$ built from a level that is $`n`$-fold on $`\mathcal P_0`$, with $`\sum_\nu\lvert g_\nu\rvert^2`$ in place of $`\lvert g\rvert^2`$ and every $`g_\nu`$ in the class named: the two bodies have the same mean velocity. Control: where two branches have different values, $`\langle\psi^{(\nu)}\vert(V_1-V_2)\vert\psi^{(\nu')}\rangle=i\bigl(E^{(\nu)}-E^{(\nu')}\bigr)\langle\psi^{(\nu)}\vert\hat r\vert\psi^{(\nu')}\rangle`$, and in a superposition of the two the mean velocities differ by a term that oscillates as $`e^{\pm i(E^{(\nu)}-E^{(\nu')})\lambda}`$. Such a state is built from two bound levels.
- **What replaces (11.9).** Second-order degenerate perturbation theory in $`P`$ gives, for a branch vector $`\psi^{(\nu)}_P`$ and with $`\langle\cdot\rangle_\nu`$ its expectation value:

```math
E^{(\nu)\prime\prime}(P)=-\eta^2\langle A_1\rangle_\nu-(1-\eta)^2\langle A_2\rangle_\nu-2\,\bigl\langle V_\eta\psi^{(\nu)}_P\big\vert\hat S\big\vert V_\eta\psi^{(\nu)}_P\bigr\rangle,\qquad \hat S=\bar Q\bigl(H(P)-E_b\bigr)^{-1}\bar Q .
\qquad\text{(11.24)}
```

  The sum over the rest of the spectrum leaves out the whole eigenspace $`\mathcal E_b`$. If several branches have the same first derivative, with $`\Pi'`$ the projector on their branch vectors, their second derivatives are the eigenvalues of $`\Pi'\bigl[\partial_P^2H-2V_\eta\hat SV_\eta\bigr]\Pi'`$, and their branch vectors are its eigenvectors. For $`n=1`$, (11.24) is (11.9). For $`n\ge2`$, (11.9) is not defined: $`Q_P(H(P)-E_b)^{-1}Q_P`$ does not exist on the rest of $`\mathcal E_b`$.
- **Members.** Degenerate levels exist in $`\mathcal W`$.
  - For a diagonal on-site binding, by (11.10) a root of $`F_-`$ can be placed on a root of $`F_+`$ by the choice of $`w_{12}`$, $`w_{21}`$. All six operators commute with $`\Xi`$ of Step 6, so the vectors with a definite $`\Xi`$ are branch vectors of every parameter.
  - For the on-site binding $`W_0=-G(E_0,P_0)^{-1}`$ on the span of $`\lvert11\rangle`$, $`\lvert22\rangle`$, with $`G`$ of Step 6 and $`E_0`$ outside the bands, $`\mathbb 1_4+GW_0`$ vanishes on that span, so $`E_0`$ is a twofold level of $`H(P_0)`$. For one such member the six matrices do not commute; this statement rests on the code (`code/v3/check_bound_pair.py`, set X).

### Step 6. Equation for the bound levels of a diagonal on-site binding (item 3a)

$`U=\lvert0\rangle\langle0\rvert\otimes W_0`$, with $`\lvert0\rangle`$ the place $`r=0`$. For $`E`$ outside the bands, $`(H^0+U-E)\psi=0`$ is equivalent to $`\psi=-(H^0-E)^{-1}\lvert0\rangle W_0\psi(0)`$, hence to $`[\mathbb 1_4+G\,W_0]\psi(0)=0`$ with $`G(E,P):=\langle0\rvert(H^0(P)-E)^{-1}\lvert0\rangle=\int\frac{\mathrm dq}{2\pi}(h_P(q)-E)^{-1}`$; a solution gives $`\psi(r)=-\int\frac{\mathrm dq}{2\pi}e^{iqr}(h_P(q)-E)^{-1}W_0\psi(0)`$, which is square-summable. The two parts of $`h_P(q)`$ commute, so $`(h_P(q)-E)^{-1}=\sum_{\sigma_1,\sigma_2}\Pi^{(1)}_{\sigma_1}\Pi^{(2)}_{\sigma_2}/(\sigma_1\omega_1+\sigma_2\omega_2-E)`$ with $`\Pi^{(i)}_\sigma=\frac12\bigl(\mathbb 1+\sigma(M_i\sigma^{(i)}_3-\tau_i\sin p_i\,\sigma^{(i)}_1)/\omega_i\bigr)`$ and $`\omega_i=\omega_i(p_i)`$. Under $`q\to q+\pi`$ both $`\sin p_i`$ change sign and the $`\omega_i`$ do not, so the terms with one factor $`\sin p_i`$ integrate to zero. $`G`$ has the diagonal elements $`G_{s_1s_2}`$ and the only other elements $`\langle11\vert G\vert22\rangle=\langle12\vert G\vert21\rangle=g_\times`$ (and their transposes). The bound levels of $`H(P)`$ are the solutions $`E`$ outside the bands of

```math
\begin{aligned}
&F_+(E,P)\,F_-(E,P)=0,\qquad F_+:=(1+w_{11}G_{11})(1+w_{22}G_{22})-w_{11}w_{22}\,g_\times^2,\quad F_-:=(1+w_{12}G_{12})(1+w_{21}G_{21})-w_{12}w_{21}\,g_\times^2,\\
&G_{s_1s_2}=\int_{-\pi}^{\pi}\frac{\mathrm dq}{2\pi}\sum_{\sigma_1,\sigma_2=\pm}\frac{\bigl(1+(-1)^{s_1-1}\sigma_1\frac{M_1}{\omega_1}\bigr)\bigl(1+(-1)^{s_2-1}\sigma_2\frac{M_2}{\omega_2}\bigr)}{4\,(\sigma_1\omega_1+\sigma_2\omega_2-E)},\qquad
g_\times=\int_{-\pi}^{\pi}\frac{\mathrm dq}{2\pi}\sum_{\sigma_1,\sigma_2=\pm}\frac{\sigma_1\sigma_2\,\tau_1\tau_2\sin p_1\sin p_2}{4\,\omega_1\omega_2\,(\sigma_1\omega_1+\sigma_2\omega_2-E)} .
\end{aligned}
\qquad\text{(11.10)}
```

The multiplicity of a level is $`\dim\ker(\mathbb 1_4+GW_0)`$. The two factors belong to the two sectors of the exact symmetry $`\Xi:=(-1)^{\hat r}\sigma^{(1)}_3\sigma^{(2)}_3`$, $`[\Xi,H(P)]=0`$, which holds for every diagonal on-site binding because each $`A_i`$ changes $`r`$ by one and flips one branch. $`F_+`$ ($`\Xi=+1`$: equal branches on even $`r`$, different branches on odd $`r`$) contains only $`w_{11},w_{22}`$; $`F_-`$ ($`\Xi=-1`$) only $`w_{12},w_{21}`$. Class: every diagonal on-site binding, all data; exact. The flat value of Step 1a (equal data, $`P\in\{0,\pi\}`$, $`E=0`$) lies in the bands and is not among these solutions.

### Step 7. Regime $`\mathsf R`$: the bound level at the band $`\mathcal B_{++}`$ (item 3b)

In $`\mathsf R`$, $`H(P)=H_0+\epsilon H_1+\epsilon^2H_2`$ with $`H_0=M_1\sigma^{(1)}_3+M_2\sigma^{(2)}_3`$, $`\epsilon H_1=A_1+A_2`$, $`\epsilon^2H_2=U`$. The eigenvalue $`M_1+M_2`$ of $`H_0`$ (projector $`\Pi`$ onto the branches $`\lvert11\rangle`$, all $`r`$) is separated from the other three by at least $`2\min(M_1,M_2)`$. All terms are bounded uniformly in $`r`$, so degenerate perturbation theory applies: the part of $`H(P)`$ with spectrum near $`M_1+M_2`$ is unitarily equivalent, by a unitary that differs from $`\mathbb 1`$ by $`O(\epsilon)`$, to

```math
H_{\rm eff}(P)=M_1+M_2+\Pi\,U\,\Pi+\Pi\Bigl(\frac{A_1^2}{2M_1}+\frac{A_2^2}{2M_2}\Bigr)\Pi+O(\epsilon^4)\quad\text{in norm}.
```

Here $`\Pi A_i\Pi=0`$; $`A_i`$ leads to the branch value $`M_1+M_2-2M_i`$ of $`H_0`$; $`\Pi A_1A_2\Pi=0`$; and the odd orders vanish because $`\sigma^{(1)}_3\sigma^{(2)}_3`$ maps $`H`$ at $`\epsilon`$ to $`H`$ at $`-\epsilon`$. With $`A_i^2=\tau_i^2\sin^2p_i=2M_ia_i(1-\cos2p_i)`$, on the coefficient $`\psi(r)`$ of $`\lvert11\rangle`$:

```math
(H_{\rm eff}\psi)(r)=\bigl(M_1+M_2+a+w\,\delta_{r,0}\bigr)\psi(r)-\tfrac12\bigl[J\,\psi(r+2)+J^{*}\psi(r-2)\bigr],\qquad J(P):=a_1e^{2i\eta P}+a_2e^{-2i(1-\eta)P}=j(P)\,e^{i\alpha(P)} .
\qquad\text{(11.11)}
```

Of the four numbers only $`w_{11}`$ enters. Even and odd $`r`$ decouple, and the binding acts on even $`r`$ only. With $`\psi(2n)=e^{-i\alpha n}\phi(n)`$ this is a chain with the hopping $`-\frac j2`$ and one changed site: its band is $`M_1+M_2+a+[-j,j]`$ (the band $`\mathcal B_{++}(P)`$ at this order), and for $`w\neq0`$ it has exactly one further eigenvector, $`\phi(n)\propto\rho^{\lvert n\rvert}`$ with $`\lvert\rho\rvert<1`$. The equations at $`n\neq0`$ and at $`n=0`$ are $`E-(M_1+M_2+a)=-\frac j2(\rho+\rho^{-1})`$ and $`\frac j2(\rho-\rho^{-1})=w`$, hence $`\rho=-\varsigma\bigl(\sqrt{w^2+j^2}-\lvert w\rvert\bigr)/j`$ and

```math
E_b(P)=M_1+M_2+a+\varsigma\sqrt{w^2+j(P)^2}+O(\epsilon^4),\qquad j(P)^2=a_1^2+a_2^2+2a_1a_2\cos2P ,
\qquad\text{(11.12)}
```

```math
\psi_P(r)=\mathcal N_P\,e^{-i\alpha(P)\,r/2}\,\rho(P)^{\lvert r\rvert/2}\,\lvert11\rangle\ \ (r\ \text{even}),\qquad \psi_P(r)=0\ \ (r\ \text{odd}),\qquad \mathcal N_P^2=\frac{\lvert w\rvert}{\sqrt{w^2+j^2}},\qquad\text{up to } O(\epsilon).
\qquad\text{(11.13)}
```

The $`O(\epsilon)`$ part is $`\bigl(\frac{A_1}{2M_1}+\frac{A_2}{2M_2}\bigr)\psi_P`$: the branches $`\lvert21\rangle`$, $`\lvert12\rangle`$ on odd $`r`$. The odd orders of $`E_b`$ vanish, so the remainder in (11.12) is $`O(\epsilon^4)`$ against terms of order $`\epsilon^2`$.

The forms of $`\rho`$ and (11.13) are for $`j(P)\neq0`$. $`j(P)=0`$ occurs only for $`a_1=a_2`$ at $`P=\pm\frac\pi2`$. Then $`J=0`$, $`\alpha`$ is not defined and not needed, the chain has no hopping, and the eigenvector of the changed site is $`\psi_P(r)=\delta_{r,0}\lvert11\rangle`$ up to $`O(\epsilon)`$, with $`E_b=M_1+M_2+a+w+O(\epsilon^4)`$. These are the limits $`\rho\to0`$, $`\mathcal N_P\to1`$ of (11.13) and the value of (11.12) at $`j=0`$.

- **Existence and number.** The level (11.12) is at the distance $`\sqrt{w^2+j^2}-j`$ from the band, of order $`\epsilon^2`$, and the remainder of $`H_{\rm eff}`$ is $`O(\epsilon^4)`$ in norm. So for small $`\epsilon`$: $`H(P)`$ has a bound level at a distance of order $`\epsilon^2`$ from $`\mathcal B_{++}(P)`$ if and only if $`\hat w_{11}\neq0`$. It is then exactly one, simple, for every $`P\in(-\pi,\pi]`$: below the band for $`\hat w_{11}<0`$, above the band for $`\hat w_{11}>0`$.
- **What the order leaves out.** Every other point of the spectrum near $`M_1+M_2`$ lies within $`O(\epsilon^4)`$ of the band. For $`\hat w_{11}=0`$, and in the sector $`\Xi=-1`$ (the branches $`\lvert11\rangle`$ on odd $`r`$, where $`w_{12},w_{21}`$ act at order $`\epsilon^4`$), a bound level, if any, is at such a distance and is not seen at leading order.
- **Other numbers.** $`w_{22}`$ enters $`E_b`$ at order $`\epsilon^6`$. First-order perturbation theory in the number $`w_{22}`$ alone gives $`\partial E_b/\partial w_{22}=\lvert\langle22\vert\psi_P(0)\rangle\rvert^2`$; the branch $`\lvert22\rangle`$ needs two flips, so its amplitude is $`O(\epsilon^2)`$ and this derivative $`O(\epsilon^4)`$, and $`w_{22}=O(\epsilon^2)`$. (In $`F_+`$: the term $`w_{11}w_{22}g_\times^2`$ is $`O(\epsilon^4)`$ against a slope $`w_{11}\partial_EG_{11}`$ of order $`\epsilon^{-2}`$.) The $`O(\epsilon^4)`$ remainder of (11.12) has other sources. $`w_{12},w_{21}`$ do not enter this level at any order.

### Step 8. Leading terms and the two limits (items 3c, 3d)

$`E_b`$ is analytic in the data with a remainder bounded uniformly near real data, so (11.12) can be differentiated and the remainders stay $`O(\epsilon^4)`$. From (11.5), (11.12), with $`(j^2)'(0)=0`$, $`(j^2)''(0)=-8a_1a_2`$, $`\partial_{M_i}a=-a_i/M_i`$, $`\tau_i\partial_{\tau_i}a=2a_i`$:

```math
E_{\rm bind}=a+\varsigma\sqrt{w^2+a^2},\quad E_b''(0)=-\varsigma\frac{4a_1a_2}{\sqrt{w^2+a^2}},\quad \langle\sigma^{(i)}_3\rangle_0=1-\frac{a_i}{M_i}\Lambda,\quad \langle A_i\rangle_0=2a_i\Lambda,\quad \langle U\rangle_0=\varsigma\frac{w^2}{\sqrt{w^2+a^2}},\qquad \Lambda=1+\frac{\varsigma\,a}{\sqrt{w^2+a^2}} .
\qquad\text{(11.14)}
```

Each is given up to $`O(\epsilon^4)`$; the terms shown (for $`\langle\sigma^{(i)}_3\rangle_0`$ the deviation from one) are of order $`\epsilon^2`$. The combination of the binding that enters is $`u=\lvert w_{11}\rvert/a`$. Limits within $`\mathsf R`$, taken as ordered limits (stated below the table), with relative corrections $`O(u^2)`$ (wide) and $`O(u^{-2})`$ (tight):

```math
\begin{array}{l|ccc}
& \text{wide } (u\to0),\ w<0 & \text{wide } (u\to0),\ w>0 & \text{tight } (u\to\infty)\\ \hline
E_{\rm bind} & -\dfrac{w^2}{2a} & 2a+\dfrac{w^2}{2a} & w+a+\dfrac{a^2}{2w}\\
E_b''(0) & \dfrac{4a_1a_2}{a}\bigl(1-\tfrac{u^2}2\bigr) & -\dfrac{4a_1a_2}{a}\bigl(1-\tfrac{u^2}2\bigr) & -\dfrac{4a_1a_2}{w}\\
1-\langle\sigma^{(i)}_3\rangle_0 & \dfrac{a_i}{M_i}\dfrac{u^2}2 & \dfrac{2a_i}{M_i} & \dfrac{a_i}{M_i}\bigl(1+\tfrac aw\bigr)\\
\langle A_i\rangle_0 & a_iu^2 & 4a_i & 2a_i\bigl(1+\tfrac aw\bigr)\\
\langle U\rangle_0 & -\dfrac{w^2}{a} & \dfrac{w^2}{a} & w-\dfrac{a^2}{2w}
\end{array}
\qquad\text{(11.15)}
```

**Order of the limits.** Every wide-pair and tight-pair form of this package is an ordered limit: the table (11.15), the statements after (11.16), (11.17), (11.20) and (11.26), and those of the Result.
1. First $`\epsilon\to0`$ at fixed hatted data, hence at a fixed $`u\in(0,\infty)`$. This gives (11.14): each quantity there is $`\epsilon^2`$ times a function of the hatted data, up to $`O(\epsilon^4)`$. The constant of this $`O(\epsilon^4)`$ depends on the hatted data; Steps 7 and 8 do not bound it for $`u\to0`$ or $`u\to\infty`$.
2. Then $`u\to0`$ (wide) or $`u\to\infty`$ (tight) in the functions (11.14), with the other hatted data fixed. As statements on the functions (11.14) the entries of (11.15) are exact up to the relative corrections named.

So a wide or tight form is the leading term of the coefficient of $`\epsilon^2`$ in the quantity (of $`\epsilon^{-2}`$ for $`\mathfrak m_b`$, of $`\epsilon^{0}`$ in (11.17)). It is not a statement at a fixed $`\epsilon`$. The value $`u=0`$ is not a member of these limits: without a binding there is no bound level, and (11.18) holds instead.

**Joint range (sufficient conditions, for the level only).** Let $`\tau:=\max_i\tau_i`$, $`M:=\min_iM_i`$ and $`\bar w:=\max\lvert w_{s_1s_2}\rvert`$. The part of $`H_{\rm eff}`$ that Step 7 neglects is of third order (two factors $`A_i`$ with one factor $`U`$, or with the shift of the denominators $`2M_i`$ by the level) and of fourth order (four factors $`A_i`$). Its norm is therefore at most $`\varrho`$ below, with numbers $`c`$, $`\varepsilon_0`$ that do not depend on the data. Let

```math
\tau+\bar w\le\varepsilon_0M\quad(\text{gap to the other branch groups}),\qquad \sqrt{w^2+a^2}-a>2\varrho\quad(\text{isolation}),\qquad \varrho:=c\,\frac{\tau^2}{M}\Bigl(\frac{\tau^2}{M^2}+\frac{\bar w}{M}\Bigr).
\qquad\text{(11.30)}
```

For every $`P`$ the level of (11.11) is simple and at the distance $`\sqrt{w^2+j^2}-j\ge\sqrt{w^2+a^2}-a`$ from the rest of the spectrum of (11.11). Under (11.30) the neglected part is smaller than half this distance, so $`H(P)`$ has exactly one eigenvalue within $`\varrho`$ of (11.12), and it is simple.
- *Wide* ($`u\le1`$, the other hatted data in a fixed bounded set): $`\varrho=O(\epsilon^4)`$, and (11.30) reads $`u^2\ge K\epsilon^2`$ with a constant $`K`$ of that set. Then $`E_{\rm bind}=-\frac{w^2}{2a}\bigl[1+O(u^2)+O(\epsilon^2/u^2)\bigr]`$ for $`w<0`$; for $`w>0`$ the same bracket multiplies the term $`\frac{w^2}{2a}`$ of $`2a+\frac{w^2}{2a}`$.
- *Tight* ($`u\ge1`$): $`\bar w=O(\epsilon^2u)`$ and $`\varrho=O(\epsilon^2u\,a)`$, the isolation condition holds for small $`\epsilon`$, and (11.30) reads $`u\le\epsilon^{-2}/K`$, that is $`\lvert w_{11}\rvert\ll M`$. Then $`E_{\rm bind}=w+a+O(a/u)+O(\epsilon^2u\,a)`$: the first two terms of the tight form hold for $`1\ll u\ll\epsilon^{-2}`$, and its third term $`\frac{a^2}{2w}`$ exceeds the remainder only for $`u\ll\epsilon^{-1}`$.
- (11.30) is sufficient. It is not necessary: for $`w_{11}<0`$ at $`P=0`$ the lower band edge is exactly $`M_1+M_2`$, and in the code the relative deviation of $`E_{\rm bind}`$ from (11.14) stays below $`4\times10^{-3}`$ for $`u`$ from $`2`$ down to $`\frac1{128}`$ at $`\max_i\tau_i/M_i=0.2`$, where $`\epsilon^2/u^2`$ reaches $`655`$. This statement rests on the code (Part 3). The scale $`u\sim\epsilon`$ is real elsewhere: for $`w_{11}>0`$, and for $`w_{11}<0`$ at $`P=\frac\pi2`$, the remainder tends to a constant of order $`\epsilon^4`$ and exceeds the isolation (same runs).
- For $`E_b''(0)`$, the expectation values, $`\mathfrak m_b`$ and $`\Gamma_i`$ no joint limit is derived: the first sentence of this step differentiates the remainder at fixed hatted data.

### Step 9. Curvature inertia, inertias of the parts and cost (item 4)

**(a)** With $`4a_1a_2/a=1/(\mathfrak m_1+\mathfrak m_2)`$, $`1/(4a_1a_2)=4\mathfrak m_1\mathfrak m_2`$ and $`\varsigma\sqrt{w^2+a^2}=E_{\rm bind}-a`$, (11.14) gives, at leading order in $`\mathsf R`$ (relative remainder $`O(\epsilon^2)`$), for both signs of $`w_{11}`$:

```math
\mathfrak m_b=-\varsigma\,(\mathfrak m_1+\mathfrak m_2)\sqrt{1+u^2}=\mathfrak m_1+\mathfrak m_2-4\,\mathfrak m_1\mathfrak m_2\,E_{\rm bind} .
\qquad\text{(11.16)}
```

The difference $`\mathfrak m_b-(\mathfrak m_1+\mathfrak m_2)`$ has the sign of $`-w_{11}`$, which is the sign of $`-E_{\rm bind}`$. For $`w_{11}<0`$ it is $`(\mathfrak m_1+\mathfrak m_2)(\sqrt{1+u^2}-1)>0`$, which grows from $`(\mathfrak m_1+\mathfrak m_2)u^2/2`$ (wide) to $`(\mathfrak m_1+\mathfrak m_2)u`$ (tight). For $`w_{11}>0`$, $`\mathfrak m_b<0`$ and the difference is $`-(\mathfrak m_1+\mathfrak m_2)(\sqrt{1+u^2}+1)`$. Through $`E_{\rm bind}`$ it is $`-4\mathfrak m_1\mathfrak m_2E_{\rm bind}`$, for a wide pair and for every $`u`$. All terms of (11.16) are of order $`\epsilon^{-2}`$.

Order of the limits (Step 8): (11.16) is the coefficient of $`\epsilon^{-2}`$ at a fixed $`u`$; "for every $`u`$" means every fixed $`u\in(0,\infty)`$, and the wide and tight values of the difference are the limits $`u\to0`$ and $`u\to\infty`$ of this coefficient. At a fixed $`u`$ the difference has a relative remainder $`O(\epsilon^2)`$, whose constant Step 8 does not bound for $`u\to0`$, where the difference itself vanishes as $`u^2`$, or for $`u\to\infty`$. No joint limit is derived.

**(b)** Let $`\tau_1=\tau_2=\tau`$, so $`\tau^2(\mathfrak m_1+\mathfrak m_2)=M_1+M_2`$ and $`4\tau^2\mathfrak m_1\mathfrak m_2=4M_1M_2/\tau^2`$. From (11.16) and (11.14):

```math
\tau^2\mathfrak m_b=M_1+M_2-\frac{4M_1M_2}{\tau^2}E_{\rm bind}+O(\epsilon^2),\qquad M_1+M_2+E_{\rm bind}=M_1+M_2+O(\epsilon^2),\qquad \sum_iM_i\langle\sigma^{(i)}_3\rangle_0=M_1+M_2-a\Lambda+O(\epsilon^4).
\qquad\text{(11.17)}
```

- $`\tau^2\mathfrak m_b`$ against the cost $`M_1+M_2+E_{\rm bind}`$: not at all. The leading difference is $`-\frac{4M_1M_2}{\tau^2}E_{\rm bind}=(M_1+M_2)\bigl(-\varsigma\sqrt{1+u^2}-1\bigr)`$, of order $`\epsilon^0`$, while the binding changes the cost by $`E_{\rm bind}=O(\epsilon^2)`$ with the opposite sign. The two agree only in the ordered limit of Step 8 (first $`\epsilon\to0`$ at fixed $`u`$, then $`u\to0`$ with $`w_{11}<0`$), in which the leading difference tends to zero, and exactly without a binding (d).
- $`\tau^2\mathfrak m_b`$ against $`\sum_iM_i\langle\sigma^{(i)}_3\rangle_0`$: not at all, with the same leading difference.
- The cost against $`\sum_iM_i\langle\sigma^{(i)}_3\rangle_0`$: they agree at order $`\epsilon^0`$ and differ at order $`\epsilon^2`$ by $`\langle A_1\rangle_0+\langle A_2\rangle_0+\langle U\rangle_0=2a\Lambda+\varsigma w^2/\sqrt{w^2+a^2}`$; this difference is exact by (11.6).

**(c)** Comparison with (21.15), (21.16) of 03-ilang-space/21-composite-body, in label units ($`\mathfrak m\leftrightarrow\sigma_X^2I`$).
- Common: the same function, $`\mathfrak m_b/(\mathfrak m_1+\mathfrak m_2)=\sqrt{1+u^2}`$ against $`I_c/2I_1=\sqrt{1+U^2/16t^2}`$, where in both cases the binding is divided by the half-width of the two-body band at total label zero ($`a`$ here, $`4t`$ there); an attractive binding raises the inertia, and the excess is linear in $`E_{\rm bind}`$ for every strength.
- Different, the coefficient: there $`I_c-2I_1=-E_{\rm bind}/v_{\max}^2`$, which is $`-\mathfrak m_1\mathfrak m_2E_{\rm bind}`$; here $`-4\mathfrak m_1\mathfrak m_2E_{\rm bind}`$. The factor $`4`$ arises because the upper branch moves by two labels per step (11.11), so $`a=\frac14(1/\mathfrak m_1+1/\mathfrak m_2)`$. With (5.11) the coefficient here is $`4M_1M_2/\tau^4`$ for $`\tau_1=\tau_2`$: it contains the rest costs and is not $`1/v_{\max}^2`$.
- Different, the cost: there, without rest terms, $`I_cv_{\max}^2=\sqrt{U^2+16t^2}=-E_{\min}(t,U)`$ by (21.12), for every $`U`$. Here a rest cost exists, and by (11.17) $`\tau^2\mathfrak m_b`$ does not follow the cost of the pair.
- Different, the notion: (21.15) is an inertia from a response; $`\mathfrak m_b`$ is a curvature.

**(d) Control, no binding.** For $`W=0`$ there is no bound level; the lower edge of $`\mathcal B_{++}(P)`$ is $`e(P)=\min_{p_1}[\omega_1(p_1)+\omega_2(P-p_1)]`$. At the minimum $`\omega_1'(p_1)=\omega_2'(p_2)`$, and for a minimum over a split of $`P`$ the inverse curvatures add. With (6.7), exactly and for all data:

```math
\frac1{e''(0)}=\mathfrak m_1+\mathfrak m_2=\frac{M_1}{\tau_1^2}+\frac{M_2}{\tau_2^2},\qquad e(0)=M_1+M_2,\qquad \langle\sigma^{(i)}_3\rangle=1 .
\qquad\text{(11.18)}
```

For $`\tau_1=\tau_2=\tau`$ the three quantities of (b) agree exactly: $`\tau^2/e''(0)=M_1+M_2`$. For $`\tau_1\neq\tau_2`$ they do not: $`\tau_1^2/e''(0)-(M_1+M_2)=M_2(\tau_1^2/\tau_2^2-1)\neq0`$, and the ratio $`1/[e''(0)(M_1+M_2)]`$ lies strictly between $`\tau_1^{-2}`$ and $`\tau_2^{-2}`$ and depends on $`M_1/M_2`$, hence on the clock levels. So the difference in (b) is caused by the binding, and for $`\tau_1\neq\tau_2`$ the comparison with a cost fails already without one. (11.16) holds for $`\tau_1\neq\tau_2`$ unchanged.

### Step 10. Clocks of the parts (item 5)

**(a)** Start: the clock label of the part $`i`$ in $`\lvert0\rangle=N_i^{-1/2}\sum_k\lvert f_k\rangle`$, the other part on its level $`k_j`$, the medium in $`\chi`$, and the positions and branches in $`\Phi`$ of Step 4, built from the bound eigenvectors of the levels $`(0,k_j)`$ with $`\lvert g\rvert^2`$ of width $`\delta P`$ around $`0`$. The levels are conserved, so the component on $`\lvert f_k\rangle`$ evolves with $`M_i\to m_i+d^{(i)}_k`$.

Class of $`g`$: normalized, with its support in a closed interval $`I_g`$ inside an open interval $`\mathcal P_0\ni0`$ on which the bound level is simple and lies outside the bands for all $`M_i`$ in the range $`[m_i,m_i+d^{(i)}_{N_i-1}]`$ of the levels, with $`\int P\,\lvert g\rvert^2=0`$ and $`\delta P^2:=\int P^2\lvert g\rvert^2`$. The reading of the clock label uses no position label, so (11.19) below holds for every such $`g`$, and the constants of its $`\delta P^2`$ term are maxima over $`I_g`$ of second derivatives in $`P`$. Its term $`O(\kappa)`$ is claimed for $`g\in\mathcal G(\mathcal P_0)`$ of Step 4.

Let $`D_i:=d^{(i)}_{N_i-1}`$ be the spread of the levels of the clock, $`\bar d_i:=\frac1{N_i}\sum_kd^{(i)}_k=\frac{\pi(N_i-1)}{N_i\lambda_{0,i}}=\frac{D_i}2`$ their mean and $`\bar M_i:=m_i+\bar d_i`$ the mean rest cost. Let the bound level at $`P=0`$ be simple and at a distance of at least $`g_0`$ from the rest of the spectrum for all $`M_i\in[m_i,m_i+D_i]`$, and let $`\delta_i:=D_i/g_0`$. By analytic perturbation theory in $`M_i`$ ($`\partial_{M_i}H=\sigma^{(i)}_3`$ has norm one), $`E_b`$ and $`\psi_P`$ are analytic in $`M_i`$ on this range, with $`\lVert\partial_{M_i}\psi_P\rVert\le1/g_0`$, $`\lvert\partial^2_{M_i}E_b\rvert\le2/g_0`$ and $`\partial^n_{M_i}E_b=O(g_0^{1-n})`$. With (11.5), around the mean level:

```math
E^{[k]}_b(P)=\Bigl[E_b(P)+\bigl(d^{(i)}_k-\bar d_i\bigr)\langle\sigma^{(i)}_3\rangle_P+\tfrac12\bigl(d^{(i)}_k-\bar d_i\bigr)^2\,\partial^2_{M_i}E_b(P)\Bigr]_{M_i=\bar M_i}+O\bigl(D_i^3/g_0^2\bigr).
```

For a diagonal on-site binding $`\psi(r)\to\sigma^{(1)}_3\sigma^{(2)}_3\psi(-r)`$ maps $`H(P)`$ to $`H(-P)`$, so $`E_b`$ and $`\langle\sigma^{(i)}_3\rangle_P`$ are even in $`P`$: the pair is at rest up to $`O(\delta P^2)`$, by (11.29) for every $`g`$ of the class above and by (11.8) for $`g\in\mathcal G(\mathcal P_0)`$, and $`\langle\sigma^{(i)}_3\rangle_P=\langle\sigma^{(i)}_3\rangle_0+O(P^2)`$. The reading of the clock label of $`i`$ (the partition by $`a_i`$, (1.3)) has the statistics $`N_i^{-2}\sum_{k,k'}e^{2\pi i(k-k')a/N_i}\langle\Psi_{k'}(\lambda)\vert\Psi_k(\lambda)\rangle`$. Four contributions enter the overlaps.

- **Linear term.** It gives the phases $`e^{-i(d_k-d_{k'})\Gamma_i\lambda}`$ with $`\Gamma_i:=\langle\sigma^{(i)}_3\rangle_0`$ at $`M_i=\bar M_i`$. With $`d^{(i)}_k=\frac{2\pi k}{N_i\lambda_{0,i}}`$ this is $`P_{N_i}`$ of (5.1) exactly.
- **Quadratic term.** It is a phase $`\beta_k`$ with $`\beta_k=\beta_{N_i-1-k}`$ and $`\lvert\beta_k\rvert\le\frac18D_i^2\,\lvert\partial^2_{M_i}E_b\rvert\,\lambda\le\frac\pi2\,\delta_i\,\lambda/\lambda_{0,i}`$. A phase that is even about the middle of the levels changes the statistics only at second order, because $`\sum_k\beta_ke^{ik\phi}`$ and $`\sum_ke^{ik\phi}`$ have the same phase $`e^{i(N_i-1)\phi/2}`$. This is why the level is expanded around $`\bar M_i`$.
- **Cubic term.** It is odd, enters at first order and is $`O(\delta_i^2\,\lambda/\lambda_{0,i})`$.
- **Eigenvector of the start.** The start has on every level the eigenvector of the level $`0`$, which differs from that of the level $`k`$ by at most $`d^{(i)}_k/g_0`$ in norm. This changes the overlaps by $`O(\delta_i^2)`$ for every $`\lambda`$.

In the form of (5.21):

```math
q_i(a;\lambda)=P_{N_i}\Bigl(a;\Gamma_i\frac{\lambda}{\lambda_{0,i}}\Bigr)+\mathcal R_i,\qquad \Gamma_i=\langle\sigma^{(i)}_3\rangle_0\Big\vert_{M_i=\bar M_i}=\frac{\partial E_b(0)}{\partial M_i}\Big\vert_{M_i=\bar M_i},\qquad \mathcal R_i=O\bigl(\delta_i^2(1+\lambda/\lambda_{0,i})^2\bigr)+O\bigl(\delta P^2(1+\lambda/\lambda_{0,i})\bigr)+O(\kappa).
\qquad\text{(11.19)}
```

Expanding $`\Gamma_i`$ around $`M_i=m_i`$, with $`Q_0`$ of (11.9) at $`P=0`$:

```math
\Gamma_i=\Gamma^{(0)}_i+\bar d_i\,\partial^2_{M_i}E_b(0)+O(\delta_i^2),\qquad \Gamma^{(0)}_i:=\langle\sigma^{(i)}_3\rangle_0\Big\vert_{M_i=m_i},\qquad \partial^2_{M_i}E_b(0)=\partial_{M_i}\langle\sigma^{(i)}_3\rangle_0=-2\,\bigl\langle\sigma^{(i)}_3\psi_0\big\vert Q_0\bigl(H(0)-E_b\bigr)^{-1}Q_0\big\vert\sigma^{(i)}_3\psi_0\bigr\rangle .
\qquad\text{(11.25)}
```

- **Rate and ratio.** The rate is $`\Gamma_i/\lambda_{0,i}`$. Its ratio to the rate $`1/\lambda_{0,i}`$ of the free part at rest ((5.21) with $`\Gamma(0)=1`$) is $`\Gamma_i\le1`$: the expectation value $`\langle\sigma^{(i)}_3\rangle_0`$ of item 2(a), taken at the mean rest cost $`\bar M_i`$ of the part $`i`$ and on the level $`k_j`$ of the other part. (11.25) is the rate to first order in the level spacing. Applied to one free body, with $`\omega_0(p_0)`$ at the rest cost $`\mu`$ in place of $`E_b`$, it gives $`\gamma\bigl[1+\frac{(N-1)\epsilon}2(1-\gamma^2)\bigr]`$ of (5.21), where $`\frac{(N-1)\epsilon}2=\bar d/m`$.
- **Two orders.** The level to first order in $`d^{(i)}_k`$ gives only $`\Gamma^{(0)}_i`$, the rate to zeroth order: the advance $`\Gamma_i\lambda/\lambda_{0,i}`$ is then wrong by $`\bar d_i\,\partial^2_{M_i}E_b\,\lambda/\lambda_{0,i}`$, which is of first order in $`\delta_i`$. The rate to first order in the level spacing needs the level to second order in $`d^{(i)}_k`$: a sum over the rest of the spectrum, as in (11.9).
- **Range of $`\lambda`$.** $`\mathcal R_i`$ is small for $`\delta_i\ll1`$ on $`0\le\lambda\ll\lambda_{0,i}/\delta_i`$, with $`\delta P^2\lambda/\lambda_{0,i}\ll1`$ and $`\kappa\to0`$ at fixed $`\lambda`$. On $`\lambda_{0,i}\lesssim\lambda\ll\lambda_{0,i}/\delta_i`$ the first-order term of (11.25) changes the statistics by more than $`\mathcal R_i`$. The condition $`\delta_i\ll1`$ is sufficient, not necessary (see (b)).

Class: every diagonal on-site binding and every bound level at $`P=0`$ that is simple for all $`M_i`$ in the range of the levels. Status: the rate to first order in the level spacing; the statistics up to the remainder $`\mathcal R_i`$, which is of second order.

**(b)** With (11.14), at leading order in $`\mathsf R`$ (remainder $`O(\epsilon^4)`$), with $`M_i=\bar M_i`$ and $`M_j=M^{(j)}_{k_j}`$:

```math
\Gamma_i=1-\frac{\tau_i^2}{4M_i^2}\,\Lambda,\qquad \Lambda=1+\frac{\varsigma}{\sqrt{1+u^2}},\qquad \frac{1-\Gamma_1}{1-\Gamma_2}=\frac{\tau_1^2/M_1^2}{\tau_2^2/M_2^2}.
\qquad\text{(11.20)}
```

To first order in the level spacing, with $`a_i`$, $`a`$, $`u`$, $`\Lambda`$ taken at $`M_i=m_i`$:

```math
\Gamma_i=1-\frac{\tau_i^2}{4m_i^2}\Bigl[\Lambda-\frac{\bar d_i}{m_i}\Bigl(2\Lambda+\varsigma\,\frac{a_i}{a}\,\frac{u^2}{(1+u^2)^{3/2}}\Bigr)\Bigr]+O\Bigl(\frac{a_i\,\bar d_i^{\,2}}{m_i^3}\Bigr)+O(\epsilon^4).
\qquad\text{(11.26)}
```

This is (11.25) with $`\partial^2_{M_i}E_b(0)=\frac{a_i}{M_i^2}\bigl[2\Lambda+\varsigma\frac{a_i}{a}\frac{u^2}{(1+u^2)^{3/2}}\bigr]`$, from (11.12) and $`\partial_{M_i}a=-a_i/M_i`$. In $`\mathsf R`$ the bounds through $`g_0=O(\epsilon^2)`$ are not sharp. By (11.12), (11.13) and the analyticity used in Step 8, $`E_b-M_1-M_2`$ and $`\psi_0`$ depend on $`M_i`$ on the scale $`M_i`$: $`\partial^n_{M_i}E_b=O(a_i/M_i^{\,n})`$ for $`n\ge2`$ and $`\lVert\partial_{M_i}\psi_0\rVert=O(1/M_i)`$. So $`\mathcal R_i`$ of (11.19) holds with $`\delta_i`$ replaced by $`D_i/M_i`$, also for $`D_i\gg g_0`$. (11.26) and these bounds are for fixed hatted data, hence a fixed $`u\in(0,\infty)`$; their constants are not bounded here for $`u\to0`$ or $`u\to\infty`$.

Both clocks are slowed. They are not slowed by the same factor: $`\Lambda`$ is common, and the factors agree at this order if and only if $`\tau_1/M_1=\tau_2/M_2`$ (for example equal data). The third relation of (11.20) compares the two ratios at one pair $`(M_1,M_2)`$. The two readings are two starts, with the pairs $`(\bar M_1,M^{(2)}_{k_2})`$ and $`(M^{(1)}_{k_1},\bar M_2)`$, which changes the relation by relative terms of first order in $`d^{(i)}_k/M_i`$. For a wide pair with $`w_{11}<0`$, $`1-\Gamma_i=\frac{\tau_i^2}{8M_i^2}u^2`$; for a tight pair $`1-\Gamma_i=\frac{\tau_i^2}{4M_i^2}(1+\frac aw)`$. Without a binding $`\Gamma_i=1`$. The wide and the tight form are ordered limits (Step 8): the coefficient $`\frac{\tau_i^2}{4M_i^2}\Lambda(u)`$ of (11.20) is obtained first, for $`\epsilon\to0`$ at fixed $`u`$, and then $`\Lambda(u)`$ is expanded for $`u\to0`$ or $`u\to\infty`$; no joint limit is derived.

## Result

Classes, regimes and statuses. Every result refers to $`C_{\rm bod}`$ of (11.21), under the assumption $`\langle\chi\vert X\vert\chi\rangle=0`$. Items 1 and 2 hold for every $`W\in\mathcal W`$, all data, every bound level and every $`P\in\mathcal P`$ at which the level lies outside the bands; they are exact. By (11.27) this is every $`P\in\mathcal P`$ except a flat value (equal data, $`P\in\{0,\pi\}`$, $`E_b=0`$), where only (11.6) is derived. For a simple level they are (11.5)–(11.9); for a degenerate level they hold in the form of Step 5a, (11.23) and (11.24). Item 3(a) and the control 4(d) are exact, for every diagonal on-site binding (4(d): no binding) and all data. Items 3(b)–(d), 4(a)–(c) and 5(b) hold for every diagonal on-site binding in $`\mathsf R`$ at leading order, with the remainders stated, at fixed hatted data. Their wide-pair and tight-pair forms are ordered limits: first $`\epsilon\to0`$ at fixed $`u`$, then $`u\to0`$ or $`u\to\infty`$ in the leading coefficient. A joint range of $`\epsilon`$ and $`u`$ is derived for the level $`E_b(P)`$ only, under the sufficient conditions (11.30). Item 5(a) holds for every diagonal on-site binding and all data, for a bound level at $`P=0`$ that is simple over the range of the levels of the clock: the rate to first order in the level spacing, the statistics up to a remainder of second order.

1. **Structure.** $`H(P)`$ is (11.1), with the convention $`\eta`$. The two-body bands and their edges at $`P=0`$ are (11.2), for every $`W`$. A band is a single point if and only if the data are equal and $`P\in\{0,\pi\}`$ (11.27). A bound level lies outside the bands, with finite multiplicity, at every $`P`$ of its interval except possibly such a point with the value $`0`$; near it (11.28) holds, and a continuous member of $`\mathcal W`$ with such a value exists (Step 1a). The replacements are (11.3); the range condition fixes $`U`$, and every single-object term can still be listed in a body term or in a record term (within the stated forms: only constants). The operator to which the results refer is $`C_{\rm bod}`$ (11.21). The seven answers are (11.4).
   - Computed from the listed terms, only $`W(r)`$ is well defined.
   - Computed from $`C_{\rm bod}`$: $`W(r)`$ yes; $`M_i`$ yes as half the gap, no as a cost of $`b_i`$; $`E_b(P)`$ yes as a total cost (1.8) only; $`E_b(P)-(M_1+M_2)`$, $`E_b(P)-E_b(0)`$, $`E_b''(0)`$ and $`\langle\sigma^{(i)}_3\rangle_P`$ yes.
   - The expression $`E_b(P)-(M_1+M_2)`$. Formed from the listed pair contract and the listed coefficients: not well defined. Formed from $`C_{\rm bod}`$ (the eigenvalue of its fibre and the half gaps): well defined under every replacement (11.3), and for the $`C`$ of the question equal to the distance $`E_{\rm bind}(P)`$ from the band edge (11.22). A constant $`c`$ added to $`C`$ is not a replacement (11.3); it changes this expression by $`c`$ and leaves $`E_{\rm bind}(P)`$ of (11.22) unchanged.
2. **Exact relations.** The five derivatives are (11.5) and the scaling relation is (11.6). $`E_b'(P)=\langle V_1\rangle_P=\langle V_2\rangle_P`$ (11.7). In a state built from the bound level on an interval $`\mathcal P_0`$ where it is simple and outside the bands, the two bodies have the same mean velocity: for every normalized $`g`$ supported in $`\mathcal P_0`$ the two velocity operators have the expectation value $`\int\lvert g\rvert^2E_b'`$ (11.29); for $`g`$ of the class $`\mathcal G(\mathcal P_0)`$ the mean position labels exist and both change at this rate, which is $`E_b'(P_0)+O(\delta P^2)`$ (11.8). $`E_b''(P)`$ is (11.9). For a degenerate level: (11.6), $`\langle V_1\rangle=\langle V_2\rangle`$ and the mean rule of (11.23) hold for every eigenvector; (11.5) and (11.7) hold for the branch vectors of the parameter that is varied (11.23); (11.24) replaces (11.9); a state built from one level, with $`g`$ of the classes named, has equal mean velocities of the two bodies.
3. **Diagonal on-site binding.** The equation is (11.10), exact for all data. In $`\mathsf R`$: a bound level at a distance of order $`\epsilon^2`$ from $`\mathcal B_{++}`$ exists iff $`\hat w_{11}\neq0`$, it is one, with $`E_b(P)`$ of (11.12) (remainder $`O(\epsilon^4)`$) and $`\psi_P`$ of (11.13) (up to $`O(\epsilon)`$; at $`j(P)=0`$ it is $`\delta_{r,0}\lvert11\rangle`$), from the effective contract (11.11); only $`w_{11}`$ enters ($`w_{22}`$ at order $`\epsilon^6`$). The five leading terms are (11.14), the limits (11.15), as ordered limits. For the level itself (11.30) gives a sufficient joint range: $`u^2\ge K\epsilon^2`$ for a wide pair, $`u\le\epsilon^{-2}/K`$ for a tight pair.
4. **Curvature, inertias, cost.** $`\mathfrak m_b=\mathfrak m_1+\mathfrak m_2-4\mathfrak m_1\mathfrak m_2E_{\rm bind}`$ (11.16), relative remainder $`O(\epsilon^2)`$, at every fixed $`u`$. For $`\tau_1=\tau_2`$, $`\tau^2\mathfrak m_b`$ differs from the cost of the pair and from $`\sum_iM_i\langle\sigma^{(i)}_3\rangle_0`$ at order $`\epsilon^0`$, by $`-\frac{4M_1M_2}{\tau^2}E_{\rm bind}`$ (11.17). The comparison with 03-ilang-space/21-composite-body is Step 9(c). The control without a binding is (11.18), exact.
5. **Clocks.** The statistics are (11.19), with the ratio $`\Gamma_i=\langle\sigma^{(i)}_3\rangle_0`$ at the mean rest cost $`\bar M_i`$, for every normalized $`g`$ of mean $`0`$ with support in a closed interval inside $`\mathcal P_0`$ (the term $`O(\kappa)`$ for $`g\in\mathcal G(\mathcal P_0)`$). To first order in the level spacing the ratio is (11.25). The remainder is of second order in $`\delta_i`$ and small for $`\lambda\ll\lambda_{0,i}/\delta_i`$. In $`\mathsf R`$, $`\Gamma_i`$ is (11.20) at $`M_i=\bar M_i`$, and (11.26) to first order in the level spacing, both at fixed $`u`$: the two clocks are not slowed by the same factor unless $`\tau_1/M_1=\tau_2/M_2`$.

Controls (M9). (11.5)–(11.9) are proven for every simple level of the class and (11.23), (11.24) for every degenerate one, at every $`P`$ where the level lies outside the bands, so no member violates them there. The member of Step 1a is the control for the exception: at its flat value $`E_b'(0)`$ does not exist. (11.9) fails for a degenerate level, and (11.19) with $`\Gamma^{(0)}_i`$ in place of $`\Gamma_i`$ fails at first order (sets X and the clock runs under "Code"). (11.8) fails as a statement on mean position labels for a normalized $`g`$ with a sharp cutoff, while (11.29) holds (Step 4). An operator read from the listed terms fails as the operator of the two bodies in a listing that differs by a single-object term (Step 2; the last check of Part 2 under "Code"). The leading-order results fail outside $`\mathsf R`$: for $`\tau_i/M_i`$ of order one the closed forms (11.14) are off by $`8`$ per cent ($`E_b''(0)`$) to $`23`$ per cent ($`\langle U\rangle_0`$) (set E under "Code"). At a fixed $`\epsilon`$ the wide form of $`E_{\rm bind}`$ for $`w_{11}>0`$ fails for $`u`$ of the order of $`\epsilon`$, and the tight forms fail for $`\lvert w_{11}\rvert`$ of the order of $`M`$ (Part 3 under "Code"). Further controls: no binding (11.18), $`\tau_1\neq\tau_2`$ (Step 9d), wide against tight (11.15).

## Consistency checks

1. **Dimensions.** $`\tau_i`$, $`M_i`$, $`w`$, $`a_i`$, $`j`$, $`E_b`$, $`E_b''`$ are costs ($`P`$ and $`q`$ are numbers); $`u`$, $`\rho`$, $`\Lambda`$, $`\langle\sigma^{(i)}_3\rangle`$, $`\Gamma_i`$ are numbers; $`\mathfrak m`$ is an inverse cost, and so is $`\mathfrak m_1\mathfrak m_2E_{\rm bind}`$ in (11.16); $`\Gamma_i\lambda/\lambda_{0,i}`$ in (11.19) is a number. $`D_i`$, $`\bar d_i`$, $`g_0`$ are costs, $`\delta_i`$ and $`\bar d_i\,\partial^2_{M_i}E_b`$ in (11.25) are numbers. Passed.
2. **No binding.** For $`w\to0^-`$, (11.12) tends to $`M_1+M_2+a-j(P)`$, the lower edge of $`\mathcal B_{++}(P)`$ at this order, and (11.14) gives $`E_b''(0)\to4a_1a_2/a=1/(\mathfrak m_1+\mathfrak m_2)`$, which is (11.18), with $`\langle\sigma^{(i)}_3\rangle_0\to1`$, $`\langle A_i\rangle_0\to0`$, $`\langle U\rangle_0\to0`$, $`\Gamma_i\to1`$ (an ordered limit in the sense of Step 8: the limit $`u\to0`$ of the leading-order forms). Passed.
3. **Scaling relation on the closed form.** With (11.14) the right side of (11.6) at $`P=0`$ is $`M_1+M_2-a\Lambda+2a\Lambda+\varsigma\frac{w^2}{\sqrt{w^2+a^2}}=M_1+M_2+a+\varsigma\frac{a^2+w^2}{\sqrt{w^2+a^2}}=E_b(0)`$ of (11.12). Passed.

## Open issues

- Whether $`\mathfrak m_b`$ is the inertia of the pair in a response to a gradient is not derived here (not asked; (11.17) shows that it is not the cost divided by $`\tau^2`$).
- Outside the order asked in item 3(b): bound levels closer than $`O(\epsilon^4)`$ to the band (for $`\hat w_{11}=0`$, and in the sector $`\Xi=-1`$) are neither established nor excluded.
- The coefficients of the $`O(\epsilon^4)`$ remainders are not derived; the code only confirms their order.
- (11.19) is derived for a bound level that stays simple over the range of the levels of the clock. The condition $`D_i\ll g_0`$ is sufficient; in $`\mathsf R`$, where $`g_0`$ is of order $`\epsilon^2`$, it is replaced by $`D_i\ll M_i`$ (Step 10b). Item 5 for a level that is degenerate at some $`M_i`$ in that range is not derived.
- The results refer to $`C_{\rm bod}`$ under the assumption $`\langle\chi\vert X\vert\chi\rangle=0`$. Without it they hold at leading order in $`\kappa`$ only; the uniform gradient $`\kappa\langle X\rangle(\hat x_1+\hat x_2)`$ is a position-dependent term and is not treated (out of scope).
- $`E_b(P)`$ is well defined only as a total cost of the given $`C`$. Whether the zero of the total cost has any content (a constant in $`C`$ changes no reading) is not a question of this package.
- Flat values (Step 1a). At a flat value only (11.6) is derived; the other relations of item 2 are not. Whether a bound level can have a flat value and be differentiable there is open; by (11.28) its derivative would be at least $`\Omega-M`$ in absolute value.
- No joint limit in $`\epsilon`$ and $`u`$ is derived for $`E_b''(0)`$, the expectation values, $`\mathfrak m_b`$ and $`\Gamma_i`$. (11.30) is sufficient and, by the code, not necessary; the numbers $`c`$, $`\varepsilon_0`$ and $`K`$ are not computed.
- The class $`\mathcal G(\mathcal P_0)`$ is sufficient for the mean position labels. The largest class of $`g`$ for which they exist is not determined.

## Code

`code/v3/check_bound_pair.py` (role: check; outputs `code/v3/output/check_bound_pair.txt`, a log, and `code/v3/output/check_bound_pair.json`, all numbers). Parts 1 and 2 are the script of v2, unchanged; the first 230 lines of the log are identical to `code/v2/output/check_bound_pair.txt`. Part 3 checks what is new in v3. The whole script runs in about 7 minutes (404 s in the run that produced the outputs). The script builds $`H(P)`$ of (11.1) with $`\eta=\frac12`$ on $`r=-L,\dots,L`$ with open ends and diagonalizes it: densely, once per set and $`P`$ (all eigenvectors, needed for (11.9)), and with a banded shift-and-invert solver for the finite differences and the doubled range. The bound level is the eigenvector of largest weight on $`(r=0,\lvert11\rangle)`$. Derivatives of $`E_b`$ are five-point differences (step $`0.01`$ in $`P`$, relative step $`10^{-3}`$ in $`M_i`$, $`\tau_i`$, $`\theta`$). Nothing in the derivation rests on the code, except the statement of Step 5a and the statement of Step 8 that are marked there.

**Part 1 (the check of v1).**

- **Range of $`r`$ and convergence.** $`L=120`$ ($`964`$ components). Convergence was checked in two ways: $`E_b`$ at $`L=240`$ differs by less than $`10^{-13}`$, and the weight of $`\psi_P`$ at $`\lvert r\rvert>60`$ is at most $`5\times10^{-8}`$ (set D) and below $`10^{-19}`$ otherwise. $`E_b`$ at $`\eta=0,0.3,1`$ and from the two solvers agrees to $`10^{-13}`$.
- **Parameter sets** ($`M_1,M_2;\ \tau_1,\tau_2;\ w_{11}`$; the other three $`w_{s_1s_2}`$ are non-zero and of the same order), each at $`P\in\{0,\pm0.15,\pm0.30\}`$: A $`(1,1;\ 0.1,0.1;\ -0.004)`$, equal data; B $`(1,1.7;\ 0.2,0.12;\ -0.01)`$; C $`(1,0.8;\ 0.1,0.15;\ +0.02)`$, level above the band; D $`(1.3,1;\ 0.15,0.2;\ -0.004)`$, wide; E $`(1,1.3;\ 1,0.8;\ -0.6)`$, $`\tau_i/M_i`$ of order one. In all sets the level is outside the bands and has $`\langle\Xi\rangle_P=+1`$ (`Gamma` in Part 1 of the output files; in Part 2 the keys `Gamma_...` are the ratios $`\Gamma_i`$).
- **Exact relations, all five sets and all $`P`$** (largest absolute deviation): (11.5) derivatives against expectation values, below $`10^{-10}`$; (11.6), below $`10^{-14}`$; (11.7) $`E_b'`$ against $`\langle V_1\rangle_P`$ and $`\langle V_2\rangle_P`$, below $`2\times10^{-10}`$ (below $`10^{-11}`$ in A–D), and $`\langle V_1\rangle_P-\langle V_2\rangle_P`$ below $`10^{-15}`$; (11.9) against the difference quotient, below $`10^{-9}`$; (11.10): the coefficients against a direct inversion of $`h_P(q)-E`$, relative deviation below $`10^{-12}`$, and the root of $`F_+`$ against $`E_b`$, below $`10^{-14}`$. These are the sizes of the rounding and truncation errors of the differences.
- **Closed forms, sets in $`\mathsf R`$.**

| set | $`\max_i\tau_i/M_i`$ | $`u`$ | $`\max_P\lvert E_b-(11.12)\rvert`$ | the same over $`(\max\tau_i/M_i)^4`$ | rel. deviation of $`E_b''(0)`$ | the same over $`(\max\tau_i/M_i)^2`$ |
| --- | --- | --- | --- | --- | --- | --- |
| A | 0.10 | 0.80 | $`2.1\times10^{-6}`$ | 0.021 | $`3.2\times10^{-4}`$ | 0.032 |
| B | 0.20 | 0.83 | $`8.3\times10^{-6}`$ | 0.005 | $`5.4\times10^{-4}`$ | 0.014 |
| C | 0.19 | 2.10 | $`2.0\times10^{-4}`$ | 0.164 | $`1.7\times10^{-2}`$ | 0.47 |
| D | 0.20 | 0.28 | $`7.7\times10^{-7}`$ | 0.0005 | $`3.6\times10^{-5}`$ | 0.001 |
| E (control) | 1.0 | 1.61 | $`4.6\times10^{-2}`$ | 0.046 | $`7.7\times10^{-2}`$ | 0.077 |

  The expectation values of (11.14) agree with the numerical ones to $`2.1\times10^{-5}`$ (A, B, D) and $`5.3\times10^{-4}`$ (C), a fraction of $`(\tau_i/M_i)^2`$ of their leading terms. (11.16), $`\mathfrak m_b-(\mathfrak m_1+\mathfrak m_2)`$ against $`-4\mathfrak m_1\mathfrak m_2E_{\rm bind}`$ with the numerical $`E_{\rm bind}`$: A $`56.043`$ against $`56.045`$; B $`42.321`$ against $`42.326`$; C $`-455.96`$ against $`-447.76`$ ($`\mathfrak m_b<0`$); D $`3.169`$ against $`3.161`$.
- **Next order in $`\epsilon`$** (set B with $`\tau_i\to\epsilon'\tau_i`$, $`w_{s_1s_2}\to\epsilon'^2w_{s_1s_2}`$, $`\epsilon'=1,\frac12,\frac14,\frac18`$): each halving of $`\epsilon'`$ divides $`E_b-(11.12)`$ by $`16.00`$ (at $`P=0`$ and at $`P=0.3`$), $`\langle\sigma^{(i)}_3\rangle_0-(11.14)`$ by $`15.6`$ to $`16.0`$, and the relative deviation of $`E_b''(0)`$ by $`3.97`$ to $`4.00`$. The remainders are of order $`\epsilon^4`$, and of relative order $`\epsilon^2`$ for $`E_b''(0)`$, as stated.
- **Control E.** Outside $`\mathsf R`$ the exact relations hold as above, while $`E_{\rm bind}=-0.288`$ against $`-0.333`$ from (11.14) and $`E_b''(0)`$ is off by $`7.7`$ per cent.

**Part 2 (new in v2; its labels I1–I5 are the issues of external round 1).**

- **I3, clock of a part: (11.19), (11.25), (11.26).** For each of the $`N_i`$ levels $`M_i=m_i+d^{(i)}_k`$ the matrix $`H(0)`$ is diagonalized, the eigenvector of the level $`0`$ is evolved on every level, and the exact statistics $`q_i(a;\lambda)`$ are formed (total label $`P=0`$ sharp, no records). They are compared with $`P_{N_i}(a;\Gamma\lambda/\lambda_{0,i})`$ at $`\lambda/\lambda_{0,i}=0.25,0.5,\dots,2N_i`$; the deviation is the largest $`\lvert q_i-P_{N_i}\rvert`$ over $`a`$ and $`\lambda`$. $`\Gamma_i`$ is $`\langle\sigma^{(i)}_3\rangle_0`$ at $`\bar M_i`$, $`\Gamma^{(0)}_i`$ the same at $`m_i`$ (the rate of v1), and (11.25) uses the sum over the rest of the spectrum.

| set, part, $`N_i`$ | $`D_i`$ | $`D_i/g_0`$ | $`\Gamma^{(0)}_i`$ | $`\Gamma_i`$ | (11.25) | deviation with $`\Gamma_i`$ | deviation with $`\Gamma^{(0)}_i`$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E, 1, 4 | 0.06 | 0.21 | 0.856470 | 0.862190 | 0.862334 | $`9.5\times10^{-4}`$ | $`7.1\times10^{-2}`$ |
| E, 1, 4 | 0.03 | 0.10 | 0.856470 | 0.859366 | 0.859402 | $`2.5\times10^{-4}`$ | $`3.6\times10^{-2}`$ |
| E, 1, 4 | 0.015 | 0.05 | 0.856470 | 0.857927 | 0.857936 | $`6.1\times10^{-5}`$ | $`1.8\times10^{-2}`$ |
| B, 1, 4 | 0.10 | 27.9 | 0.9977124 | 0.9978094 | 0.9978119 | $`4.7\times10^{-4}`$ | $`1.4\times10^{-3}`$ |
| B, 1, 4 | 0.05 | 13.9 | 0.9977124 | 0.9977615 | 0.9977621 | $`1.3\times10^{-4}`$ | $`5.9\times10^{-4}`$ |
| B, 1, 4 | 0.025 | 7.0 | 0.9977124 | 0.9977371 | 0.9977373 | $`3.3\times10^{-5}`$ | $`3.0\times10^{-4}`$ |
| B, 2, 5 | 0.10 | 27.9 | 0.9997133 | 0.9997276 | 0.9997282 | $`7.3\times10^{-6}`$ | $`2.2\times10^{-4}`$ |
| B, 2, 5 | 0.05 | 13.9 | 0.9997133 | 0.9997206 | 0.9997208 | $`1.9\times10^{-6}`$ | $`1.1\times10^{-4}`$ |
| B, 2, 5 | 0.025 | 7.0 | 0.9997133 | 0.9997170 | 0.9997170 | $`4.9\times10^{-7}`$ | $`5.7\times10^{-5}`$ |

  Each halving of the spread at fixed $`\lambda/\lambda_{0,i}`$ divides the deviation with $`\Gamma_i`$ by $`3.6`$ to $`4.1`$ (second order) and the deviation with $`\Gamma^{(0)}_i`$ by $`1.9`$ to $`2.4`$ (first order). A least-squares fit of the rate gives $`0.862146`$ (E, $`D_i=0.06`$) and $`0.9977620`$ (B, part 1, $`D_i=0.05`$). In set B the spread is far above $`g_0=0.0036`$ and the remainder is small all the same, as stated in Step 10(b) with $`D_i/M_i`$. In $`\mathsf R`$ (set B): $`\partial^2_{M_i}E_b(0)`$ is $`1.990\times10^{-3}`$ against $`1.996\times10^{-3}`$ from (11.26) (part 1) and $`2.976\times10^{-4}`$ against $`2.952\times10^{-4}`$ (part 2); (11.20) at $`\bar M_1`$ gives $`0.9978101`$ against $`0.9978094`$ ($`D_1=0.10`$).
- **I4, order of $`w_{22}`$** (set B scaled as above, $`\epsilon'=2,1,\frac12,\frac14`$): $`E_b`$ with $`w_{22}`$ minus $`E_b`$ with $`w_{22}=0`$ is $`2.9\times10^{-7}`$, $`4.4\times10^{-9}`$, $`6.9\times10^{-11}`$, $`1.1\times10^{-12}`$. Each halving divides it by $`64.5`$, $`64.1`$, $`64.2`$ (order $`\epsilon^6`$) and the weight $`\lvert\langle22\vert\psi_0(0)\rangle\rvert^2`$ by $`16.1`$, $`16.0`$, $`16.0`$ (order $`\epsilon^4`$); the difference agrees with $`w_{22}\lvert\langle22\vert\psi_0(0)\rangle\rvert^2`$ to four digits or better for $`\epsilon'\ge\frac12`$, and to two digits at $`\epsilon'=\frac14`$, where it is near the rounding error.
- **I5, $`j(P)=0`$** (set A, $`a_1=a_2`$, at $`P=\frac\pi2`$, $`\epsilon'=1,\frac12,\frac14`$): $`E_b-(M_1+M_2+a+w_{11})`$ is $`6.2\times10^{-7}`$, $`3.9\times10^{-8}`$, $`2.4\times10^{-9}`$ (ratios $`16.0`$); one minus the weight on $`(r=0,\lvert11\rangle)`$ is $`2.5\times10^{-3}`$, $`6.2\times10^{-4}`$, $`1.6\times10^{-4}`$ (ratios $`4.0`$, the $`O(\epsilon)`$ part of the eigenvector); the weight of $`\lvert11\rangle`$ at $`r\neq0`$ is $`3\times10^{-7}`$ at $`\epsilon'=1`$.
- **I2, twofold levels: (11.23), (11.24)** (set X: $`M=(1,0.7)`$, $`\tau=(0.5,0.35)`$, $`E_0=1`$, the on-site binding $`W_0=-G(E_0,P_0)^{-1}`$ on the span of $`\lvert11\rangle`$, $`\lvert22\rangle`$, which is not diagonal, with $`w_{12}=0.15`$, $`w_{21}=-0.10`$; at $`P_0=0.3`$ and at $`P_0=0`$). The two eigenvalues at $`E_0`$ differ by less than $`4\times10^{-15}`$ and are $`0.54`$ away from the next one.
  - (11.23): the eigenvalues of $`\Pi_b(\partial_\xi H)\Pi_b`$ against the slopes of the two branches (five-point differences, the branches followed by their overlap with the branch vectors): below $`10^{-11}`$ for $`M_i`$, $`\tau_i`$, $`\theta`$ and $`3\times10^{-10}`$ for $`P`$.
  - (11.24) against the second differences of the branches: below $`5\times10^{-10}`$. At $`P_0=0`$ both first derivatives in $`P`$ vanish, the branch vectors come from the second-order matrix, and $`E''=-0.1063`$ and $`+0.1929`$.
  - (11.9) with $`Q_P`$: at $`P_0=0.3`$ the term of the other vector of the level is $`6.5\times10^{-4}`$ divided by $`2\times10^{-15}`$.
  - Every eigenvector (five random vectors of the level): the residual of (11.6) is $`2\times10^{-15}`$, $`\langle V_1\rangle-\langle V_2\rangle`$ is $`10^{-16}`$, and $`\lVert\Pi_b(V_1-V_2)\Pi_b\rVert`$ is $`2\times10^{-16}`$.
  - The six matrices do not commute: at $`P_0=0.3`$ the first branch vector of $`M_1`$ has the squared overlap $`0.28`$ with that of $`\tau_1`$ and $`0.51`$ with that of $`P`$. In the branch vectors of $`M_1`$, $`\langle U\rangle`$ is $`+2.0135`$ and $`-0.7226`$, against the slopes $`+2.0170`$ and $`-0.7261`$ of the branches of $`\theta`$.
- **I1, the operator (11.21)** (a small system given in the places: two bodies with a branch label on an open chain of four positions, a medium with three places, a random $`X`$ and $`\chi`$, $`\lambda=3`$). Listing B lists $`h\,\sigma^{(1)}_3`$, a constant and a part of the motion term of $`b_2`$ in the record terms. $`C_{\rm bod}`$ of the two listings agrees to $`10^{-15}`$, while the listed pair term of B differs from it by $`2.6`$ in norm. The view of the two bodies against the evolution by $`C_{\rm bod}`$: $`4.1\times10^{-2}`$, $`1.05\times10^{-2}`$, $`2.6\times10^{-3}`$ for $`\kappa=0.04,0.02,0.01`$ (ratios $`3.9`$, $`4.0`$: second order). With a medium that is not centred, $`C_{\rm bod}`$ minus the listed $`C_{\rm pair}`$ is the gradient of (11.21) to $`10^{-15}`$, and the view against the evolution by the listed $`C_{\rm pair}`$ is $`0.153`$, $`0.074`$, $`0.037`$ (ratios $`2.05`$, $`2.01`$: first order).

**Part 3 (new in v3; I3 and I2 of external round 2).** For the wide pair the level is taken on the infinite chain, as the root of $`F_+`$ of (11.10) with the integrals over $`q`$ as means over $`2^{15}`$ values and the level measured from $`M_1+M_2`$ without cancellation; a pair with $`u\le\frac1{16}`$ does not fit into $`L=120`$. For $`u=1`$ and $`u=\frac12`$, both signs of $`w_{11}`$, the root agrees with the dense diagonalization at $`L=120`$ to $`10^{-14}`$. Data: set B with $`w_{11}=\mp u\,a`$ and the other three $`w_{s_1s_2}`$ of set B. Here $`\epsilon`$ stands for $`\max_i\tau_i/M_i=0.2`$, and every run is repeated at $`0.1`$ ($`\tau_i\to\tau_i/2`$, $`w_{12},w_{21},w_{22}\to`$ a quarter).

- **I3, wide pair.** "Remainder" is the level minus (11.12); "isolation" is the distance of the level from the exact band edge. $`\epsilon=0.2`$:

| $`u`$ | $`\epsilon^2/u^2`$ | remainder over isolation, $`w_{11}<0`$, $`P=0`$ | the same, $`w_{11}<0`$, $`P=\frac\pi2`$ | the same, $`w_{11}>0`$, $`P=0`$ | rel. deviation of the two sides of the second equality of (11.16) |
| --- | --- | --- | --- | --- | --- |
| 2 | 0.01 | $`3.9\times10^{-3}`$ | $`3.7\times10^{-3}`$ | 0.018 | $`-4.4\times10^{-3}`$ |
| 1 | 0.04 | $`2.6\times10^{-3}`$ | $`2.1\times10^{-3}`$ | 0.045 | $`-6.1\times10^{-4}`$ |
| 1/2 | 0.16 | $`1.5\times10^{-3}`$ | $`3.9\times10^{-4}`$ | 0.15 | $`+5.4\times10^{-4}`$ |
| 1/4 | 0.64 | $`7.3\times10^{-4}`$ | $`7.2\times10^{-3}`$ | 0.55 | $`+6.8\times10^{-4}`$ |
| 1/8 | 2.6 | $`3.6\times10^{-4}`$ | 0.034 | 2.2 | $`+5.8\times10^{-4}`$ |
| 1/16 | 10 | $`1.8\times10^{-4}`$ | 0.14 | 8.6 | $`+4.8\times10^{-4}`$ |
| 1/32 | 41 | $`8.8\times10^{-5}`$ | 0.58 | 34 | $`+4.1\times10^{-4}`$ |
| 1/64 | 164 | $`4.4\times10^{-5}`$ | 2.3 | 137 | $`+3.7\times10^{-4}`$ |
| 1/128 | 655 | $`2.2\times10^{-5}`$ | 9.3 | 546 | $`+3.4\times10^{-4}`$ |

  - $`w_{11}<0`$, $`P=0`$: the remainder stays far below the isolation for every $`u`$. The third column is also the relative deviation of $`E_{\rm bind}`$ from (11.14); at $`\epsilon=0.1`$ it is $`4.0`$ times smaller in every row. So (11.30) is not necessary. The two sides of the second equality of (11.16) (the numerical $`E_{\rm bind}`$, and $`E_b''(0)`$ from five-point differences of the roots) differ by less than $`7\times10^{-4}`$ for $`u\le\frac12`$, and by $`3.9`$ to $`4.6`$ times less at $`\epsilon=0.1`$.
  - $`w_{11}<0`$, $`P=\frac\pi2`$: the remainder tends to $`-5.26\times10^{-6}`$ ($`-3.29\times10^{-7}`$ at $`\epsilon=0.1`$; ratio $`16.0`$, order $`\epsilon^4`$). It exceeds the isolation for $`u\le\frac1{64}`$ (at $`\epsilon=0.1`$: for $`u=\frac1{128}`$), and there the value of (11.12) lies above the exact lower band edge.
  - $`w_{11}>0`$, $`P=0`$: the remainder tends to $`-2.01\times10^{-4}`$ ($`-1.28\times10^{-5}`$ at $`\epsilon=0.1`$; ratio $`15.8`$). It exceeds the isolation for $`u\le\frac18`$ (at $`\epsilon=0.1`$: for $`u\le\frac1{16}`$), and there $`E_{\rm bind}-2a`$ is negative, against $`+\frac{w^2}{2a}`$ of (11.15). The distance of the level from the exact upper edge agrees with $`\sqrt{w^2+a^2}-a`$ to $`0.5`$ per cent ($`0.13`$ per cent at $`\epsilon=0.1`$) for every $`u`$.
- **I3, tight pair** ($`w_{11}=-u\,a`$, $`u=2,4,\dots,128`$, dense diagonalization at $`L=120`$, $`P=0`$). The relative deviation of $`E_{\rm bind}-w_{11}`$ from (11.14) is $`0.26`$ to $`0.56`$ times $`\lvert w_{11}\rvert/M`$ for $`\lvert w_{11}\rvert/M\le0.39`$, at both $`\epsilon`$ (for example $`4.0\times10^{-2}`$ and $`4.5\times10^{-2}`$ at $`\lvert w_{11}\rvert/M=0.097`$). That of $`E_b''(0)`$ is $`0.19`$ to $`0.41`$ times $`\lvert w_{11}\rvert/M`$, and that of $`1-\langle\sigma^{(1)}_3\rangle_0`$ is $`0.4`$ to $`1.4`$ times $`\lvert w_{11}\rvert/M`$. At $`\lvert w_{11}\rvert/M=1.55`$ ($`\epsilon=0.2`$, $`u=128`$) the forms fail: $`E_b''(0)`$ has the opposite sign. The remainders grow in proportion to $`\lvert w_{11}\rvert/M`$, that is as $`\epsilon^2u`$, like $`\varrho`$ of (11.30).
- **I2, the member with a flat value** ($`M_1=M_2=\tau_1=\tau_2=1`$, $`W_0=w\,\lvert v\rangle\langle v\rvert`$ with $`w=1`$; $`\Omega-M=0.414214`$). The weight of $`v`$ on the kernel of $`h_0(q)`$ is below $`10^{-31}`$ for all $`q`$. For $`P=0.8,0.4,0.2,0.1,0.05`$ the equation $`1+w\,g_v(E,P)=0`$ has exactly one root above the mixed bands and none below them: $`E_b-\Delta(P)=3.2\times10^{-3}`$, $`4.1\times10^{-4}`$, $`5.2\times10^{-5}`$, $`6.5\times10^{-6}`$, $`8.1\times10^{-7}`$ (between $`6.3`$ and $`6.5\times10^{-3}\lvert P\rvert^3`$), and $`E_b/\lvert P\rvert=0.3754`$, $`0.4043`$, $`0.4117`$, $`0.4136`$, $`0.4141`$. The root at $`P=-0.2`$ equals that at $`P=0.2`$, and a finer grid ($`2^{17}`$ values of $`q`$) changes no digit shown. A dense diagonalization at $`L=240`$ gives the same eigenvalue to $`6\times10^{-16}`$ ($`P=0.8`$) and to $`6\times10^{-11}`$ ($`P=0.4`$, with the weight $`2\times10^{-4}`$ at $`\lvert r\rvert>120`$), as the only eigenvalue between $`\Delta(P)`$ and $`1`$. At $`P=0`$ it gives $`962=2(2L+1)`$ eigenvalues with $`\lvert E\rvert\le7\times10^{-15}`$, all states of the mixed bands; the nearest other eigenvalue is $`-1.81616`$, which is the root of $`1+w\,g_v(E,0)=0`$.

No check failed. The member of Step 1a and the bound (11.30) were derived before Part 3 was run, and the run agrees with them. The sentence of Step 8 that (11.30) is not necessary was written after the run and rests on it.

## Methods used

- Fibre decomposition of a shift-invariant two-body contract (total plane-wave label)
- Weyl's theorem on the essential spectrum; discrete spectrum; degree of a trigonometric polynomial (flat bands)
- Hellmann–Feynman theorem; second-order perturbation theory; Euler's relation for homogeneous functions
- Rellich's theorem; degenerate perturbation theory to second order (reduced resolvent)
- Partial expectation value of the contract in the start of the medium; unique split into single-object terms and a finite-range pair term
- Resolvent (Green function) equation for a rank-four on-site change; monotonicity of a resolvent matrix element in a gap
- Degenerate perturbation theory (Schrieffer–Wolff) and the one-defect chain; stability of an isolated simple eigenvalue under a change of small norm
- Commutator identity for the relative coordinate in a bound state
- Packets of fibre eigenvectors: position labels as derivatives in the total label; Taylor's formula with remainder
- Taylor expansion of the level around the mean clock level; cancellation of an even phase in the reading statistics
- Numerical diagonalization, finite differences, root of the bound-level equation on the infinite chain (check)
