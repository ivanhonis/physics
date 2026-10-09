# Dimension of the witness geometry for several recording channels

- **Subproject:** 03-ilang-space
- **Package:** 14-dimension
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-08

## Changes from previous version

- Step 5.4, the sentence after (14.12): the attainment condition for the value $`\min(n-1,d_c-1)`$ is corrected. v1 required $`r_\chi=d_c`$. The correct condition is $`r_\chi\ge\min(n,d_c)`$, together with the full-rank condition. Full spectral support ($`r_\chi=d_c`$, all joint eigenspaces one-dimensional) is necessary only when $`n\ge d_c`$ (issue I1 of `verification.md`).
- Nothing else changed. All steps, equations and tags are as in v1. Step 6 uses (14.12) only with full support ($`p_j>0`$ for all $`j`$), where the old and the corrected conditions agree, so (14.13)–(14.16) are unaffected.

## Response to verification

- **I1:** Accepted and fixed in Step 5.4. Since $`r_\chi\le J\le d_c`$, we have $`\min(n,r_\chi)=\min(n,d_c)`$ iff $`r_\chi\ge\min(n,d_c)`$. For $`n<d_c`$ this does not force $`r_\chi=d_c`$. The counterexample ($`n=4`$, $`d_c=5`$, $`K_h=\lvert e_h\rangle\langle e_h\rvert`$, $`\chi_c=\frac12(e_1+\cdots+e_4)`$, $`r_\chi=4`$, $`\dim^{(c)}_0=3`$) is correct.

## Setup and assumptions

