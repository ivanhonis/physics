# What a body presents to a field object: the source at first order in the coupling

- **Subproject:** 06-ilang-source
- **Package:** 02-what-a-body-presents
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-19

## Setup and assumptions

**Objects and contract** (question, "Setting"; each an assumption of the package, M8). A Model D body $`b`$ on a chain of $`n`$ position labels (A1), a medium $`c`$, a field object $`f`$ of any finite type ($`d_f=\dim\mathcal H_f`$) with self-adjoint $`C_f`$ and $`\Phi_x`$. Each object is the only instance of its type, so (1.11) imposes nothing and $`\mathcal H_{\rm adm}=\mathcal H`$. The total contract is $`C=C_{\rm D}+C_{bc}+C_f+C_{bf}`$ with $`C_{bc}=\sum_x\lvert x\rangle\langle x\rvert\otimes\kappa xX`$ and $`C_{bf}=C^{(a)}_{bf}`$ or $`C^{(c)}_{bf}`$ as in the question, $`\gamma\in\mathbb R`$.

**Notation.** $`\Pi_x:=\lvert x\rangle\langle x\rvert\otimes\mathbb 1_2\otimes\mathbb 1_N`$; $`O:=\sigma_3\otimes(m\mathbb 1_N+D)`$ on the internal labels; $`A_x:=\frac\tau2\bigl(\lvert x+1\rangle\langle x\rvert\otimes(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert\otimes(i\sigma_1)\bigr)\otimes\mathbb 1_N`$, the bond $`(x,x+1)`$ of the motion term ($`A_x:=0`$ for an absent bond), so $`A=\sum_xA_x`$ and $`B=\sum_x\Pi_xO`$. $`d_k=\frac{2\pi k}{N\lambda_0}`$, $`\mu_k=m+d_k`$. The *rest* $`R`$ is the set of objects other than $`f`$, and $`H_R`$ the sum of the terms not involving $`f`$ (here $`R=\{b,c\}`$, $`H_R=C_{\rm D}+C_{bc}`$). $`\mathring Y:=Y-\frac{\mathrm{Tr}Y}{d}\mathbb 1`$ is the traceless part of an operator on a $`d`$-dimensional space; $`\lVert\cdot\rVert`$ is the operator norm, $`\lVert\cdot\rVert_1`$ the trace norm.

**Inputs** (04-ilang-time/05-moving-clock@v3, quoted in the question), with $`\lvert p\rangle=\sum_xe^{ipx}\lvert x\rangle`$: by (5.5) of 04-ilang-time/05-moving-clock,
```math
C_{\rm D}\bigl(\lvert p\rangle\otimes\beta\otimes\lvert f_k\rangle\bigr)=\lvert p\rangle\otimes C_k(p)\beta\otimes\lvert f_k\rangle,\qquad C_k(p)=-\tau\sin p\,\sigma_1+\mu_k\sigma_3 ;
```
by (5.6) of 04-ilang-time/05-moving-clock, $`C_k(p)`$ has the eigenvalues $`\pm\omega_k(p)`$, $`\omega_k=\sqrt{\mu_k^2+\tau^2\sin^2p}`$, with the real eigenvectors $`\beta_{k,+}=(\cos\frac{\theta_k}2,\sin\frac{\theta_k}2)^{T}`$, $`\beta_{k,-}=(-\sin\frac{\theta_k}2,\cos\frac{\theta_k}2)^{T}`$, $`\tan\theta_k(p)=-\tau\sin p/\mu_k`$, $`\lvert\theta_k\rvert<\frac\pi2`$.

**Half-gap.** $`M_k:=\mu_k=m+d_k`$. At $`\sin p=0`$ the two branches of level $`k`$ have the costs $`\pm M_k`$, so $`M_k`$ is the half-gap of the on-site block $`\mu_k\sigma_3`$. (The question names $`M_k`$ without quoting its definition; this is the one used here.)

**Assumptions.**
- S1. Product start $`\Psi(0)=\Psi_b\otimes\chi\otimes\varphi`$ (for the pair, $`\Psi_{12}\otimes\chi\otimes\varphi`$).
- S2. First order in the coupling at fixed $`\lambda`$, valid for $`\lVert C_{bf}\rVert\,\lvert\lambda\rvert\ll1`$ with the remainder (2.4).
- S3. Normalized plane waves: on a ring of $`n`$ sites (the periodic chain, $`p\in\frac{2\pi}{n}\mathbb Z`$, a chosen description, M8), where (5.5)–(5.6) hold verbatim for $`\lvert p\rangle_n:=n^{-1/2}\lvert p\rangle`$; on the open chain, normalized packets on one branch and level.
- S4. Items 2 and 3 at zeroth order in the records: $`\kappa=0`$ or $`X\chi=0`$; for $`\kappa>0`$ a bound is given in Step 5.
- S5. Pair: $`b_1,b_2`$ of Model D type with their own parameters $`(\tau_i,m_i,N_i,\lambda_{0,i})`$, $`M^{(i)}_{k}`$, both on the position labels $`x`$ of the $`\Phi_x`$; $`U=\sum_{x_1,x_2}\Pi^{(1)}_{x_1}\Pi^{(2)}_{x_2}\otimes u(x_1,x_2)`$, $`u(x_1,x_2)`$ self-adjoint on the internal labels of both bodies, with $`[U,D_i]=0`$ so that fixed clock levels form invariant subspaces.

