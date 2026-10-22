# Inertia of a body with its own mark against its cost

- **Subproject:** 07-ilang-weight
- **Package:** 05-inertia-of-mark
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-21

## Changes from previous version

- Setup: Schrieffer–Wolff (direct rotation) and Weyl's inequality added to A3; small-$`t_f`$ statements carry an order of limits (A2) (I1, I2).
- Step 3: "where it fails" now refers to the $`\tau=0`$ distance $`d_{k,\sigma}`$ and to the sufficient criterion, not to the exact level (I1).
- Step 4, last paragraph: the one-object denominators are separated from the full many-object condition (6.4) (I4).
- Step 6: the one-speed question at order $`\gamma^2`$ is settled over the non-resonant class by the line criterion (5.12): (c) is excluded by its branch average, and for (a) the solutions are determined numerically for $`5\le L\le16`$ (isolated two-level ratios) (I3). (5.9) is now checked numerically.
- Step 7: (5.10) states $`F\neq0`$ and $`\Xi\neq0`$; reflection-equivalent pairs are treated; $`\Xi`$ is given in closed form; the next order (5.15) is given where $`\Xi=0`$ (I5).
- Step 7: (7.7) for the full grip is derived as (5.14), with a remainder in the full-grip gap $`d_s`$ and a condition on the source (I2).
- Step 8: isolation of (a), (c) is stated with the full (6.4) and its Kato bound (I4). Small $`t_f`$: failure of the criterion is separated from non-isolation, the $`\tau^2`$ coefficient from the exact curvature, with the winding curvature (5.13) and an order of limits (I1).
- Result, Open issues, Code and Methods updated; four new scripts in `code/v2/`.

## Response to verification

- I1: Accepted and fixed in Step 8 ("$`t_f`$ small", (5.13)) and Step 3. The upper-branch statement is now a failure of the criterion (5.4), not a claim of non-isolation. The divergence of the inertia is restricted to the coefficient of $`\tau^2`$ ($`\tau\to0`$ first), with the range of $`t_f`$ at fixed $`\tau`$ in which it holds. At fixed $`\tau`$ the exact curvature tends to the winding value (5.13), which is checked numerically.
- I2: Accepted and fixed in Step 7 ("(7.7) for FG"). The source-perturbed effective band contract and the band position operator are derived through order $`\tau^2g_s`$. They give (5.14), with remainder $`O(\tau^2N_f^2g_s^2/d_s^2)+O(\tau^4N_f|g_s|/d_s^3)`$ under $`\tau<d_s/2`$, $`N_f|g_s|\le d_{k,\sigma}/4`$. The check uses the joint evolution with a held source.
- I3: Accepted and fixed in Step 6, (5.12). (c): the branch average excludes one speed for every non-resonant member. (a): the equality conditions are solved; solutions exist only for two-level bodies at isolated ratios $`M_0/t_f,M_1/t_f`$ (searched for $`5\le L\le16`$).
- I4: Accepted and fixed in Step 8 ("Isolation, (a) and (c)") and Step 4. The full condition (6.4) with sums of up to $`N_f`$ excitation energies is kept, together with its distance and the bound $`\tau\lVert K\rVert<d_{k,\sigma}/2`$, and distinguished from the one-object denominators of (5.9).
- I5: Accepted and fixed in Step 7. The section states $`F\neq0`$ (iff the places are not reflection-equivalent) and $`\Xi\neq0`$; for reflection-equivalent places $`\Delta W=0`$ exactly. It derives $`\Xi=-(\rho^2+\rho'^2-1)/(3Lt_f)`$ and gives the next dependence (5.15) where $`\Xi=0`$.

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
  - Statements at small $`t_f`$ concern the coefficient of $`\tau^2`$ unless an order of limits is stated (Step 8).
- **A3 (standard mathematics).**
  - Rayleigh–Schrödinger (RS) perturbation theory for a nondegenerate isolated eigenvalue: for $`\lVert V\rVert<d/2`$, with $`d`$ the distance to the rest of the unperturbed spectrum, the eigenvalue continues analytically (Kato).
  - Schrieffer–Wolff (SW, direct rotation) for an isolated group of eigenvalues: for $`\lVert V\rVert<d/2`$ a unitary $`e^{S}`$, $`S`$ block-off-diagonal with $`\lVert S\rVert=O(\lVert V\rVert/d)`$, maps the unperturbed band onto the perturbed spectral subspace. Weyl's inequality.
  - Fourier sums on the ring, for example $`\sum_{j=1}^{L-1}\sin^{-2}(\pi j/L)=(L^2-1)/3`$; Perron–Frobenius.

**Inputs used:** (6.1), (6.4), (6.10), (6.12) of 06-ilang-source/06-own-mark; (2.14) of 02-two-free-bodies; (3.4), (3.12), (3.13) of 03-weight-of-mark; (7.7) of 06-ilang-source/07-dressed-fall, for (a) and (c) (its FG form is derived in Step 7). (6.5) of 06-ilang-source/06-own-mark is quoted but not needed, because (5.2) is exact in $`\gamma`$.

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

Where $`d_{k,\sigma}`$ vanishes or tends to zero (then (5.4) fails at every fixed $`\tau>0`$; this concerns the $`\tau=0`$ spectrum and the sufficient criterion, not the exact level at $`\tau>0`$):
1. **$`\gamma\to0`$, both branches.** $`d\to0`$: without coupling the FG body is gapless, with band $`\pm\tau\lvert\sin P\rvert`$.
2. **Upper branch, $`N_f\ge2`$.** As $`2n|\gamma|M_k`$ approaches $`\varepsilon_1`$, the upper level crosses the lowest excited level of the other branch (the branches do not mix at $`\tau=0`$). Beyond that it crosses multi-object excitations at isolated values of $`\gamma`$.
3. **$`N_f=1`$: no crossing.** The even eigenvalues of $`h(\pm|g|)`$ solve $`\pm1/|g|=\langle0\vert(E-C_1)^{-1}\vert0\rangle`$, which decreases between consecutive poles; the odd ones are $`\ge-2t_f\cos(2\pi/L)`$. Hence $`\varepsilon_0(|g|)`$ lies strictly between the two lowest eigenvalues of $`h(-|g|)`$. The upper branch is isolated for every $`\gamma\neq0`$, with $`d_{k,\sigma_u}\to0`$ as $`\varkappa_k\to\infty`$.
4. **$`L\to\infty`$ at fixed $`n,\gamma`$.** $`\varepsilon_1\to0`$, so $`d_{k,\sigma_u}\le\varepsilon_1^+\to0`$. The lower branch stays isolated, with $`d_{k,\sigma_l}\to\sqrt{4t_f^2+\gamma^2M_k^2}-2t_f`$ (the binding gap of the infinite chain; $`\Delta_b\propto N_f\to\infty`$).

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

