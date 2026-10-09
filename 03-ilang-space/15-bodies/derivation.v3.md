# Bodies, positions and the two-body distance in the leading-order witness geometry

- **Subproject:** 03-ilang-space
- **Package:** 03-ilang-space/15-bodies
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-08

## Changes from previous version

- **I1 (instantaneous recoverability).** In v2, Step 7, item 3 said without qualification that the configuration and $D$ are not functions of $V_{\{c\}}(\lambda)$ at every $\lambda$. That is false for a single realizable configuration, and false for $D$ when $D$ is constant. Item 3 now says "not necessarily". It also states the criterion at a fixed $\lambda$ separately for the configuration and for $D$, and gives the two exceptions: a single configuration, and constant $D$. In the Result, the "Line" bullet now treats $c_T=-1$, $n=2$ separately: there $D$ is a function at every $\lambda$. In the other positive cases $D$ fails at $\lambda=0$, and for $X=\sigma_x$ also at $\lambda=\pi$. The "(S2), medium" and "Window" bullets now separate recovering $D$ from recovering the configuration.
- **I2 (the medium and $D$).** The last sentence of Step 5 no longer says that the medium carries $D$. It now says that the medium records the pair vector $s$ at leading order, and that $s$ determines $D$ only under the fibre condition of Step 7.
- Nothing else is changed. All tags (15.1)–(15.22) are unchanged, and there are no new tags.

## Response to verification

- **I1:** Accepted and fixed in Step 7, item 3, and in the Result bullets "(S2), medium", "Line" and "Window". Item 3 sits under "(15.14) holds", and a single realizable configuration satisfies (15.14) trivially. So the v2 claim failed for $c_T=-1$, $n=2$ (line and window). By (15.17) the window with $c_T=-1$, $m=1$ has $D=\sqrt2$ for every configuration. There $D$ is a function of $V_{\{c\}}(\lambda)$ at every $\lambda$, including the revival (15.22), but for $n\ge3$ the configuration is not.
- **I2:** Accepted and fixed in Step 5, last paragraph. The counterexample is in Step 8 ($c_T=+1$, $n\ge3$): $\{h_1,h_3\}$ and $\{h_2,h_2\}$ have the same index sum, hence identical medium states for every $\lambda$ by (15.16), but $D=2\sigma_X$ and $D=0$.

## Setup and assumptions

