# The field as an object: sharp field states, reduced descriptions, conventions

- **Subproject:** 05-ilang-free-fall
- **Package:** 02-field-object
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-10

## Setup and assumptions

**Class.** Every description of the form stated in `question.md`: a body $`b`$, a field $`f`$ and a set $`r`$ of further objects (possibly empty), of pairwise different types, with $`\mathcal H=\mathcal H_{br}\otimes\mathcal H_f`$, $`\mathcal H_{br}:=\mathcal H_b\otimes\mathcal H_r`$, finite-dimensional (A1), and the contract

```math
C=C_{br}\otimes\mathbb 1_f+\sum_{j\in J}B_j\otimes\mathbb 1_r\otimes\Phi_j+\mathbb 1_{br}\otimes C_f \qquad\text{(2.1)}
```

for every self-adjoint $`C_{br}`$, $`C_f`$ and every finite family of self-adjoint $`B_j`$ (on $`\mathcal H_b`$) and $`\Phi_j`$ (on $`\mathcal H_f`$). The start is $`\Psi_0=\Psi_{br}\otimes\varphi`$ with $`\Psi_{br}`$ any unit vector of $`\mathcal H_{br}`$, and $`\lambda\ge0`$. The form (2.1), the product start and the field state $`\varphi`$ named in each step are assumptions (M8, A11). The results say what such descriptions give, not that the language enforces them (M10).

**Notation.** $`B_j`$ also denotes $`B_j\otimes\mathbb 1_r`$ on $`\mathcal H_{br}`$. $`\langle O\rangle_\Psi:=\langle\Psi\vert O\vert\Psi\rangle`$. $`U(\lambda):=e^{-iC\lambda}`$ and $`\Psi(\lambda)=U(\lambda)\Psi_0`$. $`V(\lambda):=\mathrm{Tr}_f\lvert\Psi(\lambda)\rangle\langle\Psi(\lambda)\rvert`$ is the view of $`\{b\}\cup r`$, and $`V_f(\lambda)`$ the view of $`\{f\}`$ (1.5).

**LI.** The hypothesis that $`\mathbb 1_b`$ and the $`B_j`$, $`j\in J`$, are linearly independent (over $`\mathbb R`$; for self-adjoint operators this is the same as over $`\mathbb C`$). Every statement below says whether it uses LI.

**Schedules.** A schedule consists of readings with projectors $`\Pi_i\otimes\mathbb 1_f`$ at $`0\le\lambda_1\le\dots\le\lambda_k`$, where $`\Pi_i`$ is diagonal in the joint places of $`b`$ and $`r`$ and belongs to the outcome $`r_i`$. By (1.3) and (1.9),

```math
p(r_1,\dots,r_k)=\bigl\lVert(\Pi_k\otimes\mathbb 1_f)\,U(\lambda_k-\lambda_{k-1})\cdots(\Pi_1\otimes\mathbb 1_f)\,U(\lambda_1)\,\Psi_0\bigr\rVert^2 . \qquad\text{(2.2)}
```

**Exact or estimate.** Every statement is exact, for all $`\Psi_{br}`$ and all $`\lambda\ge0`$, except (2.9), (2.10) and (2.14), which are expansions for $`\lambda\to0`$ at fixed operators and start, with the stated remainder.

**Input.** (17.15) of 03-ilang-space/17-motion@v2, as quoted in `question.md`: for $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$, start $`\phi\otimes\chi`$, record vectors $`u_h=(K_h-\langle K_h\rangle)\chi`$ and $`K_{h_m}=mX`$, one has $`d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X`$ with $`\sigma_X^2=\langle X^2\rangle-\langle X\rangle^2`$. It is used only in Step 8.

## Derivation

### Step 1. Sharp and stationary field: state and views (item 1a)

Let $`\Phi_j\varphi=n_j\varphi`$ and $`C_f\varphi=e_f\varphi`$. For every $`\Psi\in\mathcal H_{br}`$, (2.1) gives

```math
C\,(\Psi\otimes\varphi)=\bigl((C_{\rm red}+e_f)\Psi\bigr)\otimes\varphi,\qquad C_{\rm red}:=C_{br}+\sum_{j\in J}n_j\,B_j\otimes\mathbb 1_r . \qquad\text{(2.3)}
```

So $`\mathcal H_{br}\otimes\varphi`$ is invariant under $`C`$, and (1.9) gives

```math
\Psi(\lambda)=e^{-ie_f\lambda}\,\Psi_{\rm red}(\lambda)\otimes\varphi,\qquad \Psi_{\rm red}(\lambda):=e^{-iC_{\rm red}\lambda}\Psi_{br}, \qquad\text{(2.4)}
```

```math
V(\lambda)=\lvert\Psi_{\rm red}(\lambda)\rangle\langle\Psi_{\rm red}(\lambda)\rvert,\qquad V_f(\lambda)=\lvert\varphi\rangle\langle\varphi\rvert . \qquad\text{(2.5)}
```

This is exact for every $`\Psi_{br}`$ (a product or not) and every $`\lambda`$, and LI is not used. Both views are pure and $`V_f`$ is constant: the field does not become entangled with $`b`$ or $`r`$. The factor $`e^{-ie_f\lambda}`$ is a common phase (1.2).

### Step 2. Reduced description (item 1b)

By (2.3), $`U(\ell)`$ acts on $`\mathcal H_{br}\otimes\varphi`$ as $`e^{-ie_f\ell}e^{-iC_{\rm red}\ell}\otimes\mathbb 1_f`$, and $`\Pi_i\otimes\mathbb 1_f`$ maps this subspace into itself. Hence (2.2) becomes

