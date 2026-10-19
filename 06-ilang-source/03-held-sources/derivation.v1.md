# Held sources: field change, mutual cost and its sign

- **Subproject:** 06-ilang-source
- **Package:** 03-held-sources
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-19

## Setup and assumptions

- **Description (M8).** Objects $`b_1,b_2,f`$, each the only instance of its type. No swap condition (1.11) applies, so $`\mathcal H_{\rm adm}=\mathcal H=\mathcal H_{b_1}\otimes\mathcal H_{b_2}\otimes\mathcal H_f`$ (1.4). The field has a self-adjoint contract $`C_f`$ and self-adjoint operators $`\Phi_x`$, $`x\in X_f`$. Body $`b_i`$ is held at $`x_i\in X_f`$, $`x_1\neq x_2`$ (A15). It is coupled by $`G_i\otimes\Phi_{x_i}`$ with $`G_i`$ self-adjoint and has no other contract. $`C_f`$ is included as $`C_f\otimes\mathbb 1`$ in one of the two pair terms (A5; the sum does not depend on which), so
```math
C=\mathbb 1\otimes\mathbb 1\otimes C_f+G_1\otimes\mathbb 1\otimes\Phi_{x_1}+\mathbb 1\otimes G_2\otimes\Phi_{x_2}.
\qquad\text{(3.1)}
```
- **Spectral notation.** $`C_f\varphi_n=e_n\varphi_n`$ for an orthonormal eigenbasis $`\{\varphi_n\}`$. The distinct eigenvalues (levels) are $`\epsilon_1<\dots<\epsilon_L`$, with spectral projectors $`P_\ell`$ and multiplicities $`d_\ell`$. Further $`\bar\Phi_n(x)=\langle\varphi_n\vert\Phi_x\vert\varphi_n\rangle`$, the coupling $`V=g_1\Phi_{x_1}+g_2\Phi_{x_2}`$ and its size $`v=\lvert g_1\rvert\lVert\Phi_{x_1}\rVert+\lvert g_2\rvert\lVert\Phi_{x_2}\rVert\ge\lVert V\rVert`$. The gap of the level of $`e_n`$ is $`\Delta_n=\min\{\lvert e_m-e_n\rvert:e_m\neq e_n\}`$, and $`\Delta_{\min}=\min_n\Delta_n`$.
- **Cost.** The bodies have no other contract, so the cost of the field part is the total cost (1.8), which is well defined (M6). $`E_n(g_1,g_2)`$ is the eigenvalue of $`C_f(g_1,g_2)`$ (3.2) connected to $`e_n`$. It is the cost of the corresponding eigenvector $`\varphi_n(g)`$, called the *adapted* state.
- **Mutual term** (as in the question). It is the part of $`E_n`$ that depends on both $`g_1`$ and $`g_2`$; through second order, the $`g_1g_2`$ term. Its sign for $`g_1g_2>0`$ is the sign of the mutual cost of like sources. Reading this sign as "lower cost close together" presupposes that the mutual term vanishes for far-apart sources, which is a property of the profile (04-profile, out of scope).
- **Reference split.** Expansions are around $`g_1=g_2=0`$ in the split of $`C`$ fixed by the setting. The shift $`\Phi_x\to\Phi_x+c_x\mathbb 1`$, with the term $`-c_xG_i`$ moved to $`b_i`$, changes only first-order terms, and the response functions below are invariant under it. The shift $`G_i\to G_i+c`$, $`C_f\to C_f-c\Phi_{x_i}`$ moves the expansion point (Open issues).
- **Mixtures (extension of the setting, M8).** Take weights $`p_n=p(e_n)\ge0`$ with $`\sum_np_n=1`$, and write $`p_\ell`$ for the weight per eigenvector of level $`\ell`$. The mutual term $`W_\rho`$ of $`\rho=\sum_np_n\lvert\varphi_n\rangle\langle\varphi_n\rvert`$ is the mutual term of $`\sum_\ell p_\ell\,(\text{sum of the branches of level }\ell)`$. This is the cost of $`\beta\otimes\sum_n\sqrt{p_n}\,\tilde\varphi_n\otimes\eta_n`$, where the $`\tilde\varphi_n`$ are the eigenvectors of $`C_f(g)`$ that continue the $`\varphi_n`$, $`r`$ is an added object without contract terms, and the $`\eta_n\in\mathcal H_r`$ are orthonormal. On such a state $`C`$ acts as $`\mathbb 1`$ on $`r`$.
- **Regime (A13).** The perturbative results hold for $`v<\Delta_n/2`$ (one eigenvector or level) or for $`v<\Delta_{\min}/2`$ (mixtures), with the remainders stated. (3.3)–(3.5), the exact form of (3.14), (3.15), (3.18) and (3.19) are exact.

## Derivation

### Step 1. Reduction (item 1)

