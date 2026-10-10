# Question: 05-moving-clock

- **Subproject:** 04-ilang-time
- **Package:** 05-moving-clock
- **Equation tags:** (5.k)
- **Created:** 2026-10-10

## Goal

Determine how the readings of a clock carried by a body depend on the body's motion in the background of a recording medium:
- when they do not depend on it;
- how they depend on it for a body whose contract couples motion and clock through two anticommuting terms;
- how the rate of the carried clock is related to the body's velocity and to the maximal speed of 03-ilang-space.

This is criterion 4, without the comparison of two clocks between two meetings, which is left to a later package.

**Setting.** As in 03-ilang-space/17-motion, with places that carry a clock label (quoted under "Inputs").
- **Objects.** A body $`b`$, the only instance of its type, and a medium $`c`$, one object of another type.
- **Places.** In item 1, the places of $`b`$ are pairs $`h=(x,a)`$; in items 2–4, triples $`h=(x,s,a)`$.
  - $`x`$ is a position label: from a finite set in item 1, and $`x\in\mathbb Z`$ in items 2–4.
  - $`s\in\{1,2\}`$ is a branch label (items 2–4 only).
  - $`a\in\mathbb Z_N`$, $`N\ge2`$, is a clock label.
- **Contract.** $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, where $`K_h`$ depends only on the position label: $`K_{(x,a)}=K_x`$, respectively $`K_{(x,s,a)}=K_x`$. Places with the same $`x`$ therefore have the same record vector $`u_h`$ and lie in one point of the background.
- **Clock reading.** The reading on $`b`$ with one class $`S_a`$ per clock label, the set of all places with that label. Its statistics are $`q(a;\lambda)`$.
- **Start.** $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$.

1. **Decoupled body.** Let $`C_b=H\otimes\mathbb 1_N+\mathbb 1\otimes D'`$, with $`H`$ self-adjoint on the position labels and $`D'`$ self-adjoint on the clock labels. Let the start be $`\phi=\phi_X\otimes\eta`$, with any $`\chi`$ and any $`K_x`$. Determine $`q(a;\lambda)`$ for every $`\lambda`$. Determine whether it depends on $`H`$, on $`\phi_X`$ or on the $`K_x`$.

2. **Model with anticommuting terms: branches and velocity.** Places $`(x,s,a)`$, $`x\in\mathbb Z`$, as the limit of long finite chains with the start far from both ends (A1). State how the limit is taken. Let
   ```math
   C_b=A+B,\qquad A=\frac\tau2\sum_x\Bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\Bigr)\otimes\mathbb 1_N,\qquad B=\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m\mathbb 1_N+D),
   ```
   with $`\tau>0`$ and $`m>0`$. Here $`\sigma_1,\sigma_3`$ are the Pauli matrices on the branch label, and $`D=\frac{2\pi}{N\lambda_0}\sum_{k=0}^{N-1}k\lvert f_k\rangle\langle f_k\rvert`$ is the minimal ring clock of 02-clock on the clock label, with tick $`\lambda_0>0`$. Let the records be $`K_x=\kappa\,x\,X`$, with $`\kappa>0`$ and $`X`$ as in (17.15).
   - (a) Determine $`AB+BA`$. Determine the eigenvalues and eigenvectors of $`C_b`$ in terms of the plane waves of the chain, for each eigenvalue $`d_k`$ of $`D`$.
   - (b) **Weak records.** Work to leading order in $`\kappa`$ at fixed $`\lambda`$: the view of $`b`$ is that of $`C_b`$ alone, and positions are measured in the background (17.15). Determine the velocity $`v`$ (17-motion) of a start concentrated near a plane-wave label $`p_0`$ in the branch of positive eigenvalue for the clock level $`d_k`$. Determine $`v`$ as a function of $`p_0`$, its largest value over $`p_0`$, and the bound (17.7) for this $`C_b`$, all in units of $`\kappa\sigma_X`$.

