# Common space of two types recorded by one medium

- **Subproject:** 03-ilang-space
- **Package:** 03-ilang-space/16-common-space
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-08

## Setup and assumptions

**Setting (question.md).** Objects $`a`$ (type $`A`$, places $`h\in H_A`$, $`d_A\ge2`$), $`b`$ (type $`B`$, places $`k\in H_B`$, $`d_B\ge2`$) and the medium $`c`$ have pairwise different types, and each is the only instance of its type. So (1.11) imposes no constraint and no description label enters (Law 5, M6). The contracts and the start are

```math
C=\sum_h\lvert h\rangle\langle h\rvert_a\otimes\mathbb 1_b\otimes K^A_h+\sum_k\mathbb 1_a\otimes\lvert k\rangle\langle k\rvert_b\otimes K^B_k,
\qquad
\lvert\Psi(0)\rangle=\lvert\phi\rangle_a\otimes\lvert\vartheta\rangle_b\otimes\lvert\chi\rangle_c ,
\qquad\text{(16.1)}
```

with $`K^A_h,K^B_k`$ self-adjoint on $`\mathcal H_c`$ and $`\lambda`$-independent (A5), and $`\phi_h\neq0`$, $`\vartheta_k\neq0`$ for all $`h,k`$. The notation $`\langle X\rangle`$, $`u^A_h`$, $`u^B_k`$, $`g`$ is that of question.md. In addition:

```math
\mathcal N:=\{v\in\mathcal H_c:\langle\chi\vert v\rangle=0\},\quad
M_{hk}:=K^A_h+K^B_k,\quad
w_{hk}:=u^A_h+u^B_k,\quad
\Delta^A_{hh'}:=u^A_h-u^A_{h'},\quad
\Delta^B_{kk'}:=u^B_k-u^B_{k'} .
```

Every record vector lies in $`\mathcal N`$, since $`\langle\chi\vert u^A_h\rangle=\langle K^A_h\rangle-\langle K^A_h\rangle=0`$. With $`g`$, $`\mathcal N`$ is a real Euclidean space of dimension $`2(\dim\mathcal H_c-1)`$, and $`g(v,v)=\lVert v\rVert^2`$.

**Leading order.** This means $`\lambda\to0^+`$. The leading-order geometry of a view is its $`d_0=\lim_{\lambda\to0^+}\alpha/\lambda`$. "The view fixes $`Q`$ at leading order" means that $`Q`$ is determined by the values of $`d_0`$ on all pairs of joint places of the part. Item 1(a) is exact.

**Split convention.** The evolution (1.9), the total cost (1.8), and hence every view and every reading statistic, depend on the $`K`$'s only through $`C`$. A quantity that changes under a replacement leaving $`C`$ fixed is therefore a convention of the description, and M6 excludes it. (Only the bookkeeping of the single contract costs $`\langle C_\gamma\rangle`$ changes.)

**Inputs (quoted in question.md).**
- (2.2): $`(V_A)_{hh'}=\langle\psi_{h'}\vert\psi_h\rangle`$ and $`p_h=\lVert\psi_h\rVert^2`$.
- (3.5): $`\cos\alpha=\lvert(V_A)_{hh'}\rvert/\sqrt{p_hp_{h'}}`$, and $`\alpha`$ is a metric on $`X_V`$.
- Setting of 11: A1–A7 hold; $`\bar A\neq\emptyset`$; no type has objects on both sides of the cut; $`C=C_A+C_{\bar A}+C_\partial`$ with $`C_\partial=\sum_nA_n\otimes B_n`$ and $`A_n,B_n`$ self-adjoint; the start is a product $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with every joint weight $`\phi_h\neq0`$.
- (11.8): $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$.
- (11.10): if every $`A_n`$ is diagonal, then $`u_h=\sum_n\langle h\vert A_n\vert h\rangle(B_n-\langle B_n\rangle)\lvert\chi\rangle`$. In (11.10), $`\lvert\chi\rangle`$ is the companion factor of the start state and $`\langle B_n\rangle`$ is its expectation value.

## Derivation

### Step 1. Split freedom (item 1a)

