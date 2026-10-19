# Question: 15-curved-profile-fall

- **Subproject:** 05-ilang-free-fall
- **Package:** 15-curved-profile-fall
- **Equation tags:** (15.k)
- **Created:** 2026-10-18

## Goal

For a body whose clock level is conserved, as in 04-branch-fall, but whose level profiles are not linear in the position label, determine how a start at rest in the upper branch accelerates, and how far the result of the linear profiles, taken with the local slope at the start, describes it. No field object; the position dependence is written into the body's own contract (A10), which is an assumption of this package (M8).

**Setting.**
- **Body and records.** A body $`b`$, the only instance of its type, and a recording medium $`c`$, with the records $`K_x=\kappa\,x\,X`$, places $`(x,s,a)`$ as for Model D, $`x`$ on a chain $`\lvert x\rvert\le L`$ and $`x\in\mathbb Z`$ as the limit of long chains (A1). As in 04-branch-fall, the term $`\kappa\,x\,\langle X\rangle`$ of the records is counted in every $`V_{x,k}`$; results in the weak-record regime ($`\kappa\to0`$ at fixed $`\lambda`$, chain and start). $`\bar x_{\rm lab}(\lambda)`$ is the mean position label.
- **Level blocks (the class of 04-branch-fall with $`\zeta_{x,k}=1`$).** On the clock level $`k`$ (conserved):
  ```math
  C^{(k)}=\frac{\tau_k}2\sum_x\Bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\Bigr)+\sum_x\lvert x\rangle\langle x\rvert\otimes\bigl(M_{x,k}\,\sigma_3+V_{x,k}\,\mathbb 1_2\bigr),
  ```
  with $`\tau_k>0`$, $`M_{x,k}>0`$ on the chain and real $`V_{x,k}`$.
- **Quadratic level profiles about a point $`x_0`$.** With $`y:=x-x_0`$, for every level $`k`$:
  ```math
  M_{x,k}=M_k+G_k\,y+\tfrac12H_k\,y^2,\qquad V_{x,k}=-\mathcal F_k\,y-\tfrac12\mathcal H_k\,y^2 .
  ```
  The **slopes at $`x_0`$** are $`G_k`$, $`\mathcal F_k`$; the **curvatures** are $`H_k`$, $`\mathcal H_k`$. With $`H_k=\mathcal H_k=0`$ these are the linear level profiles of 04-branch-fall, with the origin moved to $`x_0`$.
- **Starts.** The branch start $`B_{k,+}[g]`$ of 04-branch-fall, built from the upper branch of the level block with all slopes and curvatures set to zero ($`M_{x,k}\to M_k`$, $`V_{x,k}\to0`$), with $`g`$ smooth and $`2\pi`$-periodic; it is **centred at $`x_0`$** if its mean position label is $`x_0`$, and **at rest** if its weight in $`p`$ has the mean $`0`$ on $`(-\pi,\pi]`$. $`\delta p^2`$ is the variance of that weight and $`W^2`$ the variance of the position label of the start. The start is not adapted to the profiles; this is part of the assumption (M9).
- **Order.** First order jointly in $`G_k,\mathcal F_k,H_k,\mathcal H_k`$ at fixed $`\lambda`$, fixed start and fixed chain, followed by the limit of a long chain, as in 04-branch-fall.

1. **Acceleration in a quadratic profile.** One level $`k`$, a start $`B_{k,+}[g]`$ at rest centred at $`x_0`$.
   - (a) Determine the first-order acceleration $`\mathrm d^2\bar x_{\rm lab}/\mathrm d\lambda^2`$ as a function of $`\lambda`$: separate the oscillating terms from the rest, and give the rest exactly as a function of $`\lambda`$, with its coefficients as averages over the start.
   - (b) Determine the part of (a) that the curvatures contribute, and how it depends on $`\lambda`$ and on the start (through $`W^2`$, $`\delta p^2`$ or other averages); state whether it grows with $`\lambda`$, with the power.
2. **Local slope.** Determine the conditions on $`H_k`$, $`\mathcal H_k`$, $`W`$, $`\delta p`$ and $`\lambda`$ under which the non-oscillating part of (a), averaged over a window, equals the drift acceleration at rest of the linear profiles with the slopes at $`x_0`$, $`\frac{\tau_k^2}{M_k}(\mathcal F_k-G_k)`$ of (4.16), up to a stated relative error. State whether a limit of the start exists in which this holds exactly at first order, and the order of the limits.
3. **Level independence.** Bodies with $`N\ge2`$ levels.
   - (a) The factor class: $`M_{x,k}=(m+d_k)\,n_x`$, $`V_{x,k}=0`$, $`\tau_k=\tau`$, with $`n_x=1+g\,y+\tfrac12h\,y^2`$ and $`d_k:=\frac{2\pi k}{N\lambda_0}`$. Determine whether the non-oscillating first-order acceleration of item 1 is the same for all levels at every $`\lambda`$, for every start of the class of item 1.
   - (b) Control: $`M_{x,k}=m\,n_x+d_k`$ (the factor on the rest term only), otherwise as in (a). The same question.

## Inputs

