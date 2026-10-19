# Held sources: field change, mutual cost and its sign

- **Subproject:** 06-ilang-source
- **Package:** 03-held-sources
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-19

## Changes from previous version

- Step 9, item 1: new last bullet on $`G_i`$ or $`\Phi_{x_i}`$ a multiple of $`\mathbb 1`$: the writings outside (3.25), with the verifier's two-place example as control. Reason: I1.
- Step 9, items 2 and 4: sharpness at $`x_1,x_2`$ shown to be fixed by $`C`$ for $`G_i`$, $`\Phi_{x_i}`$ not multiples of $`\mathbb 1`$; the class [I] for sectors, sector operators and sharpness restricted to this case. Reason: I1.
- Result, entries (3.2)–(3.4), (3.5) and (3.18)–(3.19): invariance stated with this restriction; otherwise a statement in the stated split. Reason: I1.
- Step 9, item 2, and (3.27): the rank identification restricted to a non-degenerate $`e_n`$; a degenerate level gives a block of ranks, with the block sum as invariant quantity. Result entries (3.10)–(3.12) and (3.27) adjusted. Reason: I2.
- Step 7, item 3, and Result entry (3.20): the sentence on a source feeling half of its own field replaced by the split of the cost into pair terms and field term and by $`\partial E_n/\partial g_i`$. Reason: I3.

## Response to verification

- I1: Accepted and fixed in Step 9, items 1, 2 and 4, and in the Result entries (3.2)–(3.5) and (3.18)–(3.19). For $`G_i`$ and $`\Phi_{x_i}`$ not multiples of $`\mathbb 1`$ the writings are those of (3.25), which keep the eigenvectors of $`\Phi_{x_i}`$, and the exact statements at $`x_1,x_2`$ are [I]. Otherwise sharpness at $`x_i`$ and the response relative to the listed $`C_f`$ are statements in the stated split; the verifier's example is the control.
- I2: Accepted and fixed in Step 9, item 2, (3.27) and the Result entries (3.10)–(3.12) and (3.27).
- I3: Accepted and fixed in Step 7, item 3, and the Result entry (3.20).

## Setup and assumptions

