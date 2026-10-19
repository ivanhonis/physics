# The field made by a held source as a common local scale for a test body

- **Subproject:** 06-ilang-source
- **Package:** 05-made-field-scale
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-19

## Changes from previous version

- S6: the start of item 3 specified (branch $`\sigma`$ of the band symbol, momentum distribution centred at $`p=0`$); first order in the gradients quantified by $`\epsilon_g`$; new conditions (P) narrow momentum, with $`\theta_k`$, and (B) branch following, with $`\eta_k`$ (I1).
- Step 4: band symbol $`h_k`$ stated; (5.7) identified as the value at the band point $`p=0`$; new paragraphs "Packet" with (5.17) (drift acceleration of a start of finite momentum width, two-sided bound on its momentum correction, its level dependence, its errors) and "Branch following" (branch coupling, its bound $`\eta_k`$, the oscillating part, the drift window) (I1).
- Step 6, "Range of the acceleration" and "Signs": windows for $`w`$ extended by (P), (B) on the ring, sign of the packet value (I1).
- Result ((5.7), new (5.17), (5.11)–(5.14)), Consistency checks (dimensions), Open issues, Methods used: updated accordingly.

## Response to verification

- I1: Accepted and fixed in S6 ((P), (B), $`\epsilon_g`$), Step 4, paragraphs "Packet" and "Branch following", (5.17), and Step 6, "Range of the acceleration" and "Signs". The level and branch independence of (5.7) is now stated at the band point $`p=0`$; for a start of finite momentum width it holds up to the relative correction $`\epsilon_k`$ of (5.17), which is in general level dependent, with the errors of the $`x`$-averaging and of branch mixing stated.

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
- **S3 Test body.** Model D with positions $`x\in\ell`$, a line of $`X_f`$ (the whole ring for $`D=1`$; on the tori a line along a lattice direction $`\hat e_\ell`$, a cycle of $`L`$ places), labelled $`x=0,\dots,L-1`$ in the record $`K_x=\kappa\,x\,X`$ of a medium $`c`$; the bonds of the motion term are those of $`\ell`$, the closing bond $`(L-1,0)`$ included. $`C_{bc}`$ is the part of $`C`$ not involving the field: $`C_{\rm D}=A+B`$, the record term and the medium's own term $`C_c`$. Coupling (2.1), form (a) or (c). $`d_k=2\pi k/(N\lambda_0)`$, $`M_k=m+d_k`$, $`\lVert O\rVert=M_{N-1}`$.
- **S4 Start.** $`\Psi(0)=\xi\otimes\varphi`$ with any body–medium state $`\xi\in\mathcal H_{bc}=\mathcal H_b\otimes\mathcal H_c`$ and a field state $`\varphi`$; $`\varphi(\lambda):=e^{-iC_f^s\lambda}\varphi`$. Items 2–3 use a stationary $`\varphi`$ (an eigenvector of $`C_f^s`$), item 4 the lowest adapted state (Step 5).
- **S5 Positivity** (items 3–4). $`\nu(x):=1+\gamma N_\varphi(x)>0`$ on $`\ell`$, and $`1+\gamma n>0`$.
- **S6 Regime of item 3.** The setting of (4.16) of 05-ilang-free-fall/04-branch-fall: a branch start at rest on level $`k`$ and branch $`\sigma`$ of the band symbol $`h_k`$ (Step 4), its momentum distribution centred at $`p=0`$ ($`p\in(-\pi,\pi]`$ the Fourier label of the position label), its support of width $`w`$ around $`x_0`$; the record background with one step $`d_0\hat e`$ per bond, so the support does not contain the closing bond of $`\ell`$ (Step 6). *Gradient:* first order in $`\epsilon_g:=\lvert\gamma N'(x_0)\rvert/\nu(x_0)`$, the relative change of the half-gaps per label, with $`\epsilon_gw\ll1`$. **(P)** *Narrow momentum:* $`c_k\,\overline{\sin^2p}\ll1`$, i.e. $`\overline{\sin^2p}\ll\min(1,\theta_k^{-2})`$, with $`\overline{(\cdot)}`$ the mean over the momentum distribution of the start, $`\theta_k:=\tau_{\rm loc}(x_0)/M_{x_0,k}`$ the local ratio of hopping to half-gap and $`c_k`$ as in (5.17). **(B)** *Branch following:* $`\eta_k:=\tfrac14\theta_k\epsilon_g\ll1`$. *Local slope:* with the lattice slope $`N'(x):=\tfrac12\bigl(N_\varphi(x+1)-N_\varphi(x-1)\bigr)`$ and curvature $`N''(x):=N_\varphi(x+1)+N_\varphi(x-1)-2N_\varphi(x)`$, $`N_\varphi(x)=N_\varphi(x_0)+N'(x_0)(x-x_0)`$ on the support up to the curvature term, with $`\lvert N''\rvert w\ll\lvert N'(x_0)\rvert`$ on the support.

Notation: $`N_\lambda(x):=\langle\varphi(\lambda)\vert\Phi_x\vert\varphi(\lambda)\rangle`$, $`\delta\Phi_x:=\Phi_x-N_\lambda(x)`$, $`\sigma_\Phi(\lambda):=\max_{x\in\ell}\bigl(\mathrm{Var}_{\varphi(\lambda)}\Phi_x\bigr)^{1/2}`$. For stationary $`\varphi`$, $`N_\lambda=N_\varphi`$ and $`\sigma_\Phi`$ are constant.

## Derivation

### Step 1. The operator by which the test body evolves

By S2, on $`\mathcal H_{bc}\otimes\mathcal H_f`$ and up to a constant (a common phase, (1.2)), $`C=C_{bc}\otimes\mathbb 1+\mathbb 1\otimes C_f^s+\gamma\sum_{x\in\ell}Q_x\otimes\Phi_x`$. For a unit vector $`\varphi`$ define the partial expectation $`\bar C_\varphi`$ on $`\mathcal H_{bc}`$ by $`\langle\xi'\vert\bar C_\varphi\vert\xi\rangle:=\langle\xi'\otimes\varphi\vert C\vert\xi\otimes\varphi\rangle`$. Inserting $`C`$:

```math
\bar C_\varphi=C_{bc}+\gamma\sum_{x\in\ell}N_\varphi(x)\,Q_x+E_\varphi\mathbb 1,\qquad N_\varphi(x)=\langle\varphi\vert\Phi_x\vert\varphi\rangle,\quad E_\varphi=\langle\varphi\vert C_f^s\vert\varphi\rangle .
\qquad\text{(5.1)}
```

Let $`\xi(\lambda)`$ solve $`i\,\mathrm d\xi/\mathrm d\lambda=(\bar C_{\varphi(\lambda)}-E_\varphi)\xi`$ ($`E_{\varphi(\lambda)}=E_\varphi`$ is conserved) and $`\Psi_{\rm eff}:=\xi(\lambda)\otimes\varphi(\lambda)`$. The product rule gives $`i\dot\Psi_{\rm eff}=C\Psi_{\rm eff}-\gamma W_\lambda\Psi_{\rm eff}`$ with $`W_\lambda:=\sum_xQ_x\otimes\delta\Phi_x`$. Hence $`D:=\Psi-\Psi_{\rm eff}`$ obeys $`i\dot D=CD+\gamma W_\lambda\Psi_{\rm eff}`$, $`D(0)=0`$, and Duhamel's formula with the unitarity of $`e^{-iC\lambda}`$ gives $`\lVert D(\lambda)\rVert\le\lvert\gamma\rvert\int_0^{\lvert\lambda\rvert}\lVert W_{s\mu}\Psi_{\rm eff}(s\mu)\rVert\,\mathrm d\mu`$ along the actual trajectory, $`s:=\mathrm{sgn}\lambda`$. Write $`W\Psi_{\rm eff}=\sum_xv_x`$, $`v_x=Q_x\xi\otimes\delta\Phi_x\varphi`$, $`\lVert\delta\Phi_x\varphi\rVert^2=\mathrm{Var}\Phi_x`$.
- (a): $`Q_xQ_y=\delta_{xy}\Pi_xO^2`$, so $`\lVert\sum_xv_x\rVert^2=\sum_x\langle\xi\vert\Pi_xO^2\vert\xi\rangle\mathrm{Var}\Phi_x\le\lVert O\rVert^2\sigma_\Phi^2`$.
- (c): $`Q_x\xi`$ lies on the places $`x-1,x,x+1`$, so $`\langle v_x,v_y\rangle=0`$ for $`\lvert x-y\rvert\ge3`$ and $`\lVert\sum_xv_x\rVert^2\le5\sum_x\lVert v_x\rVert^2`$. With $`\lVert A_x\rVert=\tau/2`$, $`\lVert Q_x\xi\rVert\le(\lVert O\rVert+\frac\tau2)\lVert(\Pi_{x-1}+\Pi_x+\Pi_{x+1})\xi\rVert`$, whose squares sum to $`3`$.