$`G_1\otimes\mathbb 1\otimes\mathbb 1`$ commutes with every term of (3.1): it acts on $`b_1`$ alone, and the only term acting on $`b_1`$ is $`G_1\otimes\mathbb 1\otimes\Phi_{x_1}`$. The same holds for $`G_2`$. Let $`\mathcal B_g=\mathcal E^{(1)}_{g_1}\otimes\mathcal E^{(2)}_{g_2}`$ be a joint eigenspace of $`(G_1,G_2)`$. Then $`\mathcal B_g\otimes\mathcal H_f`$ is invariant under $`C`$, and $`C(\beta\otimes\varphi)=\beta\otimes C_f(g_1,g_2)\varphi`$ for $`\beta\in\mathcal B_g`$, with
```math
C_f(g_1,g_2)=C_f+g_1\Phi_{x_1}+g_2\Phi_{x_2}.
\qquad\text{(3.2)}
```
By (1.9), for every $`\beta\in\mathcal B_g`$ and every $`\varphi\in\mathcal H_f`$,
```math
\lvert\Psi(\lambda)\rangle=\beta\otimes e^{-iC_f(g_1,g_2)\lambda}\varphi\qquad\text{for all }\lambda\in\mathbb R .
\qquad\text{(3.3)}
```
This includes the starts of the setting, $`\beta=\chi_1\otimes\chi_2`$ with $`G_i\chi_i=g_i\chi_i`$. For a general body start $`\beta=\sum_g\beta_g`$ with $`\beta_g\in\mathcal B_g`$, linearity (Law 3) gives
```math
\lvert\Psi(\lambda)\rangle=\sum_g\beta_g\otimes\varphi_g(\lambda),\qquad V_f(\Psi(\lambda))=\sum_g\lVert\beta_g\rVert^2\,\lvert\varphi_g(\lambda)\rangle\langle\varphi_g(\lambda)\rvert,\qquad \varphi_g(\lambda)=e^{-iC_f(g)\lambda}\varphi .
\qquad\text{(3.4)}
```
The cross terms of the view vanish because the $`\mathcal B_g`$ are orthogonal (1.7). The field is then a witness of the values $`g`$, and its view is in general not pure.

$`C`$ does not depend on $`\lambda`$, so the cost is conserved. In (3.3) it is
```math
E(\varphi;g_1,g_2)=\langle\varphi\vert C_f\vert\varphi\rangle+g_1\langle\varphi\vert\Phi_{x_1}\vert\varphi\rangle+g_2\langle\varphi\vert\Phi_{x_2}\vert\varphi\rangle\qquad\text{exactly, for all }\lambda .
\qquad\text{(3.5)}
```
A field start that does not depend on $`(g_1,g_2)`$ therefore carries no mutual term at any order. A mutual cost needs a field state that depends on the sources, such as an adapted state, and the language selects none (A11).

### Step 2. A non-degenerate eigenvector (item 2)

Let $`e_n`$ be non-degenerate, and define
```math
Q_n=\sum_{m:\,e_m\neq e_n}\frac{\lvert\varphi_m\rangle\langle\varphi_m\rvert}{e_m-e_n},\qquad
\chi_n(x,y)=\langle\varphi_n\vert\Phi_xQ_n\Phi_y+\Phi_yQ_n\Phi_x\vert\varphi_n\rangle
=\sum_{m:\,e_m\neq e_n}\frac{2\mathrm{Re}\bigl(\langle\varphi_n\vert\Phi_x\vert\varphi_m\rangle\langle\varphi_m\vert\Phi_y\vert\varphi_n\rangle\bigr)}{e_m-e_n}.
\qquad\text{(3.6)}
```

1. *Symmetry.* The two terms of $`\chi_n`$ are complex conjugates of each other, so $`\chi_n(x,y)=\chi_n(y,x)\in\mathbb R`$. $`Q_n`$ depends only on the spectral projectors of $`C_f`$, and $`Q_n\varphi_n=0`$. Hence $`\chi_n`$ depends neither on the phases or the basis chosen in other levels nor on shifts $`\Phi_x\to\Phi_x+c_x\mathbb 1`$.
2. *Expansion.* By Weyl's inequality, every eigenvalue of $`C_f(g)`$ lies within $`\lVert V\rVert\le v`$ of an eigenvalue of $`C_f`$. For $`v<\Delta_n/2`$, exactly one lies within $`\Delta_n/2`$ of $`e_n`$. By standard perturbation theory of an isolated simple eigenvalue it is simple, analytic in $`(g_1,g_2)`$ and given by the Rayleigh–Schrödinger series; this eigenvalue is $`E_n(g)`$. Through second order, $`E_n=e_n+\langle\varphi_n\vert V\vert\varphi_n\rangle-\langle\varphi_n\vert VQ_nV\vert\varphi_n\rangle`$. Symmetrising $`\langle\varphi_n\vert VQ_nV\vert\varphi_n\rangle=\sum_{i,j}g_ig_j\langle\varphi_n\vert\Phi_{x_i}Q_n\Phi_{x_j}\vert\varphi_n\rangle`$ in $`i\leftrightarrow j`$ gives
```math
E_n(g_1,g_2)=e_n+\sum_{i=1,2}\Bigl(g_i\bar\Phi_n(x_i)-\tfrac12g_i^2\chi_n(x_i,x_i)\Bigr)-g_1g_2\,\chi_n(x_1,x_2)+O\Bigl(\frac{v^3}{\Delta_n^2}\Bigr).
\qquad\text{(3.7)}
```
The second-order self term of source $`i`$ and the mutual term are
```math
\Sigma_{n,i}=-\tfrac12g_i^2\chi_n(x_i,x_i),\qquad W_n=-g_1g_2\,\chi_n(x_1,x_2).
\qquad\text{(3.8)}
```
3. *Change of the field.* Through first order the adapted eigenvector is $`\varphi_n(g)=\varphi_n-Q_nV\varphi_n+O(v^2/\Delta_n^2)`$. Hence, for every $`y\in X_f`$,
```math
\langle\varphi_n(g)\vert\Phi_y\vert\varphi_n(g)\rangle=\bar\Phi_n(y)+\delta N_n^{(1)}(y)+\delta N_n^{(2)}(y)+O\Bigl(\frac{\lVert\Phi_y\rVert v^2}{\Delta_n^2}\Bigr),\qquad \delta N_n^{(i)}(y)=-g_i\,\chi_n(y,x_i).
\qquad\text{(3.9)}
```
$`\delta N^{(i)}_n`$ is the field made by source $`i`$. By the symmetry of $`\chi_n`$ it is reciprocal: $`\delta N^{(1)}_n(x_2)/g_1=\delta N^{(2)}_n(x_1)/g_2`$.

