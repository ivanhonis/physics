# Neighbours and chain distance from the witness angle

- **Subproject:** 03-ilang-space
- **Package:** 03-ilang-space/04-neighbours
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-07

## Setup and assumptions

A description satisfying A1–A7 is fixed, with a part $`A`$ and a nonempty companion $`\bar A`$, at fixed $`\lambda`$, in the joint state $`\lvert\Psi\rangle`$. No further assumption and no approximation is made. All quantities are dimensionless.

Inputs, as quoted in `question.md`:

- From 02-view-content@v1: $`\lvert\psi_h\rangle=(\langle h\rvert\otimes\mathbb 1_{\bar A})\lvert\Psi\rangle`$ (2.1); $`(V_A)_{hh'}=\langle\psi_{h'}\vert\psi_h\rangle`$ and $`p_h=\langle h\vert V_A\vert h\rangle=\lVert\psi_h\rVert^2`$ (2.2); $`H_V=\{h:p_h>0\}`$; $`W(h,h')=\lvert G_{hh'}\rvert^2`$ with $`G_{hh'}=\langle E_{h'}\vert E_h\rangle`$.
- From 03-witness-distance@v1: $`h\approx h'\iff W(h,h')=1\iff\varrho_h=\varrho_{h'}`$ (3.1); the points $`X_V=H_V/{\approx}`$, and $`W(x,x')=W(h,h')=\mathrm{Tr}(\varrho_x\varrho_{x'})`$ for any $`h\in x`$, $`h'\in x'`$ (3.2); for a type-preserving permutation $`\pi`$ of the objects, the canonical bijection $`[h]\mapsto[h^\pi]`$ from $`X_V^A`$ to $`X_V^{\pi(A)}`$ preserves $`W`$. It is the identity when $`\pi`$ permutes only companion objects or only same-type instances inside $`A`$, and the points and $`W`$ are well defined in the sense of M6 (3.3). The witness angle $`\alpha(x,x')=\arccos\sqrt{W(x,x')}\in[0,\pi/2]`$ is a metric on $`X_V`$, with
```math
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}},\qquad h\in x,\ h'\in x'\qquad\text{(3.5)}.
```

Facts and conventions used:
- $`X_V`$ is finite, because $`H_V`$ is a subset of the finite set of joint places of $`A`$ (A1).
- For distinct points, $`\alpha(x,x')>0`$, because $`\alpha`$ is a metric.
- A graph on $`X_V`$ is a set of unordered pairs of distinct points (its edges).
- A chain from $`x`$ to $`x'`$ is a sequence $`y_0=x,\dots,y_m=x'`$ in which consecutive elements are joined by edges; $`m=0`$ is allowed when $`x=x'`$.
- Components are the classes of the relation "joined by a chain".

## Derivation

### Step 1. Related points (item 1)

For distinct $`x,x'\in X_V`$ define
```math
x\asymp x'\;:\Longleftrightarrow\;W(x,x')>0\;\Longleftrightarrow\;\alpha(x,x')<\pi/2 .
\tag{4.1}
```
The two forms are equivalent because $`\arccos`$ is strictly decreasing on $`[0,1]`$ with $`\arccos0=\pi/2`$. The relation is symmetric, because $`W(x,x')=\mathrm{Tr}(\varrho_x\varrho_{x'})`$ is symmetric. $`\Gamma_V`$ is the graph on $`X_V`$ whose edges are the pairs with $`x\asymp x'`$.

**Claim.**
```math
x\asymp x'\;\Longleftrightarrow\;(V_A)_{hh'}\neq0\quad\text{for one, equivalently for every, pair } h\in x,\ h'\in x' .
\tag{4.2}
```
*Argument.* Take any $`h\in x`$ and $`h'\in x'`$. They lie in $`H_V`$, so $`p_h,p_{h'}>0`$. By (3.5), $`\lvert(V_A)_{hh'}\rvert=\sqrt{p_hp_{h'}\,W(x,x')}`$, which is nonzero iff $`W(x,x')>0`$. By (3.2), $`W(x,x')`$ does not depend on the chosen representatives. Hence a nonzero cross term for one pair of representatives is equivalent to $`x\asymp x'`$, which is in turn equivalent to a nonzero cross term for every pair.

### Step 2. Neighbours: symmetry and well-definedness (item 2a)

For distinct $`x,x'\in X_V`$ define
```math
x\sim x'\;:\Longleftrightarrow\;x\asymp x'\ \text{ and there is no } y\in X_V \text{ with } \max\bigl(\alpha(x,y),\alpha(y,x')\bigr)<\alpha(x,x') .
\tag{4.3}
```
$`N_V`$ is the graph whose edges are the pairs with $`x\sim x'`$.

