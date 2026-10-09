# Question: 09-measurability

- **Subproject:** 03-ilang-space
- **Package:** 09-measurability
- **Equation tags:** (9.k)
- **Created:** 2026-10-08

## Goal

Determine how readings on the companion affect the view of a part and its witness geometry: the points, the witness angle $`\alpha`$ and the chain distance $`\ell`$. In particular, determine in which sense a distant reading, or a distant choice of how the system is cut, can or cannot change a local distance. The notation introduced below ($`\Pi^{\bar A}_r`$, $`\Psi_r`$, $`p(r)`$, $`W_r`$) is fixed for later packages.

**Setting.** A description satisfying A1–A7. A part $`A`$ with nonempty companion $`\bar A`$, at fixed $`\lambda`$, in an admissible state $`\lvert\Psi\rangle`$. A reading on the companion is a partition of the joint places of $`\bar A`$ into classes $`S^{\bar A}_r`$, lifted to the joint places of the system as in A4 with $`A`$ and $`\bar A`$ exchanged. Write $`\Pi^{\bar A}_r`$ for the projector onto the span of $`S^{\bar A}_r`$ in $`\mathcal H_{\bar A}`$, and $`\Pi_r=\mathbb 1_A\otimes\Pi^{\bar A}_r`$. The reading is label-free: each class is invariant under every swap of same-type objects of $`\bar A`$.

1. **Grouping of the companion.** Show that $`V_A`$, and hence $`X_V`$, $`\alpha`$, $`\sim`$ and $`\ell`$, depend only on $`\lvert\Psi\rangle`$ and on the set $`A`$. They do not depend on how the companion is grouped into subsets, or on the order of its factors.

2. **State update.** For a label-free reading on $`\bar A`$ with outcome $`r`$, derive:
   - the outcome probability $`p(r)`$;
   - the post-reading state $`\lvert\Psi_r\rangle`$, by (1.3);
   - its branch vectors $`\lvert\psi^{(r)}_h\rangle`$;
   - its view $`V_A(\Psi_r)`$.

   Show that $`\lvert\Psi_r\rangle`$ is admissible.

3. **No signalling on average.** Show that $`\sum_rp(r)\,V_A(\Psi_r)=V_A(\Psi)`$. Conclude that the statistics of every local reading on $`A`$, averaged over the outcomes of the distant reading, do not depend on whether the distant reading was made, nor on which label-free distant reading was chosen.

4. **The geometry after one outcome.** For places $`h,h'`$ that are present in $`\Psi_r`$, derive the witness data $`W_r(h,h')`$ of the post-reading state in terms of the branch vectors of $`\Psi`$. Show by an explicit example that a distant reading can change the local witness geometry for a given outcome. One example should do all of the following:
   - one outcome merges two points of $`A`$, so that $`\alpha`$ becomes $`0`$;
   - another outcome of the same reading separates them, so that $`\alpha`$ becomes $`\pi/2`$;
   - the view averaged over the outcomes is unchanged, as item 3 requires.

5. **When nothing changes.** Show that if the companion splits as $`\bar A=\bar A_1\cup\bar A_2`$ with $`\lvert\Psi\rangle=\lvert\Psi_{A\bar A_1}\rangle\otimes\lvert\Omega_{\bar A_2}\rangle`$, then every label-free reading on $`\bar A_2`$ alone leaves $`V_A`$, and hence $`X_V`$, $`\alpha`$ and $`\ell`$, unchanged for every outcome.

## Inputs

The base problem is used throughout: (1.3) reading, (1.5) view, (1.11) families, A4 local readings, A7 parts.

From 02-view-content@v1. Notation fixed there: $`p_h:=\langle h\vert V_A\vert h\rangle`$, $`H_V:=\{h:p_h>0\}`$, $`\lvert\psi_h\rangle:=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle`$, $`W(h,h')=\lvert G_{hh'}\rvert^2`$.

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

Eq. (2.5). This holds for a local reading on $`A`$ with classes $`S^A_r`$ and projectors $`\Pi^A_r`$.

```math
p(r)=\bigl\lVert\Pi_r\lvert\Psi\rangle\bigr\rVert^2=\Bigl\lVert\sum_{h\in S^A_r}\lvert h\rangle\otimes\lvert\psi_h\rangle\Bigr\rVert^2=\sum_{h\in S^A_r}p_h=\mathrm{Tr}\bigl(\Pi^A_rV_A\bigr).
```

Eq. (2.11):

```math
W(h)=1,\qquad W(h,h')=\lvert G_{hh'}\rvert^2=\frac{\lvert(V_A)_{hh'}\rvert^2}{p_hp_{h'}} .
```

From 03-witness-distance@v1. Notation fixed there: $`h\approx h'`$ iff $`W(h,h')=1`$; $`X_V:=H_V/{\approx}`$; $`\alpha(x,x'):=\arccos\sqrt{W(x,x')}\in[0,\pi/2]`$.