The same field appears on average from the unadapted start $`\varphi_n`$ of (3.3). Write $`\varphi_n=\sum_kc_k\varphi_k(g)`$ in an eigenbasis of $`C_f(g)`$. Then $`\lvert c_n\rvert^2=1-O(v^2/\Delta_n^2)`$, and the remaining components have norm $`O(v/\Delta_n)`$. Since $`E_n(g)`$ is simple, the average $`\lim_{\Lambda\to\infty}\Lambda^{-1}\int_0^\Lambda\langle\Phi_y\rangle_\lambda\,\mathrm d\lambda`$ keeps only $`\lvert c_n\rvert^2\langle\varphi_n(g)\vert\Phi_y\vert\varphi_n(g)\rangle`$ and terms $`c_k^*c_l`$ with $`k,l\neq n`$. It therefore equals (3.9) up to $`O(\lVert\Phi_y\rVert v^2/\Delta_n^2)`$. The cost of this start stays (3.5), without a mutual term.

### Step 3. A degenerate eigenvector (item 2)

Let $`e_n=\epsilon_\ell`$ have multiplicity $`d_\ell\ge2`$, and let $`Q_\ell`$ be the operator $`Q_n`$ of (3.6) for this level. For $`v<\Delta_n/2`$, $`C_f(g)`$ has exactly $`d_\ell`$ eigenvalues within $`\Delta_n/2`$ of $`\epsilon_\ell`$ (Weyl). By second-order quasi-degenerate (Schrieffer–Wolff) perturbation theory, these are, up to $`O(v^3/\Delta_n^2)`$, the eigenvalues of the Hermitian operator on $`P_\ell\mathcal H_f`$
```math
H_\ell(g)=\epsilon_\ell P_\ell+P_\ell VP_\ell-P_\ell VQ_\ell VP_\ell .
\qquad\text{(3.10)}
```
1. "Connected to $`e_n`$" names $`d_\ell`$ branches, and a vector $`\varphi_n`$ of the level does not select one of them.
2. Through first order, the branches are $`\epsilon_\ell`$ plus the eigenvalues of $`g_1A_1+g_2A_2`$, with $`A_i=P_\ell\Phi_{x_i}P_\ell`$. For $`d_\ell=2`$, write $`A_i=\alpha_iP_\ell+\vec a_i\cdot\vec\sigma`$ in an orthonormal basis of the level. Then
```math
E_{\ell,\pm}(g)=\epsilon_\ell+g_1\alpha_1+g_2\alpha_2\pm\lvert g_1\vec a_1+g_2\vec a_2\rvert+O\Bigl(\frac{v^2}{\Delta_n}\Bigr).
\qquad\text{(3.11)}
```
Suppose $`\vec a_1,\vec a_2`$ are non-zero and not parallel, i.e. $`[A_1,A_2]\neq0`$. Then $`\lvert g_1\vec a_1+g_2\vec a_2\rvert<\lvert g_1\rvert\lvert\vec a_1\rvert+\lvert g_2\rvert\lvert\vec a_2\rvert`$ for $`g_1g_2\neq0`$. Each branch then depends on both sources already at first order, not additively, and it is not differentiable at $`g=0`$. There is no expansion of the form (3.7) and no mutual term $`\propto g_1g_2`$. If instead $`[A_1,A_2]=0`$, the branches can be chosen in a joint eigenbasis as $`\epsilon_\ell+g_1a_{1\alpha}+g_2a_{2\alpha}`$, which is additive at first order (control).
3. The sum of the $`d_\ell`$ branches is the trace of $`C_f(g)`$ times the total spectral projector of the group. That projector is analytic in $`g`$, so the sum is analytic. Through second order the sum is $`\mathrm{Tr}H_\ell(g)`$, whose mutual term is $`-g_1g_2\chi^{(\ell)}(x_1,x_2)`$ with the level response
```math
\chi^{(\ell)}(x,y)=\mathrm{Tr}\bigl[P_\ell(\Phi_xQ_\ell\Phi_y+\Phi_yQ_\ell\Phi_x)\bigr]=\sum_{n:\,e_n=\epsilon_\ell}\chi_n(x,y).
\qquad\text{(3.12)}
```
The sum runs over any orthonormal basis of the level, with $`\chi_n`$ computed by (3.6). For $`d_\ell=1`$, $`\chi^{(\ell)}=\chi_n`$.

