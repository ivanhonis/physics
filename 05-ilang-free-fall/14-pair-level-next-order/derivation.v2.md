# Bound level of the pair at the next order in the regime R

- **Subproject:** 05-ilang-free-fall
- **Package:** 14-pair-level-next-order
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-18

## Changes from previous version

- Step 7: (14.12) is carried to $`u^4`$ for $`\nu\mathcal C`$ and the relative correction of $`\mathfrak m_b`$, and to $`u^5`$ for $`\beta_i\Xi_i`$. The new (14.13) gives the first non-vanishing term on every data set with $`w_{11}<0`$, using the cancellation sets $`\mathcal S_k`$, $`\mathcal X_k`$ (I1).
- Setup (class sentence) and Result: (14.12) is restated and (14.13) is added (I1).
- Consistency check 2: restricted to $`j(P)>0`$; the flat-band point $`a_1=a_2`$, $`P\equiv\pi/2\pmod\pi`$ is excluded (I2).
- Open issues: the item on vanishing coefficients of (14.12) is removed; the item on the ordered limit now covers (14.13) as well (I1).
- Code, `code/v2/check_pair_level.py`: the closed forms of (14.7)–(14.10) are now one function shared by all parts. Part C is replaced by an exact series check (sympy) and a 50-digit test of (14.13) on five data sets, including single and double cancellations (I1). Parts A and B are unchanged, and every number cited from them is the same in the v2 run.

## Response to verification

- I1: Accepted and fixed in Step 7. Each expansion is now carried until its coefficient is shown to be nonzero on the set where the earlier coefficients vanish:
  - $`\nu\mathcal C`$ and the relative correction of $`\mathfrak m_b`$: to $`u^4`$. On $`\gamma_c=2\gamma_m`$, $`\gamma_s=3\gamma_m`$ the coefficients are $`\frac92\nu\gamma_m`$ and $`-\frac{9\gamma_m}{8a}`$, which confirms the verifier's value $`\mathcal C=\frac92\gamma_mu^4`$.
  - $`\beta_i\Xi_i`$: to $`u^5`$. $`X_5<0`$ on the whole set $`X_3=0`$, and that set contains the doubly cancelling ratio $`t_*`$.

  The leading terms are collected in (14.13). Code Part C checks them on both doubly cancelling sets.
- I2: Accepted and fixed in Consistency check 2. The check is now stated for $`j(P)>0`$, which contains a neighbourhood of $`P=0`$. It does not apply at $`a_1=a_2`$, $`P\equiv\pi/2\pmod\pi`$, where the leading band is flat.

## Setup and assumptions

**Inputs** (11-bound-pair@v3, as quoted in question.md): the fibre contract (11.1), $`H(P)=A_1+A_2+M_1\sigma^{(1)}_3+M_2\sigma^{(2)}_3+U`$ on $`\psi(r)\in\mathbb C^2\otimes\mathbb C^2`$; the identities (11.5); the reduction of Step 7, $`H_{\rm eff}=M_1+M_2+\Pi U\Pi+\Pi\bigl(\frac{A_1^2}{2M_1}+\frac{A_2^2}{2M_2}\bigr)\Pi+O(\epsilon^4)`$, and its form (11.11); the level (11.12), the eigenvector (11.13), the values (11.14), the relation (11.16), and the statements of Step 7 (odd orders of $`E_b`$ vanish; $`w_{22}`$ enters $`E_b`$ at order $`\epsilon^6`$, $`w_{12},w_{21}`$ never). Notation of question.md: $`a_i,a,j(P),\alpha(P),J(P),w=w_{11},\varsigma,u,\Lambda,\mathfrak m_i,\mathfrak m_b,\omega_i`$, $`p_1+p_2=P`$.

**Notation of this package.**
- $`E_0:=M_1+M_2`$; $`\Pi`$ projects on the branch $`\lvert11\rangle`$ (all $`r`$); $`\Pi_0:=\lvert0\rangle\langle0\rvert`$ on $`r`$.
- $`T_1:=\frac{i\tau_1}{2}(e^{i\eta P}S^\dagger-e^{-i\eta P}S)`$, $`T_2:=\frac{i\tau_2}{2}(e^{i(1-\eta)P}S-e^{-i(1-\eta)P}S^\dagger)`$, so $`A_i=\sigma^{(i)}_1T_i`$. The $`T_i`$ are self-adjoint, commute (functions of $`S`$), $`\lVert T_i\rVert\le\tau_i`$; on $`e^{iqr}`$ they act as $`-\tau_i\sin p_i`$, $`p_1=q+\eta P`$, $`p_2=(1-\eta)P-q`$.
- $`e_1:=e^{2i\eta P}`$, $`e_2:=e^{-2i(1-\eta)P}`$, $`D_i:=e_iS^{\dagger2}`$ (unitary, $`(S^{\dagger2}\psi)(r)=\psi(r+2)`$); then $`T_i^2=\frac{\tau_i^2}{4}(2-D_i-D_i^\dagger)`$.
- $`\beta_i:=a_i/M_i=\tau_i^2/(4M_i^2)`$, $`\beta:=\beta_1+\beta_2`$, $`\nu:=a_1a_2/a^2\in(0,\frac14]`$, $`\bar s:=\sqrt{1+u^2}`$, $`s(P):=\sqrt{w^2+j(P)^2}`$ (so $`s(0)=a\bar s`$), $`\rho(P)`$ as in (11.13).
- $`\gamma_s:=\frac{a_1^2}{M_1}+\frac{a_2^2}{M_2}`$, $`\gamma_c:=\frac{a_2^2}{M_1}+\frac{a_1^2}{M_2}`$, $`\gamma_m:=a_1a_2\bigl(\frac1{M_1}+\frac1{M_2}\bigr)`$; note $`a\beta=\gamma_s+\gamma_m`$.
- Orders in $`\mathsf R`$: $`a_i,w,\beta_i=O(\epsilon^2)`$; $`\gamma_s,\gamma_c,\gamma_m=O(\epsilon^4)`$; $`u,\bar s,\nu`$ fixed.