The one-object denominators $`2\sigma R_k-\varepsilon_q`$ stay away from zero by R1 ($`|2R_k|<\varepsilon_1`$) for FG, and for (a) and (c) by the one-object part of (6.4) at $`\tau=0`$ ($`2M_k\neq\varepsilon_q`$). (6.4), assumed in A2, also excludes the many-object resonances. They enter $`J`$ only at $`O(\gamma^4)`$, but they set the distance $`d_{k,+}`$ (Step 8).

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

For $`\sigma=+`$, this is the $`\tau\to0`$ value of $`-[M_k^2\Delta''_{k,+}/\tau^2+\Delta_{k,+}]/\tau^2`$, the term of (6.12) that the quoted inputs leave unevaluated. At $`N_f=1`$, (5.9) agrees with $`\tau^2D`$ from the exact $`\tau^2`$ coefficient (5.2) up to $`O(\gamma^3)`$ (code, `check_inertia_ac.py`).

Two limits of (5.9):
- **$`t_f\gg M_kL^2`$** (all $`\varepsilon_q\gg M_k`$). $`D^{(a)}=\frac{n\ell_0\gamma^2M_k^2}{t_f\tau^2}(1+O(M_kL^2/t_f))`$ and $`D^{(c)}=\frac{n\gamma^2M_k^2}{2t_f\tau^2}\langle\frac{1+\cos q+\cos^2q}{1-\cos q}\rangle_q(1+O(M_kL^2/t_f))`$. Both are branch-even and proportional to $`M_k^2`$.
- **$`t_f\ll M_k`$.** Both equal $`\sigma\frac{n\gamma^2M_k^3}{2t_f^2\tau^2}\langle\frac{1+\cos q}{1-\cos q}\rangle_q(1+O(t_f/M_k))`$: branch-odd and proportional to $`M_k^3`$.

**One speed at order $`\gamma^2`$, whole non-resonant class.** With $`y:=\sigma M_k/t_f`$, (5.9) reads

```math
\tau^2D_{k,\sigma}=n\gamma^2t_f\,\mathbb F(y)+O(\gamma^3),\qquad \mathbb F_a(y)=\frac{y^2}2\Bigl\langle\frac{1}{1-\cos q}\Bigl[1+\frac{(1+\cos q)\,y(y-1)}{y-1+\cos q}\Bigr]\Bigr\rangle_q,\qquad \mathbb F_c(y)=\frac{y^2}2\Bigl\langle\frac{1+\cos q+\cos^2q+y(1+\cos q)}{1-\cos q}\Bigr\rangle_q.\qquad\text{(5.12)}
```

A change of $`v`$ at order $`\gamma`$ adds a branch-odd term at order $`\gamma`$, which (5.7) excludes. A change $`v^2\to v^2(1+b\gamma^2)`$ adds $`b\gamma^2\sigma M_k/\tau^2`$. So one $`v`$ exists at order $`\gamma^2`$ iff the $`2N`$ points $`(y,\mathbb F(y))`$, $`y=\pm M_k/t_f`$, lie on one straight line. The condition depends only on $`L`$ and the ratios $`M_k/t_f`$, not on $`N_f`$, $`\gamma`$ or $`\tau`$.
- **(c).** The branch average $`\frac12[\mathbb F_c(y)+\mathbb F_c(-y)]=\frac{y^2}2\langle\frac{1+\cos q+\cos^2q}{1-\cos q}\rangle_q`$ is untouched by $`b`$. Its coefficient is positive ($`1+\cos q+\cos^2q\ge\frac34`$), so it differs between levels, since the $`M_k`$ are distinct and $`N\ge2`$. So (c) has no single $`v`$ at order $`\gamma^2`$, for every member of the non-resonant class.
- **(a).** $`\mathbb F_a`$ has poles at the one-object resonances $`y=1-\cos q`$ (where $`\cos q(1+\cos q)\neq0`$). Two levels share a line iff their chords coincide: with $`s(x):=[\mathbb F_a(x)-\mathbb F_a(-x)]/(2x)`$ and $`i(x):=[\mathbb F_a(x)+\mathbb F_a(-x)]/2`$, iff $`s(M_0/t_f)=s(M_1/t_f)`$ and $`i(M_0/t_f)=i(M_1/t_f)`$. These are the double points of the plane curve $`x\mapsto(s(x),i(x))`$.
  - In the variables $`(u_0+u_1,\,u_0u_1)`$, $`u=x^2`$, both equations have their poles on straight lines. A search over all roots (code) finds, for every $`5\le L\le16`$, isolated solutions: 1 for $`L=5,6,8`$ and up to 21 for $`L=15`$. For example $`L=7`$: $`(M_0,M_1)/t_f=(0.35551,1.35669)`$.
  - Every solution has a resonance value $`1-\cos q`$ between $`M_0/t_f`$ and $`M_1/t_f`$.
  - At this example the exact $`\tau^2`$ coefficient confirms one speed: the deviation from a common line is $`O(\gamma^3)`$, against $`O(\gamma^2)`$ at a generic pair (code).
  - No ratio occurs in two of the solutions found. So the search finds no body with $`N\ge3`$ levels and one $`v`$ at order $`\gamma^2`$ for $`5\le L\le16`$. (The search runs on two grids, which agree except for one point at $`L=15`$; its completeness is not proven.)

  So, for $`5\le L\le16`$, (a) has no single $`v`$ at order $`\gamma^2`$, except two-level bodies at isolated ratios $`M_0/t_f`$, $`M_1/t_f`$ that straddle a one-object resonance. There $`v^2=\tau^2(1+b\gamma^2)`$, with $`b`$ fixed by the common line.