```math
p(r_1,\dots,r_k)=\bigl\lVert\Pi_k\,e^{-iC_{\rm red}(\lambda_k-\lambda_{k-1})}\cdots\Pi_1\,e^{-iC_{\rm red}\lambda_1}\,\Psi_{br}\bigr\rVert^2 , \qquad\text{(2.6)}
```

which is the statistics of the same schedule in the reduced description with the objects $`b`$, $`r`$, the contract $`C_{\rm red}`$ of (2.3) and the start $`\Psi_{br}`$. The answer is yes, exactly, for every schedule and every $`\Psi_{br}`$.

*All contracts that do this.* A contract $`C'`$ on $`\mathcal H_{br}`$ gives the statistics (2.6) for every schedule and every $`\Psi_{br}`$ if and only if

```math
C'=C_{\rm red}+\Delta,\qquad \Delta\ \text{real and diagonal in the joint places of } b \text{ and } r,\qquad [\Delta,C_{\rm red}]=0 . \qquad\text{(2.7)}
```

*Proof.* ($`\Leftarrow`$) $`e^{-iC'\ell}=e^{-i\Delta\ell}e^{-iC_{\rm red}\ell}`$, and $`e^{-i\Delta\ell}`$ commutes with every $`\Pi_i`$ (both are diagonal in the joint places) and with every $`e^{-iC_{\rm red}\ell'}`$. All factors $`e^{-i\Delta\ell}`$ can be moved to the left in (2.6), where they do not change the norm. ($`\Rightarrow`$) Read all objects of $`b`$ and $`r`$ at one $`\lambda`$, with outcome the joint place $`K`$. Equal probabilities for every $`\Psi_{br}`$ mean $`\lvert\langle K\vert e^{-iC'\lambda}\Psi_{br}\rangle\rvert=\lvert\langle K\vert e^{-iC_{\rm red}\lambda}\Psi_{br}\rangle\rvert`$ for all $`\Psi_{br}`$, hence $`e^{iC'\lambda}\lvert K\rangle=e^{i\theta_K(\lambda)}e^{iC_{\rm red}\lambda}\lvert K\rangle`$. So $`W(\lambda):=e^{-iC_{\rm red}\lambda}e^{iC'\lambda}`$ is diagonal in the joint places for all $`\lambda\ge0`$, and so are its derivatives at $`\lambda=0`$: $`W'(0)=i\Delta`$ with $`\Delta:=C'-C_{\rm red}`$, and $`W''(0)=[C_{\rm red},\Delta]-\Delta^2`$. Thus $`\Delta`$ is diagonal (and real), and $`[C_{\rm red},\Delta]`$ is diagonal; its diagonal elements vanish identically, so it is zero. $`\square`$

A real constant $`\Delta=c\,\mathbb 1_{br}`$ always qualifies. Since $`[\Delta,C_{\rm red}]_{KK'}=(\Delta_K-\Delta_{K'})(C_{\rm red})_{KK'}`$, it is the only possibility when the nonzero off-diagonal elements of $`C_{\rm red}`$ connect all joint places.

### Step 3. Expansion of the purity for small $`\lambda`$ (order estimate)

For any unit $`\varphi`$ put $`n_j:=\langle\varphi\vert\Phi_j\vert\varphi\rangle`$ (the numbers of the definition when $`\varphi`$ is sharp), take $`C_{\rm red}`$ as in (2.3), and define

```math
\omega_j^{(k)}:=(\Phi_j-n_j)\,C_f^{\,k}\,\varphi,\qquad k=0,1,2,\dots \qquad\text{(2.8)}
```

$`\varphi`$ is sharp iff $`\omega_j^{(0)}=0`$ for all $`j`$. Suppose some $`\omega_j^{(k)}\neq0`$, and let $`k_0`$ be the smallest such $`k`$. Then $`\langle\varphi\vert\omega_j^{(k_0)}\rangle=0`$: for $`k_0=0`$ by the definition of $`n_j`$, for $`k_0\ge1`$ because $`(\Phi_j-n_j)\varphi=0`$.

1. Write $`C=H_0+W`$ with $`H_0:=C_{\rm red}\otimes\mathbb 1_f+\mathbb 1_{br}\otimes C_f`$ and $`W:=\sum_jB_j\otimes(\Phi_j-n_j)`$. The vector $`\Psi_I(\lambda):=e^{iH_0\lambda}\Psi(\lambda)`$ has the same $`\mathrm{Tr}V^2`$ as $`\Psi(\lambda)`$, because $`e^{iH_0\lambda}`$ is a product of a unitary on $`\mathcal H_{br}`$ and one on $`\mathcal H_f`$. It obeys $`i\,\mathrm d\Psi_I/\mathrm d\lambda=W_I(\lambda)\Psi_I`$ with $`W_I(\mu):=e^{iH_0\mu}We^{-iH_0\mu}`$.
2. By (2.8), $`(\Phi_j-n_j)e^{-iC_f\mu}\varphi=\frac{(-i\mu)^{k_0}}{k_0!}\omega_j^{(k_0)}+O(\mu^{k_0+1})`$, so $`W_I(\mu)\Psi_0=\frac{(-i\mu)^{k_0}}{k_0!}\sum_jB_j\Psi_{br}\otimes\omega_j^{(k_0)}+O(\mu^{k_0+1})`$. In the Dyson series the $`n`$-th term is therefore $`O(\lambda^{k_0+n})`$, and

```math
\Psi_I(\lambda)=\Psi_{br}\otimes\varphi+\frac{(-i\lambda)^{k_0+1}}{(k_0+1)!}\sum_{j}B_j\Psi_{br}\otimes\omega_j^{(k_0)}+O(\lambda^{k_0+2}) . \qquad\text{(2.9)}
```