1. Insert $`\mathbb 1_b=\sum_k\lvert k\rangle\langle k\rvert`$ and $`\mathbb 1_a=\sum_h\lvert h\rangle\langle h\rvert`$ into (16.1):
```math
C=\sum_{h,k}\lvert h\rangle\langle h\rvert_a\otimes\lvert k\rangle\langle k\rvert_b\otimes M_{hk} .
\qquad\text{(16.2)}
```
2. The projectors $`\lvert h\rangle\langle h\rvert\otimes\lvert k\rangle\langle k\rvert`$ are mutually orthogonal and sum to $`\mathbb 1`$. Hence $`C`$ fixes every block: $`M_{hk}=(\langle h\rvert_a\langle k\rvert_b\otimes\mathbb 1_c)\,C\,(\lvert h\rangle_a\lvert k\rangle_b\otimes\mathbb 1_c)`$. A family $`(K'^A_h,K'^B_k)`$ therefore gives the same $`C`$ iff $`D^A_h=-D^B_k`$ for all $`h,k`$, where $`D^A_h:=K'^A_h-K^A_h`$ and $`D^B_k:=K'^B_k-K^B_k`$.
3. The left side does not depend on $`k`$ and the right side does not depend on $`h`$, so both equal one operator $`Z`$. $`Z`$ is self-adjoint because it is a difference of self-adjoint operators. Conversely, every such $`Z`$ leaves all $`M_{hk}`$ unchanged. Hence the replacements are exactly
```math
K'^A_h=K^A_h+Z,\qquad K'^B_k=K^B_k-Z,\qquad Z=Z^\dagger\ \text{on }\mathcal H_c\ \text{arbitrary.}
\qquad\text{(16.3)}
```
In words: the medium-only term $`\mathbb 1_a\otimes\mathbb 1_b\otimes Z`$ can be booked in the contract $`(a,c)`$ or in the contract $`(b,c)`$ (A5).

### Step 2. Record vectors under the split (item 1b)

1. From (16.3), $`u'^A_h=(K^A_h+Z-\langle K^A_h\rangle-\langle Z\rangle)\lvert\chi\rangle`$, and similarly for $`B`$:
```math
u^A_h\mapsto u^A_h+z,\qquad u^B_k\mapsto u^B_k-z,\qquad \lvert z\rangle=(Z-\langle Z\rangle)\lvert\chi\rangle .
\qquad\text{(16.4)}
```
2. *Range of $`z`$.* Always $`\langle\chi\vert z\rangle=0`$. Conversely, take $`v\in\mathcal N`$ and set $`Z_v:=\lvert v\rangle\langle\chi\rvert+\lvert\chi\rangle\langle v\rvert`$. This operator is self-adjoint, $`Z_v\lvert\chi\rangle=\lvert v\rangle`$ and $`\langle Z_v\rangle=2\mathrm{Re}\langle\chi\vert v\rangle=0`$, so $`z=v`$. The possible shifts are therefore exactly the vectors $`z\in\mathcal N`$.
3. *Phase.* The phase split in the product start, and the common phase (1.2), allow $`\lvert\chi\rangle\to e^{i\varphi}\lvert\chi\rangle`$. Since $`u`$ is linear in $`\chi`$ and $`\langle K\rangle`$ does not depend on the phase, every record vector is multiplied by the same factor $`e^{i\varphi}`$.
4. *Orbits.* Two record families are related by a shift (16.4) iff they have the same $`w_{hk}`$ for all $`h,k`$. The direction "only if" is immediate. For "if", $`u'^A_h-u^A_h=-(u'^B_k-u^B_k)`$ for all $`h,k`$, and the argument of Step 1.3 gives a common $`z`$, which lies in $`\mathcal N`$. Moreover $`w_{hk}=(M_{hk}-\langle M_{hk}\rangle)\lvert\chi\rangle`$ is fixed by $`C`$. Hence
```math
F\ \text{is well defined (M6)}\iff F\ \text{is a function of the family }\{w_{hk}\}=\{u^A_h+u^B_k\}\ \text{invariant under}\ w_{hk}\mapsto e^{i\varphi}w_{hk}.
\qquad\text{(16.5)}
```
5. *Examples.* The following are well defined: $`\lVert\Delta^A_{hh'}\rVert`$ and $`\lVert\Delta^B_{kk'}\rVert`$ (because $`\Delta^A_{hh'}=w_{hk}-w_{h'k}`$ and $`\Delta^B_{kk'}=w_{hk}-w_{hk'}`$), the mixed products $`g(\Delta^A_{hh'},\Delta^B_{kk'})`$, the distances $`\lVert w_{hk}-w_{h'k'}\rVert`$, and $`\lVert u^A_h+u^B_k\rVert`$. The following are not well defined: $`u^A_h`$, $`\lVert u^A_h\rVert`$, $`g(u^A_h,u^B_k)`$ and $`\lVert u^A_h-u^B_k\rVert`$.

   For the last one, (16.4) maps $`v:=u^A_h-u^B_k\in\mathcal N`$ to $`v+2z`$. Let $`\dim\mathcal H_c\ge2`$, take a unit vector $`e\in\mathcal N`$ and set $`z=-v/2+se/2`$ with $`s\ge0`$. Then $`\lVert v+2z\rVert=s`$, so
