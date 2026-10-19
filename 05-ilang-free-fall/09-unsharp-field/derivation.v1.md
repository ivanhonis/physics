# A body in a static field that is not sharp: mixture over sectors, fall, clock rate and the relation (4.24)

- **Subproject:** 05-ilang-free-fall
- **Package:** 09-unsharp-field
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-11

## Setup and assumptions

**Setting (assumption of the package, M8).** The class $`\mathcal S`$ of the question: a body $`b`$, a field $`f`$, a medium $`c`$, with $`C=\sum_\nu C^{(\nu)}_b\otimes P_\nu\otimes\mathbb 1_c+\mathbb 1_b\otimes C_f\otimes\mathbb 1_c+\sum_x\lvert x\rangle\langle x\rvert\otimes\mathbb 1_f\otimes\kappa xX`$, $`[C_f,P_\nu]=0`$, sector contracts in $`\mathcal C_{\rm lev}`$ with linear level profiles, sector generators $`C^{(\nu)}=C^{(\nu)}_b\otimes\mathbb 1_c+\sum_x\lvert x\rangle\langle x\rvert\otimes\kappa xX`$, start $`\phi\otimes\varphi\otimes\chi`$, $`w_\nu=\lVert P_\nu\varphi\rVert^2`$, $`S=\{\nu:w_\nu>0\}`$, and the subclasses $`\mathcal S_{\rm grad}`$, $`\mathcal S^{\mathcal C}_{\rm grad}`$, $`\mathcal S_{\rm a}`$, $`\mathcal S_{\rm c}`$.

**Inputs (as quoted in the question).** (2.1), (2.15)–(2.17), (2.19), (2.20) of 02-field-object; (3.23), (3.36) of 03-clock-and-fall; (4.7), (4.10), (4.11), (4.16), (4.19), (4.22), (4.24) of 04-branch-fall; (5.5), (5.6), (5.11) of 04-ilang-time/05-moving-clock; (8.1), (8.19), (8.20) of 04-ilang-time/08-maximal-speed; (17.15) of 03-ilang-space/17-motion.

**Conventions of this file.**
- A superscript $`(\nu)`$ or $`\nu`$ marks a quantity computed with the sector generator $`C^{(\nu)}`$ from the start $`\phi\otimes\chi`$. $`\mu_k:=m+d_k`$, $`\sigma_w(F):={\rm Var}_w(F)^{1/2}`$, $`\mathbf g^\nu_k:=(G^\nu_k,\mathcal F^\nu_k,g^\nu_{\zeta,k})`$.
- Positions are in label units; $`\bar x=d_0\,\bar x_{\rm lab}\,\hat e`$ with $`d_0=\kappa\sigma_X`$ by (17.15) of 03-ilang-space/17-motion, the same in all sectors because the record term does not depend on the sector.
- Level profiles are those of the effective body contract (8.19) of 04-ilang-time/08-maximal-speed. Results are at leading order in $`\kappa`$ (weak records), first order jointly in the gradients at fixed $`\lambda`$, start and chain, then the long chain.
- Status words: **exact** (an identity or a bound with all constants), **order estimate** (leading behaviour with its calculation). Every result carries its class, its order of limits and its status in brackets.

## Derivation

### Step 1. The mixture (item 1)

**(a)** Apply (2.16) with $`r=\{c\}`$ and $`\Psi_{br}=\phi\otimes\chi`$; the partial trace over $`c`$ and every expectation are linear in the view:

```math
p_x(\lambda)=\sum_{\nu\in S}w_\nu\,p^{(\nu)}_x(\lambda),\qquad \bar x_{\rm lab}(\lambda)=\sum_{\nu\in S}w_\nu\,\bar x^{(\nu)}_{\rm lab}(\lambda),\qquad p(x,a;\lambda)=\sum_{\nu\in S}w_\nu\,p^{(\nu)}(x,a;\lambda).
\qquad\text{(9.1)}
```

[Class: every member of $`\mathcal S`$, every $`\phi,\varphi,\chi`$, every $`\lambda\ge0`$, every $`\kappa`$ and chain. Status: exact.] It rests on three facts only: the start is a product of $`\phi\otimes\chi`$ and $`\varphi`$; the $`P_\nu`$ are orthogonal projectors that commute with $`C_f`$, so the companion states $`e^{-iC_f\lambda}\varphi_\nu`$ stay orthonormal and every cross term between two sectors vanishes in the view (1.7); no reading acts on the field. Functionals that are not linear in the view do not average; for the position label

```math
{\rm Var}(x)(\lambda)=\bigl\langle{\rm Var}^{(\nu)}(x)\bigr\rangle_w+{\rm Var}_w\bigl(\bar x^{(\nu)}_{\rm lab}(\lambda)\bigr)\qquad(\text{exact, from (9.1)}).
\qquad\text{(9.2)}
```

**(b)** Let the reading at $`\lambda_1`$ have the projector $`\Pi_r\otimes\mathbb 1_c\otimes\mathbb 1_f`$, $`p^{(\nu)}(r):=\lVert(\Pi_r\otimes\mathbb 1_c)\Psi^{(\nu)}(\lambda_1)\rVert^2`$ and $`p(r)=\sum_\nu w_\nu p^{(\nu)}(r)>0`$. Writing (2.17) for the schedule $`(r,r_2,\dots,r_k)`$ and dividing by $`p(r)`$:

```math
p(r_2,\dots,r_k\mid r)=\sum_{\nu\in S}w_\nu(r)\,p^{(\nu)}(r_2,\dots,r_k\mid r),\qquad w_\nu(r)=\frac{w_\nu\,p^{(\nu)}(r)}{p(r)};\qquad w_\nu(r)=w_\nu\ \forall\nu\in S\iff p^{(\nu)}(r)=p(r)\ \forall\nu\in S .
\qquad\text{(9.3)}
```

[Class as (9.1), every schedule on body and medium. Status: exact.] A sector with $`p^{(\nu)}(r)=0`$ leaves $`S`$; a sector of weight zero never enters. The reading leaves the weights unchanged for all its outcomes iff its distribution is the same in all sectors of $`S`$. Example: a reading of the clock level (conserved by every sector generator) leaves them unchanged; a position reading at $`\lambda_1>0`$ changes them in general.

