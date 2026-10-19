# The field made by a held source as a common local scale for a test body

- **Subproject:** 06-ilang-source
- **Package:** 05-made-field-scale
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-19

## Setup and assumptions

**Inputs** (as quoted in question.md).
- (2.1) of 02-what-a-body-presents@v3: $`C_{bf}=\gamma\sum_xQ_x\otimes\Phi_x`$, $`Q^{(a)}_x=\Pi_xO`$, $`Q^{(c)}_x=\Pi_xO+\tfrac12(A_x+A_{x-1})`$, with $`\Pi_x=\lvert x\rangle\langle x\rvert\otimes\mathbb 1_2\otimes\mathbb 1_N`$, $`O=\sigma_3\otimes(m\mathbb 1_N+D)`$, $`A_x`$ the bond $`(x,x+1)`$ of the motion term, $`A=\sum_xA_x`$, $`B=\sum_x\Pi_xO`$.
- (3.6), (3.9) of 03-held-sources@v4: $`\chi_n(x,y)=\sum_{m:\,e_m\neq e_n}2\mathrm{Re}\bigl(\langle\varphi_n\vert\Phi_x\vert\varphi_m\rangle\langle\varphi_m\vert\Phi_y\vert\varphi_n\rangle\bigr)/(e_m-e_n)`$ and $`\langle\varphi_n(g)\vert\Phi_y\vert\varphi_n(g)\rangle=\bar\Phi_n(y)-\sum_ig_i\chi_n(y,x_i)+O(\lVert\Phi_y\rVert v^2/\Delta_n^2)`$.
- (4.4) of 04-profile@v4: $`M^{(2)}(x_1,x_2)=-\frac{2ng_1g_2}{t_f}\Lambda^+(x_1,x_2)`$, $`\Lambda^+(x,y)=\lvert X_f\rvert^{-1}\sum_{\mathbf k\neq0}e^{i\mathbf k\cdot(x-y)}/\omega(\mathbf k)`$, $`\omega(\mathbf k)=\sum_{\mu=1}^{D}4\sin^2\frac{k_\mu}2`$.
- (17.11) of 05-ilang-free-fall/17-typical-or-forced@v3: for linear level profiles $`M_{x,k}=M_k+G_kx`$, $`V_{x,k}=-\mathcal F_kx`$: R3 $`\iff G_k=\gamma'M_k,\ \mathcal F_k=\phi M_k\ \forall k\iff\boldsymbol g\in\mathcal U_4^{\pm}`$ (fall from rest level independent on both branches). Here $`\gamma'`$ is the $`\gamma`$ of (17.11), not the coupling constant $`\gamma`$.
- (4.16), (4.24) of 05-ilang-free-fall/04-branch-fall@v3: $`a_{k,\sigma}(0)=\frac{\tau_k^2}{M_k}(\sigma\mathcal F_k-G_k)`$; $`\frac{\mathrm d^2\bar x}{\mathrm d\lambda^2}\big\vert_{\rm drift}=d_0\,a_{k,+}(0)\,\hat e=-\frac{v_{\max}^2}{d_0}\frac{r(x+1)-r(x)}{r(x)}\hat e`$, with $`v_{\max}=\tau d_0`$, $`d_0=\kappa\sigma_X`$, $`r(x)`$ the clock rate at $`x`$.