**Controls.**
- **(5.7).** It holds for every member of the class in the regime, so there is no control in the class. In the wider class with a branch-even clock term $`\mathbb 1_2\otimes D'`$ added to the body ($`D'`$ diagonal in the levels, not proportional to $`\mathbb 1`$), $`\mathrm{Cost}_{k,\sigma}`$ shifts by $`D'_k`$. $`E_{k,\sigma}(P)`$ shifts by the same $`D'_k`$ at every $`P`$, so $`\mu`$ is unchanged and (5.7) fails at order $`\gamma^0`$.
- **(5.8), (5.9), (5.12).** For FG and (c): a body with one half-gap ($`D=0`$, a wider class). Then $`D_{k,\sigma}=D_\sigma`$. For FG, $`v=\tau`$ holds through $`O(\gamma^2)`$. For (c), $`b`$ removes the odd part of $`D_\sigma`$ and the even part is a constant. For (a) the class itself contains controls: the two-level bodies at the solutions of (5.12).
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
- **Conditions.** (5.10) needs $`g_s\neq0`$ and $`F\neq0`$. On the ring $`\ell(r)=\ell_0-r(L-r)/(2L)`$. With $`\rho:=r-L/2`$, $`\rho':=r'-L/2`$ this gives $`[\ell]=(\rho^2-\rho'^2)/(2L)`$, so $`F=0`$ iff $`\rho'=\pm\rho`$: $`x'=x`$, or $`x'`$ is the mirror image of $`x`$ with respect to the source (reflection-equivalent places). For such places the reflection about $`x_s`$ maps the held description at $`x`$ onto that at $`x'`$. So $`\Delta W_{k,\sigma}=0`$ exactly, for every level and branch and to all orders: the product vanishes, is trivially universal, and $`\Xi`$ is not defined.
- **$`\Xi`$ in closed form.** $`\ell^{(2)}`$ solves $`(2-T_+-T_-)\ell^{(2)}=\ell`$ with zero mean. On $`0\le r\le L`$ it is therefore the quartic $`a_2+\frac{L^2+4}{48L}\rho^2-\frac{\rho^4}{24L}`$, since the second difference of $`\rho^4`$ is $`12\rho^2+2`$. Inserted into (5.10):
  ```math
  \Xi=-\frac{\rho^2+\rho'^2-1}{3Lt_f}.
  ```
  So $`\Xi\le0`$, and $`\Xi=0`$ iff $`\{\rho^2,\rho'^2\}=\{0,1\}`$: $`L`$ even, one place antipodal to the source and the other next to it. (Code: agreement to $`10^{-14}`$ for $`5\le L\le16`$.)
- **Leading order.** The product is the same for all levels and both branches.
- **First dependence, $`\Xi\neq0`$.** At relative order $`\gamma`$, $`\sigma\gamma M_k\Xi`$, with one coefficient $`\Xi`$ for all three couplings, and $`\lvert\gamma M_k\Xi\rvert\le\gamma M_kL/(6t_f)=O(\varkappa_k)`$.
- **Next order, $`\Xi=0`$.** Insert $`C^{\rm mark}=ng_\sigma-ns_1g^2+ns_3g_\sigma^3+O(g^4)`$, $`s_3:=s_1^2-s_2/L`$ (from (5.5)), into (3.13) through $`F_3`$: $`\Delta W=Fng_\sigma[1+\Xi g_\sigma+\Psi_0g^2+O(g^3)]`$. For the curvature:
  - FG: the bracket of (5.6) applies.
  - (a), (c): by (5.3) and the expansion of $`D`$ above, $`E''=\sigma\tau^2\frac{(1+\theta_c\gamma n)^2}{M_k(1+\gamma n)}[1-\sigma(\tau^2D_{k,\sigma}+C^{\rm ev}_k)/M_k+O(\gamma^3)]`$.

  Hence

```math
\frac{E''_{k,\sigma}(0)\,\Delta W_{k,\sigma}}{\tau^2F\Lambda}=1+\sigma\gamma M_k\Xi+\gamma^2M_k^2\Psi_0-\begin{cases}\gamma^2M_k^2K_L&\text{FG}\\ \sigma(\tau^2D_{k,\sigma}+C^{\rm ev}_k)/M_k&\text{(a), (c)}\end{cases}+O(\gamma^3),\qquad \Psi_0:=s_3-2s_1\frac{nF_2}F+\frac{n^2F_3}F,\qquad\text{(5.15)}
```

  with $`\Lambda=1`$ (FG), $`n\gamma/(1+\gamma n)`$ (a), $`n\gamma(1+\gamma n)`$ (c), equal to the $`\Lambda`$ of (5.10) at its order. Where $`\Xi=0`$:
  - **FG.** The first dependence is a level dependence $`(\Psi_0-K_L)\gamma^2(M_k^2-M_{k'}^2)`$; the branches differ at the earliest at $`O(\gamma^3)`$. For $`N_f=1`$, $`(\Psi_0-K_L)t_f^2=-0.559,-1.025,-1.625,-2.359,-3.225,-4.225`$ for $`L=6,8,\dots,16`$ (code, which also confirms (5.15) against the exact $`\tau^2`$ coefficient at $`L=8`$ for the three couplings).
  - **(c).** A branch dependence at relative order $`\gamma^2`$: by (5.9) and $`\langle\frac{\cos q(1+\cos q)}{1-\cos q}\rangle_q=\frac{(L-2)(L-4)}{3L}`$, the branch-odd part is $`-\sigma\gamma^2M_k\,n(L-2)(L-4)/(6Lt_f)\neq0`$.
  - **(a).** The branch-odd part is $`\sigma\gamma^2M_k\frac{2nM_k^2}{t_f}\bigl\langle\frac{\cos q(1+\cos q)}{(1-\cos q)(4M_k^2-\varepsilon_q^2)}\bigr\rangle_q`$. It is nonzero except where this average vanishes.

The mechanism: $`E''\Delta W\propto\mathcal W(C^{\rm mark})/R_k`$. The weight follows the whole mark, nonlinearly; the inertia follows only its branch-odd part.

**(7.7) for FG.** (7.7) was derived for (a) and (c) only; for FG it is derived here. Fix the level $`k`$ and the branch $`\sigma`$.