3. **The moving clock.** Same model and regime. The start is concentrated near $`p_0`$ in the branch of positive eigenvalue, and the clock label is in the place $`\lvert0\rangle`$.
   - Determine $`q(a;\lambda)`$ to first order in $`\frac{2\pi}{N\lambda_0 m}`$, the level spacing of $`D`$ relative to $`m`$, and to leading order in the spread of the start around $`p_0`$.
   - Determine the tick $`\lambda_0(p_0)`$: the value of $`\lambda`$ at which, to this order, the clock reading has advanced by one place with certainty.
   - Determine its ratio to the tick at $`p_0=0`$.

4. **Rate and velocity.** Express the ratio of item 3 as a function of the velocity $`v`$ of item 2(b):
   - exactly on the chain;
   - and to leading order for small $`p_0`$.

   Compare the result with the ratio of $`v`$ to the bound (17.7) and to the largest velocity of item 2(b).

## Inputs

From 02-clock@v2. Notation fixed there: $`S\lvert m\rangle=\lvert m+1\rangle`$, $`\lvert f_k\rangle=N^{-1/2}\sum_me^{2\pi ikm/N}\lvert m\rangle`$; a uniform ring clock has $`e^{-iC_K\lambda_0}\lvert m\rangle=e^{i\theta_m}\lvert m+1\rangle`$ with tick $`\lambda_0`$, and $`\Delta C_K`$ is the spread of $`C_K`$.

Eq. (2.9), "where the $`\alpha_m`$ and $`\varepsilon`$ are arbitrary reals. The phases are then $`\theta_m=\alpha_{m+1}-\alpha_m-\varepsilon\lambda_0`$ (mod $`2\pi`$, with $`\alpha_N:=\alpha_0`$). If $`\theta_m=0`$ for all $`m`$, then $`e^{-iC_K\lambda_0}=S`$. The same argument applied to $`S`$, whose eigenvalues $`e^{-2\pi ik/N}`$ on $`\lvert f_k\rangle`$ are distinct, gives exactly $`C_K=\sum_k\frac{2\pi\ell_k}{N\lambda_0}\lvert f_k\rangle\langle f_k\rvert`$ with $`\ell_k\equiv k`$."

```math
C_K=\sum_{k\in\mathbb Z_N}E_k\lvert v_k\rangle\langle v_k\rvert,\quad
\lvert v_k\rangle=\frac{1}{\sqrt N}\sum_{m}e^{2\pi ikm/N}e^{i\alpha_m}\lvert m\rangle,\quad
E_k=\varepsilon+\frac{2\pi\ell_k}{N\lambda_0},\quad \ell_k\in\mathbb Z,\ \ell_k\equiv k\ (\mathrm{mod}\ N),
```

Eq. (2.12), for the start $`\lvert0\rangle`$:

```math
\min\Delta C_K=\frac{2\pi}{\lambda_0}\sqrt{\frac{N^2-1}{12N^2}},\quad\text{attained iff } \{\ell_k\}=\{c,c+1,\dots,c+N-1\},\ c\in\mathbb Z .
```

Eq. (2.13), the place-reading distribution of a self-driven uniform ring clock of a minimal member, started at $`\lvert0\rangle`$:

```math
p(m;\lambda)=\frac{\sin^2(\pi\lambda/\lambda_0)}{N^2\sin^2\bigl(\pi(\lambda/\lambda_0-m)/N\bigr)}\qquad(\text{value }1\text{ where the denominator vanishes}).
```

From 03-ilang-space/05-recording-contract@v1. These hold in the setting of 05: one recorded object, one medium object, the recording contract $`\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, and the start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\phi_h\neq0`$ for all $`h`$. Notation fixed there: $`g(v,w):=\mathrm{Re}\langle v\vert w\rangle`$, and $`h\sim_0h'`$ iff $`u_h=u_{h'}`$.

Eq. (5.10):

```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
```

Eq. (5.11):

```math
\bigl(H_V/{\sim_0},\,d_0\bigr)\;\cong\;\bigl(\{u_h:h\in H_V\},\,\lVert\cdot\rVert\bigr)\subset(\mathcal H_c,g).
```