**Assumptions.**
- (S1) The setting, the binding, the regime $`\mathsf R`$ and the level are those of question.md (M8). The eigenvector $`\psi_P`$ of the level is a distinguished state (M9, A11). Equal parameters of the two types are never assumed (M7).
- (S2) Isolation: $`\lVert A+U\rVert\le\epsilon(\hat\tau_1+\hat\tau_2)+\epsilon^2\max\lvert\hat w_{s_1s_2}\rvert`$ is small against $`2\min(M_1,M_2)`$, the distance from $`E_0`$ to the other branch values of $`H_0`$. The Schrieffer–Wolff (SW) series then converges and is analytic in $`\epsilon`$, $`P`$ and $`M_i`$.
- (S3) Hatted data fixed, hence $`u\in(0,\infty)`$ fixed; the constants in $`O(\epsilon^k)`$ depend on them and are not claimed uniform in $`u`$.
- **Class:** every diagonal on-site binding with $`\hat w_{11}\neq0`$, both signs, all hatted data. (14.1)–(14.10) are derived for every member and (14.12)–(14.13) for every member with $`\hat w_{11}<0`$, so the class contains no control for them; the control is item 3, (14.11).

## Derivation

### Step 1. A conserved parity

Each $`A_i`$ shifts $`r`$ by $`\pm1`$ and flips the branch of body $`i`$; $`H_0`$ and $`U`$ are diagonal in $`r`$ and in the branches. Hence
```math
[H(P),\Theta]=0,\qquad \Theta:=(-1)^{\hat r}\,\sigma^{(1)}_3\sigma^{(2)}_3 .
\qquad\text{(14.1)}
```
On the coefficient of $`\lvert11\rangle`$, $`\Theta=(-1)^r`$. In the sector $`\Theta=+1`$ the binding acts at $`r=0`$ only on $`\lvert11\rangle`$ (by $`w_{11}`$) and $`\lvert22\rangle`$ (by $`w_{22}`$); $`\lvert12\rangle,\lvert21\rangle`$ at $`r=0`$ lie in $`\Theta=-1`$. The vector (11.13) lives on even $`r`$; the level is simple and $`\Theta`$ is conserved, so the exact $`\psi_P`$ lies in $`\Theta=+1`$, and $`w_{12},w_{21}`$ enter $`E_b`$ at no order.

### Step 2. Effective contract through order $`\epsilon^4`$ (item 1)

Write $`H(P)=H_0+V`$, $`H_0=M_1\sigma^{(1)}_3+M_2\sigma^{(2)}_3`$, $`V=A+U`$, $`A=A_1+A_2=O(\epsilon)`$, $`U=O(\epsilon^2)`$, and $`R:=(1-\Pi)(E_0-H_0)^{-1}(1-\Pi)`$; $`R`$ multiplies the branches $`\lvert21\rangle,\lvert12\rangle,\lvert22\rangle`$ by $`\frac1{2M_1},\frac1{2M_2},\frac1{2(M_1+M_2)}`$. Two facts select the terms: (i) $`\Pi A\Pi=0`$, $`\Pi U(1-\Pi)=0`$, $`\Pi U\Pi=w\Pi_0`$; (ii) a product between $`\Pi`$ and $`\Pi`$ with an odd number of factors $`A`$ vanishes (each $`A_i`$ flips one branch).

The canonical SW operator of the isolated group at $`E_0`$ is, to fourth order in $`V`$ (standard): $`E_0+\Pi V\Pi+\Pi VRV\Pi+\Pi VRVRV\Pi-\frac12\{\Pi VR^2V\Pi,\Pi V\Pi\}+\Pi VRVRVRV\Pi-\frac12\{\Pi VR^2V\Pi,\Pi VRV\Pi\}+Y+O(\lVert V\rVert^5)`$, where $`Y`$ collects the fourth-order terms containing the factor $`\Pi V\Pi`$. By (i)–(ii), $`\Pi VRV\Pi=\Pi ARA\Pi=O(\epsilon^2)`$, and a chain of three $`V`$ between projectors reduces to terms $`A\,U\,A`$ of order $`\epsilon^4`$. Every term of $`Y`$ is $`\Pi V\Pi=O(\epsilon^2)`$ times either a chain of three $`V`$ or further factors $`\Pi V\Pi`$ and a chain of two $`V`$, hence $`Y=O(\epsilon^6)`$. In the other fourth-order terms only the parts with four $`A`$ are of order $`\epsilon^4`$, and the order-$`\epsilon^5`$ part of the fifth-order terms has five factors $`A`$ and vanishes. With $`K:=\Pi AR^2A\Pi`$:
```math
H_{\rm eff}=E_0+w\Pi_0+\Pi ARA\Pi+\Pi ARURA\Pi+\Pi ARARARA\Pi-\tfrac12\bigl\{K,\;w\Pi_0+\Pi ARA\Pi\bigr\}+O(\epsilon^6)
\qquad\text{(14.2)}
```
in norm, uniformly in $`P`$ (since $`\lVert T_i\rVert\le\tau_i`$), by a unitary that differs from $`\mathbb 1`$ by $`O(\epsilon)`$.

Path sums on the coefficient of $`\lvert11\rangle`$:
- $`\Pi ARA\Pi=\frac{T_1^2}{2M_1}+\frac{T_2^2}{2M_2}`$ and $`K=\frac{T_1^2}{4M_1^2}+\frac{T_2^2}{4M_2^2}`$ (one flip and back).
- $`\Pi ARURA\Pi=\frac{w_{21}}{4M_1^2}T_1\Pi_0T_1+\frac{w_{12}}{4M_2^2}T_2\Pi_0T_2`$: $`U`$ acts on $`\lvert21\rangle`$, $`\lvert12\rangle`$ as $`w_{21}\Pi_0`$, $`w_{12}\Pi_0`$, and the way back flips the same branch.
- $`\Pi ARARARA\Pi`$: the middle state is $`\lvert22\rangle`$; the paths $`11{\to}21{\to}22{\to}21{\to}11`$, $`11{\to}21{\to}22{\to}12{\to}11`$, $`11{\to}12{\to}22{\to}21{\to}11`$, $`11{\to}12{\to}22{\to}12{\to}11`$ give $`\frac{T_1^2T_2^2}{8(M_1+M_2)}\bigl(\frac1{M_1}+\frac1{M_2}\bigr)^2=\frac{(M_1+M_2)T_1^2T_2^2}{8M_1^2M_2^2}`$.
- $`-\frac12\{K,\Pi ARA\Pi\}=-\frac{T_1^4}{8M_1^3}-\frac{T_2^4}{8M_2^3}-\frac{(M_1+M_2)T_1^2T_2^2}{8M_1^2M_2^2}`$.