- **Description (M8).** Objects $`b_1,b_2,f`$, each the only instance of its type. No swap condition (1.11) applies, so $`\mathcal H_{\rm adm}=\mathcal H=\mathcal H_{b_1}\otimes\mathcal H_{b_2}\otimes\mathcal H_f`$ (1.4). The field has a self-adjoint contract $`C_f`$ and self-adjoint operators $`\Phi_x`$, $`x\in X_f`$. Body $`b_i`$ is held at $`x_i\in X_f`$, $`x_1\neq x_2`$ (A15). It is coupled by $`G_i\otimes\Phi_{x_i}`$ with $`G_i`$ self-adjoint and has no other contract. $`C_f`$ is included as $`C_f\otimes\mathbb 1`$ in one of the two pair terms (A5; the sum does not depend on which), so
```math
C=\mathbb 1\otimes\mathbb 1\otimes C_f+G_1\otimes\mathbb 1\otimes\Phi_{x_1}+\mathbb 1\otimes G_2\otimes\Phi_{x_2}.
\qquad\text{(3.1)}
```
- **Spectral notation.** $`C_f\varphi_n=e_n\varphi_n`$ for an orthonormal eigenbasis $`\{\varphi_n\}`$. The distinct eigenvalues (levels) are $`\epsilon_1<\dots<\epsilon_L`$, with spectral projectors $`P_\ell`$ and multiplicities $`d_\ell`$. Further $`\bar\Phi_n(x)=\langle\varphi_n\vert\Phi_x\vert\varphi_n\rangle`$, the coupling $`V=g_1\Phi_{x_1}+g_2\Phi_{x_2}`$ and its size $`v=\lvert g_1\rvert\lVert\Phi_{x_1}\rVert+\lvert g_2\rvert\lVert\Phi_{x_2}\rVert\ge\lVert V\rVert`$. The gap of the level of $`e_n`$ is $`\Delta_n=\min\{\lvert e_m-e_n\rvert:e_m\neq e_n\}`$, and $`\Delta_{\min}=\min_n\Delta_n`$. If $`C_f`$ has a single level ($`L=1`$, in particular if $`\dim\mathcal H_f=1`$), these minima run over empty sets; then $`\Delta_n=\Delta_{\min}=\infty`$, $`Q_n=0`$ in (3.6) and every response vanishes, $`C_f(g)=\epsilon_1\mathbb 1+V`$ is its own effective operator (3.10), and the perturbative results below hold for all $`g`$ with zero remainders.
- **Cost.** The bodies have no other contract, so the cost of the field part is the total cost (1.8), which is well defined (M6). $`E_n(g_1,g_2)`$ is the eigenvalue of $`C_f(g_1,g_2)`$ (3.2) connected to $`e_n`$. It is the cost of the corresponding eigenvector $`\varphi_n(g)`$, called the *adapted* state.
- **Mutual term** (as in the question). It is the part of $`E_n`$ that depends on both $`g_1`$ and $`g_2`$; through second order, the $`g_1g_2`$ term. Its sign for $`g_1g_2>0`$ is the sign of the mutual cost of like sources. Reading this sign as "lower cost close together" presupposes that the mutual term vanishes for far-apart sources, which is a property of the profile (04-profile, out of scope). $`W_n`$ is defined relative to the expansion point $`g=0`$; Step 9 gives its invariance and an invariant counterpart $`\mathcal W_k`$. A comparison of total costs between configurations also contains the one-source terms, which depend on the places (3.24).
- **Reference split.** Expansions are around $`g_1=g_2=0`$ in the split (3.1) fixed by the setting. Step 9 derives which quantities are invariant under the replacements of the listed terms that leave $`C`$ unchanged; the Result section gives for each result its class, [I] or [F], or states that it is a statement in the stated split.
- **Mixtures (extension of the setting, M8).** Take weights $`p_n=p(e_n)\ge0`$ with $`\sum_np_n=1`$, and write $`p_\ell`$ for the weight per eigenvector of level $`\ell`$. The mutual term $`W_\rho`$ of $`\rho=\sum_np_n\lvert\varphi_n\rangle\langle\varphi_n\rvert`$ is the mutual term of $`\sum_\ell p_\ell\,(\text{sum of the branches of level }\ell)`$. For $`v<\Delta_{\min}/2`$, let $`P_\ell(g)`$ be the spectral projector of $`C_f(g)`$ for its $`d_\ell`$ eigenvalues within $`\Delta_{\min}/2`$ of $`\epsilon_\ell`$, and $`\{\tilde\varphi_{\ell j}\}_{j=1}^{d_\ell}`$ any orthonormal basis of its range. With an added object $`r`$ without contract terms and orthonormal $`\eta_{\ell j}\in\mathcal H_r`$, the state $`\beta\otimes\sum_\ell\sqrt{p_\ell}\sum_j\tilde\varphi_{\ell j}\otimes\eta_{\ell j}`$ has the field view $`\sum_\ell p_\ell P_\ell(g)`$ and, as $`C`$ acts as $`\mathbb 1`$ on $`r`$, the cost $`\sum_\ell p_\ell\mathrm{Tr}\bigl(P_\ell(g)C_f(g)\bigr)`$ for every choice of the bases. No continuation of single basis vectors is used.
- **Regime (A13).** The perturbative results hold for $`v<\Delta_n/2`$ (one eigenvector or level) or for $`v<\Delta_{\min}/2`$ (mixtures), with the remainders stated. (3.3)–(3.5), the exact form of (3.14), (3.15), (3.18), (3.19), (3.26) and (3.28) are exact; for a one-level field, see "Spectral notation".

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
Suppose $`\vec a_1,\vec a_2`$ are non-zero and not parallel, i.e. $`[A_1,A_2]\neq0`$. Then $`\lvert g_1\vec a_1+g_2\vec a_2\rvert<\lvert g_1\rvert\lvert\vec a_1\rvert+\lvert g_2\rvert\lvert\vec a_2\rvert`$ for $`g_1g_2\neq0`$. Each branch then depends on both sources already at first order, not additively, and it is not differentiable at $`g=0`$. There is no expansion of the form (3.7) and no mutual term $`\propto g_1g_2`$. If instead $`[A_1,A_2]=0`$, the branches can be chosen in a joint eigenbasis as $`\epsilon_\ell+g_1a_{1\alpha}+g_2a_{2\alpha}`$, which is additive at first order (control). Single branches can then be analytic and carry mutual terms that the level sum does not show. Example: $`C_f=\omega\sigma_3\otimes\mathbb 1`$, $`\Phi_{x_1}=\sigma_1\otimes\mathbb 1`$, $`\Phi_{x_2}=\sigma_1\otimes\sigma_3`$, $`\omega>0`$, so that both levels $`\pm\omega`$ have $`d_\ell=2`$ and $`A_1=A_2=0`$. On the eigenspaces $`s=\pm1`$ of the second $`\sigma_3`$, $`C_f(g)`$ acts as $`\omega\sigma_3+(g_1+sg_2)\sigma_1`$. The branches of the level $`-\omega`$ are $`-\sqrt{\omega^2+(g_1+sg_2)^2}`$, analytic, with mutual terms $`-s\,g_1g_2/\omega`$ of both signs, while their sum has none: $`\chi^{(\ell)}(x_1,x_2)=0`$.
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
These are identities between numbers. The relative factor $`\frac12`$ between $`\Sigma_{n,i}`$ and $`W_n`$ is the counting of the diagonal and off-diagonal terms of the quadratic form $`-\frac12\sum_{i,j}g_ig_j\chi_n(x_i,x_j)`$, not a weaker response to a source's own field. In the adapted eigenvector, $`E_n=\langle\varphi_n(g)\vert C_f\vert\varphi_n(g)\rangle+\sum_ig_i\langle\varphi_n(g)\vert\Phi_{x_i}\vert\varphi_n(g)\rangle`$. By (3.9), the pair terms are $`\sum_ig_i\bigl(\bar\Phi_n(x_i)+\delta N^{(1)}_n(x_i)+\delta N^{(2)}_n(x_i)\bigr)`$: they contain the full fields of both sources, with second-order part $`2(\Sigma_{n,1}+\Sigma_{n,2}+W_n)`$. By (3.7), the field term is then $`e_n-(\Sigma_{n,1}+\Sigma_{n,2}+W_n)`$; it takes back half of that part. Both hold up to $`O(v^3/\Delta_n^2)`$. By the Hellmann–Feynman relation for the simple eigenvalue $`E_n`$, $`\partial E_n/\partial g_i=\langle\varphi_n(g)\vert\Phi_{x_i}\vert\varphi_n(g)\rangle=\bar\Phi_n(x_i)+\delta N^{(1)}_n(x_i)+\delta N^{(2)}_n(x_i)+O(\lVert\Phi_{x_i}\rVert v^2/\Delta_n^2)`$, without a factor $`\frac12`$. What a held body feels is not defined by these identities. For ordered mixtures, (3.16) bounds the mutual term by the self terms.

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
So, at second order, $`C_f`$ and the $`\Phi_x`$ alone fix the sign of the mutual cost of like sources in no case other than the one in which every level response vanishes. In that case the mutual term vanishes for every non-degenerate eigenvector and every level sum, while single branches of a degenerate level can still have either sign (Step 3). The exact, invariant form of this alternative is (3.26). $`C_f`$ and the $`\Phi_x`$ fix:
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

   Between $`\varphi_1`$ and $`\varphi_3`$, both the sign of $`W`$ and the difference $`W(1,2)-W(1,3)`$ reverse: the difference is $`-u`$ in $`\varphi_1`$ and $`+u`$ in $`\varphi_3`$. Under either reading, one state gives like sources close together a lower mutual cost and the other a higher one. These are statements on the mutual part $`W`$ alone.

   The two readings differ in this field. $`\varphi_3`$ has a negative mutual cost, but the mutual cost is lower at the larger separation. The reason is that $`\sum_x\Phi_x=\mathbb 1`$ and $`Q_n\varphi_n=0`$ give $`\sum_y\chi_n(x,y)=0`$, so the mutual term does not vanish at the larger separation. By (3.17), with $`S_1=S_2=\chi_1(x_1,x_2)`$, every non-increasing mixture has $`W_\rho=(p_1-p_3)W_{\varphi_1}`$.

   The total cost also contains the one-source terms, which depend on the places. Write $`E_n(x_1,x_2)`$ for the cost with the sources at $`x_1,x_2`$. In $`\varphi_1`$ and $`\varphi_3`$, $`\bar\Phi_n(x)=\lvert\varphi_n(x)\rvert^2=(\frac14,\frac12,\frac14)`$, and (3.7) with (3.23) gives, for $`v<t/\sqrt2`$, with the upper sign for $`\varphi_1`$ and the lower for $`\varphi_3`$,