```math
\bigl\{\lVert u'^A_h-u'^B_k\rVert:\ \text{all splits}\bigr\}=[0,\infty)\qquad(\dim\mathcal H_c\ge2).
\qquad\text{(16.6)}
```
   If $`\dim\mathcal H_c=1`$, then $`\mathcal N=\{0\}`$ and every record vector vanishes.

### Step 3. The three views (item 2a)

1. By (16.2), $`e^{-iC\lambda}=\sum_{h,k}\lvert h\rangle\langle h\rvert\otimes\lvert k\rangle\langle k\rvert\otimes e^{-iM_{hk}\lambda}`$, so
```math
\lvert\Psi(\lambda)\rangle=\sum_{h,k}\phi_h\vartheta_k\,\lvert h\rangle_a\lvert k\rangle_b\otimes e^{-iM_{hk}\lambda}\lvert\chi\rangle .
\qquad\text{(16.7)}
```
   The place weights are $`\lvert\phi_h\rvert^2`$, $`\lvert\vartheta_k\rvert^2`$ and $`\lvert\phi_h\vartheta_k\rvert^2`$, all positive for every $`\lambda`$. So in each view $`H_V`$ is the full set of places.
2. *Setting of 11.* A1–A7 hold in every cut, the companion is nonempty, and since the three types are different no type has objects on both sides of a cut.
   - Cut $`\{a\}\vert\{b,c\}`$: $`C_A=0`$, $`C_{\bar A}=\sum_k\lvert k\rangle\langle k\rvert_b\otimes K^B_k`$, $`C_\partial=\sum_h\lvert h\rangle\langle h\rvert_a\otimes(\mathbb 1_b\otimes K^A_h)`$. The start is $`\phi\otimes(\vartheta\otimes\chi)`$ with $`\phi_h\neq0`$.
   - Cut $`\{b\}\vert\{a,c\}`$: the same with $`a\leftrightarrow b`$.
   - Cut $`\{a,b\}\vert\{c\}`$: $`C_A=C_{\bar A}=0`$, and $`C_\partial`$ is all of (16.1), with $`A_n\in\{\lvert h\rangle\langle h\rvert_a\otimes\mathbb 1_b,\ \mathbb 1_a\otimes\lvert k\rangle\langle k\rvert_b\}`$ and $`B_n\in\{K^A_h,K^B_k\}`$. The start is $`(\phi\otimes\vartheta)\otimes\chi`$ with joint weights $`\phi_h\vartheta_k\neq0`$.

   The setting of 11 therefore applies to all three cuts. In each cut every $`A_n`$ is diagonal in the place basis, so (11.10) applies as well.
3. *Cut $`\{a\}`$.* The companion factor is $`\vartheta\otimes\chi`$, $`B_h=\mathbb 1_b\otimes K^A_h`$ and $`\langle h\vert A_{h''}\vert h\rangle=\delta_{hh''}`$. Then (11.10) gives $`u_h=(\mathbb 1_b\otimes K^A_h-\langle K^A_h\rangle)(\vartheta\otimes\chi)=\vartheta\otimes u^A_h`$, and $`\lVert\vartheta\otimes\Delta^A_{hh'}\rVert=\lVert\Delta^A_{hh'}\rVert`$.
   *Cut $`\{a,b\}`$.* Here (11.10) gives $`u_{hk}=\sum_{h''}\delta_{hh''}u^A_{h''}+\sum_{k''}\delta_{kk''}u^B_{k''}=w_{hk}`$. With (11.8):