**Model (question.md).** A recorded object $`a`$ with places $`h\in H`$, $`\lvert H\rvert=n`$. Medium cells $`c=1,\dots,m`$, with $`d_c=\dim\mathcal H_c`$. All types are pairwise different, with one instance each. The initial state is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\lvert\chi\rangle=\bigotimes_c\lvert\chi_c\rangle`$ and $`\phi_h\neq0`$ for all $`h`$. The contracts are $`C=\sum_c\sum_h\lvert h\rangle\langle h\rvert\otimes K^{(c)}_h`$ with $`K^{(c)}_h`$ self-adjoint on cell $`c`$. The record vector of channel $`c`$ is $`u^{(c)}_h=(K^{(c)}_h-\langle K^{(c)}_h\rangle_c)\lvert\chi_c\rangle`$, where $`\langle X\rangle_c:=\langle\chi_c\vert X\vert\chi_c\rangle`$, and $`\dim^{(c)}_0:=\dim_{\mathbb R}\mathrm{aff}_{\mathbb R}\{u^{(c)}_h\}`$.

**Quoted inputs.**
- From 05 (setting: one recorded object, one medium object with space $`\mathcal H_c`$, contract $`\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, start $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$):
  - $`g(v,w)=\mathrm{Re}\langle v\vert w\rangle`$;
  - $`h\sim_0h'`$ iff $`u_h=u_{h'}`$;
  - $`\dim_0=\dim_{\mathbb R}\mathrm{aff}_{\mathbb R}\{u_h\}`$;
  - (5.10) $`\lim_{\lambda\to0^+}\alpha(h,h';\lambda)/\lambda=d_0(h,h')=\lVert u_h-u_{h'}\rVert`$, with $`\lvert u_h\rangle=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$;
  - (5.11) $`(H_V/{\sim_0},d_0)\cong(\{u_h\},\lVert\cdot\rVert)\subset(\mathcal H_c,g)`$;
  - (5.13) $`\langle\chi\vert u_h\rangle=0`$;
  - (5.14) $`\dim_0\le\min(d_{T(a)}-1,\,2d_c-2)`$.
- From 07 ($`K_h`$ i.i.d. in a basis $`e_1=\lvert\chi\rangle,e_2,\dots,e_{d_c}`$): (7.7) GUE gives $`\dim_0=\min(n-1,2(d_c-1))`$ a.s.; (7.11) GOE gives $`\dim_0=\min(n-1,d_c-1)`$ a.s.
- From 10:
  - $`\omega(v,w)=\mathrm{Im}\langle v\vert w\rangle`$, $`Jv=\mathrm iv`$, $`\Phi=\arg W`$;
  - (10.8) $`\Phi(h_1,\dots,h_k;\lambda)=-\lambda^2\sum_{j=1}^k\omega(u_{h_j},u_{h_{j+1}})+O(\lambda^3)`$ for $`k\ge3`$, with $`h_{k+1}:=h_1`$;
  - (10.12) $`\omega(v,w)=g(Jv,w)`$, $`g(Jv,Jw)=g(v,w)`$, $`J^2=-\mathbb 1`$.

**Assumptions.**
- **S1.** Every statement is of leading order at $`\lambda\to0^+`$. The contracts do not depend on $`\lambda`$ (A5).
- **S2 (genericity, item 3).** The records of different channels are drawn independently. Each channel's records are drawn from an absolutely continuous law on the parameter space of its class:
  - complex generic: Hermitian $`K^{(c)}_h`$, as in 07;
  - real: real symmetric $`K^{(c)}_h`$ in a real orthonormal basis $`e_1=\lvert\chi_c\rangle,e_2,\dots,e_{d_c}`$, as in 07;
  - commuting: $`K^{(c)}_h=\sum_{j=1}^{d_c}\kappa_h(j)\lvert e_j\rangle\langle e_j\rvert`$ in a fixed orthonormal basis $`\{e_j\}`$ of $`\mathcal H_c`$, with real $`\kappa_h(j)`$ drawn and $`\langle e_j\vert\chi_c\rangle\neq0`$ for all $`j`$. This is my reading of "generically within the commuting class".
- **Notation.**
  - $`\mathrm i`$ is the imaginary unit;
  - $`\mathcal H_M:=\bigotimes_c\mathcal H_c`$ and $`D:=\prod_cd_c`$;
  - $`V:=\{t\in\mathbb R^H:\sum_ht_h=0\}`$, with $`\dim V=n-1`$ and the product $`t\cdot s=\sum_ht_hs_h`$;
  - $`d^{(c)}_0(h,h'):=\lVert u^{(c)}_h-u^{(c)}_{h'}\rVert`$.

## Derivation

### Step 1. Reduction to the setting of 05

1. The $`\lvert h\rangle\langle h\rvert`$ are orthogonal projectors. For $`c\neq c'`$, $`K^{(c)}_h`$ and $`K^{(c')}_h`$ act on different tensor factors and therefore commute. Hence $`e^{-\mathrm iC\lambda}=\sum_h\lvert h\rangle\langle h\rvert\otimes\bigotimes_ce^{-\mathrm iK^{(c)}_h\lambda}`$, and
```math
C=\sum_h\lvert h\rangle\langle h\rvert\otimes K_h,\quad K_h:=\sum_{c=1}^mK^{(c)}_h,\qquad
\lvert\Psi(\lambda)\rangle=\sum_h\phi_h\lvert h\rangle\otimes\bigotimes_{c}e^{-\mathrm iK^{(c)}_h\lambda}\lvert\chi_c\rangle .
\tag{14.1}
```
2. **Carry-over.** (14.1) is the setting of 05, with the medium object replaced by the part $`M=\{c_1,\dots,c_m\}=\bar a`$. The contract is a recording contract with self-adjoint $`K_h`$ on $`\mathcal H_M`$, and the start is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\lvert\chi\rangle`$ a unit vector of $`\mathcal H_M`$. The rules from which the quantities of 05 and 10 are built do not distinguish a one-object medium from a several-object one:
   - the view (1.5)–(1.7) is defined for every part (A7) and depends on the companion only through $`\mathcal H_{\bar a}`$, its inner product and the branch states;
   - the evolution is (14.1);
   - (1.11) imposes nothing, because each type has one instance.

   The quoted right-hand sides likewise involve the medium only through $`(\mathcal H_c,\langle\cdot\vert\cdot\rangle)`$, $`\lvert\chi\rangle`$ and $`K_h`$. Hence (5.10), (5.11), (5.13), (5.14), (10.8) and (10.12) hold for the whole medium after the replacements $`\mathcal H_c\to\mathcal H_M`$, $`d_c\to D`$, $`K_h\to\sum_cK^{(c)}_h`$ and $`\lvert\chi\rangle\to\bigotimes_c\lvert\chi_c\rangle`$. Applied to channel $`c`$ alone (the setting of 05 with medium $`c`$), they give $`u^{(c)}_h`$, $`d^{(c)}_0`$ and $`\dim^{(c)}_0`$. In particular $`\langle\chi_c\vert u^{(c)}_h\rangle=0`$ by (5.13).

### Step 2. Record vectors and distance (item 1a)

