# Question: 15-bodies

- **Subproject:** 03-ilang-space
- **Package:** 15-bodies
- **Equation tags:** (15.k)
- **Created:** 2026-10-08

## Goal

Determine what a body, its position and the distance between two bodies of one type are in the leading-order witness geometry of a recording medium. Determine whether these notions are well defined, and whether the state of the medium determines them. The notions defined below (background, localized body, position, configuration, two-body distance $`D`$, state of the medium) are fixed for later packages. They mean only what their definitions say (M1, M4).

**Setting.**
- **Objects.** The bodies are objects of one type $`T`$, with places $`h\in H_T`$ and $`d_T\ge2`$. The medium $`c`$ is one object of another type, the only instance of its type. The notation $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$ and $`\lvert u_h\rangle:=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$ is that of (5.10).
- **(S1) One body.** One object $`b`$ of type $`T`$, the only instance of $`T`$. The contract is $`C=\sum_h\lvert h\rangle\langle h\rvert_b\otimes K_h`$, with $`K_h`$ self-adjoint on $`\mathcal H_c`$. The start is $`\lvert\beta\rangle\otimes\lvert\chi\rangle`$ for a place $`\beta`$.
- **(S2) Two bodies.** Two objects $`b_1,b_2`$ of type $`T`$, the only instances of $`T`$, with family $`c_T=\pm1`$. The contract is (12.7) with $`p_1,p_2`$ renamed $`b_1,b_2`$ and an $`h`$-independent $`\Delta`$; by (12.3) and (12.7), this is the general contract of the setting of 12 for which the evolution preserves admissibility. The start is $`\lvert\beta_1\beta_2\rangle_{c_T}\otimes\lvert\chi\rangle`$, where $`\lvert\beta_1\beta_2\rangle_{c_T}`$ is the unit vector proportional to $`\lvert\beta_1\beta_2\rangle+c_T\lvert\beta_2\beta_1\rangle`$, with $`\beta_1\neq\beta_2`$ if $`c_T=-1`$.

**Definitions.**
- **Background.** The background of $`T`$ is the leading-order record geometry $`(H_T/{\sim_0},d_0)`$ of (5.10) and (5.11), built from the $`u_h`$. Its points are written $`[h]_0`$. By (5.10) and (12.12), it is the leading-order geometry of the single-instance view for every product start with $`\phi_h\neq0`$ for all $`h`$: $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ in (S1), and $`\lvert\phi\rangle\otimes\lvert\phi\rangle\otimes\lvert\chi\rangle`$ in (S2) with $`c_T=+1`$.
- **Localized body, position.** In (S1), the body is localized at the point $`x`$ of the background if every place in $`H_V`$ of its view lies in $`x`$. Its position is then $`x`$.
- **Configuration, two-body distance.** In (S2), the pair is localized at the unordered pair $`\{x_1,x_2\}`$ of points ($`x_1=x_2`$ allowed) if every joint place $`(h_1,h_2)\in H_V`$ of the view of $`\{b_1,b_2\}`$ satisfies $`\{[h_1]_0,[h_2]_0\}=\{x_1,x_2\}`$ as multisets. This unordered pair is the configuration. The positions of the two bodies are $`x_1`$ and $`x_2`$, and their two-body distance is $`D:=d_0(x_1,x_2)`$.
- **State of the medium.** The state of the medium is its view $`V_{\{c\}}`$ (1.5). When it is pure, $`V_{\{c\}}=\lvert E\rangle\langle E\rvert`$, two such states are the same at leading order if $`1-\lvert\langle E\vert E'\rangle\rvert^2=o(\lambda^2)`$ as $`\lambda\to0^+`$.

1. **One body (S1).**
   - (a) Determine the exact state, whether the body is localized at $`[\beta]_0`$ for every $`\lambda`$, and the state of the medium.
   - (b) Determine a necessary and sufficient condition under which two places $`\beta,\beta'`$ give the same state of the medium for every $`\lambda`$, and one under which they give the same state at leading order. Relate both conditions to the background.

