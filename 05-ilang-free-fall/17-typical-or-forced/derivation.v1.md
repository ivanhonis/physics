# Typical or forced: how special the universal couplings of one body are

- **Subproject:** 05-ilang-free-fall
- **Package:** 17-typical-or-forced
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-18

## Setup and assumptions

**Description studied (assumption, M8, M9).** One body of Model D type, the only instance of its type ($`\tau>0`$, $`m>0`$, $`N\ge2`$, $`d_k=\frac{2\pi k}{N\lambda_0}`$, $`M_k=m+d_k`$), recorded through $`K_x=\kappa xX`$ in the weak-record regime, with $`\kappa x\langle X\rangle`$ counted in the on-site potential. A field $`f`$ in a sharp state $`\varphi`$ with linear profile $`N(x)=n_1x`$, $`n_1\neq0`$ (origin at the zero of the profile), coupled by the lapse-type pair term $`\sum_x\lvert x\rangle\langle x\rvert\otimes G\otimes\Phi_x`$ with
$`G=\sigma_3\otimes(\alpha_0\mathbb 1_N+\alpha_1D)+\mathbb 1_2\otimes(\beta_0\mathbb 1_N+\beta_1D)`$, $`\alpha_i,\beta_i\in\mathbb R`$, and optionally by a factor on the motion term whose sharp profile gives $`\zeta_x=1+g_\zeta(x+\frac12)`$. $`G`$ and Model D are diagonal in $`\lvert f_k\rangle`$, so the levels decouple, and on level $`k`$ the body sees the level block of 04-branch-fall with $`\tau_k=\tau`$ and
```math
M_{x,k}=M_k+G_kx,\ \ G_k=mg_m+d_kg_\eta,\qquad V_{x,k}=-\mathcal F_kx,\ \ \mathcal F_k=\mathcal F+d_k\mathcal F_1,\qquad
mg_m=n_1\alpha_0,\ \ g_\eta=n_1\alpha_1,\ \ \mathcal F=\mathcal F_{\rm rec}-n_1\beta_0,\ \ \mathcal F_1=-n_1\beta_1,
\qquad\text{(17.1)}
```
with $`\mathcal F_{\rm rec}:=-\kappa\langle X\rangle`$ the record part. For $`n_1\neq0`$, fixed $`\mathcal F_{\rm rec}`$ and with the motion factor present, $`(\alpha_0,\alpha_1,\beta_0,\beta_1,g_\zeta)\mapsto\boldsymbol g=(g_m,g_\eta,\mathcal F,\mathcal F_1,g_\zeta)`$ is an affine bijection onto $`\mathbb R^5`$: every $`\boldsymbol g`$ is an admissible member of $`\mathcal C^+`$. The *setting's listing* is: own term Model D, coupling $`G\otimes\Phi_x`$, record term $`\sum_x\lvert x\rangle\langle x\rvert\otimes K_x`$.

**Regime and orders.** First order in the gradients ($`\lVert\boldsymbol g\rVert\,\lvert x\rvert\ll1`$ on the region considered); branch starts at rest, drift velocity $`v`$. "Exactly" means with the full $`c_{2,k,\sigma}`$ of (4.17); "leading order in $`M_k/\tau`$" means dropping in $`c_{2,k,\sigma}`$ the terms of relative order $`M_k^2/\tau^2`$. Dimensions refer to $`\boldsymbol g\in\mathbb R^5`$ at fixed $`(\tau,m,N,\lambda_0,\mathcal F_{\rm rec})`$. Norm: Euclidean norm of the scaled vector $`\hat{\boldsymbol g}:=(g_m,g_\eta,\mathcal F/m,\mathcal F_1,g_\zeta)`$, whose components are all per label step.