Let $`\iota_c:\mathcal H_c\to\mathcal H_M`$ be the map $`\iota_c(v):=\lvert\chi_1\rangle\otimes\cdots\otimes\lvert\chi_{c-1}\rangle\otimes v\otimes\lvert\chi_{c+1}\rangle\otimes\cdots\otimes\lvert\chi_m\rangle`$. It is a complex-linear isometry. Since the $`\lvert\chi_{c'}\rangle`$ are unit vectors, $`K^{(c)}_h\lvert\chi\rangle=\iota_c(K^{(c)}_h\lvert\chi_c\rangle)`$, $`\langle\chi\vert K^{(c)}_h\vert\chi\rangle=\langle K^{(c)}_h\rangle_c`$ and $`\lvert\chi\rangle=\iota_c\lvert\chi_c\rangle`$. Inserting $`K_h`$ of (14.1) into (5.10) gives
```math
u_h=\sum_{c=1}^m\iota_c\bigl(u^{(c)}_h\bigr).
\tag{14.2}
```
For $`c\neq c'`$, $`\langle\iota_cv\vert\iota_{c'}w\rangle=\langle v\vert\chi_c\rangle\langle\chi_{c'}\vert w\rangle`$, which vanishes for $`v=u^{(c)}_h`$ by (5.13). The channel images are therefore mutually orthogonal, and
```math
\langle u_h\vert u_{h'}\rangle=\sum_c\langle u^{(c)}_h\vert u^{(c)}_{h'}\rangle,
\qquad
d_0(h,h')=\Bigl(\sum_{c=1}^m d^{(c)}_0(h,h')^2\Bigr)^{1/2}.
\tag{14.3}
```
Thus $`h\sim_0h'`$ iff $`u^{(c)}_h=u^{(c)}_{h'}`$ for every $`c`$. By (5.11), $`(H_V/{\sim_0},d_0)`$ is isometric to the set of tuples $`(u^{(1)}_h,\dots,u^{(m)}_h)`$ in the orthogonal direct sum $`\bigoplus_c\chi_c^{\perp}`$, because $`\sum_c\iota_c`$ maps this direct sum isometrically into $`\mathcal H_M`$.

### Step 3. Dimension, sum condition and general relation (items 1a–c)

1. For a family $`\{v_h\}`$ in a real vector space, the direction space of $`\mathrm{aff}_{\mathbb R}\{v_h\}`$ is $`\{\sum_ht_hv_h:t\in V\}`$. Define the real-linear maps $`A_c:V\to\mathcal H_c`$, $`A_ct:=\sum_ht_hu^{(c)}_h`$, and $`A:V\to\mathcal H_M`$, $`At:=\sum_ht_hu_h=\sum_c\iota_c(A_ct)`$. Then $`\dim^{(c)}_0=\mathrm{rank}A_c`$ and $`\dim_0=\mathrm{rank}A`$.
2. By (14.3), $`\lVert At\rVert^2=\sum_c\lVert A_ct\rVert^2`$, so $`\ker A=\bigcap_c\ker A_c`$.
3. **Read-out spaces.** For $`w\in\mathcal H_c`$ let $`f^{(c)}_w(h):=g(w,u^{(c)}_h)`$, a real function on $`H`$, and let $`\mathring f:=f-\frac1n\sum_{h}f(h)\in V`$ denote the centred version of a function $`f`$. For $`t\in V`$ we have $`g(w,A_ct)=t\cdot f^{(c)}_w=t\cdot\mathring f^{(c)}_w`$. Since $`g`$ is nondegenerate, $`t\in\ker A_c`$ iff $`t\perp\mathring f^{(c)}_w`$ for every $`w`$. With $`\perp`$ taken in $`V`$, this gives
```math
F_c:=(\ker A_c)^{\perp}=\bigl\{\mathring f^{(c)}_w:\ w\in\mathcal H_c\bigr\}\subset V,\qquad \dim F_c=\mathrm{rank}A_c=\dim^{(c)}_0 .
\tag{14.4}
```
4. Step 2 and the standard identity $`(\bigcap_cN_c)^{\perp}=\sum_cN_c^{\perp}`$ give
```math
\dim_0=\dim V-\dim\ker A=\dim_{\mathbb R}\bigl(F_1+F_2+\cdots+F_m\bigr).
\tag{14.5}
```
5. **(b)** The dimension of a sum of subspaces is at most the sum of their dimensions, with equality iff the sum is direct. Hence
```math
\dim_0=\sum_c\dim^{(c)}_0\iff F_1+\cdots+F_m=F_1\oplus\cdots\oplus F_m\iff F_c\cap\sum_{c'\neq c}F_{c'}=\{0\}\ \ \forall c .
\tag{14.6}
```
   In terms of the records: if $`h\mapsto\sum_cg(w_c,u^{(c)}_h)`$ is constant on $`H`$ for some $`w_c\in\mathcal H_c`$, then every $`h\mapsto g(w_c,u^{(c)}_h)`$ is constant.