3. Decompose $`\Psi_I=\Psi_a\otimes\varphi+\chi`$ with $`\chi\in\mathcal H_{br}\otimes\varphi^{\perp}`$. Then the view is $`\lvert\Psi_a\rangle\langle\Psi_a\rvert+V_\chi`$ with $`V_\chi:=\mathrm{Tr}_f\lvert\chi\rangle\langle\chi\rvert`$ and $`\lVert\Psi_a\rVert^2=1-\mathrm{Tr}V_\chi`$, so exactly $`1-\mathrm{Tr}V^2=2\mathrm{Tr}V_\chi-2\langle\Psi_a\vert V_\chi\vert\Psi_a\rangle-(\mathrm{Tr}V_\chi)^2-\mathrm{Tr}V_\chi^2`$. By (2.9), $`\chi`$ is the second term of (2.9) up to $`O(\lambda^{k_0+2})`$, and $`\Psi_a=\Psi_{br}+O(\lambda)`$. Hence

```math
1-\mathrm{Tr}V(\lambda)^2=\frac{2\,\lambda^{2k_0+2}}{\bigl((k_0+1)!\bigr)^2}\,\Bigl\lVert\sum_{j}\bigl(B_j-\langle B_j\rangle_{\Psi_{br}}\bigr)\Psi_{br}\otimes\omega_j^{(k_0)}\Bigr\rVert^2+O(\lambda^{2k_0+3}) . \qquad\text{(2.10)}
```

The squared norm equals $`\sum_{j,j'}\Gamma_{jj'}\,\langle\omega_j^{(k_0)}\vert\omega_{j'}^{(k_0)}\rangle`$ with $`\Gamma_{jj'}:=\langle B_jB_{j'}\rangle_{\Psi_{br}}-\langle B_j\rangle_{\Psi_{br}}\langle B_{j'}\rangle_{\Psi_{br}}`$.

*Lemma (uses LI).* If $`k_0`$ exists, the coefficient in (2.10) is nonzero for some $`\Psi_{br}`$. *Proof.* Expand $`\omega_j^{(k_0)}=\sum_\alpha w_{j\alpha}e_\alpha`$ in an orthonormal basis of $`\mathcal H_f`$. If the coefficient vanished for every $`\Psi_{br}`$, every $`\Psi_{br}`$ would be an eigenvector of $`M_\alpha\otimes\mathbb 1_r`$, $`M_\alpha:=\sum_jw_{j\alpha}B_j`$, for each $`\alpha`$. Then $`M_\alpha\in\mathbb C\,\mathbb 1_b`$, and by LI all $`w_{j\alpha}=0`$, a contradiction. $`\square`$

### Step 4. Sharp field in general: the criterion (item 2a)

**Theorem.** Let $`\varphi`$ be sharp with the numbers $`n_j`$, and assume LI. The view $`V(\lambda)`$ is pure for every $`\Psi_{br}`$ and every $`\lambda\ge0`$ if and only if

```math
\Phi_j\,C_f^{\,k}\,\varphi=n_j\,C_f^{\,k}\,\varphi\qquad\text{for all } j\in J \text{ and all } k\ge0 . \qquad\text{(2.11)}
```

Equivalent forms of (2.11): each $`\Phi_j`$ acts as the number $`n_j`$ on $`\mathcal K_\varphi:=\mathrm{span}\{C_f^{\,k}\varphi\}_{k\ge0}`$ (so $`k\le\dim\mathcal H_f-1`$ suffices); the state $`e^{-iC_f\lambda}\varphi`$ is sharp with the same numbers for every $`\lambda`$; every nonzero component of $`\varphi`$ in an eigenspace of $`C_f`$ is sharp with the numbers $`n_j`$ (standard: $`\mathcal K_\varphi`$ is the span of these components). Item 1 is the case $`\mathcal K_\varphi=\mathbb C\varphi`$.

*Proof.* (Sufficient; no LI.) $`\mathcal K_\varphi`$ is invariant under $`C_f`$ and, by (2.11), under the $`\Phi_j`$. On $`\mathcal H_{br}\otimes\mathcal K_\varphi`$, (2.1) reads $`C=C_{\rm red}\otimes\mathbb 1+\mathbb 1\otimes C_f`$, so

```math
\Psi(\lambda)=\Psi_{\rm red}(\lambda)\otimes e^{-iC_f\lambda}\varphi,\qquad V(\lambda)=\lvert\Psi_{\rm red}(\lambda)\rangle\langle\Psi_{\rm red}(\lambda)\rvert,\qquad V_f(\lambda)=\lvert e^{-iC_f\lambda}\varphi\rangle\langle e^{-iC_f\lambda}\varphi\rvert . \qquad\text{(2.12)}
```

(Necessary; uses LI.) $`1-\mathrm{Tr}V(\lambda)^2`$ is analytic in $`\lambda`$. If it vanishes for all $`\lambda\ge0`$ and all $`\Psi_{br}`$, all its Taylor coefficients at $`0`$ vanish for all $`\Psi_{br}`$. If (2.11) failed, $`k_0\ge1`$ would exist and, by the Lemma, the coefficient of $`\lambda^{2k_0+2}`$ in (2.10) would be nonzero for some $`\Psi_{br}`$. $`\square`$