Eq. (3.1):

```math
\varrho_h:=\lvert E_h\rangle\langle E_h\rvert=\frac{\lvert\psi_h\rangle\langle\psi_h\rvert}{p_h},
\qquad
h\approx h'\;\Longleftrightarrow\;W(h,h')=1\;\Longleftrightarrow\;\varrho_h=\varrho_{h'} .
```

Eq. (3.5). Here $`\alpha`$ is a metric on $`X_V`$.

```math
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}}
=\frac{\lvert\langle h\vert V_A\vert h'\rangle\rvert}{\sqrt{\langle h\vert V_A\vert h\rangle\langle h'\vert V_A\vert h'\rangle}},\qquad h\in x,\ h'\in x' .
```

From 04-neighbours@v1. Notation fixed there: related points $`x\asymp x'`$ iff $`W(x,x')>0`$; neighbours $`x\sim x'`$ by (4.3), a relation defined from the values of $`\alpha`$ on $`X_V`$ alone.

Eq. (4.2):

```math
x\asymp x'\;\Longleftrightarrow\;(V_A)_{hh'}\neq0\quad\text{for one, equivalently for every, pair } h\in x,\ h'\in x' .
```

Eq. (4.6):

```math
\ell(x,x'):=\min\Bigl\{\sum_{j=0}^{m-1}\alpha(y_j,y_{j+1})\;:\;y_0=x,\ y_m=x',\ y_j\sim y_{j+1}\Bigr\},
\qquad \ell(x,x'):=+\infty\ \text{between components.}
```

## Assumptions

- The setting stated under "Goal", at fixed $`\lambda`$.
- In Ilanguage a reading yields a single value, and the state becomes the post-reading state (1.3) (Law 1). "Averaged over outcomes" in item 3 is a statement about statistics. No mixed state is introduced (A3).

## Scope

- In scope:
  - readings on the companion: state update, the averaged view, and the post-reading witness geometry;
  - the grouping of the companion;
  - the factorized case.
- Out of scope:
  - readings on $`A`$ itself;
  - readings followed by evolution;
  - how fast a distant reading can influence $`A`$ through contracts (a light cone for readings);
  - identical-type issues beyond the label-free condition;
  - any physical meaning beyond the definitions (M1, M4).

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: short argument.
- Item 4: derive, including the example.
- Item 5: short argument.

## Expected result

The main model expects the following. Derive each statement independently, and report any discrepancy.

- Item 2: the closed forms below, and admissibility, because $`\Pi_r`$ commutes with every swap.
  - $`p(r)=\sum_h\langle\psi_h\vert\Pi^{\bar A}_r\vert\psi_h\rangle`$;
  - $`\lvert\Psi_r\rangle=\Pi_r\lvert\Psi\rangle/\sqrt{p(r)}`$;
  - $`\lvert\psi^{(r)}_h\rangle=\Pi^{\bar A}_r\lvert\psi_h\rangle/\sqrt{p(r)}`$;
  - $`\bigl(V_A(\Psi_r)\bigr)_{hh'}=\langle\psi_{h'}\vert\Pi^{\bar A}_r\vert\psi_h\rangle/p(r)`$.
- Item 3: the identity, from $`\sum_r\Pi^{\bar A}_r=\mathbb 1`$.
- Item 4: $`W_r(h,h')=\dfrac{\lvert\langle\psi_{h'}\vert\Pi^{\bar A}_r\vert\psi_h\rangle\rvert^2}{\langle\psi_h\vert\Pi^{\bar A}_r\vert\psi_h\rangle\langle\psi_{h'}\vert\Pi^{\bar A}_r\vert\psi_{h'}\rangle}`$, and an explicit example. One possible example uses a companion with three places $`k_1,k_2,k_3`$ and the branch states $`(\lvert k_1\rangle+\lvert k_2\rangle)/\sqrt2`$ and $`(\lvert k_1\rangle+\lvert k_3\rangle)/\sqrt2`$ of two places of $`A`$. With the reading $`\{k_1\}\,\vert\,\{k_2,k_3\}`$, the outcome $`k_1`$ merges the two points and the other outcome separates them.
- Item 5: $`V_A(\Psi_r)=V_A(\Psi)`$ for every outcome.

Give every main result a tag $`(9.k)`$.

Consistency checks, at most three, chosen from:

- the trivial reading with a single class changes nothing;
- a reading on a companion that perfectly records the place of $`A`$ ($`\langle\psi_{h'}\vert\psi_h\rangle=0`$ for $`h\neq h'`$, and the reading distinguishes the records) leaves a single present place, hence a single point;
- in the example of item 4, the outcome average of the post-reading views equals the original view.

## Code

None.