6. **(c)** The inclusions $`F_c\subseteq\sum_{c'}F_{c'}\subseteq V`$ and subadditivity give
```math
\max_c\dim^{(c)}_0\;\le\;\dim_0\;\le\;\min\Bigl(n-1,\ \sum_c\dim^{(c)}_0\Bigr),\qquad
\sum_c\dim^{(c)}_0\le2\sum_c(d_c-1)\le2D-2 .
\tag{14.7}
```
   The second inequality is (5.14) for each channel. The last follows from $`\prod_c(1+(d_c-1))\ge1+\sum_c(d_c-1)`$. For $`m=2`$, (14.5) reads exactly $`\dim_0=\dim^{(1)}_0+\dim^{(2)}_0-\dim(F_1\cap F_2)`$. The lower bound is attained for identical channels (all $`F_c`$ equal), and the upper bound whenever (14.6) holds.

### Step 4. Loop data of several channels

Taking imaginary parts in (14.3) gives $`\omega(u_h,u_{h'})=\sum_c\omega(u^{(c)}_h,u^{(c)}_{h'})`$. With (10.8) and $`h_{k+1}:=h_1`$,
```math
\Phi(h_1,\dots,h_k;\lambda)=-\lambda^2\sum_{c=1}^m\Omega^{(c)}(h_1,\dots,h_k)+O(\lambda^3),\qquad
\Omega^{(c)}:=\sum_{j=1}^k\omega\bigl(u^{(c)}_{h_j},u^{(c)}_{h_{j+1}}\bigr),
\tag{14.8}
```
so channel $`c`$ contributes $`-\lambda^2\Omega^{(c)}`$. Now suppress the channel index on $`K`$. The operator $`K-\langle K\rangle_c`$ is self-adjoint, the product $`\langle K_h\rangle_c\langle K_{h'}\rangle_c`$ is real, and $`\langle K_hK_{h'}\rangle_c^*=\langle K_{h'}K_h\rangle_c`$. Hence
```math
\langle u^{(c)}_h\vert u^{(c)}_{h'}\rangle=\langle K_hK_{h'}\rangle_c-\langle K_h\rangle_c\langle K_{h'}\rangle_c,
\qquad
\omega\bigl(u^{(c)}_h,u^{(c)}_{h'}\bigr)=\frac{1}{2\mathrm i}\bigl\langle[K_h,K_{h'}]\bigr\rangle_c .
\tag{14.9}
```

### Step 5. Commuting records in one channel (item 2)

1. **Spectral form.** Pairwise commuting self-adjoint operators on the finite-dimensional space $`\mathcal H_c`$ have a joint spectral decomposition $`K^{(c)}_h=\sum_{j=1}^J\kappa_h(j)P_j`$. Here $`P_1,\dots,P_J`$ are the orthogonal projectors onto the joint eigenspaces, with $`\sum_jP_j=\mathbb 1`$ and $`J\le d_c`$. The $`\kappa_h(j)`$ are real, and the tuples $`(\kappa_h(j))_{h\in H}`$ are distinct for distinct $`j`$. Let $`p_j:=\langle\chi_c\vert P_j\vert\chi_c\rangle=\lVert P_j\chi_c\rVert^2\ge0`$, so $`\sum_jp_j=1`$. Let $`S:=\{j:p_j>0\}`$, $`r_\chi:=\lvert S\rvert`$ and $`\bar\kappa_h:=\sum_jp_j\kappa_h(j)=\langle K^{(c)}_h\rangle_c`$.
2. **Gram matrix.** Since $`\langle\chi_c\vert P_jP_{j'}\vert\chi_c\rangle=\delta_{jj'}p_j`$, (14.9) becomes
```math
\langle u^{(c)}_h\vert u^{(c)}_{h'}\rangle=\sum_{j}p_j\bigl(\kappa_h(j)-\bar\kappa_h\bigr)\bigl(\kappa_{h'}(j)-\bar\kappa_{h'}\bigr),
\qquad d^{(c)}_0(h,h')^2=\mathrm{Var}_p\bigl(\kappa_h-\kappa_{h'}\bigr).
\tag{14.10}
```
   The Gram matrix is the covariance matrix of the functions $`j\mapsto\kappa_h(j)`$ under the weights $`p`$. It is real, symmetric and positive semidefinite.
3. **Loop term.** The Gram matrix is real; equivalently, $`[K_h,K_{h'}]=0`$ in (14.9). Hence $`\omega(u^{(c)}_h,u^{(c)}_{h'})=0`$ for all $`h,h'`$, and
```math
\Omega^{(c)}(h_1,\dots,h_k)=0\qquad\text{for every closed polygon}.
\tag{14.11}
```
   A commuting channel therefore contributes nothing to the $`\lambda^2`$ term of the loop phases (14.8).