```math
d_0^{a}(h,h')=\lVert u^A_h-u^A_{h'}\rVert,\qquad d_0^{b}(k,k')=\lVert u^B_k-u^B_{k'}\rVert,
\qquad\text{(16.8)}
```
```math
d_0^{ab}\bigl((h,k),(h',k')\bigr)=\lVert w_{hk}-w_{h'k'}\rVert=\lVert\Delta^A_{hh'}+\Delta^B_{kk'}\rVert .
\qquad\text{(16.9)}
```
4. *Points.* By (16.5), all three distances are well defined. Places at $`d_0^a=0`$ have equal $`u^A_h`$. So $`X_A`$ is mapped isometrically onto $`U_A:=\{u^A_h\}\subset(\mathcal N,\lVert\cdot\rVert)`$ by $`x\mapsto u^A_x`$, the common record vector of the places in $`x`$. Likewise $`X_B\cong U_B:=\{u^B_k\}`$. The view of $`\{a,b\}`$ has points $`X_{ab}\cong\{w_{hk}\}=U_A+U_B`$, the Minkowski sum, which is invariant under (16.4). For fixed $`k`$, $`x\mapsto[(h,k)]`$ with $`h\in x`$ embeds $`X_A`$ isometrically into $`X_{ab}`$, because $`d_0^{ab}((h,k),(h',k))=d_0^a(h,h')`$. The same holds with $`A`$ and $`B`$ exchanged.

### Step 4. Independence and joint content (items 2b, 2c)

1. *(2b)* By (16.8), $`d_0^a`$ involves neither the $`K^B_k`$ nor $`\vartheta`$: **no** dependence. In the cut $`\{a\}`$ the $`B`$-contract is $`C_{\bar A}`$, which enters (11.6) only through the $`h`$-independent term $`Q_\chi C_{\bar A}\chi`$. That term cancels in $`u_h-u_{h'}`$.
2. *(2c)* Expand (16.9) and use $`d_0^{ab}((h,k),(h',k))=d_0^a(h,h')`$ and $`d_0^{ab}((h,k),(h,k'))=d_0^b(k,k')`$:
```math
d_0^{ab}\bigl((h,k),(h',k')\bigr)^2=d_0^a(h,h')^2+d_0^b(k,k')^2+2\,g\bigl(\Delta^A_{hh'},\Delta^B_{kk'}\bigr).
\qquad\text{(16.10)}
```
   At leading order the view of $`\{a,b\}`$ therefore fixes:
   - (i) both separate geometries, $`d_0^a`$ and $`d_0^b`$;
   - (ii) the mixed products $`g(\Delta^A_{hh'},\Delta^B_{kk'})`$ for all $`h,h',k,k'`$. Equivalently it fixes $`\lVert\Delta^A_{hh'}-\Delta^B_{kk'}\rVert=d_0^{ab}((h,k'),(h',k))`$, because $`w_{hk'}-w_{h'k}=\Delta^A_{hh'}-\Delta^B_{kk'}`$. This quantity compares an $`A`$-displacement with a $`B`$-displacement.

   Conversely, (16.10) expresses every $`d_0^{ab}`$ through (i) and (ii), so this is the complete content. Equivalently, polarization gives the real Gram matrix of $`\{\Delta^A_{hh_0}\}_h\cup\{\Delta^B_{kk_0}\}_k`$. This fixes the pair $`(U_A,U_B)`$ up to a separate translation of each and a common orthogonal map of $`(\mathcal N,g)`$.

   The view does not fix any split-dependent quantity, for example (16.6). It does not fix the well-defined $`\lVert w_{hk}\rVert`$ either: adding a medium term $`\mathbb 1\otimes Y'`$ to $`C`$ shifts all $`w_{hk}`$ by the same vector and leaves (16.9) unchanged.

### Step 5. Correspondences (item 3)