**Assumptions** (the description chosen for study, M8, M9).
- **S1 Field.** $`N_f\ge1`$ identical field objects ($`c=+1`$), no pair terms among them; places $`X_f`$: a ring of $`L\ge5`$ places ($`D=1`$), an $`L\times L`$ torus ($`D=2`$) or an $`L^3`$ torus ($`D=3`$); own term $`C_1=-t_f\sum_{\{x,y\}}(\lvert x\rangle\langle y\rvert+\lvert y\rangle\langle x\rvert)`$, $`t_f>0`$; $`\Phi_x`$ the number of field objects at $`x`$; $`n=N_f/\lvert X_f\rvert`$. With the source the field operator is $`C_f^s:=\sum_{j=1}^{N_f}C_1^{(j)}+g_s\Phi_{x_s}`$ on the symmetric subspace $`\mathcal H_f`$.
- **S2 Source.** The held source is in a common eigenvector of its own term and of its coupled operator (eigenvalue $`g_s`$). $`C`$ then keeps the source in that vector, and the source enters only through $`g_s\Phi_{x_s}`$ and a constant; it is suppressed below.
- **S3 Test body.** Model D with positions $`x\in\ell`$, a line of $`X_f`$ (the whole ring for $`D=1`$), recorded by a medium $`c`$. $`C_{bc}`$ is the part of $`C`$ not involving the field: $`C_{\rm D}=A+B`$, the record term and the medium's own term. Coupling (2.1), form (a) or (c). $`d_k=2\pi k/(N\lambda_0)`$, $`M_k=m+d_k`$, $`\lVert O\rVert=M_{N-1}`$.
- **S4 Start.** $`\Psi(0)=\xi\otimes\varphi`$ with any body–medium state $`\xi\in\mathcal H_{bc}=\mathcal H_b\otimes\mathcal H_c`$ and a field state $`\varphi`$; $`\varphi(\lambda):=e^{-iC_f^s\lambda}\varphi`$. Items 2–3 use a stationary $`\varphi`$ (an eigenvector of $`C_f^s`$), item 4 the lowest adapted state (Step 5).
- **S5 Positivity** (items 3–4). $`\nu(x):=1+\gamma N_\varphi(x)>0`$ on $`\ell`$, and $`1+\gamma n>0`$.
- **S6 Regime of item 3.** The conditions of (4.16) of 05-ilang-free-fall/04-branch-fall (branch start at rest, first order in the gradients), and the local-slope approximation: on the support of the start (width $`w`$ around $`x_0`$) $`N_\varphi(x)=N_\varphi(x_0)+N'(x_0)(x-x_0)`$ up to a curvature term, with $`\lvert N''\rvert w\ll\lvert N'\rvert`$.

Notation: $`N_\lambda(x):=\langle\varphi(\lambda)\vert\Phi_x\vert\varphi(\lambda)\rangle`$, $`\delta\Phi_x:=\Phi_x-N_\lambda(x)`$, $`\sigma_\Phi(\lambda):=\max_{x\in\ell}\bigl(\mathrm{Var}_{\varphi(\lambda)}\Phi_x\bigr)^{1/2}`$. For stationary $`\varphi`$, $`N_\lambda=N_\varphi`$ and $`\sigma_\Phi`$ are constant.

## Derivation

### Step 1. The operator by which the test body evolves

By S2, on $`\mathcal H_{bc}\otimes\mathcal H_f`$ and up to a constant (a common phase, (1.2)), $`C=C_{bc}\otimes\mathbb 1+\mathbb 1\otimes C_f^s+\gamma\sum_{x\in\ell}Q_x\otimes\Phi_x`$. For a unit vector $`\varphi`$ define the partial expectation $`\bar C_\varphi`$ on $`\mathcal H_{bc}`$ by $`\langle\xi'\vert\bar C_\varphi\vert\xi\rangle:=\langle\xi'\otimes\varphi\vert C\vert\xi\otimes\varphi\rangle`$. Inserting $`C`$:

```math
\bar C_\varphi=C_{bc}+\gamma\sum_{x\in\ell}N_\varphi(x)\,Q_x+E_\varphi\mathbb 1,\qquad N_\varphi(x)=\langle\varphi\vert\Phi_x\vert\varphi\rangle,\quad E_\varphi=\langle\varphi\vert C_f^s\vert\varphi\rangle .
\qquad\text{(5.1)}
```

Let $`\xi(\lambda)`$ solve $`i\,\mathrm d\xi/\mathrm d\lambda=(\bar C_{\varphi(\lambda)}-E_\varphi)\xi`$ ($`E_{\varphi(\lambda)}=E_\varphi`$ is conserved) and $`\Psi_{\rm eff}:=\xi(\lambda)\otimes\varphi(\lambda)`$. The product rule gives $`i\dot\Psi_{\rm eff}=C\Psi_{\rm eff}-\gamma W_\lambda\Psi_{\rm eff}`$ with $`W_\lambda:=\sum_xQ_x\otimes\delta\Phi_x`$. Hence $`D:=\Psi-\Psi_{\rm eff}`$ obeys $`i\dot D=CD+\gamma W_\lambda\Psi_{\rm eff}`$, $`D(0)=0`$, and Duhamel's formula with the unitarity of $`e^{-iC\lambda}`$ gives $`\lVert D(\lambda)\rVert\le\lvert\gamma\rvert\int_0^{\lvert\lambda\rvert}\lVert W_\mu\Psi_{\rm eff}(\mu)\rVert\,\mathrm d\mu`$. Write $`W\Psi_{\rm eff}=\sum_xv_x`$, $`v_x=Q_x\xi\otimes\delta\Phi_x\varphi`$, $`\lVert\delta\Phi_x\varphi\rVert^2=\mathrm{Var}\Phi_x`$.
- (a): $`Q_xQ_y=\delta_{xy}\Pi_xO^2`$, so $`\lVert\sum_xv_x\rVert^2=\sum_x\langle\xi\vert\Pi_xO^2\vert\xi\rangle\mathrm{Var}\Phi_x\le\lVert O\rVert^2\sigma_\Phi^2`$.
- (c): $`Q_x\xi`$ lies on the places $`x-1,x,x+1`$, so $`\langle v_x,v_y\rangle=0`$ for $`\lvert x-y\rvert\ge3`$ and $`\lVert\sum_xv_x\rVert^2\le5\sum_x\lVert v_x\rVert^2`$. With $`\lVert A_x\rVert=\tau/2`$, $`\lVert Q_x\xi\rVert\le(\lVert O\rVert+\frac\tau2)\lVert(\Pi_{x-1}+\Pi_x+\Pi_{x+1})\xi\rVert`$, whose squares sum to $`3`$.

