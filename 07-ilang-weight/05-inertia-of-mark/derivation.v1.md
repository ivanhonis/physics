# Inertia of a body with its own mark against its cost

- **Subproject:** 07-ilang-weight
- **Package:** 05-inertia-of-mark
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-21

## Setup and assumptions

**Description (assumption, M8).** The ring of $`L\ge5`$ places carries $`N_f\ge1`$ identical field objects ($`c=+1`$) with own term $`C_1`$. $`\Phi_x`$ is their number at $`x`$, and $`n=N_f/L`$. One Model D body sits on the same ring, at clock level $`k`$ with half-gap $`M_k=m+2\pi k/(N\lambda_0)`$. It is coupled by (a), (c) or the full grip (FG), with real $`\gamma\neq0`$; records at $`\kappa\to0`$. As in 03-weight-of-mark, $`\theta=1`$ for (a) and (c), and $`\theta=0`$ for FG. The total contracts of FG and (a) differ by the rest and clock term $`B`$, so they are different descriptions, not M6 replacements.

**Notation.**
- $`g:=\gamma M_k`$, $`g_\sigma:=\sigma g`$ (the $`g_b`$ of (3.4)), and $`\varkappa_k:=|g|L/t_f`$.
- $`\varepsilon_q=2t_f(1-\cos q)`$ for $`q\in Q:=\frac{2\pi}L\{1,\dots,L-1\}`$, $`\varepsilon_1:=\varepsilon_{2\pi/L}`$, and $`\langle f\rangle_q:=\frac1L\sum_{q\in Q}f(q)`$.
- $`s_1:=\langle\varepsilon_q^{-1}\rangle_q=\ell_0/t_f`$ with $`\ell_0=\Lambda^+(0)=(L^2-1)/(12L)`$, $`s_2:=\langle\varepsilon_q^{-2}\rangle_q`$, and $`S_2:=\langle(1+\cos q)\varepsilon_q^{-2}\rangle_q=2s_2-s_1/(2t_f)`$.
- For one field object at place $`r`$ relative to the body: $`h(g):=C_1+gP_0`$, with lowest eigenvalue $`\varepsilon_0(g)`$ and positive ground vector $`\varphi_g`$ (Perron–Frobenius). $`\Omega_\sigma:=\varphi_{g_\sigma}^{\otimes N_f}`$.
- Inertia $`\mu_{k,\sigma}:=1/E''_{k,\sigma}(0)`$. Held cost (3.4): $`\mathrm{Cost}_{k,\sigma}=\theta\sigma M_k+N_f[\varepsilon_0(g_\sigma)-\varepsilon_0(0)]`$.

**Assumptions.**
- **A1 (M9, field state).** At $`\tau=0`$ the field is in $`\Omega_\sigma`$, the lowest state of the branch-$`\sigma`$ block (the lowest state adapted to the body). The dressed level is its continuation in $`\tau`$ and $`P`$.
- **A2 (A13, regime).**
  - The curvature is computed at order $`\tau^2`$, under the isolation condition (5.4) for FG and (6.4) at $`\tau=0`$ for (a) and (c).
  - FG is expanded in the weak-mark regime **R1**: $`N_f\varkappa_k\ll1`$.
  - (a) and (c) are expanded in $`\gamma`$ at fixed $`L,N_f`$, at leading order in $`\tau`$.
- **A3 (standard mathematics).** Rayleigh–Schrödinger (RS) perturbation theory for a nondegenerate isolated eigenvalue: for $`\lVert V\rVert<d/2`$, with $`d`$ the distance to the rest of the unperturbed spectrum, the eigenvalue continues analytically (Kato). Fourier sums on the ring, for example $`\sum_{j=1}^{L-1}\sin^{-2}(\pi j/L)=(L^2-1)/3`$, and Perron–Frobenius.

**Inputs used:** (6.1), (6.4), (6.10), (6.12) of 06-ilang-source/06-own-mark; (2.14) of 02-two-free-bodies; (3.4), (3.12), (3.13) of 03-weight-of-mark; (7.7) of 06-ilang-source/07-dressed-fall. (6.5) of 06-ilang-source/06-own-mark is quoted but not needed, because (5.2) is exact in $`\gamma`$.

## Derivation

### Step 1. Sector contract; the full grip

Place the body at $`x`$ and the field objects at $`x+r_i`$. The vectors $`L^{-1/2}\sum_xe^{iPx}\lvert x,s\rangle\lvert\{x+r_i\}\rangle`$ span the sector of total label $`P`$, since the total contract commutes with the joint translation. In these coordinates the field hopping acts on the $`r_i`$ unchanged, and the pair term becomes $`g_\sigma\Phi_0`$ on branch $`\sigma`$ ($`\Phi_r`$ counts the objects at relative place $`r`$). The hop $`\lvert x+1\rangle\langle x\rvert`$ maps the sector vector with $`\{r_i\}`$ to $`e^{-iP}`$ times the one with $`\{r_i-1\}`$, and the bond factor $`\frac12(\Phi_x+\Phi_{x+1})`$ of (c) acts before the hop, at relative places $`0`$ and $`1`$.

On level $`k`$ (the clock label commutes with the total contract), (6.1) holds with

```math
\hat C^{(0)}=\sum_{\sigma=\pm}\lvert\sigma\rangle\langle\sigma\rvert\otimes\hat C^{(0)}_\sigma,\quad \hat C^{(0)}_\sigma=\theta\sigma M_k+C_1+g_\sigma\Phi_0,\qquad \hat C^{(+)}=\frac\tau2(-i\sigma_1)\otimes K,\quad K=\begin{cases}T_-&\text{(a), FG}\\ T_-\bigl(1+\frac\gamma2(\Phi_0+\Phi_1)\bigr)&\text{(c)}\end{cases}
\qquad\text{(5.1)}
```

with $`T_\pm`$ shifting all relative places by $`\pm1`$. For FG, (6.1) applies unchanged: only $`\hat C^{(0)}`$ changes ($`\theta=0`$).

