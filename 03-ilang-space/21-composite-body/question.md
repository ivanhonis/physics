# Question: 21-composite-body

- **Subproject:** 03-ilang-space
- **Package:** 21-composite-body
- **Equation tags:** (21.k)
- **Created:** 2026-10-09

## Goal

Determine how a composite body, two bodies held together by a contract between them, responds as a whole to a cost gradient. In particular, determine whether its inertia is fixed by the inertias of its parts, and whether the cost of binding contributes to it. The notions defined below (centre, internal contract, uniform external gradient, total force, inverse inertia of the composite, scalar inertia) are fixed for later packages. They mean only what their definitions say (M1, M2, M4). Rates are rates with respect to $`\lambda`$; a physical time is criterion 8 and not part of this package.

**Setting.**
- **Objects.** Two bodies and a medium, of pairwise different types, each the only instance of its type, so (1.11) imposes no constraint: $`b_1`$ of type $`T_1`$ with places $`h\in H_1`$, $`b_2`$ of type $`T_2`$ with places $`k\in H_2`$ ($`d_1,d_2\ge2`$), and the medium $`c`$.
- **Contract.**
  ```math
  C=C_1\otimes\mathbb 1\otimes\mathbb 1+\mathbb 1\otimes C_2\otimes\mathbb 1+\sum_h\lvert h\rangle\langle h\rvert\otimes\mathbb 1\otimes K^{(1)}_h+\sum_k\mathbb 1\otimes\lvert k\rangle\langle k\rvert\otimes K^{(2)}_k+W\otimes\mathbb 1_c ,
  ```
  in the order $`b_1,b_2,c`$. Here $`C_1=\sum_{h,h'}t^{(1)}_{hh'}\lvert h\rangle\langle h'\rvert`$ and $`C_2=\sum_{k,k'}t^{(2)}_{kk'}\lvert k\rangle\langle k'\rvert`$ are hopping terms with $`t^{(i)}`$ Hermitian matrices, and $`K^{(1)}_h`$, $`K^{(2)}_k`$ are self-adjoint on $`\mathcal H_c`$. The **binding contract** is the pair term $`W=\sum_{h,k}W_{hk}\,\lvert h\rangle\langle h\rvert\otimes\lvert k\rangle\langle k\rvert`$ between $`b_1`$ and $`b_2`$, with real $`W_{hk}`$. By A5 the single-object terms are contained in pair terms; which ones is a convention. The **internal contract** is $`C_{\rm body}:=C_1\otimes\mathbb 1+\mathbb 1\otimes C_2+W`$ on $`\mathcal H_1\otimes\mathcal H_2`$.
- **Start.** $`\lvert\Phi\rangle\otimes\lvert\chi\rangle`$, with a unit vector $`\Phi\in\mathcal H_1\otimes\mathcal H_2`$ (it may be entangled) and a unit vector $`\chi\in\mathcal H_c`$.
- **Notation.** $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, $`\epsilon^{(i)}_h:=\langle K^{(i)}_h\rangle`$, $`\lvert u^{(1)}_h\rangle:=(K^{(1)}_h-\epsilon^{(1)}_h)\lvert\chi\rangle`$, $`\lvert u^{(2)}_k\rangle:=(K^{(2)}_k-\epsilon^{(2)}_k)\lvert\chi\rangle`$, and $`g(v,w):=\mathrm{Re}\langle v\vert w\rangle`$ on $`\mathcal H_c`$. $`p^{(1)}_h`$ and $`p^{(2)}_k`$ are the place weights of the views of $`\{b_1\}`$ and $`\{b_2\}`$. $`\Delta^{(1)}_{hh'}:=u^{(1)}_h-u^{(1)}_{h'}`$ and $`\Delta^{(2)}_{kk'}:=u^{(2)}_k-u^{(2)}_{k'}`$. $`E_1`$ and $`E_2`$ are the edge sets of the hopping graphs of $`b_1`$ and $`b_2`$.

