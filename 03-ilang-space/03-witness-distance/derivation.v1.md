# Witness distance: points and distances from the witness data of a view

- **Subproject:** 03-ilang-space
- **Package:** 03-witness-distance
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-07

## Setup and assumptions

One description, one part $A$ with nonempty companion $\bar A$, one admissible unit state $\lvert\Psi\rangle\in\mathcal H_{\rm adm}$ at fixed $\lambda$ (A3). No assumption beyond the base problem. "Point" and "distance" are defined notions only (M1, M4); no spatial meaning is attached to them.

**Inputs (02-view-content@v1, as quoted in question.md).** $p_h:=\langle h\vert V_A\vert h\rangle$, $H_V:=\{h:p_h>0\}$ (present places), $\lvert\psi_h\rangle:=(\langle h\rvert\otimes\mathbb 1_{\bar A})\lvert\Psi\rangle$ with $\lvert\Psi\rangle=\sum_h\lvert h\rangle\otimes\lvert\psi_h\rangle$ (2.1); $(V_A)_{hh'}=\langle\psi_{h'}\vert\psi_h\rangle$, $p_h=\lVert\psi_h\rVert^2$ (2.2); for $h\in H_V$, $a_h=\sqrt{p_h}e^{-i\theta_h}$, $\lvert E_h\rangle=e^{i\theta_h}\lvert\psi_h\rangle/\sqrt{p_h}$ with arbitrary real $\theta_h$ (2.7); $G_{hh'}=\langle E_{h'}\vert E_h\rangle$ (2.8); $W(h)=1$, $W(h,h')=\lvert G_{hh'}\rvert^2=\lvert(V_A)_{hh'}\rvert^2/(p_hp_{h'})$ (2.11); for a type-preserving permutation $\pi$ of the objects, $(h^\pi)_{\pi(a)}:=h_a$, $H_V^{\pi(A)}=\{h^\pi:h\in H_V^A\}$ and $W^{\pi(A)}(h_1^\pi,h_2^\pi)=W^A(h_1,h_2)$ (2.16).

The $\theta_h$ in (2.7)–(2.8) are convention phases of the split (1.6), not angles between states; the only angle used below is the witness angle $\alpha$.

**Standard facts used without proof.** Cauchy–Schwarz inequality with its equality case; the Fubini–Study angle $\arccos\lvert\langle u\vert v\rangle\rvert$ between unit vectors is a metric on rays; the spherical law of cosines (in the explicit form of Step 5); Cauchy's functional equation.

## Derivation

### Step 1. The relation $\approx$ (items 1a, 1b)

For $h\in H_V$, $\lvert E_h\rangle$ is a unit vector (2.7), and $W(h,h')=\lvert\langle E_{h'}\vert E_h\rangle\rvert^2$ (2.11).

**(a)** By Cauchy–Schwarz, $W(h,h')\le1$, with equality iff $\lvert E_h\rangle=e^{i\varphi}\lvert E_{h'}\rangle$ for some real $\varphi$, i.e. iff the two branch states differ only by a phase. By (2.7) the phases $\theta_h$ drop out of this statement. With the companion projector of a present place,