These bounds hold for every unit $`\xi`$, so $`\lVert W_\lambda(\chi\otimes\varphi(\lambda))\rVert\le c_Q\sigma_\Phi(\lambda)`$ for every unit $`\chi\in\mathcal H_{bc}`$. Therefore

```math
\bigl\lVert\Psi(\lambda)-\xi(\lambda)\otimes\varphi(\lambda)\bigr\rVert\le\delta(\lambda):=\lvert\gamma\rvert\,c_Q\int_0^{\lvert\lambda\rvert}\sigma_\Phi(s\mu)\,\mathrm d\mu,\qquad c_{Q^{(a)}}=\lVert O\rVert,\quad c_{Q^{(c)}}=\sqrt{15}\,\bigl(\lVert O\rVert+\tfrac\tau2\bigr).
\qquad\text{(5.2)}
```

For stationary $`\varphi`$, $`\xi(\lambda)=e^{-i(\bar C_\varphi-E_\varphi)\lambda}\xi`$ and $`\delta(\lambda)=\lvert\gamma\rvert c_Q\sigma_\Phi\lvert\lambda\rvert`$. The neglected term $`\gamma W`$ is the change of the field by the test body (A15). (5.2) bounds the joint state; its error is first order in $`\gamma`$, like the retained term $`\gamma\sum_xN_\varphi(x)Q_x`$, so (5.2) alone does not fix the body's evolution at first order. The view of body and medium does.

*Reduced view.* Let $`\rho(\lambda):=\mathrm{Tr}_f\lvert\Psi(\lambda)\rangle\langle\Psi(\lambda)\rvert`$, the view (1.5) of body and medium, and $`H_\lambda:=\bar C_{\varphi(\lambda)}-E_\varphi`$. In $`\mathrm{Tr}_f`$ of $`i\,\mathrm d\lvert\Psi\rangle\langle\Psi\rvert/\mathrm d\lambda=[C,\lvert\Psi\rangle\langle\Psi\rvert]`$ the field's own term drops ($`\mathrm{Tr}_f[\mathbb 1\otimes X,Y]=0`$ for field operators $`X`$), and $`\Phi_x=N_\lambda(x)+\delta\Phi_x`$ gives $`i\,\mathrm d\rho/\mathrm d\lambda=[H_\lambda,\rho]+\gamma(G-G^\dagger)`$ with $`G:=\mathrm{Tr}_f\bigl(W_\lambda\lvert\Psi\rangle\langle\Psi\rvert\bigr)`$. $`\lvert\xi\rangle\langle\xi\rvert`$ obeys the same equation without $`G`$. With $`U`$ the unitary evolution of $`H_\lambda`$, $`\Delta:=\rho-\lvert\xi\rangle\langle\xi\rvert=-i\gamma\int_0^\lambda U(\lambda,\mu)(G-G^\dagger)(\mu)U(\lambda,\mu)^\dagger\,\mathrm d\mu`$, so $`\lVert\Delta(\lambda)\rVert_1\le2\lvert\gamma\rvert\int_0^{\lvert\lambda\rvert}\lVert G(s\mu)\rVert_1\,\mathrm d\mu`$. Split $`\lvert\Psi\rangle\langle\Psi\rvert=\lvert\Psi\rangle\langle\Psi_{\rm eff}\rvert+\lvert\Psi_{\rm eff}\rangle\langle D\rvert+\lvert D\rangle\langle D\rvert`$; the partial trace does not increase the trace norm.
- $`\mathrm{Tr}_f\bigl(W\lvert\Psi\rangle\langle\xi\otimes\varphi\rvert\bigr)=\lvert(\mathbb 1\otimes\langle\varphi\rvert)W\Psi\rangle\langle\xi\rvert`$, and $`(\mathbb 1\otimes\langle\varphi\rvert)W\Psi_{\rm eff}=\sum_xQ_x\xi\,\langle\varphi\vert\delta\Phi_x\vert\varphi\rangle=0`$: the first-order term vanishes after the field trace. What remains is $`\lvert(\mathbb 1\otimes\langle\varphi\rvert)WD\rangle\langle\xi\rvert`$, of trace norm $`\sup_{\lVert\chi\rVert=1}\lvert\langle W(\chi\otimes\varphi)\vert D\rangle\rvert\le c_Q\sigma_\Phi\lVert D\rVert`$.
- $`\bigl\lVert\mathrm{Tr}_f\bigl(W\lvert\Psi_{\rm eff}\rangle\langle D\rvert\bigr)\bigr\rVert_1\le\lVert W\Psi_{\rm eff}\rVert\,\lVert D\rVert\le c_Q\sigma_\Phi\lVert D\rVert`$.
- $`\bigl\lVert\mathrm{Tr}_f\bigl(W\lvert D\rangle\langle D\rvert\bigr)\bigr\rVert_1\le\lVert W\rVert\,\lVert D\rVert^2\le c_W\phi_{\max}\lVert D\rVert^2`$, with $`\phi_{\max}(\lambda):=\max_{x\in\ell}\lVert\Phi_x-N_\lambda(x)\rVert\le N_f`$, $`c_{W^{(a)}}=\lVert O\rVert`$ ($`W^{(a)}`$ is block diagonal in the places) and $`c_{W^{(c)}}=\lVert O\rVert+\tfrac{3\tau}2`$ (the bond terms $`A_x\otimes\tfrac12(\delta\Phi_x+\delta\Phi_{x+1})`$ fall into at most three classes of disjoint bonds, each of norm $`\le\tfrac\tau2\phi_{\max}`$).

With $`\lVert D(s\mu)\rVert\le\delta(s\mu)`$ and $`\mathrm d\delta(s\mu)/\mathrm d\mu=\lvert\gamma\rvert c_Q\sigma_\Phi(s\mu)`$, the first two terms integrate to $`2\delta(\lambda)^2`$:

```math
\bigl\lVert\rho(\lambda)-\lvert\xi(\lambda)\rangle\langle\xi(\lambda)\rvert\bigr\rVert_1\le2\delta(\lambda)^2+2\lvert\gamma\rvert c_W\int_0^{\lvert\lambda\rvert}\phi_{\max}(s\mu)\,\delta(s\mu)^2\,\mathrm d\mu\le2\delta(\lambda)^2\bigl(1+\lvert\gamma\rvert c_W\hat\phi(\lambda)\lvert\lambda\rvert\bigr),\qquad\hat\phi(\lambda):=\sup_{0\le\mu\le\lvert\lambda\rvert}\phi_{\max}(s\mu).
\qquad\text{(5.15)}
```