1. *Held band with the source.* With the body at $`j`$, the held block is $`h_{j,\sigma}=C_1+g_\sigma\Phi_j+g_s\Phi_{x_s}`$ (absolute field places). Its lowest eigenvalue is $`\mathcal E_\sigma(j)=E^0_\sigma+W_\sigma(j)+O(N_f^2g_s^2/d_{k,\sigma})`$, with positive ground vector $`\Omega_\sigma(j)`$. Here $`W_\sigma(j)=g_s\langle\Omega_\sigma(j)\vert\Phi_{x_s}\vert\Omega_\sigma(j)\rangle`$ is the held weight, (3.12) with $`\theta=0`$. The vectors $`\lvert j\rangle\rangle:=\lvert j,\sigma\rangle\otimes\Omega_\sigma(j)`$ span the held band, with projector $`\Pi`$. Since $`\lVert g_s\Phi_{x_s}\rVert=N_f|g_s|`$, Weyl's inequality separates the band from the rest of the $`\tau=0`$ spectrum by $`d_s\ge d_{k,\sigma}-2N_f|g_s|`$. We require $`N_f|g_s|\le d_{k,\sigma}/4`$.
2. *Effective contract.* Let $`\tau<d_s/2`$, and let $`e^{S}`$ be the SW unitary (A3) from $`\Pi`$ to the band of the full contract. The motion term flips the branch, so the odd orders vanish:
   ```math
   H_{\rm eff}=\sum_jU(j)\lvert j\rangle\rangle\langle\langle j\rvert+\sum_jt(j)\bigl(\lvert j+1\rangle\rangle\langle\langle j-1\rvert+{\rm h.c.}\bigr)+O(\tau^4/d_s^3),
   ```
   ```math
   t(j)=-\frac{\tau^2}8\langle\Omega_\sigma(j+1)\vert R_j(\mathcal E_\sigma(j+1))+R_j(\mathcal E_\sigma(j-1))\vert\Omega_\sigma(j-1)\rangle,\qquad U(j)=\mathcal E_\sigma(j)+\frac{\tau^2}4\sum_\pm\langle\Omega_\sigma(j)\vert R_{j\pm1}(\mathcal E_\sigma(j))\vert\Omega_\sigma(j)\rangle,
   ```
   with $`R_y(E)=(E-h_{y,-\sigma})^{-1}`$; the sign of $`t`$ is $`(-i)^2`$ from two forward hops. All entries are real. At $`g_s=0`$, translation by $`j`$ maps $`t`$ onto the relative coordinates of Step 2, so $`t=-\tau^2J/4=-E''_{k,\sigma}(0)/8+O(\tau^4/d^3)`$ by (5.2).
3. *Position.* The body place $`\hat x`$ is diagonal in places and commutes with $`\Pi`$. In the band it is $`X=\Pi e^{-S}\hat xe^{S}\Pi=\hat j+\frac12\Pi[[\hat x,S],S]\Pi+O(\tau^4/d_s^4)`$, since $`\Pi[\hat x,S]\Pi=0`$. With $`S`$ at first order, $`\langle\langle j'\vert[[\hat x,S],S]\vert j\rangle\rangle=\sum_mS_{j'm}S_{mj}(j+j'-2x_m)`$. This vanishes for $`j'=j\pm2`$ (then $`x_m=j\pm1`$), and on the diagonal it gives $`\xi(j)=w_+(j)-w_-(j)`$, $`w_\pm(j)=\frac{\tau^2}4\langle\Omega_\sigma(j)\vert R_{j\pm1}^2\vert\Omega_\sigma(j)\rangle`$. At $`g_s=0`$, $`\xi=0`$ by $`\mathcal R`$, so $`\xi=O(\tau^2N_f|g_s|/d_s^3)`$.
4. *Acceleration.* Take the start $`\Psi=e^{S}\sum_j\phi_j\lvert j\rangle\rangle`$, $`\phi_j`$ real. Then $`a_{k,\sigma}(0)=\frac{d^2}{d\lambda^2}\langle\hat x\rangle\big|_0=-\langle[H_{\rm eff},[H_{\rm eff},X]]\rangle`$. For $`X=\hat j`$ the commutators give $`4\sum_jt(j)[U(j+1)-U(j-1)]\phi_{j+1}\phi_{j-1}-\langle[T,[T,\hat j]]\rangle`$, with $`T`$ the hop part; $`[T,[T,\hat j]]`$ vanishes for $`j`$-independent $`t`$. Inserting $`t=-E''/8`$ and $`U(j+1)-U(j-1)=2W'(j)`$ at leading order gives

```math
a_{k,\sigma}(0)=-E''_{k,\sigma}(0)\sum_j\phi_{j+1}\phi_{j-1}W'_{k,\sigma}(j)+O\Bigl(\frac{\tau^2N_f^2g_s^2}{d_s^2}\Bigr)+O\Bigl(\frac{\tau^4N_f|g_s|}{d_s^3}\Bigr),\qquad W'(j):=\tfrac12[W(j+1)-W(j-1)].\qquad\text{(5.14)}
```

   The remainders come from:
   - the source part of $`t`$ ($`|\partial_{g_s}t|\lesssim\tau^2N_f/d_s^2`$) times $`W'`$ ($`\le N_f|g_s|`$), and the $`O(g_s^2)`$ part of $`\mathcal E`$: the first;
   - the source parts of the $`\tau^2`$ diagonal, of $`t`$ inside $`[T,[T,\hat j]]`$ and of $`\xi`$, the $`O(\tau^4/d_s^3)`$ terms of $`H_{\rm eff}`$, and $`E''-2\tau^2J`$: the second.

   Every remainder carries $`g_s`$: at $`g_s=0`$ the band contract and $`X-\hat j`$ are translation invariant, so the double commutator vanishes.

So (7.7) holds for FG with $`E''`$ of (5.2) and the held weight with $`\theta=0`$, and the fall from rest inherits the level dependence of (5.10). Its remainder is set by the FG gap: in R1 the lower branch has $`d_s\simeq2n|\gamma|M_k`$, so the remainder grows as $`\gamma\to0`$, unlike the $`O(\tau^4\gamma g_s)`$ of (7.7). The code checks it against the joint evolution with a held source (`check_fall_full_grip.py`). For $`N_f=1`$, $`L=12,16`$, $`\gamma M_k=0.1,0.3`$, both branches, $`\tau/d=0.1,0.05`$ and $`g_s=10^{-3},2\cdot10^{-3}`$, it agrees to $`\le7.1\times10^{-3}`$. The deviation splits into a part $`\propto(\tau/d)^2`$ (coefficient $`\le0.53`$) and a part $`\propto g_s`$ ($`\le1.7\times10^{-3}`$ at $`g_s=10^{-3}t_f`$).

**Controls.**
- **Leading universality.** In the wider class of bodies whose motion term carries a level-dependent factor $`A\otimes f(D)`$, $`E''`$ scales with $`f(D_k)^2`$ while $`\Delta W`$ is unchanged, so universality fails at leading order.
- **(a), (c) with unequal couplings** of the $`m`$ and $`D`$ parts (M7) also fail. For FG such unequal couplings keep $`\Lambda=1`$.
- **The $`O(\gamma)`$ dependence.** In the wider class of a body with a position-dependent rest term and no field object (A10), $`E''\Delta W`$ is exactly universal.
### Step 8. Item 4: the hopping of the field

