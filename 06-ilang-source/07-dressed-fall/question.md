# Question: 07-dressed-fall

- **Subproject:** 06-ilang-source
- **Package:** 07-dressed-fall
- **Equation tags:** (7.k)
- **Created:** 2026-10-19

## Goal

Determine whether a body that makes a field of its own (its own mark) falls in the field of another source in the same way for all its clock levels and both branches, and to which order in its coupling. This is the second part of item 5 of the base problem. Every result is stated through quantities that the total contract fixes (M6): eigenvalues of the total contract, their dependence on the places of held bodies, and accelerations.

**Setting.**
- **Field.** The class of 04-profile on a ring of $`L`$ places: $`N_f\ge1`$ identical field objects ($`c=+1`$), no pair terms among them, own term $`C_1=-t_f\sum_x(\lvert x\rangle\langle x+1\rvert+\lvert x+1\rangle\langle x\rvert)`$, $`t_f>0`$, $`\Phi_x`$ the number of field objects at $`x`$, $`n:=N_f/L`$; $`\Lambda^+`$ the pseudo-inverse of the ring Laplacian. **State of the field** (assumption, M9): the lowest state adapted to the bodies present.
- **Source.** One held body $`s`$ (A15) at the place $`x_s`$, in an eigenvector of its coupled operator with eigenvalue $`g_s`$, coupled by $`g_s\Phi_{x_s}`$; weak: first order in $`g_s`$, with $`\lvert g_s\rvert`$ small against the field's gap $`t_f\omega_{\min}`$, $`\omega_{\min}=4\sin^2(\pi/L)`$. All expansions are at fixed $`L`$.
- **Body.** One Model D body $`b`$ (base problem, "Notation and conventions"; $`M_k:=m+d_k`$ the half-gap of level $`k`$) on the same ring, coupled to the field by (a) $`\gamma\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m\mathbb 1_N+D)\otimes\Phi_x`$ or (c) the same plus $`\gamma`$ times the motion term with the factor $`\frac12(\Phi_x+\Phi_{x+1})`$ on each bond. Its own change of the field is kept (it is not a test body). Records at $`\kappa\to0`$.
- **Held body ($`\tau=0`$).** The same body with $`\tau=0`$ is held at the place $`x`$ on level $`k`$ and branch $`\sigma`$; its *weight* $`W_{k,\sigma}(x)`$ is the dependence on $`x`$ of the eigenvalue of the total contract connected, as $`\gamma,g_s\to0`$, to this body with the field in its lowest state (a difference between places at fixed bodies, which the total contract fixes).