- **Sharpness is necessary too (LI).** The same argument with $`k_0=0`$ shows: for an arbitrary $`\varphi`$, the view is pure for every $`\Psi_{br}`$ and $`\lambda\ge0`$ iff $`\varphi`$ is sharp and (2.11) holds. Under LI these are exactly the field states in which the body and $`r`$ see definite numbers.
- **Reduced description.** When (2.11) holds, it exists, with the same contract $`C_{\rm red}`$ of (2.3): on $`\mathcal H_{br}\otimes\mathcal K_\varphi`$ every factor of (2.2) is a product, which gives (2.6). The class (2.7) is unchanged. The view of the field is pure but moves; there is no entanglement.
- **Without LI.** (2.11) is still sufficient and (2.12) holds, but (2.11) is no longer necessary. Choose a basis $`\{\mathbb 1_b,A_\alpha\}`$ of $`\mathrm{span}\{\mathbb 1_b,B_j\}`$ and write $`B_j=m_{j0}\mathbb 1_b+\sum_\alpha m_{j\alpha}A_\alpha`$. Then $`C`$ has the form (2.1) with the LI family $`A_\alpha`$, $`\Phi'_\alpha:=\sum_jm_{j\alpha}\Phi_j`$ and $`C_f':=C_f+\sum_jm_{j0}\Phi_j`$; $`\varphi`$ is sharp for the $`\Phi'_\alpha`$ with $`n'_\alpha=\sum_jm_{j\alpha}n_j`$. The necessary and sufficient condition is (2.11) for $`(\varphi,C_f',\{\Phi'_\alpha\})`$, and the reduced contract is $`C_{br}+\sum_\alpha n'_\alpha A_\alpha=C_{\rm red}-\sum_jm_{j0}n_j\,\mathbb 1_{br}`$. Example: $`J=\{1\}`$, $`B_1=\mathbb 1_b`$; the field is not coupled at all, and the view is pure for every $`\varphi`$ although (2.11) can fail.

### Step 5. Example and lowest power (item 2b)

**Example.** A field with two places $`\lvert0\rangle,\lvert1\rangle`$, one index, and $`\gamma\neq0`$:

```math
\Phi_1=\lvert1\rangle\langle1\rvert,\qquad C_f=\gamma\bigl(\lvert0\rangle\langle1\rvert+\lvert1\rangle\langle0\rvert\bigr),\qquad \varphi=\lvert0\rangle:\qquad n_1=0,\qquad \omega_1^{(1)}=\Phi_1C_f\varphi=\gamma\lvert1\rangle\neq0 . \qquad\text{(2.13)}
```

$`\varphi`$ is sharp and (2.11) fails at $`k=1`$.

**Lowest power.** For a sharp $`\varphi`$ that violates (2.11), $`k_0\ge1`$, so by (2.10) $`1-\mathrm{Tr}V^2`$ has no terms in $`\lambda^2`$ or $`\lambda^3`$, and

```math
1-\mathrm{Tr}V(\lambda)^2=\frac{\lambda^4}{2}\sum_{j,j'\in J}\Gamma_{jj'}\,\bigl\langle C_f\varphi\bigm\vert(\Phi_j-n_j)(\Phi_{j'}-n_{j'})\bigm\vert C_f\varphi\bigr\rangle+O(\lambda^5),\qquad \Gamma_{jj'}=\langle B_jB_{j'}\rangle_{\Psi_{br}}-\langle B_j\rangle_{\Psi_{br}}\langle B_{j'}\rangle_{\Psi_{br}} . \qquad\text{(2.14)}
```

The lowest power that can be nonzero is $`\lambda^4`$. Its coefficient is nonzero for some $`\Psi_{br}`$ iff some $`(\Phi_j-n_j)C_f\varphi\neq0`$ (Lemma, LI). If all these vectors vanish, the leading power is $`\lambda^{2k_0+2}`$ with the coefficient of (2.10). For comparison, a $`\varphi`$ that is not sharp has $`k_0=0`$ and starts at $`\lambda^2`$.

### Step 6. Static field that is not sharp (item 3)

Let the $`\Phi_j`$ commute with each other and with $`C_f`$; LI is not assumed. The $`\Phi_j`$ have joint spectral projectors $`P_\nu`$, labelled by the joint eigenvalues $`\nu=(\nu_j)_{j\in J}\in\mathcal N`$, with $`P_\nu P_{\nu'}=\delta_{\nu\nu'}P_\nu`$, $`\sum_\nu P_\nu=\mathbb 1_f`$ and $`[P_\nu,C_f]=0`$. Then

```math
\Phi_j=\sum_{\nu\in\mathcal N}\nu_j\,P_\nu,\qquad C=\sum_{\nu\in\mathcal N}C^{(\nu)}\otimes P_\nu+\mathbb 1_{br}\otimes C_f,\qquad C^{(\nu)}:=C_{br}+\sum_{j\in J}\nu_j\,B_j\otimes\mathbb 1_r . \qquad\text{(2.15)}
```

All summands commute, so $`U(\lambda)=\sum_\nu e^{-iC^{(\nu)}\lambda}\otimes P_\nu e^{-iC_f\lambda}`$. Let $`w_\nu:=\lVert P_\nu\varphi\rVert^2`$, $`S:=\{\nu:w_\nu>0\}`$, $`\varphi_\nu:=P_\nu\varphi/\sqrt{w_\nu}`$ and $`\Psi^{(\nu)}(\lambda):=e^{-iC^{(\nu)}\lambda}\Psi_{br}`$, the evolution in the reduced description $`\mathcal R_\nu`$ (objects $`b`$, $`r`$; contract $`C^{(\nu)}`$; start $`\Psi_{br}`$).

**(a)** The vectors $`e^{-iC_f\lambda}\varphi_\nu`$ are orthonormal, so

```math
\Psi(\lambda)=\sum_{\nu\in S}\sqrt{w_\nu}\;\Psi^{(\nu)}(\lambda)\otimes e^{-iC_f\lambda}\varphi_\nu,\qquad V(\lambda)=\sum_{\nu\in S}w_\nu\,\lvert\Psi^{(\nu)}(\lambda)\rangle\langle\Psi^{(\nu)}(\lambda)\rvert . \qquad\text{(2.16)}
```