So the view of body and medium follows $`\bar C_{\varphi(\lambda)}`$ with no first-order error; the remainder is second order in $`\gamma`$, and every reading probability of body and medium differs by at most half of it. It is small for $`\delta(\lambda)\ll1`$ and $`\lvert\gamma\rvert c_W\hat\phi\lvert\lambda\rvert\,\delta(\lambda)^2\ll1`$; for stationary $`\varphi`$ this is $`\lvert\lambda\rvert\ll(\lvert\gamma\rvert c_Q\sigma_\Phi)^{-1}`$ and $`\lvert\gamma\rvert^3c_Wc_Q^2\phi_{\max}\sigma_\Phi^2\lvert\lambda\rvert^3\ll1`$. The second-order terms themselves (among them the test body's own mark, 06-own-mark) are not computed.

*M6.* $`\bar C_\varphi`$ and the view $`\rho`$ are computed from $`C`$ and the state alone. It is therefore unchanged by every relisting that leaves $`C`$ unchanged, e.g. $`\Phi_x\to\Phi_x-c_x`$ together with $`C_{\rm D}\to C_{\rm D}+\gamma\sum_xc_xQ_x`$, place-dependent $`c_x`$ included. It does not depend on the labels of the field objects ($`\Phi_x`$ is symmetric) or on the phase of $`\varphi`$, and its multiple of $`\mathbb 1`$ is a common phase. The split of $`\bar C_\varphi`$ into $`C_{bc}`$ and $`\gamma\sum_xN_\varphi(x)Q_x`$ is not fixed: the separate values of the bare blocks, of $`\gamma`$ and of $`N_\varphi(x)`$ depend on the listing.

### Step 2. Level blocks

*Extraction rule.* The position, branch and clock places of the body belong to its type (A2), and the clock levels $`\lvert f_k\rangle`$ are built from the clock places. Every term of $`\bar C_\varphi`$ acts on the clock label through $`\mathbb 1_N`$ or $`D`$, so $`\bar C_\varphi`$ is block diagonal in the levels. Its level-$`k`$ block between the places $`x'`$ and $`x`$, an operator on branch ⊗ medium, is therefore fixed by $`C`$ and $`\varphi`$: for $`x'=x`$ the on-site operator $`\mathfrak B_{x,k}`$, for $`x'=x+1`$ the hopping. The Pauli decomposition on the branch label, $`\mathfrak B_{x,k}=\sigma_3\otimes\hat M_{x,k}+\mathbb 1_2\otimes\hat V_{x,k}+\sigma_1\otimes(\cdot)+\sigma_2\otimes(\cdot)`$, is unique. From (5.1), since $`A`$ is off-diagonal in the places, $`\hat M_{x,k}=\nu(x)M_k\mathbb 1_c`$, $`\hat V_{x,k}=K_x+C_c+E_\varphi`$, and there is no $`\sigma_1,\sigma_2`$ part. No field coupling has a $`\mathbb 1_2`$ part on the branch label, so $`\hat V_{x,k}`$ does not depend on $`k`$, and depends on $`\varphi`$ only through the constant $`E_\varphi`$. Hence $`\hat V^{(0)}_x:=\hat V_{x,k}-E_\varphi`$ is a field-independent operator on the medium, fixed by $`C`$ up to a constant: the record background, $`K_x+C_c`$ in the listing of the setting, in which (4.16), (4.24) and R3 are stated. The effective on-site block is $`B_{x,k}:=\mathfrak B_{x,k}-\mathbb 1_2\otimes\hat V^{(0)}_x`$, a multiple of $`\mathbb 1_c`$ and thus a $`2\times2`$ block. The relisting $`C_{\rm D}\to C_{\rm D}+\sum_xf_x\Pi_x`$, $`K_x\to K_x-f_x\mathbb 1_c`$ with real place-dependent $`f_x`$ leaves $`C`$, $`\bar C_\varphi`$, $`\mathfrak B_{x,k}`$ and $`\hat V^{(0)}_x`$ unchanged, hence $`B_{x,k}`$; it only renames parts of $`\hat V^{(0)}_x`$. So does $`\Phi_x\to\Phi_x-c_x`$ with $`C_{\rm D}\to C_{\rm D}+\gamma\sum_xc_xQ_x`$, which changes $`C_{bc}`$ but adds no $`\mathbb 1_2`$ part.

*Blocks.* Let $`\hat\nu:=\sum_x\nu(x)\Pi_x`$ with $`\nu(x)=1+\gamma N_\varphi(x)`$. On level $`k`$, $`O=M_k\sigma_3`$. For (a), (5.1) gives $`\gamma\sum_xN_\varphi(x)\Pi_xO=(\hat\nu-1)B`$. For (c) it gives in addition $`\gamma\sum_xN_\varphi(x)\tfrac12(A_x+A_{x-1})=\gamma\sum_x\tfrac12(N_\varphi(x)+N_\varphi(x+1))A_x`$. Since $`A_x`$ connects only $`x`$ and $`x+1`$, $`\tfrac12\{\hat\nu,A_x\}=\tfrac12(\nu(x)+\nu(x+1))A_x`$. With the extraction rule, the level-$`k`$ blocks are

```math
\begin{aligned}
&B_{x,k}=M_{x,k}\sigma_3+V_{x,k}\mathbb 1_2,\qquad M_{x,k}=\nu(x)\,M_k,\qquad V_{x,k}=E_\varphi,\\
&\text{hopping on }(x,x+1):\ \tfrac{\tau_{x,x+1}}2(-i\sigma_1),\qquad \tau^{(a)}_{x,x+1}=\tau,\qquad \tau^{(c)}_{x,x+1}=\tau\,\tfrac12\bigl(\nu(x)+\nu(x+1)\bigr),
\end{aligned}
\qquad\text{(5.3)}
```

i.e. the Model D part of $`\bar C_\varphi`$ is $`\hat\nu B+A`$ for (a) and $`\tfrac12\{\hat\nu,C_{\rm D}\}`$ for (c). Fixed by $`C`$ and $`\varphi`$ (extraction rule): $`B_{x,k}`$ and the hopping amplitudes, i.e. $`M_{x,k}`$, the hopping amplitudes and $`V_{x,k}`$ up to the common constant. Hence the level-independent ratios $`\nu(y)/\nu(x)=M_{y,k}/M_{x,k}`$ are fixed. Listing-dependent: the factorization $`M_{x,k}=\nu(x)M_k`$ (a constant relisting $`c_x=c`$ multiplies $`M_k`$, and $`\tau`$ for (c), by $`1+\gamma c`$ and divides $`\nu`$ by it) and the place-independent constant $`E_\varphi`$ in $`V_{x,k}`$.

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

*Fall.* Under S6 the profiles across the start are those of 05-ilang-free-fall with base half-gap $`\nu(x_0)M_k`$, $`G_k=\gamma N'(x_0)M_k`$, $`\mathcal F_k=0`$, and hopping $`\tau_k=\tau_{\rm loc}(x_0)`$: $`\tau`$ for (a), $`\tau\nu(x_0)`$ for (c) up to first order in the gradient. The variation of the hopping across the start (c) does not enter at first order. The blocks (5.3) have the band symbol $`h_k(x,p)=E_\varphi+M_{x,k}\sigma_3-\tau_{\rm loc}(x)\sin p\,\sigma_1`$, with $`\tau_{\rm loc}(x)=\tau`$ (a), $`\tau\nu(x)`$ (c) at first order in the gradient, and the branch energies $`E_\sigma(x,p)=E_\varphi+\sigma\epsilon(x,p)`$, $`\epsilon=\sqrt{M_{x,k}^2+\tau_{\rm loc}(x)^2\sin^2p}`$. In them the hopping multiplies $`\sin^2p`$, whose $`x`$-derivative vanishes at rest. With (4.16) of 05-ilang-free-fall/04-branch-fall and (5.6):

```math
a_{k,\sigma}(0)=-\tau_{\rm loc}(x_0)^2\,\frac{\gamma N'(x_0)}{\nu(x_0)}=-\tau_{\rm loc}(x_0)^2\Bigl[\frac{r(x_0+1)-r(x_0)}{r(x_0)}-\frac{\gamma N''(x_0)}{2\nu(x_0)}\Bigr],\qquad v_{\max}(x_0):=\tau_{\rm loc}(x_0)\,d_0 .
\qquad\text{(5.7)}
```

The second equality is exact: by (5.6), $`(r(x_0+1)-r(x_0))/r(x_0)=\gamma\bigl(N_\varphi(x_0+1)-N_\varphi(x_0)\bigr)/\nu(x_0)`$, and $`N_\varphi(x_0+1)-N_\varphi(x_0)=N'(x_0)+\tfrac12N''(x_0)`$. $`a_{k,\sigma}(0)`$, the acceleration at the band point $`p=0`$, is the same for all levels and both branches, as (17.11) of 05-ilang-free-fall/17-typical-or-forced requires for R3 with $`\phi=0`$. Multiplying by $`d_0`$: (4.24) holds with the maximal speed $`v_{\max}(x_0)`$ of the effective contract at the start, up to the curvature term, i.e. to relative error $`\lvert N''(x_0)\rvert/(2\lvert N'(x_0)\rvert)`$, which is $`\ll1/w`$ by S6. For (a), $`v_{\max}(x_0)=\tau d_0`$ at every place. For (c), $`v_{\max}(x_0)=\tau\nu(x_0)d_0`$ changes from place to place by the factor of $`r`$; with the value at a fixed reference place $`y`$ instead, (4.24) acquires the factor $`(r(x_0)/r(y))^2`$. $`\tau_{\rm loc}`$ and $`\gamma N'/\nu=(M_{x_0+1,k}-M_{x_0-1,k})/(2M_{x_0,k})`$ are fixed by $`C`$ and $`\varphi`$.

*Packet.* For a start of finite momentum width, Ehrenfest's theorem for the band symbol gives, at first order in the gradients, the drift acceleration of the mean position label at $`\lambda=0`$ as the mean over the start of $`\alpha_k:=\{\partial_pE_\sigma,E_\sigma\}=\partial_x\partial_pE_\sigma\,\partial_pE_\sigma-\partial_p^2E_\sigma\,\partial_xE_\sigma`$. The Moyal corrections carry three $`x`$-derivatives (third order), and the band vectors of the real symbol $`h_k`$ are real, so there is no first-order Berry term. $`\alpha_k`$ does not depend on $`\sigma`$. With $`\mu:=M_{x,k}`$, $`T:=\tau_{\rm loc}(x)`$ and primes for $`x`$-derivatives, $`\alpha_k=-\bigl[T^2\cos2p\,(\mu\mu'+TT'\sin^2p)-\tfrac12T^3T'\sin^22p\bigr]/\epsilon^2`$; for (a) $`T'=0`$, for (c) $`T/\mu=\tau/M_k`$ is constant. At $`x_0`$ this is $`\alpha_k(x_0,p)=a_{k,\sigma}(0)f_k(p)`$ with $`f^{(a)}_k=\cos2p/(1+\theta_k^2\sin^2p)`$ and $`f^{(c)}_k=\cos2p-\theta_k^2\sin^22p/\bigl(2(1+\theta_k^2\sin^2p)\bigr)`$. Hence $`1-f^{(a)}_k=(2+\theta_k^2)\sin^2p/(1+\theta_k^2\sin^2p)`$ and $`1-f^{(c)}_k=2\sin^2p+2\theta_k^2\sin^2p\cos^2p/(1+\theta_k^2\sin^2p)`$, both in $`[0,c_k\sin^2p]`$. Averaging over the momentum distribution of the start (the $`p`$-marginal of its Wigner function):