The mixed terms cancel:
```math
H_{\rm eff}=E_0+\sum_{i=1,2}\Bigl(\frac{T_i^2}{2M_i}-\frac{T_i^4}{8M_i^3}\Bigr)+w\Pi_0-\frac w2\{K,\Pi_0\}+\frac{w_{21}}{4M_1^2}T_1\Pi_0T_1+\frac{w_{12}}{4M_2^2}T_2\Pi_0T_2+O(\epsilon^6).
\qquad\text{(14.3)}
```
On $`e^{iqr}`$ the sum is $`\omega_1(p_1)+\omega_2(p_2)-E_0`$ through order $`\tau^4`$. With $`T_i^2=\frac{\tau_i^2}4(2-D_i-D_i^\dagger)`$, $`\frac{\tau_i^4}{128M_i^3}=\frac{a_i\beta_i}8`$, $`T_1\lvert0\rangle=\frac{i\tau_1}2(e^{i\eta P}\lvert{-1}\rangle-e^{-i\eta P}\lvert1\rangle)`$ and $`T_2\lvert0\rangle=\frac{i\tau_2}2(e^{i(1-\eta)P}\lvert1\rangle-e^{-i(1-\eta)P}\lvert{-1}\rangle)`$:
```math
\begin{aligned}
(H_{\rm eff}\psi)(r)={}&\Bigl(E_0+\textstyle\sum_i a_i\bigl(1-\frac34\beta_i\bigr)\Bigr)\psi(r)-\frac12\bigl[J_2\,\psi(r+2)+J_2^*\,\psi(r-2)\bigr]-\frac18\bigl[J_4\,\psi(r+4)+J_4^*\,\psi(r-4)\bigr]\\
&+\delta_{r,0}\Bigl[w\bigl(1-\tfrac\beta2\bigr)\psi(0)+\tfrac w8\bigl(J_\beta\,\psi(2)+J_\beta^*\,\psi(-2)\bigr)\Bigr]+\tfrac w8\bigl(\delta_{r,-2}J_\beta+\delta_{r,2}J_\beta^*\bigr)\psi(0)\\
&+\tfrac\Omega4\bigl(\delta_{r,1}+\delta_{r,-1}\bigr)\psi(r)-\tfrac14\bigl(\delta_{r,-1}L\,\psi(1)+\delta_{r,1}L^*\psi(-1)\bigr)+O(\epsilon^6),\\
J_2={}&\textstyle\sum_ia_i(1-\beta_i)e_i,\quad J_4=\sum_ia_i\beta_ie_i^2,\quad J_\beta=\sum_i\beta_ie_i,\quad \Omega=\beta_1w_{21}+\beta_2w_{12},\quad L=\beta_1w_{21}e_1+\beta_2w_{12}e_2 .
\end{aligned}
\qquad\text{(14.4)}
```
Ranges: the first line couples $`r`$ to $`r,r\pm2,r\pm4`$ for all $`r`$; the $`w_{11}`$ terms act at $`r=0`$ and between $`0`$ and $`\pm2`$; the $`w_{12},w_{21}`$ terms act at $`r=\pm1`$ and between $`-1`$ and $`1`$. Even and odd $`r`$ stay uncoupled, by (14.1). Through order $`\epsilon^2`$, (14.4) is (11.11) ($`J_2=J+O(\epsilon^4)`$). At order $`\epsilon^4`$ enter $`w_{11}`$ (also at order $`\epsilon^2`$), $`w_{12}`$ and $`w_{21}`$ (odd $`r`$ only); $`w_{22}`$ does not, since $`\lvert22\rangle`$ needs two flips each way. The code (Part B) confirms (14.4) on a ring.

### Step 3. The level for every $`P`$ (item 2a)

On even $`r`$, (14.4) is $`E_0+h_2+h_4+O(\epsilon^6)`$, with $`h_2`$ the operator (11.11) minus $`E_0`$ and $`h_4:=-\sum_iT_i^4/(8M_i^3)-\frac w2\{K,\Pi_0\}=O(\epsilon^4)`$. With $`r=2n`$, the vector (11.13), $`\psi_P(2n)=\mathcal N_Pe^{-i\alpha n}\rho^{\lvert n\rvert}`$, is an exact normalized eigenvector of $`E_0+h_2`$ with eigenvalue $`E_0+a+\varsigma s`$: substitution gives $`-\frac j2(\rho+\rho^{-1})=\varsigma s`$ for $`n\ne0`$ and $`w-j\rho=\varsigma s`$ at $`n=0`$. Its distance from the continuous spectrum $`[a-j,a+j]`$ of $`h_2`$ is $`s-j=w^2/(s+j)`$, of order $`\epsilon^2`$ at fixed $`u`$. Perturbation theory for an isolated simple eigenvalue, analytic by (S2), gives $`E_b(P)=E_0+a+\varsigma s+\langle\psi_P\vert h_4\vert\psi_P\rangle+O(\epsilon^6)`$, with a remainder analytic in $`P`$ and $`M_i`$, so that its derivatives in $`P`$ and $`M_i`$ are $`O(\epsilon^6)`$ too.

