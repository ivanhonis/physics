# Body in a recording medium: the probe's witness geometry

- **Subproject:** 03-ilang-space
- **Package:** 06-body-in-medium
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-08

## Setup and assumptions

**Notation for the imaginary unit.** Throughout, $\mathrm i$ is the imaginary unit. In Step 7, Latin $i,j$ are place indices of the probe.

**Model** (from question.md). Three objects: probe $p$, body $b$, medium $c$. They have pairwise different types and each is the only instance of its type, so (1.11) imposes no constraint. Order the factors as $\mathcal H=\mathcal H_p\otimes\mathcal H_b\otimes\mathcal H_c$, all finite-dimensional (A1). The part is $A=\{p\}$ and the companion is $\bar A=\{b,c\}$. The contract system is
$$C=\sum_h\lvert h\rangle\langle h\rvert_p\otimes\mathbb 1_b\otimes K_h+\sum_\beta\mathbb 1_p\otimes\lvert\beta\rangle\langle\beta\rvert_b\otimes B_\beta ,\qquad K_h=K_h^\dagger,\ B_\beta=B_\beta^\dagger\ \text{on }\mathcal H_c .$$
The initial state is $\lvert\Psi(0)\rangle=\lvert\phi\rangle_p\otimes\lvert\beta_0\rangle_b\otimes\lvert\chi\rangle_c$, with $\phi_h\neq0$ for all $h$ and $\lVert\chi\rVert=1$. Expectations are $\langle O\rangle:=\langle\chi\vert O\vert\chi\rangle$. For a pair of places $h,h'$ of $p$: $D:=K_h-K_{h'}$, $\tilde D:=D-\langle D\rangle$, and $\operatorname{Var}_\chi(D)=\langle\tilde D^2\rangle$.

**Inputs** (quoted in question.md): the decomposition (2.1), the view (2.2) and the witness data (2.11) from 02; the witness angle $\alpha=\arccos\sqrt W\in[0,\pi/2]$, which is a metric, (3.5) from 03; the body-free results (5.1), (5.6), (5.8), (5.9) and (5.10) from 05, with $d_0(h,h')=\lVert u_h-u_{h'}\rVert$ and $d_0^2=\operatorname{Var}_\chi(D)$.