The view is the mixture, with weights $`w_\nu`$, of the pure views of the reduced descriptions $`\mathcal R_\nu`$.

**(b)** $`\Pi_i\otimes\mathbb 1_f`$ commutes with $`\mathbb 1_{br}\otimes P_\nu`$. The vector in (2.2) is therefore $`\sum_{\nu\in S}\sqrt{w_\nu}\,\bigl(\Pi_ke^{-iC^{(\nu)}(\lambda_k-\lambda_{k-1})}\cdots\Pi_1e^{-iC^{(\nu)}\lambda_1}\Psi_{br}\bigr)\otimes e^{-iC_f\lambda_k}\varphi_\nu`$, with orthogonal summands, and

```math
p(r_1,\dots,r_k)=\sum_{\nu\in S}w_\nu\,p^{(\nu)}(r_1,\dots,r_k) , \qquad\text{(2.17)}
```

where $`p^{(\nu)}`$ is the statistics of the same schedule in $`\mathcal R_\nu`$. Any unit vector of the range of $`P_\nu`$ is sharp with the numbers $`\nu`$ and satisfies (2.11), because $`[C_f,P_\nu]=0`$; by Step 4 a start $`\Psi_{br}\otimes(\text{such a vector})`$ has the statistics $`p^{(\nu)}`$. Hence a start in which the field is sharp with numbers $`\nu`$ drawn once, with probability $`w_\nu`$, gives exactly (2.17). No schedule of readings on $`b`$ and $`r`$ distinguishes the two starts.

**(c)** From (2.16),

```math
\mathrm{Tr}V(\lambda)^2=\sum_{\nu,\nu'\in S}w_\nu w_{\nu'}\,\bigl\lvert\langle\Psi^{(\nu)}(\lambda)\vert\Psi^{(\nu')}(\lambda)\rangle\bigr\rvert^2=\sum_{\nu,\nu'\in S}w_\nu w_{\nu'}\,\bigl\lvert\langle\Psi_{br}\vert e^{iC^{(\nu)}\lambda}e^{-iC^{(\nu')}\lambda}\vert\Psi_{br}\rangle\bigr\rvert^2 . \qquad\text{(2.18)}
```

The view is pure for every $`\Psi_{br}`$ and every $`\lambda\ge0`$ if and only if

```math
\sum_{j\in J}(\nu_j-\nu'_j)\,B_j\in\mathbb R\,\mathbb 1_b\qquad\text{for all }\nu,\nu'\in S . \qquad\text{(2.19)}
```

*Proof.* Since $`\sum_{\nu,\nu'}w_\nu w_{\nu'}=1`$, purity means that every term of (2.18) has modulus one. ($`\Leftarrow`$) If $`C^{(\nu)}-C^{(\nu')}=c\,\mathbb 1`$, then $`e^{iC^{(\nu)}\lambda}e^{-iC^{(\nu')}\lambda}=e^{ic\lambda}\mathbb 1`$. ($`\Rightarrow`$) Modulus one for every unit $`\Psi_{br}`$ makes every $`\Psi_{br}`$ an eigenvector of the unitary $`e^{iC^{(\nu)}\lambda}e^{-iC^{(\nu')}\lambda}`$, which is then a multiple of $`\mathbb 1`$ for all $`\lambda\ge0`$; so is its derivative at $`\lambda=0`$, $`i(C^{(\nu)}-C^{(\nu')})=i\sum_j(\nu_j-\nu'_j)B_j`$. $`\square`$

Under LI, (2.19) holds iff $`S`$ has one element, that is, iff $`\varphi`$ is sharp. Without LI, (2.19) also holds for those non-sharp $`\varphi`$ whose $`S`$ lies in one coset of $`\{a\in\mathbb R^J:\sum_ja_jB_j\in\mathbb R\,\mathbb 1_b\}`$. When (2.19) fails, the purity is (2.18).

### Step 7. Conventions (item 4; LI assumed)

**(a)** *The replacements of $`C_{br}`$, the $`\Phi_j`$ and $`C_f`$ at fixed $`B_j`$ that leave $`C`$ unchanged are exactly*

```math
\Phi_j\to\Phi_j+a_j\,\mathbb 1_f,\qquad C_f\to C_f+c\,\mathbb 1_f,\qquad C_{br}\to C_{br}-\sum_{j\in J}a_j\,B_j\otimes\mathbb 1_r-c\,\mathbb 1_{br},\qquad a_j,c\in\mathbb R . \qquad\text{(2.20)}
```

*Proof.* (2.20) leaves (2.1) unchanged. Conversely, let $`\delta_{br},\delta_j,\delta_f`$ be self-adjoint changes with $`\delta_{br}\otimes\mathbb 1_f+\sum_jB_j\otimes\delta_j+\mathbb 1_{br}\otimes\delta_f=0`$. Multiply by $`\mathbb 1_{br}\otimes F`$ with $`F`$ self-adjoint and traceless, and take $`\mathrm{Tr}_f`$: $`\sum_j\mathrm{Tr}(F\delta_j)\,B_j+\mathrm{Tr}(F\delta_f)\,\mathbb 1_{br}=0`$. By LI, $`\mathrm{Tr}(F\delta_j)=\mathrm{Tr}(F\delta_f)=0`$ for all such $`F`$, so $`\delta_j=a_j\mathbb 1_f`$ and $`\delta_f=c\,\mathbb 1_f`$; then $`\delta_{br}`$ follows. $`\square`$

(2.20) preserves the sharpness and the stationarity of $`\varphi`$, and

```math
n_j\to n_j+a_j,\qquad e_f\to e_f+c,\qquad C_{\rm red}\to C_{\rm red}-c\,\mathbb 1_{br} . \qquad\text{(2.21)}
```