**(c)** For a traceless self-adjoint $`T`$ on $`\mathcal H_b\otimes\mathcal H_c`$, $`{\rm Tr}_{bc}[(T\otimes\mathbb 1_f)C]=\sum_\nu{\rm Tr}(TC^{(\nu)})\,P_\nu`$. Different sectors differ by more than a multiple of $`\mathbb 1`$, so a generic $`T`$ gives pairwise different coefficients, and the $`P_\nu`$ are the spectral projectors of an operator fixed by $`C`$. Given the $`P_\nu`$, $`(\mathbb 1\otimes P_\nu)C(\mathbb 1\otimes P_\nu)=C^{(\nu)}\otimes P_\nu+\mathbb 1\otimes C_fP_\nu`$ fixes $`C^{(\nu)}`$ up to $`C^{(\nu)}\to C^{(\nu)}+c_\nu\mathbb 1`$, $`C_fP_\nu\to(C_f-c_\nu)P_\nu`$. The replacement (2.20) with $`\Phi_\nu=P_\nu`$ keeps the spectral projectors and gives $`C^{(\mu)}\to C^{(\mu)}-c\,\mathbb 1`$ for all $`\mu`$ (the terms $`\sum_\nu a_\nu B_\nu`$ cancel). Hence:

```math
\begin{aligned}
&w_\nu:\ \text{yes (fixed by $C$ and $\varphi$, up to the naming of the sectors)};\qquad C^{(\nu)}_b:\ \text{no (only up to }c_\nu\mathbb 1_b);\\
&C^{(\nu)}_b-C^{(\nu')}_b:\ \text{yes under (2.20), no under the shifts }c_\nu\ \text{(only modulo }\mathbb R\,\mathbb 1_b);\qquad \tau^\nu_k,M^\nu_k,G^\nu_k,\mathcal F^\nu_k,g^\nu_{\zeta,k}:\ \text{yes}.
\end{aligned}
\qquad\text{(9.4)}
```

The shift $`c_\nu`$ changes only $`V^\nu_{x,k}\to V^\nu_{x,k}+c_\nu`$, and $`\mathcal F^\nu_k=V^\nu_{x,k}-V^\nu_{x+1,k}`$ is unchanged; the split between body and records is fixed by the effective body contract ((8.19), (8.20) of 04-ilang-time/08-maximal-speed). Without the condition that sectors differ by more than a multiple of $`\mathbb 1_b`$, only the sum of the weights of such sectors is well defined. [Class: every member of $`\mathcal S`$. Status: exact.]

### Step 2. Fall in $`\mathcal S_{\rm grad}`$: first order (item 2a)

In $`\mathcal S_{\rm grad}`$ the level block of the level $`k`$ in the sector $`\nu`$ is $`C_0+G^\nu_k\,\mathcal W_G+\mathcal F^\nu_k\,\mathcal W_{\mathcal F}+g^\nu_{\zeta,k}\,\mathcal W_\zeta`$ with operators $`C_0,\mathcal W_i`$ that do not depend on the sector, and the start $`B_{k,\sigma}[g]\otimes\chi`$ is the same in all sectors and stays in the level $`k`$. On a finite chain $`e^{-iC^{(\nu)}\lambda}`$ is entire in the gradients, so $`p^{(\nu)}_x=p^0_x+\mathbf g^\nu_k\cdot\mathbf q_x+O(\lvert\mathbf g^\nu_k\rvert^2)`$ with sector-independent $`p^0_x,\mathbf q_x`$, and by (9.1)

```math
p_x(\lambda)=p^0_x(\lambda)+\langle\mathbf g_k\rangle_w\cdot\mathbf q_x(\lambda)+O\bigl(\langle\lvert\mathbf g_k\rvert^2\rangle_w\bigr).
\qquad\text{(9.5)}
```

To first order the place weights depend on the state of the field only through the three numbers $`\langle G_k\rangle_w`$, $`\langle\mathcal F_k\rangle_w`$, $`\langle g_{\zeta,k}\rangle_w`$: they are those of the sharp field with the mean gradients. By (2.17) the same holds for every schedule. The second order contains $`\langle g_ig_j\rangle_w=\langle g_i\rangle_w\langle g_j\rangle_w+{\rm Cov}_w(g_i,g_j)`$, so the field state first enters beyond its means through the covariances of the gradients. [Class: $`\mathcal S_{\rm grad}`$, every level, branch, $`g`$, $`\varphi`$; fixed $`\lambda`$ and chain. Status: exact first-order statement.]

The first-order acceleration, its window average and $`a_{k,\sigma}(p)`$ of (4.7) are linear in $`\mathbf g^\nu_k`$ with sector-independent coefficients, and $`S`$ is finite. Averaging (4.10), (4.11) with the weights $`w_\nu`$:

```math
\bar a_{k,\sigma}(p_0):=\lim_{\delta p\to0}\lim_{\Lambda\to\infty}\overline{a^{(1)}}=\langle a_{k,\sigma}(p_0)\rangle_w=a_{k,\sigma}(p_0)\Big\vert_{\mathbf g_k\to\langle\mathbf g_k\rangle_w},\qquad \bar a_{k,\sigma}(0)=\frac{\tau_k^2}{M_k}\bigl(\sigma\langle\mathcal F_k\rangle_w-\langle G_k\rangle_w\bigr),
\qquad\text{(9.6)}
```