From 04-branch-fall@v3 (this subproject). Setting there: the class $`\mathcal C_{\rm lev}`$ of level blocks $`C^{(k)}=\frac{\tau_k}2\sum_x\zeta_{x,k}\bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\bigr)+\sum_x\lvert x\rangle\langle x\rvert\otimes(M_{x,k}\sigma_3+V_{x,k}\mathbb 1_2)`$ with the linear level profiles $`M_{x,k}=M_k+G_kx`$, $`V_{x,k}=-\mathcal F_kx`$, $`\zeta_{x,k}=1+g_{\zeta,k}(x+\frac12)`$; $`\omega_k(p):=\sqrt{M_k^2+\tau_k^2\sin^2p}`$; the branch start $`B_{k,\sigma}[g]=\int\frac{\mathrm dp}{2\pi}g(p)\lvert p\rangle\otimes\beta_{k,\sigma}(p)\otimes\lvert f_k\rangle`$ with $`\beta_{k,\sigma}`$ the eigenvectors of the block with all gradients zero; $`\langle F\rangle_g:=\int\frac{\mathrm dp}{2\pi}\lvert g\rvert^2F`$; first order in the gradients at fixed $`\lambda`$, start and chain, then a long chain; weak-record regime; $`\mathsf b_k`$ a bound linear in the gradients.

Eq. (4.7) of 04-branch-fall, the coefficient of $`\lambda`$ in the first-order velocity of $`B_{k,\sigma}[g]`$ is $`\langle a_{k,\sigma}\rangle_g`$, with

```math
\boxed{\;a_{k,\sigma}(p)=\frac{g_{\zeta,k}\tau_k^4\sin^2p-G_kM_k\tau_k^2\cos2p}{\omega_k^2}+\sigma\,\mathcal F_k\,\frac{\tau_k^2\bigl(M_k^2\cos2p-\tau_k^2\sin^4p\bigr)}{\omega_k^3}\;},\qquad\lvert a_{k,\sigma}(p)\rvert\le\frac{\tau_k^2}{M_k}\,\mathsf b_k .
```

Eq. (4.11) of 04-branch-fall, for a start concentrated at $`p_0`$ with spread $`\delta p`$, after the long-window limit of the window average $`\overline{a^{(1)}}`$ of the first-order acceleration:

```math
\bigl\lvert\langle a_{k,\sigma}\rangle_g-a_{k,\sigma}(p_0)\bigr\rvert\le\tfrac12\sup_p\lvert a_{k,\sigma}''\rvert\,\delta p^2\ \ (\text{exact}),\qquad\text{drift acceleration}=\lim_{\delta p\to0}\lim_{\Lambda\to\infty}\overline{a^{(1)}}=a_{k,\sigma}(p_0).
```

Eq. (4.16) of 04-branch-fall:

```math
\boxed{\;a_{k,\sigma}(0)=\frac{\tau_k^2}{M_k}\,\bigl(\sigma\,\mathcal F_k-G_k\bigr)\;}
```

Eq. (4.19) of 04-branch-fall, for every member of $`\mathcal C_{\rm lev}`$ with linear level profiles and $`N\ge2`$:

```math
\begin{aligned}
a_{k,+}(0)=a_+\ \forall k&\iff\frac{\tau_k^2}{M_k}(\mathcal F_k-G_k)=a_+\ \forall k,\qquad
a_{k,-}(0)=a_-\ \forall k\iff\frac{\tau_k^2}{M_k}(\mathcal F_k+G_k)=-a_-\ \forall k,\\
\text{both, with }a_+=a_-=a&\iff\mathcal F_k=0\ \text{ and }\ \frac{\tau_k^2G_k}{M_k}=-a\quad\forall k .
\end{aligned}
```

## Assumptions

- The setting under "Goal": the body, the quadratic level profiles, the factor class, the control and the branch starts are assumptions of this package (M8, M9).
- Standard first-order perturbation theory in a term of the contract, plane waves, and the averaging of oscillating terms may be used, with their conditions stated.

## Scope

- **Class.** Items 1 and 2: every level block of the setting with quadratic level profiles, every start $`B_{k,+}[g]`$ at rest centred at $`x_0`$ with finite $`W`$. Item 3: the factor class and its control, $`N\ge2`$.
- **Control.** Item 3(b).
- Out of scope: the lower branch; starts in motion; profiles of the hopping ($`\zeta_{x,k}\neq1`$); terms of the profiles beyond second order in $`y`$; second order in the slopes and curvatures; long falls; clocks and their rates; fields that are not sharp; two bodies.

## Depth

- Item 1: derive (needed by item 2 and by criterion 10, which compares fields that are not linear).
- Item 2: short argument (needed by criterion 10: when a fall at a point is defined).
- Item 3: short argument (needed by criterion 10: whether the level-independent fall of the factor class survives a curved profile).

## Expected result

- Item 1: a function of $`\lambda`$ with explicit coefficients; a term with its dependence on $`\lambda`$ and on the start.
- Item 2: conditions as inequalities, and a limit with its order.
- Item 3: two yes/no answers, each with its reason and, where no, the leading difference between two levels.

Give every main result a tag $`(15.k)`$.

Consistency checks, at most three: for example zero curvatures against (4.7) and (4.16), and $`\tau_k\to0`$.

## Code

None.