**Assumptions.** The contracts do not depend on $\lambda$ (A5), and $\lambda\ge0$. Items 1 and 2 are exact for every $\lambda$. Items 3 and 4 are Taylor expansions at $\lambda\to0^+$. Because $\mathcal H_c$ is finite-dimensional, every overlap below is an entire function of $\lambda$, so the remainders are $O(\lambda^4)$ (or $O(\lambda^3)$) at fixed operators. The expansions are quantitatively useful for $\lambda\bigl(\lVert K_h+B_{\beta_0}\rVert+\lVert K_{h'}+B_{\beta_0}\rVert\bigr)\ll1$.

**Standard facts used (F).** For self-adjoint $O_1,O_2$ on $\mathcal H_c$: $\langle O_1\rangle\in\mathbb R$; $\langle O_1O_2\rangle^*=\langle O_2O_1\rangle$, hence $\operatorname{Im}\langle O_1O_2\rangle=\langle[O_1,O_2]\rangle/(2\mathrm i)$, $\langle[O_1,O_2]\rangle\in\mathrm i\mathbb R$, and $\operatorname{Im}\langle O_1O_2O_1\rangle=0$.

## Derivation

### Step 1. Block form of the contract system and exact evolution

Insert $\mathbb 1_b=\sum_\beta\lvert\beta\rangle\langle\beta\rvert$ into the first sum of $C$ and $\mathbb 1_p=\sum_h\lvert h\rangle\langle h\rvert$ into the second (place bases are orthonormal and complete, A2):
$$
C=\sum_{h,\beta}\Pi_{h\beta}\otimes\bigl(K_h+B_\beta\bigr),\qquad \Pi_{h\beta}:=\lvert h\rangle\langle h\rvert_p\otimes\lvert\beta\rangle\langle\beta\rvert_b .
\tag{6.1}
$$
The $\Pi_{h\beta}$ are mutually orthogonal projectors, $\Pi_{h\beta}\Pi_{k\gamma}=\delta_{hk}\delta_{\beta\gamma}\Pi_{h\beta}$, with $\sum_{h,\beta}\Pi_{h\beta}=\mathbb 1_p\otimes\mathbb 1_b$. By induction, $C^n=\sum_{h,\beta}\Pi_{h\beta}\otimes(K_h+B_\beta)^n$ for every $n\ge0$. Summing the exponential series gives
$$
e^{-\mathrm iC\lambda}=\sum_{h,\beta}\Pi_{h\beta}\otimes e^{-\mathrm i(K_h+B_\beta)\lambda}.
\tag{6.2}
$$
The two contracts need not commute: their commutator is $\sum_{h,\beta}\Pi_{h\beta}\otimes[K_h,B_\beta]$. Even so, (6.2) is exact, because both contracts are diagonal in the places of $p$ and $b$. For $B_\beta=0$, (6.2) reduces to (5.1). Applying (6.2) to $\lvert\Psi(0)\rangle$ with $\Pi_{h\beta}(\lvert\phi\rangle\otimes\lvert\beta_0\rangle)=\phi_h\delta_{\beta\beta_0}\lvert h\rangle\otimes\lvert\beta_0\rangle$ gives
$$
\lvert\Psi(\lambda)\rangle=\sum_h\phi_h\,\lvert h\rangle_p\otimes\lvert\beta_0\rangle_b\otimes e^{-\mathrm i(K_h+B_{\beta_0})\lambda}\lvert\chi\rangle_c .
\tag{6.3}
$$

### Step 2. The body stays at $\beta_0$; the probe's weights and witness data

*Body.* By (6.3), $\bigl(\mathbb 1_p\otimes\langle\beta\rvert_b\otimes\mathbb 1_c\bigr)\lvert\Psi(\lambda)\rangle=0$ for every $\beta\neq\beta_0$, and $\lvert\Psi(\lambda)\rangle=\lvert\beta_0\rangle_b\otimes\lvert\Phi(\lambda)\rangle_{pc}$ is a product in $b$ versus $\{p,c\}$. Hence the view of $b$ (1.5) and the probabilities (1.3) of the local reading of $b$ with classes $\{\beta\}$ (A4) are
$$
V_{\{b\}}(\Psi(\lambda))=\lvert\beta_0\rangle\langle\beta_0\rvert ,\qquad p_b(\beta)=\delta_{\beta\beta_0}\qquad\text{for every }\lambda .
\tag{6.4}
$$
The body stays at the single place $\beta_0$ and never becomes correlated with $p$ or $c$.

*Probe weights.* By (2.1) and (6.3), $\lvert\psi_h\rangle=\phi_h\,\lvert\beta_0\rangle\otimes e^{-\mathrm i(K_h+B_{\beta_0})\lambda}\lvert\chi\rangle$. The exponential is unitary, so $p_h=\lVert\psi_h\rVert^2=\lvert\phi_h\rvert^2$ (2.2). This does not depend on $\lambda$, and $H_V$ contains every place of $p$, because $\phi_h\neq0$.

*Witness data.* By (2.2), using $\langle\beta_0\vert\beta_0\rangle=1$ and $(e^{-\mathrm iM\lambda})^\dagger=e^{\mathrm iM\lambda}$ for self-adjoint $M$,
$$
(V_A)_{hh'}=\phi_h\phi_{h'}^*\,G^{(\beta_0)}_{hh'}(\lambda),\qquad
G^{(\beta_0)}_{hh'}(\lambda):=\langle\chi\vert e^{\mathrm i(K_{h'}+B_{\beta_0})\lambda}e^{-\mathrm i(K_h+B_{\beta_0})\lambda}\vert\chi\rangle .
\tag{6.5}
$$
This is $G_{hh'}=\langle E_{h'}\vert E_h\rangle$ of 02, with $a_h=\phi_h$ and $\lvert E_h\rangle=\lvert\beta_0\rangle\otimes e^{-\mathrm i(K_h+B_{\beta_0})\lambda}\lvert\chi\rangle$. Then (2.11) gives
$$
W^{(\beta_0)}(h,h';\lambda)=\frac{\lvert(V_A)_{hh'}\rvert^2}{p_hp_{h'}}=\bigl\lvert\langle\chi\vert e^{\mathrm i(K_{h'}+B_{\beta_0})\lambda}e^{-\mathrm i(K_h+B_{\beta_0})\lambda}\vert\chi\rangle\bigr\rvert^2 .
\tag{6.6}
$$
$W^{(\beta_0)}$ is a modulus, so it does not depend on the common phase or on the phase split between $a_h$ and $\lvert E_h\rangle$ (M6). For $B_{\beta_0}=0$, (6.6) is (5.6). Since $G^{(\beta_0)}_{h'h}=\bigl(G^{(\beta_0)}_{hh'}\bigr)^*$, $W^{(\beta_0)}$ is symmetric in $h,h'$.