Two remarks used below:
- $`y=x`$ and $`y=x'`$ never satisfy the inequality: for $`y=x`$ the maximum equals $`\alpha(x,x')`$, since $`\alpha(x,x)=0`$, and similarly for $`y=x'`$. A violating $`y`$ is therefore automatically a third point.
- For a related pair, a violating $`y`$ has $`\alpha(x,y),\alpha(y,x')<\alpha(x,x')<\pi/2`$, so $`x\asymp y`$ and $`y\asymp x'`$.

*Symmetry.* $`\asymp`$ is symmetric (Step 1) and so is $`\alpha`$. For each $`y`$, the condition for the ordered pair $`(x',x)`$ reads $`\max(\alpha(x',y),\alpha(y,x))<\alpha(x',x)`$, which is the same as the condition for $`(x,x')`$. Hence $`\sim`$ is symmetric, $`N_V`$ is an undirected graph, and its edge set is contained in that of $`\Gamma_V`$.

*M6.* Definition (4.3) uses only the set $`X_V`$ and the function $`\alpha`$ on it. Let $`\Phi:X_V\to X_V'`$ be a bijection with $`\alpha'(\Phi x,\Phi x')=\alpha(x,x')`$. As $`y`$ runs over $`X_V`$, $`\Phi y`$ runs over $`X_V'`$, so the conditions (4.3) for $`(x,x')`$ and for $`(\Phi x,\Phi x')`$ coincide term by term. Hence $`x\sim x'\iff\Phi x\sim'\Phi x'`$, and the same holds for $`\asymp`$. Apply this to the bijection of (3.3), which preserves $`W`$ and therefore $`\alpha`$:
- a relabelling $`\pi`$ of the objects maps $`N_V^A`$ isomorphically onto $`N_V^{\pi(A)}`$;
- when $`\pi`$ permutes only companion objects or only same-type instances inside $`A`$, the bijection is the identity, so $`N_V`$ is unchanged (Law 5).

The common phase (1.2) and the phase split in (1.6) cannot enter either: $`X_V`$ and $`W`$ depend on $`\Psi`$ only through the $`\varrho_h`$ (3.1), and these are well defined in the sense of M6 (3.3). The same holds for $`\Gamma_V`$.

### Step 3. Only the order of the angles matters (item 2b)

Let $`g`$ be strictly increasing on $`[0,\pi/2]`$ and let $`\beta=g\circ\alpha`$. Define $`\sim_g`$ by (4.3), with $`\alpha`$ replaced by $`\beta`$ and the condition $`\alpha<\pi/2`$ replaced by $`\beta<g(\pi/2)`$. For $`u,v\in[0,\pi/2]`$:
- $`g(u)<g(v)\iff u<v`$;
- $`\max(g(u),g(v))=g(\max(u,v))`$.

Hence $`\beta(x,x')<g(\pi/2)\iff\alpha(x,x')<\pi/2`$, and for every $`y`$, $`\max(\beta(x,y),\beta(y,x'))<\beta(x,x')\iff\max(\alpha(x,y),\alpha(y,x'))<\alpha(x,x')`$. So $`\sim_g=\sim`$.

With $`g(t)=1-\cos t`$ (where $`g(\pi/2)=1`$) this gives the form used in item 4:
```math
x\sim x'\iff\cos\alpha(x,x')>0\ \text{ and no } y \text{ has } \min\bigl(\cos\alpha(x,y),\cos\alpha(y,x')\bigr)>\cos\alpha(x,x') .
\tag{4.4}
```
With $`g(t)=\sin^2t`$, the same statement holds with $`\cos\alpha`$ replaced by $`W`$. In words: $`x`$ and $`x'`$ are neighbours iff their branch states overlap, and no third point overlaps more strongly with both.

### Step 4. $`N_V`$ and $`\Gamma_V`$ have the same components (item 2c)

**Claim.** Every related pair $`x\asymp x'`$ is joined by a chain in $`N_V`$.

*Argument.* Use strong induction over the finitely many values that $`\alpha`$ takes on related pairs ($`X_V`$ is finite). Assume the claim for every related pair with a smaller angle than $`\alpha(x,x')`$.
- If $`x\sim x'`$, the one-step chain joins them.
- Otherwise, (4.3) gives a $`y`$ with $`\alpha(x,y)<\alpha(x,x')`$ and $`\alpha(y,x')<\alpha(x,x')`$. By Step 2, $`y\notin\{x,x'\}`$, and $`x\asymp y`$ and $`y\asymp x'`$ are related pairs with smaller angles. By the hypothesis, each of them is joined by a chain in $`N_V`$, and concatenating the two chains joins $`x`$ to $`x'`$.