## Derivation

### Step 1. The coupling as a sum over positions

Shifting the summation index in $`\sum_xA_x\otimes\frac12\Phi_{x+1}`$ gives $`\sum_xA_x\otimes\frac12(\Phi_x+\Phi_{x+1})=\sum_x\frac12(A_x+A_{x-1})\otimes\Phi_x`$. Both couplings therefore have the form
```math
C_{bf}=\gamma\sum_xQ_x\otimes\Phi_x,\qquad Q^{(a)}_x=\Pi_xO,\qquad Q^{(c)}_x=\Pi_xO+\tfrac12\bigl(A_x+A_{x-1}\bigr). \qquad\text{(2.1)}
```
Every $`A_x`$ enters $`Q_x`$ and $`Q_{x+1}`$ with weight $`\frac12`$; $`\mathrm{Tr}\sigma_3=0`$, and $`A_x`$ is off-diagonal in the position. Hence
```math
\sum_xQ^{(a)}_x=B,\qquad\sum_xQ^{(c)}_x=A+B=C_{\rm D},\qquad\mathrm{Tr}Q_x=0 . \qquad\text{(2.2)}
```
Since the $`\Pi_x`$ are orthogonal and $`\lVert O\rVert=\mu_{N-1}`$, $`\lVert C^{(a)}_{bf}\rVert=\lvert\gamma\rvert\mu_{N-1}\max_x\lVert\Phi_x\rVert`$. The $`A_x`$ with even (odd) $`x`$ act on disjoint pairs of sites and $`\lVert A_x\rVert=\tau/2`$, so $`\lVert C^{(c)}_{bf}\rVert\le\lvert\gamma\rvert(\mu_{N-1}+\tau)\max_x\lVert\Phi_x\rVert`$. Both bounds are independent of $`n`$.

### Step 2. Exact equation of the view of $`f`$

Let $`\rho=\lvert\Psi\rangle\langle\Psi\rvert`$ and $`V_f=\mathrm{Tr}_R\rho`$ (1.5). By (1.9), $`i\,\mathrm d\rho/\mathrm d\lambda=[C,\rho]`$. The partial trace over $`R`$ of a commutator with an operator on $`R`$ vanishes, and $`\mathrm{Tr}_R[\mathbb 1\otimes C_f,\rho]=[C_f,V_f]`$, so
```math
i\frac{\mathrm d}{\mathrm d\lambda}V_f=[C_f,V_f]+\mathrm{Tr}_R[C_{bf},\rho]\qquad\text{(exact)}.
```

### Step 3. First-order generator and remainder

Let $`\xi(\lambda):=e^{-iH_R\lambda}(\Psi_b\otimes\chi)`$ be the state of the rest at $`\gamma=0`$, $`V^0_b(\lambda)`$ its view on $`b`$, and $`\Delta:=\rho-\lvert\xi\rangle\langle\xi\rvert\otimes V_f`$. Since $`\mathrm{Tr}_R\bigl((Q_x\otimes\Phi_x)(\lvert\xi\rangle\langle\xi\rvert\otimes V_f)\bigr)=\langle\xi\vert Q_x\vert\xi\rangle\,\Phi_xV_f`$, Step 2 becomes
```math
i\frac{\mathrm d}{\mathrm d\lambda}V_f=[G_f(\lambda),V_f]+R_f(\lambda),\qquad G_f(\lambda)=C_f+\sum_xs_x(\lambda)\Phi_x,\qquad s_x(\lambda):=\gamma\langle\xi(\lambda)\vert Q_x\vert\xi(\lambda)\rangle=\gamma\mathrm{Tr}\bigl(Q_xV^0_b(\lambda)\bigr), \qquad\text{(2.3)}
```
with $`R_f=\mathrm{Tr}_R[C_{bf},\Delta]`$. The family $`s_x`$ is the source field; its total is $`S:=\sum_xs_x`$.