1. For $`x\in X_A`$ write $`u^A_x`$, and for $`y\in X_B`$ write $`u^B_y`$. Take $`h\in x`$, $`h'\in x'`$, $`k\in\pi(x)`$, $`k'\in\pi(x')`$. Then (16.9) gives $`d_0^{ab}((h,k'),(h',k))=\lVert(u^A_x-u^A_{x'})-(u^B_{\pi(x)}-u^B_{\pi(x')})\rVert`$, which does not depend on the representatives.
2. *(3a)* Hence $`\pi`$ is a correspondence iff
```math
u^A_x-u^A_{x'}=u^B_{\pi(x)}-u^B_{\pi(x')}\ \ \forall x,x'\in D_A
\iff
\exists\,t_\pi\in\mathcal N:\ u^B_{\pi(x)}=u^A_x+t_\pi\ \ \forall x\in D_A .
\qquad\text{(16.11)}
```
   For "$`\Rightarrow`$", fix $`x'=x_0`$ and set $`t_\pi:=u^B_{\pi(x_0)}-u^A_{x_0}`$. For "$`\Leftarrow`$", subtract the relations for $`x`$ and $`x'`$. Under (16.4), $`t_\pi\mapsto t_\pi-2z`$, and under the phase both sides of (16.11) get the same factor, so (16.11) is well defined. The split $`z=t_\pi/2\in\mathcal N`$ gives $`u'^B_{\pi(x)}=u'^A_x`$. So $`\pi`$ is a correspondence iff, in some split, matched points carry equal record vectors.
3. *(3b)* **Yes.** By (16.8) and (16.11):
```math
d_0^b\bigl(\pi(x),\pi(x')\bigr)=\lVert u^B_{\pi(x)}-u^B_{\pi(x')}\rVert=\lVert u^A_x-u^A_{x'}\rVert=d_0^a(x,x') .
\qquad\text{(16.12)}
```
   The converse fails (Steps 6 and 7).
4. *(3c)* Let $`\bar u^A:=\lvert X_A\rvert^{-1}\sum_{x}u^A_x`$ and define $`\bar u^B`$ likewise. A correspondence with $`D_A=X_A`$ and $`D_B=X_B`$ exists iff
```math
\lvert X_A\rvert\ge2\ \text{ and }\ U_B=U_A+t\ \text{for some }t\in\mathcal N
\iff
\lvert X_A\rvert=\lvert X_B\rvert\ge2\ \text{ and }\ U_A-\bar u^A=U_B-\bar u^B ,
\qquad\text{(16.13)}
```
   and it is then **unique**.

   *Proof.* "$`\Rightarrow`$": (16.11) together with surjectivity of $`\pi`$ gives $`U_B=U_A+t_\pi`$, and $`\lvert D_A\rvert\ge2`$ gives $`\lvert X_A\rvert\ge2`$. "$`\Leftarrow`$": define $`\pi(x)`$ as the unique $`y`$ with $`u^B_y=u^A_x+t`$. This is a bijection, because $`x\mapsto u^A_x`$, $`y\mapsto u^B_y`$ and the translation are bijections onto $`U_A`$, $`U_B`$ and $`U_B`$; then (16.11) holds.

   *Uniqueness.* If full correspondences exist with translations $`t`$ and $`t'`$, then $`U_A+t=U_A+t'`$. Comparing centroids gives $`t=t'`$, and $`\pi(x)`$ is fixed by $`u^A_x+t`$.

   *Second form.* $`U_B=U_A+t`$ implies equal cardinalities and $`t=\bar u^B-\bar u^A`$; the reverse direction is immediate. The centred sets are split invariant.

### Step 6. Example (a): one line