**Definitions.**
- **Background.** As in 17 and 20, the background of each body is the record geometry of (5.10)–(5.11) built from its $`u^{(i)}`$. Both lie in $`(\mathcal H_c,g)`$. The background is fixed by the $`K^{(i)}`$ and $`\chi`$, also when $`\Phi`$ is entangled.
- **Positions, centre, acceleration.** $`\bar x_1:=\sum_hp^{(1)}_hu^{(1)}_h`$, $`\bar x_2:=\sum_kp^{(2)}_ku^{(2)}_k`$, the **centre** $`\bar R:=\tfrac12(\bar x_1+\bar x_2)`$, and $`A:=\mathrm d^2\bar R/\mathrm d\lambda^2`$.
- **Edge costs of each body.** As defined in 20, with the part $`\{b_i\}`$ and its companion (the other body and the medium): $`L^{(1)}_{hh'}`$ for the pairs of places of $`b_1`$, and $`L^{(2)}_{kk'}`$ for those of $`b_2`$, built from the blocks of the total $`C`$ and the branch vectors of $`\{b_i\}`$.
- **Single-body expressions.** $`\mu_1:=-\sum_{\{h,h'\}\in E_1}L^{(1)}_{hh'}(0)\,\Delta^{(1)}_{hh'}\,g(\Delta^{(1)}_{hh'},\cdot\,)`$, and $`\mu_2`$ likewise for $`b_2`$: the expression (20.10) evaluated with the edge costs of $`b_i`$ in the joint start.
- **Uniform external gradient, total force, inverse inertia of the composite.** For $`f\in\mathcal H_c`$ let
  ```math
  G_f:=\sum_hg\bigl(f,u^{(1)}_h\bigr)\lvert h\rangle\langle h\rvert\otimes\mathbb 1\otimes\mathbb 1+\sum_kg\bigl(f,u^{(2)}_k\bigr)\,\mathbb 1\otimes\lvert k\rangle\langle k\rvert\otimes\mathbb 1 ,
  ```
  the same uniform gradient acting on both bodies. The force on each body is $`F:=-f`$, and the **total force** is $`F_{\rm tot}:=2F`$. The **inverse inertia of the composite** $`\mu_c`$ is the real-linear map on $`(\mathcal H_c,g)`$, if one exists, with
  ```math
  A(0)\big|_{C+G_f}-A(0)\big|_{C}=\mu_c\,F_{\rm tot}\qquad\text{for every }f\in\mathcal H_c .
  ```

1. **Well-definedness.** Determine whether $`\bar R`$, $`A`$ and $`\mu_c`$ are well defined (M6). Check:
   - the split (16.3) between the two recording contracts;
   - every other placement of single-object terms (A5), for example of a term acting on $`b_1`$ alone in $`W`$ instead of $`C_1`$;
   - the common phase (1.2) and the phase split (1.6).

   Determine whether $`\bar x_1-\bar x_2`$ is well defined.

2. **Acceleration of the centre.**
   - (a) Determine whether (20.6)–(20.7) apply to each body in this setting, with the companion of $`b_i`$ consisting of the other body and the medium. Using them, determine $`A(\lambda)`$ exactly for every $`\lambda`$, and determine which of its terms contain $`W`$.
   - (b) For the start $`\Phi\otimes\chi`$, determine $`A(0)`$ in closed form. Determine the **$`W`$-terms** of $`A(0)`$, i.e. $`A(0)-A(0)\big|_{W=0}`$ at fixed $`\Phi`$. Determine whether they vanish for every $`\Phi`$. Determine a sufficient condition on $`\Phi`$ (and on $`W`$, if needed) under which they vanish.

3. **Inertia of the composite.** For the start $`\Phi\otimes\chi`$:
   - (a) Determine $`\mu_c`$. Determine whether it is a function of the edge costs $`L^{(1)}(0)`$, $`L^{(2)}(0)`$ and the background alone. Compare it with $`\mu_1`$ and $`\mu_2`$.
   - (b) Determine whether $`\mu_c`$ depends on $`W`$ other than through $`\Phi`$. Determine whether it is symmetric with respect to $`g`$, and when it is positive semidefinite.