The reflection $`\mathcal R:r\to-r`$ leaves $`\hat C^{(0)}_\sigma`$ and $`\Omega_\sigma`$ invariant and maps $`K`$ to $`K^\dagger`$ (since $`T_+^\dagger\Phi_rT_+=\Phi_{r-1}`$). All these operators are real in the place basis.

### Step 2. Curvature at order $`\tau^2`$ and the branch splitting

$`V(P):=e^{-iP}\hat C^{(+)}+e^{iP}\hat C^{(+)\dagger}`$ flips the branch and has $`\lVert V\rVert\le\tau\lVert K\rVert`$. At $`\tau=0`$ the level is $`E^0_\sigma=\theta\sigma M_k+N_f\varepsilon_0(g_\sigma)`$, with vector $`\lvert\sigma\rangle\otimes\Omega_\sigma`$ (A1); $`d_{k,\sigma}`$ is its distance to the rest of the spectrum of $`\hat C^{(0)}`$.

The first RS order vanishes. The second uses $`R:=(E^0_\sigma-\hat C^{(0)}_{-\sigma})^{-1}`$, $`(-i)^2=i^2=-1`$ and expectation values in $`\Omega_\sigma`$:

```math
E_{k,\sigma}(P)=E^0_\sigma+\frac{\tau^2}4\bigl[\langle KRK^\dagger\rangle+\langle K^\dagger RK\rangle-2J\cos2P\bigr]+O\Bigl(\frac{\tau^4\lVert K\rVert^4}{d^3_{k,\sigma}}\Bigr).
```

Here $`J:=\langle KRK\rangle=\langle K^\dagger RK^\dagger\rangle`$ is real, by $`\mathcal R`$ and reality. Hence, exactly in $`\gamma`$:

```math
E''_{k,\sigma}(0)=2\tau^2J_{k,\sigma}+O\Bigl(\frac{\tau^4\lVert K\rVert^4}{d^3_{k,\sigma}}\Bigr),\qquad J_{k,\sigma}=\langle\Omega_\sigma\vert K\,(E^0_\sigma-\hat C^{(0)}_{-\sigma})^{-1}K\vert\Omega_\sigma\rangle .\qquad\text{(5.2)}
```

The lowest eigenvector of $`\hat C^{(0)}_{-\sigma}`$ is $`\Omega_{-\sigma}`$, and $`E^0_\sigma-E^0_{-\sigma}=\mathrm{Cost}_{k,\sigma}-\mathrm{Cost}_{k,-\sigma}`$ exactly. Define:
- $`R_k:=\frac12(\mathrm{Cost}_{k,+}-\mathrm{Cost}_{k,-})`$ and $`C^{\rm ev}_k:=\frac12(\mathrm{Cost}_{k,+}+\mathrm{Cost}_{k,-})`$;
- $`a_{k,\sigma}:=\langle\Omega_{-\sigma}\vert K\vert\Omega_\sigma\rangle`$, equal to $`\langle\Omega_{-\sigma}\vert K^\dagger\vert\Omega_\sigma\rangle`$ by $`\mathcal R`$.

Separating the term of $`\Omega_{-\sigma}`$ in the spectral sum of $`R`$ gives

```math
\mathrm{Cost}_{k,\sigma}=\sigma R_k+C^{\rm ev}_k,\qquad J_{k,\sigma}=\frac{a_{k,\sigma}^2}{2\sigma R_k}+J^{\rm exc}_{k,\sigma},\qquad \mu_{k,\sigma}=\frac{\sigma R_k}{\tau^2\bigl(a^2_{k,\sigma}+2\sigma R_kJ^{\rm exc}_{k,\sigma}\bigr)}\quad\text{at order }\tau^{-2},\qquad\text{(5.3)}
```

where $`J^{\rm exc}`$ is the sum over the excited eigenvectors of $`\hat C^{(0)}_{-\sigma}`$. The inertia is set by the branch-odd part $`R_k`$ of the cost. The even part $`C^{\rm ev}_k`$ enters only through $`a`$ and $`J^{\rm exc}`$.

**M6.** $`\mu_{k,\sigma}`$, $`R_k`$ and the level differences of $`C^{\rm ev}_k`$ are curvatures and eigenvalue differences of one total contract. $`C^{\rm ev}_k`$ itself is fixed only up to the level-independent reference, the description without the body.

**Dressed level at $`P=0`$.** $`E_{k,\sigma}(0)-E^0_\sigma=\frac{\tau^2}4\langle w\vert R\vert w\rangle`$ with $`w=(K^\dagger-K)\Omega_\sigma`$, and $`w\perp\Omega_{-\sigma}`$ by $`\mathcal R`$. So it is $`O(\tau^2)`$, without the factor $`1/R_k`$.

### Step 3. Isolation for the full grip (item 1)

At $`\tau=0`$, $`\hat C^{(0)}_\sigma=C_1+g_\sigma\Phi_0`$ acts on $`N_f`$ non-interacting bosons, and its eigenvalues are sums of eigenvalues of $`h(g_\sigma)`$. Call $`\sigma_l:=-\mathrm{sign}\gamma`$ the lower branch ($`g_{\sigma_l}=-|g|`$) and $`\sigma_u:=-\sigma_l`$ the upper one.
- **Splitting.** $`\hat C^{(0)}_{\sigma_u}-\hat C^{(0)}_{\sigma_l}=2|g|\Phi_0\ge0`$, and $`\Omega_{\sigma_u}`$ has positive density at $`r=0`$. Hence $`\Delta_b:=E^0_{\sigma_u}-E^0_{\sigma_l}=2|R_k|>0`$.
- **Lower level.** By Perron–Frobenius, $`E^0_{\sigma_l}`$ is the nondegenerate lowest eigenvalue of $`\hat C^{(0)}`$.
- **Distances.** With $`\varepsilon^\pm_1`$ the first excitation energy of $`h(\pm|g|)`$: $`d_{k,\sigma_l}=\min(\Delta_b,\varepsilon^-_1)`$, and, if $`\Delta_b<\varepsilon^-_1`$, $`d_{k,\sigma_u}=\min(\Delta_b,\varepsilon^-_1-\Delta_b,\varepsilon^+_1)`$.