### Step 4. Sums over eigenvectors (item 3)

For weights $`p_n=p(e_n)`$, set $`\chi_\rho=\sum_np_n\chi_n=\sum_\ell p_\ell\chi^{(\ell)}`$, so that $`W_\rho=-g_1g_2\chi_\rho(x_1,x_2)`$ for $`v<\Delta_{\min}/2`$. The products $`\langle\varphi_m\vert\Phi_x\vert\varphi_n\rangle\langle\varphi_n\vert\Phi_y\vert\varphi_m\rangle`$ and $`\langle\varphi_n\vert\Phi_x\vert\varphi_m\rangle\langle\varphi_m\vert\Phi_y\vert\varphi_n\rangle`$ are complex conjugates. So the term of $`\varphi_n`$ in $`\chi_m`$ has the same real part as the term of $`\varphi_m`$ in $`\chi_n`$, with the opposite denominator. Collecting each pair once gives
```math
\chi_\rho(x,y)=\sum_{(n,m):\,e_n<e_m}\frac{2(p_n-p_m)}{e_m-e_n}\mathrm{Re}\bigl(\langle\varphi_n\vert\Phi_x\vert\varphi_m\rangle\langle\varphi_m\vert\Phi_y\vert\varphi_n\rangle\bigr).
\qquad\text{(3.13)}
```
With equal weights, every coefficient vanishes.

Let a subspace $`\mathcal K`$ be invariant under $`C_f`$ and all $`\Phi_x`$. Then $`\mathcal K^\perp`$ is invariant as well, the eigenbasis can be chosen in $`\mathcal K\cup\mathcal K^\perp`$, and $`\langle\varphi_n\vert\Phi_x\vert\varphi_m\rangle=0`$ between the two. Hence only pairs inside $`\mathcal K`$ enter $`\sum_{\varphi_n\in\mathcal K}\chi_n`$, and they enter with equal weights. For all $`x,y\in X_f`$:
```math
\sum_n\chi_n(x,y)=\sum_\ell\chi^{(\ell)}(x,y)=0,\qquad\sum_{n:\,\varphi_n\in\mathcal K}\chi_n(x,y)=0 .
\qquad\text{(3.14)}
```
The exact form: the sum of all eigenvalues of $`C_f(g)`$ is $`\mathrm{Tr}C_f(g)`$, and the sum of those on $`\mathcal K`$ is $`\mathrm{Tr}_{\mathcal K}C_f(g)`$. Both are linear in $`(g_1,g_2)`$ for all $`g`$, so the sum over all branches (over the branches on $`\mathcal K`$) has no mutual part at any order.

### Step 5. The two ends of the spectrum (item 3)

Let $`U`$ be unitary on $`\mathcal H_f`$ with $`UC_fU^\dagger=-C_f`$ and $`U\Phi_xU^\dagger=\epsilon_x\Phi_x`$, $`\epsilon_x\in\{+1,-1\}`$. Then $`UC_f(g_1,g_2)U^\dagger=-C_f(-\epsilon_{x_1}g_1,-\epsilon_{x_2}g_2)`$. $`U`$ maps the level $`\epsilon_\ell`$ to the level $`-\epsilon_\ell`$, and the lowest level to the highest.

For non-degenerate $`\varphi_n`$, the vector $`\varphi_{\bar n}=U\varphi_n`$ is a non-degenerate eigenvector with $`e_{\bar n}=-e_n`$. The number $`-E_n(-\epsilon_{x_1}g_1,-\epsilon_{x_2}g_2)`$ is an eigenvalue of $`C_f(g)`$, continuous in $`g`$ and equal to $`-e_n`$ at $`g=0`$; for $`v<\Delta_n/2`$ it is therefore $`E_{\bar n}(g)`$. Comparing the $`g_1g_2`$ terms of (3.7), and using $`Q_{\bar n}=-UQ_nU^\dagger`$ for general $`x,y`$, gives
```math
E_{\bar n}(g_1,g_2)=-E_n(-\epsilon_{x_1}g_1,-\epsilon_{x_2}g_2),\qquad\chi_{\bar n}(x,y)=-\epsilon_x\epsilon_y\,\chi_n(x,y),\qquad W_{\bar n}=-\epsilon_{x_1}\epsilon_{x_2}W_n .
\qquad\text{(3.15)}
```
The level responses obey the same relation, $`\chi^{(\bar\ell)}=-\epsilon_x\epsilon_y\chi^{(\ell)}`$. If $`\epsilon_{x_1}=\epsilon_{x_2}`$, the mutual terms at the two ends of the spectrum are opposite; if $`\epsilon_{x_1}=-\epsilon_{x_2}`$, they are equal. The self terms at the two ends are always opposite.

### Step 6. Ordered mixtures (item 3)