```math
\bar a_{k,\sigma}=a_{k,\sigma}(0)\,(1-\epsilon_k),\qquad 0\le\epsilon_k\le c_k\,\overline{\sin^2p},\qquad c^{(a)}_k=2+\theta_k^2,\quad c^{(c)}_k=2+2\theta_k^2,
\qquad\text{(5.17)}
```

with $`\epsilon_k\simeq c_k\overline{\sin^2p}`$ for a narrow distribution. Evaluating $`\alpha_k`$ at $`x_0`$ instead of $`x`$ costs a relative error $`O\bigl((\epsilon_gw)^2+\epsilon_gw\,c_k(\overline{\sin^4p})^{1/2}\bigr)`$: the part linear in $`x-x_0`$ averages to zero except through its correlation with $`f_k`$, which Cauchy–Schwarz bounds. By the uncertainty relation $`w^2\,\overline{\sin^2p}\ge\tfrac14\overline{\cos p}^{\,2}`$ (from $`[x,\sin p]=i\cos p`$ on the lattice), (P) requires $`w\gg\max(1,\theta_k)`$ for a start concentrated near $`p=0`$. $`\epsilon_k`$ depends on the start and, through $`\theta_k`$, on the level. So the fall of a packet is level and branch independent, and obeys (4.24) with the curvature term of (5.7), up to the relative correction $`\epsilon_k`$, i.e. at zeroth order in (P). For two levels or branches with the same momentum distribution the relative difference of $`\bar a`$ is at most $`\bar c\,\overline{\sin^2p}/(1-\bar c\,\overline{\sin^2p})`$, $`\bar c:=\max(c_k,c_l)`$.

*Branch following.* The gradient couples the branches through $`\dot p\,\langle u_{-\sigma}\vert\partial_pu_\sigma\rangle`$ and $`\dot x\,\langle u_{-\sigma}\vert\partial_xu_\sigma\rangle`$, $`u_\pm`$ the band vectors of $`h_k`$. Since $`h_k-E_\varphi=\epsilon(\cos\vartheta\,\sigma_3-\sin\vartheta\,\sigma_1)`$ with $`\tan\vartheta=(T/\mu)\sin p`$, the $`u_\pm`$ rotate by $`\vartheta/2`$, and $`\lvert\langle u_{-\sigma}\vert\partial_pu_\sigma\rangle\rvert=\tfrac12\lvert\partial_p\vartheta\rvert\le\theta_k/2`$ at $`x_0`$. With $`\lvert\dot p\rvert=\lvert\partial_xE_\sigma\rvert`$ and the branch gap $`2\epsilon`$, the first coupling over the gap is at most $`\eta_k`$ for both couplings; the second is smaller by $`\theta_k^2\sin^2p`$ for (a) and vanishes for (c), where $`T/\mu`$ is constant. Under (B) the adiabatic theorem keeps the start on branch $`\sigma`$ up to an amplitude $`O(\eta_k)`$ on $`-\sigma`$. Its interference with branch $`\sigma`$ adds to $`\bar x`$ a part oscillating with the branch frequency $`2\epsilon\approx2M_{x_0,k}`$, which the drift of (4.24), a mean over a window $`\Delta\lambda\gg\pi/M_{x_0,k}`$, removes. The remaining corrections to the drift acceleration are of second order in the gradient, relative $`O(\epsilon_g^2+\eta_k^2)`$, and the population $`O(\eta_k^2)`$ passed to $`-\sigma`$ falls with $`a_{k,-\sigma}(0)=a_{k,\sigma}(0)`$. The window must also keep the momentum gained, $`\lvert\dot p\rvert\Delta\lambda\simeq\epsilon_gM_{x_0,k}\Delta\lambda`$, within (P); both requirements can be met since $`\epsilon_g\ll1`$ and $`\epsilon_g\theta_k\ll1`$ by S6.

### Step 5. The made field in the lowest adapted state

