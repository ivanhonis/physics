# Question: 04-neighbours

- **Subproject:** 03-ilang-space
- **Package:** 04-neighbours
- **Equation tags:** (4.k)
- **Created:** 2026-10-07

## Goal

From the witness angle alone, define which points of a part's view are neighbours, and define the distance along chains of neighbours. Then test both definitions on an explicit chain configuration. The notation introduced below ($`\asymp`$, $`\Gamma_V`$, $`\sim`$, $`N_V`$, $`\ell`$) is fixed for later packages. "Neighbour" and "chain distance" are defined notions in the sense of M1.

1. **Related points.** Call two distinct points $`x,x'\in X_V`$ related, $`x\asymp x'`$, if $`W(x,x')>0`$, equivalently $`\alpha(x,x')<\pi/2`$. Show that $`x\asymp x'`$ iff the view has a nonzero cross term between them: $`(V_A)_{hh'}\neq0`$ for (any, equivalently all) $`h\in x`$, $`h'\in x'`$. Let $`\Gamma_V`$ be the graph on $`X_V`$ whose edges are the related pairs.

2. **Neighbours.** Call two distinct points $`x,x'`$ neighbours, $`x\sim x'`$, if $`x\asymp x'`$ and no third point $`y\in X_V`$ satisfies
   ```math
   \max\bigl(\alpha(x,y),\alpha(y,x')\bigr)<\alpha(x,x').
   ```
   Let $`N_V`$ be the graph on $`X_V`$ whose edges are the neighbour pairs. Show:
   - (a) $`\sim`$ is symmetric and well defined in the sense of M6;
   - (b) $`\sim`$ depends only on the order of the values of $`\alpha`$: replacing $`\alpha`$ by $`g\circ\alpha`$ with any strictly increasing $`g`$ (and the condition $`\alpha<\pi/2`$ by $`g\circ\alpha<g(\pi/2)`$) gives the same relation;
   - (c) $`N_V`$ and $`\Gamma_V`$ have the same connected components.

3. **Chain distance.** For $`x,x'`$ in the same connected component of $`\Gamma_V`$, define
   ```math
   \ell(x,x'):=\min\Bigl\{\sum_{j=0}^{m-1}\alpha(y_j,y_{j+1})\;:\;y_0=x,\ y_m=x',\ y_j\sim y_{j+1}\ \text{for all } j\Bigr\},
   ```
   and set $`\ell(x,x'):=+\infty`$ for points in different components. Show that $`\ell`$ is a metric on each component, that $`\ell\ge\alpha`$, and that $`\ell(x,x')=\alpha(x,x')`$ whenever $`x\sim x'`$. Show by an example that $`\ell`$ can exceed $`\pi/2`$; item 4 may serve.

4. **Chain example.** Take a description with two objects $`a`$ and $`c`$ of different types, each the only instance of its type, so that (1.11) imposes no constraint. $`T(a)`$ has $`n\ge2`$ places $`h_1,\dots,h_n`$, and $`T(c)`$ has places $`k_1,\dots,k_{n+m-1}`$ with $`m\ge1`$. Let $`A=\{a\}`$, and consider the state
   ```math
   \lvert\Psi\rangle=\frac{1}{\sqrt n}\sum_{i=1}^{n}\lvert h_i\rangle\otimes\lvert E_i\rangle,
   \qquad
   \lvert E_i\rangle=\frac{1}{\sqrt m}\sum_{s=i}^{i+m-1}\lvert k_s\rangle ,
   ```
   in which the companion records the place $`h_i`$ with a blur of width $`m`$. Derive the points and their witness angles, the neighbour graph $`N_V`$, and the chain distance $`\ell`$, for every $`m\ge1`$.

## Inputs

From 02-view-content@v1. Notation fixed there: $`p_h:=\langle h\vert V_A\vert h\rangle`$, $`H_V:=\{h:p_h>0\}`$, $`\lvert\psi_h\rangle:=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle`$, and $`W(h,h')=\lvert G_{hh'}\rvert^2`$ with $`G_{hh'}=\langle E_{h'}\vert E_h\rangle`$.

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