If $`p`$ is non-increasing in $`e`$, every coefficient in (3.13) is $`\ge0`$. For real $`c_x`$ and $`\Phi_c=\sum_xc_x\Phi_x`$, (3.13) gives $`\sum_{x,y}c_xc_y\chi_\rho(x,y)=\sum_{e_n<e_m}\frac{2(p_n-p_m)}{e_m-e_n}\lvert\langle\varphi_n\vert\Phi_c\vert\varphi_m\rangle\rvert^2`$. Set $`\Sigma_{\rho,i}=-\frac12g_i^2\chi_\rho(x_i,x_i)`$. Using the $`2\times2`$ principal minor at $`x_1,x_2`$:
```math
\bigl[\chi_\rho(x,y)\bigr]_{x,y\in X_f}\succeq0\ \ (p\text{ non-increasing}),\qquad\preceq0\ \ (p\text{ non-decreasing});\qquad W_\rho^2\le4\,\Sigma_{\rho,1}\Sigma_{\rho,2}.
\qquad\text{(3.16)}
```
For non-increasing weights the self terms lower the cost ($`\Sigma_{\rho,i}\le0`$); for non-decreasing weights they raise it. The lowest (highest) non-degenerate eigenvector is the case where $`p`$ is concentrated on it.

The sign of the mutual term follows from Abel summation. Let $`S_k=\sum_{\ell\le k}\chi^{(\ell)}(x_1,x_2)`$; by (3.14), $`S_L=0`$. Then
```math
\chi_\rho(x_1,x_2)=\sum_{k=1}^{L-1}(p_k-p_{k+1})\,S_k .
\qquad\text{(3.17)}
```
For non-increasing weights all coefficients are $`\ge0`$. Hence $`W_\rho`$ has one weak sign for all non-increasing mixtures iff $`S_1,\dots,S_{L-1}`$ have one weak sign. The "if" follows from (3.17). The "only if" holds because the equal-weight mixture of levels $`1,\dots,k`$ has $`\chi_\rho(x_1,x_2)=S_k/\sum_{\ell\le k}d_\ell`$. For $`g_1g_2>0`$, that sign of $`W_\rho`$ is opposite to the sign of the $`S_k`$. For non-decreasing weights, $`\chi_\rho(x_1,x_2)=-\sum_k(p_{k+1}-p_k)S_k`$, which gives the opposite sign. The ordering alone does not fix the mutual sign: replacing $`\Phi_{x_2}`$ by $`-\Phi_{x_2}`$ reverses every $`S_k`$ and leaves (3.16) intact.

### Step 7. Sharp and responding (item 4)

1. *Sharp eigenvector.* Let a non-degenerate $`\varphi_n`$ be sharp at $`x`$, $`\Phi_x\varphi_n=N(x)\varphi_n`$. Then $`\langle\varphi_m\vert\Phi_x\vert\varphi_n\rangle=0`$ for $`m\neq n`$, and (3.6) gives $`\chi_n(x,y)=\chi_n(y,x)=0`$ for every $`y`$. By (3.9), a source at $`x`$ then makes no field and feels none at second order. If $`\varphi_n`$ is sharp at both $`x_1`$ and $`x_2`$, then $`C_f(g)\varphi_n=(e_n+g_1N(x_1)+g_2N(x_2))\varphi_n`$ for all $`g`$. Hence
```math
E_n(g_1,g_2)=e_n+g_1N(x_1)+g_2N(x_2),\qquad e^{-iC_f(g)\lambda}\varphi_n=e^{-iE_n(g)\lambda}\varphi_n,\qquad\chi_n\equiv0\ \text{ if }\varphi_n\text{ is sharp at all }x .
\qquad\text{(3.18)}
```
The first two equations are exact. The first is an eigenvalue for all $`g`$, and for $`v<\Delta_n/2`$ it is the branch $`E_n`$.
2. *Sharp along the evolution.* Suppose $`\varphi(\lambda)=e^{-iC_f\lambda}\varphi`$ satisfies $`\Phi_{x_i}\varphi(\lambda)=N_i(\lambda)\varphi(\lambda)`$ for $`i=1,2`$ and all $`\lambda`$. The $`N_i`$ are constant, since they are continuous and take values in the finite spectrum of $`\Phi_{x_i}`$. The vector $`e^{-i(g_1N_1+g_2N_2)\lambda}\varphi(\lambda)`$ solves $`i\,\mathrm d\psi/\mathrm d\lambda=C_f(g)\psi`$ with start $`\varphi`$, so by uniqueness
```math
e^{-iC_f(g_1,g_2)\lambda}\varphi=e^{-i(g_1N_1+g_2N_2)\lambda}\,e^{-iC_f\lambda}\varphi\qquad\text{for all }\lambda .
\qquad\text{(3.19)}
```
The same follows if the evolution with the sources stays sharp at $`x_1`$ and $`x_2`$. So the sources change a field state that stays sharp at both of their places only by a common phase (1.2), and its cost is (3.5) with $`\langle\Phi_{x_i}\rangle=N_i`$. A field state therefore cannot stay sharp at the places of both bodies and respond to them. Control: the lowest eigenvector of the two-place field (check 2) is not sharp and responds.
3. *Mutual and self terms.* From (3.8) and (3.9), for every non-degenerate eigenvector, and with $`\chi_\rho`$ in place of $`\chi_n`$ for every mixture,
```math
W_n=g_2\,\delta N^{(1)}_n(x_2)=g_1\,\delta N^{(2)}_n(x_1),\qquad\Sigma_{n,i}=\tfrac12g_i\,\delta N^{(i)}_n(x_i).
\qquad\text{(3.20)}
```
A source thus feels the full field made by the other source, and half of its own. For ordered mixtures, (3.16) bounds the mutual term by the self terms.

