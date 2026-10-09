# The content of the view: Gram form, invisible data and well-defined companion invariants

- **Subproject:** 03-ilang-space
- **Package:** 03-ilang-space/02-view-content
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-07

## Setup and assumptions

- Only the base problem is used (question.md quotes no inputs). The system has objects $1,\dots,N$ and an admissible joint state $\lvert\Psi\rangle\in\mathcal H_{\rm adm}$, a unit vector (A3), at fixed $\lambda$. The part $A$ and its companion $\bar A$ are nonempty, disjoint, and together contain all objects.
- A joint place of $A$ is an assignment $h=(h_a)_{a\in A}$ with $h_a\in H_{T(a)}$; a joint place of $\bar A$ is $r=(r_b)_{b\in\bar A}$. $\mathcal H_A=\bigotimes_{a\in A}\mathcal H_{T(a)}$ has the orthonormal place basis $\lvert h\rangle$; the factors are taken in a fixed order, and since basis vectors are labelled by assignments this order plays no role. The same holds for $\mathcal H_{\bar A}$.
- The identification $\mathcal H=\mathcal H_A\otimes\mathcal H_{\bar A}$ used in (1.5) is $\lvert K\rangle\mapsto\lvert K|_A\rangle\otimes\lvert K|_{\bar A}\rangle$ ($K|_A$ is the restriction of the joint place $K$ to $A$). It maps an orthonormal basis bijectively onto an orthonormal basis, so it is unitary. We write $\Psi_{hr}:=\Psi_K$ for the $K$ with $K|_A=h$, $K|_{\bar A}=r$.
- The partial trace is the linear map with $\operatorname{Tr}_{\bar A}(X\otimes Y)=X\operatorname{Tr}Y$ (standard).
- Notation fixed by question.md: $p_h$, $H_V$, $\lvert\psi_h\rangle$, $G$, $W$. Shorthand: $(V_A)_{hh'}:=\langle h\vert V_A\vert h'\rangle$.
- There are no approximations. Finite dimension (A1) is used in Step 4. No quantity below is given a distance, geometric or spatial reading (M1, M4).

## Derivation

### Step 1. Branch decomposition

Insert $\mathbb 1_A=\sum_h\lvert h\rangle\langle h\rvert$ and use $\lvert h\rangle\langle h\rvert\otimes\mathbb 1_{\bar A}=(\lvert h\rangle\otimes\mathbb 1_{\bar A})(\langle h\rvert\otimes\mathbb 1_{\bar A})$, where $\lvert h\rangle\otimes\mathbb 1_{\bar A}$ maps $\chi\mapsto\lvert h\rangle\otimes\chi$:

$$
\lvert\Psi\rangle=\sum_h\lvert h\rangle\otimes\lvert\psi_h\rangle,
\qquad
\lvert\psi_h\rangle=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle=\sum_r\Psi_{hr}\lvert r\rangle,
\qquad
\sum_h\lVert\psi_h\rVert^2=\lVert\Psi\rVert^2=1 .
\tag{2.1}
$$

The second form follows from $\langle r\vert\psi_h\rangle=(\langle h\rvert\otimes\langle r\rvert)\lvert\Psi\rangle=\Psi_{hr}$. The last identity holds because the terms of the sum are mutually orthogonal: $\bigl(\langle h\rvert\otimes\langle\psi_h\rvert\bigr)\bigl(\lvert h'\rangle\otimes\lvert\psi_{h'}\rangle\bigr)=\delta_{hh'}\lVert\psi_h\rVert^2$.

### Step 2. The view as a Gram matrix (item 2)

By (2.1), $\lvert\Psi\rangle\langle\Psi\rvert=\sum_{h,h'}\lvert h\rangle\langle h'\rvert\otimes\lvert\psi_h\rangle\langle\psi_{h'}\rvert$. Apply $\operatorname{Tr}_{\bar A}$ with $\operatorname{Tr}\lvert\psi_h\rangle\langle\psi_{h'}\rvert=\langle\psi_{h'}\vert\psi_h\rangle$:

$$
V_A=\sum_{h,h'}\langle\psi_{h'}\vert\psi_h\rangle\,\lvert h\rangle\langle h'\rvert,
\qquad\text{i.e.}\qquad
(V_A)_{hh'}=\langle\psi_{h'}\vert\psi_h\rangle,
\qquad
p_h=\lVert\psi_h\rVert^2 .
\tag{2.2}
$$

**Relation to (1.6)–(1.7).** Apply $\langle h\rvert\otimes\mathbb 1_{\bar A}$ to any decomposition (1.6). Orthonormality of the place basis gives

$$
\lvert\psi_h\rangle=a_h\lvert E_h\rangle\qquad\text{for every joint place } h \text{ of } A .
\tag{2.3}
$$

Inserting (2.3) into (2.2) gives $(V_A)_{hh'}=\langle a_{h'}E_{h'}\vert a_hE_h\rangle=a_ha_{h'}^{*}\langle E_{h'}\vert E_h\rangle$, which is (1.7). So (2.2) is the witness rule written without the convention-dependent split.

### Step 3. Basic properties (item 1)

(i) *Self-adjoint:* $(V_A)_{h'h}^{*}=\langle\psi_h\vert\psi_{h'}\rangle^{*}=\langle\psi_{h'}\vert\psi_h\rangle=(V_A)_{hh'}$.
(ii) *Positive semidefinite:* for $\lvert\phi\rangle=\sum_hc_h\lvert h\rangle$, $\langle\phi\vert V_A\vert\phi\rangle=\sum_{h,h'}c_h^{*}c_{h'}\langle\psi_{h'}\vert\psi_h\rangle=\bigl\lVert\sum_hc_h^{*}\psi_h\bigr\rVert^2\ge0$.
(iii) *Unit trace:* $\operatorname{Tr}V_A=\sum_hp_h=\sum_h\lVert\psi_h\rVert^2=1$ by (2.1).
(iv) *Support:* if $h\notin H_V$, then $\psi_h=0$ by (2.2), so $(V_A)_{hh'}=(V_A)_{h'h}=0$ for every $h'$. Together:

$$
V_A=V_A^{\dagger}\ge0,\qquad \operatorname{Tr}V_A=\sum_hp_h=1,\qquad (V_A)_{hh'}=0\ \text{ unless } h,h'\in H_V .
\tag{2.4}
$$

(v) *Local readings.* In this item $r$ labels outcomes, as in (1.3). By A4, whether a joint place $K$ lies in the class $S_r$ depends only on $K|_A$. Hence $S_r=\{K:K|_A\in S^A_r\}$ with $S^A_r:=\{K|_A:K\in S_r\}$, and the $S^A_r$ partition the joint places of $A$. The places in $S_r$ are therefore the $\lvert h\rangle\otimes\lvert r'\rangle$ with $h\in S^A_r$ and an arbitrary joint place $r'$ of $\bar A$. So $\Pi_r=\Pi^A_r\otimes\mathbb 1_{\bar A}$ with $\Pi^A_r=\sum_{h\in S^A_r}\lvert h\rangle\langle h\rvert$. By (2.1) and the orthogonality of its terms,

$$
p(r)=\bigl\lVert\Pi_r\lvert\Psi\rangle\bigr\rVert^2=\Bigl\lVert\sum_{h\in S^A_r}\lvert h\rangle\otimes\lvert\psi_h\rangle\Bigr\rVert^2=\sum_{h\in S^A_r}p_h=\operatorname{Tr}\bigl(\Pi^A_rV_A\bigr).
\tag{2.5}
$$

(vi) *M6.* $V_A$ depends on $\lvert\Psi\rangle$ only through $\lvert\Psi\rangle\langle\Psi\rvert$, which is invariant under (1.2), and it is defined without the split (1.6). Hence $V_A$, $p_h$ and $H_V$ do not depend on these conventions; labels are treated in Step 8. The branch vectors themselves change under (1.2) by the common factor: $\psi_h\to e^{i\varphi}\psi_h$.

### Step 4. What the view does not see (item 3)

Let $\lvert\Phi\rangle$ be admissible, with branch vectors $\lvert\varphi_h\rangle$. The two forms of the condition are equivalent. If $\lvert\Phi\rangle=(\mathbb 1_A\otimes U)\lvert\Psi\rangle$, then $\varphi_h=(\langle h\rvert\otimes\mathbb 1)(\mathbb 1\otimes U)\Psi=U\psi_h$. Conversely, if $\varphi_h=U\psi_h$ for all $h$, then (2.1) gives $\Phi=\sum_h\lvert h\rangle\otimes U\psi_h=(\mathbb 1_A\otimes U)\Psi$.

($\Leftarrow$) $\langle\varphi_{h'}\vert\varphi_h\rangle=\langle U\psi_{h'}\vert U\psi_h\rangle=\langle\psi_{h'}\vert\psi_h\rangle$, so the views agree by (2.2).

($\Rightarrow$) By (2.2), equal views mean that the families $(\psi_h)_h$ and $(\varphi_h)_h$, indexed by the same joint places of $A$, have the same Gram matrix. By the standard fact, there is a linear isometry $U_0$ from $S_\Psi:=\operatorname{span}\{\psi_h\}$ onto $S_\Phi:=\operatorname{span}\{\varphi_h\}$ with $U_0\psi_h=\varphi_h$. Then $\dim S_\Psi=\dim S_\Phi$, so in the finite-dimensional $\mathcal H_{\bar A}$ (A1) the complements $S_\Psi^{\perp}$ and $S_\Phi^{\perp}$ have equal dimension. Let $U_1$ map an orthonormal basis of $S_\Psi^{\perp}$ onto one of $S_\Phi^{\perp}$. Then $U:=U_0\oplus U_1$ is unitary on $\mathcal H_{\bar A}$, and $\varphi_h=U\psi_h$:

$$
V_A(\Phi)=V_A(\Psi)
\iff
\exists\,U \text{ unitary on } \mathcal H_{\bar A}:\ \lvert\varphi_h\rangle=U\lvert\psi_h\rangle\ \ \forall h
\iff
\lvert\Phi\rangle=(\mathbb 1_A\otimes U)\lvert\Psi\rangle .
\tag{2.6}
$$

$U$ is fixed on $S_\Psi$ and arbitrary on $S_\Psi^{\perp}$. The common phase (1.2) is the case $U=e^{i\varphi}\mathbb 1_{\bar A}$.

### Step 5. The convention freedom in (1.6) and the branch Gram matrix

By (2.3), every decomposition (1.6) satisfies $a_hE_h=\psi_h$. If $h\notin H_V$, then $\psi_h=0$, and $a_h\neq0$ would force $E_h=0$, contradicting the normalization in (1.6); so $a_h=0$. If $h\in H_V$, then $\psi_h\neq0$, so $a_h\neq0$, $\lVert E_h\rVert=1$ and $\lvert a_h\rvert=\sqrt{p_h}$. The general decomposition is therefore

$$
a_h=\sqrt{p_h}\,e^{-i\theta_h},\qquad \lvert E_h\rangle=e^{i\theta_h}\,\frac{\lvert\psi_h\rangle}{\sqrt{p_h}}\qquad(h\in H_V),\qquad a_h=0\qquad(h\notin H_V),
\tag{2.7}
$$

with arbitrary real $\theta_h$. Every choice is a valid decomposition, because $\sum_{h\in H_V}\lvert h\rangle\otimes\psi_h=\Psi$ by (2.1). Two conventions differ exactly by the rephasing of item 4 ($\theta_h\to\theta_h+\delta_h$). From (2.7) and (2.2),

$$
G_{hh'}=\langle E_{h'}\vert E_h\rangle=e^{i(\theta_h-\theta_{h'})}\,\frac{(V_A)_{hh'}}{\sqrt{p_hp_{h'}}},\qquad h,h'\in H_V .
\tag{2.8}
$$

So $G$ is Hermitian with $G_{hh}=1$, and the shift $\theta\to\theta+\delta$ gives $G_{hh'}\to e^{i(\delta_h-\delta_{h'})}G_{hh'}$, as stated in item 4.

### Step 6. Cyclic products are invariant (item 4a)

Write $h_{k+1}:=h_1$. Under a rephasing,

$$
W(h_1,\dots,h_k)\;\longrightarrow\;\prod_{j=1}^{k}e^{i(\theta_{h_j}-\theta_{h_{j+1}})}G_{h_jh_{j+1}}
=\exp\Bigl(i\sum_{j=1}^{k}(\theta_{h_j}-\theta_{h_{j+1}})\Bigr)\,W(h_1,\dots,h_k)=W(h_1,\dots,h_k),
\tag{2.9}
$$

because the cyclic sum telescopes to zero. This uses only the transformation law, so (2.9) holds for every matrix on $H_V$. Insert (2.8) into the definition of $W$. The phases cancel in the same way, and $\prod_j\sqrt{p_{h_j}p_{h_{j+1}}}=\prod_jp_{h_j}$, because each $h_j$ occurs once as a first and once as a second index. Hence

$$
W(h_1,\dots,h_k)=\frac{(V_A)_{h_1h_2}(V_A)_{h_2h_3}\cdots(V_A)_{h_kh_1}}{p_{h_1}p_{h_2}\cdots p_{h_k}}
=\frac{\langle\psi_{h_2}\vert\psi_{h_1}\rangle\langle\psi_{h_3}\vert\psi_{h_2}\rangle\cdots\langle\psi_{h_1}\vert\psi_{h_k}\rangle}{p_{h_1}p_{h_2}\cdots p_{h_k}} .
\tag{2.10}
$$

In particular,

$$
W(h)=1,\qquad W(h,h')=\lvert G_{hh'}\rvert^2=\frac{\lvert(V_A)_{hh'}\rvert^2}{p_hp_{h'}} .
\tag{2.11}
$$

By (2.10) and Step 3 (vi), $W$ is a function of $V_A$ alone. It is therefore independent of the common phase and of the split.

### Step 7. Completeness of the cyclic products (item 4b)

Let $G,G'$ be Gram matrices of unit vectors on $H_V$, with cyclic products $W,W'$. The proof uses only Hermiticity, $G_{h'h}=G_{hh'}^{*}$, and the same for $G'$.

($\Rightarrow$) This is (2.9).

($\Leftarrow$) Assume $W=W'$ for all $k\ge1$ and all $h_i\in H_V$.

(i) Taking $k=1$ gives $G'_{hh}=G_{hh}$. Taking $k=2$ and using Hermiticity gives $\lvert G'_{hh'}\rvert^2=W'(h,h')=W(h,h')=\lvert G_{hh'}\rvert^2$. Let $\Gamma$ be the graph on $H_V$ with an edge between $h\neq h'$ iff $G_{hh'}\neq0$; by (i), $G'$ defines the same graph.

(ii) For a walk $\gamma=(g_0,\dots,g_m)$ in $\Gamma$, put $u_\gamma:=\prod_{j=0}^{m-1}G_{g_jg_{j+1}}$ ($u_\gamma:=1$ for $m=0$), and define $u'_\gamma$ likewise. By (i), $u_\gamma\neq0$ and $\lvert u'_\gamma\rvert=\lvert u_\gamma\rvert$, so $\omega_\gamma:=u'_\gamma/u_\gamma$ has unit modulus. Let $\gamma'$ be a second walk with the same ends. Running $\gamma$ and then $\gamma'$ backwards gives a closed walk $(c_0,\dots,c_n=c_0)$ with $n=m+m'$; take $n\ge1$, since otherwise there is nothing to show. By Hermiticity the backward run contributes $u^{*}_{\gamma'}$, so $\prod_{j=0}^{n-1}G_{c_jc_{j+1}}=W(c_0,\dots,c_{n-1})=u_\gamma u^{*}_{\gamma'}$, and likewise for $G'$. Then $W=W'$ gives $u'_\gamma u'^{*}_{\gamma'}=u_\gamma u^{*}_{\gamma'}$, i.e. $\omega_\gamma\,\omega^{*}_{\gamma'}=1$. So $\omega_\gamma$ depends only on the ends of $\gamma$.

(iii) In each connected component of $\Gamma$, fix a root $h_0$ and set $e^{-i\theta_h}:=\omega_\gamma$ for any walk $\gamma$ from $h_0$ to $h$; this is well defined by (ii), and $\theta_{h_0}=0$. Let $h,h'$ be adjacent. Appending $h'$ to a walk $\gamma$ from $h_0$ to $h$ multiplies $u_\gamma$ by $G_{hh'}$ and $u'_\gamma$ by $G'_{hh'}$. Hence $e^{-i\theta_{h'}}=e^{-i\theta_h}G'_{hh'}/G_{hh'}$, i.e. $G'_{hh'}=e^{i(\theta_h-\theta_{h'})}G_{hh'}$. For distinct non-adjacent $h,h'$ (in the same or in different components), both sides vanish by (i), and on the diagonal both sides agree by (i). Therefore

$$
G'_{hh'}=e^{i(\theta_h-\theta_{h'})}G_{hh'}\ \ \forall h,h'\in H_V \text{ for some real }(\theta_h)
\iff
W'(h_1,\dots,h_k)=W(h_1,\dots,h_k)\ \ \forall k\ge1,\ h_i\in H_V .
\tag{2.12}
$$

**Conclusion.** Let $F$ be a well-defined quantity built from $G$, i.e. invariant under every rephasing. If $G$ and $G'$ have the same cyclic products, then by (2.12) $G'$ is a rephasing of $G$, so $F(G')=F(G)$. Thus $F$ is constant on the level sets of $G\mapsto W$:

$$
F(G)=f\bigl(\{W(h_1,\dots,h_k)\}_{k\ge1,\ h_i\in H_V}\bigr).
\tag{2.13}
$$

### Step 8. Label-freedom (item 5)

Let $\pi$ be a permutation of $\{1,\dots,N\}$ with $T(\pi(a))=T(a)$. Let $U_\pi$ be the unitary on $\mathcal H$ that moves the entry in slot $a$ to slot $\pi(a)$: $U_\pi\lvert K\rangle=\lvert K^\pi\rangle$ with $(K^\pi)_{\pi(a)}:=K_a$. This is well defined because $\pi$ preserves types. $\pi$ maps each type class onto itself, so it is a product of transpositions $(a_jb_j)$ of same-type objects. The map $\pi\mapsto U_\pi$ is a representation of the permutation group (standard), and $U_{(ab)}=P_{ab}$ by (1.11). Hence $U_\pi=P_{a_1b_1}\cdots P_{a_mb_m}$, and applying (1.11) $m$ times (each step stays in $\mathcal H_{\rm adm}$) gives

$$
U_\pi\lvert\Psi\rangle=\epsilon_\pi\lvert\Psi\rangle,\qquad \epsilon_\pi=\prod_{j=1}^{m}c_{T(a_j)}\in\{+1,-1\},\qquad \lvert\Psi\rangle\in\mathcal H_{\rm adm}.
\tag{2.14}
$$

The natural identification is the unitary $J_\pi:\mathcal H_A\to\mathcal H_{\pi(A)}$, $J_\pi\lvert h\rangle=\lvert h^\pi\rangle$ with $(h^\pi)_{\pi(a)}:=h_a$. Define $\bar J_\pi:\mathcal H_{\bar A}\to\mathcal H_{\overline{\pi(A)}}$ in the same way, using $\pi(\bar A)=\overline{\pi(A)}$. Since $K^\pi|_{\pi(A)}=(K|_A)^\pi$, $U_\pi=J_\pi\otimes\bar J_\pi$ in the factorizations with respect to $A$ and $\pi(A)$. By (2.14) and $\langle h^\pi\rvert J_\pi=\langle h\rvert$, the branch vectors of $\Psi$ for the part $\pi(A)$ are $\lvert\psi^{\pi(A)}_{h^\pi}\rangle=\epsilon_\pi(\langle h^\pi\rvert\otimes\mathbb 1)(J_\pi\otimes\bar J_\pi)\lvert\Psi\rangle=\epsilon_\pi\bar J_\pi\lvert\psi^A_h\rangle$. Then (2.2), the unitarity of $\bar J_\pi$ and $\epsilon_\pi^2=1$ give

$$
\langle h^\pi\vert V_{\pi(A)}(\Psi)\vert h'^\pi\rangle=\langle h\vert V_A(\Psi)\vert h'\rangle,
\qquad\text{i.e.}\qquad
V_{\pi(A)}(\Psi)=J_\pi\,V_A(\Psi)\,J_\pi^{\dagger}.
\tag{2.15}
$$

**Consequence.** By (2.15), and by (2.10) for $W$,

$$
p^{\pi(A)}_{h^\pi}=p^A_h,\qquad H_V^{\pi(A)}=\{h^\pi:h\in H_V^A\},\qquad W^{\pi(A)}(h_1^\pi,\dots,h_k^\pi)=W^A(h_1,\dots,h_k).
\tag{2.16}
$$

A part $A'$ that differs from $A$ only in which identical-type instances it contains has, for each type, the same number of objects as $A$. The same then holds for $\bar A'$ and $\bar A$. Type-preserving bijections $A\to A'$ and $\bar A\to\bar A'$ combine to a type-preserving $\pi$ with $\pi(A)=A'$, so (2.16) applies. Two such choices $\pi,\pi'$ differ by $\sigma=\pi'^{-1}\pi$, which is type-preserving with $\sigma(A)=A$, and $J_\pi=J_{\pi'}J_\sigma$. (2.15) for $\sigma$ gives $J_\sigma V_AJ_\sigma^{\dagger}=V_A$, hence $J_\pi V_AJ_\pi^{\dagger}=J_{\pi'}V_AJ_{\pi'}^{\dagger}$: the correspondence does not depend on the choice of $\pi$.

## Result

- **Gram form (item 2):** $(V_A)_{hh'}=\langle\psi_{h'}\vert\psi_h\rangle$, $p_h=\lVert\psi_h\rVert^2$ (2.2), and $\lvert\psi_h\rangle=a_h\lvert E_h\rangle$ (2.3), which recovers (1.7).
- **Basic properties (item 1):** $V_A$ is a density operator supported on $\operatorname{span}\{\lvert h\rangle:h\in H_V\}$ (2.4), and $p(r)=\operatorname{Tr}(\Pi^A_rV_A)$ for every local reading (2.5).
- **Invisible data (item 3):** $V_A(\Phi)=V_A(\Psi)$ iff $\lvert\Phi\rangle=(\mathbb 1_A\otimes U)\lvert\Psi\rangle$ for a unitary $U$ on $\mathcal H_{\bar A}$ (2.6).
- **Companion invariants (item 4):** the split freedom is exactly (2.7), and $G$ is given by (2.8). The cyclic products are rephasing invariant (2.9), and $W(h_1,\dots,h_k)=\prod_j(V_A)_{h_jh_{j+1}}/\prod_jp_{h_j}$ (2.10)–(2.11). They are complete: two Gram matrices are related by a rephasing iff all their cyclic products agree (2.12), so every well-defined function of $G$ is a function of the $W$'s (2.13).
- **Label-freedom (item 5):** $V_{\pi(A)}(\Psi)=J_\pi V_A(\Psi)J_\pi^{\dagger}$ (2.15), hence $p_h$, $H_V$ and $W$ are unchanged under exchange of identical-type instances (2.16).
- **M6 status:** $V_A$, $p_h$, $H_V$, $W$ are well defined. $\lvert\psi_h\rangle$ is defined up to the common phase, and the view sees it only up to $U$ in (2.6). $G$ depends on the convention, and only its rephasing class is data.

## Consistency checks

1. **Two-branch witness rule.** Take $\lvert\Psi\rangle=a\lvert0\rangle\lvert E_0\rangle+b\lvert1\rangle\lvert E_1\rangle$ with unit $E_0,E_1$. Then (2.1) gives $\psi_0=aE_0$, $\psi_1=bE_1$, and (2.2) gives $p_0=\lvert a\rvert^2$, $p_1=\lvert b\rvert^2$, $(V_A)_{01}=ab^{*}\langle E_1\vert E_0\rangle$. This is the cross term $ab^{*}$ of $a\lvert0\rangle+b\lvert1\rangle$ multiplied by the overlap, and it vanishes for orthogonal $E_0,E_1$, as in Section 3 of the base problem.
2. **Product state.** For $\lvert\Psi\rangle=\lvert\psi_A\rangle\otimes\lvert e\rangle$ with $\lvert\psi_A\rangle=\sum_hc_h\lvert h\rangle$: $\psi_h=c_he$ and $(V_A)_{hh'}=c_hc_{h'}^{*}$. The numerator of (2.10) is $\prod_jc_{h_j}c^{*}_{h_{j+1}}=\prod_j\lvert c_{h_j}\rvert^2$, so $W=1$ for every cycle. Consistently with (2.12), (2.8) with $\theta_h=-\arg c_h$ gives $G_{hh'}=1$ for all $h,h'$: the companion witnesses nothing.
3. **Orthogonal branch states.** If $\langle E_{h'}\vert E_h\rangle=\delta_{hh'}$ on $H_V$, then $G=\mathbb 1$ in every convention, and $V_A$ is diagonal by (2.8). A tuple containing two different places has a cyclically consecutive pair $h_j\neq h_{j+1}$, so $W=0$. If all entries are equal, $W=1$, in agreement with (2.10)–(2.11).

## Open issues

- $(p,W)$ do not determine $V_A$. By (2.8) with $\theta=0$ and by (2.12), they fix $V_A$ only up to $V_A\to DV_AD^{\dagger}$ with $D$ diagonal unitary in the place basis of $A$. An example: $\lvert\pm\rangle\otimes\lvert e\rangle$ with $\lvert\pm\rangle=(\lvert0\rangle\pm\lvert1\rangle)/\sqrt2$. The phases lost in this way are well-defined data of $V_A$, but they are not companion data. Whether later packages need them is open.
- (2.6) does not assert that $(\mathbb 1_A\otimes U)\lvert\Psi\rangle$ is admissible for every $U$. Which $U$ preserve $\mathcal H_{\rm adm}$ depends on (1.11) and is out of scope.
- (2.15)–(2.16) relate labelled joint places $h\leftrightarrow h^\pi$. A label-free specification of a part (A7) remains open. No spatial meaning is attached to $p_h$, $G$ or $W$ (M1, M4).

## Methods used

- Partial trace; branch decomposition in the place basis
- Gram matrices; unitary extension of an isometry between spans
- Gauge (rephasing) invariance; cyclic invariants; walks and connected components of a graph
- Permutation representation on tensor products; swap eigenvalues (1.11)