In Steps 6–7, $`i,j`$ are indices and $`\mathrm i`$ is the imaginary unit. Let $`\xi:=(X-\langle X\rangle)\chi`$ and $`\eta:=(Y-\langle Y\rangle)\chi`$. Then $`\lVert\xi\rVert^2=\langle\chi\vert(X-\langle X\rangle)^2\vert\chi\rangle=\sigma_X^2>0`$, and
$`u^A_{h_i}=i\,\xi`$, $`u^B_{k_j}=j\,\xi+\eta`$, $`w_{h_ik_j}=(i+j)\xi+\eta`$. By (16.8)–(16.10):
```math
d_0^a(h_i,h_{i'})=\lvert i-i'\rvert\sigma_X,\quad
d_0^b(k_j,k_{j'})=\lvert j-j'\rvert\sigma_X,\quad
d_0^{ab}=\lvert i+j-i'-j'\rvert\sigma_X,\quad
g(\Delta^A_{h_ih_{i'}},\Delta^B_{k_jk_{j'}})=(i-i')(j-j')\,\sigma_X^2 .
\qquad\text{(16.14)}
```
- $`X_A`$ and $`X_B`$ each consist of $`n`$ equally spaced points on a line. $`X_{ab}`$ consists of $`2n-1`$ equally spaced points, labelled by $`i+j\in\{2,\dots,2n\}`$.
- $`Y`$ drops out of every view. The $`A`$- and $`B`$-displacements are parallel.
- *Correspondences.* Write $`\pi(h_i)=k_{\sigma(i)}`$. Since $`\xi\neq0`$, (16.11) reads $`\sigma(i)-\sigma(i')=i-i'`$, so $`\sigma(i)=i+s`$. All correspondences are therefore
```math
\pi_{s,D}:\ h_i\mapsto k_{i+s}\ \ (h_i\in D),\qquad s\in\mathbb Z,\ \lvert s\rvert\le n-2,\qquad D\subseteq\{h_i:\max(1,1-s)\le i\le\min(n,n-s)\},\ \lvert D\rvert\ge2,
\qquad\text{(16.15)}
```
  with $`t_\pi=s\xi+\eta`$. The unique full correspondence is $`h_i\mapsto k_i`$ ($`s=0`$). This agrees with (16.13), since $`U_B=U_A+\eta`$. The reversal $`h_i\mapsto k_{n+1-i}`$ is an isometry but not a correspondence.

### Step 7. Example (b): two directions

From $`\sigma_y=\mathrm i\sigma_x\sigma_z`$ we get $`\sigma_y\lvert0\rangle=\mathrm i\,\sigma_x\lvert0\rangle=:\mathrm i\lvert e\rangle`$, where $`\lvert e\rangle`$ is a unit vector and $`\langle0\vert e\rangle=\langle\sigma_x\rangle=0`$. Hence $`\langle\sigma_y\rangle=0`$ and $`\mathcal N=\{\beta\lvert e\rangle:\beta\in\mathbb C\}`$. Since $`g(\beta e,\beta'e)=\mathrm{Re}(\beta^*\beta')`$, the map $`\beta e\mapsto(\mathrm{Re}\beta,\mathrm{Im}\beta)`$ is an isometry of $`(\mathcal N,g)`$ onto $`\mathbb R^2`$. Under it, $`u^A_{h_i}=i\,e\mapsto(i,0)`$, $`u^B_{k_j}=\mathrm i\,j\,e\mapsto(0,j)`$ and $`w_{h_ik_j}\mapsto(i,j)`$:
```math
d_0^a=\lvert i-i'\rvert,\quad d_0^b=\lvert j-j'\rvert,\quad
d_0^{ab}=\sqrt{(i-i')^2+(j-j')^2},\quad
g(\Delta^A_{h_ih_{i'}},\Delta^B_{k_jk_{j'}})=\mathrm{Re}\bigl(\mathrm i\,(i-i')(j-j')\bigr)=0 .
\qquad\text{(16.16)}
```
- $`X_A`$ and $`X_B`$ each consist of $`n`$ points on a line. $`X_{ab}`$ is the $`n\times n`$ unit square grid in $`\mathbb R^2`$. The $`A`$- and $`B`$-displacements are orthogonal.
- *Correspondences.* (16.11) requires $`(i-i')\,e=\mathrm i\,(\sigma(i)-\sigma(i'))\,e`$. The left side is real and the right side imaginary, so both vanish and $`i=i'`$. Since $`\lvert D_A\rvert\ge2`$, **no correspondence exists**. In particular $`h_i\mapsto k_i`$ is an isometry (16.8) but not a correspondence. This agrees with (16.13): the centred sets lie on orthogonal lines.

## Result

