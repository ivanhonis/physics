# Question: 07-random-records

- **Subproject:** 03-ilang-space
- **Package:** 07-random-records
- **Equation tags:** (7.k)
- **Created:** 2026-10-08

## Goal

Determine the leading-order witness geometry that a recording contract produces when no structure is written into the contract: the record operators are drawn at random, independently for each place, from a unitarily invariant ensemble. The aim is to separate what the language gives generically from what an example puts in by hand. The notation introduced below ($\mathrm{GUE}(s)$, $\mathrm{GOE}(s)$, $n$, $m$) is fixed for later packages.

**Setting.** The setting of 05-recording-contract:
- **Description.** Two objects, $a$ and $c$, of different types, each the only instance of its type; the part is $A=\{a\}$.
- **Contract.** A recording contract $C=\sum_h\lvert h\rangle\langle h\rvert\otimes K_h$.
- **Initial state.** The product state $\lvert\phi\rangle\otimes\lvert\chi\rangle$, with $\phi_h\neq0$ for every $h$.

Write $n:=d_{T(a)}\ge2$ for the number of places of $a$, and $d_c:=\dim\mathcal H_c\ge2$. Fix an orthonormal basis $e_1=\lvert\chi\rangle,e_2,\dots,e_{d_c}$ of $\mathcal H_c$, and write $K_{ab}:=\langle e_a\vert K\vert e_b\rangle$.

**Ensembles.** The operators $K_h$, $h=1,\dots,n$, are independent and identically distributed, drawn from one of the following.
- **$\mathrm{GUE}(s)$.** $K=K^\dagger$, the probability density on self-adjoint operators is proportional to $\exp\bigl(-\operatorname{Tr}K^2/(2s^2)\bigr)$, and $s>0$. Equivalently, the entries $K_{ab}$ with $a<b$ are complex Gaussian with mean $0$ and $E\lvert K_{ab}\rvert^2=s^2$, with independent real and imaginary parts of variance $s^2/2$ each. The diagonal entries are real Gaussian with variance $s^2$, and all these entries are independent. This ensemble is invariant under $K\mapsto UKU^\dagger$ for every unitary $U$, so it singles out no direction in $\mathcal H_c$.
- **$\mathrm{GOE}(s)$.** $K$ is real symmetric in the basis $(e_a)$, with density proportional to $\exp\bigl(-\operatorname{Tr}K^2/(4s^2)\bigr)$. Equivalently, $K_{ab}$ with $a<b$ is real Gaussian with variance $s^2$, the diagonal entries are real Gaussian with variance $2s^2$, and all are independent. This ensemble is invariant under real orthogonal $K\mapsto OKO^{T}$.

1. **Record vectors (GUE).** Show that the record vectors $u_h$ of (5.10) are independent for different $h$. Show that each is a circularly symmetric complex Gaussian vector in $\chi^\perp$ with mean $0$ and covariance $s^2\mathbb 1_{\chi^\perp}$, that is, $E\lvert\langle e\vert u_h\rangle\rvert^2=s^2$ for every unit vector $e\in\chi^\perp$.

2. **Distances (GUE).** For $h\neq h'$, derive the distribution of $d_0(h,h')^2$, together with its mean, its variance and its relative standard deviation. Show that these depend only on $s$ and $d_c$.

3. **Dimension (GUE).** Show that almost surely the leading-order dimension (5.14) equals $\min\bigl(n-1,\,2(d_c-1)\bigr)$, that is, the bound (5.14) is attained.

4. **Real variant (GOE).** Derive the analogues of items 1–3 for $\mathrm{GOE}(s)$. In this case $u_h$ is a real Gaussian vector in the real span of $e_2,\dots,e_{d_c}$.

5. **Two regimes.** Write $m$ for the real dimension of the space in which the $u_h$ lie: $m=2(d_c-1)$ for GUE, $m=d_c-1$ for GOE.
   - (a) Fix $n$ and let $d_c\to\infty$. Show that all pairwise distances $d_0$ divided by their common mean value converge to $1$ in probability, so the normalized configuration tends to a regular simplex.
   - (b) For $n>m+1$, the configuration consists of $n$ independent Gaussian points in a Euclidean space of dimension $m$, and its affine dimension is $m$, fixed by the medium and not by $n$.

