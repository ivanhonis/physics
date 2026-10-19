# Question: 17-typical-or-forced

- **Subproject:** 05-ilang-free-fall
- **Package:** 17-typical-or-forced
- **Equation tags:** (17.k)
- **Created:** 2026-10-18

## Goal

For one body in a sharp field with a linear profile, in a stated class of couplings between field and body, determine how special the couplings are that give a fall that is the same for all clock levels (criterion 4) and the relation (4.24) between the fall and the clock rates at two places (criterion 5): which conditions are necessary and which sufficient, the dimension of the set they define in the class, how a small deviation from the set breaks the two results, and whether a requirement stated in the terms of the language selects the set. This is criterion 10 for one body.

**Setting.**
- **Body.** One body of Model D type, the only instance of its type, with $`\tau>0`$, $`m>0`$, a clock with $`N\ge2`$ places, $`d_k:=\frac{2\pi k}{N\lambda_0}`$, $`M_k:=m+d_k`$; records $`K_x=\kappa\,x\,X`$, weak-record regime, with the term $`\kappa\,x\,\langle X\rangle`$ counted in $`V_{x,k}`$ as in 04-branch-fall. Its own contract is Model D: on the level $`k`$ the on-site block is $`M_k\sigma_3`$ and the hopping is $`\tau`$.
- **The class $`\mathcal C^+`$ of couplings.** A sharp field with a linear profile, coupled to the body by lapse-type pair terms whose body operator acts on the branch and clock labels as $`\sigma_3\otimes(\alpha_0\mathbb 1_N+\alpha_1D)+\mathbb 1_2\otimes(\beta_0\mathbb 1_N+\beta_1D)`$, with $`D`$ the clock operator of Model D, and optionally a factor on the motion term. On the level $`k`$ this gives the level block of 04-branch-fall with $`\tau_k=\tau`$, $`M_k=m+d_k`$ and the linear level profiles
  ```math
  G_k=m\,g_m+d_k\,g_\eta,\qquad \mathcal F_k=\mathcal F+d_k\,\mathcal F_1,\qquad g_{\zeta,k}=g_\zeta ,
  ```
  with five real gradients $`\boldsymbol g:=(g_m,g_\eta,\mathcal F,\mathcal F_1,g_\zeta)`$, the record term included in $`\mathcal F`$. The class $`\mathcal C`$ of 03-clock-and-fall is the subclass $`\mathcal F_1=0`$. Every member is an assumption of this package (M8).
- **Results asked about.** Item 4 of the base problem in the form of (4.19), for the upper branch, the lower branch and both, from rest; through the order $`v^2`$ in the form of (4.20), exactly and at leading order in $`M_k/\tau`$. Item 5 in the form of (4.24), with the rate at a place defined as in (3.23).
- **Orders.** First order in the gradients, as in 04-branch-fall; "dimension" and "codimension" refer to the set of $`\boldsymbol g\in\mathbb R^5`$ at fixed body data $`(\tau,m,N,\lambda_0)`$.

1. **Necessary and sufficient conditions.** For $`N=2`$ and for $`N\ge3`$:
   - (a) determine the set $`\mathcal U_4\subset\mathbb R^5`$ of $`\boldsymbol g`$ for which the fall from rest is the same for all levels, separately for the upper branch, the lower branch and both, and through the order $`v^2`$ (exactly, and at leading order in $`M_k/\tau`$);
   - (b) determine the rate at a place for the members of $`\mathcal C^+`$ (at zeroth order in the gradients, in the wide-start form of (3.23)), and the set $`\mathcal U_5`$ of $`\boldsymbol g`$ for which (4.24) holds with a non-zero common acceleration;
   - (c) give the dimension and the codimension of each set in $`\mathbb R^5`$.
2. **Stability.** For $`\boldsymbol g`$ at a distance $`\delta`$ from $`\mathcal U_4`$ (in a stated norm): determine the order in $`\delta`$ of the largest difference of $`a_{k,+}(0)`$ between two levels, and of the defect of (4.24).
3. **Requirements.** For each of the following candidate requirements on the coupling, determine (i) whether it is stated in the terms of the language, that is, whether it is well defined under every replacement of the listed terms that leaves the total contract unchanged (M6), and (ii) whether it is necessary for, sufficient for, or unrelated to membership in $`\mathcal U_4`$ (both branches, from rest) and in $`\mathcal U_5`$:
   - (R1) the body operator of the coupling is a multiple of the body's own on-site term as listed, $`\sigma_3\otimes(m\mathbb 1_N+D)`$;
   - (R2) on every level, the coupling multiplies the traceless part of the body's own on-site block on the branch label, and has no part proportional to $`\mathbb 1_2`$;
   - (R3) any further requirement the derivation finds that is stated in the terms of the language and selects $`\mathcal U_4`$ or $`\mathcal U_5`$; if there is none within $`\mathcal C^+`$, say so.
   For each requirement, give a member of $`\mathcal C^+`$ that satisfies it and fails item 4, or prove that there is none.