- **Split (1a, 1b).** The replacements are $`K^A_h\to K^A_h+Z`$ and $`K^B_k\to K^B_k-Z`$ with arbitrary $`Z=Z^\dagger`$ (16.3). They shift $`u^A_h\to u^A_h+z`$ and $`u^B_k\to u^B_k-z`$ for an arbitrary $`z\in\mathcal N`$ (16.4). The well-defined functions are exactly the phase-invariant functions of $`w_{hk}=u^A_h+u^B_k`$ (16.5). $`\lVert u^A_h-u^B_k\rVert`$ is **not** well defined: across splits it takes every value in $`[0,\infty)`$ (16.6).
- **Views (2a).** The setting of 11 applies to all three cuts. The distances are $`d_0^a=\lVert\Delta^A\rVert`$, $`d_0^b=\lVert\Delta^B\rVert`$ (16.8) and $`d_0^{ab}=\lVert\Delta^A+\Delta^B\rVert`$ (16.9). Hence $`X_{ab}\cong U_A+U_B`$, which contains isometric copies of $`X_A`$ and of $`X_B`$.
- **2b.** $`d_0^a`$ depends neither on the $`K^B_k`$ nor on $`\vartheta`$.
- **2c.** The view of $`\{a,b\}`$ fixes $`d_0^a`$, $`d_0^b`$ and the mixed products $`g(\Delta^A_{hh'},\Delta^B_{kk'})`$ (16.10), and nothing else at leading order. In particular it does not fix any distance between a point of $`A`$ and a point of $`B`$.
- **Correspondences (3).** (a) $`\pi`$ is a correspondence iff $`u^B_{\pi(x)}-u^A_x`$ is the same vector for all $`x\in D_A`$ (16.11). (b) Every correspondence is an isometry (16.12); the converse fails. (c) A full correspondence exists iff $`U_B`$ is a translate of $`U_A`$ and $`\lvert X_A\rvert\ge2`$ (16.13), and it is then unique.
- **Examples (4).** (a) The geometry is one line, $`Y`$ drops out, the correspondences are the shifts (16.15), and the unique full correspondence is $`h_i\mapsto k_i`$ (16.14). (b) The joint view is a square grid with orthogonal displacement directions, and there is no correspondence (16.16).

## Consistency checks

1. **Dimensions and rescaling.** $`C`$ has dimension $`1/\lambda`$, and so do $`u`$ and $`d_0`$; $`\alpha\approx\lambda d_0`$ is dimensionless. Under $`C\to\mu C`$ with $`\mu>0`$, $`\alpha(\lambda;\mu C)=\alpha(\mu\lambda;C)`$, so $`d_0\to\mu d_0`$. This matches $`u\to\mu u`$ in (16.8)–(16.10). (16.11) is homogeneous, so the correspondences are unchanged, and $`Z\to\mu Z`$.
2. **$`k`$-independent $`K^B_k=K`$.** The split $`Z=K`$ makes $`K'^B=0`$, so $`b`$ decouples, its view stays pure and $`d_0^b\equiv0`$. (16.8) agrees, since all $`u^B_k`$ are equal. The state is $`\vartheta\otimes(\cdots)`$, so the view of $`\{a,b\}`$ is $`V_a\otimes\lvert\vartheta\rangle\langle\vartheta\rvert`$ and $`d_0^{ab}=d_0^a`$, as (16.9) gives. $`\lvert X_B\rvert=1`$, so there is no correspondence, and the mixed products vanish.
3. **Exchange $`a\leftrightarrow b`$.** (16.3) maps to itself with $`Z\to-Z`$, (16.8) exchanges its two parts and (16.9) is symmetric. (16.11) becomes the same condition for $`\pi^{-1}`$ with $`t\to-t`$, which matches the symmetric definition of a correspondence.

## Open issues

- Points with $`d_0=0`$ may be separated at higher orders. There the $`K^B_k`$, and commutators $`[K^A_h,K^B_k]`$, can enter the view of $`\{a\}`$. This is out of scope.
- Correspondences are defined at leading order only. Whether they persist at higher $`\lambda`$, and any rule that selects among the partial correspondences (16.15), are open and out of scope.
- $`d_0`$ sees only the real Euclidean structure $`g`$ of $`\mathcal N`$. For example, the relative factor $`\mathrm i`$ in Step 7 enters only through orthogonality.

## Methods used

- Block decomposition of an operator by orthogonal projectors
- Gauge (split) freedom and invariants of the shift group
- Partial trace; leading-order witness distance (inputs (11.8), (11.10))
- Polarization identity; real Gram matrix; Minkowski sum
- Translation and centroid argument for finite point sets
- Pauli-matrix algebra