For the smallest value no such $`y`$ can exist, so that pair is a neighbour pair; this covers the start of the induction.

Every edge of $`N_V`$ is an edge of $`\Gamma_V`$ (Step 2), so every $`N_V`$-chain is a $`\Gamma_V`$-chain. Conversely, replacing each edge of a $`\Gamma_V`$-chain by an $`N_V`$-chain from the Claim gives an $`N_V`$-chain with the same ends. Hence
```math
x,x'\ \text{are joined in }\Gamma_V\iff x,x'\ \text{are joined in }N_V ,
\tag{4.5}
```
and $`N_V`$ and $`\Gamma_V`$ have the same connected components.

### Step 5. The chain distance (item 3)

```math
\ell(x,x'):=\min\Bigl\{\sum_{j=0}^{m-1}\alpha(y_j,y_{j+1})\;:\;y_0=x,\ y_m=x',\ y_j\sim y_{j+1}\Bigr\},
\qquad \ell(x,x'):=+\infty\ \text{between components.}
\tag{4.6}
```
By (4.5), a chain exists exactly when $`x`$ and $`x'`$ lie in the same component of $`\Gamma_V`$. On such a component, $`\ell`$ is the shortest-path distance of the finite connected graph $`N_V`$ with positive edge weights $`\alpha(y,y')>0`$. By the standard result, the minimum is attained (on a simple path) and is a metric.

The value $`+\infty`$ between components keeps the triangle inequality $`\ell(x,z)\le\ell(x,y)+\ell(y,z)`$: if $`x`$ and $`z`$ lie in different components, then $`y`$ lies in a different component from at least one of them, and the right side is $`+\infty`$. Hence $`\ell`$ is an extended metric on $`X_V`$.

*$`\ell\ge\alpha`$.* For any chain, the triangle inequality of $`\alpha`$ (3.5), applied repeatedly, gives $`\alpha(x,x')\le\sum_j\alpha(y_j,y_{j+1})`$. Taking the minimum gives $`\ell\ge\alpha`$; between components, $`\ell=+\infty`$.

*$`\ell=\alpha`$ on neighbours.* If $`x\sim x'`$, the chain $`(x,x')`$ gives $`\ell(x,x')\le\alpha(x,x')`$. Together with $`\ell\ge\alpha`$:
```math
\ell\ \text{is an extended metric on } X_V,\qquad \ell\ge\alpha,\qquad \ell(x,x')=\alpha(x,x')\ \text{ if } x\sim x' .
\tag{4.7}
```
An example with $`\ell>\pi/2`$ is (4.14) in Step 10.

### Step 6. Chain example: branch data and view (item 4)

$`a`$ and $`c`$ have different types and each is the only instance of its type. No pair of objects falls under (1.11), so $`\mathcal H_{\rm adm}=\mathcal H`$ and $`\lvert\Psi\rangle`$ is admissible. Write $`S_i=\{i,\dots,i+m-1\}\subseteq\{1,\dots,n+m-1\}`$ for the support of $`\lvert E_i\rangle`$.

1. By (2.1), $`\lvert\psi_{h_i}\rangle=n^{-1/2}\lvert E_i\rangle`$, and $`\lVert E_i\rVert^2=\lvert S_i\rvert/m=1`$. So $`p_{h_i}=1/n>0`$ and $`H_V=\{h_1,\dots,h_n\}`$, and (1.6) holds with $`a_{h_i}=n^{-1/2}`$ and $`\lvert E_{h_i}\rangle=\lvert E_i\rangle`$.
2. Since the $`\lvert k_s\rangle`$ are orthonormal, $`G_{h_ih_j}=\langle E_j\vert E_i\rangle=\lvert S_i\cap S_j\rvert/m`$.
3. Let $`d=\lvert i-j\rvert`$. Then $`S_i\cap S_j=\{\max(i,j),\dots,\min(i,j)+m-1\}`$, which has $`m-d`$ elements if $`d<m`$ and is empty otherwise.
4. By (2.2), $`(V_A)_{h_ih_j}=\langle\psi_{h_j}\vert\psi_{h_i}\rangle=G_{h_ih_j}/n`$.

Hence
```math
G_{h_ih_j}=\frac{\max(0,\,m-\lvert i-j\rvert)}{m},\qquad (V_A)_{h_ih_j}=\frac1n\,G_{h_ih_j}.
\tag{4.8}
```

