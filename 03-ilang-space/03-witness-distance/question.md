# Question: 03-witness-distance

- **Subproject:** 03-ilang-space
- **Package:** 03-witness-distance
- **Equation tags:** (3.k)
- **Created:** 2026-10-07

## Goal

Define points and a distance from the witness data in the view of a part $`A`$, and determine how far the choice of the distance is fixed. The notation introduced below ($`\approx`$, $`[h]`$, $`X_V`$, $`\alpha`$) is fixed for later packages. "Point" and "distance" are defined notions in the sense of M1; no further spatial meaning is attached to them.

1. **Points.** On the present places $`H_V`$ of $`A`$, define $`h\approx h'`$ iff $`W(h,h')=1`$. Show:
   - (a) $`W(h,h')=1`$ iff $`\lvert E_h\rangle`$ and $`\lvert E_{h'}\rangle`$ differ only by a phase, that is, iff the companion does not witness the difference between $`h`$ and $`h'`$;
   - (b) $`\approx`$ is an equivalence relation, and $`W(h,h')`$ depends only on the classes $`[h]`$ and $`[h']`$;
   - (c) the set of classes $`X_V:=H_V/{\approx}`$, whose elements are the points, and $`W`$ on $`X_V`$ are well defined in the sense of M6;
   - (d) if $`A`$ contains several instances of the same type, then present joint places of $`A`$ that differ only by a permutation of these instances lie in the same point.

2. **Witness angle.** For points $`x=[h]`$ and $`x'=[h']`$, define
   ```math
   \alpha(x,x'):=\arccos\sqrt{W(h,h')}\in[0,\pi/2].
   ```
   State that $`\alpha`$ is a metric on $`X_V`$, and express $`\cos\alpha`$ through matrix elements of $`V_A`$.

3. **Distances from the witness data.** Consider candidate distances $`d=g\circ\alpha`$ with $`g:[0,\pi/2]\to[0,\infty)`$; equivalently, functions of the pair invariant $`W`$.
   - (a) **Realizability.** Show that every triple $`(\alpha_1,\alpha_2,\alpha_3)\in[0,\pi/2]^3`$ that satisfies the three triangle inequalities occurs, in some description, as the witness angles $`\bigl(\alpha(x_1,x_2),\alpha(x_2,x_3),\alpha(x_1,x_3)\bigr)`$ of the points of three present places. Give a sufficient condition on the description. An example of such a condition: the companion contains an object of a type with at least three places, and that type does not occur in $`A`$.
   - (b) **Characterization.** Conclude that $`g\circ\alpha`$ is a metric on $`X_V`$ for every description iff three conditions hold: $`g(0)=0`$; $`g>0`$ on $`(0,\pi/2]`$; and $`g(\alpha_3)\le g(\alpha_1)+g(\alpha_2)`$ for every such triple. Give a simple sufficient condition, for example that $`g`$ is nondecreasing and subadditive.
   - (c) **Candidates.** Decide for each of the following candidates whether it is a metric for every description: $`\alpha`$, $`\sqrt{1-W}`$, $`\sqrt{2(1-\sqrt W)}`$, $`1-\sqrt W`$, $`1-W`$, and $`\sqrt{-\ln W}`$ (the last one on descriptions with all $`W>0`$). For each candidate that fails, give a realizable triple that violates the triangle inequality. For each candidate that qualifies, state its range.

4. **Additivity.** Call three points aligned, with $`x'`$ between $`x`$ and $`x''`$, if $`\alpha(x,x'')=\alpha(x,x')+\alpha(x',x'')`$. Take $`g`$ as in item 3, and in addition nondecreasing or continuous. Show that $`g\circ\alpha`$ is additive on every aligned triple,
   ```math
   g\bigl(\alpha(x,x'')\bigr)=g\bigl(\alpha(x,x')\bigr)+g\bigl(\alpha(x',x'')\bigr),
   ```
   iff $`g(\alpha)=c\,\alpha`$ with a constant $`c>0`$. The argument uses that aligned triples are realizable for every pair of angles with sum at most $`\pi/2`$.

## Inputs

From 02-view-content@v1.