For an extreme non-degenerate eigenvector, $`Q_n`$ is definite on $`\varphi_n^\perp`$. Then $`\chi_n(x_i,x_i)=2\langle\delta_i\vert Q_n\vert\delta_i\rangle`$, with $`\delta_i=(\Phi_{x_i}-\bar\Phi_n(x_i))\varphi_n`$, vanishes iff $`\varphi_n`$ is sharp at $`x_i`$, and in that case $`W_n=0`$. For interior eigenvectors the bound does not hold in general. Take the field with places $`0,1,2`$ and
```math
C_f=\omega\bigl(\lvert2\rangle\langle2\rvert-\lvert0\rangle\langle0\rvert\bigr),\ \ \Phi_{x_{1,2}}=\lvert0\rangle\langle1\rvert\pm\lvert2\rangle\langle1\rvert+\text{h.c.},\ \ \omega>0:\qquad\chi_1(x_i,x_i)=0,\ \ \chi_1(x_1,x_2)=-\frac4\omega .
\qquad\text{(3.21)}
```
In its eigenvector $`\varphi_1=\lvert1\rangle`$, $`e_1=0`$, both self terms vanish, $`\Sigma_{1,1}=\Sigma_{1,2}=0`$, but $`W_1=4g_1g_2/\omega\neq0`$.

### Step 8. The sign as a condition on the state (item 5)

1. *Both signs.* By (3.14), for every field of the class and every $`x_1\neq x_2`$, either $`\chi^{(\ell)}(x_1,x_2)=0`$ for every level $`\ell`$, or
```math
\min_\ell\chi^{(\ell)}(x_1,x_2)<0<\max_\ell\chi^{(\ell)}(x_1,x_2).
\qquad\text{(3.22)}
```
So, at second order, $`C_f`$ and the $`\Phi_x`$ alone never fix the sign of the mutual cost of like sources, except in the case where it vanishes in every level. They fix:
   - the numbers $`\chi^{(\ell)}(x_1,x_2)`$ (3.12)–(3.13);
   - the partial sums $`S_k`$, and with them whether all non-increasing mixtures share one sign (3.17);
   - the relation between the two ends of the spectrum (3.15);
   - the sign of the self terms for ordered weights (3.16).

   The state fixes the rest:
   - which eigenvector or mixture the field is in;
   - whether the field state depends on the sources at all; if it does not, there is no mutual cost (3.5);
   - whether the state is sharp at a body's place; if it is, the mutual term vanishes at second order (3.18).
2. *Explicit field.* Take three places on a chain, $`H_f=X_f=\{1,2,3\}`$, with $`C_f=-t\bigl(\lvert1\rangle\langle2\rvert+\lvert2\rangle\langle3\rvert+\text{h.c.}\bigr)`$, $`t>0`$, and $`\Phi_x=\lvert x\rangle\langle x\rvert`$ (an assumption of the example, M8). The eigenvectors are $`\varphi_1=(\frac12,\frac1{\sqrt2},\frac12)`$, $`\varphi_2=(\frac1{\sqrt2},0,-\frac1{\sqrt2})`$ and $`\varphi_3=(\frac12,-\frac1{\sqrt2},\frac12)`$, with $`e=-\sqrt2t,\,0,\,\sqrt2t`$. Evaluating (3.6) gives
```math
\chi_1=\frac{1}{16\sqrt2\,t}\begin{pmatrix}5&-2&-3\\-2&4&-2\\-3&-2&5\end{pmatrix},\qquad\chi_3=-\chi_1,\qquad\chi_2=0 .
\qquad\text{(3.23)}
```
Here $`\chi_3=-\chi_1`$ is (3.15) with $`U=\mathrm{diag}(1,-1,1)`$ and $`\epsilon_x=+1`$, and $`\chi_2=0`$ then follows from (3.14). Let $`u=g_1g_2/(16\sqrt2\,t)>0`$ (like sources). The mutual terms are:
   - in $`\varphi_1`$: $`W=2u`$ at the neighbouring places $`(1,2)`$ and $`W=3u`$ at the end places $`(1,3)`$;
   - in $`\varphi_3`$: $`W=-2u`$ and $`W=-3u`$;
   - in $`\varphi_2`$: $`W=0`$.

   Between $`\varphi_1`$ and $`\varphi_3`$, both the sign of $`W`$ and the difference $`W(1,2)-W(1,3)`$ reverse: the difference is $`-u`$ in $`\varphi_1`$ and $`+u`$ in $`\varphi_3`$. Under either reading, one state gives like sources close together a lower cost and the other a higher one.

   The two readings differ in this field. $`\varphi_3`$ has a negative mutual cost, but the cost is lower at the larger separation. The reason is that $`\sum_x\Phi_x=\mathbb 1`$ and $`Q_n\varphi_n=0`$ give $`\sum_y\chi_n(x,y)=0`$, so the mutual term does not vanish at the larger separation. By (3.17), with $`S_1=S_2=\chi_1(x_1,x_2)`$, every non-increasing mixture has $`W_\rho=(p_1-p_3)W_{\varphi_1}`$.