Take $`n,\gamma,M_k,\tau`$ fixed (and $`L`$, unless stated).
- **$`v`$.** (5.7) does not depend on $`t_f`$.
- **Isolation, FG.** The lower branch needs only $`\tau<\frac12\min(\Delta_b,\varepsilon^-_1)`$. For $`N_f\ge2`$, the upper branch lies below the excited lower-branch levels only if $`\varepsilon_1>2n|\gamma|M_k`$ (leading order in $`\varkappa_k`$), that is $`t_f>n|\gamma|M_k/(1-\cos\frac{2\pi}L)\simeq N_f|\gamma|M_kL/(2\pi^2)`$. In every case $`d_{k,\sigma_u}\le\varepsilon^+_1<\varepsilon_1`$. R1 needs $`t_f\gg N_f|\gamma|M_kL`$.
- **Isolation, (a) and (c).** The $`\tau=0`$ distances are $`d_{k,-}=\min(\varepsilon^{(-)}_1,2R_k)`$ and $`d_{k,+}=\min\bigl(\varepsilon^{(+)}_1,\min_E|2R_k-E|\bigr)`$. Here $`\varepsilon^{(\pm)}_1`$ is the first excitation energy of $`\hat C^{(0)}_\pm`$, and $`E`$ runs over all excitation energies of $`\hat C^{(0)}_-`$, including $`0`$.
  - At $`\gamma\to0`$ the $`E`$ are the sums $`\sum_{i=1}^j\varepsilon_{q_i}`$ of up to $`N_f`$ one-object energies. So (6.4) at $`\tau=0`$ is $`2M_k\neq\sum_{i=1}^j\varepsilon_{q_i}`$ for $`1\le j\le N_f`$, up to $`O(\gamma)`$ shifts.
  - (5.2) holds for $`\tau\lVert K\rVert<\frac12d_{k,\sigma}`$, with $`\lVert K\rVert=1`$ for (a) and $`\le1+|\gamma|N_f/2`$ for (c).
  - The denominators of (5.9) need only the one-object part, $`2M_k\neq\varepsilon_q`$, which holds for $`\varepsilon_1>2M_k`$ or $`4t_f<2M_k`$. The full condition holds for $`\varepsilon_1>2M_k`$ or $`4N_ft_f<2M_k`$. In between it fails on a discrete set of $`t_f`$, for example $`L=6`$, $`N_f\ge2`$, $`M_k=3t_f`$: $`2M_k=3t_f+3t_f`$.
  - At $`L\to\infty`$ with fixed $`n`$ the sums become dense in $`[0,4N_ft_f]`$, so $`d_{k,+}\to0`$ and the upper branch of (a), (c) leaves the regime.
- **Size of the first level dependence.** It stays at order $`\gamma^2`$ in $`\mu`$, with relative size

```math
\frac{\tau^2D_{k,\sigma}}{\sigma R_k}=\begin{cases}\sigma\gamma M_k\ell_0/t_f&\text{FG},\\ \sigma n\gamma^2M_k\ell_0/t_f\ \text{(a)},\quad \sigma n\gamma^2M_kL\,(1+O(L^{-1}))/(4t_f)\ \text{(c)},& t_f\gg M_kL^2,\\ n\gamma^2M_k^2\bigl\langle\frac{1+\cos q}{1-\cos q}\bigr\rangle_q/(2t_f^2)\simeq n\gamma^2M_k^2L/(6t_f^2)\ \text{(a), (c)},& t_f\ll M_k,\end{cases}\qquad \gamma M_k\Xi=O\Bigl(\frac{\gamma M_kL}{t_f}\Bigr).\qquad\text{(5.11)}
```

- **$`t_f`$ large.** Every level and branch dependence of items 2 and 3 vanishes as $`1/t_f`$, and the body approaches the mean-field Model D body.
- **$`t_f`$ small against $`M_k`$** (with R1 kept by a small $`\gamma`$). FG keeps (5.8). In (a) and (c) the dependence grows as $`1/t_f^2`$ and becomes branch-odd.
- **One speed for (a) and $`t_f`$.** Varying $`t_f`$ moves $`(M_0,M_1)/t_f`$ along a ray. So a two-level body has one speed at order $`\gamma^2`$ for some $`t_f`$ only if $`M_1/M_0`$ equals $`x_1/x_0`$ of a double point of (5.12), and then at an isolated $`t_f`$ with a resonance $`\varepsilon_q`$ between $`2M_0`$ and $`2M_1`$. For $`t_f`$ so large that $`2M_k<\varepsilon_1`$ for all $`k`$, or so small that $`2M_k>4t_f`$ for all $`k`$, there is none (searched range $`5\le L\le16`$).
- **$`t_f`$ small, FG (order of limits).**
  - *Upper branch.* $`d_{k,\sigma_u}\le\varepsilon^+_1<\varepsilon_1\simeq4\pi^2t_f/L^2`$. So for $`t_f\lesssim\tau L^2/(2\pi^2)`$ the criterion (5.4) fails and (5.2) is not controlled. This does not show that the exact level is not isolated; the upper branch is not followed there.
  - *Lower branch, harmonics.* As $`t_f\to0`$, $`d_{k,\sigma_l}\to|g|`$, so (5.4) holds for $`\tau<|g|/2`$. In the sector contract $`P`$ enters only through the body hops, $`e^{\mp iP}`$ each. A term $`\cos(DP)`$ of the level therefore comes from closed paths with net body displacement $`D`$:
    - $`D`$ is even, since each hop flips the branch;
    - the path has at least $`|D|`$ body hops;
    - it has at least $`N_f\,{\rm dist}(D,L\mathbb Z)`$ field hops, since every object must return to its relative place modulo $`L`$.

    The $`\tau^2`$ term ($`D=\pm2`$) gives $`J=O(t_f^{2N_f})`$.
  - *Lower branch at $`t_f=0`$.* Only windings $`D\in L\mathbb Z`$ survive. The lowest is $`|D|=L`$ (even $`L`$) or $`2L`$ (odd $`L`$) body hops in one direction. Away from the objects the cost is $`0`$, so the denominators are $`-G`$, $`G:=N_f|\gamma|M_k`$; for odd $`L`$ the path passes the objects once in the upper branch (denominator $`-2G`$). Hence