From 03-ilang-space/17-motion@v2. Setting there: $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, $`C_b=\sum_{h,h'}t_{hh'}\lvert h\rangle\langle h'\rvert`$ with $`t_{hh'}=t_{h'h}^*`$; the hopping graph joins $`h\neq h'`$ iff $`t_{hh'}\neq0`$; the start is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, $`\lvert u_h\rangle:=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$, $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$. Definitions fixed there, with $`p_h(\lambda)`$ the place weights of the view of $`b`$:

```math
\bar x(\lambda):=\sum_hp_h(\lambda)\,u_h,\qquad s(\lambda)^2:=\sum_hp_h(\lambda)\,\bigl\lVert u_h-\bar x(\lambda)\bigr\rVert^2,\qquad v(\lambda):=\frac{\mathrm d\bar x}{\mathrm d\lambda}.
```

Eq. (17.7), with $`W`$ the witness weight of the view of $`b`$, $`q_h:=\sqrt{p_h}`$, and $`a_{hh'}:=\lvert t_{hh'}\rvert d_0(h,h')`$ with largest eigenvalue $`\varrho(a)`$; the bound holds for every start and every $`\lambda`$:

```math
\lVert v(\lambda)\rVert\le\sum_{\{h,h'\}\in E}2\lvert t_{hh'}\rvert d_0(h,h')\sqrt{W(h,h';\lambda)p_hp_{h'}}\le\sum_{h,h'}a_{hh'}q_hq_{h'}\le v_{\max}:=\varrho(a)\le\max_h\sum_{h'}\lvert t_{hh'}\rvert\,d_0(h,h') .
```

Eq. (17.15), for the chain $`h_m`$, $`m\in\mathbb Z`$, with $`K_{h_m}=m\,X`$, $`X`$ self-adjoint on $`\mathcal H_c`$, $`\sigma_X:=(\langle X^2\rangle-\langle X\rangle^2)^{1/2}>0`$ and $`e:=(X-\langle X\rangle)\chi`$, so that $`\lVert e\rVert=\sigma_X`$ and $`u_{h_m}=m\,e`$:

```math
d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X,\qquad \bar x=\bar m\,e,\quad \bar m:=\sum_mm\,p_{h_m},\qquad s^2=\sigma_X^2\sum_m(m-\bar m)^2p_{h_m} .
```

Eq. (17.20), the bound (17.7) for the chain with $`C_b=t\sum_m(\lvert h_m\rangle\langle h_{m+1}\rvert+\lvert h_{m+1}\rangle\langle h_m\rvert)`$, $`t>0`$:

```math
v_{\max}=2t\,\sigma_X .
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- No object other than $`b`$ has the type of $`b`$, and $`c`$ is the only instance of its type.
- Items 2–4 use the weak-record regime stated in item 2(b); state every place where it is used.

## Scope

- In scope:
  - the decoupled body in general (item 1);
  - the model of items 2–4;
  - the clock reading of the carried clock;
  - starts concentrated near one plane-wave label in one branch.
- Out of scope:
  - the comparison of two carried clocks between two meetings;
  - inertia (criterion 5, a separate package) and a common maximal speed for all types (criterion 6);
  - branches of negative eigenvalue, and starts that mix the two branches, beyond what item 3 needs;
  - effects of the records beyond leading order in $`\kappa`$;
  - any physical meaning of $`\lambda`$ beyond the definitions (M1).

## Depth

- Item 1: short argument.
- Item 2: derive. Standard facts on plane waves and group velocity may be used, stated.
- Item 3: derive.
- Item 4: derive.

## Expected result

- Item 1: a closed form and a yes/no answer for each dependence.
- Item 2: an identity and closed forms; a closed form, its maximum, and the value of the bound.
- Item 3: a closed form to the stated order, a closed form for $`\lambda_0(p_0)`$, and a ratio.
- Item 4: an exact relation, its small-$`p_0`$ form, and a comparison.

Give every main result a tag $`(5.k)`$.

Consistency checks, at most three: for example $`p_0=0`$, $`N=2`$, and the limit $`m\to0`$ or $`\tau\to0`$.

## Code

None.
