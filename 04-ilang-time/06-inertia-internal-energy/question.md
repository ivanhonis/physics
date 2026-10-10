# Question: 06-inertia-internal-energy

- **Subproject:** 04-ilang-time
- **Package:** 06-inertia-internal-energy
- **Equation tags:** (6.k)
- **Created:** 2026-10-10

## Goal

Determine whether, and how, the inertia of a body depends on its internal cost, here the cost of the clock it carries. Compare with the inverse inertia of 03-ilang-space/20-cost-and-mass. That inverse inertia is the response at $`\lambda=0`$, and for a body with internal labels it may differ from the response averaged over the internal oscillations. Both are determined here. This is criterion 5.

**Setting.** As in 03-ilang-space/20-cost-and-mass, items 2–4 (quoted under "Inputs"), with places that carry internal labels.
- **Objects.** A body $`b`$, the only instance of its type, and a medium $`c`$, one object of another type.
- **Places.** In item 1, the places of $`b`$ are pairs $`h=(x,a)`$; in items 2–4, triples $`h=(x,s,a)`$.
  - $`x`$ is a position label: from a finite set in item 1, and $`x\in\mathbb Z`$ in items 2–4.
  - $`s\in\{1,2\}`$ is a branch label (items 2–4).
  - $`a\in\mathbb Z_N`$, $`N\ge2`$, is a clock label.
- **Contract.** $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, where $`K_h`$ depends only on the position label. Places with the same $`x`$ have the same $`u_h`$, so the edges between them lie inside one point of the background.
- **Blocks of $`C_b`$.** $`C_b=\sum_{x,x'}\lvert x\rangle\langle x'\rvert\otimes T_{xx'}`$, where $`T_{xx'}`$ acts on the internal labels and $`T_{x'x}=T_{xx'}^\dagger`$. The amplitudes of a start $`\phi`$ at position $`x`$ form the internal vector $`\phi_x`$.
- **Model D (items 2–4).** Places $`(x,s,a)`$ with $`x\in\mathbb Z`$, as the limit of long finite chains with the start far from both ends (A1). State how the limit is taken. Let
  ```math
  C_b=A+B,\qquad A=\frac\tau2\sum_x\Bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\Bigr)\otimes\mathbb 1_N,\qquad B=\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes(m\mathbb 1_N+D),
  ```
  with $`\tau>0`$ and $`m>0`$.
  - $`\sigma_1,\sigma_3`$ are the Pauli matrices on the branch label.
  - $`D=\frac{2\pi}{N\lambda_0}\sum_{k=0}^{N-1}k\lvert f_k\rangle\langle f_k\rvert`$ is the minimal ring clock of 02-clock on the clock label, with eigenvalues $`d_k=\frac{2\pi k}{N\lambda_0}`$.
  - The records are $`K_x=\kappa\,x\,X`$, with $`\kappa>0`$ and $`X`$ as in (17.15).
  - The **rest cost** of clock level $`k`$ is the positive eigenvalue of $`C_b`$ on the plane wave with label $`p=0`$ and clock level $`k`$.

1. **The inverse inertia of 20 for a body with internal labels.** Places $`(x,a)`$, general $`C_b`$, product start $`\phi\otimes\chi`$.
   - Express $`L_{hh'}(0)`$ and the inverse inertia $`\mu`$ of (20.10) through the blocks $`T_{xx'}`$, $`x\neq x'`$, and the internal vectors $`\phi_x`$. Determine whether edges between places with the same $`x`$ contribute.
   - For the decoupled body ($`T_{xx'}=t_{xx'}\mathbb 1_N`$ for $`x\neq x'`$, arbitrary $`T_{xx}`$) and a start $`\phi_X\otimes\eta`$, determine $`\mu`$. Determine whether it depends on $`\eta`$ or on the $`T_{xx}`$.