4. **Verdict.** From items 1–3: state whether, within $`\mathcal C^+`$, the couplings that give items 4 and 5 are typical (an open set), exceptional (a set of positive codimension), or selected by a requirement of item 3, with the order to which each statement holds.

## Inputs

From 04-branch-fall@v3 (this subproject). Setting there: the class $`\mathcal C_{\rm lev}`$ of level blocks $`C^{(k)}=\frac{\tau_k}2\sum_x\zeta_{x,k}\bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\bigr)+\sum_x\lvert x\rangle\langle x\rvert\otimes(M_{x,k}\sigma_3+V_{x,k}\mathbb 1_2)`$ with the linear level profiles $`M_{x,k}=M_k+G_kx`$, $`V_{x,k}=-\mathcal F_kx`$, $`\zeta_{x,k}=1+g_{\zeta,k}(x+\frac12)`$; branch starts at rest; first order in the gradients; $`v`$ is the drift velocity of the branch start at zero gradients; in the background of (17.15) of 03-ilang-space/17-motion, $`d_0=\kappa\sigma_X`$ is the distance of neighbouring positions, $`v_{\max}=\tau d_0`$, $`\bar x`$ is the mean position and $`\hat e:=e/\sigma_X`$ its unit direction ($`e:=(X-\langle X\rangle)\chi`$); $`r(x)`$ is the rate (3.23) at $`x`$.

Eq. (4.16) of 04-branch-fall:

```math
\boxed{\;a_{k,\sigma}(0)=\frac{\tau_k^2}{M_k}\,\bigl(\sigma\,\mathcal F_k-G_k\bigr)\;}
```

Eq. (4.17) of 04-branch-fall:

```math
a_{k,\sigma}=\frac{\tau^2}{M}(\sigma\mathcal F-G)+c_{2,k,\sigma}\,v^2+O(v^4),\qquad
c_{2,k,\sigma}=g_\zeta+\frac GM\Bigl(1+\frac{2M^2}{\tau^2}\Bigr)-\sigma\,\frac{\mathcal F}{M}\Bigl(\frac32+\frac{2M^2}{\tau^2}\Bigr).
```

Eq. (4.19) of 04-branch-fall, for every member of $`\mathcal C_{\rm lev}`$ with linear level profiles and $`N\ge2`$:

```math
\begin{aligned}
a_{k,+}(0)=a_+\ \forall k&\iff\frac{\tau_k^2}{M_k}(\mathcal F_k-G_k)=a_+\ \forall k,\qquad
a_{k,-}(0)=a_-\ \forall k\iff\frac{\tau_k^2}{M_k}(\mathcal F_k+G_k)=-a_-\ \forall k,\\
\text{both, with }a_+=a_-=a&\iff\mathcal F_k=0\ \text{ and }\ \frac{\tau_k^2G_k}{M_k}=-a\quad\forall k .
\end{aligned}
```

Eq. (4.20) of 04-branch-fall: in motion (upper branch), $`a_{k,+}`$ is the same function of $`v`$ through the order $`v^2`$ for all $`k`$ iff (i) $`\frac{\tau_k^2}{M_k}(\mathcal F_k-G_k)=a_0`$ for all $`k`$ and (ii), exactly,

```math
c_{2,k,+}=g_{\zeta,k}-\frac{\mathcal F_k}{2M_k}-\frac{a_0}{\tau_k^2}\Bigl(1+\frac{2M_k^2}{\tau_k^2}\Bigr)\quad\text{independent of }k .
```

Eq. (4.22) of 04-branch-fall, for the class $`\mathcal C`$ ($`\tau_k=\tau`$, $`M_k=m+d_k`$, $`G_k=mg_m+d_kg_\eta`$, $`\mathcal F_k=\mathcal F`$, $`g_{\zeta,k}=g_\zeta`$) and every $`N\ge2`$:

```math
a_{k,+}(0)\ \text{level-independent}\iff\mathcal F=m(g_m-g_\eta);\qquad a_{k,-}(0)\ \text{level-independent}\iff\mathcal F=-m(g_m-g_\eta);\qquad\text{value }-\tau^2g_\eta\text{ in each case};
```

Eq. (4.24) of 04-branch-fall, for the class $`\mathcal C`$ with $`a_{k,+}(0)=a\neq0`$ for all $`k`$, at first order in the gradients:

```math
\boxed{\;\frac{\mathrm d^2\bar x}{\mathrm d\lambda^2}\Big\vert_{\rm drift}=d_0\,a_{k,+}(0)\,\hat e=-\,\frac{v_{\max}^2}{d_0}\;\frac{r(x+1)-r(x)}{r(x)}\;\hat e\;}
```

From 03-clock-and-fall@v3 (this subproject). Setting there: the class $`\mathcal C`$ with the linear profiles $`m_x=m(1+g_mx)`$, $`\eta_x=1+g_\eta x`$, $`V_x=-\mathcal Fx`$, $`\zeta_x=1+g_\zeta(x+\frac12)`$; $`E^{\pm}_{x,k}:=V_x\pm M_{x,k}`$ are the on-site eigenvalues of the level $`k`$ at $`x`$ (modulo a common constant); $`r_W(x_0)`$ is the rate of the clock of a start of width $`W`$ at $`x_0`$, read from the advance of the clock distribution; $`\varsigma_W`$, $`\delta_W`$, $`\tau^0`$ are quantities of that start.

Eq. (3.23) of 03-clock-and-fall, the definition of the rate at $`x_0`$:

```math
\text{rate at }x_0:=\lim_{W\to\infty}r_W(x_0)=\frac{\eta_{x_0}}{\lambda_0}=\frac{N}{2\pi}\bigl(E^+_{x_0,k+1}-E^+_{x_0,k}\bigr),\ \ \text{tick }\frac{\lambda_0}{\eta_{x_0}};\qquad\text{at finite }W:\ \ r_W=\frac{\eta_{x_0}}{\lambda_0}(1-\varsigma_W),\ \ \text{tick }\frac{\lambda_0}{\eta_{x_0}(1-\varsigma_W)},\ \ \Bigl\lvert r_W-\frac{\eta_{x_0}}{\lambda_0}\Bigr\rvert\le\frac{\eta_{x_0}}{\lambda_0}\,\delta_W^2\frac{\tau^{0\,2}}{m_{x_0}^2}.
```

## Assumptions

- The setting under "Goal". The body, the class $`\mathcal C^+`$, the sharp field with a linear profile and the branch starts are assumptions of this package (M8, M9). A result for $`\mathcal C^+`$ says what the language allows in this class, not what it implies for every coupling (M10).
- The results of 04-branch-fall and 03-clock-and-fall apply to $`\mathcal C^+`$ where its members are members of their classes; where they are not (the rate for $`\mathcal F_1\neq0`$), the package derives what it needs.

## Scope

- **Class.** Items 1–4: the class $`\mathcal C^+`$, $`N\ge2`$ (with $`N=2`$ and $`N\ge3`$ separated where they differ).
- **Control.** Item 3 asks for a member that satisfies each requirement and fails item 4, or a proof that there is none.
- Out of scope: couplings that mix the branches or the clock levels; profiles that are not linear (15-curved-profile-fall); fields that are not sharp (09–12); bodies of two types (08-two-types); composite bodies (13, 16); second order in the gradients. The closing report combines these with the result of this package.

## Depth

- Item 1: short argument (from the quoted results; the rate for $`\mathcal F_1\neq0`$ derived) (needed by items 2–4 and criterion 10).
- Item 2: short argument (needed by criterion 10: robust or fine-tuned).
- Item 3: derive (needed by criterion 10: selected by a requirement of the language or not).
- Item 4: short argument (the answer to criterion 10 for one body).

## Expected result

- Item 1: sets given by equations in $`\boldsymbol g`$, with their dimensions and codimensions, for $`N=2`$ and $`N\ge3`$.
- Item 2: two orders in $`\delta`$.
- Item 3: for each requirement, two answers (well defined or not; necessary, sufficient or unrelated) with a control.
- Item 4: a classification with its orders.

Give every main result a tag $`(17.k)`$.

Consistency checks, at most three: for example the subclass $`\mathcal C`$ against (4.22), and Model D without a field.

## Code

None.