Notation fixed there: $`p_h:=\langle h\vert V_A\vert h\rangle`$ and $`H_V:=\{h : p_h>0\}`$, where $`h`$ runs over the joint places of $`A`$; $`\lvert\psi_h\rangle:=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle`$; $`G_{hh'}:=\langle E_{h'}\vert E_h\rangle`$ for $`h,h'\in H_V`$; $`W(h_1,\dots,h_k):=G_{h_1h_2}G_{h_2h_3}\cdots G_{h_{k-1}h_k}G_{h_kh_1}`$.

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

Eq. (2.7), the general decomposition (1.6), with arbitrary real $`\theta_h`$:

```math
a_h=\sqrt{p_h}\,e^{-i\theta_h},\qquad \lvert E_h\rangle=e^{i\theta_h}\,\frac{\lvert\psi_h\rangle}{\sqrt{p_h}}\qquad(h\in H_V),\qquad a_h=0\qquad(h\notin H_V),
```

Eq. (2.8):

```math
G_{hh'}=\langle E_{h'}\vert E_h\rangle=e^{i(\theta_h-\theta_{h'})}\,\frac{(V_A)_{hh'}}{\sqrt{p_hp_{h'}}},\qquad h,h'\in H_V .
```

Eq. (2.11):

```math
W(h)=1,\qquad W(h,h')=\lvert G_{hh'}\rvert^2=\frac{\lvert(V_A)_{hh'}\rvert^2}{p_hp_{h'}} .
```

Eq. (2.16). Here $`\pi`$ is a permutation of the objects with $`T(\pi(a))=T(a)`$, and $`(h^\pi)_{\pi(a)}:=h_a`$. For every admissible state:

```math
p^{\pi(A)}_{h^\pi}=p^A_h,\qquad H_V^{\pi(A)}=\{h^\pi:h\in H_V^A\},\qquad W^{\pi(A)}(h_1^\pi,\dots,h_k^\pi)=W^A(h_1,\dots,h_k).
```

## Assumptions

None beyond the base problem. The part $`A`$ and its companion $`\bar A`$ are both nonempty, and $`\lambda`$ is fixed.

## Scope

- In scope:
  - one part $`A`$ and one admissible state at fixed $`\lambda`$;
  - points as classes of present places;
  - distances as functions of the pair invariant $`W(h,h')`$.
- Out of scope:
  - neighbourhood, locality, paths and geodesics beyond item 4, and dimension;
  - the cyclic products $`W(h_1,\dots,h_k)`$ with $`k\ge3`$ and the phases they carry;
  - evolution, several parts, and comparison of the points of different parts;
  - any physical or spatial meaning beyond the definitions (M1, M4).

## Depth

- Item 1: short argument.
- Item 2: standard. $`\alpha`$ is the angle between the rays of $`\lvert E_h\rangle`$ and $`\lvert E_{h'}\rangle`$, and that this angle is a metric on rays may be used without proof. The expression for $`\cos\alpha`$ takes one line.
- Item 3 (a): derive.
- Item 3 (b): short argument.
- Item 3 (c): short argument for each candidate.
- Item 4: short argument. The solution of Cauchy's functional equation for monotone or continuous functions may be used without proof.

## Expected result

- Item 1: the equivalence relation and its classes, with statements (a)–(d).
- Item 2: $`\alpha`$ is a metric on $`X_V`$, and $`\cos\alpha(x,x')=\lvert(V_A)_{hh'}\rvert/\sqrt{p_hp_{h'}}`$.
- Item 3: an explicit realization of the triples; the if-and-only-if characterization with a sufficient condition; and for each candidate a verdict, with a counterexample triple or the range.
- Item 4: the if-and-only-if statement $`g=c\,\alpha`$.

Give every main result a tag $`(3.k)`$.

Consistency checks, at most three, chosen from:

- for a product state, $`X_V`$ consists of a single point;
- for mutually orthogonal branch states, every two distinct points are at witness angle $`\pi/2`$;
- for two present places, $`\cos\alpha`$ equals the modulus of the overlap $`\langle E_1\vert E_0\rangle`$ in the two-branch witness rule (base problem, Section 3).

## Code

None.