2. **Model D: response at $`\lambda=0`$.** Consider the start $`\phi=\phi_X\otimes\lvert1\rangle\otimes\lvert f_k\rangle`$, where $`\lvert1\rangle`$ is the branch label $`s=1`$ and $`\phi_X`$ is a normalized position state. Determine $`L_{hh'}(0)`$ on every edge and the inverse inertia $`\mu`$ of (20.10) for this start.

3. **Model D: averaged response.** Add a uniform cost gradient (in the sense of 20, by changing only the diagonal entries $`t_{hh}`$), with force $`F`$, and work to first order in $`F`$.
   - **Start.** Concentrated near the plane-wave label $`p_0=0`$, in the branch of positive eigenvalue, with clock level $`k`$.
   - **Regime.** Weak records: to leading order in $`\kappa`$ at fixed $`\lambda`$, the view of $`b`$ is that of $`C_b`$ plus the gradient term, and positions are measured in the background (17.15).
   - **Acceleration.** Determine $`a(\lambda)=\mathrm d^2\bar x/\mathrm d\lambda^2`$. Then determine its average over $`\lambda`$-intervals that are long compared with the inverse of the gap between the two branches and short enough for the first-order treatment. State both conditions.
   - **Inertia.** Define the averaged inverse inertia $`\mu_{\rm av}(k)`$ as the coefficient of $`F`$ in this average, and determine it.
   - **Dependence.** Determine how $`\mu_{\rm av}(k)`$ depends on $`d_k`$, and its relation to the rest cost of level $`k`$.
   - **Decoupled body.** Determine $`\mu_{\rm av}`$ for the decoupled body of item 1 on the chain, with nearest-neighbour hopping $`t`$ and any clock term, and whether it depends on the clock level.

4. **Comparison.** Compare $`\mu`$ of (20.10) with $`\mu_{\rm av}`$ for Model D and for the decoupled body. Determine for which of the two bodies they coincide, and why.

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

From 03-ilang-space/05-recording-contract@v1. These hold in the setting of 05: one recorded object, one medium object, the recording contract $`\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, and the start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\phi_h\neq0`$ for all $`h`$. Notation fixed there: $`g(v,w):=\mathrm{Re}\langle v\vert w\rangle`$, and $`h\sim_0h'`$ iff $`u_h=u_{h'}`$.

Eq. (5.10):

```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
```

From 03-ilang-space/17-motion@v2. Setting there: $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, $`C_b=\sum_{h,h'}t_{hh'}\lvert h\rangle\langle h'\rvert`$ with $`t_{hh'}=t_{h'h}^*`$; the hopping graph joins $`h\neq h'`$ iff $`t_{hh'}\neq0`$, and $`E`$ is its set of edges; the start is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$. Definitions fixed there, with $`p_h(\lambda)`$ the place weights of the view of $`b`$:

```math
\bar x(\lambda):=\sum_hp_h(\lambda)\,u_h,\qquad v(\lambda):=\frac{\mathrm d\bar x}{\mathrm d\lambda}.
```

Eq. (17.15), for the chain $`h_m`$, $`m\in\mathbb Z`$, with $`K_{h_m}=m\,X`$, $`X`$ self-adjoint on $`\mathcal H_c`$, $`\sigma_X:=(\langle X^2\rangle-\langle X\rangle^2)^{1/2}>0`$ and $`e:=(X-\langle X\rangle)\chi`$, so that $`\lVert e\rVert=\sigma_X`$ and $`u_{h_m}=m\,e`$:

```math
d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X,\qquad \bar x=\bar m\,e,\quad \bar m:=\sum_mm\,p_{h_m},\qquad s^2=\sigma_X^2\sum_m(m-\bar m)^2p_{h_m} .
```