## Result

- **(3.2), (3.3), (3.4)** (theorem, item 1). Class: every finite field and every $`C_f`$, $`\Phi_x`$, $`G_i`$ of the setting. Take any field start and a body start in one joint eigenspace of $`(G_1,G_2)`$, with eigenvalues $`(g_1,g_2)`$. The bodies stay in their start, and the field evolves by $`e^{-iC_f(g_1,g_2)\lambda}`$ with $`C_f(g_1,g_2)=C_f+g_1\Phi_{x_1}+g_2\Phi_{x_2}`$, exactly for all $`\lambda`$. For other body starts this holds branch by branch, and the field view is the mixture (3.4). This is an identity, with no control in the class.
- **(3.5)** (theorem). Same class and starts. The cost is exactly linear in $`(g_1,g_2)`$ and conserved. A field start that does not depend on the sources carries no mutual term at any order.
- **(3.6)** (definition). The response function $`\chi_n(x,y)`$ of a non-degenerate eigenvector, written with the reduced resolvent $`Q_n`$. It is real and symmetric, and it is independent of phases, of the basis chosen in other levels and of shifts $`\Phi_x\to\Phi_x+c_x\mathbb 1`$.
- **(3.7), (3.8)** (formula, item 2). Non-degenerate $`\varphi_n`$, $`v<\Delta_n/2`$: $`E_n=e_n+\sum_i(g_i\bar\Phi_n(x_i)+\Sigma_{n,i})+W_n+O(v^3/\Delta_n^2)`$. The self terms are $`\Sigma_{n,i}=-\frac12g_i^2\chi_n(x_i,x_i)`$ and the mutual term is $`W_n=-g_1g_2\chi_n(x_1,x_2)`$.
- **(3.9)** (formula). Same conditions. In the adapted eigenvector, source $`i`$ changes $`\langle\Phi_y\rangle`$ by $`\delta N^{(i)}_n(y)=-g_i\chi_n(y,x_i)`$, with remainder $`O(\lVert\Phi_y\rVert v^2/\Delta_n^2)`$, and this change is reciprocal. From the unadapted start $`\varphi_n`$, the $`\lambda`$-average of $`\langle\Phi_y\rangle`$ equals it to the same order, while the cost stays (3.5).
- **(3.10), (3.11), (3.12)** (formula and negative, item 2). Degenerate level, $`d_\ell\ge2`$, $`v<\Delta_n/2`$. There are $`d_\ell`$ branches; up to $`O(v^3/\Delta_n^2)`$ they are the eigenvalues of $`H_\ell(g)`$. For $`d_\ell=2`$ with $`[A_1,A_2]\neq0`$, each branch depends on both sources at first order, non-additively and non-differentiably at $`g=0`$, so it has no mutual term $`\propto g_1g_2`$. Control: $`[A_1,A_2]=0`$. The sum of the branches is analytic, with mutual term $`-g_1g_2\chi^{(\ell)}(x_1,x_2)`$, where $`\chi^{(\ell)}`$ is the level response.
- **(3.13), (3.14)** (theorem, item 3). For weights $`p(e_n)`$ and $`v<\Delta_{\min}/2`$, the pair formula (3.13) holds. For all $`x,y`$, $`\sum_n\chi_n(x,y)=0`$, and the same sum vanishes over the eigenvectors in any subspace invariant under $`C_f`$ and all $`\Phi_x`$. In exact form, the sum over all branches has no mutual part at any order. This is an identity, with no control.
- **(3.15)** (theorem, item 3). Class: fields with a unitary $`U`$, $`UC_fU^\dagger=-C_f`$, $`U\Phi_xU^\dagger=\epsilon_x\Phi_x`$, and non-degenerate $`\varphi_n`$, $`v<\Delta_n/2`$. Exactly, $`E_{U\varphi_n}(g_1,g_2)=-E_n(-\epsilon_{x_1}g_1,-\epsilon_{x_2}g_2)`$, $`\chi_{U\varphi_n}=-\epsilon_x\epsilon_y\chi_n`$ and $`W_{U\varphi_n}=-\epsilon_{x_1}\epsilon_{x_2}W_n`$. The mutual terms of the lowest and the highest eigenvector are opposite if $`\epsilon_{x_1}=\epsilon_{x_2}`$ and equal if $`\epsilon_{x_1}=-\epsilon_{x_2}`$. This is an identity in its class.
- **(3.16)** (theorem, item 3). Second order, $`v<\Delta_{\min}/2`$. For weights non-increasing (non-decreasing) in $`e`$, $`[\chi_\rho(x,y)]`$ is positive (negative) semidefinite, the self terms are $`\le0`$ ($`\ge0`$), and $`W_\rho^2\le4\Sigma_{\rho,1}\Sigma_{\rho,2}`$. For interior eigenvectors the bound can fail; (3.21) is the control.
- **(3.17)** (criterion, item 3). Same order. $`W_\rho`$ has one weak sign for all non-increasing mixtures iff the partial sums $`S_1,\dots,S_{L-1}`$ have one weak sign; non-decreasing mixtures then have the opposite sign. The ordering alone does not fix the sign; control: $`\Phi_{x_2}\to-\Phi_{x_2}`$.
- **(3.18), (3.19)** (theorem and negative, item 4). A non-degenerate eigenvector sharp at $`x`$ has $`\chi_n(x,\cdot)=0`$, and $`\chi_n\equiv0`$ if it is sharp at all $`x`$. If it is sharp at $`x_1`$ and $`x_2`$, $`E_n`$ is exactly linear and the field is unchanged up to a phase. A field state that stays sharp at $`x_1`$ and $`x_2`$ along its evolution is changed by the sources only by a phase, for all $`\lambda`$. So a field state cannot stay sharp at the places of both bodies and respond to them. Control: the non-sharp lowest eigenvector of the two-place field responds.
- **(3.20)** (formula, item 4). At second order, for every non-degenerate eigenvector and every mixture: $`W=g_2\delta N^{(1)}(x_2)=g_1\delta N^{(2)}(x_1)`$ and $`\Sigma_i=\frac12g_i\delta N^{(i)}(x_i)`$. For an extreme non-degenerate eigenvector, $`\chi_n(x_i,x_i)=0`$ iff the eigenvector is sharp at $`x_i`$, and then $`W_n=0`$.
- **(3.21)** (example). A three-place field whose interior eigenvector has zero self terms and a non-zero mutual term $`4g_1g_2/\omega`$.
- **(3.22)** (negative, item 5). For every field of the class and every $`x_1\neq x_2`$, at second order: either all level responses $`\chi^{(\ell)}(x_1,x_2)`$ vanish, or levels with both signs occur. The sign of the mutual cost of like sources is therefore never fixed by $`C_f`$ and the $`\Phi_x`$ alone, except in the case where it vanishes in every level. Those fix the level responses, the partial sums $`S_k`$, the relation between the ends of the spectrum and the sign of the self terms for ordered weights. The state fixes which eigenvector or mixture, whether the field depends on the sources at all, and whether it is sharp at a body's place.
- **(3.23)** (example, item 5). Three-place chain, second order. In the lowest eigenvector the mutual cost of like sources is $`2u>0`$ at neighbouring places and $`3u`$ at the end places. In the highest it is $`-2u`$ and $`-3u`$, and in the middle eigenvector it is $`0`$, with $`u=g_1g_2/(16\sqrt2t)`$. Both the sign and the neighbour-minus-end difference reverse between the lowest and the highest eigenvector.