```math
E_n(1,2)-E_n(1,3)=\frac{g_2}4\pm\frac{g_2(g_2-2g_1)}{32\sqrt2\,t}+O\Bigl(\frac{\lvert g_2\rvert v^2}{t^2}\Bigr).
\qquad\text{(3.24)}
```
   The remainder carries the factor $`g_2`$ because the difference vanishes identically at $`g_2=0`$. For $`g_2\neq0`$ and $`v/t`$ small enough, the difference has the sign of $`g_2`$ in both states: the total cost does not reverse its preference between the neighbouring and the end place, and only its second-order part reverses. (3.24) is a difference of total costs between configurations, invariant by Step 9; the reversal of $`W`$ holds in invariant form for $`\mathcal W_k`$ (3.27).

### Step 9. Invariance under replacements that leave $`C`$ unchanged (M6)

1. *Replacements in one configuration.* For real $`a_i\neq0`$, $`c_i`$, $`d_i`$,
```math
G_i\otimes\Phi_{x_i}=(a_iG_i+c_i)\otimes\frac{\Phi_{x_i}-d_i}{a_i}+d_i\,G_i\otimes\mathbb 1-c_i\,\mathbb 1\otimes\frac{\Phi_{x_i}-d_i}{a_i}.
\qquad\text{(3.25)}
```
   So $`C`$ is also written with $`G_i'=a_iG_i+c_i`$, $`\Phi'_{x_i}=(\Phi_{x_i}-d_i)/a_i`$, the field term $`C_f'=C_f-c_1\Phi'_{x_1}-c_2\Phi'_{x_2}`$ and single-object terms $`d_iG_i`$ on $`b_i`$ (A5). If $`G_i`$ and $`\Phi_{x_i}`$ are not multiples of $`\mathbb 1`$, these are, up to constants, all writings of $`C`$ with pair terms $`G_i'\otimes\Phi'_{x_i}`$ and single-object terms: the part of $`C`$ that is traceless on $`b_i`$ and on $`f`$ is the product of the traceless parts of $`G_i`$ and $`\Phi_{x_i}`$, which fixes them up to $`a_i`$, and $`C`$ then fixes the single-object terms.
   - $`c_1=c_2=0`$: $`C_f`$, $`e_n`$, $`\varphi_n`$ and $`Q_n`$ do not change, and $`g_i'\Phi'_{x_i}=g_i\Phi_{x_i}-g_id_i`$, whose constant the body term restores. So the one-source terms $`g_i\bar\Phi_n(x_i)+\Sigma_{n,i}`$ (body term included), $`W_n`$ and the cost $`g_j\,\delta N^{(i)}_n(x_j)`$ felt by body $`j`$ are unchanged; $`\chi_n(x_i,x_j)`$ is multiplied by $`1/(a_ia_j)`$, and $`g_1g_2>0`$ is kept iff $`a_1a_2>0`$.
   - $`c_i\neq0`$: the new expansion point $`g'=0`$ is $`g_i=-c_i/a_i`$, and $`C_f'`$ is, up to a constant, the operator $`C_f(-c_1/a_1,-c_2/a_2)`$ of the family (3.2). (3.7)–(3.9) then expand the same eigenvalues about another point, with other coefficients. For the two-place field of check 2 with $`c_1=c`$, $`c_2=0`$, $`a_i=1`$, $`d_i=0`$: $`\chi'(1,2)=-t^2/[4(t^2+c^2/4)^{3/2}]\neq\chi(1,2)=-1/(4t)`$ for $`c\neq0`$.
   - $`G_i`$ or $`\Phi_{x_i}`$ a multiple of $`\mathbb 1`$: the pair term of body $`i`$ is a single-object term, and $`C`$ has writings outside (3.25). For $`G_i=g_i\mathbb 1`$, $`\Phi_{x_i}`$ can be replaced by any self-adjoint $`\Phi'_{x_i}`$, with $`C_f'=C_f+g_i(\Phi_{x_i}-\Phi'_{x_i})`$. For $`\Phi_{x_i}=\phi\,\mathbb 1`$, $`G_i\otimes\Phi_{x_i}=\mathbb 1\otimes\Phi'_{x_i}+\phi\,G_i\otimes\mathbb 1-\mathbb 1\otimes\Phi'_{x_i}`$ for any $`\Phi'_{x_i}`$: $`G_i'=\mathbb 1`$, $`C_f'=C_f-\Phi'_{x_i}`$ and the body term $`\phi G_i`$, which also changes the sectors of body $`i`$. So $`C`$ does not fix $`\Phi_{x_i}`$, and sharpness at $`x_i`$ and the response relative to the listed $`C_f`$ are statements in the stated split. Control: $`G_1=G_2=\mathbb 1`$ and $`C_f=\Phi_{x_1}=\Phi_{x_2}=\sigma_3`$ give the same $`C`$ as $`C_f'=3\sigma_3-2\sigma_1`$, $`\Phi'_{x_1}=\Phi'_{x_2}=\sigma_1`$; $`\lvert0\rangle`$ is sharp at both places in the first writing and at neither in the second.