with $`\bigl\lvert\overline{a^{(1)}}-\langle\langle a_{k,\sigma}\rangle_g\rangle_w\bigr\rvert\le\frac{2\tau_k}{M_k\Lambda}\langle\mathsf b_k\rangle_w\bigl(X_g+\frac{\tau_k}{2M_k}\bigr)`$ and $`\bigl\lvert\langle\langle a_{k,\sigma}\rangle_g\rangle_w-\bar a_{k,\sigma}(p_0)\bigr\rvert\le\frac12\langle\sup_p\lvert a''_{k,\sigma}\rvert\rangle_w\,\delta p^2`$. [Class: as (9.5). Limits: first order in the gradients, long chain, leading $`\kappa`$, then $`\Lambda\to\infty`$, then $`\delta p\to0`$. Status: exact bounds, exact limit.] Forms of the earlier results for the mean position label:
- (4.16) holds as (9.6), and (4.19) holds with $`G_k,\mathcal F_k`$ replaced by $`\langle G_k\rangle_w,\langle\mathcal F_k\rangle_w`$; in particular both branches with one value $`a`$ iff $`\langle\mathcal F_k\rangle_w=0`$ and $`\tau_k^2\langle G_k\rangle_w/M_k=-a`$ for all $`k`$.
- (4.22) holds in $`\mathcal S^{\mathcal C}_{\rm grad}`$ as: $`\bar a_{k,\pm}(0)`$ is level-independent iff $`\langle\mathcal F\rangle_w=\pm m\bigl(\langle g_m\rangle_w-\langle g_\eta\rangle_w\bigr)`$, with the value $`-\tau^2\langle g_\eta\rangle_w`$.
- (4.24) holds for the mean rates $`\bar r`$ under the condition (9.15) of Step 5.

### Step 3. Spread of the displacement over the sectors (item 2b)

By (4.7) the first-order velocity in the sector $`\nu`$ is $`\lambda\langle a^\nu_{k,\sigma}\rangle_g+\rho^\nu(\lambda)`$. Both terms are linear in $`\mathbf g^\nu_k`$, so $`\rho^\nu=\mathbf g^\nu_k\cdot\boldsymbol\rho`$ with three sector-independent functions bounded for all $`\lambda\ge0`$: $`R_i(g):=\sup_\lambda\lvert\rho_i\rvert<\infty`$ and $`R^\nu:=\sum_i\lvert g^\nu_{i,k}\rvert R_i(g)`$. Integrating from $`0`$: $`\Delta x^\nu_{k,\sigma}(\lambda)=\frac12\lambda^2\langle a^\nu_{k,\sigma}\rangle_g+E^\nu(\lambda)`$ with $`\lvert E^\nu\rvert\le\lambda R^\nu`$. With the Cauchy–Schwarz inequality for $`{\rm Cov}_w`$:

```math
{\rm Var}_w\bigl(\Delta x_{k,\sigma}(\lambda)\bigr)=\frac{\lambda^4}4\,{\rm Var}_w\bigl(\langle a_{k,\sigma}\rangle_g\bigr)+{\rm rem},\qquad\lvert{\rm rem}\rvert\le\lambda^3\,\sigma_w\bigl(\langle a_{k,\sigma}\rangle_g\bigr)\langle R^2\rangle_w^{1/2}+\lambda^2\langle R^2\rangle_w .
\qquad\text{(9.7)}
```

[Class: $`\mathcal S_{\rm grad}`$, every $`k,\sigma,g,\varphi`$, all $`\lambda\ge0`$. Status: exact.] For a start at rest, (4.11) gives $`\lvert\langle a^\nu_{k,\sigma}\rangle_g-a^\nu_{k,\sigma}(0)\rvert\le\frac12\sup\lvert a^{\nu\prime\prime}_{k,\sigma}\rvert\delta p^2`$, and with (4.16)

```math
\lim_{\delta p\to0}\ \lim_{\lambda\to\infty}\frac{{\rm Var}_w\bigl(\Delta x_{k,\sigma}(\lambda)\bigr)}{\lambda^4}=\frac14{\rm Var}_w\bigl(a_{k,\sigma}(0)\bigr)=\frac{\tau_k^4}{4M_k^2}\Bigl[{\rm Var}_w(\mathcal F_k)+{\rm Var}_w(G_k)-2\sigma\,{\rm Cov}_w(\mathcal F_k,G_k)\Bigr].
\qquad\text{(9.8)}
```

[Limits, in this order: first-order term of each sector at fixed $`\lambda`$, $`g`$, chain; long chain; leading $`\kappa`$; $`\lambda\to\infty`$ at fixed $`g`$; $`\delta p\to0`$. Status: exact limit.] The last two limits commute only along sequences with $`R_i(g)/\lambda\to0`$; for $`\delta p\to0`$ at fixed $`\lambda`$ the bound in (9.7) diverges with the position spread $`X_g`$ of the start, and the inputs define no quantity in that order. Since the zeroth-order displacement is the same in all sectors of $`\mathcal S_{\rm grad}`$, (9.7) is also the leading (second) order in the gradients of the term $`{\rm Var}_w(\bar x^{(\nu)}_{\rm lab})`$ of (9.2). Because $`\tau_k^2/M_k>0`$:

```math
\begin{aligned}
(9.8)=0\ \text{for }(k,\sigma)&\iff\sigma\mathcal F^\nu_k-G^\nu_k\ \text{is the same for all }\nu\in S;\qquad\text{for }k\text{ and both }\sigma\iff\mathcal F^\nu_k\text{ and }G^\nu_k\text{ are each the same on }S;\\
\text{for all levels}&\iff\text{the respective condition holds for every }k=0,\dots,N-1 .
\end{aligned}
\qquad\text{(9.9)}
```

[Status: exact.] Exceptional members: a sharp field satisfies (9.9) trivially; sectors of weight zero do not enter; sectors of $`S`$ that differ only in $`g_{\zeta,k}`$ or only in other levels satisfy (9.9) although the field is not sharp. At finite $`\delta p`$ the coefficient $`\frac14{\rm Var}_w(\langle a_{k,\sigma}\rangle_g)`$ vanishes iff $`\langle a^\nu_{k,\sigma}\rangle_g`$ is the same on $`S`$, and differs from (9.8) by $`O(\delta p^2)`$. When the coefficient vanishes, $`\lvert{\rm rem}\rvert\le\lambda^2\langle R^2\rangle_w`$.

### Step 4. Independence of the level: sectors against the mean (item 2c)

(4.19) applied to each sector contract gives, for $`N\ge2`$:

```math
\begin{aligned}
a^\nu_{k,+}(0)\ \text{level-independent }\forall\nu\in S&\iff\forall\nu\in S\ \exists a^\nu_+:\ \tfrac{\tau_k^2}{M_k}(\mathcal F^\nu_k-G^\nu_k)=a^\nu_+\ \forall k;\\
\text{both branches}&\iff\forall\nu\in S:\ \tfrac{\tau_k^2\mathcal F^\nu_k}{M_k}=\tfrac{a^\nu_+-a^\nu_-}2\ \text{ and }\ \tfrac{\tau_k^2G^\nu_k}{M_k}=-\tfrac{a^\nu_++a^\nu_-}2\ \ \forall k
\end{aligned}
\qquad\text{(9.10)}
```

(with one value $`a^\nu`$ in both branches iff $`\mathcal F^\nu_k=0`$ and $`\tau_k^2G^\nu_k/M_k=-a^\nu`$). The values $`a^\nu_\pm`$ may differ between sectors. [Class: $`\mathcal S_{\rm grad}`$. Limits as (4.11). Status: exact.] A level-independent $`\bar a_{k,\sigma}(0)`$ is by (9.6) one condition on the means and does **not** imply (9.10). Control, a member of $`\mathcal S^{\mathcal C}_{\rm grad}`$ with two sectors, $`\varepsilon\ne0`$:

```math
w_1=w_2=\tfrac12,\quad g^{1,2}_\eta=g,\quad g^{1,2}_m=g\pm\varepsilon,\quad g^\nu_\zeta=\mathcal F^\nu=0:\qquad a^{1,2}_{k,\sigma}(0)=-\tau^2g\mp\frac{\tau^2\varepsilon m}{\mu_k},\qquad\bar a_{k,\sigma}(0)=-\tau^2g\ \ \forall k,\sigma .
\qquad\text{(9.11)}
```

The mean drift is the same for all levels in both branches, the sector drifts are not. In readings of the position, the mean and by (9.5) every first-order statistic are the same in the two cases. A start in one level determines, through (9.1) and (9.2), the distribution over the sectors of the sector drifts (weights $`w_\nu`$ at the values $`a^\nu_{k,\sigma}(0)`$), whose first moment is $`\bar a_{k,\sigma}(0)`$ and whose variance is (9.8). Under (9.10) this distribution is the same for all levels; in the control $`{\rm Var}_w(a_{k,\sigma}(0))=\tau^4\varepsilon^2m^2/\mu_k^2`$ depends on $`k`$. The distinction is of second order in the gradients. A single body cannot compare two levels inside one sector, so a member that violates (9.10) with a level-independent distribution is not distinguished by such readings.

### Step 5. Clock in $`\mathcal S^{\mathcal C}_{\rm grad}`$ (item 3)

**(a)** By (9.1) the statistics of the clock label is the mixture with the weights $`w_\nu`$ of the sector statistics (3.36), with the local parameters $`\tau^{0,\nu},m^{0,\nu},\eta^{0,\nu}`$ of the sector; in the wide-start form each sector is a ring clock with the advance $`\vartheta^\nu=r^\nu(x_0)\lambda`$, $`r^\nu(x_0)=\eta^\nu_{x_0}/\lambda_0`$ by (3.23). With $`\eta^\nu_{x_0}=1+g^\nu_\eta x_0`$:

```math
\bar\vartheta(\lambda;x_0)=\bigl(1+\langle g_\eta\rangle_wx_0\bigr)\frac\lambda{\lambda_0},\qquad\bar r(x_0):=\frac{\mathrm d\bar\vartheta}{\mathrm d\lambda}=\frac{1+\langle g_\eta\rangle_wx_0}{\lambda_0},\qquad{\rm Var}_w\bigl(\vartheta(\lambda;x_0)\bigr)={\rm Var}_w(g_\eta)\,x_0^2\,\frac{\lambda^2}{\lambda_0^2} .
\qquad\text{(9.12)}
```

The standard deviation stays below $`\epsilon`$ ticks (advance $`\epsilon`$) iff $`\lambda<\lambda_\epsilon:=\epsilon\lambda_0/\bigl(\lvert x_0\rvert\sigma_w(g_\eta)\bigr)`$, that is for fewer than $`\epsilon(1+\langle g_\eta\rangle_wx_0)/(\lvert x_0\rvert\sigma_w(g_\eta))`$ mean ticks; for all $`\lambda`$ if $`x_0\,\sigma_w(g_\eta)=0`$. At finite $`W`$: $`\bar r_W=\langle\frac{\eta_{x_0}}{\lambda_0}(1-\varsigma_W)\rangle_w`$ and $`\lvert\bar r_W-\bar r\rvert\le\langle\frac{\eta_{x_0}}{\lambda_0}\delta_W^2\frac{\tau^{0\,2}}{m_{x_0}^2}\rangle_w`$. [Class: $`\mathcal S^{\mathcal C}_{\rm grad}`$, every $`x_0`$, every $`\varphi`$. Orders: those of (3.36) in every sector (zeroth order in the gradients at the local parameters, first order in the level spacing), then $`W\to\infty`$, uniform because $`S`$ is finite. Status: the mixture is exact; (9.12) is exact given (3.23).] The place $`x=0`$ is the place where the factors $`\eta^\nu_x`$ of all sectors agree.

**(b)** Two runs with the starts $`S_{\rm clock}(x_{1,2})\otimes\varphi\otimes\chi`$ (the same $`\varphi`$), their mean advances compared at equal $`\lambda`$ (this uses the order of $`\lambda`$, A8):

```math
\frac{\bar r(x_1)}{\bar r(x_2)}=\frac{\bar\vartheta(\lambda;x_1)}{\bar\vartheta(\lambda;x_2)}=\frac{1+\langle g_\eta\rangle_wx_1}{1+\langle g_\eta\rangle_wx_2},\qquad\frac{\bar r(x+1)-\bar r(x)}{\bar r(x)}=\frac{\langle g_\eta\rangle_w}{1+\langle g_\eta\rangle_wx}=\langle g_\eta\rangle_w+O(g^2).
\qquad\text{(9.13)}
```