For FG $`\lVert K\rVert=1`$, so by Kato (5.2) holds for $`\tau<d/2`$. In R1, $`\Delta_b=2n|g|(1+O(\varkappa_k^2))`$ by (5.5), and $`\varepsilon^\pm_1=\varepsilon_1(1+O(\varkappa_k))`$. The condition reads

```math
\tau<\tfrac12d_{k,\sigma},\qquad d_{k,\sigma}\simeq\begin{cases}\min\bigl(2n|\gamma|M_k,\ \varepsilon_1\bigr),&\sigma\gamma<0,\\ \min\bigl(2n|\gamma|M_k,\ \varepsilon_1-2n|\gamma|M_k\bigr),&\sigma\gamma>0,\ 2n|\gamma|M_k<\varepsilon_1,\end{cases}\qquad \varepsilon_1=2t_f\Bigl(1-\cos\frac{2\pi}L\Bigr).\qquad\text{(5.4)}
```

Where it fails:
1. **$`\gamma\to0`$, both branches.** $`d\to0`$: without coupling the FG body is gapless, with band $`\pm\tau\lvert\sin P\rvert`$.
2. **Upper branch, $`N_f\ge2`$.** As $`2n|\gamma|M_k`$ approaches $`\varepsilon_1`$, the upper level crosses the lowest excited level of the other branch (the branches do not mix at $`\tau=0`$). Beyond that it crosses multi-object excitations at isolated values of $`\gamma`$.
3. **$`N_f=1`$: no crossing.** The even eigenvalues of $`h(\pm|g|)`$ solve $`\pm1/|g|=\langle0\vert(E-C_1)^{-1}\vert0\rangle`$, which decreases between consecutive poles; the odd ones are $`\ge-2t_f\cos(2\pi/L)`$. Hence $`\varepsilon_0(|g|)`$ lies strictly between the two lowest eigenvalues of $`h(-|g|)`$. The upper branch is isolated for every $`\gamma\neq0`$, with $`d_{k,\sigma_u}\to0`$ as $`\varkappa_k\to\infty`$.
4. **$`L\to\infty`$ at fixed $`n,\gamma`$.** $`\varepsilon_1\to0`$ and the upper branch fails. The lower branch stays isolated, with $`d_{k,\sigma_l}\to\sqrt{4t_f^2+\gamma^2M_k^2}-2t_f`$ (the binding gap of the infinite chain; $`\Delta_b\propto N_f\to\infty`$).

### Step 4. Weak-mark expansion

RS for $`h(g)=h(0)+gP_0`$ in plane waves $`\lvert q\rangle`$, with $`\langle q\vert P_0\vert q'\rangle=1/L`$ and $`u:=\lvert q{=}0\rangle`$, gives

```math
\begin{aligned}
&\varphi_g=u+g\varphi^{(1)}+O(g^2),\quad \langle q\vert\varphi^{(1)}\rangle=-\frac1{L\varepsilon_q},\qquad \varepsilon_0(g)=-2t_f+\frac gL-\frac{g^2s_1}L+\frac{g^3}L\Bigl(s_1^2-\frac{s_2}L\Bigr)+O(g^4),\\
&R_k=\theta M_k+n\gamma M_k\bigl[1+\gamma^2M_k^2(s_1^2-s_2/L)\bigr]+O(\gamma^5),\qquad C^{\rm ev}_k=-n\gamma^2M_k^2\,\ell_0/t_f+O(\gamma^4),\\
&a^2_{k,\sigma}=(1+\theta_c\gamma n)^2-2ng^2S_2+O(\gamma^3),\qquad J^{\rm exc}_{k,\sigma}=2n\Bigl\langle\frac{\cos q\,(1+\cos q)\,u_q^2}{2\sigma R_k-\varepsilon_q}\Bigr\rangle_q+O(\gamma^3),
\end{aligned}\qquad\text{(5.5)}
```

with $`\theta_c=1`$ for (c) and $`0`$ otherwise. The vertex is $`u_q=-g_\sigma/\varepsilon_q`$ for (a) and FG, and $`u_q=\gamma/2-g_\sigma/\varepsilon_q`$ for (c). Reasons:
- **$`\varepsilon_0(g)`$.** In the third RS order all matrix elements equal $`g/L`$, so $`E^{(3)}=(g/L)^3[(\sum_q\varepsilon_q^{-1})^2-\sum_q\varepsilon_q^{-2}]`$. $`R_k`$ and $`C^{\rm ev}_k`$ are the odd and even parts in $`g`$ of (3.4).
- **$`a`$ for (a) and FG.** $`a=\alpha^{N_f}`$ with
```math
\alpha:=\langle\varphi_{-g_\sigma}\vert T_-\varphi_{g_\sigma}\rangle=1-g^2\bigl(\lVert\varphi^{(1)}\rVert^2+\langle\varphi^{(1)}\vert T_+\varphi^{(1)}\rangle\bigr)+O(g^4)=1-g^2S_2/L+O(g^4).
```
  $`\alpha`$ is even in $`g`$ by $`\mathcal R`$. The $`O(g)`$ terms vanish because $`T_\pm u=u`$ and $`\varphi^{(1)}\perp u`$.