Moments of (11.13). With $`\mathcal N_P^2=\lvert w\rvert/s`$, $`\rho^2=\frac{s-\lvert w\rvert}{s+\lvert w\rvert}`$, and the sum split into $`n\ge0`$, $`n\le-m`$ and the $`m-1`$ terms between, for $`m\ge0`$:
```math
\langle\psi_P\vert S^{\dagger2m}\vert\psi_P\rangle=e^{-im\alpha}c_m,\qquad c_m=\mathcal N_P^2\sum_{n\in\mathbb Z}\rho^{\lvert n\rvert+\lvert n+m\rvert}=\rho^m\Bigl(1+m\frac{\lvert w\rvert}{s}\Bigr),
\qquad\text{(14.5)}
```
so $`c_1=-\varsigma j/s`$ and $`c_2=\frac{j^2(s+2\lvert w\rvert)}{s(s+\lvert w\rvert)^2}`$. Define $`\theta_i`$ by $`je^{i\theta_1}=a_1+a_2e^{2iP}`$, $`je^{i\theta_2}=a_2+a_1e^{-2iP}`$; since $`e^{-i\alpha}=J^*/j`$, $`e_ie^{-i\alpha}=e^{i\theta_i}`$ and $`\langle D_i^m\rangle=e^{im\theta_i}c_m`$. Put $`\kappa_i:=j\cos\theta_i`$, $`\lambda_i:=j^2\cos2\theta_i`$: $`\kappa_1=a_1+a_2\cos2P`$, $`\lambda_1=a_1^2+2a_1a_2\cos2P+a_2^2\cos4P`$, and $`\kappa_2,\lambda_2`$ by $`a_1\leftrightarrow a_2`$.

Now $`\frac{T_i^4}{8M_i^3}=\frac{a_i\beta_i}8(6-4D_i-4D_i^\dagger+D_i^2+D_i^{\dagger2})`$ has expectation $`\frac{a_i\beta_i}8(6-8c_1\cos\theta_i+2c_2\cos2\theta_i)`$. With $`K=\frac\beta2-\frac14\sum_i\beta_i(D_i+D_i^\dagger)`$, $`-\frac w2\langle\{K,\Pi_0\}\rangle=-w\,{\rm Re}\bigl[\psi_P(0)^*(K\psi_P)(0)\bigr]=-\frac{\varsigma w^2}{2s}(\beta-\rho g)`$, $`g:=\beta_1\cos\theta_1+\beta_2\cos\theta_2`$. With $`\varsigma\rho=-j/(s+\lvert w\rvert)`$:
```math
E_b(P)=E_0+a+\varsigma s-\sum_{i=1,2}\frac{a_i^2}{8M_i}\Bigl[6+\frac{8\varsigma\kappa_i}{s}+\frac{2(s+2\lvert w\rvert)\lambda_i}{s(s+\lvert w\rvert)^2}\Bigr]-\frac{w^2}{2s}\Bigl[\varsigma\beta+\frac{\beta_1\kappa_1+\beta_2\kappa_2}{s+\lvert w\rvert}\Bigr]+O(\epsilon^6).
\qquad\text{(14.6)}
```
It is even in $`P`$ and independent of $`\eta`$.

### Step 4. Binding cost and rest terms (item 2b)

At $`P=0`$: $`j=a`$, $`\kappa_i=a`$, $`\lambda_i=a^2`$, $`s=a\bar s`$, and $`\frac{\bar s+2u}{\bar s(\bar s+u)^2}=1-2u^2+\frac{2u^3}{\bar s}`$ (use $`(\bar s+u)^{-1}=\bar s-u`$). Then (14.6) gives
```math
E_{\rm bind}=a(1+\varsigma\bar s)+\mathcal E_4+O(\epsilon^6),\qquad \mathcal E_4=-\frac{\gamma_s}2\,\phi_A-\frac{\gamma_s+\gamma_m}2\,\phi_B,\qquad \phi_A=2-u^2+\frac{2\varsigma+u^3}{\bar s},\quad \phi_B=\frac{u^2(\varsigma+\bar s-u)}{\bar s}.
\qquad\text{(14.7)}
```
By (11.5), $`\langle\sigma^{(i)}_3\rangle_0=1+\partial E_{\rm bind}/\partial M_i`$ at fixed $`\tau_i`$ and $`w_{s_1s_2}`$. With $`\partial_{M_i}a=-\beta_i`$, $`\partial_{M_i}u=u\beta_i/a`$, $`\partial_{M_i}\gamma_s=-3\beta_i^2`$ and $`\partial_{M_i}(a\beta)=-\beta_i\beta-2a\beta_i/M_i`$, the leading term gives $`-\beta_i\Lambda`$ (as in (11.14)), and
```math
\langle\sigma^{(i)}_3\rangle_0=1-\beta_i\Lambda+\beta_i\,\Xi_i+O(\epsilon^6),\qquad \Xi_i=\frac32\beta_i\phi_A-\frac{\gamma_s}{2a}\,u\phi_A'+\frac12\Bigl(\beta+\frac{2a}{M_i}\Bigr)\phi_B-\frac\beta2\,u\phi_B',
\qquad\text{(14.8)}
```
with $`u\phi_A'=-2u^2+\frac{3u^3}{\bar s}-\frac{u^2(2\varsigma+u^3)}{\bar s^3}`$ and $`u\phi_B'=2u^2-\frac{3u^3}{\bar s}+\frac{\varsigma u^2(2+u^2)+u^5}{\bar s^3}`$.

### Step 5. Curvature and curvature inertia (items 2b, 2c)