Therefore

```math
\bigl\lVert\Psi(\lambda)-\xi(\lambda)\otimes\varphi(\lambda)\bigr\rVert\le\lvert\gamma\rvert\,c_Q\int_0^{\lvert\lambda\rvert}\sigma_\Phi(\mu)\,\mathrm d\mu,\qquad c_{Q^{(a)}}=\lVert O\rVert,\quad c_{Q^{(c)}}=\sqrt{15}\,\bigl(\lVert O\rVert+\tfrac\tau2\bigr).
\qquad\text{(5.2)}
```

For stationary $`\varphi`$, $`\xi(\lambda)=e^{-i(\bar C_\varphi-E_\varphi)\lambda}\xi`$: up to a common phase the test body evolves by the $`\lambda`$-independent $`\bar C_\varphi`$ and the field stays in $`\varphi`$, with remainder at most $`\lvert\gamma\rvert c_Q\sigma_\Phi\lvert\lambda\rvert`$; reading probabilities change by at most twice that. The neglected term $`\gamma W`$ is the change of the field by the test body, so (5.2) is the order of the test-body neglect (A15): first order in $`\gamma`$, proportional to the field fluctuation $`\sigma_\Phi`$ and to $`\lvert\lambda\rvert`$. The description holds for $`\lvert\lambda\rvert\ll(\lvert\gamma\rvert c_Q\sigma_\Phi)^{-1}`$.

*M6.* $`\bar C_\varphi`$ is computed from $`C`$ and $`\varphi`$ alone. It is therefore unchanged by every relisting that leaves $`C`$ unchanged, e.g. $`\Phi_x\to\Phi_x-c_x`$ together with $`C_{\rm D}\to C_{\rm D}+\gamma\sum_xc_xQ_x`$, place-dependent $`c_x`$ included. It does not depend on the labels of the field objects ($`\Phi_x`$ is symmetric) or on the phase of $`\varphi`$, and its multiple of $`\mathbb 1`$ is a common phase. The split of $`\bar C_\varphi`$ into $`C_{bc}`$ and $`\gamma\sum_xN_\varphi(x)Q_x`$ is not fixed: the separate values of the bare blocks, of $`\gamma`$ and of $`N_\varphi(x)`$ depend on the listing.

### Step 2. Level blocks

Let $`\hat\nu:=\sum_x\nu(x)\Pi_x`$ with $`\nu(x)=1+\gamma N_\varphi(x)`$. On level $`k`$, $`O=M_k\sigma_3`$. For (a), (5.1) gives $`\gamma\sum_xN_\varphi(x)\Pi_xO=(\hat\nu-1)B`$. For (c) it gives in addition $`\gamma\sum_xN_\varphi(x)\tfrac12(A_x+A_{x-1})=\gamma\sum_x\tfrac12(N_\varphi(x)+N_\varphi(x+1))A_x`$. Since $`A_x`$ connects only $`x`$ and $`x+1`$, $`\tfrac12\{\hat\nu,A_x\}=\tfrac12(\nu(x)+\nu(x+1))A_x`$. The record term and the medium do not involve the field and stay the background of 05-ilang-free-fall. The level-$`k`$ blocks of $`\bar C_\varphi`$ are

```math
\begin{aligned}
&B_{x,k}=M_{x,k}\sigma_3+V_{x,k}\mathbb 1_2,\qquad M_{x,k}=\nu(x)\,M_k,\qquad V_{x,k}=E_\varphi,\\
&\text{hopping on }(x,x+1):\ \tfrac{\tau_{x,x+1}}2(-i\sigma_1),\qquad \tau^{(a)}_{x,x+1}=\tau,\qquad \tau^{(c)}_{x,x+1}=\tau\,\tfrac12\bigl(\nu(x)+\nu(x+1)\bigr),
\end{aligned}
\qquad\text{(5.3)}
```