- **$`a`$ for (c).** It gains $`\frac\gamma2N_f\alpha^{N_f-1}\bigl[\varphi_{-g_\sigma}(-1)\varphi_{g_\sigma}(0)+\varphi_{-g_\sigma}(0)\varphi_{g_\sigma}(1)\bigr]=\gamma n+O(\gamma^3)`$. The $`O(g)`$ parts cancel because $`\varphi^{(1)}`$ is even in $`r`$.
- **$`J^{\rm exc}`$.** The component of $`K\Omega_\sigma`$ with one object excited is $`N_f^{1/2}`$ times a one-object vector $`\eta`$, with $`\langle q\vert\eta\rangle=L^{-1}(1+e^{iq})u_q+O(\gamma^2)`$. Its sources:
  - $`T_-\varphi_{g_\sigma}-\alpha\varphi_{-g_\sigma}=g_\sigma(1+T_-)\varphi^{(1)}`$;
  - for (c), also $`\frac\gamma2T_-(P_0+P_1)u`$, with $`\langle q\vert T_-(P_0+P_1)\vert u\rangle=(1+e^{iq})/L`$.

  The corresponding component of $`K^\dagger\Omega_\sigma`$ is its $`\mathcal R`$-image, and the excitation energy is $`\varepsilon_q+O(\gamma)`$. For even $`f`$, $`\sum_q(1+e^{iq})^2f(q)=\sum_q2\cos q(1+\cos q)f(q)`$. Two-object excitations contribute $`O(\gamma^4)`$.

The denominators stay away from zero by R1 ($`|2R_k|<\varepsilon_1`$) for FG, and by (6.4) at $`\tau=0`$ ($`2M_k\neq\varepsilon_q`$) for (a) and (c).

### Step 5. Item 1: curvature of the full grip

Put $`\theta=\theta_c=0`$ in (5.5):
- $`2\sigma R_k=2ng_\sigma[1+g^2(s_1^2-s_2/L)]`$;
- $`a^2=1-2ng^2S_2`$;
- $`2\sigma R_kJ^{\rm exc}=O(n^2|g|^3\langle\varepsilon_q^{-3}\rangle_q)=O(N_f^2\varkappa_k^3)`$.

By (5.2) and (5.3), under (5.4) and R1:

```math
E''_{k,\sigma}(0)=\frac{\tau^2}{n\sigma\gamma M_k}\Bigl[1-\gamma^2M_k^2K_L+O(N_f^2\varkappa_k^3)\Bigr]+O\Bigl(\frac{\tau^4}{d_{k,\sigma}^3}\Bigr),\qquad K_L=2nS_2+s_1^2-\frac{s_2}L\simeq\frac{(N_f+1)L^2}{180\,t_f^2}.\qquad\text{(5.6)}
```

So $`\gamma^2M_k^2K_L\simeq(N_f+1)\varkappa_k^2/180`$. The leading term is the curvature $`\tau^2/(\sigma\tilde M)`$ of a Model D body with rest half-gap $`\tilde M=n\gamma M_k`$: in FG the mean density of the field supplies the rest term. Beyond R1, (5.2) still gives the order-$`\tau^2`$ curvature wherever $`d_{k,\sigma}>2\tau`$; for the lower branch this holds at every $`\gamma\neq0`$ for small enough $`\tau`$. The check of (5.2) and (5.6) against the exact dressed level is under "Code".

### Step 6. Item 2: inertia against cost

**Which cost.** The held cost (3.4) enters every comparison. By Step 2, $`E_{k,\sigma}(0)-N_f\varepsilon_0(0)-\mathrm{Cost}_{k,\sigma}=O(\tau^2)`$, without the factor $`1/R_k`$. Divided by $`v^2`$ it is $`O(\tau^0)`$, below the order $`\tau^{-2}`$ of $`\mu`$. So the dressed level gives the same answers here, and the bracket of (6.12) reduces to the held cost as $`\tau\to0`$.

**Criterion (M6).** One speed $`v`$ for all levels and branches means that $`D_{k,\sigma}:=\mu_{k,\sigma}-\mathrm{Cost}_{k,\sigma}/v^2`$ does not depend on $`(k,\sigma)`$; the constant is the reference of the cost. Equivalently, every difference of inertia between levels and branches equals the difference of cost divided by $`v^2`$.

**Leading order.**
- FG: by (5.3) and (5.5), $`a^2=1+O(\gamma^2)`$ and $`2\sigma R_kJ^{\rm exc}=O(\gamma^3)`$, so $`\mu=\sigma R_k/\tau^2+O(\gamma^3)`$.
- (a), (c): (2.14), with $`\mathrm{Cost}=\sigma R_k+O(\gamma^2)`$.

Together:

```math
\mu_{k,\sigma}=\frac{\mathrm{Cost}_{k,\sigma}}{v^2}+O(\gamma^2)\ \text{ for every }k,\sigma,\qquad v=\tau\ \text{ (a), FG},\qquad v=\tau(1+\gamma n)\ \text{ (c)}.\qquad\text{(5.7)}
```

For FG the leading term is of order $`\gamma`$: $`\mu=n\sigma\gamma M_k/\tau^2`$.

**Identification of $`v`$.** $`v`$ is the slope at $`P\to0`$ of the band of the motion term alone, with its mean-field factor: $`\pm v\lvert\sin P\rvert`$. This is the $`M_k\to0`$ limit of the mean-field bands $`(M_k^2(1+\gamma n)^2+\tau^2\sin^2P)^{1/2}`$ (a), $`(1+\gamma n)(M_k^2+\tau^2\sin^2P)^{1/2}`$ (c) and $`(n^2\gamma^2M_k^2+\tau^2\sin^2P)^{1/2}`$ (FG).
- In the regime every level has a nonzero mean-field half-gap, so its group velocity stays below $`v`$; no level attains it.
- For FG, $`\pm\tau\lvert\sin P\rvert`$ is the band of the description at $`\gamma=0`$.
- $`v`$ does not depend on $`t_f`$, so it is not fixed by the field band $`-2t_f\cos q`$.

**Order $`\gamma^2`$.** Changing $`v`$ at order $`\gamma^2`$ ($`v^2\to v^2(1+b\gamma^2)`$) adds $`b\gamma^2\sigma M_k/\tau^2+O(\gamma^3)`$ to $`D`$ for (a) and (c), and only $`O(\gamma^3)`$ for FG.

*FG.* By (5.3) and (5.5):