4. **Largest $`\dim^{(c)}_0`$.** Since $`P_j\chi_c=0`$ for $`j\notin S`$, we have $`u^{(c)}_h=\sum_{j\in S}(\kappa_h(j)-\bar\kappa_h)P_j\lvert\chi_c\rangle=\Theta(\Pi\kappa_h)`$, where:
   - $`\kappa_h\in\mathbb R^S`$ denotes the restriction to $`S`$;
   - $`\Theta:\mathbb R^S\to\mathcal H_c`$, $`x\mapsto\sum_{j\in S}x_jP_j\lvert\chi_c\rangle`$, is injective, because the vectors $`P_j\lvert\chi_c\rangle`$, $`j\in S`$, are nonzero and mutually orthogonal;
   - $`\Pi y:=y-(\sum_{j\in S}p_jy_j)\mathbf 1`$ is a projector on $`\mathbb R^S`$ with kernel $`\mathbb R\mathbf 1`$.

   Fix $`h_0`$ and let $`L:=\mathrm{span}_{\mathbb R}\{\kappa_h-\kappa_{h_0}\}`$. The direction space of $`\mathrm{aff}\{u^{(c)}_h\}`$ is $`\Theta\Pi(L)`$, and $`\dim\Pi(L)=\dim(L+\mathbb R\mathbf 1)-1`$. Let $`[\cdots]_S`$ denote the real $`r_\chi\times n`$ matrix with the columns shown. Then
```math
\dim^{(c)}_0=\mathrm{rank}_{\mathbb R}\bigl[\mathbf 1,\ \kappa_h-\kappa_{h_0}\ (h\neq h_0)\bigr]_{S}-1\ \le\ \min(n,r_\chi)-1\ \le\ \min(n,d_c)-1 .
\tag{14.12}
```
   The first bound is attained iff the matrix has full rank $`\min(n,r_\chi)`$. Since $`r_\chi\le J\le d_c`$, the second bound is attained iff $`r_\chi\ge\min(n,d_c)`$. Hence the value $`\min(n-1,d_c-1)`$ is attained iff the matrix has full rank and $`r_\chi\ge\min(n,d_c)`$:
   - for $`n\ge d_c`$ this requires $`r_\chi=d_c`$: all joint eigenspaces are one-dimensional, and $`\lvert\chi_c\rangle`$ has a nonzero component along every joint eigenvector;
   - for $`n<d_c`$ it requires only that $`\lvert\chi_c\rangle`$ have nonzero weight on at least $`n`$ joint eigenspaces.

   The value depends on $`p`$ only through its support $`S`$.

### Step 6. Generic dimension of several channels (item 3)

1. **Carriers.** In each class, the records of channel $`c`$ lie in a real subspace $`S_c\subseteq\chi_c^\perp`$ of dimension $`\delta_c`$:
   - complex generic: $`S_c=\chi_c^\perp`$ by (5.13), so $`\delta_c=2(d_c-1)`$;
   - real: $`u^{(c)}_h=\sum_{k\ge2}(K^{(c)}_h)_{k1}e_k`$ has real coefficients, so $`S_c=\mathrm{span}_{\mathbb R}\{e_2,\dots,e_{d_c}\}`$ and $`\delta_c=d_c-1`$;
   - commuting (S2): $`u^{(c)}_h=\sum_j(\kappa_h(j)-\bar\kappa_h)\langle e_j\vert\chi_c\rangle\lvert e_j\rangle`$, so $`S_c=\{\sum_jx_j\langle e_j\vert\chi_c\rangle\lvert e_j\rangle:\ x\in\mathbb R^{d_c},\ \sum_jp_jx_j=0\}`$ with all $`p_j=\lvert\langle e_j\vert\chi_c\rangle\rvert^2>0`$, and $`\delta_c=d_c-1`$.

   Conversely, every family $`(v_h)\in S_c^H`$ is realized within the class:
   - complex generic and real: by $`K^{(c)}_h=\lvert v_h\rangle\langle\chi_c\rvert+\lvert\chi_c\rangle\langle v_h\rvert`$, which is real symmetric for real $`v_h`$ and gives $`\langle K^{(c)}_h\rangle_c=0`$ and $`u^{(c)}_h=v_h`$;
   - commuting: by $`\kappa_h=x_h`$, where $`v_h=\sum_jx_h(j)\langle e_j\vert\chi_c\rangle\lvert e_j\rangle`$, which gives $`\bar\kappa_h=0`$.
2. **Rank.** By Step 3, $`\dim_0=\mathrm{rank}A`$, with $`A:V\to\bigoplus_cS_c`$, a space of real dimension $`\sum_c\delta_c`$.
   - In fixed real bases, the entries of $`A`$ are linear in the draw. $`\mathrm{rank}A\ge r`$ iff some $`r\times r`$ minor, a polynomial in the draw, is nonzero.
   - Let $`r_*:=\min(n-1,\sum_c\delta_c)`$. Choose the $`v_h`$ in step 1 so that $`r_*`$ of the tuples $`(v^{(c)}_h-v^{(c)}_{h_0})_c`$, $`h\neq h_0`$, are linearly independent. Then some $`r_*\times r_*`$ minor is a nonzero polynomial.
   - A nonzero polynomial vanishes only on a Lebesgue-null set, so this minor is nonzero almost surely under S2. Since $`\mathrm{rank}A\le r_*`$ always,