```math
E''_{k,\sigma_l}(0)\big|_{t_f=0}=\begin{cases}2(-1)^{L/2}L^2\,\dfrac{\tau^L}{2^LG^{L-1}},&L\text{ even},\\[2mm]-4L^2\,\dfrac{\tau^{2L}}{2^{2L}G^{2L-1}},&L\text{ odd},\end{cases}\qquad\times\bigl(1+O(L\tau^2/G^2)\bigr)\qquad\text{(5.13)}
```

    (code: ratio of the exact curvature to (5.13) $`0.97`$–$`0.98`$ for $`L=5,6,8`$ at $`\tau=0.1G`$, and $`0.85`$ for $`L=7`$ at $`\tau=0.2G`$).
  - *Order of limits.* The divergence of the inertia as $`t_f\to0`$ at finite cost ($`\mathrm{Cost}_{k,\sigma_l}\to-N_f|\gamma|M_k`$) holds for the coefficient of $`\tau^2`$, that is with $`\tau\to0`$ taken first. At fixed $`\tau`$ it holds while the $`\tau^2`$ term dominates every other harmonic: $`(t_f/|g|)^{2N_f}\gg(\tau/|g|)^{L-2}`$ for even $`L`$, and $`(t_f/|g|)^{N_f}\gg(\tau/|g|)^{L-3}`$ for odd $`L`$ (from $`D=\pm(L-1)`$), up to factors depending on $`L`$ and $`N_f`$. Over that range $`\mu`$ grows as $`t_f^{-2N_f}`$, and the inertia does not follow the cost.
  - At fixed $`\tau`$ and $`t_f\to0`$ on a finite ring, the exact curvature tends to (5.13), so the inertia stays finite. It diverges only as $`\tau/G\to0`$, or as $`L\to\infty`$ at fixed $`N_f`$. (Code: $`L=6`$, $`\tau=0.2|g|`$, crossover at $`t_f\approx0.01|g|`$–$`0.02|g|`$.)
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
  - $`d_{k,\sigma}\to0`$ as $`\gamma\to0`$ (both branches) and as $`L\to\infty`$ at fixed $`n,\gamma`$ (upper branch), so (5.4) fails there at every fixed $`\tau>0`$.
- **(5.5)** Weak-mark expansions of $`\varphi_g`$, $`\varepsilon_0`$, $`R_k`$, $`C^{\rm ev}_k=-n\gamma^2M_k^2\ell_0/t_f+O(\gamma^4)`$, $`a^2`$ and $`J^{\rm exc}`$, through the displayed orders, under R1 (FG) or (6.4) at $`\tau=0`$ ((a), (c)).
- **(5.6)** Item 1. Under (5.4) and R1, $`E''_{k,\sigma}(0)=\frac{\tau^2}{n\sigma\gamma M_k}[1-\gamma^2M_k^2K_L+O(N_f^2\varkappa_k^3)]+O(\tau^4/d^3_{k,\sigma})`$, with $`\gamma^2M_k^2K_L\simeq(N_f+1)\varkappa_k^2/180`$. The leading term is the curvature of a Model D body with half-gap $`n\gamma M_k`$.
- **(5.7)** Item 2 at leading order. $`\mu_{k,\sigma}=\mathrm{Cost}_{k,\sigma}/v^2+O(\gamma^2)`$ for every level and branch, with $`v=\tau`$ for (a) and FG and $`v=\tau(1+\gamma n)`$ for (c). The held cost enters; the dressed level gives the same answer. $`v`$ is the slope at $`P\to0`$ of the band $`\pm v\lvert\sin P\rvert`$ of the mean-field motion term alone. No level attains it, and it is independent of $`t_f`$, so it is not fixed by the field band.
- **(5.8)** Item 2 at order $`\gamma^2`$, FG. $`\mu_{k,\sigma}-\mathrm{Cost}_{k,\sigma}/\tau^2=n\ell_0\gamma^2M_k^2/(t_f\tau^2)+O(\gamma^3)`$. Branch differences agree through $`O(\gamma^2)`$, but level differences differ by $`n\ell_0\gamma^2(M_k^2-M_{k'}^2)/(t_f\tau^2)`$. There is no single $`v`$ at order $`\gamma^2`$ (in R1).
- **(5.9)** Item 2 at order $`\gamma^2`$, (a) and (c), non-resonant class ((6.4) at $`\tau=0`$). $`D_{k,\sigma}=\mu_{k,\sigma}-\mathrm{Cost}_{k,\sigma}/v^2`$ is given by (5.9), at leading order in $`\tau`$. It is checked against the exact $`\tau^2`$ coefficient at $`N_f=1`$.
- **(5.12)** Item 2, one speed at order $`\gamma^2`$, (a) and (c), non-resonant class, leading order in $`\tau`$. $`\tau^2D_{k,\sigma}=n\gamma^2t_f\mathbb F(\sigma M_k/t_f)+O(\gamma^3)`$. One $`v`$ exists at order $`\gamma^2`$ iff the points $`(\pm M_k/t_f,\mathbb F(\pm M_k/t_f))`$ of all levels lie on one line; this depends only on $`L`$ and $`M_k/t_f`$.
  - (c): never, for any member of the class, since the branch average is $`\propto M_k^2`$ with a positive coefficient and Model D has $`N\ge2`$ distinct $`M_k`$.
  - (a): for two levels the condition is that $`(M_0,M_1)/t_f`$ is a double point of the chord curve $`x\mapsto(s(x),i(x))`$. In the searched range $`5\le L\le16`$ such points exist for every $`L`$; they are isolated, and each one found straddles a one-object resonance $`2M_k=\varepsilon_q`$. The search finds no body with $`N\ge3`$ levels and one $`v`$. So for $`5\le L\le16`$, as far as the numerical search is complete, one $`v`$ exists at order $`\gamma^2`$ only for two-level bodies at these isolated ratios.
- **(5.10)** Item 3, at first order in $`g_s`$, for $`g_s\neq0`$ and places $`x,x'`$ that are not reflection-equivalent with respect to the source ($`F\neq0`$). $`E''_{k,\sigma}(0)\Delta W_{k,\sigma}=\tau^2F\Lambda[1+\sigma\gamma M_k\Xi+O(\gamma^2)]`$, with $`\Lambda=1`$ (FG), $`n\gamma(1\mp\gamma n)`$ ((a), (c)), and $`\Xi=-(\rho^2+\rho'^2-1)/(3Lt_f)`$, $`\rho=r-L/2`$, $`\rho'=r'-L/2`$, $`r=x_s-x`$ and $`r'=x_s-x'`$ taken in $`\{0,\dots,L-1\}`$.
  - The product is the same for all levels and both branches at leading order.
  - If $`\Xi\neq0`$, the first level and branch dependence is $`\sigma\gamma M_k\Xi`$ at relative order $`\gamma`$, of size $`O(\varkappa_k)`$, with the same $`\Xi`$ for the three couplings.
  - $`\Xi=0`$ iff $`L`$ is even and the places are the antipode of the source and a neighbour of it.
  - For reflection-equivalent places $`\Delta W_{k,\sigma}=0`$ exactly.