The order-$`\epsilon^4`$ part of (14.6) is $`-\sum_i\frac{a_i\beta_i}8(6-8c_1\cos\theta_i+2c_2\cos2\theta_i)-\frac{\varsigma w^2}2\bigl(\frac\beta s-\frac\rho s\,g\bigr)`$. All blocks are even in $`P`$; $`c_1,c_2,s,\rho`$ depend on $`P`$ through $`j^2=a^2-4a_1a_2\sin^2P`$, and $`\sin\theta_1=a_2\sin2P/j`$, $`\sin\theta_2=-a_1\sin2P/j`$ give $`\theta_1'=2a_2/a`$, $`\theta_2'=-2a_1/a`$ (primes: $`\partial_P`$ at $`P=0`$). Differentiating through $`j^2`$ ($`\partial_{j^2}s=\frac1{2s}`$, $`\partial_{j^2}\ln\rho=\frac{\lvert w\rvert}{2j^2s}`$) and using $`(\bar s-u)^2(u+2\bar s)=2\bar s^3-3u-2u^3`$:
$`c_1''=\frac{4\varsigma\nu u^2}{\bar s^3}`$, $`c_2''=-\frac{8\nu u^2(2\bar s^3-3u-2u^3)}{\bar s^3}`$, $`a(1/s)''=\frac{4\nu}{\bar s^3}`$, $`a(\rho/s)''=\frac{4\varsigma\nu(\bar s-u)(u\bar s-1)}{\bar s^3}`$, $`g''=-\frac{4\nu(\gamma_c+\gamma_m)}a`$, at $`c_1=-\frac\varsigma{\bar s}`$, $`c_2=1-2u^2+\frac{2u^3}{\bar s}`$, $`a\rho/s=-\frac{\varsigma(\bar s-u)}{\bar s}`$, $`g=\beta`$.
The second derivative of the order-$`\epsilon^4`$ part is $`-\sum_i\frac{a_i\beta_i}8\bigl[-8c_1''+2c_2''+8\theta_i'^2(c_1-c_2)\bigr]-\frac{\varsigma w^2}2\bigl[\beta(1/s)''-\beta(\rho/s)''-(\rho/s)g''\bigr]`$. With $`\sum_ia_i\beta_i\theta_i'^2=4\nu\gamma_m`$ and $`(\bar s-u)(u\bar s-1)=2u+u^3-\bar s^3`$:
```math
\begin{aligned}
E_b''(0)={}&-\frac{4\varsigma\nu a}{\bar s}+\nu\,\mathcal C+O(\epsilon^6),\\
\mathcal C={}&\frac{2u^2}{\bar s^3}\bigl[\gamma_s(\varsigma+\bar s^3-u-u^3)-\gamma_m(\varsigma+\bar s^3-2u-u^3)\bigr]+4\gamma_m\Bigl(1+\frac\varsigma{\bar s}-2u^2+\frac{2u^3}{\bar s}\Bigr)+\frac{2u^2(\bar s-u)}{\bar s}(\gamma_c+\gamma_m).
\end{aligned}
\qquad\text{(14.9)}
```
The first term is $`E_b''(0)`$ of (11.14). Since $`\mathfrak m_1+\mathfrak m_2=a/(4a_1a_2)`$, inverting (14.9) gives
```math
\mathfrak m_b=-\varsigma(\mathfrak m_1+\mathfrak m_2)\sqrt{1+u^2}\,\Bigl[1+\frac{\varsigma\bar s}{4a}\,\mathcal C+O(\epsilon^4)\Bigr].
\qquad\text{(14.10)}
```

### Step 6. Inertia against the binding cost (item 3)

With $`4\mathfrak m_1\mathfrak m_2=1/(4a_1a_2)`$ and the identity $`\mathfrak m_1+\mathfrak m_2-\frac{a(1+\varsigma\bar s)}{4a_1a_2}=-\varsigma\bar s(\mathfrak m_1+\mathfrak m_2)`$ (the leading order of (11.16)), (14.7) and (14.10) give
```math
\mathfrak m_b-\bigl(\mathfrak m_1+\mathfrak m_2-4\mathfrak m_1\mathfrak m_2E_{\rm bind}\bigr)=-\frac{(1+u^2)\,\mathcal C-4\,\mathcal E_4}{16\,a_1a_2}+\mathfrak m_b\,O(\epsilon^4),
\qquad\text{(14.11)}
```
whose first term, divided by $`\mathfrak m_b`$, is $`\frac{\varsigma[(1+u^2)\mathcal C-4\mathcal E_4]}{4a\bar s}+O(\epsilon^4)`$, of order $`\epsilon^2`$. It does not vanish identically. For $`w_{11}<0`$ and $`u\to0`$, (14.12) gives $`(1+u^2)\mathcal C-4\mathcal E_4=2(\gamma_c-2\gamma_m)u^2+O(u^3)`$, nonzero at small enough $`u`$ unless $`\gamma_c=2\gamma_m`$ (equal data of the two bodies: $`\gamma_c-2\gamma_m=-2a_1^2/M_1`$). For the data sets D1, D2, D3 of the code, the predicted relative differences are $`-7.0\times10^{-4}\,\epsilon^2`$, $`1.07\,\epsilon^2`$, $`2.40\times10^{-3}\,\epsilon^2`$; the numerical differences agree with them to $`O(\epsilon^4)`$ (log, Part A, "item 3").

### Step 7. Wide pair (item 4)

For $`\varsigma=-1`$ and $`u\to0`$ in the coefficients ($`\bar s=1+\frac{u^2}2-\frac{u^4}8+O(u^6)`$): $`\phi_A=u^3-\frac34u^4-\frac12u^5`$, $`u\phi_A'=3u^3-3u^4-\frac52u^5`$, $`\phi_B=-u^3+\frac12u^4+\frac12u^5`$, $`u\phi_B'=-3u^3+2u^4+\frac52u^5`$, each up to $`O(u^6)`$. Inserting into (14.7)–(14.10):
```math
\begin{aligned}
&\mathcal E_4=\tfrac12\gamma_m\,u^3+O(u^4),\qquad \nu\,\mathcal C=2\nu(\gamma_c-2\gamma_m)\,u^2+2\nu(5\gamma_m-\gamma_s-\gamma_c)\,u^3+\nu\bigl(3\gamma_s-\tfrac92\gamma_m\bigr)u^4+O(u^5),\\
&\frac{\varsigma\bar s}{4a}\,\mathcal C=-\frac{\gamma_c-2\gamma_m}{2a}\,u^2-\frac{5\gamma_m-\gamma_s-\gamma_c}{2a}\,u^3-\frac{6\gamma_s+2\gamma_c-13\gamma_m}{8a}\,u^4+O(u^5),\\
&\beta_1\Xi_1=\beta_1\bigl(X_3u^3+X_4u^4+X_5u^5\bigr)+O(u^6),\qquad X_3=\frac{a_2}{2a}\Bigl[\frac{a_1-2a_2}{M_1}+\frac{2a_1-a_2}{M_2}\Bigr],\\
&X_4=\frac{a_1^2-7a_1a_2+4a_2^2}{8aM_1}+\frac{3a_2(a_2-a_1)}{4aM_2},\qquad X_5=\frac{a_2}{4a}\Bigl[\frac{2a_2-3a_1}{M_1}+\frac{a_2-4a_1}{M_2}\Bigr],
\end{aligned}
\qquad\text{(14.12)}
```
and $`\beta_2\Xi_2`$ by exchanging the labels 1 and 2 (also in the $`X_k`$). Code, Part C1: the exact Taylor coefficients of the closed forms (14.7)–(14.10), with symbolic data, are identical to those of (14.12).