Without pair terms among the field objects, $`C_f^s=\sum_jh^{(j)}`$ with $`h=C_1+g_s\lvert x_s\rangle\langle x_s\rvert`$. $`h`$ has off-diagonal entries $`-t_f\le0`$ on a connected graph, so by Perron–Frobenius its lowest eigenvector $`u_g`$ is unique and positive, for every real $`g_s`$. The lowest state of $`C_f^s`$ is then $`u_g^{\otimes N_f}`$, which is symmetric and unique. In it the $`N_f`$ objects are independent: $`N(y)=N_fu_g(y)^2`$ and $`\mathrm{Var}\Phi_y=N_fu_g(y)^2(1-u_g(y)^2)\le N(y)`$. In (5.2), $`\sigma_\Phi^2\le\max_yN(y)`$.

Apply (3.9) to one field object ($`\Phi_y\to\lvert y\rangle\langle y\rvert`$, $`v=\lvert g_s\rvert`$). The eigenvectors of $`C_1`$ are the plane waves $`\lvert X_f\rvert^{-1/2}e^{i\mathbf k\cdot x}`$ with eigenvalues $`-2Dt_f+t_f\omega(\mathbf k)`$; the lowest is uniform, with gap $`t_f\omega_{\min}`$, $`\omega_{\min}=4\sin^2(\pi/L)`$. In (3.6) each term is $`\lvert X_f\rvert^{-2}e^{i\mathbf k\cdot(y-x_s)}/(t_f\omega(\mathbf k))`$, so $`\chi_0=\frac{2}{\lvert X_f\rvert t_f}\Lambda^+`$. Multiplying by $`N_f`$:

```math
N(y)=n-\frac{2n\,g_s}{t_f}\,\Lambda^+(y,x_s)+O\Bigl(\frac{N_fg_s^2}{t_f^2\omega_{\min}^2}\Bigr),\qquad \delta N(y):=N(y)-n,
\qquad\text{(5.8)}
```

with the kernel $`\frac{2n}{t_f}\Lambda^+`$ of (4.4). (3.9) is used with $`v=\lvert g_s\rvert`$ and the gap $`\Delta_0=t_f\omega_{\min}`$, under **(W1)** $`\lvert g_s\rvert\ll t_f\omega_{\min}`$, with $`\omega_{\min}\approx4\pi^2/L^2`$ for $`L\gg1`$: at fixed $`g_s`$ it fails as $`L`$ grows, and the large-$`L`$ forms below are used at finite $`L`$ within (W1). $`R_N\lesssim N_fg_s^2/(t_f\omega_{\min})^2`$ denotes the remainder of (5.8) at one place. On the ring, with $`\varrho\in[0,L/2]`$ the ring distance from $`x_s`$,

```math
\Lambda^+(x,x_s)=\frac{L^2-1}{12L}-\frac{\varrho(L-\varrho)}{2L}.
\qquad\text{(5.9)}
```

Check: for $`G:=`$ (5.9), $`(\Lambda G)(x)=2G(x)-G(x+1)-G(x-1)`$ is $`-1/L`$ for $`\varrho\neq0`$ (the second difference of $`-\varrho(L-\varrho)/(2L)`$ is $`+1/L`$) and $`1-1/L`$ at $`\varrho=0`$, so $`\Lambda G=\delta_{x_s}-1/L`$; the constant makes $`\sum_xG=0`$, which fixes $`\Lambda^+\delta_{x_s}`$. On the tori, with $`\vec\varrho=x-x_s`$ (nearest image) and $`\varrho=\lvert\vec\varrho\rvert`$, the standard asymptotics of the lattice Green function give, for $`1\ll\varrho\ll L`$,

```math
\Lambda^+(x,x_s)=c_L-\frac{\ln\varrho}{2\pi}+O(\varrho^{-2})+O\Bigl(\frac{\varrho^2}{L^2}\Bigr)\ (D=2),\qquad \Lambda^+(x,x_s)=\frac{1}{4\pi\varrho}-c_L'+O(\varrho^{-3})+O\Bigl(\frac{\varrho^2}{L^3}\Bigr)\ (D=3),
\qquad\text{(5.10)}
```

with constants $`c_L,c'_L`$ and gradients given by the term-by-term derivatives.

### Step 6. Dependence on the place relative to the source

By (5.6) and (5.7), exactly, $`r(y)/r(x)-1=\gamma(N(y)-N(x))/\nu(x)`$ and $`a_{k,\sigma}(0)=-\tau_{\rm loc}(x_0)^2\gamma N'(x_0)/\nu(x_0)`$. Let $`\bar\gamma:=\gamma/(1+\gamma n)`$, which has the sign of $`\gamma`$ by S5, and $`\tau_0:=\tau`$ (a), $`\tau_0:=\tau(1+\gamma n)`$ (c). Then $`\nu(x)=(1+\gamma n)(1+\bar\gamma\,\delta N(x))`$, $`\tau_{\rm loc}(x_0)=\tau_0(1+\bar\gamma\,\delta N(x_0))`$ for (c), and exactly

```math
\frac{r(y)}{r(x)}-1=\frac{\bar\gamma\bigl(\delta N(y)-\delta N(x)\bigr)}{1+\bar\gamma\,\delta N(x)},\qquad a_{k,\sigma}(0)=-\tau_0^2\,\bar\gamma\,N'(x_0)\times\begin{cases}\bigl(1+\bar\gamma\,\delta N(x_0)\bigr)^{-1}&\text{(a)},\\ 1+\bar\gamma\,\delta N(x_0)&\text{(c)}.\end{cases}
```

Let $`\varepsilon_\nu:=\lvert\bar\gamma\rvert\max_{y\in\ell}\lvert\delta N(y)\rvert`$. The expansion needs **(W2)** $`\varepsilon_\nu\ll1`$, which for $`\delta N\not\equiv0`$ fails as $`1+\gamma n\to0`$, where $`\bar\gamma`$ diverges; on the ring, by (5.9), $`\varepsilon_\nu\le\lvert\bar\gamma\rvert\bigl(\frac{n\lvert g_s\rvert}{t_f}\frac{L^2-1}{6L}+R_N\bigr)`$. Expanding in $`\varepsilon_\nu`$ and inserting (5.8), with $`\partial_\ell`$ the central difference along $`\ell`$ (as $`N'`$ in S6):

```math
\frac{r(y)}{r(x)}=1+\frac{2n\bar\gamma g_s}{t_f}\bigl[\Lambda^+(x,x_s)-\Lambda^+(y,x_s)\bigr]\bigl(1+O(\varepsilon_\nu)\bigr)+O\bigl(\lvert\bar\gamma\rvert R_N\bigr),
\qquad\text{(5.11)}
```

```math
a_{k,\sigma}(0)\big\vert_{x_0}=\frac{2n\bar\gamma g_s}{t_f}\,\tau_0^2\;\partial_\ell\Lambda^+(x_0,x_s)\bigl(1+O(\varepsilon_\nu)\bigr)+O\bigl(\tau_0^2\lvert\bar\gamma\rvert R_N\bigr).
\qquad\text{(5.12)}
```

The leading terms are of first order in $`g_s`$; the errors are the lapse expansion (relative, $`O(\varepsilon_\nu)`$) and the remainder of (5.8) (absolute). With (5.9) on the ring ($`\varrho_x`$ the ring distance of $`x`$ from $`x_s`$, a graph separation; $`a`$ counted positive away from the source along the shorter arc), the leading terms are

```math
\frac{r(y)}{r(x)}=1+\frac{n\bar\gamma g_s}{t_fL}\bigl[\varrho_y(L-\varrho_y)-\varrho_x(L-\varrho_x)\bigr],\qquad a_{k,\sigma}(0)=-\frac{n\bar\gamma g_s}{t_f}\,\tau_0^2\Bigl(1-\frac{2\varrho}{L}\Bigr).
\qquad\text{(5.13)}
```