```math
D_{k,\sigma}=-\frac{C^{\rm ev}_k}{\tau^2}+O(\gamma^3)=\frac{n\ell_0\gamma^2M_k^2}{t_f\tau^2}+O(\gamma^3),\qquad (\mu_{k,\sigma}-\mu_{k',\sigma'})-\frac{\mathrm{Cost}_{k,\sigma}-\mathrm{Cost}_{k',\sigma'}}{\tau^2}=\frac{n\ell_0\gamma^2(M_k^2-M_{k'}^2)}{t_f\tau^2}+O(\gamma^3).\qquad\text{(5.8)}
```

The branch differences at one level still agree through $`O(\gamma^2)`$, but the level differences do not. The inertia follows the branch-odd part of the cost, not its even part (the second-order mark).

*(a) and (c).* With $`v`$ of (5.7), (5.3) and (5.5) give
```math
D_{k,\sigma}=-\frac{C^{\rm ev}_k}{\tau^2}+\frac{\sigma M_k}{\tau^2}\bigl(2ng^2S_2-2\sigma M_kJ^{\rm exc}_{k,\sigma}\bigr)+O(\gamma^3).
```
The bracket equals $`\frac{n\gamma^2M_k^2}{t_f^2}\bigl\langle\frac{(1+\cos q)(\sigma M_k-t_f)}{(1-\cos q)(2\sigma M_k-\varepsilon_q)}\bigr\rangle_q`$ for (a), using $`1-\frac{2\sigma M\cos q}{2\sigma M-\varepsilon_q}=\frac{2(1-\cos q)(\sigma M-t_f)}{2\sigma M-\varepsilon_q}`$. For (c) it equals $`\frac{n\gamma^2M_k}{2t_f^2}\bigl\langle\frac{(1+\cos q)(M_k+\sigma t_f\cos q)}{1-\cos q}\bigr\rangle_q`$: the vertex $`(\varepsilon_q-2\sigma M_k)^2/(4\varepsilon_q^2)`$ cancels the denominator. Hence

```math
\begin{aligned}
D^{(a)}_{k,\sigma}&=\frac{n\gamma^2M_k^2}{2t_f^2\tau^2}\Bigl\langle\frac1{1-\cos q}\Bigl[t_f+\frac{2M_k(1+\cos q)(M_k-\sigma t_f)}{2\sigma M_k-\varepsilon_q}\Bigr]\Bigr\rangle_q+O(\gamma^3),\\
D^{(c)}_{k,\sigma}&=\frac{n\gamma^2M_k^2}{2t_f^2\tau^2}\Bigl\langle\frac{t_f(1+\cos q+\cos^2q)+\sigma M_k(1+\cos q)}{1-\cos q}\Bigr\rangle_q+O(\gamma^3).
\end{aligned}\qquad\text{(5.9)}
```

For $`\sigma=+`$, this is the $`\tau\to0`$ value of $`-[M_k^2\Delta''_{k,+}/\tau^2+\Delta_{k,+}]/\tau^2`$, the term of (6.12) that the quoted inputs leave unevaluated.

Two limits of (5.9):
- **$`t_f\gg M_kL^2`$** (all $`\varepsilon_q\gg M_k`$). $`D^{(a)}=\frac{n\ell_0\gamma^2M_k^2}{t_f\tau^2}(1+O(M_kL^2/t_f))`$ and $`D^{(c)}=\frac{n\gamma^2M_k^2}{2t_f\tau^2}\langle\frac{1+\cos q+\cos^2q}{1-\cos q}\rangle_q(1+O(M_kL^2/t_f))`$. Both are branch-even and proportional to $`M_k^2`$; the branch-odd term $`b\gamma^2\sigma M_k/\tau^2`$ cannot remove them.
- **$`t_f\ll M_k`$.** Both equal $`\sigma\frac{n\gamma^2M_k^3}{2t_f^2\tau^2}\langle\frac{1+\cos q}{1-\cos q}\rangle_q(1+O(t_f/M_k))`$. They are branch-odd but proportional to $`M_k^3`$, which $`b\gamma^2\sigma M_k`$ removes for at most one value of $`M_k`$.

So there is no single $`v`$ at order $`\gamma^2`$ in either limit. Away from the resonances $`2M_k=\varepsilon_q`$, $`D`$ is analytic in $`t_f`$, so the condition can hold at most at isolated values of $`t_f`$.

**Controls.**
- **(5.7).** It holds for every member of the class in the regime, so there is no control in the class. In the wider class with a branch-even clock term $`\mathbb 1_2\otimes D'`$ added to the body ($`D'`$ diagonal in the levels, not proportional to $`\mathbb 1`$), $`\mathrm{Cost}_{k,\sigma}`$ shifts by $`D'_k`$. $`E_{k,\sigma}(P)`$ shifts by the same $`D'_k`$ at every $`P`$, so $`\mu`$ is unchanged and (5.7) fails at order $`\gamma^0`$.
- **(5.8), (5.9).** Control: a body with one half-gap ($`D=0`$, a wider class). Then $`D_{k,\sigma}=D_\sigma`$. For FG, $`v=\tau`$ holds through $`O(\gamma^2)`$. For (a) and (c), $`b`$ removes the odd part of $`D_\sigma`$ and the even part is a constant.
### Step 7. Item 3: weight over inertia

By (3.12) and (3.13), $`\Delta W_{k,\sigma}=\mathcal W(C^{\rm mark}_{k,\sigma})`$ for (a) and (c) (they coincide at $`\tau=0`$) and for FG ($`\theta=0`$). The rest term does not depend on the place, so all three share
```math
C^{\rm mark}_{k,\sigma}=\mathrm{Cost}_{k,\sigma}-\theta\sigma M_k=n\sigma\gamma M_k-n\ell_0\gamma^2M_k^2/t_f+O(\gamma^3).
```
For $`E''`$ use (6.10), $`\sigma\tau^2(1\mp\gamma n)/M_k+O(\gamma^2)`$ for (a) and (c), and (5.6) for FG. With $`\mathcal W(C)=FC+F_2C^2+O(C^3)`$:

```math
E''_{k,\sigma}(0)\,\Delta W_{k,\sigma}=\tau^2F\,\Lambda\,\bigl[1+\sigma\gamma M_k\,\Xi+O(\gamma^2)\bigr]+O(g_s^2),\qquad \Xi:=\frac{nF_2}F-\frac{\ell_0}{t_f}=-\frac{[\ell^2+2\ell_0\ell-2\ell^{(2)}/\lvert X_f\rvert]}{2t_f\,[\ell]},\qquad\text{(5.10)}
```

with $`\Lambda=1`$ for FG, $`n\gamma(1-\gamma n)`$ for (a) and $`n\gamma(1+\gamma n)`$ for (c).
- **Leading order.** The product is the same for all levels and both branches.
- **First dependence.** At relative order $`\gamma`$, $`\sigma\gamma M_k\Xi`$, with one coefficient $`\Xi`$ for all three couplings. Since $`\ell,\ell_0=O(L)`$ and $`\ell^{(2)}=O(L^3)`$, $`\lvert\gamma M_k\Xi\rvert=O(\varkappa_k)`$.

The mechanism: $`E''\Delta W\propto\mathcal W(C^{\rm mark})/R_k`$. The weight follows the whole mark, nonlinearly; the inertia follows only its branch-odd part.

**(7.7) for FG.** The premises of (7.7) are:
- a start with real envelope in an isolated band;
- the held weight as the place dependence at first order in $`g_s`$;
- the coefficient of $`\tau^2`$.

FG provides all three: by (5.1)–(5.4) the band at order $`\tau^2`$ has the same form, $`E^0_\sigma+\text{const}-\frac{\tau^2}2J\cos2P`$, and $`W`$ is that of (3.12) with $`\theta=0`$. So (7.7) applies to FG with $`E''`$ of (5.2), and the fall from rest inherits the level dependence of (5.10).

**Controls.**
- **Leading universality.** In the wider class of bodies whose motion term carries a level-dependent factor $`A\otimes f(D)`$, $`E''`$ scales with $`f(D_k)^2`$ while $`\Delta W`$ is unchanged, so universality fails at leading order.
- **(a), (c) with unequal couplings** of the $`m`$ and $`D`$ parts (M7) also fail. For FG such unequal couplings keep $`\Lambda=1`$.
- **The $`O(\gamma)`$ dependence.** In the wider class of a body with a position-dependent rest term and no field object (A10), $`E''\Delta W`$ is exactly universal.
### Step 8. Item 4: the hopping of the field

Take $`n,\gamma,M_k,\tau`$ fixed (and $`L`$, unless stated).
- **$`v`$.** (5.7) does not depend on $`t_f`$.
- **Isolation, FG.** The lower branch needs only $`\tau<\frac12\min(\Delta_b,\varepsilon^-_1)`$. For $`N_f\ge2`$, the upper branch lies below the excited lower-branch levels only if $`\varepsilon_1>2n|\gamma|M_k`$ (leading order in $`\varkappa_k`$), that is $`t_f>n|\gamma|M_k/(1-\cos\frac{2\pi}L)\simeq N_f|\gamma|M_kL/(2\pi^2)`$. In every case $`d_{k,\sigma_u}\le\varepsilon^+_1<\varepsilon_1`$. R1 needs $`t_f\gg N_f|\gamma|M_kL`$.
- **Isolation, (a) and (c).** The denominators of (5.9) avoid zero when $`\varepsilon_1>2M_k`$ or $`4t_f<2M_k`$.
- **Size of the first level dependence.** It stays at order $`\gamma^2`$ in $`\mu`$, with relative size

```math
\frac{\tau^2D_{k,\sigma}}{\sigma R_k}=\begin{cases}\sigma\gamma M_k\ell_0/t_f&\text{FG},\\ \sigma n\gamma^2M_k\ell_0/t_f\ \text{(a)},\quad \sigma n\gamma^2M_kL\,(1+O(L^{-1}))/(4t_f)\ \text{(c)},& t_f\gg M_kL^2,\\ n\gamma^2M_k^2\bigl\langle\frac{1+\cos q}{1-\cos q}\bigr\rangle_q/(2t_f^2)\simeq n\gamma^2M_k^2L/(6t_f^2)\ \text{(a), (c)},& t_f\ll M_k,\end{cases}\qquad \gamma M_k\Xi=O\Bigl(\frac{\gamma M_kL}{t_f}\Bigr).\qquad\text{(5.11)}
```

- **$`t_f`$ large.** Every level and branch dependence of items 2 and 3 vanishes as $`1/t_f`$, and the body approaches the mean-field Model D body.
- **$`t_f`$ small against $`M_k`$** (with R1 kept by a small $`\gamma`$). FG keeps (5.8). In (a) and (c) the dependence grows as $`1/t_f^2`$ and becomes branch-odd.
- **$`t_f`$ small against $`\tau`$.**
  - The FG upper branch is not isolated, since $`d_{k,\sigma_u}<\varepsilon_1\simeq4\pi^2t_f/L^2<2\tau`$.
  - The lower branch is isolated for $`t_f\ll\tau\ll|\gamma|M_k`$. There $`J=\langle K^\dagger\Omega_\sigma\vert R\vert K\Omega_\sigma\rangle=O(t_f^{2N_f})`$: every object must move from beside the body on one side to the other side, by two hops of amplitude $`t_f`$. At $`t_f=0`$, $`R`$ is diagonal in places and $`J=0`$.
  - So $`\mu\to\infty`$ while $`\mathrm{Cost}_{k,\sigma_l}\to-N_f|\gamma|M_k`$: the inertia does not follow the cost.