i.e. the Model D part of $`\bar C_\varphi`$ is $`\hat\nu B+A`$ for (a) and $`\tfrac12\{\hat\nu,C_{\rm D}\}`$ for (c). Fixed by $`C`$ and $`\varphi`$: the blocks of $`\bar C_\varphi`$, i.e. $`M_{x,k}`$, the hopping amplitudes and $`V_{x,k}`$ up to the common constant. Hence the level-independent ratios $`\nu(y)/\nu(x)=M_{y,k}/M_{x,k}`$ are fixed. Listing-dependent: the factorization $`M_{x,k}=\nu(x)M_k`$ (a constant relisting $`c_x=c`$ multiplies $`M_k`$, and $`\tau`$ for (c), by $`1+\gamma c`$ and divides $`\nu`$ by it) and the place-independent constant $`E_\varphi`$ in $`V_{x,k}`$.

### Step 3. R3 place by place, the hopping, and a control

From (5.3), for both couplings and every $`\varphi`$ (at every $`\lambda`$ if $`\varphi`$ is not stationary):

```math
B_{x+1,k}-B_{x,k}=M_k\,\Gamma(x),\qquad \Gamma(x)=\gamma\bigl(N_\varphi(x+1)-N_\varphi(x)\bigr)\sigma_3 ;\qquad\text{for }\nu(x)\neq0:\ B_{x+1,k}-B_{x,k}=M_{x,k}\,\frac{\nu(x+1)-\nu(x)}{\nu(x)}\,\sigma_3 .
\qquad\text{(5.4)}
```

$`\Gamma(x)`$ does not depend on $`k`$, so R3 holds at every place. It has no $`\mathbb 1_2`$ part ($`\phi=0`$ in the parametrization of (17.11) of 05-ilang-free-fall/17-typical-or-forced). The second form uses only fixed quantities.

*Hopping.* (a): the hopping is $`\tau`$ at every bond, while the on-site blocks change by $`\nu(x+1)/\nu(x)`$. The two factors differ at every place with $`\gamma(N_\varphi(x+1)-N_\varphi(x))\neq0`$. (c): by (5.3), every matrix element of the Model D part of $`\bar C_\varphi`$ between places $`x,x'`$ ($`x'=x`$ or a neighbour) equals that of $`C_{\rm D}`$ times $`\tfrac12(\nu(x)+\nu(x'))`$. The hopping of every level thus carries the same local factor as the on-site blocks, evaluated as the mean over the two ends of the bond.

*Control.* Take the pair term of the same form with $`Q^{(r)}_x=\Pi_x\,\sigma_3\otimes m\mathbb 1_N`$ (rest term only). Then $`B^{(r)}_{x,k}=(M_k+\gamma mN_\varphi(x))\sigma_3+E_\varphi\mathbb 1_2`$. R3 at $`x`$ would require $`M_k\Gamma=\gamma m\Delta N\sigma_3`$ for $`k=0,1`$, $`\Delta N:=N_\varphi(x+1)-N_\varphi(x)`$. With $`M_0=m`$ this forces $`\Gamma=\gamma\Delta N\sigma_3`$ and then $`d_1\gamma\Delta N=0`$, where $`d_1=2\pi/(N\lambda_0)>0`$. Under (4.16) of 05-ilang-free-fall/04-branch-fall ($`G_k=\gamma mN'`$, $`\mathcal F_k=0`$, $`\tau_k=\tau`$):

```math
B^{(r)}_{x+1,k}-B^{(r)}_{x,k}=\gamma m\,\Delta N\,\sigma_3,\qquad a^{(r)}_{k,\sigma}(0)=-\tau^2\,\frac{\gamma m\,N'(x_0)}{M_k+\gamma mN_\varphi(x_0)} .
\qquad\text{(5.5)}
```

So R3 fails at every place with $`\gamma\Delta N\neq0`$, and there the fall from rest depends on the level.

### Step 4. Clock rate and fall in a stationary field state

The on-site eigenvalues are $`E_\varphi\pm\nu(x)M_k`$. By S5 the upper one is $`E_\varphi+\nu(x)M_k`$, and its spacing between levels $`k,l`$ is $`\nu(x)(d_l-d_k)`$. The clock-rate ratio of two places is therefore

```math
\frac{r(y)}{r(x)}=\frac{\nu(y)}{\nu(x)}=\frac{M_{y,k}}{M_{x,k}},
\qquad\text{(5.6)}
```

the same for every pair of levels. It is exact in $`\bar C_\varphi`$ (no gradient expansion), and the lower branch gives the same ratio.