With (5.10) on the tori, to leading order in $`1\ll\varrho\ll L`$ ($`\vec\varrho=x-x_s`$ the nearest-image coordinate difference, $`\varrho`$ its Euclidean norm, not the $`\ell^1`$ graph distance; $`\varrho_\parallel:=\hat e_\ell\cdot\vec\varrho`$):

```math
\frac{r(y)}{r(x)}=1+\frac{n\bar\gamma g_s}{\pi t_f}\ln\frac{\varrho_y}{\varrho_x},\quad a=-\frac{n\bar\gamma g_s\tau_0^2}{\pi t_f}\frac{\hat e_\ell\cdot\vec\varrho}{\varrho^2}\ (D=2);\qquad \frac{r(y)}{r(x)}=1+\frac{n\bar\gamma g_s}{2\pi t_f}\Bigl(\frac1{\varrho_x}-\frac1{\varrho_y}\Bigr),\quad a=-\frac{n\bar\gamma g_s\tau_0^2}{2\pi t_f}\frac{\hat e_\ell\cdot\vec\varrho}{\varrho^3}\ (D=3).
\qquad\text{(5.14)}
```

*Range of the acceleration (S6).* On the ring, for $`x\neq x_s`$, $`\Lambda^+(\cdot,x_s)`$ is quadratic along $`\ell`$ with second difference $`+1/L`$, and its central-difference slope in the direction away from $`x_s`$ is exactly $`-(\tfrac12-\varrho/L)`$; at $`x_s`$ it has a kink (second difference $`-(1-1/L)`$). So (5.13) is the local-slope value of the first-order profile without further error. S6 requires $`w\ll\varrho`$ and $`\lvert N''\rvert w\ll\lvert N'\rvert`$, i.e. $`w\ll L/2-\varrho`$. (P) adds $`w\gg\max(1,\theta_k)`$ (Step 4), so the window is $`\max(1,\theta_k)\ll w\ll\min(\varrho,L/2-\varrho)`$. At leading order $`\epsilon_g=\lvert\bar\gamma\rvert\frac{n\lvert g_s\rvert}{t_f}\bigl(1-\frac{2\varrho}L\bigr)`$, so $`\epsilon_gw\ll1`$ and (B) hold when $`\lvert\bar\gamma\rvert n\lvert g_s\rvert/t_f\ll\min(w^{-1},\theta_k^{-1})`$. The curvature term of (5.7) is a correction of first order in $`g_s`$ to (4.24), of relative size $`1/(L-2\varrho)`$. On the tori the leading forms give a slope along $`\ell`$ proportional to $`\varrho_\parallel/\varrho^D`$ and $`\lvert\partial_\ell^2N\rvert/\lvert\partial_\ell N\rvert=\lvert\varrho^2-D\varrho_\parallel^2\rvert/(\varrho^2\lvert\varrho_\parallel\rvert)\le(D-1)/\lvert\varrho_\parallel\rvert`$. The directional condition of S6 thus holds for $`w\ll\lvert\varrho_\parallel\rvert`$ (which implies $`w\ll\varrho`$), and fails near the foot point $`\varrho_\parallel=0`$ of $`x_s`$ on $`\ell`$, where the slope along $`\ell`$ vanishes. With (P) the window is $`\max(1,\theta_k)\ll w\ll\lvert\varrho_\parallel\rvert`$.

*Signs (graph coordinates).* By the exact forms above and S5, $`\mathrm{sgn}\bigl(r(y)/r(x)-1\bigr)=\mathrm{sgn}\bigl(\gamma(N(y)-N(x))\bigr)`$ and $`\mathrm{sgn}a_{k,\sigma}(0)=-\mathrm{sgn}\bigl(\gamma N'(x_0)\bigr)`$; (W2) is not needed. Under (P), $`1-\epsilon_k>0`$ in (5.17), so the packet value has the same sign. These are the signs of the leading terms of (5.11), (5.12) when $`R_N<\frac{n\lvert g_s\rvert}{t_f}\lvert\Lambda^+(x,x_s)-\Lambda^+(y,x_s)\rvert`$, resp. $`R_N<\frac{2n\lvert g_s\rvert}{t_f}\lvert\partial_\ell\Lambda^+(x_0,x_s)\rvert`$. With $`R_N\lesssim N_fg_s^2/(t_f\omega_{\min})^2`$ and $`N_f=n\lvert X_f\rvert`$, sufficient conditions are $`\lvert g_s\rvert\ll t_f\omega_{\min}^2\lvert\Lambda^+(x,x_s)-\Lambda^+(y,x_s)\rvert/\lvert X_f\rvert`$, resp. $`\lvert g_s\rvert\ll t_f\omega_{\min}^2\lvert\partial_\ell\Lambda^+(x_0,x_s)\rvert/\lvert X_f\rvert`$; they imply (W1), since $`\lvert\Lambda^+(x,y)\rvert\le\lVert\Lambda^+\rVert=1/\omega_{\min}`$. $`\Lambda^+(\cdot,x_s)`$ decreases with $`\varrho`$: exactly on the ring for $`0\le\varrho\le L/2`$ by (5.9), and in the leading forms (5.10) on the tori. Hence, under these conditions, for $`g_s\gamma>0`$ the clock runs slower at smaller $`\varrho`$ and the drift acceleration points to decreasing $`\varrho`$: on the ring along the shorter arc towards $`x_s`$, on the tori along $`\ell`$ towards the foot point. For $`g_s\gamma<0`$ both reverse.

*Graph separation and recorded distance.* $`\varrho`$, $`\vec\varrho`$ and "towards" above are positions in the field graph. The record $`K_x=\kappa\,x\,X`$ fixes recorded positions only on $`\ell`$: in the background of (4.24) the recorded position moves by $`d_0\hat e`$ per label step on every bond of $`\ell`$ except the closing bond $`(L-1,0)`$, whose record increment is $`-\kappa(L-1)X`$ instead of $`\kappa X`$; across it the background of (4.16) and (4.24) does not hold (S6). The setting fixes no record of the source; for $`x_s\in\ell`$ its recorded position is taken as that of the label $`x_s`$. For labels of $`\ell`$ with label separation $`s\in\{0,\dots,L-1\}`$ the recorded distance is $`d_0s`$, while their graph separation along $`\ell`$ is $`\min(s,L-s)`$; the two coincide iff $`s\le L/2`$.

*Ring.* With $`s:=\lvert x_0-x_s\rvert`$, $`\varrho=\min(s,L-s)`$ and $`\varrho(L-\varrho)=s(L-s)`$, the leading terms of (5.13) read in recorded terms

```math
\frac{r(y)}{r(x)}=1+\frac{n\bar\gamma g_s}{t_fL}\bigl[s_y(L-s_y)-s_x(L-s_x)\bigr],\qquad a^{\rm rec}_{k,\sigma}(0)=\frac{n\bar\gamma g_s}{t_f}\,\tau_0^2\Bigl(1-\frac{2s}{L}\Bigr),
\qquad\text{(5.16)}
```

with $`a^{\rm rec}`$ counted positive towards the recorded position of $`x_s`$, the errors of (5.11), (5.12), and starts whose support contains neither $`x_s`$ nor the closing bond. For $`s<L/2`$ the recorded and the graph statements agree. For $`s>L/2`$ the shorter arc crosses the closing bond: for $`g_s\gamma>0`$ the fall is towards the source in the graph but away from it in the recorded geometry, and along $`\ell`$ the clock is slower at larger recorded distance from $`x_s`$.