2. *One configuration.* For $`G_i,\Phi_{x_i}`$ not multiples of $`\mathbb 1`$, item 1 changes only the labels $`g_i'=a_ig_i+c_i`$ of the joint eigenspaces $`\mathcal B_\alpha`$ of $`(G_1,G_2)`$ (the *sectors* $`\alpha`$), not the eigenspaces. The operator $`K_\alpha`$ on $`\mathcal H_f`$ with $`C(\beta\otimes\varphi)=\beta\otimes K_\alpha\varphi`$ for $`\beta\in\mathcal B_\alpha`$ is therefore fixed by $`C`$; in the stated split $`K_\alpha=C_f(g_1,g_2)`$, (3.2). So are the evolution and the views of Step 1, the cost of every state, and the ordered eigenvalues $`E^{(1)}_\alpha\le E^{(2)}_\alpha\le\dots`$ of $`K_\alpha`$ with their eigenspaces. Sharpness at $`x_i`$ is fixed too, since $`\Phi'_{x_i}=(\Phi_{x_i}-d_i)/a_i`$ has the eigenvectors of $`\Phi_{x_i}`$. An eigenvector of $`C_f`$ sharp at $`x_1,x_2`$ is an eigenvector of $`C_f'=C_f-\sum_ic_i\Phi'_{x_i}`$. By (3.19) at $`g_i=-c_i/a_i`$, where $`C_f(g)`$ is $`C_f'`$ up to a constant, a state whose evolution under $`C_f`$ stays sharp at $`x_1,x_2`$ has the same property under $`C_f'`$. So the exact statements (3.18)–(3.19) at $`x_1,x_2`$ hold in every writing. Weyl's inequality for ordered eigenvalues, $`\lvert E^{(k)}_\alpha-e^{(k)}\rvert\le\lVert V\rVert\le v`$ with $`e^{(1)}\le e^{(2)}\le\dots`$ the eigenvalues of $`C_f`$, gives for a non-degenerate $`e_n`$ and $`v<\Delta_n/2`$: $`E_n(g)=E^{(k)}_\alpha`$ with $`k=\#\{m:e_m\le e_n\}`$, the rank of $`e_n`$. So the cost of the adapted state is invariant, while its decomposition in (3.7) is not (item 1). For a level $`\epsilon_\ell`$ of multiplicity $`d_\ell\ge2`$ and $`v<\Delta_n/2`$, the same inequality gives a block of $`d_\ell`$ ranks, $`k_\ell-d_\ell<k\le k_\ell`$ with $`k_\ell=\#\{m:e_m\le\epsilon_\ell\}`$. The rank $`\#\{m:e_m\le e_n\}=k_\ell`$ is the same for every vector of the level and does not represent its $`d_\ell`$ branches (Step 3, item 1). The invariant counterpart of the level sum of Step 3 is the block sum $`\sum_{k_\ell-d_\ell<k\le k_\ell}E^{(k)}_\alpha`$, the trace of $`K_\alpha`$ times its spectral projector for these ranks. For eigenvalues $`g_i\neq g_i'`$ of $`G_i`$, write $`K_{g_1g_2}`$ and $`E^{(k)}_{g_1g_2}`$ for the sector $`(g_1,g_2)`$. As $`C_f(g)`$ is affine in $`g`$,
```math
K_{g_1g_2}-K_{g_1'g_2}-K_{g_1g_2'}+K_{g_1'g_2'}=0,\qquad
\mathcal W_k=E^{(k)}_{g_1g_2}-E^{(k)}_{g_1'g_2}-E^{(k)}_{g_1g_2'}+E^{(k)}_{g_1'g_2'},\qquad
\sum_k\mathcal W_k=0 .
\qquad\text{(3.26)}
```
   $`\mathcal W_k`$, the *mutual cost of the change of both sources* in the state of rank $`k`$, is the cost change when both sources change minus the changes when one of them changes. It is fixed by $`C`$ and the four sectors, exactly and without an expansion point. The sum rule follows from $`\sum_kE^{(k)}_\alpha=\mathrm{Tr}K_\alpha`$ and the first equation, and it holds as well for the eigenvalues on a subspace invariant under all $`K_\alpha`$. So, exactly, either every $`\mathcal W_k`$ vanishes or both signs occur. A field state that is the same in the four sectors has, by the first equation, zero mixed difference of its costs (3.5). If (3.7) applies at the four sectors, with $`v`$ the largest of its four values, the terms that depend on one $`g_i`$ only cancel and
```math
\mathcal W_k=-(g_1-g_1')(g_2-g_2')\,\chi_n(x_1,x_2)+O\Bigl(\frac{v^3}{\Delta_n^2}\Bigr),\qquad k=\text{rank of a non-degenerate }e_n .
\qquad\text{(3.27)}
```
   This holds in every split in which (3.7) applies at the four sectors, with the same left side. For a degenerate level, (3.10)–(3.12) give the same, with $`\chi^{(\ell)}(x_1,x_2)`$ in place of $`\chi_n(x_1,x_2)`$, for the sum of $`\mathcal W_k`$ over its block of ranks: the terms linear in $`g`$ and in $`g_i^2`$ drop out of the mixed difference of $`\mathrm{Tr}H_\ell(g)`$. Under (3.25), $`(g_1-g_1')(g_2-g_2')`$ is multiplied by $`a_1a_2`$, so in one configuration it is a convention whether two changes are like.
3. *The family of configurations.* The class of the setting contains the same bodies at every pair $`x_1\neq x_2`$ of $`X_f`$: the total contracts $`C(x_1,x_2)`$ of (3.1) with one $`C_f`$, one set $`\{\Phi_x\}`$ and one pair $`G_1,G_2`$ (M8). A replacement may differ from one configuration to another (a place-dependent replacement, M6); it leaves every $`C(x_1,x_2)`$, and with it everything of item 2, unchanged. So the total cost $`E^{(k)}_\alpha(x_1,x_2)`$ of each state named by its rank, its dependence on the places at fixed sectors and its differences between configurations, such as (3.24), are invariant. In the stated split (3.7) gives them; there the one-source terms $`g_i\bar\Phi_n(x_i)+\Sigma_{n,i}`$ depend on the places as well as $`W_n`$. For $`x\neq x'`$ and $`y\notin\{x,x'\}`$ the differences of total contracts
```math
C(x,y)-C(x',y)=G_1\otimes\mathbb 1\otimes(\Phi_x-\Phi_{x'}),\qquad C(y,x)-C(y,x')=\mathbb 1\otimes G_2\otimes(\Phi_x-\Phi_{x'})
\qquad\text{(3.28)}
```
   are invariant. A non-zero product of self-adjoint operators fixes its factors up to a real factor, and the two products share the field factor. Let $`\lvert X_f\rvert\ge3`$, $`\Phi_x\neq\Phi_{x'}`$ for some $`x,x'`$, and $`G_i`$ not a multiple of $`\mathbb 1`$. Take any writing of all $`C(x_1,x_2)`$ with one field term, one set of field operators, one pair of body operators and fixed single-object terms. By (3.28), $`G_i'=aG_i`$ with one $`a\neq0`$ for both bodies, zeros included, and $`\Phi'_x-\Phi_x/a`$ does not depend on $`x`$; since $`G_i`$ is not a multiple of $`\mathbb 1`$ and $`C`$ has no further term of the form $`G_i\otimes D`$, this difference is a multiple of $`\mathbb 1`$. This is (3.25) with $`c_1=c_2=0`$, $`a_1=a_2=a`$, $`d_1=d_2`$, and $`C_f'=C_f`$. The stated split is thus, up to $`a`$ and $`d`$, the only writing of all configurations with one field term, one set of field operators and one pair of body operators. By item 1, the decomposition of Steps 2–8 is invariant under these replacements, with $`\chi_n\to\chi_n/a^2`$, $`\delta N^{(i)}_n\to\delta N^{(i)}_n/a`$, and $`W_n`$, $`\Sigma_{n,i}`$ and the sign of $`g_1g_2`$ unchanged. A place-dependent replacement changes no cost but can change the decomposition; an example is item 1 with $`c_1\neq0`$ in every configuration, so that $`C_f'=C_f-c_1\Phi'_{x_1}`$ follows body 1. In a two-place field (3.28) is not available. There $`C(1,2)-C(2,1)=(G_1\otimes\mathbb 1-\mathbb 1\otimes G_2)\otimes(\Phi_1-\Phi_2)`$ fixes the zeros only up to a common shift $`c_1=c_2=c`$, with $`C_f'=C_f-c(\Phi'_1+\Phi'_2)`$; this changes $`C_f`$ by more than a constant unless $`\Phi_1+\Phi_2\propto\mathbb 1`$.
4. *Classes used in the Result section.*
   - **[I]**: invariant under every replacement in one configuration (items 1–2), hence under place-dependent ones. An [I] statement that names sectors, sector operators or sharpness at $`x_i`$ needs $`G_i`$ and $`\Phi_{x_i}`$ not multiples of $`\mathbb 1`$ (item 2); otherwise it is a statement in the stated split (item 1, last bullet). The cost of a given state is [I] without this condition.
   - **[F]**: a statement in the stated split that holds in every split in which its conditions hold, with that split's $`C_f`$, $`\Phi_x`$, $`G_i`$. For the family of item 3 with $`\lvert X_f\rvert\ge3`$, some $`\Phi_x\neq\Phi_{x'}`$ and $`G_i`$ not multiples of $`\mathbb 1`$, it is invariant up to the factor $`a`$ under every replacement that is the same in all configurations. In one configuration, in a two-place field with $`\Phi_1+\Phi_2\not\propto\mathbb 1`$, and under place-dependent replacements, its values can depend on the expansion point (item 1).

## Result

- **(3.2), (3.3), (3.4)** (theorem, item 1). Class: every finite field and every $`C_f`$, $`\Phi_x`$, $`G_i`$ of the setting. Take any field start and a body start in one joint eigenspace of $`(G_1,G_2)`$, with eigenvalues $`(g_1,g_2)`$. The bodies stay in their start, and the field evolves by $`e^{-iC_f(g_1,g_2)\lambda}`$ with $`C_f(g_1,g_2)=C_f+g_1\Phi_{x_1}+g_2\Phi_{x_2}`$, exactly for all $`\lambda`$. For other body starts this holds branch by branch, and the field view is the mixture (3.4). This is an identity, with no control in the class. Invariance: [I] for $`G_i`$ and $`\Phi_{x_i}`$ not multiples of $`\mathbb 1`$; then $`C_f(g_1,g_2)`$ is the sector operator $`K_\alpha`$ of Step 9, and only its parametrisation by $`(g_1,g_2)`$ depends on the split.
- **(3.5)** (theorem). Same class and starts. The cost is exactly linear in $`(g_1,g_2)`$ and conserved. A field start that does not depend on the sources carries no mutual term at any order. Invariance: the cost of each state is [I]; for $`G_i`$ and $`\Phi_{x_i}`$ not multiples of $`\mathbb 1`$, the invariant form of the last statement is the first equation of (3.26).
- **(3.6)** (definition). The response function $`\chi_n(x,y)`$ of a non-degenerate eigenvector, written with the reduced resolvent $`Q_n`$. It is real and symmetric, and it is independent of phases, of the basis chosen in other levels and of shifts $`\Phi_x\to\Phi_x+c_x\mathbb 1`$. Invariance: [F]; under (3.25) with $`c_i=0`$, $`\chi_n(x_i,x_j)`$ is multiplied by $`1/(a_ia_j)`$.
- **(3.7), (3.8)** (formula, item 2). Non-degenerate $`\varphi_n`$, $`v<\Delta_n/2`$: $`E_n=e_n+\sum_i(g_i\bar\Phi_n(x_i)+\Sigma_{n,i})+W_n+O(v^3/\Delta_n^2)`$. The self terms are $`\Sigma_{n,i}=-\frac12g_i^2\chi_n(x_i,x_i)`$ and the mutual term is $`W_n=-g_1g_2\chi_n(x_1,x_2)`$. Invariance: $`E_n(g)`$ is the eigenvalue $`E^{(k)}_\alpha`$ of rank $`k`$ of the sector operator, [I]; its decomposition into $`e_n`$, one-source terms and $`W_n`$ is [F].
- **(3.9)** (formula). Same conditions. In the adapted eigenvector, source $`i`$ changes $`\langle\Phi_y\rangle`$ by $`\delta N^{(i)}_n(y)=-g_i\chi_n(y,x_i)`$, with remainder $`O(\lVert\Phi_y\rVert v^2/\Delta_n^2)`$, and this change is reciprocal. From the unadapted start $`\varphi_n`$, the $`\lambda`$-average of $`\langle\Phi_y\rangle`$ equals it to the same order, while the cost stays (3.5). Invariance: [F].
- **(3.10), (3.11), (3.12)** (formula and negative, item 2). Degenerate level, $`d_\ell\ge2`$, $`v<\Delta_n/2`$. There are $`d_\ell`$ branches; up to $`O(v^3/\Delta_n^2)`$ they are the eigenvalues of $`H_\ell(g)`$. For $`d_\ell=2`$ with $`[A_1,A_2]\neq0`$, each branch depends on both sources at first order, non-additively and non-differentiably at $`g=0`$, so it has no mutual term $`\propto g_1g_2`$. Control: $`[A_1,A_2]=0`$; then single branches can be analytic and carry mutual terms of both signs while the level response vanishes (example in Step 3). The sum of the branches is always analytic, with mutual term $`-g_1g_2\chi^{(\ell)}(x_1,x_2)`$, where $`\chi^{(\ell)}`$ is the level response. Invariance: [F]. The sum of the branches is the block sum of the ordered eigenvalues $`E^{(k)}_\alpha`$ over the $`d_\ell`$ ranks of the level, [I]; the rank $`\#\{m:e_m\le e_n\}`$ is the same for every vector of the level and does not represent its branches (Step 9, item 2).
- **(3.13), (3.14)** (theorem, item 3). For weights $`p(e_n)`$ and $`v<\Delta_{\min}/2`$, the pair formula (3.13) holds. For all $`x,y`$, $`\sum_n\chi_n(x,y)=0`$, and the same sum vanishes over the eigenvectors in any subspace invariant under $`C_f`$ and all $`\Phi_x`$. In exact form, the sum over all branches has no mutual part at any order. This is an identity, with no control. Invariance: [F]; the exact form is [I] as the sum rule of (3.26).
- **(3.15)** (theorem, item 3). Class: fields with a unitary $`U`$, $`UC_fU^\dagger=-C_f`$, $`U\Phi_xU^\dagger=\epsilon_x\Phi_x`$, and non-degenerate $`\varphi_n`$, $`v<\Delta_n/2`$. Exactly, $`E_{U\varphi_n}(g_1,g_2)=-E_n(-\epsilon_{x_1}g_1,-\epsilon_{x_2}g_2)`$, $`\chi_{U\varphi_n}=-\epsilon_x\epsilon_y\chi_n`$ and $`W_{U\varphi_n}=-\epsilon_{x_1}\epsilon_{x_2}W_n`$. The mutual terms of the lowest and the highest eigenvector are opposite if $`\epsilon_{x_1}=\epsilon_{x_2}`$ and equal if $`\epsilon_{x_1}=-\epsilon_{x_2}`$. This is an identity in its class. Invariance: [F], except that a shift $`d`$ of the $`\Phi_x`$ adds a term linear in $`g`$ to the first relation; the relations for $`\chi`$ and $`W`$ are unchanged.
- **(3.16)** (theorem, item 3). Second order, $`v<\Delta_{\min}/2`$. For weights non-increasing (non-decreasing) in $`e`$, $`[\chi_\rho(x,y)]`$ is positive (negative) semidefinite, the self terms are $`\le0`$ ($`\ge0`$), and $`W_\rho^2\le4\Sigma_{\rho,1}\Sigma_{\rho,2}`$. For interior eigenvectors the bound can fail; (3.21) is the control. Invariance: [F].
- **(3.17)** (criterion, item 3). Same order. $`W_\rho`$ has one weak sign for all non-increasing mixtures iff the partial sums $`S_1,\dots,S_{L-1}`$ have one weak sign; non-decreasing mixtures then have the opposite sign. The ordering alone does not fix the sign; control: $`\Phi_{x_2}\to-\Phi_{x_2}`$. Invariance: [F].
- **(3.18), (3.19)** (theorem and negative, item 4). A non-degenerate eigenvector sharp at $`x`$ has $`\chi_n(x,\cdot)=0`$, and $`\chi_n\equiv0`$ if it is sharp at all $`x`$. If it is sharp at $`x_1`$ and $`x_2`$, $`E_n`$ is exactly linear and the field is unchanged up to a phase. A field state that stays sharp at $`x_1`$ and $`x_2`$ along its evolution is changed by the sources only by a phase, for all $`\lambda`$. So a field state cannot stay sharp at the places of both bodies and respond to them. Control: the non-sharp lowest eigenvector of the two-place field responds. Invariance: for $`G_i`$ and $`\Phi_{x_i}`$ not multiples of $`\mathbb 1`$, the exact statements at $`x_1,x_2`$ are [I], since every writing (3.25) keeps the eigenvectors of $`\Phi_{x_i}`$ and keeps the states of (3.18)–(3.19) (Step 9, item 2); $`\chi_n(x,\cdot)=0`$ and sharpness at all $`x`$ are [F]. If $`G_i`$ or $`\Phi_{x_i}`$ is a multiple of $`\mathbb 1`$, sharpness at $`x_i`$ and the response relative to the listed $`C_f`$ are statements in the stated split; control: Step 9, item 1, last bullet.
- **(3.20)** (formula, item 4). At second order, for every non-degenerate eigenvector and every mixture: $`W=g_2\delta N^{(1)}(x_2)=g_1\delta N^{(2)}(x_1)`$ and $`\Sigma_i=\frac12g_i\delta N^{(i)}(x_i)`$. These are identities between numbers; the relative factor $`\frac12`$ counts the diagonal and off-diagonal terms of the quadratic form. In the adapted eigenvector the pair terms contain the full fields of both sources, with second-order part $`2(\Sigma_{n,1}+\Sigma_{n,2}+W_n)`$, and the field term takes back half of it, up to $`O(v^3/\Delta_n^2)`$. $`\partial E_n/\partial g_i`$ contains $`\delta N^{(1)}_n(x_i)+\delta N^{(2)}_n(x_i)`$ without a factor $`\frac12`$, up to $`O(\lVert\Phi_{x_i}\rVert v^2/\Delta_n^2)`$. What a held body feels is not defined by these identities. For an extreme non-degenerate eigenvector, $`\chi_n(x_i,x_i)=0`$ iff the eigenvector is sharp at $`x_i`$, and then $`W_n=0`$. Invariance: [F].
- **(3.21)** (example). A three-place field whose interior eigenvector has zero self terms and a non-zero mutual term $`4g_1g_2/\omega`$. Invariance: a statement in the stated split, since $`X_f`$ has only two places.
- **(3.22)** (negative, item 5). For every field of the class and every $`x_1\neq x_2`$, at second order: either all level responses $`\chi^{(\ell)}(x_1,x_2)`$ vanish, or levels with both signs occur. The sign of the mutual cost of like sources is therefore fixed by $`C_f`$ and the $`\Phi_x`$ alone in no case other than the one in which every level response vanishes; there the mutual term vanishes for every non-degenerate eigenvector and every level sum, while single branches of a degenerate level can have either sign. $`C_f`$ and the $`\Phi_x`$ fix the level responses, the partial sums $`S_k`$, the relation between the ends of the spectrum and the sign of the self terms for ordered weights. The state fixes which eigenvector or mixture, whether the field depends on the sources at all, and whether it is sharp at a body's place. Invariance: [F]; the exact alternative for $`\mathcal W_k`$ in (3.26) is [I].
- **(3.23)** (example, item 5). Three-place chain, second order. In the lowest eigenvector the mutual cost of like sources is $`2u>0`$ at neighbouring places and $`3u`$ at the end places. In the highest it is $`-2u`$ and $`-3u`$, and in the middle eigenvector it is $`0`$, with $`u=g_1g_2/(16\sqrt2t)`$. Both the sign and the neighbour-minus-end difference reverse between the lowest and the highest eigenvector. This compares the mutual part only; the total cost is (3.24). Invariance: [F]; by (3.27), the same values hold for $`\mathcal W_k`$, which is [I], with $`(g_1-g_1')(g_2-g_2')`$ in place of $`g_1g_2`$ and remainder $`O(v^3/t^2)`$.
- **(3.24)** (example, item 5). Three-place chain of (3.23), lowest (upper sign) and highest (lower sign) eigenvector, $`v<t/\sqrt2`$: $`E_n(1,2)-E_n(1,3)=\frac{g_2}4\pm\frac{g_2(g_2-2g_1)}{32\sqrt2\,t}+O(\lvert g_2\rvert v^2/t^2)`$. For $`g_2\neq0`$ and $`v/t`$ small enough it has the sign of $`g_2`$ in both states: the total cost does not reverse its preference between the neighbouring and the end place, and only its second-order part reverses. Invariance: [I] (a difference of total costs between configurations).
- **(3.25)** (formula). Class: every $`G_i`$, $`\Phi_{x_i}`$ of the setting, real $`a_i\neq0`$, $`c_i`$, $`d_i`$. The identity gives the writings of $`C`$ with $`G_i'=a_iG_i+c_i`$, $`\Phi'_{x_i}=(\Phi_{x_i}-d_i)/a_i`$, $`C_f'=C_f-\sum_ic_i\Phi'_{x_i}`$ and body terms $`d_iG_i`$; if $`G_i`$ and $`\Phi_{x_i}`$ are not multiples of $`\mathbb 1`$, these are all writings in the form of the setting, up to constants. With $`c_i=0`$ the quantities of Steps 2–8 are unchanged up to the factors $`a_i`$; with $`c_i\neq0`$ the expansion point moves to $`g_i=-c_i/a_i`$ and the coefficients of (3.7)–(3.9) change (control: the two-place field, $`\chi'(1,2)\neq\chi(1,2)`$).
- **(3.26)** (theorem). Class: one configuration, $`G_i`$ and $`\Phi_{x_i}`$ not multiples of $`\mathbb 1`$, two eigenvalues $`g_i\neq g_i'`$ of each $`G_i`$. The sectors, the sector operators $`K_\alpha`$ and their ordered eigenvalues $`E^{(k)}_\alpha`$ are fixed by $`C`$. Exactly, the sector operators have zero mixed difference, and the mutual cost $`\mathcal W_k`$ of the change of both sources satisfies $`\sum_k\mathcal W_k=0`$, also over the eigenvalues on any subspace invariant under all $`K_\alpha`$; so either all $`\mathcal W_k`$ vanish or both signs occur. Invariance: [I]. This is an identity; there is no control in the class.
- **(3.27)** (formula). If (3.7) applies at the four sectors, with $`v`$ its largest value there: $`\mathcal W_k=-(g_1-g_1')(g_2-g_2')\chi_n(x_1,x_2)+O(v^3/\Delta_n^2)`$, $`k`$ the rank of the non-degenerate $`e_n`$, in every split in which this condition holds. For a degenerate level with $`v<\Delta_n/2`$ at the four sectors, the sum of $`\mathcal W_k`$ over its block of $`d_\ell`$ ranks is the same with $`\chi^{(\ell)}(x_1,x_2)`$ in place of $`\chi_n(x_1,x_2)`$. Invariance: the left side is [I]; whether two changes are like is a convention in one configuration and is fixed by (3.28).
- **(3.28)** (theorem). Class: the configurations of the setting with $`\lvert X_f\rvert\ge3`$, $`\Phi_x\neq\Phi_{x'}`$ for some $`x,x'`$, and $`G_i`$ not multiples of $`\mathbb 1`$. The differences (3.28) of total contracts are [I]; with one set of field operators they fix $`G_1,G_2`$, zeros included, up to one common factor $`a`$. The stated split is, up to $`a`$ and a common shift $`d`$ of the $`\Phi_x`$, the only writing of all configurations with one field term, one set of field operators and one pair of body operators, and the [F] results are invariant under every replacement that is the same in all configurations. Total costs, their dependence on the places at fixed sectors and their differences between configurations are [I] under every replacement, place-dependent ones included. Control: a two-place field with $`\Phi_1+\Phi_2\not\propto\mathbb 1`$, where a common shift of the zeros remains, and a single configuration, where (3.25) with $`c_i\neq0`$ applies.

## Consistency checks

1. **Dimensions and $`g_2=0`$.** $`g_i\Phi_x`$ is a cost and, by (3.6), $`\chi_n`$ has the dimension of $`\Phi^2/\text{cost}`$. Every term of (3.7) is therefore a cost. At $`g_2=0`$ the mutual term vanishes, and (3.7) becomes the one-source expansion. Passed.
2. **Two-place field.** Take $`C_f=-t\sigma_1`$ and $`\Phi_x=\lvert x\rangle\langle x\rvert`$. The exact eigenvalues are $`\frac{g_1+g_2}2\mp\sqrt{t^2+(g_1-g_2)^2/4}`$. The lowest expands to $`-t+\frac{g_1+g_2}2-\frac{(g_1-g_2)^2}{8t}`$, with mutual term $`+\frac{g_1g_2}{4t}`$ and self terms $`-\frac{g_i^2}{8t}`$. (3.6) gives the same: $`\chi(1,2)=-\frac1{4t}`$ and $`\chi(x,x)=\frac1{4t}`$. The highest eigenvalue has the opposite second-order terms, as required by (3.14) and by (3.15) with $`U=\sigma_3`$. The bound (3.16) holds with equality. The mixed sector difference of the exact lowest eigenvalue is $`(g_1-g_1')(g_2-g_2')/(4t)`$ at second order, as (3.27) requires. Since $`\Phi_1+\Phi_2=\mathbb 1`$, the common shift left by the two-place family (Step 9, item 3) changes $`C_f`$ only by a constant. Passed.
3. **$`\Phi_x`$ commuting with $`C_f`$.** A non-degenerate $`\varphi_n`$ is then an eigenvector of every $`\Phi_x`$, i.e. sharp. (3.6) gives $`\chi_n=0`$, and (3.7) reduces to $`e_n+\sum_ig_i\bar\Phi_n(x_i)`$, which is the exact eigenvalue, in agreement with (3.18). Passed.

## Open issues

- No relaxation (A11). What, if anything, brings the field into an adapted state is open; in unadapted starts the cost has no mutual term (3.5).
- The dependence on distance, whether the mutual term vanishes for far-apart sources, and hence which reading of the sign applies, belong to 04-profile.
- For degenerate levels, the level sums are always analytic; single branches may or may not be (Step 3), and no general statement on their mutual terms is derived. Orders above the second are not treated, except in the exact results.
- Mixtures are realised through an added object without contracts, which is an extension of the setting.

## Methods used

- reduction on joint eigenspaces of conserved operators
- Rayleigh–Schrödinger and quasi-degenerate (Schrieffer–Wolff) perturbation theory
- Weyl's inequality, reduced resolvent
- trace identities, Abel summation
- semidefinite matrices, Cauchy–Schwarz
- spectrum-reflecting unitary symmetry
- uniqueness of the factors of a product operator, mixed second differences