**Inputs** (quoted in question.md):
- (4.16) of 04-branch-fall: $`a_{k,\sigma}(0)=\frac{\tau_k^2}{M_k}(\sigma\mathcal F_k-G_k)`$, level by level, for $`\mathcal C_{\rm lev}`$ with linear level profiles.
- (4.17) of 04-branch-fall: $`c_{2,k,\sigma}=g_\zeta+\frac{G_k}{M_k}\bigl(1+\frac{2M_k^2}{\tau^2}\bigr)-\sigma\frac{\mathcal F_k}{M_k}\bigl(\frac32+\frac{2M_k^2}{\tau^2}\bigr)`$; (4.20): the upper branch falls alike on all levels through $`v^2`$ iff $`\frac{\tau^2}{M_k}(\mathcal F_k-G_k)=a_0`$ for all $`k`$ and $`c_{2,k,+}=g_\zeta-\frac{\mathcal F_k}{2M_k}-\frac{a_0}{\tau^2}\bigl(1+\frac{2M_k^2}{\tau^2}\bigr)`$ is independent of $`k`$.
- (4.24) of 04-branch-fall, for $`\mathcal C`$ with $`a_{k,+}(0)=a\neq0`$: $`\frac{\mathrm d^2\bar x}{\mathrm d\lambda^2}\big\vert_{\rm drift}=d_0a_{k,+}(0)\hat e=-\frac{v_{\max}^2}{d_0}\frac{r(x+1)-r(x)}{r(x)}\hat e`$, $`v_{\max}=\tau d_0`$.
- (3.23) of 03-clock-and-fall: rate at $`x_0`$ $`:=\lim_{W\to\infty}r_W(x_0)=\frac{\eta_{x_0}}{\lambda_0}=\frac N{2\pi}\bigl(E^+_{x_0,k+1}-E^+_{x_0,k}\bigr)`$, $`E^\pm_{x,k}=V_{x,k}\pm M_{x,k}`$.
- (4.19), (4.22) of 04-branch-fall: used in the checks.

**Use of (4.24) in $`\mathcal C^+`$ (assumption).** Since $`v_{\max}=\tau d_0`$, (4.24) is equivalent to its label form $`a_{k,+}(0)=-\tau^2\frac{r(x+1)-r(x)}{r(x)}`$. Its first equality, which converts a common label acceleration into the drift of $`\bar x`$, is taken over to $`\mathcal C^+`$ unchanged. "(4.24) holds on level $`k`$" means that the label form holds on level $`k`$.

## Derivation

### Step 1. Fall from rest (item 1a, 1c)

By (4.16) and (17.1), with $`d_k=M_k-m`$: $`\sigma\mathcal F_k-G_k=\sigma\mathcal F-mg_m+d_k(\sigma\mathcal F_1-g_\eta)=m\ell_\sigma+M_k(\sigma\mathcal F_1-g_\eta)`$, hence
```math
a_{k,\sigma}(0)=\tau^2(\sigma\mathcal F_1-g_\eta)+\tau^2\,\frac{m}{M_k}\,\ell_\sigma,
\qquad
\ell_\sigma:=\sigma\frac{\mathcal F}{m}-g_m+g_\eta-\sigma\mathcal F_1 .
\qquad\text{(17.2)}
```
For $`N\ge2`$, $`k\mapsto m/M_k`$ is strictly decreasing, so $`a_{k,\sigma}(0)`$ is the same on all levels iff $`\ell_\sigma=0`$, with value $`a_\sigma=\tau^2(\sigma\mathcal F_1-g_\eta)`$. Since $`\ell_++\ell_-=2(g_\eta-g_m)`$, $`\ell_+-\ell_-=2(\mathcal F/m-\mathcal F_1)`$ and, on $`\mathcal U_4^{\pm}`$, $`a_+-a_-=2\tau^2\mathcal F_1`$:
```math
\begin{aligned}
\mathcal U_4^{+}&=\{\mathcal F=m(g_m-g_\eta+\mathcal F_1)\},\ \ a_+=\tau^2(\mathcal F_1-g_\eta);\qquad
\mathcal U_4^{-}=\{\mathcal F=m(\mathcal F_1+g_\eta-g_m)\},\ \ a_-=-\tau^2(\mathcal F_1+g_\eta);\\
\mathcal U_4^{\pm}&=\mathcal U_4^+\cap\mathcal U_4^-=\{g_m=g_\eta,\ \mathcal F=m\mathcal F_1\};\qquad
\mathcal U_4^{=}=\mathcal U_4^{\pm}\cap\{a_+=a_-\}=\{g_m=g_\eta,\ \mathcal F=\mathcal F_1=0\},\ \ a=-\tau^2g_\eta .
\end{aligned}
\qquad\text{(17.3)}
```
In $`\hat{\boldsymbol g}`$, $`\ell_\pm=\boldsymbol n_\pm\cdot\hat{\boldsymbol g}`$ with $`\boldsymbol n_\pm=(-1,1,\pm1,\mp1,0)`$, $`\lvert\boldsymbol n_\pm\rvert=2`$, $`\boldsymbol n_+\cdot\boldsymbol n_-=0`$, and $`\mathcal U_4^=`$ adds the independent equation $`\mathcal F_1=0`$. Dimensions $`4,4,3,2`$, codimensions $`1,1,2,3`$, the same for $`N=2`$ and $`N\ge3`$.

### Step 2. Through the order $`v^2`$ (item 1a, 1c)