- **$`L\to\infty`$ at fixed $`n`$.** $`N_f\varkappa_k=n|\gamma|M_kL^2/t_f\to\infty`$: R1, the upper-branch isolation and (5.6)–(5.10) fail, and the order-$`\gamma^2`$ level dependences grow in proportion to $`L`$ ($`\ell_0\simeq L/12`$, $`\langle(1-\cos q)^{-1}\rangle_q\simeq L/6`$). (5.2) and (5.3) still hold for the lower branch.

## Result

Class: one Model D body on the ring field of $`N_f\ge1`$ objects, $`L\ge5`$, couplings (a), (c) and FG, field state A1, every level $`k`$ and both branches.

- **(5.1)** The sector contract has the form (6.1) with $`\hat C^{(0)}_\sigma=\theta\sigma M_k+C_1+g_\sigma\Phi_0`$ and $`\hat C^{(+)}=\frac\tau2(-i\sigma_1)\otimes K`$. For FG, (6.1) applies unchanged and only $`\hat C^{(0)}`$ changes ($`\theta=0`$).
- **(5.2)** Wherever the $`\tau=0`$ level is isolated at distance $`d_{k,\sigma}`$: $`E''_{k,\sigma}(0)=2\tau^2J_{k,\sigma}+O(\tau^4\lVert K\rVert^4/d^3_{k,\sigma})`$, exact in $`\gamma`$.
- **(5.3)** $`\mathrm{Cost}_{k,\sigma}=\sigma R_k+C^{\rm ev}_k`$ and, at order $`\tau^{-2}`$, $`\mu_{k,\sigma}=\sigma R_k/[\tau^2(a^2_{k,\sigma}+2\sigma R_kJ^{\rm exc}_{k,\sigma})]`$. The inertia is set by the branch-odd part $`R_k`$ of the held cost. The dressed level at $`P=0`$ differs from the held level by $`O(\tau^2)`$, without the factor $`1/R_k`$.
- **(5.4)** FG isolation: $`\tau<\frac12d_{k,\sigma}`$, with $`d`$ as displayed (at leading order in $`\varkappa_k`$).
  - The lower branch ($`\sigma\gamma<0`$) is isolated for every $`\gamma\neq0`$, every $`L`$ and every $`N_f`$.
  - For $`N_f=1`$ the upper branch is isolated for every $`\gamma\neq0`$.
  - For $`N_f\ge2`$ the upper level lies below every excited lower-branch level iff $`\Delta_b<\varepsilon^-_1`$ (in R1: $`2n|\gamma|M_k<\varepsilon_1`$); beyond, it crosses lower-branch levels at isolated values of $`\gamma`$.
  - Isolation fails as $`\gamma\to0`$ (both branches) and as $`L\to\infty`$ at fixed $`n,\gamma`$ (upper branch).
- **(5.5)** Weak-mark expansions of $`\varphi_g`$, $`\varepsilon_0`$, $`R_k`$, $`C^{\rm ev}_k=-n\gamma^2M_k^2\ell_0/t_f+O(\gamma^4)`$, $`a^2`$ and $`J^{\rm exc}`$, through the displayed orders, under R1 (FG) or (6.4) at $`\tau=0`$ ((a), (c)).
- **(5.6)** Item 1. Under (5.4) and R1, $`E''_{k,\sigma}(0)=\frac{\tau^2}{n\sigma\gamma M_k}[1-\gamma^2M_k^2K_L+O(N_f^2\varkappa_k^3)]+O(\tau^4/d^3_{k,\sigma})`$, with $`\gamma^2M_k^2K_L\simeq(N_f+1)\varkappa_k^2/180`$. The leading term is the curvature of a Model D body with half-gap $`n\gamma M_k`$.
- **(5.7)** Item 2 at leading order. $`\mu_{k,\sigma}=\mathrm{Cost}_{k,\sigma}/v^2+O(\gamma^2)`$ for every level and branch, with $`v=\tau`$ for (a) and FG and $`v=\tau(1+\gamma n)`$ for (c). The held cost enters; the dressed level gives the same answer. $`v`$ is the slope at $`P\to0`$ of the band $`\pm v\lvert\sin P\rvert`$ of the mean-field motion term alone. No level attains it, and it is independent of $`t_f`$, so it is not fixed by the field band.
- **(5.8)** Item 2 at order $`\gamma^2`$, FG. $`\mu_{k,\sigma}-\mathrm{Cost}_{k,\sigma}/\tau^2=n\ell_0\gamma^2M_k^2/(t_f\tau^2)+O(\gamma^3)`$. Branch differences agree through $`O(\gamma^2)`$, but level differences differ by $`n\ell_0\gamma^2(M_k^2-M_{k'}^2)/(t_f\tau^2)`$. There is no single $`v`$ at order $`\gamma^2`$ (in R1).
- **(5.9)** Item 2 at order $`\gamma^2`$, (a) and (c). $`D_{k,\sigma}`$ is given by (5.9), at leading order in $`\tau`$. In the limits $`t_f\gg M_kL^2`$ and $`t_f\ll M_k`$ no change of $`v`$ makes it level- and branch-independent, so there is no single $`v`$ at order $`\gamma^2`$. For other $`t_f`$ the condition can hold only at isolated values of $`t_f`$.
- **(5.10)** Item 3, at first order in $`g_s`$. $`E''_{k,\sigma}(0)\Delta W_{k,\sigma}=\tau^2F\Lambda[1+\sigma\gamma M_k\Xi+O(\gamma^2)]`$, with $`\Lambda=1`$ (FG), $`n\gamma(1\mp\gamma n)`$ ((a), (c)). It is the same for all levels and both branches at leading order. The first level and branch dependence is $`\sigma\gamma M_k\Xi`$ at relative order $`\gamma`$, of size $`O(\varkappa_k)`$, with the same $`\Xi`$ for the three couplings. (7.7) applies to FG with $`E''`$ of (5.2).
- **(5.11)** Item 4.
  - $`v`$ is independent of $`t_f`$.
  - For $`N_f\ge2`$, the FG upper level lies below the excited lower-branch levels only for $`t_f>n|\gamma|M_k/(1-\cos\frac{2\pi}L)`$ (leading order in $`\varkappa_k`$).
  - The first level dependence stays at order $`\gamma^2`$, with the relative sizes displayed. It vanishes as $`1/t_f`$ for large $`t_f`$, and in (a) and (c) it grows as $`1/t_f^2`$ for $`t_f\ll M_k`$.
  - For $`t_f\ll\tau`$ the FG upper branch is not isolated. The FG lower branch is isolated for $`\tau\ll|\gamma|M_k`$, and there $`\mu\to\infty`$ as $`t_f\to0`$ at finite cost.
  - At fixed $`n`$ and $`\gamma`$, (5.6)–(5.10) have no $`L\to\infty`$ limit (R1 fails); (5.2) and (5.3) still hold for the lower branch.