The $`a_j`$ are independent of each other. For a lapse-type term, $`B_x=\lvert x\rangle\langle x\rvert\otimes G`$ (LI holds iff $`G\notin\mathbb R\,\mathbb 1_{\rm int}`$), the numbers $`a_x`$ move the term $`\sum_xa_x\lvert x\rangle\langle x\rvert\otimes G`$, which is diagonal in the positions, between the pair term with the field and the body's own term: a place-dependent replacement.

*Without LI:* every relation $`\sum_jz_jB_j=z_0\mathbb 1_b`$ adds the replacements $`\Phi_j\to\Phi_j+z_jE`$, $`C_f\to C_f-z_0E`$, with $`E`$ any self-adjoint operator on $`\mathcal H_f`$. If $`E\varphi\notin\mathbb C\varphi`$ they destroy the sharpness for the family, so that "sharp" itself is then not well defined.

**(b)** From (2.21):
- The numbers $`n_j`$ are **not** well defined.
- The differences $`n_j-n_{j'}`$, $`j\neq j'`$, are **not** well defined: they change by $`a_j-a_{j'}`$, which is arbitrary. For a lapse-type term, neither the profile $`n_x`$ nor its difference between two positions is well defined.
- $`C_{\rm red}`$ is well defined up to a real multiple of $`\mathbb 1_{br}`$, which changes the common phase (1.2) in (2.4) and nothing in (2.5), (2.6); this is the case $`\Delta=c\,\mathbb 1`$ of (2.7). Exactly well defined is

```math
\hat C:=C_{\rm red}+e_f\,\mathbb 1_{br}=(\mathbb 1_{br}\otimes\langle\varphi\rvert)\,C\,(\mathbb 1_{br}\otimes\lvert\varphi\rangle) , \qquad\text{(2.22)}
```

  which depends only on $`C`$ and $`\varphi`$, and is therefore the same in every listing of the terms of $`C`$, at fixed $`B_j`$ or not.
- The hypothesis of item 1 is well defined: under LI, $`\varphi`$ is sharp and stationary iff $`C`$ maps $`\mathcal H_{br}\otimes\varphi`$ into itself. ($`\Rightarrow`$) is (2.3). ($`\Leftarrow`$) With $`Q:=\mathbb 1_f-\lvert\varphi\rangle\langle\varphi\rvert`$, $`\sum_jB_j\Psi\otimes Q\Phi_j\varphi+\Psi\otimes QC_f\varphi=0`$ for all $`\Psi`$; taking components in a basis of $`\mathcal H_f`$ and using LI gives $`Q\Phi_j\varphi=0=QC_f\varphi`$.
- Invariant under (2.20) are also the differences between two field states, $`n_j(\varphi)-n_j(\varphi')`$, and in Step 6 the weights $`w_\nu`$, the differences $`\nu_j-\nu'_j`$ and $`C^{(\nu)}-C^{(\nu')}`$.

**On-site blocks.** Let $`\mathcal H_b=\mathcal H_{\rm pos}\otimes\mathcal H_{\rm int}`$ (positions $`x`$, internal labels), $`B_x=\lvert x\rangle\langle x\rvert\otimes G`$, and $`C_{br}=C_b\otimes\mathbb 1_r+\sum_x\lvert x\rangle\langle x\rvert\otimes\mathbb 1_{\rm int}\otimes K_x+R`$, where $`C_b`$ is the body's own term, $`K_x`$ acts on the medium and $`R`$ collects the remaining terms. For an operator $`O`$ on $`\mathcal H_{br}`$ let $`O_{xx}:=(\langle x\rvert\otimes\mathbb 1)\,O\,(\lvert x\rangle\otimes\mathbb 1)`$, an operator on $`\mathcal H_{\rm int}\otimes\mathcal H_r`$. The on-site block of $`C_{\rm red}`$ is

```math
\Omega_x:=(C_{\rm red})_{xx}=(C_b)_{xx}\otimes\mathbb 1_r+\mathbb 1_{\rm int}\otimes K_x+n_x\,G\otimes\mathbb 1_r+R_{xx}=\hat C_{xx}-e_f . \qquad\text{(2.23)}
```

In every listing of $`C`$ in which $`\varphi`$ is sharp and stationary, (2.3) gives $`C_{\rm red}=\hat C-e_f\mathbb 1_{br}`$ with the number $`e_f`$ of that listing; this uses no LI. Hence:
- $`\Omega_x`$ is well defined up to a real constant that is the same at all positions;
- $`\Omega_x-\Omega_{x'}=\hat C_{xx}-\hat C_{x'x'}`$ is well defined exactly;
- the three place-dependent parts of $`\Omega_x`$ are **not** separately well defined. With arbitrary real $`a_x`$, $`k_x`$, the replacements
  1. body and field: $`\Phi_x\to\Phi_x+a_x\mathbb 1_f`$, $`C_b\to C_b-\sum_xa_x\lvert x\rangle\langle x\rvert\otimes G`$, a case of (2.20);
  2. body and medium: $`K_x\to K_x+k_x\mathbb 1`$, $`C_b\to C_b-\sum_xk_x\lvert x\rangle\langle x\rvert\otimes\mathbb 1_{\rm int}`$;
  3. medium and field: $`K_x\to K_x+k_x\mathbb 1`$, and the pair term with the field enlarged by the members $`B'_x=\lvert x\rangle\langle x\rvert\otimes\mathbb 1_{\rm int}`$, $`\Phi'_x=-k_x\mathbb 1_f`$ (not at fixed $`B_j`$; $`\varphi`$ stays sharp)

  leave $`C`$, $`\hat C`$ and every $`\Omega_x`$ unchanged, and change $`n_x`$, $`(C_b)_{xx}`$ and $`K_x`$ by arbitrary functions of $`x`$. In $`\Omega_x-\Omega_{x'}`$ only the sum of the three contributions is well defined.