From 03-witness-distance@v1. Notation fixed there: $`h\approx h'`$ iff $`W(h,h')=1`$; $`[h]`$ is the class of $`h`$; $`X_V:=H_V/{\approx}`$ is the set of points; $`\alpha(x,x'):=\arccos\sqrt{W(x,x')}\in[0,\pi/2]`$ is the witness angle.

Eq. (3.1):

```math
\varrho_h:=\lvert E_h\rangle\langle E_h\rvert=\frac{\lvert\psi_h\rangle\langle\psi_h\rvert}{p_h},
\qquad
h\approx h'\;\Longleftrightarrow\;W(h,h')=1\;\Longleftrightarrow\;\varrho_h=\varrho_{h'} .
```

Eq. (3.2):

```math
X_V:=H_V/{\approx},\qquad
\varrho_x:=\varrho_h,\qquad
W(x,x'):=W(h,h')=\mathrm{Tr}(\varrho_x\varrho_{x'})\qquad(h\in x,\ h'\in x'),
```

Eq. (3.3). Here $`\pi`$ is a type-preserving permutation of the objects, and the map below is the canonical bijection induced by $`h\mapsto h^\pi`$. It is the identity on $`X_V`$ when $`\pi`$ permutes only companion objects or only same-type instances inside $`A`$. The points and $`W`$ are well defined in the sense of M6.

```math
X_V^A\to X_V^{\pi(A)},\quad [h]\mapsto[h^\pi],\qquad
W^{\pi(A)}\bigl([h_1^\pi],[h_2^\pi]\bigr)=W^A\bigl([h_1],[h_2]\bigr).
```

Eq. (3.5). Here $`\alpha`$ is a metric on $`X_V`$.

```math
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}}
=\frac{\lvert\langle h\vert V_A\vert h'\rangle\rvert}{\sqrt{\langle h\vert V_A\vert h\rangle\langle h'\vert V_A\vert h'\rangle}},\qquad h\in x,\ h'\in x' .
```

## Assumptions

None beyond the base problem. The part $`A`$ and its companion $`\bar A`$ are both nonempty, and $`\lambda`$ is fixed.

## Scope

- In scope: the relation $`\asymp`$, the neighbour relation $`\sim`$ and the chain distance $`\ell`$ for one part at fixed $`\lambda`$, and the chain example of item 4.
- Out of scope:
  - other neighbour rules and comparisons between them;
  - whether the contract system couples only neighbours (locality);
  - dimension and limits of growing families;
  - evolution, several parts, and the phases of the cyclic products with $`k\ge3`$;
  - any physical or spatial meaning beyond the definitions (M1, M4).

## Depth

- Item 1: short argument.
- Item 2 (a) and (b): short argument.
- Item 2 (c): short argument. Standard facts about minimum spanning trees, such as the cut property, may be used without proof.
- Item 3: short argument. Standard facts about shortest-path metrics on graphs with positive edge weights may be used without proof.
- Item 4: derive.

## Expected result

- Item 1: the equivalence $`x\asymp x'\iff(V_A)_{hh'}\neq0`$.
- Item 2: statements (a)–(c).
- Item 3: $`\ell`$ is a metric on each component (an extended metric on $`X_V`$), $`\ell\ge\alpha`$, and $`\ell=\alpha`$ on neighbour pairs; an example with $`\ell>\pi/2`$.
- Item 4: closed forms for the witness angles, the neighbour graph and $`\ell`$, separately for $`m=1`$ and for $`m\ge2`$. If the computation does not give the following, report the discrepancy:
  - for $`m\ge2`$: the $`n`$ points $`x_i=[h_i]`$ are distinct, with $`\cos\alpha(x_i,x_j)=\max(0,m-\lvert i-j\rvert)/m`$;
  - $`N_V`$ is the chain $`x_1\sim x_2\sim\dots\sim x_n`$;
  - $`\ell(x_i,x_j)=\lvert i-j\rvert\arccos(1-1/m)`$;
  - for $`m=1`$ no two points are related.

Give every main result a tag $`(4.k)`$.

Consistency checks, at most three, chosen from:
- for a product state, $`X_V`$ is a single point, and there are no neighbours;
- in item 4 with $`m=1`$, all branch states are orthogonal and every component of $`\Gamma_V`$ is a single point;
- in item 4 with $`m\ge n`$, every two points are related, and $`N_V`$ is still the chain.

## Code

None.