## Consistency checks

1. **$`\gamma\to0`$ and mean field for (a), (c) against (6.10).** With $`a=1+\theta_c\gamma n`$, $`J^{\rm exc}=0`$ and $`R_k=M_k(1+\gamma n)`$, (5.2)–(5.3) give $`\sigma\tau^2/(M_k(1+\gamma n))`$ for (a) and $`\sigma\tau^2(1+\gamma n)/M_k`$ for (c). These are the mean-field parts of (6.10), and both reduce to $`\sigma\tau^2/M_k`$ at $`\gamma=0`$. Passed.
2. **FG at mean field against a body with a rest term.** The leading term of (5.6), $`\tau^2/(\sigma n\gamma M_k)`$, is the curvature at $`P=0`$ of $`\pm(\tilde M^2+\tau^2\sin^2P)^{1/2}`$ with $`\tilde M=n\gamma M_k`$. That body's held cost $`\sigma\tilde M`$ equals the leading FG cost. Passed.
3. **Dimensions.** $`\tau,t_f,M_k,g_s`$, costs and $`E''`$ are contract units, and $`\gamma,n,P,\ell,F`$ are dimensionless. $`K_L\propto t_f^{-2}`$, and $`\tau^2D/(\sigma R)`$ and $`\gamma M_k\Xi`$ are dimensionless. $`E''\Delta W=\tau^2F\Lambda`$ has units of contract squared. Passed.

## Open issues

- The error term of (7.7) for FG is not re-derived.
- FG beyond R1 (strong mark), including the lower branch as $`L\to\infty`$ at fixed $`n`$: (5.2) holds there, but items 2 and 3 are not evaluated.
- (5.9) is derived at $`\tau\to0`$ only; the finite-$`\tau`$ bracket of (6.12) is not evaluated, and (5.9) is not checked numerically.
- $`N_f\ge2`$ and the FG upper branch beyond $`2n|\gamma|M_k=\varepsilon_1`$ are not checked numerically.
- The $`O(\gamma)`$ term of (5.10) has a control only in a wider class.
- The relation of $`v=\tau`$ to the maximal speed of 03-ilang-space is not quoted here and not used.

## Code

`code/v1/check_full_grip.py` (check) does the following:
- builds the sector contract (5.1) for FG with $`N_f=1`$, and verifies it against the full contract at $`L=6`$ (eigenvalues agree to $`4\times10^{-15}`$);
- for $`L=8,13`$, $`t_f=1`$, $`M_k\in\{1,1.4\}`$ ($`m=1`$, $`N=2`$, $`\lambda_0=5\pi/2`$), $`\gamma\in\{0.01,0.02,0.3\}`$ and both branches, computes the exact curvature of the dressed level at $`P=0`$, by second-order perturbation in $`P`$ from a full diagonalization, at $`\tau=10^{-5}`$ and $`\tau=d/5`$, together with the exact isolation distance $`d`$;
- compares it with (5.2) and (5.6);
- compares $`\tau^2\mu-\mathrm{Cost}`$, its level and branch differences, and $`E''\Delta W/(\tau^2F)`$ with (5.8) and (5.10), and $`\Delta W`$ with (3.13).

Output: `code/v1/output/check_full_grip.txt`. Results:
- (5.2): agreement to $`\le1.4\times10^{-12}`$ at $`\tau=10^{-5}`$ ($`\le5\times10^{-10}`$ at $`\gamma=0.3`$, $`\varkappa_k\le5.5`$); at $`\tau=d/5`$ to $`\le9\times10^{-9}`$ ($`\gamma\le0.02`$) and $`\le1.1\times10^{-3}`$ ($`\gamma=0.3`$).
- (5.6): agreement to $`\le1.2\times10^{-5}`$ for $`N_f\varkappa_k\le0.36`$, with deviation $`\propto\gamma^3`$; up to $`0.1`$ at $`\gamma=0.3`$ (outside R1).
- (5.8): $`\tau^2\mu-\mathrm{Cost}`$ within $`2.4\%`$ (the deviation is branch-odd, $`O(\gamma^3)`$); the level difference $`k=1`$ minus $`k=0`$ within $`3.2\%`$; $`\tau^2(\mu_+-\mu_-)`$ equals $`\mathrm{Cost}_+-\mathrm{Cost}_-`$ to $`\le7\times10^{-4}`$ of the latter.
- (5.10): the branch-odd part of $`E''\Delta W/(\tau^2F)-1`$ equals $`\gamma M_k\Xi`$ to $`\le0.2\%`$ ($`\Xi=-0.167`$ for $`L=8`$, $`-0.808`$ for $`L=13`$, places $`r=2,3`$); the branch-even part is $`O(\gamma^2)`$; (3.13) reproduces $`\Delta W`$ to $`O(C^3)`$.

## Methods used

- sector decomposition by joint translation; reflection symmetry
- Rayleigh–Schrödinger perturbation theory; Kato's isolation criterion
- spectral decomposition of resolvents; Franck–Condon overlaps of product states
- Perron–Frobenius; secular equation of a rank-one perturbation
- Fourier sums on the ring
- exact diagonalization; second-order perturbation in $`P`$ (numerical check)
