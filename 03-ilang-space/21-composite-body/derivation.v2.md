# Composite body: response of two bound bodies to a uniform cost gradient

- **Subproject:** 03-ilang-space
- **Package:** 21-composite-body
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-09

## Changes from previous version

- **Step 2, after (21.2) (I1).** The sentence "Off-diagonal single-object terms cannot be moved, because $W$ and the recording terms are diagonal in the places of the bodies" was false as a statement about A5, so it was removed. In its place is a paragraph, "Placements outside the form of the setting". It treats the diagonal binding operator $W$ and the full $b_1$–$b_2$ pair term as separate objects. It shows that every A5 regrouping, including one that lists an off-diagonal single-object term in any pair term, leaves the total $C$, $\Psi(\lambda)$, the $p^{(i)}$ and the blocks (21.1) unchanged. It also states that $E_i$, $L^{(i)}$ and $(t^{(i)},K^{(i)},W)$ are read from the total $C$, so every placement is covered by (21.2).
- **Step 2, "Phases" (I2).** "if and only if" became "if", with the kernel of $f\mapsto G_f$ stated and an explanation of why the covariance of $\mu_c$ holds for every representative.
- **Result, item 1 (I1).** Reworded to match the extended placement check.
- No other step, formula or tag changed.

## Response to verification

- **I1:** Accepted and fixed in Step 2 (paragraph "Placements outside the form of the setting") and in Result item 1.
- **I2:** Accepted and fixed in Step 2 ("Phases").

## Setup and assumptions

The setting, the start $\Phi\otimes\chi$, the notation and the definitions (background, $\bar x_i$, $\bar R$, $A$, $L^{(i)}$, $\mu_i$, $G_f$, $F$, $F_{\rm tot}$, $\mu_c$) are those of question.md, "Goal". A1–A7 hold. Items 1–3 are exact for finite place sets (A1). Item 4 works on $\ell^2(\mathbb Z)\otimes\ell^2(\mathbb Z)\otimes\mathcal H_c$ with starts of finite support, $t>0$, $U\le0$ ($U=0$ only for comparison), $\sigma_X>0$. Inputs used as quoted: (2.1)–(2.2), (5.10)–(5.11), (16.3)–(16.4), (17.15), (17.20), (20.1), (20.6), (20.7) together with the quoted Step 4 of 20, (20.10), (20.12), (20.13).

Additional notation.
- $\Phi=\sum_{h,k}\Phi_{hk}\lvert h\rangle\lvert k\rangle$. The views of the start are $(\rho_1)_{hh'}=\sum_k\Phi_{hk}\Phi^*_{h'k}$ and $(\rho_2)_{kk'}=\sum_h\Phi_{hk}\Phi^*_{hk'}$, so $p^{(i)}(0)$ is the diagonal of $\rho_i$.
- Branch vectors (2.1): $\psi^{(1)}_h(\lambda)\in\mathcal H_2\otimes\mathcal H_c$ for the part $\{b_1\}$, and $\psi^{(2)}_k(\lambda)\in\mathcal H_1\otimes\mathcal H_c$ for $\{b_2\}$. Their blocks are $C^{(1)}_{hh'}$ and $C^{(2)}_{kk'}$, and their currents (20.6) are $J^{(i)}$.
- $W_{h\cdot}:=\sum_kW_{hk}\lvert k\rangle\langle k\rvert$ on $\mathcal H_2$; $W_{\cdot k}:=\sum_hW_{hk}\lvert h\rangle\langle h\rvert$ on $\mathcal H_1$; $\Omega^{(1)}_h:=t^{(1)}_{hh}+\epsilon^{(1)}_h$; $\Omega^{(2)}_k:=t^{(2)}_{kk}+\epsilon^{(2)}_k$.
- Formulas are written for $b_1$. The formulas for $b_2$ follow by exchanging the roles of $h$ and $k$ in $\Phi_{hk}$, $W_{hk}$, $t^{(i)}$ and $K^{(i)}$.

## Derivation

### Step 1. Blocks of $C$

For the part $\{b_1\}$ with companion $\{b_2,c\}$, the five terms of $C$ give the blocks