*Fall.* Under S6 the profiles across the start are those of 05-ilang-free-fall with base half-gap $`\nu(x_0)M_k`$, $`G_k=\gamma N'(x_0)M_k`$, $`\mathcal F_k=0`$, and hopping $`\tau_k=\tau_{\rm loc}(x_0)`$: $`\tau`$ for (a), $`\tau\nu(x_0)`$ for (c) up to first order in the gradient. The variation of the hopping across the start (c) does not enter at first order. In the band energy of a branch, $`E_\sigma(x,p)=E_\varphi+\sigma\sqrt{M_{x,k}^2+\tau_{\rm loc}(x)^2\sin^2p}`$, the hopping multiplies $`\sin^2p`$, whose $`x`$-derivative vanishes at rest. With (4.16) of 05-ilang-free-fall/04-branch-fall and (5.6):

```math
a_{k,\sigma}(0)=-\tau_{\rm loc}(x_0)^2\,\frac{\gamma N'(x_0)}{\nu(x_0)}=-\tau_{\rm loc}(x_0)^2\,\frac{r(x_0+1)-r(x_0)}{r(x_0)},\qquad v_{\max}(x_0):=\tau_{\rm loc}(x_0)\,d_0 .
\qquad\text{(5.7)}
```

The second equality holds at first order in the gradient. $`a_{k,\sigma}`$ is the same for all levels and both branches, as (17.11) of 05-ilang-free-fall/17-typical-or-forced requires for R3 with $`\phi=0`$. Multiplying by $`d_0`$, $`d_0a_{k,+}(0)=-\frac{v_{\max}(x_0)^2}{d_0}\frac{r(x_0+1)-r(x_0)}{r(x_0)}`$: (4.24) holds with the maximal speed $`v_{\max}(x_0)`$ of the effective contract at the start. For (a), $`v_{\max}(x_0)=\tau d_0`$ at every place. For (c), $`v_{\max}(x_0)=\tau\nu(x_0)d_0`$ changes from place to place by the factor of $`r`$; with the value at a fixed reference place $`y`$ instead, (4.24) acquires the factor $`(r(x_0)/r(y))^2`$. $`\tau_{\rm loc}`$ and $`\gamma N'/\nu=(M_{x_0+1,k}-M_{x_0,k})/M_{x_0,k}`$ are fixed by $`C`$ and $`\varphi`$.

### Step 5. The made field in the lowest adapted state

Without pair terms among the field objects, $`C_f^s=\sum_jh^{(j)}`$ with $`h=C_1+g_s\lvert x_s\rangle\langle x_s\rvert`$. $`h`$ has off-diagonal entries $`-t_f\le0`$ on a connected graph, so by Perron–Frobenius its lowest eigenvector $`u_g`$ is unique and positive, for every real $`g_s`$. The lowest state of $`C_f^s`$ is then $`u_g^{\otimes N_f}`$, which is symmetric and unique. In it the $`N_f`$ objects are independent: $`N(y)=N_fu_g(y)^2`$ and $`\mathrm{Var}\Phi_y=N_fu_g(y)^2(1-u_g(y)^2)\le N(y)`$. In (5.2), $`\sigma_\Phi^2\le\max_yN(y)`$.

Apply (3.9) to one field object ($`\Phi_y\to\lvert y\rangle\langle y\rvert`$, $`v=\lvert g_s\rvert`$). The eigenvectors of $`C_1`$ are the plane waves $`\lvert X_f\rvert^{-1/2}e^{i\mathbf k\cdot x}`$ with eigenvalues $`-2Dt_f+t_f\omega(\mathbf k)`$; the lowest is uniform, with gap $`t_f\omega_{\min}`$, $`\omega_{\min}=4\sin^2(\pi/L)`$. In (3.6) each term is $`\lvert X_f\rvert^{-2}e^{i\mathbf k\cdot(y-x_s)}/(t_f\omega(\mathbf k))`$, so $`\chi_0=\frac{2}{\lvert X_f\rvert t_f}\Lambda^+`$. Multiplying by $`N_f`$:

```math
N(y)=n-\frac{2n\,g_s}{t_f}\,\Lambda^+(y,x_s)+O\Bigl(\frac{N_fg_s^2}{t_f^2\omega_{\min}^2}\Bigr),\qquad \delta N(y):=N(y)-n,
\qquad\text{(5.8)}
```

with the kernel $`\frac{2n}{t_f}\Lambda^+`$ of (4.4). On the ring, with $`\varrho\in[0,L/2]`$ the ring distance from $`x_s`$,

```math
\Lambda^+(x,x_s)=\frac{L^2-1}{12L}-\frac{\varrho(L-\varrho)}{2L}.
\qquad\text{(5.9)}
```