**First non-vanishing term.** At fixed $`a_1,a_2`$, the coefficients of $`\mathcal E_4`$, $`\nu\mathcal C`$, $`\frac{\varsigma\bar s}{4a}\mathcal C`$ and $`\Xi_1`$ in (14.12) are linear forms in $`(1/M_1,1/M_2)`$. Both of these are positive, and $`\beta_1>0`$.
- $`\mathcal E_4`$: $`\gamma_m>0`$.
- $`\nu\mathcal C`$ and $`\frac{\varsigma\bar s}{4a}\mathcal C`$: their $`u^2`$ coefficients vanish iff $`\gamma_c=2\gamma_m`$. There, their $`u^3`$ coefficients are $`2\nu(3\gamma_m-\gamma_s)`$ and $`-\frac{3\gamma_m-\gamma_s}{2a}`$. Where in addition $`\gamma_s=3\gamma_m`$, their $`u^4`$ coefficients are $`\frac92\nu\gamma_m`$ and $`-\frac{9\gamma_m}{8a}`$, both nonzero.
  - Location of these sets. $`(\gamma_c-2\gamma_m)+(\gamma_s-3\gamma_m)=(a_1^2+a_2^2-5a_1a_2)(\frac1{M_1}+\frac1{M_2})`$, and $`\gamma_c=2\gamma_m`$ iff $`a_1(2a_2-a_1)M_1=a_2(a_2-2a_1)M_2`$. Hence both conditions hold exactly at $`a_1/a_2=\frac{5\mp\sqrt{21}}2`$, $`M_1/M_2=\frac{11\pm\sqrt{21}}{10}`$ (the example of verification I1). The first condition alone holds, e.g., at $`a_1/a_2=\frac14`$, $`M_1/M_2=\frac87`$.
- $`\beta_1\Xi_1`$: $`X_3=0`$ iff $`(2a_2-a_1)/M_1=(2a_1-a_2)/M_2`$. Since $`1/M_i>0`$ and the two sides can be neither both zero nor both negative, this holds iff $`\frac12<a_1/a_2<2`$ and $`\frac{M_1}{M_2}=\frac{2a_2-a_1}{2a_1-a_2}`$. This is also the condition $`X_3=0`$ for $`\beta_2\Xi_2`$. On this set, with $`t:=a_1/a_2`$,
```math
X_4=\frac{a_2^3\,f(t)}{8aM_1(2a_1-a_2)},\quad f(t)=2t^3-9t^2-3t+8,\qquad X_5=-\frac{a_1a_2}{2M_1(2a_1-a_2)}<0 .
```
  On $`(\frac12,2)`$, $`f'<0`$, with $`f(\frac12)=\frac92`$ and $`f(2)=-18`$. Hence $`X_4`$ vanishes at exactly one ratio $`t_*\approx0.86254`$ (then $`M_1/M_2\approx1.56873`$), and there $`X_5\neq0`$. Equal data lie on $`X_3=0`$ with $`t=1`$, where $`\beta_i\Xi_i\simeq-\frac{\beta_i^2}8u^4`$.

Define the sets of hatted data $`\mathcal S_1:=\{\gamma_c\neq2\gamma_m\}`$, $`\mathcal S_2:=\{\gamma_c=2\gamma_m,\ \gamma_s\neq3\gamma_m\}`$, $`\mathcal S_3:=\{\gamma_c=2\gamma_m,\ \gamma_s=3\gamma_m\}`$, and $`\mathcal X_1:=\{X_3\neq0\}`$, $`\mathcal X_2:=\{X_3=0,\ a_1\neq t_*a_2\}`$, $`\mathcal X_3:=\{X_3=0,\ a_1=t_*a_2\}`$. Each list partitions the class with $`w_{11}<0`$, and all six sets are non-empty. Then
```math
\begin{aligned}
\mathcal E_4&\simeq\tfrac12\gamma_m u^3\quad\text{(all data)},\\
\nu\mathcal C&\simeq 2\nu(\gamma_c-2\gamma_m)u^2,\ \ 2\nu(3\gamma_m-\gamma_s)u^3,\ \ \tfrac92\nu\gamma_m u^4\quad\text{on }\mathcal S_1,\ \mathcal S_2,\ \mathcal S_3,\\
\frac{\varsigma\bar s}{4a}\mathcal C&\simeq-\frac{\gamma_c-2\gamma_m}{2a}u^2,\ \ -\frac{3\gamma_m-\gamma_s}{2a}u^3,\ \ -\frac{9\gamma_m}{8a}u^4\quad\text{on }\mathcal S_1,\ \mathcal S_2,\ \mathcal S_3,\\
\beta_1\Xi_1&\simeq\beta_1X_3u^3,\ \ \beta_1X_4u^4,\ \ \beta_1X_5u^5\quad\text{on }\mathcal X_1,\ \mathcal X_2,\ \mathcal X_3,
\end{aligned}
\qquad\text{(14.13)}
```
each with a coefficient that is nonzero on its set. $`\beta_2\Xi_2`$ follows by exchanging the labels 1 and 2, in the sets as well. Code, Part C2 (50-digit arithmetic) tests five data sets: D3, equal data, $`\mathcal S_2`$ ($`a_1/a_2=\frac14`$, $`M_1/M_2=\frac87`$), $`\mathcal S_3`$ and $`\mathcal X_3`$.
- On each set, the first displayed coefficient above $`10^{-30}`$ is the one that (14.13) selects.
- At $`u=10^{-3}`$ the ratios of the closed forms to the terms of (14.13) lie between 0.9970 and 1.0040. The deviations are about ten times smaller than at $`u=10^{-2}`$, as expected for deviations proportional to $`u`$.