### Step 8. One object as recording medium and field (item 5)

Here $`\mathcal H=\mathcal H_b\otimes\mathcal H_c`$ with $`\mathcal H_b=\mathcal H_{\rm pos}\otimes\mathcal H_{\rm int}`$, the start is $`\phi\otimes\chi`$, readings are made on $`b`$ only, and

```math
C=C_b\otimes\mathbb 1_c+\sum_x\lvert x\rangle\langle x\rvert\otimes\Bigl(\mathbb 1_{\rm int}\otimes\kappa\,x\,X+G\otimes(\mathbb 1_c+g\,x\,Y)\Bigr) . \qquad\text{(2.24)}
```

This is (2.1) with $`r=\emptyset`$, $`f=c`$, $`C_f=0`$ and the commuting field operators $`\kappa xX`$ and $`\mathbb 1_c+gxY`$, so Step 6 applies (it uses no LI). Let $`P_{y\xi}`$ be the joint spectral projectors of $`(Y,X)`$, $`P_y:=\sum_\xi P_{y\xi}`$, $`w_{y\xi}:=\lVert P_{y\xi}\chi\rVert^2`$ and $`w_y:=\sum_\xi w_{y\xi}`$.

**(a)** Since $`g\neq0`$ and a position $`x\neq0`$ exists, $`\chi`$ is sharp for the $`\Phi_x`$ iff $`Y\chi=y\chi`$ for a real $`y`$. Then $`(\Phi_x-\langle\Phi_x\rangle)\chi=0`$, so the lapse-type term adds nothing to the record vectors, $`u_x=\kappa x\,(X-\langle X\rangle)\chi`$, and (17.15) with $`X\to\kappa X`$ gives $`d_0(x,x')=\kappa\lvert x-x'\rvert\,\sigma_X`$. The condition is

```math
Y\chi=y\,\chi\qquad\text{and}\qquad\sigma_X^2=\langle\chi\vert X^2\vert\chi\rangle-\langle\chi\vert X\vert\chi\rangle^2>0 : \qquad\text{(2.25)}
```

$`\chi`$ lies in one eigenspace $`\mathcal E_y`$ of $`Y`$ and has components in at least two eigenspaces of $`X`$. Such a $`\chi`$ exists iff $`X`$ is not a function of $`Y`$; in particular none exists for $`Y=X`$. Under (2.25), $`\mathcal H_b\otimes\mathcal E_y`$ contains the start and is invariant under $`C`$ and under the readings on $`b`$, and on it

```math
C=\Bigl(C_b+\sum_xn_x\,\lvert x\rangle\langle x\rvert\otimes G\Bigr)\otimes\mathbb 1_c+\sum_x\lvert x\rangle\langle x\rvert\otimes\mathbb 1_{\rm int}\otimes\kappa\,x\,X,\qquad n_x=1+g\,y\,x . \qquad\text{(2.26)}
```

Exactly, for every $`\phi`$ and every schedule of readings on $`b`$: the factor $`\Phi_x`$ amounts to the number $`n_x`$, a profile linear in $`x`$ with slope $`g\,y`$ (flat if $`y=0`$). The body behaves as a body with the own term $`C_b+\sum_xn_x\lvert x\rangle\langle x\rvert\otimes G`$ that is recorded by $`c`$ through $`K_x`$ alone, a description of the form of 17-motion. By Step 7 this term cannot be told from a position-dependent own term of the body's type (A10).

**(b)** If $`\chi`$ is not an eigenvector of $`Y`$, (2.16) with $`\nu=(y,\xi)`$ gives

```math
V_b(\lambda)=\sum_{y,\xi}w_{y\xi}\,\lvert\phi^{(y,\xi)}(\lambda)\rangle\langle\phi^{(y,\xi)}(\lambda)\rvert,\qquad \phi^{(y,\xi)}(\lambda)=e^{-iC_b^{(y,\xi)}\lambda}\phi,\qquad C_b^{(y,\xi)}:=C_b+\sum_x\lvert x\rangle\langle x\rvert\otimes\bigl((1+g\,y\,x)\,G+\kappa\,\xi\,x\,\mathbb 1_{\rm int}\bigr) . \qquad\text{(2.27)}
```

The view of the body is the mixture, with weights $`w_{y\xi}`$, of the pure views of reduced descriptions of the body alone. The reduced description $`(y,\xi)`$ has the profile $`n_x=1+g\,y\,x`$ and the record gradient $`\kappa\xi`$ (the record term reduced to the number $`\kappa\xi x`$). A profile and a gradient occur together exactly for the pairs with $`w_{y\xi}>0`$, with the joint distribution $`w_{y\xi}`$ of the commuting operators $`Y`$ and $`X`$ in $`\chi`$. Summed over $`\xi`$ at fixed $`y`$: $`V_b=\sum_yw_yV_b^{[y]}`$, where $`V_b^{[y]}`$ is the view of the body in the description (2.26) started in $`\phi\otimes\chi_y`$, $`\chi_y:=P_y\chi/\sqrt{w_y}`$, whose record distances are $`\kappa\lvert x-x'\rvert\,\sigma_X^{[y]}`$ with $`\sigma_X^{[y]}`$ the standard deviation of $`X`$ in $`\chi_y`$. If $`X=h(Y)`$, for example $`Y=X`$, then $`\xi=h(y)`$: each profile occurs with exactly one gradient, and $`\sigma_X^{[y]}=0`$ for every $`y`$.

## Result