## Consistency checks

1. **Dimensions and $`g_2=0`$.** $`g_i\Phi_x`$ is a cost and, by (3.6), $`\chi_n`$ has the dimension of $`\Phi^2/\text{cost}`$. Every term of (3.7) is therefore a cost. At $`g_2=0`$ the mutual term vanishes, and (3.7) becomes the one-source expansion. Passed.
2. **Two-place field.** Take $`C_f=-t\sigma_1`$ and $`\Phi_x=\lvert x\rangle\langle x\rvert`$. The exact eigenvalues are $`\frac{g_1+g_2}2\mp\sqrt{t^2+(g_1-g_2)^2/4}`$. The lowest expands to $`-t+\frac{g_1+g_2}2-\frac{(g_1-g_2)^2}{8t}`$, with mutual term $`+\frac{g_1g_2}{4t}`$ and self terms $`-\frac{g_i^2}{8t}`$. (3.6) gives the same: $`\chi(1,2)=-\frac1{4t}`$ and $`\chi(x,x)=\frac1{4t}`$. The highest eigenvalue has the opposite second-order terms, as required by (3.14) and by (3.15) with $`U=\sigma_3`$. The bound (3.16) holds with equality. Passed.
3. **$`\Phi_x`$ commuting with $`C_f`$.** A non-degenerate $`\varphi_n`$ is then an eigenvector of every $`\Phi_x`$, i.e. sharp. (3.6) gives $`\chi_n=0`$, and (3.7) reduces to $`e_n+\sum_ig_i\bar\Phi_n(x_i)`$, which is the exact eigenvalue, in agreement with (3.18). Passed.

## Open issues

- The zero of $`G_i`$ is a convention (M6). The shift $`G_i\to G_i+c`$, $`C_f\to C_f-c\Phi_{x_i}`$ leaves $`C`$ and the exact spectrum of $`C_f(g)`$ unchanged, but it changes the reference eigenvectors and the split into self and mutual terms. This is to be settled with 02-what-a-body-presents.
- No relaxation (A11). What, if anything, brings the field into an adapted state is open; in unadapted starts the cost has no mutual term (3.5).
- The dependence on distance, whether the mutual term vanishes for far-apart sources, and hence which reading of the sign applies, belong to 04-profile.
- For degenerate levels, only level sums carry an analytic mutual term. Orders above the second are not treated, except in the exact results.
- Mixtures are realised through an added object without contracts, which is an extension of the setting.

## Methods used

- reduction on joint eigenspaces of conserved operators
- Rayleigh–Schrödinger and quasi-degenerate (Schrieffer–Wolff) perturbation theory
- Weyl's inequality, reduced resolvent
- trace identities, Abel summation
- semidefinite matrices, Cauchy–Schwarz
- spectrum-reflecting unitary symmetry