2. **Two bodies (S2), either family.**
   - (a) Determine the exact state. Determine whether the pair stays localized at $`\{[\beta_1]_0,[\beta_2]_0\}`$, whether it becomes correlated with the medium, and the state of the medium.
   - (b) Determine whether the positions and $`D`$ are well defined (M6), in particular whether they depend on the description labels, on the split (12.6) or on $`\Delta`$.
   - (c) Determine the single-instance view and the view of $`\{b_1,b_2\}`$ in this state, and whether their witness data depend on $`D`$.
   - (d) Determine a necessary and sufficient condition, in terms of the record vectors, under which two starts give the same state of the medium at leading order, and a sufficient condition under which they give the same state for every $`\lambda`$. Relate the first condition to the pair geometry (12.13).
   - (e) Determine whether $`D`$ is in general a function of the state of the medium at leading order. Determine a necessary and sufficient condition on the record vectors under which the state of the medium at leading order distinguishes all configurations.

3. **Examples.** (S2) with $`\Delta=0`$, for either family; $`i`$ is an index.
   - (a) **Line.** The places are $`h_1,\dots,h_n`$ with $`n\ge2`$, and $`K_{h_i}=i\,X`$, where $`X`$ is self-adjoint on $`\mathcal H_c`$ and $`\sigma_X:=(\langle X^2\rangle-\langle X\rangle^2)^{1/2}>0`$.
   - (b) **Window.** The places are $`h_1,\dots,h_n`$ with $`n\ge2`$, and the window width is $`m\ge1`$. The medium has the places $`\{0,1\}^L`$ with $`L:=n+m-1`$, and $`\lvert\chi\rangle=\lvert0\cdots0\rangle`$. The operator $`\sigma_x^{[l]}`$ maps each place of $`c`$ to the place with bit $`l`$ flipped, and $`K_{h_i}:=\sum_{l=i}^{i+m-1}\sigma_x^{[l]}`$.

   For each example, determine $`D`$ and $`d_0`$ of the background, the pairs of configurations that give the same state of the medium (for every $`\lambda`$, and at leading order), and whether $`D`$ is a function of the state of the medium.

## Inputs

From 02-view-content@v1. Notation fixed there: $`p_h:=\langle h\vert V_A\vert h\rangle`$, $`H_V:=\{h:p_h>0\}`$, $`\lvert\psi_h\rangle:=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle`$, $`G_{hh'}=\langle E_{h'}\vert E_h\rangle`$.

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

Eq. (2.11):

```math
W(h)=1,\qquad W(h,h')=\lvert G_{hh'}\rvert^2=\frac{\lvert(V_A)_{hh'}\rvert^2}{p_hp_{h'}} .
```

Eq. (2.16). Here $`\pi`$ is a permutation of the objects with $`T(\pi(a))=T(a)`$, and $`(h^\pi)_{\pi(a)}:=h_a`$. For every admissible state:

```math
p^{\pi(A)}_{h^\pi}=p^A_h,\qquad H_V^{\pi(A)}=\{h^\pi:h\in H_V^A\},\qquad W^{\pi(A)}(h_1^\pi,\dots,h_k^\pi)=W^A(h_1,\dots,h_k).
```

From 03-witness-distance@v1. Notation fixed there: $`h\approx h'`$ iff $`W(h,h')=1`$; $`X_V:=H_V/{\approx}`$; $`\alpha(x,x'):=\arccos\sqrt{W(x,x')}\in[0,\pi/2]`$.

Eq. (3.4). Here $`a\neq b`$ are objects of $`A`$ of the same type $`T`$, and $`h^{(ab)}`$ is $`h`$ with the entries $`a,b`$ exchanged.

```math
\lvert\psi_h\rangle=\bigl(\langle h^{(ab)}\rvert\otimes\mathbb 1_{\bar A}\bigr)P_{ab}\lvert\Psi\rangle=c_T\,\lvert\psi_{h^{(ab)}}\rangle .
```

Eq. (3.5). Here $`\alpha`$ is a metric on $`X_V`$.

```math
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}}
=\frac{\lvert\langle h\vert V_A\vert h'\rangle\rvert}{\sqrt{\langle h\vert V_A\vert h\rangle\langle h'\vert V_A\vert h'\rangle}},\qquad h\in x,\ h'\in x' .
```

From 05-recording-contract@v1. These hold in the setting of 05: one recorded object, one medium object, and the recording contract $`\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$. (5.6), (5.10) and (5.11) are for the start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\phi_h\neq0`$ for all $`h`$. Notation fixed there: $`g(v,w):=\mathrm{Re}\langle v\vert w\rangle`$, and $`h\sim_0h'`$ iff $`u_h=u_{h'}`$.

Eq. (5.1):

```math
e^{-iC\lambda}=\sum_h\lvert h\rangle\langle h\rvert\otimes e^{-iK_h\lambda}.
```

Eq. (5.6):