- **Item 1.** (a) State (2.4) and views (2.5): a product for all $`\lambda`$, both views pure, no entanglement; exact, no LI. (b) Yes: every schedule has the statistics (2.6) of the reduced description with the contract $`C_{\rm red}`$ of (2.3). The contracts that do this are exactly those of (2.7).
- **Item 2.** (a) Under LI the view is pure for every $`\Psi_{br}`$, $`\lambda\ge0`$ iff (2.11); then the state is (2.12) and the reduced description exists with the same $`C_{\rm red}`$ (2.3). Without LI, (2.11) is sufficient but not necessary; the criterion is (2.11) for the reduced family of Step 4. (b) Example (2.13). The lowest power is $`\lambda^4`$ with the coefficient of (2.14); in general $`\lambda^{2k_0+2}`$ with the coefficient of (2.10) (order estimates).
- **Item 3.** (a) Mixture (2.16) of the reduced descriptions with contracts (2.15). (b) Statistics (2.17); readings on $`b`$ and $`r`$ cannot distinguish the start from a sharp field with numbers drawn with probabilities $`w_\nu`$. (c) Pure iff (2.19), which under LI means $`\varphi`$ sharp; otherwise the purity is (2.18).
- **Item 4.** (a) Replacements (2.20), transformations (2.21). (b) Not well defined: $`n_j`$, and $`n_j-n_{j'}`$. Well defined: $`C_{\rm red}`$ up to a real multiple of $`\mathbb 1_{br}`$, and $`\hat C`$ (2.22) exactly. The on-site block (2.23) is well defined up to a constant common to all positions, the differences of blocks exactly; the split of a block into body, medium and field parts is not well defined.
- **Item 5.** (a) Condition (2.25); the factor amounts to the linear profile $`n_x=1+g\,y\,x`$ of (2.26). (b) Mixture (2.27), with profile and record gradient distributed jointly as $`Y`$ and $`X`$ in $`\chi`$.
- **Controls (M9).** (2.13)–(2.14) and (2.16)–(2.18) are the descriptions in which (2.4)–(2.6) fail: a sharp field that does not stay sharp, and a static field that is not sharp.

## Consistency checks

1. **Dimensions.** A change of unit $`\lambda\to\lambda/s`$ takes $`C\to sC`$, so each product $`B_j\otimes\Phi_j`$ and $`C_f`$ scale with $`s`$. With dimensionless $`\Phi_j`$: $`n_j`$, $`w_\nu`$ and $`\mathrm{Tr}V^2`$ are dimensionless, (2.3), (2.15), (2.22) are homogeneous, and the coefficient of (2.10) scales as $`s^{2k_0+2}`$ (two factors $`B_j`$, $`2k_0`$ factors $`C_f`$), which compensates $`\lambda^{2k_0+2}`$. Passed.
2. **$`\Phi_j=\mathbb 1_f`$ for all $`j`$ (this includes a field with one place).** Every $`\varphi`$ is sharp with $`n_j=1`$, (2.11) holds for every $`\varphi`$ and $`C_f`$, all $`\omega_j^{(k)}=0`$, (2.16) has the single sector $`\nu=(1,\dots,1)`$, and $`C_{\rm red}=C_{br}+\sum_jB_j`$. Directly: $`C=(C_{br}+\sum_jB_j)\otimes\mathbb 1_f+\mathbb 1_{br}\otimes C_f`$, the field decouples. Passed.
3. **Two-place field, one index.** Body with two places, $`B_1=\beta\sigma_3`$, $`C_{br}=0`$, $`r=\emptyset`$, $`\Psi_{br}=(\lvert0\rangle+\lvert1\rangle)/\sqrt2`$, so $`\Gamma_{11}=\beta^2`$. (i) The field of (2.13): with $`E_\pm(\lambda)=e^{-i(\pm\beta\Phi_1+C_f)\lambda}\lvert0\rangle`$ one finds $`E_+-E_-=-\lambda^2\beta\gamma\lvert1\rangle+O(\lambda^3)`$ and, by (1.7), $`1-\mathrm{Tr}V^2=\tfrac12\bigl(1-\lvert\langle E_-\vert E_+\rangle\rvert^2\bigr)=\tfrac12\beta^2\gamma^2\lambda^4+O(\lambda^5)`$, equal to (2.14). (ii) Static: $`C_f=0`$, $`\varphi=(\lvert0\rangle+\lvert1\rangle)/\sqrt2`$; (2.18) gives $`1-\mathrm{Tr}V^2=\tfrac12\sin^2\beta\lambda`$, and (2.10) with $`k_0=0`$, $`\lVert\omega_1^{(0)}\rVert^2=\tfrac14`$, gives $`\tfrac12\beta^2\lambda^2`$. Passed.

## Open issues

- (2.10) and (2.14) are expansions for $`\lambda\to0`$; no bound on the remainder, and no range of $`\lambda`$ on which the leading term dominates, is derived here.
- A field whose $`\Phi_j`$ do not commute with $`C_f`$ is treated only through the criterion (2.11) and the expansion (2.10); its view at finite $`\lambda`$ is left to a later package.
- Starts in which the field is entangled with $`b`$ or $`r`$, and readings on the field, are outside the question. In Step 8, readings on the medium are not treated.
- Which operator $`G`$ the field multiplies, and what the well-defined differences $`\Omega_x-\Omega_{x'}`$ of (2.23) mean for a clock and for motion, belong to 03-clock-and-fall. A later package that uses a profile $`n_x`$ must fix the listing, or work with (2.22) and (2.23).

## Methods used

- Invariant subspaces of a self-adjoint operator
- Partial trace, purity of a view
- Interaction picture and Dyson series
- Krylov subspace, analyticity in $`\lambda`$
- Joint spectral decomposition of commuting self-adjoint operators
- Linear independence in tensor products of operator spaces