$$
C^{(1)}_{hh'}=t^{(1)}_{hh'}\,\mathbb 1_{2c}\quad(h\neq h'),\qquad
C^{(1)}_{hh}=t^{(1)}_{hh}+C_2\otimes\mathbb 1_c+\sum_k\lvert k\rangle\langle k\rvert\otimes K^{(2)}_k+\mathbb 1_2\otimes K^{(1)}_h+W_{h\cdot}\otimes\mathbb 1_c ,
\tag{21.1}
$$

and likewise for $\{b_2\}$. The cost edges of $b_i$ are therefore exactly $E_i$. At $\lambda=0$ we have $\psi^{(1)}_h=\phi_h\otimes\chi$ with $\phi_h:=\sum_k\Phi_{hk}\lvert k\rangle$, and $\langle\phi_j\vert\phi_{h'}\rangle=(\rho_1)_{h'j}$ by (2.2). Hence the edge costs of 20 are $L^{(1)}_{hh'}(0)=2\operatorname{Re}[t^{(1)}_{hh'}(\rho_1)_{h'h}]$.

### Step 2. Well-definedness (item 1)

**Freedom of the description.** Two data sets $(t^{(1)},t^{(2)},K^{(1)},K^{(2)},W)$ of the form of the setting give the same $C$ if and only if their operators $(\langle h\rvert\langle k\rvert\otimes\mathbb 1_c)\,C\,(\lvert h'\rangle\lvert k'\rangle\otimes\mathbb 1_c)=t^{(1)}_{hh'}\delta_{kk'}+\delta_{hh'}t^{(2)}_{kk'}+\delta_{hh'}\delta_{kk'}(K^{(1)}_h+K^{(2)}_k+W_{hk})$ agree. This fixes the off-diagonal $t^{(i)}$. It also forces $\delta K^{(1)}_h+\delta K^{(2)}_k$ to be a real multiple of $\mathbb 1_c$ for every pair $h,k$, so $\delta K^{(1)}_h-\delta K^{(1)}_{h'}$ is a scalar. The general change is therefore

$$
\delta K^{(1)}_h=Z+\alpha_h,\quad \delta K^{(2)}_k=-Z+\beta_k,\quad \delta t^{(1)}_{hh}=\tau_h,\quad \delta t^{(2)}_{kk}=\tau'_k,\quad \delta W_{hk}=-(\tau_h+\alpha_h)-(\tau'_k+\beta_k),
\tag{21.2}
$$

where $Z=Z^\dagger$ on $\mathcal H_c$ and $\alpha_h,\beta_k,\tau_h,\tau'_k$ are real. This family contains:
- the split (16.3);
- every placement of single-object terms (A5), for example a diagonal term on $b_1$ moved from $C_1$ into $W$ ($\delta W_{hk}=-\tau_h$) or into the records ($\alpha_h=-\tau_h$).

**Placements outside the form of the setting.** A5 also allows a single-object term $D=D^\dagger$ on $b_1$, diagonal or not, to be listed in the $b_1$–$b_2$ pair term as $D\otimes\mathbb 1_2$, or in the $b_1$–$c$ pair term as $D\otimes\mathbb 1_c$. The same holds for $b_2$, and for a term on $c$ in either body–medium pair term. The full $b_1$–$b_2$ pair term is then $W+D\otimes\mathbb 1_2$, which differs from the binding operator $W$. In all formulas, $W$ denotes the diagonal binding operator of a data set of the form of the setting that reproduces $C$. Every regrouping leaves the total $C$ unchanged, and with it $\Psi(\lambda)$, the $p^{(i)}$ and the blocks (21.1). Every input of the formulas below is read from the total $C$, not from a contract list:
- the edge sets are $E_1=\{\{h,h'\}:h\neq h',\ C^{(1)}_{hh'}\neq0\}$, and $E_2$ likewise;
- the edge costs $L^{(i)}$ are built from the blocks;
- the data $(t^{(i)},K^{(i)},W)$ are read from the matrix elements above.

In these matrix elements an off-diagonal $D$ appears as $D_{hh'}\delta_{kk'}\mathbb 1_c$, i.e. as part of $t^{(1)}_{hh'}$, wherever it is listed. A diagonal $D$, or a term on $c$, gives one of the changes (21.2). Hence (21.2) covers every A5 placement. The scalars drop out of the record vectors, and (16.4) gives $u^{(1)}_h\mapsto u^{(1)}_h+z$ and $u^{(2)}_k\mapsto u^{(2)}_k-z$, with $z=(Z-\langle Z\rangle)\chi$. All $\Delta^{(i)}$ and $E_i$ are unchanged.

**Consequences.**
- $\Psi(\lambda)=e^{-iC\lambda}(\Phi\otimes\chi)$ depends only on $C$, so every $p^{(i)}_h(\lambda)$ is invariant. Since $\sum_hp^{(1)}_h=1$, $\bar x_1\mapsto\bar x_1+z$ and $\bar x_2\mapsto\bar x_2-z$. The centre $\bar R(\lambda)$ gives the two bodies equal weight, so it and $A(\lambda)$ are **invariant**.
- $G_f\mapsto G_f+g(f,z)\mathbb 1-g(f,z)\mathbb 1=G_f$. Hence $C+G_f$, $A(0)\vert_{C+G_f}$ and $\mu_c$ are **invariant**.
- The difference transforms as

$$
\bar x_1-\bar x_2\;\longmapsto\;\bar x_1-\bar x_2+2z .
\tag{21.3}
$$

  Every $z$ with $\langle\chi\vert z\rangle=0$ occurs: $Z=\lvert z\rangle\langle\chi\rvert+\lvert\chi\rangle\langle z\rvert$ gives $Z\chi=z$ and $\langle Z\rangle=0$. All $u^{(i)}$ lie in $\chi^\perp:=\{v:\langle\chi\vert v\rangle=0\}$. So the choice of split can give $\bar x_1-\bar x_2$ any value in $\chi^\perp$: it is **not well defined**, and neither is any of its components. Differences within one body, such as $\Delta^{(i)}$ and $\bar x_i(\lambda)-\bar x_i(0)$, are well defined.
- **Phases.** The common phase of the start or of $\Psi(\lambda)$ changes no view, and hence no $p^{(i)}_h$ and no $L^{(i)}$. How much of that phase sits on $\chi$ is a convention: $\Phi\otimes\chi=e^{-i\theta}\Phi\otimes e^{i\theta}\chi$. Moving it maps $u\mapsto e^{i\theta}u$. Then $\bar x_i$, $\bar R$ and $A$ are mapped by the $g$-isometry $R_\theta:v\mapsto e^{i\theta}v$. $G_f$ stays the same if $f\mapsto R_\theta f$, and then $\mu_c\mapsto R_\theta\mu_cR_\theta^{-1}$. This condition is sufficient, not necessary. The real-linear map $f\mapsto G_f$ has a kernel, which contains $\chi$ and $i\chi$ because all $u^{(i)}$ lie in $\chi^\perp$, so $G_f$ fixes $f$ only modulo that kernel. On the kernel $G_f=0$, so $\mu_c$ maps it to zero, and the covariance of $\mu_c$ does not depend on which representative $f$ is used. These quantities are therefore well defined as structures on the background, which is itself fixed only up to $R_\theta$. All their $g$-products with the $\Delta^{(i)}$ are invariant. The phase split (1.6) does not enter, because every definition uses $\psi_h$ (2.1) and $p_h$ (2.2).

### Step 3. Exact acceleration of the centre (item 2(a))

**Applicability.** (20.1) holds for every description and every object that is the only instance of its type. (20.6) follows from (20.1) alone. (20.7) follows from (20.1) and the $\lambda$-independence of the record vectors. The quoted Step 4 of 20 also gives (20.7) edge by edge: $\dot J_{h'\to h}=2\operatorname{Re}[\dots]=A_{hh'}+B_{hh'}$. None of this uses the structure of the companion, and here the record vectors are fixed by $K^{(i)}$ and $\chi$. So (20.6)–(20.7) **apply** to $b_1$ with companion $\{b_2,c\}$ and to $b_2$ with companion $\{b_1,c\}$, with cost edges $E_1$ and $E_2$.

**Exact identity.** By (21.1), $C^{(1)}_{hh'}$ is a multiple of $\mathbb 1$ for $h\neq h'$. Hence $C^{(1)}_{hh}C^{(1)}_{hh'}-C^{(1)}_{hh'}C^{(1)}_{h'h'}=t^{(1)}_{hh'}(C^{(1)}_{hh}-C^{(1)}_{h'h'})$, in which $C_2$ and the $K^{(2)}$ cancel, and $\langle\eta_h\rvert=\sum_{j\neq h}t^{(1)}_{jh}\langle\psi^{(1)}_j\rvert$. With $A=\tfrac12(\ddot{\bar x}_1+\ddot{\bar x}_2)$, for every $\lambda$:

$$
\begin{aligned}
A(\lambda)&=\tfrac12\sum_{i=1,2}\ \sum_{\{h,h'\}\in E_i}\bigl[A^{(i)}_{hh'}(\lambda)+B^{(i)}_{hh'}(\lambda)\bigr]\Delta^{(i)}_{hh'},\\
A^{(1)}_{hh'}&=2\operatorname{Re}\Bigl[t^{(1)}_{hh'}\Bigl(\sum_{j\neq h}t^{(1)}_{jh}\langle\psi^{(1)}_j\vert\psi^{(1)}_{h'}\rangle-\sum_{j\neq h'}t^{(1)}_{h'j}\langle\psi^{(1)}_h\vert\psi^{(1)}_j\rangle\Bigr)\Bigr],\\
B^{(1)}_{hh'}&=2\operatorname{Re}\Bigl[t^{(1)}_{hh'}\langle\psi^{(1)}_h\vert\bigl(t^{(1)}_{hh}-t^{(1)}_{h'h'}\bigr)+\mathbb 1_2\otimes\bigl(K^{(1)}_h-K^{(1)}_{h'}\bigr)+\bigl(W_{h\cdot}-W_{h'\cdot}\bigr)\otimes\mathbb 1_c\vert\psi^{(1)}_{h'}\rangle\Bigr].
\end{aligned}
\tag{21.4}
$$

**Terms that contain $W$.** $W$ appears explicitly only in the last term of each $B^{(i)}$:

$$
A_W(\lambda)=\tfrac12\Bigl[\sum_{E_1}w^{(1)}_{hh'}\Delta^{(1)}_{hh'}+\sum_{E_2}w^{(2)}_{kk'}\Delta^{(2)}_{kk'}\Bigr],\qquad
w^{(1)}_{hh'}:=2\operatorname{Re}\bigl[t^{(1)}_{hh'}\langle\psi^{(1)}_h\vert(W_{h\cdot}-W_{h'\cdot})\otimes\mathbb 1_c\vert\psi^{(1)}_{h'}\rangle\bigr],
\tag{21.5}
$$

and $w^{(2)}_{kk'}$ is the same with $W_{\cdot k}-W_{\cdot k'}$. For $\lambda>0$ every term of (21.4) also depends on $W$ implicitly, through $\Psi(\lambda)$.

### Step 4. $A(0)$ and its $W$-terms (item 2(b))

**Closed form.** Put $\psi^{(1)}_h=\phi_h\otimes\chi$ into (21.4). This uses $\langle\psi^{(1)}_j\vert\psi^{(1)}_{h'}\rangle=(\rho_1)_{h'j}$, $\langle\chi\vert K^{(1)}_h-K^{(1)}_{h'}\vert\chi\rangle=\epsilon^{(1)}_h-\epsilon^{(1)}_{h'}$ and $\operatorname{Re}[t^{(1)}_{hh'}(\rho_1)_{h'h}]=\tfrac12L^{(1)}_{hh'}(0)$:

$$
A(0)=\tfrac12\sum_{i=1,2}\Bigl[a^{(i)}_{\rm hop}+\sum_{E_i}\bigl(\Omega^{(i)}_h-\Omega^{(i)}_{h'}\bigr)L^{(i)}_{hh'}(0)\,\Delta^{(i)}_{hh'}\Bigr]+A_W(0).
\tag{21.6}
$$

Here $a^{(1)}_{\rm hop}:=\sum_{E_1}A^{(1)}_{hh'}(0)\Delta^{(1)}_{hh'}$, with $A^{(1)}_{hh'}(0)=2\operatorname{Re}\bigl[t^{(1)}_{hh'}\bigl(\sum_{j\neq h}t^{(1)}_{jh}(\rho_1)_{h'j}-\sum_{j\neq h'}t^{(1)}_{h'j}(\rho_1)_{jh}\bigr)\bigr]$. The $W$-terms are

$$
A_W(0)=\tfrac12\Bigl[\sum_{E_1}\sum_k\ell^{(1)}_{hh';k}\bigl(W_{hk}-W_{h'k}\bigr)\Delta^{(1)}_{hh'}+\sum_{E_2}\sum_h\ell^{(2)}_{kk';h}\bigl(W_{hk}-W_{hk'}\bigr)\Delta^{(2)}_{kk'}\Bigr],\quad
\ell^{(1)}_{hh';k}:=2\operatorname{Re}\bigl(t^{(1)}_{hh'}\Phi^*_{hk}\Phi_{h'k}\bigr),\ \ \ell^{(2)}_{kk';h}:=2\operatorname{Re}\bigl(t^{(2)}_{kk'}\Phi^*_{hk}\Phi_{hk'}\bigr).
\tag{21.7}
$$

Since $\sum_k\ell^{(1)}_{hh';k}=L^{(1)}_{hh'}(0)$, the $\ell$ are the edge costs of one body resolved by the place of the other. All terms of (21.6) except $A_W(0)$ depend on $\Phi$ only through the views $\rho_i$; $A_W(0)$ also depends on the correlations of $\Phi$. $A(0)-A(0)\vert_{W=0}=A_W(0)$, because only $A_W(0)$ contains $W$. The $W$-terms are defined relative to the given $W$: under (21.2), $A_W(0)$ changes by $-\tfrac12\sum_{E_1}[(\tau_h+\alpha_h)-(\tau_{h'}+\alpha_{h'})]L^{(1)}_{hh'}\Delta^{(1)}_{hh'}$ (and likewise for $b_2$). The $\Omega$-term compensates this change exactly, so only $A(0)$ is invariant.

**They do not vanish for every $\Phi$.** Take $\Phi=\phi\otimes\lvert k_0\rangle$ with $\phi=(\lvert h_1\rangle+e^{i\theta}\lvert h_2\rangle)/\sqrt2$, $\{h_1,h_2\}\in E_1$ and $e^{i\theta}=t^{(1)*}_{h_1h_2}/\lvert t^{(1)}_{h_1h_2}\rvert$. Then $\ell^{(1)}_{h_1h_2;k_0}=\lvert t^{(1)}_{h_1h_2}\rvert$. All other $\ell^{(1)}$ vanish, and so do all $\ell^{(2)}$, because only one place of $b_2$ carries weight. Hence $A_W(0)=\tfrac12\lvert t^{(1)}_{h_1h_2}\rvert(W_{h_1k_0}-W_{h_2k_0})\Delta^{(1)}_{h_1h_2}\neq0$ whenever $W_{h_1k_0}\neq W_{h_2k_0}$ and $u^{(1)}_{h_1}\neq u^{(1)}_{h_2}$.

**Sufficient condition (on $\Phi$ and $W$).** If

$$
\ell^{(1)}_{hh';k}\,(W_{hk}-W_{h'k})=0\ \ \forall\,\{h,h'\}\in E_1,\ k,\qquad
\ell^{(2)}_{kk';h}\,(W_{hk}-W_{hk'})=0\ \ \forall\,\{k,k'\}\in E_2,\ h,
\tag{21.8}
$$

then every term of (21.7) vanishes, so $A_W(0)=0$. In words: no edge cost resolved by the place of the other body sits on a hop across which the binding changes. An example is $\Phi$ equal to a single joint place.

**Eigenvectors of $C_{\rm body}$.** Let $C_{\rm body}\Phi=E\Phi$, and evolve $\Phi\otimes\chi$ under $C_{\rm body}\otimes\mathbb 1_c$. Then $\Psi(\lambda)=e^{-iE\lambda}\Phi\otimes\chi$, so every $J^{(i)}$ is constant. The edge-by-edge identity with the blocks (21.1) at $K^{(i)}=0$ then gives, on every edge of $E_1$ (and likewise for $b_2$),

$$
w^{(1)}_{hh'}(0)=-A^{(1)}_{hh'}(0)-\bigl(t^{(1)}_{hh}-t^{(1)}_{h'h'}\bigr)L^{(1)}_{hh'}(0).
\tag{21.9}
$$

None of these quantities contains $K^{(i)}$, so (21.9) also holds for the full $C$. Inserting it into (21.6) gives $A(0)=\tfrac12\sum_i\sum_{E_i}(\epsilon^{(i)}_h-\epsilon^{(i)}_{h'})L^{(i)}_{hh'}(0)\Delta^{(i)}_{hh'}$. In an eigenvector of $C_{\rm body}$, therefore, the $W$-terms do not vanish but are cancelled by the hopping and on-site terms. $A_W(0)=0$ holds if and only if $\sum_i\bigl[a^{(i)}_{\rm hop}+\sum_{E_i}(t^{(i)}_{hh}-t^{(i)}_{h'h'})L^{(i)}_{hh'}(0)\Delta^{(i)}_{hh'}\bigr]=0$. On the chain of item 4 this bracket vanishes identically (Step 7); Step 10 gives the approximate version of the statement.

### Step 5. Inertia of the composite (item 3)

Adding $G_f$ shifts $t^{(1)}_{hh}$ by $g(f,u^{(1)}_h)$ and $t^{(2)}_{kk}$ by $g(f,u^{(2)}_k)$. It changes none of $K^{(i)}$, $\chi$ (so neither background), $\Phi$, the off-diagonal $t^{(i)}$ or $W$. In (21.6), $a^{(i)}_{\rm hop}$, $L^{(i)}(0)$ and $A_W(0)$ contain no diagonal $t^{(i)}$. Only $\Omega^{(i)}_h-\Omega^{(i)}_{h'}$ changes, by $g(f,\Delta^{(i)}_{hh'})$. With $f=-F=-\tfrac12F_{\rm tot}$:

$$A(0)\vert_{C+G_f}-A(0)\vert_C=-\tfrac14\sum_i\sum_{E_i}L^{(i)}_{hh'}(0)\Delta^{(i)}_{hh'}\,g(\Delta^{(i)}_{hh'},F_{\rm tot}).$$

This is real-linear in $F_{\rm tot}$, which runs through all of $\mathcal H_c$. So $\mu_c$ exists, is unique, and equals

$$
\mu_c=-\frac14\sum_{i=1,2}\ \sum_{\{h,h'\}\in E_i}L^{(i)}_{hh'}(0)\,\Delta^{(i)}_{hh'}\,g\bigl(\Delta^{(i)}_{hh'},\cdot\,\bigr)=\frac14\bigl(\mu_1+\mu_2\bigr).
\tag{21.10}
$$

**(a)** $\mu_c$ is a function of the edge costs $L^{(1)}(0)$, $L^{(2)}(0)$ and the backgrounds (through the $\Delta^{(i)}$) alone. It equals one quarter of the sum of the parts' $\mu_i$, evaluated in the joint start. Each $\mu_i$ depends on $\Phi$ only through the view $\rho_i$ (Step 1). For $\mu_1=\mu_2$, $\mu_c=\tfrac12\mu_1$. If $\mu_i=I_i^{-1}\hat n\,g(\hat n,\cdot)$ with a common unit vector $\hat n$, then $I_c=4I_1I_2/(I_1+I_2)$, which equals $I_1+I_2$ only if $I_1=I_2$.

**(b)** $W$ does not appear in (21.10). It enters $\mu_c$ only through $\Phi$, for example when $\Phi$ is chosen near the bottom of $C_{\rm body}$ (Step 8). $\mu_c$ is $g$-symmetric, since $g(v,\mu_cw)=-\tfrac14\sum_i\sum_{E_i}L^{(i)}_{hh'}(0)\,g(\Delta^{(i)}_{hh'},v)\,g(\Delta^{(i)}_{hh'},w)$. It is positive semidefinite if and only if

$$
\sum_{i=1,2}\ \sum_{E_i}L^{(i)}_{hh'}(0)\,g\bigl(\Delta^{(i)}_{hh'},v\bigr)^2\le0\qquad\forall\,v\in\mathcal H_c .
\tag{21.11}
$$

A sufficient condition is $L^{(i)}_{hh'}(0)\le0$ on every edge with $\Delta^{(i)}_{hh'}\neq0$.

### Step 6. Spectrum of $C_{\rm body}$ on the chain (item 4(a), standard)

$C_{\rm body}$ commutes with the joint shift. In the basis $e^{iK(m+n)/2}\varphi(m-n)$, with $K\in(-\pi,\pi]$ the total quasi-momentum, it reduces to a chain in $r=m-n$ with hopping $2t\cos(K/2)$ and an on-site term $U$ at $r=0$. Such a chain has the continuum $[-4t\lvert\cos\tfrac K2\rvert,4t\lvert\cos\tfrac K2\rvert]$ (the values $4t\cos\tfrac K2\cos q$). For $U<0$ it has exactly one bound state, with $\varphi(r)\propto x_K^{\lvert r\rvert}$, $\lvert x_K\rvert<1$, below that continuum. Hence

$$
E_b(K)=-\sqrt{U^2+16t^2\cos^2\tfrac K2},\qquad \operatorname{spec}C_{\rm body}=[-4t,4t]\cup\bigl[-\sqrt{U^2+16t^2},\,-\lvert U\rvert\bigr],\qquad E_{\min}(t,U)=-\sqrt{U^2+16t^2}.
\tag{21.12}
$$

At $U=0$ there is no bound state, and $E_{\min}(t,0)=-4t$ agrees with the formula.

### Step 7. The chain for starts of finite support

The records give $u^{(1)}_{h_m}=u^{(2)}_{k_m}=m\,e$ (as in (17.15)), so $\Delta=-e$ on every edge $\{m,m+1\}$, and $\Omega^{(i)}_m=m\langle X\rangle$ (20.12). Let $M_1$, $M_2$ be copies of $M$ on $b_1$, $b_2$; then $\bar x_i=\langle M_i\rangle e$. Let $S_1,S_2$ be the shifts on $b_1,b_2$, $C_{\rm hop}:=C_1\otimes\mathbb 1+\mathbb 1\otimes C_2$, and $Y_i:=t(S_i-S_i^\dagger)$, with $\lVert Y_i\rVert\le2t$. By (1.9), $\ddot{\langle M_1\rangle}=-\langle[C,[C,M_1]]\rangle$, and the following hold:
- $[S,M]=S$ gives $[C,M_1]=Y_1$. All other terms of $C$ are diagonal in $h$ or act on other objects.
- $[C_1,Y_1]=2t^2[S_1^\dagger,S_1]=0$, because $S$ is unitary on $\ell^2(\mathbb Z)$; this is $a^{\rm hop}=0$, cf. (20.13).
- $[M_1X,Y_1]=-C_1X$ for the record term $\sum_m\lvert h_m\rangle\langle h_m\rvert\otimes mX=M_1X$.
- $C_2$ and $M_2X$ commute with $Y_1$.

Hence $\ddot{\bar x}_1(0)=\bigl(\langle C_1\otimes\mathbb 1\rangle_\Phi\langle X\rangle-\langle\Phi\vert[W,Y_1]\vert\Phi\rangle\bigr)e$, and likewise for $b_2$. With $\sum_{E_1}L^{(1)}(0)=\langle C_1\otimes\mathbb 1\rangle_\Phi$ (zero diagonal), (21.10) and (21.7) give

$$
\mu_c=-\tfrac14\langle C_{\rm hop}\rangle_\Phi\,\sigma_X^2\,\hat e\,g(\hat e,\cdot\,),\qquad
A(0)=\tfrac12\langle C_{\rm hop}\rangle_\Phi\langle X\rangle\,e+A_W(0),\qquad
A_W(0)=-\tfrac12\langle\Phi\vert[W,Y_1+Y_2]\vert\Phi\rangle\,e ,
\tag{21.13}
$$

with $\langle\Phi\vert[W,Y_1]\vert\Phi\rangle=2tU\operatorname{Re}\sum_m\bigl(\Phi^*_{mm}\Phi_{m+1,m}-\Phi^*_{m,m+1}\Phi_{m+1,m+1}\bigr)$, where $\Phi_{mn}$ is the weight of $\lvert h_mk_n\rangle$. **Moment bounds:** none are needed. For finite support every sum over places is finite, and a long finite chain gives the same values at $\lambda=0$. The limits below involve only the bounded operators $C_{\rm body}$, $C_{\rm hop}$, $Y_i$ and $[W,Y_i]$.

### Step 8. Composite at rest, and one body (items 4(b), 4(c))

Write $C_{\rm body}=C_{\rm hop}+UQ$ with $Q:=\sum_m\lvert h_mk_m\rangle\langle h_mk_m\rvert$, and let $E_{\min}(s,U)$ be the bottom of the spectrum with $t\to s$. By the variational principle, $E_{\min}(s,U)=\inf_\Phi\langle (s/t)C_{\rm hop}+UQ\rangle_\Phi$. Finite-support vectors are dense, so sequences as in (b) exist. Let $\delta_n:=\langle C_{\rm body}\rangle_{\Phi_n}-E_{\min}(t,U)\to0$. For every $s>0$,

$$E_{\min}(s,U)-E_{\min}(t,U)\le\delta_n+\tfrac{s-t}{t}\langle C_{\rm hop}\rangle_{\Phi_n}.$$

Divide by $s-t$ (for $s>t$ and for $s<t$), let $n\to\infty$, and then $s\to t$. Since $E_{\min}$ is differentiable in $t$, this gives

$$
\lim_{n\to\infty}\langle C_{\rm hop}\rangle_{\Phi_n}=t\,\partial_tE_{\min}(t,U)=-\frac{16t^2}{\sqrt{U^2+16t^2}}
\tag{21.14}
$$

for every such sequence. By (21.13), $\mu_c$ converges to $I_c^{-1}\hat e\,g(\hat e,\cdot)$, **independently of the sequence**.

For one body, (20.10) on the chain gives $\mu=-\langle C_1\rangle e\,g(e,\cdot)$ (because $\sum_EL=\langle C_1\rangle$ and $\Delta=-e$). The infimum $\inf\operatorname{spec}C_1=-2t$ is standard (the spectrum is $[-2t,2t]$). Hence:

$$
I_c(t,U,\sigma_X)=\frac{\sqrt{U^2+16t^2}}{4t^2\sigma_X^2},\qquad I_1=\frac{1}{2t\sigma_X^2},\qquad I_c(t,0,\sigma_X)=\frac{1}{t\sigma_X^2}=2I_1,\qquad \frac{I_c}{2I_1}=\sqrt{1+\frac{U^2}{16t^2}} .
\tag{21.15}
$$

So $I_c>2I_1$ for $U<0$: the binding makes the edge costs of the joint ground state less negative, $\lvert\lim\langle C_{\rm hop}\rangle\rvert<4t$.

### Step 9. Binding and inertia (item 4(d))

From (21.12), $E_{\rm bind}=4t-\sqrt{U^2+16t^2}<0$; from (17.20), $v_{\max}^2=4t^2\sigma_X^2$. Then (21.15) gives

$$
I_c-2I_1=\frac{\sqrt{U^2+16t^2}-4t}{4t^2\sigma_X^2}=-\frac{E_{\rm bind}}{v_{\max}^2},
\tag{21.16}
$$

$$
I_c\,v_{\max}^2=\sqrt{U^2+16t^2}=-E_{\min}(t,U).
\tag{21.17}
$$

Both are functions of the stated quantities alone. **Invariance under $C\to C+c\mathbb 1$.** $\Psi(\lambda)$ only acquires the common phase $e^{-ic\lambda}$, so by (1.2) no view changes. $u$, $t$ and $\sigma_X$ are unchanged, so $I_c$, $I_1$ and $v_{\max}$ are unchanged. If $c$ is placed in $C_{\rm body}$ (for example $W_{hk}\to W_{hk}+c$), then $E_{\min}\to E_{\min}+c$, and (21.17) fails for $c\neq0$. If $c$ is placed in the records (A5), $E_{\min}$ is unchanged. So $E_{\min}$ itself depends on a convention, and (21.17) holds only in the normalization of the example (zero diagonal of $C_1$ and $C_2$, $W=0$ off $m=n$). $E_{\rm bind}$ is a difference, unchanged when the same $c$ is added in the same placement at $U$ and at $U=0$. So (21.16) is invariant.

### Step 10. Limit of the $W$-terms (item 4(e))

$C_{\rm body}=C_1+C_2+W$, $[C_1,Y_1]=0$ and $[C_2,Y_1]=0$, so $[W,Y_1]=[C_{\rm body},Y_1]$. Let $\Gamma:=C_{\rm body}-E_{\min}\ge0$, which is bounded with $\lVert\Gamma\rVert=4t-E_{\min}$. Since $\Gamma^2\le\lVert\Gamma\rVert\,\Gamma$,

$$
\bigl\lvert\langle\Phi\vert[W,Y_i]\vert\Phi\rangle\bigr\rvert=\bigl\lvert\langle\Gamma\Phi\vert Y_i\Phi\rangle-\langle Y_i^\dagger\Phi\vert\Gamma\Phi\rangle\bigr\rvert\le4t\sqrt{\lVert\Gamma\rVert\,\langle\Phi\vert\Gamma\vert\Phi\rangle}\ \xrightarrow{\ (b)\ }\ 0,
\qquad\text{so}\qquad \lim A_W(0)=0 .
\tag{21.18}
$$

With $F=-\langle X\rangle e/\sigma_X^2$ from (20.12), (21.13) gives $\mu_cF_{\rm tot}=-\tfrac14\langle C_{\rm hop}\rangle e\,g(e,2F)=\tfrac12\langle C_{\rm hop}\rangle\langle X\rangle e$. Hence $A(0)-\mu_cF_{\rm tot}=A_W(0)$ exactly, for every start of finite support. By (21.14) and (21.18), **yes**: $\lim A(0)=\lim\mu_cF_{\rm tot}=-\dfrac{8t^2\langle X\rangle}{\sqrt{U^2+16t^2}}\,e$.

## Result

1. **Well-definedness.** $\bar R$, $A$ and $\mu_c$ are invariant under every rewriting (21.2) of $C$. These rewritings include the split (16.3) and every placement of single-object terms (A5), diagonal or not and in any pair term: every such placement leaves the total $C$ and its blocks unchanged, and (21.2) covers it (Step 2). They are also invariant under the common phase, up to the global isometry $R_\theta$ of the background. The phase split (1.6) does not enter. $\bar x_1-\bar x_2$ is **not** well defined (21.3).
2. **Acceleration of the centre.** (20.6)–(20.7) apply to each body. The exact $A(\lambda)$ is (21.4); $W$ appears explicitly only in (21.5). The closed form of $A(0)$ is (21.6), with $W$-terms (21.7). They do not vanish for every $\Phi$. Sufficient conditions for their vanishing are (21.8), or an eigenvector of $C_{\rm body}$ whose $W$-free terms add up to zero (21.9).
3. **Inertia of the composite.** $\mu_c=\tfrac14(\mu_1+\mu_2)$ (21.10). It is a function of $L^{(1)}(0)$, $L^{(2)}(0)$ and the backgrounds alone, has no explicit dependence on $W$, and is $g$-symmetric. It is positive semidefinite if and only if (21.11) holds, and in particular if all edge costs are $\le0$.
4. **Chain.** The spectrum is (21.12), with $E_{\min}=-\sqrt{U^2+16t^2}$. The scalar inertias $I_c=\sqrt{U^2+16t^2}/(4t^2\sigma_X^2)$, $I_1=1/(2t\sigma_X^2)$ and $I_c(U=0)=2I_1$ do not depend on the sequence (21.15). The binding raises the inertia: $I_c-2I_1=-E_{\rm bind}/v_{\max}^2$ (21.16), which is invariant. $I_cv_{\max}^2=-E_{\min}$ (21.17) is not invariant under $C\to C+c\mathbb 1$. $\lim A_W(0)=0$ and $\lim A(0)=\lim\mu_cF_{\rm tot}$ (21.18).

**Answer to the goal.** The composite's inverse inertia is fixed by the parts' inverse inertias, evaluated in the joint start (21.10). The binding cost contributes no explicit term. It acts only through the state, by changing the parts' edge costs, and on the chain this gives (21.16).

## Consistency checks

1. **$U=0$ (two independent bodies).** Each $\langle C_i\rangle\ge-2t$ and the sum tends to $-4t$, so each tends to $-2t$. Then (21.10) gives $\mu_c\to\tfrac14(2+2)t\sigma_X^2\hat e\,g(\hat e,\cdot)$, so $I_c=2I_1$, in agreement with (21.15) at $U=0$; also $A_W\equiv0$.
2. **Strong binding $\lvert U\rvert\gg t$.** By (21.12), $E_b(K)\approx U+\tfrac{4t^2}{U}(1+\cos K)$. This is the band of a single body on the pair places $\lvert h_mk_m\rangle$ (centre $me$) with hopping $2t^2/U$. That body feels the gradient $2\Omega_m$, that is, the force $F_{\rm tot}$. The one-body result gives $I=\lvert U\rvert/(4t^2\sigma_X^2)$, which is the limit of (21.15).
3. **Dimensions.** Set $[C]=[\lambda]^{-1}=:\nu$. Then $t,U,X,\sigma_X,u,\bar x\sim\nu$, $F\sim1$ and $A\sim\nu^3$. In (21.10), $\mu_c\sim L\,\Delta^2\sim\nu^3$, and indeed $I_c^{-1}\sim\nu^3$ in (21.15). Both sides of (21.16) are $\sim\nu^{-3}$.

## Open issues

- $\mu_c$ is the response at $\lambda=0$ only. Whether the composite then moves as one body for $\lambda>0$ is out of scope.
- The separation of two bodies recorded in one medium is not defined (21.3). A relative position would need structure beyond this setting.
- The split of $A(0)$ into $A_W$ and the rest, and $E_{\min}$ itself, depend on the placement convention (A5). Only $A(0)$, $\mu_c$ and $E_{\rm bind}$ (under a common shift) are invariant.
- Relation (21.16) is established only for the chain example.

## Methods used

- block decomposition of $C$ for a one-object part; branch vectors and views
- description freedom (A5, M6) via operator matrix elements
- current identity and its $\lambda$-derivative (20.6)–(20.7)
- linear response at $\lambda=0$ to a uniform gradient
- Heisenberg commutators with the position operator on $\ell^2(\mathbb Z)$
- separation into total and relative quasi-momentum; single-impurity bound state
- variational principle; Hellmann–Feynman for approximate minimizers (one-sided difference quotients)
- operator inequality $\Gamma^2\le\lVert\Gamma\rVert\Gamma$ for bounded $\Gamma\ge0$