## Result

- **(14.1)** [theorem; every diagonal on-site binding, every $`P`$, exact]: $`\Theta=(-1)^{\hat r}\sigma^{(1)}_3\sigma^{(2)}_3`$ commutes with $`H(P)`$. In the class, the level lies in $`\Theta=+1`$, so $`w_{12},w_{21}`$ enter $`E_b`$ at no order.
- **(14.3)–(14.4)** [formula; every member of the class, every $`P`$, under (S2)]: the operator on $`\psi(r)`$ that replaces (11.11), unitarily equivalent to the part of $`H(P)`$ near $`M_1+M_2`$ through order $`\epsilon^4`$, with remainder $`O(\epsilon^6)`$ in norm uniformly in $`P`$. The terms and ranges are those of (14.4). At this order enter $`w_{11}`$ (orders $`\epsilon^2`$, $`\epsilon^4`$), and $`w_{12},w_{21}`$ (order $`\epsilon^4`$, on odd $`r`$ only); $`w_{22}`$ does not enter.
- **(14.6)** [formula; class, every $`P`$, fixed hatted data, both signs]: $`E_b(P)`$ through order $`\epsilon^4`$, remainder $`O(\epsilon^6)`$ with constants depending on the hatted data; even in $`P`$ and independent of $`\eta`$.
- **(14.7)** [formula; class, fixed hatted data]: $`E_{\rm bind}=a(1+\varsigma\bar s)+\mathcal E_4+O(\epsilon^6)`$.
- **(14.8)** [formula; class, fixed hatted data]: $`\langle\sigma^{(i)}_3\rangle_0=1-\beta_i\Lambda+\beta_i\Xi_i+O(\epsilon^6)`$, $`i=1,2`$, from (11.5).
- **(14.9)** [formula; class, fixed hatted data]: $`E_b''(0)=-4\varsigma\nu a/\bar s+\nu\,\mathcal C+O(\epsilon^6)`$.
- **(14.10)** [formula; class, fixed hatted data]: $`\mathfrak m_b=-\varsigma(\mathfrak m_1+\mathfrak m_2)\sqrt{1+u^2}\,[1+\frac{\varsigma\bar s}{4a}\mathcal C+O(\epsilon^4)]`$, the relative correction being of order $`\epsilon^2`$.
- **(14.11)** [negative; class, fixed hatted data; the control of item 3]: with $`E_{\rm bind}`$ of (14.7), the relation (11.16) holds at relative order $`\epsilon^2`$ only on the data with $`(1+u^2)\mathcal C=4\mathcal E_4`$. Otherwise it fails, with leading difference $`-[(1+u^2)\mathcal C-4\mathcal E_4]/(16a_1a_2)`$, of relative order $`\epsilon^2`$. The difference does not vanish identically: it is nonzero for $`w_{11}<0`$ at small enough $`u`$ when $`\gamma_c\neq2\gamma_m`$ (e.g. equal data), and for the data sets D1–D3.
- **(14.12)** [formula; $`w_{11}<0`$, ordered limit: $`\epsilon\to0`$ at fixed $`u`$, then $`u\to0`$ in the coefficients]: the small-$`u`$ expansions, with the coefficients displayed in (14.12):
  - $`\mathcal E_4`$ through $`u^3`$;
  - $`\nu\mathcal C`$ and the relative correction $`\frac{\varsigma\bar s}{4a}\mathcal C`$ of $`\mathfrak m_b`$ through $`u^4`$;
  - $`\beta_i\Xi_i`$ through $`u^5`$.
- **(14.13)** [theorem; every member with $`w_{11}<0`$, same ordered limit]: the leading term in $`u`$ of each order-$`\epsilon^4`$ coefficient of item 2(b), and of the relative correction of item 2(c), is as displayed in (14.13). Each coefficient there is nonzero on its set, and all six sets are non-empty.
  - $`\mathcal E_4\simeq\frac12\gamma_mu^3`$ for all data.
  - $`\nu\mathcal C`$ and the relative correction of $`\mathfrak m_b`$: of order $`u^2`$, $`u^3`$, $`u^4`$ on $`\mathcal S_1`$, $`\mathcal S_2`$, $`\mathcal S_3`$ respectively.
  - $`\beta_1\Xi_1`$: of order $`u^3`$, $`u^4`$, $`u^5`$ on $`\mathcal X_1`$, $`\mathcal X_2`$, $`\mathcal X_3`$ respectively. $`\beta_2\Xi_2`$ follows by exchanging the labels.

## Consistency checks

1. **Dimensions and scaling.** $`a_i,w,s,\kappa_i,\gamma_{s,c,m}`$ are costs; $`\lambda_i`$ is a squared cost; $`\beta_i,u,\nu,c_m`$ are dimensionless. Every term of (14.6), (14.7) and (14.9) is a cost, and (14.8) and the bracket of (14.10) are dimensionless. Under $`(M_i,\tau_i,w_{s_1s_2})\to\ell(M_i,\tau_i,w_{s_1s_2})`$, $`H(P)\to\ell H(P)`$; (14.6), (14.7) and (14.9) scale as $`\ell`$, (14.8) is invariant, and (14.10) scales as $`\ell^{-1}`$, as they must. Passed.
2. **No binding, ordered limit $`u\to0`$, $`w_{11}<0`$, at $`P`$ with $`j(P)>0`$** (this includes a neighbourhood of $`P=0`$, since $`j(0)=a`$). The check does not apply where $`j(P)=0`$, that is at $`a_1=a_2`$, $`P\equiv\pi/2\pmod\pi`$. There the leading band is flat, the stationarity argument below fails, and the order-$`\epsilon^4`$ terms select among its degenerate minimizers. In (14.6), $`s\to j`$, the first bracket tends to $`6-8\cos\theta_i+2\cos2\theta_i=4(1-\cos\theta_i)^2`$, and the $`w^2`$ term vanishes. Since $`a_1\sin\theta_1+a_2\sin\theta_2=0`$ and $`\theta_1-\theta_2=2P`$, $`(p_1^*,p_2^*)=(\theta_1/2,-\theta_2/2)`$ minimizes the leading band. The order-$`\epsilon^4`$ part therefore tends to $`-\sum_i\frac{\tau_i^4\sin^4p_i^*}{8M_i^3}`$, and $`E_b(P)\to\min_{p_1+p_2=P}[\omega_1+\omega_2]`$ through order $`\epsilon^4`$: by stationarity, the shift of the minimizer does not enter at this order. At $`P=0`$ every order-$`\epsilon^4`$ coefficient tends to 0 (14.12). Passed.
3. **Numerical diagonalization** (Code, log Parts A–C). For D1–D3, the deviations from (11.14) scale as $`\epsilon^4`$ (fitted slopes 3.94–4.27), those from (14.6)–(14.9) as $`\epsilon^6`$ (slopes 5.94–6.02; one slope of 5.37 at a deviation of $`6\times10^{-12}`$, the finite-difference noise level). The eigenvalue deviations of the effective operator (14.4) on a ring scale as $`\epsilon^6`$ (slopes 5.97, 5.99), and without the $`w_{12},w_{21}`$ terms they approach $`\epsilon^4`$ (slopes 4.85, 4.26). Passed.