### Step 3. Commuting records (item 2)

Let $[B_{\beta_0},K_h]=[B_{\beta_0},K_{h'}]=0$. The exponential of a sum of commuting operators factorizes, so $e^{-\mathrm i(K_h+B_{\beta_0})\lambda}=e^{-\mathrm iB_{\beta_0}\lambda}e^{-\mathrm iK_h\lambda}$ and $e^{\mathrm i(K_{h'}+B_{\beta_0})\lambda}=e^{\mathrm iK_{h'}\lambda}e^{\mathrm iB_{\beta_0}\lambda}$. In the product the factors $e^{\pm\mathrm iB_{\beta_0}\lambda}$ cancel, so the overlap itself (not only its modulus) is body-independent:
$$
G^{(\beta_0)}_{hh'}(\lambda)=\langle\chi\vert e^{\mathrm iK_{h'}\lambda}e^{-\mathrm iK_h\lambda}\vert\chi\rangle,\qquad
W^{(\beta_0)}(h,h';\lambda)=W(h,h';\lambda)\ \text{of (5.6)}\quad\text{for every }\lambda\ge0 .
\tag{6.7}
$$
A multiple of the identity, $B_{\beta_0}=b\,\mathbb 1$, commutes with everything, so such a body has no effect.

### Step 4. Expansion of the overlap

Write $M:=K_h+B_{\beta_0}$ and $M':=K_{h'}+B_{\beta_0}$, so that $M-M'=D$, and let $G:=G^{(\beta_0)}_{hh'}(\lambda)$. Expand $e^{\mathrm iM'\lambda}=1+\mathrm iM'\lambda-\tfrac12M'^2\lambda^2-\tfrac{\mathrm i}6M'^3\lambda^3+O(\lambda^4)$ and $e^{-\mathrm iM\lambda}=1-\mathrm iM\lambda-\tfrac12M^2\lambda^2+\tfrac{\mathrm i}6M^3\lambda^3+O(\lambda^4)$, multiply, and collect the orders:
$$
\begin{aligned}
\lambda^2:&\quad -\tfrac12M^2+M'M-\tfrac12M'^2=-\tfrac12\bigl(D^2+[M,M']\bigr),\\
\lambda^3:&\quad \tfrac{\mathrm i}6\bigl(M^3-3M'M^2+3M'^2M-M'^3\bigr),
\end{aligned}
$$
where $D^2=M^2-MM'-M'M+M'^2$ was used. Taking expectations gives $G=1+g_1\lambda+g_2\lambda^2+g_3\lambda^3+O(\lambda^4)$ with
$$
g_1=-\mathrm i\langle D\rangle,\qquad g_2=-\tfrac12\bigl(\langle D^2\rangle+\langle[M,M']\rangle\bigr),\qquad g_3=\tfrac{\mathrm i}6\bigl\langle M^3-3M'M^2+3M'^2M-M'^3\bigr\rangle .
\tag{6.8}
$$

### Step 5. $W^{(\beta_0)}$ to third order and the coefficient $c_3^{(\beta_0)}$

With $\varepsilon:=G-1$, $W^{(\beta_0)}=\lvert G\rvert^2=1+2\operatorname{Re}\varepsilon+\lvert\varepsilon\rvert^2$. Order by order, using (F):

1. $\lambda^1$: $2\operatorname{Re}g_1=0$, since $\langle D\rangle\in\mathbb R$.
2. $\lambda^2$: $\lvert g_1\rvert^2+2\operatorname{Re}g_2=\langle D\rangle^2-\langle D^2\rangle=-\operatorname{Var}_\chi(D)$, because $\langle[M,M']\rangle$ is imaginary. $D=K_h-K_{h'}$ does not contain $B_{\beta_0}$, and $B_{\beta_0}$ enters $g_2$ only through the imaginary $\langle[M,M']\rangle$. The second-order term is therefore body-independent.
3. $\lambda^3$: $c_3=2\operatorname{Re}g_3+2\operatorname{Re}(g_1g_2^*)$. Since $\operatorname{Im}\langle M^3\rangle=\operatorname{Im}\langle M'^3\rangle=0$, $2\operatorname{Re}g_3=-\tfrac13\operatorname{Im}\langle\cdots\rangle=\operatorname{Im}\langle M'M^2\rangle-\operatorname{Im}\langle M'^2M\rangle$. With $\langle[M,M']\rangle=2\mathrm i\operatorname{Im}\langle MM'\rangle$, $g_1g_2^*=\tfrac{\mathrm i}2\langle D\rangle\bigl(\langle D^2\rangle-2\mathrm i\operatorname{Im}\langle MM'\rangle\bigr)$, so $2\operatorname{Re}(g_1g_2^*)=2\langle D\rangle\operatorname{Im}\langle MM'\rangle$. Hence
   $$c_3=\operatorname{Im}\langle M'M^2\rangle-\operatorname{Im}\langle M'^2M\rangle+2\langle D\rangle\operatorname{Im}\langle MM'\rangle .$$
4. Simplification. Insert $M=M'+D$. Using $\operatorname{Im}\langle M'^3\rangle=\operatorname{Im}\langle M'DM'\rangle=\operatorname{Im}\langle M'^2\rangle=0$: $\operatorname{Im}\langle M'M^2\rangle=\operatorname{Im}\langle M'^2D\rangle+\operatorname{Im}\langle M'D^2\rangle$, $\operatorname{Im}\langle M'^2M\rangle=\operatorname{Im}\langle M'^2D\rangle$, and $\operatorname{Im}\langle MM'\rangle=\operatorname{Im}\langle DM'\rangle$. So $c_3=\operatorname{Im}\langle M'D^2\rangle+2\langle D\rangle\operatorname{Im}\langle DM'\rangle$. Now insert $D=\tilde D+\langle D\rangle$. Then $\operatorname{Im}\langle M'D^2\rangle=\operatorname{Im}\langle M'\tilde D^2\rangle+2\langle D\rangle\operatorname{Im}\langle M'\tilde D\rangle$ and $\operatorname{Im}\langle DM'\rangle=\operatorname{Im}\langle\tilde DM'\rangle=-\operatorname{Im}\langle M'\tilde D\rangle$. The cross terms cancel.

Result:
$$
W^{(\beta_0)}(h,h';\lambda)=1-\lambda^2\operatorname{Var}_\chi(D)+\lambda^3c_3^{(\beta_0)}(h,h')+O(\lambda^4),
\tag{6.9}
$$
$$
c_3^{(\beta_0)}(h,h')=\operatorname{Im}\langle\chi\vert\,(K_{h'}+B_{\beta_0})\,\tilde D^2\vert\chi\rangle ,
\tag{6.10}
$$
$$
c_3^{(\beta_0)}=c_3^{(0)}+\operatorname{Im}\langle\chi\vert B_{\beta_0}\tilde D^2\vert\chi\rangle,\qquad
c_3^{(0)}(h,h')=\operatorname{Im}\langle\chi\vert K_{h'}\tilde D^2\vert\chi\rangle,\qquad
\operatorname{Im}\langle\chi\vert B_{\beta_0}\tilde D^2\vert\chi\rangle=\frac{\langle\chi\vert[B_{\beta_0},\tilde D^2]\vert\chi\rangle}{2\mathrm i}.
\tag{6.11}
$$
Here $c_3^{(0)}$ is the third-order coefficient of the body-free data (5.6). Since $K_h=K_{h'}+D$ and $\operatorname{Im}\langle D\tilde D^2\rangle=\operatorname{Im}\langle\tilde D^3\rangle+\langle D\rangle\operatorname{Im}\langle\tilde D^2\rangle=0$, $K_{h'}$ can be replaced by $K_h$ in (6.10) and (6.11). So $c_3^{(\beta_0)}$ is symmetric in $h,h'$, as (6.6) requires.

### Step 6. Witness angle to second order

By (3.5), $\cos\alpha=\sqrt W$ with $\alpha\in[0,\pi/2]$. Hence $\sin\alpha=\sqrt{1-W}$, and $\alpha=\arcsin\sqrt{1-W}$, because $\arcsin:[0,1]\to[0,\pi/2]$ inverts $\sin$ on $[0,\pi/2]$. Let $d_0>0$, where $d_0^2=\operatorname{Var}_\chi(D)$ by (5.9)–(5.10). By (6.9), $1-W=\lambda^2d_0^2\bigl(1-\lambda c_3/d_0^2+O(\lambda^2)\bigr)$, so for $\lambda>0$, $\sqrt{1-W}=\lambda d_0\bigl(1-\lambda c_3/(2d_0^2)+O(\lambda^2)\bigr)$. With $\arcsin x=x+O(x^3)$,
$$
\alpha^{(\beta_0)}(h,h';\lambda)=\lambda d_0(h,h')+\lambda^2\alpha_2^{(\beta_0)}(h,h')+O(\lambda^3),\qquad
\alpha_2^{(\beta_0)}=-\frac{c_3^{(\beta_0)}}{2d_0},
\tag{6.12}
$$
$$
\alpha_2^{(\beta_0)}=\alpha_2^{(0)}-\frac{\operatorname{Im}\langle\chi\vert B_{\beta_0}\tilde D^2\vert\chi\rangle}{2d_0},\qquad
\alpha_2^{(0)}=-\frac{\operatorname{Im}\langle\chi\vert K_{h'}\tilde D^2\vert\chi\rangle}{2d_0}.
\tag{6.13}
$$
The leading distance $\lambda d_0$ is body-independent. The body first acts at order $\lambda^2$.

### Step 7. Qubit example

Pauli facts: $\sigma_a^2=\mathbb 1$, $\sigma_x\sigma_z=-\sigma_z\sigma_x$, $\sigma_y\sigma_x=-\mathrm i\sigma_z$, $\sigma_y\sigma_z=\mathrm i\sigma_x$. In $\lvert0\rangle$: $\langle\sigma_x\rangle=\langle\sigma_y\rangle=0$ and $\langle\sigma_z\rangle=1$. Hence $X^2=2\,\mathbb 1$, $\langle X\rangle=1$, $\sigma_yX=\mathrm i(\sigma_x-\sigma_z)$ and $\langle\sigma_yX\rangle=-\mathrm i$.

For the pair $(h_i,h_j)$: $D=(i-j)X$, $\langle D\rangle=i-j$, $\tilde D=(i-j)(X-\mathbb 1)$, and $\tilde D^2=(i-j)^2(X^2-2X+\mathbb 1)=(i-j)^2(3\,\mathbb 1-2X)$. Then:

1. $\operatorname{Var}_\chi(D)=(i-j)^2(3-2\langle X\rangle)=(i-j)^2$ and $d_0(h_i,h_j)=\lvert i-j\rvert$.
2. $c_3^{(0)}=\operatorname{Im}\langle jX\,\tilde D^2\rangle=j(i-j)^2\operatorname{Im}\langle3X-2X^2\rangle=j(i-j)^2\operatorname{Im}(3-4)=0$.
3. Body part: $\operatorname{Im}\langle\beta_0\sigma_y\tilde D^2\rangle=\beta_0(i-j)^2\operatorname{Im}\bigl(3\langle\sigma_y\rangle-2\langle\sigma_yX\rangle\bigr)=\beta_0(i-j)^2\operatorname{Im}(2\mathrm i)=2\beta_0(i-j)^2$.

Item 2 does not apply here, because $[\sigma_y,X]=2\mathrm i(\sigma_x-\sigma_z)\neq0$. By (6.9)–(6.13),
$$
c_3^{(\beta_0)}(h_i,h_j)=2\beta_0(i-j)^2,\qquad
W^{(\beta_0)}(h_i,h_j;\lambda)=1-(i-j)^2\lambda^2+2\beta_0(i-j)^2\lambda^3+O(\lambda^4),
\tag{6.14}
$$
$$
\alpha_2^{(\beta_0)}(h_i,h_j)=-\beta_0\lvert i-j\rvert,\qquad
\alpha^{(\beta_0)}(h_i,h_j;\lambda)=\lambda\lvert i-j\rvert\,(1-\beta_0\lambda)+O(\lambda^3).
\tag{6.15}
$$
For $i=j$, $M=M'$ gives $G=1$ and $\alpha=0$ exactly, in agreement with (6.15). The expansion is controlled for $\lambda\sqrt{2n^2+\beta_0^2}\ll1$, since $\lVert K_{h_i}+\beta_0\sigma_y\rVert=\sqrt{2i^2+\beta_0^2}$.

*Dependence on the body's place.* To order $\lambda^2$, the probe sees $h_1,\dots,h_n$ as an equally spaced chain, $\alpha\propto\lvert i-j\rvert$, as without the body. The body's place $\beta_0$ enters only through one common factor $1-\beta_0\lambda$ that multiplies every probe distance. Ratios of distances are therefore unchanged to this order. A body at $\beta_0>0$ contracts the probe's distances, a body at $\beta_0<0$ dilates them, and $\beta_0=0$ gives the body-free distances. The effect is linear in $\beta_0$ and is one power of $\lambda$ below the leading distance. Two places $\beta_0\neq\beta_0'$ give probe distances that differ by $(\beta_0'-\beta_0)\lambda^2\lvert i-j\rvert+O(\lambda^3)$.

### Step 8. Contrast: $B_\beta=\beta X$

$[\beta X,iX]=0$ for all $i$, so (6.7) holds for every $\beta_0$ and every $\lambda$. Exactly, $e^{\mathrm ijX\lambda}e^{-\mathrm iiX\lambda}=e^{-\mathrm i\theta\,n\cdot\sigma}=\cos\theta\,\mathbb 1-\mathrm i\sin\theta\,n\cdot\sigma$, with $X=\sqrt2\,n\cdot\sigma$, $n=(1,0,1)/\sqrt2$, $\theta=\sqrt2(i-j)\lambda$ and $\langle n\cdot\sigma\rangle=1/\sqrt2$. Hence
$$
W^{(\beta_0)}(h_i,h_j;\lambda)=\cos^2\theta+\tfrac12\sin^2\theta=1-\tfrac12\sin^2\!\bigl(\sqrt2(i-j)\lambda\bigr)\qquad\text{for every }\beta_0 .
\tag{6.16}
$$
Its expansion, $1-(i-j)^2\lambda^2+O(\lambda^4)$, agrees with (6.14) at $\beta_0=0$.

## Result

- **Item 1.** The exact state is (6.3), obtained from the block form (6.1)–(6.2). The body stays at $\beta_0$ for every $\lambda$ (6.4). The probe weights are $p_h=\lvert\phi_h\rvert^2$, independent of $\lambda$. The witness data are (6.6), which reduce to (5.6) for $B_{\beta_0}=0$.
- **Item 2.** If $B_{\beta_0}$ commutes with $K_h$ and $K_{h'}$, the overlap and $W$ are exactly body-free (6.7). In particular, $B_{\beta_0}\propto\mathbb 1$ has no effect.
- **Item 3.** $W^{(\beta_0)}=1-\lambda^2\operatorname{Var}_\chi(D)+\lambda^3c_3^{(\beta_0)}+O(\lambda^4)$ (6.9), with a body-free $\lambda^2$ term. $c_3^{(\beta_0)}=\operatorname{Im}\langle(K_{h'}+B_{\beta_0})\tilde D^2\rangle$ (6.10), and its body part is $\operatorname{Im}\langle B_{\beta_0}\tilde D^2\rangle$ (6.11). $\alpha^{(\beta_0)}=\lambda d_0+\lambda^2\alpha_2^{(\beta_0)}+O(\lambda^3)$ with $\alpha_2^{(\beta_0)}=-c_3^{(\beta_0)}/(2d_0)$ (6.12)–(6.13). Both agree with the expectation in question.md.
- **Item 4.** $c_3^{(\beta_0)}=2\beta_0(i-j)^2$ (6.14) and $\alpha^{(\beta_0)}=\lambda\lvert i-j\rvert(1-\beta_0\lambda)+O(\lambda^3)$ (6.15): a common rescaling of all probe distances by $1-\beta_0\lambda$. For $B_\beta=\beta X$ there is no effect for any $\lambda$ (6.16). All of this agrees with the expectation in question.md.

## Consistency checks

1. **$B_{\beta_0}=0$.** (6.6) becomes (5.6). The $\lambda^2$ coefficient of (6.9) is $-\operatorname{Var}_\chi(K_h-K_{h'})$, as in (5.8)–(5.9). The leading term of (6.12) gives $\alpha/\lambda\to d_0$, as in (5.10).
2. **$B_{\beta_0}=\beta_0\mathbb 1$.** Exactly, (6.7) gives no effect. At third order, (6.11) agrees independently: $\operatorname{Im}\langle\beta_0\tilde D^2\rangle=\beta_0\operatorname{Im}\langle\tilde D^2\rangle=0$, because $\tilde D^2$ is self-adjoint.
3. **Example with $B_\beta=\beta X$.** The body part of (6.11) is $\beta_0(i-j)^2\operatorname{Im}\langle3X-2X^2\rangle=0$, consistent with the exact statement (6.16) from item 2.

## Open issues

- In general, $c_3^{(0)}=\operatorname{Im}\langle K_{h'}\tilde D^2\rangle\neq0$, so the body-free angle already has a $\lambda^2$ term. In the qubit example it vanishes, and so there $c_3^{(\beta_0)}$ consists only of the body part.
- The condition of item 2 is sufficient for exact body-independence, not necessary. At order $\lambda^3$, the body term vanishes already when $\langle[B_{\beta_0},\tilde D^2]\rangle=0$. Necessary conditions were not studied.
- In the example, it is not determined whether the uniform rescaling of the distances persists beyond order $\lambda^2$. Large $\lambda$, bodies in superposition, the dependence on a probe–body distance and the relation to the cost $L$ are out of scope.

## Methods used

- Spectral block decomposition of the contract operator by orthogonal place projectors
- Exponential series of block-diagonal operators; factorization of exponentials of commuting operators
- Partial trace / witness rule (2.1), (2.2), (2.11)
- Taylor expansion of operator exponentials to third order
- Reality and imaginarity of expectations of products of self-adjoint operators
- Inversion of $\arccos\sqrt{W}$ via $\arcsin$ series
- Pauli-matrix algebra
