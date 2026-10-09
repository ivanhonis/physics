# Question: 12-identical-probes

- **Subproject:** 03-ilang-space
- **Package:** 12-identical-probes
- **Equation tags:** (12.k)
- **Created:** 2026-10-08

## Goal

Determine whether two identical probes, recorded by the same medium, assign the same distance to the same pair of places, and whether different cuts that contain these places agree. This is the cut-independence question in the language of this subproject. It needs first what Law 5 implies for the recording contracts of identical instances. The notation introduced below ($`K^{(1)}_h`$, $`K^{(2)}_h`$, $`\Delta`$) is fixed for later packages.

**Setting.**
- **Objects.** Three objects: the probes $`p_1`$ and $`p_2`$, of one type $`T`$ with places $`h\in H_T`$ and $`d_T\ge2`$, and the medium $`c`$, of a different type and the only instance of its type.
- **Contracts.** Each probe is recorded by the medium:
  ```math
  C=\sum_{h}\lvert h\rangle\langle h\rvert_{p_1}\otimes K^{(1)}_h+\sum_{h}\lvert h\rangle\langle h\rvert_{p_2}\otimes K^{(2)}_h ,
  ```
  with $`K^{(1)}_h`$, $`K^{(2)}_h`$ self-adjoint on $`\mathcal H_c`$, each extended by the identity on the other probe.
- **Notation.** $`P_{12}`$ is the swap of $`p_1`$ and $`p_2`$ (1.11), $`c_T`$ the family of $`T`$, and $`\mathcal H_{\rm adm}`$ the admissible subspace.

1. **Law 5 and the records.** For either family:
   - (a) Show that the evolution maps $`\mathcal H_{\rm adm}`$ into itself for every $`\lambda`$ iff $`(P_{12}CP_{12}-C)\,\mathcal H_{\rm adm}=0`$, and that in this setting this holds iff $`\Delta:=K^{(1)}_h-K^{(2)}_h`$ does not depend on $`h`$.
   - (b) Show that the contract system is swap-invariant, $`P_{12}CP_{12}=C`$, iff $`\Delta=0`$.
   - (c) Show that for an $`h`$-independent $`\Delta`$ the contract system is the swap-invariant one with $`K_h:=K^{(1)}_h`$, minus the medium-only term $`\mathbb 1_{p_1p_2}\otimes\Delta`$.

2. **Each probe sees the same background.** Let $`c_T=+1`$, let $`\Delta`$ be $`h`$-independent, and let the initial state be the admissible product $`\lvert\phi\rangle\otimes\lvert\phi\rangle\otimes\lvert\chi\rangle`$, with $`\phi_h\neq0`$ for every $`h`$. The single-instance views of $`p_1`$ and $`p_2`$ are equal (2.16). Show that their leading-order distance is
   ```math
   d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle ,
   ```
   the value (5.10) of a single probe recorded alone. Show also that it depends neither on $`\phi`$ nor on $`\Delta`$. Here the cut $`\{p_1\}\mid\{p_2,c\}`$ separates two identical instances, which is outside the setting of 11-cut-boundary. State whether the derivation of (11.5)–(11.8) carries over, and why.

3. **Cut consistency.** In the setting of item 2, take the cut $`\{p_1,p_2\}\mid\{c\}`$. Derive the leading-order distance between joint places $`(h_1,h_2)`$ and $`(h_1',h_2')`$ of the pair. Show:
   - joint places that differ by the swap are one point;
   - for joint places that differ only in the place of one probe, the pair distance equals the single-probe distance of item 2.

4. **The partner as a witness.** Let $`c_T=+1`$ and take the initial state $`\tfrac{1}{\sqrt2}\bigl(\lvert hh'\rangle+\lvert h'h\rangle\bigr)\otimes\lvert\chi\rangle`$ with $`h\neq h'`$. Show that already at $`\lambda=0`$ the single-instance view has $`W(h,h')=0`$: each probe is a perfect witness for the other. Conclude that the agreement of item 2 needs probes that are not correlated with each other.

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