1. **Weight of a body with its own mark.** For the held body: determine $`W_{k,\sigma}(x)-W_{k,\sigma}(x')`$ at first order in $`g_s`$ and through second order in $`\gamma`$, on the ring, at fixed $`L`$, $`N_f`$, $`t_f`$; give its dependence on $`M_k`$ and $`\sigma`$, and state whether it is proportional, for all levels and both branches, to one function of the place times a factor that depends on the level only through $`M_k`$ (and which factor).
2. **Fall.** For $`\tau>0`$, in a regime to be stated and named as an assumption (in particular the relation of the body's motion to the response of the field, and the order in $`\tau`$): determine the drift acceleration from rest of the body with its own mark at the band point $`p=0`$ in the field of the source, at first order in $`g_s`$ and through relative order $`\gamma`$ beyond the leading term, using the weight of item 1 and the curvature (6.10) of 06-own-mark; state whether it is the same for all levels and both branches at that order, and, if not, the first order in $`\gamma`$ and the parameter at which a level or branch dependence appears. If none appears at relative order $`\gamma`$, say so and state what the next order needs; do not compute it.

## Inputs

From 04-profile@v4 (this subproject). Setting there: the field class of the setting above, held sources $`g_i\Phi_{x_i}`$ at $`x_1`$, $`x_2`$; $`h(g)`$ the one-object contract with the sources, $`\varepsilon_0(g)`$ its lowest eigenvalue; on the ring the one-object lowest eigenvector is uniform and the reduced resolvent is $`\Lambda^+/t_f`$.

Eq. (4.2) of 04-profile:

```math
E(g)=N_f\,\varepsilon_0(g),\qquad M=N_f\bigl[\varepsilon_0(g_1,g_2)-\varepsilon_0(g_1,0)-\varepsilon_0(0,g_2)+\varepsilon_0(0,0)\bigr].\qquad\text{(4.2)}
```

Eq. (4.4) of 04-profile:

```math
M^{(2)}(x_1,x_2)=-\frac{2n\,g_1g_2}{t_f}\,\Lambda^+(x_1,x_2),\qquad \Lambda^+(x,y)=\frac1{\lvert X_f\rvert}\sum_{\mathbf k\neq0}\frac{e^{i\mathbf k\cdot(x-y)}}{\omega(\mathbf k)},\quad \omega(\mathbf k)=\sum_{\mu=1}^{D}4\sin^2\frac{k_\mu}2,\qquad \sum_{x_2\in X_f}M^{(2)}(x_1,x_2)=0,\qquad\text{(4.4)}
```

From 05-made-field-scale@v3 (this subproject). Setting there: a test body (its own change of the field neglected) in the field made by the held source; $`N_\varphi(x)`$ the expectation of $`\Phi_x`$ in the field state, $`\nu(x)=1+\gamma N_\varphi(x)`$, $`N'`$ the lattice slope of $`N_\varphi`$, $`N''`$ its second difference, $`r(x)`$ the clock rate at $`x`$, $`\tau_{\rm loc}(x_0)`$ the local hopping ($`\tau`$ for (a), $`\tau\nu(x_0)`$ for (c)), $`d_0`$ the record step; branch start at rest at $`x_0`$.

Eq. (5.7) of 05-made-field-scale:

```math
a_{k,\sigma}(0)=-\tau_{\rm loc}(x_0)^2\,\frac{\gamma N'(x_0)}{\nu(x_0)}=-\tau_{\rm loc}(x_0)^2\Bigl[\frac{r(x_0+1)-r(x_0)}{r(x_0)}-\frac{\gamma N''(x_0)}{2\nu(x_0)}\Bigr],\qquad v_{\max}(x_0):=\tau_{\rm loc}(x_0)\,d_0 .
\qquad\text{(5.7)}
```

Eq. (5.8) of 05-made-field-scale (lowest adapted state, $`\omega_{\min}=4\sin^2(\pi/L)`$):

```math
N(y)=n-\frac{2n\,g_s}{t_f}\,\Lambda^+(y,x_s)+O\Bigl(\frac{N_fg_s^2}{t_f^2\omega_{\min}^2}\Bigr),\qquad \delta N(y):=N(y)-n,
\qquad\text{(5.8)}
```

From 06-own-mark@v3 (this subproject). Setting there: the field and the body of the setting above without the source; $`A`$ the motion term of Model D, $`C_f`$ the field's own term, $`C\big|_k`$ the total contract on clock level $`k`$; $`E_{k,\sigma}(P)`$ the dressed level (eigenvalue of the total contract in the sector of clock level $`k`$ and total plane-wave label $`P`$, connected to the branch start $`(P,\sigma,k)`$ with the field in its lowest state); $`\varepsilon_0(g)`$ the lowest eigenvalue of one object with a held source $`g`$ at the body's place; $`S_0=\sum_{q\ne0}\varepsilon_q^{-1}=(L^2-1)/(12t_f)`$, $`\varepsilon_q=2t_f(1-\cos q)`$; $`G_{k,\sigma}(P,q)`$ the second-order kernel of 06-own-mark. Every perturbative statement there holds under the isolation condition (6.4) of 06-own-mark, sufficient for $`\sigma=+`$ at $`P=0`$: $`2t_fN_f<M_k`$.

Eq. (6.2) of 06-own-mark:

```math
\begin{aligned}\text{(a)}:\ C\big|_k&=A+M_k\sigma_3\textstyle\sum_x\lvert x\rangle\langle x\rvert(1+\gamma\Phi_x)+C_f,\\ \text{(c)}:\ C\big|_k&=\text{(a)}+\gamma\tfrac\tau2\textstyle\sum_x\bigl(\lvert x+1\rangle\langle x\rvert(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert(i\sigma_1)\bigr)\tfrac12(\Phi_x+\Phi_{x+1}).\end{aligned}\qquad\text{(6.2)}
```

Eq. (6.7) of 06-own-mark:

```math
E_{k,\sigma}(P)\big|_{\tau=0}=\sigma M_k+N_f\,\varepsilon_0(\sigma\gamma M_k)\ \ \text{for all }P\ \text{and all }\gamma,\qquad N_f\varepsilon_0(g)=-2t_fN_f+gn-g^2\tfrac nLS_0+O(g^3).\qquad\text{(6.7)}
```

Eq. (6.10) of 06-own-mark:

```math
E''_{k,\sigma}(0)=\sigma\frac{\tau^2}{M_k}\times\begin{cases}1-\gamma n+\gamma^2n^2&\text{(a)}\\ 1+\gamma n&\text{(c)}\end{cases}+\Delta''_{k,\sigma}+O(\gamma^3),\qquad \Delta''_{k,\sigma}:=\gamma^2\frac nL\sum_{q\ne0}\partial_P^2G_{k,\sigma}(P,q)\big|_{P=0}.\qquad\text{(6.10)}
```

**Note (2026-10-19, after external round 1).** The isolation condition of 06-own-mark, cited above in words, is quoted here. Setting there: $`\omega_k(p)=\sqrt{M_k^2+\tau^2\sin^2p}`$ the body's branch energies without coupling; $`(Q,E_{\rm exc})`$ the total label and excitation energy of an excited field eigenstate; the start $`(P,\sigma,k)`$ is a simple eigenvalue of its sector at $`\gamma=0`$ iff

```math
\sigma\omega_k(P)\neq\sigma'\omega_k(P-Q)+E_{\rm exc}\quad\text{for every excited field eigenstate }(Q,E_{\rm exc})\text{ and }\sigma'=\pm\qquad\text{(6.4)}
```

## Assumptions

- The setting under "Goal". The field class, the held source, the lowest adapted state, the body and its couplings are assumptions of the package (M8, M9); the regime of item 2 is named by the derivation.
- Standard perturbation theory for an isolated eigenvalue may be used with its conditions stated.

## Scope

- **Class.** Both couplings, every $`N_f\ge1`$, $`L\ge5`$, every level $`k`$, both branches; item 2 in the stated regime, inside the isolation condition of 06-own-mark.
- Out of scope: second order in $`g_s`$; the tori; a moving source; bound pairs; the second-order own-mark curvature beyond its order.

## Depth

- Item 1: derive (needed by item 2 and by item 5 of the base problem: the weight of a body that makes a field).
- Item 2: derive (needed by item 5 of the base problem: whether a body can make a field and fall universally in another one, and to which order).

## Expected result

- Item 1: an expression for the weight difference through second order in $`\gamma`$, and a yes/no answer on the factorization with the factor named.
- Item 2: an expression for the acceleration through relative order $`\gamma`$, with the regime; a yes/no answer on level and branch independence, with the order and parameter of the first dependence.

Give every main result a tag $`(7.k)`$.

Consistency checks, at most three: for example the leading term of item 2 against (5.7) with (5.8), $`g_s=0`$, and the limit $`\tau\to0`$ of item 2.

## Code

Required: check: for $`N_f=1`$ on rings of two sizes, the weight difference of item 1 against the exact lowest eigenvalue of one field object with the two held point terms (body and source), at several values of $`\gamma`$ and $`g_s`$, with the scaling of the deviation.