*Tori.* With $`\vec\varrho_\perp:=\vec\varrho-\varrho_\parallel\hat e_\ell`$: the record fixes the recorded distance $`d_0s_\parallel`$ from $`x_0`$ to the foot point of $`x_s`$ on $`\ell`$, $`s_\parallel`$ the label separation ($`s_\parallel=\lvert\varrho_\parallel\rvert`$ iff $`s_\parallel\le L/2`$). The transverse separation $`\vec\varrho_\perp`$, and with it $`\varrho`$, has no recorded counterpart in this setting, so the size of (5.14) depends on graph quantities that the record does not fix. In recorded terms (5.14) says, for $`g_s\gamma>0`$ and $`s_\parallel<L/2`$: along $`\ell`$ the fall points to the foot point and the clock is slower nearer to it; for $`s_\parallel>L/2`$ both are reversed in the recorded geometry, as on the ring.

## Result

- **(5.1), (5.2), (5.15)** [theorem]. Class: couplings (a) and (c); every field state $`\varphi`$; product starts $`\xi\otimes\varphi`$ with every body–medium state $`\xi`$ (S1–S4); every real $`\lambda`$, $`s=\mathrm{sgn}\lambda`$. The view of body and medium equals $`\lvert\xi(\lambda)\rangle\langle\xi(\lambda)\rvert`$, with $`\xi`$ evolving by the partial expectation $`\bar C_{\varphi(\lambda)}`$ of the total contract in the field state (5.1), up to a trace-norm remainder of at most $`2\delta(\lambda)^2\bigl(1+\lvert\gamma\rvert c_W\hat\phi(\lambda)\lvert\lambda\rvert\bigr)`$ (5.15). The first-order term vanishes after the field trace, so this remainder is second order in $`\gamma`$; it is small for $`\delta\ll1`$ and $`\lvert\gamma\rvert c_W\hat\phi\lvert\lambda\rvert\delta^2\ll1`$. The joint state equals $`\xi(\lambda)\otimes\varphi(\lambda)`$ up to a common phase and a remainder of norm at most $`\delta(\lambda)=\lvert\gamma\rvert c_Q\int_0^{\lvert\lambda\rvert}\sigma_\Phi(s\mu)\,\mathrm d\mu`$ (5.2), first order in $`\gamma`$: the test body's change of the field. For stationary $`\varphi`$ the operator is $`\lambda`$-independent and $`\delta=\lvert\gamma\rvert c_Q\sigma_\Phi\lvert\lambda\rvert`$; in the lowest adapted state $`\sigma_\Phi^2\le\max_yN(y)`$ and $`\hat\phi\le N_f`$. $`\bar C_\varphi`$ and the view are fixed by $`C`$ and the state; the split of $`\bar C_\varphi`$ into own and field-made parts is not.
- **(5.3)** [formula]. Same class. Extraction rule (Step 2): $`B_{x,k}`$ is the level-$`k`$ on-site operator of $`\bar C_\varphi`$ minus its field-independent scalar background $`\hat V^{(0)}_x`$, which is $`K_x+C_c`$ in the listing of the setting. The level-$`k`$ blocks are: on-site $`\nu(x)M_k\sigma_3+E_\varphi\mathbb 1_2`$; hopping $`\tau`$ for (a) and $`\tau\frac12(\nu(x)+\nu(x+1))`$ for (c). Fixed by $`C`$ and $`\varphi`$: $`B_{x,k}`$, also under place-dependent relistings between body term and record term, and the hopping amplitudes; hence $`M_{x,k}`$, $`V_{x,k}`$ up to a common constant, and the ratios $`M_{y,k}/M_{x,k}=\nu(y)/\nu(x)`$. Listing-dependent: the factorization $`M_{x,k}=\nu(x)M_k`$ and the place-independent constant in $`V_{x,k}`$.
- **(5.4)** [theorem]. Class: (a) and (c), every field state, every place (at every $`\lambda`$). R3 holds with $`\Gamma(x)=\gamma(N_\varphi(x+1)-N_\varphi(x))\sigma_3`$, without a $`\mathbb 1_2`$ part. In fixed quantities, $`B_{x+1,k}-B_{x,k}=M_{x,k}\frac{\nu(x+1)-\nu(x)}{\nu(x)}\sigma_3`$ for $`\nu(x)\neq0`$. The hopping changes by the same factor as the on-site blocks for (c), with the bond carrying the mean $`\frac12(\nu(x)+\nu(x+1))`$ of the factors of its ends. For (a) it does not: the hopping stays $`\tau`$ at every place, and the factors differ wherever $`\gamma(N_\varphi(x+1)-N_\varphi(x))\neq0`$. No field state violates R3 for (a) or (c); the control is (5.5).
- **(5.5)** [negative]. Control: the pair term $`\gamma\sum_x\Pi_x\sigma_3\otimes m\mathbb 1_N\otimes\Phi_x`$ (rest term only). R3 fails at every place with $`\gamma(N_\varphi(x+1)-N_\varphi(x))\neq0`$, and there the fall from rest (under S6) depends on the level.
- **(5.6)** [formula]. Class: (a), (c), stationary $`\varphi`$, S5. The clock-rate ratio of two places is $`r(y)/r(x)=\nu(y)/\nu(x)=M_{y,k}/M_{x,k}`$, the same for every pair of levels and for both branches. It is exact in $`\bar C_\varphi`$.
- **(5.7)** [theorem]. Class: (a), (c), stationary $`\varphi`$, branch starts at rest, S5–S6; first order in the gradients. At the band point $`p=0`$, $`a_{k,\sigma}(0)=-\tau_{\rm loc}(x_0)^2\,\gamma N'(x_0)/\nu(x_0)`$ with the lattice slope $`N'`$, the same for all levels and both branches. (4.24) of 05-ilang-free-fall/04-branch-fall holds with $`v_{\max}(x_0)=\tau_{\rm loc}(x_0)d_0`$ up to the curvature term of (5.7), of relative size $`\lvert N''(x_0)\rvert/(2\lvert N'(x_0)\rvert)`$. For (a) $`v_{\max}(x_0)`$ is $`\tau d_0`$ at every place. For (c) it is $`\tau\nu(x_0)d_0`$, which changes from place to place by the factor of $`r`$; with a place-independent $`v_{\max}`$ taken at a reference place $`y`$, (4.24) carries the factor $`(r(x_0)/r(y))^2`$.
- **(5.17)** [theorem]. Class: as (5.7), with (P) and (B) of S6. A start of finite momentum width has the drift acceleration $`\bar a_{k,\sigma}=a_{k,\sigma}(0)(1-\epsilon_k)`$ with $`0\le\epsilon_k\le c_k\overline{\sin^2p}`$, $`c_k=2+\theta_k^2`$ for (a) and $`2+2\theta_k^2`$ for (c), $`\theta_k=\tau_{\rm loc}(x_0)/M_{x_0,k}`$, up to relative errors $`O\bigl((\epsilon_gw)^2+\epsilon_gw\,c_k(\overline{\sin^4p})^{1/2}+\eta_k^2\bigr)`$; the branch oscillation at frequency $`\approx2M_{x_0,k}`$, of amplitude controlled by $`\eta_k`$, is not part of the drift. $`\epsilon_k`$ depends on the start and, through $`\theta_k`$, on the level: the fall of a packet is level and branch independent, and obeys (4.24) with the curvature term of (5.7), up to the relative correction $`\epsilon_k`$, i.e. at zeroth order in $`c_k\overline{\sin^2p}`$. For a start concentrated near $`p=0`$, (P) requires $`w\gg\max(1,\theta_k)`$.
- **(5.8), (5.9)** [formula]. The lowest adapted state is $`u_g^{\otimes N_f}`$, unique for every real $`g_s`$. Under (W1) $`\lvert g_s\rvert\ll t_f\omega_{\min}`$, in it $`N(y)=n-\frac{2ng_s}{t_f}\Lambda^+(y,x_s)`$ up to $`R_N\lesssim N_fg_s^2/(t_f\omega_{\min})^2`$, with $`\Lambda^+`$ on the ring given exactly by (5.9).
- **(5.11), (5.12)** [formula]. Class: (a), (c), lowest adapted state, S5, (W1) (and S6 for the acceleration). Clock-rate ratio $`1+\frac{2n\bar\gamma g_s}{t_f}[\Lambda^+(x,x_s)-\Lambda^+(y,x_s)]`$; acceleration at $`p=0`$ $`\frac{2n\bar\gamma g_s}{t_f}\tau_0^2\partial_\ell\Lambda^+(x_0,x_s)`$, level and branch independent (for a start of finite momentum width with the relative correction $`\epsilon_k`$ of (5.17)); first order in $`g_s`$, with $`\bar\gamma=\gamma/(1+\gamma n)`$ and $`\tau_0`$ the source-free hopping of $`\bar C_\varphi`$, up to a relative error $`O(\varepsilon_\nu)`$, small under (W2) $`\varepsilon_\nu\ll1`$, and an absolute error $`O(\lvert\bar\gamma\rvert R_N)`$ ($`O(\tau_0^2\lvert\bar\gamma\rvert R_N)`$ for the acceleration).
- **(5.13), (5.14)** [formula, criterion]. Graph coordinates, with the errors of (5.11), (5.12). Ring: (5.13), exact in $`L`$ for the first-order profile; the acceleration is its local-slope value, for $`w\ll\min(\varrho,L/2-\varrho)`$, and with (P) $`\max(1,\theta_k)\ll w`$. Square and cubic tori, leading forms for $`1\ll\varrho\ll L`$ ($`\varrho`$ the Euclidean norm of the coordinate difference): (5.14), with the logarithm ($`D=2`$) and $`1/\varrho`$ ($`D=3`$) in the clock ratio, and the acceleration along $`\ell`$ the projection on $`\hat e_\ell`$ of a radial vector of size $`\propto\varrho^{-1}`$ ($`D=2`$), $`\propto\varrho^{-2}`$ ($`D=3`$), for $`w\ll\lvert\varrho_\parallel\rvert`$, and with (P) $`\max(1,\theta_k)\ll w`$. Signs, with S5 and without (W2): the clock-rate difference has the sign of $`\gamma(N(y)-N(x))`$ and the acceleration that of $`-\gamma N'(x_0)`$, also its packet value (5.17) under (P). When $`R_N`$ is below the first-order differences (sufficient: $`\lvert g_s\rvert\ll t_f\omega_{\min}^2\lvert\Lambda^+(x,x_s)-\Lambda^+(y,x_s)\rvert/\lvert X_f\rvert`$, resp. the same with $`\lvert\partial_\ell\Lambda^+(x_0,x_s)\rvert`$): for $`g_s\gamma>0`$ the clock is slower at smaller graph separation $`\varrho`$ and the fall points to decreasing $`\varrho`$ (ring: along the shorter arc; tori: along $`\ell`$ towards the foot point of $`x_s`$); for $`g_s\gamma<0`$ the clock is faster nearer the source and the fall points away from it.
- **(5.16)** [criterion]. Recorded geometry. On $`\ell`$ the recorded distance $`d_0s`$ (label separation $`s`$) and the graph separation $`\min(s,L-s)`$ coincide iff $`s\le L/2`$. On the ring, in terms of $`s=\lvert x_0-x_s\rvert`$, the leading terms are (5.16), for starts whose support contains neither $`x_s`$ nor the closing bond $`(L-1,0)`$. Under the sign conditions of (5.13) and for $`g_s\gamma>0`$, the fall is towards the recorded position of $`x_s`$ for $`s<L/2`$ and away from it for $`s>L/2`$, where the shorter arc crosses the closing bond. On the tori the record fixes only the recorded distance $`d_0s_\parallel`$ along $`\ell`$ to the foot point of $`x_s`$; the transverse separation $`\vec\varrho_\perp`$ has no recorded counterpart in the setting, so the size of (5.14) is a function of graph coordinates.