- **(5.15)** Item 3 at relative order $`\gamma^2`$, same conditions: the display, with $`\Lambda=1`$, $`n\gamma/(1+\gamma n)`$, $`n\gamma(1+\gamma n)`$. Where $`\Xi=0`$, the first dependence is:
  - FG: the level dependence $`(\Psi_0-K_L)\gamma^2(M_k^2-M_{k'}^2)`$, nonzero for $`N_f=1`$, $`6\le L\le16`$ even;
  - (c): the branch dependence $`-\sigma\gamma^2M_kn(L-2)(L-4)/(6Lt_f)\neq0`$;
  - (a): the branch dependence displayed in Step 7, nonzero unless its average vanishes.
- **(5.14)** FG form of (7.7), first order in $`g_s`$, under $`\tau<d_s/2`$, $`N_f|g_s|\le d_{k,\sigma}/4`$, $`d_s\ge d_{k,\sigma}-2N_f|g_s|`$: $`a_{k,\sigma}(0)=-E''_{k,\sigma}(0)\sum_j\phi_{j+1}\phi_{j-1}W'_{k,\sigma}(j)+O(\tau^2N_f^2g_s^2/d_s^2)+O(\tau^4N_f|g_s|/d_s^3)`$, for a start with real envelope in the dressed band, $`W'`$ the central difference of the held weight ($`\theta=0`$). The fall from rest thus inherits (5.10).
- **(5.11)** Item 4.
  - $`v`$ is independent of $`t_f`$.
  - For $`N_f\ge2`$, the FG upper level lies below the excited lower-branch levels only for $`t_f>n|\gamma|M_k/(1-\cos\frac{2\pi}L)`$ (leading order in $`\varkappa_k`$).
  - For (a), (c) the upper-branch isolation is (6.4) with sums of up to $`N_f`$ one-object energies. At leading order in $`\gamma`$ it holds for $`\varepsilon_1>2M_k`$ or $`4N_ft_f<2M_k`$, and in between it fails on a discrete set of $`t_f`$.
  - The first level dependence stays at order $`\gamma^2`$, with the relative sizes displayed. It vanishes as $`1/t_f`$ for large $`t_f`$, and in (a) and (c) it grows as $`1/t_f^2`$ for $`t_f\ll M_k`$.
  - For $`t_f\lesssim\tau L^2/(2\pi^2)`$ the criterion (5.4) fails for the FG upper branch, which is not followed there.
  - FG lower branch, $`\tau<|g|/2`$: the $`\tau^2`$ coefficient of $`E''`$ is $`O(t_f^{2N_f})`$. So with $`\tau\to0`$ first, $`\mu\to\infty`$ as $`t_f\to0`$ at finite cost. At fixed $`\tau`$ this holds only while $`(t_f/|g|)^{2N_f}\gg(\tau/|g|)^{L-2}`$ ($`L`$ even), resp. $`(t_f/|g|)^{N_f}\gg(\tau/|g|)^{L-3}`$ ($`L`$ odd), up to factors depending on $`L`$ and $`N_f`$.
  - At fixed $`n`$ and $`\gamma`$, (5.6)–(5.10) have no $`L\to\infty`$ limit (R1 fails); (5.2) and (5.3) still hold for the lower branch.
- **(5.13)** FG lower branch at $`t_f=0`$, $`\tau<|\gamma|M_k/2`$, $`G=N_f|\gamma|M_k`$: the curvature is the winding term displayed, of order $`\tau^L`$ ($`L`$ even) or $`\tau^{2L}`$ ($`L`$ odd). So at fixed $`\tau`$ on a finite ring the exact inertia stays finite as $`t_f\to0`$.

## Consistency checks

1. **$`\gamma\to0`$ and mean field for (a), (c) against (6.10).** With $`a=1+\theta_c\gamma n`$, $`J^{\rm exc}=0`$ and $`R_k=M_k(1+\gamma n)`$, (5.2)–(5.3) give $`\sigma\tau^2/(M_k(1+\gamma n))`$ for (a) and $`\sigma\tau^2(1+\gamma n)/M_k`$ for (c). These are the mean-field parts of (6.10), and both reduce to $`\sigma\tau^2/M_k`$ at $`\gamma=0`$. Passed.
2. **FG at mean field against a body with a rest term.** The leading term of (5.6), $`\tau^2/(\sigma n\gamma M_k)`$, is the curvature at $`P=0`$ of $`\pm(\tilde M^2+\tau^2\sin^2P)^{1/2}`$ with $`\tilde M=n\gamma M_k`$. That body's held cost $`\sigma\tilde M`$ equals the leading FG cost. Passed.
3. **Dimensions.** $`\tau,t_f,M_k,g_s`$, costs and $`E''`$ are contract units, and $`\gamma,n,P,\ell,F`$ are dimensionless. $`K_L\propto t_f^{-2}`$, and $`\tau^2D/(\sigma R)`$ and $`\gamma M_k\Xi`$ are dimensionless. $`E''\Delta W=\tau^2F\Lambda`$ has units of contract squared. Passed.

## Open issues

- FG beyond R1 (strong mark), including the lower branch as $`L\to\infty`$ at fixed $`n`$: (5.2) holds there, but items 2 and 3 are not evaluated.
- (5.9) and (5.12) are derived at $`\tau\to0`$ only; the finite-$`\tau`$ bracket of (6.12) is not evaluated.
- The solutions of (5.12) for (a) are determined numerically, for $`5\le L\le16`$ only, by a root search whose completeness is not proven (two grids differ by one point at $`L=15`$). For $`L>16`$ their existence and the absence of solutions with $`N\ge3`$ levels are not shown.
- The FG upper branch for $`t_f\lesssim\tau L^2/(2\pi^2)`$, where (5.4) fails, is not followed.
- The prefactors of the order-of-limits conditions at small $`t_f`$ are not evaluated.
- (5.14) is checked at $`N_f=1`$ only; its remainders are bounds, not leading terms.
- $`N_f\ge2`$ and the FG upper branch beyond $`2n|\gamma|M_k=\varepsilon_1`$ are not checked numerically.
- The $`O(\gamma)`$ term of (5.10) has a control only in a wider class.
- The relation of $`v=\tau`$ to the maximal speed of 03-ilang-space is not quoted here and not used.