From 03-ilang-space/20-cost-and-mass@v2. Setting: that of 17, items 2–4 of 20. Definitions fixed there:
- **Blocks.** $`C_{hh'}:=(\langle h\rvert\otimes\mathbb 1)C(\lvert h'\rangle\otimes\mathbb 1)`$; in this setting $`C_{hh'}=t_{hh'}\mathbb 1_c`$ for $`h\neq h'`$ and $`C_{hh}=t_{hh}\mathbb 1_c+K_h`$.
- **Costs.** The site cost is $`L_h(\lambda):=\langle\psi_h\vert C_{hh}\vert\psi_h\rangle`$ and the edge cost is $`L_{hh'}(\lambda):=2\mathrm{Re}\langle\psi_h\vert C_{hh'}\vert\psi_{h'}\rangle`$, with $`\lvert\psi_h\rangle:=(\langle h\rvert\otimes\mathbb 1)\lvert\Psi\rangle`$.
- **Site cost per unit weight.** $`\Omega_h:=\langle\chi\vert C_{hh}\vert\chi\rangle=t_{hh}+\epsilon_h`$, with $`\epsilon_h:=\langle K_h\rangle`$.
- **Acceleration.** $`a:=\mathrm d^2\bar x/\mathrm d\lambda^2`$.
- **Uniform cost gradient, force, inverse inertia.** "The site costs per unit weight have a uniform gradient if there is a vector $`f\in\mathcal H_c`$ with $`\Omega_h-\Omega_{h'}=g\bigl(f,u_h-u_{h'}\bigr)`$ for all $`h,h'`$. The **force** is $`F:=-f`$. Vary the description only through the diagonal entries $`t_{hh}`$; this changes the $`\Omega_h`$ and nothing else. Let $`a_0`$ be the value of $`a(0)`$ when all $`\Omega_h`$ are equal. The **inverse inertia** $`\mu`$ is the real-linear map on $`(\mathcal H_c,g)`$, if one exists, such that $`a(0)=a_0+\mu F`$ for every uniform gradient."

The derivation uses $`\Delta_{hh'}:=u_h-u_{h'}`$, and for the product start $`L_{hh'}(0)=2\mathrm{Re}[t_{hh'}\phi_h^*\phi_{h'}]`$. Eq. (20.10), "For a uniform gradient, $`\Omega_h-\Omega_{h'}=g(f,\Delta_{hh'})=-g(F,\Delta_{hh'})`$. Then (20.9) gives"

```math
a(0)=a_0+\mu F,\qquad \mu=-\sum_{\{h,h'\}\in E}L_{hh'}(0)\,\Delta_{hh'}\,g\bigl(\Delta_{hh'},\,\cdot\,\bigr) .
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- No object other than $`b`$ has the type of $`b`$, and $`c`$ is the only instance of its type.
- Item 3 uses the weak-record regime and first order in $`F`$; state every place where they are used, and the conditions on the averaging interval.

## Scope

- In scope:
  - the inverse inertia (20.10) for bodies with internal labels (item 1);
  - Model D at $`\lambda=0`$ (item 2) and averaged (item 3);
  - the decoupled body for comparison.
- Out of scope:
  - moving clocks and their rates (criterion 4, a separate package);
  - a common maximal speed for all types (criterion 6);
  - composite bodies of several objects;
  - branches of negative eigenvalue beyond what the averaging needs;
  - effects of the records beyond leading order in $`\kappa`$;
  - any physical meaning of $`\lambda`$ or of the costs beyond the definitions (M1, M3).

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: derive. Standard facts on plane waves, branches and their response to a uniform gradient may be used, stated.
- Item 4: short argument.

## Expected result

- Item 1: closed forms; a yes/no answer; a closed form and yes/no answers.
- Item 2: closed forms and a value.
- Item 3: a closed form for the average, the conditions on the interval, a closed form for $`\mu_{\rm av}(k)`$, a relation to the rest cost, and a closed form with a yes/no answer for the decoupled body.
- Item 4: a comparison and a reason.

Give every main result a tag $`(6.k)`$.

Consistency checks, at most three: for example $`N`$ arbitrary with $`k=0`$, $`\tau\to0`$, and the decoupled body against (20.10).

## Code

None.