*Upper branch.* On $`\mathcal U_4^+`$, $`\mathcal F_k=\Delta+M_k\mathcal F_1`$ with $`\Delta:=m(g_m-g_\eta)`$, so (4.20)(ii) reads
```math
c_{2,k,+}=g_\zeta-\frac{\mathcal F_1}2-\frac{a_+}{\tau^2}-h(M_k),\qquad h(u):=\frac{\Delta}{2u}+\frac{2a_+}{\tau^4}\,u^2 ,
\qquad\text{(17.4)}
```
and the condition is that $`h(M_k)`$ is independent of $`k`$.
1. *Exactly, $`N=2`$:* $`h(M_0)=h(M_1)`$ $`\iff`$ $`\frac{\Delta}{2}\frac{M_1-M_0}{M_0M_1}=\frac{2a_+}{\tau^4}(M_1-M_0)(M_1+M_0)`$ $`\iff`$ $`\Delta=\frac{4a_+}{\tau^4}M_0M_1(M_0+M_1)`$. This equation does not contain $`\mathcal F`$, while $`\ell_+`$ does, so the two are independent.
2. *Exactly, $`N\ge3`$:* $`h(M_k)=h_0`$ means that $`p(u)=\frac{2a_+}{\tau^4}u^3-h_0u+\frac\Delta2`$ vanishes at $`N\ge3`$ distinct positive points. If $`a_+\neq0`$, $`p`$ is a cubic without $`u^2`$ term, so its three roots sum to zero, impossible for three positive roots. Hence $`a_+=0`$, then $`p`$ is affine with three roots, so $`h_0=\Delta=0`$.
3. *Leading order in $`M_k/\tau`$:* the $`u^2`$ term of $`h`$ is of relative order $`M_k^2/\tau^2`$ and is dropped; $`\Delta/(2M_k)`$ is $`k`$-independent iff $`\Delta=0`$, for every $`N\ge2`$. On the resulting set the residual is $`c_{2,k,+}-c_{2,0,+}=-\frac{2a_+}{\tau^4}(M_k^2-m^2)`$.

*Lower branch.* In (4.16)–(4.17), $`\mathcal F_k`$ enters only as $`\sigma\mathcal F_k`$, so the lower-branch conditions are those of the upper branch under the reflection $`R:(\mathcal F,\mathcal F_1)\mapsto(-\mathcal F,-\mathcal F_1)`$, which maps $`a_+`$ to $`a_-`$. Hence:
```math
\begin{aligned}
&\mathcal U^+_{4,v}=\Bigl\{\ell_+=0,\ m(g_m-g_\eta)=\tfrac{4M_0M_1(M_0+M_1)}{\tau^2}(\mathcal F_1-g_\eta)\Bigr\}\ (N=2,\ \dim3);\qquad
\mathcal U^+_{4,v}=\{g_m=g_\eta=\mathcal F_1,\ \mathcal F=mg_\eta\}\ (N\ge3,\ \dim2,\ a_+=0);\\
&\text{leading order in }M_k/\tau,\ N\ge2:\ \ \mathcal U^+_{4,v,0}=\{g_m=g_\eta,\ \mathcal F=m\mathcal F_1\}=\mathcal U_4^{\pm}\ (\dim3);\qquad
\mathcal U^-_{4,v}=R\,\mathcal U^+_{4,v},\ \ \mathcal U^-_{4,v,0}=R\,\mathcal U^+_{4,v,0};\\
&\text{both branches: exactly }\mathcal U^+_{4,v}\cap\mathcal U^-_{4,v}=\{g_m=g_\eta=\mathcal F=\mathcal F_1=0\}\ (\dim1,\ a_\pm=0);\ \ \text{at leading order }\mathcal U_4^{\pm}\ (\dim3).
\end{aligned}
\qquad\text{(17.5)}
```
For both branches exactly with $`N=2`$: $`\ell_\pm=0`$ gives $`\Delta=0`$, $`\mathcal F=m\mathcal F_1`$, then item 1 gives $`a_+=a_-=0`$, so $`\mathcal F_1=g_\eta=0`$; for $`N\ge3`$ intersect the two sets of item 2. $`\mathcal U_4^\pm`$ is $`R`$-invariant.

### Step 3. Rate at a place (item 1b)