## Inputs

From 05-recording-contract@v1. These hold in the setting above. $d_0$ is the leading-order distance, $\alpha(h,h';\lambda)=\lambda d_0(h,h')+o(\lambda)$, and $(\mathcal H_c,g)$ with $g(v,w):=\operatorname{Re}\langle v\vert w\rangle$ is a real Euclidean space of dimension $2d_c$. The relation $h\sim_0h'$ means $u_h=u_{h'}$, and $\dim_0:=\dim_{\mathbb R}\operatorname{aff}_{\mathbb R}\{u_h\}$.

Eq. (5.10):

$$
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
$$

Eq. (5.11):

$$
\bigl(H_V/{\sim_0},\,d_0\bigr)\;\cong\;\bigl(\{u_h:h\in H_V\},\,\lVert\cdot\rVert\bigr)\subset(\mathcal H_c,g).
$$

Eq. (5.13):

$$
\langle\chi\vert u_h\rangle=\langle K_h\rangle-\langle K_h\rangle\langle\chi\vert\chi\rangle=0 ,
$$

Eq. (5.14):

$$
\dim_0\le\min\bigl(d_{T(a)}-1,\;2d_c-2\bigr).
$$

## Assumptions

- The setting and the ensembles stated under "Goal". The operators $K_h$ are random but do not depend on $\lambda$ (A5). Each statement is about the leading-order geometry $d_0$ at small $\lambda$, as in (5.10).
- A random contract stands for an ensemble of descriptions. A statement "almost surely" or "in probability" refers to this ensemble.

## Scope

- In scope:
  - the distribution of the record vectors and of the leading-order distances;
  - the leading-order dimension;
  - the real variant;
  - the two regimes.
- Out of scope:
  - finite $\lambda$;
  - the neighbour structure of 04-neighbours on the random configuration;
  - non-Gaussian ensembles and universality;
  - the joint distribution of all pairwise distances beyond what items 2 and 5 need;
  - locality, several parts, and bodies;
  - any physical or spatial meaning beyond the definitions (M1, M4).

## Depth

- Item 1: derive.
- Item 2: derive.
- Item 3: short argument. The standard fact may be used without proof: independent random vectors with absolutely continuous distributions on $\mathbb R^m$ are in general position almost surely.
- Item 4: short argument, by analogy with items 1–3.
- Item 5: short argument. Standard concentration facts (for example Chebyshev's inequality) may be used without proof.

## Expected result

The main model expects the following. Derive each statement, and report any discrepancy in a distribution, a factor or a dimension.

- Item 1: $u_h=\sum_{a\ge2}(K_h)_{a1}\,e_a$, independent and identically distributed, circularly symmetric complex Gaussian with covariance $s^2\mathbb 1_{\chi^\perp}$.
- Item 2: $d_0(h,h')^2=s^2\,\chi^2_{2(d_c-1)}$, that is, $s^2$ times a chi-square variable with $2(d_c-1)$ degrees of freedom. Mean $2(d_c-1)s^2$, variance $4(d_c-1)s^4$, relative standard deviation $1/\sqrt{d_c-1}$.
- Item 3: $\dim_0=\min\bigl(n-1,\,2(d_c-1)\bigr)$ almost surely.
- Item 4: $d_0^2=2s^2\,\chi^2_{d_c-1}$, mean $2(d_c-1)s^2$, relative standard deviation $\sqrt{2/(d_c-1)}$, and $\dim_0=\min(n-1,\,d_c-1)$ almost surely.
- Item 5: the convergence statement in (a), and the dimension statement in (b).

Give every main result a tag $(7.k)$.

Consistency checks, at most three, chosen from:
- a qubit medium ($d_c=2$, GUE): the $u_h$ lie in a complex line $\cong\mathbb R^2$, so $\dim_0=2$ for $n\ge3$;
- $s\to0$: every $d_0\to0$, and all places merge into one point;
- $n=2$: a single distance, and $\dim_0=1$ almost surely.

## Code

None.