```math
\dim_0=\min\Bigl(n-1,\ \sum_{c=1}^m\delta_c\Bigr)\quad\text{generically},\qquad
\delta_c=\begin{cases}2(d_c-1)&\text{complex generic},\\ d_c-1&\text{real or commuting}.\end{cases}
\tag{14.13}
```
   For $`m=1`$ this reproduces (7.7), (7.11) and the attained bound (14.12).
3. **Loop data.**
   - Real channel: the $`u^{(c)}_h`$ are real combinations of the orthonormal $`e_k`$. Their Gram matrix is real, so $`\Omega^{(c)}=0`$.
   - Commuting channel: $`\Omega^{(c)}=0`$ by (14.11).
   - Complex generic channel with $`d_c\ge2`$, and a triangle of distinct places $`h_1,h_2,h_3`$: $`\Omega^{(c)}`$ is a polynomial in the draw. It equals $`\omega(e_2,\mathrm ie_2)=1`$ at $`v_{h_1}=e_2`$, $`v_{h_2}=\mathrm ie_2`$, $`v_{h_3}=0`$. If, in addition, the records of all other channels vanish, the total $`\sum_c\Omega^{(c)}`$ takes the same value.

   By the polynomial argument, applied to all (finitely many) triangles at once,
```math
\text{the }\lambda^2\text{ term of }\Phi(h_1,h_2,h_3;\lambda)\text{ is generically }\neq0\iff\text{some channel is complex generic with }d_c\ge2;\ \text{otherwise it is }0 .
\tag{14.14}
```

### Step 7. Combinations with $`\dim_0=3`$ (item 3)

Cells with $`d_c=1`$ have $`\delta_c=0`$ and $`u^{(c)}_h=0`$; they are omitted. Since $`n-1\ge3`$, (14.13) gives $`\dim_0=3`$ generically iff
```math
\sum_c\delta_c=3\quad(n\ge5),\qquad\sum_c\delta_c\ge3\quad(n=4).
\tag{14.15}
```
For $`n\ge5`$: a complex generic channel has even $`\delta_c\ge2`$. So at most one such channel appears, with $`d_c=2`$, and the remaining $`\delta=1`$ comes from one real or commuting qubit. The table lists all solutions; R denotes a real or commuting channel, chosen per channel.

| channels (class, $`d_c`$) | $`\delta_c`$ | $`D=\prod_cd_c`$ | $`\lambda^2`$ loop term (14.14) |
|---|---|---|---|
| GUE(2) + R(2) | 2+1 | 4 | generically nonzero |
| R(4) | 3 | 4 | zero |
| R(3) + R(2) | 2+1 | 6 | zero |
| R(2) + R(2) + R(2) | 1+1+1 | 8 | zero |

For $`n=4`$: every combination with $`\sum_c\delta_c\ge3`$ gives $`\dim_0=3`$.

**Minimal total dimension.** We use $`D=\prod_c(1+(d_c-1))\ge1+\sum_c(d_c-1)`$, with equality only when there is a single nontrivial cell.
- $`n\ge5`$: the table gives $`D_{\min}=4`$, both with loop data (GUE(2)+R(2)) and without (R(4)). $`D\le3`$ allows only a single nontrivial cell with $`d_c\le3`$. Its $`\delta_c`$ lies in $`\{1,2,4\}`$, which excludes $`\delta_c=3`$.
- $`n=4`$, with loop data: $`D_{\min}=3`$, attained by a single complex generic qutrit ($`\delta=4`$). $`D=2`$ allows only $`\delta\le2`$.
- $`n=4`$, without loop data: all channels are R, so $`\sum_c(d_c-1)\ge3`$ and hence $`D\ge4`$. This is attained by R(4).

In summary,
```math
D_{\min}=4\ \text{with and without loop data}\ (n\ge5);\qquad D_{\min}=3\ \text{with},\ D_{\min}=4\ \text{without}\ (n=4).
\tag{14.16}
```

### Step 8. Cubic lattice (item 4a)