4. **Example: bound pair on the chain.**
   - **Setting of the example.** Both bodies live on the chain of 17: $`b_1`$ has the places $`h_m`$ and $`b_2`$ the places $`k_m`$, $`m\in\mathbb Z`$. The hopping is the same for both: $`C_1=t\sum_m\bigl(\lvert h_m\rangle\langle h_{m+1}\rvert+\lvert h_{m+1}\rangle\langle h_m\rvert\bigr)`$ with $`t>0`$, and $`C_2`$ likewise on the $`k_m`$. The records are linear and identical: $`K^{(1)}_{h_m}=K^{(2)}_{k_m}=m\,X`$, with one $`X`$, $`\sigma_X>0`$ and $`e:=(X-\langle X\rangle)\chi`$. The binding is on-site: $`W=U\sum_m\lvert h_m\rangle\langle h_m\rvert\otimes\lvert k_m\rangle\langle k_m\rvert`$ with real $`U<0`$.
   - **Starts and costs.** Use starts of finite support. $`E_{\min}(t,U):=\inf\mathrm{spec}C_{\rm body}`$ on $`\ell^2(\mathbb Z)\otimes\ell^2(\mathbb Z)`$.
   - **Items.**
     - (a) State the spectrum of $`C_{\rm body}`$: the two-body continuum and the bound states as functions of the total quasi-momentum, and $`E_{\min}(t,U)`$.
     - (b) **Composite at rest.** Consider sequences of starts $`\Phi_n\otimes\chi`$ with $`\langle\Phi_n\vert C_{\rm body}\vert\Phi_n\rangle\to E_{\min}(t,U)`$. Determine the limit of $`\mu_c`$ along such sequences, and whether it depends on the sequence. Write the limit as $`\mu_c=I_c^{-1}\,\hat e\,g(\hat e,\cdot\,)`$ with $`\hat e:=e/\sigma_X`$, and determine the **scalar inertia** $`I_c(t,U,\sigma_X)`$.
     - (c) Determine in the same way the scalar inertia $`I_1`$ of one body alone on this chain, as in 20: sequences of starts with $`\langle C_1\rangle\to\inf\mathrm{spec}C_1`$, inertia from (20.10). Determine also $`I_c`$ at $`U=0`$. Compare $`I_c(t,U,\sigma_X)`$ with $`2I_1`$.
     - (d) Let $`E_{\rm bind}:=E_{\min}(t,U)-E_{\min}(t,0)`$, and let $`v_{\max}=2t\sigma_X`$ be the maximal speed (17.20).
       - Determine whether $`I_c-2I_1`$ is a function of $`E_{\rm bind}`$ and $`v_{\max}`$ alone, and if so, which function.
       - Determine whether $`I_c\,v_{\max}^2`$ is a function of $`E_{\min}`$ alone, and whether such a relation is unchanged under $`C\to C+c\,\mathbb 1`$.
     - (e) Along the sequences of (b), determine the limit of the $`W`$-terms of $`A(0)`$. Determine whether $`\lim A(0)=\lim\mu_c\,F_{\rm tot}`$, where $`F_{\rm tot}=2F`$ and $`F`$ is the force of (20.12).

## Inputs

From 02-view-content@v1. Notation fixed there: $`p_h:=\langle h\vert V_A\vert h\rangle`$, $`\lvert\psi_h\rangle:=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle`$.

Eq. (2.1):

```math
\lvert\Psi\rangle=\sum_h\lvert h\rangle\otimes\lvert\psi_h\rangle,
\qquad
\lvert\psi_h\rangle=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle=\sum_r\Psi_{hr}\lvert r\rangle,
\qquad
\sum_h\lVert\psi_h\rVert^2=\lVert\Psi\rVert^2=1 .
```

Eq. (2.2):

```math
V_A=\sum_{h,h'}\langle\psi_{h'}\vert\psi_h\rangle\,\lvert h\rangle\langle h'\rvert,
\qquad\text{i.e.}\qquad
(V_A)_{hh'}=\langle\psi_{h'}\vert\psi_h\rangle,
\qquad
p_h=\lVert\psi_h\rVert^2 .
```

From 05-recording-contract@v1. These hold in the setting of 05: one recorded object, one medium object, the recording contract $`\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, and the start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\phi_h\neq0`$ for all $`h`$. Notation fixed there: $`g(v,w):=\mathrm{Re}\langle v\vert w\rangle`$, and $`h\sim_0h'`$ iff $`u_h=u_{h'}`$.

Eq. (5.10):

```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
```

Eq. (5.11):

```math
\bigl(H_V/{\sim_0},\,d_0\bigr)\;\cong\;\bigl(\{u_h:h\in H_V\},\,\lVert\cdot\rVert\bigr)\subset(\mathcal H_c,g).
```