## Open issues

- The remainders are not shown to be uniform in $`u`$ (the gap $`s-j`$ vanishes as $`u\to0`$); (14.12)–(14.13) are derived only as the ordered limit.
- The data on which $`(1+u^2)\mathcal C=4\mathcal E_4`$, where (11.16) survives at relative order $`\epsilon^2`$, are not characterized.
- On odd $`r`$ (sector $`\Theta=-1`$), the $`w_{12},w_{21}`$ terms of (14.4) may produce a further level near the band; other levels are out of scope.

## Code

- `code/v2/check_pair_level.py` (role: check). Output: `code/v2/output/check_pair_level.log`, which contains every number cited here. The closed forms of (14.7)–(14.10) are coded once and used by Parts A and C.
  - **Part A.** Diagonalizes $`H(P)`$ of (11.1) in the sector $`\Theta=+1`$ on the open range $`r\in[-L,L]`$, with $`L=2\lceil40/\ln(1/\lvert\rho(0)\rvert)\rceil`$ (so $`\lvert\psi_P(\pm L)\rvert\lesssim e^{-40}`$): $`L=112,80,408`$ for D1, D2, D3. It takes $`\eta=\frac12`$ and $`\epsilon\in\{0.2,0.1,0.05\}`$. The data sets (hatted; all $`w_{s_1s_2}`$ nonzero) are:
    - D1: $`\hat\tau=(1,1.6)`$, $`M=(1,2.5)`$, $`\hat w_{11}=-0.4`$, $`u=0.79`$;
    - D2: $`\hat\tau=(1.3,0.8)`$, $`M=(1.5,0.7)`$, $`\hat w_{11}=+0.6`$, $`u=1.18`$;
    - D3: $`\hat\tau=(1.2,0.9)`$, $`M=(0.8,1.3)`$, $`\hat w_{11}=-0.12`$, $`u=0.198`$.

    The level is the lowest ($`w_{11}<0`$) or highest ($`w_{11}>0`$) eigenvalue of the cluster above $`E_0-\min M_i`$. $`E_b''(0)`$ comes from a 7-point finite-difference stencil in $`P`$ with step $`h=0.05`$ (using $`E_b(-P)=E_b(P)`$), with a control stencil of step $`0.1`$. Convergence was checked by repeating every run with $`1.5L`$, which changes all quantities by at most $`6\times10^{-12}`$. The two stencils differ by at most $`2\times10^{-9}`$, the truncation error of the step-$`0.1`$ stencil, which is $`2^6`$ times larger than that of the step-$`0.05`$ one. Part A compares $`E_{\rm bind}`$, $`E_b''(0)`$, $`\langle\sigma^{(i)}_3\rangle_0`$ and $`E_b(0.3)`$ with (11.14) and with (14.6)–(14.9), gives the slopes in $`\epsilon`$, and compares item 3 with (14.11) and $`\mathfrak m_b`$ with (14.10).
  - **Part B.** Compares the cluster eigenvalues of $`H(P)`$ on a ring of 40 sites ($`P=0.37`$, $`\eta=0.3`$, D1) with (14.4) built from its explicit coefficients.
  - **Part C1.** Computes with sympy the exact Taylor coefficients in $`u`$ ($`\varsigma=-1`$, symbolic $`a_1,a_2,1/M_1,1/M_2>0`$) of the closed forms of $`\mathcal E_4`$, $`\nu\mathcal C`$, the relative correction of $`\mathfrak m_b`$ and $`\Xi_{1,2}`$. It compares them with (14.12) through $`u^3`$, $`u^4`$, $`u^4`$, $`u^5`$.
  - **Part C2.** Computes $`t_*`$ and, in 50-digit arithmetic (mpmath), selects for each line the first coefficient of (14.12) above $`10^{-30}`$. It then evaluates the ratio of the closed form to that term at $`u=10^{-2},10^{-3}`$. The five data sets are:
    - D3 (in $`\mathcal S_1`$, $`\mathcal X_1`$);
    - equal data (in $`\mathcal X_2`$);
    - $`a_1/a_2=\frac14`$, $`M_1/M_2=\frac87`$ ($`\mathcal S_2`$);
    - $`a_1/a_2=\frac{5-\sqrt{21}}2`$, $`M_1/M_2=\frac{11+\sqrt{21}}{10}`$ ($`\mathcal S_3`$);
    - $`a_1/a_2=t_*`$, $`M_1/M_2=\frac{2-t_*}{2t_*-1}`$ ($`\mathcal X_3`$).

## Methods used

- Canonical Schrieffer–Wolff reduction to fourth order
- Conserved parity and sector reduction
- Perturbation theory of an isolated simple eigenvalue; Hellmann–Feynman identities (11.5)
- Lattice contact bound state, geometric sums
- Taylor expansion in $`P`$, asymptotic expansion in $`u`$
- Exact diagonalization, finite-difference stencils, convergence in system size
- Case analysis of linear forms on cancellation sets; computer-algebra series and high-precision arithmetic (check)