From 05-recording-contract@v1. These hold in the setting of 05: one recorded object, one medium, the recording contract $`\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, and the initial state $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$.

Eq. (5.10):

```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
```

From 11-cut-boundary@v1. These hold in the setting of 11:
- no type has objects on both sides of the cut;
- $`C=C_A+C_{\bar A}+C_\partial`$;
- the initial state is the product $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\phi_h\neq0`$;
- $`Q_\chi:=\mathbb 1_{\bar A}-\lvert\chi\rangle\langle\chi\rvert`$, and $`v_h`$ is the first-order coefficient of $`\psi_h/\phi_h`$ in (11.5).

Eq. (11.6):

```math
Q_\chi\lvert v_h\rangle=Q_\chi C_{\bar A}\lvert\chi\rangle+\lvert u_h\rangle,\qquad
\lvert u_h\rangle=\frac{1}{\phi_h}\,Q_\chi\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)C_\partial\bigl(\lvert\phi\rangle\otimes\lvert\chi\rangle\bigr).
```

Eq. (11.8):

```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert .
```

## Assumptions

- The setting stated under "Goal". All contracts are independent of $`\lambda`$ (A5).
- Item 1 holds for every $`\lambda`$. Items 2 and 3 are statements for $`\lambda\to0^+`$. Item 4 is a statement at $`\lambda=0`$.

## Scope

- In scope:
  - the consequence of Law 5 for the recording contracts of two identical probes;
  - the single-instance and pair geometries at leading order for $`c_T=+1`$ and uncorrelated probes;
  - the partner as a witness.
- Out of scope:
  - the sign-changing family beyond item 1;
  - more than two probes;
  - orders beyond the leading one;
  - several media and bodies;
  - any physical or spatial meaning beyond the definitions (M1, M4).

## Depth

- Item 1: derive.
- Item 2: derive.
- Item 3: short argument.
- Item 4: short argument.

## Expected result

The main model expects the following. Derive each statement independently, and report any discrepancy.

- Item 1:
  - $`(P_{12}CP_{12}-C)(\lvert ab\rangle\otimes\xi)=\lvert ab\rangle\otimes\bigl(\Delta_b-\Delta_a\bigr)\xi`$, with $`\Delta_h:=K^{(1)}_h-K^{(2)}_h`$;
  - hence invariance of $`\mathcal H_{\rm adm}`$ iff $`\Delta_h`$ is $`h`$-independent;
  - swap invariance iff $`\Delta=0`$;
  - the decomposition of (c).
- Item 2:
  - the derivation of (11.5)–(11.8) is algebraic and uses only the product initial state and finite dimension, so it carries over;
  - with $`C_\partial=\sum_h\lvert h\rangle\langle h\rvert_{p_1}\otimes K_h`$ one gets $`u_h=\lvert\phi\rangle\otimes(K_h-\langle K_h\rangle)\lvert\chi\rangle`$, hence $`d_0`$ of (5.10);
  - $`\Delta`$ enters only $`C_{\bar A}`$, and $`\phi`$ enters only as a unit factor.
- Item 3:
  - $`d_0\bigl((h_1,h_2),(h_1',h_2')\bigr)=\lVert u_{h_1}+u_{h_2}-u_{h_1'}-u_{h_2'}\rVert`$;
  - swapped joint places coincide, by (3.4);
  - the one-probe differences reduce to item 2.
- Item 4: the branch vectors of the two places are $`\lvert h'\rangle\otimes\lvert\chi\rangle`$ and $`\lvert h\rangle\otimes\lvert\chi\rangle`$ up to normalization, which are orthogonal.

Give every main result a tag $`(12.k)`$.

Consistency checks, at most three, chosen from:
- with all $`K_h`$ equal, every distance vanishes;
- removing $`p_2`$ reproduces (5.10);
- the swap symmetry of the pair geometry in item 3.

## Code

None.