### Step 7. Points and witness angles (all $`m\ge1`$)

By (4.8), $`W(h_i,h_j)=G_{h_ih_j}^2`$, and this equals $`1`$ iff $`i=j`$. So for every $`m\ge1`$ the $`n`$ points $`x_i=[h_i]`$ are distinct, $`X_V=\{x_1,\dots,x_n\}`$, and
```math
\cos\alpha(x_i,x_j)=\frac{\max(0,\,m-\lvert i-j\rvert)}{m},\qquad
\alpha(x_i,x_j)=\begin{cases}\arccos\bigl(1-\lvert i-j\rvert/m\bigr), & \lvert i-j\rvert<m,\\[2pt] \pi/2, & \lvert i-j\rvert\ge m.\end{cases}
\tag{4.9}
```
By (4.1), $`x_i\asymp x_j\iff1\le\lvert i-j\rvert\le m-1`$. So $`\Gamma_V`$ is the band graph with these edges:
```math
x_i\asymp x_j\iff 1\le\lvert i-j\rvert\le m-1 .
\tag{4.10}
```

### Step 8. The case $`m=1`$

Here $`\lvert E_i\rangle=\lvert k_i\rangle`$ are mutually orthogonal, and (4.9) gives $`\alpha(x_i,x_j)=\pi/2`$ for all $`i\neq j`$. By (4.10), no two points are related. $`\Gamma_V`$ and $`N_V`$ have no edges, every point is its own component, and by (4.6)
```math
m=1:\qquad \Gamma_V=N_V=\text{no edges},\qquad \ell(x_i,x_j)=\begin{cases}0,&i=j,\\+\infty,&i\neq j.\end{cases}
\tag{4.11}
```

### Step 9. The neighbour graph for $`m\ge2`$

Let $`c(e)=\max(0,m-e)/m`$ for integers $`e\ge0`$. It is strictly decreasing on $`\{0,\dots,m\}`$ and zero for $`e\ge m`$.
1. Take a related pair, so $`d=\lvert i-j\rvert\in\{1,\dots,m-1\}`$ and $`c(d)>0`$.
2. For any integer $`e\ge0`$, $`c(e)>c(d)\iff e<d`$. Indeed, $`e<d`$ gives $`c(e)>c(d)`$ by the strict decrease. If $`d\le e\le m`$, then $`c(e)\le c(d)`$, and if $`e>m`$, then $`c(e)=0<c(d)`$.
3. By (4.4) and (4.9), $`x_i\not\sim x_j`$ iff some index $`k`$ has $`\lvert i-k\rvert<d`$ and $`\lvert k-j\rvert<d`$.
4. If $`d\ge2`$, the index $`k=i+\mathrm{sgn}(j-i)`$ gives $`\lvert i-k\rvert=1<d`$ and $`\lvert k-j\rvert=d-1<d`$, so the pair is not a neighbour pair.
5. If $`d=1`$, the condition $`\lvert i-k\rvert<1`$ forces $`k=i`$, and then $`\lvert k-j\rvert=1\not<1`$. So the pair is a neighbour pair; it is related because $`m\ge2`$.

```math
m\ge2:\qquad x_i\sim x_j\iff\lvert i-j\rvert=1,\qquad N_V:\ x_1\sim x_2\sim\dots\sim x_n .
\tag{4.12}
```

### Step 10. The chain distance for $`m\ge2`$

By (4.9), every edge of $`N_V`$ has weight $`\theta_m:=\alpha(x_i,x_{i+1})=\arccos(1-1/m)\in(0,\pi/2)`$. Take $`i<j`$ without loss of generality. By (4.12), a chain from $`x_i`$ to $`x_j`$ is a walk on $`\{1,\dots,n\}`$ with steps $`\pm1`$. It must cross each edge $`\{k,k+1\}`$ with $`i\le k<j`$ at least once, because that edge separates $`i`$ from $`j`$ in the path graph. So its length is at least $`(j-i)\theta_m`$, and the monotone chain $`x_i,x_{i+1},\dots,x_j`$ attains this bound. Hence
```math
m\ge2:\qquad \ell(x_i,x_j)=\lvert i-j\rvert\,\arccos\Bigl(1-\frac1m\Bigr).
\tag{4.13}
```
*Example with $`\ell>\pi/2`$ (item 3).* Take $`n=3`$ and $`m=2`$. Then $`\theta_2=\arccos\frac12=\frac\pi3`$, and by (4.9), with $`\lvert1-3\rvert=2=m`$,
```math
\ell(x_1,x_3)=\frac{2\pi}{3}>\frac{\pi}{2}=\alpha(x_1,x_3).
\tag{4.14}
```