Since $`\langle0\vert\sigma_x\vert0\rangle=0`$ and $`\sigma_x\lvert0\rangle=\lvert1\rangle`$, we get $`u^{(1)}_h=x\lvert1\rangle`$, $`u^{(2)}_h=y\lvert1\rangle`$ and $`u^{(3)}_h=z\lvert1\rangle`$. With (14.2), (14.3), and the cells ordered $`1,2,3`$:
```math
u_h=x\lvert100\rangle+y\lvert010\rangle+z\lvert001\rangle,\qquad
d_0(h,h')=\sqrt{(x-x')^2+(y-y')^2+(z-z')^2}.
\tag{14.17}
```
- **Distance.** The map $`h\mapsto u_h`$ is injective. So $`\sim_0`$ is trivial, and $`(H,d_0)`$ is isometric to $`\{1,\dots,N\}^3\subset\mathbb R^3`$ with the Euclidean distance.
- **Dimension.** Each $`\dim^{(c)}_0=1`$, since $`N\ge2`$. By (14.4), $`F_1=\mathbb R\mathring x`$, $`F_2=\mathbb R\mathring y`$ and $`F_3=\mathbb R\mathring z`$ (since $`g(w,x\lvert1\rangle)=x\mathrm{Re}\langle w\vert1\rangle`$). If $`ax+by+cz`$ is constant on $`\{1,\dots,N\}^3`$ with $`N\ge2`$, then $`a=b=c=0`$. So the sum of the $`F_c`$ is direct, and $`\dim_0=3`$ by (14.6).
- **Loop.** The Gram matrix $`\langle u_h\vert u_{h'}\rangle=xx'+yy'+zz'`$ is real. All three channels are commuting ($`\sigma_x`$ only), consistent with (14.11).

Hence, for every lattice triangle,
```math
\dim_0=3,\qquad\Phi(h_1,h_2,h_3;\lambda)=O(\lambda^3)\quad(\lambda^2\text{ term }=0).
\tag{14.18}
```

### Step 9. Plane plus line (item 4b)

Since $`\sigma_y\lvert0\rangle=\mathrm i\lvert1\rangle`$ and $`\langle0\vert\sigma_y\vert0\rangle=0`$, we get $`u^{(1)}_h=(x+\mathrm iy)\lvert1\rangle`$ and $`u^{(2)}_h=z\lvert1\rangle`$. Therefore
```math
u_h=(x+\mathrm iy)\lvert10\rangle+z\lvert01\rangle,\qquad
\langle u_h\vert u_{h'}\rangle=xx'+yy'+zz'+\mathrm i\,(xy'-yx'),
\tag{14.19}
```
```math
d_0(h,h')=\sqrt{(x-x')^2+(y-y')^2+(z-z')^2},
\tag{14.20}
```
- **Distance.** As in Step 8, $`(H,d_0)`$ is isometric to $`\{1,\dots,N\}^3\subset\mathbb R^3`$.
- **Dimension.** $`w=\lvert1\rangle`$ gives $`f^{(1)}_w=x`$, and $`w=\mathrm i\lvert1\rangle`$ gives $`f^{(1)}_w=\mathrm{Re}[-\mathrm i(x+\mathrm iy)]=y`$. So $`F_1=\mathrm{span}\{\mathring x,\mathring y\}`$ and $`\dim^{(1)}_0=2`$, while $`F_2=\mathbb R\mathring z`$ and $`\dim^{(2)}_0=1`$. The sum is direct, so $`\dim_0=3`$ by (14.6).
- **Loop.** By (14.19), $`\omega(u_h,u_{h'})=xy'-yx'`$. Only channel 1 contributes, since channel 2 is commuting (14.11). By (14.8), with $`h_j=(x_j,y_j,z_j)`$,
```math
\Phi(h_1,h_2,h_3;\lambda)=-\lambda^2\bigl[(x_2-x_1)(y_3-y_1)-(x_3-x_1)(y_2-y_1)\bigr]+O(\lambda^3).
\tag{14.21}
```
The bracket is the integer $`2A_{xy}`$, where $`A_{xy}`$ is the signed area of the projection of the triangle onto the $`(x,y)`$ coordinates. It is nonzero iff the projected points are not collinear. For example, the term is $`-\lambda^2`$ for $`h_1=(x,y,z)`$, $`h_2=(x+1,y,z)`$, $`h_3=(x,y+1,z)`$, and $`0`$ for every triangle with constant $`x`$ or constant $`y`$.

## Result