- **Objects, settings, definitions.** The objects and the settings (S1), (S2) are those of question.md. So are the definitions of background, localized body, position, configuration, two-body distance $D$ and state of the medium. These notions mean only what their definitions say (M1, M4).
- **Notation.** For a self-adjoint $Y$ on $\mathcal H_c$: $\langle Y\rangle=\langle\chi\vert Y\vert\chi\rangle$ and $\tilde Y:=Y-\langle Y\rangle\mathbb 1$. Record vectors: $\lvert u_h\rangle=\tilde K_h\lvert\chi\rangle$ (5.10). Since $h\sim_0h'$ iff $u_h=u_{h'}$, the vector $u_x:=u_h$ ($h\in x$) is well defined for a background point $x$, and $d_0(x,x')=\lVert u_x-u_{x'}\rVert$ (5.11). $d_c:=\dim\mathcal H_c$.
- **Inputs used** (all quoted in question.md): (2.1), (2.2) $(V_A)_{hh'}=\langle\psi_{h'}\vert\psi_h\rangle$, $p_h=\lVert\psi_h\rVert^2$; (2.11) $W(h,h')=\lvert(V_A)_{hh'}\rvert^2/(p_hp_{h'})$; (2.16) relabelling covariance; (3.5); (5.1) $e^{-iC\lambda}=\sum_h\lvert h\rangle\langle h\rvert\otimes e^{-iK_h\lambda}$; (5.6) $W(h,h';\lambda)=\lvert\langle\chi\vert e^{iK_{h'}\lambda}e^{-iK_h\lambda}\vert\chi\rangle\rvert^2$; (5.10), (5.11); (12.6) the split $K^{(1)}_h\to K^{(1)}_h+X$, $K^{(2)}_h\to K^{(2)}_h-X$, $\Delta\to\Delta+2X$; (12.7) $C=\sum_h(\lvert h\rangle\langle h\rvert_{b_1}+\lvert h\rangle\langle h\rvert_{b_2})\otimes K_h-\mathbb 1_{b_1b_2}\otimes\Delta$; (12.13) $d_0((h_1,h_2),(h_1',h_2'))=\lVert u_{h_1}+u_{h_2}-u_{h_1'}-u_{h_2'}\rVert$.
- **Assumptions.** A1 (finite dimension) and A5 ($\lambda$-independent contracts). $\lambda\in\mathbb R$. "For every $\lambda$" is exact; "leading order" means $\lambda\to0^+$. Two starts are always compared within one description (same $C$, $\chi$, $c_T$).

## Derivation

### Step 1. Two facts on orbits of the medium

Let $Y_1,Y_2$ be self-adjoint on $\mathcal H_c$, with $f_j(\lambda):=e^{-iY_j\lambda}\lvert\chi\rangle$, $a_j:=\tilde Y_j\lvert\chi\rangle$, and $\langle\chi\vert a_j\rangle=0$.

**(i) Leading order.** We have $\langle f_2\vert f_1\rangle=e^{i(\langle Y_2\rangle-\langle Y_1\rangle)\lambda}\langle\chi\vert e^{i\tilde Y_2\lambda}e^{-i\tilde Y_1\lambda}\vert\chi\rangle$. Expanding the exponentials to second order and using $\langle\tilde Y_j\rangle=0$ gives $\langle\chi\vert e^{i\tilde Y_2\lambda}e^{-i\tilde Y_1\lambda}\vert\chi\rangle=1+\lambda^2z+O(\lambda^3)$, with $z=\langle a_2\vert a_1\rangle-\tfrac12\lVert a_1\rVert^2-\tfrac12\lVert a_2\rVert^2$. Since $2\operatorname{Re}z=-\lVert a_1-a_2\rVert^2$,

$$
1-\lvert\langle f_2(\lambda)\vert f_1(\lambda)\rangle\rvert^2=\lambda^2\,\bigl\lVert\tilde Y_1\chi-\tilde Y_2\chi\bigr\rVert^2+O(\lambda^3).
\tag{15.1}
$$

This is the content of (5.6) and (5.10) for two operators. So $f_1,f_2$ are the same state at leading order iff $\tilde Y_1\chi=\tilde Y_2\chi$.

**(ii) Exact.** The two orbits are the same state for every $\lambda$ iff

$$
(Y_1-Y_2)\,Y_1^n\lvert\chi\rangle=\mu_0\,Y_1^n\lvert\chi\rangle\quad(n=0,\dots,d_c-1),\qquad\mu_0:=\langle Y_1\rangle-\langle Y_2\rangle ,
\tag{15.2}
$$

and in that case $f_2(\lambda)=e^{i\mu_0\lambda}f_1(\lambda)$.
- ($\Leftarrow$) $\mathcal Z:=\operatorname{span}\{Y_1^n\chi\}$ is $Y_1$-invariant, and by Cayley–Hamilton $n<d_c$ suffices. On $\mathcal Z$ we have $Y_2=Y_1-\mu_0$, so $\mathcal Z$ is $Y_2$-invariant and $e^{-iY_2\lambda}=e^{i\mu_0\lambda}e^{-iY_1\lambda}$ on $\mathcal Z\ni\chi$.
- ($\Rightarrow$) Write $f_1=\omega f_2$, where $\omega=\langle f_2\vert f_1\rangle$ is analytic and $\lvert\omega\rvert=1$. Differentiating gives $-iY_1f_1=(\omega'/\omega)f_1-iY_2f_1$, so $f_1(\lambda)$ is an eigenvector of $Y_1-Y_2$. Its eigenvalue $\langle f_1\vert(Y_1-Y_2)\vert f_1\rangle$ is continuous and takes values in a finite spectrum, so it is constant, equal to $\mu_0$. Hence $f_1(\lambda)\in\ker(Y_1-Y_2-\mu_0)$ for all $\lambda$, and so is every derivative $(-iY_1)^n\chi$ at $\lambda=0$.

The case $n=0$ of (15.2) is exactly $\tilde Y_1\chi=\tilde Y_2\chi$.

### Step 2. One body (S1): item 1

**(a)** By (5.1), $e^{-iC\lambda}(\lvert\beta\rangle\otimes\lvert\chi\rangle)=\lvert\beta\rangle\otimes e^{-iK_\beta\lambda}\lvert\chi\rangle$. The state is a product, so (1.5) gives

$$
\lvert\Psi(\lambda)\rangle=\lvert\beta\rangle\otimes\lvert E_\beta(\lambda)\rangle,\quad
\lvert E_\beta(\lambda)\rangle=e^{-iK_\beta\lambda}\lvert\chi\rangle,\quad
V_{\{b\}}=\lvert\beta\rangle\langle\beta\rvert,\quad
V_{\{c\}}=\lvert E_\beta\rangle\langle E_\beta\rvert .
\tag{15.3}
$$

$H_V=\{\beta\}\subseteq[\beta]_0$, so the body is localized at $[\beta]_0$ for every $\lambda$ and is never correlated with the medium. The state of the medium is pure.

**(b)** Apply Step 1 with $Y_1=K_\beta$, $Y_2=K_{\beta'}$. Then $\tilde Y_1\chi-\tilde Y_2\chi=u_\beta-u_{\beta'}$, and by (5.6) $\lvert\langle E_{\beta'}\vert E_\beta\rangle\rvert^2=W(\beta,\beta';\lambda)$, the witness weight of the product start $\lvert\phi\rangle\otimes\lvert\chi\rangle$. Hence

$$
\begin{aligned}
&\text{same state }\forall\lambda\iff(K_\beta-K_{\beta'})K_\beta^n\chi=\bigl(\langle K_\beta\rangle-\langle K_{\beta'}\rangle\bigr)K_\beta^n\chi\ \ \forall n\iff W(\beta,\beta';\lambda)=1\ \ \forall\lambda,\\
&\text{same state at leading order}\iff u_\beta=u_{\beta'}\iff[\beta]_0=[\beta']_0,\qquad 1-\lvert\langle E_{\beta'}\vert E_\beta\rangle\rvert^2=\lambda^2d_0(\beta,\beta')^2+O(\lambda^3).
\end{aligned}
\tag{15.4}
$$

**Relation to the background.**
- At leading order, the medium state determines the position, and is determined by it. Two places give the same leading-order medium state iff they are the same background point, and the medium states of different points separate at the rate $d_0$.
- The exact condition is the leading-order one ($n=0$) together with the conditions $n\ge1$. It therefore implies $[\beta]_0=[\beta']_0$, but not conversely. Example: $\mathcal H_c=\mathbb C^2$, $\chi=\lvert0\rangle$, $K_{\beta'}=\sigma_x$, $K_\beta=\sigma_x+\lvert1\rangle\langle1\rvert$. Here $u_\beta=u_{\beta'}$, but $(K_\beta-K_{\beta'})K_\beta\chi=\lvert1\rangle\neq0=\mu_0K_\beta\chi$.

### Step 3. Two bodies (S2), exact state: item 2(a)

Insert $\mathbb 1=\sum_{h}\lvert h\rangle\langle h\rvert$ for the other body in each term of (12.7):

$$
C=\sum_{h_1,h_2}\lvert h_1h_2\rangle\langle h_1h_2\rvert\otimes K_{h_1h_2},\qquad
K_{h_1h_2}:=K_{h_1}+K_{h_2}-\Delta=K_{h_2h_1}=K_{h_1h_2}^{\dagger}.
\tag{15.5}
$$

The projectors $\lvert h_1h_2\rangle\langle h_1h_2\rvert$ are orthogonal and complete, so $e^{-iC\lambda}=\sum\lvert h_1h_2\rangle\langle h_1h_2\rvert\otimes e^{-iK_{h_1h_2}\lambda}$, as for (5.1). Both terms of the start carry the same operator $K_{\beta_1\beta_2}=K_{\beta_2\beta_1}$, so

$$
\lvert\Psi(\lambda)\rangle=\lvert\beta_1\beta_2\rangle_{c_T}\otimes\lvert E_{\beta_1\beta_2}(\lambda)\rangle,\qquad
\lvert E_{\beta_1\beta_2}(\lambda)\rangle=e^{-iK_{\beta_1\beta_2}\lambda}\lvert\chi\rangle .
\tag{15.6}
$$

The state is admissible, since $P_{12}\lvert\beta_1\beta_2\rangle_{c_T}=c_T\lvert\beta_1\beta_2\rangle_{c_T}$. For every $\lambda$:
- The pair is not correlated with the medium.
- $V_{\{b_1,b_2\}}=\lvert\beta_1\beta_2\rangle_{c_T}\langle\beta_1\beta_2\rvert_{c_T}$ with $H_V=\{(\beta_1,\beta_2),(\beta_2,\beta_1)\}$. Both elements have the multiset $\{[\beta_1]_0,[\beta_2]_0\}$, so the pair stays localized at this configuration.
- The state of the medium $V_{\{c\}}=\lvert E_{\beta_1\beta_2}\rangle\langle E_{\beta_1\beta_2}\rvert$ is pure.

The two-body distance is

$$
D=d_0\bigl([\beta_1]_0,[\beta_2]_0\bigr)=\bigl\lVert u_{\beta_1}-u_{\beta_2}\bigr\rVert,\qquad\text{independent of }\lambda .
\tag{15.7}
$$

### Step 4. Well-definedness (M6): item 2(b)

1. **Uniqueness.** $H_V\neq\emptyset$, so the configuration is unique. It is a multiset: no body is assigned a particular point (Law 5), and $D$ is symmetric in $x_1,x_2$.
2. **Labels, state side.** Take (2.16) with $\pi=(b_1b_2)$ and $\pi(A)=A=\{b_1,b_2\}$. It maps $H_V$ to $\{(h_2,h_1)\}$, and the multiset $\{[h_1]_0,[h_2]_0\}$ does not change.
3. **Split (12.6).** $C$ and $K_{h_1h_2}=K^{(1)}_{h_1}+K^{(2)}_{h_2}$ do not change, while
$$
u_h\to u_h+w\quad\text{for all }h,\qquad w:=\tilde X\lvert\chi\rangle .
\tag{15.8}
$$
A common translation leaves $\sim_0$, $[h]_0$, $d_0$, the configuration and $D$ unchanged.
4. **Labels, contract side.** Exchanging the labels gives $b_1$ the term $K^{(2)}_h=K_h-\Delta$. The new data are $K_h\to K_h-\Delta$, $\Delta\to-\Delta$, which is (12.6) with $X=-\Delta$, already covered by 3. Moreover $P_{12}CP_{12}=C$ by (15.5).
5. **$\Delta$.** $u_h$ is built from $K_h$ alone, so at fixed $K_h$ the configuration and $D$ do not depend on $\Delta$. For a given $C$, $\Delta$ is moreover pure convention: (12.6) with $X=-\Delta/2$ sets it to $0$. $\Delta$ enters only the medium state (15.6).
6. **Phases.** $H_V$ is built from the $p_h$, which do not depend on any phase. Changing $\chi\to e^{i\varphi}\chi$ multiplies all $u_h$ by $e^{i\varphi}$, an isometry. The phase split (1.6) is not used.

**Conclusion.** The positions (as an unordered pair) and $D$ are well defined. $D$ depends only on the configuration, $\chi$ and $C$, through $u_h-u_{h'}=\widetilde{(K_h-K_{h'})}\,\chi$ with $K_h-K_{h'}=K_{hk}-K_{h'k}$ for any $k$.

### Step 5. The views of the bodies: item 2(c)

Let $\beta_1\neq\beta_2$. The companion of $\{b_1\}$ is $\{b_2,c\}$. Grouping (15.6) by the place of $b_1$ (2.1) gives:
- $\psi_{\beta_1}=2^{-1/2}\lvert\beta_2\rangle\otimes\lvert E\rangle$;
- $\psi_{\beta_2}=c_T2^{-1/2}\lvert\beta_1\rangle\otimes\lvert E\rangle$;
- all other $\psi_h=0$.

Hence $\langle\psi_{\beta_2}\vert\psi_{\beta_1}\rangle=0$. By (2.2) and (2.11):

$$
V_{\{b_1\}}=\tfrac12\bigl(\lvert\beta_1\rangle\langle\beta_1\rvert+\lvert\beta_2\rangle\langle\beta_2\rvert\bigr),\qquad H_V=\{\beta_1,\beta_2\},\qquad W(\beta_1,\beta_2)=0,\ \ \alpha=\tfrac{\pi}{2}.
\tag{15.9}
$$

The witness of the cross term is $b_2$, whose branch states $\lvert\beta_2\rangle,\lvert\beta_1\rangle$ are orthogonal. $V_{\{b_2\}}$ is the same by (2.16). For $\beta_1=\beta_2=\beta$, $V_{\{b_1\}}=\lvert\beta\rangle\langle\beta\rvert$. The view of the pair is pure:

$$
V_{\{b_1,b_2\}}=\lvert\beta_1\beta_2\rangle_{c_T}\langle\beta_1\beta_2\rvert_{c_T},\qquad p_{(\beta_1,\beta_2)}=p_{(\beta_2,\beta_1)}=\tfrac12,\qquad W\bigl((\beta_1,\beta_2),(\beta_2,\beta_1)\bigr)=\frac{\lvert c_T/2\rvert^2}{1/4}=1 .
\tag{15.10}
$$

**Normalized witness geometry.** $X_V$ of the pair view is a single point, and (15.9) gives two points at angle $\pi/2$. These normalized witness data ($W$, $\alpha$, and $X_V$ as an abstract metric space) do not depend on $D$, $\lambda$, $\Delta$, $\chi$ or the $K_h$: they are the same for every start with $\beta_1\neq\beta_2$. Hence $D$ is not a quantity of the witness geometry of either view. The background, through which $D$ is defined, is the geometry of a different start (a product start).

**Full views.** The full place-indexed views do retain the configuration. The place basis is type data (A2), not an instance label, and $V_{\{b_1\}}$ and $V_{\{b_2\}}$ have the same diagonal by (2.16). Define the occupation numbers

$$
n_h:=2\,\langle h\vert V_{\{b_1\}}\vert h\rangle\in\{0,1,2\},\qquad\sum_hn_h=2 .
\tag{15.20}
$$

By (15.9), $n_{\beta_1}=n_{\beta_2}=1$ for $\beta_1\neq\beta_2$, and $n_\beta=2$ for $\beta_1=\beta_2=\beta$. So $n$ is the place multiset $\{\beta_1,\beta_2\}$, and each element of the support $H_V$ of (15.10) gives the same multiset. Applying $h\mapsto[h]_0$ gives the configuration, and (15.7) then gives $D$. Thus the views determine $D$ together with the background, which $C$ and $\chi$ fix through (5.10). The medium, by contrast, records at leading order only the pair vector $s$ (Steps 6, 7). This determines $D$ only when $D$ is constant on each set of realizable configurations with the same $s$, which fails in general: the line configurations $\{h_1,h_3\}$ and $\{h_2,h_2\}$ have the same medium state for every $\lambda$ but $D=2\sigma_X$ and $D=0$ (Step 8).

### Step 6. The state of the medium: item 2(d)

Apply Step 1 with $Y_1=K_{\beta_1\beta_2}$ and $Y_2=K_{\beta_1'\beta_2'}$. Since $\tilde K_{h_1h_2}\chi=u_{h_1}+u_{h_2}-\tilde\Delta\chi$, the $\Delta$ term cancels in the difference. Write $s(x_1,x_2):=u_{x_1}+u_{x_2}$, the pair record vector of a configuration. Then (15.1) and the expression (12.13) give

$$
1-\bigl\lvert\langle E_{\beta_1'\beta_2'}\vert E_{\beta_1\beta_2}\rangle\bigr\rvert^2
=\lambda^2\bigl\lVert u_{\beta_1}+u_{\beta_2}-u_{\beta_1'}-u_{\beta_2'}\bigr\rVert^2+O(\lambda^3)
=\lambda^2\,d_0\bigl((\beta_1,\beta_2),(\beta_1',\beta_2')\bigr)^2+O(\lambda^3),
\tag{15.11}
$$

$$
\text{same state at leading order}\iff u_{\beta_1}+u_{\beta_2}=u_{\beta_1'}+u_{\beta_2'}\iff d_0\bigl((\beta_1,\beta_2),(\beta_1',\beta_2')\bigr)=0 .
\tag{15.12}
$$

**Relation to the pair geometry.** Two starts give the same leading-order medium state iff their joint places are the same point of the pair geometry (12.13). For $c_T=+1$ this is the leading-order geometry of the view of $\{b_1,b_2\}$ for the start $\phi\otimes\phi\otimes\chi$. The two medium states separate at the rate of the pair-geometry distance. For $c_T=-1$, (12.13) is used only as a formula. The condition (15.12) is invariant under (15.8), since $2w$ cancels, and it depends only on the configurations.

**Sufficient condition for every $\lambda$.** If $K_{\beta_1'\beta_2'}=K_{\beta_1\beta_2}-\mu$, then $e^{-iK_{\beta_1'\beta_2'}\lambda}=e^{i\mu\lambda}e^{-iK_{\beta_1\beta_2}\lambda}$, so

$$
K_{\beta_1}+K_{\beta_2}-K_{\beta_1'}-K_{\beta_2'}=\mu\,\mathbb 1\ \ (\mu\in\mathbb R)\ \Longrightarrow\ \lvert E_{\beta_1'\beta_2'}(\lambda)\rangle=e^{i\mu\lambda}\lvert E_{\beta_1\beta_2}(\lambda)\rangle\ \ \forall\lambda .
\tag{15.13}
$$

This condition does not involve $\Delta$. The necessary and sufficient condition is (15.2) with $Y_1=K_{\beta_1\beta_2}$, $Y_2=K_{\beta_1'\beta_2'}$. There $Y_1-Y_2$ does not depend on $\Delta$, but $Y_1^n\chi$ does.

### Step 7. Does the medium determine $D$? Item 2(e)

By (15.12), the leading-order medium state is a function of the configuration, and it fixes the configuration only up to the value of $s$. $D$ is a function of the leading-order medium state iff equal $s$ implies equal $D$. This fails in general: the line example (Step 8) has distinct configurations with equal $s$ and different $D$, and their medium states are even identical for every $\lambda$.

Realizable configurations:
- $c_T=+1$: all multisets of background points;
- $c_T=-1$: $x_1\neq x_2$, or $x_1=x_2$ when $x_1$ contains at least two places.

By (15.12), the leading-order medium state distinguishes all configurations iff $s$ is injective on them:

$$
u_{x_1}+u_{x_2}=u_{x_1'}+u_{x_2'}\ \Longrightarrow\ \{x_1,x_2\}=\{x_1',x_2'\}\qquad\text{for all realizable configurations.}
\tag{15.14}
$$

Equivalently, no two distinct realizable configurations share the midpoint $\tfrac12(u_{x_1}+u_{x_2})$. For $c_T=+1$ this excludes in particular any record vector being the midpoint of two others. (15.14) is invariant under (15.8).

**Leading order, orbit and instantaneous state.** The leading-order medium state and the relation "same for every $\lambda$" are properties of the whole orbit $\lambda\mapsto V_{\{c\}}(\lambda)$, not of $V_{\{c\}}$ at one $\lambda$. When (15.14) holds:
1. The configuration and $D$ are functions of the leading-order medium state. They are therefore also functions of the orbit, since equal orbits have equal leading-order states.
2. They are functions of the instantaneous state for small $\lambda\neq0$. There are finitely many starts (joint places). For each pair of starts with $s\neq s'$, (15.11) gives $1-\lvert\langle E'\vert E\rangle\rvert^2>0$ for $0<\lvert\lambda\rvert<\lambda_{ss'}$, with some $\lambda_{ss'}>0$. Let $\lambda_0>0$ be the minimum over these finitely many pairs. Then
$$
0<\lvert\lambda\rvert<\lambda_0:\qquad V_{\{c\}}(\lambda)\ \text{determines } s,\ \text{hence, under (15.14), the configuration and } D .
\tag{15.21}
$$
3. They are not necessarily functions of $V_{\{c\}}(\lambda)$ at every $\lambda$, and the configuration and $D$ must be treated separately. At a fixed $\lambda$, $V_{\{c\}}(\lambda)$ determines the configuration iff it differs for any two distinct realizable configurations. It determines $D$ iff $D$ is constant on every set of realizable configurations with the same $V_{\{c\}}(\lambda)$, which is a weaker condition.
   - At $\lambda=0$ every start gives $V_{\{c\}}=\lvert\chi\rangle\langle\chi\rvert$. So the configuration is determined iff there is a single realizable configuration, and $D$ iff $D$ is constant on the realizable configurations.
   - At finite $\lambda$, revivals can merge configurations with different $D$ (Steps 8, 9).
   - Exceptions occur. With a single realizable configuration (line and window, $c_T=-1$, $n=2$), the configuration and $D$ are functions of $V_{\{c\}}(\lambda)$ at every $\lambda$. In the window with $c_T=-1$, $m=1$, $D=\sqrt2$ is constant by (15.17), so $D$ is a function of $V_{\{c\}}(\lambda)$ at every $\lambda$. For $n\ge3$ the configuration there is not a function of $V_{\{c\}}(0)$ or of $V_{\{c\}}(\pi)$ (15.22).

### Step 8. Line: item 3(a)

Here $u_{h_i}=i\,\xi$ with $\xi:=\tilde X\chi$ and $\lVert\xi\rVert^2=\langle X^2\rangle-\langle X\rangle^2=\sigma_X^2>0$. All $u_{h_i}$ are distinct, so every place is its own background point and the background is $\{1,\dots,n\}$ with the metric $\sigma_X\lvert i-j\rvert$:

$$
d_0(h_i,h_j)=\sigma_X\lvert i-j\rvert,\qquad D\bigl(\{h_{i_1},h_{i_2}\}\bigr)=\sigma_X\lvert i_1-i_2\rvert .
\tag{15.15}
$$

With $\Delta=0$: $K_{h_{i_1}h_{i_2}}=(i_1+i_2)X$ and $E=e^{-i(i_1+i_2)X\lambda}\chi$.
- Equal sums give identical states, by (15.13) with $\mu=0$.
- Unequal sums give $\lambda^2\sigma_X^2(i_1+i_2-i_1'-i_2')^2\neq0$ in (15.11), so the states differ at leading order and hence at small $\lambda$.

Therefore

$$
\text{same medium state (for every }\lambda\text{, and at leading order)}\iff i_1+i_2=i_1'+i_2' .
\tag{15.16}
$$

A sum together with $\lvert i_1-i_2\rvert$ fixes the multiset. So distinct configurations with the same sum always have different $D$.

Coincidences exist exactly in these cases:
- $c_T=+1$, $n\ge3$: for example $\{h_1,h_3\}$ and $\{h_2,h_2\}$, with $D=2\sigma_X$ and $D=0$;
- $c_T=-1$, $n\ge4$: for example $\{h_1,h_4\}$ and $\{h_2,h_3\}$, with $D=3\sigma_X$ and $D=\sigma_X$.

For $c_T=+1$, $n=2$ the sums are $2,3,4$; for $c_T=-1$, $n=3$ they are $3,4,5$.

**Answer.**
- **Leading-order state and orbit.** $D$ is a function of the leading-order medium state, and of the orbit, iff $n=2$ ($c_T=+1$) or $n\le3$ ($c_T=-1$). The medium records only $i_1+i_2$, that is, the midpoint of the record vectors.
- **Instantaneous state, negative cases.** The coinciding configurations have identical medium states for every $\lambda$. So $D$ is a function of $V_{\{c\}}(\lambda)$ at no $\lambda$.
- **Instantaneous state, positive cases.** $D$ is a function of $V_{\{c\}}(\lambda)$ for $0<\lvert\lambda\rvert<\lambda_0$, by (15.21). It is not a function at every $\lambda$ in general. Example: $\mathcal H_c=\mathbb C^2$, $X=\sigma_x$, $\chi=\lvert0\rangle$, so $\sigma_X=1$. Then $e^{-iS\sigma_x\pi}\chi=(-1)^S\chi$ for every sum $S$, so at $\lambda=\pi$ all configurations give the same medium state. Their $D$ takes the values $0,\sigma_X$ ($c_T=+1$, $n=2$) and $\sigma_X,2\sigma_X$ ($c_T=-1$, $n=3$).
- **Trivial case.** For $c_T=-1$, $n=2$ there is only one configuration, so $D$ is trivially a function of the medium state at every $\lambda$.

### Step 9. Window: item 3(b)

**Record vectors and background.** Let $\lvert e_l\rangle$ ($l=1,\dots,L$) be the place of $c$ with only bit $l$ set. Then $\sigma_x^{[l]}\chi=\lvert e_l\rangle$ is orthonormal and orthogonal to $\chi$, so $\langle\sigma_x^{[l]}\rangle=0$. Let $w_i:=\{i,\dots,i+m-1\}\subseteq\{1,\dots,L\}$. Since $\lvert w_i\cap w_j\rvert=\max(m-\lvert i-j\rvert,0)$,

$$
\lvert u_{h_i}\rangle=\sum_{l\in w_i}\lvert e_l\rangle,\qquad
d_0(h_i,h_j)=\sqrt{\lvert w_i\triangle w_j\rvert}=\sqrt{2\min(\lvert i-j\rvert,m)},\qquad
D=\sqrt{2\min(\lvert i_1-i_2\rvert,m)} .
\tag{15.17}
$$

All $u_{h_i}$ are distinct, so every place is its own background point.

**Medium state.** $K_{h_{i_1}h_{i_2}}=\sum_l\nu_l\,\sigma_x^{[l]}$ with $\nu_l:=[l\in w_{i_1}]+[l\in w_{i_2}]\in\{0,1,2\}$. The terms commute and act on different bits, and $e^{-i\theta\sigma_x}=\cos\theta-i\sin\theta\,\sigma_x$, so

$$
\lvert E_{i_1i_2}(\lambda)\rangle=\bigotimes_{l=1}^{L}\bigl(\cos(\nu_l\lambda)\lvert0\rangle-i\sin(\nu_l\lambda)\lvert1\rangle\bigr),\qquad
\bigl\lvert\langle E_{i_1'i_2'}\vert E_{i_1i_2}\rangle\bigr\rvert=\prod_{l}\bigl\lvert\cos\bigl((\nu_l-\nu_l')\lambda\bigr)\bigr\rvert .
\tag{15.18}
$$

- **Every $\lambda$.** The overlap is $1$ for every $\lambda$ iff $\nu=\nu'$.
- **Leading order.** $s=\sum_l\nu_l\lvert e_l\rangle$, so the states agree iff $\nu=\nu'$.
- **$\nu$ fixes the configuration.** $\min(i_1,i_2)=\min\{l:\nu_l>0\}$, and $\nu-\mathbf 1_{w_{\min}}=\mathbf 1_{w_{\max}}$ then fixes $\max(i_1,i_2)$. Hence

$$
\text{same medium state (for every }\lambda\text{, or at leading order)}\iff\{i_1,i_2\}=\{i_1',i_2'\}.
\tag{15.19}
$$

**Answer.**
- **Leading-order state and orbit.** (15.14) holds for both families and all $n,m$, so the configuration and $D$ are functions of the leading-order medium state and of the orbit. Explicitly, $D^2=\#\{l:\nu_l=1\}=4m-\lVert s\rVert^2$. This follows from $\sum_l\nu_l=2m$ and $\lVert s\rVert^2=\#\{\nu_l=1\}+4\#\{\nu_l=2\}$.
- **Small $\lambda$.** In (15.21) one can take $\lambda_0=\pi/2$. If $\nu\neq\nu'$, some factor of (15.18) has $\lvert\nu_l-\nu_l'\rvert\in\{1,2\}$, and then $\lvert\cos((\nu_l-\nu_l')\lambda)\rvert<1$ for $0<\lvert\lambda\rvert<\pi/2$.
- **Revival.** At $\lambda=\pi$ every factor of (15.18) is $(-1)^{\nu_l}\lvert0\rangle$. Since $\sum_l\nu_l=2m$,
$$
\lvert E_{i_1i_2}(\pi)\rangle=(-1)^{\sum_l\nu_l}\lvert\chi\rangle=\lvert\chi\rangle\qquad\text{for every configuration}.
\tag{15.22}
$$
So $D$ is a function of $V_{\{c\}}(\pi)$ iff it is constant on the realizable configurations. That holds only for $c_T=-1$ with $n=2$ or $m=1$. For $c_T=+1$, $\{h_1,h_1\}$ and $\{h_1,h_2\}$ have $D=0$ and $D=\sqrt2$. For $c_T=-1$ with $n\ge3$ and $m\ge2$, $\{h_1,h_2\}$ and $\{h_1,h_3\}$ have $D=\sqrt2$ and $D=2$.

## Result

- **(S1).** The state is the exact product (15.3), and the body is localized at $[\beta]_0$ for every $\lambda$. The medium state is the same for every $\lambda$ iff (15.4), first line, holds: the cyclic condition (15.2), equivalently $W(\beta,\beta';\lambda)=1$ $\forall\lambda$. It is the same at leading order iff $[\beta]_0=[\beta']_0$ (15.4). The first condition implies the second, but not conversely.
- **(S2), state and views.** The state is the exact product (15.6): the pair stays localized at $\{[\beta_1]_0,[\beta_2]_0\}$ and is never correlated with the medium, and the medium state is pure. $D=\lVert u_{\beta_1}-u_{\beta_2}\rVert$ (15.7) is well defined: independent of labels, of the split (15.8) and of $\Delta$. The normalized witness geometries of the views, (15.9) and (15.10), do not depend on $D$. The full views give the place multiset through the occupation numbers (15.20), and hence, with the background, the configuration and $D$.
- **(S2), medium.** Same medium state at leading order iff $u_{\beta_1}+u_{\beta_2}=u_{\beta_1'}+u_{\beta_2'}$, that is, iff the two joint places are the same point of (12.13) ((15.11), (15.12)). The same for every $\lambda$ follows if (15.13) holds. $D$ is not in general a function of the medium state. The leading-order medium state distinguishes all configurations iff (15.14) holds. Then the orbit also distinguishes them, and so does $V_{\{c\}}(\lambda)$ for $0<\lvert\lambda\rvert<\lambda_0$ (15.21), but not necessarily at every $\lambda$. At a fixed $\lambda$, $D$ can be a function of $V_{\{c\}}(\lambda)$ even where the configuration is not. This happens when $D$ is constant on the configurations with the same $V_{\{c\}}(\lambda)$ (Step 7, item 3).
- **Line.** $d_0=\sigma_X\lvert i-j\rvert$ and $D=\sigma_X\lvert i_1-i_2\rvert$ (15.15). Same medium state iff the index sums are equal (15.16). $D$ is a function of the leading-order medium state, and of the orbit, only for $n=2$ ($c_T=+1$) or $n\le3$ ($c_T=-1$). In these cases it is also a function of $V_{\{c\}}(\lambda)$ for $0<\lvert\lambda\rvert<\lambda_0$ (15.21). For $c_T=-1$, $n=2$ there is a single configuration, so $D$ is a function of $V_{\{c\}}(\lambda)$ at every $\lambda$. For $c_T=+1$, $n=2$ and $c_T=-1$, $n=3$, $D$ is not constant on the configurations. So it is not a function of $V_{\{c\}}(0)=\lvert\chi\rangle\langle\chi\rvert$, and for $X=\sigma_x$, $\chi=\lvert0\rangle$ it is not one at the revival $\lambda=\pi$ either. In the other cases $D$ is a function at no $\lambda$.
- **Window.** $d_0=D=\sqrt{2\min(\lvert i-j\rvert,m)}$ (15.17). Same medium state iff same configuration (15.19). $D$ is a function of the leading-order medium state and of the orbit, with $D^2=4m-\lVert s\rVert^2$. It is also a function of $V_{\{c\}}(\lambda)$ for $0<\lvert\lambda\rvert<\pi/2$. At $\lambda=\pi$, as at $\lambda=0$, every configuration gives $\chi$ (15.22). There the configuration is determined only for $c_T=-1$, $n=2$ (a single configuration). $D$ is determined iff it is constant on the realizable configurations, that is, for $c_T=-1$ with $n=2$ or $m=1$.

## Consistency checks

1. **$\beta_1=\beta_2=\beta$, $c_T=+1$.** Here $\lvert\beta\beta\rangle_+=\lvert\beta\beta\rangle$, and (15.6) is (15.3) with $K_\beta\to2K_\beta-\Delta$. The view (15.9) reduces to the localized (S1) view, and $D=0$. Comparing $\{x,x\}$ with $\{x',x'\}$, (15.11) gives the rate $2d_0(x,x')$. This agrees with (15.4) for record vectors $2u$ and with (12.13) at $(h,h),(h',h')$.
2. **Split (12.6), and dimensions.** $C$, $K_{h_1h_2}$ and $E$ do not change. $u\to u+w$ leaves (15.7), the differences in (15.11), and (15.14) unchanged. $K$, $\Delta$ and $u$ carry the units of $C$, and $\lambda$ the inverse units, so $\lambda d_0$, $\lambda D$ and the right sides of (15.1) and (15.11) are dimensionless.
3. **Window with $m=1$.** Here $u_{h_i}=e_i$ are orthonormal, and (15.17) gives $d_0=\sqrt2$ for $i\neq j$, which equals $\lVert e_i-e_j\rVert$ directly. $\nu$ is the indicator of the multiset, so it fixes the configuration. $D^2=4-\lVert s\rVert^2$ gives $0$ for $\{i,i\}$ and $2$ for $\{i,j\}$.

## Open issues

- $D$ is defined through the background. For $c_T=-1$, whether the background is the geometry of a view is out of scope. The normalized witness geometries of the bodies' views (15.9), (15.10) do not contain $D$. $D$ follows from the place content of the views (15.20) together with the background. At leading order the medium records only the pair vector $s$ (the midpoint), not $D$ in general.
- Recoverability from the instantaneous medium state is shown only for $0<\lvert\lambda\rvert<\lambda_0$ (15.21). The full set of $\lambda$ at which revivals merge configurations is not characterized, except at $\lambda=\pi$ in the window (15.22).
- For (S2) the exact criterion is given only in operator form, (15.2) with $K_{\beta_1\beta_2}$. It is not reduced to record vectors.
- Localized starts never become correlated with the medium. Delocalized starts, motion, more bodies and several types are out of scope.

## Methods used

- Block-diagonal unitary evolution, functional calculus of self-adjoint operators
- Partial trace, witness weights, occupation numbers
- Second-order expansion of overlaps
- Cyclic subspaces, Cayley–Hamilton theorem, continuity of eigenvalues in a finite spectrum
- Symmetrized two-body states, relabelling covariance
- Translation invariance under the contract split
- Uniform small-$\lambda$ bound over finitely many starts, revivals of periodic orbits
- Elementary combinatorics of intervals (injectivity of sums, Sidon-type condition)