## Result

- **Item 1:** $`x\asymp x'\iff W(x,x')>0\iff\alpha(x,x')<\pi/2`$ (4.1), which holds iff $`(V_A)_{hh'}\neq0`$ for one, equivalently every, pair of representatives (4.2).
- **Item 2:** $`\sim`$ (4.3) is:
  - (a) symmetric and well defined in the sense of M6: relabellings act as graph isomorphisms of $`N_V`$, and as the identity for permutations inside $`\bar A`$ or of same-type instances inside $`A`$;
  - (b) invariant under $`\alpha\mapsto g\circ\alpha`$ for strictly increasing $`g`$, in particular expressible through $`\cos\alpha`$ or $`W`$ (4.4);
  - (c) $`N_V`$ and $`\Gamma_V`$ have the same components (4.5).
- **Item 3:** $`\ell`$ (4.6) is an extended metric on $`X_V`$ (a metric on each component), with $`\ell\ge\alpha`$ and $`\ell=\alpha`$ on neighbour pairs (4.7). An example with $`\ell>\pi/2`$ is (4.14).
- **Item 4:**
  - For every $`m\ge1`$, the points $`x_i=[h_i]`$ are distinct, with $`\cos\alpha(x_i,x_j)=\max(0,m-\lvert i-j\rvert)/m`$ (4.9), and $`x_i\asymp x_j\iff1\le\lvert i-j\rvert\le m-1`$ (4.10).
  - For $`m=1`$, no two points are related and $`\ell=+\infty`$ off the diagonal (4.11).
  - For $`m\ge2`$, $`N_V`$ is the chain $`x_1\sim\dots\sim x_n`$ (4.12), and $`\ell(x_i,x_j)=\lvert i-j\rvert\arccos(1-1/m)`$ (4.13).

## Consistency checks

1. **Product state.** Take $`\lvert\Psi\rangle=\lvert\phi\rangle\otimes\lvert\chi\rangle`$. Then $`\lvert\psi_h\rangle=\phi_h\lvert\chi\rangle`$, so all $`\varrho_h=\lvert\chi\rangle\langle\chi\rvert`$ coincide, and by (3.1) $`X_V`$ is a single point. There are no distinct pairs, so $`\Gamma_V`$ and $`N_V`$ have no edges and $`\ell\equiv0`$. The cross terms $`(V_A)_{hh'}=\phi_h\phi_{h'}^*\neq0`$ occur only between places of the same point, consistent with (4.2), which concerns distinct points only.
2. **$`m=1`$ via the view.** By (4.8), $`V_A=\frac1n\sum_i\lvert h_i\rangle\langle h_i\rvert`$ is diagonal. By (4.2) alone, no two points are related, so every component of $`\Gamma_V`$ is a single point. This agrees with (4.11), which was obtained from the angles, and with (4.5).
3. **$`m\ge n`$.** Then $`\lvert i-j\rvert\le n-1\le m-1`$ for all pairs, so $`\Gamma_V`$ is complete by (4.10), while $`N_V`$ is still the chain (4.12): Step 9 used only $`d\le m-1`$. Take $`n=m=3`$: $`\ell(x_1,x_3)=2\arccos\frac23\approx1.682>\alpha(x_1,x_3)=\arccos\frac13\approx1.231`$. This agrees with $`\ell\ge\alpha`$ (4.7), with strict inequality for a related pair that is not a neighbour pair.

## Open issues

- Comparison with the expected result: no discrepancy in the closed forms.
  - The points $`x_i`$ are distinct for every $`m\ge1`$, not only for $`m\ge2`$.
  - Formula (4.13) holds only for $`m\ge2`$. At $`m=1`$, $`\ell=+\infty`$ off the diagonal (4.11), not $`\lvert i-j\rvert\pi/2`$.
- Definition (4.3) uses a strict inequality, so ties do not remove an edge. For example, if all distinct pairs have the same $`W>0`$, then $`N_V`$ is complete. Whether this is the desired behaviour is a question about other neighbour rules, which is out of scope.
- That $`\ell`$ is well defined in the sense of M6 was not asked. It follows as in Step 2, since $`\ell`$ is built from $`N_V`$ and $`\alpha`$ only.

## Methods used

- Matrix elements of the partial trace; overlaps of branch states
- Quotient by an equivalence relation; angle metric
- Invariance under strictly increasing reparametrization
- Strong induction over a finite ordered set
- Shortest-path (extended) metrics on graphs with positive edge weights
- Counting the overlap of integer intervals