[Status: exact given (9.12); independent of $`\lambda`$ and of the unit of $`\lambda`$.] It is the ratio of the means, not the mean of the sector ratios $`\eta^\nu_{x_1}/\eta^\nu_{x_2}`$: two runs do not share a sector.

**(c)** With $`\vartheta^\nu=(1+g^\nu_\eta x_0)\lambda/\lambda_0`$ and $`\Delta x^\nu_{k,\sigma}`$ of Step 3 at the same $`\lambda`$, and $`a^\nu_{k,\sigma}(0)=\tau^2(\sigma\mathcal F^\nu-mg^\nu_m-d_kg^\nu_\eta)/\mu_k`$ from (4.16):

```math
{\rm Cov}_w\bigl(\vartheta,\Delta x_{k,\sigma}\bigr)=\frac{x_0\lambda^3}{2\lambda_0}{\rm Cov}_w\bigl(g_\eta,\langle a_{k,\sigma}\rangle_g\bigr)+{\rm rem}',\qquad\lim_{\delta p\to0}\lim_{\lambda\to\infty}\frac{{\rm Cov}_w}{\lambda^3}=\frac{x_0\tau^2}{2\lambda_0\mu_k}\Bigl[\sigma{\rm Cov}_w(g_\eta,\mathcal F)-m\,{\rm Cov}_w(g_\eta,g_m)-d_k{\rm Var}_w(g_\eta)\Bigr],
\qquad\text{(9.14)}
```

with $`\lvert{\rm rem}'\rvert\le\lvert x_0\rvert\lambda^2\sigma_w(g_\eta)\langle R^2\rangle_w^{1/2}/\lambda_0`$. [Class: $`\mathcal S^{\mathcal C}_{\rm grad}`$. Limits as (9.8). Status: exact.] For $`x_0\ne0`$ the advance and the leading displacement are functions of each other on $`S`$ iff $`g^\nu_\eta=g^{\nu'}_\eta\Leftrightarrow a^\nu_{k,\sigma}(0)=a^{\nu'}_{k,\sigma}(0)`$ for all $`\nu,\nu'\in S`$. A sufficient condition, which gives the same affine relation for all levels, is $`\mathcal F^\nu=\sigma m(g^\nu_m-g^\nu_\eta)`$ in every sector of $`S`$: then $`a^\nu_{k,\sigma}(0)=-\tau^2g^\nu_\eta`$, the limit in (9.14) is $`-x_0\tau^2{\rm Var}_w(g_\eta)/(2\lambda_0)`$, and the correlation is $`-{\rm sgn}(x_0)`$. At $`x_0=0`$ the advance is the same in all sectors and the covariance vanishes.

**(d)** By (9.6), $`\bar a_{k,+}(0)=\tau^2\bigl(\langle\mathcal F\rangle_w-m\langle g_m\rangle_w-d_k\langle g_\eta\rangle_w\bigr)/\mu_k`$, and by (9.13) with $`v_{\max}=\tau d_0`$ the right side of (4.24) for the rates $`\bar r`$ is $`-d_0\tau^2\langle g_\eta\rangle_w\hat e`$. Equating:

```math
d_0\,\bar a_{k,+}(0)\,\hat e=-\frac{v_{\max}^2}{d_0}\,\frac{\bar r(x+1)-\bar r(x)}{\bar r(x)}\,\hat e\quad\iff\quad\bigl\langle\mathcal F-m(g_m-g_\eta)\bigr\rangle_w=0 .
\qquad\text{(9.15)}
```

[Class: $`\mathcal S^{\mathcal C}_{\rm grad}`$, upper branch; first order in the gradients, leading $`\kappa`$, limits of (9.6). Status: exact.] The condition does not contain $`k`$: it holds for one level iff for all, and then $`\bar a_{k,+}(0)=-\tau^2\langle g_\eta\rangle_w`$ (the lower branch has $`-m`$ in place of $`m`$). Sector by sector, (4.24) holds in the sector $`\nu`$ iff $`\mathcal F^\nu=m(g^\nu_m-g^\nu_\eta)`$ (by (4.22)). This for all $`\nu\in S`$ is sufficient for (9.15) for every $`w`$ on $`S`$, and not necessary: in the control (9.11) the relation (9.15) holds and (4.24) holds in no sector, and for $`w_1\ne w_2`$ it fails, $`\langle\mathcal F-m(g_m-g_\eta)\rangle_w=-m\varepsilon(w_1-w_2)`$. The relation for the means is a property of the contract together with the state of the field.

### Step 6. Sector data of $`\mathcal S_{\rm a}`$ and $`\mathcal S_{\rm c}`$ (item 4a)

In $`\mathcal S_{\rm a}`$ the on-site block of the level $`k`$ is $`(n^\nu+\gamma^\nu x)\mu_k\sigma_3`$ and the motion term is $`A`$. In $`\mathcal S_{\rm c}`$, $`\frac12\{\hat x,\lvert x+1\rangle\langle x\rvert\}=(x+\frac12)\lvert x+1\rangle\langle x\rvert`$ gives the hopping factor $`n^\nu+\gamma^\nu(x+\frac12)`$, and the on-site block is the same. The effective contract adds $`\mathcal F^\nu_k=-\kappa\langle X\rangle`$, the same for all sectors and levels; it vanishes at the leading order in $`\kappa`$ used here. Each sector is the member of the class $`\mathcal C`$ with the data $`(\tau^\nu,\,n^\nu m,\,N,\,\lambda_0/n^\nu)`$ (since $`n^\nu D`$ is $`D`$ with $`\lambda_0\to\lambda_0/n^\nu`$) and $`g^\nu:=\gamma^\nu/n^\nu`$:

```math
\begin{array}{l|c|c}
& \mathcal S_{\rm a} & \mathcal S_{\rm c}\\\hline
\tau^\nu_k,\ M^\nu_k,\ G^\nu_k,\ g^\nu_{\zeta,k},\ \mathcal F^\nu_k & \tau,\ n^\nu\mu_k,\ \gamma^\nu\mu_k,\ 0,\ 0 & n^\nu\tau,\ n^\nu\mu_k,\ \gamma^\nu\mu_k,\ \gamma^\nu/n^\nu,\ 0\\
\text{class }\mathcal C & \text{variant (a)},\ g=g^\nu,\ \tau^\nu=\tau & \text{variant (c)},\ g=g^\nu,\ \tau^\nu=n^\nu\tau\\
r^\nu(x)\ \text{(3.23), wide start} & (n^\nu+\gamma^\nu x)/\lambda_0 & (n^\nu+\gamma^\nu x)/\lambda_0\\
v^\nu_{\max}\ \text{(5.11)} & \tau d_0 & n^\nu\tau d_0\\
a^\nu_{k,\pm}(0)\ \text{(4.16)} & -\tau^2\gamma^\nu/n^\nu & -\tau^2n^\nu\gamma^\nu
\end{array}
\qquad\text{(9.16)}
```

Within a sector the drift acceleration from rest is the same for all levels and both branches (yes, both subclasses), and (4.24) holds with the sector's own $`v^\nu_{\max}`$ (yes, both): $`-(v^{\nu}_{\max})^2\gamma^\nu/(d_0n^\nu)=d_0a^\nu_{k,\pm}(0)`$ at first order. [Class: every member of $`\mathcal S_{\rm a}`$, $`\mathcal S_{\rm c}`$. Orders: those of (3.23), (4.16), (4.24). Status: exact given the inputs.]

### Step 7. Branch starts in different sectors (item 4b)

By (5.6) of 04-ilang-time/05-moving-clock, $`\tan\theta^\nu_k=-\tau^\nu_k\sin p/M^\nu_k`$. In $`\mathcal S_{\rm c}`$ this is $`-\tau\sin p/\mu_k`$ for every $`\nu`$: the branches and branch starts are the same in all sectors. In $`\mathcal S_{\rm a}`$, with $`\Delta^\nu_k(p):=\theta^{\nu_0}_k-\theta^\nu_k=\arctan\frac{\tau\sin p}{n^\nu\mu_k}-\arctan\frac{\tau\sin p}{n^{\nu_0}\mu_k}`$:

```math
\beta^{\nu_0}_{k,\sigma}=\cos\tfrac{\Delta^\nu_k}2\,\beta^\nu_{k,\sigma}+\sigma\sin\tfrac{\Delta^\nu_k}2\,\beta^\nu_{k,-\sigma},\qquad{\sf W}^\nu_k[g]:=\bigl\langle\sin^2\tfrac{\Delta^\nu_k}2\bigr\rangle_g\le\frac{\tau^2}{4\mu_k^2}\Bigl(\frac1{n^\nu}-\frac1{n^{\nu_0}}\Bigr)^2\delta p^2\ \ (\text{start at rest}),
\qquad\text{(9.17)}
```

so $`B^{\nu_0}_{k,\sigma}[g]`$ has in the sector $`\nu`$ the amplitudes $`g\cos\frac{\Delta}2`$ in the branch $`\sigma`$ and $`\sigma g\sin\frac\Delta2`$ in the branch $`-\sigma`$. The bound uses $`\sin^2\frac\Delta2\le\frac{\Delta^2}4`$, $`\lvert\arctan u-\arctan u'\rvert\le\lvert u-u'\rvert`$ and $`\langle\sin^2p\rangle_g\le\delta p^2`$; it is the leading term when $`\langle p^4\rangle_g=o(\delta p^2)`$. [Status: exact identity and bound.] For smooth $`g`$ the start is a branch start of the sector $`\nu`$ iff $`n^\nu=n^{\nu_0}`$.

For $`n^\nu\ne n^{\nu_0}`$ write the start as $`\phi_\sigma+\phi_{-\sigma}`$ in the branches of $`\nu`$. The first-order velocity is a quadratic form, $`v^{(1)}[\phi]=v^{(1)}[\phi_\sigma]+v^{(1)}[\phi_{-\sigma}]+\mathsf X(\lambda)`$. By (4.7) for each component, and since $`a^\nu_{k,+}(p)=a^\nu_{k,-}(p)=:a^\nu_k(p)`$ for $`\mathcal F=0`$, the first two terms are $`\lambda\langle a^\nu_k\rangle_g`$ plus a bounded rest. For the cross part $`\mathsf X`$: on momentum amplitudes $`\hat x=i\partial_p`$, the level block is $`H_0(p)+G\hat x\sigma_3`$ with $`H_0=\omega(P_+-P_-)`$, the velocity is $`H_0'(p)=-\tau\cos p\,\sigma_1`$, and its first-order Heisenberg term is $`\mathcal V_1(\lambda)=i\int_0^\lambda\mathrm ds\,[W_I(s),v_I(\lambda)]`$ with $`W=G\hat x\sigma_3`$. In the blocks $`P_\sigma\mathcal V_1P_{-\sigma}`$ every term carries $`e^{\pm2i\omega\lambda}`$ or is bounded; the growing ones are $`\lambda\,c(p)e^{\pm2i\omega\lambda}`$ (branch-diagonal part of $`W_I`$ against the off-diagonal part of $`v_I`$) and $`\lambda^2\omega'(p)c(p)e^{\pm2i\omega\lambda}`$ (factors $`s`$, $`\lambda`$ arise only from $`\partial_pe^{\pm i\omega s}`$, always with $`\omega'`$). One integration by parts ($`\omega'e^{2i\omega\lambda}=\partial_pe^{2i\omega\lambda}/2i\lambda`$) reduces the second kind to the first, and stationary phase at the non-degenerate stationary points $`p\in\{0,\pi,\pm\frac\pi2\}`$ of $`\omega`$ gives $`\int\mathrm dp\,A(p)e^{\pm2i\omega\lambda}=O(\lambda^{-1/2})`$ for smooth $`A`$. Hence $`\mathsf X(\lambda)=O(\lambda^{1/2})`$, and