Check: the second difference of $`-\varrho(L-\varrho)/(2L)`$ is $`-1/L`$ for $`\varrho\neq0`$ and $`1-1/L`$ at $`\varrho=0`$, so $`\Lambda G=\delta_{x_s}-1/L`$; the constant makes $`\sum_xG=0`$, which fixes $`\Lambda^+\delta_{x_s}`$. On the tori, with $`\vec\varrho=x-x_s`$ (nearest image) and $`\varrho=\lvert\vec\varrho\rvert`$, the standard asymptotics of the lattice Green function give, for $`1\ll\varrho\ll L`$,

```math
\Lambda^+(x,x_s)=c_L-\frac{\ln\varrho}{2\pi}+O(\varrho^{-2})+O\Bigl(\frac{\varrho^2}{L^2}\Bigr)\ (D=2),\qquad \Lambda^+(x,x_s)=\frac{1}{4\pi\varrho}-c_L'+O(\varrho^{-3})+O\Bigl(\frac{\varrho^2}{L^3}\Bigr)\ (D=3),
\qquad\text{(5.10)}
```

with constants $`c_L,c'_L`$ and gradients given by the term-by-term derivatives.

### Step 6. Dependence on the distance from the source

Insert (5.8) into (5.6) and (5.7). With $`\bar\gamma:=\gamma/(1+\gamma n)`$, which has the sign of $`\gamma`$ by S5, $`\gamma/\nu(x)=\bar\gamma+O(g_s)`$ and $`\nu(y)/\nu(x)=1+\bar\gamma(\delta N(y)-\delta N(x))+O(g_s^2)`$. Also $`\tau_{\rm loc}=\tau_0+O(g_s)`$, with $`\tau_0=\tau`$ (a) and $`\tau_0=\tau(1+\gamma n)`$ (c). Then

```math
\frac{r(y)}{r(x)}=1+\frac{2n\bar\gamma g_s}{t_f}\bigl[\Lambda^+(x,x_s)-\Lambda^+(y,x_s)\bigr]+O(g_s^2),
\qquad\text{(5.11)}
```

```math
a_{k,\sigma}(0)\big\vert_{x_0}=\frac{2n\bar\gamma g_s}{t_f}\,\tau_0^2\;\partial_\ell\Lambda^+(x_0,x_s)+O(g_s^2),
\qquad\text{(5.12)}
```

where $`\partial_\ell`$ is the slope along $`\ell`$. With (5.9) on the ring ($`\varrho_x`$ the ring distance of $`x`$; $`a`$ counted positive away from the source):

```math
\frac{r(y)}{r(x)}=1+\frac{n\bar\gamma g_s}{t_fL}\bigl[\varrho_y(L-\varrho_y)-\varrho_x(L-\varrho_x)\bigr]+O(g_s^2),\qquad a_{k,\sigma}(0)=-\frac{n\bar\gamma g_s}{t_f}\,\tau_0^2\Bigl(1-\frac{2\varrho}{L}\Bigr)+O(g_s^2).
\qquad\text{(5.13)}
```

With (5.10) on the tori, to leading order in $`1\ll\varrho\ll L`$:

```math
\frac{r(y)}{r(x)}=1+\frac{n\bar\gamma g_s}{\pi t_f}\ln\frac{\varrho_y}{\varrho_x},\quad a=-\frac{n\bar\gamma g_s\tau_0^2}{\pi t_f}\frac{\hat e_\ell\cdot\vec\varrho}{\varrho^2}\ (D=2);\qquad \frac{r(y)}{r(x)}=1+\frac{n\bar\gamma g_s}{2\pi t_f}\Bigl(\frac1{\varrho_x}-\frac1{\varrho_y}\Bigr),\quad a=-\frac{n\bar\gamma g_s\tau_0^2}{2\pi t_f}\frac{\hat e_\ell\cdot\vec\varrho}{\varrho^3}\ (D=3).
\qquad\text{(5.14)}
```

*Range.* S6 fails where the made field has a kink or a vanishing slope. On the ring, $`\Lambda^+`$ has a kink at $`x_s`$ and zero slope at the antipode, and its curvature is $`-1/L`$; the acceleration formulas need $`w\ll\varrho`$ and $`w\ll L/2-\varrho`$. On the tori the curvature is $`\sim\varrho^{-2}`$ against a slope $`\sim\varrho^{-1}`$, so they need $`w\ll\varrho`$.