$$
\varrho_h:=\lvert E_h\rangle\langle E_h\rvert=\frac{\lvert\psi_h\rangle\langle\psi_h\rvert}{p_h},
\qquad
h\approx h'\;\Longleftrightarrow\;W(h,h')=1\;\Longleftrightarrow\;\varrho_h=\varrho_{h'} .
\tag{3.1}
$$

In terms of the witness rule: $\lvert(V_A)_{hh'}\rvert=\sqrt{p_hp_{h'}}\,\lvert G_{hh'}\rvert\le\sqrt{p_hp_{h'}}$ by (2.8), and the bound is reached iff the companion is in the same state (same ray, (1.2)) in the two branches. Then the cross term between $h$ and $h'$ is fully retained: the companion does not witness the difference between $h$ and $h'$. For $W(h,h')<1$ it witnesses it at least partially.

**(b)** By (3.1), $\approx$ is equality of the projectors $\varrho_h$, hence reflexive, symmetric and transitive. Moreover $W(h,h')=\operatorname{Tr}(\varrho_h\varrho_{h'})$ depends on $h,h'$ only through $\varrho_h,\varrho_{h'}$, i.e. only through the classes $[h],[h']$. Hence

$$
X_V:=H_V/{\approx},\qquad
\varrho_x:=\varrho_h,\qquad
W(x,x'):=W(h,h')=\operatorname{Tr}(\varrho_x\varrho_{x'})\qquad(h\in x,\ h'\in x'),
\tag{3.2}
$$

are well defined, and $x\mapsto\varrho_x$ is injective on $X_V$. The points are in one-to-one correspondence with the distinct companion states (rays) that occur as branch states. $X_V\neq\emptyset$, since $\sum_hp_h=1$.

### Step 2. Independence of conventions (item 1c)

- *Common phase (1.2):* $\lvert\Psi\rangle\to e^{i\varphi}\lvert\Psi\rangle$ leaves $\lvert\Psi\rangle\langle\Psi\rvert$, hence $V_A$ (1.5) and every $\varrho_h$, unchanged.
- *Phase split (1.6):* $H_V$ is fixed by the diagonal of $V_A$, and $W(h,h')$ by $V_A$ alone (2.11). So $\approx$, $X_V$ and $W$ on $X_V$ are functions of $V_A$ and contain no $\theta_h$. The place basis is part of the type (A2), so no basis convention enters either.
- *Labels (Law 5):* relabelling by a type-preserving permutation $\pi$ describes the same system. It turns the part $A$ into $\pi(A)$ and its joint places $h$ into $h^\pi$. By (2.16), $h\mapsto h^\pi$ is a bijection $H_V^A\to H_V^{\pi(A)}$ that preserves $W$ on pairs, hence preserves $\approx$ (defined by $W=1$). It therefore induces the canonical bijection

$$
X_V^A\to X_V^{\pi(A)},\quad [h]\mapsto[h^\pi],\qquad
W^{\pi(A)}\bigl([h_1^\pi],[h_2^\pi]\bigr)=W^A\bigl([h_1],[h_2]\bigr).
\tag{3.3}
$$

The two descriptions thus give the same points with the same $W$. If $\pi$ permutes only companion objects, then $h^\pi=h$. If it permutes only instances inside $A$, then $[h^\pi]=[h]$ by Step 3. In both cases (3.3) is the identity on $X_V$. Hence $X_V$ and $W$ are well defined in the sense of M6.

### Step 3. Permuted instances lie in one point (item 1d)

Let $a\neq b$ be objects of $A$ of the same type $T$, and let $h^{(ab)}$ be $h$ with entries $a,b$ exchanged. Then $P_{ab}=P^A_{ab}\otimes\mathbb 1_{\bar A}$ with $P^A_{ab}\lvert h\rangle=\lvert h^{(ab)}\rangle$. $P^A_{ab}$ permutes the place basis and is self-adjoint, so $\langle h^{(ab)}\rvert P^A_{ab}=\langle h\rvert$. With (1.11) and (2.1):

$$
\lvert\psi_h\rangle=\bigl(\langle h^{(ab)}\rvert\otimes\mathbb 1_{\bar A}\bigr)P_{ab}\lvert\Psi\rangle=c_T\,\lvert\psi_{h^{(ab)}}\rangle .
\tag{3.4}
$$

Hence $p_{h^{(ab)}}=p_h$, so $h^{(ab)}$ is present iff $h$ is, and $\varrho_{h^{(ab)}}=\varrho_h$, i.e. $h^{(ab)}\approx h$ by (3.1). Every permutation of same-type instances inside $A$ is a product of such transpositions. By transitivity, $h^\pi\approx h$ for every present $h$. (For $c_T=-1$ and $h_a=h_b$, (3.4) gives $\psi_h=0$; such places are never present.)

### Step 4. Witness angle (item 2, standard)

$\alpha(x,x')=\arccos\sqrt{W(x,x')}=\arccos\lvert\langle E_{h'}\vert E_h\rangle\rvert\in[0,\pi/2]$ is the Fubini–Study angle between the rays $\varrho_x,\varrho_{x'}$. That angle is a metric on rays, and $x\mapsto\varrho_x$ is injective (3.2). Hence $\alpha$ is a metric on $X_V$. By (2.11),

$$
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}}
=\frac{\lvert\langle h\vert V_A\vert h'\rangle\rvert}{\sqrt{\langle h\vert V_A\vert h\rangle\langle h'\vert V_A\vert h'\rangle}},\qquad h\in x,\ h'\in x' .
\tag{3.5}
$$

### Step 5. Realizability of triangle triples (item 3a)

Let $(\alpha_1,\alpha_2,\alpha_3)\in[0,\pi/2]^3$ satisfy $\alpha_3\le\alpha_1+\alpha_2$, $\alpha_1\le\alpha_2+\alpha_3$, $\alpha_2\le\alpha_1+\alpha_3$. Write $\alpha_{12}=\alpha_1$, $\alpha_{23}=\alpha_2$, $\alpha_{13}=\alpha_3$.

**5.1 Reduction.** By (3.5), it suffices to find an admissible state with three present places $h_1,h_2,h_3$ whose branch states are, up to phases, unit vectors $e_1,e_2,e_3$ with $\lvert\langle e_i\vert e_j\rangle\rvert=\cos\alpha_{ij}$.

**5.2 Vectors.** In $\mathbb R^3\subset\mathbb C^3$ take

$$
e_1=(1,0,0),\qquad e_2=(\cos\alpha_1,\sin\alpha_1,0),\qquad e_3=(\cos\alpha_3,\ \sin\alpha_3\cos\phi,\ \sin\alpha_3\sin\phi).
\tag{3.6}
$$

Then $\langle e_1\vert e_2\rangle=\cos\alpha_1$, $\langle e_1\vert e_3\rangle=\cos\alpha_3$ and $\langle e_2\vert e_3\rangle=\cos\alpha_1\cos\alpha_3+\sin\alpha_1\sin\alpha_3\cos\phi$. If $\sin\alpha_1\sin\alpha_3=0$, the triangle inequalities force $\alpha_2=\alpha_1+\alpha_3$ (one of them is $0$), and any $\phi$ works. Otherwise choose $\phi\in[0,\pi]$ with

$$
\cos\phi=\frac{\cos\alpha_2-\cos\alpha_1\cos\alpha_3}{\sin\alpha_1\sin\alpha_3}.
\tag{3.7}
$$

This lies in $[-1,1]$ iff $\cos(\alpha_1+\alpha_3)\le\cos\alpha_2\le\cos(\alpha_1-\alpha_3)$. Since $\lvert\alpha_1-\alpha_3\rvert,\alpha_2,\alpha_1+\alpha_3\in[0,\pi]$ and $\cos$ decreases strictly there, this is $\lvert\alpha_1-\alpha_3\rvert\le\alpha_2\le\alpha_1+\alpha_3$, i.e. exactly the three triangle inequalities. All three overlaps are cosines of angles in $[0,\pi/2]$, hence $\ge0$, so $\lvert\langle e_i\vert e_j\rangle\rvert=\cos\alpha_{ij}$.

**5.3 Sufficient condition and state.** Condition **(R)**: the description has an admissible state (A3), and $A$ contains an object $a$ and $\bar A$ an object $c$, each the only instance of its type in the description, with $d_{T(a)}\ge3$ and $d_{T(c)}\ge3$.

Let $A'=A\setminus\{a\}$ and $\bar A'=\bar A\setminus\{c\}$ (the "rest"). No swap in (1.11) involves $a$ or $c$, so every swap acts as the identity on their factors, and $\mathcal H_{\rm adm}=\mathcal H_{T(a)}\otimes\mathcal H_{T(c)}\otimes\mathcal H^{\rm rest}_{\rm adm}$, up to the ordering of factors. Here $\mathcal H^{\rm rest}_{\rm adm}\neq\{0\}$, because $\mathcal H_{\rm adm}\neq\{0\}$. Pick a unit $\lvert\Omega\rangle=\sum_u\lvert u\rangle\otimes\lvert\omega_u\rangle\in\mathcal H^{\rm rest}_{\rm adm}$ ($u$ joint places of $A'$, $\lvert\omega_u\rangle\in\mathcal H_{\bar A'}$; the obvious reading applies if $A'$ or $\bar A'$ is empty). Pick distinct places $h_1,h_2,h_3$ of $T(a)$ and $k_1,k_2,k_3$ of $T(c)$, and set $\lvert e_i\rangle:=\sum_j(e_i)_j\lvert k_j\rangle$ with (3.6), (3.7). Define

$$
\lvert\Psi\rangle=\frac{1}{\sqrt3}\sum_{i=1}^{3}\sum_u\lvert h_i\,u\rangle\otimes\bigl(\lvert e_i\rangle\otimes\lvert\omega_u\rangle\bigr).
\tag{3.8}
$$

It lies in $\mathcal H_{\rm adm}$ and has norm $1$ (the $\lvert h_iu\rangle$ are orthonormal). By (2.1), $\lvert\psi_{h_iu}\rangle=\tfrac{1}{\sqrt3}\lvert e_i\rangle\otimes\lvert\omega_u\rangle$ and $p_{h_iu}=\lVert\omega_u\rVert^2/3$. Fix $u_0$ with $\omega_{u_0}\neq0$. The places $h_iu_0$ are then present, and by (2.2), (2.11), $W(h_iu_0,h_ju_0)=\lvert\langle e_j\vert e_i\rangle\rvert^2=\cos^2\alpha_{ij}$. So the points $x_i=[h_iu_0]$ have witness angles $(\alpha_1,\alpha_2,\alpha_3)$.

The minimal description satisfying (R) has two objects, $A=\{a\}$, $\bar A=\{c\}$, $T(a)\neq T(c)$, three places each. There $H_V=\{h_1,h_2,h_3\}$, so these are the only points.

**5.4 Remark on the example condition of the question.** "$\bar A$ contains an object of a type with $\ge3$ places that does not occur in $A$" is not sufficient by itself. (i) $A$ must admit three present places with independent branch states: if $A$ is a single object with two places, three distinct points never occur. (ii) If that type is sign-changing with exactly $d_T$ instances, its admissible subspace is one-dimensional. Its state then factors out of every branch state and witnesses nothing. (R) avoids both cases.

### Step 6. Characterization (item 3b)

$d=g\circ\alpha=f\circ W$ with $f(w)=g(\arccos\sqrt w)$; $w\mapsto\arccos\sqrt w$ is a bijection $[0,1]\to[0,\pi/2]$, so the two forms are equivalent. Claim:

$$
g\circ\alpha\ \text{is a metric on }X_V\text{ for every description}
\iff
\begin{cases}
g(0)=0,\qquad g>0\ \text{on }(0,\pi/2],\\
g(\alpha_3)\le g(\alpha_1)+g(\alpha_2)\ \text{for every triangle triple in }[0,\pi/2]^3 .
\end{cases}
\tag{3.9}
$$

*Only if.* $d(x,x)=g(0)$ must vanish. For $\alpha\in(0,\pi/2]$, the triple $(\alpha,0,\alpha)$ is a triangle triple, so by Step 5 two distinct points at angle $\alpha$ exist, and $g(\alpha)>0$ is needed. For every triangle triple, Step 5 realizes points with these angles, and the triangle inequality $d(x_1,x_3)\le d(x_1,x_2)+d(x_2,x_3)$ is the third condition.

*If.* $d(x,x')=0\iff\alpha(x,x')=0\iff x=x'$; $d$ is symmetric because $\alpha$ is. For any three points of any description, $(\alpha(x_1,x_2),\alpha(x_2,x_3),\alpha(x_1,x_3))$ is a triangle triple in $[0,\pi/2]^3$, since $\alpha$ is a metric (Step 4). The set of triangle triples is invariant under permutations, so all three triangle inequalities of $d$ hold.

**Sufficient condition.** If $g(0)=0$, $g>0$ on $(0,\pi/2]$, $g$ is nondecreasing and $g$ is subadditive ($g(s+t)\le g(s)+g(t)$ for $s,t\ge0$, $s+t\le\pi/2$), then $g\circ\alpha$ is a metric for every description. Indeed, for a triangle triple, with $t:=\min(\alpha_2,\pi/2-\alpha_1)\le\alpha_2$,

$$
g(\alpha_3)\le g\bigl(\min(\alpha_1+\alpha_2,\pi/2)\bigr)=g(\alpha_1+t)\le g(\alpha_1)+g(t)\le g(\alpha_1)+g(\alpha_2).
\tag{3.10}
$$

### Step 7. Candidates (item 3c)

With $\sqrt W=\cos\alpha$:

$$
\sqrt{1-W}=\sin\alpha,\quad
\sqrt{2(1-\sqrt W)}=2\sin\tfrac{\alpha}{2},\quad
1-\sqrt W=2\sin^2\tfrac{\alpha}{2},\quad
1-W=\sin^2\alpha,\quad
\sqrt{-\ln W}=\sqrt{-2\ln\cos\alpha}.
\tag{3.11}
$$

**Qualify** (via (3.10)). $\alpha$, $\sin\alpha$ and $2\sin(\alpha/2)$ vanish at $0$ and increase strictly on $[0,\pi/2]$. They are subadditive: trivially for $\alpha$; $\sin(s+t)=\sin s\cos t+\cos s\sin t\le\sin s+\sin t$ for $s,t\ge0$, $s+t\le\pi/2$; and the same identity with $s/2,t/2$ for $2\sin(\alpha/2)$. Their ranges are $[0,\pi/2]$, $[0,1]$ and $[0,\sqrt2]$. Each full range occurs, since every angle is realized (Step 5). The maximum is reached iff the branch states are orthogonal.

**Fail.** Take the triangle triple $(\pi/6,\pi/6,\pi/3)$, realized by Step 5 ($\phi=0$) in the two-object description, where these are all pairs of points. There $W=\tfrac34,\tfrac34,\tfrac14$, all $>0$ (as required for the last candidate):

| candidate | $d(x_1,x_3)$ | $d(x_1,x_2)+d(x_2,x_3)$ |
|---|---|---|
| $1-\sqrt W$ | $1/2$ | $2-\sqrt3\approx0.268$ |
| $1-W$ | $3/4$ | $1/2$ |
| $\sqrt{-\ln W}$ | $\sqrt{\ln4}\approx1.177$ | $2\sqrt{\ln(4/3)}\approx1.073$ |

For the last line, $\ln4>4\ln\tfrac43\iff4>\tfrac{256}{81}$. All three satisfy $g(0)=0$ and $g>0$; they fail only the triangle inequality.

### Step 8. Additivity (item 4)

For $s,t\ge0$ with $s+t\le\pi/2$, the triple $(s,t,s+t)$ is a triangle triple. By Step 5 it is realized by points with $x_2$ between $x_1$ and $x_3$. Conversely, every aligned triple has angles of this form. Hence additivity of $g\circ\alpha$ on all aligned triples of all descriptions is equivalent to

$$
g(s+t)=g(s)+g(t),\qquad s,t\ge0,\ s+t\le\pi/2 .
\tag{3.12}
$$

*If:* $g=c\alpha$ with $c>0$ satisfies (3.12) and is a metric by Step 7.

*Only if:* $s=t=0$ gives $g(0)=0$. By induction, $g(k\pi/2n)=k\,g(\pi/2n)$ for $k\le n$. With $k=n$, $g(q\pi/2)=q\,g(\pi/2)$ for every rational $q\in[0,1]$, so $g=c\alpha$ with $c:=2g(\pi/2)/\pi$ on a dense set. Continuity, or monotonicity (squeeze $\alpha$ between rational points), extends this to $[0,\pi/2]$. Moreover $c>0$, since $g(\pi/2)>0$ by (3.9). Thus

$$
g\circ\alpha\ \text{additive on every aligned triple}\iff g(\alpha)=c\,\alpha,\quad c>0 .
\tag{3.13}
$$

Among the qualifying candidates of Step 7, only $\alpha$ is additive. $\sin\alpha$ and $2\sin(\alpha/2)$ are strictly subadditive on aligned triples with $s,t>0$.

## Result

- **Points:** $h\approx h'\iff W(h,h')=1\iff\varrho_h=\varrho_{h'}$ (3.1): the companion does not witness the difference. The points are $X_V=H_V/{\approx}$ with $W(x,x')=\operatorname{Tr}\varrho_x\varrho_{x'}$ (3.2). They are independent of the common phase, the phase split and the labels (3.3), and permuted same-type instances in $A$ lie in one point (3.4).
- **Witness angle:** $\alpha$ is a metric on $X_V$ with $\cos\alpha(x,x')=\lvert(V_A)_{hh'}\rvert/\sqrt{p_hp_{h'}}$ (3.5).
- **Realizability:** under condition (R), every triangle triple in $[0,\pi/2]^3$ is realized by (3.6)–(3.8).
- **Characterization:** (3.9), with the sufficient condition "nondecreasing and subadditive" (3.10).
- **Candidates:** $\alpha$, $\sqrt{1-W}$ and $\sqrt{2(1-\sqrt W)}$ are metrics, with ranges $[0,\pi/2]$, $[0,1]$ and $[0,\sqrt2]$. $1-\sqrt W$, $1-W$ and $\sqrt{-\ln W}$ fail on the triple $(\pi/6,\pi/6,\pi/3)$ (3.11).
- **Additivity:** additivity on aligned triples holds iff $g=c\,\alpha$, $c>0$ (3.12)–(3.13).

## Consistency checks

1. **Product state** $\lvert\Psi\rangle=\lvert\phi\rangle\otimes\lvert\chi\rangle$. Then $\lvert\psi_h\rangle=\phi_h\lvert\chi\rangle$ and $\varrho_h=\lvert\chi\rangle\langle\chi\rvert$ for all present $h$. So $X_V$ is a single point, as (3.5) also gives: $\lvert(V_A)_{hh'}\rvert=\lvert\phi_h\phi_{h'}\rvert=\sqrt{p_hp_{h'}}$.
2. **Orthogonal branch states.** $\langle E_{h'}\vert E_h\rangle=0$ for $h\neq h'$ makes every class a singleton, and $\alpha=\arccos0=\pi/2$ for any two distinct points ($V_A$ diagonal in (3.5)).
3. **Two-branch witness rule** $a\lvert0\rangle\lvert E_0\rangle+b\lvert1\rangle\lvert E_1\rangle$, $ab\neq0$. Here $(V_A)_{01}=ab^*\langle E_1\vert E_0\rangle$, $p_0=\lvert a\rvert^2$, $p_1=\lvert b\rvert^2$, so (3.5) gives $\cos\alpha=\lvert\langle E_1\vert E_0\rangle\rvert$.

## Open issues

- (R) is sufficient, not necessary. A necessary and sufficient condition on the description (types, families, numbers of instances, the split $A|\bar A$) for realizing all triangle triples is not derived. The example condition of the question needs the supplements of Step 5.4.
- The metric requirement alone leaves a large class of $g$, e.g. $\sin\alpha$ and $2\sin(\alpha/2)$. Only additivity on aligned triples fixes $g$ up to scale.
- $X_V$ and $W$ depend on the state and on $\lambda$. Comparing points across $\lambda$ or across parts, and the phases of $W(h_1,\dots,h_k)$ for $k\ge3$, are out of scope.

## Methods used

- Partial trace and view matrix elements
- Cauchy–Schwarz inequality (equality case)
- Quotient by an equivalence relation; rays and projectors
- Permutation (swap) symmetry of identical instances
- Fubini–Study angle on rays
- Gram vectors, spherical law of cosines
- Subadditivity; Cauchy's functional equation on an interval