```math
\mathcal S_{\rm a}:\quad\overline{a^{(1),\nu}}=\langle a^\nu_k\rangle_g+O(\Lambda^{-1/2})\ \ (\Lambda\to\infty,\ \text{fixed }\lambda_1,g),\qquad\lim_{\delta p\to0}\lim_{\Lambda\to\infty}\overline{a^{(1),\nu}}=a^\nu_k(0)=-\tau^2\frac{\gamma^\nu}{n^\nu}\quad\forall\nu\in S .
\qquad\text{(9.18)}
```

[Status: order estimate for the cross part, with the calculation above; exact for the two branch parts.] Statement: in $`\mathcal S_{\rm c}`$, (4.16) gives the sector drift acceleration in every sector of $`S`$ for every branch start, with the limits and the exact bounds of (4.10), (4.11), uniform on the finite $`S`$. In $`\mathcal S_{\rm a}`$ this holds at finite $`\delta p`$ and $`\Lambda`$ only in the sectors with $`n^\nu=n^{\nu_0}`$; in the others it holds for starts at rest in the limit $`\Lambda\to\infty`$ followed by $`\delta p\to0`$, in which $`{\sf W}^\nu_k\to0`$ by (9.17), without the bound (4.10).

### Step 8. Means over the sectors in $`\mathcal S_{\rm a}`$ and $`\mathcal S_{\rm c}`$ (item 4c)

From (9.16) and (9.1), for the start $`S_{\rm clock}(0)`$ (at $`x_0`$: $`n\to n+\gamma x_0`$), in both subclasses:

```math
\bar\vartheta(\lambda)=\bar n\,\frac\lambda{\lambda_0},\qquad{\rm Var}_w(\vartheta)={\rm Var}_w(n)\frac{\lambda^2}{\lambda_0^2},\qquad\bar r(x)=\frac{\bar n+\bar\gamma x}{\lambda_0},\qquad\bar\varrho=\frac{\bar r(1)-\bar r(0)}{\bar r(0)}=\frac{\bar\gamma}{\bar n},\qquad\bar a=\begin{cases}-\tau^2\langle\gamma/n\rangle_w&\mathcal S_{\rm a}\\-\tau^2\langle n\gamma\rangle_w&\mathcal S_{\rm c}\end{cases}
\qquad\text{(9.19)}
```

Here the advance is not sharp already at $`x_0=0`$: its standard deviation is below $`\epsilon`$ ticks iff $`\lambda<\epsilon\lambda_0/\sigma_w(n)`$. By (9.18) and Step 7, $`\bar a`$ is also the drift acceleration from rest of the mean position label. For $`\bar\gamma\ne0`$, using $`\langle\gamma\rangle_w=\langle n\rangle_w\langle\gamma/n\rangle_w+{\rm Cov}_w(n,\gamma/n)`$ and $`\langle n\gamma\rangle_w=\bar n\bar\gamma+{\rm Cov}_w(n,\gamma)`$:

```math
\frac{\bar a}{\bar\varrho}=-\tau^2\,\frac{\bar n\,\langle\gamma/n\rangle_w}{\bar\gamma}\ \ (\mathcal S_{\rm a}),\qquad\frac{\bar a}{\bar\varrho}=-\tau^2\bar n^2\Bigl(1+\frac{{\rm Cov}_w(n,\gamma)}{\bar n\bar\gamma}\Bigr)\ \ (\mathcal S_{\rm c});\qquad\text{sharp value: }-\tau^2\ (\mathcal S_{\rm a}),\ \ -\tau^2\bar n^2\ (\mathcal S_{\rm c}),
\qquad\text{(9.20)}
```

where the sharp value is $`-v_{\max}^2/d_0^2`$ of (4.24) for the factor $`\bar n+\bar\gamma x`$, by (9.16). Equality holds iff $`{\rm Cov}_w(n,\gamma/n)=0`$ in $`\mathcal S_{\rm a}`$, and iff $`{\rm Cov}_w(n,\gamma)=0`$ in $`\mathcal S_{\rm c}`$. A sharp $`n`$ ($`{\rm Var}_w(n)=0`$) is sufficient in both and necessary in neither. Controls with $`n`$ not sharp: $`\gamma^\nu=g\,n^\nu`$ gives equality in $`\mathcal S_{\rm a}`$ and $`\bar a/\bar\varrho=-\tau^2\langle n^2\rangle_w`$ in $`\mathcal S_{\rm c}`$; a sector-independent $`\gamma`$ gives equality in $`\mathcal S_{\rm c}`$ and $`-\tau^2\bar n\langle1/n\rangle_w`$, of modulus above $`\tau^2`$, in $`\mathcal S_{\rm a}`$. For a narrow distribution, $`u:=(n-\bar n)/\bar n`$ with $`\lvert u\rvert\le\epsilon<1`$ on $`S`$ and $`\frac1{1+u}=1-u+u^2-\frac{u^3}{1+u}`$:

```math
\mathcal S_{\rm a}:\quad\frac{\bar a}{\bar\varrho}=-\tau^2\Bigl[1+\frac{{\rm Var}_w(n)}{\bar n^2}-\frac{{\rm Cov}_w(n,\gamma)}{\bar n\bar\gamma}+\rho_3\Bigr],\qquad\rho_3=\frac{\langle(\gamma-\bar\gamma)u^2\rangle_w-\langle\gamma u^3/(1+u)\rangle_w}{\bar\gamma},
\qquad\text{(9.21)}
```

with $`\lvert\rho_3\rvert\le\epsilon^2\bigl[\max_S\lvert\gamma-\bar\gamma\rvert+\epsilon\max_S\lvert\gamma\rvert/(1-\epsilon)\bigr]/\lvert\bar\gamma\rvert`$, of third order in the joint spread of $`n`$ and $`\gamma`$; in $`\mathcal S_{\rm c}`$ the deviation $`{\rm Cov}_w(n,\gamma)/(\bar n\bar\gamma)`$ of (9.20) is exact. [Class: every member of $`\mathcal S_{\rm a}`$, $`\mathcal S_{\rm c}`$, every $`\varphi`$ with $`\bar\gamma\ne0`$. Orders: those of (9.16), (9.18). Status: (9.19)–(9.21) exact given (9.16); $`\bar a`$ as a drift of the mean label in $`\mathcal S_{\rm a}`$ has the status of (9.18).]