At zeroth order in the gradients, the contract at $`x_0`$ is frozen to the homogeneous one with on-site part $`\sigma_3\otimes(m_{x_0}\mathbb 1_N+\eta_{x_0}D)+\mathbb 1_2\otimes(V_{x_0}\mathbb 1_N-\mathcal F_1x_0D)`$, where $`m_{x_0}=m(1+g_mx_0)`$, $`\eta_{x_0}=1+g_\eta x_0`$, $`V_{x_0}=-\mathcal Fx_0`$, and hopping $`\tau\zeta_{x_0}`$. Write it as $`C^{\mathcal C}_{x_0}-\mathcal F_1x_0\,\mathbb 1\otimes\mathbb 1_2\otimes D`$, with $`C^{\mathcal C}_{x_0}`$ the frozen member of $`\mathcal C`$ with the same $`(g_m,g_\eta,\mathcal F,g_\zeta)`$. The added term is the identity on position and branch, and $`D`$ commutes with the clock factors of $`C^{\mathcal C}_{x_0}`$ ($`\mathbb 1_N`$ and $`m_{x_0}\mathbb 1_N+\eta_{x_0}D`$). So the two terms commute and $`e^{-iC_{x_0}\lambda}=e^{-iC^{\mathcal C}_{x_0}\lambda}e^{i\mathcal F_1x_0D\lambda}`$ exactly. By (3.23), for $`W\to\infty`$ the first factor acts on the clock of the upper-branch start as $`e^{-i\eta_{x_0}D\lambda}`$ up to a common phase: the level phases are $`E^+_{x_0,k}`$, affine in $`d_k`$ with slope $`\eta_{x_0}`$. The product acts as $`e^{-i(\eta_{x_0}-\mathcal F_1x_0)D\lambda}`$, which is the clock evolution of $`\mathcal C`$ with $`\eta_{x_0}\to\eta_{x_0}-\mathcal F_1x_0`$. By (3.23),
```math
r(x_0)=\frac{1+(g_\eta-\mathcal F_1)\,x_0}{\lambda_0}=\frac N{2\pi}\bigl(E^+_{x_0,k+1}-E^+_{x_0,k}\bigr),
\qquad E^+_{x,k}=m(1+g_mx)-\mathcal Fx+d_k\bigl(1+(g_\eta-\mathcal F_1)x\bigr),
\qquad\text{(17.6)}
```
the same for every $`k`$, because $`E^+_{x,k}`$ is affine in $`d_k`$.

### Step 4. Relation (4.24) and $`\mathcal U_5`$ (item 1b, 1c)

By (17.6), $`\frac{r(x+1)-r(x)}{r(x)}=\frac{g_\eta-\mathcal F_1}{1+(g_\eta-\mathcal F_1)x}=g_\eta-\mathcal F_1+O(\lVert\boldsymbol g\rVert^2)`$. With (17.2), the defect of the label form of (4.24) on level $`k`$ is
```math
\mathcal D_k:=a_{k,+}(0)+\tau^2\frac{r(x+1)-r(x)}{r(x)}=\tau^2\frac{m}{M_k}\,\ell_+ +O(\lVert\boldsymbol g\rVert^2),
\qquad
\mathcal U_5=\{\ell_+=0,\ \mathcal F_1\neq g_\eta\}=\mathcal U_4^+\setminus\{a_+=0\}.
\qquad\text{(17.7)}
```
Since $`m/M_k\neq0`$, (4.24) holds on one level iff it holds on every level, iff $`\ell_+=0`$. The common value is then $`a_+=\tau^2(\mathcal F_1-g_\eta)`$, nonzero iff $`\mathcal F_1\neq g_\eta`$. $`\{\ell_+=0,\mathcal F_1=g_\eta\}`$ has codimension 2, so $`\mathcal U_5`$ is an open dense part of the hyperplane $`\mathcal U_4^+`$: dimension 4, codimension 1, for every $`N\ge2`$.

### Step 5. Stability (item 2)

The distance of $`\hat{\boldsymbol g}`$ from $`\mathcal U_4^+`$ is $`\delta=\lvert\ell_+\rvert/2`$. By (17.2) and (17.7), $`a_{k,+}(0)`$ and $`\mathcal D_k`$ are monotone in $`k`$, with extreme levels $`k=0`$ ($`M_0=m`$) and $`k=N-1`$:
```math
\max_{k,k'}\bigl\lvert a_{k,+}(0)-a_{k',+}(0)\bigr\rvert=2\tau^2\delta\,\frac{d_{N-1}}{m+d_{N-1}},
\qquad
\max_k\lvert\mathcal D_k\rvert=\lvert\mathcal D_0\rvert=2\tau^2\delta .
\qquad\text{(17.8)}
```
For the distance $`\delta_\pm`$ from $`\mathcal U_4^\pm`$, the orthogonality of $`\boldsymbol n_\pm`$ gives $`\delta_\pm^2=(\ell_+^2+\ell_-^2)/4`$. On branch $`\sigma`$ the largest level difference is therefore at most $`2\tau^2\delta_\pm d_{N-1}/M_{N-1}`$, with equality when $`\ell_{-\sigma}=0`$. Both quantities are of first order in $`\delta`$, with the exact coefficients above at first order in the gradients.

### Step 6. Requirements (item 3)