*Remainder.* $`\Psi^0(\lambda)=\xi(\lambda)\otimes e^{-iC_f\lambda}\varphi`$ is the evolution at $`\gamma=0`$. By Duhamel's formula, $`\Psi-\Psi^0=-i\int_0^\lambda e^{-iC(\lambda-\lambda')}C_{bf}\Psi^0(\lambda')\,\mathrm d\lambda'`$, so $`\lVert\Psi-\Psi^0\rVert\le\lVert C_{bf}\rVert\lvert\lambda\rvert`$. For unit vectors $`\lVert\psi\psi^\dagger-\phi\phi^\dagger\rVert_1\le2\lVert\psi-\phi\rVert`$, partial traces do not increase the trace norm, and $`\Delta=(\rho-\rho^0)-\lvert\xi\rangle\langle\xi\rvert\otimes(V_f-V^0_f)`$ with $`\rho^0=\lvert\xi\rangle\langle\xi\rvert\otimes V_f^0`$. Hence $`\lVert\Delta\rVert_1\le4\lVert C_{bf}\rVert\lvert\lambda\rvert`$ and
```math
\lVert R_f(\lambda)\rVert_1\le2\lVert C_{bf}\rVert\,\lVert\Delta\rVert_1\le8\lVert C_{bf}\rVert^2\lvert\lambda\rvert . \qquad\text{(2.4)}
```
The difference between $`V_f`$ and the evolution of $`V_f(0)`$ by the $`\lambda`$-dependent contract $`G_f`$ obeys the same equation with source $`R_f`$ and starts at zero; unitary conjugation preserves $`\lVert\cdot\rVert_1`$, so the difference is at most $`4\lVert C_{bf}\rVert^2\lambda^2`$. For the pair, $`C_{bf}\to C_{b_1f}+C_{b_2f}`$, $`s_x=\gamma_1\langle Q^{(1)}_x\rangle+\gamma_2\langle Q^{(2)}_x\rangle`$, with $`\xi`$ the state of $`R=\{b_1,b_2,c\}`$ at zero coupling; nothing else changes.

### Step 4. When the first-order generator is a contract of $`f`$ alone

With the spectral decomposition $`H_R=\sum_EE\,P_E`$ (finite, A1), $`\xi(\lambda)=\sum_Ee^{-iE\lambda}P_E\xi_0`$, $`\xi_0=\Psi_b\otimes\chi`$, and (2.3) becomes
```math
G_f(\lambda)=C_f+\sum_\nu e^{i\nu\lambda}\,\Gamma_\nu,\qquad\Gamma_\nu:=\gamma\sum_{E-E'=\nu}\ \sum_x\langle\xi_0\vert P_EQ_xP_{E'}\vert\xi_0\rangle\,\Phi_x . \qquad\text{(2.5)}
```
Exponentials with distinct real frequencies are linearly independent functions of $`\lambda\in\mathbb R`$ (A9; apply it to each matrix element). Hence $`G_f`$ is independent of $`\lambda`$ iff $`\Gamma_\nu=0`$ for every $`\nu\neq0`$, and then $`G_f=C_f+\Gamma_0`$. Two sufficient cases:
- a stationary start, $`\xi_0`$ in one eigenspace of $`H_R`$; for $`\kappa=0`$ or $`X\chi=0`$ this is $`\Psi_b`$ an eigenvector of $`C_{\rm D}`$, since then $`H_R(\psi\otimes\chi)=(C_{\rm D}\psi)\otimes\chi`$ for every $`\psi`$;
- $`\Phi_x=\Phi`$ for all $`x`$ in coupling (c) with $`\kappa=0`$ or $`X\chi=0`$, and any $`\Psi_b`$: then $`G_f=C_f+\gamma\langle C_{\rm D}\rangle\Phi`$ by (2.2), and $`\langle C_{\rm D}\rangle`$ is conserved. In (a), $`\langle B\rangle`$ is not conserved in general: for a superposition of the two branches at one $`p`$ with $`\sin p\ne0`$ it oscillates with frequency $`2\omega_k`$, because $`\langle\beta_{k,+}\vert\sigma_3\vert\beta_{k,-}\rangle=-\sin\theta_k\neq0`$.

*Control.* Take the ring (S3), $`\kappa=0`$, and the start $`\Psi_b=\frac1{\sqrt2}\bigl(\lvert p\rangle_n\otimes\beta_{k,+}(p)+\lvert0\rangle_n\otimes\beta_{k,+}(0)\bigr)\otimes\lvert f_k\rangle`$ with $`p\in\frac{2\pi}n\mathbb Z`$ and $`\sin p\neq0`$. The two components have the costs $`\omega_k(p)`$ and $`M_k`$. The required matrix elements are $`\langle0\vert_n\Pi_x\lvert p\rangle_n=e^{ipx}/n`$, $`\langle0\vert_n\frac12(A_x+A_{x-1})\lvert p\rangle_n=-\frac{\tau}{2n}\sin p\,e^{ipx}\sigma_1`$ (direct computation) and $`\beta_{k,+}(0)=(1,0)^{T}`$. They give
```math
s_x(\lambda)=\frac{\gamma}{2n}\Bigl(\langle\beta_{k,+}(p)\vert\hat Q\vert\beta_{k,+}(p)\rangle+M_k\Bigr)+\frac{\gamma g}{n}\cos\bigl(px-(\omega_k(p)-M_k)\lambda\bigr), \qquad\text{(2.6)}
```
with $`\hat Q=\mu_k\sigma_3`$, $`g^{(a)}=M_k\cos\frac{\theta_k}2`$ for (a) and $`\hat Q=C_k(p)`$, $`g^{(c)}=M_k\cos\frac{\theta_k}2-\frac\tau2\sin p\,\sin\frac{\theta_k}2`$ for (c). Both $`g`$ are positive, since $`\cos\frac{\theta_k}2>0`$ and $`\sin\frac{\theta_k}2`$ has the sign of $`-\sin p`$. Since $`\omega_k(p)>M_k`$, $`s_x`$ depends on $`\lambda`$, and $`G_f`$ depends on $`\lambda`$ whenever $`\sum_xe^{ipx}\Phi_x\neq0`$ (for example, when the $`\Phi_x`$ are linearly independent).

### Step 5. Total source of a branch start (item 2)

By (2.2), $`S=\gamma\langle B\rangle`$ for (a) and $`S=\gamma\langle C_{\rm D}\rangle`$ for (c). Both operators commute with the translations of the position label. By (5.5) they act on $`\lvert p\rangle\otimes\beta\otimes\lvert f_k\rangle`$ as $`\mu_k\sigma_3`$ and $`C_k(p)`$ on $`\beta`$ ($`B`$ is diagonal in $`x`$, and $`O\lvert f_k\rangle=\mu_k\sigma_3\lvert f_k\rangle`$). For the branch $`\sigma\in\{+1,-1\}`$, (5.6) gives $`\langle\beta_{k,\sigma}\vert\sigma_3\vert\beta_{k,\sigma}\rangle=\sigma(\cos^2\frac{\theta_k}2-\sin^2\frac{\theta_k}2)=\sigma\cos\theta_k=\sigma M_k/\omega_k`$ (because $`\lvert\theta_k\rvert<\frac\pi2`$) and $`\langle\beta_{k,\sigma}\vert C_k\vert\beta_{k,\sigma}\rangle=\sigma\omega_k`$. For the branch start $`\lvert p\rangle_n\otimes\beta_{k,\sigma}(p)\otimes\lvert f_k\rangle`$ (S3) this gives
```math
S^{(a)}_{k,\sigma}(p)=\gamma\sigma\frac{M_k^2}{\omega_k(p)}=\frac{\gamma\sigma M_k^2}{\sqrt{M_k^2+\tau^2\sin^2p}},\qquad S^{(c)}_{k,\sigma}(p)=\gamma\sigma\,\omega_k(p)=\gamma\sigma\sqrt{M_k^2+\tau^2\sin^2p}, \qquad\text{(2.7)}
```
uniformly distributed, $`s_x=S/n`$. With $`L_b:=\langle C_{\rm D}\rangle=\sigma\omega_k(p)`$, the cost of the body's own term in the start,
```math
S^{(c)}_{k,\sigma}=\gamma L_b,\qquad S^{(a)}_{k,\sigma}=\gamma\frac{M_k^2}{L_b}=\gamma L_b\Bigl(\frac{M_k}{\omega_k(p)}\Bigr)^2. \qquad\text{(2.8)}
```
With $`\kappa=0`$ or $`X\chi=0`$, $`\xi(\lambda)=e^{-i\sigma\omega_k\lambda}\xi_0`$, so (2.7) holds at every $`\lambda`$, and $`G_f`$ is $`\lambda`$-independent (Step 4). A normalized packet $`\int g(p)\lvert p\rangle\otimes\beta_{k,\sigma}(p)\otimes\lvert f_k\rangle\frac{\mathrm dp}{2\pi}`$ on one branch and level stays on that branch, and both operators are block-diagonal in $`p`$. Its total source is therefore $`\int\lvert g\rvert^2S_{k,\sigma}(p)\frac{\mathrm dp}{2\pi}`$, constant in $`\lambda`$. For $`\kappa>0`$ and $`X\chi\neq0`$, Duhamel's formula between $`H_R`$ and $`C_{\rm D}`$ gives $`\lvert S(\lambda)-S(0)\rvert\le2\lvert\gamma\rvert\,\lVert\sum_xQ_x\rVert\int_0^{\lvert\lambda\rvert}\lVert C_{bc}\,\xi^0(\lambda')\rVert\,\mathrm d\lambda'`$, where $`\xi^0`$ is the evolution at $`\kappa=0`$. This correction is of first order in $`\kappa`$ at fixed $`\lambda`$.

**Dependence.** $`S_{k,\sigma}(p)`$ is odd in $`\sigma`$. It depends on $`p`$ only through $`\sin^2p`$, and on $`k`$ only through $`M_k=m+\frac{2\pi k}{N\lambda_0}`$. As $`\sin^2p`$ goes from $`0`$ to $`1`$, $`\lvert S^{(a)}\rvert`$ decreases from $`\lvert\gamma\rvert M_k`$ to $`\lvert\gamma\rvert M_k^2/\sqrt{M_k^2+\tau^2}`$, while $`\lvert S^{(c)}\rvert`$ increases from $`\lvert\gamma\rvert M_k`$ to $`\lvert\gamma\rvert\sqrt{M_k^2+\tau^2}`$. Both moduli increase with $`M_k`$.

### Step 6. Bound pair (item 3)

Take $`\Psi_{12}`$ an eigenvector of the pair contract $`C_{\rm pair}:=C_{{\rm D},1}+C_{{\rm D},2}+U`$ with eigenvalue $`E_{12}`$ (the cost of the pair), on the clock levels $`(k_1,k_2)`$ (S5), with $`\kappa=0`$. The start is stationary, so $`G_f`$ is $`\lambda`$-independent (Step 4). By Step 3 and (2.2), $`S=\gamma_1\langle\sum_xQ^{(1)}_x\rangle+\gamma_2\langle\sum_xQ^{(2)}_x\rangle`$. On level $`k_i`$, $`B_i`$ acts as $`M^{(i)}_{k_i}\sigma^{(i)}_3`$, and $`\langle C_{{\rm D},1}\rangle+\langle C_{{\rm D},2}\rangle=E_{12}-\langle U\rangle`$. Therefore
```math
S^{(a)}_{12}=\gamma_1M^{(1)}_{k_1}\langle\sigma^{(1)}_3\rangle+\gamma_2M^{(2)}_{k_2}\langle\sigma^{(2)}_3\rangle,\qquad S^{(c)}_{12}=\gamma_1\langle C_{{\rm D},1}\rangle+\gamma_2\langle C_{{\rm D},2}\rangle\ \overset{\gamma_1=\gamma_2=\gamma}{=}\ \gamma\bigl(E_{12}-\langle U\rangle\bigr), \qquad\text{(2.9)}
```
where the expectation values are taken in $`\Psi_{12}`$. $`U`$ contributes no term of its own: the binding enters only through the state. The total is exactly the sum of what the two parts present in the joint state, because $`\sum_xQ_x`$ is a sum of one-body operators.

*Control.* Take $`U=u\,\sigma^{(1)}_1\sigma^{(2)}_1`$ ($`u\in\mathbb R`$, $`u\neq0`$, identity in positions and clocks), the ring with $`p_1=p_2=0`$, and levels $`(k_1,k_2)`$. By (5.5), $`C_{k}(0)=\mu_k\sigma_3`$ and $`\langle A_i\rangle=0`$, so (a) and (c) coincide. Put $`M:=M^{(1)}_{k_1}+M^{(2)}_{k_2}`$. On $`{\rm span}\{\lvert{\uparrow\uparrow}\rangle,\lvert{\downarrow\downarrow}\rangle\}`$, $`C_{\rm pair}`$ is $`\begin{pmatrix}M&u\\u&-M\end{pmatrix}`$. Its upper eigenvector $`(\cos\frac\phi2,\sin\frac\phi2)`$, $`\tan\phi=u/M`$, $`\lvert\phi\rvert<\frac\pi2`$, has $`\langle\sigma^{(i)}_3\rangle=\cos\phi`$ and $`\langle\sigma^{(1)}_1\sigma^{(2)}_1\rangle=\sin\phi`$, hence
```math
E_{12}=\sqrt{M^2+u^2},\qquad\langle U\rangle=\frac{u^2}{E_{12}},\qquad S_{12}=\bigl(\gamma_1M^{(1)}_{k_1}+\gamma_2M^{(2)}_{k_2}\bigr)\frac{M}{\sqrt{M^2+u^2}} . \qquad\text{(2.10)}
```
The free parts in the same branch, level and $`p=0`$ present $`\gamma_iM^{(i)}_{k_i}`$ (2.7). So $`S_{12}`$ differs from the sum of the free sources whenever $`u\neq0`$ and $`\gamma_1M^{(1)}_{k_1}+\gamma_2M^{(2)}_{k_2}\neq0`$, while $`E_{12}`$ exceeds the sum $`M`$ of the free costs. The same block, with $`u=u(x_1,x_2)`$, arises for held bodies at fixed positions (A15).

### Step 7. Replacements that leave $`C`$ unchanged (item 4)

Every operator $`Y`$ on $`\mathcal H_b\otimes\mathcal H_c\otimes\mathcal H_f`$ has a unique decomposition $`Y=\sum_{S\subseteq\{b,c,f\}}Y_S`$, in which $`Y_S`$ acts as the identity outside $`S`$ and is traceless in every object of $`S`$. (Expand in product bases of $`\{\mathbb 1\}\cup\{\text{traceless}\}`$; this is linear algebra, M5.) A term on the pair $`\{o,o'\}`$ has components only for $`S\subseteq\{o,o'\}`$. Let two listings with one term per pair give the same $`C`$. The component on a two-object set $`\{o,o'\}`$ comes only from the difference of the two $`\{o,o'\}`$ terms, so that difference has no two-object component. The single-object components of the differences add up to zero for each object, up to constants whose total is zero. Hence the replacements that leave $`C`$ unchanged are exactly
```math
\begin{aligned}&C_{\rm D}\to C_{\rm D}+Z^{\rm D}_b,\quad C_{bc}\to C_{bc}+Z^{bc}_b+Z^{bc}_c,\quad C_{bf}\to C_{bf}+Z^{bf}_b+Z^{bf}_f,\quad C_f\to C_f+Z^{f}_f,\quad C_{cf}:=Z^{cf}_c+Z^{cf}_f,\\&Z^{\rm D}_b+Z^{bc}_b+Z^{bf}_b=0,\qquad Z^{bc}_c+Z^{cf}_c=0,\qquad Z^{f}_f+Z^{bf}_f+Z^{cf}_f=0\quad(\text{up to constants of total zero}),\end{aligned} \qquad\text{(2.11)}
```
where $`Z^{\cdot}_o`$ is any self-adjoint operator on $`\mathcal H_o`$: a constant, a place-dependent operator such as $`\sum_xz_x\Pi_x`$, or an internal operator. $`C_{cf}`$ is a new $`c`$–$`f`$ term, absent from the listing. In words, the only freedom is to move single-object operators between the terms that contain the object. The two-object components $`C_{\{b,c\}}`$ and $`C_{\{b,f\}}`$ are fixed by $`C`$. By (2.2), $`\mathrm{Tr}Q_x=0`$, so $`C_{\{b,f\}}=\gamma\sum_xQ_x\otimes\mathring\Phi_x`$, and the trace parts of the $`\Phi_x`$ give the single-$`b`$ operator $`\gamma\sum_x\frac{\mathrm{Tr}\Phi_x}{d_f}Q_x`$.

### Step 8. What the total contract fixes

*Generator.* For $`C=H_R\otimes\mathbb 1+\mathbb 1\otimes C_f+C_{bf}`$, $`\mathrm{Tr}_R\bigl((\lvert\xi\rangle\langle\xi\rvert\otimes\mathbb 1)C\bigr)=\langle H_R\rangle\mathbb 1+G_f`$, so
```math
G_f(\lambda)\equiv\mathrm{Tr}_R\bigl((\lvert\xi(\lambda)\rangle\langle\xi(\lambda)\rvert\otimes\mathbb 1_f)\,C\bigr)\pmod{\mathbb 1_f}. \qquad\text{(2.12)}
```
Only the multiple of $`\mathbb 1_f`$ drops out of $`[G_f,V_f]`$. The right side uses $`C`$ and $`\xi`$. Moves (2.11) inside $`H_R`$ (between $`C_{\rm D}`$ and $`C_{bc}`$) leave $`\xi`$ unchanged. A move of an $`O(\gamma)`$ operator between $`C_{bf}`$ and $`H_R`$ changes $`\xi`$ by $`O(\gamma\lvert\lambda\rvert)`$ and $`G_f`$ by $`O(\gamma^2\lvert\lambda\rvert)`$, which lies inside (2.4). So $`G_f`$ modulo $`\mathbb 1_f`$ is well defined to first order. For two starts of the same description, the difference is $`G_f-G'_f\equiv\sum_x(s_x-s'_x)\mathring\Phi_x`$.

*Split.* A move $`Z^{bf}_f=-Z^f_f`$ leaves $`G_f`$ unchanged. It shifts the part $`\sum_xs_x\Phi_x`$ that the listing attributes to the body by the state-independent operator $`Z^{bf}_f`$. For $`Z^{bf}_f=\sum_x\zeta_x\mathring\Phi_x`$ this is $`s_x\to s_x+\zeta_x`$, with the body operator $`Q_x\to Q_x+\frac{\zeta_x}{\gamma}\mathbb 1_b`$. Without a rule that fixes the form of the body operator, the source field is therefore fixed only up to state-independent shifts.

*Rule: the form (a) or (c).* Read the source from a listing whose $`b`$–$`f`$ term has the form (a), resp. (c), with $`O`$ replaced by $`a'O+c_0`$ and with $`\mathring\Phi_x`$ unchanged up to one common factor. Assume $`\gamma\neq0`$ and $`\mathring\Phi_y\neq0`$ for some $`y`$. Two such listings of the same $`C`$ differ in $`C_{\{b,f\}}`$ by the two-object component of $`\gamma\sum_x\Pi_x\bigl((a'-1)O+c_0\bigr)\otimes\mathring\Phi_x`$, which (2.11) requires to vanish. Taking $`\mathrm{Tr}_f`$ removes the single-$`b`$ part, since $`\mathring\Phi_x`$ is traceless. Multiplying by $`\Pi_y\otimes\mathbb 1`$ then gives $`((a'-1)O+c_0)\otimes\mathring\Phi_y=\mathbb 1\otimes\mathring Z`$ for every $`y`$, for one traceless $`\mathring Z`$ on $`\mathcal H_f`$. Since $`O`$ is not a multiple of $`\mathbb 1`$, $`a'=1`$, and then $`c_0\mathring\Phi_y=\mathring Z`$ for all $`y`$. Conversely, if all $`\mathring\Phi_x`$ are equal, $`c_0\sum_x\Pi_x\otimes\mathring\Phi=c_0\mathbb 1_b\otimes\mathring\Phi`$ is a single-$`f`$ operator, which can be moved into $`C_f`$. Hence
```math
\text{a constant }c_0\neq0\text{ added to }\sigma_3\otimes(m\mathbb 1_N+D)\text{ leaves }C\text{ unchanged (after moves (2.11))}\iff\mathring\Phi_x=\mathring\Phi_y\ \text{for all }x,y . \qquad\text{(2.13)}
```
The only remaining refactorization is $`(\gamma_i,\Phi_x)\to(\gamma_i/a,\,a\Phi_x)`$, common to all bodies coupled to the same $`\Phi_x`$: one $`\gamma`$ multiplies the same $`O`$ at every $`x`$. It changes no term and multiplies every source by $`1/a`$. When the zero is fixed, $`s_x=\gamma\langle Q_x\rangle`$ is thus fixed by $`C`$ and the state, up to this common factor. When the zero is a convention, $`s_x\to s_x+\gamma c_0\langle\Pi_x\rangle`$ and $`S\to S+\gamma c_0`$ for every normalized state, with $`c_0`$ chosen independently for each body. Differences between two starts of one body change by $`\gamma c_0(\langle\Pi_x\rangle-\langle\Pi_x\rangle')`$, which sums to zero over $`x`$. This gives
```math
\begin{aligned}&\text{if }\exists\,x,y:\ \mathring\Phi_x\neq\mathring\Phi_y:\ s_x,\ S\text{ and the ratios }s^{(1)}_x/s^{(2)}_x,\ S_1/S_2\text{ are fixed by }C\text{ and the state, up to the common factor }1/a\ (\text{ratios exactly});\\&\text{if all }\mathring\Phi_x\text{ are equal: the family }s_x,\ S\text{ and the ratios are not fixed }(S\to S+\gamma c_0,\ c_0\text{ free for each body});\ \text{differences }S-S'\text{ between starts of one body are, up to }1/a.\end{aligned} \qquad\text{(2.14)}
```
The relation (2.8) of $`S`$ to the cost is a relation to the listed $`C_{\rm D}`$: a move $`Z^{\rm D}_b`$, a constant included, changes $`L_b`$ but not $`S`$. So $`S^{(c)}=\gamma L_b`$ holds in the listing where the body's own term equals $`\sum_xQ^{(c)}_x`$. This is consistent with M6: the cost of a single object is not well defined.

## Result

Class throughout: the setting of the question (Model D body, medium with $`K_x=\kappa xX`$, field object of any finite type with any $`C_f`$ and $`\Phi_x`$, coupling (a) or (c)); further conditions are stated per item. All of these are chosen descriptions (M8).

1. **(2.1), (2.2)** (definition, exact). Both couplings are $`C_{bf}=\gamma\sum_xQ_x\otimes\Phi_x`$ with $`Q^{(a)}_x=\Pi_xO`$ and $`Q^{(c)}_x=\Pi_xO+\frac12(A_x+A_{x-1})`$. They satisfy $`\sum_xQ^{(a)}_x=B`$, $`\sum_xQ^{(c)}_x=C_{\rm D}`$ and $`\mathrm{Tr}Q_x=0`$.
2. **(2.3)** (formula; every product start $`\Psi_b\otimes\chi\otimes\varphi`$; first order in $`\gamma`$ at fixed $`\lambda`$). The view of $`f`$ obeys $`i\,\mathrm dV_f/\mathrm d\lambda=[G_f(\lambda),V_f]+R_f`$, with $`G_f=C_f+\sum_xs_x(\lambda)\Phi_x`$. The source field is $`s_x(\lambda)=\gamma\langle\xi(\lambda)\vert Q_x\vert\xi(\lambda)\rangle`$, where $`\xi(\lambda)=e^{-iH_R\lambda}(\Psi_b\otimes\chi)`$ is the state of the rest at zero coupling. For the pair, $`s_x=\gamma_1\langle Q^{(1)}_x\rangle+\gamma_2\langle Q^{(2)}_x\rangle`$.
3. **(2.4)** (theorem; same class; every $`\lambda`$). $`\lVert R_f(\lambda)\rVert_1\le8\lVert C_{bf}\rVert^2\lvert\lambda\rvert`$, with $`\lVert C_{bf}\rVert\le\lvert\gamma\rvert(\mu_{N-1}+\tau)\max_x\lVert\Phi_x\rVert`$ for both couplings, independently of $`n`$. The view differs from its evolution under $`G_f`$ by at most $`4\lVert C_{bf}\rVert^2\lambda^2`$ in trace norm. The first-order generator is accurate for $`\lVert C_{bf}\rVert\lvert\lambda\rvert\ll1`$.
4. **(2.5)** (criterion; same class). $`G_f`$ is independent of $`\lambda`$, hence a contract of $`f`$ alone, iff $`\Gamma_\nu=0`$ for every Bohr frequency $`\nu\neq0`$ of $`H_R`$. This holds for every start in one eigenspace of $`H_R`$ (for $`\kappa=0`$ or $`X\chi=0`$: $`\Psi_b`$ an eigenvector of $`C_{\rm D}`$). In coupling (c) with $`\Phi_x=\Phi`$ for all $`x`$ and $`\kappa=0`$ or $`X\chi=0`$, it holds for every start.
5. **(2.6)** (example, control of item 1). On a ring with $`\kappa=0`$, take the start $`\frac1{\sqrt2}(\lvert p\rangle_n\beta_{k,+}(p)+\lvert0\rangle_n\beta_{k,+}(0))\lvert f_k\rangle`$ with $`\sin p\neq0`$. Its source field oscillates with frequency $`\omega_k(p)-M_k`$ in both couplings, so $`G_f`$ depends on $`\lambda`$ whenever $`\sum_xe^{ipx}\Phi_x\neq0`$.
6. **(2.7)** (formula; branch start of branch $`\sigma=\pm1`$, level $`k`$, label $`p`$ on a ring; zeroth order in the records, $`\kappa=0`$ or $`X\chi=0`$; first order in $`\gamma`$). The total sources are $`S^{(a)}_{k,\sigma}(p)=\gamma\sigma M_k^2/\omega_k(p)`$ and $`S^{(c)}_{k,\sigma}(p)=\gamma\sigma\omega_k(p)`$, constant in $`\lambda`$ and uniform in $`x`$. Both are odd in $`\sigma`$ and depend on $`p`$ only through $`\sin^2p`$. As $`\sin^2p`$ goes from $`0`$ to $`1`$, $`\lvert S^{(a)}\rvert`$ decreases from $`\lvert\gamma\rvert M_k`$, while $`\lvert S^{(c)}\rvert`$ increases from $`\lvert\gamma\rvert M_k`$. Both depend on $`k`$ only through $`M_k`$, and their moduli increase with it. For a packet on one branch and level, $`S`$ is the $`\lvert g(p)\rvert^2`$-average of (2.7). For $`\kappa>0`$, $`X\chi\neq0`$, the correction is of first order in $`\kappa`$ at fixed $`\lambda`$, with the bound of Step 5.
7. **(2.8)** (formula; same conditions as (2.7)). $`S^{(c)}=\gamma L_b`$ and $`S^{(a)}=\gamma M_k^2/L_b`$, with $`L_b=\langle C_{\rm D}\rangle=\sigma\omega_k(p)`$. This is a relation to the listed body term: it holds in the listing in which the body's own term is $`\sum_xQ_x`$, and a move (2.11) of a single-body operator $`Z^{\rm D}_b`$ into $`C_{\rm D}`$ changes $`L_b`$ by $`\langle Z^{\rm D}_b\rangle`$ but does not change $`S`$.
8. **(2.9)** (formula; every eigenvector of $`C_{\rm pair}`$ on fixed levels, every binding of the form S5; $`\kappa=0`$; first order in $`\gamma_i`$). The total source of the pair is $`S^{(a)}_{12}=\sum_i\gamma_iM^{(i)}_{k_i}\langle\sigma^{(i)}_3\rangle`$ and $`S^{(c)}_{12}=\sum_i\gamma_i\langle C_{{\rm D},i}\rangle`$; for $`\gamma_1=\gamma_2=\gamma`$, $`S^{(c)}_{12}=\gamma(E_{12}-\langle U\rangle)`$. The binding term contributes no term of its own, and the total is exactly the sum of what the parts present in the joint state.
9. **(2.10)** (example, control of item 3; $`U=u\sigma^{(1)}_1\sigma^{(2)}_1`$, $`p_1=p_2=0`$ on a ring, or held bodies). The pair presents $`(\gamma_1M^{(1)}_{k_1}+\gamma_2M^{(2)}_{k_2})M/\sqrt{M^2+u^2}`$. This differs from the sum of the free sources whenever $`u\neq0`$ and $`\gamma_1M^{(1)}_{k_1}+\gamma_2M^{(2)}_{k_2}\neq0`$, while its cost $`\sqrt{M^2+u^2}`$ exceeds $`M`$.
10. **(2.11)** (theorem; whole setting). The replacements that leave $`C`$ unchanged are exactly the moves of single-object operators (constants, place-dependent and internal operators) between the terms that contain the object, including a new $`c`$–$`f`$ term. The two-object components, in particular $`C_{\{b,f\}}=\gamma\sum_xQ_x\otimes\mathring\Phi_x`$, are fixed by $`C`$.
11. **(2.12)** (theorem; first order in $`\gamma`$). $`G_f`$ modulo $`\mathbb 1_f`$ is fixed by $`C`$ and the start. So is its change between two starts, $`\sum_x(s_x-s'_x)\mathring\Phi_x`$. The split of $`G_f`$ into $`C_f`$ and a body part is not fixed: without a rule for the form of the body operator, $`s_x`$ is fixed only up to state-independent shifts.
12. **(2.13)** (criterion; couplings (a), (c) with $`\gamma\neq0`$ and some $`\mathring\Phi_y\neq0`$). A constant added to $`\sigma_3\otimes(m\mathbb 1_N+D)`$ is a convention iff all $`\mathring\Phi_x`$ are equal (the field does not resolve positions). Otherwise the zero of the body operator is fixed by $`C`$.
13. **(2.14)** (criterion; same conditions, reading the source from a listing of form (a) or (c)). If some $`\mathring\Phi_x\neq\mathring\Phi_y`$, then the source field, its total and its value relative to another body coupled to the same $`\Phi_x`$ are well defined. The first two are fixed up to one factor $`1/a`$ (the normalization of the $`\Phi_x`$) that is common to all bodies; the ratios are fixed exactly where the denominator is nonzero. If all $`\mathring\Phi_x`$ are equal, none of the three is well defined, since $`S\to S+\gamma c_0`$ with $`c_0`$ free for each body. What is then well defined are the differences $`S-S'`$ between two starts of one body (up to $`1/a`$) and the ratios of such differences.

## Consistency checks

1. **Dimensions.** $`\tau`$, $`m`$, $`d_k`$, $`\omega_k`$ and $`C`$ have the unit of $`1/\lambda`$. $`s_x\Phi_x`$ has the unit of $`\gamma\Phi_x\cdot O`$, the same as $`C_{bf}`$, so $`G_f`$ has the unit of $`C`$. In (2.4), $`\lVert C_{bf}\rVert^2\lvert\lambda\rvert`$ has the unit of $`C`$, like $`[G_f,V_f]`$. In (2.7)–(2.10), $`S`$ has the unit of $`\gamma M_k`$. Passed.
2. **Body without motion, $`\tau\to0`$.** $`\omega_k\to M_k`$, $`\theta_k\to0`$ and $`Q^{(c)}_x\to Q^{(a)}_x`$. Both lines of (2.7) give $`\gamma\sigma M_k`$, (2.8) gives $`\gamma M_k^2/L_b=\gamma L_b`$, and the two forms of (2.9) coincide. Passed.
3. **Sum over both branches.** $`S_{k,+}(p)+S_{k,-}(p)=0`$ in both couplings. This equals $`\gamma`$ times the trace of the $`2\times2`$ block ($`\mu_k\sigma_3`$ resp. $`C_k(p)`$) and agrees with $`\mathrm{Tr}Q_x=0`$ in (2.2). Passed.

## Open issues

- $`M_k`$ is taken as $`\mu_k=m+d_k`$, the half-gap of the on-site block; the question does not quote its definition.
- Normalized branch starts are taken on a ring or as packets; boundary corrections for long open chains are not estimated.
- With records ($`\kappa>0`$, $`X\chi\neq0`$) only a bound on the change of the total source is given; the $`O(\kappa)`$ correction itself is not computed.
- The common factor $`1/a`$ (normalization of the $`\Phi_x`$) and which field descriptions fix it are left to the packages on the field's response and profile.
- For the pair, only eigenvectors of the pair contract and one control are treated; there is no general relation between the pair's source and those of its free parts.

## Methods used

- von Neumann equation for the view (partial trace)
- first-order (mean-field) perturbation theory at fixed $`\lambda`$; Duhamel formula; trace-norm bounds
- spectral decomposition; linear independence of exponentials
- plane-wave block diagonalization; two-level eigenproblem
- decomposition of operators on tensor products into traceless components