## Result

Summary (item 5). "Sector" is every sector of $`S`$; orders are first order in the gradients and leading order in $`\kappa`$, with the limits of the cited tags.

| Quantity | Within every sector | Means in $`\mathcal S_{\rm grad}`$ | Means in $`\mathcal S_{\rm a}`$ | Means in $`\mathcal S_{\rm c}`$ |
| --- | --- | --- | --- | --- |
| Rate of the clock at $`x`$ | $`\eta^\nu_x/\lambda_0`$, (3.23) | $`(1+\langle g_\eta\rangle_wx)/\lambda_0`$; spread of the advance $`\lvert x\rvert\sigma_w(g_\eta)\lambda/\lambda_0`$, (9.12) | $`(\bar n+\bar\gamma x)/\lambda_0`$; spread $`\sigma_w(n+\gamma x)\lambda/\lambda_0`$, (9.19) | as $`\mathcal S_{\rm a}`$, (9.19) |
| Ratio of the rates at $`x_1,x_2`$ | $`\eta^\nu_{x_1}/\eta^\nu_{x_2}`$ | ratio of the means, (9.13) | $`(\bar n+\bar\gamma x_1)/(\bar n+\bar\gamma x_2)`$ | as $`\mathcal S_{\rm a}`$ |
| Drift acceleration from rest | (4.16); (9.16) | (4.16) at the mean gradients, (9.6); spread (9.8) | $`-\tau^2\langle\gamma/n\rangle_w`$, (9.19), limit (9.18) | $`-\tau^2\langle n\gamma\rangle_w`$, (9.19) |
| Its independence of the level | (4.19), i.e. (9.10) | (4.19) at the mean gradients; weaker than (9.10), control (9.11) | yes, both branches, (9.16) | yes, both branches, (9.16) |
| Relation (4.24) | iff $`\mathcal F^\nu=m(g^\nu_m-g^\nu_\eta)`$; always in $`\mathcal S_{\rm a}`$, $`\mathcal S_{\rm c}`$ with $`v^\nu_{\max}`$ | iff $`\langle\mathcal F-m(g_m-g_\eta)\rangle_w=0`$, (9.15) | iff $`{\rm Cov}_w(n,\gamma/n)=0`$, (9.20), (9.21) | iff $`{\rm Cov}_w(n,\gamma)=0`$, with $`v_{\max}=\bar n\tau d_0`$, (9.20) |

Tagged results: (9.1) mixture; (9.2) total variance; (9.3) weights after a reading; (9.4) well-defined quantities; (9.5) first-order place weights; (9.6) mean drift acceleration; (9.7), (9.8) spread of the displacement; (9.9) its vanishing; (9.10) level independence in every sector; (9.11) control; (9.12) clock mixture; (9.13) ratio of mean rates; (9.14) covariance; (9.15) relation (4.24) for the means; (9.16) sector data of $`\mathcal S_{\rm a}`$, $`\mathcal S_{\rm c}`$; (9.17) branch components; (9.18) drift in every sector of $`\mathcal S_{\rm a}`$; (9.19) means; (9.20) ratio $`\bar a/\bar\varrho`$; (9.21) leading deviation.

## Consistency checks

1. **Dimensions.** Labels are pure numbers; $`\tau,M,G,\mathcal F,1/\lambda_0`$ are costs ($`1/\lambda`$), $`g_\zeta,g_m,g_\eta,n,\gamma/n`$ are pure numbers. (9.6): $`\tau^2G/M\sim\lambda^{-2}`$. (9.8): $`\lambda^4\cdot\lambda^{-4}`$, a pure number. (9.14): $`\lambda^3\tau^2/\lambda_0\sim1`$. (9.20): $`\bar a/\bar\varrho\sim\tau^2=v_{\max}^2/d_0^2`$. Passed.
2. **Sharp field.** For $`S=\{\nu\}`$ all $`{\rm Var}_w`$ and $`{\rm Cov}_w`$ vanish: (9.3) gives $`w_\nu(r)=1`$, (9.6) is (4.16), (9.8) and (9.14) vanish, (9.13) is $`\eta_{x_1}/\eta_{x_2}`$, (9.15) is the condition of (4.22), (9.20) gives the sharp values, and $`\rho_3=0`$. Passed.
3. **Two sectors with equal weights, control (9.11).** Direct evaluation: $`\frac12(a^1+a^2)=-\tau^2g`$ and $`{\rm Var}_w=\frac14(a^1-a^2)^2=\tau^4\varepsilon^2m^2/\mu_k^2`$, equal to (9.8) with $`{\rm Var}_w(G_k)=m^2\varepsilon^2`$, $`M_k=\mu_k`$; (9.15) reads $`\frac12(-m\varepsilon)+\frac12(m\varepsilon)=0`$. Passed.

## Open issues

- The cross part of the first-order velocity in $`\mathcal S_{\rm a}`$, (9.18), is an order estimate $`O(\lambda^{1/2})`$ by stationary phase; a bound with explicit constants, of the kind of (4.10), was not derived.
- The constants $`R_i(g)`$ of (9.7) are taken from the boundedness stated in (4.7); their explicit form in terms of $`X_g`$ is not quoted, so the joint limit $`\lambda\to\infty`$, $`\delta p\to0`$ of (9.8) is stated only in the order given.
- The term $`\langle{\rm Var}^{(\nu)}(x)\rangle_w`$ of (9.2) at second order in the gradients is outside the scope; only the term over the sectors is determined.

## Methods used

- Block decomposition of a contract over commuting projectors; mixture (incoherent sum) over sectors
- Conditional weights after a reading (Bayes rule from joint statistics)
- First-order perturbation theory (Dyson expansion) in the gradients; linearity in the sector gradients
- Law of total variance; Cauchy–Schwarz inequality for covariances
- Branch (eigenvector) decomposition of two-band blocks; stationary phase and integration by parts for oscillatory integrals
- Moment expansion of a ratio of means