- **Carry-over (Step 1).** (5.10)–(5.14), (10.8) and (10.12) hold for the composite medium after the replacements $`\mathcal H_c\to\mathcal H_M`$, $`K_h\to\sum_cK^{(c)}_h`$, $`\chi\to\bigotimes_c\chi_c`$.
- **Item 1.**
  - (a) $`u_h=\sum_c\iota_c(u^{(c)}_h)`$ (14.2), with mutually orthogonal channel images. $`d_0^2=\sum_c(d^{(c)}_0)^2`$ (14.3). $`\dim_0=\dim(F_1+\cdots+F_m)`$ (14.5), with the read-out spaces $`F_c`$ of (14.4).
  - (b) $`\dim_0=\sum_c\dim^{(c)}_0`$ iff the $`F_c`$ are linearly independent (14.6).
  - (c) $`\max_c\dim^{(c)}_0\le\dim_0\le\min(n-1,\sum_c\dim^{(c)}_0)`$ (14.7).
  - Loop phases: the $`\lambda^2`$ term is a sum of channel contributions (14.8), with $`\omega=\frac1{2\mathrm i}\langle[K_h,K_{h'}]\rangle_c`$ (14.9).
- **Item 2.** The Gram matrix is a real covariance matrix (14.10). $`\dim^{(c)}_0\le\min(n,r_\chi)-1\le\min(n,d_c)-1`$, with the rank formula of (14.12). The value $`\min(n-1,d_c-1)`$ is attained iff the matrix in (14.12) has full rank and $`r_\chi\ge\min(n,d_c)`$; full spectral support is needed only for $`n\ge d_c`$. The channel's $`\lambda^2`$ loop term vanishes (14.11).
- **Item 3.**
  - Generically, $`\dim_0=\min(n-1,\sum_c\delta_c)`$ (14.13).
  - The $`\lambda^2`$ loop term is generically nonzero iff there is a complex generic channel with $`d_c\ge2`$ (14.14).
  - $`\dim_0=3`$ iff $`\sum_c\delta_c=3`$ for $`n\ge5`$, or $`\sum_c\delta_c\ge3`$ for $`n=4`$ (14.15); the solutions are listed in the table of Step 7.
  - $`D_{\min}`$ is given in (14.16).
- **Item 4.**
  - (a) Euclidean $`d_0`$, $`\dim_0=3`$, zero $`\lambda^2`$ loop term (14.17), (14.18).
  - (b) Euclidean $`d_0`$, $`\dim_0=3`$, and loop phase $`-\lambda^2\cdot2A_{xy}`$ (14.19)–(14.21).

## Consistency checks

1. **Scaling.** The evolution (14.1) depends only on $`\lambda K`$. Under $`K^{(c)}_h\to sK^{(c)}_h`$ with $`s>0`$:
   - $`u\to su`$ and $`d_0\to sd_0`$, so $`\lambda d_0`$ is invariant under $`\lambda\to\lambda/s`$;
   - $`\omega\to s^2\omega`$, so $`\lambda^2\Omega^{(c)}`$ is invariant in (14.8) and (14.21);
   - $`\dim_0`$, $`\dim^{(c)}_0`$ and $`\delta_c`$ are unchanged.
2. **Single channel ($`m=1`$).** Here $`\iota_1=\mathrm{id}`$, and (14.2), (14.3) reduce to (5.10). (14.5) gives $`\dim_0=\dim^{(1)}_0`$, the two bounds in (14.7) coincide, and (14.6) holds trivially. (14.8) reduces to (10.8), and (14.13) reduces to (7.7) and (7.11).
3. **Loop reversal.** Reversing $`(h_1,\dots,h_k)`$ flips the sign of every $`\Omega^{(c)}`$, because $`\omega`$ is antisymmetric (it is the imaginary part of a Hermitian form). In (14.21), exchanging $`h_2\leftrightarrow h_3`$ flips the sign of the bracket. As a cross-check of (14.9) in Step 9, $`[x\sigma_x+y\sigma_y,\,x'\sigma_x+y'\sigma_y]=2\mathrm i(xy'-yx')\sigma_z`$ and $`\langle0\vert\sigma_z\vert0\rangle=1`$ reproduce $`\omega=xy'-yx'`$.

## Open issues

- The carry-over (Step 1) assumes that the constructions of 05 and 10 refer to the medium only as the companion part of $`a`$ (view and branch states). Only their quoted equations were available here.
- Two parts of S2 are readings of "generically within a class": the independence of the channels, and the definition of the generic commuting class.
- Only the $`\lambda^2`$ term of the loop phases is determined. For real and commuting channels the loop phases are $`O(\lambda^3)`$; higher orders are not addressed.
- For $`n=4`$, $`\dim_0=3=n-1`$ is the maximal possible value. The condition (14.15) is then only a threshold.

## Methods used

- tensor-product isometric embeddings, orthogonal decomposition
- real affine spans, rank–nullity, orthogonal complements of intersections and sums of subspaces
- splitting of a Hermitian form into Euclidean and symplectic parts
- joint spectral decomposition of commuting self-adjoint operators; covariance matrices
- genericity through nonvanishing polynomials (minors), absolute continuity
- shoelace formula for signed areas