**6.1 Relistings.** For any self-adjoint $`Q`$ on the body and any pair term $`C_\gamma`$ of the body,
```math
C_{\rm own}\to C_{\rm own}-Q,\qquad C_\gamma\to C_\gamma+Q\otimes\mathbb 1
\qquad\text{(17.9)}
```
leaves $`C`$ unchanged, so by A5 and M6 the two listings are the same description. Instances:
- (M1) $`Q=c\,\mathbb 1`$ into the record term: the zero of the body's own cost.
- (M2) $`Q=\epsilon\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes\mathbb 1_N`$, $`0<\lvert\epsilon\rvert<m`$, into the record pair term: the own term stays of Model D form, with $`m\to m-\epsilon`$.
- (M3) $`Q=-c\sum_x\lvert x\rangle\langle x\rvert\otimes G`$ into the field pair term: the coupling stays $`G\otimes(\Phi_x-c)`$ and the own on-site term becomes $`\sigma_3\otimes(m+D)+cG`$.

The effective level blocks in $`\varphi`$ and in the medium background are computed from the total $`C`$. Hence $`M_{x,k}`$, $`\zeta_{x,k}`$, and $`V_{x,k}`$ up to one common constant are invariant under (17.9) and under the common phase. So are $`\boldsymbol g`$, $`M_k`$, (17.2), (17.6) and the sets (17.3), (17.5), (17.7).