## Consistency checks

- **Dimensions.** $`\gamma`$ and $`n,\Lambda^+`$ are numbers; $`g_s,t_f,\tau,M_k`$ have the dimension of $`C`$, i.e. $`1/\lambda`$. Then $`n\bar\gamma g_s/t_f`$, $`\delta=\lvert\gamma\rvert c_Q\sigma_\Phi\lvert\lambda\rvert`$ and $`\lvert\gamma\rvert c_W\phi_{\max}\lvert\lambda\rvert`$ are dimensionless, and $`a\propto\tau_0^2`$ has the dimension of label$`/\lambda^2`$; $`\theta_k=\tau_{\rm loc}/M_{x_0,k}`$, $`\epsilon_g`$, $`\eta_k`$ and $`c_k\overline{\sin^2p}`$ are dimensionless. Passed.
- **$`g_s=0`$ or $`\gamma=0`$.** For $`g_s=0`$, (5.8) gives $`N=n`$ uniform, hence $`\Gamma=0`$, $`r(y)/r(x)=1`$ and $`a=0`$ in (5.11)–(5.14) and (5.16). For $`\gamma=0`$, $`\bar C_\varphi=C_{bc}+E_\varphi`$ and the bounds (5.2), (5.15) vanish. Passed.
- **Sharp field.** Take $`t_f=0`$ and $`\varphi`$ a joint eigenvector of all $`\Phi_x`$. Then $`\varphi`$ is stationary, $`\sigma_\Phi=0`$, (5.2) and (5.15) are exact, and $`C(\xi\otimes\varphi)=(\bar C_\varphi\xi)\otimes\varphi`$ directly: the given lapse field of 05-ilang-free-fall with on-site factor $`1+\gamma N(x)`$. Passed.

## Open issues

- The bounds (5.2) and (5.15) grow with $`\lvert\lambda\rvert`$, and (5.15) contains $`\phi_{\max}\le N_f`$, which is crude for many field objects. A bound that uses the field gap $`t_f\omega_{\min}`$ (a non-growing first-order joint-state remainder plus a second-order shift, which is the test body's own mark of 06-own-mark) is not derived.
- The remainder $`R_N`$ of (5.8), taken from (3.9) per field object, is crude; the sign conditions it gives shrink fast with $`L`$. A sharp estimate of the second-order profile is not derived.
- Non-product starts, and non-stationary field states for items 3–4 (a $`\lambda`$-dependent profile), are not treated.
- The branch oscillation of $`\bar x`$ (amplitude $`O(\eta_k)`$), excluded from the drift, and the second-order corrections $`O(\epsilon_g^2+\eta_k^2)`$ to the packet fall are not computed.
- Regions with $`\nu(x)\le0`$ or without (W2), the neighbourhoods $`\varrho\lesssim w`$ of the source, the ring antipode, $`\varrho\sim L`$ and the foot point $`\lvert\varrho_\parallel\rvert\lesssim w`$ on the tori, and starts across the closing bond of $`\ell`$ are outside the formulas.
- The setting fixes no record of the source and no recorded transverse separation on the tori; a recorded distance to a source off $`\ell`$ would need a record beyond the single line $`\ell`$, which is not part of the setting.

## Methods used

- partial expectation (mean field) over the field state
- Duhamel formula, unitarity
- partial trace and trace-norm estimate of the reduced view
- Pauli decomposition of on-site operators
- Rayleigh–Schrödinger perturbation theory (via (3.9))
- Perron–Frobenius theorem, product states of independent identical objects
- plane-wave diagonalization, graph Laplacian pseudo-inverse, lattice Green function asymptotics
- semiclassical band dynamics, local-slope (Taylor) expansion
- Ehrenfest theorem for the band symbol (Weyl–Moyal), adiabatic theorem, lattice uncertainty relation