From 16-common-space@v2. These hold in the setting of 16: three objects of pairwise different types, $`a`$ of type $`A`$ with places $`h`$, $`b`$ of type $`B`$ with places $`k`$, and the medium $`c`$, with $`C=\sum_h\lvert h\rangle\langle h\rvert_a\otimes K^A_h+\sum_k\lvert k\rangle\langle k\rvert_b\otimes K^B_k`$ and $`u^A_h`$, $`u^B_k`$ the record vectors. In the notation of this question, $`a,A\to b_1,T_1`$ and $`b,B\to b_2,T_2`$. Eq. (16.3) lists all replacements of the record operators that leave $`C`$ unchanged:

```math
K'^A_h=K^A_h+Z,\qquad K'^B_k=K^B_k-Z,\qquad Z=Z^\dagger\ \text{on }\mathcal H_c\ \text{arbitrary.}
```

Eq. (16.4):

```math
u^A_h\mapsto u^A_h+z,\qquad u^B_k\mapsto u^B_k-z,\qquad \lvert z\rangle=(Z-\langle Z\rangle)\lvert\chi\rangle .
```

From 17-motion@v2, for the chain of 17 (one body with places $`h_m`$, $`C_b=t(S+S^\dagger)`$, $`S:=\sum_m\lvert h_m\rangle\langle h_{m+1}\rvert`$, $`K_{h_m}=m\,X`$, $`e:=(X-\langle X\rangle)\chi`$, $`\lVert e\rVert=\sigma_X`$). Eq. (17.15):

```math
d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X,\qquad \bar x=\bar m\,e,\quad \bar m:=\sum_mm\,p_{h_m},\qquad s^2=\sigma_X^2\sum_m(m-\bar m)^2p_{h_m} .
```

From Step 10 of 17, verbatim: "The bound (17.7) for this chain: $`a=t\sigma_X(S+S^\dagger)`$, whose largest spectral value and row sum are both $`2t\sigma_X`$." Eq. (17.20):

```math
v_{\max}=2t\,\sigma_X .
```

From 20-cost-and-mass@v2. Definitions fixed in its question, for an object $`b`$ that is the only instance of its type, the part $`A=\{b\}`$ and branch vectors $`\psi_h`$ of (2.1): blocks $`C_{hh'}:=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\,C\,\bigl(\lvert h'\rangle\otimes\mathbb 1_{\bar A}\bigr)`$; site cost $`L_h:=\langle\psi_h\vert C_{hh}\vert\psi_h\rangle`$; edge cost $`L_{hh'}:=2\mathrm{Re}\langle\psi_h\vert C_{hh'}\vert\psi_{h'}\rangle`$ for $`h\neq h'`$; in the body–medium setting of 20, site cost per unit weight $`\Omega_h:=\langle\chi\vert C_{hh}\vert\chi\rangle=t_{hh}+\epsilon_h`$, force $`F:=-f`$ for a uniform gradient $`\Omega_h-\Omega_{h'}=g(f,u_h-u_{h'})`$, and $`\Delta_{hh'}:=u_h-u_{h'}`$. Eq. (20.1), for every description satisfying A1–A7:

```math
C=\sum_{h,h'}\lvert h\rangle\langle h'\rvert\otimes C_{hh'},\quad C_{h'h}=C_{hh'}^\dagger,\qquad
i\frac{\mathrm d}{\mathrm d\lambda}\lvert\psi_h\rangle=\sum_{h'}C_{hh'}\lvert\psi_{h'}\rangle .
```

From Step 4 of 20, verbatim: "By (20.1), $`\dot p_h=2\mathrm{Re}\langle\psi_h\vert\dot\psi_h\rangle`$. The term with $`C_{hh}`$ drops out because it is real, so"

Eq. (20.6):

```math
\frac{\mathrm dp_h}{\mathrm d\lambda}=\sum_{h'\neq h}J_{h'\to h},\qquad J_{h'\to h}:=2\mathrm{Im}\langle\psi_h\vert C_{hh'}\vert\psi_{h'}\rangle=-J_{h\to h'} .
```

From Step 4 of 20, verbatim: "Since the $`u_h`$ do not depend on $`\lambda`$: $`a=\sum_h\ddot p_hu_h=\sum_{h\neq h'}\dot J_{h'\to h}u_h=\sum_{\{h,h'\}}\dot J_{h'\to h}\Delta_{hh'}`$, by antisymmetry." "By (20.1), $`\langle\dot\psi_h\rvert=i\sum_k\langle\psi_k\rvert C_{kh}`$, so $`\frac{\mathrm d}{\mathrm d\lambda}\langle\psi_h\vert C_{hh'}\vert\psi_{h'}\rangle=i\sum_k\bigl[\langle\psi_k\vert C_{kh}C_{hh'}\vert\psi_{h'}\rangle-\langle\psi_h\vert C_{hh'}C_{h'k}\vert\psi_k\rangle\bigr]`$. Separating $`k=h`$ in the first sum and $`k=h'`$ in the second gives the exact identity"