*Signs.* $`\Lambda^+(\cdot,x_s)`$ decreases with $`\varrho`$: exactly on the ring for $`0\le\varrho\le L/2`$ by (5.9), and in the leading forms (5.10) on the tori. Hence, at first order in $`g_s`$, for $`g_s\gamma>0`$ the clock runs slower nearer the source and the drift acceleration points towards it: on the ring towards $`x_s`$ along the shorter arc, on the tori with the component along $`\ell`$ that decreases $`\varrho`$. For $`g_s\gamma<0`$ both reverse: the clock runs faster nearer the source and the fall is away from it.

## Result

- **(5.1), (5.2)** [theorem]. Class: couplings (a) and (c); every field state $`\varphi`$; product starts $`\xi\otimes\varphi`$ with every body–medium state $`\xi`$ (S1–S4). The joint state equals $`\xi(\lambda)\otimes\varphi(\lambda)`$, with $`\xi`$ evolving by the partial expectation $`\bar C_{\varphi(\lambda)}`$ of the total contract in the field state (5.1), up to a common phase and a remainder of norm at most $`\lvert\gamma\rvert c_Q\int_0^{\lvert\lambda\rvert}\sigma_\Phi`$ (5.2). This is first order in $`\gamma`$, valid for $`\lvert\lambda\rvert\ll(\lvert\gamma\rvert c_Q\sigma_\Phi)^{-1}`$; the neglected term is the test body's own change of the field. For stationary $`\varphi`$ the operator is $`\lambda`$-independent, and in the lowest adapted state $`\sigma_\Phi^2\le\max_yN(y)`$. $`\bar C_\varphi`$ is fixed by $`C`$ and $`\varphi`$; its split into own and field-made parts is not. The bound holds for every member of the class.
- **(5.3)** [formula]. Same class. The level-$`k`$ blocks of $`\bar C_\varphi`$: on-site $`\nu(x)M_k\sigma_3+E_\varphi\mathbb 1_2`$; hopping $`\tau`$ for (a) and $`\tau\frac12(\nu(x)+\nu(x+1))`$ for (c). Fixed by $`C`$ and $`\varphi`$: $`M_{x,k}`$, the hopping amplitudes and $`V_{x,k}`$ up to a common constant, hence the ratios $`M_{y,k}/M_{x,k}=\nu(y)/\nu(x)`$. Listing-dependent: the factorization $`M_{x,k}=\nu(x)M_k`$ and the place-independent constant in $`V_{x,k}`$.
- **(5.4)** [theorem]. Class: (a) and (c), every field state, every place (at every $`\lambda`$). R3 holds with $`\Gamma(x)=\gamma(N_\varphi(x+1)-N_\varphi(x))\sigma_3`$, without a $`\mathbb 1_2`$ part. In fixed quantities, $`B_{x+1,k}-B_{x,k}=M_{x,k}\frac{\nu(x+1)-\nu(x)}{\nu(x)}\sigma_3`$ for $`\nu(x)\neq0`$. The hopping changes by the same factor as the on-site blocks for (c), with the bond carrying the mean $`\frac12(\nu(x)+\nu(x+1))`$ of the factors of its ends. For (a) it does not: the hopping stays $`\tau`$ at every place, and the factors differ wherever $`\gamma(N_\varphi(x+1)-N_\varphi(x))\neq0`$. No field state violates R3 for (a) or (c); the control is (5.5).
- **(5.5)** [negative]. Control: the pair term $`\gamma\sum_x\Pi_x\sigma_3\otimes m\mathbb 1_N\otimes\Phi_x`$ (rest term only). R3 fails at every place with $`\gamma(N_\varphi(x+1)-N_\varphi(x))\neq0`$, and there the fall from rest (under S6) depends on the level.
- **(5.6)** [formula]. Class: (a), (c), stationary $`\varphi`$, S5. The clock-rate ratio of two places is $`r(y)/r(x)=\nu(y)/\nu(x)=M_{y,k}/M_{x,k}`$, the same for every pair of levels and for both branches. It is exact in $`\bar C_\varphi`$.
- **(5.7)** [theorem]. Class: (a), (c), stationary $`\varphi`$, branch starts at rest, S5–S6; first order in the gradients. $`a_{k,\sigma}(0)=-\tau_{\rm loc}(x_0)^2\,\gamma N'(x_0)/\nu(x_0)`$, the same for all levels and both branches. (4.24) of 05-ilang-free-fall/04-branch-fall holds with $`v_{\max}(x_0)=\tau_{\rm loc}(x_0)d_0`$. For (a) this is $`\tau d_0`$ at every place. For (c) it is $`\tau\nu(x_0)d_0`$, which changes from place to place by the factor of $`r`$; with a place-independent $`v_{\max}`$ taken at a reference place $`y`$, (4.24) carries the factor $`(r(x_0)/r(y))^2`$.
- **(5.8), (5.9)** [formula]. The lowest adapted state is $`u_g^{\otimes N_f}`$, unique for every real $`g_s`$. In it $`N(y)=n-\frac{2ng_s}{t_f}\Lambda^+(y,x_s)`$ up to $`O(N_fg_s^2/(t_f\omega_{\min})^2)`$, with $`\Lambda^+`$ on the ring given exactly by (5.9).
- **(5.11), (5.12)** [formula]. Class: (a), (c), lowest adapted state, S5 (and S6 for the acceleration); first order in $`g_s`$, with $`\bar\gamma=\gamma/(1+\gamma n)`$ and $`\tau_0`$ the source-free hopping of $`\bar C_\varphi`$. Clock-rate ratio $`1+\frac{2n\bar\gamma g_s}{t_f}[\Lambda^+(x,x_s)-\Lambda^+(y,x_s)]`$; acceleration $`\frac{2n\bar\gamma g_s}{t_f}\tau_0^2\partial_\ell\Lambda^+(x_0,x_s)`$, level and branch independent.
- **(5.13), (5.14)** [formula, criterion]. Ring, exact in $`L`$ at first order in $`g_s`$: (5.13), for the acceleration with $`w\ll\varrho`$ and $`w\ll L/2-\varrho`$. Square and cubic tori, leading forms for $`1\ll\varrho\ll L`$, $`w\ll\varrho`$: (5.14), with the logarithm ($`D=2`$) and $`1/\varrho`$ ($`D=3`$) in the clock ratio, and the acceleration along $`\ell`$ the projection on $`\hat e_\ell`$ of a radial vector of size $`\propto\varrho^{-1}`$ ($`D=2`$), $`\propto\varrho^{-2}`$ ($`D=3`$). Signs, at first order in $`g_s`$, with S5 and in these ranges: for $`g_s\gamma>0`$ the clock is slower nearer the source and the fall is towards it; for $`g_s\gamma<0`$ the clock is faster nearer the source and the fall is away from it.