**6.2 R1.** In the setting's listing, with (17.1) and $`n_1\neq0`$,
```math
\text{R1}\iff\text{R2}\iff G=\alpha\,\sigma_3\otimes(m\mathbb 1_N+D)\iff g_m=g_\eta,\ \ \mathcal F_1=0,\ \ \mathcal F=\mathcal F_{\rm rec};\qquad\text{then }\ \ell_\pm=\pm\mathcal F_{\rm rec}/m .
\qquad\text{(17.10)}
```
1. *Well defined?* No. After (M2), the own on-site term is $`\sigma_3\otimes((m-\epsilon)\mathbb 1_N+D)`$. Then $`G=\alpha\sigma_3\otimes(m+D)`$ with $`\alpha\neq0`$ fails R1 (its $`\mathbb 1_N`$ and $`D`$ coefficients have ratio $`m\neq m-\epsilon`$), while $`G'=\alpha\sigma_3\otimes((m-\epsilon)\mathbb 1_N+D)`$ satisfies it. For one and the same $`C`$, the verdict of R1 depends on the listing. (M1) changes it as well.
2. *Relation (setting's listing).* If $`\mathcal F_{\rm rec}=0`$, R1 is equivalent to $`\mathcal U_4^=`$ by (17.3). It is therefore sufficient for $`\mathcal U_4^\pm`$, and for $`\mathcal U_5`$ when $`\alpha\neq0`$ ($`a=-\tau^2n_1\alpha`$). It is not necessary for either: take $`G=(\alpha\sigma_3+\beta\mathbb 1_2)\otimes(m\mathbb 1_N+D)`$ with $`\beta\neq0`$; by (17.1), $`g_m=g_\eta=n_1\alpha`$ and $`\mathcal F=m\mathcal F_1=-mn_1\beta`$, so $`G\in\mathcal U_4^\pm`$, and $`G\in\mathcal U_5`$ if $`\beta\neq-\alpha`$, yet $`G`$ fails R1. If $`\mathcal F_{\rm rec}\neq0`$, then $`\ell_\pm\neq0`$, so R1 excludes $`\mathcal U_4^\pm`$ and $`\mathcal U_5`$. So R1 is not necessary for $`\mathcal U_4^\pm`$ or $`\mathcal U_5`$ for any $`\mathcal F_{\rm rec}`$. It is sufficient for $`\mathcal U_4^\pm`$ iff $`\mathcal F_{\rm rec}=0`$, and for $`\mathcal U_5`$ iff in addition $`\alpha\neq0`$.
3. *Controls.* (a) Setting's listing with $`\mathcal F_{\rm rec}\neq0`$: every R1 coupling fails item 4 on both branches. (b) $`\mathcal F_{\rm rec}=0`$: $`G'`$ of item 1 satisfies R1 in the listing (M2), and by (17.1) $`\ell_\pm=n_1\alpha\epsilon/m\neq0`$, so item 4 fails on both branches.

**6.3 R2.** We read R2 as follows: on level $`k`$ the coupling block is $`\Phi_x`$ times $`\alpha`$ times the traceless part, on the branch label, of the own on-site block, with $`\alpha`$ level-independent, and $`G`$ has no $`\mathbb 1_2`$-part. In the setting's listing the own block $`M_k\sigma_3`$ is traceless and $`G`$ has the level block $`(\alpha_0+\alpha_1d_k)\sigma_3+(\beta_0+\beta_1d_k)\mathbb 1_2`$. With two distinct $`d_k`$, R2 $`\iff`$ $`\beta_0=\beta_1=0`$, $`\alpha_0=\alpha m`$, $`\alpha_1=\alpha`$, which is the set (17.10).
1. *Well defined?* No. R2 is invariant under (M1) and under every relisting with $`Q=\mathbb 1_2\otimes Q'`$, $`Q'`$ diagonal in position and level, because the traceless part does not see them. It is also invariant under (M3) when $`1+c\alpha\neq0`$: the traceless own block becomes $`(1+c\alpha)M_k\sigma_3`$ and R2 holds with $`\alpha/(1+c\alpha)`$. Under (M2) the traceless own block becomes $`(M_k-\epsilon)\sigma_3`$, and $`M_k/(M_k-\epsilon)`$ depends on $`k`$, so $`G`$ and $`G'`$ of 6.2 exchange their verdicts. R2 thus removes the dependence on the zero of the cost, but not the dependence on the listing.
2. *Relation and controls:* as for R1 (same set in the setting's listing; the same controls (a), (b), with (M2) applied to the traceless block).

**6.4 R3.** Let $`B_{x,k}:=M_{x,k}\sigma_3+V_{x,k}\mathbb 1_2`$ be the effective on-site block of level $`k`$ (in $`\varphi`$ and the medium background), and $`M_k=\frac12(E^+_{0,k}-E^-_{0,k})`$ its half-gap between branches. The requirements are:
- (R3) there is a level-independent operator $`\Gamma`$ on the branch label with $`B_{x+1,k}-B_{x,k}=M_k\Gamma`$ for every $`k`$;
- (R3$`^+`$) $`E^+_{x+1,k}-E^+_{x,k}=\gamma_+M_k`$ for every $`k`$, with one real $`\gamma_+`$.

Both are taken at first order in the gradients.
1. *Well defined?* Yes. Only differences of effective costs at neighbouring places (where the common constant cancels) and branch gaps enter, and both are computed from the total $`C`$. So R3 and R3$`^+`$ are invariant under (17.9) and under the common phase.
2. *Relation.* In $`\mathcal C^+`$, $`B_{x+1,k}-B_{x,k}=G_k\sigma_3-\mathcal F_k\mathbb 1_2`$, so $`\Gamma=\gamma\sigma_3-\phi\mathbb 1_2`$. With two distinct $`M_k`$:
```math
\text{R3}\iff G_k=\gamma M_k,\ \mathcal F_k=\phi M_k\ \forall k\iff g_m=g_\eta=\gamma,\ \mathcal F_1=\phi,\ \mathcal F=m\phi\iff\boldsymbol g\in\mathcal U_4^{\pm};\qquad
\text{R3}^+\iff\ell_+=0\iff\boldsymbol g\in\mathcal U_4^{+},
\qquad\text{(17.11)}
```
where R3$`^+`$ uses $`\mathcal F_k-G_k=m\ell_++M_k(\mathcal F_1-g_\eta)`$ from Step 1. Hence: $`\Gamma`$ traceless ($`\phi=0`$) $`\iff\mathcal U_4^=`$; R3$`^+`$ with $`\gamma_+=g_\eta-\mathcal F_1\neq0`$ $`\iff\mathcal U_5`$; and $`a_+=-\tau^2\gamma_+`$. R3 is necessary and sufficient for $`\mathcal U_4^\pm`$, so by (17.2) no member of $`\mathcal C^+`$ satisfies R3 and fails item 4 from rest. Through $`v^2`$ exactly it is not sufficient. Control: R3 with $`\phi\neq\gamma`$, i.e. $`a_+\neq0`$, has $`\Delta=0`$ and so fails (17.5) for $`N=2`$ and for $`N\ge3`$.
3. In the setting's listing, $`B_{x+1,k}-B_{x,k}=n_1G^{(k)}-\mathcal F_{\rm rec}\mathbb 1_2`$, with $`G^{(k)}`$ the level block of $`G`$. R3 therefore reads $`n_1G^{(k)}=M_k\Gamma+\mathcal F_{\rm rec}\mathbb 1_2`$ for all $`k`$: it ties the coupling to the body's half-gaps and to the record force.

### Step 7. Verdict (item 4)

At first order in the gradients, every set of (17.3), (17.5) and (17.7) has as closure a proper linear subspace of $`\mathbb R^5`$:
```math
\mathrm{int}\,\mathcal U=\emptyset\quad\text{and}\quad\mathbb R^5\setminus\overline{\mathcal U}\ \text{is open and dense, for every set }\mathcal U\text{ of (17.3), (17.5), (17.7)} .
\qquad\text{(17.12)}
```
The couplings that give items 4 and 5 are therefore exceptional (codimension 1 to 4), not typical. By (17.8) they are broken linearly in the distance. They are selected by the well-defined requirement R3 (R3$`^+`$ for $`\mathcal U_4^+`$ and $`\mathcal U_5`$), not by R1 or R2, which are not well defined. By (17.1) every $`\boldsymbol g\in\mathbb R^5`$ is an admissible description, so within $`\mathcal C^+`$ the language does not enforce R3. This follows from admissibility (A10, M8), not from items 1–3 (M10).

## Result

Class throughout: $`\mathcal C^+`$ as in the Setup (one Model D body, the only one of its type; sharp field with linear profile, $`n_1\neq0`$; weak records), $`N\ge2`$, first order in the gradients, branch starts at rest, unless stated.

- **(17.1)** (definition) Parametrization of $`\mathcal C^+`$ by $`\boldsymbol g`$, with $`\mathcal F=\mathcal F_{\rm rec}-n_1\beta_0`$ and $`\mathcal F_1=-n_1\beta_1`$. It is onto $`\mathbb R^5`$ at fixed $`\mathcal F_{\rm rec}`$.
- **(17.2)** (formula) $`a_{k,\sigma}(0)=\tau^2(\sigma\mathcal F_1-g_\eta)+\tau^2\frac m{M_k}\ell_\sigma`$.
- **(17.3)** (criterion) For $`N=2`$ and $`N\ge3`$ alike:
  - the fall from rest is level-independent on branch $`\sigma`$ iff $`\ell_\sigma=0`$;
  - on both branches iff $`g_m=g_\eta`$ and $`\mathcal F=m\mathcal F_1`$;
  - on both branches with $`a_+=a_-`$ iff in addition $`\mathcal F_1=0`$.

  Codimensions $`1,1,2,3`$.
- **(17.4)–(17.5)** (criterion) Upper branch through $`v^2`$, exactly:
  - $`N=2`$: $`\ell_+=0`$ and $`m(g_m-g_\eta)=\frac{4M_0M_1(M_0+M_1)}{\tau^2}(\mathcal F_1-g_\eta)`$, codimension 2;
  - $`N\ge3`$: $`g_m=g_\eta=\mathcal F_1`$ and $`\mathcal F=mg_\eta`$, codimension 3, with $`a_+=0`$.

  At leading order in $`M_k/\tau`$ (residual of relative order $`M_k^2/\tau^2`$) the set is $`\mathcal U_4^\pm`$, codimension 2, for every $`N\ge2`$. The lower branch gives the images under $`(\mathcal F,\mathcal F_1)\mapsto(-\mathcal F,-\mathcal F_1)`$. Both branches: exactly, only $`g_\zeta`$ may be nonzero (codimension 4, zero fall), for $`N=2`$ and $`N\ge3`$; at leading order, $`\mathcal U_4^\pm`$.
- **(17.6)** (formula) Wide-start rate at $`x_0`$, at zeroth order in the gradients: $`r(x_0)=[1+(g_\eta-\mathcal F_1)x_0]/\lambda_0=\frac N{2\pi}(E^+_{x_0,k+1}-E^+_{x_0,k})`$ for every $`k`$.
- **(17.7)** (criterion) The defect of (4.24) on level $`k`$ is $`\mathcal D_k=\tau^2\frac m{M_k}\ell_+`$ up to $`O(\lVert\boldsymbol g\rVert^2)`$. (4.24) holds on one level iff it holds on all levels, iff $`\ell_+=0`$. $`\mathcal U_5=\mathcal U_4^+\setminus\{\mathcal F_1=g_\eta\}`$ has dimension 4 and codimension 1, for $`N=2`$ and $`N\ge3`$. This uses the first equality of (4.24) carried over to $`\mathcal C^+`$.
- **(17.8)** (formula) At distance $`\delta`$ from $`\mathcal U_4^+`$ in the norm of $`\hat{\boldsymbol g}`$: the largest level difference of $`a_{k,+}(0)`$ is $`2\tau^2\delta\,d_{N-1}/(m+d_{N-1})`$, and the largest defect of (4.24) is $`2\tau^2\delta`$. Both are of order $`\delta^1`$. At distance $`\delta_\pm`$ from $`\mathcal U_4^\pm`$, the largest level difference on each branch is at most $`2\tau^2\delta_\pm d_{N-1}/M_{N-1}`$.
- **(17.9)** (definition) Relistings (M1)–(M3). The effective level blocks, up to one common constant, are invariant, and so are $`\boldsymbol g`$ and all sets above.
- **(17.10)** (negative) R1 and R2 are not well defined: (M2) changes their verdict for a fixed $`C`$, and (M1) does so for R1. In the setting's listing they define the same set, $`g_m=g_\eta`$, $`\mathcal F_1=0`$, $`\mathcal F=\mathcal F_{\rm rec}`$. This set equals $`\mathcal U_4^=`$ if $`\mathcal F_{\rm rec}=0`$ and is disjoint from $`\mathcal U_4^\pm`$ and $`\mathcal U_5`$ if $`\mathcal F_{\rm rec}\neq0`$. R1 and R2 are not necessary for $`\mathcal U_4^\pm`$ or $`\mathcal U_5`$. They are sufficient for $`\mathcal U_4^\pm`$ iff $`\mathcal F_{\rm rec}=0`$, and for $`\mathcal U_5`$ iff in addition $`\alpha\neq0`$. Controls that satisfy them and fail item 4 on both branches: any R1 coupling with $`\mathcal F_{\rm rec}\neq0`$; or, for $`\mathcal F_{\rm rec}=0`$, $`G'=\alpha\sigma_3\otimes((m-\epsilon)\mathbb 1_N+D)`$ with $`\alpha\neq0`$ in the listing (M2).
- **(17.11)** (theorem) R3 (block gradient $`=M_k\Gamma`$ with a level-independent $`\Gamma`$) is well defined and is equivalent to $`\mathcal U_4^\pm`$. With $`\Gamma`$ traceless it is equivalent to $`\mathcal U_4^=`$. R3$`^+`$ is equivalent to $`\mathcal U_4^+`$, and R3$`^+`$ with $`\gamma_+\neq0`$ to $`\mathcal U_5`$. There is no control in $`\mathcal C^+`$ from rest. Through $`v^2`$ exactly, R3 with $`a_+\neq0`$ fails.
- **(17.12)** (theorem) Verdict: the sets are exceptional, with empty interior and positive codimension; they are broken at first order in $`\delta`$; they are selected by R3; and within $`\mathcal C^+`$ they are not enforced by the language, since every $`\boldsymbol g`$ is admissible.

## Consistency checks

1. **Dimensions.** Costs $`\tau,m,d_k,\mathcal F`$ are per unit of $`\lambda`$, and $`g_m,g_\eta,g_\zeta,\mathcal F_1`$ are per label step. Then $`a_{k,\sigma}(0)`$ and $`\tau^2(\mathcal F_1-g_\eta)`$ have dimension $`[\lambda]^{-2}`$; $`\ell_\sigma`$, $`h(u)`$ and $`\delta`$ are dimensionless; $`r`$ is per unit of $`\lambda`$; (17.8) has dimension $`[\lambda]^{-2}`$. Passed.
2. **Subclass $`\mathcal C`$ ($`\mathcal F_1=0`$).** (17.3) gives $`\mathcal F=\pm m(g_m-g_\eta)`$ with value $`-\tau^2g_\eta`$, which is (4.22). $`\mathcal U_4^=`$ gives $`\mathcal F_k=0`$ and $`\tau^2G_k/M_k=\tau^2g_\eta=-a`$, which is (4.19). (17.6) reduces to $`\eta_{x_0}/\lambda_0`$, which is (3.23). (17.7) gives (4.24) on $`\mathcal U_4^+`$ with $`a\neq0`$. Passed.
3. **Model D without field and records ($`\boldsymbol g=0`$).** $`a_{k,\sigma}(0)=0`$; $`\boldsymbol g=0`$ lies in every set of (17.3) and (17.5); $`c_{2,k,+}=0`$ by (17.4); $`r=1/\lambda_0`$. Passed.

## Open issues

- The first equality of (4.24), which converts the label acceleration into the drift of $`\bar x`$, is carried over to $`\mathcal C^+`$ without re-derivation.
- (17.6) is the $`W\to\infty`$ form only. The finite-$`W`$ rate and its bound in (3.23) are not re-derived for $`\mathcal F_1\neq0`$.
- The lower branch through $`v^2`$ uses (4.17) at $`\sigma=-1`$ level by level, in the form analogous to (4.20), which is quoted for the upper branch only.
- $`\mathcal F_{\rm rec}=-\kappa\langle X\rangle`$ depends on the medium background. Whether the background of 03-ilang-space fixes $`\langle X\rangle=0`$ is not quoted.
- R3 is equivalent to the property it selects. Whether a requirement outside $`\mathcal C^+`$ selects it (couplings that mix branches or levels, non-linear profiles, fields that are not sharp, several bodies) is out of scope.

## Methods used

- affine parametrization of a coupling class
- partial fractions in the level label and injectivity of Möbius maps
- root counting for a depressed cubic
- commuting factorization of the evolution
- relisting argument for M6 invariance, with explicit controls
- distance to hyperplanes, linear stability