## Code

All scripts are checks. They run with $`N_f=1`$, and their outputs are in `code/v2/output/`.

`code/v2/check_full_grip.py` (copied from v1, unchanged) does the following:
- builds the sector contract (5.1) for FG with $`N_f=1`$, and verifies it against the full contract at $`L=6`$ (eigenvalues agree to $`4\times10^{-15}`$);
- for $`L=8,13`$, $`t_f=1`$, $`M_k\in\{1,1.4\}`$ ($`m=1`$, $`N=2`$, $`\lambda_0=5\pi/2`$), $`\gamma\in\{0.01,0.02,0.3\}`$ and both branches, computes the exact curvature of the dressed level at $`P=0`$, by second-order perturbation in $`P`$ from a full diagonalization, at $`\tau=10^{-5}`$ and $`\tau=d/5`$, together with the exact isolation distance $`d`$;
- compares it with (5.2) and (5.6);
- compares $`\tau^2\mu-\mathrm{Cost}`$, its level and branch differences, and $`E''\Delta W/(\tau^2F)`$ with (5.8) and (5.10), and $`\Delta W`$ with (3.13).

Output: `code/v2/output/check_full_grip.txt`. Results:
- (5.2): agreement to $`\le1.4\times10^{-12}`$ at $`\tau=10^{-5}`$ ($`\le5\times10^{-10}`$ at $`\gamma=0.3`$, $`\varkappa_k\le5.5`$); at $`\tau=d/5`$ to $`\le9\times10^{-9}`$ ($`\gamma\le0.02`$) and $`\le1.1\times10^{-3}`$ ($`\gamma=0.3`$).
- (5.6): agreement to $`\le1.2\times10^{-5}`$ for $`N_f\varkappa_k\le0.36`$, with deviation $`\propto\gamma^3`$; up to $`0.1`$ at $`\gamma=0.3`$ (outside R1).
- (5.8): $`\tau^2\mu-\mathrm{Cost}`$ within $`2.4\%`$ (the deviation is branch-odd, $`O(\gamma^3)`$); the level difference $`k=1`$ minus $`k=0`$ within $`3.2\%`$; $`\tau^2(\mu_+-\mu_-)`$ equals $`\mathrm{Cost}_+-\mathrm{Cost}_-`$ to $`\le7\times10^{-4}`$ of the latter.
- (5.10): the branch-odd part of $`E''\Delta W/(\tau^2F)-1`$ equals $`\gamma M_k\Xi`$ to $`\le0.2\%`$ ($`\Xi=-0.167`$ for $`L=8`$, $`-0.808`$ for $`L=13`$, places $`r=2,3`$); the branch-even part is $`O(\gamma^2)`$; (3.13) reproduces $`\Delta W`$ to $`O(C^3)`$.

`code/v2/check_inertia_ac.py` → `check_inertia_ac.txt`:
- (5.9) for (a), (c) at $`L=7,13`$, $`M_k\in\{1,1.4\}`$, $`\gamma\in\{0.01,0.02\}`$, both branches, against $`\tau^2D`$ from the exact $`\tau^2`$ coefficient $`J`$ of (5.2). $`(\text{exact}-(5.9))/\gamma^3`$ is the same at both $`\gamma`$, between $`-1.32`$ and $`-0.03`$. The exact curvature at $`\tau=10^{-4}`$ equals $`2\tau^2J`$ to $`\le2\times10^{-12}`$.
- (5.12): the (c) branch-average coefficient for $`5\le L\le16`$ (all positive).
- (5.12): all double points of the (a) chord curve for $`5\le L\le16`$ (root search in $`(u_0+u_1,u_0u_1)`$ on two grids, which agree except one point at $`L=15`$). It reports the resonance between the two ratios and that no ratio is shared.
- At the $`L=7`$ double point the residual of the four points from a line, divided by $`\gamma^2`$, is $`1.0,2.1,4.2\times10^{-3}`$ for $`\gamma=0.002,0.004,0.008`$, against $`0.106`$ at $`(M_0,M_1)=(1,1.4)`$.

`code/v2/check_small_hopping.py` → `check_small_hopping.txt`:
- (5.13) at $`t_f=0`$ for $`L=5,\dots,8`$: the ratio of the exact curvature to (5.13) tends to 1 with deviation $`\approx(0.3`$–$`0.6)L\tau^2/G^2`$.
- The crossover at $`L=6`$, $`\tau=0.2G`$: the exact curvature follows $`2\tau^2J`$ within $`13\%`$ (the $`O(\tau^2/d^2)`$ correction) for $`t_f\ge0.05G`$ and tends to the winding value as $`t_f\to0`$; $`2\tau^2J=-8\tau^2t_f^2`$ at small $`t_f`$.

`code/v2/check_fall_full_grip.py` → `check_fall_full_grip.txt`: (5.14) from the joint description of body, branch and field object with a held source. The start is the dressed band state (direct rotation), and $`a(0)`$ comes from the double commutator and from the joint evolution $`e^{-iC\lambda}`$ (the two agree to all digits). Parameters and agreement are given in Step 7.

`code/v2/check_weight_next_order.py` → `check_weight_next_order.txt`:
- $`F=0`$ exactly on the reflection-equivalent pairs for $`5\le L\le16`$.
- $`\Xi`$ equals its closed form to $`\le8\times10^{-15}`$, and $`\Xi=0`$ pairs occur as stated.
- $`\Psi_0-K_L`$ at those pairs.
- (5.15) at $`L=8`$, $`(r,r')=(3,4)`$ for FG ($`M_k=1,1.4`$) and for (a), (c) ($`M_k=1.2,1.6`$, non-resonant): $`(\text{exact}-\text{prediction})/\gamma^3`$ is the same at $`\gamma=0.01,0.02`$.

## Methods used

- sector decomposition by joint translation; reflection symmetry
- Rayleigh–Schrödinger perturbation theory; Kato's isolation criterion
- Schrieffer–Wolff (direct rotation) effective band contract; Weyl's inequality
- spectral decomposition of resolvents; Franck–Condon overlaps of product states
- path (hopping) expansion in $`\tau`$ and $`t_f`$; winding paths on the ring
- Perron–Frobenius; secular equation of a rank-one perturbation
- Fourier sums on the ring; discrete Poisson equation for $`\ell^{(2)}`$
- double points of a rational plane curve (numerical root search)
- exact diagonalization; second-order perturbation in $`P`$; joint evolution (numerical checks)