Eq. (20.7), where $`E`$ is the set of cost edges:

```math
a(\lambda)=\sum_{\{h,h'\}\in E}\bigl[A_{hh'}+B_{hh'}\bigr]\Delta_{hh'},\qquad
\begin{aligned}
A_{hh'}&=2\mathrm{Re}\bigl[\langle\eta_h\vert C_{hh'}\vert\psi_{h'}\rangle-\langle\psi_h\vert C_{hh'}\vert\eta_{h'}\rangle\bigr],\quad \lvert\eta_h\rangle:=\textstyle\sum_{k\neq h}C_{hk}\lvert\psi_k\rangle,\\
B_{hh'}&=2\mathrm{Re}\langle\psi_h\vert C_{hh}C_{hh'}-C_{hh'}C_{h'h'}\vert\psi_{h'}\rangle .
\end{aligned}
```

Eq. (20.10), in the body–medium setting of 20 with the product start $`\phi\otimes\chi`$, where $`a_0`$ is $`a(0)`$ at equal $`\Omega_h`$ and $`\mu`$ is defined by $`a(0)=a_0+\mu F`$ for every uniform gradient produced by varying the $`t_{hh}`$:

```math
a(0)=a_0+\mu F,\qquad \mu=-\sum_{\{h,h'\}\in E}L_{hh'}(0)\,\Delta_{hh'}\,g\bigl(\Delta_{hh'},\,\cdot\,\bigr) .
```

Eq. (20.12), for the chain of 17:

```math
\Omega_{h_m}=m\langle X\rangle,\qquad F=-\frac{\langle X\rangle}{\sigma_X^2}\,e .
```

Eq. (20.13), for the chain of 17 ($`a^{\rm hop}:=\sum_EA_{hh'}\Delta_{hh'}`$):

```math
a^{\rm hop}(\lambda)\equiv0,\qquad a_0=0\ \text{ for every start of finite support} .
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5), and $`\lambda\ge0`$.
- Items 1–3 are exact. Item 2(a) holds for every $`\lambda`$; items 2(b) and 3 concern $`\lambda=0`$.
- Item 4 works on $`\ell^2(\mathbb Z)\otimes\ell^2(\mathbb Z)\otimes\mathcal H_c`$, as the limit of long finite chains (A1), with starts of finite support. The sums over places must converge; state the moment bounds that are needed, as 20 does for one body.

## Scope

- In scope:
  - two bodies of different types, bound by a contract that is diagonal in their places, and recorded by one medium;
  - the acceleration of their centre, and its response to a uniform external gradient at $`\lambda=0`$;
  - the bound pair on the chain with on-site attractive binding.
- Out of scope:
  - $`\lambda>0`$ beyond the exact identity of item 2(a);
  - bodies of identical types, and composites of more than two bodies;
  - other hopping graphs or dimensions, and repulsive binding ($`U>0`$);
  - whether the cost of the composite acts on other bodies;
  - a physical time (criterion 8);
  - any physical or spatial meaning beyond the definitions (M1, M2, M4).

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: derive.
- Item 4(a): standard (state the results used).
- Item 4(b)–(d): derive.
- Item 4(e): short argument.

## Expected result

- Item 1: invariance statements; a yes/no answer for $`\bar x_1-\bar x_2`$.
- Item 2: an applicability statement and an exact identity; the $`W`$-terms in closed form; a yes/no answer and a sufficient condition.
- Item 3: a closed form for $`\mu_c`$; yes/no answers; a comparison; a positivity condition.
- Item 4: the standard spectrum; closed forms for $`I_c`$, $`I_1`$ and $`I_c`$ at $`U=0`$ in $`t`$, $`U`$, $`\sigma_X`$; a comparison; yes/no answers and, where yes, the functions; a limit and a yes/no answer.

Give every main result a tag $`(21.k)`$.

Consistency checks, at most three: for example $`U=0`$ (two independent bodies), strong binding $`\lvert U\rvert\gg t`$, and dimensions.

## Code

None.