```math
W(h,h';\lambda)=\bigl\lvert\langle\chi\vert e^{iK_{h'}\lambda}e^{-iK_h\lambda}\vert\chi\rangle\bigr\rvert^2 .
```

Eq. (5.10):

```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
```

Eq. (5.11):

```math
\bigl(H_V/{\sim_0},\,d_0\bigr)\;\cong\;\bigl(\{u_h:h\in H_V\},\,\lVert\cdot\rVert\bigr)\subset(\mathcal H_c,g).
```

From 12-identical-probes@v1. These hold in the setting of 12: probes $`p_1,p_2`$ of one type $`T`$ with $`d_T\ge2`$, a medium $`c`$ that is the only instance of its type, the contract $`C=\sum_h\lvert h\rangle\langle h\rvert_{p_1}\otimes K^{(1)}_h+\sum_h\lvert h\rangle\langle h\rvert_{p_2}\otimes K^{(2)}_h`$, and $`\Delta_h:=K^{(1)}_h-K^{(2)}_h`$, written $`\Delta`$ when it does not depend on $`h`$, with $`K_h:=K^{(1)}_h`$. (12.12)–(12.14) hold for $`c_T=+1`$, an $`h`$-independent $`\Delta`$ and the start $`\lvert\phi\rangle\otimes\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\phi_h\neq0`$ for all $`h`$. (12.12) is for the view of $`\{p_1\}`$; (12.13) and (12.14) are for the view of $`\{p_1,p_2\}`$, with companion $`\{c\}`$.

Eq. (12.3):

```math
e^{-iC\lambda}\mathcal H_{\rm adm}\subseteq\mathcal H_{\rm adm}\ \ \forall\lambda
\iff(P_{12}CP_{12}-C)\,\mathcal H_{\rm adm}=0
\iff\Delta_h=\Delta\ \text{ for all }h .
```

Eq. (12.6), the freedom of splitting the same $`C`$ into its two contract terms:

```math
K^{(1)}_h\to K^{(1)}_h+X,\qquad K^{(2)}_h\to K^{(2)}_h-X,\qquad \Delta_h\to\Delta_h+2X,\qquad X=X^\dagger\ \text{on }\mathcal H_c .
```

Eq. (12.7), for $`h`$-independent $`\Delta`$:

```math
C=\sum_h\bigl(\lvert h\rangle\langle h\rvert_{p_1}+\lvert h\rangle\langle h\rvert_{p_2}\bigr)\otimes K_h-\mathbb 1_{p_1p_2}\otimes\Delta .
```

Eq. (12.12):

```math
d_0(h,h')=\lim_{\lambda\to0^+}\frac{\alpha^{\{p_1\}}(h,h';\lambda)}{\lambda}=\bigl\lVert u_h-u_{h'}\bigr\rVert,\qquad\lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
```

Eq. (12.13):

```math
d_0\bigl((h_1,h_2),(h_1',h_2')\bigr)=\bigl\lVert u_{h_1}+u_{h_2}-u_{h_1'}-u_{h_2'}\bigr\rVert .
```

Eq. (12.14):

```math
W\bigl((h_1,h_2),(h_2,h_1);\lambda\bigr)=1\qquad\forall\lambda .
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5).
- "Leading order" refers to $`\lambda\to0^+`$. Statements "for every $`\lambda`$" are exact.

## Scope

- In scope:
  - one body, and two bodies of one type, recorded by one medium, with the localized starts of (S1) and (S2);
  - the leading order, and the exact statements asked for;
  - the two examples.
- Out of scope:
  - contracts that move bodies, and motion;
  - bodies of different types, and more than two bodies;
  - whether the background is the geometry of some view for $`c_T=-1`$;
  - distances other than $`d_0`$, such as the finite-$`\lambda`$ witness angle or chain distances;
  - the cost;
  - any physical or spatial meaning beyond the definitions (M1, M4).

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: derive.

## Expected result

- Item 1: a closed form for the state, and two equivalences.
- Item 2: a closed form for the state; statements on localization, correlation and well-definedness; the two views; an equivalence and a sufficient condition; a yes/no answer and an equivalence.
- Item 3: closed forms for $`D`$ and $`d_0`$; the pairs of configurations with the same state of the medium; a yes/no answer for each example.

Give every main result a tag $`(15.k)`$.

Consistency checks, at most three: for example $`\beta_1=\beta_2`$ for $`c_T=+1`$, a change of split (12.6), and $`m=1`$ in the window example.

## Code

None.