## Consistency checks

- **Dimensions.** $`\gamma`$ and $`n,\Lambda^+`$ are numbers; $`g_s,t_f,\tau,M_k`$ have the dimension of $`C`$, i.e. $`1/\lambda`$. Then $`n\bar\gamma g_s/t_f`$ and $`\lvert\gamma\rvert c_Q\sigma_\Phi\lvert\lambda\rvert`$ are dimensionless, and $`a\propto\tau_0^2`$ has the dimension of label$`/\lambda^2`$. Passed.
- **$`g_s=0`$ or $`\gamma=0`$.** For $`g_s=0`$, (5.8) gives $`N=n`$ uniform, hence $`\Gamma=0`$, $`r(y)/r(x)=1`$ and $`a=0`$ in (5.11)–(5.14). For $`\gamma=0`$, $`\bar C_\varphi=C_{bc}+E_\varphi`$ and the bound (5.2) vanishes. Passed.
- **Sharp field.** Take $`t_f=0`$ and $`\varphi`$ a joint eigenvector of all $`\Phi_x`$. Then $`\varphi`$ is stationary, $`\sigma_\Phi=0`$, (5.2) is exact, and $`C(\xi\otimes\varphi)=(\bar C_\varphi\xi)\otimes\varphi`$ directly: the given lapse field of 05-ilang-free-fall with on-site factor $`1+\gamma N(x)`$. Passed.

## Open issues

- The bound (5.2) grows linearly in $`\lambda`$. A bound that uses the field gap $`t_f\omega_{\min}`$ (a non-growing first-order remainder plus a second-order shift, which is the test body's own mark of 06-own-mark) is not derived.
- The remainder of (5.8), taken from (3.9) per field object, is crude ($`N_fg_s^2/(t_f\omega_{\min})^2`$); a sharp estimate of the second-order profile is not derived.
- Non-product starts, and non-stationary field states for items 3–4 (a $`\lambda`$-dependent profile), are not treated.
- Regions with $`\nu(x)\le0`$ and the neighbourhoods $`\varrho\lesssim w`$ of the source are outside the formulas, as are the ring antipode and $`\varrho\sim L`$ on the tori.

## Methods used

- partial expectation (mean field) over the field state
- Duhamel formula, unitarity
- Rayleigh–Schrödinger perturbation theory (via (3.9))
- Perron–Frobenius theorem, product states of independent identical objects
- plane-wave diagonalization, graph Laplacian pseudo-inverse, lattice Green function asymptotics
- semiclassical band dynamics, local-slope (Taylor) expansion
